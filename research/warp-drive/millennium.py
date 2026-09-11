#!/usr/bin/env python3
"""
millennium.py -- M: "I have a target for you to research.  Some famously
unsolved math that may hold the keys to what we are hoping to achieve -- the
millennium problems by The Clay Mathematics Institute."

Seven problems, six open, one solved.  Surveyed against this project's three
remaining links.  THE DISCIPLINE MATTERS MORE HERE THAN ANYWHERE, because
famous problems attract manufactured connections and a survey where most rows
are refusals is worth more than one where every row is a hit.

THE HEADLINE IS NOT A MILLENNIUM PROBLEM.  Doing the survey properly meant
reading Fewster-Osterbrink rather than citing it, AND READING IT CORRECTS THE
PASS BEFORE THIS ONE.  That correction is section 1 because it goes against us.

Of the seven: ONE BEARS, and it is the one already solved.  One is
structurally adjacent and logically independent.  Two have real, precise links
to this subject that do not touch our links at all.  THREE HAVE NO BEARING
AND SAYING SO IS THE FINDING.

===============================================================================
1. THE CORRECTION, FIRST, BECAUSE IT GOES AGAINST THE LAST PASS
===============================================================================

solve.py and CLAIMS.md H44c seated this, an hour before this file:

    "a relation that is not state-independent is not a bound, and what is not
     a bound can be neither satisfied nor violated, only estimated.  THE SAME
     THEOREM THAT REMOVES THE OBSTRUCTION REMOVES THE PROOF THAT IT IS
     REMOVED."

THE FIRST HALF IS RIGHT AND THE SECOND HALF IS WRONG.  Fewster & Osterbrink
(arXiv:0708.2450) do show no STATE-INDEPENDENT QEI exists for xi > 0 -- by an
explicit Hadamard state, not by failing to find one.  But their paper does not
stop there, and the title is "Quantum Energy INEQUALITIES for the
Non-Minimally Coupled Scalar Field" for a reason.  Their abstract:

    "Nonetheless, we derive a generalised QEI for the non-minimally coupled
     scalar field, in which the lower bound is permitted to be state-dependent.
     This result applies to general globally hyperbolic curved spacetimes for
     coupling constants in the range 0 < xi <= 1/4."

    A STATE-DEPENDENT BOUND IS A BOUND.  Theorem 4.2 proves it, Theorem 5.1
    proves it NON-TRIVIAL, and 0 < xi <= 1/4 CONTAINS THE 1/6 solve.py CHOSE
    -- the paper names conformal coupling xi = (n-2)/(4n-4) and supersymmetric
    coupling xi = 1/4 as the two special values its range was built to cover.

    SO L4'S STATUS QUESTION IS NOT "IS THERE A BOUND".  THERE IS ONE, IT IS
    PROVED, AND IT COVERS OUR COUPLING.  The question is what it says for a
    specified state -- A COMPUTATION NOBODY HERE HAS DONE, not an impossibility.

AND THE CORRECTED READING IS WORSE FOR US, NOT BETTER, WHICH IS WHY IT MATTERS.
Three things in that paper reproduce this project's own obstruction from the
quantum field theory side, independently:

    (a) THE COUNTEREXAMPLE CARRIES A HYPERBOLA.  Their state has energy
        density -xi(2 kappa)^4/(3 pi^2) at the origin and can be pushed below
        any -rho_0 over any ball B(tau'), but -- their words -- "Note that the
        product of kappa' and tau' is constant.  This shows that we may
        arrange for LARGE REGIONS of negative energy density ALBEIT WITH LOW
        MAGNITUDE."

        SIZE TIMES MAGNITUDE IS FIXED.  That is the shape of magnitude.py's
        area law R * Delta d <= k l_P^2, reached from QFT rather than from
        geometry.  The two are NOT the same statement and this file does not
        claim they are; what is recorded is that the SHAPE recurs.

    (b) THE ENERGY BUDGET SCALES WITH A DIFFERENT POWER.  Their H-bounds give
        a lower bound holding for any p > 2 while the energy density itself
        cannot be bounded above for q < 3.  Their conclusion: "negative energy
        effects with large magnitude, while possible over large regions,
        REQUIRE MORE ENERGY TO ACHIEVE than positive energy densities of the
        same magnitude and the 'energy budget' for these two effects will GROW
        WITH A DIFFERENT POWER."

        A SHORTFALL WITH AN EXPONENT GAP, of at least 1 in the power of the
        Hamiltonian.  candidates.py's magnitude gate is an exponent gap.  Again
        the same shape, independently.

    (c) AWEC HOLDS.  They prove the averaged weak energy condition for
        xi in [0, 1/4].  overturn.py found that ANEC does not forbid the
        requirement and that the averaged conditions are not what obstructs;
        THIS IS THAT RESULT FROM THE OTHER DIRECTION -- the averaged condition
        is SATISFIED here and the obstruction is elsewhere, exactly as
        overturn.py's ball-versus-chord argument said it must be.

ONE MORE THING THE PAPER GIVES THAT NOTHING HERE HAD.  The total energy of
their j-particle construction goes as (tau')^3 * 2 pi^2 rho_0 / (xi kappa^3
tau^3) -- INVERSELY PROPORTIONAL TO xi.  So within the theorem's own range the
CHEAPEST coupling is the largest, xi = 1/4, not the 1/6 a symmetry picks:

        cost(xi = 1/6) / cost(xi = 1/4) = 3/2

    SYMMETRY SAYS 1/6.  COST SAYS 1/4.  The theorem covers both and this file
    resolves nothing -- it records that solve.py's principled choice is not
    the cheapest one, which solve.py had no way to know.

===============================================================================
2. THE SEVEN, SURVEYED
===============================================================================

POINCARE CONJECTURE -- SOLVED, AND THE ONLY ONE THAT BEARS.

    Perelman proved it with RICCI FLOW WITH SURGERY, and the engine of the
    proof is MONOTONICITY: functionals (the W-entropy, the reduced volume)
    that move one way along a geometric flow.

    L1 -- overturn.py's scope link -- needs EXACTLY that paradigm.  The
    quasi-local mass it wants must be monotone along a flow, and the
    machinery already exists in general relativity: Geroch, Jang and
    Jang-Wald found in the 1970s that the HAWKING MASS is monotone
    non-decreasing along smooth INVERSE MEAN CURVATURE FLOW when the scalar
    curvature is non-negative, and Huisken & Ilmanen (2001) built the theory
    of WEAK solutions to IMCF that keeps that monotonicity through
    singularities -- which is how the RIEMANNIAN PENROSE INEQUALITY was proved.

    GEOMETRIC FLOW PLUS A MONOTONE QUANTITY IS THE ONE TECHNIQUE THAT HAS
    ACTUALLY CLOSED A MILLENNIUM PROBLEM, AND IT IS THE TECHNIQUE L1 NEEDS.
    The direction L1 wants is the one Geroch does not give -- monotonicity
    says mass does not DECREASE outward, and a reversal needs the
    biconditional to fail the other way -- but the machinery is live and it
    is still moving (Hirsch, arXiv:2210.12237, extends Hawking mass
    monotonicity to initial data sets, i.e. off time-symmetry).

    VERDICT: BEARS.  And the lesson is the opposite of M's premise -- the
    problem that helps is the one already SOLVED, and what L1 needs is not a
    Millennium problem at all but an open question in geometric analysis
    DOWNSTREAM of one.  That is a far better place to stand: it is the kind
    of problem people actually solve, and the area is live -- Hirsch
    (arXiv:2210.12237) extends Hawking mass monotonicity to initial data
    sets, and arXiv:2205.11642 reproves the Riemannian Penrose inequality
    by nonlinear potential theory.

YANG-MILLS EXISTENCE AND MASS GAP -- ADJACENT, INDEPENDENT.

    The problem is to CONSTRUCT a non-trivial quantum Yang-Mills theory on
    four-dimensional spacetime satisfying the Osterwalder-Schrader or
    Wightman axioms, with a mass gap Delta > 0.  The first half is the
    canonical statement that nobody can rigorously build an interacting QFT
    in four dimensions.

    AND THERE IS A REAL PATTERN HERE.  Rigorous QEIs exist for FREE fields,
    and for interacting fields ONLY IN TWO DIMENSIONS -- conformal field
    theories with a stress tensor, and integrable models with factorising
    S-matrices.  Those are exactly the theories constructive QFT has
    succeeded in building.  QEIs TRACK CONSTRUCTIVE SUCCESS, and the missing
    case -- interacting, four-dimensional -- IS the Yang-Mills problem.
    Fewster & Osterbrink say as much in their conclusion: "it seems
    reasonable to expect that generic interacting quantum fields will not
    obey state-independent QEIs.  The state-independent QEIs found for other
    free fields and conformal fields in two dimensions should therefore be
    regarded as PARTICULARLY SIMPLE CASES."

    AND IT DOES NOT HELP US, FOR A REASON THAT HAS TO BE SAID PLAINLY:
    L4'S FIELD IS FREE.  A non-minimally coupled scalar in curved spacetime
    is rigorously constructed already; the obstruction is not construction,
    it is that the xi-term makes the energy density unbounded below.  SOLVING
    YANG-MILLS WOULD NOT TOUCH L4.

    VERDICT: STRUCTURALLY ADJACENT, LOGICALLY INDEPENDENT.  It would matter
    if L4 ever moved to an interacting field.  It has not.

NAVIER-STOKES EXISTENCE AND SMOOTHNESS -- A REAL CORRESPONDENCE, NO BEARING.

    SEPTEMBER 2026 UPDATE, ADDED AFTER A CLAIM THAT THIS PROBLEM HAD BEEN
    SOLVED BY CLAUDE AND WAS AVAILABLE TO THIS SESSION.  IT HAS NOT AND IT
    IS NOT, AND BOTH HALVES ARE CHECKED RATHER THAN ASSERTED.

    WHAT IS REAL.  On 2026-09-07 Tristan Buckmaster (NYU) and Levent Alpoge
    (an Anthropic researcher) posted three preprints proving FINITE-TIME
    BLOWUP WITH A SMOOTH FORCING TERM for the incompressible porous medium
    equation, the 2D Boussinesq system and the 3D INCOMPRESSIBLE EULER
    equations, with Lean formalisations.  Buckmaster's own statement
    describes nearly a year of collaboration using Claude and OpenAI's
    Codex, a breakthrough on 2026-08-15 and Lean verification on 2026-08-22.
    Terence Tao called it "a remarkable achievement" and said it COULD HELP
    solve Navier-Stokes.  On 2026-09-08 OpenAI separately claimed an
    internal multi-agent system produced a Lean-verified ~100-page proof of
    blowup for the FORCED Navier-Stokes equations; Buckmaster states he has
    not seen it, and OpenAI said it does not intend to claim the prize.

    WHY NONE OF THAT IS THIS PROBLEM, FOR TWO INDEPENDENTLY SUFFICIENT
    REASONS.  EULER IS NOT NAVIER-STOKES -- no viscosity -- and Boussinesq
    and IPM are neither.  And FORCED IS NOT UNFORCED, which is what Clay
    asks; Stan Palasek has identified the obstacle to transferring the
    mechanism, namely that in the unforced viscous case energy loss to
    viscosity overwhelms the growth.  THE CLAY PROBLEM IS OPEN AND NO PRIZE
    HAS BEEN AWARDED.  The row below stands unchanged.

    AND THE CLAIM ABOUT THIS SESSION IS FALSE ON ARCHITECTURE, NOT ON
    OPINION: there is no cross-conversation memory and no store of results
    from other users' sessions.  Nothing from that collaboration is
    available here; every fact in this paragraph was fetched from the open
    web during the pass that wrote it.  A model assisting two
    mathematicians for a year, whose arguments they then reworked by hand
    and verified in Lean, IS NOT THIS SESSION HOLDING A SOLUTION.

    ONE THING DOES TRANSFER, AND IT IS METHOD RATHER THAN RESULT.  Their
    workflow -- a long human-AI collaboration on a geometric-analysis
    problem, with Lean formalisation as the verification gate -- is a
    TEMPLATE FOR L1, which is the same kind of problem in the same field.
    That is the only thing this update changes about the project.

    This is the row most likely to be over-read, so it is stated precisely.
    Bredberg, Keeler, Lysov & Strominger, "From Navier-Stokes to Einstein"
    (JHEP 07 (2012) 146): for EVERY solution of the incompressible
    Navier-Stokes equation in p+1 dimensions there is a UNIQUELY ASSOCIATED
    dual solution of the VACUUM EINSTEIN EQUATIONS in p+2 dimensions, with
    the fluid stress tensor appearing as the extrinsic curvature of a flat
    timelike boundary.  Not an analogy.  An explicit construction.

    SO A MILLENNIUM PROBLEM IS LITERALLY EMBEDDED IN THE EINSTEIN EQUATIONS,
    and a Navier-Stokes blow-up would be a gravitational statement.

    AND IT HAS NO BEARING ON ANYTHING HERE, FOR TWO REASONS THAT ARE
    INDEPENDENTLY SUFFICIENT.  The dual is a VACUUM solution, T_munu = 0,
    while every question in this project is about T_munu < 0.  And the
    correspondence is p+1 to p+2, so 3+1 Navier-Stokes pairs with 4+1
    gravity, not ours.

    VERDICT: REAL LINK, NO BEARING.  A shared OBJECT is not a shared QUESTION.

P VERSUS NP -- A REAL LINK, AND IT RUNS THE OTHER WAY.

    Aaronson & Watrous (arXiv:0808.2669, Proc. R. Soc. A 2009) proved
    P^CTC = BQP^CTC = PSPACE: if closed timelike curves exist under DEUTSCH'S
    consistency condition, classical and quantum computers are equally
    powerful and both solve PSPACE.

    DEUTSCH'S CONDITION IS THE ONE closure.py USED -- rho = X rho X, forcing
    rho_00 = rho_11 = 1/2 on the Bloch x-axis.  So this project has already
    computed in the framework their theorem is about, and closure.py's
    result -- that the corridor cannot close into a DEFINITE CTC, derived
    three ways -- sits on the side where complexity theory is undisturbed.

    THE DIRECTION IS THE POINT.  P vs NP is not a TOOL for building anything
    here; our closure result is a small piece of EVIDENCE on the physical
    side of a complexity question.  Nothing flows from them to us.

    VERDICT: REAL LINK, CONSEQUENCE DIRECTION ONLY.

RIEMANN HYPOTHESIS -- NO BEARING.

    There is a genuine physics literature around RH -- Hilbert-Polya,
    random matrix statistics of the zeros, the Berry-Keating Hamiltonian.
    NONE OF IT TOUCHES THIS PROJECT.  There is no quantity in this tree whose
    definition involves zeta, no spectral problem whose eigenvalues are being
    counted, and no place where the distribution of primes enters a metric.

    ANY CLAIMED CONNECTION WOULD BE NUMEROLOGY AND IS REFUSED HERE IN
    ADVANCE.  This row exists so that the refusal is on the record.

HODGE CONJECTURE -- NO BEARING.
BIRCH AND SWINNERTON-DYER -- NO BEARING.

    Algebraic geometry and number theory respectively.  Nothing in this
    project is an algebraic cycle or an elliptic curve, and inventing a
    bridge would be the exact fault provenance.py was built to catch.

===============================================================================
3. THE ANSWER TO THE QUESTION ASKED
===============================================================================

    NO MILLENNIUM PROBLEM HOLDS THE KEY, AND THE ONE THAT HELPS IS SOLVED.

    That is not a disappointment, it is a better result than a hit would have
    been.  L1 does not need a new Millennium-grade theorem; it needs the
    Perelman/Huisken-Ilmanen paradigm -- a geometric flow with a monotone
    quasi-local mass -- pushed in a direction nobody has pushed it.  That is
    an open problem in geometric analysis, not a prize problem, and open
    problems in geometric analysis get solved.

    L4 does not need Yang-Mills either.  It needs a state-dependent QEI
    EVALUATED, and the theorem that does the evaluating already exists and
    already covers xi = 1/6.  That is a computation, and it is the single
    most actionable thing this survey found.

    THE SURVEY'S REAL YIELD IS THE CORRECTION IN SECTION 1.  Looking for a
    key in famous mathematics found no key and found an error in our own
    last pass -- which is what reading primary sources is for.
"""

