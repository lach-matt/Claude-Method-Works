#!/usr/bin/env python3
"""Consolidate the artefacts sealed inside drive/ into extracted/.

The Drive mirror holds 31 archives (.zip/.tar.gz) and 9 Claude project exports
whose contents are not reachable without unpacking them. This walks all of them
and writes every distinct body exactly once into extracted/, with
extracted/LEDGER.tsv recording what every source occurrence resolved to.

Disposition of each source occurrence, in order of precedence:

  PRESENT-IN-REPO   already tracked under drive/, method/, tools/ or docs/;
                    not written, target_path names the existing file
  DUP-OF-EXTRACTED  same md5 already written from an earlier source;
                    not written, target_path names the single copy
  SKIPPED-DERIVED   compiled bytecode (.pyc), which .gitignore excludes
  EXTRACTED         written to target_path

Archives are visited canonical copy first, so a body lands under the plain
archive name rather than a `__<driveFileId>` or `-1` variant.

A project doc whose filename claims a binary container (.pdf, .docx, ...) holds
extracted *text*, not the original bytes — the export stores no binary. Those
are written with `.txt` appended and the substitution noted in the ledger.

drive/ is input only and is never modified: the MANIFEST.tsv <-> tree bijection
it asserts stays intact.

Regenerate:  python3 tools/consolidate.py
Verify:      python3 tools/consolidate.py --verify

Stdlib only. Idempotent: rerunning reproduces the same tree and ledger.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import tarfile
import unicodedata
import zipfile
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "extracted")
SEARCH = ("drive", "method", "tools", "docs")
TEXT_MASK = (".pdf", ".docx", ".doc", ".pptx", ".xlsx")
LEDGER_COLS = ("source", "member", "size_bytes", "md5",
               "disposition", "target_path", "note")


def md5b(data):
    return hashlib.md5(data).hexdigest()


def slug(text):
    text = unicodedata.normalize("NFKD", text).strip()
    text = re.sub(r"[^\w\s.-]", "", text, flags=re.U)
    text = re.sub(r"[\s_]+", "-", text).strip("-.")
    return text.lower() or "untitled"


def index_repo():
    """md5 -> first repo-relative path, for everything already tracked."""
    have = {}
    for sub in SEARCH:
        for dirpath, _, names in os.walk(os.path.join(ROOT, sub)):
            for name in names:
                path = os.path.join(dirpath, name)
                try:
                    data = open(path, "rb").read()
                except OSError:
                    continue
                have.setdefault(md5b(data), os.path.relpath(path, ROOT))
    return have


def find_archives():
    """Archives in drive/, canonical copies first."""
    found = []
    for dirpath, _, names in os.walk(os.path.join(ROOT, "drive")):
        for name in names:
            if name.endswith((".zip", ".tgz")) or (name.endswith(".gz") and ".tar" in name):
                found.append(os.path.join(dirpath, name))
    found.sort(key=lambda p: ("__" in os.path.basename(p),
                              ".tar-1." in p or "-1." in os.path.basename(p),
                              len(p), p))
    return found


def archive_dirname(path):
    base = os.path.basename(path)
    for suffix in (".tar.gz", ".tar-1.gz", ".tgz", ".zip", ".gz"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    return slug(re.sub(r"__[A-Za-z0-9_-]{20,}$", "", base))


def iter_archive(path):
    """Yield (member_name, bytes) for every regular file in the archive."""
    if path.endswith(".zip"):
        with zipfile.ZipFile(path) as zf:
            for info in zf.infolist():
                if not info.is_dir():
                    yield info.filename, zf.read(info)
    else:
        with tarfile.open(path, "r:gz") as tf:
            for member in tf:
                if not member.isfile():
                    continue
                handle = tf.extractfile(member)
                if handle is not None:
                    yield member.name, handle.read()


class Consolidator:
    def __init__(self):
        self.have = index_repo()
        self.placed = {}
        self.ledger = []

    def consider(self, data, target_rel, source, member, note=""):
        digest = md5b(data)
        if member.lower().endswith(".pyc"):
            self._row(source, member, data, digest, "SKIPPED-DERIVED", "",
                      "compiled bytecode; .gitignore excludes *.py[cod]")
            return
        if digest in self.have:
            self._row(source, member, data, digest, "PRESENT-IN-REPO",
                      self.have[digest],
                      note or "byte-identical to a file already tracked")
            return
        if digest in self.placed:
            self._row(source, member, data, digest, "DUP-OF-EXTRACTED",
                      self.placed[digest], note)
            return
        path = os.path.join(ROOT, target_rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as fh:
            fh.write(data)
        self.placed[digest] = target_rel
        self._row(source, member, data, digest, "EXTRACTED", target_rel, note)

    def _row(self, source, member, data, digest, disposition, target, note):
        self.ledger.append((source, member, len(data), digest,
                            disposition, target, note))

    def run_archives(self):
        for path in find_archives():
            rel = os.path.relpath(path, ROOT)
            into = archive_dirname(path)
            try:
                for member, data in iter_archive(path):
                    self.consider(data,
                                  "extracted/archives/%s/%s" % (into, member.lstrip("./")),
                                  rel, member)
            except (tarfile.TarError, zipfile.BadZipFile, OSError) as exc:
                self.ledger.append((rel, "", 0, "", "ERROR", "", str(exc)))

    def run_projects(self):
        folder = os.path.join(ROOT, "drive", "The Method Materials", "Claude Projects")
        projects = []
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".json"):
                continue
            path = os.path.join(folder, name)
            export = json.load(open(path))
            rel = os.path.relpath(path, ROOT)
            title = (export.get("name") or "").strip()
            docs = export.get("docs", [])
            into = slug(title) if title else export["uuid"]
            projects.append({
                "project_uuid": export["uuid"], "name": title,
                "created_at": export.get("created_at", ""),
                "updated_at": export.get("updated_at", ""),
                "doc_count": str(len(docs)),
                "extract_dir": into if docs else "", "source": rel,
            })
            for doc in docs:
                body = doc.get("content", "").encode()
                filename = doc.get("filename") or doc.get("uuid", "doc")
                note = ""
                if filename.lower().endswith(TEXT_MASK):
                    filename += ".txt"
                    note = ("stored content is extracted text, not the original "
                            "binary; .txt appended")
                self.consider(body, "extracted/projects/%s/%s" % (into, filename),
                              rel, doc.get("filename", ""), note)
        return projects

    def write_reports(self, projects):
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, "LEDGER.tsv"), "w", newline="") as fh:
            fh.write("\t".join(LEDGER_COLS) + "\n")
            for row in sorted(self.ledger, key=lambda r: (r[0], r[1])):
                fh.write("\t".join(str(c).replace("\t", " ") for c in row) + "\n")
        cols = ("project_uuid", "name", "created_at", "updated_at",
                "doc_count", "extract_dir", "source")
        with open(os.path.join(OUT, "PROJECT-INDEX.tsv"), "w", newline="") as fh:
            fh.write("\t".join(cols) + "\n")
            for p in sorted(projects, key=lambda p: p["name"]):
                fh.write("\t".join(p[c] for c in cols) + "\n")


def verify():
    ledger = os.path.join(OUT, "LEDGER.tsv")
    if not os.path.isfile(ledger):
        print("no ledger at %s; run without --verify first" % ledger)
        return 1
    checked = bad = dangling = 0
    with open(ledger) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            disposition = row["disposition"]
            target = os.path.join(ROOT, row["target_path"])
            if disposition == "EXTRACTED":
                checked += 1
                if not os.path.isfile(target):
                    bad += 1
                    print("MISSING  %s" % row["target_path"])
                    continue
                data = open(target, "rb").read()
                if md5b(data) != row["md5"] or str(len(data)) != row["size_bytes"]:
                    bad += 1
                    print("MISMATCH %s" % row["target_path"])
            elif disposition in ("DUP-OF-EXTRACTED", "PRESENT-IN-REPO"):
                if not os.path.isfile(target):
                    dangling += 1
                    print("DANGLING %s" % row["target_path"])
    print("verified %d extracted files: %d bad, %d dangling pointers"
          % (checked, bad, dangling))
    return 1 if (bad or dangling) else 0


def main():
    worker = Consolidator()
    worker.run_archives()
    projects = worker.run_projects()
    worker.write_reports(projects)
    counts = Counter(row[4] for row in worker.ledger)
    print("ledger rows: %d" % len(worker.ledger))
    for disposition, count in counts.most_common():
        print("  %-18s %d" % (disposition, count))
    written = sum(row[2] for row in worker.ledger if row[4] == "EXTRACTED")
    print("distinct bodies written: %d (%s bytes)"
          % (len(worker.placed), format(written, ",")))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--verify", action="store_true",
                        help="re-hash the extracted tree against LEDGER.tsv and exit")
    sys.exit(verify() if parser.parse_args().verify else main())
