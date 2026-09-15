#!/usr/bin/env python3
r"""
hexad.py -- THE FIGURE THE SEATED INDEXES MAKE, and what changes as it grows.

M: "What happens if we combine all 6 MIs into a single index of which in 3D it
represents a 6 cornered polygon, with join threads as diagonals?"

    python3 hexad.py             the reading
    python3 hexad.py --selftest  fixtures

THE FILE IS STILL CALLED hexad.py AND THE FIGURE IS NO LONGER A HEXAD.  It was
six when it was built.  Seating the channel index and the entropy index took it
to eight, and the name is kept because the finding is exactly that the figure
GROWS -- renaming it at every seating would hide the thing worth seeing.

===============================================================================
0. THE CONSTRUCTION IS ALREADY PAID FOR
===============================================================================

Every seated index carries a cell on the SAME admissible chart --
(K, height, width) -- because DOCKET 3 fixed that chart for all of them.  So the
figure is just

        F  =  { cell(M) : M a seated master index }

and it is an index in exactly the space its own members are charted in.  No new
coordinates, nothing chosen.  At eight:

        refusal index        (0,  5,  4)      channel index      (0, 16, 24)
        provenance           (0,  5,  5)      ionisation ladder  (0, 18, 16)
        entropy index        (2,  4,  5)      shell fibration    (3, 26, 17)
        MI (the nine)        (2,  5,  2)      Janet fibration    (7, 30, 12)

===============================================================================
1. THE FIGURE'S CHANNEL IS NOT STABLE UNDER GROWTH
===============================================================================

        six     K2 -- closes STATISTICS      own cell (2, 4, 2)
        seven   K0 -- closes NOTHING         own cell (0, 4, 3)
        eight   K0 -- closes NOTHING         own cell (0, 4, 4)

    AT SIX IT CLOSED IN STATISTICS -- the master index's own channel, which read
    as a striking invariance of level.  **THE SEVENTH VERTEX DESTROYED IT.**
    Adding the entropy index alone takes the figure to K0, and it does not come
    back.  So the hexad's K2 was a fact about those six and not about the
    construction, and this file says so where it once said otherwise.

===============================================================================
2. THE JOIN THREADS, AND A CORRESPONDENCE THAT IS TRUE ONLY AT SIX
===============================================================================

A thread between two vertices is their JOIN, the coordinatewise max.

        six     15 pairs   10 land   5 escape    5 distinct escape cells
        seven   21 pairs   12 land   9 escape    5 distinct
        eight   28 pairs   14 land  14 escape    9 distinct

    AT SIX, AND ONLY AT SIX, THE ESCAPING DIAGONALS ARE EXACTLY THE INFORMATION
    DEFICIT: five escapes, five distinct cells, E(information) = 5.

    **AND THE REASON IS A ONE-ROUND CLOSURE, WHICH IS NOT GENERAL.**  Information's
    operator is join-closure, and join-closure ITERATES -- the joins of the new
    cells with the old must be added too.  At six that second round adds nothing,
    so the pairwise diagonals are the whole deficit.  At eight the second round
    adds one more cell, and the count goes 9 distinct diagonals against a deficit
    of 10.  Measured:

        six     one round adds  5,  full closure adds  5  in 1 round
        eight   one round adds  9,  full closure adds 10  in 2 rounds

    SO THE EARLIER STATEMENT -- "the escaping diagonals are exactly what the
    index fails to know" -- IS TRUE AT SIX AND IS NOT A LAW.  What is always true
    is that the FULL join-closure is the information deficit, which is
    definitional and says less.  Recorded rather than quietly re-pinned, because
    the difference is between a picture and a theorem.

===============================================================================
3. SELF-SEATING: CONVERGES AT SIX AND SEVEN, CYCLES AT EIGHT
===============================================================================

rindex.py found the refusal index CYCLES when recomputed over an inventory
containing itself.  Put the figure to the same test -- add its own cell as an
extra member and recompute:

        six     FIXED POINT at step 2, seven cells
        seven   FIXED POINT at step 3, eight cells
        eight   **CYCLE, period 2, from step 2**

    **THE FIXED POINT IS LOST AS THE FIGURE GROWS.**  At six this file reported
    convergence and offered an explanation -- that the figure's members are cells
    already computed, so a new one disturbs nothing.  That explanation predicted
    convergence at every size and is REFUTED at eight.  The honest statement is
    that self-seating converges for some seated sets and not others, and nothing
    here says which in advance.

        THE REFUTED SENTENCE, kept because it was published: "Self-reference is
        not uniformly fatal here."  It is not uniformly fatal and it is not
        uniformly survivable either; the hexad and the octad disagree.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    TO NAME A PARTICULAR POLYGON AS THE CLASSIFICATION.  sources.py measures 84
    further second-order indexes buildable from nine admissible measurements,
    occupying 20 vertices the figure does not have.  Any claim that a fixed
    figure is the classification is refuted by building one more index.

    TO READ THE SIX-VERTEX PROPERTIES AS STRUCTURAL.  K2, the one-round closure
    and the fixed point are all properties of that particular six, and all three
    fail by eight.

    TO DRAW IT AS A REGULAR POLYGON.  The vertices are not coplanar and not
    evenly spaced; the render places them at their measured coordinates.
"""

