#!/usr/bin/env python3
r"""
petrov.py -- THE GRAVITY INDEX. The Petrov classification of the Weyl tensor.

M: "Build the Petrov classification as the gravity index."

    IT IS THE EXACT COUNTERPART OF THE SUBSTANCE INDEX. Hawking-Ellis classifies
    the MATTER tensor by its eigenvalue structure; Petrov classifies the CURVATURE
    tensor by the multiplicity of its principal null directions. Matter and
    geometry, the two sides of the field equation, each with a named family and a
    real ordering.

    python3 petrov.py             the reading
    python3 petrov.py --selftest  fixtures

===============================================================================
THE LADDER IS NOT A CHAIN, AND THAT IS WHY IT TAKES TWO SLOTS
===============================================================================

A Weyl tensor has four principal null directions counted with multiplicity, and
the type is the partition:

        I    (1,1,1,1)   four distinct -- algebraically GENERAL
        II   (2,1,1)     one pair coincides
        D    (2,2)       two pairs
        III  (3,1)       three coincide
        N    (4)         all four coincide
        O    --          the Weyl tensor vanishes; conformally flat

**THE PENROSE SPECIALISATION ORDER IS A PARTIAL ORDER, NOT A TOTAL ONE.** D and
III are both specialisations of II and NEITHER specialises the other. A single
ordinal slot cannot carry that, and forcing one would invent a comparison the
geometry does not make. So the type is carried by TWO measured slots and the
partial order comes out of them rather than being asserted:

        P  distinct principal null directions   O 0, N 1, D 2, III 2, II 3, I 4
        X  maximum multiplicity                 O 0, I 1, II 2, D 2, III 3, N 4

D and III agree on P and differ on X, which is exactly how they differ.

===============================================================================
THE MEMBERS, ALL STANDARD
===============================================================================

    spacetime                type   P  X  E  V
    Minkowski                O      0  0  1  0
    FLRW                     O      0  0  1  1
    generic vacuum           I      4  1  1  0
    Robinson-Trautman        II     3  2  1  0
    Schwarzschild            D      2  2  1  0
    Kerr                     D      2  2  1  0
    Reissner-Nordstrom       D      2  2  1  1
    pp-wave                  N      1  4  1  0
    gravitational-wave far field N  1  4  0  0

    E  evidential directness   0 measured   1 standard, derived
    V  vacuum                  0 yes        1 no

The type-D condition is not taken on trust here: this tree already verifies it
to 3.5e-16 independently.  And ONE ROW IS MEASURED rather than derived -- the
far-field gravitational wave, Type N, which is what a detector detects.

**TYPE III HAS NO MEMBER.**  Not a claim that it is empty -- a fact about what
has been classified. The substance index has the same hole at ITS Type III, and
the two holes are at the same place in two different classifications, which is
recorded and not explained.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not force the specialisation order into one slot.**  D and III are
incomparable and two slots are what it takes to say so.

**It does not assign a Petrov type to the warp metrics.**  Neither the
Alcubierre metric nor the warpshell has a Petrov type computed anywhere in this
tree, and computing one is a measurement this file does not make. Their absence
from the table is an absence, not a zero.

**It does not read a shared hole as a connection.**  Both this index and the
substance index have an unoccupied Type III. That is recorded because it is
striking, and it is not offered as meaning anything.
"""

import sys

import hlaw

# (name, type, P, X, E, V, note)
SPACETIMES = [
    ("Minkowski",              "O",   0, 0, 1, 0, "flat; Weyl vanishes"),
    ("FLRW",                   "O",   0, 0, 1, 1, "conformally flat, non-vacuum"),
    ("generic vacuum",         "I",   4, 1, 1, 0, "algebraically general"),
    ("Robinson-Trautman",      "II",  3, 2, 1, 0, "one repeated PND"),
    ("Schwarzschild",          "D",   2, 2, 1, 0, "type D, verified in this tree"),
    ("Kerr",                   "D",   2, 2, 1, 0, "type D; same cell as Schwarzschild"),
    ("Reissner-Nordstrom",     "D",   2, 2, 1, 1, "type D, non-vacuum"),
    ("pp-wave",                "N",   1, 4, 1, 0, "all four PNDs coincide"),
    ("GW far field",           "N",   1, 4, 0, 0, "MEASURED -- what a detector sees"),
]
COORDS = ("P", "X", "E", "V")
TYPES = ("O", "N", "D", "III", "II", "I")
TYPE_III_UNOCCUPIED = True

# The Penrose specialisation order, as PAIRS that hold. D and III are both below
# II and incomparable with each other -- the reason the index needs two slots.
SPECIALISES = (("II", "I"), ("D", "II"), ("III", "II"), ("N", "III"), ("N", "D"),
               ("O", "N"))


def cells():
    return frozenset(tuple(r[2:6]) for r in SPACETIMES)


def type_of(P, X):
    """The Petrov type from the two measured slots."""
    return {(0, 0): "O", (1, 4): "N", (2, 2): "D", (2, 3): "III",
            (3, 2): "II", (4, 1): "I"}.get((P, X))


