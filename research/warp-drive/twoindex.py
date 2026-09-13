#!/usr/bin/env python3
r"""
twoindex.py -- ARE THEY TWO INDICES, AND DO THEY OSCILLATE INTO EACH OTHER?

M: "Can we try to build an index that contains only exotic matter, and intersect
it with the periodic index of neutral ground state elements where the
intersection is genuine.  I want to see if it can indeed be two separate indices
that interact with each other in an oscillation."

    TWO INDICES: YES, AND CLEANLY -- THE GENUINE INTERSECTION IS EMPTY.
    OSCILLATING INTO EACH OTHER: NO. ZERO ANTICIPATION, BOTH DIRECTIONS,
    ALL FIVE LANGUAGES.
    AND THE REASON IS THE FINDING: THE CONTACT IS ONE-DIMENSIONAL.

    python3 twoindex.py             the reading
    python3 twoindex.py --selftest  fixtures

===============================================================================
THE EMBEDDING, AND WHY IT IS THE HONEST ONE AVAILABLE
===============================================================================

Two indices cannot be intersected until they share coordinates, and a forced
embedding manufactures whichever answer it is pointed at.  So the axes here are
only those BOTH sides genuinely carry, and every one was established by earlier
measurement rather than invented for this test:

    L   enters the ionisation limit?    0 no   1 yes
    Q   regime                          0 classical      1 semiclassical
    E   evidential directness           0 measured  1 analogue  2 derived
    S   scaling with nuclear charge     0 none   1 Z^2   2 Z^4

Four axes, a 36-cell box.  That thinness is not a defect of the construction --
it is the measurement.  There were no further genuinely shared axes to use.

===============================================================================
1. THE INTERSECTION IS EMPTY
===============================================================================

Nine exotic mechanisms collapse to 5 distinct cells; seven periodic entries to
3.  **No cell is shared.**  This needs no control and no statistics: the two
indices occupy disjoint cells of the box they both live in.

    THE FIRST HALF OF THE QUESTION IS ANSWERED YES.  They are two indices.

===============================================================================
2. THEY INTERACT UNDER CLOSURE -- AND SO WOULD ANY TWO SETS
===============================================================================

Closing the union admits cells that closing each part separately does not:

    language      L(X u P)   L(X) u L(P)   interaction
    order              24         13            11
    algebra            24         13            11
    geometry           20         10            10
    information        17         11             6
    statistics         11          9             2

That looks like coupling and it is not.  Over 600 random disjoint 5+3 splits of
the same box, a statistics interaction term of **2 or more occurs 81.7 % of the
time, with a mean of 4.16** -- so the measured 2 is BELOW the random average,
and a term of 2 or fewer is itself unremarkable at 30.7 %.

    THE TEST DOES NOT DECIDE, AND IT IS REPORTED AS NOT DECIDING.  An
    interaction term in a shared product box is generic; reading one as
    evidence of a physical coupling would be reading the box, not the physics.

===============================================================================
3. THE OSCILLATION TEST, AND IT IS A CLEAN NO
===============================================================================

If two indices are one oscillating system, the closure of either should
ANTICIPATE cells of the other -- that is what a residue overlapping an orbit
means, and it is the shape already used to test the oscillation claim once.
Hide one index, close the other, count what is recovered:

    periodic -> exotic     0 of 5 hidden cells, every language
    exotic -> periodic     0 of 3 hidden cells, every language

**ZERO, IN BOTH DIRECTIONS, UNDER ALL FIVE.**  And the control is worse than
zero for the claim: random three-cell sets recover exotic cells at a mean of
0.55 under `order`, so an arbitrary set does BETTER at anticipating the exotic
index than the periodic index does.

    THE SECOND HALF OF THE QUESTION IS ANSWERED NO.  On this embedding the two
    indices do not oscillate into each other; they do not touch at all.

===============================================================================
4. WHY, AND THIS IS THE PART WORTH KEEPING
===============================================================================

The two results are one result.  Every exotic mechanism but one contributes
EXACTLY ZERO to a free ion's ionisation limit -- boundaries, prepared states,
moving mirrors and proper acceleration are all absent from a free atom -- and
the single exception is vacuum polarisation.  So the whole contact between the
two indices is:

        ONE MECHANISM, TOUCHING ONE QUANTITY.

**A ONE-DIMENSIONAL INTERSECTION IS A CONTACT, NOT A COUPLING.**  There is no
second point to define a direction with, so there is nothing for an oscillation
to run along.  The negative in section 3 is not a failure to find a coupling
that is there; it is what a single point of contact must look like under any
test of this shape.

WHAT WOULD CHANGE IT, stated so the negative is useful.  A second genuine
contact.  The nearest candidate is already identified and already priced:
Casimir-Polder touches electronic structure through the static polarisability
and clears the defect axis's resolution at ten nanometres -- but it is zero on a
FREE ion, and every banked species is free.  **A bound system held near a
surface would populate a second point of contact, and two points admit a
direction.**  That is a capture, not a calculation, and nothing here does it.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not read a generic interaction term as a coupling.**  Section 2's
numbers are printed beside the control that makes them unremarkable.

**It does not widen the embedding until something appears.**  Four axes were
genuinely shared; a fifth would have had to be invented, and inventing one is
how this test would have been made to pass.

**It does not report the zero as a refutation of oscillation in general.**  It
refutes it on this embedding, between these two indices, and section 4 says
exactly what the negative is caused by.

**It does not claim the intersection is empty because nothing connects them.**
One thing does, at 1.63 and 2.32 sigma. It is one thing, and one is not enough.
"""

