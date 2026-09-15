#!/usr/bin/env python3
r"""
store.py -- THE SIX FIRST-ORDER INDEXES THE ARTEFACT STORE CARRIES, built.

M: "We are trying to identify first-order indexes. Every time we think we have
identified all of them, more show up. The complete characterization index is not
settled until all first-order indexes are identified and built."

    python3 store.py             the reading
    python3 store.py --selftest  fixtures   (slow: the manifest channel is ~4m)

===============================================================================
0. WHY THESE SIX AND NOT A CHOICE
===============================================================================

`sources.py` named six first-order sources this tree had not built and ruled them
out of scope.  DOCKET 13 recorded that the ruling was taken under a scope that
has since moved.  These are those six, in the order that file names them, with
nothing added and nothing dropped:

    the BUILD series      the build snapshots, by number and stream
    the drive manifest    every mirrored file, by kind, size and depth
    the Register          every hole in the Register's numbering
    the recovered ledger  every conversation, by what was recovered from it
    the coverage census   every artefact name, by family and disposition
    the dockets           this tree's own open questions

    FIRST-ORDER MEANS THE MEMBERS ARE THINGS THE CORPUS BANKS.  Not measurements
    of the seated indexes -- that is second-order, and `sources.py` measured that
    its supply is unbounded.  Each of the six below reads a generated table and
    charts its rows.

    THE CORPUS IS READ AND NEVER WRITTEN.  Every source here is a `.tsv` the
    corpus's own instruments generate, opened read-only.  `CLAUDE.md` governs
    those trees; this file adds nothing to them and regenerates nothing.

===============================================================================
1. EVERY COORDINATE IS A COUNT OR A MEASURED QUANTITY, NEVER A RANKING
===============================================================================

A categorical column -- a mime type, a gap class, a docket state -- has no order,
and inventing one puts a RECONSTRUCTED status into every figure downstream.  So
no category is ranked here.  Instead a category contributes **how many rows
carry it**, which is a measurement of the table and is ordered because integers
are.

    mime type  ->  how many of the 820 files are that type
    gap class  ->  how many of the 132 gaps are that class
    stream     ->  how many builds are in that stream

    THAT IS THE ONE DESIGN DECISION IN THIS FILE and it is what keeps
    `STATUS_ORDER_IS_RECONSTRUCTED` -- which `axes.py` and `obstruction.py` both
    have to carry -- out of it entirely.  It costs something: two categories of
    equal size become the same coordinate value, so the chart cannot tell a PDF
    from a ZIP if the mirror holds equally many.  `collisions()` reports where
    that happens rather than leaving it to be discovered.

===============================================================================
2. WHAT IS MEASURED AND WHAT IS NOT
===============================================================================

Each index gets its cell on the same admissible chart every other index in this
tree uses, and each is put through DOCKET 3's criterion in `criterion()`.  What
this file does NOT do is claim any of them fills a cell the figure demands.
`occupy.py` measured that eight of the ten demanded cells need 18 to 30 members
and can only be first-order; these are the first six first-order indexes built
since.  Section 5 reports where each lands, and the two indexes built before the
demand table was read both missed.

===============================================================================
3. WHAT THIS FILE REFUSES
===============================================================================

To read a table the corpus does not generate.  Six files, all listed in
`SOURCES`, all produced by a named instrument.  Nothing is scraped and no tree is
walked; `CLAUDE.md` is explicit that the store is read from its manifests.

To treat six as complete.  M's point is that the supply keeps growing, and this
file cannot refute that -- it builds the six that were NAMED, and a seventh
source found tomorrow is a seventh index.  `UNNAMED_SOURCES_MAY_EXIST = True`.

To smooth a table.  Where a column is empty or unparseable the row is counted as
`skipped` and reported, never guessed at.
"""

import collections
import csv
import os
import re
import sys

import hlaw
import mi

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UNNAMED_SOURCES_MAY_EXIST = True