import itertools
import sys

import hlaw
import mi

import axes as _axes
import entropy as _entropy
import fibred as _fibred
import inversion as _inversion
import ions as _ions
import madelung as _madelung
import probability as _probability
import rindex as _rindex
import channels as _channels

# The six the figure was built on, in the order it first reported them.
SIX = ("MI (the nine)", "refusal index", "provenance",
       "ionisation ladder", "shell fibration", "Janet fibration")
ADDED = ("entropy index", "channel index",
         "inversion index", "probability index")


def all_indexes():
    """{name: the index itself} over every seated master index."""
    return {
        "MI (the nine)": frozenset(mi.index().values()),
        "refusal index": _rindex.rindex(),
        "provenance": _axes.index(),
        "ionisation ladder": _ions.index(),
        "shell fibration": _fibred.index(),
        "Janet fibration": _madelung.janet(),
        "entropy index": _entropy.index(),
        "channel index": _channels.index(),
        "inversion index": _inversion.index(),
        "probability index": _probability.index(),
    }


def cells(names=None):
    """{name: its cell on the admissible chart}, over `names` or all ten."""
    A = all_indexes()
    ns = list(A) if names is None else list(names)
    return {n: mi.cell(A[n]) for n in ns}


def figure(names=None):
    """F -- the seated cells as one index."""
    return frozenset(cells(names).values())


def hexad():
    """The original six, kept so the growth is measurable against it."""
    return figure(SIX)


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def _join(a, b):
    return tuple(max(x, y) for x, y in zip(a, b))


def _meet(a, b):
    return tuple(min(x, y) for x, y in zip(a, b))


def threads(names=None):
    """[(a, b, join, join lands, meet, meet lands)] over every pair."""
    F = figure(names)
    who = {v: k for k, v in cells(names).items()}
    return [(who[a], who[b], _join(a, b), _join(a, b) in F,
             _meet(a, b), _meet(a, b) in F)
            for a, b in itertools.combinations(sorted(F), 2)]


def escaping(names=None):
    """([(a, b, join)] leaving the figure, [(a, b, meet)] likewise)."""
    t = threads(names)
    return ([(a, b, j) for a, b, j, jl, _m, _ml in t if not jl],
            [(a, b, m) for a, b, _j, _jl, m, ml in t if not ml])


def join_closure(names=None):
    """(the closure, cells it adds, how many ROUNDS it took).

    The round count is the whole of section 2: at six the closure stabilises in
    one round, so the pairwise diagonals ARE the deficit; above six it does not.
    """
    S = set(figure(names))
    start, rounds = len(S), 0
    while True:
        new = {_join(a, b) for a in S for b in S} - S
        if not new:
            return frozenset(S), len(S) - start, rounds
        S |= new
        rounds += 1


def deficit(names=None, lang="information"):
    F = figure(names)
    cl, _b = hlaw.closures(F)
    return len(cl[lang]) - len(F)


def diagonals_equal_deficit(names=None):
    """(escaping pairs, distinct escape cells, E(information), rounds).

    True correspondence needs distinct == E, which needs a one-round closure.
    """
    ej, _em = escaping(names)
    _c, _added, rounds = join_closure(names)
    return len(ej), len({j for _a, _b, j in ej}), deficit(names), rounds


def self_seat(names=None, steps=12):
    """(verdict, step, cells) -- add the figure's own cell and recompute."""
    base = set(cells(names).values())
    cur, seq = frozenset(base), [frozenset(base)]
    for s in range(1, steps + 1):
        nxt = frozenset(base | {mi.cell(cur)})
        if nxt == cur:
            return "FIXED POINT", s, len(nxt)
        if nxt in seq:
            return "CYCLE period %d" % (s - seq.index(nxt)), s, len(nxt)
        seq.append(nxt)
        cur = nxt
    return "UNSETTLED", None, len(cur)


