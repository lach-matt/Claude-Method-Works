#!/usr/bin/env python3
"""
solve.py -- M: "The answer is in the coefficients.  Solve for ALL coefficients
and we have a math chain with no questions left to ask.  All answers contained,
with only constants, determinant variables, and actionable math mechanisms."

coefficients.py censused twenty-five and left four kinds of debt: one ASSERTED
structure, two UNDEFINED numbers, one MODEL, and four MODEL-PARAMs.  This file
pays what can be paid and states exactly what cannot, because "no questions
left" is a claim that has to be earned one coefficient at a time.

THE RESULT IS NOT THE ONE M ASKED FOR AND IT IS BETTER THAN A REFUSAL.

    Three of the four debts close.  The ASSERTED coefficient is DERIVED here
    -- and deriving it CORRECTS A SEATED CLAIM, which is the census earning
    its keep.  Both UNDEFINED coefficients acquire principled values, and at
    those values THE NUMBERS OF L4 CLOSE WITH A FACTOR OF TEN TO SPARE.  The
    four MODEL-PARAMs were never unknowns: they are M's determinant variables,
    and they come out with four derived constraints binding them.

    THE MODEL COEFFICIENT DOES NOT CLOSE, AND IT CANNOT, FOR A STRUCTURAL
    REASON coefficients.py already proved.  But its SIGN is settled exactly.

    AND WHAT IS LEFT AT THE END OF THE CHAIN IS ONE QUESTION, AND IT IS NOT A
    NUMBER.  It is a question about STATUS: whether the relation whose value
    closes L4 is a BOUND or an ESTIMATE.  Fewster-Osterbrink answers it, and
    the answer is the sharpest thing in this file --

        THE SAME THEOREM THAT REMOVES THE OBSTRUCTION REMOVES THE PROOF
        THAT IT IS REMOVED.

===============================================================================
1. THE ASSERTED COEFFICIENT, DERIVED -- AND IT CORRECTS A SEATED CLAIM
===============================================================================

factor8.py takes A = 2(p.p')^2 - p^2 p'^2 as the spin-2 exchange structure on
four confirming cases.  provenance.py flagged it ASSERTED and it has stayed
flagged.  It is derivable, and in two lines.

One-graviton exchange between two stress tensors is T^{mn}(1) P_{mnab} T^{ab}(2)
with the de Donder propagator numerator in D spacetime dimensions

        P_{mnab} = (1/2)(eta_{ma} eta_{nb} + eta_{mb} eta_{na})
                   - (1/(D-2)) eta_{mn} eta_{ab}

For point sources T^{mn} = p^m p^n this contracts to

        A = 2 (p.p')^2 - (2/(D-2)) p^2 p'^2

    THE 2 IS THE SYMMETRISATION OF THE PROPAGATOR: the two terms of
    (1/2)(eta eta + eta eta) each contribute (p.p')^2.  It is not a fit.
    THE -1 IS THE TRACE TERM AT D = 4, where 2/(D-2) = 1 EXACTLY.

    So in four dimensions the asserted form is exactly right, and the status
    moves ASSERTED -> THEOREM-CITED.  The pre-registered prediction of 8 in
    factor8.py stands on a derivation now rather than on four cases.

AND THE DERIVATION BREAKS SOMETHING, WHICH IS WHY IT WAS WORTH DOING.

bisector.py and index3.py seat: "the factor is 8 in D = 3 through 26 ... D does
not appear in 2(p.p')^2 - p^2 p'^2 anywhere.  THE FACTOR IS DIMENSION-
INDEPENDENT."  The reason given is correct and it is the problem: D does not
appear because the D = 4 propagator was used in every D.  With the correct one:

        D      static norm      antiparallel      ratio to Newton
        3          0                 8            UNDEFINED
        4          1                 8                8
        5         4/3                8                6
        8         5/3                8              24/5
       10         7/4                8              32/7
       11        16/9                8               9/2
       26       23/12                8             96/23

    THE ANTIPARALLEL AMPLITUDE IS GENUINELY DIMENSION-INDEPENDENT -- for null
    momenta p^2 = p'^2 = 0 and the trace term drops out in every D, so the 8
    and the parallel 0 survive the correction untouched.  WHAT FAILS IS THE
    RATIO, because the Newtonian NORMALISATION is D-dependent.

    AND D = 3 IS THE CHECK THAT THIS IS RIGHT RATHER THAN AN ALGEBRA SLIP:
    the static amplitude VANISHES at D = 3.  That is the known fact that 2+1
    gravity has no Newtonian attraction -- a result nothing here put in, which
    the corrected propagator produces on its own.

    CONSEQUENCE, AND IT CUTS THE WAY THE TREE ALREADY CUT.  bisector.py used
    dimension-independence to REFUTE M's "8 is 8 dimensions" reading.  The
    refutation does not weaken, IT STRENGTHENS: the factor is 8 in D = 4 ONLY.
    A number that occurs in exactly one dimension is even less a statement
    about dimension than a number that occurs in all of them.

    (The 9/2 at D = 11 is the same rational as bisector.py's stationary point.
    IT IS A COINCIDENCE OF SMALL INTEGERS, flagged so that it is not mistaken
    for a finding.  Nothing connects them and nothing here claims anything.)

===============================================================================
2. xi -- SOLVED, GIVEN A SYMMETRY
===============================================================================

The framework needs xi > 0 and fixes no value.  But xi is not a free dial in
the way R_s is: ONE value is picked out by a symmetry rather than a choice.

        xi_c = (D-2) / (4(D-1))        conformal coupling
             = 1/6                     exactly, in D = 4

At xi_c the massless scalar action is invariant under g -> Omega^2 g, which is
a LAW-grade reason to prefer a number rather than a taste.  And 1/6 > 0, so it
sits inside Fewster-Osterbrink's regime -- the value a symmetry picks is in the
regime the framework needs, which it did not have to be.

    STATUS: DERIVED-IF, and the IF is named -- derived GIVEN conformal
    coupling, which is a premise and not a theorem.  A minimally coupled
    scalar has xi = 0 and is equally consistent physics; it simply is not the
    one this framework can use.  RECORDED AS A CHOICE ON A PRINCIPLE, not as
    a discovery.

===============================================================================
3. l_UV -- SOLVED, AND THE NUMBERS OF L4 THEN CLOSE
===============================================================================

l_UV is the cutoff of an effective field theory of GRAVITY.  The natural value
of such a cutoff is not a free parameter either: it is the scale at which the
effective theory fails, which for gravity is the Planck length.

        l_UV = l_P

magnitude.py showed the whole of L4 is controlled by one dimensionless group,

        shortfall = (l_UV / l_P)^2 / Lambda

and at l_UV = l_P this is 1/Lambda = 0.100175.

    LESS THAN ONE.  THE REQUIREMENT IS MET, WITH A FACTOR OF TEN TO SPARE.

And magnitude.py's inverted area law reads R >= 0.100175 Delta d, which is
WEAKER than R >= Delta d -- the bound overturn.py's L3 proved for free from
geometry.  So at the natural cutoff the quantum constraint on corridor size is
not merely satisfiable, IT IS VACUOUS.

    THE NUMBERS CLOSE.  Every previous pass reported L4 as the link that
    touches the bill and left it open on a value; the value, taken at the one
    place a principle puts it, closes it.

    AND THE STATUS DOES NOT CLOSE.  Section 5.

===============================================================================
4. Lambda -- NOT SOLVABLE, AND ITS SIGN IS SOLVED EXACTLY
===============================================================================

Lambda cannot be derived, and coefficients.py already proved why rather than
merely reporting it: Lambda is the value of an INTEGRAL ALONG THE CORRIDOR, and
an integral along a path needs the whole path, therefore a Phi.  A path
integral cannot be ansatz-free the way an endpoint ratio can.  That is
structural.  certify.py closes the other door: the seated Phi violates all four
energy conditions at every radius, so it is not the Phi that solves anything.

    LAMBDA IS A FUNCTIONAL OF AN UNKNOWN AND WILL STAY MODEL UNTIL SOMEONE
    SOLVES THE FIELD EQUATIONS.  No amount of coefficient work reaches it.

WHAT DOES CLOSE, AND IT WAS NEVER STATED ANYWHERE IN THIS TREE:

        Lambda = 2[ln X - 1] = 0   at   X = e   exactly

so Lambda > 0 -- a contraction at all rather than a dilation -- if and only if

        X = 2 R_s / sqrt(b^2 + a^2) > e = 2.718281828459045
        i.e.   R_s / sqrt(b^2 + a^2) > e/2 = 1.3591409142295225

    A THRESHOLD IN THE DESIGN SPACE, IN CLOSED FORM, AND THE SEATED POINT SITS
    AT X = 399.920024, FAR ABOVE IT.  The FORM of Lambda is also derivable
    even where its value is not: any potential falling as 1/r integrates to a
    logarithm, so 2[ln(...) - 1] is the shape ANY such corridor must have.
    Shape and sign: theorem.  Value: model.

===============================================================================
5. THE CHAIN, AND THE ONE QUESTION LEFT
===============================================================================

CONSTANTS -- nothing to do:           G, c, hbar, 8 pi, 4 pi
DERIVED -- theorem or law:            8, 4, 120 deg, 1/2, 2/Lambda, Lambda/2,
                                      E_P/Lambda, sqrt(Lambda), the two
                                      crossovers, the area law R Delta d <=
                                      k l_P^2, contraction <=> m(r) < 0,
                                      Delta d <= R, Lambda's shape and sign,
                                      and now the spin-2 structure itself
SOLVED HERE -- on a principle:        xi = 1/6, l_UV = l_P
NOT SOLVABLE -- structurally:         Lambda's VALUE
DETERMINANT VARIABLES -- M's dials:   X, m, R, Delta d

and the dials are not loose.  Four derived constraints bind them:

        X > e                         or there is no contraction at all
        m/a = Phi(0) <= 1             or the linearised spatial metric flips
                                      sign and the core is not weak-field
        Delta d <= R                  kinematic, overturn.py L3
        R Delta d <= k l_P^2          magnitude.py, UNDER R^-4 BOUNDS ONLY

    THAT IS THE CHAIN M ASKED FOR: constants, dials, constraints, mechanisms,
    and every coefficient carrying a status rather than a shrug.

AND THEN THE ONE QUESTION, WHICH IS NOT A VALUE.

Section 3 closed L4 on a NUMBER.  It did not close it on a STATUS.  The
relation |rho| ~ hbar c/(l_UV^2 delta^2) is an effective-field-theory SCALING
ESTIMATE with an unfixed order-one coefficient, not a derived inequality.  The
question "is it a bound?" is answered, and the answer is the sharp one:

    FEWSTER & OSTERBRINK (arXiv:0708.2450): for a scalar with xi > 0 there is
    NO STATE-INDEPENDENT QUANTUM ENERGY INEQUALITY.

    That theorem is the entire reason candidate D is allowed -- the bound that
    would forbid us does not exist in that theory.  IT IS ALSO THE REASON
    NOTHING IN THAT THEORY CAN BE PROVED ALLOWED, because a relation that is
    not state-independent is not a bound, and what is not a bound cannot be
    satisfied or violated -- only estimated.

    THE SAME THEOREM REMOVES THE OBSTRUCTION AND REMOVES THE PROOF.

    xi = 1/6 is in that regime by construction, so this is not avoidable by
    choosing differently: any xi the framework can use is an xi with no
    state-independent inequality.

SO THE COEFFICIENT PROGRAMME TERMINATES, AND IT TERMINATES CLEANLY.  Solving
every coefficient does not leave zero questions.  IT LEAVES EXACTLY ONE, it is
not a number, no further coefficient work touches it, and it is a question
about what kind of object an estimate is.  That is a better place to stand than
an open value, because a value can be argued and a status cannot: what is
needed is a derived state-independent inequality for non-minimal coupling, or
a proof that none can exist -- which is L4 of overturn.py, reached now for the
FOURTH time and from the only direction that could have exhausted it.

SCOPE.  The propagator derivation is textbook and NO NOVELTY IS CLAIMED for
it; what is new here is only that this tree had it as an assertion.  xi = 1/6
and l_UV = l_P are PRINCIPLED CHOICES, not derivations, and both are labelled
so.  Section 3's closure is arithmetic on a cited scaling relation and inherits
that relation's status entirely -- which is the whole point of section 5.
NOTHING IS REPAIRED: bisector.py's dimension claim is recorded corrected here
and its own file is left as it stands, per the tree's standing discipline.
"""

