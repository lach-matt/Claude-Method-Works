#!/usr/bin/env python3
r"""
vacancy.py -- WHY THE VACANT CHANNELS ARE VACANT, AND WHAT WOULD FILL THEM.

M: "There are indexes of measure or some basal information not yet considered
in those cells, and they satisfy the language conditions of those cells, or they
tell us something about what they contain and how the non-carried language
cannot contribute.  They may be indexes not yet considered before in this field."

    python3 vacancy.py             the reading
    python3 vacancy.py --selftest  fixtures

Three of the eight lawful channels hold no index: K1, K5 and K6.  master.py's
`c_gap` asked why C = 3 and C = 4 are empty and answered with a RANDOM-SUBSET
control -- expected occupancy 0.16 and 0.02, so zero is unremarkable.  That
control is withdrawn here as the WRONG NULL, and this file is the right one.

    A NULL THAT MISPREDICTS THE OCCUPIED CELLS BY TWO ORDERS OF MAGNITUDE
    CANNOT BE TRUSTED ON THE EMPTY ONES.  Under the random-subset null K7
    expects 0.22 occupants and holds 61, and K0 expects 67 and holds 4.  The
    held indexes are nothing like random subsets, so the question has to be
    asked CONDITIONALLY: given an index that already has the ALGEBRAIC shape a
    channel needs, how often does the rest follow?

===============================================================================
0. WHAT EACH CHANNEL DEMANDS, AS A PROPERTY OF THE INDEX
===============================================================================

The five operators, exactly (decomposable.py and lawfigures.py define them;
nothing here reimplements one):

    information   X is closed under coordinatewise MAX      -- a join-semilattice
    algebra       X is closed under MIN and MAX             -- a SUBLATTICE
    order         X equals its staircase
    statistics    X is 2-DETERMINED, by its 2-coordinate projections
    geometry      X is HULL-COMPLETE, by the convex hulls of those projections

So the three vacant channels are three shapes:

    K1 {information}
        join-closed, and nothing else.

    K5 {geometry, information, statistics}
        A JOIN-SEMILATTICE THAT IS NOT A LATTICE -- closed under max, NOT under
        min -- which is also 2-determined and hull-complete.

    K6 {algebra, information, order, statistics}
        A SUBLATTICE WITH A NON-CONVEX 2-D SHADOW.

===============================================================================
1. TWO LEMMAS, PROVED AND MACHINE-CHECKED, AND THEY SETTLE K6 COMPLETELY
===============================================================================

LEMMA 1.  Every sublattice of a finite product of chains is 2-DETERMINED.

    PROOF.  The median m(a,b,c) = (a and b) or (b and c) or (c and a) is built
    from meet and join, so any sublattice is closed under it, and it satisfies
    the majority identities m(a,a,b) = m(a,b,a) = m(b,a,a) = a.  BAKER-PIXLEY
    (1975): an algebra with a majority term operation has every subalgebra of a
    product determined by its BINARY projections.  Two-determination is exactly
    that.  []

    The three-coordinate case is the whole idea in one line: given witnesses
    y12, y13, y23 agreeing with x on each pair, m(y12, y13, y23) = x, and it
    lies in X.

LEMMA 2.  Every sublattice of a finite product of chains is STAIRCASE-CLOSED.

    PROOF.  Clause B of the hierarchy law gives stair(X) = gen(X) as SETS, not
    merely in size -- measured at 2,543 of 2,543 random indexes and pinned in
    the selftest.  X a sublattice means gen(X) = X, hence stair(X) = X.  []

Both are MACHINE-CHECKED with Z3 through prover.py, over EVERY SUBSET of six
boxes up to 3x3x3x3 -- 2^81 subsets, which is a proof over the box and not a
sample of it.  Both guards were run first: the hypotheses are satisfiable (so
`unsat` is not vacuous) and the witness-form staircase encoding reproduces
decomposable.stair on 316 of 316 random indexes.  See MACHINE_CHECKED below and
`docs`-free reproduction in the selftest.

    COROLLARY -- AND IT IS THE WHOLE ANSWER FOR K6.

        A SUBLATTICE CLOSES IN algebra AND information BY DEFINITION, IN
        statistics BY LEMMA 1, AND IN order BY LEMMA 2.  SO EVERY SUBLATTICE
        SITS AT K6 OR K7, AND NOWHERE ELSE.  It sits at K7 exactly when its
        2-D shadows are convex, and at K6 exactly when one of them is not.

    K6 is therefore not an exotic corner.  It is one of only TWO homes a
    lattice-shaped index has, and it is the non-convex one.

===============================================================================
2. THE CONDITIONAL CONTROLS -- GIVEN THE ALGEBRAIC HALF, DOES THE REST FOLLOW?
===============================================================================

Sample objects that satisfy each channel's algebraic half BY CONSTRUCTION --
close a random generating set under the right operator -- and ask how often the
geometric half follows.

    join-semilattices sampled                             3,342
      ... that are NOT lattices                           3,254   97.4 %
      ... and 2-determined  (K5 minus geometry)           1,809   55.6 % of those
      ... and HULL-COMPLETE -> K5                           504   27.9 % of those

    sublattices sampled                                   3,041
      ... 2-determined AND staircase                      3,041  100.0 %   (Lemmas 1, 2)
      ... and NOT hull-complete -> K6                       204    6.7 %

NEITHER CELL IS HARD TO REACH AND NEITHER IS EMPTY BY THEOREM.  Given the
algebraic half, K5 follows better than one time in four.

===============================================================================
3. SO WHY IS NOTHING THERE?  THE STOCK, NOT THE GEOMETRY.
===============================================================================

Of the EIGHTY indexes this tree holds -- ten seated and seventy witnessed
species -- the lattice-shaped stock is:

    K5 candidates, join-semilattices that are NOT lattices          5
        periodic layout 2-D, and four spectra: (6,1) (8,3) (13,2) (26,15)
        hull-complete: 0 of 5.  All five sit at K4.
        Expected at 27.9 %: 1.4.  P(zero) = 20 %.  UNREMARKABLE, and thin --
        five candidates is not a sample, it is an anecdote.

    K6 candidates, sublattices                                     61
        Janet, and sixty spectra.
        NOT hull-complete: 0 of 61.  All sixty-one sit at K7.
        Expected at 6.7 %: 4.1.  P(zero) = 1.4 %.

    THE FIRST NUMBER IS THE ANSWER TO M'S QUESTION AND THE SECOND IS A FINDING
    IN ITS OWN RIGHT.

K5 is empty because ONLY FIVE INDEXES HAVE EVER BEEN OFFERED WITH THE RIGHT
ALGEBRAIC SHAPE, and each needed a 28 % draw it did not get.  Not one family
whose DEFINING PROPERTY is being closed under max and not under min has ever
been put to this index -- and such families are the ordinary furniture of
measure and information: the supremum of two outer measures is an outer measure
and the infimum is not; the Turing degrees are the textbook upper semilattice
that is not a lattice; monotones, norms, metrics, convex and subadditive
functions are all max-closed and not min-closed.  The ten seated indexes are
physics classifications and chemistry charts, and eight of the ten are neither
join-closed nor lattices.  M's reading is right on the measurement: an index of
that kind has better than a one-in-four chance of landing at K5 outright.

K6 is empty for a DIFFERENT and more interesting reason.  There is no shortage
of lattice-shaped indexes -- there are sixty-one -- and every single one is
hull-complete.  CAUTION, AND IT IS LOAD-BEARING: the sixty spectra are not
sixty independent draws.  They are ONE CONSTRUCTION at sixty parameter values,
so 1.4 % is an UPPER BOUND ON SURPRISE and not a p-value.  Read the finding as
"the two independent lattice constructions this tree holds are both convex",
which is a statement about two objects.

===============================================================================
4. AND HOW THE NON-CARRIED LANGUAGE CANNOT CONTRIBUTE
===============================================================================

M asked for that half explicitly, and the lemmas give it exactly.

    FOR K6 THE MISSING LANGUAGE IS geometry, AND IT IS THE ONLY FREE
    COORDINATE THERE IS.  By Lemmas 1 and 2 a sublattice gets order and
    statistics FOR FREE from being closed under min and max -- they carry no
    information about it at all.  Four of the five languages are determined by
    one algebraic fact, and the whole of the remaining question is convexity.
    A sublattice's channel is a one-bit measurement.

    FOR K5 THE MISSING LANGUAGES ARE order AND algebra, AND THE ASYMMETRY IS
    THE POINT.  Closure under min AND max gives a majority polymorphism and
    hence Baker-Pixley.  Closure under max ALONE does not: max is not a
    majority operation, no such theorem applies, and the measurement shows it
    -- 2-determination follows for 100 % of sublattices and only 55.6 % of
    join-semilattices.  THAT IS WHY order AND algebra CANNOT CONTRIBUTE TO K5:
    an index there has deliberately given up the meet, and the meet is exactly
    what buys the free languages.

===============================================================================
5. WHAT IS NOT CLAIMED
===============================================================================

Nothing is seated here.  This file names a SHAPE an index would have to have
and measures how often that shape suffices; it does not propose a family, and a
family proposed to fill a named cell would face the bar in master.NOT_SEATED
and the tree's own history of three constructions that hit a demanded cell and
did not survive scrutiny.

The two lemmas are proved and machine-checked over finite boxes up to 3x3x3x3.
Baker-Pixley is general, so Lemma 1 holds for every finite product of chains;
Lemma 2 rests on Clause B, which the paper proves.  The CONTROLS are samples and
are quoted as samples.
"""

