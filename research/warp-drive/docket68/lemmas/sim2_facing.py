#!/usr/bin/env python3
"""sim2_facing.py -- B4d simulation, phase 2, first instrument (M-RULINGS item 168): can two pieces of our one plane
face each other across a static bulk?  Computed, READ and deduced; not verified; not seated.  First headed "... not
verified; not seated".

M's words (verbatim in the rulings file; quoted in SIM2-FACING.md, never paraphrased as M's): item 168 "My sense:
positions, one universe"; 152 (1) "two separate positions connected by/reached through a dimension." and (2) "It could
very well be possible, so let's consider this an option and check it."; 126; 127 (1) "1 - yes"; 116 (a) "No, separate"
and (b); 117 and 120 (the NEC "appears broken, but is not"); 123 "forget the coin metaphor."; 118 "Yes: law and
history"; 119; 129 (1); 130 (1) "no added matter"; 136 (2) "released at position two at the closing of the horizon" and
(3) "It is a bridge, not a physical place."; 138; 139 (1), (2), (4); 140; 141 "I suggest the planes are static"; 143 A;
155 (2) "Yes, in bits"; 157; 158 (4); 161; 162; 166 "Both planes at once"; 101 (7).  Items 169-171 (2026-10-09) bear on
why this phase is static at one moment: 169 (no travel through time alone), 170 (the world on position 2's clock, the
object keeping position 1's), 171 (space-only teleportation is this phase).  The theorem's clause (B): "A vacuum
five-dimensional bulk carries the corridor. The plane is free of matter, at the Randall-Sundrum tension."

THE SETUP.  Units m = 1, e = m/ell, nu = 2/kappa_5^2 (one-sided Israel factor).  Static SO(3) bulk, vacuum, Lambda_5 =
-6/ell^2: ds^2 = dy^2 - A dt^2 + B dr^2 + C dOmega^2, grown from eq. (17) on position 1's piece P1 (y = 0, clause (B),
157) by b4_static.series (exact, rational).  kappa_X = (1/2) d_y ln X; a = (kappa_t + kappa_r + 2 kappa_th)/4,
a~ = a + 1/ell; the wall coefficients w_r = kappa_r - kappa_t, w_th = kappa_th - kappa_t (the warp cancels from both and
from a~).  Position 2's piece P2 is a second piece of the same mirrored plane, one-sided toward the slab
(H-Z2-PIECES); it faces P1 when its bulk nearest approach p2 = (r2, depth) is attained in the static region
(H-NEAREST-APPROACH) -- a depth is a property of the bulk, never the corridor's length (155: bits) and never an output
called a distance (139 (4), 101 (7)).  Junction, normal into the slab: S^a_b = -nu (K^a_b - delta K); for a static P2,
rho + p_i = nu (k_t - k_i) for any tension (the local Israel lemma).

  S1  LEMMA T, THE RICCATI TRAP (deduced; T1 computed exactly on the owner's series).  a' = 1/ell^2 - a^2 - Pi.Pi/4
      (5D Raychaudhuri, R_yy = -4/ell^2); Pi.Pi >= 0 (static: K diagonal); a(0) = -1/ell (Gauss, R4 = 0); so a~ <= 0 at
      every depth the Gaussian chart reaches.  Anchor: a~ = -(R_ab R^ab/12)(y^3 + 5 e y^4) + O(y^5).
  S2  LEMMA C, COMPARISON AT THE NEAREST POINT (deduced; the comparison step standard-not-READ): k_t(P2) = -kappa_t,
      k_spatial(P2) >= -kappa_spatial at p2.
  S3  COROLLARY T5c (deduced): a matter-free mirrored P2 reads s2 <= ell a(depth) <= -1, every depth, every ell.  Within
      one universe under clause (B) two matter-free pieces of our plane cannot face each other: decided.
  S4  LEMMA W (deduced): a static mirrored P2 whose total stress obeys the NEC, nearest approach in the static region,
      needs w_r >= 0 and w_th >= 0 there -- any tension, any matter split, no bulk field equation used.
  S5  LEADING ORDERS (computed, exact): w_r = R_rad (y + 3 e y^2), w_th = R_tan (y + 3 e y^2) + O(y^3);
      R_rad = -2m(r - 2m)/(r^2 (2r - 3m)^2) < 0, R_tan = m/(r (2r - 3m)^2) > 0 (sim1_transition.static_nec).
  S6  THE THROAT (STRUCTURAL + computed): eq. (17) at r = 2m is AdS2(2m) x S2(2m); over it the bulk is homogeneous and
      w_r = 0 by the AdS2 boost.
  S7  THE THROAT BULK (computed by ODE, constraint to 3e-12 relative): y_s^th = 2.5536, 2.3744, 2.2247, 1.9868, 1.6591,
      1.2803, 0.9139, 0.6101, 0.3864m at ell = inf, 32m, 16m, 8m, 4m, 2m, m, m/2, m/4 (alpha -> 0; K diverges); a~ <= 0;
      w_th > 0; the level-set stress rho = nu (p + 2q), rho + p_r = 0, rho + p_th = nu (q - p).
  S8  THE FIRST CORRECTION IN x = r - 2m (computed): w_r = x W1(y) + O(x^2); y* = first zero of W1 = 1.7901, 1.7286,
      1.6720, 1.5709, 1.4053, 1.1673, 0.8812, 0.6042, 0.3856m (y*/y_s 0.701 to 0.998); the band [y*, y_s^th); K(y*)/K_bs
      18.3 to 5.9e8; rho_m(y*) = +0.1215 nu/m flat, -0.73 to -36.5 sigma_RS at finite ell; positive energy needs
      ell >= ell_W = 49.86m; the edge lies below 30 K_bs for ell > 21.05m, below 100 K_bs for ell > 5.82m, never below 10.
  S9  THE MAP ON THE OWNER'S BULK (computed; raw Pade as evidence): 13 radii x 9 ell at order 32, banked: 4406 verified
      points; at every one of the 3861 at r >= 2.05m or ell <= 2m, w_r < 0, w_th > 0, a~ < 0; w_r >= 0 only at r <= 2.02m
      and ell >= 4m, past a sign change at 1.821, 1.758, 1.700, 1.597, 1.428m (r = 2.005m, ell = inf to 4m).
  S10 THROAT AND OWNER AGREE (computed): the sign change extrapolated to x -> 0 meets y* to 0.1%; W1(1.088) to 0.5%; the
      x -> 0 extrapolation of w_th, a~ to 0.2%; y_s^th 1-3% below the near-throat columns' Pade singularity.
  S11 LEMMA N (deduced; sympy): Gamma^y_ab = -(1/2) d_y g_ab; a radial null ray tangent to a level set has
      y'' = w_r B r'^2.  Corollary W: warped products have w = 0 (the black string, RS2).
  S12 THE DECISION per ell (WIDE / THROAT-BAND / NONE), from S7-S9: THROAT-BAND at every ell -- CONFIRMED on the owner's
      bulk at ell >= 4m, EXPANSION-ONLY at ell <= 2m (the r = 2.005m column's verified top lies below y*: not
      reached); regular at 30 and 100 K_bs for ell = inf, 32m, at 100 only for 16m, 8m, at none for ell <= 4m;
      positive energy only at ell >= 49.86m.
  S13 THE HAND-OFF TO PHASE 3 (deduced): s_slab = ell a(depth) <= -1; the outer side needed for 139's figures.
  S14 THE ESCAPES LEFT (STRUCTURAL / OPEN).
  The computed branch (S4, S7-S12) rests on the board's H-README-ON-P2, which conflicts with 130 (1) and 136 (2) as M
  worded them; it is necessary, not sufficient, and never B4d green.

Owners imported by path (never copied): b4_static.py (series, _eq17, _schwarzschild, pade), b4d_stage5.py (warped,
orders, _approx, nearest_real, evaluator for K only, k_bs, wall_exact; _clean only in C5's mutation), b4d_stage6.py
(sigma_over_rs), b4d_stage7.py (ricci_squared, slab_trace), sim1_transition.py (static_nec, eq17_rkk).
Needs python-flint, sympy, numpy, scipy, mpmath.
python3 sim2_facing.py [--selftest] [--regenerate]   (selftest about 2 min; regenerate about 22 min on 3 CPUs, 40 CPU-min)
"""
import contextlib
import importlib.util
import inspect
import io
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr
from multiprocessing import Pool

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
BANK = os.path.join(HERE, "sim2_bank.json")
ORDER = 32
ES2 = [Fr(0), Fr(1, 32), Fr(1, 16), Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(4)]
RADII2 = ["401/200", "201/100", "101/50", "41/20", "21/10", "43/20", "11/5", "23/10", "5/2", "3", "4", "5", "10"]
NGRID = 40                  # S9's y grid
VAL_TOL = 1e-4              # two Pade orders agree on A, B, C (b4_static S3's criterion)
W_ABS, W_REL = 1e-6, 1e-3   # and on w_r, w_th (this instrument's addition; it can only remove points)
DOUBLET = 2e-3              # a real pole with a zero this close is a Froissart doublet (b4d_stage5.nearest_real's rule)
CAP = 10.0                  # scan cap in m
WIDE_R = 2.1                # S12: WIDE needs an admissible point at r_c >= 2.1m
NEAR_R = 2.02               # S12: CONFIRMED needs an owner column at r_c <= 2.02m ...
CONFIRM_TOL = 0.05          # ... admissible within 5% of the throat's y*
KF = (10, 30, 100)          # thresholds of K/K_bs, reported together with the strict y < y_s
ALPHA_END = 1e-9            # y_s^th: alpha -> 0 (converged to 1e-7 m by alpha = 1e-6)
ALPHA_FULL = 1e-6           # the O(x) system is followed to alpha = 1e-6
BANNED_KEYS = ("dist", "separation", "time", "redshift", "speed", "velocity", "length", "clock", "arrival")
BANNED_ARGS = {"d", "D", "sep", "separation", "distance", "dist", "gap", "length", "time", "speed", "velocity",
               "redshift", "arrival"}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


B4 = _load(os.path.join(HERE, "b4_static.py"), "sim2_b4static")
S5 = _load(os.path.join(HERE, "b4d_stage5.py"), "sim2_stage5")
S6 = _load(os.path.join(HERE, "b4d_stage6.py"), "sim2_stage6")
S7 = _load(os.path.join(HERE, "b4d_stage7.py"), "sim2_stage7")
SIM1 = _load(os.path.join(HERE, "sim1_transition.py"), "sim2_sim1")

_NEC = {}


def _nec():
    """sim1_transition.static_nec (eq. (17)'s Weyl fluid: rho, p_r, p_t and the radial/tangential NEC sums), cached."""
    if not _NEC:
        _NEC.update(SIM1.static_nec())
    return _NEC


_RKK = {}


def rkk_closed(rc):
    """sim1_transition.eq17_rkk: eq. (17)'s radial null Ricci R_kk (k = (1/sqrt F, sqrt H)), at r = rc -- R_rad's sign."""
    if not _RKK:
        Rkk, resid = SIM1.eq17_rkk()
        _RKK.update({"Rkk": Rkk, "resid": resid})
    rs = [s for s in _RKK["Rkk"].free_symbols if s.name == "r"][0]
    return sp.nsimplify(_RKK["Rkk"].subs(rs, sp.Rational(rc))), _RKK["resid"]


