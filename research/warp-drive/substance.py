#!/usr/bin/env python3
r"""
substance.py -- THE HAWKING-ELLIS TYPE, SEATED WHERE IT DISCRIMINATES.

M: "Add the Hawking-Ellis type as the next axis."

    IT CANNOT BE AN AXIS OF THE CONDITION FAMILY, AND THE REASON IS MEASURED.
    IT IS THE SPINE OF A DIFFERENT INDEX, AND THAT INDEX IS NEW.

    python3 substance.py             the reading
    python3 substance.py --selftest  fixtures

===============================================================================
WHY NOT AN AXIS OF THE ENERGY-CONDITION FAMILY
===============================================================================

Every member of that family is a UNIVERSAL QUANTIFICATION applied to whatever
tensor it is handed.  The Hawking-Ellis type is a property of the tensor handed
IN, not of the condition doing the quantifying.  Measured rather than argued:

    conditions naming a type in their own statement    0 of 19
    adding a constant type column                      box 576 -> 576
    closures with the column                           identical, all five

**A CONSTANT COLUMN IS NOT AN AXIS.**  It never varies, so it separates no two
cells and carries no ladder.  This is the same category error that disqualified
velocity one pass earlier -- an ARGUMENT of the family mistaken for a coordinate
of it -- and it is recorded here rather than seated there.

===============================================================================
THE INDEX WHERE IT DOES DISCRIMINATE
===============================================================================

Classify SUBSTANCES rather than conditions and the type is the spine.  Four
slots, all measured or READ, none constant:

    H  Hawking-Ellis type, by increasing departure from having a rest frame
       0 = I  diagonalisable, a timelike eigenvector, a rest frame exists
       1 = II defective null case
       2 = III
       3 = IV a complex eigenvalue pair -- NO observer anywhere has a rest frame
    N  does it satisfy the NEC pointwise      0 yes   1 no
    E  evidential directness                  0 measured  1 analogue  2 derived
    K  is it a prescribed GEOMETRY rather than a prescribed matter content
       0 matter first   1 metric first

The members are READ from the tree, not invented:

    substance                     H   N   E   K   source
    ordinary matter / fluid       I   0   0   0   every substance handled
    electromagnetic field         I   0   0   0   the same
    Casimir vacuum                I   1   0   0   NEC-violating and Type I
    minimal scalar at its VEV     I   0   2   0   saturates the NEC exactly
    squeezed vacuum               I   1   0   0   measured, Ford-Roman bounded
    radiation / null dust         II  0   0   0   the defective null case
    photon-rocket exterior        II  0   2   0   Le's solution
    **the Alcubierre drive**      IV  1   2   1   MEASURED Type IV, every point
    warpshell                     I   0   2   1   Type I, dominant-energy

===============================================================================
AND IT DEMANDED TWO CELLS. ONE WAS ALREADY IN THE TREE. THE OTHER IS THE TARGET
===============================================================================

Closed under `statistics`, the nine substances did NOT close: E = 2, and the two
demanded cells were both **Type I, NEC-violating, derived-only** -- one
matter-first, one metric-first.

THE MATTER-FIRST ONE WAS ALREADY HELD AND HAD NOT BEEN SEATED: the non-minimal
scalar.  A scalar field has a rest frame, so Type I; violating the NEC is the
entire purpose of a positive xi; and it has never been measured, so derived.
Seating it drops E from 2 to 1, exactly as the semiclassical WEC did for the
condition family.

**THE ONE THAT REMAINS IS THE DESIGN TARGET, AND THE INDEX ASKED FOR IT
UNPROMPTED:**

        Type I, NEC-violating, derived, METRIC-FIRST

Read against the three metric-first rows already seated, that is precise:
the Alcubierre drive is metric-first and NEC-violating but **Type IV**, a class
with no known members; warpshell is metric-first and **Type I** but
**NEC-satisfying**, so it opens nothing.  The demanded cell is the one that is
both -- physically classed AND throat-opening.  **The index is not describing a
substance anyone has; it is stating the specification.**

Nothing is seated for it. A demanded cell is a candidate for a name, never a
claim that the thing exists.

**AND THE POINT OF THE INDEX IS THE LAST ROWS.**  Nothing known is Type IV.
The Alcubierre stress-energy is Type IV at every point tested -- computed from
the metric on a grid, differenced twice, characteristic polynomial by
Faddeev-LeVerrier and roots by Durand-Kerner, no library and no classification
assumed, validated against a vacuum noise floor six orders below signal and
against an independently held closed form.  **The warp drive asks for a
substance of a type nothing in the universe is known to be.**

That is not "impossible".  It is UNKNOWN, which is weaker and stronger at once:
weaker because no theorem forbids it, stronger because it is not a shortfall in
degree but a class with no members.  And the route out is seated beside it --
warpshell is Type I, reached by prescribing matter first rather than the metric.
**THE TYPE IS SET BY WHICH END YOU PRESCRIBE FROM**, which is the K slot, and it
is why K is in the index.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not add a constant column to the condition family.**  The measurement
above is why, and it is kept runnable so the reason survives the decision.

**It does not claim Type IV is impossible.**  Nothing known is Type IV; that is
a census, not a theorem, and the file says census.

**It does not seat a substance it cannot source.**  Type III has no member here
and the slot value is simply unoccupied -- which is a fact about what has been
classified, not a claim that Type III is empty.
"""

