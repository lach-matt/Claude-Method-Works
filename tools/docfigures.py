#!/usr/bin/env python3
"""docfigures.py -- do the repository's own documents still state true numbers?

`arith.py` checks the arithmetic the volumes state about themselves. This does the
same for the documents that describe the REPOSITORY -- CLAUDE.md and docs/ -- and
it exists because they went stale without anyone noticing:

    CLAUDE.md said 559 artefacts held against 431 ABSENT. The instrument measured
    702 and 4. `extracted/` and `recovered/` had landed 143 of them and nothing
    updated the prose, so the entry-point document -- the one every chat reads
    first -- overstated the gap by two orders of magnitude.

Every row below pins a CLAIMED value beside a measurement. A row is STALE when
they differ. That is a finding about the documentation, never about the corpus:
the tree is right and the sentence is old.

WHAT IT REFUSES
---------------
It does not edit a document, and it does not decide which of the two is correct.
It reports the drift and names the file to read. Where a claim is a range or a
prose phrase rather than a number, it is not pinned here at all -- a check that
cannot be made exactly is not made.

It also refuses to measure anything requiring the 393 MB chat export, so it stays
fast enough to run at the top of a session. `coverage.py --chats` owns that.

stdlib only.  python3 tools/docfigures.py [--selftest] [-v]
"""
import argparse
import csv
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _rows(rel):
    with open(ROOT / rel, encoding="utf-8", errors="replace") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _walk(rel, skip=()):
    out = []
    for dp, _, fs in os.walk(ROOT / rel):
        if any(s in dp for s in skip):
            continue
        out += [os.path.join(dp, f) for f in fs]
    return out


def _entries(rel):
    """Every Register entry number a member seats, GROUPED HEADINGS HONOURED.

    A bare `### N` read undercounts The Register by 32 and invents 32 gaps that
    are not gaps -- DEFERRED.md docket 9(c)/30 records the same trap.
    """
    t = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    s = set()
    for m in re.finditer(r"\n### ([\d,\s]+)\n", t):
        for part in re.split(r"\s*,\s*", m.group(1).strip()):
            if part.strip().isdigit():
                s.add(int(part.strip()))
    return s


def _manifest():
    return [r["repo_path"] for r in _rows("drive/MANIFEST.tsv")]


def _build_nums(suffix):
    return sorted(int(re.search(r"BUILD(\d+)", p).group(1))
                  for p in _manifest() if p.endswith(suffix))


# (document, label, claimed, measurement)
def checks():
    man = _manifest()
    cov = _rows("COVERAGE.tsv")
    led = _rows("extracted/LEDGER.tsv")
    rec = _rows("recovered/LEDGER.tsv")
    idx = _rows("drive/chats/INDEX.tsv")
    ext = {r["target_path"] for r in led if r["disposition"] == "EXTRACTED"}
    R = _entries("method/members/The_Method_1_6___The_Register-2.md")
    W = _entries("method/members/WORKING-REGISTER.md")
    roots = {p.split("/")[0] for p in man}
    disk = set()
    for root in roots:
        base = ROOT / "drive" / root
        for dp, _, fs in os.walk(base):
            for f in fs:
                disk.add(os.path.relpath(os.path.join(dp, f), ROOT / "drive"))
    cs = lambda s: sum(1 for r in cov if r["status"] == s)
    gaps = [n for n in range(min(R), max(R) + 1) if n not in R]

    return [
        ("CLAUDE.md", "members extracted from the bundles", 343,
         len(_rows("method/MEMBER-INDEX.tsv"))),
        ("CLAUDE.md", "drive/ MANIFEST rows", 819, len(man)),
        ("CLAUDE.md", "drive/ manifest-tree bijection (orphans, both ways)", 0,
         len(disk ^ set(man))),
        ("CLAUDE.md", "drive/ rows with status ok", 819,
         sum(1 for r in _rows("drive/MANIFEST.tsv") if r["status"] == "ok")),
        ("CLAUDE.md", "drive/chats/ files (no manifest row)", 354,
         len(_walk("drive/chats"))),
        ("CLAUDE.md", "drive/PENDING.tsv rows", 4, len(_rows("drive/PENDING.tsv"))),
        ("CLAUDE.md", "extracted/ source occurrences", 2504, len(led)),
        ("CLAUDE.md", "extracted/ bodies written", 779, len(ext)),
        ("CLAUDE.md", "extracted/ bodies, MB (1dp)", 57.4,
         round(sum(os.path.getsize(ROOT / p) for p in ext) / 1e6, 1)),
        ("CLAUDE.md", "recovered/ files", 2382,
         len({r["target_path"] for r in rec if r["target_path"]})),
        ("CLAUDE.md", "recovered/ ledger rows", 2433, len(rec)),
        ("CLAUDE.md", "recovered/ RECOVERED-TRUNCATED", 23,
         sum(1 for r in rec if r["status"] == "RECOVERED-TRUNCATED")),
        ("CLAUDE.md", "chat conversations", 352, len(idx)),
        ("CLAUDE.md", "chat messages", 11879,
         sum(int(r["message_count"]) for r in idx)),
        ("CLAUDE.md", "artefact names in the two live bundles", 1005, len(cov)),
        ("CLAUDE.md", "artefacts HELD", 702, cs("HELD")),
        ("CLAUDE.md", "artefacts HELD-VIA-ALIAS", 15, cs("HELD-VIA-ALIAS")),
        ("CLAUDE.md", "artefacts IN-CHAT-BODY", 11, cs("IN-CHAT-BODY")),
        ("CLAUDE.md", "artefacts IN-CHAT", 273, cs("IN-CHAT")),
        ("CLAUDE.md", "artefacts ABSENT", 4, cs("ABSENT")),
        ("CLAUDE.md", "BUILD .md files in the manifest", 140,
         sum(1 for p in man if "The_Method_1_6_BUILD" in p and p.endswith(".md"))),
        ("CLAUDE.md", "BUILD compendia stream, plain name", 123,
         len(_build_nums("_compendia_papers_audits.md"))),
        ("CLAUDE.md", "BUILD main stream, plain name", 12,
         len(_build_nums("_main_and_register.md"))),
        ("CLAUDE.md", "BUILD compendia lowest / highest", (9, 179),
         (min(_build_nums("_compendia_papers_audits.md")),
          max(_build_nums("_compendia_papers_audits.md")))),
        ("CLAUDE.md", "BUILD main lowest / highest", (9, 90),
         (min(_build_nums("_main_and_register.md")),
          max(_build_nums("_main_and_register.md")))),
        ("CLAUDE.md", "figure bundles held", 3,
         sum(1 for p in man if re.search(r"figures_BUILD\d+\.zip$", p))),
        ("CLAUDE.md", "__<driveFileId> duplicates", 99,
         sum(1 for p in man if "__" in os.path.basename(p))),
        ("docs/PROSE-ONLY.md", "PROSE-ONLY rows", 1168,
         len(_rows("PROSE-ONLY.tsv"))),
        ("docs/PROSE-ONLY.md", "PROSE-ONLY conversations", 194,
         len({r["conversation"] for r in _rows("PROSE-ONLY.tsv")})),
        ("docs/RETRACTION-AUDIT.md", "RETRACTION-AUDIT rows", 391,
         len(_rows("RETRACTION-AUDIT.tsv"))),
        ("docs/RETRACTION-AUDIT.md", "LIVE-SUPERSEDED", 25,
         sum(1 for r in _rows("RETRACTION-AUDIT.tsv")
             if r["verdict"] == "LIVE-SUPERSEDED")),
        ("docs/REGISTER-GAPS.md", "The Register entries", 1660, len(R)),
        ("docs/REGISTER-GAPS.md", "Working Register entries", 119, len(W)),
        ("docs/REGISTER-GAPS.md", "registers seated in both (must be 0)", 0, len(R & W)),
        ("docs/REGISTER-GAPS.md", "numbering gaps", 132, len(gaps)),
        ("docs/REGISTER-GAPS.md", "seated in neither register", 13,
         len([n for n in gaps if n not in W])),
    ]