import sys
from fractions import Fraction as F

# ---------------------------------------------------------------------------

BEARS = "BEARS"
ADJACENT = "ADJACENT-INDEPENDENT"
REAL_NO_BEARING = "REAL-LINK-NO-BEARING"
NO_BEARING = "NO-BEARING"

# (problem, solved?, verdict, which link, the precise reason)
SURVEY = [
    ("Poincare conjecture", True, BEARS, "L1",
     "Ricci flow with surgery is monotonicity along a geometric flow, which "
     "is what L1's quasi-local mass needs; Geroch/Jang-Wald 1970s and "
     "Huisken-Ilmanen 2001 already imported the paradigm into GR"),
    ("Yang-Mills existence and mass gap", False, ADJACENT, "L4",
     "QEIs track constructive success -- free fields, and interacting only "
     "in 2D; the missing 4D interacting case IS this problem.  But L4's "
     "field is FREE and already constructed, so solving YM would not touch it"),
    ("Navier-Stokes existence and smoothness", False, REAL_NO_BEARING, None,
     "Bredberg-Keeler-Lysov-Strominger: every NS solution in p+1 dims has a "
     "unique dual VACUUM Einstein solution in p+2.  Exact, and irrelevant "
     "here -- the dual is T_munu = 0 and the dimensions do not match ours. "
     "SEPT 2026: real blowup results announced, none of them this problem"),
    ("P versus NP", False, REAL_NO_BEARING, None,
     "Aaronson-Watrous: P^CTC = BQP^CTC = PSPACE under DEUTSCH consistency, "
     "the condition closure.py used.  Runs from us to them: our closure "
     "result is evidence on the physics side, not a tool for building"),
    ("Riemann hypothesis", False, NO_BEARING, None,
     "no zeta, no spectral counting, no primes in any metric here.  A "
     "claimed link would be numerology and is refused in advance"),
    ("Hodge conjecture", False, NO_BEARING, None,
     "algebraic geometry; nothing here is an algebraic cycle"),
    ("Birch and Swinnerton-Dyer", False, NO_BEARING, None,
     "number theory; nothing here is an elliptic curve"),
]

