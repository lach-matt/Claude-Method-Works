#!/usr/bin/env python3
r"""
filled.py -- THE FIRST DEMANDED CELL, OCCUPIED AND SEATED.  (2, 5, 4), nine
witnesses, and the choice between them is immaterial because they agree.

M, ruling DOCKET 12: "yes" -- a demanded cell that is satisfiable gets seated.

    python3 filled.py             the reading
    python3 filled.py --selftest  fixtures

===============================================================================
0. WHAT THE RULING SETTLED AND WHAT IT LEFT
===============================================================================

`occupy.py` found that `(2, 5, 4)` -- one of the ten cells the figure demands --
is occupied by a second-order index from `sources.py`'s pre-existing measurement
pool, and occupied NINE ways.  DOCKET 12 asked whether a satisfiable cell gets
seated and listed the objection: with nine witnesses there is no principle
picking one, so the vertex would be arbitrary.

    THE OBJECTION DISSOLVES ON MEASUREMENT, AND THAT IS THIS FILE'S ONE CLAIM.
    A vertex of the figure IS A CELL.  All nine witnesses give the SAME cell, so
    the figure does not depend on which is chosen -- `witnesses_agree()` checks
    every one of the nine and the figure is identical under each.  What is
    arbitrary is which index to name as the witness; what is seated is the cell,
    and the cell is unique.

    SO THE RULING IS EXECUTABLE.  `CANON` names the lexicographically first
    arity-2 witness for reproducibility, `CANON_IS_ARBITRARY = True` says so, and
    nothing downstream reads `CANON` except the report.

===============================================================================
1. WHAT SEATING IT COSTS
===============================================================================

By `demand.py`'s L2 -- seating a demanded cell drops E by exactly one and leaves
J(F) unchanged -- this takes the figure from ten vertices to eleven and

        E from 10 to 9

with the other nine demanded cells exactly as they were.  `effect()` measures it
rather than quoting the lemma.

===============================================================================
2. WHAT THIS FILE REFUSES
===============================================================================

To seat the other eight witnesses.  They are the same cell; seating them would
add nothing to the figure and would inflate the vertex count with duplicates.
They are listed in `WITNESSES` so the multiplicity is visible.

To claim the index is interesting in itself.  It is a re-chart of the seated nine
on three of `sources.py`'s admissible measurements, and `entropy.py`'s warning
stands: the second-order supply is unbounded.  What earns this one a seat is not
that it is a good index but that the figure demanded its cell and DOCKET 12 ruled
such a cell gets seated.

To generalise the ruling to `(2, 5, 5)`.  That cell is reachable in principle and
occupied by nothing in the pool.  A ruling that a satisfiable cell gets seated
says nothing about an unsatisfied one, and `occupy.py` keeps reporting it OPEN.
"""

import itertools
import sys

import hlaw
import mi
import sources

TARGET = (2, 5, 4)
CANON = ("Hmin", "comparable")
CANON_IS_ARBITRARY = True


def witnesses(arities=(2, 3, 4)):
    """[combo] -- every measurement combination whose index lands on TARGET."""
    inv = mi.inventory()
    M = sources.measurements()
    adm = sources.admissible()
    out = []
    for a in arities:
        for combo in itertools.combinations(adm, a):
            P = frozenset(tuple(M[c](X) for c in combo) for X in inv.values())
            if mi.cell(P) == TARGET:
                out.append(combo)
    return sorted(out)


def build(combo=CANON):
    """The index one witness gives."""
    inv = mi.inventory()
    M = sources.measurements()
    return frozenset(tuple(M[c](X) for c in combo) for X in inv.values())


def index():
    """The seated index at the demanded cell."""
    return build(CANON)


def witnesses_agree():
    """[(combo, cell, members)] -- every witness, and whether the cells match.

    The whole argument of section 0: if they all give TARGET, the vertex is
    well defined and the choice of CANON changes nothing.
    """
    return [(c, mi.cell(build(c)), len(build(c))) for c in witnesses()]


