#!/usr/bin/env python3
"""
signed.py -- DOCKET 68, work item Q-1s: the signed / complex entropy of a quasi-probability.  Not seated.
Write-up: Q1s-signed.md.  Nothing here edits the board or measure.py: measure.py (A3) and tools/cypher.py are
IMPORTED, never copied.

    python3 signed.py              report (every table below, as data)
    python3 signed.py --selftest   checks with CONTROLS (cases built to fail, which must fail)
    python3 signed.py --json       the report's numbers as JSON

M's ruling (CHARTER.md, 2026-10-03): "we can define this. We plot it. With all its inverses, and reflections on
the same multi-axis graph and the positive values will triangulate the negative values".

WHAT IS COMPUTED (each item is a function below; every number in Q1s-signed.md is printed by this file)
  (1) H = -sum p Log p on the principal branch for a quasi-probability p (sum p = 1, some p_i < 0):
      Re H = -sum p ln|p| (branch-free), Im H = pi N, N = total negative weight.  The branch set: entry i on
      branch k_i adds -2 pi i k_i p_i to H (NOT 2 pi i k per negative entry -- that is the shift of the LOG; see
      discrepancy D1).  A UNIFORM shift k on every entry adds exactly -2 pi i k (because sum p = 1).
      The multi-axis table: per entry (p, |p|, ln|p|, arg, reflected arg, Re/Im contributions, inverse axis
      -Log p, branch step), the branch grid, the reflection (conjugate) and the N-sweep of p = (1+N, -N).
  (2) Products: Re H additive (needs sum p = 1: control with sum p = 2 FAILS); Im H = pi(N_p P_q + P_p N_q),
      P = 1 + N the positive mass, so Im H is superadditive by 2 pi N_p N_q; M = ln sum|p| additive and zero
      iff no entry is negative; N = (sum|p| - 1)/2.  Exact (sympy) on a 2x2 sign pattern, numeric on random.
  (3) Re H < 0: exact range for n entries and negativity N > 0,
        min = -P ln P + N ln(N/(n-1)),   max = -P ln(P/(n-1)) + N ln N,   P = 1 + N,
      the threshold N*(n) above which EVERY n-entry quasi-distribution has Re H < 0, and a random search that
      can falsify the bounds.  (1.5, -0.5) -> -0.954771 nats.
  (4) Baez-Fritz-Leinster (1106.1791v3 Thm 2, p.4, READ) restated on signed measures (H-FINSIGNED):
      functoriality is STRUCTURAL for any difference of a state function; convex linearity, continuity and the
      codomain [0, inf) are tested on Re H, M, Im H with computed counterexamples; a 12-functional dictionary
      gives the convex-linear lawful family (null space) and the product-additive family.  Brandenburger-La Mura
      (2410.15976v5, READ) Theorem 1 is checked: their Example 1 reproduced; Re H fails their Axiom 5' (|w|
      weights) and satisfies the same axiom with SIGNED weights; the exponential branch of that signed-weight
      variant violates their Axiom 0 (computed counterexamples).  Uniqueness: what is shown is stated exactly.
  (5) M's triangulation: (a) continuous -- filtered back-projection (inverse Radon, Lvovsky-Raymer
      quant-ph/0511044v2 eqs 19-20 p.7, READ) of the Wigner function of (|0>+|1>)/sqrt 2 from its exact,
      non-negative quadrature marginals, recovering the negative region; controls: 2 angles fail; the vacuum
      reconstructs non-negative at many angles and NOT at 3 angles.  (b) exact -- the discrete Wigner functions
      of a qubit (Wootters net, GHW quant-ph/0401155v6) and a qutrit (Gross quant-ph/0602001v3): Born
      probabilities on the d+1 striations determine the negative entry exactly by GHW eq.(55) p.27; control:
      with d striations two density matrices share every marginal and differ at the negative point.
  (6) The literature READ at source is tabulated in LITERATURE (arXiv id, version, page, what is used).
  (7) Applications: (a) a qubit Wigner function with negativity, exact; (b) A3's Bell pair (measure.BELL,
      imported) on the product phase space; (c) a signed weighting of The Method's index Lambda (tools/cypher via
      A3's route) under H-MOBIUS-WEIGHT.

NAMED HYPOTHESES (every limitation is one)
  H-PRINCIPAL   principal branch, arg in (-pi, pi], arg(negative) = +pi (2310.19296v1 p.5 convention).
  H-READING-M   "inverses and reflections" is READ here as: the branch lattice, the conjugate branch (arg = -pi,
                Im -> -Im) and the inverse axis -Log p (surprisal).  M's meaning is ASKED, not presumed.
  H-NORM        sum p = 1.  Re H additivity depends on it (control).
  H-FINSIGNED   BFL's category with signed measures of total 1, measure-preserving functions, lambda in [0,1].
  H-DICTIONARY  the lawful-family results hold only inside the 12 listed functionals.  Over all continuous
                functionals uniqueness is OPEN.
  H-RD          the Renyi (1961) / Daroczy (1963) step "g is affine or exponential" is NAMED-NOT-READ; it is
                restated and used in 2410.15976v5 pp.3, 11 (READ).
  H-QUBIT-NET   the qubit Wigner function is Wootters' with one of GHW's two quantum nets (p.30-31: two
                equivalence classes, one similarity class).  Negativity of a given state depends on the net.
  H-ODD-WIGNER  the qutrit Wigner function is Gross's (A(0) = parity; quant-ph/0602001v3 p.5 eq.15, Thm 6.5).
  H-PRODUCT-PS  two-qubit Wigner function = tensor product of single-qubit phase-point operators (GHW p.38 eq.73).
  H-FBP         Ram-Lak filter, finite grid and angle count, NOISELESS analytic marginals (H-NOISELESS); the
                finite-sample run is reported, not graded.
  H-MOBIUS-WEIGHT  the signed weighting on Lambda is the Mobius inverse of Lambda's indicator over the coordinate-
                wise order of cypher's rank-coded box, normalised at the bottom cell.  One choice among many; it
                says nothing about register 66 (order ideal), which is not touched here.
  H-UNIFORM     (A3's) every admitted cell equiprobable, for the non-negative baseline.

stdlib + numpy + sympy.
"""
import cmath
import contextlib
import io
import itertools
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402

LN2 = math.log(2.0)
PI = math.pi


# ============================================================================ (1) the complex entropy

def neg(p):
    """N: total negative weight."""
    return -sum(x for x in p if x < 0)


def pos(p):
    """P: total positive weight (= 1 + N when sum p = 1)."""
    return sum(x for x in p if x > 0)


def re_h(p):
    """Re H = -sum p ln|p|, 0 ln 0 = 0.  Branch-free."""
    return -sum(x * math.log(abs(x)) for x in p if x != 0)


def im_h(p):
    """Im H on the principal branch (H-PRINCIPAL): -sum p arg p = pi N."""
    return PI * neg(p)


def H(p, ks=None):
    """H = -sum p_i Log_k p_i with entry i on branch k_i (default principal).  Log_k z = ln|z| + i(arg z + 2 pi k)."""
    ks = ks or [0] * len(p)
    tot = 0j
    for x, k in zip(p, ks):
        if x == 0:
            continue
        arg = PI if x < 0 else 0.0
        tot += -x * complex(math.log(abs(x)), arg + 2 * PI * k)
    return tot


def mana(p):
    """M = ln sum|p| (natural log; Veitch et al. 1307.7171v1 Def.12 p.11 use 'log')."""
    return math.log(sum(abs(x) for x in p))


def multiaxis_table(p):
    """Per-entry axes: the data of M's 'multi-axis graph' (H-READING-M)."""
    rows = []
    for i, x in enumerate(p):
        a = PI if x < 0 else 0.0
        rows.append({"i": i, "p": x, "abs": abs(x), "sign": (x > 0) - (x < 0),
                     "ln_abs": math.log(abs(x)) if x else None,
                     "arg_principal": a, "arg_reflected": -a,
                     "re_contrib": -x * math.log(abs(x)) if x else 0.0,
                     "im_contrib": -x * a,
                     "inverse_axis_re": -math.log(abs(x)) if x else None,     # -Log p (surprisal), real part
                     "inverse_axis_im": -a,
                     "branch_step_im": -2 * PI * x})                           # Im H shift per unit k_i
    return rows


def branch_grid(p, kmax=2):
    """Every branch with k_i in [-kmax, kmax] for each entry.  Returns rows (ks, Re, Im, |H|, arg H, e^H)."""
    out = []
    for ks in itertools.product(range(-kmax, kmax + 1), repeat=len(p)):
        h = H(p, list(ks))
        e = cmath.exp(h)
        out.append({"ks": ks, "re": h.real, "im": h.imag, "abs": abs(h), "arg": cmath.phase(h),
                    "exp_re": e.real, "exp_im": e.imag})
    return out


def n_sweep(Ns=(0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0)):
    """p = (1+N, -N): the curve (Re H, Im H, -Im H [reflection], M, N) -- multi-axis data."""
    rows = []
    for N in Ns:
        p = [1 + N, -N] if N > 0 else [1.0]
        rows.append({"N": N, "re": re_h(p), "im": im_h(p), "im_reflected": -im_h(p), "M": mana(p),
                     "M_bits": mana(p) / LN2, "re_bits": re_h(p) / LN2})
    return rows


# ============================================================================ (2) products

def product(p, q):
    return [a * b for a in p for b in q]


def rand_quasi(rng, n, Ntarget=None, npos=None):
    """A random quasi-probability with sum 1 and n entries, at least one negative (n >= 2)."""
    npos = npos or rng.randint(1, n - 1)
    nneg = n - npos
    N = Ntarget if Ntarget is not None else rng.uniform(0.01, 1.5)
    wp = [rng.random() + 1e-3 for _ in range(npos)]
    wn = [rng.random() + 1e-3 for _ in range(nneg)]
    sp, sn = sum(wp), sum(wn)
    p = [(1 + N) * w / sp for w in wp] + [-N * w / sn for w in wn]
    rng.shuffle(p)
    return p


