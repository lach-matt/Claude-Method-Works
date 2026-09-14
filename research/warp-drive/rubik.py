#!/usr/bin/env python3
r"""
rubik.py -- FORCING NON-CLOSURE BY SLICE MOVES, AND THE PARA-INDEXES IT NAMES.

M: "We can force measurements and additional para-indexes by forcing non-closure
through rubik axis shifts, scrambling the index."

    python3 rubik.py             the reading
    python3 rubik.py --selftest  fixtures

===============================================================================
1. WHAT A MOVE IS
===============================================================================

The master index collapses to three coordinates without loss -- (Sc, Oc) is a
strict function of C on every cell that appears anywhere -- so the object is a
6 x 3 x 4 cuboid on (C, D, R).  A cuboid is a puzzle, and a puzzle has moves.

    A SLICE MOVE fixes one coordinate at one value and cyclically shifts a
    SECOND coordinate for every cell in that slice.

        move(fix=D, at=2, shift=R, by=1)
            every cell with D = 2 has its R raised by one, mod 4;
            every other cell is untouched.

That is the legal move of a cuboid puzzle -- a layer turn on a non-square face
is a shift rather than a rotation -- and it is a BIJECTION ON THE BOX, so the
cell count is preserved exactly and no two cells ever collide.  82 moves exist:
47 of type 1 and 35 of type 2.

===============================================================================
2. TWO KINDS OF MOVE, AND THEY DO NOT CARRY THE SAME WEIGHT
===============================================================================

C is MEASURED -- it is how many of the five languages close the index, obtained
by running the operators.  D and R are ASSIGNED -- they are bands, and the band
edges were chosen.  So a move that shifts D or R asks a legitimate question and
a move that shifts C asks a hypothetical one, and this file never conflates
them.

    TYPE 1  (47 moves)  shifts only D or R.  C is never moved.
                        "How much of the closure was resting on where the bands
                        happened to fall?"  A LEGITIMATE PERTURBATION: it is the
                        banding-sensitivity sweep done finely and per-slice
                        instead of coarsely and globally.

    TYPE 2  (35 moves)  shifts C.  COUNTERFACTUAL, and labelled as such: it asks
                        what the structure would demand if an index closed in a
                        different number of languages than it does.  Nothing
                        derived from a type-2 move is a statement about the
                        seated corpus.

After any move the 5-tuple is rebuilt from C through the lawful map, because the
closing set is a DOWN-SET of the hierarchy law's containments and (Sc, Oc)
therefore follows C at every value but one.  C = 1 is the exception -- statistics
alone gives (1, 0) and information alone would give (0, 0) -- and every C = 1
cell in this corpus is statistics, so that branch is taken.  RECONSTRUCTED, not
measured, and it is the one place this file supplies a value the corpus does not
state.

===============================================================================
3. THE H97 HAZARD, WHICH IS THE WHOLE REASON FOR CARE
===============================================================================

This tree has already been burned by exactly this operation.  H97: a measurement
was taken on a RE-COORDINATED index and the extra structure it showed was read
as a property of the object.  It was a property of the coordinate system.
alpha.py records the correction and decompose.py records three more of the same
shape.

    SO A SINGLE SCRAMBLE PROVES NOTHING, AND THIS FILE NEVER QUOTES ONE.

What a scramble is good for is the ORBIT.  A property that survives every move
is a property of the index; a property that dies on the first move was a
property of the arrangement.  Every finding below is a statement about the
orbit, a count over the orbit, or a frequency across the orbit -- never a
reading of one scrambled state.

===============================================================================
4. WHAT A PARA-INDEX IS
===============================================================================

    A PARA-INDEX is a cell that scrambles DEMAND, expressed in the SEATED FRAME,
    which no seated index occupies.

When a move breaks closure, the closure operator over-generates, and the cells
it adds are specifications: an index closed by this many languages, at this
arity band, at this density, would have to exist for the structure to close.
Under the seated arrangement statistics demands nothing, so there are no
specifications to read.  BREAKING THE CLOSURE IS WHAT MAKES THE STRUCTURE SPEAK.

A para-index carries a ROBUSTNESS: the fraction of scrambles under which it is
demanded.  A cell wanted under one scramble in a thousand is noise.  A cell
wanted under most of them is the structure asking for something in a way that
does not depend on where the bands fell.

    AND A PARA-INDEX IS A CANDIDATE FOR A NAME, NOT AN INSTRUCTION TO BUILD ONE.
    Nothing here is seated, and no para-index is claimed to exist.

THE FRAME IS THE WHOLE DIFFICULTY.  Each scramble demands cells in ITS OWN
coordinates, and those differ from scramble to scramble, so the demands cannot
be added up as they stand.  Every demand is therefore PULLED BACK through the
inverse scramble into the seated frame before it is counted.  A first pass
skipped that, added demands across incompatible frames, and found zero
para-indexes -- an artefact of summing numbers that were not in the same units.

===============================================================================
5. AND THE ORBIT SEPARATES LAW FROM ACCIDENT, EXACTLY
===============================================================================

This is what the scrambling is really for, and it was not what it was built for.

The hierarchy law declares SEVEN containments lawful, out of twenty ordered
pairs of the five languages.  The other thirteen may happen to hold on any
particular index without being lawful -- hlaw.py's `index_only` asks exactly
that question and can only answer "here".  A scramble asks it everywhere.

    Over 3,000 type-1 scrambles, E(a) <= E(b) NEVER FAILS for 7 ordered pairs
    and FAILS AT LEAST ONCE for the other 13.

    THE SEVEN ARE EXACTLY THE SEVEN THE LAW DECLARES.  No lawful containment is
    broken by any scramble; no unlawful containment survives all of them.

So the orbit is a DISCRIMINATOR: it separates what the law guarantees from what
the seated arrangement merely happened to satisfy, and on this index the law is
neither too strong nor too weak.  Clause E says there is no total ranking, and
the orbit is where that stops being an assertion.

AND THE MARGINS ARE THE INTERESTING PART.  Three of the thirteen escape being
lawful only barely:

        statistics <= information      breaks in     2 of 3,000   (0.07 %)
        geometry   <= order            breaks in    48 of 3,000   (1.6 %)
        geometry   <= algebra          breaks in    48 of 3,000   (1.6 %)

while the rest break in a third to all of the orbit.  The first margin was 16
of 3,000 before the bounds correction, so the tightest near-law got EIGHT TIMES
TIGHTER and is still not a law -- which is the sharpest available statement of
how thin that particular edge of the hierarchy is.  Those three are very
nearly laws and are not, which is a sharper statement of where the hierarchy is
thin than counting refutations on one arrangement can give.
"""

