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
    else.  Its COROLLARY adds a regular centre.  THIS TEST NEEDS ALL OF THAT
    AND TWO MORE HYPOTHESES:  T^mu_mu = 0 EXACTLY, and a TEST-FIELD BACKGROUND.
    Two hypotheses in and nothing new out.

    AND THE CLASS IS SMALLER THAN THE FIRST DRAFT KNEW.  THEOREM X, section 3a:
    IF THE GEOMETRY IS SOURCED BY THIS T, the identity m = 4 pi r^3 p_r reduces
    the exact anisotropic TOV equation to (u + p_r) Phi' = 0 POINTWISE, whose
    only regular-centred solution is MINKOWSKI.  THE EXACTLY-SOURCED CLASS IS
    EMPTY.  So "Phi' = 0" is WITHDRAWN as an exactness route -- under the field
    equation it gives 4 pi r^3 p_r = MINUS m, the wormhole branch -- and what
    the instrument runs on is the TEST-FIELD reading, where the background is
    fixed, m is the matter integral, and section 6's delta is the measured
    error on the join.

    NO NOVELTY IS CLAIMED FOR ANY LINE OF THE MATHEMATICS, and DOCKET 54's
    "I did not find either stated in this form" IS WITHDRAWN: it is in print
    since 1995 at the latest and its flat parent since 1911.  Section 1.

    THE HEADLINE THE WITNESS FORCES.  The integration constant is NOT a limit
    of m.  In Reissner-Nordstrom both m(r) and 4 pi r^3 p_r(r) diverge to
    -infinity at the centre while their difference is EXACTLY M at every
    radius: C is a renormalised central mass, and an instrument computing it as
    lim m(r) returns -infinity where the answer is finite.  RN breaks
    certify.py's m(0) = 0 and this identity's r^3 p_r -> 0 in the same region,
    but THE TWO HYPOTHESES ARE LOGICALLY INDEPENDENT -- section 11's separating
    witness proves it, and the draft's "one fact seen twice" is WITHDRAWN.
    Section 4 holds RN in full; it is not restated here.

    NO GATE MOVES.  A cheaper test for a requirement is not a cheaper
    requirement.  candidates.py's KIND/DEADLINE/MAGNITUDE are unchanged,
    overturn.py's L4 is unchanged, and the bill for 1 % contraction of proper
    radial distance at R = 1 m is 9.7773e+40 Pa [DERIVED] of radial TENSION --
    2.46e+13 [DERIVED] times the best in-hypothesis tension known (a magnetar
    field, itself DERIVED from an inferred B).  Section 9 carries every status.

    NOTHING IS REPAIRED AND NO PEER IS EDITED.  Section 11 is a status table
    naming what each peer's claim becomes; the human seats any change.

    WHAT THE SELFTEST'S ROWS ARE WORTH, STATED BEFORE THEY ARE READ.  Every row
    prints a KIND.  MEASURED pins a quantity against something outside this
    file's own algebra; DECLARED pins a module constant against the literal
    beside it; CONSTRUCTION holds for ALL inputs because both sides are the
    same algebra written here twice.  A CONSTRUCTION row is worth keeping -- it
    catches a formula drifting out of step with its own inverse -- but IT IS
    NOT EVIDENCE AND IS NOT COUNTED AS ANY.  64 of 175 rows are MEASURED; the
    census is printed at the end of the run and pinned in FIXTURE_KINDS.

    THIS SECTION IS A VERDICT, NOT A FIFTH COPY OF THE FILE.  An audit pass
    measured the draft's section 0 as a 55-line compressed restatement of
    sections 1, 4, 9 and 11/12 -- the prior-art chain, the RN argument, the
    containment and the refusal list, each at near-full length.  Every one of
    those now appears here in at most three lines with a pointer, and nowhere
    else in this section.

===============================================================================
1.  PRIOR ART, FIRST, AND IT GOES AGAINST US
===============================================================================

THE IDENTITY IS PUBLISHED, IN FULL GENERAL RELATIVITY, AND IN A STRONGER FORM
THAN THE ONE DOCKET 54 DERIVED.  L. Herrera, arXiv:1801.08358v2, eq. (32):

    m_T = e^{(nu+lambda)/2} [ m(r) + 4 pi r^3 P_r ]

-- Tolman mass = redshift factor x (Misner-Sharp mass + 4 pi r^3 p_r), with no
flat-background hypothesis at all.  Rearranged, 4 pi r^3 p_r = e^{-(nu+lambda)/2}
m_T - m, which is DOCKET 54's identity with the traceless step not yet taken and
with a factor a flat derivation cannot see.  The same paper's eq. (10),
nu' = 2(m + 4 pi P_r r^3)/(r(r - 2m)), is the field equation THEOREM X turns on.
BOTH WERE RE-READ AT SOURCE BY THIS REPAIR PASS and are CITED, not RECOVERED.

Herrera & Di Prisco, arXiv:gr-qc/9810020, eq. (39), states it again
time-dependently -- m_T = e^{(nu+lambda)/2}[m(r,t) - 4 pi r^3 T^1_1], which with
that paper's T^1_1 = -P_r is the claimed form.  IT DATES ITS OWN DERIVATION to
Herrera, Di Prisco, Hernandez-Pastora & Santos, Phys. Lett. A 237, 113 (1998),
and SEPARATELY records that its eq. (39) "is, formally, the same expression for
m_T in terms of m and T^1_1, that appears in the static (or quasi-static) case
(eq.(25) in [20])", where [20] is Herrera & Santos, Gen. Rel. Gravit. 27, 1071
(1995).  A FIRST DRAFT OF THIS FILE WROTE THAT THE 1998 PAPER "ITSELF RESTATES"
THE 1995 ONE.  THE SOURCE DOES NOT SAY THAT, and the sentence is WITHDRAWN: it
was an inference presented as the source's own statement, in the one section
whose job is to go against us.  The load-bearing conclusion -- in print since
1995 at the latest -- is untouched, and rests on the quoted sentence alone.

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

Trace over i on a sphere of radius R with X^i = R n^i and dS_l = n_l R^2 dOmega:
THE LEFT-HAND SURFACE TERM IS 4 pi R^3 <T^r_r>(R), and the right-hand side is
the volume integral int_V Theta^{ii} d^3x of the spatial stress trace.  DOCKET
54's "EXACT, NO INTEGRATION CONSTANT" is Laue plus the divergence theorem.

    A FALSE SENTENCE IS CORRECTED HERE RATHER THAN QUIETLY REPLACED.  A first
    draft of this file wrote "Trace over i on a sphere and the RIGHT-hand side
    is 4 pi R^3 p_r(R)", which inverts the two sides of the equation it cites.
    Re-read at source by this repair pass (Wang, Can. J. Phys. 93, 1470 (2015),
    eq. (20)): the surface integral is on the left.  The file's every LATER use
    of the relation is the right way round -- the complete-apparatus argument
    sets int_V Theta^{ii} = 0 and concludes 4 pi R^3 p_r(R) = 0, and obligation
    family L encodes that direction -- so nothing downstream moves.  A slip that
    does not propagate is still a false sentence about a cited equation.

    AND A DISCREPANCY IN THE von Laue CITATION, RECORDED NOT SILENTLY ALIGNED.
    This file prints "Ann. Phys. 340(8), 524 (1911)"; Wang's own reference [1],
    which is the route by which von Laue is RECOVERED here, prints "Ann. Phys.
    35, 524 (1911)".  The two numberings are the same paper (35 is the original
    series, 340 the Wiley continuous numbering).  Since the row's status is
    RECOVERED THROUGH WANG, the number Wang prints is the one it is entitled to,
    and both are given rather than one being chosen.
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

STATUS OF THE ATTRIBUTIONS, NOT FLATTENED, AND THE RULE CHANGED THIS PASS.  A
draft of this section said "NO PDF WAS RE-OPENED WHILE THIS FILE WAS COMPOSED,
and a row's status is that pass's, not this file's".  THAT IS NO LONGER TRUE AND
THE SENTENCE IS WITHDRAWN: the repair pass re-opened Herrera arXiv:1801.08358 at
source and read eq. (10), eq. (22) and eq. (32) there, so those three rows are
CITED by THIS pass and their notes say which.  Every other CITED row is still
the earlier pass's and is still marked as that pass's.  A status names WHO read
it, never merely that someone did.
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
                                (b) a TEST-FIELD BACKGROUND -- the background
                                    metric is fixed and is NOT sourced by this
                                    T, so that the K term below is absent by
                                    construction rather than by cancellation,
                                because the exact curved relation is

        d(r^3 p_r)/dr = r^2 (u + T^mu_mu) - r^3 (u + p_r) Phi'      (V10)

ONE LOCAL CONDITION KILLS K, NOT TWO, AND THE FIRST DRAFT NAMED THE WRONG ONE.
The draft offered "(i) Phi' = 0, or (ii) u + p_r = 0" and justified BOTH with
the single sentence "Herrera's redshift factor e^{(nu+lambda)/2} does not cancel
unless g_tt g_rr = -1".  That sentence is a justification of (ii) ALONE.  From
the COMPUTED Einstein tensor (V26, residual 0),

        nu' + lambda' = 8 pi r e^{lambda} (u + p_r) ,

so nu + lambda = const -- i.e. g_tt g_rr = -1, i.e. the redshift factor is unity
-- HOLDS IF AND ONLY IF u + p_r = 0.  Phi' = nu'/2 = 0 does NOT give it: it
leaves lambda' = 8 pi r e^{lambda}(u + p_r), so nu + lambda still runs.  And
Phi' = 0 TOGETHER WITH nu + lambda = 0 forces lambda' = 0, so 1 - 2m/r is
constant, so with a regular centre m == 0.  (i) IS WITHDRAWN (section 3); there
was only ever one local exactness route, and section 3 shows the regular centre
excludes it.  So the honest reading of (b) is the test-field one.

WHAT IT HONESTLY BUYS -- AND THE ECONOMY IS SMALLER THAN THE DRAFT CLAIMED:
    - ONE EVALUATION OF T^r_r AT R, **GIVEN** an a-priori bound on chi_max and
      on V/|m(R)|.  ABSENT THOSE TWO THE QUADRATURE IS NOT AVOIDED.  The draft
      said "ONE EVALUATION INSTEAD OF A QUADRATURE" flatly; that is false off
      the exact class, and section 3a shows the exact class is empty.  Section
      6's profile-free fallback is |delta| <= [chi/(1-chi)] V/|m(R)| with
      V := INT_0^R 4 pi r^2 (|u| + |p_r|) dr -- AN INTEGRAL OVER THE SAME BALL,
      on the same integrand class as INT 4 pi r^2 u dr.  And section 6's exact
      closed form delta = chi/2 is available only because the near-wall PROFILE
      was banked in advance, i.e. because the whole radial dependence of u and
      p_r was already known -- at which point the ball integral is free anyway.
      What the test buys is therefore one evaluation PLUS two a-priori bounds,
      never one evaluation instead of a quadrature.
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

WHEN IS THE FLAT IDENTITY EXACT IN A SOURCED CURVED SPACETIME?  Precisely when
K = 0.  THE DRAFT NAMED TWO LOCAL SUFFICIENT CONDITIONS AND ONE OF THEM IS
WITHDRAWN HERE:

    (i)  Phi' == 0      -- WITHDRAWN.  IT IS NOT AN EXACTNESS CONDITION; IT IS
                           THE WORMHOLE BRANCH, AND IT CONTRADICTS THE IDENTITY.
    (ii) u + p_r == 0   -- THE RADIAL NEC IS SATURATED everywhere.  Survives,
                           and the regular centre excludes it.

WHY (i) IS WITHDRAWN, IN ONE EXACT STEP.  The COMPUTED G^r_r (V9) gives
Phi' = (m + 4 pi r^3 p_r)/(r(r - 2m)).  Setting Phi' = 0 therefore forces

        4 pi r^3 p_r = MINUS m ,

which is this file's OWN V18a -- derived three hundred lines further down for
the Morris-Thorne throat and never connected back to section 2.  It is the
OPPOSITE SIGN to the identity 4 pi r^3 p_r = +m.  Conjoining the two gives
2m = 0, hence m == 0 and p_r == 0: the class on which the draft's stated
exactness hypothesis holds AND the identity is exact contains nothing but the
vacuum.  Machine-checked twice -- sympy V27 (the two equations solve to
{m: 0, p_r: 0}) and z3 obligation I7 (unsat with m != 0, and unsat with
p_r != 0).  The published parent says it too: Herrera arXiv:1801.08358 eq. (10),
read at source.  "Phi' = 0 is the wormhole branch" and "Phi' = 0 is an exactness
route for the identity" ARE THE SAME EQUATION READ WITH OPPOSITE SIGNS, and the
file held both at once for the length of a draft.

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
ALREADY EXCLUDES.  The draft wrote "the two exceptions are the same object";
the sharper and now-correct statement is that THERE WAS ONLY EVER ONE EXCEPTION,
and the other route was impossible.

===============================================================================
3a. THEOREM X -- THE EXACTLY-SOURCED CLASS IS EMPTY
===============================================================================

    HYPOTHESES.  Traceless, conserved, spherically symmetric, static, regular
    centre, AND THE GEOMETRY SOURCED BY THIS T THROUGH THE EINSTEIN EQUATIONS.
    CONCLUSION.  Minkowski.  u == p_r == p_t == m == 0 at every radius.

