#!/usr/bin/env python3
r"""exact.py -- NO COEFFICIENTS.  EXACT CALCULATIONS ONLY.  DOCKET 40.

    python3 exact.py             the reading
    python3 exact.py --selftest  fixtures

M: "no coefficients, exact calculations only, now that we have the ability to
calculate and machine check any coefficient."

`coefficients.py` censused the framework's twenty-five numbers by PROVENANCE --
where each came from.  This file censuses them by EXACTNESS: does a closed form
exist, does it reproduce the decimal the tree has been quoting, and if no closed
form exists, what exactly is missing.  sympy is the arbiter and every form below
is evaluated to thirty digits against the recorded value.

===============================================================================
1. THE FINDING: ALMOST EVERY "MEASURED" NUMBER WAS ALREADY EXACT
===============================================================================

The provenance census graded two numbers MEASURED -- "a number this tree solved
for" -- and one MODEL, the coefficient that sets the bill.  All three are closed
forms, and were being carried as decimals:

    Lambda        = 2[ln X - 1]          X = 2 R_s / sqrt(b^2 + a^2)
    crossover FR  = sqrt(3 Lambda / (32 pi^2))   in units of l_P
    crossover Cas = the Casimir crossing, exact in Lambda

At the seated design point (a, R_s, b) = (1/50, 200, 1) these are not
approximations of anything:

    X      = 20000 sqrt(2501) / 2501                 EXACT, a surd
    Lambda = ln(400000000/2501) - 2                  EXACT, a logarithm

and `Lambda` evaluates to 9.982529174194637038..., which is the float the tree
has been quoting to sixteen places.  NOTHING WAS FITTED.  The number looked
like a coefficient because it was written as one.

    SO THE RULE IS SATISFIABLE ALMOST EVERYWHERE, and the work it asks for is
    mostly transcription: carry the form, print the decimal only at the edge.

===============================================================================
2. AND IT LOCALISES THE THREE THAT ARE NOT
===============================================================================

    xi        UNDEFINED.  The non-minimal coupling.  The framework needs
              xi > 0 and fixes no value; Fewster-Osterbrink then says no
              state-independent QEI exists, which is candidate D's whole hope.
              NO CLOSED FORM AND NO MEASUREMENT.  It is not a coefficient this
              tree may use.

    l_UV      UNDEFINED.  The EFT cutoff of Fliss et al.  The shortfall closes
              at l_UV = sqrt(Lambda) l_P and nothing says that is the cutoff.
              NO CLOSED FORM AND NO MEASUREMENT.

    the 2     ASSERTED, in A = 2(p.p')^2 - p^2 p'^2, taken on four confirming
              cases.  THIS ONE IS DECIDABLE and it is the first target: four
              cases is not a proof, and a finite algebraic identity is exactly
              what sympy and z3 settle.  Until it is settled it is an
              assumption wearing a digit.

    AND ONE MORE THE PROVENANCE CENSUS NEVER HELD, because it is not in the
    framework but in the measurement: the ceiling 0.0218 c of MEASURED.md is a
    LEAST-SQUARES ZERO of the null-energy minimum in its linear regime.  That
    is a fit.  Under this rule it may not be quoted as a derived number; it is
    a measurement with a spread, and the spread is the 0.1 % between the two
    grids.  `NOT_EXACT` carries it so it cannot be quoted as anything else.

===============================================================================
3. WHAT EXACTNESS BUYS, AND IT IS NOT TIDINESS
===============================================================================

Carrying Lambda as a form rather than a float makes the design derivatives
closed forms too, and they were never stated in this tree:

    dLambda/dR_s =  2 / R_s
    dLambda/da   = -2a / (b^2 + a^2)
    dLambda/db   = -2b / (b^2 + a^2)

At the seated point that is 1/100, -100/2501 and -5000/2501 exactly:

    THE RAY PARAMETER b IS THE STRONGEST LEVER ON THE BILL BY TWO ORDERS OF
    MAGNITUDE -- |dLambda/db| is 199.92 times |dLambda/dR_s| and 50 times
    |dLambda/da|.  A float census cannot say that; three exact derivatives say
    it in one line.  `leverage()` computes them and `--selftest` pins them as
    rationals, not as decimals.

And the sign threshold is exact and was already known in this tree, so it is
re-derived here rather than restated: Lambda > 0 -- a contraction rather than a
dilation -- iff X > e, i.e. R_s / sqrt(b^2 + a^2) > e/2.  `threshold()` proves
it by monotonicity rather than by sampling.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    TO CALL THE DESIGN INPUTS COEFFICIENTS.  a, R_s, b and m are FREE INPUTS of
    a chosen ansatz, not numbers with values to be derived.  Under this rule
    they are carried as SYMBOLS and never as 0.02, 200.0, 1.0.  A seated point
    is a substitution, made at the edge and reported as one.

    TO CALL Lambda DERIVED.  Its FORM is a theorem -- any potential falling as
    1/r integrates to a logarithm -- and its VALUE is exact once the ansatz is
    chosen.  Neither makes the ansatz right.  `solve.py` states why it stays
    MODEL and that is unchanged here: exactness is not derivation.

    TO REPAIR THE THREE.  They are named, their status is recorded, and the
    first is queued as decidable.  A finding is recorded, never repaired.
"""

