#!/usr/bin/env python3
r"""
inversion.py -- THE INVERSION INDEX: the twenty places where the fill order and
the shell order disagree, as an index in their own right.

M: "I wonder if any missing vertex might contain an inversion index."

    python3 inversion.py             the reading
    python3 inversion.py --selftest  fixtures

===============================================================================
0. BUILT BEFORE THE DEMAND TABLE WAS READ, AND THAT IS DELIBERATE
===============================================================================

`demand.py` prints ten cells the octad is missing.  An index built to land on one
of them would be fitted, and a fitted vertex closes nothing.  This index is built
from the corpus's own disagreement, its coordinates are put through the DOCKET 3
criterion on their own merits, and WHERE IT LANDS IS REPORTED IN SECTION 5
WHETHER OR NOT IT IS WANTED.

===============================================================================
1. THE OBJECT EXISTS AND IT IS NOT A CONSTRUCTION
===============================================================================

`fibred.py` charts the differentiating electron by shell, `madelung.py` by fill
order.  Those are two total orders on the SAME twenty-five subshells, and they
disagree.  The disagreements are the members here.

    Madelung order      sort by (n+l, n)      -- which subshell fills next
    shell order         sort by (n, l)        -- which subshell is further out

    4s fills before 3d: (4,0) has n+l = 4, (3,2) has n+l = 5.  But 3d is the
    inner subshell.  THAT PAIR IS AN INVERSION, and it is the reason the
    transition metals exist.

An inversion is an unordered pair of subshells the two orders rank oppositely.
Over the seated reach of 170 elements there are twenty-five subshells and

    TWENTY INVERSIONS.  Not a sample, not a choice -- every pair, checked.

    EVERY INVERSION CROSSES A SHELL BOUNDARY, and that is forced rather than
    observed.  If two subshells share n, then the shell order ranks them by l and
    the Madelung order ranks them by n+l, which at equal n is also l.  The two
    agree.  So an inversion needs n1 != n2, and `crossing_is_forced()` proves it
    by exhausting the pairs rather than quoting the argument.

===============================================================================
2. THE THREE COORDINATES
===============================================================================

For an inversion {a, b} with a the one that FILLS FIRST (Madelung-earlier) and b
the one that lies FURTHER IN (shell-earlier):

        depth   a.n - b.n, how many shells the inversion reaches across.
                Positive by section 1, and 1, 2 or 3 here.
        span    how far apart the two are in the Madelung sequence.
        reach   how far apart they are in the shell sequence.

    ALL THREE ARE READ OFF THE TWO ORDERS AND NOTHING ELSE.  No capacity, no
    occupancy, no atomic number: an inversion is a fact about two orderings, and
    its coordinates are distances in those orderings.

===============================================================================
3. THE CHART CRITERION, MEASURED NOT ASSUMED
===============================================================================

DOCKET 3: a coordinate is admissible iff appending a monotone redundant
coordinate to the index does not move it.  `criterion()` runs that test on this
index and prints the count; the reading in section 5 is void if any coordinate
moves.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

To call an inversion an anomaly.  The Madelung order is the empirical one and the
shell order is the hydrogenic one; neither is the correction of the other, and
the corpus rules on neither.  `depth` is written a.n - b.n because a is the
Madelung-earlier member, which is a labelling convention and is stated as one.

To extend past the seated reach.  Twenty-five subshells is what 170 elements
give; `reach_control()` measures the inversion count at shorter reaches so the
dependence is visible rather than hidden.

To read the count as a physical constant.  Twenty is a fact about a reach.
"""

import itertools
import sys

import fibred
import hlaw
import mi

REACH = fibred.REACH                        # 170


def subshells(reach=REACH):
    """The (n, l) subshells the differentiating electron visits, sorted by n,l."""
    return sorted({(n, l) for n, l, _k in fibred.addresses(reach).values()})


def orders(reach=REACH):
    """({s: madelung rank}, {s: shell rank}) over the subshells."""
    subs = subshells(reach)
    mad = sorted(subs, key=lambda t: (t[0] + t[1], t[0]))
    sh = sorted(subs, key=lambda t: (t[0], t[1]))
    return {s: i for i, s in enumerate(mad)}, {s: i for i, s in enumerate(sh)}