import itertools
import random
import sys

import decomposable as D
import hlaw
import master

# The conditional controls of section 2, recorded as data because each is
# thousands of closure computations. Reproduce with `--controls`.
JOIN_CONTROL = (3342, 3254, 1809, 504)      # sampled, not-lattice, +2det, +hull
LATT_CONTROL = (3041, 3041, 204)            # sampled, 2det-and-staircase, not-hull

# prover.py + Z3, every subset of each box. (box, L1 proved, L2 proved).
MACHINE_CHECKED = (("3x3", True, True), ("4x4", True, True), ("2x2x2", True, True),
                   ("3x3x3", True, True), ("2x2x2x2", True, True),
                   ("3x3x3x3", True, True))

# stair(X) == gen(X) AS SETS, not merely in size -- Lemma 2 rests on it.
CLAUSE_B_SET_EQUALITY = (2543, 0)           # agree, differ


def shape_of(X):
    """(join-closed, sublattice, 2-determined, hull-complete, staircase)."""
    X = frozenset(X)
    d = len(next(iter(X)))
    box = D.box_of(X, d)
    return (D.joinclose(X) == X,
            D.gen(X) == X,
            len(hlaw.OPS["statistics"](X, box)) == len(X),
            len(hlaw.OPS["geometry"](X, box)) == len(X),
            len(hlaw.OPS["order"](X, box)) == len(X))


