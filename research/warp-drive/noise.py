#!/usr/bin/env python3
r"""
noise.py -- D22.  THE SMEARED FLUCTUATION DEMAND, PRICED AT THE CORRIDOR'S SCALES.

    python3 noise.py             the reading
    python3 noise.py --selftest  every figure re-derived; controls that can fail

Needs sympy, mpmath, z3 (imported inside functions; importing this module is
stdlib-only).  Imports achievable.py (C, the demand, the hold time),
fewsterteo.py (the clamped sampler in double precision, its quadrature panels,
CORRIDOR_MODE_FUNCTIONS) and fluctuation.py (the pointwise thermal Delta', T1)
-- none is copied.

SEATED BY DOCKET 64, with the ruling's section B1 fixes and the verifier's
(verify-fluct) SHOULD-FIX and NOTE items applied.  What changed, and why, is
recorded in WITHDRAWN and CORRECTED below; nothing withdrawn is deleted.

===============================================================================
0.  THE QUESTION, AND THE ANSWER -- STATUS SPLIT
===============================================================================

fluctuation.py proved the POINTWISE Kuo-Ford measure is >= 1/3 for every
zero-mean Gaussian state and is sign-blind.  D22 asked for the SMEARED price at
the corridor's own scales and whether the demand column must be restated about a
distribution.

    THEOREM C1, IN THE FLAT MODEL H1-H6 (section 3).  For the free scalar
    (minimal coupling, m >= 0) in Minkowski spacetime, the Fewster-sampled
    energy density A_tau (Friedrichs extension) is bounded below as an
    OPERATOR by -C/tau^4.  Under H6 ("distribution" = the quantum spectral
    measure of A_tau) every individual measurement outcome, in every state,
    lies in its spectrum.  So a density more negative than -C/tau^4 is not the
    mean of any state and is not the outcome of any single measurement in any
    state: under H6 its probability is exactly zero (a THEOREM consequence,
    not a measured figure).

    APPLICATION TO THE CORRIDOR: SURVEY.  H2 fails there -- the demand's own
    curvature length l_G is shorter than the sampling length b by
    b/l_G = sqrt(B_OVER_LG_SQUARED) = 61.237 at every b.  The flat figures at
    the corridor's scales (71.256 orders at the hold time, 64.108 at l_G,
    60.108 at 0.1 l_G, b = 1 m) are flat bounds applied inside a curved region.
    The curved decision is O2's (CURVED_PART_CARRIED_BY): by FFR 1004.0179
    note [18], an absolute QEI evaluated on the corridor decides the
    distribution question there with no variance at all.

    UNDER THE GAUSSIAN EINSTEIN-LANGEVIN SURROGATE (Hu & Verdaguer 0802.0658
    Eq. (3.13); a different reading of "distribution", NOT H6) the probability
    is not zero.  With the vacuum's noise kernel it is
    exp(-10^EL_VACUUM_LOG10_NEG_LN_P) = exp(-10^141.916) at b = 1 m, computed
    below -- so BELOW exp(-10^141) and NOT below exp(-10^142) (CORRECTED:
    DOCKET 64's ruling typed exp(-10^142)).  For a state whose noise kernel is
    larger than the vacuum's the surrogate's probability is set by that
    kernel, which is NOT computed here.

    The requirement is unchanged in the flat model and on the vacuum-noise
    surrogate: restating the demand column about a distribution refuses
    exactly what the expectation-value column refuses.

===============================================================================
1.  (a)  THE VACUUM VARIANCE OF THE SMEARED ENERGY DENSITY -- EXACT IN tau
===============================================================================

For any real sampler f(t) on an inertial worldline, Minkowski vacuum, massless
minimally coupled scalar, rho = (1/2) SUM_A (d_A phi)^2:

    Var_0[rho(f)] = (1 / (3360 pi^4)) INT_0^oo w^7 |fhat(w)|^2 dw        (V)

DERIVED TWO INDEPENDENT WAYS, BOTH EXACT IN SYMPY:
  (P) point-split: <:rho(t)::rho(t'):>_0 = 3/(2 pi^4 (t-t'-i0)^8), from
      d_A d'_B of 1/(4 pi^2 sigma), and 1/(u-i0)^8 = (1/7!) INT w^7 e^{-iwu};
  (F) mode sum: the two-particle amplitude of rho(f)|0>, the angular average of
      (1 + cos theta)^2 (= 8/3) and the Beta integral INT_0^s w^3(s-w)^3 = s^7/140.
CONTROLS AGAINST SOURCE, EACH ABLE TO FAIL: the same machinery must reproduce
Fewster, Ford & Roman 1204.3570 Table I second moments -- a_2 = 2 (phi^2),
9/2 (phidot^2), 3/2 (rho_S) for the Lorentzian -- and FFR 1004.0179 Eq. (18),
G_2 = c/(24 pi^2 tau^4) at c = 1 for the Gaussian in 2D.  All four do.

By scaling, Var_0 = K_f / tau^8 EXACTLY, K_f a pure number of the sampler's
SHAPE.  Lorentzian K = 3/(512 pi^4), Gaussian K = 1/(70 pi^4) (exact, sympy).
For FEWSTER'S OWN SAMPLER -- f = g^2, g the L^2-normalised fundamental of
d^4/dt^4 with clamped ends on [0, tau], the sampler whose Rayleigh quotient is
mu_1^4 and so gives C = mu_1^4/(16 pi^2) (Fewster 1208.5399 Eq. (4)) --

    K_F = 19.8...  (MEASURED, 25 digits, two routes: a position-space
                    principal value with the exponential integral Ein, and a
                    Fourier quadrature in double precision; measured agreement
                    about 3e-12, ENFORCED at 1e-11)

    SD_0(tau) = sqrt(K_F)/tau^4 = SD0_OVER_C x C/tau^4    (tau-independent)

So the vacuum's smeared fluctuation is of the SAME ORDER as the QEI bound at
every tau -- the ratio is a shape number, not a function of scale.  At the
corridor's hold time tau = b/c, b = 1 m: SD_0 = 1.4e-25 Pa, against the demand
1.8058e46 Pa, 71.1 orders (flat figures; see the SURVEY status above).

===============================================================================
2.  (b)  T1 DOES NOT SURVIVE SMEARING -- COUNTEREXAMPLE, PROVED
===============================================================================

Smear Kuo-Ford's own measure (normal-ordered square, their normalisation):
    Delta'_f = ( <:A^2:> - <A>^2 ) / <A>^2 ,   A = rho(f).
For a zero-mean Gaussian state with normal-ordered two-point kernel G_AB,
Delta'_f = 2 ||K||_HS^2 / (tr K)^2 with K = f^(1/2) G f^(1/2).  Pointwise K is
4x4 and Cauchy-Schwarz gives 2/4 = 1/2 -- that IS T1 (fluctuation.py).
ILLUSTRATION ONLY, NOT PART OF THE PROOF: for a finite symmetric n x n matrix
the floor is 2/n, and z3 shows it at n = 4 (1/2 holds) and n = 8 (1/2 fails,
1/4 holds).  The smeared K acts on L^2(R) (x) C^4 and is not finite-rank; that
"smearing makes the rank unbounded" is NOT proved here.  The proof of (b) is
the counterexample below.

THE COUNTEREXAMPLE: THERMAL RADIATION, a zero-mean Gaussian (quasifree, KMS,
Hadamard) state.  Its normal-ordered phidot kernel in closed form is
    g(u) = -(1/2pi^2) d^3/du^3 [ (pi/2beta) coth(pi u/beta) - 1/(2u) ],
g(0) = pi^2/(30 beta^4) = rho (Stefan-Boltzmann), g -> -3/(2 pi^2 u^4).
Isotropy gives Delta'_f = (2/3) INT h(u) g(u)^2 du / g(0)^2, h = f*f.
HOELDER (L^inf x L^1) -- previously misnamed "Young" -- with ||h||_inf = h(0)
= ||f||_2^2 (h is an autocorrelation) and ||g^2||_1 = 180 (zeta(6) - zeta(7))
/(pi^3 beta^7) (Parseval, exact) gives the THEOREM

    Delta'_f  <=  (2/3) ||f||_2^2 ||g^2||_1 / rho^2
              =   (beta/tau) 108000 (zeta6 - zeta7)/(sqrt(2pi) pi^7)   (Gaussian f)

(the coefficient 108000 and zeta6 = pi^6/945 are DERIVED in sympy, not typed;
Delta_f = Delta'_f/(1 + Delta'_f), so Delta'_f < 1/2 is Delta_f < 1/3: the
same crossing breaks both halves of T1.)
z3 proves the right side < 1/2 at tau = beta from rational bounds on pi and
zeta(7); its hypotheses are checked satisfiable, and the same z3 query at
tau = beta/10 is NOT provable (vacuity guard).
MEASURED (Gaussian sampler, beta = 1): Delta'_f -> 2/3 as tau -> 0,
reproducing fluctuation.py's pointwise thermal value (imported); it is 1/2 at
tau* = TAU_STAR_OVER_BETA beta, 0.1186 at tau = beta, and falls as beta/tau.

THE NOISE KERNEL ITSELF IS A DIFFERENT QUANTITY AND IT IS MEASURED TOO.  Hu &
Verdaguer's N = <{t,t}>/2 is the FULL connected variance: vacuum part, a
vacuum-thermal cross term X (shot noise -- one contraction with the vacuum,
one with the photons) and KF's normal-ordered part.  X dominates:
Var = Var_0 + (4/3) X + (2/3) Y, X >= 0 because both spectral densities are
positive, and the full relative fluctuation R is 4.00 at tau = beta, 1.21 at
10 beta, 0.381 at 100 beta, and 1/2 at tau = 58.05 beta.  Its large-tau law is
exact: tau R^2 -> L = [(4/3) (S_0*S_g)(0) sqrt(2pi)/(4 pi^2)
+ (2/3) ||g^2||_1/sqrt(2pi)] / rho^2 = 14.513 (both coefficients derived in
sympy), matched by the measurement at 100 beta to about 1e-5 relative
(ENFORCED at 2e-5).  So R ~ 3.81 sqrt(beta/tau): smearing drives BOTH measures
to zero, which is what lets the semiclassical equation carry blackbody
radiation -- fluctuation.py's reason (a), now computed.  KF's normal ordering
deletes the shot noise, which is the dominant term.

===============================================================================
3.  (c)  THE QUESTION THAT DECIDES THE ROW -- IN THE FLAT MODEL
===============================================================================

THEOREM C1.  Hypotheses, each named and checked against the object
(HYPOTHESES below carries the same list with each check's status):
  H1  free scalar, minimal coupling, m >= 0.        MODEL (the refusal's own).
  H2  Minkowski spacetime, inertial worldline.       FAILS ON THE CORRIDOR,
                                                     MEASURED (b/l_G = 61.237).
  H3  A_tau realised as the FRIEDRICHS extension of the smeared Wick-ordered
      operator on Hadamard vectors, the self-adjoint operator FFR 1204.3570
      Sec. I say they mean; its lower bound is the form bound.  LOAD-BEARING:
      FFR say essential self-adjointness is "not fully resolved", and a
      different self-adjoint extension of a semibounded operator need not
      keep the Friedrichs lower bound.  C1 is about the Friedrichs extension.
  H4  the sampler root g in W^{2,2}(R) -- Fewster 1208.5399 p. 10: bound (3)
      "remains valid if one take g to be an element of the Sobolev space
      W^{2,2}(R)".  CHECKED: g, g' vanish at both ends (30 digits), g'' bounded.
  H5  the demanded density is held throughout an interval of length tau.
  H6  "distribution" means the quantum spectral measure mu_psi of A_tau (the
      measurement distribution of FFR 1004.0179 note [18]).  NOT the Gaussian
      Einstein-Langevin source of stochastic gravity, which H&V note
      "captures only partially the quantum nature" of the fluctuations; that
      reading is priced separately (section 0) and gives a nonzero number.
Then <psi, A_tau psi> >= -(1/16pi^2) INT g''^2 = -mu_1^4/(16 pi^2 tau^4) =
-C/tau^4 for every psi in the form domain (Fewster (3); the Rayleigh quotient of
the clamped mode is mu_1^4, CHECKED); Rayleigh-Ritz puts sigma(A_tau) in
[-C/tau^4, oo); every measurement distribution mu_psi is supported in
sigma(A_tau) (FFR 1004.0179 note [18], (a) => (b) => (c)).  So under H6
Prob_psi(outcome <= -D) = 0 for every psi whenever D > C/tau^4.   QED.

H2 IS NOT SATISFIED BY THE CORRIDOR, AND THE INSTRUMENT MEASURES BY HOW MUCH.
The demand fixes G_00 = 8 pi G D / c^4 in the core, a curvature length
l_G = (8 pi G D/c^4)^(-1/2) = 1.633e-2 m at b = 1 m, and (b / l_G)^2 is
EXACTLY 6 (M/b)/(a/b)^3 = B_OVER_LG_SQUARED = 3750 at every b -- derived
symbolically from achievable.required_density, a function of achievable.py's
two window parameters alone.  So achievable.py's sampling length b is 61 times
the curvature length the demand itself sets -- outside Ford-Roman's own
condition, "sampling time ... much smaller than the smallest local radius of
curvature" (gr-qc/9607003 Sec. 4, READ in achievable.py).  The flat refusal
survives shortening: H5 holds on every sub-interval, and at sampling length
eps*l_G the flat shortfall is log10(D/Q) + 4 log10(eps l_G/b): 64.108 orders
(eps = 1) and 60.108 orders (eps = 0.1) at b = 1 m.  corridor()'s output is
PINNED to that law (and to achievable's duration bound at the shorter time);
breaking the exponent 4 to 3 turns the selftest red.
THAT IS A FLAT-SPACE FIGURE AT A SHORTER SAMPLING TIME, NOT A CURVED QEI; the
curved evaluation is O2 (Fewster & Smith on the corridor, blocked on the
mode functions, fewsterteo.CORRIDOR_MODE_FUNCTIONS) and nothing here closes or
opens a row for it.

THE CURVED-SPACE VARIANCE -- WHAT IS AND IS NOT SHOWN.  The ledger's D22 text
said the smeared price "needs the curved-space renormalisation of quartic
operator products Kuo & Ford said did not exist".  That is wrong ONLY AS TO NEW
RENORMALISATION: Hu & Verdaguer (0802.0658 Sec. 3.2, after Eq. (3.12), READ):
for a linear field the noise kernel "is free of ultraviolet divergences because
the regularized T_ab differs from the renormalized T^R_ab by the identity
operator times some tensor counterterms ... so that in the subtraction (3.12)
the counterterms cancel".  A c-number shift moves the mean and no central
moment.  That quote is about SEPARATED points; H&V Sec. 5.2.1 say divergences
do occur in the coincidence limit.  FINITENESS of the WORLDLINE-SMEARED curved
variance for Hadamard states needs one more step: the pull-back of the
restricted Wightman derivatives to a timelike curve has wavefront set in
R x R+ x R x R-, so their product is defined (Fewster 1208.5399 Sec. 3.3).
That argument is NAMED, NOT RUN here.  Kuo & Ford's <:A^2:> in curved space
needs a REFERENCE STATE for its normal ordering; Var = <A^2> - <A>^2 does not.
The corridor's own curved variance is still NOT computed: it needs the
corridor's two-point function, which does not exist in the tree.

WHAT THIS FILE REFUSES
  * The relative fluctuation of a state carrying an ADMISSIBLE negative mean
    (between -C/tau^4 and 0) is NOT computed: the variance of a state near the
    bottom of the spectrum is not fixed by the mean, and no general bound is
    claimed.  It is not needed for the row: the demanded mean is not admissible
    (in the flat model).
  * Nonminimal coupling (Fewster 1208.5399 Sec. 5.1: no state-independent QEI;
    state-dependent bounds, Fewster-Osterbrink) and interacting fields (Sec.
    5.2): H1 is essential and nothing is claimed there.
  * The curved evaluation (O2).  No curvature-tightened figure is printed.
  * The Einstein-Langevin surrogate for states other than the vacuum: the
    probability there is set by the state's noise kernel, not computed.
  * 1204.3570's lower-bound estimates (0.0236 etc.) are FITS to 65 moments that
    FFR say may not determine the distribution; they are not used.

SOURCES, READ AT SOURCE THROUGH alphaXiv (full text or page text):
  Fewster, Ford & Roman 1004.0179 (2D; Eqs. (4), (18), (21)-(25), note [18]) --
  full text.  Fewster, Ford & Roman 1204.3570 (4D; Sec. I, Eqs. (24)-(36),
  Table I, Sec. IV) -- full text, read through Sec. V.A; Secs. V.B-VIII NOT
  READ.  Fewster 1208.5399 Sec. 1.3 Eqs. (1)-(4) and remarks, Sec. 2.4-2.5 --
  page text; Sec. 3.3 NAMED (cited by the DOCKET 64 verifier; its argument is
  not run here); Secs. 5.1 (nonminimal) and 5.2 (interacting) as cited.
  Hu & Verdaguer 0802.0658 (the 2008 update of the Living Review) Secs. 3.2,
  5.2.1, Eq. (3.13) -- page text; the 2003/2004 Living Review gr-qc/0307032
  that FFR cite is NAMED-NOT-READ.
"""
import os
import sys
import math
import cmath

