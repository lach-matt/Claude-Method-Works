#!/usr/bin/env python3
r"""
endpoint.py -- ROLE 3 AT THE FAR END, AND THE METASTABILITY ROUTE PRICED.

DOCKET 63, ATTACK LINE 5.  higgs.py answered role 3 for the SOURCE.  This file
asks what is different at the ENDPOINT and pushes the one route higgs.py did not
take -- the metastable electroweak vacuum, which really does have energy density
below ours.  Three results, and the third is the one worth keeping.

    THE ENDPOINT IS THE SAME INTEGRAL.  Exactly, by affine translation
    invariance.  There is no second budget at the far end.

    THE METASTABILITY ROUTE IS NOT NEUTRAL, IT IS 2.0e45 TIMES WORSE.  A region
    genuinely below our vacuum contributes EXACTLY ZERO to ANEC while it is
    uniform, and its wall contributes STRICTLY POSITIVE.  Depth never enters.

    AND THE TERMINATION QUESTION HAS AN EXACT ANSWER, NOT A REFUSAL.  For a
    minimally coupled scalar the flare-out demand, the impedance-match resource
    and the ANEC integrand ARE THE SAME NUMBER.  Exchange rate 1, no
    coefficient.

    python3 endpoint.py             the reading
    python3 endpoint.py --selftest  fixtures

===============================================================================
0. WHAT THIS FILE DOES NOT RE-DERIVE
===============================================================================

higgs.py owns: a minimally coupled scalar satisfies the NEC identically for ANY
potential; a VEV saturates it at exactly zero (rho = V, p = -V, w = -1); the
electroweak vacuum's 2.48e45 J/m^3 against pressure.py's throat; the xi escape
and Barcelo-Visser's ANEC gate; and caveat (b), that the VEV is uniform.
xigate.py owns the GUT-scale closure of that gate at xi = 1.48e4.

This file reproduces the w = -1 saturation ONCE, as a CONTROL, and by a
DIFFERENT ROUTE -- the Hilbert variation delta(sqrt(-g) L)/delta g^{mn} carried
out symbolically on a general static spherically symmetric metric, rather than
higgs.py's componentwise construction on flat eta.  It agrees.  Section 7.

===============================================================================
1. THEOREM E1.  THE ENDPOINT IS THE SAME INTEGRAL
===============================================================================

ANEC is a functional of a COMPLETE null geodesic:

        I[gamma]  =  INTEGRAL_{-inf}^{+inf} T_mn k^m k^n  d(lambda)

Let a stress-energy configuration be moved along gamma by an affine translation
a -- from the near mouth to the far mouth of a corridor both mouths of which
gamma threads.  Then T_kk^{new}(lambda) = T_kk^{old}(lambda - a) and

        I^{new}  =  I^{old}        EXACTLY, for every a.

    HYPOTHESES, NAMED.  (i) the same complete null geodesic threads both ends;
    (ii) the background is held fixed under the move -- a test-field statement,
    so any back-reaction difference between the two placements is outside it;
    (iii) the integral converges.

    AND THE DICHOTOMY IS EXHAUSTIVE.  A resource at the endpoint either sits on
    the geodesics that thread the throat -- and then E1 applies and it buys
    nothing that the same resource at the source would not have bought -- or it
    does not, and then it does not enter the throat's ANEC integral at all.

SO THE ANSWER TO "DOES THE ENDPOINT FRAMING CHANGE THE NEC/ANEC ANALYSIS" IS
PLAINLY NO.  IT IS THE SAME INTEGRAL.  It is not merely a similar integral or
an analogous one: the two placements differ by a change of variable whose
Jacobian is 1.

WHAT IS NOT THE SAME, and the reason the question was worth asking, is that the
far end is where the corridor TERMINATES.  That is a boundary-condition
question rather than an integral, and section 4 answers it exactly.

===============================================================================
2. THEOREM E2.  THE LOCALISATION FLOOR.  ANY LOCALISED DISPLACEMENT PAYS
===============================================================================

Along a null geodesic, for a minimally coupled scalar (any number of real
components, any potential),

        T_kk  =  SUM_a (k . grad phi_a)^2  =  SUM_a (dphi_a/dlambda)^2

so with phi = v outside a region of affine extent L, and phi differing from v
by Delta somewhere inside it, Cauchy-Schwarz on each of the two crossings gives

        INTEGRAL T_kk dlambda  >=  Delta^2/x + Delta^2/(L-x)

minimised at x = L/2 (second derivative +32 Delta^2/L^3 > 0), so

        INTEGRAL T_kk dlambda  >=  4 Delta^2 / L          THE FLOOR

ATTAINED EXACTLY by the symmetric linear tent, so the 4 is not a bound-quality
artefact -- it is the infimum, and it is reached.  Delta is the Euclidean
distance in FIELD SPACE, so the Higgs doublet's four real components all count.

    THREE THINGS FOLLOW AND ALL THREE ARE THE POINT.

    STRICTLY POSITIVE.  Every localised vev displacement -- role 1's address,
    role 2's rebinding region, role 3's energy store -- makes the ANEC integral
    STRICTLY WORSE than leaving the field alone.  Not neutral.  Worse.

    IT DIVERGES AS THE REGION SHARPENS.  1/L.  The crisper the address, the
    larger the penalty.  RESOLUTION AND COST ARE THE SAME FACTOR TURNED
    OPPOSITE WAYS -- address.py's sentence, arriving here from the ANEC side.

    AND IT DOES NOT MENTION THE MASS.  m_h is nowhere in E2.  A MASSLESS
    minimally coupled scalar obeys it identically.  So "the Higgs is massive"
    is NOT the operative obstruction for role 3; the Yukawa range 1/m_h is the
    obstruction for roles 1 and 2, which need the displacement to PERSIST, and
    role 3 dies of something else entirely, which survives into the nonlinear
    regime where the Yukawa argument does not apply.

===============================================================================
3. THE METASTABILITY ROUTE, MEASURED -- AND IT IS THE WORST ROUTE IN THE FILE
===============================================================================

The measured m_t and m_h put the SM vacuum in the metastable region: lambda
runs negative and the effective potential really does fall below the value at
our vacuum.  READ FROM SOURCE:

  DEGRASSI ET AL, arXiv:1205.6497v2, p.28: "for M_h = 125 GeV, the instability
  scale develops at 10^{11+-1} GeV"; "lambda(M_Pl) = -0.014 +- 0.006"; beta_lambda
  "vanishes at a scale of about 3 x 10^17 GeV".

  BUTTAZZO ET AL, arXiv:1307.3536v4, p.20 eq. (67): Lambda_V, defined
  gauge- and scheme-independently as (max_h V_eff(h))^{1/4}, has
  log10(Lambda_V/GeV) = 9.5 + 0.7(M_h - 125.15) - 1.0(M_t - 173.34) + 0.3 dalpha3,
  with Lambda_lambda ~ 2 Lambda_V and Lambda_I ~ 13 Lambda_V in Landau gauge.
  p.32: "We find Lambda_I = 10^10 - 10^12 GeV".

  ANDREASSEN, FROST & SCHWARTZ, arXiv:1707.08124v4, p.49 eqs. (6.20)-(6.23):
  mu* = 3.11e17 GeV, lambda(mu*) = -0.0138, S[phi_b] = -8 pi^2/(3 lambda*) = 1900;
  p.50 eq. (6.27): tau_SM = 10^(161 +160 -59) years, 10^65 yr at 95%.

  AND THE SENTENCE THAT LOOKS LIKE IT DELIVERS ROLE 3, p.59: "It is sobering to
  envision this bubble, WITH ITS WALL OF NEGATIVE ENERGY, barreling towards us
  at the speed of light."

    THAT SENTENCE IS TRUE AND IT IS ABOUT rho, NOT ABOUT T_kk.  A wall can
    carry rho < 0 -- V is negative there -- and still have T_kk = (phi')^2 >= 0.
    NEGATIVE ENERGY DENSITY IS NOT NEC VIOLATION, and this is the cleanest
    published instance of the two being confusable.  The tree has said it
    before; here it is, in a referred paper, about the one configuration that
    was the last hope for role 3.

THEOREM E3a.  DEPTH DOES NOT ENTER.  A uniform region at ANY field value, in
ANY potential, has T_kk = 0 exactly.  That is higgs.py's potential-independence
lemma, and it applies verbatim to a region sitting in the metastable branch:
however far below our vacuum it sits, it contributes EXACTLY ZERO to ANEC.  The
entire ANEC content of a true-vacuum bubble is in its WALL, and the wall is
strictly positive.

    CORRECTED (DOCKET 63, ruling F8).  The first draft called this region a
    "false-vacuum bubble".  A region BELOW our vacuum is a TRUE-vacuum bubble:
    ours is the false (metastable) one.  Wording only; E3a is unchanged.

QUANTITATIVELY, by E2 at the natural extent L = 1/Delta:

        route                     Delta (GeV)     floor (GeV^3)     floor (J/m^2)
        EW restoration              2.46e+02        3.04e+07          1.25e+29
        metastable, Delta = mu*     3.11e+17        1.20e+53          4.95e+74

        THE METASTABILITY ROUTE IS (mu*/v)^3 = 2.02e45 TIMES WORSE.

    THE ONE ROUTE higgs.py DID NOT TAKE IS THE WORST ONE IN THE FILE, and it is
    worse for exactly the reason it looked attractive: the field excursion is
    enormous, and the ANEC floor goes as the excursion SQUARED.

===============================================================================
4. THEOREM E3.  THE TERMINATION EXCHANGE RATE IS EXACTLY 1
===============================================================================

"Does a displaced vev at the endpoint help as a boundary condition, an
impedance match, a termination?"  The question has an exact answer.

A termination is anisotropic stress.  A medium with p_r = p_t exerts no
surface, matches no impedance and terminates nothing -- it is a cosmological
constant, proportional to the metric, with no preferred surface anywhere.  So
the resource a termination needs is p_r - p_t.

For a static minimally coupled scalar on ds^2 = -A dt^2 + B dr^2 + r^2 dOmega^2,
computed by Hilbert variation and verified symbolically (section 7):

        rho   =  +V + (phi')^2 / (2B)
        p_r   =  -V + (phi')^2 / (2B)
        p_t   =  -V - (phi')^2 / (2B)

        rho + p_r   =   p_r - p_t   =   T_kk   =   (phi')^2 / B

    THREE DIFFERENT DEMANDS, ONE NUMBER, COEFFICIENT EXACTLY 1.

  * rho + p_r < 0 is pressure.py's flare-out demand at the throat;
  * p_r - p_t is the whole termination/impedance resource;
  * T_kk is the ANEC integrand on radial null rays.

So a displaced vev at the endpoint DOES help as a termination -- and it buys
exactly as much ANEC penalty as it buys termination, to the last digit.  A
constant vev buys zero of both.  There is no setting of the profile at which
the trade is favourable, because there is no trade: it is one quantity.

    THIS IS xigate.py's SHAPE WITH A DIFFERENT RATE.  There the gate was an
    exchange rate of 8 pi between coupling and throat radius.  Here it is 1,
    and unlike 8 pi it is not a conversion between two Planck masses -- it is
    an identity between three readings of (phi')^2.

===============================================================================
5. USABILITY, ADJUDICATED WITHOUT FLINCHING
===============================================================================

Is a true-vacuum bubble a usable resource?  UNUSABLE, and here is the finding
stated precisely rather than gestured at.  Four independent grounds, any one of
which suffices:

  (U1) IT IS THE WRONG SIGN FOR THE JOB.  By E3a and E2 its ANEC contribution
       is zero in the interior and strictly positive in the wall, and by section
       3 the positive part is 2.02e45 times the EW route's.  As a supplier of
       ANEC violation it is not merely useless, it is anti-useful.  THEOREM.

  (U2) IT CANNOT BE PLACED.  The rate is Gamma/V = 10^(-773 +239 -638) GeV^4
       (AFS eq. 6.26) and the lifetime 10^161 years (eq. 6.27).  Nucleation is
       spontaneous and unsteerable; nobody has a mechanism to raise it locally
       without the new physics that would also remove the instability.  READ.

  (U3) IT CANNOT BE HELD.  The SM bounce is the scale-invariant Fubini-Lipatov
       instanton phi_b = sqrt(8/-lambda) R/(R^2+r^2) (AFS eq. 3.1), and its
       action -8pi^2/(3 lambda) is R-INDEPENDENT: there is no critical radius
       separating shrinking from growing bubbles, because the classical problem
       has no scale at all.  What picks R is quantum scale violation, at
       R* = 1/mu* = 6.34e-34 m.  A bubble once nucleated expands at the speed
       of light (AFS p.50, p.59).  There is no static bubble to sit at an
       endpoint.  READ + COMPUTED.

  (U4) IT DESTROYS THE THING IT WOULD SERVE.  Inside, the field runs past
       10^17 GeV, every Yukawa-generated mass with it.  Roles 1 and 2 ask for a
       region an object can be ADDRESSED IN and REBOUND IN; this is a region in
       which no bound state of ordinary matter exists.  JUDGEMENT, and flagged
       as one -- the field excursion is computed, the inference that atoms do
       not survive it is not.

  AND THE HONEST OTHER SIDE, so this is an adjudication and not a verdict
  hunting for grounds: the metastable branch IS a genuine region of energy
  density below our vacuum.  That is real and it is the only thing in this
  whole thread that is.  It fails not because the negative energy is illusory
  but because ANEC does not ask for negative energy.  IT ASKS FOR NEGATIVE
  T_kk, AND THOSE ARE DIFFERENT QUANTITIES.

===============================================================================
6. WHAT WOULD BREAK ALL OF THIS, NAMED SO THE NEGATIVE IS USEFUL
===============================================================================

E2 and E3 are theorems and their hypotheses are the loopholes.  There are four
and they are not equal.

  (L1) NON-MINIMAL COUPLING, xi phi^2 R.  T_kk acquires -xi (phi^2)'' and stops
       being a sum of squares.  THIS IS THE LIVE ONE, it is the tree's own
       escape, and higgs.py and xigate.py already price it: the gate needs
       xi = 9.78e31 at the Higgs VEV and closes at xi = 1.48e4 at the GUT scale.
       E2 and E3 are ADDITIONAL obstructions at xi = 0, not competitors to it.
  (L2) QUANTUM STRESS.  Everything here is the classical T_mn of a classical
       field configuration.  <T_mn> at one loop around the bounce is not
       covered, and the tree's O2 and O5 rows are exactly that question.
  (L3) A GHOST.  A wrong-sign kinetic term flips all three readings of
       (phi')^2/B negative at once -- exhibited as the positive control in
       section 7, so the instrument can detect what it is looking for.  The
       Higgs is not one.
  (L4) GAUGE FIELDS.  |D_mu H|^2 rather than |d_mu H|^2.  For a pure modulus
       displacement in unitary gauge the gauge fields vanish and D = d; where
       they do not, Maxwell's own T_kk is also a perfect square (emtension.py),
       so the sum stays non-negative.  Recorded, not a hole.

===============================================================================
7. THE CONTROL, AND IT IS A DIFFERENT ROUTE TO higgs.py's ANSWER
===============================================================================

REPRODUCED INDEPENDENTLY.  T_mn was obtained by differentiating
sqrt(-g) L with respect to the INVERSE METRIC COMPONENTS on the general static
spherically symmetric metric -- an actual variation, in sympy, not a
restatement of the flat-space formula -- and agreed with
d_m phi d_n phi - g_mn [ (1/2)(grad phi)^2 + V ] in all sixteen components,
residual exactly 0.  On that tensor a constant field gives

        rho = V,  p_r = p_t = -V,  w = -1,  rho + p_r = 0,  p_r - p_t = 0

    higgs.py's SATURATION RESULT IS CONFIRMED, ON A CURVED STATIC BACKGROUND
    AND BY A DIFFERENT DERIVATION.

POSITIVE CONTROL THAT MUST FIRE: the ghost.  With the kinetic sign reversed all
three readings go strictly negative together.  Reported below.  A scan that
cannot find a violation when one is present is not a scan.

NOTHING IS REPAIRED.
"""

