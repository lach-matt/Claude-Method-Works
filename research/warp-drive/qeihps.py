#!/usr/bin/env python3
r"""
qeihps.py -- DOCKET 64 LINE 3: A QUANTUM ENERGY INEQUALITY ON THE HOCHBERG-
POPOV-SUSHKOV SELF-CONSISTENT WORMHOLE.  THE DOCKET 62 INSTRUMENT (FEWSTER-SMITH)
IS REFUSED ON HYPOTHESIS FOR HPS's FIELD; THE TWO QEIs KONTOU NAMES (FO Thm 4.2,
FFKP Thm IV.1) ARE REFUSED ON HPS's STATE AS PUBLISHED -- BOTH HOLD ONLY FOR
HADAMARD STATES AND HPS's IS NOT ESTABLISHED HADAMARD -- AND WERE IT HADAMARD
THEY WOULD STILL BE UNEVALUABLE (OPEN); WHAT CAN BE COMPUTED EXACTLY IS
COMPUTED.  ON THE THROAT GEODESIC HPS's OWN <rho> IS POSITIVE -- AND THAT IS
NOT A TEST OF ANY QEI.
(CORRECTED, DOCKET 67 follow-up, M ruled: this said the two QEIs "APPLY IN
FORM BUT CANNOT BE EVALUATED ON HPS" and the throat value was "NOT A TEST OF
ANY APPLICABLE QEI"; "in form" left out both theorems' own Hadamard clause.)

    python3 qeihps.py             the reading
    python3 qeihps.py --selftest  sympy + mpmath + z3; every figure re-derived

Seated by DOCKET 64 (ruling B3, and the line's verifier: three SHOULD-FIX and
three NOTEs applied -- see section 6).  Imports seated modules from
research/warp-drive, copies none.

===============================================================================
0. THE REQUEST, READ AT SOURCE -- AND WHAT IT ACTUALLY NAMES
===============================================================================

E.-A. Kontou, "Wormhole restrictions from quantum energy inequalities",
Universe 10 (2024) 291, arXiv:2405.05963, Sec. 5.2 ("Timelike QEI Constraints"),
p. 19 of 28, READ in full text:

    "I should mention that the previous analysis was performed for a minimally
    coupled scalar field.  An interesting, semiclassically self-consistent
    wormhole solution is using nonminimal coupling to the curvature [90].  The
    throat of the wormhole derived is of Planck length or up to the order 10^2
    l_pl, so it is doubtful that it can be considered in the regime of the
    semiclassical approximation.  However, it would be of interest to examine
    that wormhole solution using one of the QEIs for the nonminimally coupled
    fields derived in [17,30] to determine its exact validity."

[90] = Hochberg, Popov & Sushkov, PRL 78 (1997) 2050 (gr-qc/9701064).
[17] = Fliss, Freivogel, Kontou & Pardo Santos, arXiv:2309.10848.
[30] = Fewster & Osterbrink, J. Phys. A 41 (2008) 025402, arXiv:0708.2450.

TWO CORRECTIONS TO THE DOCKET 62 RULING, both READ:
  (i)  The request is real and is attributable.  It names the NON-MINIMAL QEIs
       [17,30] -- not Fewster & Smith, and not a generic difference QEI.  ([30]
       IS a difference QEI, and state-dependent.)
  (ii) "Fewster & Smith is now the better instrument for it" is REFUTED ON
       HYPOTHESIS FOR HPS's FIELD (xi = 1/6) ONLY (section 1).  It is
       UNAFFECTED for the minimally coupled corridor (ledger row O2):
       fewsterteo.RIGHT_INSTRUMENT and throatmass.NARROWING_3_STATUS stand, and
       nothing here speaks to them.  Kontou's own Sec. 3.2 says why the
       Fewster-Smith class of derivations cannot reach this field (CORRECTED,
       DOCKET 67: this line said "no absolute or state-independent inequality";
       the sentence is about the FS sum-of-squares derivations, and FO Sec. 6
       expects an absolute NMC version to be adaptable): "This is not true, for
       example, for the T_split operator of nonminimally coupled fields, so these
       inequalities cannot be used in this case.  State-dependent bounds have
       been derived for the nonminimally coupled field [17,29,30]."

===============================================================================
1. HYPOTHESES, NAMED AND CHECKED AGAINST THE OBJECT
===============================================================================

HPS's FIELD (gr-qc/9701064, READ in full): "We consider the case of a
conformally coupled scalar field"; eqs. (5)-(7) are written "for a conformally
coupled scalar (xi = 1/6)"; footnote [20]: "scalar mass and temperature to
zero: m = kappa = 0".  Source term: the Anderson-Hiscock-Samuel ANALYTIC
APPROXIMATION to <T> (PRD 51, 4337), their eq. (4) -- an approximation, not the
exact expectation value in a specified Hadamard state.  Units hbar=c=G=1, MTW.

  FEWSTER & SMITH gr-qc/0702056 (READ): "the first absolute QEI for the
  minimally-coupled massive quantum Klein-Gordon field on four dimensional
  globally hyperbolic spacetimes"; field equation (nabla^2 + mu^2)phi = 0.
      minimal coupling ........ HPS xi = 1/6            FAILS -> REFUSED
      Hadamard state .......... HPS <T> is the AHS approximation   NOT MET
      globally hyperbolic ..... local: a small sampling domain     MET locally
                                inside a convex normal neighbourhood (CORRECTED,
                                DOCKET 67: "a causal diamond suffices" -- a
                                causal diamond is not in general one)
  FS themselves (Sec. 2.2): for the non-minimally coupled field "one must smear
  the stress-energy tensor even to obtain an inequality on the classical field
  ... which necessitates a more complicated analysis".  REFUSED: evaluating FS on
  HPS would be failure mode (4).

  FEWSTER & OSTERBRINK 0708.2450 Thm 4.2 (READ) -- written for THAT field,
  and REFUSED on HPS's state (its Hadamard clause; see below):
          (rho_quant o gamma)(f^2) >= -Q_xi(f),
      Q_xi(f) = Qt_A^xi(f) 1 + xi (:Phi^2: o gamma)(Q_B[f]) + xi (:Phi^2: o gamma)(Q_C^xi[f]),
      Q_B[f] = 2 (f')^2,  Q_C^xi[f] = f^2 (R_mn g^m g^n - (1/2)(1 - 4 xi) R).
      (Q_C as FO print it, in their Birrell-Davies [-,-,-] signs, FO fn. 2, not
      this file's MTW: in MTW it reads -f^2 (R_uu + (1/2)(1 - 4 xi) R).  Q_C is
      never evaluated here; named by DOCKET 67.)
      globally hyperbolic, smooth metric (FO's hypothesis; CORRECTED, DOCKET 67:
      this list and FORM_TAGS[FO] omitted it, though it is carried for FS and
      FFKP) ..... restorable LOCALLY on a globally hyperbolic neighbourhood of
      gamma(supp f) -- NAMED, not computed; not a FORM_TAGS entry
      CORRECTED (DOCKET 67 follow-up): now a FORM_TAGS entry ("globhyp"),
      applied LOCALLY -- FO on a globally hyperbolic neighbourhood N of
      gamma(supp f) as a spacetime in its own right.  COMPUTED: the metric is
      ANALYTIC on |l| < eps about the throat (normal_form(): det of the
      fourth-derivative matrix -(3L+4) x non-zero at data (9), only zero
      L = -4/3; ll a constraint propagated by div E = 0 identically; Cauchy's
      analytic-ODE theorem NAMED; eps not computed).  NAMED, not computed: a
      static metric is strongly causal, so small globally hyperbolic
      neighbourhoods exist; a reference Hadamard state on N (Fulling-
      Narcowich-Wald, NAMED-NOT-READ) ............................ MET LOCALLY
      xi in [0, 1/4] .......... 1/6                         MET  (computed from HPS_XI)
      timelike geodesic ....... the throat worldline l = 0: acceleration
                                f'/(2f), derived from metric (2) by sympy and
                                evaluated at HPS data (9): 0  MET  (computed)
      Hadamard state psi ...... HPS <T> is the AHS approximation   NOT-ESTABLISHED
                                ("On the set of Hadamard states, we then find",
                                FO p.10: a hypothesis OF THE THEOREM -- a FORM
                                tag since the DOCKET 67 follow-up, so FO is
                                REFUSED on it; it was filed as an evaluation
                                input and FO read OPEN)
      rho_quant NORMAL-ORDERED against a reference Hadamard state omega_0
      (DIFFERENCE type) ......................... needs omega_0 on HPS  NOT-FOUND
      :Phi^2: in the state ..................... HPS print no <phi^2>  NOT-FOUND
  FO Sec. 3 prove there is NO state-independent bound for xi > 0 -- FOR THE
  MASSLESS FIELD IN 4D MINKOWSKI SPACE (their construction, and their
  conclusion: "at least for massless fields in four-dimensional Minkowski
  space"); it is NOT proved on HPS's curved background.  Their conclusion: an
  absolute version for non-minimal coupling "can also be adapted" -- expected,
  NOT DONE.  Searched (alphaXiv, "absolute QEI non-minimally coupled curved
  spacetime"): none found.  NOT-FOUND.

  FLISS-FREIVOGEL-KONTOU-PARDO SANTOS 2309.10848 THEOREM IV.1, eq. (72) (READ,
  Sec. IV.A-B) -- Kontou's [17], a CURVED-SPACETIME worldvolume NULL QEI, and
  it too is REFUSED on HPS's state (its Hadamard clause; CORRECTED, DOCKET 67
  follow-up, M ruled -- this said "it too applies IN FORM"):
      <:rho_n:(f^2)>_psi >= -2 INT_D d^n alpha/(2 pi)^n ((Q x Q) W_0)_kappa(fbar_alpha, f_alpha)
                            - xi <:phi^2:(Q[f])>_psi,
      Q = l^mu nabla_mu,  Q[f] = nabla_mu nabla_nu (l^mu l^nu f^2) + (1/2) R_mn l^m l^n f^2.
      (Q[f] as printed in v1, (69b).  DOCKET 67: v1's own conserved eq. (9)
      gives -R_mn l^m l^n f^2, and (13) and (61) as printed disagree with both
      -- a DISCREPANCY IN v1, recorded, not a refutation, and not to be quoted
      against the unread SciPost version.  Nothing here evaluates Q[f]; it would
      matter on HPS, whose throat has R_ll != 0 on any open supp f.)
      free field on a fixed background ... HPS's xi = 1/6 scalar on metric (2)
                                                                    MET  (in form)
                                (a FORM_TAGS row, "free", since the DOCKET 67
                                follow-up; record HPS_FIELD_FREE)
      Wick powers by the Leibniz-rule prescription ... a property of the
      construction, not of HPS                     (both named, DOCKET 67)
      any xi ("holds for any value of the coupling constant") ...   MET  (computed)
      M globally hyperbolic, f supported in a SMALL SAMPLING DOMAIN: an open
      set inside a globally hyperbolic convex normal neighbourhood, one
      hyperbolic chart ... metric (2) is non-degenerate Lorentzian at the throat
      (f(0) > 0, r(0) > 0, computed); a convex normal neighbourhood then exists
      about any point (Whitehead; NAMED, not computed)              MET LOCALLY
      CORRECTED (DOCKET 67): "MET LOCALLY" is computed from f(0) > 0 and r(0) > 0
      alone, and rests on an UNNAMED hypothesis -- the metric's connection C^{1,1}
      or better on an open neighbourhood of the throat, which non-degeneracy at a
      point does not give and which is NOT PROVED here (the Taylor radius is not
      proved, section 3).  Whitehead supplies convexity and normality only; the
      globally hyperbolic qualifier (asserted in FS p.7 without citation) and
      the one-hyperbolic-chart clause are separate results, not Whitehead's.
      CORRECTED (DOCKET 67 follow-up): the regularity is now COMPUTED, not
      presumed -- the metric is analytic (so C^{1,1}) on |l| < eps about the
      throat (normal_form(); see FO's "globhyp" above); eps is not computed.
      The row reads it, and returns NOT-ESTABLISHED on a control where it is
      withheld.  The globally hyperbolic qualifier and the chart (66) stay NAMED.
      l^mu null near supp f ... radial l = f^(-1/2) d_t + d_l, g(l,l) = 0
      (sympy)                                                       MET  (computed)
      Hadamard state psi ...... HPS <T> is the AHS approximation   NOT-ESTABLISHED
                                ("for all Hadamard states psi", p.18: a
                                hypothesis OF THE THEOREM, P3 -- a FORM tag
                                since the DOCKET 67 follow-up, M ruled)
      W_0, the two-point function of a reference Hadamard state on HPS
      (DIFFERENCE type: the left side is <T^ren>_psi - <T^ren>_psi0, eq. (59))
                                                                    NOT-FOUND
      <:phi^2:> in the state ... HPS print no <phi^2>               NOT-FOUND
  So FFKP Thm IV.1 is BLOCKED THE SAME WAY AS FO Thm 4.2 -- since the DOCKET
  67 follow-up, REFUSED as FO is, on the Hadamard clause alone (computed: every
  other form row MET); were HPS's state shown Hadamard, both would be OPEN on
  the two NOT-FOUND inputs (CONDITIONAL_IF_HADAMARD, computed).  REFUSED is
  about HPS's state as published; it is not a finding that HPS violates
  either inequality, and not a no-go.  Its self-reference
  instance (psi_0 = psi) is NOT examined here.  CAVEAT, not a hypothesis of
  the theorem: the convex normal neighbourhood about the throat is set by a
  curvature radius of 0.0243 l_P, so any sampling domain it admits is
  sub-Planckian IN THE ANGULAR DIRECTIONS (conjugate distance pi r_0 = 0.0763
  l_P) -- Kontou's own doubt about the semiclassical regime of [90].
  CORRECTED (DOCKET 67): "any sampling domain" was unqualified; the tidal
  tensor vanishes exactly on the throat worldline, so nothing computed bounds a
  domain's extent in t by r_0 (nor is a domain long in t constructed).

  FFKP's DSNEC/SNEC forms (75)-(93) are MINKOWSKI (reference state: the
  Minkowski vacuum, chosen in the sentence before eq. (75)).  Kontou 2024
  Sec. 3.3: "the DSNEC ... currently makes sense only on Minkowski spacetime or
  at length scales sufficiently smaller than the curvature scale."  (The elided
  words are "of Equation (49)": her clause is about the MINIMALLY coupled
  DSNEC, and this file transfers it to FFKP's non-minimally coupled forms.)
  HPS's throat is not flat (Kretschmann 4/r_0^4 != 0, computed), and
  "sufficiently smaller" is SUB-PLANCKIAN under either curvature-radius
  definition below.  REFUSED on HPS -- ON THIS FILE'S OWN PREMISE that a
  sampling length below l_P is outside the semiclassical regime: the l_P floor
  is neither Kontou's nor FFKP's (named, DOCKET 67).  The DSN row also leaves
  out FFKP's state class (79), the free-scalar and null-plane-smearing
  hypotheses and the massless/factorisation steps; they decide nothing here,
  because the row is REFUSED on flatness (see FORM_TAGS).
  CORRECTED (DOCKET 67 follow-up): they are now FORM_TAGS rows -- free scalar
  (MET), Hadamard ((75) restates (72): NOT-ESTABLISHED), null-plane smearing
  (76) (NOT-ESTABLISHED off flat) and the state class (79) (NOT-ESTABLISHED:
  HPS print no <phi^2>).  On HPS the status stays REFUSED, now on four rows;
  on a flat control the DSNEC is REFUSED on the state, not EVALUABLE, until
  Hadamard and <phi^2> are supplied.  The massless and factorised-f steps
  select a sub-form ((80) holds without them) and stay NAMED; HPS's m = 0
  meets the massless one.  QEI_KIND[DSN] is now "absolute" (Minkowski-vacuum
  reference, whose <T^ren> vanishes); being a NULL inequality it still cannot
  be satisfied by HPS's rho > 0 (QEI_CONTRACTION; throat_verdict()).

  THE CURVATURE RADIUS, DEFINED (ruling B3).  At HPS's throat data the ONLY
  non-zero orthonormal Riemann components are R_(theta phi theta phi) and its
  index permutations, and R_(theta phi theta phi) = 1/r_0^2 (computed).  THE
  CURVATURE RADIUS USED HERE is r_c := |R_(theta phi theta phi)|^(-1/2) = r_0 =
  1/sqrt(540 pi) = 0.0242789 l_P at L = -2/3.  The Kretschmann definition
  gives (R_abcd R^abcd)^(-1/4) = (4/r_0^4)^(-1/4) = r_0/sqrt 2 = 0.0171677 l_P.
  Both are sub-Planckian; the DSNEC refusal holds under either.

===============================================================================
2. HPS's EQUATIONS, TESTED BEFORE THEY ARE USED
===============================================================================

Eqs. (5)-(7) were transcribed from the arXiv text layer and TESTED, not trusted:
  * printed Einstein-tensor left sides == G^mu_nu of metric (2), sympy: 0, 0, 0.
  * DIMENSION: every term must scale as length^-4.  One does not: ll log bracket
    "-4 f'^2 r'^2/(f^2 r)" (length^-3).  Unique homogeneous repair: /(f^2 r^2).
  * CONSERVATION nabla_mu T^mu_l = 0 FAILS as printed.  The log bracket must be
    conserved AND traceless on its own (it multiplies ln(mu^2 f), mu arbitrary,
    footnote [20]).  Scanning every printed log-bracket coefficient for a single
    change that restores BOTH: EXACTLY ONE exists -- tt log bracket,
    f'^2 f''/f^3, 16 -> 116.  With the two repairs: log bracket conserved (0),
    traceless (0), full tensor conserved (0).  Whether the paper or the text
    layer carries the defect cannot be told from here; BOTH REPAIRED TERMS CARRY
    f' AND VANISH AT THE THROAT, so nothing below depends on them.
  * TRACE of the non-log part == 16 (Riem^2 - Ric^2 + c Box R) with c SOLVED,
    unique, c = 1 (the other sign has no solution): <T^mu_mu> =
    (1/2880 pi^2)(R_abcd R^abcd - R_ab R^ab + Box R), a pure local curvature
    scalar, the form of the conformal-scalar trace anomaly (form NAMED-NOT-READ
    against a primary source) IN THE AHS SCHEME: the Box R coefficient is
    scheme-dependent, a beta-type (1)H term shifting it (CORRECTED, DOCKET 67).
    An independent check on every non-log coefficient.

===============================================================================
3. WHAT IS COMPUTED EXACTLY ON HPS  (THEOREM, sympy; signs by z3)
===============================================================================

HYPOTHESES OF THE EQUATION SOLVED HERE (named, DOCKET 67): the semiclassical
Einstein equation with Lambda = alpha = beta = 0 in the AHS scheme, one field
(N = 1, no large-N limit), solved as the unreduced fourth-order system without
Flanagan-Wald's physical-solution prescription (r_0 ~ hbar^(1/2), so the throat
has no expansion in hbar about a classical solution), at a 0.0243 l_P throat
where semiclassical validity is not established.  A beta-type term moves r_0,
the fourth derivatives, <rho>(0) and the sign of <rho + p_l>(0) (DOCKET 67,
computed); every result below is the b = 0 member and is HPS's system's.
L carries the renormalisation scale: HPS's log term is ln(mu^2 f), so the range
-1 <= L < 0 below is a statement about ln(mu^2 f(0)) (DOCKET 67: the log
bracket is exactly -96 x the Bach tensor, so a shift in ln mu is a shift in
alpha).

HPS boundary data (9): -1 <= L = ln f(0) < 0, f' = f'' = f''' = 0, r' = r'' =
r''' = 0, r(0) = sqrt(-16 K^2 L), K^2 = 1/(5760 pi).  The ll equation at l = 0
reproduces r_0 (and throatmass.hps_quartic, a different route).  The tt and
theta-theta equations at l = 0 are linear in the fourth derivatives:

    f''''(0)/f(0) = 259200 pi^2 (-L - 1)/(L (3L + 4))       >= 0 on [-1, 0)
    r''''(0)/r(0) = 129600 pi^2 (2 - L^2)/(L^2 (3L + 4))    >  0 on [-1, 0)

so the throat IS a minimum of r, quartic (r'' = 0 there).  At the throat:

    rho   = -T^t_t = 1/(8 pi r_0^2) = -45/L   >  0     (67.5 at L = -2/3)
    p_l   = -rho                     (radial NEC SATURATED exactly: rho + p_l = 0)
    p_t   = 0                        (rho + p_t = rho > 0)
    8 pi (rho + p_l)(l) = -(r''''(0)/r(0)) l^2 + O(l^4)       -> < 0 for l != 0
    at L = -2/3:  rho + p_l = -28350 pi l^2 + O(l^4)   (Planck units)

THE THROAT WORLDLINE l = 0 IS A COMPLETE TIMELIKE GEODESIC OF A STATIC METRIC,
so <rho> along it is the constant -45/L for all proper time.  For EVERY sampling
function g:

    INT g(tau)^2 <T_ab u^a u^b> dtau  =  (-45/L) ||g||^2  >  0   EXACTLY.

Every radial observer crossing the throat measures the same rho there
(gamma^2 (rho + v^2 p_l) = rho when p_l = -rho).  The NEC violation that makes
the geometry a wormhole is OFF the throat, O(l^2).  THIS IS HPS's OWN <T> (the
AHS approximation) ON THE THROAT: a THEOREM about HPS's system, and NOT the left
side of any QEI that applies to this field (section 4(a)).

===============================================================================
4. THE ANSWER TO "SATISFY OR VIOLATE, AND BY HOW MUCH"
===============================================================================

(a) ON THE THROAT GEODESIC: NOT A TEST -- no applicable QEI is evaluated by
    it.  HPS's own <rho> there is -45/L > 0 (67.5 rho_P at their plotted
    L = -2/3; 45 <= rho < oo over their family) -- that stands, THEOREM.  But
    the only QEIs whose hypotheses HPS's field meets in form, FO Thm 4.2 and
    FFKP Thm IV.1, are DIFFERENCE inequalities: their left side is
    <rho_ren>_Psi - <rho_ren>_Psi0 (FO Sec. 2; FFKP eq. (59)), not HPS's <T>,
    and FO's lower bound -Q_xi contains xi <:Phi^2:>(Q_B + Q_C), which can be
    positive.  So HPS's positive throat <rho> decides NO applicable inequality.
    ("Satisfied" would hold only for an ABSOLUTE bound whose lower bound is
    <= 0, and by section 1 none of those applies to this field.)  The verdict
    word is computed by throat_verdict() from the QEI catalogue (VERDICT_
    THROAT_GEODESIC); it returns SATISFIED only if an applicable absolute QEI
    exists, and the selftest shows it does so on a control catalogue.
    CORRECTED (DOCKET 67 follow-up, M ruled): FO and FFKP do NOT meet their
    hypotheses "in form" -- both hold only for Hadamard states, and that
    clause is now a form tag -- so on HPS NO QEI applies (throat_verdict
    returns NOT A TEST with an empty applicable list).  The difference
    argument above is kept as the CONDITIONAL: were HPS's state Hadamard,
    FO and FFKP would apply and rho > 0 would still decide neither.  And a
    second ground, new: FFKP Thm IV.1 and the DSNEC are NULL inequalities,
    whose left side on HPS is rho + p_l (0 on the throat worldline, negative
    at O(l^2) off it), not rho; throat_verdict() now returns SATISFIED only
    for an applicable ABSOLUTE TIMELIKE QEI (QEI_CONTRACTION), and a control
    shows the clause bites.

    WITHDRAWN (DOCKET 64 verifier, SHOULD-FIX; kept, not deleted):
      | "That is SATISFIED, exactly -- and it is not a QEI test of anything,
      |  because the only negative energy HPS carry is off the throat."
      -- withdrawn: over-represents; see (a).
      | "The minimal-coupling flat bound -C_F/tau^4 is satisfied with the
      |  whole of 67.5 ||g||^2 to spare."
      -- withdrawn: it applies a minimal-coupling, Minkowski bound to a
         xi = 1/6 field at a sub-Planckian curvature radius -- failure mode (4)
         inside this instrument.  (VERDICT_THROAT_GEODESIC_WITHDRAWN.)
(b) FOR THE INEQUALITIES WRITTEN FOR HPS's FIELD -- FO Thm 4.2 AND FFKP
    Thm IV.1 (eq. 72), the two Kontou names: REFUSED ON HPS's STATE AS
    PUBLISHED (both theorems hold "for all" / "on the set of" Hadamard states;
    HPS's state is the AHS approximation, NOT-ESTABLISHED Hadamard), and were
    it Hadamard, NOT EVALUABLE -- OPEN.  CORRECTED (DOCKET 67 follow-up, M
    ruled: "Adding the missing Hadamard hypothesis in qeihps.py would move
    FFKP from OPEN to REFUSED. - do it."; FO held to the same standard, since
    FO-P6 is the same clause): this read "FOR THE INEQUALITIES THAT APPLY TO
    HPS's FIELD ... NOT EVALUABLE -- OPEN".  REFUSED is not a finding that HPS
    violates either inequality, and not a no-go: Kontou's question stays
    unanswered, and the two blockers below stand behind the first.  Both are
    difference inequalities; the left side needs a reference Hadamard state's
    <T^ren> (FO) or two-point function W_0 (FFKP) on HPS, and the right side
    needs <:Phi^2:> in HPS's state.  Neither is in print: HPS read in full
    print neither, and two alphaXiv searches (QEI / two-point function /
    <phi^2> on the HPS wormhole; absolute QEI for non-minimal coupling)
    returned no paper that evaluates any QEI on HPS or supplies either input.
    NOT-FOUND.  Nor is HPS's state established as Hadamard (AHS approximation;
    AHS NOT-REACHED).  The ONE FO instance that can be written down --
    omega_0 = HPS's own state -- reads 0 >= -Qt_A(f), with Qt_A >= 0 (FO): TRUE
    FOR EVERY METRIC AND THEREFORE VACUOUS.  And it is available only IF HPS's
    state is Hadamard, which FO require of omega_0 and which is NOT-ESTABLISHED
    above (named, DOCKET 67).  It is computed below only so the
    refusal names what it refuses.
(c) OFF THE THROAT, where rho + p_l < 0: HPS's solution exists only as boundary
    data plus figures; no closed form over any interval is printed.  The Taylor
    coefficients are exact; a smeared integral needs the series' radius of
    convergence, which is NOT PROVED.  REFUSED as an exact evaluation.
    (DOCKET 67 follow-up: that an analytic solution EXISTS on some |l| < eps
    is now computed -- normal_form() -- so the radius is positive; its size,
    which a smeared integral needs, is still NOT PROVED.)

===============================================================================
5. CONTROLS, AND EACH CAN FAIL
===============================================================================

  C1 FLAT LIMIT.  FO Thm 4.3's state-independent part, from their eq. (53) by
     direct integration (sympy) AND from their eq. (55)-(56), massless n = 4:
     Qt_A = (1/(4 pi^3)) (1/4 - xi/3) INT_0^oo |fhat|^2 u^4 du.  At xi = 0 this
     is (1/16 pi^3) INT |fhat|^2 u^4 = FS eq. (88) exactly, and by Parseval
     (1/16 pi^2) INT (g'')^2 (Fewster-Thompson 2301.01698 eq. (1.4), READ).  On
     the clamped-beam optimum of duration tau, MEASURED by quadrature (not by
     the closed form): B/||g||^2 = mu_1^4/(16 pi^2 tau^4) = achievable.FEWSTER_C
     / tau^4.  A C-infinity bump gives a STRICTLY larger ratio (the variational
     arm, which fails if mu_1 or the bound is mis-set).  At xi = 1/6 the
     state-independent part is 7/9 of the minimal one.
  C2 A STATE KNOWN TO VIOLATE.  FO's one-particle state (their (25)), energy
     density on the worldline RE-DERIVED from (24)-(25) and equal to their (28)
     identically; norm 1 and energy 2 kappa/3 (their (26)) reproduced.  At
     xi = 1/6 its smeared energy density is negative for a sampler inside
     |t| < 1/(sqrt(31) kappa); the j-particle state violates the MINIMAL-coupling
     state-independent bound for j >= j* (MEASURED) -- the reason FS cannot be
     used on this field, shown rather than asserted -- while FO's state-dependent
     bound HOLDS at every j (the per-particle slope is non-negative).
  C3 TRANSCRIPTION.  Conservation FAILS on the text as extracted (residual
     printed); passes repaired; the repair scan returns exactly one candidate.
  C4 THE SIGN MACHINERY CAN RETURN NEGATIVE.  The same series gives
     rho + p_l < 0 off the throat, and a radial observer of rapidity eta sees
     rho + sinh^2(eta)(rho + p_l) at l != 0, negative for large eta -- so the
     positive throat value is not a sign-convention artefact.

  WHAT THE SELFTEST COUNTS.  A [ok]/[XX] row is COMPUTED: its left side is
  produced by code that can return the other answer (every hypothesis verdict
  is derived from HPS_XI, from the acceleration f'/(2f) at data (9), or from
  the curvature; each derivation also has a control that returns the other
  word).  A [pin] row is a RECORD PIN: it restates what was READ or searched
  (the request's existence, HPS's xi, NOT-FOUND flags) and can fail only if the
  record is edited.  The two are counted separately.

===============================================================================
6. DOCKET 64 CORRECTIONS APPLIED ON SEATING
===============================================================================

  Ruling B3: curvature-radius definition stated and computed (section 1);
    the path is this file's own directory, not an absolute path.
  Verifier SHOULD-FIX 1: throat verdict "SATISFIED" WITHDRAWN -> "NOT A TEST"
    (section 4(a)); the -C_F/tau^4 sentence withdrawn and kept, marked.
  Verifier SHOULD-FIX 2: FFKP 2309.10848 Thm IV.1 (eq. 72) added to the
    hypothesis table and the OPEN verdict; blocked the same way as FO.
  Verifier SHOULD-FIX 3: hypothesis verdicts COMPUTED, typed-literal selftest
    rows made computed or relabelled [pin].
  Verifier NOTEs: FO Sec. 3 scoped to massless 4D Minkowski; the DOCKET 62
    refutation scoped to HPS's field (O2 unaffected).  No new ledger row (the
    ruling: qeihps co-owns O5's text).
  Where the ruling (no SHOULD-FIX) and the verifier (three) differ, the
  verifier's weaker statement is applied: the ruling never saw the verdict.

===============================================================================
7. DOCKET 67 FOLLOW-UP: VERDICTS MOVED ON M's RULING
===============================================================================

  M: "Adding the missing Hadamard hypothesis in qeihps.py would move FFKP from
  OPEN to REFUSED. - do it."; the other verdicts held to the same standard (a
  verdict rests on a correct, stated ground, computed or READ).  Records:
  docket67-raw adjudications/shards, keys 2309.10848-thmiv.1,
  0708.2450-thm4.2, kontou-fo-ffkp-nmc-qei, 2309.10848-dsnec.
    FORM_TAGS  FFKP + hadamard, + free; FO + hadamard, + globhyp; DSN + free,
               + hadamard, + nullplane, + phimax (each READ at source).
    STATUSES   FO   OPEN -> REFUSED (Hadamard clause)
               FFKP OPEN -> REFUSED (Hadamard clause)
               DSN  REFUSED -> REFUSED (flat; Hadamard; null plane; (79))
               FS   REFUSED, unchanged
               throat verdict NOT A TEST, unchanged; applicable FO, FFKP -> none
               conditional on Hadamard (computed): FO, FFKP OPEN, as before
    REGULARITY the "MET LOCALLY" rows now read a computed ground
               (normal_form(): analytic on |l| < eps), not f(0), r(0) > 0
               at one point; a control withholds it and the rows say
               NOT-ESTABLISHED.
    KIND       QEI_KIND[DSN] difference -> absolute; QEI_CONTRACTION added;
               throat_verdict SATISFIED needs ABSOLUTE AND TIMELIKE.
  Every superseded wording is kept beside its replacement, marked.
"""