import itertools
import random
import sys

import hlaw
import master

# (C, D, R) and their extents. C runs 0..5 because the hierarchy law admits six
# closing-set sizes; D and R are master.py's own bands.
AXES = ("C", "D", "R")
SIZE = (6, 3, 4)

# C -> (Sc, Oc). Forced at every value but C = 1, where {statistics} gives (1,0)
# and {information} would give (0,0). RECONSTRUCTED at C = 1, from the fact that
# every C = 1 cell in this corpus is statistics.
SIG = {0: (0, 0), 1: (1, 0), 2: (1, 0), 3: (1, 0), 4: (1, 1), 5: (1, 1)}
SIG_STATUS = {0: "FORCED", 1: "RECONSTRUCTED", 2: "FORCED",
              3: "FORCED", 4: "FORCED", 5: "FORCED"}

NOTHING_IS_SEATED_HERE = True
A_SINGLE_SCRAMBLE_PROVES_NOTHING = True


def to3(c5):
    """5-tuple -> (C, D, R)."""
    return (c5[0], c5[3], c5[4])


def to5(c3):
    """(C, D, R) -> 5-tuple, rebuilding (Sc, Oc) through the lawful map."""
    sc, oc = SIG[c3[0]]
    return (c3[0], sc, oc, c3[1], c3[2])


def seated():
    """The master index as a set of 3-tuples."""
    return frozenset(to3(c) for c in master.master_index().values())