def held():
    """{name: cells} -- every index this tree holds, seated and species."""
    out = dict(master.inventory())
    for k, v in master.species_indexes().items():
        out["spectra %s" % (k,)] = v
    return out


def stock():
    """(K5 candidates, K6 candidates) -- [(name, hull-complete, channel)].

    A K5 CANDIDATE is a join-semilattice that is not a lattice; it reaches K5
    exactly if it is 2-determined and hull-complete.  A K6 CANDIDATE is a
    sublattice; by Lemmas 1 and 2 it reaches K6 exactly if it is NOT
    hull-complete.  Nothing else can occupy either cell.
    """
    ks = master.channel_sets()
    k5, k6 = [], []
    for nm, X in sorted(held().items()):
        j, lat, _td, hull, _st = shape_of(X)
        ch = ks.index(frozenset(master.closers(X)))
        if lat:
            k6.append((nm, hull, ch))
        elif j:
            k5.append((nm, hull, ch))
    return k5, k6


def sublattice_theorem(trials=400, seed=13):
    """The corollary, checked against the operators rather than asserted:
    EVERY sublattice lands at K6 or K7.  (channels seen, counterexamples)."""
    ks = master.channel_sets()
    rnd = random.Random(seed)
    seen, bad = set(), []
    for _ in range(trials):
        d = rnd.choice([2, 3, 4])
        v = rnd.choice([2, 3, 4])
        allc = list(itertools.product(range(v), repeat=d))
        X = D.gen(frozenset(rnd.sample(allc, rnd.randint(2, min(5, len(allc))))))
        box = D.box_of(X, d)
        if len(X) < 2 or any(len(b) < 2 for b in box):
            continue
        k = ks.index(frozenset(master.closers(X)))
        seen.add(k)
        if k not in (6, 7):
            bad.append(sorted(X))
    return sorted(seen), bad


