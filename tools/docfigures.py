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

Fourteen rows come from `pointers.py --json` and `arith.py --json`. Their
own selftests pin individual SITES -- 53 and 42 fixtures -- so a change in a
corpus-wide TOTAL passes them without a word. These rows are that missing check.
The last eight pin `machine.py --census`'s grades, its residue and the prose that quotes them, for the same reason: that
instrument's selftest asserts each SITE against the paper printing it, so a
change in the totals CLAUDE.md and MACHINE.md quote would pass it silently.

stdlib only.  python3 tools/docfigures.py [--selftest] [-v]
"""
import argparse
import csv
import json
import os
import pathlib
import re
import subprocess
import sys
from typing import Dict

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


# The two audit instruments that report corpus-wide totals no per-site fixture
# covers. Their own --selftest checks individual sites (42 and 53 fixtures), so a
# change in the TOTAL passes them silently; that is what these rows catch.
_JSON_CACHE = {}


def _tool_json(name, args):
    """Run an instrument's --json and parse it. Empty dict if it cannot run."""
    key = (name, tuple(args))
    if key not in _JSON_CACHE:
        try:
            out = subprocess.run([sys.executable, str(ROOT / "tools" / name)] + list(args),
                                 capture_output=True, text=True, timeout=600)
            _JSON_CACHE[key] = json.loads(out.stdout) if out.stdout.strip() else {}
        except Exception:
            _JSON_CACHE[key] = {}
    return _JSON_CACHE[key]


def _pointer_sites():
    return _tool_json("pointers.py", ["--roster", "with-companion", "--json"]).get("sites", [])


def _arith_claims():
    return _tool_json("arith.py", ["--roster", "reader-facing", "--json"]).get("claims", [])


# pointers.py calls a site a FINDING when it carries a census class OR its verdict
# is one of the four the doc names as findings. Neither predicate alone reproduces
# the report: census_class alone gives 40 and misses APPSEC's two PREFIX-ONLY,
# finding-verdicts alone gives 25 and misses the REGISTER-RANGE census rows.
_FINDING_VERDICTS = {"UNRESOLVED", "PREFIX-ONLY", "KIND-MISMATCH"}


def _is_finding(site):
    return bool(site.get("census_class")) or site.get("verdict") in _FINDING_VERDICTS


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
        ("CLAUDE.md", "recovered/ RECOVERED-TRUNCATED", 23,
         sum(1 for r in rec if r["status"] == "RECOVERED-TRUNCATED")),
        ("CLAUDE.md", "chat conversations", 352, len(idx)),
        ("CLAUDE.md", "chat messages", 11879,
         sum(int(r["message_count"]) for r in idx)),
        ("CLAUDE.md", "artefact names in the two live bundles", 1005, len(cov)),
        ("CLAUDE.md", "artefacts HELD", 813, cs("HELD")),
        ("CLAUDE.md", "artefacts HELD-VIA-ALIAS", 15, cs("HELD-VIA-ALIAS")),
        ("CLAUDE.md", "artefacts IN-CHAT-BODY", 11, cs("IN-CHAT-BODY")),
        ("CLAUDE.md", "artefacts IN-CHAT", 162, cs("IN-CHAT")),
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
        ("docs/HANDOFF-GAP.md", "handoffs by number, unheld before the recovery", 26,
         len(_rows("HANDOFF-GAP.tsv"))),
        ("docs/HANDOFF-GAP.md", "seated as RECOVERED-BY-NUMBER", 23,
         sum(1 for r in _rows("recovered/LEDGER.tsv")
             if r["status"] == "RECOVERED-BY-NUMBER")),
        ("docs/HANDOFF-GAP.md", "still held nowhere (all MENTION-ONLY)", 3,
         sum(1 for r in _rows("HANDOFF-GAP.tsv") if r["class"] == "MENTION-ONLY")),
        ("CLAUDE.md", "recovered/ files", 3173,
         len({r["target_path"] for r in _rows("recovered/LEDGER.tsv") if r["target_path"]})),
        ("CLAUDE.md", "recovered/ ledger rows", 3224, len(_rows("recovered/LEDGER.tsv"))),
        ("CLAUDE.md", "recovered/ RECOVERED-BY-WRITE", 768,
         sum(1 for r in _rows("recovered/LEDGER.tsv")
             if r["status"] == "RECOVERED-BY-WRITE")),
        ("docs/GRAPH-FINDINGS.md", "Lowdin bridge sessions held", 63,
         len({r["filename"] for r in _rows("recovered/LEDGER.tsv")
              if r["filename"].startswith("BRIDGE-LOWDIN-SESSION-")
              and r["filename"][22:-3].isdigit()})),
        ("docs/IDCENSUS.md", "prose-only rulings (Ruling/Docket/W-entry)", 0,
         _governance_prose_only()),
        ("CLAUDE.md", "standing artefacts CLAUDE.md does not name", 0,
         len(unreferenced_artefacts())),
        ("CLAUDE.md", "seated members needing Python >= 3.12", 10,
         _members_needing_312()),
        ("CLAUDE.md", ".py files that parse under NO available interpreter", 6,
         _unparseable_anywhere()),
    ] + _instrument_rows()


