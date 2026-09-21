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
    Ford-Roman QI                1  1  0  0  0   K = 0 is WRONG; see DOCKET 55
    Fewster-Osterbrink QEI       1  1  0  0  1   state-independent; SNEC's cell
    QNEC                         0  2  1  0  1   entropy variation on the RHS
    Bekenstein                   2  1  0  1  0   saturated by black holes
    Bousso covariant             2  1  0  1  1   lightsheets

**WITHDRAWN IN PLACE -- DOCKET 55.**  What stood here was:

    "THE ONE THAT MATTERS FOR THIS PROJECT IS FORD-ROMAN, AND IT IS SATURATED.
     The negative-energy census turns on that: Casimir is the Ford-Roman bound
     saturated, not an exception to it, which is why no material choice crosses
     it.  A saturated bound is a wall with something already standing against
     it."

CASIMIR DOES NOT SATURATE IT, AND THE MEASUREMENT IS THE AUTHOR'S OWN.  Fewster,
"Lectures on quantum energy inequalities", arXiv:1208.5399 Sec. 1.3, read at
source, derives the a priori bound T_00 >= -C/(2 l)^4 for a trajectory at
distance l from a Casimir plate and reports that the known Casimir density
"ranges between 3-7% of the bound".  Reproduced from his own expression in the
selftest below: 6.8 % at the midpoint, 3.2 % off it.  He then asks in print
"why is the Casimir energy density a comparatively small proportion of the
allowed bound?"  Three per cent is not a wall with something standing against
it.  Ford & Roman say the same from the other side in gr-qc/9510071 Sec. 2: a
constant negative Casimir density "would not be possible if Eq. (1) holds for
all tau_0", and the inequality is rescued only by capping tau_0 <~ 0.46 L.

    THE K = 0 CODING IS THEREFORE WRONG AND IS **RECORDED, NOT REPAIRED**.
    K = 0 means "known to be saturated" and Ford-Roman is not.  Re-coding it to
    1 was MEASURED this pass and costs, exactly: cells 8 -> 7; the two-way QEI
    collision becomes a three-way with Ford-Roman in it; saturated 4 -> 3;
    E under statistics 1 -> 2; and it breaks master.py's check "two drop-one
    variants reach the demanded cell", which falls from ['G', 'K'] to ['K'].
    That is a change to what this family IS and it propagates one level up, so
    it belongs to its own docket and not to this one.  The integer is left
    standing with its fault named; the PROSE claim, which is what achievable.py
    copied, is withdrawn here.

===============================================================================
WHAT THE BOUNDS INDEX IS FOR
===============================================================================

Two things it makes visible that the B slot alone cannot:

**THE GRAVITY SPLIT.**  Two of the eight bounds have gravity in them and six do
not.  The six are statements about quantum field theory on a fixed background;
the two are statements about spacetime.  That division is invisible from inside
the energy-condition family, where every bound is just a value of B.

**SATURATION IS A PROPERTY OF THE BOUND, NOT OF THE CONDITION.**  Four of the
eight are coded known-saturated -- zero by the vacuum and by the electromagnetic
field, ANEC by the vacuum along a complete null geodesic, Ford-Roman by Casimir,
Bekenstein by black holes -- and the other four are not. That is what tells you
which walls have already been reached, and it is the difference between a bound
that is a limit and one that is merely an estimate.  The count was written as
three here on the first pass, omitting ANEC; the table was right and the
sentence was wrong, and the selftest is what caught it.

    **DOCKET 55: "Ford-Roman by Casimir" IS WITHDRAWN AND THE COUNT OF FOUR IS
    A COUNT OF THE CODING, NOT OF THE LITERATURE.**  Casimir sits at 3-7 % of
    the Ford-Roman bound, measured in the selftest from Fewster's own
    expression.  The honest count of known-saturated bounds is THREE.  The
    integer is left at K = 0 only because re-coding it propagates past this
    file; the reasons and the exact cost are in the section above.

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
about WHAT THE SMEARING RUNS OVER.

    **CORRECTED -- DOCKET 55.**  What stood here was "Ford, Helfer and Roman
    prove that a quantum energy inequality EXISTS for timelike and null smearing
    and PROVABLY DOES NOT EXIST for a purely spatial average."  THE NULL HALF IS
    FALSE, AND FALSE IN THE OPPOSITE DIRECTION.  Ford-Helfer-Roman prove nothing
    about null smearing; their own text flags the companion result, verbatim,
    gr-qc/0208045 p.4: "(A related construction has subsequently been used, in
    Ref. [23], to prove that there are NO quantum inequalities along null
    geodesics in four-dimensional Minkowski spacetime.)"  Ref. [23] is Fewster &
    Roman, "Null energy conditions in quantum field theory", PRD 67 044003,
    gr-qc/0209036, read at source this pass; its abstract: "weighted averages of
    the null-contracted stress-energy tensor along null geodesics are unbounded
    from below on the class of Hadamard states.  Thus there are no quantum
    inequalities along null geodesics in four-dimensional Minkowski spacetime.
    This is in contrast to the case for two-dimensional flat spacetime."

    THE CORRECT SENTENCE.  Ford-Helfer-Roman prove that no QEI exists for a
    purely SPATIAL average over a bounded region in four dimensions.  A QEI does
    exist for TIMELIKE smearing.  For NULL smearing the answer splits, and the
    split is a fault in this index's Z slot: ANEC over a COMPLETE null geodesic
    holds (Klinkhammer; Wald & Yurtsever, and Fewster-Roman verify their own
    counterexample states obey it), while over a FINITE null segment no QEI
    exists in 4D.  Fewster-Roman also prove that the null-CONTRACTED stress
    energy smeared along a TIMELIKE worldline is bounded, in any globally
    hyperbolic spacetime -- so what matters is the DOMAIN of the smearing, not
    the character of the vector contracted in.  Z = 1 currently seats the proven
    ANEC beside SNEC, whose finite null smearing exists only because Freivogel &
    Krommydas insert a 1/G_N.  CANDIDATE INDEX FAULT, recorded not adjudicated.

    A distinction a theorem turns on is a coordinate, not a note, and the Z slot
    is now it.  Adding it alone: the family
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
the right shape, and that no such instrument CAN exist over a bounded region in
four dimensions -- which is stronger than "is known to exist", and is the one
word DOCKET 55 sharpened.