def r_hat(rc):
    """R_rad = R^r_r - R^t_t = 8 pi (rho + p_r) and R_tan = R^th_th - R^t_t = 8 pi (rho + p_t) of eq. (17), exact."""
    n = _nec()
    rs = [s for s in n["radial"].free_symbols if s.name == "r"][0]
    rv = sp.Rational(rc)
    return sp.nsimplify(8 * sp.pi * n["radial"].subs(rs, rv)), sp.nsimplify(8 * sp.pi * n["tangential"].subs(rs, rv))


# ------------------------------------------------------------------------------------------------ exact series helpers
def _deriv(c):
    return [k * c[k] for k in range(1, len(c))]


def _mul(a, b, n):
    return [sum((a[i] * b[k - i] for i in range(k + 1) if i < len(a) and k - i < len(b)), Fr(0)) for k in range(n + 1)]


def _div(a, b, n):
    out = []
    for k in range(n + 1):
        s = (a[k] if k < len(a) else Fr(0)) - sum((b[j] * out[k - j] for j in range(1, k + 1) if j < len(b)), Fr(0))
        out.append(s / b[0])
    return out


def kappas(rc, e, N):
    """Exact Taylor series (orders 0..N-1) of kappa_t, kappa_r, kappa_th = (1/2) d_y ln X on the owner's series."""
    S = B4.series(rc, N, e)
    out = {}
    for X in "ABC":
        c = [Fr(v) for v in S[X][0][:N + 1]]
        out[X] = [v / 2 for v in _div(_deriv(c), c, N - 1)]
    return out


# ------------------------------------------------------------------------------------------------ S1 Lemma T
def riccati_identity(rc, e, N=14, ryy_sign=-1):
    """T1 on the owner's exact series: the coefficients of a' - (1/ell^2 - a^2 - Pi.Pi/4) through y^(N-2).  ryy_sign is
    the sign of R_yy = ryy_sign 4/ell^2 (the vacuum has -1; +1 is C3's mutation)."""
    k = kappas(rc, e, N)
    n = N - 2
    a = [(k["A"][j] + k["B"][j] + 2 * k["C"][j]) / 4 for j in range(N)]
    Pi = {X: [k[X][j] - a[j] for j in range(N)] for X in "ABC"}
    PiPi = [u + v + 2 * w for u, v, w in zip(_mul(Pi["A"], Pi["A"], n), _mul(Pi["B"], Pi["B"], n),
                                              _mul(Pi["C"], Pi["C"], n))]
    aa = _mul(a, a, n)
    ee = Fr(e) ** 2
    rhs = [(-ryy_sign * ee if j == 0 else Fr(0)) - aa[j] - PiPi[j] / 4 for j in range(n + 1)]
    ap = _deriv(a)
    return [ap[j] - rhs[j] for j in range(n + 1)]


def lemma_t():
    """T1-T4 as symbolic statements: the Raychaudhuri split, the Riccati comparison and its fixed point at s1 = 1."""
    kt, kr, kq, ee, s1, Y = sp.symbols("k_t k_r k_q e s_1 Y", real=True)
    a = (kt + kr + 2 * kq) / 4
    split = sp.expand((kt**2 + kr**2 + 2 * kq**2) - (4 * a**2 + (kt - a)**2 + (kr - a)**2 + 2 * (kq - a)**2))
    ep = sp.Symbol("e", positive=True)
    comp = ep * sp.tanh(ep * Y - sp.atanh(s1))                 # solves b' = e^2 - b^2, b(0) = -e s1
    ode = sp.simplify(sp.diff(comp, Y) - (ep**2 - comp**2))
    start = sp.simplify(comp.subs(Y, 0) + ep * s1)
    fixed = sp.limit(comp, s1, 1, "-")                          # s1 = 1: the depth drops out
    return {"split": split, "ode": ode, "start": start, "fixed_point": sp.simplify(fixed / ep)}


# ------------------------------------------------------------------------------------------------ S3 Corollary T5c
def t5c(e):
    """s2 <= ell a(depth) <= -1 for a matter-free mirrored P2 facing P1 (one-universe law, s1 = 1); the general bound
    s2 <= tanh(depth/ell - artanh s1) for the controls.  Symbolic in the depth Y."""
    s1, Y = sp.symbols("s_1 Y", real=True)
    gen = sp.tanh(Y * sp.Rational(Fr(e).numerator, Fr(e).denominator) - sp.atanh(s1)) if e != 0 else None
    at_rs = sp.limit(gen, s1, 1, "-") if gen is not None else sp.Integer(-1)
    return {"general": gen, "at_s1_1": at_rs, "s2_max": sp.Integer(-1)}


# ------------------------------------------------------------------------------------------------ S4 Lemma W
def israel(K, nu=1, trace_from=0):
    """One-sided Israel: S^a_b = -nu (K^a_b - delta K); K the mixed diagonal (k_t, k_r, k_th, k_ph).  Returns rho and
    the pressures p_i = S^i_i.  trace_from = 1 (the trace over the spatial part only) is C2's mutation."""
    tr = sum(K[trace_from:])
    S = [-nu * (k - tr) for k in K]
    return -S[0], S[1:]


def lemma_w(kt, kr, kth):
    """At a nearest point p2 with the bulk's kappa_t, kappa_r, kappa_th: Lemma W's necessary condition for a static
    mirrored P2 whose total stress obeys the NEC (any tension, any matter split)."""
    w_r, w_th = kr - kt, kth - kt
    return {"w_r": w_r, "w_th": w_th, "admissible": bool(w_r >= 0 and w_th >= 0)}


def lemma_w_proof(n_trials=20000, seed=7, flip=False):
    """W's step, exact and sampled: with k_t = -kappa_t and k_spatial = -kappa_spatial + H (H >= 0, any symmetric 3x3),
    k_t I - k_spatial = diag(w) - H, so NEC (k_t I >= k_spatial) forces diag(w) >= H >= 0.  Sampled over random kappa and
    H; flip = True reverses the comparison (H <= 0), which must produce counterexamples."""
    w1, w2 = sp.symbols("w_1 w_2", real=True)
    kt_, kr_, kq_ = sp.symbols("kappa_t kappa_r kappa_q", real=True)
    Hs = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (min(i, j), max(i, j)), real=True))
    lhs = (-kt_) * sp.eye(3) - (-sp.diag(kr_, kq_, kq_) + Hs)
    exact = sp.simplify(lhs - (sp.diag(kr_ - kt_, kq_ - kt_, kq_ - kt_) - Hs)) == sp.zeros(3, 3)
    rng = np.random.default_rng(seed)
    bad = nec = 0
    for _ in range(n_trials):
        kap = rng.normal(size=3)
        M = rng.normal(size=(3, 3))
        H = 0.3 * M @ M.T * (-1 if flip else 1)
        k_sp = -np.diag([kap[1], kap[2], kap[2]]) + H
        if np.all(np.linalg.eigvalsh((-kap[0]) * np.eye(3) - k_sp) >= 0):
            nec += 1
            if not (kap[1] - kap[0] >= 0 and kap[2] - kap[0] >= 0):
                bad += 1
    return {"exact": exact, "nec_samples": nec, "counterexamples": bad}


# ------------------------------------------------------------------------------------------------ S5 leading orders
def leading_coefficients(rc, e, N=8):
    """Exact y^0..y^4 coefficients of w_r, w_th and a~ on the owner's series, with eq. (17)'s R_rad, R_tan and
    R_ab R^ab."""
    k = kappas(rc, e, N)
    wr = [k["B"][j] - k["A"][j] for j in range(5)]
    wth = [k["C"][j] - k["A"][j] for j in range(5)]
    at = [(k["A"][j] + k["B"][j] + 2 * k["C"][j]) / 4 + (Fr(e) if j == 0 else 0) for j in range(5)]
    Rr, Rt = r_hat(rc)
    _, RR = S7.ricci_squared(sp.Rational(rc))
    return {"wr": wr, "wth": wth, "at": at, "R_rad": Rr, "R_tan": Rt, "RR": sp.nsimplify(RR)}


def check_leading(rc, e):
    """C4: S5's coefficients exact, and against the owners (wall_exact for w_r, slab_trace for a~)."""
    L = leading_coefficients(rc, e)
    ee = sp.Rational(Fr(e).numerator, Fr(e).denominator)
    q = lambda v: sp.Rational(v.numerator, v.denominator)
    ok = (q(L["wr"][0]) == 0 and q(L["wr"][1]) == L["R_rad"] and q(L["wr"][2]) == 3 * ee * L["R_rad"]
          and q(L["wth"][0]) == 0 and q(L["wth"][1]) == L["R_tan"] and q(L["wth"][2]) == 3 * ee * L["R_tan"]
          and all(q(L["at"][j]) == 0 for j in range(3)) and q(L["at"][3]) == -L["RR"] / 12
          and q(L["at"][4]) == -5 * ee * L["RR"] / 12)
    w0, w1, w2, R4 = S5.wall_exact(Fr(e), rc)
    own_w = (w0 == 0 and w1 == 0 and w2 == 0 and sp.nsimplify(R4) == L["R_rad"])
    st = S7.slab_trace(Fr(e), rc)
    own_a = all(sp.nsimplify(-st.coeff(S7.d, j) + (ee if j == 0 else 0)) == q(L["at"][j]) for j in range(5))
    rk, resid = rkk_closed(rc)
    own_w = own_w and rk == L["R_rad"] and resid == 0
    return ok, own_w, own_a, L


# ------------------------------------------------------------------------------------------------ geometry helpers (sympy)
def _ricci_diag(g, X):
    """Christoffels and Ricci R_bc of a diagonal metric g (list) in coordinates X."""
    n = len(X)
    gi = [1 / v for v in g]
    G = {}
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                v = 0
                if a == b:
                    v += sp.diff(g[a], X[c])
                if a == c:
                    v += sp.diff(g[a], X[b])
                if b == c:
                    v -= sp.diff(g[b], X[a])
                v = v * gi[a] / 2
                if v != 0:
                    G[(a, b, c)] = G[(a, c, b)] = v
    Gm = lambda a, b, c: G.get((a, b, c), 0)

    def R(b, c):
        s = 0
        for a in range(n):
            s += sp.diff(Gm(a, b, c), X[a]) - sp.diff(Gm(a, b, a), X[c])
            for k in range(n):
                s += Gm(a, a, k) * Gm(k, b, c) - Gm(a, c, k) * Gm(k, b, a)
        return s
    return R, gi, Gm