WD = os.path.dirname(os.path.abspath(__file__))
if WD not in sys.path:
    sys.path.insert(0, WD)

import achievable          # C, the demand, the hold time
import fewsterteo          # the clamped sampler (double), GL panels
import fluctuation         # pointwise thermal Delta', T1

# ------------------------------------------------------------------ statuses
KEY = "smeared"
ROW = "D22"
STATUS = ("C1: THEOREM in the flat model H1-H6; (b) T1 fails under smearing: "
          "THEOREM; K_F, Delta'_f, R and the corridor figures: MEASURED; "
          "application to the corridor: SURVEY (H2 fails)")
STATUS_PARTS = {
    "C1": "THEOREM (flat model H1-H6)",
    "b_T1_fails_under_smearing": "THEOREM (Hoelder bound + z3, vacuity guard)",
    "K_F, Delta'_f, R, L, corridor figures": "MEASURED",
    "corridor application": "SURVEY",
    "rank-4 / rank-8 z3 checks": "ILLUSTRATION",
    "curved variance finiteness (Fewster 1208.5399 Sec. 3.3)": "NAMED, NOT RUN",
}
C1_FLAT_THEOREM = True                 # C1 proved in H1-H6 (flat)
CORRIDOR_APPLICATION = "SURVEY"        # H2 fails on the corridor
CURVED_PART_CARRIED_BY = "O2"          # absolute QEI on the corridor, via FFR note [18]
DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT = False
T1_SURVIVES_SMEARING = False
CURVED_VARIANCE_NEEDS_QUARTIC_RENORMALISATION = False     # no NEW renormalisation (H&V 3.2, READ)
CURVED_VARIANCE_FINITENESS = "NAMED, NOT RUN (Fewster 1208.5399 Sec. 3.3, wavefront pull-back)"
KUO_FORD_NORMAL_ORDERING_NEEDS_REFERENCE_STATE_IN_CURVED_SPACE = True
VARIANCE_NEEDS_REFERENCE_STATE = False
CURVED_VARIANCE_COMPUTED = False
ADMISSIBLE_NEGATIVE_MEAN_FLUCTUATION_COMPUTED = False
EL_SURROGATE_NONVACUUM_COMPUTED = False
ROW_TO_OPEN = None
PRICES_THE_CORRIDOR_FLAT = True        # SD_0 at tau = b/c, b = 1 m, computed (flat)
PRICES_THE_CORRIDOR_CURVED = False     # needs the corridor's two-point function (O2's blocker)
DECIDES_D22 = False                    # WITHDRAWN (was True) -- see WITHDRAWN