def rand_prob(rng, n):
    w = [rng.random() + 1e-3 for _ in range(n)]
    s = sum(w)
    return [x / s for x in w]


def additivity_numeric(rng, trials=400):
    w = {"re": 0.0, "im_formula": 0.0, "M": 0.0, "N_identity": 0.0, "im_superadd_min": 1e9, "im_excess_min": 1e9}
    for _ in range(trials):
        p = rand_quasi(rng, rng.randint(2, 5))
        q = rand_quasi(rng, rng.randint(2, 5))
        pq = product(p, q)
        w["re"] = max(w["re"], abs(re_h(pq) - re_h(p) - re_h(q)))
        form = PI * (neg(p) * pos(q) + pos(p) * neg(q))
        w["im_formula"] = max(w["im_formula"], abs(im_h(pq) - form))
        w["M"] = max(w["M"], abs(mana(pq) - mana(p) - mana(q)))
        w["N_identity"] = max(w["N_identity"], abs(neg(pq) - (sum(abs(x) for x in pq) - 1) / 2))
        w["im_excess_min"] = min(w["im_excess_min"], im_h(pq) - im_h(p) - im_h(q))
        w["im_superadd_min"] = min(w["im_superadd_min"],
                                   (im_h(pq) - im_h(p) - im_h(q)) - 2 * PI * neg(p) * neg(q))
    return w


def additivity_unnormalised_control(rng, trials=50):
    """CONTROL: with sum p = 2 the Re H additivity identity must FAIL (it uses sum p = 1)."""
    worst = 0.0
    for _ in range(trials):
        p = [2 * x for x in rand_quasi(rng, 3)]
        q = rand_quasi(rng, 3)
        worst = max(worst, abs(re_h(product(p, q)) - re_h(p) - re_h(q)))
    return worst


def additivity_exact():
    """sympy, exact: p = (1+a, -a), q = (1+b, -b), a, b > 0."""
    import sympy as sp
    a, b = sp.symbols("a b", positive=True)
    p = [1 + a, -a]
    q = [1 + b, -b]

    def reh(v):   # each entry's sign is known symbolically: |x| = x for the (1+.) entries, -x otherwise
        s = 0
        for x in v:
            ax = sp.factor(x if sp.ask(sp.Q.positive(x)) else -x)
            s += -x * sp.expand_log(sp.log(ax), force=True)
        return s

    pq = [sp.expand(x * y) for x in p for y in q]
    d = sp.simplify(sp.expand(reh(pq) - reh(p) - reh(q)))
    Npq = (1 + a) * b + a * (1 + b)                       # the two negative products
    form = (a * (1 + b) + (1 + a) * b)                    # N_p P_q + P_p N_q
    Mdiff = sp.simplify(sp.log(sum(sp.Abs(x) for x in pq)) - sp.log(1 + 2 * a) - sp.log(1 + 2 * b))
    return {"re_residual": str(d), "im_formula_residual": str(sp.simplify(Npq - form)),
            "M_residual": str(sp.simplify(sp.expand_log(Mdiff, force=True))),
            "im_superadditive_excess": str(sp.simplify(Npq - a - b))}


# ============================================================================ (3) where Re H < 0

def reh_bounds(n, N):
    """Exact range of Re H over n-entry quasi-distributions with negativity N > 0 (n >= 2)."""
    P = 1 + N
    lo = -P * math.log(P) + N * math.log(N / (n - 1))
    hi = -P * math.log(P / (n - 1)) + N * math.log(N)
    return lo, hi


def reh_extremals(n, N):
    P = 1 + N
    lo = [P] + [-N / (n - 1)] * (n - 1)
    hi = [P / (n - 1)] * (n - 1) + [-N]
    return lo, hi


def max_reh_floor(n):
    """min over N > 0 of max Re H(n, N).  Exact: max Re H is convex in N with derivative ln((n-1)N/(1+N)), so the
    minimum is at N = 1/(n-2) and equals ln(n-2) (n >= 3).  For n = 2 max Re H < 0 for every N > 0.
    Returned: (N at the minimum by golden-section search, the minimum, the closed form)."""
    if n == 2:
        return None
    f = lambda N: reh_bounds(n, N)[1]
    a, b = 1e-9, 50.0
    gr = (math.sqrt(5) - 1) / 2
    for _ in range(300):
        c, d = b - gr * (b - a), a + gr * (b - a)
        if f(c) < f(d):
            b = d
        else:
            a = c
    Nm = (a + b) / 2
    return {"N_at_min": Nm, "min_of_max": f(Nm), "closed_form_N": 1 / (n - 2), "closed_form_min": math.log(n - 2)}


def bounds_random_search(rng, trials=4000):
    """Random quasi-distributions never leave [lo, hi] (a check that CAN fail), and fraction with Re H < 0."""
    worst_out = 0.0
    for _ in range(trials):
        n = rng.randint(2, 6)
        N = rng.choice([0.05, 0.25, 0.5, 1.0, 2.0])
        p = rand_quasi(rng, n, Ntarget=N)
        lo, hi = reh_bounds(n, N)
        r = re_h(p)
        worst_out = max(worst_out, lo - r, r - hi)
    return worst_out


def range_table():
    rows = []
    for n in (2, 3, 4, 5, 8):
        for N in (0.05, 0.25, 0.5, 1.0, 2.0):
            lo, hi = reh_bounds(n, N)
            rows.append({"n": n, "N": N, "min_nats": lo, "max_nats": hi, "negative_possible": lo < 0,
                         "negative_forced": hi < 0})
    return rows


# ============================================================================ (4) BFL on signed measures; BLM

def push(p, f, ny):
    q = [0.0] * ny
    for i, j in enumerate(f):
        q[j] += p[i]
    return q


def rand_surj(rng, n, m):
    f = list(range(m)) + [rng.randrange(m) for _ in range(n - m)]
    rng.shuffle(f)
    return f


def direct_sum(lam, p1, p2):
    return [lam * x for x in p1] + [(1 - lam) * x for x in p2]


# dictionary of functionals X on signed measures (objects); F_X(f: p -> q) = X(p) - X(q)
def _hplus(p):
    return -sum(x * math.log(x) for x in p if x > 0)


def _J(p):
    return sum(abs(x) * math.log(abs(x)) for x in p if x < 0)


DICT = {
    "h_plus": _hplus,                                       # -sum_{p>0} p ln p
    "J": _J,                                                # sum_{p<0} |p| ln|p|     (Re H = h_plus + J)
    "N": neg,
    "M": mana,
    "N^2": lambda p: neg(p) ** 2,
    "sum_p2": lambda p: sum(x * x for x in p),
    "sum_p_absp": lambda p: sum(x * abs(x) for x in p),
    "NlnN": lambda p: neg(p) * math.log(neg(p)) if neg(p) > 0 else 0.0,
    "PlnP": lambda p: pos(p) * math.log(pos(p)),
    "count_neg": lambda p: float(sum(1 for x in p if x < 0)),
    "hartley": lambda p: math.log(sum(1 for x in p if x != 0)),
    "renyi2_signed": lambda p: -math.log(sum(x * x for x in p)),   # BLM eq.(10) at alpha = 2, natural log
}


def _rand_morphism(rng):
    n = rng.randint(3, 6)
    m = rng.randint(1, n - 1)
    p = rand_quasi(rng, n)
    f = rand_surj(rng, n, m)
    return p, f, m


def convex_residual_matrix(rng, rows=500):
    names = list(DICT)
    R = []
    for _ in range(rows):
        p1, f1, m1 = _rand_morphism(rng)
        p2, f2, m2 = _rand_morphism(rng)
        lam = rng.uniform(0.05, 0.95)
        q1, q2 = push(p1, f1, m1), push(p2, f2, m2)
        P = direct_sum(lam, p1, p2)
        Q = direct_sum(lam, q1, q2)
        row = []
        for nm in names:
            X = DICT[nm]
            row.append((X(P) - X(Q)) - lam * (X(p1) - X(q1)) - (1 - lam) * (X(p2) - X(q2)))
        R.append(row)
    return names, np.array(R)


def product_residual_matrix(rng, rows=300):
    names = list(DICT)
    R = []
    for _ in range(rows):
        p = rand_quasi(rng, rng.randint(2, 4))
        q = rand_quasi(rng, rng.randint(2, 4))
        pq = product(p, q)
        R.append([DICT[nm](pq) - DICT[nm](p) - DICT[nm](q) for nm in names])
    return names, np.array(R)


def null_space(R, rel=1e-9):
    """Null space of R.  Columns that are identically zero (to 1e-12 of the largest column) are null on their own;
    the rest are scaled to unit norm before the SVD, so the tolerance is scale-free."""
    norms = np.linalg.norm(R, axis=0)
    big = max(float(norms.max()), 1.0)
    zero = norms <= 1e-12 * big
    vecs = []
    for j in np.where(zero)[0]:
        e = np.zeros(R.shape[1])
        e[j] = 1.0
        vecs.append(e)
    keep = np.where(~zero)[0]
    s = np.array([])
    if len(keep):
        Rn = R[:, keep] / norms[keep]
        U, s, Vt = np.linalg.svd(Rn, full_matrices=True)
        tol = rel * max(s.max(), 1.0)
        rank = int((s > tol).sum())
        for v in Vt[rank:]:
            e = np.zeros(R.shape[1])
            e[keep] = v / norms[keep]
            vecs.append(e)
    basis = np.array(vecs).T if vecs else np.zeros((R.shape[1], 0))
    return basis, s


