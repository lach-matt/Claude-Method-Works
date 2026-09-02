#!/usr/bin/env python3
"""Turn a huge Claude ``conversations.json`` export into something git can hold.

A Claude data export is one enormous JSON document -- the copies in this repo's
Drive folder are 388,264,753 bytes (370 MiB) each.  GitHub hard-limits a single
file to 100 MB, so the export cannot enter the repository as an ordinary git
object.  This script offers the two ways out:

**shard** (the default) writes one small JSON file per conversation, grouped into
``YYYY-MM`` subdirectories taken from each conversation's creation date, plus an
``INDEX.tsv`` and a ``SUMMARY.json``.  Many small readable files are what a
code-graph indexer such as Graphify can actually use; one 370 MiB blob is not.

**--gzip** writes a single ``<name>.json.gz`` instead.  JSON compresses roughly
ten to one, so a 370 MiB export should land near 35 MiB, under the GitHub limit.
The script measures the real ratio and refuses to leave a file behind if the
result is still over 100 MB, pointing at sharding instead.

Typical use::

    python3 tools/shard_conversations.py conversations.json --dry-run
    python3 tools/shard_conversations.py conversations.json --out drive/chats
    python3 tools/shard_conversations.py conversations.json --gzip --out drive/chats

Memory: if `ijson <https://pypi.org/project/ijson/>`_ is importable the input is
parsed as a stream and memory stays flat no matter how large the file is.  Without
it the script falls back to ``json.load``, which needs roughly 4-8x the file size
in RAM (about 3 GB for a 370 MiB export); that fallback always announces itself
on stderr, it never happens silently.  ``--gzip`` never parses at all, so it is
safe on any input regardless of ijson.

Nothing about the export's shape is assumed.  The top level may be a JSON array
of conversations or an object wrapping one (``{"conversations": [...]}``), and the
per-conversation key names (``uuid``/``id``, ``name``/``title``,
``chat_messages``/``messages``, ...) are detected from the data.  When nothing
recognisable is found the script says which keys it *did* see and stops, rather
than raising a KeyError or writing garbage.

Exit codes: 0 success, 1 refusal or failed verification, 2 bad arguments.
"""

from __future__ import annotations

import argparse
import dataclasses
import decimal
import gzip
import io
import json
import logging
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence, Set, Tuple

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #

#: GitHub rejects any single file larger than this, on push, with no override.
GITHUB_FILE_LIMIT_BYTES = 100 * 1024 * 1024

#: Tens of thousands of tiny files is its own problem for git; raise with
#: --max-files when that really is what you want.
DEFAULT_MAX_FILES = 5000

INDEX_NAME = "INDEX.tsv"
SUMMARY_NAME = "SUMMARY.json"
UNDATED_DIR = "undated"

INDEX_COLUMNS: Tuple[str, ...] = (
    "shard_path",
    "conversation_id",
    "title",
    "created_at",
    "updated_at",
    "message_count",
    "bytes",
)

#: Candidate key names, in order of preference.  Claude exports have used the
#: first of each group; the rest are defensive.
ID_KEYS: Tuple[str, ...] = ("uuid", "id", "conversation_id", "conversationId", "chat_id")
TITLE_KEYS: Tuple[str, ...] = ("name", "title", "summary", "subject")
CREATED_KEYS: Tuple[str, ...] = ("created_at", "createdAt", "create_time", "created", "created_on")
UPDATED_KEYS: Tuple[str, ...] = ("updated_at", "updatedAt", "update_time", "updated", "modified_at")
MESSAGE_KEYS: Tuple[str, ...] = ("chat_messages", "messages", "chatMessages", "turns", "events")

#: When the document is an object rather than an array, these key names win if
#: present; otherwise the first top-level key holding an array is used.
CONTAINER_KEYS: Tuple[str, ...] = ("conversations", "chats", "data", "items", "records")

#: How many conversations to look at before deciding on the key names.
SCHEMA_SAMPLE_SIZE = 8

#: Bytes of input compressed to estimate the ratio during ``--gzip --dry-run``.
GZIP_SAMPLE_BYTES = 64 * 1024 * 1024
COPY_CHUNK_BYTES = 4 * 1024 * 1024
GZIP_LEVEL = 9

MAX_COMPONENT_CHARS = 120
UNSAFE_CHARS = re.compile(r"[^A-Za-z0-9._-]+")

#: Every C0 and C1 control character.  A NUL in a conversation title would make
#: git treat INDEX.tsv as binary, killing diffs on the one file the shards exist
#: to make readable, so no control character reaches a TSV field.
CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f-\x9f]")

#: Lone UTF-16 surrogates occur in real chat exports and cannot be encoded as
#: UTF-8 at all; ``serialise`` escapes them rather than dying mid-write.
SURROGATES = re.compile(r"[\ud800-\udfff]")

LOGGER = logging.getLogger("shard_conversations")


class ExportError(Exception):
    """The input is not a Claude export shape this tool can handle."""


class StreamingUnsupported(ExportError):
    """ijson cannot represent something in this document, but ``json.load`` can.

    Raised only for inputs the in-memory parser reads losslessly (a JSON integer
    wider than 64 bits, say).  ``main`` catches it and re-runs with ``json.load``
    instead of failing; it never reaches the user as an error.
    """


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #


def clean_field(value: Any) -> str:
    """Make a value safe for a tab-separated field: no control characters at all.

    Tabs and newlines would break the row; a NUL would make git call INDEX.tsv a
    binary file; the rest of the C0/C1 range confuses TSV readers.  All of them
    become a space.
    """
    text = "" if value is None else str(value)
    return CONTROL_CHARS.sub(" ", text).strip()


def human_bytes(count: float) -> str:
    step = float(count)
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if abs(step) < 1024.0 or unit == "TiB":
            if unit == "B":
                return "{:.0f} B".format(step)
            return "{:.1f} {}".format(step, unit)
        step /= 1024.0
    return "{:.1f} TiB".format(step)  # pragma: no cover - unreachable