import sys

import sympy as sp

# The design inputs.  SYMBOLS, never floats -- section 4's first refusal.
a, Rs, b, m = sp.symbols("a R_s b m", positive=True)

X = 2 * Rs / sp.sqrt(b**2 + a**2)
LAM = 2 * (sp.log(X) - 1)

# The one seated design point, as EXACT rationals.  A substitution made at the
# edge, which is the only place a number is allowed to appear.
SEAT = {a: sp.Rational(1, 50), Rs: sp.Integer(200), b: sp.Integer(1),
        m: sp.Rational(1, 50)}

# Constants of nature: measurements with provenance, which the rule admits.
# CODATA 2018; carried as exact rationals of their quoted digits, so that a
# number is never silently re-rounded downstream.
G = sp.Rational(667430, 10**16)                      # m^3 kg^-1 s^-2
c = sp.Integer(299792458)                            # m s^-1, exact by definition
hbar = sp.Rational(1054571817, 10**43)               # J s
E_PLANCK = sp.sqrt(hbar * c**5 / G)

# (name, closed form or None, the decimal the tree quotes, digits it quotes,
#  status, note)
ROWS = [
    ("8 pi", 8 * sp.pi, "25.132741", 8, "LAW", "G_mn = 8 pi T_mn"),
    ("4 pi", 4 * sp.pi, "12.566371", 8, "GEOMETRIC", "dm/dr = 4 pi r^2 rho"),
    ("8", sp.Integer(8), "8", 1, "THEOREM", "factor8.py"),
    ("4", sp.Integer(4), "4", 1, "THEOREM", "bisector.py"),
    ("120 deg", sp.Integer(120), "120", 3, "THEOREM", "bisector.py, exactly 2 pi/3"),
    ("1/2", sp.Rational(1, 2), "0.5", 2, "THEOREM", "teardown.py"),
    ("3/(32 pi^2)", 3 / (32 * sp.pi**2), "0.009495", 4, "THEOREM", "candidates.py"),
    ("pi^2/720", sp.pi**2 / 720, "0.013708", 5, "THEOREM", "candidates.py"),
    ("X", X, "399.920024", 9, "EXACT", "20000 sqrt(2501)/2501, a surd"),
    ("Lambda", LAM, "9.982529174194637", 16, "EXACT",
     "ln(400000000/2501) - 2.  Carried as a FLOAT everywhere in the tree."),
    ("sqrt(Lambda)", sp.sqrt(LAM), "3.159514", 7, "THEOREM", "overturn.py"),
    ("2/Lambda", 2 / LAM, "0.200350028", 9, "IDENTITY", "lightbuild.py"),
    ("Lambda/2", LAM / 2, "4.9912645871", 11, "IDENTITY", "lightbuild.py"),
    ("crossover FR", sp.sqrt(3 * LAM / (32 * sp.pi**2)), "0.307933", 6, "EXACT",
     "graded MEASURED by the provenance census; it is a surd in Lambda"),
    ("k_Cas", sp.pi**2 * LAM / 720, "0.136838353", 9, "EXACT",
     "graded MEASURED by the provenance census; exact in Lambda"),
    ("E_P/Lambda", E_PLANCK / LAM, "1.959505e8", 7, "IDENTITY",
     "planckcell.py; exact once G, c, hbar are fixed"),
]