def effect():
    """(vertices before, E before, vertices after, E after) -- measured."""
    import demand
    import hexad
    F = hexad.figure()
    G = frozenset(F) | {TARGET}
    return len(F), demand.E(F), len(G), demand.E(G)


def demand_unchanged():
    """(the other demanded cells before, after) -- L2 says they do not move."""
    import demand
    import hexad
    F = hexad.figure()
    before = set(demand.demand(F)) - {TARGET}
    after = set(demand.demand(frozenset(F) | {TARGET}))
    return sorted(before), sorted(after)


def closers():
    X = index()
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def criterion():
    X = index()
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


# ---------------------------------------------------------------------------

def report():
    w = witnesses_agree()
    print("=" * 74)
    print("THE FIRST DEMANDED CELL, OCCUPIED AND SEATED")
    print("=" * 74)
    print()
    print("1. NINE WITNESSES, AND THEY AGREE.")
    print("   %-40s %-12s %s" % ("measurements", "cell", "members"))
    for combo, c, n in w:
        print("   %-40s %-12s %d" % (", ".join(combo), str(c), n))
    agree = len({c for _k, c, _n in w}) == 1
    print("   ALL NINE GIVE THE SAME CELL: %s" % agree)
    print("   A vertex IS a cell, so the figure does not depend on which is")
    print("   chosen. What is arbitrary is the name of the witness, and")
    print("   CANON_IS_ARBITRARY = %s says so." % CANON_IS_ARBITRARY)
    print()
    print("2. THE SEATED INDEX.")
    print("   witness     %s" % (", ".join(CANON),))
    print("   members     %d" % len(index()))
    print("   closes      %s" % (", ".join(closers()) or "nothing"))
    print("   CELL        %s" % (mi.cell(index()),))
    crit = criterion()
    print("   criterion   K %d  height %d  width %d   %s"
          % (crit["K"], crit["height"], crit["width"],
             "all admissible" if not any(crit.values()) else "A COORDINATE MOVED"))
    print()
    print("3. WHAT IT COSTS, MEASURED NOT QUOTED.")
    nb, eb, na, ea = effect()
    print("   vertices  %d -> %d" % (nb, na))
    print("   E         %d -> %d" % (eb, ea))
    before, after = demand_unchanged()
    print("   the other demanded cells are unchanged: %s" % (before == after))
    print("   %d cells still demanded." % len(after))
    print()
    print("4. REFUSED: to seat the other eight witnesses -- they are the same")
    print("   cell. To call the index interesting in itself: it is a re-chart of")
    print("   the seated nine, and the second-order supply is unbounded. To")
    print("   generalise to (2,5,5), which is reachable and occupied by nothing.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    w = witnesses()
    chk("nine witnesses", len(w), 9)
    chk("the canonical one is among them", CANON in w, True)
    chk("it is the lexicographically first at arity 2",
        sorted(c for c in w if len(c) == 2)[0], CANON)
    agreed = witnesses_agree()
    chk("every witness gives the TARGET cell",
        sorted({c for _k, c, _n in agreed}), [TARGET])
    chk("so the vertex is well defined", len({c for _k, c, _n in agreed}), 1)
    chk("the choice is flagged arbitrary", CANON_IS_ARBITRARY, True)
    chk("the seated index has nine members", len(index()), 9)
    chk("its cell is the target", mi.cell(index()), TARGET)
    chk("it closes statistics alone", closers(), ["statistics"])
    crit = criterion()
    chk("K admissible", crit["K"], 0)
    chk("height admissible", crit["height"], 0)
    chk("width admissible", crit["width"], 0)
    chk("height and width bound the size",
        max(TARGET[1], TARGET[2]) <= len(index()) <= TARGET[1] * TARGET[2], True)
    nb, eb, na, ea = effect()
    chk("it adds one vertex", na - nb, 1)
    chk("E drops by exactly one", eb - ea, 1)
    chk("from ten to nine", (eb, ea), (10, 9))
    before, after = demand_unchanged()
    chk("the other demanded cells do not move", before, after)
    chk("nine cells remain demanded", len(after), 9)
    chk("and the target is no longer one of them", TARGET in after, False)
    print("filled selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