def sanitize_component(raw: str, fallback: str) -> str:
    """Turn arbitrary text into one safe, portable path component."""
    text = UNSAFE_CHARS.sub("-", str(raw))
    previous = None
    while previous != text:
        previous = text
        text = text.strip("-. ")
    if len(text) > MAX_COMPONENT_CHARS:
        text = text[:MAX_COMPONENT_CHARS].rstrip("-. ")
    if not text or text in (".", ".."):
        return fallback
    return text


def parse_timestamp(value: Any) -> Optional[datetime]:
    """Best-effort timestamp parse; ``None`` when the value is unusable.

    Handles ISO 8601 with or without ``Z``/offset/fractional seconds, plain
    dates, and epoch seconds or milliseconds given as a number.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float, decimal.Decimal)):
        seconds = float(value)
        if seconds > 1e11:  # milliseconds
            seconds /= 1000.0
        try:
            return datetime.fromtimestamp(seconds, tz=timezone.utc)
        except (OverflowError, OSError, ValueError):
            return None
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                parsed = datetime.strptime(value.strip(), fmt)
                break
            except ValueError:
                continue
        else:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def month_directory(value: Any) -> str:
    """``YYYY-MM`` for a usable timestamp, ``undated`` otherwise."""
    parsed = parse_timestamp(value)
    return UNDATED_DIR if parsed is None else parsed.strftime("%Y-%m")


def remove_quietly(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass
    except OSError as exc:  # pragma: no cover - best effort cleanup
        LOGGER.debug("could not remove %s: %s", path, exc)


def write_text_atomically(path: Path, text: str) -> int:
    """Write ``text`` via a sibling temp file and an atomic rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="\n",
        dir=str(path.parent),
        prefix=".shard-conversations-",
        delete=False,
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            handle.write(text)
        size = temp_path.stat().st_size
        # NamedTemporaryFile is 0600; these files are meant to be committed.
        os.chmod(str(temp_path), 0o644)
        os.replace(str(temp_path), str(path))
        return size
    except BaseException:
        remove_quietly(temp_path)
        raise


# --------------------------------------------------------------------------- #
# Schema detection
# --------------------------------------------------------------------------- #


@dataclasses.dataclass(frozen=True)
class Schema:
    """Which key names this particular export actually uses."""

    container_key: Optional[str]
    id_key: Optional[str]
    title_key: Optional[str]
    created_key: Optional[str]
    updated_key: Optional[str]
    messages_key: Optional[str]

    def as_dict(self) -> Dict[str, Optional[str]]:
        return {
            "container_key": self.container_key,
            "id_key": self.id_key,
            "title_key": self.title_key,
            "created_key": self.created_key,
            "updated_key": self.updated_key,
            "messages_key": self.messages_key,
        }

    def describe(self) -> str:
        used = ", ".join(
            "{}={}".format(name, value)
            for name, value in self.as_dict().items()
            if value is not None
        )
        return used or "none detected"


def first_present(
    record: Dict[str, Any], preferred: Optional[str], candidates: Sequence[str]
) -> Tuple[Optional[str], Any]:
    """Return the first key of ``candidates`` present in ``record``, plus value.

    The schema's detected key is tried first so a mixed export still resolves
    consistently, then the remaining candidates as a per-record fallback.
    """
    order: List[str] = []
    if preferred:
        order.append(preferred)
    order.extend(key for key in candidates if key != preferred)
    for key in order:
        if key in record and record[key] is not None:
            return key, record[key]
    return None, None


def detect_schema(samples: Sequence[Any], container_key: Optional[str]) -> Schema:
    """Work out the key names from the first few conversations.

    Raises ``ExportError`` -- naming the keys that were actually seen -- when the
    records look nothing like conversations.
    """
    dict_samples = [item for item in samples if isinstance(item, dict)]
    if samples and not dict_samples:
        kinds = sorted({type(item).__name__ for item in samples})
        raise ExportError(
            "the export's list holds {} values, not conversation objects; "
            "this does not look like a Claude conversations export".format("/".join(kinds))
        )

    def pick(candidates: Sequence[str]) -> Optional[str]:
        for key in candidates:
            if any(key in sample for sample in dict_samples):
                return key
        return None

    schema = Schema(
        container_key=container_key,
        id_key=pick(ID_KEYS),
        title_key=pick(TITLE_KEYS),
        created_key=pick(CREATED_KEYS),
        updated_key=pick(UPDATED_KEYS),
        messages_key=pick(MESSAGE_KEYS),
    )

    if dict_samples and not (schema.id_key or schema.title_key or schema.messages_key):
        seen: List[str] = []
        for sample in dict_samples:
            for key in sample:
                if key not in seen:
                    seen.append(str(key))
        shown = ", ".join(repr(key) for key in seen[:25]) or "(no keys at all)"
        raise ExportError(
            "no conversation-shaped keys found in the first {} record(s).\n"
            "Expected one of id={} title={} messages={}.\n"
            "The keys actually present are: {}".format(
                len(dict_samples),
                "/".join(ID_KEYS[:3]),
                "/".join(TITLE_KEYS[:2]),
                "/".join(MESSAGE_KEYS[:2]),
                shown,
            )
        )
    return schema


def message_count_of(record: Dict[str, Any], schema: Schema) -> int:
    _key, value = first_present(record, schema.messages_key, MESSAGE_KEYS)
    if isinstance(value, (list, tuple)):
        return len(value)
    if isinstance(value, dict):
        return len(value)
    return 0


# --------------------------------------------------------------------------- #
# Reading the export
# --------------------------------------------------------------------------- #


class ConversationSource:
    """A re-iterable sequence of conversation objects.

    Re-iterable matters: the ``--max-files`` guard has to know the conversation
    count *before* the first shard is written, which means one counting pass and
    then one writing pass.
    """

    container_key: Optional[str] = None
    parser: str = "unknown"
    streaming: bool = False

    def __iter__(self) -> Iterator[Any]:  # pragma: no cover - interface
        raise NotImplementedError