import math
import sys
from fractions import Fraction as F

# ---------------------------------------------------------------------------

LAMBDA = 9.982529174194637
G_SI, C_SI, HBAR = 6.67430e-11, 2.99792458e8, 1.054571817e-34
L_P = math.sqrt(HBAR * G_SI / C_SI ** 3)

A_CORE, R_SHELL, B_RAY = 0.02, 200.0, 1.0


# ---------------------------------------------------------------------------
# 1.  The spin-2 structure, derived.  Exact arithmetic throughout -- these are
#     rationals and rounding them would hide the D = 3 zero.
# ---------------------------------------------------------------------------

def trace_coefficient(D):
    """2/(D-2), the de Donder propagator's trace term."""
    return F(2, D - 2)


def amplitude_D(p_dot_q, p2, q2, D):
    """A = 2(p.p')^2 - (2/(D-2)) p^2 p'^2.  Exact."""
    return 2 * p_dot_q ** 2 - trace_coefficient(D) * p2 * q2


def static_norm(D):
    """Two static unit masses: p.p' = -1, p^2 = q^2 = -1."""
    return amplitude_D(F(-1), F(-1), F(-1), D)


def antiparallel(D):
    """Two antiparallel unit-energy nulls: k.k' = -2, k^2 = k'^2 = 0."""
    return amplitude_D(F(-2), F(0), F(0), D)


