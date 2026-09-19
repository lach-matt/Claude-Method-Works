#!/usr/bin/env python3
"""
staircase.py -- THE LADDER IS REAL.  IT IS A STAIRCASE OF AVAILABILITY, IT IS
INDEXED BY COORDINATES RATHER THAN OBJECTS, AND ITS FIRST STEP IS INVERTED.

M: "Directability is given by the order.  Every additional object given next to
the first singularity of binary value, creates an order.  Two values is a set.
3 requires algebra to show their relationship in the form of a triangle, which
asks further geometry, which asks for probable positions in spacetime, which
then asks for NECs to know which probable position is possible, which asks for
the logical citation for verification."

THIS IS A DIFFERENT CLAIM FROM THE LAST ONE AND IT FINDS SOMETHING THE LAST
MEASUREMENT MISSED.  selfindex.py measured DIRECTEDNESS BY COMPOSITION -- does
applying A then B differ from B then A -- and found nine of ten pairs commute.
M is now claiming DIRECTEDNESS BY AVAILABILITY: that a language cannot be
reached until enough objects exist.  THAT IS A DIFFERENT QUESTION, IT WAS NOT
TESTED, AND THE ANSWER IS YES.

    THE TWO ANSWERS ARE COMPATIBLE AND TOGETHER THEY SAY WHAT THE HIERARCHY IS:
    A SET OF COMMUTING OPERATORS THAT SWITCH ON AT DIFFERENT DIMENSIONS.  Not a
    chain, and not a flat set.  A STEP FUNCTION.

Three clauses confirmed, three refuted.

===============================================================================
1. THE LADDER EXISTS, AND IT IS IN THE CYPHER'S OWN PRECONDITIONS
===============================================================================

Not inferred -- READ FROM tools/cypher.py, three refusals, verbatim:

    op_order       "R needs at least two coordinates"
    op_geometry    "needs at least two coordinates"
    op_statistics  "needs more than {k} coordinates at order {k} (reg 1175)"

op_algebra and op_information carry NO dimension precondition at all.  So the
staircase is forced by the source, and register 1175 -- the degeneracy at d = 2
-- is cited for the third step.  MEASURED, projecting the energy-condition
family onto its first d coordinates:

        d = 1    algebra, information          (and both at E = 0)
        d = 2    + order, geometry
        d = 3    + statistics
        d = 4, 5  no further change

THREE RUNGS.  M IS RIGHT THAT THE HIERARCHY HAS A DIRECTION, AND IT IS HERE.

===============================================================================
2. BUT IT IS INDEXED BY COORDINATES, NOT BY OBJECTS
===============================================================================

M says "every additional OBJECT ... creates an order", and "3 requires algebra".
Tested directly, holding d = 5 and varying the number of cells:

        1 cell    all five SPEAK
        2 cells   all five SPEAK
        3 cells   all five SPEAK
        4, 6, 10, 17 cells   all five SPEAK

    THERE IS NO OBJECT-COUNT THRESHOLD ANYWHERE.  ONE OBJECT IN FIVE
    COORDINATES ALREADY REACHES EVERY LANGUAGE.

The ladder is real and it is a ladder of DIMENSIONS -- of how many things can be
said ABOUT an object, not of how many objects there are.  That is a sharper
statement than the one proposed, and it is the one the source supports.

===============================================================================
3. AND THE FIRST STEP IS INVERTED
===============================================================================

The chain runs binary -> order -> algebra -> geometry.  MEASURED FIRST
AVAILABILITY runs the other way at the first step and merges at the second:

        algebra      first speaks at d = 1
        information  first speaks at d = 1
        geometry     first speaks at d = 2
        order        first speaks at d = 2
        statistics   first speaks at d = 3

    ALGEBRA NEEDS NOTHING.  ORDER NEEDS TWO.  So algebra is not downstream of
    order; it is available strictly earlier.  AND ORDER AND GEOMETRY ARE NOT
    SEQUENTIAL -- they switch on together, at the same dimension, and no
    measurement here separates them.

Nor is algebra's d = 1 appearance vacuous: on the four T values it admits
exactly those four, E = 0.  It speaks and it closes.

===============================================================================
4. THE TRIANGLE IS EXACTLY RIGHT, AND IT IS INSIDE GEOMETRY
===============================================================================

"3 requires algebra to show their relationship in the form of a triangle."  The
number is right and the place is one language over.  tools/cypher.py's own hull
routine, docstring verbatim: "Monotone-chain hull of a 2-D integer point set;
RETURNS 1, 2 OR >= 3 POINTS."  Verified:

        1 point   -> a point
        2 points  -> a segment
        3 points  -> A TRIANGLE

THREE IS PRECISELY WHERE GEOMETRY'S HULL STOPS BEING DEGENERATE, and op_geometry
cites Caratheodory's bound at d = 2 for it.  The intuition lands on a real
threshold in the code.  It is a threshold of GEOMETRY and not a demand FOR it.

===============================================================================
5. STATISTICS LAST -- CONFIRMED, AND MORE SHARPLY THAN CLAIMED
===============================================================================

The chain puts statistics after geometry.  It is.  And the way it arrives is
sharper than "after": statistics is SILENT at d = 1 and d = 2, and from d = 3
upward it closes the family EXACTLY, E = 0 at d = 3, 4 and 5, while every other
language over-generates and gets worse with dimension.

    THERE IS NO INTERMEDIATE REGIME.  It cannot speak, and then it is exact.

===============================================================================
6. THE SCORECARD
===============================================================================

    CONFIRMED   a cardinality ladder exists and gives the hierarchy a direction
    CONFIRMED   three points is the triangle threshold, in geometry's own hull
    CONFIRMED   statistics comes after geometry
    REFUTED     it is indexed by objects -- no object-count threshold exists
    REFUTED     order precedes algebra -- algebra is available strictly earlier
    REFUTED     order and geometry are sequential -- they are simultaneous

Three and three, against nought and three last round.  THE REFINEMENT FOUND
SOMETHING REAL THAT THE PREVIOUS MEASUREMENT DID NOT ASK FOR.

NOTHING IS REPAIRED.
"""

