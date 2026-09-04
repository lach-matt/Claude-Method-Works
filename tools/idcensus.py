#!/usr/bin/env python3
"""idcensus.py -- which governance identifiers does the chat export name that the
repository does not hold?

`docs/PROSE-ONLY.md` records a stage-A census of exactly this: 164 `W-` entries
named in prose against 195 present, 734 registers against 933, 40 prose-only
faults, 178 prose-only registers. **That census is not reproducible.** The pattern
set that produced it was never banked, and re-deriving it by eye gives materially
different counts even for the kinds that cannot have changed -- 54 rulings named
where the table says 47. So the table's figures can be read as a record of what a
pass once found, and not re-run.

This is that census, banked, with every pattern stated in one place. Its numbers
are NOT the table's and are not offered as a correction to it: they are a
different measurement under a declared method, and the two should not be
subtracted from one another. What this buys is that the NEXT change to the tree
can be measured against a fixed instrument instead of against prose.

WHAT IT REFUSES
---------------
It will not report an identifier as prose-only on the strength of the repository's
own audit files. `PROSE-ONLY.tsv`, `RETRACTION-AUDIT.tsv` and their documents QUOTE
the export; counting them as repository presence makes an identifier read as held
because a session wrote it down. They are excluded, and the exclusion list is in
EXCLUDE below where it can be argued with.

It also refuses to call a prose-only identifier a loss. A name in prose is not
proof a file or an entry ever existed -- the same discipline `coverage.py` states
for ABSENT.

stdlib only.  python3 tools/idcensus.py [--selftest] [--kind KIND] [--list]
"""
import argparse
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHATS = ROOT / "drive" / "chats"
EXT = {".md", ".py", ".tsv", ".csv", ".txt", ".json"}
SKIP_DIRS = {".git", "graphify-out", "__pycache__"}

# The repository's own audit artefacts quote the chat export verbatim. Counting
# them as presence is self-defeating: an identifier would read as held because
# this repository recorded that it was not.
EXCLUDE = {
    "PROSE-ONLY.tsv", "RETRACTION-AUDIT.tsv", "HANDOFF-GAP.tsv", "REGISTER-GAPS.tsv",
    "docs/PROSE-ONLY.md", "docs/RETRACTION-AUDIT.md", "docs/HANDOFF-GAP.md",
    "docs/REGISTER-GAPS.md", "docs/GRAPH-FINDINGS.md", "docs/IDCENSUS.md",
}

# TWO SPELLINGS BREAK A NAIVE PATTERN, and both were found producing false
# prose-only entries in the first run of this file:
#
#   ZERO PADDING     "W-001...W-027" and "W-1" are the same entry written two
#                    ways. Counting them separately reported 15 prose-only W
#                    entries where the true figure is far smaller.
#   LIST CONTINUATION  "MC-07/08/09" and "registers 219, 220, 221" carry the
#                    prefix once. A pattern requiring it on every element sees
#                    the first and loses the rest -- which both understates what
#                    the prose names and, through the repository side, overstates
#                    what is prose-only.
#
# Both are handled below rather than left as caveats.
LIST_TAIL = re.compile(r"\s*(?:[,/;]|\band\b|[\u2013\u2014-])\s*(\d{1,4})\b")


def _norm(v):
    """W-001 and W-1 are one entry. Strip leading zeros, keep a bare 0."""
    if "." in v:
        return v
    return v.lstrip("0") or "0"


# One pattern per kind, stated here so the census can be argued with rather than
# guessed at. The 165 floor on registers is register_cites.py's, quoted by
# tools/pointers.py: below it a three-digit token is not a register citation.
PATTERNS = {
    "W-entry":  (re.compile(r"\bW-(\d{1,3})\b"), None),
    "Ruling":   (re.compile(r"(?i)\bruling\s+(\d{1,3})\b"), None),
    "Docket":   (re.compile(r"(?i)\bdocket\s+(\d{1,3})\b"), None),
    "Fault":    (re.compile(r"\bF(\d{1,2}\.\d{1,2})\b"), None),
    "Register": (re.compile(r"(?i)\bregisters?\s+(\d{3,4})\b"),
                 lambda v: v.isdigit() and int(v) >= 165),
    "MC-entry": (re.compile(r"\bMC-(\d{1,3})\b"), None),
    "DEF":      (re.compile(r"\bDEF-(\d{1,3})\b"), None),
    "HANDOFF":  (re.compile(r"\bHANDOFF-(\d{1,3})\b"), None),
}


def _scan(text, found):
    for kind, (rx, keep) in PATTERNS.items():
        for m in rx.finditer(text):
            vals = [m.group(1)]
            # follow a run of "MC-07/08/09" or "registers 219, 220, 221"
            pos = m.end()
            while True:
                t2 = LIST_TAIL.match(text, pos)
                if not t2 or len(vals) > 60:
                    break
                vals.append(t2.group(1))
                pos = t2.end()
            for v in vals:
                if keep is None or keep(v):
                    found[kind].add(_norm(v))


def prose_ids():
    found = collections.defaultdict(set)
    for s in sorted(CHATS.rglob("*.json")):
        if s.name == "SUMMARY.json":
            continue
        try:
            _scan(s.read_text(encoding="utf-8", errors="replace"), found)
        except OSError:
            continue
    return found