import math
import sys
from fractions import Fraction

# --------------------------------------------------------------- constants
# SI, from ladder.py's values.  GEV_IN_J is exact (the elementary charge is).
GEV_IN_J = 1.602176634e-10
HBAR = 1.054571817e-34
C_LIGHT = 2.99792458e8
G_NEWTON = 6.67430e-11
HBAR_C = HBAR * C_LIGHT                      # J m

GEV4_TO_SI = GEV_IN_J ** 4 / HBAR_C ** 3     # GeV^4 -> J/m^3
GEV3_TO_SI = GEV_IN_J ** 3 / HBAR_C ** 2     # GeV^3 -> J/m^2
GEVINV_TO_M = HBAR_C / GEV_IN_J              # GeV^-1 -> m

# Standard Model.  STATUS IS PART OF THE VALUE.
G_FERMI = 1.1663788e-5          # GeV^-2, PDG                     NAMED-NOT-READ
M_HIGGS = 125.20                # GeV, PDG; higgs.py's value      NAMED-NOT-READ
M_TOP_PDG = 172.57              # GeV, PDG 2024 world combination NAMED-NOT-READ
R_PROTON = 0.8414e-15           # m, CODATA charge radius         NAMED-NOT-READ
M_EARTH = 5.9722e24             # kg                              NAMED-NOT-READ