import math
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
WD = HERE                      # ruling B1/B3: this file's own directory
if WD not in sys.path:
    sys.path.insert(0, WD)

import achievable      # FEWSTER_C, FEWSTER_MU1 -- seated, imported, not copied
import throatmass      # hps_quartic -- a different route to r_0

# ---------------------------------------------------------------------------
# READ, as data.  These are RECORDS (what was read or searched); the selftest
# restates them as [pin] rows, not as controls.
# ---------------------------------------------------------------------------

KONTOU_SOURCE = ("E.-A. Kontou, Universe 10 (2024) 291, arXiv:2405.05963, "
                 "Sec. 5.2, p. 19 of 28")
KONTOU_REQUEST = (
    "However, it would be of interest to examine that wormhole solution using "
    "one of the QEIs for the nonminimally coupled fields derived in [17,30] to "
    "determine its exact validity.")
KONTOU_REQUEST_FOUND = True        # RECORD: read at source (text kept out of tree)
KONTOU_NAMES = {17: "Fliss-Freivogel-Kontou-Pardo Santos 2309.10848",
                30: "Fewster-Osterbrink 0708.2450"}
KONTOU_ON_ABSOLUTE_FOR_NMC = (
    "This is not true, for example, for the T_split operator of nonminimally "
    "coupled fields, so these inequalities cannot be used in this case.  "
    "State-dependent bounds have been derived for the nonminimally coupled "
    "field [17,29,30].")

