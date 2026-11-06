#!/usr/bin/env python3
"""lam0data5: workstream D, round 8's three blocks on lambda0 (CONSTANTS5.md R8.2): the stage-1 data on Sigma (S_1,
B_1), an admissible envelope, and the stability constant over X*'s past (LAMBDA0-DATA5.md). Labels: computed (exact,
sympy; floating point where said), certified (Arb balls, python-flint; exact rationals), READ (cited lines and .out
values), deduced (where said).

Conventions (N1STAR-PROOF.md sections 0-6, READ by content). Kerr-Schild coordinates (tau, r, th, phi1, phi2) of 0.1,
g0 = eta + (mu(v)/r^2) dv dv, v = tau + r; Sigma = {tau = tau0}, on which v = tau0 + r and the phase is s = v/lam.
The approximant (5.1) at stage 1: g_app = g0 + lam W(X, u/lam) + lam m_1 + lam^2 gh_2(X, u/lam) + ..., u = v + lam
phi_1 + ..., W = W_TT + chi dv dv (lead5.py). Lemma 6.2 at m = 1: phi_1 = 0 and (m_1)_{tau .} = 0 on Sigma, h_1 = a dr dr
(the spatial part of m_1), so d_tau phi_1 = -(1/2) m_1(ell, ell) = -a/2 there (Lemma 5.3 (b), ell = g0^-1 dv = -d_tau +
d_r); chi = 0 on Sigma with its tangential derivatives (stage 0's data). The order-1 mean of K is the free datum Q_1 =
w Pi + q (dr dth + dth dr) ("given h_m, Q_m fixes d_tau of that spatial part"). A profile f(v, r, th, s) is
differentiated along Sigma by d_r -> d_r + d_v + lam^-1 d_s, and in tau (oscillating profiles) by d_v + (lam^-1 +
d_tau phi_1) d_s; series are carried as {(k, n): coefficient of lam^k z^n}, z = e^(i s), truncated at k = 1 (the
order-1 mean is complete at that truncation: every lam^2 term enters it only through a fast derivative multiplied by
a non-oscillating factor, whose mean is zero; DOC below).

  D1 (exact) The gauge vector on Sigma: D^(0) = 0, and the gh_2-dependence of D^(1) is Pol(d_s gh_2) (lowered by g0),
     Pol(Y) = Y(ell, .) - (1/2) dv tr_g0 Y, for a generic gh_2 (the eight class components, harmonics 1 and 2).
  D2 (exact) Step (i) at m = 1: the first harmonic of D^(1) at gh_2 = 0 has only a th component, independent of a (the
     terms of Lambda_1 cancel: W(ell, .) = 0, tr W = 0, W angular); with Pol^+ = Pol^T (Pol Pol^T)^-1 (Euclidean in the
     Cartesian (tau, x)), gh_2's first harmonic on Sigma is G2_(tau th) = -G2_(r th) = (A E/(6 r^(3/2))) [(5 H sin 2th
     + 2 S^2 H') cos s + (5 H sin 2th - 2 C^2 H') sin s], all other components 0; its second harmonic (from chi's d_tau
     and the W^2 terms) is printed. Step (ii): the mean of D^(1) = 0 fixes d_tau (m_1)_(tau .) (printed).
  D3 (exact) The constraint map (J_r, J_th, rho) of the slice data: no lam^-1 term; its order-0 mean is proportional to
     mu' - (2/9) A^2 E^2 H^2 (C^4 + S^4) in every component (stage 0's energy condition, lead5 L2).
  D4 (exact) The order-1 mean: <Phi^(1)> = P(h_1, Q_1) + B_1 a - S_1, P the linearisation at g0's data, equal to
     data5.py's lin_0 coefficient by coefficient (40 digits at three points), and, with Lambda := r^2 + mu,
        B_1 = H^2 (C^4 + S^4) A^2 E^2 a (-(1/3) Lambda^(-3/2), 0, (2/3) r Lambda^-2)          in (J_r, J_th, rho),
        S_1 = (0, -A^2 E^2 H^2 sin 2th / (3 r^2 Lambda^(1/2)), 0).
     B_1 is algebraic in a; the phase d_tau phi_1 = -a/2 carries the part (-(1/3) r^-4 Lambda^(1/2), 0, (1/3) r^-3)
     A^2 E^2 H^2 (C^4 + S^4) a; gh_2 (both harmonics) and chi's d_tau contribute nothing (recomputed with each off).
  D5 (exact) The system decouples: with the record's H (H^2 (C^4 + S^4) = 1), every coefficient of P + B_1 is free of th
     except the angular operators, which are -(1/Lambda) Lap on a (rho) and -(2/r^2) div on q dth (J_r), Lap P_k(cos 2th)
     = -4 k (k + 1) P_k; and H^2 sin 2th = sum_k sigma_k d_th P_k(cos 2th), sigma_k = -((2k+1)/2) int_-1^1 atan(x) P_k(x)
     dx (exact, k <= 11; 0 for even k). So a = sum a_k P_k, w = sum w_k P_k, q = sum q_k d_th P_k solve, for each k, a
     linear system of three ODEs in r (printed), from zero data at r = a: Lemma 6.4's system is solved mode by mode.
  D6 (computed, floating point) The identity D4 at finite lam, by a route that shares nothing with the two-scale
     series: the constraint map of the slice data of g_app (test a, w, q; E = 1 + v/4, mu' = (2/9) E^2, the record's
     H, A = 1), evaluated pointwise by second-order jets, integrated against a Gaussian in r (sd 0.3 at r = 3.5, where
     every oscillating term is O(lam^oo)); at lam = 1/32 and 1/64 and th = 0.35, 0.8, 1.2, the remainder W(lam) -
     lam int f <Phi^(1)> drops by 2^p, p >= 1.6, in every component.
  D7 (computed, floating point) The stage-1 data on Sigma for envelope5's envelope: the mode ODEs (k = 1, ..., 11, odd)
     integrated (Radau, rtol 1e-11, and 1e-9 as a check) from r = 5/2 (below it E = 0 and the data vanish) to 11/2; mu
     integrated beside them reaches 227/192; sizes on the past of X* (r <= 4) and on the slice.
  D8 (computed, floating point) The residual drops by the predicted order: for E = 1 + v/4, the stage-0 data have the
     weak J_th residual of order lam (p in [0.85, 1.15]); with the stage-1 data of D5 (solved, k <= 11) it is of order
     lam^2 (p >= 1.6), J_r and rho of order lam^2 in both.
  E1 (proved; computed) The envelope env = c beta((2v - 4)/3), beta(y) = cos^12(pi y/2) exp(-y^2/(1 - y^2)) on |y| < 1
     (envelope5.py) is admissible: beta = e cos^12(pi y/2) phi(1 - y^2), phi(t) = exp(-1/t) (t > 0), 0 (t <= 0), and
     phi^(k)(t) = P_k(1/t) exp(-1/t) with P_(k+1)(x) = x^2 (P_k(x) - P_k'(x)) (sympy, k <= 8), each -> 0 as t -> 0+
     (sympy limit): C^oo, supp env = [1/2, 7/2]; int env^2 = 105/128 (c in envelope5's certified interval, READ, and the
     integrated mu of D7 ends at 227/192); mu' = (2/9) A^2 env^2 >= 0.
  G1 (certified) X*'s past by domain of dependence: a piecewise-linear rho~(tau) from (tau*, a) backwards (2000 pieces,
     exact rationals) whose slopes satisfy rho~' >= (1 - m)/(1 + m), m = mu/rho~^2 >= 1/rho~^2 (mu >= mu0 = 1): the
     surface r = rho~(tau) is a future boundary (every future causal vector Y has Y^r <= ((1 - m)/(1 + m)) Y^tau).
  G2 (certified) The local energy rate of Lemma 2.3 at gt = g0 (stage1rate5's forms, imported): kappa(r) := (1/r)
     sup |lambda(r M, Q)| on 600 r-cells of [a, b(tau0)] (Arb); and its suffix maxima.
  G3 (certified) Lemma G: E_rho~(tau*) <= e^(int kappa(rho~(tau)) dtau) (E_rho~(tau0) + ...); the principal-part
     factor e^((1/2) int kappa) over X*'s past, against the record's e^(kappa Dtau*/2) = 5.103e10 (classm5 K5).
  Controls (each mutates the computed path and must fail): C1 S_1 with its sign flipped: D6's order test fails; C2 the
  phase d_tau phi_1 = -a/2 dropped from the data: D6 fails; C3 B_1 dropped from the prediction: D6 fails; C4 the
  numerics' envelope sin^4: E1's smoothness fails (its fourth derivative jumps at v = 1/2); C5 X* perturbed to r = a +
  1/100: the base of the chain, (4/3) env(2) r^(-3/2) >= 12.593309, fails there; C6 G1 with slopes 1.25 times too
  steep: the future-boundary check fails.

    python3 checks/lam0data5.py        (about 40 minutes on a loaded machine)
"""
import builtins
import contextlib
import io
import math
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import flint
import mpmath
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import stage1rate5 as SR          # noqa: E402  (forms, to_arb_fn, A_LO, B_HI, MU0, MU_END, C_ENV)
    import data5 as D5                # noqa: E402  (lin_0, the record's linearisation)

OK = {}
B_FORM = {}
T0 = time.time()
C_LO, C_HI = flint.arb('1.32407110621'), flint.arb('1.3241034918')   # READ envelope5.out E1
CAPP = Fr(12593309, 10 ** 6)                                         # READ lzerotrace5.out T3 (operator norm)
RECORD_K5 = flint.arb('5.103e10')                                    # READ classm5.out K5


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)
    sys.stdout.flush()


def el():
    return '[%.0fs]' % (time.time() - T0)


# ------------------------------------------------------------------------------------------------------------------
# the two-scale series on Sigma
I = sp.I
r = sp.Symbol('r', positive=True)
th, v, A = sp.symbols('theta v A', real=True)
mu = sp.Function('mu')(v)
Ef = sp.Function('E')(v)
Hf = sp.Function('H')(th)
af = sp.Function('a')(r, th)
wf = sp.Function('w')(r, th)
qf = sp.Function('q')(r, th)
C, S = sp.cos(th), sp.sin(th)
mp, mpp = sp.symbols('mp mpp')
TOP = [1]


class TS(dict):
    """{(k, n): coefficient of lam^k z^n}; products truncated at k = TOP"""

    def copy(self):
        return TS(dict(self))

    def __add__(self, o):
        out = TS(dict(self))
        if not isinstance(o, TS):
            o = TS.const(o)
        for key, c in o.items():
            out[key] = out.get(key, 0) + c
        return out.clean()

    __radd__ = __add__

    def __neg__(self):
        return TS({k: -c for k, c in self.items()})

    def __sub__(self, o):
        return self + (-o if isinstance(o, TS) else TS.const(-o))

    def __mul__(self, o):
        if not isinstance(o, TS):
            return TS() if o == 0 else TS({k: c * o for k, c in self.items()})
        out = {}
        for (k1, n1), c1 in self.items():
            for (k2, n2), c2 in o.items():
                if k1 + k2 <= TOP[0]:
                    key = (k1 + k2, n1 + n2)
                    out[key] = out.get(key, 0) + c1 * c2
        return TS(out).clean()

    __rmul__ = __mul__

    def clean(self, expand=False):
        out = TS()
        for key, c in self.items():
            c = sp.expand(c) if expand else c
            if c != 0:
                out[key] = c
        return out

    def trunc(self, top):
        return TS({k: c for k, c in self.items() if k[0] <= top})

    @staticmethod
    def const(c, k=0, n=0):
        return TS({(k, n): c}) if c != 0 else TS()

    def mean(self, k):
        return self.get((k, 0), sp.Integer(0))


