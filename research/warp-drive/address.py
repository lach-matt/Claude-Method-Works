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
is seen 23 orders further away (22 at the gravimeter accuracy and 1 s noise
figures; section 6) by an instrument nobody had to invent.

===============================================================================
1. WHAT THE DISPLACEMENT IS SENSITIVE THROUGH, AND THE CHANNEL THAT IS BLIND
===============================================================================

Every charged-fermion mass in the minimal SM is m_f = y_f v / sqrt(2), so
d ln m_f / d ln v = 1 EXACTLY, at tree level and at fixed Yukawa.  alpha =
e^2/4pi hbar c contains no v at all: e = g sin(th_W) is a gauge coupling.  SO AT
TREE LEVEL A DISPLACED VEV MOVES EVERY MASS AND LEAVES alpha ALONE.

    CORRECTED (DOCKET 67).  This first read "Every fermion mass".  Neutrino
    masses lie outside the minimal SM (a Weinberg-operator Majorana mass has
    d ln m/d ln v = 2); none is used here.  Two hypotheses the "EXACTLY"
    carries, NAMED: (a) kappa_f = 1 -- for any m_f(v), d ln m_f/d ln v IS the
    Higgs-coupling modifier kappa_f, and for the electron it is unmeasured:
    |kappa_e| < 260, with SM first-generation values ASSUMED in the LHC fits
    (ATLAS 2207.00092 p.8); (b) the scale at which the Yukawa is fixed, which
    is not named.  Held at a high scale, w = 1/(1+gamma_m) < 1 and K_mu(H1,
    S = 0.06) is -0.752 rather than -0.731 (DOCKET 67, ORDER); the sign holds.

That single fact decides which clock can see it, and it rules OUT the channel a
reader reaches for first.

    An optical transition frequency, in units of the Rydberg, is a pure
    function of alpha: nu_opt / c R_inf = F(alpha).  The electron mass CANCELS.
    So an OPTICAL-TO-OPTICAL frequency RATIO -- among the most precise
    measurements of any physical quantity other than symmetry tests, 3e-16 in
    Godun 2014 -- IS BLIND TO eps THROUGH mu, AT TREE LEVEL, FOR A POINT
    NUCLEUS OF INFINITE MASS.

    CORRECTED (DOCKET 67).  This first said "the sharpest measurement in
    physics ... and heading below 1e-18".  The nearest source wording
    (2512.21428 p.2) keeps "other than symmetry tests".  Single-clock
    systematic budgets READ are below 1e-18 (1.1e-19 to 8.1e-19), but no
    inter-species optical RATIO is yet: best 2.2e-18 (Al+/Sr, 2512.21428).

    THAT IS NOT THIS FILE'S ASSERTION.  It is Godun et al.'s own B_E3 = B_E2 =
    0 -- which they call "negligible", not zero -- READ FROM SOURCE below, and
    it is the control this file must reproduce.

    WITHDRAWN (DOCKET 63, W10).  The first draft said "IS EXACTLY BLIND".  IT
    IS NOT.  Finite nuclear size adds (4/3) Z^4 (r_N/a_0)^2 / n^3 Rydberg to
    every S level, and r_N/a_0 is proportional to m_e r_N, hence to v at tree
    level (H2, r_N held fixed).  For hydrogen nu(1S-2S)/nu(2P-3D), with
    x = r_p/a_0, finite_size_K() derives in sympy K = 28x^2/(14x^2 - 9) =
    -7.87e-10 -- nonzero, same place, alpha fixed.  Kept as
    OPTICAL_OPTICAL_IS_EXACTLY_BLIND = False.

    CORRECTED (DOCKET 67).  This went on: "Recoil terms in m_e/M add more.
    Small; and under H2, where K_alpha = 0, it is the LEADING same-place
    sensitivity."  The non-relativistic reduced mass cancels exactly in a
    same-atom ratio.  The relativistic recoil term -m_r^2 c^2 (f-1)^2/(2M)
    does not -- that formula is RECALLED (Barker-Glover / CODATA), NAMED-NOT-
    READ -- and computed from it under H2 at S = 0.06 it gives K_recoil =
    +6.05e-9 for H(1S-2S)/(2P-3D), 7.7 times K and of opposite sign.  So,
    conditional on that formula, recoil and not finite size is the leading H2
    same-place term.  Either way the ratio is not exactly blind, which is all
    W10 withdraws.

    AND THE BLINDNESS HAS A HYPOTHESIS, WHICH SECTION 7 CASHES: it holds for two
    transitions AT THE SAME PLACE.  Two copies of the SAME optical clock in
    DIFFERENT places do not cancel R_inf, because R_inf = alpha^2 m_e c/2h is
    proportional to m_e at fixed alpha and m_e is proportional to the LOCAL v.
    A TRANSPORTED CLOCK CARRIES COEFFICIENT +1 -- EXACTLY +1 at tree level
    with alpha fixed (H2) and an infinite-mass nucleus -- and it turns out to
    be the best channel here.

    CORRECTED (DOCKET 67).  This first said "COEFFICIENT EXACTLY +1" with
    neither hypothesis.  Under H1's own K_alpha the coefficient is
    1 + (2 + A_opt) K_alpha: 1.0037 at A_opt = 0, 1.0053 for Yb+ E2, 0.9927
    for Yb+ E3; with hydrogen's reduced mass under H2 it is 0.999488
    (computed).  It also needs kappa_e = 1 (above).

The microwave hyperfine splitting does not cancel m_e:

    nu_hf / c R_inf  ~  alpha^2 * g_I * (m_e/m_p) * F_rel(Z alpha)