HPS_SOURCE = "Hochberg, Popov & Sushkov, gr-qc/9701064, PRL 78 (1997) 2050"
HPS_XI = Fraction(1, 6)            # "for a conformally coupled scalar (xi = 1/6)"
HPS_MASS_TEMPERATURE = (0, 0)      # footnote [20]: m = kappa = 0
HPS_SOURCE_TERM = "Anderson-Hiscock-Samuel ANALYTIC APPROXIMATION, PRD 51 4337"
HPS_K2_TIMES_PI = Fraction(1, 5760)    # K^2 = 1/(5760 pi), HPS
HPS_PLOTTED_LNF0 = (-2, 3)         # "a particular numerical solution for ln f(0) = -2/3"
#: HPS boundary data (9) at l = 0: derivative order k -> value of f^(k)(0),
#: r^(k)(0), k = 1, 2, 3 (all zero).  -1 <= ln f(0) < 0.
HPS_DATA_9_F = {1: 0, 2: 0, 3: 0}
HPS_DATA_9_R = {1: 0, 2: 0, 3: 0}
HPS_PRINTS_PHI2 = False            # HPS read in full: no <phi^2> anywhere
HPS_PRINTS_CLOSED_FORM_SOLUTION = False   # boundary data (9) + figures only
HPS_STATE_HADAMARD_ESTABLISHED = False    # AHS approximation; AHS NOT-REACHED
REFERENCE_STATE_ON_HPS_FOUND = False      # two alphaXiv searches: none
TAYLOR_RADIUS_OF_CONVERGENCE_PROVED = False
#: RECORD (DOCKET 67 follow-up, M ruled): HPS's field is a FREE scalar on a
#: given metric -- "We consider the case of a conformally coupled scalar field",
#: m = 0, no self-interaction term in HPS's eqs. (5)-(7), which are the AHS
#: free-field approximation; READ as such by DOCKET 67 audit 2309.10848-thmiv.1
#: ("P2 is met in form").  FFKP Thm IV.1's P2 and the DSNEC's free-scalar
#: hypothesis read this record.
HPS_FIELD_FREE = True

# ---------------------------------------------------------------------------
# COMPUTED AT IMPORT (stdlib only; the ledger imports this module).  Each
# closed form used here is DERIVED by sympy in --selftest and the stdlib value
# is compared with the sympy value there:
#   r_0^2 = -16 K^2 L           (ll equation at l = 0; throat())
#   rho   = 1/(8 pi r_0^2)      (-G^t_t/(8 pi) at data (9); throat())
#   R_(theta phi theta phi) = 1/r_0^2, Kretschmann = 4/r_0^4 (einstein_and_anomaly())
#   a     = f'/(2 f)            (static-observer acceleration; static_acceleration())
#   det   = -(3 ln f + 4)/(129600 pi^2 f r)  (the (f'''', r'''') coefficient
#           matrix of the tt and theta-theta equations; normal_form())
# ---------------------------------------------------------------------------

_L0 = Fraction(*HPS_PLOTTED_LNF0)
#: rho at the throat is RHO_THROAT_COEFF / (-L), Planck units
RHO_THROAT_COEFF = 1 / (8 * 16 * HPS_K2_TIMES_PI)
RHO_THROAT_AT_PLOTTED = RHO_THROAT_COEFF / (-_L0)
R0_SQUARED_TIMES_PI_AT_PLOTTED = -16 * HPS_K2_TIMES_PI * _L0     # pi r_0^2
#: THE curvature radius (ruling B3): r_c := |R_(theta phi theta phi)|^(-1/2) = r_0
CURVATURE_RADIUS_LP = math.sqrt(float(R0_SQUARED_TIMES_PI_AT_PLOTTED) / math.pi)
KRETSCHMANN_AT_THROAT = 4 / CURVATURE_RADIUS_LP**4
#: the Kretschmann definition, (R_abcd R^abcd)^(-1/4)
KRETSCHMANN_RADIUS_LP = KRETSCHMANN_AT_THROAT ** -0.25
CURVATURE_RADIUS_DEFINITION = (
    "r_c := |R_(theta phi theta phi)|^(-1/2) = r_0 = %.7f l_P (the only "
    "non-zero orthonormal Riemann component at the throat); the Kretschmann "
    "definition (R_abcd R^abcd)^(-1/4) = r_0/sqrt 2 = %.7f l_P; both "
    "sub-Planckian" % (CURVATURE_RADIUS_LP, KRETSCHMANN_RADIUS_LP))

#: the radii as printed in the docstring; --selftest checks both.
CURVATURE_RADIUS_LP_PRINTED = 0.0242789
KRETSCHMANN_RADIUS_LP_PRINTED = 0.0171677


def static_acceleration_at(f1, lnf0):
    """a = f'/(2f) at l = 0 for the static observer of metric (2); the form is
    DERIVED from the metric by static_acceleration() in --selftest."""
    return f1 / (2 * math.exp(lnf0))


THROAT_ACCELERATION = static_acceleration_at(HPS_DATA_9_F[1], float(_L0))
THROAT_F0 = math.exp(float(_L0))
#: radial null field l = f^(-1/2) d_t + d_l:  g(l, l) = -f (f^(-1/2))^2 + 1
THROAT_RADIAL_NULL_NORM = -THROAT_F0 * (THROAT_F0 ** -0.5) ** 2 + 1

#: METRIC REGULARITY NEAR THE THROAT (DOCKET 67 follow-up; it was the UNNAMED,
#: NOT PROVED hypothesis behind FFKP's "MET LOCALLY", and FO's restored
#: "globally hyperbolic, smooth metric" needs it too).  COMPUTED in --selftest
#: by normal_form(): the tt and theta-theta equations are LINEAR in
#: (f'''', r'''') with coefficient determinant -(3 ln f + 4)/(129600 pi^2 f r);
#: the ll equation carries no fourth derivative; and div(G - 8 pi T) = 0
#: IDENTICALLY (off shell).  At data (9) the determinant's factor is 3L + 4.
#: Where it is non-zero (and f, r > 0) the reduced system is a regular
#: ANALYTIC ODE in normal form, so a unique analytic solution exists on some
#: |l| < eps (Cauchy's existence theorem for analytic ODEs, NAMED); along it
#: the identity gives E_l' = -(f'/(2f) + 2 r'/r) E_l with E_l(0) = 0 (data (9)
#: solve the ll equation), so E_l = 0 and the full system holds.  The metric is
#: then analytic -- C^{1,1} and smooth -- on (-eps, eps) x R x S^2.  eps is NOT
#: computed (that is the Taylor radius, section 4(c)).
NORMAL_FORM_DET_FACTOR_AT_PLOTTED = 3 * _L0 + 4          # 2 at L = -2/3
METRIC_ANALYTIC_NEAR_THROAT = (NORMAL_FORM_DET_FACTOR_AT_PLOTTED != 0
                               and THROAT_F0 > 0 and CURVATURE_RADIUS_LP > 0)

#: xi ranges, closed.  None = every real xi.
FS_XI_RANGE = (Fraction(0), Fraction(0))          # minimal coupling only
FO_XI_RANGE = (Fraction(0), Fraction(1, 4))       # FO Thm 4.2
FFKP_XI_RANGE = None                              # FFKP Thm IV.1: "any value"


def xi_in(xi, rng):
    return rng is None or rng[0] <= xi <= rng[1]


FS, FO, FFKP, DSN = ("Fewster-Smith gr-qc/0702056",
                     "Fewster-Osterbrink 0708.2450 Thm 4.2",
                     "FFKP 2309.10848 Thm IV.1 (eq. 72)",
                     "FFKP 2309.10848 DSNEC/SNEC (75)-(93)")
#: each inequality's left side: HPS's <T> itself (absolute) or a difference
#: against a reference state (difference)
#: CORRECTED (DOCKET 67 follow-up, M: "address/repair/correct"): DSN was
#: labelled "difference".  On its own Minkowski domain its reference state is
#: the Minkowski vacuum (FFKP, the sentence before eq. (75)), whose renormalised
#: stress tensor vanishes, so its left side IS <T^ren>_psi: in effect ABSOLUTE.
#: It is labelled so.  (It moves nothing on HPS, where DSN is REFUSED; it is the
#: label throat_verdict() reads on a flat control.)  It carried this note:
#: "DOCKET 67, recorded not repaired: on its own Minkowski domain DSN's
#: difference against the Minkowski vacuum is in effect absolute.  The label is
#: data that throat_verdict() reads, and DSN is REFUSED and excluded there, so
#: it is left."
QEI_KIND = {FS: "absolute", FO: "difference", FFKP: "difference", DSN: "absolute"}
#: which contraction of T each inequality bounds, and on what (READ: FS and FO
#: Thm 4.2 bound rho = T(u,u) on a timelike worldline; FFKP Thm IV.1 bounds
#: <:rho_n:> = T(l,l) smeared over a worldvolume; the DSNEC bounds T_{--}
#: smeared on a null plane, (76)).  NEW (DOCKET 67 follow-up): throat_verdict()
#: used HPS's positive throat rho for every inequality, but a NULL inequality's
#: left side on HPS is rho + p_l -- exactly 0 on the throat worldline and
#: negative at O(l^2) off it (section 3) -- so rho > 0 decides no null QEI.
QEI_CONTRACTION = {FS: "timelike", FO: "timelike", FFKP: "null", DSN: "null"}
#: the hypotheses that decide whether an inequality applies to THIS FIELD AND
#: WORLDLINE ("in form"); the rest are inputs needed to EVALUATE it.  For FS,
#: an absolute QEI, the Hadamard state is a hypothesis of the theorem.
#: CORRECTED (DOCKET 67 follow-up, M ruled: "Adding the missing Hadamard
#: hypothesis in qeihps.py would move FFKP from OPEN to REFUSED. - do it.").
#: The sets were FS {xi, hadamard}, FO {xi, geodesic}, FFKP {xi, domain, null},
#: DSN {flat}, with this note, "recorded and NOT changed here, because these
#: sets decide the computed statuses":
#:   FO   omits FO's "globally hyperbolic, smooth metric" (carried for FS and
#:        FFKP); restorable locally, NAMED not computed (docstring section 1).
#:   FO, FFKP  file "Hadamard state psi" as an evaluation input, though "for all
#:        Hadamard states" is a hypothesis of both theorems; it is still listed
#:        and blocks evaluation (NOT-ESTABLISHED), so OPEN is unaffected.
#:   DSN  carries only "flat": FFKP's state class (79), free scalar, null-plane
#:        smearing and the massless/factorisation steps are not tagged, so a
#:        flat control returns EVALUABLE with no inputs; on HPS it is REFUSED.
#: Now every hypothesis OF THE THEOREM is a form tag (READ, each at source):
#:   FO   + "globhyp" (FO Thm 4.2: "defined on a globally hyperbolic spacetime
#:        with smooth metric", 0708.2450 p.10; audits 0708.2450-thm4.2,
#:        kontou-fo-ffkp-nmc-qei FO-P3) and + "hadamard" ("On the set of
#:        Hadamard states, we then find", FO-P6) -- held to the same standard
#:        as FFKP's, which M ruled on: the two theorems state the same clause.
#:   FFKP + "hadamard" (Thm IV.1: "for all Hadamard states psi", 2309.10848v1
#:        p.18; audit 2309.10848-thmiv.1 P3) and + "free" (P2, a free scalar on
#:        a fixed background).
#:   DSN  + "free", + "hadamard" ((75) is (72) restated, so it inherits "for all
#:        Hadamard states"), + "nullplane" (smearing f(x+,x-)^2 delta^(n-2)(y),
#:        (76)) and + "phimax" (the state class <:phi^2:>_psi <= phi_max^2,
#:        (79): "We can make progress if we focus on the class of states
#:        obeying" it; without it no DSNEC "in its standard form" is written).
#:        Audit 2309.10848-dsnec.  The massless (82)-(83), (93)-(97) and
#:        factorised-f steps are NOT tagged: they select a sub-form, not the
#:        family -- (80) holds without them -- and HPS's m = 0 (fn [20]) meets
#:        the massless one anyway; NAMED here, decide nothing.
#: STATUSES THAT MOVE (computed by qei_status; the selftest pins them):
#:   FO   OPEN (Hadamard, omega_0, <:Phi^2:> missing) -> REFUSED (Hadamard
#:        state psi NOT-ESTABLISHED)
#:   FFKP OPEN (the same three) -> REFUSED (Hadamard state psi NOT-ESTABLISHED)
#:   DSN  REFUSED (flat) -> REFUSED (flat; Hadamard; null plane; (79))
#:   throat_verdict: NOT A TEST with FO, FFKP applicable -> NOT A TEST with
#:        none applicable.
#: REFUSED here is a statement about HPS's state AS PUBLISHED: the theorems'
#: own Hadamard clause is not established for it (the AHS approximation).  It
#: is NOT a finding that HPS violates either inequality, and NOT a no-go: were
#: HPS's state shown Hadamard, both would be OPEN, blocked on omega_0 / W_0 and
#: <:Phi^2:> (computed on that control: CONDITIONAL_IF_HADAMARD below).
FORM_TAGS = {FS: {"xi", "hadamard"},
             FO: {"xi", "geodesic", "globhyp", "hadamard"},
             FFKP: {"xi", "free", "domain", "null", "hadamard"},
             DSN: {"flat", "free", "hadamard", "nullplane", "phimax"}}


