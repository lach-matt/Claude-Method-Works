#!/usr/bin/env python3
r"""
latticectc.py -- O3: THE FLAT-BULK LATTICE THEOREM.  SEATED.  THE CLOSURE REFUSED.

DOCKET 62's O3 pass left one real theorem in /tmp/work (chain.py, lattice.py) and
one proposed closure the ruling refused.  This file seats the theorem, with both
of its controls firing, and records the refusal so it is not re-proposed.

    python3 latticectc.py             the reading
    python3 latticectc.py --selftest  exact rationals + z3; under a minute
    python3 latticectc.py --full      the docket's full chain scan (K <= 4,
                                      |n| <= 6) -- several minutes

===============================================================================
1. THE THEOREM
===============================================================================

HYPOTHESES, named, and there are three:
    H1  the bulk is FLAT, R^{1,d};
    H2  it is quotiented by a rank-n TRANSLATION lattice L acting freely;
    H3  branes are TEST hypersurfaces -- arbitrary timelike hyperplanes in
        arbitrary motion, carrying no back-reaction -- so a causal curve is
        UNCONSTRAINED in the bulk (stronger than GKLP, who keep it on branes).

    (a) A closed causal curve exists in the quotient IFF L contains a nonzero
        causal vector.  The number of legs is irrelevant: REDUCTION LEMMA, a
        chain of K future-causal legs summing to V with total dt > 0 exists iff
        V is itself future-causal and nonzero.  One direction is K = 1; the
        other is that the future causal cone is closed under addition, proved
        here as Cauchy-Schwarz (the Lagrange identity, sympy) plus a scalar
        lemma (z3, unsat), and checked leg-by-leg in z3 at K = 1, 2 (--full:
        up to 4).

    (b) n = 1 with a SPATIAL circle: L = Z xi, xi spacelike, so m^2 |xi|^2 > 0
        for every m != 0.  The condition of (a) is VACUOUS.  GKLP's 'no' is
        therefore FORCED, not contingent -- robust against any number of
        branes, any velocities, any observer boost including supercritical, any
        tilt, any winding, any chain length.

    (c) n >= 2: with Gram entries A = |g1|^2 > 0, C = |g2|^2 > 0, H = <g1,g2>,
        span(L) is TIMELIKE iff H^2 > AC, and then Q(m,n) = A m^2 + 2H mn + C n^2
        is negative on the open interval between the roots of A t^2 + 2H t + C,
        which contains a rational m/n: L CONTAINS a timelike vector and the
        quotient has CTCs.  If span(L) is SPACELIKE (AC > H^2) Q is positive
        definite and no nonzero lattice vector is causal.  CONSTRUCTIVE here:
        timelike_vector() returns the lattice vector, verified in exact
        rationals -- not found by searching a box.

    THE SEPARATING WITNESS, exact.  e1 = (0.9, 1, 0, 0) and e2 = (0.9, 0, 1, 0)
    are both spacelike, |e|^2 = +0.19 each; e1 + e2 = (1.8, 1, 1, 0) is timelike,
    |e1+e2|^2 = -1.24.  A spacelike vector spans a spacelike line; two spacelike
    vectors need not span a spacelike plane.

    THE BOUNDARY.  g1 = (1, 1, s) with s irrational, g2 = (0, 0, 1): every
    nonzero lattice vector has norm (ms + n)^2 > 0, so no CTC -- but span(L)
    contains the null vector (1, 1, 0), so there is no global linear time
    function.  Causal but not stably causal.  Measure zero, and exactly where
    the two routes below come apart.

===============================================================================
2. WITHDRAWAL SEATED: DOCKET 57's "TWO INDEPENDENT ROUTES"
===============================================================================

At codimension one the two routes are ONE FACT SEEN TWICE: xi spacelike is
equivalent to xi-perp containing a timelike vector (the vector
v = (|xi_x|^2, xi_t xi_x) is orthogonal to xi with |v|^2 = |xi_x|^2 (xi_t^2 -
|xi_x|^2), verified in sympy).  They separate only at rank >= 2, where every
generator can pass route B while the span fails route A -- the witness above --
and the degenerate span is the exact boundary.  The algebraic form DOCKET 57
quotes is a brane-frame special case, not the general theorem.  NARROWED.

===============================================================================
3. WHAT IS REFUSED, AND RECORDED SO IT IS NOT RE-PROPOSED
===============================================================================

    THE CODIMENSION-ONE CTC AS A BRANEWORLD RESULT.  The pass built a 5D metric
    by letting both of PPDW's 6D warp functions depend on one coordinate, on the
    warrant "nothing forbids two independent warp functions of one coordinate".
    It has no bulk field equation, no brane action, no Israel junction
    condition [K_ab] - h_ab [K] = -8 pi G_5 S_ab, no Z2 identification, and its
    stress tensor is read off its own Einstein tensor.  A braneworld is not a
    metric with a distinguished slice.  What it establishes is "there exists a
    5D Lorentzian metric containing a CTC" -- Goedel 1949, never in doubt --
    and it is bought with the ledger's own refused currency: the static-observer
    density is negative and the NEC fails on the u = 0.8 slice that carries the
    negative-time leg.  Those two figures are NOT seated: the category is
    refused, so its numbers are not the board's.
    THE "NEC EVERYWHERE" ROW.  O3 with one clause added; the scan behind it had
    no discriminating power (no profile satisfied the NEC, CTC or not).  Folded
    into O3, not opened.
    THE CALDWELL & LANGLOIS WITHDRAWAL.  No referent: the tree cites them only
    as a bulk-SHORTCUT result (index3.py, nopath.py), never as a no-CTC result.
    Not seated.

O3 stays OPEN, narrowed and split: the flat-bulk quotient case is settled by the
theorem; the warped / field-equation-satisfying case is what remains.
"""

