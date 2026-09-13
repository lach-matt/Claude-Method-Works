#!/usr/bin/env python3
r"""
orbit.py -- IF EVERYTHING OSCILLATES, WHAT IS THE RESIDUE?

M: "Energy is on organic state.  It is always in motion because energy is
neither created nor destroyed, and energy is transferable.  But because
everything is in motion, there is a natural oscillation in spacetime which
makes the residue cells relevant.  Oscillation increases statistical
probability and possibility."

    THE CLAIM HOLDS, AND ONE LANGUAGE IS WHERE IT HOLDS.

An index read once is a SNAPSHOT.  If the system oscillates, the snapshot is
part of an ORBIT, and the cells a language admits without having observed --
the residue L(X) \ X -- stop being fiction: some of them are what the system
passes through on the rest of the cycle.  That is testable, and it is tested
here by hiding part of the seated index and asking what the closure of what
remains recovers.

    python3 orbit.py             the reading
    python3 orbit.py --selftest  fixtures

===============================================================================
WHAT IT MEASURES
===============================================================================

Against the full orbit X, for a snapshot X_t of m cells:

    RECALL     |X and L(X_t)| / |X|        how much of the ORBIT is anticipated
    PRECISION  |X and L(X_t)| / |L(X_t)|   how much of what is ADMITTED is real

A snapshot with no closure at all scores recall m/|X| at precision 1.  Any
language beating m/|X| on recall is genuinely anticipating motion it has not
seen.  Any language below 1 on precision is inventing cells the orbit never
visits.  BOTH NUMBERS ARE NEEDED and reporting either alone misleads: order
looks clairvoyant on recall and is nine-tenths noise.

===============================================================================
WHAT IT FINDS
===============================================================================

  * EVERY language beats the raw snapshot on recall.  The residue really does
    overlap the orbit.  The claim's first half is confirmed.

  * ONLY `geometry` is right about it.  Around 91 % recall at 61 % precision,
    against `order`/`algebra` matching that recall at about 10 % precision --
    they anticipate the orbit by admitting nearly everything.

  * `statistics` has precision 1 EXACTLY, AND THAT IS A THEOREM, not a
    measurement.  It is monotone, and E = 0 on the full orbit, so for any
    snapshot X_t subset X:  statistics(X_t) subset statistics(X) = X.  It
    cannot over-claim.  It also barely anticipates -- a few points over the
    raw snapshot -- because a language that admits only what it saw has
    nothing to say about where the thing is going.

  * THE MIMIC BAND AND THE ANTICIPATION BAND ARE THE SAME BAND.  `geometry`
    was the only language whose residue sits in 0 < E/|X| < 1 on this index,
    and it is the only language whose residue is mostly real orbit.  Those are
    two different measurements landing on one operator.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It never reports recall without precision.**  The whole finding is a
trade-off and either number alone inverts the conclusion.

**It does not claim the closure IS the orbit.**  It is not: even seeing 14 of
17 cells, no language reliably recovers the whole, and the best case recovers
all of it in well under half of draws.  The residue OVERLAPS the orbit.  It
does not equal it, and the file says so where the numbers are printed.

**It does not model an oscillation.**  Hiding cells at random is a stand-in
for a cycle, not a cycle.  A real orbit visits cells in an order and with a
period, and neither is represented here.  What is measured is the weaker and
still meaningful thing: whether a partial view closes toward the whole.
"""

import random
import sys

import hlaw
import necindex

LANGS = hlaw.LANGS


def orbit():
    """The full seated index, standing in for one complete cycle."""
    return frozenset(necindex.cells())


def snapshot_scores(m, trials=200, seed=5):
    """{lang: (recall, precision)} averaged over `trials` snapshots of size m."""
    X = orbit()
    rnd = random.Random(seed)
    acc = {L: [0.0, 0.0, 0] for L in LANGS}
    for _ in range(trials):
        Xt = frozenset(rnd.sample(sorted(X), m))
        cl, _ = hlaw.closures(Xt)
        for L in LANGS:
            inter = len(X & cl[L])
            acc[L][0] += inter / len(X)
            acc[L][1] += inter / max(len(cl[L]), 1)
            acc[L][2] += (X <= cl[L])
    return {L: (a[0] / trials, a[1] / trials, a[2]) for L, a in acc.items()}