def hypothesis_table(xi=HPS_XI, accel=THROAT_ACCELERATION, f0=THROAT_F0,
                     r0=CURVATURE_RADIUS_LP, null_norm=THROAT_RADIAL_NULL_NORM,
                     kretschmann=KRETSCHMANN_AT_THROAT,
                     radii=(CURVATURE_RADIUS_LP, KRETSCHMANN_RADIUS_LP),
                     hadamard=HPS_STATE_HADAMARD_ESTABLISHED,
                     ref_state=REFERENCE_STATE_ON_HPS_FOUND,
                     phi2=HPS_PRINTS_PHI2,
                     regular=METRIC_ANALYTIC_NEAR_THROAT,
                     free=HPS_FIELD_FREE):
    """Rows (instrument, tag, hypothesis, HPS, verdict); every verdict is
    COMPUTED from the arguments.  Verdict words: MET, MET LOCALLY, FAILS,
    NOT-FOUND, NOT-ESTABLISHED."""
    had = "MET" if hadamard else "NOT-ESTABLISHED"
    ref = "MET" if ref_state else "NOT-FOUND"
    ph2 = "MET" if phi2 else "NOT-FOUND"
    fre = "MET" if free else "FAILS"
    flat = kretschmann == 0
    # DOCKET 67 follow-up: a LOCAL hypothesis is met only where the metric is
    # regular on a neighbourhood (computed: METRIC_ANALYTIC_NEAR_THROAT), not
    # from f0 > 0 and r0 > 0 at one point, which is all it read before.
    local = ("FAILS" if not (f0 > 0 and r0 > 0) else
             "MET LOCALLY" if regular else "NOT-ESTABLISHED")
    rows = []
    for ins, rng in ((FS, FS_XI_RANGE), (FO, FO_XI_RANGE), (FFKP, FFKP_XI_RANGE)):
        hyp = ("any xi" if rng is None else
               "xi = 0 (minimal coupling)" if rng[0] == rng[1] == 0 else
               "%s <= xi <= %s" % rng)
        rows.append((ins, "xi", hyp, "xi = %s" % xi,
                     "MET" if xi_in(xi, rng) else "FAILS"))
    rows += [
        (FS, "hadamard", "Hadamard state", "AHS approximation", had),
        (FO, "geodesic", "timelike geodesic",
         "throat worldline, f'/(2f) = %g" % accel,
         "MET" if accel == 0 else "FAILS"),
        # DOCKET 67 follow-up: FO-P3, restored.  Applied LOCALLY: FO on a
        # globally hyperbolic neighbourhood N of gamma(supp f) taken as a
        # spacetime in its own right.  Computed: the metric is analytic on a
        # neighbourhood of the throat (normal_form()).  NAMED, not computed:
        # a static metric is stably, hence strongly, causal, and a strongly
        # causal spacetime has arbitrarily small globally hyperbolic
        # neighbourhoods; a reference Hadamard state on N exists (Fulling-
        # Narcowich-Wald, NAMED-NOT-READ).
        (FO, "globhyp", "globally hyperbolic spacetime with smooth metric "
         "(restricted to a neighbourhood of gamma(supp f))",
         "metric analytic on |l| < eps (normal form, det factor 3L + 4 = %s); "
         "causality results NAMED" % NORMAL_FORM_DET_FACTOR_AT_PLOTTED, local),
        (FO, "hadamard", "Hadamard state psi (FO: 'on the set of Hadamard "
         "states')", "AHS approximation", had),
        (FO, "ref", "reference Hadamard state omega_0 on HPS", "searched", ref),
        (FO, "phi2", "<:Phi^2:> in the state", "HPS print none", ph2),
        (FFKP, "free", "free scalar on a fixed background (P2)",
         "conformally coupled scalar, m = 0, on metric (2)", fre),
        # DOCKET 67: "MET LOCALLY" below was computed from f0 > 0 and r0 > 0 at
        # one point; it presumed the connection C^{1,1} on a neighbourhood
        # (then not proved).  CORRECTED (follow-up): the regularity is now
        # computed (normal_form(): analytic on |l| < eps) and the row reads it.
        # Whitehead supplies convexity and normality; global hyperbolicity of a
        # small neighbourhood and the one hyperbolic chart (66) stay NAMED.
        (FFKP, "domain", "small sampling domain, globally hyperbolic convex "
         "normal neighbourhood",
         "f(0) = %.4g > 0, r(0) = %.4g > 0, metric analytic near the throat; "
         "Whitehead NAMED" % (f0, r0), local),
        (FFKP, "null", "l^mu null near supp f",
         "radial l; |g(l,l)| = %.1e (float), 0 exactly by sympy" % abs(null_norm),
         "MET" if abs(null_norm) < 1e-12 else "FAILS"),
        (FFKP, "hadamard", "Hadamard state psi (Thm IV.1: 'for all Hadamard "
         "states')", "AHS approximation", had),
        (FFKP, "ref", "W_0 of a reference Hadamard state on HPS", "searched", ref),
        (FFKP, "phi2", "<:phi^2:> in the state", "HPS print none", ph2),
        # DOCKET 67: "kretschmann == 0" is NECESSARY, not sufficient, for flat
        # (a vacuum plane wave has Kretschmann 0 with R_uxux = -1), and
        # "min(radii) > 1" is necessary, not sufficient, for a sampling length l
        # with l_P <= l <= r_c/k to exist (r_c = 7/4 l_P passes, none exists at
        # k = 10).  The clause "sampling << curvature radius" is Kontou 2024
        # Sec. 3.3 on the minimally coupled DSNEC; the l_P floor is this file's
        # premise.  On HPS the row FAILS under either reading.
        (DSN, "flat", "Minkowski, or sampling << curvature radius (>= l_P)",
         "Kretschmann %.3g; radii %s l_P"
         % (kretschmann, ", ".join("%.4g" % x for x in radii)),
         "MET" if (flat or min(radii) > 1) else "FAILS"),
        # DOCKET 67 follow-up: the four DSNEC hypotheses the row dropped.
        (DSN, "free", "free scalar (FFKP Sec. IV.C)",
         "conformally coupled scalar, m = 0", fre),
        (DSN, "hadamard", "Hadamard state psi ((75) is (72) restated)",
         "AHS approximation", had),
        # Minkowski null coordinates (x+, x-, y); on a curved throat no null
        # plane of that kind is established.  Its predicate is the flat row's
        # necessary condition (Kretschmann 0), so it inherits that caveat.
        (DSN, "nullplane", "null-plane smearing f(x+,x-)^2 delta^(n-2)(y) (76)",
         "Kretschmann %.3g" % kretschmann, "MET" if flat else "NOT-ESTABLISHED"),
        # (79) bounds <:phi^2:>_psi; any state whose <:phi^2:> is known and
        # bounded on supp f lies in the class for some phi_max.  HPS print none.
        (DSN, "phimax", "state class <:phi^2:>_psi <= phi_max^2 (79)",
         "HPS print no <phi^2>", "MET" if phi2 else "NOT-ESTABLISHED"),
    ]
    return tuple(rows)


def qei_status(rows, ins):
    """REFUSED if a form hypothesis is not met; OPEN (applies in form, not
    evaluable) if an input is missing; EVALUABLE otherwise.  Returns
    (word, the unmet hypotheses that decide it)."""
    mine = [r for r in rows if r[0] == ins]
    unmet = [r for r in mine if not r[4].startswith("MET")]
    form = [r[2] for r in unmet if r[1] in FORM_TAGS[ins]]
    inputs = [r[2] for r in unmet if r[1] not in FORM_TAGS[ins]]
    if form:
        return "REFUSED", form
    if inputs:
        return "OPEN", inputs
    return "EVALUABLE", []


def throat_verdict(rows, rho_positive):
    """What HPS's positive throat <rho> decides.  SATISFIED only if some
    applicable (not REFUSED) inequality is ABSOLUTE and TIMELIKE -- its left
    side is then HPS's <T(u,u)> itself, and a lower bound <= 0 cannot be
    violated by rho > 0.  Otherwise: NOT A TEST.  CORRECTED (DOCKET 67
    follow-up): the TIMELIKE clause is new -- a null inequality's left side on
    HPS is rho + p_l, not rho (QEI_CONTRACTION)."""
    applicable = [i for i in QEI_KIND if qei_status(rows, i)[0] != "REFUSED"]
    if rho_positive and any(QEI_KIND[i] == "absolute"
                            and QEI_CONTRACTION[i] == "timelike"
                            for i in applicable):
        return "SATISFIED", applicable
    return "NOT A TEST", applicable


def off_throat_status(closed_form, radius_proved):
    return "EVALUABLE" if (closed_form or radius_proved) else "REFUSED"


#: The hypothesis table, computed.
HYPOTHESES = hypothesis_table()
_FS_STATUS, _FS_WHY = qei_status(HYPOTHESES, FS)
_FO_STATUS, _FO_WHY = qei_status(HYPOTHESES, FO)
_FFKP_STATUS, _FFKP_WHY = qei_status(HYPOTHESES, FFKP)
_DSN_STATUS, _DSN_WHY = qei_status(HYPOTHESES, DSN)
_THROAT_WORD, _APPLICABLE = throat_verdict(HYPOTHESES, RHO_THROAT_AT_PLOTTED > 0)
#: DOCKET 67 follow-up: the CONDITIONAL the REFUSED statuses leave standing --
#: the same table with HPS's state taken Hadamard (and nothing else changed).
#: A control, computed, never HPS's status.
_IF_HADAMARD = hypothesis_table(hadamard=True)
CONDITIONAL_IF_HADAMARD = {i: qei_status(_IF_HADAMARD, i) for i in (FO, FFKP)}


def refused_on(rows, ins):
    """The unmet FORM tags of one inequality (computed from the table)."""
    return [r[1] for r in rows if r[0] == ins and r[1] in FORM_TAGS[ins]
            and not r[4].startswith("MET")]


#: every form hypothesis of FO and FFKP other than the Hadamard clause, met?
OTHER_FORM_HYPOTHESES_MET = all(
    r[4].startswith("MET") for r in HYPOTHESES
    if r[0] in (FO, FFKP) and r[1] in FORM_TAGS[r[0]] and r[1] != "hadamard")
_OTHER_MET_WORD = "met" if OTHER_FORM_HYPOTHESES_MET else "NOT all met (see HYPOTHESES)"

#: the references the request cites, parsed from the quoted text
KONTOU_CITED_REFS = tuple(int(x) for x in
                          re.search(r"\[([\d,]+)\]", KONTOU_REQUEST).group(1).split(","))
KONTOU_NAMES_FEWSTER_SMITH = any("0702056" in KONTOU_NAMES.get(k, "") or
                                 "Fewster-Smith" in KONTOU_NAMES.get(k, "")
                                 for k in KONTOU_CITED_REFS)

FS_APPLIES_TO_HPS = _FS_STATUS != "REFUSED"
FEWSTER_SMITH_ON_HPS = ("%s -- not met on HPS's field: %s" % (_FS_STATUS, "; ".join(_FS_WHY))
                        if _FS_STATUS == "REFUSED" else _FS_STATUS)
#: CORRECTED (DOCKET 67 follow-up, M ruled on FFKP; FO held to the same
#: standard).  These read "OPEN -- applies in form (xi, geodesic) but NOT
#: EVALUABLE on HPS: ..." and "OPEN -- applies in form (any xi; small sampling
#: domain, given C^{1,1} regularity near the throat, not proved here; null l)
#: but NOT EVALUABLE on HPS, blocked as FO is: ...".  The words are computed.
FO_ON_HPS = ("%s -- not applicable to HPS's state as published: %s, a "
             "hypothesis of FO Thm 4.2 itself.  Not a finding of violation: if "
             "HPS's state were Hadamard, %s (computed), its only writable "
             "instance (omega_0 = HPS's own state) being vacuous"
             % (_FO_STATUS, "; ".join(_FO_WHY),
                "%s on %s" % (CONDITIONAL_IF_HADAMARD[FO][0],
                              "; ".join(CONDITIONAL_IF_HADAMARD[FO][1]))))
FFKP_IV1_ON_HPS = ("%s -- not applicable to HPS's state as published: %s, a "
                   "hypothesis of Thm IV.1 itself, as for FO.  Not a finding of "
                   "violation: if HPS's state were Hadamard, %s (computed; the "
                   "other form hypotheses -- any xi, free field, small sampling "
                   "domain on the metric's analytic neighbourhood, null l -- "
                   "%s)"
                   % (_FFKP_STATUS, "; ".join(_FFKP_WHY),
                      "%s on %s" % (CONDITIONAL_IF_HADAMARD[FFKP][0],
                                    "; ".join(CONDITIONAL_IF_HADAMARD[FFKP][1])),
                      "are met" if OTHER_FORM_HYPOTHESES_MET else
                      "NOT all met, see HYPOTHESES"))
#: CORRECTED (DOCKET 67 follow-up): the four restored DSNEC hypotheses are
#: named in the word's reason; the status (REFUSED) does not move.
DSNEC_ON_HPS = ("%s -- Minkowski-only; HPS's throat is not flat and its curvature "
                "radius %.4f l_P (Kretschmann definition %.4f l_P) is sub-Planckian; "
                "also unmet on HPS: %s"
                % (_DSN_STATUS, CURVATURE_RADIUS_LP, KRETSCHMANN_RADIUS_LP,
                   "; ".join(w for w in _DSN_WHY if not w.startswith("Minkowski"))))