import math
import random
import sys
from fractions import Fraction as Fr

# ---------------------------------------------------------------------------
# The ruling, as data.  ledger.py asks these.
# ---------------------------------------------------------------------------

O3_STATUS = "OPEN (narrowed) -- NOT CLOSED, and split"
O3_CLOSED = False

LATTICE_THEOREM_STATUS = "THEOREM"
LATTICE_THEOREM = ("in a flat bulk quotiented by a rank-n translation lattice L "
                   "acting freely, with branes as test hyperplanes in arbitrary "
                   "motion, a closed causal curve exists iff L contains a "
                   "nonzero causal vector")
HYPOTHESES = ("H1 flat bulk R^{1,d}",
              "H2 quotient by a rank-n translation lattice acting freely",
              "H3 branes are test hypersurfaces; causal curves unconstrained "
              "in the bulk")
GKLP_NO_IS_FORCED = True                 # rank 1, spatial circle: vacuous
RANK2_TIMELIKE_SPAN_HAS_CTC = True
RANK2_SPACELIKE_SPAN_HAS_CTC = False
DEGENERATE_SPAN = "causal but not stably causal -- the exact boundary"

#: The separating witness, exact rationals, (t, x, y, z) with signature (-+++).
WITNESS_E1 = (Fr(9, 10), Fr(1), Fr(0), Fr(0))
WITNESS_E2 = (Fr(9, 10), Fr(0), Fr(1), Fr(0))

#: GKLP's compactification vector at beta = 3/5, 2 pi R = 1, brane frame:
#: xi = (-gamma beta, 0, 0, gamma).  Spacelike, |xi|^2 = +1.
GKLP_BETA = Fr(3, 5)

DOCKET57_TWO_ROUTES = ("NARROWED: at codimension one the two routes are one "
                       "fact seen twice (xi spacelike <=> xi-perp contains a "
                       "timelike vector); they separate only at rank >= 2, "
                       "the degenerate span being the exact boundary; the "
                       "algebraic form quoted is a brane-frame special case")
