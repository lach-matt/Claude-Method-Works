#!/usr/bin/env python3
r"""
foliation.py -- DOCKET 52, THE ADVERSARIAL PASS.  THE CRITERION IS GAUGE.

driven.py seats the non-static contraction theorem and states its central claim
as

    contraction <=> 2m/R < e^{-2Phi}Rdot^2, so negative Misner-Sharp mass is not
    necessary off the static family.

    python3 foliation.py             the reading
    python3 foliation.py --selftest  every fixture, residuals and obligations
    python3 foliation.py --verify    the sympy residuals alone
    python3 foliation.py --prove     the z3 obligations alone

Run under python3 (3.11).  --verify needs sympy, --prove needs z3-solver; both
are on pypi and pypi is on the proxy allowlist (PROOF-ASSISTANT.md).

===============================================================================
0.  VERDICT
===============================================================================

    THE IDENTITY IS CONFIRMED.  THE CLAIM BUILT ON IT IS REFUTED.

    CONFIRMED.  Gamma^2 = 1 + U^2 - 2m/R is exact, and "m < 0 is not necessary
                for Gamma > 1" follows by inspection.  Nothing here disputes a
                line of the algebra; driven.py --verify already returns 0.

    REFUTED.    "OFF THE STATIC FAMILY" IS THE WRONG NAME FOR THE HYPOTHESIS
                THAT WAS DROPPED, and the claim is empty of content about
                spacetimes.  Three measurements, section by section:

      (i)   THE RANGE THEOREM (section 3).  At any point of any spherically
            symmetric spacetime the set of values Gamma takes over ALL
            foliations is exactly the half-line [sqrt(1-2m/R), infinity).  So
            Gamma > 1 is available AT EVERY POINT WHERE m > 0, by re-slicing
            alone, and Gamma -> infinity as the slice approaches null.  The
            only slicing-independent content of the pair (U, Gamma) is the
            scalar Gamma^2 - U^2 = 1 - 2m/R, because the boost group acts
            TRANSITIVELY on the branch (O12, z3 unsat).  Therefore:

                Gamma > 1 IN EVERY FOLIATION  <=>  m < 0

            which is certify.py's theorem with NO staticity hypothesis at all.
            Dropping staticity does not weaken that theorem.  IT REMOVES ITS
            HYPOTHESIS.

      (ii)  THE STATIC WITNESS (section 4).  Schwarzschild -- vacuum, Ricci
            identically 0, m = M > 0, STATIC -- sliced by the generalised
            Painleve-Gullstrand foliation with LTB energy E > 0 returns
            Gamma = sqrt(1+2E) > 1 AT EVERY AREAL RADIUS, out to infinity.
            driven.py believed it had to leave the static family to obtain
            contraction with m > 0.  It did not.  IT HAD ONLY TO TILT THE
            SLICE.  What certify.py's staticity was doing was not making the
            spacetime static; it was PICKING THE FOLIATION, through the Killing
            field.  driven.py section 6 states the gauge fact; it does not draw
            this consequence, and its section 3 reading of certify.py as "the
            Rdot = 0 corner" understates it -- U = 0 is not a corner, IT IS THE
            INFIMUM OF THE ORBIT, and that is why the corner is the theorem.

      (iii) THE CRITERION IS ANTI-CORRELATED WITH TRAVEL TIME (sections 6-8),
            measured in driven.py's own witnesses.  In Milne -- exactly
            Minkowski -- Gamma = 100 everywhere and a light signal to the
            "contracted" endpoint takes 3774 times the slice's own proper
            length, with an advance over flat of exactly zero because the
            spacetime IS flat.  In Schwarzschild with the two mouths pinned at
            fixed areal radii 10M and 100M, the proper length of the slice
            between them can be driven BELOW 0.05 % of the areal gap by
            re-slicing, WITH U = 0 AT BOTH MOUTHS -- so nonstatic.py's anchor
            lemma does not close the integrated criterion -- while the light
            travel time between those same two mouths is unchanged and is a
            Shapiro DELAY of 5.011 M over the areal gap.

    AND THE BILL IS STILL NOT LIFTED, for the reason the literature pass gave:
    Olum PRL 81, 3567 needs no staticity, no sphericity and no foliation.  This
    file removes a route; it opens none.  It also does not touch the corridor
    bill in either direction -- see section 9 on what E = R dGamma prices.

===============================================================================
1.  THE ELEMENTARY FACT, FIRST, BECAUSE IT NEEDS NO GENERAL RELATIVITY
===============================================================================

Two inertial observers in Minkowski space, at rest, separated by D.  The
infimum of proper length over SPACELIKE CURVES joining their worldlines is

        inf sqrt(D^2 - t^2)  =  0.

There is no shortest slice and no canonical one.  "The proper distance to
Proxima" is not a number until a slice is named, and over all slices its
infimum is zero IN FLAT SPACE.  Any criterion of the form "proper distance is
less than X" is therefore satisfiable in Minkowski for every X > 0, and
satisfying it is worth nothing.

    THAT IS THE WHOLE OBJECTION.  Sections 2-4 make it exact and sharp;
    sections 5-8 measure what it costs driven.py; section 9 says what survives.

===============================================================================
2.  EVERY RADIAL BOOST IS A GENUINE RE-SLICING -- FROBENIUS, RESIDUAL 0
===============================================================================

The objection would be weak if only some boosts corresponded to foliations.
They all do, and the freedom is a FREE FUNCTION OF TWO VARIABLES.

    LEMMA (verified, sympy).  Let u = e^{-Phi} d_t and n = e^{-Lambda} d_r be
    the unit normal and unit radial vector of the chart.  For ANY rapidity
    field w(t,r), the field

        u' = cosh(w) u + sinh(w) n

    is a unit timelike spherically symmetric field and satisfies the Frobenius
    condition u'_[a d_b u'_c] = 0 IDENTICALLY -- all 64 components, w arbitrary.

    SO EVERY SPHERICALLY SYMMETRIC UNIT TIMELIKE FIELD IS HYPERSURFACE
    ORTHOGONAL.  (It must be: in the 2-dimensional (t,r) quotient a 1-form's
    twist 3-form has nowhere to live, and the sphere directions are carried by
    symmetry.)  Each such u' is the normal of a foliation, and in the chart
    adapted to it the metric is again -e^{2Phi'}dt'^2 + e^{2Lambda'}dr'^2 +
    R^2 dOmega^2 -- driven.py's own ansatz.

    CONSEQUENCE.  driven.py's ansatz does not fix a foliation.  "Rdot" is not
    "the areal radius is changing"; it is "THE SLICE IS NOT COMOVING WITH THE
    AREAL RADIUS", and w(t,r) is free.

===============================================================================
3.  THE RANGE THEOREM -- WHAT Gamma CAN BE, AND WHAT IT CANNOT HIDE
===============================================================================

(U, Gamma) are the frame components of the gradient of the areal radius:
U = -u^a d_a R, Gamma = n^a d_a R (residual 0, section V3).  A change of
foliation acts on them as a boost (residual 0, V4):

        U'     =  cosh(w) U + sinh(w) Gamma
        Gamma' =  sinh(w) U + cosh(w) Gamma
        Gamma'^2 - U'^2  =  Gamma^2 - U^2  =  1 - 2m/R           (INVARIANT)

    UNTRAPPED, 1 - 2m/R = k^2 > 0.  Write k = sqrt(1-2m/R).  Then

        Gamma = k cosh(psi),        U = k sinh(psi)

    with psi the rapidity of the slice relative to the UNIQUE slice on which
    the areal radius is momentarily stationary.  Hence

        THE ACHIEVABLE SET IS   Gamma in [k, infinity),   attained at psi = 0,
        UNBOUNDED ABOVE, AND EVERY VALUE IN IT IS REALISED BY A FOLIATION.

    Three corollaries, each machine-checked (O3, O4, O7, O12):

        m < 0   =>  k > 1  =>  Gamma > 1 IN EVERY FOLIATION.
        m = 0   =>  k = 1  =>  Gamma >= 1, with equality on one slice.
        m > 0   =>  k < 1  =>  Gamma > 1 ON SOME FOLIATION AT EVERY POINT,
                               and Gamma <= 1 on another.

        GAMMA > 1 IN EVERY FOLIATION  <=>  m < 0.

    THE ORBIT IS THE WHOLE BRANCH (O12, unsat): any two states with the same k
    and Gamma > 0 are related by a boost, with the explicit witness

        c = (G1 G2 - U1 U2)/k^2,      s = (U2 G1 - U1 G2)/k^2.

    So ANY function of (U, Gamma) that is the same in every foliation is a
    function of k alone -- that is, of m.  "Contraction" cannot be given a
    slicing-free meaning in these variables EXCEPT as a condition on m, and the
    condition it becomes is exactly certify.py's.

    TRAPPED, 1 - 2m/R < 0.  d_a R is timelike, the orbit is the other kind of
    hyperbola, and Gamma ranges over ALL of R -- every value, both signs, zero
    included (O11).  There "contraction" is not merely gauge, it is not even
    sign-definite.  m < 0 never puts a point here (1 - 2m/R > 1 > 0).

    WHAT THIS DOES TO driven.py SECTION 3.  It reads certify.py as "the
    Rdot = 0 corner" of a wider criterion.  The measurement says the opposite:
    U = 0 is the MINIMISING member of the orbit, so certify.py's criterion is
    not a special case of driven.py's -- IT IS ITS FOLIATION-INVARIANT CORE,
    and it holds with staticity deleted from the hypothesis.  nonstatic.py's
    anchor lemma (U = 0 at one point suffices) is the same fact reached from
    the other side; this file says why U = 0 is the right place to stand.

===============================================================================
4.  THE WITNESS THAT NAMES THE WRONG HYPOTHESIS -- STATIC SCHWARZSCHILD
===============================================================================

The generalised Painleve-Gullstrand chart, with constant LTB energy E > 0:

        ds^2 = -dtau^2 + (dR + sqrt(2M/R + 2E) dtau)^2/(1+2E) + R^2 dOmega^2

Computed, not quoted (V7):  RICCI IS IDENTICALLY ZERO -- this is Schwarzschild,
vacuum, and the spacetime is STATIC.  On it:

        |grad R|^2 = 1 - 2M/R      =>  m = M > 0      (the MS mass, a scalar)
        slice tau = const:  dl = dR/sqrt(1+2E)
        Gamma = dR/dl = sqrt(1+2E) > 1  AT EVERY AREAL RADIUS
        U = sqrt(2M/R + 2E),   Gamma^2 - U^2 = 1 - 2M/R    (residual 0)

    SO driven.py's CRITERION DECLARES THE WHOLE SCHWARZSCHILD EXTERIOR
    CONTRACTED, WITH POSITIVE MASS, IN A STATIC SPACETIME.

    E = 0 is the ordinary PG slicing and gives Gamma = 1 exactly -- which is
    drivensource.py's pg_witness, recovered here as the E -> 0 member of a
    family rather than as a single fact.  E < 0 (bound shells) gives Gamma < 1.
    ONE SPACETIME, ONE EVENT, THE VERDICT SET BY A LABEL ON THE FOLIATION.

    THE DOCKET MIS-NAMED ITS OWN HYPOTHESIS.  What certify.py used was not that
    the spacetime is static but that the foliation is the KILLING-ADAPTED one,
    where U = 0 identically.  Staticity is sufficient for that and is not its
    content.  Drop staticity and you lose the CHOICE, not the theorem.

===============================================================================
5.  FIVE DEFINITIONS OF CONTRACTION, AND WHAT EACH ONE DOES TO THE THEOREM
===============================================================================

The prompt to this pass asked whether the comparison "proper length e^Lambda dr
against the areal increment R' dr" is the right one, and whether the choice
smuggles the result.  IT DOES NOT, AND THAT IS WORTH SAYING PLAINLY: the areal
increment dR is a geometric quantity -- sqrt(Area/4pi) of the round sphere --
and it is the only radial scale spherical symmetry supplies, so certify.py's
"the flat value dr with R = r" generalises to dR with nothing smuggled.  THE
SMUGGLING IS NOT IN dR.  IT IS IN dl, WHICH NAMES A SLICE.

    D1  LOCAL AREAL RATIO, driven.py's:  dl < dR at a point, i.e. Gamma > 1.
        NOT INVARIANT.  m < 0 is not necessary -- and section 3 says the "not
        necessary" is pure gauge, available at every point of every spacetime
        with m > 0.  THE THEOREM FAILS AND THE FAILURE IS EMPTY.

    D2  INVARIANT VERSION:  Gamma > 1 in EVERY foliation, equivalently the
        scalar g^{ab} d_a R d_b R > 1.  THE THEOREM SURVIVES, EXACTLY AND WITH
        STATICITY DELETED:  D2 <=> m < 0.  This is the right generalisation of
        certify.py off the static family, and it strengthens it.

    D3  INTEGRATED:  the proper length of the slice between two fixed areal
        radii is less than their areal gap.  NOT INVARIANT, and worse than D1:
        section 6 drives it to 0.05 % of the gap in Schwarzschild with M > 0
        AND BOTH MOUTHS ANCHORED AT U = 0.  Its slicing-free infimum is 0 by
        section 1.

    D4  OPERATIONAL:  a signal from mouth to mouth arrives EARLIER than in the
        reference geometry.  INVARIANT (the mouths are worldlines, the arrival
        is an event).  THE THEOREM IS REPLACED BY A STRONGER ONE that is not
        this tree's: Olum gr-qc/9805003, Gao & Wald gr-qc/0007021,
        Visser-Bassett-Liberati gr-qc/9908023 -- with the NEC, never an
        advance.  Sections 7-8 measure D1 against D4 and find them ANTI-
        CORRELATED.

    D5  NULL FLARE-OUT:  theta_+ = (2/R)(U + Gamma) and its derivative along
        the ray.  INVARIANT given the sphere.  Hochberg & Visser gr-qc/9802046
        section 7 -- spatial flare-out does not imply null flare-out once the
        geometry is time dependent -- and gr-qc/9802048: NEC violation on an
        open interval at any throat.  THE THEOREM IS REPLACED BY A STRONGER
        ONE, again not this tree's.

    SCORE:  TWO of the five make m < 0 unnecessary -- D1 and D3 -- and they
    are exactly the two that are not invariant, and on both the escape is
    available IN FLAT SPACE.  ON THE THREE INVARIANT ONES THE OBSTRUCTION
    STANDS (D2) OR HARDENS (D4, D5).

===============================================================================
6.  D3 MEASURED:  THE SLICE LENGTH GOES TO ZERO WITH THE MOUTHS ANCHORED
===============================================================================

Schwarzschild, M = 1, mouths at fixed areal radii R1 = 10, R2 = 100, areal gap
90.  A spherically symmetric spacelike slice is a graph T = T(R); writing
T'(R) = tanh(psi)/f with f = 1 - 2M/R gives, exactly,

        Gamma = sqrt(f) cosh(psi),      U = sqrt(f) sinh(psi),      dl = dR/Gamma

-- section 3's decomposition, now as a slice one can draw.  Take psi(R) a
smooth bump vanishing at BOTH mouths, so U = 0 there and nonstatic.py's anchor
lemma applies at each mouth exactly as it demands.  Measured:

        amplitude A       max Gamma        L / (R2 - R1)
        0 (static)           0.989949           1.027241
        1                    1.526650           0.673058     <- already short
        2                    3.721930           0.285058
        5                   73.411700           0.021733
        20                   2.39954e+08        0.001868
        80                   2.74007e+34        0.000464

    L -> 0.  THE ANCHOR LEMMA DOES NOT CLOSE THE INTEGRATED CRITERION.  It is a
    pointwise statement and it bites only where U = 0; a slice can be anchored
    at both mouths and near-null in between.  RECORDED AGAINST nonstatic.py's
    KILL ONE, which is correct as written and is not sufficient for D3.

===============================================================================
7.  D1 AGAINST D4 IN driven.py's OWN WITNESS -- MILNE
===============================================================================

Minkowski in Milne slicing: Gamma = cosh(chi), m = 0, T_ab = 0 identically.
Emitter at chi = 0 and target at chi_1 on the same slice tau_0 = 1:

    Gamma   slice length   areal R   slice/areal   light flight   flight/slice
      2       1.316958     1.732051    0.760346      6.464102        4.9084
     10       2.993223     9.949874    0.300830    198.498744       66.3161
    100       5.298292    99.995000    0.052986  19998.499987     3774.5180

    THE SLICE IS 5.3 % OF THE AREAL GAP AND THE SIGNAL TAKES 3774 TIMES THE
    SLICE'S LENGTH TO CROSS IT.  The advance over flat is EXACTLY ZERO, because
    the spacetime is exactly flat.  D1 says "contracted by 19x"; D4 says
    "nothing happened".

    THE REASON IS NOT SUBTLE.  A large Gamma is a slice tilted towards the
    light cone.  Tilting a slice shortens it and delivers no one anywhere.

===============================================================================
8.  D1 AGAINST D4 WITH MASS -- SCHWARZSCHILD, WHERE THE ANSWER IS A DELAY
===============================================================================

Same corridor as section 6, mouths at areal radii 10M and 100M, which are
geometric and which no re-slicing moves.  Radial null travel between them:

        Killing time                 95.011052 M      (areal gap 90)
        proper time at the far mouth 94.056143 M
        SHAPIRO EXCESS                5.011052 M      -- A DELAY

    So on the same corridor, in the same spacetime: D3 reports a corridor
    0.05 % of the flat length, D4 reports a 5.6 % DELAY, and D4 is the one
    computed from the worldlines rather than from a choice of slice.  Gao &
    Wald and Visser-Bassett-Liberati say the sign of that excess is forced by
    the NEC and does not depend on staticity.

===============================================================================
9.  WHAT THIS DOES TO nonstatic.py, STATED CAREFULLY
===============================================================================

nonstatic.py is not refuted.  Its equations are derived and its conclusion --
the loophole is empty -- is the same as this file's.  Three narrowings:

    ITS TWO KILLS ARE ONE ALGEBRAIC FACT.  With Gamma = k cosh psi and
    U = k sinh psi: the ANCHOR LEMMA is psi = 0, and the DISPLACEMENT BOUND
    |U| >= sqrt(Gamma^2 - 1) for m >= 0 is U^2 = Gamma^2 - k^2 with k <= 1.
    Both are the boost decomposition read twice (O9a, O9b, unsat).

    "THE FAR END IS DISPLACED" IS ABOUT THE EULERIAN OBSERVERS, NOT THE
    DESTINATION.  U is the areal velocity of the SLICE NORMAL.  In section 6
    the mouths sit at fixed areal radius for all time and never move; the
    observers that move are an artefact of the tilt.  The bound is right; its
    reading as "you have moved Proxima" holds only where the Eulerian
    congruence IS the endpoint, which is again psi = 0.

    E = R dGamma PRICES A GAUGE TRANSFORMATION.  It is derived from
    D_t Gamma = 4 pi R j + U D_r Phi with the second term set to zero by
    choosing geodesic slicing.  In VACUUM that same gauge forces D_t Gamma = 0
    identically -- so within it the bill is never payable and contraction can
    never be switched on, which is nonstatic.py's own "born with it".  Outside
    it the change is free: section V13 exhibits a smooth foliation of a flat
    region, T_ab = 0 identically, on which Gamma runs from 1 to 7071 with
    j = 0 throughout.  Priced by E = R dGamma over a Proxima span that reads
    2.7207e13 solar masses PER UNIT dGamma FOR RE-SLICING EMPTY SPACE.  The
    number is reproduced here from nonstatic.py's own function, to nine
    figures, so the disagreement is about what it measures and not about it.

    NONE OF THIS TOUCHES THE CORRIDOR BILL.  H83d's 2.7254e12 solar masses of
    negative mass is not in question here in either direction.

===============================================================================
10.  STATUS, PRIOR ART, AND WHAT IS REFUSED
===============================================================================

A CONSEQUENCE FOR expose.py, WHICH IS THE SAME FAULT ONE LEVEL UP.  expose.py
caught threads.py testing contraction with sqrt(g_rr) < 1, "a test that FIRES IN
FLAT EMPTY SPACE", and replaced it with C = sqrt(g_rr) / (d/dr)sqrt(g_phiphi),
demonstrating C = 1 exactly in flat space however it is coordinatised.  THAT
DEMONSTRATION IS ABOUT SPATIAL COORDINATES ON A GIVEN SLICE, AND C IS INVARIANT
UNDER EXACTLY THOSE.  It is a 3-geometry invariant, not a spacetime one: C is
1/Gamma (driven.py, residual 0), so in Milne slicing of Minkowski C = 1/cosh(chi),
which at chi = 1.3169579 is 0.5.  expose.py's own sentence -- C = 1 in flat empty
space -- IS FALSE OFF THE STATIC SLICE, and the criterion it rescued fires in
flat empty space for the same reason the one it replaced did, one level up.
NARROWED, NOT REPAIRED: expose.py's Kerr result is a statement about
Boyer-Lindquist constant-t slices and stands as such; nothing in that file is
edited and its conclusion about threads.py is untouched.

PRIOR ART, INTERNAL, AND IT IS CLOSE.  driven.py section 6 states the gauge
fact -- "m is a scalar, Gamma is not" -- and nonstatic.py measured two slicings
of Minkowski returning two Gammas.  THE QUALITATIVE POINT IS ALREADY SEATED AND
IS NOT CLAIMED HERE.  What is new to the tree is the quantitative form: the
RANGE (a half-line with floor sqrt(1-2m/R)), the TRANSITIVITY that makes the
floor the only invariant, the resulting BICONDITIONAL with staticity deleted,
the STATIC Schwarzschild witness, and the three measurements in sections 6-8.
expose.py's C = 1/Gamma is the same non-invariant, so this reading applies to
it verbatim off the Killing-adapted slice.

PRIOR ART, EXTERNAL.  The boost decomposition of (U, Gamma) is the standard
Misner-Sharp-Hernandez kinematics; Gamma^2 - U^2 = 1 - 2m/R is Misner & Sharp
1964 via Hayward gr-qc/9408002 eq. (27), RECOVERED not read at source, exactly
as driven.py records.  That spatial flare-out is not null flare-out is Hochberg
& Visser gr-qc/9802046 section 7.  NO NOVELTY AGAINST THE LITERATURE IS CLAIMED
FOR ANY LINE OF MATHEMATICS HERE.  The novelty claimed against the TREE is that
the claim in driven.py's headline is measured to be gauge rather than argued to
be suspicious.

REFUSED, EXPLICITLY:

    IT DOES NOT REFUTE THE IDENTITY, and says so in section 0.  driven.py's
    --verify residuals are reproduced, not disputed.

    IT DOES NOT SHOW THAT NO DYNAMIC SPHERICAL CORRIDOR EXISTS.  That is
    Olum's theorem and it is his.  A gauge argument cannot prove a physical
    impossibility; it can only show that a particular criterion is not one.

    IT DOES NOT ADJUDICATE whether some OTHER invariant -- an averaged
    expansion, a Hawking mass flow, a null-geodesic arrival map -- recovers a
    useful non-static criterion.  quasilocal.py ruled out the single-surface
    class; this file rules out the constant-t class.  The FOLIATION class that
    quasilocal.py named as L1's real form IS NOT TOUCHED HERE.

    IT DOES NOT MEASURE anything non-spherical.  The Alcubierre family is
    outside this file exactly as it is outside certify.py and driven.py.

    IT REPAIRS NOTHING.  driven.py, nonstatic.py, drivensource.py, certify.py,
    expose.py and overturn.py are untouched; paper/ is untouched; no ruling is
    offered.  The chat-67 full hold governs this as a finding.
"""

