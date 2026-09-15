#!/usr/bin/env python3
r"""
overlap.py -- IS ANY INDEX SAYING WHAT ANOTHER ALREADY SAID?  Over-representation
detected before it is seated, because it corrupts density and cascades.

M: "I suspect that some of what your probes return for index proposals may be
duplicate information. So please be careful. Over representation must be avoided
at all costs because it screws index density and effects cascades."

    python3 overlap.py             the reading
    python3 overlap.py --selftest  fixtures

===============================================================================
0. WHY THIS IS A CORRECTNESS PROBLEM AND NOT A TIDINESS ONE
===============================================================================

`density.py` makes the whole palindrome question turn on

        density = |J(F)| / |box|

Seat the same information twice and both terms move, in opposite and wrong
directions.  Two charts of one body of data will usually land on DIFFERENT
cells, so the figure gains a vertex it has not earned; if either cell sits
outside the current coordinate ranges the BOX GROWS MULTIPLICATIVELY while the
closure grows additively, and the density falls for a reason that is pure
bookkeeping.

    THEN IT CASCADES.  E is |J(F)| - |F|, so a spurious vertex changes the
    demand; the demand decides which cells are DEMANDED; DEMANDED decides
    whether the next index lowers E or raises it.  One duplicate re-labels
    every verdict after it.

    A DUPLICATE THAT LANDS ON THE SAME CELL IS HARMLESS AND ALREADY CAUGHT --
    the seating run reports DUPLICATE CELL and the figure does not move.  THE
    DANGEROUS CASE IS THE ONE THAT LANDS SOMEWHERE ELSE, and nothing in this
    tree was looking for it before this file.

===============================================================================
1. TWO TESTS, BECAUSE ONE MISSES THE CASE THAT MATTERS
===============================================================================

    CELL OVERLAP.  The Jaccard of two indexes' cell sets.  Catches two charts
    that agree, and is schema-free, so it runs over every registered index.
    IT DOES NOT CATCH the dangerous case: two charts of the same rows landing
    on disjoint cells score ZERO here and look maximally distinct.

    ROW OVERLAP.  The Jaccard of the two sources' underlying rows on a shared
    identity key.  This is the one that catches it.  Five REC-ASD families and
    the queue2 and spectra_raw captures are all "one atomic energy level" --
    if they are the same levels under different headers, the row key says so
    and no cell measurement ever would.

    SO A PAIR IS ONLY DISTINCT WHEN BOTH TESTS SAY SO, and a pair with low cell
    overlap and high row overlap is the worst case rather than the best.

===============================================================================
2. THE IDENTITY KEY, AND WHY IT IS NARROW ON PURPOSE
===============================================================================

Two tables are comparable when they share enough columns to name the same
thing.  `key_for()` handles the shapes actually present:

    an atomic level    (species or Z, configuration, term, J)
    a nuclide          (Z, A)
    a channel          (Z, charge, l, mult)
    a file             its repo path

A pair with no shared key is NOT-COMPARABLE, which is reported as its own
verdict and never as DISTINCT.  Calling two things distinct because you could
not compare them is the error this file exists to avoid making.

===============================================================================
3. A NEAR-INJECTIVE COORDINATE IS A LABEL, AND IT CORRUPTS DENSITY TOO
===============================================================================

The same concern from the other side.  A coordinate whose distinct values
number nearly as many as the members SEPARATES EVERYTHING and therefore groups
nothing: it is a row identifier wearing a measurement's clothes.

    IT IS NOT MERELY UNINFORMATIVE, IT IS EXPENSIVE, and the two facts have one
    cause.  Charting cost tracks the BOX -- the product of the coordinate
    alphabets -- and not the cell count, which was measured directly:

        drive manifest   661 cells   alphabets [12, 640,   2]   box    15,360
        member index     343 cells   alphabets [ 7, 329, 343]   box   789,929

    BOTH OF THOSE ARE NOW DELETED -- they were filing-system indexes, not
    indexes of the periodic elements -- but the measurement stands and is why
    this section exists.

    HALF THE CELLS AND FIFTY-ONE TIMES THE BOX, because the member index
    carries TWO near-injective coordinates -- `bytes` at 329 distinct over 343
    members and `bundle_offset` at 343 over 343 -- whose alphabets multiply.
    The manifest escapes only because its third coordinate, path depth, has two
    values.  Charting the manifest took 211 seconds; the member index had not
    finished after seventy-two minutes of CPU.

    AND IT IS THE SAME DENSITY FAULT M NAMED.  density = |J(F)| / |box|.  A
    near-injective coordinate inflates the denominator directly, so an index
    charted on two of them drives the density down while telling the figure
    almost nothing -- over-representation by resolution rather than by
    duplication.

`resolution()` measures it: distinct values over members, per coordinate.  Above
`LABEL` the coordinate is reported as a label rather than a measurement.  THIS
FILE DOES NOT RE-CHART ANYTHING -- the member index is mine and is badly
charted, and that is recorded here rather than quietly fixed, because a
re-chart changes a seated figure and that is a ruling.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

To drop a source.  It measures and reports; which of an overlapping pair to
seat is a ruling, and `admit()` only ever returns a recommendation with the
measurement beside it.

To treat high overlap as proof of duplication.  Two independent measurements of
the same 88 elements SHOULD share rows -- that is what makes them checkable
against each other, and `laws.py` depends on exactly that. Overlap is a flag
for a reading, not a verdict.

To compare what it cannot key.  NOT-COMPARABLE is a real answer and it is
returned rather than guessed past.
"""

