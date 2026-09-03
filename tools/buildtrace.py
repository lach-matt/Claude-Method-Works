#!/usr/bin/env python3
"""tools/buildtrace.py -- provenance across the BUILD series.

The archive holds the build series as snapshots: The_Method_1_6_BUILD<N>_*.md,
BUILD9 to BUILD179, in two streams, 596 MiB in 140 files. They are the only
record of when a figure entered the books and when it changed. Answering
"which build introduced this number" by hand means grepping a third of a
gigabyte, which CLAUDE.md forbids outright:

    "Do not read or grep the tree wholesale: start from MANIFEST.tsv, then run
     targeted ls/grep against specific paths."

So this starts from MANIFEST.tsv, and every mode that touches the tree states
its byte budget first and refuses to exceed it. DOCKET.md section 2: "State a
budget rather than a negative when a computation is too large."

    python3 tools/buildtrace.py --builds              # from the manifest; reads no build
    python3 tools/buildtrace.py --first "976 cells"   # bisect: ~9 reads, not 119
    python3 tools/buildtrace.py --trace "976 cells" --stream main
    python3 tools/buildtrace.py --verify 90
    python3 tools/buildtrace.py --selftest

Stdlib only, Python 3.9+.

Three things it refuses to do:

  1. It never scans the tree wholesale without saying what that costs. Every
     tree-touching mode prints "budget: N files, X MiB" and --trace refuses
     over --budget (default 256 MiB) rather than quietly reading 596.

  2. It never reports a first-appearance from a bisect without checking that
     the token is monotone. A bisect is only valid if a token, once
     introduced, stays; if the newest build lacks it, the token was withdrawn,
     the bisect is meaningless, and it says NON-MONOTONE instead of a number.

  3. It never merges a build's variant copies. A ".REPAIRED", a "-1" and a
     "__<driveFileId>" copy are all deliberate (CLAUDE.md: "Both are
     intentional -- do not merge or delete either"), so the canonical plain
     name is traced and the variants are listed, never silently averaged in.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_MANIFEST = os.path.join(REPO, "drive", "MANIFEST.tsv")
DEFAULT_TREE = os.path.join(REPO, "drive")
STORE = os.path.join(REPO, "method")

# The live bundles, which are the newest members of the two streams.
# The live bundles, which are the newest members of the two streams. Named here as
# method/verify.py names them on this branch; a build that advances either must move both.
LIVE = {
    "main": ("The_Method_1_6_BUILD94_main_and_register.md",
             "6079e066b5e480db6c47f754660a9b6e"),
    "compendia": ("The_Method_1_6_BUILD192_compendia_papers_audits.md",
                  "3ad4c61d720fc0b9af669984039d6cfa"),
}

STREAMS = {"compendia": "compendia_papers_audits", "main": "main_and_register"}

RE_BUILD = re.compile(
    r"The_Method_1_6_BUILD(?P<n>\d+)_"
    r"(?P<stream>compendia_papers_audits|main_and_register)"
    r"(?P<variant>|\.REPAIRED|-1|__[A-Za-z0-9_-]+)\.md$"
)

CHUNK = 1 << 20


class Build:
    __slots__ = ("n", "stream", "variant", "repo_path", "size", "md5", "folder")

    def __init__(self, n, stream, variant, repo_path, size, md5):
        self.n = n
        self.stream = stream
        self.variant = variant
        self.repo_path = repo_path
        self.size = size
        self.md5 = md5
        self.folder = os.path.dirname(repo_path)

    @property
    def canonical(self):
        return self.variant == ""

    @property
    def label(self):
        return "BUILD%d%s" % (self.n, self.variant)

    def path(self, tree=DEFAULT_TREE):
        return os.path.join(tree, self.repo_path)

    def asdict(self):
        return {"build": self.n, "stream": self.stream,
                "variant": self.variant, "canonical": self.canonical,
                "repo_path": self.repo_path, "size": self.size,
                "md5": self.md5}


def read_series(manifest=DEFAULT_MANIFEST):
    """The build series, from MANIFEST.tsv alone. Reads no build file.

    CLAUDE.md: the manifest is the entry point and is never hand-edited; the
    manifest and the tree are an exact bijection. Everything here -- which
    builds exist, their size, their md5 -- comes from it."""
    out = []
    with open(manifest, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        col = {name: i for i, name in enumerate(header)}
        for line in fh:
            row = line.rstrip("\n").split("\t")
            if len(row) < len(header):
                continue
            repo_path = row[col["repo_path"]]
            m = RE_BUILD.search(repo_path)
            if not m:
                continue
            out.append(Build(int(m.group("n")), m.group("stream"),
                             m.group("variant"), repo_path,
                             int(row[col["drive_size_bytes"]] or 0),
                             row[col["md5"]]))
    out.sort(key=lambda b: (b.stream, b.n, b.variant))
    return out


def select(series, stream=None, canonical_only=True, folder=None):
    out = series
    if stream:
        out = [b for b in out if b.stream == STREAMS[stream]]
    if canonical_only:
        out = [b for b in out if b.canonical]
    if folder is not None:
        out = [b for b in out if b.folder == folder]
    return sorted(out, key=lambda b: (b.n, b.variant))


def primary_folder(series):
    """The folder the series proper lives in. The delivery subfolders hold
    their own copies of a handful of builds; tracing across both would
    interleave two histories."""
    counts = {}
    for b in select(series, canonical_only=True):
        counts[b.folder] = counts.get(b.folder, 0) + 1
    return max(counts, key=counts.get) if counts else ""


# ---------------------------------------------------------------------------
# Counting
# ---------------------------------------------------------------------------

def count_in(path, token, chunk=CHUNK):
    """Occurrences of a fixed string, streamed.

    The overlap is why a token straddling a chunk boundary is still counted:
    without carrying the last len(token)-1 bytes forward, a 596 MiB scan
    silently loses roughly one occurrence per megabyte boundary."""
    needle = token.encode("utf-8")
    keep = len(needle) - 1
    total = 0
    tail = b""
    with open(path, "rb") as fh:
        while True:
            block = fh.read(chunk)
            if not block:
                break
            buf = tail + block
            total += buf.count(needle)
            tail = buf[-keep:] if keep else b""
    return total


def md5_of(path, chunk=CHUNK):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


class Cache:
    """Counts, keyed by the file's manifest md5 and the token. A build is a
    snapshot and never changes, so a count once measured is permanent."""

    def __init__(self, path):
        self.path = path
        self.data = {}
        if path and os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    self.data = json.load(fh)
            except (ValueError, OSError):
                self.data = {}

    def get(self, md5, token):
        return self.data.get(md5 + "\t" + token)

    def put(self, md5, token, n):
        self.data[md5 + "\t" + token] = n

    def flush(self):
        if not self.path:
            return
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, "w", encoding="utf-8") as fh:
                json.dump(self.data, fh)
        except OSError:
            pass


def counted(build, token, tree, cache, reads):
    hit = cache.get(build.md5, token) if cache else None
    if hit is not None:
        return hit, False
    n = count_in(build.path(tree), token)
    if cache:
        cache.put(build.md5, token, n)
    reads.append(build)
    return n, True


def transitions(counts):
    """The builds where a count changes, labelled.

    Pure, so the labelling is unit-tested rather than inferred from a 448 MiB
    scan. counts is [(build number, count)] in series order; a token absent
    throughout yields nothing at all -- printing "BUILD9 0 WITHDRAWN" for
    something that was never there states a withdrawal that never happened."""
    out = []
    prev = 0
    for n, c in counts:
        if c == prev:
            continue
        out.append((n, c, "first appears" if prev == 0
                    else "WITHDRAWN" if c == 0 else "changes"))
        prev = c
    return out


def budget(builds, label="budget"):
    total = sum(b.size for b in builds)
    print("%s: %d file%s, %.1f MiB"
          % (label, len(builds), "" if len(builds) == 1 else "s",
             total / 1048576.0))
    return total


# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------

def mode_builds(series, stream, variants):
    for name, key in sorted(STREAMS.items()):
        if stream and stream != name:
            continue
        rows = select(series, name, canonical_only=not variants)
        if not rows:
            continue
        total = sum(b.size for b in rows)
        print("%s stream (%s): %d files, %.1f MiB, BUILD%d to BUILD%d"
              % (name, key, len(rows), total / 1048576.0,
                 rows[0].n, rows[-1].n))
        folders = {}
        for b in rows:
            folders.setdefault(b.folder, []).append(b.n)
        for folder, ns in sorted(folders.items()):
            print("    %-46s %3d: %s"
                  % (folder or ".", len(ns),
                     ", ".join(str(n) for n in sorted(set(ns)))))
        var = [b for b in select(series, name, canonical_only=False)
               if not b.canonical]
        if var and not variants:
            print("    %d variant cop%s not traced (--variants lists them): %s"
                  % (len(var), "y" if len(var) == 1 else "ies",
                     ", ".join(sorted(b.label for b in var))))
        print()
    return 0


def mode_first(series, token, stream, tree, cache, cap):
    """Bisect for the first build containing a fixed string.

    Refusal 2: valid only if the token is monotone -- once in, it stays. The
    endpoints are measured first, so a token that was WITHDRAWN is reported as
    non-monotone rather than as a first appearance that does not mean
    anything."""
    rows = select(series, stream, folder=primary_folder(series))
    if len(rows) < 2:
        print("not enough builds in the %s stream to bisect" % (stream or "?"))
        return 2
    reads = []
    lo_n, hi_n = rows[0], rows[-1]
    print("series: %s BUILD%d to BUILD%d, %d builds"
          % (stream or "both", lo_n.n, hi_n.n, len(rows)))
    print("bisect reads about %d of them" % (len(rows).bit_length() + 1))

    first_c, _ = counted(rows[0], token, tree, cache, reads)
    last_c, _ = counted(rows[-1], token, tree, cache, reads)
    if last_c == 0 and first_c == 0:
        print()
        print("ABSENT from both endpoints (BUILD%d and BUILD%d)."
              % (lo_n.n, hi_n.n))
        print("  That is not absence from the series: a token added and later "
              "withdrawn is absent at both ends.")
        print("  Only --trace can settle it, and only for the builds the "
              "archive holds.")
        budget(reads, "read")
        return 1
    if last_c == 0:
        print()
        print("WITHDRAWN, so NON-MONOTONE: present in the oldest build "
              "(BUILD%d, %d occurrence%s) and absent from the newest "
              "(BUILD%d)." % (lo_n.n, first_c, "" if first_c == 1 else "s",
                              hi_n.n))
        print("  A bisect locates a first appearance only for a token that "
              "persists; this one does not.")
        print("  Use --trace for the whole series; it will show where it went.")
        budget(reads, "read")
        return 1
    if first_c:
        print()
        print("present in the OLDEST build in the series (BUILD%d), %d "
              "occurrence%s" % (lo_n.n, first_c, "" if first_c == 1 else "s"))
        print("  Its introduction predates the series; the archive cannot "
              "date it.")
        budget(reads, "read")
        return 0

    lo, hi = 0, len(rows) - 1          # rows[lo] absent, rows[hi] present
    while hi - lo > 1:
        mid = (lo + hi) // 2
        c, _ = counted(rows[mid], token, tree, cache, reads)
        if c:
            hi = mid
        else:
            lo = mid
    print()
    print("FIRST APPEARANCE  BUILD%d  (%s)" % (rows[hi].n, rows[hi].repo_path))
    c, _ = counted(rows[hi], token, tree, cache, reads)
    print("  BUILD%-4d %d occurrence%s" % (rows[hi].n, c,
                                           "" if c == 1 else "s"))
    print("  BUILD%-4d absent  (the build immediately before it in the series)"
          % rows[lo].n)
    print("  Monotone at the endpoints; the series has gaps, so BUILD%d is the "
          "first build PRESENT IN THE ARCHIVE that carries it." % rows[hi].n)
    budget(reads, "read")
    return 0


def mode_trace(series, token, stream, tree, cache, cap):
    rows = select(series, stream, folder=primary_folder(series))
    unread = [b for b in rows if cache.get(b.md5, token) is None]
    total = budget(unread or rows, "budget")
    if unread and total > cap:
        print()
        print("REFUSED: %.1f MiB exceeds the %.1f MiB budget."
              % (total / 1048576.0, cap / 1048576.0))
        print("  --first bisects the same question in about %d reads."
              % (len(rows).bit_length() + 1))
        print("  --stream main is %.1f MiB; raise the ceiling with --budget."
              % (sum(b.size for b in select(series, "main",
                                            folder=primary_folder(series)))
                 / 1048576.0))
        return 2
    print()
    reads = []
    counts = []
    for b in rows:
        c, _ = counted(b, token, tree, cache, reads)
        counts.append((b, c))
    rows_t = transitions([(b.n, c) for b, c in counts])
    print("transitions in %r (only the builds where the count changes):"
          % token)
    print()
    if not rows_t:
        print("  none -- absent from all %d builds read" % len(counts))
    for n, c, label in rows_t:
        print("  BUILD%-5d %-6d %s" % (n, c, label))
    print()
    nz = [c for _, c in counts if c]
    print("%d builds read, present in %d of them, count %s"
          % (len(counts), len(nz),
             "steady at %d" % nz[0] if nz and len(set(nz)) == 1
             else "%d to %d" % (min(nz), max(nz)) if nz else "0 throughout"))
    if reads:
        budget(reads, "read")
    return 0


def mode_verify(series, which, tree):
    """The mirror's own guarantee, re-asserted: the on-disk file against the
    md5 the manifest records for it."""
    rows = [b for b in series if which is None or b.n == which]
    if not rows:
        print("no build %s in the manifest" % which)
        return 2
    budget(rows, "budget")
    print()
    bad = 0
    for b in sorted(rows, key=lambda x: (x.stream, x.n, x.variant)):
        path = b.path(tree)
        if not os.path.exists(path):
            print("  MISSING  %s" % b.repo_path)
            bad += 1
            continue
        got = md5_of(path)
        ok = got == b.md5
        size_ok = os.path.getsize(path) == b.size
        print("  %-8s %-12s %s%s"
              % ("OK" if ok and size_ok else "MISMATCH", b.label, b.repo_path,
                 "" if ok and size_ok else "  (md5 %s, manifest %s)"
                 % (got[:12], b.md5[:12])))
        if not (ok and size_ok):
            bad += 1
    print()
    print("%d checked, %d bad" % (len(rows), bad))
    return 0 if not bad else 1


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def selftest(manifest, tree):
    fails = []
    checked = 0

    def check(cond, msg):
        nonlocal checked
        checked += 1
        if not cond:
            fails.append(msg)

    series = read_series(manifest)
    check(bool(series), "no build files found in the manifest")

    canon = select(series, canonical_only=True)
    main = select(series, "main", folder=primary_folder(series))
    comp = select(series, "compendia", folder=primary_folder(series))
    check(len(main) >= 12, "main_and_register stream has %d canonical builds "
                           "in the primary folder, expected >= 12" % len(main))
    check(len(comp) >= 100, "compendia stream has %d canonical builds in the "
                            "primary folder, expected >= 100" % len(comp))
    check(comp[0].n == 9, "the compendia series starts at BUILD%d, expected 9"
          % comp[0].n)

    # Ordering must be by build number, since higher N is newer.
    check(all(a.n < b.n for a, b in zip(comp, comp[1:])),
          "the compendia series is not strictly increasing in build number")

    # The manifest and the tree are an exact bijection (CLAUDE.md), so every
    # build row must have a file.
    absent = [b.repo_path for b in canon if not os.path.exists(b.path(tree))]
    check(not absent, "%d canonical build rows have no file on disk: %s"
          % (len(absent), absent[:3]))

    # Variants are recognised and kept apart, never merged.
    variants = [b for b in series if not b.canonical]
    check(bool(variants), "no variant copies recognised; the .REPAIRED, -1 "
                          "and __<driveFileId> forms should parse")
    check(all(b.canonical for b in canon), "select() leaked a variant")

    # The chunk-boundary overlap. Without the carry a token straddling the
    # boundary is lost, which is the one bug a streamed count can hide.
    tmp = os.path.join(os.path.dirname(os.path.abspath(manifest)),
                       ".buildtrace-selftest.tmp")
    try:
        with open(tmp, "wb") as fh:
            fh.write(b"x" * 30 + b"NEEDLE" + b"y" * 30)
        for chunk in (1, 2, 3, 7, 31, 32, 33, 64, 4096):
            got = count_in(tmp, "NEEDLE", chunk=chunk)
            check(got == 1, "count_in with chunk=%d found %d NEEDLE, "
                            "expected 1" % (chunk, got))
        check(count_in(tmp, "x" * 30, chunk=4) == 1,
              "count_in lost a 30-byte token at chunk=4")
        check(count_in(tmp, "ABSENT", chunk=8) == 0,
              "count_in invented an absent token")
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

    # The transition labeller, which is what a 448 MiB scan reports through.
    for counts, want in [
            ([(9, 0), (10, 0)], []),
            ([(9, 3), (10, 3)], [(9, 3, "first appears")]),
            ([(9, 0), (10, 2), (11, 2), (12, 5)],
             [(10, 2, "first appears"), (12, 5, "changes")]),
            ([(9, 4), (10, 0)],
             [(9, 4, "first appears"), (10, 0, "WITHDRAWN")]),
            ([(9, 0), (10, 1), (11, 0), (12, 1)],
             [(10, 1, "first appears"), (11, 0, "WITHDRAWN"),
              (12, 1, "first appears")]),
    ]:
        check(transitions(counts) == want,
              "transitions(%s) = %s, expected %s"
              % (counts, transitions(counts), want))

    # A dated withdrawal, on two targeted reads rather than a series scan.
    # DEFECT-CENSUS row 2 records "Theorem 7.1 is absent -- withdrawn". The
    # main stream carries the token twice through BUILD10 -- the statement and
    # a citation -- and once from BUILD54 on. That dates the withdrawal.
    main_by_n = {b.n: b for b in main}
    for n, want in ((10, 2), (54, 1)):
        if n not in main_by_n:
            check(False, "the main stream has no BUILD%d to date the "
                         "Theorem 7.1 withdrawal against" % n)
            continue
        checked += 1
        got = count_in(main_by_n[n].path(tree), "Theorem 7.1")
        if got != want:
            fails.append("BUILD%d main carries 'Theorem 7.1' %d time(s), "
                         "expected %d (census row 2 dates the withdrawal to "
                         "BUILD54)" % (n, got, want))

    # The store and the archive must agree on the live bundles. This is what
    # drive/ is for: Ruling 56 makes Prints & Proofs the original-input
    # witness, and a witness that disagrees with the store is the finding.
    for stream, (fname, want_md5) in sorted(LIVE.items()):
        rows = [b for b in series if os.path.basename(b.repo_path) == fname]
        store = os.path.join(STORE, fname)
        if not os.path.exists(store):
            check(False, "the store has no %s" % fname)
            continue
        checked += 1
        got = md5_of(store)
        if got != want_md5:
            fails.append("the store's %s is md5 %s; CLAUDE.md section 3 "
                         "records %s" % (fname, got, want_md5))
        if rows:
            checked += 1
            if rows[0].md5 != want_md5:
                fails.append("the archive's %s is md5 %s; the store's live "
                             "bundle is %s -- store and witness disagree"
                             % (fname, rows[0].md5, want_md5))
        else:
            print("  note: the archive does not mirror %s (the live %s "
                  "bundle); nothing to cross-check" % (fname, stream))

    print("fixtures checked: %d  failed: %d" % (checked, len(fails)))
    for f in fails:
        print("  FAIL " + f)
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED")
    return 0 if not fails else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Provenance across the BUILD series.")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST)
    ap.add_argument("--tree", default=DEFAULT_TREE)
    ap.add_argument("--cache",
                    default=os.path.join(REPO, ".buildtrace-cache.json"),
                    help="counts, keyed by manifest md5; a snapshot never "
                         "changes so a count is permanent")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--stream", choices=sorted(STREAMS))
    ap.add_argument("--variants", action="store_true",
                    help="--builds: list the .REPAIRED / -1 / __id copies")
    ap.add_argument("--budget", type=float, default=256.0,
                    help="ceiling in MiB for --trace (default 256)")
    ap.add_argument("--builds", action="store_true",
                    help="the series, from the manifest; reads no build file")
    ap.add_argument("--first", metavar="TOKEN",
                    help="bisect for the first build carrying a fixed string")
    ap.add_argument("--trace", metavar="TOKEN",
                    help="the whole series; prints only the transitions")
    ap.add_argument("--verify", nargs="?", type=int, const=-1,
                    metavar="N", help="on-disk md5 against the manifest's; "
                                      "a build number, or all of them")
    ap.add_argument("--json", action="store_true",
                    help="--builds: the series as JSON")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest(args.manifest, args.tree)

    series = read_series(args.manifest)
    if not series:
        print("no build files in %s" % args.manifest, file=sys.stderr)
        return 2

    if args.json and args.builds:
        json.dump([b.asdict() for b in
                   select(series, args.stream, not args.variants)],
                  sys.stdout, indent=2)
        print()
        return 0
    if args.builds:
        return mode_builds(series, args.stream, args.variants)
    if args.verify is not None:
        return mode_verify(series, None if args.verify == -1 else args.verify,
                           args.tree)

    cache = Cache(None if args.no_cache else args.cache)
    cap = args.budget * 1048576.0
    try:
        if args.first:
            return mode_first(series, args.first, args.stream, args.tree,
                              cache, cap)
        if args.trace:
            return mode_trace(series, args.trace, args.stream, args.tree,
                              cache, cap)
    finally:
        cache.flush()

    ap.error("name a mode: --builds, --first, --trace, --verify or --selftest")


if __name__ == "__main__":
    sys.exit(main())
