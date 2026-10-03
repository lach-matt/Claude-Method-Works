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
  (4b) (R3-alone, 2026-10-03) over EVERY continuous SEPARABLE functional X = sum g(p_i) (H-SEPARABLE): functoriality +
      convex linearity (lambda in [0,1]) + continuity force X = c Re H + b N, step by step -- the algebraic steps
      machine-checked by z3 over an uninterpreted g (vacuity and encoding guards run, controls built to fail), the
      solution identity and the product step by sympy, the two analytic lemmas (Cauchy under continuity) DERIVED and
      READ as cited.  Consequences: codomain kept => only b N (b >= 0); product additivity => Re H alone.
      Kontsevich's appendix to math/0008089v1 (READ pp.42-44): his (A), (B), (C) hold for Re H on two entries over
      all of R, and he CLAIMS (p.43, cohomological sketch) that H_inf = Re H on (x, 1-x) is their unique continuous
      solution; the signed-weight chain rule holds for Re H; N fails both (control).  A counterexample to the
      uniqueness of M (g3, V2-0) and the census of signed measures that convex linearity cannot reach.
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

  (8) (M-apply, 2026-10-03; M item 2 "Carry both") BOTH mean-value weightings carried, each with the functional it
      selects and every axiom computed for it: SIGNED w -> Re H (A0, A2', A3, A4, A5'(w) hold; A5'(|w|) fails; keeps
      BFL convex linearity on FinProb), |w| -> signed Renyi H_alpha (A0, A2', A3, A4, A5'(|w|) hold, BLM Theorem 1
      READ; A5'(w) fails; on probabilities it is Renyi, not BFL's Shannon).  Neither is preferred here.
  (9) (M-apply; M items 3 and 6) the GROUND-STATE CALIBRATION.  Default MASS/BINDING: a state's mass budget over
      protons, electrons, neutrons and the (negative) binding, from READ AME2020 / PDG / NIST values; the ground is the
      neutral atom.  Selectable: GROUND-CONFIG (LW1-ground.py via populate) and IONISATION (NIST ladder; populate's
      banked limits reported).  ONE multi-axis table centred at the ground carries all four inverses and reflections
      (log branches of p/p0; conjugate and reciprocal; fold to |p|; Radon inverse).  TESTED, not assumed: the signed
      relative entropy D_s(p||p0) = sum p Log(p/p0) is 0 at the ground (STRUCTURAL) and meets product additivity (Re),
      convex linearity and the chain rule, and FAILS Gibbs non-negativity and data processing; the entropy deviation
      Re H(p) - Re H(p0) is NOT a relative entropy unless the cross term sum (p - p0) ln|p0| vanishes.  Applied to
      Fe-56 and its ions, C-12+, the proton, and The Method's index under H-INDEX-GROUND-BOX / -LAMBDA.

NAMED HYPOTHESES (every limitation is one)
  H-PRINCIPAL   principal branch, arg in (-pi, pi], arg(negative) = +pi (2310.19296v1 p.5 convention).
  H-READING-M   "inverses and reflections" is READ here as: the branch lattice, the conjugate branch (arg = -pi,
                Im -> -Im) and the inverse axis -Log p (surprisal).  M's meaning is ASKED, not presumed.
  H-NORM        sum p = 1.  Re H additivity depends on it (control).
  H-FINSIGNED   BFL's category with signed measures of total 1, measure-preserving functions, lambda in [0,1].
  H-DICTIONARY  the 12-functional lawful-family results hold only inside the 12 listed functionals.
  H-SEPARABLE   (4b) X(p) = sum_i g(p_i) with g: R -> R continuous.  Under it the lawful family is span{Re H, N}
                (derived and machine-checked).  Over NON-separable continuous functionals uniqueness is OPEN; it is
                not even constrained on a convex atom (a signed measure with no split into blocks of totals in (0,1)).
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
  (M-apply, 2026-10-03)
  H-READING-M is ANSWERED by M (item 3): "All of the above" -- all four readings are carried, centred at the ground.
  H-CAL          which calibration a use takes; named at every use (default MASS/BINDING, M item 6).
  H-MASS-CELLS   a state's mass budget written over four cells (Z m_p, (Z-q) m_e, N m_n, -B); B the shortfall.
  H-AME-ATOMIC   AME2020's masses are neutral-atom ground-state masses (the table's own convention, header READ).
  H-IE-GROUND    NIST's ionisation energies are ground-to-ground, so M_ion = M_atom - q m_e + sum of the first q.
  H-ISOELECTRONIC (GROUND-CONFIG) an ion's configuration is its isoelectronic neutral's -- populate's mapping,
                 RECONSTRUCTED there and here.
  H-LADDER-CELLS (IONISATION) the cells are the electrons in removal order, weighted by each ionisation energy.
  H-RADON-PAD    the Radon column lays cells row-major on Z_d^2 (d prime) and pads with zeros.
  H-INDEX-GROUND-BOX / H-INDEX-GROUND-LAMBDA  The Method's index has no periodic-table ground: the uniform measure on
                 the 6,912-cell box, or on Lambda's 976 cells, is named as its ground.

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


# ============================================================================ (4b) separable functionals; Kontsevich
# Added by R3-alone (2026-10-03), answering the FOR verifier's V2-1 problem 5 and the AGAINST verifier's V2-0 problems
# 1, 3, 4.  THE CLAIM (H-SEPARABLE, H-FINSIGNED, H-CONT-G):  if F on FinSigned is functorial, convex-linear with
# lambda in [0,1] (BFL 1106.1791v3 p.4 eq.(2), READ) and continuous, and X(p) := F(!_p) is SEPARABLE,
# X(p) = sum_i g(p_i) with g: R -> R continuous, then X = c Re H + b N for constants c, b, and conversely.
# The steps, each with its status (Q1s-signed.md s.4b prints the same list):
#   (0) F(id) = F(id o id) = 2 F(id) => F(id) = 0; F(f: p -> q) = X(p) - X(q) because !_p = !_q o f
#       (BFL p.9 eq.(8)).  STRUCTURAL (holds for any functor into (R, +)); not counted.
#   (1) convex linearity on !_p, !_q: X(lam p (+) (1-lam) q) = X(lam, 1-lam) + lam X(p) + (1-lam) X(q).  STRUCTURAL
#       restatement of the axiom on a pair of terminal maps.
#   (2) g(1) = X(pt) = 0, and g(0) = 0 (convex linearity at lam = 1 with |q| = 2).            Z3 (z3_g0)
#   (3) phi_lam(x) := g(lam x) - lam g(x) is additive in x for every lam in (0,1): compare
#       (x, y, 1-x-y) with (x+y, 1-x-y), each convex-combined with the point.                Z3 (z3_cauchy)
#   (4) continuous + additive => phi_lam(x) = A(lam) x (Cauchy; READ as cited in 2410.15976v5 p.10 Lemma A.1, which
#       cites Aczel-Dhombres; Kontsevich math/0008089v1 p.43 takes the same step for measurable psi_lambda).  DERIVED.
#   (5) x > 0: h = g/x has h(lam x) = h(x) + B(lam), B(lam) = A(lam)/lam = g(lam)/lam; B(lam mu) = B(lam) + B(mu),
#       continuous => B = a ln lam; h(1) = 0 => g(x) = a x ln x on (0, inf).                     DERIVED
#   (6) x < 0: u(x) = h(x) - a ln|x| has u(lam x) = u(x) for all lam in (0,1) => u = beta constant on (-inf, 0)
#       => g(x) = a x ln|x| + beta x.                                                              DERIVED
#   (7) sum_i g(p_i) = -a Re H - beta N, i.e. X = c Re H + b N with c = -a, b = -beta.  The solution's identity
#       g(lam x) - lam g(x) = a lam ln(lam) x on each sign is checked in sympy.                 SYMPY (sep_sympy)
#   (8) conversely Re H and N are convex-linear (sympy on a sign pattern; numeric null space below).
#   CONSEQUENCES (each Z3 or sympy): BFL's codomain [0, inf) kept => c = 0, b >= 0 (z3_codomain); product
#   additivity => b = 0, Re H alone (sympy, N(pq) - N(p) - N(q) = 2 N_p N_q).  Shannon on FinProb does NOT fix b:
#   N vanishes on every probability measure.
# NOT CLAIMED: anything about NON-separable functionals.  Convex linearity does not reach a signed atom that has no
# split into blocks with totals in (0,1) (convex_decompositions; every n = 2 signed measure is such an atom), so the
# general uniqueness question stays OPEN (H-SEPARABLE is the named hypothesis that closes it here).

def convex_decompositions(p, tol=1e-12):
    """Splits of p into two non-empty blocks whose totals lam, 1 - lam both lie in (0, 1): exactly the ways p can be
    written lam p1 (+) (1-lam) p2 with p1, p2 of total 1 and lam in (0,1), up to the order of entries.  A block of
    total 0 cannot be normalised, and a total outside [0, 1] would need lam outside BFL's range."""
    n = len(p)
    out = []
    for mask in range(1, 2 ** (n - 1)):          # entry n-1 always in block B: each unordered split once
        A = [i for i in range(n) if mask >> i & 1]
        B = [i for i in range(n) if not mask >> i & 1]
        lam = sum(p[i] for i in A)
        if tol < lam < 1 - tol:
            out.append((tuple(A), tuple(B), lam))
    return out


def indecomposable_census(rng, trials=2000):
    """How often a random signed measure has NO convex decomposition (the region separability must cover)."""
    rows = {}
    for n in (2, 3, 4, 5):
        k = sum(1 for _ in range(trials) if not convex_decompositions(rand_quasi(rng, n)))
        rows[n] = k / trials
    return rows


def separable_nullspace(rng, rows=400):
    """COMPUTED corroboration (the FOR verifier's scratch check, rebuilt here): a 14-function separable basis
    (x ln|x|, x, x^2, x^3, x ln^2|x|, |x|^1.5, |x|^2.5, separately on positive and negative entries); 400 random
    convex-linearity rows plus X(pt) = 0.  The null space should be span{Re H, N}.  CONTROL: without the
    convex-linearity rows the null space is large (13)."""
    L = lambda x: math.log(abs(x))
    basis = [("xlnx", lambda x: -x * L(x)), ("x", lambda x: x), ("x2", lambda x: x * x), ("x3", lambda x: x ** 3),
             ("xln2", lambda x: x * L(x) ** 2), ("x15", lambda x: abs(x) ** 1.5), ("x25", lambda x: abs(x) ** 2.5)]
    cols = [(nm + s, sgn, f) for s, sgn in (("+", 1), ("-", -1)) for nm, f in basis]

    def feat(v):
        return np.array([sum(f(x) for x in v if (x > 0 if sgn > 0 else x < 0)) for _, sgn, f in cols])

    def rq():
        return rand_quasi(rng, rng.randint(2, 4))
    A = [feat([1.0])]
    for _ in range(rows):
        p, q, lam = rq(), rq(), rng.uniform(0.05, 0.95)
        A.append(feat(direct_sum(lam, p, q)) - feat([lam, 1 - lam]) - lam * feat(p) - (1 - lam) * feat(q))
    A = np.array(A)
    A = A / (np.linalg.norm(A, axis=1, keepdims=True) + 1e-300)
    _, sv, vt = np.linalg.svd(A)
    rank = int((sv > 1e-9 * sv[0]).sum())
    null = vt[rank:]
    names = [c[0] for c in cols]
    reh = np.zeros(len(cols)); reh[names.index("xlnx+")] = 1; reh[names.index("xlnx-")] = 1
    nn = np.zeros(len(cols)); nn[names.index("x-")] = -1           # N = -sum_{x<0} x
    S = np.array([reh, nn])
    out_of_span = float(np.linalg.norm(null - (null @ S.T) @ np.linalg.inv(S @ S.T) @ S)) if len(null) else 0.0
    span_out = float(np.linalg.norm(S - (S @ null.T) @ null)) if len(null) else float("inf")
    control_dim = len(cols) - int(np.linalg.matrix_rank(np.array([feat([1.0])])))
    return {"basis": names, "rows": rows, "null_dim": int(len(null)), "null_outside_span_ReH_N": out_of_span,
            "span_ReH_N_outside_null": span_out, "control_null_dim_without_CL_rows": control_dim}