# ------------------------------------------------------------------------------------------------ S6 the throat
def near_horizon(data=None):
    """Eq. (17) at r = 2m: R^a_b from sim1_transition.static_nec (R = 0, so R^a_b = 8 pi T^a_b of the Weyl fluid); the
    expansions F = A ~ x/2, H = 1/B ~ x^2 (x = r - 2m); the AdS2 factor's curvature (-1/2: radius 2m) and the S2 radius."""
    n = _nec()
    rs = [s for s in n["rho"].free_symbols if s.name == "r"][0]
    Rmix = [sp.nsimplify(v.subs(rs, 2)) for v in (-8 * sp.pi * n["rho"], 8 * sp.pi * n["pr"], 8 * sp.pi * n["pt"])]
    x, t = sp.symbols("x t", positive=True)
    F, H = (data or B4._eq17)(2 + x)
    Fs = sp.series(F, x, 0, 3).removeO()
    Hs = sp.series(H, x, 0, 4).removeO()
    Rf, gi, _ = _ricci_diag([-sp.Rational(1, 2) * x, 1 / x**2], [t, x])
    R2 = sp.simplify(gi[0] * Rf(0, 0) + gi[1] * Rf(1, 1))
    return {"R_mixed": Rmix + [Rmix[2]], "F": Fs, "H": Hs, "F_lead": sp.limit(F / x, x, 0),
            "H_lead": sp.limit(H / x**2, x, 0), "AdS2_R": R2, "S2_radius": sp.sqrt((2 + x)**2).subs(x, 0)}


def throat_equations(s2=1):
    """C7: the throat ODEs re-derived from a sympy 5D Ricci of ds^2 = dy^2 + alpha^2 [-(x/2) dt^2 + dx^2/x^2]
    + 4 beta^2 dOmega^2 (vacuum, Lambda_5 = -6/ell^2), and the Kretschmann formula K_th.  s2 = -1 flips the S2 curvature
    in the coded system (the mutation)."""
    y, t, x, th, ph = sp.symbols("y t x theta phi", real=True)
    e = sp.Symbol("e", nonnegative=True)
    al, be = sp.Function("alpha")(y), sp.Function("beta")(y)
    g = [sp.Integer(1), -al**2 * x / 2, al**2 / x**2, 4 * be**2, 4 * be**2 * sp.sin(th)**2]
    X = [y, t, x, th, ph]
    R, gi, Gm = _ricci_diag(g, X)
    E = [sp.simplify(gi[i] * R(i, i) + 4 * e**2) for i in range(5)]
    p, q, P, Q, a, b = sp.symbols("p q P Q a b")
    sub = {sp.Derivative(al, (y, 2)): (P + p**2) * a, sp.Derivative(be, (y, 2)): (Q + q**2) * b,
           sp.Derivative(al, y): p * a, sp.Derivative(be, y): q * b}
    Es = [sp.simplify(v.subs(sub).subs({al: a, be: b})) for v in E]
    sol = sp.solve([Es[1], Es[3]], [P, Q], dict=True)[0]
    coded_P = 4 * e**2 - 2 * p**2 - 2 * p * q - 1 / (4 * a**2)
    coded_Q = 4 * e**2 - 2 * q**2 - 2 * p * q + s2 / (4 * b**2)
    cons = sp.expand(Es[0].subs(sol))
    coded_c = p**2 + q**2 + 4 * p * q - 6 * e**2 - 1 / (4 * b**2) + 1 / (4 * a**2)
    # Kretschmann of the same metric, all components
    import itertools
    n = 5
    Gam = [[[Gm(i, j, k) for k in range(n)] for j in range(n)] for i in range(n)]
    K = 0
    for i, j, k, l in itertools.product(range(n), repeat=4):
        if k >= l:
            continue
        Rv = (sp.diff(Gam[i][j][l], X[k]) - sp.diff(Gam[i][j][k], X[l])
              + sum(Gam[i][k][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][k] for m in range(n)))
        if Rv != 0:
            K += 2 * Rv**2 * g[i] * gi[j] * gi[k] * gi[l]
    Ks = sp.simplify(K.subs(sub).subs({al: a, be: b}))
    coded_K = 4 * (2 * (P + p**2)**2 + 2 * (Q + q**2)**2 + (p**2 + 1 / (4 * a**2))**2 + (q**2 - 1 / (4 * b**2))**2
                   + 4 * p**2 * q**2)
    return {"P": sp.simplify(sol[P] - coded_P), "Q": sp.simplify(sol[Q] - coded_Q),
            "xx_tt": sp.simplify(Es[2] - Es[1]), "ph_th": sp.simplify(Es[4] - Es[3]),
            "constraint_ratio": sp.simplify(cons / coded_c), "yx": sp.simplify(R(0, 2)),
            "K": sp.simplify(Ks - coded_K)}


def throat_first_order():
    """C8: the O(x) equations re-derived: A = (x/2) alpha^2 (1 + x a1), B = (alpha^2/x^2)(1 + x b1),
    C = 4 beta^2 (1 + x c1); the tt, xx, thth equations at O(x) solved for a1'', b1'', c1'' against the coded ones; the
    momentum constraint (R_yx at O(1)) and the O(x) Hamiltonian constraint (yy); the data's O(x) terms from eq. (17)."""
    y, t, x, th, ph = sp.symbols("y t x theta phi", real=True)
    e = sp.Symbol("e", nonnegative=True)
    al, be = sp.Function("alpha")(y), sp.Function("beta")(y)
    a1, b1, c1 = sp.Function("a1")(y), sp.Function("b1")(y), sp.Function("c1")(y)
    A = x * al**2 / 2 * (1 + x * a1)
    B = al**2 / x**2 * (1 + x * b1)
    C = 4 * be**2 * (1 + x * c1)
    g = [sp.Integer(1), -A, B, C, C * sp.sin(th)**2]
    X = [y, t, x, th, ph]
    R, gi, _ = _ricci_diag(g, X)
    p, q, P, Q, a, b = sp.symbols("p q P Q a b")
    A1, B1, C1, dA, dB, dC, ddA, ddB, ddC = sp.symbols("A1 B1 C1 dA dB dC ddA ddB ddC")
    sub = {sp.Derivative(al, (y, 2)): (P + p**2) * a, sp.Derivative(be, (y, 2)): (Q + q**2) * b,
           sp.Derivative(al, y): p * a, sp.Derivative(be, y): q * b,
           sp.Derivative(a1, (y, 2)): ddA, sp.Derivative(b1, (y, 2)): ddB, sp.Derivative(c1, (y, 2)): ddC,
           sp.Derivative(a1, y): dA, sp.Derivative(b1, y): dB, sp.Derivative(c1, y): dC}
    fin = {al: a, be: b, a1: A1, b1: B1, c1: C1}
    bg = {P: 4 * e**2 - 2 * p**2 - 2 * p * q - 1 / (4 * a**2), Q: 4 * e**2 - 2 * q**2 - 2 * p * q + 1 / (4 * b**2)}
    out = {}
    for (i, j) in [(0, 0), (1, 1), (2, 2), (3, 3), (0, 2)]:
        Eij = gi[i] * R(i, j) + (4 * e**2 if i == j else 0)
        ser = sp.series(Eij.subs(sub).subs(fin).subs(bg), x, 0, 2).removeO()
        out[(i, j)] = (sp.simplify(ser.coeff(x, 0)), sp.simplify(ser.coeff(x, 1)))
    sol = sp.solve([out[(1, 1)][1], out[(2, 2)][1], out[(3, 3)][1]], [ddA, ddB, ddC], dict=True)[0]
    coded = {ddA: -(2 * A1 - B1 + C1) / a**2 - (3 * dA + dB + 2 * dC) * p - 2 * dA * q,
             ddB: -(2 * A1 - B1 + 2 * C1) / a**2 - (dA + 3 * dB + 2 * dC) * p - 2 * dB * q,
             ddC: -(dA + dB) * q - 2 * (p + 2 * q) * dC - C1 / (2 * b**2) - 3 * C1 / (2 * a**2)}
    mom = -sp.Rational(3, 4) * dA + dB / 4 - dC + C1 * (p - q)
    ham = sp.expand(out[(0, 0)][1].subs(sol))
    coded_ham = (2 * A1 / a**2 - B1 / a**2 + C1 / (2 * b**2) + 3 * C1 / a**2 + (dA + dB) * (p + 2 * q)
                 + 4 * dC * p + 2 * dC * q)
    xs = sp.Symbol("x", positive=True)
    F, H = B4._eq17(2 + xs)
    Aser = sp.series(F, xs, 0, 3).removeO()
    Bser = sp.series(1 / H * xs**2, xs, 0, 2).removeO()
    Cser = sp.series((2 + xs)**2 / 4, xs, 0, 2).removeO()
    data = (sp.simplify(Aser.coeff(xs, 2) / Aser.coeff(xs, 1)), Bser.coeff(xs, 1) / Bser.coeff(xs, 0),
            Cser.coeff(xs, 1) / Cser.coeff(xs, 0))
    return {"dd": [sp.simplify(sol[k] - coded[k]) for k in (ddA, ddB, ddC)],
            "mom_ratio": sp.simplify(out[(0, 2)][0] / mom), "ham": sp.simplify(ham - coded_ham),
            "O1_zero": [out[(i, i)][0] for i in (1, 2, 3)], "data": data}


# ------------------------------------------------------------------------------------------------ S7/S8 the throat bulk
def throat_rhs(y, u, e, s2=1.0, mut=0.0):
    """(alpha, beta, p, q) and the O(x) system (a1, b1, c1 and their y-derivatives).  s2 = -1 flips the S2 curvature
    (C7's mutation); mut != 0 perturbs the coded b1'' (C8's mutation)."""
    al, be, p, q, a1, b1, c1, da, db, dc = u
    P = 4 * e * e - 2 * p * p - 2 * p * q - 1 / (4 * al * al)
    Q = 4 * e * e - 2 * q * q - 2 * p * q + s2 / (4 * be * be)
    dda = -(2 * a1 - b1 + c1) / al**2 - (3 * da + db + 2 * dc) * p - 2 * da * q
    ddb = -(2 * a1 - b1 + 2 * c1) / al**2 - (da + 3 * db + 2 * dc) * p - 2 * db * q + mut * db * p
    ddc = -(da + db) * q - 2 * (p + 2 * q) * dc - c1 / (2 * be * be) - 3 * c1 / (2 * al * al)
    return [p * al, q * be, P, Q, da, db, dc, dda, ddb, ddc]


def kret_throat(u, e):
    """K_th = 4[2(p' + p^2)^2 + 2(q' + q^2)^2 + (p^2 + 1/(4 alpha^2))^2 + (q^2 - 1/(4 beta^2))^2 + 4 p^2 q^2] (C7)."""
    al, be, p, q = u[:4]
    P = 4 * e * e - 2 * p * p - 2 * p * q - 1 / (4 * al * al)
    Q = 4 * e * e - 2 * q * q - 2 * p * q + 1 / (4 * be * be)
    return 4 * (2 * (P + p * p)**2 + 2 * (Q + q * q)**2 + (p * p + 1 / (4 * al * al))**2
                + (q * q - 1 / (4 * be * be))**2 + 4 * p * p * q * q)


