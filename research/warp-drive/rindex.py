#!/usr/bin/env python3
r"""
rindex.py -- THE REFUSAL INDEX SEATED, and the fixed-point question settled:
IT DEPENDS ON THE CHART, and two faithful charts disagree.

M: "build these three as well please" -- the sixth master index, and the one
refusal.py declined to build.

    python3 rindex.py             the reading
    python3 rindex.py --selftest  fixtures

===============================================================================
0. WHAT refusal.py REFUSED, AND WHY THIS IS NOT AN OVERRULING
===============================================================================

refusal.py section 5, verbatim:

    "R is computed FROM the inventory.  Seating it as a member changes the
    inventory, which changes R, which changes what was seated.  That is a
    fixed-point problem and not a formality.  This file therefore seats R as a
    FUNCTION ON THE MEMBERS ... and does not add a row.  **Whether the iteration
    converges is open here and is the first thing to settle next.**"

    THIS FILE SETTLES IT AND THE REFUSAL SURVIVES.  The iteration is run, and on
    the one chart that is both faithful and natural it does NOT converge -- it
    enters a two-cycle.  refusal.py was right not to seat R, and it is now right
    for a measured reason rather than a cautious one.

===============================================================================
1. THE CONSTRUCTION, AND THE MAP WHOSE FIXED POINT IS IN QUESTION
===============================================================================

R(X) is a SET of refusal kinds, a subset of {K0..K7}.  To be an index it must
be a set of CELLS, so each member's refusal set is charted:

        indicator      the 8-bit vector (1 if Kn in R(X) else 0)
        (|R|, min, max)  size, least kind, greatest kind
        (|R|, sum)       size and the sum of the kinds
        (min, max)       least and greatest kind

The map whose fixed point is at issue is then

        F(R)  =  { chart(R(X)) : X in the nine seated indexes, and X = R }

-- rebuild the refusal index over an inventory that already contains R.  A fixed
point is F(R) = R: an R that is unchanged by its own seating.

    EXACTLY ONE OF THESE CHARTS IS THE OBVIOUS ONE.  The indicator vector loses
    nothing -- it IS the refusal set, written as a tuple -- and refusal.py has
    already established that the nine refusal sets are pairwise distinct, so it
    charts nine indexes onto nine cells.  The other three are coarsenings kept
    as controls.

===============================================================================
2. THE ANSWER: CHART-DEPENDENT, AND THE FAITHFUL CHARTS DISAGREE
===============================================================================

        chart              cells  faithful  K    period  verdict
        indicator          9      yes       K0   2       CYCLES, no fixed point
        (|R|, min, max)    6      no        K7   2       CYCLES, no fixed point
        (|R|, sum)         9      yes       K7   1       FIXED POINT
        (min, max)         1      no        K7   1       FIXED POINT

    **TWO FAITHFUL CHARTS, AND THEY DISAGREE.**  Both keep nine indexes on nine
    cells; the indicator cycles and (|R|, sum) is a fixed point from the first
    step.  So "does the refusal index converge when seated?" HAS NO ANSWER
    INDEPENDENT OF THE CHART, and that is the same shape as DOCKET 3's finding
    about the master cell.  Faithfulness does not settle it; coarseness does not
    settle it; only naming a chart settles it.

    **AND THE CYCLE IS ONE BIT WIDE.**  On the indicator chart the two states of
    the cycle differ in exactly one cell, and those two cells differ in exactly
    one coordinate: the K5 bit.

        A   (1, 1, 0, 1, 0, 1, 0, 1)     K0, K1, K3, K5, K7
        B   (1, 1, 0, 1, 0, 0, 0, 1)     K0, K1, K3,     K7

    Seating R makes K5 occur in the inventory's refusal structure; recomputing
    with K5 present makes it stop occurring; and so on.  **K5 is one of the three
    channels charts3.py proved unreachable from the element address.**  It is not
    reachable here either -- it flickers.

===============================================================================
3. SO THE ORIGINAL REFUSAL IS UPHELD, AND SHARPENED
===============================================================================

    refusal.py declined to seat R because the fixed point was unsettled.  It is
    now settled and the answer does not licence seating: on the faithful,
    obvious chart there IS NO fixed point, so there is no R that survives its own
    seating.  Seating it would mean choosing the chart that happens to converge,
    which is choosing the answer.

    WHAT THIS FILE THEREFORE SEATS IS NOTHING.  It builds R as an index, measures
    it, runs the iteration, and reports.  R0 -- the refusal index over the nine,
    before any seating -- is a perfectly good object with a cell of its own, and
    it is the thing quoted as "the sixth master index" throughout.  What is NOT
    claimed is that it is a MEMBER of the master index.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    TO CALL THE (|R|, sum) FIXED POINT A RESOLUTION.  It is a fixed point of one
    chart among four, and the chart that disagrees with it is at least as
    faithful.  Quoting the convergent one alone would be choosing evidence.

    TO READ THE FLICKERING K5 AS AN OCCURRENCE.  A kind that appears on even
    iterations and vanishes on odd ones is not present in the corpus.  It is the
    signature of a construction that does not settle.

    TO SEAT R.  See section 3.  Nothing here is added to mi.inventory().
"""

