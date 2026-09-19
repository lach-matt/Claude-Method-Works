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
    Z  SMEARING SIGNATURE   0 pointwise
                            1 timelike or null   -- a QEI exists
                            2 spacelike / region -- FORD-HELFER-ROMAN PROVE
                                                    NO QEI EXISTS

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
CORRECTED: THE FILL DOES NOT SURVIVE COMPLETING THE FAMILY
===============================================================================

At eight seated indexes the master index demanded exactly one cell,
(1, 1, 0, 2, 1).  THIS FILE, AS FIRST WRITTEN, OCCUPIED IT EXACTLY -- seven
cells, five coordinates, box 72, density 9.7 %, closed by `statistics` alone --
and seating it returned the master index to closure.  That was reported with two
caveats: the demanded cell was on the record beforehand, so it was not a blind
prediction, and the fill is banding-dependent, holding in 10 of 40 bandings.

    **BOTH CAVEATS WERE TRUE AND NEITHER WAS THE ONE THAT MATTERED.  THE FILL
    DOES NOT SURVIVE COMPLETING THIS FAMILY, AND TWO SEPARATE COMPLETIONS KILL
    IT INDEPENDENTLY.**

**ONE: A COORDINATE WAS MISSING, AND A THEOREM MAKES IT LOAD-BEARING.**  The W
slot says WHAT is bounded -- pointwise, smeared, entropy -- and says nothing
about WHAT THE SMEARING RUNS OVER.  Ford, Helfer and Roman prove that a quantum
energy inequality EXISTS for timelike and null smearing and PROVABLY DOES NOT
EXIST for a purely spatial average.  A distinction a theorem turns on is a
coordinate, not a note, and the Z slot is now it.  Adding it alone: the family
still closes under `statistics`, but its master cell moves to (1, 1, 0, 2, 0)
and THE DEMAND IS NO LONGER FILLED.

**TWO: A MEMBER WAS MISSING.**  Casini's relative-entropy bound, dS_A <= d<H_A>
(arXiv:0804.2182; Blanco and Casini, PRL 111 221601), is a published bound of
exactly the kind this family seats -- an entropy bounded by a modular energy,
the same species as Bekenstein and QNEC, both of which were already here.  It
was simply not seated.  Adding IT alone, without the Z slot: the family STOPS
CLOSING, E = 2 under statistics, and the master cell moves to (0, 0, 0, 2, 1).
THE DEMAND IS NOT FILLED EITHER WAY.

    SO THE FILL RESTED ON THE FAMILY BEING EXACTLY THOSE EIGHT MEMBERS IN
    EXACTLY THOSE FIVE COORDINATES.  It was fragile to MEMBERSHIP, not only to
    banding, and membership is a fact about the literature rather than a choice.

**AND SEATING CASINI COSTS THIS FILE FOUR OF ITS OWN CLAIMS**, every one of
which turns out to have been a coincidence of the eight:

    "every entropy bound is gravitational"          FALSE -- Casini has no G
    "the two gravitational bounds are exactly the
     two entropy bounds"                            FALSE -- there are three
                                                    entropy bounds now
    "only QNEC has a state-dependent RHS"           FALSE -- Casini too
    "statistics closes the bounds index"            FALSE -- E = 2

Recorded, not repaired: the claims are withdrawn where they fail and the pins
below now assert the corrected values.

===============================================================================
WHAT THE SMEARING SIGNATURE SHOWS, AND IT IS THE USEFUL PART
===============================================================================

The Z slot splits the nine two / four / three:

    Z = 0  pointwise               zero, QNEC
    Z = 1  timelike or null        ANEC, SNEC, Ford-Roman, Fewster-Osterbrink
    Z = 2  spacelike / region      Casini, Bekenstein, Bousso

    AND THE SPLIT IS NOT THE GRAVITY SPLIT.  All three region bounds have W = 2,
    an ENTROPY on the left; only two of them have gravity in them.

Which gives the gap its exact shape.  certify.py's requirement is a VOLUME
INTEGRAL OF rho OVER A BALL -- spacelike signature, energy density bounded.
Read down the two columns:

    every bound whose left-hand side is an ENERGY DENSITY has Z = 0 or 1
    every bound with Z = 2 has an ENTROPY on its left-hand side

    THERE IS NO BOUND IN THIS FAMILY WHOSE SMEARING SIGNATURE MATCHES THE
    REQUIREMENT AND WHOSE BOUNDED OBJECT IS AN ENERGY.

