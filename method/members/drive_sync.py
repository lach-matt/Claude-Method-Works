#!/usr/bin/env python3
"""Mirror Google Drive folders into this repository.

This is the size-unlimited replacement for the Google Drive MCP connector, which
drops any payload larger than about 6 MiB.  Every download here is streamed to a
temporary file with ``MediaIoBaseDownload`` and then atomically moved into place,
so file size is bounded only by disk space.

Typical use::

    python3 tools/drive_sync.py                 # sync both Method folders
    python3 tools/drive_sync.py --only BUILD15  # just the big build files
    python3 tools/drive_sync.py --dry-run -v    # show what would change
    python3 tools/drive_sync.py --prune         # also delete local orphans

Authentication uses the OAuth 2.0 installed-application flow.  Put the OAuth
client secrets ("Desktop app" credentials from the Google Cloud console) at
``~/.config/drive-sync/credentials.json`` (or point ``--credentials`` /
``$GOOGLE_DRIVE_CREDENTIALS`` at them).  The resulting token is cached next to it
in ``token.json`` and refreshed automatically; the browser consent flow only runs
again when the refresh fails.

The script rewrites ``<dest>/MANIFEST.tsv``, an 8-column tab-separated file with
the columns ``repo_path drive_id drive_title mime_type drive_size_bytes
drive_modified md5 status``, sorted by ``repo_path``.  The naming conventions of
the existing mirror are preserved exactly:

* Within one Drive folder, when several files share a title the most recently
  modified copy keeps the plain name and every older copy gets
  ``__<driveFileId>`` inserted before the extension.
* Google-native documents are exported (Docs to Markdown, Sheets to CSV, Slides
  to PDF, Drawings to PNG); their recorded size is the size of the export, not
  the size Drive reports for the native file.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import hashlib
import http.client
import logging
import os
import socket
import ssl
import sys
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple, TypeVar

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #

SCOPES: Tuple[str, ...] = ("https://www.googleapis.com/auth/drive.readonly",)

DEFAULT_FOLDER_NAMES: Tuple[str, ...] = (
    "The Method Materials",
    "The Method Prints & Proofs",
)

CONFIG_DIR = Path.home() / ".config" / "drive-sync"
DEFAULT_CREDENTIALS_PATH = CONFIG_DIR / "credentials.json"
DEFAULT_TOKEN_PATH = CONFIG_DIR / "token.json"
CREDENTIALS_ENV_VAR = "GOOGLE_DRIVE_CREDENTIALS"

FOLDER_MIME = "application/vnd.google-apps.folder"
SHORTCUT_MIME = "application/vnd.google-apps.shortcut"
GOOGLE_NATIVE_PREFIX = "application/vnd.google-apps."

#: Google-native mime type -> (export mime type, file extension).
EXPORT_FORMATS: Dict[str, Tuple[str, str]] = {
    "application/vnd.google-apps.document": ("text/markdown", ".md"),
    "application/vnd.google-apps.spreadsheet": ("text/csv", ".csv"),
    "application/vnd.google-apps.presentation": ("application/pdf", ".pdf"),
    "application/vnd.google-apps.drawing": ("image/png", ".png"),
}

LIST_FIELDS = (
    "nextPageToken, files(id, name, mimeType, size, md5Checksum, "
    "modifiedTime, shortcutDetails)"
)
GET_FIELDS = "id, name, mimeType, size, md5Checksum, modifiedTime, shortcutDetails"
PAGE_SIZE = 1000

DOWNLOAD_CHUNK_BYTES = 8 * 1024 * 1024
HTTP_TIMEOUT_SECONDS = 300
RETRY_ATTEMPTS = 5
RETRY_BASE_SECONDS = 2.0
#: Drive refuses to export a native document larger than this.
EXPORT_SIZE_LIMIT_BYTES = 10 * 1024 * 1024
MAX_FILENAME_BYTES = 255
# GitHub rejects any single file over 100 MiB on push, so fetching one costs
# transfer and disk for something that can never be committed.  Default ceiling
# for --max-file-bytes; see docs/REPO-SIZE.md.
GITHUB_FILE_LIMIT_BYTES = 100 * 1024 * 1024

MANIFEST_NAME = "MANIFEST.tsv"
MANIFEST_COLUMNS: Tuple[str, ...] = (
    "repo_path",
    "drive_id",
    "drive_title",
    "mime_type",
    "drive_size_bytes",
    "drive_modified",
    "md5",
    "status",
)
#: Never pruned, even when they sit inside the destination tree.
PROTECTED_DEST_FILES = frozenset({MANIFEST_NAME, "README.md"})
TEMP_PREFIX = ".drive-sync-"

STATUS_OK = "ok"

LOGGER = logging.getLogger("drive_sync")

T = TypeVar("T")

#: Transport-level failures worth retrying.  ``socket.timeout`` is an alias of
#: ``TimeoutError`` on modern Pythons; both are listed for 3.9 compatibility.
RETRYABLE_NETWORK_ERRORS: Tuple[type, ...] = (
    socket.timeout,
    socket.gaierror,
    TimeoutError,
    ConnectionError,
    ssl.SSLError,
    http.client.HTTPException,
)


class ContentMismatch(http.client.HTTPException):
    """A transfer completed but the bytes are not what Drive said they would be.

    Subclasses ``HTTPException`` deliberately, for two reasons: it is in
    ``RETRYABLE_NETWORK_ERRORS``, so a truncated transfer is retried like any
    other transport fault; and ``sync_entry`` already treats that class as an
    I/O failure, so a persistent mismatch becomes a FAILED row rather than
    crashing the run.
    """


class Action:
    """Outcome categories reported in the final summary."""

    ADDED = "added"
    UPDATED = "updated"
    UNCHANGED = "unchanged"
    EXPORTED = "exported"
    SKIPPED = "skipped"
    FAILED = "failed"

    ORDER: Tuple[str, ...] = (ADDED, UPDATED, UNCHANGED, EXPORTED, SKIPPED, FAILED)


# --------------------------------------------------------------------------- #
# Data model
# --------------------------------------------------------------------------- #


@dataclasses.dataclass(frozen=True)
class DriveEntry:
    """One downloadable Drive file, already located inside the mirror tree."""

    file_id: str
    title: str
    mime_type: str
    size: Optional[int]
    md5: Optional[str]
    modified_time: str
    folder_path: str
    via_shortcut: bool = False

    @property
    def is_native(self) -> bool:
        return self.mime_type.startswith(GOOGLE_NATIVE_PREFIX)

    @property
    def export_format(self) -> Optional[Tuple[str, str]]:
        return EXPORT_FORMATS.get(self.mime_type)


@dataclasses.dataclass(frozen=True)
class ManifestRow:
    repo_path: str
    drive_id: str
    drive_title: str
    mime_type: str
    drive_size_bytes: str
    drive_modified: str
    md5: str
    status: str

    def as_fields(self) -> Tuple[str, ...]:
        return (
            self.repo_path,
            self.drive_id,
            self.drive_title,
            self.mime_type,
            self.drive_size_bytes,
            self.drive_modified,
            self.md5,
            self.status,
        )


@dataclasses.dataclass(frozen=True)
class SyncOutcome:
    repo_path: str
    action: str
    row: ManifestRow
    message: str = ""


@dataclasses.dataclass(frozen=True)
class RootFolder:
    name: str
    folder_id: str


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #


def clean_field(value: object) -> str:
    """Make a value safe for a tab-separated field: no tabs, no newlines."""
    text = "" if value is None else str(value)
    for char in ("\t", "\r\n", "\r", "\n"):
        text = text.replace(char, " ")
    return text.strip()


def md5_of_file(path: Path, chunk_bytes: int = 1024 * 1024) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_bytes), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_rfc3339(value: str) -> datetime:
    """Parse a Drive timestamp; unparseable values sort as 'very old'."""
    if not value:
        return datetime.min.replace(tzinfo=timezone.utc)
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
            try:
                parsed = datetime.strptime(value, fmt)
                break
            except ValueError:
                continue
        else:
            return datetime.min.replace(tzinfo=timezone.utc)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def sanitize_filename(raw: str, fallback: str) -> str:
    """Turn a Drive title into a safe single path component.

    Path separators and NUL are replaced, control characters dropped, and
    leading/trailing whitespace and dots stripped.  Callers append the export
    extension *before* sanitizing so that titles which legitimately end in dots
    (``"... corresponds to ..."`` -> ``"... corresponds to ....md"``) survive.
    """
    text = raw.replace("\x00", "").replace("/", "_")
    if os.sep != "/":
        text = text.replace(os.sep, "_")
    if os.altsep and os.altsep != "/":
        text = text.replace(os.altsep, "_")
    text = "".join(" " if char in "\t\r\n" else char for char in text)
    text = "".join(char for char in text if char.isprintable())

    previous = None
    while previous != text:
        previous = text
        text = text.strip().strip(".")

    if text in ("", ".", ".."):
        text = fallback
    return text


def compose_name(stem: str, extension: str, suffix: str = "") -> str:
    """Join a stem, an optional ``__<id>`` suffix and an extension.

    The stem is truncated (never the suffix or extension) so the result fits in
    a single filesystem component.
    """
    tail = f"{suffix}{extension}"
    budget = MAX_FILENAME_BYTES - len(tail.encode("utf-8"))
    if budget < 1:
        budget = 1
    encoded = stem.encode("utf-8")
    if len(encoded) > budget:
        stem = encoded[:budget].decode("utf-8", "ignore")
    return f"{stem}{tail}"


def join_repo_path(folder_path: str, name: str) -> str:
    return f"{folder_path}/{name}" if folder_path else name


def remove_quietly(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass
    except OSError as exc:  # pragma: no cover - best effort cleanup
        LOGGER.debug("could not remove %s: %s", path, exc)


# --------------------------------------------------------------------------- #
# Manifest I/O
# --------------------------------------------------------------------------- #


def read_manifest(path: Path) -> Dict[str, ManifestRow]:
    """Load an existing manifest, keyed by ``repo_path``.  Missing file -> {}."""
    rows: Dict[str, ManifestRow] = {}
    if not path.is_file():
        return rows
    with path.open("r", encoding="utf-8", newline="") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.rstrip("\n").rstrip("\r")
            if not line:
                continue
            fields = line.split("\t")
            if line_number == 1 and fields and fields[0] == MANIFEST_COLUMNS[0]:
                continue
            if len(fields) != len(MANIFEST_COLUMNS):
                LOGGER.warning(
                    "%s line %d: expected %d columns, found %d - ignoring",
                    path,
                    line_number,
                    len(MANIFEST_COLUMNS),
                    len(fields),
                )
                continue
            row = ManifestRow(*fields)
            rows[row.repo_path] = row
    return rows


def write_manifest(path: Path, rows: Iterable[ManifestRow]) -> None:
    ordered = sorted(rows, key=lambda row: row.repo_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="\n",
        dir=str(path.parent),
        prefix=TEMP_PREFIX,
        suffix=".tsv",
        delete=False,
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            handle.write("\t".join(MANIFEST_COLUMNS) + "\n")
            for row in ordered:
                handle.write("\t".join(clean_field(f) for f in row.as_fields()) + "\n")
        os.replace(str(temp_path), str(path))
    except BaseException:
        remove_quietly(temp_path)
        raise


# --------------------------------------------------------------------------- #
# Google API plumbing
# --------------------------------------------------------------------------- #


@dataclasses.dataclass(frozen=True)
class GoogleModules:
    """Lazily imported Google symbols, passed around instead of globals.

    Importing lazily keeps ``--help`` (and any argument error) working on a
    machine that has not installed the client libraries yet.
    """

    build: Callable[..., object]
    http_error: type
    media_download: type
    credentials_cls: type
    installed_app_flow: type
    refresh_request: type
    refresh_error: type
    authorized_http: Callable[..., object]
    http_factory: Callable[..., object]


def load_google_modules() -> GoogleModules:
    try:
        import google_auth_httplib2
        import httplib2
        from google.auth.exceptions import RefreshError
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        from googleapiclient.http import MediaIoBaseDownload
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise SystemExit(
            "Missing Google client libraries ({}).\n"
            "Install them with:\n"
            "    python3 -m pip install -r tools/requirements.txt".format(exc)
        ) from exc

    return GoogleModules(
        build=build,
        http_error=HttpError,
        media_download=MediaIoBaseDownload,
        credentials_cls=Credentials,
        installed_app_flow=InstalledAppFlow,
        refresh_request=Request,
        refresh_error=RefreshError,
        authorized_http=google_auth_httplib2.AuthorizedHttp,
        http_factory=httplib2.Http,
    )


def http_status_of(error: BaseException) -> Optional[int]:
    response = getattr(error, "resp", None)
    status = getattr(response, "status", None)
    if status is None:
        status = getattr(error, "status_code", None)
    try:
        return int(status)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def is_retryable_http_error(error: BaseException) -> bool:
    """429 and 5xx are transient; 401/403/404 never are."""
    status = http_status_of(error)
    if status is None:
        return False
    if status in (401, 403, 404):
        return False
    return status == 429 or 500 <= status < 600


def is_export_too_large(error: BaseException) -> bool:
    """Detect Drive's 10 MB ``files.export`` ceiling."""
    status = http_status_of(error)
    if status not in (400, 403):
        return False
    text = str(error).lower()
    content = getattr(error, "content", b"")
    if isinstance(content, bytes):
        text += " " + content.decode("utf-8", "replace").lower()
    else:  # pragma: no cover - defensive
        text += " " + str(content).lower()
    return "exportsizelimitexceeded" in text or "too large to be exported" in text


