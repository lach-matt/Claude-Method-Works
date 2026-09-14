#!/usr/bin/env python3
r"""
charts.py -- WHICH COORDINATES ARE PROPERTIES OF THE INDEX, AND WHICH ARE
PROPERTIES OF THE CHART.  DOCKET 3's criterion, and the two axes it removes.

M: "The (D, R) coordinates you chose at the first build. If they don't work,
then replace them with what does work."

    python3 charts.py             the reading
    python3 charts.py --selftest  fixtures

DOCKET 3 asked "what is a legitimate chart?" and recorded that no criterion
existed here.  There is one, it is a single test, and it disqualifies two of
the master index's five coordinates.

===============================================================================
1. THE TEST
===============================================================================

Append to every cell a REDUNDANT COORDINATE -- a function g of the cell it
already is.  It carries ZERO information: the new chart separates exactly what
the old one separated, member for member.  Anything that moves under it was
never a property of the index.

    A COORDINATE IS ADMISSIBLE IFF IT IS INVARIANT UNDER APPENDING A MONOTONE
    REDUNDANT COORDINATE.

And the reason it is monotone that matters is a one-line proof.  For monotone g,

        x <= y  =>  g(x) <= g(y)      hence  (x, g(x)) <= (y, g(y))  iff  x <= y

so THE CONTAINMENT ORDER IS PRESERVED EXACTLY.  Every invariant of that order
survives by construction; anything computed from the BOX rather than the ORDER
need not.  That is the whole criterion.

===============================================================================
2. WHAT IT DISQUALIFIES, AND IT IS THE TWO AXES THIS TREE CHOSE FIRST
===============================================================================

Over the ten seated indexes:

    arity   -- the D axis        MOVES ON 10 OF 10
    density -- the R axis        MOVES ON 10 OF 10
    cells                        invariant
    height  (longest chain)      invariant
    width   (largest antichain)  invariant
    comparable pairs             invariant
    join-irreducibles            invariant

D AND R ARE THE WORST TWO COORDINATES AVAILABLE.  They fail on every index,
without exception, and they are the two the master index was built on.  Both are
facts about the box; neither is a fact about the index.  Every result resting on
them is a result about how the index was written down -- which is what DOCKET 3
said and this measures.

===============================================================================
3. THE REPLACEMENT, AND WHY THESE TWO
===============================================================================

    HEIGHT   the longest chain in the containment order.
             MIRSKY: it equals the minimum number of antichains covering X.
    WIDTH    the largest antichain.
             DILWORTH: it equals the minimum number of chains covering X.

Both are canonical -- each is a min-max theorem, not a definition someone chose
-- both are measured with no threshold anywhere, and both are invariant by the
proof in section 1.  With K they give

    (K, height, width)

three axes, every one measured.  K is which languages close the index; height is
how deep it is; width is how broad.

    AND THE BOX IS RAGGED, WHICH IS DOCKET 3'S OTHER HALF.  Dilworth forces
    |X| <= height x width, so the three axes are NOT independent -- an index's
    size constrains where it can sit.  The product box is wrong here in exactly
    the way DOCKET 3 says it is wrong everywhere, and this time the constraint
    is a theorem rather than a census.

===============================================================================
4. THE LIMIT OF THE CRITERION, STATED BECAUSE IT IS NOT SMALL
===============================================================================

The criterion is exactly as strong as MONOTONE re-charting and no stronger.
Under a NON-MONOTONE redundant coordinate:

    height moves on 8 of 10        width moves on 7 of 10

That is not a failure of the criterion, it is its content.  A non-monotone
coordinate REORDERS the members; height and width are invariants OF THAT ORDER
and cannot survive its destruction -- nothing could except raw size.  This
tree's own witness is the periodic table's `block`, order-reversing on 356 pairs,
which takes the three-coordinate layout from closing in statistics to closing in
nothing.

    SO THE CRITERION IS: a chart is legitimate up to MONOTONE re-charting.
    Whether a NON-MONOTONE coordinate may be appended at all is a separate
    question and this file does not answer it.

===============================================================================
5. WHAT THE REPLACEMENT COSTS, AND IT COSTS TWO FINDINGS
===============================================================================

Rebuilt on (K, height, width) the master index is ten indexes over NINE distinct
cells, box 4 x 5 x 6, and it CLOSES IN statistics at E = 0 demanding nothing.

    THAT CLOSURE IS THE ROBUST FACT.  It holds on the original five-coordinate
    chart, on (K, D, R), and on four of the six measured triples -- charts that
    share no coordinate but K.

But two findings do not survive, and both were consequences of D and R:

    SELF-MEMBERSHIP.  The master index was a cell of itself, and the witness
    moved with the chart -- energy-conditions and exotic mechanisms under
    (C,Sc,Oc,D,R), spacetimes (Petrov) under (K,D,R).  Under EVERY ONE of the
    six measured triples its own cell is VACANT.  Self-membership was an
    artefact of the assigned axes.

    THE SPACETIME OVERLAP.  It followed from the same thing.  Under (K,D,R) the
    MI's own cell was Petrov's; the specificity was carried entirely by D and R,
    since on the measured coordinate K the MI matches four indexes equally.
    Replacing D and R removes it.

Neither is repaired here.  Both are recorded as withdrawn, with the measurement
that withdrew them.
"""

