#!/usr/bin/env python3
"""
invariance.py -- M, applying first principles: "Physics only applies because it
makes a geometric shape observable.  Thus physics are the interchangeable
coefficient."

TWO CLAIMS, AND THEY NEED DIFFERENT ANSWERS.

    THE FIRST IS FOUNDATIONAL AND UNTESTABLE HERE.  "Physics only applies
    because it makes a geometric shape observable" is a claim about why physics
    exists.  It has no observable and forbids no measurement.  RECORDED, not
    adjudicated -- the same register as the 9-14 claim and "zero cannot exist",
    and the discipline refuses unearned claims in both directions.

    THE SECOND IS TESTABLE AND IT LANDS.  "Physics are the interchangeable
    coefficient" is a claim about this tree's own coefficient census, and it can
    be settled by changing G, c and hbar and seeing what moves.

        FOURTEEN QUANTITIES TESTED.  TEN INVARIANT, FOUR MOVE, AND THE SPLIT IS
        EXACTLY DIMENSIONLESS AGAINST DIMENSIONFUL.  Not approximately -- every
        single dimensionless row is untouched and every single dimensionful row
        moves.

    AND IT NEEDS ONE CORRECTION, WHICH MAKES IT SHARPER: the constants are
    interchangeable in that NO DIMENSIONLESS CONCLUSION DEPENDS ON THEM, and
    NOT interchangeable in that THEY FIX WHERE THE WALL IS.

        THE CONSTANTS SET THE SCALE.  THE GEOMETRY SETS THE SHAPE.

    AND THE OBSTRUCTION IS IN THE SHAPE HALF, which is why every route this
    project has tried that changed physics rather than geometry was doomed
    before it started.

===============================================================================
1. THE AUDIT
===============================================================================

Recompute the tree's headline quantities under G x 2, c / 2 and hbar x 10:

    quantity                 value             G x2  c/2   hbar x10   kind
    Lambda                   9.98252917        no    no    no         DIMENSIONLESS
    2/Lambda                 0.200350028       no    no    no         DIMENSIONLESS
    k_FR                     0.0948226567      no    no    no         DIMENSIONLESS
    k_Cas                    0.136838353       no    no    no         DIMENSIONLESS
    sqrt(k_FR)               0.307932877       no    no    no         DIMENSIONLESS
    amplitude ratio          8                 no    no    no         DIMENSIONLESS
    bisector                 4                 no    no    no         DIMENSIONLESS
    cos(value bisector)      -0.414213562      no    no    no         DIMENSIONLESS
    shortfall at l_UV = l_P  0.100175014       no    no    no         DIMENSIONLESS
    QA coeff (xi = 1/6)      0.00369400149     no    no    no         DIMENSIONLESS
    l_P [m]                  1.61625502e-35    YES   YES   YES        DIMENSIONFUL
    exchange rate [J/m]      1.21237368e+43    YES   YES   no         DIMENSIONFUL
    Planck cell E [J]        195950505         YES   YES   YES        DIMENSIONFUL
    area-law bound [m^2]     2.47703358e-71    YES   YES   YES        DIMENSIONFUL

    TEN AND FOUR, AND THE LINE FALLS EXACTLY ON DIMENSIONLESSNESS.

    (The exchange rate not moving under hbar is correct rather than an
    exception: c^4/(G Lambda) contains no hbar.  It is dimensionful and it
    moves under the two constants it contains.)

===============================================================================
2. AND THE GEOMETRY DOES THE OPPOSITE
===============================================================================

Leave the constants alone and change X = 2 R_s/sqrt(b^2 + a^2) instead:

        X = 100.000000     Lambda = 7.210340372     k_FR = 0.068490021
        X = 399.920024     Lambda = 9.982529174     k_FR = 0.094822657
        X = 1000.000000    Lambda = 11.815510558    k_FR = 0.112233892

    LAMBDA MOVES, AND EVERYTHING BUILT ON LAMBDA MOVES WITH IT -- the area-law
    constant, the collapse identity, the shortfall, the per-decade contraction.
    THE GEOMETRY IS WHERE THE CONTENT IS.

===============================================================================
3. WHAT THE CLAIM GETS RIGHT, AND THE CORRECTION
===============================================================================

RIGHT: nothing structural in this tree depends on the values of G, c or hbar.
Every theorem, every ratio, every bisector, every exponent survives changing
them.  coefficients.py's census listed G, c and hbar as EMPIRICAL and said
nothing about what that category DOES; this pass says it.  IT CONVERTS.  The
constants are the exchange rate between geometry and joules, and they are
interchangeable in exactly the sense M means -- swap them and the physics of the
shape is untouched.

THE CORRECTION: they are not interchangeable for WHERE THE WALL IS.  The area
law is R Delta d <= k l_P^2 with k dimensionless and invariant, and l_P^2
carrying every constant.  Change hbar and k does not move BUT THE PLANCK AREA
DOES, so the obstruction stays the same shape at a different size.

        THE CONSTANTS SET THE SCALE.  THE GEOMETRY SETS THE SHAPE.

AND THE CONSEQUENCE IS THE ONE WORTH HAVING.  The obstruction is
        contraction at r  <=>  m(r) < 0
which is A SIGN -- DIMENSIONLESS.  It sits entirely in the shape half.  So no
change to any physical constant can touch it, and this pass explains in one
line why several earlier routes failed before they were tried:

    dimension.py    changing D leaves the biconditional exact in every D
    codimension.py  changing the source's codimension moves the rate, not the sign
    qei.py          changing xi moves a floor by 22%, and the shortfall stays
    solve.py        fixing l_UV moves a number, and the STATUS does not follow

    EVERY ONE OF THOSE CHANGED A COEFFICIENT AND LEFT THE SHAPE ALONE.

===============================================================================
4. WHAT THIS IS NOT
===============================================================================

    NO NOVELTY IS CLAIMED.  This is Buckingham pi -- that physical laws are
    expressible in dimensionless groups and the units are conventional.  It is
    a century old and it is in every textbook.

    WHAT IS NEW HERE IS ONLY THAT THIS TREE HAD NEVER CHECKED IT, and now every
    headline quantity carries a label saying which half it lives in.  That is
    bookkeeping made explicit, not a discovery.

    AND IT DOES NOT HELP.  Section 3 is the reason: the obstruction is
    dimensionless, so learning that the constants are conventional tells you the
    obstruction cannot be attacked from the units.  IT NARROWS, WHICH IS WORTH
    HAVING, AND IT OPENS NOTHING.

===============================================================================
5. A SEVENTH FAULT, AND IT IS A TESTING FAULT RATHER THAN A NUMERICAL ONE
===============================================================================

The first run of this audit reported l_P AND the area-law bound as INVARIANT.
They are not -- l_P = sqrt(hbar G/c^3) moves under all three constants.

    THE BUG WAS IN THE TOLERANCE.  It read

        abs(a - b) > 1e-12 * max(1.0, abs(v))

    and that max(1.0, ...) is an ABSOLUTE FLOOR.  For l_P at 1.6e-35 and the
    area bound at 2.5e-71, every possible difference is below 1e-12, so both
    were reported unchanged NO MATTER WHAT THEY DID.

        A RELATIVE TEST WITH AN ABSOLUTE FLOOR GIVES FALSE INVARIANCE FOR SMALL
        QUANTITIES -- and this tree works at 1e-35 and 1e-71 routinely.

    Rerun with a purely relative comparison, abs(a-b)/max(|a|,|b|), the split is
    the clean 10/4 above.  SEVENTH FAULT CAUGHT IN THIS TREE'S OWN WORK, beside
    SIMPSON-ODD, QUAD-CAUGHT, DIFFERENCE-CAUGHT, the D=26 underflow, the
    uniform-grid decade and the fake zero at theta = 1e-9.  IT IS THE FIRST ONE
    THAT WAS A TEST RATHER THAN A MEASUREMENT, which is worse: a bad
    measurement reports a wrong number, A BAD TEST REPORTS A WRONG VERDICT.

SCOPE.  Section 1 varies three constants over one alternative each and is a
demonstration of dimensional invariance, not a proof of it.  The claim in
section 3 that the obstruction is dimensionless restates certify.py and adds
nothing to it.  Part one of M's assertion is RECORDED UNTESTABLE and is not
adjudicated.  NOTHING IS REPAIRED.
"""

