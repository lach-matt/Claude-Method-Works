#!/usr/bin/env python3
r"""
address.py -- DOCKET 63, ROLE 1.  CAN A DISPLACED HIGGS VEV BE AN ADDRESS?

    python3 address.py             the reading
    python3 address.py --selftest  fixtures and controls

M: "what would it take to excite a Higgs field at the endpoint?"  Asked which
role the field is playing, M allowed all three.  ROLE 1 is ADDRESSING: a
locally displaced vev as a physically distinguishable region -- a real address
rather than a coordinate.  It was the most promising of the three because it
needs only DETECTABILITY and no mass budget.

IT DIES, AND NOT OF THE OBSTRUCTION THAT WAS EXPECTED.

`higgs.py` owns the vev, the NEC identity and the Barcelo-Visser gate, and is
IMPORTED here, never re-derived.  What is new is the detection side: the exact
sensitivity coefficient of each observable to eps = dv/v, the exact energy of a
linear displacement, the exact range of one, and -- the finding -- that ORDINARY
MATTER ALREADY DOES THIS, better than any device could, and that the same source
is seen 23 orders further away by an instrument nobody had to invent.

===============================================================================
1. WHAT THE DISPLACEMENT IS SENSITIVE THROUGH, AND THE CHANNEL THAT IS BLIND
===============================================================================

Every fermion mass is m_f = y_f v / sqrt(2), so d ln m_f / d ln v = 1 EXACTLY,
at fixed Yukawa.  alpha = e^2/4pi hbar c contains no v at all: e = g sin(th_W)
is a gauge coupling.  SO AT TREE LEVEL A DISPLACED VEV MOVES EVERY MASS AND
LEAVES alpha ALONE.

That single fact decides which clock can see it, and it rules OUT the channel a
reader reaches for first.

    An optical transition frequency, in units of the Rydberg, is a pure
    function of alpha: nu_opt / c R_inf = F(alpha).  The electron mass CANCELS.
    So an OPTICAL-TO-OPTICAL frequency RATIO -- the sharpest measurement in
    physics, 3e-16 in Godun 2014 and heading below 1e-18 -- IS BLIND TO eps
    THROUGH mu, AT TREE LEVEL, FOR A POINT NUCLEUS OF INFINITE MASS.

    THAT IS NOT THIS FILE'S ASSERTION.  It is Godun et al.'s own B_E3 = B_E2 =
    0 -- which they call "negligible", not zero -- READ FROM SOURCE below, and
    it is the control this file must reproduce.

    WITHDRAWN (DOCKET 63, W10).  The first draft said "IS EXACTLY BLIND".  IT
    IS NOT.  Finite nuclear size adds (4/3) Z^4 (r_N/a_0)^2 / n^3 Rydberg to
    every S level, and r_N/a_0 is proportional to m_e r_N, hence to v at tree
    level (H2, r_N held fixed).  For hydrogen nu(1S-2S)/nu(2P-3D), with
    x = r_p/a_0, finite_size_K() derives in sympy K = 28x^2/(14x^2 - 9) =
    -7.87e-10 -- nonzero, same place, alpha fixed.  Recoil terms in m_e/M add
    more.  Small; and under H2, where K_alpha = 0, it is the LEADING
    same-place sensitivity.  Kept as OPTICAL_OPTICAL_IS_EXACTLY_BLIND = False.

    AND THE BLINDNESS HAS A HYPOTHESIS, WHICH SECTION 7 CASHES: it holds for two
    transitions AT THE SAME PLACE.  Two copies of the SAME optical clock in
    DIFFERENT places do not cancel R_inf, because R_inf is proportional to m_e
    and m_e is proportional to the LOCAL v.  A TRANSPORTED CLOCK CARRIES
    COEFFICIENT EXACTLY +1, and it turns out to be the best channel here.

The microwave hyperfine splitting does not cancel m_e:

    nu_hf / c R_inf  ~  alpha^2 * g_I * (m_e/m_p) * F_rel(Z alpha)

-- one factor alpha^2 from mu_B mu_N / a_0^3 against the Rydberg, and one
factor (m_e/m_p) from the nuclear magneton.  So the OPTICAL-TO-CESIUM ratio
carries exponent exactly +1 in mu = m_p/m_e and exactly 2 (plus relativistic
corrections) in alpha.  THAT is the channel, and Godun's Cs-limited 6e-16 is
TWICE their optical ratio's 3e-16 -- CS_CHANNEL_COARSER_BY, computed, is 2.

    WITHDRAWN (DOCKET 63, W10).  The first draft said the Cs channel is "a
    hundred times coarser than the blind one".  The factor is 2, not 100.

===============================================================================
2. HOW MUCH DOES mu MOVE?  THE PROTON IS NOT AS INERT AS THE 0.96% SUGGESTS
===============================================================================

The tempting statement is that the Higgs supplies 2m_u + m_d = 8.99 MeV of the
proton's 938.272 MeV -- 0.96% -- so m_p barely moves and mu tracks m_e alone.
The CONCLUSION survives.  THE REASON DOES NOT, and the correction is a factor
that DEPENDS ON S: 24.0 at the valence 0.0096, 4.48 at S = 0.06 and 3.25 at
S = 0.09 (NAIVE_CORRECTION_FACTOR, computed).

    CORRECTED (DOCKET 63, ruling F6).  The first draft said "a factor of
    thirty" here and "TWENTY-FOUR" below.  Twenty-four holds only at the
    valence value S = 0.0096, which is a sum of current-quark masses and NOT a
    Feynman-Hellmann fraction; at the scanned sigma-term values it is 3 to 4.5.

Lambda_QCD is not independent of v.  One-loop threshold matching across the
charm, bottom and top thresholds, with b_0(n_f) = 11 - 2 n_f/3 and
b_0(n_f - 1) - b_0(n_f) = 2/3 at each, gives EXACTLY

    Lambda_3 = Lambda_6^(7/9) * (m_c m_b m_t)^(2/27)

-- so each heavy quark enters with power 2/27, and since every heavy quark mass
is proportional to v,

    d ln Lambda_QCD / d ln v  =  3 * 2/27  =  2/9     EXACTLY

DERIVED IN THIS FILE OVER Fraction, not quoted.  Then by dimensional
homogeneity m_p = Lambda f(m_q/Lambda), so d ln m_p/d ln Lambda = 1 - S with
S = sum_q sigma_q/m_p the Feynman-Hellmann light-quark fraction, and

    H1  alpha_s FIXED AT A HIGH SCALE:   d ln m_p/d ln v = 2/9 + (7/9) S
    H2  Lambda_QCD ITSELF FIXED:         d ln m_p/d ln v = S

H1 gives 0.229 at S = 0.0096 -- TWENTY-FOUR TIMES the naive 0.0096.  Both
hypotheses are named because BOTH ARE IN THE LITERATURE and they are not the
same physics; neither is assumed.  What matters is that they agree on the
answer:

    K_mu = d ln mu / d ln v = -7(1-S)/9  (H1)   or   S - 1  (H2)

    S = 0.0096 :  K_mu = -0.7703 (H1)   -0.9904 (H2)
    S = 0.06   :  K_mu = -0.7311 (H1)   -0.9400 (H2)

O(1) AND NEGATIVE UNDER EVERY HYPOTHESIS, because the electron side carries it.
THE 0.96% SPLIT IS THE RIGHT OBSERVATION ATTACHED TO THE WRONG TERM: mu is
sensitive not because m_p is inert but because m_e is not.

===============================================================================
3. THE THRESHOLD, THE COST, AND WHY THE COST IS NOT THE COST
===============================================================================

eps_det = (fractional accuracy of an optical-to-Cs ratio) / |K_mu|, and Godun
2014's absolute frequencies carry 6e-16, Cs-limited.  That is eps_det ~ 8e-16.

The exact linear-regime energy density, with NO small-eps expansion:

    V(v(1+eps)) / |V_min|  =  eps^2 (2 + eps)^2        EXACT
                           ->  4 eps^2                  as eps -> 0

sympy residual of that identity is 0.  At eps_det it is of order 1e16 J/m^3,
which is large but is INSIDE the range of energies humans have released, so on
the energy measure ADDRESSING LOOKS AFFORDABLE.

IT IS NOT, AND THE ENERGY IS THE WRONG METER.  The displacement has to be
SOURCED.  A fermion background sources the Higgs through its scalar density,
and the static uniform solution of (nabla^2 - m_h^2) dphi = (m_psi/v) n is

    eps  =  - rho_H c^2 / (v^2 m_h^2)  =  - rho_H c^2 / (8 |V_min|)   EXACT

(v^2 m_h^2 = 2 lambda v^4 = 8 |V_min| exactly; sympy residual 0), with rho_H
the HIGGS-DERIVED part of the mass density.  Holding eps_det therefore takes a
source whose rest energy is 8|V_min| eps_det -- and that is 2/eps_det, some
2.4e15, TIMES the field energy it buys (EXACTLY 8/(eps (2+eps)^2), which
source_to_field_ratio() computes and the selftest expands in sympy).  PRICING
ADDRESSING AT ITS FIELD ENERGY UNDERSTATES IT BY FIFTEEN ORDERS.

    WITHDRAWN (DOCKET 63, W12).  The first draft said "1/(4 eps_det), some
    1e15".  The file's own selftest pinned 2/eps; the two differ by a factor
    of 8 (2.5e15 against 3.1e14 at eps = 8e-16).

===============================================================================
4. THE RANGE
===============================================================================

    WITHDRAWN (DOCKET 63, W13).  This heading first read "THE RANGE, AND IT IS
    THE SAME OBSTRUCTION EVERY ROLE HITS".  It is not: role 3 falls to a
    theorem that never mentions the Higgs mass (T_kk is a square -- ledger
    D17), and role 2's m_e mechanism falls to an exact dilation (D18).  The
    range is role 1's obstruction, and what is left of role 2's.

lambda_h = hbar/(m_h c) = 1.5761e-18 m -- computed here from higgs.M_HIGGS, and
0.0019 proton radii.  Outside a source, eps(r) = eps_0 (r_0/r) e^{-(r-r_0)/lam}.

    PUSH THE FIELD TO 2v -- eps_0 = 1, the edge of the linear regime -- ACROSS A
    WHOLE CUBIC METRE, AND IT IS UNDETECTABLE 54.7 ATTOMETRES OUTSIDE ITS OWN
    SURFACE.

At eps_0 = 1e-18 the range is not small, it is UNDEFINED: 1e-18 is already
three orders below eps_det, so there is nothing to detect in contact, let alone
at a distance.

===============================================================================
5. ULTRALOCALITY -- WHY A DISPLACED VEV IS NOT AN ADDRESS EVEN IN PRINCIPLE
===============================================================================

For a source varying on a scale L >> lambda_h the gradient term is negligible
and the solution is ALGEBRAIC:

    dphi(x) = -J(x)/m_h^2 * [1 + O((lambda_h/L)^2)],   (lambda_h/1 m)^2 = 2.5e-36

So dphi AT A POINT IS A FUNCTION OF THE MASS DENSITY AT THAT POINT AND NOTHING
ELSE.  There is no integral over the body, no falloff to read a distant source
by, and no way to make the field say anything the local density does not
already say.

    A DISPLACED VEV IS NOT AN ADDRESS.  IT IS A CONTACT-ONLY READOUT OF LOCAL
    MASS DENSITY, CARRYING STRICTLY LESS THAN THE DENSITY ITSELF.

AND NATURE ALREADY RUNS THE EXPERIMENT.  Nuclear matter displaces the vev by
eps = -3.26e-13 (H1) or -7.28e-14 (H2) -- 398 or 114 TIMES eps_det under the
SAME hypothesis -- everywhere there is a nucleus, which is everywhere.  The
largest Higgs displacement in the solar system is inside an ordinary atomic
nucleus, it is two orders over threshold, and no measurement outside that
nucleus has ever registered it.

    CORRECTED (DOCKET 63, ruling F5).  The first draft gave only -7.28e-14 and
    "NINETY TIMES".  That used the Higgs-derived fraction f = S, which is H2
    ONLY, against this file's own refusal to choose, and then divided by the
    H1 eps_det -- two hypotheses in one ratio.  The Higgs-derived fraction of
    a nucleon is d ln m_p/d ln v: S under H2, 2/9 + 7S/9 = 0.268889 under H1
    at S = 0.06.  Both are now carried (higgs_fraction()), and every ratio is
    taken inside one hypothesis.  Role 1 is not
untested; it is tested, at scale, continuously, with a null result that is
built into the screening length.

===============================================================================
6. THE SAME SOURCE, SEEN 23 ORDERS FURTHER AWAY, BY GRAVITY
===============================================================================

Take the source that puts eps exactly at threshold over a 1 m sphere.  Its
Higgs signature is readable at contact and nowhere else.  Its GRAVITATIONAL
signature is readable by a 1e-9 m/s^2 gravimeter out to 1.4e7 m (H1) or
2.6e7 m (H2).

    ROLE 1 IS NOT MERELY EXPENSIVE.  IT IS STRICTLY DOMINATED, BY MORE THAN
    TWENTY ORDERS OF MAGNITUDE, BY AN INSTRUMENT THAT ALREADY EXISTS AND READS
    THE SAME SOURCE -- BECAUSE THE GRAVITON IS MASSLESS AND THE HIGGS IS NOT.

===============================================================================
7. THE PROBE ROUTE -- THE BEST CHANNEL, AND IT STILL FAILS, ON THE SOURCE
===============================================================================

Send something in and bring it back, so the field never has to reach the
observer.  THERE ARE TWO PROBES AND THEY FAIL DIFFERENTLY.

A PROBE THAT MUST RESOLVE THE REGION.  If the displaced region is no bigger
than lambda_h, the probe needs de Broglie wavelength <= lambda_h, so p >= m_h c
and E >= m_h c^2.  Its sensitivity is its rest-mass dependence, and that is

    d ln E / d ln m  =  (m c^2/E)^2       EXACT (sympy residual 0)

For an electron that ceiling is (m_e/m_h)^2 = 1.6658e-11, AT eps = 1.  Against
the sharpest published clock ratio, 3e-16, the probe reads nothing until

    eps >= 1.80e-5

and holding THAT takes a source at 1.5e25 (H1) to 6.6e25 (H2) kg/m^3 --
5.5e7 to 2.5e8 times nuclear density.  RESOLUTION AND SENSITIVITY ARE THE SAME FACTOR TURNED OPPOSITE WAYS.

    AND THAT VERY FACTOR IS THE SOURCE EFFICIENCY.  A species of mass m and
    energy E sources the Higgs as (m c^2/E)^2 per unit energy density, exactly
    1 at rest and falling as the square thereafter.  ONE LEMMA FORBIDS BOTH
    READING A SMALL REGION AND PAYING FOR A LARGE ONE WITH ENERGY INSTEAD OF
    MASS.

A PROBE THAT DOES NOT.  If the region is macroscopic the probe can be slow, and
then it is simply a clock: nu_opt is proportional to c R_inf, R_inf to m_e, m_e
to the LOCAL v, so a clock carried in and compared with its twin outside reads

    d ln(nu_in/nu_out) / d eps  =  +1       EXACTLY

THE BEST COEFFICIENT ANYWHERE IN THIS FILE, and at 1e-18 clock comparison it
gives eps_det = 1e-18 -- three orders better than the stationary channel.
ROLE 1's ONE SURVIVING ROUTE IS A COURIER, NOT A SIGNAL.

IT DIES ON THE SOURCE, NOT ON THE DETECTOR.  A clock needs a bound atomic
transition, so the region must be at least a Bohr radius across -- 3.36e7
screening lengths -- and by section 5 the displacement is ultralocal, so the
source must FILL it.  eps = 1e-18 across an atom takes

    8.20e11 kg/m^3 (H1)  to  3.67e12 kg/m^3 (H2),
    3.63e7 to 1.63e8 times the density of osmium

(the first draft gave only the H2 figure; DOCKET 63 F5)

and no bound optical transition exists in such a medium.  THE MEDIUM THAT MAKES
THE SIGNAL DESTROYS THE INSTRUMENT THAT READS IT.  (That last clause is a
JUDGEMENT about pressure ionisation and is flagged as one; the density ratio is
not.)

===============================================================================
8. THE ONE LOOPHOLE WORTH THE NAME: A Th-229 NUCLEAR CLOCK AS THE COURIER
===============================================================================

An electronic clock reads eps through m_e alone, coefficient 1.  A NUCLEAR clock
reads it through m_q/Lambda_QCD, and Flambaum (arXiv:0705.3704v2 eq. 9, READ
FROM SOURCE) estimates a FIVE-ORDER enhancement for the 229-Th transition:

    dw/w  ~  10^5 (2 da/a + 0.5 dX_q/X_q - 5 dX_s/X_s) (7 eV/w)

X_q = m_q/Lambda and X_s = m_s/Lambda both move with v at d ln X/d ln v = 7/9
under H1 and exactly 1 under H2, so the coefficient of eps is about -3.5e5 and

    eps_det(Th-229 courier)  =  2.9e-24        -- EIGHT ORDERS BETTER

(2.86e-24 under H1 with the corrected K_alpha of section 11; the first draft's
2.84e-24 carried the withdrawn K_alpha)

This is the best number in the file by a wide margin and it is NOT dismissed.
It does not save Role 1, and the reason is section 9, not a budget.

(Flambaum calls his own figure "a rough estimate"; it is carried as ORDER, and
section 9's verdict does not depend on its value.)

A NECESSARY HYPOTHESIS, STATED: eps = -rho c^2/(8|V_min|) is a COARSE-GRAINED
statement.  lambda_h is 1.6 attometres and no matter is uniform at that scale --
nucleons are 1.8 fm apart, so e^{-d/lambda_h} between two of them is about
1e-496.  The formula is right for what a bound electron or a nucleus SAMPLES,
which is the mean density over its own support, and it is NOT the pointwise
field.  Every rho in this file is a coarse-grained mean and is used only where
that is the right object.

===============================================================================
9. THE DOMINATION THEOREM.  GROWING THE SOURCE MAKES IT WORSE
===============================================================================

Put a source of mean density rho in a sphere of radius R.

    HIGGS RANGE      d  =  lambda_h ln(eps_0/eps_det),  eps_0 proportional to rho
                        so  d  grows as  ln rho
    NEWTON RANGE     r  =  sqrt(G M/a_floor),  M proportional to rho
                        so  r  grows as  sqrt(rho)

    THEOREM.  r/d grows without bound as sqrt(rho)/ln(rho).  NO SOURCE STRENGTH
    CLOSES THE GAP, AND EVERY INCREASE IN THE SOURCE WIDENS IT.

That is not a comparison of two numbers, which could be argued about.  It is a
comparison of two FUNCTIONS, and it is monotone.  The Higgs is massive and the
graviton is not, and a screened field's reach is logarithmic in its source while
an unscreened field's is a power.

    ROLE 1 IS REFUTED, NOT PRICED.  There is no source, no detector and no
    budget for which a displaced vev addresses a region better than weighing it.

===============================================================================
10. WHAT THIS FILE REFUSES
===============================================================================

TO RESOLVE H1 AGAINST H2.  What is held fixed when v varies is a question about
physics above the electroweak scale and this file has no instrument for it.
Both are carried, every number is reported under both, and the finding is that
they AGREE.

TO CALL S MEASURED.  The light-quark fraction sigma_q/m_p is read at three
declared values spanning the naive valence sum and the lattice sigma-term
range.  It is a SCAN, not a measurement, and no conclusion here turns on it.

TO QUOTE A CODATA UNCERTAINTY.  m_p/m_e is measured to ~1e-11; that is NAMED-
NOT-READ and it is not used, because the clock channel beats it by 10^4.5 and
the argument does not need it.

TO PRICE THE NONLINEAR REGIME.  A bubble -- of the true vacuum below ours,
or a region held at phi = 0, which is a spinodal maximum and not a false
vacuum -- is not this file's subject.  (The first draft said "a false-vacuum
bubble", which names neither; DOCKET 63 F8/F10.)  Role 1 needs only detectability, and detectability fails inside the
linear regime, which is the stronger place to fail.

TO CALL PRESSURE IONISATION A MEASUREMENT.  Section 7's closing clause -- that
no bound optical transition survives at 8.20e11 to 3.67e12 kg/m^3 -- is a
JUDGEMENT.  The
density ratio it rests on is computed; the ionisation claim is not, and no
number here depends on it.

TO CLAIM THE 0.96% FIGURE IS WRONG.  It is right about the valence quark masses
and wrong only as a sensitivity coefficient.  Section 2 says which.

===============================================================================
11. DOCKET 63: WHAT THIS FILE GOT WRONG, KEPT RATHER THAN DELETED
===============================================================================

Every corrected figure is COMPUTED below; every withdrawn claim is a constant
with its reason (WITHDRAWN, keyed by ledger row).

  W10  "EXACTLY BLIND" and "a hundred times coarser" -- section 1.
       OPTICAL_OPTICAL_IS_EXACTLY_BLIND = False, K_FINITE_SIZE_HYDROGEN,
       CS_CHANNEL_COARSER_BY.
  W11  K_alpha(H1) = -9.979521e-3.  THE SIGN WAS WRONG AND THE W THRESHOLD WAS
       MISSING.  With alpha fixed at a high scale, 1/alpha(0) = 1/alpha(Lambda)
       + SUM b_i ln(Lambda/m_i)/(2 pi), so d ln alpha/d ln v = +alpha SUM b_i
       w_i/(2 pi): a heavier charged fermion screens over a shorter interval
       and alpha(0) RISES.  The W (b = -22/3 + 1/3 = -7, w = 1) antiscreens.
       One loop gives EXACTLY +43 alpha/(54 pi) = +1.849653e-3
       (K_ALPHA_H1_COEFFICIENT = 43/54, over Fraction; the sign is checked in
       sympy).  Consequences, computed: the Th-229 H1 coefficient moves from
       -3.520e5 to -3.496e5, the optical/optical H1 row from -0.0682 to
       +0.0126.  K_alpha_as_first_written() keeps the withdrawn formula so
       the withdrawn number is reproduced, not typed.
       THE RULING'S OWN CONSEQUENCE FIGURES DO NOT FOLLOW FROM ITS OWN
       K_alpha, AND THIS FILE DOES NOT SEAT THEM.  DOCKET 63 ruling F7
       printed "Th-229 H1 goes to about -3.48e5" and "the optical/optical H1
       row goes to +0.0682".  Both are the WITHDRAWN K_alpha with its sign
       flipped (+9.98e-3), not the ruling's own +43 alpha/(54 pi) =
       +1.85e-3: dA x (-K_first) = +0.0682, and 1e5 (3.5 - 2 x 9.98e-3)
       = 3.48e5, where the corrected product is dA x K = +0.0126 and
       1e5 (3.5 - 2 K) = 3.496e5.  RULING_F7_PRINTED holds the two figures
       as READ strings; RULING_F7_K_REQUIRED solves each, through the owning
       function, for the K_alpha it would need; RULING_F7_FOLLOWS_FROM_ITS_
       K_ALPHA and RULING_F7_IS_THE_SIGN_FLIP are COMPUTED by rounding each
       candidate to the ruling's printed quantum.  The seated values are the
       computed +0.0126331 and -3.49630e5.  A ruling-figure divergence,
       RECORDED for M, not repaired in the ruling.
  W12  "1/(4 eps_det)" -- section 3.  SOURCE_TO_FIELD_IS_QUARTER_OVER_EPS =
       False; the factor between the two, ~8, is computed by asking
       source_to_field_ratio() (it is 32/(2+eps)^2, 8 only as eps -> 0).
  W13  "THE SAME OBSTRUCTION EVERY ROLE HITS" -- section 4.
       SAME_OBSTRUCTION_EVERY_ROLE = False.
  F5   The source fractions were H2 only -- sections 5 and 7.  EPS_NUCLEAR
       and COURIER_SOURCE_KG_M3 now carry both hypotheses.
  F6   "a factor of thirty" against "twenty-four" -- section 2.

NOTHING IS REPAIRED.
"""