def sep_sympy():
    """SYMPY: (7) the solution identity on each sign; (8) Re H convex-linear on a sign pattern (N's convex linearity
    is one line by hand: lam, 1-lam >= 0 keep every sign, and N(lam, 1-lam) = 0; it is also in the numeric null space);
    and the product step N(pq) - N(p) - N(q) = 2ab for p = (1+a, -a), q = (1+b, -b)."""
    import sympy as sp
    a, beta = sp.symbols("a beta", real=True)
    lp = sp.symbols("lp", positive=True)
    xp = sp.symbols("xp", positive=True)
    gpos = lambda t: a * t * sp.log(t)                              # t > 0
    gneg = lambda t, at: a * t * sp.log(at) + beta * t              # t < 0, at = |t|
    r_pos = sp.simplify(sp.expand_log(gpos(lp * xp) - lp * gpos(xp) - a * lp * sp.log(lp) * xp, force=True))
    r_neg = sp.simplify(sp.expand_log(gneg(-lp * xp, lp * xp) - lp * gneg(-xp, xp) - a * lp * sp.log(lp) * (-xp),
                                      force=True))
    # (8): p = (1+s, -s), q = (1+t, -t), s, t > 0, lam in (0,1); X(lam p (+) (1-lam) q) - X(lam,1-lam) - lam X(p) - ...
    s, t = sp.symbols("s t", positive=True)
    L1 = sp.symbols("L1", positive=True)                            # lam = L1/(1+L1) in (0,1)
    lm = L1 / (1 + L1)
    ent = lambda v: -sum(c * sp.log(sp.Abs(c)) for c in v)
    p, q = [1 + s, -s], [1 + t, -t]
    P = [lm * c for c in p] + [(1 - lm) * c for c in q]
    reh_res = sp.simplify(sp.expand_log(ent(P) - ent([lm, 1 - lm]) - lm * ent(p) - (1 - lm) * ent(q), force=True))
    aa, bb = sp.symbols("a b", positive=True)
    pq = [(1 + aa) * (1 + bb), -(1 + aa) * bb, -aa * (1 + bb), aa * bb]          # signs: +, -, -, +
    N_prod = sp.expand(((1 + aa) * bb + aa * (1 + bb)) - aa - bb)
    return {"solution_identity_pos": str(r_pos), "solution_identity_neg": str(r_neg),
            "ReH_convex_linear_residual": str(reh_res),
            "N_product_excess": str(N_prod), "pq_entries": [str(v) for v in pq]}


def _z3():
    try:
        import z3
        return z3
    except ImportError:
        return None


def z3_obligations():
    """Z3 (z3-solver; installed by pip, not vendored: PROOF-ASSISTANT.md).  Each obligation is proved by refuting its
    negation over GROUND INSTANCES of the axiom (sound: the instances follow from the universal axiom), with an
    uninterpreted g: R -> R.  Guards (PROOF-ASSISTANT.md): VACUITY -- the premises are satisfiable by a non-zero
    member (g = min(x, 0), i.e. X = -N) for EVERY lam in [0,1], x, y (proved, not sampled); ENCODING -- the encoded
    convex-linearity residual, evaluated in Python on g = -x ln|x| (Re H), is ~0, and on g = x^2 it is not; CONTROL --
    dropping the second instance leaves the Cauchy step unprovable (z3 returns a countermodel).
    Returns None if z3 is not importable (the selftest then prints the obligations as SKIPPED and counts them)."""
    z3 = _z3()
    if z3 is None:
        return None
    Rs = z3.RealSort()
    out = {}

    def cl(g, lam, p, q):
        """The convex-linearity instance for separable X = sum g on the terminal maps of p and q."""
        lhs = z3.Sum([g(lam * c) for c in p] + [g((1 - lam) * c) for c in q])
        rhs = g(lam) + g(1 - lam) + lam * z3.Sum([g(c) for c in p]) + (1 - lam) * z3.Sum([g(c) for c in q])
        return lhs == rhs

    def prove(premises, goal):
        s = z3.Solver()
        s.set("timeout", 60000)
        s.add(*premises)
        s.add(z3.Not(goal))
        r = s.check()
        return str(r)      # 'unsat' = proved

    # (2) g(0) = 0, from g(1) = 0 and convex linearity at lam = 1 with p = pt, q = (s, 1-s)
    g = z3.Function("g", Rs, Rs)
    sv = z3.Real("s")
    prem2 = [g(1) == 0, cl(g, z3.RealVal(1), [z3.RealVal(1)], [sv, 1 - sv])]
    out["z3_g0"] = prove(prem2, g(0) == 0)
    # (3) Cauchy: phi(x) + phi(y) = phi(x+y), phi(t) = g(lam t) - lam g(t), for symbolic lam in (0,1), x, y
    lam, x, y = z3.Reals("lam x y")
    phi = lambda t: g(lam * t) - lam * g(t)
    inst_a = cl(g, lam, [x, y, 1 - x - y], [z3.RealVal(1)])
    inst_b = cl(g, lam, [x + y, 1 - x - y], [z3.RealVal(1)])
    base = [g(1) == 0, g(0) == 0, lam > 0, lam < 1]
    out["z3_cauchy"] = prove(base + [inst_a, inst_b], phi(x) + phi(y) == phi(x + y))
    out["z3_cauchy_control_drop_instance_b"] = prove(base + [inst_a], phi(x) + phi(y) == phi(x + y))   # must be 'sat'
    # VACUITY: g = min(t, 0) (X = -N) satisfies both instances and g(0) = g(1) = 0 for ALL lam in [0,1], x, y
    gm = lambda t: z3.If(t < 0, t, z3.RealVal(0))
    lam2, x2, y2, s2 = z3.Reals("lam2 x2 y2 s2")
    vac = z3.And(cl(gm, lam2, [x2, y2, 1 - x2 - y2], [z3.RealVal(1)]), cl(gm, lam2, [x2 + y2, 1 - x2 - y2], [z3.RealVal(1)]),
                 cl(gm, z3.RealVal(1), [z3.RealVal(1)], [s2, 1 - s2]))
    out["vacuity_minus_N_satisfies_premises_for_all"] = prove([lam2 >= 0, lam2 <= 1], vac)               # 'unsat' = valid
    out["vacuity_member_nonzero"] = str(z3.simplify(gm(z3.RealVal(-1))))                               # -1, not 0
    # CODOMAIN: F = c dReH + b dN >= 0 on three morphisms (values from re_h/neg below, exact rationals of the floats)
    c, b = z3.Reals("c b")
    morph = codomain_morphisms()
    rv = lambda v: z3.RealVal(repr(float(v)))
    prem_c = [c * rv(m["dReH"]) + b * rv(m["dN"]) >= 0 for m in morph]
    out["z3_codomain"] = prove(prem_c, z3.And(c == 0, b >= 0))
    s = z3.Solver(); s.add(*prem_c); s.add(b > 0)
    out["codomain_vacuity_b_positive_sat"] = str(s.check())                                             # 'sat'
    s = z3.Solver(); s.add(*[c * rv(m["dReH"]) + b * rv(m["dN"]) >= 0 for m in morph if m["name"] != "merge_negatives"])
    s.add(c > 0)
    out["codomain_control_without_merge_c_positive"] = str(s.check())                                   # 'sat'
    out["z3_version"] = z3.get_version_string()
    return out


def encoding_guard(rng, trials=300):
    """ENCODING guard for z3_obligations: the Python twin of cl() on g = -x ln|x| (Re H) and on g = min(x, 0)
    (X = -N) has residual ~0 on random real (x, y, lam); on g = x^2 it does not (control)."""
    def g_reh(t):
        return -t * math.log(abs(t)) if t != 0 else 0.0

    def res(g, lam, p, q):
        return (sum(g(lam * c) for c in p) + sum(g((1 - lam) * c) for c in q)
                - (g(lam) + g(1 - lam) + lam * sum(g(c) for c in p) + (1 - lam) * sum(g(c) for c in q)))
    w = {"reh": 0.0, "minusN": 0.0, "x2_min": 1e9}
    for _ in range(trials):
        x, y, lam = rng.uniform(-3, 3), rng.uniform(-3, 3), rng.uniform(0.05, 0.95)
        p, q = [x, y, 1 - x - y], [1.0]
        w["reh"] = max(w["reh"], abs(res(g_reh, lam, p, q)))
        w["minusN"] = max(w["minusN"], abs(res(lambda t: min(t, 0.0), lam, p, q)))
        w["x2_min"] = min(w["x2_min"], abs(res(lambda t: t * t, lam, p, q)))
    return w


def codomain_morphisms():
    """Three morphisms used by z3_codomain, each with dReH = Re H(p) - Re H(q) and dN = N(p) - N(q) computed here."""
    ms = [("prob_merge", [0.5, 0.5], [1.0]), ("merge_negatives", [1.6, -0.3, -0.3], [1.6, -0.6]),
          ("crush", [1.5, -0.5], [1.0])]
    return [{"name": nm, "p": p, "q": q, "dReH": re_h(p) - re_h(q), "dN": neg(p) - neg(q)} for nm, p, q in ms]


def kontsevich_checks(rng, trials=400):
    """Kontsevich, appendix 'The 1 1/2-logarithm' to Elbaz-Vincent & Gangl math/0008089v1 (READ pp.42-44):
      (A) H(1-x) = H(x); (B) H(x+y) = H(y) + (1-y) H(x/(1-y)) + y H(-x/y), y != 0, 1; (C) x H(1/x) = -H(x), x != 0;
    p.43 CLAIM: the only nonzero continuous solution R -> R, up to scale, is H_inf(x) = -(x log|x| + (1-x) log|1-x|).
    H_inf(x) IS Re H on the two-entry signed measure (x, 1-x), so the claim is a uniqueness statement for Re H on
    two entries over all of R.  Checked here: Re H satisfies (A), (B), (C) on random reals; the chain rule with
    SIGNED outer weights, Re H(p o (g_1..g_n)) = Re H(p) + sum p_i Re H(g_i), on random signed p, g_i.
    CONTROL: N, which is convex-linear in BFL's sense (lam in [0,1]), FAILS (B) and FAILS the signed-weight chain
    rule -- Kontsevich's equations admit negative weights, BFL's convex linearity does not, and that is exactly
    where N is excluded."""
    H2 = lambda x: re_h([x, 1 - x])
    N2 = lambda x: neg([x, 1 - x])
    w = {"A": 0.0, "B": 0.0, "C": 0.0, "chain": 0.0, "B_N_max": 0.0, "chain_N_max": 0.0}
    for _ in range(trials):
        x, y = rng.uniform(-4, 4), rng.uniform(-4, 4)
        if min(abs(y), abs(1 - y), abs(x)) < 1e-3:
            continue
        w["A"] = max(w["A"], abs(H2(1 - x) - H2(x)))
        w["B"] = max(w["B"], abs(H2(x + y) - (H2(y) + (1 - y) * H2(x / (1 - y)) + y * H2(-x / y))))
        w["C"] = max(w["C"], abs(x * H2(1 / x) + H2(x)))
        w["B_N_max"] = max(w["B_N_max"], abs(N2(x + y) - (N2(y) + (1 - y) * N2(x / (1 - y)) + y * N2(-x / y))))
        p = rand_quasi(rng, rng.randint(2, 4))
        gs = [rand_quasi(rng, rng.randint(2, 3)) for _ in p]
        comp = [pi * gij for pi, gi in zip(p, gs) for gij in gi]
        w["chain"] = max(w["chain"], abs(re_h(comp) - re_h(p) - sum(pi * re_h(gi) for pi, gi in zip(p, gs))))
        w["chain_N_max"] = max(w["chain_N_max"], abs(neg(comp) - neg(p) - sum(pi * neg(gi) for pi, gi in zip(p, gs))))
    # the worked control instance: x = 0.5, y = -1
    w["B_N_instance"] = {"x": 0.5, "y": -1.0, "lhs": N2(-0.5), "rhs": N2(-1.0) + 2.0 * N2(0.25) + (-1.0) * N2(0.5)}
    # Kontsevich's phi(x, y) = (x+y) H((x)/(x+y)) is set to 0 when x + y = 0 (p.43): a block of total 0 is excluded
    w["zero_total_block_note"] = "phi(x, -x) := 0 by definition on p.43; such a block has no normalised Re H"
    return w