class MemorySource(ConversationSource):
    """Conversations already materialised by ``json.load``."""

    def __init__(self, records: Sequence[Any], container_key: Optional[str]) -> None:
        self._records = records
        self.container_key = container_key
        self.parser = "json (whole file in memory)"
        self.streaming = False

    def __iter__(self) -> Iterator[Any]:
        return iter(self._records)


class StreamingSource(ConversationSource):
    """Conversations pulled from disk one at a time by ijson."""

    def __init__(self, path: Path, container_key: Optional[str], ijson_module: Any) -> None:
        self._path = path
        self._ijson = ijson_module
        self.container_key = container_key
        self.parser = "ijson {} (streaming)".format(getattr(ijson_module, "__version__", "?"))
        self.streaming = True
        self._prefix = "item" if container_key is None else "{}.item".format(container_key)
        self._kwargs: Dict[str, Any] = {"use_float": True} if supports_use_float(ijson_module) else {}
        self._errors = ijson_error_types(ijson_module)

    def __iter__(self) -> Iterator[Any]:
        try:
            with self._path.open("rb") as handle:
                for record in self._ijson.items(handle, self._prefix, **self._kwargs):
                    yield record
        except self._errors as exc:
            raise translate_ijson_error(self._path, exc) from exc


def supports_use_float(ijson_module: Any) -> bool:
    """ijson >= 3.1 can decode JSON numbers as float instead of Decimal.

    Older versions cannot, so their Decimals are converted at serialisation time
    by ``json_default`` instead.
    """
    try:
        list(ijson_module.items(io.BytesIO(b"[]"), "item", use_float=True))
    except TypeError:
        return False
    except Exception:  # noqa: BLE001 - a probe must never break the run
        return False
    return True


def import_ijson() -> Optional[Any]:
    try:
        import ijson  # type: ignore
    except ImportError:
        return None
    return ijson


def ijson_error_types(ijson_module: Any) -> Tuple[type, ...]:
    """The parse-failure exceptions this ijson exposes, as a tuple for ``except``.

    ijson's errors do not inherit from ``ValueError``, so nothing else in this
    file would catch them; without this they escape ``main`` as a traceback.
    """
    found: List[type] = []
    holders = [ijson_module, getattr(ijson_module, "common", None)]
    for holder in holders:
        for name in ("JSONError", "IncompleteJSONError"):
            candidate = getattr(holder, name, None)
            if isinstance(candidate, type) and issubclass(candidate, BaseException):
                if not any(issubclass(candidate, existing) for existing in found):
                    found.append(candidate)
    return tuple(found)


def translate_ijson_error(path: Path, exc: BaseException) -> ExportError:
    """Turn an ijson parse failure into a readable ``ExportError``.

    A number too wide for ijson's C backend is not a broken file -- ``json.load``
    reads it losslessly -- so that one becomes ``StreamingUnsupported`` and
    ``main`` retries in memory instead of reporting a corrupt export.
    """
    text = " ".join(str(exc).split())
    if "overflow" in text.lower():
        return StreamingUnsupported(
            "{}: ijson cannot represent a number in this export ({})".format(path, text)
        )
    return ExportError(
        "{} is not valid JSON (streaming parser): {}.\n"
        "If the export was copied over a network, re-download it and compare byte "
        "counts against the source.".format(path, text)
    )


def choose_container_key(
    array_keys: Sequence[str], counts: Optional[Dict[str, int]] = None
) -> Optional[str]:
    """Pick the one top-level array to shard, out of every array that exists.

    Both parsers call this, so ijson and ``json.load`` can never disagree about
    which array a given file means.  Preference order is ``CONTAINER_KEYS``; any
    other top-level array is named in a warning rather than dropped in silence.
    """
    if not array_keys:
        return None

    chosen: Optional[str] = None
    for name in CONTAINER_KEYS:
        if name in array_keys:
            chosen = name
            break
    if chosen is None:
        chosen = array_keys[0]
        LOGGER.warning(
            "no %s key; using the first top-level array, %r",
            "/".join(CONTAINER_KEYS[:2]),
            chosen,
        )

    ignored = [key for key in array_keys if key != chosen]
    if ignored:
        def describe(key: str) -> str:
            if counts is not None and key in counts:
                count = counts[key]
                return "{!r} ({} {})".format(key, count, "entry" if count == 1 else "entries")
            return repr(key)

        LOGGER.warning(
            "the top-level object holds %d arrays; sharding %r only and IGNORING %s. "
            "If the conversations are in one of those, pass a file whose wrapper key "
            "is one of %s, or unwrap it.",
            len(array_keys),
            chosen,
            ", ".join(describe(key) for key in ignored),
            "/".join(CONTAINER_KEYS),
        )
    return chosen


def first_json_token(path: Path) -> str:
    """The first non-whitespace character of the document (``[``, ``{`` or ...)."""
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(4096)
            if not chunk:
                return ""
            # strip leading whitespace and any UTF-8 BOM bytes
            stripped = chunk.lstrip(b" \t\r\n\xef\xbb\xbf")
            if stripped:
                return stripped[:1].decode("utf-8", "replace")


