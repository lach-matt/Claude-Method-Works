#!/usr/bin/env python3
r"""
hexad.py -- THE SIX MASTER INDEXES AS ONE INDEX: six points in the admissible
chart, fifteen join threads, and a self-seating that converges where the
refusal index's did not.

M: "What happens if we combine all 6 MIs into a single index of which in 3D it
represents a 6 cornered polygon, with join threads as diagonals?"

    python3 hexad.py             the reading
    python3 hexad.py --selftest  fixtures

===============================================================================
0. THE CONSTRUCTION IS ALREADY PAID FOR
===============================================================================

Every one of the six carries a cell on the SAME admissible chart --
(K, height, width) -- because DOCKET 3 fixed that chart for all of them.  So no
new coordinates are needed and nothing is chosen: the hexad is just

        H  =  { cell(M) : M one of the six master indexes }

and it is a six-cell index in exactly the space the others are charted in.
THE SIX CELLS ARE DISTINCT, so it really is a hexad and not a smaller figure
wearing six labels.

        MI (the nine)        (2,  5,  2)      closes statistics
        refusal index        (0,  5,  4)      closes nothing
        provenance           (0,  5,  5)      closes nothing
        ionisation ladder    (0, 18, 16)      closes nothing
        shell fibration      (3, 26, 17)      closes geometry, statistics
        Janet fibration      (7, 30, 12)      closes all five

===============================================================================
1. WHAT IT CLOSES, AND THE CHANNEL DOES NOT MOVE GOING UP A LEVEL
===============================================================================

        6 cells, K2 -- closes STATISTICS and nothing else
        its own cell (2, 4, 2)

    **THAT IS THE MASTER INDEX'S OWN CHANNEL.**  MI, an index of nine indexes,
    closes in statistics.  The hexad, an index of six indexes-of-things and
    indexes-of-indexes, closes in statistics too.  Going up a level of
    abstraction did not change which language holds.

    AND THE HEXAD IS NOT ONE OF ITS OWN MEMBERS.  Its cell (2, 4, 2) differs
    from MI's (2, 5, 2) in height alone, and is not among the six.  So as it
    stands it does not contain itself -- which is where section 3 starts.

===============================================================================
2. THE FIFTEEN JOIN THREADS: TEN LAND, FIVE ESCAPE
===============================================================================

A thread between two vertices is their JOIN, the coordinatewise max.  In a
product of chains that join is always another point of the box; the question is
whether it is another VERTEX.

        10 of the 15 joins land on one of the six
         5 escape the figure

    **AND THE FIVE ESCAPING JOINS ARE EXACTLY THE INFORMATION DEFICIT.**
    E(information) = 5, and the join-closure adds exactly five cells.  The
    correspondence is not a coincidence and not an approximation: information's
    operator IS join-closure, so the cells it demands are precisely the joins
    that escape.  **The diagonals that leave the polygon are what the index
    fails to know.**

        the five escaping joins        refusal v MI      (2,  5,  4)
                                       provenance v MI   (2,  5,  5)
                                       ions v MI         (2, 18, 16)
                                       ions v Janet      (7, 30, 16)
                                       shell v Janet     (7, 30, 17)

    **MI IS IN THREE OF THE FIVE.**  The index of indexes is the vertex hardest
    to join with the rest: pair it with the refusal index, with provenance, or
    with the ladder, and the thread leaves the figure every time.  Pair it with
    either fibration and the thread lands.  Nothing else is in more than two.

    THE MEETS BEHAVE DIFFERENTLY AND THE ASYMMETRY IS REAL.  Five meets escape
    as well, but they land on only THREE distinct cells -- the three K0 vertices
    all meet MI at the same place, (0, 5, 2).  So meet-closure adds three where
    join-closure adds five, and the figure is lopsided in a way a hexagon drawn
    on paper would hide.

===============================================================================
3. SEAT THE HEXAD IN ITSELF AND IT CONVERGES
===============================================================================

The refusal index could not be seated: rindex.py found that recomputing it over
an inventory containing itself CYCLES, with period two, on the faithful chart.
Put the hexad to the same test -- add its own cell as a seventh member and
recompute:

        step 1    7 cells, K2, own cell (2, 4, 2)
        step 2    unchanged -- FIXED POINT

    **IT CONVERGES IN ONE STEP, AND THE FIXED POINT CONTAINS ITSELF.**  The
    seventh member IS the hexad's own cell, and adding it changes nothing:
    cell(H + {cell(H)}) = cell(H) = (2, 4, 2).

    SO SELF-REFERENCE IS NOT UNIFORMLY FATAL HERE, AND THAT IS THE FINDING.
    Two objects in this tree were put to the same test and gave opposite
    answers.  The refusal index cycles because R is recomputed FROM the
    inventory -- adding a member changes every other member's value.  The
    hexad's members are CELLS, already computed, and adding a seventh does not
    disturb the other six; only the hexad's own cell could move, and it does not.

        THE DIFFERENCE IS THAT ONE MAP IS MONOTONE IN ITS INPUT AND THE OTHER
        IS NOT.  Stated as a measurement rather than a theorem: this file
        verifies the fixed point, it does not prove convergence is forced.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    TO CALL THE HEPTAD A SEVENTH MASTER INDEX.  Its seventh member is a
    bookkeeping entry -- the hexad's own cell -- not a new object with its own
    members.  The count of master indexes is six.

    TO READ THE CONVERGENCE AS A LICENCE TO SEAT THE REFUSAL INDEX.  The two
    tests are of different maps and gave different answers; the refusal index's
    cycle stands exactly as rindex.py reports it.

    TO DRAW THE HEXAD AS A REGULAR HEXAGON.  Six points in (K, height, width)
    are not coplanar and not evenly spaced; the render places them at their
    measured coordinates.  A tidy hexagon would be a picture of the word "six",
    not of the index.
"""

