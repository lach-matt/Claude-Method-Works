#!/usr/bin/env python3
"""
phase1.py -- PHASE 1: THE TRANSITION, DEFINED AND PROVED.

Thirty-one passes produced 257 findings.  This file does not add one.  It steps
back, states what a TRANSITION is, proves what can be proved about it, prices
it, and ranks the candidates on the two criteria that were asked for: THE
FASTEST OPERATOR AND THE LOWEST COST.

Everything here is either proved from the definition, or measured by an
instrument named at the claim.  Nothing is asserted.

===============================================================================
THE DEFINITION
===============================================================================

A TRANSITION between two declared endpoints A and B is a one-parameter family
of metrics g_s on a FIXED manifold, s in [0,1], satisfying five conditions:

    D1  ENDPOINTS ARE LABELS, NOT WORLDLINES.  A and B are the same points of
        the manifold at every s.  Nothing is transported anywhere by the
        operator itself.

    D2  COMPACT SUPPORT.  g_s = g_0 outside a compact corridor K containing A
        and B.  The universe outside K does not know this happened.
        CORRECTED (DOCKET 67): the seated Phi meets D2 only approximately.
        Its Plummer core is not cut at R_s: outside the shell Phi is about
        -m a^2/(2 r^3), not 0 (formation.py's SEATED_COMPACT_SUPPORT is
        False), contributing -5.0e-9 per unit m to the contraction.  M_ADM = 0
        holds exactly.  This moves neither the core's energy-condition
        violation nor the positive-mass route.

    D3  THE PROPER DISTANCE FALLS.  d_s(A,B), measured on the slice, is
        decreasing in s.  This is the ONLY thing the operator does.

    D4  NO MOMENTUM, IN TWO PARTS (restated on M's ruling, DOCKET 64):
        (i)  T^{0i} = 0 in EVERY CONFIGURATION g_s the device holds, read in
             that configuration's adapted (static) coordinates; and
        (ii) ZERO NET MOMENTUM across any passage between configurations --
             no thrust, no exhaust, no reaction mass, no centre-of-mass motion.
        It was first written "T^{0i} = 0 throughout".  formation.py proved that
        every passage from flat space holding areal radii fixed carries
        T^{0r} != 0 at some instant wherever the enclosed mass is negative
        (F1, THEOREM), radially and with zero net momentum.  Kept pointwise,
        D4 would class FORMING the device as propulsion by this file's own
        classifier, though nothing is pushed anywhere.  Restated, a device
        that actually thrusts still fails D4 (ii), and Alcubierre still fails
        D4 (i).  D4_AS_FIRST_WRITTEN keeps the original.
        CORRECTED (DOCKET 67): T^{0i} is a component, not an invariant --
        coordinate T^{0i} = J^i - rho_E beta^i -- and (i) as first restated
        named no frame.  The frame is a hypothesis of D4 (i): the same static
        geometry written in Galilean-moving coordinates X = x - v t has
        T^{0x} = v T^{00} != 0.  For Alcubierre the verdict is the same in the
        coordinate, Eulerian and invariant readings.

    D5  BOTH ENDPOINTS DECLARED AT ONSET.  The family is not defined until A
        AND B are both given.  (transit.py's gate, which refuses to initialise
        part 2 without a declared arrival.)

    *** SCOPE, ADDED BY create.py: D1-D5 WAS WRITTEN FOR THE CORRIDOR. ***

    D1 fixes the MANIFOLD and D2 asks for a compactly supported metric change
    on it.  A WORMHOLE GATE FAILS D2 -- not by a little, and not on size: R^3
    is simply connected and a handle (intra-universe) wormhole is not, and no
    continuous deformation of a metric on a fixed manifold bridges that at any
    support.  CORRECTED (DOCKET 67): first written 'a wormhole is not', with
    no qualifier.  The Morris-Thorne inter-universe section R x S^2 IS simply
    connected; it differs from R^3 through H_2 = Z, a second end, and the
    conclusion holds through that instead.  A Hochberg-Visser trivial-topology
    wormhole has R^3 itself as its section.  The candidate
    ranking below has no throat architecture in it either.

    So "PHASE 1 IS FINISHED AS MATHEMATICS" is finished ABOUT THE CORRIDOR.
    The definition is not wrong; it is narrower than the architecture this
    project has since adopted, and create.py records what that costs -- chiefly
    that CREATING a gate's handle or second end is a TOPOLOGY problem with its
    own theorem, harsher in kind than the source problem, while ENLARGING a
    throat is a metric problem that every instrument here already covers.
    CORRECTED (DOCKET 67): first written 'CREATING a throat is a TOPOLOGY
    problem'.  A throat alone is not: DOCKET 67 built a smooth family on FIXED
    R^3, unchanged outside 1 < r < 3, that acquires a minimal 2-sphere with
    flare-out (R' = 0, R'' = 14.2 > 0 at r = 1.993) from s ~ 0.277 on.  That
    throat opens into a bounded region, not onto a shortcut, so it is not a
    gate; what needs a topology change is the handle or the second end.

    A CONSTRUCTION SATISFYING D1-D5 IS A TRANSITION.  ONE VIOLATING D4 IS
    PROPULSION AND IS NOT IN SCOPE.  Alcubierre's shift vector violates D4 (i),
    and that is the whole reason it is a different object.  CORRECTED (DOCKET
    67): first written 'by construction'.  It follows from his particular
    shift, not from the presence of one: for unit lapse and flat slices
    8 pi J_i = -(1/2)(curl curl beta)_i exactly, and Alcubierre's shift has
    curl curl beta != 0.  DOCKET 67 computed his T^{0i} != 0 (coordinate,
    Eulerian and invariant readings); his paper computes only T^{00}.

===============================================================================
THEOREM 1 -- THE QUANTITY IS PROPER DISTANCE, NOT LIGHT TIME
===============================================================================

For a static metric in isotropic form, g_tt = -e^{2Phi}, g_ij = e^{-2Phi}
delta_ij, a payload at rest at A has four-velocity u = e^{-Phi} d/dt.  What "how
far away is B" means for THAT observer is the spatial length on its own slice:

        d(A,B)  =  int e^{-Phi} dl              THE TRANSITION QUANTITY

whereas the coordinate time for a light signal is

        t(A,B)  =  int e^{-2Phi} dl             THE PROPULSION QUANTITY

    ONE Phi, TWO EXPONENTS, RATIO EXACTLY 2 -- exactly for the exponents.  For
    the savings the ratio is (1 - e^{-2Phi})/(1 - e^{-Phi}) = 1 + e^{-Phi}
    = 2 - Phi + ..., which is 2 to first order (unified.py measured 1.9940 to
    2.0229 over both signs of Phi); in PPN terms it is (1 + gamma)/gamma, so it
    carries gamma = 1.  (CORRECTED, DOCKET 67: 'EXACTLY' was not scoped.)  They cannot be moved separately, and the
    one a transition acts on is the FIRST.  Asking whether the second beats
    flat space is asking a propulsion question, which is why chronology.py's
    answer to it -- LATE, at every range past X_c -- does not touch this.

===============================================================================
THEOREM 2 -- NO MOMENTUM.  THIS IS NOT PROPULSION.
===============================================================================

For any static Phi, in static-adapted coordinates, the mixed components of
the Einstein tensor vanish identically: G^{0i} = 0, hence T^{0i} = 0.
transition.py returns exactly 0.0 -- but that zero is built into the code
(every time derivative set to zero, a diagonal metric installed), so the check
could not have failed; the theorem carries it, not a measurement.  D4 (i) is
not an extra assumption on the construction; it is automatic for anything
static.

    STATIC IS SUFFICIENT FOR D4 (i).  IT IS NOT NECESSARY, AND A SHIFT VECTOR
    IS NOT SUFFICIENT TO FAIL IT.

CORRECTED (DOCKET 67).  First written: 'MEASURED EXACTLY 0.0, not to a
tolerance', '... and it fails automatically for anything with a shift vector',
and 'SO THE STATIC/DYNAMIC SPLIT IS EXACTLY THE TRANSITION/PROPULSION SPLIT.
That is the cleanest thing in this file.'  DOCKET 67 computed counterexamples
to the converse: flat space with a constant shift, flat space with a
rigid-rotation shift, Painleve-Gullstrand Schwarzschild, and Kerr in
Boyer-Lindquist (non-static, with a shift no coordinate change removes) all
carry a shift and have T^{0i} = 0; a gradient shift at unit lapse has Eulerian
J = 0 exactly.  For unit lapse and flat slices the criterion is
curl curl beta != 0.  Time dependence with no shift at all gives G_{01} != 0.
This file's verdict uses only the forward direction, static => no momentum,
and that stands.

===============================================================================
THEOREM 3 -- HOLDING IT IS FREE
===============================================================================

A static configuration does no work: budget.py's is_powered() is False, and
stability.py measures the shell radially STABLE at beta^2 = 0 (V'' = +2.965e-2
against an ordinary shell's -3.036e-2).  Once established, the corridor holds
itself.

    THE CORRIDOR IS NOT A MACHINE THAT RUNS.  IT IS A SHAPE THAT STAYS.

===============================================================================
THEOREM 4 -- A SINGLE TRANSITION CAN NEVER BEAT LIGHT
===============================================================================

The metric is evolved by a hyperbolic system with characteristic speed c, and
matter acting in a compact region cannot alter the metric outside its causal
future.  A corridor of coordinate length L, established by agents acting inside
it, is therefore not complete before L/2c after the first action -- best case,
acting from the midpoint -- and an endpoint cannot know it is complete before
then either.

    HYPOTHESES, NAMED (DOCKET 67; first left unnamed): classical matter whose
    own characteristics are causal (speed <= c); the maximal globally
    hyperbolic development; and every action causally downstream of ONE
    event.  The first is not free here -- the corridor is exotic by this
    file's own record (D4, formation.py F1) -- and a matter cone of speed
    v > c halves the floor to L/4c (violating the WEC or DEC does not by
    itself widen the domain of influence: Kontou-Sanders).  WEC-violating
    matter is not barred from a compactly generated Cauchy horizon
    (Kay-Radzikowski-Wald), beyond which no uniqueness is supplied, and
    quantum sources are outside the theorem.  N actors already in place
    complete at L/(2Nc) after the first action: the floor moves to placing
    them; it does not vanish.

    COROLLARY: the first traversal cannot arrive before a light signal
    despatched when establishment began.  THE TRANSITION IS NEVER A LEAD.

    This is not a defect and it is not chronology protection.  It is the price
    of D2: a compactly supported change has to be made, and making it is
    causal.  chronology.py's separate result -- that the light time is LATE at
    range for every weak-field configuration -- is the same wall seen from the
    propulsion side.

===============================================================================
THEOREM 5 -- SO ALL THE VALUE IS IN AMORTISATION, AND HERE IT IS AVAILABLE
===============================================================================

Theorems 3 and 4 together say the whole question is: IS THE ESTABLISHMENT PAID
ONCE OR PER USE?

    GJW'S 2016 PROTOCOL: PER USE.  Each coupling pulse opens one short window
    ("only open for a small proper time", sec. 5).  That per-use reading is
    THIS TREE'S INFERENCE (amortize.py's), not GJW's statement: their sentence
    -- in flat space the coupling would be produced by ambient propagation,
    "the same as the interaction we studied, EXCEPT WITH A TIME DELAY" --
    says how a flat-space coupling would be produced, and nothing about per
    use against built once.  CORRECTED (DOCKET 67): first written "GJW: PER
    USE.  Their own sentence closes it", following amortize.py's "CLOSED by
    the source".  The case GJW's footnote 2 declined has since been built,
    static and reusable: Maldacena-Qi 1804.00491 (an eternal traversable
    wormhole from a time-independent coupling) and Maldacena-Milekhin-Popov
    1807.04726 (4D, asymptotically flat, the coupling carried by ambient
    exchange, and no lead over the ambient path).  So "not reusable" holds
    for the 2016 protocol, not for the GJW class.

    A STATIC CORRIDOR: PAID ONCE.  It is not a coupling and it is not a signal.
    It is a shape, it holds itself (Theorem 3), and nothing about it is
    per-use.

    THIS IS WHERE THE AMORTISATION ARGUMENT THAT FAILED FOR GJW'S 2016
    PROTOCOL SUCCEEDS, AND THE REASON IS TIME INDEPENDENCE -- WHAT GJW'S
    FOOTNOTE 2 DECLINED TO CONSIDER FOR THEIR INTERACTION.  CORRECTED (DOCKET
    67): first written "A TIME-INDEPENDENT CONFIGURATION".  The footnote says
    "time-independent interaction" and declines only an interaction that is
    time-independent for all t; GJW did compute a coupling switched on and
    held (Fig. 3.1a, eq. 3.18), and the geometry is time-dependent in every
    case they computed.

    Amortised over N traversals the establishment contributes L/(2Nc), which
    goes to zero.  What is left is the reduced proper distance, permanently.

===============================================================================
THE TRANSITION EQUATION
===============================================================================

Measured, then matched to closed form, then checked for linearity:

        Delta d  =  (G/c^2) * M * Lambda,   Lambda = 2[ln(2 R_s / sqrt(b^2+a^2)) - 1]

  * SATURATES, once both endpoints lie outside the shell (X >= R_s).  The
    contraction agrees to about 7.8 digits at half-baselines 400, 2000 and
    20000 in this file's Simpson run (relative spread 1.5e-8 to 1.8e-8; exact
    quadrature gives 1.26e-10).  It does not grow with the distance being
    contracted.  With the endpoints inside the shell (X = 50, 100, 150) the
    contraction per unit m is 8.680, 9.566 and 9.877, and it does grow.
    CORRECTED (DOCKET 67): first written with b where lam() uses
    sqrt(b^2 + a^2) (9.982929 against 9.982529, 4.0e-5), as "IDENTICAL TO
    NINE DIGITS", and with the outside-the-shell condition unnamed.
  * LINEAR IN MASS.  Contraction per unit m: 9.975, 9.967, 9.952, 9.923, 9.864
    over m = 5e-3 to 8e-2 -- constant to 1 %, drifting only by the Phi^2 term.
  * Lambda = 9.9825 from the closed form against 9.975 measured at m = 5e-3.
    AGREEMENT TO 0.08 %.

    SO THE CONTRACTION IS PROPORTIONAL TO MASS AND INDEPENDENT OF THE DISTANCE
    CONTRACTED.  Lambda is a pure geometric factor of order ten, and it can be
    improved only LOGARITHMICALLY, through R_s/b.

    At the seated geometry (R_s/b and a/b fixed) there is no free parameter
    left, and R_s/b moves Lambda only logarithmically (lambda_cost_of_improving).
    This is the whole physics of the object.  (CORRECTED, DOCKET 67: first
    written "There is no free parameter left", unscoped.)

===============================================================================
THE PRICE OF THE CORRIDOR -- THE LOWEST COST AMONG ENTRIES THAT KEEP D2
===============================================================================

        exchange rate    c^2/(G Lambda)  =  1.349e26 kg per metre contracted
        one solar mass   buys 14.7 km of contraction
        Proxima, 4.2465 ly, contracted by 1 %   ->   2.72e10 solar masses
        Proxima, 4.2465 ly, contracted by 50 %  ->   1.36e12 solar masses

    A GALAXY OF NEGATIVE MASS TO SHAVE ONE PERCENT OFF THE ROAD TO PROXIMA
    (ALPHA CENTAURI C).

    CORRECTED (DOCKET 67 follow-up, M: "repair all figures").  First written
    at L = 4.0 ly -- 2.57e10 (1 %) and 1.28e12 (50 %) solar masses -- under
    the heading 'THE PRICE, AND IT IS THE ANSWER TO "LOWEST COST"' and the
    sentence '... OFF ALPHA CENTAURI'.  Re-based on the target the tree seats
    everywhere else, Proxima at its Gaia DR3 parallax (READ via Reyle 2021
    Table 1; L_PROXIMA, 4.2464599 ly at J2016.0): 2.72477e10 and 1.36238e12,
    6.2 % higher.  Alpha Cen AB, priced beside it at its three READ orbital
    parallaxes (4.344 to 4.390 ly), gives 2.787e10 to 2.817e10 (1 %) and
    1.394e12 to 1.408e12 (50 %).  Every one stays in the 1e10-Msun decade, so
    the galaxy sentence stands.  The heading is narrowed because the bare
    negative mass, included on M's ruling, is cheaper per unit |M| at every
    baseline the corridor's saturated law covers (THE RANKING below): with
    the shell spanning the baseline (X = R_s, the same b) its Lambda is
    11.98, so its 1 % price at Proxima is 0.833 of the corridor's, 2.27e10
    solar masses -- still a galaxy -- and it falls further, logarithmically,
    with any wider baseline or narrower b.  It pays in D2.

    CORRECTED (DOCKET 67).  Both corrections raise the price; the decade, and
    the sentence above, stand.
      * 4.0 ly is a round baseline, not the named star's distance.  READ at
        source: alpha Cen AB at 4.344 to 4.390 ly (orbital parallaxes 750.81,
        747.17 and 743 mas: Akeson 2021, Kervella 2016, Pourbaix-Boffin 2016)
        and Proxima at 4.246 ly (768.13 mas, Lurie 2014 as restated in
        Kervella 2016).  Every figure linear in L is 6-10 % higher there: the
        1 % price prints 2.7e10 (Proxima) to 2.8e10 (AB) and the 50 % price
        1.36e12 to 1.41e12.  [Applied by the follow-up above: the figures are
        now priced at Proxima's Gaia DR3 distance.]
      * The two prices use the first-order law outside its window.  With the
        endpoints outside the shell at the seated R_s/b = 200 they need
        m >= 0.401 (1 %) and m >= 20.04 (50 %); the measured window ends at
        m = 0.08, where the seated geometry covers contractions up to 0.200 %.
        The exact ansatz contraction at those m is 0.944 and 0.403 of the
        linear law, so the 1 % price is 5.9 % low; at 50 % the peak potential
        is about 20, not weak field, and what GR gives there is OPEN.

    That is the honest order of magnitude and it is not improvable by
    cleverness in THIS architecture (the corridor), because Delta d is LINEAR
    in M (to first order) with a coefficient fixed by c^2/G and a logarithm.  At the seated
    geometry nothing is left to optimise but that logarithm's R_s/b.  (First
    written "Nothing in the geometry is left to optimise".)

===============================================================================
WHAT PHASE 1 ESTABLISHES, PLAINLY
===============================================================================

    THE TRANSITION IS WELL DEFINED.        D1-D5, and they are checkable.
    IT IS NOT PROPULSION.                  Theorem 2, exactly and structurally.
    IT IS NOT FORBIDDEN BY THE CHRONOLOGY  Because it violates the energy
    OR POSITIVE-MASS THEOREMS.             conditions they assume -- see below.
    IT IS NEVER A LEAD.                    Theorem 4.
    ITS VALUE IS ENTIRELY AMORTISED.       Theorem 5, and that route is open
                                           here and closed for GJW.
    AND IT COSTS 1.349e26 kg PER METRE.    The transition equation.
    A BARE NEGATIVE MASS COSTS LESS        THE RANKING (DOCKET 67 follow-up,
    AND FAILS D2.                          M: 'include it'): M_ADM = -|M|.

    CORRECTED (DOCKET 67): the third line was first written "IT IS NOT
    FORBIDDEN.  No energy condition, no chronology theorem and no positive-mass
    theorem is violated by D1-D5 with M_ADM = 0."  The seated device violates
    NEC, WEC, SEC and DEC at every 0 < r < R_s (8 pi (rho + p_t) =
    -6 m a^2 e^{2Phi}/(r^2 + a^2)^{5/2} < 0 there).  The chronology and
    positive-mass theorems assume an energy condition, so their clauses hold
    only because the first clause fails: one violation and two consequences
    of it, not three permissions.  With the DEC kept, M_ADM = 0 with a
    non-flat static slice is excluded by the PMT's rigidity clause (the
    seated slice has R(0) < 0).  The chronology clause is vacuous for held
    static configurations and unchecked for passages: OPEN.

    The physics is settled.  What is not settled is the source: everything
    above needs M < 0, and achievable.py's 65 orders and core.py's Type I
    specification are where that stands.  THAT IS PHASE 2, AND IT IS NOT A
    MATHEMATICS PROBLEM.

stdlib only.
"""
import math, sys