def d_and_iii_incomparable():
    """D and III agree on P and differ on X -- neither specialises the other."""
    d = (2, 2)
    iii = (2, 3)
    return d[0] == iii[0] and d[1] != iii[1] and \
        ("D", "III") not in SPECIALISES and ("III", "D") not in SPECIALISES


def report():
    X = cells()
    print("=" * 74)
    print("THE GRAVITY INDEX -- PETROV CLASSIFICATION OF THE WEYL TENSOR")
    print("=" * 74)
    print()
    print("The exact counterpart of the substance index: Hawking-Ellis classifies")
    print("the MATTER tensor by eigenvalue structure, Petrov classifies the")
    print("CURVATURE tensor by the multiplicity of its principal null directions.")
    print("Matter and geometry, the two sides of the field equation.")
    print()
    print("1. THE LADDER IS NOT A CHAIN, WHICH IS WHY IT TAKES TWO SLOTS.")
    print("   D and III are both specialisations of II and NEITHER specialises")
    print("   the other. One ordinal slot cannot carry that; forcing one would")
    print("   invent a comparison the geometry does not make.")
    print("     P  distinct principal null directions")
    print("     X  maximum multiplicity")
    print("   D is (P=2, X=2) and III is (P=2, X=3): they agree on P and differ")
    print("   on X, which is exactly how they differ. Incomparable: %s"
          % d_and_iii_incomparable())
    print()
    print("2. THE MEMBERS.")
    print("   %-28s %-5s %2s %2s %2s %2s  %s" % ("spacetime", "type", *COORDS, "note"))
    for nm, t, P, Xm, E, V, note in SPACETIMES:
        print("   %-28s %-5s %2d %2d %2d %2d  %s" % (nm, t, P, Xm, E, V, note))
    print()
    print("   %d spacetimes -> %d distinct cells" % (len(SPACETIMES), len(X)))
    cl, _ = hlaw.closures(X)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(X)
        print("     %-13s admits %2d  E %2d%s" % (L, len(cl[L]), e,
              "   <-- CLOSES" if e == 0 else ""))
    dem = sorted(cl["statistics"] - X)
    if dem:
        print("   DEMANDED: %s" % ", ".join("%s = type %s" % (c, type_of(c[0], c[1]))
                                            for c in dem))
    print()
    print("3. TYPE III HAS NO MEMBER, and neither has it in the substance index.")
    print("   Two different classifications with a hole at the same name. That is")
    print("   recorded because it is striking and it is NOT offered as meaning")
    print("   anything. A hole is a fact about what has been classified.")
    print()
    print("   AND ONE ROW IS MEASURED rather than derived: the far-field")
    print("   gravitational wave, Type N -- which is what a detector detects.")
    print()
    print("   NO PETROV TYPE IS ASSIGNED TO THE WARP METRICS. Neither the")
    print("   Alcubierre metric nor the warpshell has one computed anywhere in")
    print("   this tree. Their absence is an absence, not a zero.")
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

    print("petrov selftest")
    chk("nine spacetimes", len(SPACETIMES), 9)
    chk("six Petrov types named", len(TYPES), 6)
    X = cells()
    chk("giving eight distinct cells", len(X), 8)
    chk("no coordinate is constant",
        all(len({c[i] for c in X}) > 1 for i in range(4)), True)

    # The two slots reproduce every type, and D/III are incomparable.
    for t, P, Xm in (("O", 0, 0), ("N", 1, 4), ("D", 2, 2), ("III", 2, 3),
                     ("II", 3, 2), ("I", 4, 1)):
        chk("(P=%d, X=%d) is type %s" % (P, Xm, t), type_of(P, Xm), t)
    chk("D and III are INCOMPARABLE, which is why two slots", d_and_iii_incomparable(), True)
    chk("and the specialisation order has neither above the other",
        ("D", "III") in SPECIALISES or ("III", "D") in SPECIALISES, False)

    # Every seated member's (P, X) really is its stated type.
    chk("every member's slots reproduce its stated type",
        all(type_of(r[2], r[3]) == r[1] for r in SPACETIMES), True)

    # The three type-D rows, one of which is a genuine cell collision.
    ds = [r[0] for r in SPACETIMES if r[1] == "D"]
    chk("three spacetimes are type D", sorted(ds),
        ["Kerr", "Reissner-Nordstrom", "Schwarzschild"])
    chk("Schwarzschild and Kerr share a cell exactly",
        tuple(r[2:6] for r in SPACETIMES if r[0] == "Schwarzschild") ==
        tuple(r[2:6] for r in SPACETIMES if r[0] == "Kerr"), True)
    chk("and Reissner-Nordstrom differs from them only in V",
        [r[5] for r in SPACETIMES if r[1] == "D"], [0, 0, 1])

    chk("Type III has no member", TYPE_III_UNOCCUPIED, True)
    chk("and no seated cell is type III",
        any(type_of(c[0], c[1]) == "III" for c in X), False)
    chk("exactly one row is MEASURED rather than derived",
        [r[0] for r in SPACETIMES if r[4] == 0], ["GW far field"])
    chk("and it is type N", [r[1] for r in SPACETIMES if r[4] == 0], ["N"])

    chk("no warp metric is assigned a type here",
        any("warp" in r[0].lower() or "alcubierre" in r[0].lower() for r in SPACETIMES),
        False)
    print("petrov selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