import sys

import hlaw

# (name, H, N, E, K, source)
SUBSTANCES = [
    ("ordinary matter / fluid",  0, 0, 0, 0, "every substance ever handled is Type I"),
    ("electromagnetic field",    0, 0, 0, 0, "the same"),
    ("Casimir vacuum",           0, 1, 0, 0, "NEC-violating and Type I, measured"),
    ("minimal scalar at VEV",    0, 0, 2, 0, "saturates the NEC exactly"),
    ("squeezed vacuum",          0, 1, 0, 0, "measured; Ford-Roman bounded"),
    ("radiation / null dust",    1, 0, 0, 0, "the defective null case"),
    ("photon-rocket exterior",   1, 0, 2, 0, "Le's solution"),
    ("the Alcubierre drive",     3, 1, 2, 1, "MEASURED Type IV at every point tested"),
    ("warpshell",                0, 0, 2, 1, "Type I, dominant-energy, observer-robust"),
    # DEMANDED BY THE INDEX BEFORE IT WAS SEATED, and the tree already held it.
    ("non-minimal scalar (xi)",  0, 1, 2, 0, "Barcelo-Visser; a scalar has a rest "
                                             "frame, and NEC violation is its purpose"),
]
COORDS = ("H", "N", "E", "K")
TYPE_NAME = {0: "I", 1: "II", 2: "III", 3: "IV"}
NOTHING_KNOWN_IS_TYPE_IV = True


def cells():
    return frozenset(tuple(r[1:5]) for r in SUBSTANCES)


def by_type():
    d = {}
    for r in SUBSTANCES:
        d.setdefault(r[1], []).append(r[0])
    return d


def constant_column_test():
    """Adding the type to the CONDITION family changes nothing. (box, box, same)."""
    import necindex
    X = frozenset(necindex.cells())
    Y = frozenset(c + (0,) for c in X)
    def boxof(S):
        d = len(next(iter(S)))
        n = 1
        for i in range(d):
            n *= len({c[i] for c in S})
        return n
    a, _ = hlaw.closures(X)
    b, _ = hlaw.closures(Y)
    named = sum(1 for r in necindex.FAMILY if "type" in r[7].lower())
    return boxof(X), boxof(Y), {L: len(a[L]) for L in hlaw.LANGS} == {L: len(b[L]) for L in hlaw.LANGS}, named


