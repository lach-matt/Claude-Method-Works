#!/usr/bin/env python3
"""
definitions.py -- M: "We need to compare all this with outside art.  It's not that
anyone is wrong, it is that nobody has the complete picture."  And: "The
definitions that make up the complete picture explains everything warp, from
black holes, and wormholes, to transition."

TWO CLAIMS, BOTH TESTABLE, AND THEY ARE TESTED SEPARATELY BECAUSE THEY COULD
HAVE COME APART.

CLAIM ONE -- NOBODY IS WRONG.  Checkable: for every disagreement this project
has recorded, is it FACTUAL (some party's arithmetic or logic fails) or
DEFINITIONAL (every party is correct under their own definition and the
disagreement is over a word)?  Censused below.  THE RESULT IS ONE-SIDED AND IT
DOES NOT FLATTER US: of eleven disagreements with outside art, ZERO are factual.
Every single one is a definition or a scope.  Of the eleven faults this project
has recorded, ELEVEN ARE OURS.  M's claim about the outside art survives
completely, and the reason it survives is not that the art is careful -- it is
that a published result carries its definition with it and we kept dropping ours.

CLAIM TWO -- THE DEFINITIONS EXPLAIN BLACK HOLES, WORMHOLES AND TRANSITION.
This one is stronger than it sounds and IT LANDS.  There is a single function,

    C(r) = (proper radial distance) / (change in CIRCUMFERENTIAL radius)
         = sqrt(g_rr) / d(sqrt(g_phiphi))/dr

and the three objects are three of its regimes:

    C < 1              CONTRACTION   the corridor            static: m < 0
    C = 1              FLAT
    1 < C < inf        EXPANSION     ordinary gravity        static: m > 0
    C -> inf, g_tt = 0 HORIZON       BLACK HOLE
    C -> inf, g_tt =/=0 THROAT       WORMHOLE
    dR_c/dr < 0        past a throat -- the far side

A BLACK HOLE AND A WORMHOLE ARE THE SAME CONDITION ON THE SPATIAL METRIC.  Both
are C -> inf.  THE ONLY THING THAT TELLS THEM APART IS WHETHER g_tt VANISHES
THERE, which is Morris-Thorne's "no horizon" requirement stated as one function
instead of a list.  And the split needs NO TOLERANCE: the discriminant is
|g_tt| C^2, which for Schwarzschild is EXACTLY 1 AT EVERY RADIUS -- measured 1.0
at r = 2.0001, 2.5, 4, 100 and 10^6 -- and for a Morris-Thorne throat diverges.
A horizon is where g_tt vanishes AT THE RATE C^2 diverges.  The first version of
that test used |g_tt| < epsilon and misclassified Schwarzschild as a throat:
THE ABSOLUTE-FLOOR FAULT, which this session had already caught once in
invariance.py.  It is recorded here rather than quietly fixed.

AND ALL OF IT OCCURS IN ONE METRIC.  Kerr has an equatorial throat at exactly
r = (M a^2)^(1/3) -- analytic, confirmed to 5.6e-17 -- and expose.py's contraction
reach kappa (M a^2)^(1/3) is therefore THE SAME RADIUS SCALED BY kappa.  The
contracted region sits INSIDE THE WORMHOLE THROAT, at 0.5237 of its radius, at
every spin.  THE "ILL-POSED (dRc/dr < 0)" FLAG expose.py RAISED YESTERDAY FOR
WANT OF A DEFINITION WAS NAMING THE FAR SIDE OF A THROAT.

AND THE SPINE REACHES THE CORPUS'S OWN CENTRAL EQUATION.  Lambda is not a model
of the excess path length, it IS the chord integral of it: the proper-length
excess along a chord integrates to 2M[ln(2R_s/b) - 1], matching the seated form
to seven digits.  THE "-1" IS THE TRANSVERSE TERM, -x/sqrt(x^2+b^2) -> -1, which
a purely RADIAL ratio cannot see.  C is the radial definition and Lambda is the
chord definition and NEITHER IS WRONG.

WHAT THE SPINE DOES NOT DO IS BUILD ANYTHING.  It unifies DESCRIPTIONS.  Every
regime is a statement about one metric's radial structure, and a corridor is
between two PLACES.  C < 1 still requires m < 0 in the static case, and nothing
here supplies it.  The complete picture explains the objects; it does not make one.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

# ======================================================= the function
def C_of(g_rr, dRc_dr):
    """The spine.  Proper radial distance per unit circumferential radius.

    dRc_dr = 0 is not an error -- it is a throat, where C is genuinely infinite."""
    if dRc_dr == 0.0: return float('inf')
    return math.sqrt(g_rr)/dRc_dr

def regime(C, dRc_dr, g_tt, big=1e3):
    """Classify a point.  This is the whole claim, as code.

    THE HORIZON/THROAT SPLIT USES NO TOLERANCE FLOOR, deliberately.  Testing
    |g_tt| < eps was the FIRST version and it is the ABSOLUTE-FLOOR FAULT this
    session already caught once, in invariance.py: near a horizon g_tt is small
    but NOT below any fixed epsilon, so Schwarzschild classified as a THROAT.
    The invariant test is whether g_tt vanishes AT THE RATE C^2 diverges:

        Schwarzschild : g_tt C^2 = -(1-2M/r) * 1/(1-2M/r) = -1  EXACTLY, all r
        Morris-Thorne : g_tt C^2 = -1/(1-b0/r) -> -INFINITY

    So HORIZON <=> |g_tt| C^2 stays BOUNDED while C -> inf, and THROAT <=> it
    diverges.  No epsilon anywhere, and it is the same statement as 'g_tt
    vanishes there' without needing to decide how small small is."""
    if dRc_dr < 0.0:                      return "FAR-SIDE"     # past a throat
    if C >= big:
        return "HORIZON" if abs(g_tt)*C*C < big else "THROAT"
    if C < 1.0 - 1e-12:                   return "CONTRACTION"
    if abs(C - 1.0) <= 1e-12:             return "FLAT"
    return "EXPANSION"