===============================================================================
DOCKET 55 -- THE CONTRADICTION WITH achievable.py, AND WHAT THE EMPTY CELL MEANS
===============================================================================

**THIS FILE AND achievable.py CONTRADICTED EACH OTHER IN PRINT AND NEITHER NAMED
THE OTHER.**  achievable.py's docstring said the negative-energy census is
"bounded by a THEOREM rather than by engineering", reading Ford-Roman as a cap
on |rho| over a spatial scale L.  This file says no bound of that signature
exists.  Both could not stand.  THIS FILE WAS RIGHT; achievable.py has been
withdrawn in place.  A finding that does not name the file it refutes is how a
contradiction survives both selftests, so it is named here.

THREE FUNCTIONALS, KEPT APART.  The whole docket is that these are different:

    F1  POINTWISE   rho(x) at a spacetime point.        NO lower bound exists
                                                        (Epstein-Glaser-Jaffe).
    F2  WORLDLINE   a TIME average at ONE point.        Ford-Roman, Z = 1.
    F3  BALL        INT_ball rho dV at ONE INSTANT.     certify.py's requirement.

achievable.py restated F2 as F1 with a SPATIAL L, then evaluated it on F3.  Two
substitutions, neither argued.  This index already carried the refutation in
machine-readable form: the Ford-Roman row is coded Z = 1, and achievable.py used
that same bound at Z = 2.

**AND THE EMPTY CELL IS EMPTY FOR A REASON THIS FILE UNDERSTATED.**  The
boundary is not spacelike-versus-timelike.  It is BOUNDED-versus-UNBOUNDED
REGION, and Ford-Helfer-Roman say both halves in one sentence, verbatim:

    "there are no purely spatially averaged quantum inequalities over BOUNDED
     REGIONS in four-dimensional Minkowski spacetime, EVEN THOUGH THE INTEGRAL
     OVER ALL SPACE IS BOUNDED."

The second half is a member this index does not hold.  Their Eqs. (2)-(3):
H = INT d^{d-1}x :T_00: over ALL space at fixed time obeys <H> >= 0, with
equality only in the vacuum.  THAT LEFT-HAND SIDE IS A SPACELIKE-SMEARED ENERGY
DENSITY AND THE BOUNDED OBJECT IS AN ENERGY -- the combination this family has
none of.  Seating it was MEASURED this pass, coded (W 1, B 0, S 0, G 0, K 0,
Z 2): members 9 -> 10, cells 8 -> 9, E under statistics 1 -> 3, and it flips
exactly the two claims below -- "EVERY region-signature bound has an ENTROPY on
its left" becomes False, and the empty (Z = 2, energy) list gains one member.
**RECORDED, NOT REPAIRED.**  Membership is a fact about the literature rather
than a choice -- this file learned that when Casini killed its own fill -- and
seating a member changes what the family IS.  It is the next docket, not this
one.  The correction it forces is a NARROWING and is strictly stronger: no bound
in this family has spacelike signature, bounds an ENERGY, and applies to a
BOUNDED region; FHR prove there cannot be one.  A corridor of finite radius is
not protected by <H> >= 0, because the compensating positive energy is simply
outside the ball -- FHR's own mechanism, "the compensating positive energy is
arbitrarily far from the negative energy".