import sys

import hlaw
import mi
import refusal

MAX_STEPS = 14


def indicator(S):
    """The refusal set as an 8-bit vector -- loses nothing."""
    return tuple(1 if k in S else 0 for k in range(8))


CHARTS = {
    "indicator": indicator,
    "(|R|, min, max)": lambda S: (len(S), min(S), max(S)),
    "(|R|, sum)": lambda S: (len(S), sum(S)),
    "(min, max)": lambda S: (min(S), max(S)),
}
FAITHFUL = ("indicator", "(|R|, sum)")


# ---------------------------------------------------------------------------

def rindex(inv=None, chart="indicator"):
    """The refusal index over an inventory, on the named chart."""
    inv = mi.inventory() if inv is None else inv
    f = CHARTS[chart]
    return frozenset(f(refusal.refusal_set(X)) for X in inv.values())


def step(R, chart="indicator"):
    """F(R) -- rebuild the refusal index over an inventory containing R."""
    inv = dict(mi.inventory())
    inv["THE REFUSAL INDEX"] = R
    return rindex(inv, chart)


def orbit(chart="indicator", steps=MAX_STEPS):
    """[R0, F(R0), F(F(R0)), ...] -- the iteration, as a list."""
    seq = [rindex(None, chart)]
    for _ in range(steps):
        seq.append(step(seq[-1], chart))
    return seq


def convergence(chart="indicator", steps=MAX_STEPS):
    """(period, step it is entered at, the repeating states).

    period 1 is a FIXED POINT: F(R) = R.  Any period above 1 is a cycle and
    means no R survives its own seating on that chart.
    """
    seq = orbit(chart, steps)
    for i, a in enumerate(seq):
        for j in range(i):
            if seq[j] == a:
                return i - j, j, seq[j:i]
    return None, None, []


def faithful(chart):
    """True iff the chart keeps the nine seated indexes on nine cells."""
    return len(rindex(None, chart)) == len(mi.inventory())


def survey():
    """[(chart, cells, faithful, K, period, entered, is a fixed point)]."""
    out = []
    for name in CHARTS:
        R = rindex(None, name)
        per, ent, _cyc = convergence(name)
        out.append((name, len(R), faithful(name), mi.K(R), per, ent, per == 1))
    return out


