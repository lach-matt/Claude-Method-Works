#!/usr/bin/env python3
"""Recover the artefacts the chats wrote, out of the sharded export.

`drive/chats` holds 352 conversations. Inside them the work was repeatedly
written to disk with a shell heredoc:

    cat > /mnt/user-data/outputs/HANDOFF-16.md <<'EOF'
    # HANDOFF-16 - The Method 1.6
    ...
    EOF

That form is **self-labelling and exact**: it names its own target file and
delimits its own body, so recovery needs no guessing about where a document
starts or ends. This walks every shard, extracts every such write, and lands
each distinct body once in `recovered/`.

**These are RECOVERED, not mirrored.** The status word is the corpus's own
(CLAUDE.md): the bytes were measured out of the chat export rather than fetched
from the file they were written to. No claim is made that a recovered file is
byte-identical to a copy held anywhere else, and nothing here is a member of any
bundle. `drive/` remains the mirror of record.

A second form carries a body without naming it: a `code_block` node whose
`code` begins with the document's own Markdown heading. That is exact text, but
the filename has to be **inferred from the heading**, so it is a weaker claim and
carries its own status, `RECOVERED-BY-HEADING`. To avoid manufacturing files out
of arbitrary headings, this rule is applied **only to names `COVERAGE.tsv`
already says the corpus asks for** - it recovers what is known to be missing and
invents nothing.

**What this deliberately does not recover.** A file *uploaded* into a chat
appears in the export as a `files` entry carrying `file_name` and `file_uuid`
and **no content at all**, so its bytes are simply not present and no tool can
produce them. Bodies shown only as a `view` tool result carry line numbers and a
tab, and de-numbering them would be reconstruction rather than recovery, so they
are left alone. Only the heredoc rule is applied.

Versions: 147 names were written more than once with differing content, because
the work evolved. Every distinct body is kept. The one from the newest
conversation keeps the plain name; the others take a `__<md5 prefix>` suffix
before the extension, mirroring how `drive/` already distinguishes same-titled
Drive copies.

Regenerate:  python3 tools/recover.py
Verify:      python3 tools/recover.py --verify
Selftest:    python3 tools/recover.py --selftest

Stdlib only. Idempotent.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHATS = os.path.join(ROOT, "drive", "chats")
OUT = os.path.join(ROOT, "recovered")
LEDGER = os.path.join(OUT, "LEDGER.tsv")
SEARCH = ("drive", "method", "tools", "docs", "extracted")

HEREDOC = re.compile(
    r"cat\s*>\s*(?:'([^']+)'|\"([^\"]+)\"|(\S+))\s*<<\s*'?(\w+)'?\n(.*?)\n\4", re.S)
BLOCK_HEAD = re.compile(r"^#+[ \t]*([A-Za-z0-9][A-Za-z0-9._-]{2,60})")
COVERAGE = os.path.join(ROOT, "COVERAGE.tsv")
# A chat that showed a file through a paging viewer elides the middle and says so.
# Capturing that display yields a body that is valid text, hashes cleanly, and is
# silently missing content -- so it must be labelled, not trusted.
TRUNCATED = re.compile(rb"<[ ]*truncated lines (\d+)-(\d+)[ ]*>")
COLS = ("filename", "md5", "size_bytes", "status", "target_path",
        "source_shard", "conversation", "created_at", "versions", "note")


def md5b(data):
    return hashlib.md5(data).hexdigest()


def walk_strings(obj, out):
    if isinstance(obj, str):
        out.append(obj)
    elif isinstance(obj, dict):
        for value in obj.values():
            walk_strings(value, out)
    elif isinstance(obj, list):
        for value in obj:
            walk_strings(value, out)


def repo_md5s():
    """Everything already tracked, so a recovered body is never a second copy."""
    have = set()
    for sub in SEARCH:
        for dirpath, _, names in os.walk(os.path.join(ROOT, sub)):
            if os.path.abspath(dirpath).startswith(os.path.abspath(CHATS)):
                continue
            for name in names:
                try:
                    have.add(md5b(open(os.path.join(dirpath, name), "rb").read()))
                except OSError:
                    pass
    return have


def shard_index():
    """shard_path -> (title, created_at), from the export's own INDEX.tsv."""
    path = os.path.join(CHATS, "INDEX.tsv")
    if not os.path.isfile(path):
        return {}
    with open(path) as handle:
        return {r["shard_path"]: (r["title"], r["created_at"])
                for r in csv.DictReader(handle, delimiter="\t")}