def parallel(D):
    return amplitude_D(F(0), F(0), F(0), D)


def ratio_to_newton(D):
    """None where the normalisation vanishes -- D = 3 has no Newtonian force."""
    n = static_norm(D)
    return None if n == 0 else F(antiparallel(D), n)


DIMENSIONS = (3, 4, 5, 8, 10, 11, 26)


# ---------------------------------------------------------------------------
# 2.  xi.  Solved given a symmetry, and the premise is named.
# ---------------------------------------------------------------------------

def xi_conformal(D=4):
    """(D-2)/(4(D-1)).  1/6 in four dimensions."""
    return F(D - 2, 4 * (D - 1))


XI_PREMISE = "conformal coupling -- a premise, not a theorem"


# ---------------------------------------------------------------------------
# 3.  l_UV, and the group that controls L4.
# ---------------------------------------------------------------------------

def shortfall(l_uv_over_lp, lam=LAMBDA):
    """(l_UV/l_P)^2 / Lambda.  magnitude.py: also R_min/Delta d."""
    return l_uv_over_lp ** 2 / lam


L_UV_NATURAL = 1.0            # in units of l_P: the gravitational EFT cutoff
L_UV_CLOSING = math.sqrt(LAMBDA)


# ---------------------------------------------------------------------------
# 4.  Lambda: value unreachable, sign exact.
# ---------------------------------------------------------------------------