def describe_null(names, basis):
    """Reduce the null-space basis to row echelon form and print each vector by its non-zero entries."""
    if basis.shape[1] == 0:
        return []
    B = basis.T.copy()
    out = []
    # Gaussian elimination for a readable basis
    r = 0
    piv_cols = []
    for c in range(B.shape[1]):
        if r >= B.shape[0]:
            break
        piv = np.argmax(np.abs(B[r:, c])) + r
        if abs(B[piv, c]) < 1e-8:
            continue
        B[[r, piv]] = B[[piv, r]]
        B[r] = B[r] / B[r, c]
        for k in range(B.shape[0]):
            if k != r:
                B[k] = B[k] - B[k, c] * B[r]
        piv_cols.append(c)
        r += 1
    for v in B[:r]:
        out.append({names[j]: round(float(v[j]), 9) for j in range(len(names)) if abs(v[j]) > 1e-7})
    return out


def continuity_check(X, steps=(1e-2, 1e-4, 1e-6, 1e-8)):
    """An entry crosses zero: p(t) = (1 + t, 0.5 - t, -0.5) -> merge to a point; F(f_t) -> F(f_0)?"""
    base = [1.0, 0.5, -0.5]
    f0 = X(base) - X([1.0])
    return max(abs((X([1.0 + t, 0.5 - t, -0.5]) - X([1.0])) - f0) for t in steps)


def zero_crossing_continuity(X, eps=1e-9):
    """Value just below, at, and just above a zero entry: discontinuity shows as a jump."""
    a = X([0.5 + eps, 0.5, -eps])
    b = X([0.5, 0.5, 0.0])
    c = X([0.5 - eps, 0.5, eps])
    return max(abs(a - b), abs(c - b))


def bfl_codomain_counterexamples():
    out = {}
    # (i) the one-point crush of (1.5, -0.5): F = Re H(p) - 0
    out["crush_(1.5,-0.5)"] = {"F_reH": re_h([1.5, -0.5]), "F_imH": im_h([1.5, -0.5]),
                               "F_M": mana([1.5, -0.5])}
    # (ii) merge two negative entries: (a, -b, -c) -> (a, -(b+c)); N unchanged, Re H falls by (b+c) H2
    a, b, c = 1.6, 0.3, 0.3
    p, q = [a, -b, -c], [a, -(b + c)]
    out["merge_negatives"] = {"p": p, "q": q, "F_reH": re_h(p) - re_h(q), "F_imH": im_h(p) - im_h(q),
                              "F_M": mana(p) - mana(q),
                              "predicted_F_reH": -(b + c) * math.log(2.0)}
    return out


def nonneg_random(X, rng, trials=600):
    worst = 1e9
    for _ in range(trials):
        p, f, m = _rand_morphism(rng)
        worst = min(worst, X(p) - X(push(p, f, m)))
    return worst


def convex_counterexample_M():
    p1, q1 = [1.5, -0.5], [1.0]
    p2, q2 = [0.5, 0.5], [1.0]
    lam = 0.5
    P, Q = direct_sum(lam, p1, p2), direct_sum(lam, q1, q2)
    lhs = mana(P) - mana(Q)
    rhs = lam * (mana(p1) - mana(q1)) + (1 - lam) * (mana(p2) - mana(q2))
    return {"lhs": lhs, "rhs": rhs, "gap": lhs - rhs}


# Brandenburger-La Mura 2410.15976v5 (READ): generalised signed measures with sum p != 0, log base 2
def blm_reh(P):
    return -sum(x * math.log2(abs(x)) for x in P if x != 0) / sum(P)


def blm_shannon_abs(P):
    """their eq.(11), p.4: the |p|-weighted 'signed Shannon' they exclude."""
    return -sum(abs(x) * math.log2(abs(x)) for x in P if x != 0) / abs(sum(P))


def blm_renyi(P, alpha):
    """their eq.(10), p.4."""
    return -1.0 / (alpha - 1) * math.log2(sum(abs(x) ** alpha for x in P if x != 0) / abs(sum(P)))


def blm_renorm1(P):
    """their eq.(45), p.9."""
    return -math.log2(sum(abs(x) for x in P) / abs(sum(P)))


def signed_weight_exponential(P, alpha):
    """The exponential branch of the SIGNED-weight mean-value rule: argument sum sign(p)|p|^alpha / sum p."""
    return sum((1 if x > 0 else -1) * abs(x) ** alpha for x in P if x != 0) / sum(P)


def axiom0_counterexample(alpha):
    """A signed probability measure (sum 1) on which the signed-weight exponential branch is not real."""
    if alpha > 1:
        b = 1.0
        eps = 0.5 * (0.5) ** (1.0 / (alpha - 1))
        k = int(math.ceil((1 + b) / eps))
        P = [(1 + b) / k] * k + [-b]
    else:
        B = 1.0
        m = 2
        while (1 + B) ** alpha - m ** (1 - alpha) * B ** alpha >= 0:
            m *= 2
        P = [1 + B] + [-B / m] * m
    return P, signed_weight_exponential(P, alpha)


def blm_checks():
    out = {}
    out["example1_abs_P"] = blm_shannon_abs([2, -1])                 # READ p.4: -2
    out["example1_abs_PQ"] = blm_shannon_abs([4, -2, -2, 1])         # READ p.4: -12
    out["reH_P"] = blm_reh([2, -1])
    out["reH_PQ"] = blm_reh([4, -2, -2, 1])
    # mean-value with P = (-0.5), Q = (1.5): affine g, |w| weights (5') vs signed weights
    P, Q = [-0.5], [1.5]
    wP, wQ = sum(P), sum(Q)
    union = blm_reh(P + Q)
    out["mv_union"] = union
    out["mv_abs_weights"] = (abs(wP) * blm_reh(P) + abs(wQ) * blm_reh(Q)) / abs(wP + wQ)
    out["mv_signed_weights"] = (wP * blm_reh(P) + wQ * blm_reh(Q)) / (wP + wQ)
    out["calibration_H((1/2))"] = blm_reh([0.5])
    # Re H is not a signed Renyi entropy for any alpha (scan): the best alpha still misses on a test set
    tests = [[1.5, -0.5], [2, -1], [0.7, 0.4, -0.1], [1.2, -0.1, -0.1], [0.5, 0.5]]
    best = min((max(abs(blm_reh(t) - blm_renyi(t, a)) for t in tests), a)
               for a in [x / 100 for x in range(5, 600) if x != 100])
    out["closest_signed_renyi_alpha"] = best[1]
    out["closest_signed_renyi_maxgap_bits"] = best[0]
    out["renorm1_vs_minus_M_bits"] = blm_renorm1([1.5, -0.5]) + mana([1.5, -0.5]) / LN2
    out["axiom0"] = {a: axiom0_counterexample(a)[1] for a in (0.1, 0.5, 0.9, 1.1, 2.0, 3.0, 5.0)}
    return out


def signed_mean_value_random(rng, trials=300):
    """Re H (BLM normalisation) obeys the SIGNED-weight mean-value rule exactly with affine g, on random splits."""
    worst = 0.0
    for _ in range(trials):
        A = [rng.uniform(-1, 2) for _ in range(rng.randint(1, 4))]
        B = [rng.uniform(-1, 2) for _ in range(rng.randint(1, 4))]
        if min(abs(sum(A)), abs(sum(B)), abs(sum(A) + sum(B))) < 1e-2 or 0 in A + B:
            continue
        lhs = blm_reh(A + B)
        rhs = (sum(A) * blm_reh(A) + sum(B) * blm_reh(B)) / (sum(A) + sum(B))
        worst = max(worst, abs(lhs - rhs))
    return worst


def blm_extensivity_random(rng, trials=300):
    worst = 0.0
    for _ in range(trials):
        A = [rng.uniform(-1, 2) for _ in range(rng.randint(1, 4))]
        B = [rng.uniform(-1, 2) for _ in range(rng.randint(1, 4))]
        if min(abs(sum(A)), abs(sum(B))) < 1e-2 or 0 in A + B:
            continue
        worst = max(worst, abs(blm_reh(product(A, B)) - blm_reh(A) - blm_reh(B)))
    return worst


# ============================================================================ (5) triangulation

def psi_n(n, x):
    """Harmonic-oscillator eigenfunctions, hbar = 1 (Lvovsky-Raymer eq.26 p.8)."""
    h0 = np.ones_like(x)
    if n == 0:
        H_ = h0
    else:
        hm, H_ = h0, 2 * x
        for k in range(1, n):
            hm, H_ = H_, 2 * x * H_ - 2 * k * hm
    return np.pi ** -0.25 * H_ / math.sqrt(2.0 ** n * math.factorial(n)) * np.exp(-x * x / 2)


def marginal(coeffs, theta, s):
    """pr(s, theta) = |sum_n c_n e^{-i n theta} psi_n(s)|^2: a Born probability density, non-negative."""
    amp = sum(c * np.exp(-1j * n * theta) * psi_n(n, s) for n, c in enumerate(coeffs))
    return np.abs(amp) ** 2


def wigner_exact(state, X, Pm):
    """Closed forms (checked against the marginals in selftest): W(x,p), hbar = 1, integral W = 1."""
    r2 = X ** 2 + Pm ** 2
    if state == "vac":
        return np.exp(-r2) / np.pi
    if state == "fock1":
        return (2 * r2 - 1) * np.exp(-r2) / np.pi
    if state == "sup01":     # (|0> + |1>)/sqrt 2
        return (r2 + math.sqrt(2) * X) * np.exp(-r2) / np.pi
    raise ValueError(state)


STATE_COEFFS = {"vac": [1.0], "fock1": [0.0, 1.0], "sup01": [1 / math.sqrt(2), 1 / math.sqrt(2)]}