DOCKET57_ROUTES_INDEPENDENT_AT_CODIM1 = False

CODIM1_CTC_IS_BRANEWORLD_RESULT = False
CODIM1_CTC_REFUSAL = ("hand-written 5D metric: no bulk field equation, no brane "
                      "action, no Israel junction condition, no Z2; stress "
                      "tensor read off its own Einstein tensor; NEC-violating "
                      "on the CTC slice -- Goedel-class, not a braneworld")
NEC_EVERYWHERE_ROW_OPENED = False
CALDWELL_LANGLOIS_WITHDRAWAL_SEATED = False

O3_ANSWERED_BY = ("a CTC in a braneworld whose bulk satisfies its field "
                  "equations with Israel junction conditions at the brane -- "
                  "with the NEC satisfied everywhere, the folded-in clause -- "
                  "or a theorem forbidding one beyond the flat quotient (the "
                  "flat quotient itself is settled by D21)")
#: CORRECTED IN PLACE (consolidation verifier, DOCKETS 62/63): this string
#: previously ended "...beyond the flat quotient, which the lattice theorem now
#: settles" -- readable as D21 settling the beyond-flat question.  D21 is seated
#: for the flat bulk only; the beyond-flat theorem is what the row still asks.
O3_ANSWERED_BY_WITHDRAWN_WORDING = ("a theorem forbidding one beyond the flat "
                                    "quotient, which the lattice theorem now "
                                    "settles")

NOT_SEARCHED = ("Tipler", "Hawking chronology protection",
                "Hawking & Ellis Prop 6.4.2", "Polychronakos 2210.11497")


# ============================================================ exact geometry
def nrm(v):
    """Minkowski norm, signature (-,+,+,...): negative is timelike."""
    return -v[0] * v[0] + sum(c * c for c in v[1:])


def ip(a, b):
    return -a[0] * b[0] + sum(a[i] * b[i] for i in range(1, len(a)))


def add(a, b, m=1, n=1):
    return tuple(m * x + n * y for x, y in zip(a, b))


def gklp_xi(beta=GKLP_BETA):
    """(-gamma beta, 0, 0, gamma) with gamma = 1/sqrt(1-beta^2), exact at 3/5."""
    g2 = 1 / (1 - beta * beta)
    g = Fr(math.isqrt(g2.numerator), math.isqrt(g2.denominator))
    assert g * g == g2, "gamma must be rational for an exact witness"
    return (-g * beta, Fr(0), Fr(0), g)


def gram(g1, g2):
    return nrm(g1), nrm(g2), ip(g1, g2)


def span_kind(g1, g2):
    """'timelike' if span(g1,g2) contains a timelike vector, 'spacelike' if the
    induced form is positive definite, 'degenerate' otherwise.  Exact."""
    A, C, H = gram(g1, g2)
    det = A * C - H * H
    if A > 0 and det > 0:
        return "spacelike"
    if det < 0:
        return "timelike"
    return "degenerate"


def timelike_vector(g1, g2):
    """CONSTRUCTIVE (c): for a timelike span with spacelike generators, return
    integers (m, n) with Q(m, n) < 0, verified exactly.  Terminates: once
    q > 2/width the interval q*(t-, t+) holds an integer."""
    A, C, H = gram(g1, g2)
    assert A > 0 and H * H > A * C, "needs A > 0 and a timelike span"
    D = math.sqrt(float(H * H - A * C))
    lo, hi = (-float(H) - D) / float(A), (-float(H) + D) / float(A)
    q = 1
    while True:
        for p in (math.floor(q * (lo + hi) / 2), math.ceil(q * (lo + hi) / 2)):
            if A * p * p + 2 * H * p * q + C * q * q < 0:
                return p, q
        q += 1


def rank1_has_causal(g, mmax=40):
    return any(nrm(tuple(m * c for c in g)) <= 0 for m in range(-mmax, mmax + 1) if m)