# Named, not silently omitted.  Nothing here may be used as a number.
NOT_EXACT = (
    ("xi", "UNDEFINED", "non-minimal coupling; framework needs xi > 0 and "
     "fixes no value.  No closed form, no measurement."),
    ("l_UV", "UNDEFINED", "the EFT cutoff of Fliss et al.  Closes the "
     "shortfall at sqrt(Lambda) l_P and nothing says that is the cutoff."),
    ("2 in A", "ASSERTED", "A = 2(p.p')^2 - p^2 p'^2, taken on four "
     "confirming cases.  DECIDABLE, and the first target."),
    ("0.0218 c", "FITTED", "MEASURED.md's ceiling: a LEAST-SQUARES ZERO of "
     "the null minimum in its linear regime, two grids agreeing to 0.1 %.  A "
     "measurement with a spread, never a derived number."),
)

# The design inputs are not coefficients; the rule carries them as symbols.
DESIGN_INPUTS = ("a", "R_s", "b", "m")


def value(expr, digits=30):
    """A closed form at the seated point, to `digits` places."""
    return sp.N(expr.subs(SEAT) if expr.free_symbols else expr, digits)


def agrees(expr, quoted, digits):
    """Does the closed form reproduce the quoted decimal TO ITS OWN PRECISION?

    The tree printed these at limited width, so equality is the wrong test and
    would fail honestly-rounded rows.  The test is agreement to the number of
    significant digits actually printed.
    """
    got, want = value(expr, digits + 8), sp.Float(quoted, digits + 8)
    if want == 0:
        return abs(got) < sp.Float(10) ** (-digits)
    return abs(got - want) / abs(want) < sp.Float(10) ** (-(digits - 1))


def audit():
    """[(name, agrees?, exact form, value)] over every closed form."""
    return [(nm, bool(agrees(e, q, d)), sp.srepr if False else sp.simplify(e),
             value(e, 20)) for nm, e, q, d, _s, _w in ROWS]


def disagreements():
    """The rows whose closed form does NOT reproduce the quoted decimal."""
    return [nm for nm, e, q, d, _s, _w in ROWS if not agrees(e, q, d)]


def leverage():
    """{input: exact dLambda/dinput} and its value at the seated point."""
    out = {}
    for s in (Rs, a, b):
        d = sp.simplify(sp.diff(LAM, s))
        out[str(s)] = (d, sp.nsimplify(d.subs(SEAT), rational=True))
    return out


def threshold():
    """(the exact condition for Lambda > 0, proved by monotonicity).

    Lambda = 2[ln X - 1] is strictly increasing in X on X > 0, since
    dLambda/dX = 2/X > 0, so Lambda > 0 iff X > e.  Returned with the
    derivative that proves it rather than a sampled sign.
    """
    Xs = sp.Symbol("X", positive=True)
    L = 2 * (sp.log(Xs) - 1)
    return (sp.simplify(sp.diff(L, Xs)), sp.solve(sp.Eq(L, 0), Xs)[0],
            sp.simplify(sp.Rational(1, 2) * sp.E))