import itertools
import random
import sys

import hlaw

# Cells are (L, Q, E, S). Nine mechanisms, seven periodic entries.
EXOTIC = {
    "vacuum polarisation": (1, 1, 0, 2),
    "static Casimir":      (0, 1, 0, 0),
    "Casimir-Polder":      (0, 1, 0, 0),
    "squeezed vacuum":     (0, 1, 0, 0),
    "dynamical Casimir":   (0, 1, 0, 0),
    "Hawking/Unruh":       (0, 1, 1, 0),
    "static radial EM":    (0, 0, 0, 0),
    "minimal scalar VEV":  (0, 0, 2, 0),
    "non-minimal scalar":  (0, 0, 2, 0),
}
PERIODIC = {
    "Li III limit":   (1, 1, 0, 1),
    "B V limit":      (1, 1, 0, 1),
    "B IV limit":     (1, 1, 0, 1),
    "P IV limit":     (1, 1, 0, 1),
    "Dirac term":     (1, 0, 2, 2),
    "neutral ground": (0, 0, 0, 1),
    "ionic stage":    (0, 0, 0, 1),
}
ALPHA = (2, 2, 3, 3)


def cells(d):
    return frozenset(d.values())


def interaction(X, P, lang):
    """L(X u P) minus L(X) u L(P) -- cells that exist only because both are."""
    cX, _ = hlaw.closures(X)
    cP, _ = hlaw.closures(P)
    cU, _ = hlaw.closures(X | P)
    return cU[lang] - (cX[lang] | cP[lang])


def anticipates(seen, hidden, lang):
    """How many hidden cells the closure of `seen` recovers."""
    cl, _ = hlaw.closures(frozenset(seen))
    return len(cl[lang] & hidden)


def control_interaction(n=600, seed=5, lang="statistics"):
    """(fraction with a term >= ours, mean term) for random disjoint 5+3 splits.

    Without this the interaction table means nothing: any two disjoint sets in a
    shared product box interact, and the question is only whether these two do
    so more than arbitrary ones.
    """
    allc = list(itertools.product(*[range(a) for a in ALPHA]))
    rnd = random.Random(seed)
    sizes = []
    for _ in range(n):
        s = rnd.sample(allc, 8)
        sizes.append(len(interaction(frozenset(s[:5]), frozenset(s[5:]), lang)))
    ours = len(interaction(cells(EXOTIC), cells(PERIODIC), lang))
    return sum(1 for x in sizes if x >= 2) / n, sum(sizes) / n, ours


def control_anticipation(n=600, seed=11, lang="order"):
    """Mean recovery of the exotic cells by a RANDOM three-cell set."""
    X = cells(EXOTIC)
    allc = [c for c in itertools.product(*[range(a) for a in ALPHA]) if c not in X]
    rnd = random.Random(seed)
    return sum(anticipates(rnd.sample(allc, 3), X, lang) for _ in range(n)) / n