# c exact, G the CODATA 2018 point value.  DOCKET 67: G's u_r = 2.2e-5 is an
# expanded uncertainty over mutually inconsistent inputs, so the figures here
# hold to about 4-5 significant figures.  SOLAR_MASS = 1.98892e30 equals
# GM_sun/G for G = 6.67259e-11 (CODATA 1986, by numerical match); with this
# file's G it misses the nominal (GM)^N_sun = 1.3271244e20 by +2.57e-4, so the
# solar-mass figures hold to about 3.6 significant figures -- every figure
# printed, not the constants' fifth digit.
# CORRECTED (DOCKET 67 follow-up, M: "repair all figures").  LIGHT_YEAR was
# typed 9.4607e15, a 5-figure truncation of c x Julian year (-3.2e-6), so
# 4 ly / 2c came out 1.9999936 Julian years, not exactly 2.  It is now
# COMPUTED as c x 365.25 x 86400 s = 9460730472580800 m (the IAU light year;
# the definition is NAMED-NOT-READ and used only as an exact constant, as
# foliation.py and ladder.py use it).
C_SI, G_SI = 2.99792458e8, 6.67430e-11
JULIAN_YEAR_S = 365.25 * 86400.0
SOLAR_MASS, LIGHT_YEAR = 1.98892e30, C_SI * JULIAN_YEAR_S
A_CORE, R_SHELL, B_RAY = 0.02, 200.0, 1.0