import itertools
import sys

import hlaw
import mi

import axes as _axes
import fibred as _fibred
import ions as _ions
import madelung as _madelung
import rindex as _rindex

ORDER = ("MI (the nine)", "refusal index", "provenance",
         "ionisation ladder", "shell fibration", "Janet fibration")


def six():
    """{name: the index itself} -- the six master indexes."""
    return {
        "MI (the nine)": frozenset(mi.index().values()),
        "refusal index": _rindex.rindex(),
        "provenance": _axes.index(),
        "ionisation ladder": _ions.index(),
        "shell fibration": _fibred.index(),
        "Janet fibration": _madelung.janet(),
    }


def cells():
    """{name: its cell on the admissible chart}."""
    return {nm: mi.cell(X) for nm, X in six().items()}


def hexad():
    """H -- the six cells as one index."""
    return frozenset(cells().values())


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def deficits(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return {L: len(cl[L]) - len(X) for L in sorted(hlaw.LANGS)}


def _join(a, b):
    return tuple(max(x, y) for x, y in zip(a, b))


def _meet(a, b):
    return tuple(min(x, y) for x, y in zip(a, b))


def threads():
    """[(nameA, nameB, join, join lands, meet, meet lands)] over all 15 pairs."""
    H = hexad()
    who = {v: k for k, v in cells().items()}
    out = []
    for a, b in itertools.combinations(sorted(H), 2):
        j, m = _join(a, b), _meet(a, b)
        out.append((who[a], who[b], j, j in H, m, m in H))
    return out


def escaping():
    """([(a, b, join)] that leave the figure, [(a, b, meet)] likewise)."""
    t = threads()
    return ([(a, b, j) for a, b, j, jl, _m, _ml in t if not jl],
            [(a, b, m) for a, b, _j, _jl, m, ml in t if not ml])


def involvement():
    """{vertex: how many escaping joins it is in} -- who resists joining."""
    out = {}
    for a, b, _j in escaping()[0]:
        out[a] = out.get(a, 0) + 1
        out[b] = out.get(b, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))


def self_seat(steps=10):
    """[(step, cells, K, own cell)] and the verdict, seating H inside itself.

    The same test rindex.py ran on the refusal index, which CYCLED.  Here the
    seventh member is the hexad's own cell.
    """
    base = set(cells().values())
    cur, seq, rows = frozenset(base), [frozenset(base)], []
    for s in range(1, steps + 1):
        nxt = frozenset(base | {mi.cell(cur)})
        rows.append((s, len(nxt), mi.K(nxt), mi.cell(nxt)))
        if nxt == cur:
            return rows, "FIXED POINT", s
        if nxt in seq:
            return rows, "CYCLE", seq.index(nxt)
        seq.append(nxt)
        cur = nxt
    return rows, "UNSETTLED", None


def heptad():
    """The fixed point: the six plus the hexad's own cell."""
    base = set(cells().values())
    return frozenset(base | {mi.cell(frozenset(base))})


# ---------------------------------------------------------------------------

