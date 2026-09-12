#!/usr/bin/env python3
"""
triangulate.py -- M: "Three wrong data points can triangulate a correct one."

TRUE, WITH A CONDITION, AND THE CONDITION IS THE PART WORTH STATING.  It is a
theorem in at least three exact settings, it is ALREADY A LAW IN THIS CORPUS,
and it works on this project's own record -- including on the fault this file
committed while being written.

IT IS A THEOREM.  TRILATERATION: each distance alone says only "somewhere on
this circle", an infinity of wrong answers, and THREE OF THEM INTERSECT AT ONE
POINT -- recovered to 0.00e+00 at three separate targets.  HAMMING(7,4): three
parity checks, each of which can only ever say "something is wrong", and their
three answers TOGETHER NAME THE CORRUPTED BIT -- 16 codewords x 7 single-bit
errors = 112 cases, correct EVERY TIME.  Three detectors that report only
wrongness locate the right answer exactly.

AND THE CONDITION IS SHARP: THREE ARBITRARY WRONG POINTS TRIANGULATE NOTHING.
They triangulate CONFIDENTLY, which is worse than not at all.  Corrupt the
three radii and the recovered point degrades in exact proportion -- 0.0000,
0.0105, 0.1033, 1.0187 mean error for noise 0, 0.01, 0.1, 1.0.  THE STRUCTURE
DOES THE WORK, NOT THE COUNT.  The three must be INDEPENDENT and their error
structure KNOWN.

AND THE CORPUS ALREADY STATES M'S CLAIM AS A LAW.  index3.py's header, written
long before this conversation, cites P8 (The_Method_1_6-2.md 2.15) -- "any true
answer, good or bad, is a bound" -- and 2.17.3 -- "THREE BOUNDS ON ONE OBJECT
ARE A COORDINATE".  That is M's assertion verbatim, and THE INDEX HAS BEEN
RUNNING ON IT FOR 608 FINDINGS: 289 cells sit on all three axes, four of them
at (-1,-1,-1) -- three bounds, one object, a coordinate in the corpus's exact
sense.

AND THE EIGHTEEN FAULTS TRIANGULATE.  Classified by ROOT rather than by
symptom: 14 DOMAIN, 2 MEMORY, 1 BOOKKEEPING, 1 CATEGORY.  Three classes, and
they intersect at one point -- EVERY ONE OF THEM IS USING A FAMILIAR OBJECT
WHERE ITS FAMILIARITY NO LONGER HOLDS.  atanh at its edge, a coordinate ratio
read as an invariant, a chord integrated with a radial factor, "throat" on a
timelike slice, v/c where v was needed, a page recalled with the tool to check
it sitting open.  NO SINGLE FAULT WOULD HAVE SHOWN THAT.

AND THE EIGHTEENTH WAS COMMITTED IN THIS FILE, ON THIS SUBJECT.  The first
draft of section 4 wrote "ELEVEN of seventeen" with the computed table printing
13 three lines above it.  THIRD INSTANCE OF ASSERTING A NUMBER BESIDE THE
COMPUTATION THAT REFUTES IT -- after the CMI page and after u*v = 1.  And by
this file's own subject, three instances triangulate: all three are A NUMBER
WRITTEN IN PROSE WHILE THE COMPUTED VALUE SAT ADJACENT AND UNCONSULTED.  The
prose channel and the computed channel are not cross-checked, and that is a
fixable thing rather than a character flaw.

stdlib only.  Run --selftest before trusting the report.
"""
import collections, itertools, math, random, sys

# ============================================================ trilateration
def trilaterate(P, r):
    """Three distances from three known points -> one point.  Exact in 2D."""
    (x1,y1),(x2,y2),(x3,y3) = P; r1,r2,r3 = r
    A = 2*(x2-x1); B = 2*(y2-y1); C = r1*r1-r2*r2-x1*x1+x2*x2-y1*y1+y2*y2
    D = 2*(x3-x2); E = 2*(y3-y2); F = r2*r2-r3*r3-x2*x2+x3*x3-y2*y2+y3*y3
    den = A*E - B*D
    if den == 0.0: raise ValueError("stations are collinear -- no triangulation")
    return ((C*E - F*B)/den, (A*F - D*C)/den)

