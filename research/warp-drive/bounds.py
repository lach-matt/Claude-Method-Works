#!/usr/bin/env python3
r"""
bounds.py -- THE BOUNDS INDEX.  What the right-hand sides are, as a family.

M: "Bound axes and indexes are perfectly acceptable.  All available axes and
indexes must be included, including the bounds."

Every member of the energy-condition family has a right-hand side, and the B
slot orders those by how much negativity each licenses.  That slot is a
COORDINATE of that index.  The bounds themselves are a FAMILY, with their own
members and their own slots, and this is that family.

    python3 bounds.py             the reading
    python3 bounds.py --selftest  fixtures

===============================================================================
THE SLOTS
===============================================================================

    W  what is bounded      0 a pointwise density
                            1 a smeared or averaged density
                            2 an entropy
    B  the bound's value    0 zero
                            1 a negative constant
                            2 a state functional
    S  state-dependent RHS  0 no    1 yes
    G  gravity enters       0 no    1 yes (a G or an area appears)
    K  known to be saturated 0 yes  1 not known

B is deliberately the SAME ladder as the energy-condition family's B slot --
by how much negativity the bound licenses -- so the two indexes agree where they
overlap rather than each inventing a coding.

===============================================================================
THE MEMBERS
===============================================================================

    bound                        W  B  S  G  K   note
    zero (the NEC's own RHS)     0  0  0  0  0   saturated by vacuum and by EM
    ANEC                         1  0  0  0  0   the averaged bound, RHS zero
    SNEC                         1  1  0  0  1   smeared null
    Ford-Roman QI                1  1  0  0  0   **Casimir saturates it**
    Fewster-Osterbrink QEI       1  1  0  0  1   state-independent; SNEC's cell
    QNEC                         0  2  1  0  1   entropy variation on the RHS
    Bekenstein                   2  1  0  1  0   saturated by black holes
    Bousso covariant             2  1  0  1  1   lightsheets

**THE ONE THAT MATTERS FOR THIS PROJECT IS FORD-ROMAN, AND IT IS SATURATED.**
The negative-energy census turns on that: Casimir is the Ford-Roman bound
saturated, not an exception to it, which is why no material choice crosses it.
A saturated bound is a wall with something already standing against it.

===============================================================================
WHAT THE BOUNDS INDEX IS FOR
===============================================================================

Two things it makes visible that the B slot alone cannot:

**THE GRAVITY SPLIT.**  Two of the eight bounds have gravity in them and six do
not.  The six are statements about quantum field theory on a fixed background;
the two are statements about spacetime.  That division is invisible from inside
the energy-condition family, where every bound is just a value of B.

**SATURATION IS A PROPERTY OF THE BOUND, NOT OF THE CONDITION.**  Four of the
eight are known to be saturated -- zero by the vacuum and by the electromagnetic
field, ANEC by the vacuum along a complete null geodesic, Ford-Roman by Casimir,
Bekenstein by black holes -- and the other four are not. That is what tells you
which walls have already been reached, and it is the difference between a bound
that is a limit and one that is merely an estimate.  The count was written as
three here on the first pass, omitting ANEC; the table was right and the
sentence was wrong, and the selftest is what caught it.

===============================================================================
WHERE IT LANDS IN THE MASTER INDEX -- AND IT IS THE CELL THAT WAS DEMANDED
===============================================================================

At eight seated indexes the master index stopped closing and demanded exactly
one cell: closed by one language and that language `statistics`, five or more
coordinates, density between 5 % and 30 %.  Nothing seated occupied it.

This index does.  Seven cells, five coordinates, box 72, density 9.7 %, closed
by `statistics` and nothing else.  Seating it returns the master index to
closure with nothing further demanded.

Stated at its true strength and no higher: the demanded cell was on the record
before this file was written, so it is not a blind prediction; and the arity
band is carried entirely by the choice to seat five slots -- drop any one and
the hit fails.  What is not a choice is the closure signature, which a random
seven-cell set in this same box reproduces about one time in a hundred.  The
master index's own module holds the control and the caveat.
"""

import sys

import hlaw

# (name, W, B, S, G, K, note)
BOUNDS = [
    ("zero (the NEC's RHS)",   0, 0, 0, 0, 0, "saturated by the vacuum and by EM"),
    ("ANEC",                   1, 0, 0, 0, 0, "averaged, RHS zero"),
    ("SNEC",                   1, 1, 0, 0, 1, "smeared null"),
    ("Ford-Roman QI",          1, 1, 0, 0, 0, "CASIMIR SATURATES IT"),
    ("Fewster-Osterbrink QEI", 1, 1, 0, 0, 1, "state-independent; shares SNEC's cell"),
    ("QNEC",                   0, 2, 1, 0, 1, "entropy variation on the RHS"),
    ("Bekenstein",             2, 1, 0, 1, 0, "saturated by black holes"),
    ("Bousso covariant",       2, 1, 0, 1, 1, "lightsheets"),
]
COORDS = ("W", "B", "S", "G", "K")


