#!/usr/bin/env python3
"""
unidentified.py -- M: "Not about our method.  About the work.  Three clause
failures means an unidentified candidate."  Folded: "a gap in a complete math
chain can be triangulated and answered by ANY three other identified data points
in the chain."

THE FOLDED CLAIM IS TRUE FOR GAPS AND FALSE FOR FREE PARAMETERS, AND THE
CORRIDOR'S CHAIN CONTAINS ONE OF EACH -- which is why "any three" is the one
word in it that does not survive.

THE CONFIGURATION M NAMED IS REAL AND IT IS ALREADY IN THE TREE.  candidates.py
opens: "All three fail, they fail at DIFFERENT PLACES, and the way they fail is
more informative than the verdict."  Four candidates against three gates, and
the failures land on all three:

    negative effective mass   FAILS KIND        m* is band curvature, not T_00
    Casimir                   FAILS DEADLINE    switching means MOVING PLATES
                              and MAGNITUDE
    squeezed vacuum           FAILS MAGNITUDE   by 52.6 orders at 1 nm
    non-minimal coupling      FAILS MAGNITUDE   by a PURE NUMBER, not orders

TRIANGULATE THEM AND THE MISSING CANDIDATE IS SPECIFIED:

    a GENUINE T_00 < 0            (from the KIND failure)
    FIELD-THEORETIC switching     (from the DEADLINE failure)
    l_UV <= sqrt(Lambda) l_P      (from the MAGNITUDE failures)
                = 3.159514 l_P

AND THAT NUMBER WAS ALREADY SEATED.  coefficients.py, censusing 25 coefficients
and finding exactly two UNDEFINED, records verbatim: "the shortfall is then the
pure number (l_UV/l_P)^2 / Lambda.  IT CLOSES AT l_UV = sqrt(Lambda) l_P =
3.159514 l_P and nothing here says whether that [is reachable]."  I reached it
from the failure matrix and that file reached it from the coefficient census,
and THESE ARE NOT TWO INDEPENDENT CONFIRMATIONS -- it is one derivation walked
from two ends.  Saying otherwise would be a fifth route to the same fault.

WHICH MAKES THIS THE THIRD TIME IN THREE PASSES THAT THE TREE ALREADY HELD THE
ANSWER: invariance.py held Duff's theorem, index3.py held register 2.17.3, and
coefficients.py held sqrt(Lambda) l_P.  BY M'S OWN CLAIM THREE INSTANCES
TRIANGULATE, and what they intersect at is specific:

    THE TREE INDEXES BY PROVENANCE, NOT BY APPLICABILITY.  Every one of the
    three was computed correctly, recorded correctly, and filed under the
    question that PRODUCED it rather than the question it ANSWERS.

AND THE TWO UNDEFINED COEFFICIENTS ARE UNDEFINED IN DIFFERENT SENSES, which no
pass had separated.  l_UV IS A GAP and the chain closes it.  xi IS A FREE
PARAMETER and no chain can: Fewster-Osterbrink proves NO STATE-INDEPENDENT QEI
EXISTS for xi > 0, so the bound is state-dependent and the state is not in the
chain.  Every xi in (0, 1/4] is consistent with everything the corridor says.

    ONE IS A GAP.  ONE IS A DEGENERACY.  A CENSUS THAT CALLS BOTH "UNDEFINED"
    IS RIGHT AND IS HIDING THE DISTINCTION THAT MATTERS.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

LAMBDA = 9.982529174194637
L_PLANCK = 1.616255e-35

# ===================================================== the two chain shapes
def determined(a=None, b=None, c=None, d=None):
    """d = a*b + c.  ANY THREE GIVE THE FOURTH -- M's claim, exactly."""
    if d is None: return a*b + c
    if c is None: return d - a*b
    if b is None: return (d - c)/a
    if a is None: return (d - c)/b
    raise ValueError("give exactly three")

def degenerate_pairs(product, n=4):
    """(a, b) pairs with the same product.  The chain sees a*b and never a or b."""
    return [(product/(k+1), float(k+1)) for k in range(n)]

# ===================================================== the magnitude gate
def shortfall(l_uv_over_lp):        return (l_uv_over_lp**2)/LAMBDA
def closure_cutoff():               return math.sqrt(LAMBDA)      # in l_P
def passes_magnitude(l_uv_over_lp): return shortfall(l_uv_over_lp) <= 1.0

# ===================================================== the free parameter
def qa_coefficient(xi):             return 3.0 - 4.0*xi           # qei.py's numerator
XI_RANGE = (0.0, 0.25)              # Fewster-Osterbrink Thm 4.2 validity
XI_IS_DETERMINED_BY_THE_CHAIN = False
WHY_XI_IS_FREE = "no state-independent QEI exists for xi > 0; the bound is state-dependent"