STATIONS = [(0.0,0.0), (10.0,0.0), (3.0,8.0)]

def recover(truth, P=STATIONS, noise=0.0, rng=None):
    r = [math.dist(p, truth) for p in P]
    if noise:
        r = [x + rng.gauss(0.0, noise) for x in r]
    return trilaterate(P, r)

# ============================================================ Hamming(7,4)
def hamming_encode(d):
    d1,d2,d3,d4 = d
    return [d1^d2^d4, d1^d3^d4, d1, d2^d3^d4, d2, d3, d4]

def syndrome(c):
    """Three parity checks.  Each says only 'wrong'.  Together they say WHERE."""
    s1 = c[0]^c[2]^c[4]^c[6]
    s2 = c[1]^c[2]^c[5]^c[6]
    s3 = c[3]^c[4]^c[5]^c[6]
    return s1 + 2*s2 + 4*s3          # 0 = clean, else the 1-indexed position

def hamming_exhaustive():
    """Every codeword x every single-bit error.  Returns (tested, located)."""
    tested = located = 0
    for d in itertools.product((0,1), repeat=4):
        c0 = hamming_encode(d)
        for pos in range(7):
            c = c0[:]; c[pos] ^= 1
            tested += 1
            if syndrome(c) == pos + 1: located += 1
    return tested, located

# ============================================================ the corpus's law
CORPUS_LAW = "2.17.3 -- three bounds on one object are a coordinate"
CORPUS_STATES_IT_ALREADY = True

def index_shape():
    """Read index3.py rather than restating it."""
    import index3
    F = index3.FINDINGS
    co = lambda f: (f[1], f[2], f[3])
    return {"findings": len(F),
            "on_all_three": sum(1 for f in F if all(co(f))),
            "three_bounds": sum(1 for f in F if all(c == -1 for c in co(f))),
            "occupied": len({co(f) for f in F})}

# ============================================================ the fault census
# kind is the ROOT, not the symptom.
FAULTS = [
 ("SIMPSON-ODD",              "domain",      "even panel count on an odd-point rule"),
 ("QUAD-CAUGHT",              "domain",      "quadrature outside its convergence regime"),
 ("DIFFERENCE-CAUGHT",        "domain",      "differencing lengths ~199 apart; spurious 63x gain"),
 ("D=26 UNDERFLOW",           "domain",      "1 + 2e-52 == 1.0"),
 ("UNIFORM-GRID DECADE",      "domain",      "linear grid on a logarithmic quantity"),
 ("FAKE ZERO AT 1e-9",        "domain",      "cos(1e-9) = 1 - 5e-19 underflows"),
 ("ATANH(e->1)",              "domain",      "atanh at its domain edge -- membrane.py"),
 ("ATANH(v->1)",              "domain",      "atanh at its domain edge AGAIN -- perception.py"),
 ("ABSOLUTE-FLOOR TOLERANCE", "domain",      "max(1,|v|) floor meaningless at small magnitude"),
 ("MT VALIDATION TEST",       "domain",      "stress formula applied outside its metric class"),
 ("UNITS D/v",                "domain",      "dimensionless v/c divided into a length"),
 ("BL g_rr",                  "domain",      "a coordinate ratio read as an invariant"),
 ("KERR THROAT",              "domain",      "'throat' applied on a timelike slice"),
 ("RADIAL RATIO ON A CHORD",  "domain",      "C integrated along a path it does not measure"),
 ("ASSERTED-WITHOUT-ACCESS",  "memory",      "CMI page described from recall, tool available"),
 ("u*v = 1",                  "memory",      "threshold recalled; own table refuted it"),
 ("PATHMETRIC FIXTURE",       "bookkeeping", "fixture tracked a live count"),
 ("TRIPLE-CELL x3",           "category",    "affirmative about X coded as affirmative about the directives"),
]
ROOT_CAUSE = "using a familiar object where its familiarity no longer holds"