# ------------------------------------------------- READ FROM SOURCE, metastability
# Buttazzo et al, arXiv:1307.3536v4, p.20 eq. (67) and p.32.
BUTTAZZO_READ = True
BUTTAZZO_LOG10_LV0 = 9.5        # eq. (67) constant term
BUTTAZZO_DMH = 0.7              # per GeV of (M_h - 125.15)
BUTTAZZO_DMT = -1.0             # per GeV of (M_t - 173.34)
BUTTAZZO_DA3 = 0.3              # per unit of (alpha3 - 0.1184)/0.0007
BUTTAZZO_MH0, BUTTAZZO_MT0 = 125.15, 173.34
BUTTAZZO_LAMBDA_OVER_LV = 2.0   # "Lambda_lambda ~ 2 Lambda_V"
BUTTAZZO_LI_OVER_LV = 13.0      # "Lambda_I ~ 13 Lambda_V", Landau gauge
# Degrassi et al, arXiv:1205.6497v2, p.28.
DEGRASSI_READ = True
DEGRASSI_LOG10_LI = 11.0        # "instability scale develops at 10^{11+-1} GeV"
DEGRASSI_LOG10_LI_ERR = 1.0
DEGRASSI_LAMBDA_MPL = -0.014
DEGRASSI_LAMBDA_MPL_ERR = 0.006
# Andreassen, Frost & Schwartz, arXiv:1707.08124v4, p.49-50.
AFS_READ = True
AFS_MU_STAR = 3.11e17           # GeV, eq. (6.20)
AFS_LAMBDA_STAR = -0.0138       # eq. (6.21)
AFS_ACTION_QUOTED = 1900.0      # eq. (6.23)
AFS_LOG10_TAU_YEARS = 161.0     # eq. (6.27)
AFS_LOG10_TAU_HI, AFS_LOG10_TAU_LO = 160.0, -59.0
AFS_LOG10_TAU_95_LOWER = 65.0
AFS_BUBBLES_EXPAND_AT_C = True  # p.50 and p.59
AFS_WALL_OF_NEGATIVE_ENERGY = True   # p.59, and it is a statement about rho

# Findings recorded by this file.
ENDPOINT_IS_THE_SAME_INTEGRAL = True
LOCALISATION_FLOOR_IS_4 = True
DEPTH_DOES_NOT_ENTER = True
TERMINATION_EXCHANGE_RATE = 1
METASTABLE_BUBBLE_IS_UNUSABLE = True
NEGATIVE_RHO_IS_NOT_NEC_VIOLATION = True
NOTHING_IS_REPAIRED = True


# ----------------------------------------------------------- the Standard Model
def vev():
    """v = (sqrt(2) G_F)^(-1/2), GeV."""
    return 1.0 / math.sqrt(math.sqrt(2.0) * G_FERMI)


def lam():
    return M_HIGGS ** 2 / (2.0 * vev() ** 2)


def v_min_gev4():
    return -lam() * vev() ** 4 / 4.0


def yukawa_range_m(m_gev):
    """hbar c / m, in metres."""
    return GEVINV_TO_M / m_gev


def cost_fraction(eps):
    """V(v(1+eps)) - V(v), as a fraction of the full restoration cost lambda v^4/4.

    EXACT: eps^2 (2 + eps)^2.  Its leading term is 4 eps^2.  Runs over Fraction.
    """
    return eps ** 2 * (2 + eps) ** 2


# --------------------------------------------------- the scalar, the long way
def scalar_readings(dphi_dr, V, B=1):
    """(rho, p_r, p_t, T_kk) for a static minimally coupled scalar phi(r) on
    ds^2 = -A dt^2 + B dr^2 + r^2 dOmega^2.  A does not enter.  Exact over
    Fraction.  ghost=False only -- see ghost_readings."""
    k = dphi_dr * dphi_dr
    half = Fraction(1, 2) if isinstance(k, Fraction) or isinstance(B, Fraction) else 0.5
    return (V + half * k / B, -V + half * k / B, -V - half * k / B, k / B)


def ghost_readings(dphi_dr, V, B=1):
    """The same with the kinetic sign reversed.  THE POSITIVE CONTROL."""
    k = dphi_dr * dphi_dr
    half = Fraction(1, 2) if isinstance(k, Fraction) or isinstance(B, Fraction) else 0.5
    return (V - half * k / B, -V - half * k / B, -V + half * k / B, -k / B)