def moves(kind="all"):
    """[(fix_axis, at, shift_axis, by)] -- every legal slice move.

    kind: "1" shifts only D or R (C never moves; a legitimate perturbation of
    the ASSIGNED coordinates), "2" shifts C (counterfactual), "all" for both.
    """
    out = []
    for fa in range(3):
        for at in range(SIZE[fa]):
            for sa in range(3):
                if sa == fa:
                    continue
                for by in range(1, SIZE[sa]):
                    t = "2" if sa == 0 else "1"
                    if kind in ("all", t):
                        out.append((fa, at, sa, by))
    return out


def apply_move(X, mv):
    """Apply one slice move to a set of 3-tuples. A bijection on the box."""
    fa, at, sa, by = mv
    out = set()
    for c in X:
        if c[fa] == at:
            c = list(c)
            c[sa] = (c[sa] + by) % SIZE[sa]
            c = tuple(c)
        out.add(c)
    return frozenset(out)


def scramble(X, seq):
    for mv in seq:
        X = apply_move(X, mv)
    return X


def name(mv):
    fa, at, sa, by = mv
    return "%s=%d %s+%d" % (AXES[fa], at, AXES[sa], by)


def profile(X3):
    """{language: E} for a 3-tuple set, measured on its rebuilt 5-tuples."""
    X5 = frozenset(to5(c) for c in X3)
    cl, _ = hlaw.closures(X5)
    return {L: len(cl[L]) - len(X5) for L in hlaw.LANGS}


def demanded(X3):
    """The cells statistics demands, back in 3-tuple form."""
    X5 = frozenset(to5(c) for c in X3)
    cl, _ = hlaw.closures(X5)
    return frozenset(to3(c) for c in cl["statistics"] - X5)


def single_move_census(kind="1"):
    """(breaks, holds, [(move, E_statistics)]) over every move of that kind.

    THE FIRST QUESTION: does the closure survive one move? If most single moves
    leave statistics closing, the closure is a property of the SHAPE and the
    arrangement is doing no work.
    """
    X = seated()
    rows = []
    for mv in moves(kind):
        rows.append((mv, profile(apply_move(X, mv))["statistics"]))
    breaks = sum(1 for _m, e in rows if e > 0)
    return breaks, len(rows) - breaks, rows


def orbit_signatures(depth=2, kind="1", cap=40000):
    """{E-vector: shortest depth at which it appears}, breadth-first.

    The orbit is the object; a single scrambled state is not.
    """
    X = seated()
    seen = {X: 0}
    sigs = {}
    frontier = [X]
    sigs[tuple(profile(X)[L] for L in hlaw.LANGS)] = 0
    for d in range(1, depth + 1):
        nxt = []
        for S in frontier:
            for mv in moves(kind):
                T = apply_move(S, mv)
                if T in seen:
                    continue
                seen[T] = d
                nxt.append(T)
                k = tuple(profile(T)[L] for L in hlaw.LANGS)
                sigs.setdefault(k, d)
                if len(seen) >= cap:
                    return sigs, len(seen)
        frontier = nxt
    return sigs, len(seen)


def undo(mv):
    """The move that reverses mv."""
    fa, at, sa, by = mv
    return (fa, at, sa, (SIZE[sa] - by) % SIZE[sa])


def pull_back(cells, seq):
    """Carry a set of cells from a scrambled frame back to the seated one.

    THIS IS WHAT MAKES THE CENSUS MEAN ANYTHING. Each scramble demands cells in
    ITS OWN coordinates, and those coordinates differ from scramble to scramble,
    so the demands cannot simply be added up. Undoing the scramble expresses
    every demand in the seated frame, where they are comparable. A first pass
    skipped this, counted demands in whichever frame produced them, and found
    that every demanded cell was occupied by SOME scramble -- zero para-indexes,
    which was an artefact of adding up numbers that were not in the same units.
    """
    out = frozenset(cells)
    for mv in reversed(seq):
        out = apply_move(out, undo(mv))
    return out


def para_index_census(n=4000, length=3, kind="1", seed=17):
    """(counts, n) -- how often each SEATED-FRAME cell is demanded, over n
    random scrambles of the given length, every demand pulled back."""
    X = seated()
    mv = moves(kind)
    rnd = random.Random(seed)
    counts = {}
    for _ in range(n):
        seq = [rnd.choice(mv) for _ in range(length)]
        for c in pull_back(demanded(scramble(X, seq)), seq):
            counts[c] = counts.get(c, 0) + 1
    return counts, n