ABSOLUTE_QEI_FOR_NMC = ("NOT-FOUND -- FO conclusion: 'can also be adapted' "
                        "(expected, not done); alphaXiv search returned none")
#: Kontou's requested test, over BOTH inequalities she names (for O5's text)
#: CORRECTED (DOCKET 67 follow-up).  It read: "FO Thm 4.2 OPEN and FFKP Thm
#: IV.1 (eq. 72) OPEN -- both apply in form to HPS's xi = 1/6 field on the
#: throat worldline (FO: a timelike geodesic; FFKP: a small sampling domain,
#: metric regularity there not proved, and null l) and neither is evaluable
#: (reference state / W_0 and <:Phi^2:> on HPS NOT-FOUND; HPS's state not
#: established Hadamard)".  "Apply in form" omitted both theorems' own
#: Hadamard clause; the statuses are now computed with it.
KONTOU_REQUESTED_TEST_ON_HPS = (
    "FO Thm 4.2 %s and FFKP Thm IV.1 (eq. 72) %s on HPS's xi = %s field -- "
    "both theorems hold only for Hadamard states, and HPS's state (the AHS "
    "approximation) is not established Hadamard; every other form hypothesis "
    "is %s (FO: xi in [0, 1/4], a timelike geodesic, a globally hyperbolic "
    "neighbourhood; FFKP: any xi, free field, a small sampling domain, null l). "
    "Not a finding that HPS violates either: were its state Hadamard both "
    "would be %s/%s, blocked on a reference state / W_0 and <:Phi^2:> on HPS "
    "(NOT-FOUND)"
    % (_FO_STATUS, _FFKP_STATUS, HPS_XI, _OTHER_MET_WORD,
       CONDITIONAL_IF_HADAMARD[FO][0], CONDITIONAL_IF_HADAMARD[FFKP][0]))
DOCKET62_ATTRIBUTION_STANDS = KONTOU_REQUEST_FOUND   # the request exists, Kontou 2024
DOCKET62_INSTRUMENT_STANDS = FS_APPLIES_TO_HPS       # FS on HPS's field
DOCKET62_REFUTATION_SCOPE = (
    "REFUTED FOR HPS's FIELD (xi = %s) only; unaffected for the minimally "
    "coupled corridor (O2): fewsterteo.RIGHT_INSTRUMENT and "
    "throatmass.NARROWING_3_STATUS stand" % HPS_XI)
OFF_THROAT_SMEARED_EVALUATION = (
    "%s -- series radius of convergence not proved; no closed-form solution "
    "in print" % off_throat_status(HPS_PRINTS_CLOSED_FORM_SOLUTION,
                                   TAYLOR_RADIUS_OF_CONVERGENCE_PROVED))

#: CORRECTED (DOCKET 67 follow-up).  It read "... but the applicable QEIs
#: (FO; FFKP) are difference inequalities whose left side is <rho_ren>_Psi -
#: <rho_ren>_Psi0, not HPS's <T>; no applicable QEI is evaluated by it ...".
#: With the Hadamard clause tagged, NO QEI applies to HPS's state; the
#: difference argument survives as the conditional (if Hadamard: FO, FFKP).
VERDICT_THROAT_GEODESIC = (
    "%s -- HPS's own <rho> there is %s/(-L) > 0 (%s at L = %s; THEOREM), but "
    "no QEI applies to HPS's state as published (applicable: %s; refused on "
    "unmet form hypotheses -- %s).  Were the state Hadamard, the applicable "
    "ones (%s) would be difference inequalities (left side <rho_ren>_Psi - "
    "<rho_ren>_Psi0, not HPS's <T>), FFKP's a null one (left side rho + p_l: 0 "
    "on the throat worldline, negative at O(l^2) off it), so rho > 0 would "
    "still decide none ('SATISFIED' withdrawn, DOCKET 64 verifier)"
    % (_THROAT_WORD, RHO_THROAT_COEFF, float(RHO_THROAT_AT_PLOTTED), _L0,
       "; ".join(_APPLICABLE) or "none",
       "; ".join("%s: %s" % (n, ", ".join(refused_on(HYPOTHESES, i)))
                 for n, i in (("FS", FS), ("FO", FO), ("FFKP", FFKP), ("DSNEC", DSN))
                 if refused_on(HYPOTHESES, i)),
       "; ".join(throat_verdict(_IF_HADAMARD, RHO_THROAT_AT_PLOTTED > 0)[1])))
#: WITHDRAWN (DOCKET 64 verifier, SHOULD-FIX).  Kept and marked; never current.
VERDICT_THROAT_GEODESIC_WITHDRAWN = (
    "WITHDRAWN: 'SATISFIED -- <rho> = -45/L > 0 (67.5 at L = -2/3)', and 'the "
    "minimal-coupling flat bound -C_F/tau^4 is satisfied with the whole of "
    "67.5 ||g||^2 to spare' (a minimal-coupling Minkowski bound applied to a "
    "xi = 1/6 field: failure mode 4)")
#: CORRECTED (DOCKET 67 follow-up).  It read "OPEN -- FO Thm 4.2 and FFKP
#: Thm IV.1 apply in form; neither is evaluable on HPS (blockers named in
#: HYPOTHESES)".  The word is computed from the two statuses.
VERDICT_APPLICABLE_QEI = (
    "%s -- FO Thm 4.2 and FFKP Thm IV.1 do not apply to HPS's state as "
    "published (their Hadamard clause NOT-ESTABLISHED); were it Hadamard, "
    "both %s and neither evaluable (blockers named in HYPOTHESES)"
    % (_FO_STATUS if _FO_STATUS == _FFKP_STATUS
       else "%s/%s" % (_FO_STATUS, _FFKP_STATUS),
       "/".join(sorted({CONDITIONAL_IF_HADAMARD[i][0] for i in (FO, FFKP)}))))

#: the unique single-coefficient repair found by repair_scan(); --selftest
#: re-runs the scan and compares.  (component, monomial, printed, repaired)
REPAIR_DIMENSION = ("ll-log", "f'^2 r'^2/(f^2 r)", "/(f^2 r)", "/(f^2 r^2)")
REPAIR_CONSERVATION = ("tt-log", "f'^2 f''/f^3", 16, 116)


# ---------------------------------------------------------------------------
# HPS eqs. (5)-(7), as the text layer reads them.  printed=True keeps the two
# defects; printed=False applies the two repairs of section 2.
# ---------------------------------------------------------------------------

def hps_system(sp, printed=False):
    l = sp.Symbol('l', real=True)
    f = sp.Function('f')(l)
    r = sp.Function('r')(l)
    f1, f2, f3, f4 = [f.diff(l, k) for k in (1, 2, 3, 4)]
    r1, r2, r3, r4 = [r.diff(l, k) for k in (1, 2, 3, 4)]
    At = (32/r**4 + 7*f1**4/f**4 - 24*f1**3*r1/(f**3*r) + 24*f1**2*r1**2/(f**2*r**2)
          - 32*r1**4/r**4 + 4*f1**2*f2/f**3 - 12*f2**2/f**2 + 80*f1**2*r2/(f**2*r)
          - 160*f1*r1*r2/(f*r**2) + 128*r1**2*r2/r**3 - 64*f2*r2/(f*r) + 32*r2**2/r**2
          - 16*f1*f3/f**2 + 64*r1*f3/(f*r) - 96*f1*r3/(f*r) - 64*r1*r3/r**2
          + 16*f4/f - 64*r4/r)
    c_tt = 16 if printed else 116
    Bt = (16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2)
          - 16*r1**4/r**4 + c_tt*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2
          + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3
          + 16*f2*r2/(f*r) + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r)
          - 16*f1*r3/(f*r) - 32*r1*r3/r**2 + 16*f4/f - 32*r4/r)
    Al = (f1**4/f**4 - 16*f1**3*r1/(f**3*r) + 64*f1*r1**3/(f*r**3) - 4*f1**2*f2/f**3
          + 64*f1*r1*f2/(f**2*r) - 64*r1**2*f2/(f*r**2) - 4*f2**2/f**2
          - 48*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) + 32*f2*r2/(f*r)
          + 8*f1*f3/f**2 - 32*r1*f3/(f*r) - 32*f1*r3/(f*r))
    den = r if printed else r**2
    Bl = (16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*den)
          + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3
          + 48*f1*r1*f2/(f**2*r) - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2
          - 16*f1**2*r2/(f**2*r) + 16*f1*r1*r2/(f*r**2) + 16*f2*r2/(f*r)
          - 16*r2**2/r**2 + 8*f1*f3/f**2 - 16*r1*f3/(f*r) - 16*f1*r3/(f*r)
          + 32*r1*r3/r**2)
    Ah = (17*f1**4/f**4 - 16*f1**3*r1/(f**3*r) - 32*f1*r1**3/(f*r**3)
          - 52*f1**2*f2/f**3 + 32*f1*r1*f2/(f**2*r) + 32*r1**2*f2/(f*r**2)
          + 28*f2**2/f**2 + 16*f1**2*r2/(f**2*r) + 64*f1*r1*r2/(f*r**2)
          - 32*f2*r2/(f*r) + 24*f1*f3/f**2 - 48*r1*f3/(f*r) + 32*f1*r3/(f*r)
          - 16*f4/f)
    Bh = (-16/r**4 + 21*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2)
          - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3
          + 28*f1*r1*f2/(f**2*r) + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2
          + 4*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) - 32*r1**2*r2/r**3
          - 16*f2*r2/(f*r) + 20*f1*f3/f**2 - 24*r1*f3/(f*r) + 16*f1*r3/(f*r)
          - 8*f4/f + 16*r4/r)
    Gt = 2*r2/r + r1**2/r**2 - 1/r**2          # HPS's printed left sides
    Gl = f1*r1/(f*r) + r1**2/r**2 - 1/r**2
    Gh = f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2)
    return dict(l=l, f=f, r=r, A=(At, Al, Ah), B=(Bt, Bl, Bh), G=(Gt, Gl, Gh),
                K2=sp.Rational(HPS_K2_TIMES_PI.numerator, HPS_K2_TIMES_PI.denominator) / sp.pi)


def _cons(sp, S, T):
    """nabla_mu T^mu_l for diagonal T = (T^t_t, T^l_l, T^th_th) in metric (2)."""
    l, f, r = S['l'], S['f'], S['r']
    Tt, Tl, Th = T
    return sp.diff(Tl, l) + f.diff(l)/(2*f)*(Tl - Tt) + 2*r.diff(l)/r*(Tl - Th)


def conservation(sp, printed=False):
    """(total residual, log-bracket residual, log-bracket trace)."""
    S = hps_system(sp, printed)
    lf = sp.log(S['f'])
    T = tuple(a + lf*b for a, b in zip(S['A'], S['B']))
    tot = sp.simplify(sp.expand(_cons(sp, S, T)))
    Bc = sp.simplify(sp.expand(_cons(sp, S, S['B'])))
    Bt, Bl, Bh = S['B']
    tr = sp.simplify(Bt + Bl + 2*Bh)
    return tot, Bc, tr


def dimension_defects(sp, printed=True):
    """Terms of the RHS brackets that do not scale as length^-4 under
    l -> lam l, r -> lam r (f dimensionless)."""
    S = hps_system(sp, printed)
    l, f, r = S['l'], S['f'], S['r']
    lam = sp.Symbol('lam', positive=True)
    subs = {}
    for k in (4, 3, 2, 1):
        subs[f.diff(l, k)] = sp.Symbol('F%d' % k) * lam**(-k)
        subs[r.diff(l, k)] = sp.Symbol('R%d' % k) * lam**(1 - k)
    subs[f] = sp.Symbol('F0')
    subs[r] = sp.Symbol('R0') * lam
    bad = []
    for name, X in zip(("tt", "ll", "th", "tt-log", "ll-log", "th-log"),
                       S['A'] + S['B']):
        for m in sp.Add.make_args(sp.expand(X)):
            ms = m.xreplace(subs)
            sc = sp.simplify(ms / ms.subs(lam, 1))
            if sp.simplify(sc - lam**-4) != 0:
                bad.append((name, m))
    return bad


def repair_scan(sp):
    """With the dimension repair applied and the tt coefficient AS PRINTED (16),
    try every single change delta*m to one printed log-bracket monomial m:
    return those for which a CONSTANT delta makes the full tensor conserved
    AND the log bracket traceless."""
    S = hps_system(sp, printed=False)
    l, f, r = S['l'], S['f'], S['r']
    f1, f2 = f.diff(l), f.diff(l, 2)
    Bt, Bl, Bh = S['B']
    Bt = Bt - 100*f1**2*f2/f**3                       # back to the printed 16
    lf = sp.log(f)
    T = tuple(a + lf*b for a, b in zip(S['A'], (Bt, Bl, Bh)))
    R0 = sp.simplify(sp.expand(_cons(sp, S, T)))
    tr0 = sp.simplify(Bt + Bl + 2*Bh)
    hits = []
    for comp, X in (("tt-log", Bt), ("ll-log", Bl), ("th-log", Bh)):
        for m in sp.Add.make_args(sp.expand(X)):
            if comp == "tt-log":
                eff = -lf*f1/(2*f)*m
                etr = m
            elif comp == "th-log":
                eff = -lf*2*r.diff(l)/r*m
                etr = 2*m
            else:
                eff = (lf*(sp.diff(m, l) + (f1/(2*f) + 2*r.diff(l)/r)*m)
                       + f1/f*m)
                etr = m
            eff = sp.simplify(eff)
            if eff == 0:
                continue
            d = sp.simplify(-R0/eff)
            if d.has(l) or d.has(f) or d.has(r):
                continue
            if sp.simplify(tr0 + d*etr) != 0:
                continue
            hits.append((comp, m, d))
    return R0, hits