def fbp(state, K, grid_half=3.5, ngrid=141, S=7.0, ds=0.01, marginals=None):
    """Filtered back-projection (Ram-Lak), W(x,p) = sum_k (pi/K) Q_k(x cos th_k + p sin th_k)."""
    s = np.arange(-S, S + ds / 2, ds)
    npad = 1
    while npad < 4 * len(s):
        npad *= 2
    nu = np.fft.fftfreq(npad, d=ds)
    filt = np.abs(nu)
    g = np.linspace(-grid_half, grid_half, ngrid)
    X, Pm = np.meshgrid(g, g, indexing="ij")
    W = np.zeros_like(X)
    thetas = np.arange(K) * np.pi / K
    for k, th in enumerate(thetas):
        pr = marginals[k] if marginals is not None else marginal(STATE_COEFFS[state], th, s)
        # Q(t) = int |nu| P^(nu) e^{2 pi i nu t} d nu with P^ = ds * FFT and d nu = 1/(npad ds): Q = ifft(FFT |nu|)
        Q = np.real(np.fft.ifft(np.fft.fft(pr, n=npad) * filt))[: len(s)]
        t = X * np.cos(th) + Pm * np.sin(th)
        W += np.interp(t, s, Q) * (np.pi / K)
    return g, X, Pm, W


def fbp_metrics(state, K, thr=0.02):
    g, X, Pm, Wr = fbp(state, K)
    We = wigner_exact(state, X, Pm)
    err = float(np.max(np.abs(Wr - We)))
    me, mr = (We < -thr), (Wr < -thr)
    union = (me | mr).sum()
    iou = float((me & mr).sum() / union) if union else 1.0
    ie, ir = np.unravel_index(np.argmin(We), We.shape), np.unravel_index(np.argmin(Wr), Wr.shape)
    return {"state": state, "K": K, "max_abs_err": err, "exact_min": float(We.min()),
            "recon_min": float(Wr.min()), "exact_argmin": (float(g[ie[0]]), float(g[ie[1]])),
            "recon_argmin": (float(g[ir[0]]), float(g[ir[1]])), "neg_region_iou": iou,
            "marginals_min": float(min(marginal(STATE_COEFFS[state], th, np.linspace(-7, 7, 1401)).min()
                                       for th in np.arange(K) * np.pi / K)),
            "exact_negative_volume": float(-We[We < 0].sum() * (g[1] - g[0]) ** 2)}


def fbp_finite_sample(state="sup01", K=72, shots=20000, seed=5):
    """H-NOISELESS relaxed: each angle's marginal replaced by a histogram of `shots` sampled quadratures."""
    rng = np.random.default_rng(seed)
    S, ds = 7.0, 0.01
    s = np.arange(-S, S + ds / 2, ds)
    margs = []
    for k in range(K):
        th = k * np.pi / K
        pr = marginal(STATE_COEFFS[state], th, s)
        cdf = np.cumsum(pr)
        cdf /= cdf[-1]
        xs = np.interp(rng.random(shots), cdf, s)
        h, edges = np.histogram(xs, bins=np.arange(-S - ds / 2, S + ds, ds * 5))
        centers = (edges[:-1] + edges[1:]) / 2
        dens = h / (shots * ds * 5)
        margs.append(np.interp(s, centers, dens))
    g, X, Pm, Wr = fbp(state, K, marginals=margs)
    We = wigner_exact(state, X, Pm)
    i = np.unravel_index(np.argmin(We), We.shape)
    # smooth estimate at the exact minimum: mean over a 5x5 patch (0.25 x 0.25)
    patch = Wr[i[0] - 2:i[0] + 3, i[1] - 2:i[1] + 3]
    return {"K": K, "shots_per_angle": shots, "exact_min": float(We[i]), "recon_at_exact_min_patch": float(patch.mean()),
            "recon_patch_std": float(patch.std())}


def continuous_complex_entropy(state, half=7.0, n=1401):
    g = np.linspace(-half, half, n)
    X, Pm = np.meshgrid(g, g, indexing="ij")
    W = wigner_exact(state, X, Pm)
    dA = (g[1] - g[0]) ** 2
    nz = W != 0
    reh = float(-(W[nz] * np.log(np.abs(W[nz]))).sum() * dA)
    vol_neg = float(-W[W < 0].sum() * dA)
    return {"state": state, "norm": float(W.sum() * dA), "re_h": reh, "im_h": PI * vol_neg, "vol_neg": vol_neg}


# ---- discrete, exact

def qubit_A(sy=+1):
    """Wootters qubit phase-point operators, A(q,p) = (I + (-1)^q Z + (-1)^p X + sy (-1)^{q+p} Y)/2 (H-QUBIT-NET)."""
    import sympy as sp
    I2 = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Z = sp.Matrix([[1, 0], [0, -1]])
    return {(q, p): (I2 + (-1) ** q * Z + (-1) ** p * X + sy * (-1) ** (q + p) * Y) / 2
            for q in range(2) for p in range(2)}


def qutrit_A():
    """Gross's odd-d phase-point operators for d = 3 (H-ODD-WIGNER): A(q,p) = X^q Z^p Par Z^-p X^-q."""
    import sympy as sp
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    d = 3
    Xs = sp.Matrix(d, d, lambda i, j: 1 if i == (j + 1) % d else 0)
    Zs = sp.diag(*[w ** j for j in range(d)])
    Par = sp.Matrix(d, d, lambda i, j: 1 if i == (-j) % d else 0)
    out = {}
    for q in range(d):
        for p in range(d):
            U = Xs ** q * Zs ** p
            out[(q, p)] = sp.simplify(U * Par * U.inv())
    return out


def lines(d):
    """All lines of Z_d^2 (d prime): striation by direction, each with d parallel lines."""
    dirs = [(0, 1)] + [(1, m) for m in range(d)]
    out = []
    for (a, b) in dirs:
        seen = set()
        for q0 in range(d):
            for p0 in range(d):
                L = frozenset(((q0 + t * a) % d, (p0 + t * b) % d) for t in range(d))
                if L not in seen:
                    seen.add(L)
                    out.append(((a, b), L))
    return out


def wigner_discrete(rho, A, d):
    import sympy as sp
    return {k: sp.nsimplify(sp.simplify((rho * v).trace() / d)) for k, v in A.items()}


def triangulate_exact(rho, A, d, use_dirs=None):
    """Born probabilities P(line) = Tr(rho Q(line)), Q = (1/d) sum_{a in line} A(a) (checked rank-1 projectors);
    reconstruction W(a) = (1/d)(sum_{lines through a} P(line) - 1) (GHW quant-ph/0401155v6 eq.(55) p.27)."""
    import sympy as sp
    Ls = lines(d)
    projs_ok = True
    P = {}
    for dirn, L in Ls:
        Q = sp.simplify(sum((A[a] for a in L), sp.zeros(d, d)) / d)
        if sp.simplify(Q * Q - Q) != sp.zeros(d, d) or sp.simplify(Q.trace()) != 1:
            projs_ok = False
        P[(dirn, L)] = sp.nsimplify(sp.simplify((rho * Q).trace()))
    W = {}
    for a in A:
        W[a] = sp.nsimplify(sp.simplify((sum(P[k] for k in P if a in k[1]) - 1) / d))
    return projs_ok, P, W


def bloch_rho(v):
    import sympy as sp
    x, y, z = v
    return sp.Matrix([[1 + z, x - sp.I * y], [x + sp.I * y, 1 - z]]) / 2


def qutrit_strange_rho():
    import sympy as sp
    S = sp.Matrix([0, 1, -1]) / sp.sqrt(2)
    return S * S.T


def striation_control_numeric(d=3, keep=3, eps_scan=(0.05, 0.02, 0.01, 0.005)):
    """CONTROL: with `keep` < d+1 striations the line-sum map has a kernel; a second density matrix shares every
    kept marginal and differs at the negative point.  Numeric (numpy), d = 3."""
    import sympy as sp
    A = {k: np.array(sp.N(v), dtype=complex) for k, v in qutrit_A().items()}
    pts = sorted(A)
    Ls = lines(d)
    dirs = sorted({dr for dr, _ in Ls})
    kept_dirs = dirs[:keep]
    rows_all = [[1.0 if a in L else 0.0 for a in pts] for _, L in Ls]
    rows_kept = [[1.0 if a in L else 0.0 for a in pts] for dr, L in Ls if dr in kept_dirs]
    rank_all = int(np.linalg.matrix_rank(np.array(rows_all)))
    rank_kept = int(np.linalg.matrix_rank(np.array(rows_kept)))
    # kernel of the kept line sums
    U, s, Vt = np.linalg.svd(np.array(rows_kept))
    ker = Vt[rank_kept:]
    i0 = pts.index((0, 0))
    v = ker[np.argmax(np.abs(ker[:, i0]))]
    v = v / v[i0]                                       # kernel vector with value 1 at the origin
    Kop = sum(v[j] * A[pts[j]] for j in range(len(pts)))
    Sv = np.array([0, 1, -1]) / math.sqrt(2)
    rho = 0.9 * np.outer(Sv, Sv) + 0.1 * np.eye(3) / 3
    eps = None
    for e in eps_scan:
        if np.linalg.eigvalsh(rho + e * Kop).min() >= -1e-12:
            eps = e
            break
    rho2 = rho + eps * Kop
    W1 = np.array([np.trace(rho @ A[a]).real / d for a in pts])
    W2 = np.array([np.trace(rho2 @ A[a]).real / d for a in pts])
    kept_gap = max(abs(sum(W1[pts.index(a)] - W2[pts.index(a)] for a in L)) for dr, L in Ls if dr in kept_dirs)
    dropped_gap = max(abs(sum(W1[pts.index(a)] - W2[pts.index(a)] for a in L)) for dr, L in Ls if dr not in kept_dirs)
    return {"rank_all_striations": rank_all, "rank_kept": rank_kept, "points": len(pts), "eps": eps,
            "rho2_min_eig": float(np.linalg.eigvalsh(rho2).min()), "kept_marginal_gap": float(kept_gap),
            "dropped_striation_gap": float(dropped_gap), "W_origin_rho": float(W1[i0]), "W_origin_rho2": float(W2[i0])}


# ============================================================================ (7) applications

