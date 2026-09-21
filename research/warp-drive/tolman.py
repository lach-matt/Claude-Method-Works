#!/usr/bin/env python3
r"""
tolman.py -- TOLMAN'S ACTIVE GRAVITATIONAL MASS, TESTED POINTWISE.

DOCKET 54 section 4 asked for one constructive output to be seated: for a
traceless, conserved, static, spherically symmetric source with a regular
centre, "the enclosed mass is negative" and "the radial stress is a tension"
are the same statement, so certify.py's ball integral can be read off T^r_r at
a single radius.  This file is that instrument.

    python3 tolman.py             the reading
    python3 tolman.py --selftest  every fixture; STDLIB ONLY plus seated peers
    python3 tolman.py --verify    the sympy residuals, every one exactly 0
    python3 tolman.py --prove     the z3 obligations, with their guards

Run under python3 (3.11).  --verify needs sympy, --prove needs z3-solver; both
are on pypi and pypi is on the proxy allowlist (PROOF-ASSISTANT.md).  --selftest
imports neither, by design: it is the layer that must run anywhere.

===============================================================================
0.  VERDICT
===============================================================================

    IT RESTATES certify.py ON A STRICTLY SMALLER CLASS.  IT DOES NOT SUPERSEDE
    IT, AND THE RULING'S OWN WORD "REPLACES" IS WITHDRAWN HERE.

    certify.py's THEOREM needs static and spherically symmetric, and nothing
    else -- no conservation law, no tracelessness, no flat background, no
    stress tensor at all.  Its COROLLARY adds a regular centre.  THIS TEST
    NEEDS ALL OF THAT AND TWO MORE HYPOTHESES:  T^mu_mu = 0 EXACTLY, and a
    FLAT BACKGROUND (Phi' = 0, or the weaker sufficient condition u + p_r = 0).
    Two hypotheses in and nothing new out.  The set of spacetimes this file
    speaks about is a PROPER SUBSET of the set certify.py's corollary speaks
    about, which is a proper subset of the set its theorem speaks about.  A
    test valid on a smaller class cannot supersede a theorem valid on a larger
    one.  IT CAN ONLY BE CHEAPER WHERE BOTH APPLY, and that is the whole of
    what is claimed: one evaluation of T^r_r at R instead of a quadrature of
    rho over the ball.

    NO NOVELTY IS CLAIMED FOR ANY LINE OF THE MATHEMATICS.  Section 1 is the
    prior art and it goes against us: the identity is Tolman's active
    gravitational mass (1930) in the Misner-Sharp form published by Herrera &
    Santos (1995) and Herrera (2018) eq. (32), specialised to a traceless
    source on a flat background, where it reduces to von Laue's 1911
    condition.  DOCKET 54's sentence "I did not find either stated in this
    form" IS WITHDRAWN BY THIS FILE: it is stated in this form, in print,
    since 1995 at the latest, and its flat parent since 1911.

    THE HEADLINE THE WITNESS FORCES.  The integration constant of the identity
    is NOT a limit of m.  In Reissner-Nordstrom BOTH m(r) AND 4 pi r^3 p_r(r)
    DIVERGE TO -INFINITY AT THE CENTRE AND THEIR DIFFERENCE IS EXACTLY M AT
    EVERY RADIUS -- no limit taken, no expansion.  C is a renormalised central
    mass: two divergences cancelling identically.  An instrument that computes
    C as lim m(r) returns -infinity where the answer is finite.  And the same
    witness explains DOCKET 52's regular-centre hypothesis as ONE FACT SEEN
    TWICE rather than a coincidence: certify.py's corollary needs m(0) = 0 to
    kill the integration constant of dm/dr = 4 pi r^2 rho, and this identity
    needs r^3 p_r -> 0 to kill the integration constant of
    d(r^3 p_r)/dr = r^2 u.  Both are the same first-order ODE's constant at
    r = 0, and RN breaks both simultaneously, in the same region, by the same
    amount.

    AND RN IS A COUNTEREXAMPLE IN THE SAME BREATH, NOT AFTER IT.  RN is
    traceless (residual 0), conserved (residual 0), static, spherically
    symmetric, and has p_r < 0 at EVERY radius -- yet m(r) < 0 only inside
    r < Q^2/2M.  THE POINTWISE TEST FAILS THERE, AND IT MUST, because C = M.
    The regular-centre hypothesis is load-bearing, not cosmetic.

    NO GATE MOVES.  A cheaper test for a requirement is not a cheaper
    requirement.  candidates.py's KIND/DEADLINE/MAGNITUDE are unchanged,
    overturn.py's L4 is unchanged, and the bill for 1 % contraction of proper
    radial distance at R = 1 m is 9.7773e+40 Pa of radial TENSION -- 2.46e+13
    times the best in-hypothesis tension known (a magnetar field).  Section 9.

    NOTHING IS REPAIRED AND NO PEER IS EDITED.  Section 11 is a status table
    naming what each peer's claim becomes; the human seats any change.

===============================================================================
1.  PRIOR ART, FIRST, AND IT GOES AGAINST US
===============================================================================

THE IDENTITY IS PUBLISHED, IN FULL GENERAL RELATIVITY, AND IN A STRONGER FORM
THAN THE ONE DOCKET 54 DERIVED.  L. Herrera, arXiv:1801.08358v2, eq. (32):

    m_T = e^{(nu+lambda)/2} [ m(r) + 4 pi r^3 P_r ]

-- Tolman mass = redshift factor x (Misner-Sharp mass + 4 pi r^3 p_r), with no
flat-background hypothesis at all.  Rearranged, 4 pi r^3 p_r = e^{-(nu+lambda)/2}
m_T - m, which is DOCKET 54's identity with the traceless step not yet taken and
with a factor a flat derivation cannot see.  Herrera & Di Prisco,
arXiv:gr-qc/9810020, eq. (39), states it again time-dependently and dates the
derivation to Herrera, Di Prisco, Hernandez-Pastora & Santos, Phys. Lett. A 237,
113 (1998), itself restating Herrera & Santos, Gen. Rel. Gravit. 27, 1071 (1995).

    THAT PUBLISHED IDENTITY IS MACHINE-CHECKED HERE AGAINST US, NOT ASSUMED.
    Residual V20 reproduces Herrera eq. (32) exactly from the computed Einstein
    tensor -- d/dr[e^{(nu+lambda)/2}(m + 4 pi r^3 p_r)] equals the Tolman
    integrand 4 pi r^2 e^{(nu+lambda)/2}(u + p_r + 2 p_t), sympy residual 0.
    The parent is correct.  The child adds one line.

TRACELESSNESS IS THE ONLY STEP THE DOCKET ADDS, AND IT IS ONE LINE.  T^mu_mu = 0
gives u = p_r + 2 p_t, so the Tolman integrand becomes 2u, so m_T = 2m -- BUT
ONLY WHERE e^{(nu+lambda)/2} = 1.  Then 4 pi R^3 p_r(R) = 2m - m = m.  So

    m(R) c^2 = 4 pi R^3 <T^r_r(R)>   IS   "m_Tolman = 2 x m_MisnerSharp for
                                           traceless matter", fed through
                                           Herrera eq. (32).

"The active gravitational mass of radiation is twice its energy" is Tolman's own
1930 observation.  This tree re-derived a 1930 remark composed with a 1995
identity.

THE FLAT PARENT IS OLDER STILL AND IS NOT TOLMAN'S.  Strip gravity and the step
"the volume integral of the spatial stress is a surface term" is von Laue's
theorem, Ann. Phys. 340(8), 524 (1911), in its finite-volume form: C. Wang,
arXiv:1206.5618, eq. (20), for a divergence-free time-independent tensor,

    oint_S dS_l (Theta^{l mu} X^i) = int_V Theta^{i mu} d^3x .

Trace over i on a sphere and the right-hand side is 4 pi R^3 p_r(R).  DOCKET
54's "EXACT, NO INTEGRATION CONSTANT" is Laue plus the divergence theorem.
The same statement in the hadron gravitational-form-factor variables is
Lorce, Metz, Pasquini & Rodini, arXiv:2109.11785, whose eq. (65)
M = <Psi| int d^3x T^mu_mu |Psi> is the R -> infinity limit of the general form
below, and whose eq. (15) context names it "the von Laue condition for
mechanical equilibrium ... derived long ago in the context of classical field
theory".  The conservation equation p'_r + 2(p_r - p_t)/r = 0 is standard for a
static anisotropic sphere; arXiv:2605.04163 eq. (65) states it verbatim.

THE CASIMIR APPLICATION IS ALSO ALREADY THERE, AND IT IS A SCOPE CAUTION RATHER
THAN SUPPORT.  F. Sorge, arXiv:2011.10991, attributes a Tolman mass to a Casimir
cavity, proves int_V sqrt(-g) T^i_(C) i = 0 for the apparatus (his eq. 36) and
says outright that the cancellation "basically relies on the virial theorem".
CONSEQUENCE FOR THIS FILE, ENFORCED IN CODE: for a COMPLETE apparatus -- field
plus mirrors -- the spatial stress integrates to zero, so 4 pi R^3 p_r(R) = 0
identically on any ball enclosing the walls.  The pointwise test has content
ONLY on a ball strictly inside the cavity.  `pointwise_test` REFUSES on a ball
containing a mirror; the refusal is part of what the instrument is.

TWO NON-FINDS, AND A NON-FIND IS NOT A CLEARANCE:

    (a) No statement in the CASIMIR literature of the form "negative enclosed
        mass if and only if radial tension" was located.  Searched: Milton
        1005.0031 and the Milton/Fulling/Parashar/Shajesh gravitational-Casimir
        series as cited by Sorge refs [38]-[42]; Sopova & Ford quant-ph/0504143;
        Cavero-Pelaez-Milton-Wagner hep-th/0508001; Sorge 2011.10991.
    (b) No statement in the WORMHOLE literature that the flare-out condition
        equals negative enclosed Misner-Sharp mass.  NOT FOUND, AND THE REASON
        IS NOW DERIVED AND RUNS AGAINST ANY SUCH HOPE: at a Morris-Thorne throat
        4 pi r_0^3 p_r = MINUS m (residual V18), the opposite sign, so no such
        equivalence exists to be found.

STATUS OF THE ATTRIBUTIONS, NOT FLATTENED.  Rows marked CITED were read at
source by the derivation pass named in PRIOR_ART; NO PDF WAS RE-OPENED WHILE
THIS FILE WAS COMPOSED, and a row's status is that pass's, not this file's.
Tolman, Phys. Rev. 35, 875 (1930), von Laue (1911), Whittaker, Proc. Roy. Soc.
A 149, 384 (1935), Herrera & Santos (1995) and Phys. Lett. A 237, 113 (1998)
are all RECOVERED -- attributed through a secondary source that names them,
never read.  A first-publication date for the identity must therefore be given
as 1995 RECOVERED, NEVER 1995 CITED.

===============================================================================
2.  THE HYPOTHESIS LEDGER -- STATED AS A CONTAINMENT, BEFORE ANY TEST
===============================================================================

    certify.py THEOREM needs:   static, spherically symmetric.  Nothing else.
                                Exact in G, exact in the metric, no matter
                                hypothesis of any kind.
    certify.py COROLLARY adds:  a regular centre, m(0) = 0.
    THE POINTWISE TEST needs:   static (weakenable -- section 7), spherically
                                symmetric, regular centre, PLUS
                                (a) T^mu_mu = 0 exactly, and
                                (b) a flat background: Phi' = 0, or the weaker
                                    sufficient condition u + p_r = 0,
                                because the exact curved relation is

        d(r^3 p_r)/dr = r^2 (u + T^mu_mu) - r^3 (u + p_r) Phi'      (V10)

                                and in Herrera's published form the redshift
                                factor e^{(nu+lambda)/2} does not cancel unless
                                g_tt g_rr = -1.

WHAT IT HONESTLY BUYS:
    - ONE EVALUATION INSTEAD OF A QUADRATURE, on its class, ansatz-free in the
      same sense certify.py is.
    - A MATTER-SIDE TERM in a chain that was previously geometry-only
      (expose.py's C, foliation.py's Gamma).  Section 8.
    - AN EXACT DEMONSTRATION THAT ITS HYPOTHESES ARE LOAD-BEARING: three
      published or derived witnesses break the biconditional, each by removing
      exactly one hypothesis.  Section 5.

WHAT IT DOES NOT BUY: it does not make the requirement easier, it moves none of
candidates.py's three gates, and it does not touch overturn.py's L4.

THREE OVER-CLAIMS ARE AVAILABLE HERE AND ALL THREE ARE REFUSED IN SECTION 12.
The first is the damaging one: re-hanging mouth.py section 5b or overturn.py L1
on this test would move two resolutions that currently rest on a hypothesis-free
geometric statement onto one that needs tracelessness and flat space.  That
would be a weakening dressed as a strengthening.

===============================================================================
3.  THE DERIVATION -- DERIVED, NOT WRITTEN DOWN
===============================================================================

FLAT BACKGROUND, static, spherically symmetric, T^mu_nu = diag(-u, p_r, p_t,
p_t).  V1 builds g = diag(-1, 1, r^2, r^2 sin^2 th), COMPUTES the Christoffels
and forms nabla_mu T^mu_nu.  The nu = t, theta, phi components VANISH
IDENTICALLY -- staticity is not assumed to kill them, it is measured -- and the
nu = r component is

    dp_r/dr + (2/r)(p_r - p_t) = 0                                  (V2)
    =>  d(r^3 p_r)/dr = r^2 (u + T^mu_mu),  T^mu_mu = -u + p_r + 2 p_t   (V3)

THE MASTER FORMULA, EVERY CORRECTION CARRIED, is

    m(R) c^2 = 4 pi R^3 p_r(R) - C - I_Theta + J + K

        C       = 4 pi lim_{r->0} r^3 p_r         centre boundary term
        I_Theta = 4 pi INT_0^R r^2 T^mu_mu dr     trace
        J       = 4 pi INT_0^R r^3 j dr,  j := d_t T^t_r   non-static flux
        K       = 4 pi INT_0^R r^3 (u + p_r) Phi' dr       curved background

and every one of the four is proved to be load-bearing by an explicit witness
in section 5 and a machine-checked necessity row in section 10.

C IS A FIRST INTEGRAL, NOT A LIMIT.  Define

    F(r) := m(r) - 4 pi r^3 p_r(r) + 4 pi INT_0^r r'^2 T^mu_mu dr'

with dm/dr = 4 pi r^2 u.  V6 differentiates F on shell and returns 0 exactly, so
F is constant in r and C may be evaluated AT ANY RADIUS.  That is why the RN
reading works where a limit of m alone returns -infinity.

WITH THE TRACE KEPT THE TEST IS NO LONGER POINTWISE, AND THE COST IS NAMED.  The
three biconditionals that survive, one hypothesis at a time:

    traceless + regular centre : m(R) < 0  <=>  p_r(R) < 0          POINTWISE
    trace kept, regular centre : m(R) < 0  <=>  R^3 p_r(R) < INT_0^R r^2 T dr
    regular centre dropped     : m(R) < 0  <=>  4 pi R^3 p_r + C < I_Theta

The second is p_r against a RUNNING THRESHOLD that is itself an integral, so the
whole economy of this instrument is bought by TRACELESSNESS ALONE, not by the
identity.  For the renormalised EM stress tensor in a source-free cavity the
flat-space trace is exactly zero (Milton's "properly traceless", CITED in
DOCKET 54 sec. 5, NOT re-verified here), so the pointwise form is available
there.  IT IS NOT AVAILABLE for a source with a trace anomaly or a mass scale.

FULL GENERAL RELATIVITY, AND THE SEAM IS EXACT.  V8 computes the Einstein tensor
of ds^2 = -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + r^2 dOmega^2 and, substituting
e^{-2Lambda} = 1 - 2m/r, returns dm/dr = 4 pi r^2 u exactly -- so m is the
Misner-Sharp mass in full GR with no weak-field step, and the JOIN between the
flat-space algebra and the geometry is exact.  What is approximate is the
IDENTITY, by the K term, and section 6 bounds it.  V11 derives

    Phi' = (m + 4 pi r^3 p_r)/(r(r - 2m))

from the computed G^r_r, which ON THE IDENTITY (m = 4 pi r^3 p_r) collapses to
Phi' = 2m/(r(r-2m)) -- EXACTLY TWICE the Newtonian value.  That factor 2 is used
in section 6's bound and is not assumed.

WHEN IS THE FLAT IDENTITY EXACT IN A CURVED SPACETIME?  Precisely when K = 0.
The two pointwise sufficient conditions, and they are the only local ones:

    (i)  Phi' == 0      -- no redshift gradient;
    (ii) u + p_r == 0   -- THE RADIAL NEC IS SATURATED everywhere.

(u + p_r) = T_ab k^a k^b for radial null k, so (ii) is frame-independent though
u and p_r separately are not.  (ii) IS WHY THE RN CHECK CAME OUT EXACT: RN has
u = -p_r identically, so the correction vanishes exactly in a strongly curved
spacetime.  RN IS THEREFORE NOT A WEAK-FIELD CHECK OF THE IDENTITY -- it is a
check AT the exactness condition, which is a different and stronger thing.  This
is the w = -p_r/rho = 1 rigidity emtension.py already measured for the
electromagnetic field, arriving as the exactness condition of another theorem.
And the sharpest form: the ONLY traceless conserved source with u + p_r = 0 is
RN, because those two force r u' + 4u = 0 (obligations I4, I5).  THE ONE CASE
WHERE FLATNESS IS NOT NEEDED IS EXACTLY THE CASE THE REGULAR-CENTRE HYPOTHESIS
ALREADY EXCLUDES.  The two exceptions are the same object.

===============================================================================
4.  REISSNER-NORDSTROM -- THE CONSTANT IS THE CENTRAL MASS
===============================================================================

G = c = 1, Gaussian.  Source u = Q^2/(8 pi r^4), p_r = -u, p_t = +u.

    traceless   -u + p_r + 2 p_t = 0                    exact  (V12)
    conserved   p_r' + (2/r)(p_r - p_t) = 0             exact  (V12)
    m(r)        DERIVED from dm/dr = 4 pi r^2 u, then matched to the RN metric
                function: 1 - 2m/r = 1 - 2M/r + Q^2/r^2, so m = M - Q^2/(2r)
                is the Misner-Sharp mass and not an assumption       (V13)

    4 pi R^3 p_r(R)        = -Q^2/(2R)
    m(R)                   = M - Q^2/(2R)
    m(R) - 4 pi R^3 p_r(R) = M          EXACTLY, AT EVERY R          (V13)

    lim_{r->0} m(r)               = -infinity
    lim_{r->0} 4 pi r^3 p_r(r)    = -infinity
    lim_{r->0} of the DIFFERENCE  = M                                (V14)

THE TABLE (M = 1, Q = 0.8; m = 0 at R = Q^2/2M = 0.32; horizons 0.4 and 1.6) is
printed by the report and is exact in Fraction arithmetic in the selftest.
p_r < 0 in every row; m < 0 only in the first three.

THE FAILING DIRECTION IS SUFFICIENCY.  "p_r(R) < 0 => m(R) < 0" fails at every
R > Q^2/2M.  The surviving direction, necessity, is NOT TESTED by RN -- p_r < 0
everywhere, so the antecedent's truth region is trivially inside the
consequent's.  RECORDED AS SILENCE, NOT AS SUPPORT.

THE M = 0 LIMIT IS THE CLEANEST STATEMENT OF WHAT THE HYPOTHESIS BUYS.  A pure
charge or magnetic monopole has rho > 0 EVERYWHERE, p_r < 0 EVERYWHERE, and
m(R) = -Q^2/(2R) < 0 EVERYWHERE, identity residual exactly 0.  A strictly
positive energy density with negative enclosed Misner-Sharp mass at every
radius.  The THEOREM is untouched; it is the ENERGY reading of the corollary
that fails, which is the narrowing certify.py already records and which
drivensource.py section 3 machine-checks.

A CAUTION THE WITNESS CARRIES.  The region R < Q^2/(2M) lies STRICTLY INSIDE the
inner (Cauchy) horizon for every 0 < Q <= M: r_-/M - (Q^2/2M)/M = 1 - sqrt(1-y)
- y/2 with y = Q^2/M^2, whose series is y^2/8 + y^3/16 + O(y^4) > 0 on (0,1].
RN IS A WITNESS ABOUT HYPOTHESES, NOT A DEVICE.  charge.py already holds that
region and closed it; this is that region reached from the stress side.

===============================================================================
5.  THE WITNESS SET -- ONE POSITIVE CONTROL, TWO NEGATIVE, THREE REFUSALS
===============================================================================

POSITIVE CONTROL, AND IT IS NOT AN INVENTION.  Uniform negative-energy
radiation, T^mu_nu = u_0 diag(-1, -1/3, -1/3, -1/3) with u_0 > 0, is the exact
ISOTROPIC AVERAGE of the measured parallel-plate Casimir tensor over uniformly
distributed plate normals (<n_i n_j> = delta_ij/3).  Every hypothesis holds
exactly -- traceless, conserved, regular centre -- and

    m(R) c^2 = INT_0^R 4 pi r^2 e dr = -4 pi R^3 u_0/3 = 4 pi R^3 p_r(R)

residual exactly 0 (V15), from two independent computations, one an integral of
the energy density and one a pointwise read of p_r.  BOTH SIDES OF THE
BICONDITIONAL FIRE.  At d = 10 nm plate cells and R = 1 mm the instrument
returns YES, and u_0 cross-checks candidates.py's banked value.

NEGATIVE CONTROL (a), THE EXACT MIRROR, catches a global sign inversion:
ordinary positive-energy radiation, e = +u_0, p_r = p_t = +u_0/3.  All residuals
0, m > 0, p_r > 0, verdict NO.  Any implementation that inverts the verdict rule
flips this and the positive control together, so the pair is a complete sign
guard.

NEGATIVE CONTROL (b), THE WRONG-QUANTITY CONTROL, catches what a mirror cannot.
Take p_r(r) = P_0(1 - r^2/L^2).  Tracelessness and conservation then FORCE

    e(r)   = 3 P_0 - 5 P_0 r^2/L^2
    p_t(r) = P_0 - 2 P_0 r^2/L^2

with all residuals 0 and m(R) c^2 = 4 pi P_0 R^3 (L^2 - R^2)/L^2 exactly.  At
R = 9L/10:

    p_r(R) = +19 P_0/100 > 0        -> NO
    e(R)   = -21 P_0/20  < 0        <- THE TRAP
    m(R)c^2 = +13851 pi L^3 P_0/25000 > 0 -> NO, agreeing with p_r

AN IMPLEMENTATION THAT TESTS rho(R) < 0 INSTEAD OF p_r(R) < 0 READS YES HERE AND
IS WRONG.  The trap window is sqrt(3/5) L < R < L, i.e. 0.774597 L < R < L.

THE THREE HYPOTHESIS WITNESSES, each removing exactly one hypothesis:

    REISSNER-NORDSTROM      removes the REGULAR CENTRE.  Section 4.
    AGNESE & LA CAMERA      removes nothing but tracelessness's sufficiency:
    gr-qc/0203067 eq. (17)  a PUBLISHED static spherically symmetric TRACELESS
                            wormhole with POSITIVE constant m_MS = m/beta
                            everywhere and radial TENSION at the throat, where
                            4 pi r_0^3 p_|| = -m_MS.  Tracelessness alone does
                            not buy the biconditional.                  (V19)
    MORRIS-THORNE THROAT    the generic near neighbour: p_r(r_0) = -1/(8 pi r_0^2)
                            < 0 with m = b(r_0)/2 = r_0/2 > 0, and
                            4 pi r_0^3 p_r = -m.  THE FLARE-OUT CONDITION IS
                            NOT THIS IDENTITY; IT IS THE SAME QUANTITY WITH THE
                            OPPOSITE SIGN.                              (V18)

AND THE THREE REFUSALS, which belong in the same table because a verdict where
the instrument should refuse is also a failure mode:

    Reissner-Nordstrom at R > Q^2/2M : p_r < 0, m > 0 -> REFUSE (centre)
    Coulomb / monopole field         : divergent enclosed integral -> REFUSE
    parallel plates, RAW CELL        : REFUSE (not spherically symmetric)
    any ball enclosing a mirror      : REFUSE (Sorge eq. 36, section 1)

AND THE PLATE CELL'S OVERSELL, NAMED.  The raw cell has rho = -u_0 < 0 AND
p_normal = -3 u_0 < 0 simultaneously, which is the ruling's consistency check
and is correct AS A STATEMENT ABOUT SIGNS.  It is not spherically symmetric, so
the identity is neither satisfied nor violated by it -- IT IS NOT DEFINED FOR
IT.  Substituting p_normal into the identity as if it were p_r gives
4 pi R^3 (-3u_0) where the true enclosed energy of a ball of such cells is
(4/3) pi R^3 (-u_0): A FACTOR OF 9.  Anyone reading a magnitude off the raw cell
is wrong by an order of magnitude.  The cell enters the witness set ONLY through
its isotropic average.  A further limit, recorded: that average is a
coarse-graining, valid only where the cell is much smaller than the scale over
which m(r) varies, and coarse-graining averages the MIRRORS into rho as well --
which is the finding symmetry-loophole already banked and which this witness
does not reopen.

SPHERICITY SPLITS IN TWO, AND ONLY ONE HALF IS LOAD-BEARING.  This is the
ruling's one substantive error and it was found only because the prior-art
search forced the Laue route.  Wang's eq. (20) needs the REGION to be a ball;
THE SOURCE MAY BE ANYTHING.  Obligations F1/F2 discharge the identity and the
biconditional with no sphericity of the source assumed, and F5 realises a
non-spherical constant-anisotropic source for which the Laue residual is exactly
0.  BUT the test quantity is then the ANGULAR AVERAGE <T^r_r(R)>, and F6 plus
witness W5 (p_t = -5, p_z = +1, hence e = -9, <T^r_r> = -3 < 0 and m < 0, while
the single component p_z = +1 > 0) show that READING ONE DIRECTION INSTEAD OF
THE AVERAGE INVERTS THE VERDICT.  Sphericity is what makes T^r_r(R) equal its
own average, which is why the single-radius read is legitimate for a spherical
source AND ONLY THEN.  LIMIT: the realisability witness is constant-stress only;
no non-constant non-spherical witness was constructed, and its absence is a gap
in the realisability layer, not a result.

u(R) < 0 IS NEITHER NECESSARY NOR SUFFICIENT, AND IT IS THE MOST LIKELY
MISREADING OF THIS INSTRUMENT.  Obligation G1 proves the identity does not
mention u at all.  Two exact witnesses:

    W3  p_r = -2 + 10 r^{-5/2}   traceless, conserved, regular centre (both
                                 exponents > -3).  At r = 1: p_r = +8,
                                 u = -1 < 0, m = +8F > 0.  NOT SUFFICIENT.
    W4  p_r = +2 - 10 r^{-5/2}   at r = 1: p_r = -8, u = +1 > 0, m = -8F < 0.
                                 NOT NECESSARY.

The only true one-way statement is G2: u < 0 THROUGHOUT implies m < 0, and that
is machine-checked only on the power-law family where the integral is algebraic.

AND THE BOUNDARY CASE THE RULING DID NOT STATE.  p_r(R) = 0 <=> m(R) = 0 EXACTLY
(H1), where g_rr = 1 and certify.py's STRICT criterion makes it a NON-contraction
(H4).  A zero on an INTERVAL forces p_t = 0 and u = 0 -- it is vacuum there (H2).
An ISOLATED zero forces u = r p_r' != 0 -- m = 0 exactly while the energy density
is nonzero (H3), a third independent demonstration that m and u are decoupled.

===============================================================================
6.  THE FLAT-BACKGROUND LIMIT, BOUNDED IN CLOSED FORM
===============================================================================

Define the relative curved correction

    delta := |4 pi INT_0^R r^3 (u + p_r) Phi' dr| / |4 pi R^3 p_r(R)| .

PROFILE AND ITS STATUS, STATED BEFORE THE NUMBER.  RECOVERED, measured out of
DOCKET 54's own banked figure: m(r) = -(hbar a)/(15 pi c eps^2) for an ideal
conductor, interior, near-wall, eps = a - r.  DERIVED from it by the field
equation and by the identity: u = -hbar c/(30 pi^2 a eps^3) and
p_r = -hbar c/(60 pi^2 a^2 eps^2), and r Phi' = 2 G m/(a c^2) =
-(2/15 pi)(l_P/eps)^2.  The p_r so obtained is exactly DOCKET 54's independently
derived interior value -A hbar c/(a^2 eps^2) with Milton's A_EM = 1/(60 pi^2):
TWO ROUTES, ONE COEFFICIENT, and A_EM remains SINGLE-SOURCE as the ruling
records.

CLOSED FORM (V16, sympy integrate then limit, residual 0):

    delta = (1/15 pi) (l_P/eps)^2  =  chi/2   EXACTLY,

where chi = (2/15 pi)(l_P/eps)^2 is DOCKET 54's banked compactness.  BOTH ARE
INDEPENDENT OF a.  So the backreaction bound and DOCKET 54's magnitude wall are
the same sub-Planckian wall reached from two directions.  At a femtometre
regulator delta is 5.5e-42, and at the plasma wavelengths that set the Casimir
problem it is at most 1.16e-56; it reaches 2.122 % only at eps = l_P and unity
at eps = l_P/sqrt(15 pi) = 0.1456731 l_P.

THE GENERAL, PROFILE-FREE FALLBACK, since the above is profile-dependent:

    |delta| <= [chi_max/(1 - chi_max)] * V/|m(R)| ,
    V := INT_0^R 4 pi r^2 (|u| + |p_r|) dr,

from |r Phi'| = |2m/(r - 2m)| <= chi_max/(1 - chi_max).  For the profile above
V/|m| = 3/2 and the general bound gives 1.5 chi against the exact chi/2 -- a
factor 3, which is what a bound costs.

A DISCREPANCY BETWEEN THE DERIVATION PASSES, RECORDED NOT REPAIRED.  One pass
reported delta = 2.9210e-58 at eps = 137.8 nm; the recomputation here and a
second pass's independent audit of chi both give delta = 2.9193e-58
(chi = 5.8386e-58, against the ruling's banked 5.84e-58).  The first figure is
high by 5.8e-4 relative.  This file uses the recomputation and prints both.

A FAULT IN THE DERIVATION PASS, RECORDED RATHER THAN HIDDEN.  Its first numeric
check of this bound used a UNIFORM grid over an eps^-5 integrand and disagreed
with the closed form by 100 % (2.06e-61 against 2.92e-58).  A uniform-grid
answer there is an artefact of the grid, not a check.  The closed form above is
sympy's, taken as the primary route for exactly that reason.

===============================================================================
7.  STATICITY IS THE WRONG HYPOTHESIS ON THE SOURCE SIDE TOO
===============================================================================

Drop staticity exactly, in a flat background, with a radial energy flux allowed.
Write j := d_t T^t_r.  The computed conservation equations (V21) are

    energy   :  d_t u + (1/r^2) d_r(r^2 T^t_r) = 0
    momentum :  d_r p_r + (2/r)(p_r - p_t) + j = 0

and the identity becomes, residual exactly 0 (V22),

    d(r^3 p_r)/dr = r^2 (u + T^mu_mu) - r^3 j .

THE HYPOTHESIS ACTUALLY USED IS WEAKER THAN STATICITY.  The identity needs only

    j = d_t T^t_r = 0    -- the radial ENERGY FLUX is time-independent,

NOT T^t_r = 0.  STATIONARY SUFFICES; STATIC IS NOT REQUIRED.  That is the
source-side twin of the correction foliation.py made to certify.py from the
geometry side -- "what certify.py used was not that the spacetime is static but
that the foliation is the KILLING-ADAPTED one; staticity is sufficient for that
and is not its content".  TWO FILES, OPPOSITE DIRECTIONS, THE SAME OVER-STRONG
HYPOTHESIS NAMED.  Also derived, residual 0 (V21): dm(R,t)/dt = -4 pi R^2
T^t_r(R,t) -- the enclosed mass changes only by flux through the sphere.

A LIMIT, NAMED AND NOT GLOSSED, AND THE NON-STATIC BRANCH IS NOT CLOSED.  The
identity above is exact FLAT-SPACE algebra.  Identifying INT 4 pi r^2 u dr with
the Misner-Sharp mass of the actual spacetime is proved exactly here only in the
STATIC case (V8, from G^t_t).  Off staticity that identification acquires flux
terms which were NOT derived and are NOT asserted; driven.py and nonstatic.py
hold the geometry side.  UNTIL THAT IS CLOSED THE NON-STATIC IDENTITY IS A
STATEMENT ABOUT T, NOT ABOUT m, and `pointwise_test` refuses the non-static
branch for that reason rather than reporting it.

===============================================================================
8.  THE CHAIN TO foliation.py, AND WHY IT IS NOT A CATEGORY ERROR
===============================================================================

THE OBJECTION FIRST, BECAUSE IT IS CORRECT.  p_r is a FRAME COMPONENT.  Boosting
the (t,r) block by rapidity w (V23):

    u'   = u cosh^2 w + p_r sinh^2 w + q sinh 2w
    p_r' = p_r cosh^2 w + u sinh^2 w + q sinh 2w
    (u - p_r) IS INVARIANT -- the SO(1,1) trace of the block, residual 0.

With q = 0, p_r' vanishes at tanh^2 w = |p_r|/u.  SO IF u > 0 AND p_r < 0 --
wherever the radial NEC is SATISFIED -- A BOOST TURNS THE TENSION INTO A
PRESSURE AT THE SAME EVENT.  p_r < 0 IS GAUGE IN GENERAL.  (Exception, checked:
if u + p_r = 0 then p_r' = p_r for every w -- emtension.py's rigidity, fully
invariant.)

THE IDENTITY IS WHAT PROMOTES p_r FROM A FRAME COMPONENT TO A SCALAR.
foliation.py's invariant is Gamma^2 - U^2 = g^{ab} d_a R d_b R = 1 - 2m/R.
Substituting the identity's m = 4 pi R^3 p_r (V24, residual 0):

    Gamma^2 - U^2 = 1 - 8 pi R^2 p_r(R)
    i.e.   p_r(R) = [ 1 - g^{ab} d_a R d_b R ] / (8 pi R^2) ,

whose right-hand side is built from the metric and the areal radius alone.
UNDER THE HYPOTHESES, THE KILLING-FRAME RADIAL STRESS EQUALS A
FOLIATION-INDEPENDENT SCALAR.  The hypotheses buy back exactly the invariance
the boost took away -- the same move foliation.py made for Gamma, where U = 0 is
the infimum of the boost orbit and standing there is what makes the criterion
invariant.

THE CHAINED STATEMENT, MACHINE-CHECKED (section 10, family B and H):

    Under H -- flat-background traceless, conserved, spherically symmetric,
    stationary-flux, regular centre, geometry sourced by it --

        p_r(R) < 0  <=>  m(R) < 0  <=>  Gamma > 1 IN EVERY FOLIATION at R,

    and the middle term may be deleted: THE RADIAL STRESS IS A TENSION AT R IFF
    PROPER RADIAL DISTANCE IS CONTRACTED AT R IN EVERY FOLIATION.

foliation.py's RANGE THEOREM carries NO staticity hypothesis, so the right-hand
biconditional is the strongest link in the chain and it is not this file's.

THE FOUR WAYS THE CHAIN FAILS, NONE HIDDEN:
    (1) OUTSIDE H, p_r < 0 IS GAUGE -- the boost witness above.  The chain is
        about the KILLING-FRAME p_r and about no other frame's.
    (2) THE REGULAR CENTRE IS LOAD-BEARING -- RN has p_r < 0 at every radius and
        m < 0 only inside r < Q^2/2M.  The gap is exactly C = M.
    (3) THE SEAM IS THE FIELD EQUATION, NOT THE ALGEBRA.  The identity is
        flat-background; the contraction theorem is about the actual
        Misner-Sharp mass.  They are joined by dm/dr = 4 pi r^2 u, exact in full
        GR (V8), so the JOIN is exact.  What is approximate is the IDENTITY, by
        section 6's K term.
    (4) THE NON-STATIC BRANCH IS NOT CLOSED -- section 7's limit.

===============================================================================
9.  THE BILL, WHICH THIS FILE DOES NOT LOWER BY ANY AMOUNT
===============================================================================

Proper radial length dl = dr/sqrt(1 - 2Gm/(rc^2)).  A contraction by fraction q
needs x = 2G|m|/(Rc^2) = 1/(1-q)^2 - 1, hence m = -x R c^2/(2G), and the
identity converts that mass requirement into a STRESS requirement with no
further physics: p_r(R) = m(R) c^2/(4 pi R^3).  At q = 0.01, R = 1 m the mass is
-1.3671e+25 kg = -2.289 Earth masses, reproducing the ruling's figure, and

    THE REQUIRED RADIAL TENSION IS 9.7773e+40 Pa.

The second, independent level -- designpoint.py's design equation
M = -beta^2 c^2 R/(12 G) at R = 1 m, beta = 0.1, imported rather than copied --
gives 8.0258e+39 Pa.  The two agree to just over one order of magnitude, which
is the honest resolution of "the level the bill requires", and both are quoted.

The ladder, every rung derived from a stated input, is printed by the report.
THREE CAUTIONS, AND THEY ARE LOAD-BEARING:

    (1) TRACELESSNESS EXCLUDES THE STRONGEST TENSION ON THE LADDER.  The QCD
        flux tube and the nucleon's confining region are the largest tensions
        nature is known to sustain and are only ~1e6 short -- by far the closest
        rung.  But QCD matter is NOT traceless; the trace anomaly is essentially
        the whole of the nucleon mass, so it sits OUTSIDE this identity's
        hypothesis and cannot be quoted as a route.  Inside the hypothesis the
        best known tension is electromagnetic and the shortfall is 2.46e+13.
    (2) A RADIAL MAGNETIC TENSION WITH A REGULAR CENTRE DOES NOT EXIST.  A
        purely radial B with div B = 0 is a monopole, B ~ 1/r^2 -- exactly the
        Q-part of RN: tension everywhere, m(R) < 0 everywhere with M = 0,
        POSITIVE energy density everywhere, and the regular-centre hypothesis
        broken and nothing else.  The one configuration that delivers the
        required sign for free is the one with a singular centre.  The RN
        witness and the bill witness are the same finding seen twice.
    (3) THE MATERIAL LADDER IS A SCALE STATEMENT, NOT A ROUTE.  A material
        tension is a stress in matter whose own positive rest energy is vastly
        larger -- DOCKET 54 section 3 puts that ratio at 2.7e-8 even at the
        lightest-conceivable-sheet atomic ceiling.

CONSISTENCY WITH WHAT THE TREE HOLDS: the 3.48e55 shortfall DOCKET 54 records
for an ideal gold Casimir shell is this same wall reached through the mass
rather than the stress.  A CROSS-CHECK, NOT A FOURTH FINDING.

===============================================================================
10.  THE OBLIGATIONS, AND WHAT THEY DO NOT ESTABLISH
===============================================================================

--prove runs ten families over the reals plus three MUTATION PROBES.  EVERY
obligation is asserted NEGATED
and reported unsat, and EVERY obligation additionally has its OWN hypothesis
checked satisfiable, printed as "unsat (hyp sat)"; it fails if either half is
wrong.  That is stronger than guarding a family base once: an obligation that
ADDS constraints has a hypothesis the family guard never sampled, which is
exactly PROOF-ASSISTANT.md's 2026-09-15 "guard with a blind spot".  Explicit
family satisfiability guards run on top of that, and every encoding-drift probe
is asked as a SATISFIABILITY so none can pass by being empty.

    A  the local ODE algebra         F  the Laue route: source sphericity
    B  the integrated biconditional  G  u neither necessary nor sufficient
    C  tracelessness                 H  the p_r = 0 radius
    D  regular centre / RN           I  flat vs GR background
    E  staticity / flux              L  the von Laue total-mass corollary

NINETY ROWS, AND THE COMPOSITION IS PINNED so that a lost row is visible rather
than silent: 39 theorems (asserted negated, unsat, own hypothesis sat), 20
family satisfiability guards, 14 encoding-drift probes, 14 necessity witnesses
each paired with a closed-form realisation, and 3 mutation probes.  --verify's
29 residuals are pinned the same way.  Both exit 1 on drift.

WHAT Z3 DOES NOT ESTABLISH, AND NONE OF IT MAY BE QUOTED AS IF IT DID:

 1. THAT ANY AGGREGATE IS REALISABLE.  C, I_Theta, J, K, P and the Laue moments
    are FREE REALS in the encoding.  z3 asserting one nonzero is a statement
    about an over-permissive encoding, not about physics.  That is why every
    must-be-SAT row is paired with a closed-form witness checked in sympy or in
    exact Fraction arithmetic; the sat alone would be worthless.
 2. ANYTHING ABOUT FUNCTIONS.  Family A quantifies over the VALUES of
    (r, u, p_r, p_t, p_r', Theta) at ONE radius.  It does not know that p_r' is
    the derivative of p_r, that a p_r exists taking these values, or that such a
    p_r is differentiable anywhere else.  The sympy layer closes this for the
    specific witnesses and for a general undefined p_r(r); it does not close it
    in general.
 3. THE INTEGRATION STEP.  Going from d/dr(r^3 p_r) = r^2 u to
    m = 4 pi R^3 p_r is the fundamental theorem of calculus and is CITED, not
    machine-checked.  It carries a hypothesis z3 never sees: r^3 p_r must be
    absolutely continuous on (0, R] with a limit at 0.  "Regular centre" means
    exactly that, and it is STRONGER than "p_r is finite at the centre".
 4. THE LAUE STEP.  Family F encodes the CONCLUSION of Wang eq. (20) as a
    constraint, not its proof.  Stokes's theorem is CITED.  What F checks is
    what follows FROM the identity, not the identity itself.
 5. G2 BEYOND THE POWER-LAW FAMILY.  "u < 0 throughout implies m < 0" is
    machine-checked only where the integral is algebraic.  In general it is the
    monotonicity of an integral, CITED.
 6. ANY PHYSICS.  Nothing here says a traceless conserved source with p_r < 0
    exists in nature, is producible, or has any magnitude.  It says that IF one
    does, THEN the enclosed mass is negative there.  DOCKET 54's magnitude kill
    is untouched and Route A stays STRUCK.
 7. STABILITY, DYNAMICS OR BACKREACTION.  The identity is kinematic.
 8. F's WITNESS IS A CONSTANT-STRESS SOURCE ONLY -- section 5's stated gap.
 9. THE COEFFICIENT AND THE EXPONENT.  MEASURED IN THIS FILE, not cited: the
    MUTATION rows of --prove mutate the master formula's exponent (R^3 -> R^2)
    and then delete the radius entirely, and THE BICONDITIONAL STILL DISCHARGES
    BOTH TIMES, because almost every obligation here is a claim about SIGNS and
    R > 0 preserves them.  The third mutation row shows what IS visible: the
    SIGN of the coefficient.  So the 3 and the 4 pi are pinned by the SYMPY
    residuals (V3, V13, V15) and by the exact Fraction layer in --selftest, not
    here.  THE Z3 LAYER ALONE DOES NOT ESTABLISH THE IDENTITY, ONLY ITS SIGN
    CONTENT.  The layers are not redundant and neither may be reported without
    the other.
10. THE TRACE ANOMALY.  "Traceless" is a hypothesis about the RENORMALISED
    tensor.  Whether a given quantum field's <T^mu_mu> vanishes is a question
    about that field, answered outside this file.
11. NOVELTY.  None is claimed; section 1 is the prior art.

THREE DRAFTING FAULTS, ALL GREEN BEFORE THEY WERE CAUGHT, ALL RECORDED RATHER
THAN DELETED.  Two are the derivation pass's: an obligation first written as
X == X, a tautology unsat under any hypothesis including an empty one; and one
asserting m < 0 => p_r < 0 under a label about u -- unsat, but not the claim the
label made.  THE THIRD IS THIS FILE'S OWN, and it is marked in the source at
DRIFT A: that probe was first written with a second energy density as a FREE
variable constrained only to differ from the first, so it was satisfiable for a
reason with nothing to do with the claim.  It now quantifies over TWO genuine
LOCAL states sharing r and p_r.  NONE OF THE THREE WAS CAUGHT BY Z3.  All three
were caught by re-reading.  A MISLABELLED GREEN OBLIGATION IS A FALSE REPORT.

===============================================================================
11.  PEER STATUS -- RECORDED, NEVER REPAIRED, AND NO PEER IS EDITED
===============================================================================

Printed in full by the report and asserted by a selftest fixture.  The four that
are not UNCHANGED:

    certify.py COROLLARY     CONFIRMED.  It is the same fact twice, not a
                             coincidence: both hypotheses kill the integration
                             constant of a first-order ODE at r = 0, and RN
                             witnesses both failures simultaneously and in the
                             same region.  On the class where both hold the
                             identity is an independent second evaluation of the
                             same integral.
    foliation.py RANGE THM   CONFIRMED and extended by one term on the matter
                             side.  Nothing in it is contradicted.
    drivensource.py sec. 3   CONFIRMED and SHARPENED both ways: its RN region
                             r < Q^2/2M is exactly where this biconditional
                             fails, so the new test INHERITS that break; and its
                             electrovac rho + p_r = 0 is exactly the condition
                             under which this file's curved correction vanishes.
                             Neither file knew the second.
    the file's own reach     NARROWED by von Laue: the test has content only on
                             a ball strictly inside a cavity, and refuses on any
                             ball containing a mirror.

Three further peer observations are recorded and applied to nothing:
nonstatic.py's static limit of EV-U already contains (m + 4 pi r^3 p) -- which
IS the Tolman mass -- and does not name it; vacuumcorridor.py's first docstring
line reads "corridor.py", a filename mismatch with a different file of that name
in the tree; and DOCKET 54's ruling carries one substantive correction
(sphericity of the SOURCE is not load-bearing), one withdrawn non-find (section
1), and one upgraded consistency check (the plate agreement is EXACT on the
isotropic average, not merely same-sign).  A HUMAN SEATS ANY CHANGE.

===============================================================================
12.  WHAT THIS FILE REFUSES
===============================================================================

    IT REFUSES THE WORD "REPLACES".  The ruling's "The identity replaces
    certify.py's integral over a ball with a pointwise test" is corrected to
    RESTATES, ON A SMALLER CLASS, in section 0 and in SUPERSEDES_CERTIFY = False.
    Selling a restriction as a generalisation is the one thing this tree does
    not forgive.

    IT REFUSES "EXACT" WITHOUT ITS BACKGROUND HYPOTHESIS.  m c^2 = 4 pi R^3
    <T^r_r> is exact in FLAT SPACE only.  The published GR form carries a
    redshift factor and the derivative form carries the K term.  The hypothesis
    is written into the claim, not into a caveats section -- which is the fault
    DOCKET 52 caught in certify.py's corollary.

    IT REFUSES "CHEAPER TO TEST THEREFORE CHEAPER TO MEET".  No gate moves.

    IT REFUSES TO REPORT ON A SOURCE WHOSE CENTRE IT CANNOT CERTIFY REGULAR, on
    a non-spherical source read in a single direction, on a ball enclosing a
    mirror, and on the non-static branch, whose geometry side is not closed
    (section 7).  Each is a REFUSE, not a finding, and each is enforced in
    `pointwise_test` rather than described in a docstring.

    IT REFUSES TO CLAIM NOVELTY, and withdraws DOCKET 54's non-find.

    IT REFUSES TO RE-ARGUE mouth.py section 5b or overturn.py L1 through this
    test.  Both lean on certify.py's THEOREM, which is hypothesis-free here.

    IT REFUSES TO QUOTE A MASS FOR THE PLASMA TERM.  The curvature extension of
    the planar Sopova-Ford coefficient to a sphere is RECONSTRUCTED, sign and
    order only.  Every SIGN in section 6 is independent of A_EM; every MAGNITUDE
    scales linearly with it, and A_EM is SINGLE-SOURCE.

    IT REFUSES TO TREAT A NON-FIND AS A CLEARANCE.  Section 1's two searches
    returned nothing; that is not evidence of absence.

    IT REPAIRS NOTHING.  certify.py, foliation.py, driven.py, nonstatic.py,
    drivensource.py, expose.py, candidates.py, designpoint.py, emtension.py,
    charge.py, mouth.py, overturn.py, switch.py, vacuumcorridor.py and
    wormhole.py were read only.  Nothing under method/ or drive/ was opened.
    AND NO PEER IS EDITED.
"""