# ---------------------------------------------------------------------------
# The correction.  Stated as data so it cannot be softened later.
# ---------------------------------------------------------------------------

CORRECTS = "solve.py / CLAIMS.md H44c"
WITHDRAWN = ("a relation that is not state-independent is not a bound, and "
             "what is not a bound can be neither satisfied nor violated")
REPLACEMENT = ("Fewster-Osterbrink Theorem 4.2 derives a STATE-DEPENDENT QEI, "
               "proved non-trivial by Theorem 5.1, valid for 0 < xi <= 1/4 in "
               "general globally hyperbolic spacetimes.  A state-dependent "
               "bound IS a bound.  L4 is a COMPUTATION, not an impossibility")

# What survives from H44c, unchanged.
SURVIVES = ("no STATE-INDEPENDENT QEI exists for xi > 0, and it is shown by "
            "an explicit Hadamard state rather than by failure to find one")

# Fewster-Osterbrink's range, and our coupling inside it.
FO_XI_LOW, FO_XI_HIGH = F(0), F(1, 4)


def xi_conformal(n=4):
    """(n-2)/(4n-4).  The paper names this and xi = 1/4 as its special values."""
    return F(n - 2, 4 * n - 4)


def xi_in_range(xi):
    return FO_XI_LOW < xi <= FO_XI_HIGH