def throat_bulk(e, s2=1.0, mut=0.0, b1_0=2.5):
    """The throat bulk at e = m/ell: the zeroth-order system followed to alpha = 1e-9 (y_s^th), and the full system with
    the O(x) correction followed to alpha = 1e-6.  Start: alpha = beta = 1, p = q = -e; a1 = -1/2, b1 = 5/2, c1 = 1, all
    first derivatives 0 (eq. (17)'s data, C8)."""
    ef = float(e)
    u0 = [1.0, 1.0, -ef, -ef, -0.5, b1_0, 1.0, 0.0, 0.0, 0.0]

    def end0(y, u, *_):
        return u[0] - ALPHA_END
    end0.terminal = True

    def blow(y, u, *_):
        return abs(u[2]) + abs(u[3]) - 1e15
    blow.terminal = True

    def end1(y, u, *_):
        return u[0] - ALPHA_FULL
    end1.terminal = True
    f0 = lambda y, u: throat_rhs(y, list(u) + [0.0] * 6, ef, s2)[:4]
    sol0 = solve_ivp(f0, [0, 12], u0[:4], method="DOP853", rtol=1e-13, atol=1e-15, events=[end0, blow],
                     dense_output=True)
    sol = solve_ivp(lambda y, u: throat_rhs(y, u, ef, s2, mut), [0, 12], u0, method="DOP853", rtol=1e-13, atol=1e-15,
                    events=[end1, blow], dense_output=True)
    return {"e": ef, "y_s": float(sol0.t[-1]), "y_end": float(sol.t[-1]), "sol": sol, "sol0": sol0,
            "reached_alpha0": bool(sol0.status == 1 and len(sol0.t_events[0]) > 0)}


def _first_root(f, lo, hi, n=4000, rising=None):
    yy = np.linspace(lo, hi, n)
    v = np.array([f(z) for z in yy])
    s = np.sign(v)
    idx = np.where(s[:-1] * s[1:] < 0)[0]
    if rising is not None:
        idx = [i for i in idx if (v[i + 1] > v[i]) == rising]
    if not len(idx):
        return None
    i = idx[0]
    return float(brentq(f, yy[i], yy[i + 1], xtol=1e-13))


def _ystar(tb):
    s, ys, ye = tb["sol"], tb["y_s"], tb["y_end"]
    W1 = lambda y: float(s.sol(y)[8] - s.sol(y)[7]) / 2
    return _first_root(W1, 1e-3 * ys, ye * (1 - 1e-9), rising=True), W1


def _yK(tb, f):
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    g = lambda y: kret_throat(s.sol(y), ef) - f * S5.k_bs(ef, 2.0, y)
    return _first_root(g, 1e-3 * ys, ye * (1 - 1e-9), rising=True)


def throat_row(e):
    """One row of S8's table at e = m/ell, with S7's checks."""
    tb = throat_bulk(e)
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    yst, W1 = _ystar(tb)
    yK = {f: _yK(tb, f) for f in KF}
    U = lambda y: s.sol(y)
    rho = lambda y: float(U(y)[2] + 2 * U(y)[3] - 3 * ef)                  # rho_m in units of nu/m (level set)
    g95 = np.linspace(1e-3 * ys, 0.95 * ys, 3000)
    V = s.sol(g95)
    al, be, p, q = V[0], V[1], V[2], V[3]
    cons = p * p + q * q + 4 * p * q - 6 * ef * ef - 1 / (4 * be * be) + 1 / (4 * al * al)
    scale = p * p + q * q + 1 / (4 * al * al) + 1 / (4 * be * be) + 6 * ef * ef
    g90 = np.linspace(1e-3 * ys, 0.9 * ys, 3000)
    Z = s.sol(g90)
    mom = -0.75 * Z[7] + Z[8] / 4 - Z[9] + Z[6] * (Z[2] - Z[3])
    ham = (2 * Z[4] / Z[0]**2 - Z[5] / Z[0]**2 + Z[6] / (2 * Z[1]**2) + 3 * Z[6] / Z[0]**2
           + (Z[7] + Z[8]) * (Z[2] + 2 * Z[3]) + 4 * Z[9] * Z[2] + 2 * Z[9] * Z[3])
    gall = np.linspace(1e-3 * ys, ye * (1 - 1e-6), 3000)
    A_ = s.sol(gall)
    row = {"e": str(Fr(e)), "ell": None if ef == 0 else 1 / ef, "y_s": ys, "y_star": yst,
           "frac": None if yst is None else yst / ys, "yK": {str(f): yK[f] for f in KF},
           "K_ratio": None if yst is None else kret_throat(U(yst), ef) / S5.k_bs(ef, 2.0, yst),
           "rho_m": None if yst is None else rho(yst),
           "rho_m_rs": None if (yst is None or ef == 0) else rho(yst) / (3 * ef),
           "w_th_min": float(np.min(A_[3] - A_[2])), "at_max": float(np.max((A_[2] + A_[3]) / 2 + ef)),
           "cons_rel": float(np.max(np.abs(cons) / scale)), "mom": float(np.max(np.abs(mom))),
           "ham": float(np.max(np.abs(ham))), "reached": tb["reached_alpha0"],
           "W1_026": float(W1(0.26)) if 0.26 < ye else None, "W1_1088": float(W1(1.088)) if 1.088 < ye else None}
    if yst is not None:
        u = U(yst)
        row["level_set"] = {"rho": float(u[2] + 2 * u[3]), "rho_plus_pr": 0.0, "rho_plus_pth": float(u[3] - u[2])}
        band = np.linspace(yst, ye * (1 - 1e-6), 1500)
        row["rho_m_band_max"] = float(np.max(np.array([rho(z) for z in band])))
    return row


def _rho_at_ystar(e):
    tb = throat_bulk(e)
    yst, _ = _ystar(tb)
    u = tb["sol"].sol(yst)
    return float(u[2] + 2 * u[3] - 3 * float(e))


def _rho_band_max(e):
    tb = throat_bulk(e)
    yst, _ = _ystar(tb)
    s, ye = tb["sol"], tb["y_end"]
    band = np.linspace(yst, ye * (1 - 1e-6), 1500)
    V = s.sol(band)
    return float(np.max(V[2] + 2 * V[3] - 3 * float(e)))


def _edge_minus_yK(e, f):
    tb = throat_bulk(e)
    yst, _ = _ystar(tb)
    return yst - _yK(tb, f)


def ell_w(band=False):
    """ell_W: rho_m(y*) >= 0 iff ell >= ell_W (band=True: the maximum of rho_m over [y*, y_s))."""
    fn = _rho_band_max if band else _rho_at_ystar
    ew = brentq(fn, 1e-4, 0.05, xtol=1e-10)
    return 1 / ew, ew


def ell_c(f):
    """ell_c(f): the band's shallow edge lies below f K_bs (y* < y_K(f)) iff ell > ell_c(f); None if never."""
    g0 = _edge_minus_yK(1e-6, f)
    g1 = _edge_minus_yK(2.0, f)
    if g0 * g1 > 0:
        return None, g0
    ec = brentq(lambda e: _edge_minus_yK(e, f), 1e-6, 2.0, xtol=1e-10)
    return 1 / ec, g0


def throat_table(es=ES2, thresholds=True):
    """S8's table over ES2, ell_W (at y* and over the band) and ell_c(10, 30, 100)."""
    out = {"rows": [throat_row(e) for e in es]}
    if thresholds:
        out["ell_W"], out["e_W"] = ell_w()
        out["ell_W_band"], _ = ell_w(band=True)
        out["ell_c"] = {str(f): ell_c(f)[0] for f in KF}
        out["edge_minus_yK10_flat"] = _edge_minus_yK(1e-6, 10)
    return out


# ------------------------------------------------------------------------------------------------ S9 the map
def _mpc(c):
    return [mp.mpf(v.numerator) / v.denominator for v in reversed(c)]


def _dco(pp):
    n = len(pp) - 1
    return [c * (n - i) for i, c in enumerate(pp[:-1])] or [mp.mpf(0)]


def raw_rational(c, o):
    """Raw Pade (b4_static.pade through b4d_stage5._approx) of a warp-divided series: value and log-derivative
    p'/p - q'/q, with no doublet removal; and its real roots in (0, CAP] split into Froissart doublets and the rest."""
    p, q = S5._approx(c, o)
    pp, qq = _mpc(p), _mpc(q)
    dp, dq = _dco(pp), _dco(qq)
    rp = np.roots([float(v) for v in reversed(q)]) if len(q) > 1 else np.array([])
    rz = np.roots([float(v) for v in reversed(p)]) if len(p) > 1 else np.array([])
    real = lambda z: abs(z.imag) < 1e-8 * max(1.0, abs(z)) and 0 < z.real <= CAP
    near = lambda z, pool: len(pool) and min(abs(z - w) for w in pool) < DOUBLET * max(1.0, abs(z))
    block = sorted([z.real for z in rp if real(z) and not near(z, rz)] + [z.real for z in rz if real(z) and not near(z, rp)])
    doublets = sorted(z.real for z in rp if real(z) and near(z, rz))
    return {"val": lambda y: mp.polyval(pp, mp.mpf(y)) / mp.polyval(qq, mp.mpf(y)),
            "ld": lambda y: (mp.polyval(dp, mp.mpf(y)) / mp.polyval(pp, mp.mpf(y))
                             - mp.polyval(dq, mp.mpf(y)) / mp.polyval(qq, mp.mpf(y))),
            "block": block[0] if block else math.inf, "doublets": doublets}


def _w_at(Rs, y):
    lA, lB, lC = (Rs[X]["ld"](y) for X in "ABC")
    return float((lB - lA) / 2), float((lC - lA) / 2), float((lA + lB + 2 * lC) / 8)


def column_w(rc, e, N=ORDER, ngrid=NGRID, with_k=True):
    """One owner column: raw Pade of A~, B~, C~ at S5.orders(N); w_r, w_th, a~ on a 40-point y grid up to the scan top;
    verified points (two orders agree on A, B, C to 1e-4, all positive, no real non-doublet pole or zero of the two
    orders below y, and the two orders agree on w_r and w_th); the admissible set; K/K_bs at admissible points through
    b4d_stage5.evaluator at two orders."""
    t0 = time.process_time()
    mp.mp.dps = 40
    r = float(Fr(rc))
    S = B4.series(rc, N, e)
    W = S5.warped(S, e, N)
    ords = S5.orders(N)
    sing = [S5.nearest_real(W["C"][0], o) for o in ords]
    ysl = [float(z[0]) for z in sing if z]
    stable = bool(len(ysl) == 3 and (max(ysl) - min(ysl)) / float(np.median(ysl)) < 0.05)
    R = {o: {X: raw_rational(W[X][0], o) for X in "ABC"} for o in ords}
    block = min(R[o][X]["block"] for o in ords[:2] for X in "ABC")
    doublets = sorted({round(z, 4) for o in ords[:2] for X in "ABC" for z in R[o][X]["doublets"]})

    def point(y):
        vals = [[R[o][X]["val"](y) for X in "ABC"] for o in ords[:2]]
        okv = (y < block and all(v > 0 for row in vals for v in row)
               and all(abs(a - b) <= VAL_TOL * abs(b) for a, b in zip(vals[0], vals[1])))
        w = [_w_at(R[o], y) for o in ords]
        okw = all(abs(w[0][i] - w[1][i]) <= W_ABS + W_REL * abs(w[1][i]) for i in (0, 1))
        return okv, okw, w

    if stable:
        top = min(0.95 * float(np.median(ysl)), CAP)
    else:
        top = 0.0
        for y in np.linspace(CAP / 200, CAP, 200):
            okv, okw, _ = point(float(y))
            if not (okv and okw):
                break
            top = float(y)
    grid = [top * k / ngrid for k in range(1, ngrid + 1)] if top > 0 else []
    rows, prefix = [], True
    for y in grid:
        okv, okw, w = point(y)
        prefix = prefix and okv and okw
        adm = prefix and all(w[i][0] >= 0 and w[i][1] >= 0 for i in (0, 1))
        rows.append({"y": y, "wr": w[1][0], "wth": w[1][1], "at": w[1][2],
                     "wr_spread": max(abs(w[i][0] - w[j][0]) for i in range(3) for j in range(3)),
                     "val_ok": okv, "w_ok": okw, "ver": prefix, "adm": adm})
    ver = [z for z in rows if z["ver"]]
    vtop = ver[-1]["y"] if ver else 0.0
    wr_zero = None
    for z0, z1 in zip(ver, ver[1:]):
        if z0["wr"] < 0 <= z1["wr"]:
            f = lambda yy: float((R[ords[1]]["B"]["ld"](yy) - R[ords[1]]["A"]["ld"](yy)) / 2)
            wr_zero = float(brentq(f, z0["y"], z1["y"], xtol=1e-10))
            break
    kk = []
    adm = [z for z in rows if z["adm"]]
    if with_k and adm:
        Ks = [S5.evaluator(W, e, o)[0] for o in ords[:2]]
        pick = adm if len(adm) <= 12 else [adm[int(round(i * (len(adm) - 1) / 11))] for i in range(12)]
        for z in pick:
            kb = S5.k_bs(e, r, z["y"])
            kk.append([z["y"], Ks[0](z["y"]) / kb, Ks[1](z["y"]) / kb])
    return {"rc": rc, "r": r, "e": str(Fr(e)), "N": N, "ys": ysl, "ys_im": [float(z[1]) for z in sing if z],
            "ys_stable": stable, "top": top, "block": None if block == math.inf else block, "doublets": doublets,
            "rows": rows, "vtop": vtop, "wr_zero": wr_zero, "kk": kk, "cost_s": time.process_time() - t0}