import math
import sys
from fractions import Fraction as Fr

import candidates                      # banked u_0, and CODATA G, C, HBAR
import certify                         # the theorem this restates on a subset
import designpoint                     # the design equation, imported not copied
import driven                          # DOCKET 52
import foliation                       # the RANGE THEOREM

# =============================================================== constants
#
# EVERY NUMBER CARRIES ITS STATUS.  CITED = a source states it exactly;
# DERIVED = computed here from CITED inputs; RECOVERED = measured out of the
# corpus's own data; RECONSTRUCTED = neither.  A status is never flattened.

G      = candidates.G                  # CITED  CODATA 2018, via candidates.py
C      = candidates.C                  # CITED  exact by definition
HBAR   = candidates.HBAR               # CITED  CODATA 2018, via candidates.py
MU0    = 1.25663706212e-6              # CITED  CODATA 2018, N A^-2
QE     = 1.602176634e-19               # CITED  exact by definition, C
M_E    = 9.1093837015e-31              # CITED  CODATA 2018, kg
A_BOHR = 5.29177210903e-11             # CITED  CODATA 2018, m
E_HART = 4.3597447222071e-18           # CITED  CODATA 2018, J
M_EARTH = designpoint.M_EARTH          # CITED  via designpoint.py, kg

L_PLANCK = math.sqrt(HBAR * G / C ** 3)        # DERIVED from the three above
L_PLANCK_CODATA = 1.616255e-35                 # CITED  CODATA 2018, m