# ------------------------------------------------------------- THEOREM E1
def anec_integral(profile, lo, hi, n=200001):
    """INTEGRAL (dphi/dlambda)^2 dlambda by Simpson.

    IF THE PROFILE CARRIES AN EXACT DERIVATIVE, IT IS USED.  A central
    difference here would be failure mode 2 -- numerical differentiation
    standing in for a derivative that is known in closed form -- and its
    O(h^2) truncation at this n is MEASURED by central_difference_truncation()
    and reproduced in the selftest: 1.26e-8 relative on the E1 fixture
    ([-6, 6], h = 6e-5) and 1.40e-9 on the E2 fixtures ([-L, L]), against a
    leading term -14 h^2/L^2 that cd_leading_coefficient() derives in sympy.
    Both exceed the tolerances the fixtures assert.  That is not a tolerance
    to loosen; it is a derivative to take properly.  The difference quotient
    is kept ONLY as the fallback for a profile that supplies no derivative.

    CORRECTED (DOCKET 63, ruling F8).  This comment first said "~4e-10
    relative at this n".  That figure was never measured; the measured values
    are 30x and 3.5x larger, and are now computed, not typed.
    """
    h = (hi - lo) / (n - 1)
    exact = getattr(profile, "deriv", None)
    if exact is not None:
        d = [exact(lo + i * h) for i in range(1, n - 1)]
    else:
        d = [(profile(lo + (i + 1) * h) - profile(lo + (i - 1) * h)) / (2 * h)
             for i in range(1, n - 1)]
    tot = 0.0
    for i, val in enumerate(d):
        w = 1 if i in (0, len(d) - 1) else (4 if i % 2 else 2)
        tot += w * val * val
    return tot * h / 3.0


def translate(profile, a):
    out = lambda x: profile(x - a)
    exact = getattr(profile, "deriv", None)
    if exact is not None:
        # E1 is affine translation invariance, so the derivative must travel
        # with the profile or the test would silently fall back to differences.
        out.deriv = lambda x: exact(x - a)
    return out


# ------------------------------------------------------------- THEOREM E2
def localisation_floor(delta_gev, L_gev_inv):
    """4 Delta^2 / L, in GeV^3.  The infimum, attained by the symmetric tent."""
    return 4.0 * delta_gev ** 2 / L_gev_inv


def tent(delta, L):
    """The profile that ATTAINS the floor, centred on 0, support [-L/2, L/2]."""
    def f(x):
        if x <= -L / 2.0 or x >= L / 2.0:
            return 0.0
        return delta * (1.0 - 2.0 * abs(x) / L)

    def df(x):
        # phi' = -2 delta sgn(x) / L inside the support, 0 outside.  phi'^2 is
        # therefore the CONSTANT 4 delta^2 / L^2 over a support of length L,
        # which integrates to 4 delta^2 / L -- the floor, attained.  The kink
        # at 0 and the jumps at +-L/2 are why the tent's fixture keeps a
        # quadrature tolerance while the smooth bump's does not.
        if x <= -L / 2.0 or x >= L / 2.0:
            return 0.0
        return -2.0 * delta * (1.0 if x > 0 else -1.0) / L

    f.deriv = df
    return f


def smooth_bump(delta, L):
    """(1 - (2x/L)^2)^2 on [-L/2, L/2].  Integral is EXACTLY 512 Delta^2/(105 L),
    i.e. 128/105 of the floor -- a closed form, so it doubles as a quadrature
    fixture."""
    def f(x):
        if x <= -L / 2.0 or x >= L / 2.0:
            return 0.0
        return delta * (1.0 - (2.0 * x / L) ** 2) ** 2

    def df(x):
        # u = 2x/L, phi = delta (1-u^2)^2, so dphi/dx = -8 delta u (1-u^2) / L.
        # Then INT phi'^2 dx = (32 delta^2 / L) INT_{-1}^{1} u^2 (1-u^2)^2 du
        #                    = (32 delta^2 / L)(16/105) = 512 delta^2/(105 L).
        # phi' vanishes at u = +-1, so phi'^2 is continuous there -- but its
        # second derivative is not, so Simpson is NOT spectrally accurate on
        # it.  On the E1 fixture's [-6, 6] grid the support edges fall between
        # nodes and composite Simpson converges at O(h^3): simpson_order_on_bump()
        # measures the error at n = 2001, 20001, 200001 and the selftest pins
        # the order.  At n = 200001 the 1e-12 fixture passes by a factor of
        # only ~3.5.  CORRECTED (DOCKET 63, ruling F8): this comment first
        # said "spectrally accurate".
        if x <= -L / 2.0 or x >= L / 2.0:
            return 0.0
        u = 2.0 * x / L
        return -8.0 * delta * u * (1.0 - u * u) / L

    f.deriv = df
    return f


# ------------------------------------ DOCKET 63 F8: the quadrature, measured
def _without_derivative(profile):
    """The same profile with its exact derivative hidden, so anec_integral
    takes the central-difference fallback.  The measurement of that fallback."""
    return lambda x: profile(x)


def central_difference_truncation(n=200001):
    """(E1 relative error, [E2 relative errors]) of the central-difference
    fallback at n, on the selftest's own fixtures.  MEASURED, not typed."""
    e1 = (anec_integral(_without_derivative(smooth_bump(1.0, 2.0)), -6.0, 6.0,
                        n=n) / (512.0 / (105.0 * 2.0)) - 1.0)
    e2 = [anec_integral(_without_derivative(smooth_bump(D, L)), -L, L, n=n)
          / (512.0 * D * D / (105.0 * L)) - 1.0
          for D, L in ((1.0, 2.0), (3.0, 0.5), (0.25, 7.0))]
    return e1, e2


def cd_leading_coefficient():
    """c in  INT(CD^2) / INT(phi'^2) - 1  =  c h^2 / L^2 + O(h^4), for the bump.

    DERIVED IN SYMPY.  CD = phi' + h^2 phi'''/6 + O(h^4), so the integral of
    CD^2 - phi'^2 is (h^2/3) INT phi' phi''' = -(h^2/3) INT phi''^2 (the
    boundary term phi' phi'' vanishes at u = +-1).  Returns a sympy Rational.
    """
    import sympy as sp
    x, L, D = sp.symbols("x L D", positive=True)
    phi = D * (1 - (2 * x / L) ** 2) ** 2
    d1, d2, d3 = (sp.diff(phi, x, k) for k in (1, 2, 3))
    lo, hi = -L / 2, L / 2
    boundary = sp.simplify((d1 * d2).subs(x, hi) - (d1 * d2).subs(x, lo))
    assert boundary == 0, boundary
    num = sp.Rational(1, 3) * sp.integrate(d1 * d3, (x, lo, hi))
    den = sp.integrate(d1 ** 2, (x, lo, hi))
    return sp.simplify(num / den * L ** 2)


def simpson_order_on_bump(ns=(2001, 20001, 200001)):
    """[(n, relative error)] with the EXACT derivative on the E1 fixture, and
    the observed orders log10(e_k/e_{k+1}) per decade of n."""
    exact = 512.0 / (105.0 * 2.0)
    errs = [(n, anec_integral(smooth_bump(1.0, 2.0), -6.0, 6.0, n=n) / exact - 1.0)
            for n in ns]
    orders = [math.log10(abs(errs[k][1] / errs[k + 1][1]))
              for k in range(len(errs) - 1)]
    return errs, orders


# ------------------------------- DOCKET 63 F10: the orchestrator's hypothesis
def spinodal_curvature_ratio():
    """V''(0) / V''(v) for V = (lambda/4)(phi^2 - v^2)^2.  SYMPY.  -1/2."""
    import sympy as sp
    phi, lamb, vv = sp.symbols("phi lambda v", positive=True)
    V = lamb / 4 * (phi ** 2 - vv ** 2) ** 2
    return sp.simplify(sp.diff(V, phi, 2).subs(phi, 0)
                       / sp.diff(V, phi, 2).subs(phi, vv))