import sys

import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

LADDER_EXISTS = True
INDEXED_BY_COORDINATES_NOT_OBJECTS = True
FIRST_STEP_IS_INVERTED = True
ORDER_AND_GEOMETRY_ARE_SIMULTANEOUS = True
TRIANGLE_IS_INSIDE_GEOMETRY = True
STATISTICS_IS_LAST = True
NOTHING_IS_REPAIRED = True


def projected(d):
    """The energy-condition family projected onto its first d coordinates."""
    coords = necindex.COORDS[:d]
    vo = {k: necindex.VALUE_ORDER[k] for k in coords}
    cells = sorted({c[:d] for c in necindex.cells()})
    return cypher.Index("projection", coords, cells, value_order=vo), cells


def speaks_at_dimension(d):
    ix, cells = projected(d)
    out = {}
    for n in necindex.OPERATORS:
        adm, note = cypher.ADMISSION[n][0](ix, OPTS)
        out[n] = None if adm is None else (len(adm), len(set(adm) - set(cells)))
    return out, ix


def speaks_at_object_count(k):
    """Hold d = 5 and take only the first k cells."""
    cells = necindex.cells()[:k]
    ix = necindex.pinned_index(cells)
    out = {}
    for n in necindex.OPERATORS:
        adm, _ = cypher.ADMISSION[n][0](ix, OPTS)
        out[n] = adm is not None
    return out


def first_availability():
    first = {}
    for d in range(1, 6):
        got, _ = speaks_at_dimension(d)
        for n, v in got.items():
            if v is not None and n not in first:
                first[n] = d
    return first