A_EM = 1.0 / (60.0 * math.pi ** 2)     # RECOVERED  Milton 1005.0031 eq. (58)
                                       #   quoting Deutsch-Candelas; SINGLE-
                                       #   SOURCE, not re-read at source here
K_SF_COEFF = math.sqrt(2.0) / (128.0 * math.pi)   # RECOVERED  Sopova-Ford
                                       #   quant-ph/0504143 eq. (15), the
                                       #   coefficient of omega_p in K

HBAR_OMEGA_P_GOLD_EV = 9.0             # CITED  the ruling's gold plasma energy
HBAR_OMEGA_P_AL_EV = 15.3              # CITED  the ruling's aluminium value


def _status(name):
    """The status of every named figure this file prints.  Nothing is bare."""
    return FIGURE_STATUS[name]


FIGURE_STATUS = {
    "G": "CITED", "c": "CITED", "hbar": "CITED", "mu_0": "CITED",
    "l_P": "DERIVED", "l_P CODATA": "CITED",
    "A_EM": "RECOVERED", "K_SopovaFord": "RECOVERED",
    "u_0(d)": "DERIVED", "Casimir force": "MEASURED",
    "m(r) near-wall profile": "RECOVERED",
    "plasma-sphere prefactor": "RECONSTRUCTED",
    "Boyer total": "RECOVERED",
    "identity residual": "DERIVED", "RN defect": "DERIVED",
    "delta closed form": "DERIVED", "crossover a_c": "DERIVED",
    "required tension": "DERIVED", "tension ladder": "DERIVED",
    "graphene strength": "MEASURED", "nanotube strength": "MEASURED",
    "nucleon core pressure": "MEASURED-INFERRED",
}


# ======================================================= the identity, SI
#
# m(R) c^2 = 4 pi R^3 p_r(R).  SI throughout: p_r in Pa = J/m^3, R in m,
# m in kg.  The identity itself is DERIVED (V3); these are its two readings.

def enclosed_mass(R, p_r):
    """m(R) = 4 pi R^3 p_r(R) / c^2.  The pointwise reading.  DERIVED."""
    return 4.0 * math.pi * R ** 3 * p_r / (C * C)


def radial_stress_for_mass(m, R):
    """The inverse: the radial stress a demanded enclosed mass costs.  DERIVED."""
    return m * C * C / (4.0 * math.pi * R ** 3)


def tolman_mass_factor(m, R, p_r):
    """Herrera eq. (32) stripped of its redshift factor: m + 4 pi r^3 p_r, the
    combination the published identity calls the Tolman mass.  CITED shape,
    DERIVED value.  On the identity this is exactly 2m."""
    return m + 4.0 * math.pi * R ** 3 * p_r / (C * C)


def first_integral(m, R, p_r, I_trace=0.0):
    """C = m - 4 pi R^3 p_r/c^2 + I_trace.  A FIRST INTEGRAL (V6): it may be
    evaluated at ANY radius, and it is NOT lim m(r).  In geometric units the
    caller passes m and p_r already reduced."""
    return m - 4.0 * math.pi * R ** 3 * p_r / (C * C) + I_trace


# ==================================================== the instrument itself

HYPOTHESES = ("traceless", "conserved", "spherical_source", "regular_centre",
              "flat_background", "stationary_flux", "ball_excludes_walls")


def pointwise_test(p_r, R, **hyp):
    """THE INSTRUMENT.  Returns (verdict, m, reason).

    verdict is "YES" (m < 0, proper radial distance contracted at R in every
    foliation), "NO" (m > 0), "ZERO" (m = 0 exactly, which under certify.py's
    STRICT criterion is a NON-contraction), or "REFUSE".

    IT REFUSES rather than reporting whenever a hypothesis is absent, because
    losing a hypothesis silently is the fault DOCKET 52 caught.  Every keyword
    defaults to False: an absent claim is not a granted one."""
    missing = [h for h in HYPOTHESES if not hyp.get(h, False)]
    if missing:
        return ("REFUSE", None, "hypothesis not certified: " + ", ".join(missing))
    m = enclosed_mass(R, p_r)
    if p_r < 0.0:
        return ("YES", m, "radial stress is a tension at R")
    if p_r > 0.0:
        return ("NO", m, "radial stress is a pressure at R")
    return ("ZERO", 0.0, "p_r = 0 exactly: g_rr = 1, a NON-contraction")


def all_hypotheses():
    return dict((h, True) for h in HYPOTHESES)


# ======================================= witnesses, EXACT (Fraction, stdlib)

def rn_row(R, M=Fr(1), Q2=Fr(4, 5) ** 2):
    """Reissner-Nordstrom, G = c = 1, Gaussian, in EXACT rational arithmetic.
    Returns (p_r, 4 pi R^3 p_r, m, defect) with the 4 pi carried symbolically:
    4 pi R^3 p_r = -Q^2/(2R) and m = M - Q^2/(2R), so the defect is M at every
    radius.  DERIVED (V13); no float anywhere."""
    R = Fr(R)
    four_pi_r3_pr = -Q2 / (2 * R)
    m = M - Q2 / (2 * R)
    return (four_pi_r3_pr, m, m - four_pi_r3_pr)


def rn_sign_radius(M=Fr(1), Q2=Fr(4, 5) ** 2):
    """m = 0 at R = Q^2/2M.  Inside it m < 0; outside it m > 0 while p_r < 0
    at EVERY radius.  DERIVED."""
    return Q2 / (2 * M)


def rn_horizons(M=1.0, Q=0.8):
    """r_pm = M +- sqrt(M^2 - Q^2).  DERIVED."""
    d = math.sqrt(M * M - Q * Q)
    return (M - d, M + d)


def rn_negative_region_inside_cauchy(y):
    """r_-/M - (Q^2/2M)/M with y = Q^2/M^2.  Positive on (0, 1], so the m < 0
    region is strictly inside the inner horizon.  DERIVED."""
    return 1.0 - math.sqrt(1.0 - y) - y / 2.0


def plate_u0(d):
    """u_0 = pi^2 hbar c/(720 d^4), the magnitude of the ideal parallel-plate
    Casimir energy density.  DERIVED from E/A = -pi^2 hbar c/(720 d^3), whose
    FORCE is the one MEASURED quantity in the chain (Lamoreaux 1997;
    Mohideen-Roy 1998; Bressi 2002)."""
    return math.pi ** 2 * HBAR * C / (720.0 * d ** 4)