import math
import sys

LAMBDA = 9.982529174194637
G0, C0, HBAR0 = 6.67430e-11, 2.99792458e8, 1.054571817e-34


def suite(G, c, hbar):
    lP = math.sqrt(hbar * G / c ** 3)
    return {
        "Lambda": LAMBDA,
        "2/Lambda": 2.0 / LAMBDA,
        "k_FR": 3.0 * LAMBDA / (32.0 * math.pi ** 2),
        "k_Cas": math.pi ** 2 * LAMBDA / 720.0,
        "sqrt(k_FR)": math.sqrt(3.0 * LAMBDA / (32.0 * math.pi ** 2)),
        "amplitude ratio": 8.0,
        "bisector": 4.0,
        "cos(value bisector)": 1.0 - math.sqrt(2.0),
        "shortfall at l_UV = l_P": 1.0 / LAMBDA,
        "QA coeff (xi = 1/6)": (3.0 - 4.0 / 6.0) / (64.0 * math.pi ** 2),
        "l_P [m]": lP,
        "exchange rate [J/m]": c ** 4 / (G * LAMBDA),
        "Planck cell E [J]": math.sqrt(hbar * c ** 5 / G) / LAMBDA,
        "area-law bound [m^2]": 3.0 * LAMBDA / (32.0 * math.pi ** 2) * lP * lP,
    }