WITHDRAWN = {
    "DECIDES_D22 = True": (
        "DOCKET 64 ruling B1 / verify-fluct defect 0: C1 is proved only in the "
        "flat model and the instrument itself measures H2 failing by 61x on the "
        "corridor.  Replaced by C1_FLAT_THEOREM = True, CORRIDOR_APPLICATION = "
        "'SURVEY', CURVED_PART_CARRIED_BY = 'O2'."),
    "STATUS = 'THEOREM' (bare)": "split as STATUS / STATUS_PARTS above (ruling B1).",
    "'Probability exactly zero' without H6": (
        "holds only for the quantum spectral measure (H6); under the Gaussian "
        "Einstein-Langevin surrogate the probability is nonzero (verify-fluct "
        "defect 2)."),
    "'Young's inequality' for the (b) bound": "it is Hoelder (L^inf x L^1).",
    "'z3 proves the finite cases' as part of (b)'s proof": (
        "the rank-4/rank-8 checks are ILLUSTRATION about finite matrices; "
        "unbounded rank of the smeared kernel is not proved."),
    "'Fewster 5.1' for interacting fields": (
        "Sec. 5.1 is nonminimal coupling; interacting fields are Sec. 5.2."),
    "'the curved variance needs no renormalisation' (unqualified)": (
        "narrowed: no NEW renormalisation (READ); finiteness of the smeared "
        "curved variance NAMED (Fewster Sec. 3.3), not run."),
    "the '71.256 CONTROL'": (
        "it never read corridor(); it is a RECORD PIN READ from achievable.  "
        "corridor()'s own output is now pinned (corridor_pins)."),
}
CORRECTED = {
    "EL surrogate bound 'below exp(-10^142)' (DOCKET 64 ruling A1/D, verifier fix)": (
        "computed: -ln P = 10^EL_VACUUM_LOG10_NEG_LN_P = 10^141.916 with the "
        "vacuum noise kernel at b = 1 m, since (D/SD_0)^2/2 = 10^(2 x 71.108) / 2."
        "  exp(-10^141.916) is LARGER than exp(-10^142).  The supported "
        "statement is 'below exp(-10^141)', and only for the vacuum's noise "
        "kernel."),
}

# ------------------------------------------------------------------ hypotheses
HYPOTHESES = {
    "H1": ("free scalar, minimal coupling, m >= 0", "MODEL (the refusal's own)"),
    "H2": ("Minkowski spacetime, inertial worldline",
           "FAILS ON THE CORRIDOR: b/l_G = sqrt(B_OVER_LG_SQUARED), computed"),
    "H3": ("A_tau is the Friedrichs extension", "ASSUMED, load-bearing (FFR: 'not fully resolved')"),
    "H4": ("sampler root g in W^{2,2}", "CHECKED: g, g' vanish at the ends; g'' bounded"),
    "H5": ("demand held over an interval of length tau",
           "the demand's own statement: held for achievable.hold_time(b) = b/c"),
    "H6": ("'distribution' = quantum spectral measure of A_tau",
           "DEFINITION; the EL-surrogate reading priced separately"),
}

# ------------------------------------------------------------------ fixtures
# Figures the (stdlib-only) ledger prints.  Each FIXTURE is a MEASURED record
# value that --selftest reproduces from the computation; the others are
# computed here at import from achievable.py and the K_F fixture, stdlib only.
K_F_FIXTURE = 19.80242121506098        # FIXTURE: K_position (route P), pinned by --selftest
TAU_STAR_OVER_BETA = 0.140196          # FIXTURE: dprime_crossing, 6 digits, pinned by --selftest

B_OVER_LG_SQUARED = 6.0 * achievable.M_OVER_B / achievable.A_OVER_B ** 3   # computed
H2_SATISFIED_BY_CORRIDOR = math.sqrt(B_OVER_LG_SQUARED) < 1.0              # computed: False
SD0_OVER_C = math.sqrt(K_F_FIXTURE) / achievable.FEWSTER_C                 # computed from the fixture


def el_vacuum_log10_neg_ln_p(K_F=K_F_FIXTURE, b=1.0):
    """log10(-ln P) for P = Prob(A <= -D) under the Gaussian Einstein-Langevin
    surrogate with the VACUUM noise kernel (mean 0, SD = SD_0), stdlib only.
    Mills ratio: phi(z)/z (1 - 1/z^2) <= P <= phi(z)/z, so
    -ln P = z^2/2 + ln(z sqrt(2 pi)) + O(1/z^2); at z ~ 1e71 the O(1/z^2) term
    is far below double precision.  --selftest checks this against mpmath's
    erfc at 30 digits."""
    unit = achievable.HBAR / (achievable.C_SI ** 3 * achievable.hold_time(b) ** 4)
    z = achievable.required_density(b) / (math.sqrt(K_F) * unit)
    lz = math.log10(z)
    # -ln P = (z^2/2) (1 + 2 ln(z sqrt(2pi))/z^2); log10 of it, without overflow
    return 2 * lz - math.log10(2.0) + math.log10(1.0 + 2.0 * math.log(z * math.sqrt(2 * math.pi)) / z / z)


EL_VACUUM_LOG10_NEG_LN_P = el_vacuum_log10_neg_ln_p()                # computed: 141.916
EL_VACUUM_BELOW_EXP_MINUS_10_141 = EL_VACUUM_LOG10_NEG_LN_P > 141.0  # computed: True
EL_VACUUM_BELOW_EXP_MINUS_10_142 = EL_VACUUM_LOG10_NEG_LN_P > 142.0  # computed: False

SOURCES = {
    "1004.0179": ("Fewster, Ford & Roman, Probability distributions of smeared "
                  "quantum stress tensors (2D)", "full text"),
    "1204.3570": ("Fewster, Ford & Roman, Probability distributions for quantum "
                  "stress tensors in four dimensions", "full text through Sec. V.A"),
    "1208.5399": ("Fewster, Lectures on quantum energy inequalities",
                  "page text, Secs. 1.3, 2.4, 2.5, 4.2; Sec. 3.3 NAMED; "
                  "Sec. 5.1 nonminimal coupling, Sec. 5.2 interacting fields"),
    "0802.0658": ("Hu & Verdaguer, Stochastic Gravity: Theory and Applications "
                  "(2008 update)", "page text, Secs. 3.2, 5.2.1, Eq. (3.13)"),
    "gr-qc/0307032": ("Hu & Verdaguer, Living Rev. Rel. 7, 3 (2004)",
                      "NAMED-NOT-READ"),
}


def _need():
    try:
        import sympy as sp
        import mpmath as mp
        import z3
    except ImportError as exc:                  # pragma: no cover
        raise SystemExit("noise.py needs sympy, mpmath, z3: %s" % exc)
    return sp, mp, z3


# ============================================================ 1. the kernel
def kernel_point_split(sp):
    """(P): <:rho(t)::rho(t'):>_0 and <:phidot^2 phidot^2:>_0 as c/u^8.

    D_AB = d_A d'_B W, W = 1/(4 pi^2 sigma), spatial separation set to zero
    after differentiating; Wick: <:rho::rho':> = (1/2) SUM_AB D_AB^2."""
    t, tp, x, y, z, xp, yp, zp = sp.symbols('t tp x y z xp yp zp', real=True)
    u = sp.symbols('u', positive=True)
    W = 1 / (4 * sp.pi**2 * ((x - xp)**2 + (y - yp)**2 + (z - zp)**2 - (t - tp)**2))
    X, XP = (t, x, y, z), (tp, xp, yp, zp)
    at = {x: 0, y: 0, z: 0, xp: 0, yp: 0, zp: 0}
    D = [[sp.simplify(sp.diff(W, X[A], XP[B]).subs(at).subs({t: u, tp: 0}))
          for B in range(4)] for A in range(4)]
    rho = sp.simplify(sp.Rational(1, 2) * sum(D[A][B]**2 for A in range(4) for B in range(4)))
    pd2 = sp.simplify(2 * D[0][0]**2)
    return dict(D=D, rho=sp.simplify(rho * u**8), phidot2=sp.simplify(pd2 * u**8),
                D00=sp.simplify(D[0][0] * u**4))


def fourier_power(sp, n):
    """INT_0^oo w^(n-1) e^{-a w} dw = (n-1)!/a^n, a = i(u - i eps): the
    identity 1/(u-i0)^n = (1/(n-1)!) INT_0^oo w^(n-1) e^{-iwu} dw, since i^n = 1
    for n = 8.  Returns the sympy value of the integral at symbolic a > 0."""
    w, a = sp.symbols('w a', positive=True)
    return sp.simplify(sp.integrate(w**(n - 1) * sp.exp(-a * w), (w, 0, sp.oo)) * a**n)


def kernel_mode_sum(sp, which, drop_angle=False):
    """(F): Var = kappa * INT_0^oo s^n |fhat(s)|^2 ds, from ||A|0>||^2.

    which: 'rho' (4D energy density), 'phidot2', 'phi2' (4D Wick squares),
           'chiral' (2D right-moving T_R = :(d_u phi)^2:).
    drop_angle=True replaces the angular average by 1 -- a PLANTED ERROR used
    only by the selftest to show the FFR comparison can fail."""
    w, wp, c, s = sp.symbols('w wp c s', positive=True)
    cs = sp.symbols('cs', real=True)
    if which == 'chiral':
        # dmu = dk/(2 pi 2k); amplitude (ik)(ik') = -k k'
        P2 = (w * wp)**2
        integrand = 2 * P2 / ((4 * sp.pi * w) * (4 * sp.pi * wp))
    else:
        # dmu = d^3k/((2pi)^3 2w); d^3k -> w^2 dw dOmega; angular measure of the
        # relative angle: (4 pi)(2 pi) INT_{-1}^{1} d(cos)
        if which == 'rho':
            P2 = sp.Rational(1, 4) * (w * wp + w * wp * cs)**2
        elif which == 'phidot2':
            P2 = (w * wp)**2
        elif which == 'phi2':
            P2 = sp.Integer(1)
        else:
            raise ValueError(which)
        if drop_angle:
            ang = 8 * sp.pi**2 * 2 * P2.subs(cs, 1)
        else:
            ang = 8 * sp.pi**2 * sp.integrate(P2, (cs, -1, 1))
        integrand = 2 * ang * w**2 * wp**2 / ((2 * sp.pi)**6 * 4 * w * wp)
    # INT INT dw dwp F(w + wp) h(w, wp) = INT ds F(s) INT_0^s h(w, s - w) dw
    radial = sp.integrate(sp.expand(integrand.subs(wp, s - w)), (w, 0, s))
    radial = sp.factor(sp.simplify(radial))
    n = sp.degree(sp.Poly(radial, s))
    return sp.simplify(radial / s**n), n