def _job(args):
    rc, es = args
    return column_w(rc, Fr(es))


def regenerate(procs=3):
    """S9 over RADII2 x ES2 at order 32 (multiprocessing.Pool(3)), and S8's table; writes sim2_bank.json."""
    jobs = [(rc, str(e)) for e in ES2 for rc in RADII2]
    jobs.sort(key=lambda j: (float(Fr(j[0])) > 2.05, -float(Fr(j[1]))))   # near-throat and steep columns first
    t0 = time.monotonic()
    with Pool(procs) as pool:
        cols = pool.map(_job, jobs, chunksize=1)
    table = throat_table()
    bank = {"note": "regenerated by lemmas/sim2_facing.py --regenerate", "N": ORDER, "radii": RADII2,
            "es": [str(e) for e in ES2], "grid": NGRID, "val_tol": VAL_TOL, "w_tol": [W_ABS, W_REL],
            "columns": {"%s|%s" % (c["rc"], c["e"]): c for c in cols}, "throat": table,
            "wall_s": time.monotonic() - t0}
    json.dump(bank, open(BANK, "w"), separators=(",", ":"), default=float)
    return bank


def load_bank():
    return json.load(open(BANK))


def admissible(bank):
    """The admissible set per ell: (r_c, y) with w_r >= 0, w_th >= 0 at two verified Pade orders."""
    out = {}
    for es in bank["es"]:
        out[es] = [(c["rc"], c["r"], z["y"]) for k, c in bank["columns"].items() if c["e"] == es
                   for z in c["rows"] if z["adm"]]
    return out


def map_summary(bank):
    """S9's statements over the verified points: signs of w_r, w_th, a~ by class of column."""
    far = [(c, z) for c in bank["columns"].values() for z in c["rows"] if z["ver"]
           and (c["r"] >= 2.05 or Fr(c["e"]) >= Fr(1, 2))]
    allv = [(c, z) for c in bank["columns"].values() for z in c["rows"] if z["ver"]]
    pos = sorted({(c["rc"], c["e"]) for c, z in allv if z["wr"] >= 0})
    return {"n_ver": len(allv), "n_far": len(far),
            "far_wr_neg": sum(z["wr"] < 0 for _, z in far), "far_wth_pos": sum(z["wth"] > 0 for _, z in far),
            "far_at_neg": sum(z["at"] < 0 for _, z in far), "at_max": max(z["at"] for _, z in allv),
            "wth_min": min(z["wth"] for _, z in allv), "wr_pos_cols": pos,
            "removed_by_w": sum(1 for c in bank["columns"].values() for z in c["rows"] if z["val_ok"] and not z["w_ok"])}


# ------------------------------------------------------------------------------------------------ S11 Lemma N
def lemma_n(sign=-1):
    """Gamma^y_ab = sign (1/2) d_y g_ab is checked (sign = -1 is the true connection; +1 is the mutation), and the
    radial null ray tangent to a level set: y'' = -Gamma^y_tt t'^2 - Gamma^y_rr r'^2 with t'^2 = B r'^2/A, against
    w_r B r'^2.  Corollary W: a warped product has kappa_t = kappa_r = kappa_th."""
    y, t, r, th, ph, rdot = sp.symbols("y t r theta phi rdot", real=True)
    A, B, C = (sp.Function(n)(y, r) for n in "ABC")
    g = [sp.Integer(1), -A, B, C, C * sp.sin(th)**2]
    X = [y, t, r, th, ph]
    _, _, Gm = _ricci_diag(g, X)
    conn = all(sp.simplify(Gm(0, i, i) - sign * sp.Rational(1, 2) * sp.diff(g[i], y)) == 0 for i in range(1, 5))
    G = (lambda a_, b_, c_: sign * sp.Rational(1, 2) * sp.diff(g[b_], y) if (a_ == 0 and b_ == c_ and b_ > 0)
         else Gm(a_, b_, c_))
    tdot2 = B * rdot**2 / A
    ydd = -G(0, 1, 1) * tdot2 - G(0, 2, 2) * rdot**2
    w_r = (sp.diff(B, y) / B - sp.diff(A, y) / A) / 2
    ray = sp.simplify(ydd - w_r * B * rdot**2)
    f, F, H = sp.Function("f")(y), sp.Function("F")(r), sp.Function("H")(r)
    gw = [sp.exp(2 * f) * F, sp.exp(2 * f) / H, sp.exp(2 * f) * r**2]
    kap = [sp.simplify(sp.diff(v, y) / (2 * v)) for v in gw]
    return {"connection": conn, "ray": ray, "warped_w": [sp.simplify(kap[1] - kap[0]), sp.simplify(kap[2] - kap[0])]}


# ------------------------------------------------------------------------------------------------ C11 exact controls
def schwarzschild_control(rc="3", e=Fr(1), N=16):
    """Schwarzschild data: the warp-divided series terminates (the black string), so w_r = w_th = a~ = 0 exactly."""
    S = B4.series(rc, N, e, data=B4._schwarzschild)
    W = S5.warped(S, e, N)
    term = all(W[X][0][k] == 0 for X in "ABC" for k in range(1, N + 1))
    kap = {}
    for X in "ABC":
        c = [Fr(v) for v in S[X][0][:N + 1]]
        kap[X] = [v / 2 for v in _div(_deriv(c), c, N - 1)]
    wr = all(kap["B"][j] - kap["A"][j] == 0 for j in range(N))
    wth = all(kap["C"][j] - kap["A"][j] == 0 for j in range(N))
    at = all((kap["A"][j] + kap["B"][j] + 2 * kap["C"][j]) / 4 + (Fr(e) if j == 0 else 0) == 0 for j in range(N))
    return {"terminates": term, "w_r": wr, "w_th": wth, "at": at}


def wedge(warp="cosh"):
    """The AdS4-sliced wedge d rho^2 + cosh^2(rho/ell) g4 (g4 AdS4 of radius ell, Poincare chart): Einstein with
    Lambda_5 = -6/ell^2; a = tanh((y - rho*)/ell)/ell along y = rho + rho*; P1 at y = 0 reads s1 = tanh(rho*/ell), and a
    facing sheet at y = 2 rho* reads s2 = s1 (T5 equality).  warp = 'sinh' is the mutation."""
    rho, t, x1, x2, z = sp.symbols("rho t x1 x2 z", real=True)
    ell = sp.Symbol("ell", positive=True)
    c2 = (sp.cosh(rho / ell) if warp == "cosh" else sp.sinh(rho / ell))**2
    h = ell**2 / z**2
    g = [sp.Integer(1), -c2 * h, c2 * h, c2 * h, c2 * h]
    X = [rho, t, x1, x2, z]
    R, gi, _ = _ricci_diag(g, X)
    einstein = [sp.simplify(gi[i] * R(i, i) + 4 / ell**2) for i in range(5)]
    a = sp.simplify(sp.diff(c2, rho) / (2 * c2))
    u = sp.Symbol("u", positive=True)                                  # u = rho*/ell
    s1 = sp.simplify(-ell * a.subs(rho, -u * ell))
    s2 = sp.simplify(ell * a.subs(rho, u * ell))
    bound = sp.tanh(2 * u - sp.atanh(s1))
    num = ([abs(float(bound.subs(u, v)) - float(s2.subs(u, v))) for v in (0.1, 0.5, 1.3)] if warp == "cosh"
           else [float("nan")])
    return {"einstein": einstein, "a": a, "s1": s1, "s2": s2, "equal": sp.simplify(s2 - s1) == 0,
            "bound_gap": max(num)}


# ------------------------------------------------------------------------------------------------ S12 decision
def decide(bank, table):
    """Per ell: WIDE (an admissible verified point at r_c >= 2.1m), THROAT-BAND (y* < y_s^th, every admissible point at
    r_c < 2.1m; qualified CONFIRMED / EXPANSION-ONLY, regular at 10/30/100 K_bs, the strict y < y_s, WEC), NONE (no
    zero of W1 before y_s^th and no admissible point), else UNDECIDED."""
    adm = admissible(bank)
    rows = {r_["e"]: r_ for r_ in table["rows"]}
    out = {}
    for es in bank["es"]:
        row = rows[es]
        A = adm[es]
        wide = [a for a in A if a[1] >= WIDE_R]
        ys_, yst = row["y_s"], row["y_star"]
        d = {"y_s": ys_, "y_star": yst, "n_adm": len(A), "wide": wide[:5]}
        if wide:
            d["class"] = "WIDE"
        elif yst is not None and yst < ys_:
            d["class"] = "THROAT-BAND"
        elif not A:
            d["class"] = "NONE"
        else:
            d["class"] = "UNDECIDED"
        near = [c for c in bank["columns"].values() if c["e"] == es and c["r"] < WIDE_R]
        d["not_reached"] = sorted([(c["rc"], round(c["vtop"], 4)) for c in near
                                   if yst is not None and c["vtop"] < yst], key=lambda v: Fr(v[0]))
        conf = []
        for c in near:
            if c["r"] <= NEAR_R + 1e-12 and any(z["adm"] for z in c["rows"]) and yst:
                edge = c["wr_zero"] if c["wr_zero"] is not None else min(z["y"] for z in c["rows"] if z["adm"])
                conf.append((c["rc"], edge, abs(edge - yst) / yst))
        conf.sort(key=lambda v: v[2])
        d["confirm"] = conf
        d["confirmed"] = bool(conf and conf[0][2] <= CONFIRM_TOL)
        if yst is not None:
            d["regular"] = {str(f): bool(row["yK"][str(f)] is not None and yst < row["yK"][str(f)]) for f in KF}
            d["strict"] = bool(yst < ys_)
            d["settled"] = len(set(d["regular"].values())) == 1
            d["wec"] = bool(row["rho_m"] >= 0)
        out[es] = d
    return out


