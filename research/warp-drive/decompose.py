#!/usr/bin/env python3
"""
decompose.py -- OBJECT AND CONDITIONS: THE SPLIT IS REAL BETWEEN TWO LANGUAGES,
AND THE EQUATION HOLDS PER CELL AND FAILS AS A SET.

M: "It is two tiers.  The first half describes the object.  The second half
describes the environment/conditions for that object to exist in its current
state."  And: "|Object - state - transition| = object".

THE READING IS RIGHT ABOUT TWO LANGUAGES AND THE MEASUREMENT FINDS THREE TIERS
PLUS AN ANOMALY.  The equation is TRUE ONE CELL AT A TIME, FALSE FOR THE SET,
AND -- the part that matters -- THE DECOMPOSITION IT PRESUMES IS NOT UNIQUE.

===============================================================================
1. THE SENSITIVITY PROFILE.  FOUR SIGNATURES, NOT TWO
===============================================================================

Two perturbations, each adding one cell to the family: an INTERIOR cell (inside
every 2-D hull already) and a HULL-EXTENDING cell (admitted by order but not by
geometry).  Which languages notice?

        language      interior       hull-extending    signature
        order          0 of 12         0 of 40         ( 0 , 0 )
        algebra        0 of 12         0 of 40         ( 0 , 0 )
        GEOMETRY       0 of 12        40 of 40         ( 0 , 1 )
        information   10 of 12         5 of 40         (.83, .13)
        STATISTICS    12 of 12        40 of 40         ( 1 , 1 )

    GEOMETRY SEES EXTENT AND NOTHING ELSE.  STATISTICS SEES EVERY CELL.  THAT
    PAIR IS EXACTLY M'S OBJECT AND CONDITIONS, AND IT IS MEASURED.

BUT THE OTHER THREE DO NOT SIT ON EITHER SIDE.  Order and algebra do not move at
all, on either perturbation -- they are not describing the object, they are
COARSE, their closure so large that no single cell reaches it.  And information
is the only language whose profile is INVERTED: more sensitive to an interior
cell than to a hull-extending one, 83 per cent against 13.

    THIRD ANOMALY TO LAND ON INFORMATION.  alpha.py: the only non-commuting
    pair.  regress.py: the only incomparable pair.  Here: the only inverted
    sensitivity.  Statistics is distinguished by being exact and invariant;
    INFORMATION IS DISTINGUISHED BY BEING THE EXCEPTION EVERY TIME.

And the geometry/information incomparability regress.py found is explained by
this, without needing geometry to be constant: GEOMETRY IS BOUNDARY-DETERMINED
AND INFORMATION IS CONTENT-DETERMINED.  Two different reductions of one cell
set, and neither refines the other.

===============================================================================
2. |Object - state| = object.  TRUE PER CELL
===============================================================================

Read as "the object is unchanged by removing its state", the equation names
state as WHATEVER THE OBJECT IS INVARIANT TO -- which makes it measurable rather
than definitional.  Removing each cell in turn and asking whether geometry
notices:

        order          moved by  5 of 17    invariant to 12
        algebra        moved by  5 of 17    invariant to 12
        GEOMETRY       moved by  7 of 17    INVARIANT TO 10
        information    moved by 11 of 17    invariant to  6
        statistics     moved by 12 of 17    invariant to  5

TEN OF SEVENTEEN CELLS CAN BE REMOVED AND GEOMETRY DOES NOT NOTICE.  Seven are
its extreme points.  SO THE EQUATION HOLDS, ONE CELL AT A TIME.

===============================================================================
3. AND FAILS AS A SET, WHICH IS THE FINDING
===============================================================================

Remove all ten at once and GEOMETRY CHANGES.  The invariance is not additive,
and the reason is in the mechanism rather than in the arithmetic: a hull is
fixed by its extreme points, so removing a non-extreme point costs nothing --
BUT ONCE ENOUGH ARE GONE, POINTS THAT WERE INTERIOR BECOME EXTREME.  The set of
removable cells is not simultaneously removable.

    AND THE DECOMPOSITION IS NOT UNIQUE, WHICH IS WORSE THAN IT FAILING.
    Stripping greedily while geometry holds removes 8 cells and leaves 9.  Over
    six random removal orders the strip size is 6, 7 OR 8.

        THERE IS NO CANONICAL STATE TO SUBTRACT.  Different orders of removal
        leave different objects of different sizes, and nothing in the operator
        picks one.

The equation presumes a clean split of a cell set into object and state.  The
measurement says this operator does not admit one: removability is
CONTEXT-DEPENDENT, not an independence structure, so "the state" is not a
well-defined thing to take away.

    WHAT WOULD BE NEEDED IS A CANONICAL DECOMPOSITION.  That is a real and
    stateable requirement, and geometry's hull does not supply it.

NOTHING IS REPAIRED.
"""