-- one factor alpha^2 from mu_B mu_N / a_0^3 against the Rydberg, and one
factor (m_e/m_p) from the nuclear magneton.  So the OPTICAL-TO-CESIUM ratio
carries exponent exactly +1 in mu = m_p/m_e and exactly 2 (plus relativistic
corrections) in alpha -- WITH g_I HELD FIXED.  THAT is the channel, and Godun's
6e-16 absolute frequencies are about TWICE their optical ratio's 3e-16 --
CS_CHANNEL_COARSER_BY, the quotient of those two printed figures, is 2.

    HYPOTHESIS, NAMED (DOCKET 67): g_I fixed.  It is Godun's own condition for
    B_Cs = -1 ("the 133Cs nuclear g-factor has negligible sensitivity to
    changes in the strong interaction"), and a displaced vev moves exactly
    that variable, X_q = m_q/Lambda_QCD (7/9 under H1, 1 under H2).  Computed:
    the optical/Cs coefficient moves 1.06% per 0.01 of kappa_Cs, under both;
    kappa_Cs was NOT READ.

    CORRECTED (DOCKET 67).  This first called the 6e-16 "Cs-limited" and the
    factor "TWICE".  Godun p.1 says the absolute frequencies are "limited by
    Cs primary standards"; their Table I/II budget puts most of the variance
    in the Cs-referenced statistics (61% E2, 85% E3), not the Cs fountain
    systematics (~10%).  The 2 divides two one-digit roundings: Table I
    gives 6.13/3.36 = 1.82 (E2) and 5.79/3.36 = 1.72 (E3).  W10's "2, not
    100" holds at every reading.

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

    CORRECTED (DOCKET 67).  "3 to 4.5" is the scan's 0.09 and 0.06 rows, and
    0.06 counts u + d only (S_SCAN).  At current u + d + s sums it is 2.82
    (FLAG 2024 N_f = 2+1+1, S = 0.1086), 2.78 (phenomenological sigma_piN
    plus lattice sigma_s, 0.1108) and 3.17 (FLAG N_f = 2+1, 0.0928).

Lambda_QCD is not independent of v.  One-loop threshold matching across the
charm, bottom and top thresholds, with b_0(n_f) = 11 - 2 n_f/3 and
b_0(n_f - 1) - b_0(n_f) = 2/3 at each, gives EXACTLY

    Lambda_3 = Lambda_6^(7/9) * (m_c m_b m_t)^(2/27)

-- so each heavy quark enters with power 2/27, and since every heavy quark mass
is proportional to v (at one loop it does not matter which mass: matching at
mu = kappa m_Q for any fixed kappa gives the same exponent),

    d ln Lambda_QCD / d ln v  =  3 * 2/27  =  2/9     EXACTLY, AT ONE LOOP

DERIVED IN THIS FILE OVER Fraction, not quoted.

    CORRECTED (DOCKET 67).  This line first read "2/9 EXACTLY" with no order.
    The exactness is the rational arithmetic of the one-loop truncation, not
    the physical derivative: beyond it the value is 0.23006 (NLO), 0.23501
    (NNLO) and 0.23839 (N3LO, Hill-Solon) (DOCKET 67, computed).  Beyond one
    loop "which mass" matters too: Yukawas fixed at a high scale make
    m_Q(m_Q) scale as v^(1/(1 + 2 alpha_s/pi)).  HYPOTHESES the 2/9 carries,
    NAMED: Standard-Model coloured content between m_t and the high scale
    (Coc et al. 2007 footnote 1 -- squark and gluino thresholds would add
    their own steps), and charm treated as a decoupled heavy quark (Hill-
    Solon's f_c = 0.073(3) + O(1/m_c)).

Then by dimensional homogeneity of the QCD part m_p = Lambda f(m_q/Lambda), so
d ln m_p/d ln Lambda = 1 - S with S = sum_q sigma_q/m_p the Feynman-Hellmann
light-quark fraction, summed over u, d AND s (the flavours below Lambda_3), and

    H1  alpha_s FIXED AT A HIGH SCALE:   d ln m_p/d ln v = 2/9 + (7/9) S
    H2  Lambda_QCD ITSELF FIXED:         d ln m_p/d ln v = S

    HYPOTHESES, NAMED (DOCKET 67).  (i) H1's form is the leading-order (SVZ)
    evaluation of the exact sum_{q=u..t} f_q; beyond leading order f(0.06) is
    0.28177 rather than 0.26889, and the (1 - S) factorisation fails at about
    the 2% level.  (ii) QCD only: the electromagnetic part of m_p (about 1e-3
    of it, NAMED-NOT-READ) is dropped here; its v-dependence enters through
    K_alpha, carried separately (W11).  (iii) The light-quark masses are the
    ones held against Lambda; at fixed m_q(2 GeV) the coefficient would be
    1 - S(1 + gamma_m) = 0.9285 rather than 0.9400 at S = 0.06.  This file
    never holds m_q(2 GeV) fixed while Lambda moves.

H1 gives 0.2297 at S = 0.0096 -- TWENTY-FOUR TIMES the naive 0.0096.  Both
hypotheses are named because they are not the same physics; neither is
assumed.  H1 is Coc et al. 2007's Delta alpha = 0 (READ in DOCKET 67).  No H2
statement has been READ: Flambaum's p.4 sentence fits both (see FLAMBAUM).

    CORRECTED (DOCKET 67).  This first printed "0.229" (0.22967 truncated) and
    said both hypotheses are named "because BOTH ARE IN THE LITERATURE".  The
    citation behind H2 does not establish it; Calmet 1707.06922 was found as
    a possible H2-type statement and NOT READ.

What matters is that they agree on the answer:

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
2014's absolute frequencies carry 6e-16, Cs-referenced.  That is eps_det ~
8e-16.  (ratio_sensitivity uses B and K only; Godun's alpha term moves it 2.2%
under H1 and not at all under H2 -- see that function.)

The exact linear-regime energy density of the tree-level SM quartic, with NO
small-eps expansion:

    (V(v(1+eps)) - V_min) / |V_min|  =  eps^2 (2 + eps)^2     EXACT
                                     ->  4 eps^2               as eps -> 0

At eps_det it is of order 1e16 J/m^3, which is large but is INSIDE the range of
energies humans have released, so on the energy measure ADDRESSING LOOKS
AFFORDABLE.

    CORRECTED (DOCKET 67).  This first wrote V(v(1+eps))/|V_min|, which under
    higgs.py's V(0) = 0 is eps^2(2+eps)^2 - 1 (cost_fraction computes the
    difference, correctly), and said "sympy residual of that identity is 0"
    with no sympy code in this file behind it -- the selftest checks
    cost_fraction against its own formula.  The residual IS 0: DOCKET 67
    computed it, and excite.py derives the identity.  HYPOTHESES "EXACT"
    carries, NAMED: the tree-level potential, and SM self-couplings.  Beyond
    4 eps^2 the cost is 4 eps^2 + 4 kappa_lambda eps^3 + kappa_4 eps^4, and
    data bound kappa_lambda only to (-1.2, 7.5), so only the leading 4 eps^2
    is fixed by data -- which is all that is used at eps_det.

IT IS NOT, AND THE ENERGY IS THE WRONG METER.  The displacement has to be
SOURCED.  A fermion background sources the Higgs through its scalar density,
and the static uniform solution of (nabla^2 - m_h^2) dphi = (m_psi/v) n is,
LINEAR AND AT TREE LEVEL,

    eps  =  - rho_H c^2 / (v^2 m_h^2)  =  - rho_H c^2 / (8 |V_min|)

(v^2 m_h^2 = 2 lambda v^4 = 8 |V_min| is an exact identity; the selftest checks
it to 1e-12), with rho_H the HIGGS-DERIVED part of the mass density.  Holding
eps_det therefore takes a source whose rest energy is 8|V_min| eps_det -- and
that is 2/eps_det, some 2.4e15, TIMES the field energy it buys (8/(eps
(2+eps)^2), which source_to_field_ratio() computes and the selftest expands in
sympy).  PRICING ADDRESSING AT ITS FIELD ENERGY UNDERSTATES IT BY FIFTEEN
ORDERS.

    CORRECTED (DOCKET 67).  The source law was marked "EXACT" and the ratio
    "EXACTLY 8/(eps (2+eps)^2)".  The identity is exact; the law is linear and
    tree-level, and the ratio is a linearised source over the nonlinear
    energy, so exact in neither.  The exact uniform ratio for the SM shape is
    4(1+eps)/(eps(2+eps)); both tend to 2/eps, and they differ by 1.2e-15
    relative at eps_det and by a factor 3 at eps = 1.  HYPOTHESES, NAMED:
    (i) tree level -- m_h is the PDG pole mass used as the tree curvature
    V''(v); the uniform static response is set by the zero-momentum
    curvature and the falloff by the pole, which coincide at leading order.
    The loop difference is NOT computed; the margin is: v^2 m_h^2 would have
    to change x114 (H2) or x398 (H1) before a verdict moves.  (ii) psibar psi
    -> n, the nonrelativistic identification of the scalar density (a free
    Fermi gas at n0 has rho_s/rho_B = 0.9774, -2.3%).  (iii) The perturbative
    branch (section 8).

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

lambda_h = hbar/(m_h c) = 1.5770e-18 m -- computed here from higgs.M_HIGGS (the
pole mass, at tree level), and 0.0019 proton radii.  Outside a source, eps(r) =
eps_0 (r_0/r) e^{-(r-r_0)/lam}.

    CORRECTED (DOCKET 67).  The figure first printed was 1.5761e-18 m, the
    withdrawn 125.20 GeV rounding.  And eps_0 here is the INTERIOR value: for
    a uniform sphere with R >> lambda_h the linear sharp-edge solution has
    surface value eps_0/2, so every standoff in this file is long by
    lambda_h ln 2 = 1.09e-18 m -- conservative, in the Higgs's favour.

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

    dphi(x) = -J(x)/m_h^2 + O(J''/m_h^4),   (lambda_h/1 m)^2 = 2.5e-36

(the bound is absolute, |dphi + J/m_h^2| <= |J''|/m_h^4.  CORRECTED (DOCKET
67): the multiplicative form "[1 + O((lambda_h/L)^2)]" first written here fails
where J = 0 but dphi != 0.)

So dphi AT A POINT IS A FUNCTION OF THE MASS DENSITY AT THAT POINT AND NOTHING
ELSE.  There is no integral over the body, no falloff to read a distant source
by, and no way to make the field say anything the local density does not
already say.

    A DISPLACED VEV IS NOT AN ADDRESS.  IT IS A CONTACT-ONLY READOUT OF LOCAL
    MASS DENSITY, CARRYING STRICTLY LESS THAN THE DENSITY ITSELF.

AND NATURE ALREADY RUNS THE EXPERIMENT.  Nuclear matter at saturation density
displaces the vev by eps = -3.27e-13 (H1) or -7.29e-14 (H2) -- 398 or 114 TIMES
eps_det under the SAME hypothesis -- inside every heavy nucleus.  Averaged over
a light nucleus's own support, which is the coarse-grained object section 8
says a rho is, it is less but still over threshold: deuteron 57x (H1) / 16x
(H2), alpha 234x / 67x (CODATA 2022 radii, uniform sphere; DOCKET 67).  The
largest Higgs displacement in the solar system is inside an ordinary atomic
nucleus, over threshold in every nucleus tested and two orders over in heavy
ones, and no measurement outside that nucleus has ever registered it.

    CORRECTED (DOCKET 67).  This first applied "398 or 114 TIMES" to
    "everywhere there is a nucleus" and called it "two orders over threshold"
    without scope: n0 is the interior density of infinite symmetric matter.
    Under H2 "two orders" holds only for n0 >= 0.1401 fm^-3.  The figures
    above use S = 0.06, u + d only (S_SCAN); at S = 0.09 eps is -3.55e-13 (H1).

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
pull exceeds a 1e-9 m/s^2 gravimeter floor out to 1.4e7 m (H1) or 2.6e7 m (H2)
-- a field-strength radius (1.4e7 m exceeds Earth's diameter, 1.274e7 m), not a
terrestrial baseline.

    HYPOTHESES, NAMED (DOCKET 67; Freier et al. 1512.05660 READ).  1e-9 m/s^2
    is a relative long-term STABILITY figure (an Allan deviation reached at
    ~1e5 s); absolute accuracy is 3.9e-8 and 1 s noise 9.6e-8, and below
    ~1e-8 background models alone do not suffice.  So a static source is
    read at 1e-9 only by modulation or differencing integrated over ~1e4-1e5
    s.  A gravimeter reads one vertical axis; for surface geometry the
    vertical component at the antipode is still 1.16e-9 (H1) / 4.03e-9 (H2).
    At the accuracy and 1 s noise readings r/d is 4.0e22 / 7.4e22 and
    2.6e22 / 4.7e22 (H1 / H2): "more than twenty orders" holds at every
    reading, 23 orders only at the stability floor.

    ROLE 1 IS NOT MERELY EXPENSIVE.  IT IS STRICTLY DOMINATED, BY MORE THAN
    TWENTY ORDERS OF MAGNITUDE, BY AN INSTRUMENT THAT ALREADY EXISTS AND READS
    THE SAME SOURCE -- BECAUSE GRAVITY IS UNSCREENED AT THESE RANGES AND THE
    HIGGS IS NOT.

    CORRECTED (DOCKET 67).  The last clause first read "BECAUSE THE GRAVITON
    IS MASSLESS".  Masslessness is GR's postulate; the data give an upper
    bound, m_g < 1.76e-23 eV (PDG), which moves no figure here (a field
    deficit ~2.6e-18 at 2.6e7 m).

===============================================================================
7. THE PROBE ROUTE -- THE BEST CHANNEL, AND IT STILL FAILS, ON THE SOURCE
===============================================================================

Send something in and bring it back, so the field never has to reach the
observer.  THERE ARE TWO PROBES AND THEY FAIL DIFFERENTLY.

A PROBE THAT MUST RESOLVE THE REGION.  If the displaced region is no bigger
than lambda_h, the probe needs de Broglie wavelength <= lambda_h, so p >= m_h c
and E >= m_h c^2.  Its sensitivity is its rest-mass dependence, and that is

    d ln E / d ln m  =  (m c^2/E)^2       EXACT (sympy residual 0)

For an electron that ceiling is (m_e/m_h)^2 = 1.6677e-11, AT eps = 1.  Against
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

    d ln(nu_in/nu_out) / d eps  =  +1       (tree level, alpha fixed, infinite
                                             nuclear mass, kappa_e = 1)

THE BEST COEFFICIENT ANYWHERE IN THIS FILE (1.0037, 1.0053 or 0.9927 under H1,
0.999488 with hydrogen's reduced mass -- section 1), and at a 1e-18 clock
comparison it gives eps_det = 1e-18 -- three orders better than the stationary
channel.  ROLE 1's ONE SURVIVING ROUTE IS A COURIER, NOT A SIGNAL.

    CORRECTED (DOCKET 67).  The coefficient was printed "+1 EXACTLY".  And the
    1e-18 is an ORDER for a stationary electronic clock comparison: a clock
    CARRIED across a boundary is a different measurement, every sub-1e-18
    figure READ is stationary and in-lab, and the best transportable figure
    seen is 2.1e-18 systematic (2507.14030, abstract only).

IT DIES ON THE SOURCE, NOT ON THE DETECTOR.  A clock needs a bound atomic
transition, so the region must be at least a Bohr radius across -- 3.36e7
screening lengths -- and by section 5 the displacement is ultralocal, so the
source must FILL it.  eps = 1e-18 across an atom takes

    8.19e11 kg/m^3 (H1)  to  3.67e12 kg/m^3 (H2),
    3.63e7 to 1.62e8 times the density of osmium

(the first draft gave only the H2 figure; DOCKET 63 F5.  DOCKET 67: these two
lines first printed 8.20e11 and 1.63e8, withdrawn-125.20 roundings.)

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
under H1 and exactly 1 under H2 -- HYPOTHESIS, NAMED: they move together, where
Flambaum keeps them independent; under it the two terms partly cancel (0.5 - 5)
and the X_s term carries 91% of the coefficient -- so the coefficient of eps is
about -3.5e5 at the review's normalisation w = 7 eV, and at AN ASSUMED 1e-18
NUCLEAR-CLOCK ACCURACY

    eps_det(Th-229 courier)  ~  3e-24        -- EIGHT ORDERS BETTER, IF SUCH A
                                                CLOCK EXISTED

(2.86e-24 under H1 at 7 eV with the corrected K_alpha of section 11 --
three figures of arithmetic on a "rough estimate", not of physics; the first
draft's 2.84e-24 carried the withdrawn K_alpha)

    CORRECTED (DOCKET 67).  This first printed "2.9e-24 -- EIGHT ORDERS
    BETTER" unqualified.  Three things it carried unflagged.  (i) The 1e-18
    is the electronic-clock ORDER applied to a nuclear clock: the READ
    Th-229 state is nu_Th/nu_Sr to 1.06e-12 with systematics unevaluated
    (2406.18719 p.8), and at that precision eps_det(Th-229) = 3.0e-18, no
    better than the electronic courier.  The ORDER label was on the
    coefficient, not on the accuracy.  (ii) The transition is now measured
    at 8.355733554 eV (Beeks 2407.17300), so (7 eV/w) = 0.8377, not 1: at the
    measured w the H1 coefficient is -2.929e5 and eps_det 3.41e-24.
    TH229_OMEGA_EV stays 7.0 so the pins below are the review's.  (iii) The
    X_q and X_s coefficients are unmeasured and contested (Flambaum-Wiringa
    0807.4943 is 3.3x higher on X_q; no later X_s computation found); a
    strong enhancement of ~1e4 would raise eps_det 10x.

This is the best number in the file by a wide margin and it is NOT dismissed.
It does not save Role 1, and the reason is section 9, not a budget.

(Flambaum calls his own figure "a rough estimate"; it is carried as ORDER, and
section 9's verdict does not depend on its value -- now COMPUTED, DOCKET 67:
domination_ratio stays finite and above 1e20 (2.8e20 to 5.6e35) for eps_det
from 2.86e-25 to 1e-16, which spans the measured w and enhancements 1e3-1e6.)

A NECESSARY HYPOTHESIS, STATED: eps = -rho c^2/(8|V_min|) is a COARSE-GRAINED
statement.  lambda_h is 1.6 attometres and no matter is uniform at that scale --
nucleons are 1.8 fm apart, so e^{-d/lambda_h} between two of them is about
1e-496.  The formula is right for what a bound electron or a nucleus SAMPLES,
which is the mean density over its own support, and it is NOT the pointwise
field.  Every rho in this file is a coarse-grained mean and is used only where
that is the right object.

A SECOND NECESSARY HYPOTHESIS, NAMED BY DOCKET 67: the static solution used is
the PERTURBATIVE BRANCH.  eps << 1 does not by itself exclude others.  Shi
2107.04206 (a real Z2 phi^4, source held fixed) has more than one finite-energy
static configuration above a critical source; with this file's H1 f that is a
uniform 1 m sphere at rho of order 1e12 kg/m^3 (8.8e11 and 2.6e12 in two
DOCKET 67 audits), where eps ~ 1e-18 -- inside the 1 m sources of sections 6
and 9, far from nuclear matter (margin 4.7e8) and from the atom-scale courier
(4.5e9).  It is contested for the SM doublet (Shi p.14: a toy model).  If it
applied, the Higgs reach would scale as R sqrt(ln), not lambda_h ln rho, and
gravity would still out-read it by ~1e6-1e10 (order of magnitude).

===============================================================================
9. THE DOMINATION THEOREM.  GROWING THE SOURCE MAKES IT WORSE
===============================================================================

Put a source of mean density rho in a sphere of radius R.

    HIGGS RANGE      d  =  lambda_h ln(eps_0/eps_det),  eps_0 proportional to rho
                        so  d  grows as  ln rho
    NEWTON RANGE     r  =  sqrt(G M/a_floor),  M proportional to rho
                        so  r  grows as  sqrt(rho)

    THEOREM.  r/d goes as sqrt(rho)/ln(rho).  NO SOURCE STRENGTH CLOSES THE
    GAP, AND ABOVE e^2 TIMES THRESHOLD EVERY INCREASE IN THE SOURCE WIDENS IT.

That is not a comparison of two numbers, which could be argued about.  It is a
comparison of two FUNCTIONS.  The Higgs is massive and gravity, at these
ranges, is unscreened, and in linear exchange a massive field's reach is
logarithmic in its source while a massless field's is a power.  (Screening by
other than mass -- Debye, Vainshtein, chameleon -- is not this; gravity with
positive mass has no Debye screening.)

    CORRECTED (DOCKET 67).  The theorem first read "r/d grows without bound
    ... AND EVERY INCREASE IN THE SOURCE WIDENS IT", and this paragraph "it
    is monotone".  d/drho [sqrt(rho)/ln(B rho)] has the sign of ln(B rho) - 2,
    so r/d FALLS while eps_det < eps_0 < e^2 eps_det: domination_ratio gives
    1.82e24 at 9.83e11 and 4.78e23 at 2.46e12 kg/m^3 (eps_det = 1e-18), and
    at the Th-229 eps_det a minimum of 6.97e20 at 7.389 x threshold.  The
    decade grids of the report and selftest step over the dip.  "Without
    bound" is the formula's, on two hypotheses: m_g = 0 exactly -- for any
    graviton mass allowed (m_g < 1.76e-23 eV) both reaches are logarithmic
    and r/d tends to lambda_g/lambda_h = 7.1e33, bounded and still dominating
    -- and rho unbounded at fixed R, which a static 1 m sphere is not: it
    collapses near 1.6e26 kg/m^3 (Buchdahl's 8/9 near 1.4e26), where r/d is
    ~1e29, and in strong field the Newtonian range only under-reads.  The
    verdict uses r/d >> 1 alone, which holds through the window: minimum
    4.12e23 from threshold to collapse at eps_det = 1e-18.

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
declared values, from the naive valence sum to 0.09.  It is a SCAN, not a
measurement, and no sign, order or status conclusion here turns on it;
magnitudes do.

    CORRECTED (DOCKET 67).  This first said the three values span "the
    lattice sigma-term range".  They do not reach current u + d + s sums: 0.09
    covers FLAG 2024 N_f = 2+1 (0.0928), not N_f = 2+1+1 (0.1086) nor
    phenomenological sigma_piN plus lattice sigma_s (0.1108).  And the middle
    row counts u + d only (S_SCAN).  Tested over S in [0.0096, 0.12], no sign,
    order or status moves.

TO QUOTE A CODATA UNCERTAINTY.  m_p/m_e is measured to ~1e-11; that is NAMED-
NOT-READ and it is not used, because the clock channel beats it by 10^4.5 and
the argument does not need it.

TO PRICE THE NONLINEAR REGIME.  A bubble -- of the true vacuum below ours,
or a region held at phi = 0, which is a spinodal maximum and not a false
vacuum -- is not this file's subject.  (The first draft said "a false-vacuum
bubble", which names neither; DOCKET 63 F8/F10.)  Role 1 needs only detectability, and detectability fails inside the
linear regime, which is the stronger place to fail.

TO CALL PRESSURE IONISATION A MEASUREMENT.  Section 7's closing clause -- that
no bound optical transition survives at 8.19e11 to 3.67e12 kg/m^3 -- is a
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
       sympy).  DOCKET 67: "one loop" is one loop in QED, and the 43/54 is
       exact only within the hypotheses alpha_thresholds() and K_alpha() now
       name (SM-only charged content; perturbative b at the hadronic u, d, s
       thresholds, which carry 16/43 of it).  Its SIGN survives every bracket
       DOCKET 67 tried.  Consequences, computed: the Th-229 H1 coefficient moves from
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

===============================================================================
12. DOCKET 67: WORDING CORRECTED IN PLACE, NO VERDICT MOVED
===============================================================================

On M's ruling "Repair all" for DOCKET 67's wording findings, each site above
marked "CORRECTED (DOCKET 67)" or "NAMED (DOCKET 67)" keeps what it first said.
No constant, flag, pin or computed figure changed; the docstring figures that
still carried the withdrawn m_h = 125.20 roundings now print the computed ones.
"""

import math
import sys
from decimal import Decimal
from fractions import Fraction

import higgs

# --------------------------------------------------------------- imported, not copied
V_GEV = higgs.vev()        # (sqrt2 G_F)^(-1/2): the tree-level/on-shell v.  The
                           # MS-bar v is 0.155% higher (DOCKET 67; moves v^2
                           # figures 3.1e-3, no verdict).
M_HIGGS = higgs.M_HIGGS    # the PDG pole mass, used here as the tree curvature
LAMBDA_QUARTIC = higgs.lam()   # imported; used nowhere in this file (DOCKET 67)
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
#   DOCKET 67, recorded and not reconciled: m_N here is m_p (n_0 m_p to 4
#   digits).  The tree's other nuclear density is 2.3e17 (n_0 = 0.1375;
#   warpdrive.py, emwarp.py, drivespec.py, mouth.py), 16% lower; at 2.3e17
#   the section 5 ratios are 342x (H1) and 98.2x (H2).
GRAVIMETER_FLOOR = 1.0e-9        # m/s^2, ~0.1 microGal             ORDER
#   DOCKET 67 (Freier et al. 1512.05660 READ): at source 1e-9 is a RELATIVE
#   long-term stability figure (~1e5 s Allan deviation).  Absolute accuracy is
#   3.9e-8 and 1 s noise 9.6e-8.  Used here as an instantaneous threshold for
#   a static source, which needs modulation or differencing (section 6).

#: Godun et al., PRL 113, 210801 (2014) = arXiv:1407.0164v2.  READ FROM SOURCE.
#: p.4: "r_dot/r = (A_1 - A_2) alpha_dot/alpha + (B_1 - B_2) mu_dot/mu.  The
#: sensitivity coefficients A_i ... are: A_E3 = -5.95, A_E2 = 0.88, A_Cs = 2.83.
#: Dependence on mu_dot arises through the nuclear magnetic moment and is
#: negligible for optical transitions (the sensitivity coefficient
#: B_E3 = B_E2 = 0).  As the 133Cs nuclear g-factor has negligible
#: sensitivity to changes in the strong interaction [37, 38], an AFM history
#: can also be interpreted to set constraints on mu_dot/mu (B_Cs = -1)."
#: Their mu is m_p/m_e.  CORRECTED (DOCKET 67): this quote first cut, with
#: "...", the g-factor sentence -- the condition B_Cs = -1 rests on, and the
#: one a displaced vev violates by moving X_q (section 1, g_I fixed).
GODUN = {"A_E3": -5.95, "A_E2": 0.88, "A_Cs": 2.83,
         "B_E3": 0.0, "B_E2": 0.0, "B_Cs": -1.0}
GODUN_RATIO_UNC = 3.0e-16        # "fractional uncertainty 3 x 10^-16", p.1
GODUN_ABS_UNC = 6.0e-16          # "relative standard uncertainty of 6 x 10^-16"
GODUN_READ_FROM_SOURCE = True

#: Flambaum, arXiv:0705.3704v2 p.4, READ FROM SOURCE: "The proton mass is
#: proportional to Lambda_QCD (M_p ~ 3 Lambda_QCD)".  It holds under H1 and H2
#: alike: m_p = Lambda F(m_q/Lambda) is common to both, and Lambda_3 itself
#: moves at 2/9 under H1.  CORRECTED (DOCKET 67): this comment first ended
#: "-- this project's H2".  The sentence does not say Lambda is fixed as v
#: varies; Flambaum's "Lambda_QCD constant" is a units convention.  The "3"
#: is used nowhere in this file.
FLAMBAUM_READ_FROM_SOURCE = True

#: The light-quark fraction S = sum_q sigma_q/m_p, q = u, d, s.  A scanned
#: input (ORDER), not a measurement.  (label, value)
#: DOCKET 67: the middle row is sigma_piN/m_p, u + d only -- 56 MeV is the
#: phenomenological value in the neutral-pion convention (59.1 - 3.1;
#: 2412.13138 p.1), not Hoferichter's 59.1 -- so it drops sigma_s, which S's
#: own definition includes.  Only the 0.09 row carries strange, and beside 56
#: MeV it implies sigma_s = 28 MeV, below FLAG 2024's 41.0 / 44.9.  The labels
#: are kept: they are keys the selftest and excite.py read.
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
    """Sum of the heavy-quark exponents: every heavy mass is proportional to v.

    EXACT as the one-loop rational (2/9 for all three); not the physical
    derivative, which is 0.23006 / 0.23501 / 0.23839 at NLO / NNLO / N3LO
    (DOCKET 67).  Every consumer below inherits the one-loop qualifier."""
    _, e = _lambda_exponent_direct(n_heavy)
    return sum(e.values())


def dln_mp_dln_v(S, hypothesis):
    """d ln m_p / d ln v.  S = sum_q sigma_q/m_p (Feynman-Hellmann, q = u,d,s).

    H1 is the leading-order (SVZ, one-loop 2/9) evaluation of the exact
    sum_{q=u..t} f_q; beyond it f(0.06) = 0.28177, not 0.26889 (DOCKET 67)."""
    if hypothesis == "H1":
        return dln_lambda_dln_v() * (1 - S) + S
    if hypothesis == "H2":
        return S
    raise ValueError(hypothesis)


def K_mu(S, hypothesis):
    """d ln(m_p/m_e) / d ln v.  Subtracts d ln m_e/d ln v = 1.

    HYPOTHESIS, NAMED: kappa_e = 1 -- the exponent IS the electron's Higgs-
    coupling modifier, set to its tree-level SM value; it is unmeasured
    (|kappa_e| < 260) and K_mu moves one-for-one with it.  CORRECTED (DOCKET
    67): this docstring first read "m_e is 100% Higgs, so subtract exactly 1"."""
    return dln_mp_dln_v(S, hypothesis) - 1


#: One-loop QED coefficients: above its threshold a species drives
#: d(1/alpha)/d ln mu = -b/(2 pi).  READ-VIA-RESTATEMENT (DOCKET 67) for 4/3
#: and for the sum -7; the split -22/3 + 1/3 is NAMED-NOT-READ.
#: CORRECTED (DOCKET 67, on M's ruling "ok, update").  First labelled
#: "Standard textbook values, NAMED-NOT-READ".  The textbook derivations were
#: not read; two later sources restating them were (audit key
#: qed-one-loop-beta-coefficients, read_status READ-VIA-RESTATEMENT): PDG 2024
#: Review 10 eq.(10.13), MS-bar, whose -(7/4) ln(MZ^2/MW^2) carries b_W = -7;
#: and Buttazzo et al. 1307.3536 App. B.1 eqs.(96)-(97), b_1 = 41/10, b_2 =
#: -19/6.  Neither prints '4/3' literally: 4/3 per unit N_c Q^2 follows from
#: the two together by an exact sum rule (the audit's check C5).  The split
#: -22/3 + 1/3 is printed in neither, and only its sum enters this file.  The
#: scheme is not named here: the MS-bar matching constants dropped are pure
#: numbers with no mass ratio, so at one loop they do not enter d/d ln v
#: (argued, not machine-checked).
B_DIRAC_UNIT_CHARGE = Fraction(4, 3)                 # a Dirac fermion, Q = 1
B_W_BOSON = Fraction(-22, 3) + Fraction(1, 3)        # W+- and its Goldstone: -7
QED_COEFFICIENT_STATUS = {
    "b = 4/3 per unit-charge Dirac fermion": "READ-VIA-RESTATEMENT",
    "b_W = -7 (the sum)": "READ-VIA-RESTATEMENT",
    "b_W split -22/3 + 1/3": "NAMED-NOT-READ",
}


def alpha_thresholds():
    """[(name, b_i, w_i)] for every charged threshold, w_i = d ln m_i/d ln v.

    w = 1 for a mass proportional to v (leptons, c, b, t, and m_W = g v/2;
    kappa = 1, tree level);
    w = 2/9 (one loop) for a light quark whose threshold is hadronic, i.e.
    Lambda_QCD.  EXACT RATIONALS of that model.

    HYPOTHESES, NAMED (DOCKET 67): SM-only charged content between these
    thresholds and the high scale (any other charged species adds b_i w_i/2);
    that a hadronic QED threshold scales as Lambda_3 rather than as a hadron
    mass (which carries the (1 - S) + S mix of dln_mp_dln_v); and the
    perturbative b = (4/3) N_c Q^2 at it, an implicit chiral limit (the u, d,
    s current masses, themselves proportional to v under H1, negligible in
    the hadronic vacuum polarization, which PDG treats as non-perturbative
    and data-driven).  The u, d, s rows carry 16/43 of the 43/54.  Brackets,
    not measurements: w = 0 gives 1/2, w_s = 1 gives 157/162, a pion-like
    11/18 for all three gives 71/54; the sign holds in each.
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
    H1 (alpha fixed at a high scale): +43 alpha/(54 pi) at one loop IN QED,
    with the W threshold, under alpha_thresholds()'s named hypotheses
    (SM-only charged content; O(alpha_s) quark corrections not included).  CORRECTED (DOCKET 63, W11): the first version returned
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
    """d ln(nu_1/nu_2) / d ln v for a clock pair, using B and K only.

    Drops Godun's (A_1 - A_2) K_alpha term (DOCKET 67).  Exact under H2
    (K_alpha = 0).  Under H1 it moves the E3/Cs sensitivity -0.7311 ->
    -0.7474 and eps_det 8.21e-16 -> 8.03e-16 (2.2%); for E2/Cs, 0.5%."""
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
    """(V(v(1+eps)) - V_min)/|V_min| = eps^2 (2+eps)^2, EXACT for the
    tree-level SM quartic.  No small-eps expansion.  CORRECTED (DOCKET 67):
    first written V(v(1+eps))/|V_min|, which under higgs.py's V(0) = 0 is
    this minus 1; the code always computed the difference."""
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

    8/(|eps| (2+eps)^2), which tends to 2/|eps| -- the linearised source over
    the nonlinear energy.  The exact uniform ratio for the SM shape is
    4(1+eps)/(eps(2+eps)): equal to 1.2e-15 relative at eps_det, a factor 3
    apart at eps = 1.  CORRECTED (DOCKET 67): first called "EXACTLY".
    CORRECTED (DOCKET 63,
    W12): this docstring and section 3 first said 1/(4 eps) -- a factor of 8
    below the ratio this function has always returned."""
    return (8.0 * VMIN_SI * abs(eps)) / energy_density(eps)


# ===================================================================== section 4
def yukawa_range():
    """lambda_h = hbar/(m_h c), metres.  From higgs.M_HIGGS, not retyped.
    m_h is the pole mass, taken as the tree curvature V''(v) (tree level)."""
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

    eps_0 is taken at the surface.  For a uniform sphere with R >> lambda_h the
    linear sharp-edge exterior starts at eps_0/2, so d is long by lambda_h ln 2
    = 1.09e-18 m -- conservative, in the Higgs's favour (DOCKET 67).
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
    """r where GM/r^2 falls to the gravimeter floor.

    The floor is treated as an instantaneous absolute threshold for a static
    source; at source 1e-9 is a ~1e5 s stability figure (GRAVIMETER_FLOOR,
    section 6).  Exterior formula: valid for r >= R; it holds at every point
    used here (809 m at threshold, 1.37e7 m, 2.56e7 m; DOCKET 67)."""
    return math.sqrt(G * mass_kg / floor)


# ===================================================================== section 7
def dlnE_dlnm(m_kg, p_si):
    """(m c^2/E)^2 -- the exact probe sensitivity AND the source efficiency."""
    E = math.sqrt((p_si * C) ** 2 + (m_kg * C ** 2) ** 2)
    return (m_kg * C ** 2 / E) ** 2


def B_transported_optical():
    """Coefficient of eps for the SAME optical clock read in two places.

    nu_opt ~ c R_inf F(alpha) and R_inf ~ alpha^2 m_e ~ v at fixed alpha, so
    the ratio of a clock inside the displaced region to its twin outside is
    (1 + eps).  +1 at tree level, alpha fixed (H2), infinite nuclear mass and
    kappa_e = 1 -- R_inf cancels between two TRANSITIONS, never between two
    PLACES.  Under H1's K_alpha it is 1 + (2 + A_opt) K_alpha (1.0037,
    1.0053, 0.9927); with hydrogen's reduced mass under H2, 0.999488.
    CORRECTED (DOCKET 67): first called "EXACTLY +1".  The function returns
    the tree-level value.
    """
    return 1.0


def eps_detectable_transported(frac_accuracy):
    """Threshold for the courier channel.  Coefficient 1 at tree level."""
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
TH229_COEFFS = {"alpha": 2.0, "X_q": 0.5, "X_s": -5.0}   # X_q, X_s unmeasured
                                     # and contested (DOCKET 67); X_s carries
                                     # 91% of the coefficient here
TH229_OMEGA_EV = 7.0                 # the review's own normalisation.  The
                                     # transition is MEASURED at 8.355733554
                                     # eV (Beeks 2407.17300): (7 eV/w) =
                                     # 0.8377, not 1.  Kept at 7.0 so the pins
                                     # are the review's (DOCKET 67).
TH229_IS_ORDER = True                # the COEFFICIENT is ORDER.  The 1e-18
                                     # accuracy applied to it below is the
                                     # electronic-clock ORDER, not a nuclear-
                                     # clock state (READ: 1.06e-12).


def dln_X_dln_v(hypothesis):
    """d ln(m_q/Lambda_QCD)/d ln v.  Same for X_s: both quark masses go as v.
    H1 uses the one-loop 2/9; X_q and X_s moving together is this file's
    hypothesis, not Flambaum's (DOCKET 67)."""
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
    """Standoff outside a source of mean density rho.  Grows as ln(rho) on the
    perturbative branch (section 8).  Starts the tail at eps0, not the
    sharp-edge eps0/2: long by lambda_h ln 2, conservative (DOCKET 67)."""
    eps0 = abs(eps_from_matter(rho_total, higgs_fraction))
    if eps0 <= eps_det:
        return 0.0
    return yukawa_range() * math.log(eps0 / eps_det)


def newton_range(rho_total, R, floor=GRAVIMETER_FLOOR):
    """Range of a gravimeter on the same sphere.  Grows as sqrt(rho).
    Exterior, weak-field formula; see gravimetric_radius."""
    M = rho_total * 4.0 / 3.0 * math.pi * R ** 3
    return gravimetric_radius(M, floor)


def domination_ratio(rho_total, R, higgs_fraction, eps_det):
    """newton_range / higgs_range.  As a formula it diverges for m_g = 0 and
    rho unbounded; it is not monotone just above threshold (minimum at
    eps_0 = e^2 eps_det), and a static R = 1 m sphere collapses near 1.6e26
    kg/m^3.  CORRECTED (DOCKET 67): first "The theorem says this diverges"."""
    d = higgs_range(rho_total, higgs_fraction, eps_det)
    if d <= 0.0:
        return float("inf")
    return newton_range(rho_total, R) / d


# ===================================================================== DOCKET 63
def higgs_fraction(S, hypothesis):
    """The Higgs-derived fraction of a nucleon's mass, f = d ln m_p/d ln v.

    S under H2; 2/9 + 7S/9 under H1 -- leading order, one loop (beyond it
    0.28177 at S = 0.06; DOCKET 67).  DOCKET 63 F5: the first draft used f = S
    everywhere, which is H2 only.  (Electrons, 100% Higgs, add m_e/m_N ~ 5e-4
    of the mass and are neglected here as they always were.)"""
    return float(dln_mp_dln_v(S, hypothesis))


HYPOTHESES = ("H1", "H2")


def eps_det_stationary(hypothesis, S=None):
    """The adopted optical/Cs threshold at Godun's 6e-16 absolute accuracy
    (Cs-referenced; most of its variance is Cs-referenced statistics), using
    B and K only -- ratio_sensitivity drops the K_alpha term (2.2% under H1).
    DOCKET 67: first described as "Cs-limited"."""
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
    recoil (m_e/M) omitted.  Z = 1.  CORRECTED (DOCKET 67): this first said
    recoil "only adds".  The non-relativistic reduced mass cancels in this
    ratio; the relativistic recoil term (RECALLED, NAMED-NOT-READ) does not,
    and computed from it K_recoil = +6.05e-9, opposite in sign to this K and
    7.7 times it.
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
#: DOCKET 67: at S = 0.06 (u + d only; S_SCAN), with H1's LO SVZ fraction.  H2
#: (f = S) has no READ support as a Higgs-nucleon coupling -- Cline 1306.4710
#: supports SVZ (f_N = 0.30) -- and is carried because the file refuses to
#: choose.  Saturation density: heavy-nucleus interiors (section 5).
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
    print(" 10. the Th-229 loophole, computed rather than dismissed -- at an")
    print("     ASSUMED 1e-18 nuclear-clock accuracy (READ state: 1.06e-12)")
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
    print("      ON THIS GRID THE LAST COLUMN RISES.  Between grid points just")
    print("      above threshold it dips (r/d falls until eps_0 = e^2 eps_det,")
    print("      section 9); it never approaches 1.  No source strength closes it.")
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
    print("  %.0f (H1) or %.0f (H2) times over threshold in a heavy nucleus,"
          % (EPS_NUCLEAR_OVER_DET["H1"], EPS_NUCLEAR_OVER_DET["H2"]))
    print("  over it in every nucleus tested, and nothing outside the nucleus")
    print("  sees it; and the one source that would work is read by an ordinary")
    print("  gravimeter twenty-three orders further out (at the 1e-9 stability")
    print("  floor; twenty-two at its accuracy).  A Th-229 courier at an assumed")
    print("  1e-18 would be eight orders better than the stationary channel and")
    print("  changes nothing, because the gap it must close goes as")
    print("  sqrt(rho)/ln(rho) and stays above 1e20.  REFUTED, NOT PRICED.")
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
    chk("d ln Lambda/d ln v = 2/9 EXACTLY at one loop", dln_lambda_dln_v(),
        Fraction(2, 9))
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
    # DOCKET 67: the QED coefficients' status follows what was READ; only the
    # W split (which never enters a figure) stays NAMED-NOT-READ.
    chk("QED 4/3 and the sum -7 are READ-VIA-RESTATEMENT; the split is not",
        sorted(QED_COEFFICIENT_STATUS.values()),
        ["NAMED-NOT-READ", "READ-VIA-RESTATEMENT", "READ-VIA-RESTATEMENT"])
    chk("  and the coefficients those statuses label are 4/3 and -7",
        (B_DIRAC_UNIT_CHARGE, B_W_BOSON), (Fraction(4, 3), Fraction(-7)))
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
    # M's ruling switched m_h to the READ 125.13 (DOCKET 63 F2).  Every m_h fixture
    # below KEEPS its original literal, pinned at the withdrawn 125.20, and expects
    # it times MH**k, k the power of m_h the figure carries -- so the check still
    # fails if anything but m_h moved, or if the power is wrong.
    MH = (higgs.M_HIGGS / higgs.M_HIGGS_PIN_WITHDRAWN)
    chkrel("lambda_h", lam, 1.576094e-18 * MH ** -1, 1e-6)
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
    chkrel("  by, under H1", abs(EPS_NUCLEAR["H1"]), 3.26359e-13 * MH ** -2, 1e-5)
    chkrel("  by, under H2 (the first draft's only figure)",
           abs(EPS_NUCLEAR["H2"]), 7.28239e-14 * MH ** -2, 1e-5)
    chkrel("  times eps_det, both under H1", EPS_NUCLEAR_OVER_DET["H1"],
           397.674 * MH ** -2, 1e-5)
    chkrel("  times eps_det, both under H2", EPS_NUCLEAR_OVER_DET["H2"],
           114.091 * MH ** -2, 1e-5)
    chkrel("WITHDRAWN 'about NINETY': H2's fraction over H1's threshold",
           EPS_NUCLEAR_OVER_DET_AS_FIRST_WRITTEN, 88.737 * MH ** -2, 1e-4)
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
    for hyp, want in (("H1", 1.371597e7 * MH), ("H2", 2.560737e7 * MH)):
        ed = eps_det_stationary(hyp)
        rho_tot, _ = source_density(ed, higgs_fraction(S_mid, hyp))
        rg = gravimetric_radius(rho_tot * 4.0 / 3.0 * math.pi)
        chkrel("the threshold 1 m source is read by gravity to (%s)" % hyp,
               rg, want, 1e-5)
        # DOCKET 67: holds at the 1e-9 STABILITY floor only; at the READ
        # accuracy (3.9e-8) and 1 s noise (9.6e-8) r/d is 4.0e22 / 2.6e22 (H1).
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
    # instrument refused it.  (m_e/m_h)^2 = (0.511/125200)^2 = 1.6658e-11 at the
    # withdrawn 125.20; the fixture is scaled by MH**-2 to the READ 125.13,
    # 1.6677e-11.
    chkrel("an electron resolving lambda_h", ceil_e, 1.665833e-11 * MH ** -2, 1e-5)
    chkrel("  which is exactly (m_e/m_h)^2", ceil_e,
           (M_E_MEV / (M_HIGGS * 1e3)) ** 2, 1e-4)
    chk("so it is ABOVE the best clock ratio, and the probe is not dead here",
        ceil_e > GODUN_RATIO_UNC, True)
    eps_probe = GODUN_RATIO_UNC / ceil_e
    chkrel("  it needs eps >=", eps_probe, 1.80090e-5 * MH ** 2, 1e-4)
    for hyp, want in (("H1", 5.518163e7 * MH ** 4), ("H2", 2.472955e8 * MH ** 4)):
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
           8.19956e11 * MH ** 2, 1e-5)
    chkrel("  and under H2 (the first draft's only figure)",
           COURIER_SOURCE_KG_M3["H2"], 3.6746e12 * MH ** 2, 1e-4)
    chkrel("  H1 times the density of osmium",
           COURIER_SOURCE_KG_M3["H1"] / 22590.0, 3.62973e7 * MH ** 2, 1e-5)
    chkrel("  H2 times the density of osmium",
           COURIER_SOURCE_KG_M3["H2"] / 22590.0, 1.6267e8 * MH ** 2, 1e-4)
    chkrel("  the Higgs-derived part is 2.204772e11 under both (DOCKET 63 A.5)",
           source_density(1e-18, 1.0)[1], 2.204772e11 * MH ** 2, 1e-6)
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
    # DOCKET 67: at an ASSUMED 1e-18 and the review's 7 eV; 3.41e-24 at the
    # measured 8.3557 eV, 3.0e-18 at the READ clock state (1.06e-12).
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
    # DOCKET 67: true on this decade grid, which steps over the dip between
    # threshold and e^2 x threshold (minimum 6.97e20 at 7.389 x threshold).
    chk("AND ON THE DECADE GRID IT IS INCREASING IN rho",
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