def cells():
    return frozenset(tuple(r[1:6]) for r in BOUNDS)


def saturated():
    return [r[0] for r in BOUNDS if r[5] == 0]


def gravitational():
    return [r[0] for r in BOUNDS if r[4] == 1]


def collisions():
    seen = {}
    for r in BOUNDS:
        seen.setdefault(tuple(r[1:6]), []).append(r[0])
    return sorted(tuple(sorted(v)) for v in seen.values() if len(v) > 1)


def report():
    X = cells()
    print("=" * 74)
    print("THE BOUNDS INDEX -- the right-hand sides, as a family")
    print("=" * 74)
    print()
    print("The energy-condition family's B slot orders bounds by how much")
    print("negativity each licenses. That slot is a COORDINATE of that index.")
    print("The bounds themselves are a FAMILY, and this is it.")
    print()
    print("   %-26s %2s %2s %2s %2s %2s  %s" % ("bound", *COORDS, "note"))
    for nm, W, B, S, G, K, note in BOUNDS:
        print("   %-26s %2d %2d %2d %2d %2d  %s" % (nm, W, B, S, G, K, note))
    print()
    print("   %d bounds -> %d distinct cells" % (len(BOUNDS), len(X)))
    for a in collisions():
        print("     collision: %s" % " and ".join(a))
    cl, _ = hlaw.closures(X)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(X)
        print("     %-13s admits %2d  E %2d%s" % (L, len(cl[L]), e,
              "   <-- CLOSES" if e == 0 else ""))
    dem = sorted(cl["statistics"] - X)
    if dem:
        print("   DEMANDED: %s" % ", ".join(str(c) for c in dem))
    print()
    print("   THE GRAVITY SPLIT: %d of %d bounds have gravity in them --" 
          % (len(gravitational()), len(BOUNDS)))
    print("     %s" % ", ".join(gravitational()))
    print("   The other six are statements about quantum field theory on a fixed")
    print("   background. That division is invisible from inside the")
    print("   energy-condition family, where every bound is just a value of B.")
    print()
    print("   SATURATION IS A PROPERTY OF THE BOUND, NOT OF THE CONDITION.")
    print("   Known saturated: %s." % ", ".join(saturated()))
    print("   That is which walls have already been reached, and it is the")
    print("   difference between a bound that is a limit and one that is an")
    print("   estimate. FORD-ROMAN IS SATURATED, BY CASIMIR -- which is why no")
    print("   material choice crosses it and why the negative-energy census turns")
    print("   on it.")
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

    print("bounds selftest")
    X = cells()
    chk("eight named bounds", len(BOUNDS), 8)
    chk("seven distinct cells", len(X), 7)
    chk("five coordinates", len(COORDS), 5)
    chk("no coordinate is constant",
        all(len({c[i] for c in X}) > 1 for i in range(5)), True)

    chk("one cell collision, and it is the two QEIs", collisions(),
        [("Fewster-Osterbrink QEI", "SNEC")])
    chk("four bounds are known saturated", len(saturated()), 4)
    chk("and Ford-Roman is one of them", "Ford-Roman QI" in saturated(), True)
    chk("two bounds have gravity in them", len(gravitational()), 2)
    chk("and they are the two entropy bounds",
        sorted(gravitational()), ["Bekenstein", "Bousso covariant"])
    chk("every entropy bound is gravitational",
        all(r[4] == 1 for r in BOUNDS if r[1] == 2), True)
    chk("and no non-entropy bound is",
        any(r[4] == 1 for r in BOUNDS if r[1] != 2), False)

    chk("only QNEC has a state-dependent RHS",
        [r[0] for r in BOUNDS if r[3] == 1], ["QNEC"])
    chk("and it is the only one whose bound is a state functional",
        [r[0] for r in BOUNDS if r[2] == 2], ["QNEC"])

    # B is the SAME ladder as the energy-condition family's, deliberately.
    import necindex
    chk("B reuses the seated bound ladder's values",
        {r[2] for r in BOUNDS} <= {c[4] for c in necindex.cells()}, True)

    cl, _ = hlaw.closures(X)
    chk("statistics closes the bounds index", len(cl["statistics"]) - len(X), 0)
    chk("and it is the ONLY language that does",
        [L for L in hlaw.LANGS if len(cl[L]) == len(X)], ["statistics"])

    # WHERE IT LANDS ONE LEVEL UP. Pinned here as well as in the master index's
    # own module, because a coordinate change in THIS file would move it.
    import master
    chk("shape is 5 coordinates in a box of 72", master.shape(X)[:2], (5, 72))
    chk("density band 1 (5-30%)", master.master_cell(X)[4], 1)
    chk("IT OCCUPIES THE CELL THE MASTER INDEX DEMANDED AT EIGHT",
        master.master_cell(X), master.DEMANDED_AT_EIGHT)
    print("bounds selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