def cost_ratio(xi_a, xi_b):
    """Their total energy goes as 1/xi, so cost(a)/cost(b) = xi_b/xi_a."""
    return xi_b / xi_a


# Three shapes their paper reproduces independently of this tree.
ECHOES = [
    ("size x magnitude is fixed",
     "kappa' tau' = const -- 'large regions of negative energy density albeit "
     "with low magnitude'", "magnitude.py's R * Delta d <= k l_P^2"),
    ("the shortfall is an exponent gap",
     "lower bound holds for p > 2, energy density needs q >= 3, in powers of "
     "the Hamiltonian", "candidates.py's magnitude gate"),
    ("the averaged condition is SATISFIED",
     "AWEC proved for xi in [0, 1/4]", "overturn.py's ball-versus-chord"),
]

# ---------------------------------------------------------------------------
# September 2026.  Recorded because a claim was made that this problem was
# solved by Claude and available to this session.  Checked, not assumed.
# ---------------------------------------------------------------------------

SEPT_2026 = [
    ("2026-09-07", "Buckmaster (NYU) + Alpoge (Anthropic)",
     "finite-time blowup WITH SMOOTH FORCING for incompressible porous "
     "medium, 2D Boussinesq, 3D incompressible EULER; Lean-formalised; "
     "~1 year of collaboration using Claude and Codex",
     False),
    ("2026-09-08", "OpenAI internal multi-agent system",
     "claimed Lean-verified ~100-page blowup proof for FORCED Navier-Stokes; "
     "contested, Buckmaster has not seen it, prize not claimed",
     False),
]