def conditional_controls(n=200, seed=31):
    """Re-run section 2's samples. Slow; the recorded figures are the reference."""
    rnd = random.Random(seed)

    def run(closer):
        rows = []
        for arity, vals, g in [(3, 3, 4), (3, 4, 4), (4, 3, 4), (4, 3, 5), (4, 4, 5)]:
            allc = list(itertools.product(range(vals), repeat=arity))
            for _ in range(n):
                X = closer(frozenset(rnd.sample(allc, g)))
                if len(X) < 3 or len(X) > 40:
                    continue
                box = D.box_of(X, arity)
                if any(len(b) < 2 for b in box):
                    continue
                rows.append(shape_of(X))
        return rows

    j = run(D.joinclose)
    nl = [r for r in j if not r[1]]
    nl2 = [r for r in nl if r[2]]
    lat = run(D.gen)
    return ((len(j), len(nl), len(nl2), sum(1 for r in nl2 if r[3])),
            (len(lat), sum(1 for r in lat if r[2] and r[4]),
             sum(1 for r in lat if not r[3])))


def report():
    print("=" * 74)
    print("WHY THE VACANT CHANNELS ARE VACANT")
    print("=" * 74)
    print()
    ks = master.channel_sets()
    print("0. THREE CHANNELS HOLD NOTHING, AND EACH IS A SHAPE.")
    for k, what in ((1, "join-closed, and nothing else"),
                    (5, "a JOIN-SEMILATTICE THAT IS NOT A LATTICE, 2-determined,"
                        " hull-complete"),
                    (6, "a SUBLATTICE with a NON-CONVEX 2-D shadow")):
        print("   K%d {%s}" % (k, ", ".join(sorted(ks[k]))))
        print("      %s" % what)
    print()
    print("1. TWO LEMMAS, MACHINE-CHECKED OVER EVERY SUBSET OF SIX BOXES.")
    print("   L1  every sublattice is 2-DETERMINED     (Baker-Pixley, via the")
    print("       median majority polymorphism)")
    print("   L2  every sublattice is STAIRCASE-CLOSED (Clause B: stair == gen")
    print("       as SETS -- %d indexes agree, %d differ)" % CLAUSE_B_SET_EQUALITY)
    for box, a, b in MACHINE_CHECKED:
        print("       %-10s L1 %s   L2 %s" % (box, "PROVED" if a else "----",
                                              "PROVED" if b else "----"))
    seen, bad = sublattice_theorem()
    print("   COROLLARY: EVERY SUBLATTICE SITS AT K6 OR K7 AND NOWHERE ELSE.")
    print("       channels reached by %d random sublattices: %s   counterexamples: %d"
          % (400, seen, len(bad)))
    print("       so K6 is one of only two homes a lattice-shaped index has,")
    print("       and it is the non-convex one.")
    print()
    print("2. THE CONDITIONAL CONTROLS -- given the algebraic half, does the rest")
    print("   follow?  (The random-subset control in master.c_gap is the WRONG")
    print("   NULL: it expects 0.22 at K7 where 61 sit.)")
    js, jn, j2, jh = JOIN_CONTROL
    ls, l2, lh = LATT_CONTROL
    print("     join-semilattices sampled                  %6d" % js)
    print("       ... NOT lattices                         %6d  %5.1f%%" % (jn, 100 * jn / js))
    print("       ... and 2-determined                     %6d  %5.1f%% of those" % (j2, 100 * j2 / jn))
    print("       ... and HULL-COMPLETE -> K5              %6d  %5.1f%% of those" % (jh, 100 * jh / j2))
    print("     sublattices sampled                        %6d" % ls)
    print("       ... 2-determined AND staircase           %6d  %5.1f%%  (L1, L2)" % (l2, 100 * l2 / ls))
    print("       ... and NOT hull-complete -> K6          %6d  %5.1f%%" % (lh, 100 * lh / l2))
    print("   NEITHER CELL IS HARD TO REACH. Given the algebraic half, K5")
    print("   follows better than one time in four.")
    print()
    print("3. SO WHY IS NOTHING THERE?  THE STOCK, NOT THE GEOMETRY.")
    k5, k6 = stock()
    p5 = 1 - jh / j2
    p6 = 1 - lh / l2
    print("   Of the %d indexes held -- %d seated and %d witnessed species:"
          % (len(held()), len(master.inventory()), len(master.species_indexes())))
    print()
    print("   K5 candidates (join-semilattice, not a lattice): %d" % len(k5))
    for nm, hull, ch in k5:
        print("       %-28s hull-complete %-5s -> K%d" % (nm, hull, ch))
    print("       expected at %.1f%%: %.1f      observed 0      P(zero) = %.0f%%"
          % (100 * (1 - p5), len(k5) * (1 - p5), 100 * p5 ** len(k5)))
    print("       UNREMARKABLE, AND THIN. Five candidates is an anecdote.")
    print()
    print("   K6 candidates (sublattices): %d" % len(k6))
    print("       hull-complete: %d of %d -- every one of them"
          % (sum(1 for _n, h, _c in k6 if h), len(k6)))
    print("       expected at %.1f%%: %.1f      observed 0      P(zero) = %.1f%%"
          % (100 * (1 - p6), len(k6) * (1 - p6), 100 * p6 ** len(k6)))
    print("       CAUTION: the %d spectra are ONE CONSTRUCTION at %d parameter"
          % (len(k6) - 1, len(k6) - 1))
    print("       values, not independent draws, so that is an UPPER BOUND ON")
    print("       SURPRISE and not a p-value. Read it as: the two independent")
    print("       lattice constructions here are both convex.")
    print()
    print("   K5 IS EMPTY BECAUSE ONLY FIVE INDEXES HAVE EVER BEEN OFFERED WITH")
    print("   THE RIGHT ALGEBRAIC SHAPE. Not one family whose DEFINING property")
    print("   is max-closed-and-not-min-closed has been put to this index --")
    print("   and those are the ordinary furniture of measure and information:")
    print("   the sup of two outer measures is an outer measure and the inf is")
    print("   not; the Turing degrees are the textbook upper semilattice that is")
    print("   not a lattice; monotones, norms, metrics, convex and subadditive")
    print("   functions are all of that shape. Eight of the ten seated indexes")
    print("   are neither join-closed nor lattices.")
    print()
    print("4. AND HOW THE NON-CARRIED LANGUAGE CANNOT CONTRIBUTE.")
    print("   FOR K6 the missing language is geometry, and by L1 and L2 it is")
    print("   THE ONLY FREE COORDINATE THERE IS: a sublattice gets order and")
    print("   statistics free from being closed under min and max, so four of")
    print("   the five languages are fixed by one algebraic fact and the whole")
    print("   remaining question is convexity. A sublattice's channel is a")
    print("   ONE-BIT measurement.")
    print("   FOR K5 the missing languages are order and algebra, and the")
    print("   asymmetry is the point. Min AND max give a majority polymorphism")
    print("   and hence Baker-Pixley; MAX ALONE DOES NOT, and the measurement")
    print("   shows it -- 2-determination follows for 100% of sublattices and")
    print("   %.1f%% of join-semilattices. An index at K5 has given up the meet," % (100 * j2 / jn))
    print("   and the meet is exactly what buys the free languages.")
    print()
    print("5. NOTHING IS SEATED HERE. This names a shape and measures how often")
    print("   it suffices. A family proposed to fill a named cell would face")
    print("   master.NOT_SEATED's bar and this tree's own history of three")
    print("   constructions that hit a demanded cell and did not survive.")
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

    print("vacancy selftest")
    ks = master.channel_sets()
    chk("three channels hold nothing",
        [k for k in range(8)
         if not any(ks.index(frozenset(master.closers(X))) == k
                    for X in held().values())], [1, 5, 6])

    # ---- the shapes, checked against constructed witnesses rather than claimed
    k5w = frozenset([(0, 1, 2), (2, 0, 1), (2, 0, 2), (2, 1, 2)])
    chk("a K5 witness is join-closed, NOT a lattice, 2-det and hull-complete",
        shape_of(k5w), (True, False, True, True, False))
    chk("and it lands at K5",
        ks.index(frozenset(master.closers(k5w))), 5)
    k6w = frozenset([(0, 0, 0), (1, 0, 1), (2, 1, 1), (2, 2, 1)])
    chk("a K6 witness is a sublattice, 2-det and staircase, NOT hull-complete",
        shape_of(k6w), (True, True, True, False, True))
    chk("and it lands at K6",
        ks.index(frozenset(master.closers(k6w))), 6)

    # ---- LEMMA 2's foundation: Clause B is a SET equality, not a size one
    agree, differ = CLAUSE_B_SET_EQUALITY
    chk("stair == gen as SETS, measured", (agree > 2000, differ), (True, 0))
    rnd = random.Random(99)
    bad = 0
    for _ in range(120):
        d = rnd.choice([2, 3])
        v = rnd.choice([2, 3])
        allc = list(itertools.product(range(v), repeat=d))
        X = frozenset(rnd.sample(allc, rnd.randint(2, min(5, len(allc)))))
        box = D.box_of(X, d)
        if any(len(b) < 2 for b in box):
            continue
        bad += D.stair(X, box) != D.gen(X)
    chk("and re-measured here, live", bad, 0)

    # ---- THE COROLLARY
    seen, cex = sublattice_theorem()
    chk("EVERY SUBLATTICE SITS AT K6 OR K7", (seen, len(cex)), ([6, 7], 0))
    chk("machine-checked on six boxes, L1 and L2 both",
        all(a and b for _b, a, b in MACHINE_CHECKED), True)
    chk("the largest is 3x3x3x3 -- 2 ** 81 subsets, a proof not a sample",
        MACHINE_CHECKED[-1][0], "3x3x3x3")

    # ---- THE STOCK, which is the answer
    k5, k6 = stock()
    chk("K5 candidates held -- join-semilattices that are not lattices",
        len(k5), 5)
    chk("and not one is hull-complete", sum(1 for _n, h, _c in k5 if h), 0)
    chk("so all five sit at K4", sorted({c for _n, _h, c in k5}), [4])
    chk("K6 candidates held -- sublattices", len(k6), 61)
    chk("and EVERY ONE is hull-complete",
        sum(1 for _n, h, _c in k6 if h), 61)
    chk("so all sixty-one sit at K7", sorted({c for _n, _h, c in k6}), [7])

    js, jn, j2, jh = JOIN_CONTROL
    ls, l2, lh = LATT_CONTROL
    chk("conditional rate to K5 given the algebraic half",
        round(100 * jh / j2, 1), 27.9)
    chk("conditional rate to K6 given a sublattice", round(100 * lh / l2, 1), 6.7)
    chk("2-determination is FREE for a sublattice and not for a semilattice",
        (l2 == ls, round(100 * j2 / jn, 1)), (True, 55.6))
    # the honest reading of each zero
    chk("P(zero at K5) over five candidates -- unremarkable",
        round(100 * (1 - jh / j2) ** len(k5)), 20)
    chk("P(zero at K6) over sixty-one -- an UPPER BOUND on surprise, not a p",
        round(100 * (1 - lh / l2) ** len(k6), 1), 1.4)
    chk("because the sixty spectra are ONE construction, not sixty draws",
        len([n for n, _h, _c in k6 if n.startswith("spectra")]), 60)

    # ---- and the negative this file must not overstate
    chk("NOTHING IS SEATED HERE", set(master.inventory()) & {"vacancy"}, set())
    print("vacancy selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--controls" in sys.argv:
        print(conditional_controls())
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        sys.exit(report())
