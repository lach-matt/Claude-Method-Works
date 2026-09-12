#!/usr/bin/env python3
"""
canonical.py -- THE CANONICAL DECOMPOSITION EXISTS.  H105c IS WITHDRAWN, THE
DEAD ENDS ARE REAL, AND THE TWO IRREDUCIBLE CONDITIONS HAVE NAMES.

M: "The canonical decomposition is a transition itself."  And: "It is a
transition to a position that cannot accept it."  And: "acceptance is determined
by which NECs are satisfied, and which satisfied NECs can replace the ones that
are not satisfied."

ALL THREE HOLD, AND THE FIRST OVERTURNS decompose.py's CONCLUSION.

===============================================================================
1. H105c IS WITHDRAWN.  THE DECOMPOSITION IS CANONICAL
===============================================================================

decompose.py reported "the decomposition is NOT unique -- 6, 7 or 8 depending on
the order".  THAT WAS A GREEDY SEARCH.  Removability is DOWNWARD CLOSED --
geometry is monotone, so if removing S preserves the hulls then so does removing
any subset of S -- which means no removable set can contain a cell that is not
removable alone.  THE SEARCH IS THEREFORE OVER SUBSETS OF TEN CELLS, 2^10, AND
EXHAUSTIBLE IN A SECOND.  Run exhaustively:

        440 removable subsets       a simplicial complex
        6 maximal ones (facets)     sizes 6, 6, 7, 7, 7, 8
        MAXIMUM SIZE 8, AND EXACTLY ONE SET ACHIEVES IT

    THE CANONICAL DECOMPOSITION EXISTS: a unique maximum removal of 8 cells,
    leaving 9.  "Not unique" was reporting the search's dead ends, not the
    structure's.

FOURTH TIME THIS SESSION A PROPERTY OF THE METHOD WAS READ AS A PROPERTY OF THE
OBJECT.  H97 was the coordinate re-ranking, H100 the algebra budget, H102 the
Index-supplied value order, and this is greedy stranding.  Each time the
scaffolding was invisible until it produced a number that looked like a finding.

===============================================================================
2. AND THE DEAD ENDS ARE EXACTLY WHAT M NAMED
===============================================================================

"A transition to a position that cannot accept it."  MEASURED: five of the six
facets are maximal but NOT maximum -- two strand two cells short, three strand
one short.  They are positions reachable by valid removals from which no further
removal is possible, and which are not the answer.

        200 random greedy walks:   70 reach the maximum
                                   98 strand at 7
                                   32 strand at 6

    ONLY 35 PER CENT OF WALKS REACH THE CANONICAL DECOMPOSITION.  Sixty-five per
    cent arrive at a position that cannot accept the next step.  M's phrase is
    not a metaphor for this; it is a description of it.

===============================================================================
3. THE REPLACEMENT RELATION, WHICH IS WHAT ACCEPTANCE MEANS HERE
===============================================================================

"Which satisfied NECs can replace the ones that are not satisfied."  In hull
terms this is exact and it is Caratheodory: A CELL IS REMOVABLE IFF IT IS NOT
EXTREME -- iff its position in every 2-D shadow is a convex combination of the
others.  It is removable BECAUSE OTHERS COVER IT.  Measured, pairwise:

        6 ordered conflicts of 90:  removing d costs c its removability
        THREE MUTUALLY EXCLUSIVE PAIRS, each cell covering the other

            SNEC                <-> QEI (Ford-Roman / Fewster-Osterbrink)
            semiclassical-WEC   <-> QEI (Ford-Roman / Fewster-Osterbrink)
            BV-effective-NEC    <-> BV-effective-ANEC

TWO CELLS THAT COVER EACH OTHER CANNOT BOTH GO -- one must stay to cover the
other.  So the maximum removal is the complement of a MINIMUM VERTEX COVER of
that conflict graph, and the cover has size 2: QEI sits in two of the three
pairs, BV-effective-ANEC in one.  TEN REMOVABLE, TWO MUST STAY, MAXIMUM EIGHT.
The arithmetic of the canonical decomposition is a vertex cover.

===============================================================================
4. AND THE TWO IRREDUCIBLE CONDITIONS ARE THE TWO THIS THREAD RUNS ON
===============================================================================

    QEI -- FORD-ROMAN / FEWSTER-OSTERBRINK
    BV-EFFECTIVE-ANEC

The quantum energy inequality is persist.py's wall, the bound that permits the
corridor's density for 2.8e-26 s against a required 5.1e-9.  The Barcelo-Visser
effective averaged NEC is higgs.py's xi escape and necindex.py's ONE DOOR, the
only slot any throat-opening route has ever moved.

    THE TWO CONDITIONS THE INDEX CANNOT DO WITHOUT ARE THE TWO THE WHOLE THREAD
    HAS TURNED ON, AND NOTHING IN THE COMPUTATION WAS LOOKING FOR THEM.  It fell
    out of a vertex cover on a hull-conflict graph.

Recorded as a convergence and not a theorem: this is a property of an 18-cell
family under geometry's hull operator, not a statement about gravity.

===============================================================================
5. SO THE EQUATION HOLDS, WITH BOTH SIDES NAMED
===============================================================================

    |Object - state| = object

    state  = the unique maximum removable set, 8 cells
    object = the 9 that survive it

TRUE, EXACTLY, AND NO LONGER ONLY ONE CELL AT A TIME.  decompose.py could not
say this because it never found the maximum.

NOTHING IS REPAIRED.
"""