def growth():
    """[(size, K, own cell, verdict, step)] at six, seven and eight."""
    out = []
    for k in range(6, 6 + len(ADDED) + 1):
        ns = list(SIX) + list(ADDED[:k - 6])
        F = figure(ns)
        v, s, _n = self_seat(ns)
        out.append((k, mi.K(F), mi.cell(F), v, s))
    return out


def involvement(names=None):
    """{vertex: how many escaping joins it is in}."""
    out = {}
    for a, b, _j in escaping(names)[0]:
        out[a] = out.get(a, 0) + 1
        out[b] = out.get(b, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))


# ---------------------------------------------------------------------------

def report():
    F = figure()
    print("=" * 74)
    print("THE FIGURE THE SEATED INDEXES MAKE -- now ten, once six")
    print("=" * 74)
    print()
    print("0. THE CONSTRUCTION IS ALREADY PAID FOR. Every seated index carries")
    print("   a cell on the SAME admissible chart, so nothing is chosen.")
    for nm, c in sorted(cells().items(), key=lambda kv: kv[1]):
        print("   %-22s %s" % (nm, c))
    print()

    print("1. THE CHANNEL IS NOT STABLE UNDER GROWTH.")
    for k, K, c, v, s in growth():
        print("   %d vertices  K%-2d  closes %-12s own cell %s"
              % (k, K, ", ".join(closers(figure(list(SIX) + list(ADDED[:k - 6]))))
                 or "nothing", c))
    print("   At six it closed in STATISTICS -- the master index's own channel.")
    print("   THE SEVENTH VERTEX DESTROYED IT and it does not come back.")
    print()

    print("2. THE JOIN THREADS.")
    for k in range(6, 7 + len(ADDED)):
        ns = list(SIX) + list(ADDED[:k - 6])
        p, d, E, r = diagonals_equal_deficit(ns)
        tot = len(threads(ns))
        print("   %d vertices  %2d pairs  %2d escape  %2d distinct  E(info) %2d"
              "  closure rounds %d" % (k, tot, p, d, E, r))
    print("   AT SIX, AND ONLY AT SIX, distinct escapes == E(information).")
    print("   The reason is a ONE-ROUND closure: join-closure iterates, and at")
    print("   six the second round adds nothing. At eight it adds one more, so")
    print("   nine diagonals stand against a deficit of ten.")
    print("   What is ALWAYS true is that the FULL join-closure is the deficit,")
    print("   which is definitional and says less.")
    print("   AND E DID NOT MOVE FROM EIGHT TO TEN. Both vertices seated after")
    print("   the octad are NEUTRAL in demand.py's sense -- outside the closure,")
    print("   adding no join but themselves -- so the figure grew by two and the")
    print("   ten cells it is missing are the same ten. Growth is not automatic")
    print("   drift away from closure, and that had not been measured before.")
    print()

    print("3. SELF-SEATING.")
    for k, _K, _c, v, s in growth():
        print("   %d vertices  %-18s at step %s" % (k, v, s))
    print("   THE FIXED POINT IS LOST AS THE FIGURE GROWS. At six this file")
    print("   reported convergence and explained it by the members being cells")
    print("   already computed -- an explanation that predicted convergence at")
    print("   every size, and is REFUTED at eight.")
    print()
    print("   who resists joining, at ten: %s"
          % list(involvement().items())[:4])
    print()
    print("4. WHAT THE FIGURE IS MISSING IS NOW A LIST, NOT A MOOD.")
    try:
        import demand
        import occupy
        print("   E = %d, and demand.py names the %d cells."
              % (demand.E(F), demand.E(F)))
        cl, op = occupy.unreachable()
        print("   %d of them are CLOSED to every second-order index over this"
              % len(cl))
        print("   figure by a counting bound; they can only be first-order.")
        print("   Of the %d that remain, one is occupied eight ways and one is"
              % len(op))
        print("   open. DOCKET 12 asks whether a satisfiable cell is seated.")
    except Exception as exc:                       # pragma: no cover
        print("   (demand.py / occupy.py not consulted: %s)" % exc)
    print()
    print("5. REFUSED: to name a particular polygon as the classification --")
    print("   sources.py measures 84 further second-order indexes on 20")
    print("   vertices this figure does not have. To read the six-vertex")
    print("   properties as structural -- K2, the one-round closure and the")
    print("   fixed point all fail by eight. To draw it as a regular polygon.")
    print("   To call ten the final shape: E is 10 and the condition is 0 or 1.")
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
    F, c = figure(), cells()
    OCTAD = list(SIX) + list(ADDED[:2])
    F8 = figure(OCTAD)

    chk("ten seated indexes", len(all_indexes()), 10)
    chk("on ten DISTINCT cells", len(F), 10)
    chk("the octad is still eight distinct cells", len(F8), 8)
    chk("the original six are still six distinct cells", len(hexad()), 6)
    chk("MI's cell", c["MI (the nine)"], (2, 5, 2))
    chk("the entropy index's", c["entropy index"], (2, 4, 5))
    chk("the channel index's", c["channel index"], (0, 16, 24))
    chk("the inversion index's", c["inversion index"], (2, 6, 5))
    chk("the probability index's", c["probability index"], (2, 8, 9))

    # ---- THE CHANNEL IS NOT STABLE. The headline correction.
    g = growth()
    chk("at six the figure closed in statistics", closers(hexad()),
        ["statistics"])
    chk("at eight it closes NOTHING", closers(F8), [])
    chk("at ten it still closes nothing", closers(F), [])
    chk("K at six..ten", [K for _k, K, _c, _v, _s in g], [2, 0, 0, 0, 0])
    chk("own cell at six..ten", [cc for _k, _K, cc, _v, _s in g],
        [(2, 4, 2), (0, 4, 3), (0, 4, 4), (0, 4, 4), (0, 5, 4)])
    # SO THE SEVENTH VERTEX ALONE DID IT.
    chk("the seventh vertex alone destroyed the channel",
        (mi.K(hexad()), mi.K(figure(list(SIX) + ["entropy index"]))), (2, 0))

    # ---- the correspondence, and its true condition
    p6, d6, E6, r6 = diagonals_equal_deficit(SIX)
    p8, d8, E8, r8 = diagonals_equal_deficit(OCTAD)
    p10, d10, E10, r10 = diagonals_equal_deficit()
    chk("at six: escapes, distinct, E(info)", (p6, d6, E6), (5, 5, 5))
    chk("and the join-closure stabilises in ONE round", r6, 1)
    chk("at eight: escapes, distinct, E(info)", (p8, d8, E8), (14, 9, 10))
    chk("and it takes TWO rounds", r8, 2)
    # THE CORRECTION, pinned both ways so it cannot be requoted as a law.
    chk("so distinct == E(info) at six", d6 == E6, True)
    chk("and NOT at eight", d8 == E8, False)
    # AND E DID NOT MOVE FROM EIGHT TO TEN -- both new vertices are neutral.
    chk("E(info) at ten is still ten", E10, 10)
    chk("but the escaping pairs grew", p10 > p8, True)
    chk("so more diagonals escape while the DEFICIT stands still", 
        (p8, E8, p10, E10), (14, 10, p10, 10))
    # WHAT IS ALWAYS TRUE.
    for ns, lab in ((SIX, " (at six)"), (OCTAD, " (at eight)"), (None, " (at ten)")):
        _cl, added, _r = join_closure(ns)
        chk("full join-closure == E(information)%s" % lab, added, deficit(ns))

    # ---- SELF-SEATING FLIPS
    chk("six converges", self_seat(SIX)[0], "FIXED POINT")
    chk("seven converges", self_seat(list(SIX) + ["entropy index"])[0],
        "FIXED POINT")
    chk("EIGHT CYCLES", self_seat(OCTAD)[0], "CYCLE period 2")
    chk("so the fixed point is lost as the figure grows",
        [v for _k, _K, _c, v, _s in g][:3],
        ["FIXED POINT", "FIXED POINT", "CYCLE period 2"])

    # ---- the pairwise threads still count correctly
    chk("28 pairs at eight", len(threads(OCTAD)), 28)
    chk("45 pairs at ten", len(threads()), 45)
    chk("14 land, 14 escape at eight",
        (sum(1 for _a, _b, _j, jl, _m, _ml in threads(OCTAD) if jl), p8),
        (14, 14))
    chk("every pair either lands or escapes, at ten",
        sum(1 for _a, _b, _j, jl, _m, _ml in threads() if jl) + p10, 45)

    print("hexad selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