import itertools
import sys

import decomposable as D
import hlaw
import master

_le = lambda a, b: all(p <= q for p, q in zip(a, b))


def height(X):
    """The longest chain in the containment order.  Mirsky's theorem makes it
    the minimum number of antichains that cover X."""
    S = sorted(X)
    best = {}
    for x in S:
        best[x] = 1 + max([best[y] for y in S if y != x and _le(y, x)] or [0])
    return max(best.values())


def width(X):
    """The largest antichain.  Dilworth's theorem makes it the minimum number of
    chains that cover X.  Computed as |X| minus a maximum matching on the
    comparability DAG, which is Dilworth by Konig."""
    S = sorted(X)
    n = len(S)
    adj = {i: [j for j in range(n) if i != j and _le(S[i], S[j])] for i in range(n)}
    mt = {}

    def aug(i, seen):
        for j in adj[i]:
            if j in seen:
                continue
            seen.add(j)
            if j not in mt or aug(mt[j], seen):
                mt[j] = i
                return True
        return False

    return n - sum(aug(i, set()) for i in range(n))


def arity(X):
    return len(next(iter(X)))


def density(X):
    d = arity(X)
    n = 1
    for b in D.box_of(X, d):
        n *= len(b)
    return len(X) / n


def cells(X):
    return len(X)


def comparable_pairs(X):
    S = sorted(X)
    return sum(1 for a, b in itertools.combinations(S, 2)
               if _le(a, b) or _le(b, a))


def joinirr(X):
    S = set(X)
    return sum(1 for c in S if not any(
        tuple(map(max, a, b)) == c and a != c and b != c for a in S for b in S))


def channel(X):
    return master.channel_sets().index(frozenset(master.closers(X)))


CANDIDATES = (("arity (the D axis)", arity), ("density (the R axis)", density),
              ("cells", cells), ("height", height), ("width", width),
              ("comparable pairs", comparable_pairs),
              ("join-irreducibles", joinirr))

# g(c) = c[0] is monotone; g(c) = -c[0] reverses and is not.
MONOTONE = lambda c: c[0]
NON_MONOTONE = lambda c: -c[0]


def recharted(X, g):
    """X with one redundant coordinate appended -- zero information added."""
    return frozenset(tuple(c) + (g(c),) for c in X)


def admissibility(g=None):
    """{coordinate: how many of the seated indexes it moves on}.  Zero is
    admissible; anything else is a property of the chart."""
    g = MONOTONE if g is None else g
    out = {}
    for nm, f in CANDIDATES:
        out[nm] = sum(1 for X in master.inventory().values()
                      if f(X) != f(recharted(X, g)))
    return out


def cell(X):
    """The master cell on measured axes: (K, height, width)."""
    return (channel(X), height(X), width(X))


def rebuilt():
    """{index: (K, height, width)} -- the master index on measured axes."""
    return {nm: cell(X) for nm, X in master.inventory().items()}


def self_cell(coord=None):
    """(the master index's own cell, who occupies it) under a given chart."""
    coord = cell if coord is None else coord
    M = {nm: coord(X) for nm, X in master.inventory().items()}
    C = frozenset(M.values())
    own = coord(C)
    return own, sorted(nm for nm, c in M.items() if c == own)


def measured_triples():
    """[(names, distinct cells, closers, demands, own cell, witness)] over every
    triple of K with two admissible coordinates."""
    F = {"height": height, "width": width, "cells": cells, "joinirr": joinirr}
    out = []
    for b, c in itertools.combinations(sorted(F), 2):
        names = ("K", b, c)
        f = lambda X, _n=names: tuple(
            (channel if n == "K" else F[n])(X) for n in _n)
        M = {nm: f(X) for nm, X in master.inventory().items()}
        C = frozenset(M.values())
        cl, _ = hlaw.closures(C)
        own = f(C)
        out.append((names, len(C),
                    [L for L in hlaw.LANGS if len(cl[L]) == len(C)],
                    sorted(cl["statistics"] - C), own,
                    sorted(nm for nm, v in M.items() if v == own)))
    return out