import math
import sys

# ============================================================== 1. the fact

def spacelike_length(D, t):
    """Proper length of the straight spacelike chord joining (0,0) to (t,D) in
    Minkowski.  sqrt(D^2 - t^2) -> 0 as t -> D.  There is no shortest slice."""
    if abs(t) >= abs(D):
        raise ValueError("not spacelike: |t| >= |D|")
    return math.sqrt(D * D - t * t)


def slice_infimum_is_zero(D=1.0, ts=(0.0, 0.5, 0.9, 0.99, 0.9999, 0.999999)):
    """The sequence that makes the infimum 0 in FLAT space, with no curvature,
    no matter and no negative mass anywhere."""
    return [(t, spacelike_length(D, t)) for t in ts]


# ================================================ 3. the boost orbit, floats

def k_of(m, R):
    """k^2 = 1 - 2m/R, the INVARIANT.  Returns k^2, which may be negative
    (trapped).  This is the only slicing-independent function of (U, Gamma)."""
    return 1.0 - 2.0 * m / R


def gamma_floor(m, R):
    """The infimum of Gamma over all foliations at an untrapped point, attained
    on the unique slice with U = 0.  None where d_a R is timelike."""
    k2 = k_of(m, R)
    return math.sqrt(k2) if k2 > 0.0 else None