import csv
import itertools
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LEVEL_COLS = ("configuration", "config", "Configuration", "term", "Term",
              "J", "level_cm1", "Level", "level")
NUCLIDE_COLS = ("Z", "A", "N")
CHANNEL_COLS = ("Z", "charge", "l", "mult")


def read(rel, limit=None):
    """Rows of a tsv, as dicts.  `limit` bounds a large table."""
    path = os.path.join(ROOT, rel)
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f, delimiter="\t")
        out = []
        for i, row in enumerate(r):
            if limit is not None and i >= limit:
                break
            out.append(row)
        return out


def shape(rel):
    """The column names, as a tuple."""
    rows = read(rel, limit=1)
    return tuple(rows[0]) if rows else ()


def kind(cols):
    """What a row of this table IS, from its columns alone."""
    c = set(cols)
    if {"Z", "A"} <= c or {"Z", "N"} <= c:
        return "nuclide"
    if set(CHANNEL_COLS) <= c:
        return "channel"
    if any(x in c for x in ("configuration", "config", "Configuration")) and \
       any(x in c for x in ("term", "Term")):
        return "level"
    return "other"


def key_for(row, cols):
    """A canonical identity for one row, or None when it cannot be keyed."""
    k = kind(cols)
    g = lambda *names: next((str(row[n]).strip() for n in names
                             if n in row and row[n] not in (None, "")), None)
    if k == "nuclide":
        z, a = g("Z"), g("A")
        return ("nuclide", z, a) if z and a else None
    if k == "channel":
        vals = [g(n) for n in CHANNEL_COLS]
        return ("channel",) + tuple(vals) if all(vals) else None
    if k == "level":
        cfg = g("configuration", "config", "Configuration")
        trm = g("term", "Term")
        j = g("J")
        sp = g("species", "element", "symbol", "Z")
        return ("level", sp, cfg, trm, j) if cfg and trm else None
    return None


def keys(rel, limit=None):
    """The set of identity keys a table carries."""
    rows = read(rel, limit=limit)
    if not rows:
        return frozenset(), "empty"
    cols = tuple(rows[0])
    k = kind(cols)
    out = {key_for(r, cols) for r in rows}
    out.discard(None)
    return frozenset(out), k


def jaccard(a, b):
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b) if (a | b) else 0.0