def detect_container_key_streaming(path: Path, ijson_module: Any) -> Optional[str]:
    """For an object-wrapped export, find the top-level key holding the array.

    Returns ``None`` when the document is a bare array.  Raises ``ExportError``
    when it is neither, or when no top-level array exists.
    """
    token = first_json_token(path)
    if token == "[":
        return None
    if token != "{":
        raise ExportError(
            "the file does not start with '[' or '{{' (found {!r}); "
            "it is not a JSON conversations export".format(token or "end of file")
        )

    keys_seen: List[str] = []
    array_keys: List[str] = []
    counts: Dict[str, int] = {}
    item_prefixes: Dict[str, str] = {}
    current_key: Optional[str] = None
    # Every top-level array is collected before choosing, so that this and
    # container_key_from_object below cannot pick different arrays from one file.
    try:
        with path.open("rb") as handle:
            for prefix, event, value in ijson_module.parse(handle):
                if prefix == "" and event == "map_key":
                    current_key = str(value)
                    keys_seen.append(current_key)
                    continue
                if current_key is not None and prefix == current_key and event == "start_array":
                    array_keys.append(current_key)
                    counts[current_key] = 0
                    item_prefixes["{}.item".format(current_key)] = current_key
                    continue
                owner = item_prefixes.get(prefix)
                if owner is not None and event in (
                    "start_map",
                    "start_array",
                    "string",
                    "number",
                    "integer",
                    "double",
                    "boolean",
                    "null",
                ):
                    counts[owner] += 1
                if prefix == "" and event == "end_map":
                    break
    except ijson_error_types(ijson_module) as exc:
        raise translate_ijson_error(path, exc) from exc

    chosen = choose_container_key(array_keys, counts)
    if chosen is not None:
        return chosen

    shown = ", ".join(repr(key) for key in keys_seen[:25]) or "(none)"
    raise ExportError(
        "the top-level object holds no array of conversations.\n"
        "Top-level keys present: {}".format(shown)
    )


def container_key_from_object(document: Dict[str, Any]) -> str:
    array_keys = [str(key) for key, value in document.items() if isinstance(value, list)]
    counts = {str(key): len(value) for key, value in document.items() if isinstance(value, list)}
    chosen = choose_container_key(array_keys, counts)
    if chosen is not None:
        return chosen
    shown = ", ".join(repr(key) for key in list(document)[:25]) or "(none)"
    raise ExportError(
        "the top-level object holds no array of conversations.\n"
        "Top-level keys present: {}".format(shown)
    )


def open_source(path: Path, size_bytes: int) -> ConversationSource:
    """Build a re-iterable source, streaming when ijson is available."""
    ijson_module = import_ijson()
    if ijson_module is not None:
        LOGGER.info(
            "using ijson %s: the input is parsed as a stream, memory stays flat",
            getattr(ijson_module, "__version__", "?"),
        )
        container_key = detect_container_key_streaming(path, ijson_module)
        if container_key is not None and "." in container_key:
            raise ExportError(
                "the wrapper key {!r} contains a dot, which ijson prefixes cannot "
                "address unambiguously. Uninstall ijson to use the in-memory "
                "parser, or rename the key.".format(container_key)
            )
        return StreamingSource(path, container_key, ijson_module)

    return load_in_memory(path, size_bytes)


def load_in_memory(path: Path, size_bytes: int) -> ConversationSource:
    """Parse the whole document with ``json.load``; used when ijson is absent or
    cannot represent the file (see ``StreamingUnsupported``)."""
    LOGGER.warning(
        "ijson is NOT installed: falling back to json.load, which holds the whole "
        "document in memory and typically needs 4-8x the file size in RAM "
        "(roughly %s for this %s input). Install it with "
        "'python3 -m pip install ijson' for constant-memory streaming.",
        human_bytes(size_bytes * 6),
        human_bytes(size_bytes),
    )
    try:
        with path.open("r", encoding="utf-8") as handle:
            document = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ExportError("{} is not valid JSON: {}".format(path, exc)) from exc
    except MemoryError as exc:  # pragma: no cover - environment dependent
        raise ExportError(
            "ran out of memory loading {} ({}). Install ijson "
            "('python3 -m pip install ijson') so the file can be streamed.".format(
                path, human_bytes(size_bytes)
            )
        ) from exc

    if isinstance(document, list):
        return MemorySource(document, None)
    if isinstance(document, dict):
        key = container_key_from_object(document)
        return MemorySource(document[key], key)
    raise ExportError(
        "the top level of {} is a {}, not an array or object; "
        "this is not a conversations export".format(path, type(document).__name__)
    )


def sample_records(source: ConversationSource, limit: int = SCHEMA_SAMPLE_SIZE) -> List[Any]:
    samples: List[Any] = []
    for record in source:
        samples.append(record)
        if len(samples) >= limit:
            break
    return samples


# --------------------------------------------------------------------------- #
# Sharding
# --------------------------------------------------------------------------- #


@dataclasses.dataclass(frozen=True)
class IndexRow:
    shard_path: str
    conversation_id: str
    title: str
    created_at: str
    updated_at: str
    message_count: int
    bytes: int

    def as_fields(self) -> Tuple[str, ...]:
        return (
            self.shard_path,
            self.conversation_id,
            self.title,
            self.created_at,
            self.updated_at,
            str(self.message_count),
            str(self.bytes),
        )


@dataclasses.dataclass
class ShardResult:
    conversations: int = 0
    messages: int = 0
    bytes_out: int = 0
    rows: List[IndexRow] = dataclasses.field(default_factory=list)

    @property
    def largest(self) -> Optional[IndexRow]:
        if not self.rows:
            return None
        return max(self.rows, key=lambda row: row.bytes)


def json_default(value: Any) -> Any:
    """Make ijson's Decimal numbers serialisable again, losing no integer."""
    if isinstance(value, decimal.Decimal):
        if value == value.to_integral_value():
            return int(value)
        return float(value)
    raise TypeError(
        "cannot serialise {} in a conversation record".format(type(value).__name__)
    )


def serialise(record: Any) -> str:
    """One conversation as pretty JSON: readable in a diff and to an indexer.

    ``ensure_ascii=False`` keeps accents, CJK and emoji legible.  Real exports do
    contain lone UTF-16 surrogates (an unpaired ``\\ud800``), which no UTF-8
    encoder will accept; when one is present this re-dumps the record with
    ``ensure_ascii=True`` so it round-trips as the escape it arrived as, instead
    of raising UnicodeEncodeError halfway through writing the output tree.
    """
    text = json.dumps(
        record, ensure_ascii=False, indent=2, sort_keys=False, default=json_default
    )
    if SURROGATES.search(text):
        text = json.dumps(
            record, ensure_ascii=True, indent=2, sort_keys=False, default=json_default
        )
    return text + "\n"