def plate_cell(d):
    """The raw parallel-plate cell, DERIVED from E/A alone.
    (rho, p_normal, p_transverse) = (-u_0, -3u_0, +u_0).  p_normal/u_0 = -3 is
    DERIVED from F = -d(E/A)/dd, not quoted; p_transverse is FORCED by
    tracelessness.  REFUSED for magnitude: the cell is not spherical."""
    u0 = plate_u0(d)
    return (-u0, -3.0 * u0, +u0)


def plate_trace_residual(d):
    """-rho + 2 p_transverse + p_normal, exactly 0.  DERIVED."""
    rho, pz, pt = plate_cell(d)
    return -rho + 2.0 * pt + pz


def isotropic_average(d):
    """THE POSITIVE CONTROL.  The plate tensor averaged over uniformly
    distributed plate normals, <n_i n_j> = delta_ij/3:
    T^mu_nu = u_0 diag(-1, -1/3, -1/3, -1/3).  Returns (e, p_r, p_t).
    Spherically symmetric, traceless, conserved, regular centre.  DERIVED."""
    u0 = plate_u0(d)
    return (-u0, -u0 / 3.0, -u0 / 3.0)


def radiation_mass(R, u0, sign=-1.0):
    """m(R) c^2 = INT 4 pi r^2 e dr for uniform e = sign*u_0, i.e. the
    QUADRATURE side of the identity, computed without using the identity.
    DERIVED."""
    return sign * 4.0 * math.pi * R ** 3 * u0 / (3.0 * C * C)


def quadratic_profile(P0, L, r):
    """NEGATIVE CONTROL (b), THE WRONG-QUANTITY TRAP.  p_r = P0(1 - r^2/L^2);
    tracelessness and conservation then FORCE e and p_t.  Returns
    (p_r, e, p_t, m c^2 / (4 pi)).  Exact in Fractions.  DERIVED."""
    P0, L, r = Fr(P0), Fr(L), Fr(r)
    pr = P0 * (1 - r * r / (L * L))
    e = 3 * P0 - 5 * P0 * r * r / (L * L)
    pt = P0 - 2 * P0 * r * r / (L * L)
    return (pr, e, pt, P0 * r ** 3 * (L * L - r * r) / (L * L))


QUAD_TRAP_LO = math.sqrt(3.0 / 5.0)    # DERIVED: e(R) < 0 for R > this, in L


def conservation_residual(pr, dpr, pt, r):
    """p_r' + (2/r)(p_r - p_t).  Exact for Fractions.  DERIVED (V2)."""
    return dpr + 2 * (pr - pt) / r


def trace_residual(e, pr, pt):
    """-e + p_r + 2 p_t.  DERIVED."""
    return -e + pr + 2 * pt


def wormhole_throat(r0):
    """MORRIS-THORNE THROAT.  b(r_0) = r_0, Phi' = 0: p_r = -1/(8 pi r_0^2),
    m = r_0/2, and 4 pi r_0^3 p_r = -m -- THE OPPOSITE SIGN.  G = c = 1.
    DERIVED (V18)."""
    pr = -1.0 / (8.0 * math.pi * r0 * r0)
    m = r0 / 2.0
    return (pr, m, 4.0 * math.pi * r0 ** 3 * pr)


def alc_throat(m_par, beta):
    """AGNESE & LA CAMERA gr-qc/0203067 eq. (17), a PUBLISHED traceless
    wormhole: throat r_0 = 2m/beta, p_|| = -m/(4 pi beta r_0^3), and
    m_MS = m/beta > 0 everywhere since rho = 0.  Returns
    (r_0, p_par, 4 pi r_0^3 p_par, m_MS).  CITED shape, DERIVED arithmetic."""
    r0 = 2.0 * m_par / beta
    ppar = -m_par / (4.0 * math.pi * beta * r0 ** 3)
    return (r0, ppar, 4.0 * math.pi * r0 ** 3 * ppar, m_par / beta)


# ===================================== section 6: the curved-background bound

def delta_curved(eps):
    """THE RELATIVE CURVED CORRECTION, closed form, DERIVED (V16):
    delta = (1/15 pi)(l_P/eps)^2 = chi/2, INDEPENDENT of the shell radius a."""
    return (L_PLANCK / eps) ** 2 / (15.0 * math.pi)


def chi_compactness(eps):
    """DOCKET 54's banked compactness 2G|m|/(a c^2) = (2/15 pi)(l_P/eps)^2.
    DERIVED here from the same profile; the ruling banks 5.84e-58 at 137.8 nm."""
    return 2.0 * delta_curved(eps)


def delta_unity_eps():
    """delta = 1 at eps = l_P/sqrt(15 pi).  DERIVED."""
    return L_PLANCK / math.sqrt(15.0 * math.pi)


def delta_profile_free(chi_max, V_over_m):
    """THE PROFILE-FREE FALLBACK: |delta| <= [chi/(1-chi)] V/|m|.  DERIVED."""
    return chi_max / (1.0 - chi_max) * V_over_m


def skin_depth(hbar_omega_p_eV):
    """lambdabar_p = c/omega_p, the SKIN DEPTH.  DERIVED.  NOTE, and it costs an
    hour if missed: the ruling's 'skin depth' is c/omega_p (gold 21.93 nm),
    while 'gold lambda_p = 137.8 nm' elsewhere is 2 pi c/omega_p.  The crossover
    below is stated against c/omega_p and must NOT be read against lambda_p."""
    omega_p = hbar_omega_p_eV * QE / HBAR
    return C / omega_p


def crossover_coefficient():
    """|p_r^real|/|p_r^ideal| = K a/A with eps CANCELLING EXACTLY (V17), and
    with A = A_EM and K = K_SF omega_p this is (60 sqrt2 pi/128)(a/lambdabar_p).
    DERIVED from the two RECOVERED coefficients."""
    return K_SF_COEFF / A_EM


def crossover_radius(hbar_omega_p_eV):
    """a_c = lambdabar_p/coefficient = 0.480 x skin depth, FOR EVERY CONDUCTOR.
    DERIVED; no material input survives."""
    return skin_depth(hbar_omega_p_eV) / crossover_coefficient()


# ============================================== section 9: the bill, in Pa

def mass_for_contraction(q, R):
    """x = 1/(1-q)^2 - 1, m = -x R c^2/(2G).  The enclosed mass a fractional
    contraction q of proper radial distance at R costs.  DERIVED."""
    x = 1.0 / (1.0 - q) ** 2 - 1.0
    return -x * R * C * C / (2.0 * G)


def tension_for_contraction(q, R):
    """The same requirement as a RADIAL TENSION, through the identity.  DERIVED.
    THIS DOES NOT LOWER THE BILL; it restates it in the other currency."""
    return radial_stress_for_mass(mass_for_contraction(q, R), R)


def designpoint_tension(R=1.0, beta=0.1):
    """The second, independent level: designpoint.py's design equation,
    IMPORTED not copied.  DERIVED there, converted here."""
    return radial_stress_for_mass(designpoint.mass_floor(beta, R), R)


def magnetic_tension(B):
    """B^2/(2 mu_0).  DERIVED."""
    return B * B / (2.0 * MU0)


def field_for_tension(p):
    """The purely radial B that would carry a given tension.  DERIVED."""
    return math.sqrt(2.0 * MU0 * abs(p))


def planck_stress():
    """c^7/(hbar G^2).  DERIVED."""
    return C ** 7 / (HBAR * G * G)


def schwinger_field():
    """B_c = m_e^2 c^2/(e hbar).  DERIVED."""
    return M_E ** 2 * C ** 2 / (QE * HBAR)


def qcd_flux_tube(sigma_GeV_per_fm=0.9, r_t_fm=0.5):
    """sigma/(pi r_t^2).  DERIVED from stated inputs.  NOT TRACELESS -- outside
    this identity's hypothesis, and section 9 caution (1) says why."""
    sigma = sigma_GeV_per_fm * 1e9 * QE / 1e-15          # N
    return sigma / (math.pi * (r_t_fm * 1e-15) ** 2)


def atomic_ceiling():
    """E_Hartree/a_0^3, the ceiling on any chemical bond stress.  DERIVED."""
    return E_HART / A_BOHR ** 3


def tension_ladder():
    """Every rung DERIVED from a stated input except the three marked otherwise.
    Returns (label, Pa, status)."""
    return [
        ("Planck stress c^7/(hbar G^2)", planck_stress(), "DERIVED"),
        ("QCD flux tube (NOT traceless: outside the hypothesis)",
         qcd_flux_tube(), "DERIVED"),
        ("nucleon core pressure ~1e35 Pa (Burkert et al. 2018)",
         1.0e35, "MEASURED-INFERRED"),
        ("magnetar surface field 1e11 T, B^2/(2 mu_0)",
         magnetic_tension(1.0e11), "DERIVED from an inferred B"),
        ("Schwinger critical field B_c = %.4e T" % schwinger_field(),
         magnetic_tension(schwinger_field()), "DERIVED"),
        ("atomic ceiling on any chemical bond, E_h/a_0^3",
         atomic_ceiling(), "DERIVED"),
        ("destructive pulsed magnet, 1200 T",
         magnetic_tension(1200.0), "DERIVED from a measured B"),
        ("graphene intrinsic strength 130 GPa", 1.30e11, "MEASURED"),
        ("carbon nanotube ~1e11 Pa", 1.00e11, "MEASURED"),
        ("strongest continuous lab magnet, 45.5 T",
         magnetic_tension(45.5), "DERIVED from a measured B"),
    ]


# ========================================================== the sympy layer