def harvest():
    """filename -> md5 -> (shard, body). Every heredoc write in every shard."""
    found = defaultdict(dict)
    shards = 0
    for dirpath, _, names in os.walk(CHATS):
        for name in sorted(names):
            if not name.endswith(".json") or name == "SUMMARY.json":
                continue
            path = os.path.join(dirpath, name)
            try:
                doc = json.load(open(path))
            except (OSError, ValueError):
                continue
            shards += 1
            rel = os.path.relpath(path, CHATS)
            buf = []
            walk_strings(doc, buf)
            for text in buf:
                if "cat" not in text or "<<" not in text:
                    continue
                for match in HEREDOC.finditer(text):
                    target = match.group(1) or match.group(2) or match.group(3)
                    body = match.group(5).encode()
                    found[os.path.basename(target)].setdefault(md5b(body), (rel, body))
    return found, shards


def census_wanted():
    """Every artefact name the corpus itself names, whatever its current status.

    NOT filtered on status. COVERAGE.tsv is regenerated *from* recovered/, so a
    name this tool successfully recovers turns HELD on the next census -- and
    filtering on "not held" would then hide it from the code-block rule, so a
    second run would silently produce a smaller tree than the first. Reading the
    artefact column alone keeps the rule a pure function of the corpus, which is
    what makes the tool idempotent.
    """
    if not os.path.isfile(COVERAGE):
        return set()
    with open(COVERAGE) as handle:
        return {r["artefact"] for r in csv.DictReader(handle, delimiter="\t")}


def walk_blocks(obj, out):
    if isinstance(obj, dict):
        if obj.get("type") == "code_block" and isinstance(obj.get("code"), str):
            out.append(obj["code"])
        for value in obj.values():
            walk_blocks(value, out)
    elif isinstance(obj, list):
        for value in obj:
            walk_blocks(value, out)


def harvest_blocks(wanted):
    """filename -> md5 -> (shard, body), from heading-matched code blocks."""
    found = defaultdict(dict)
    if not wanted:
        return found
    for dirpath, _, names in os.walk(CHATS):
        for name in sorted(names):
            if not name.endswith(".json") or name == "SUMMARY.json":
                continue
            path = os.path.join(dirpath, name)
            try:
                doc = json.load(open(path))
            except (OSError, ValueError):
                continue
            rel = os.path.relpath(path, CHATS)
            blocks = []
            walk_blocks(doc, blocks)
            for code in blocks:
                match = BLOCK_HEAD.match(code.lstrip("\n"))
                if not match:
                    continue
                stem = match.group(1)
                for candidate in (stem + ".md", stem):
                    if candidate in wanted:
                        body = code.encode()
                        found[candidate].setdefault(md5b(body), (rel, body))
    return found


def _negate_date(value):
    """Sort key that puts the newest date first while ascending."""
    return tuple(-ord(c) for c in value)


def target_for(filename, digest, newest):
    if digest == newest:
        return filename
    stem, ext = os.path.splitext(filename)
    return "%s__%s%s" % (stem, digest[:8], ext)