def app_qubit():
    """(a) The Bloch state (-1,-1,-1)/sqrt 3 under both GHW qubit nets (H-QUBIT-NET), exact."""
    import sympy as sp
    v = [-1 / sp.sqrt(3)] * 3
    rho = bloch_rho(v)
    out = {}
    for sy in (+1, -1):
        A = qubit_A(sy)
        W = wigner_discrete(rho, A, 2)
        pv = [float(W[k]) for k in sorted(W)]
        out[f"net_sy={sy:+d}"] = {"W": {str(k): str(W[k]) for k in sorted(W)}, "N": neg(pv),
                                  "re_h_nats": re_h(pv), "im_h": im_h(pv), "M_nats": mana(pv)}
    # max negativity over pure qubit states for net sy=+1 (grid over the sphere)
    best = (0, None)
    for th in np.linspace(0, np.pi, 181):
        for ph in np.linspace(0, 2 * np.pi, 361):
            x, y, z = np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)
            Ws = [(1 + (-1) ** q * z + (-1) ** p * x + (-1) ** (q + p) * y) / 4 for q in range(2) for p in range(2)]
            if neg(Ws) > best[0]:
                best = (neg(Ws), (float(x), float(y), float(z)))
    out["max_N_pure_net+1"] = {"N": best[0], "bloch": best[1], "exact_(sqrt3-1)/4": (math.sqrt(3) - 1) / 4}
    return out


def app_bell():
    """(b) A3's Bell pair (measure.BELL, imported) on the product phase space (H-PRODUCT-PS)."""
    import measure
    A1 = {k: np.array(v.evalf(), dtype=complex) for k, v in qubit_A(+1).items()}
    rho = np.outer(measure.BELL, measure.BELL.conj())
    W = {}
    for a in A1:
        for b in A1:
            W[(a, b)] = float(np.trace(rho @ np.kron(A1[a], A1[b])).real / 4)
    pv = list(W.values())
    WA = {}
    for (a, b), w in W.items():
        WA[a] = WA.get(a, 0.0) + w
    WB = {}
    for (a, b), w in W.items():
        WB[b] = WB.get(b, 0.0) + w
    out = {"values": sorted({round(x, 12) for x in pv}), "count_negative": sum(1 for x in pv if x < 0),
           "sum": sum(pv), "N": neg(pv), "re_h_bits": re_h(pv) / LN2, "im_h": im_h(pv), "M_bits": mana(pv) / LN2,
           "re_h_A_bits": re_h(list(WA.values())) / LN2, "re_h_B_bits": re_h(list(WB.values())) / LN2,
           "measure_conditional_entropy_bell_bits": measure.conditional_entropy_bell()}
    out["re_h_mutual_bits"] = out["re_h_A_bits"] + out["re_h_B_bits"] - out["re_h_bits"]
    return out


def lambda_mobius(control_box=False, random_set=None, vectors=False):
    """(c) H-MOBIUS-WEIGHT on cypher's Lambda, imported by A3's route (measure.lambda_counts / cypher._lambda).
    vectors=True (added by Q1s-integrate, 2026-10-03) also returns the two normalised signed weightings as lists
    ("p_vector", "q_vector"), so that measure.py's Q-1 can evaluate them itself; nothing else changes."""
    import measure
    import cypher
    cells_n, box_n, E = measure.lambda_counts()
    ix = cypher._lambda()
    shape = tuple(len(a) for a in ix.alphabets)
    ind = np.zeros(shape)
    if control_box:
        ind[...] = 1.0
    elif random_set is not None:
        ind = random_set
    else:
        for c in ix.cells:
            ind[c] = 1.0
    p = ind.copy()
    for ax in range(len(shape)):
        sh = np.zeros_like(p)
        sl_dst = [slice(None)] * len(shape)
        sl_src = [slice(None)] * len(shape)
        sl_dst[ax] = slice(0, shape[ax] - 1)
        sl_src[ax] = slice(1, shape[ax])
        sh[tuple(sl_dst)] = p[tuple(sl_src)]
        p = p - sh
    # reconstruction: suffix sums along every axis must return the indicator
    rec = p.copy()
    for ax in range(len(shape)):
        rec = np.flip(np.cumsum(np.flip(rec, axis=ax), axis=ax), axis=ax)
    bottom = tuple(0 for _ in shape)
    tot = p.sum()
    out = {"cells_imported": cells_n, "box_imported": box_n, "E_order": E, "shape": shape,
           "box_from_shape": int(np.prod(shape)), "bottom_in_set": bool(ind[bottom] == 1.0),
           "reconstruction_max_err": float(np.max(np.abs(rec - ind))), "sum_p": float(tot)}
    if tot != 0:
        pv = (p[p != 0] / tot).ravel().tolist()
        # q(x) = p(x) |down(x)| / |set|: a signed mixture of uniform box distributions
        idx = np.argwhere(p != 0)
        sizes = np.array([np.prod([i + 1 for i in x]) for x in idx])
        qv = (p[p != 0] * sizes / ind.sum()).ravel().tolist()
        out.update({"support": len(pv), "n_positive": sum(1 for x in pv if x > 0),
                    "n_negative": sum(1 for x in pv if x < 0), "values_p": sorted({round(x, 9) for x in pv}),
                    "N_p": neg(pv), "re_h_p_bits": re_h(pv) / LN2, "im_h_p": im_h(pv), "M_p_bits": mana(pv) / LN2,
                    "sum_q": float(sum(qv)), "N_q": neg(qv), "re_h_q_bits": re_h(qv) / LN2, "im_h_q": im_h(qv),
                    "M_q_bits": mana(qv) / LN2,
                    "uniform_re_h_bits": math.log2(ind.sum()),
                    "A3_bits_per_cell": measure.method_bits()["bits_per_cell"]})
        if vectors:
            out.update({"p_vector": [float(x) for x in pv], "q_vector": [float(x) for x in qv]})
    return out


# ============================================================================ (6) literature (READ at source this pass)

LITERATURE = [
    ("2310.19296v1", "Cerf, Hertz, Van Herstraeten, Complex-valued Wigner entropy of a quantum state", "READ",
     "p.5 eqs.(28)-(31) principal-branch complex Wigner entropy, h_i = pi(|W|-W)/2 integrated; p.5 real-valued "
     "extensions not concave; p.6 eq.(32) h_i = pi Vol_-; p.6-7 Property 3 Re additive (uses normalisation), "
     "Property 4 Im superadditive, Delta = (2/pi) h_i(W1) h_i(W2); p.7 fn.4 Vol_-(W) = Vol_+Vol_- + Vol_-Vol_+; "
     "p.8 eq.(49) thermal h_c = ln pi + 1 + ln(1+2 nu); p.8 Re h_c below ln pi + 1 for some Wigner-negative states; "
     "p.13 fn.7 branch choice and e^{h_c}.  CONTINUOUS variables only."),
    ("2512.03505v1", "Park, Jeong, Complex Wigner entropy and Fisher control of negativity in an oval billiard", "READ",
     "p.1-4: applies the complex Wigner entropy, h_i = pi N, to billiard modes; continuous."),
    ("2410.15976v5", "Brandenburger, La Mura, Axiomatization of Renyi entropy on quantum phase space", "READ",
     "p.3-4 Axioms 0, 2', 3, 4, 5' for signed finite measures; Theorem 1 p.4 signed Renyi eq.(10); "
     "p.4 Example 1: |p|-weighted signed Shannon eq.(11) fails extensivity (-2, -12 vs -4); p.9 eq.(45) "
     "renormalised alpha=1 = -log(sum|p|/|sum p|); appendix pp.10-11 proof (Renyi-Daroczy step carried)."),
    ("2503.03759v1", "Li, Xu, Cao, Information entropy of complex probability", "READ",
     "p.9 eq.(12): -sum P log P with the complex principal log for complex-valued P; no axiomatic uniqueness."),
    ("1307.7171v1", "Veitch, Mousavian, Gottesman, Emerson, The resource theory of stabilizer computation", "READ",
     "p.10 Def.10 sum negativity sn = (sum|W| - 1)/2; p.10 eq.(2) sum|W| multiplicative; p.11 Def.12 mana "
     "M = log sum|W|, additive; p.12 Theorem 15 uniqueness of sn under monotone + negative-values-only + "
     "permutation invariance; p.15 Fig.4 qutrit strange state sn = 1/3; odd prime d (p.3)."),
    ("1201.1256v4", "Veitch, Ferrie, Gross, Emerson, Negative quasi-probability as a resource for quantum computation",
     "READ", "p.1-2: Wigner negativity (odd d, Gross's function) necessary for speed-up / magic-state distillation."),
    ("quant-ph/0401155v6", "Gibbons, Hoffman, Wootters, Discrete phase space based on finite fields", "READ",
     "p.23 eqs.(45)-(47) line sums = Born probabilities; p.27 eq.(55) W = (1/N)[sum_{lines through a} P - 1]; "
     "p.28 N^{N+1} quantum nets; p.30-31 qubit: two equivalence classes, one similarity class; p.33 qutrit: two "
     "similarity classes; p.38 eq.(73) tensor-product A for N = 4."),
    ("quant-ph/0602001v3", "Gross, Hudson's theorem for finite-dimensional quantum systems", "READ",
     "p.1-2 Theorem 2: odd d, pure state W >= 0 iff stabilizer; p.5 eq.(15), Thm 6.5 A(0) = parity; p.10 eq.(24) "
     "antisymmetric qutrit state, W(0) = (1/2)(1/3 - 1) = -1/3."),
    ("quant-ph/0406015v1", "Kenfack, Zyczkowski, Negativity of the Wigner function as an indicator of nonclassicality",
     "READ", "p.2 eq.(2.2) delta = int|W| - 1 = twice the negative volume; p.7 eq.(4.11) delta(|1>) = 4 e^{-1/2} - 2."),
    ("quant-ph/0511044v2", "Lvovsky, Raymer, Continuous-variable optical quantum state tomography (review)", "READ",
     "p.3 Smithey et al. 1993 first OHT, squeezed state, inverse Radon; p.6 eq.(17) marginals = projections of W; "
     "p.7 eqs.(19)-(21) filtered back-projection, low-pass cutoff; p.9 FBP ripples, MaxLik preferred; p.17-18 "
     "Lvovsky et al. 2001 single photon, W negative near origin at efficiency > 0.5 (0.55, later 0.62)."),
    ("1106.1791v3", "Baez, Fritz, Leinster, A characterization of entropy in terms of information loss", "READ",
     "p.3 Def.1 FinProb (measures nonnegative, p.3); p.4 Theorem 2 and the continuity definition; p.5 Cor.4 "
     "FinMeas; p.7-8 Faddeev, Thms 5-6 (I >= 0); p.9 proof."),
    ("Smithey, Beck, Raymer, Faridani, PRL 70, 1244 (1993)", "first optical homodyne tomography", "NAMED-NOT-READ",
     "not on arXiv; what it did is READ only through quant-ph/0511044v2 p.3 (squeezed state; Gaussian, W >= 0)."),
    ("Wootters, Ann. Phys. 176, 1 (1987)", "original discrete Wigner function", "NAMED-NOT-READ",
     "not on arXiv; its qubit form is READ through quant-ph/0401155v6 p.31."),
    ("Renyi 1961; Daroczy 1963", "mean-value characterisation", "NAMED-NOT-READ",
     "restated in 2410.15976v5 p.3; carries H-RD."),
    ("Lvovsky et al., PRL 87, 050402 (2001)", "single-photon OHT with negative W", "NAMED-NOT-READ",
     "READ only through quant-ph/0511044v2 p.17-18."),
]