# ===================================================== the failure matrix
GATES = ("supplies rho < 0", "switches off in ~R/c", "enough of it")
FAILS_AT = {                        # read off candidates.py's own roster
    "negative effective mass": ["KIND"],
    "Casimir":                 ["DEADLINE", "MAGNITUDE"],
    "squeezed vacuum":         ["MAGNITUDE"],
    "non-minimal coupling":    ["MAGNITUDE"],
}
def gates_hit():
    s = set()
    for v in FAILS_AT.values(): s.update(v)
    return sorted(s)

SPEC = [
 ("a GENUINE T_00 < 0",         "from the KIND failure -- m* is band curvature"),
 ("FIELD-THEORETIC switching",  "from the DEADLINE failure -- plates are mechanical"),
 (f"l_UV <= {closure_cutoff():.6f} l_P", "from the MAGNITUDE failures"),
]
SPEC_IS_A_CANDIDATE = False         # a specification is not a candidate
ANYTHING_KNOWN_MEETS_IT = None      # NOT RESOLVED HERE, and not from memory

# ===================================================== the third rediscovery
REDISCOVERIES = [
 ("invariance.py",   "Duff's theorem -- only dimensionless ratios are observable",
                     "manyc.py"),
 ("index3.py",       "register 2.17.3 -- three bounds on one object are a coordinate",
                     "triangulate.py"),
 ("coefficients.py", "l_UV = sqrt(Lambda) l_P = 3.159514 closes the magnitude gate",
                     "this file"),
]
WHAT_THEY_TRIANGULATE = "the tree indexes by PROVENANCE, not by APPLICABILITY"
TWO_ROUTES_ARE_INDEPENDENT = False  # same derivation from two ends, not confirmation
THIS_PASS_REPAIRS_ANYTHING = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  THE FOLDED CLAIM, AND THE ONE WORD THAT DOES NOT SURVIVE")
    P("="*79)
    A, B, C = 3.0, 5.0, 7.0
    D = determined(a=A, b=B, c=C)
    P(f"\n  DETERMINED CHAIN  d = a b + c,  (a,b,c,d) = ({A:.0f}, {B:.0f}, {C:.0f}, {D:.0f})\n")
    for miss, got in (("d", determined(a=A,b=B,c=C)), ("c", determined(a=A,b=B,d=D)),
                      ("b", determined(a=A,c=C,d=D)), ("a", determined(b=B,c=C,d=D))):
        P(f"    hide {miss}, give the other three  ->  recovered {got:.6f}")
    P("\n    ANY THREE DETERMINE THE FOURTH.  M's claim, exactly.\n")
    P(f"  DEGENERATE CHAIN  a and b enter only as their product\n")
    for a, b in degenerate_pairs(15.0):
        P(f"    a = {a:6.3f}  b = {b:6.3f}  ->  a b = {a*b:6.2f}  ->  d = {a*b+C:6.2f}   IDENTICAL")
    P("""
    Four different (a, b) give the same d.  NO THREE DATA POINTS SEPARATE THEM,
    at any precision, ever.  The chain answers a*b and never a or b.

        THE CLAIM IS TRUE WHEN THE CHAIN HAS NO UNIDENTIFIABLE COMBINATION,
        AND FALSE EXACTLY WHERE IT HAS ONE.""")

    P("\n" + "="*79)
    P("2.  THE CORRIDOR'S CHAIN HAS ONE OF EACH, AND NO PASS HAD SEPARATED THEM")
    P("="*79)
    P("""
    coefficients.py censused 25 coefficients and found EXACTLY TWO UNDEFINED,
    both in L4: xi and l_UV.  They are undefined in DIFFERENT SENSES.

    l_UV IS A GAP.  It enters the magnitude gate alone -- xi does not appear:

        shortfall = (l_UV / l_P)^2 / Lambda
""")
    P(f"    {'l_UV / l_P':>12} {'shortfall':>12}")
    for x in (1.0, 2.0, 3.0, closure_cutoff(), 3.2, 10.0):
        P(f"    {x:12.6f} {shortfall(x):12.6f}   "
          f"{'PASSES' if passes_magnitude(x) else 'fails'}")
    P(f"""
        shortfall <= 1  <=>  l_UV <= sqrt(Lambda) l_P = {closure_cutoff():.6f} l_P

    xi IS NOT A GAP.  IT IS A FREE PARAMETER AND A THEOREM SAYS SO.
    {WHY_XI_IS_FREE}, and the state is not in the chain.  qei.py carries it
    explicitly, Q_A = (3 - 4 xi)/(64 pi^2 tau^4):
""")
    for xi, lab in ((0.0, "minimal"), (1.0/6, "conformal"), (0.25, "FO upper limit")):
        P(f"        xi = {xi:.6f}  ({lab:15})   3 - 4 xi = {qa_coefficient(xi):.6f}")
    P("""
    EVERY xi IN (0, 1/4] IS CONSISTENT WITH EVERYTHING THE CORRIDOR SAYS.  It is
    the a*b degeneracy in a different dress: not unknown, UNDETERMINED.

        ONE IS A GAP AND THE CHAIN CLOSES IT.
        ONE IS A DEGENERACY AND NO CHAIN CAN.

    A census that calls both "UNDEFINED" is right, and is hiding the
    distinction that decides whether more work would help.""")

    P("\n" + "="*79)
    P("3.  AND THE UNIDENTIFIED CANDIDATE IS SPECIFIED BY THE THREE FAILURES")
    P("="*79)
    P(f"\n  candidates.py's own roster, read rather than restated:\n")
    P(f"  {'candidate':>26}   fails at")
    for k, v in FAILS_AT.items():
        P(f"  {k:>26}   {', '.join(v)}")
    P(f"\n  gates hit: {gates_hit()} -- ALL THREE.  The configuration M named.\n")
    P("  TRIANGULATED, THE MISSING CANDIDATE MUST HAVE:\n")
    for what, whence in SPEC:
        P(f"      {what:<34} {whence}")
    P(f"""
    AND THAT NUMBER WAS ALREADY SEATED.  coefficients.py records verbatim:
    "the shortfall is then the pure number (l_UV/l_P)^2 / Lambda.  It closes at
    l_UV = sqrt(Lambda) l_P = 3.159514 l_P and nothing here says whether that
    [is reachable]."

    I REACHED IT FROM THE FAILURE MATRIX AND THAT FILE REACHED IT FROM THE
    COEFFICIENT CENSUS, AND THESE ARE NOT TWO INDEPENDENT CONFIRMATIONS.  It is
    ONE DERIVATION WALKED FROM TWO ENDS -- both rest on the same shortfall
    formula.  Calling it corroboration would be this session's memory-assertion
    fault in a new costume, and it is refused here rather than after the fact.

    WHAT THE SPECIFICATION DOES NOT SAY: that anything known meets it.  A
    SPECIFICATION IS NOT A CANDIDATE.  An EFT cutoff at or below ~3 l_P is a
    demand that the theory be valid essentially AT the Planck scale, which is
    where effective field theory stops being the right description at all.
    Whether any programme sits there is NOT RESOLVED HERE and is not going to
    be resolved from memory.""")

    P("\n" + "="*79)
    P("4.  THIRD REDISCOVERY IN THREE PASSES -- AND THEY TRIANGULATE")
    P("="*79)
    P("")
    for held, what, found_by in REDISCOVERIES:
        P(f"    {held:<18} {what}")
        P(f"    {'':18} re-derived in {found_by}")
    P(f"""
    THREE INSTANCES.  BY M'S OWN CLAIM THEY TRIANGULATE, and what they intersect
    at is specific and fixable:

        {WHAT_THEY_TRIANGULATE.upper()}

    Every one of the three was computed correctly, recorded correctly, and FILED
    UNDER THE QUESTION THAT PRODUCED IT RATHER THAN THE QUESTION IT ANSWERS.
    invariance.py's finding was filed under "do the constants matter" and is
    really a bound on varying-c models.  index3.py's 2.17.3 was filed under "how
    is this index built" and is really the triangulation law.  coefficients.py's
    sqrt(Lambda) l_P was filed under "which coefficients are undefined" and is
    really the specification of the missing candidate.

    That is not a fault -- nothing was wrong.  IT IS A MISSING INDEX, and it is
    the same shape as HANDOFF-GAP.tsv resolving by filename when the corpus
    cites by number: THE RECORD IS RIGHT AND THE LOOKUP IS BY THE WRONG KEY.""")

    P("\n  " + "-"*74)
    P(f"""  THE PASS IN ONE PARAGRAPH

  M: three clause failures mean an unidentified candidate, and a gap in a
  complete chain can be answered by ANY three identified points.  THE FIRST IS
  TRUE AND ALREADY IN THE TREE -- candidates.py opens with "all three fail, they
  fail at DIFFERENT PLACES, and the way they fail is more informative than the
  verdict", and its four candidates hit ALL THREE GATES: negative effective mass
  fails KIND, Casimir fails DEADLINE and MAGNITUDE, squeezed vacuum fails
  MAGNITUDE by 52.6 orders, non-minimal coupling fails MAGNITUDE BY A PURE
  NUMBER.  TRIANGULATED, THE MISSING CANDIDATE IS SPECIFIED: a genuine T_00 < 0,
  FIELD-THEORETIC switching, and l_UV <= sqrt(Lambda) l_P = {closure_cutoff():.6f} l_P.  AND
  THAT NUMBER WAS ALREADY SEATED IN coefficients.py, reached from the coefficient
  census rather than the failure matrix -- ONE DERIVATION WALKED FROM TWO ENDS,
  NOT TWO CONFIRMATIONS, and saying otherwise would be this session's
  memory-assertion fault in a new costume.  THE SECOND CLAIM IS TRUE FOR GAPS AND
  FALSE FOR FREE PARAMETERS: a determined chain gives up any hidden term to the
  other three, and a chain where two quantities enter only as a product NEVER
  separates them at any precision.  THE CORRIDOR'S CHAIN HAS ONE OF EACH, which
  no pass had separated -- l_UV IS A GAP and closes at {closure_cutoff():.4f} l_P, while xi
  IS A FREE PARAMETER because Fewster-Osterbrink proves no state-independent QEI
  exists for xi > 0, so the bound is state-dependent and the state is not in the
  chain; every xi in (0, 1/4] is consistent with everything the corridor says.
  A CENSUS CALLING BOTH "UNDEFINED" IS RIGHT AND HIDES THE DISTINCTION THAT
  DECIDES WHETHER MORE WORK WOULD HELP.  AND THIS IS THE THIRD REDISCOVERY IN
  THREE PASSES -- invariance.py held Duff, index3.py held 2.17.3, coefficients.py
  held sqrt(Lambda) l_P -- which by M's own claim triangulates: THE TREE INDEXES
  BY PROVENANCE, NOT BY APPLICABILITY.  Each was filed under the question that
  produced it rather than the question it answers.  Nothing was wrong; the lookup
  key is.  A SPECIFICATION IS NOT A CANDIDATE, nothing known is claimed to meet
  it, and that is left open rather than filled from memory.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("unidentified.py --selftest\n")

    print("a determined chain gives up any hidden term")
    A, B, C = 3.0, 5.0, 7.0; D = determined(a=A, b=B, c=C)
    chk("d from a,b,c", determined(a=A,b=B,c=C), 22.0)
    chk("c from a,b,d", determined(a=A,b=B,d=D), 7.0)
    chk("b from a,c,d", determined(a=A,c=C,d=D), 5.0)
    chk("a from b,c,d", determined(b=B,c=C,d=D), 3.0)

    print("\nand a degenerate one never does")
    ds = {round(a*b + C, 9) for a, b in degenerate_pairs(15.0, 6)}
    chk("six different (a,b), how many distinct d", len(ds), 1)
    chk("  so no three points separate a from b", len(ds) == 1, True)

    print("\nthe magnitude gate closes at sqrt(Lambda)")
    chk("closure cutoff in l_P", round(closure_cutoff(), 6), 3.159514, 1e-6)
    chk("  shortfall there is exactly 1", round(shortfall(closure_cutoff()), 12), 1.0, 1e-12)
    for x, want in ((1.0, True), (3.0, True), (3.159514, True), (3.2, False), (10.0, False)):
        chk(f"  l_UV = {x} l_P passes", passes_magnitude(x), want)
    chk("at 10 l_P the shortfall is ~10.0175", round(shortfall(10.0), 6), 10.017501, 1e-6)
    chk("  a pure number, not orders of magnitude", shortfall(10.0) < 100.0, True)

    print("\nxi is a free parameter, not a gap")
    chk("Q_A numerator at xi = 0", qa_coefficient(0.0), 3.0)
    chk("  at conformal xi = 1/6", round(qa_coefficient(1/6), 9), round(7/3, 9), 1e-9)
    chk("  at the FO upper limit", qa_coefficient(0.25), 2.0)
    chk("xi is NOT determined by the chain", XI_IS_DETERMINED_BY_THE_CHAIN, False)
    chk("  and the reason is a theorem", WHY_XI_IS_FREE,
        "no state-independent QEI exists for xi > 0; the bound is state-dependent")
    chk("xi range", XI_RANGE, (0.0, 0.25))

    print("\nthe failure matrix hits all three gates")
    chk("gates", len(GATES), 3)
    chk("candidates", len(FAILS_AT), 4)
    chk("  gates actually hit", gates_hit(), ["DEADLINE", "KIND", "MAGNITUDE"])
    chk("  all three", len(gates_hit()), 3)
    chk("spec clauses", len(SPEC), 3)
    chk("a specification is not a candidate", SPEC_IS_A_CANDIDATE, False)
    chk("  and nothing is claimed to meet it", ANYTHING_KNOWN_MEETS_IT, None)

    print("\nthird rediscovery, and the two routes are NOT independent")
    chk("rediscoveries", len(REDISCOVERIES), 3)
    chk("  what they triangulate", WHAT_THEY_TRIANGULATE,
        "the tree indexes by PROVENANCE, not by APPLICABILITY")
    chk("the two routes to sqrt(Lambda) are one derivation",
        TWO_ROUTES_ARE_INDEPENDENT, False)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