FOUR STEPS, EVERY ONE OF THEM AN EQUATION THIS FILE ALREADY HELD.  Impose the
identity m(r) = 4 pi r^3 p_r(r) at every radius.

    (1) dm/dr = 4 pi r^2 u, EXACT IN FULL GR from the computed G^t_t (V8),
        then forces u = 3 p_r + r p_r'                              -- V5.
    (2) Tracelessness forces p_t = p_r + r p_r'/2                   -- A4.
    (3) G^r_r gives Phi' = (m + 4 pi r^3 p_r)/(r(r - 2m)) = 2m/(r(r - 2m))
        on the identity                                             -- V11.
    (4) Substitute (1)-(3) into the exact anisotropic TOV equation
        p_r' + (2/r)(p_r - p_t) + (u + p_r) Phi' = 0                -- V10a.
        THE FIRST TWO TERMS CANCEL IDENTICALLY, p_r' - p_r' = 0, AND WHAT IS
        LEFT OVER IS

                        (u + p_r) Phi' == 0     POINTWISE.           (V28)

Phi' = 8 pi r p_r/(1 - 8 pi r^2 p_r) vanishes only where p_r = 0, so this is
(u + p_r) m == 0 at every radius.  If m is not identically zero then u + p_r = 0
on an open set, which with tracelessness and conservation forces r u' + 4u = 0,
so u = K/r^4 -- REISSNER-NORDSTROM, whose r^3 p_r -> -INFINITY at the centre and
which the regular centre therefore excludes.  Hence m == 0, so p_r = m/(4 pi r^3)
== 0, so u = 3 p_r + r p_r' == 0 and p_t = (u - p_r)/2 == 0.  Vacuum, Phi' = 0,
MINKOWSKI.

    MACHINE-CHECKED IN BOTH LAYERS.  sympy V28 reduces the TOV residual on the
    identity to 8 pi r (-r p_r' - 4 p_r) p_r/(8 pi r^2 p_r - 1) and confirms it
    equals (u + p_r) Phi' with residual 0; V29 dsolves the surviving branch to
    u = C1/r^4.  z3 family X: X1 the hypothesis set is SAT (so this is not a
    vacuous proof), X2 it entails (u + p_r) m == 0, X3 it is UNSAT with
    u + p_r != 0 and p_r != 0 together.

    WHY NEITHER LAYER CAUGHT IT BEFORE, MEASURED NOT GUESSED.  Family I declared
    Phi_p a FREE real and never linked it to (m + 4 pi r^3 p_r)/(r(r - 2m)).
    Reproducing family I's encoding verbatim, And(LOCALGR, Phi_p == 0,
    m == F r^3 p_r, m != 0) comes back SAT -- that is DRIFT X, kept as a
    standing probe.  Adding the one missing constraint turns the same query
    UNSAT -- that is I7.  ONE LINE OF ENCODING SEPARATED A GREEN GUARD FROM AN
    EMPTINESS PROOF, and GUARDS I1, I2 and I3 passed throughout because the link
    was absent.  This is refusal 1 of section 10 in its second direction: a free
    real asserted ZERO is exactly as much a statement about the encoding as a
    free real asserted NONZERO.

WHAT SURVIVES, AND IT IS WHAT THE INSTRUMENT ACTUALLY RUNS.  THE TEST-FIELD
READING.  The background is fixed by fiat -- Minkowski, or any metric not
sourced by this T -- the conservation law nabla_mu T^mu_nu = 0 is imposed on
THAT background, and m denotes the MATTER INTEGRAL INT_0^R 4 pi r^2 u dr rather
than the Misner-Sharp mass of a spacetime this T generates.  On that reading
every witness in section 5 is legal, the identity is exact flat-space algebra,
and section 6's delta BOUNDS THE ERROR MADE IN HANDING m to a geometric theorem
that wants the Misner-Sharp mass.  THAT BOUND IS NOW LOAD-BEARING RATHER THAN
REASSURING: it is the whole of the join, and it is a quadrature.

    REFUSED, AND WHY.  The adversarial pass proposed renaming the hypothesis
    keyword `flat_background_to_relative_error_delta`.  REFUSED.  A tolerance
    inside a keyword NAME invites a caller to grant the hypothesis by eyeballing
    a number, which is the failure mode the whole refusal surface exists to
    stop.  The keyword becomes `test_field_background` -- naming the READING,
    which is a thing a caller can actually certify -- and the tolerance is a
    separate explicitly-passed argument with its own refusal.  A hypothesis and
    its error bar are two objects and this file does not fuse them.

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

POSITIVE CONTROL, AND IT IS NOT AN INVENTION -- BUT IT IS A TEST-FIELD CONTROL
AND THE DRAFT DID NOT SAY SO.  Uniform negative-energy radiation,
T^mu_nu = u_0 diag(-1, -1/3, -1/3, -1/3) with u_0 > 0, is the exact ISOTROPIC
AVERAGE of the measured parallel-plate Casimir tensor over uniformly distributed
plate normals (<n_i n_j> = delta_ij/3).  It is traceless, regular-centred, and
conserved IN FLAT SPACE -- and

    IT IS NOT A SOLUTION OF THE EINSTEIN EQUATIONS IT WOULD SOURCE.  The draft
    wrote "Every hypothesis holds exactly".  Measured (V30): for this tensor
    m(r) = -4 pi r^3 u_0/3, so G^r_r gives Phi' = -8 pi r u_0/(8 pi r^2 u_0 + 3),
    which is zero only at u_0 = 0; and the exact anisotropic TOV residual is
    32 pi r u_0^2/(3(8 pi r^2 u_0 + 3)), STRICTLY POSITIVE for u_0 > 0.  The
    control satisfies the hypotheses precisely BECAUSE IT DOES NOT GRAVITATE.
    That is THEOREM X seen from the other end, and it is why the selftest grants
    it `test_field_background` and NOT a sourced-background claim.

with

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

THE IDENTITY DETERMINES THE KILLING-FRAME p_r BY A SCALAR.  IT DOES NOT MAKE
p_r A SCALAR, AND THE DRAFT'S V24 LABEL SAID IT DID.  The Misner-Sharp invariant
-- Gamma^2 - U^2 = g^{ab} d_a R d_b R = 1 - 2m/R, which is MISNER & SHARP (1964)
and Hernandez, and which foliation.py's RANGE THEOREM is built on rather than
being foliation.py's own -- combined with the identity's m = 4 pi R^3 p_r gives
(V24, residual 0)

    Gamma^2 - U^2 = 1 - 8 pi R^2 p_r(R)
    i.e.   p_r(R) = [ 1 - g^{ab} d_a R d_b R ] / (8 pi R^2) ,

whose right-hand side is built from the metric and the areal radius alone.

    WITHDRAWN: "so p_r is a SCALAR under H".  A FRAME COMPONENT WHOSE VALUE IS
    COMPUTABLE FROM AN INVARIANT IS STILL A FRAME COMPONENT.  The correct
    statement is that UNDER H THE KILLING-FRAME RADIAL STRESS IS DETERMINED BY A
    FOLIATION-INDEPENDENT SCALAR; it is not itself one.  A witness INSIDE the
    class makes the difference bite (V31, and the exact triple is seated as
    `boost_witness`): p_r = r^6 - 1, u = 9r^6 - 3, p_t = 4r^6 - 1 is traceless
    (residual 0), conserved (residual 0), regular-centred (r^3 p_r -> 0), and
    satisfies the identity at EVERY radius (residual 0).  At R = 9/10 it reads
    p_r = -0.468559 < 0, m = -4.292415, 1 - 2m/R = 10.538699 > 1: the instrument
    says YES and foliation.py says Gamma > 1 in every foliation.  Now apply this
    file's OWN boost law V23 at that same event with q = 0.  p_r'(w) vanishes at
    w_c = 0.566301 and is POSITIVE above it -- +0.568159 at w = 0.80, +2.526289
    at w = 1.20 -- while 1 - 2m/R is a scalar and does not move.  SO THE TWO
    SIDES OF THE HEADLINE COME APART AT ONE AND THE SAME EVENT, INSIDE THE CLASS.
    The escape is to stand in the Killing frame, and it is a real escape -- but
    then the headline must CARRY that qualifier instead of relegating it to a
    failure mode, which is what it now does.

THE CHAINED STATEMENT, MACHINE-CHECKED (section 10, family B and H):

    Under H -- TEST-FIELD-background traceless, conserved, spherically
    symmetric, stationary-flux, regular centre, and m read as the matter
    integral INT 4 pi r^2 u dr --

        p_r(R) < 0  <=>  m(R) < 0  <=>  Gamma > 1 IN EVERY FOLIATION at R,

    and the middle term may be deleted: THE KILLING-FRAME RADIAL STRESS IS A
    TENSION AT R IFF PROPER RADIAL DISTANCE IS CONTRACTED AT R IN EVERY
    FOLIATION -- to the accuracy of section 6's delta on the join.

    H IS THE TEST-FIELD H AND THAT IS NOT A CONVENIENCE.  The draft wrote
    "geometry sourced by it" into H.  THEOREM X (section 3a) shows that H so
    read is satisfied only by Minkowski, under which p_r == 0 and m == 0 at
    every radius, no side is ever strictly negative, AND THE CHAIN NEVER FIRES.
    A vacuously true chained biconditional is not a result.  The file cannot
    have both readings and does not try: it takes the test-field one, states the
    join error, and keeps the boost witness -- which is legal in that reading --
    as the reason the headline says KILLING-FRAME.

foliation.py's RANGE THEOREM carries NO staticity hypothesis, so the right-hand
biconditional is the strongest link in the chain and it is not this file's.

THE FOUR WAYS THE CHAIN FAILS, NONE HIDDEN:
    (1) p_r < 0 IS GAUGE, INSIDE THE CLASS AS WELL AS OUTSIDE IT -- the boost
        witness above is IN H.  The chain is about the KILLING-FRAME p_r and
        about no other frame's, and the draft's "OUTSIDE H, p_r < 0 IS GAUGE"
        wrongly implied that inside the class it is not.  WITHDRAWN.
    (2) THE REGULAR CENTRE IS LOAD-BEARING -- RN has p_r < 0 at every radius and
        m < 0 only inside r < Q^2/2M.  The gap is exactly C = M.
    (3) THE SEAM IS THE FIELD EQUATION, NOT THE ALGEBRA, AND IT IS THE WEAKEST
        LINK RATHER THAN AN EXACT ONE.  The identity is test-field algebra; the
        contraction theorem is about the actual Misner-Sharp mass.  The relation
        dm/dr = 4 pi r^2 u is exact in full GR (V8) -- but THEOREM X shows that
        imposing BOTH it and the identity on a sourced geometry leaves only
        Minkowski, so the join cannot be taken as exact and simultaneous.  What
        quantifies the seam is section 6's delta, and nothing else does.  The
        draft's "so the JOIN is exact" is WITHDRAWN.
    (4) THE NON-STATIC BRANCH IS NOT CLOSED -- section 7's limit.

===============================================================================
9.  THE BILL, WHICH THIS FILE DOES NOT LOWER BY ANY AMOUNT
===============================================================================

Proper radial length dl = dr/sqrt(1 - 2Gm/(rc^2)).  A contraction by fraction q
needs x = 2G|m|/(Rc^2) = 1/(1-q)^2 - 1, hence m = -x R c^2/(2G), and the
identity converts that mass requirement into a STRESS requirement with no
further physics: p_r(R) = m(R) c^2/(4 pi R^3).  At q = 0.01, R = 1 m the mass is
-1.3671e+25 kg [DERIVED] = -2.289 Earth masses [DERIVED], reproducing the
ruling's figure, and

    THE REQUIRED RADIAL TENSION IS 9.7773e+40 Pa  [DERIVED].

EVERY FIGURE IN THIS SECTION CARRIES ITS STATUS AT THE POINT OF STATEMENT, not
only in FIGURE_STATUS.  The draft attached statuses in code and throughout
section 6 and then left sections 0 and 9 -- the VERDICT and the bill, which are
the most-read text in the file -- with seven bare numbers.  DERIVED here means
computed in this file from CITED constants; RECOVERED means measured out of
DOCKET 54's own banked figures and NOT recomputed.