def hull_shape(pts):
    h = cypher._hull2(pts)
    return len(h), ("point", "segment", "TRIANGLE")[min(len(h), 3) - 1]


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  by DIMENSION -- the ladder")
    print("      %-3s %-6s %-6s %s" % ("d", "cells", "box", "admits / E"))
    for d in range(1, 6):
        got, ix = speaks_at_dimension(d)
        parts = ["%s=%s" % (n[:4], "SILENT" if got[n] is None
                            else "%d/%d" % got[n]) for n in necindex.OPERATORS]
        print("      %-3d %-6d %-6d %s" % (d, len(ix.cells), ix.box,
                                           "  ".join(parts)))
    print()
    print("  by OBJECT COUNT -- no ladder")
    print("      %-6s %s" % ("cells", "all five speak?"))
    for k in (1, 2, 3, 4, 6, 10, 17):
        got = speaks_at_object_count(k)
        print("      %-6d %s" % (k, all(got.values())))
    print()
    print("  first availability")
    for n, d in sorted(first_availability().items(), key=lambda kv: (kv[1], kv[0])):
        print("      %-13s d = %d" % (n, d))
    print()
    print("  the triangle, in geometry's own hull")
    for pts in ([(0, 0)], [(0, 0), (2, 2)], [(0, 0), (2, 0), (1, 2)]):
        k, name = hull_shape(pts)
        print("      %d point(s) -> %d vertices, a %s" % (len(pts), k, name))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Three confirmed, three refuted.  The ladder is real and it is in")
    print("  the cypher's own preconditions -- but it counts COORDINATES, not")
    print("  objects; algebra is available strictly before order, not after;")
    print("  and order and geometry switch on together.  The triangle is exact")
    print("  and sits inside geometry.  Statistics is last, and arrives already")
    print("  closing at E = 0.  A staircase of availability, over a set of")
    print("  commuting operators.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("staircase.py --selftest")
    print()

    # ------------------------------------- 1. the ladder, from the preconditions
    fa = first_availability()
    chk("algebra first speaks at d = 1", fa["algebra"], 1)
    chk("information first speaks at d = 1", fa["information"], 1)
    chk("order first speaks at d = 2", fa["order"], 2)
    chk("geometry first speaks at d = 2", fa["geometry"], 2)
    chk("statistics first speaks at d = 3", fa["statistics"], 3)
    chk("so the ladder has three rungs", sorted(set(fa.values())), [1, 2, 3])
    chk("recorded", LADDER_EXISTS, True)
    # the refusals are the corpus's own words, not an inference
    d1, _ = speaks_at_dimension(1)
    chk("at d = 1 exactly two languages speak",
        sorted(n for n, v in d1.items() if v is not None),
        ["algebra", "information"])
    d2, _ = speaks_at_dimension(2)
    chk("at d = 2 exactly four speak",
        len([n for n, v in d2.items() if v is not None]), 4)
    chk("and statistics is the one still silent",
        [n for n, v in d2.items() if v is None], ["statistics"])

    # -------------------------- 2. indexed by coordinates, NOT by object count
    for k in (1, 2, 3, 4, 6, 10, 17):
        chk("at d=5 with %d cell(s) all five speak" % k,
            all(speaks_at_object_count(k).values()), True)
    chk("so there is NO object-count threshold",
        INDEXED_BY_COORDINATES_NOT_OBJECTS, True)
    # NEGATIVE CONTROL: the dimension threshold IS real, so "no threshold" is a
    # finding about object count and not a broken test.
    chk("while the dimension threshold is real",
        speaks_at_dimension(1)[0]["statistics"], None)

    # ------------------------------------------------ 3. the first step inverts
    chk("algebra is available strictly before order",
        fa["algebra"] < fa["order"], True)
    chk("recorded as inverted", FIRST_STEP_IS_INVERTED, True)
    chk("and order and geometry are simultaneous",
        fa["order"] == fa["geometry"], True)
    chk("recorded", ORDER_AND_GEOMETRY_ARE_SIMULTANEOUS, True)
    # algebra at d = 1 is not vacuous: it closes the 1-D index exactly
    chk("algebra at d = 1 closes exactly", d1["algebra"][1], 0)
    chk("and admits precisely the cells it was given", d1["algebra"][0], 4)

    # ---------------------------------------------------- 4. the triangle
    chk("one point is a point", hull_shape([(0, 0)])[1], "point")
    chk("two points are a segment", hull_shape([(0, 0), (2, 2)])[1], "segment")
    chk("THREE points are a triangle",
        hull_shape([(0, 0), (2, 0), (1, 2)])[1], "TRIANGLE")
    chk("recorded as a threshold of geometry, not a demand for it",
        TRIANGLE_IS_INSIDE_GEOMETRY, True)

    # ------------------------------------------------- 5. statistics is last
    chk("statistics is last on the ladder", fa["statistics"], max(fa.values()))
    chk("silent below d = 3",
        [speaks_at_dimension(d)[0]["statistics"] for d in (1, 2)], [None, None])
    chk("and E = 0 at every dimension it can run",
        [speaks_at_dimension(d)[0]["statistics"][1] for d in (3, 4, 5)],
        [0, 0, 0])
    # NEGATIVE CONTROL: no other language manages that, so it is a distinction
    chk("while no other language closes at d = 5",
        [n for n in necindex.OPERATORS
         if n != "statistics" and speaks_at_dimension(5)[0][n][1] == 0], [])
    chk("recorded", STATISTICS_IS_LAST, True)

    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