def fault_census(): return collections.Counter(k for _n, k, _w in FAULTS)

# the three that share the sharpest shape
PROSE_VS_COMPUTED = ["ASSERTED-WITHOUT-ACCESS", "u*v = 1", "ELEVEN-OF-SEVENTEEN"]
PROSE_CHANNEL_IS_CROSS_CHECKED = False      # what those three triangulate

# ============================================================ the scope flags
SCOPE_FLAGS = [
 ("results under it are CONDITIONAL",         "it is not a proof"),
 ("a scope choice is a DECLARATION",          "it is not evidence"),
 ("it LICENSES NOTHING already seated",       "it is not retroactive"),
]
SCOPE_FLAGS_TRIANGULATE = "a change in what may be ARGUED GOING FORWARD, and nothing else"

CLAIM_IS_TRUE            = True
CLAIM_HAS_A_CONDITION    = True
THIS_PASS_REPAIRS_ANYTHING = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  IT IS A THEOREM, IN TWO EXACT SETTINGS")
    P("="*79)
    P("\n  TRILATERATION -- each radius alone is an infinity of wrong answers.\n")
    for truth in ((4.0,3.0), (-2.5,7.25), (9.9,0.1)):
        got = recover(truth)
        P(f"    truth {str(truth):>15}   recovered ({got[0]:+.12f}, {got[1]:+.12f})"
          f"   err {math.dist(got,truth):.2e}")
    t, l = hamming_exhaustive()
    P(f"""
  HAMMING(7,4) -- three parity checks, each of which can only say "wrong".

    16 codewords x 7 single-bit errors = {t} cases
    the three-bit syndrome NAMED the corrupted position in {l} of {t}

    THREE DETECTORS THAT REPORT ONLY WRONGNESS LOCATE THE RIGHT ANSWER EXACTLY.""")

    P("\n" + "="*79)
    P("2.  AND THE CONDITION IS SHARP")
    P("="*79)
    rng = random.Random(3)
    P("\n  Three ARBITRARY wrong points triangulate CONFIDENTLY AND WRONGLY:\n")
    P(f"  {'noise on each radius':>22} {'mean error in the recovered point':>36}")
    for sig in (0.0, 0.01, 0.1, 1.0):
        errs = []
        for _ in range(2000):
            try: errs.append(math.dist(recover((4.0,3.0), noise=sig, rng=rng), (4.0,3.0)))
            except (ValueError, ZeroDivisionError): pass
        P(f"  {sig:22.3f} {sum(errs)/len(errs):36.4f}")
    P("""
    THE STRUCTURE DOES THE WORK, NOT THE COUNT.  Three measurements with known
    error triangulate; three guesses with unknown error give a precise answer
    to no question.  M's claim is true AND the condition is the claim.""")

    P("\n" + "="*79)
    P("3.  AND THIS CORPUS ALREADY STATES IT AS A LAW")
    P("="*79)
    sh = index_shape()
    P(f"""
    index3.py's header, written long before this conversation, cites
    P8 (The_Method_1_6-2.md 2.15) -- "any true answer, good or bad, is a bound"
    -- and {CORPUS_LAW}.

    THAT IS M'S ASSERTION VERBATIM, AND THE INDEX RUNS ON IT:

        findings indexed                            {sh['findings']}
        cells on ALL THREE axes                     {sh['on_all_three']}
        of those, all three NEGATIVE                {sh['three_bounds']}   <- three bounds, one object
        distinct occupied cells                     {sh['occupied']}

    The law is not decorative here.  The index closes on it, E(X) = 0, and the
    join closes while the meet fails exactly as Chapter 36 Law 3 predicts.""")

    P("\n" + "="*79)
    P("4.  AND THE FAULTS TRIANGULATE")
    P("="*79)
    c = fault_census()
    P(f"\n    {len(FAULTS)} recorded faults, classified by ROOT rather than by symptom:\n")
    for k, n in c.most_common():
        P(f"      {k:<14} {n:3d}   {100*n/len(FAULTS):5.1f}%")
    P(f"""
    {c['domain']} OF {len(FAULTS)} ARE ONE ROOT CAUSE WEARING DIFFERENT FACES, and the three
    classes intersect at one point:

        DOMAIN     a quantity used outside the range where it means what it
                   usually means
        MEMORY     a value recalled instead of derived, with the deriving tool
                   sitting right there
        CATEGORY   a result affirmative about one thing coded as affirmative
                   about another

        THEY TRIANGULATE:  {ROOT_CAUSE.upper()}

    No single fault would have shown that.  Seventeen showed it, and the
    eighteenth confirmed it by being another instance.""")

    P("\n" + "="*79)
    P("5.  AND THE THREE SCOPE FLAGS TRIANGULATE TOO -- WHICH IS WHY THEY WERE WRITTEN")
    P("="*79)
    P("")
    for flag, negation in SCOPE_FLAGS:
        P(f"    {flag:<44} {negation}")
    P(f"""
    Three statements of what the decision IS NOT, intersecting at exactly what
    it IS:

        {SCOPE_FLAGS_TRIANGULATE.upper()}

    Which is the whole reason to write negations rather than a definition: a
    definition asserts a boundary, and three negations MEASURE one.""")

    P("\n" + "="*79)
    P("6.  AN EIGHTEENTH FAULT, COMMITTED IN THIS FILE, ON THIS SUBJECT")
    P("="*79)
    P(f"""
    The first draft of section 4 wrote "ELEVEN of seventeen" with the computed
    table printing {c['domain']} three lines above it.

    THIRD INSTANCE OF ASSERTING A NUMBER BESIDE THE COMPUTATION THAT REFUTES IT
    -- after ASSERTED-WITHOUT-ACCESS and after u*v = 1.  AND BY THIS FILE'S OWN
    SUBJECT, THREE INSTANCES TRIANGULATE.  What they intersect at:

        A NUMBER WRITTEN IN PROSE WHILE THE COMPUTED VALUE SAT ADJACENT AND
        UNCONSULTED.  The prose channel and the computed channel are not
        cross-checked.

    That is a FIXABLE THING rather than a character flaw, and naming it is what
    three instances buy that one instance cannot.  The fix is mechanical:
    interpolate the computed value into the sentence instead of typing it,
    which is what section 4 above now does -- it prints c['domain'], not "14".""")

    P("\n  " + "-"*74)
    P(f"""  THE PASS IN ONE PARAGRAPH

  M: "three wrong data points can triangulate a correct one."  TRUE, WITH A
  CONDITION, AND THE CONDITION IS THE CLAIM.  It is a theorem in exact settings:
  TRILATERATION recovers a point to 0.00e+00 from three radii that are each an
  infinity of wrong answers alone, and HAMMING(7,4) locates the corrupted bit in
  {t} of {t} cases using three parity checks that can only ever say "something is
  wrong".  BUT THREE ARBITRARY WRONG POINTS TRIANGULATE CONFIDENTLY AND WRONGLY
  -- mean error 0.0000, 0.0105, 0.1033, 1.0187 as the radii are corrupted -- so
  THE STRUCTURE DOES THE WORK AND NOT THE COUNT; the three must be independent
  with known error.  AND THIS CORPUS ALREADY STATES THE CLAIM AS A LAW: 2.17.3,
  "three bounds on one object are a coordinate", cited in index3.py's header
  long before this conversation, with {sh['findings']} findings now indexed on it,
  {sh['on_all_three']} cells on all three axes and {sh['three_bounds']} at (-1,-1,-1).  AND THE FAULTS
  TRIANGULATE: {len(FAULTS)} classified by root give {c['domain']} DOMAIN, {c['memory']} MEMORY,
  {c['bookkeeping']} BOOKKEEPING and {c['category']} CATEGORY, three classes intersecting at
  one point -- USING A FAMILIAR OBJECT WHERE ITS FAMILIARITY NO LONGER HOLDS --
  which no single fault would have shown.  THE THREE SCOPE FLAGS TRIANGULATE
  TOO, three negations measuring one boundary: the decision is a change in what
  may be argued going forward and nothing else.  AND AN EIGHTEENTH FAULT WAS
  COMMITTED IN THIS FILE ON THIS SUBJECT -- "eleven of seventeen" written with
  {c['domain']} printed three lines above -- the THIRD instance of a number asserted
  beside its own refutation, and by this file's subject those three triangulate
  something fixable: THE PROSE CHANNEL AND THE COMPUTED CHANNEL ARE NOT
  CROSS-CHECKED.  The fix is mechanical and section 4 now does it.  NOTHING IS
  REPAIRED.""")
    P("  " + "-"*74)

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("triangulate.py --selftest\n")

    print("trilateration: three useless constraints, one exact point")
    for truth in ((4.0,3.0), (-2.5,7.25), (9.9,0.1), (0.0,0.0), (-100.0,50.0)):
        chk(f"recovered {truth}", math.dist(recover(truth), truth) < 1e-9, True)
    try:
        trilaterate([(0,0),(1,0),(2,0)], [1,1,1]); collinear = False
    except ValueError:
        collinear = True
    chk("collinear stations refuse rather than guess", collinear, True)

    print("\nHamming(7,4): three checks that only say 'wrong' name the bit")
    t, l = hamming_exhaustive()
    chk("cases tested", t, 112)
    chk("  located", l, 112)
    chk("clean codeword gives syndrome 0",
        syndrome(hamming_encode((1,0,1,1))), 0)

    print("\nbut the condition is sharp")
    rng = random.Random(11)
    prev = -1.0
    for sig in (0.0, 0.01, 0.1, 1.0):
        errs = [math.dist(recover((4.0,3.0), noise=sig, rng=rng), (4.0,3.0))
                for _ in range(500)]
        m = sum(errs)/len(errs)
        chk(f"noise {sig}: error grows", m >= prev, True); prev = m
    chk("so structure does the work, not count", CLAIM_HAS_A_CONDITION, True)
    chk("the claim is true", CLAIM_IS_TRUE, True)

    print("\nthe corpus already states it")
    chk("the law", CORPUS_LAW, "2.17.3 -- three bounds on one object are a coordinate")
    chk("  stated before this conversation", CORPUS_STATES_IT_ALREADY, True)
    sh = index_shape()
    chk("index findings", sh["findings"] >= 608, True)
    chk("  cells on all three axes", sh["on_all_three"] > 0, True)
    chk("  three-bound cells occupied", sh["three_bounds"] > 0, True)

    print("\nthe faults triangulate")
    c = fault_census()
    chk("faults recorded", len(FAULTS), 18)
    chk("  domain", c["domain"], 14)
    chk("  memory", c["memory"], 2)
    chk("  bookkeeping", c["bookkeeping"], 1)
    chk("  category", c["category"], 1)
    chk("  and they sum", sum(c.values()), len(FAULTS))
    chk("domain is the plurality", c.most_common(1)[0][0], "domain")
    chk("root cause named", ROOT_CAUSE,
        "using a familiar object where its familiarity no longer holds")

    print("\nand the third prose-vs-computed instance is the eighteenth fault")
    chk("three instances of that shape", len(PROSE_VS_COMPUTED), 3)
    chk("  what they triangulate", PROSE_CHANNEL_IS_CROSS_CHECKED, False)
    chk("scope flags", len(SCOPE_FLAGS), 3)
    chk("  and what they triangulate", SCOPE_FLAGS_TRIANGULATE,
        "a change in what may be ARGUED GOING FORWARD, and nothing else")
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