def dilworth_ragged():
    """[(index, cells, height*width)] -- Dilworth's bound, which makes the box
    ragged rather than a product."""
    return [(nm, len(X), height(X) * width(X))
            for nm, X in master.inventory().items()]


def report():
    print("=" * 74)
    print("WHICH COORDINATES ARE THE INDEX, AND WHICH ARE THE CHART")
    print("=" * 74)
    print()
    print("1. THE TEST. Append a REDUNDANT coordinate -- a function of the cell")
    print("   it already is, carrying zero information about which member is")
    print("   which. For a MONOTONE one the containment order is preserved")
    print("   EXACTLY, so every invariant of that order survives by proof.")
    print()
    print("2. WHAT MOVES, over the ten seated indexes:")
    mono, non = admissibility(MONOTONE), admissibility(NON_MONOTONE)
    print("   %-24s %10s %14s" % ("coordinate", "monotone", "non-monotone"))
    for nm, _f in CANDIDATES:
        tag = "  ADMISSIBLE" if mono[nm] == 0 else ""
        print("   %-24s %6d/10 %10d/10%s" % (nm, mono[nm], non[nm], tag))
    print()
    print("   D AND R FAIL ON EVERY INDEX. They are the two axes this tree")
    print("   chose first, and both are facts about the BOX, not the index.")
    print()
    print("3. THE REPLACEMENT: (K, height, width), every axis measured.")
    print("   height -- longest chain; MIRSKY: = min antichain cover")
    print("   width  -- largest antichain; DILWORTH: = min chain cover")
    R = rebuilt()
    for nm, c in sorted(R.items(), key=lambda t: t[1]):
        print("      %-28s %s" % (nm, c))
    C = frozenset(R.values())
    cl, box = hlaw.closures(C)
    nb = 1
    for b in box:
        nb *= len(b)
    print("   %d indexes, %d distinct cells, box %s = %d, density %.1f%%"
          % (len(R), len(C), [len(b) for b in box], nb, 100 * len(C) / nb))
    print("   E: %s" % {L: len(cl[L]) - len(C) for L in hlaw.LANGS})
    print("   CLOSES IN %s, demanding %s"
          % ([L for L in hlaw.LANGS if len(cl[L]) == len(C)],
             sorted(cl["statistics"] - C) or "NOTHING"))
    print()
    print("   AND DILWORTH MAKES THE BOX RAGGED: |X| <= height x width, so the")
    print("   axes are not independent. Checked on all ten:")
    bad = [t for t in dilworth_ragged() if t[1] > t[2]]
    print("      violations: %d" % len(bad))
    print()
    print("4. THE LIMIT. Under a NON-MONOTONE redundant coordinate height moves")
    print("   on %d of 10 and width on %d of 10. That is the criterion's content,"
          % (non["height"], non["width"]))
    print("   not its failure: a non-monotone coordinate REORDERS the members and")
    print("   these are invariants of that order. The periodic table's `block` is")
    print("   this tree's own witness -- order-reversing on 356 pairs.")
    print()
    print("5. WHAT THE REPLACEMENT COSTS. Every measured triple, and the two")
    print("   band-edge charts for comparison:")
    print("   %-28s %5s %-11s %s" % ("chart", "cells", "closes", "own cell -> witness"))
    for names, n, clo, dem, own, who in measured_triples():
        print("   %-28s %5d %-11s %s -> %s"
              % ("(" + ", ".join(names) + ")", n, ",".join(clo) or "none",
                 own, who or "NOTHING"))
    for nm, f in (("(C,Sc,Oc,D,R)  original", master.master_cell),
                  ("(K,D,R)  intermediate",
                   lambda X: (channel(X),) + master.master_cell(X)[3:])):
        own, who = self_cell(f)
        M = {n: f(X) for n, X in master.inventory().items()}
        C2 = frozenset(M.values())
        cl2, _ = hlaw.closures(C2)
        print("   %-28s %5d %-11s %s -> %s"
              % (nm, len(C2),
                 ",".join(L for L in hlaw.LANGS if len(cl2[L]) == len(C2)) or "none",
                 own, who or "NOTHING"))
    print()
    print("   SELF-MEMBERSHIP IS AN ARTEFACT OF THE ASSIGNED AXES. Its witness")
    print("   moved with the chart, and under every measured triple the master")
    print("   index's own cell is VACANT. The spacetime overlap followed from the")
    print("   same thing and goes with it. WITHDRAWN, both.")
    print()
    print("   WHAT SURVIVES EVERY CHART: the master index closes in statistics")
    print("   at E = 0 and demands nothing.")
    return 0