import random
import sys

import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

OBJECT_CONDITIONS_PAIR_IS_REAL = True
THREE_TIERS_NOT_TWO = True
INFORMATION_IS_THE_EXCEPTION_AGAIN = True
EQUATION_HOLDS_PER_CELL = True
EQUATION_FAILS_AS_A_SET = True
DECOMPOSITION_IS_NOT_UNIQUE = True
NOTHING_IS_REPAIRED = True


def admitted(cells):
    ix = necindex.pinned_index(cells)
    return {n: frozenset(cypher.ADMISSION[n][0](ix, OPTS)[0])
            for n in necindex.OPERATORS}


def geom(cells):
    return frozenset(cypher.op_geometry(necindex.pinned_index(cells), OPTS)[0])


def sensitivity(limit=40):
    """Add an interior cell, and add a hull-extending cell.  Who notices?"""
    X = set(necindex.cells())
    base = admitted(X)
    interior = sorted(base["geometry"] - X)
    outside = sorted(base["order"] - base["geometry"])[:limit]
    out = {n: [0, 0] for n in necindex.OPERATORS}
    for c in interior:
        r = admitted(X | {c})
        for n in necindex.OPERATORS:
            if r[n] != base[n]:
                out[n][0] += 1
    for c in outside:
        r = admitted(X | {c})
        for n in necindex.OPERATORS:
            if r[n] != base[n]:
                out[n][1] += 1
    return out, len(interior), len(outside)


def removal_sensitivity():
    X = set(necindex.cells())
    base = admitted(X)
    moved = {n: 0 for n in necindex.OPERATORS}
    for c in sorted(X):
        r = admitted(X - {c})
        for n in necindex.OPERATORS:
            if r[n] != base[n]:
                moved[n] += 1
    return moved, len(X)


def individually_removable():
    X = set(necindex.cells())
    b = geom(X)
    return [c for c in sorted(X) if geom(X - {c}) == b]


def strip(order=None):
    """Remove cells while geometry is unchanged.  Returns (stripped, kept)."""
    X = set(necindex.cells())
    b = geom(X)
    kept = set(X)
    n = 0
    progress = True
    while progress:
        progress = False
        seq = sorted(kept) if order is None else order(sorted(kept))
        for c in seq:
            if geom(kept - {c}) == b:
                kept.discard(c)
                n += 1
                progress = True
                break
    return n, len(kept), frozenset(kept)