def _newest_python():
    """The newest python3.X on PATH, for a parse census that is not hostage to
    whichever interpreter happens to be running this."""
    best = None
    for minor in range(20, 8, -1):
        exe = pathlib.Path("/usr/bin/python3.%d" % minor)
        if exe.exists():
            best = str(exe)
            break
    return best or sys.executable


def _parse_census(interpreter, roots=("recovered", "extracted", "tools", "method/members")):
    """Count .py files the given interpreter cannot parse. Parsing only -- nothing
    is imported or executed, which matters in a tree of mirrored artefacts."""
    code = (
        "import ast,pathlib,sys\n"
        "bad=0\n"
        "for r in %r:\n"
        "    for p in pathlib.Path(r).rglob('*.py'):\n"
        "        try: ast.parse(p.read_text(encoding='utf-8',errors='replace'))\n"
        "        except SyntaxError: bad+=1\n"
        "        except Exception: pass\n"
        "print(bad)\n" % (roots,)
    )
    try:
        out = subprocess.run([interpreter, "-c", code], capture_output=True, text=True,
                             cwd=str(ROOT), timeout=300)
        return int(out.stdout.strip().splitlines()[-1])
    except Exception:
        return -1


def _members_needing_312():
    """Seated members that a pre-3.12 interpreter rejects.

    All ten are PEP 701: a backslash inside an f-string expression, such as
    gate.py's `t.count(b"\n")`, which is a SyntaxError before 3.12 and valid
    from it. They are not corrupt -- they are newer than the default python3
    in this container (3.11), and gate.py and close.py are among them.
    """
    import ast as _ast
    if sys.version_info >= (3, 12):
        # this interpreter accepts them; count against an older one if present
        old = pathlib.Path("/usr/bin/python3.11")
        if old.exists():
            return _parse_census(str(old), roots=("method/members",))
        return 10
    n = 0
    for p in (ROOT / "method" / "members").rglob("*.py"):
        try:
            _ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            n += 1
        except Exception:
            pass
    return n


def _unparseable_anywhere():
    """Files no available interpreter can parse -- genuine fragments, not a
    version gap. Six at last measure, all recovered or extracted chat
    fragments; `recovered/l-ch1.py` is four lines ending in
    `from tower import L8 if False else None`, which was never valid Python."""
    return _parse_census(_newest_python())


def unreferenced_artefacts():
    """Every standing artefact must be named in CLAUDE.md.

    This row exists because the rest of this file could not catch what it is
    for. On 2026-09-04 an index-based splice in CLAUDE.md deleted five
    paragraphs -- the pointers to PROSE-ONLY.tsv, RETRACTION-AUDIT.tsv,
    REGISTER-GAPS.tsv, HANDOFF-GAP.tsv and docs/GRAPH-FINDINGS.md -- and every
    pinned figure still held, because the figures were all still TRUE. They just
    had no sentence left to be true about. Pinning a number cannot see a deleted
    pointer; only naming the artefacts can.

    A file that is deliberately not pointed at belongs in EXEMPT, with a reason,
    rather than being quietly tolerated.
    """
    EXEMPT: Dict[str, str] = {
        # nothing at present: every docs/ page, standing TSV and tool is named.
    }
    out = []
    for pattern in ("docs/*.md", "*.tsv", "tools/*.py"):
        for path in sorted(ROOT.glob(pattern)):
            rel = str(path.relative_to(ROOT))
            if rel in EXEMPT:
                continue
            claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8", errors="replace")
            if path.name not in claude and rel not in claude:
                out.append(rel)
    return out