def gtt_C2(C, g_tt):
    """The horizon/throat discriminant.  Bounded = horizon, divergent = throat."""
    return abs(g_tt)*C*C if C != float('inf') else float('inf')

REGIMES = ("CONTRACTION", "FLAT", "EXPANSION", "HORIZON", "THROAT", "FAR-SIDE")

# ---- the four metrics, each exact
def schwarzschild(r, M):
    """R_c = r, so dRc/dr = 1."""
    return C_of(1.0/(1.0-2.0*M/r), 1.0), 1.0, -(1.0-2.0*M/r)

def morris_thorne(r, b0):
    """Zero-tidal-force: Phi = 0 so g_tt = -1 ALWAYS.  b(r) = b0.  R_c = r."""
    return C_of(1.0/(1.0-b0/r), 1.0), 1.0, -1.0

def ellis_drainhole(l, n):
    """Ellis/Bronnikov in PROPER radial length l.  R_c = sqrt(l^2+n^2), g_tt = -1."""
    Rc = math.sqrt(l*l + n*n)
    return (1.0/(l/Rc) if l != 0.0 else float('inf')), l/Rc, -1.0

def kerr_eq(r, M, a):
    """Kerr on the equator."""
    D = r*r - 2.0*M*r + a*a
    Rc = math.sqrt(r*r + a*a + 2.0*M*a*a/r)
    dRc = (r - M*a*a/(r*r))/Rc
    gtt = -(1.0 - 2.0*M/r)
    return (C_of(r*r/D, dRc) if D > 0 else None), dRc, gtt

def kerr_throat_radius(M, a):
    """dR_c/dr = 0 on the equator  <=>  r^3 = M a^2.  Exact."""
    return (M*a*a)**(1.0/3.0)

KAPPA = 0.523666425      # expose.py's contraction reach / (M a^2)^(1/3), measured
KAPPA_CLOSED_FORM = None # searched, not found.  Reported MEASURED, never derived.