def call_with_retry(
    operation: Callable[[], T],
    *,
    description: str,
    http_error_cls: type,
    attempts: int = RETRY_ATTEMPTS,
    base_seconds: float = RETRY_BASE_SECONDS,
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    """Run ``operation`` with deterministic exponential backoff (2s, 4s, 8s...).

    Retries 429/5xx responses and transport timeouts only; 401/403/404 and every
    other exception propagate immediately.
    """
    for attempt in range(1, attempts + 1):
        try:
            return operation()
        except http_error_cls as exc:  # type: ignore[misc]
            if attempt >= attempts or not is_retryable_http_error(exc):
                raise
            reason = "HTTP {}".format(http_status_of(exc))
        except RETRYABLE_NETWORK_ERRORS as exc:
            if attempt >= attempts:
                raise
            reason = type(exc).__name__
        delay = base_seconds * (2 ** (attempt - 1))
        LOGGER.warning(
            "%s failed (%s); retry %d/%d in %.0fs",
            description,
            reason,
            attempt + 1,
            attempts,
            delay,
        )
        sleep(delay)
    raise RuntimeError("unreachable: retry loop exhausted for " + description)


def escape_query_value(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


class DriveClient:
    """Thin Drive v3 wrapper.

    ``googleapiclient`` service objects are not thread safe, so one service is
    built per thread from the shared credentials.
    """

    def __init__(
        self,
        credentials: object,
        modules: GoogleModules,
        timeout: int = HTTP_TIMEOUT_SECONDS,
    ) -> None:
        self._credentials = credentials
        self._modules = modules
        self._timeout = timeout
        self._thread_state = threading.local()

    @property
    def service(self) -> object:
        service = getattr(self._thread_state, "service", None)
        if service is None:
            authorized = self._modules.authorized_http(
                self._credentials,
                http=self._modules.http_factory(timeout=self._timeout),
            )
            service = self._modules.build(
                "drive", "v3", http=authorized, cache_discovery=False
            )
            self._thread_state.service = service
        return service

    def _retry(self, operation: Callable[[], T], description: str) -> T:
        return call_with_retry(
            operation,
            description=description,
            http_error_cls=self._modules.http_error,
        )

    @property
    def http_error_class(self) -> type:
        """``googleapiclient.errors.HttpError``, for callers' except clauses."""
        return self._modules.http_error

    # -- metadata ---------------------------------------------------------- #

    def get_file(self, file_id: str, fields: str = GET_FIELDS) -> Dict[str, object]:
        return self._retry(
            lambda: self.service.files()  # type: ignore[attr-defined]
            .get(fileId=file_id, fields=fields, supportsAllDrives=True)
            .execute(),
            "get metadata for {}".format(file_id),
        )

    def list_children(self, folder_id: str) -> List[Dict[str, object]]:
        """List every non-trashed child of ``folder_id``, following pageToken."""
        query = "'{}' in parents and trashed = false".format(escape_query_value(folder_id))
        return self._list_all(query, LIST_FIELDS, "list children of {}".format(folder_id))

    def find_folders_by_name(self, name: str) -> List[Dict[str, object]]:
        query = "name = '{}' and mimeType = '{}' and trashed = false".format(
            escape_query_value(name), FOLDER_MIME
        )
        return self._list_all(
            query,
            "nextPageToken, files(id, name, mimeType, modifiedTime)",
            "search for folder {!r}".format(name),
        )

    def _list_all(self, query: str, fields: str, description: str) -> List[Dict[str, object]]:
        items: List[Dict[str, object]] = []
        page_token: Optional[str] = None
        while True:
            token = page_token

            def request() -> Dict[str, object]:
                return (
                    self.service.files()  # type: ignore[attr-defined]
                    .list(
                        q=query,
                        pageSize=PAGE_SIZE,
                        fields=fields,
                        pageToken=token,
                        supportsAllDrives=True,
                        includeItemsFromAllDrives=True,
                    )
                    .execute()
                )

            response = self._retry(request, description)
            items.extend(response.get("files", []) or [])
            page_token = response.get("nextPageToken")  # type: ignore[assignment]
            if not page_token:
                return items

    # -- content ----------------------------------------------------------- #

    def download_file(
        self,
        file_id: str,
        destination: Path,
        expected_size: Optional[int] = None,
        expected_md5: str = "",
    ) -> Tuple[int, str]:
        return self._stream(
            lambda: self.service.files().get_media(  # type: ignore[attr-defined]
                fileId=file_id, supportsAllDrives=True
            ),
            destination,
            "download {}".format(file_id),
            expected_size=expected_size,
            expected_md5=expected_md5,
        )

    def export_file(
        self, file_id: str, export_mime: str, destination: Path
    ) -> Tuple[int, str]:
        # Drive reports neither size nor md5 for a native document, so an export
        # has nothing to check against; it is verified by the manifest instead.
        return self._stream(
            lambda: self.service.files().export_media(  # type: ignore[attr-defined]
                fileId=file_id, mimeType=export_mime
            ),
            destination,
            "export {} as {}".format(file_id, export_mime),
        )

    def _stream(
        self,
        make_request: Callable[[], object],
        destination: Path,
        description: str,
        expected_size: Optional[int] = None,
        expected_md5: str = "",
    ) -> Tuple[int, str]:
        """Stream a media request to ``destination`` via a sibling temp file.

        Nothing is ever held in memory beyond one chunk, which is what removes
        the size ceiling the MCP connector has.
        """

        def attempt() -> Tuple[int, str]:
            destination.parent.mkdir(parents=True, exist_ok=True)
            handle_fd, temp_name = tempfile.mkstemp(
                dir=str(destination.parent), prefix=TEMP_PREFIX, suffix=".part"
            )
            temp_path = Path(temp_name)
            try:
                with os.fdopen(handle_fd, "wb") as handle:
                    downloader = self._modules.media_download(
                        handle, make_request(), chunksize=DOWNLOAD_CHUNK_BYTES
                    )
                    done = False
                    try:
                        while not done:
                            _progress, done = downloader.next_chunk(num_retries=0)
                    except self._modules.http_error as exc:  # type: ignore[misc]
                        # Drive answers a ranged GET for zero-byte content with
                        # 416; that is an empty file, not a failure.  It only
                        # means that when NOTHING has been written yet: a 416
                        # partway through is a truncated transfer, and treating
                        # it as "empty" would install the partial file as
                        # complete.
                        if http_status_of(exc) != 416:
                            raise
                        if handle.tell():
                            raise ContentMismatch(
                                "{}: HTTP 416 after {} bytes — transfer truncated".format(
                                    description, handle.tell()
                                )
                            ) from exc
                        LOGGER.debug("%s returned 416: treating as empty", description)
                    handle.flush()
                    os.fsync(handle.fileno())

                # Verify BEFORE installing.  Everything above wrote to a sibling
                # temp file, so a transfer that fails this check is discarded and
                # any previously verified copy at `destination` is left intact.
                size = temp_path.stat().st_size
                if expected_size is not None and size != expected_size:
                    raise ContentMismatch(
                        "{}: got {} bytes, Drive says {}".format(
                            description, size, expected_size
                        )
                    )
                digest = md5_of_file(temp_path)
                if expected_md5 and digest != expected_md5:
                    raise ContentMismatch(
                        "{}: md5 {} does not match Drive's {}".format(
                            description, digest, expected_md5
                        )
                    )
                os.replace(str(temp_path), str(destination))
                return size, digest
            except BaseException:
                remove_quietly(temp_path)
                raise

        return call_with_retry(
            attempt,
            description=description,
            http_error_cls=self._modules.http_error,
        )


# --------------------------------------------------------------------------- #
# Credentials
# --------------------------------------------------------------------------- #


def save_token(credentials: object, token_path: Path) -> None:
    token_path.parent.mkdir(parents=True, exist_ok=True)
    payload = credentials.to_json()  # type: ignore[attr-defined]
    temp_path = token_path.with_name(token_path.name + ".tmp")
    with open(str(temp_path), "w", encoding="utf-8") as handle:
        handle.write(payload)
    os.chmod(str(temp_path), 0o600)
    os.replace(str(temp_path), str(token_path))


def has_required_scopes(credentials: object) -> bool:
    """True unless the cached token demonstrably lacks the read-only scope."""
    checker = getattr(credentials, "has_scopes", None)
    if checker is None:
        return True
    try:
        return bool(checker(list(SCOPES)))
    except Exception:  # noqa: BLE001 - a scope check must never break auth
        return True


def load_credentials(
    modules: GoogleModules,
    credentials_path: Path,
    token_path: Path,
) -> object:
    """Return usable OAuth credentials, refreshing or re-consenting as needed."""
    credentials = None
    if token_path.is_file():
        try:
            credentials = modules.credentials_cls.from_authorized_user_file(  # type: ignore[attr-defined]
                str(token_path), list(SCOPES)
            )
        except (ValueError, OSError) as exc:
            LOGGER.warning("ignoring unreadable token %s: %s", token_path, exc)
            credentials = None

    if credentials is not None and not has_required_scopes(credentials):
        LOGGER.warning("cached token lacks %s; starting consent flow", SCOPES[0])
        credentials = None

    if credentials is not None and getattr(credentials, "valid", False):
        return credentials

    if (
        credentials is not None
        and getattr(credentials, "expired", False)
        and getattr(credentials, "refresh_token", None)
    ):
        try:
            LOGGER.debug("refreshing cached token")
            credentials.refresh(modules.refresh_request())  # type: ignore[attr-defined]
            save_token(credentials, token_path)
            return credentials
        except (modules.refresh_error, OSError) as exc:  # type: ignore[misc]
            LOGGER.warning("token refresh failed (%s); starting consent flow", exc)
            credentials = None

    if not credentials_path.is_file():
        raise SystemExit(
            "OAuth client secrets not found at {}\n"
            "Create a Desktop-app OAuth client in the Google Cloud console, download\n"
            "the JSON, and save it there (or pass --credentials / set ${}).".format(
                credentials_path, CREDENTIALS_ENV_VAR
            )
        )

    LOGGER.info("starting browser consent flow using %s", credentials_path)
    flow = modules.installed_app_flow.from_client_secrets_file(  # type: ignore[attr-defined]
        str(credentials_path), list(SCOPES)
    )
    credentials = flow.run_local_server(port=0)
    save_token(credentials, token_path)
    return credentials


# --------------------------------------------------------------------------- #
# Folder resolution and traversal
# --------------------------------------------------------------------------- #


def resolve_root_folders(
    client: DriveClient,
    folder_names: Sequence[str],
    folder_ids: Sequence[str],
) -> List[RootFolder]:
    """Turn names/ids into concrete root folders, refusing ambiguous names."""
    roots: List[RootFolder] = []
    seen: Set[str] = set()

    for folder_id in folder_ids:
        metadata = client.get_file(folder_id, fields="id, name, mimeType")
        if metadata.get("mimeType") != FOLDER_MIME:
            raise SystemExit(
                "--folder-id {} is not a folder (mimeType {})".format(
                    folder_id, metadata.get("mimeType")
                )
            )
        identifier = str(metadata.get("id", folder_id))
        if identifier in seen:
            continue
        seen.add(identifier)
        roots.append(RootFolder(name=str(metadata.get("name", folder_id)), folder_id=identifier))

    for name in folder_names:
        matches = client.find_folders_by_name(name)
        if not matches:
            raise SystemExit(
                "No Drive folder named {!r} is visible to this account.".format(name)
            )
        if len(matches) > 1:
            lines = [
                "Folder name {!r} is ambiguous - {} folders match. "
                "Re-run with --folder-id for the one you want:".format(name, len(matches))
            ]
            for match in matches:
                lines.append(
                    "  --folder-id {}   (name={!r}, modified={})".format(
                        match.get("id"), match.get("name"), match.get("modifiedTime")
                    )
                )
            raise SystemExit("\n".join(lines))
        match = matches[0]
        identifier = str(match.get("id"))
        if identifier in seen:
            continue
        seen.add(identifier)
        roots.append(RootFolder(name=str(match.get("name", name)), folder_id=identifier))

    if not roots:
        raise SystemExit("No folders to sync; pass --folder or --folder-id.")
    return roots


def walk_root(
    client: DriveClient, root: RootFolder
) -> Tuple[List[DriveEntry], Dict[str, Set[str]]]:
    """Recursively list one root folder.

    Returns the files found (with their mirror-relative folder path) and, per
    folder path, the set of subdirectory names, which the naming pass uses to
    avoid file/directory collisions.
    """
    root_dir = sanitize_filename(root.name, "drive-{}".format(root.folder_id))
    entries: List[DriveEntry] = []
    dir_names: Dict[str, Set[str]] = {}
    visited: Set[str] = set()
    stack: List[Tuple[str, str]] = [(root.folder_id, root_dir)]

    while stack:
        folder_id, folder_path = stack.pop()
        if folder_id in visited:
            LOGGER.warning("skipping already-visited folder %s at %s", folder_id, folder_path)
            continue
        visited.add(folder_id)
        dir_names.setdefault(folder_path, set())

        LOGGER.debug("listing %s (%s)", folder_path, folder_id)
        for child in client.list_children(folder_id):
            child_id = str(child.get("id", ""))
            child_name = str(child.get("name", "") or "")
            child_mime = str(child.get("mimeType", "") or "")
            if not child_id:
                continue

            if child_mime == FOLDER_MIME:
                sub_dir = sanitize_filename(child_name, "folder-{}".format(child_id))
                if sub_dir in dir_names[folder_path]:
                    LOGGER.warning(
                        "two Drive subfolders named %r in %s will merge into one directory",
                        sub_dir,
                        folder_path or ".",
                    )
                dir_names[folder_path].add(sub_dir)
                stack.append((child_id, join_repo_path(folder_path, sub_dir)))
                continue

            if child_mime == SHORTCUT_MIME:
                resolved = resolve_shortcut(client, child, folder_path)
                if resolved is None:
                    continue
                target_id, target = resolved
                target_mime = str(target.get("mimeType", "") or "")
                if target_mime == FOLDER_MIME:
                    sub_dir = sanitize_filename(child_name, "folder-{}".format(target_id))
                    dir_names[folder_path].add(sub_dir)
                    stack.append((target_id, join_repo_path(folder_path, sub_dir)))
                    continue
                entries.append(make_entry(target, folder_path, title=child_name, via_shortcut=True))
                continue

            entries.append(make_entry(child, folder_path))

    return entries, dir_names


def resolve_shortcut(
    client: DriveClient, shortcut: Dict[str, object], folder_path: str
) -> Optional[Tuple[str, Dict[str, object]]]:
    details = shortcut.get("shortcutDetails") or {}
    target_id = ""
    if isinstance(details, dict):
        target_id = str(details.get("targetId", "") or "")
    if not target_id:
        LOGGER.warning(
            "shortcut %r in %s has no target; skipping",
            shortcut.get("name"),
            folder_path or ".",
        )
        return None
    try:
        target = client.get_file(target_id)
    except Exception as exc:  # noqa: BLE001 - a dead shortcut must not stop the sync
        LOGGER.warning(
            "shortcut %r in %s points at unreachable file %s (%s); skipping",
            shortcut.get("name"),
            folder_path or ".",
            target_id,
            clean_field(exc)[:160],
        )
        return None
    return target_id, target


def make_entry(
    metadata: Dict[str, object],
    folder_path: str,
    title: Optional[str] = None,
    via_shortcut: bool = False,
) -> DriveEntry:
    raw_size = metadata.get("size")
    try:
        size = int(raw_size) if raw_size is not None else None
    except (TypeError, ValueError):
        size = None
    return DriveEntry(
        file_id=str(metadata.get("id", "")),
        title=str(title if title is not None else metadata.get("name", "")),
        mime_type=str(metadata.get("mimeType", "") or ""),
        size=size,
        md5=str(metadata.get("md5Checksum")) if metadata.get("md5Checksum") else None,
        modified_time=str(metadata.get("modifiedTime", "") or ""),
        folder_path=folder_path,
        via_shortcut=via_shortcut,
    )


# --------------------------------------------------------------------------- #
# Naming
# --------------------------------------------------------------------------- #


def candidate_filename(entry: DriveEntry) -> str:
    """The filename a Drive file wants, before duplicate resolution."""
    name = entry.title
    export = entry.export_format
    if export is not None:
        extension = export[1]
        if not name.lower().endswith(extension):
            name = name + extension
    return sanitize_filename(name, "drive-{}".format(entry.file_id))


def assign_repo_paths(
    entries: Sequence[DriveEntry], dir_names: Dict[str, Set[str]]
) -> List[Tuple[DriveEntry, str]]:
    """Resolve same-title files within a folder.

    Newest modifiedTime keeps the plain name; older copies get ``__<driveFileId>``
    inserted before the extension.  Ties are broken by ascending file id so the
    result is stable across runs.
    """
    grouped: Dict[str, List[DriveEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.folder_path, []).append(entry)

    assignments: List[Tuple[DriveEntry, str]] = []
    for folder_path in sorted(grouped):
        buckets: Dict[str, List[DriveEntry]] = {}
        for entry in grouped[folder_path]:
            buckets.setdefault(candidate_filename(entry), []).append(entry)

        taken: Set[str] = set(dir_names.get(folder_path, set()))
        for name in sorted(buckets):
            bucket = sorted(buckets[name], key=lambda item: item.file_id)
            bucket.sort(key=lambda item: parse_rfc3339(item.modified_time), reverse=True)
            stem, extension = os.path.splitext(name)
            for index, entry in enumerate(bucket):
                if index == 0 and name not in taken:
                    final = compose_name(stem, extension)
                else:
                    final = compose_name(stem, extension, "__{}".format(entry.file_id))
                taken.add(final)
                assignments.append((entry, join_repo_path(folder_path, final)))
    return assignments


# --------------------------------------------------------------------------- #
# Syncing one file
# --------------------------------------------------------------------------- #


def build_row(
    entry: DriveEntry,
    repo_path: str,
    size: Optional[int],
    md5: str,
    status: str,
) -> ManifestRow:
    return ManifestRow(
        repo_path=repo_path,
        drive_id=entry.file_id,
        drive_title=entry.title,
        mime_type=entry.mime_type,
        drive_size_bytes="" if size is None else str(size),
        drive_modified=entry.modified_time,
        md5=md5 or "",
        status=status,
    )


def short_error(exc: BaseException) -> str:
    return clean_field("{}: {}".format(type(exc).__name__, exc))[:200]


def local_path_for(dest_root: Path, repo_path: str) -> Path:
    return dest_root.joinpath(*repo_path.split("/"))


def sync_entry(
    client: DriveClient,
    entry: DriveEntry,
    repo_path: str,
    dest_root: Path,
    previous: Dict[str, ManifestRow],
    dry_run: bool,
) -> SyncOutcome:
    """Bring one Drive file into the mirror and describe what happened."""
    target = local_path_for(dest_root, repo_path)
    previous_row = previous.get(repo_path)
    io_errors = (OSError, http.client.HTTPException)

    if entry.is_native and entry.export_format is None:
        message = "unsupported Google-native type {}".format(entry.mime_type)
        LOGGER.warning("skipping %s: %s", repo_path, message)
        return SyncOutcome(
            repo_path,
            Action.SKIPPED,
            build_row(entry, repo_path, entry.size, "", "skipped: " + message),
            message,
        )

    try:
        local_md5 = md5_of_file(target) if target.is_file() else ""
    except OSError as exc:
        local_md5 = ""
        LOGGER.debug("cannot hash %s: %s", target, exc)

    if entry.export_format is not None:
        export_mime, _extension = entry.export_format
        # Drive reports neither size nor md5 for native docs, so freshness comes
        # from the manifest: same export bytes and no newer Drive revision.
        if (
            local_md5
            and previous_row is not None
            and previous_row.drive_id == entry.file_id
            and previous_row.md5 == local_md5
            and parse_rfc3339(previous_row.drive_modified) >= parse_rfc3339(entry.modified_time)
        ):
            LOGGER.debug("unchanged export %s", repo_path)
            return SyncOutcome(
                repo_path,
                Action.UNCHANGED,
                build_row(entry, repo_path, target.stat().st_size, local_md5, STATUS_OK),
            )

        if dry_run:
            return SyncOutcome(
                repo_path,
                Action.EXPORTED,
                build_row(
                    entry,
                    repo_path,
                    previous_row.drive_size_bytes if previous_row else None,
                    local_md5,
                    "dry-run: would export as " + export_mime,
                ),
                "would export",
            )

        try:
            size, new_md5 = client.export_file(entry.file_id, export_mime, target)
        except client.http_error_class as exc:  # type: ignore[misc]
            if is_export_too_large(exc):
                status = (
                    "export-too-large: Drive will not export documents over "
                    "{} MB".format(EXPORT_SIZE_LIMIT_BYTES // (1024 * 1024))
                )
            else:
                status = "failed: " + short_error(exc)
            LOGGER.error("%s: %s", repo_path, status)
            return SyncOutcome(
                repo_path, Action.FAILED, build_row(entry, repo_path, entry.size, "", status), status
            )
        except io_errors as exc:
            status = "failed: " + short_error(exc)
            LOGGER.error("%s: %s", repo_path, status)
            return SyncOutcome(
                repo_path, Action.FAILED, build_row(entry, repo_path, entry.size, "", status), status
            )

        action = Action.UNCHANGED if new_md5 == local_md5 else Action.EXPORTED
        LOGGER.info("%s %s (%d bytes)", action, repo_path, size)
        return SyncOutcome(
            repo_path, action, build_row(entry, repo_path, size, new_md5, STATUS_OK)
        )

    existed = target.is_file()
    if existed:
        if entry.md5 and local_md5 == entry.md5:
            LOGGER.debug("unchanged %s", repo_path)
            return SyncOutcome(
                repo_path,
                Action.UNCHANGED,
                build_row(entry, repo_path, entry.size, local_md5, STATUS_OK),
            )
        if (
            not entry.md5
            and local_md5
            and previous_row is not None
            and previous_row.drive_id == entry.file_id
            and previous_row.md5 == local_md5
            and parse_rfc3339(previous_row.drive_modified) >= parse_rfc3339(entry.modified_time)
        ):
            LOGGER.debug("unchanged (no Drive md5) %s", repo_path)
            return SyncOutcome(
                repo_path,
                Action.UNCHANGED,
                build_row(entry, repo_path, entry.size, local_md5, STATUS_OK),
            )

    action = Action.UPDATED if existed else Action.ADDED
    if dry_run:
        return SyncOutcome(
            repo_path,
            action,
            build_row(entry, repo_path, entry.size, "", "dry-run: would " + action),
            "would " + action,
        )

    # Both checks happen inside download_file, against the temp file, before it
    # replaces anything.  A mismatch therefore leaves `target` untouched: a bad
    # transfer can no longer destroy a previously verified copy.
    try:
        size, new_md5 = client.download_file(
            entry.file_id,
            target,
            expected_size=entry.size,
            expected_md5=entry.md5 or "",
        )
    except client.http_error_class as exc:  # type: ignore[misc]
        status = "failed: " + short_error(exc)
        LOGGER.error("%s: %s", repo_path, status)
        return SyncOutcome(
            repo_path, Action.FAILED, build_row(entry, repo_path, entry.size, "", status), status
        )
    except io_errors as exc:
        status = "failed: " + short_error(exc)
        LOGGER.error("%s: %s", repo_path, status)
        return SyncOutcome(
            repo_path, Action.FAILED, build_row(entry, repo_path, entry.size, "", status), status
        )

    LOGGER.info("%s %s (%d bytes)", action, repo_path, size)
    # Record the bytes actually written, never Drive's declared size: when both
    # are known they have just been asserted equal, and when Drive gives no size
    # this is the only honest number.
    return SyncOutcome(
        repo_path, action, build_row(entry, repo_path, size, new_md5, STATUS_OK)
    )


# --------------------------------------------------------------------------- #
# Pruning
# --------------------------------------------------------------------------- #


def find_local_extras(
    dest_root: Path, root_dir_names: Sequence[str], expected: Set[str]
) -> List[Path]:
    """Files inside the mirrored roots that Drive no longer has."""
    extras: List[Path] = []
    for dir_name in root_dir_names:
        base = dest_root / dir_name
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if path.name in PROTECTED_DEST_FILES or path.name.startswith(TEMP_PREFIX):
                continue
            relative = path.relative_to(dest_root).as_posix()
            if relative in expected:
                continue
            extras.append(path)
    return extras


def prune_extras(dest_root: Path, extras: Sequence[Path]) -> Tuple[int, int]:
    """Delete orphaned files and any directories they leave empty."""
    removed = 0
    failed = 0
    parents: Set[Path] = set()
    for path in extras:
        try:
            path.unlink()
            removed += 1
            parents.add(path.parent)
            LOGGER.info("pruned %s", path.relative_to(dest_root).as_posix())
        except OSError as exc:
            failed += 1
            LOGGER.error("could not prune %s: %s", path, exc)

    for parent in sorted(parents, key=lambda item: len(item.parts), reverse=True):
        current = parent
        while current != dest_root and dest_root in current.parents:
            try:
                current.rmdir()
            except OSError:
                break
            LOGGER.info("removed empty directory %s", current.relative_to(dest_root).as_posix())
            current = current.parent
    return removed, failed


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def repo_root() -> Path:
    _h = Path(__file__).resolve().parent
    return _h.parent.parent if _h.name == 'members' else _h.parent   # the repo root, from tools/ or from a seated copy in method/members/


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="drive_sync.py",
        description=(
            "Mirror Google Drive folders into this repository with no file size "
            "limit, and regenerate MANIFEST.tsv."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Default folders: {}\n"
            "Credentials: --credentials, ${}, or {}\n".format(
                ", ".join(repr(name) for name in DEFAULT_FOLDER_NAMES),
                CREDENTIALS_ENV_VAR,
                DEFAULT_CREDENTIALS_PATH,
            )
        ),
    )
    parser.add_argument(
        "--dest",
        default=str(repo_root() / "drive"),
        help="destination directory for the mirror (default: %(default)s)",
    )
    parser.add_argument(
        "--folder",
        action="append",
        default=[],
        metavar="NAME",
        help="Drive folder name to sync; repeatable. Overrides the defaults.",
    )
    parser.add_argument(
        "--folder-id",
        action="append",
        default=[],
        metavar="ID",
        help="Drive folder id to sync; repeatable. Overrides the defaults.",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="SUBSTRING",
        help="only sync files whose repo path contains SUBSTRING; repeatable.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        metavar="SUBSTRING",
        help="never sync files whose repo path contains SUBSTRING; repeatable. "
        "Applied after --only.",
    )
    parser.add_argument(
        "--max-file-bytes",
        type=int,
        default=GITHUB_FILE_LIMIT_BYTES,
        metavar="N",
        help="skip files larger than N bytes (default: %(default)s, GitHub's "
        "per-file hard limit). Git cannot accept a file over this size, so "
        "downloading one only costs transfer and disk. Pass 0 to disable.",
    )
    parser.add_argument(
        "--credentials",
        default=None,
        metavar="PATH",
        help="OAuth client secrets JSON (default: ${} or {})".format(
            CREDENTIALS_ENV_VAR, DEFAULT_CREDENTIALS_PATH
        ),
    )
    parser.add_argument(
        "--token",
        default=str(DEFAULT_TOKEN_PATH),
        metavar="PATH",
        help="cached OAuth token (default: %(default)s)",
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=4,
        metavar="N",
        help="parallel download workers (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would change; write nothing, not even the manifest.",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help="delete local files that are no longer in Drive (default: report only).",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="debug logging")
    return parser


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s %(message)s",
        stream=sys.stderr,
    )


def resolve_credentials_path(argument: Optional[str]) -> Path:
    if argument:
        return Path(argument).expanduser()
    env_value = os.environ.get(CREDENTIALS_ENV_VAR)
    if env_value:
        return Path(env_value).expanduser()
    return DEFAULT_CREDENTIALS_PATH


def selected_by_only(repo_path: str, patterns: Sequence[str]) -> bool:
    return not patterns or any(pattern in repo_path for pattern in patterns)


def excluded_reason(
    entry: DriveEntry, repo_path: str, patterns: Sequence[str], max_bytes: Optional[int]
) -> str:
    """Why this file is being left alone, or "" to sync it."""
    for pattern in patterns:
        if pattern in repo_path:
            return "excluded by --exclude {}".format(pattern)
    if max_bytes is not None and entry.size is not None and entry.size > max_bytes:
        return "excluded: {} bytes is over --max-file-bytes {}".format(
            entry.size, max_bytes
        )
    return ""


def run_sync(
    client: DriveClient,
    assignments: Sequence[Tuple[DriveEntry, str]],
    dest_root: Path,
    previous: Dict[str, ManifestRow],
    jobs: int,
    dry_run: bool,
) -> List[SyncOutcome]:
    outcomes: List[SyncOutcome] = []
    if not assignments:
        return outcomes
    workers = max(1, min(jobs, len(assignments)))
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(
                sync_entry, client, entry, repo_path, dest_root, previous, dry_run
            ): (entry, repo_path)
            for entry, repo_path in assignments
        }
        for future in concurrent.futures.as_completed(futures):
            entry, repo_path = futures[future]
            try:
                outcomes.append(future.result())
            except Exception as exc:  # noqa: BLE001
                # sync_entry handles HTTP and I/O faults itself, so reaching here
                # means something unforeseen.  Turn it into a FAILED row instead
                # of letting it propagate: one bad file used to abort the whole
                # run and discard the outcomes of every file that had already
                # succeeded, losing the manifest for all of them.
                status = "failed: " + short_error(exc)
                LOGGER.exception("%s: unexpected error", repo_path)
                outcomes.append(
                    SyncOutcome(
                        repo_path,
                        Action.FAILED,
                        build_row(entry, repo_path, entry.size, "", status),
                        status,
                    )
                )
    return outcomes


def print_summary(
    outcomes: Sequence[SyncOutcome],
    deferred: int,
    extras: Sequence[Path],
    pruned: int,
    dest_root: Path,
    dry_run: bool,
) -> int:
    counts: Dict[str, int] = {action: 0 for action in Action.ORDER}
    for outcome in outcomes:
        counts[outcome.action] = counts.get(outcome.action, 0) + 1
    counts[Action.SKIPPED] += deferred

    print()
    print("Drive sync summary ({}{}):".format(dest_root, " - DRY RUN" if dry_run else ""))
    for action in Action.ORDER:
        print("  {:<10} {}".format(action, counts[action]))

    failures = [outcome for outcome in outcomes if outcome.action == Action.FAILED]
    if failures:
        print("\nFailures:")
        for outcome in sorted(failures, key=lambda item: item.repo_path):
            print("  {}: {}".format(outcome.repo_path, outcome.row.status))

    if extras:
        header = "Pruned {} local file(s) not in Drive:".format(pruned) if pruned else (
            "{} local file(s) are no longer in Drive (re-run with --prune to delete):".format(
                len(extras)
            )
        )
        print("\n" + header)
        for path in extras[:50]:
            print("  {}".format(path.relative_to(dest_root).as_posix()))
        if len(extras) > 50:
            print("  ... and {} more".format(len(extras) - 50))

    return 1 if failures else 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    configure_logging(args.verbose)

    if args.jobs < 1:
        raise SystemExit("--jobs must be at least 1")

    dest_root = Path(args.dest).expanduser().resolve()
    manifest_path = dest_root / MANIFEST_NAME
    folder_names: Sequence[str] = args.folder or (
        [] if args.folder_id else list(DEFAULT_FOLDER_NAMES)
    )

    # Everything above this line is argument handling only: no network, no auth.
    modules = load_google_modules()
    credentials = load_credentials(
        modules,
        resolve_credentials_path(args.credentials),
        Path(args.token).expanduser(),
    )
    client = DriveClient(credentials, modules)

    roots = resolve_root_folders(client, folder_names, args.folder_id)
    LOGGER.info(
        "syncing %s into %s",
        ", ".join("{!r} ({})".format(root.name, root.folder_id) for root in roots),
        dest_root,
    )

    entries: List[DriveEntry] = []
    dir_names: Dict[str, Set[str]] = {}
    root_dir_names: List[str] = []
    for root in roots:
        root_entries, root_dirs = walk_root(client, root)
        entries.extend(root_entries)
        for folder_path, names in root_dirs.items():
            dir_names.setdefault(folder_path, set()).update(names)
        root_dir_names.append(sanitize_filename(root.name, "drive-{}".format(root.folder_id)))
    LOGGER.info("found %d file(s) in Drive", len(entries))

    assignments = assign_repo_paths(entries, dir_names)
    expected_paths: Set[str] = set()
    for _entry, repo_path in assignments:
        if repo_path in expected_paths:
            LOGGER.warning("two Drive files map to the same path %s", repo_path)
        expected_paths.add(repo_path)

    previous = read_manifest(manifest_path)

    max_file_bytes = args.max_file_bytes if args.max_file_bytes > 0 else None
    selected: List[Tuple[DriveEntry, str]] = []
    deferred: List[Tuple[DriveEntry, str]] = []
    excluded: List[Tuple[DriveEntry, str, str]] = []
    for entry, repo_path in assignments:
        if not selected_by_only(repo_path, args.only):
            deferred.append((entry, repo_path))
            continue
        reason = excluded_reason(entry, repo_path, args.exclude, max_file_bytes)
        if reason:
            excluded.append((entry, repo_path, reason))
        else:
            selected.append((entry, repo_path))
    if args.only:
        LOGGER.info(
            "--only matched %d of %d file(s); the rest keep their manifest rows",
            len(selected) + len(excluded),
            len(assignments),
        )
    if excluded:
        LOGGER.info(
            "excluded %d file(s) totalling %d bytes; each keeps a manifest row "
            "saying why",
            len(excluded),
            sum(entry.size or 0 for entry, _path, _reason in excluded),
        )
        for _entry, path, reason in excluded:
            LOGGER.debug("excluded %s: %s", path, reason)

    outcomes = run_sync(client, selected, dest_root, previous, args.jobs, args.dry_run)

    rows: List[ManifestRow] = [outcome.row for outcome in outcomes]
    for entry, repo_path in deferred:
        carried = previous.get(repo_path)
        if carried is not None and carried.drive_id == entry.file_id:
            rows.append(carried)
        else:
            rows.append(
                build_row(entry, repo_path, entry.size, "", "not-checked: excluded by --only")
            )
    for entry, repo_path, reason in excluded:
        # An excluded file that is already mirrored keeps the row it earned; the
        # exclusion says "do not fetch this", not "forget what we know about it".
        carried = previous.get(repo_path)
        if carried is not None and carried.drive_id == entry.file_id and carried.md5:
            rows.append(carried)
        else:
            rows.append(build_row(entry, repo_path, entry.size, "", reason))

    extras = find_local_extras(dest_root, root_dir_names, expected_paths)
    pruned = 0
    prune_failures = 0
    if extras and args.prune and not args.dry_run:
        pruned, prune_failures = prune_extras(dest_root, extras)

    if not args.dry_run:
        write_manifest(manifest_path, rows)
        LOGGER.info("wrote %s (%d rows)", manifest_path, len(rows))
    else:
        LOGGER.info("dry run: %s left untouched", manifest_path)

    exit_code = print_summary(
        outcomes, len(deferred), extras, pruned, dest_root, args.dry_run
    )
    return 1 if prune_failures else exit_code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:  # pragma: no cover - interactive use
        print("interrupted", file=sys.stderr)
        sys.exit(130)