def sampler_variances(sp, kappa, n):
    """Var for the Lorentzian (fhat = e^{-|w| tau}) and Gaussian
    (fhat = e^{-w^2 tau^2/4}) samplers, exact."""
    s, tau = sp.symbols('s tau', positive=True)
    lor = sp.simplify(kappa * sp.integrate(s**n * sp.exp(-2 * s * tau), (s, 0, sp.oo)))
    gau = sp.simplify(kappa * sp.integrate(s**n * sp.exp(-s**2 * tau**2 / 2), (s, 0, sp.oo)))
    return lor, gau, tau


_VAC = {}


def vacuum_gaussian_K(sp):
    """Gaussian-sampler Var_0 tau^8, DERIVED from the mode sum (cached)."""
    if 'K' not in _VAC:
        kap, n = kernel_mode_sum(sp, 'rho')
        lor, gau, tt = sampler_variances(sp, kap, n)
        _VAC['K'] = sp.simplify(gau.subs(tt, 1))
    return _VAC['K']


def fe_bound_lorentzian(sp):
    """(4 pi tau^2)^2 * (1/16 pi^2) INT ((sqrt L)'')^2 dt: FFR 1204.3570 quote the
    Fewster-Eveson bound for rho_S as x_0(FE) = 27/128.  Fewster (3) is the
    bound C comes from, so this ties C's normalisation to FFR's number."""
    t, tau = sp.symbols('t tau', positive=True)
    L = tau / (sp.pi * (t**2 + tau**2))
    I = 2 * sp.integrate(sp.simplify(sp.diff(sp.sqrt(L), t, 2)**2), (t, 0, sp.oo))
    return sp.simplify((4 * sp.pi * tau**2)**2 * I / (16 * sp.pi**2))


# =================================================== 1b. Fewster's own sampler
def clamped(mp, root_guess='4.73'):
    """g = cosh - cos - sigma (sinh - sin) at mu, as SUM c_k e^{a_k t}; F = g^2/N
    as SUM over pairs.  mu from the DEFINING equation cos mu cosh mu = 1."""
    mu = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, mp.mpf(root_guess))
    sg = (mp.cosh(mu) - mp.cos(mu)) / (mp.sinh(mu) - mp.sin(mu))
    a = [mu, -mu, 1j * mu, -1j * mu]
    c = [(1 - sg) / 2, (1 + sg) / 2, -(1 + 1j * sg) / 2, -(1 - 1j * sg) / 2]

    def g(t, d=0):
        return mp.re(sum(ck * ak**d * mp.exp(ak * t) for ak, ck in zip(a, c)))
    N = mp.quad(lambda t: g(t)**2, [0, 0.5, 1])
    S = [(a[j] + a[k], c[j] * c[k] / N) for j in range(4) for k in range(4)]
    return dict(mu=mu, g=g, N=N, S=S)


def _Fn(S, n, t, mp):
    return mp.re(sum(cc * s**n * mp.exp(s * t) for s, cc in S))


def rayleigh(mp, cl):
    """INT g''^2 / INT g^2 -- equals mu^4 for the clamped fundamental."""
    g = cl['g']
    return mp.quad(lambda t: g(t, 2)**2, [0, 0.5, 1]) / cl['N']


def _ein(z, mp):
    """Ein(z) = SUM_{k>=1} (-1)^(k+1) z^k/(k k!) -- entire; |z| <= 2 mu here."""
    tot, term, k = mp.mpc(0), mp.mpc(1), 0
    while True:
        k += 1
        term = term * z / k
        add = term / k * (1 if k % 2 else -1)
        tot += add
        if abs(add) < mp.mpf(10) ** (-mp.mp.dps - 5) and k > 5:
            return tot


def K_position(mp, cl):
    """ROUTE P.  Var_0 = (3/2pi^4) INT INT F F/(x-y-i0)^8.
    u^-8 = -(1/7!) (u^-1)^(7); four integrations by parts in x, three in y (F,
    F', F'', F''' vanish at both ends) give -(1/7!) INT INT F''''(x) F'''(y)
    /(x-y-i0).  Its i pi delta part is i pi [F'''^2/2]_0^1 = 0.  The PV inner
    integral is closed form: PV INT_0^1 e^{sy}/(x-y) dy
        = -e^{sx} [ -Ein(-s(1-x)) + Ein(s x) + ln((1-x)/x) ]."""
    S = cl['S']

    def inner(x):
        tot = 0
        for s, cc in S:
            if s == 0:
                continue
            tot += cc * s**3 * (-mp.exp(s * x)) * (
                -_ein(-s * (1 - x), mp) + _ein(s * x, mp) + mp.log((1 - x) / x))
        return mp.re(tot)
    pv = mp.quad(lambda x: _Fn(S, 4, x, mp) * inner(x), [0, 0.5, 1])
    return mp.mpf(3) / (2 * mp.pi**4) * (-1 / mp.factorial(7)) * pv


def K_fourier(U=2.0e4):
    """ROUTE F, double precision, independent code path.  F-hat = H/nu^4 with
    H = FT(F'''') (no cancellation: H ~ 1/nu), so INT_0^oo nu^7 |Fhat|^2 =
    INT_0^oo |H|^2/nu.  Panels and nodes are fewsterteo's (imported).  Tail
    beyond U: |H|^2 -> 2 F4^2 (1 - cos nu)/nu^2 with F4 = F''''(0) = F''''(1)
    (the mode is symmetric), whose integral against 1/nu is F4^2/U^2 to
    O(U^-3)."""
    a, c = fewsterteo._sampler()
    N = fewsterteo._panels(lambda t: sum(ck * cmath.exp(ak * t) for ak, ck in zip(a, c)).real ** 2,
                           0.0, 1.0, 0.02)
    S = [(a[j] + a[k], c[j] * c[k] / N) for j in range(4) for k in range(4)]

    def H(nu):
        tot = 0j
        for s, cc in S:
            if s == 0:
                continue
            zz = s - 1j * nu
            tot += cc * s**4 * (cmath.exp(zz) - 1.0) / zz
        return tot

    def integrand(nu):
        if nu == 0.0:
            return 0.0
        h = H(nu)
        return (h.real**2 + h.imag**2) / nu
    F4 = sum(cc * s**4 for s, cc in S).real
    J = fewsterteo._panels(integrand, 0.0, U, 1.0) + F4**2 / U**2
    return J / (3360.0 * math.pi**4), F4


# ================================================================ 2. thermal
def thermal_kernel(sp):
    """g(u) = <:phidot(t+u) phidot(t):>_beta at one point, beta = 1, closed
    form, from INT_0^oo sin(ku)/(e^k - 1) dk = (pi/2) coth(pi u) - 1/(2u)."""
    u = sp.symbols('u', positive=True)
    base = sp.pi / 2 * sp.coth(sp.pi * u) - 1 / (2 * u)
    g = sp.simplify(-sp.diff(base, u, 3) / (2 * sp.pi**2))
    return u, base, g


def g2_norm_exact(sp):
    """||g^2||_1 = (1/4 pi^3) INT_0^oo k^6 n(k)^2 dk = 180 (zeta6 - zeta7)/pi^3
    (Parseval; 1/(e^x-1)^2 = SUM (n-1) e^{-nx})."""
    n = sp.symbols('n', integer=True, positive=True)
    series = sp.summation((n - 1) * sp.factorial(6) / n**7, (n, 1, sp.oo))
    return sp.simplify(series / (4 * sp.pi**3)), sp.simplify(180 * (sp.zeta(6) - sp.zeta(7)) / sp.pi**3)


def cross_at_zero_exact(sp):
    """(S_0*S_g)(0) = INT_0^oo S_0(w) S_g(w) dw = (1/4 pi^2) INT_0^oo w^6 n(w) dw
    = (1/4 pi^2) SUM_n 6!/n^7 (1/(e^x-1) = SUM e^{-nx}).  DERIVED."""
    n = sp.symbols('n', integer=True, positive=True)
    return sp.simplify(sp.summation(sp.factorial(6) / n**7, (n, 1, sp.oo)) / (4 * sp.pi**2))


def _mpnum(sp, mp, expr):
    return mp.mpf(str(sp.N(expr, mp.mp.dps + 15)))


_THERMAL = {}


def _thermal_prep(sp):
    if 'prep' not in _THERMAL:
        u, base, g = thermal_kernel(sp)
        T = sp.symbols('T', positive=True)
        hs = sp.exp(-u**2 / (2 * T**2)) / (T * sp.sqrt(2 * sp.pi))
        gser = sp.series(g, u, 0, 40).removeO()   # radius 1; 40 terms at u < 0.2
        _THERMAL['prep'] = (u, base, g, sp.lambdify(u, g, 'mpmath'),
                            sp.lambdify(u, gser, 'mpmath'),
                            sp.lambdify((u, T), sp.diff(hs * g, u, 3), 'mpmath'),
                            sp.lambdify((u, T), sp.diff(hs * gser, u, 3), 'mpmath'))
        _THERMAL['rho'] = sp.limit(g, u, 0)           # DERIVED: pi^2/30
        _THERMAL['g2'] = g2_norm_exact(sp)[0]         # DERIVED: the series form
        _THERMAL['K0'] = vacuum_gaussian_K(sp)        # DERIVED: 1/(70 pi^4)
        _THERMAL['conv0'] = cross_at_zero_exact(sp)   # DERIVED: 720 zeta7/(4 pi^2)
    return _THERMAL