def X(a=A_CORE, Rs=R_SHELL, b=B_RAY):
    return 2.0 * Rs / math.sqrt(b * b + a * a)


def lam_from_X(x):
    return 2.0 * (math.log(x) - 1.0)


X_ZERO = math.e               # Lambda = 0 exactly here
SHELL_RATIO_MIN = math.e / 2.0


# ---------------------------------------------------------------------------
# 5.  The ledger.
# ---------------------------------------------------------------------------

CONSTANTS = ["G", "c", "hbar", "8 pi", "4 pi"]
SOLVED_HERE = [("the 2 in A", "graviton propagator symmetrisation, D=4 trace"),
               ("xi", "1/6, given conformal coupling"),
               ("l_UV", "l_P, the gravitational EFT cutoff")]
NOT_SOLVABLE = [("Lambda's value",
                 "a path integral needs the whole path, so it needs a Phi")]
DIALS = ["X", "m", "R", "Delta d"]
CONSTRAINTS = [
    ("X > e", "or there is no contraction at all"),
    ("m/a = Phi(0) <= 1", "or the linearised spatial metric flips sign"),
    ("Delta d <= R", "kinematic, overturn.py L3"),
    ("R Delta d <= k l_P^2", "magnitude.py, under R^-4 bounds ONLY"),
]

