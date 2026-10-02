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
                            1 timelike or null   -- a QEI exists for timelike
                                                    smearing; along a FINITE
                                                    null segment none does
                                                    (Fewster-Roman: the free
                                                    massless minimally coupled
                                                    scalar, 4D Minkowski) --
                                                    the CANDIDATE INDEX FAULT
                                                    below
                            2 spacelike / region -- FORD-HELFER-ROMAN PROVE NO
                                                    STATE-INDEPENDENT QEI
                                                    EXISTS over a bounded
                                                    region, for the free
                                                    massless minimally coupled
                                                    scalar in 4D Minkowski

    CORRECTED (DOCKET 67).  The Z gloss read "1 timelike or null -- a QEI
    exists" and "2 spacelike / region -- FORD-HELFER-ROMAN PROVE NO QEI
    EXISTS".  The first said of null smearing what holds over a complete
    geodesic (ANEC) and fails over a finite segment in 4D (Fewster-Roman
    gr-qc/0209036); the second dropped FHR's field, their state-independence
    and Minkowski space (gr-qc/0208045 abstract, p.9).  No integer moved.

B is deliberately the SAME ladder as the energy-condition family's B slot --
by how much negativity the bound licenses -- so the two indexes agree where they
overlap rather than each inventing a coding.

===============================================================================
THE MEMBERS
===============================================================================

    bound                        W  B  S  G  K   note
    zero (the NEC's own RHS)     0  0  0  0  0   saturated by vacuum and by EM
    ANEC                         1  0  0  0  0   the averaged bound, RHS zero
                                                 (K = 0: the vacuum, Minkowski)
    SNEC                         1  1  0  0  1   smeared null
    Ford-Roman QI                1  1  0  0  0   K = 0 is WRONG; see DOCKET 55
    Fewster-Osterbrink QEI       1  1  0  0  1   S = 0 is the xi = 0 cell; FO's
                                                 xi > 0 bound is state-dependent
    QNEC                         0  2  1  0  1   entropy variation on the RHS
    Bekenstein                   2  1  0  1  0   saturated by Schwarzschild, D = 4
    Bousso covariant             2  1  0  1  1   lightsheets; a conjecture

    This is the table AS FIRST SEATED -- eight members, five coordinates, and
    Bekenstein still at G = 1.  BOUNDS below is the record: nine members, the
    Z coordinate, and Bekenstein at G = 0 since DOCKET 4.  CORRECTED (DOCKET
    67): the notes read "state-independent; SNEC's cell" for Fewster-Osterbrink,
    "saturated by black holes" for Bekenstein and "lightsheets" alone for
    Bousso; the reasons are at the BOUNDS rows.  No integer moved.

**WITHDRAWN IN PLACE -- DOCKET 55.**  What stood here was:

    "THE ONE THAT MATTERS FOR THIS PROJECT IS FORD-ROMAN, AND IT IS SATURATED.
     The negative-energy census turns on that: Casimir is the Ford-Roman bound
     saturated, not an exception to it, which is why no material choice crosses
     it.  A saturated bound is a wall with something already standing against
     it."

CASIMIR DOES NOT SATURATE FEWSTER'S A PRIORI BOUND, AND THE CALCULATION IS THE
AUTHOR'S OWN.  Fewster,
"Lectures on quantum energy inequalities", arXiv:1208.5399 Sec. 1.3, read at
source, derives the a priori bound T_00 >= -C/(2 l)^4 for a trajectory at
distance l from a Casimir plate and reports that the known Casimir density --
of the massless minimally coupled scalar between Dirichlet plates, a
calculated vacuum density, not a measured one -- "ranges between 3-7% of the
bound".  Reproduced from his own expression in the selftest below: 6.7 % at
the midpoint, 3.2 % off it, on the scalar's pi^2/1440 constant term, which
this file now uses (6.8 % and 3.2 % on his printed pi^2/1140; the misprint is
a discrepancy, and '3-7%' holds on either).  (CORRECTED, DOCKET 67, on M's
ruling "address/correct/repair all figures": this read "6.8 % at the
midpoint, 3.2 % off it, on his printed pi^2/1140 (6.7 % and 3.2 % on the
scalar's pi^2/1440 ...)", the default having been the misprint.)  He then asks in print "why is the Casimir energy density a
comparatively small proportion of the allowed bound?"  The bound is built on
his Eq. (3), which he calls "known not to be optimal", so three per cent is of
THAT bound -- not of the unknown sharp bound, and not of Ford-Roman's
Lorentzian -3/(32 pi^2 tau_0^4).  Ford & Roman, gr-qc/9510071 Sec. 2, say
nothing about saturation: for one free massless minimally coupled real scalar
with a periodic identification, a constant negative Casimir density "would
not be possible if Eq. (1) holds for all tau_0", and their flat-space Eq. (1)
is met only by capping tau_0 <~ 0.46 L for a static observer (tau_0 <
0.42 L/gamma over all v, their Eq. (9)) -- and the cap is defined by
equality, so at the cap the density EQUALS that bound by construction.  Exact
QIs posed in the bounded spacetime itself are measured from its own vacuum
and need no cap (Pfenning gr-qc/9805037; Fewster-Teo gr-qc/9812032, as the
DOCKET 67 audit cites them).

    CORRECTED (DOCKET 67).  What stood here was "CASIMIR DOES NOT SATURATE IT,
    AND THE MEASUREMENT IS THE AUTHOR'S OWN" -- unqualified 'Casimir', for a
    Dirichlet-scalar result; 'measurement', for a calculation; and 'IT', the
    Ford-Roman bound, for Fewster's own -- and "Three per cent is not a wall
    with something standing against it.  Ford & Roman say the same from the
    other side ... the inequality is rescued only by capping tau_0 <~ 0.46 L."
    Non-saturation is not Ford-Roman's statement, the static-observer and
    single-scalar hypotheses were dropped, and 'only' holds for the flat
    Eq. (1) alone.  No verdict moved.

    THE K = 0 CODING IS THEREFORE WRONG AND IS **RECORDED, NOT REPAIRED**.
    K = 0 means "known to be saturated", and no source read shows Ford-Roman
    saturated: Ford & Roman claim no saturation (gr-qc/9607003), and
    Fewster's calculation refutes saturation of his own bound only -- an OPEN
    saturation is K = 1, 'not known'.  (CORRECTED, DOCKET 67: this read "and
    Ford-Roman is not", which no source read establishes.)  Re-coding it to
    1 was MEASURED this pass and costs, exactly: cells 8 -> 7; the two-way QEI
    collision becomes a three-way with Ford-Roman in it; saturated 4 -> 3;
    E under statistics 1 -> 2; and it breaks master.py's check "two drop-one
    variants reach the demanded cell", which falls from ['G', 'K'] to ['K'].
    That is a change to what this family IS and it propagates one level up, so
    it belongs to its own docket and not to this one.  The integer is left
    standing with its fault named; the PROSE claim, which is what achievable.py
    copied, is withdrawn here.

**DOCKET 67 NARROWS THE GROUND, AND IT IS RECORDED, NOT REPAIRED**
(key ford-roman-qi-and-fewster-casimir-fraction, NARROWED; the reopen
adjudicated REOPENS-NARROWER; recorded on M's ruling of 2026-10-02).  The
3-7 % above is of Fewster's OWN a priori Eq. (4) bound, which he calls known
not to be optimal -- not of the Ford-Roman bound, and not of the unknown SHARP
bound.  The withdrawal stays carried on four counts (W2 in the ledger):
saturation of Fewster's own bound (3.1964 % to 6.7028 %, on the correct
pi^2/1440 constant term); saturation across the slab of ANY bound of the form
-K/(2l)^4 (the ratio profile does not depend on K and falls by 2.097 from the
midplane to the plates); 'not an exception' against the uncapped Ford-Roman
Eq. (1) (a static negative density violates it above the cap); and 'known
saturated' (K = 0 stays WRONG: an OPEN saturation is K = 1, 'not known').
ONE READING OF THE PREMISE IS OPEN, NOT REFUTED: whether the midplane density of
the massless minimally coupled Dirichlet scalar saturates the unknown sharp
bound -C_s/(2l)^4.  The bracket is 6.7028 % to 100 %; 100 % needs
C_s = 0.212471 = C/14.919 AND Fewster's locality step -- the sharp Minkowski
constant holding inside the 2l window -- whose justification is his ref. [31],
Fewster-Pfenning math-ph/0602042, NAMED-NOT-READ (sharp_bound_reading()).
Saturation in Ford-Roman's CAPPED sense was never computed for that profile
(OPEN); where it was computed, for the periodic scalar of gr-qc/9510071, the
cap is defined by equality, so equality there holds by construction and is
evidence neither way.  The inference 'which is why no material choice crosses
it' is NOT reinstated: with its premise OPEN it is unsupported, and nothing
anti-warp comes back.  On M's ruling "Repair all" the prose of this file was
then CORRECTED in place (DOCKET 67 prose pass, each site marked); the K
integer, FORD_ROMAN_K_IS_WRONG and every pin are unchanged.

===============================================================================
WHAT THE BOUNDS INDEX IS FOR
===============================================================================

Two things it makes visible that the B slot alone cannot:

**THE GRAVITY SPLIT.**  One of the nine bounds has gravity in it -- Bousso, with
A/4G in its statement -- and eight do not.  The eight are statements about
quantum field theory on a given background, most proved only in Minkowski
space (ANEC fails on generic curved 4D backgrounds: Visser gr-qc/9409043;
Urban-Olum 0910.5925, re-derived by the DOCKET 67 audit); the one is a
statement about spacetime.  That division is invisible from inside the
energy-condition family, where every bound is just a value of B.

    CORRECTED (DOCKET 67).  What stood here was "Two of the eight bounds have
    gravity in them and six do not.  The six are statements about quantum
    field theory on a fixed background; the two are statements about
    spacetime."  The count was stale against this file's own coding since
    DOCKET 4 (Bekenstein G 1 -> 0) and Casini's seating, and 'a fixed
    background' was wider than what ANEC's proofs cover.

**SATURATION IS A PROPERTY OF THE BOUND, NOT OF THE CONDITION.**  Four of the
nine are coded known-saturated -- zero by the vacuum and by the electromagnetic
field, ANEC by the Minkowski vacuum along a complete null geodesic (in curved
space the conformal vacuum can give a negative ANEC integral: Urban-Olum
eq. 42, re-derived by the DOCKET 67 audit), Ford-Roman by Casimir, Bekenstein
by the Schwarzschild black hole in D = 4 (an extrapolation: the hole lies
outside the bound's weakly-self-gravitating class; Reissner-Nordstrom gives
r+/2M < 1 for Q != 0, Kerr's ratio depends on which R is taken, and D > 4
gives 2/(D-2), all computed by the DOCKET 67 audit) -- and the other five are
not. (CORRECTED, DOCKET 67: "Four of the eight ... ANEC by the vacuum ...
Bekenstein by black holes ... the other four are not.")  That is what tells you
which walls have already been reached, and it is the difference between a bound
that is a limit and one that is merely an estimate.  The count was written as
three here on the first pass, omitting ANEC; the table was right and the
sentence was wrong, and the selftest is what caught it.

    **DOCKET 55: "Ford-Roman by Casimir" IS WITHDRAWN AND THE COUNT OF FOUR IS
    A COUNT OF THE CODING, NOT OF THE LITERATURE.**  The Dirichlet scalar's
    Casimir density sits at 3-7 % of Fewster's own a priori Eq. (4) bound,
    computed in the selftest from his own expression; against the unknown
    sharp bound the midplane reading is OPEN (the DOCKET 67 paragraph above),
    and no source read shows Ford-Roman saturated.  The honest count of
    known-saturated bounds is THREE: it stands on K's definition, under which
    an OPEN saturation is 'not known'.  The integer is left at K = 0 only
    because re-coding it propagates past this file; the reasons and the exact
    cost are in the section above.
    CORRECTED (DOCKET 67): this read "Casimir sits at 3-7 % of the Ford-Roman
    bound, measured in the selftest" -- Fewster's bound relabelled
    'Ford-Roman', and a calculation called a measurement.

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
    gr-qc/0209036, read at source this pass; its abstract: "For the quantised,
    massless, minimally coupled real scalar field in four-dimensional Minkowski
    space, we show (by an explicit construction) that weighted averages of
    the null-contracted stress-energy tensor along null geodesics are unbounded
    from below on the class of Hadamard states.  Thus there are no quantum
    inequalities along null geodesics in four-dimensional Minkowski spacetime.
    This is in contrast to the case for two-dimensional flat spacetime, where
    such inequalities do exist."  (CORRECTED, DOCKET 67: the quotation began
    at "weighted averages" and ended at "flat spacetime." with no ellipsis,
    cutting the opening clause that is the field hypothesis.)

    THE CORRECT SENTENCE.  Ford-Helfer-Roman prove that no state-independent
    QEI exists for a purely SPATIAL average over a bounded region, for the free
    massless minimally coupled scalar in four-dimensional Minkowski space.  A
    QEI does exist for TIMELIKE smearing.  For NULL smearing the answer splits,
    and the split is a fault in this index's Z slot: ANEC over a COMPLETE null
    geodesic holds in Minkowski space for the free scalar on the states each
    proof covers (Klinkhammer, a dense set of Fock states; Wald & Yurtsever,
    whose general proof is in 2D curved spacetime and whose 4D result covers a
    restricted class of Hadamard states in Minkowski -- their note added in
    proof, as Visser gr-qc/9409043 quotes it, says ANEC fails for generic
    perturbations of Minkowski in 4D; and Fewster-Roman verify, by a formal
    limit, that their own counterexample states obey it), while over a FINITE
    null segment no QEI exists for the free massless minimally coupled scalar
    in 4D Minkowski.  Fewster-Roman also prove that the null-CONTRACTED stress
    energy smeared along a TIMELIKE worldline is bounded, in any globally
    hyperbolic spacetime, for the free minimally coupled Klein-Gordon field
    over Hadamard states, relative to a Hadamard reference state -- so, inside
    those hypotheses, what matters is the DOMAIN of the smearing, not the
    character of the vector contracted in (for xi != 0 no state-independent
    QEI exists: Fewster-Osterbrink 0708.2450).  CORRECTED (DOCKET 67): this
    sentence named no field, background or state class at any of its four
    claims, and cited Wald-Yurtsever as a 4D co-proof.  Z = 1 currently seats the proven
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
    "only QNEC has a state-dependent RHS"           FALSE -- Casini too, and
                                                    read at source Fewster-
                                                    Osterbrink as well (xi > 0;
                                                    DOCKET 67) -- the pin keeps
                                                    the coding's two
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
    an ENTROPY on the left; only one of them, Bousso, has gravity in it.

    CORRECTED (DOCKET 67).  This read "only two of them have gravity in them",
    stale against this file's own coding since DOCKET 4.  And Bousso's Z = 2
    is this index's coding of a bound stated on a NULL hypersurface (a
    light-sheet; the spacelike version fails, hep-th/9905177 p.6), which Z's
    own definition puts at 1.  The DOCKET 67 audit measured the re-coding
    Z 2 -> 1: cells stay 8, the split becomes two / five / two, and the Z = 2
    gravity list empties.  Recorded; the integer is unchanged.

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
the right shape, and that no state-independent such instrument CAN exist over a
bounded region for the free massless minimally coupled scalar in
four-dimensional Minkowski space -- which is stronger than "is known to exist",
and is the one word DOCKET 55 sharpened.  (CORRECTED, DOCKET 67: this read "no
such instrument CAN exist over a bounded region in four dimensions", dropping
FHR's field, their state-independence and Minkowski space.  For a
field-specific spatial bound -- a massive scalar, Maxwell, Dirac -- FHR prove
nothing, and such a bound would be an instrument AGAINST the warp.)

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

    F1  POINTWISE   rho(x) at a spacetime point.        Not nonnegative
                                                        (Epstein-Glaser-Jaffe,
                                                        Minkowski, zero vacuum
                                                        value); unbounded below
                                                        for free fields over
                                                        Hadamard states.
    F2  WORLDLINE   a TIME average at ONE point.        Ford-Roman, Z = 1.
    F3  BALL        INT_ball rho dV at ONE INSTANT.     certify.py's requirement.

achievable.py restated F2 as F1 with a SPATIAL L, then evaluated it on F3.  Two
substitutions, neither argued.  This index already carried the refutation in
machine-readable form: the Ford-Roman row is coded Z = 1, and achievable.py used
that same bound at Z = 2.  (CORRECTED, DOCKET 67: F1 read "NO lower bound exists
(Epstein-Glaser-Jaffe)".  EGJ as restated prove nonpositivity only, in
Minkowski space with zero vacuum expectation value; unboundedness below is the
free-field Hadamard result, not theirs.)

**AND THE EMPTY CELL IS EMPTY FOR A REASON THIS FILE UNDERSTATED.**  The
boundary is not spacelike-versus-timelike.  It is BOUNDED-versus-UNBOUNDED
REGION, and Ford-Helfer-Roman say both halves in one sentence, verbatim:

    "there are no purely spatially averaged quantum inequalities over BOUNDED
     REGIONS in four-dimensional Minkowski spacetime, EVEN THOUGH THE INTEGRAL
     OVER ALL SPACE IS BOUNDED."

The second half is a member this index does not hold.  Their Eqs. (2)-(3):
H = INT d^{d-1}x :T_00: over ALL space at fixed time obeys <H> >= 0, with
equality only in the vacuum -- for a quantum field in "boundary-free Minkowski
spacetime" (FHR p.2, quoted there as a known result).  With boundaries, energy
normal-ordered against the Minkowski vacuum can be negative: Casimir.
(CORRECTED, DOCKET 67: the boundary-free hypothesis was not stated.)  THAT LEFT-HAND SIDE IS A SPACELIKE-SMEARED ENERGY
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
BOUNDED region; FHR prove there cannot be a state-independent one for the free
massless minimally coupled scalar in 4D Minkowski space.  (CORRECTED, DOCKET
67: this read "FHR prove there cannot be one".  The S slot makes
state-independence load-bearing: FHR refute S = 0 only.  The DOCKET 67 audit
computed that in their own witness family a bound depending on the state only
through <H> also fails; general state-dependent spatial bounds stay OPEN as
far as FHR go.)  A corridor of finite radius is
not protected by <H> >= 0, because the compensating positive energy is simply
outside the ball -- FHR's own mechanism, "the compensating positive energy is
arbitrarily far from the negative energy".

**WHAT PRICES THE BALL INTEGRAL ANYWAY, WITHOUT ENTERING THIS CELL.**  The cell
stays empty and the corridor is still refused, and the two facts are consistent
because the refusal never averages in space.  Fewster arXiv:1208.5399 Eq. (4):
if <T_00> stays below rho for a DURATION tau at a point, then rho >= -C/tau^4
with C ~ 3.17 as he prints it.  The closed form C = mu_1^4/(16 pi^2) =
3.169857938310467, cos(mu_1) cosh(mu_1) = 1, is this tree's computation from
his clamped-eigenvalue description; he does not print it.  (CORRECTED, DOCKET
67: the closed form was credited to Eq. (4).)  That
is a Z = 1 instrument applied at each point of the ball and summed, licensed by
the corridor's own STATICITY rather than by any spatial smearing -- so
Ford-Helfer-Roman, whose witness states are explicitly transient and explicitly
obey the temporal inequality, cannot touch it.  The corridor must hold for at
least one light-crossing, and it is refused by 71.256 orders at metre scale
(achievable.py, corrected).

    SO THE OBSTRUCTION IS PRICED ON THE **DURATION** AXIS, BY AN INSTRUMENT OF
    THE WRONG SHAPE UNDER AN EXTRA HYPOTHESIS THE CONFIGURATION SUPPLIES.  That
    is neither this file's "unpriced" nor achievable.py's "theorem".  It is
    also not a theorem about matter in general: Fewster Sec. 5.1 reports
    (Fewster-Osterbrink) that for the massless scalar NONMINIMALLY coupled with
    xi > 0, in 4D Minkowski space, the smeared energy density is unbounded
    below over states -- in this file's words, no state-independent QEI at
    all -- and that field, massless at xi = 1/6, is DOCKET 53 Route B's own,
    though Route B's background is curved and the non-existence is proved
    only in Minkowski space.  (CORRECTED, DOCKET 67: this read "Fewster Sec.
    5.1 states that the NONMINIMALLY coupled scalar admits no
    state-independent QEI at all" -- a paraphrase given as his wording, the
    words 'state-independent QEI' being Sec. 5.2's, with the sign of xi,
    masslessness and Minkowski space dropped.  The DOCKET 67 audit computed
    that the argument also carries to xi < 0 for the massless field in 4D
    Minkowski; no source read states it.)  DOCKET 55's verdict is
    NO-IN-PRACTICE.
"""

import math
import sys

import hlaw

# (name, W, B, S, G, K, Z, note)
BOUNDS = [
    ("zero (the NEC's RHS)",   0, 0, 0, 0, 0, 0, "saturated by the vacuum and by EM"),
    # DOCKET 67: K = 0 here is the Minkowski vacuum's exact zero; in curved
    # space the conformal vacuum can give a negative ANEC integral.
    ("ANEC",                   1, 0, 0, 0, 0, 1, "averaged, RHS zero; K=0 in Minkowski"),
    ("SNEC",                   1, 1, 0, 0, 1, 1, "smeared null"),
    # DOCKET 55: the note said "CASIMIR SATURATES IT".  No source read shows
    # it -- Fewster arXiv:1208.5399 Sec.1.3 calculates the Dirichlet scalar's
    # Casimir density at 3-7 % of his own a priori bound, reproduced in the
    # selftest, and Ford & Roman claim no saturation.  K = 0 ("known
    # saturated") is therefore a wrong integer.  Left standing because
    # re-coding it costs this index four pins and breaks a master.py check;
    # see the DOCKET 55 section.
    # DOCKET 67: the note's VERDICT (K=0 WRONG) stands on K's own coding (OPEN
    # saturation is 'not known'); only its REASON is narrowed -- the 3-7% is
    # of Fewster's a priori Eq. (4) bound, not Ford-Roman's, and the
    # sharp-bound midplane reading is OPEN.  CORRECTED (DOCKET 67): the note
    # read "K=0 WRONG, D55: Casimir is 3-7% of it", and this comment said
    # "measures ... of the QEI bound".
    ("Ford-Roman QI",          1, 1, 0, 0, 0, 1, "K=0 WRONG (saturation not known); "
                                                 "D55/D67: Dirichlet Casimir is 3-7% "
                                                 "of Fewster's own bound"),
    # DOCKET 67, recorded: S = 0 / B = 1 is the cell of the MINIMALLY coupled
    # QEI (xi = 0: Fewster-Eveson 1998, Fewster 2000).  Fewster-Osterbrink's
    # own result (xi > 0) is state-dependent -- B = 2, S = 1 on this ladder --
    # and they prove no state-independent bound exists for xi in (0, 1/4].
    # The integers are unchanged; the collision pin below exists only because
    # of them.  CORRECTED (DOCKET 67): the note read "state-independent;
    # shares SNEC's cell".
    ("Fewster-Osterbrink QEI", 1, 1, 0, 0, 1, 1, "xi = 0 cell (FO's xi > 0 bound is "
                                                 "state-dependent); shares SNEC's cell"),
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
    # CORRECTED (DOCKET 67) -- the hypotheses the lines above dropped, no
    # integer moved.  Bousso says it of the bound "in its regime of
    # validity", weakly gravitating systems (M << R/G), and of the hbar-form
    # S <= 2 pi R E with hbar held fixed: in the l_Pl-form G appears, and
    # G -> 0 at fixed l_Pl sends the bound to 0.  E is the total energy of a
    # complete system and R the radius of a sphere circumscribing it (Page
    # 1804.10623 gives counterexamples when E leaves out the walls).  The
    # black-hole saturation K = 0 carries is Schwarzschild in D = 4, with
    # M/(R/G) = 1/2 -- outside that regime, and non-existent at G = 0 -- so
    # this one row pairs two regimes; inside the regime Bousso calls a
    # precisely saturating example "an important outstanding problem"
    # (p.10).  He also calls the bound's formulation unsettled (entropy
    # definition, the species problem; p.8); Casini's rigorous form is seated
    # separately.  And S = 0 / B = 1 is this index's coding of an RHS that
    # contains the system's energy (<K>, a state functional, in the proven
    # form): a recorded discrepancy, not graded.
    ("Bekenstein",             2, 1, 0, 0, 0, 2, "saturated by Schwarzschild (D=4), "
                                                 "outside its weak-gravity regime; "
                                                 "G re-coded 1->0, DOCKET 4"),
    # DOCKET 67, recorded, no integer moved.  Bousso's covariant bound holds
    # under Einstein's equation, the dominant energy condition (1999; the
    # review: NEC plus causal energy flow), no naked singularities and an
    # approximately classical geometry -- so NEC-violating matter lies outside
    # the 1999 statement (only the weak-gravity BCFM version, 1404.5635, drops
    # the NEC) -- and Bousso calls it a conjecture with "no fundamental
    # derivation" (review p.19).  K = 1 is defensible but is not the source's
    # word: the review says it "can be saturated, but no example is known
    # where it is exceeded"; FMW show only 'within a factor of order unity'.
    # Re-coding K 1 -> 0 was measured by the DOCKET 67 audit: saturated 4 -> 5, cells stay 8.  Z = 2
    # is the coding of a null-hypersurface bound (see the Z-split section).
    # CORRECTED (DOCKET 67): the note read "lightsheets" alone.
    ("Bousso covariant",       2, 1, 0, 1, 1, 2, "lightsheets; a conjecture"),
]
COORDS = ("W", "B", "S", "G", "K", "Z")

# DOCKET 55.  Two facts about this table that the table itself cannot carry.
# The first is a known-wrong integer left standing with its fault named --
# wrong on K's own definition: no source read shows Ford-Roman saturated, and
# an OPEN saturation is 'not known' (DOCKET 67; CORRECTED, the reason once
# read 'Casimir does not saturate it'); the
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


#: CORRECTED (DOCKET 67, key ford-roman-qi-and-fewster-casimir-fraction, on M's
#: ruling "address/correct/repair all figures").  casimir_fraction_of_bound
#: defaulted to const_term=1140.0, Fewster's printed constant, and its selftest
#: pin 0.0682 (rel 1e-2) was keyed to it.  The constant term of the massless
#: minimally coupled Dirichlet scalar between plates a distance L apart is
#: pi^2/1440 (the audit re-derived it two ways: zeta mode sum, and the periodic
#: a = 2L image family; half the EM pi^2/720), so 1440 is the default now and
#: the printed 1140 survives only as an explicit argument, kept as a control.
#: Computed (python3 -c "import bounds as b; print(b.casimir_fraction_of_bound
#: (0.0, const_term=c))" for c = 1140, 1440): midpoint 0.067597448 on 1140,
#: 0.067028446 on 1440; at z/L = 0.4, 0.031975913 and 0.031975003.
SCALAR_DIRICHLET_CONST_TERM = 1440.0
FEWSTER_PRINTED_CONST_TERM = 1140.0     # his text layer's misprint, READ


def casimir_fraction_of_bound(z_over_L, L=1.0, const_term=SCALAR_DIRICHLET_CONST_TERM):
    """DOCKET 55, and it is the calculation that withdraws "CASIMIR SATURATES IT".

    Fewster arXiv:1208.5399 Sec. 1.3 gives the a priori QEI bound for a
    trajectory at distance l from the nearer of two Casimir plates,
        T_00  >=  -C/(2 l)^4,      C ~ 3.17 (closed form mu_1^4/(16 pi^2) ours),
    against the known Casimir density for the massless minimally coupled scalar
    between Dirichlet plates
        T_00  =  -pi^2/(1140 L^4) - pi^2/(48 L^4) (3 - 2 cos^2(pi z/L))/cos^4(pi z/L).
    He reports the ratio as "3-7%".  Returned here as a fraction, computed --
    of THIS bound, which rests on his Eq. (3), "known not to be optimal"; it
    says nothing of the unknown sharp bound, nor of Ford-Roman's.
    The constant term is printed 1140 above -- a misprint in his text layer, a
    discrepancy and not a refutation; the scalar's constant is pi^2/1440, half
    the EM pi^2/720 -- and the default is the scalar's 1440; pass
    const_term=1140 to reproduce his printed figure.  '3-7%' holds on either.
    (CORRECTED, DOCKET 67: 'measurement', the unqualified bound and the
    unflagged 1140.  CORRECTED again, DOCKET 67 figures pass: this read "and
    is used as printed by default, so the pinned figures do not move; DOCKET
    67's figures pass const_term=1440".)"""
    z = z_over_L * L
    rho = (-math.pi ** 2 / (const_term * L ** 4)
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


# DOCKET 67, key ford-roman-qi-and-fewster-casimir-fraction (NARROWED; the
# reopen adjudicated REOPENS-NARROWER; recorded on M's ruling of 2026-10-02).
# W2 stays WITHDRAWN on four carried counts; one reading of its premise is
# OPEN, not refuted, and the capped-sense saturation was never computed for
# the Dirichlet minimally coupled profile.  Nothing anti-warp is reinstated.
CAPPED_SENSE_SATURATION_DIRICHLET = "OPEN (never computed for that profile)"
FEWSTER_LOCALITY_STEP = ("Fewster's ref. [31], Fewster-Pfenning math-ph/0602042: "
                         "NAMED-NOT-READ")
NO_MATERIAL_CHOICE_CROSSES_IT_REINSTATED = False


def fewster_C():
    """C = mu_1^4/(16 pi^2), cos(mu_1) cosh(mu_1) = 1: this tree's closed form of
    the C ~ 3.17 Fewster prints at 1208.5399 Eq. (4), which he does not print
    in closed form (CORRECTED, DOCKET 67)."""
    f = lambda m: math.cos(m) * math.cosh(m) - 1.0
    lo, hi = 4.0, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0.0:
            hi = mid
        else:
            lo = mid
    return (0.5 * (lo + hi)) ** 4 / (16.0 * math.pi ** 2)


def sharp_bound_reading():
    """DOCKET 67's figures for W2, all computed here on the scalar's pi^2/1440:
    the midplane fraction of Fewster's own bound (the bracket's lower end, its
    upper end 100 %), its plate limit 1/(pi^2 C), the constant C_s a midplane
    saturation of a -C_s/(2l)^4 bound needs and C/C_s, the K-independent
    spread mid/plate, and, under C_s, the fraction at z = L/4."""
    C = fewster_C()
    mid = casimir_fraction_of_bound(0.0, const_term=1440.0)
    plate = 1.0 / (math.pi ** 2 * C)
    c_s = mid * C
    return {"bracket": (mid, 1.0), "plate": plate, "C_s": c_s, "C_over_C_s": C / c_s,
            "spread_mid_over_plate": mid / plate,
            "quarter_under_C_s": casimir_fraction_of_bound(0.25, const_term=1440.0) / mid}


def sharp_reading_status(c_s_known=None):
    """Does the midplane density saturate a -c_s/(2l)^4 bound?  With the sharp
    constant UNKNOWN (c_s_known None) the fraction ranges over the bracket
    [Fewster's own fraction, 100 %], which contains saturation: OPEN.  With a
    constant given, the fraction mid*C/c_s is computed: SATURATED at 1 (to
    1e-9), REFUTED below it."""
    sb = sharp_bound_reading()
    if c_s_known is None:
        lo, hi = sb["bracket"]
        return "OPEN" if lo < 1.0 <= hi else "REFUTED"
    f = sb["bracket"][0] * fewster_C() / c_s_known
    return "SATURATED" if abs(f - 1.0) < 1e-9 else ("REFUTED" if f < 1.0 else "VIOLATED")


#: DERIVED: the sharp constant is unknown, so the reading is OPEN, not refuted.
SHARP_BOUND_MIDPLANE_SATURATION = sharp_reading_status()


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
    print("   The other %d are statements about quantum field theory on a given"
          % (len(BOUNDS) - len(gravitational())))
    print("   background, most proved only in Minkowski space (ANEC fails on")
    print("   generic curved 4D backgrounds). That division is invisible from")
    print("   inside the energy-condition family, where every bound is a value of B.")
    print()
    print("   SATURATION IS A PROPERTY OF THE BOUND, NOT OF THE CONDITION.")
    print("   Known saturated: %s." % ", ".join(saturated()))
    print("   That is which walls have already been reached, and it is the")
    print("   difference between a bound that is a limit and one that is an")
    print("   estimate.")
    print()
    print("   WITHDRAWN, DOCKET 55: 'FORD-ROMAN IS SATURATED, BY CASIMIR -- which")
    print("   is why no material choice crosses it.'  Fewster arXiv:1208.5399")
    print("   Sec.1.3 calculates the Dirichlet scalar's Casimir density at 3-7% of")
    print("   his own a priori bound, known not to be optimal (%.1f%% at the"
          % (100 * casimir_fraction_of_bound(0.0)))
    print("   midpoint on the scalar's pi^2/1440; %.1f%% on his printed pi^2/1140),"
          % (100 * casimir_fraction_of_bound(0.0, const_term=FEWSTER_PRINTED_CONST_TERM)))
    print("   and asks in print why it is so small a proportion.  No source read shows")
    print("   Ford-Roman saturated, so K = 0 is a known-wrong integer, recorded")
    print("   rather than repaired; see the DOCKET 55 and DOCKET 67 sections.")
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

    # DOCKET 67: this collision exists only because Fewster-Osterbrink is coded
    # in the xi = 0 cell (S = 0, B = 1); read at source FO's xi > 0 bound is
    # state-dependent.  Recorded; the coding and the pin are unchanged.
    chk("one cell collision, and it is the two QEIs", collisions(),
        [("Fewster-Osterbrink QEI", "SNEC")])
    # DOCKET 67: these two pin the CODING.  No source read shows Ford-Roman
    # saturated (FORD_ROMAN_K_IS_WRONG); the honest count is pinned below.
    chk("four bounds are CODED known-saturated", len(saturated()), 4)
    chk("and Ford-Roman is one of them -- the known-wrong K = 0",
        "Ford-Roman QI" in saturated(), True)
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
    # DOCKET 67: on the coding.  Read at source, Fewster-Osterbrink (xi > 0)
    # would be a third member; its row is coded S = 0 (the xi = 0 cell).
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
    # CORRECTED (DOCKET 67): this pin read near(_mid, 0.0682, 1e-2), keyed to
    # Fewster's printed 1140 (a misprint) as the default; it passed there at
    # |rel| 0.0088 and fails on the scalar's 1440 at |rel| 0.0172.  The default
    # is now 1440 and the pin is the computed 0.067028446; the printed 1140 is
    # pinned separately as a control, so the two constants stay distinguishable.
    near("midpoint fraction, against Fewster's printed '3-7%' (scalar's 1440)",
         _mid, 0.067028446, 1e-6)
    near("  control: on his printed 1140 the midpoint is 0.067597448",
         casimir_fraction_of_bound(0.0, const_term=FEWSTER_PRINTED_CONST_TERM),
         0.067597448, 1e-6)
    chk("  control: the old 0.0682 pin (rel 1e-2) fails on the scalar's 1440",
        abs(_mid / 0.0682 - 1.0) <= 1e-2, False)
    chk("  '3-7%' holds on either constant, midplane to z/L = 0.4",
        all(0.03 <= casimir_fraction_of_bound(z, const_term=c) <= 0.07
            for z in (0.0, 0.2, 0.4)
            for c in (SCALAR_DIRICHLET_CONST_TERM, FEWSTER_PRINTED_CONST_TERM)),
        True)
    chk("SO THE DIRICHLET CASIMIR DENSITY DOES NOT SATURATE FEWSTER'S OWN BOUND",
        all(casimir_fraction_of_bound(z) < 0.10 for z in (0.0, 0.2, 0.4)), True)
    chk("no saturation is known, so K = 0 on the Ford-Roman row is a KNOWN-WRONG "
        "INTEGER, recorded not repaired", FORD_ROMAN_K_IS_WRONG, True)
    chk("the honest count of known-saturated bounds is three, not four",
        len(saturated()) - 1, 3)

    # (b') DOCKET 67 (ford-roman-qi-and-fewster-casimir-fraction, M's ruling
    # 2026-10-02): W2 stays WITHDRAWN on four counts; one reading is OPEN.
    _sb = sharp_bound_reading()
    near("DOCKET 67: midplane fraction of Fewster's own bound (pi^2/1440)",
         _sb["bracket"][0], 0.067028446, 1e-6)
    near("  its plate limit 1/(pi^2 C): Fewster's own bound, 3.1964 %",
         _sb["plate"], 0.031963951, 1e-6)
    near("  a midplane saturation needs C_s = 0.212471", _sb["C_s"], 0.21247065, 1e-6)
    near("  = C/14.919", _sb["C_over_C_s"], 14.919, 1e-4)
    near("  the spread mid/plate, the same for every K (no uniform saturation)",
         _sb["spread_mid_over_plate"], 2.097, 1e-3)
    near("  under C_s the fraction at z = L/4 is 48.589 %",
         _sb["quarter_under_C_s"], 0.4858871, 1e-6)
    chk("  the bracket's upper end is saturation, and that reading is OPEN, its "
        "locality step NAMED-NOT-READ; capped-sense OPEN; nothing reinstated",
        (_sb["bracket"][1], SHARP_BOUND_MIDPLANE_SATURATION,
         FEWSTER_LOCALITY_STEP.endswith("NAMED-NOT-READ"),
         CAPPED_SENSE_SATURATION_DIRICHLET.startswith("OPEN"),
         NO_MATERIAL_CHOICE_CROSSES_IT_REINSTATED, FORD_ROMAN_K_IS_WRONG),
        (1.0, "OPEN", True, True, False, True))
    chk("  control: with Fewster's own C taken as sharp the reading is REFUTED "
        "(count (i)); with C_s = 0.212471 it is SATURATED -- the OPEN is the "
        "unknown constant alone", (sharp_reading_status(fewster_C()),
                                   sharp_reading_status(_sb["C_s"])),
        ("REFUTED", "SATURATED"))
    # CORRECTED (DOCKET 67 figures pass): this check read "the default
    # measurement still uses the printed 1140 (recorded, not repaired)",
    # asserting default != bracket[0].  The default is now the scalar's 1440,
    # so the default IS the bracket's lower end; the 1140 figure differs.
    chk("  the default now uses the scalar's 1440 (= the bracket's lower end), "
        "and the printed 1140 gives a different figure",
        (casimir_fraction_of_bound(0.0) == _sb["bracket"][0],
         casimir_fraction_of_bound(0.0, const_term=FEWSTER_PRINTED_CONST_TERM)
         != _sb["bracket"][0]), (True, True))

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
    print("       there cannot be a state-independent one for the free massless")
    print("       minimally coupled scalar in 4D Minkowski.  All-space is")
    print("       spacelike and bounded below (boundary-free); a finite ball is")
    print("       spacelike and, for that field, unbounded below.")

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