def einstein_and_anomaly(sp):
    """(1) printed left sides - G^mu_nu of metric (2); (2) the constant c in
    trace(A) = 16 (Riem^2 - Ric^2 + c Box R), for both overall signs;
    (3) the Kretschmann scalar at throat data."""
    S = hps_system(sp)
    l, f, r = S['l'], S['f'], S['r']
    t, th, ph = sp.symbols('t theta phi')
    X = [t, l, th, ph]
    g = sp.diag(-f, 1, r**2, r**2*sp.sin(th)**2)
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Rm = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c]
                             for k in range(n))
                    Rm[a, b, c, d] = sp.simplify(e)
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rm[a, b, a, d] for a in range(n))))
    Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    Gmix = sp.simplify(gi*(Ric - Rs*g/2))
    lhs = tuple(sp.simplify(Gmix[i, i] - S['G'][j]) for j, i in enumerate((0, 1, 2)))
    Kr = 0
    for (a, b, c, d), v in Rm.items():
        if v != 0:
            Kr += (g[a, a]*v)**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
    Kr = sp.simplify(Kr)
    Ric2 = sp.simplify(sum(Ric[a, b]**2*gi[a, a]*gi[b, b] for a in range(n) for b in range(n)))
    boxR = sp.simplify(sp.diff(Rs, l, 2) + (f.diff(l)/(2*f) + 2*r.diff(l)/r)*sp.diff(Rs, l))
    At, Al, Ah = S['A']
    trA = sp.simplify(At + Al + 2*Ah)
    c = sp.Symbol('c')
    gens = [f, r] + [f.diff(l, k) for k in range(1, 5)] + [r.diff(l, k) for k in range(1, 5)]
    sols = {}
    for s in (1, -1):
        num = sp.numer(sp.together(sp.expand(trA - s*16*(Kr - Ric2) - c*16*boxR)))
        sols[s] = sp.solve(sp.Poly(sp.expand(num), *gens).coeffs(), c, dict=True)
    z = {f.diff(l, k): HPS_DATA_9_F[k] for k in (2, 1)}
    z.update({r.diff(l, k): HPS_DATA_9_R[k] for k in (2, 1)})
    Kr0 = sp.simplify(Kr.subs(z))
    # orthonormal components R_(abcd) = g_aa R^a_bcd / sqrt|g_aa g_bb g_cc g_dd|,
    # squared (to stay rational), at the throat data; and the signed
    # R_(theta phi theta phi)
    ortho2 = {}
    for (a, b, c, d), v in Rm.items():
        w = sp.simplify(((g[a, a]*v)**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]).subs(z))
        if w != 0:
            ortho2[a, b, c, d] = w
    R_thph = sp.simplify((g[2, 2]*Rm[2, 3, 2, 3]/(g[2, 2]*g[3, 3])).subs(z))
    return lhs, sols, Kr0, ortho2, R_thph


def static_acceleration(sp):
    """The 4-acceleration of the static observer u = f^(-1/2) d_t of metric
    (2), DERIVED from the Christoffel symbols: a^l = Gamma^l_tt (u^t)^2.
    Returns (a^l as a function of l, a^l at HPS data (9) with ln f(0) = L)."""
    l = sp.Symbol('l', real=True)
    t = sp.Symbol('t')
    f = sp.Function('f')(l)
    r = sp.Function('r')(l)
    th = sp.Symbol('theta')
    X = [t, l, th, sp.Symbol('phi')]
    g = sp.diag(-f, 1, r**2, r**2*sp.sin(th)**2)
    gi = g.inv()
    Gam_ltt = sp.simplify(sum(gi[1, d]*(2*sp.diff(g[d, 0], X[0]) - sp.diff(g[0, 0], X[d]))
                              for d in range(4))/2)
    a = sp.simplify(Gam_ltt/f)
    L = sp.Symbol('L', real=True)
    a0 = sp.simplify(a.subs(f.diff(l), HPS_DATA_9_F[1]).subs(f, sp.exp(L)))
    return dict(l=l, f=f, a=a, a0=a0, L=L)


def radial_null_norm(sp):
    """g(l, l) for l = f^(-1/2) d_t + d_l in metric (2), exactly."""
    l = sp.Symbol('l', real=True)
    f = sp.Function('f')(l)
    ell = (1/sp.sqrt(f), 1)
    return sp.simplify(-f*ell[0]**2 + ell[1]**2)


# ---------------------------------------------------------------------------
# Section 3: the throat.
# ---------------------------------------------------------------------------

def throat(sp):
    """Exact throat quantities as functions of L = ln f(0), HPS data (9).  The
    Lambda = alpha = beta = 0, N = 1, unreduced member of the semiclassical
    equation (section 3's named hypotheses, DOCKET 67)."""
    S = hps_system(sp)
    l, f, r, K2 = S['l'], S['f'], S['r'], S['K2']
    L, a, b = sp.symbols('L a b', real=True)
    rt = sp.Symbol('rt', positive=True)

    def at0(e):
        e = e.subs({f.diff(l, 4): a*sp.exp(L), r.diff(l, 4): b*rt})
        e = e.subs({f.diff(l, k): HPS_DATA_9_F[k] for k in (3, 2, 1)})
        e = e.subs({r.diff(l, k): HPS_DATA_9_R[k] for k in (3, 2, 1)})
        return sp.simplify(e.subs({f: sp.exp(L), r: rt}))
    lf = sp.log(f)
    E = [at0(G - K2*(A + lf*B)) for G, A, B in zip(S['G'], S['A'], S['B'])]
    r0 = [s for s in sp.solve(sp.Eq(E[1], 0), rt) if s.is_positive is not False]
    rr = sp.sqrt(-16*K2*L)
    sol = sp.solve([E[0].subs(rt, rr), E[2].subs(rt, rr)], [a, b], dict=True)[0]
    A4, B4 = sp.factor(sol[a]), sp.factor(sol[b])
    rho = sp.simplify(1/(8*sp.pi*rr**2))
    # p_l from the ll RIGHT side alone (no fourth derivatives): 8 pi p_l = K2*16 L / r^4
    p_l_rhs = sp.simplify(K2*16*L/rr**4/(8*sp.pi))
    # series of 8 pi (rho + p_l) = G^l_l - G^t_t about the throat, to O(l^2)
    lam = sp.Symbol('lam', real=True)
    fser = sp.exp(L)*(1 + A4*lam**4/24)
    rser = rr*(1 + B4*lam**4/24)
    nec = (sp.diff(fser, lam)*sp.diff(rser, lam)/(fser*rser)
           - 2*sp.diff(rser, lam, 2)/rser)
    nec2 = sp.simplify(sp.series(nec, lam, 0, 3).removeO().coeff(lam, 2))
    Gt = (2*sp.diff(rser, lam, 2)/rser + sp.diff(rser, lam)**2/rser**2 - 1/rser**2)
    rho2 = sp.simplify(sp.series(-Gt/(8*sp.pi), lam, 0, 3).removeO().coeff(lam, 2))
    return dict(L=L, r0_ll=r0, r0=rr, A4=A4, B4=B4, rho=rho, p_l_rhs=p_l_rhs,
                p_t=sp.simplify(at0(S['G'][2]) / (8*sp.pi)),
                nec2=nec2, rho2=rho2)


def normal_form(sp):
    """DOCKET 67 follow-up: the regularity ground behind every LOCAL hypothesis
    (FO "globally hyperbolic, smooth metric" restricted to a neighbourhood;
    FFKP's small sampling domain).  Returns
      det   the determinant of the (f'''', r'''') coefficient matrix of the tt
            and theta-theta equations E = G - K^2 (A + ln f B), generic point;
      El4   d E_l / d(f'''', r'''') (the ll equation is a constraint: (0, 0));
      div   nabla_mu E^mu_l, off shell (the identity that propagates it);
      det0  det at data (9), as a function of L (f = e^L, r = sqrt(-16K^2L)).
    With det0 != 0 the reduced system is a regular analytic ODE in normal form
    at the data point (Cauchy's existence theorem, NAMED, gives a unique
    analytic solution on some |l| < eps), and E_l' = -(f'/(2f) + 2r'/r) E_l,
    E_l(0) = 0, then gives E_l = 0 there."""
    S = hps_system(sp)
    l, f, r, K2 = S['l'], S['f'], S['r'], S['K2']
    f4, r4 = f.diff(l, 4), r.diff(l, 4)
    lf = sp.log(f)
    E = [G - K2*(A + lf*B) for G, A, B in zip(S['G'], S['A'], S['B'])]
    M = sp.Matrix([[sp.diff(E[i], v) for v in (f4, r4)] for i in (0, 2)])
    det = sp.factor(sp.simplify(M.det()))
    El4 = (sp.simplify(sp.diff(E[1], f4)), sp.simplify(sp.diff(E[1], r4)))
    div = sp.simplify(_cons(sp, S, E))
    L = sp.Symbol('L', real=True)
    det0 = sp.factor(sp.simplify(det.subs({f: sp.exp(L), r: sp.sqrt(-16*K2*L)})))
    return dict(det=det, El4=El4, div=div, det0=det0, L=L, f=f, r=r)


def throat_signs_z3():
    """z3 over the reals: on HPS's range -1 <= L < 0 is there ANY L with
    r4/r <= 0, f4/f < 0, or rho <= 0?  Each must be UNSAT.  CONTROLS: just
    outside the range the same formulas DO change sign -- f4/f < 0 on
    (-4/3, -1), r4/r < 0 on (-sqrt 2, -4/3) -- and the solver must say SAT."""
    import z3
    L = z3.Real('L')
    dom = z3.And(L >= -1, L < 0)
    B4 = (2 - L*L) / (L*L*(3*L + 4))        # r4/r over 129600 pi^2 > 0
    A4 = (-L - 1) / (L*(3*L + 4))           # f4/f over 259200 pi^2 > 0
    rho = -45 / L

    def sat(*c):
        s = z3.Solver()
        s.add(*c)
        return str(s.check())
    return {'r4<=0': sat(dom, B4 <= 0), 'f4<0': sat(dom, A4 < 0),
            'rho<=0': sat(dom, rho <= 0),
            'control f4': sat(L > z3.RealVal(-4) / 3, L < -1, A4 < 0),
            'control r4': sat(L > z3.RealVal(-141) / 100, L < z3.RealVal(-134) / 100,
                              B4 < 0)}


# ---------------------------------------------------------------------------
# Section 5: controls.
# ---------------------------------------------------------------------------

def fo_flat_coefficient(sp):
    """FO eq. (53), massless n = 4, integrated directly; and eq. (55) read off.
    Both return c(xi) with Qt_A = (1/(4 pi^3)) c(xi) INT_0^oo |fhat|^2 u^4."""
    k, u = sp.symbols('k u', positive=True)
    xi = sp.Symbol('xi', real=True)
    c53 = sp.simplify(sp.integrate(k*((1 - 2*xi)*k**2 + 2*xi*(u - k)**2), (k, 0, u)) / u**4)
    n = 4
    c55 = sp.Rational(1, n) - 4*xi/(n - 1) + 2*xi/(n - 2)     # Q_{n,k} -> 1, m -> 0
    S2 = 4*sp.pi                                              # S_{n-2} = S_2
    pref = S2 / (2*sp.pi)**n
    return xi, c53, sp.simplify(c55), sp.simplify(pref)


def clamped_beam_ratio(sp, mp, mu):
    """INT (g'')^2 / INT g^2 for the clamped-beam fundamental on [0, 1], by
    quadrature -- NOT by the identity that makes it mu^4.  g'' by sympy."""
    x, m, sg = sp.symbols('x m sg', real=True)
    ge = sp.cosh(m*x) - sp.cos(m*x) - sg*(sp.sinh(m*x) - sp.sin(m*x))
    g = sp.lambdify((x, m, sg), ge, 'mpmath')
    g2 = sp.lambdify((x, m, sg), sp.diff(ge, x, 2), 'mpmath')
    sig = (mp.cosh(mu) - mp.cos(mu)) / (mp.sinh(mu) - mp.sin(mu))
    num = mp.quad(lambda y: g2(y, mu, sig)**2, [0, 0.5, 1])
    den = mp.quad(lambda y: g(y, mu, sig)**2, [0, 0.5, 1])
    return num / den


def bump(sp, mp, tau):
    """C-infinity sampler exp(-1/(1-(t/tau)^2)) on |t| < tau, zero outside; its
    first two derivatives by sympy (exact), evaluated in mpmath."""
    t = sp.Symbol('t', real=True)
    T = sp.Symbol('T', positive=True)
    ge = sp.exp(-1/(1 - (t/T)**2))
    fs = [sp.lambdify((t, T), sp.diff(ge, t, k), 'mpmath') for k in (0, 1, 2)]

    def mk(F):
        return lambda x: F(x, tau) if abs(x) < tau else mp.mpf(0)
    return tuple(mk(F) for F in fs)


def fo_state_sympy(sp):
    """FO's one-particle state (their (25)), kappa symbolic: psi(t) at x = 0,
    re-derived energy density (their (24)), and <:Phi^2:>; plus norm/energy."""
    t, k = sp.symbols('t k', real=True)
    kap = sp.Symbol('kappa', positive=True)
    xi = sp.Symbol('xi', real=True)
    h = 4*sp.pi*sp.sqrt(2)*(kap - k/3)*sp.exp(-k/kap)/kap**2
    psi = sp.simplify(sp.integrate(k*sp.exp(-sp.I*t*k)*h, (k, 0, sp.oo), conds='none')
                      / (4*sp.pi**2))
    d1, d2 = sp.diff(psi, t), sp.diff(psi, t, 2)
    rho = sp.simplify(sp.expand_complex(d1*sp.conjugate(d1))
                      - 4*xi*sp.re(sp.expand_complex(sp.conjugate(psi)*d2)))
    s = t*kap
    fo28 = 8*kap**4/(3*(1 + s**2)**5*sp.pi**2)*((3*s**4 + 3*s**2) - xi*(18*s**4 - 44*s**2 + 2))
    phi2 = sp.simplify(2*sp.expand_complex(psi*sp.conjugate(psi)))
    dmu = 4*sp.pi*k**2/((2*sp.pi)**3*2*k)
    norm = sp.simplify(sp.integrate(dmu*h**2, (k, 0, sp.oo)))
    energy = sp.simplify(sp.integrate(dmu*k*h**2, (k, 0, sp.oo)))
    return dict(t=t, kap=kap, xi=xi, rho=rho, fo28=fo28, phi2=phi2,
                norm=norm, energy=energy)


def violation_control(sp, mp, tau=0.1):
    """kappa = 1, xi = HPS_XI (1/6), C-infinity bump of half-width tau.  Returns
    (L1, B_min, Qt_A, Phi-slope, j*) where L1 = INT g^2 <rho>_1,
    B_min = (1/16 pi^2) INT (g'')^2, Qt_A = (1 - 4 xi/3) B_min,
    slope = L1 + xi INT <:Phi^2:>_1 2 g'^2 (FO holds at every j iff >= 0),
    j* = least j with j L1 < -B_min."""
    mp.mp.dps = 30
    st = fo_state_sympy(sp)
    xi = sp.Rational(HPS_XI.numerator, HPS_XI.denominator)
    rho1 = sp.lambdify(st['t'], st['rho'].subs({st['kap']: 1, st['xi']: xi}), 'mpmath')
    phi2 = sp.lambdify(st['t'], st['phi2'].subs(st['kap'], 1), 'mpmath')
    g, gp, gpp = bump(sp, mp, tau)
    iv = [-tau, 0, tau]
    L1 = mp.quad(lambda t: g(t)**2*rho1(t), iv)
    Bmin = mp.quad(lambda t: gpp(t)**2, iv) / (16*mp.pi**2)
    xm = mp.mpf(HPS_XI.numerator)/HPS_XI.denominator
    QA = (1 - mp.mpf(4)/3*xm) * Bmin
    slope = L1 + xm*mp.quad(lambda t: phi2(t)*2*gp(t)**2, iv)
    jstar = int(mp.floor(Bmin / (-L1))) + 1 if L1 < 0 else None
    return L1, Bmin, QA, slope, jstar


# ---------------------------------------------------------------------------
# report / selftest
# ---------------------------------------------------------------------------