The second, independent level -- designpoint.py's design equation
M = -beta^2 c^2 R/(12 G) at R = 1 m, beta = 0.1, imported rather than copied --
gives 8.0258e+39 Pa [DERIVED, through designpoint.py's own constants].  The two agree to just over one order of magnitude, which
is the honest resolution of "the level the bill requires", and both are quoted.

The ladder, every rung derived from a stated input, is printed by the report.
THREE CAUTIONS, AND THEY ARE LOAD-BEARING:

    (1) TRACELESSNESS EXCLUDES THE STRONGEST TENSION ON THE LADDER.  The QCD
        flux tube and the nucleon's confining region are the largest tensions
        nature is known to sustain and are only ~1e6 [DERIVED] short -- by far
        the closest rung.  But QCD matter is NOT traceless; the trace anomaly is
        essentially the whole of the nucleon mass, so it sits OUTSIDE this
        identity's hypothesis and cannot be quoted as a route.  Inside the
        hypothesis the best known tension is electromagnetic and the shortfall
        is 2.46e+13 [DERIVED -- a ratio of two DERIVED rungs, the magnetar rung
        itself resting on an INFERRED field, as tension_ladder() records].
    (2) A RADIAL MAGNETIC TENSION WITH A REGULAR CENTRE DOES NOT EXIST.  A
        purely radial B with div B = 0 is a monopole, B ~ 1/r^2 -- exactly the
        Q-part of RN: tension everywhere, m(R) < 0 everywhere with M = 0,
        POSITIVE energy density everywhere, and the regular-centre hypothesis
        broken and nothing else.  The one configuration that delivers the
        required sign for free is the one with a singular centre.  The RN
        witness and the bill witness are the same finding seen twice.
    (3) THE MATERIAL LADDER IS A SCALE STATEMENT, NOT A ROUTE.  A material
        tension is a stress in matter whose own positive rest energy is vastly
        larger -- DOCKET 54 section 3 puts that ratio at 2.7e-8 [RECOVERED
        from the ruling, which derives it; NOT recomputed here] even at the
        lightest-conceivable-sheet atomic ceiling.

CONSISTENCY WITH WHAT THE TREE HOLDS: the 3.48e55 shortfall [RECOVERED from
DOCKET 54; NOT recomputed here] that the ruling records for an ideal gold
Casimir shell is this same wall reached through the mass rather than the stress.
A CROSS-CHECK, NOT A FOURTH FINDING.

===============================================================================
10.  THE OBLIGATIONS, AND WHAT THEY DO NOT ESTABLISH
===============================================================================

--prove runs ELEVEN families over the reals plus three MUTATION PROBES.  EVERY
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
    D  regular centre / RN           I  test-field vs SOURCED background
    E  staticity / flux              X  THEOREM X: sourced H is empty
                                     L  the von Laue total-mass corollary

102 ROWS, AND THE COMPOSITION IS PINNED so that a lost row is visible rather
than silent: 38 theorems (asserted negated, unsat, own hypothesis sat), 22
family satisfiability guards, 22 encoding-drift probes, 16 necessity witnesses
each paired with a closed-form realisation, 3 mutation probes, and 1
over-representation containment row.  --verify's 37 residuals are pinned the
same way.  Both exit 1 on drift.

THE COMPOSITION MOVED FROM 39/20/14/14/3 = 90 AND THE THEOREM BUCKET WENT DOWN
WHILE THE TOTAL WENT UP.  Family X and obligations I7/I8 added four theorems;
FIVE were deleted as OVER-REPRESENTATION.  B2, D5, E4, H1 and I3 all carried the
IDENTICAL hypothesis FULL and conclusions ALL ENTAILED BY B3's -- six labels,
one theorem, counted six times -- and L2 was L1 with m alpha-renamed to I_uTh.
Worse than the count: D5, E4 and I3 each claimed to isolate ONE correction term
("with C = 0 restored", "with J = 0", "with K = 0") while every one of them set
ALL FOUR to zero, so no row proved what its label said.  D5 and E4 return as
ISOLATION rows that leave the other three corrections FREE -- and the honest
answer there is SAT, which is what those labels had always implied and never
tested.  THE ENTAILMENT IS NOT ASSERTED, IT IS MACHINE-CHECKED: the CONTAINMENT
row discharges "B3's conclusion implies B1's", so the deletion is a recorded
measurement rather than a quiet tidy-up.  Not a repair of a peer; a repair of
this file's own arithmetic about itself.

AND THE DRIFT PROBES WERE MEASURED, NOT ASSUMED EFFECTIVE.  An adversarial pass
ran 18 mutations against the encodings and found that only 5 of the draft's 14
DRIFT rows ever fired: B, C, F, G, H and L were caught by a GUARD or by a
theorem row flipping, never by their own family's probe.  A probe that never
fires is decoration.  Six were rewritten to probe their OWN family's encoding --
DRIFT B2 (MASTER's four corrections are genuinely free), DRIFT C2 (I_Theta
genuinely moves m), DRIFT F3 (the Laue moments admit I_xx != I_yy), DRIFT G2
(without the s*A < 0 link m > 0 is satisfiable), DRIFT H2 (GRR admits
g_rr != 1), DRIFT L2 (with p_r at the cut free, m = 0 is not forced) -- and each
was then re-mutated and CONFIRMED RED.  The table is at the end of this section.
DRIFT B2 was additionally the third MUTATION row's formula VERBATIM, counted
once in each bucket; the file disclosed the duplication in the mutation's own
label and still double-counted it.  DRIFT E was z3-equivalent to its own GUARD
E1 -- under LOCALJ with r > 0 and j != 0 the extra conjunct is entailed -- and
is replaced by a probe the guard does not entail.

    EVERY FAMILY, ONE OVER-CONSTRAINT OF ITS OWN ENCODING, PROBE CONFIRMED RED.
    Run on scratchpad copies; the original is byte-unchanged and NO PEER IS
    EDITED.  A probe is built from the SAME callable as its family wherever a
    hand-written copy would not have moved -- that generator-not-literal step is
    what the table measures.

      family  the over-constraint applied            the probe that went RED
      ------  ------------------------------------   -----------------------
      A       Theta = 0 baked into LOCAL             DRIFT A2
      B       K dropped from MASTERg                 DRIFT B2
      C       the trace term dropped from TRACEg     DRIFT C2
      D       C dropped from MASTERg                 DRIFT D2
      E       the flux term dropped from LOCALJg     DRIFT E
      F       axisymmetry baked into LAUE            DRIFT F3
      G       the s*A < 0 GIVEN baked into POWG      DRIFT G2
      H       m = 0 baked into GRR                   DRIFT H2
      I       Phi' = 0 baked into LOCALGR            DRIFT I
      X       Phi' = 0 baked into EINSTEINg          DRIFT X2
      L       the cut p_r = 0 baked into CUTG        DRIFT L and DRIFT L2

    ELEVEN FAMILIES, ELEVEN MUTATIONS, ELEVEN RED PROBES.  What this does NOT
    show is that every drift probe is independently load-bearing: eleven of the
    twenty-two were inert under these eleven mutations, and they are kept
    because each states something true about its family that no other row says.
    A PROBE MEASURED INERT IS RECORDED AS INERT, not deleted and not promoted.

WHAT Z3 DOES NOT ESTABLISH, AND NONE OF IT MAY BE QUOTED AS IF IT DID:

 1. THAT ANY AGGREGATE IS REALISABLE.  C, I_Theta, J, K, P, Phi_p and the Laue
    moments are FREE REALS in the encoding.  A FREE REAL ASSERTED **EITHER**
    NONZERO **OR** ZERO IS A STATEMENT ABOUT THE ENCODING, NOT ABOUT PHYSICS.
    The draft stated this caution in one direction only -- nonzero -- and the
    direction it omitted is the one that cost it THEOREM X: Phi_p was a free
    real in family I, was not named in this list at all, and setting it to zero
    looked like a hypothesis when it was an encoding choice the field equation
    forbids.  GUARDS I1, I2 and I3 were green throughout.  Family I now carries
    the G^r_r constraint as obligation I7, DRIFT X keeps the unlinked query as a
    standing record of what the omission permitted, and every must-be-SAT row is
    paired with a closed-form witness checked in sympy or in exact Fraction
    arithmetic; the sat alone would be worthless.
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
11.  PEER STATUS -- RECORDED, NEVER REPAIRED
===============================================================================

Printed in full by the report and asserted by a selftest fixture.  The four that
are not UNCHANGED:

    certify.py COROLLARY     CONFIRMED-AND-DISTINGUISHED.  Both hypotheses kill
                             the integration constant of a FIRST-ORDER ODE at
                             r = 0, and RN breaks both simultaneously in the
                             same region.  BUT THEY ARE DIFFERENT CONSTANTS OF
                             DIFFERENT ODEs AND NEITHER IMPLIES THE OTHER.  The
                             draft's "ONE FACT SEEN TWICE" is WITHDRAWN; the
                             separating witness is exact and is seated as
                             `independence_witness`:

                                 u == 0,  p_r = A/r^3,  p_t = -A/(2 r^3)

                             is traceless (residual 0) and conserved (residual
                             0); m(R) = INT 4 pi r^2 * 0 dr = 0, so certify.py's
                             COROLLARY hypothesis m(0) = 0 HOLDS -- while
                             C = 4 pi lim r^3 p_r = 4 pi A != 0, so THIS
                             identity's hypothesis FAILS and the identity is
                             off by exactly -4 pi A at every radius (V32).  The
                             converse separation is equally immediate: C = 0
                             with a central point mass m(0) != 0 leaves
                             4 pi R^3 p_r = m(R) - m(0), defect m(0).  RN is a
                             case where BOTH fail, which is what was actually
                             observed; it is not a case where they are the same
                             condition.  On the class where both hold the
                             identity is an independent second evaluation of the
                             same integral, and THAT much the draft had right.
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

    AND IT REFUSES TO SAY SO SIX TIMES.  An audit pass counted the sentence
    "nothing is repaired and no peer is edited" asserted six times over and the
    refusal of the word "replaces" six times over.  Both are true; neither gets
    more room for being repeated.  The convention this tree uses is prose once,
    a module constant, and a selftest fixture, and that is what is left.

    ON SIZE, THE FINDING IS ACCEPTED IN PART AND REFUSED IN PART, WITH NUMBERS.
    The audit measured the draft at 2,358 lines with a 772-line docstring
    against foliation.py's 1,134/408 -- 2.1x the largest peer -- "for a result
    the file itself correctly describes as 'Two hypotheses in and nothing new
    out'".  AFTER THIS REPAIR IT IS BIGGER, NOT SMALLER, and pretending
    otherwise would be the over-claim.  The two selftest rows below MEASURE the
    docstring against foliation.py's at run time so the ratio cannot drift
    silently, and DOCSTRING_LINE_CEILING is a commitment, not a description.

    ACCEPTED: duplication is what over-representation means, and it was cut.
    Section 0 lost its reprints of sections 1, 4 and 12 and now carries each in
    at most three lines with a pointer.  Five z3 obligations were deleted as one
    theorem wearing six labels.  One selftest fixture was deleted for comparing
    a call with itself.  Two sentences that were each asserted six times are
    asserted at the tree's convention.

    REFUSED: that the remaining growth is over-representation.  It is new
    content, and it is adversarial content -- THEOREM X and its four-step
    derivation, five withdrawals (condition (i), "p_r is a scalar", "one fact
    seen twice", "the join is exact", "one evaluation instead of a quadrature")
    each of which must carry the derivation that kills it, twelve new z3
    obligations, eight new sympy residuals, the eleven-family drift table, and
    the kind census.  A WITHDRAWAL IS LONGER THAN THE CLAIM IT WITHDRAWS, every
    time, because the claim needed one sentence and the withdrawal needs a
    proof.  Cutting them to fit a line budget would be exactly the "thin
    argument" this tree refuses, and a caveats section is what the length buys
    the file's way out of.  The cost is recorded here and not softened: A
    READER WHO WANTS ONLY THE RESULT SHOULD READ SECTIONS 0, 3a AND 8 AND STOP.
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
              "test_field_background", "stationary_flux", "ball_excludes_walls")

# `test_field_background` REPLACES THE DRAFT'S `flat_background`, and the rename
# is the finding rather than a tidy-up.  THEOREM X (section 3a): no self-
# gravitating non-vacuum source can honestly grant a SOURCED flat background,
# because Phi' = 0 plus the field equation forces 4 pi r^3 p_r = -m, which
# contradicts the identity and leaves only Minkowski.  What a caller CAN certify
# is that the background is fixed and not sourced by this T -- a reading, not a
# tolerance -- so that is what the keyword names.  See the REFUSED note in
# section 3a for why it is not named after an error bound instead.
KIND_TAG = {"MEASURED": "MEAS", "DECLARED": "DECL", "CONSTRUCTION": "CONS"}

KIND_MEANING = {
    "MEASURED": "pins a quantity against something OUTSIDE this file's algebra",
    "DECLARED": "pins a module constant against the literal written beside it",
    "CONSTRUCTION": "holds for ALL inputs: both sides are the same algebra here",
}

# THE CENSUS IS PINNED BECAUSE THE PROPORTION IS THE FINDING.  An adversarial
# pass measured 33 of the draft's 128 rows as tautologies -- two evaluations of
# one formula, holding for 200-400 random draws with max deviation 4e-16 -- and
# 22 more as bare declaration pins, leaving roughly 73 with content outside this
# file.  None of them was marked as anything.  A TAUTOLOGY IN A SELFTEST IS
# WORSE THAN NO FIXTURE, BECAUSE IT READS AS COVERAGE.  The response here is
# fourfold: the purest self-comparison (section 9's a-independence row, whose
# two sides were the SAME CALL) is DELETED and replaced by a probe that actually
# varies a; several construction rows have gained a MEASURED sibling that a sign
# flip cannot survive; every remaining row now PRINTS its kind, so the reader is
# told what a row is worth at the moment they read it; and the census counts its
# OWN two rows rather than reporting on all-but-itself.
#
# THE PROPORTION IS NOT FLATTERING AND IS NOT DRESSED UP.  85 of 175 rows are
# DECLARED -- a module constant against the literal beside it -- which catches a
# constant drifting away from the prose that quotes it and catches nothing else.
# 26 are CONSTRUCTION and are evidence of nothing.  64 are MEASURED.  A reader
# who wants to know what this file has actually tested should read those 64.
FIXTURE_KINDS = {"MEASURED": 64, "DECLARED": 85, "CONSTRUCTION": 26}
CONSTRUCTION_IS_NOT_EVIDENCE = True

# A CEILING, NOT A DESCRIPTION.  Section 12 accepts the audit's size finding in
# part and refuses it in part; this is the half that is enforced.  The selftest
# MEASURES the docstring against it and against foliation.py's at run time, so
# the ratio cannot grow silently.  Raising this number is a decision a human
# makes, not something a pass does on its way past.
DOCSTRING_LINE_CEILING = 1120


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


def isotropic_average_mirror(d):
    """NEGATIVE CONTROL (a), THE EXACT MIRROR: (e, p_r, p_t) = +u_0(1, 1/3, 1/3).
    DERIVED.  SEATED AS A FUNCTION RATHER THAN WRITTEN INLINE IN selftest():
    while the triple was a literal in the test body its tracelessness half could
    not fail whatever this module did, so only its VERDICT half was live."""
    u0 = plate_u0(d)
    return (+u0, +u0 / 3.0, +u0 / 3.0)


def boost_radial_stress(u, p_r, w, q=0.0):
    """THE BOOST LAW V23, as a function: p_r' = p_r cosh^2 w + u sinh^2 w
    + q sinh 2w.  DERIVED.  p_r IS A FRAME COMPONENT and this is what moves it."""
    return (p_r * math.cosh(w) ** 2 + u * math.sinh(w) ** 2
            + q * math.sinh(2.0 * w))


def critical_rapidity(u, p_r):
    """tanh^2 w_c = |p_r|/u, where a tension boosts to zero (V25).  DERIVED.
    Defined only where u > 0 > p_r and |p_r| < u."""
    return math.atanh(math.sqrt(abs(p_r) / u))


def boost_witness(r):
    """THE GAUGE WITNESS, INSIDE THE CLASS.  p_r = r^6 - 1, with u and p_t
    FORCED by V5 and A4 rather than chosen.  Returns (p_r, u, p_t).  Traceless,
    conserved, regular-centred, and the identity holds at EVERY radius -- and at
    R = 9/10 a finite boost turns its tension into a pressure while 1 - 2m/R,
    a scalar, does not move.  Section 8.  DERIVED; exact in Fractions."""
    r = Fr(r)
    return (r ** 6 - 1, 9 * r ** 6 - 3, 4 * r ** 6 - 1)


def independence_witness(r, A=Fr(1)):
    """THE SEPARATING WITNESS for section 11: u == 0, p_r = A/r^3,
    p_t = -A/(2 r^3).  Traceless and conserved exactly; m(R) == 0 so
    certify.py's COROLLARY hypothesis m(0) = 0 HOLDS, while
    C = 4 pi lim r^3 p_r = 4 pi A != 0 so THIS identity's hypothesis FAILS.
    The two hypotheses are therefore LOGICALLY INDEPENDENT.  Returns
    (p_r, u, p_t, C/(4 pi)).  DERIVED; exact in Fractions."""
    r = Fr(r)
    return (A / r ** 3, Fr(0), -A / (2 * r ** 3), A)


def tov_residual(u, p_r, p_t, dp_r, r, dPhi):
    """THE EXACT ANISOTROPIC TOV RESIDUAL (V10a):
    p_r' + (2/r)(p_r - p_t) + (u + p_r) Phi'.  Zero on shell.  DERIVED.
    This is the function THEOREM X evaluates on the identity."""
    return dp_r + 2 * (p_r - p_t) / r + (u + p_r) * dPhi


def dPhi_sourced(m, r, p_r_geom):
    """Phi' = (m + 4 pi r^3 p_r)/(r(r - 2m)) from the COMPUTED G^r_r (V9), in
    G = c = 1.  DERIVED.  NAMING THE THING FAMILY I LEFT FREE: while Phi' was an
    unconstrained real in the encoding, 'Phi' = 0' read as a hypothesis when the
    field equation makes it 4 pi r^3 p_r = -m.  Section 3a."""
    return (m + 4.0 * math.pi * r ** 3 * p_r_geom) / (r * (r - 2.0 * m))


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


def delta_quadrature(a, eps, n=20000):
    """delta BY QUADRATURE rather than by the closed form: the V16 integrand
    INT_eps^a 4 pi (a-E)^3 (u + p_r) Phi' dE over 4 pi (a-eps)^3 p_r(eps), with
    the near-wall profile carrying `a` explicitly at every step.  DERIVED.

    THIS IS HOW a-INDEPENDENCE IS TESTED, and it is the only way it can be:
    `a` does not appear in delta_curved's signature, so no call of that function
    can probe it.  LOG GRID -- the integrand goes as eps^-5, and section 6
    records a derivation pass whose uniform grid was 100 % wrong on exactly this
    integrand."""
    lo, hi = math.log(eps), math.log(a)
    h = (hi - lo) / n
    tot, prev = 0.0, None
    for i in range(n + 1):
        E = math.exp(lo + h * i)
        uw = -HBAR * C / (30.0 * math.pi ** 2 * a * E ** 3)
        pw = -HBAR * C / (60.0 * math.pi ** 2 * a * a * E ** 2)
        ph = -(2.0 / (15.0 * math.pi)) * L_PLANCK ** 2 / (E ** 2 * (a - E))
        f = 4.0 * math.pi * (a - E) ** 3 * (uw + pw) * ph * E   # dE = E dlnE
        if prev is not None:
            tot += 0.5 * (prev + f) * h
        prev = f
    den = (4.0 * math.pi * (a - eps) ** 3
           * (-HBAR * C / (60.0 * math.pi ** 2 * a * a * eps ** 2)))
    return abs(tot / den)


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
    inv = sp.Eq(GG ** 2 - UU ** 2, 1 - 2 * mS / RR)      # MISNER & SHARP (1964)
    out.append(("V24 SUBSTITUTING THE IDENTITY INTO THE MISNER-SHARP INVARIANT: "
                "Gamma^2 - U^2 = 1 - 8 pi R^2 p_r, so under H the KILLING-FRAME "
                "p_r is DETERMINED BY a scalar -- it is NOT itself a scalar "
                "(V31 is the witness; the draft's label is WITHDRAWN)",
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

    # ------------------------- 2/3.  THE TWO BACKGROUND CONDITIONS ARE DISTINCT
    nuf = sp.Function("nu")(r)
    lamf = sp.Function("lambda")(r)
    gnl = sp.diag(-sp.exp(nuf), sp.exp(lamf), r ** 2, r ** 2 * sp.sin(th) ** 2)
    gnli = gnl.inv()
    Gnl = christoffels(gnl, x)
    Rnl = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            e = 0
            for a in range(4):
                e += sp.diff(Gnl[a][b][c], x[a]) - sp.diff(Gnl[a][b][a], x[c])
                for d in range(4):
                    e += Gnl[a][a][d] * Gnl[d][b][c] - Gnl[a][c][d] * Gnl[d][b][a]
            Rnl[b, c] = sp.simplify(e)
    Rsnl = sp.simplify(sum(gnli[i, j] * Rnl[i, j]
                           for i in range(4) for j in range(4)))
    Enl = sp.simplify(gnli * sp.simplify(Rnl - sp.Rational(1, 2) * Rsnl * gnl))
    dnu_nl = sp.solve(sp.Eq(sp.simplify(Enl[1, 1]), 8 * sp.pi * pr),
                      sp.Derivative(nuf, r))[0]
    dlam_nl = sp.solve(sp.Eq(sp.simplify(Enl[0, 0]), -8 * sp.pi * u),
                       sp.Derivative(lamf, r))[0]
    out.append(("V26 g_tt g_rr = -1 IFF u + p_r = 0, NOT iff Phi' = 0: "
                "nu' + lam' = 8 pi r e^lam (u + p_r)",
                sp.simplify(dnu_nl + dlam_nl
                            - 8 * sp.pi * r * sp.exp(lamf) * (u + pr)), 0))

    # ---------------------------- 3.  Phi' = 0 IS THE WORMHOLE BRANCH, WITHDRAWN
    Msym, Psym = sp.symbols("M_w P_w")
    sol_i = sp.solve([sp.Eq(4 * sp.pi * r ** 3 * Psym, -Msym),
                      sp.Eq(4 * sp.pi * r ** 3 * Psym, Msym)],
                     [Msym, Psym], dict=True)
    out.append(("V27 CONDITION (i) WITHDRAWN: Phi' = 0 gives 4pi r^3 p_r = -m, "
                "which with the identity forces m = 0 and p_r = 0",
                sp.simplify(4 * sp.pi * r ** 3 * prMT + mfun)
                + (0 if sol_i == [{Msym: 0, Psym: 0}] else 1), 0))

    # ------------------------------------ 3a.  THEOREM X, THE EMPTINESS RESULT
    mId = 4 * sp.pi * r ** 3 * pr                    # the identity, imposed
    uId = sp.simplify(sp.diff(mId, r) / (4 * sp.pi * r ** 2))   # forced by V8
    ptId = sp.simplify((uId - pr) / 2)                          # forced by trace
    PhiId = sp.simplify((mId + 4 * sp.pi * r ** 3 * pr) / (r * (r - 2 * mId)))
    tovX = sp.simplify(sp.expand(sp.simplify(
        dvc[1].subs({sp.Derivative(Phi, r): PhiId}).subs(
            {u: uId, pt: ptId}).doit())))
    out.append(("V28 THEOREM X: on the identity the exact TOV residual collapses "
                "to (u + p_r) Phi' EXACTLY -- the emptiness result",
                sp.simplify(tovX - (uId + pr) * PhiId), 0))
    uX = sp.Function("u_X")(r)
    dsX = sp.dsolve(sp.Eq(r * sp.diff(uX, r) + 4 * uX, 0), uX)
    cX = sp.Symbol("C1")
    out.append(("V29 ... and the surviving branch u + p_r = 0 dsolves to "
                "u = C1/r^4, i.e. RN, which the regular centre excludes",
                sp.simplify(dsX.rhs * r ** 4 - cX)
                + (0 if sp.limit(r ** 3 * (-cX / r ** 4), r, 0, "+") is not sp.S.Zero
                   else 1), 0))

    # ------------------- 5.  THE POSITIVE CONTROL IS A TEST-FIELD CONTROL ONLY
    mPC = -4 * sp.pi * r ** 3 * u0 / 3
    PhiPC = sp.simplify((mPC + 4 * sp.pi * r ** 3 * prPC) / (r * (r - 2 * mPC)))
    out.append(("V30 THE POSITIVE CONTROL DOES NOT SOURCE ITS OWN GEOMETRY: its "
                "exact TOV residual is 32 pi r u_0^2/(3(8 pi r^2 u_0 + 3))",
                sp.simplify((0 + 0 + (ePC + prPC) * PhiPC)
                            - 32 * sp.pi * r * u0 ** 2
                            / (3 * (8 * sp.pi * r ** 2 * u0 + 3))), 0))

    # ------------------------------- 8.  THE GAUGE WITNESS, INSIDE THE CLASS
    prG, uG, ptG = r ** 6 - 1, 9 * r ** 6 - 3, 4 * r ** 6 - 1
    out.append(("V31 THE BOOST WITNESS IS IN THE CLASS: traceless, conserved, "
                "regular centre, and the identity exact at EVERY radius",
                sp.simplify(-uG + prG + 2 * ptG)
                + sp.simplify(sp.diff(prG, r) + 2 * (prG - ptG) / r)
                + sp.simplify(sp.limit(r ** 3 * prG, r, 0, "+"))
                + sp.simplify(sp.integrate(4 * sp.pi * r ** 2 * uG, (r, 0, R0))
                              - 4 * sp.pi * R0 ** 3 * prG.subs(r, R0)), 0))

    # ------- 11.  m(0) = 0 AND r^3 p_r -> 0 ARE INDEPENDENT, WITH THE WITNESS
    Aw = sp.Symbol("A_w", positive=True)
    prZ, uZ, ptZ = Aw / r ** 3, sp.Integer(0), -Aw / (2 * r ** 3)
    out.append(("V32 THE SEPARATING WITNESS: traceless, conserved, m(R) == 0 so "
                "certify.py's m(0) = 0 HOLDS, while C = 4 pi A != 0 and the "
                "identity is off by exactly -4 pi A",
                sp.simplify(-uZ + prZ + 2 * ptZ)
                + sp.simplify(sp.diff(prZ, r) + 2 * (prZ - ptZ) / r)
                + sp.simplify(sp.integrate(4 * sp.pi * r ** 2 * uZ, (r, 0, R0)))
                + sp.simplify((0 - 4 * sp.pi * R0 ** 3 * prZ.subs(r, R0))
                              + 4 * sp.pi * Aw), 0))

    # --------------------------------------------- THE LAYER'S OWN NEGATIVE
    # CONTROL.  EVERY OTHER ROW HERE ASSERTS ZERO, so the layer's pass/fail
    # SHAPE could not distinguish "the identity holds" from "the expression
    # collapsed to 0 for an unrelated reason".  This row's expected value is
    # deliberately NOT zero: read with the WRONG sign, the Morris-Thorne
    # residual is 2m rather than 0, and the layer must report that.
    out.append(("V33 NEGATIVE CONTROL FOR THIS LAYER: the throat residual read "
                "with the WRONG sign is -2m, NOT 0 -- a row that must be nonzero",
                sp.simplify(4 * sp.pi * r ** 3 * prMT - mfun),
                sp.simplify(-2 * mfun)))
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
    if n.startswith("CONTAINMENT"):
        return "over-representation containment (measured)"
    return None                        # decided by the want-string at the caller


def _z3():
    import prover
    prover.require_z3()
    import z3
    return z3


def obligations():
    """Eleven families over the reals -- A-I, X and L.  Every theorem row is asserted NEGATED and
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
    # THE FAMILY ENCODINGS ARE GENERATORS, NOT LITERALS, WHEREVER A DRIFT PROBE
    # HAS TO SEE THEM.  A probe written out by hand beside its family does not
    # move when the family's encoding is over-constrained, which is exactly how
    # nine of the draft's fourteen DRIFT rows managed never to fire under 18
    # mutations.  Building the probe from the same callable is what makes the
    # mutation propagate; the confirmed-red table is at the end of section 10.
    def MASTERg(mv, c, it, j, k):
        return z3.And(F > 0, R > 0, mv == F * R ** 3 * pr - c - it + j + k)

    K2 = z3.Real("K2")
    MASTER = MASTERg(m, Cc, I_Th, J, K)
    FULL = z3.And(MASTER, Cc == 0, I_Th == 0, J == 0, K == 0)
    sat("GUARD B0  the master formula is satisfiable", MASTER)
    sat("GUARD B1  under ALL hypotheses, m < 0 is satisfiable", z3.And(FULL, m < 0))
    sat("GUARD B2  under ALL hypotheses, m > 0 is satisfiable", z3.And(FULL, m > 0))
    # OVER-REPRESENTATION REMOVED, AND THE CONTAINMENT IS MEASURED NOT ASSERTED.
    # B1, B2, H1, D5, E4 and I3 all had the IDENTICAL hypothesis FULL and
    # conclusions ALL ENTAILED BY B3's -- six labels, one theorem, counted six
    # times.  Worse, D5/E4/I3 each claimed to isolate ONE correction term ("with
    # C = 0 restored", "with J = 0", "with K = 0") while every one of them set
    # ALL FOUR to zero, so no row proved what its label said.  B2, D5, E4, H1 and
    # I3 are DELETED; B1 is kept as the named headline; B3 is kept as the
    # strongest form; and CONTAINMENT below machine-checks the entailment so the
    # relationship is recorded rather than re-hidden.  The isolation claims those
    # labels wanted are the ISOLATION rows further down, which are honest because
    # they leave the other three terms FREE and come out SAT.
    ob("B1  THE BICONDITIONAL   m(R) < 0  <=>  p_r(R) < 0", FULL, (m < 0) == (pr < 0))
    ob("B3  trichotomy is exhausted: the three signs agree, always",
       FULL, z3.And((m < 0) == (pr < 0), (m > 0) == (pr > 0), (m == 0) == (pr == 0)))
    ob("CONTAINMENT  B3's conclusion ENTAILS B1's, the positive half and the "
       "zero case -- MEASURED here, which is why those are not separate rows",
       z3.BoolVal(True),
       z3.Implies(z3.And((m < 0) == (pr < 0), (m > 0) == (pr > 0),
                         (m == 0) == (pr == 0)),
                  z3.And((m < 0) == (pr < 0), (m > 0) == (pr > 0),
                         (pr == 0) == (m == 0))))
    ob("B4  AT EVERY RADIUS, not one: the signs agree at BOTH, independently",
       z3.And(F > 0, R1 > 0, R2 > 0, m1 == F * R1 ** 3 * pr1, m2 == F * R2 ** 3 * pr2),
       z3.And((m1 < 0) == (pr1 < 0), (m2 < 0) == (pr2 < 0)))
    sat("DRIFT B1  two radii MAY disagree in sign -- 'together' is at ONE radius",
        z3.And(F > 0, R1 > 0, R2 > 0, m1 == F * R1 ** 3 * pr1,
               m2 == F * R2 ** 3 * pr2, m1 < 0, m2 > 0))
    # DRIFT B2 WAS THE THIRD MUTATION ROW'S FORMULA, VERBATIM, COUNTED ONCE IN
    # THE DRIFT BUCKET AND ONCE IN THE MUTATION BUCKET.  The file disclosed the
    # duplication in the mutation's own label and still counted it twice.  The
    # mutation row keeps the formula, because that bucket's job is to show the
    # layer is not entirely sign-blind; family B's drift probe becomes one that
    # probes B's OWN encoding -- that MASTER's four corrections are genuinely
    # free, so two states may share R and p_r and differ in m.
    sat("DRIFT B2  K IS A GENUINE DEGREE OF FREEDOM IN MASTER: two states share "
        "R, p_r, C, I_Theta and J, differ only in K, and therefore differ in m "
        "-- goes unsat the moment K is dropped from the master formula",
        z3.And(MASTERg(m1, Cc, I_Th, J, K), MASTERg(m2, Cc, I_Th, J, K2),
               K != K2, m1 != m2))
    sat("DRIFT B3  THE IDENTITY DOES THE WORK: keep F > 0 and R > 0 but drop the "
        "link, and m < 0 with p_r > 0 is immediately satisfiable",
        z3.And(F > 0, R > 0, m < 0, pr > 0))

    # ------------------------------------------------------ C  tracelessness
    def TRACEg(mv, it):
        return z3.And(F > 0, R > 0, mv == F * R ** 3 * pr - it)

    TRACE = TRACEg(m, I_Th)
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
    sat("DRIFT C2  I_Theta GENUINELY MOVES m: two TRACE states, built from the "
        "SAME encoding, share R and p_r, differ in I_Theta, and therefore "
        "differ in m -- goes unsat the moment the trace term is dropped",
        z3.And(TRACEg(m1, I_Th), TRACEg(m2, I_uTh), I_Th != I_uTh, m1 != m2))

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
    sat("D5  ISOLATION, AND THE HONEST ANSWER IS SAT: zeroing C ALONE, with "
        "I_Theta, J and K left FREE, does NOT restore the biconditional",
        z3.And(MASTER, Cc == 0, m < 0, pr > 0))
    sat("D6  REGULAR CENTRE IS NECESSARY: C != 0 gives p_r < 0 with m > 0",
        z3.And(MASTER, I_Th == 0, J == 0, K == 0, Cc != 0, pr < 0, m > 0))
    sat("D7  RN EXACTLY, regulated at eps: m = F q (1/eps - 1/R) > 0, p_r < 0",
        z3.And(F > 0, q > 0, eps > 0, R > eps, m * eps * R == F * q * (R - eps),
               pr * R ** 4 == -q, m > 0, pr < 0))
    sat("DRIFT D   a REGULAR traceless conserved profile must still exist",
        z3.And(LOCAL, dpr == 0, u == 3 * pr, Th == 0, pr != 0))
    Cc2 = z3.Real("C2")
    sat("DRIFT D2  C IS A GENUINE DEGREE OF FREEDOM IN MASTER, which is what "
        "makes the regular centre a HYPOTHESIS: two states share R, p_r, "
        "I_Theta, J and K, differ only in C, and therefore differ in m",
        z3.And(MASTERg(m1, Cc, I_Th, J, K), MASTERg(m2, Cc2, I_Th, J, K),
               Cc != Cc2, m1 != m2))

    # -------------------------------------------- E  staticity and the flux
    def LOCALJg(jv, dv):
        return z3.And(r > 0, r * jv + r * dv + 2 * (pr - pt) == 0,
                      Th == -u + pr + 2 * pt)

    LOCALJ = LOCALJg(jj, dpr)
    sat("GUARD E0  LOCALJ is satisfiable", LOCALJ)
    sat("GUARD E1  LOCALJ with j != 0 is satisfiable", z3.And(LOCALJ, jj != 0))
    ob("E1  j = 0 recovers the flat static identity exactly",
       z3.And(LOCALJ, jj == 0), D == r * r * (u + Th))
    ob("E2  THE EXACT FLUX-CARRYING LOCAL IDENTITY",
       LOCALJ, D == r * r * (u + Th) - r ** 3 * jj)
    ob("E3  THE HYPOTHESIS USED IS d_t T^t_r = 0, NOT STATICITY",
       z3.And(LOCALJ, jj == 0, Th == 0), D == r * r * u)
    sat("E4  ISOLATION: zeroing J ALONE, with C, I_Theta and K FREE, does NOT "
        "restore the biconditional either",
        z3.And(MASTER, J == 0, m < 0, pr > 0))
    sat("E5  STATICITY IS LOAD-BEARING: J != 0 gives m < 0 with p_r > 0",
        z3.And(MASTER, Cc == 0, I_Th == 0, K == 0, J != 0, m < 0, pr > 0))
    sat("E6  W7 EXACTLY: p_r = 1, R = 1, J = -2F gives m = -F < 0",
        z3.And(MASTER, R == 1, pr == 1, Cc == 0, I_Th == 0, K == 0,
               J == -2 * F, m == -F, m < 0, pr > 0))
    # DRIFT E WAS z3-EQUIVALENT TO GUARD E1 -- under LOCALJ with r > 0 and
    # j != 0 the extra conjunct is ENTAILED, so the probe added nothing its own
    # guard did not already have.  Measured: flipping the LOCALJ flux sign turned
    # E1, E2 and E3 red while DRIFT E stayed green.  Replaced by a probe the
    # guard does NOT entail -- that LOCALJ admits two states agreeing on
    # r, p_r, p_t and differing in j, i.e. that j is a genuine extra degree of
    # freedom rather than a function of the others.
    jj2, dpr3 = z3.Reals("j2 dp_r3")
    sat("DRIFT E   j IS NOT DETERMINED BY THE PROFILE VALUES: two LOCALJ states "
        "built from the SAME encoding share r, p_r and p_t yet differ in j -- "
        "only the PAIR (j, p_r') is fixed, which is exactly why 'stationary "
        "flux' is a hypothesis, and dropping the flux term turns this unsat",
        z3.And(LOCALJg(jj, dpr), LOCALJg(jj2, dpr3), jj != jj2, dpr != dpr3))

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
    sat("DRIFT F3  THE LAUE MOMENTS ARE GENUINELY INDEPENDENT: LAUE admits "
        "I_xx != I_yy, so nothing in the encoding has quietly made the source "
        "axisymmetric",
        z3.And(LAUE, Ixx != Iyy))

    # --------------------------------- G  u is neither necessary nor sufficient
    sat("GUARD G0  FULL with u free is satisfiable", z3.And(FULL, u != 0))
    ob("G1  THE IDENTITY DOES NOT MENTION u: same F, R, p_r => same m",
       z3.And(F > 0, R > 0, m1 == F * R ** 3 * pr, m2 == F * R ** 3 * pr, u != u2),
       m1 == m2)
    # G2/G3's LABELS ARE NARROWED TO WHAT THEY PROVE.  The rows contain NO
    # variable u and no power law -- their whole captured footprint is
    # {A, F, P, m, s} -- so "u < 0 throughout implies m < 0" was a strong label
    # on the thin claim "a negative times two positives is negative".  The
    # load-bearing physics, that integrating a negative u over a ball yields a
    # negative A, is ASSERTED in the hypothesis as s*A < 0 and is nowhere
    # established here.  It is CITED (monotonicity of an integral), refusal 5.
    #
    # REFUSED, AND WHY.  The adversarial pass offered a second route: "declare A
    # as an integral surrogate and add the monotonicity constraint that makes
    # A < 0 follow from u < 0".  REFUSED.  That constraint IS the claim.  Adding
    # it would put the physics into the encoding and then report the encoding
    # back as a theorem -- precisely refusal 1's fault, and precisely how
    # Phi_p = 0 passed as a hypothesis for the length of a draft.  z3 has no
    # integral and cannot acquire one by being told the answer.  The honest move
    # is the one taken: narrow the LABEL to the GIVEN, and keep DRIFT G2 to show
    # that without the GIVEN the conclusion fails.  The integral step stays
    # CITED in refusal 5 where a reader will look for it.
    def POWG(mv):
        return z3.And(F > 0, Pp > 0, ss > 0, mv == F * Aa * Pp)

    ob("G2  GIVEN that the power-law integral A carries u's sign (s*A < 0, CITED "
       "not proved here), m carries it too",
       z3.And(POWG(m), ss * Aa < 0), m < 0)
    ob("G3  G2's CONTRAPOSITIVE, under the same GIVEN: m >= 0 forces s*A >= 0",
       z3.And(POWG(m), m >= 0), ss * Aa >= 0)
    sat("DRIFT G2  AND THE GIVEN IS LOAD-BEARING: WITHOUT the s*A < 0 link, "
        "m > 0 is satisfiable on the very same family -- so G2's hypothesis is "
        "doing the work, and baking it into the encoding turns this unsat",
        z3.And(POWG(m), m > 0))
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
    # H1 DELETED: identical hypothesis to B1/B3 and its conclusion is entailed by
    # B3's, as CONTAINMENT machine-checks.  The p_r = 0 radius keeps H2-H5, which
    # say things B3 does not.
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
    sat("DRIFT H2  GRR is a GENUINE constraint and not a tautology: it admits "
        "g_rr != 1, so H4's g_rr = 1 is earned by m = 0 rather than built in",
        z3.And(GRR, grr != 1))

    # -------------------------------------------- I  flat versus GR background
    LOCALGR = z3.And(r > 0, r * dpr + 2 * (pr - pt) + r * Phip * (u + pr) == 0,
                     Th == -u + pr + 2 * pt)
    sat("GUARD I0  LOCALGR is satisfiable", LOCALGR)
    sat("GUARD I1  LOCALGR with Phi' != 0 is satisfiable", z3.And(LOCALGR, Phip != 0))
    ob("I1  THE EXACT GR LOCAL IDENTITY, areal-radius gauge",
       LOCALGR, D == r * r * (u + Th) - r ** 3 * Phip * (u + pr))
    # I2 IS KEPT AND ITS LABEL IS NARROWED.  REFUSED, AND WHY: the adversarial
    # pass asked for I2 to be "re-read as the emptiness result".  REFUSED.  I2 is
    # a TRUE statement about the LOCAL conservation algebra with Phi_p a free
    # parameter, and that algebra is exactly what the TEST-FIELD reading uses --
    # it is the row that licenses the instrument's actual domain.  Re-reading a
    # true row as a false one would manufacture a mislabelled obligation, which
    # is the very fault section 10 already records three of.  What was wrong was
    # never I2; it was that NOTHING linked Phi_p to the field equation, so I2 was
    # quoted as licensing the SOURCED reading too.  The emptiness is therefore a
    # NEW row (I7), not a re-reading of an old one.
    ob("I2  Phi' = 0 recovers the flat identity exactly -- TRUE OF THE LOCAL "
       "ALGEBRA, and it does NOT license the sourced reading (see I7)",
       z3.And(LOCALGR, Phip == 0), D == r * r * (u + Th))
    ob("I4  THE CORRECTION VANISHES IFF u + p_r = 0, WHICH FORCES r u' + 4u = 0",
       z3.And(LOCALGR, Th == 0, u + pr == 0, du == -dpr), r * du + 4 * u == 0)
    ob("I5  ... and RN satisfies that ODE",
       z3.And(r > 0, q > 0, w * r ** 4 == q, u == w, du * r ** 5 == -4 * q),
       r * du + 4 * u == 0)
    sat("I6  FLAT BACKGROUND IS LOAD-BEARING: K != 0 gives m < 0 with p_r > 0",
        z3.And(MASTER, Cc == 0, I_Th == 0, J == 0, K != 0, m < 0, pr > 0))
    sat("DRIFT I   Phi' genuinely changes the local identity",
        z3.And(LOCALGR, Phip != 0, D != r * r * (u + Th)))

    # ------- THE LINK FAMILY I NEVER HAD.  Phi_p was a FREE real: nothing tied
    # it to the COMPUTED G^r_r.  One line of encoding separated a green guard
    # from an emptiness proof.  Section 3a.
    def EINSTEINg(phv):
        return z3.And(F > 0, r - 2 * m > 0,
                      phv * r * (r - 2 * m) == m + F * r ** 3 * pr)

    EINSTEIN = EINSTEINg(Phip)
    sat("GUARD I2s  the G^r_r link is itself satisfiable", EINSTEIN)
    ob("I7  CONDITION (i) IS IMPOSSIBLE: under G^r_r, Phi' = 0 AND the identity "
       "m = F r^3 p_r force m == 0 -- the draft's exactness route is EMPTY",
       z3.And(EINSTEIN, LOCALGR, Phip == 0, m == F * r ** 3 * pr), m == 0)
    ob("I8  ... and p_r == 0 with it, so the class is the vacuum and nothing else",
       z3.And(EINSTEIN, LOCALGR, Phip == 0, m == F * r ** 3 * pr), pr == 0)
    sat("DRIFT X   WITHOUT the G^r_r link the SAME query is satisfiable -- kept "
        "as a standing record of exactly what the omission permitted",
        z3.And(LOCALGR, Phip == 0, m == F * r ** 3 * pr, m != 0, F > 0))

    # ------------------------------ X  THEOREM X, THE EMPTINESS OF SOURCED H
    HX = z3.And(r > 0, EINSTEINg(Phip),
                r * dpr + 2 * (pr - pt) + r * Phip * (u + pr) == 0,
                Th == 0, Th == -u + pr + 2 * pt,
                u == 3 * pr + r * dpr,
                m == F * r ** 3 * pr)
    sat("GUARD X0  THEOREM X's hypothesis set is SATISFIABLE -- so the emptiness "
        "below is a real derivation and not a vacuous one", HX)
    ob("X1  THEOREM X: sourced H forces (u + p_r) * m == 0 POINTWISE", HX,
       (u + pr) * m == 0)
    ob("X2  ... and Phi' vanishes exactly where m does", HX, (Phip == 0) == (m == 0))
    sat("X3  THE ONLY ESCAPE IS u + p_r = 0, i.e. RN: sourced H with BOTH "
        "u + p_r != 0 and p_r != 0 is UNSATISFIABLE",
        z3.And(HX, u + pr != 0, pr != 0), want_sat=False)
    sat("DRIFT X2  the sourced encoding is not empty for its OWN sake: built "
        "from the SAME G^r_r generator, drop the identity and a nonzero p_r "
        "with NONZERO Phi' returns -- so I7's emptiness is the identity's "
        "doing and not the encoding's",
        z3.And(r > 0, EINSTEINg(Phip), pr != 0, Phip != 0))

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
        "reverses it -- THE ONE MUTATION THAT DOES BITE",
        z3.And(F < 0, R > 0, m == F * R ** 3 * pr, m < 0, pr > 0))

    # ------------------------------------- L  the von Laue total-mass corollary
    def CUTG(mv, prv):
        return z3.And(F > 0, Rc > 0, mv == F * Rc ** 3 * prv)

    sat("GUARD L0  the corollary's premise set is satisfiable", CUTG(m, pr))
    # L1's LABEL IS NARROWED AND L2 IS DELETED.  L2 was L1 with m renamed to
    # I_uTh -- alpha-equivalent under that substitution, hypothesis and
    # conclusion both, machine-checked -- so it was one obligation counted twice
    # under two labels.  And L1's own load-bearing step, that a BOUNDED source
    # has p_r = 0 at the cut, is the HYPOTHESIS here, not a result: it comes from
    # the matching condition [P_r]_Sigma = 0, which is CITED (Herrera
    # arXiv:1801.08358 eq. (22), read at source) and is not proved in this layer.
    ob("L1  GIVEN p_r = 0 at the cut (CITED: the matching condition [P_r]_Sigma "
       "= 0; NOT proved here), a traceless conserved static regular source has "
       "m = 0 EXACTLY -- which is von Laue for the total mass",
       z3.And(CUTG(m, pr), pr == 0), m == 0)
    sat("DRIFT L   an UNBOUNDED source (p_r != 0 at the cut) may have m != 0",
        z3.And(CUTG(m, pr), pr != 0, m != 0))
    sat("DRIFT L2  AND THE CUT CONDITION IS LOAD-BEARING, NOT DECORATIVE: with "
        "p_r at the cut left FREE, m == 0 is not forced -- built from the SAME "
        "premise generator, so baking p_r = 0 into it turns this unsat",
        z3.And(CUTG(m, pr), m != 0))
    return out


# =============================================================== status lines

VERDICT = ("RESTATES certify.py ON A STRICTLY SMALLER CLASS -- CHEAPER WHERE "
           "BOTH APPLY, AND NO GATE MOVES")
SUPERSEDES_CERTIFY = False
RESTATES_CERTIFY_ON_SMALLER_CLASS = True
CLASS_IS_A_PROPER_SUBSET = True
HYPOTHESES_ADDED = ("T^mu_mu = 0 exactly, and a TEST-FIELD BACKGROUND -- the "
                    "background metric fixed and NOT sourced by this T.  The "
                    "draft wrote \"a flat background (Phi' = 0, or the weaker "
                    "sufficient condition u + p_r = 0)\"; Phi' = 0 is WITHDRAWN "
                    "by THEOREM X and u + p_r = 0 is excluded by the regular "
                    "centre, so neither names a nonempty sourced class")
IDENTITY_IS_EXACT_IN_FLAT_SPACE_ONLY = True
CURVED_CORRECTION = "K = 4 pi INT_0^R r^3 (u + p_r) Phi' dr"
CURVED_CORRECTION_VANISHES_IFF = (
    "pointwise, (u + p_r) Phi' = 0.  ON A SOURCED GEOMETRY that leaves only "
    "u + p_r = 0 -- the saturated radial NEC, hence RN, hence excluded by the "
    "regular centre -- because Phi' = 0 there forces 4 pi r^3 p_r = -m, the "
    "OPPOSITE sign to the identity (THEOREM X).  On the TEST-FIELD reading the "
    "term is absent by construction and delta bounds the join")
ONLY_TRACELESS_CONSERVED_SOURCE_WITH_U_PLUS_PR_ZERO = "Reissner-Nordstrom"
INTEGRATION_CONSTANT_IS_A_LIMIT_OF_M = False
INTEGRATION_CONSTANT_IS = "the renormalised CENTRAL MASS, a first integral"
REGULAR_CENTRE_IS_LOAD_BEARING = True
TRACELESSNESS_IS_LOAD_BEARING = True
BACKGROUND_HYPOTHESIS_IS_LOAD_BEARING = True
BACKGROUND_HYPOTHESIS = "test-field: the background is FIXED and not sourced by T"
EXACTLY_SOURCED_CLASS_IS_EMPTY = True      # THEOREM X, section 3a
PHI_PRIME_ZERO_IS_AN_EXACTNESS_ROUTE = False   # WITHDRAWN: it is the wormhole branch
ONLY_LOCAL_EXACTNESS_CONDITION = "u + p_r = 0, which the regular centre excludes"
P_R_IS_A_SCALAR_UNDER_H = False            # WITHDRAWN: determined by one, not one
HEADLINE_FRAME = "the KILLING frame, and the headline carries it explicitly"
M0_AND_R3PR_ARE_THE_SAME_HYPOTHESIS = False    # WITHDRAWN: independent, V32
POSITIVE_CONTROL_IS_TEST_FIELD_ONLY = True     # V30
ONE_EVALUATION_INSTEAD_OF_A_QUADRATURE = False # only GIVEN two a-priori bounds
JOIN_TO_GEOMETRY_IS_EXACT = False              # WITHDRAWN: delta is the join
SOURCE_SPHERICITY_IS_LOAD_BEARING = False
READ_DIRECTION_SPHERICITY_IS_LOAD_BEARING = True
STATICITY_IS_THE_RIGHT_NAME = False
HYPOTHESIS_ACTUALLY_USED_OFF_STATICITY = "d_t T^t_r = 0 -- a STATIONARY flux"
NONSTATIC_BRANCH_IS_CLOSED = False
U_AT_R_IS_NECESSARY = False
U_AT_R_IS_SUFFICIENT = False
TEST_QUANTITY = "the ANGULAR AVERAGE <T^r_r(R)>, never a single component"
VERIFY_HAS_A_NONZERO_ROW = True        # V33; every other row asserts exactly 0
RESIDUAL_COUNT = 37                    # --verify rows; V33 is the ONE that must be nonzero
OBLIGATION_COMPOSITION = {             # --prove rows, and the shape is pinned
    "theorem, negated -> unsat, own hypothesis sat": 38,
    "family satisfiability guard (sat)": 22,
    "encoding-drift probe (sat)": 22,
    "necessity witness (sat)": 16,
    "mutation probe": 3,
    "over-representation containment (measured)": 1,
}
OBLIGATION_COUNT = 102
# WAS 39/20/14/14/3 = 90.  The theorem bucket FELL by one although family X and
# I7/I8 added four, because FIVE rows were deleted as over-representation: B2,
# D5, E4, H1 and I3 shared the identical hypothesis FULL with B1 and had
# conclusions all entailed by B3's, and L2 was L1 alpha-renamed.  Six labels,
# two theorems.  The CONTAINMENT row now machine-checks that entailment, so the
# reduction is a recorded measurement rather than a quiet deletion.  D5 and E4
# survive as ISOLATION rows that leave the other corrections FREE and come out
# SAT -- which is what their old labels had always claimed and never tested.
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
SCOPE = ("TEST-FIELD-background traceless conserved spherically symmetric "
         "sources with a regular centre and a stationary radial flux, read in "
         "the KILLING frame; nothing non-spherical, nothing with a trace "
         "anomaly, nothing about the deep interior, and NOTHING SOURCED -- "
         "THEOREM X shows the exactly-sourced class is empty")
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
     "CITED", "read at source by the prior-art pass AND re-read at source by "
              "the repair pass; re-derived here, V20 = 0"),
    ("Herrera, arXiv:1801.08358v2 eq. (10) -- nu' = 2(m + 4pi P_r r^3)/(r(r-2m))",
     "CITED", "read at source by the repair pass; THE FIELD EQUATION THEOREM X "
              "TURNS ON, and the reason condition (i) is withdrawn"),
    ("Herrera, arXiv:1801.08358v2 eq. (22) -- the Darmois matching [P_r]_Sigma = 0",
     "CITED", "read at source by the repair pass; eqs (20)-(22) are stated "
              "there as necessary AND sufficient for a smooth match.  It is "
              "obligation L1's GIVEN, and L1 does not prove it"),
    ("Herrera & Di Prisco, arXiv:gr-qc/9810020 eq. (39) -- the time-dependent form",
     "CITED", "read at source by the prior-art pass and re-read at source by "
              "the audit pass, which found the 'itself restating' slip section "
              "1 now withdraws; NOT re-opened by the repair pass"),
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
    ("certify.py COROLLARY (m = INT 4 pi r'^2 rho, needing m(0) = 0)",
     "CONFIRMED-AND-DISTINGUISHED",
     "THE DRAFT'S 'ONE FACT SEEN TWICE' IS WITHDRAWN.  Both hypotheses kill "
     "the integration constant of a FIRST-ORDER ODE at r = 0, and RN breaks "
     "both simultaneously in the same region -- but they are constants of "
     "DIFFERENT ODEs and NEITHER IMPLIES THE OTHER.  The separating witness is "
     "exact and seated as `independence_witness` (V32): u == 0, p_r = A/r^3, "
     "p_t = -A/(2r^3) is traceless and conserved with m(R) = 0, so certify.py's "
     "m(0) = 0 HOLDS while C = 4 pi A != 0 and this identity is off by -4 pi A "
     "at every radius.  Converse: C = 0 with a central point mass leaves a "
     "defect m(0).  RN breaks both; that is all RN licenses.  On the class "
     "where both hold the identity is an independent second evaluation of the "
     "same integral, and THAT much the draft had right."),
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

PEER_STATUS_COUNTS = {"UNCHANGED": 12, "CONFIRMED": 3, "CORRECTED": 1,
                      "CONFIRMED-AND-DISTINGUISHED": 1, "NARROWED": 1}


# ==================================================================== selftest

def selftest():
    """STDLIB ONLY plus seated peers of this tree.  sympy and z3 are NOT
    imported here by design: --verify and --prove are the layers that need them,
    and this is the layer that must run anywhere.  Section 10 refusal 9 stands:
    the layers are not redundant and neither may be reported without the other."""
    ok = True
    kinds = {"MEASURED": 0, "DECLARED": 0, "CONSTRUCTION": 0}

    def chk(label, got, want, kind="DECLARED"):
        nonlocal ok
        good = got == want
        ok &= good
        kinds[kind] += 1
        print("  %-62s %-11s %-11s %-4s %s"
              % (label, str(got)[:11], str(want)[:11], KIND_TAG[kind],
                 "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9, scale=None, kind="MEASURED"):
        """RELATIVE against |want|, or against an EXPLICIT scale the caller
        supplies.  A comparison against zero MUST name its scale.

        THE DRAFT'S TOLERANCE WAS `tol * max(1.0, abs(want))`, which silently
        turned every relative tolerance into an ABSOLUTE FLOOR of `tol` whenever
        |want| < 1.  Six fixtures compared kilogram- and dimensionless-scale
        quantities of order 1e-15 to 1e-58 against absolute floors of 1e-14 to
        1e-3, so ZERO PASSED AND SO DID THE SIGN-FLIPPED VALUE.  Measured, not
        inferred: with radiation_mass multiplied by 1e6 the row "the QUADRATURE
        and the POINTWISE read agree exactly" printed -2.019814e-21 against
        -2.019814e-15 and marked it ok.  Sign inversions inside
        tolman_mass_factor (Herrera eq. (32)'s combination, this file's declared
        prior-art parent) and inside first_integral (the function implementing
        the headline claim about C) both survived with exit 0 and nothing red.
        THREE OF THIS FILE'S NAMED QUANTITIES HAD NO EFFECTIVE FLOAT-LAYER TEST.
        `max(1.0, ...)` is gone and a zero-`want` row without a scale is now a
        hard error rather than a pass.

        AND THE REPAIR WAS RE-MUTATED, NOT ASSUMED.  On scratchpad copies, the
        original byte-unchanged and no peer edited: chi_compactness 2 -> 3 now
        turns 1 row red; the tolman_mass_factor sign flip 3 rows; the
        first_integral sign flip 1 row; radiation_mass x 1e6 2 rows, AND SO DOES
        radiation_mass x (1 + 1e-7), which is ten orders of magnitude finer than
        the mutation the draft marked ok.  An enclosed_mass sign flip turns 10
        red.  All five exit 1."""
        nonlocal ok
        if scale is None:
            if want == 0.0:
                raise ValueError(
                    "near(%r): want == 0 requires an explicit scale=; an "
                    "absolute floor is not a tolerance" % label)
            denom = abs(want)
        else:
            denom = abs(scale)
            if denom == 0.0:
                raise ValueError("near(%r): scale must be nonzero" % label)
        good = abs(got - want) <= tol * denom
        ok &= good
        kinds[kind] += 1
        print("  %-62s %12.6g %12.6g %-4s %s"
              % (label, got, want, KIND_TAG[kind], "ok" if good else "FAIL"))

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
    chk("  nothing is repaired, and no peer is edited",
        (NOTHING_IS_REPAIRED, NO_PEER_IS_EDITED), (True, True))

    print("\n0b. THE CLAIMS THIS FILE WITHDREW, PINNED SO THEY CANNOT CREEP BACK")
    chk("  the exactly-SOURCED class is EMPTY (THEOREM X)",
        EXACTLY_SOURCED_CLASS_IS_EMPTY, True)
    chk("  Phi' = 0 is NOT an exactness route -- it is the wormhole branch",
        PHI_PRIME_ZERO_IS_AN_EXACTNESS_ROUTE, False)
    chk("  exactly ONE local exactness condition survives",
        ONLY_LOCAL_EXACTNESS_CONDITION.startswith("u + p_r = 0"), True)
    chk("  p_r is NOT a scalar under H, only determined by one",
        P_R_IS_A_SCALAR_UNDER_H, False)
    chk("  so the headline carries its frame", "KILLING" in HEADLINE_FRAME, True)
    chk("  m(0) = 0 and r^3 p_r -> 0 are NOT the same hypothesis",
        M0_AND_R3PR_ARE_THE_SAME_HYPOTHESIS, False)
    chk("  the economy is not 'one evaluation instead of a quadrature'",
        ONE_EVALUATION_INSTEAD_OF_A_QUADRATURE, False)
    chk("  and the join to the geometry is NOT exact -- delta is the join",
        JOIN_TO_GEOMETRY_IS_EXACT, False)

    print("\n0c. THE WITNESSES THOSE WITHDRAWALS REST ON, MEASURED HERE")
    # THEOREM X, in floats, from the module's own dPhi_sourced: impose the
    # identity and the TOV residual must collapse to (u + p_r) Phi'.
    for rr, pp in ((0.7, -0.03), (1.3, 0.011), (2.0, -0.004)):
        mm = 4.0 * math.pi * rr ** 3 * pp
        dpr_ = 0.25
        uu = 3.0 * pp + rr * dpr_
        ptt = pp + rr * dpr_ / 2.0
        dph = dPhi_sourced(mm, rr, pp)
        near("  THEOREM X at r = %g: TOV residual == (u + p_r) Phi'" % rr,
             tov_residual(uu, pp, ptt, dpr_, rr, dph), (uu + pp) * dph,
             1e-12, scale=max(abs((uu + pp) * dph), 1e-300), kind="MEASURED")
    near("  and Phi' = 0 forces 4 pi r^3 p_r = -m, the OPPOSITE sign",
         dPhi_sourced(-4.0 * math.pi * 1.5 ** 3 * (-0.02), 1.5, -0.02), 0.0,
         1e-12, scale=1.0, kind="MEASURED")
    prb, ub, ptb = boost_witness(Fr(9, 10))
    chk("  THE BOOST WITNESS is traceless and conserved, exactly",
        (trace_residual(ub, prb, ptb),
         conservation_residual(prb, 6 * Fr(9, 10) ** 5, ptb, Fr(9, 10))),
        (Fr(0), Fr(0)), kind="MEASURED")
    pf, uf = float(prb), float(ub)
    chk("  ... its Killing-frame p_r is a TENSION at R = 9/10", pf < 0.0, True,
        kind="MEASURED")
    wc = critical_rapidity(uf, pf)
    near("  ... and the critical rapidity is 0.566301", wc, 0.566301, 1e-5,
         kind="MEASURED")
    chk("  ... ABOVE WHICH THE SAME EVENT READS A PRESSURE: p_r is GAUGE",
        (boost_radial_stress(uf, pf, 0.80) > 0.0
         and boost_radial_stress(uf, pf, 1.20) > 0.0), True, kind="MEASURED")
    mB = 4.0 * math.pi * 0.9 ** 3 * pf
    near("  ... while 1 - 2m/R, a SCALAR, does not move: 10.538699",
         1.0 - 2.0 * mB / 0.9, 10.538699, 1e-6, kind="MEASURED")
    prI, uI, ptI, CI = independence_witness(Fr(1, 2))
    chk("  THE SEPARATING WITNESS is traceless and conserved, exactly",
        (trace_residual(uI, prI, ptI),
         conservation_residual(prI, -3 * Fr(1) / Fr(1, 2) ** 4, ptI, Fr(1, 2))),
        (Fr(0), Fr(0)), kind="MEASURED")
    chk("  ... u == 0 so m(R) == 0: certify.py's m(0) = 0 HOLDS", uI, Fr(0),
        kind="MEASURED")
    chk("  ... while C/(4 pi) = A != 0: THIS identity's hypothesis FAILS",
        CI != 0, True, kind="MEASURED")
    chk("  ... so neither implies the other, and they are NOT one fact twice",
        M0_AND_R3PR_ARE_THE_SAME_HYPOTHESIS, False)

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
             radial_stress_for_mass(m, R), p, kind="CONSTRUCTION")
    # BOTH ROWS BELOW USED TO COMPARE AGAINST A BARE 0.0 OR A SUB-UNIT VALUE
    # UNDER AN ABSOLUTE FLOOR, so a sign inversion inside either function passed
    # with nothing red.  They now carry an explicit scale and a second, MEASURED
    # reading that a sign flip cannot survive.
    m7 = enclosed_mass(1.0, -7.0)
    near("  the Tolman combination is exactly 2m on the identity",
         tolman_mass_factor(m7, 1.0, -7.0), 2.0 * m7, scale=abs(m7),
         kind="CONSTRUCTION")
    chk("  ... and its SIGN is the sign of m, which a flip would invert",
        tolman_mass_factor(m7, 1.0, -7.0) < 0.0, True, kind="MEASURED")
    near("  ... and it is +2m for a pressure, not -2m",
         tolman_mass_factor(enclosed_mass(1.0, +7.0), 1.0, +7.0)
         / enclosed_mass(1.0, +7.0), 2.0, kind="MEASURED")
    m3 = enclosed_mass(3.0, -2.0)
    near("  the first integral is 0 on the identity, AGAINST THE TERM SCALE",
         first_integral(m3, 3.0, -2.0), 0.0, scale=abs(m3), kind="CONSTRUCTION")
    near("  ... and it is EXACTLY the centre term when one is present: C = m(0)",
         first_integral(m3 + 5.0, 3.0, -2.0), 5.0, kind="MEASURED")
    near("  ... and it is NOT sign-degenerate: -5 for the other polarity",
         first_integral(m3 - 5.0, 3.0, -2.0), -5.0, kind="MEASURED")

    print("\n4. REISSNER-NORDSTROM -- EXACT RATIONAL ARITHMETIC, NO FLOATS")
    print("     %8s %18s %14s %10s" % ("R", "4 pi R^3 p_r", "m(R)", "defect"))
    defects = []
    for R in ("1/20", "1/10", "1/5", "8/25", "2/5", "1/2", "1", "8/5", "5", "100"):
        f3, m, d = rn_row(Fr(R))
        defects.append(d)
        print("     %8s %18s %14s %10s"
              % (R, str(float(f3))[:16], str(float(m))[:12], str(d)))
    chk("  the defect is EXACTLY M = 1 at every radius, as a Fraction",
        set(defects), {Fr(1)}, kind="CONSTRUCTION")
    chk("  ... and the SAME defect for an independent (M, Q) -- M = 7/3",
        set(rn_row(Fr(R), M=Fr(7, 3), Q2=Fr(9, 16))[2]
            for R in ("1/7", "1/2", "3", "40")), {Fr(7, 3)}, kind="MEASURED")
    chk("  m = 0 exactly at R = Q^2/2M = 8/25", rn_sign_radius(), Fr(8, 25),
        kind="CONSTRUCTION")
    chk("  ... and at 9/56 for the independent pair, tracking Q^2/2M",
        rn_sign_radius(M=Fr(7, 3), Q2=Fr(9, 16)), Fr(27, 224), kind="MEASURED")
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
         plate_trace_residual(d) / u0, 0.0, 1e-14, scale=1.0,
         kind="CONSTRUCTION")
    rho, pz, ptr = plate_cell(d)
    near("  p_normal/u_0 = -3, DERIVED from F = -d(E/A)/dd", pz / u0, -3.0,
         kind="CONSTRUCTION")
    near("  rho/u_0 = -1", rho / u0, -1.0, kind="CONSTRUCTION")
    near("  p_transverse/u_0 = +1, FORCED by tracelessness", ptr / u0, +1.0,
         kind="CONSTRUCTION")
    chk("  BOTH have the right sign simultaneously (the ruling's check)",
        (rho < 0.0 and pz < 0.0), True, kind="MEASURED")
    e, pr_i, pt_i = isotropic_average(d)
    near("  POSITIVE CONTROL: isotropic average is traceless (residual/u_0)",
         trace_residual(e, pr_i, pt_i) / u0, 0.0, 1e-14, scale=1.0,
         kind="CONSTRUCTION")
    m_quad = radiation_mass(R, u0, -1.0)
    m_ident = enclosed_mass(R, pr_i)
    near("  and the QUADRATURE and the POINTWISE read agree exactly",
         m_ident, m_quad, 1e-14, kind="MEASURED")
    chk("  VERDICT YES", pointwise_test(pr_i, R, **all_hypotheses())[0], "YES")
    print("     u_0 = %.6e J/m^3   p_r = %.6e Pa   m = %.6e kg"
          % (u0, pr_i, m_ident))
    near("  ... and m cross-checks the derivation pass's -2.019814e-21 kg",
         m_ident, -2.019814e-21, 1e-4, kind="MEASURED")
    near("  THE MAGNITUDE ERROR IF THE RAW CELL IS READ AS p_r: a factor 9",
         enclosed_mass(R, pz) / m_quad, 9.0, kind="MEASURED")
    # NEGATIVE CONTROL (a) NOW COMES FROM THE MODULE, not from a literal triple
    # written in this function.  While it was inline its tracelessness half
    # could not fail whatever the module did; only its VERDICT half was live.
    e2, pr2_, pt2_ = isotropic_average_mirror(d)
    near("  NEGATIVE CONTROL (a): the exact mirror is traceless (residual/u_0)",
         trace_residual(e2, pr2_, pt2_) / u0, 0.0, 1e-14, scale=1.0,
         kind="MEASURED")
    chk("  ... and it IS the mirror of the module's own positive control",
        (e2, pr2_, pt2_) == tuple(-x for x in isotropic_average(d)), True,
        kind="MEASURED")
    chk("  VERDICT NO", pointwise_test(pr2_, R, **all_hypotheses())[0], "NO",
        kind="MEASURED")
    near("  and its mass is the exact mirror too",
         enclosed_mass(R, pr2_), -m_ident, 1e-14, kind="CONSTRUCTION")

    print("     -- AND THE POSITIVE CONTROL IS A TEST-FIELD CONTROL (V30)")
    m_pc = -4.0 * math.pi * R ** 3 * u0 / 3.0 / (C * C)
    # In G = c = 1 the control has m = -4 pi r^3 u_0/3 and p_r = -u_0/3, so
    # Phi' = 2m/(r(r-2m)) is nonzero for every u_0 > 0, and the exact TOV
    # residual (u + p_r) Phi' = (-4 u_0/3) Phi' is STRICTLY POSITIVE.
    u0g = 1.0e-3                       # geometric units; the sign is the point
    r_g = 1.0
    m_g = -4.0 * math.pi * r_g ** 3 * u0g / 3.0
    phi_g = dPhi_sourced(m_g, r_g, -u0g / 3.0)
    chk("  its Phi' from the COMPUTED G^r_r is NONZERO: it does NOT source the "
        "geometry it is credited with", phi_g != 0.0, True, kind="MEASURED")
    near("  ... and Phi' = 2m/(r(r-2m)) exactly, m being negative here",
         phi_g, 2.0 * m_g / (r_g * (r_g - 2.0 * m_g)), kind="MEASURED")
    near("  ... so its exact TOV residual is 32 pi r u_0^2/(3(8 pi r^2 u_0 + 3))"
         ", STRICTLY POSITIVE (V30)",
         tov_residual(-u0g, -u0g / 3.0, -u0g / 3.0, 0.0, r_g, phi_g),
         32.0 * math.pi * r_g * u0g ** 2
         / (3.0 * (8.0 * math.pi * r_g ** 2 * u0g + 3.0)), 1e-9,
         kind="MEASURED")
    chk("  ... so the hypothesis it is granted is test-field, never sourced",
        POSITIVE_CONTROL_IS_TEST_FIELD_ONLY, True)
    chk("  and the keyword says so", "test_field_background" in HYPOTHESES, True)

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
        mq, Fr(9, 10) ** 3 * prq, kind="CONSTRUCTION")
    # quadratic_profile RETURNS mq ALREADY IN THE SOLVED FORM, so the row above
    # is an identity of its own two lines.  The MEASURED content is that the
    # returned e and p_t are the ones tracelessness and conservation FORCE, and
    # that the quadrature of that e reproduces mq -- checked here in exact
    # Fractions by integrating term by term rather than by reusing the formula.
    Lq, Pq = Fr(1), Fr(1)
    for Rq in (Fr(1, 4), Fr(3, 5), Fr(9, 10)):
        prx, ex, ptx, mx = quadratic_profile(Pq, Lq, Rq)
        quad = Pq * Rq ** 3 - Pq * Rq ** 5 / (Lq * Lq)   # INT r^2 e dr, exact
        chk("  QUADRATURE of the FORCED e reproduces m at R = %s" % Rq,
            quad, mx, kind="MEASURED")
        chk("  ... trace and conservation residuals both exactly 0 there",
            (trace_residual(ex, prx, ptx),
             conservation_residual(prx, -2 * Pq * Rq / (Lq * Lq), ptx, Rq)),
            (Fr(0), Fr(0)), kind="MEASURED")
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
    near("  Morris-Thorne throat: 4 pi r_0^3 p_r = -m", fw, -mw,
         kind="CONSTRUCTION")
    chk("  so the flare-out condition is NOT this identity", fw == -mw, True,
        kind="CONSTRUCTION")
    r0a, ppar, f4, mms = alc_throat(1.0, 0.5)
    near("  Agnese-La Camera eq. (17): 4 pi r_0^3 p_|| = -m_MS", f4, -mms,
         kind="CONSTRUCTION")
    chk("  with m_MS > 0 EVERYWHERE and tension at the throat",
        (mms > 0.0 and ppar < 0.0), True, kind="MEASURED")
    chk("  tracelessness alone does not buy the biconditional",
        TRACELESSNESS_IS_LOAD_BEARING, True)

    print("\n9. THE CURVED-BACKGROUND BOUND")
    near("  delta at eps = l_P is exactly 1/(15 pi)", delta_curved(L_PLANCK),
         1.0 / (15.0 * math.pi), kind="CONSTRUCTION")
    near("  delta = 1 at eps = l_P/sqrt(15 pi)", delta_unity_eps() / L_PLANCK,
         1.0 / math.sqrt(15.0 * math.pi), 1e-14, kind="CONSTRUCTION")
    near("  ... and delta evaluated there is exactly 1",
         delta_curved(delta_unity_eps()), 1.0, 1e-14, kind="CONSTRUCTION")
    # THE DRAFT'S ROW HERE COMPARED delta_curved(1e-9) WITH delta_curved(1e-9)
    # -- THE SAME CALL ON BOTH SIDES.  It could not fail under any mutation
    # whatever, and since `a` never appears in delta_curved's signature the
    # claim in its label was untestable by it.  DELETED.  Replaced by a probe
    # that actually varies a: the FULL V16 integral, quadratured at four shell
    # radii three decades apart, must return the same delta and must agree with
    # the closed form.  On a LOG grid, because the integrand goes as eps^-5 and
    # section 6 records a derivation pass that lost 100 % to a uniform one.
    near("  delta is INDEPENDENT of the shell radius a: the FULL integral at "
         "a = 1 um and a = 1 mm, three decades apart, agrees to 1e-5",
         delta_quadrature(1e-6, 1e-12) / delta_quadrature(1e-3, 1e-12), 1.0,
         1e-5, kind="MEASURED")
    for a_shell in (1e-6, 1e-4, 1e-3):
        near("  ... and the quadrature reproduces the closed form at a = %.0e m"
             % a_shell,
             delta_quadrature(a_shell, 1e-12) / delta_curved(1e-12), 1.0, 1e-5,
             kind="MEASURED")
    near("  and scales as eps^-2 exactly", delta_curved(1e-10) / delta_curved(1e-9),
         100.0, kind="CONSTRUCTION")
    chi = chi_compactness(1.378e-7)
    near("  chi at eps = 137.8 nm against DOCKET 54's banked 5.84e-58", chi,
         5.84e-58, 1e-3)
    print("     delta(137.8 nm) = %.4e   chi = %.4e   (a derivation pass "
          "reported delta = 2.9210e-58)" % (delta_curved(1.378e-7), chi))
    chk("  THE DERIVATION PASSES DISAGREE AT 5.8e-4 AND THE RECOMPUTATION WINS",
        abs(delta_curved(1.378e-7) / 2.9210e-58 - 1.0) < 2e-3, True)
    near("  the profile-free fallback at chi = 5.8386e-58, V/|m| = 3/2, / chi",
         delta_profile_free(chi, 1.5) / chi, 1.5, 1e-9, kind="CONSTRUCTION")
    chk("  which costs a factor 3 against the exact chi/2",
        round(delta_profile_free(chi, 1.5) / (chi / 2.0)), 3)
    near("  the crossover coefficient is 60 sqrt(2) pi/128", crossover_coefficient(),
         60.0 * math.sqrt(2.0) * math.pi / 128.0, kind="CONSTRUCTION")
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
            - crossover_radius(15.3) / skin_depth(15.3)) < 1e-15, True,
        kind="CONSTRUCTION")

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
    chk("  certify.py's COROLLARY is CONFIRMED-AND-DISTINGUISHED, never "
        "superseded and never conflated",
        [s for t, s, _ in PEER_STATUS if t.startswith("certify.py COROLLARY")],
        ["CONFIRMED-AND-DISTINGUISHED"])
    chk("  ... and the two hypotheses are NOT declared the same fact",
        M0_AND_R3PR_ARE_THE_SAME_HYPOTHESIS, False)
    chk("  overturn.py's L4 is UNCHANGED, which is the last word",
        [s for t, s, _ in PEER_STATUS if t.startswith("overturn.py L4")],
        ["UNCHANGED"])
    chk("  the ruling itself is the one CORRECTED row",
        sum(1 for _, s, _ in PEER_STATUS if s == "CORRECTED"), 1)
    chk("  and exactly one row NARROWS this file's own reach",
        sum(1 for _, s, _ in PEER_STATUS if s == "NARROWED"), 1)
    chk("  every row carries a reason", all(bool(w) for _, _, w in PEER_STATUS), True)

    print("\n13. THE REFUSAL SURFACE")
    chk("  the word 'replaces' is refused", "replaces" in REFUSED, True)
    chk("  the background hypothesis is named in the scope, and it is the "
        "TEST-FIELD one", "TEST-FIELD-background" in SCOPE, True)
    chk("  ... and the scope says outright that nothing sourced is in it",
        "NOTHING SOURCED" in SCOPE, True)
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
        sum(OBLIGATION_COMPOSITION.values()), OBLIGATION_COUNT,
        kind="CONSTRUCTION")
    chk("  every mutation probe is counted as a probe, never as a theorem",
        classify_row("MUTATION  R^3 -> R^2 ..."), "mutation probe",
        kind="CONSTRUCTION")
    chk("  and --verify's row count is pinned too", RESIDUAL_COUNT, 37)
    chk("  ... and ONE of those rows is a NEGATIVE control, expected nonzero",
        VERIFY_HAS_A_NONZERO_ROW, True)
    doc_lines = len(__doc__.splitlines())
    peer_lines = len(foliation.__doc__.splitlines())
    chk("  THE SIZE COST, MEASURED NOT DESCRIBED: this docstring is under its "
        "declared ceiling", doc_lines <= DOCSTRING_LINE_CEILING, True,
        kind="MEASURED")
    print("     docstring %d lines against foliation.py's %d -- ratio %.2f, "
          "and section 12 refuses to call that a virtue"
          % (doc_lines, peer_lines, doc_lines / float(peer_lines)))
    chk("  ... and the ratio to the largest peer is over 2, which is the "
        "finding rather than the defence",
        doc_lines > 2 * peer_lines, True, kind="MEASURED")

    # THE CENSUS COUNTS ITS OWN TWO ROWS.  A census printed before the rows
    # that pin it is a census of all-but-two of the run, and the pin would then
    # be a number about a set nobody can see.  The two below are DECLARED and
    # are added in advance.
    census = dict(kinds)
    census["DECLARED"] += 2
    total = sum(census.values())
    print("\n14. WHAT ALL %d ROWS OF THIS RUN ACTUALLY ARE -- THE KIND CENSUS"
          % total)
    for k in ("MEASURED", "DECLARED", "CONSTRUCTION"):
        print("     %-14s %4d  %s" % (k, census[k], KIND_MEANING[k]))
    print("     %-14s %4d  (the two rows below included in advance)"
          % ("TOTAL", total))
    chk("  the kind census matches its pin, ITS OWN TWO ROWS INCLUDED",
        census, FIXTURE_KINDS)
    chk("  and a CONSTRUCTION row is never counted as evidence",
        CONSTRUCTION_IS_NOT_EVIDENCE, True)

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
    print("  HYPOTHESIS.  Inside it, the shortfall is 2.46e+13 [DERIVED].")

    print("\n" + BAR)
    print("PEER STATUS -- RECORDED, NEVER REPAIRED")
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