def m_uniqueness_counterexample(rng, trials=300):
    """AGAINST V2-0 problem 4, re-computed: g3(p) = ln(sum|p|^3 / |sum p^3|) is product-additive (sum|pq|^3 and
    sum (pq)^3 are both multiplicative), is 0 on every probability vector, and differs from M on (1.5, -0.5).
    So 'M is THE product-additive functional vanishing on probabilities' needs a qualifier (H-DICTIONARY, or
    functions of N alone).  M itself is the exponent-1 member, ln(sum|p| / |sum p|).  g3 is undefined where
    sum p^3 = 0, which some signed measures reach: a counterexample to uniqueness, not a proposed measure."""
    g3 = lambda p: math.log(sum(abs(x) ** 3 for x in p) / abs(sum(x ** 3 for x in p)))
    worst_prod, worst_prob = 0.0, 0.0
    for _ in range(trials):
        p, q = rand_quasi(rng, rng.randint(2, 4)), rand_quasi(rng, rng.randint(2, 4))
        if min(abs(sum(x ** 3 for x in p)), abs(sum(x ** 3 for x in q))) < 1e-3:
            continue
        worst_prod = max(worst_prod, abs(g3(product(p, q)) - g3(p) - g3(q)))
        worst_prob = max(worst_prob, abs(g3(rand_prob(rng, rng.randint(2, 6)))))
    return {"product_residual": worst_prod, "on_probabilities_max": worst_prob, "g3_(1.5,-0.5)": g3([1.5, -0.5]),
            "M_(1.5,-0.5)": mana([1.5, -0.5])}


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


def lambda_mobius(control_box=False, random_set=None, vectors=False, support_cells=False):
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
        if support_cells:                     # M-apply (2026-10-03): the support's coordinates, same order as p_vector
            out["support_cells"] = [tuple(int(i) for i in x) for x in idx]
    return out


# ============================================================================ (8) both weightings carried (M, item 2)
# M (M-RULINGS-2026-10-03.md item 2): "Carry both (Recommended)".  Brandenburger-La Mura's mean-value axiom 5'
# (2410.15976v5 p.3 eq.(9), READ this pass) weights the two parts by |w(P)|, |w(Q)| over |w(P) + w(Q)|; the variant
# with SIGNED weights w(P), w(Q) over w(P) + w(Q) is this file's (4)(d).  Each weighting is carried with the functional
# it selects and with every axiom computed for it below -- none is declared.  Axiom numbering is theirs (p.3):
# A0 real-valuedness, A2' continuity of H((p)) for p != 0, A3 calibration H((1/2)) = 1, A4 extensivity
# H(P * Q) = H(P) + H(Q), A5' the mean-value property with the stated weighting.

WEIGHTING_ALPHAS = (0.5, 2.0)        # two orders of signed Renyi (alpha > 0, alpha != 1; BLM Theorem 1, p.4)


def blm_hartley(P):
    """BLM's alpha = 0 limit (p.4, eq.(A.18) p.11): log2(#{p_i != 0} / |sum p|)."""
    return math.log2(sum(1 for x in P if x != 0) / abs(sum(P)))


def _rand_signed_measure(rng, nmax=4):
    while True:
        A = [rng.uniform(-1, 2) for _ in range(rng.randint(1, nmax))]
        if abs(sum(A)) > 1e-2 and all(abs(x) > 1e-9 for x in A):
            return A


def mean_value_residual(F, g, ginv, weighting, rng, trials=300):
    """max |F(P u Q) - g^-1(mean)| over random signed P, Q, with the mean taken under `weighting`:
    'abs'    : (|wP| g(F(P)) + |wQ| g(F(Q))) / |wP + wQ|     (BLM Axiom 5', p.3 eq.(9), READ)
    'signed' : ( wP  g(F(P)) +  wQ  g(F(Q))) /  (wP + wQ)    (this file's signed-weight variant)
    Returns (worst residual, number of pairs where g^-1 is undefined, one such pair)."""
    worst, undefined, witness = 0.0, 0, None
    for _ in range(trials):
        A, B = _rand_signed_measure(rng), _rand_signed_measure(rng)
        wA, wB = sum(A), sum(B)
        if abs(wA + wB) < 1e-2:
            continue
        if weighting == "abs":
            m = (abs(wA) * g(F(A)) + abs(wB) * g(F(B))) / abs(wA + wB)
        else:
            m = (wA * g(F(A)) + wB * g(F(B))) / (wA + wB)
        try:
            v = ginv(m)
        except ValueError:
            undefined += 1
            witness = witness or (A, B, m)
            continue
        worst = max(worst, abs(F(A + B) - v))
    return worst, undefined, witness


def _axioms_of(F, g, ginv, rng):
    """A0, A2', A3, A4 and A5' under both weightings, computed for the functional F (BLM normalisation)."""
    vals = [F(_rand_signed_measure(rng, 6)) for _ in range(300)]
    a0 = all(isinstance(v, float) and math.isfinite(v) for v in vals)
    grid = [x / 50 for x in range(-100, 101) if x != 0]
    a2 = max(abs(F([x]) + math.log2(abs(x))) for x in grid)          # H((p)) = -log2|p| (BLM Lemma A.1, p.10)
    a3 = F([0.5])
    a4 = 0.0
    for _ in range(300):
        A, B = _rand_signed_measure(rng), _rand_signed_measure(rng)
        a4 = max(a4, abs(F(product(A, B)) - F(A) - F(B)))
    mv_abs = mean_value_residual(F, g, ginv, "abs", rng)
    mv_sgn = mean_value_residual(F, g, ginv, "signed", rng)
    return {"A0_real_on_300_signed": a0, "A2_max_dev_from_-log2|p|": a2, "A3_H((1/2))": a3,
            "A4_extensivity_worst": a4,
            "A5_abs_weights_worst": mv_abs[0], "A5_abs_weights_undefined": mv_abs[1],
            "A5_signed_weights_worst": mv_sgn[0], "A5_signed_weights_undefined": mv_sgn[1]}


def weightings(rng):
    """Both weightings, each with the functional it selects and the axioms computed for it.
      signed w -> Re H (affine g; BLM normalisation -sum p log2|p| / sum p).  Selection DERIVED-CONDITIONAL (4)(d),
                  carrying H-RD.  Its exponential branch fails A0 (axiom0_counterexample).
      |w|      -> signed Renyi H_alpha (exponential g(x) = 2^((1-alpha)x)); READ: BLM Theorem 1 (p.4), proof pp.10-11
                  carrying H-RD.  Its affine branch, the |p|-weighted 'signed Shannon' eq.(11), fails A4 (Example 1,
                  p.4, reproduced in blm_checks).
    Also computed for each: does it reduce to BFL's Shannon on probability measures (convex linearity on FinProb),
    and does it keep BFL's codomain [0, inf) on signed morphisms."""
    lin = (lambda x: x, lambda y: y)
    out = {"signed w": {"functional": "Re H (BLM-normalised)", "g": "affine",
                        "selection_status": "DERIVED-CONDITIONAL (H-RD; Lemma A.2 induction with signed weights)",
                        "axioms": _axioms_of(blm_reh, lin[0], lin[1], rng)}}
    for a in WEIGHTING_ALPHAS:
        g = (lambda a_: (lambda x: 2.0 ** ((1 - a_) * x)))(a)

        def ginv(y, a_=a):
            if y <= 0:
                raise ValueError("g^-1 undefined: argument <= 0")
            return math.log2(y) / (1 - a_)
        F = (lambda a_: (lambda P: blm_renyi(P, a_)))(a)
        out[f"|w|, alpha = {a}"] = {"functional": f"signed Renyi H_{a}", "g": "exponential",
                                    "selection_status": "READ (BLM Theorem 1, p.4; proof pp.10-11 carries H-RD)",
                                    "axioms": _axioms_of(F, g, ginv, rng)}
    # on probability measures: Re H IS Shannon; signed Renyi-alpha is Renyi-alpha, which fails BFL convex linearity
    # (measure.py's control F_renyi2); computed here on the 1106.1791 convex combination for the two functionals.
    def convex_gap(Fp):
        worst = 0.0
        for _ in range(200):
            lam = rng.random()
            p1, p2 = rand_prob(rng, rng.randint(2, 5)), rand_prob(rng, rng.randint(2, 5))
            q1, q2 = [sum(p1)], [sum(p2)]
            loss = lambda p, q: Fp(p) - Fp(q)
            lhs = loss(direct_sum(lam, p1, p2), direct_sum(lam, q1, q2))
            rhs = lam * loss(p1, q1) + (1 - lam) * loss(p2, q2)
            worst = max(worst, abs(lhs - rhs))
        return worst
    out["signed w"]["BFL_convex_linearity_on_FinProb_worst"] = convex_gap(blm_reh)
    for a in WEIGHTING_ALPHAS:
        out[f"|w|, alpha = {a}"]["BFL_convex_linearity_on_FinProb_worst"] = convex_gap(lambda P, a_=a: blm_renyi(P, a_))
    # BFL codomain on the signed crush (1.5, -0.5) -> one point: loss = F(p) - F((1))
    out["signed w"]["crush_loss_(1.5,-0.5)_bits"] = blm_reh([1.5, -0.5]) - blm_reh([1.0])
    for a in WEIGHTING_ALPHAS:
        out[f"|w|, alpha = {a}"]["crush_loss_(1.5,-0.5)_bits"] = blm_renyi([1.5, -0.5], a) - blm_renyi([1.0], a)
    out["hartley_alpha0"] = {"A3": blm_hartley([0.5]), "A4_on_(2,-1)x(2,-1)": blm_hartley([4, -2, -2, 1]) -
                             2 * blm_hartley([2, -1])}
    return out


def both_on(p):
    """Both weightings' functionals on one weighting p (sum p = 1), in bits: Re H and signed Renyi-alpha."""
    return {"Re H (signed w)": re_h(p) / LN2, **{f"H_{a} (|w|)": blm_renyi(p, a) for a in WEIGHTING_ALPHAS}}