def report():
    print(__doc__.split("=====", 1)[0].strip())
    import sympy as sp
    T = throat(sp)
    L0 = sp.Rational(*HPS_PLOTTED_LNF0)
    print("\nREQUEST (%s):\n  %s" % (KONTOU_SOURCE, KONTOU_REQUEST))
    print("\nHYPOTHESES (every verdict computed):")
    for ins, _tag, hyp, obj, v in HYPOTHESES:
        print("  %-38s %-44s %s\n  %38s %-44s" % (ins, hyp, v, "", "HPS: " + obj))
    print("\nTHROAT (L = ln f(0) = %s):" % L0)
    print("  r_0^2          = %s" % sp.simplify(T['r0'].subs(T['L'], L0)**2))
    print("  f''''(0)/f(0)  = %s" % sp.simplify(T['A4'].subs(T['L'], L0)))
    print("  r''''(0)/r(0)  = %s" % sp.simplify(T['B4'].subs(T['L'], L0)))
    print("  rho            = %s" % sp.simplify(T['rho'].subs(T['L'], L0)))
    print("  rho + p_l      = %s l^2 + O(l^4)"
          % sp.simplify(T['nec2'].subs(T['L'], L0) / (8*sp.pi)))
    print("  curvature radius: %s" % CURVATURE_RADIUS_DEFINITION)
    print("\nVERDICT, throat geodesic : %s" % VERDICT_THROAT_GEODESIC)
    print("  (withdrawn)            : %s" % VERDICT_THROAT_GEODESIC_WITHDRAWN)
    print("VERDICT, applicable QEIs : %s" % VERDICT_APPLICABLE_QEI)
    print("FO Thm 4.2 on HPS        : %s" % FO_ON_HPS)
    print("FFKP Thm IV.1 on HPS     : %s" % FFKP_IV1_ON_HPS)
    print("Fewster-Smith on HPS     : %s" % FEWSTER_SMITH_ON_HPS)
    print("  DOCKET 62 instrument   : %s" % DOCKET62_REFUTATION_SCOPE)
    print("DSNEC on HPS             : %s" % DSNEC_ON_HPS)
    print("Off-throat smeared       : %s" % OFF_THROAT_SMEARED_EVALUATION)
    return 0