def thermal_numbers(sp, mp, taus, fourier_at=None):
    """Delta'_f (KF's normal-ordered measure) and the FULL noise-kernel relative
    fluctuation, Gaussian sampler of width tau (units of beta = 1).

    Full variance of A = rho(f) in the thermal state (isotropy, Wick):
        Var = Var_0 + (4/3) X + (2/3) Y,
        X = INT h W_0 g du,  Y = INT h g^2 du,  h = f*f,  W_0 = 3/(2pi^2 (u-i0)^4).
    POSITION ROUTE (all tau): Y directly; X = (1/2pi^2) INT_0^oo q3(u)/u du,
    q3 the third derivative of q = h g, from (u-i0)^-4 = -(1/6) d^3/du^3
    (u-i0)^-1 and q3 odd.  FOURIER ROUTE (at tau = fourier_at only -- slow):
    X and Y as INT |fhat|^2 (S*S)/(4 pi^2), S_0 = w^3 theta(w)/2pi,
    S_g = |w|^3 n(|w|)/2pi.
    rho, ||g^2||_1 and the vacuum Gaussian K are DERIVED in sympy (cached)."""
    P = _thermal_prep(sp)
    u, base, g, g_mp, gs_mp, q3, q3s = P['prep']
    gf = lambda x: gs_mp(abs(x)) if abs(x) < mp.mpf('0.2') else g_mp(abs(x))
    q3f = lambda x, t: q3s(x, t) if x < mp.mpf('0.2') else q3(x, t)
    rho = _mpnum(sp, mp, P['rho'])
    g2 = _mpnum(sp, mp, P['g2'])
    K0 = _mpnum(sp, mp, P['K0'])
    S0 = lambda w: w**3 / (2 * mp.pi) if w > 0 else mp.mpf(0)
    Sg = lambda w: (abs(w)**3 / mp.expm1(abs(w)) / (2 * mp.pi)) if w != 0 else mp.mpf(0)

    def conv(A, B, nu):
        return mp.quad(lambda w: A(w) * B(nu - w), [-mp.inf, min(0, nu), max(0, nu), mp.inf])
    out = []
    for tau in taus:
        tau = mp.mpf(tau)
        h = lambda x: mp.exp(-x**2 / (2 * tau**2)) / (tau * mp.sqrt(2 * mp.pi))
        pts = [0, mp.mpf('0.2'), tau, 10 * tau + 10, mp.inf]
        Y = 2 * mp.quad(lambda x: h(x) * gf(x)**2, pts)
        X = mp.quad(lambda x: q3f(x, tau) / x, pts) / (2 * mp.pi**2)
        var0 = K0 / tau**8
        full = var0 + mp.mpf(4) / 3 * X + mp.mpf(2) / 3 * Y
        # Hoelder: INT h g^2 <= h(0) ||g^2||_1, h(0) = ||f||_2^2 = 1/(tau sqrt(2 pi))
        hoelder = mp.mpf(2) / 3 * h(0) * g2 / rho**2
        row = dict(tau=tau, dprime=mp.mpf(2) / 3 * Y / rho**2, Y=Y, X=X, var0=var0,
                   full_rel=mp.sqrt(full) / rho, hoelder=hoelder)
        if fourier_at is not None and tau == mp.mpf(fourier_at):
            fh2 = lambda nu: mp.exp(-nu**2 * tau**2 / 2)
            row['Y_f'] = 2 * mp.quad(lambda nu: fh2(nu) * conv(Sg, Sg, nu),
                                     [0, 1 / tau, 10 / tau, mp.inf]) / (4 * mp.pi**2)
            row['X_f'] = mp.quad(lambda nu: fh2(nu) * conv(S0, Sg, nu),
                                 [-mp.inf, -1 / tau, 0, 1 / tau, mp.inf]) / (4 * mp.pi**2)
        out.append(row)
    return out, gf, g, u, base


def vacuum_pv_control(sp):
    """The position-space PV machinery on the VACUUM, exactly: Var_0 =
    (2/3) INT h W_0^2 = (3/2pi^4)(1/7!) 2 INT_0^oo h7(u)/u du, h7 the seventh
    derivative of the Gaussian h = f*f.  Must equal the mode sum's Gaussian
    Var_0 (vacuum_gaussian_K / tau^8).  Returns the ratio (sympy, exact)."""
    u, T = sp.symbols('u T', positive=True)
    h = sp.exp(-u**2 / (2 * T**2)) / (T * sp.sqrt(2 * sp.pi))
    I = sp.integrate(sp.expand(sp.diff(h, u, 7) / u), (u, 0, sp.oo))
    return sp.simplify(sp.Rational(3, 2) / sp.pi**4 / sp.factorial(7) * 2 * I
                       * T**8 / vacuum_gaussian_K(sp))


def full_asymptotic(sp, mp):
    """tau R^2 -> L as tau -> oo (beta = 1), R the FULL relative fluctuation:
    X -> (S_0*S_g)(0) sqrt(2pi)/(4 pi^2 tau);  Y -> ||g^2||_1 /(sqrt(2pi) tau);
    Var_0 ~ tau^-8 drops out.  Every coefficient DERIVED (cross_at_zero_exact,
    g2_norm_exact, the thermal kernel's g(0))."""
    P = _thermal_prep(sp)
    rho = _mpnum(sp, mp, P['rho'])
    X1 = _mpnum(sp, mp, P['conv0']) * mp.sqrt(2 * mp.pi) / (4 * mp.pi**2)
    Y1 = _mpnum(sp, mp, P['g2']) / mp.sqrt(2 * mp.pi)
    return (mp.mpf(4) / 3 * X1 + mp.mpf(2) / 3 * Y1) / rho**2


def full_crossing(sp, mp):
    """tau (units of beta) at which the FULL relative fluctuation is 1/2."""
    def R(t):
        return thermal_numbers(sp, mp, (t,))[0][0]['full_rel'] - mp.mpf(1) / 2
    return mp.findroot(R, (mp.mpf(40), mp.mpf(80)), solver='secant')


def dprime_crossing(sp, mp, gf):
    rho = _mpnum(sp, mp, _thermal_prep(sp)['rho'])

    def dp(tau):
        h = lambda x: mp.exp(-x**2 / (2 * tau**2)) / (tau * mp.sqrt(2 * mp.pi))
        return mp.mpf(2) / 3 * 2 * mp.quad(lambda x: h(x) * gf(x)**2, [0, tau, 10 * tau, mp.inf]) / rho**2
    return mp.findroot(lambda t: dp(t) - mp.mpf(1) / 2, mp.mpf('0.07'))


# ==================================================================== proofs
def prove(z3, hyps, goal):
    s = z3.Solver()
    s.add(*hyps)
    s.add(z3.Not(goal))
    return s.check() == z3.unsat


def hoelder_bound_constants(sp):
    """DERIVE the Hoelder bound's constants in sympy: B(tau) = (2/3) h(0)
    ||g^2||_1 / rho^2 with h(0) = 1/(tau sqrt(2 pi)) (beta = 1).  Returns
    (coef, z6) with B = coef (zeta(6) - zeta(7)) / (tau sqrt(2 pi) pi^7) and
    zeta(6) = z6 pi^6; coef and z6 are exact rationals (108000 and 1/945)."""
    tau = sp.symbols('tau', positive=True)
    u, base, g = thermal_kernel(sp)
    rho = sp.limit(g, u, 0)
    B = sp.Rational(2, 3) / (tau * sp.sqrt(2 * sp.pi)) * g2_norm_exact(sp)[1] / rho**2
    z6 = sp.nsimplify(sp.zeta(6) / sp.pi**6)
    coef = sp.simplify(B * tau * sp.sqrt(2 * sp.pi) * sp.pi**7 / (sp.zeta(6) - sp.zeta(7)))
    return coef, z6


def hoelder_bound_proof(z3, tau_over_beta, coef, z6):
    """PROVE (beta/tau) coef (z6 pi^6 - z7)/(sqrt(2 pi) pi^7) < 1/2 from
    333/106 < pi < 355/113, sum_{1}^{30} n^-7 <= z7 <= that + 1/(6*30^6),
    r^2 = 2 pi, r > 0.  Returns (proved, hypotheses_satisfiable): the second
    is the vacuity guard -- a proof from unsatisfiable hypotheses is worthless."""
    from fractions import Fraction as Fr
    lo7 = sum(Fr(1, n**7) for n in range(1, 31))
    hi7 = lo7 + Fr(1, 6 * 30**6)
    p, z7, r = z3.Reals('p z7 r')
    T = z3.RealVal(str(Fr(tau_over_beta).limit_denominator(10**6)))
    H = [p > z3.RealVal("333/106"), p < z3.RealVal("355/113"),
         z7 >= z3.RealVal(str(lo7)), z7 <= z3.RealVal(str(hi7)),
         r > 0, r * r == 2 * p]
    # bound < 1/2  <=>  2*coef*(z6 p^6 - z7) < T r p^7   (all positive)
    goal = 2 * z3.RealVal(str(coef)) * (z3.RealVal(str(z6)) * p**6 - z7) < T * r * p**7
    s = z3.Solver()
    s.add(*H)
    return prove(z3, H, goal), s.check() == z3.sat


def rank_floor(z3, n, floor):
    """ILLUSTRATION, NOT PROOF: for a real symmetric n x n K,
    2 ||K||^2 >= floor (tr K)^2.  A statement about finite matrices only; the
    smeared thermal kernel is not finite-rank.  Returns (proved,
    counterexample_exists)."""
    k = {(i, j): z3.Real('k%d_%d' % (min(i, j), max(i, j))) for i in range(n) for j in range(n)}
    tr = z3.Sum([k[i, i] for i in range(n)])
    hs = z3.Sum([k[i, j] * k[i, j] for i in range(n) for j in range(n)])
    goal = 2 * hs >= z3.RealVal(floor) * tr * tr
    proved = prove(z3, [], goal)
    s = z3.Solver()
    s.add(z3.Not(goal))
    return proved, s.check() == z3.sat