def inversions(reach=REACH):
    """[(a, b)] with a Madelung-earlier and b shell-earlier.  Every pair checked."""
    pm, ps = orders(reach)
    out = []
    for x, y in itertools.combinations(subshells(reach), 2):
        if (pm[x] - pm[y]) * (ps[x] - ps[y]) < 0:
            a, b = (x, y) if pm[x] < pm[y] else (y, x)
            out.append((a, b))
    return sorted(out)


def coords(a, b, reach=REACH):
    """(depth, span, reach) for the inversion {a, b}."""
    pm, ps = orders(reach)
    return (a[0] - b[0], abs(pm[a] - pm[b]), abs(ps[a] - ps[b]))


def index(reach=REACH):
    """The inversion index as a set of cells."""
    return frozenset(coords(a, b, reach) for a, b in inversions(reach))


def table(reach=REACH):
    """[(a, b, coords)] -- every inversion with its cell."""
    return [(a, b, coords(a, b, reach)) for a, b in inversions(reach)]


# ---------------------------------------------------------------------------
# the things that have to be checked rather than asserted
# ---------------------------------------------------------------------------

def crossing_is_forced(reach=REACH):
    """(pairs sharing n, how many of them invert) -- must be (some, 0).

    At equal n the Madelung key (n+l, n) and the shell key (n, l) both reduce to
    l, so the orders agree.  Exhausted rather than argued.
    """
    pm, ps = orders(reach)
    same = [(x, y) for x, y in itertools.combinations(subshells(reach), 2)
            if x[0] == y[0]]
    bad = [(x, y) for x, y in same if (pm[x] - pm[y]) * (ps[x] - ps[y]) < 0]
    return len(same), len(bad)


def depths(reach=REACH):
    """{depth: count} -- how far the inversions reach."""
    out = {}
    for _a, _b, (d, _s, _r) in table(reach):
        out[d] = out.get(d, 0) + 1
    return dict(sorted(out.items()))


def collisions(reach=REACH):
    """(inversions, distinct cells) -- how much the chart forgets."""
    return len(inversions(reach)), len(index(reach))


def criterion(reach=REACH):
    """{coordinate: how many of the three move under a monotone redundant append}.

    DOCKET 3.  Append g(x) = x_0 to every member and recompute the coordinate of
    the index; an admissible coordinate does not move.
    """
    X = index(reach)
    lifted = frozenset(t + (t[0],) for t in X)
    got = {}
    for nm, f in (("height", mi.height), ("width", mi.width),
                  ("K", lambda S: mi.K(S))):
        got[nm] = 0 if f(X) == f(lifted) else 1
    return got


def reach_control(reaches=None):
    """[(reach, subshells, inversions, cells, K)] -- the reach dependence, shown."""
    out = []
    for r in (reaches or (10, 18, 36, 54, 86, 118, 170)):
        subs = subshells(r)
        X = index(r)
        # A reach with no inversion has an EMPTY index, and an empty index has
        # no channel -- hlaw's operators need a member to read the arity off.
        # That is a real row, not one to drop: it says where the object begins.
        out.append((r, len(subs), len(inversions(r)), len(X),
                    mi.K(X) if X else None))
    return out


def closers(reach=REACH):
    X = index(reach)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(reach=REACH):
    return mi.cell(index(reach))


# ---------------------------------------------------------------------------