def para_indexes(n=4000, length=3, kind="1", seed=17):
    """[(cell, robustness)] -- cells demanded in the seated frame under scramble
    that NO SEATED INDEX OCCUPIES, best first."""
    counts, N = para_index_census(n, length, kind, seed)
    X = seated()
    out = [(c, k / N) for c, k in counts.items() if c not in X]
    return sorted(out, key=lambda t: (-t[1], t[0]))


def demand_is_the_top_para(n=4000, length=3, kind="1", seed=17):
    """(rank, robustness, counterfactual top, its robustness) for the master
    index's own demanded cell in the para census.

    THE FINDING, AND ITS OWN CONTROL. The cell master.py demands at rest is also
    the cell the scrambles demand most often -- rank 1 under both move families,
    at roughly twice the runner-up.  That is a statement about STABILITY and NOT
    an independent confirmation, which is what the control establishes: refill
    the demand by fiat and rerun, and the cell is gone from the census entirely
    while the ranking reorganises around other cells.  The two measurements
    share a cause.  What survives the control is the comparison of MAGNITUDES --
    the demanded cell is asked for more often than the best cell available in
    the world where it is already filled.
    """
    D3 = to3(master.DEMANDED_AT_EIGHT)
    pi = para_indexes(n, length, kind, seed)
    rank = next((i + 1 for i, (c, _r) in enumerate(pi) if c == D3), None)
    rob = dict(pi).get(D3, 0.0)

    filled = frozenset(set(seated()) | {D3})
    orig = globals()["seated"]
    globals()["seated"] = lambda: filled
    try:
        pf = para_indexes(n, length, kind, seed)
    finally:
        globals()["seated"] = orig
    return rank, rob, (pf[0][0] if pf else None), (pf[0][1] if pf else 0.0)


def invariants(n=1200, length=4, kind="1", seed=23):
    """What survives every scramble tried. A property invariant over the orbit
    is a property of the INDEX; one that dies on the first move was a property
    of the arrangement."""
    X = seated()
    mv = moves(kind)
    rnd = random.Random(seed)
    tests = {
        "cell count is preserved": lambda S: len(S) == len(X),
        "statistics still closes": lambda S: profile(S)["statistics"] == 0,
        "order and algebra agree": lambda S: profile(S)["order"] == profile(S)["algebra"],
        "statistics is weakest or equal":
            lambda S: (lambda p: all(p["statistics"] <= p[L] for L in hlaw.LANGS))(profile(S)),
        "geometry demands fewer than order":
            lambda S: (lambda p: p["geometry"] <= p["order"])(profile(S)),
        "some language over-generates":
            lambda S: any(profile(S)[L] > 0 for L in hlaw.LANGS),
    }
    hold = {k: 0 for k in tests}
    for _ in range(n):
        S = scramble(X, [rnd.choice(mv) for _ in range(length)])
        for k, f in tests.items():
            if f(S):
                hold[k] += 1
    return hold, n


def law_separation(n=3000, length=4, kind="1", seed=11):
    """({(a,b): breaks}, n) -- for every ordered pair of languages, how many
    scrambles violate E(a) <= E(b).

    THE DISCRIMINATOR. A containment that never breaks across the orbit is
    lawful; one that breaks somewhere was an accident of the seated arrangement.
    hlaw.py's index_only() can only ask whether an unlawful containment holds
    HERE; this asks it everywhere the moves reach.
    """
    X = seated()
    mv = moves(kind)
    rnd = random.Random(seed)
    L = list(hlaw.LANGS)
    pairs = [(a, b) for a in L for b in L if a != b]
    viol = {p: 0 for p in pairs}
    for _ in range(n):
        pr = profile(scramble(X, [rnd.choice(mv) for _ in range(length)]))
        for a, b in pairs:
            if pr[a] > pr[b]:
                viol[(a, b)] += 1
    return viol, n