def build(write=True):
    found, shards = harvest()
    have = repo_md5s()
    index = shard_index()
    # second rule: only for names the census already asks for
    wanted = census_wanted() - set(found)
    blocks = harvest_blocks(wanted)
    origin = {}
    for name in found:
        origin[name] = "RECOVERED"
    for name, versions in blocks.items():
        origin.setdefault(name, "RECOVERED-BY-HEADING")
        found[name].update(versions)
    rows = []
    written = 0
    for filename in sorted(found):
        versions = found[filename]
        # A complete body always outranks a truncated one for the plain name, and
        # only then does recency decide. Ordering on date alone hands the canonical
        # name to whichever conversation was latest -- which for HANDOFF-37/38/39
        # is the one showing an elided view, leaving the full text hidden behind a
        # __<md5> suffix. Completeness first, then newest.
        ordered = sorted(
            versions.items(),
            key=lambda kv: (bool(TRUNCATED.search(kv[1][1])),
                            _negate_date(index.get(kv[1][0], ("", ""))[1])))
        newest = ordered[0][0]
        for digest, (shard, body) in ordered:
            title, created = index.get(shard, ("", ""))
            if digest in have:
                rows.append((filename, digest, len(body), "PRESENT-IN-REPO", "",
                             shard, title, created, len(versions), ""))
                continue
            elided = TRUNCATED.findall(body)
            note = ""
            status = origin[filename]
            if elided:
                lost = sum(int(b) - int(a) + 1 for a, b in elided)
                status = "RECOVERED-TRUNCATED"
                note = ("INCOMPLETE: %d line(s) elided by the chat's own display "
                        "across %d marker(s)" % (lost, len(elided)))
            target = os.path.join("recovered", target_for(filename, digest, newest))
            if write:
                dest = os.path.join(ROOT, target)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as handle:
                    handle.write(body)
                written += 1
            rows.append((filename, digest, len(body), status, target,
                         shard, title, created, len(versions), note))
    if write:
        os.makedirs(OUT, exist_ok=True)
        with open(LEDGER, "w", newline="") as handle:
            handle.write("\t".join(COLS) + "\n")
            for row in rows:
                handle.write("\t".join(str(c).replace("\t", " ") for c in row) + "\n")
    return rows, shards, written


def verify():
    if not os.path.isfile(LEDGER):
        print("no ledger; run without --verify first")
        return 1
    checked = bad = 0
    with open(LEDGER) as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if not row["status"].startswith("RECOVERED"):
                continue
            checked += 1
            path = os.path.join(ROOT, row["target_path"])
            if not os.path.isfile(path):
                bad += 1
                print("MISSING  %s" % row["target_path"])
                continue
            data = open(path, "rb").read()
            if md5b(data) != row["md5"] or str(len(data)) != row["size_bytes"]:
                bad += 1
                print("MISMATCH %s" % row["target_path"])
    print("verified %d recovered file(s): %d bad" % (checked, bad))
    return 1 if bad else 0


def selftest():
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-52s = %-6s expected %-6s %s" % (label, got, want, "ok" if good else "FAIL"))

    found, shards = harvest()
    check("shards in the export", shards, 352)
    check("distinct filenames written by heredoc", len(found), 2015)
    check("distinct bodies", sum(len(v) for v in found.values()), 2196)
    check("HANDOFF-16.md recovered", "HANDOFF-16.md" in found, True)
    body = list(found.get("HANDOFF-16.md", {}).values())
    check("its body opens with its own title line",
          bool(body) and body[0][1].startswith(b"# HANDOFF-16"), True)
    check("names with more than one version",
          sum(1 for v in found.values() if len(v) > 1), 147)
    blocks = harvest_blocks(census_wanted() - set(found))
    check("census names reached only by the code-block rule", len(blocks), 123)
    trunc = sum(1 for vs in found.values() for _, b in vs.values() if TRUNCATED.search(b))
    check("bodies carrying a truncation marker", trunc, 23)
    check("HANDOFF-47.md among them", "HANDOFF-47.md" in blocks, True)
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    rows, shards, written = build(write=True)
    counts = Counter(r[3] for r in rows)
    print("shards read: %d" % shards)
    print("ledger rows: %d" % len(rows))
    for status, count in counts.most_common():
        print("  %-16s %d" % (status, count))
    total = sum(r[2] for r in rows if r[3].startswith("RECOVERED"))
    print("recovered: %d file(s), %s bytes" % (written, format(total, ",")))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--verify", action="store_true",
                        help="re-hash the recovered tree against LEDGER.tsv")
    parser.add_argument("--selftest", action="store_true",
                        help="assert the corpus's own recorded numbers")
    args = parser.parse_args()
    sys.exit(verify() if args.verify else selftest() if args.selftest else main())