# THE TARGET (DOCKET 67 follow-up, M: "repair all figures").  The corridor was
# priced at L = 4.0 ly, a round baseline that named no star but was attached
# to "Alpha Centauri".  It is now priced at PROXIMA CENTAURI (alpha Cen C):
#   * it is the tree's seated destination -- foliation.PROXIMA_LY (re-exported
#     by ledger.py), closeout, nonstatic, oneway, driven and mouth all price
#     the corridor there, so the tree now prices ONE corridor at ONE distance;
#   * its distance is a single catalogue trigonometric parallax with formal
#     relative sigma 6.5e-5, whereas alpha Cen AB has only orbital parallaxes
#     in 5.77-sigma mutual tension (743 / 747.17 / 750.81 mas) and no Gaia
#     standard solution (Akeson 2021 p.9; Kervella 2016 sec 5.3).
# The parallax is READ-VIA-RESTATEMENT (DOCKET 67, key gaia-dr3-proxima-
# distance): Gaia EDR3 = DR3, 768.066539187357 +- 0.049872905 mas at epoch
# J2016.0, as printed in Reyle et al. 2021, arXiv:2104.14972 Table 1; DR3
# astrometry = EDR3 READ in Vallenari et al. 2022, arXiv:2208.00211 sec 3.2.
# NAMED HYPOTHESES on the distance: d = 1/parallax (inversion bias ~4e-9);
# epoch J2016.0 -- by 2026.74 the radial approach moves it -1.89e-4 relative,
# below every figure printed here; the zero-point bias is NOT subtracted (the
# Lindegren 2021 recipe is invalid at Proxima's colour; illustrated, it moves
# the distance -3e-5 to -5e-5).  The au (149597870700 m) and the parsec
# (648000/pi au) are IAU definitions, NAMED-NOT-READ, used as exact constants.
GAIA_DR3_PROXIMA_PARALLAX_MAS = 768.066539187357
AU_M = 149597870700.0
L_PROXIMA = AU_M * 648000.0 / math.pi / (GAIA_DR3_PROXIMA_PARALLAX_MAS / 1000.0)
#: alpha Cen AB, READ (DOCKET 67, key alpha-centauri-distance-4ly): orbital
#: parallaxes Akeson 2021 (arXiv:2104.10086 p.14), Kervella 2016
#: (arXiv:1610.06079 p.1), Pourbaix-Boffin 2016 (arXiv:1601.01636 p.2).
#: Priced beside the target, not as it.
ALPHA_CEN_AB_PARALLAX_MAS = (750.81, 747.17, 743.0)
#: The baseline first written, kept so the correction has an object.
L_AS_FIRST_WRITTEN_LY = 4.0