def report():
    X, P = cells(EXOTIC), cells(PERIODIC)
    print("=" * 74)
    print("TWO INDICES, AND WHETHER THEY OSCILLATE INTO EACH OTHER")
    print("=" * 74)
    print()
    print("EMBEDDING: four axes, and every one was established by earlier")
    print("measurement rather than invented here -- L enters the limit, Q regime,")
    print("E evidential directness, S scaling with nuclear charge. A 36-cell box.")
    print("That thinness is the measurement, not a defect: there were no further")
    print("genuinely shared axes to use.")
    print()

    print("1. THE INTERSECTION IS EMPTY.")
    print("   %d mechanisms -> %d distinct cells; %d periodic entries -> %d cells."
          % (len(EXOTIC), len(X), len(PERIODIC), len(P)))
    print("   shared cells: %s" % (sorted(X & P) or "NONE"))
    print("   THE FIRST HALF IS ANSWERED YES. They are two indices.")
    print()

    print("2. THEY INTERACT UNDER CLOSURE -- AND SO WOULD ANY TWO SETS.")
    cX, _ = hlaw.closures(X)
    cP, _ = hlaw.closures(P)
    cU, _ = hlaw.closures(X | P)
    print("   %-13s %9s %13s %13s" % ("language", "L(X u P)", "L(X) u L(P)", "interaction"))
    for L in hlaw.LANGS:
        sep = cX[L] | cP[L]
        print("   %-13s %9d %13d %13d" % (L, len(cU[L]), len(sep), len(cU[L] - sep)))
    frac, mean, ours = control_interaction()
    print()
    print("   CONTROL, 600 random disjoint 5+3 splits of the same box:")
    print("     a statistics term of >= 2 occurs %.1f%% of the time, mean %.2f."
          % (100 * frac, mean))
    print("     ours is %d -- BELOW the random average." % ours)
    print("   THE TEST DOES NOT DECIDE, and is reported as not deciding.")
    print()

    print("3. THE OSCILLATION TEST, AND IT IS A CLEAN NO.")
    for lab, seen, hidden in (("periodic -> exotic", P, X), ("exotic -> periodic", X, P)):
        got = [anticipates(seen, hidden, L) for L in hlaw.LANGS]
        print("   %-20s %s of %d hidden, every language"
              % (lab, got[0] if len(set(got)) == 1 else got, len(hidden)))
    m = control_anticipation()
    print("   CONTROL: a RANDOM three-cell set recovers exotic cells at a mean of")
    print("     %.2f under `order` -- an arbitrary set does BETTER than the" % m)
    print("     periodic index does at anticipating the exotic one.")
    print("   THE SECOND HALF IS ANSWERED NO.")
    print()

    print("4. WHY, AND THIS IS THE PART WORTH KEEPING.")
    print("   Every exotic mechanism but one contributes EXACTLY ZERO to a free")
    print("   ion's limit -- boundaries, prepared states, moving mirrors and proper")
    print("   acceleration are all absent from a free atom. The exception is")
    print("   vacuum polarisation. So the whole contact is:")
    print()
    print("        ONE MECHANISM, TOUCHING ONE QUANTITY.")
    print()
    print("   A ONE-DIMENSIONAL INTERSECTION IS A CONTACT, NOT A COUPLING. There")
    print("   is no second point to define a direction with, so there is nothing")
    print("   for an oscillation to run along. The zero in section 3 is what a")
    print("   single point of contact MUST look like under any test of this shape.")
    print()
    print("   WHAT WOULD CHANGE IT: a second genuine contact. Casimir-Polder")
    print("   touches electronic structure through the static polarisability and")
    print("   clears the defect resolution at ten nanometres -- but it is zero on a")
    print("   FREE ion, and every banked species is free. A BOUND SYSTEM HELD NEAR")
    print("   A SURFACE would populate a second point, and two points admit a")
    print("   direction. That is a capture, not a calculation.")
    return 0


def selftest():
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("twoindex selftest")
    X, P = cells(EXOTIC), cells(PERIODIC)
    chk("nine mechanisms collapse to five cells", (len(EXOTIC), len(X)), (9, 5))
    chk("seven periodic entries collapse to three", (len(PERIODIC), len(P)), (7, 3))
    chk("THE INTERSECTION IS EMPTY", sorted(X & P), [])
    chk("the box is 36 cells", ALPHA[0] * ALPHA[1] * ALPHA[2] * ALPHA[3], 36)

    chk("statistics has an interaction term of 2",
        len(interaction(X, P, "statistics")), 2)
    chk("and every language has a non-empty one",
        all(interaction(X, P, L) for L in hlaw.LANGS), True)
    frac, mean, ours = control_interaction()
    chk("but a term >= 2 is generic in the control", frac > 0.5, True)
    chk("and ours is below the random mean", ours < mean, True)

    # The oscillation test: zero, both directions, every language.
    chk("periodic anticipates NO exotic cell, any language",
        [anticipates(P, X, L) for L in hlaw.LANGS], [0] * 5)
    chk("exotic anticipates NO periodic cell, any language",
        [anticipates(X, P, L) for L in hlaw.LANGS], [0] * 5)
    chk("and a random set does better than the periodic index",
        control_anticipation() > 0, True)

    # The cause: exactly one mechanism has a non-zero limit entry.
    chk("exactly one mechanism enters the limit",
        sum(1 for c in EXOTIC.values() if c[0] == 1), 1)
    chk("and it is vacuum polarisation", EXOTIC["vacuum polarisation"][0], 1)
    print("twoindex selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