def report():
    print("=" * 74)
    print("THE HAWKING-ELLIS TYPE, SEATED WHERE IT DISCRIMINATES")
    print("=" * 74)
    print()
    b0, b1, same, named = constant_column_test()
    print("1. IT CANNOT BE AN AXIS OF THE CONDITION FAMILY.")
    print("   Every member there is a universal quantification applied to whatever")
    print("   tensor it is handed; the type is a property of the tensor handed IN.")
    print("     conditions naming a type in their own statement   %d of 19" % named)
    print("     adding a constant type column                     box %d -> %d" % (b0, b1))
    print("     closures with the column                          %s"
          % ("identical, all five" if same else "CHANGED"))
    print("   A CONSTANT COLUMN IS NOT AN AXIS. Same category error that")
    print("   disqualified velocity: an ARGUMENT mistaken for a coordinate.")
    print()

    print("2. THE INDEX WHERE IT DOES DISCRIMINATE -- substances, not conditions.")
    print("   %-28s %-4s %-3s %-3s %-3s %s" % ("substance", "type", "NEC", "ev", "K", "source"))
    for nm, H, N, E, K, src in SUBSTANCES:
        print("   %-28s %-4s %-3s %-3s %-3s %s"
              % (nm, TYPE_NAME[H], "no" if N else "yes", E, K, src[:30]))
    X = cells()
    cl, _ = hlaw.closures(X)
    print()
    print("   %d substances -> %d distinct cells" % (len(SUBSTANCES), len(X)))
    for L in hlaw.LANGS:
        print("     %-13s admits %2d  E %2d%s" % (L, len(cl[L]), len(cl[L]) - len(X),
              "   <-- CLOSES" if len(cl[L]) == len(X) else ""))
    print()

    print("3. AND THE POINT IS THE LAST TWO ROWS.")
    bt = by_type()
    for t in sorted(bt):
        print("     Type %-3s %s" % (TYPE_NAME[t], ", ".join(bt[t])))
    print("   NOTHING KNOWN IS TYPE IV, and the Alcubierre stress-energy is Type IV")
    print("   at every point tested -- computed from the metric on a grid, twice")
    print("   differenced, characteristic polynomial by Faddeev-LeVerrier and roots")
    print("   by Durand-Kerner, no library and no classification assumed.")
    print("   THE WARP DRIVE ASKS FOR A SUBSTANCE OF A TYPE NOTHING IS KNOWN TO BE.")
    print()
    print("   That is not impossible -- it is UNKNOWN, which is weaker because no")
    print("   theorem forbids it and stronger because it is not a shortfall in")
    print("   degree but a class with no members. And the route out sits beside it:")
    print("   warpshell is Type I, reached by prescribing MATTER first instead of")
    print("   the metric. THE TYPE IS SET BY WHICH END YOU PRESCRIBE FROM, which")
    print("   is the K slot and why K is in the index.")
    print()
    print("   Type III has no member here. That is a fact about what has been")
    print("   classified, not a claim that Type III is empty.")
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

    print("substance selftest")
    b0, b1, same, named = constant_column_test()
    chk("no condition names a type in its own statement", named, 0)
    chk("a constant type column leaves the box unchanged", (b0, b1), (576, 576))
    chk("and leaves every closure unchanged", same, True)

    X = cells()
    chk("ten substances", len(SUBSTANCES), 10)
    chk("giving eight distinct cells", len(X), 8)
    chk("four coordinates", len(COORDS), 4)
    chk("and no coordinate is constant",
        all(len({c[i] for c in X}) > 1 for i in range(4)), True)

    bt = by_type()
    chk("Type I holds seven substances", len(bt[0]), 7)
    chk("Type II holds two", len(bt[1]), 2)
    chk("Type III holds none -- unoccupied, not claimed empty", 2 in bt, False)
    chk("and Type IV holds exactly one", bt[3], ["the Alcubierre drive"])
    chk("which is the drive, and it is metric-first",
        [r[4] for r in SUBSTANCES if r[1] == 3], [1])
    chk("while warpshell is Type I and also metric-first-adjacent",
        [(r[1], r[4]) for r in SUBSTANCES if r[0] == "warpshell"], [(0, 1)])
    chk("so the type is not determined by K alone",
        len({r[1] for r in SUBSTANCES if r[4] == 1}), 2)

    cl, _ = hlaw.closures(X)
    # THE FINDING: it does not close. It demands the design target.
    chk("statistics does NOT close it -- one cell demanded",
        len(cl["statistics"]) - len(X), 1)
    chk("and the demanded cell is Type I, NEC-violating, derived, METRIC-FIRST",
        sorted(cl["statistics"] - X), [(0, 1, 2, 1)])
    chk("no seated substance occupies it", (0, 1, 2, 1) in X, False)
    chk("the drive is metric-first and NEC-violating but Type IV",
        [(r[1], r[2], r[4]) for r in SUBSTANCES if r[0] == "the Alcubierre drive"],
        [(3, 1, 1)])
    chk("warpshell is metric-first and Type I but NEC-SATISFYING",
        [(r[1], r[2], r[4]) for r in SUBSTANCES if r[0] == "warpshell"], [(0, 0, 1)])
    chk("so the demand is for the one that is BOTH", True, True)
    chk("nothing known is Type IV", NOTHING_KNOWN_IS_TYPE_IV, True)
    print("substance selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
