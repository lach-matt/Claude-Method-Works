#!/usr/bin/env python3
r"""
occupy.py -- WHICH OF THE DEMANDED CELLS CAN BE FILLED, AND BY WHAT KIND OF
INDEX.  Eight of the ten are closed to second-order indexes by a counting
argument, one is occupied nine ways over, and one is open.

M: "I suggest there exists at least one more vertex index of measurable class and
value... Whatever the final shape and its vertexes are is the scope."

    python3 occupy.py             the reading
    python3 occupy.py --selftest  fixtures

===============================================================================
0. THE CENSUS IS NOT A FIT, AND THE ORDER OF EVENTS IS WHY
===============================================================================

`sources.py` fixed a family of second-order indexes BEFORE `demand.py` printed a
demand table: nine admissible measurements over the seated inventory, every
combination of two, three and four of them.  That family is a pool, not a search.
This file intersects the pool's cells with the demand and reports the overlap.

    NOTHING WAS BUILT TO LAND ON A CELL.  The pool predates the table, the
    inversion index and the probability index were built and measured before it
    was consulted, and both landed OUTSIDE it.  That is the control: a procedure
    that only ever produces hits is fitting, and this one produces misses.

===============================================================================
1. THE COUNTING ARGUMENT, AND IT CLOSES MOST OF THE TABLE
===============================================================================

    AN INDEX OF n MEMBERS HAS height <= n AND width <= n.

Trivially: a chain is a set of members and an antichain is a set of members.  So
a cell (K, h, w) requires at least max(h, w) members -- which `demand.size_band`
already prints as the low end of its band.  Turn it around:

    A SECOND-ORDER INDEX OVER THE N SEATED INDEXES HAS AT MOST N MEMBERS, so it
    can only occupy a cell with max(h, w) <= N.

At N = 10 seated vertices, a demanded cell with height or width above 10 is
UNREACHABLE by any second-order index over them -- not unbuilt, unreachable, and
no cleverness about which measurements to use can change it.  `unreachable()`
applies the test; `counting_bound_holds()` checks the premise over the seated
inventory rather than quoting it.

    THAT IS THE STRONGEST THING IN THIS FILE.  Eight of the ten demanded cells
    need 18 to 30 members.  They can only be FIRST-ORDER -- indexes whose members
    are things the corpus banks, not measurements of the indexes already seated.
    The programme's remaining work is therefore mostly a question about the
    corpus, not about this tree's own bookkeeping.

===============================================================================
2. WHAT THE POOL ACTUALLY OCCUPIES
===============================================================================

`occupation()` runs every combination at arity 2, 3 and 4 and records the cell.
The overlap with the demand is reported per arity, and the measurement
combinations that produce each hit are named, because a cell occupied by one
freak combination and a cell occupied by eight are different evidence.

===============================================================================
3. WHY NOTHING IS SEATED HERE
===============================================================================

A cell shown occupiable is not thereby a vertex.  `entropy.py` states the reason
and it binds here: the supply of second-order indexes is bounded only by the
supply of admissible measurements, which is not bounded at all, so seating one
because it lands where the figure wants a vertex would make the vertex count
arbitrary.  NINE different measurement combinations reach (2, 5, 4) -- eight at
arity 2 and 3, one more at arity 4, which is why the first count taken was eight
and the fixture corrected it -- and there is no principle in this tree that picks
one of them.

    SO THE FINDING IS RECORDED AND THE SEATING IS NOT DONE.  E stays at 10.  What
    changes is that one of the ten is now known to be SATISFIABLE and eight are
    known to be closed to an entire class of candidate.  DOCKET 12 asks whether a
    satisfiable cell should be seated and by what rule.
"""

import itertools
import sys

import demand
import hexad
import mi
import sources

ARITIES = (2, 3, 4)


def seated_count():
    """How many vertices the live figure has -- the second-order ceiling."""
    return len(hexad.cells())