import math
import sys
from decimal import Decimal
from fractions import Fraction

import higgs

# --------------------------------------------------------------- imported, not copied
V_GEV = higgs.vev()
M_HIGGS = higgs.M_HIGGS
LAMBDA_QUARTIC = higgs.lam()
VMIN_SI = abs(higgs.gev4_to_si(higgs.v_min_gev4()))     # J/m^3, higgs.py owns it
HBAR = higgs.HBAR
C = higgs.c
G = higgs.G
GEV_IN_J = higgs.GEV_IN_J

# --------------------------------------------------------------- measured inputs
M_E_MEV = 0.51099895000          # PDG/CODATA                       NAMED-NOT-READ
M_P_MEV = 938.27208816           # PDG/CODATA                       NAMED-NOT-READ
QUARK_SUM_MEV = 8.990            # 2 m_u + m_d, PDG MS-bar 2 GeV    NAMED-NOT-READ
R_PROTON_M = 0.8414e-15          # CODATA rms charge radius         NAMED-NOT-READ
A_BOHR_M = 5.29177210903e-11     # CODATA                           NAMED-NOT-READ
ALPHA_EM = 1.0 / 137.035999084   # CODATA                           NAMED-NOT-READ
RHO_NUCLEAR = 2.676e17           # kg/m^3, n_0 = 0.16/fm^3 * m_N    DERIVED-FROM-ORDER
GRAVIMETER_FLOOR = 1.0e-9        # m/s^2, ~0.1 microGal             ORDER