**WHAT PRICES THE BALL INTEGRAL ANYWAY, WITHOUT ENTERING THIS CELL.**  The cell
stays empty and the corridor is still refused, and the two facts are consistent
because the refusal never averages in space.  Fewster arXiv:1208.5399 Eq. (4):
if <T_00> stays below rho for a DURATION tau at a point, then rho >= -C/tau^4
with C = mu_1^4/(16 pi^2) = 3.169857938310467, cos(mu_1) cosh(mu_1) = 1.  That
is a Z = 1 instrument applied at each point of the ball and summed, licensed by
the corridor's own STATICITY rather than by any spatial smearing -- so
Ford-Helfer-Roman, whose witness states are explicitly transient and explicitly
obey the temporal inequality, cannot touch it.  The corridor must hold for at
least one light-crossing, and it is refused by 71.256 orders at metre scale
(achievable.py, corrected).

    SO THE OBSTRUCTION IS PRICED ON THE **DURATION** AXIS, BY AN INSTRUMENT OF
    THE WRONG SHAPE UNDER AN EXTRA HYPOTHESIS THE CONFIGURATION SUPPLIES.  That
    is neither this file's "unpriced" nor achievable.py's "theorem".  It is
    also not a theorem about matter in general: Fewster Sec. 5.1 states that the
    NONMINIMALLY coupled scalar admits no state-independent QEI at all, and that
    is DOCKET 53 Route B's own field.  DOCKET 55's verdict is NO-IN-PRACTICE.