def Dr(T):
    out = {}
    for (k, n), c in T.items():
        sl = sp.diff(c, r) + sp.diff(c, v)
        if sl != 0:
            out[(k, n)] = out.get((k, n), 0) + sl
        if n != 0:
            out[(k - 1, n)] = out.get((k - 1, n), 0) + I * n * c
    return TS(out).clean()


def Dth(T):
    return TS({key: sp.diff(c, th) for key, c in T.items()}).clean()


def Dt_osc(T, phit):
    out = {}
    for (k, n), c in T.items():
        sl = sp.diff(c, v)
        if sl != 0:
            out[(k, n)] = out.get((k, n), 0) + sl
        if n != 0:
            out[(k - 1, n)] = out.get((k - 1, n), 0) + I * n * c
            if phit != 0:
                out[(k, n)] = out.get((k, n), 0) + I * n * c * phit
    return TS(out).clean()


def wave_comps():
    """W_TT's (th th, phi1 phi1, phi2 phi2) components, the factor lam included (lead5.py's wave in z-form)"""
    K = A * Ef * Hf * r ** sp.Rational(-3, 2)
    cz, sz = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}, {1: 1 / (2 * I), -1: -1 / (2 * I)}
    a1 = {n: K * (2 * C ** 2 * cz[n] - S ** 2 * sz[n]) / 3 for n in (1, -1)}
    a2 = {n: K * (2 * S ** 2 * sz[n] - C ** 2 * cz[n]) / 3 for n in (1, -1)}
    return (TS({(1, n): -2 * r ** 2 * (a1[n] + a2[n]) for n in (1, -1)}),
            TS({(1, n): 2 * r ** 2 * C ** 2 * a1[n] for n in (1, -1)}),
            TS({(1, n): 2 * r ** 2 * S ** 2 * a2[n] for n in (1, -1)}))


def chidot_ts():
    """d_tau chi on Sigma (KS; = d_v at fixed r): READ stage0bd5.py's closed form chi = -(1/12) A^2 E^2 H^2 (4 cos 2th
    sin 2s + sin^2 2th cos 2s) (r^-2 - (v - tau0)^(-1/2) r^(-3/2)), zero on Sigma, whose d_v there (v - tau0 = r) is
    -(1/24) A^2 E^2 H^2 (4 cos 2th sin 2s + sin^2 2th cos 2s) r^-3; the factor lam included"""
    pre = -A ** 2 * Ef ** 2 * Hf ** 2 / (24 * r ** 3)
    c2, s2 = sp.sin(2 * th) ** 2, 4 * sp.cos(2 * th)
    out = {}
    for n in (2, -2):
        out[(1, n)] = pre * (c2 / 2 + s2 * (sp.Rational(1, 2) / I if n == 2 else -sp.Rational(1, 2) / I))
    return TS(out)


def tsm(n):
    return [[TS() for _ in range(n)] for _ in range(n)]


# ------------------------------------------------------------------------------------------------------------------
# D1-D2: the gauge vector on Sigma (5D)
CL = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]
NM = ['tt', 'tr', 'rr', 'tth', 'rth', 'thth', 'p1p1', 'p2p2']


def background5():
    m = mu / r ** 2
    g0, gi0 = sp.zeros(5), sp.zeros(5)
    g0[0, 0], g0[0, 1], g0[1, 0], g0[1, 1] = -1 + m, m, m, 1 + m
    g0[2, 2], g0[3, 3], g0[4, 4] = r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2
    gi0[0, 0], gi0[0, 1], gi0[1, 0], gi0[1, 1] = -1 - m, m, m, 1 - m
    gi0[2, 2], gi0[3, 3], gi0[4, 4] = 1 / r ** 2, 1 / (r ** 2 * C ** 2), 1 / (r ** 2 * S ** 2)
    return g0, gi0


def gauge(g2=None, phase=True, chi=False):
    """the lowered D(g_app) on Sigma as TS (orders <= 1); g2: {component name: TS at order 2} or None"""
    g0, gi0 = background5()
    Wth, Wp1, Wp2 = wave_comps()
    phit = -af / 2 if phase else 0
    W, M1, G2 = tsm(5), tsm(5), tsm(5)
    W[2][2], W[3][3], W[4][4] = Wth, Wp1, Wp2
    M1[1][1] = TS.const(af, 1, 0)
    if g2:
        for (i, j), nm in zip(CL, NM):
            if nm in g2:
                G2[i][j] = G2[j][i] = g2[nm]
    g = [[TS.const(g0[i, j]) + W[i][j] + M1[i][j] + G2[i][j] for j in range(5)] for i in range(5)]
    dg = [tsm(5) for _ in range(5)]
    cd = chidot_ts() if chi else TS()
    for i in range(5):
        for j in range(5):
            dg[0][i][j] = (TS.const(sp.diff(g0[i, j], v)) + Dt_osc(W[i][j], phit) + Dt_osc(G2[i][j], 0)).trunc(1)
            if chi and i < 2 and j < 2:
                dg[0][i][j] = dg[0][i][j] + cd
            dg[1][i][j] = Dr(g[i][j]).trunc(1)
            dg[2][i][j] = Dth(g[i][j]).trunc(1)
    gi = tsm(5)
    for i in range(5):
        for j in range(5):
            acc = TS.const(gi0[i, j])
            for k in range(5):
                for l_ in range(5):
                    if gi0[i, k] != 0 and gi0[l_, j] != 0 and (W[k][l_] or M1[k][l_] or G2[k][l_]):
                        acc = acc - (W[k][l_] + M1[k][l_] + G2[k][l_]) * (gi0[i, k] * gi0[l_, j])
            gi[i][j] = acc.trunc(1)
    dg0 = [[[sp.diff(g0[i, j], v) if c == 0 else (sp.diff(g0[i, j], r) + sp.diff(g0[i, j], v) if c == 1 else
              (sp.diff(g0[i, j], th) if c == 2 else 0)) for j in range(5)] for i in range(5)] for c in range(5)]
    Dv = []
    for rho_ in range(5):
        acc = TS()
        for a_ in range(5):
            for b_ in range(5):
                if not gi[a_][b_]:
                    continue
                G, G0 = TS(), 0
                for sg in range(5):
                    comb = dg[a_][sg][b_] + dg[b_][sg][a_] - dg[sg][a_][b_]
                    if comb and gi[rho_][sg]:
                        G = G + gi[rho_][sg] * comb * sp.Rational(1, 2)
                    G0 += gi0[rho_, sg] * (dg0[a_][sg][b_] + dg0[b_][sg][a_] - dg0[sg][a_][b_]) / 2
                diff = (G - G0).trunc(1)
                if diff:
                    acc = acc + gi[a_][b_] * diff
        Dv.append(acc.trunc(1))
    return [sum((Dv[q_] * g0[b_, q_] for q_ in range(5) if g0[b_, q_] != 0), TS()) for b_ in range(5)], g0, gi0


def pol(Y, g0, gi0):
    ell, dv = [-1, 1, 0, 0, 0], [1, 1, 0, 0, 0]
    tr = sum(gi0[i, j] * Y[i, j] for i in range(5) for j in range(5))
    return [sum(ell[i] * Y[i, b] for i in range(5)) - sp.Rational(1, 2) * dv[b] * tr for b in range(5)]


def polplus(c, g0, gi0):
    """the Euclidean-minimal preimage in the class of the class covector (c_tau, c_r, c_th) (coordinate components)"""
    sig = [1, 1, r, r * C, r * S]
    ys = sp.symbols('y0:8')
    Y = sp.zeros(5)
    for (i, j), y in zip(CL, ys):
        Y[i, j] = Y[j, i] = y * (1 if i == j else 1 / sp.sqrt(2)) * sig[i] * sig[j]
    pv = pol(Y, g0, gi0)
    Mx = sp.Matrix([[sp.diff(pv[b], y) / sig[b] for y in ys] for b in range(3)])
    yv = Mx.T * (Mx * Mx.T).applyfunc(sp.simplify).inv() * sp.Matrix([c[b] / sig[b] for b in range(3)])
    return {nm: sp.simplify(y * (1 if i == j else 1 / sp.sqrt(2)) * sig[i] * sig[j])
            for ((i, j), nm), y in zip(zip(CL, NM), list(yv))}


# ------------------------------------------------------------------------------------------------------------------
# D3-D4: the constraint map of the slice data, two-scale
def christoffel4(gi, dg):
    G = [tsm(4) for _ in range(4)]
    for a_ in range(4):
        for b_ in range(4):
            for c_ in range(b_, 4):
                acc = TS()
                for d_ in range(4):
                    comb = dg[b_][d_][c_] + dg[c_][d_][b_] - dg[d_][b_][c_]
                    if gi[a_][d_] and comb:
                        acc = acc + gi[a_][d_] * comb * sp.Rational(1, 2)
                G[a_][b_][c_] = G[a_][c_][b_] = acc.trunc(1).clean(expand=True)
    return G