def counting_bound_holds():
    """[(name, |X|, height, width)] with any violation of h, w <= |X| flagged.

    The premise of section 1, checked over every seated index rather than
    quoted.  A violation would be a bug in mi.height or mi.width.
    """
    out = []
    for nm, X in hexad.all_indexes().items():
        h, w = mi.height(X), mi.width(X)
        out.append((nm, len(X), h, w, h <= len(X) and w <= len(X)))
    return out


def unreachable(ceiling=None):
    """([cells no second-order index over the figure can occupy], [the rest]).

    The test is max(height, width) > ceiling, with ceiling the number of seated
    vertices.  Nothing about which measurements are available enters it.
    """
    ceiling = seated_count() if ceiling is None else ceiling
    D = demand.demand(hexad.figure())
    closed = [c for c in D if max(c[1], c[2]) > ceiling]
    return closed, [c for c in D if c not in closed]


def occupation(arities=ARITIES):
    """{arity: (indexes, {cell: [combos]})} over the whole pool."""
    inv = mi.inventory()
    M = sources.measurements()
    adm = sources.admissible()
    out = {}
    for a in arities:
        cells, n = {}, 0
        for combo in itertools.combinations(adm, a):
            P = frozenset(tuple(M[c](X) for c in combo) for X in inv.values())
            cells.setdefault(mi.cell(P), []).append(combo)
            n += 1
        out[a] = (n, cells)
    return out


def hits(arities=ARITIES):
    """{arity: {demanded cell: [combos reaching it]}} -- the overlap."""
    D = set(demand.demand(hexad.figure()))
    return {a: {c: v for c, v in cells.items() if c in D}
            for a, (_n, cells) in occupation(arities).items()}


def misses():
    """[(name, cell, in the demand?)] for the two built-and-measured indexes.

    The control on section 0: both were built before the demand table was read
    and both landed outside it.
    """
    D = set(demand.demand(hexad.figure()))
    C = hexad.cells()
    return [(nm, C[nm], C[nm] in D)
            for nm in ("inversion index", "probability index")]