# ------------------------------------------------------------ the definition

CONDITIONS = (
    ("D1", "endpoints are labels, not worldlines",
     "A and B are the same manifold points at every s"),
    ("D2", "compact support",
     "g_s = g_0 outside a compact corridor K"),
    ("D3", "the proper distance falls",
     "d_s(A,B) decreasing in s -- the only thing the operator does"),
    ("D4", "no momentum: T^{0i} = 0 in each configuration (in its adapted "
           "frame), and zero net momentum across a passage",
     "no thrust, no exhaust, no reaction mass -- restated on M's ruling "
     "(DOCKET 64): a transient flux with zero net momentum, which formation "
     "provably requires (formation.py F1), is not propulsion"),
    ("D5", "both endpoints declared at onset",
     "transit.py's gate: part 2 will not initialise without an arrival"),
)


#: D4 as first written, kept so the restatement has an object (M's ruling,
#: DOCKET 64 ruling D.2).
D4_AS_FIRST_WRITTEN = "no momentum: T^{0i} = 0 throughout"
D4_RESTATED_ON_M_RULING = True


def is_transition(has_momentum_flux, endpoints_declared, distance_falls,
                  compact, labels_fixed, net_momentum=False, passage_flux=False):
    """D1-D5, with D4 as restated on M's ruling.  has_momentum_flux is T^{0i} != 0
    IN A CONFIGURATION the device holds -- D4 (i); net_momentum is a non-zero net
    momentum across a passage -- D4 (ii).  Either makes the construction
    PROPULSION.  passage_flux, a transient T^{0i} != 0 during a passage with zero
    net momentum, is accepted and does NOT: that is what formation requires."""
    return (labels_fixed and compact and distance_falls
            and not has_momentum_flux and not net_momentum
            and endpoints_declared)


def alcubierre_is_propulsion():
    """Alcubierre's shift gives T^{0i} != 0, so D4 fails.  Different object.

    CORRECTED (DOCKET 67): first written 'The shift vector gives T^{0i} != 0'.
    It is passed here as the input True, not computed, and Alcubierre's paper
    computes only T^{00}.  DOCKET 67 computed it true for his metric (his
    shift has curl curl beta != 0); a shift as such does not give it (flat
    constant shift, rigid rotation, Kerr: T^{0i} = 0).
    """
    return not is_transition(True, True, True, True, True)


# --------------------------------------------------- Theorem 1: the quantity

def phi_device(x, b, m, a=A_CORE, Rs=R_SHELL):
    """Phi of the seated device.  m > 0 is the MAGNITUDE of a negative core
    mass: with g_tt = -e^{2Phi} the Newtonian identification is Phi = -U, so
    Phi > 0 here is M < 0 (sign convention named, DOCKET 67)."""
    r = math.hypot(x, b)
    return m / math.sqrt(r * r + a * a) - m / max(r, Rs)


def _simpson(f, X, n=100001):
    h = 2.0 * X / n
    s = 0.0
    for i in range(n + 1):
        x = -X + i * h
        s += (1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)) * f(x)
    return s * h / 3.0


def proper_contraction(m, b=B_RAY, X=20000.0, n=100001):
    """int (1 - e^{-Phi}) dl -- THE TRANSITION QUANTITY.  Positive = shorter."""
    return _simpson(lambda x: 1.0 - math.exp(-phi_device(x, b, m)), X, n)


def light_saving(m, b=B_RAY, X=20000.0, n=100001):
    """int (1 - e^{-2Phi}) dl -- the PROPULSION quantity.  Not what we act on."""
    return _simpson(lambda x: 1.0 - math.exp(-2.0 * phi_device(x, b, m)), X, n)


def exponent_ratio(m=2.0e-2):
    """Exactly two: e^{-2Phi} against e^{-Phi}.  One Phi moves both."""
    return light_saving(m) / proper_contraction(m)


# ------------------------------------------------- Theorems 2 and 3, by import

def no_momentum():
    """T^{0i} = 0 EXACTLY for a static Phi.  Measured, not bounded."""
    import transition, concentric
    mx, _t00 = transition.momentum_flux(concentric.potential(2.0e-2),
                                        (1.0, 1.0, 0.0), 2.0e-2)
    return mx == 0.0