SOURCES = {
    "build series": "drive/MANIFEST.tsv",
    "drive manifest": "drive/MANIFEST.tsv",
    "register gaps": "REGISTER-GAPS.tsv",
    "recovered ledger": "recovered/LEDGER.tsv",
    "coverage census": "COVERAGE.tsv",
    "dockets": "research/warp-drive/DOCKET.md",
}
_SKIPPED = {}


def _rows(rel):
    with open(os.path.join(ROOT, rel), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def _tally(vals):
    """{value: how many rows carry it} -- a category's contribution."""
    return collections.Counter(vals)


# ---------------------------------------------------------------------------
# 1. the drive manifest -- every mirrored file
# ---------------------------------------------------------------------------

def manifest_index():
    """(how common its kind is, its size, its path depth) over 820 files."""
    rs = _rows(SOURCES["drive manifest"])
    kind = _tally(r["mime_type"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        s = _int(r["drive_size_bytes"])
        if s is None:
            skip += 1
            continue
        out.add((kind[r["mime_type"]], s, r["repo_path"].count("/")))
    _SKIPPED["drive manifest"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 2. the BUILD series
# ---------------------------------------------------------------------------

def _stream(title):
    if "main_and_register" in title:
        return "main"
    if "compendia" in title:
        return "compendia"
    return "figures"


def build_index():
    """(build number, how many builds share its stream, its size)."""
    rs = [r for r in _rows(SOURCES["build series"])
          if re.search(r"BUILD\d+", r["drive_title"] or "")]
    st = _tally(_stream(r["drive_title"]) for r in rs)
    out, skip = set(), 0
    for r in rs:
        n = _int(re.search(r"BUILD(\d+)", r["drive_title"]).group(1))
        s = _int(r["drive_size_bytes"])
        if n is None or s is None:
            skip += 1
            continue
        out.add((n, st[_stream(r["drive_title"])], s))
    _SKIPPED["build series"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 3. the Register's numbering gaps
# ---------------------------------------------------------------------------

def register_index():
    """(the missing number, how many gaps share its class, the span it sits in).

    The span is next_seated - prev_seated: how wide the hole is in the numbering
    around it, which is a fact about the Register and not about the gap's cause.
    """
    rs = _rows(SOURCES["register gaps"])
    cls = _tally(r["class"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        n, p, q = _int(r["number"]), _int(r["prev_seated"]), _int(r["next_seated"])
        if n is None or p is None or q is None:
            skip += 1
            continue
        out.add((n, cls[r["class"]], q - p))
    _SKIPPED["register gaps"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 4. the recovered ledger, by conversation
# ---------------------------------------------------------------------------

def recovered_index():
    """(files recovered, distinct statuses, total bytes) per conversation.

    THE MEMBERS ARE CONVERSATIONS, NOT FILES.  3,224 ledger rows over 259
    conversations; charting the rows would make the index a restatement of the
    ledger, where charting the conversations asks what each one yielded.
    """
    rs = _rows(SOURCES["recovered ledger"])
    by = collections.defaultdict(list)
    for r in rs:
        by[r["conversation"]].append(r)
    out, skip = set(), 0
    for v in by.values():
        sz = [_int(x["size_bytes"]) for x in v]
        if any(s is None for s in sz):
            skip += 1
            continue
        out.add((len(v), len({x["status"] for x in v}), sum(sz)))
    _SKIPPED["recovered ledger"] = skip
    return frozenset(out)


def conversations():
    rs = _rows(SOURCES["recovered ledger"])
    return len({r["conversation"] for r in rs})


# ---------------------------------------------------------------------------
# 5. the coverage census
# ---------------------------------------------------------------------------

def coverage_index():
    """(how big its family is, how big its disposition is, is it held)."""
    rs = _rows(SOURCES["coverage census"])
    fam = _tally(r["family"] for r in rs)
    st = _tally(r["status"] for r in rs)
    return frozenset((fam[r["family"]], st[r["status"]],
                      1 if (r["held_as"] or "").strip() else 0) for r in rs)


# ---------------------------------------------------------------------------
# 6. this tree's own dockets
# ---------------------------------------------------------------------------

DOCKET_HEAD = re.compile(r"^## DOCKET (\d+) — (.+)$", re.M)


def _dockets():
    """[(number, state, lines)] read from DOCKET.md's own headings."""
    path = os.path.join(ROOT, SOURCES["dockets"])
    text = open(path, encoding="utf-8").read()
    hits = list(DOCKET_HEAD.finditer(text))
    out = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        head = m.group(2)
        state = ("PINNED" if "PINNED" in head else
                 "RULED" if "RULED" in head else
                 "REPAIRED" if "REPAIRED" in head else "OPEN")
        out.append((int(m.group(1)), state,
                    text[m.start():end].count("\n")))
    return out


def docket_index():
    """(docket number, how many dockets share its state, how long it is)."""
    d = _dockets()
    st = _tally(s for _n, s, _l in d)
    return frozenset((n, st[s], ln) for n, s, ln in d)


# ---------------------------------------------------------------------------

INDEXES = {
    "build series": build_index,
    "drive manifest": manifest_index,
    "register gaps": register_index,
    "recovered ledger": recovered_index,
    "coverage census": coverage_index,
    "dockets": docket_index,
}
_CELL = {}


def cell(name):
    if name not in _CELL:
        _CELL[name] = mi.cell(INDEXES[name]())
    return _CELL[name]


def closers(name):
    X = INDEXES[name]()
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def shapes():
    """[(name, cells, height, width)] -- cheap; no channel computed."""
    out = []
    for n, f in INDEXES.items():
        X = f()
        out.append((n, len(X), mi.height(X), mi.width(X)))
    return out


def collisions():
    """[(name, categories, distinct tallies)] -- where equal-sized kinds merge.

    The cost of using a category's SIZE in place of a ranking, named rather than
    left to be found.
    """
    out = []
    for nm, col, rel in (("drive manifest", "mime_type", SOURCES["drive manifest"]),
                         ("register gaps", "class", SOURCES["register gaps"])):
        t = _tally(r[col] for r in _rows(rel))
        out.append((nm, len(t), len(set(t.values()))))
    d = _dockets()
    t = _tally(s for _n, s, _l in d)
    out.append(("dockets", len(t), len(set(t.values()))))
    return out


def criterion(name):
    """{coordinate: moves under a monotone redundant append}.  DOCKET 3."""
    X = INDEXES[name]()
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


def against_demand():
    """[(name, cell, verdict)] -- where each of the six lands on the figure."""
    import demand
    import hexad
    F = hexad.figure()
    D = set(demand.demand(F))
    J, _r = demand.closure(F)
    out = []
    for n in INDEXES:
        c = cell(n)
        if c in D:
            v = "DEMANDED -- seating it drops E by one"
        elif c in J:
            v = "already a cell of the closure"
        elif demand.neutral(c, F):
            v = "neutral -- costs nothing, closes nothing"
        else:
            v = "disruptive -- raises E by %d" % (demand.E(F | {c}) - demand.E(F))
        out.append((n, c, v))
    return out


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("THE SIX FIRST-ORDER INDEXES THE ARTEFACT STORE CARRIES")
    print("=" * 74)
    print()
    print("1. THE SOURCES, ALL READ-ONLY AND ALL CORPUS-GENERATED.")
    for n, rel in SOURCES.items():
        print("   %-18s %s" % (n, rel))
    print()
    print("2. THE SHAPES.")
    print("   %-18s %-8s %-8s %s" % ("index", "cells", "height", "width"))
    for n, c, h, w in shapes():
        print("   %-18s %-8d %-8d %d" % (n, c, h, w))
    if any(_SKIPPED.values()):
        print("   skipped rows: %s"
              % {k: v for k, v in _SKIPPED.items() if v})
    else:
        print("   no row was skipped: every column parsed.")
    print()
    print("3. THE COST OF USING A CATEGORY'S SIZE INSTEAD OF A RANKING.")
    for nm, cats, dist in collisions():
        print("   %-18s %d categories -> %d distinct values%s"
              % (nm, cats, dist, "" if cats == dist else "   SOME MERGE"))
    print("   No RECONSTRUCTED order is carried anywhere in this file.")
    print()
    print("4. THE CHART CRITERION (DOCKET 3) AND THE CHANNELS.")
    print("   (the drive manifest's channel takes about four minutes)")
    bad = False
    for n in INDEXES:
        crit = criterion(n)
        bad |= any(crit.values())
        print("   %-18s %-12s closes %s"
              % (n, str(cell(n)), ", ".join(closers(n)) or "nothing"))
    if bad:
        print("   A COORDINATE MOVED. The reading below is void.")
        return 1
    print()
    print("5. WHERE THEY LAND.")
    for n, c, v in against_demand():
        print("   %-18s %-12s %s" % (n, str(c), v))
    print()
    print("6. REFUSED: to treat six as complete. M's point is that the supply")
    print("   keeps growing and this file cannot refute it -- it builds the six")
    print("   that were NAMED, and a seventh source found tomorrow is a seventh")
    print("   index. UNNAMED_SOURCES_MAY_EXIST = True. To read a table the")
    print("   corpus does not generate. To smooth one: a row that will not")
    print("   parse is skipped and counted.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("six sources named", len(SOURCES), 6)
    chk("six indexes built", len(INDEXES), 6)
    chk("every source file exists",
        [n for n, r in SOURCES.items()
         if not os.path.exists(os.path.join(ROOT, r))], [])
    chk("the supply is not claimed complete", UNNAMED_SOURCES_MAY_EXIST, True)

    chk("the manifest mirrors 820 files",
        len(_rows(SOURCES["drive manifest"])), 820)
    chk("the coverage census is 1,005 names",
        len(_rows(SOURCES["coverage census"])), 1005)
    chk("the Register has 132 numbered gaps",
        len(_rows(SOURCES["register gaps"])), 132)
    chk("the recovered ledger is 3,224 rows",
        len(_rows(SOURCES["recovered ledger"])), 3224)
    chk("over 259 conversations", conversations(), 259)
    d = _dockets()
    chk("the dockets are numbered 1..14 with none missing",
        sorted(n for n, _s, _l in d), list(range(1, 15)))
    chk("DOCKET 11 is pinned",
        next(s for n, s, _l in d if n == 11), "PINNED")
    chk("DOCKET 3 is ruled", next(s for n, s, _l in d if n == 3), "RULED")

    sh = {n: (c, h, w) for n, c, h, w in shapes()}
    chk("build series cells", sh["build series"][0], 131)
    chk("drive manifest cells", sh["drive manifest"][0], 661)
    chk("register gaps cells", sh["register gaps"][0], 132)
    chk("recovered ledger cells", sh["recovered ledger"][0], 259)
    chk("coverage census cells", sh["coverage census"][0], 23)
    chk("dockets cells", sh["dockets"][0], 14)
    chk("no row was skipped", {k: v for k, v in _SKIPPED.items() if v}, {})
    for n, (c, h, w) in sh.items():
        chk("%s: height and width bound the size" % n,
            max(h, w) <= c <= h * w, True)

    for n in INDEXES:
        crit = criterion(n)
        chk("%s: K admissible" % n, crit["K"], 0)
        chk("%s: height admissible" % n, crit["height"], 0)
        chk("%s: width admissible" % n, crit["width"], 0)
        chk("%s: the cell is a 3-tuple" % n, len(cell(n)), 3)

    chk("all six verdicts reported", len(against_demand()), 6)
    print("store selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