def box_has_causal(g1, g2, nmax=30):
    """Brute force -- used only as the CONTROL that must return 0 on spacelike spans."""
    for m in range(-nmax, nmax + 1):
        for n in range(-nmax, nmax + 1):
            if (m, n) != (0, 0) and nrm(add(g1, g2, m, n)) <= 0:
                return True
    return False


def census(seed, want, count, dim=3):
    """Random exact-rational rank-2 lattices in R^{1,dim-1} with SPACELIKE
    generators and the requested span kind."""
    rnd = random.Random(seed)
    out = []
    while len(out) < count:
        g1 = tuple(Fr(rnd.randint(-9, 9), rnd.randint(1, 7)) for _ in range(dim))
        g2 = tuple(Fr(rnd.randint(-9, 9), rnd.randint(1, 7)) for _ in range(dim))
        if nrm(g1) > 0 and nrm(g2) > 0 and span_kind(g1, g2) == want:
            out.append((g1, g2))
    return out


# COMPUTED AT IMPORT, exact, for ledger.py.
WITNESS_NORMS = (nrm(WITNESS_E1), nrm(WITNESS_E2), nrm(add(WITNESS_E1, WITNESS_E2)))
WITNESS_SPAN = span_kind(WITNESS_E1, WITNESS_E2)


# ============================================================ z3 legs
def chain_to(z3, V, K, timeout_ms=20000):
    """Does a closed chain of K future-causal legs summing to V exist, total dt > 0?"""
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    dts, dxs = [], []
    for i in range(K):
        dt = z3.Real("dt%d" % i)
        dx = [z3.Real("dx%d_%d" % (i, k)) for k in range(len(V) - 1)]
        dts.append(dt)
        dxs.append(dx)
        s.add(dt >= 0)
        s.add(dt * dt >= z3.Sum([c * c for c in dx]))
    s.add(z3.Sum(dts) == z3.RealVal(str(V[0])))
    for k in range(len(V) - 1):
        s.add(z3.Sum([dxs[i][k] for i in range(K)]) == z3.RealVal(str(V[k + 1])))
    s.add(z3.Sum(dts) > 0)
    return s.check()


def chain_scan(z3, gens, nmax, K):
    """Windings n with |n_i| <= nmax whose closing vector admits a K-leg chain."""
    import itertools
    hits = []
    for ns in itertools.product(*([range(-nmax, nmax + 1)] * len(gens))):
        if all(n == 0 for n in ns):
            continue
        V = [-sum(ns[a] * gens[a][k] for a in range(len(gens))) for k in range(4)]
        if chain_to(z3, V, K) == z3.sat:
            hits.append(ns)
    return hits


def cone_is_convex(z3, sp):
    """The future causal cone is closed under addition, in any dimension.

    Cauchy-Schwarz by the Lagrange identity (sympy, d = 3), then the scalar
    lemma in z3: t1 >= a >= 0, t2 >= b >= 0, dot <= a b  =>
    (t1+t2)^2 >= a^2 + b^2 + 2 dot.  Returns (lagrange residual, z3 verdict)."""
    x = sp.symbols('x0:3', real=True)
    y = sp.symbols('y0:3', real=True)
    nx2 = sum(c * c for c in x)
    ny2 = sum(c * c for c in y)
    dot = sum(a * b for a, b in zip(x, y))
    lag = sum((x[i] * y[j] - x[j] * y[i]) ** 2 for i in range(3) for j in range(i + 1, 3))
    resid = sp.expand(nx2 * ny2 - dot ** 2 - lag)
    t1, t2, a, b, d = z3.Reals('t1 t2 a b d')
    s = z3.Solver()
    s.add(a >= 0, b >= 0, t1 >= a, t2 >= b, d <= a * b)
    s.add((t1 + t2) * (t1 + t2) < a * a + b * b + 2 * d)
    return resid, s.check()