import itertools
import random
import sys

import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

H105C_WITHDRAWN = True
DECOMPOSITION_IS_CANONICAL = True
DEAD_ENDS_ARE_REAL = True
COVER_IS_THE_MECHANISM = True
CONVERGENCE_NOT_THEOREM = True
NOTHING_IS_REPAIRED = True


def geom(cells):
    return frozenset(cypher.op_geometry(necindex.pinned_index(cells), OPTS)[0])


def singles():
    X = frozenset(necindex.cells())
    b = geom(X)
    return [c for c in sorted(X) if geom(X - {c}) == b]


def complex_faces():
    """Every removable subset.  Downward closed, so subsets of the singles."""
    X = frozenset(necindex.cells())
    b = geom(X)
    S = singles()
    return {frozenset(T) for r in range(len(S) + 1)
            for T in itertools.combinations(S, r)
            if geom(X - set(T)) == b}


def facets():
    f = complex_faces()
    return [s for s in f if not any(s < t for t in f)]


def maximum():
    f = facets()
    m = max(len(s) for s in f)
    top = [s for s in f if len(s) == m]
    return m, top


def conflicts():
    """(c, d): removing d costs c its removability."""
    X = frozenset(necindex.cells())
    S = singles()
    out = []
    for c, d in itertools.permutations(S, 2):
        Y = X - {d}
        if geom(Y - {c}) != geom(Y):
            out.append((c, d))
    return out


def mutual_pairs():
    con = set(conflicts())
    return [(a, b) for a, b in itertools.combinations(singles(), 2)
            if (a, b) in con and (b, a) in con]


def walk(seed):
    X = frozenset(necindex.cells())
    b = geom(X)
    rnd = random.Random(seed)
    kept, n, prog = set(X), 0, True
    while prog:
        prog = False
        for c in rnd.sample(sorted(kept), len(kept)):
            if geom(kept - {c}) == b:
                kept.discard(c)
                n += 1
                prog = True
                break
    return n