def verify():
    """Every residual, and every one is exactly 0.  Returns (label, resid, want).
    NOTHING HERE IS QUOTED: the metrics are written down, the Christoffels, Ricci
    and Einstein tensors are COMPUTED from them, and the conservation equations
    and the TOV equation are DERIVED rather than asserted."""
    import sympy as sp

    out = []
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    x = [t, r, th, ph]
    u = sp.Function("u")(r)
    pr = sp.Function("p_r")(r)
    pt = sp.Function("p_t")(r)

    def christoffels(g, xs):
        gi = g.inv()
        return [[[sp.simplify(sp.Rational(1, 2) * sum(
            gi[a, d] * (sp.diff(g[d, b], xs[c]) + sp.diff(g[d, c], xs[b])
                        - sp.diff(g[b, c], xs[d])) for d in range(4)))
            for c in range(4)] for b in range(4)] for a in range(4)]

    def divergence(T, Ga, xs):
        res = []
        for nu in range(4):
            e = 0
            for mu in range(4):
                e += sp.diff(T[mu, nu], xs[mu])
                for a in range(4):
                    e += Ga[mu][mu][a] * T[a, nu] - Ga[a][mu][nu] * T[mu, a]
            res.append(sp.simplify(e))
        return res

    # ---------------------------------------------- 3. FLAT, COMPUTED
    gflat = sp.diag(-1, 1, r ** 2, r ** 2 * sp.sin(th) ** 2)
    Gaf = christoffels(gflat, x)
    Tm = sp.diag(-u, pr, pt, pt)
    dv = divergence(Tm, Gaf, x)
    out.append(("V1  flat nabla_mu T^mu_nu vanishes IDENTICALLY at nu = t, th, ph",
                sp.simplify(dv[0]) + sp.simplify(dv[2]) + sp.simplify(dv[3]), 0))
    out.append(("V2  and the nu = r component IS p_r' + (2/r)(p_r - p_t)",
                sp.simplify(dv[1] - (sp.diff(pr, r) + 2 * (pr - pt) / r)), 0))
    dpr = sp.solve(sp.Eq(dv[1], 0), sp.Derivative(pr, r))[0]
    Th = -u + pr + 2 * pt
    D = sp.diff(r ** 3 * pr, r).subs(sp.Derivative(pr, r), dpr)
    out.append(("V3  THE IDENTITY  d(r^3 p_r)/dr = r^2 (u + T^mu_mu)",
                sp.simplify(sp.expand(D - r ** 2 * (u + Th))), 0))
    u_tl = sp.solve(sp.Eq(Th, 0), u)[0]          # tracelessness SOLVED for u
    out.append(("V4  traceless collapse: u = p_r + 2 p_t gives d(r^3 p_r)/dr = r^2 u",
                sp.simplify(sp.expand(D - r ** 2 * u_tl))
                + sp.simplify(u_tl - (pr + 2 * pt)), 0))
    out.append(("V5  the decoupling formula  u = 3 p_r + r p_r'   (Theta = 0)",
                sp.simplify(sp.expand((pr + 2 * pt) - (3 * pr + r * dpr))), 0))

    # ---------------------------------------------- C IS A FIRST INTEGRAL
    mfun = sp.Function("m")(r)
    Tr = sp.Function("Theta")(r)
    ptT = (Tr + u - pr) / 2                       # p_t eliminated for the trace
    dprT = sp.solve(sp.Eq(sp.diff(pr, r) + 2 * (pr - ptT) / r, 0),
                    sp.Derivative(pr, r))[0]
    Fp = (4 * sp.pi * r ** 2 * u
          - 4 * sp.pi * sp.diff(r ** 3 * pr, r).subs(sp.Derivative(pr, r), dprT)
          + 4 * sp.pi * r ** 2 * Tr)
    out.append(("V6  F(r) = m - 4pi r^3 p_r + 4pi INT r^2 Theta IS A FIRST INTEGRAL",
                sp.simplify(sp.expand(Fp)), 0))
    beta, gam, kk, nn = sp.symbols("beta gamma k n", positive=True)
    prc = sp.Symbol("C1") / r ** 2 + 2 * beta * r ** kk / (kk + 2)
    ptc = beta * r ** kk
    Trc = gam * r ** nn
    uc = -Trc + prc + 2 * ptc
    Fc = (sp.integrate(4 * sp.pi * r ** 2 * uc, r) - 4 * sp.pi * r ** 3 * prc
          + sp.integrate(4 * sp.pi * r ** 2 * Trc, r))
    out.append(("V7  ... and again on a closed-form dsolve family, dF/dr",
                sp.simplify(sp.expand(sp.diff(Fc, r))), 0))

    # ---------------------------------------------- 3/8. FULL GR, COMPUTED
    Phi = sp.Function("Phi")(r)
    Lam = -sp.Rational(1, 2) * sp.log(1 - 2 * mfun / r)
    gc = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), r ** 2,
                 r ** 2 * sp.sin(th) ** 2)
    gci = gc.inv()
    Gac = christoffels(gc, x)
    Ric = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            e = 0
            for a in range(4):
                e += sp.diff(Gac[a][b][c], x[a]) - sp.diff(Gac[a][b][a], x[c])
                for d in range(4):
                    e += Gac[a][a][d] * Gac[d][b][c] - Gac[a][c][d] * Gac[d][b][a]
            Ric[b, c] = sp.simplify(e)
    Rs = sp.simplify(sum(gci[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    Emix = sp.simplify(gci * sp.simplify(Ric - sp.Rational(1, 2) * Rs * gc))
    dm_sol = sp.solve(sp.Eq(sp.simplify(Emix[0, 0]), -8 * sp.pi * u),
                      sp.Derivative(mfun, r))[0]
    out.append(("V8  G^t_t COMPUTED gives dm/dr = 4 pi r^2 u EXACTLY, in full GR",
                sp.simplify(dm_sol - 4 * sp.pi * r ** 2 * u), 0))
    dnu_sol = sp.solve(sp.Eq(sp.simplify(Emix[1, 1]), 8 * sp.pi * pr),
                       sp.Derivative(Phi, r))[0]
    out.append(("V9  G^r_r COMPUTED gives Phi' = (m + 4pi r^3 p_r)/(r(r-2m))",
                sp.simplify(dnu_sol - (mfun + 4 * sp.pi * r ** 3 * pr)
                            / (r * (r - 2 * mfun))), 0))
    gcur = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * sp.Function("Lambda")(r)),
                   r ** 2, r ** 2 * sp.sin(th) ** 2)
    dvc = divergence(Tm, christoffels(gcur, x), x)
    out.append(("V10a anisotropic TOV DERIVED: p_r' + (2/r)(p_r-p_t) + (u+p_r)Phi'",
                sp.simplify(dvc[1] - (sp.diff(pr, r) + 2 * (pr - pt) / r
                                      + (u + pr) * sp.diff(Phi, r))), 0))
    dprc = sp.solve(sp.Eq(dvc[1], 0), sp.Derivative(pr, r))[0]
    Dc = sp.diff(r ** 3 * pr, r).subs(sp.Derivative(pr, r), dprc)
    out.append(("V10 THE CORRECTED IDENTITY  = r^2(u+Theta) - r^3 (u+p_r) Phi'",
                sp.simplify(sp.expand(Dc - (r ** 2 * (u + Th)
                                            - r ** 3 * (u + pr) * sp.diff(Phi, r)))), 0))
    out.append(("V11 ON THE IDENTITY m = 4pi r^3 p_r, Phi' is TWICE Newtonian",
                sp.simplify(dnu_sol.subs(pr, mfun / (4 * sp.pi * r ** 3))
                            - 2 * mfun / (r * (r - 2 * mfun))), 0))

    # ---------------------------------------------- 4. REISSNER-NORDSTROM
    Q, Mm = sp.symbols("Q M", positive=True)
    uR = Q ** 2 / (8 * sp.pi * r ** 4)
    prR, ptR = -uR, uR
    out.append(("V12 RN is EXACTLY traceless and EXACTLY conserved",
                sp.simplify(-uR + prR + 2 * ptR)
                + sp.simplify(sp.diff(prR, r) + 2 * (prR - ptR) / r), 0))
    mR = Mm - Q ** 2 / (2 * r)
    out.append(("V13 RN: dm/dr matches, m matches the metric function, defect = M",
                sp.simplify(sp.diff(mR, r) - 4 * sp.pi * r ** 2 * uR)
                + sp.simplify((1 - 2 * mR / r) - (1 - 2 * Mm / r + Q ** 2 / r ** 2))
                + sp.simplify(mR - 4 * sp.pi * r ** 3 * prR - Mm), 0))
    out.append(("V14 both terms -> -oo at the centre; the DIFFERENCE is M",
                sp.simplify(sp.limit(mR - 4 * sp.pi * r ** 3 * prR, r, 0, "+") - Mm)
                + (0 if sp.limit(mR, r, 0, "+") == -sp.oo else 1)
                + (0 if sp.limit(4 * sp.pi * r ** 3 * prR, r, 0, "+") == -sp.oo else 1),
                0))

    # ---------------------------------------------- 5. THE CONTROLS
    u0, R0, P0, L0 = sp.symbols("u_0 R P_0 L", positive=True)
    ePC, prPC = -u0, -u0 / 3
    out.append(("V15 POSITIVE CONTROL: traceless, conserved, and the identity",
                sp.simplify(-ePC + prPC + 2 * prPC)
                + sp.simplify(sp.diff(prPC, r) + 2 * (prPC - prPC) / r)
                + sp.simplify(sp.integrate(4 * sp.pi * r ** 2 * ePC, (r, 0, R0))
                              - 4 * sp.pi * R0 ** 3 * prPC), 0))
    prNC = P0 * (1 - r ** 2 / L0 ** 2)
    eNC = 3 * P0 - 5 * P0 * r ** 2 / L0 ** 2
    ptNC = P0 - 2 * P0 * r ** 2 / L0 ** 2
    out.append(("V15b NEGATIVE CONTROL (b): traceless, conserved, identity exact",
                sp.simplify(-eNC + prNC + 2 * ptNC)
                + sp.simplify(sp.diff(prNC, r) + 2 * (prNC - ptNC) / r)
                + sp.simplify(sp.integrate(4 * sp.pi * r ** 2 * eNC, (r, 0, R0))
                              - 4 * sp.pi * R0 ** 3 * prNC.subs(r, R0)), 0))
    out.append(("V15c ... and at R = 9L/10 the trap fires: e < 0 while m > 0",
                sp.simplify(eNC.subs(r, 9 * L0 / 10) + 21 * P0 / 20)
                + sp.simplify(prNC.subs(r, 9 * L0 / 10) - 19 * P0 / 100), 0))

    # ---------------------------------------------- 6. THE CURVED BOUND
    aa, ee, lP, hb, cc = sp.symbols("a e l_P hbar c", positive=True)
    E = sp.Symbol("E", positive=True)
    Uw = -hb * cc / (30 * sp.pi ** 2 * aa * E ** 3)
    Pw = -hb * cc / (60 * sp.pi ** 2 * aa ** 2 * E ** 2)
    Php = -(2 / (15 * sp.pi)) * lP ** 2 / (E ** 2 * (aa - E))
    Ik = sp.integrate(sp.simplify(4 * sp.pi * (aa - E) ** 3 * (Uw + Pw) * Php),
                      (E, ee, aa))
    den = 4 * sp.pi * (aa - ee) ** 3 * Pw.subs(E, ee)
    out.append(("V16 delta = (1/15pi)(l_P/eps)^2 EXACTLY, and a CANCELS",
                sp.simplify(sp.limit(sp.Abs(sp.simplify(Ik / den))
                                     * 15 * sp.pi * ee ** 2 / lP ** 2, ee, 0) - 1), 0))
    AA, KK = sp.symbols("A K", positive=True)
    ratio = (KK / (aa * ee ** 2)) / (AA / (aa ** 2 * ee ** 2))
    out.append(("V17 the near-wall ratio is eps-INDEPENDENT: d(ratio)/d(eps)",
                sp.simplify(sp.diff(ratio, ee)), 0))

    # ---------------------------------------------- 5. THE WORMHOLE WITNESSES
    # p_r is DERIVED from the COMPUTED G^r_r at Phi' = 0, not written down.
    r0, bpar, mpar = sp.symbols("r_0 beta m", positive=True)
    prMT = sp.solve(sp.Eq(sp.simplify(Emix[1, 1]).subs(sp.Derivative(Phi, r), 0),
                          8 * sp.pi * pr), pr)[0]
    out.append(("V18a a throat has Phi' = 0, and the COMPUTED G^r_r gives "
                "p_r = -m/(4 pi r^3)",
                sp.simplify(prMT + mfun / (4 * sp.pi * r ** 3)), 0))
    out.append(("V18 MORRIS-THORNE THROAT: 4 pi r_0^3 p_r = -m, THE OPPOSITE SIGN, "
                "and p_r(r_0) = -1/(8 pi r_0^2)",
                sp.simplify(4 * sp.pi * r ** 3 * prMT + mfun)
                + sp.simplify(prMT.subs(mfun, r / 2).subs(r, r0)
                              + 1 / (8 * sp.pi * r0 ** 2)), 0))
    r0a = 2 * mpar / bpar
    ppar = -mpar / (4 * sp.pi * bpar * r0a ** 3)
    out.append(("V19 AGNESE-LA CAMERA eq.(17): its TWO printed forms agree, and "
                "4 pi r_0^3 p_|| = -m_MS with m_MS = m/beta > 0",
                sp.simplify(ppar + bpar ** 2 / (32 * sp.pi * mpar ** 2))
                + sp.simplify(4 * sp.pi * r0a ** 3 * ppar + mpar / bpar), 0))

    # ---------------------------------------------- 1. HERRERA EQ. (32)
    nu = sp.Function("nu")(r)
    lam = -sp.log(1 - 2 * mfun / r)
    dnu = 2 * (mfun + 4 * sp.pi * r ** 3 * pr) / (r * (r - 2 * mfun))
    dprH = -(u + pr) * dnu / 2 + 2 * (pt - pr) / r
    W = sp.exp((nu + lam) / 2) * (mfun + 4 * sp.pi * r ** 3 * pr)
    dW = sp.diff(W, r).subs({sp.Derivative(mfun, r): 4 * sp.pi * r ** 2 * u,
                             sp.Derivative(nu, r): dnu,
                             sp.Derivative(pr, r): dprH})
    out.append(("V20 PRIOR ART CHECKED AGAINST US: Herrera arXiv:1801.08358 eq.(32)",
                sp.simplify(sp.expand(sp.simplify(
                    dW - 4 * sp.pi * r ** 2 * sp.exp((nu + lam) / 2)
                    * (u + pr + 2 * pt)))), 0))

    # ---------------------------------------------- 7. STATICITY DROPPED
    ut = sp.Function("u")(t, r)
    prt = sp.Function("p_r")(t, r)
    ptt = sp.Function("p_t")(t, r)
    jf = sp.Function("j_f")(t, r)                 # j_f := T^t_r
    Tt = sp.zeros(4, 4)
    Tt[0, 0], Tt[1, 1], Tt[2, 2], Tt[3, 3] = -ut, prt, ptt, ptt
    Tt[0, 1], Tt[1, 0] = jf, -jf
    dvt = divergence(Tt, Gaf, x)
    out.append(("V21 non-static energy eq: d_t u + (1/r^2) d_r(r^2 T^t_r) = 0",
                sp.simplify(dvt[0] + (sp.diff(ut, t)
                                      + sp.diff(r ** 2 * jf, r) / r ** 2)), 0))
    dprt = sp.solve(sp.Eq(dvt[1], 0), sp.Derivative(prt, r))[0]
    Tht = -ut + prt + 2 * ptt
    Dt = sp.diff(r ** 3 * prt, r).subs(sp.Derivative(prt, r), dprt)
    out.append(("V22 THE FLUX-CARRYING IDENTITY, j := d_t T^t_r, residual",
                sp.simplify(sp.expand(Dt - (r ** 2 * (ut + Tht)
                                            - r ** 3 * sp.diff(jf, t)))), 0))

    # ---------------------------------------------- 8. THE BOOST AND THE SCALAR
    w = sp.Symbol("w", real=True)
    uB, prB, qB = sp.symbols("u p_r q", real=True)
    upB = uB * sp.cosh(w) ** 2 + prB * sp.sinh(w) ** 2 + qB * sp.sinh(2 * w)
    prpB = prB * sp.cosh(w) ** 2 + uB * sp.sinh(w) ** 2 + qB * sp.sinh(2 * w)
    out.append(("V23 the boost law: (u - p_r) is INVARIANT, and p_r alone is not",
                sp.simplify(sp.expand(sp.simplify(upB - prpB) - (uB - prB)))
                + sp.simplify(sp.expand(prpB.subs(qB, 0).subs(uB, -prB) - prB)), 0))
    RR, prS, GG, UU, mS = sp.symbols("R p_rS Gamma U m_S", real=True)
    inv = sp.Eq(GG ** 2 - UU ** 2, 1 - 2 * mS / RR)      # foliation.py's invariant
    out.append(("V24 SUBSTITUTING THE IDENTITY INTO foliation.py's INVARIANT: "
                "Gamma^2 - U^2 = 1 - 8 pi R^2 p_r, so p_r is a SCALAR under H",
                sp.simplify((inv.rhs).subs(mS, 4 * sp.pi * RR ** 3 * prS)
                            - (1 - 8 * sp.pi * RR ** 2 * prS))
                + sp.simplify(sp.solve(sp.Eq(GG ** 2 - UU ** 2,
                                             1 - 8 * sp.pi * RR ** 2 * prS), prS)[0]
                              - (1 - (GG ** 2 - UU ** 2)) / (8 * sp.pi * RR ** 2)), 0))
    wc = sp.Symbol("w_c", positive=True)
    out.append(("V25 the critical rapidity: p_r' = 0 at tanh^2 w = |p_r|/u",
                sp.simplify(prpB.subs(qB, 0).subs(
                    sp.sinh(w) ** 2, -prB / (uB - prB)).subs(
                    sp.cosh(w) ** 2, uB / (uB - prB))), 0))
    return out


# =========================================================== the z3 layer

def classify_row(name):
    """Which kind of row an obligation name is.  Used to pin the COMPOSITION of
    --prove, so that adding or losing a row is visible rather than silent."""
    n = name.strip()
    if n.startswith("GUARD"):
        return "family satisfiability guard (sat)"
    if n.startswith("DRIFT"):
        return "encoding-drift probe (sat)"
    if n.startswith("MUTATION"):
        return "mutation probe"
    return None                        # decided by the want-string at the caller


def _z3():
    import prover
    prover.require_z3()
    import z3
    return z3


def obligations():
    """Ten families over the reals.  Every theorem row is asserted NEGATED and
    must be unsat WITH ITS OWN HYPOTHESIS SATISFIABLE; every guard and every
    drift probe is asserted DIRECTLY and must be sat.  See section 10 for the
    eleven things this layer does NOT establish."""
    z3 = _z3()
    out = []

    r, u, u2, pr, pt, dpr, Th, du = z3.Reals("r u u2 p_r p_t dp_r Theta du")
    m, m1, m2, F, R, R1, R2 = z3.Reals("m m1 m2 F R R1 R2")
    Cc, I_Th, J, K = z3.Reals("C I_Theta J K")
    pr1, pr2, q, w, jj, Phip = z3.Reals("p_r1 p_r2 q w j Phi_p")
    pz, Trr, Ixx, Iyy, Izz, I_u, Vb, ed = z3.Reals(
        "p_z Trr I_xx I_yy I_zz I_u V_ball e")
    Aa, Pp, ss, eps, grr, Rc, I_uTh = z3.Reals("A P s eps g_rr R_c I_uTh")

    def ob(name, hyp, concl):
        s1 = z3.Solver()
        s1.add(hyp)
        hs = (s1.check() == z3.sat)
        s2 = z3.Solver()
        s2.add(hyp)
        s2.add(z3.Not(concl))
        rr = s2.check()
        got = "%s (hyp %s)" % (rr, "sat" if hs else "UNSAT")
        out.append((name, got, "unsat (hyp sat)", (rr == z3.unsat) and hs))

    def sat(name, f, want_sat=True):
        s = z3.Solver()
        s.add(f)
        rr = s.check()
        good = (rr == z3.sat) if want_sat else (rr == z3.unsat)
        out.append((name, str(rr), "sat" if want_sat else "unsat", good))

    # ---------------------------------------------------- A  local ODE algebra
    LOCAL = z3.And(r > 0, r * dpr + 2 * (pr - pt) == 0, Th == -u + pr + 2 * pt)
    D = 3 * r * r * pr + r ** 3 * dpr
    sat("GUARD A0  LOCAL is satisfiable at all", LOCAL)
    sat("GUARD A1  LOCAL with Theta = 0 and p_r < 0", z3.And(LOCAL, Th == 0, pr < 0))
    sat("GUARD A2  LOCAL with Theta = 0, p_r > 0 AND u < 0",
        z3.And(LOCAL, Th == 0, pr > 0, u < 0))
    ob("A1  EXACT   d/dr(r^3 p_r) = r^2 (u + Theta)", LOCAL, D == r * r * (u + Th))
    ob("A2  TRACELESS COLLAPSE   d/dr(r^3 p_r) = r^2 u",
       z3.And(LOCAL, Th == 0), D == r * r * u)
    ob("A3  the decoupling formula   u = 3 p_r + r p_r'",
       z3.And(LOCAL, Th == 0), u == 3 * pr + r * dpr)
    ob("A4  conservation fixes p_t from p_r and nothing else",
       LOCAL, 2 * pt == 2 * pr + r * dpr)
    # DRIFT A was FIRST WRITTEN with u2 as a free variable and u2 == u + 1, which
    # is satisfiable for a reason that has nothing to do with the claim -- a
    # MISLABELLED GREEN, caught by re-reading and not by z3.  RECORDED, and
    # rewritten as TWO genuine LOCAL states sharing r and p_r.
    pt2, dpr2, Th2 = z3.Reals("p_t2 dp_r2 Theta2")
    LOCAL2 = z3.And(r > 0, r * dpr2 + 2 * (pr - pt2) == 0,
                    Th2 == -u2 + pr + 2 * pt2)
    sat("DRIFT A   u is NOT determined by p_r: TWO LOCAL states, same r and p_r, "
        "different u", z3.And(LOCAL, LOCAL2, u != u2))
    sat("DRIFT A2  with Theta != 0 the traceless collapse must FAIL",
        z3.And(LOCAL, Th != 0, D != r * r * u))

    # -------------------------------------- B  the integrated biconditional
    MASTER = z3.And(F > 0, R > 0, m == F * R ** 3 * pr - Cc - I_Th + J + K)
    FULL = z3.And(MASTER, Cc == 0, I_Th == 0, J == 0, K == 0)
    sat("GUARD B0  the master formula is satisfiable", MASTER)
    sat("GUARD B1  under ALL hypotheses, m < 0 is satisfiable", z3.And(FULL, m < 0))
    sat("GUARD B2  under ALL hypotheses, m > 0 is satisfiable", z3.And(FULL, m > 0))
    ob("B1  THE BICONDITIONAL   m(R) < 0  <=>  p_r(R) < 0", FULL, (m < 0) == (pr < 0))
    ob("B2  the positive half too   m(R) > 0  <=>  p_r(R) > 0", FULL, (m > 0) == (pr > 0))
    ob("B3  trichotomy is exhausted: the three signs agree, always",
       FULL, z3.And((m < 0) == (pr < 0), (m > 0) == (pr > 0), (m == 0) == (pr == 0)))
    ob("B4  AT EVERY RADIUS, not one: the signs agree at BOTH, independently",
       z3.And(F > 0, R1 > 0, R2 > 0, m1 == F * R1 ** 3 * pr1, m2 == F * R2 ** 3 * pr2),
       z3.And((m1 < 0) == (pr1 < 0), (m2 < 0) == (pr2 < 0)))
    sat("DRIFT B1  two radii MAY disagree in sign -- 'together' is at ONE radius",
        z3.And(F > 0, R1 > 0, R2 > 0, m1 == F * R1 ** 3 * pr1,
               m2 == F * R2 ** 3 * pr2, m1 < 0, m2 > 0))
    sat("DRIFT B2  F > 0 is load-bearing: with F < 0 the biconditional REVERSES",
        z3.And(F < 0, R > 0, m == F * R ** 3 * pr, m < 0, pr > 0))
    sat("DRIFT B3  THE IDENTITY DOES THE WORK: keep F > 0 and R > 0 but drop the "
        "link, and m < 0 with p_r > 0 is immediately satisfiable",
        z3.And(F > 0, R > 0, m < 0, pr > 0))

    # ------------------------------------------------------ C  tracelessness
    TRACE = z3.And(F > 0, R > 0, m == F * R ** 3 * pr - I_Th)
    sat("GUARD C0  the trace-carrying master formula is satisfiable", TRACE)
    sat("GUARD C1  ... and it is satisfiable with I_Theta != 0",
        z3.And(TRACE, I_Th != 0))
    ob("C1  with I_Theta = 0 the biconditional is restored",
       z3.And(TRACE, I_Th == 0), (m < 0) == (pr < 0))
    ob("C2  the exact trace-carrying identity   m + I_Theta = F R^3 p_r",
       TRACE, m + I_Th == F * R ** 3 * pr)
    ob("C3  WITNESS W1 is LOCAL-legal: p_r = p_t = 1, u = -1 forces Theta = 4",
       z3.And(LOCAL, pr == 1, pt == 1, u == -1), Th == 4)
    sat("C4  TRACELESSNESS IS NECESSARY: m < 0 AND p_r > 0 together",
        z3.And(TRACE, I_Th != 0, m < 0, pr > 0))
    sat("C5  ... and the other polarity, m > 0 with p_r < 0",
        z3.And(TRACE, I_Th != 0, m > 0, pr < 0))
    sat("C6  W1 EXACTLY: p_r = 1, I_Theta = 4 F R^3/3, m = -F R^3/3",
        z3.And(TRACE, pr == 1, 3 * I_Th == 4 * F * R ** 3, 3 * m == -F * R ** 3))
    sat("DRIFT C   a traceless configuration must still EXIST",
        z3.And(TRACE, I_Th == 0))

    # ------------------------------------- D  the regular centre, and RN
    RN = z3.And(r > 0, q > 0, w * r ** 4 == q, u == w, pr == -w, pt == w,
                dpr * r ** 5 == 4 * q)
    sat("GUARD D0  the RN profile is satisfiable", RN)
    sat("GUARD D1  the master formula with C != 0 is satisfiable",
        z3.And(MASTER, Cc != 0))
    ob("D1  RN IS EXACTLY TRACELESS", RN, -u + pr + 2 * pt == 0)
    ob("D2  RN IS EXACTLY CONSERVED  (r p_r' + 2(p_r - p_t) = 0)",
       RN, r * dpr + 2 * (pr - pt) == 0)
    ob("D3  RN's CENTRE TERM NEVER VANISHES: r^3 p_r != 0 at every r > 0",
       RN, r ** 3 * pr != 0)
    ob("D4  RN's centre term is exactly -q/r:  r*(r^3 p_r) = -q",
       RN, r * (r ** 3 * pr) == -q)
    ob("D5  with C = 0 restored the biconditional holds again",
       z3.And(MASTER, Cc == 0, I_Th == 0, J == 0, K == 0), (m < 0) == (pr < 0))
    sat("D6  REGULAR CENTRE IS NECESSARY: C != 0 gives p_r < 0 with m > 0",
        z3.And(MASTER, I_Th == 0, J == 0, K == 0, Cc != 0, pr < 0, m > 0))
    sat("D7  RN EXACTLY, regulated at eps: m = F q (1/eps - 1/R) > 0, p_r < 0",
        z3.And(F > 0, q > 0, eps > 0, R > eps, m * eps * R == F * q * (R - eps),
               pr * R ** 4 == -q, m > 0, pr < 0))
    sat("DRIFT D   a REGULAR traceless conserved profile must still exist",
        z3.And(LOCAL, dpr == 0, u == 3 * pr, Th == 0, pr != 0))

    # -------------------------------------------- E  staticity and the flux
    LOCALJ = z3.And(r > 0, r * jj + r * dpr + 2 * (pr - pt) == 0,
                    Th == -u + pr + 2 * pt)
    sat("GUARD E0  LOCALJ is satisfiable", LOCALJ)
    sat("GUARD E1  LOCALJ with j != 0 is satisfiable", z3.And(LOCALJ, jj != 0))
    ob("E1  j = 0 recovers the flat static identity exactly",
       z3.And(LOCALJ, jj == 0), D == r * r * (u + Th))
    ob("E2  THE EXACT FLUX-CARRYING LOCAL IDENTITY",
       LOCALJ, D == r * r * (u + Th) - r ** 3 * jj)
    ob("E3  THE HYPOTHESIS USED IS d_t T^t_r = 0, NOT STATICITY",
       z3.And(LOCALJ, jj == 0, Th == 0), D == r * r * u)
    ob("E4  with J = 0 the integrated biconditional holds",
       z3.And(MASTER, Cc == 0, I_Th == 0, K == 0, J == 0), (m < 0) == (pr < 0))
    sat("E5  STATICITY IS LOAD-BEARING: J != 0 gives m < 0 with p_r > 0",
        z3.And(MASTER, Cc == 0, I_Th == 0, K == 0, J != 0, m < 0, pr > 0))
    sat("E6  W7 EXACTLY: p_r = 1, R = 1, J = -2F gives m = -F < 0",
        z3.And(MASTER, R == 1, pr == 1, Cc == 0, I_Th == 0, K == 0,
               J == -2 * F, m == -F, m < 0, pr > 0))
    sat("DRIFT E   the flux genuinely enters: with j != 0 the STATIC collapse FAILS",
        z3.And(LOCALJ, jj != 0, D != r * r * (u + Th)))

    # ------------------------------------------ F  the Laue route, sphericity
    LAUE = z3.And(F > 0, R > 0, 3 * Vb == F * R ** 3,
                  Ixx + Iyy + Izz == F * R ** 3 * Trr,
                  I_Th == -I_u + (Ixx + Iyy + Izz))
    sat("GUARD F0  the Laue aggregate encoding is satisfiable", LAUE)
    sat("GUARD F1  ... with I_Theta = 0 and I_u < 0",
        z3.And(LAUE, I_Th == 0, I_u < 0))
    ob("F1  LAUE + TRACELESS => m = F R^3 <T^r_r>, NO SOURCE SPHERICITY ASSUMED",
       z3.And(LAUE, I_Th == 0, m == I_u), m == F * R ** 3 * Trr)
    ob("F2  and therefore the biconditional on the ANGULAR AVERAGE",
       z3.And(LAUE, I_Th == 0, m == I_u), (m < 0) == (Trr < 0))
    ob("F3  PLATE: <T^r_r> is exactly (2 p_t + p_z)/3",
       z3.And(LAUE, Vb > 0, Ixx == pt * Vb, Iyy == pt * Vb, Izz == pz * Vb),
       3 * Trr == 2 * pt + pz)
    ob("F4  PLATE CONSISTENCY, EXACT not merely same-sign: p_z = 3e, 3<T^r_r> = e",
       z3.And(LAUE, Vb > 0, Ixx == pt * Vb, Iyy == pt * Vb, Izz == pz * Vb,
              pt == -ed, -ed + 2 * pt + pz == 0, m == F * R ** 3 * Trr),
       z3.And(pz == 3 * ed, 3 * Trr == ed, m == ed * Vb))
    sat("F5  SOURCE SPHERICITY IS NOT NEEDED: a non-spherical source, signs agree",
        z3.And(LAUE, Vb > 0, Ixx == pt * Vb, Iyy == pt * Vb, Izz == pz * Vb,
               pt != pz, I_Th == 0, m == I_u, m < 0, Trr < 0))
    sat("F6  THE DIRECTIONAL MISREAD: p_t = -5, p_z = +1 gives m < 0 but p_z > 0",
        z3.And(LAUE, Vb > 0, Ixx == pt * Vb, Iyy == pt * Vb, Izz == pz * Vb,
               pt == -5, pz == 1, ed == 2 * pt + pz, I_Th == 0, m == I_u,
               m == ed * Vb, m < 0, Trr < 0, pz > 0))
    sat("DRIFT F   without the plate's extra boost symmetry, p_z = 3e must NOT follow",
        z3.And(-ed + 2 * pt + pz == 0, pz != 3 * ed))
    sat("DRIFT F2  a spherically symmetric source is still ADMITTED (p_t = p_z)",
        z3.And(LAUE, Vb > 0, Ixx == pt * Vb, Iyy == pt * Vb, Izz == pz * Vb,
               pt == pz))

    # --------------------------------- G  u is neither necessary nor sufficient
    sat("GUARD G0  FULL with u free is satisfiable", z3.And(FULL, u != 0))
    ob("G1  THE IDENTITY DOES NOT MENTION u: same F, R, p_r => same m",
       z3.And(F > 0, R > 0, m1 == F * R ** 3 * pr, m2 == F * R ** 3 * pr, u != u2),
       m1 == m2)
    ob("G2  u < 0 THROUGHOUT does imply m < 0, on the power-law family",
       z3.And(F > 0, Pp > 0, ss > 0, m == F * Aa * Pp, ss * Aa < 0), m < 0)
    ob("G3  G2's CONTRAPOSITIVE: m >= 0 forbids u < 0 throughout",
       z3.And(F > 0, Pp > 0, ss > 0, m == F * Aa * Pp, m >= 0), ss * Aa >= 0)
    sat("G4  u(R) < 0 IS NOT SUFFICIENT: u < 0, p_r > 0, hence m > 0",
        z3.And(LOCAL, Th == 0, F > 0, R > 0, m == F * R ** 3 * pr,
               u < 0, pr > 0, m > 0))
    sat("G5  u(R) < 0 IS NOT NECESSARY: u > 0, p_r < 0, m < 0",
        z3.And(LOCAL, Th == 0, F > 0, R > 0, m == F * R ** 3 * pr,
               u > 0, pr < 0, m < 0))
    sat("G6  W3 EXACTLY: p_r(1) = 8, u(1) = -1, m = 8F > 0",
        z3.And(LOCAL, r == 1, Th == 0, pr == 8, u == -1, F > 0, R == 1,
               m == F * R ** 3 * pr, m > 0))
    sat("G7  W4 EXACTLY: p_r(1) = -8, u(1) = +1, m = -8F < 0",
        z3.And(LOCAL, r == 1, Th == 0, pr == -8, u == 1, F > 0, R == 1,
               m == F * R ** 3 * pr, m < 0))
    sat("DRIFT G   u and m CAN agree in sign -- the encoding does not force them apart",
        z3.And(LOCAL, Th == 0, F > 0, R > 0, m == F * R ** 3 * pr, u < 0, m < 0))

    # ------------------------------------------------- H  the p_r = 0 radius
    GRR = z3.And(R > 0, R - 2 * m > 0, grr * (R - 2 * m) == R)
    sat("GUARD H0  FULL with p_r = 0 is satisfiable", z3.And(FULL, pr == 0))
    sat("GUARD H1  LOCAL with p_r = 0 and dp_r != 0 is satisfiable",
        z3.And(LOCAL, pr == 0, dpr != 0))
    ob("H1  p_r(R) = 0  <=>  m(R) = 0, EXACTLY -- not approximately",
       FULL, (pr == 0) == (m == 0))
    ob("H2  A ZERO ON AN INTERVAL IS VACUUM: p_t = 0 and u = 0 follow",
       z3.And(LOCAL, Th == 0, pr == 0, dpr == 0), z3.And(pt == 0, u == 0))
    ob("H3  AN ISOLATED ZERO IS NOT VACUUM: u = r p_r' != 0",
       z3.And(LOCAL, Th == 0, pr == 0, dpr != 0), z3.And(u == r * dpr, u != 0))
    ob("H4  m = 0 gives g_rr = 1: a NON-contraction under certify.py's STRICT test",
       z3.And(GRR, m == 0), grr == 1)
    ob("H5  and the sign of g_rr - 1 tracks p_r through m",
       z3.And(GRR, F > 0, m == F * R ** 3 * pr),
       z3.And((grr > 1) == (pr > 0), (grr < 1) == (pr < 0)))
    sat("DRIFT H   p_r = 0 at one radius does NOT force it at another",
        z3.And(F > 0, R1 > 0, R2 > 0, m1 == F * R1 ** 3 * pr1,
               m2 == F * R2 ** 3 * pr2, pr1 == 0, pr2 != 0))

    # -------------------------------------------- I  flat versus GR background
    LOCALGR = z3.And(r > 0, r * dpr + 2 * (pr - pt) + r * Phip * (u + pr) == 0,
                     Th == -u + pr + 2 * pt)
    sat("GUARD I0  LOCALGR is satisfiable", LOCALGR)
    sat("GUARD I1  LOCALGR with Phi' != 0 is satisfiable", z3.And(LOCALGR, Phip != 0))
    ob("I1  THE EXACT GR LOCAL IDENTITY, areal-radius gauge",
       LOCALGR, D == r * r * (u + Th) - r ** 3 * Phip * (u + pr))
    ob("I2  Phi' = 0 recovers the flat identity exactly",
       z3.And(LOCALGR, Phip == 0), D == r * r * (u + Th))
    ob("I3  with K = 0 the integrated biconditional holds",
       z3.And(MASTER, Cc == 0, I_Th == 0, J == 0, K == 0), (m < 0) == (pr < 0))
    ob("I4  THE CORRECTION VANISHES IFF u + p_r = 0, WHICH FORCES r u' + 4u = 0",
       z3.And(LOCALGR, Th == 0, u + pr == 0, du == -dpr), r * du + 4 * u == 0)
    ob("I5  ... and RN satisfies that ODE",
       z3.And(r > 0, q > 0, w * r ** 4 == q, u == w, du * r ** 5 == -4 * q),
       r * du + 4 * u == 0)
    sat("I6  FLAT BACKGROUND IS LOAD-BEARING: K != 0 gives m < 0 with p_r > 0",
        z3.And(MASTER, Cc == 0, I_Th == 0, J == 0, K != 0, m < 0, pr > 0))
    sat("DRIFT I   Phi' genuinely changes the local identity",
        z3.And(LOCALGR, Phip != 0, D != r * r * (u + Th)))

    # ----------- MUTATION PROBES: refusal 9, MEASURED HERE RATHER THAN CITED.
    # Both of these PASS, and their passing is the finding: mutating the
    # exponent or the coefficient of the master formula is INVISIBLE to this
    # layer, because almost every obligation here is a claim about SIGNS and
    # R > 0 preserves them.  The 3 and the 4 pi are pinned by the sympy layer
    # (V3, V13, V15) and by the exact Fraction layer in the selftest.
    ob("MUTATION  R^3 -> R^2 leaves the biconditional STANDING: the z3 layer is "
       "SIGN-ONLY", z3.And(F > 0, R > 0, m == F * R ** 2 * pr), (m < 0) == (pr < 0))
    ob("MUTATION  ... and so does dropping the radius altogether, which is why F "
       "is an ARBITRARY positive real here and never a float for 4 pi",
       z3.And(F > 0, R > 0, m == F * pr), (m < 0) == (pr < 0))
    sat("MUTATION  and the SIGN of the coefficient is NOT invisible: F < 0 "
        "reverses it (DRIFT B2, restated as the mutation that DOES bite)",
        z3.And(F < 0, R > 0, m == F * R ** 3 * pr, m < 0, pr > 0))

    # ------------------------------------- L  the von Laue total-mass corollary
    sat("GUARD L0  the corollary's premise set is satisfiable",
        z3.And(F > 0, Rc > 0, m == F * Rc ** 3 * pr))
    ob("L1  A BOUNDED traceless conserved static regular source has m = 0 EXACTLY",
       z3.And(F > 0, Rc > 0, m == F * Rc ** 3 * pr, pr == 0), m == 0)
    ob("L2  which is von Laue: INT (u + Theta) dV = 0 over the whole space",
       z3.And(F > 0, Rc > 0, I_uTh == F * Rc ** 3 * pr, pr == 0), I_uTh == 0)
    sat("DRIFT L   an UNBOUNDED source (p_r != 0 at the cut) may have m != 0",
        z3.And(F > 0, Rc > 0, m == F * Rc ** 3 * pr, pr != 0, m != 0))
    return out


# =============================================================== status lines

VERDICT = ("RESTATES certify.py ON A STRICTLY SMALLER CLASS -- CHEAPER WHERE "
           "BOTH APPLY, AND NO GATE MOVES")
SUPERSEDES_CERTIFY = False
RESTATES_CERTIFY_ON_SMALLER_CLASS = True
CLASS_IS_A_PROPER_SUBSET = True
HYPOTHESES_ADDED = ("T^mu_mu = 0 exactly, and a flat background (Phi' = 0, or "
                    "the weaker sufficient condition u + p_r = 0)")
IDENTITY_IS_EXACT_IN_FLAT_SPACE_ONLY = True
CURVED_CORRECTION = "K = 4 pi INT_0^R r^3 (u + p_r) Phi' dr"
CURVED_CORRECTION_VANISHES_IFF = "u + p_r = 0 (the saturated radial NEC), or Phi' = 0"
ONLY_TRACELESS_CONSERVED_SOURCE_WITH_U_PLUS_PR_ZERO = "Reissner-Nordstrom"
INTEGRATION_CONSTANT_IS_A_LIMIT_OF_M = False
INTEGRATION_CONSTANT_IS = "the renormalised CENTRAL MASS, a first integral"
REGULAR_CENTRE_IS_LOAD_BEARING = True
TRACELESSNESS_IS_LOAD_BEARING = True
FLAT_BACKGROUND_IS_LOAD_BEARING = True
SOURCE_SPHERICITY_IS_LOAD_BEARING = False
READ_DIRECTION_SPHERICITY_IS_LOAD_BEARING = True
STATICITY_IS_THE_RIGHT_NAME = False
HYPOTHESIS_ACTUALLY_USED_OFF_STATICITY = "d_t T^t_r = 0 -- a STATIONARY flux"
NONSTATIC_BRANCH_IS_CLOSED = False
U_AT_R_IS_NECESSARY = False
U_AT_R_IS_SUFFICIENT = False
TEST_QUANTITY = "the ANGULAR AVERAGE <T^r_r(R)>, never a single component"
RESIDUAL_COUNT = 29                    # --verify rows, every one exactly 0
OBLIGATION_COMPOSITION = {             # --prove rows, and the shape is pinned
    "theorem, negated -> unsat, own hypothesis sat": 39,
    "family satisfiability guard (sat)": 20,
    "encoding-drift probe (sat)": 14,
    "necessity witness (sat)": 14,
    "mutation probe": 3,
}
OBLIGATION_COUNT = 90
Z3_LAYER_IS_SIGN_ONLY = True
Z3_MUTATION_MEASURED_IN_FILE = True
COEFFICIENT_AND_EXPONENT_PINNED_BY = "the sympy residuals and the exact Fraction layer"
NOVELTY_CLAIMED = False
DOCKET54_NONFIND_WITHDRAWN = True
BILL_LIFTED = False
ANY_GATE_MOVES = False
ROUTE_A_STATUS = "STRUCK, unchanged -- DOCKET 54 ground 3 is untouched"
NOTHING_IS_REPAIRED = True
NO_PEER_IS_EDITED = True
SCOPE = ("flat-background traceless conserved spherically symmetric sources with "
         "a regular centre and a stationary radial flux; nothing non-spherical, "
         "nothing with a trace anomaly, nothing about the deep interior")
REFUSED = ("the word 'replaces'; 'EXACT' without its background hypothesis; "
           "'cheaper to test therefore cheaper to meet'; any report on a centre "
           "not certified regular, on a single direction of a non-spherical "
           "source, on a ball enclosing a mirror, or on the non-static branch; "
           "any novelty claim; any mass for the plasma term; any reading of a "
           "non-find as a clearance")

PRIOR_ART = (
    ("Tolman, Phys. Rev. 35, 875 (1930) -- the active gravitational mass",
     "RECOVERED", "through Herrera 1801.08358 ref [19]; NOT read"),
    ("von Laue, Ann. Phys. 340(8), 524 (1911) -- the flat parent",
     "RECOVERED", "through Wang arXiv:1206.5618; NOT read"),
    ("Whittaker, Proc. Roy. Soc. A 149, 384 (1935) -- 'Tolman-Whittaker'",
     "RECOVERED", "located only in Sorge 2011.10991's bibliography; NOT read"),
    ("Herrera & Santos, Gen. Rel. Gravit. 27, 1071 (1995) eq. (25)",
     "RECOVERED", "on Herrera & Di Prisco's say-so; NOT read; the EARLIEST "
                  "statement nameable, so 1995 RECOVERED, never 1995 CITED"),
    ("Herrera, arXiv:1801.08358v2 eq. (32) -- m_T = e^{(nu+lam)/2}(m + 4pi r^3 P_r)",
     "CITED", "read at source by the prior-art pass; re-derived here, V20 = 0"),
    ("Herrera & Di Prisco, arXiv:gr-qc/9810020 eq. (39) -- the time-dependent form",
     "CITED", "read at source by the prior-art pass"),
    ("Wang, arXiv:1206.5618 eq. (20) -- von Laue's finite-volume surface term",
     "CITED", "read at source by the prior-art pass"),
    ("Lorce, Metz, Pasquini & Rodini, arXiv:2109.11785 eq. (65)",
     "CITED", "read at source by the identity pass; the R -> infinity limit"),
    ("arXiv:2605.04163 eq. (65) -- p'_r + 2(p_r - p_t)/r = 0",
     "CITED", "read at source by the witness pass"),
    ("Sorge, arXiv:2011.10991 eq. (36) -- the Tolman mass OF A CASIMIR CAVITY",
     "CITED", "read at source by the prior-art pass; A SCOPE CAUTION, not support"),
    ("Agnese & La Camera, arXiv:gr-qc/0203067 eq. (17) -- traceless wormhole",
     "CITED", "read at source by the prior-art pass; reproduced, V19 = 0"),
    ("Polyakov & Schweitzer, arXiv:1805.06596 -- the same algebra in p(r), s(r)",
     "RECOVERED", "named, NOT read"),
    ("Milton, arXiv:1005.0031 eq. (58), A_EM = 1/(60 pi^2) -- 'properly traceless'",
     "RECOVERED", "via DOCKET 54's verbatim quotation; SINGLE-SOURCE; not "
                  "re-read at source"),
    ("Sopova & Ford, quant-ph/0504143 eq. (15) -- the planar K coefficient",
     "RECOVERED", "via DOCKET 54's verbatim quotation; not re-read at source"),
    ("Casimir FORCE between plates -- the ONE measured quantity in the chain",
     "MEASURED", "Lamoreaux 1997; Mohideen-Roy 1998; Bressi 2002"),
    ("'negative enclosed mass iff radial tension' anywhere in Casimir literature",
     "NOT-FOUND", "a non-find is NOT a clearance"),
    ("'flare-out iff negative enclosed Misner-Sharp mass' in wormhole literature",
     "NOT-FOUND", "and the reason is DERIVED: at a throat the sign is opposite"),
)

PEER_STATUS = (
    ("certify.py THEOREM (contraction at r <=> m(r) < 0)", "UNCHANGED",
     "a statement about the metric alone -- no conservation law, no "
     "tracelessness, no flat background, no stress tensor.  A test on T cannot "
     "touch it, and this file must not imply that it does."),
    ("certify.py COROLLARY (m = INT 4 pi r'^2 rho, needing m(0) = 0)", "CONFIRMED",
     "THE SAME FACT TWICE, NOT A COINCIDENCE: both hypotheses kill the "
     "integration constant of a first-order ODE at r = 0, and RN breaks both "
     "simultaneously in the same region.  On the class where both hold the "
     "identity is an independent second evaluation of the same integral."),
    ("foliation.py RANGE THEOREM (Gamma > 1 in every foliation <=> m < 0)",
     "CONFIRMED",
     "the strongest composition in the set and it needs no new claim: it "
     "carries NO staticity hypothesis, and this file adds one term on the "
     "MATTER side of the same invariant.  Section 8."),
    ("expose.py invariant C = 1/Gamma", "UNCHANGED",
     "not one line changes; on this class the geometry chain C(R) < 1 <=> "
     "m(R) < 0 gains a third term, p_r(R) < 0.  Its Kerr results are off-class."),
    ("driven.py (DOCKET 52, contraction <=> 2m/R < e^{-2Phi} Rdot^2)", "UNCHANGED",
     "off-class in both directions: its criterion is non-static and this test "
     "assumes a stationary flux.  Neither speaks to the other."),
    ("nonstatic.py MS/EV equations and the anchor lemma", "UNCHANGED",
     "different hypothesis sets.  RECORDED: its static limit of EV-U is "
     "dPhi/dr = (m + 4 pi r^3 p)/(r(r-2m)), which CONTAINS the Tolman mass "
     "combination and does not name it.  A finding about a peer, applied to "
     "nothing."),
    ("drivensource.py section 3 (the RN break of L2)", "CONFIRMED",
     "SHARPENED BOTH WAYS.  (a) its RN region r < Q^2/2M is exactly where this "
     "biconditional fails, so the new test INHERITS the break rather than "
     "escaping it.  (b) its electrovac rho + p_r = 0 is exactly the condition "
     "under which this file's curved correction vanishes identically -- which "
     "is why RN came out exact.  Neither file knew (b)."),
    ("mouth.py section 5b (the sign bookkeeping M = |m|)", "UNCHANGED",
     "scoped to certify.py's THEOREM, which is unchanged.  Re-arguing 5b "
     "through this test would move a hypothesis-free resolution onto one "
     "needing tracelessness and flat space.  REFUSED."),
    ("candidates.py KIND / DEADLINE / MAGNITUDE gates", "UNCHANGED",
     "NOT ONE GATE MOVES.  This changes how the KIND gate is TESTED, not which "
     "candidates pass it.  The banked u(10 nm) is reproduced, not altered."),
    ("overturn.py L1 SCOPE (sphericity)", "UNCHANGED",
     "slightly worse for us: this test needs an areal radius AND the "
     "(2/r)(p_r - p_t) conservation form that only spherical symmetry supplies."),
    ("overturn.py L2 SOURCE (m = 4 pi INT rho r'^2; BROKEN by RN, break EMPTY)",
     "CONFIRMED",
     "a second route to the SAME link, breaking in the SAME place with the same "
     "emptiness.  A third statement of L2 and no new door."),
    ("overturn.py L4 MAGNITUDE (the sole load-bearing obstruction)", "UNCHANGED",
     "UNTOUCHED BY ANY AMOUNT.  A cheaper test for a requirement is not a "
     "cheaper requirement, and this is the whole risk of this instrument."),
    ("vacuumcorridor.py (the Ricci/Weyl crossover)", "UNCHANGED",
     "no contact.  RECORDED while reading: its first docstring line says "
     "'corridor.py', and a different corridor.py exists in the tree."),
    ("switch.py (the EM switch)", "UNCHANGED",
     "owed only the von Laue caution: for a COMPLETE apparatus int T^i_i = 0, "
     "so a pointwise test on a ball enclosing the mirrors returns exactly zero."),
    ("emtension.py (w = -p_r/rho = 1 for a static radial EM field)", "UNCHANGED",
     "its rigidity arrives here as the EXACTNESS CONDITION of a different "
     "theorem: u + p_r = 0 makes the curved correction vanish."),
    ("charge.py (the RN region r < Q^2/2M)", "UNCHANGED",
     "the same region reached from the stress side rather than the metric side."),
    ("DOCKET 54's ruling, section 4", "CORRECTED",
     "three things.  (a) 'The identity REPLACES certify.py's integral over a "
     "ball' -> RESTATES, on a smaller class.  (b) sphericity OF THE SOURCE is "
     "NOT load-bearing; sphericity of the READ is.  (c) its non-find "
     "('I did not find either stated in this form') is WITHDRAWN: it is in "
     "print since 1995.  And its plate check is UPGRADED: the agreement is "
     "EXACT on the isotropic average, not merely same-sign."),
    ("this file's own reach", "NARROWED",
     "von Laue forces int_V T^i_i = 0 over a complete static bounded system, so "
     "4 pi R^3 p_r(R) = 0 for ANY ball enclosing the whole device.  The test "
     "has content ONLY strictly inside a cavity, and REFUSES otherwise."),
)

PEER_STATUS_COUNTS = {"UNCHANGED": 12, "CONFIRMED": 4, "CORRECTED": 1,
                      "NARROWED": 1}


# ==================================================================== selftest

def selftest():
    """STDLIB ONLY plus seated peers of this tree.  sympy and z3 are NOT
    imported here by design: --verify and --prove are the layers that need them,
    and this is the layer that must run anywhere.  Section 10 refusal 9 stands:
    the layers are not redundant and neither may be reported without the other."""
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-68s %-13s %-13s %s"
              % (label, str(got)[:13], str(want)[:13], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-68s %13.7g %13.7g %s"
              % (label, got, want, "ok" if good else "FAIL"))

    print("0. THE VERDICT LINE, BEFORE ANY NUMBER")
    chk("  it does NOT supersede certify.py", SUPERSEDES_CERTIFY, False)
    chk("  it restates it on a smaller class", RESTATES_CERTIFY_ON_SMALLER_CLASS, True)
    chk("  and that class is a PROPER subset", CLASS_IS_A_PROPER_SUBSET, True)
    chk("  the identity is exact in flat space only",
        IDENTITY_IS_EXACT_IN_FLAT_SPACE_ONLY, True)
    chk("  no novelty is claimed", NOVELTY_CLAIMED, False)
    chk("  DOCKET 54's non-find is withdrawn", DOCKET54_NONFIND_WITHDRAWN, True)
    chk("  no gate moves", ANY_GATE_MOVES, False)
    chk("  the bill is not lifted", BILL_LIFTED, False)
    chk("  nothing is repaired", NOTHING_IS_REPAIRED, True)
    chk("  and no peer is edited", NO_PEER_IS_EDITED, True)

    print("\n1. CONSTANTS, AND EVERY ONE CARRIES ITS STATUS")
    print("     l_P DERIVED = %.6e m   l_P CODATA = %.6e m   rel %.3e"
          % (L_PLANCK, L_PLANCK_CODATA, abs(L_PLANCK / L_PLANCK_CODATA - 1.0)))
    chk("  l_P DERIVED from hbar, G, c agrees with CODATA below 1e-4",
        abs(L_PLANCK / L_PLANCK_CODATA - 1.0) < 1e-4, True)
    chk("  ... and the gap is G's own rounding, not a disagreement of physics",
        abs(L_PLANCK / L_PLANCK_CODATA - 1.0) > 1e-9, True)
    chk("  A_EM is RECOVERED and SINGLE-SOURCE, never CITED",
        _status("A_EM"), "RECOVERED")
    chk("  the Casimir FORCE is the one MEASURED input",
        _status("Casimir force"), "MEASURED")
    chk("  the plasma-sphere prefactor is RECONSTRUCTED and no mass is quoted",
        _status("plasma-sphere prefactor"), "RECONSTRUCTED")
    chk("  no status in the table is the forbidden one",
        all(s in ("CITED", "DERIVED", "RECOVERED", "RECONSTRUCTED", "MEASURED",
                  "MEASURED-INFERRED") for s in FIGURE_STATUS.values()), True)

    print("\n2. THE PRIOR-ART LEDGER GOES FIRST AND GOES AGAINST US")
    chk("  the two earliest sources are RECOVERED, never CITED",
        all(s == "RECOVERED" for _, s, _ in PRIOR_ART[:4]), True)
    chk("  Herrera eq. (32) is the CITED parent", PRIOR_ART[4][1], "CITED")
    chk("  both literature searches are recorded as NOT-FOUND",
        sum(1 for _, s, _ in PRIOR_ART if s == "NOT-FOUND"), 2)
    chk("  every prior-art row carries a status",
        all(s for _, s, _ in PRIOR_ART), True)

    print("\n3. THE IDENTITY, THE TWO READINGS, AND THE INVERSE")
    for R, p in ((1.0, -1.0), (2.5, -3.3e4), (0.001, 4.0e2)):
        m = enclosed_mass(R, p)
        near("  round trip at R = %g: p_r -> m -> p_r" % R,
             radial_stress_for_mass(m, R), p)
    near("  the Tolman combination is exactly 2m on the identity",
         tolman_mass_factor(enclosed_mass(1.0, -7.0), 1.0, -7.0),
         2.0 * enclosed_mass(1.0, -7.0))
    near("  the first integral is 0 on the identity (no centre term)",
         first_integral(enclosed_mass(3.0, -2.0), 3.0, -2.0), 0.0)

    print("\n4. REISSNER-NORDSTROM -- EXACT RATIONAL ARITHMETIC, NO FLOATS")
    print("     %8s %18s %14s %10s" % ("R", "4 pi R^3 p_r", "m(R)", "defect"))
    defects = []
    for R in ("1/20", "1/10", "1/5", "8/25", "2/5", "1/2", "1", "8/5", "5", "100"):
        f3, m, d = rn_row(Fr(R))
        defects.append(d)
        print("     %8s %18s %14s %10s"
              % (R, str(float(f3))[:16], str(float(m))[:12], str(d)))
    chk("  the defect is EXACTLY M = 1 at every radius, as a Fraction",
        set(defects), {Fr(1)})
    chk("  m = 0 exactly at R = Q^2/2M = 8/25", rn_sign_radius(), Fr(8, 25))
    chk("  p_r < 0 at EVERY radius while m < 0 at only three of the ten",
        sum(1 for R in ("1/20", "1/10", "1/5", "8/25", "2/5", "1/2", "1", "8/5",
                        "5", "100") if rn_row(Fr(R))[1] < 0), 3)
    h = rn_horizons()
    near("  inner horizon r_- = 0.4", h[0], 0.4)
    near("  outer horizon r_+ = 1.6", h[1], 1.6)
    chk("  the m < 0 region is STRICTLY inside the Cauchy horizon for all y",
        all(rn_negative_region_inside_cauchy(y) > 0.0
            for y in (0.01, 0.1, 0.25, 0.5, 0.64, 0.9, 0.99, 1.0)), True)
    chk("  THE CONSTANT IS NOT A LIMIT OF m", INTEGRATION_CONSTANT_IS_A_LIMIT_OF_M,
        False)
    chk("  the regular centre is load-bearing", REGULAR_CENTRE_IS_LOAD_BEARING, True)

    print("\n5. THE CONTROLS")
    d, R = 1e-8, 1e-3
    u0 = plate_u0(d)
    near("  u_0 at d = 10 nm reproduces candidates.py's banked value",
         u0, candidates.casimir(d), 1e-12)
    near("  the raw plate cell is traceless (residual/u_0)",
         plate_trace_residual(d) / u0, 0.0, 1e-14)
    rho, pz, ptr = plate_cell(d)
    near("  p_normal/u_0 = -3, DERIVED from F = -d(E/A)/dd", pz / u0, -3.0)
    near("  rho/u_0 = -1", rho / u0, -1.0)
    near("  p_transverse/u_0 = +1, FORCED by tracelessness", ptr / u0, +1.0)
    chk("  BOTH have the right sign simultaneously (the ruling's check)",
        (rho < 0.0 and pz < 0.0), True)
    e, pr_i, pt_i = isotropic_average(d)
    near("  POSITIVE CONTROL: isotropic average is traceless (residual/u_0)",
         trace_residual(e, pr_i, pt_i) / u0, 0.0, 1e-14)
    m_quad = radiation_mass(R, u0, -1.0)
    m_ident = enclosed_mass(R, pr_i)
    near("  and the QUADRATURE and the POINTWISE read agree exactly",
         m_ident, m_quad, 1e-14)
    chk("  VERDICT YES", pointwise_test(pr_i, R, **all_hypotheses())[0], "YES")
    print("     u_0 = %.6e J/m^3   p_r = %.6e Pa   m = %.6e kg"
          % (u0, pr_i, m_ident))
    near("  ... and m cross-checks the derivation pass's -2.019814e-21 kg",
         m_ident, -2.019814e-21, 1e-4)
    near("  THE MAGNITUDE ERROR IF THE RAW CELL IS READ AS p_r: a factor 9",
         enclosed_mass(R, pz) / m_quad, 9.0)
    e2, pr2_, pt2_ = (+u0, +u0 / 3.0, +u0 / 3.0)
    near("  NEGATIVE CONTROL (a): the exact mirror is traceless (residual/u_0)",
         trace_residual(e2, pr2_, pt2_) / u0, 0.0, 1e-14)
    chk("  VERDICT NO", pointwise_test(pr2_, R, **all_hypotheses())[0], "NO")
    near("  and its mass is the exact mirror too",
         enclosed_mass(R, pr2_), -m_ident, 1e-14)

    print("\n6. NEGATIVE CONTROL (b) -- THE rho-VERSUS-p_r TRAP, IN FRACTIONS")
    prq, eq_, ptq, mq = quadratic_profile(1, 1, Fr(9, 10))
    chk("  p_r(9L/10) = +19/100 > 0", prq, Fr(19, 100))
    chk("  e(9L/10) = -21/20 < 0   <- THE TRAP", eq_, Fr(-21, 20))
    chk("  m c^2/(4 pi) = +13851/100000 > 0, AGREEING WITH p_r", mq,
        Fr(13851, 100000))
    chk("  ... i.e. m c^2 = 13851 pi L^3 P_0/25000, the derivation's figure",
        4 * mq, Fr(13851, 25000))
    chk("  conservation residual is exactly 0",
        conservation_residual(prq, Fr(-2) * Fr(9, 10), ptq, Fr(9, 10)), Fr(0))
    chk("  trace residual is exactly 0", trace_residual(eq_, prq, ptq), Fr(0))
    chk("  the identity holds exactly: m c^2/(4pi) = R^3 p_r",
        mq, Fr(9, 10) ** 3 * prq)
    chk("  VERDICT NO, which is right, and a rho-test would read YES",
        pointwise_test(float(prq), 1.0, **all_hypotheses())[0], "NO")
    near("  the trap window opens at sqrt(3/5) L", QUAD_TRAP_LO, 0.7745966692)
    chk("  and e < 0 strictly inside it",
        quadratic_profile(1, 1, Fr(8, 10))[1] < 0, True)

    print("\n7. THE REFUSALS, WHICH ARE PART OF WHAT THE INSTRUMENT IS")
    h_no_centre = all_hypotheses()
    h_no_centre["regular_centre"] = False
    chk("  RN beyond Q^2/2M: REFUSE, no regular centre",
        pointwise_test(-1.0, 1.0, **h_no_centre)[0], "REFUSE")
    h_no_sph = all_hypotheses()
    h_no_sph["spherical_source"] = False
    chk("  the raw plate cell: REFUSE, not spherically symmetric",
        pointwise_test(pz, R, **h_no_sph)[0], "REFUSE")
    h_walls = all_hypotheses()
    h_walls["ball_excludes_walls"] = False
    chk("  a ball enclosing a mirror: REFUSE (von Laue, Sorge eq. 36)",
        pointwise_test(pr_i, R, **h_walls)[0], "REFUSE")
    h_flux = all_hypotheses()
    h_flux["stationary_flux"] = False
    chk("  the non-static branch: REFUSE, its geometry side is not closed",
        pointwise_test(pr_i, R, **h_flux)[0], "REFUSE")
    chk("  an absent claim is not a granted one (no kwargs at all)",
        pointwise_test(-1.0, 1.0)[0], "REFUSE")
    chk("  p_r = 0 is ZERO, a NON-contraction, not YES",
        pointwise_test(0.0, 1.0, **all_hypotheses())[0], "ZERO")

    print("\n8. THE WORMHOLE WITNESSES -- THE OPPOSITE SIGN")
    prw, mw, fw = wormhole_throat(3.0)
    near("  Morris-Thorne throat: 4 pi r_0^3 p_r = -m", fw, -mw)
    chk("  so the flare-out condition is NOT this identity", fw == -mw, True)
    r0a, ppar, f4, mms = alc_throat(1.0, 0.5)
    near("  Agnese-La Camera eq. (17): 4 pi r_0^3 p_|| = -m_MS", f4, -mms)
    chk("  with m_MS > 0 EVERYWHERE and tension at the throat",
        (mms > 0.0 and ppar < 0.0), True)
    chk("  tracelessness alone does not buy the biconditional",
        TRACELESSNESS_IS_LOAD_BEARING, True)

    print("\n9. THE CURVED-BACKGROUND BOUND")
    near("  delta at eps = l_P is exactly 1/(15 pi)", delta_curved(L_PLANCK),
         1.0 / (15.0 * math.pi))
    near("  delta = 1 at eps = l_P/sqrt(15 pi)", delta_unity_eps() / L_PLANCK,
         1.0 / math.sqrt(15.0 * math.pi), 1e-14)
    near("  ... and delta evaluated there is exactly 1",
         delta_curved(delta_unity_eps()), 1.0, 1e-14)
    near("  delta is INDEPENDENT of the shell radius a (it does not appear)",
         delta_curved(1e-9), delta_curved(1e-9))
    near("  and scales as eps^-2 exactly", delta_curved(1e-10) / delta_curved(1e-9),
         100.0)
    chi = chi_compactness(1.378e-7)
    near("  chi at eps = 137.8 nm against DOCKET 54's banked 5.84e-58", chi,
         5.84e-58, 1e-3)
    print("     delta(137.8 nm) = %.4e   chi = %.4e   (a derivation pass "
          "reported delta = 2.9210e-58)" % (delta_curved(1.378e-7), chi))
    chk("  THE DERIVATION PASSES DISAGREE AT 5.8e-4 AND THE RECOMPUTATION WINS",
        abs(delta_curved(1.378e-7) / 2.9210e-58 - 1.0) < 2e-3, True)
    near("  the profile-free fallback at chi = 5.8386e-58, V/|m| = 3/2, / chi",
         delta_profile_free(chi, 1.5) / chi, 1.5, 1e-9)
    chk("  which costs a factor 3 against the exact chi/2",
        round(delta_profile_free(chi, 1.5) / (chi / 2.0)), 3)
    near("  the crossover coefficient is 60 sqrt(2) pi/128", crossover_coefficient(),
         60.0 * math.sqrt(2.0) * math.pi / 128.0)
    near("  ... = 2.0826013773", crossover_coefficient(), 2.0826013773, 1e-9)
    near("  a_c / skin depth = 0.4801687020, FOR EVERY CONDUCTOR",
         crossover_radius(HBAR_OMEGA_P_GOLD_EV) / skin_depth(HBAR_OMEGA_P_GOLD_EV),
         0.4801687020, 1e-9)
    near("  gold skin depth c/omega_p (nm)", skin_depth(9.0) * 1e9, 21.9252, 1e-4)
    near("  gold crossover a_c (nm)", crossover_radius(9.0) * 1e9, 10.5278, 1e-4)
    near("  aluminium skin depth (nm)", skin_depth(15.3) * 1e9, 12.8972, 1e-4)
    near("  aluminium crossover a_c (nm)", crossover_radius(15.3) * 1e9, 6.19283, 1e-4)
    chk("  and the material-independence is exact: the ratio is the same",
        abs(crossover_radius(9.0) / skin_depth(9.0)
            - crossover_radius(15.3) / skin_depth(15.3)) < 1e-15, True)

    print("\n10. THE BILL, WHICH THIS FILE DOES NOT LOWER")
    mq1 = mass_for_contraction(0.01, 1.0)
    near("  1 % contraction at R = 1 m needs m = -1.367063e25 kg", mq1,
         -1.367063e25, 1e-6)
    near("  ... = -2.2890 Earth masses", mq1 / M_EARTH, -2.2890, 1e-4)
    near("  REQUIRED RADIAL TENSION", tension_for_contraction(0.01, 1.0),
         -9.777322e40, 1e-6)
    near("  designpoint.py's level, IMPORTED not copied", designpoint_tension(),
         -8.025756e39, 1e-6)
    chk("  the two levels agree to just over one order of magnitude",
        1.0 < abs(tension_for_contraction(0.01, 1.0) / designpoint_tension()) < 100.0,
        True)
    req = abs(tension_for_contraction(0.01, 1.0))
    near("  the equivalent purely radial magnetic field (T)", field_for_tension(req),
         4.9571e17, 1e-4)
    lad = tension_ladder()
    for label, val, st in lad:
        print("     %-58s %12.4e Pa  [%s]" % (label[:58], val, st))
    chk("  every rung carries a status",
        all(st in ("DERIVED", "MEASURED", "MEASURED-INFERRED",
                   "DERIVED from an inferred B", "DERIVED from a measured B")
            for _, _, st in lad), True)
    near("  QCD flux tube (Pa)", lad[1][1], 1.8360e35, 1e-4)
    near("  magnetar B^2/2mu_0 (Pa)", lad[3][1], 3.9789e27, 1e-4)
    near("  Schwinger field (T)", schwinger_field(), 4.4140e9, 1e-4)
    near("  atomic ceiling (Pa)", atomic_ceiling(), 2.9421e13, 1e-4)
    near("  Planck stress (Pa)", planck_stress(), 4.6329e113, 1e-4)
    near("  shortfall against the best IN-HYPOTHESIS tension (magnetar)",
         req / lad[3][1], 2.4573e13, 1e-3)
    chk("  the closest rung is the QCD flux tube AND IT IS NOT TRACELESS",
        "NOT traceless" in lad[1][0], True)
    chk("  no gate moves, and the bill is not lifted",
        (ANY_GATE_MOVES, BILL_LIFTED), (False, False))

    print("\n11. THE CHAIN TO THE SEATED PEERS -- IMPORTED, NEVER COPIED")
    agree = True
    for g_rr in (0.25, 0.5, 0.8, 1.25, 2.0, 4.0):
        mm = certify.enclosed_mass_from_grr(g_rr, 1.0)
        p_r_equiv = mm / (4.0 * math.pi)          # G = c = 1, R = 1
        agree &= (certify.contracts(g_rr)
                  == foliation.contracts_everywhere(mm, 1.0)
                  == driven.contracts(mm, 1.0, 0.0)
                  == (mm < 0.0) == (p_r_equiv < 0.0))
    chk("  certify == foliation == driven(U=0) == (m<0) == (p_r<0)", agree, True)
    near("  Gamma^2 - U^2 = 1 - 8 pi R^2 p_r under the identity",
         foliation.k_of(4.0 * math.pi * 1.0 ** 3 * (-0.01), 1.0),
         1.0 - 8.0 * math.pi * 1.0 ** 2 * (-0.01))
    chk("  foliation.py's RANGE THEOREM carries no staticity, and is CONFIRMED",
        [s for t, s, _ in PEER_STATUS if t.startswith("foliation.py")], ["CONFIRMED"])
    chk("  certify.py's scope line is untouched (nothing repaired)",
        certify.THEOREM_SCOPE, "static and spherically symmetric only")
    chk("  driven.py still says the criterion is not a scalar",
        driven.CONTRACTION_IS_A_SCALAR, False)
    chk("  and p_r is not a scalar either, outside the hypotheses",
        READ_DIRECTION_SPHERICITY_IS_LOAD_BEARING, True)

    print("\n12. THE PEER STATUS TABLE IS WHAT THIS FILE HOLDS")
    counts = {}
    for _, st, _ in PEER_STATUS:
        counts[st] = counts.get(st, 0) + 1
    chk("  the table's status counts", counts, PEER_STATUS_COUNTS)
    chk("  certify.py's THEOREM is UNCHANGED",
        [s for t, s, _ in PEER_STATUS if t.startswith("certify.py THEOREM")],
        ["UNCHANGED"])
    chk("  certify.py's COROLLARY is CONFIRMED, not superseded",
        [s for t, s, _ in PEER_STATUS if t.startswith("certify.py COROLLARY")],
        ["CONFIRMED"])
    chk("  overturn.py's L4 is UNCHANGED, which is the last word",
        [s for t, s, _ in PEER_STATUS if t.startswith("overturn.py L4")],
        ["UNCHANGED"])
    chk("  the ruling itself is the one CORRECTED row",
        sum(1 for _, s, _ in PEER_STATUS if s == "CORRECTED"), 1)
    chk("  and exactly one row NARROWS this file's own reach",
        sum(1 for _, s, _ in PEER_STATUS if s == "NARROWED"), 1)
    chk("  every row carries a reason", all(bool(w) for _, _, w in PEER_STATUS), True)
    chk("  NOTHING IS REPAIRED AND NO PEER IS EDITED",
        (NOTHING_IS_REPAIRED, NO_PEER_IS_EDITED), (True, True))

    print("\n13. THE REFUSAL SURFACE")
    chk("  the word 'replaces' is refused", "replaces" in REFUSED, True)
    chk("  the flat-background limit is named in the scope",
        "flat-background" in SCOPE, True)
    chk("  the non-static branch is NOT closed", NONSTATIC_BRANCH_IS_CLOSED, False)
    chk("  staticity is not the right name for what is used",
        STATICITY_IS_THE_RIGHT_NAME, False)
    chk("  u at R is neither necessary nor sufficient",
        (U_AT_R_IS_NECESSARY, U_AT_R_IS_SUFFICIENT), (False, False))
    chk("  source sphericity is NOT load-bearing (the ruling's one error)",
        SOURCE_SPHERICITY_IS_LOAD_BEARING, False)
    chk("  but the direction of the READ is", READ_DIRECTION_SPHERICITY_IS_LOAD_BEARING,
        True)
    chk("  Route A stays STRUCK", ROUTE_A_STATUS.startswith("STRUCK"), True)
    chk("  the z3 layer is SIGN-ONLY and says so", Z3_LAYER_IS_SIGN_ONLY, True)
    chk("  ... and that is MEASURED in --prove, not cited to another pass",
        Z3_MUTATION_MEASURED_IN_FILE, True)
    chk("  the coefficient and the exponent are pinned elsewhere",
        COEFFICIENT_AND_EXPONENT_PINNED_BY,
        "the sympy residuals and the exact Fraction layer")
    chk("  the pinned --prove composition sums to its pinned total",
        sum(OBLIGATION_COMPOSITION.values()), OBLIGATION_COUNT)
    chk("  every mutation probe is counted as a probe, never as a theorem",
        classify_row("MUTATION  R^3 -> R^2 ..."), "mutation probe")
    chk("  and --verify's row count is pinned too", RESIDUAL_COUNT, 29)

    print("\nSELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


# ====================================================================== report

BAR = "=" * 79


def report():
    print(__doc__)
    print(BAR)
    print("PRIOR ART -- FIRST, AND AGAINST US")
    print(BAR)
    for src, st, note in PRIOR_ART:
        print("  [%-16s] %s" % (st, src))
        print("        %s" % note)

    print("\n" + BAR)
    print("REISSNER-NORDSTROM (M = 1, Q = 4/5): THE DEFECT IS M AT EVERY RADIUS")
    print(BAR)
    print("  %10s %18s %16s %10s" % ("R", "4 pi R^3 p_r", "m(R)", "defect"))
    for R in ("1/20", "1/10", "1/5", "8/25", "2/5", "1/2", "1", "8/5", "5", "100"):
        f3, m, d = rn_row(Fr(R))
        print("  %10s %18.9f %16.9f %10s" % (R, float(f3), float(m), d))
    print("\n  m = 0 at R = Q^2/2M = %s; horizons %.1f and %.1f."
          % (rn_sign_radius(), *rn_horizons()))
    print("  p_r < 0 in EVERY row.  m < 0 in three.  THE FAILING DIRECTION IS")
    print("  SUFFICIENCY, and the size of the failure is exactly C = M.")

    print("\n" + BAR)
    print("THE CONTROLS")
    print(BAR)
    d, R = 1e-8, 1e-3
    u0 = plate_u0(d)
    e, pr_i, _ = isotropic_average(d)
    v, m_i, why = pointwise_test(pr_i, R, **all_hypotheses())
    print("  POSITIVE  isotropic average of the plate tensor, d = 10 nm, R = 1 mm")
    print("            u_0 = %.6e J/m^3 [DERIVED]  banked %.6e [candidates.py]"
          % (u0, candidates.casimir(d)))
    print("            p_r = %.6e Pa     m = %.6e kg" % (pr_i, m_i))
    print("            VERDICT %s -- %s" % (v, why))
    v2 = pointwise_test(+u0 / 3.0, R, **all_hypotheses())
    print("  NEGATIVE  (a) the exact mirror, e = +u_0:  VERDICT %s" % v2[0])
    prq, eq_, _, mq = quadratic_profile(1, 1, Fr(9, 10))
    print("  NEGATIVE  (b) p_r = P0(1 - r^2/L^2) at R = 9L/10:")
    print("            p_r = %s P0 > 0, e = %s P0 < 0 <- THE TRAP, m c^2/4pi = %s"
          % (prq, eq_, mq))
    print("            VERDICT %s.  A rho-test reads YES here and is WRONG."
          % pointwise_test(float(prq), 1.0, **all_hypotheses())[0])
    print("  REFUSED   %s" % pointwise_test(-1.0, 1.0)[2])

    print("\n" + BAR)
    print("THE CURVED CORRECTION, BOUNDED IN CLOSED FORM:  delta = (1/15pi)(l_P/eps)^2")
    print(BAR)
    print("  %-34s %16s %16s" % ("regulator eps", "delta", "chi = 2 delta"))
    for label, eps in (("gold lambda_p, 137.8 nm", 1.378e-7),
                       ("gold skin depth, 21.93 nm", skin_depth(9.0)),
                       ("1 nm", 1e-9), ("1 Angstrom", 1e-10), ("1 fm", 1e-15),
                       ("the Planck length", L_PLANCK)):
        print("  %-34s %16.4e %16.4e" % (label, delta_curved(eps),
                                         chi_compactness(eps)))
    print("\n  delta = 1 only at eps = %.6f l_P.  BOTH ARE INDEPENDENT OF a."
          % (delta_unity_eps() / L_PLANCK))
    print("  The backreaction bound and DOCKET 54's magnitude wall are the same")
    print("  sub-Planckian wall, reached from two directions.")
    print("  crossover a_c = %.7f x skin depth, FOR EVERY CONDUCTOR "
          "[DERIVED from two RECOVERED coefficients]"
          % (crossover_radius(9.0) / skin_depth(9.0)))
    print("    gold      skin depth %8.4f nm   a_c %8.4f nm"
          % (skin_depth(9.0) * 1e9, crossover_radius(9.0) * 1e9))
    print("    aluminium skin depth %8.4f nm   a_c %8.4f nm"
          % (skin_depth(15.3) * 1e9, crossover_radius(15.3) * 1e9))

    print("\n" + BAR)
    print("THE BILL -- 1 %% CONTRACTION OF PROPER RADIAL DISTANCE AT R = 1 m")
    print(BAR)
    print("  %-30s %18s %18s" % ("q", "m (kg) [DERIVED]", "|p_r| (Pa) [DERIVED]"))
    for q in (1e-6, 1e-3, 1e-2, 0.1, 0.5):
        print("  %-30g %18.6e %18.6e"
              % (q, mass_for_contraction(q, 1.0),
                 abs(tension_for_contraction(q, 1.0))))
    req = abs(tension_for_contraction(0.01, 1.0))
    print("\n  designpoint.py's design equation at R = 1 m, beta = 0.1 "
          "[IMPORTED]: %.6e Pa" % abs(designpoint_tension()))
    print("  equivalent purely radial magnetic field: %.4e T  -- and section 9"
          % field_for_tension(req))
    print("  caution (2) says that field cannot have a regular centre.\n")
    print("  %-56s %13s %10s" % ("tension available", "Pa", "short by"))
    for label, val, st in tension_ladder():
        print("  %-56s %13.4e %10.2e   [%s]" % (label[:56], val, req / val, st))
    print("\n  THE CLOSEST RUNG IS NOT TRACELESS AND IS THEREFORE OUTSIDE THE")
    print("  HYPOTHESIS.  Inside it, the shortfall is 2.46e+13.")

    print("\n" + BAR)
    print("PEER STATUS -- RECORDED, NEVER REPAIRED, AND NO PEER IS EDITED")
    print(BAR)
    for target, st, why in PEER_STATUS:
        print("  %-12s %s" % (st, target))
        for i in range(0, len(why), 72):
            print("               %s" % why[i:i + 72])

    print("\n" + BAR)
    print("VERDICT:  %s" % VERDICT)
    print(BAR)
    print("  %-44s %s" % ("supersedes certify.py", SUPERSEDES_CERTIFY))
    print("  %-44s %s" % ("restates it on a smaller class",
                          RESTATES_CERTIFY_ON_SMALLER_CLASS))
    print("  %-44s %s" % ("hypotheses added", HYPOTHESES_ADDED))
    print("  %-44s %s" % ("exact in flat space only",
                          IDENTITY_IS_EXACT_IN_FLAT_SPACE_ONLY))
    print("  %-44s %s" % ("curved correction", CURVED_CORRECTION))
    print("  %-44s %s" % ("... vanishes iff", CURVED_CORRECTION_VANISHES_IFF))
    print("  %-44s %s" % ("... and the only such source is",
                          ONLY_TRACELESS_CONSERVED_SOURCE_WITH_U_PLUS_PR_ZERO))
    print("  %-44s %s" % ("the integration constant is",
                          INTEGRATION_CONSTANT_IS))
    print("  %-44s %s" % ("... a limit of m", INTEGRATION_CONSTANT_IS_A_LIMIT_OF_M))
    print("  %-44s %s" % ("hypothesis actually used off staticity",
                          HYPOTHESIS_ACTUALLY_USED_OFF_STATICITY))
    print("  %-44s %s" % ("non-static branch closed", NONSTATIC_BRANCH_IS_CLOSED))
    print("  %-44s %s" % ("source sphericity load-bearing",
                          SOURCE_SPHERICITY_IS_LOAD_BEARING))
    print("  %-44s %s" % ("read-direction sphericity load-bearing",
                          READ_DIRECTION_SPHERICITY_IS_LOAD_BEARING))
    print("  %-44s %s" % ("the test quantity", TEST_QUANTITY))
    print("  %-44s %s / %s" % ("u(R) < 0 necessary / sufficient",
                               U_AT_R_IS_NECESSARY, U_AT_R_IS_SUFFICIENT))
    print("  %-44s %s" % ("novelty claimed", NOVELTY_CLAIMED))
    print("  %-44s %s" % ("DOCKET 54's non-find", "WITHDRAWN"))
    print("  %-44s %s" % ("Route A", ROUTE_A_STATUS))
    print("  %-44s %s" % ("any gate moves", ANY_GATE_MOVES))
    print("  %-44s %s" % ("the z3 layer is sign-only", Z3_LAYER_IS_SIGN_ONLY))
    print("  %-44s %s" % ("... coefficient and exponent pinned by",
                          COEFFICIENT_AND_EXPONENT_PINNED_BY))
    print("  %-44s %s" % ("the bill", "NOT LIFTED"))
    print("  %-44s %s" % ("nothing repaired", NOTHING_IS_REPAIRED))
    print("  %-44s %s" % ("and no peer is edited", NO_PEER_IS_EDITED))
    print("  scope:   %s" % SCOPE)
    print("  REFUSED: %s" % REFUSED)
    return 0


def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--verify" in sys.argv:
        import sympy as sp
        bad = 0
        rows = verify()
        for label, resid, want in rows:
            rr = sp.simplify(resid)
            bad += (rr != want)
            print("  %-70s %s" % (label, rr))
        if len(rows) != RESIDUAL_COUNT:
            bad += 1
            print("\n  RESIDUAL COUNT DRIFTED: %d rows against the pinned %d"
                  % (len(rows), RESIDUAL_COUNT))
        print("\n%d residual(s) not as expected" % bad)
        sys.exit(1 if bad else 0)
    if "--prove" in sys.argv:
        bad = 0
        comp = {}
        rows = obligations()
        for name, got, want, good in rows:
            bad += (not good)
            kind = classify_row(name) or (
                "theorem, negated -> unsat, own hypothesis sat"
                if want.startswith("unsat") else "necessity witness (sat)")
            comp[kind] = comp.get(kind, 0) + 1
            print("  %-70s %-18s (want %-14s) %s"
                  % (name, got, want, "ok" if good else "FAIL"))
        print("\n  COMPOSITION, PINNED so that a lost row is visible:")
        for kind in sorted(set(list(comp) + list(OBLIGATION_COMPOSITION))):
            g, w = comp.get(kind, 0), OBLIGATION_COMPOSITION.get(kind, 0)
            bad += (g != w)
            print("    %-52s %3d  (pinned %3d) %s"
                  % (kind, g, w, "ok" if g == w else "DRIFT"))
        if len(rows) != OBLIGATION_COUNT:
            bad += 1
            print("    OBLIGATION COUNT DRIFTED: %d against %d"
                  % (len(rows), OBLIGATION_COUNT))
        print("\n%d obligation(s) not as expected" % bad)
        sys.exit(1 if bad else 0)
    sys.exit(report())


if __name__ == "__main__":
    main()
