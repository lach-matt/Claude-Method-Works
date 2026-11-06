#!/usr/bin/env python3
"""m22evol5: the stage-1 evolution on X*'s past and the number M_22 = (m_1)_phi1phi1(X*)/a^2 (LAMBDA0-DATA5.md section
12; CONSTANTS5.md R8.2's step (S2)-(S3)). Companion of lam0data5.py, whose Cauchy data on Sigma it evolves. Labels:
computed (exact, sympy; floating point where said), deduced (where said), READ (cited lines and .out values).

The system (N1STAR-PROOF.md Lemma 5.3 (a)-(c) at m = 1, READ by content). In lead5.py's ingoing Eddington-Finkelstein
coordinates (v, r, th, phi1, phi2), g_app = G(X, u/lam), G = g0 + lam (W + m_1) + lam^2 gh_2, u = v + lam phi_1, W =
W_TT + chi dv dv (chi stage0bd5.py's closed form, READ). Ric^H(g_app) is expanded as series {(k, n, d)}: lam^k, z^n
(z = e^(is)), d the degree in the stage-1 unknowns (m_1: eight class components; phi_1; gh_2: eight components at the
harmonics +-1, +-2, +-3), cut at lam^1 and at d = 1. The stage-1 system is: the order-1 coefficient's part of degree <= 1
vanishes at every harmonic (its d = 2 part is the e_2 term the lemma leaves to stage 2), with e_1 = 2 ell.d phi_1 -
m_1(ell, ell) = 0 (Lemma 5.3 (b), ell = d_r).

  S1 (exact) The expansion: the six non-class components vanish to order 1; the order-0 coefficient's degree-1 part
     is proportional to e_1 = -m_rr + 2 d_r phi_1 in every component (it vanishes by (b)); its degree-0 part is
     proportional to mu' - (2/9) A^2 E^2 H^2 (C^4 + S^4) (the energy condition) in vv and zero elsewhere, harmonics
     included: stage 0, with chi's closed form, is verified.
  S2 (exact) The structure: the mean equations' principal part is -(1/2) g0^ab d_a d_b on each component (no second
     derivative of another); each oscillating equation for the harmonic n carries the transport -i n d_r of its own
     component; the mean's known source is S = -(4/9) A^2 E^2 H^2 sin 2th r^-3 in v th alone (stage5.out S2, READ).
  S3 (exact; deduced) The closed subsystem: the mean equations involve gh_2 only through its first harmonic in (r th,
     th th, phi1 phi1, phi2 phi2) and through gh_2(r r); every r r equation is a homogeneous transport of gh_2(r r) at
     its own harmonic, so gh_2(r r) = 0 (zero data on Sigma); and the first-harmonic equations of (r th, th th, phi1 phi1,
     phi2 phi2) involve no other gh_2 component. So (m_1, phi_1, gh_2's first harmonic in those four) is closed, and the
     rest of gh_2 is slaved to it.
  S4 (exact) The first harmonic of D^(1) (the gauge vector's, lowered) in terms of the same unknowns, for the
     diagnostic N3.
  N1 (computed, floating point) The solve on X*'s past: tau from tau0 = -2 to tau* = 2 - a in Kerr-Schild time, the
     radial domain between the outgoing null ray through X* (backwards, DOP853) and the null surface v = 3, both
     boundaries characteristic or outflow (no boundary condition); Chebyshev-Lobatto in r (first-order form, psi =
     d_r m_1), Chebyshev-Gauss in x = cos 2th with the axis-regular variables (h_vth/sin 2th, h_th th, (h_th th - h_p2/
     S^2)/S^2, (h_th th - h_p1/C^2)/C^2) and product-rule jets, RK4 with step cfl L(tau)/Nr^2. Data: lam0data5's
     (D2, D4, D5, D7; Section 6 of LAMBDA0-DATA5.md), envelope5's envelope. M_22 at several resolutions.
  N2 (computed, floating point) Domain of dependence: the outer boundary moved to v = 2.6 leaves M_22 unchanged.
  N3 (computed, floating point) The gauge diagnostic: the first harmonic of D^(1), zero on Sigma by (F1), stays small
     against the size of its terms along the solve (the contracted Bianchi identity, not built into the equations).
  Controls (each mutates the computed path and must fail): C1 the mean source S with its sign flipped: M_22 leaves the
  band of N1; C2 gh_2's coupling into the mean dropped: M_22 leaves the band; C3 gh_2's first-harmonic data on Sigma
  set to zero (violating (F1)): the gauge diagnostic N3 fails at tau0.

    python3 checks/m22evol5.py [--selftest]       (every check; about two hours on a loaded machine)
"""
import builtins
import contextlib
import io
import math
import os
import pickle
import sys
import textwrap
import time

import mpmath
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import lam0data5 as L5             # noqa: E402  (the Sigma data: S_1, B_1, the mode ODEs, gh_2 on Sigma)