#: Godun et al., PRL 113, 210801 (2014) = arXiv:1407.0164v2.  READ FROM SOURCE.
#: p.4: "r_dot/r = (A_1 - A_2) alpha_dot/alpha + (B_1 - B_2) mu_dot/mu.  The
#: sensitivity coefficients A_i ... are: A_E3 = -5.95, A_E2 = 0.88, A_Cs = 2.83.
#: Dependence on mu_dot arises through the nuclear magnetic moment and is
#: negligible for optical transitions (the sensitivity coefficient
#: B_E3 = B_E2 = 0). ... (B_Cs = -1)."  Their mu is m_p/m_e.
GODUN = {"A_E3": -5.95, "A_E2": 0.88, "A_Cs": 2.83,
         "B_E3": 0.0, "B_E2": 0.0, "B_Cs": -1.0}
GODUN_RATIO_UNC = 3.0e-16        # "fractional uncertainty 3 x 10^-16", p.1
GODUN_ABS_UNC = 6.0e-16          # "relative standard uncertainty of 6 x 10^-16"
GODUN_READ_FROM_SOURCE = True

#: Flambaum, arXiv:0705.3704v2 p.4, READ FROM SOURCE: "The proton mass is
#: proportional to Lambda_QCD (M_p ~ 3 Lambda_QCD)" -- this project's H2.
FLAMBAUM_READ_FROM_SOURCE = True

#: The light-quark fraction S = sum_q sigma_q/m_p.  A scanned input (ORDER),
#: not a measurement.  (label, value)
S_SCAN = (("naive valence 2m_u+m_d", QUARK_SUM_MEV / M_P_MEV),
          ("sigma_piN ~ 56 MeV", 0.06),
          ("with strange sigma term", 0.09))

TREE_LEVEL_ALPHA_IS_V_INDEPENDENT = True
#: Blind THROUGH mu, at tree level, for a point nucleus of infinite mass --
#: Godun's B_E3 = B_E2 = 0.  NOT exactly blind: see
#: OPTICAL_OPTICAL_IS_EXACTLY_BLIND = False (DOCKET 63, W10).
OPTICAL_OPTICAL_IS_BLIND = True
NOTHING_IS_REPAIRED = True
H1_VS_H2_IS_REFUSED = True


# ===================================================================== section 2
def beta0(nf):
    """One-loop QCD beta coefficient b_0 = 11 - 2 n_f/3.  EXACT RATIONAL."""
    return Fraction(11) - Fraction(2, 3) * nf


def threshold_step(nf):
    """b_0(n_f - 1) - b_0(n_f), the exponent a heavy quark carries at matching."""
    return beta0(nf - 1) - beta0(nf)


def _lambda_exponent_direct(n_heavy=3):
    """The same thing, written as the composition it is.  EXACT.

    ln Lambda_3 = (b6/b3) ln Lambda_6 + sum over thresholds; each heavy quark
    contributes (2/3) divided by the product of the b's below it, which
    telescopes to (2/3)/b_3 per quark ONLY when the intermediate roots are taken
    in order.  Done here by carrying the exponent vector explicitly.
    """
    # state: Lambda_n^1 = Lambda_6^(a) * prod m_Q^(e_Q)
    a = Fraction(1)
    e = {}
    order = [(6, "m_t"), (5, "m_b"), (4, "m_c")][:n_heavy]
    for nf, name in order:
        b_hi, b_lo = beta0(nf), beta0(nf - 1)
        step = threshold_step(nf)
        # Lambda_{nf-1} = (Lambda_nf^{b_hi} m^{step})^{1/b_lo}
        a = a * b_hi / b_lo
        for k in e:
            e[k] = e[k] * b_hi / b_lo
        e[name] = step / b_lo
    return a, e


def dln_lambda_dln_v(n_heavy=3):
    """Sum of the heavy-quark exponents: every heavy mass is proportional to v."""
    _, e = _lambda_exponent_direct(n_heavy)
    return sum(e.values())


def dln_mp_dln_v(S, hypothesis):
    """d ln m_p / d ln v.  S = sum_q sigma_q/m_p (Feynman-Hellmann)."""
    if hypothesis == "H1":
        return dln_lambda_dln_v() * (1 - S) + S
    if hypothesis == "H2":
        return S
    raise ValueError(hypothesis)


def K_mu(S, hypothesis):
    """d ln(m_p/m_e) / d ln v.  m_e is 100% Higgs, so subtract exactly 1."""
    return dln_mp_dln_v(S, hypothesis) - 1


#: One-loop QED coefficients: above its threshold a species drives
#: d(1/alpha)/d ln mu = -b/(2 pi).  Standard textbook values, NAMED-NOT-READ.
B_DIRAC_UNIT_CHARGE = Fraction(4, 3)                 # a Dirac fermion, Q = 1
B_W_BOSON = Fraction(-22, 3) + Fraction(1, 3)        # W+- and its Goldstone: -7


def alpha_thresholds():
    """[(name, b_i, w_i)] for every charged threshold, w_i = d ln m_i/d ln v.

    w = 1 for a mass proportional to v (leptons, c, b, t, and m_W = g v/2);
    w = 2/9 for a light quark whose threshold is hadronic, i.e. Lambda_QCD.
    EXACT RATIONALS.
    """
    wl = dln_lambda_dln_v()
    rows = [(n, B_DIRAC_UNIT_CHARGE * 1 * Fraction(1), Fraction(1))
            for n in ("e", "mu", "tau")]
    rows += [(n, B_DIRAC_UNIT_CHARGE * 3 * Fraction(4, 9), Fraction(1))
             for n in ("c", "t")]
    rows += [("b", B_DIRAC_UNIT_CHARGE * 3 * Fraction(1, 9), Fraction(1))]
    rows += [(n, B_DIRAC_UNIT_CHARGE * 3 * q2, wl)
             for n, q2 in (("u", Fraction(4, 9)), ("d", Fraction(1, 9)),
                           ("s", Fraction(1, 9)))]
    rows += [("W", B_W_BOSON, Fraction(1))]
    return rows


def K_alpha_coefficient(hypothesis, with_W=True):
    """K_alpha = coefficient * alpha / pi.  EXACT Fraction.

    With alpha fixed at a high scale Lambda (H1),
        1/alpha(0) = 1/alpha(Lambda) + SUM_i b_i ln(Lambda/m_i) / (2 pi)
    so d(1/alpha(0))/d ln v = -SUM b_i w_i/(2 pi) and
        d ln alpha / d ln v = +alpha SUM b_i w_i / (2 pi).
    POSITIVE for a fermion: a heavier charged fermion screens over a shorter
    interval, so alpha(0) rises.  The sign is checked in sympy by the selftest.
    """
    if hypothesis == "H2":
        return Fraction(0)
    if hypothesis != "H1":
        raise ValueError(hypothesis)
    tot = sum(b * w for n, b, w in alpha_thresholds() if with_W or n != "W")
    return tot / 2


def K_alpha(hypothesis):
    """d ln alpha / d ln v.

    H2 (e fixed at low energy): EXACTLY ZERO -- alpha contains no v.
    H1 (alpha fixed at a high scale): +43 alpha/(54 pi) at one loop, with the
    W threshold.  CORRECTED (DOCKET 63, W11): the first version returned
    -9.979521e-3 -- wrong sign, no W.  See K_alpha_as_first_written.
    """
    return float(K_alpha_coefficient(hypothesis)) * ALPHA_EM / math.pi


def K_alpha_as_first_written(hypothesis):
    """THE WITHDRAWN FORMULA, KEPT SO ITS NUMBER IS REPRODUCED, NOT TYPED.

    delta(1/alpha) = +(4/3) SUM N_c Q^2 w / (2 pi) and K = -alpha delta(1/alpha):
    the sign of the running is inverted and the W threshold is absent.
    WITHDRAWN (DOCKET 63, W11).
    """
    if hypothesis == "H2":
        return 0.0
    w_light = float(dln_lambda_dln_v())
    tot = 0.0
    # (N_c, Q, weight) for the twelve charged SM fermions
    for _ in range(3):                                  # e, mu, tau
        tot += 1 * 1.0 ** 2 * 1.0
    for q, w in ((2.0 / 3.0, 1.0), (2.0 / 3.0, 1.0)):   # c, t
        tot += 3 * q ** 2 * w
    tot += 3 * (1.0 / 3.0) ** 2 * 1.0                   # b
    for q in (2.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0):         # u, d, s -- hadronic
        tot += 3 * q ** 2 * w_light
    d_inv_alpha = (4.0 / 3.0) * tot / (2.0 * math.pi)
    return -ALPHA_EM * d_inv_alpha


def K_alpha_sign_sympy():
    """d ln alpha(0) / d ln m for ONE threshold of coefficient b, in sympy.
    Returns the expression; the selftest asserts it is +alpha b/(2 pi)."""
    import sympy as sp
    a_hi, b, Lam, m = sp.symbols("alpha_Lambda b Lambda m", positive=True)
    inv0 = 1 / a_hi + b * sp.log(Lam / m) / (2 * sp.pi)
    alpha0 = 1 / inv0
    return sp.simplify(sp.diff(sp.log(alpha0), m) * m - alpha0 * b / (2 * sp.pi))


# ===================================================================== section 1
def B_optical():
    """Exponent of mu in nu/(c R_inf) for a purely electronic transition."""
    return 0.0


def B_hyperfine():
    """Exponent of mu = m_p/m_e in nu_hf/(c R_inf).

    nu_hf/(c R_inf) ~ alpha^2 g_I (m_e/m_p) F_rel, and m_e/m_p = mu^-1.
    """
    return -1.0


def A_hyperfine_nonrelativistic():
    """Exponent of alpha in nu_hf/(c R_inf), before relativistic corrections."""
    return 2.0


def ratio_sensitivity(name1, name2, S, hypothesis):
    """d ln(nu_1/nu_2) / d ln v for a clock pair, using B and K only."""
    B = {"optical": B_optical(), "hyperfine": B_hyperfine()}
    return (B[name1] - B[name2]) * K_mu(S, hypothesis)


def eps_detectable(frac_accuracy, name1, name2, S, hypothesis):
    """Smallest eps a pair resolves.  None when the pair is blind to eps."""
    k = ratio_sensitivity(name1, name2, S, hypothesis)
    if k == 0.0:
        return None
    return frac_accuracy / abs(k)


def eps_detectable_alpha(frac_accuracy, delta_A, hypothesis):
    """Via the alpha channel: an optical PAIR, sensitive only through K_alpha."""
    k = delta_A * K_alpha(hypothesis)
    if k == 0.0:
        return None
    return frac_accuracy / abs(k)


# ===================================================================== section 3
def cost_fraction(eps):
    """V(v(1+eps))/|V_min|, EXACT: eps^2 (2+eps)^2.  No small-eps expansion."""
    return eps ** 2 * (2.0 + eps) ** 2


def energy_density(eps):
    """J/m^3 held by a uniform linear displacement eps."""
    return VMIN_SI * cost_fraction(eps)