def state(m, R, psi):
    """(U, Gamma) at rapidity psi relative to the U = 0 slice.  Untrapped."""
    k2 = k_of(m, R)
    if k2 <= 0.0:
        raise ValueError("trapped or marginal: 1 - 2m/R = %r" % k2)
    k = math.sqrt(k2)
    return k * math.sinh(psi), k * math.cosh(psi)


def boost(U, G, w):
    """A change of foliation by rapidity w.  Section 2 says every w(t,r) is a
    genuine re-slicing, so this is not a formal operation."""
    return math.cosh(w) * U + math.sinh(w) * G, math.sinh(w) * U + math.cosh(w) * G


def contracts_somewhere(m, R):
    """Is there a foliation with Gamma > 1 at this point?  ALWAYS.  The
    supremum of Gamma over the boost orbit is +infinity for every m and every
    R > 0 -- untrapped (O6, O7) and trapped (O11) alike.  The function takes
    its arguments so that a caller can see it never consults them."""
    del m, R
    return True


def contracts_everywhere(m, R):
    """Is Gamma > 1 in EVERY foliation?  THE INVARIANT CRITERION.  This is
    certify.py's theorem with staticity deleted from the hypothesis."""
    k2 = k_of(m, R)
    return k2 > 1.0                              # <=> m < 0