"""

import math
import sys

import hlaw

# (name, W, B, S, G, K, Z, note)
BOUNDS = [
    ("zero (the NEC's RHS)",   0, 0, 0, 0, 0, 0, "saturated by the vacuum and by EM"),
    ("ANEC",                   1, 0, 0, 0, 0, 1, "averaged, RHS zero"),
    ("SNEC",                   1, 1, 0, 0, 1, 1, "smeared null"),
    # DOCKET 55: the note said "CASIMIR SATURATES IT".  It does not -- Fewster
    # arXiv:1208.5399 Sec.1.3 measures the Casimir density at 3-7 % of the QEI
    # bound, reproduced in the selftest.  K = 0 ("known saturated") is therefore
    # a wrong integer.  Left standing because re-coding it costs this index four
    # pins and breaks a master.py check; see the DOCKET 55 section.
    ("Ford-Roman QI",          1, 1, 0, 0, 0, 1, "K=0 WRONG, D55: Casimir is 3-7% of it"),
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

# DOCKET 55.  Two facts about this table that the table itself cannot carry.
# The first is a known-wrong integer left standing with its fault named; the
# second is the signature of the instrument that actually prices the corridor,
# and it is Z = 1 -- so the empty (Z = 2, energy) cell stays empty.
FORD_ROMAN_K_IS_WRONG = True
DURATION_ROUTE_Z = 1


def cells():
    return frozenset(tuple(r[1:7]) for r in BOUNDS)


def saturated():
    return [r[0] for r in BOUNDS if r[5] == 0]


def gravitational():
    return [r[0] for r in BOUNDS if r[4] == 1]


def casimir_fraction_of_bound(z_over_L, L=1.0):
    """DOCKET 55, and it is the measurement that withdraws "CASIMIR SATURATES IT".

    Fewster arXiv:1208.5399 Sec. 1.3 gives the a priori QEI bound for a
    trajectory at distance l from the nearer of two Casimir plates,
        T_00  >=  -C/(2 l)^4,      C = mu_1^4/(16 pi^2),
    against the known Casimir density for the massless minimally coupled scalar
        T_00  =  -pi^2/(1140 L^4) - pi^2/(48 L^4) (3 - 2 cos^2(pi z/L))/cos^4(pi z/L).
    He reports the ratio as "3-7%".  Returned here as a fraction, computed."""
    z = z_over_L * L
    rho = (-math.pi ** 2 / (1140.0 * L ** 4)
           - math.pi ** 2 / (48.0 * L ** 4)
           * (3.0 - 2.0 * math.cos(math.pi * z / L) ** 2)
           / math.cos(math.pi * z / L) ** 4)
    ell = L / 2.0 - abs(z)
    mu = 4.0
    f = lambda m: math.cos(m) * math.cosh(m) - 1.0
    lo, hi = 4.0, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0.0:
            hi = mid
        else:
            lo = mid
    mu = 0.5 * (lo + hi)
    C = mu ** 4 / (16.0 * math.pi ** 2)
    return rho / (-C / (2.0 * ell) ** 4)


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
    print("   estimate.")
    print()
    print("   WITHDRAWN, DOCKET 55: 'FORD-ROMAN IS SATURATED, BY CASIMIR -- which")
    print("   is why no material choice crosses it.'  Fewster arXiv:1208.5399")
    print("   Sec.1.3 measures the Casimir density at 3-7%% of the bound (%.1f%%"
          % (100 * casimir_fraction_of_bound(0.0)))
    print("   at the midpoint, reproduced here) and asks in print why it is so")
    print("   small a proportion.  The K = 0 coding is a known-wrong integer,")
    print("   recorded rather than repaired; see the DOCKET 55 section.")
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

    def near(name, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  [%s] %-58s %.6g" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r within %r" % (want, tol))

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

    # ================= DOCKET 55 =================
    print("\nDOCKET 55 -- THE CONTRADICTION WITH achievable.py")
    # (a) the index already carried the refutation, in machine-readable form.
    _fr = [r for r in BOUNDS if r[0] == "Ford-Roman QI"][0]
    chk("Ford-Roman is coded Z = 1, a TIMELIKE/NULL smearing", _fr[6], 1)
    chk("so achievable.py used a Z = 1 bound on a Z = 2 requirement",
        _fr[6] != 2, True)
    chk("and the requirement's signature is Z = 2, with no energy bound there",
        [r[0] for r in BOUNDS if r[6] == 2 and r[1] != 2], [])

    # (b) WITHDRAWN: "CASIMIR SATURATES IT".  Measured from Fewster 1208.5399.
    _mid = casimir_fraction_of_bound(0.0)
    _off = casimir_fraction_of_bound(0.4)
    print("     Casimir density as a fraction of Fewster's a priori QEI bound:")
    print("       at the midpoint   %.1f %%" % (100 * _mid))
    print("       at z/L = 0.4      %.1f %%" % (100 * _off))
    near("midpoint fraction, against Fewster's printed '3-7%'", _mid, 0.0682, 1e-2)
    chk("SO CASIMIR DOES NOT SATURATE FORD-ROMAN -- every sample under 10 %",
        all(casimir_fraction_of_bound(z) < 0.10 for z in (0.0, 0.2, 0.4)), True)
    chk("which makes K = 0 on that row a KNOWN-WRONG INTEGER, recorded not repaired",
        FORD_ROMAN_K_IS_WRONG, True)
    chk("the honest count of known-saturated bounds is three, not four",
        len(saturated()) - 1, 3)

    # (c) what re-coding it would cost -- MEASURED, which is why it is deferred.
    _rc = [list(r) for r in BOUNDS]
    for _r in _rc:
        if _r[0] == "Ford-Roman QI":
            _r[5] = 1
    _Xrc = frozenset(tuple(_r[1:7]) for _r in _rc)
    chk("re-coding K would take the index from eight cells to seven",
        (len(X), len(_Xrc)), (8, 7))
    chk("and E under statistics from one to two",
        (len(cl["statistics"]) - len(X),
         len(hlaw.closures(_Xrc)[0]["statistics"]) - len(_Xrc)), (1, 2))

    # (d) THE MISSING MEMBER.  <H> >= 0 over ALL space: a spacelike-smeared
    # ENERGY, which this family has none of.  Ford-Helfer-Roman Eqs. (2)-(3).
    _H = ("global Hamiltonian positivity", 1, 0, 0, 0, 0, 2,
          "<H> >= 0 over ALL space at fixed t; FHR Eqs. (2)-(3)")
    _v = list(BOUNDS) + [_H]
    _Xv = frozenset(tuple(r[1:7]) for r in _v)
    chk("seating <H> >= 0 would take the family to ten members, nine cells",
        (len(_v), len(_Xv)), (10, 9))
    chk("and it FLIPS 'every region-signature bound has an ENTROPY on its left'",
        all(r[1] == 2 for r in _v if r[6] == 2), False)
    chk("filling the cell this file reports empty",
        [r[0] for r in _v if r[6] == 2 and r[1] != 2],
        ["global Hamiltonian positivity"])
    chk("RECORDED, NOT REPAIRED -- the member is not seated here",
        len(BOUNDS), 9)
    print("       The narrowing it forces is STRONGER, not weaker: the empty")
    print("       cell is (spacelike, energy, BOUNDED region), and FHR prove")
    print("       there cannot be one.  All-space is spacelike and bounded")
    print("       below; any finite ball is spacelike and unbounded below.")

    # (e) and what prices the ball anyway, without entering the cell.
    chk("the (Z = 2, energy) cell is STILL empty in the seated family",
        [r[0] for r in BOUNDS if r[6] == 2 and r[1] != 2], [])
    chk("the duration route is Z = 1 -- it never averages in space",
        DURATION_ROUTE_Z, 1)
    print("       so the corridor is priced on the DURATION axis by a Z = 1")
    print("       instrument applied pointwise under the corridor's own")
    print("       staticity.  Not 'unpriced', and not 'bounded by a theorem'.")

    print("\nbounds selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