def shard_relative_path(
    record: Dict[str, Any], schema: Schema, index: int, taken: Set[str]
) -> Tuple[str, str, str, str, str]:
    """Decide where one conversation goes.

    Returns ``(relative_path, conversation_id, title, created_at, updated_at)``.
    The id becomes the filename; with no id, a sanitised title plus the record's
    ordinal is used, and a bare ordinal when there is no title either.
    """
    _id_key, raw_id = first_present(record, schema.id_key, ID_KEYS)
    _title_key, raw_title = first_present(record, schema.title_key, TITLE_KEYS)
    _created_key, raw_created = first_present(record, schema.created_key, CREATED_KEYS)
    _updated_key, raw_updated = first_present(record, schema.updated_key, UPDATED_KEYS)

    conversation_id = "" if raw_id is None else str(raw_id).strip()
    title = "" if raw_title is None else str(raw_title)

    if conversation_id:
        stem = sanitize_component(conversation_id, "conversation-{:06d}".format(index))
    elif title.strip():
        stem = "{}-{:06d}".format(
            sanitize_component(title, "conversation"), index
        )
    else:
        stem = "conversation-{:06d}".format(index)

    directory = month_directory(raw_created)
    relative = "{}/{}.json".format(directory, stem)
    if relative in taken:
        # Duplicate ids (or titles) exist in real exports; keep both.
        suffix = 2
        while "{}/{}__{}.json".format(directory, stem, suffix) in taken:
            suffix += 1
        relative = "{}/{}__{}.json".format(directory, stem, suffix)
    taken.add(relative)

    return (
        relative,
        conversation_id,
        clean_field(title),
        clean_field(raw_created),
        clean_field(raw_updated),
    )


def require_dict(record: Any, index: int) -> Dict[str, Any]:
    if isinstance(record, dict):
        return record
    raise ExportError(
        "conversation #{} is a {}, not an object; this does not look like a "
        "Claude conversations export".format(index, type(record).__name__)
    )


def survey(source: ConversationSource, schema: Schema, measure: bool) -> Tuple[int, int, int]:
    """Count conversations and messages without writing anything.

    With ``measure`` the exact serialised size is computed too, which is what
    ``--dry-run`` reports as the projected output size.
    """
    conversations = 0
    messages = 0
    projected = 0
    for index, raw in enumerate(source):
        record = require_dict(raw, index)
        conversations += 1
        messages += message_count_of(record, schema)
        if measure:
            projected += len(serialise(record).encode("utf-8"))
        if conversations % 1000 == 0:
            LOGGER.debug("surveyed %d conversations", conversations)
    return conversations, messages, projected


def write_shards(
    source: ConversationSource,
    schema: Schema,
    out_dir: Path,
    result: Optional[ShardResult] = None,
) -> ShardResult:
    """Write one file per conversation.

    ``result`` may be supplied by the caller so that a failure part-way through
    still leaves it holding everything written up to that point, which is what
    ``run_shard`` reports instead of a traceback.
    """
    if result is None:
        result = ShardResult()
    taken: Set[str] = set()
    made_dirs: Set[Path] = set()

    for index, raw in enumerate(source):
        record = require_dict(raw, index)
        relative, conversation_id, title, created, updated = shard_relative_path(
            record, schema, index, taken
        )
        target = out_dir.joinpath(*relative.split("/"))
        if target.parent not in made_dirs:
            target.parent.mkdir(parents=True, exist_ok=True)
            made_dirs.add(target.parent)

        # Atomic: a shard is either absent or complete, never torn.
        size = write_text_atomically(target, serialise(record))

        count = message_count_of(record, schema)
        result.conversations += 1
        result.messages += count
        result.bytes_out += size
        result.rows.append(
            IndexRow(
                shard_path=relative,
                conversation_id=conversation_id,
                title=title,
                created_at=created,
                updated_at=updated,
                message_count=count,
                bytes=size,
            )
        )
        if result.conversations % 1000 == 0:
            LOGGER.info("wrote %d shards", result.conversations)

    return result


def write_index(out_dir: Path, rows: Sequence[IndexRow]) -> int:
    lines = ["\t".join(INDEX_COLUMNS)]
    for row in sorted(rows, key=lambda item: item.shard_path):
        lines.append("\t".join(clean_field(field) for field in row.as_fields()))
    return write_text_atomically(out_dir / INDEX_NAME, "\n".join(lines) + "\n")


def write_summary(out_dir: Path, summary: Dict[str, Any]) -> int:
    return write_text_atomically(
        out_dir / SUMMARY_NAME,
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
    )


def verify_shards(out_dir: Path, rows: Sequence[IndexRow], expected: int) -> List[str]:
    """Re-read every shard: it must exist, parse, and be one of ``expected``."""
    problems: List[str] = []
    for row in rows:
        path = out_dir.joinpath(*row.shard_path.split("/"))
        try:
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
        except FileNotFoundError:
            problems.append("{}: missing after writing".format(row.shard_path))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            # A shard truncated mid multi-byte character raises UnicodeDecodeError,
            # not JSONDecodeError; both are corruption this pass exists to report,
            # so neither may abort the run before the other shards are checked.
            problems.append("{}: does not parse ({})".format(row.shard_path, exc))
        except OSError as exc:
            problems.append("{}: unreadable ({})".format(row.shard_path, exc))
    if len(rows) != expected:
        problems.append(
            "wrote {} shard(s) for {} conversation(s) read".format(len(rows), expected)
        )
    # Shards always live one level down (YYYY-MM/ or undated/); INDEX.tsv and
    # SUMMARY.json sit at the top and must not be counted as shards.
    on_disk = sum(
        1
        for path in out_dir.rglob("*.json")
        if path.is_file() and path.parent != out_dir
    )
    if on_disk != expected:
        problems.append(
            "found {} .json file(s) under {} but read {} conversation(s)".format(
                on_disk, out_dir, expected
            )
        )
    return problems