# ============================================================================ (9) the ground-state calibration
# M (item 3): "Remember that the center begins at the ground state values given in real numbers from the periodic
# table. That is the calibration".  M (item 6): "Mass/ binding. But could work for any of the other options depending
# on the question being asks or the object of study".  So the DEFAULT calibration is MASS/BINDING, and two others are
# selectable: GROUND-CONFIG (LW1-ground.py, through tools/populate.py) and IONISATION (the ionisation ladder; what
# tools/populate.py itself banks is reported beside it).  Every use below names its calibration.
#
# THE OBJECT (named: H-MASS-CELLS).  A state of an atom or ion is written as its mass-energy budget over four cells --
# protons Z m_p, electrons (Z - q) m_e, neutrons N m_n, and the binding -B -- divided by the state's mass M.  The four
# weights total 1 EXACTLY (B is defined as the shortfall), and the binding is a NEGATIVE weight: a quasi-probability
# read straight off the periodic table's real numbers.  The GROUND is the neutral atom in its ground state (AME2020's
# atomic mass); a state's signed deviation from it is d = p - p0, and in log space ln(p/p0), which is 0 at the ground.
#
# DATA (each READ on the board; none typed here):
#   AME2020 Table I mass excesses -- gravity.nuclides() (imported), the board's capture of the published table
#     (Chinese Physics C 45, 030003, from the PDF M supplied; cross-checked by its header against the fetched
#     mass_1.mas20).  No arXiv copy of AME2020 was found (alphaXiv search, 2026-10-03), so the arXiv route is closed;
#     the capture is the READ.
#   m_p, m_n, m_e -- massform.MASS_MEV (imported), PDG-2026 capture, READ.
#   ionisation energies -- NIST ASD captures IE-neutral-all.tsv (first IE, Z = 1-108) and LADDER-K-Kr.tsv (every
#     charge, Z = 19-36), read here as data (no board instrument reads them yet).
#   u c^2 -- DERIVED-FROM-READ: M(1H) = m_p + m_e - I(H) and M(1H) = u + Delta(1H) give u = m_p + m_e - I(H) - Delta(1H).
#     CODATA 2018's u (gravity.U_KG, typed there; NAMED-NOT-READ) is a cross-check only.

CAPTURES = os.path.abspath(os.path.join(HERE, "..", "..", "..", "extracted", "archives", "restore-point-2-13",
                                        "captures"))
CAL_DEFAULT = "MASS/BINDING"
CALIBRATIONS = ("MASS/BINDING", "GROUND-CONFIG", "IONISATION")
MASS_CELLS = ("protons", "electrons", "neutrons", "binding")
_CAL_CACHE = {}


def _board_mod(name):
    """Import a board instrument quietly from research/warp-drive or tools (several print at import)."""
    wd = os.path.abspath(os.path.join(HERE, ".."))
    tools = os.path.abspath(os.path.join(HERE, "..", "..", "..", "tools"))
    for d in (wd, tools):
        if d not in sys.path:
            sys.path.insert(0, d)
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__(name)


def _read_tsv(fname, ncol):
    rows = []
    with open(os.path.join(CAPTURES, fname), encoding="utf-8") as fh:
        for ln in fh:
            if ln.startswith("#") or not ln.strip():
                continue
            parts = ln.rstrip("\n").split("\t")
            if len(parts) >= ncol and parts[0].strip().lstrip("-").isdigit():
                rows.append(parts)
    return rows


def ionisation_ev():
    """{(Z, charge): (IE eV, quality)} from the two NIST captures (READ).  Where both carry a neutral value they are
    compared in the selftest (the ladder capture is the multi-charge one)."""
    if "ie" not in _CAL_CACHE:
        ie, first = {}, {}
        for r in _read_tsv("IE-neutral-all.tsv", 5):
            first[int(r[0])] = (float(r[2]), r[4].strip())
        for r in _read_tsv("LADDER-K-Kr.tsv", 4):
            ie[(int(r[0]), int(r[1].replace("+", "")))] = (float(r[2]), r[3].strip())
        for z, v in first.items():
            ie.setdefault((z, 0), v)
        _CAL_CACHE["ie"] = (ie, first)
    return _CAL_CACHE["ie"]


def read_constants():
    """Every number the MASS/BINDING calibration uses, with its status."""
    if "k" not in _CAL_CACHE:
        mf, gr = _board_mod("massform"), _board_mod("gravity")
        ie, first = ionisation_ev()
        dH = [r for r in gr.nuclides() if r[0] == 1 and r[2] == 1][0][4]
        dn = [r for r in gr.nuclides() if r[0] == 0 and r[2] == 1][0][4]
        mp, mn, me = (mf.MASS_MEV[k] * 1000.0 for k in ("p", "n", "e"))            # keV
        u = mp + me - first[1][0] / 1000.0 - dH                                       # keV, DERIVED-FROM-READ
        u_codata = gr.U_KG * gr.C_SI ** 2 / gr.KEV_J                                  # NAMED-NOT-READ cross-check
        _CAL_CACHE["k"] = {"m_p_keV": mp, "m_n_keV": mn, "m_e_keV": me, "Delta_1H_keV": dH, "Delta_n_keV": dn,
                           "I_H_eV": first[1][0], "u_keV": u, "u_keV_CODATA2018": u_codata,
                           "m_n_via_AME_keV": u + dn,
                           "status": {"m_p, m_n, m_e": "READ (PDG-2026 capture via massform.MASS_MEV)",
                                      "Delta": "READ (AME2020 Table I capture via gravity.nuclides)",
                                      "I": "READ (NIST ASD captures)", "u": "DERIVED-FROM-READ",
                                      "u_CODATA2018": "NAMED-NOT-READ (gravity.U_KG), cross-check only"}}
    return _CAL_CACHE["k"]


def mass_excess_keV(Z, A):
    gr = _board_mod("gravity")
    rows = [r for r in gr.nuclides() if r[0] == Z and r[2] == A]
    if not rows:
        raise KeyError(f"AME2020 Table I holds no Z = {Z}, A = {A}")
    return rows[0][4], rows[0][5]


def mass_cells(Z, A, q=0):
    """H-MASS-CELLS for the state (Z, A, charge q), in keV: (cells, M_state).  M_state = M_atom - q m_e + sum of the
    first q ionisation energies (each ground-to-ground, H-IE-GROUND); B_state = Z m_p + (Z-q) m_e + N m_n - M_state.
    Refuses (KeyError) a q whose ladder the captures do not hold: an unread value is not filled in."""
    k = read_constants()
    ie, _ = ionisation_ev()
    dm, quality = mass_excess_keV(Z, A)
    M_atom = A * k["u_keV"] + dm
    need = [(Z, j) for j in range(q)]
    missing = [s for s in need if s not in ie]
    if missing:
        raise KeyError(f"ionisation energies NOT READ for {missing[:3]}{'...' if len(missing) > 3 else ''}")
    sum_ie = sum(ie[s][0] for s in need) / 1000.0
    M = M_atom - q * k["m_e_keV"] + sum_ie
    N = A - Z
    cells = [Z * k["m_p_keV"], (Z - q) * k["m_e_keV"], N * k["m_n_keV"]]
    cells.append(M - sum(cells))                                          # = -B_state
    return cells, M, {"AME_quality": quality, "IE_qualities": sorted({ie[s][1] for s in need}), "sum_IE_keV": sum_ie}


def calibrate(Z, A=None, q=0, calibration=CAL_DEFAULT):
    """(p, p0, cells, info) for the state (Z, A, q) against its element's ground, under the NAMED calibration.
      MASS/BINDING  (default)  H-MASS-CELLS: p = cells / M_state, p0 = the neutral atom's (READ masses / binding).
      GROUND-CONFIG            LW1-ground.py's observed ground configuration (through tools/populate.py, imported):
                               p = subshell occupancies / electrons.  The ion's configuration is the isoelectronic
                               neutral's (populate.ionisation_cells' mapping: RECONSTRUCTED there, and here).
      IONISATION               cells = the Z electrons in removal order, weight = each one's ionisation energy (NIST
                               ladder, READ); the ion's first q cells are empty.  populate.series_limit is consulted
                               for every stage and what it banks is reported (it banks very few stages).
    Only MASS/BINDING carries a negative weight; the other two are non-negative, so their measures are Shannon's."""
    if calibration not in CALIBRATIONS:
        raise ValueError(f"calibration must be one of {CALIBRATIONS}")
    if calibration == "MASS/BINDING":
        if A is None:
            raise ValueError("MASS/BINDING needs a nuclide (Z, A)")
        x, M, inf = mass_cells(Z, A, q)
        x0, M0, inf0 = mass_cells(Z, A, 0)
        return ([v / M for v in x], [v / M0 for v in x0], list(MASS_CELLS),
                {"calibration": calibration, "unit": "keV", "x": x, "x0": x0, "M_state_keV": M, "M_ground_keV": M0,
                 "B_ground_keV": -x0[3], "B_state_keV": -x[3], **inf,
                 "hypotheses": ["H-MASS-CELLS", "H-IE-GROUND", "H-AME-ATOMIC"]})
    if calibration == "GROUND-CONFIG":
        pop = _board_mod("populate")
        Ne = Z - q
        if Ne < 1:
            raise ValueError("no electrons: GROUND-CONFIG has no distribution for a bare nucleus")
        g0 = {(n, l): o for n, l, o in pop.LW1.expand(Z)}
        g = {(n, l): o for n, l, o in pop.LW1.expand(Ne)}
        keys = sorted(set(g0) | set(g))
        cells = ["%d%s" % (n, pop.LSYM[l]) for n, l in keys]
        return ([g.get(k, 0) / Ne for k in keys], [g0.get(k, 0) / Z for k in keys], cells,
                {"calibration": calibration, "unit": "electrons", "x": [g.get(k, 0) for k in keys],
                 "x0": [g0.get(k, 0) for k in keys], "ground_level": pop.LW1.GROUND[Z][2],
                 "ion_configuration_status": "RECONSTRUCTED (isoelectronic neutral, populate.ionisation_cells)",
                 "hypotheses": ["H-ISOELECTRONIC"]})
    pop = _board_mod("populate")
    ie, _ = ionisation_ev()
    stages = [(Z, j) for j in range(Z)]
    missing = [s for s in stages if s not in ie]
    if missing:
        raise KeyError(f"IONISATION needs the full ladder; NOT READ for {len(missing)} stages of Z = {Z}")
    x0 = [ie[s][0] for s in stages]
    x = [0.0 if j < q else x0[j] for j in range(Z)]
    banked = {j + 1: pop.series_limit(Z, j + 1) for j in range(Z)}
    return ([v / sum(x) for v in x], [v / sum(x0) for v in x0], [f"e{j + 1}" for j in range(Z)],
            {"calibration": calibration, "unit": "eV", "x": x, "x0": x0,
             "populate_series_limit_banked": {k: v for k, v in banked.items() if v is not None},
             "qualities": sorted({ie[s][1] for s in stages}), "hypotheses": ["H-LADDER-CELLS"]})


# ---------------------------------------------------------------------------- the centred measures

def rel_entropy(p, p0):
    """D_s(p || p0) = sum p_i Log(p_i / p0_i), principal branch (H-PRINCIPAL), complex.  0 Log(0/x) = 0.  Returns
    None where p_i != 0 at p0_i = 0 (BF 1402.3067v2 p.1: the term is infinite) -- absolute continuity fails."""
    tot = 0j
    for a, b in zip(p, p0):
        if a == 0:
            continue
        if b == 0:
            return None
        r = a / b
        tot += a * complex(math.log(abs(r)), PI if r < 0 else 0.0)
    return tot