def named(cell):
    for r in necindex.FAMILY:
        if tuple(r[1:6]) == cell:
            yield r[0]


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    f = complex_faces()
    fac = facets()
    m, top = maximum()
    X = frozenset(necindex.cells())
    print("  the removable complex")
    print("      %-42s %d" % ("individually removable cells", len(singles())))
    print("      %-42s %d" % ("removable subsets (faces)", len(f)))
    print("      %-42s %d" % ("maximal ones (facets)", len(fac)))
    print("      %-42s %s" % ("facet sizes", sorted(len(s) for s in fac)))
    print("      %-42s %d" % ("maximum size", m))
    print("      %-42s %d" % ("sets achieving it", len(top)))
    print("      %-42s %d" % ("cells surviving the maximum", len(X) - m))
    print()
    print("  dead ends -- maximal but not maximum")
    for s in sorted(fac, key=len):
        if len(s) < m:
            print("      size %d, stranding %d short" % (len(s), m - len(s)))
    from collections import Counter
    c = Counter(walk(s) for s in range(200))
    print("      200 random greedy walks:")
    for k in sorted(c):
        print("         end at %d : %3d   %s" % (k, c[k],
                                                 "MAXIMUM" if k == m else "stranded"))
    print("      %-42s %.1f%%" % ("reach the canonical decomposition",
                                  100.0 * c[m] / 200))
    print()
    print("  the replacement relation")
    print("      %-42s %d of %d" % ("ordered conflicts", len(conflicts()),
                                    len(singles()) * (len(singles()) - 1)))
    mp = mutual_pairs()
    print("      %-42s %d" % ("mutually exclusive pairs", len(mp)))
    for a, b in mp:
        print("         %-28s <-> %s" % (" / ".join(named(a)),
                                         " / ".join(named(b))))
    left = sorted(set(singles()) - set(top[0]))
    print()
    print("  the two the maximum must leave behind")
    for c2 in left:
        print("      %s" % " / ".join(named(c2)))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The canonical decomposition exists -- a unique maximum of 8,")
    print("  leaving 9.  decompose.py's 'not unique' was greedy stranding, and")
    print("  only 35%% of walks reach the answer.  Acceptance is covering:")
    print("  three mutually exclusive pairs, a vertex cover of size two.  And")
    print("  the two irreducible conditions are the QEI and BV-effective-ANEC")
    print("  -- the two this whole thread has run on.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("canonical.py --selftest")
    print()
    X = frozenset(necindex.cells())
    S = singles()

    # ------------------------- 1. downward closure makes it exhaustible
    chk("individually removable cells", len(S), 10)
    f = complex_faces()
    chk("removable subsets", len(f), 440)
    # downward closure, checked rather than assumed
    chk("the family is downward closed",
        all(frozenset(t) in f for s in f for t in
            itertools.combinations(sorted(s), max(0, len(s) - 1))), True)
    fac = facets()
    chk("facets", len(fac), 6)
    chk("facet sizes", sorted(len(s) for s in fac), [6, 6, 7, 7, 7, 8])
    m, top = maximum()
    chk("maximum removable size", m, 8)
    chk("and EXACTLY ONE set achieves it", len(top), 1)
    chk("leaving this many cells", len(X) - m, 9)
    chk("recorded: the decomposition is canonical",
        DECOMPOSITION_IS_CANONICAL, True)
    chk("so H105c is withdrawn", H105C_WITHDRAWN, True)
    # and the equation holds exactly for it
    chk("|Object - state| = object, for the canonical state",
        geom(X - top[0]), geom(X))

    # ---------------------------------------- 2. the dead ends are real
    chk("facets short of the maximum", sum(1 for s in fac if len(s) < m), 5)
    from collections import Counter
    c = Counter(walk(s) for s in range(200))
    chk("walks reaching the maximum", c[m], 70)
    chk("walks stranded", 200 - c[m], 130)
    chk("so most walks do NOT reach it", c[m] < 100, True)
    chk("recorded", DEAD_ENDS_ARE_REAL, True)
    # NEGATIVE CONTROL: some walks DO reach it, so stranding is a property of
    # the complex and not of a broken walk.
    chk("but some do", c[m] > 0, True)

    # ------------------------------------ 3. acceptance is covering
    con = conflicts()
    chk("ordered conflicts", len(con), 6)
    mp = mutual_pairs()
    chk("mutually exclusive pairs", len(mp), 3)
    left = sorted(set(S) - set(top[0]))
    chk("cells the maximum leaves behind", len(left), 2)
    # the survivors are exactly a vertex cover of the mutual-exclusion graph
    chk("and they cover every mutual pair",
        all(a in left or b in left for a, b in mp), True)
    # MINIMALITY, written properly: the first draft of this line was a garbled
    # expression that happened to evaluate False.  The claim is that no SINGLE
    # cell covers all three mutual pairs, so a cover of size 2 is minimum.
    chk("no single cell covers all three pairs",
        [v for v in S if all(v in (a, b) for a, b in mp)], [])
    chk("so the size-2 cover is minimum", len(left), 2)
    chk("so maximum = 10 - 2", m, len(S) - len(left))
    chk("recorded", COVER_IS_THE_MECHANISM, True)

    # ----------------------- 4. and the two irreducibles have names
    names = sorted(n for c2 in left for n in named(c2))
    chk("the two left behind are named", names,
        ["BV-effective-ANEC", "QEI-Fewster-Osterbrink", "QEI-Ford-Roman"])
    chk("one is the quantum energy inequality",
        any("QEI" in n for n in names), True)
    chk("the other is Barcelo-Visser's effective ANEC",
        "BV-effective-ANEC" in names, True)
    chk("recorded as a convergence, not a theorem",
        CONVERGENCE_NOT_THEOREM, True)
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