def report():
    H = hexad()
    print("=" * 74)
    print("THE HEXAD -- the six master indexes as one index")
    print("=" * 74)
    print()
    print("0. THE CONSTRUCTION IS ALREADY PAID FOR. All six carry a cell on the")
    print("   SAME admissible chart, so nothing is chosen.")
    c = cells()
    for nm in ORDER:
        X = six()[nm]
        print("   %-20s %-12s %5d members   closes %s"
              % (nm, str(c[nm]), len(X), ", ".join(closers(X)) or "nothing"))
    print("   six distinct cells: %s" % (len(H) == 6))
    print()

    print("1. WHAT IT CLOSES.")
    print("   %d cells   K%d   closes %s   its own cell %s"
          % (len(H), mi.K(H), ", ".join(closers(H)) or "NOTHING", mi.cell(H)))
    print("   THE MASTER INDEX'S OWN CHANNEL -- going up a level did not move")
    print("   which language holds. And the hexad is NOT one of its own members.")
    print()

    print("2. THE FIFTEEN JOIN THREADS.")
    t = threads()
    land = sum(1 for _a, _b, _j, jl, _m, _ml in t if jl)
    print("   %-20s %-20s %-14s %-9s %-14s %s"
          % ("from", "to", "join", "", "meet", ""))
    for a, b, j, jl, m, ml in t:
        print("   %-20s %-20s %-14s %-9s %-14s %s"
              % (a, b, j, "LANDS" if jl else "escapes",
                 m, "LANDS" if ml else "escapes"))
    ej, em = escaping()
    D = deficits(H)
    print()
    print("   joins landing %d of 15, escaping %d" % (land, len(ej)))
    print("   E(information) = %d, and join-closure adds %d cells."
          % (D["information"], len({_join(a, b) for a in H for b in H}) - len(H)))
    print("   THE ESCAPING DIAGONALS ARE EXACTLY WHAT THE INDEX FAILS TO KNOW:")
    print("   information's operator IS join-closure.")
    print("   meets escaping %d but landing on only %d distinct cells -- the")
    print("   three K0 vertices all meet MI at the same place."
          % (len(em), len({m for _a, _b, m in em})))
    print("   who resists joining: %s" % involvement())
    print()

    print("3. SEAT THE HEXAD IN ITSELF.")
    rows, verdict, at = self_seat()
    for s, n, k, cc in rows:
        print("   step %d: %d cells  K%d  own cell %s" % (s, n, k, cc))
    print("   VERDICT: %s at step %s" % (verdict, at))
    print("   The refusal index CYCLED under the same test. This converges in")
    print("   one step and the fixed point CONTAINS ITSELF. Self-reference is")
    print("   not uniformly fatal here, and that is the finding.")
    print()
    print("4. REFUSED: to call the heptad a seventh master index -- its seventh")
    print("   member is a bookkeeping entry, not an object with members. To")
    print("   read this convergence as licence to seat the refusal index --")
    print("   different maps, different answers. To draw the hexad as a REGULAR")
    print("   hexagon -- the six points are not coplanar and not evenly spaced.")
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

    print("hexad selftest")
    H, c = hexad(), cells()

    chk("six master indexes", len(six()), 6)
    chk("on six DISTINCT cells -- it really is a hexad", len(H), 6)
    chk("MI's cell", c["MI (the nine)"], (2, 5, 2))
    chk("the refusal index's", c["refusal index"], (0, 5, 4))
    chk("provenance's", c["provenance"], (0, 5, 5))
    chk("the ladder's", c["ionisation ladder"], (0, 18, 16))
    chk("the shell fibration's", c["shell fibration"], (3, 26, 17))
    chk("Janet's", c["Janet fibration"], (7, 30, 12))

    # ---- the channel does not move going up a level
    chk("the hexad closes in statistics alone", closers(H), ["statistics"])
    chk("which is K2 -- the master index's own channel",
        (mi.K(H), mi.K(frozenset(mi.index().values()))), (2, 2))
    chk("its own cell", mi.cell(H), (2, 4, 2))
    chk("and it is NOT one of its own members", mi.cell(H) in H, False)

    # ---- the threads
    t = threads()
    chk("fifteen pairs", len(t), 15)
    land = sum(1 for _a, _b, _j, jl, _m, _ml in t if jl)
    chk("ten joins land on a vertex", land, 10)
    ej, em = escaping()
    chk("and five escape", len(ej), 5)
    # THE CORRESPONDENCE, and it is exact rather than approximate.
    D = deficits(H)
    chk("E(information) EQUALS the number of escaping joins",
        (D["information"], len(ej)), (5, 5))
    chk("because information's operator IS join-closure",
        len({_join(a, b) for a in H for b in H} - H), 5)
    chk("statistics closes, so its deficit is zero", D["statistics"], 0)

    # ---- who resists
    chk("MI is in three of the five escaping joins",
        involvement()["MI (the nine)"], 3)
    chk("and nothing else is in more than two",
        max(v for k, v in involvement().items() if k != "MI (the nine)"), 2)

    # ---- the meet asymmetry
    chk("five meets escape too", len(em), 5)
    chk("but onto only THREE distinct cells", len({m for _a, _b, m in em}), 3)
    chk("the three K0 vertices all meet MI at the same place",
        sorted({m for a, b, m in em
                if "MI (the nine)" in (a, b)}), [(0, 5, 2)])

    # ---- THE HEADLINE: it converges where the refusal index cycled
    rows, verdict, at = self_seat()
    chk("seating the hexad in itself CONVERGES", verdict, "FIXED POINT")
    chk("at step 2, on seven cells", (at, rows[-1][1]), (2, 7))
    chk("and the fixed point CONTAINS ITSELF", mi.cell(heptad()) in heptad(),
        True)
    chk("its channel is unchanged by the seating", mi.K(heptad()), 2)
    # THE CONTRAST, re-read from rindex rather than recalled.
    per, _ent, _cyc = _rindex.convergence("indicator")
    chk("where the refusal index CYCLES on its faithful chart", per, 2)
    chk("so the two self-seatings give opposite answers",
        (verdict == "FIXED POINT", per == 1), (True, False))

    print("hexad selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