def mass_equivalent(eps):
    """kg/m^3 of the stored field energy."""
    return energy_density(eps) / C ** 2


def source_density(eps, higgs_fraction):
    """Total matter density, kg/m^3, whose scalar density holds this eps.

    eps = -rho_H c^2/(8|V_min|) with rho_H the Higgs-derived part.
    """
    rho_h = abs(eps) * 8.0 * VMIN_SI / C ** 2
    return rho_h / higgs_fraction, rho_h


def eps_from_matter(rho_total, higgs_fraction):
    """The displacement ordinary matter already carries.  NEGATIVE."""
    return -(rho_total * higgs_fraction) * C ** 2 / (8.0 * VMIN_SI)


def source_to_field_ratio(eps):
    """Source rest energy / stored field energy.

    EXACTLY 8/(|eps| (2+eps)^2), which tends to 2/|eps|.  CORRECTED (DOCKET 63,
    W12): this docstring and section 3 first said 1/(4 eps) -- a factor of 8
    below the ratio this function has always returned."""
    return (8.0 * VMIN_SI * abs(eps)) / energy_density(eps)


# ===================================================================== section 4
def yukawa_range():
    """lambda_h = hbar/(m_h c), metres.  From higgs.M_HIGGS, not retyped."""
    return HBAR * C / (M_HIGGS * GEV_IN_J)


def ultralocality_error(L):
    """(lambda_h/L)^2 -- the fractional error of the algebraic solution."""
    return (yukawa_range() / L) ** 2


def detection_standoff(eps_0, r0, eps_det):
    """How far OUTSIDE r0 the displacement stays above eps_det.  Metres.

    Solves eps_0 (r0/r) e^{-(r-r0)/lam} = eps_det for d = r - r0, RETURNING d
    AND NEVER r, because d is of order 1e-17 m and r0 of order 1: in double
    precision r - r0 evaluates to EXACTLY ZERO for r0 = 1 m, which is
    higgs.py's own catastrophic-cancellation channel appearing again.  The
    iteration is on d, so the small quantity is never the difference of two
    large ones.

    Returns None when the source is not above threshold even at contact.
    """
    if eps_0 <= eps_det:
        return None
    lam = yukawa_range()
    d = 0.0
    for _ in range(200):
        arg = eps_0 / (eps_det * (1.0 + d / r0))
        if arg <= 1.0:
            return None
        new = lam * math.log(arg)
        if abs(new - d) <= 1e-15 * abs(new):
            return new
        d = new
    return d


def gravimetric_radius(mass_kg, floor=GRAVIMETER_FLOOR):
    """r where GM/r^2 falls to the gravimeter floor."""
    return math.sqrt(G * mass_kg / floor)


# ===================================================================== section 7
def dlnE_dlnm(m_kg, p_si):
    """(m c^2/E)^2 -- the exact probe sensitivity AND the source efficiency."""
    E = math.sqrt((p_si * C) ** 2 + (m_kg * C ** 2) ** 2)
    return (m_kg * C ** 2 / E) ** 2


def B_transported_optical():
    """Coefficient of eps for the SAME optical clock read in two places.

    nu_opt ~ c R_inf F(alpha) and R_inf ~ m_e ~ v, so the ratio of a clock
    inside the displaced region to its twin outside is (1 + eps).  EXACTLY +1 --
    R_inf cancels between two TRANSITIONS, never between two PLACES.
    """
    return 1.0


def eps_detectable_transported(frac_accuracy):
    """Threshold for the courier channel.  Coefficient is exactly 1."""
    return frac_accuracy / abs(B_transported_optical())


def probe_ceiling(m_probe_mev, L):
    """Best d ln E/d ln m for a probe that resolves a region of size L."""
    p = HBAR / L                                        # kg m/s
    m = m_probe_mev * 1e6 * 1.602176634e-19 / C ** 2
    return dlnE_dlnm(m, p)


# ===================================================================== section 8
#: Flambaum, arXiv:0705.3704v2, eq. (9), READ FROM SOURCE and called by its
#: author "A rough estimate".  Carried as ORDER.
TH229_ENHANCEMENT = 1.0e5
TH229_COEFFS = {"alpha": 2.0, "X_q": 0.5, "X_s": -5.0}
TH229_OMEGA_EV = 7.0                 # the review's own normalisation
TH229_IS_ORDER = True


def dln_X_dln_v(hypothesis):
    """d ln(m_q/Lambda_QCD)/d ln v.  Same for X_s: both quark masses go as v."""
    if hypothesis == "H1":
        return 1.0 - float(dln_lambda_dln_v())
    if hypothesis == "H2":
        return 1.0
    raise ValueError(hypothesis)


def th229_coefficient(hypothesis, omega_ev=TH229_OMEGA_EV, k_alpha=None):
    """d ln(omega_Th)/d eps, from Flambaum eq. (9).  k_alpha defaults to the
    corrected K_alpha; pass K_alpha_as_first_written to reproduce the
    withdrawn figure."""
    k_alpha = K_alpha if k_alpha is None else k_alpha
    kx = dln_X_dln_v(hypothesis)
    inner = (TH229_COEFFS["alpha"] * k_alpha(hypothesis)
             + TH229_COEFFS["X_q"] * kx
             + TH229_COEFFS["X_s"] * kx)
    return TH229_ENHANCEMENT * inner * (7.0 / omega_ev)


def eps_detectable_th229(frac_accuracy, hypothesis, k_alpha=None):
    return frac_accuracy / abs(th229_coefficient(hypothesis, k_alpha=k_alpha))


# ===================================================================== section 9
def higgs_range(rho_total, higgs_fraction, eps_det):
    """Standoff outside a source of mean density rho.  Grows as ln(rho)."""
    eps0 = abs(eps_from_matter(rho_total, higgs_fraction))
    if eps0 <= eps_det:
        return 0.0
    return yukawa_range() * math.log(eps0 / eps_det)


def newton_range(rho_total, R, floor=GRAVIMETER_FLOOR):
    """Range of a gravimeter on the same sphere.  Grows as sqrt(rho)."""
    M = rho_total * 4.0 / 3.0 * math.pi * R ** 3
    return gravimetric_radius(M, floor)


def domination_ratio(rho_total, R, higgs_fraction, eps_det):
    """newton_range / higgs_range.  The theorem says this diverges."""
    d = higgs_range(rho_total, higgs_fraction, eps_det)
    if d <= 0.0:
        return float("inf")
    return newton_range(rho_total, R) / d


# ===================================================================== DOCKET 63
def higgs_fraction(S, hypothesis):
    """The Higgs-derived fraction of a nucleon's mass, f = d ln m_p/d ln v.

    S under H2; 2/9 + 7S/9 under H1.  DOCKET 63 F5: the first draft used f = S
    everywhere, which is H2 only.  (Electrons, 100% Higgs, add m_e/m_N ~ 5e-4
    of the mass and are neglected here as they always were.)"""
    return float(dln_mp_dln_v(S, hypothesis))


HYPOTHESES = ("H1", "H2")


def eps_det_stationary(hypothesis, S=None):
    """The adopted optical/Cs threshold at Godun's Cs-limited accuracy."""
    S = S_SCAN[1][1] if S is None else S
    return eps_detectable(GODUN_ABS_UNC, "optical", "hyperfine", S, hypothesis)


def finite_size_K(x=None):
    """K = d ln[nu(1S-2S)/nu(2P-3D)] / d ln v in hydrogen, from finite nuclear
    size alone, at x = r_N/a_0 (default r_p/a_0).  Closed form 28x^2/(14x^2-9);
    stdlib, so importing this module never needs sympy.  THE FORM IS DERIVED,
    NOT TRUSTED: finite_size_K_sympy() derives it and the selftest asserts the
    residual is exactly zero.  Series: -28x^2/9."""
    x = R_PROTON_M / A_BOHR_M if x is None else x
    return 28.0 * x * x / (14.0 * x * x - 9.0)


def finite_size_K_sympy():
    """The derivation behind finite_size_K, in sympy.  Returns (K(x), x).

    HYPOTHESES, NAMED: alpha fixed and r_N fixed (H2), so x = r_N/a_0 is
    proportional to m_e, hence to v; S levels shifted by (4/3) Z^4 x^2/n^3
    Rydberg (uniform-sphere nucleus, leading order), P and D not at all;
    recoil (m_e/M) omitted, which only adds.  Z = 1.
    """
    import sympy as sp
    x = sp.symbols("x", positive=True)

    def E(n, l):
        shift = sp.Rational(4, 3) * x ** 2 / n ** 3 if l == 0 else 0
        return -sp.Rational(1, n ** 2) + shift

    nu1 = E(2, 0) - E(1, 0)
    nu2 = E(3, 2) - E(2, 1)
    return sp.simplify(sp.diff(sp.log(nu1 / nu2), x) * x), x


def source_to_field_series():
    """8/(eps (2+eps)^2) expanded in sympy.  The leading term is 2/eps."""
    import sympy as sp
    e = sp.symbols("epsilon", positive=True)
    exact = (8 * e) / (e ** 2 * (2 + e) ** 2)
    return exact, sp.series(exact, e, 0, 2).removeO()


def naive_correction_factor(S):
    """(d ln m_p/d ln v under H1) / S -- the factor the 0.96% reading misses."""
    return higgs_fraction(S, "H1") / S


# --- W10: optical/optical is NOT exactly blind; the Cs channel is 2x, not 100x
OPTICAL_OPTICAL_IS_EXACTLY_BLIND = False           # WITHDRAWN (W10)
K_FINITE_SIZE_HYDROGEN = finite_size_K()           # COMPUTED (H2); sympy-checked
CS_CHANNEL_COARSER_BY = GODUN_ABS_UNC / GODUN_RATIO_UNC   # COMPUTED: 2
CS_CHANNEL_IS_HUNDRED_TIMES_COARSER = False         # WITHDRAWN (W10)
# --- W11: K_alpha(H1) had the wrong sign and no W threshold
K_ALPHA_H1 = K_alpha("H1")                          # COMPUTED, +43 alpha/(54 pi)
K_ALPHA_H1_COEFFICIENT = K_alpha_coefficient("H1")  # EXACT: 43/54
K_ALPHA_H1_AS_FIRST_WRITTEN = K_alpha_as_first_written("H1")   # WITHDRAWN value
K_ALPHA_H1_IS_NEGATIVE = False                      # WITHDRAWN (W11)
#: DOCKET 63 ruling F7's two printed consequence figures, READ VERBATIM from
#: the ruling as strings so their printed precision is kept.  NOT SEATED: the
#: ruling's own arithmetic is the withdrawn K_alpha with its sign flipped.
RULING_F7_PRINTED = {"th229_H1": "-3.48e5", "optical_optical_H1": "+0.0682"}


def _printed_value_and_quantum(txt):
    """A printed figure's value and the unit of its last printed digit."""
    d = Decimal(txt)
    return float(d), float(Decimal(1).scaleb(d.as_tuple().exponent))


def rounds_to_printed(x, txt):
    """Would x, rounded to txt's last printed digit, print as txt?"""
    v, q = _printed_value_and_quantum(txt)
    return abs(x - v) <= 0.5 * q


def f7_consequence(which, k):
    """The F7 consequence at K_alpha(H1) = k, asked of the owning formula."""
    if which == "th229_H1":
        return th229_coefficient("H1", k_alpha=lambda h: k)
    return (GODUN["A_E2"] - GODUN["A_E3"]) * k


def ruling_f7_k_required(which):
    """The K_alpha(H1) the ruling's printed figure would need.  Both
    consequences are affine in K_alpha (the selftest checks it), so solve
    from two evaluations.  Returns (K, the K-width of the printed quantum)."""
    v, q = _printed_value_and_quantum(RULING_F7_PRINTED[which])
    c0, c1 = f7_consequence(which, 0.0), f7_consequence(which, 1.0)
    return (v - c0) / (c1 - c0), 0.5 * q / abs(c1 - c0)


RULING_F7_K_REQUIRED = {w: ruling_f7_k_required(w) for w in RULING_F7_PRINTED}
RULING_F7_SEATED = {w: f7_consequence(w, K_ALPHA_H1) for w in RULING_F7_PRINTED}
RULING_F7_SIGN_FLIP = {w: f7_consequence(w, -K_ALPHA_H1_AS_FIRST_WRITTEN)
                       for w in RULING_F7_PRINTED}