def centred(p, p0):
    """The two ground-centred candidates, and the identity that relates them (DERIVED, checked here):
         Re H(p0) - Re H(p) = Re D_s(p||p0) + X,     X = sum (p_i - p0_i) ln|p0_i|   (the cross term).
    So the entropy deviation dRe H = Re H(p) - Re H(p0) equals -Re D_s exactly when X = 0 (e.g. |p0| constant on
    the joint support and both totals 1), and otherwise it is NOT a relative entropy."""
    D = rel_entropy(p, p0)
    X = sum((a - b) * math.log(abs(b)) for a, b in zip(p, p0) if b != 0)
    dre = re_h(p) - re_h(p0)
    return {"D": D, "re_D": None if D is None else D.real, "im_D": None if D is None else D.imag,
            "D_reverse": rel_entropy(p0, p), "dReH": dre, "cross_X": X,
            "identity_residual": None if D is None else (re_h(p0) - re_h(p)) - (D.real + X)}


def radon_grid(vals, d=None):
    """The discrete Radon transform on Z_d^2 (d prime; cells laid row-major, zero-padded: H-RADON-PAD) and its exact
    inverse W(a) = (sum over the d+1 lines through a of P(line) - T) / d, T the total (DERIVED: every other point
    shares exactly one line with a; the GHW eq.(55) form, p.27, for T = 1).  Returns (line sums, reconstruction,
    max reconstruction error, min line sum)."""
    if d is None:
        d = next(k for k in (2, 3, 5, 7, 11, 13) if k * k >= len(vals))
    pts = [(i // d, i % d) for i in range(d * d)]
    W = {pt: (vals[i] if i < len(vals) else 0.0) for i, pt in enumerate(pts)}
    T = sum(W.values())
    L = lines(d)
    P = {(dirn, Lset): sum(W[x] for x in Lset) for dirn, Lset in L}
    rec = {a: (sum(v for (dirn, Lset), v in P.items() if a in Lset) - T) / d for a in pts}
    err = max(abs(rec[a] - W[a]) for a in pts)
    return P, [rec[a] for a in pts][:len(vals)], err, min(P.values())


def centred_table(p, p0, cells):
    """ONE multi-axis table, centred at the ground state: per cell the deviation and the four 'inverses and
    reflections' M ruled all carried (item 3) -- (1) the log branches of the ratio r = p/p0, (2) the conjugate and
    the reciprocal (reflection through the ground), (3) the fold to |p|, (4) the Radon inverse -- each 0 / identity
    at the ground by construction where it is a deviation."""
    rows = []
    _, rec_d, err_d, min_d = radon_grid([a - b for a, b in zip(p, p0)])
    _, rec_p, err_p, min_p = radon_grid(p)
    for i, (a, b, c) in enumerate(zip(p, p0, cells)):
        r = None if b == 0 else a / b
        arg = None if r is None or r == 0 else (PI if r < 0 else 0.0)
        rows.append({
            "cell": c, "p": a, "p0": b, "d=p-p0": a - b,
            "(1) ln|r|": None if not r else math.log(abs(r)), "(1) arg r (principal)": arg,
            "(1) Im D step per unit k_i": None if r is None else 2 * PI * a,
            "(2) arg conj": None if arg is None else -arg, "(2) 1/r": None if not r else 1 / r,
            "(2) -Log r (re)": None if not r else -math.log(abs(r)),
            "(3) |p|": abs(a), "(3) |p0|": abs(b),
            "(3) ln(|p|/|p0|)": None if (a == 0 or b == 0) else math.log(abs(a) / abs(b)),
            "(4) Radon-inverse d": rec_d[i], "(4) Radon-inverse p": rec_p[i]})
    sa, sb = sum(abs(x) for x in p), sum(abs(x) for x in p0)
    fold_D = rel_entropy([abs(x) / sa for x in p], [abs(x) / sb for x in p0])
    return {"rows": rows, "radon_err_d": err_d, "radon_err_p": err_p, "radon_min_line_d": min_d,
            "radon_min_line_p": min_p, "fold_renormalised_D": None if fold_D is None else fold_D.real,
            "reflection_D_reverse": rel_entropy(p0, p)}


# ---------------------------------------------------------------------------- is it a relative entropy? (tested)

def rand_full_signed(rng, n, N=None):
    """A random quasi-probability with total 1 and no zero entry (n >= 2)."""
    return rand_quasi(rng, n, Ntarget=N)


def re_axioms(rng, trials=400):
    """Re D_s tested against relative entropy's properties.  Shannon cases (both non-negative) must pass every one --
    that is the control set; signed cases are measured, not presumed.
      R0  D(p||p) = 0                                (definitional: ln 1 = 0; printed STRUCTURAL)
      R1  Gibbs: D >= 0  (BF Theorem 7's codomain [0, inf], 1402.3067v2 p.11)
      R2  product additivity  D(p x q || p0 x q0) = D(p||p0) + D(q||q0)
      R3  data processing under coarse-graining f:  D(f_*p || f_*p0) <= D(p||p0)
      R4  convex linearity (BF p.3, p.15):  D(lam p (+) (1-lam) q || lam p0 (+) (1-lam) q0) = lam D + (1-lam) D'
      R5  chain rule (the conditional-expectation law, BF p.26 eq.(5.1) form): D(p||p0) = D(f_*p||f_*p0)
          + sum_y (f_*p)_y D(p|y || p0|y), block totals non-zero."""
    out = {}
    sh_min, sg_min, sg_w = 1e9, 1e9, None
    for _ in range(trials):
        n = rng.randint(2, 6)
        a, b = rand_prob(rng, n), rand_prob(rng, n)
        sh_min = min(sh_min, rel_entropy(a, b).real)
        s, t = rand_full_signed(rng, n), rand_full_signed(rng, n)
        v = rel_entropy(s, t).real
        if v < sg_min:
            sg_min, sg_w = v, (s, t)
    out["R1_shannon_min"] = sh_min
    out["R1_signed_min"] = sg_min
    out["R1_signed_witness"] = sg_w
    out["R1_reference_signed_(0.5,0.5)||(1.5,-0.5)"] = rel_entropy([0.5, 0.5], [1.5, -0.5]).real
    out["R1_state_signed_(1.5,-0.5)||(0.9,0.1)"] = rel_entropy([1.5, -0.5], [0.9, 0.1]).real
    r2, r2im, r2c = 0.0, 0.0, 0.0
    for _ in range(trials):
        p, p0 = rand_full_signed(rng, 3), rand_full_signed(rng, 3)
        q, q0 = rand_full_signed(rng, 2), rand_full_signed(rng, 2)
        lhs = rel_entropy(product(p, q), product(p0, q0))
        rhs = rel_entropy(p, p0) + rel_entropy(q, q0)
        r2 = max(r2, abs(lhs.real - rhs.real))
        r2im = max(r2im, abs(lhs.imag - rhs.imag))
        q2 = [2 * x for x in q]                                      # control: total 2 breaks Re additivity
        r2c = max(r2c, abs(rel_entropy(product(p, q2), product(p0, q0)).real - rel_entropy(p, p0).real
                           - rel_entropy(q2, q0).real))
    out["R2_re_worst"], out["R2_im_worst"], out["R2_control_total2_worst"] = r2, r2im, r2c
    sh_viol, sg_viol, sg_wit = 0, 0, None
    for _ in range(trials):
        n = rng.randint(3, 6)
        m = rng.randint(2, n - 1)
        f = rand_surj(rng, n, m)
        a, b = rand_prob(rng, n), rand_prob(rng, n)
        sh_viol += rel_entropy(push(a, f, m), push(b, f, m)).real > rel_entropy(a, b).real + 1e-12
        s, t = rand_full_signed(rng, n), rand_full_signed(rng, n)
        ps, pt = push(s, f, m), push(t, f, m)
        if min(abs(x) for x in ps + pt) < 1e-6:
            continue
        if rel_entropy(ps, pt).real > rel_entropy(s, t).real + 1e-12:
            sg_viol += 1
            sg_wit = sg_wit or (s, t, f)
    out["R3_shannon_violations"], out["R3_signed_violations"], out["R3_signed_witness"] = sh_viol, sg_viol, sg_wit
    r4 = 0.0
    for _ in range(trials):
        lam = rng.random()
        p, p0 = rand_full_signed(rng, 3), rand_full_signed(rng, 3)
        q, q0 = rand_full_signed(rng, 2), rand_full_signed(rng, 2)
        lhs = rel_entropy(direct_sum(lam, p, q), direct_sum(lam, p0, q0))
        rhs = lam * rel_entropy(p, p0) + (1 - lam) * rel_entropy(q, q0)
        r4 = max(r4, abs(lhs - rhs))
    out["R4_convex_worst"] = r4
    r5 = 0.0
    for _ in range(trials):
        n = rng.randint(3, 6)
        m = rng.randint(2, n - 1)
        f = rand_surj(rng, n, m)
        s, t = rand_full_signed(rng, n), rand_full_signed(rng, n)
        ps, pt = push(s, f, m), push(t, f, m)
        if min(abs(x) for x in ps + pt) < 1e-3:
            continue
        cond = 0.0
        for y in range(m):
            idx = [i for i in range(n) if f[i] == y]
            cond += ps[y] * rel_entropy([s[i] / ps[y] for i in idx], [t[i] / pt[y] for i in idx]).real
        r5 = max(r5, abs(rel_entropy(s, t).real - rel_entropy(ps, pt).real - cond))
    out["R5_chain_rule_re_worst"] = r5
    return out


def index_centred():
    """The Method's index under a NAMED ground (no periodic-table numbers exist for it):
      H-INDEX-GROUND-BOX     the ground is the uniform measure on the full product box (6,912 cells: every coordinate
                             combination, before closure);
      H-INDEX-GROUND-LAMBDA  the ground is the uniform measure on Lambda (976 cells; A3's H-UNIFORM).
    States: the Mobius weighting p and the box-mixture q (H-MOBIUS-WEIGHT), and the uniform measure on Lambda."""
    import measure
    import cypher
    ix = cypher._lambda()
    shape = tuple(len(a) for a in ix.alphabets)
    ind = np.zeros(shape)
    for c in ix.cells:
        ind[c] = 1.0
    with contextlib.redirect_stdout(io.StringIO()):
        lm = lambda_mobius(vectors=True, support_cells=True)
    box_n = int(np.prod(shape))
    lam_n = int(ind.sum())
    supp = lm["support_cells"]
    in_lambda = sum(1 for c in supp if ind[c] == 1.0)
    out = {"box": box_n, "lambda": lam_n, "support": len(supp), "support_in_lambda": in_lambda,
           "support_outside_lambda": len(supp) - in_lambda}
    for nm, vec in (("mobius_p", lm["p_vector"]), ("box_mixture_q", lm["q_vector"])):
        D = sum(a * complex(math.log(abs(a) * box_n), PI if a < 0 else 0.0) for a in vec)
        out[nm] = {"D_vs_box_bits": D.real / LN2, "imD_vs_box": D.imag, "N": neg(vec),
                   "dReH_vs_box_bits": (re_h(vec) - math.log(box_n)) / LN2,
                   "cross_X_vs_box": -math.log(box_n) * (sum(vec) - 1.0),
                   "D_vs_lambda": None if in_lambda < len(supp) else "finite",
                   "both_weightings": both_on(vec)}
    out["uniform_lambda_vs_box_bits"] = math.log(box_n / lam_n) / LN2
    out["A3_closure_bits"] = measure.method_bits()["closure_bits"]
    return out


def centred_applications():
    """The calibration applied: one element and its ions under the DEFAULT calibration, the alternatives offered on
    the same ion, and two controls.  Every entry names its calibration."""
    out = {}
    for lab, (Z, A, q) in {"Fe-56 ground (element; centre)": (26, 56, 0), "Fe-56 +1 (ion)": (26, 56, 1),
                           "Fe-56 +26 (bare nucleus)": (26, 56, 26), "C-12 +1 (ion)": (6, 12, 1),
                           "H-1 +1 (the proton)": (1, 1, 1)}.items():
        p, p0, cells, info = calibrate(Z, A, q, CAL_DEFAULT)
        c = centred(p, p0)
        out[lab] = {"calibration": info["calibration"], "p": p, "p0": p0, "N_p": neg(p), "N_p0": neg(p0),
                    "case": "SIGNED" if min(p) < 0 else "SHANNON", "B_ground_keV": info["B_ground_keV"],
                    "B_state_keV": info["B_state_keV"], "sum_IE_keV": info["sum_IE_keV"],
                    "re_h_p_nats": re_h(p), "re_h_p0_nats": re_h(p0), **{k: c[k] for k in c},
                    "table": centred_table(p, p0, cells), "both_weightings": both_on(p)}
    alt = {}
    for cal in ("GROUND-CONFIG", "IONISATION"):
        p, p0, cells, info = calibrate(26, 56, 1, cal)
        alt[cal] = {"calibration": cal, "cells": cells, "N_p": neg(p), **centred(p, p0),
                    "info": {k: v for k, v in info.items() if k not in ("x", "x0")}}
    out["alternatives, Fe +1"] = alt
    p, p0, _, _ = calibrate(26, 54, 0)
    q, q0, _, _ = calibrate(26, 56, 0)
    out["CONTROL another ground: Fe-54 ground vs Fe-56 ground"] = centred(p, q0)
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
    ("math/0008089v1", "Elbaz-Vincent, Gangl, On poly(ana)logs I, with the appendix 'The 1 1/2-logarithm' by M. "
     "Kontsevich (his unpublished note of 1995)", "READ",
     "p.42: (A) H(1-x) = H(x), (B) H(x+y) = H(y) + (1-y)H(x/(1-y)) + yH(-x/y) for y != 0,1, (C) xH(1/x) = -H(x), "
     "proved for H_p on Z/p; p.43: 'Claim: there is only one (up to a scalar factor) nonzero continuous solution of "
     "(A), (B), (C) in maps from R to itself', H_inf(x) = -(x log|x| + (1-x) log|1-x|), with a cohomological SKETCH: "
     "phi(x,y) = (x+y)H(x/(x+y)), set to 0 when x+y = 0; 'no non-trivial measurable cohomology classes in H^2(R,R)' "
     "asserted; psi_lambda(x) = psi(lambda x) - lambda psi(x) additive, linear for measurable maps; psi(x)/x = a log|x| + b; "
     "(C) 'irrelevant' to the argument; p.44: the chain rule for a variable with PROBABILITIES p_i, reduction to the "
     "two-valued case, 'well-defined iff (A) and (B)' stated as easily checked; p.10 Prop.2.13 (Elbaz-Vincent, Gangl): "
     "the differentiable case 'well-known (cf. [22])'; p.10-11 Rem.2.14: Aczel-Dhombres, locally integrable on ]0,1[; "
     "p.2: Cathelineau reached the same equation."),
    ("1903.06961v3", "Leinster, Entropy modulo a prime", "READ",
     "p.1-4 builds on Kontsevich's note; p.8 nonzero mod-p 'probabilities' can sum to zero; p.26 the reduction to "
     "two-element distributions, 'a similar reduction can be performed over R'; p.27: over R the binary Shannon "
     "function is, up to scale, the only measurable solution of the fundamental equation with F(0) = F(1), and "
     "Shannon entropy of finite REAL PROBABILITY distributions is characterised by measurability, symmetry and the "
     "chain rule (Lee 1964); Remark 9.6: symmetry is essential to fundamental-equation approaches (F(pi) = pi also "
     "solves (152))."),
    ("1402.3067v2", "Baez, Fritz, A Bayesian characterization of relative entropy (M-apply, 2026-10-03)", "READ",
     "p.1 S(q,p) = sum q ln(q/p), infinite where p = 0 < q, values in [0, inf]; p.2-3 FinStat (finite sets with "
     "PROBABILITY distributions; stochastic hypotheses s), RE a functor; p.3 lower semicontinuity, convex linearity; "
     "p.9 Def.6 FP (optimal hypotheses); p.11 Theorem 7: lower semicontinuous, convex linear functors FinStat -> [0, inf] "
     "vanishing on FP are c RE; p.13 P(X) = distributions in [0,1]; p.15 convex linearity computed; p.26-27 Petz's "
     "conditional-expectation law (5.1) and its gap.  Proved for probability measures only: nothing is inherited by "
     "signed ones."),
    ("2410.15976v5 (re-read)", "Brandenburger, La Mura, Axiom 5' (M-apply, 2026-10-03)", "READ",
     "p.3 eq.(9): numerator |w(P)| g(H(P)) + |w(Q)| g(H(Q)), denominator |w(P) + w(Q)|; p.4: why |w| (subsystem size) "
     "and why the summed denominator; p.2 eq.(1); p.4 Theorem 1 (alpha > 0, alpha != 1; alpha = 0 as Hartley); p.10-11 "
     "Lemmas A.1-A.5 (A.3: affine g excluded by A4 on (1/2,1/2) x (2,-1))."),
    ("AME2020 Table I (Wang, Huang, Kondev, Audi, Naimi, Chinese Physics C 45, 030003 (2021))", "the atomic mass table",
     "READ (board capture)", "not on arXiv (alphaXiv discovery search 2026-10-03 found no copy); READ as the board's "
     "capture extracted/.../captures/AME2020-TableI.tsv from the published PDF M supplied, through gravity.nuclides()."),
    ("NIST ASD ver. 5.12 (Kramida, Ralchenko, Reader, NIST ASD Team 2024)", "ionisation energies", "READ (board capture)",
     "IE-neutral-all.tsv (first IE, Z = 1-108) and LADDER-K-Kr.tsv (every charge, Z = 19-36), fetched 2026-08-11; "
     "not on arXiv."),
    ("Cathelineau, Math. Scand. 63 (1988); Ann. Inst. Fourier 46 (1996)", "the same equation from Hilbert's third "
     "problem / infinitesimal polylogarithms", "NAMED-NOT-READ", "cited math/0008089v1 p.2, 1903.06961v3 p.4."),
    ("Lee, Ann. Math. Stat. 35 (1964); Aczel-Dhombres (1989)", "fundamental equation; Cauchy's equation",
     "NAMED-NOT-READ", "READ only as cited: 1903.06961v3 p.27; math/0008089v1 p.10-11; 2410.15976v5 p.10 Lemma A.1."),
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
    rng4b = random.Random(20261004)             # a separate stream, so (4b) leaves every earlier number unchanged
    R["sep_sympy"] = sep_sympy()
    R["sep_z3"] = z3_obligations()
    R["sep_encoding_guard"] = encoding_guard(rng4b)
    R["sep_nullspace"] = separable_nullspace(rng4b)
    R["codomain_morphisms"] = codomain_morphisms()
    R["kontsevich"] = kontsevich_checks(rng4b)
    R["m_counterexample"] = m_uniqueness_counterexample(rng4b)
    R["indecomposable_census"] = indecomposable_census(rng4b)
    R["decomp_(1.6,-0.3,-0.3)"] = convex_decompositions([1.6, -0.3, -0.3])
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
    # (8)-(9), M-apply (2026-10-03): separate RNG streams, so every earlier number is unchanged
    R["weightings"] = weightings(random.Random(20261005))
    R["constants"] = read_constants()
    R["centred_apps"] = centred_applications()
    R["index_centred"] = index_centred()
    R["re_axioms"] = re_axioms(random.Random(20261006))
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
    print("\n(4b) separable functionals X = sum g(p_i) (H-SEPARABLE); Kontsevich's 1 1/2-logarithm")
    print("    sympy (solution identity, Re H convex-linear, N product excess):", R["sep_sympy"])
    print("    z3 obligations ('unsat' = proved; controls 'sat'):", R["sep_z3"] if R["sep_z3"] is not None else
          "SKIPPED: z3 not importable (pip install z3-solver)")
    print("    encoding guard:", R["sep_encoding_guard"])
    print("    numeric separable null space:", R["sep_nullspace"])
    print("    codomain morphisms:", [(m["name"], round(m["dReH"], 6), round(m["dN"], 6)) for m in R["codomain_morphisms"]])
    print("    Kontsevich (A),(B),(C), signed chain rule; N controls:", R["kontsevich"])
    print("    M-uniqueness counterexample g3:", R["m_counterexample"])
    print("    fraction of random signed measures with NO convex decomposition (n: fraction):", R["indecomposable_census"],
          "; (1.6,-0.3,-0.3):", R["decomp_(1.6,-0.3,-0.3)"])
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
    print("\n(8) both weightings carried (M item 2): the functional each selects, and its axioms (computed)")
    for k, v in R["weightings"].items():
        if k == "hartley_alpha0":
            print(f"    signed Hartley (alpha = 0): A3 {v['A3']}, A4 on (2,-1)x(2,-1) {v['A4_on_(2,-1)x(2,-1)']}")
            continue
        a = v["axioms"]
        print(f"    {k:<16} -> {v['functional']:<24} [{v['selection_status']}]")
        print(f"        A0 {a['A0_real_on_300_signed']}  A2' {a['A2_max_dev_from_-log2|p|']:.1e}  A3 {a['A3_H((1/2))']:.6f}"
              f"  A4 {a['A4_extensivity_worst']:.1e}  A5'(|w|) {a['A5_abs_weights_worst']:.2e} ({a['A5_abs_weights_undefined']} undefined)"
              f"  A5'(w) {a['A5_signed_weights_worst']:.2e} ({a['A5_signed_weights_undefined']} undefined)")
        print(f"        BFL convex linearity on FinProb, worst {v['BFL_convex_linearity_on_FinProb_worst']:.2e}; "
              f"crush (1.5,-0.5) loss {v['crush_loss_(1.5,-0.5)_bits']:+.6f} bits")
    print("\n(9) the ground-state calibration (M items 3, 6): default MASS/BINDING; GROUND-CONFIG and IONISATION selectable")
    k = R["constants"]
    print(f"    u = m_p + m_e - I(H) - Delta(1H) = {k['u_keV']:.4f} keV (DERIVED-FROM-READ); CODATA 2018 "
          f"{k['u_keV_CODATA2018']:.4f} (NAMED-NOT-READ); m_n via AME {k['m_n_via_AME_keV']:.4f} vs PDG {k['m_n_keV']:.4f}")
    for lab, v in R["centred_apps"].items():
        if "table" not in v:
            continue
        print(f"    [{v['calibration']}] {lab}: case {v['case']}, N {v['N_p']:.9f} (ground {v['N_p0']:.9f}); "
              f"B {v['B_state_keV']:.4f} keV (ground {v['B_ground_keV']:.4f})")
        print(f"        Re D(p||p0) {v['re_D']:.6e} nats, Im D {v['im_D']:.3e}; dRe H {v['dReH']:+.6e}; cross X "
              f"{v['cross_X']:+.6e}; identity residual {v['identity_residual']:.1e}; D(p0||p) "
              f"{'inf' if v['D_reverse'] is None else '%.6e' % v['D_reverse'].real}")
        t = v["table"]
        print(f"        Radon inverse error {t['radon_err_p']:.1e} (p), {t['radon_err_d']:.1e} (d); min line sum of p "
              f"{t['radon_min_line_p']:+.6f}; folded-renormalised D {t['fold_renormalised_D']}")
        print(f"        both weightings: {v['both_weightings']}")
        for r in t["rows"]:
            print("          " + "  ".join(f"{kk}={('%.6g' % vv) if isinstance(vv, float) else vv}" for kk, vv in r.items()))
    for cal, v in R["centred_apps"]["alternatives, Fe +1"].items():
        print(f"    [{cal}] Fe +1: N {v['N_p']}, Re D {v['re_D']:.6e}, dRe H {v['dReH']:+.6e}, X {v['cross_X']:+.6e}; "
              f"{v['info']}")
    print(f"    CONTROL another ground (Fe-54 vs Fe-56): {R['centred_apps']['CONTROL another ground: Fe-54 ground vs Fe-56 ground']}")
    print(f"    The Method's index (H-INDEX-GROUND-BOX / -LAMBDA): {R['index_centred']}")
    print(f"    is the centred measure a relative entropy? Re D_s against R0-R5: {R['re_axioms']}")
    print("\n(6) literature:")
    for L in R["literature"]:
        print(f"    [{L['status']}] {L['id']}: {L['title']}")


def selftest():
    R = build()
    res = []
    skipped = []

    def chk(name, ok, detail="", control=False, structural=False):
        res.append((name, bool(ok), control and not structural, structural))
        tag = "[STRUCTURAL: cannot fail, not evidence] " if structural else ("[CONTROL] " if control else "")
        print(f"  {'ok  ' if ok else 'FAIL'} {tag}{name}  {detail}")

    e = R["example"]
    print("(1) complex entropy")
    chk("Re H(1.5,-0.5) = -0.954771 nats (charter -0.95; task -0.9548)", abs(e["re_h_nats"] + 0.9547712) < 1e-6,
        f"{e['re_h_nats']:.7f}")
    chk("Im H = pi N on the principal branch", abs(e["H"][1] - PI * 0.5) < 1e-12, f"{e['H'][1]:.6f}")
    chk("Re H identical on every branch of the grid", max(abs(r["re"] - e["re_h_nats"]) for r in R["branch_grid"]) < 1e-12,
        "H() computes the real part -x ln|x| with no k in it (R3-alone relabel)", structural=True)
    g = {r["ks"]: r["im"] for r in R["branch_grid"]}
    chk("branch k on the NEGATIVE entry shifts Im H by -2 pi k p = +pi k (k=1), NOT 2 pi (D1)",
        abs(g[(0, 1)] - g[(0, 0)] - PI) < 1e-12 and abs(g[(0, 1)] - g[(0, 0)] - 2 * PI) > 1, f"{g[(0, 1)] - g[(0, 0)]:.6f}")
    chk("uniform branch shift k gives dIm = -2 pi k exactly (sum p = 1)",
        all(abs(u["dIm"] + 2 * PI * u["k"]) < 1e-12 for u in R["uniform_shift"]),
        "one line: -sum p_i 2 pi k = -2 pi k when sum p = 1 (R3-alone relabel)", structural=True)
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
    chk("N = (sum|p| - 1)/2", a["N_identity"] < 1e-12, "definitional: sum|p| = P + N, sum p = P - N = 1 (V2-0 relabel)",
        structural=True)
    ex = R["additivity_exact"]
    chk("sympy exact: Re residual 0, Im formula 0, M residual 0", ex["re_residual"] == "0" and
        ex["im_formula_residual"] == "0" and ex["M_residual"] == "0", str(ex))
    chk("Re H additivity FAILS when sum p = 2", R["additivity_unnormalised_control"] > 1e-3,
        f"{R['additivity_unnormalised_control']:.4f}", control=True)
    chk("M = 0 for a probability vector and > 0 with a negative entry", mana([0.2, 0.8]) == 0.0 and mana([1.1, -0.1]) > 0,
        "definitional: sum|p| = 1 + 2N (R3-alone relabel)", structural=True)
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
    print("(4b) separable functionals (H-SEPARABLE); Kontsevich's 1 1/2-logarithm")
    chk("step (0)-(1): F(f) = X(p) - X(q) and the convex-linearity identity on terminal maps", True,
        "restatements of functoriality and of the axiom", structural=True)
    sy = R["sep_sympy"]
    chk("sympy: g = a x ln|x| (+ beta x for x < 0) gives g(lam x) - lam g(x) = a lam ln(lam) x on each sign",
        sy["solution_identity_pos"] == "0" and sy["solution_identity_neg"] == "0", str(sy["solution_identity_neg"]))
    chk("sympy: Re H convex-linear on (1+s,-s), (1+t,-t), lam in (0,1): residual exactly 0",
        sy["ReH_convex_linear_residual"] == "0")
    chk("sympy: N(pq) - N(p) - N(q) = 2ab (so product additivity forces b = 0 in c Re H + b N)",
        sy["N_product_excess"] == "2*a*b", sy["N_product_excess"])
    Z = R["sep_z3"]
    if Z is None:
        print("  SKIP 6 z3 obligations (z3 not importable; pip install z3-solver).  NOT checked, NOT counted.")
        skipped.append(6)
    else:
        chk("Z3 step (2): g(1) = 0 and convex linearity at lam = 1 force g(0) = 0", Z["z3_g0"] == "unsat", Z["z3_g0"])
        chk("Z3 step (3): two convex-linearity instances force phi_lam(x) + phi_lam(y) = phi_lam(x + y)",
            Z["z3_cauchy"] == "unsat", Z["z3_cauchy"])
        chk("Z3 control: with one instance dropped the Cauchy step is NOT provable (countermodel)",
            Z["z3_cauchy_control_drop_instance_b"] == "sat", Z["z3_cauchy_control_drop_instance_b"], control=True)
        chk("Z3 vacuity guard: g = min(x, 0) (X = -N, non-zero) satisfies every premise for ALL lam in [0,1], x, y",
            Z["vacuity_minus_N_satisfies_premises_for_all"] == "unsat" and Z["vacuity_member_nonzero"] == "-1")
        chk("Z3 consequence: BFL's codomain on three morphisms forces c = 0 and b >= 0 (only b N survives)",
            Z["z3_codomain"] == "unsat" and Z["codomain_vacuity_b_positive_sat"] == "sat", Z["z3_codomain"])
        chk("Z3 control: without the merge-negatives morphism, c > 0 is consistent with the codomain",
            Z["codomain_control_without_merge_c_positive"] == "sat", "", control=True)
    eg = R["sep_encoding_guard"]
    chk("encoding guard: the encoded convex-linearity residual is ~0 on Re H's and on -N's g", eg["reh"] < 1e-12 and
        eg["minusN"] < 1e-12, f"{eg['reh']:.1e}, {eg['minusN']:.1e}")
    chk("encoding guard control: g = x^2 leaves a residual (the encoding can fail)", eg["x2_min"] > 1e-3,
        f"min {eg['x2_min']:.3f}", control=True)
    sn = R["sep_nullspace"]
    chk("numeric: a 14-function separable basis has convex-linear null space = span{Re H, N}",
        sn["null_dim"] == 2 and sn["null_outside_span_ReH_N"] < 1e-9 and sn["span_ReH_N_outside_null"] < 1e-9,
        f"dim {sn['null_dim']}, residuals {sn['null_outside_span_ReH_N']:.1e} / {sn['span_ReH_N_outside_null']:.1e}")
    chk("numeric control: without the convex-linearity rows the null space has dimension 13",
        sn["control_null_dim_without_CL_rows"] == 13, "", control=True)
    k = R["kontsevich"]
    chk("Kontsevich (A), (B), (C) hold for Re H on two entries over random reals (math/0008089v1 p.42, READ)",
        max(k["A"], k["B"], k["C"]) < 1e-12, f"(B) {k['B']:.1e}")
    chk("chain rule with SIGNED outer weights holds for Re H (p.44's reduction, applied to signed weights)",
        k["chain"] < 1e-12, f"{k['chain']:.1e}")
    chk("control: N fails Kontsevich's (B) (x = 0.5, y = -1: 0.5 vs 1.0) and the signed-weight chain rule",
        k["B_N_max"] > 0.1 and k["chain_N_max"] > 0.1 and abs(k["B_N_instance"]["lhs"] - k["B_N_instance"]["rhs"]) > 0.1,
        f"(B) {k['B_N_max']:.3f}, chain {k['chain_N_max']:.3f}", control=True)
    mc = R["m_counterexample"]
    chk("M is NOT the unique product-additive functional vanishing on probabilities: g3 = ln(sum|p|^3/|sum p^3|)",
        mc["product_residual"] < 1e-11 and mc["on_probabilities_max"] < 1e-12 and abs(mc["g3_(1.5,-0.5)"] - mc["M_(1.5,-0.5)"]) > 0.1,
        f"g3(1.5,-0.5) = {mc['g3_(1.5,-0.5)']:.4f} vs M = {mc['M_(1.5,-0.5)']:.4f}")
    ic = R["indecomposable_census"]
    chk("every n = 2 signed measure is a convex atom (block totals 1+N and -N)", ic[2] == 1.0, "", structural=True)
    chk("(1.6, -0.3, -0.3) has no convex decomposition; at n = 3 about half of random signed measures have none",
        R["decomp_(1.6,-0.3,-0.3)"] == [] and 0.2 < ic[3] < 0.9, f"n=3: {ic[3]:.3f}, n=5: {ic[5]:.3f}")
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
    chk("uniform measure on Lambda: Re H = log2 976 = A3's 9.930737 bits", abs(al["uniform_re_h_bits"] - al["A3_bits_per_cell"]) < 1e-12,
        "Re H of a uniform non-negative vector is ln n by definition; the count 976 is checked above (V2-0 relabel)",
        structural=True)
    chk("the Mobius weighting of Lambda is signed (N > 0)", al["N_p"] > 0, f"N_p = {al['N_p']:.4f}")
    ac = R["app_lambda_box_control"]
    chk("a full box has a one-point Mobius weight, N = 0", ac["support"] == 1 and ac["N_p"] == 0, control=True)
    print("(8) both weightings carried (M item 2)")
    W = R["weightings"]
    ws = W["signed w"]["axioms"]
    chk("signed w -> Re H: A0 real, A2' H((p)) = -log2|p|, A3 = 1, A4 extensive, A5' with SIGNED weights exact",
        ws["A0_real_on_300_signed"] and ws["A2_max_dev_from_-log2|p|"] < 1e-12 and abs(ws["A3_H((1/2))"] - 1) < 1e-12
        and ws["A4_extensivity_worst"] < 1e-9 and ws["A5_signed_weights_worst"] < 1e-9,
        f"A4 {ws['A4_extensivity_worst']:.1e}, A5'(w) {ws['A5_signed_weights_worst']:.1e}")
    chk("Re H FAILS A5' with |w| weights (BLM's eq.(9), READ p.3)", ws["A5_abs_weights_worst"] > 1e-2,
        f"worst {ws['A5_abs_weights_worst']:.3f}", control=True)
    for a in WEIGHTING_ALPHAS:
        wa = W[f"|w|, alpha = {a}"]["axioms"]
        chk(f"|w| -> signed Renyi H_{a}: A0, A2', A3, A4 and A5' with |w| weights exact (tests the reading of eq.(9))",
            wa["A0_real_on_300_signed"] and wa["A2_max_dev_from_-log2|p|"] < 1e-12 and abs(wa["A3_H((1/2))"] - 1) < 1e-12
            and wa["A4_extensivity_worst"] < 1e-9 and wa["A5_abs_weights_worst"] < 1e-9 and wa["A5_abs_weights_undefined"] == 0,
            f"A5'(|w|) {wa['A5_abs_weights_worst']:.1e}")
        chk(f"signed Renyi H_{a} FAILS A5' with signed weights (residual or undefined g^-1)",
            wa["A5_signed_weights_worst"] > 1e-2 or wa["A5_signed_weights_undefined"] > 0,
            f"worst {wa['A5_signed_weights_worst']:.3f}, undefined {wa['A5_signed_weights_undefined']}", control=True)
        chk(f"on probability measures H_{a} is not BFL's Shannon: it fails BFL convex linearity",
            W[f"|w|, alpha = {a}"]["BFL_convex_linearity_on_FinProb_worst"] > 1e-2,
            f"{W[f'|w|, alpha = {a}']['BFL_convex_linearity_on_FinProb_worst']:.3f}")
    chk("Re H (BLM-normalised) keeps BFL convex linearity on FinProb", W["signed w"]["BFL_convex_linearity_on_FinProb_worst"]
        < 1e-12, f"{W['signed w']['BFL_convex_linearity_on_FinProb_worst']:.1e}")
    chk("signed Hartley (alpha = 0): A3 = 1 and A4 on (2,-1)x(2,-1) = 0", abs(W["hartley_alpha0"]["A3"] - 1) < 1e-12 and
        abs(W["hartley_alpha0"]["A4_on_(2,-1)x(2,-1)"]) < 1e-12)

    print("(9) the ground-state calibration (M items 3, 6)")
    k = R["constants"]
    chk("u derived from READ values (m_p + m_e - I(H) - Delta(1H)) agrees with CODATA 2018 within 2 eV (PDG rounds m_p to 1 eV)",
        abs(k["u_keV"] - k["u_keV_CODATA2018"]) < 2e-3, f"{(k['u_keV'] - k['u_keV_CODATA2018']) * 1e3:+.3f} eV")
    chk("m_n by two READ routes (PDG; u + Delta(n) from AME) agrees within 2 eV", abs(k["m_n_via_AME_keV"] - k["m_n_keV"]) < 2e-3,
        f"{(k['m_n_via_AME_keV'] - k['m_n_keV']) * 1e3:+.3f} eV")
    ie, first = ionisation_ev()
    chk("NIST: Fe I's IE in the ladder capture equals the neutral-row capture", abs(ie[(26, 0)][0] - first[26][0]) < 1e-6,
        f"{ie[(26, 0)][0]} vs {first[26][0]} eV")
    A = R["centred_apps"]
    fe0, fe1, fe26 = A["Fe-56 ground (element; centre)"], A["Fe-56 +1 (ion)"], A["Fe-56 +26 (bare nucleus)"]
    gr = _board_mod("gravity")
    b_ame = 26 * k["Delta_1H_keV"] + 30 * k["Delta_n_keV"] - mass_excess_keV(26, 56)[0]
    chk("Fe-56: B by the four-cell route = AME's B (Z Delta_H + N Delta_n - Delta) + Z I(H), within N x 2 eV",
        abs(fe0["B_ground_keV"] - b_ame - 26 * k["I_H_eV"] / 1000) < 30 * 2e-3,
        f"{fe0['B_ground_keV']:.4f} vs {b_ame + 26 * k['I_H_eV'] / 1000:.4f} keV")
    chk("each weighting totals 1 (B is defined as the shortfall)", all(abs(sum(v["p"]) - 1) < 1e-12 and abs(sum(v["p0"]) - 1)
        < 1e-12 for v in A.values() if "p" in v), structural=True)
    chk("H-1 ground: B = I(H) exactly (u was defined through M(1H))", abs(A["H-1 +1 (the proton)"]["B_ground_keV"] -
        k["I_H_eV"] / 1000) < 1e-9, structural=True)
    chk("the element's ground is a quasi-probability: exactly one negative cell, the binding (Fe-56, C-12)",
        fe0["case"] == "SIGNED" and sum(1 for x in fe0["p0"] if x < 0) == 1 and fe0["p0"][3] < 0
        and A["C-12 +1 (ion)"]["p0"][3] < 0, f"N(Fe-56) = {fe0['N_p0']:.9f}")
    chk("the proton (H-1 +1) carries no binding: case SHANNON, N = 0", A["H-1 +1 (the proton)"]["case"] == "SHANNON")
    chk("at the ground, D(p0||p0) = 0, dRe H = 0, every deviation 0 (the required value at p = p0)",
        fe0["re_D"] == 0 and fe0["im_D"] == 0 and fe0["dReH"] == 0 and all(r["d=p-p0"] == 0 for r in fe0["table"]["rows"]),
        "ln(x/x) = 0 by definition", structural=True)
    ctl = A["CONTROL another ground: Fe-54 ground vs Fe-56 ground"]
    chk("CONTROL: a different ground (Fe-54's state against Fe-56's ground) gives D != 0", ctl["re_D"] > 1e-6,
        f"{ctl['re_D']:.3e} nats", control=True)
    apps = [v for v in A.values() if "table" in v]
    chk("the identity Re H(p0) - Re H(p) = Re D + X holds on every application (DERIVED, checked)",
        all(abs(v["identity_residual"]) < 1e-12 for v in apps), f"max {max(abs(v['identity_residual']) for v in apps):.1e}")
    chk("TEST: the ground-centred entropy deviation is NOT a relative entropy -- for Fe +1, dRe H != -Re D (X != 0)",
        abs(fe1["dReH"] + fe1["re_D"]) > 1e-6 and abs(fe1["cross_X"]) > 1e-6,
        f"dRe H {fe1['dReH']:+.3e} vs -Re D {-fe1['re_D']:+.3e}; X {fe1['cross_X']:+.3e}")
    chk("Fe +1 and Fe +26 (MASS/BINDING): D(p||p0) > 0, signs agree cell by cell (Im D = 0), binding falls by sum IE",
        fe1["re_D"] > 0 and fe26["re_D"] > fe1["re_D"] and fe1["im_D"] == 0 and fe26["im_D"] == 0 and
        abs(fe0["B_ground_keV"] - fe1["B_state_keV"] - fe1["sum_IE_keV"]) < 1e-6,  # keV; float floor ~5e-9 at M ~ 5e7 keV
        f"Re D {fe1['re_D']:.3e} / {fe26['re_D']:.3e} nats")
    chk("Radon inverse on Z_2^2 recovers every cell and every deviation exactly", all(v["table"]["radon_err_p"] < 1e-14 and
        v["table"]["radon_err_d"] < 1e-14 for v in apps))
    chk("but the positive-projection triangulation does not hold for H-MASS-CELLS: a line sum of the ground is negative",
        fe0["table"]["radon_min_line_p"] < 0, f"min {fe0['table']['radon_min_line_p']:+.6f}")
    alt = A["alternatives, Fe +1"]
    chk("alternatives selectable: GROUND-CONFIG and IONISATION give non-negative weights (Shannon case), finite D",
        all(v["N_p"] == 0 and v["re_D"] is not None and v["re_D"] > 0 for v in alt.values()),
        f"{ {c: round(v['re_D'], 6) for c, v in alt.items()} }")
    chk("populate.series_limit banks no stage of Fe (reported, not filled in)", alt["IONISATION"]["info"]
        ["populate_series_limit_banked"] == {})
    refused = []
    for args in ((6, 12, 0, "IONISATION"), (6, 12, 2, "MASS/BINDING")):
        try:
            calibrate(args[0], args[1], args[2], args[3])
        except KeyError:
            refused.append(args)
    chk("an unread value is not filled in: C's full ladder and C II's IE are NOT READ, and both calls refuse",
        len(refused) == 2, str(refused), control=True)
    ix = R["index_centred"]
    chk("index, H-INDEX-GROUND-BOX: dRe H = -Re D exactly (X = 0: |p0| constant, both totals 1); Re D = log2 6912 for the Mobius p",
        abs(ix["mobius_p"]["dReH_vs_box_bits"] + ix["mobius_p"]["D_vs_box_bits"]) < 1e-9 and
        abs(ix["mobius_p"]["D_vs_box_bits"] - math.log2(6912)) < 1e-9, f"{ix['mobius_p']['D_vs_box_bits']:.6f} bits")
    chk("index, H-INDEX-GROUND-LAMBDA: D is infinite -- 288 of the Mobius weight's 317 cells lie outside Lambda",
        ix["support_outside_lambda"] == 288 and ix["mobius_p"]["D_vs_lambda"] is None, f"{ix['support_in_lambda']} inside")
    chk("D(uniform Lambda || uniform box) = A3's closure bits log2(6912/976)", abs(ix["uniform_lambda_vs_box_bits"] -
        ix["A3_closure_bits"]) < 1e-12, f"{ix['uniform_lambda_vs_box_bits']:.6f}")
    ra = R["re_axioms"]
    chk("R1 Gibbs: Shannon pairs D >= 0 (control set)", ra["R1_shannon_min"] >= 0, f"min {ra['R1_shannon_min']:.2e}")
    chk("R1 Gibbs FAILS on signed pairs, with the reference signed and with the state signed",
        ra["R1_signed_min"] < 0 and ra["R1_reference_signed_(0.5,0.5)||(1.5,-0.5)"] < 0 and
        ra["R1_state_signed_(1.5,-0.5)||(0.9,0.1)"] < 0, f"{ra['R1_reference_signed_(0.5,0.5)||(1.5,-0.5)']:.4f}, "
        f"{ra['R1_state_signed_(1.5,-0.5)||(0.9,0.1)']:.4f}")
    chk("R2 product additivity holds for Re D_s (totals 1)", ra["R2_re_worst"] < 1e-9, f"{ra['R2_re_worst']:.1e}")
    chk("R2 CONTROL: a factor of total 2 breaks it", ra["R2_control_total2_worst"] > 1e-3, control=True)
    chk("R2 does NOT hold for Im D_s (sign mismatches do not factor)", ra["R2_im_worst"] > 1e-3, f"{ra['R2_im_worst']:.3f}")
    chk("R3 data processing: 0 Shannon violations; signed violations found", ra["R3_shannon_violations"] == 0 and
        ra["R3_signed_violations"] > 0, f"signed {ra['R3_signed_violations']}")
    chk("R4 convex linearity (BF p.3) holds for D_s, Re and Im", ra["R4_convex_worst"] < 1e-9, f"{ra['R4_convex_worst']:.1e}")
    chk("R5 chain rule (conditional-expectation law) holds for Re D_s", ra["R5_chain_rule_re_worst"] < 1e-9,
        f"{ra['R5_chain_rule_re_worst']:.1e}")
    n_ctrl = sum(1 for r in res if r[2])
    n_struct = sum(1 for r in res if r[3])
    n_fail = sum(1 for r in res if not r[1])
    n_counted = len(res) - n_struct
    n_cfail = sum(1 for r in res if not r[1] and not r[3])
    print(f"\n{n_counted - n_cfail}/{n_counted} counted checks pass ({n_ctrl} of them controls); {n_struct} STRUCTURAL "
          f"(cannot fail; printed, not counted); {sum(skipped)} SKIPPED; {n_fail} failed in all")
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