def repo_ids():
    found = collections.defaultdict(set)
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in EXT:
            continue
        if any(s in p.parts for s in SKIP_DIRS):
            continue
        if str(p).startswith(str(CHATS)):
            continue
        if str(p.relative_to(ROOT)) in EXCLUDE:
            continue
        try:
            if p.stat().st_size > 40 * 1024 * 1024:
                continue
            _scan(p.read_text(encoding="utf-8", errors="replace"), found)
        except OSError:
            continue
    return found


def _register_max():
    """The Register's own highest seated entry, grouped headings honoured."""
    t = (ROOT / "method/members/The_Method_1_6___The_Register-2.md").read_text(
        encoding="utf-8", errors="replace")
    s = set()
    for m in re.finditer(r"\n### ([\d,\s]+)\n", t):
        for part in re.split(r"\s*,\s*", m.group(1).strip()):
            if part.strip().isdigit():
                s.add(int(part.strip()))
    return max(s)


def report(kind=None, listing=False):
    prose, repo = prose_ids(), repo_ids()
    rmax = _register_max()
    print("  IDENTIFIER CENSUS -- named in the chat export, against held in the repository\n")
    print(f'      {"kind":<12}{"in prose":>10}{"in repo":>9}{"prose-only":>12}')
    total = 0
    for k in PATTERNS:
        if kind and k.lower() != kind.lower():
            continue
        only = prose[k] - repo[k]
        # A "register" numbered above the Register's own maximum is almost always
        # a LINE reference to a file whose name contains "register" -- established
        # in docs/REGISTER-GAPS.md, where 4481 is WORKING-REGISTER's line count.
        # 1793 and 1794 are the known real exceptions, drafted past the end.
        above = {v for v in only if k == "Register" and v.isdigit() and int(v) > rmax}
        only = only - above
        total += len(only)
        extra = f"   (+{len(above)} above the Register's max {rmax}, read as line refs)" if above else ""
        print(f"      {k:<12}{len(prose[k]):>10}{len(repo[k]):>9}{len(only):>12}{extra}")
        if listing and above:
            print("            above-max, NOT counted: " + ", ".join(sorted(above, key=int)))
        if listing and only:
            def srt(v):
                return (0, float(v)) if v.replace(".", "").isdigit() else (1, 0)
            print("            " + ", ".join(sorted(only, key=srt)))
    print(f'\n      {"TOTAL":<12}{"":>10}{"":>9}{total:>12}')
    print()
    print("      PROSE-ONLY is not a finding of loss. A name in prose is not proof a")
    print("      file or an entry ever existed. docs/PROSE-ONLY.md's stage-A table is a")
    print("      DIFFERENT measurement whose patterns were never banked; do not subtract")
    print("      one from the other.")
    return 0


def selftest():
    """Structural fixtures. A total is the thing that moves, so none is pinned."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-56s = %-7s expected %-7s %s" % (label, got, want, "ok" if good else "FAIL"))

    check("W-001 and W-1 normalise to one entry", _norm("001"), "1")
    check("a bare 0 survives normalisation", _norm("0"), "0")
    check("a fault id is left alone by normalisation", _norm("18.3"), "18.3")
    f0 = collections.defaultdict(set)
    _scan("MC-07/08/09 closed", f0)
    check("a slash list carries the prefix forward", sorted(f0["MC-entry"]), ["7", "8", "9"])
    f1 = collections.defaultdict(set)
    _scan("registers 219, 220 and 221", f1)
    check("a comma-and list carries the prefix forward",
          sorted(f1["Register"], key=int), ["219", "220", "221"])
    check("every kind carries a compiled pattern",
          sum(1 for rx, _ in PATTERNS.values() if hasattr(rx, "finditer")), len(PATTERNS))
    # the register floor is register_cites.py's and must actually bite
    rx, keep = PATTERNS["Register"]
    check("register floor rejects 164", keep("164"), False)
    check("register floor accepts 165", keep("165"), True)
    f = collections.defaultdict(set)
    _scan("see register 1493 and Register 164, W-101, Ruling 27, F18.3, MC-39, "
          "DEF-118, HANDOFF-71, docket 9", f)
    check("register 1493 read, 164 refused", sorted(f["Register"]), ["1493"])
    check("W-101 read", sorted(f["W-entry"]), ["101"])
    check("Ruling 27 read", sorted(f["Ruling"]), ["27"])
    check("F18.3 read", sorted(f["Fault"]), ["18.3"])
    check("MC-39 read", sorted(f["MC-entry"]), ["39"])
    check("DEF-118 read", sorted(f["DEF"]), ["118"])
    check("HANDOFF-71 read", sorted(f["HANDOFF"]), ["71"])
    check("docket 9 read", sorted(f["Docket"]), ["9"])
    # the audit artefacts must be excluded, or the census answers itself
    check("PROSE-ONLY.tsv is excluded from repository presence",
          "PROSE-ONLY.tsv" in EXCLUDE, True)
    check("RETRACTION-AUDIT.tsv is excluded", "RETRACTION-AUDIT.tsv" in EXCLUDE, True)
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true", help="assert the patterns and the exclusions")
    ap.add_argument("--kind", help="census one kind only")
    ap.add_argument("--list", action="store_true", dest="listing",
                    help="list the prose-only identifiers of each kind")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return report(kind=a.kind, listing=a.listing)


if __name__ == "__main__":
    sys.exit(main())