def report(verbose=False):
    rows = checks()
    stale = [r for r in rows if r[2] != r[3]]
    doc = None
    for d, label, claimed, got in rows:
        if d != doc:
            print(f"\n  {d}")
            doc = d
        mark = "ok  " if claimed == got else "STALE"
        if verbose or claimed != got:
            print(f"      {mark}  {label:<48} states {claimed!s:<12} measured {got}")
        else:
            print(f"      ok     {label:<48} {got}")
    print()
    if stale:
        print(f"  {len(stale)} of {len(rows)} figures have drifted. The tree is right and the")
        print("  sentence is old: read the named document and correct the prose.")
    else:
        print(f"  all {len(rows)} pinned figures still hold.")
    return 1 if stale else 0


def selftest():
    """Fixtures are structural, not the totals -- a total is what goes stale."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-56s = %-7s expected %-7s %s" % (label, got, want, "ok" if good else "FAIL"))

    rows = checks()
    check("every row carries a document, a claim and a measurement",
          sum(1 for r in rows if len(r) == 4 and r[0] and r[1]), len(rows))
    check("no label is pinned twice", len({(r[0], r[1]) for r in rows}), len(rows))
    # the grouped-heading trap: a bare read must give a DIFFERENT, smaller count
    t = (ROOT / "method/members/The_Method_1_6___The_Register-2.md").read_text(
        encoding="utf-8", errors="replace")
    bare = len({int(m) for m in re.findall(r"\n### (\d+)\n", t)})
    grouped = len(_entries("method/members/The_Method_1_6___The_Register-2.md"))
    check("grouped headings are honoured (bare read is smaller)", bare < grouped, True)
    check("the bare read's shortfall is the documented 32", grouped - bare, 32)
    # the two registers must never overlap -- that is Ruling 27, not a preference
    R = _entries("method/members/The_Method_1_6___The_Register-2.md")
    W = _entries("method/members/WORKING-REGISTER.md")
    check("Ruling 27: the two registers do not overlap", len(R & W), 0)
    check("COVERAGE.tsv is the --chats run (IN-CHAT rows present)",
          sum(1 for r in _rows("COVERAGE.tsv") if r["status"] == "IN-CHAT") > 0, True)
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true",
                    help="assert the checks' own structure and the corpus's invariants")
    ap.add_argument("-v", "--verbose", action="store_true", help="print every row")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    print("  DOCUMENT FIGURES -- what the repository says about itself, measured")
    return report(verbose=a.verbose)


if __name__ == "__main__":
    sys.exit(main())