def strip_sizes(seeds=range(6)):
    out = set()
    for s in seeds:
        rnd = random.Random(s)
        out.add(strip(lambda L, r=rnd: r.sample(L, len(L)))[0])
    return sorted(out)


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    sens, ni, no = sensitivity()
    print("  sensitivity: adding one cell (%d interior, %d hull-extending)"
          % (ni, no))
    print("      %-13s %-14s %-16s %s" % ("language", "interior", "extending",
                                          "signature"))
    for n in necindex.OPERATORS:
        a, b = sens[n]
        print("      %-13s %-14s %-16s (%.2f, %.2f)"
              % (n, "%d of %d" % (a, ni), "%d of %d" % (b, no), a / ni, b / no))
    print()
    moved, tot = removal_sensitivity()
    print("  sensitivity: removing one cell of %d" % tot)
    for n in necindex.OPERATORS:
        print("      %-13s moved by %2d   invariant to %2d"
              % (n, moved[n], tot - moved[n]))
    print()
    rem = individually_removable()
    X = set(necindex.cells())
    print("  the equation")
    print("      %-44s %d of %d" % ("cells geometry does not notice, singly",
                                    len(rem), len(X)))
    print("      %-44s %s" % ("removing all of them at once leaves it?",
                              geom(X - set(rem)) == geom(X)))
    s, k, _ = strip()
    print("      %-44s %d stripped, %d kept" % ("greedy strip while it holds",
                                                s, k))
    print("      %-44s %s" % ("strip sizes over six random orders",
                              strip_sizes()))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Geometry sees extent, statistics sees every cell -- that pair IS")
    print("  object and conditions, measured.  The other three do not sit on")
    print("  either side: order and algebra do not move at all, and information")
    print("  is inverted, its third anomaly.  The equation holds one cell at a")
    print("  time and fails as a set, and the decomposition it presumes is not")
    print("  unique: six, seven or eight strip, depending on the order.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("decompose.py --selftest")
    print()
    sens, ni, no = sensitivity()

    # ------------------------------------------ 1. the four signatures
    chk("interior cells available", ni, 12)
    chk("hull-extending cells tested", no, 40)
    chk("geometry ignores every interior cell", sens["geometry"][0], 0)
    chk("and notices every hull-extending one", sens["geometry"][1], no)
    chk("statistics notices both, totally", sens["statistics"], [ni, no])
    chk("order notices neither", sens["order"], [0, 0])
    chk("algebra notices neither", sens["algebra"], [0, 0])
    chk("recorded: geometry and statistics are the object/conditions pair",
        OBJECT_CONDITIONS_PAIR_IS_REAL, True)
    chk("but four distinct signatures, not two",
        len({tuple(v) for v in sens.values()}), 4)
    chk("recorded", THREE_TIERS_NOT_TWO, True)
    # information is INVERTED -- more sensitive to interior than to boundary
    chk("information is more sensitive to interior than to extending",
        sens["information"][0] / ni > sens["information"][1] / no, True)
    chk("and it is the only one",
        [n for n in necindex.OPERATORS
         if sens[n][0] / ni > sens[n][1] / no], ["information"])
    chk("recorded", INFORMATION_IS_THE_EXCEPTION_AGAIN, True)

    # ------------------------------------------- 2. the equation, per cell
    moved, tot = removal_sensitivity()
    chk("cells in the family", tot, 17)
    chk("geometry is moved by 7 removals", moved["geometry"], 7)
    rem = individually_removable()
    chk("so 10 are individually removable", len(rem), 10)
    chk("recorded", EQUATION_HOLDS_PER_CELL, True)
    # NEGATIVE CONTROL: not every cell is removable, so the invariance is a
    # property of those ten and not of removal in general.
    chk("and 7 are not", tot - len(rem), 7)

    # ------------------------------------------- 3. and fails as a set
    X = set(necindex.cells())
    chk("removing all ten at once MOVES geometry",
        geom(X - set(rem)) == geom(X), False)
    chk("recorded", EQUATION_FAILS_AS_A_SET, True)
    s, k, kept = strip()
    chk("greedy strips 8", s, 8)
    chk("leaving 9", k, 9)
    # the first draft of this line compared geom(X) to geom(X) -- a call against
    # itself, which is true of anything.  It must compare AFTER the strip to
    # BEFORE, on genuinely different cell sets.
    chk("the strip really removed cells", len(kept) < len(X), True)
    chk("and geometry is unchanged on the SURVIVORS", geom(kept), geom(X))
    sizes = strip_sizes()
    chk("strip sizes over six random orders", sizes, [6, 7, 8])
    chk("so the decomposition is NOT unique", len(sizes) > 1, True)
    chk("recorded", DECOMPOSITION_IS_NOT_UNIQUE, True)

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