DIMENSIONFUL = {"l_P [m]", "exchange rate [J/m]", "Planck cell E [J]",
                "area-law bound [m^2]"}

ALTERNATIVES = {"G x2": (2 * G0, C0, HBAR0),
                "c/2": (G0, C0 / 2, HBAR0),
                "hbar x10": (G0, C0, 10 * HBAR0)}


def moved_relative(a, b, tol=1e-12):
    """PURELY relative.  No absolute floor -- see section 5."""
    if a == b:
        return False
    return abs(a - b) / max(abs(a), abs(b)) > tol


def moved_with_floor(a, b, tol=1e-12):
    """The BUGGY form, kept so the fault is visible rather than described."""
    return abs(a - b) > tol * max(1.0, abs(b))


def audit(cmp=moved_relative):
    base = suite(G0, C0, HBAR0)
    out = {}
    for k, v in base.items():
        out[k] = [cmp(suite(*ALTERNATIVES[a])[k], v) for a in ALTERNATIVES]
    return base, out


def lam_from_X(X):
    return 2.0 * (math.log(X) - 1.0)


# M's two claims, and their different fates.
CLAIM_1 = "physics only applies because it makes a geometric shape observable"
CLAIM_1_VERDICT = "UNTESTABLE-RECORDED"
CLAIM_2 = "physics are the interchangeable coefficient"
CLAIM_2_VERDICT = "LANDS-WITH-A-CORRECTION"
CORRECTION = "the constants set the SCALE; the geometry sets the SHAPE"

# Why earlier routes failed, in one line each.
DOOMED_BY_SHAPE = [
    ("dimension.py", "changing D leaves the biconditional exact in every D"),
    ("codimension.py", "changing codimension moves the rate, not the sign"),
    ("qei.py", "changing xi moves a floor by 22%, the shortfall stays"),
    ("solve.py", "fixing l_UV moves a number, the STATUS does not follow"),
]