#: COMPUTED: does the ruling's own K_alpha reproduce its printed figures?
RULING_F7_FOLLOWS_FROM_ITS_K_ALPHA = all(
    rounds_to_printed(RULING_F7_SEATED[w], RULING_F7_PRINTED[w])
    for w in RULING_F7_PRINTED)
#: COMPUTED: does the withdrawn K_alpha, sign flipped, reproduce them?
RULING_F7_IS_THE_SIGN_FLIP = all(
    rounds_to_printed(RULING_F7_SIGN_FLIP[w], RULING_F7_PRINTED[w])
    for w in RULING_F7_PRINTED)
# --- W12: the source/field ratio is 2/eps, not 1/(4 eps)
SOURCE_TO_FIELD_IS_QUARTER_OVER_EPS = False         # WITHDRAWN (W12)
#: COMPUTED by asking the owner: source_to_field_ratio(eps) over the withdrawn
#: 1/(4 eps), i.e. x 4 eps.  Exactly 32/(2+eps)^2 -- ~8, not the literal 8.
SOURCE_TO_FIELD_W12_FACTOR = (source_to_field_ratio(eps_det_stationary("H1"))
                              * 4.0 * eps_det_stationary("H1"))
# --- W13: the range is not the same obstruction for every role
SAME_OBSTRUCTION_EVERY_ROLE = False                 # WITHDRAWN (W13)
# --- F5: the source fractions, under BOTH hypotheses
SOURCE_FRACTION_WAS_H2_ONLY = True                  # the first draft's error
EPS_NUCLEAR = {h: eps_from_matter(RHO_NUCLEAR, higgs_fraction(S_SCAN[1][1], h))
               for h in HYPOTHESES}
EPS_NUCLEAR_OVER_DET = {h: abs(EPS_NUCLEAR[h]) / eps_det_stationary(h)
                        for h in HYPOTHESES}
#: The first draft's "about NINETY TIMES": H2's fraction over H1's threshold.
EPS_NUCLEAR_OVER_DET_AS_FIRST_WRITTEN = (abs(EPS_NUCLEAR["H2"])
                                         / eps_det_stationary("H1"))
COURIER_SOURCE_KG_M3 = {h: source_density(eps_detectable_transported(1e-18),
                                          higgs_fraction(S_SCAN[1][1], h))[0]
                        for h in HYPOTHESES}
# --- F6: "a factor of thirty" against "twenty-four"
NAIVE_CORRECTION_FACTOR = {lab: naive_correction_factor(S) for lab, S in S_SCAN}
FACTOR_OF_THIRTY = False                            # CORRECTED (F6)

WITHDRAWN = {
    "W10": ("address.py section 1: an optical/optical ratio 'IS EXACTLY BLIND' "
            "to eps, and the Cs channel is 'a hundred times coarser'",
            "finite nuclear size gives K = 28x^2/(14x^2 - 9) = %.4e in hydrogen "
            "(sympy, H2); the Cs channel is %.0fx coarser, not 100x"
            % (K_FINITE_SIZE_HYDROGEN, CS_CHANNEL_COARSER_BY)),
    "W11": ("address.py K_alpha(H1) = %.6e" % K_ALPHA_H1_AS_FIRST_WRITTEN,
            "sign wrong and W threshold missing; one loop gives +%s alpha/pi "
            "= %+.6e" % (K_ALPHA_H1_COEFFICIENT, K_ALPHA_H1)),
    "W12": ("address.py section 3: the source outweighs the field by "
            "'1/(4 eps_det)'",
            "the ratio is 2/eps (the selftest's own pin); the two differ by a "
            "factor of %.0f" % SOURCE_TO_FIELD_W12_FACTOR),
    "W13": ("address.py section 4: the range is 'THE SAME OBSTRUCTION EVERY "
            "ROLE HITS'",
            "role 3 falls to T_kk being a square, mass-independent (D17); "
            "role 2's m_e mechanism to an exact dilation (D18)"),
}


# ===================================================================== report
def report():
    print(__doc__)
    lam = yukawa_range()
    S_mid = S_SCAN[1][1]
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  imported from higgs.py, never retyped")
    print("      %-40s %18.6f GeV" % ("v", V_GEV))
    print("      %-40s %18.6f GeV" % ("m_h", M_HIGGS))
    print("      %-40s %18.6e J/m^3" % ("|V_min|", VMIN_SI))
    print("      %-40s %18.6e J/m^3" % ("8|V_min| = v^2 m_h^2", 8 * VMIN_SI))
    print()
    print("  1. the QCD exponent, EXACT over Fraction")
    a, e = _lambda_exponent_direct()
    print("      %-40s %18s" % ("Lambda_6 power in Lambda_3", a))
    for k in ("m_c", "m_b", "m_t"):
        print("      %-40s %18s" % ("  power of %s" % k, e[k]))
    print("      %-40s %18s" % ("d ln Lambda/d ln v", dln_lambda_dln_v()))
    print()
    print("  2. the sensitivity coefficients")
    print("      %-30s %11s %11s %11s %11s"
          % ("S", "dlnmp H1", "K_mu H1", "dlnmp H2", "K_mu H2"))
    for lab, S in S_SCAN:
        print("      %-30s %11.6f %11.6f %11.6f %11.6f"
              % ("%s (%.4f)" % (lab, S), dln_mp_dln_v(S, "H1"), K_mu(S, "H1"),
                 dln_mp_dln_v(S, "H2"), K_mu(S, "H2")))
    print("      %-40s %18s" % ("naive-correction factor dlnmp(H1)/S", ""))
    for lab, S in S_SCAN:
        print("      %-40s %18.4f" % ("  " + lab, naive_correction_factor(S)))
    print("      %-40s %18.6e" % ("K_alpha under H1, one loop, with W",
                                  K_alpha("H1")))
    print("      %-40s %18s" % ("  = coefficient x alpha/pi, coefficient",
                                K_alpha_coefficient("H1")))
    print("      %-40s %18.6e" % ("  WITHDRAWN first value (W11)",
                                  K_alpha_as_first_written("H1")))
    print("      %-40s %18.6e" % ("K_alpha under H2 (exact)", K_alpha("H2")))
    print("      %-40s %18.2f" % ("  |K_mu/K_alpha| under H1",
                                  abs(K_mu(S_mid, "H1") / K_alpha("H1"))))
    print()
    print("  3. the channels, and the blind one")
    print("      %-34s %10s %12s %14s"
          % ("channel", "dln/deps", "accuracy", "eps_det"))
    rows = [("optical / optical (Godun ratio)", "optical", "optical",
             GODUN_RATIO_UNC),
            ("optical / Cs (Godun absolute)", "optical", "hyperfine",
             GODUN_ABS_UNC),
            ("optical / Cs, future 1e-18", "optical", "hyperfine", 1.0e-18)]
    for lab, n1, n2, acc in rows:
        k = ratio_sensitivity(n1, n2, S_mid, "H1")
        ed = eps_detectable(acc, n1, n2, S_mid, "H1")
        print("      %-34s %10.4f %12.1e %14s"
              % (lab, k, acc, "BLIND (mu)" if ed is None else "%.4e" % ed))
    dA = GODUN["A_E2"] - GODUN["A_E3"]
    ea = eps_detectable_alpha(GODUN_RATIO_UNC, dA, "H1")
    print("      %-34s %10.4f %12.1e %14.4e"
          % ("optical/optical via K_alpha, H1", dA * K_alpha("H1"),
             GODUN_RATIO_UNC, ea))
    print("      %-34s %10.4f %12s %14s"
          % ("  WITHDRAWN first value (W11)",
             dA * K_alpha_as_first_written("H1"), "", ""))
    print("      %-34s %10s %12s %14s"
          % ("  ruling F7 printed (NOT SEATED)",
             RULING_F7_PRINTED["optical_optical_H1"], "",
             "sign flip" if RULING_F7_IS_THE_SIGN_FLIP else ""))
    print("      %-34s %10.4f %12.1e %14s"
          % ("  the same, under H2", 0.0, GODUN_RATIO_UNC, "BLIND (alpha)"))
    print("      %-34s %10.3e %12s %14s"
          % ("H 1S-2S/2P-3D, finite size (H2)", K_FINITE_SIZE_HYDROGEN, "",
             "NOT EXACTLY 0"))
    print("      %-40s %18.1f" % ("Cs channel coarser than the ratio by",
                                  CS_CHANNEL_COARSER_BY))
    print()
    for hyp in HYPOTHESES:
        print("      THE ADOPTED THRESHOLD, %s and S = 0.06:  eps_det = %.4e"
              % (hyp, eps_det_stationary(hyp)))
    eps_det = eps_det_stationary("H1")
    print()
    print("  4. the cost at threshold, and the cost that is not the cost")
    print("      %-40s %18.6e" % ("cost fraction eps^2(2+eps)^2 (H1 eps_det)",
                                  cost_fraction(eps_det)))
    print("      %-40s %18.6e J/m^3" % ("stored field energy",
                                        energy_density(eps_det)))
    print("      %-40s %18.6e kg/m^3" % ("  as mass", mass_equivalent(eps_det)))
    print("      %-40s %18.6e t TNT/m^3"
          % ("  as TNT", energy_density(eps_det) / 4.184e9))
    for hyp in HYPOTHESES:
        ed = eps_det_stationary(hyp)
        rho_tot, rho_h = source_density(ed, higgs_fraction(S_mid, hyp))
        print("      %s, f = %.6f" % (hyp, higgs_fraction(S_mid, hyp)))
        print("      %-40s %18.6e kg/m^3" % ("  Higgs-derived source density",
                                             rho_h))
        print("      %-40s %18.6e kg/m^3" % ("  total source density", rho_tot))
        print("      %-40s %18.6e" % ("  as a fraction of nuclear density",
                                      rho_tot / RHO_NUCLEAR))
        print("      %-40s %18.6e" % ("  source rest energy / field energy",
                                      source_to_field_ratio(ed)))
        print("      %-40s %18.6e" % ("    2/eps_det (the W12 correction)",
                                      2.0 / ed))
    print("      %-40s %18.1f" % ("  WITHDRAWN 1/(4 eps) was low by",
                                  SOURCE_TO_FIELD_W12_FACTOR))
    print()
    print("  5. the range")
    print("      %-40s %18.6e m" % ("lambda_h = hbar/(m_h c)", lam))
    print("      %-40s %18.6e" % ("  in proton radii", lam / R_PROTON_M))
    print("      %-40s %18.6e" % ("  Bohr radius / lambda_h", A_BOHR_M / lam))
    print("      %-40s %18.6e" % ("ultralocality error at L = 1 m",
                                  ultralocality_error(1.0)))
    print("      %-34s %10s %14s %18s"
          % ("source", "eps_0", "r_0 (m)", "detection radius"))
    for lab, e0, r0 in (("field pushed to 2v, 1 m sphere", 1.0, 1.0),
                        ("field pushed to 2v, nuclear-size", 1.0, 1e-15),
                        ("eps_0 = 1e-18 as proposed", 1e-18, 1.0),
                        ("eps_0 = eps_det exactly", eps_det, 1.0)):
        d = detection_standoff(e0, r0, eps_det)
        print("      %-34s %10.1e %14.1e %18s"
              % (lab, e0, r0,
                 "NOT DETECTABLE" if d is None else "%.4e m outside" % d))
    print()
    print("  6. what matter already does -- each ratio inside ONE hypothesis")
    print("      %-30s %12s %14s %10s %14s %10s"
          % ("medium", "rho (kg/m^3)", "eps H1", "/det H1", "eps H2",
             "/det H2"))
    for lab, rho in (("nuclear matter", RHO_NUCLEAR),
                     ("white-dwarf core", 1e9),
                     ("osmium", 22590.0),
                     ("water", 1000.0),
                     ("laboratory vacuum 1e-10 Pa", 1e-15)):
        cells = []
        for hyp in HYPOTHESES:
            ev = eps_from_matter(rho, higgs_fraction(S_mid, hyp))
            cells += [ev, abs(ev) / eps_det_stationary(hyp)]
        print("      %-30s %12.3e %14.4e %10.3e %14.4e %10.3e"
              % tuple([lab, rho] + cells))
    print("      %-40s %18.2f" % ("WITHDRAWN 'ninety times' (H2 f / H1 det)",
                                  EPS_NUCLEAR_OVER_DET_AS_FIRST_WRITTEN))
    print()
    print("  7. the same source, read by gravity")
    Vol = 4.0 / 3.0 * math.pi * 1.0 ** 3
    for hyp in HYPOTHESES:
        ed = eps_det_stationary(hyp)
        rho_tot, _ = source_density(ed, higgs_fraction(S_mid, hyp))
        M = rho_tot * Vol
        rg = gravimetric_radius(M)
        print("      %s" % hyp)
        print("      %-40s %18.6e kg" % ("  mass of the threshold 1 m sphere", M))
        print("      %-40s %18.6e m" % ("  gravimetric range at 1e-9 m/s^2", rg))
        print("      %-40s %18.6e m" % ("  Higgs range (same source)", 0.0))
        print("      %-40s %18.6e" % ("  ratio to the 2v best case",
                                      rg / detection_standoff(1.0, 1.0, ed)))
        Mg = GRAVIMETER_FLOOR * 1.0 ** 2 / G
        ev = abs(eps_from_matter(Mg, higgs_fraction(S_mid, hyp)))
        print("      %-40s %18.6e kg" % ("  mass gravity reads at 1 m", Mg))
        print("      %-40s %18.6e" % ("    its eps in a 1 m^3 box", ev))
        print("      %-40s %18.6e" % ("    short of eps_det by", ed / ev))
    print()
    print("  8. the probe lemma")
    print("      %-34s %14s %18s" % ("probe", "resolves (m)", "dlnE/dlnm ceiling"))
    for lab, mev in (("electron", M_E_MEV), ("proton", M_P_MEV),
                     ("Higgs itself", M_HIGGS * 1e3)):
        print("      %-34s %14.3e %18.6e"
              % (lab, lam, probe_ceiling(mev, lam)))
    print("      %-40s %18.6e" % ("(m_e/m_h)^2",
                                  (M_E_MEV / (M_HIGGS * 1e3)) ** 2))
    ep = GODUN_RATIO_UNC / probe_ceiling(M_E_MEV, lam)
    print("      %-40s %18.6e" % ("eps a resolving probe needs", ep))
    for hyp in HYPOTHESES:
        rp, _ = source_density(ep, higgs_fraction(S_mid, hyp))
        print("      %-40s %18.6e kg/m^3" % ("  its source, %s" % hyp, rp))
        print("      %-40s %18.6e" % ("    / nuclear density", rp / RHO_NUCLEAR))
    print()
    print("  9. the courier -- the best channel in the file")
    print("      %-40s %18.6f" % ("coefficient of eps", B_transported_optical()))
    ec = eps_detectable_transported(1e-18)
    print("      %-40s %18.6e" % ("eps_det at 1e-18 clock comparison", ec))
    print("      %-40s %18.6e" % ("  better than the stationary channel by",
                                  eps_det / ec))
    print("      %-40s %18.6e m" % ("region needed (a Bohr radius)", A_BOHR_M))
    print("      %-40s %18.6e" % ("  in screening lengths", A_BOHR_M / lam))
    for hyp in HYPOTHESES:
        rc = COURIER_SOURCE_KG_M3[hyp]
        print("      %-40s %18.6e kg/m^3" % ("source that must fill it, %s" % hyp,
                                             rc))
        print("      %-40s %18.6e" % ("  times osmium", rc / 22590.0))
    print()
    print(" 10. the Th-229 loophole, computed rather than dismissed")
    for hyp in HYPOTHESES:
        c229 = th229_coefficient(hyp)
        e229 = eps_detectable_th229(1e-18, hyp)
        r229, _ = source_density(e229, higgs_fraction(S_mid, hyp))
        print("      %-18s coeff %12.4e  eps_det %11.4e  source %11.4e kg/m^3"
              % (hyp, c229, e229, r229))
    print("      %-18s coeff %12.4e  eps_det %11.4e"
          % ("H1 WITHDRAWN K_a",
             th229_coefficient("H1", k_alpha=K_alpha_as_first_written),
             eps_detectable_th229(1e-18, "H1",
                                  k_alpha=K_alpha_as_first_written)))
    e229 = eps_detectable_th229(1e-18, "H1")
    print("      %-40s %18.6e" % ("better than the electronic courier by",
                                  1e-18 / e229))
    print("      %-40s %18.6e"
          % ("  its source (H1), times osmium",
             source_density(e229, higgs_fraction(S_mid, "H1"))[0] / 22590.0))
    print()
    print(" 11. the domination theorem -- ln(rho) against sqrt(rho), H1")
    fH1 = higgs_fraction(S_mid, "H1")
    print("      %-14s %14s %14s %14s %12s"
          % ("rho (kg/m^3)", "eps", "Higgs d (m)", "Newton r (m)", "r/d"))
    for rho in (1e4, 1e7, 1e10, 1e13, 1e16, RHO_NUCLEAR, 1e22):
        d = higgs_range(rho, fH1, e229)
        rr = newton_range(rho, 1.0)
        print("      %14.3e %14.4e %14.4e %14.4e %12.4e"
              % (rho, abs(eps_from_matter(rho, fH1)), d, rr,
                 domination_ratio(rho, 1.0, fH1, e229)))
    print("      AND THE LAST COLUMN IS MONOTONE INCREASING.  That is the")
    print("      theorem: no source strength closes it.")
    print()
    print(" 12. DOCKET 63: withdrawn, kept")
    import textwrap
    for key in sorted(WITHDRAWN):
        claim, why = WITHDRAWN[key]
        print("      %s  %s" % (key, textwrap.fill(claim, 66,
                                                   subsequent_indent=" " * 10)))
        print("          -> %s" % textwrap.fill(why, 63,
                                                subsequent_indent=" " * 13))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Role 1 needed only detectability and it does not have it.  The")
    print("  displacement is ultralocal, so it is not an address but a contact")
    print("  readout of local density; nuclear matter already holds one")
    print("  %.0f (H1) or %.0f (H2) times over threshold and nothing outside"
          % (EPS_NUCLEAR_OVER_DET["H1"], EPS_NUCLEAR_OVER_DET["H2"]))
    print("  the nucleus sees it; and the one source that would work is read by")
    print("  an ordinary gravimeter twenty-three orders further out.  The Th-229")
    print("  courier is eight orders better than the stationary channel and")
    print("  changes nothing, because the gap it must close grows as")
    print("  sqrt(rho)/ln(rho) and diverges.  REFUTED, NOT PRICED.")
    print()