def the_cycle(chart="indicator"):
    """(A, B, cells differing, the coordinate that flickers) for a 2-cycle."""
    per, _ent, cyc = convergence(chart)
    if per != 2:
        return None
    A, B = cyc
    dA, dB = sorted(A - B), sorted(B - A)
    flick = [i for i in range(len(dA[0]))
             if dA[0][i] != dB[0][i]] if len(dA) == len(dB) == 1 else []
    return A, B, (dA, dB), flick


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("THE REFUSAL INDEX -- seated as an object, and the fixed point settled")
    print("=" * 74)
    print()
    print("0. refusal.py SECTION 5 LEFT THIS OPEN: 'Whether the iteration")
    print("   converges is open here and is the first thing to settle next.'")
    print("   It is settled below, and the refusal it justified SURVIVES.")
    print()

    R0 = rindex()
    print("1. R0 -- the refusal index over the nine, before any seating.")
    print("   %d cells   K%d   closes %s   cell %s"
          % (len(R0), mi.K(R0), ", ".join(closers(R0)) or "NOTHING",
             (mi.cell(R0),)))
    print("   the nine refusal sets are pairwise distinct, so the indicator")
    print("   chart is FAITHFUL: nine indexes, nine cells, nothing lost.")
    print()

    print("2. THE ITERATION. F(R) = the refusal index rebuilt over an")
    print("   inventory that already contains R. A fixed point is F(R) = R.")
    print("   %-18s %5s %9s %4s %7s  %s"
          % ("chart", "cells", "faithful", "K", "period", "verdict"))
    for nm, n, f, k, per, ent, fp in survey():
        print("   %-18s %5d %9s  K%-2d %4d@%-2d  %s"
              % (nm, n, "yes" if f else "no", k, per, ent,
                 "FIXED POINT" if fp else "CYCLES, no fixed point"))
    print()
    print("   TWO FAITHFUL CHARTS AND THEY DISAGREE: the indicator cycles,")
    print("   (|R|, sum) is a fixed point from the first step. So the question")
    print("   HAS NO CHART-INDEPENDENT ANSWER -- the same shape as DOCKET 3.")
    print()

    c = the_cycle("indicator")
    if c:
        A, B, (dA, dB), flick = c
        print("3. AND THE CYCLE IS ONE BIT WIDE.")
        print("   the two states differ in exactly %d cell each way" % len(dA))
        print("     A has %s" % (dA[0],))
        print("     B has %s" % (dB[0],))
        print("   and those differ in coordinate(s) %s -- the K%s bit."
              % (flick, ", K".join(map(str, flick))))
        print("   Seating R makes K5 occur; recomputing with K5 present makes")
        print("   it stop. K5 is one of the three channels charts3.py proved")
        print("   unreachable from the element address. It is not reached here")
        print("   either -- IT FLICKERS.")
    print()
    print("4. SO THE REFUSAL IS UPHELD. On the faithful, obvious chart there is")
    print("   NO R that survives its own seating. Seating it would mean")
    print("   choosing the chart that happens to converge, which is choosing")
    print("   the answer. NOTHING IS ADDED TO mi.inventory().")
    return 0


# ---------------------------------------------------------------------------

def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("rindex selftest")
    R0 = rindex()

    # ---- R0 as an object
    chk("nine indexes, nine refusal cells -- the indicator loses nothing",
        (len(mi.inventory()), len(R0)), (9, 9))
    chk("and the indicator chart is therefore FAITHFUL", faithful("indicator"),
        True)
    chk("R0 closes NOTHING", closers(R0), [])
    chk("which is K0", mi.K(R0), 0)
    chk("its cell on the admissible chart", mi.cell(R0), (0, 5, 4))

    # ---- THE HEADLINE. refusal.py's open question, answered.
    per, ent, _c = convergence("indicator")
    chk("ON THE FAITHFUL CHART THE ITERATION DOES NOT CONVERGE", per != 1, True)
    chk("it enters a 2-cycle at step 2", (per, ent), (2, 2))

    # ---- and it is chart-dependent, which is the real finding
    sv = {r[0]: r for r in survey()}
    chk("(|R|, sum) is ALSO faithful", sv["(|R|, sum)"][2], True)
    chk("and it IS a fixed point, immediately", (sv["(|R|, sum)"][4],
                                                 sv["(|R|, sum)"][5]), (1, 0))
    # TWO FAITHFUL CHARTS, OPPOSITE ANSWERS. The whole point.
    chk("SO TWO FAITHFUL CHARTS DISAGREE ABOUT CONVERGENCE",
        sorted((n, fp) for n, _c, f, _k, _p, _e, fp in survey() if f),
        [("(|R|, sum)", True), ("indicator", False)])
    chk("the two coarsenings split the same way",
        sorted((n, fp) for n, _c, f, _k, _p, _e, fp in survey() if not f),
        [("(min, max)", True), ("(|R|, min, max)", False)])

    # ---- the cycle, and its width
    A, B, (dA, dB), flick = the_cycle("indicator")
    chk("the cycle's two states differ in ONE cell each way",
        (len(dA), len(dB)), (1, 1))
    chk("and those two cells differ in ONE coordinate", len(flick), 1)
    chk("which is the K5 bit", flick, [5])
    chk("A carries K0, K1, K3, K5, K7",
        [i for i, b in enumerate(dA[0]) if b], [0, 1, 3, 5, 7])
    chk("B carries the same without K5",
        [i for i, b in enumerate(dB[0]) if b], [0, 1, 3, 7])
    # K5 IS ONE OF THE THREE charts3 PROVED UNREACHABLE. Re-read, not recalled.
    import charts3
    chk("and K5 is unreachable from the element address",
        5 in charts3.census()["all"], False)

    # ---- nothing is seated
    chk("mi.inventory() is untouched -- nine members, no refusal index",
        len(mi.inventory()), 9)
    chk("and R0 is not among them",
        any(frozenset(v) == R0 for v in mi.inventory().values()), False)

    print("rindex selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