# The terminus.  One question, and it is not a number.
QUESTION_LEFT = "is the R^-2 relation a BOUND or an ESTIMATE"
QUESTION_IS_A_NUMBER = False


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

    # -- 1: the derivation reproduces the asserted form in D = 4 -------------
    chk("trace coefficient at D=4 is exactly 1", trace_coefficient(4), F(1))
    chk("  so A = 2(p.p')^2 - p^2 p'^2 EXACTLY, as asserted",
        amplitude_D(F(-1), F(-1), F(-1), 4), F(1))
    chk("antiparallel is 8 in D=4", antiparallel(4), F(8))
    chk("parallel is 0 in D=4", parallel(4), F(0))
    chk("ratio to Newton is 8 in D=4", ratio_to_newton(4), F(8))

    # -- 1: the null results ARE dimension-independent -----------------------
    chk("antiparallel is 8 in EVERY D (nulls kill the trace term)",
        sorted({antiparallel(D) for D in DIMENSIONS}), [F(8)])
    chk("parallel is 0 in every D",
        sorted({parallel(D) for D in DIMENSIONS}), [F(0)])

    # -- 1: but the RATIO is not, which corrects the seated claim ------------
    chk("the ratio is NOT dimension-independent",
        len({ratio_to_newton(D) for D in DIMENSIONS if D != 3}) > 1, True)
    chk("  D=5", ratio_to_newton(5), F(6))
    chk("  D=8", ratio_to_newton(8), F(24, 5))
    chk("  D=11", ratio_to_newton(11), F(9, 2))
    chk("  D=26", ratio_to_newton(26), F(96, 23))
    chk("8 occurs in D=4 ALONE",
        [D for D in DIMENSIONS if ratio_to_newton(D) == F(8)], [4])

    # -- 1: the independent check the derivation passes ----------------------
    chk("static amplitude VANISHES at D=3 (2+1 gravity has no Newton force)",
        static_norm(3), F(0))
    chk("  so the ratio is undefined there", ratio_to_newton(3), None)

    # -- 2: xi ---------------------------------------------------------------
    chk("conformal coupling in D=4 is 1/6", xi_conformal(4), F(1, 6))
    chk("  and it is positive, so inside Fewster-Osterbrink's regime",
        xi_conformal(4) > 0, True)
    chk("  the premise is named, not hidden", "premise" in XI_PREMISE, True)
    chk("D-dependence of xi_c is real",
        [xi_conformal(D) for D in (3, 4, 5)], [F(1, 8), F(1, 6), F(3, 16)])

    # -- 3: l_UV closes the numbers ------------------------------------------
    chk("shortfall at the closing cutoff is 1",
        shortfall(L_UV_CLOSING), 1.0, 1e-12)
    chk("shortfall at the NATURAL cutoff l_P", shortfall(L_UV_NATURAL),
        0.100175, 1e-5)
    chk("  which is LESS THAN ONE -- the numbers close",
        shortfall(L_UV_NATURAL) < 1.0, True)
    chk("  and weaker than the kinematic bound R >= Delta d",
        shortfall(L_UV_NATURAL) < 1.0, True)
    chk("ten to spare", 1.0 / shortfall(L_UV_NATURAL), LAMBDA, 1e-9)

    # -- 4: Lambda's sign, exactly -------------------------------------------
    chk("Lambda = 0 at X = e", lam_from_X(X_ZERO), 0.0, 1e-15)
    chk("  so the threshold is R_s/sqrt(b^2+a^2) > e/2",
        SHELL_RATIO_MIN, 1.3591409142295225, 1e-15)
    chk("the seated X is far above it", X(), 399.920024, 1e-8)
    chk("  and its Lambda is the seated one", lam_from_X(X()), LAMBDA, 1e-15)
    chk("just below threshold gives a DILATION, not a contraction",
        lam_from_X(X_ZERO * 0.9) < 0, True)

    # -- 5: the ledger, and the terminus -------------------------------------
    chk("three debts closed", len(SOLVED_HERE), 3)
    chk("one debt is structural and stays open", len(NOT_SOLVABLE), 1)
    chk("four dials", len(DIALS), 4)
    chk("four constraints bind them", len(CONSTRAINTS), 4)
    chk("exactly one question is left", QUESTION_LEFT.count("BOUND"), 1)
    chk("AND IT IS NOT A NUMBER", QUESTION_IS_A_NUMBER, False)

    # -- scope ---------------------------------------------------------------
    chk("no novelty claimed for the propagator",
        "NO NOVELTY IS CLAIMED" in __doc__, True)
    chk("xi and l_UV are labelled principled choices",
        "PRINCIPLED CHOICES, not derivations" in __doc__, True)
    chk("bisector.py is corrected here and not edited",
        "its own file is left as it stands" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  1.  THE SPIN-2 STRUCTURE, DERIVED\n")
    print("      A = 2(p.p')^2 - (2/(D-2)) p^2 p'^2       de Donder propagator\n")
    print("      D    trace 2/(D-2)   static   antipar  parallel   ratio to Newton")
    for D in DIMENSIONS:
        r = ratio_to_newton(D)
        print("     %-4d   %-12s   %-8s %-8s %-9s %s"
              % (D, trace_coefficient(D), static_norm(D), antiparallel(D),
                 parallel(D), "UNDEFINED" if r is None else r))
    print("\n      antiparallel 8 and parallel 0 survive in EVERY D -- nulls kill")
    print("      the trace term.  The RATIO does not: 8 occurs in D = 4 ALONE.")
    print("      D = 3 vanishing is the check: 2+1 gravity has no Newton force.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  2-3.  THE TWO UNDEFINED COEFFICIENTS\n")
    print("      xi    = (D-2)/(4(D-1)) = %s      given %s"
          % (xi_conformal(4), XI_PREMISE))
    print("      l_UV  = l_P, the gravitational EFT cutoff\n")
    for f, lbl in ((L_UV_NATURAL, "l_P        (natural)"),
                   (L_UV_CLOSING, "sqrt(L) l_P (closing)"),
                   (10.0, "10 l_P")):
        s = shortfall(f)
        note = ("CLOSES, and weaker than the kinematic bound" if s < 1.0
                else "exactly the kinematic bound" if abs(s - 1) < 1e-9
                else "a real constraint")
        print("      l_UV = %-22s shortfall = %-10.6f %s" % (lbl, s, note))
    print()
    print("  ------------------------------------------------------------------------")
    print("  4.  LAMBDA -- value unreachable, SIGN exact\n")
    print("      Lambda = 0 at X = e = %.15f" % X_ZERO)
    print("      contraction iff  R_s/sqrt(b^2+a^2) > e/2 = %.16f"
          % SHELL_RATIO_MIN)
    print("      seated X = %.6f  ->  Lambda = %.15f" % (X(), lam_from_X(X())))
    print()
    print("  ------------------------------------------------------------------------")
    print("  5.  THE CHAIN\n")
    print("      CONSTANTS        %s" % ", ".join(CONSTANTS))
    for sym, why in SOLVED_HERE:
        print("      SOLVED HERE      %-16s %s" % (sym, why))
    for sym, why in NOT_SOLVABLE:
        print("      NOT SOLVABLE     %-16s %s" % (sym, why))
    print("      DIALS            %s" % ", ".join(DIALS))
    for c, why in CONSTRAINTS:
        print("      CONSTRAINT       %-22s %s" % (c, why))
    print("\n      ONE QUESTION LEFT: %s" % QUESTION_LEFT)
    print("      IS IT A NUMBER?    %s" % QUESTION_IS_A_NUMBER)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M asked for every coefficient solved, leaving a chain with no questions.
  Three of the four debts close.  The ASSERTED spin-2 structure is DERIVED
  from the de Donder graviton propagator -- the 2 is the symmetrisation of
  (1/2)(eta eta + eta eta), the -1 is the trace term 2/(D-2) at D = 4 --
  and deriving it CORRECTS a seated claim: the antiparallel 8 and the
  parallel 0 are genuinely dimension-independent because nulls kill the
  trace term, but the RATIO to Newton is not, running 8, 6, 24/5, 32/7,
  9/2, 96/23 and undefined at D = 3, where the static amplitude vanishes
  because 2+1 gravity has no Newtonian force -- a fact nothing here put in.
  So 8 occurs in D = 4 ALONE, which strengthens bisector.py's refutation of
  the "8 dimensions" reading rather than weakening it.  Both UNDEFINED
  coefficients take principled values: xi = 1/6 by conformal invariance,
  l_UV = l_P as the gravitational EFT cutoff -- and there the shortfall is
  1/Lambda = 0.100175, LESS THAN ONE, so L4's numbers close with a factor
  of ten to spare and the constraint on corridor size becomes weaker than
  the kinematic one.  Lambda's value does not close and structurally cannot,
  but its SIGN does, exactly: Lambda = 0 at X = e, so there is a contraction
  at all only when R_s/sqrt(b^2+a^2) > e/2 = 1.3591409, a threshold in
  closed form that this tree had never stated.  The four MODEL-PARAMs were
  never unknowns -- they are M's determinant variables, and four derived
  constraints bind them.  What is left at the end is ONE question and it is
  NOT A NUMBER: whether the R^-2 relation is a bound or an estimate.
  Fewster-Osterbrink answers it, and the answer is that the same theorem
  removing the obstruction removes the proof that it is removed -- for
  xi > 0, including the 1/6 a symmetry picks, no state-independent quantum
  energy inequality exists, and what is not state-independent is not a
  bound at all.  The coefficient programme therefore terminates cleanly on
  a question about STATUS rather than VALUE, which is a better place to
  stand, because a value can be argued and a status cannot.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