def slice_data(phase=True, g2=None, chidot=False):
    """(gamma, gamma^-1, Gamma, K) on Sigma; g2 = {'rth': TS, 'tth': TS, ...} (orders 2) or None; K's order-1 mean is
    replaced by Q = w Pi + q (dr dth + dth dr); also returns K's order-1 mean before the replacement"""
    m = mu / r ** 2
    Wth, Wp1, Wp2 = wave_comps()
    g0 = [1 + m, r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2]
    gam = tsm(4)
    for i in range(4):
        gam[i][i] = TS.const(g0[i])
    gam[0][0] = gam[0][0] + TS.const(af, 1, 0)
    gam[1][1], gam[2][2], gam[3][3] = gam[1][1] + Wth, gam[2][2] + Wp1, gam[3][3] + Wp2
    sp_ix = {'rr': (0, 0), 'rth': (0, 1), 'thth': (1, 1), 'p1p1': (2, 2), 'p2p2': (3, 3)}
    for nm, (i, j) in sp_ix.items():
        if g2 and nm in g2:
            gam[i][j] = gam[i][j] + g2[nm]
            if i != j:
                gam[j][i] = gam[i][j]
    TOP[0] = 2
    gi0 = [1 / x for x in g0]
    dl = [[gam[i][j] - TS.const(g0[i] if i == j else 0) for j in range(4)] for i in range(4)]
    gi = tsm(4)
    for i in range(4):
        for j in range(4):
            acc = TS.const(gi0[i] if i == j else 0) - dl[i][j] * (gi0[i] * gi0[j])
            for k in range(4):
                if dl[i][k] and dl[k][j]:
                    acc = acc + dl[i][k] * dl[k][j] * (gi0[i] * gi0[k] * gi0[j])
            gi[i][j] = acc.trunc(2).clean(expand=True)
    TOP[0] = 1
    dg = [tsm(4) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dg[0][i][j], dg[1][i][j] = Dr(gam[i][j]).trunc(1), Dth(gam[i][j]).trunc(1)
    G = christoffel4(gi, dg)
    beta = [TS.const(m), TS(), TS(), TS()]
    for nm, k in (('tr', 0), ('tth', 1)):
        if g2 and nm in g2:
            beta[k] = beta[k] + g2[nm]
    N2 = (TS.const(1 - m) + gi[0][0] * beta[0] * beta[0]).trunc(1)
    N20 = sp.simplify(N2.get((0, 0), 0))
    Ninv = (TS.const(1) - TS({k: c / N20 for k, c in N2.items() if k != (0, 0)}) * sp.Rational(1, 2)) * (
        1 / sp.sqrt(N20))
    phit = -af / 2 if phase else 0
    Wd = tsm(4)
    Wd[1][1], Wd[2][2], Wd[3][3] = Wth, Wp1, Wp2
    der = [Dr, Dth, lambda x: TS(), lambda x: TS()]
    K = tsm(4)
    for i in range(4):
        for j in range(i, 4):
            dt = TS.const(sp.diff(g0[i], v) if i == j else 0) + Dt_osc(Wd[i][j], phit)
            for nm, (p_, q_) in sp_ix.items():
                if g2 and nm in g2 and (p_, q_) == (i, j):
                    dt = dt + Dt_osc(g2[nm], 0)
            if chidot and (i, j) == (0, 0):
                dt = dt + chidot_ts()
            lie = der[i](beta[j]) + der[j](beta[i])
            for k in range(4):
                if beta[k] and G[k][i][j]:
                    lie = lie - G[k][i][j] * beta[k] * 2
            K[i][j] = K[j][i] = ((dt - lie) * Ninv * sp.Rational(1, 2)).trunc(1).clean(expand=True)
    Kmean1 = [[K[i][j].mean(1) for j in range(4)] for i in range(4)]
    Q = [[0] * 4 for _ in range(4)]
    Q[0][1] = Q[1][0] = qf
    for i in (1, 2, 3):
        Q[i][i] = wf * g0[i]
    for i in range(4):
        for j in range(4):
            Kn = K[i][j].copy()
            Kn[(1, 0)] = Q[i][j]
            K[i][j] = Kn.clean()
    return gam, gi, G, K, Kmean1


def constraints(gi, G, K):
    """(J_r, J_th, rho) as TS: the order-1 mean is complete (DOC); the order-1 oscillating part is not used"""
    n = 4
    der = [Dr, Dth, lambda x: TS(), lambda x: TS()]
    R = TS()
    for b_ in range(n):
        for c_ in range(n):
            if not gi[b_][c_]:
                continue
            e = TS()
            for a_ in range(n):
                if G[a_][b_][c_]:
                    e = e + der[a_](G[a_][b_][c_])
                if G[a_][b_][a_]:
                    e = e - der[c_](G[a_][b_][a_])
                for d_ in range(n):
                    if G[a_][a_][d_] and G[d_][b_][c_]:
                        e = e + G[a_][a_][d_] * G[d_][b_][c_]
                    if G[a_][c_][d_] and G[d_][b_][a_]:
                        e = e - G[a_][c_][d_] * G[d_][b_][a_]
            R = R + gi[b_][c_] * e
    trK = sum((gi[i][j] * K[i][j] for i in range(n) for j in range(n) if gi[i][j] and K[i][j]), TS())
    Ku = [[sum((gi[i][k] * K[k][j] for k in range(n) if gi[i][k] and K[k][j]), TS()) for j in range(n)]
          for i in range(n)]
    K2 = sum((Ku[i][j] * Ku[j][i] for i in range(n) for j in range(n) if Ku[i][j] and Ku[j][i]), TS())
    rho_ = R - K2 + trK * trK
    out = []
    for i in range(2):
        div = TS()
        for j in range(n):
            for k in range(n):
                if not gi[j][k]:
                    continue
                cov = der[k](K[i][j])
                for l_ in range(n):
                    if G[l_][k][i] and K[l_][j]:
                        cov = cov - G[l_][k][i] * K[l_][j]
                    if G[l_][k][j] and K[i][l_]:
                        cov = cov - G[l_][k][j] * K[i][l_]
                div = div + gi[j][k] * cov
        out.append((-div + der[i](trK)) * 2)
    return out[0], out[1], rho_


# ------------------------------------------------------------------------------------------------------------------
# jets of the unknowns, coefficient forms
SYM = {}
for _f, _nm in ((af, 'a'), (wf, 'w'), (qf, 'q')):
    SYM[_f] = sp.Symbol(_nm)
    for _i in range(3):
        for _j in range(3 - _i):
            if _i + _j:
                SYM[sp.Derivative(_f, *([r] * _i + [th] * _j))] = sp.Symbol('%s_%s%s' % (_nm, 'r' * _i, 't' * _j))


def tojet(e):
    e = e.subs(sp.Derivative(mu, (v, 2)), mpp).subs(sp.Derivative(mu, v), mp)
    e = e.subs({k: SYM[k] for k in sorted([k for k in SYM if isinstance(k, sp.Derivative)],
                                           key=lambda k: -k.derivative_count)})
    return sp.expand(e.subs({f: SYM[f] for f in (af, wf, qf)}))


def coeffs(e):
    e = tojet(e)
    out = {str(s_): e.coeff(s_) for s_ in SYM.values() if e.coeff(s_) != 0}
    rest = sp.expand(e - sum(e.coeff(s_) * s_ for s_ in SYM.values()))
    if rest != 0:
        out['1'] = rest
    return out


PTS = [dict(r=Fr(7, 3), th=Fr(2, 5), v=Fr(5, 7), mu=Fr(13, 10), mp=Fr(3, 11), mpp=Fr(-2, 9), A=Fr(3, 2)),
       dict(r=Fr(13, 4), th=Fr(1, 3), v=Fr(-4, 9), mu=Fr(9, 5), mp=Fr(1, 7), mpp=Fr(5, 3), A=Fr(2, 3)),
       dict(r=Fr(1, 2), th=Fr(6, 5), v=Fr(1, 9), mu=Fr(2, 3), mp=Fr(4, 5), mpp=Fr(1, 4), A=Fr(5, 4))]


def numzero(e, tol=1e-25):
    """zero at 40 digits at three rational points (E, H and their derivatives replaced by rationals)"""
    for pt in PTS:
        x = e.subs({sp.Derivative(Ef, (v, 2)): Fr(1, 3), sp.Derivative(Ef, v): Fr(-2, 7),
                    sp.Derivative(Hf, (th, 2)): Fr(3, 5), sp.Derivative(Hf, th): Fr(1, 6)})
        x = x.subs({Ef: Fr(9, 8), Hf: Fr(11, 10)}).subs({mp: pt['mp'], mpp: pt['mpp']}).subs(mu, pt['mu'])
        x = x.subs({r: pt['r'], th: pt['th'], v: pt['v'], A: pt['A']})
        if abs(sp.N(x, 40)) > tol:
            return False
    return True


def harm_sub(Fl):
    """gh_2's first harmonic from D2: G2_tth = F_th,n/(2 i n), G2_rth = -G2_tth"""
    return {'tth': TS({(2, n): Fl[2].get((1, n), 0) / (2 * I * n) for n in (1, -1)}),
            'rth': TS({(2, n): -Fl[2].get((1, n), 0) / (2 * I * n) for n in (1, -1)})}


def order1_mean(**kw):
    gam, gi, G, K, Km1 = slice_data(**kw)
    Jr, Jt, rho_ = constraints(gi, G, K)
    return {'Jr': Jr, 'Jt': Jt, 'rho': rho_}, Km1


# ------------------------------------------------------------------------------------------------------------------
# finite-lam jets (D6, D8): an independent evaluation of the constraint map
class J:
    """second-order jet in (r, th) over numpy arrays; o = the order still valid"""
    __slots__ = ('v', 'd', 'h', 'o')

    def __init__(self, v_, d=None, h=None, o=2):
        z_ = np.zeros_like(v_)
        self.v, self.o = v_, o
        self.d = d if d is not None else [z_, z_]
        self.h = h if h is not None else [[z_, z_], [z_, z_]]

    def __add__(self, b):
        if not isinstance(b, J):
            return J(self.v + b, self.d, self.h, self.o)
        return J(self.v + b.v, [self.d[i] + b.d[i] for i in range(2)],
                 [[self.h[i][j] + b.h[i][j] for j in range(2)] for i in range(2)], min(self.o, b.o))

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, [-x for x in self.d], [[-x for x in row] for row in self.h], self.o)

    def __sub__(self, b):
        return self + (-b)

    def __mul__(self, b):
        if not isinstance(b, J):
            return J(self.v * b, [x * b for x in self.d], [[x * b for x in row] for row in self.h], self.o)
        return J(self.v * b.v, [self.d[i] * b.v + self.v * b.d[i] for i in range(2)],
                 [[self.h[i][j] * b.v + self.d[i] * b.d[j] + self.d[j] * b.d[i] + self.v * b.h[i][j]
                   for j in range(2)] for i in range(2)], min(self.o, b.o))

    __rmul__ = __mul__

    def fn(self, f0, f1, f2):
        return J(f0, [f1 * x for x in self.d], [[f2 * self.d[i] * self.d[j] + f1 * self.h[i][j] for j in range(2)]
                                                 for i in range(2)], self.o)

    def inv(self):
        return self.fn(1 / self.v, -1 / self.v ** 2, 2 / self.v ** 3)

    def __truediv__(self, b):
        return self * (b.inv() if isinstance(b, J) else 1.0 / b)

    def sqrt(self):
        s_ = np.sqrt(self.v)
        return self.fn(s_, 0.5 / s_, -0.25 / (s_ * self.v))

    def D(self, i):
        return J(self.d[i], [self.h[i][0], self.h[i][1]], None, self.o - 1)