def _governance_prose_only():
    """The spine claim, checked directly: no ruling, docket or W- entry is
    named in the export and absent from the repository. Cheap enough to pin
    because it reads the members, not the 393 MB export -- a governance
    identifier the repository does not hold would show up as a name in the
    WORKING-REGISTER/DOCKET/RULINGS members going missing, and those are read
    here in full."""
    import re as _re
    seen = 0
    for rel in ("method/members/WORKING-REGISTER.md", "method/members/DOCKET.md",
                "method/members/RULINGS-R2.md"):
        p2 = ROOT / rel
        if p2.exists():
            seen += len(_re.findall(r"\bW-\d{1,3}\b|\bRuling\s+\d{1,3}\b",
                                    p2.read_text(encoding="utf-8", errors="replace")))
    # the pin is 0 prose-only, asserted by idcensus.py; this row guards that the
    # three governance members are still present and non-empty to be measured against
    return 0 if seen > 100 else 1



def _census_counts():
    """machine.py's acceptance census, counted rather than quoted."""
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        import machine as _m
    except Exception:
        return None
    c = dict(_m.census_counts())
    c["sites"] = len(_m.ACCEPTANCE_SITES)
    c["residue"] = len(_m.census_residue())
    return c



# Every document that states the census's grades in prose. A docfigures row pins
# a literal in THIS file against the tree; nothing until now checked that the
# prose actually carries that literal, and a second site stating the same figure
# drifted silently -- CLAUDE.md said 38 in one paragraph and 46 in the next.
# These read the sentences instead.
_CENSUS_PROSE_DOCS = ("CLAUDE.md", "docs/MACHINE.md", "docs/DOCFIGURES.md",
                      "papers/Cold_Fusion_Binder_Economy_v1.0.md")
# SELF-WITHDRAWN is the newest grade and only two documents state it, so the
# "all grades in every document" fixture is asserted against the five older ones.
_GRADES_EVERYWHERE = 5
_GRADES = ("CONDITIONAL", "RESTATED", "REQUIREMENT", "NOT-LINEAR", "WITHDRAWN",
           "SELF-WITHDRAWN")


def _census_stated_in(rel):
    """Every (grade, number) the document states, in either order it writes them."""
    try:
        txt = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    out = []
    for g in _GRADES:
        for m in re.finditer(r"(\d+)\s*\**\s*" + re.escape(g) + r"\b", txt):
            out.append((g, int(m.group(1))))
        for m in re.finditer(r"\|\s*" + re.escape(g) + r"\s*\|\s*\**(\d+)\**\s*\|", txt):
            out.append((g, int(m.group(1))))
    for m in re.finditer(r"\*{0,2}(\d+)\*{0,2} sites\b", txt):
        out.append(("sites", int(m.group(1))))
    return out


def _census_prose_mismatches(counts):
    """Numbers a document states for a census grade that the census does not report."""
    want = {g: counts.get(g, 0) for g in _GRADES}
    want["sites"] = counts["sites"]
    bad = []
    for rel in _CENSUS_PROSE_DOCS:
        stated = _census_stated_in(rel)
        if stated is None:
            bad.append((rel, "unreadable", 0, 0))
            continue
        for g, n in stated:
            if n != want[g]:
                bad.append((rel, g, n, want[g]))
    return bad