That is what certify.py meant by "no standard QI bounds it directly", stated as
a property of the index rather than as a remark, and Ford-Helfer-Roman is why it
is a theorem rather than a gap in anyone's reading.  IT DOES NOT WEAKEN THE
OBSTRUCTION.  It says the obstruction has never been priced by an instrument of
the right shape, and that no such instrument is known to exist.
"""

import sys

import hlaw

# (name, W, B, S, G, K, Z, note)
BOUNDS = [
    ("zero (the NEC's RHS)",   0, 0, 0, 0, 0, 0, "saturated by the vacuum and by EM"),
    ("ANEC",                   1, 0, 0, 0, 0, 1, "averaged, RHS zero"),
    ("SNEC",                   1, 1, 0, 0, 1, 1, "smeared null"),
    ("Ford-Roman QI",          1, 1, 0, 0, 0, 1, "CASIMIR SATURATES IT"),
    ("Fewster-Osterbrink QEI", 1, 1, 0, 0, 1, 1, "state-independent; shares SNEC's cell"),
    ("QNEC",                   0, 2, 1, 0, 1, 0, "entropy variation on the RHS"),
    ("Casini (relative entropy)",
                               2, 2, 1, 0, 1, 2, "dS_A <= d<H_A>; SEATED LATE, and "
                                                 "it costs this file four claims"),
    # DOCKET 4: G was 1. The slot's own rule is "a G or an area appears" and
    # S <= 2 pi R E has neither; Bousso states in print (hep-th/0402058) that
    # the bound "does not contain Newton's constant" and "remains nontrivial
    # when gravity is turned off completely"; and the black-hole SATURATION
    # that motivated G = 1 is already carried by K = 0. Coding it twice made
    # G stop being a coordinate. THIS KILLS BOTH K1 CELLS OF THIS INDEX.
    ("Bekenstein",             2, 1, 0, 0, 0, 2, "saturated by black holes; G re-coded 1->0, DOCKET 4"),
    ("Bousso covariant",       2, 1, 0, 1, 1, 2, "lightsheets"),
]
COORDS = ("W", "B", "S", "G", "K", "Z")


def cells():
    return frozenset(tuple(r[1:7]) for r in BOUNDS)


def saturated():
    return [r[0] for r in BOUNDS if r[5] == 0]


def gravitational():
    return [r[0] for r in BOUNDS if r[4] == 1]


def collisions():
    seen = {}
    for r in BOUNDS:
        seen.setdefault(tuple(r[1:7]), []).append(r[0])
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
    print("   %-26s %2s %2s %2s %2s %2s %2s  %s" % ("bound", *COORDS, "note"))
    for nm, W, B, S, G, K, Z, note in BOUNDS:
        print("   %-26s %2d %2d %2d %2d %2d %2d  %s"
              % (nm, W, B, S, G, K, Z, note))
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
    chk("nine named bounds -- Casini seated late", len(BOUNDS), 9)
    chk("eight distinct cells", len(X), 8)
    chk("six coordinates -- the smearing signature is one of them", len(COORDS), 6)
    chk("no coordinate is constant",
        all(len({c[i] for c in X}) > 1 for i in range(len(COORDS))), True)

    chk("one cell collision, and it is the two QEIs", collisions(),
        [("Fewster-Osterbrink QEI", "SNEC")])
    chk("four bounds are known saturated", len(saturated()), 4)
    chk("and Ford-Roman is one of them", "Ford-Roman QI" in saturated(), True)
    # DOCKET 4 moved this: Bekenstein re-coded G 1 -> 0, so ONE bound carries
    # gravity and it is Bousso, which genuinely has A/4G in its statement.
    chk("ONE bound has gravity in it, and it is Bousso", len(gravitational()), 1)
    # WITHDRAWN. Each of the next three was a coincidence of the eight members
    # first seated, and seating Casini -- a published bound of exactly the kind
    # this family holds -- refutes all three. The corrected values are pinned.
    chk("'every entropy bound is gravitational' is FALSE",
        all(r[4] == 1 for r in BOUNDS if r[1] == 2), False)
    chk("there are THREE entropy bounds and ONE gravitational one",
        (len([r for r in BOUNDS if r[1] == 2]), len(gravitational())), (3, 1))
    # DOCKET 4 again, and it doubles the count: TWO of the three entropy bounds
    # now carry no Newton constant in their statements.
    chk("TWO entropy bounds carry no Newton constant",
        sorted(r[0] for r in BOUNDS if r[1] == 2 and r[4] == 0),
        ["Bekenstein", "Casini (relative entropy)"])
    chk("'only QNEC has a state-dependent RHS' is FALSE",
        [r[0] for r in BOUNDS if r[3] == 1],
        ["QNEC", "Casini (relative entropy)"])

    # B is the SAME ladder as the energy-condition family's, deliberately.
    import necindex
    chk("B reuses the seated bound ladder's values",
        {r[2] for r in BOUNDS} <= {c[4] for c in necindex.cells()}, True)

    cl, _ = hlaw.closures(X)
    # ALSO WITHDRAWN, and this is the one that mattered.
    # E was 2 with Bekenstein at G = 1. DOCKET 4 took it to 1 -- the re-coding
    # moves the index CLOSER to closing without closing it, and it is what kills
    # both K1 cells of this family.
    chk("'statistics closes the bounds index' is FALSE -- E is 1, not 0",
        len(cl["statistics"]) - len(X), 1)
    chk("nothing closes it now",
        [L for L in hlaw.LANGS if len(cl[L]) == len(X)], [])

    # ---- THE SMEARING SIGNATURE, and the gap it gives an exact shape
    Z = {0: [], 1: [], 2: []}
    for r in BOUNDS:
        Z[r[6]].append(r[0])
    chk("the signature splits the nine two / four / three",
        [len(Z[0]), len(Z[1]), len(Z[2])], [2, 4, 3])
    chk("and the region bounds are not the gravitational ones",
        sorted(Z[2]) == sorted(gravitational()), False)
    chk("EVERY region-signature bound has an ENTROPY on its left",
        all(r[1] == 2 for r in BOUNDS if r[6] == 2), True)
    chk("and every energy-density bound is pointwise or timelike/null",
        all(r[6] in (0, 1) for r in BOUNDS if r[1] != 2), True)
    chk("SO NO BOUND HERE MATCHES THE REQUIREMENT'S SIGNATURE AND BOUNDS AN ENERGY",
        [r[0] for r in BOUNDS if r[6] == 2 and r[1] != 2], [])

    # ---- WHERE IT LANDS ONE LEVEL UP, AND THE FILL IS GONE
    import master
    chk("shape is 6 coordinates in a box of 216", master.shape(X)[:2], (6, 216))
    chk("THE DEMANDED-CELL FILL DOES NOT SURVIVE COMPLETING THE FAMILY",
        master.master_cell(X) == master.DEMANDED_AT_EIGHT, False)
    chk("the master cell is now", master.master_cell(X), (0, 0, 0, 2, 0))
    # and EACH completion kills it independently -- measured, not asserted
    five = frozenset(tuple(r[1:6]) for r in BOUNDS)
    chk("seating Casini alone (five coords) already misses it",
        master.master_cell(five) == master.DEMANDED_AT_EIGHT, False)
    eight6 = frozenset(tuple(r[1:7]) for r in BOUNDS
                       if r[0] != "Casini (relative entropy)")
    chk("and adding the signature alone (eight members) also misses it",
        master.master_cell(eight6) == master.DEMANDED_AT_EIGHT, False)
    chk("and with the signature alone the family no longer closes either",
        len(hlaw.closures(eight6)[0]["statistics"]) - len(eight6), 1)
    # ---- DOCKET 4's CONSEQUENCE, pinned where the re-coding lives.
    import itertools as _it
    _ks = master.channel_sets()
    _cl, _box = hlaw.closures(X)
    _k1 = [c for c in _it.product(*_box)
           if _ks.index(frozenset(L for L in hlaw.LANGS if c not in _cl[L])) == 1]
    chk("THIS INDEX NOW HOLDS NO K1 CELL AT ALL -- it held two", _k1, [])
    # and the reversal is one integer, so the pin says which
    _rows = [list(r) for r in BOUNDS]
    for _r in _rows:
        if _r[0].startswith("Bekenstein"):
            _r[4] = 1
    _back = frozenset(tuple(_r[1:7]) for _r in _rows)
    _cl2, _box2 = hlaw.closures(_back)
    _k1b = [c for c in _it.product(*_box2)
            if _ks.index(frozenset(L for L in hlaw.LANGS if c not in _cl2[L])) == 1]
    chk("and putting Bekenstein back at G = 1 restores exactly two",
        _k1b, [(2, 1, 0, 0, 0, 2), (2, 1, 0, 0, 1, 2)])

    print("bounds selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