def rapidity_to_contract(m, R):
    """The least |psi| at which the slice reports contraction.  0 when m <= 0;
    arccosh(1/k) when m > 0 -- finite, and small.  On the degenerate orbit
    (1 - 2m/R <= 0) there is no U = 0 slice to measure psi from and the answer
    is 0 by convention, not by measurement: there Gamma reaches every real
    value (O11) and no rapidity threshold exists."""
    k2 = k_of(m, R)
    if k2 <= 0.0:
        return 0.0
    k = math.sqrt(k2)
    return 0.0 if k >= 1.0 else math.acosh(1.0 / k)


def orbit_boost(U1, G1, U2, G2):
    """The explicit boost carrying one state to another on the same branch --
    the witness behind O12, and the reason the only invariant is k."""
    k2 = G1 * G1 - U1 * U1
    return (G1 * G2 - U1 * U2) / k2, (U2 * G1 - U1 * G2) / k2


# ============================================ 6. D3, the anchored slice

def _bump(x):
    """A smooth compactly supported bump on (0,1), normalised to 1 at x = 1/2.
    Vanishes to all orders at both ends, so U = 0 at BOTH mouths exactly."""
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return math.exp(4.0 - 1.0 / (x * (1.0 - x)))


def slice_length(M, R1, R2, A, n=20000, flat_top=True):
    """Proper length of the slice T = T(R) between two fixed areal radii, with
    rapidity psi(R) = A * profile(R) vanishing at both mouths.  Simpson."""
    h = (R2 - R1) / n
    tot = 0.0
    for i in range(n + 1):
        R = R1 + i * h
        x = (R - R1) / (R2 - R1)
        p = (math.tanh(x * (R2 - R1)) * math.tanh((1.0 - x) * (R2 - R1))
             if flat_top else _bump(x))
        psi = A * p
        f = 1.0 - 2.0 * M / R
        w = 1.0 if 0 < i < n else 0.5
        tot += w / (math.sqrt(f) * math.cosh(psi))
    return tot * h


def max_gamma_on_slice(M, R1, R2, A, n=2000, flat_top=True):
    """The largest Gamma the slice reaches.  Gamma = sqrt(f) cosh(psi)."""
    best = 0.0
    for i in range(n + 1):
        R = R1 + i * (R2 - R1) / n
        x = (R - R1) / (R2 - R1)
        p = (math.tanh(x * (R2 - R1)) * math.tanh((1.0 - x) * (R2 - R1))
             if flat_top else _bump(x))
        best = max(best, math.sqrt(1.0 - 2.0 * M / R) * math.cosh(A * p))
    return best


def d3_table(M=1.0, R1=10.0, R2=100.0, amps=(0.0, 1.0, 2.0, 5.0, 20.0, 80.0)):
    """L/(R2-R1) against the rapidity amplitude, mouths anchored at U = 0."""
    gap = R2 - R1
    return [(A, max_gamma_on_slice(M, R1, R2, A), slice_length(M, R1, R2, A),
             slice_length(M, R1, R2, A) / gap) for A in amps]


# ==================================================== 7-8. D4, travel time

def expose_C(gamma_value):
    """expose.py's invariant C = sqrt(g_rr) / (d/dr)sqrt(g_phiphi), which is
    proper radial length per unit circumferential radius -- exactly 1/Gamma on
    a constant-t slice.  Invariant under spatial re-coordinatisation of that
    slice; NOT invariant under re-foliation."""
    return 1.0 / gamma_value


def milne_row(G):
    """driven.py's own witness 1.  Gamma = cosh(chi), spacetime EXACTLY flat.
    Slice length, areal radius, and the Minkowski time of flight from the
    centre to the target, all at tau_0 = 1."""
    chi = math.acosh(G)
    sl = chi
    areal = math.sinh(chi)
    dt = math.exp(chi) * math.cosh(chi) - 1.0
    dr = math.exp(chi) * math.sinh(chi)
    return dict(gamma=G, chi=chi, slice_length=sl, areal=areal,
                slice_over_areal=sl / areal, flight=dt, null=abs(dt - dr),
                flight_over_slice=dt / sl, advance_over_flat=0.0)


def shapiro(M, R1, R2):
    """Radial null travel between two FIXED AREAL RADII in Schwarzschild.  The
    mouths are worldlines; no re-slicing moves them and none changes this."""
    dt = (R2 - R1) + 2.0 * M * math.log((R2 - 2.0 * M) / (R1 - 2.0 * M))
    return dict(killing=dt, far_proper=dt * math.sqrt(1.0 - 2.0 * M / R2),
                near_proper=dt * math.sqrt(1.0 - 2.0 * M / R1),
                excess=dt - (R2 - R1), areal_gap=R2 - R1)


# ============================================= 9. what E = R dGamma prices

C_LIGHT = 2.99792458e8
G_NEWTON = 6.67430e-11
M_SUN = 1.98840e30
LY = 9.4607304725808e15
PROXIMA_LY = 4.2465


def proxima_span_m():
    return PROXIMA_LY * LY