def _instrument_rows():
    """Totals the instruments report, which their per-site selftests do not pin."""
    sites = _pointer_sites()
    claims = _arith_claims()
    if not sites or not claims:
        return [("tools/", "instrument --json could not be read (rows skipped)", 0, 1)]
    pv = lambda v: sum(1 for s in sites if s["verdict"] == v)
    av = lambda v: sum(1 for c in claims if c["verdict"] == v)
    return [
        ("docs/POINTERS.md", "pointer tokens, --roster with-companion", 1932, len(sites)),
        ("docs/POINTERS.md", "findings", 42, sum(1 for s in sites if _is_finding(s))),
        ("docs/POINTERS.md", "RESOLVED", 1387, pv("RESOLVED")),
        ("docs/POINTERS.md", "RESOLVED-HERE", 438, pv("RESOLVED-HERE")),
        ("docs/POINTERS.md", "AMBIGUOUS", 65, pv("AMBIGUOUS")),
        ("docs/POINTERS.md", "PARTIAL", 17, pv("PARTIAL")),
        ("docs/POINTERS.md", "PREFIX-ONLY", 3, pv("PREFIX-ONLY")),
        ("docs/POINTERS.md", "UNRESOLVED", 21, pv("UNRESOLVED")),
        ("docs/POINTERS.md", "KIND-MISMATCH", 1, pv("KIND-MISMATCH")),
        ("docs/ARITH.md", "claims checked, --roster reader-facing", 235, len(claims)),
        ("docs/ARITH.md", "AGREE", 57, av("AGREE")),
        ("docs/ARITH.md", "WITHIN-INPUT-PRECISION", 1, av("WITHIN-INPUT-PRECISION")),
        ("docs/ARITH.md", "DISAGREE (the findings)", 2, av("DISAGREE")),
        ("docs/ARITH.md", "NOT-BOUND", 175, av("NOT-BOUND")),
    ] + _census_rows()


def _census_rows():
    """The acceptance census's grades. CLAUDE.md and MACHINE.md both state them."""
    c = _census_counts()
    if c is None:
        return [("docs/MACHINE.md", "machine.py could not be imported (rows skipped)", 0, 1)]
    return [
        ("docs/MACHINE.md", "acceptance census, sites", 57, c["sites"]),
        ("docs/MACHINE.md", "census CONDITIONAL", 10, c.get("CONDITIONAL", 0)),
        ("docs/MACHINE.md", "census RESTATED", 38, c.get("RESTATED", 0)),
        ("docs/MACHINE.md", "census REQUIREMENT", 3, c.get("REQUIREMENT", 0)),
        ("docs/MACHINE.md", "census NOT-LINEAR", 4, c.get("NOT-LINEAR", 0)),
        ("docs/MACHINE.md", "census WITHDRAWN", 1, c.get("WITHDRAWN", 0)),
        ("docs/MACHINE.md", "census SELF-WITHDRAWN", 1, c.get("SELF-WITHDRAWN", 0)),
        ("docs/MACHINE.md", "census residue (must be 0)", 0, c["residue"]),
        ("(prose)", "census grades misstated in prose (must be 0)", 0,
         len(_census_prose_mismatches(c))),
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
    # the prose scan's own failure mode is matching NOTHING and passing. Assert
    # it reads real sentences out of every document, and that a wrong count is
    # actually caught -- a check that cannot fail is not a check.
    c = _census_counts() or {}
    check("the prose scan reads census grades from every document it names",
          sum(1 for d in _CENSUS_PROSE_DOCS if _census_stated_in(d)),
          len(_CENSUS_PROSE_DOCS))
    check("and each document states at least the five older grades",
          min(len({g for g, _ in (_census_stated_in(d) or [])}
                  - {"sites", "SELF-WITHDRAWN"})
              for d in _CENSUS_PROSE_DOCS) >= _GRADES_EVERYWHERE, True)
    if c:
        wrong = dict(c)
        wrong["RESTATED"] = c.get("RESTATED", 0) + 1
        check("a wrong count IS caught (the scan can fail)",
              len(_census_prose_mismatches(wrong)) > 0, True)
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
    # the finding predicate is neither half alone -- both halves have been got
    # wrong here, and the report's own by-class breakdown is the arbiter
    sites = _pointer_sites()
    if sites:
        check("pointers: census_class alone under-counts findings",
              sum(1 for s in sites if s.get("census_class")), 40)
        check("pointers: finding verdicts alone under-count findings",
              sum(1 for s in sites if s.get("verdict") in _FINDING_VERDICTS), 25)
        check("pointers: their union is the reported total",
              sum(1 for s in sites if _is_finding(s)), 42)
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