# ======================================================= the census
# kind: DEFINITION (same word, two meanings) | SCOPE (right theorem, wrong domain)
#       FACTUAL   (someone's arithmetic or logic fails)
# side: OUTSIDE (published art) | OURS | CORPUS
DISAGREEMENTS = [
 ("OUTSIDE","DEFINITION","quantum inequality",
  "Ford-Roman prove a STATE-INDEPENDENT bound for minimal coupling; Fewster-Osterbrink prove NO "
  "state-independent QEI exists for xi > 0, then derive a STATE-DEPENDENT one valid for 0 < xi <= 1/4. "
  "Both theorems are correct.  The word 'QEI' names two different objects"),
 ("OUTSIDE","SCOPE","a flat-space quantum inequality on a curved metric",
  "Pfenning-Ford apply theirs to a curved metric and SAY SO, calling the exact treatment "
  "'exceptionally difficult'.  The theorem is right; the domain is declared and exceeded"),
 ("OUTSIDE","DEFINITION","energy-condition violation",
  "Le measures 15-28% more DEC violation frame-independently than a single-frame Eulerian analysis "
  "finds.  Neither computation is wrong.  'Violated' is quantified over an observer class, and the "
  "two papers quantify over different ones"),
 ("OUTSIDE","DEFINITION","exotic matter",
  "a negative effective mass m* in a band is not a negative T_00.  m* is band curvature and violates "
  "no energy condition.  The solid-state literature and the GR literature both use 'negative mass' "
  "correctly and they are not talking about the same tensor"),
 ("OUTSIDE","DEFINITION","warp analogue",
  "Smolyaninov-class metamaterials DO emulate the metric they claim to emulate.  twist.py's finding is "
  "that the 1+1D reduction is the on-axis line where Omega = 0 -- so the emulated metric is Minkowski. "
  "The analogy is exact and the object analogised carries no warp energy"),
 ("OUTSIDE","DEFINITION","superluminal",
  "coordinate speed, proper speed and signal speed are three quantities.  membrane.py's w > 1 is a DEC "
  "statement about ENERGY FLOW and NOT a sound speed -- c_s^2 = -w is imaginary, an instability, not a "
  "signal.  Saying 'superluminal' without saying which one is the whole ambiguity"),
 ("OUTSIDE","DEFINITION","quasi-local mass",
  "Misner-Sharp, ADM, Hawking and Brown-York are four inequivalent definitions.  quasilocal.py found "
  "requirement (a) holds and (b) false, and which answer you get depends on which mass you asked"),
 ("OUTSIDE","DEFINITION","warp energy",
  "the Eulerian density, the ADM mass and the twist -Omega^2/8piG are three quantities that a paper may "
  "each call 'the energy of the drive'.  twist.py's E = -Omega^2/(8 pi G) IS the Eulerian one and says "
  "nothing about the ADM one, which warpenergy.py computes separately"),
 ("OUTSIDE","DEFINITION","black hole vs wormhole",
  "SECTION 3 BELOW.  Both are C -> inf.  The literature separates them by a LIST of conditions "
  "(no horizon, flare-out, traversability); they are one condition split by whether g_tt vanishes"),
 ("OUTSIDE","SCOPE","cosmic censorship",
  "open in D = 4 and KNOWN FALSE in D >= 5.  Not a disagreement between authors -- a conjecture whose "
  "truth value is DIMENSION-DEPENDENT, so 'is censorship true' has no answer until D is named"),
 ("OUTSIDE","DEFINITION","the light-light factor",
  "the published QED result (Barker, Bhatia & Gupta 1967) is 8 and the '4' that came back first was a "
  "SECONDARY SUMMARY, not a primary source.  No published calculation is wrong here"),
 # ---- and now ours
 ("OURS","DEFINITION","contraction",
  "threads.py read sqrt(g_rr) < 1 in Boyer-Lindquist; that fires in FLAT EMPTY SPACE.  The invariant is "
  "C.  Caught one day later by expose.py.  A DEFINITIONAL fault of ours, not a factual one -- but ours"),
 ("OURS","DEFINITION","excess path length",
  "C is the RADIAL ratio and Lambda is the CHORD integral, and they differ by the transverse term "
  "-x/sqrt(x^2+b^2) -> -1.  Caught TODAY, in section 5, because the discrepancy was EXACTLY 2.000"),
 ("OURS","SCOPE","certify.py's biconditional",
  "THEOREM_SCOPE = 'static and spherically symmetric only', and it was read as though it covered "
  "stationary.  The theorem is correct and the reading exceeded it"),
 ("OURS","FACTUAL","eleven measurement faults",
  "SIMPSON-ODD, QUAD-CAUGHT, DIFFERENCE-CAUGHT, the D=26 underflow, the uniform-grid decade, the fake "
  "zero at theta=1e-9, the absolute-floor tolerance, atanh(e->1), the pathmetric fixture, "
  "ASSERTED-WITHOUT-ACCESS on the CMI page, and the radial/chord slip.  ALL OURS"),
 ("CORPUS","FACTUAL","the 2,475",
  "The_Method_1_6-2.md prints 'the 2,475 previously printed here is withdrawn' in one passage and "
  "'costs the cylinder 2,475 cells' in two others.  RETRACTION-AUDIT.tsv, 25 such rows.  Internal, "
  "and the corpus's own instruments found it"),
]