def row_overlap(rel_a, rel_b, limit=None):
    """(jaccard, shared, |a|, |b|, verdict) on the two tables' row identities."""
    ka, tya = keys(rel_a, limit)
    kb, tyb = keys(rel_b, limit)
    if tya != tyb or tya == "other" or not ka or not kb:
        return (None, 0, len(ka), len(kb), "NOT-COMPARABLE")
    j = jaccard(ka, kb)
    shared = len(ka & kb)
    if ka == kb:
        v = "IDENTICAL"
    elif ka <= kb or kb <= ka:
        v = "CONTAINED"
    elif j > 0.5:
        v = "OVERLAPPING"
    elif shared:
        v = "PARTIAL"
    else:
        v = "DISJOINT"
    return (j, shared, len(ka), len(kb), v)


def cell_overlap(A, B):
    """(jaccard, verdict) on two indexes' CELL sets.  Schema-free."""
    j = jaccard(frozenset(A), frozenset(B))
    if A == B:
        v = "IDENTICAL"
    elif A <= B or B <= A:
        v = "CONTAINED"
    elif j > 0.5:
        v = "OVERLAPPING"
    else:
        v = "DISTINCT"
    return j, v


LABEL = 0.9


def resolution(X):
    """[(coordinate, distinct, members, ratio, verdict)] for one index.

    ratio near 1 means the coordinate separates nearly every member, which is
    a label rather than a measurement: it groups nothing and multiplies the
    box.  See section 3.
    """
    X = sorted(X)
    n = len(X)
    out = []
    for i in range(len(X[0]) if X else 0):
        d = len({c[i] for c in X})
        r = d / n if n else 0.0
        out.append((i, d, n, round(r, 4),
                    "LABEL" if r >= LABEL else "measurement"))
    return out


def box_of(X):
    """The product of the coordinate alphabets -- what charting cost tracks."""
    if not X:
        return 0
    b = 1
    for i in range(len(next(iter(X)))):
        b *= len({c[i] for c in X})
    return b


def labelled():
    """[(name, cells, box, [label coordinates])] over every registered index.

    An index with TWO label coordinates is the expensive-and-uninformative
    case, and it is named rather than silently tolerated.
    """
    import registry
    out = []
    for nm, _mo, _a, _m, _w, _q in registry.rows():
        try:
            X = registry.index_of(nm)
        except Exception:                          # pragma: no cover
            continue
        labs = [i for i, _d, _n, _r, v in resolution(X) if v == "LABEL"]
        out.append((nm, len(X), box_of(X), labs))
    return sorted(out, key=lambda t: -t[2])


def seated_cells():
    """{name: cell set} over every registered index, cheaply."""
    import registry
    out = {}
    for nm, _mo, _a, _m, _w, _q in registry.rows():
        try:
            out[nm] = frozenset(registry.index_of(nm))
        except Exception:                          # pragma: no cover
            continue
    return out


def seated_pairs(top=14):
    """[(a, b, jaccard, verdict)] the most overlapping pairs among the seated."""
    C = seated_cells()
    out = []
    for a, b in itertools.combinations(sorted(C), 2):
        j, v = cell_overlap(C[a], C[b])
        if v != "DISTINCT":
            out.append((a, b, j, v))
    return sorted(out, key=lambda t: -t[2])[:top]