# --------------------------------------------------------------------------- #
# Gzip mode
# --------------------------------------------------------------------------- #


class ByteCounter:
    """A write-only sink that records how many bytes it was handed."""

    def __init__(self) -> None:
        self.total = 0

    def write(self, data: bytes) -> int:
        self.total += len(data)
        return len(data)

    def flush(self) -> None:
        return None


def compress_stream(source_path: Path, sink: Any, limit_bytes: Optional[int] = None) -> Tuple[int, int]:
    """Gzip ``source_path`` into ``sink``; returns ``(bytes_read, bytes_written)``.

    ``mtime=0`` and an empty embedded filename keep the output byte-identical
    across runs, so re-running does not churn the git object.  Nothing larger
    than one chunk is ever held in memory.
    """
    read_total = 0
    counter = sink if isinstance(sink, ByteCounter) else None
    with gzip.GzipFile(filename="", mode="wb", compresslevel=GZIP_LEVEL, fileobj=sink, mtime=0) as gz:
        with source_path.open("rb") as handle:
            while True:
                if limit_bytes is not None and read_total >= limit_bytes:
                    break
                want = COPY_CHUNK_BYTES
                if limit_bytes is not None:
                    want = min(want, limit_bytes - read_total)
                chunk = handle.read(want)
                if not chunk:
                    break
                read_total += len(chunk)
                gz.write(chunk)
    written = counter.total if counter is not None else sink.tell()
    return read_total, written


def verify_gzip(path: Path, expected_bytes: int) -> List[str]:
    """Decompress the result and confirm it yields the original byte count."""
    problems: List[str] = []
    total = 0
    try:
        with gzip.open(str(path), "rb") as handle:
            while True:
                chunk = handle.read(COPY_CHUNK_BYTES)
                if not chunk:
                    break
                total += len(chunk)
    except OSError as exc:
        problems.append("{} does not decompress ({})".format(path.name, exc))
        return problems
    if total != expected_bytes:
        problems.append(
            "{} decompresses to {} bytes, expected {}".format(path.name, total, expected_bytes)
        )
    return problems