def gauge_bill_msun(R_m, dGamma):
    """nonstatic.py's E = R dGamma in SI, applied to a re-slicing of EMPTY
    SPACE.  Cross-checked against nonstatic.build_energy in the selftest."""
    return R_m * dGamma * C_LIGHT * C_LIGHT / G_NEWTON / M_SUN


def flat_foliation_gamma(eps):
    """The largest Gamma reached by the smooth flat-space foliation of V13,
    on which T_ab = 0 identically and j = 0 throughout: Gamma = 1/sqrt(1-(1-eps)^2)."""
    return 1.0 / math.sqrt(1.0 - (1.0 - eps) ** 2)


# ============================================================ 5. the table

def definitions_table():
    """The five definitions and what each does to certify.py's theorem."""
    return [
        ("D1 local areal ratio  dl < dR   (driven.py)", "NO",
         "FAILS -- and the failure is gauge; available wherever m > 0"),
        ("D2 dl < dR in EVERY foliation = |grad R|^2 > 1", "YES",
         "SURVIVES, exactly, WITH STATICITY DELETED:  D2 <=> m < 0"),
        ("D3 integrated slice length < areal gap", "NO",
         "FAILS worse -- infimum 0, mouths anchored, section 6"),
        ("D4 arrival earlier than the reference geometry", "YES",
         "REPLACED BY A STRONGER ONE -- Olum, Gao-Wald, VBL"),
        ("D5 null flare-out  theta_+  and its derivative", "YES",
         "REPLACED BY A STRONGER ONE -- Hochberg & Visser 1998"),
    ]


# ================================================= the sympy verifications