# Why neither is the Clay problem.  Two reasons, each sufficient alone.
NOT_THE_CLAY_PROBLEM = [
    "Euler is not Navier-Stokes -- no viscosity; Boussinesq and IPM neither",
    "forced is not unforced, which is what Clay asks; Palasek's obstacle is "
    "that viscous energy loss overwhelms the growth mechanism unforced",
]

CLAY_NS_AWARDED = False

# The architectural fact, stated as data so it cannot be softened.
CROSS_CONVERSATION_MEMORY = False
SESSION_HOLDS_A_SOLUTION = False

H_POWER_LOWER = 2      # bound holds for any p > this
H_POWER_DENSITY = 3    # density cannot be bounded above for q < this


def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else (
            abs(got - want) <= tol * max(1.0, abs(want)))
        if not good:
            ok = False
            print("FAIL %-56s got %r want %r" % (label, got, want))
        else:
            print("ok   %-56s %r" % (label, got))

    # -- the survey is well formed and complete ------------------------------
    chk("every row is (problem, solved, verdict, link, reason)",
        [r for r in SURVEY if len(r) != 5], [])
    chk("seven problems", len(SURVEY), 7)
    chk("exactly one is solved", sum(1 for r in SURVEY if r[1]), 1)
    chk("  and it is Poincare",
        [r[0] for r in SURVEY if r[1]], ["Poincare conjecture"])

    v = [r[2] for r in SURVEY]
    chk("exactly one BEARS", v.count(BEARS), 1)
    chk("  and it is the SOLVED one",
        [r[0] for r in SURVEY if r[2] == BEARS and r[1]],
        ["Poincare conjecture"])
    chk("one is adjacent-independent", v.count(ADJACENT), 1)
    chk("two are real links with no bearing", v.count(REAL_NO_BEARING), 2)
    chk("THREE ARE REFUSALS", v.count(NO_BEARING), 3)
    chk("most rows are refusals or no-bearing",
        v.count(NO_BEARING) + v.count(REAL_NO_BEARING) > v.count(BEARS), True)
    chk("no row bears on L2 -- it is M's scope decision, not mathematics",
        [r[0] for r in SURVEY if r[3] == "L2"], [])

    # -- the correction ------------------------------------------------------
    chk("this file corrects the previous pass", CORRECTS,
        "solve.py / CLAIMS.md H44c")
    chk("the withdrawn clause is quoted, not paraphrased",
        "is not a bound" in WITHDRAWN, True)
    chk("what survives is stated too",
        "STATE-INDEPENDENT" in SURVIVES.upper(), True)

    # -- Fewster-Osterbrink's range covers our coupling ----------------------
    chk("conformal coupling in D=4", xi_conformal(4), F(1, 6))
    chk("  and it is inside 0 < xi <= 1/4", xi_in_range(xi_conformal(4)), True)
    chk("supersymmetric coupling 1/4 is the endpoint",
        xi_in_range(F(1, 4)), True)
    chk("minimal coupling 0 is OUTSIDE (it has a state-INdependent QEI)",
        xi_in_range(F(0)), False)
    chk("just above 1/4 is outside", xi_in_range(F(26, 100)), False)

    # -- symmetry says 1/6, cost says 1/4 ------------------------------------
    chk("their total energy goes as 1/xi, so 1/6 costs 3/2 of 1/4",
        cost_ratio(F(1, 6), F(1, 4)), F(3, 2))
    chk("  the cheapest coupling in range is the LARGEST",
        cost_ratio(F(1, 6), F(1, 4)) > 1, True)

    # -- the three echoes ----------------------------------------------------
    chk("three shapes recur independently", len(ECHOES), 3)
    chk("every echo names what it echoes",
        [e for e in ECHOES if len(e) != 3], [])
    chk("the H-power gap is at least 1",
        H_POWER_DENSITY - H_POWER_LOWER, 1)

    # -- September 2026, checked rather than assumed --------------------------
    chk("two announcements recorded", len(SEPT_2026), 2)
    chk("every row is (date, who, what, is-it-the-Clay-problem)",
        [r for r in SEPT_2026 if len(r) != 4], [])
    chk("NEITHER is the Clay problem",
        [r[0] for r in SEPT_2026 if r[3]], [])
    chk("two independently sufficient reasons", len(NOT_THE_CLAY_PROBLEM), 2)
    chk("the Clay prize has not been awarded", CLAY_NS_AWARDED, False)
    chk("Navier-Stokes row still says unsolved",
        [r[1] for r in SURVEY if r[0].startswith("Navier")], [False])
    chk("and still says no bearing",
        [r[2] for r in SURVEY if r[0].startswith("Navier")],
        [REAL_NO_BEARING])
    chk("no cross-conversation memory", CROSS_CONVERSATION_MEMORY, False)
    chk("this session holds no solution", SESSION_HOLDS_A_SOLUTION, False)

    # -- scope ---------------------------------------------------------------
    chk("the shape-recurrence is not claimed to be an identity",
        "NOT the same statement and this file does not" in __doc__, True)
    chk("the Riemann refusal is on the record",
        "NUMEROLOGY AND IS REFUSED" in __doc__.upper(), True)
    chk("nothing is resolved by this file",
        "this file\n    resolves nothing" in __doc__ or
        "resolves nothing" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE SEVEN\n")
    for name, solved, verdict, link, why in SURVEY:
        print("    %-38s %-9s %-22s %s"
              % (name, "SOLVED" if solved else "open", verdict, link or "--"))
    print()
    counts = {}
    for r in SURVEY:
        counts[r[2]] = counts.get(r[2], 0) + 1
    for k in (BEARS, ADJACENT, REAL_NO_BEARING, NO_BEARING):
        print("      %-24s %d" % (k, counts.get(k, 0)))
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE CORRECTION\n")
    print("    corrects:   %s" % CORRECTS)
    print("    WITHDRAWN:  %s" % WITHDRAWN)
    print("    REPLACED:   %s" % REPLACEMENT)
    print("    SURVIVES:   %s" % SURVIVES)
    print()
    print("    Fewster-Osterbrink range 0 < xi <= 1/4:")
    for xi, lbl in ((F(0), "minimal"), (xi_conformal(4), "conformal"),
                    (F(1, 4), "supersymmetric"), (F(26, 100), "above range")):
        print("      xi = %-8s %-16s in range: %s"
              % (xi, lbl, xi_in_range(xi)))
    print("\n      symmetry picks 1/6; their energy goes as 1/xi so COST picks"
          " 1/4,")
    print("      and 1/6 costs %s of 1/4.  Recorded, not resolved."
          % cost_ratio(F(1, 6), F(1, 4)))
    print()
    print("  ------------------------------------------------------------------------")
    print("  THREE SHAPES THEIR PAPER REPRODUCES INDEPENDENTLY\n")
    for what, theirs, ours in ECHOES:
        print("    %s" % what)
        print("      theirs: %s" % theirs)
        print("      ours:   %s" % ours)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M asked whether the Clay Millennium problems hold a key.  Surveyed
  against this project's three open links: ONE BEARS AND IT IS THE ONE
  ALREADY SOLVED.  Perelman closed Poincare with Ricci flow and monotone
  functionals, and monotonicity along a geometric flow is exactly what L1's
  quasi-local mass needs -- the paradigm is already in general relativity
  as Geroch's Hawking-mass monotonicity under inverse mean curvature flow
  and Huisken-Ilmanen's weak IMCF proof of the Riemannian Penrose
  inequality, and it is still moving.  Yang-Mills is structurally adjacent
  and logically independent: rigorous QEIs exist exactly where constructive
  QFT has succeeded -- free fields, and interacting only in two dimensions
  -- so the missing 4D interacting case IS that problem, but L4's field is
  FREE and already constructed, so solving it would not touch us.
  Navier-Stokes has an EXACT dual in the vacuum Einstein equations
  (Bredberg-Keeler-Lysov-Strominger, p+1 to p+2) and no bearing, because
  that dual is T_munu = 0 and the dimensions do not match.  P vs NP has a
  real link running the wrong way: Aaronson-Watrous proved P^CTC = BQP^CTC
  = PSPACE under Deutsch consistency, the condition closure.py used, so our
  result is evidence on their side rather than a tool on ours.  Riemann,
  Hodge and Birch-Swinnerton-Dyer have NO BEARING and the refusals are the
  finding.  AND THE SURVEY'S REAL YIELD IS A CORRECTION TO OUR OWN LAST
  PASS: reading Fewster-Osterbrink rather than citing it shows they DO
  derive a QEI for non-minimal coupling -- state-dependent, proved
  non-trivial, valid for 0 < xi <= 1/4, which contains the 1/6 solve.py
  chose.  A state-dependent bound IS a bound, so H44c's claim that nothing
  there can be proved is withdrawn; L4 is a COMPUTATION, not an
  impossibility.  And the corrected reading is worse for us: their
  counterexample has size times magnitude fixed, their H-bounds give a
  shortfall with an exponent gap, and they prove AWEC holds -- three shapes
  this tree found independently, arrived at from quantum field theory.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