# ========================================================== 3. the corridor
def corridor(K_F, b=1.0, _shorten_exponent=4):
    """The flat figures at the corridor's scales.  _shorten_exponent is a
    PLANTED-ERROR hook used only by --selftest (and the verifier's break) to
    show corridor_pins fires when the shortening law is wrong; it is 4 in
    every real call.  prob_outcome_at_demand_H6 is a THEOREM CONSEQUENCE of C1
    under H1-H6 (conditional on -D < -Q), not a measured figure."""
    C = achievable.FEWSTER_C
    Q = achievable.persistence_allow(b)                  # C hbar/(c^3 tau^4), tau = b/c
    D = achievable.required_density(b)
    unit = achievable.HBAR / (achievable.C_SI**3 * achievable.hold_time(b)**4)
    sd = math.sqrt(K_F) * unit
    lG = (8 * math.pi * achievable.G_SI * D / achievable.C_SI**4) ** -0.5
    short = lambda eps: math.log10(achievable.persistence_shortfall(b)
                                   * (eps * lG / b) ** _shorten_exponent)
    return dict(C=C, Q=Q, D=D, sd=sd, sd_over_Q=sd / Q, D_over_sd=D / sd,
                orders_sd=math.log10(D / sd), orders_Q=math.log10(D / Q),
                lG=lG, b_over_lG=b / lG,
                short1=short(1.0), short01=short(0.1),
                prob_outcome_at_demand_H6=("0 -- THEOREM consequence of C1 (H1-H6)"
                                           if -D < -Q else "NOT DECIDED BY C1"))


def shortening_exponent():
    """The exponent of the flat bound's scaling with sampling time, READ OFF
    achievable's duration bound (not typed): log10(Q(b)/Q(10 b))."""
    return math.log10(achievable.persistence_allow(1.0) / achievable.persistence_allow(10.0))


def corridor_pins(c, b=1.0):
    """Residuals pinning corridor()'s OWN output (ruling B1 / verify-fluct
    defect 1).  Each is 0 to float rounding when corridor() is right:
      dq     log10(D/Q) from corridor() vs log10(achievable.persistence_shortfall(b))
      law1   short1 vs log10(D/Q) + k log10(l_G/b), k = shortening_exponent()
      step   (short1 - short01) vs k log10(10) = k
      direct short(eps) vs log10(D / achievable.persistence_allow(eps l_G)) --
             achievable's duration bound evaluated at the shorter sampling
             time, an independent route, eps = 1 and 0.1."""
    k = shortening_exponent()
    lg = math.log10(c['lG'] / b)
    return dict(
        dq=abs(c['orders_Q'] - math.log10(achievable.persistence_shortfall(b))),
        law1=abs(c['short1'] - (c['orders_Q'] + k * lg)),
        step=abs((c['short1'] - c['short01']) - k),
        direct=max(abs(c['short1'] - math.log10(c['D'] / achievable.persistence_allow(c['lG']))),
                   abs(c['short01'] - math.log10(c['D'] / achievable.persistence_allow(0.1 * c['lG'])))))


PIN_TOL = 1e-12        # absolute, in log10 units: float rounding, not a physical tolerance


def el_surrogate_mp(mp, D, sd):
    """Gaussian Einstein-Langevin surrogate, VACUUM noise kernel: P = Prob(A <=
    -D) = erfc(z/sqrt2)/2, z = D/SD_0, by mpmath's erfc at the working
    precision.  Returns (z, log10(-ln P))."""
    z = mp.mpf(D) / mp.mpf(sd)
    P = mp.erfc(z / mp.sqrt(2)) / 2
    return z, mp.log10(-mp.log(P))


def b_over_lG_symbolic(sp):
    """(b/l_G)^2 = 8 pi G D b^2/c^4, with D = achievable.required_density(b, m, a)
    called on SYMBOLS: returns (the expression, its free symbols).  b must
    cancel exactly; the coefficient of m/a^3 is 6 up to the float pi and SI
    constants achievable carries."""
    m, a, b = sp.symbols('m a b', positive=True)
    D = achievable.required_density(b, m, a)
    e = sp.simplify(8 * sp.pi * achievable.G_SI * D / achievable.C_SI**4 * b**2)
    return e, e.free_symbols, (m, a, b)


# ==================================================================== report
def compute(sp, mp, z3, fast=False):
    r = {}
    kp = kernel_point_split(sp)
    r['kp'] = kp
    r['fourier8'] = fourier_power(sp, 8)
    r['kf'] = {w: kernel_mode_sum(sp, w) for w in ('rho', 'phidot2', 'phi2', 'chiral')}
    r['kf_planted'] = kernel_mode_sum(sp, 'rho', drop_angle=True)
    r['fe27'] = fe_bound_lorentzian(sp)
    mp.mp.dps = 30
    cl = clamped(mp)
    r['cl'] = cl
    r['rayleigh'] = rayleigh(mp, cl)
    r['bc'] = max(abs(v) for v in (cl['g'](0), cl['g'](0, 1), cl['g'](1), cl['g'](1, 1)))
    r['g2sup'] = max(abs(cl['g'](mp.mpf(i) / 200, 2)) for i in range(201))
    cl2 = clamped(mp, '7.85')
    r['rayleigh_mu2'] = rayleigh(mp, cl2)
    mp.mp.dps = 25
    r['K_P'] = K_position(mp, cl)
    r['K_F'], r['F4'] = K_fourier()
    mp.mp.dps = 20
    taus = (0.01, 0.1, 1, 10, 100)
    r['th'], gf, g, u, base = thermal_numbers(sp, mp, taus, fourier_at=None if fast else 1)
    r['L'] = full_asymptotic(sp, mp)
    r['full_cross'] = full_crossing(sp, mp)
    r['vac_pv'] = vacuum_pv_control(sp)
    r['g_sym'], r['u'], r['base'], r['gf'] = g, u, base, gf
    r['tau_star'] = dprime_crossing(sp, mp, gf)
    r['g2'] = g2_norm_exact(sp)
    r['hconst'] = hoelder_bound_constants(sp)
    r['hoelder1'] = hoelder_bound_proof(z3, 1, *r['hconst'])
    r['hoelder01'] = hoelder_bound_proof(z3, sp.Rational(1, 10), *r['hconst'])
    r['rank4'] = rank_floor(z3, 4, "1/2")
    r['rank8_half'] = rank_floor(z3, 8, "1/2")
    r['rank8_quarter'] = rank_floor(z3, 8, "1/4")
    r['cor'] = corridor(float(r['K_P']))
    mp.mp.dps = 30
    r['el'] = el_surrogate_mp(mp, r['cor']['D'], mp.sqrt(r['K_P']) * mp.mpf(
        achievable.HBAR / (achievable.C_SI**3 * achievable.hold_time(1.0)**4)))
    return r


def report():
    sp, mp, z3 = _need()
    r = compute(sp, mp, z3)
    print("=" * 79)
    print("noise.py -- D22, the smeared fluctuation demand at the corridor's scales")
    print("=" * 79)
    print("STATUS: %s" % STATUS)
    kap, n = r['kf']['rho']
    print("\n(a) Var_0[rho(f)] = %s * INT_0^oo w^%d |fhat|^2 dw   (mode sum)" % (kap, n))
    print("    point-split <:rho::rho':>_0 = %s / (u-i0)^8" % r['kp']['rho'])
    lor, gau, _ = sampler_variances(sp, kap, n)
    print("    Lorentzian Var_0 = %s    Gaussian Var_0 = %s" % (lor, gau))
    print("    Fewster's clamped sampler: K_F = %s (route P, 25 dps)" % mp.nstr(r['K_P'], 20))
    print("                               K_F = %.12g (route F, double)" % r['K_F'])
    c = r['cor']
    print("    SD_0 / (C/tau^4) = %.6f  at EVERY tau" % c['sd_over_Q'])
    print("    at tau = b/c, b = 1 m (flat):  SD_0 = %.4e Pa   C/tau^4 = %.4e Pa   demand = %.4e Pa"
          % (c['sd'], c['Q'], c['D']))
    print("    demand / SD_0 = 10^%.3f" % c['orders_sd'])
    print("\n(b) thermal, Gaussian sampler, tau in units of beta:")
    print("    %8s %14s %14s %16s" % ("tau", "Delta'_f", "Hoelder bound", "full rel. fluct"))
    for row in r['th']:
        print("    %8s %14s %14s %16s" % (mp.nstr(row['tau'], 3), mp.nstr(row['dprime'], 8),
                                         mp.nstr(row['hoelder'], 8), mp.nstr(row['full_rel'], 8)))
    print("    Delta'_f = 1/2 at tau = %s beta;  z3: Hoelder bound < 1/2 at tau = beta: %s;"
          " at tau = beta/10: %s" % (mp.nstr(r['tau_star'], 6), r['hoelder1'][0], r['hoelder01'][0]))
    print("    (rank-4 / rank-8 z3 checks: ILLUSTRATION only)")
    print("    T1 SURVIVES SMEARING: %s" % T1_SURVIVES_SMEARING)
    print("\n(c) C1 (THEOREM, flat model H1-H6): sigma(A_tau) in [-C/tau^4, oo).")
    print("    demand / (C/tau^4) = 10^%.3f  (READ from achievable: persistence_shortfall)"
          % c['orders_Q'])
    print("    Prob(any single outcome <= -demand), any state, under H6: %s"
          % c['prob_outcome_at_demand_H6'])
    print("    Einstein-Langevin surrogate, vacuum noise kernel: P = exp(-10^%.3f)"
          " (z = 10^%.3f);  below exp(-10^141): %s;  below exp(-10^142): %s"
          % (float(r['el'][1]), float(mp.log10(r['el'][0])),
             EL_VACUUM_BELOW_EXP_MINUS_10_141, EL_VACUUM_BELOW_EXP_MINUS_10_142))
    print("    H2 check: curvature length l_G = %.4e m;  b / l_G = %.3f at every b"
          % (c['lG'], c['b_over_lG']))
    print("    CORRIDOR APPLICATION: %s -- flat shortfall at sampling length l_G: %.3f orders;"
          " at 0.1 l_G: %.3f orders" % (CORRIDOR_APPLICATION, c['short1'], c['short01']))
    pins = corridor_pins(c)
    print("    corridor pins (max residual, log10 units): %.2e" % max(pins.values()))
    print("    curved part carried by: %s" % CURVED_PART_CARRIED_BY)
    print("    full noise-kernel relative fluctuation: 1/2 at tau = %s beta; tau R^2 -> %s"
          % (mp.nstr(r['full_cross'], 6), mp.nstr(r['L'], 8)))
    print("    IN THE FLAT MODEL THE DEMAND COLUMN IS NOT RESTATED; ON THE CORRIDOR, SURVEY.\n")