# ============================================================================ build / report

def build():
    rng = random.Random(20261003)
    R = {}
    p0 = [1.5, -0.5]
    R["example"] = {"p": p0, "H": [H(p0).real, H(p0).imag], "re_h_nats": re_h(p0), "re_h_bits": re_h(p0) / LN2,
                    "im_h": im_h(p0), "N": neg(p0), "M": mana(p0)}
    R["multiaxis"] = multiaxis_table(p0)
    R["branch_grid"] = branch_grid(p0)
    p3 = [0.7, 0.45, -0.15]
    R["multiaxis_3"] = multiaxis_table(p3)
    R["uniform_shift"] = [{"k": k, "dIm": H(p3, [k] * 3).imag - H(p3).imag} for k in (-2, -1, 1, 2)]
    R["n_sweep"] = n_sweep()
    R["additivity_numeric"] = additivity_numeric(rng)
    R["additivity_exact"] = additivity_exact()
    R["additivity_unnormalised_control"] = additivity_unnormalised_control(rng)
    R["range_table"] = range_table()
    R["max_floor"] = {n: max_reh_floor(n) for n in (3, 4, 5, 8, 16)}
    R["bounds_random_worst_excess"] = bounds_random_search(rng)
    names, Rc = convex_residual_matrix(rng)
    bc, sc = null_space(Rc)
    names2, Rp = product_residual_matrix(rng)
    bp, sp_ = null_space(Rp)
    R["dictionary"] = names
    R["convex_null"] = describe_null(names, bc)
    R["product_null"] = describe_null(names2, bp)
    bb, _ = null_space(np.vstack([Rc, Rp]))
    R["convex_and_product_null"] = describe_null(names, bb)
    R["continuity"] = {nm: {"along_sequence": continuity_check(DICT[nm]),
                            "zero_crossing_jump": zero_crossing_continuity(DICT[nm])}
                       for nm in names}
    R["continuity"]["re_h"] = {"along_sequence": continuity_check(re_h), "zero_crossing_jump": zero_crossing_continuity(re_h)}
    R["codomain"] = bfl_codomain_counterexamples()
    R["nonneg_random_min"] = {"re_h": nonneg_random(re_h, rng), "im_h": nonneg_random(im_h, rng),
                              "M": nonneg_random(mana, rng)}
    R["convex_counterexample_M"] = convex_counterexample_M()
    R["blm"] = blm_checks()
    R["blm_signed_mean_value_worst"] = signed_mean_value_random(rng)
    R["blm_extensivity_worst"] = blm_extensivity_random(rng)
    R["fbp"] = [fbp_metrics("sup01", 180), fbp_metrics("sup01", 2), fbp_metrics("sup01", 12),
                fbp_metrics("vac", 180), fbp_metrics("vac", 3), fbp_metrics("fock1", 180)]
    R["fbp_finite_sample"] = fbp_finite_sample()
    R["continuous_h"] = [continuous_complex_entropy("vac"), continuous_complex_entropy("fock1"),
                         continuous_complex_entropy("sup01")]
    import sympy as sp
    rho_q = bloch_rho([-1 / sp.sqrt(3)] * 3)
    okq, Pq, Wq = triangulate_exact(rho_q, qubit_A(+1), 2)
    Wq_direct = wigner_discrete(rho_q, qubit_A(+1), 2)
    rho_t = qutrit_strange_rho()
    okt, Pt, Wt = triangulate_exact(rho_t, qutrit_A(), 3)
    Wt_direct = wigner_discrete(rho_t, qutrit_A(), 3)
    R["exact_qubit"] = {"projectors_ok": okq, "P_lines": sorted(str(v) for v in Pq.values()),
                        "P_min": min(float(v) for v in Pq.values()),
                        "W_reconstructed": {str(k): str(v) for k, v in Wq.items()},
                        "W_direct": {str(k): str(v) for k, v in Wq_direct.items()},
                        "agree": all(sp.simplify(Wq[k] - Wq_direct[k]) == 0 for k in Wq)}
    pv_t = [float(Wt_direct[k]) for k in sorted(Wt_direct)]
    R["exact_qutrit"] = {"projectors_ok": okt, "P_lines": sorted(str(v) for v in Pt.values()),
                         "P_min": min(float(v) for v in Pt.values()),
                         "W_reconstructed": {str(k): str(v) for k, v in Wt.items()},
                         "W_direct": {str(k): str(v) for k, v in Wt_direct.items()},
                         "agree": all(sp.simplify(Wt[k] - Wt_direct[k]) == 0 for k in Wt),
                         "N": neg(pv_t), "M_nats": mana(pv_t), "re_h_nats": re_h(pv_t),
                         "re_h_exact": str(sp.nsimplify(sp.Rational(4, 3) * sp.log(6) - sp.Rational(1, 3) * sp.log(3)))}
    R["striation_control"] = striation_control_numeric()
    R["app_qubit"] = app_qubit()
    R["app_bell"] = app_bell()
    with contextlib.redirect_stdout(io.StringIO()):
        R["app_lambda"] = lambda_mobius()
        R["app_lambda_box_control"] = lambda_mobius(control_box=True)
    R["literature"] = [{"id": a, "title": b, "status": c, "used": d} for a, b, c, d in LITERATURE]
    return R


def report(R):
    f = lambda x: f"{x:.6f}" if isinstance(x, float) else str(x)
    print("Q-1s -- signed / complex entropy (signed.py).  Not seated.\n")
    e = R["example"]
    print(f"(1) p = {e['p']}: H = {e['H'][0]:.6f} + {e['H'][1]:.6f} i nats; Re H = {e['re_h_bits']:.6f} bits; "
          f"N = {e['N']}; M = {e['M']:.6f} nats")
    print("    multi-axis table, p = (1.5, -0.5)  [i, p, |p|, ln|p|, arg, arg_reflected, Re-contrib, Im-contrib, "
          "-Log p (re, im), Im step per k]")
    for r in R["multiaxis"]:
        print("     ", r["i"], f(r["p"]), f(r["abs"]), f(r["ln_abs"]), f(r["arg_principal"]), f(r["arg_reflected"]),
              f(r["re_contrib"]), f(r["im_contrib"]), f(r["inverse_axis_re"]), f(r["inverse_axis_im"]),
              f(r["branch_step_im"]))
    print("    branch grid (k_pos, k_neg) -> Re H, Im H, |H|, arg H, e^H  [Re H is branch-free]")
    for r in R["branch_grid"]:
        print(f"      {r['ks']}: {r['re']:.6f} {r['im']:+.6f} {r['abs']:.6f} {r['arg']:+.6f} "
              f"({r['exp_re']:+.6f}{r['exp_im']:+.6f}i)")
    print("    uniform shift k on all three entries of (0.7, 0.45, -0.15): dIm =",
          [f"{u['k']}: {u['dIm']:+.6f}" for u in R["uniform_shift"]], "(= -2 pi k)")
    print("    N-sweep p = (1+N, -N): N, Re H, Im H, -Im H (reflection), M")
    for r in R["n_sweep"]:
        print(f"      {r['N']:.2f}  {r['re']:+.6f}  {r['im']:.6f}  {r['im_reflected']:+.6f}  {r['M']:.6f}")
    a = R["additivity_numeric"]
    print(f"\n(2) products (400 random): |Re residual| <= {a['re']:.1e}; |Im - pi(N_p P_q + P_p N_q)| <= "
          f"{a['im_formula']:.1e}; |M residual| <= {a['M']:.1e}; N identity {a['N_identity']:.1e}; "
          f"min(Im excess - 2 pi N_p N_q) = {a['im_superadd_min']:.1e}")
    print("    exact (sympy, (1+a,-a) x (1+b,-b)):", R["additivity_exact"])
    print(f"    CONTROL sum p = 2: Re H additivity residual = {R['additivity_unnormalised_control']:.4f} (must be > 0)")
    print("\n(3) range of Re H (nats) for n entries, negativity N:")
    for r in R["range_table"]:
        print(f"      n={r['n']} N={r['N']:<5} [{r['min_nats']:+.6f}, {r['max_nats']:+.6f}]  negative possible "
              f"{r['negative_possible']}, forced {r['negative_forced']}")
    print("    Re H < 0 is FORCED only for n = 2.  For n >= 3, min over N of max Re H = ln(n-2) at N = 1/(n-2):",
          {k: (round(v["N_at_min"], 6), round(v["min_of_max"], 6), round(v["closed_form_min"], 6))
           for k, v in R["max_floor"].items()})
    print(f"    random search: worst excursion outside the bounds = {R['bounds_random_worst_excess']:.2e} (<= 0 holds)")
    print("\n(4) BFL Theorem 2 on signed measures (H-FINSIGNED); dictionary =", R["dictionary"])
    print("    convex-linear null space:", R["convex_null"])
    print("    product-additive null space:", R["product_null"])
    print("    both:", R["convex_and_product_null"])
    print("    codomain counterexamples:", R["codomain"])
    print("    min F over random morphisms (>= 0 required):", R["nonneg_random_min"])
    print("    M convex-linearity counterexample:", R["convex_counterexample_M"])
    print("    continuity (zero-crossing jump):", {k: f"{v['zero_crossing_jump']:.1e}" for k, v in R["continuity"].items()})
    print("    Brandenburger-La Mura:", R["blm"])
    print(f"    Re H signed-weight mean-value worst {R['blm_signed_mean_value_worst']:.1e}; "
          f"extensivity worst {R['blm_extensivity_worst']:.1e}")
    print("\n(5) triangulation")
    for m in R["fbp"]:
        print(f"    FBP {m['state']:>5} K={m['K']:>3}: max|err| {m['max_abs_err']:.4f}, exact min {m['exact_min']:+.5f} "
              f"at {m['exact_argmin']}, recon min {m['recon_min']:+.5f} at {m['recon_argmin']}, IoU(neg) "
              f"{m['neg_region_iou']:.3f}, marginals min {m['marginals_min']:.2e}")
    print("    finite-sample FBP:", R["fbp_finite_sample"])
    print("    continuous complex Wigner entropy:", R["continuous_h"])
    for key in ("exact_qubit", "exact_qutrit"):
        x = R[key]
        print(f"    {key}: projectors {x['projectors_ok']}, min P(line) {x['P_min']:.6f}, reconstruction agrees "
              f"{x['agree']}, W = {x['W_reconstructed']}")
    print("    qutrit strange state: N, M, Re H =", R["exact_qutrit"]["N"], R["exact_qutrit"]["M_nats"],
          R["exact_qutrit"]["re_h_nats"], R["exact_qutrit"]["re_h_exact"])
    print("    CONTROL d striations:", R["striation_control"])
    print("\n(7) applications")
    print("    (a) qubit:", R["app_qubit"])
    print("    (b) Bell (measure.BELL):", R["app_bell"])
    print("    (c) Lambda (H-MOBIUS-WEIGHT):", R["app_lambda"])
    print("        box control:", {k: R["app_lambda_box_control"][k] for k in ("N_p", "support", "n_negative")})
    print("\n(6) literature:")
    for L in R["literature"]:
        print(f"    [{L['status']}] {L['id']}: {L['title']}")