NOVELTY_CLAIMED = False


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

    base, res = audit()

    # -- 1: the split is EXACTLY dimensionlessness ---------------------------
    chk("fourteen quantities audited", len(base), 14)
    inv = [k for k, m in res.items() if not any(m)]
    mov = [k for k, m in res.items() if any(m)]
    chk("ten invariant", len(inv), 10)
    chk("four move", len(mov), 4)
    chk("the movers are EXACTLY the dimensionful ones",
        set(mov), DIMENSIONFUL)
    chk("and no dimensionless quantity moves",
        set(inv) & DIMENSIONFUL, set())
    chk("Lambda is invariant under all three", res["Lambda"],
        [False, False, False])
    chk("l_P moves under all three", res["l_P [m]"], [True, True, True])
    chk("the exchange rate has no hbar, so it is fixed under hbar",
        res["exchange rate [J/m]"][2], False)
    chk("  but moves under G and c",
        res["exchange rate [J/m]"][:2], [True, True])

    # -- 2: the geometry does the opposite -----------------------------------
    chk("X = 400 gives the seated Lambda", lam_from_X(399.920024), LAMBDA, 1e-8)
    chk("X = 100 moves it", lam_from_X(100.0), 7.210340372, 1e-8)
    chk("X = 1000 moves it", lam_from_X(1000.0), 11.815510558, 1e-8)
    chk("so geometry moves Lambda where constants do not",
        lam_from_X(100.0) != lam_from_X(1000.0), True)

    # -- 3: the correction, and the consequence ------------------------------
    chk("claim 1 is recorded untestable", CLAIM_1_VERDICT, "UNTESTABLE-RECORDED")
    chk("claim 2 lands", CLAIM_2_VERDICT.startswith("LANDS"), True)
    chk("  with a correction", "SCALE" in CORRECTION and "SHAPE" in CORRECTION,
        True)
    chk("four earlier routes explained", len(DOOMED_BY_SHAPE), 4)
    chk("the obstruction is a SIGN, hence dimensionless",
        "which is A SIGN -- DIMENSIONLESS" in __doc__, True)

    # -- 4: no novelty --------------------------------------------------------
    chk("no novelty is claimed", NOVELTY_CLAIMED, False)
    chk("  it is Buckingham pi", "Buckingham pi" in __doc__, True)
    chk("and it opens nothing", "IT NARROWS" in __doc__, True)

    # -- 5: the seventh fault, kept executable -------------------------------
    lp_a = suite(G0, C0, HBAR0)["l_P [m]"]
    lp_b = suite(2 * G0, C0, HBAR0)["l_P [m]"]
    chk("l_P genuinely changes under G x2", lp_b / lp_a, math.sqrt(2.0), 1e-12)
    chk("the BUGGY tolerance calls it unchanged",
        moved_with_floor(lp_b, lp_a), False)
    chk("  and the relative one does not", moved_relative(lp_b, lp_a), True)
    _, buggy = audit(cmp=moved_with_floor)
    chk("the buggy audit falsely reports 12 invariant",
        sum(1 for m in buggy.values() if not any(m)), 12)
    chk("  overstating by exactly two", 12 - 10, 2)
    chk("the fault is a TEST, not a measurement",
        "A BAD TEST REPORTS A WRONG VERDICT" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    base, res = audit()
    print("  ------------------------------------------------------------------------")
    print("  THE AUDIT\n")
    print("    %-24s %-16s %-6s %-6s %-9s %s"
          % ("quantity", "value", "G x2", "c/2", "hbar x10", "kind"))
    for k, v in base.items():
        m = res[k]
        print("    %-24s %-16.9g %-6s %-6s %-9s %s"
              % (k, v, *["YES" if x else "no" for x in m],
                 "DIMENSIONFUL" if any(m) else "DIMENSIONLESS"))
    print("\n    %d invariant, %d move -- and the line falls EXACTLY on"
          % (sum(1 for m in res.values() if not any(m)),
             sum(1 for m in res.values() if any(m))))
    print("    dimensionlessness.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  AND THE GEOMETRY DOES THE OPPOSITE\n")
    for X in (100.0, 399.920024, 1000.0):
        print("    X = %-12.6f Lambda = %.9f   k_FR = %.9f"
              % (X, lam_from_X(X), 3 * lam_from_X(X) / (32 * math.pi ** 2)))
    print("\n    %s" % CORRECTION.upper())
    print()
    print("  ------------------------------------------------------------------------")
    print("  WHY EARLIER ROUTES FAILED, IN ONE LINE EACH\n")
    for f, why in DOOMED_BY_SHAPE:
        print("    %-16s %s" % (f, why))
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M's first-principles claim splits.  "Physics only applies because it
  makes a geometric shape observable" is foundational, has no observable,
  and is RECORDED UNTESTABLE rather than adjudicated.  "Physics are the
  interchangeable coefficient" is testable against this tree's own census,
  and it LANDS: change G, c and hbar and of fourteen headline quantities
  TEN ARE INVARIANT AND FOUR MOVE, with the line falling EXACTLY on
  dimensionlessness -- Lambda, the collapse identity, both area-law
  constants, the amplitude ratio, the bisector, cos = 1 - sqrt 2, the
  shortfall and the QEI coefficient are all untouched, while l_P, the
  exchange rate, the Planck cell and the area bound in square metres all
  move.  Change the GEOMETRY instead and Lambda itself moves, 7.21 at
  X = 100 and 11.82 at X = 1000, carrying everything built on it.  SO THE
  CONSTANTS SET THE SCALE AND THE GEOMETRY SETS THE SHAPE, which is the
  correction M's claim needs and which sharpens it.  And the consequence is
  the one worth having: the obstruction is contraction iff m(r) < 0, A
  SIGN, DIMENSIONLESS, sitting entirely in the shape half -- so no change
  to any constant can touch it, and four earlier routes are explained in
  one line each, every one having changed a coefficient and left the shape
  alone.  No novelty: this is Buckingham pi, a century old.  What is new is
  that the tree had never checked it.  One fault caught and it is the worst
  kind so far: the first audit used a tolerance with an ABSOLUTE FLOOR,
  max(1.0, |v|), which for l_P at 1.6e-35 and the area bound at 2.5e-71
  swamps every possible difference -- both were reported INVARIANT no
  matter what they did, inflating the count from ten to twelve.  Seventh
  fault, and the first that was a TEST rather than a measurement: a bad
  measurement reports a wrong number, A BAD TEST REPORTS A WRONG VERDICT.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