# ================================================================== selftest
def selftest():
    sp, mp, z3 = _need()
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-72s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def near(label, got, want, tol):
        ok = abs(float(got) / float(want) - 1.0) <= tol
        print("  [%s] %-72s %.12g" % ("ok" if ok else "XX", label, float(got)))
        if not ok:
            fails.append((label, float(got), float(want)))

    def within(label, resid, tol):
        ok = float(resid) <= tol
        print("  [%s] %-72s %.3g" % ("ok" if ok else "XX", label, float(resid)))
        if not ok:
            fails.append((label, float(resid), tol))

    print("noise.py --selftest")
    print("  row kinds: CONTROL = computed, can fail; RECORD = a pinned flag or")
    print("  fixture, reproduced where marked; ILLUSTRATION = not part of a proof\n")
    r = compute(sp, mp, z3)
    s, tau = sp.symbols('s tau', positive=True)

    print("(a) THE KERNEL, TWO ROUTES")
    chk("(P) D_00 = 3/(2 pi^2 u^4): FFR 1204.3570 Eq. (25)", r['kp']['D00'], 3 / (2 * sp.pi**2))
    chk("(P) <:rho::rho':>_0 u^8 = 3/(2 pi^4)", r['kp']['rho'], 3 / (2 * sp.pi**4))
    chk("1/(u-i0)^8 = (1/7!) INT w^7 e^{-iwu}: the integral times a^8 is 7!",
        r['fourier8'], sp.factorial(7))
    kap, n = r['kf']['rho']
    chk("(F) mode sum: Var_0 = kappa INT s^7|fhat|^2, kappa = 1/(3360 pi^4)",
        (kap, n), (1 / (3360 * sp.pi**4), 7))
    chk("CONTROL (P) and (F) agree: c_P / 7! = kappa",
        sp.simplify(r['kp']['rho'] / sp.factorial(7) - kap), 0)
    kpd, npd = r['kf']['phidot2']
    chk("CONTROL (P) and (F) agree for phidot^2 too",
        sp.simplify(r['kp']['phidot2'] / sp.factorial(7) - kpd), 0)

    print("\n    CONTROLS AGAINST SOURCE -- FFR Table I (Lorentzian) and FFR 2D Eq. (18)")
    for w, scale, want in (('phi2', (4 * sp.pi * tau)**4, 2),
                           ('phidot2', (4 * sp.pi * tau**2)**4, sp.Rational(9, 2)),
                           ('rho', (4 * sp.pi * tau**2)**4, sp.Rational(3, 2))):
        k, nn = r['kf'][w]
        lor, gau, tt = sampler_variances(sp, k, nn)
        chk("a_2(%s) = %s" % (w, want), sp.simplify(lor.subs(tt, tau) * scale), want)
    k, nn = r['kf']['chiral']
    lor, gau, tt = sampler_variances(sp, k, nn)
    chk("2D chiral, Gaussian: G_2[f] = 1/(24 pi^2 tau^4)  [FFR 2D Eq. (18), c=1]",
        sp.simplify(gau.subs(tt, tau) * 24 * sp.pi**2 * tau**4), 1)
    k, nn = r['kf_planted']
    lor, gau, tt = sampler_variances(sp, k, nn)
    chk("  PLANTED ERROR (angular average dropped) FAILS the a_2(rho) = 3/2 test",
        sp.simplify(lor.subs(tt, tau) * (4 * sp.pi * tau**2)**4) == sp.Rational(3, 2), False)
    lor, gau, tt = sampler_variances(sp, kap, n)
    chk("Lorentzian K = 3/(512 pi^4)", sp.simplify(lor.subs(tt, 1)), 3 / (512 * sp.pi**4))
    chk("Gaussian   K = 1/(70 pi^4)", sp.simplify(gau.subs(tt, 1)), 1 / (70 * sp.pi**4))
    chk("Fewster-Eveson bound for the Lorentzian is FFR's 27/128", r['fe27'], sp.Rational(27, 128))

    print("\n    FEWSTER'S OWN SAMPLER")
    near("mu_1 from cos mu cosh mu = 1 matches achievable.FEWSTER_MU1",
         r['cl']['mu'], achievable.FEWSTER_MU1, 1e-14)
    near("Rayleigh quotient INT g''^2/INT g^2 = mu_1^4, so C = mu_1^4/16pi^2",
         r['rayleigh'] / (16 * mp.pi**2), achievable.FEWSTER_C, 1e-13)
    chk("  CONTROL: the second clamped root gives a different C (the check bites)",
        abs(float(r['rayleigh_mu2'] / (16 * mp.pi**2)) - achievable.FEWSTER_C) > 1.0, True)
    chk("H4 CONTROL: g, g' vanish at both ends to 1e-25 (clamped)", float(r['bc']) < 1e-25, True)
    chk("H4 CONTROL: g'' bounded on [0,1] (so g in W^{2,2})", float(r['g2sup']) < 1e3, True)
    near("K_F: route P (position PV, 25 dps) = route F (Fourier, double), tol 1e-11",
         r['K_P'], r['K_F'], 1e-11)
    chk("  CONTROL: route F truncated at U = 200 without its tail disagrees",
        abs(K_fourier(200.0)[0] - r['F4']**2 / 200.0**2 / (3360 * math.pi**4) - r['K_F'])
        > 1e-11 * r['K_F'], True)
    chk("F4 = F''''(0) = F''''(1) (the mode is symmetric; route F's tail uses it)",
        abs(float(_Fn(r['cl']['S'], 4, 0, mp) - _Fn(r['cl']['S'], 4, 1, mp)))
        < 1e-15 * float(_Fn(r['cl']['S'], 4, 0, mp)), True)
    near("FIXTURE K_F_FIXTURE reproduced by route P", r['K_P'], K_F_FIXTURE, 1e-14)

    print("\n    THE CORRIDOR (flat figures; application is a SURVEY)")
    c = r['cor']
    near("SD_0/(C/tau^4) = sqrt(K_F)/C, a shape number", c['sd_over_Q'],
         math.sqrt(float(r['K_P'])) / achievable.FEWSTER_C, 1e-12)
    near("FIXTURE-DERIVED SD0_OVER_C reproduced by corridor()", c['sd_over_Q'], SD0_OVER_C, 1e-12)
    chk("  and it is the same at b = 1 m and b = 1 light-year",
        abs(corridor(float(r['K_P']), 9.4607e15)['sd_over_Q'] / c['sd_over_Q'] - 1) < 1e-12, True)
    near("RECORD: demand at b = 1 m, achievable.required_density(1)", c['D'],
         1.8057952075209083e46, 1e-12)
    near("RECORD: C/tau^4 at tau = b/c, achievable.persistence_allow(1)", c['Q'],
         1.002159073400914e-25, 1e-12)
    within("CONTROL: log10(D/SD_0) = log10(D/Q) - log10(SD0/C) (abs, 1e-12)",
           abs(c['orders_sd'] - (c['orders_Q'] - math.log10(c['sd_over_Q']))), PIN_TOL)

    print("\n(b) T1 UNDER SMEARING")
    th = r['th']
    u, g = r['u'], r['g_sym']
    chk("thermal g(0) = pi^2/30 = rho (Stefan-Boltzmann, beta = 1)",
        sp.simplify(sp.limit(g, u, 0) - sp.pi**2 / 30), 0)
    chk("thermal g ~ -3/(2 pi^2 u^4) at large u", sp.limit(g * u**4, u, sp.oo), -3 / (2 * sp.pi**2))
    mp.mp.dps = 20
    uu = mp.mpf('0.7')
    direct = mp.quad(lambda k: k**3 * mp.cos(k * uu) / (mp.exp(k) - 1), [0, mp.inf]) / (2 * mp.pi**2)
    near("CONTROL: closed-form g(0.7) = its defining mode integral", r['gf'](uu), direct, 1e-15)
    L, beta = sp.symbols('L beta', positive=True)
    thm = fluctuation.image_stress(sp, lambda k: (sp.I * k * beta, 0))
    chk("fluctuation.py's pointwise thermal Delta' is 2/3 (imported)", thm['Dprime'], sp.Rational(2, 3))
    near("  and the smeared Delta'_f tends to it: tau = 0.01 beta", th[0]['dprime'],
         thm['Dprime'], 3e-3)
    chk("  converging: the gap to 2/3 shrinks > 50x from tau = 0.1 to 0.01",
        abs(th[0]['dprime'] - mp.mpf(2) / 3) * 50 < abs(th[1]['dprime'] - mp.mpf(2) / 3), True)
    chk("FIXTURE TAU_STAR_OVER_BETA = dprime_crossing rounded to 6 digits",
        round(float(r['tau_star']), 6), TAU_STAR_OVER_BETA)
    ga, gb = r['g2']
    chk("||g^2||_1 = 180 (zeta6 - zeta7)/pi^3, series = closed form", sp.simplify(ga - gb), 0)
    chk("(S_0*S_g)(0) = 720 zeta(7)/(4 pi^2), derived by the series",
        sp.simplify(cross_at_zero_exact(sp) - 720 * sp.zeta(7) / (4 * sp.pi**2)), 0)
    chk("CONTROL: the position-space PV machinery gives the mode sum's Gaussian Var_0",
        r['vac_pv'], 1)
    near("CONTROL: Y by position space = Y by spectral convolution (tau = beta)",
         th[2]['Y'], th[2]['Y_f'], 1e-8)
    near("CONTROL: X by position-space PV = X by spectral convolution (tau = beta)",
         th[2]['X'], th[2]['X_f'], 1e-8)
    coef, z6 = r['hconst']
    chk("Hoelder coefficient DERIVED: (2/3)(900/pi^4)(180/pi^3) -> 108000", coef, 108000)
    chk("zeta(6) = pi^6/945, DERIVED", z6, sp.Rational(1, 945))
    near("CONTROL: the sympy Hoelder bound at tau = beta = the mpmath row's",
         (coef * (sp.zeta(6) - sp.zeta(7)) / (sp.sqrt(2 * sp.pi) * sp.pi**7)).evalf(25),
         th[2]['hoelder'], 1e-15)
    chk("Delta'_f <= Hoelder bound at every tau measured",
        all(row['dprime'] <= row['hoelder'] for row in th), True)
    chk("Delta'_f < 1/2 at tau = beta (MEASURED)", th[2]['dprime'] < 0.5, True)
    chk("THEOREM: z3 proves the Hoelder bound < 1/2 at tau = beta", r['hoelder1'][0], True)
    chk("VACUITY GUARD: the proof's hypotheses are satisfiable", r['hoelder1'][1], True)
    chk("VACUITY GUARD: the same z3 query at tau = beta/10 is not provable",
        r['hoelder01'][0], False)
    chk("CONTROL: coefficient x10 makes the z3 proof fail",
        hoelder_bound_proof(z3, 1, coef * 10, z6)[0], False)
    chk("ILLUSTRATION rank 4: 2||K||^2 >= (1/2)(tr K)^2 (finite matrices; T1's case)",
        r['rank4'][0], True)
    chk("ILLUSTRATION rank 8: the 1/2 floor fails (z3 finds K)", r['rank8_half'], (False, True))
    chk("ILLUSTRATION rank 8: 1/4 = 2/8 holds (finite matrices only)", r['rank8_quarter'][0], True)
    chk("T1 as fluctuation.py proves it still holds pointwise",
        fluctuation.theorems(z3)['T1'], True)
    chk("the FULL noise-kernel relative fluctuation is > 1 at tau = beta (shot noise)",
        th[2]['full_rel'] > 1, True)
    chk("  and < 1/2 at tau = 100 beta", th[4]['full_rel'] < 0.5, True)
    chk("  and it FALLS monotonically over the five tau measured",
        all(th[i]['full_rel'] > th[i + 1]['full_rel'] for i in range(4)), True)
    near("  tau R^2 at tau = 100 beta matches its large-tau law L (tol 2e-5)",
         th[4]['tau'] * th[4]['full_rel']**2, r['L'], 2e-5)
    chk("  crossing of 1/2 lies between 10 and 100 beta",
        10 < r['full_cross'] < 100, True)
    chk("  cross term X >= 0 (spectral densities are positive)",
        all(row['X'] >= 0 for row in th), True)
    chk("CONTROL: T1_SURVIVES_SMEARING agrees with the z3 proof and the measurement",
        T1_SURVIVES_SMEARING, not (r['hoelder1'][0] and r['hoelder1'][1] and th[2]['dprime'] < 0.5))

    print("\n(c) THE DECISION -- C1 IN THE FLAT MODEL, SURVEY ON THE CORRIDOR")
    chk("CONTROL: -demand lies below the spectrum's floor -C/tau^4", -c['D'] < -c['Q'], True)
    chk("RECORD (THEOREM consequence under H6, not a figure): outcome probability",
        c['prob_outcome_at_demand_H6'].startswith("0 -- THEOREM"), True)
    chk("RECORD: C1_FLAT_THEOREM, CORRIDOR_APPLICATION, CURVED_PART_CARRIED_BY",
        (C1_FLAT_THEOREM, CORRIDOR_APPLICATION, CURVED_PART_CARRIED_BY), (True, "SURVEY", "O2"))
    chk("RECORD: DECIDES_D22 withdrawn and kept in WITHDRAWN",
        (DECIDES_D22, "DECIDES_D22 = True" in WITHDRAWN), (False, True))
    chk("every hypothesis H1-H6 is named with a check status",
        sorted(HYPOTHESES) == ["H%d" % i for i in range(1, 7)]
        and all(len(v) == 2 and v[1] for v in HYPOTHESES.values()), True)
    within("CORRIDOR PIN: log10(D/Q) from corridor() = log10(persistence_shortfall(1))",
           corridor_pins(c)['dq'], PIN_TOL)
    within("CORRIDOR PIN: short1 = log10(D/Q) + k log10(l_G/b), k read off achievable",
           corridor_pins(c)['law1'], PIN_TOL)
    within("CORRIDOR PIN: short1 - short01 = k", corridor_pins(c)['step'], PIN_TOL)
    within("CORRIDOR PIN: short(eps) = log10(D / persistence_allow(eps l_G))",
           corridor_pins(c)['direct'], PIN_TOL)
    within("  the exponent k read off achievable's duration bound is 4",
           abs(shortening_exponent() - 4), PIN_TOL)
    bad = corridor_pins(corridor(float(r['K_P']), 1.0, _shorten_exponent=3))
    chk("  CONTROL: the exponent-3 break (verify-fluct) turns law1, step, direct red",
        (bad['law1'] > PIN_TOL, bad['step'] > PIN_TOL, bad['direct'] > PIN_TOL),
        (True, True, True))
    chk("RECORD PIN (READ from achievable, not re-derived): 71.256 at the hold time",
        round(math.log10(achievable.persistence_shortfall(1.0)), 3), 71.256)
    within("B_OVER_LG_SQUARED (computed at import) = corridor()'s (b/l_G)^2 (rel)",
           abs(c['b_over_lG']**2 / B_OVER_LG_SQUARED - 1), 1e-12)
    e, free, (ms, as_, bs) = b_over_lG_symbolic(sp)
    chk("DERIVED: (b/l_G)^2 from achievable.required_density on symbols is free of b",
        bs in free, False)
    within("  and equals 6 m/a^3 (float pi and SI constants; rel)",
           abs(float(sp.simplify(e * as_**3 / ms)) / 6 - 1), 1e-12)
    chk("  and 6 (M/b)/(a/b)^3 at achievable's window is 3750",
        round(B_OVER_LG_SQUARED, 6), 3750.0)
    within("  and b/l_G is the same at b = 1 km (D ~ 1/b^2; rel)",
           abs(corridor(float(r['K_P']), 1e3)['b_over_lG'] / c['b_over_lG'] - 1), 1e-12)
    chk("CONTROL: H2_SATISFIED_BY_CORRIDOR agrees with the computed b/l_G < 1",
        H2_SATISFIED_BY_CORRIDOR, c['b_over_lG'] < 1.0)
    chk("  and H2 fails there", H2_SATISFIED_BY_CORRIDOR, False)

    print("\n    THE EINSTEIN-LANGEVIN SURROGATE (not H6)")
    z, lnp = r['el']
    within("CONTROL: log10(-ln P) by mpmath erfc = the stdlib Mills form (abs)",
           abs(float(lnp) - el_vacuum_log10_neg_ln_p(float(r['K_P']))), 1e-9)
    within("  and = EL_VACUUM_LOG10_NEG_LN_P (import-time, from the K_F fixture)",
           abs(float(lnp) - EL_VACUUM_LOG10_NEG_LN_P), 1e-9)
    within("  and log10 z = log10(D/SD_0) from corridor()",
           abs(float(mp.log10(z)) - c['orders_sd']), 1e-9)
    chk("P < exp(-10^141): computed", EL_VACUUM_BELOW_EXP_MINUS_10_141, True)
    chk("P < exp(-10^142) is FALSE: the ruling's typed bound is CORRECTED",
        (EL_VACUUM_BELOW_EXP_MINUS_10_142, float(lnp) < 142.0), (False, True))
    chk("  and the correction is recorded", any("exp(-10^142)" in k for k in CORRECTED), True)

    print("\n    REFUSALS AND RECORDS")
    chk("RECORD: the distribution restatement changes no requirement (flat model)",
        DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT, False)
    chk("CONTROL: ... and C1 applies: the demand exceeds the flat floor",
        DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT, not (c['D'] > c['Q']))
    chk("CONTROL: the curved variance is NOT computed, and the corridor's mode "
        "functions are NOT-FOUND", (CURVED_VARIANCE_COMPUTED,
                                     fewsterteo.CORRIDOR_MODE_FUNCTIONS.startswith("NOT-FOUND")),
        (False, True))
    chk("RECORD: no NEW renormalisation; finiteness NAMED, not run",
        (CURVED_VARIANCE_NEEDS_QUARTIC_RENORMALISATION,
         CURVED_VARIANCE_FINITENESS.startswith("NAMED, NOT RUN")), (False, True))
    chk("RECORD: Kuo-Ford <:A^2:> needs a reference state in curved space; Var does not",
        (KUO_FORD_NORMAL_ORDERING_NEEDS_REFERENCE_STATE_IN_CURVED_SPACE,
         VARIANCE_NEEDS_REFERENCE_STATE), (True, False))
    chk("RECORD: admissible-negative-mean fluctuation NOT computed",
        ADMISSIBLE_NEGATIVE_MEAN_FLUCTUATION_COMPUTED, False)
    chk("RECORD: the EL surrogate for non-vacuum states NOT computed",
        EL_SURROGATE_NONVACUUM_COMPUTED, False)
    chk("RECORD: no row is opened", ROW_TO_OPEN, None)
    chk("RECORD: the curved price is NOT claimed", PRICES_THE_CORRIDOR_CURVED, False)
    chk("RECORD: gr-qc/0307032 is NAMED-NOT-READ", SOURCES["gr-qc/0307032"][1], "NAMED-NOT-READ")
    chk("RECORD: Fewster Sec. 5.1 nonminimal, Sec. 5.2 interacting (cited as such)",
        "Sec. 5.1 nonminimal coupling, Sec. 5.2 interacting fields" in SOURCES["1208.5399"][1], True)

    print()
    if fails:
        print("  SELFTEST FAILED: %d" % len(fails))
        for f in fails:
            print("    %s: got %r want %r" % f)
        return 1
    print("  SELFTEST OK")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