# ------------------------------------------------------------------------------------------------ S13 hand-off
def delta_rows():
    """s_slab = ell a(depth) <= -1 (S3); two-sided sigma_2/lambda_RS = (s_slab + s_outer)/2, so 139's -1/3 needs
    s_outer >= +1/3 and stage 7 K5's -1/6 needs s_outer >= +2/3 (both positive: the outer side decays, K4)."""
    s_slab = Fr(-1)
    need = {str(s2): 2 * s2 - s_slab for s2 in (Fr(-1, 3), Fr(-1, 6))}
    rows = [("(0, 0 | 0)", "EMPTY (S3, T5c)"), ("(0, 0 | NEC)", "S12"), ("(0, 0 | NEC+WEC)", "ell >= ell_W only")]
    return {"s_slab_max": s_slab, "s_outer_min": need, "rows": rows}


# For the next instrument, sim2_passage (escape E-PASS): anchors two judges reproduced in the design phase, kept internal
# under 119 (the address is the input's) -- not computed here, never printed by this instrument.
PASSAGE_ANCHORS = {"r2_star": "116.34 ... 2.247m", "cycle": "2.75 -> 4.00939 -> 2.75000", "r_star": 3.191934,
                   "Y_max": 1.5946}

ESCAPES = [
    ("E-NS", "non-static (152 (2))", "scheduled as phase 2b-ii, the brief evolution"),
    ("E-ROT", "non-diagonal K (141's internal motion)", "open"),
    ("E-BULK", "Ric(n,n) < -4/ell^2", "T fails; W stands"),
    ("E-ASYM", "P2 not mirrored, with its own outer side", "phase 3"),
    ("E-PASS", "no second sheet; end 2 of our own plane reached through the horizon", "the next instrument, sim2_passage"),
    ("E-G", "global closure of P2", "phase 2b-i"),
    ("E-AN", "outside the analytic class", "open"),
]


# ------------------------------------------------------------------------------------------------ C14 address guard
def address_guard(extra_keys=None, extra_funcs=()):
    """No function of this instrument takes a plane separation (by signature), and no key of the bank or the report
    names a distance, time, redshift or speed (139 (4), 101 (7))."""
    mod = sys.modules[__name__]
    funcs = [f for _, f in inspect.getmembers(mod, inspect.isfunction) if f.__module__ == mod.__name__]
    funcs += list(extra_funcs)
    bad_args = sorted({(f.__name__, p) for f in funcs for p in inspect.signature(f).parameters if p in BANNED_ARGS})
    keys = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                keys.add(str(k))
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    if os.path.exists(BANK):
        walk(load_bank())
    if extra_keys:
        walk(extra_keys)
    bad_keys = sorted(k for k in keys if any(b in k.lower() for b in BANNED_KEYS))
    return {"n_funcs": len(funcs), "bad_args": bad_args, "bad_keys": bad_keys, "n_keys": len(keys)}


# ------------------------------------------------------------------------------------------------ the owner-side checks
def owner_column(rc, e, N, o_index=1):
    """w_r, w_th, a~ from the raw Pade at one order -- for C5, C9, C10."""
    mp.mp.dps = 40
    W = S5.warped(B4.series(rc, N, e), e, N)
    o = S5.orders(N)[o_index]
    R = {X: raw_rational(W[X][0], o) for X in "ABC"}
    return W, o, R