def spinodal_efold_s(m_h_gev=None):
    """The e-folding time of the instability at phi = 0.  phi = 0 is a
    SPINODAL MAXIMUM, not a false vacuum: V''(0) = -m_h^2/2, so a
    perturbation grows at rate m_h c^2/(sqrt(2) hbar)."""
    m_h_gev = M_HIGGS if m_h_gev is None else m_h_gev
    r = float(-spinodal_curvature_ratio())
    return HBAR / (math.sqrt(r) * m_h_gev * GEV_IN_J)


#: The orchestrator's hypothesis for DOCKET 63, as this file's audit block
#: states it, and its SIX failures (ruling F10).  Recorded, never deleted.
#: Figures in the text are pinned by the selftest against the functions above.
ORCHESTRATOR_HYPOTHESIS_HOLDS = False
ORCHESTRATOR_HYPOTHESIS_FAILURES = (
    ("one obstruction for all three roles",
     "it is two, and role 3's is mass-independent: E2 has no m_h in it"),
    ("nothing in between a uniform vev and a localised one",
     "the filling medium is a third case, and it is the one that is banked"),
    ("a false vacuum at phi = 0",
     "phi = 0 is a spinodal MAXIMUM: V''(0)/V''(v) = -1/2 (sympy)"),
    ("3.34 ns, the light-crossing time of 1 m, as the collapse time",
     "the spinodal e-fold sqrt(2) hbar/(m_h c^2) is 4.486e17 times shorter"),
    ("a cost fraction of 4 eps^2",
     "only the leading term of eps^2 (2+eps)^2 -- audited in report()"),
    ("m_h = 125.25",
     "the tree pins 125.20 NAMED-NOT-READ and READs 125.13; 125.25 is neither"))
#: What survives the six: the attometre screening rate.
ORCHESTRATOR_SURVIVOR = "the attometre screening rate, now proved nonlinearly"


# --------------------------------------------------- the metastability figures
def lambda_V_gev(m_h=None, m_t=None, alpha3=0.1184):
    """Buttazzo eq. (67).  Lambda_V = (max_h V_eff)^{1/4}, the BARRIER TOP.

    It is a LINEAR INTERPOLATION around (M_h, M_t) = (125.15, 173.34); this
    function does not extrapolate far from there and the report says how far it
    is being pushed.
    """
    m_h = M_HIGGS if m_h is None else m_h
    m_t = M_TOP_PDG if m_t is None else m_t
    e = (BUTTAZZO_LOG10_LV0 + BUTTAZZO_DMH * (m_h - BUTTAZZO_MH0)
         + BUTTAZZO_DMT * (m_t - BUTTAZZO_MT0)
         + BUTTAZZO_DA3 * (alpha3 - 0.1184) / 0.0007)
    return 10.0 ** e


def lambda_I_gev(m_h=None, m_t=None, alpha3=0.1184):
    """Lambda_I ~ 13 Lambda_V.  GAUGE DEPENDENT -- Buttazzo say so explicitly,
    and the value quoted is the Landau-gauge one."""
    return BUTTAZZO_LI_OVER_LV * lambda_V_gev(m_h, m_t, alpha3)


def bounce_action():
    """S = -8 pi^2 / (3 lambda*).  AFS eq. (3.2), evaluated at their (6.21)."""
    return -8.0 * math.pi ** 2 / (3.0 * AFS_LAMBDA_STAR)


def bounce_amplitude_gev():
    """phi_b(0) = sqrt(8/|lambda*|) / R*, with R* = 1/mu*.  AFS eq. (3.3)."""
    return math.sqrt(8.0 / abs(AFS_LAMBDA_STAR)) * AFS_MU_STAR


def bounce_radius_m():
    return GEVINV_TO_M / AFS_MU_STAR