def verdicts():
    """[(cell, verdict, evidence)] -- one row per demanded cell."""
    closed, open_ = unreachable()
    H = hits()
    out = []
    for c in demand.demand(hexad.figure()):
        if c in closed:
            out.append((c, "SECOND-ORDER CLOSED",
                        "needs %d members; only %d vertices exist"
                        % (max(c[1], c[2]), seated_count())))
        else:
            ways = sorted({tuple(k) for a in H for k in H[a].get(c, [])})
            out.append((c, "OCCUPIED" if ways else "OPEN",
                        "%d combinations reach it" % len(ways) if ways
                        else "reachable in principle, unoccupied by the pool"))
    return out


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("WHICH DEMANDED CELLS CAN BE FILLED, AND BY WHAT KIND OF INDEX")
    print("=" * 74)
    print()
    print("1. THE COUNTING BOUND, CHECKED NOT QUOTED.")
    bad = [r for r in counting_bound_holds() if not r[4]]
    for nm, n, h, w, ok in counting_bound_holds():
        print("   %-20s |X| %-6d height %-4d width %-4d %s"
              % (nm, n, h, w, "ok" if ok else "VIOLATION"))
    if bad:
        print("   THE PREMISE FAILS. Everything below is void.")
        return 1
    print("   -- so a cell needs max(height, width) members, and a second-order")
    print("      index over the %d seated vertices cannot have more than %d."
          % (seated_count(), seated_count()))
    print()

    print("2. THE TEN DEMANDED CELLS, ADJUDICATED.")
    print("   %-13s %-22s %s" % ("cell", "verdict", "evidence"))
    for c, v, e in verdicts():
        print("   %-13s %-22s %s" % (str(c), v, e))
    print()
    closed, open_ = unreachable()
    print("   %d of 10 are CLOSED to every second-order index over this figure."
          % len(closed))
    print("   They need 18 to 30 members and can only be FIRST-ORDER: indexes")
    print("   whose members are things the corpus banks. The remaining work is")
    print("   a question about the corpus, not about this tree's bookkeeping.")
    print()

    print("3. WHAT THE POOL OCCUPIES, BY ARITY.")
    H = hits()
    for a, (n, cells) in sorted(occupation().items()):
        h = H[a]
        print("   arity %d   %3d indexes   %2d distinct cells   %d demanded %s"
              % (a, n, len(cells), len(h),
                 sorted(h) if h else ""))
    print()
    combos = sorted({tuple(k) for a in H for k in H[a].get((2, 5, 4), [])})
    print("   (2, 5, 4) is reached by %d distinct measurement combinations:"
          % len(combos))
    for c in combos:
        print("       %s" % (", ".join(c),))
    print("   %d ways is evidence of a real cell, not of one freak chart." 
          % len(combos))
    print()

    print("4. THE CONTROL -- the two indexes built before this table was read.")
    for nm, c, hit in misses():
        print("   %-20s %-12s %s" % (nm, str(c),
                                     "IN the demand" if hit else "OUTSIDE it"))
    print("   A procedure that only ever produces hits is fitting. This one")
    print("   produced two misses first, and they are seated anyway.")
    print()

    print("5. NOTHING IS SEATED HERE, AND E STAYS AT %d."
          % demand.E(hexad.figure()))
    print("   A satisfiable cell is not a vertex. The supply of second-order")
    print("   indexes is unbounded, %d combinations reach (2,5,4), and this"
          % len(combos))
    print("   tree has no principle that picks one. DOCKET 12 asks for one.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the figure has ten vertices", seated_count(), 10)
    chk("the counting bound holds on every seated index",
        all(r[4] for r in counting_bound_holds()), True)
    closed, open_ = unreachable()
    chk("eight demanded cells are second-order closed", len(closed), 8)
    chk("two are reachable in principle", len(open_), 2)
    chk("(2,5,4) is reachable", (2, 5, 4) in open_, True)
    chk("(2,5,5) is reachable", (2, 5, 5) in open_, True)
    chk("(7,30,24) is closed", (7, 30, 24) in closed, True)
    chk("(0,18,24) is closed", (0, 18, 24) in closed, True)
    chk("every closed cell needs more than ten members",
        all(max(c[1], c[2]) > 10 for c in closed), True)
    chk("every reachable cell needs at most ten",
        all(max(c[1], c[2]) <= 10 for c in open_), True)
    H = hits()
    chk("arity 2 hits one cell", sorted(H[2]), [(2, 5, 4)])
    chk("arity 3 hits one cell", sorted(H[3]), [(2, 5, 4)])
    chk("arity 4 hits one cell", sorted(H[4]), [(2, 5, 4)])
    combos = sorted({tuple(k) for a in H for k in H[a].get((2, 5, 4), [])})
    chk("(2,5,4) is reached NINE ways -- eight at arity 2-3, one at arity 4",
        len(combos), 9)
    chk("and arity 4 is what makes it nine",
        len({tuple(k) for a in (2, 3) for k in H[a].get((2, 5, 4), [])}), 8)
    chk("('Hmin','comparable') is one of them",
        ("Hmin", "comparable") in combos, True)
    chk("(2,5,5) is NOT occupied by the pool",
        any((2, 5, 5) in H[a] for a in H), False)
    occ = occupation()
    chk("arity 3 has 84 indexes", occ[3][0], 84)
    chk("arity 3 has 21 distinct cells", len(occ[3][1]), 21)
    m = misses()
    chk("both controls were measured", len(m), 2)
    chk("the inversion index missed the demand", m[0][2], False)
    chk("the probability index missed the demand", m[1][2], False)
    v = verdicts()
    chk("one verdict per demanded cell", len(v), 10)
    chk("exactly one cell is OCCUPIED",
        sum(1 for _c, x, _e in v if x == "OCCUPIED"), 1)
    chk("exactly one cell is OPEN",
        sum(1 for _c, x, _e in v if x == "OPEN"), 1)
    chk("E is unchanged by this file", demand.E(hexad.figure()), 10)
    print("occupy selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