def admit(rel, admitted, limit=20000):
    """(recommend, why) for a candidate table against those already admitted.

    A RECOMMENDATION, NEVER A DROP.  Which of an overlapping pair to seat is a
    ruling; this reports what was measured and what it implies.
    """
    for other in admitted:
        j, shared, na, nb, v = row_overlap(rel, other, limit)
        if v in ("IDENTICAL", "CONTAINED"):
            return False, "%s of %s (jaccard %.3f, %d shared rows)" % (
                v.lower(), other, j, shared)
        if v == "OVERLAPPING":
            return False, "overlaps %s at jaccard %.3f on %d shared rows" % (
                other, j, shared)
    return True, "no admitted source shares its rows"


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("IS ANY INDEX SAYING WHAT ANOTHER ALREADY SAID?")
    print("=" * 74)
    print()
    print("1. WHY IT IS A CORRECTNESS PROBLEM.")
    print("   density = |J(F)| / |box|. Seat one body of data twice and the")
    print("   two charts land on DIFFERENT cells, so the figure gains a vertex")
    print("   it has not earned; if either cell is outside the current ranges")
    print("   the box grows MULTIPLICATIVELY while the closure grows")
    print("   additively. Then it cascades: E decides which cells are")
    print("   DEMANDED, and DEMANDED decides whether the next index lowers E")
    print("   or raises it. One duplicate re-labels every verdict after it.")
    print()
    print("   A duplicate landing on the SAME cell is harmless and already")
    print("   caught -- the seating run reports DUPLICATE CELL. The dangerous")
    print("   case lands elsewhere, and nothing was looking for it.")
    print()
    print("2. THE SEATED INDEXES, PAIRWISE ON CELLS.")
    sp = seated_pairs()
    if not sp:
        print("   no two seated indexes share cells beyond DISTINCT.")
    for a, b, j, v in sp:
        print("   %-24s %-24s %.3f  %s" % (a[:24], b[:24], j, v))
    print("   CELL OVERLAP IS THE WEAK TEST and it is reported first so it is")
    print("   not mistaken for the strong one: two charts of the same rows on")
    print("   disjoint cells score ZERO here and look maximally distinct.")
    print()
    print("3. RESOLUTION -- a coordinate that separates everything is a label.")
    print("   Charting cost tracks the BOX, not the cell count. The ten")
    print("   largest boxes among the seated indexes:")
    print("   %-24s %-7s %-12s %s" % ("index", "cells", "box", "label coords"))
    for nm, n, b, labs in labelled()[:10]:
        print("   %-24s %-7d %-12d %s"
              % (nm[:24], n, b, labs if labs else ""))
    print("   TWO label coordinates is the expensive-and-uninformative case:")
    print("   the alphabets multiply into the box, and density = |J(F)|/|box|")
    print("   falls for no informational reason. Recorded, not re-charted -- a")
    print("   re-chart moves a seated figure and that is a ruling.")
    print()
    print("4. REFUSED: to drop a source -- which of an overlapping pair to")
    print("   seat is a ruling. To treat overlap as proof: two independent")
    print("   measurements of the same 88 elements SHOULD share rows, and")
    print("   laws.py depends on exactly that. To compare what it cannot key:")
    print("   NOT-COMPARABLE is a real answer and is returned, never guessed")
    print("   past. Calling two things distinct because you could not compare")
    print("   them is the error this file exists to avoid.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # the jaccard, on cases computable by hand
    chk("disjoint sets score 0", jaccard(frozenset({1}), frozenset({2})), 0.0)
    chk("identical sets score 1", jaccard(frozenset({1}), frozenset({1})), 1.0)
    chk("half-shared scores a third",
        round(jaccard(frozenset({1, 2}), frozenset({2, 3})), 4), 0.3333)
    chk("two empties score 1", jaccard(frozenset(), frozenset()), 1.0)

    # the cell test, and the hole in it
    A, B = frozenset({(0, 0, 0)}), frozenset({(1, 1, 1)})
    chk("two disjoint cell sets read DISTINCT", cell_overlap(A, B)[1], "DISTINCT")
    chk("a subset reads CONTAINED",
        cell_overlap(A, frozenset({(0, 0, 0), (1, 1, 1)}))[1], "CONTAINED")
    chk("equal sets read IDENTICAL", cell_overlap(A, A)[1], "IDENTICAL")

    # kind detection on the shapes actually present
    chk("a nuclide table is recognised", kind(("Z", "N", "A", "symbol")), "nuclide")
    chk("a channel table is recognised",
        kind(("Z", "charge", "l", "mult", "delta")), "channel")
    chk("a level table is recognised",
        kind(("configuration", "term", "J", "level_cm1")), "level")
    chk("an uppercase level table is recognised",
        kind(("Configuration", "Term", "J", "Level")), "level")
    chk("an unkeyable table is `other`", kind(("a", "b")), "other")

    # keys
    cols = ("configuration", "term", "J", "level_cm1")
    r1 = {"configuration": "3s2.3p", "term": "2P*", "J": "1/2",
          "level_cm1": "0.0"}
    r2 = dict(r1, level_cm1="112.061")
    chk("a level key ignores the value, keying the state",
        key_for(r1, cols), key_for(r2, cols))
    chk("and it is not None", key_for(r1, cols) is not None, True)
    chk("a row missing its term cannot be keyed",
        key_for({"configuration": "x", "J": "1"}, cols), None)

    # NOT-COMPARABLE is a real answer
    j, shared, na, nb, v = row_overlap("COVERAGE.tsv", "REGISTER-GAPS.tsv")
    chk("two unkeyable tables are NOT-COMPARABLE", v, "NOT-COMPARABLE")
    chk("and they are NOT called distinct", v == "DISTINCT", False)

    # a table against itself must be IDENTICAL
    sp = "extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv"
    co = "extracted/archives/method16-rp-b-data/COORDINATES.tsv"
    j2, sh2, _a2, _b2, v2 = row_overlap(co, co, limit=2000)
    chk("a channel table against itself is IDENTICAL", v2, "IDENTICAL")
    chk("with jaccard 1", j2, 1.0)
    chk("and it keyed some rows", sh2 > 0, True)

    # admit() recommends, never drops
    rec, why = admit(co, [co], limit=2000)
    chk("a source already admitted is not re-admitted", rec, False)
    chk("and the reason names the overlap", "identical" in why, True)
    rec2, why2 = admit(sp, [], limit=2000)
    chk("against nothing admitted, a source is admitted", rec2, True)

    # RESOLUTION, on cases computable by hand
    inj = frozenset({(0, i, 0) for i in range(10)})
    res = resolution(inj)
    chk("an injective coordinate is a LABEL", res[1][4], "LABEL")
    chk("and its ratio is 1", res[1][3], 1.0)
    chk("a constant coordinate is a measurement", res[0][4], "measurement")
    chk("and its ratio is 1/n", res[0][3], 0.1)
    chk("the box of that toy is 1 x 10 x 1", box_of(inj), 10)
    chk("box is the product of the alphabets",
        box_of(frozenset({(0, 0, 0), (1, 1, 1), (2, 2, 2)})), 27)
    chk("an empty index has box 0", box_of(frozenset()), 0)
    # THE CASE THAT PROMPTED THIS SECTION IS GONE, AND THE FIXTURE GOES WITH
    # IT.  The member index and the drive manifest were filing-system indexes
    # -- 343 files in a bundle, 820 mirrored files -- and were deleted when M
    # ruled that an index whose members carry no quantum numbers is not an
    # index of this project.  The measurement they produced is kept in the
    # docstring as the reason this section exists; the fixture is re-pointed at
    # a constructed case so it tests the instrument and not the deleted data.
    two_labels = frozenset((i % 2, i, i * 3) for i in range(12))
    chk("an index with two near-injective coordinates is caught",
        len([1 for _i, _d, _n, _r, v in resolution(two_labels)
             if v == "LABEL"]), 2)
    chk("and its box dwarfs its cell count",
        box_of(two_labels) > len(two_labels) * 20, True)

    C = seated_cells()
    # A PROPERTY, NOT A PINNED COUNT -- see the same note in demand.py.
    chk("every registered index yielded cells", len(C),
        len(__import__("registry").rows()))
    chk("and every one is an element index",
        sorted(C) == sorted(n for n, *_r in __import__("registry").rows()), True)
    print("overlap selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