def pade_honesty():
    """C5: at r = 2.15m, ell = m: the raw Pade at N = 24 against the partial sums of the exact series at orders 24, 28
    and 32 (a partial sum counts as converged at y where orders 28 and 32 agree to 1e-9), and the mutation through
    b4d_stage5._clean."""
    W, o, R = owner_column("43/20", Fr(1), 24)
    W32 = S5.warped(B4.series("43/20", 32, Fr(1)), Fr(1), 32)

    def psum(Wx, X, y, n):
        c = [float(v) for v in Wx[X][0][:n + 1]]
        return sum(k * c[k] * y**(k - 1) for k in range(1, len(c))) / sum(c[k] * y**k for k in range(len(c)))
    out = []
    for y in (0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        raw = _w_at(R, y)[0]
        ps = {n: (psum(W32, "B", y, n) - psum(W32, "A", y, n)) / 2 for n in (24, 28, 32)}
        out.append((y, raw, ps[24], ps[28], ps[32]))
    pq = {X: S5._approx(W[X][0], o) for X in "ABC"}
    cl = {}
    for X in "ABC":
        pp, qq, dz = S5._clean(*pq[X])
        dp, dq = _dco(pp), _dco(qq)

        def ld(yv, pp=pp, qq=qq, dp=dp, dq=dq, dz=dz):
            yv = mp.mpf(yv)
            v = mp.polyval(dp, yv) / mp.polyval(pp, yv) - mp.polyval(dq, yv) / mp.polyval(qq, yv)
            for pole, zero in dz:
                v += 1 / (yv - pole) - 1 / (yv - zero)
            return mp.re(v)
        cl[X] = ld
    clean = float((cl["B"](0.02) - cl["A"](0.02)) / 2)
    return {"rows": out, "clean_002": clean, "raw_002": out[0][1]}


def throat_vs_owner():
    """C9: at ell = 2m, columns 401/200 and 201/100 (N = 20) against the throat ODE at y = 0.13, 0.26 (w_th, a~), and the
    gap ratio (linear in x).  C10: W1(1.088) against w_r(2.005)/0.005 (flat, N = 24)."""
    tb = throat_bulk(Fr(1, 2))
    s = tb["sol"]
    ode = {y: (float(s.sol(y)[3] - s.sol(y)[2]), float((s.sol(y)[2] + s.sol(y)[3]) / 2 + 0.5)) for y in (0.13, 0.26)}
    own = {}
    for rc in ("401/200", "201/100"):
        _, _, R = owner_column(rc, Fr(1, 2), 20)
        own[rc] = {y: _w_at(R, y)[1:] for y in (0.13, 0.26)}
    rel = {rc: {y: [abs(own[rc][y][i] / ode[y][i] - 1) for i in (0, 1)] for y in ode} for rc in own}
    ratio = {y: [(own["201/100"][y][i] - ode[y][i]) / (own["401/200"][y][i] - ode[y][i]) for i in (0, 1)] for y in ode}
    tb0 = throat_bulk(Fr(0))
    W1 = float(tb0["sol"].sol(1.088)[8] - tb0["sol"].sol(1.088)[7]) / 2
    _, _, R0 = owner_column("401/200", Fr(0), 24)
    wr = _w_at(R0, 1.088)[0]
    return {"ode": ode, "own": own, "rel": rel, "ratio": ratio, "W1": W1, "wr_over_x": wr / 0.005}


# ------------------------------------------------------------------------------------------------ report
def _ell(es):
    e = Fr(es)
    return "inf" if e == 0 else ("%gm" % float(1 / e))


def compute_live():
    """The fast exact parts the report prints live (seconds)."""
    return {"lead3": leading_coefficients("3", Fr(1, 2)), "lead215": leading_coefficients("43/20", Fr(1, 2)),
            "t5c": t5c(Fr(1)), "lemma_t": lemma_t(), "near": near_horizon(), "n": lemma_n(), "delta": delta_rows(),
            "wproof": lemma_w_proof(4000)}


def report(bank, live):
    T = bank["throat"]
    dec = decide(bank, T)
    ms = map_summary(bank)
    print("sim2_facing.py -- B4d simulation phase 2: two pieces of our plane facing across a static bulk\n")
    lt = live["lemma_t"]
    print("S1 Lemma T (deduced; T1 exact on the owner's series, selftest C3): Raychaudhuri split residual %s; the "
          "comparison solution e tanh(e y - artanh s1) solves b' = e^2 - b^2 (residual %s), and at s1 = 1 is the fixed "
          "point %s/ell: a~ <= 0 at every depth" % (lt["split"], lt["ode"], lt["fixed_point"]))
    L3 = live["lead3"]
    print("   anchor r = 3m, ell = 2m: a~ = (%s) y^3 + (%s) y^4 + O(y^5) = -(R_ab R^ab/12)(y^3 + 5 e y^4), R_ab R^ab = %s"
          % (L3["at"][3], L3["at"][4], L3["RR"]))
    print("S2 Lemma C (deduced; comparison standard-not-READ): k_t(P2) = -kappa_t, k_spatial(P2) >= -kappa_spatial")
    tc = live["t5c"]
    print("S3 T5c (deduced): a matter-free mirrored P2 reads s2 <= ell a(depth) <= %s at every depth and ell; general "
          "bound s2 <= %s, which at s1 -> 1 is %s (the depth drops out).  DECIDED: under clause (B) two matter-free "
          "pieces of our plane cannot face each other" % (tc["s2_max"], tc["general"], tc["at_s1_1"]))
    wp = live["wproof"]
    print("S4 Lemma W (deduced): k_t I - k_spatial = diag(w) - H exactly: %s; %d NEC-obeying random samples, %d "
          "counterexamples to w >= 0" % (wp["exact"], wp["nec_samples"], wp["counterexamples"]))
    L215 = live["lead215"]
    print("S5 leading orders (exact): r = 3m: R_rad %s, R_tan %s, y^2 terms at ell = 2m %s, %s; r = 2.15m: R_rad %s, "
          "R_tan %s" % (L3["R_rad"], L3["R_tan"], L3["wr"][2], L3["wth"][2], L215["R_rad"], L215["R_tan"]))
    nh = live["near"]
    print("S6 near horizon: R^a_b(r = 2m) = %s; F ~ %s x, H ~ %s x^2; AdS2 curvature %s (radius 2m), S2 radius %s"
          % (nh["R_mixed"], nh["F_lead"], nh["H_lead"], nh["AdS2_R"], nh["S2_radius"]))
    print("S7/S8 the throat bulk (ODE; rho_m in nu/m, level set; K_bs = b4d_stage5.k_bs(e, 2, y)):")
    print("   ell    y_s^th   y*      y*/y_s  y_K(10/30/100)          K(y*)/K_bs  rho_m(y*) nu/m  (sigma_RS)  "
          "w_th min   a~ max    constraint")
    for r_ in T["rows"]:
        yk = r_["yK"]
        print("   %-5s  %.4f   %s  %s   %s  %10.3g  %+9.4f  %10s  %.2e  %+.1e  %.0e" % (
            _ell(r_["e"]), r_["y_s"], "%.4f" % r_["y_star"] if r_["y_star"] else "none  ",
            "%.3f" % r_["frac"] if r_["frac"] else "  -  ",
            " / ".join("%.3f" % yk[str(f)] if yk[str(f)] else "  -  " for f in KF), r_["K_ratio"] or float("nan"),
            r_["rho_m"] if r_["rho_m"] is not None else float("nan"),
            "" if r_["rho_m_rs"] is None else "(%+.3f)" % r_["rho_m_rs"], r_["w_th_min"], r_["at_max"],
            r_["cons_rel"]))
    print("   WEC in the band (rho_m(y*) >= 0): ell >= ell_W = %.2fm (e <= %.6f); maximum over the band gives %.2fm"
          % (T["ell_W"], T["e_W"], T["ell_W_band"]))
    print("   the band's shallow edge below f K_bs: f = 10 %s; f = 30 for ell > %s; f = 100 for ell > %s" % (
        "never (flat: y* - y_K(10) = %+.3f m)" % T["edge_minus_yK10_flat"] if T["ell_c"]["10"] is None
        else "for ell > %.2fm" % T["ell_c"]["10"],
        "%.2fm" % T["ell_c"]["30"] if T["ell_c"]["30"] else "never", "%.2fm" % T["ell_c"]["100"] if T["ell_c"]["100"]
        else "never"))
    print("S9 the map (order 32, %d columns, raw Pade, %d verified points; the w-agreement removed %d value-verified "
          "points):" % (len(bank["columns"]), ms["n_ver"], ms["removed_by_w"]))
    print("   columns at r >= 2.05m or ell <= 2m: %d verified points; w_r < 0 at %d, w_th > 0 at %d, a~ < 0 at %d" % (
        ms["n_far"], ms["far_wr_neg"], ms["far_wth_pos"], ms["far_at_neg"]))
    print("   over every verified point: max a~ %.2e, min w_th %.2e; columns with some verified w_r >= 0: %s" % (
        ms["at_max"], ms["wth_min"], ", ".join("%s@%s" % (rc, _ell(es)) for rc, es in ms["wr_pos_cols"])))
    for es in bank["es"]:
        cs = [bank["columns"]["%s|%s" % (rc, es)] for rc in ("401/200", "201/100", "101/50")]
        print("   ell = %-5s r = 2.005/2.01/2.02m: verified top %s; w_r changes sign at %s; y_s(C~) %s" % (
            _ell(es), "/".join("%.3f" % c["vtop"] for c in cs),
            "/".join("%.3f" % c["wr_zero"] if c["wr_zero"] else "-" for c in cs),
            "/".join("%.3f" % float(np.median(c["ys"])) if c["ys"] else "-" for c in cs)))
    print("   K/K_bs at the shallowest admissible point (two Pade orders, b4d_stage5.evaluator):")
    for es in bank["es"]:
        pts = sorted([(c["r"], c["rc"], k) for c in bank["columns"].values() if c["e"] == es and c["kk"]
                      for k in c["kk"][:1]])
        if pts:
            print("   ell = %-5s %s" % (_ell(es), "; ".join("r = %s: y = %.3f, %.1f/%.1f" % (rc, k[0], k[1], k[2])
                                                          for _, rc, k in pts)))
    print("S10 throat and owner: the sign change of w_r, extrapolated to x -> 0 (2 y0(2.005m) - y0(2.01m)), against y*:")
    for r_ in T["rows"]:
        c1 = bank["columns"]["401/200|%s" % r_["e"]]
        c2 = bank["columns"]["201/100|%s" % r_["e"]]
        if c1["wr_zero"] and c2["wr_zero"]:
            ex = 2 * c1["wr_zero"] - c2["wr_zero"]
            print("   ell = %-5s %.4f against y* %.4f (%.2f%%)" % (_ell(r_["e"]), ex, r_["y_star"],
                                                                 100 * abs(ex / r_["y_star"] - 1)))
    print("   y_s^th against the r = 2.005m column's C~ singularity (three Pade orders):")
    for r_ in T["rows"]:
        c = bank["columns"]["401/200|%s" % r_["e"]]
        print("   ell = %-5s %.4f against %s" % (_ell(r_["e"]), r_["y_s"],
                                                "/".join("%.4f" % v for v in c["ys"]) if c["ys"] else "-"))
    nl = live["n"]
    print("S11 Lemma N (sympy): Gamma^y_ab = -(1/2) d_y g_ab: %s; y'' - w_r B r'^2 = %s; warped products w = %s" % (
        nl["connection"], nl["ray"], nl["warped_w"]))
    print("S12 decision:")
    for es in bank["es"]:
        d = dec[es]
        line = "   ell = %-5s %s" % (_ell(es), d["class"])
        if d["class"] == "THROAT-BAND":
            cf = d["confirm"][0] if d["confirm"] else None
            line += (" %s%s; regular at 10/30/100 K_bs: %s (strict y < y_s: %s; settled: %s); WEC: %s; admissible "
                     "points %d" % ("CONFIRMED" if d["confirmed"] else "EXPANSION-ONLY",
                                    " (%s, edge %.4f vs y* %.4f, %.1f%%)" % (cf[0], cf[1], d["y_star"], 100 * cf[2])
                                    if cf else "", "/".join("yes" if d["regular"][str(f)] else "no" for f in KF),
                                    d["strict"], d["settled"], "yes" if d["wec"] else "no", d["n_adm"]))
            if d["not_reached"]:
                line += "; not reached: %s" % ", ".join("%s (top %.3f)" % v for v in d["not_reached"])
        print(line)
    dl = live["delta"]
    print("S13 hand-off: s_slab <= %s; s_outer needed: %s (both > 0: the outer side decays, stage 7 K4); rows: %s" % (
        dl["s_slab_max"], ", ".join("%s -> >= %s" % kv for kv in dl["s_outer_min"].items()),
        "; ".join("%s %s" % r_ for r_ in dl["rows"])))
    print("S14 escapes: %s" % "; ".join("%s (%s): %s" % e_ for e_ in ESCAPES))
    print("   No length, distance, time, redshift or speed is computed (155/R4, 101 (7), 139 (4)).")
    return dec


# ------------------------------------------------------------------------------------------------ selftest
PIN = {  # this instrument's own computed values (C13), pinned at its first regeneration
    "0": {"y_s": 2.55355, "y_star": 1.79006, "K_ratio": 18.3},
    "1": {"y_s": 0.91386, "y_star": 0.88119, "K_ratio": 2.69e4},
    "ell_W": 49.86, "ell_c30": 21.05,
}


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))
        sys.stdout.flush()

    t0 = time.monotonic()
    # C1
    e = sp.Symbol("e", positive=True)
    rho1, _ = israel([-e] * 4)
    rhoL, _ = israel([+e] * 4)
    rhoM, _ = israel([-e] * 4)
    rhoT, _ = israel([-e] * 4, trace_from=1)
    s1 = sp.simplify(rho1 / (3 * e))
    sL = sp.simplify(rhoL / (3 * e))
    sM = sp.simplify(rhoM / (3 * e))
    sT = sp.simplify(rhoT / (3 * e))
    chk("C1 Israel calibration: P1 (n = +d_y, K = -h/ell) reads s = %s = b4d_stage6.sigma_over_rs(-e,-e,e) = %s; an RS2 "
        "level set read with n = -d_y reads s = %s (RS1's negative sheet); mutations: n = +d_y gives %s, failing RS1; "
        "the trace over the spatial part only gives P1 s = %s" % (s1, S6.sigma_over_rs(-e, -e, e), sL, sM, sT),
        s1 == 1 and S6.sigma_over_rs(-e, -e, e) == 1 and sL == -1 and sM != -1 and sT != 1)
    # C2
    kt, kr, kq, kp, c, nu = sp.symbols("k_t k_r k_q k_p c nu", real=True)
    K = [kt + c, kr + c, kq + c, kp + c]
    rho, ps = israel(K, nu)
    li = [sp.simplify(rho + ps[i] - nu * (kt - [kr, kq, kp][i])) for i in range(3)]
    rho_m, ps_m = israel(K, nu / 2)
    li_m = [sp.simplify(rho_m + ps_m[i] - nu * (kt - [kr, kq, kp][i])) for i in range(3)]
    rho_t, ps_t = israel(K, nu, trace_from=1)
    li_t = [sp.simplify(rho_t + ps_t[i] - nu * (kt - [kr, kq, kp][i])) for i in range(3)]
    wp = lemma_w_proof()
    wf = lemma_w_proof(flip=True)
    chk("C2 local Israel lemma: rho + p_i - nu (k_t - k_i) = %s for any added tension c; mutation (the two-sided factor "
        "nu/2) leaves %s; the trace drops out of rho + p_i (a trace error leaves %s, so C1 catches it); Lemma W's step "
        "exact (%s), %d NEC samples with %d counterexamples, and the reversed comparison produces %d"
        % (li, li_m[0], li_t[0], wp["exact"], wp["nec_samples"], wp["counterexamples"], wf["counterexamples"]),
        all(v == 0 for v in li) and any(v != 0 for v in li_m) and all(v == 0 for v in li_t) and wp["exact"]
        and wp["counterexamples"] == 0 and wp["nec_samples"] > 100 and wf["counterexamples"] > 0)
    # C3
    r0 = riccati_identity("43/20", Fr(0))
    r1 = riccati_identity("43/20", Fr(1))
    rm = riccati_identity("43/20", Fr(1), ryy_sign=+1)
    chk("C3 T1 exact on the owner's series at r = 2.15m: a' - (1/ell^2 - a^2 - Pi.Pi/4) = 0 through y^12 at ell = inf "
        "and m (%d and %d nonzero coefficients); mutation R_yy = +4/ell^2 leaves %s at y^0"
        % (sum(v != 0 for v in r0), sum(v != 0 for v in r1), rm[0]),
        len(r0) == 13 and all(v == 0 for v in r0) and all(v == 0 for v in r1) and rm[0] != 0)
    # C4
    res = [(rc, es, check_leading(rc, es)) for rc in ("3", "43/20") for es in (Fr(0), Fr(1, 2), Fr(1))]
    L3 = [L for rc, es, (_, _, _, L) in res if rc == "3" and es == Fr(1, 2)][0]
    L2 = [L for rc, es, (_, _, _, L) in res if rc == "43/20"][0]
    chk("C4 S5 exact at r = 3m and 2.15m, ell = inf, 2m, m: w_r = R_rad(y + 3ey^2), w_th = R_tan(y + 3ey^2), a~ = "
        "-(RR/12)(y^3 + 5ey^4); against b4d_stage5.wall_exact, sim1_transition.eq17_rkk and b4d_stage7.slab_trace; r = 3m: %s, %s (y^2 at ell = 2m: "
        "%s, %s); r = 2.15m: %s, %s" % (L3["R_rad"], L3["R_tan"], L3["wr"][2], L3["wth"][2], L2["R_rad"], L2["R_tan"]),
        all(a and b and c_ for _, _, (a, b, c_, _) in res) and L3["R_rad"] == sp.Rational(-2, 81)
        and L3["R_tan"] == sp.Rational(1, 27) and L3["wr"][2] == Fr(-1, 27) and L3["wth"][2] == Fr(1, 18)
        and L2["R_rad"] == sp.Rational(-12000, 312481) and L2["R_tan"] == sp.Rational(2000, 7267))
    # C5
    ph = pade_honesty()
    conv = [v for v in ph["rows"] if abs(v[3] - v[4]) <= 1e-9 * abs(v[4])]
    worst_conv = max(abs(v[1] - v[4]) / abs(v[4]) for v in conv)
    lit = {v[0]: abs(v[1] - v[2]) / abs(v[2]) for v in ph["rows"]}
    at6 = [v for v in ph["rows"] if v[0] == 0.6][0]
    pade32, sum24 = abs(at6[1] - at6[4]) / abs(at6[4]), abs(at6[2] - at6[4]) / abs(at6[4])
    dclean = abs(ph["clean_002"] - ph["raw_002"])
    chk("C5 Pade honesty (r = 2.15m, ell = m, N = 24): raw-Pade w_r equals the converged partial sums (orders 28 and 32 "
        "agree to 1e-9: y <= %.1f) to %.1e relative, and the order-24 partial sums to %.1e at y = 0.5; at y = 0.6 the "
        "order-24 sums have not converged (%.1e from order 32) and the raw Pade is nearer the order-32 sums (%.1e) -- "
        "the spec's 1e-7 at 0.6 fails on the partial sums, not the Pade (%.1e); mutation through b4d_stage5._clean "
        "differs by %.2e at y = 0.02 (%.0f%%)" % (max(v[0] for v in conv), worst_conv, lit[0.5], sum24, pade32, lit[0.6],
                                                 dclean, 100 * dclean / abs(ph["raw_002"])),
        worst_conv < 1e-7 and max(v[0] for v in conv) >= 0.4 and lit[0.5] < 1e-7 and pade32 < sum24 and dclean > 1e-4)
    # C6
    nh = near_horizon()
    nm = near_horizon(B4._schwarzschild)
    chk("C6 near horizon: R^a_b(r = 2m) = %s; F ~ %s x, H ~ %s x^2; AdS2 curvature %s (radius 2m); mutation "
        "(Schwarzschild data) gives H/x^2 -> %s" % (nh["R_mixed"], nh["F_lead"], nh["H_lead"], nh["AdS2_R"],
                                                   nm["H_lead"]),
        nh["R_mixed"] == [sp.Rational(-1, 4), sp.Rational(-1, 4), sp.Rational(1, 4), sp.Rational(1, 4)]
        and nh["F_lead"] == sp.Rational(1, 2) and nh["H_lead"] == 1 and nh["AdS2_R"] == sp.Rational(-1, 2)
        and nm["H_lead"] != 1)
    # C7
    te = throat_equations()
    tm = throat_equations(s2=-1)
    rows01 = {es: throat_row(Fr(es)) for es in ("0", "1")}
    rows_all = [throat_row(e_) for e_ in (Fr(1, 2), Fr(4))] + list(rows01.values())
    tbm = throat_bulk(Fr(1, 2), s2=-1.0)
    sm = tbm["sol0"]
    gm = np.linspace(0, 0.95 * sm.t[-1], 500)
    V = sm.sol(gm)
    consm = V[2]**2 + V[3]**2 + 4 * V[2] * V[3] - 1.5 - 1 / (4 * V[1]**2) + 1 / (4 * V[0]**2)
    scm = V[2]**2 + V[3]**2 + 1 / (4 * V[0]**2) + 1 / (4 * V[1]**2) + 1.5
    mutc = float(np.max(np.abs(consm) / scm))
    chk("C7 throat ODEs from a sympy 5D Ricci: p', q' residuals %s, %s; xx = tt (%s), phph = thth (%s); constraint = "
        "%s x coded; R_yx = %s; K_th residual %s; constraint held to %.1e relative below 0.95 y_s (ell = inf, 2m, m, "
        "m/4); mutation (S2 curvature flipped): coded q' residual %s, constraint %.2f relative"
        % (te["P"], te["Q"], te["xx_tt"], te["ph_th"], te["constraint_ratio"], te["yx"], te["K"],
           max(r_["cons_rel"] for r_ in rows_all), tm["Q"], mutc),
        te["P"] == 0 and te["Q"] == 0 and te["xx_tt"] == 0 and te["ph_th"] == 0 and te["constraint_ratio"] == 2
        and te["yx"] == 0 and te["K"] == 0 and max(r_["cons_rel"] for r_ in rows_all) < 1e-11 and tm["Q"] != 0
        and mutc > 0.1)
    # C8
    tf = throat_first_order()
    tbx = throat_bulk(Fr(1), mut=0.5)
    tbd = throat_bulk(Fr(1), b1_0=1.5)

    def maxcon(tb):
        s, ys = tb["sol"], tb["y_s"]
        Z = s.sol(np.linspace(1e-3 * ys, 0.9 * ys, 2000))
        mom = -0.75 * Z[7] + Z[8] / 4 - Z[9] + Z[6] * (Z[2] - Z[3])
        ham = (2 * Z[4] / Z[0]**2 - Z[5] / Z[0]**2 + Z[6] / (2 * Z[1]**2) + 3 * Z[6] / Z[0]**2
               + (Z[7] + Z[8]) * (Z[2] + 2 * Z[3]) + 4 * Z[9] * Z[2] + 2 * Z[9] * Z[3])
        return float(np.max(np.abs(mom))), float(np.max(np.abs(ham)))
    mx, hx = maxcon(tbx)
    md, hd = maxcon(tbd)
    chk("C8 O(x) equations from sympy: a1'', b1'', c1'' residuals %s; momentum constraint = %s x coded; O(x) "
        "Hamiltonian residual %s; data from eq. (17): a1, b1, c1 = %s; along the solution |mom| <= %.1e, |ham| <= %.1e "
        "below 0.9 y_s; mutations: b1'' perturbed gives |mom| %.2f, wrong data b1 = 3/2 gives |ham| %.2f"
        % (tf["dd"], tf["mom_ratio"], tf["ham"], tf["data"], max(r_["mom"] for r_ in rows_all),
           max(r_["ham"] for r_ in rows_all), mx, hd),
        all(v == 0 for v in tf["dd"]) and tf["mom_ratio"] == 1 and tf["ham"] == 0
        and tf["data"] == (sp.Rational(-1, 2), sp.Rational(5, 2), 1) and all(v == 0 for v in tf["O1_zero"])
        and max(r_["mom"] for r_ in rows_all) < 1e-6 and max(r_["ham"] for r_ in rows_all) < 1e-6
        and mx > 1e-3 and hd > 1e-3)
    # C9, C10
    tv = throat_vs_owner()
    ratios = [v for y in tv["ratio"] for v in tv["ratio"][y]]
    rich = [abs((2 * tv["own"]["401/200"][y][i] - tv["own"]["201/100"][y][i]) / tv["ode"][y][i] - 1)
            for y in tv["ode"] for i in (0, 1)]
    r005 = [v for y in tv["rel"]["401/200"] for v in tv["rel"]["401/200"][y]]
    r01 = [v for y in tv["rel"]["201/100"] for v in tv["rel"]["201/100"][y]]
    chk("C9 throat against owner (ell = 2m, N = 20, y = 0.13 and 0.26): w_th, a~ within %.1f%% of the ODE at r = 2.005m "
        "and %.1f%% at 2.01m; the gap is linear in x (ratio %s), and the x -> 0 extrapolation 2 own(2.005) - own(2.01) "
        "meets the ODE to %.2f%%" % (100 * max(r005), 100 * max(r01), ", ".join("%.3f" % v for v in ratios),
                                     100 * max(rich)),
        max(r005) < 0.04 and all(abs(v - 2) <= 0.3 for v in ratios) and max(rich) < 0.005)
    chk("C10 W1(1.088) = %.4f against w_r(2.005m)/0.005 = %.4f (flat, N = 24): %.2f%%"
        % (tv["W1"], tv["wr_over_x"], 100 * abs(tv["wr_over_x"] / tv["W1"] - 1)),
        abs(tv["wr_over_x"] / tv["W1"] - 1) < 0.02)
    # C11
    sc = schwarzschild_control()
    wd = wedge()
    wm = wedge("sinh")
    chk("C11 exact controls: Schwarzschild data (ell = m) terminate %s, w_r = w_th = a~ = 0 exactly %s; the AdS4-sliced "
        "wedge is Einstein (%s), a = %s, s1 = %s, s2 = %s, equal %s, T5 bound gap %.1e; mutation sinh warp: Einstein "
        "residuals %s" % (sc["terminates"], sc["w_r"] and sc["w_th"] and sc["at"], all(v == 0 for v in wd["einstein"]),
                          wd["a"], wd["s1"], wd["s2"], wd["equal"], wd["bound_gap"],
                          [v for v in wm["einstein"] if v != 0][:1]),
        sc["terminates"] and sc["w_r"] and sc["w_th"] and sc["at"] and all(v == 0 for v in wd["einstein"])
        and wd["equal"] and wd["bound_gap"] < 1e-14 and any(v != 0 for v in wm["einstein"]))
    # C12
    ln = lemma_n()
    lm = lemma_n(sign=+1)
    chk("C12 Lemma N: Gamma^y_ab = -(1/2) d_y g_ab %s; y'' - w_r B r'^2 = %s; warped products w = %s; mutation (+1/2) "
        "connection %s, ray residual nonzero %s" % (ln["connection"], ln["ray"], ln["warped_w"], lm["connection"],
                                                   lm["ray"] != 0),
        ln["connection"] and ln["ray"] == 0 and ln["warped_w"] == [0, 0] and not lm["connection"] and lm["ray"] != 0)
    # C13
    lw, _ = ell_w()
    lc30, _ = ell_c(30)
    r0_, r1_ = rows01["0"], rows01["1"]
    chk("C13 S8's table: ell = inf y_s %.5f, y* %.5f, K(y*)/K_bs %.3g; ell = m y_s %.5f, y* %.5f, K %.3g; ell_W = %.2fm; "
        "ell_c(30) = %.2fm (pinned: %s)" % (r0_["y_s"], r0_["y_star"], r0_["K_ratio"], r1_["y_s"], r1_["y_star"],
                                           r1_["K_ratio"], lw, lc30, PIN),
        abs(r0_["y_s"] - PIN["0"]["y_s"]) < 2e-5 and abs(r0_["y_star"] - PIN["0"]["y_star"]) < 2e-5
        and abs(r0_["K_ratio"] / PIN["0"]["K_ratio"] - 1) < 5e-3 and abs(r1_["y_s"] - PIN["1"]["y_s"]) < 2e-5
        and abs(r1_["y_star"] - PIN["1"]["y_star"]) < 2e-5 and abs(r1_["K_ratio"] / PIN["1"]["K_ratio"] - 1) < 5e-3
        and abs(lw - PIN["ell_W"]) <= 0.05 and abs(lc30 - PIN["ell_c30"]) <= 0.05)
    # C14
    g = address_guard()

    def leak(separation):
        return separation
    gm_ = address_guard(extra_keys={"arrival_time": 1.0}, extra_funcs=(leak,))
    chk("C14 address guard: %d functions, no argument names a plane separation (%s); %d bank keys, none names a "
        "distance, time, redshift or speed (%s); mutation flags %s and %s" % (
            g["n_funcs"], g["bad_args"] or "none", g["n_keys"], g["bad_keys"] or "none", gm_["bad_args"],
            gm_["bad_keys"]),
        not g["bad_args"] and not g["bad_keys"] and g["n_keys"] > 10 and gm_["bad_args"] and gm_["bad_keys"])
    print("selftest: %d/%d (%.0f s)" % (ok, n, time.monotonic() - t0))
    return ok == n


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        regenerate()
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report(load_bank(), compute_live())