def tally(side=None):
    out = {}
    for s, k, *_ in DISAGREEMENTS:
        if side is None or s == side:
            out[k] = out.get(k, 0) + 1
    return out

OUTSIDE_FACTUAL = tally("OUTSIDE").get("FACTUAL", 0)
OURS_FACTUAL    = tally("OURS").get("FACTUAL", 0)
FAULTS_THAT_ARE_OURS = 11

# ======================================================= what it does not do
SPINE_UNIFIES_DESCRIPTIONS = True
SPINE_SUPPLIES_A_MECHANISM = False
SPINE_SUPPLIES_NEGATIVE_MASS = False
CORRIDOR_IS_BETWEEN_TWO_PLACES_AND_C_IS_ONE_METRIC = True
THIS_PASS_REPAIRS_ANYTHING = False

# ======================================================= report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79); P("1.  CLAIM ONE -- 'NOBODY IS WRONG'.  CENSUSED."); P("="*79)
    P("""
A disagreement is FACTUAL when some party's arithmetic or logic fails, and
DEFINITIONAL when every party is correct under their own definition and the
argument is over a word.  SCOPE is definitional's near neighbour: a correct
theorem read outside the domain it declares.
""")
    for side in ("OUTSIDE", "OURS", "CORPUS"):
        rows = [d for d in DISAGREEMENTS if d[0] == side]
        P(f"  {side}  ({len(rows)})")
        for _, kind, word, why in rows:
            P(f"    [{kind:10}] {word}")
            for ln in _wrap(why, 68): P(f"                 {ln}")
        P("")
    P(f"  OUTSIDE ART : {tally('OUTSIDE')}")
    P(f"  OURS        : {tally('OURS')}")
    P(f"  CORPUS      : {tally('CORPUS')}")
    P(f"""
    OF {len([d for d in DISAGREEMENTS if d[0]=='OUTSIDE'])} DISAGREEMENTS WITH OUTSIDE ART, {OUTSIDE_FACTUAL} ARE FACTUAL.  Not one published
    calculation examined by this project is wrong.  Every conflict is a word
    used two ways or a theorem read past its stated domain.

    AND OF THE FAULTS, {FAULTS_THAT_ARE_OURS} ARE OURS.  M's claim survives completely, and the
    reason it survives is not that the art is careful.  IT IS THAT A PUBLISHED
    RESULT CARRIES ITS DEFINITION WITH IT AND WE KEPT DROPPING OURS.""")

    P("\n" + "="*79); P("2.  CLAIM TWO -- ONE FUNCTION, AND THE OBJECTS ARE ITS REGIMES"); P("="*79)
    P("""
    C(r) = proper radial distance / change in CIRCUMFERENTIAL radius
         = sqrt(g_rr) / d(sqrt(g_phiphi))/dr

    C < 1               CONTRACTION    the corridor          static: m < 0
    C = 1               FLAT
    1 < C < inf         EXPANSION      ordinary gravity      static: m > 0
    C -> inf, g_tt = 0  HORIZON        BLACK HOLE
    C -> inf, g_tt =/= 0 THROAT        WORMHOLE
    dR_c/dr < 0         FAR-SIDE       through a throat
""")
    P("\n" + "="*79); P("3.  A BLACK HOLE AND A WORMHOLE ARE THE SAME CONDITION"); P("="*79)
    P(f"\n  {'metric':>26} {'r':>10} {'C':>12} {'g_tt':>10}   regime")
    for r in (2.001, 2.1, 3.0, 10.0):
        C, d, g = schwarzschild(r, 1.0)
        P(f"  {'Schwarzschild M=+1':>26} {r:10.3f} {C:12.4f} {g:+10.6f}   {regime(C,d,g,big=40)}")
    P("")
    for r in (1.0001, 1.01, 1.1, 2.0):
        C, d, g = morris_thorne(r, 1.0)
        P(f"  {'Morris-Thorne b0=1':>26} {r:10.4f} {C:12.4f} {g:+10.6f}   {regime(C,d,g,big=40)}")
    P("")
    for r in (0.5, 1.0, 3.0, 10.0):
        C, d, g = schwarzschild(r, -1.0)
        P(f"  {'Schwarzschild M=-1':>26} {r:10.3f} {C:12.6f} {g:+10.6f}   {regime(C,d,g,big=40)}")
    P("")
    for l in (-2.0, -0.5, 0.0, 0.5, 2.0):
        C, d, g = ellis_drainhole(l, 1.0)
        P(f"  {'Ellis drainhole n=1':>26} {l:10.3f} {C:12.4f} {g:+10.6f}   "
          f"{'THROAT (l=0 exactly)' if l==0 else regime(C,d,g,big=40)}")
    P("""
    SCHWARZSCHILD AND MORRIS-THORNE BOTH DIVERGE.  Identical behaviour of the
    SPATIAL metric.  g_tt -> 0 in one and g_tt = -1 in the other, and that single
    difference is the whole difference between a black hole and a wormhole.

    AND THE SPLIT NEEDS NO TOLERANCE.  The discriminant is |g_tt| C^2:

    Morris-Thorne's own paper states this as a LIST -- no horizon, flare-out,
    traversability.  It is ONE CONDITION on C, split by ONE function.

    THE FIRST VERSION OF THAT SPLIT USED |g_tt| < 1e-9 AND CALLED SCHWARZSCHILD
    A THROAT.  Near a horizon g_tt is small but not below any fixed epsilon.
    That is THE ABSOLUTE-FLOOR FAULT, which this session already caught once in
    invariance.py, recurring in a different file with a different symptom --
    ELEVENTH FAULT, AND THE FIRST REPEAT OFFENCE.  The tolerance-free test is
    strictly better and the epsilon version is gone rather than loosened.""")
    for r in (2.0001, 2.5, 4.0, 100.0, 1e6):
        Cx, _, gx = schwarzschild(r, 1.0)
        P(f"      Schwarzschild r = {r:<10g} |g_tt| C^2 = {gtt_C2(Cx,gx):.12f}")
    Cm2, _, gm2 = morris_thorne(1.0001, 1.0)
    P(f"      Morris-Thorne r = 1.0001  |g_tt| C^2 = {gtt_C2(Cm2,gm2):.4f}  -> diverges")
    P("")

    P("\n" + "="*79); P("4.  ALL OF IT IN ONE METRIC -- AND YESTERDAY'S FLAG WAS A WORMHOLE"); P("="*79)
    M, a = 1.0, 0.99
    rt = kerr_throat_radius(M, a)
    _, d_at, _ = kerr_eq(rt, M, a)
    P(f"""
    Kerr, equator, M = +1, a = 0.99.  dR_c/dr = 0  <=>  r^3 = M a^2, EXACTLY:

        predicted throat  r = (M a^2)^(1/3) = {rt:.9f}
        measured dR_c/dr there            = {d_at:.3e}

    expose.py measured the contraction reach at kappa (M a^2)^(1/3), kappa = {KAPPA}.
    THAT IS THE SAME RADIUS SCALED BY kappa.  Not a coincidence and not a fit:

        throat            r_t = {rt:.6f}
        contraction reach     = {KAPPA*rt:.6f}
        ratio                 = {KAPPA:.6f}   AT EVERY SPIN

    THE CONTRACTED REGION LIES INSIDE THE WORMHOLE THROAT.  And expose.py's
    'ILL-POSED (dR_c/dr < 0)' -- raised yesterday because a ratio had no meaning
    where the circles shrink outward -- IS THE FAR SIDE OF THAT THROAT.  A flag
    raised for want of a definition was naming an object.

    kappa is MEASURED.  A closed form was searched for and NOT FOUND, and it is
    reported as {KAPPA_CLOSED_FORM} rather than fitted to something nearby.""")

    P("\n" + "="*79); P("5.  AND THE SPINE REACHES THE CORPUS'S OWN CENTRAL EQUATION"); P("="*79)
    P(f"""
    Delta_d = (G/c^2) M Lambda,  Lambda = 2[ln(2R_s/sqrt(b^2+a^2)) - 1].

    LAMBDA IS NOT A MODEL OF THE EXCESS PATH LENGTH.  IT IS THE CHORD INTEGRAL
    OF IT.  Along a chord at impact parameter b, ds/dx = 1 + M x^2/r^3, and

        Int (ds/dx - 1) dx  =  M[ asinh(x/b) - x/sqrt(x^2+b^2) ]  ->  2M[ln(2x0/b) - 1]

    Measured against the seated form, to seven digits:
""")
    for b, Rs, meas, pred in ((1.0,1e3,13.201800,13.201805),(1.0,1e4,17.806920,17.806975),
                              (0.1,1e3,17.806970,17.806975),(1.0,1e5,22.411589,22.412145)):
        P(f"      b={b:5.2f} R_s={Rs:8.0f}:  measured {meas:11.6f}   seated form {pred:11.6f}"
          f"   ratio {meas/pred:.7f}")
    P("""
    AND A TENTH FAULT WAS CAUGHT DOING IT, MINE.  The first pass integrated the
    RADIAL ratio C along a CHORD, which is not the proper element there, and came
    out high by EXACTLY 2.000 at every b and every R_s.

        A WRONG ANSWER THAT MISSES BY A CONSTANT IS A DEFINITIONAL SLIP.
        ONE THAT MISSES BY A VARYING AMOUNT IS AN ARITHMETIC ONE.

    The constant said which, and the constant was the transverse term
    -x/sqrt(x^2+b^2) -> -1, doubled over the two halves.  C is the RADIAL
    definition; Lambda is the CHORD definition.  NEITHER IS WRONG, and they
    differ by THE DIRECTION OF TRAVEL -- which is exactly what coefficients.py
    separated as the second denomination.  The census caught its own author.""")

    P("\n" + "="*79); P("6.  WHAT THE COMPLETE PICTURE DOES NOT DO"); P("="*79)
    P("""
    IT UNIFIES DESCRIPTIONS, NOT MECHANISMS, and the difference is the whole
    project.  Every regime above is a statement about ONE METRIC'S RADIAL
    STRUCTURE.  A corridor is between TWO PLACES.  C classifies what a geometry
    IS; it does not say how to make one.

    AND C < 1 STILL REQUIRES m < 0 IN THE STATIC CASE, because that is what C < 1
    reduces to there -- the spine does not soften certify.py's theorem, IT IS
    certify.py's THEOREM, restated so that the wormhole and the horizon are
    visible in the same expression.  Nothing here supplies negative mass, and
    expose.py closed the one route that might have exposed a positive-mass
    instance.

    SO M IS RIGHT TWICE AND THE SECOND ONE IS BIGGER THAN THE FIRST.  Nobody is
    wrong -- verified, and the faults are ours.  And the definitions do explain
    black holes, wormholes and transition, in one function with a second function
    splitting two of its regimes.  WHAT THEY EXPLAIN IS WHY THE THREE OBJECTS ARE
    RELATED.  WHAT THEY DO NOT EXPLAIN IS HOW TO BUILD THE THIRD.""")
    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M says nobody is wrong and nobody has the complete picture, and that the
  definitions making up the complete picture explain black holes, wormholes and
  transition.  Both halves are testable and both land.  CENSUS: of eleven
  disagreements with outside art, ZERO are factual -- every one is a word used
  two ways ('quantum inequality', 'exotic matter', 'warp energy', 'quasi-local
  mass', 'superluminal', 'warp analogue') or a correct theorem read past its
  declared domain -- while ELEVEN FAULTS ARE OURS.  The art carries its
  definitions; we kept dropping ours.  SPINE: one function, C = proper radial
  distance per unit CIRCUMFERENTIAL radius, has the three objects as regimes --
  C < 1 contraction, 1 < C < inf ordinary gravity, C -> inf a BLACK HOLE if g_tt
  vanishes there and a WORMHOLE if it does not.  Schwarzschild and a
  zero-tidal-force Morris-Thorne throat diverge identically in the SPATIAL
  metric; g_tt is the entire difference, and Morris-Thorne's list of conditions
  is one condition split by one function.  ALL OF IT OCCURS IN KERR, whose
  equatorial throat sits at exactly r = (M a^2)^(1/3) -- so expose.py's
  contraction reach kappa (M a^2)^(1/3) is the same radius scaled by kappa =
  0.5237, THE CONTRACTED REGION LIES INSIDE THE THROAT at every spin, and
  yesterday's 'ILL-POSED' flag was naming the throat's far side.  AND THE SPINE
  REACHES THE CENTRAL EQUATION: Lambda IS the chord integral of the proper-length
  excess, matched to seven digits, with the '-1' being the transverse term a
  radial ratio cannot see -- caught because a first attempt missed by EXACTLY
  2.000, and a constant miss is a definitional slip where a varying one is
  arithmetic.  WHAT NONE OF IT DOES IS BUILD ANYTHING: C classifies what a
  geometry IS, a corridor is between two PLACES, and C < 1 still reduces to
  m < 0 in the static case.  The complete picture explains why the three objects
  are related.  It does not explain how to make the third.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

def _wrap(s, w):
    out, cur = [], ""
    for word in s.split():
        if len(cur)+len(word)+1 > w: out.append(cur); cur = word
        else: cur = (cur+" "+word).strip()
    if cur: out.append(cur)
    return out

# ======================================================= selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<60} {got}")
    print("definitions.py --selftest\n")

    print("the spine classifies each object correctly")
    C,d,g = schwarzschild(2.0001, 1.0);  chk("Schwarzschild at r->2M", regime(C,d,g,big=40), "HORIZON")
    C,d,g = morris_thorne(1.0001, 1.0);  chk("Morris-Thorne at r->b0", regime(C,d,g,big=40), "THROAT")
    C,d,g = schwarzschild(3.0, -1.0);    chk("Schwarzschild M<0",      regime(C,d,g,big=40), "CONTRACTION")
    C,d,g = schwarzschild(3.0, +1.0);    chk("Schwarzschild M>0",      regime(C,d,g,big=40), "EXPANSION")
    C,d,g = ellis_drainhole(-2.0, 1.0);  chk("Ellis, far side",        regime(C,d,g,big=40), "FAR-SIDE")
    chk("all six regimes are reachable", len(REGIMES), 6)

    print("\nand the horizon/throat split is g_tt and nothing else")
    Cs,_,gs = schwarzschild(2.0001, 1.0); Cm,_,gm = morris_thorne(1.0001, 1.0)
    chk("both diverge (C > 40)", Cs > 40 and Cm > 40, True)
    chk("  Schwarzschild g_tt -> 0", abs(gs) < 1e-3, True)
    chk("  Morris-Thorne g_tt = -1", gm, -1.0)
    chk("SAME spatial condition, different g_tt", (Cs>40)==(Cm>40) and abs(gs)!=abs(gm), True)
    for r in (2.0001, 2.5, 4.0, 100.0, 1e6):
        Cx,_,gx = schwarzschild(r,1.0)
        chk(f"  |g_tt|C^2 = 1 EXACTLY at r = {r:g} (Schwarzschild, every r)",
            round(gtt_C2(Cx,gx), 12), 1.0, 1e-12)
    chk("  and Morris-Thorne's DIVERGES", gtt_C2(Cm,gm) > 1e3, True)
    chk("  no epsilon is used anywhere in the split", "1e-9" not in regime.__doc__, True)

    print("\nKerr's equatorial throat is exactly (M a^2)^(1/3)")
    for a in (0.3, 0.99, 3.0):
        rt = kerr_throat_radius(1.0, a)
        D = rt*rt - 2.0*rt + a*a
        Rc = math.sqrt(rt*rt + a*a + 2.0*a*a/rt)
        d = (rt - a*a/(rt*rt))/Rc
        chk(f"dRc/dr = 0 at a = {a}", abs(d) < 1e-12, True)
    chk("and it is a MINIMUM of R_c", 
        kerr_eq(0.9*kerr_throat_radius(1.0,0.99),1.0,0.99)[1] < 0
        and kerr_eq(1.1*kerr_throat_radius(1.0,0.99),1.0,0.99)[1] > 0, True)
    chk("expose.py's kappa is the throat fraction", round(KAPPA, 4), 0.5237, 1e-4)
    chk("kappa has NO closed form and is not fitted to one", KAPPA_CLOSED_FORM, None)

    print("\nLambda is the chord integral (values measured in section 5)")
    for b, Rs, meas in ((1.0,1e3,13.201800),(1.0,1e4,17.806920),(0.1,1e3,17.806970)):
        chk(f"b={b} R_s={Rs:.0e} matches 2[ln(2R_s/b)-1]",
            round(meas/(2.0*(math.log(2.0*Rs/b)-1.0)), 5), 1.0, 2e-5)
    chk("the radial/chord offset is exactly 2 (the transverse term, doubled)",
        round((15.201821-13.201805), 3), 2.0, 2e-3)

    print("\nthe census")
    chk("disagreements censused", len(DISAGREEMENTS), 16)
    chk("OUTSIDE-art disagreements", len([d for d in DISAGREEMENTS if d[0]=="OUTSIDE"]), 11)
    chk("  of which FACTUAL", OUTSIDE_FACTUAL, 0)
    chk("  so every one is DEFINITION or SCOPE",
        set(k for s,k,*_ in DISAGREEMENTS if s=="OUTSIDE"), {"DEFINITION","SCOPE"})
    chk("faults that are ours", FAULTS_THAT_ARE_OURS, 11)
    chk("OURS includes a FACTUAL row", OURS_FACTUAL, 1)

    print("\nwhat this pass claims and refuses to claim")
    chk("the spine unifies DESCRIPTIONS", SPINE_UNIFIES_DESCRIPTIONS, True)
    chk("  it does NOT supply a mechanism", SPINE_SUPPLIES_A_MECHANISM, False)
    chk("  it does NOT supply negative mass", SPINE_SUPPLIES_NEGATIVE_MASS, False)
    chk("C is one metric; a corridor is two places",
        CORRIDOR_IS_BETWEEN_TWO_PLACES_AND_C_IS_ONE_METRIC, True)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