OK = {}
T0 = time.time()
I = sp.I
v, th, A = sp.symbols('v theta A', real=True)
r = sp.Symbol('r', positive=True)
Mf, Ef, Hf = sp.Function('M')(v), sp.Function('E')(v), sp.Function('H')(th)
C, S = sp.cos(th), sp.sin(th)
X = [v, r, th]
CL = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]
NM = ['vv', 'vr', 'rr', 'vt', 'rt', 'tt', 'p1', 'p2']
GC = ['rt', 'tt', 'p1', 'p2']
TOPK = [2]
E0, E1, E2, M0, M1_, M2_, H0, H1, H2 = sp.symbols('E0 E1 E2 M0 M1 M2 H0 H1 H2')
A_PT = (9 / 1250) ** (1 / 8) / 2
TAU0, TAU_STAR = -2.0, 2.0 - A_PT


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)
    sys.stdout.flush()


def el():
    return '[%.0fs]' % (time.time() - T0)


# ------------------------------------------------------------------------------------------------------------------
# series {(k, n, d)}
class T3(dict):
    def __add__(self, o):
        out = T3(self)
        for k, c in o.items():
            out[k] = out.get(k, 0) + c
        return T3({k: c for k, c in out.items() if c != 0})

    def __sub__(self, o):
        return self + o * (-1)

    def __mul__(self, o):
        if not isinstance(o, T3):
            return T3() if o == 0 else T3({k: c * o for k, c in self.items()})
        out = {}
        for (k1, n1, d1), c1 in self.items():
            for (k2, n2, d2), c2 in o.items():
                k, d = k1 + k2, d1 + d2
                if k <= TOPK[0] and d <= 1:
                    key = (k, n1 + n2, d)
                    out[key] = out.get(key, 0) + c1 * c2
        return T3({k: c for k, c in out.items() if c != 0})

    __rmul__ = __mul__

    def trunc(self, top):
        return T3({k: c for k, c in self.items() if k[0] <= top})


def const(c, k=0, n=0, d=0):
    return T3({(k, n, d): c}) if c != 0 else T3()


def make_D(phi):
    dphi = [sp.diff(phi, x) for x in X] + [0, 0]

    def D(Tt, a):
        out = {}
        for (k, n, d), c in Tt.items():
            if a < 3:
                sl = sp.diff(c, X[a])
                if sl != 0:
                    out[(k, n, d)] = out.get((k, n, d), 0) + sl
            if n != 0:
                if a == 0:
                    out[(k - 1, n, d)] = out.get((k - 1, n, d), 0) + I * n * c
                if d == 0 and dphi[a] != 0:
                    out[(k, n, 1)] = out.get((k, n, 1), 0) + I * n * c * dphi[a]
        return T3({k: c for k, c in out.items() if c != 0})
    return D


def background():
    f = 1 - Mf / r ** 2
    g = sp.diag(-f, 0, r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2)
    g[0, 1] = g[1, 0] = 1
    gi = sp.zeros(5)
    gi[0, 1] = gi[1, 0] = 1
    gi[1, 1] = f
    for i, w in zip((2, 3, 4), (r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2)):
        gi[i, i] = 1 / w
    return g, gi


def wave_ts(src_sign=1):
    K = A * Ef * Hf * r ** sp.Rational(-3, 2)
    cz, sz = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}, {1: 1 / (2 * I), -1: -1 / (2 * I)}
    a1 = {n: K * (2 * C ** 2 * cz[n] - S ** 2 * sz[n]) / 3 for n in (1, -1)}
    a2 = {n: K * (2 * S ** 2 * sz[n] - C ** 2 * cz[n]) / 3 for n in (1, -1)}
    W = [[T3() for _ in range(5)] for _ in range(5)]
    W[2][2] = T3({(1, n, 0): -2 * r ** 2 * (a1[n] + a2[n]) for n in (1, -1)})
    W[3][3] = T3({(1, n, 0): 2 * r ** 2 * C ** 2 * a1[n] for n in (1, -1)})
    W[4][4] = T3({(1, n, 0): 2 * r ** 2 * S ** 2 * a2[n] for n in (1, -1)})
    kk = r ** -2 - (v + 2) ** sp.Rational(-1, 2) * r ** sp.Rational(-3, 2)     # tau0 = -2
    pre = -A ** 2 * Ef ** 2 * Hf ** 2 / 12 * kk
    c2, s2 = sp.sin(2 * th) ** 2, 4 * sp.cos(2 * th)
    W[0][0] = T3({(1, 2, 0): pre * (c2 / 2 + s2 / (2 * I)), (1, -2, 0): pre * (c2 / 2 - s2 / (2 * I))})
    return W


def unknowns(harms):
    m1 = {nm: sp.Function('m_' + nm)(v, r, th) for nm in NM}
    G = {(nm, n): sp.Function('G%s_%s' % (('p%d' % n) if n > 0 else ('m%d' % -n), nm))(v, r, th)
         for nm in NM for n in harms}
    return m1, G, sp.Function('phi')(v, r, th)