def codim1_one_fact(sp):
    """xi spacelike => v = (|xi_x|^2, xi_t xi_x) is orthogonal and timelike.
    Residuals of <v, xi> and of |v|^2 - |xi_x|^2 (xi_t^2 - |xi_x|^2), 1+3 dims."""
    xt = sp.Symbol('xi_t', real=True)
    xs = sp.symbols('xi1:4', real=True)
    s2 = sum(c * c for c in xs)
    v = (s2,) + tuple(xt * c for c in xs)
    xi = (xt,) + xs
    return (sp.expand(ip(v, xi)),
            sp.expand(nrm(v) - s2 * (xt * xt - s2)))


# ============================================================ report / selftest
def report():
    print(__doc__.split("=====", 1)[0].strip())
    e1, e2 = WITNESS_E1, WITNESS_E2
    print("\nTHE WITNESS  |e1|^2 = %s  |e2|^2 = %s  |e1+e2|^2 = %s  span: %s"
          % (nrm(e1), nrm(e2), nrm(add(e1, e2)), span_kind(e1, e2)))
    print("  constructive timelike lattice vector (m, n) =", timelike_vector(e1, e2))
    xi = gklp_xi()
    print("GKLP xi = %s, |xi|^2 = %s: rank 1, spatial -- no causal multiple"
          % (tuple(str(c) for c in xi), nrm(xi)))
    print("\nO3: %s" % O3_STATUS)
    print("REFUSED: the codimension-one CTC as a braneworld result -- %s" % CODIM1_CTC_REFUSAL)
    print("RESTATED: %s" % O3_ANSWERED_BY)
    return 0