def constraint_map(cp):
    """(J_r, J_th, rho) of gamma (components g_rr, g_rt, g_tt, g_11, g_22), K = (k - L_beta gamma)/(2N), N^2 = -g00 +
    gamma^ij beta_i beta_j, k = d_tau gamma (components k_..), beta = (b_r, b_t); fields of (r, th)"""
    Z = J(np.zeros_like(cp['g_rr'].v), o=9)
    g = [[Z] * 4 for _ in range(4)]
    g[0][0], g[0][1], g[1][0], g[1][1], g[2][2], g[3][3] = (cp['g_rr'], cp['g_rt'], cp['g_rt'], cp['g_tt'],
                                                            cp['g_11'], cp['g_22'])
    idet = (g[0][0] * g[1][1] - g[0][1] * g[0][1]).inv()
    gi = [[Z] * 4 for _ in range(4)]
    gi[0][0], gi[1][1], gi[2][2], gi[3][3] = g[1][1] * idet, g[0][0] * idet, g[2][2].inv(), g[3][3].inv()
    gi[0][1] = gi[1][0] = -g[0][1] * idet

    def dd(x, c):
        return x.D(c) if c < 2 else Z
    dg = [[[dd(g[i][j], c) for j in range(4)] for i in range(4)] for c in range(4)]
    G = [[[sum((gi[a_][d_] * (dg[b_][d_][c_] + dg[c_][d_][b_] - dg[d_][b_][c_]) * 0.5 for d_ in range(4)), Z)
           for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]
    R = Z
    for b_ in range(4):
        for c_ in range(4):
            e = Z
            for a_ in range(4):
                e = e + dd(G[a_][b_][c_], a_) - dd(G[a_][b_][a_], c_)
                for d_ in range(4):
                    e = e + G[a_][a_][d_] * G[d_][b_][c_] - G[a_][c_][d_] * G[d_][b_][a_]
            R = R + gi[b_][c_] * e
    beta = [cp['b_r'], cp['b_t'], Z, Z]
    N2 = -cp['g00']
    for i in range(4):
        for j in range(4):
            N2 = N2 + gi[i][j] * beta[i] * beta[j]
    N = N2.sqrt()
    kd = [[Z] * 4 for _ in range(4)]
    kd[0][0], kd[0][1], kd[1][0], kd[1][1], kd[2][2], kd[3][3] = (cp['k_rr'], cp['k_rt'], cp['k_rt'], cp['k_tt'],
                                                                  cp['k_11'], cp['k_22'])
    K = [[(kd[i][j] - dd(beta[j], i) - dd(beta[i], j) + sum((G[k][i][j] * beta[k] * 2.0 for k in range(4)), Z))
          / (N * 2.0) for j in range(4)] for i in range(4)]
    trK = sum((gi[i][j] * K[i][j] for i in range(4) for j in range(4)), Z)
    Ku = [[sum((gi[i][k] * K[k][j] for k in range(4)), Z) for j in range(4)] for i in range(4)]
    rho_ = R - sum((Ku[i][j] * Ku[j][i] for i in range(4) for j in range(4)), Z) + trK * trK
    Jc = []
    for i in range(2):
        div = Z
        for j in range(4):
            for k in range(4):
                cov = dd(K[i][j], k)
                for l_ in range(4):
                    cov = cov - G[l_][k][i] * K[l_][j] - G[l_][k][j] * K[i][l_]
                div = div + gi[j][k] * cov
        Jc.append(((-div) + dd(trK, i)) * 2.0)
    return Jc[0].v, Jc[1].v, rho_.v


RS, TS_, SS = sp.symbols('R T S_', real=True)
TAU0 = -2


def jets_of(exprs, rr, tt):
    """second-order jets (numpy) of sympy expressions in (R, T)"""
    out = {}
    for k_, e in exprs.items():
        d = [sp.diff(e, RS), sp.diff(e, TS_)]
        h = [[sp.diff(d[0], RS), sp.diff(d[0], TS_)], [sp.diff(d[1], RS), sp.diff(d[1], TS_)]]
        f = sp.lambdify((RS, TS_), [e, d, h], 'numpy')
        val, dv_, hv = f(rr, tt)
        bc = lambda x: np.broadcast_to(np.asarray(x, dtype=float), rr.shape).copy()     # noqa: E731
        out[k_] = J(bc(val), [bc(dv_[0]), bc(dv_[1])], [[bc(hv[0][0]), bc(hv[0][1])], [bc(hv[1][0]),
                                                                                       bc(hv[1][1])]], 2)
    return out


class Model:
    """explicit E(v), mu(v) = mu0 + (2/9) int E^2 (the energy condition), the record's H, A = 1"""

    def __init__(self, Eexp, mu0=1):
        vv = sp.Symbol('vv')
        self.E = Eexp
        self.mu = lambda x: mu0 + sp.Rational(2, 9) * sp.integrate(Eexp(vv) ** 2, (vv, 0, x))
        self.H = lambda x: sp.sqrt(2 / (1 + sp.cos(2 * x) ** 2))
        self.vv = vv

    def ex(self, e, tf=None):
        """our symbols -> explicit (R, T); tf maps a, w, q to explicit expressions (or None)"""
        vv, vexp = self.vv, TAU0 + RS
        e = e.subs({mpp: sp.diff(self.mu(vv), vv, 2).subs(vv, vexp), mp: sp.diff(self.mu(vv), vv).subs(vv, vexp)})
        e = e.subs(sp.Derivative(Ef, v), sp.diff(self.E(vv), vv).subs(vv, vexp))
        e = e.subs(sp.Derivative(Hf, th), sp.diff(self.H(TS_), TS_))
        e = e.subs({Ef: self.E(vexp), Hf: self.H(TS_), mu: self.mu(vexp), A: 1})
        if tf:
            for f in (af, wf, qf):
                e = e.subs(sp.Derivative(f, r, th), sp.diff(tf[f], RS, TS_))
                e = e.subs(sp.Derivative(f, (r, 2)), sp.diff(tf[f], RS, 2)).subs(sp.Derivative(f, (th, 2)),
                                                                                  sp.diff(tf[f], TS_, 2))
                e = e.subs(sp.Derivative(f, r), sp.diff(tf[f], RS)).subs(sp.Derivative(f, th), sp.diff(tf[f], TS_))
            e = e.subs({af: tf[af], wf: tf[wf], qf: tf[qf]})
        return e.subs({r: RS, th: TS_, v: vexp})


def explicit_parts(M, lam, G2c, M1c):
    """the (R, T) expressions the slice data are built from at lam: W, d_v W, d_s W at s = (tau0 + R)/lam, gh_2, the
    background, and the coefficients of K's order-1 mean in a (M1c)"""
    vexp = TAU0 + RS
    sv = vexp / lam
    K_ = M.E(vexp) * M.H(TS_) * RS ** sp.Rational(-3, 2)
    vv = M.vv
    Kd = sp.diff(M.E(vv), vv).subs(vv, vexp) * M.H(TS_) * RS ** sp.Rational(-3, 2)
    Cc, Ss_ = sp.cos(TS_), sp.sin(TS_)

    def wav(Kx, sder=0):
        a1 = Kx * (2 * Cc ** 2 * sp.cos(SS) - Ss_ ** 2 * sp.sin(SS)) / 3
        a2 = Kx * (2 * Ss_ ** 2 * sp.sin(SS) - Cc ** 2 * sp.cos(SS)) / 3
        comps = [-2 * RS ** 2 * (a1 + a2), 2 * RS ** 2 * Cc ** 2 * a1, 2 * RS ** 2 * Ss_ ** 2 * a2]
        return [sp.diff(x, SS, sder).subs(SS, sv) for x in comps]
    ex = {}
    for nm, x in zip(('W_tt', 'W_11', 'W_22'), wav(K_)):
        ex[nm] = x
    for nm, x in zip(('V_tt', 'V_11', 'V_22'), wav(Kd)):
        ex[nm] = x
    for nm, x in zip(('Ws_tt', 'Ws_11', 'Ws_22'), wav(K_, 1)):
        ex[nm] = x
    s = sp.Symbol('s', real=True)
    g2 = M.ex(sum(c * k for k, c in G2c.items()).subs(s, SS))
    ex['G2'] = g2.subs(SS, sv)
    ex['G2s'] = sp.diff(g2, SS).subs(SS, sv)
    m = M.mu(vexp) / RS ** 2
    ex['one_m'] = 1 + m
    ex['m'] = m
    ex['mdot'] = sp.diff(M.mu(vv), vv).subs(vv, vexp) / RS ** 2
    ex['N0'] = (1 + m) ** sp.Rational(-1, 2)
    ex['gtt0'], ex['g110'], ex['g220'] = RS ** 2, RS ** 2 * Cc ** 2, RS ** 2 * Ss_ ** 2
    for k_, e in M1c.items():
        ex['M1_' + k_] = M.ex(e)
    return ex


def slice_jets(X, lam, Ja, Jw, Jq, phase=True, g2=True):
    """the jets of the slice components at lam from explicit parts X (jets) and the unknowns' jets"""
    lam = float(lam)
    Jar, Jat = Ja.D(0), Ja.D(1)
    two_N0 = X['N0'] * 2.0
    M1 = {'rr': X['M1_rr_a'] * Ja + X['M1_rr_ar'] * Jar, 'rth': X['M1_rth_at'] * Jat,
          'thth': X['M1_thth_a'] * Ja, 'p1p1': X['M1_p1p1_a'] * Ja, 'p2p2': X['M1_p2p2_a'] * Ja}
    Hd = {'rr': -(two_N0 * M1['rr']), 'rth': two_N0 * (Jq - M1['rth']),
          'thth': two_N0 * (Jw * X['gtt0'] - M1['thth']), 'p1p1': two_N0 * (Jw * X['g110'] - M1['p1p1']),
          'p2p2': two_N0 * (Jw * X['g220'] - M1['p2p2'])}
    G2 = X['G2'] if g2 else X['G2'] * 0.0
    G2s = X['G2s'] if g2 else X['G2s'] * 0.0
    ph = Ja * (-0.5) if phase else Ja * 0.0
    cp = {'g_rr': X['one_m'] + Ja * lam, 'g_rt': G2 * (-lam ** 2), 'g_tt': X['gtt0'] + X['W_tt'] * lam,
          'g_11': X['g110'] + X['W_11'] * lam, 'g_22': X['g220'] + X['W_22'] * lam, 'b_r': X['m'],
          'b_t': G2 * lam ** 2, 'g00': X['m'] - 1.0, 'k_rr': X['mdot'] + Hd['rr'] * lam,
          'k_rt': G2s * (-lam) + Hd['rth'] * lam}
    for c_, h_ in (('tt', 'thth'), ('11', 'p1p1'), ('22', 'p2p2')):
        cp['k_' + c_] = (X['V_' + c_] * lam + X['Ws_' + c_] + ph * X['Ws_' + c_] * lam + Hd[h_] * lam)
    return cp


def gauss(rc, sig, L=8.0, n=2400):
    x, wq = np.polynomial.legendre.leggauss(n)
    rr = rc + L * sig * x
    return rr, wq * L * sig * np.exp(-(rr - rc) ** 2 / (2 * sig ** 2))


# ------------------------------------------------------------------------------------------------------------------
def legendre_jets(k, tt, odd_der=False):
    """P_k(cos 2th) and its th-derivatives to order 2 (odd_der: of d_th P_k, to order 2)"""
    x = sp.Symbol('x_')
    f = sp.legendre(k, sp.cos(2 * x))
    if odd_der:
        f = sp.diff(f, x)
    fs = [sp.lambdify(x, sp.diff(f, x, j), 'numpy') for j in range(3)]
    return [np.broadcast_to(np.asarray(g(tt), dtype=float), tt.shape) for g in fs]


def mode_odes(Mc):
    """the right sides (a', w', q') of the mode ODEs, with E, mu, k, sigma as symbols"""
    E_, mu_, k_, sg_ = sp.symbols('E_ mu_ k_ sg_')
    a_, w_, q_ = sp.symbols('a_ w_ q_')
    c = {key: sp.simplify(val.subs({Ef: E_, mu: mu_, A: 1})) for key, val in Mc.items()}
    L_ = r ** 2 + mu_
    cs = sp.simplify(c[('Jt', '1')] * (sp.cos(th) ** 4 + sp.sin(th) ** 4) / sp.sin(2 * th))
    ra = -((4 * k_ * (k_ + 1) / L_ + c[('rho', 'a')]) * a_ + c[('rho', 'w')] * w_) / c[('rho', 'a_r')]
    rw = -(c[('Jr', 'w')] * w_ + 8 * k_ * (k_ + 1) / r ** 2 * q_ + c[('Jr', 'a')] * a_) / c[('Jr', 'w_r')]
    rq = -(c[('Jt', 'q')] * q_ + 4 * w_ + c[('Jt', 'a_t')] * a_ + cs * sg_) / c[('Jt', 'q_r')]
    rhs = [sp.simplify(e) for e in (ra, rw, rq)]
    return rhs, sp.lambdify((r, E_, mu_, k_, a_, w_, q_, sg_), rhs, 'numpy'), cs


def sigma_k(k):
    x = sp.Symbol('x')
    return sp.nsimplify(sp.simplify(-sp.Rational(2 * k + 1, 2) * sp.integrate(sp.atan(x) * sp.legendre(k, x),
                                                                                (x, -1, 1))))


def solve_modes(fode, Efun, r0, r1, mu0, ks, rtol=1e-11, mu_in_state=True, mufun=None):
    sols = {}
    for k in ks:
        sk = float(sigma_k(k))

        def F(rr, y, k=k, sk=sk):
            vv = TAU0 + rr
            E = Efun(vv)
            mu_v = y[3] if mu_in_state else mufun(vv)
            da, dw, dq = fode(rr, E, mu_v, k, y[0], y[1], y[2], sk)
            return [da, dw, dq, 2.0 / 9.0 * E ** 2]
        sols[k] = solve_ivp(F, (r0, r1), [0, 0, 0, mu0], method='Radau', rtol=rtol, atol=1e-15, dense_output=True)
    return sols


# ------------------------------------------------------------------------------------------------------------------
def check_d1_d2():
    g0, gi0 = background5()
    gen = {nm: TS({(2, n): sp.Symbol('P%d_%s' % (n + 2, nm)) for n in (1, -1, 2, -2)}) for nm in NM}
    Fl, _, _ = gauge(g2=gen, chi=True)
    low_zero = all(sp.simplify(sp.expand(c)) == 0 for b in range(5) for (k, n), c in Fl[b].items() if k <= 0)
    ok_pol = True
    for n in (1, -1, 2, -2):
        Y = sp.zeros(5)
        for (i, j), nm in zip(CL, NM):
            Y[i, j] = Y[j, i] = sp.Symbol('P%d_%s' % (n + 2, nm)) * I * n
        pv = pol(Y, g0, gi0)
        syms = [sp.Symbol('P%d_%s' % (n + 2, nm)) for nm in NM]
        for b in range(5):
            c = sp.expand(Fl[b].get((1, n), 0))
            ok_pol &= sp.simplify(sum(c.coeff(x) * x for x in syms) - pv[b]) == 0
    OK['D1'] = low_zero and ok_pol
    print('  D1 (exact): on Sigma D^(0) = 0 (every component, every harmonic): %s; with a generic gh_2 (eight class '
          'components, harmonics 1, 2) the gh_2-part of D^(1) is Pol(d_s gh_2), lowered by g0: %s %s'
          % (low_zero, ok_pol, el()))
    F0, _, _ = gauge(g2=None)
    first = {b: {n: sp.expand(F0[b].get((1, n), 0)) for n in (1, -1)} for b in range(5)}
    only_th = all(first[b][n] == 0 for b in (0, 1, 3, 4) for n in (1, -1))
    a_free = not any(first[2][n].has(af) for n in (1, -1))
    pp = polplus([0, 0, sp.Symbol('c')], g0, gi0)
    pp_ok = (sp.simplify(pp['tth'] + sp.Symbol('c') / 2) == 0 and sp.simplify(pp['rth'] - sp.Symbol('c') / 2) == 0
             and all(pp[nm] == 0 for nm in NM if nm not in ('tth', 'rth')))
    s = sp.Symbol('s', real=True)
    G2 = sp.expand(sum(first[2][n] / (2 * I * n) * (sp.cos(s) + I * n * sp.sin(s)) for n in (1, -1)))
    Hp = sp.Derivative(Hf, th)
    claim = A * Ef / (6 * r ** sp.Rational(3, 2)) * ((5 * Hf * sp.sin(2 * th) + 2 * S ** 2 * Hp) * sp.cos(s)
                                                      + (5 * Hf * sp.sin(2 * th) - 2 * C ** 2 * Hp) * sp.sin(s))
    g2_ok = sp.simplify(sp.expand_trig(G2 - claim)) == 0
    # second harmonic: chi's d_tau and the W^2 terms
    Fc, _, _ = gauge(g2=None, chi=True)
    sec = {}
    for n in (2, -2):
        cvec = [sp.expand(Fc[b].get((1, n), 0)) for b in range(3)]
        sol = polplus([-x for x in cvec], g0, gi0)
        sec[n] = {nm: sp.simplify(val / (I * n)) for nm, val in sol.items()}
    sec_real = {}
    for nm in NM:
        e = sp.expand(sum(sec[n][nm] * (sp.cos(2 * s) + I * sp.sign(n) * sp.sin(2 * s)) for n in (2, -2)))
        sec_real[nm] = sp.factor(sp.simplify(e)) if e != 0 else 0
    # step (ii): the mean of D^(1) with d_tau m_1 (T on tau components, H on spatial ones)
    nmd = {(0, 0): 'T_tt', (0, 1): 'T_tr', (0, 2): 'T_tth', (1, 1): 'H_rr', (1, 2): 'H_rth', (2, 2): 'H_thth',
           (3, 3): 'H_p1', (4, 4): 'H_p2'}
    md = sp.zeros(5)
    for (i, j), nm in nmd.items():
        md[i, j] = md[j, i] = sp.Function(nm)(r, th)
    Dm = [sum(gi0[a_, b_] * gi0[rh, sg] * ((md[sg, b_] if a_ == 0 else 0) + (md[sg, a_] if b_ == 0 else 0)
                                             - (md[a_, b_] if sg == 0 else 0)) / 2
              for a_ in range(5) for b_ in range(5) for sg in range(5)) for rh in range(5)]
    mean = [sp.simplify(sp.expand_trig(sum(g0[b, q_] * Dm[q_] for q_ in range(5)) + sp.expand(F0[b].get((1, 0), 0))))
            for b in range(3)]
    OK['D2'] = only_th and a_free and pp_ok and g2_ok
    print('  D2 (exact): the first harmonic of D^(1) at gh_2 = 0 lies in the th component only: %s, independent of a '
          '(Lambda_1 = 0 in the class): %s; Pol^+ of (0, 0, c) is c (dr dth - dtau dth)/2 symmetrised (tth -c/2, rth '
          'c/2, others 0): %s; so gh_2 on Sigma, first harmonic: G2_(tau th) = -G2_(r th) = (A E/(6 r^(3/2))) [(5 H sin '
          '2th + 2 S^2 H\') cos s + (5 H sin 2th - 2 C^2 H\') sin s]: %s %s' % (only_th, a_free, pp_ok, g2_ok, el()))
    print('      gh_2 on Sigma, second harmonic (computed, exact; chi\'s d_tau READ from stage0bd5.py):')
    for nm in NM:
        if sec_real[nm] != 0:
            print('        G2_(%s) = %s' % (nm, sec_real[nm]))
    print('      step (ii), the mean of D^(1) on Sigma (= 0 fixes d_tau (m_1)_(tau .), the coefficient -(1 + mu/r^2) of '
          'T_tr, T_tth being invertible):')
    for b, e in zip(('tau', 'r', 'th'), mean):
        print('        D^(1)_%s mean = %s' % (b, sp.collect(sp.expand(e), list(md.atoms(sp.Function)))))
    return F0, first


DOC = """  DOC (deduced) Why the truncation at k = 1 gives the complete order-1 mean: a coefficient of lam^2 or higher reaches
  order 1 only through one fast derivative lam^-1 d_s (gamma's lam^2 terms in Gamma; K's lam^2 terms in div K and d
  tr K), and is then multiplied by an order-0 factor; the order-0 parts of gamma^-1 are g0's (not oscillating), so
  these terms are d_s of something times a non-oscillating factor, of mean zero. gamma^-1 is kept to lam^2 since it
  meets the lam^-1 of d_s^2 (lam W). The order-1 oscillating parts are incomplete and are not used."""


def check_d3_d4(F0):
    g2 = harm_sub(F0)
    out, Km1 = order1_mean(g2=g2)
    low = all(sp.simplify(sp.expand(c)) == 0 for X in out.values() for (k, n), c in X.items() if k < 0)
    en = sp.Rational(2, 9) * A ** 2 * Ef ** 2 * Hf ** 2 * (C ** 4 + S ** 4)
    m0 = {}
    for nm, X in out.items():
        c0 = sp.expand(X.mean(0)).subs(sp.Derivative(mu, v), mp)
        m0[nm] = sp.simplify(c0.subs(mp, en)) == 0 and (c0 == 0 or sp.simplify(sp.diff(c0, mp)) != 0)
    OK['D3'] = low and all(m0.values())
    print('  D3 (exact): no lam^-1 term in (J_r, J_th, rho): %s; the order-0 mean vanishes exactly at mu\' = (2/9) A^2 '
          'E^2 H^2 (C^4 + S^4), stage 0\'s energy condition: %s %s' % (low, m0, el()))
    print(DOC)
    CO = {nm: {k: sp.factor(sp.simplify(c)) for k, c in coeffs(X.mean(1)).items()} for nm, X in out.items()}
    # P against data5.py's lin_0
    lin0, _ = D5.perturbed(False)
    ok_p = True
    for nm, X in zip(('Jr', 'Jt', 'rho'), lin0):
        c5 = D5.coeff(X, 0).subs({D5.r: r, D5.th: th, D5.v: v}).subs({D5.af: af, D5.wf: wf, D5.qf: qf}).subs(D5.mu, mu)
        c5 = coeffs(c5)
        mine = {k: c.subs(A, 0) for k, c in CO[nm].items()}
        ok_p &= all(numzero(c5.get(k, 0) - mine.get(k, 0)) for k in set(c5) | set(mine))
    L_ = r ** 2 + mu
    h4 = A ** 2 * Ef ** 2 * Hf ** 2 * (C ** 4 + S ** 4)
    B = {'Jr': -h4 / (3 * L_ ** sp.Rational(3, 2)), 'Jt': sp.Integer(0), 'rho': sp.Rational(2, 3) * r * h4 / L_ ** 2}
    B_FORM.update(B)
    Sv = {'Jr': 0, 'Jt': -A ** 2 * Ef ** 2 * Hf ** 2 * sp.sin(2 * th) / (3 * r ** 2 * sp.sqrt(L_)), 'rho': 0}
    ok_b = all(numzero(CO[nm].get('a', 0) - CO[nm].get('a', 0).subs(A, 0) - B[nm]) for nm in CO)
    ok_s = all(numzero(CO[nm].get('1', 0) + Sv[nm]) for nm in CO)
    alg = all(numzero(CO[nm].get(k, 0) - CO[nm].get(k, 0).subs(A, 0)) for nm in CO for k in CO[nm] if k not in
              ('a', '1'))
    # what each piece contributes: the phase, gh_2 (with a generic second harmonic too), chi's d_tau
    gen2 = {'rth': TS({(2, n): sp.Symbol('X%d_rth' % (n + 2)) for n in (2, -2)}),
            'thth': TS({(2, n): sp.Symbol('X%d_thth' % (n + 2)) for n in (2, -2)}),
            'tth': TS({(2, n): sp.Symbol('X%d_tth' % (n + 2)) for n in (2, -2)}),
            'tr': TS({(2, n): sp.Symbol('X%d_tr' % (n + 2)) for n in (2, -2)})}
    variants = {'no phase': dict(g2=g2, phase=False), 'no gh_2': dict(g2=None),
                'gh_2 + generic second harmonic': dict(g2={k: g2.get(k, TS()) + gen2.get(k, TS()) for k in
                                                           set(g2) | set(gen2)}),
                'chi\'s d_tau on': dict(g2=g2, chidot=True)}
    changes = {}
    for lab, kw in variants.items():
        o2, _ = order1_mean(**kw)
        ch = {}
        for nm, X in o2.items():
            cf = coeffs(X.mean(1))
            dk = {k: sp.factor(sp.simplify(cf.get(k, 0) - CO[nm].get(k, 0))) for k in set(cf) | set(CO[nm])
                  if not numzero(cf.get(k, 0) - CO[nm].get(k, 0))}
            if dk:
                ch[nm] = dk
        changes[lab] = ch
        print('      %s: change of <Phi^(1)>: %s %s' % (lab, ch if ch else 'none', el()))
    ph = changes['no phase']
    ph_ok = (set(ph) == {'Jr', 'rho'} and numzero(ph['Jr'].get('a', 0) - h4 * sp.sqrt(L_) / (3 * r ** 4))
             and numzero(ph['rho'].get('a', 0) + h4 / (3 * r ** 3)))
    none_else = all(not changes[k] for k in variants if k != 'no phase')
    OK['D4'] = ok_p and ok_b and ok_s and alg and ph_ok and none_else
    print('  D4 (exact): <Phi^(1)> = P(h_1, Q_1) + B_1 a - S_1 with P = data5.py\'s lin_0 coefficient by coefficient '
          '(40 digits, three points): %s; B_1 = H^2 (C^4 + S^4) A^2 E^2 a (-(1/3) Lambda^(-3/2), 0, (2/3) r '
          'Lambda^-2): %s; S_1 = (0, -A^2 E^2 H^2 sin 2th/(3 r^2 Lambda^(1/2)), 0): %s; no other coefficient carries A '
          '(B_1 algebraic in a): %s; the phase carries (-(1/3) r^-4 Lambda^(1/2), 0, (1/3) r^-3) A^2 E^2 H^2 (C^4 + '
          'S^4) a of B_1: %s; gh_2 (both harmonics) and chi\'s d_tau change nothing: %s %s'
          % (ok_p, ok_b, ok_s, alg, ph_ok, none_else, el()))
    print('      the coefficients of <Phi^(1)> (key: the jet multiplied; \'1\' the term free of a, w, q; mp = mu\'):')
    for nm in ('Jr', 'Jt', 'rho'):
        for k, c in sorted(CO[nm].items()):
            if not numzero(c):
                print('        %s[%s] = %s' % (nm, k, c))
    M1 = {}
    for (i, j), nm in (((0, 0), 'rr'), ((0, 1), 'rth'), ((1, 1), 'thth'), ((2, 2), 'p1p1'), ((3, 3), 'p2p2')):
        M1[nm] = sp.factor(sp.simplify(sp.expand(Km1[i][j]).subs(sp.Derivative(mu, v), mp)))
    print('      K\'s order-1 mean from the metric with d_tau h_1 = 0 (so Q_1 = M1 + d_tau h_1/(2 N0), N0 = (1 + '
          'mu/r^2)^(-1/2)); no W^2 term:')
    for nm, e in M1.items():
        print('        M1_%s = %s' % (nm, e))
    return CO, M1, g2


def check_d5(CO):
    Hrec = (C ** 4 + S ** 4) ** sp.Rational(-1, 2)
    hr = sp.simplify(sp.expand_trig(Hrec ** 2 - 2 / (1 + sp.cos(2 * th) ** 2))) == 0
    Mc = {}
    free = True
    for nm in ('Jr', 'Jt', 'rho'):
        for key, c in CO[nm].items():
            e = sp.factor(sp.simplify(c.subs(Hf, Hrec).subs(mp, sp.Rational(2, 9) * A ** 2 * Ef ** 2)))
            Mc[(nm, key)] = e
            if (nm, key) not in (('rho', 'a_t'), ('Jr', 'q'), ('Jt', '1')):
                free &= sp.simplify(sp.diff(e, th)) == 0
    cot = sp.cos(2 * th) / sp.sin(2 * th)
    lap = sp.simplify(Mc[('rho', 'a_t')] - 2 * cot * Mc[('rho', 'a_tt')]) == 0
    div = sp.simplify(Mc[('Jr', 'q')] - 2 * cot * Mc[('Jr', 'q_t')]) == 0
    eig = all(sp.simplify(sp.expand_trig(sp.diff(sp.legendre(k, sp.cos(2 * th)), th, 2) + 2 * cot * sp.diff(
        sp.legendre(k, sp.cos(2 * th)), th) + 4 * k * (k + 1) * sp.legendre(k, sp.cos(2 * th)))) == 0
        for k in range(1, 5))
    src = sp.simplify(Mc[('Jt', '1')] * (C ** 4 + S ** 4) / sp.sin(2 * th))
    src_ok = sp.simplify(sp.diff(src, th)) == 0
    sig = {k: sigma_k(k) for k in range(1, 12)}
    x = sp.Symbol('x')
    part = sum(sig[k] * sp.legendre(k, x) for k in range(1, 12))
    tail = max(abs(float(part.subs(x, xx)) + math.atan(xx)) for xx in np.linspace(-1, 1, 41))
    even0 = all(sig[k] == 0 for k in range(2, 12, 2))
    rhs, fode, cs = mode_odes(Mc)
    OK['D5'] = hr and free and lap and div and eig and src_ok and even0 and tail < 1e-4
    print('  D5 (exact): H_rec = (C^4 + S^4)^(-1/2): %s; with it every coefficient of P + B_1 is free of th except '
          'the angular operators: %s; these are -(1/Lambda) Lap a (rho): %s and -(2/r^2) div (q dth) (J_r): %s; Lap '
          'P_k(cos 2th) = -4 k (k + 1) P_k, k <= 4: %s; the source is (A^2 E^2/(3 r^2 Lambda^(1/2))) H^2 sin 2th, '
          'H^2 sin 2th = sum sigma_k d_th P_k: %s; sigma_k = 0 for even k: %s; |sum_(k<=11) sigma_k P_k + atan| <= %.1e '
          'on [-1, 1] %s' % (hr, free, lap, div, eig, src_ok, even0, tail, el()))
    print('      sigma_k (exact): ' + '; '.join('%d: %s = %.6g' % (k, sig[k], float(sig[k])) for k in range(1, 12, 2)))
    print('      the mode ODEs (E_, mu_ for E(v), mu(v) at v = tau0 + r; k the mode; sg_ = sigma_k):')
    for nm, e in zip(('a_k\'', 'w_k\'', 'q_k\''), rhs):
        print('        %s = %s' % (nm, e))
    return fode, Mc


def check_d6(CO, M1, F0):
    M = Model(lambda x: 1 + x / 4)
    aT = (sp.Rational(1, 7) + sp.cos(2 * TS_) / 5) * (1 + RS / 10)
    wT = RS * sp.cos(2 * TS_) / 9 + sp.Rational(1, 11)
    qT = sp.sin(2 * TS_) * RS / 13
    rr, wq = gauss(3.5, 0.3)
    G2c = harm_closed(F0)
    M1c = m1_coeffs(M1)
    ths = (0.35, 0.8, 1.2)
    res = {}
    for t_ in ths:
        tt = np.full_like(rr, t_)
        U = jets_of({'a': aT, 'w': wT, 'q': qT}, rr, tt)
        jv = jet_values(U)
        pr = {}
        for nm in ('Jr', 'Jt', 'rho'):
            cf = {k: sp.lambdify((RS, TS_), M.ex(c), 'numpy') for k, c in CO[nm].items()}
            vals = {k: np.broadcast_to(np.asarray(f(rr, tt), dtype=float), rr.shape) for k, f in cf.items()}
            pr[nm] = {k: float(np.sum(wq * vals[k] * jv[k])) for k in vals}
        Bf = {nm: sp.lambdify((RS, TS_), M.ex(e), 'numpy') for nm, e in B_FORM.items()}
        pB = {nm: float(np.sum(wq * np.broadcast_to(np.asarray(Bf[nm](rr, tt), dtype=float), rr.shape) * jv['a']))
              for nm in Bf}
        res[t_] = {'pred': pr, 'pred_B': pB}
        for lam in (Fr(1, 32), Fr(1, 64)):
            X = jets_of(explicit_parts(M, sp.Rational(lam.numerator, lam.denominator), G2c, M1c), rr, tt)
            for lab, kw in (('data', {}), ('no phase', dict(phase=False))):
                Jr_, Jt_, rho_ = constraint_map(slice_jets(X, lam, U['a'], U['w'], U['q'], **kw))
                res[t_][(lab, lam)] = {nm: float(np.sum(wq * x_)) for nm, x_ in zip(('Jr', 'Jt', 'rho'),
                                                                                      (Jr_, Jt_, rho_))}
        print('      th = %.2f done %s' % (t_, el()))
    return res


def jet_values(U):
    a, w, q = U['a'], U['w'], U['q']
    one = np.ones_like(a.v)
    jv = {'1': one}
    for nm, X in (('a', a), ('w', w), ('q', q)):
        jv[nm], jv[nm + '_r'], jv[nm + '_t'] = X.v, X.d[0], X.d[1]
        jv[nm + '_rr'], jv[nm + '_rt'], jv[nm + '_tt'] = X.h[0][0], X.h[0][1], X.h[1][1]
    return jv


def harm_closed(F0):
    s = sp.Symbol('s', real=True)
    G2 = sp.expand(sum(sp.expand(F0[2].get((1, n), 0)) / (2 * I * n) * (sp.cos(s) + I * n * sp.sin(s))
                       for n in (1, -1)))
    return sp.collect(G2, [sp.cos(s), sp.sin(s)], evaluate=False)


def m1_coeffs(M1):
    aj = {nm: tojet(e.subs(mp, sp.Derivative(mu, v))) for nm, e in M1.items()}
    sa, sar, sat = sp.Symbol('a'), sp.Symbol('a_r'), sp.Symbol('a_t')
    out = {'rr_a': aj['rr'].coeff(sa), 'rr_ar': aj['rr'].coeff(sar), 'rth_at': aj['rth'].coeff(sat),
           'thth_a': aj['thth'].coeff(sa), 'p1p1_a': aj['p1p1'].coeff(sa), 'p2p2_a': aj['p2p2'].coeff(sa)}
    rest = sum(sp.expand(aj[nm]) for nm in aj) - sum(out[k] * (sar if k.endswith('ar') else (sat if k.endswith(
        'at') else sa)) for k in out)
    assert sp.simplify(sp.expand(rest)) == 0, 'M1 is not of the expected form'
    return {k: c.subs(mp, sp.Derivative(mu, v)) for k, c in out.items()}


def order_p(x1, x2):
    return math.log(abs(x1) / abs(x2), 2) if x2 != 0 and x1 != 0 else float('inf')


def assess_d6(res, flipS=False, dropB=False, lab='data'):
    """the orders p of the remainders W(lam) - lam I1 between lam = 1/32 and 1/64"""
    ps = {}
    for t_, d in res.items():
        for nm in ('Jr', 'Jt', 'rho'):
            pr = dict(d['pred'][nm])
            if flipS and '1' in pr:
                pr['1'] = -pr['1']
            if dropB and 'a' in pr:
                pr['a'] = pr['a'] - d['pred_B'][nm]
            I1 = sum(pr.values())
            rem = [d[(lab, lam)][nm] - float(lam) * I1 for lam in (Fr(1, 32), Fr(1, 64))]
            ps[(t_, nm)] = (order_p(*rem), rem)
    return ps


def env_float():
    """envelope5.py's env, c from int beta^2 by mpmath quadrature (floating point; certified interval READ)"""
    Ib = mpmath.quad(lambda y: (mpmath.cos(mpmath.pi * y / 2) ** 12 * mpmath.exp(-y ** 2 / (1 - y ** 2))) ** 2,
                     [-1, 0, 1])
    c = float(mpmath.sqrt((mpmath.mpf(105) / 128) / (mpmath.mpf(3) / 2 * Ib)))

    def env(vv):
        y = (2 * vv - 4) / 3
        return c * math.cos(math.pi * y / 2) ** 12 * math.exp(-y * y / (1 - y * y)) if abs(y) < 1 else 0.0
    return env, c


def mode_jets(sols, ks, r0, r1, rr, tt, deg=40):
    nodes = np.cos(np.pi * (np.arange(4 * deg) + 0.5) / (4 * deg))
    xs = (r0 + r1) / 2 + (r1 - r0) / 2 * nodes
    xi = (2 * rr - (r0 + r1)) / (r1 - r0)
    sc = 2 / (r1 - r0)
    out = {}
    for nm, i in (('a', 0), ('w', 1), ('q', 2)):
        v_, dr, dt, hrr, hrt, htt = (np.zeros_like(rr) for _ in range(6))
        for k in ks:
            ch = np.polynomial.chebyshev.Chebyshev.fit(nodes, sols[k].sol(xs)[i], deg, domain=[-1, 1])
            f0, f1, f2 = ch(xi), ch.deriv(1)(xi) * sc, ch.deriv(2)(xi) * sc ** 2
            P = legendre_jets(k, tt, odd_der=(nm == 'q'))
            v_, dr, dt = v_ + f0 * P[0], dr + f1 * P[0], dt + f0 * P[1]
            hrr, hrt, htt = hrr + f2 * P[0], hrt + f1 * P[1], htt + f0 * P[2]
        out[nm] = J(v_, [dr, dt], [[hrr, hrt], [hrt, htt]], 2)
    return out


def check_d7(fode):
    env, c = env_float()
    ks = (1, 3, 5, 7, 9, 11)
    s1 = solve_modes(fode, env, 2.5, 5.5, 1.0, ks)
    s2 = solve_modes(fode, env, 2.5, 5.5, 1.0, ks, rtol=1e-9)
    tt = np.linspace(1e-3, np.pi / 2 - 1e-3, 61)
    sizes = {}
    for lab, (lo, hi) in (('past of X* (r <= 4)', (2.5, 4.0)), ('slice (r <= 11/2)', (2.5, 5.5))):
        rr = np.linspace(lo, hi, 301)
        R_, T_ = np.meshgrid(rr, tt, indexing='ij')
        tot = {nm: np.zeros_like(R_) for nm in 'awq'}
        dif = 0.0
        for k in ks:
            y1, y2 = s1[k].sol(rr), s2[k].sol(rr)
            dif = max(dif, float(np.max(np.abs(y1[:3] - y2[:3]))))
            P = legendre_jets(k, T_)
            dP = legendre_jets(k, T_, odd_der=True)
            tot['a'] += y1[0][:, None] * P[0]
            tot['w'] += y1[1][:, None] * P[0]
            tot['q'] += y1[2][:, None] * dP[0]
        sizes[lab] = ({nm: float(np.max(np.abs(x))) for nm, x in tot.items()}, dif)
    mu_end = float(s1[1].sol(5.5)[3])
    OK['D7'] = (abs(mu_end - 227 / 192) < 1e-9 and sizes['slice (r <= 11/2)'][1] < 1e-8
                and sizes['slice (r <= 11/2)'][0]['a'] < 1e-3)
    print('  D7 (computed, floating point): envelope5\'s envelope (c = %.10f by quadrature, inside envelope5\'s certified '
          '[1.32407110621, 1.3241034918]: %s); the mode ODEs k = 1, ..., 11 (odd) from zero data at r = 5/2; mu '
          'integrated beside them reaches %.13f at r = 11/2 (227/192 = %.13f)' % (
              c, float(C_LO.lower()) <= c <= float(C_HI.upper()), mu_end, 227 / 192))
    for lab, (mx, dif) in sizes.items():
        print('      on %s: sup |a| = %.3e, sup |w| = %.3e, sup |q| = %.3e (sup over th on a grid; rtol 1e-11 against '
              '1e-9: %.1e)' % (lab, mx['a'], mx['w'], mx['q'], dif))
    print('      so h_1 = a dr dr is below 1e-3 on the slice, against the |a_1| > 12.37 the data alone would need to move '
          'the operator-norm bound (R8.0 (6), classm5 K3): computed now, not only implausible; sup |a| < 1e-3: %s %s'
          % (OK['D7'], el()))
    return env, c, s1


def check_d8(fode, M1, F0):
    M = Model(lambda x: 1 + x / 4)
    ks = (1, 3, 5, 7, 9, 11)
    r0, r1 = 1.1, 5.9
    mufl = sp.lambdify(M.vv, M.mu(M.vv))
    sols = solve_modes(fode, lambda vv: 1 + vv / 4, r0, r1, float(mufl(TAU0 + r0)), ks)
    rr, wq = gauss(3.5, 0.3)
    G2c, M1c = harm_closed(F0), m1_coeffs(M1)
    out = {}
    for t_ in (0.35, 0.8, 1.2):
        tt = np.full_like(rr, t_)
        U = mode_jets(sols, ks, r0, r1, rr, tt)
        Z = J(np.zeros_like(rr), o=9)
        for lam in (Fr(1, 32), Fr(1, 64)):
            X = jets_of(explicit_parts(M, sp.Rational(lam.numerator, lam.denominator), G2c, M1c), rr, tt)
            for lab, args, kw in (('stage 0', (Z, Z, Z), dict(g2=False)), ('stage 1', (U['a'], U['w'], U['q']), {})):
                Jr_, Jt_, rho_ = constraint_map(slice_jets(X, lam, *args, **kw))
                out[(lab, lam, t_)] = [float(np.sum(wq * x_)) for x_ in (Jr_, Jt_, rho_)]
        print('      th = %.2f done %s' % (t_, el()))
    ok = True
    for t_ in (0.35, 0.8, 1.2):
        line = []
        for lab in ('stage 0', 'stage 1'):
            ps = [order_p(out[(lab, Fr(1, 32), t_)][i], out[(lab, Fr(1, 64), t_)][i]) for i in range(3)]
            if lab == 'stage 0':
                ok &= 0.85 <= ps[1] <= 1.15 and ps[0] >= 1.6 and ps[2] >= 1.6
            else:
                ok &= all(p >= 1.6 for p in ps)
            line.append('%s: W(1/32) = %s, p = %s' % (lab, ['%.3e' % x for x in out[(lab, Fr(1, 32), t_)]],
                                                      ['%.2f' % p for p in ps]))
        print('      th = %.2f  %s' % (t_, '; '.join(line)))
    OK['D8'] = ok
    print('  D8 (computed, floating point): the weak residual (J_r, J_th, rho) of the stage-0 data is of order lam in '
          'J_th (the mean -S_1) and of order lam^2 in J_r, rho; with the stage-1 data of D5 it is of order lam^2 in all '
          'three (p from lam = 1/32 to 1/64): %s %s' % (ok, el()))


def smooth_end(f, x, x0, side, kmax=8, eps=mpmath.mpf('1e-3')):
    """the derivatives of f at x0 + side*eps, k = 1..kmax (mpmath.diff, 60 digits)"""
    with mpmath.workdps(60):
        return [abs(mpmath.diff(lambda t: f(t), x0 + side * eps, k)) for k in range(1, kmax + 1)]


def check_e1():
    t, xx = sp.symbols('t x', positive=True)
    P = sp.Integer(1)
    ok_rec, ok_lim = True, True
    for k in range(1, 9):
        P = sp.expand(xx ** 2 * (P - sp.diff(P, xx)))
        ok_rec &= sp.simplify(sp.diff(sp.exp(-1 / t), t, k) - P.subs(xx, 1 / t) * sp.exp(-1 / t)) == 0
        ok_lim &= sp.limit(P * sp.exp(-xx), xx, sp.oo) == 0
    y = sp.Symbol('y', real=True)
    ok_fac = sp.simplify(sp.exp(-y ** 2 / (1 - y ** 2)) - sp.E * sp.exp(-1 / (1 - y ** 2))) == 0
    beta = lambda q: (mpmath.cos(mpmath.pi * q / 2) ** 12 * mpmath.exp(-q ** 2 / (1 - q ** 2))) if abs(q) < 1 else 0
    d_end = smooth_end(beta, None, mpmath.mpf(1), -1)
    sin4 = lambda vv: mpmath.sin(mpmath.pi * (vv - mpmath.mpf(1) / 2) / 3) ** 4
    d_sin = smooth_end(sin4, None, mpmath.mpf(1) / 2, 1)
    vv = sp.Symbol('vv')
    j4 = sp.diff(sp.sin(sp.pi * (vv - sp.Rational(1, 2)) / 3) ** 4, vv, 4).subs(vv, sp.Rational(1, 2))
    smooth = ok_rec and ok_lim and ok_fac and max(d_end) < 1e-100
    OK['E1'] = smooth
    OK['C4'] = not (max(d_sin) < 1e-100) and j4 != 0
    print('  E1 (proved; computed): phi^(k)(t) = P_k(1/t) e^(-1/t) with P_(k+1)(x) = x^2 (P_k - P_k\'), k <= 8: %s; '
          'P_k(x) e^(-x) -> 0 as x -> oo: %s; exp(-y^2/(1 - y^2)) = e exp(-1/(1 - y^2)): %s; so beta = e cos^12(pi '
          'y/2) phi(1 - y^2) is C^oo with support [-1, 1] and env with support [1/2, 7/2]; the derivatives 1..8 of beta '
          'at y = 1 - 1e-3 are at most %s (60 digits): %s' % (ok_rec, ok_lim, ok_fac, mpmath.nstr(max(d_end), 3),
                                                               smooth))
    print('  C4 (control): the numerics\' sin^4(pi (v - 1/2)/3): its derivatives 1..8 at v = 1/2 + 1e-3 reach %s, and '
          'its fourth derivative at v = 1/2 is %s != 0 (0 from the left): not C^4, E1\'s test fails: %s' % (
              mpmath.nstr(max(d_sin), 4), j4, OK['C4']))


def gron_cells(ncell=600, mcells=8, kcells=4):
    M_, Q_, P_, G_, Ye, mm, kk, R_ = SR.forms()
    A_ = sp.simplify(Q_[0, 0] * Q_[1, 1] - Q_[0, 1] ** 2)
    B_ = sp.simplify(M_[0, 0] * Q_[1, 1] + M_[1, 1] * Q_[0, 0] - 2 * M_[0, 1] * Q_[0, 1])
    C_ = sp.simplify(M_[0, 0] * M_[1, 1] - M_[0, 1] ** 2)
    fA, fB, fC = (SR.to_arb_fn(e, (mm, kk)) for e in (A_, B_, C_))
    fang = SR.to_arb_fn(sp.simplify(M_[2, 2] / Q_[2, 2]), (mm, kk))
    rs = [SR.A_LO + (SR.B_HI - SR.A_LO) * Fr(i, ncell) for i in range(ncell + 1)]
    mup = Fr(2, 9) * SR.C_ENV ** 2
    cells = []
    for i in range(ncell):
        r0, r1 = rs[i], rs[i + 1]
        mlo, mhi, khi = SR.MU0 / r1 ** 2, SR.MU_END / r0 ** 2, mup / r0
        loc = flint.arb(0)
        for jm in range(mcells):
            ml, mh = mlo + (mhi - mlo) * Fr(jm, mcells), mlo + (mhi - mlo) * Fr(jm + 1, mcells)
            mbox = flint.arb((SR.arb_q(ml) + SR.arb_q(mh)) / 2, (SR.arb_q(mh) - SR.arb_q(ml)) / 2)
            for jk in range(kcells):
                kl, kh = khi * Fr(jk, kcells), khi * Fr(jk + 1, kcells)
                kbox = flint.arb((SR.arb_q(kl) + SR.arb_q(kh)) / 2, (SR.arb_q(kh) - SR.arb_q(kl)) / 2)
                Av, Bv, Cv = fA(mbox, kbox), fB(mbox, kbox), fC(mbox, kbox)
                disc = Bv * Bv - 4 * Av * Cv
                sq = disc.sqrt() if disc > 0 else abs(disc).sqrt()
                lamb = (abs(Bv) + sq) / (2 * Av) if Av > 0 else flint.arb('inf')
                lamb = max(lamb, abs(fang(mbox, kbox)), key=lambda z: float(z.upper()))
                if float(lamb.upper()) > float(loc.upper()):
                    loc = lamb
        cells.append((r0, r1, (loc / SR.arb_q(r0)).upper()))
    sm, best = [None] * ncell, flint.arb(0)
    for i in range(ncell - 1, -1, -1):
        if float(cells[i][2].upper()) > float(best.upper()):
            best = cells[i][2]
        sm[i] = best
    return cells, sm


def rate_at(rho_, cells, sm):
    for i, (r0, r1, _) in enumerate(cells):
        if r1 > rho_:
            return sm[i]
    return sm[-1]


def boundary_curve(a_lo, dtau, n=2000, steep=Fr(1)):
    """rho~ backwards from (tau*, a_lo): pieces (dt, rho at the later end, sigma = -slope); sigma rounded down"""
    dt, rho_, out = Fr(dtau) / n, Fr(a_lo), []
    for _ in range(n):
        m_lo = 1 / (rho_ + dt) ** 2
        sig = Fr(int((m_lo - 1) / (m_lo + 1) * 10 ** 9), 10 ** 9) if m_lo > 1 else Fr(0)
        sig = sig * steep
        out.append((dt, rho_, sig))
        rho_ = rho_ + sig * dt
    return out


def slope_ok(pieces):
    """exact: on each piece, every point (rho in [rho_i, rho_i + sigma dt]) has (m - 1)/(m + 1) >= sigma, m >= mu0/rho^2
    with mu0 = 1 the least mu on Omega; sigma <= 1 keeps the piece inside [rho_i, rho_i + dt]"""
    for dt, rho_, sig in pieces:
        if sig > 1:
            return False
        if sig == 0:
            if rho_ > 1:
                return False
            continue
        m_lo = 1 / (rho_ + sig * dt) ** 2
        if not (m_lo > 1 and (m_lo - 1) / (m_lo + 1) >= sig):
            return False
    return True


def check_g():
    flint.ctx.prec = 120
    cells, sm = gron_cells()
    a_lo = SR.A_LO
    dtau = 4 - a_lo
    pieces = boundary_curve(a_lo, dtau)
    ok1 = slope_ok(pieces)
    tot = flint.arb(0)
    for dt, rho_, sig in pieces:
        tot += rate_at(rho_, cells, sm) * SR.arb_q(dt)
    fac = (tot / 2).exp()
    rho_end = pieces[-1][1] + pieces[-1][2] * pieces[-1][0]
    OK['G1'] = ok1 and rho_end < 1
    OK['G2'] = flint.arb('12') < cells[0][2] < flint.arb('13.3')
    OK['G3'] = fac < flint.arb('1500') and fac > flint.arb('1000')
    print('  G1 (certified, exact rationals): rho~ from (tau*, a) back to tau0 = tau* - (4 - a) in 2000 pieces, every '
          'slope >= (1 - m)/(1 + m) with m >= 1/rho~^2: %s; rho~(tau0) = %.6f < 1 (it approaches the horizon from '
          'inside): %s' % (ok1, float(rho_end), OK['G1']))
    print('  G2 (certified, Arb): the local rate kappa(r) on 600 r-cells of [a, b(tau0)]; at r = a: %s (stage1rate5\'s '
          '13.2197 on 400 cells); sup over r >= 0.5: %s, >= 1: %s, >= 2: %s: %s' % (
              cells[0][2].str(6), rate_at(Fr(1, 2), cells, sm).str(6), rate_at(Fr(1), cells, sm).str(6),
              rate_at(Fr(2), cells, sm).str(6), OK['G2']))
    print('  G3 (certified): int_(tau0)^(tau*) kappa(rho~(tau)) dtau <= %s, so the principal-part factor over X*\'s past '
          'is e^((1/2) int) <= %s, against the record\'s e^(kappa Dtau*/2) <= 5.103e10 (classm5 K5): smaller by a '
          'factor %s; pinned in (1000, 1500): %s %s' % (tot.str(6), fac.str(6), (RECORD_K5 / fac).str(3), OK['G3'],
                                                         el()))
    steep = boundary_curve(a_lo, dtau, steep=Fr(5, 4))
    OK['C6'] = not slope_ok(steep)
    print('  C6 (control): the slopes 1.25 times steeper (rho~ moving outward faster than the outgoing null rays): the '
          'future-boundary check fails: %s' % OK['C6'])
    return fac


def check_chain(fac):
    a = SR.a_ball() if hasattr(SR, 'a_ball') else None
    q0 = (flint.arb(9) / 1250) ** (flint.arb(1) / 8)
    a = q0 / 2
    base = 4 * C_LO / 3 * a ** flint.arb(-1.5)
    capp = flint.arb(CAPP.numerator) / CAPP.denominator
    ok_base = base > capp
    pert = 4 * C_HI / 3 * (a + flint.arb(1) / 100) ** flint.arb(-1.5)
    OK['C5'] = not (pert > capp)
    print('  The chain (deduced, R8.2, READ classm5 K1-K2, K4): C_app >= (4/3) K + |M_22| at X*, (4/3) K >= %s > '
          '12.593309: %s; an enclosure [lo, hi] of M_22, 0 not in it, would give lambda0 < 0.0024433 x 12.593309/'
          '(12.593309 + min(|lo|, |hi|)) (operator norm). No enclosure is computed here (LAMBDA0-DATA5.md, M_22).' % (
              base.str(9), ok_base))
    print('  C5 (control): X* perturbed to r = a + 1/100: (4/3) env(2) r^(-3/2) <= %s < 12.593309, so the base of the '
          'chain fails there: %s' % (pert.str(9), OK['C5']))
    tol = 1 / fac
    print('  The tolerance (deduced, the reading of classm5 K5): an a posteriori enclosure of M_22 through Lemma 2.3\'s '
          'principal part needs the residual below |M_22| times about %s (was 2e-11), before c_Y q^(1/2) (<= 2^(1/2) '
          'x 37.8, stage1rate5 K3), the lower-order coefficients and the Sobolev constant of the point value; not met: '
          'no approximate solution of the evolution exists here.' % tol.str(3))
    return ok_base


def main():
    print('lam0data5: the stage-1 data on Sigma (S_1, B_1), an admissible envelope, and the stability constant over X*\'s '
          'past (CONSTANTS5.md R8.2 blocks (a)-(c))')
    F0, first = check_d1_d2()
    CO, M1, g2 = check_d3_d4(F0)
    fode, Mc = check_d5(CO)
    print('  D6 (computed, floating point): the identity at finite lam, E = 1 + v/4, the record\'s H, A = 1, test a, w, q:')
    res = check_d6(CO, M1, F0)
    ps = assess_d6(res)
    OK['D6'] = all(p >= 1.6 for p, rem in ps.values())
    for t_ in sorted(res):
        print('      th = %.2f: remainders W(lam) - lam I1 at lam = 1/32, 1/64 and orders p: %s' % (t_, '; '.join(
            '%s %.2e %.2e p = %.2f' % (nm, ps[(t_, nm)][1][0], ps[(t_, nm)][1][1], ps[(t_, nm)][0])
            for nm in ('Jr', 'Jt', 'rho'))))
    print('  D6: every remainder of order lam^2 (p >= 1.6): %s %s' % (OK['D6'], el()))
    p1 = assess_d6(res, flipS=True)
    OK['C1'] = not all(p >= 1.6 for p, rem in p1.values())
    print('  C1 (control): S_1 with its sign flipped: orders %s: D6 fails: %s' % (
        ['%.2f' % p for (t_, nm), (p, rem) in sorted(p1.items()) if nm == 'Jt'], OK['C1']))
    p2 = assess_d6(res, lab='no phase')
    OK['C2'] = not all(p >= 1.6 for p, rem in p2.values())
    print('  C2 (control): the phase d_tau phi_1 = -a/2 dropped from the data: orders (J_r, rho) %s: D6 fails: %s' % (
        ['%.2f' % p for (t_, nm), (p, rem) in sorted(p2.items()) if nm != 'Jt'], OK['C2']))
    p3 = assess_d6(res, dropB=True)
    OK['C3'] = not all(p >= 1.6 for p, rem in p3.values())
    print('  C3 (control): B_1 dropped from the prediction: orders (J_r, rho) %s: D6 fails: %s' % (
        ['%.2f' % p for (t_, nm), (p, rem) in sorted(p3.items()) if nm != 'Jt'], OK['C3']))
    check_d7(fode)
    check_d8(fode, M1, F0)
    check_e1()
    fac = check_g()
    check_chain(fac)
    print('  Not decided here (LAMBDA0-DATA5.md): a certified enclosure of M_22 = (m_1)_phi1phi1(X*)/a^2, which needs a '
          'validated solve of Lemma 5.3 (a)-(c) at m = 1 on X*\'s past from the Cauchy data of D2, D4, D5, D7.')
    for k, val in OK.items():
        builtins.print(k, 'PASS' if val else 'FAIL')
    builtins.print('lam0data5: %d/%d %s' % (sum(OK.values()), len(OK), el()))
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