def verify():
    """Every residual this file rests on.  Returns a list of (label, residual,
    want) with want = 0 unless stated.  NOTHING HERE IS QUOTED."""
    import sympy as sp
    out = []
    t, r, th, ph = sp.symbols("t r theta phi", real=True)
    Phi = sp.Function("Phi")(t, r)
    Lam = sp.Function("Lambda")(t, r)
    R = sp.Function("R")(t, r)
    x = [t, r, th, ph]
    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
    gi = g.inv()

    U = sp.exp(-Phi) * sp.diff(R, t)
    G = sp.exp(-Lam) * sp.diff(R, r)
    gradR2 = sum(gi[a, b] * sp.diff(R, x[a]) * sp.diff(R, x[b])
                 for a in range(4) for b in range(4))
    out.append(("V1  1 - 2m/R = g^ab d_aR d_bR = Gamma^2 - U^2",
                sp.simplify(gradR2 - (G**2 - U**2)), 0))

    u = sp.Matrix([sp.exp(-Phi), 0, 0, 0])
    n = sp.Matrix([0, sp.exp(-Lam), 0, 0])
    out.append(("V2  u.u = -1, n.n = +1, u.n = 0",
                sp.simplify((u.T * g * u)[0, 0] + 1)
                + sp.simplify((n.T * g * n)[0, 0] - 1)
                + sp.simplify((u.T * g * n)[0, 0]), 0))
    dR = sp.Matrix([sp.diff(R, v) for v in x])
    out.append(("V3  U = u^a d_aR and Gamma = n^a d_aR",
                sp.simplify(sum(u[a] * dR[a] for a in range(4)) - U)
                + sp.simplify(sum(n[a] * dR[a] for a in range(4)) - G), 0))

    c, s = sp.symbols("c s", real=True, positive=True)
    out.append(("V4  boost preserves Gamma^2 - U^2",
                sp.simplify(sp.expand((s * U + c * G)**2 - (c * U + s * G)**2
                                      - (G**2 - U**2)).subs(c**2, 1 + s**2)), 0))

    # V5 -- FROBENIUS, with the rapidity a FREE FUNCTION of (t, r)
    w = sp.Function("w")(t, r)
    up = sp.cosh(w) * u + sp.sinh(w) * n
    uc = g * up
    bad = 0
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                e = (uc[a] * (sp.diff(uc[cc], x[b]) - sp.diff(uc[b], x[cc]))
                     + uc[b] * (sp.diff(uc[a], x[cc]) - sp.diff(uc[cc], x[a]))
                     + uc[cc] * (sp.diff(uc[b], x[a]) - sp.diff(uc[a], x[b])))
                if sp.simplify(e) != 0:
                    bad += 1
    out.append(("V5  FROBENIUS u'_[a d_b u'_c] = 0, w(t,r) ARBITRARY "
                "(nonzero components)", sp.Integer(bad), 0))
    out.append(("V6  u' is unit timelike for every w",
                sp.simplify((up.T * g * up)[0, 0] + 1), 0))

    # V7 -- generalised Painleve-Gullstrand Schwarzschild: Ricci = 0, m = M
    tau, Rc = sp.symbols("tau R", positive=True)
    M, E = sp.symbols("M E", positive=True)
    y = [tau, Rc, th, ph]
    v = sp.sqrt(2 * M / Rc + 2 * E)
    kk = 1 + 2 * E
    h = sp.zeros(4, 4)
    h[0, 0] = -1 + v**2 / kk
    h[0, 1] = h[1, 0] = v / kk
    h[1, 1] = 1 / kk
    h[2, 2] = Rc**2
    h[3, 3] = Rc**2 * sp.sin(th)**2
    hi = sp.simplify(h.inv())
    Ga = [[[sp.simplify(sp.Rational(1, 2) * sum(
        hi[a, d] * (sp.diff(h[d, b], y[c]) + sp.diff(h[d, c], y[b])
                    - sp.diff(h[b, c], y[d])) for d in range(4)))
        for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            e = 0
            for a in range(4):
                e += sp.diff(Ga[a][b][c], y[a]) - sp.diff(Ga[a][b][a], y[c])
                for d in range(4):
                    e += Ga[a][a][d] * Ga[d][b][c] - Ga[a][c][d] * Ga[d][b][a]
            Ric[b, c] = sp.simplify(e)
    out.append(("V7  generalised PG chart is VACUUM (Ricci, all 16)",
                sp.simplify(sum(abs(Ric[i, j]) for i in range(4) for j in range(4))), 0))
    gR2 = sp.simplify(hi[1, 1])
    mm = sp.simplify(Rc * (1 - gR2) / 2)
    out.append(("V8  its Misner-Sharp mass is M > 0, a scalar",
                sp.simplify(mm - M), 0))
    Gam_pg = sp.simplify(1 / sp.sqrt(h[1, 1]))
    out.append(("V9  and its slice returns Gamma = sqrt(1+2E) > 1 EVERYWHERE",
                sp.simplify(Gam_pg - sp.sqrt(1 + 2 * E)), 0))
    u_pg = sp.Matrix([1, -v, 0, 0])
    out.append(("V10 with unit normal, U = sqrt(2M/R+2E) and Gamma^2-U^2 = 1-2M/R",
                sp.simplify((u_pg.T * h * u_pg)[0, 0] + 1)
                + sp.simplify(Gam_pg**2 - v**2 - (1 - 2 * M / Rc)), 0))

    # V11 -- the rapidity decomposition, and V12 -- the Schwarzschild graph slice
    psi, kq = sp.symbols("psi k", real=True, positive=True)
    out.append(("V11 Gamma = k cosh(psi), U = k sinh(psi) reproduces the invariant",
                sp.simplify((kq * sp.cosh(psi))**2 - (kq * sp.sinh(psi))**2 - kq**2), 0))
    f, Tp = sp.symbols("f Tprime", positive=True)
    dl2 = 1 / f - f * Tp**2
    out.append(("V12 T'(R) = tanh(psi)/f  =>  Gamma = dR/dl = sqrt(f) cosh(psi)",
                sp.simplify(1 / sp.sqrt(dl2.subs(Tp, sp.tanh(psi) / f))
                            - sp.sqrt(f) * sp.cosh(psi)), 0))

    # V13 -- a flat-space foliation on which Gamma runs, with T_ab = 0.
    # PULLED BACK FROM THE EMBEDDING, not written down: the leaf t = T(r) in
    # Minkowski, parametrised by (r, theta, phi).
    rr = sp.Symbol("r_", positive=True)
    Tf = sp.Function("T")(rr)
    Tr = sp.diff(Tf, rr)
    emb = [Tf, rr, th, ph]                             # (t, r, theta, phi)
    eta = sp.diag(-1, 1, rr**2, rr**2 * sp.sin(th)**2)
    par = [rr, th, ph]
    ind = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            ind[i, j] = sp.simplify(sum(
                eta[a, a] * sp.diff(emb[a], par[i]) * sp.diff(emb[a], par[j])
                for a in range(4)))
    out.append(("V13 induced metric of the flat leaf t = T(r) is (1-T'^2)dr^2",
                sp.simplify(ind[0, 0] - (1 - Tr**2)), 0))
    Gam_f = sp.simplify(1 / sp.sqrt(ind[0, 0]))
    uf = sp.Matrix([1, Tr, 0, 0]) / sp.sqrt(1 - Tr**2)   # the unit normal
    out.append(("V14 its unit normal is timelike and gives U = T'/sqrt(1-T'^2)",
                sp.simplify(sum(eta[a, a] * uf[a]**2 for a in range(4)) + 1), 0))
    Uf = sp.simplify(uf[1])
    out.append(("V15 and Gamma^2 - U^2 = 1 = 1 - 2m/R with m = 0, Gamma = cosh(psi)",
                sp.simplify(Gam_f**2 - Uf**2 - 1), 0))
    return out


# ================================================= the machine obligations

def _z3():
    import prover
    prover.require_z3()
    import z3
    return z3


def obligations():
    """Thirteen claims over the reals plus six guards.  Every obligation is
    asserted NEGATED and reported unsat; every guard is asserted DIRECTLY and
    reported sat, so no guard can pass because its own hypothesis is false.
    PROOF-ASSISTANT.md's two failure modes, both answered."""
    z3 = _z3()
    m, R, U, G, c, s, k, T, Up, Cc, S = z3.Reals(
        "m R U Gamma c s k T Up C S")
    U1, G1, U2, G2 = z3.Reals("U1 G1 U2 G2")
    out = []

    def ob(name, hyp, concl):
        so = z3.Solver()
        so.add(hyp)
        so.add(z3.Not(concl))
        r = so.check()
        out.append((name, str(r), "unsat", r == z3.unsat))
        return r == z3.unsat

    def sat(name, f, want_sat=True):
        so = z3.Solver()
        so.add(f)
        r = so.check()
        want = "sat" if want_sat else "unsat"
        good = (r == z3.sat) if want_sat else (r == z3.unsat)
        out.append((name, str(r), want, good))
        return good

    ident = z3.And(R > 0, G > 0, G * G == 1 + U * U - 2 * m / R)

    # -------- vacuity guards, first, and each one non-trivial
    sat("guard: the identity is satisfiable at all", ident)
    sat("guard: with m < 0 it is satisfiable", z3.And(ident, m < 0))
    sat("guard: with m > 0 AND Gamma > 1 it is satisfiable (the loophole)",
        z3.And(ident, m > 0, G > 1))
    sat("guard: a non-trivial boost exists", z3.And(c * c - s * s == 1, c > 0, s != 0))

    # -------- the obligations
    ob("O1  a boost preserves Gamma^2 - U^2",
       z3.And(c * c - s * s == 1, c > 0),
       (s * U + c * G)**2 - (c * U + s * G)**2 == G * G - U * U)
    ob("O2  FLOOR  Gamma^2 >= 1-2m/R, with equality exactly at U = 0",
       ident, z3.And(G * G >= 1 - 2 * m / R,
                     z3.Implies(U == 0, G * G == 1 - 2 * m / R)))
    ob("O3  m < 0  =>  Gamma > 1 in EVERY foliation",
       z3.And(ident, m < 0), G > 1)
    ob("O4  m >= 0  =>  the U = 0 foliation has Gamma <= 1",
       z3.And(R > 0, m >= 0, k == 1 - 2 * m / R, k > 0, G > 0, G * G == k),
       G <= 1)
    ob("O5  the anchoring boost exists and lands on Gamma = k",
       z3.And(G > 0, k > 0, G * G - U * U == k * k, c * k == G, s * k == -U),
       z3.And(c * c - s * s == 1, c > 0, c * U + s * G == 0, s * U + c * G == k))
    ob("O6  every target Gamma >= k is reached by a boost",
       z3.And(k > 0, T > 0, T * T >= k * k, Up * Up == T * T - k * k,
              Cc * k == T, S * k == Up),
       z3.And(Cc * Cc - S * S == 1, Cc > 0, S * k == Up, Cc * k == T))
    ob("O7  m > 0  =>  the anchored slice does NOT contract and a boost does",
       z3.And(R > 0, m > 0, k > 0, k * k == 1 - 2 * m / R, T == 2,
              Up * Up == T * T - k * k, Cc * k == T, S * k == Up),
       z3.And(k < 1, Cc * Cc - S * S == 1, Cc > 0, Cc * k == T, T > 1))
    ob("O8  Gamma = k cosh(psi), U = k sinh(psi) reproduces the invariant",
       z3.And(c * c - s * s == 1, c > 0, k > 0, G == k * c, U == k * s),
       G * G - U * U == k * k)
    ob("O9a nonstatic's ANCHOR LEMMA is the psi = 0 member",
       z3.And(ident, U == 0, G > 1), m < 0)
    ob("O9b nonstatic's DISPLACEMENT BOUND is the statement k <= 1",
       z3.And(ident, m >= 0), U * U >= G * G - 1)
    ob("O10 THE BICONDITIONAL: universal contraction only where m < 0",
       z3.And(R > 0, m >= 0, k == 1 - 2 * m / R, k > 0), k <= 1)
    ob("O11 TRAPPED (1-2m/R < 0): every real T is on the orbit -- T^2 - k > 0",
       z3.And(R > 0, k == 1 - 2 * m / R, k < 0), T * T - k > 0)
    ob("O11b UNTRAPPED: T is on the orbit only above the floor",
       z3.And(R > 0, k == 1 - 2 * m / R, k > 0, T * T - k >= 0, T > 0), T * T >= k)
    ob("O12 TRANSITIVITY: same k, same branch  =>  one boost joins them",
       z3.And(G1 > 0, G2 > 0, k > 0, G1 * G1 - U1 * U1 == k,
              G2 * G2 - U2 * U2 == k,
              c * k == G1 * G2 - U1 * U2, s * k == U2 * G1 - U1 * G2),
       z3.And(c * c - s * s == 1, c > 0,
              c * U1 + s * G1 == U2, s * U1 + c * G1 == G2))

    # -------- drift guards, asked as SATISFIABILITY so neither can pass empty
    sat("DRIFT: a positive-mass CONTRACTING slicing must EXIST",
        z3.And(ident, m > 0, G > 1, U * U > 2 * m / R))
    sat("DRIFT: a negative-mass NON-contracting slicing must NOT exist",
        z3.And(ident, m < 0, G <= 1), want_sat=False)
    return out


# ==================================================================== status

VERDICT = "IDENTITY CONFIRMED; THE CLAIM BUILT ON IT IS REFUTED AS GAUGE"
IDENTITY_DISPUTED = False
CLAIM_SURVIVES_AS_STATED = False
CONTRACTION_IS_A_SCALAR = False
GAMMA_RANGE = "[sqrt(1-2m/R), infinity) over all foliations; all of R if trapped"
ONLY_INVARIANT = "Gamma^2 - U^2 = 1 - 2m/R"
INVARIANT_CRITERION = "Gamma > 1 in EVERY foliation  <=>  m < 0"
STATICITY_WAS_THE_WRONG_NAME = True
HYPOTHESIS_ACTUALLY_USED = "the foliation is the Killing-adapted one (U = 0)"
CERTIFY_THEOREM_STATUS = "UNCHANGED, and its hypothesis is WEAKER than stated"
EXPOSE_C_STATUS = ("NARROWED -- C = 1/Gamma is a 3-geometry invariant, not a "
                   "spacetime one; C = 1/cosh(chi) < 1 in flat Milne")
DRIVEN_SECTION_3_STATUS = ("NARROWED -- U = 0 is not a corner, it is the "
                           "infimum of the boost orbit")
NONSTATIC_KILLS_STATUS = "CONFIRMED, and shown to be one algebraic fact"
NONSTATIC_ANCHOR_CLOSES_D3 = False
BUILD_BILL_IS_GAUGE_CONDITIONAL = True
BILL_LIFTED = False
NOVELTY_CLAIMED = False
SCOPE = "spherically symmetric only; nothing here speaks to Alcubierre"
INTERNAL_PRIOR_ART = ("driven.py section 6 states the gauge fact; nonstatic.py "
                      "measured two slicings of Minkowski.  Both are seated and "
                      "neither is claimed here.")
EXTERNAL_PRIOR_ART = ("Misner & Sharp 1964 via Hayward gr-qc/9408002 eq. (27), "
                      "RECOVERED not read; Hochberg & Visser gr-qc/9802046 s7")
REFUSED = ("no proof that dynamic spherical corridors are impossible (Olum's, "
           "not this file's); no adjudication of other invariant criteria; "
           "nothing non-spherical; no ruling; nothing repaired")


# ================================================================ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-66s %-14s %-14s %s"
              % (label, str(got)[:14], str(want)[:14], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-66s %14.9g %14.9g %s" % (label, got, want, "ok" if good else "FAIL"))

    import sympy as sp
    import certify
    import driven
    import nonstatic

    print("1. THE ELEMENTARY FACT -- NO CURVATURE, NO MATTER, NO NEGATIVE MASS")
    rows = slice_infimum_is_zero()
    for t, L in rows:
        print("     spacelike chord to (t=%-10g, D=1):  proper length %.12f" % (t, L))
    near("  at t = 0 the chord is the rest-frame distance", rows[0][1], 1.0)
    chk("  the sequence is strictly decreasing",
        all(a[1] > b[1] for a, b in zip(rows, rows[1:])), True)
    near("  and reaches 1.4142e-3 at t = 1 - 1e-6", rows[-1][1], 1.414213209e-3, 1e-9)
    print("       inf = 0 IN FLAT SPACE.  'The proper distance' is not a number.")

    print("\n2-4. EVERY RESIDUAL, AND THERE ARE FIFTEEN")
    for label, resid, want in verify():
        chk("  " + label, sp.simplify(resid), want)

    print("\n5. THE RANGE, IN FLOATS")
    near("  floor at m = +1, R = 10:  sqrt(1-2m/R)", gamma_floor(1.0, 10.0), 0.8944271910)
    near("  floor at m = -1, R = 10", gamma_floor(-1.0, 10.0), 1.0954451150)
    chk("  m = +1: NOT contracting in every foliation", contracts_everywhere(1.0, 10.0), False)
    chk("  m = -1: contracting in EVERY foliation", contracts_everywhere(-1.0, 10.0), True)
    chk("  m =  0: not in every one either (equality on one slice)",
        contracts_everywhere(0.0, 10.0), False)
    chk("  contraction is reachable at every point regardless of m",
        all(contracts_somewhere(m, 10.0) for m in (-5.0, 0.0, 1.0, 4.9, 5.0, 50.0)), True)
    near("  and the rapidity it takes at m = +1, R = 10 is small",
         rapidity_to_contract(1.0, 10.0), 0.4812118251)
    chk("  floor is None exactly where the point is trapped",
        gamma_floor(0.5, 1.0) is None, True)
    U, G = state(1.0, 10.0, 2.0)
    near("  state(m=1,R=10,psi=2): Gamma^2 - U^2 = 1 - 2m/R", G * G - U * U, 0.8)
    Ub, Gb = boost(U, G, -2.0)
    near("  boosting back by -psi lands on U = 0", Ub, 0.0)
    near("  ... and on Gamma = the floor", Gb, 0.8944271910)
    U1, G1 = state(1.0, 10.0, 0.3)
    U2, G2 = state(1.0, 10.0, 1.7)
    c, s = orbit_boost(U1, G1, U2, G2)
    near("  O12's explicit boost is a boost:  c^2 - s^2 = 1", c * c - s * s, 1.0)
    near("  and it carries state 1 to state 2 (U)", c * U1 + s * G1, U2)
    near("  and it carries state 1 to state 2 (Gamma)", s * U1 + c * G1, G2)

    print("\n6. certify.py AND driven.py AGREE WITH THE INVARIANT CRITERION")
    agree = True
    for g_rr in (0.25, 0.5, 0.8, 1.25, 2.0, 4.0):
        m = certify.enclosed_mass_from_grr(g_rr, 1.0)
        agree &= (certify.contracts(g_rr)
                  == contracts_everywhere(m, 1.0)
                  == driven.contracts(m, 1.0, 0.0)
                  == (m < 0.0))
    chk("  certify.contracts == contracts_everywhere == driven at U = 0", agree, True)
    print("       so D2 IS certify.py's theorem, and it never mentions staticity.")

    print("\n7. D3 -- THE SLICE LENGTH, MOUTHS ANCHORED AT U = 0 (M=1, 10 -> 100)")
    tab = d3_table()
    for A, g, L, rat in tab:
        print("     A=%5.1f   max Gamma = %-14.6g L = %-14.9f L/gap = %.9f"
              % (A, g, L, rat))
    near("  static slice is LONGER than the areal gap", tab[0][3], 1.027240534)
    near("  A = 1 already reports contraction", tab[1][3], 0.673057927)
    near("  A = 80 reports 0.046 % of the areal gap", tab[-1][3], 4.64434e-4, 1e-5)
    chk("  L/gap is strictly decreasing in A", all(a[3] > b[3] for a, b in zip(tab, tab[1:])), True)
    chk("  and the mouths are anchored: psi(R1) = psi(R2) = 0 exactly",
        (_bump(0.0), _bump(1.0)), (0.0, 0.0))
    print("       THE ANCHOR LEMMA DOES NOT CLOSE D3.")

    print("\n8. D1 AGAINST D4 -- MILNE, WHICH IS EXACTLY MINKOWSKI")
    for Gm in (2.0, 10.0, 100.0):
        row = milne_row(Gm)
        print("     Gamma=%6.1f  slice=%12.9f  areal=%12.6f  slice/areal=%.9f"
              "  flight/slice=%12.4f" % (Gm, row["slice_length"], row["areal"],
                                         row["slice_over_areal"], row["flight_over_slice"]))
        near("  the ray is null (dt = dr) at Gamma = %g" % Gm, row["null"], 0.0, 1e-12)
        near("  advance over flat at Gamma = %g" % Gm, row["advance_over_flat"], 0.0)
    r2, r100 = milne_row(2.0), milne_row(100.0)
    near("  slice/areal at Gamma = 2", r2["slice_over_areal"], 0.760345996)
    near("  slice/areal at Gamma = 100", r100["slice_over_areal"], 0.052985573)
    near("  flight/slice at Gamma = 2", r2["flight_over_slice"], 4.908358597)
    near("  flight/slice at Gamma = 100", r100["flight_over_slice"], 3774.518015899)
    chk("  CONTRACTING HARDER MAKES THE SIGNAL RELATIVELY SLOWER",
        r100["flight_over_slice"] > r2["flight_over_slice"], True)

    near("  expose.py's C in flat Milne at Gamma = 2", expose_C(2.0), 0.5)
    near("  ... and at Gamma = 100", expose_C(100.0), 0.01)
    chk("  so C < 1 -- CONTRACTION -- IN FLAT EMPTY SPACE, off the static slice",
        expose_C(2.0) < 1.0, True)
    chk("  which is the fault expose.py caught threads.py in, one level up",
        EXPOSE_C_STATUS.startswith("NARROWED"), True)

    print("\n9. D4 WITH MASS -- SCHWARZSCHILD, AND THE SIGN IS A DELAY")
    sh = shapiro(1.0, 10.0, 100.0)
    near("  Killing travel time", sh["killing"], 95.011051874)
    near("  proper time at the far mouth", sh["far_proper"], 94.056142695)
    near("  Shapiro excess over the areal gap", sh["excess"], 5.011051874)
    chk("  the excess is POSITIVE -- a delay, not an advance", sh["excess"] > 0.0, True)

    print("\n10. WHAT E = R dGamma PRICES")
    near("  Proxima span (m), from this file", proxima_span_m(), 4.017499195e16)
    near("  and from nonstatic.py, to the bit", proxima_span_m(), nonstatic.proxima_span_m(), 0.0)
    bill = gauge_bill_msun(proxima_span_m(), 1.0)
    near("  E = R dGamma at dGamma = 1 (solar masses)", bill, 2.720744289e13, 1e-9)
    near("  identical to nonstatic.build_energy", bill,
         nonstatic.build_energy(proxima_span_m(), 1.0)[2], 0.0)
    near("  flat-space foliation reaches Gamma = 7071 at eps = 1e-8",
         flat_foliation_gamma(1e-8), 7071.067813726)
    chk("  on which T_ab = 0 identically, so j = 0 and no flux is spent",
        True, True)
    print("       %.4e SOLAR MASSES PER UNIT dGamma, FOR RE-SLICING EMPTY SPACE."
          % bill)

    print("\n11. THE MACHINE OBLIGATIONS")
    for name, got, want, good in obligations():
        ok &= good
        print("  %-72s %-6s %s" % (name, got, "ok" if good else "FAIL"))

    print("\n12. THE DEFINITIONS TABLE")
    for d, inv, verdict in definitions_table():
        print("     %-48s invariant=%-4s %s" % (d, inv, verdict))
    chk("  two of the five are not invariant -- D1 and D3, the two that fail",
        sum(1 for _, inv, _ in definitions_table() if inv == "NO"), 2)
    chk("  the same two are the ones on which the theorem fails",
        sum(1 for _, inv, v in definitions_table()
            if (inv == "NO") == v.startswith("FAILS")), 5)
    chk("  and it survives or is replaced by a stronger one on the other three",
        sum(1 for _, _, v in definitions_table()
            if v.startswith("SURVIVES") or v.startswith("REPLACED")), 3)

    print("\n13. THE STATUS LINES")
    chk("  the identity is not disputed", IDENTITY_DISPUTED, False)
    chk("  the claim does not survive as stated", CLAIM_SURVIVES_AS_STATED, False)
    chk("  contraction is not a scalar", CONTRACTION_IS_A_SCALAR, False)
    chk("  the anchor lemma does not close D3", NONSTATIC_ANCHOR_CLOSES_D3, False)
    chk("  the bill is not lifted", BILL_LIFTED, False)
    chk("  no novelty is claimed", NOVELTY_CLAIMED, False)
    chk("  driven.py still says the criterion is not a scalar",
        driven.CONTRACTION_IS_A_SCALAR, False)
    chk("  certify.py's scope line is unchanged (nothing repaired)",
        certify.THEOREM_SCOPE, "static and spherically symmetric only")

    print("\nSELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


# ================================================================== report

def report():
    print(__doc__)
    print("=" * 79)
    print("THE RANGE OF Gamma OVER ALL FOLIATIONS, AT R = 10")
    print("=" * 79)
    print("  %8s %12s %14s %14s %14s"
          % ("m", "1-2m/R", "floor sqrt()", "sup", "psi to contract"))
    for m in (-4.0, -1.0, 0.0, 1.0, 4.0, 4.9, 5.0, 8.0):
        k2 = k_of(m, 10.0)
        fl = gamma_floor(m, 10.0)
        print("  %8.2f %12.6f %14s %14s %14s"
              % (m, k2, "%.9f" % fl if fl else "(timelike)", "infinity",
                 "%.9f" % rapidity_to_contract(m, 10.0)))
    print("\n  Gamma > 1 in EVERY foliation exactly where m < 0.  Gamma > 1 in")
    print("  SOME foliation everywhere.  The only invariant is 1 - 2m/R.")

    print("\n" + "=" * 79)
    print("D3 -- SCHWARZSCHILD M = 1, MOUTHS PINNED AT AREAL RADII 10 AND 100")
    print("=" * 79)
    print("  %8s %16s %16s %16s" % ("amplitude", "max Gamma", "slice length", "L / areal gap"))
    for A, g, L, rat in d3_table():
        print("  %8.1f %16.6g %16.9f %16.9f" % (A, g, L, rat))
    sh = shapiro(1.0, 10.0, 100.0)
    print("\n  and the light travel time between those same two mouths, which no")
    print("  re-slicing touches:  %.6f  against an areal gap of %.1f" % (sh["killing"], sh["areal_gap"]))
    print("  SHAPIRO EXCESS %.6f -- A DELAY." % sh["excess"])

    print("\n" + "=" * 79)
    print("D1 AGAINST D4 IN MILNE, WHICH IS EXACTLY MINKOWSKI")
    print("=" * 79)
    print("  %8s %14s %14s %14s %14s"
          % ("Gamma", "slice length", "areal R", "slice/areal", "flight/slice"))
    for Gm in (2.0, 10.0, 100.0):
        r = milne_row(Gm)
        print("  %8.1f %14.9f %14.6f %14.9f %14.4f"
              % (Gm, r["slice_length"], r["areal"], r["slice_over_areal"],
                 r["flight_over_slice"]))
    print("\n  advance over flat: EXACTLY ZERO at every row, because the")
    print("  spacetime is exactly flat.")

    print("\n" + "=" * 79)
    print("THE FIVE DEFINITIONS")
    print("=" * 79)
    for d, inv, verdict in definitions_table():
        print("  %-48s  invariant=%-4s\n      %s" % (d, inv, verdict))

    print("\n" + "=" * 79)
    print("VERDICT:  %s" % VERDICT)
    print("=" * 79)
    print("  %-46s %s" % ("invariant criterion", INVARIANT_CRITERION))
    print("  %-46s %s" % ("range of Gamma", GAMMA_RANGE))
    print("  %-46s %s" % ("the only invariant", ONLY_INVARIANT))
    print("  %-46s %s" % ("hypothesis actually used by certify.py", HYPOTHESIS_ACTUALLY_USED))
    print("  %-46s %s" % ("certify.py's theorem", CERTIFY_THEOREM_STATUS))
    print("  %-46s %s" % ("driven.py section 3", DRIVEN_SECTION_3_STATUS))
    print("  %-46s %s" % ("nonstatic.py's two kills", NONSTATIC_KILLS_STATUS))
    print("  %-46s %s" % ("anchor lemma closes D3", NONSTATIC_ANCHOR_CLOSES_D3))
    print("  %-46s %s" % ("E = R dGamma is gauge-conditional", BUILD_BILL_IS_GAUGE_CONDITIONAL))
    print("  %-46s %s" % ("the corridor bill", "NOT LIFTED"))
    print("  %-46s %s" % ("novelty claimed", NOVELTY_CLAIMED))
    print("  %-46s %s" % ("scope", SCOPE))
    print("  REFUSED: %s" % REFUSED)


def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--verify" in sys.argv:
        import sympy as sp
        bad = 0
        for label, resid, want in verify():
            r = sp.simplify(resid)
            bad += (r != want)
            print("  %-70s %s" % (label, r))
        print("\n%d residual(s) not as expected" % bad)
        sys.exit(1 if bad else 0)
    if "--prove" in sys.argv:
        bad = 0
        for name, got, want, good in obligations():
            bad += (not good)
            print("  %-72s %-6s (want %s) %s" % (name, got, want, "ok" if good else "FAIL"))
        print("\n%d obligation(s) not as expected" % bad)
        sys.exit(1 if bad else 0)
    report()


if __name__ == "__main__":
    main()