def selftest(full=False):
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-62s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    try:
        import sympy as sp
        import z3
    except ImportError as exc:                       # pragma: no cover
        raise SystemExit("latticectc.py --selftest needs sympy and z3: %s" % exc)

    print("1. THE WITNESS, EXACT")
    e1, e2 = WITNESS_E1, WITNESS_E2
    chk("|e1|^2 = +0.19 (spacelike)", nrm(e1), Fr(19, 100))
    chk("|e2|^2 = +0.19 (spacelike)", nrm(e2), Fr(19, 100))
    chk("|e1+e2|^2 = -1.24 (timelike)", nrm(add(e1, e2)), Fr(-124, 100))
    chk("so span(e1, e2) is timelike", span_kind(e1, e2), "timelike")
    m, n = timelike_vector(e1, e2)
    chk("constructive: m e1 + n e2 is timelike, exactly", nrm(add(e1, e2, m, n)) < 0, True)

    print("\n2. THE REDUCTION LEMMA -- THE NUMBER OF LEGS DOES NOT MATTER")
    resid, verdict = cone_is_convex(z3, sp)
    chk("Lagrange identity |x|^2|y|^2 - (x.y)^2 = sum of squares", resid, 0)
    chk("scalar lemma: sum of future-causal is future-causal (z3)", str(verdict), "unsat")
    for V, want in (((1, 0, 0, 0), "sat"), ((1, 2, 0, 0), "unsat"),
                    ((2, 1, 1, 0), "sat"), ((-1, 0, 0, 0), "unsat")):
        for K in ((1, 2, 3) if full else (1, 2)):
            chk("V = %s, K = %d legs" % (V, K), str(chain_to(z3, V, K)), want)

    print("\n3. ROUTE A, MACHINE-CHECKED -- AND BOTH CONTROLS FIRE")
    xi = gklp_xi()
    chk("GKLP xi is spacelike, |xi|^2 = +1", nrm(xi), 1)
    for K in ((1, 2, 3, 4) if full else (1, 2)):
        chk("codim 1 flat bulk: K = %d, |n| <= 6 -> closed chains" % K,
            len(chain_scan(z3, [xi], 6, K)), 0)
    for K in ((1, 3) if full else (1, 2)):
        chk("CONTROL I: timelike span, K = %d, |n| <= 2 -> 4 (instrument CAN say yes)" % K,
            len(chain_scan(z3, [e1, e2], 2, K)), 4)
    s1, s2 = (Fr(0), Fr(1), Fr(0), Fr(0)), (Fr(1, 2), Fr(0), Fr(1), Fr(0))
    chk("CONTROL II: the spacelike pair spans a spacelike plane", span_kind(s1, s2),
        "spacelike")
    for K in ((1, 2, 3) if full else (1, 2)):
        chk("CONTROL II: spacelike span, K = %d, |n| <= %d -> 0 (rank is not the trigger)"
            % (K, 4 if full else 2), len(chain_scan(z3, [s1, s2], 4 if full else 2, K)), 0)

    print("\n4. THE CODIMENSION THEOREM, EXACT RATIONALS")
    N = 2000 if full else 400
    tl = census(7, "timelike", N)
    chk("timelike-span rank-2 lattices: constructive causal vector in all %d" % N,
        all(nrm(add(g1, g2, *timelike_vector(g1, g2))) < 0 for g1, g2 in tl), True)
    sl = census(23, "spacelike", N)
    chk("spacelike-span: positive definite (A > 0, AC - H^2 > 0) in all %d" % N,
        all(gram(g1, g2)[0] > 0 and gram(g1, g2)[0] * gram(g1, g2)[1]
            > gram(g1, g2)[2] ** 2 for g1, g2 in sl), True)
    chk("CONTROL: brute force finds no causal vector in any spacelike span (|m|,|n|<=12)",
        sum(box_has_causal(g1, g2, 12) for g1, g2 in sl[:100]), 0)
    chk("CONTROL: the same brute force DOES find one in every timelike span",
        all(box_has_causal(g1, g2, 40) for g1, g2 in tl[:100]), True)
    rnd = random.Random(5)
    r1 = 0
    for _ in range(N):
        while True:
            g = tuple(Fr(rnd.randint(-9, 9), rnd.randint(1, 7)) for _ in range(3))
            if nrm(g) > 0:
                break
        r1 += rank1_has_causal(g)
    chk("rank 1, spacelike generator: causal multiples in %d lattices" % N, r1, 0)

    print("\n5. THE BOUNDARY AND THE WITHDRAWAL")
    s_irr = math.sqrt(2.0)
    chk("degenerate span g1 = (1,1,sqrt2), g2 = (0,0,1): no causal vector, |m|,|n|<=60",
        sum(1 for a in range(-60, 61) for b in range(-60, 61)
            if (a, b) != (0, 0) and (a * s_irr + b) ** 2 <= 1e-12), 0)
    o, w = codim1_one_fact(sp)
    chk("codim 1: v = (|xi_x|^2, xi_t xi_x) is orthogonal to xi", o, 0)
    chk("codim 1: |v|^2 = |xi_x|^2 (xi_t^2 - |xi_x|^2), < 0 iff xi spacelike", w, 0)
    chk("so DOCKET 57's two routes are NOT independent at codimension one",
        DOCKET57_ROUTES_INDEPENDENT_AT_CODIM1, False)

    print("\n6. WHAT IS REFUSED")
    chk("the codimension-one CTC is not a braneworld result",
        CODIM1_CTC_IS_BRANEWORLD_RESULT, False)
    chk("the 'NEC everywhere' row is not opened", NEC_EVERYWHERE_ROW_OPENED, False)
    chk("the Caldwell & Langlois withdrawal is not seated",
        CALDWELL_LANGLOIS_WITHDRAWAL_SEATED, False)
    chk("O3 is not closed", O3_CLOSED, False)
    chk("O3's answering condition no longer carries the withdrawn wording "
        "(record pin)", O3_ANSWERED_BY_WITHDRAWN_WORDING in O3_ANSWERED_BY, False)
    chk("  and scopes D21 to the flat quotient only (record pin)",
        O3_ANSWERED_BY.endswith("(the flat quotient itself is settled by D21)"),
        True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--full" in sys.argv:
        sys.exit(selftest(full=True))
    sys.exit(selftest() if "--selftest" in sys.argv else report())