def metric_parts(harms):
    g0, g0i = background()
    m1, G, phi = unknowns(harms)
    W = wave_ts()
    dl = [[W[i][j] for j in range(5)] for i in range(5)]
    for (i, j), nm in zip(CL, NM):
        add = const(m1[nm], 1, 0, 1)
        for n in harms:
            add = add + const(G[(nm, n)], 2, n, 1)
        dl[i][j] = dl[i][j] + add
        if i != j:
            dl[j][i] = dl[i][j]
    return g0, g0i, dl, (m1, G, phi)


def inverse(g0i, dl, top):
    gi = [[None] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            acc = const(g0i[i, j])
            for k in range(5):
                for l_ in range(5):
                    if g0i[i, k] == 0 or g0i[l_, j] == 0 or not dl[k][l_]:
                        continue
                    acc = acc - dl[k][l_] * (g0i[i, k] * g0i[l_, j])
                    if top >= 2:
                        for p in range(5):
                            for q in range(5):
                                if g0i[l_, p] != 0 and g0i[q, j] != 0 and dl[p][q]:
                                    acc = acc + dl[k][l_] * dl[p][q] * (g0i[i, k] * g0i[l_, p] * g0i[q, j])
            gi[i][j] = acc.trunc(top)
    return gi


def christoffel(gi, dg, top):
    G_ = [[[None] * 5 for _ in range(5)] for _ in range(5)]
    for a_ in range(5):
        for b_ in range(5):
            for c_ in range(b_, 5):
                acc = T3()
                for d_ in range(5):
                    comb = dg[b_][d_][c_] + dg[c_][d_][b_] - dg[d_][b_][c_]
                    if gi[a_][d_] and comb:
                        acc = acc + gi[a_][d_] * comb * sp.Rational(1, 2)
                G_[a_][b_][c_] = G_[a_][c_][b_] = acc.trunc(top)
    return G_


def ric_h(harms=(1, -1, 2, -2, 3, -3)):
    g0, g0i, dl, unk = metric_parts(harms)
    D = make_D(unk[2])
    g = [[const(g0[i, j]) + dl[i][j] for j in range(5)] for i in range(5)]
    TOPK[0] = 2
    gi = inverse(g0i, dl, 2)
    dg = [[[D(g[i][j], c).trunc(2) for j in range(5)] for i in range(5)] for c in range(5)]
    G_ = christoffel(gi, dg, 2)
    dg0 = [[[sp.diff(g0[i, j], X[c]) if c < 3 else 0 for j in range(5)] for i in range(5)] for c in range(5)]
    Gh = [[[sum(g0i[a_, d_] * (dg0[b_][d_][c_] + dg0[c_][d_][b_] - dg0[d_][b_][c_]) for d_ in range(5)) / 2
            for c_ in range(5)] for b_ in range(5)] for a_ in range(5)]
    Dv = []
    for rho in range(5):
        acc = T3()
        for a_ in range(5):
            for b_ in range(5):
                if gi[a_][b_]:
                    diff = G_[rho][a_][b_] - const(Gh[rho][a_][b_])
                    if diff:
                        acc = acc + gi[a_][b_] * diff
        Dv.append(acc.trunc(2))
    TOPK[0] = 1
    pairs = CL + [(i, j) for i in range(5) for j in range(i, 5) if (i, j) not in CL]
    names = NM + ['x%d%d' % (i, j) for i in range(5) for j in range(i, 5) if (i, j) not in CL]
    out = {}
    for (b_, c_), nm in zip(pairs, names):
        e = T3()
        for a_ in range(5):
            e = e + D(G_[a_][b_][c_], a_) - D(G_[a_][b_][a_], c_)
            for d_ in range(5):
                if G_[a_][a_][d_] and G_[d_][b_][c_]:
                    e = e + G_[a_][a_][d_] * G_[d_][b_][c_]
                if G_[a_][c_][d_] and G_[d_][b_][a_]:
                    e = e - G_[a_][c_][d_] * G_[d_][b_][a_]
        hb, hc = T3(), T3()
        for p in range(5):
            nab_c = D(Dv[p], c_) + sum((Dv[q] * Gh[p][c_][q] for q in range(5) if Gh[p][c_][q] != 0), T3())
            nab_b = D(Dv[p], b_) + sum((Dv[q] * Gh[p][b_][q] for q in range(5) if Gh[p][b_][q] != 0), T3())
            hb = hb + g[b_][p] * nab_c
            hc = hc + g[c_][p] * nab_b
        out[nm] = (e - (hb + hc) * sp.Rational(1, 2)).trunc(1)
    return out, unk


def gauge_first(harms=(1, -1, 2, -2)):
    """the first harmonic of D^(1), lowered by g0 (orders <= 1)"""
    g0, g0i, dl, unk = metric_parts(harms)
    D = make_D(unk[2])
    g = [[const(g0[i, j]) + dl[i][j] for j in range(5)] for i in range(5)]
    TOPK[0] = 1
    gi = inverse(g0i, dl, 1)
    dg = [[[D(g[i][j], c).trunc(1) for j in range(5)] for i in range(5)] for c in range(5)]
    G_ = christoffel(gi, dg, 1)
    dg0 = [[[sp.diff(g0[i, j], X[c]) if c < 3 else 0 for j in range(5)] for i in range(5)] for c in range(5)]
    Gh = [[[sum(g0i[a_, d_] * (dg0[b_][d_][c_] + dg0[c_][d_][b_] - dg0[d_][b_][c_]) for d_ in range(5)) / 2
            for c_ in range(5)] for b_ in range(5)] for a_ in range(5)]
    Dv = []
    for rho in range(5):
        acc = T3()
        for a_ in range(5):
            for b_ in range(5):
                if gi[a_][b_]:
                    diff = G_[rho][a_][b_] - const(Gh[rho][a_][b_])
                    if diff:
                        acc = acc + gi[a_][b_] * diff
        Dv.append(acc.trunc(1))
    return [sum((Dv[q] * g0[b, q] for q in range(5) if g0[b, q] != 0), T3()) for b in range(5)], unk


# ------------------------------------------------------------------------------------------------------------------
# coefficient extraction
def plainify(e):
    rep = {}
    for f, x, syms in ((Ef, v, (E0, E1, E2)), (Mf, v, (M0, M1_, M2_)), (Hf, th, (H0, H1, H2))):
        for k in (2, 1):
            rep[sp.Derivative(f, (x, k))] = syms[k]
        rep[f] = syms[0]
    for d in sorted([k for k in rep if isinstance(k, sp.Derivative)], key=lambda k: -k.derivative_count):
        e = e.subs(d, rep[d])
    e = e.subs({f: rep[f] for f in (Ef, Mf, Hf)})
    assert not e.has(sp.Derivative), 'a third derivative of a known function'
    return e


def jet_key(a):
    if isinstance(a, sp.Derivative):
        cnt = {v: 0, r: 0, th: 0}
        for x, k in a.variable_count:
            cnt[x] += k
        return (a.expr.func.__name__, (cnt[v], cnt[r], cnt[th]))
    return (a.func.__name__, (0, 0, 0))


def linear_coeffs(lin, names):
    lin = sp.expand(lin)
    atoms = set()
    for a in lin.atoms(sp.Function, sp.Derivative):
        f = a.expr if isinstance(a, sp.Derivative) else a
        if hasattr(f, 'func') and f.func.__name__ in names:
            atoms.add(a)
    syms = {}
    for a in sorted(atoms, key=lambda a: -(a.derivative_count if isinstance(a, sp.Derivative) else 0)):
        syms[a] = sp.Symbol('U%d' % len(syms))
    ls = lin
    for a, s_ in syms.items():
        ls = ls.subs(a, s_)
    ls = sp.expand(ls)
    coef = {jet_key(a): plainify(ls.coeff(s_)) for a, s_ in syms.items() if ls.coeff(s_) != 0}
    rest = sp.expand(ls - sum(ls.coeff(s_) * s_ for s_ in syms.values()))
    return coef, rest


def extract(out, unk, nmax=3):
    m1, G, phi = unk
    names = set(f.func.__name__ for f in list(m1.values()) + list(G.values()) + [phi])
    res = {}
    for nm in NM:
        for n in range(0, nmax + 1):
            coef, rest = linear_coeffs(out[nm].get((1, n, 1), 0), names)
            res[(nm, n)] = dict(coef=coef, src=plainify(sp.expand(out[nm].get((1, n, 0), 0))), rest=rest)
    return res


# ------------------------------------------------------------------------------------------------------------------
# the envelope, the grids, the solver
def envelope():
    y = sp.Symbol('y')
    beta = sp.cos(sp.pi * y / 2) ** 12 * sp.exp(-y ** 2 / (1 - y ** 2))
    fb = [sp.lambdify(y, sp.diff(beta, y, k), 'numpy') for k in range(3)]
    env, c = L5.env_float()

    def E(vv, k=0):
        vv = np.asarray(vv, dtype=float)
        yy = (2 * vv - 4) / 3
        out = np.zeros_like(yy)
        msk = np.abs(yy) < 1 - 1e-12
        out[msk] = c * fb[k](yy[msk]) * (2 / 3) ** k
        return out
    nodes = np.cos(np.pi * (np.arange(400) + 0.5) / 400)
    vs = 2 + 1.5 * nodes
    with mpmath.workdps(30):
        f = lambda t: (c * mpmath.cos(mpmath.pi * (2 * t - 4) / 6) ** 12        # noqa: E731
                       * mpmath.exp(-((2 * t - 4) / 3) ** 2 / (1 - ((2 * t - 4) / 3) ** 2))) ** 2
        vals = [float(1 + mpmath.mpf(2) / 9 * mpmath.quad(f, [0.5, 2, vv])) if vv > 0.5 else 1.0 for vv in vs]
    ch = np.polynomial.chebyshev.Chebyshev.fit(nodes, vals, 160, domain=[-1, 1])

    def mu(vv):
        vv = np.asarray(vv, dtype=float)
        out = np.where(vv <= 0.5, 1.0, 227 / 192).astype(float)
        msk = (vv > 0.5) & (vv < 3.5)
        out[msk] = ch((vv[msk] - 2) / 1.5)
        return out
    return E, mu, c


def cheb_lobatto(N):
    k = np.arange(N)
    xg = np.cos(np.pi * k / (N - 1))
    c = np.ones(N)
    c[0] = c[-1] = 2
    c *= (-1) ** k
    Xm = np.tile(xg, (N, 1)).T
    Dm = (np.outer(c, 1 / c)) / (Xm - Xm.T + np.eye(N))
    Dm = Dm - np.diag(Dm.sum(axis=1))
    return (1 - xg) / 2, -2 * Dm


def cheb_gauss(N):
    x = np.cos(np.pi * (np.arange(N) + 0.5) / N)
    V = np.polynomial.chebyshev.chebvander(x, N - 1)
    Vi = np.linalg.inv(V)
    dV, ddV = np.zeros_like(V), np.zeros_like(V)
    for k in range(N):
        ck = np.zeros(N)
        ck[k] = 1
        dV[:, k] = np.polynomial.chebyshev.chebval(x, np.polynomial.chebyshev.chebder(ck))
        ddV[:, k] = np.polynomial.chebyshev.chebval(x, np.polynomial.chebyshev.chebder(ck, 2))
    return x, dV @ Vi, ddV @ Vi, np.ones(N) @ Vi, ((-1.0) ** np.arange(N)) @ Vi


SYMS = (v, r, th, E0, E1, E2, M0, M1_, M2_, H0, H1, H2)


class Solver:
    """the closed stage-1 subsystem: m_1 (8, regular variables), pi = d_tau m_1, psi = d_r m_1, phi_1, and gh_2's
    first harmonic in (r th, th th, phi1 phi1, phi2 phi2), on r in [rho(tau), vout - tau]"""

    def __init__(self, Nr, Nx, system, env, vout=3.0, src_sign=1.0, gcouple=1.0):
        self.Nr, self.Nx, self.vout, self.src_sign, self.gcouple = Nr, Nx, vout, src_sign, gcouple
        self.xi, self.Dxi = cheb_lobatto(Nr)
        self.x, self.Dx, self.Dxx, self.ep, self.em = cheb_gauss(Nx)
        self.th = np.arccos(self.x) / 2
        self.s2 = np.sqrt(1 - self.x ** 2)
        self.S2, self.C2 = (1 - self.x) / 2, (1 + self.x) / 2
        self.E, self.mu, self.c = env
        self.funcs = system
        t = sp.Symbol('t')
        Hs = (sp.cos(t) ** 4 + sp.sin(t) ** 4) ** sp.Rational(-1, 2)
        self.H = [sp.lambdify(t, sp.diff(Hs, t, k), 'numpy')(self.th) * np.ones_like(self.th) for k in range(3)]
        self.a = A_PT
        self.FT = self.factors()

        def F(t_, y):
            m = float(self.mu(np.array([t_ + y[0]]))[0]) / y[0] ** 2
            return [(1 - m) / (1 + m)]
        self.raysol = solve_ivp(F, (TAU_STAR, TAU0 - 1e-9), [self.a], method='DOP853', rtol=1e-13, atol=1e-15,
                                dense_output=True)

    def grid(self, tau):
        y = float(self.raysol.sol(tau)[0])
        m = float(self.mu(np.array([tau + y]))[0]) / y ** 2
        L = self.vout - tau - y
        return y + L * self.xi, L, (1 - m) / (1 + m) * (1 - self.xi) - self.xi

    def dr(self, u, L):
        return (self.Dxi @ u) / L

    def dxx(self, u):
        return u @ self.Dx.T, u @ self.Dxx.T

    def theta_even(self, u):
        ux, uxx = self.dxx(u)
        return -2 * self.s2 * ux, 4 * (1 - self.x ** 2) * uxx - 4 * self.x * ux

    def factors(self):
        x, s2, S2, C2 = self.x, self.s2, self.S2, self.C2
        one = (np.ones_like(x), np.zeros_like(x), np.zeros_like(x))
        fs = (s2, 2 * x, -4 * s2)
        fS2, fS4 = (S2, s2, 2 * x), (S2 ** 2, 2 * S2 * s2, 2 * s2 ** 2 + 4 * x * S2)
        fC2, fC4 = (C2, -s2, -2 * x), (C2 ** 2, -2 * C2 * s2, 2 * s2 ** 2 - 4 * x * C2)
        neg = lambda f: tuple(-q for q in f)                    # noqa: E731
        return {'vv': [(0, one)], 'vr': [(1, one)], 'rr': [(2, one)], 'vt': [(3, fs)], 'rt': [(4, fs)],
                'tt': [(5, one)], 'p1': [(5, fC2), (7, neg(fC4))], 'p2': [(5, fS2), (6, neg(fS4))]}

    def pjets(self, flist, W):
        """value, d_th, d_thth of sum F w by the product rule (no aliasing)"""
        val, d1, d2 = 0.0, 0.0, 0.0
        for idx, (F, Fp, Fpp) in flist:
            w = W[idx]
            wx, wxx = self.dxx(w)
            wt = -2 * self.s2 * wx
            wtt = -4 * self.x * wx + 4 * (1 - self.x ** 2) * wxx
            val, d1, d2 = val + F * w, d1 + Fp * w + F * wt, d2 + Fpp * w + 2 * Fp * wt + F * wtt
        return val, d1, d2

    def args(self, tau, r1):
        rr = r1[:, None] * np.ones((1, self.Nx))
        vv = tau + rr
        th_ = np.ones((self.Nr, 1)) * self.th[None, :]
        Ev = [self.E(vv, k) for k in range(3)]
        Hv = [np.ones((self.Nr, 1)) * h[None, :] for h in self.H]
        return (vv, rr, th_, Ev[0], Ev[1], Ev[2], self.mu(vv), 2 / 9 * Ev[0] ** 2, 4 / 9 * Ev[0] * Ev[1],
                Hv[0], Hv[1], Hv[2]), rr

    def coord(self, m, G):
        mval = {nm: sum(F[0] * m[i] for i, F in self.FT[nm]) for nm in NM}
        Greg = {4: G[0], 5: G[1], 7: G[2], 6: G[3]}
        Gval = {nm: sum(F[0] * Greg[i] for i, F in self.FT[nm]) for nm in GC}
        return mval, Gval, Greg

    def rhs(self, tau, state):
        m, pi, psi, phi, G = state
        r1, L, speed = self.grid(tau)
        args, rr = self.args(tau, r1)
        psir = [self.dr(q, L) for q in psi]
        pir = [self.dr(p, L) for p in pi]
        J = {}
        for nm in NM:
            fl = self.FT[nm]
            val, ut, utt = self.pjets(fl, m)
            ur, urt, _ = self.pjets(fl, psi)
            urr, _, _ = self.pjets(fl, psir)
            pv, pt, _ = self.pjets(fl, pi)
            pr, _, _ = self.pjets(fl, pir)
            J[nm] = dict(val=val, ur=ur, ut=ut, urr=urr, urt=urt, utt=utt, pv=pv, pr=pr, pt=pt)
        phr = self.dr(phi, L)
        pht, phtt = self.theta_even(phi)
        mrr = J['rr']
        phtau = phr - mrr['val'] / 2                       # 2 d_r^EF phi_1 = m_rr^EF (Lemma 5.3 (b))
        PH = {(1, 0, 0): phtau, (0, 1, 0): mrr['val'] / 2, (0, 0, 1): pht, (0, 0, 2): phtt,
              (1, 1, 0): mrr['pv'] / 2, (0, 2, 0): (mrr['ur'] - mrr['pv']) / 2}
        _, Gv, Greg = self.coord(m, G)
        Gr = {nm: sum(F[0] * self.dr(Greg[i], L) for i, F in self.FT[nm]) for nm in GC}
        KN = {(0, 0, 0): 'val', (1, 0, 0): 'pv', (0, 0, 1): 'ut', (1, 0, 1): 'pt', (0, 0, 2): 'utt'}

        def known(nm, jet):
            j = J[nm]
            if jet in KN:
                return j[KN[jet]]
            if jet == (0, 1, 0):
                return j['ur'] - j['pv']
            if jet == (0, 1, 1):
                return j['urt'] - j['pt']
            if jet == (1, 1, 0):
                return j['pr']
            if jet == (0, 2, 0):
                return j['urr'] - 2 * j['pr']
            if jet == (2, 0, 0):
                return 0.0
            raise KeyError(jet)

        def evaluate(key):
            ks, f = self.funcs[key]
            vals = f(*args)
            alpha = 0.0
            sgn = self.src_sign if key == ('m', 'vt') else 1.0
            beta = sgn * np.broadcast_to(np.asarray(vals[-1], dtype=complex), rr.shape).copy()
            for (fname, jet), cval in zip(ks, vals[:-1]):
                cval = np.broadcast_to(np.asarray(cval, dtype=complex), rr.shape)
                if fname.startswith('m_'):
                    nm = fname[2:]
                    beta = beta + cval * known(nm, jet)
                    if nm == key[1] and key[0] == 'm' and jet in ((2, 0, 0), (0, 2, 0), (1, 1, 0)):
                        alpha = alpha + (cval if jet != (1, 1, 0) else -cval)
                    elif jet in ((2, 0, 0), (0, 2, 0), (1, 1, 0)):
                        raise ValueError('a second time derivative of another component')
                elif fname == 'phi':
                    beta = beta + cval * PH[jet]
                elif fname[:4] in ('Gp1_', 'Gm1_'):
                    nm = fname[4:]
                    if nm == 'rr':
                        continue                               # gh_2(r r) = 0 (S3)
                    gg = Gv[nm] if fname[:4] == 'Gp1_' else np.conj(Gv[nm])
                    if jet == (0, 0, 0):
                        beta = beta + cval * gg * (self.gcouple if key[0] == 'm' else 1.0)
                    elif jet == (0, 1, 0) and key[0] == 'g' and nm == key[1] and fname[:4] == 'Gp1_':
                        beta = beta + cval * Gr[nm]
                        alpha = alpha - cval
                    else:
                        raise ValueError('unexpected gh_2 jet')
                elif fname.endswith('_rr') and fname[:2] == 'Gp' or fname[:2] == 'Gm' and fname.endswith('_rr'):
                    continue
                else:
                    raise KeyError(fname)
            return alpha, beta

        Xc = {nm: np.real(-np.divide(*evaluate(('m', nm))[::-1])) for nm in NM}
        Yc = {}
        for nm in GC:
            al, be = evaluate(('g', nm))
            Yc[nm] = -be / al
        Xreg = self.regular(Xc)
        Yreg = self.regular_g(Yc)
        sp_ = speed[:, None]
        dm = [p + sp_ * q for q, p in zip(psi, pi)]
        dpi = [Xr + sp_ * self.dr(p, L) for Xr, p in zip(Xreg, pi)]
        dpsi = [self.dr(p, L) + sp_ * self.dr(q, L) for p, q in zip(pi, psi)]
        dphi = phtau + sp_ * phr
        dG = [Yr + sp_ * self.dr(g, L) for Yr, g in zip(Yreg, G)]
        return dm, dpi, dpsi, dphi, dG

    def div_axis(self, F, which):
        """F/S^2 (which = +1) or F/C^2 (which = -1), after removing F's value at the axis"""
        if which > 0:
            F = F - np.outer(F @ self.ep, (1 + self.x) / 2)
            return F / self.S2
        F = F - np.outer(F @ self.em, (1 - self.x) / 2)
        return F / self.C2

    def regular(self, Xc):
        return [Xc['vv'], Xc['vr'], Xc['rr'], Xc['vt'] / self.s2, Xc['rt'] / self.s2, Xc['tt'],
                self.div_axis(Xc['tt'] - Xc['p2'] / self.S2, 1), self.div_axis(Xc['tt'] - Xc['p1'] / self.C2, -1)]

    def regular_g(self, Yc):
        return [Yc['rt'] / self.s2, Yc['tt'], self.div_axis(Yc['tt'] - Yc['p1'] / self.C2, -1),
                self.div_axis(Yc['tt'] - Yc['p2'] / self.S2, 1)]


def load_system(res):
    funcs = {}
    for key, d in [(('m', nm), res[(nm, 0)]) for nm in NM] + [(('g', nm), res[(nm, 1)]) for nm in GC]:
        ks = list(d['coef'].keys())
        exprs = [d['coef'][k].subs(A, 1) for k in ks] + [d['src'].subs(A, 1)]
        funcs[key] = (ks, sp.lambdify(SYMS, exprs, modules='numpy', cse=True))
    return funcs


# ------------------------------------------------------------------------------------------------------------------
# the Cauchy data on Sigma (lam0data5's construction; LAMBDA0-DATA5.md section 6)
def mode_setup():
    F0, _, _ = L5.gauge(g2=None)
    out, _ = L5.order1_mean(g2=L5.harm_sub(F0))
    CO = {nm: {k: sp.factor(sp.simplify(c)) for k, c in L5.coeffs(X_.mean(1)).items()} for nm, X_ in out.items()}
    Hrec = (L5.C ** 4 + L5.S ** 4) ** sp.Rational(-1, 2)
    Mc = {(nm, k): sp.factor(sp.simplify(c.subs(L5.Hf, Hrec).subs(L5.mp, sp.Rational(2, 9) * L5.A ** 2
                                                                         * L5.Ef ** 2)))
          for nm in CO for k, c in CO[nm].items()}
    _, fode, _ = L5.mode_odes(Mc)
    return fode


KS = (1, 3, 5, 7, 9, 11, 13)


def cauchy_data(Sv, fode, g_data=True):
    r1, L, _ = Sv.grid(TAU0)
    E, mu = Sv.E, Sv.mu
    envf = lambda vv: float(E(np.array([vv]))[0])                # noqa: E731
    sols = L5.solve_modes(fode, envf, 2.5, float(r1.max()) + 1e-9, 1.0, KS)
    Nr, Nx = Sv.Nr, Sv.Nx
    av, ar, at, wv, qv = (np.zeros((Nr, Nx)) for _ in range(5))
    t = sp.Symbol('t')
    for k in KS:
        Pk = sp.legendre(k, sp.cos(2 * t))
        P = sp.lambdify(t, Pk, 'numpy')(Sv.th) * np.ones_like(Sv.th)
        dP = sp.lambdify(t, sp.diff(Pk, t), 'numpy')(Sv.th) * np.ones_like(Sv.th)
        sk = float(L5.sigma_k(k))
        for i, rr in enumerate(r1):
            if rr < 2.5:
                continue
            y = sols[k].sol(rr)
            da, dw, dq = fode(rr, envf(TAU0 + rr), y[3], k, y[0], y[1], y[2], sk)
            av[i] += y[0] * P
            ar[i] += da * P
            at[i] += y[0] * dP
            wv[i] += y[1] * P
            qv[i] += y[2] * dP
    rr = r1[:, None] * np.ones((1, Nx))
    vv = TAU0 + rr
    muv, mup = mu(vv), 2 / 9 * E(vv) ** 2
    Lam, m = rr ** 2 + muv, muv / rr ** 2
    N0 = rr / np.sqrt(Lam)
    M1rr = muv * (2 * rr ** 5 * Lam * ar + (2 * muv ** 3 + 4 * muv ** 2 * rr ** 2 + 4 * muv * rr ** 4
                                            - 2 * mup * rr ** 5 - mup * muv * rr ** 3) * av) / (4 * rr ** 6 * Lam ** 1.5)
    M1rt = muv * at / (2 * rr * np.sqrt(Lam))
    cM = muv * (2 * rr ** 4 - muv ** 2) / (2 * rr ** 4 * Lam ** 1.5)
    Hrr, Hrt, hA = -2 * N0 * M1rr, 2 * N0 * (qv - M1rt), 2 * N0 * (wv - cM * av)
    Ttt = -((1 - m) * Hrr + 3 * hA) / (1 + m)
    Ttr = (m * Hrr + 0.5 * (1 - m) * ar + (3 / rr - muv / rr ** 3) * av) / (1 + m)
    Tth = (m * Hrt - 0.5 * (1 - m) * at) / (1 + m)
    s2 = Sv.s2[None, :]
    z = np.zeros((Nr, Nx))
    mst = [z.copy(), z.copy(), av.copy(), z.copy(), z.copy(), z.copy(), z.copy(), z.copy()]
    pst = [Ttt, Ttr - Ttt, Ttt - 2 * Ttr + Hrr, Tth / s2, (Hrt - Tth) / s2, rr ** 2 * hA, z.copy(), z.copy()]
    psi = [Sv.dr(u, L) for u in mst]
    psi[2] = ar.copy()
    thg = Sv.th[None, :]
    Ev = E(vv)
    al = Ev / (6 * rr ** 1.5) * (5 * Sv.H[0][None, :] * np.sin(2 * thg) + 2 * np.sin(thg) ** 2 * Sv.H[1][None, :])
    be = Ev / (6 * rr ** 1.5) * (5 * Sv.H[0][None, :] * np.sin(2 * thg) - 2 * np.cos(thg) ** 2 * Sv.H[1][None, :])
    G = [(-(al - 1j * be) / s2) if g_data else z.astype(complex), z.astype(complex), z.astype(complex),
         z.astype(complex)]
    return (mst, pst, psi, z.copy(), G)


# ------------------------------------------------------------------------------------------------------------------
def axpy(state, k, h):
    return tuple([u + h * d for u, d in zip(a, b)] if isinstance(a, list) else a + h * b for a, b in zip(state, k))


def rk4(Sv, state, cfl, tend=TAU_STAR, hook=None):
    tau, steps = TAU0, []
    t = tau
    while t < tend - 1e-14:
        _, Lt, _ = Sv.grid(t)
        hh = min(cfl * Lt / Sv.Nr ** 2, tend - t)
        steps.append(hh)
        t += hh
    for i, h in enumerate(steps):
        k1 = Sv.rhs(tau, state)
        k2 = Sv.rhs(tau + h / 2, axpy(state, k1, h / 2))
        k3 = Sv.rhs(tau + h / 2, axpy(state, k2, h / 2))
        k4 = Sv.rhs(tau + h, axpy(state, k3, h))
        comb = tuple([(p + 2 * q + 2 * s_ + w) / 6 for p, q, s_, w in zip(a, b, c, d)] if isinstance(a, list)
                     else (a + 2 * b + 2 * c + d) / 6 for a, b, c, d in zip(k1, k2, k3, k4))
        state = axpy(state, comb, h)
        tau += h
        if hook is not None and i == len(steps) // 2:
            hook(tau, state)
    return state, tau, len(steps)


def m22(Sv, state):
    m = state[0]
    return float(((m[5][0] - m[7][0]) @ Sv.ep) / Sv.a ** 2)        # (T - B)(r = a, x = 1)/a^2: p1 = C^2 (T - C^2 B)


def gauge_residual(Sv, gfun, state, tau):
    m, pi, psi, phi, G = state
    r1, L, _ = Sv.grid(tau)
    args, rr = Sv.args(tau, r1)
    mval, Gval, _ = Sv.coord(m, G)
    Gval = dict(Gval, rr=0 * G[0])
    pht, _ = Sv.theta_even(phi)
    out = {}
    for b, (ks, f) in gfun.items():
        vals = f(*args)
        tot = np.broadcast_to(np.asarray(vals[-1], dtype=complex), rr.shape).copy()
        scale = np.abs(tot).copy()
        for (fname, jet), c in zip(ks, vals[:-1]):
            c = np.broadcast_to(np.asarray(c, dtype=complex), rr.shape)
            if fname.startswith('Gp1_'):
                term = c * Gval[fname[4:]]
            elif fname.startswith('m_'):
                term = c * mval[fname[2:]]
            elif fname == 'phi' and jet == (0, 0, 1):
                term = c * pht
            else:
                raise KeyError((fname, jet))
            tot, scale = tot + term, scale + np.abs(term)
        out[b] = (float(np.max(np.abs(tot))), float(np.max(scale)))
    return out