def run_gzip(
    input_path: Path,
    size_bytes: int,
    out_dir: Path,
    dry_run: bool,
    force: bool,
) -> Tuple[int, Dict[str, Any]]:
    """Compress the export to a single .gz, refusing to leave one over 100 MB."""
    target = out_dir / (input_path.name + ".gz")
    summary: Dict[str, Any] = {
        "tool": "shard_conversations.py",
        "mode": "gzip",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "input": {"path": str(input_path), "bytes": size_bytes},
        "parser": "none (gzip mode copies bytes, it does not parse)",
        "schema": None,
        "conversations": None,
        "messages": None,
        "bytes_in": size_bytes,
    }

    if dry_run:
        sample_limit = min(size_bytes, GZIP_SAMPLE_BYTES)
        counter = ByteCounter()
        read, written = compress_stream(input_path, counter, limit_bytes=sample_limit)
        ratio = (read / written) if written else 0.0
        projected = int(size_bytes / ratio) if ratio else 0
        print("Dry run - gzip mode, nothing written")
        print("  input               {} ({} bytes)".format(human_bytes(size_bytes), size_bytes))
        print("  sampled             {} at level {}".format(human_bytes(read), GZIP_LEVEL))
        print("  measured ratio      {:.1f} to 1".format(ratio))
        print("  projected output    ~{} -> {}".format(human_bytes(projected), target))
        print(
            "  GitHub 100 MB limit {}".format(
                "would be exceeded - use the default sharding mode"
                if projected > GITHUB_FILE_LIMIT_BYTES
                else "OK"
            )
        )
        summary.update(
            {
                "dry_run": True,
                "output": str(target),
                "sampled_bytes": read,
                "measured_ratio": round(ratio, 3),
                "projected_bytes_out": projected,
            }
        )
        return 0, summary

    if target.exists() and not force:
        raise SystemExit(
            "refusing to overwrite {}\nRe-run with --force to replace it.".format(target)
        )

    # The same rule shard mode applies: a directory holding an earlier run's
    # output is not a safe place to drop a .gz and a fresh SUMMARY.json into,
    # because that SUMMARY.json is the only record of what those shards are.
    if out_dir.is_dir():
        leftovers = sorted(entry.name for entry in out_dir.iterdir() if entry != target)
        if leftovers and not force:
            raise SystemExit(
                "refusing to write into non-empty directory {}\n"
                "It already holds {} entr{} ({}{}), and gzip mode would overwrite "
                "{} there -- destroying the record of whatever produced them.\n"
                "Move it aside, choose another --out, or re-run with --force.".format(
                    out_dir,
                    len(leftovers),
                    "y" if len(leftovers) == 1 else "ies",
                    ", ".join(leftovers[:5]),
                    ", ..." if len(leftovers) > 5 else "",
                    SUMMARY_NAME,
                )
            )
        if leftovers:
            LOGGER.warning(
                "--force: writing into non-empty %s; %s is replaced with this gzip run's "
                "summary and any earlier shard inventory there is lost",
                out_dir,
                SUMMARY_NAME,
            )
    out_dir.mkdir(parents=True, exist_ok=True)

    handle = tempfile.NamedTemporaryFile(
        "wb", dir=str(out_dir), prefix=".shard-conversations-", suffix=".gz.part", delete=False
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            read, _written = compress_stream(input_path, handle)
        bytes_out = temp_path.stat().st_size
        ratio = (read / bytes_out) if bytes_out else 0.0

        if bytes_out > GITHUB_FILE_LIMIT_BYTES:
            remove_quietly(temp_path)
            raise SystemExit(
                "refusing to write {}: it compressed to {} ({} bytes), still above "
                "GitHub's 100 MB per-file hard limit (achieved ratio {:.1f} to 1).\n"
                "Use the default sharding mode instead, which writes one small file "
                "per conversation:\n"
                "    python3 {} {} --out {}".format(
                    target.name,
                    human_bytes(bytes_out),
                    bytes_out,
                    ratio,
                    sys.argv[0] or Path(__file__).name,
                    input_path,
                    out_dir,
                )
            )

        os.chmod(str(temp_path), 0o644)
        os.replace(str(temp_path), str(target))
    except BaseException:
        remove_quietly(temp_path)
        raise

    LOGGER.info("verifying %s", target.name)
    problems = verify_gzip(target, size_bytes)

    summary.update(
        {
            "dry_run": False,
            "output": str(target),
            "bytes_out": bytes_out,
            "compression_ratio": round(ratio, 3),
            "github_limit_bytes": GITHUB_FILE_LIMIT_BYTES,
            "verified": not problems,
        }
    )
    summary_bytes = write_summary(out_dir, summary)

    print("Gzip summary:")
    print("  input             {} ({} bytes)".format(human_bytes(size_bytes), size_bytes))
    print("  output            {}".format(target))
    print("  compressed        {} ({} bytes)".format(human_bytes(bytes_out), bytes_out))
    print("  ratio             {:.1f} to 1".format(ratio))
    print(
        "  GitHub 100 MB     OK, {} to spare".format(
            human_bytes(GITHUB_FILE_LIMIT_BYTES - bytes_out)
        )
    )
    print("  summary           {} ({} bytes)".format(out_dir / SUMMARY_NAME, summary_bytes))

    if problems:
        print("\nVerification FAILED:", file=sys.stderr)
        for problem in problems:
            print("  {}".format(problem), file=sys.stderr)
        return 1, summary
    print("  verified          decompresses to the original {} bytes".format(size_bytes))
    return 0, summary


# --------------------------------------------------------------------------- #
# Shard mode
# --------------------------------------------------------------------------- #


def base_summary(input_path: Path, size_bytes: int, source: ConversationSource, schema: Schema) -> Dict[str, Any]:
    return {
        "tool": "shard_conversations.py",
        "mode": "shard",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "input": {"path": str(input_path), "bytes": size_bytes},
        "parser": source.parser,
        "schema": schema.as_dict(),
    }


def run_shard(
    input_path: Path,
    size_bytes: int,
    source: ConversationSource,
    schema: Schema,
    out_dir: Path,
    dry_run: bool,
    force: bool,
    max_files: int,
) -> Tuple[int, Dict[str, Any]]:
    summary = base_summary(input_path, size_bytes, source, schema)

    LOGGER.info("counting conversations before writing anything")
    conversations, messages, projected = survey(source, schema, measure=dry_run)
    over_limit = conversations > max_files

    if conversations == 0:
        # An empty result must not read like a clean run: the usual cause is that
        # the wrong top-level array was picked (see choose_container_key's warning).
        LOGGER.warning(
            "%s holds NO conversations. Nothing but an empty index would be written. "
            "If the export is not genuinely empty, the wrong top-level array was "
            "chosen -- check any 'IGNORING' warning above.",
            "the {!r} array".format(schema.container_key)
            if schema.container_key
            else "the top-level array",
        )

    if dry_run:
        print("Dry run - shard mode, nothing written")
        print("  input               {} ({} bytes)".format(human_bytes(size_bytes), size_bytes))
        print("  parser              {}".format(source.parser))
        print("  schema              {}".format(schema.describe()))
        print("  conversations       {:,}".format(conversations))
        print("  messages            {:,}".format(messages))
        print(
            "  projected output    {} across {:,} file(s) -> {}".format(
                human_bytes(projected), conversations, out_dir
            )
        )
        print(
            "  --max-files         {}".format(
                "WOULD REFUSE: {:,} shards exceeds the limit of {:,}".format(
                    conversations, max_files
                )
                if over_limit
                else "OK (limit {:,})".format(max_files)
            )
        )
        summary.update(
            {
                "dry_run": True,
                "output_dir": str(out_dir),
                "conversations": conversations,
                "messages": messages,
                "bytes_in": size_bytes,
                "projected_bytes_out": projected,
                "max_files": max_files,
            }
        )
        return 0, summary

    if over_limit:
        raise SystemExit(
            "refusing to write {:,} shards: --max-files is {:,}.\n"
            "That many small files is its own problem for git. Re-run with "
            "--max-files {} if that is genuinely what you want.".format(
                conversations, max_files, conversations
            )
        )

    if out_dir.exists() and out_dir.is_dir() and any(out_dir.iterdir()):
        if not force:
            raise SystemExit(
                "refusing to write into non-empty directory {}\n"
                "Move it aside, choose another --out, or re-run with --force.".format(out_dir)
            )
        LOGGER.warning(
            "--force: writing into non-empty %s; files left from an earlier run are "
            "not removed, and any that remain are reported by the final verification",
            out_dir,
        )
    out_dir.mkdir(parents=True, exist_ok=True)

    LOGGER.info("writing %d shard(s) to %s", conversations, out_dir)
    result = ShardResult()
    try:
        write_shards(source, schema, out_dir, result)
    except (ExportError, KeyboardInterrupt, SystemExit):
        raise
    except Exception as exc:  # noqa: BLE001 - say what was written, never a traceback
        raise SystemExit(
            "failed while writing shards: {}: {}\n"
            "{:,} shard(s) were written before the failure{}; no {} and no {} were "
            "written, so the output directory is incomplete.\n"
            "Delete {} and re-run once the cause is fixed.".format(
                type(exc).__name__,
                exc,
                len(result.rows),
                " (last: {})".format(result.rows[-1].shard_path) if result.rows else "",
                INDEX_NAME,
                SUMMARY_NAME,
                out_dir,
            )
        ) from exc
    index_bytes = write_index(out_dir, result.rows)

    LOGGER.info("verifying %d shard(s)", len(result.rows))
    problems = verify_shards(out_dir, result.rows, conversations)

    largest = result.largest
    summary.update(
        {
            "dry_run": False,
            "output_dir": str(out_dir),
            "conversations": result.conversations,
            "messages": result.messages,
            "bytes_in": size_bytes,
            "bytes_out": result.bytes_out,
            "shards_written": len(result.rows),
            "largest_shard": (
                None if largest is None else {"path": largest.shard_path, "bytes": largest.bytes}
            ),
            "index": {"path": INDEX_NAME, "rows": len(result.rows), "bytes": index_bytes},
            "max_files": max_files,
            "verified": not problems,
        }
    )
    summary_bytes = write_summary(out_dir, summary)

    print("Shard summary:")
    print("  input             {} ({} bytes)".format(human_bytes(size_bytes), size_bytes))
    print("  parser            {}".format(source.parser))
    print("  schema            {}".format(schema.describe()))
    print("  conversations     {:,}".format(result.conversations))
    print("  messages          {:,}".format(result.messages))
    print(
        "  shards            {:,} file(s), {} total, in {}".format(
            len(result.rows), human_bytes(result.bytes_out), out_dir
        )
    )
    if largest is not None:
        print("  largest shard     {} ({})".format(largest.shard_path, human_bytes(largest.bytes)))
    print("  index             {} ({} rows, {} bytes)".format(INDEX_NAME, len(result.rows), index_bytes))
    print("  summary           {} ({} bytes)".format(SUMMARY_NAME, summary_bytes))

    if problems:
        print("\nVerification FAILED:", file=sys.stderr)
        for problem in problems[:20]:
            print("  {}".format(problem), file=sys.stderr)
        if len(problems) > 20:
            print("  ... and {} more".format(len(problems) - 20), file=sys.stderr)
        return 1, summary

    print("  verified          all {:,} shard(s) re-read and parsed".format(len(result.rows)))
    return 0, summary


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def default_out_dir(input_path: Path) -> Path:
    stem = input_path.name
    for extension in (".json", ".JSON"):
        if stem.endswith(extension):
            stem = stem[: -len(extension)]
            break
    return input_path.parent / "{}-shards".format(stem or "conversations")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="shard_conversations.py",
        description=(
            "Split a Claude conversations.json export into one small JSON file per "
            "conversation (default), or compress it to a single .json.gz, so it can "
            "live in a git repository under GitHub's 100 MB per-file limit."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Modes:\n"
            "  (default)  shard: <out>/<YYYY-MM>/<uuid>.json plus INDEX.tsv and SUMMARY.json.\n"
            "             Undated conversations go to <out>/undated/. Many small readable\n"
            "             files are what a code-graph indexer can use.\n"
            "  --gzip     one <out>/<name>.json.gz instead. JSON compresses about ten to\n"
            "             one; the script measures the real ratio and refuses to leave a\n"
            "             file behind if it is still over 100 MB.\n"
            "\n"
            "Memory: install ijson (python3 -m pip install ijson) and the input is parsed\n"
            "as a stream at flat memory. Without it json.load is used, which needs roughly\n"
            "4-8x the file size in RAM; that fallback always warns on stderr. --gzip never\n"
            "parses, so it is safe on any input either way.\n"
            "\n"
            "Exit codes: 0 success, 1 refusal or failed verification, 2 bad arguments.\n"
        ),
    )
    parser.add_argument("input", metavar="INPUT", help="the conversations.json export to read")
    parser.add_argument(
        "--out",
        metavar="DIR",
        default=None,
        help="output directory (default: <input>-shards next to the input)",
    )
    parser.add_argument(
        "--gzip",
        action="store_true",
        help="write one compressed <name>.json.gz instead of sharding",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="parse and report counts and projected output size; write nothing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="write into a non-empty output directory (or replace an existing .gz)",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=DEFAULT_MAX_FILES,
        metavar="N",
        help="refuse to write more than N shards (default: %(default)s)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="debug logging")
    return parser


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s %(message)s",
        stream=sys.stderr,
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    if args.max_files < 1:
        parser.error("--max-files must be at least 1")

    input_path = Path(args.input).expanduser()
    out_dir = Path(args.out).expanduser() if args.out else default_out_dir(input_path)

    # Everything above this line is argument handling only: nothing is read.
    if not input_path.is_file():
        raise SystemExit("no such file: {}".format(input_path))
    size_bytes = input_path.stat().st_size
    if size_bytes == 0:
        raise SystemExit("{} is empty".format(input_path))

    out_dir = out_dir.resolve()
    # Checked here rather than at mkdir time so an --out typo (--out drive/chats.json)
    # fails in one line now, not with a FileExistsError after the whole counting pass.
    if out_dir.exists() and not out_dir.is_dir():
        raise SystemExit("--out {} exists and is not a directory".format(out_dir))

    def shard_with(source: ConversationSource) -> int:
        schema = detect_schema(sample_records(source), source.container_key)
        LOGGER.info("detected schema: %s", schema.describe())
        code, _summary = run_shard(
            input_path.resolve(),
            size_bytes,
            source,
            schema,
            out_dir,
            args.dry_run,
            args.force,
            args.max_files,
        )
        return code

    try:
        if args.gzip:
            code, _summary = run_gzip(
                input_path.resolve(), size_bytes, out_dir, args.dry_run, args.force
            )
            return code

        try:
            return shard_with(open_source(input_path, size_bytes))
        except StreamingUnsupported as exc:
            # Not a broken export: json.load reads this one losslessly. Nothing has
            # been written yet -- run_shard counts the whole input before writing,
            # so any streaming parse failure surfaces during that pass.
            LOGGER.warning("%s; retrying with the in-memory parser", exc)
            return shard_with(load_in_memory(input_path, size_bytes))
    except ExportError as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:  # pragma: no cover - interactive use
        print("interrupted", file=sys.stderr)
        sys.exit(130)