def holding_is_free():
    """Static => no power (budget.py) and radially stable (stability.py)."""
    import budget, stability
    return (not budget.is_powered()
            and stability.V_second(*stability.device(2.0e-2), 0.0) > 0.0)


# ----------------------------------------------- Theorem 4: the operator's floor

def establishment_time(L_metres):
    """L/2c: best case for agents acting from ONE causal origin at the midpoint.

    CORRECTED (DOCKET 67): first written 'best case, acting from the midpoint',
    which presumes a single causal origin -- N actors already in place
    complete at L/(2Nc) after the first action -- and matter whose
    characteristics are causal (Theorem 4's named hypotheses).

    A compactly supported metric change is made by matter, and matter cannot
    alter the metric outside its own causal future.  So the corridor is not
    complete, and no endpoint can know it is complete, before this.
    """
    return L_metres / (2.0 * C_SI)


def single_transition_total(L_metres):
    """Establishment plus one traversal at c through the finished corridor.

    The corridor's own saving is a SATURATED fixed offset (the transition
    equation), so at any astronomical L it is negligible against L/c and the
    traversal is L/c to every digit that matters.
    """
    return establishment_time(L_metres) + L_metres / C_SI


def single_transition_beats_light(L_metres=L_PROXIMA):
    """Theorem 4, COMPUTED rather than asserted: 1.5 L/c against L/c.

    The 1.5 is this scheme's value -- act from the midpoint, finish, then
    traverse.  The causal floor's ratio is 1, an attainable tie, so the False
    holds either way (DOCKET 67).  L defaults to the target, Proxima at its
    READ Gaia DR3 distance (CORRECTED, DOCKET 67 follow-up: first defaulted
    to 4.0 ly, a round baseline that named no target); the ratio does not
    depend on L.

    An earlier draft of this function returned False by construction, which is
    not a test of anything.  It now compares two numbers.
    """
    return single_transition_total(L_metres) < L_metres / C_SI


def single_transition_penalty(L_metres=L_PROXIMA):
    """How much WORSE this scheme (act from the midpoint, finish, traverse) is
    than just sending the signal: 1.5x.  The causal floor's ratio is 1
    (DOCKET 67); the 1.5 is not a bound."""
    return single_transition_total(L_metres) / (L_metres / C_SI)


def lambda_cost_of_improving(target):
    """R_s/b needed for a given Lambda.  Logarithmic means BRUTAL.

    Lambda = 2[ln(2 R_s/b) - 1], so R_s/b = exp(target/2 + 1)/2.  Going from
    the seated 9.98 to 100 costs a shell 7e21 times the corridor width.
    """
    return math.exp(target / 2.0 + 1.0) / 2.0


def amortised_establishment(L_metres, N):
    """L/(2Nc) -> 0.  All the value of a transition is here."""
    return establishment_time(L_metres) / N


# ------------------------------------------------------ the transition equation