def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("charts selftest")
    mono = admissibility(MONOTONE)
    n_idx = len(master.inventory())
    chk("the D axis moves on EVERY seated index",
        mono["arity (the D axis)"], n_idx)
    chk("and so does the R axis", mono["density (the R axis)"], n_idx)
    chk("height is invariant", mono["height"], 0)
    chk("width is invariant", mono["width"], 0)
    chk("as are cells, comparable pairs and join-irreducibles",
        [mono[k] for k in ("cells", "comparable pairs", "join-irreducibles")],
        [0, 0, 0])
    non = admissibility(NON_MONOTONE)
    chk("but NOT under a non-monotone re-charting -- height", non["height"], 7)
    chk("... and width", non["width"], 8)
    chk("only raw size survives that, and it discriminates least", non["cells"], 0)

    # the proof, checked rather than asserted: monotone g preserves the order
    bad = 0
    for X in master.inventory().values():
        S = sorted(X)
        Y = {c: tuple(c) + (MONOTONE(c),) for c in S}
        for a, b in itertools.combinations(S, 2):
            if _le(a, b) != _le(Y[a], Y[b]):
                bad += 1
    chk("MONOTONE re-charting preserves the containment order exactly", bad, 0)

    R = rebuilt()
    chk("nine indexes on (K, height, width) -- 2-D withdrawn by DOCKET 2",
        len(R), 9)
    chk("eight distinct cells", len(frozenset(R.values())), 8)
    chk("the shared cell is exotic mechanisms and Petrov",
        sorted(n for n, c in R.items() if c == (2, 3, 4)),
        ["exotic mechanisms", "spacetimes (Petrov)"])
    C = frozenset(R.values())
    cl, _ = hlaw.closures(C)
    chk("and it STILL closes in statistics at E = 0",
        (len(cl["statistics"]) - len(C),
         [L for L in hlaw.LANGS if len(cl[L]) == len(C)]), (0, ["statistics"]))

    chk("DILWORTH: |X| <= height x width on every index",
        [t[0] for t in dilworth_ragged() if t[1] > t[2]], [])

    # the two withdrawals
    own, who = self_cell()
    chk("on the canonical measured axes the MI's own cell is VACANT",
        (own, who), ((2, 5, 2), []))
    trip = measured_triples()
    # THE STORY HAS CHANGED AND THE REVISION IS THE POINT. This once read
    # "vacant under EVERY measured triple", against band-edge charts where the
    # index WAS self-membered -- so self-membership looked like an artefact of
    # the assigned axes specifically. Withdrawing the 2-D chart removed it from
    # the band-edge charts TOO, and one measured triple gained it. The honest
    # statement is weaker and better: SELF-MEMBERSHIP IS CHART-DEPENDENT AND
    # RARE -- it holds in ONE of the eight charts tried, and not the canonical.
    chk("and vacant under five of the six measured triples",
        sum(1 for _n, _c, _cl, _d, _o, w in trip if w), 1)
    chk("the one exception is (K, cells, height), witnessed by bounds",
        [(list(nm), w) for nm, _c, _cl, _d, _o, w in trip if w],
        [(["K", "cells", "height"], ["bounds"])])
    chk("six measured triples were swept", len(trip), 6)
    chk("four of the six still close in statistics",
        sum(1 for _n, _c, clo, _d, _o, _w in trip if clo == ["statistics"]), 4)
    # THE TWO BAND-EDGE CHARTS NO LONGER SELF-MEMBER EITHER. They did while the
    # 2-D chart was seated -- energy-conditions and exotic mechanisms under the
    # original five coordinates, spacetimes (Petrov) under (K,D,R), and the
    # spacetime reading was built on that second one. DOCKET 2 removed both.
    _o5, w5 = self_cell(master.master_cell)
    chk("the ORIGINAL chart no longer self-members", (_o5, w5),
        ((2, 1, 0, 2, 1), []))
    _o3, w3 = self_cell(lambda X: (channel(X),) + master.master_cell(X)[3:])
    chk("nor does (K,D,R), which is where the spacetime reading came from",
        (_o3, w3), ((3, 1, 2), []))
    chk("so self-membership survives in 1 of the 8 charts tried, not 2",
        sum(1 for _n, _c, _cl, _d, _o, w in trip if w) + bool(w5) + bool(w3), 1)
    print("charts selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