def raw_recall(m):
    """What a snapshot scores with no closure at all."""
    return m / len(orbit())


def report():
    X = orbit()
    print("=" * 74)
    print("THE ORBIT: WHAT A SNAPSHOT'S CLOSURE KNOWS ABOUT THE REST OF THE CYCLE")
    print("=" * 74)
    print("Orbit = the seated index, %d cells.  A snapshot hides the rest." % len(X))
    print()
    print("  %-4s %-8s %s" % ("m", "raw", "  ".join("%-18s" % L for L in LANGS)))
    for m in (14, 12, 10, 8, 6):
        sc = snapshot_scores(m)
        cells = "  ".join("%-18s" % ("rec %2d%% prec %3d%%" % (100 * sc[L][0], 100 * sc[L][1]))
                          for L in LANGS)
        print("  %-4d %-8s %s" % (m, "%d%%" % (100 * raw_recall(m)), cells))
    print()
    print("  raw = recall of the snapshot with no closure applied, at precision 100%.")
    print()
    print("READ IT AS A TRADE-OFF, WHICH IS THE ONLY HONEST WAY:")
    print("  * every language beats the raw snapshot on recall, so the residue")
    print("    really does overlap the orbit -- the claim's first half holds;")
    print("  * only `geometry` is RIGHT about it, near 61% precision while")
    print("    `order`/`algebra` reach the same recall at about 10%;")
    print("  * `statistics` is at precision 100% BY THEOREM: monotone, and")
    print("    E = 0 on the orbit, so statistics(X_t) subset statistics(X) = X.")
    print()
    sc = snapshot_scores(14)
    print("  And no language recovers the WHOLE orbit reliably. At m = 14 of %d:" % len(X))
    for L in LANGS:
        print("     %-12s recovered all of it in %3d of 200 draws" % (L, sc[L][2]))
    print()
    print("  THE RESIDUE OVERLAPS THE ORBIT. IT DOES NOT EQUAL IT.")
    return 0


def selftest():
    ok = True

    def chk(name, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("orbit selftest")
    X = orbit()
    chk("the orbit is the seated index", len(X), 18)

    # The theorem: statistics is monotone and E = 0 on the orbit, so its closure
    # of any snapshot is a SUBSET of the orbit -- precision exactly 1.
    rnd = random.Random(3)
    worst = 1.0
    for _ in range(60):
        m = rnd.randint(3, 16)
        Xt = frozenset(rnd.sample(sorted(X), m))
        cl, _ = hlaw.closures(Xt)
        worst = min(worst, len(X & cl["statistics"]) / max(len(cl["statistics"]), 1))
    chk("statistics precision is exactly 1, by monotonicity + E=0", worst, 1.0, 1e-12)

    sc = snapshot_scores(14)
    # Every language must beat the raw snapshot on recall, or the claim fails.
    for L in LANGS:
        chk("%s beats the raw snapshot on recall (m=14)" % L, sc[L][0] > raw_recall(14), True)
    # geometry is the one with a usable precision; order floods.
    chk("geometry precision is far above order's", sc["geometry"][1] > 3 * sc["order"][1], True)
    chk("geometry recall is within 5 points of order's",
        abs(sc["geometry"][0] - sc["order"][0]) < 0.05, True)
    chk("order precision is under 20%", sc["order"][1] < 0.20, True)
    # And nobody recovers the whole orbit reliably.
    chk("no language recovers the whole orbit in most draws",
        max(sc[L][2] for L in LANGS) < 100, True)

    # Monotonicity in m: a bigger snapshot recalls more, for every language.
    s10, s14 = snapshot_scores(10), snapshot_scores(14)
    for L in LANGS:
        chk("%s recall rises with snapshot size" % L, s14[L][0] > s10[L][0], True)

    print("orbit selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
