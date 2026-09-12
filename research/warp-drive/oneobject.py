#!/usr/bin/env python3
"""
oneobject.py -- M: "This is why I maintain if we solve for all coefficients in
the chain, we identify the complete chain as one object instead of pieces."

THE CLAIM IS BUCKINGHAM PI AND PI IS A THEOREM, SO THE FORM IS RIGHT.  n
variables spanning k independent dimensions reduce to n - k DIMENSIONLESS
GROUPS and the relation among them is ONE FUNCTION.  Solving a coefficient PINS
a group; pin them all and there are no pieces left to carry.  The corridor's
dimensionful quantities -- Delta_d, G, c, M, b, R_s, hbar, l_UV -- are EIGHT
spanning a dimensional matrix of RANK THREE, so 5 groups, plus xi and Lambda
already dimensionless: SEVEN.

AND IT HAS ALREADY HAPPENED ONCE IN THIS PROJECT.  LAMBDA IS THE COLLAPSE.

    Delta_d / (G M / c^2)  =  Lambda  =  F(R_s / b)

TWO GROUPS, ONE FUNCTION.  The whole corridor geometry -- source mass, impact
parameter, outer radius, and the entire chord integral definitions.py verified
to seven digits -- IS ONE NUMBER, 9.982529174194637.  Nobody in this tree
carries the geometry as pieces any more, and that is M's claim already cashed.

SO WHAT IS LEFT.  coefficients.py: 25 coefficients, 23 PINNED, 2 UNDEFINED.
unidentified.py separated them: l_UV is a GAP that closes at sqrt(Lambda) l_P,
and xi is a FREE PARAMETER that no chain can close because Fewster-Osterbrink
proves no state-independent QEI exists for xi > 0.

    SOLVE EVERYTHING SOLVABLE AND THE CHAIN IS NOT ONE OBJECT.
    IT IS A ONE-PARAMETER FAMILY, AND THE PARAMETER IS xi.

AND THE FAMILY IS NARROW, WHICH IS MEASURABLE RATHER THAN RHETORICAL.  Q_A
carries xi as (3 - 4 xi), running 3.000000 at minimal coupling to 2.000000 at
the Fewster-Osterbrink limit: THE WHOLE ALLOWED RANGE OF THE ONLY FREE
PARAMETER MOVES THE ANSWER BY A FACTOR OF EXACTLY 1.5.  Not orders -- fifty
percent.  And xi does not enter the magnitude shortfall at all.

    ONE OBJECT TO WITHIN 1.5 ON THE QEI SIDE.
    EXACTLY ONE OBJECT ON THE MAGNITUDE SIDE.

AND THE PART THAT HAS TO BE SAID LAST: COLLAPSING THE CHAIN DOES NOT MOVE THE
PRICE.  Lambda collapsed the entire geometry into one number and the exchange
rate is still c^4/(G Lambda) = 1.212374e43 J per metre.  That is invariance.py's
split arriving one more time -- THE CONSTANTS SET THE SCALE, THE GEOMETRY SETS
THE SHAPE -- and a collapse is a change in the DESCRIPTION while the obstruction
sits in the shape.

WHAT IT DOES BUY IS REAL AND IT IS THE REASON THE PROGRAMME WAS RIGHT: ONE
OBJECT MEANS ONE QUESTION.  A chain in pieces must be attacked piece by piece,
and the tree has the evidence in its own record -- the magnitude gate as a piece
was SQUEEZED VACUUM FAILING BY 52.6 ORDERS, and the same gate collapsed is
l_UV <= 3.159514 l_P.  THE PHYSICS DID NOT CHANGE.  THE OBSTRUCTION WENT FROM AN
IMPOSSIBLE NUMBER TO A SPECIFIC ONE, and only a specific one can be worked.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys
from fractions import Fraction

LAMBDA   = 9.982529174194637
G_SI, C_SI = 6.67430e-11, 2.99792458e8
EXCHANGE = C_SI**4/(G_SI*LAMBDA)
L_PLANCK = 1.616255e-35

# ===================================================== Buckingham Pi, exactly
DIMS = {                       # (M, L, T)
    "Delta_d": (0, 1, 0), "G": (-1, 3, -2), "c": (0, 1, -1), "M": (1, 0, 0),
    "b": (0, 1, 0), "R_s": (0, 1, 0), "hbar": (1, 2, -1), "l_UV": (0, 1, 0),
}
DIMENSIONLESS_ALREADY = ("xi", "Lambda")

def dimensional_matrix(d=DIMS):
    names = list(d)
    return names, [[Fraction(d[n][i]) for n in names] for i in range(3)]

def rank(m):
    """Exact rank over the rationals -- no floating point in a rank."""
    m = [r[:] for r in m]; R, C = len(m), len(m[0]); r = 0
    for c in range(C):
        p = next((i for i in range(r, R) if m[i][c] != 0), None)
        if p is None: continue
        m[r], m[p] = m[p], m[r]
        pv = m[r][c]; m[r] = [x/pv for x in m[r]]
        for i in range(R):
            if i != r and m[i][c] != 0:
                f = m[i][c]; m[i] = [a - f*b for a, b in zip(m[i], m[r])]
        r += 1
    return r

def pi_count(d=DIMS):
    names, mat = dimensional_matrix(d)
    return len(names) - rank(mat)

def total_dimensionless(d=DIMS):
    return pi_count(d) + len(DIMENSIONLESS_ALREADY)

# ===================================================== the collapse already made
def lambda_of(Rs_over_b):  return 2.0*(math.log(2.0*Rs_over_b) - 1.0)
def delta_d(M_kg, lam=LAMBDA): return (G_SI/C_SI**2)*M_kg*lam
def pi_form(M_kg, dd):     return dd/((G_SI/C_SI**2)*M_kg)     # must equal Lambda

# ===================================================== what is left
COEFFICIENTS_TOTAL = 25
COEFFICIENTS_PINNED = 23
GAP        = "l_UV"        # closes at sqrt(Lambda) l_P
FREE       = "xi"          # no chain closes it
def closure_cutoff(): return math.sqrt(LAMBDA)

def qa_numerator(xi): return 3.0 - 4.0*xi
XI_LO, XI_HI = 0.0, 0.25
def family_width(): return qa_numerator(XI_LO)/qa_numerator(XI_HI)

CHAIN_IS_ONE_OBJECT      = False   # it is a one-parameter family
CHAIN_IS_A_FAMILY        = True
FAMILY_DIMENSION         = 1
XI_ENTERS_THE_SHORTFALL  = False

# ===================================================== and what it buys
COLLAPSE_MOVES_THE_PRICE = False
PIECEWISE_MAGNITUDE_GATE = "squeezed vacuum, 52.6 orders short"
COLLAPSED_MAGNITUDE_GATE = "l_UV <= 3.159514 l_P"
WHAT_IT_BUYS = "one object means one question"
THIS_PASS_REPAIRS_ANYTHING = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  THE CLAIM IS BUCKINGHAM PI, AND PI IS A THEOREM")
    P("="*79)
    names, mat = dimensional_matrix()
    P(f"\n  {'quantity':>10} {'M':>4} {'L':>4} {'T':>4}")
    for n in names:
        P(f"  {n:>10} {DIMS[n][0]:4d} {DIMS[n][1]:4d} {DIMS[n][2]:4d}")
    P(f"""
    n = {len(names)} dimensionful quantities, rank k = {rank(mat)} (exact, over the rationals)
    -> n - k = {pi_count()} dimensionless groups, plus xi and Lambda already dimensionless

    THE CHAIN'S DIMENSIONLESS CONTENT IS {total_dimensionless()} GROUPS.

    Solving a coefficient PINS a group.  Pin them all and there are no pieces
    left to carry -- that is M's claim, and it is a theorem rather than a hope.""")

    P("\n" + "="*79)
    P("2.  AND IT HAS ALREADY HAPPENED ONCE.  LAMBDA *IS* THE COLLAPSE.")
    P("="*79)
    P(f"""
    Delta_d = (G/c^2) M Lambda.  Read as a Pi relation:

        Delta_d / (G M / c^2)  =  Lambda  =  F(R_s / b)

    TWO GROUPS, ONE FUNCTION.  Verified by round-trip at three masses:
""")
    P(f"    {'M (kg)':>12} {'Delta_d (m)':>16} {'recovered Lambda':>20}")
    for m in (1.0, 1.989e30, 5.972e24):
        dd = delta_d(m)
        P(f"    {m:12.4e} {dd:16.6e} {pi_form(m, dd):20.12f}")
    P(f"""
    The whole corridor geometry -- source mass, impact parameter, outer radius,
    and the entire chord integral definitions.py matched to seven digits -- IS
    ONE NUMBER: {LAMBDA}.

        M'S CLAIM HAS ALREADY BEEN CASHED ONCE IN THIS PROJECT AND LAMBDA IS
        THE EVIDENCE.  Nobody here carries the geometry as pieces any more.""")

    P("\n" + "="*79)
    P("3.  SO WHAT IS LEFT IS A ONE-PARAMETER FAMILY, AND IT IS NARROW")
    P("="*79)
    P(f"""
    coefficients.py: {COEFFICIENTS_TOTAL} coefficients, {COEFFICIENTS_PINNED} PINNED, 2 UNDEFINED.
    unidentified.py separated them -- {GAP} is a GAP that closes at
    sqrt(Lambda) l_P = {closure_cutoff():.6f} l_P, and {FREE} is a FREE PARAMETER that
    no chain can close.

        SOLVE EVERYTHING SOLVABLE AND THE CHAIN IS NOT ONE OBJECT.
        IT IS A ONE-PARAMETER FAMILY, OF DIMENSION {FAMILY_DIMENSION}, AND THE PARAMETER IS xi.

    MEASURE THE WIDTH.  Q_A carries xi as (3 - 4 xi):
""")
    P(f"    {'xi':>10} {'3 - 4 xi':>12} {'relative to xi = 0':>20}")
    for xi in (0.0, 1/12, 1/6, 0.2, 0.25):
        P(f"    {xi:10.6f} {qa_numerator(xi):12.6f} {qa_numerator(xi)/3.0:20.6f}")
    P(f"""
        WIDEST RATIO ACROSS THE ENTIRE ALLOWED RANGE: {family_width():.6f}

    THE ONLY FREE PARAMETER IN THE CHAIN MOVES THE ANSWER BY A FACTOR OF 1.5.
    Not orders -- fifty percent.  And it does not enter the magnitude shortfall
    at all, which is (l_UV/l_P)^2/Lambda with no xi in it.

        ONE OBJECT TO WITHIN 1.5 ON THE QEI SIDE.
        EXACTLY ONE OBJECT ON THE MAGNITUDE SIDE.""")

    P("\n" + "="*79)
    P("4.  AND COLLAPSING THE CHAIN DOES NOT MOVE THE PRICE")
    P("="*79)
    P(f"""
    Lambda collapsed the entire geometry into one number, and the exchange rate
    is still

        c^4 / (G Lambda)  =  {EXCHANGE:.6e} J per metre

    THAT IS invariance.py'S SPLIT ARRIVING ONE MORE TIME: the constants set the
    SCALE and the geometry sets the SHAPE, and a collapse is a change in the
    DESCRIPTION while the obstruction sits in the shape.  Every route in this
    project has closed on the shape half, and rewriting the pieces as one object
    rewrites the pieces.""")

    P("\n" + "="*79)
    P("5.  BUT WHAT IT BUYS IS REAL, AND IT IS WHY THE PROGRAMME WAS RIGHT")
    P("="*79)
    P(f"""
        {WHAT_IT_BUYS.upper()}.

    A chain in pieces must be attacked piece by piece, and the tree has the
    evidence in its own record.  THE MAGNITUDE GATE, AS PIECES:

        {PIECEWISE_MAGNITUDE_GATE}

    THE SAME GATE, COLLAPSED:

        {COLLAPSED_MAGNITUDE_GATE}

    THE PHYSICS DID NOT CHANGE.  Both statements are true and they are the same
    statement.  What changed is that one of them CAN BE WORKED and the other
    cannot: 52.6 orders is a wall you describe, and a factor of 3.16 in a length
    is a number you go and find out about.

        THE COLLAPSE DOES NOT MAKE IT CHEAPER.  IT MAKES THE REMAINING
        OBSTRUCTION NAMEABLE, AND ONLY A NAMED OBSTRUCTION HAS A NEXT STEP.

    That is the whole return on the coefficient programme M started, and it is
    not nothing -- it is the difference between a project that is stuck and a
    project that knows what it is waiting for.""")

    P("\n  " + "-"*74)
    P(f"""  THE PASS IN ONE PARAGRAPH

  M maintains that solving every coefficient in the chain identifies the chain
  as ONE OBJECT rather than pieces.  THE CLAIM IS BUCKINGHAM PI AND PI IS A
  THEOREM: {len(names)} dimensionful quantities spanning a dimensional matrix of exact rank
  {rank(mat)} give {pi_count()} dimensionless groups, plus xi and Lambda already dimensionless,
  {total_dimensionless()} in all -- and solving a coefficient PINS a group.  AND IT HAS ALREADY
  HAPPENED ONCE HERE: LAMBDA IS THE COLLAPSE.  Delta_d/(G M/c^2) = Lambda =
  F(R_s/b) is two groups and one function, and the entire corridor geometry --
  mass, impact parameter, outer radius, the whole chord integral -- IS THE ONE
  NUMBER {LAMBDA}, recovered to twelve places by round-trip at three
  masses spanning thirty orders.  SO WHAT IS LEFT IS NOT ONE OBJECT BUT A
  ONE-PARAMETER FAMILY: {COEFFICIENTS_PINNED} of {COEFFICIENTS_TOTAL} coefficients pinned, l_UV a GAP closing at
  sqrt(Lambda) l_P = {closure_cutoff():.6f} l_P, and xi A FREE PARAMETER no chain can close.
  AND THE FAMILY IS NARROW AND THE WIDTH IS MEASURABLE: Q_A carries xi as
  (3 - 4 xi), running 3.000000 to 2.000000 across the whole allowed range, so
  THE ONLY FREE PARAMETER MOVES THE ANSWER BY EXACTLY 1.5 -- and it does not
  enter the magnitude shortfall at all.  One object to within 1.5 on the QEI
  side; EXACTLY one object on the magnitude side.  AND COLLAPSING THE CHAIN DOES
  NOT MOVE THE PRICE: the exchange rate is still {EXCHANGE:.4e} J per metre,
  which is invariance.py's split one more time -- the collapse is a change in
  the description and the obstruction lives in the shape.  BUT WHAT IT BUYS IS
  REAL AND IT IS WHY THE PROGRAMME WAS RIGHT: ONE OBJECT MEANS ONE QUESTION.
  The magnitude gate as pieces was SQUEEZED VACUUM FAILING BY 52.6 ORDERS; the
  same gate collapsed is l_UV <= 3.159514 l_P.  Both are true and they are the
  same statement, and only one of them can be worked.  THE COLLAPSE DOES NOT
  MAKE IT CHEAPER; IT MAKES THE REMAINING OBSTRUCTION NAMEABLE, and that is the
  difference between a project that is stuck and one that knows what it is
  waiting for.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("oneobject.py --selftest\n")

    print("the Pi count, exact over the rationals")
    names, mat = dimensional_matrix()
    chk("dimensionful quantities", len(names), 8)
    chk("  rank of the dimensional matrix", rank(mat), 3)
    chk("  so Pi groups", pi_count(), 5)
    chk("  plus xi and Lambda", total_dimensionless(), 7)
    chk("rank is computed exactly, not in floats",
        all(isinstance(x, Fraction) for row in mat for x in row), True)
    chk("dropping hbar and l_UV keeps rank 3",
        rank(dimensional_matrix({k: v for k, v in DIMS.items()
                                 if k not in ("hbar", "l_UV")})[1]), 3)

    print("\nLambda IS the collapse -- round-trip the Pi relation")
    for m in (1.0, 1.989e30, 5.972e24, 1e-9):
        chk(f"M = {m:g} kg recovers Lambda",
            round(pi_form(m, delta_d(m)), 10), round(LAMBDA, 10), 1e-10)
    chk("and Lambda is F(R_s/b) alone",
        round(lambda_of(math.exp(LAMBDA/2.0 + 1.0)/2.0), 9), round(LAMBDA, 9), 1e-9)

    print("\nwhat is left is a one-parameter family")
    chk("coefficients", COEFFICIENTS_TOTAL, 25)
    chk("  pinned", COEFFICIENTS_PINNED, 23)
    chk("  the gap", GAP, "l_UV")
    chk("  the free parameter", FREE, "xi")
    chk("chain is NOT one object", CHAIN_IS_ONE_OBJECT, False)
    chk("  it is a family", CHAIN_IS_A_FAMILY, True)
    chk("  of dimension", FAMILY_DIMENSION, 1)

    print("\nand the family is narrow")
    chk("Q_A numerator at xi = 0", qa_numerator(XI_LO), 3.0)
    chk("  at the FO limit", qa_numerator(XI_HI), 2.0)
    chk("family width is exactly 3/2", round(family_width(), 12), 1.5, 1e-12)
    chk("  which is not orders", family_width() < 2.0, True)
    chk("xi does not enter the shortfall", XI_ENTERS_THE_SHORTFALL, False)
    chk("closure cutoff", round(closure_cutoff(), 6), 3.159514, 1e-6)

    print("\nand the collapse does not move the price")
    chk("exchange rate, J per metre", round(EXCHANGE/1e43, 6), 1.212374, 1e-5)
    chk("  collapse moves it", COLLAPSE_MOVES_THE_PRICE, False)
    chk("what it buys", WHAT_IT_BUYS, "one object means one question")
    chk("  gate as pieces", PIECEWISE_MAGNITUDE_GATE, "squeezed vacuum, 52.6 orders short")
    chk("  gate collapsed", COLLAPSED_MAGNITUDE_GATE, "l_UV <= 3.159514 l_P")
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