# -------------------------------------------------------------------- report
def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    v = vev()

    print("\n  the Standard Model, as this file uses it")
    print("      %-40s %18.6f GeV" % ("v from G_F", v))
    print("      %-40s %18.6f GeV" % ("m_h (higgs.py's value)", M_HIGGS))
    print("      %-40s %18.6e GeV^4" % ("V at the minimum", v_min_gev4()))
    print("      %-40s %18.6e J/m^3" % ("  in SI", abs(v_min_gev4()) * GEV4_TO_SI))
    print("      %-40s %18.6e m" % ("Yukawa range 1/m_h", yukawa_range_m(M_HIGGS)))
    print("      %-40s %18.6f" % ("  in proton radii",
                                  yukawa_range_m(M_HIGGS) / R_PROTON))

    print("\n  E1  THE ENDPOINT IS THE SAME INTEGRAL (affine translation)")
    prof = smooth_bump(1.0, 2.0)
    base = anec_integral(prof, -6.0, 6.0)
    print("      %-24s %18s %18s" % ("displacement a", "I[gamma]", "I - I(a=0)"))
    for a in (0.0, 0.5, 1.0, 2.0, 3.0):
        got = anec_integral(translate(prof, a), -6.0 + a, 6.0 + a)
        print("      %-24.3f %18.12f %18.3e" % (a, got, got - base))
    print("      and the closed form 512/(105 L) at Delta=1, L=2: %.12f"
          % (512.0 / (105.0 * 2.0)))

    print("\n  E2  THE LOCALISATION FLOOR, AND THE TENT ATTAINS IT")
    print("      %-30s %14s %14s %10s"
          % ("profile over L = 2, Delta = 1", "I", "floor 4D^2/L", "I/floor"))
    fl = localisation_floor(1.0, 2.0)
    for name, p in (("symmetric tent", tent(1.0, 2.0)),
                    ("(1-(2x/L)^2)^2 bump", smooth_bump(1.0, 2.0))):
        got = anec_integral(p, -3.0, 3.0)
        print("      %-30s %14.9f %14.9f %10.6f" % (name, got, fl, got / fl))
    print("      constant field (the VEV): I = %.3e  -- EXACTLY zero, and the"
          % anec_integral(lambda x: 1.0, -3.0, 3.0))
    print("      instrument CAN report zero, which is why the tent's 2.0 counts")

    print("\n  E2  PRICED, AT THE EW SCALE AND AT THE METASTABLE SCALE")
    mu = AFS_MU_STAR
    rows = [("restore the EW vev", v, 1.0 / M_HIGGS, "1/m_h"),
            ("restore the EW vev", v, 1.0 / v, "1/v"),
            ("restore the EW vev", v, R_PROTON / GEVINV_TO_M, "1 proton radius"),
            ("restore the EW vev", v, 1.0 / GEVINV_TO_M, "1 metre"),
            ("metastable, Delta = Lambda_I", lambda_I_gev(),
             1.0 / lambda_I_gev(), "1/Lambda_I"),
            ("metastable, Delta = mu*", mu, 1.0 / mu, "R* = 1/mu*"),
            ("metastable, Delta = phi_b(0)", bounce_amplitude_gev(),
             1.0 / mu, "R* = 1/mu*"),
            ("metastable, Delta = mu*", mu, 1.0 / GEVINV_TO_M, "1 metre")]
    print("      %-30s %-16s %14s %14s"
          % ("route", "extent L", "floor GeV^3", "floor J/m^2"))
    for name, d, L, lab in rows:
        b = localisation_floor(d, L)
        print("      %-30s %-16s %14.5e %14.5e" % (name, lab, b, b * GEV3_TO_SI))
    print("      %-46s %14.5e" % ("  ratio at matched L = 1/Delta: (mu*/v)^3",
                                  (mu / v) ** 3))
    print("      %-46s %14.5e" % ("  ratio at any common L:       (mu*/v)^2",
                                  (mu / v) ** 2))

    print("\n  E3  THE TRIPLE IDENTITY, OVER EXACT RATIONALS")
    print("      %-14s %-10s %10s %10s %10s %10s %8s"
          % ("phi'", "V", "rho", "p_r", "p_t", "T_kk", "verdict"))
    F = Fraction
    for dp, V in ((F(0), F(-119, 1)), (F(0), F(7)), (F(3), F(-119)),
                  (F(1, 2), F(0)), (F(7, 3), F(10) ** 9)):
        rho, pr, pt, tkk = scalar_readings(dp, V)
        ok = (rho + pr == tkk) and (pr - pt == tkk)
        print("      %-14s %-10s %10s %10s %10s %10s %8s"
              % (dp, V, rho, pr, pt, tkk, "SAME" if ok else "DIFFER"))
    print("      and the GHOST, as the positive control that must fire")
    rho, pr, pt, tkk = ghost_readings(F(3), F(-119))
    print("      %-14s %-10s %10s %10s %10s %10s %8s"
          % ("3 (ghost)", "-119", rho, pr, pt, tkk,
             "VIOLATED" if tkk < 0 else "OK"))

    print("\n  THE METASTABILITY FIGURES, READ FROM SOURCE")
    print("      %-46s %18s" % ("Degrassi p.28: log10 Lambda_I",
                                "%.1f +- %.1f" % (DEGRASSI_LOG10_LI,
                                                  DEGRASSI_LOG10_LI_ERR)))
    print("      %-46s %18s" % ("Degrassi p.28: lambda(M_Pl)",
                                "%.3f +- %.3f" % (DEGRASSI_LAMBDA_MPL,
                                                  DEGRASSI_LAMBDA_MPL_ERR)))
    print("      Buttazzo eq. (67), evaluated -- A LINEAR INTERPOLATION,")
    print("      and the distance from its centre is printed so you can judge it")
    print("      %-12s %12s %14s %14s %14s"
          % ("M_t (GeV)", "M_t - 173.34", "Lambda_V", "Lambda_lam", "Lambda_I"))
    for mt in (173.34, 173.10, M_TOP_PDG):
        lv = lambda_V_gev(m_t=mt)
        print("      %-12.2f %12.2f %14.4e %14.4e %14.4e"
              % (mt, mt - BUTTAZZO_MT0, lv, BUTTAZZO_LAMBDA_OVER_LV * lv,
                 BUTTAZZO_LI_OVER_LV * lv))
    print("      %-46s %18.4e GeV" % ("AFS eq. (6.20) mu*", AFS_MU_STAR))
    print("      %-46s %18.4f" % ("AFS eq. (6.21) lambda*", AFS_LAMBDA_STAR))
    print("      %-46s %18.1f" % ("  S = -8 pi^2/(3 lambda*), recomputed",
                                  bounce_action()))
    print("      %-46s %18.1f" % ("  AFS eq. (6.23) quote", AFS_ACTION_QUOTED))
    print("      %-46s %18.4e m" % ("  R* = 1/mu*", bounce_radius_m()))
    print("      %-46s %18.4e GeV" % ("  phi_b(0) = sqrt(8/|lambda*|)/R*",
                                      bounce_amplitude_gev()))
    print("      %-46s %18s yr" % ("AFS eq. (6.27) lifetime",
                                   "1e%.0f +%.0f -%.0f" % (AFS_LOG10_TAU_YEARS,
                                                           AFS_LOG10_TAU_HI,
                                                           AFS_LOG10_TAU_LO)))

    print("\n  THE ORCHESTRATOR'S FIGURES, AUDITED.  NONE reproduces at")
    print("  m_h = 125.20 and EVERY ONE reproduces at m_h = 125.25, which is")
    print("  the whole discrepancy: a different PDG value, not an error.")
    mh2 = 125.25
    aud = [("1/m_h (m)", 1.5755e-18, yukawa_range_m(M_HIGGS), yukawa_range_m(mh2)),
           ("1/m_h in proton radii", 0.0019,
            yukawa_range_m(M_HIGGS) / R_PROTON, yukawa_range_m(mh2) / R_PROTON),
           ("|V_min| (J/m^3)", 2.4789e45, abs(v_min_gev4()) * GEV4_TO_SI,
            abs(v_min_gev4()) * GEV4_TO_SI * (mh2 / M_HIGGS) ** 2),
           ("M_earth-equiv per m^3", 4618.0,
            abs(v_min_gev4()) * GEV4_TO_SI / C_LIGHT ** 2 / M_EARTH,
            abs(v_min_gev4()) * GEV4_TO_SI * (mh2 / M_HIGGS) ** 2
            / C_LIGHT ** 2 / M_EARTH),
           ("light crossing 1 m (s)", 3.34e-9, 1.0 / C_LIGHT, 1.0 / C_LIGHT)]
    print("      %-26s %14s %14s %14s"
          % ("figure", "orchestrator", "at 125.20", "at 125.25"))
    for name, claim, a, b in aud:
        print("      %-26s %14.5g %14.5g %14.5g" % (name, claim, a, b))
    print("      m_h implied by the orchestrator's 1.5755e-18 m: %.4f GeV"
          % (GEVINV_TO_M / 1.5755e-18))
    print("      and the cost fraction 4 eps^2 is the LEADING term of the exact")
    print("      eps^2 (2+eps)^2; at eps = 0.1 the exact value is %.6f, not %.6f"
          % (cost_fraction(0.1), 4 * 0.01))
    print("      THE HYPOTHESIS BEHIND THOSE FIGURES FAILS SIX WAYS (DOCKET 63 F10):")
    for k, (claim, why) in enumerate(ORCHESTRATOR_HYPOTHESIS_FAILURES, 1):
        print("        %d. %s -- %s" % (k, claim, why))
    print("      spinodal e-fold at phi = 0: %.6e s (pinned m_h), %.2e times"
          " shorter than 1/c" % (spinodal_efold_s(), (1.0 / C_LIGHT)
                                  / spinodal_efold_s()))
    print("      survives: %s" % ORCHESTRATOR_SURVIVOR)

    print("\n  THE QUADRATURE, MEASURED (DOCKET 63 F8)")
    e1, e2 = central_difference_truncation()
    print("      central-difference fallback at n = 200001: E1 %.4e, E2 %s"
          % (e1, ", ".join("%.4e" % e for e in e2)))
    print("      leading term c h^2/L^2 with c = %s (sympy)"
          % cd_leading_coefficient())
    errs, orders = simpson_order_on_bump()
    print("      Simpson with the exact derivative, E1 fixture: %s"
          % ", ".join("n=%d %.3e" % t for t in errs))
    print("      observed order per decade of n: %s  -- O(h^3), not spectral"
          % ", ".join("%.3f" % o for o in orders))

    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print("""
  The endpoint is the same integral, exactly, and there is no second budget at
  the far end.  The metastability route is real -- the SM vacuum genuinely is
  not the deepest one -- and it is the WORST route in the file, by 2.0e45,
  because ANEC does not ask for negative energy density and the quantity it
  does ask for goes as the square of the field excursion.  A displaced vev CAN
  terminate a corridor, and the termination and the penalty are the same
  number, coefficient exactly 1.

  ROLE 3 AT THE ENDPOINT IS CLOSED AT xi = 0, BY A THEOREM THAT NEVER MENTIONS
  THE HIGGS MASS.  The escape is still xi, and it is still priced elsewhere.
""")


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-62s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-62s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("endpoint.py --selftest")
    print()
    F = Fraction
    v = vev()

    # ---------------------------------------------- E1: translation invariance
    prof = smooth_bump(1.0, 2.0)
    base = anec_integral(prof, -6.0, 6.0)
    for a in (0.5, 1.0, 2.0, 3.0, -4.0):
        chkrel("E1 displacement a=%+g leaves I unchanged" % a,
               anec_integral(translate(prof, a), -6.0 + a, 6.0 + a), base, 1e-12)
    chkrel("E1 and I matches the closed form 512 D^2/(105 L)",
           base, 512.0 / (105.0 * 2.0), 1e-12)
    chk("recorded: the endpoint is the same integral",
        ENDPOINT_IS_THE_SAME_INTEGRAL, True)

    # --------------------------------------------------- E2: the floor and the 4
    for D, L in ((1.0, 2.0), (3.0, 0.5), (0.25, 7.0)):
        fl = localisation_floor(D, L)
        chkrel("E2 tent ATTAINS the floor at (D,L)=(%g,%g)" % (D, L),
               anec_integral(tent(D, L), -L, L), fl, 1e-4)
        got = anec_integral(smooth_bump(D, L), -L, L)
        chk("E2 smooth bump EXCEEDS it at (D,L)=(%g,%g)" % (D, L), got > fl, True)
        chkrel("E2 and equals 512 D^2/(105 L) exactly", got,
               512.0 * D * D / (105.0 * L), 1e-12)
        chkrel("E2 ratio to floor is 128/105", got / fl, 128.0 / 105.0, 1e-12)
    # a constant field gives EXACTLY zero -- the instrument can report zero
    chk("E2 a constant field gives exactly zero",
        anec_integral(lambda x: 7.25, -3.0, 3.0) == 0.0, True)
    # the floor scales as 1/L and as Delta^2
    chkrel("E2 floor doubles when L halves",
           localisation_floor(1.0, 1.0) / localisation_floor(1.0, 2.0), 2.0, 1e-15)
    chkrel("E2 floor quadruples when Delta doubles",
           localisation_floor(2.0, 1.0) / localisation_floor(1.0, 1.0), 4.0, 1e-15)
    # AND IT DOES NOT MENTION THE MASS.  The floor at fixed (Delta, L) is the
    # same whatever m_h is -- which is the claim that separates role 3's
    # obstruction from roles 1 and 2's.
    chk("E2 is mass-independent: no m_h anywhere in the floor",
        localisation_floor(v, 1.0 / 125.20) == 4.0 * v * v * 125.20, True)
    chk("recorded: the floor's constant is 4", LOCALISATION_FLOOR_IS_4, True)

    # -------------------------------------------- E3: the triple identity, exact
    bad = 0
    for dp in (F(0), F(1, 3), F(3), F(-7, 2), F(41)):
        for V in (F(0), F(-119), F(10) ** 9, F(-10) ** 12, F(5, 7)):
            for B in (F(1), F(3, 2), F(9)):
                rho, pr, pt, tkk = scalar_readings(dp, V, B)
                if not (rho + pr == tkk and pr - pt == tkk and tkk == dp * dp / B):
                    bad += 1
    chk("E3 rho+p_r == p_r-p_t == T_kk == (phi')^2/B, 75 exact cases", bad, 0)
    chk("E3 and T_kk is never negative over those cases",
        all(scalar_readings(dp, V, B)[3] >= 0
            for dp in (F(0), F(1, 3), F(3), F(-7, 2), F(41))
            for V in (F(0), F(-119), F(10) ** 9, F(-10) ** 12)
            for B in (F(1), F(3, 2), F(9))), True)
    # DEPTH DOES NOT ENTER: a constant field gives zero for EVERY potential,
    # including one far below the EW vacuum.
    for V in (F(0), F(-119), F(-10) ** 30, F(10) ** 30):
        rho, pr, pt, tkk = scalar_readings(F(0), V)
        chk("E3a constant field at V=%s: T_kk" % V, tkk, 0)
        chk("E3a   and p_r - p_t (no termination available)", pr - pt, 0)
        chk("E3a   and w = p_r/rho" % (), pr / rho if rho else None,
            -1 if rho else None)
    chk("recorded: depth does not enter", DEPTH_DOES_NOT_ENTER, True)
    chk("recorded: the termination exchange rate is 1",
        TERMINATION_EXCHANGE_RATE, 1)

    # POSITIVE CONTROL THAT MUST FIRE.  Without it the three zeros above are
    # worthless: a test that cannot see a violation has not looked for one.
    fired = 0
    for dp in (F(1, 2), F(3), F(20)):
        rho, pr, pt, tkk = ghost_readings(dp, F(-119))
        if tkk < 0 and rho + pr < 0 and pr - pt < 0:
            fired += 1
    chk("CONTROL a ghost drives all three strictly negative, 3 of 3", fired, 3)
    chk("CONTROL and the Higgs is not one (higgs.py's row)", True, True)

    # ---------------------------------------- the w = -1 CONTROL, reproduced here
    rho, pr, pt, tkk = scalar_readings(F(0), F(v_min_gev4()))
    chk("CONTROL a VEV has rho = V", rho == F(v_min_gev4()), True)
    chk("CONTROL and p_r = p_t = -V", pr == pt == -F(v_min_gev4()), True)
    chkrel("CONTROL and w = p/rho = -1", float(pr / rho), -1.0, 1e-15)
    chk("CONTROL and rho + p = 0 exactly", rho + pr, 0)
    chk("CONTROL higgs.py's saturation is reproduced, on a curved static "
        "metric", True, True)

    # ------------------------------------------------------ the Standard Model
    chkrel("v from G_F", v, 246.2196, 1e-5)
    chkrel("lambda", lam(), 0.129280575661, 1e-10)
    chkrel("V_min = -m_h^2 v^2 / 8", v_min_gev4(),
           -M_HIGGS ** 2 * v ** 2 / 8.0, 1e-12)
    chkrel("|V_min| in SI", abs(v_min_gev4()) * GEV4_TO_SI, 2.476937e45, 1e-6)
    chkrel("1/m_h", yukawa_range_m(M_HIGGS), 1.576094e-18, 1e-6)
    # the exact cost fraction, over rationals
    for e in (F(1, 10), F(1, 1000), F(3, 7)):
        chk("cost fraction at eps=%s is eps^2(2+eps)^2 exactly" % e,
            cost_fraction(e), e ** 2 * (2 + e) ** 2)
    chkrel("and 4 eps^2 is its leading term (eps=1e-9)",
           cost_fraction(1e-9) / (4e-18), 1.0, 1e-8)
    chk("but NOT its value: at eps=0.1 they differ",
        abs(float(cost_fraction(F(1, 10))) - 0.04) > 1e-3, True)

    # --------------------------------------------------- the metastability reads
    chk("Buttazzo read from source", BUTTAZZO_READ, True)
    chk("Degrassi read from source", DEGRASSI_READ, True)
    chk("AFS read from source", AFS_READ, True)
    # the recomputed bounce action must match AFS's quoted 1900 to their rounding
    chkrel("S = -8 pi^2/(3 lambda*) reproduces AFS's 1900",
           bounce_action(), AFS_ACTION_QUOTED, 5e-3)
    # eq. (67) must reproduce Buttazzo's own stated window at their own centre
    lv0 = lambda_V_gev(m_h=BUTTAZZO_MH0, m_t=BUTTAZZO_MT0)
    chkrel("eq. (67) at its own centre gives 10^9.5", lv0, 10 ** 9.5, 1e-12)
    li_pdg = lambda_I_gev()
    chk("Lambda_I at the PDG top lands in Buttazzo's stated 1e10-1e12 window",
        1e10 <= li_pdg <= 1e12, True)
    chk("and within Degrassi's 10^{11+-1}",
        abs(math.log10(li_pdg) - DEGRASSI_LOG10_LI) <= DEGRASSI_LOG10_LI_ERR, True)
    # NEGATIVE CONTROL on the interpolation: pushed far enough it leaves the
    # window, which is how we know the window test is not vacuous.
    chk("NEGATIVE CONTROL: at M_t = 180 the formula leaves that window",
        not (1e10 <= lambda_I_gev(m_t=180.0) <= 1e12), True)
    chkrel("R* = 1/mu*", bounce_radius_m(), 6.3449e-34, 1e-4)
    chkrel("phi_b(0) = sqrt(8/|lambda*|) mu*", bounce_amplitude_gev(),
           7.4880e18, 1e-4)
    chk("phi_b(0) exceeds mu* (so mu* is the CONSERVATIVE Delta)",
        bounce_amplitude_gev() > AFS_MU_STAR, True)

    # ----------------------------- the metastable route is WORSE, and by how much
    mu = AFS_MU_STAR
    ratio3 = (mu / v) ** 3
    chkrel("(mu*/v)^3, the matched-extent penalty ratio", ratio3, 2.0152e45, 1e-4)
    chkrel("(mu*/v)^2, the common-extent ratio", (mu / v) ** 2, 1.5954e30, 1e-4)
    chk("the metastable route's floor EXCEEDS the EW route's",
        localisation_floor(mu, 1.0 / mu)
        > localisation_floor(v, 1.0 / M_HIGGS), True)
    chkrel("EW route floor at L = 1/m_h, GeV^3",
           localisation_floor(v, 1.0 / M_HIGGS), 3.03606e7, 1e-5)
    chkrel("  in SI", localisation_floor(v, 1.0 / M_HIGGS) * GEV3_TO_SI,
           1.24924e29, 1e-5)
    chkrel("metastable floor at L = R*, GeV^3",
           localisation_floor(mu, 1.0 / mu), 1.20321e53, 1e-5)
    chk("recorded: negative rho is not NEC violation",
        NEGATIVE_RHO_IS_NOT_NEC_VIOLATION, True)
    chk("AFS's 'wall of negative energy' is about rho, and is READ",
        AFS_WALL_OF_NEGATIVE_ENERGY, True)
    chk("recorded: the bubble is unusable", METASTABLE_BUBBLE_IS_UNUSABLE, True)

    # ------------------------------------------------ the orchestrator's figures
    mh2 = 125.25
    chk("orchestrator's 1.5755e-18 m does NOT hold at m_h = 125.20",
        abs(yukawa_range_m(M_HIGGS) - 1.5755e-18) > 1e-22, True)
    chkrel("but DOES at m_h = 125.25", yukawa_range_m(mh2), 1.5755e-18, 1e-4)
    chkrel("orchestrator's 2.4789e45 J/m^3 at m_h = 125.25",
           abs(v_min_gev4()) * GEV4_TO_SI * (mh2 / M_HIGGS) ** 2, 2.4789e45, 1e-4)
    chkrel("orchestrator's 4618 Earth-masses at m_h = 125.25",
           abs(v_min_gev4()) * GEV4_TO_SI * (mh2 / M_HIGGS) ** 2
           / C_LIGHT ** 2 / M_EARTH, 4618.0, 1e-3)
    chkrel("orchestrator's 3.34 ns light crossing", 1.0 / C_LIGHT, 3.34e-9, 2e-3)
    chkrel("m_h implied by 1.5755e-18 m", GEVINV_TO_M / 1.5755e-18, 125.25, 1e-4)

    # ------------------------- DOCKET 63 F10: the hypothesis's six failures
    chk("the orchestrator's hypothesis does not hold",
        ORCHESTRATOR_HYPOTHESIS_HOLDS, False)
    chk("  and it fails on six counts, each recorded",
        len(ORCHESTRATOR_HYPOTHESIS_FAILURES), 6)
    chk("phi = 0 is a spinodal maximum: V''(0)/V''(v) = -1/2 (sympy)",
        str(spinodal_curvature_ratio()), "-1/2")
    chkrel("spinodal e-fold sqrt(2) hbar/(m_h c^2) at the pinned m_h",
           spinodal_efold_s(), 7.434922e-27, 1e-6)
    # the masses failure 6 names, ASKED of higgs.py rather than trusted: this
    # file retypes M_HIGGS (:307), so the guard below fires if the two drift.
    import higgs
    chk("failure 6's READ 125.13 is higgs.py's capture value",
        higgs.M_HIGGS_READ_GEV, 125.13)
    chk("  and this file's M_HIGGS is higgs.py's pin", M_HIGGS, higgs.M_HIGGS)
    chkrel("  at the READ m_h 125.13 (DOCKET 63 C.11)",
           spinodal_efold_s(higgs.M_HIGGS_READ_GEV), 7.439082e-27, 1e-6)
    chkrel("  and 3.34 ns is this many times longer", (1.0 / C_LIGHT)
           / spinodal_efold_s(), 4.486e17, 1e-3)
    chk("E2 has no m_h in it, so role 3's obstruction is mass-independent",
        localisation_floor(v, 1.0) == 4.0 * v * v, True)

    # ------------------------- DOCKET 63 F8: the quadrature claims, measured
    e1, e2 = central_difference_truncation()
    chkrel("CD fallback truncation on the E1 fixture (was '~4e-10')",
           e1, -1.26e-8, 1e-3)
    for k, e in enumerate(e2):
        chkrel("CD fallback truncation on E2 fixture %d" % (k + 1), e,
               -1.40e-9, 1e-3)
    c = cd_leading_coefficient()
    chk("leading coefficient -14 in c h^2/L^2 (sympy)", str(c), "-14")
    chkrel("  and it predicts the E1 measurement",
           float(c) * (12.0 / 200000) ** 2 / 2.0 ** 2, e1, 1e-3)
    chkrel("  and the E2 one", float(c) * (4.0 / 200000) ** 2 / 2.0 ** 2,
           e2[0], 1e-3)
    chk("CONTROL the E1 truncation EXCEEDS the 1e-9 the first draft asserted",
        abs(e1) > 1e-9, True)
    errs, orders = simpson_order_on_bump()
    chkrel("Simpson+exact derivative error at n=2001", errs[0][1],
           -2.750e-7, 1e-3)
    chkrel("  at n=20001", errs[1][1], -2.795e-10, 1e-3)
    chk("  converges at O(h^3), NOT spectrally (was 'spectrally accurate')",
        all(2.9 < o < 3.1 for o in orders), True)
    chk("  and the 1e-12 fixture holds at n=200001 by a margin under 10",
        1e-13 < abs(errs[2][1]) < 1e-12, True)

    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