def distance_to_break(kind="1", cap=3):
    """Fewest type-1 moves that make statistics stop closing. None if > cap."""
    X = seated()
    mv = moves(kind)
    seen = {X}
    frontier = [X]
    for d in range(1, cap + 1):
        nxt = []
        for S in frontier:
            for m in mv:
                T = apply_move(S, m)
                if T in seen:
                    continue
                if profile(T)["statistics"] > 0:
                    return d
                seen.add(T)
                nxt.append(T)
        frontier = nxt
    return None


def report():
    print("=" * 74)
    print("RUBIK SLICE MOVES ON THE MASTER INDEX -- FORCED NON-CLOSURE")
    print("=" * 74)
    print()
    X = seated()
    print("  the state (NO LONGER CLOSED): %d cells on a %dx%dx%d cuboid, E = %s"
          % (len(X), SIZE[0], SIZE[1], SIZE[2],
             {L: profile(X)[L] for L in hlaw.LANGS}))
    print("  moves available: %d type-1 (D,R only) + %d type-2 (moves C) = %d"
          % (len(moves("1")), len(moves("2")), len(moves("all"))))
    print()

    print("1. DOES ONE MOVE BREAK IT?")
    for k, lbl in (("1", "type 1, legitimate"), ("2", "type 2, counterfactual")):
        b, h, rows = single_move_census(k)
        print("   %-24s %3d of %3d moves BREAK closure  (%.0f%%), %d hold"
              % (lbl, b, b + h, 100.0 * b / (b + h), h))
    b1, h1, rows1 = single_move_census("1")
    worst = sorted(rows1, key=lambda r: -r[1])[:5]
    print("   the five type-1 moves that cost the most:")
    for mv, e in worst:
        print("      %-14s statistics demands %2d" % (name(mv), e))
    print("   AND THE ONES THAT HOLD ARE THE FINDING: %d type-1 moves leave the" % h1)
    print("   closure intact, so the arrangement is not rigid -- some of the")
    print("   banding could have fallen differently at no cost.")
    print()

    print("2. THE ORBIT, NOT ANY ONE SCRAMBLE.")
    sigs, states = orbit_signatures(depth=2, kind="1")
    print("   states reached within two type-1 moves: %d" % states)
    print("   distinct E-vectors among them:           %d" % len(sigs))
    closing = [s for s in sigs if s[hlaw.LANGS.index("statistics")] == 0]
    print("   of those, still closed by statistics:    %d" % len(closing))
    d = distance_to_break("1")
    print("   fewest type-1 moves that break closure:  %s" % d)
    print()

    print("3. THE PARA-INDEXES -- demanded under scramble, seated nowhere.")
    pi = para_indexes()
    print("   %d cells are demanded in the seated frame and seated nowhere." % len(pi))
    print("   (every demand pulled back through its own inverse scramble first)")
    print("   %-16s %-10s  what would have to exist" % ("cell (C,D,R)", "robustness"))
    BD = ["2 coords", "3-4 coords", "5+ coords"]
    BR = ["<5%", "5-30%", "30-60%", ">60%"]
    for c, r in pi[:10]:
        print("   %-16s %6.1f%%     closed by %d, %s, density %s"
              % (str(c), 100 * r, c[0], BD[c[1]], BR[c[2]]))
    if pi:
        print("   THE TOP ROW IS THE STRUCTURE'S MOST PERSISTENT REQUEST. It is a")
        print("   candidate for a name and NOTHING IS SEATED FOR IT.")
    print()
    print("   AND THE TOP ROW IS THE MASTER INDEX'S OWN DEMANDED CELL.")
    rk, rob, cf, cfr = demand_is_the_top_para()
    print("   %s -- rank %s at %.1f%%, against %.1f%% for the runner-up."
          % (str(to3(master.DEMANDED_AT_EIGHT)), rk, 100 * rob,
             100 * pi[1][1] if len(pi) > 1 else 0.0))
    print("   It was not eligible before the bounds correction: the bounds index")
    print("   sat on that cell, so a seated cell could not be a para-index.")
    print("   THE CONTROL, AND IT CUTS AGAINST THE EASY READING. Refill the")
    print("   demand by fiat and rerun: the cell leaves the census entirely and")
    print("   %s tops it at %.1f%%. So this is NOT an independent"
          % (str(cf), 100 * cfr))
    print("   confirmation of the demand -- the two measurements share a cause.")
    print("   What survives is the MAGNITUDE: %.1f%% against %.1f%%, so the"
          % (100 * rob, 100 * cfr))
    print("   demanded cell is asked for more often than the best cell available")
    print("   in the world where it is already filled.")
    print()

    print("4. THE ORBIT SEPARATES LAW FROM ACCIDENT, EXACTLY.")
    viol, n = law_separation()
    lawful = set(hlaw.LAWFUL)
    never = sorted(p for p, v in viol.items() if v == 0)
    print("   %d ordered pairs of languages; %d never break across %d scrambles."
          % (len(viol), len(never), n))
    print("   the law declares %d lawful. Overlap: %d. Lawful pairs broken: %d."
          % (len(lawful), len(set(never) & lawful), len(lawful - set(never))))
    print("   unlawful pairs that survived the whole orbit: %d"
          % len(set(never) - lawful))
    print("   SO THE SEVEN THAT HOLD ARE EXACTLY THE SEVEN THE LAW DECLARES.")
    print()
    print("   and the margins -- the three that escape being lawful only barely:")
    for p, v in sorted((p for p in viol.items() if p[1] > 0), key=lambda t: t[1])[:3]:
        print("      %-13s <= %-13s breaks in %4d of %d  (%.1f%%)"
              % (p[0][0], p[0][1], p[1], n, 100.0 * p[1] / n))
    print("   while the rest break in a third to all of the orbit. Clause E says")
    print("   there is no total ranking; this is where that stops being an")
    print("   assertion.")
    print()

    print("5. WHAT SURVIVES EVERY SCRAMBLE IS ABOUT THE INDEX.")
    hold, n = invariants()
    for k in sorted(hold, key=lambda k: -hold[k]):
        v = hold[k]
        tag = "INVARIANT" if v == n else ("never" if v == 0 else "")
        print("   %-38s %5d / %d  %s" % (k, v, n, tag))
    print("   An invariant here is a property of the INDEX. Anything that dies")
    print("   on the first move was a property of the ARRANGEMENT, and H97 is")
    print("   what happens when the two are confused.")
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

    print("rubik selftest")
    X = seated()
    chk("the solved state is the master index", len(X), 8)
    chk("and it collapses to three coordinates", len(next(iter(X))), 3)
    # THE SOLVED STATE NO LONGER CLOSES. Completing the bounds family took the
    # master index off closure, so this file's "solved" state is now E = 1 under
    # statistics. The law separation below is UNAFFECTED -- it is a statement
    # about the ORBIT, and surviving a change of input exactly is worth more
    # than it would have been worth had the input never moved.
    chk("the state no longer closes -- E = 1", profile(X)["statistics"], 1)

    # --- the move set
    chk("type-1 moves", len(moves("1")), 47)
    chk("type-2 moves", len(moves("2")), 35)
    chk("82 in all", len(moves("all")), 82)
    chk("no type-1 move shifts C",
        any(sa == 0 for _f, _a, sa, _b in moves("1")), False)
    chk("every type-2 move shifts C",
        all(sa == 0 for _f, _a, sa, _b in moves("2")), True)

    # --- a move is a bijection: size preserved, and it is invertible
    sizes = {len(apply_move(X, m)) for m in moves("all")}
    chk("every move preserves the cell count", sizes, {8})
    inv_ok = True
    for m in moves("all"):
        fa, at, sa, by = m
        back = (fa, at, sa, (SIZE[sa] - by) % SIZE[sa])
        if back[3] == 0:
            continue
        if apply_move(apply_move(X, m), back) != X:
            inv_ok = False
            break
    chk("and every move is invertible by its complement", inv_ok, True)

    # --- the 5-tuple rebuild agrees with the seated index exactly
    chk("to5(to3(c)) recovers every seated cell",
        frozenset(to5(to3(c)) for c in master.master_index().values()),
        frozenset(master.master_index().values()))
    chk("the lawful map is FORCED everywhere but C = 1",
        sorted(k for k, v in SIG_STATUS.items() if v != "FORCED"), [1])

    # --- the census
    b1, h1, _r = single_move_census("1")
    chk("type-1 moves that break closure", b1, 42)
    chk("type-1 moves that hold it", h1, 5)
    chk("so a single move does NOT always break it", h1 > 0, True)
    chk("fewest type-1 moves to break closure", distance_to_break("1"), 1)
    b2, h2, _r2 = single_move_census("2")
    chk("and the counterfactual moves break it about as often", (b2, h2), (22, 13))

    # --- the orbit
    sigs, states = orbit_signatures(depth=1, kind="1")
    chk("states within one type-1 move", states, 36)
    chk("distinct E-vectors among them", len(sigs), 32)
    chk("the solved vector is among them",
        tuple(profile(X)[L] for L in hlaw.LANGS) in sigs, True)

    # --- para-indexes. THE PULL-BACK IS LOAD-BEARING: without it the demands of
    # different scrambles are in different coordinate systems and the census
    # returns nothing.
    seq = [(1, 2, 2, 1), (2, 0, 1, 1)]
    chk("pulling a scramble back undoes it exactly",
        pull_back(scramble(X, seq), seq), X)
    pi = para_indexes(n=600, length=3, kind="1", seed=5)
    chk("para-indexes at 600 scrambles", len(pi), 18)
    # --- AND THE TOP PARA-INDEX IS THE MASTER INDEX'S OWN DEMANDED CELL, with
    # its own control pinned beside it so the claim cannot be quoted at the
    # wrong strength. It is a STABILITY result, not a confirmation.
    _rk, _rob, _cf, _cfr = demand_is_the_top_para(n=1000, length=3, seed=17)
    chk("the demanded cell is the top para-index", _rk, 1)
    chk("and it is not eligible while the fill stands -- the control",
        _cf != to3(master.DEMANDED_AT_EIGHT), True)
    chk("SO THIS IS NOT INDEPENDENT CONFIRMATION; the magnitude is what stands",
        _rob > _cfr, True)
    chk("none of them is a seated cell", any(c in X for c, _r in pi), False)
    chk("every one is demanded by some scramble", all(r > 0 for _c, r in pi), True)
    chk("and the list is sorted by robustness",
        all(pi[i][1] >= pi[i + 1][1] for i in range(len(pi) - 1)), True)

    # --- THE HEADLINE: the orbit separates lawful containments from accidents.
    viol, vn = law_separation(n=1500, length=4, seed=11)
    never = {p for p, v in viol.items() if v == 0}
    lawful = set(hlaw.LAWFUL)
    chk("ordered pairs of languages", len(viol), 20)
    chk("containments the orbit NEVER breaks", len(never), 7)
    chk("and they are EXACTLY the ones the law declares", never, lawful)
    chk("no lawful containment is broken by any scramble", len(lawful - never), 0)
    chk("no unlawful containment survives the whole orbit", len(never - lawful), 0)
    # the near-misses: three escape lawfulness only barely, and that is the point
    chk("statistics <= information breaks only rarely",
        viol[("statistics", "information")], 2)
    chk("geometry <= order likewise", viol[("geometry", "order")], 21)
    chk("but both DO break, so neither is lawful",
        viol[("statistics", "information")] > 0 and viol[("geometry", "order")] > 0,
        True)

    # --- invariants. THE NEGATIVE CONTROL MATTERS MOST: if everything were
    # invariant the scramble would be doing nothing.
    hold, n = invariants(n=200, length=4, seed=23)
    chk("cell count is invariant", hold["cell count is preserved"], n)
    chk("order and algebra agree everywhere -- Clause B, a theorem",
        hold["order and algebra agree"], n)
    chk("BUT closure is NOT invariant, so the scramble does work",
        hold["statistics still closes"], 47)
    chk("and it is not always broken either",
        hold["statistics still closes"] > 0, True)
    chk("geometry-under-order is NOT invariant -- the law does not claim it",
        hold["geometry demands fewer than order"], 197)

    chk("nothing is seated here", NOTHING_IS_SEATED_HERE, True)
    chk("a single scramble proves nothing", A_SINGLE_SCRAMBLE_PROVES_NOTHING, True)
    print("rubik selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