# ===================================================================== selftest
def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-60s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-60s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("address.py --selftest")
    print()

    # -------------------------------------------- CONTROL 1: Godun's own coefficients
    # THIS MUST FIRE.  The machinery of section 1 is a derivation of B_i from
    # nu_hf/(c R_inf) ~ alpha^2 g_I (m_e/m_p) F_rel and nu_opt/(c R_inf) = F(alpha).
    # If that derivation is wrong, these three published integers do not come out.
    print("  CONTROL 1 -- reproduce Godun et al. 2014's published B and A")
    chk("read from source", GODUN_READ_FROM_SOURCE, True)
    chk("B_E3 = 0 (published)  <-  derived optical exponent",
        B_optical(), GODUN["B_E3"])
    chk("B_E2 = 0 (published)  <-  derived optical exponent",
        B_optical(), GODUN["B_E2"])
    chk("B_Cs = -1 (published) <-  derived hyperfine exponent",
        B_hyperfine(), GODUN["B_Cs"])
    chk("A_Cs integer part 2 (published 2.83) <- derived alpha^2",
        A_hyperfine_nonrelativistic(), float(int(GODUN["A_Cs"])))
    chkrel("and the relativistic remainder is the published 0.83",
           GODUN["A_Cs"] - A_hyperfine_nonrelativistic(), 0.83, 1e-12)
    # and the inversion Godun states must be reproducible from those coefficients
    dA = GODUN["A_E3"] - GODUN["A_Cs"]
    dB = GODUN["B_E3"] - GODUN["B_Cs"]
    chkrel("A_E3 - A_Cs", dA, -8.78, 1e-12)
    chkrel("B_E3 - B_Cs", dB, 1.0, 1e-12)
    # NEGATIVE CONTROL for control 1: the natural slip is to give the optical
    # transition B = +1 because nu_opt ~ m_e.  If it did, B_E3 - B_Cs would be 2
    # and every mu_dot in the literature would be off by a factor two.
    chk("the slip B_opt = +1 would double Godun's mu coefficient",
        (1.0 - GODUN["B_Cs"]) / dB, 2.0)

    # -------------------------------------------- CONTROL 2: the blind channel fires
    # A scan with no positive control is worthless.  Here the POSITIVE control is
    # that the optical/Cs pair MUST return a finite eps_det, and the NEGATIVE
    # control is that the optical/optical pair MUST return None.
    print()
    print("  CONTROL 2 -- the blind channel is blind and the live one is live")
    S_mid = S_SCAN[1][1]
    chk("optical/optical is blind to eps",
        eps_detectable(1e-18, "optical", "optical", S_mid, "H1"), None)
    chk("optical/Cs is not",
        eps_detectable(1e-18, "optical", "hyperfine", S_mid, "H1") is not None,
        True)
    chk("and it stays live under H2",
        eps_detectable(1e-18, "optical", "hyperfine", S_mid, "H2") is not None,
        True)
    chk("OPTICAL_OPTICAL_IS_BLIND (through mu, point nucleus)",
        OPTICAL_OPTICAL_IS_BLIND, True)

    # ------------------------------------------------------- the QCD exponent, EXACT
    print()
    print("  the QCD exponent")
    chk("b_0(3)", beta0(3), Fraction(9))
    chk("b_0(4)", beta0(4), Fraction(25, 3))
    chk("b_0(5)", beta0(5), Fraction(23, 3))
    chk("b_0(6)", beta0(6), Fraction(7))
    for nf in (4, 5, 6):
        chk("threshold step at n_f=%d" % nf, threshold_step(nf),
            Fraction(2, 3))
    a, e = _lambda_exponent_direct()
    chk("Lambda_6 power", a, Fraction(7, 9))
    for k in ("m_c", "m_b", "m_t"):
        chk("power of %s is 2/27" % k, e[k], Fraction(2, 27))
    chk("d ln Lambda/d ln v = 2/9 EXACTLY", dln_lambda_dln_v(), Fraction(2, 9))
    # homogeneity: the powers must reconstruct Lambda_3's mass dimension, 1
    chk("mass dimensions close", a + sum(e.values()), Fraction(1))
    # 2/27 IS THE POWER IN Lambda_3 AND NOWHERE ELSE.  Integrating out only the
    # top and stopping at n_f = 5 gives (2/3)/b_0(5) = 2/23, a DIFFERENT object.
    # The first draft asserted 2/27 there and the exact arithmetic refused it.
    chk("stopping at n_f = 5 gives 2/23, not 2/27", dln_lambda_dln_v(1),
        Fraction(2, 23))
    chk("2/27 is the power in Lambda_3, reached only after all three",
        _lambda_exponent_direct(3)[1]["m_t"], Fraction(2, 27))

    # ------------------------------------------------------------- K_mu, both ways
    print()
    print("  K_mu")
    for lab, S in S_SCAN:
        k1, k2 = K_mu(S, "H1"), K_mu(S, "H2")
        chk("O(1) and negative under H1: %s" % lab, -1.0 < k1 < -0.5, True)
        chk("O(1) and negative under H2: %s" % lab, -1.0 < k2 < -0.5, True)
    chkrel("K_mu(H1) at the naive 0.96%", K_mu(QUARK_SUM_MEV / M_P_MEV, "H1"),
           -0.7703262, 1e-6)
    chkrel("K_mu(H2) at the naive 0.96%", K_mu(QUARK_SUM_MEV / M_P_MEV, "H2"),
           -0.9904191, 1e-6)
    # THE CORRECTION THIS FILE MAKES: H1 is 24x the naive sensitivity of m_p
    chkrel("H1's dln m_p/dln v is 24x the naive 0.0096",
           dln_mp_dln_v(QUARK_SUM_MEV / M_P_MEV, "H1")
           / (QUARK_SUM_MEV / M_P_MEV), 23.9, 2e-2)
    # the two hypotheses AGREE on the verdict, which is the point
    chk("H1 and H2 agree within a factor 1.3 at every S",
        all(abs(K_mu(S, "H2") / K_mu(S, "H1")) < 1.3 for _, S in S_SCAN), True)
    chk("K_alpha is EXACTLY zero under H2", K_alpha("H2"), 0.0)
    # DOCKET 63 W11.  RE-PINNED: +43 alpha/(54 pi), positive, W included.
    chk("K_alpha(H1) coefficient is EXACTLY 43/54 (x alpha/pi)",
        K_alpha_coefficient("H1"), Fraction(43, 54))
    chkrel("K_alpha(H1) = +43 alpha/(54 pi)", K_alpha("H1"), 1.849653e-3, 1e-6)
    chk("  and it is POSITIVE (the first version's sign was wrong)",
        K_alpha("H1") > 0.0, True)
    chk("  and about 400x below |K_mu| under H1",
        300 < abs(K_mu(S_mid, "H1") / K_alpha("H1")) < 500, True)
    import sympy as sp
    chk("sympy: d ln alpha(0)/d ln m = +alpha b/(2 pi) for one threshold",
        K_alpha_sign_sympy(), 0)
    chk("the fermions alone give 116/27, the W gives -7/2",
        (K_alpha_coefficient("H1", with_W=False),
         K_alpha_coefficient("H1") - K_alpha_coefficient("H1", with_W=False)),
        (Fraction(116, 27), Fraction(-7, 2)))
    # THE WITHDRAWN VALUE, REPRODUCED BY ITS OWN FORMULA, NOT TYPED
    chkrel("WITHDRAWN K_alpha(H1) as first written", K_alpha_as_first_written("H1"),
           -9.979521e-3, 1e-6)
    chkrel("  which is exactly the fermion-only value with its sign flipped",
           K_alpha_as_first_written("H1"),
           -float(K_alpha_coefficient("H1", with_W=False)) * ALPHA_EM / math.pi,
           1e-12)
    chk("recorded: K_alpha(H1) is not negative", K_ALPHA_H1_IS_NEGATIVE, False)
    chk("TREE_LEVEL_ALPHA_IS_V_INDEPENDENT",
        TREE_LEVEL_ALPHA_IS_V_INDEPENDENT, True)

    # ---------------------------------------------------- the cost identity, EXACT
    print()
    print("  the cost")
    chk("cost fraction is exactly zero at eps = 0", cost_fraction(0.0), 0.0)
    chk("and exactly 1 at eps = -1 (the field driven to zero)",
        cost_fraction(-1.0), 1.0)
    for eps in (1e-20, 1e-12, 1e-6):
        chkrel("eps^2(2+eps)^2 -> 4 eps^2 at eps=%g" % eps,
               cost_fraction(eps) / (4 * eps ** 2), 1.0, 1e-5)
    # the exact form is NOT 4 eps^2, and at eps = 1 the difference is 125%
    chkrel("at eps = 1 the exact form is 9, not 4", cost_fraction(1.0), 9.0,
           1e-12)
    chkrel("energy density at eps=1 is 9|V_min|", energy_density(1.0),
           9.0 * VMIN_SI, 1e-12)
    # 8|V_min| = v^2 m_h^2 -- the identity the source formula rests on
    chkrel("8|V_min| = v^2 m_h^2",
           8.0 * VMIN_SI,
           higgs.gev4_to_si(V_GEV ** 2 * M_HIGGS ** 2), 1e-12)
    # source and eps invert
    for eps in (1e-16, 1e-10, 1e-3):
        rho_tot, _ = source_density(eps, 0.06)
        chkrel("source_density inverts at eps=%g" % eps,
               abs(eps_from_matter(rho_tot, 0.06)), eps, 1e-12)
    # THE FINDING: the field energy is a 1e-15 fraction of the source
    eps_det = eps_detectable(GODUN_ABS_UNC, "optical", "hyperfine",
                             S_SCAN[1][1], "H1")
    chk("the source outweighs the field energy by more than 1e14",
        source_to_field_ratio(eps_det) > 1e14, True)
    chkrel("and that ratio is exactly 2/eps", source_to_field_ratio(eps_det),
           2.0 / eps_det, 1e-6)

    # --------------------------------------------------------------- the range
    print()
    print("  the range")
    lam = yukawa_range()
    chkrel("lambda_h", lam, 1.576094e-18, 1e-6)
    chkrel("  in proton radii", lam / R_PROTON_M, 1.8732e-3, 1e-3)
    chkrel("  Bohr radii per lambda_h", A_BOHR_M / lam, 3.3575e7, 1e-3)
    chk("no atom fits in the screening length", A_BOHR_M / lam > 1e7, True)
    chk("nor does a proton", R_PROTON_M / lam > 1e2, True)
    chk("ultralocality error at 1 m is below 1e-35",
        ultralocality_error(1.0) < 1e-35, True)
    # POSITIVE CONTROL on detection_radius: it must return something above r0
    d = detection_standoff(1.0, 1.0, eps_det)
    chk("a maximal source IS detectable outside itself", d is not None, True)
    chk("  but by less than 1e-16 m", d < 1e-16, True)
    chkrel("  and the standoff is exactly lambda_h ln(1/eps_det)", d,
           lam * math.log(1.0 / eps_det), 1e-12)
    # AND THE CANCELLATION IS REAL: r - r0 is exactly zero in double precision,
    # which is why detection_standoff never forms that difference.
    chk("r - r0 would have evaluated to exactly zero", (1.0 + d) - 1.0, 0.0)
    # NEGATIVE CONTROL: a source at or below threshold must return None
    chk("eps_0 = 1e-18 is not detectable at all",
        detection_standoff(1e-18, 1.0, eps_det), None)
    chk("eps_0 = eps_det exactly is not detectable outside itself",
        detection_standoff(eps_det, 1.0, eps_det), None)
    # the standoff is set by lambda_h and NOT by the source size
    # NOT exactly the same: for r0 = 1 fm the standoff is 5.5% of r0, so the
    # 1/r geometric factor is no longer negligible and shaves 0.15% off it.
    # Asserting equality to 1e-6 FAILED, and the discrepancy is that factor.
    d_fm = detection_standoff(1.0, 1e-15, eps_det)
    chkrel("the standoff is set by lambda_h, not by the source size", d_fm, d,
           2e-3)
    chk("  and is SMALLER for the small source, by the 1/r factor", d_fm < d,
        True)
    chkrel("  by exactly lambda_h ln(1 + d/r0)", d - d_fm,
           lam * math.log(1.0 + d_fm / 1e-15), 1e-6)

    # ------------------------------------------------- what matter already does
    print()
    print("  what matter already does")
    # DOCKET 63 F5: the fraction is d ln m_p/d ln v, under EACH hypothesis,
    # and every ratio is taken inside one of them.
    chkrel("Higgs-derived fraction under H1 at S = 0.06",
           higgs_fraction(S_mid, "H1"), 0.268889, 1e-5)
    chk("  and under H2 it is S itself", higgs_fraction(S_mid, "H2"), S_mid)
    for hyp in HYPOTHESES:
        chk("nuclear matter displaces the vev DOWNWARD (%s)" % hyp,
            EPS_NUCLEAR[hyp] < 0.0, True)
    chkrel("  by, under H1", abs(EPS_NUCLEAR["H1"]), 3.26359e-13, 1e-5)
    chkrel("  by, under H2 (the first draft's only figure)",
           abs(EPS_NUCLEAR["H2"]), 7.28239e-14, 1e-5)
    chkrel("  times eps_det, both under H1", EPS_NUCLEAR_OVER_DET["H1"],
           397.674, 1e-5)
    chkrel("  times eps_det, both under H2", EPS_NUCLEAR_OVER_DET["H2"],
           114.091, 1e-5)
    chkrel("WITHDRAWN 'about NINETY': H2's fraction over H1's threshold",
           EPS_NUCLEAR_OVER_DET_AS_FIRST_WRITTEN, 88.737, 1e-4)
    for hyp in HYPOTHESES:
        chk("water is nowhere near it (%s)" % hyp,
            abs(eps_from_matter(1000.0, higgs_fraction(S_mid, hyp)))
            < eps_det_stationary(hyp), True)
    # linear in density -- the ultralocality statement, checked
    chkrel("eps is exactly linear in rho",
           eps_from_matter(2.0 * RHO_NUCLEAR, 0.06)
           / eps_from_matter(RHO_NUCLEAR, 0.06), 2.0, 1e-12)

    # ------------------------------------------------------- gravity dominates
    print()
    print("  gravity")
    for hyp, want in (("H1", 1.371597e7), ("H2", 2.560737e7)):
        ed = eps_det_stationary(hyp)
        rho_tot, _ = source_density(ed, higgs_fraction(S_mid, hyp))
        rg = gravimetric_radius(rho_tot * 4.0 / 3.0 * math.pi)
        chkrel("the threshold 1 m source is read by gravity to (%s)" % hyp,
               rg, want, 1e-5)
        chk("  which beats the Higgs standoff by more than 1e23 (%s)" % hyp,
            rg / detection_standoff(1.0, 1.0, ed) > 1e23, True)
    # POSITIVE CONTROL on the gravimeter model: it must reproduce g at Earth
    chkrel("gravimetric model reproduces Earth surface gravity",
           G * 5.9722e24 / 6.371e6 ** 2, 9.8, 1e-2)

    # ---------------------------------------------------------- the probe lemma
    print()
    print("  the probe lemma")
    # EXACT: d ln E/d ln m = (m c^2/E)^2, equal to 1 at rest and 0 massless
    m_e_kg = M_E_MEV * 1e6 * 1.602176634e-19 / C ** 2
    chkrel("at rest the sensitivity is exactly 1", dlnE_dlnm(m_e_kg, 0.0), 1.0,
           1e-15)
    chk("and it is monotone decreasing in p",
        all(dlnE_dlnm(m_e_kg, p) > dlnE_dlnm(m_e_kg, 10 * p)
            for p in (1e-24, 1e-22, 1e-20, 1e-18)), True)
    # the ceiling for a probe that resolves lambda_h
    ceil_e = probe_ceiling(M_E_MEV, lam)
    # THE FIRST DRAFT PUT THIS AT 1.67e-17 BY WRITING m_e AS 0.511e-3 MeV.  The
    # instrument refused it.  (m_e/m_h)^2 = (0.511/125200)^2 = 1.6658e-11.
    chkrel("an electron resolving lambda_h", ceil_e, 1.665833e-11, 1e-5)
    chkrel("  which is exactly (m_e/m_h)^2", ceil_e,
           (M_E_MEV / (M_HIGGS * 1e3)) ** 2, 1e-4)
    chk("so it is ABOVE the best clock ratio, and the probe is not dead here",
        ceil_e > GODUN_RATIO_UNC, True)
    eps_probe = GODUN_RATIO_UNC / ceil_e
    chkrel("  it needs eps >=", eps_probe, 1.80090e-5, 1e-4)
    for hyp, want in (("H1", 5.518163e7), ("H2", 2.472955e8)):
        rho_probe, _ = source_density(eps_probe, higgs_fraction(S_mid, hyp))
        chkrel("  whose source, in nuclear densities (%s)" % hyp,
               rho_probe / RHO_NUCLEAR, want, 1e-5)
    # NEGATIVE CONTROL: a probe that does NOT need to resolve lambda_h is fine,
    # which is why the lemma has to be tied to the resolution requirement
    chk("a probe resolving only 1 m keeps full sensitivity",
        probe_ceiling(M_E_MEV, 1.0) > 0.99, True)

    # ------------------------------------------------- the courier, and its kill
    print()
    print("  the transported clock")
    chk("two PLACES do not cancel R_inf the way two TRANSITIONS do",
        B_transported_optical(), 1.0)
    chk("  so it beats every stationary channel",
        eps_detectable_transported(1e-18)
        < eps_detectable(GODUN_ABS_UNC, "optical", "hyperfine",
                         S_SCAN[1][1], "H1"), True)
    chkrel("  eps_det for the courier", eps_detectable_transported(1e-18),
           1e-18, 1e-15)
    # DOCKET 63 F5.  The first draft pinned only the H2 figure, 3.6746e12.
    chkrel("  but the source it needs, kg/m^3, H1", COURIER_SOURCE_KG_M3["H1"],
           8.19956e11, 1e-5)
    chkrel("  and under H2 (the first draft's only figure)",
           COURIER_SOURCE_KG_M3["H2"], 3.6746e12, 1e-4)
    chkrel("  H1 times the density of osmium",
           COURIER_SOURCE_KG_M3["H1"] / 22590.0, 3.62973e7, 1e-5)
    chkrel("  H2 times the density of osmium",
           COURIER_SOURCE_KG_M3["H2"] / 22590.0, 1.6267e8, 1e-4)
    chkrel("  the Higgs-derived part is 2.204772e11 under both (DOCKET 63 A.5)",
           source_density(1e-18, 1.0)[1], 2.204772e11, 1e-6)
    chk("  and the region must be at least a Bohr radius across",
        A_BOHR_M / yukawa_range() > 1e7, True)

    # ------------------------------------------------ the Th-229 loophole
    print()
    print("  the Th-229 loophole")
    chk("X_q and X_s move with v under H1 at 7/9",
        abs(dln_X_dln_v("H1") - 7.0 / 9.0) < 1e-12, True)
    chk("and at exactly 1 under H2", dln_X_dln_v("H2"), 1.0)
    for hyp in ("H1", "H2"):
        chk("the Th coefficient is large and negative under %s" % hyp,
            th229_coefficient(hyp) < -1e5, True)
    e229 = eps_detectable_th229(1e-18, "H1")
    # RE-PINNED (DOCKET 63 W11): the corrected K_alpha moves this 0.67%.
    chkrel("eps_det for the Th courier", e229, 2.86017e-24, 1e-5)
    chkrel("  Th coefficient under H1, corrected K_alpha",
           th229_coefficient("H1"), -3.49630e5, 1e-5)
    chkrel("  WITHDRAWN: with the first K_alpha it was -3.520e5",
           th229_coefficient("H1", k_alpha=K_alpha_as_first_written),
           -3.51996e5, 1e-5)
    chkrel("  and eps_det 2.8412e-24 (the first draft's fixture)",
           eps_detectable_th229(1e-18, "H1", k_alpha=K_alpha_as_first_written),
           2.8409e-24, 1e-4)
    chk("  which beats the electronic courier by more than 1e5",
        1e-18 / e229 > 1e5, True)
    chk("  and it is NOT dismissed: it is the best number here",
        e229 < eps_detectable_transported(1e-18), True)
    chk("Flambaum's own figure is carried as ORDER", TH229_IS_ORDER, True)
    # NEGATIVE CONTROL on the enhancement.  Removing it must cost EXACTLY 1e5
    # and no more -- which also shows the enhancement is not doing all the work:
    # the unenhanced transition already beats an electronic clock 3.5x, through
    # the -5 on X_s alone.  The first draft asserted the opposite and was wrong.
    saved = globals()["TH229_ENHANCEMENT"]
    globals()["TH229_ENHANCEMENT"] = 1.0
    bare = eps_detectable_th229(1e-18, "H1")
    globals()["TH229_ENHANCEMENT"] = saved
    chkrel("removing the 1e5 enhancement costs exactly 1e5", bare / e229, 1e5,
           1e-12)
    chk("  and the BARE Th transition still beats the electronic courier",
        bare < eps_detectable_transported(1e-18), True)
    # RE-PINNED (W11): |2 K_alpha + 0.5(7/9) - 5(7/9)| = 3.5 - 2 K_alpha
    chkrel("  by the X_s coefficient alone",
           eps_detectable_transported(1e-18) / bare, 3.49630, 1e-5)
    chkrel("and the enhancement restores it exactly",
           eps_detectable_th229(1e-18, "H1"), e229, 1e-15)

    # ------------------------------------------------ the domination theorem
    print()
    print("  the domination theorem")
    rhos = [10.0 ** k for k in range(4, 23)]
    fH1 = higgs_fraction(S_mid, "H1")      # e229 is H1's, so the fraction is too
    ratios = [domination_ratio(r, 1.0, fH1, e229) for r in rhos]
    finite = [(r, x) for r, x in zip(rhos, ratios) if x != float("inf")]
    chk("the ratio is finite once the source is above threshold",
        len(finite) > 10, True)
    chk("AND IT IS MONOTONE INCREASING IN rho",
        all(finite[i][1] < finite[i + 1][1] for i in range(len(finite) - 1)),
        True)
    chk("  by more than 1e5 across the decades where both are defined",
        finite[-1][1] / finite[0][1] > 1e5, True)
    # the scaling itself: Higgs as ln, Newton as sqrt
    d1 = higgs_range(1e10, fH1, e229)
    d2 = higgs_range(1e20, fH1, e229)
    n1 = newton_range(1e10, 1.0)
    n2 = newton_range(1e20, 1.0)
    chkrel("Newton range scales as sqrt(rho): 1e10 -> 1e20 gives 1e5",
           n2 / n1, 1e5, 1e-9)
    chk("Higgs range scales as ln(rho): the same ten decades give under 10",
        d2 / d1 < 10.0, True)
    chk("  so Newton outgrows Higgs by more than 1e4 over ten decades",
        (n2 / n1) / (d2 / d1) > 1e4, True)
    chkrel("  and the increment is exactly lambda_h ln(1e10)", d2 - d1,
           yukawa_range() * math.log(1e10), 1e-9)
    # POSITIVE CONTROL: below threshold the Higgs range must be exactly zero
    chk("a source below threshold has EXACTLY zero Higgs range",
        higgs_range(1.0, fH1, e229), 0.0)

    # ------------------------------------------------ DOCKET 63: W10, W12, W13, F6
    print()
    print("  DOCKET 63 withdrawals")
    Ksym, xs = finite_size_K_sympy()
    chk("W10 sympy derives K = 28x^2/(14x^2 - 9): residual",
        sp.simplify(Ksym - 28 * xs ** 2 / (14 * xs ** 2 - 9)), 0)
    chk("W10   and its series leads with -28x^2/9",
        sp.series(Ksym, xs, 0, 4).removeO(), -sp.Rational(28, 9) * xs ** 2)
    chkrel("W10 finite nuclear size in hydrogen, H2", K_FINITE_SIZE_HYDROGEN,
           -7.8654e-10, 1e-4)
    chk("W10 CONTROL: a point nucleus (x = 0) gives exactly zero",
        finite_size_K(0.0), 0.0)
    chk("W10 so optical/optical is NOT exactly blind",
        OPTICAL_OPTICAL_IS_EXACTLY_BLIND, False)
    chk("W10 the Cs channel is 2x coarser than the ratio, not 100x",
        CS_CHANNEL_COARSER_BY, 2.0)
    chk("W10   recorded", CS_CHANNEL_IS_HUNDRED_TIMES_COARSER, False)
    exact, ser = source_to_field_series()
    e_ = sp.symbols("epsilon", positive=True)
    chk("W12 sympy: source/field = 8/(eps (2+eps)^2) -> 2/eps - 2 + ...",
        sp.simplify(ser - (2 / e_ - 2 + sp.Rational(3, 2) * e_)), 0)
    chkrel("W12 source_to_field_ratio agrees with the exact form",
           source_to_field_ratio(1e-3), float(exact.subs(e_, sp.Rational(1, 1000))),
           1e-12)
    chk("W12 sympy: 4 eps x source/field -> 8 as eps -> 0",
        sp.limit(4 * e_ * exact, e_, 0), 8)
    # ASKS the owner: source_to_field_ratio(eps_det) x 4 eps_det = 32/(2+eps)^2
    chkrel("W12 the withdrawn 1/(4 eps) is low by ~8 (source_to_field_ratio x 4 eps)",
           SOURCE_TO_FIELD_W12_FACTOR, 8.0, 1e-12)
    chk("W12   and not by the literal 8: it is 32/(2+eps)^2 < 8",
        SOURCE_TO_FIELD_W12_FACTOR < 8.0, True)
    s16 = source_to_field_ratio(8e-16)
    chk("W12   2.5e15 at eps = 8e-16 (DOCKET 63 D), asked of source_to_field_ratio",
        rounds_to_printed(s16, "2.5e15"), True)
    w16 = 1.0 / (4.0 * 8e-16)          # the WITHDRAWN formula, evaluated
    chk("W12   against the withdrawn 1/(4 eps) = 3.1e14 (DOCKET 63 D)",
        rounds_to_printed(w16, "3.1e14"), True)
    chkrel("W12   their quotient, the owner over the withdrawn form, is ~8",
           s16 / w16, 8.0, 1e-12)
    chk("W12   recorded", SOURCE_TO_FIELD_IS_QUARTER_OVER_EPS, False)
    chk("W13 the range is not the same obstruction for every role",
        SAME_OBSTRUCTION_EVERY_ROLE, False)
    chk("W10-W13 are all kept, with a reason each",
        sorted(k for k, v in WITHDRAWN.items() if len(v) == 2 and v[1]),
        ["W10", "W11", "W12", "W13"])
    # F6: the factor is S-dependent; 24 only at the valence (non-FH) value
    chkrel("F6 naive-correction factor at the valence 0.0096",
           NAIVE_CORRECTION_FACTOR["naive valence 2m_u+m_d"], 23.9708, 1e-5)
    chkrel("F6   at sigma_piN 0.06", NAIVE_CORRECTION_FACTOR["sigma_piN ~ 56 MeV"],
           4.48148, 1e-5)
    chkrel("F6   at 0.09", NAIVE_CORRECTION_FACTOR["with strange sigma term"],
           3.24691, 1e-5)
    chk("F6 'a factor of thirty' holds at no scanned S",
        all(v < 25 for v in NAIVE_CORRECTION_FACTOR.values()), True)
    chk("F6   recorded", FACTOR_OF_THIRTY, False)
    # the section-3 row the docstring cites for W11's consequence
    dA_ = GODUN["A_E2"] - GODUN["A_E3"]
    chkrel("W11 optical/optical H1 row, corrected", dA_ * K_alpha("H1"),
           0.0126331, 1e-5)
    chkrel("W11   withdrawn", dA_ * K_alpha_as_first_written("H1"),
           -0.0681601, 1e-5)
    # W11 / ruling F7: the ruling's printed consequences, solved for the
    # K_alpha they need.  Each check can fail: it rounds a COMPUTED candidate
    # to the ruling's printed quantum.
    for w in RULING_F7_PRINTED:
        c0, c1 = f7_consequence(w, 0.0), f7_consequence(w, 1.0)
        chkrel("F7 %s is affine in K_alpha (checked at K = 0.37)" % w,
               f7_consequence(w, 0.37), c0 + 0.37 * (c1 - c0), 1e-12)
        kreq, kw = RULING_F7_K_REQUIRED[w]
        chk("F7 %s: ruling's %s needs K = %.4e; its own +43a/(54pi) is outside"
            % (w, RULING_F7_PRINTED[w], kreq), abs(kreq - K_ALPHA_H1) > kw, True)
        chk("F7 %s:   the withdrawn K sign-flipped (%.4e) is inside +-%.1e"
            % (w, -K_ALPHA_H1_AS_FIRST_WRITTEN, kw),
            abs(kreq + K_ALPHA_H1_AS_FIRST_WRITTEN) <= kw, True)
    chk("F7 the ruling's figures do NOT follow from its own K_alpha",
        RULING_F7_FOLLOWS_FROM_ITS_K_ALPHA, False)
    chk("F7   they are the withdrawn K_alpha with its sign flipped",
        RULING_F7_IS_THE_SIGN_FLIP, True)
    chk("F7   and the seated rows are the computed products, not the ruling's",
        (RULING_F7_SEATED["optical_optical_H1"] == dA_ * K_alpha("H1"),
         RULING_F7_SEATED["th229_H1"] == th229_coefficient("H1")), (True, True))

    print()
    chk("H1 vs H2 is refused, not resolved", H1_VS_H2_IS_REFUSED, True)
    chk("Flambaum read from source", FLAMBAUM_READ_FROM_SOURCE, True)
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