def selftest():
    import sympy as sp
    import mpmath as mp
    ok = True
    n_chk = [0, 0]      # computed checks, record pins

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        n_chk[0] += 1
        print("  [%s] %-64s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def pin(label, got, want):
        """RECORD PIN: restates what was READ or searched.  It fails only if
        the record is edited; it is not a control and is counted apart."""
        nonlocal ok
        good = got == want
        ok &= good
        n_chk[1] += 1
        print("  [%s] %-64s %s" % ("pin" if good else "XX", label,
                                    got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol):
        nonlocal ok
        d = abs(got - want) / max(mp.mpf('1e-40'), abs(want))
        good = d <= tol
        ok &= good
        n_chk[0] += 1
        print("  [%s] %-64s %s (rel %.1e)" % ("ok" if good else "XX", label,
                                              mp.nstr(got, 15), float(d)))

    def verdict(rows, ins, tag):
        return [r[4] for r in rows if r[0] == ins and r[1] == tag]

    def _swapped(table, key, value, fn):
        """fn() with table[key] = value, restored afterwards (a control)."""
        old = table[key]
        table[key] = value
        try:
            return fn()
        finally:
            table[key] = old

    print("qeihps.py --selftest\n")
    print("0. THE REQUEST AND ITS NAMES (READ)")
    pin("Kontou's request found at source (record of the reading)",
        KONTOU_REQUEST_FOUND, True)
    chk("the request's cited refs, parsed from the quote, are the names held",
        KONTOU_CITED_REFS, tuple(sorted(KONTOU_NAMES)))
    chk("  and none of them is Fewster-Smith (computed from the names)",
        KONTOU_NAMES_FEWSTER_SMITH, False)
    pin("HPS's field: xi = 1/6 (record of HPS's text)", HPS_XI, Fraction(1, 6))
    pin("HPS's field: massless, zero temperature (fn [20])",
        HPS_MASS_TEMPERATURE, (0, 0))
    pin("NOT-FOUND records: reference state, <phi^2>, Hadamard, closed form",
        (REFERENCE_STATE_ON_HPS_FOUND, HPS_PRINTS_PHI2,
         HPS_STATE_HADAMARD_ESTABLISHED, HPS_PRINTS_CLOSED_FORM_SOLUTION,
         TAYLOR_RADIUS_OF_CONVERGENCE_PROVED), (False,)*5)
    pin("HPS's field is a free scalar (record; audit 2309.10848-thmiv.1 P2)",
        HPS_FIELD_FREE, True)

    print("\n1. HYPOTHESES -- every verdict COMPUTED; each predicate has a control")
    chk("CONTROL xi predicate: xi = 0 meets FS's range", xi_in(Fraction(0), FS_XI_RANGE), True)
    chk("CONTROL xi predicate: xi = 1/3 fails FO's [0, 1/4]",
        xi_in(Fraction(1, 3), FO_XI_RANGE), False)
    chk("CONTROL xi predicate: xi = 1/4 meets FO's closed range",
        xi_in(Fraction(1, 4), FO_XI_RANGE), True)
    acc = static_acceleration(sp)
    chk("static-observer acceleration from Christoffels = f'/(2f) (sympy)",
        sp.simplify(acc['a'] - acc['f'].diff(acc['l'])/(2*acc['f'])), 0)
    chk("  at HPS data (9): exactly 0", acc['a0'], 0)
    a0_plotted = float(acc['a0'].subs(acc['L'], sp.Rational(*HPS_PLOTTED_LNF0)))
    chk("  equals the stdlib THROAT_ACCELERATION the table uses",
        a0_plotted == THROAT_ACCELERATION, True)
    chk("radial l = f^(-1/2) d_t + d_l is null in metric (2), exactly (sympy)",
        radial_null_norm(sp), 0)
    rows = hypothesis_table(xi=HPS_XI, accel=a0_plotted)
    chk("table rebuilt from the sympy acceleration == HYPOTHESES (%d rows)" % len(rows),
        rows == HYPOTHESES, True)
    chk("Fewster-Smith: minimal coupling (from HPS_XI)", verdict(rows, FS, "xi"), ["FAILS"])
    chk("Fewster-Osterbrink: 0 <= xi <= 1/4 (from HPS_XI)", verdict(rows, FO, "xi"), ["MET"])
    chk("Fewster-Osterbrink: timelike geodesic (from f'/(2f) at data (9))",
        verdict(rows, FO, "geodesic"), ["MET"])
    chk("FFKP Thm IV.1: any xi / free / sampling domain / null l",
        [verdict(rows, FFKP, t)[0] for t in ("xi", "free", "domain", "null")],
        ["MET", "MET", "MET LOCALLY", "MET"])
    chk("DSNEC: Minkowski or radius >= l_P (from the curvature)",
        verdict(rows, DSN, "flat"), ["FAILS"])

    print("\n1b. METRIC REGULARITY NEAR THE THROAT (DOCKET 67 follow-up; sympy)")
    nf = normal_form(sp)
    fq, rq = nf['f'], nf['r']
    chk("det of the (f4, r4) matrix of the tt, th eqs = -(3 ln f + 4)/(129600 pi^2 f r)",
        sp.simplify(nf['det'] + (3*sp.log(fq) + 4)/(129600*sp.pi**2*fq*rq)), 0)
    chk("  the ll equation carries no fourth derivative (a constraint)",
        nf['El4'], (0, 0))
    chk("  div(G - K^2(A + ln f B)) = 0 identically, off shell (propagates it)",
        nf['div'], 0)
    Lq = nf['L']
    chk("  at data (9): det = -sqrt(10)(3L+4) e^-L/(21600 pi^(3/2) sqrt(-L))",
        sp.simplify(nf['det0'] + sp.sqrt(10)*(3*Lq + 4)*sp.exp(-Lq)
                    / (21600*sp.pi**sp.Rational(3, 2)*sp.sqrt(-Lq))), 0)
    chk("  its only real zero is L = -4/3, outside HPS's -1 <= L < 0",
        sp.solve(sp.Eq(nf['det0'], 0), Lq), [sp.Rational(-4, 3)])
    chk("  3L + 4 at L = -2/3 == stdlib NORMAL_FORM_DET_FACTOR_AT_PLOTTED (= 2)",
        (3*sp.Rational(*HPS_PLOTTED_LNF0) + 4,
         NORMAL_FORM_DET_FACTOR_AT_PLOTTED), (2, 2))
    chk("  so METRIC_ANALYTIC_NEAR_THROAT (computed), and over HPS's family "
        "min(3L+4) on [-1, 0) = 1 > 0",
        (METRIC_ANALYTIC_NEAR_THROAT, 3*(-1) + 4), (True, 1))
    chk("CONTROL normal form: at L = -4/3 (outside HPS's family) the det vanishes",
        sp.simplify(nf['det0'].subs(Lq, sp.Rational(-4, 3))), 0)
    ctl_irr = hypothesis_table(regular=False)
    chk("CONTROL regularity unproved -> FO globhyp and FFKP domain NOT-ESTABLISHED",
        (verdict(ctl_irr, FO, "globhyp"), verdict(ctl_irr, FFKP, "domain")),
        (["NOT-ESTABLISHED"], ["NOT-ESTABLISHED"]))
    chk("CONTROL degenerate point (f0 = 0) -> both FAILS",
        (verdict(hypothesis_table(f0=0), FO, "globhyp"),
         verdict(hypothesis_table(f0=0), FFKP, "domain")), (["FAILS"], ["FAILS"]))
    chk("Fewster-Osterbrink: globally hyperbolic, smooth metric (restored; local)",
        verdict(rows, FO, "globhyp"), ["MET LOCALLY"])
    chk("CONTROL free field: a non-free field FAILS FFKP's P2 and the DSNEC's",
        (verdict(hypothesis_table(free=False), FFKP, "free"),
         verdict(hypothesis_table(free=False), DSN, "free")), (["FAILS"], ["FAILS"]))
    ctl_geo = hypothesis_table(accel=static_acceleration_at(1, float(_L0)))
    chk("CONTROL geodesic: with f'(0) = 1 the throat worldline FAILS",
        verdict(ctl_geo, FO, "geodesic"), ["FAILS"])
    ctl_min = hypothesis_table(xi=Fraction(0))
    chk("CONTROL minimal field: FS xi row MET at xi = 0",
        verdict(ctl_min, FS, "xi"), ["MET"])
    chk("CONTROL flat: Kretschmann 0 meets the DSNEC row (necessary, not "
        "sufficient, for Minkowski)",
        verdict(hypothesis_table(kretschmann=0), DSN, "flat"), ["MET"])
    # DOCKET 67 follow-up: the flat control used to return ('EVALUABLE', [])
    # with <phi^2> NOT-FOUND (audit 2309.10848-dsnec).  With (79), Hadamard and
    # the null plane tagged it is refused on the state, and evaluable only
    # when the state's hypotheses are met too.
    chk("CONTROL flat, state unknown: DSNEC REFUSED on Hadamard and (79), not "
        "EVALUABLE",
        qei_status(hypothesis_table(kretschmann=0), DSN),
        ("REFUSED", ["Hadamard state psi ((75) is (72) restated)",
                     "state class <:phi^2:>_psi <= phi_max^2 (79)"]))
    ctl_flat = hypothesis_table(kretschmann=0, hadamard=True, phi2=True)
    chk("CONTROL flat, Hadamard, <phi^2> known: DSNEC EVALUABLE",
        qei_status(ctl_flat, DSN), ("EVALUABLE", []))
    chk("CONTROL throat_verdict: DSNEC absolute but NULL -> still NOT A TEST "
        "(xi = 1/6: FS refused; no absolute timelike QEI applies)",
        throat_verdict(ctl_flat, True), ("NOT A TEST", [FO, FFKP, DSN]))
    chk("  the null clause bites: same catalogue, DSNEC read timelike -> SATISFIED",
        (QEI_KIND[DSN], QEI_CONTRACTION[DSN],
         _swapped(QEI_CONTRACTION, DSN, "timelike",
                  lambda: throat_verdict(ctl_flat, True)[0])),
        ("absolute", "null", "SATISFIED"))
    ctl_all = hypothesis_table(xi=Fraction(0), hadamard=True, ref_state=True, phi2=True)
    chk("CONTROL qei_status: all inputs present -> FO EVALUABLE, FS applies",
        (qei_status(ctl_all, FO)[0], qei_status(ctl_all, FS)[0]),
        ("EVALUABLE", "EVALUABLE"))
    chk("CONTROL throat_verdict: an applicable ABSOLUTE QEI -> SATISFIED",
        throat_verdict(ctl_all, True)[0], "SATISFIED")
    chk("FS on HPS (computed): REFUSED", qei_status(HYPOTHESES, FS)[0], "REFUSED")
    chk("  so the DOCKET 62 instrument does not stand for HPS's field",
        DOCKET62_INSTRUMENT_STANDS, False)
    # CORRECTED (DOCKET 67 follow-up, M ruled): these pinned FO "OPEN, 3
    # inputs missing", FFKP "OPEN, blocked as FO is", DSNEC "REFUSED" on flat
    # alone and the throat verdict with FO, FFKP applicable.
    chk("FO Thm 4.2 on HPS (computed): REFUSED on its Hadamard clause alone",
        (qei_status(HYPOTHESES, FO)[0], refused_on(HYPOTHESES, FO)),
        ("REFUSED", ["hadamard"]))
    chk("FFKP Thm IV.1 on HPS (computed): REFUSED on its Hadamard clause alone",
        (qei_status(HYPOTHESES, FFKP)[0], refused_on(HYPOTHESES, FFKP)),
        ("REFUSED", ["hadamard"]))
    chk("  and FFKP's unmet rows are FO's (blocked the same way)",
        [r[1] for r in rows if r[0] == FFKP and not r[4].startswith("MET")],
        [r[1] for r in rows if r[0] == FO and not r[4].startswith("MET")])
    chk("CONDITIONAL (HPS's state taken Hadamard): FO, FFKP OPEN on 2 inputs each",
        [(CONDITIONAL_IF_HADAMARD[i][0], len(CONDITIONAL_IF_HADAMARD[i][1]))
         for i in (FO, FFKP)], [("OPEN", 2), ("OPEN", 2)])
    chk("  and that conditional is the table's (recomputed here)",
        [qei_status(hypothesis_table(hadamard=True), i) for i in (FO, FFKP)],
        [CONDITIONAL_IF_HADAMARD[FO], CONDITIONAL_IF_HADAMARD[FFKP]])
    chk("CONTROL the Hadamard tag decides: drop it from FFKP's form set -> OPEN",
        _swapped(FORM_TAGS, FFKP, FORM_TAGS[FFKP] - {"hadamard"},
                 lambda: qei_status(HYPOTHESES, FFKP)[0]), "OPEN")
    chk("DSNEC on HPS (computed): REFUSED on flat, Hadamard, null plane, (79)",
        (qei_status(HYPOTHESES, DSN)[0], refused_on(HYPOTHESES, DSN)),
        ("REFUSED", ["flat", "hadamard", "nullplane", "phimax"]))
    chk("throat verdict (computed): NOT A TEST; no QEI applicable",
        throat_verdict(HYPOTHESES, RHO_THROAT_AT_PLOTTED > 0), ("NOT A TEST", []))
    chk("  conditional on Hadamard: NOT A TEST; applicable = FO, FFKP",
        throat_verdict(hypothesis_table(hadamard=True), True), ("NOT A TEST", [FO, FFKP]))
    chk("off-throat evaluation (computed): REFUSED; control -> EVALUABLE",
        (off_throat_status(HPS_PRINTS_CLOSED_FORM_SOLUTION,
                           TAYLOR_RADIUS_OF_CONVERGENCE_PROVED),
         off_throat_status(False, True)), ("REFUSED", "EVALUABLE"))

    print("\n2. HPS's EQUATIONS, TESTED (C3)")
    lhs, sols, Kr0, ortho2, R_thph = einstein_and_anomaly(sp)
    chk("printed G^t_t, G^l_l, G^th_th == G of metric (2)", lhs, (0, 0, 0))
    S0 = hps_system(sp, printed=True)
    bad = dimension_defects(sp, printed=True)
    chk("dimension: exactly one printed term is not length^-4", len(bad), 1)
    fl, rl = S0['f'].diff(S0['l']), S0['r'].diff(S0['l'])
    chk("  and it is the ll-log term -4 f'^2 r'^2/(f^2 r)",
        (bad[0][0], sp.simplify(bad[0][1] + 4*fl**2*rl**2/(S0['f']**2*S0['r']))),
        ("ll-log", 0))
    chk("repaired text: no dimension defect", len(dimension_defects(sp, printed=False)), 0)
    tot_p, _Bc_p, _tr_p = conservation(sp, printed=True)
    chk("CONTROL FIRES: text as extracted is NOT conserved", tot_p != 0, True)
    R0, hits = repair_scan(sp)
    print("      residual with tt coefficient as printed: %s" % R0)
    chk("repair scan: exactly one single-coefficient repair", len(hits), 1)
    S = hps_system(sp)
    f, l = S['f'], S['l']
    if hits:
        c_pr = sp.simplify(hits[0][1]/(f.diff(l)**2*f.diff(l, 2)/f**3))
        chk("  it is tt-log f'^2 f''/f^3: printed 16, repaired 116",
            (hits[0][0], c_pr, sp.simplify(c_pr*(1 + hits[0][2]))), ("tt-log", 16, 116))
    else:
        chk("  it is tt-log f'^2 f''/f^3: printed 16, repaired 116", None, ("tt-log", 16, 116))
    tot, Bc, tr = conservation(sp, printed=False)
    chk("repaired: full tensor conserved", tot, 0)
    chk("repaired: log bracket conserved on its own", Bc, 0)
    chk("repaired: log bracket traceless", tr, 0)
    chk("non-log trace = 16(Riem^2 - Ric^2 + c BoxR): c solved, unique",
        [s[sp.Symbol('c')] for s in sols[1]], [1])
    chk("  the opposite sign admits no c", sols[-1], [])

    print("\n3. THE THROAT (THEOREM, sympy)")
    T = throat(sp)
    L = T['L']
    L0 = sp.Rational(*HPS_PLOTTED_LNF0)
    chk("ll eq at l = 0 gives r_0^2 = -16 K^2 L",
        [sp.simplify(x**2 + 16*S['K2']*L) for x in T['r0_ll']], [0])
    s1, _s2 = throatmass.hps_quartic(sp)
    chk("  equals throatmass.hps_quartic at L = -2/3 (other route)",
        sp.simplify(T['r0'].subs(L, L0) - s1[0]), 0)
    chk("r_0^2 = 1/(540 pi) at L = -2/3", sp.simplify(T['r0'].subs(L, L0)**2),
        1/(540*sp.pi))
    chk("  == the stdlib pi r_0^2 behind CURVATURE_RADIUS_LP",
        sp.simplify(sp.pi*T['r0'].subs(L, L0)**2
                    - sp.Rational(R0_SQUARED_TIMES_PI_AT_PLOTTED.numerator,
                                  R0_SQUARED_TIMES_PI_AT_PLOTTED.denominator)), 0)
    chk("f''''(0)/f(0) = 259200 pi^2 (-L-1)/(L(3L+4))",
        sp.simplify(T['A4'] - 259200*sp.pi**2*(-L - 1)/(L*(3*L + 4))), 0)
    chk("r''''(0)/r(0) = 129600 pi^2 (2-L^2)/(L^2(3L+4))",
        sp.simplify(T['B4'] - 129600*sp.pi**2*(2 - L**2)/(L**2*(3*L + 4))), 0)
    chk("  at L = -2/3: 226800 pi^2", sp.simplify(T['B4'].subs(L, L0)), 226800*sp.pi**2)
    chk("rho(throat) = -45/L", sp.simplify(T['rho'] + 45/L), 0)
    chk("  coefficient == stdlib RHO_THROAT_COEFF", sp.simplify(-T['rho']*L),
        sp.Integer(RHO_THROAT_COEFF))
    chk("  = 135/2 at L = -2/3 == stdlib RHO_THROAT_AT_PLOTTED",
        sp.simplify(T['rho'].subs(L, L0)),
        sp.Rational(RHO_THROAT_AT_PLOTTED.numerator, RHO_THROAT_AT_PLOTTED.denominator))
    chk("p_l from the ll RIGHT side = -rho (radial NEC saturated)",
        sp.simplify(T['p_l_rhs'] + T['rho']), 0)
    chk("p_t(throat) = 0", T['p_t'], 0)
    chk("8 pi (rho + p_l) = -(r''''/r) l^2 + O(l^4)",
        sp.simplify(T['nec2'] + T['B4']), 0)
    chk("  rho + p_l = -28350 pi l^2 at L = -2/3",
        sp.simplify(T['nec2'].subs(L, L0)/(8*sp.pi)), -28350*sp.pi)
    z = throat_signs_z3()
    chk("z3: r''''/r <= 0 somewhere on [-1,0)", z['r4<=0'], 'unsat')
    chk("z3: f''''/f < 0 somewhere on [-1,0)", z['f4<0'], 'unsat')
    chk("z3: rho <= 0 somewhere on [-1,0)", z['rho<=0'], 'unsat')
    chk("z3 CONTROL: f4/f < 0 on (-4/3, -1) is found", z['control f4'], 'sat')
    chk("z3 CONTROL: r4/r < 0 on (-1.41, -1.34) is found", z['control r4'], 'sat')

    print("\n3b. THE CURVATURE RADIUS, DEFINED (ruling B3)")
    rr = S['r']
    QQ = sp.Symbol('q', positive=True)       # a positive radius, for the root
    chk("orthonormal Riemann at the throat: only (th ph th ph) and permutations",
        sorted(ortho2), [(2, 3, 2, 3), (2, 3, 3, 2), (3, 2, 2, 3), (3, 2, 3, 2)])
    chk("  each squared component = 1/r^4", [sp.simplify(v*rr**4) for v in ortho2.values()],
        [1, 1, 1, 1])
    chk("  signed R_(theta phi theta phi) = 1/r^2, so r_c := |R|^(-1/2) = r_0",
        sp.simplify(R_thph*rr**2), 1)
    chk("Kretschmann at throat data = 4/r^4 (= 4 x the squared component)",
        sp.simplify(Kr0*rr**4), 4)
    chk("  Kretschmann^(-1/4) = r_0/sqrt 2, exactly",
        sp.simplify((4/QQ**4)**sp.Rational(-1, 4) - QQ/sp.sqrt(2)), 0)
    r0v = T['r0'].subs(L, L0)
    near("r_c at the throat, l_P: sympy vs stdlib CURVATURE_RADIUS_LP",
         mp.mpf(CURVATURE_RADIUS_LP), mp.mpf(sp.N(r0v, 30)), 1e-14)
    near("Kretschmann radius: sympy vs stdlib KRETSCHMANN_RADIUS_LP",
         mp.mpf(KRETSCHMANN_RADIUS_LP), mp.mpf(sp.N(r0v/sp.sqrt(2), 30)), 1e-14)
    near("  r_c printed in section 1", mp.mpf(CURVATURE_RADIUS_LP_PRINTED),
         mp.mpf(sp.N(r0v, 30)), 5e-6)
    near("  Kretschmann radius printed in section 1", mp.mpf(KRETSCHMANN_RADIUS_LP_PRINTED),
         mp.mpf(sp.N(r0v/sp.sqrt(2), 30)), 5e-6)
    chk("both definitions sub-Planckian (the DSNEC refusal holds under either)",
        bool(sp.N(r0v) < 1 and sp.N(r0v/sp.sqrt(2)) < 1), True)

    print("\n4. C4 -- THE SAME MACHINERY RETURNS NEGATIVE OFF THE THROAT")
    eta = sp.Symbol('eta', positive=True)
    lam = sp.Symbol('lam', positive=True)
    rho_l = T['rho'] + T['rho2']*lam**2
    nec_l = T['nec2']/(8*sp.pi)*lam**2
    boosted = (rho_l + sp.sinh(eta)**2*nec_l).subs(L, L0)
    chk("rho + p_l < 0 at l = 1e-3 (leading order)",
        bool(nec_l.subs({L: L0, lam: sp.Rational(1, 1000)}) < 0), True)
    chk("boosted radial observer at l = 1e-3, eta = 10: negative",
        bool(boosted.subs({lam: sp.Rational(1, 1000), eta: 10}) < 0), True)
    chk("at the throat every radial observer sees rho: ch^2 rho + sh^2 p_l = rho",
        sp.simplify(sp.cosh(eta)**2*T['rho'] + sp.sinh(eta)**2*T['p_l_rhs'] - T['rho']), 0)

    print("\n5. C1 -- THE FLAT LIMIT")
    xi, c53, c55, pref = fo_flat_coefficient(sp)
    chk("FO (53) integrated == FO (55) coefficient", sp.simplify(c53 - c55), 0)
    chk("  c(xi) = 1/4 - xi/3", sp.simplify(c53 - (sp.Rational(1, 4) - xi/3)), 0)
    chk("prefactor S_2/(2 pi)^4 = 1/(4 pi^3)", sp.simplify(pref - 1/(4*sp.pi**3)), 0)
    chk("xi = 0: (1/(4pi^3))(1/4) = 1/(16 pi^3), FS (88)",
        sp.simplify(pref*c53.subs(xi, 0) - 1/(16*sp.pi**3)), 0)
    chk("xi = 1/6: state-independent part is 7/9 of the minimal one",
        sp.simplify(c53.subs(xi, sp.Rational(1, 6))/c53.subs(xi, 0)), sp.Rational(7, 9))
    mp.mp.dps = 40
    mu1 = mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, 4.73)
    near("mu_1 (mpmath findroot) == achievable.FEWSTER_MU1", mu1,
         mp.mpf(achievable.FEWSTER_MU1), 1e-14)
    q = clamped_beam_ratio(sp, mp, mu1)
    near("clamped-beam INT g''^2/INT g^2, by quadrature, == mu_1^4", q, mu1**4, 1e-25)
    near("so (1/16pi^2) INT g''^2/||g||^2 == achievable.FEWSTER_C (tau = 1)",
         q/(16*mp.pi**2), mp.mpf(achievable.FEWSTER_C), 1e-14)
    g, _gp, gpp = bump(sp, mp, mp.mpf(1)/2)
    mp.mp.dps = 25
    qb = mp.quad(lambda t: gpp(t)**2, [-0.5, 0, 0.5]) / mp.quad(lambda t: g(t)**2, [-0.5, 0, 0.5])
    chk("variational arm: the C-inf bump's ratio EXCEEDS mu_1^4 (tau = 1)",
        bool(qb > mu1**4), True)

    print("\n6. C2 -- A STATE KNOWN TO VIOLATE")
    st = fo_state_sympy(sp)
    chk("FO one-particle state: norm 1 (their normalisation)", st['norm'], 1)
    chk("  energy 2 kappa/3 (their (26))", sp.simplify(st['energy'] - 2*st['kap']/3), 0)
    chk("  energy density RE-DERIVED from (24)-(25) == their (28)",
        sp.simplify(st['rho'] - st['fo28']), 0)
    chk("  at t = 0: -xi (2 kappa)^4/(3 pi^2) (their (29))",
        sp.simplify(st['rho'].subs(st['t'], 0) + st['xi']*(2*st['kap'])**4/(3*sp.pi**2)), 0)
    L1, Bmin, QA, slope, jstar = violation_control(sp, mp, tau=mp.mpf(1)/10)
    print("      tau = 0.1/kappa: INT g^2 rho_1 = %s, B_min = %s, j* = %s"
          % (mp.nstr(L1, 10), mp.nstr(Bmin, 10), jstar))
    chk("xi = 1/6, one particle: smeared energy density NEGATIVE", bool(L1 < 0), True)
    chk("j* particles VIOLATE the minimal state-independent bound",
        bool(jstar is not None and jstar * L1 < -Bmin and (jstar - 1) * L1 >= -Bmin), True)
    chk("FO's state-dependent bound HOLDS at every j (slope >= 0)", bool(slope >= 0), True)
    chk("  and at j*: j L1 >= -Qt_A - j xi <:Phi^2:>(Q_B)",
        bool(jstar is not None and jstar*L1 >= -QA - jstar*(slope - L1)), True)
    L1w, Bw, _QAw, _sw, _jw = violation_control(sp, mp, tau=mp.mpf(1))
    chk("wide sampler (tau = 1/kappa): one-particle average turns POSITIVE",
        bool(L1w > 0), True)

    print("\n7. WHAT THIS FILE REFUSES, AND WHAT IT WITHDREW (computed words)")
    chk("Fewster-Smith status word, from the table", FEWSTER_SMITH_ON_HPS.split(" --")[0],
        "REFUSED")
    chk("DSNEC status word, from the table", DSNEC_ON_HPS.split(" --")[0], "REFUSED")
    # CORRECTED (DOCKET 67 follow-up): pinned ("OPEN", "OPEN") before.
    chk("FO and FFKP status words, from the table: REFUSED (Hadamard clause)",
        (FO_ON_HPS.split(" --")[0], FFKP_IV1_ON_HPS.split(" --")[0]),
        ("REFUSED", "REFUSED"))
    chk("  and each names the conditional OPEN, not a violation",
        all("if HPS's state were Hadamard, OPEN" in w and "Not a finding of "
            "violation" in w for w in (FO_ON_HPS, FFKP_IV1_ON_HPS)), True)
    chk("Kontou's requested test and the applicable-QEI verdict carry the words",
        (KONTOU_REQUESTED_TEST_ON_HPS.split(" and FFKP")[0],
         VERDICT_APPLICABLE_QEI.split(" --")[0]),
        ("FO Thm 4.2 REFUSED", "REFUSED"))
    chk("the throat verdict carries the computed word, not 'SATISFIED'",
        VERDICT_THROAT_GEODESIC.split(" --")[0], "NOT A TEST")
    pin("the withdrawn verdict is kept and marked WITHDRAWN",
        VERDICT_THROAT_GEODESIC_WITHDRAWN.startswith("WITHDRAWN"), True)

    print("\n  %d computed checks + %d record pins" % tuple(n_chk))
    print("  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(report())