def report():
    X = index()
    inv = inversions()
    print("=" * 74)
    print("THE INVERSION INDEX -- where the fill order and the shell order")
    print("disagree, as an index")
    print("=" * 74)
    print()
    print("1. THE MEMBERS.")
    print("   subshells in the seated reach   %d" % len(subshells()))
    print("   pairs                           %d"
          % (len(subshells()) * (len(subshells()) - 1) // 2))
    print("   INVERSIONS                      %d" % len(inv))
    same, bad = crossing_is_forced()
    print("   pairs sharing a shell           %d, of which inverting %d"
          % (same, bad))
    print("   -- so every inversion crosses a shell, and it is forced, not luck.")
    print()
    print("2. THE FIRST SIX, AND THE FIRST IS WHY TRANSITION METALS EXIST.")
    print("   %-10s %-10s %-6s %-6s %s" % ("fills 1st", "inner", "depth", "span",
                                           "reach"))
    for a, b, (d, s, r) in table()[:6]:
        print("   %-10s %-10s %-6d %-6d %d" % (str(a), str(b), d, s, r))
    print()
    print("3. HOW FAR THEY REACH.")
    for d, c in depths().items():
        print("   depth %d shells   %2d inversions" % (d, c))
    n, k = collisions()
    print("   %d inversions on %d distinct cells -- %d collide." % (n, k, n - k))
    print()
    print("4. THE CHART CRITERION (DOCKET 3).")
    crit = criterion()
    for nm, moved in sorted(crit.items()):
        print("   %-8s moves on %d   %s"
              % (nm, moved, "ADMISSIBLE" if not moved else "DISQUALIFIED"))
    if any(crit.values()):
        print("   A COORDINATE MOVED. The reading below is void.")
        return 1
    print()
    print("5. WHERE IT LANDS -- measured, and reported whichever way it goes.")
    print("   closes in   %s" % (", ".join(closers()) or "nothing"))
    print("   CELL        %s" % (cell(),))
    try:
        import demand
        d = demand.demand(__import__("hexad").figure())
        if cell() in d:
            print("   AND THAT CELL IS ONE THE OCTAD DEMANDS.  E drops by one.")
        else:
            print("   THAT CELL IS NOT DEMANDED BY THE OCTAD.  Seating it raises E;")
            print("   demand.py measures by how much.  Reported, not hidden.")
    except Exception as exc:                       # pragma: no cover
        print("   (demand.py not consulted: %s)" % exc)
    print()
    print("6. THE REACH DEPENDENCE, SHOWN RATHER THAN HIDDEN.")
    print("   %-8s %-11s %-12s %-7s %s"
          % ("reach", "subshells", "inversions", "cells", "K"))
    for r, sn, i, c, k in reach_control():
        print("   %-8d %-11d %-12d %-7d %s"
              % (r, sn, i, c, "-- no index yet" if k is None else k))
    print()
    print("7. REFUSED: to call an inversion an anomaly -- neither order is the")
    print("   correction of the other, and the corpus rules on neither. To read")
    print("   twenty as a constant: it is a fact about a reach, and the table")
    print("   above is why that is said out loud.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("subshells in the reach", len(subshells()), 25)
    chk("inversions", len(inversions()), 20)
    same, bad = crossing_is_forced()
    chk("no pair sharing a shell inverts", bad, 0)
    chk("and there are such pairs to check", same > 0, True)
    chk("every inversion has positive depth",
        all(d > 0 for _a, _b, (d, _s, _r) in table()), True)
    chk("3d/4s is an inversion", ((3, 2), (4, 0)) in
        [(b, a) for a, b in inversions()] + list(inversions()), True)
    chk("4s fills first, 3d is inner", ((4, 0), (3, 2)) in inversions(), True)
    chk("6s fills before 4f, and 4f is inner",
        ((6, 0), (4, 3)) in inversions(), True)
    chk("depth distribution", depths(), {1: 14, 2: 5, 3: 1})
    chk("depths sum to the inversion count", sum(depths().values()), 20)
    chk("max depth is three shells", max(depths()), 3)
    n, k = collisions()
    chk("inversions", n, 20)
    chk("distinct cells", k, len(index()))
    chk("the chart forgets some", n > k, True)
    crit = criterion()
    chk("height admissible", crit["height"], 0)
    chk("width admissible", crit["width"], 0)
    chk("K admissible", crit["K"], 0)
    chk("K is a lawful channel", 0 <= mi.K(index()) <= 7, True)
    chk("the cell is a 3-tuple", len(cell()), 3)
    chk("height and width bound the size",
        max(cell()[1], cell()[2]) <= len(index()) <= cell()[1] * cell()[2], True)
    rc = reach_control()
    chk("the reach control has rows", len(rc) >= 4, True)
    chk("inversions are monotone in reach",
        all(rc[i][2] <= rc[i + 1][2] for i in range(len(rc) - 1)), True)
    chk("the object begins somewhere -- some reach has no index",
        any(k is None for *_r, k in rc), True)
    chk("no inversion below neon", inversions(10), [])
    print("inversion selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