def lam(b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """Lambda = 2[ln(2 R_s / sqrt(b^2 + a^2)) - 1].  A pure number, order ten."""
    return 2.0 * (math.log(2.0 * Rs / math.sqrt(b * b + a * a)) - 1.0)


def contraction_law(M_kg, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """Delta d = (G/c^2) M Lambda.  Linear in M, independent of the distance."""
    return G_SI * M_kg / C_SI ** 2 * lam(b, a, Rs)


def mass_for_contraction(dd_metres, **kw):
    return dd_metres / contraction_law(1.0, **kw)


def exchange_rate(**kw):
    """kg per metre contracted: c^2/(G Lambda)."""
    return 1.0 / contraction_law(1.0, **kw)


def contraction_saturates(m=2.0e-2, tol=1e-6):
    """It does not grow with the distance being contracted."""
    a = proper_contraction(m, X=400.0)
    b = proper_contraction(m, X=20000.0)
    return abs(b - a) <= tol * abs(a)


def contraction_is_linear(tol=2e-2):
    """Contraction per unit m is constant to 1 %, drifting only by Phi^2."""
    r = [proper_contraction(m) / m for m in (5.0e-3, 1.0e-2, 2.0e-2, 4.0e-2)]
    return (max(r) - min(r)) / max(r) < tol


# --------------------------------- the bare negative mass, computed (DOCKET 67)
#
# M RULED (DOCKET 67 follow-up): "phase1.py still excludes bare negative mass
# outright, which affects its ranking. - include it."  It was excluded with a
# None Lambda slot on the ground 'forbidden by the positive mass theorem'.
# The PMT forbids E_ADM < 0 only for data satisfying the DEC (EHLS
# arXiv:1110.2087 Thm 1, READ-VIA-RESTATEMENT; DOCKET 67 key
# positive-mass-theorem, check C2: a static constant-negative-density ball,
# complete, regular, asymptotically flat, E_ADM < 0, is not forbidden).  The
# ground was false, so the slot is now COMPUTED, here, at the seated geometry.

def phi_bare(x, b, m, a=A_CORE):
    """Phi of a BARE negative mass: the seated Plummer core with no shell.
    m > 0 is the magnitude of M < 0 (same convention as phi_device)."""
    r = math.hypot(x, b)
    return m / math.sqrt(r * r + a * a)


def lam_bare(X, b=B_RAY, a=A_CORE):
    """First-order contraction per unit m along the ray at impact parameter b,
    half-baseline X: int Phi dx / m = 2 asinh(X / sqrt(b^2 + a^2)).  It does
    NOT saturate: ~ 2 ln(2X/sqrt(b^2+a^2)), growing with the baseline."""
    return 2.0 * math.asinh(X / math.sqrt(b * b + a * a))


def bare_contraction(m, b=B_RAY, X=20000.0, n=100001):
    """int (1 - e^{-Phi}) dl for the bare mass -- the same quantity and the
    same quadrature as proper_contraction."""
    return _simpson(lambda x: 1.0 - math.exp(-phi_bare(x, b, m)), X, n)


def bare_crossover(lo=1.0, hi=1000.0):
    """Half-baseline X* above which the bare mass contracts more per unit |M|
    than the corridor: lam_bare(X*) = lam().  Bisection; ~ R_s/e."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if lam_bare(mid) < lam() else (lo, mid)
    return 0.5 * (lo + hi)


def far_field_mass(phi, r=1.0e6, m=1.0):
    """lim r Phi / m.  Weak field, Phi -> -M_ADM/r (G = c = 1, Phi > 0 for
    M < 0), so this is -M_ADM/m: 1 for the bare mass, ~0 for the corridor."""
    return r * phi(r, 0.0, m) / m


def bare_density_at(r, m=2.0e-2, h=1.0e-3):
    """4 pi rho = lap Phi_N, weak field, G = 1, with Phi_N = Phi (g_tt =
    -e^{2Phi} ~ -(1 + 2 Phi_N); a positive mass has Phi_N = -M/r < 0).
    Finite-difference Laplacian, radial: rho < 0 at every r (Plummer, closed
    form bare_density_closed)."""
    f = lambda q: phi_bare(q, 0.0, m)
    lap = (f(r + h) - 2.0 * f(r) + f(r - h)) / h ** 2 \
        + (2.0 / r) * (f(r + h) - f(r - h)) / (2.0 * h)
    return lap / (4.0 * math.pi)


def bare_density_closed(r, m=2.0e-2, a=A_CORE):
    """-3 m a^2 / (4 pi (r^2 + a^2)^{5/2}): negative at every r."""
    return -3.0 * m * a * a / (4.0 * math.pi * (r * r + a * a) ** 2.5)


#: The bare mass's slot is read at THIS file's quadrature window, X = 20000 b
#: (= 100 R_s, the window every contraction above is measured on).  It is a
#: function of the window, unlike the corridor's saturated lam(); the ranking
#: below does not depend on the choice, because lam_bare exceeds lam() at
#: every X > X* = 73.57 b, which includes every X >= R_s at which the
#: corridor's saturated law holds (selftest).
BARE_WINDOW_X = 20000.0
#: Radial stability of a static negative-mass ball is NOT computed here
#: (stability.py measures the shell device only): a NAMED hypothesis of its
#: 'reusable', which rests on 'static => no work' (budget.is_powered()).
BARE_STABILITY_COMPUTED = False

#: D2 per rankable entry, COMPUTED by far_field_mass (selftest).  The corridor
#: meets D2 approximately (M_ADM = 0 exactly; tail -m a^2/(2 r^3), see D2);
#: the bare mass FAILS it outright: M_ADM = -|M| != 0 and Phi ~ |M|/r outside
#: every compact K, so the universe outside K does know.
D2_STATUS = {
    "static concentric corridor": "APPROX (M_ADM = 0; Plummer tail ~ r^-3)",
    "bare negative mass": "FAILS (M_ADM = -|M|; Phi ~ |M|/r at every r)",
}


# --------------------------------- the ranking: fastest operator, lowest cost

# (name, Lambda-equivalent per unit mass, reusable?, why)
CANDIDATES = (
    ("static concentric corridor", lam(), True,
     "M_ADM = 0, holds itself, paid once.  The only rankable entry that keeps "
     "D2 (approximately).  CORRECTED (DOCKET 67 follow-up): first written "
     "'THE ONLY REUSABLE ENTRY'; the bare negative mass and the Casimir "
     "corridor are reusable too"),
    ("bare negative mass", lam_bare(BARE_WINDOW_X), True,
     "Lambda grows as ln(baseline) instead of saturating: 21.19 at this "
     "file's window X = 20000 b, above the corridor's 9.98 at every X > 73.6 b "
     "(~ R_s/e).  ITS COSTS, STATED: it violates the WEC and DEC at every r "
     "(rho < 0 throughout), as the corridor's core does at 0 < r < R_s, so the "
     "DEC does not separate them; it FAILS D2 (M_ADM = -|M| != 0, felt at "
     "every distance); and its radial stability is not computed.  CORRECTED "
     "(DOCKET 67 follow-up, M: 'include it'): first written 'forbidden by the "
     "positive mass theorem', then 'excluded here by the PMT, which forbids it "
     "only under the DEC', with Lambda slot None; the PMT does not forbid a "
     "DEC-violating E_ADM < 0, so the slot is now computed (lam_bare)"),
    ("GJW double-trace coupling", None, False,
     "PER USE as the 2016 pulsed protocol (each pulse opens one short "
     "window) -- this tree's inference, not GJW's 'except with a time delay' "
     "sentence; the static couplings of 1804.00491 and 1807.04726 are "
     "reusable (DOCKET 67).  Theorem 5 is not applied to the 2016 protocol"),
    ("Casimir corridor", None, True,
     "reusable; gjw.py's 4.39e71 short at metre scale is GJW's flat-space "
     "CYCLE (one free massless scalar, flat transversely infinite uniform "
     "density, cycle length 2D), not this corridor.  CORRECTED (DOCKET 67): "
     "the plate model (vacuumcorridor.py) gives 2.193e71 at 1 m, and every "
     "variant computed stays at 5e70 to 3.5e72"),
    ("charge state", 0.0, True,
     "no contraction at all: Phi > 0 only inside r < Q^2/2M, which is hidden "
     "at every Q up to extremal (charge.py samples q <= 1).  CORRECTED "
     "(DOCKET 67): first written 'at every Q'; for Q > M there is no horizon "
     "and bare superextremal RN has a vacuum Phi > 0 region, excluded only "
     "under a regular centre with rho >= 0"),
    ("Alcubierre shift", None, False,
     "EXCLUDED BY D4 -- T^{0i} != 0.  It is propulsion, a different object"),
)


def ranked():
    """Reusable entries with a computed Lambda > 0, cheapest first (largest
    Lambda = fewest kg per metre).

    CORRECTED (DOCKET 67 follow-up): first written 'Only entries that are
    reusable AND satisfy D1-D5 can be ranked at all', returned in list order.
    Read literally that admitted nothing -- the corridor meets D2 only
    approximately -- and the bare negative mass was not filtered by D2 but by
    a None slot resting on the PMT.  On M's ruling it is included, and D2 is
    reported per entry (D2_STATUS) rather than silently applied to one."""
    r = [c for c in CANDIDATES if c[1] is not None and c[1] > 0.0 and c[2]]
    return sorted(r, key=lambda c: -c[1])


def the_winner():
    """THE FASTEST OPERATOR AND THE LOWEST COST.  Fastest is a tie: both
    rankable entries are static and established causally, so both have
    Theorem 4's floor and the same 1.5 L/c (single_transition_penalty does
    not depend on the architecture).  Lowest cost decides: the entry with
    strictly the largest Lambda, or None on a tie.

    CORRECTED (DOCKET 67 follow-up): returned the single rankable entry,
    'static concentric corridor', which won 'by being the only entry that is
    both reusable and permitted'.  With the bare negative mass included
    (M's ruling) the winner on the two criteria asked is the BARE NEGATIVE
    MASS, at the cost of D2 (it is not compactly supported: M_ADM != 0)."""
    r = ranked()
    if not r:
        return None
    if len(r) > 1 and r[0][1] == r[1][1]:
        return None
    return r[0][0]


def the_winner_keeping_d2():
    """The same ranking restricted to entries that do not FAIL D2."""
    r = [c for c in ranked() if not D2_STATUS.get(c[0], "").startswith("FAILS")]
    return r[0][0] if r else None


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE DEFINITION -- D1 to D5")
    for tag, what, _why in CONDITIONS:
        print("      %-4s %s" % (tag, what))
    chk("a construction meeting all five is a transition",
        is_transition(False, True, True, True, True), True)
    chk("one with momentum flux is PROPULSION, not a transition",
        is_transition(True, True, True, True, True), False)
    chk("Alcubierre's shift is excluded by D4", alcubierre_is_propulsion(), True)
    # D4 AS RESTATED ON M'S RULING (DOCKET 64): each row can fail.
    chk("D4 (ii): a device with net momentum across its passage is PROPULSION",
        is_transition(False, True, True, True, True, net_momentum=True), False)
    chk("D4 restated: a transient passage flux with zero net momentum is NOT",
        is_transition(False, True, True, True, True, passage_flux=True), True)
    chk("  and the first wording is kept, and differs from the restatement",
        (D4_AS_FIRST_WRITTEN.startswith("no momentum"),
         D4_AS_FIRST_WRITTEN != [c for c in CONDITIONS if c[0] == "D4"][0][1]),
        (True, True))
    chk("and one with no declared arrival is not defined at all",
        is_transition(False, False, True, True, True), False)

    print("\nTHEOREM 1 -- the quantity is PROPER DISTANCE, not light time")
    near("exponent ratio, light time over proper distance", exponent_ratio(), 2.0, 5e-3)
    print("      so a transition acts on the FIRST, and chronology.py's LATE")
    print("      verdict is an answer about the second.")

    print("\nTHEOREM 2 -- no momentum.  Exactly zero, not to a tolerance.")
    chk("T^{0i} = 0 for the static device", no_momentum(), True)

    print("\nTHEOREM 3 -- holding it is free")
    chk("not powered, and radially stable", holding_is_free(), True)

    print("\nTHEOREM 4 -- a single transition can never beat light")
    # CORRECTED (DOCKET 67): these three pins read 6.3113e7, 6.3113e4 and
    # 1.4742e4, passing only under rtol 1e-3; the functions return 6.31150e7,
    # 6.31150e4 and 1.47442e4.  The pins now carry the computed values.
    # CORRECTED (DOCKET 67 follow-up): re-based from L = 4.0 ly (6.31150e7 s,
    # 2.0 yr, 6.31150e4 s) to the target, Proxima at its READ Gaia DR3
    # distance, and pinned to 1e-6 at the computed values:
    #   python3 -c "import phase1 as p; print(p.L_PROXIMA/p.LIGHT_YEAR,
    #     p.establishment_time(p.L_PROXIMA), p.establishment_time(p.L_PROXIMA)
    #     /p.JULIAN_YEAR_S)"  ->  4.2464599  6.700404e7  2.1232300
    near("the target: Proxima, Gaia DR3 1/parallax (ly)", L_PROXIMA / LIGHT_YEAR,
         4.2464599, 1e-7)
    chk("  and it is the tree's seated destination to 4 dp (foliation.py)",
        round(L_PROXIMA / LIGHT_YEAR, 4) == __import__("foliation").PROXIMA_LY, True)
    chk("  and not alpha Cen AB (all three READ orbital parallaxes farther)",
        all(AU_M * 648000.0 / math.pi / (p / 1000.0) > 1.02 * L_PROXIMA
            for p in ALPHA_CEN_AB_PARALLAX_MAS), True)
    near("light year = c x Julian year (m)", LIGHT_YEAR, 9460730472580800.0, 1e-15)
    near("establishment of the Proxima corridor (s)", establishment_time(L_PROXIMA),
         6.700404e7, 1e-6)
    near("  in Julian years", establishment_time(L_PROXIMA) / JULIAN_YEAR_S,
         2.1232300, 1e-6)
    near("  (first written at 4.0 ly: exactly 2 yr once LY is exact)",
         establishment_time(L_AS_FIRST_WRITTEN_LY * LIGHT_YEAR) / JULIAN_YEAR_S,
         2.0, 1e-12)
    chk("a single transition beats light -- COMPUTED, not asserted",
        single_transition_beats_light(), False)
    near("  this scheme (midpoint, finish, traverse) is worse by",
         single_transition_penalty(), 1.5, 1e-6)

    print("\nTHEOREM 5 -- so the value is amortised, and here it is available")
    near("establishment share at N = 1000", amortised_establishment(L_PROXIMA, 1000),
         6.700404e4, 1e-6)
    print("      GJW's 2016 pulsed coupling is per use (this tree's inference,")
    print("      not their sentence), so Theorem 5 is not applied to it.")

    print("\nTHE TRANSITION EQUATION -- Delta d = (G/c^2) M Lambda")
    near("Lambda from the closed form", lam(), 9.982529, 1e-6)
    near("  against the measured contraction per unit m at m = 5e-3",
         proper_contraction(5.0e-3) / 5.0e-3, lam(), 1e-3)
    chk("the contraction SATURATES -- no baseline in it", contraction_saturates(), True)
    chk("and it is LINEAR in mass", contraction_is_linear(), True)
    # ROUND-TRIP, not a transcribed constant: feed the required R_s/b back
    # through Lambda and it must return the target.  Two hand-typed fixtures
    # here were wrong on the first run, which is why this is a round-trip.
    for target in (20.0, 100.0):
        ratio = lambda_cost_of_improving(target)
        near("R_s/b for Lambda = %-5.0f -> round-trips to" % target,
             lam(b=1.0, a=0.0, Rs=ratio), target, 1e-9)
    print("      R_s/b = %.4e for Lambda = 20, and %.4e for Lambda = 100."
          % (lambda_cost_of_improving(20.0), lambda_cost_of_improving(100.0)))
    print("      so Lambda is improvable ONLY logarithmically: a tenfold gain")
    print("      costs a shell 7.05e21 times the corridor width.  At the seated")
    print("      geometry only that logarithm is left to optimise.")

    print("\nTHE PRICE")
    near("exchange rate (kg per metre contracted)", exchange_rate(), 1.34894e26, 1e-4)
    near("one solar mass buys (m)", contraction_law(SOLAR_MASS), 1.47442e4, 1e-3)
    # First-order law (the exact ansatz gives 0.944 and 0.403 of these: see
    # THE PRICE's DOCKET 67 note).  CORRECTED (DOCKET 67 follow-up): these
    # pins were the 4.0 ly prices 2.5667e10 and 1.2833e12; they are now the
    # Proxima prices, computed:
    #   python3 -c "import phase1 as p; print(p.mass_for_contraction(0.01*
    #     p.L_PROXIMA)/p.SOLAR_MASS, p.mass_for_contraction(0.5*p.L_PROXIMA)
    #     /p.SOLAR_MASS)"  ->  2.72477e10  1.36238e12
    near("Proxima contracted by 1 %, in solar masses",
         mass_for_contraction(0.01 * L_PROXIMA) / SOLAR_MASS, 2.72477e10, 1e-5)
    near("Proxima contracted by 50 %, in solar masses",
         mass_for_contraction(0.50 * L_PROXIMA) / SOLAR_MASS, 1.36238e12, 1e-5)
    near("  the first-written 4.0 ly price (kept), 1 %",
         mass_for_contraction(0.01 * L_AS_FIRST_WRITTEN_LY * LIGHT_YEAR) / SOLAR_MASS,
         2.56663e10, 1e-5)
    ab = [mass_for_contraction(0.01 * AU_M * 648000.0 / math.pi / (p / 1000.0))
          / SOLAR_MASS for p in ALPHA_CEN_AB_PARALLAX_MAS]
    near("  alpha Cen AB beside it, 1 %, nearest READ (A21 750.81 mas)",
         min(ab), 2.78739e10, 1e-5)
    near("  alpha Cen AB beside it, 1 %, farthest READ (PB16 743 mas)",
         max(ab), 2.81669e10, 1e-5)
    chk("  every price stays in the 1e10-Msun decade (the galaxy sentence)",
        all(1e10 <= x < 1e11 for x in ab + [mass_for_contraction(0.01 * L_PROXIMA)
                                            / SOLAR_MASS]), True)

    print("\nTHE RANKING -- fastest operator, lowest cost")
    for n, L, reuse, why in CANDIDATES:
        print("      %-28s %-9s %-9s %s"
              % (n, ("%.3f" % L) if L is not None else "-",
                 "reusable" if reuse else "PER USE", why[:34]))
    # THE BARE NEGATIVE MASS, INCLUDED ON M'S RULING (DOCKET 67 follow-up).
    # Its slot is computed (lam_bare) and checked against the same quadrature
    # the corridor's is checked against; the controls below can each fail.
    near("bare negative mass: Lambda at the window X = 20000 b (closed form)",
         lam_bare(BARE_WINDOW_X), 21.192870, 1e-6)
    near("  against the measured contraction per unit m at m = 5e-3",
         bare_contraction(5.0e-3) / 5.0e-3, lam_bare(BARE_WINDOW_X), 1e-3)
    near("  it does NOT saturate: X = 400 -> 20000 changes it by (ratio)",
         lam_bare(20000.0) / lam_bare(400.0), 1.585245, 1e-6)
    near("  crossover X* where it overtakes the corridor (units of b)",
         bare_crossover(), 73.572489, 1e-6)
    chk("  X* < R_s: cheaper at every baseline the saturated law covers",
        bare_crossover() < R_SHELL and lam_bare(R_SHELL) > lam(), True)
    near("  ITS COST, D2: lim r Phi/m = -M_ADM/m (1 = not compactly supported)",
         far_field_mass(phi_bare), 1.0, 1e-9)
    chk("  and the corridor's far field carries no mass (M_ADM = 0)",
        abs(far_field_mass(phi_device)) < 1e-9, True)
    chk("  ITS COST, DEC/WEC: rho < 0 at r = 0.01, 1, 10 (finite difference)",
        all(bare_density_at(r) < 0.0 for r in (0.01, 1.0, 10.0)), True)
    near("  and the finite difference matches the Plummer closed form at r = 1",
         bare_density_at(1.0), bare_density_closed(1.0), 1e-4)
    chk("  its radial stability is computed here", BARE_STABILITY_COMPUTED, False)
    # CORRECTED (DOCKET 67 follow-up): these pinned 1 rankable entry and the
    # winner 'static concentric corridor' ('It wins by being the only entry
    # that is both reusable and permitted').  With the bare mass included:
    chk("candidates that are reusable AND rankable", len(ranked()), 2)
    chk("  ranked cheapest first",
        [c[0] for c in ranked()], ["bare negative mass", "static concentric corridor"])
    chk("the winner (fastest ties by Theorem 4; lowest cost decides)",
        the_winner(), "bare negative mass")
    chk("the winner among entries that keep D2", the_winner_keeping_d2(),
        "static concentric corridor")
    near("  corridor price / bare price at the window (kg per metre)",
         lam() / lam_bare(BARE_WINDOW_X), 0.471032, 1e-5)
    near("  and with the shell spanning the baseline (X = R_s)",
         lam() / lam_bare(R_SHELL), 0.833089, 1e-5)
    print("      The bare negative mass is cheaper per unit |M| at every")
    print("      baseline the corridor's law covers, and it pays for that in")
    print("      D2: its M_ADM is -|M|, so it is not compactly supported and")
    print("      is a transition only if D2 is dropped.  The DEC does not")
    print("      separate the two: both violate it.  Among entries that keep")
    print("      D2 the corridor is still the only one.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT -- PHASE 1

  THE TRANSITION IS DEFINED: D1-D5, and every condition is checkable
  rather than rhetorical.  Static is SUFFICIENT for D4 (i): T^{0i} = 0
  is automatic for a static metric in its adapted coordinates.  It is
  not necessary, and a shift does not by itself fail D4 (flat constant
  shift, Kerr); Alcubierre's does (curl curl beta != 0).  (CORRECTED,
  DOCKET 67: first written 'The static/dynamic split IS the
  transition/propulsion split, exactly, because T^{0i} = 0 is
  automatic for a static metric and impossible with a shift vector'.)

  IT IS NOT FORBIDDEN BY THE CHRONOLOGY OR POSITIVE-MASS THEOREMS,
  because it violates the energy conditions they assume: the seated
  device violates NEC, WEC, SEC and DEC throughout its core, and with
  the DEC kept, PMT rigidity excludes M_ADM = 0 on a non-flat static
  slice.  (CORRECTED, DOCKET 67: first written 'Nothing in D1-D5 with
  M_ADM = 0 violates an energy condition, a chronology theorem or the
  positive mass theorem'.)

  IT IS NEVER A LEAD.  Establishing a compactly supported corridor is
  causal, so it cannot be complete before L/2c, and the first
  traversal cannot beat a signal sent when building began.  All of
  the value is in AMORTISATION -- and that route, closed for GJW's
  2016 pulsed protocol (this tree's inference from their 'except with
  a time delay', not their statement), is open here, because a
  static shape is not a signal.

  AND IT COSTS.  Delta d = (G/c^2) M Lambda, with Lambda = 9.9825, a
  pure geometric number improvable only logarithmically.  Linear in
  mass to first order, independent of the distance contracted once the
  endpoints are outside the shell, saturating to about 7.8 digits in
  this file's quadrature.  The exchange rate is 1.349e26 kg per metre:
  one solar mass buys 14.7 km, and one percent off the road to Proxima
  (4.2465 ly, Gaia DR3, READ) is 2.72e10 solar masses by the
  first-order law -- 2.79e10 to 2.82e10 at alpha Cen AB's READ
  orbital parallaxes -- and more again by the exact ansatz (0.944 of
  linear).  (CORRECTED, DOCKET 67: first written 'one percent off
  Alpha Centauri is 2.6e10' and 'saturating to nine digits'; then
  'one percent off 4.0 ly is 2.6e10 ... 2.7e10 to 2.8e10 at Alpha
  Centauri's READ distance', re-based on Proxima on M's 'repair all
  figures'.)

  THE RANKING.  Two entries are reusable with a computed Lambda: the
  corridor (9.98, saturated) and the BARE NEGATIVE MASS (21.19 at this
  file's window, growing as ln(baseline), larger than the corridor's at
  every half-baseline above 73.6 b, i.e. at every one the corridor's
  law covers).  Fastest is a tie (Theorem 4 binds both), so lowest cost
  decides and THE BARE NEGATIVE MASS RANKS FIRST.  Its costs: it
  violates the WEC and DEC everywhere (so does the corridor's core, so
  the DEC does not separate them), its radial stability is not
  computed, and it FAILS D2 -- M_ADM = -|M|, felt at every distance --
  so it is a transition only with D2 dropped.  Among entries that keep
  D2 the corridor is the only one.  (CORRECTED, DOCKET 67 follow-up,
  M: 'include it': the bare negative mass was excluded as 'forbidden
  by the positive mass theorem', which forbids it only under the DEC,
  and the corridor won as the only rankable entry.)

  PHASE 1 IS THE MATHEMATICS AND THE MATHEMATICS IS FINISHED.  At the
  seated geometry there is no free parameter left, and R_s/b moves it
  only logarithmically -- the contraction is
  proportional to mass with a coefficient fixed by c^2/G and a
  logarithm.  What remains is not a mathematics problem: every line
  above needs M < 0, and that is phase 2.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