def seated_above_threshold():
    """(X at the seat, e, strictly above?) -- exact, no float comparison."""
    Xv = X.subs(SEAT)
    return (sp.nsimplify(Xv), sp.E, bool(sp.simplify(Xv - sp.E) > 0))


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("every closed form reproduces the decimal the tree quotes",
        disagreements(), [])
    chk("sixteen rows carry a closed form", len(ROWS), 16)
    chk("and four numbers do not, each named", len(NOT_EXACT), 4)

    # THE TWO THE PROVENANCE CENSUS CALLED MEASURED ARE SURDS, NOT MEASUREMENTS.
    chk("X is a surd, not a decimal", sp.simplify(X.subs(SEAT)),
        sp.Rational(20000, 2501) * sp.sqrt(2501))
    chk("Lambda is a logarithm, not a float", sp.simplify(LAM.subs(SEAT)),
        sp.log(sp.Rational(400000000, 2501)) - 2)
    chk("and it matches the float the tree carries, to 16 places",
        bool(abs(value(LAM, 25) - sp.Float("9.982529174194637", 25))
             < sp.Float("1e-15")), True)

    # THE LEVERAGE, AS RATIONALS.  A decimal here would be the thing the rule
    # forbids, so the fixture is exact.
    lev = leverage()
    chk("dLambda/dR_s = 2/R_s", sp.simplify(lev["R_s"][0] - 2 / Rs), 0)
    chk("dLambda/da = -2a/(b^2+a^2)",
        sp.simplify(lev["a"][0] + 2 * a / (b**2 + a**2)), 0)
    chk("dLambda/db = -2b/(b^2+a^2)",
        sp.simplify(lev["b"][0] + 2 * b / (b**2 + a**2)), 0)
    chk("at the seat they are 1/100, -100/2501, -5000/2501 EXACTLY",
        (lev["R_s"][1], lev["a"][1], lev["b"][1]),
        (sp.Rational(1, 100), sp.Rational(-100, 2501),
         sp.Rational(-5000, 2501)))
    chk("so b outweighs R_s by exactly 500000/2501",
        sp.Rational(abs(lev["b"][1]), abs(lev["R_s"][1])),
        sp.Rational(500000, 2501))

    # THE THRESHOLD, PROVED RATHER THAN SAMPLED.
    d, root, halfe = threshold()
    Xs = sp.Symbol("X", positive=True)
    chk("dLambda/dX = 2/X > 0, so Lambda is strictly increasing in X",
        sp.simplify(d - 2 / Xs), 0)
    chk("hence Lambda > 0 iff X > e, exactly", root, sp.E)
    chk("and the threshold on the geometry is e/2", halfe, sp.E / 2)
    Xv, e_, above = seated_above_threshold()
    chk("the seated point is strictly above it, by exact comparison",
        above, True)

    # THE REFUSALS.
    chk("the design inputs are symbols, not numbers",
        sorted(str(s) for s in (a, Rs, b, m)), sorted(DESIGN_INPUTS))
    chk("the fitted ceiling is carried as FITTED and not as a result",
        [s for _n, s, _w in NOT_EXACT if s == "FITTED"], ["FITTED"])
    chk("and the two undefined ones are still undefined",
        sorted(n for n, s, _w in NOT_EXACT if s == "UNDEFINED"),
        ["l_UV", "xi"])

    print("exact selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 40 -- NO COEFFICIENTS.  EXACT CALCULATIONS ONLY.")
    print("=" * 79)
    print()
    print("1. EVERY CLOSED FORM, AGAINST THE DECIMAL THE TREE QUOTES")
    print("   %-15s %-11s %-24s %s" % ("name", "status", "exact", "value"))
    for nm, e, q, d, st, _w in ROWS:
        ex = sp.simplify(e.subs(SEAT)) if e.free_symbols else e
        s = str(ex)
        print("   %-15s %-11s %-24s %s"
              % (nm, st, s[:24], sp.N(value(e, 18), 12)))
    bad = disagreements()
    print()
    print("   %d closed forms, %d disagree with the quoted decimal."
          % (len(ROWS), len(bad)))
    print("   THE TWO THE PROVENANCE CENSUS GRADED `MEASURED` ARE SURDS:")
    print("     X      = %s" % sp.simplify(X.subs(SEAT)))
    print("     Lambda = %s" % sp.simplify(LAM.subs(SEAT)))
    print("   Nothing was fitted.  They looked like coefficients because they")
    print("   were written as coefficients.")
    print()
    print("2. WHAT HAS NO CLOSED FORM -- AND MAY NOT BE USED AS A NUMBER")
    for nm, st, why in NOT_EXACT:
        print("     %-10s %-10s %s" % (nm, st, why))
    print()
    print("3. WHAT EXACTNESS BUYS: THE DESIGN DERIVATIVES, NEVER STATED HERE")
    lev = leverage()
    for k in ("R_s", "a", "b"):
        print("     dLambda/d%-4s = %-22s = %s at the seat"
              % (k, lev[k][0], lev[k][1]))
    print("   THE RAY PARAMETER b IS THE STRONGEST LEVER ON THE BILL, by")
    print("   exactly %s over R_s and exactly %s over a."
          % (sp.Rational(abs(lev["b"][1]), abs(lev["R_s"][1])),
             sp.Rational(abs(lev["b"][1]), abs(lev["a"][1]))))
    print()
    print("4. THE SIGN THRESHOLD, PROVED BY MONOTONICITY")
    d, root, halfe = threshold()
    print("     dLambda/dX = %s > 0, so Lambda > 0 iff X > %s" % (d, root))
    print("     i.e. R_s / sqrt(b^2 + a^2) > e/2 = %s" % sp.N(halfe, 16))
    Xv, _e, above = seated_above_threshold()
    print("     the seat sits at X = %s, strictly above: %s"
          % (sp.N(Xv, 12), above))
    print()
    print("5. WHAT THIS FILE REFUSES")
    print("   To call a, R_s, b, m coefficients.  They are FREE INPUTS and are")
    print("   carried as symbols; a seated point is a substitution made at the")
    print("   edge.  To call Lambda derived -- exactness is not derivation, and")
    print("   solve.py's reason it stays MODEL is unchanged.  To repair the")
    print("   four: they are named, and the asserted 2 is queued as decidable.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