def selftest():
    R = build()
    res = []

    def chk(name, ok, detail="", control=False, structural=False):
        res.append((name, bool(ok), control and not structural, structural))
        tag = "[STRUCTURAL: cannot fail, not evidence] " if structural else ("[CONTROL] " if control else "")
        print(f"  {'ok  ' if ok else 'FAIL'} {tag}{name}  {detail}")

    e = R["example"]
    print("(1) complex entropy")
    chk("Re H(1.5,-0.5) = -0.954771 nats (charter -0.95; task -0.9548)", abs(e["re_h_nats"] + 0.9547712) < 1e-6,
        f"{e['re_h_nats']:.7f}")
    chk("Im H = pi N on the principal branch", abs(e["H"][1] - PI * 0.5) < 1e-12, f"{e['H'][1]:.6f}")
    chk("Re H identical on every branch of the grid", max(abs(r["re"] - e["re_h_nats"]) for r in R["branch_grid"]) < 1e-12)
    g = {r["ks"]: r["im"] for r in R["branch_grid"]}
    chk("branch k on the NEGATIVE entry shifts Im H by -2 pi k p = +pi k (k=1), NOT 2 pi (D1)",
        abs(g[(0, 1)] - g[(0, 0)] - PI) < 1e-12 and abs(g[(0, 1)] - g[(0, 0)] - 2 * PI) > 1, f"{g[(0, 1)] - g[(0, 0)]:.6f}")
    chk("uniform branch shift k gives dIm = -2 pi k exactly (sum p = 1)",
        all(abs(u["dIm"] + 2 * PI * u["k"]) < 1e-12 for u in R["uniform_shift"]))
    chk("e^H changes under a per-entry branch (k_neg = 1 flips its sign for N = 0.5)",
        abs(complex(*[[r["exp_re"], r["exp_im"]] for r in R["branch_grid"] if r["ks"] == (0, 1)][0])
            + complex(*[[r["exp_re"], r["exp_im"]] for r in R["branch_grid"] if r["ks"] == (0, 0)][0])) < 1e-12,
        "e^{H} is branch-invariant only for uniform shifts", control=True)
    print("(2) products")
    a = R["additivity_numeric"]
    chk("Re H additive on products", a["re"] < 1e-11, f"{a['re']:.1e}")
    chk("Im H = pi(N_p P_q + P_p N_q)", a["im_formula"] < 1e-11, f"{a['im_formula']:.1e}")
    chk("Im H superadditive by exactly 2 pi N_p N_q", abs(a["im_superadd_min"]) < 1e-11)
    chk("the hypothesis 'Im H additive' is REJECTED: excess > 0 in every sample", a["im_excess_min"] > 1e-6,
        f"min excess {a['im_excess_min']:.2e}", control=True)
    chk("M additive", a["M"] < 1e-11, f"{a['M']:.1e}")
    chk("N = (sum|p| - 1)/2", a["N_identity"] < 1e-12)
    ex = R["additivity_exact"]
    chk("sympy exact: Re residual 0, Im formula 0, M residual 0", ex["re_residual"] == "0" and
        ex["im_formula_residual"] == "0" and ex["M_residual"] == "0", str(ex))
    chk("Re H additivity FAILS when sum p = 2", R["additivity_unnormalised_control"] > 1e-3,
        f"{R['additivity_unnormalised_control']:.4f}", control=True)
    chk("M = 0 for a probability vector and > 0 with a negative entry", mana([0.2, 0.8]) == 0.0 and mana([1.1, -0.1]) > 0)
    print("(3) where Re H < 0")
    lo, hi = reh_bounds(2, 0.5)
    chk("n = 2 bounds collapse to the single value at (1.5,-0.5)", abs(lo - hi) < 1e-12 and abs(lo + 0.9547712) < 1e-6)
    chk("random search never leaves the exact range (can fail)", R["bounds_random_worst_excess"] <= 1e-12,
        f"{R['bounds_random_worst_excess']:.2e}")
    ok_att = all(abs(re_h(reh_extremals(n, N)[0]) - reh_bounds(n, N)[0]) < 1e-12 and
                 abs(re_h(reh_extremals(n, N)[1]) - reh_bounds(n, N)[1]) < 1e-12
                 for n in (2, 3, 5) for N in (0.1, 1.0))
    chk("both bounds attained by the extremal constructions", ok_att)
    chk("a wrong bound (max reduced by 1e-3) IS violated by its own extremal",
        re_h(reh_extremals(4, 0.5)[1]) > reh_bounds(4, 0.5)[1] - 1e-3, control=True)
    mf_ = R["max_floor"]
    chk("min over N of max Re H = ln(n-2) at N = 1/(n-2) (golden-section search vs closed form)",
        all(abs(v["min_of_max"] - v["closed_form_min"]) < 1e-9 and abs(v["N_at_min"] - v["closed_form_N"]) < 1e-5
            for v in mf_.values()), str({k: round(v["min_of_max"], 6) for k, v in mf_.items()}))
    chk("min Re H < 0 for every (n, N > 0) in the table: negativity always PERMITS Re H < 0",
        all(r["negative_possible"] for r in R["range_table"]))
    chk("Re H < 0 FORCED exactly in the n = 2 rows", all(r["negative_forced"] == (r["n"] == 2) for r in R["range_table"]))
    print("(4) BFL on signed measures; Brandenburger-La Mura")
    chk("functoriality of any F = X(p) - X(q)", True, "a difference of a state function telescopes", structural=True)
    cn = R["convex_null"]
    chk("convex-linear null space = span{h_plus + J (= Re H), N}",
        len(cn) == 2 and any(set(v) == {"h_plus", "J"} and abs(v["h_plus"] - v["J"]) < 1e-6 for v in cn)
        and any(set(v) == {"N"} for v in cn), str(cn))
    pn = R["product_null"]
    chk("product-additive null space = span{Re H, M, hartley, renyi2_signed}; N is NOT in it",
        len(pn) == 4 and any(set(v) == {"h_plus", "J"} for v in pn) and any(set(v) == {"M"} for v in pn)
        and any(set(v) == {"hartley"} for v in pn) and any(set(v) == {"renyi2_signed"} for v in pn), str(pn))
    bn = R["convex_and_product_null"]
    chk("convex-linear AND product-additive: Re H only (in the dictionary)",
        len(bn) == 1 and set(bn[0]) == {"h_plus", "J"}, str(bn))
    cd = R["codomain"]
    chk("Re H fails BFL's codomain [0,inf): crush of (1.5,-0.5) gives F < 0", cd["crush_(1.5,-0.5)"]["F_reH"] < 0, control=True)
    mn = cd["merge_negatives"]
    chk("merging negatives: F_ReH = -(b+c) ln 2 < 0 with N unchanged (so no a ReH + b N is >= 0 unless a = 0)",
        abs(mn["F_reH"] - mn["predicted_F_reH"]) < 1e-12 and abs(mn["F_imH"]) < 1e-12)
    nr = R["nonneg_random_min"]
    chk("Im H and M: F >= 0 on 600 random signed morphisms", nr["im_h"] >= -1e-12 and nr["M"] >= -1e-12, str(nr))
    chk("Re H: F < 0 found among random signed morphisms", nr["re_h"] < 0, f"{nr['re_h']:.4f}", control=True)
    chk("M fails convex linearity (computed counterexample)", abs(R["convex_counterexample_M"]["gap"]) > 1e-3,
        str(R["convex_counterexample_M"]))
    ct = R["continuity"]
    chk("Re H, N, M continuous through a zero crossing", all(ct[k]["zero_crossing_jump"] < 1e-6 for k in ("re_h", "N", "M")))
    chk("count_neg and hartley jump at a zero crossing", ct["count_neg"]["zero_crossing_jump"] > 0.5 and
        ct["hartley"]["zero_crossing_jump"] > 0.1, control=True)
    b = R["blm"]
    chk("BLM Example 1 reproduced (READ p.4: -2 and -12)", abs(b["example1_abs_P"] + 2) < 1e-12 and
        abs(b["example1_abs_PQ"] + 12) < 1e-12)
    chk("Re H on the same measures is extensive: -2 + -2 = -4", abs(b["reH_P"] + 2) < 1e-12 and abs(b["reH_PQ"] + 4) < 1e-12)
    chk("Re H extensive on random signed measures (BLM Axiom 4)", R["blm_extensivity_worst"] < 1e-11)
    chk("calibration H((1/2)) = 1 bit (Axiom 3)", abs(b["calibration_H((1/2))"] - 1) < 1e-12)
    chk("Re H FAILS Axiom 5' (|w| weights, affine g): union != |w|-mean", abs(b["mv_union"] - b["mv_abs_weights"]) > 0.5,
        f"{b['mv_union']:.4f} vs {b['mv_abs_weights']:.4f}", control=True)
    chk("Re H SATISFIES the signed-weight mean-value rule (affine g)", abs(b["mv_union"] - b["mv_signed_weights"]) < 1e-12
        and R["blm_signed_mean_value_worst"] < 1e-10)
    chk("Re H is not a signed Renyi entropy for any alpha in (0.05, 6)", b["closest_signed_renyi_maxgap_bits"] > 0.05,
        f"closest alpha {b['closest_signed_renyi_alpha']}, gap {b['closest_signed_renyi_maxgap_bits']:.3f} bits")
    chk("signed-weight exponential branch violates Axiom 0 for every tested alpha",
        all(v < 0 for v in b["axiom0"].values()), str({k: round(v, 4) for k, v in b["axiom0"].items()}))
    chk("BLM eq.(45) = -M (bits) when sum p = 1", abs(b["renorm1_vs_minus_M_bits"]) < 1e-12, structural=True)
    print("(5) triangulation")
    F = {(m["state"], m["K"]): m for m in R["fbp"]}
    m = F[("sup01", 180)]
    chk("marginals are non-negative (Born densities)", m["marginals_min"] >= 0)
    chk("FBP K=180 recovers W of (|0>+|1>)/sqrt2: max|err| < 0.01", m["max_abs_err"] < 0.01, f"{m['max_abs_err']:.4f}")
    chk("FBP K=180 recovers the negative region (IoU > 0.9) and its minimum within 0.01",
        m["neg_region_iou"] > 0.9 and abs(m["recon_min"] - m["exact_min"]) < 0.01,
        f"IoU {m['neg_region_iou']:.3f}, min {m['recon_min']:+.4f} vs {m['exact_min']:+.4f}")
    m2 = F[("sup01", 2)]
    chk("K=2 angles FAILS (max|err| > 0.05 or IoU < 0.5)", m2["max_abs_err"] > 0.05 or m2["neg_region_iou"] < 0.5,
        f"err {m2['max_abs_err']:.3f}, IoU {m2['neg_region_iou']:.3f}", control=True)
    mv = F[("vac", 180)]
    chk("vacuum (W >= 0) reconstructs non-negative at K=180 (min > -1e-3)", mv["recon_min"] > -1e-3, f"{mv['recon_min']:.2e}")
    mv3 = F[("vac", 3)]
    chk("the non-negativity test CAN fail: vacuum at K=3 shows min < -1e-3", mv3["recon_min"] < -1e-3,
        f"{mv3['recon_min']:.3e}", control=True)
    mf = F[("fock1", 180)]
    chk("Fock |1>: FBP minimum -1/pi at the origin within 0.01", abs(mf["recon_min"] + 1 / PI) < 0.01, f"{mf['recon_min']:.4f}")
    fs = R["fbp_finite_sample"]
    chk("finite sample (72 angles x 20000): negativity still recovered (patch mean < 0)",
        fs["recon_at_exact_min_patch"] < 0, f"{fs['recon_at_exact_min_patch']:+.4f} +/- {fs['recon_patch_std']:.4f} "
                                            f"(exact {fs['exact_min']:+.4f})")
    ch = {c["state"]: c for c in R["continuous_h"]}
    chk("vacuum Re h_c = ln pi + 1 (2310.19296v1 eq.49 p.8, READ)", abs(ch["vac"]["re_h"] - (math.log(PI) + 1)) < 1e-6,
        f"{ch['vac']['re_h']:.7f} vs {math.log(PI) + 1:.7f}")
    chk("Fock |1> Im h_c = pi delta/2, delta = 4e^{-1/2} - 2 (quant-ph/0406015v1 eq.4.11 p.7, READ)",
        abs(ch["fock1"]["im_h"] - PI * (4 * math.exp(-0.5) - 2) / 2) < 1e-4,
        f"{ch['fock1']['im_h']:.6f} vs {PI * (4 * math.exp(-0.5) - 2) / 2:.6f}")
    q = R["exact_qubit"]
    chk("qubit: line operators are rank-1 projectors; Born P(line) >= 0", q["projectors_ok"] and q["P_min"] >= 0)
    chk("qubit: GHW eq.(55) reconstruction == Tr(rho A)/2 exactly, incl. W(0,0) = (1 - sqrt3)/4",
        q["agree"] and q["W_reconstructed"]["(0, 0)"] in ("1/4 - sqrt(3)/4", "-sqrt(3)/4 + 1/4"), q["W_reconstructed"]["(0, 0)"])
    t = R["exact_qutrit"]
    chk("qutrit: line operators are rank-1 projectors; Born P(line) >= 0", t["projectors_ok"] and t["P_min"] >= 0)
    chk("qutrit strange state: positive marginals give W(0,0) = -1/3 exactly", t["agree"] and t["W_reconstructed"]["(0, 0)"] == "-1/3")
    chk("qutrit: N = 1/3 (sum negativity, 1307.7171v1 p.15 Fig.4, READ), M = ln 5/3",
        abs(t["N"] - 1 / 3) < 1e-12 and abs(t["M_nats"] - math.log(5 / 3)) < 1e-12)
    sc = R["striation_control"]
    chk("3 of 4 striations: rank 7 < 9; a second state shares every kept marginal and differs at the origin",
        sc["rank_kept"] == 7 and sc["rank_all_striations"] == 9 and sc["kept_marginal_gap"] < 1e-12 and
        sc["rho2_min_eig"] >= -1e-12 and abs(sc["W_origin_rho"] - sc["W_origin_rho2"]) > 1e-3 and sc["dropped_striation_gap"] > 1e-4,
        f"W(0,0): {sc['W_origin_rho']:+.4f} vs {sc['W_origin_rho2']:+.4f}", control=True)
    print("(7) applications")
    aq = R["app_qubit"]
    chk("qubit (-1,-1,-1)/sqrt3: negative under net +1, NOT under net -1 (H-QUBIT-NET matters)",
        aq["net_sy=+1"]["N"] > 0.18 and aq["net_sy=-1"]["N"] == 0, f"N = {aq['net_sy=+1']['N']:.6f} / {aq['net_sy=-1']['N']}",
        control=True)
    chk("max pure-state negativity on the grid ~ (sqrt3-1)/4", abs(aq["max_N_pure_net+1"]["N"] - (math.sqrt(3) - 1) / 4) < 1e-3)
    ab = R["app_bell"]
    chk("Bell pair: 12 entries +1/8, 4 entries -1/8; N = 1/2; Re H = 3 bits; M = 1 bit",
        ab["count_negative"] == 4 and abs(ab["N"] - 0.5) < 1e-12 and abs(ab["re_h_bits"] - 3) < 1e-12 and
        abs(ab["M_bits"] - 1) < 1e-12, str(ab["values"]))
    al = R["app_lambda"]
    chk("Lambda imported: 976 cells, box 6912 = product of alphabet sizes", al["cells_imported"] == 976 and
        al["box_imported"] == 6912 and al["box_from_shape"] == 6912)
    chk("Mobius reconstruction of Lambda's indicator is exact; sum p = 1 (bottom cell admitted)",
        al["reconstruction_max_err"] == 0 and al["sum_p"] == 1.0 and al["bottom_in_set"])
    chk("uniform measure on Lambda: Re H = log2 976 = A3's 9.930737 bits", abs(al["uniform_re_h_bits"] - al["A3_bits_per_cell"]) < 1e-12)
    chk("the Mobius weighting of Lambda is signed (N > 0)", al["N_p"] > 0, f"N_p = {al['N_p']:.4f}")
    ac = R["app_lambda_box_control"]
    chk("a full box has a one-point Mobius weight, N = 0", ac["support"] == 1 and ac["N_p"] == 0, control=True)
    n_ctrl = sum(1 for r in res if r[2])
    n_struct = sum(1 for r in res if r[3])
    n_fail = sum(1 for r in res if not r[1])
    print(f"\n{len(res)} checks, {n_fail} failed; {n_ctrl} controls; {n_struct} STRUCTURAL (not evidence)")
    return n_fail == 0, R


def to_jsonable(o):
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, complex):
        return [o.real, o.imag]
    return o


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        ok, _ = selftest()
        sys.exit(0 if ok else 1)
    R = build()
    if "--json" in sys.argv:
        print(json.dumps(to_jsonable(R), indent=1))
    else:
        report(R)
