#!/usr/bin/env python3
"""stage0bd5: certified bounds, to order 14, on every derivative of the explicit profiles of Theorem A at the paper's
point with envelope5.py's smooth envelope: the wave W_TT, the second harmonic chi dv dv (together g_1 - m_1 at phi_1 =
0) and the stage-1 mean source S (CONSTANTS5.md, Round 2, item (i)).

The objects (READ: lead5.py's W_TT and its L4 transport; checks/stage5.out S2 for S; f computed here with lead5.py's
reduced Ricci, as checks/stage5.py `source` does), in Eddington-Finkelstein components, A = 1:

    W_TT = r^2 (-2 (P1 + P2) dth^2 + 2 c^2 P1 dphi1^2 + 2 s^2 P2 dphi2^2),  K = E(v) H(th) r^(-3/2),
           P1 = K (2 c^2 cos s - s^2 sin s)/3,  P2 = K (2 s^2 sin s - c^2 cos s)/3,  H = (2/(1 + cos^2 2th))^(1/2);
    chi  = -(1/12) E^2 H^2 (4 cos2th sin 2s + sin^2 2th cos 2s) (r^-2 - (v - tau0)^(-1/2) r^(-3/2))   (times dv dv);
    S    = -(4/9) E^2 H^2 sin 2th r^-3 (dv dth + dth dv)                                    (the s-mean of R^(1)).

In Cartesian (tau, x), with rho1^2 = x1^2 + x2^2, rho2^2 = x3^2 + x4^2, R2 = |x|^2, c^2 = rho1^2/R2, s^2 = rho2^2/R2,
eta1 = x1 dx1 + x2 dx2, eta2 = x3 dx3 + x4 dx4, d12 = dx1^2 + dx2^2, d34 = dx3^2 + dx4^2, U = dtau + xhat.dx = dv and
k = H R2^(-3/4) (deduced; checked against the pullback, X1):

    W_TT = E(v) (Gc cos s + Gs sin s),
      Gc = (k/3) (4c^2 d12 - 2c^2 d34 - (2/R2)(2c^2 + 3s^2) eta1 eta1 + (2/R2) c^2 eta2 eta2 + (2c^2/R2)(eta1 eta2 + eta2 eta1)),
      Gs = (k/3) (-2s^2 d12 + 4s^2 d34 + (2/R2) s^2 eta1 eta1 - (2/R2)(2s^2 + 3c^2) eta2 eta2 + (2s^2/R2)(eta1 eta2 + eta2 eta1)),
    chi dv dv = E^2 (Ga) + E^2 (v - tau0)^(-1/2) (Gb),  Ga = -(1/12) H^2 R2^-1 T2 U U,  Gb = -R2^(1/4) Ga,
      T2 = 4 (c^2 - s^2) sin 2s + 4 c^2 s^2 cos 2s,
    S = -(4/9) E^2 H^2 R2^(-3/2) (U xi + xi U),  xi = sin2th dth = 2 (c^2 eta2 - s^2 eta1)/R2,

each smooth on r > 0 (the axes rho1 = 0, rho2 = 0 included). Labels: computed (interval arithmetic; floating point where
said); deduced (the bound calculus below).

  The bound calculus (deduced). For a tensor field F put D_F[n] := sup_points sup_{|e| = 1} ||(e.d)^n F||_Frobenius,
  e a unit vector in (tau, x, s). By Banach's theorem on symmetric multilinear forms on a Hilbert space, every
  component of every n-th derivative is at most D_F[n]. Along a line the product and chain rules are one-dimensional:
  D_{FG}[n] <= sum_j C(n, j) D_F[j] D_G[n - j] (also for outer products of tensors) and D_{h o q}[n] <= sum_k
  sup|h^(k)| B_{n,k}(D_q[1], D_q[2], ...) (Bell polynomials). The pieces, on the unit sphere |x| = 1 (sup over the
  sphere and over unit e): |x|^-alpha has D[m] = (alpha)_m exactly, attained radially (|x + t e|^-alpha = sum_m
  C_m^(alpha/2)(-tau) t^m, |C_m^lambda| <= C_m^lambda(1) for lambda > 0); x1^2 + x2^2, x3^2 + x4^2 and their difference
  have D = (1, 2, 2, 0, ...); eta1, eta2 and x have D = (1, 1, 0, ...); d12, d34 have Frobenius norm 2^(1/2); H =
  h(q), q = cos 2th = (rho1^2 - rho2^2)/R2 in [-1, 1], h = 2^(1/2) (1 + q^2)^(-1/2), sup|h^(k)| on [-1, 1] by interval
  Taylor arithmetic in the centred form (as envelope5.py); H^2 likewise. Every x-tensor is homogeneous (Gc, Gs, Gb of
  degree -3/2, Ga of degree -2, S's x-factor of degree -4), so on |x| = r its majorant is r^(deg - m) times the unit
  one, largest at r = a. The envelope enters through v = tau + r: V_1 = 2^(1/2), V_m <= m! r^(1-m) g_m (m >= 2), g_m
  the sup of the Gegenbauer polynomial |C_m^(-1/2)| on [-1, 1] (|x + s e| = r sum_m C_m^(-1/2)(t) (-s/r)^m); and
  the phase: the s-derivatives of cos(h s), sin(h s) cost h per order, with ||A cos + B sin|| <= (||A||^2 +
  ||B||^2)^(1/2). Every factor decreases in r, so the bounds at r = a hold on all of Omega x S^1. (A first version
  used Cauchy's estimate on complex polydiscs; complex rectangle arithmetic could not certify the branch of H beyond
  radius 0.04 r, where the factor 25^n made the bounds useless, so it was replaced.)

  X1 (floating point) the Cartesian forms equal the pullbacks of the EF forms at 400 random points (relative error
     < 1e-10), chi solves (d_r + 3/(2r)) d_s chi = r^-3 f with zero data on Sigma_tau0 (sympy, exact), and the
     Cartesian components stay bounded at the axes.
  X2 (certified) the support: on Omega, E(v) != 0 forces r in [a, 11/2]; the boxes cover r in [0.2698, 5.5] x th in
     [0, pi/2].
  X3 (certified) D[n], n = 0..14, for W_TT, chi dv dv, their sum (g_1 - m_1 at phi_1 = 0) and S, on Omega x S^1.
     Not sharp: the composition majorant for H loses up to about 1e5 at order 11 against the scale of H's complex
     singularities (q = +-i, at imaginary distance 0.44 in th), and the Leibniz sums lose more.
  X4 (certified) a lower bound: at v = 2, r = 0.27 > a, the operator norm of W_TT exceeds a certified value, so every
     admissible C_app (|g_app - g0| <= C_app lam, which forces C_app >= sup |W_TT|_op: g_1 = m_1 + W(X, th + phi_1),
     and W_TT changes sign under th -> th + pi while m_1 and chi do not) is at least that, and lambda0 <=
     eps1/(2 C_app) <= 0.60132/(2 C_app) for every admissible eps1 (eps1hyp5.py H3).
  Controls (must fail, and do): C1 a sign flipped in Gc's cross term breaks X1; C2 the majorant (3/2)_m of |x|^(-3/2)
  equals its radial derivative at every order (exact), so "half the majorant" is refuted; C3 the order-1 bound for
  W_TT is above a finite-difference value at one point (floating point) and the claim D/1e9 is refuted by it.

    python3 checks/stage0bd5.py        (about ten minutes, most of it envelope5's bounds)
"""
import math
import os
import random
import sys
import textwrap
import time
from fractions import Fraction as Fr

import mpmath
import numpy as np
import sympy as sp
from mpmath import iv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import envelope5 as EV  # noqa: E402
import lzeroconst5 as LZ  # noqa: E402

iv.prec = 80
mpmath.mp.prec = 80
KMAX = 14
R_LO, R_HI = Fr(2698, 10000), Fr(11, 2)
TAU0 = -2


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


lo_end, hi_end = EV.lo_end, EV.hi_end


def fiv(q):
    """a Fraction as a (narrow) mpmath.iv interval"""
    return iv.mpf(q.numerator) / q.denominator


class CI:
    """complex rectangle: re + i im, re and im mpmath.iv intervals"""
    __slots__ = ('re', 'im')

    def __init__(self, re, im=0):
        self.re = re if isinstance(re, type(iv.mpf(0))) else iv.mpf(re)
        self.im = im if isinstance(im, type(iv.mpf(0))) else iv.mpf(im)

    def __add__(self, o):
        o = o if isinstance(o, CI) else CI(o)
        return CI(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, CI) else CI(o)
        return CI(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return CI(o) - self

    def __neg__(self):
        return CI(-self.re, -self.im)

    def __mul__(self, o):
        if not isinstance(o, CI):
            o = iv.mpf(o)
            return CI(self.re * o, self.im * o)
        return CI(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def sq(self):
        return CI(self.re ** 2 - self.im ** 2, 2 * self.re * self.im)

    def abs2(self):
        return self.re ** 2 + self.im ** 2

    def __truediv__(self, o):
        if not isinstance(o, CI):
            o = iv.mpf(o)
            return CI(self.re / o, self.im / o)
        d = o.abs2()
        if not lo_end(d) > 0:
            raise ZeroDivisionError
        return CI(self.re * o.re + self.im * o.im, self.im * o.re - self.re * o.im) * (1 / d)

    def mod_hi(self):
        return hi_end(iv.sqrt(self.abs2()))

    def mod_lo(self):
        return lo_end(iv.sqrt(self.abs2()))


def gegen_sup(m):
    """sup over [-1, 1] of |C_m^(-1/2)| (exact recurrence; certified sup via round 1's poly_sup on [0, 1], parity)"""
    C = [[Fr(1)], [Fr(0), Fr(-1)]]
    for n in range(2, m + 1):
        a = [Fr(0)] + [2 * (n - Fr(3, 2)) * c for c in C[n - 1]]
        b = C[n - 2] + [Fr(0)] * (len(a) - len(C[n - 2]))
        C.append([(x - (n - 3) * y) / n for x, y in zip(a, b)])
    return LZ.poly_sup(C[m], N=4000)


def bell(V, n):
    """B[n][k] partial Bell polynomials at the nonnegative intervals V[1..n] (iv)"""
    B = [[iv.mpf(0)] * (n + 1) for _ in range(n + 1)]
    B[0][0] = iv.mpf(1)
    for nn in range(1, n + 1):
        for k in range(1, nn + 1):
            B[nn][k] = sum((math.comb(nn - 1, i - 1) * V[i] * B[nn - i][k - 1] for i in range(1, nn - k + 2)),
                           iv.mpf(0))
    return B


def fdb(F, B, n):
    return F[0] if n == 0 else sum((F[k] * B[n][k] for k in range(1, n + 1)), iv.mpf(0))


def seq_mul(A, B):
    """Leibniz majorant along a line: D_{AB}[n] <= sum_j C(n, j) D_A[j] D_B[n - j]"""
    return [sum((math.comb(n, j) * A[j] * B[n - j] for j in range(n + 1)), iv.mpf(0)) for n in range(len(A))]


def seq_add(*Ss, w=None):
    w = w or [1] * len(Ss)
    return [sum((c * S_[n] for c, S_ in zip(w, Ss)), iv.mpf(0)) for n in range(len(Ss[0]))]


def seq_scale(S_, c):
    return [x * c for x in S_]


def pochhammer(alpha):
    """|x|^-alpha on the unit sphere: sup |(e.d)^m| = (alpha)_m, attained radially (|x + te|^-alpha = sum_m
    C_m^(alpha/2)(-tau) t^m and |C_m^lambda| <= C_m^lambda(1) = (2 lambda)_m/m! for lambda > 0)"""
    out = [iv.mpf(1)]
    for m in range(1, KMAX + 1):
        out.append(out[-1] * (fiv(alpha) + m - 1))
    return out


def ts_pow(a, p):
    """a^p for a Fraction p, a[0] > 0: n a0 b_n = sum_{j=1}^{n} ((p + 1) j - n) a_j b_(n-j)"""
    K = len(a) - 1
    if not lo_end(a[0]) > 0:
        raise ValueError('power of a series with non-positive constant term')
    pp = fiv(p)
    b = [iv.exp(pp * iv.log(a[0]))]
    for n in range(1, K + 1):
        b.append(sum((((pp + 1) * j - n) * a[j] * b[n - j] for j in range(1, n + 1)), iv.mpf(0)) / (n * a[0]))
    return b


def h_bounds(power, scale, cells=400, J=4):
    """sup over q in [-1, 1] of |d^k [scale (1 + q^2)^power]|, k <= KMAX (even function; centred interval form)"""
    best = [mpmath.mpf(0)] * (KMAX + 1)
    for i in range(cells):
        lo, hi = mpmath.mpf(i) / cells, mpmath.mpf(i + 1) / cells
        mid, h = (lo + hi) / 2, (hi - lo) / 2
        ser = {}
        for key, q0 in (('m', iv.mpf(mid)), ('c', iv.mpf([lo, hi]))):
            qq = EV.ts_mul(EV.ts_var(q0, KMAX + J), EV.ts_var(q0, KMAX + J))
            one = EV.ts_const(1, KMAX + J)
            ser[key] = EV.ts_scale(ts_pow([x + y for x, y in zip(one, qq)], power), scale)
        for k in range(KMAX + 1):
            v = sum(EV.ivmax_abs(ser['m'][k + j]) * math.factorial(k + j) / math.factorial(j) * h ** j for j in range(J))
            v += EV.ivmax_abs(ser['c'][k + J]) * math.factorial(k + J) / math.factorial(J) * h ** J
            best[k] = max(best[k], v * EV.SAFE)
    return [iv.mpf(b) for b in best]


def x_tensors(gs):
    """majorants D[m](1) on the unit sphere of the analytic x-tensors (see the docstring), iv sequences"""
    K = KMAX
    zero = [iv.mpf(0)] * (K + 1)
    P = [iv.mpf(1), iv.mpf(2), iv.mpf(2)] + zero[3:]          # x1^2 + x2^2, x3^2 + x4^2, and their difference
    eta = [iv.mpf(1), iv.mpf(1)] + zero[2:]                   # eta1, eta2 (vectors), and x itself
    const2 = [iv.sqrt(iv.mpf(2))] + zero[1:]                  # d12, d34 (Frobenius sqrt 2)
    iR2, R2_34, R2_32, ir = pochhammer(Fr(2)), pochhammer(Fr(3, 2)), pochhammer(Fr(3)), pochhammer(Fr(1))
    c2 = seq_mul(P, iR2)
    s2 = c2
    q = seq_mul(P, iR2)
    q[0] = iv.mpf(1)                                          # |cos 2th| <= 1
    c2[0] = iv.mpf(1)
    hH = h_bounds(Fr(-1, 2), iv.sqrt(iv.mpf(2)))
    hH2 = h_bounds(Fr(-1), iv.mpf(2))
    H = [fdb_seq(hH, q, n) for n in range(K + 1)]
    H2 = [fdb_seq(hH2, q, n) for n in range(K + 1)]
    xhat = seq_mul(eta, ir)
    U = [iv.sqrt(iv.mpf(2))] + xhat[1:]
    UU = seq_mul(U, U)
    e11 = seq_mul(eta, eta)
    cross = seq_scale(seq_mul(eta, eta), 2)
    Bc = seq_add(seq_mul(c2, const2), seq_mul(c2, const2), seq_mul(iR2, seq_mul(seq_add(c2, s2, w=[2, 3]), e11)),
                 seq_mul(iR2, seq_mul(c2, e11)), seq_mul(c2, seq_mul(iR2, cross)), w=[4, 2, 2, 2, 2])
    Gc = seq_scale(seq_mul(H, seq_mul(R2_34, Bc)), iv.mpf(1) / 3)
    Gs = Gc                                                   # the same majorant (c and s exchanged)
    c2s2 = seq_mul(c2, s2)
    c2s2[0] = iv.mpf(1) / 4                                   # c^2 s^2 = sin^2(2th)/4 <= 1/4
    Ga_s2 = seq_scale(seq_mul(H2, seq_mul(iR2, seq_mul(q, UU))), iv.mpf(4) / 12)
    Ga_c2 = seq_scale(seq_mul(H2, seq_mul(iR2, seq_mul(c2s2, UU))), iv.mpf(4) / 12)
    Gb_s2 = seq_scale(seq_mul(H2, seq_mul(R2_34, seq_mul(q, UU))), iv.mpf(4) / 12)
    Gb_c2 = seq_scale(seq_mul(H2, seq_mul(R2_34, seq_mul(c2s2, UU))), iv.mpf(4) / 12)
    xi = seq_scale(seq_mul(seq_add(seq_mul(c2, eta), seq_mul(s2, eta)), iR2), 2)
    GS = seq_scale(seq_mul(H2, seq_mul(R2_32, seq_mul(U, xi))), iv.mpf(8) / 9)
    blocks = {'R2^-3/4': R2_34, 'H': H, 'H2': H2, 'q': q, 'U': U}
    return blocks, {'Gc': Gc, 'Gs': Gs, 'Ga_c2': Ga_c2, 'Ga_s2': Ga_s2, 'Gb_c2': Gb_c2, 'Gb_s2': Gb_s2, 'GS': GS}


def fdb_seq(Fk, D, n):
    """Faa di Bruno majorant for h(q(x)) along a line: sum_k sup|h^(k)| B_{n,k}(D[1], D[2], ...)"""
    if n == 0:
        return Fk[0]
    Vv = [None] + D[1:]
    B = bell(Vv, n)
    return sum((Fk[k] * B[n][k] for k in range(1, n + 1)), iv.mpf(0))


def env_funcs(ek):
    E = [iv.mpf(e) for e in ek]
    E2 = [sum((math.comb(k, j) * E[j] * E[k - j] for j in range(k + 1)), iv.mpf(0)) for k in range(KMAX + 1)]
    q = []
    for m in range(KMAX + 1):
        pr = iv.mpf(1)
        for i in range(m):
            pr *= iv.mpf(1) / 2 + i
        q.append(pr * (iv.mpf(5) / 2) ** (-iv.mpf(1) / 2 - m))         # v - tau0 >= 5/2 on supp E
    E2k = [sum((math.comb(k, j) * E2[j] * q[k - j] for j in range(k + 1)), iv.mpf(0)) for k in range(KMAX + 1)]
    return E, E2, E2k


# ---- X1: the Cartesian forms against the EF pullbacks (floating point) ----
def ef_pullback(X, s_, which):
    tau, x = X[0], np.array(X[1:])
    r = np.linalg.norm(x)
    rho1, rho2 = np.hypot(x[0], x[1]), np.hypot(x[2], x[3])
    c, s = rho1 / r, rho2 / r
    th = math.atan2(rho2, rho1)
    H = math.sqrt(2 / (1 + math.cos(2 * th) ** 2))
    grad_r = np.concatenate([[0.0], x / r])
    grad_v = np.concatenate([[1.0], x / r])
    g_rho1 = np.array([0, x[0], x[1], 0, 0]) / rho1
    g_rho2 = np.array([0, 0, 0, x[2], x[3]]) / rho2
    grad_th = (rho1 * g_rho2 - rho2 * g_rho1) / r ** 2
    grad_p1 = np.array([0, -x[1], x[0], 0, 0]) / rho1 ** 2
    grad_p2 = np.array([0, 0, 0, -x[3], x[2]]) / rho2 ** 2
    if which == 'TT':
        K = H * r ** -1.5
        P1 = K * (2 * c * c * math.cos(s_) - s * s * math.sin(s_)) / 3
        P2 = K * (2 * s * s * math.sin(s_) - c * c * math.cos(s_)) / 3
        return r * r * (-2 * (P1 + P2) * np.outer(grad_th, grad_th) + 2 * c * c * P1 * np.outer(grad_p1, grad_p1)
                        + 2 * s * s * P2 * np.outer(grad_p2, grad_p2))
    if which == 'S':
        Svth = -4 / 9 * H * H * math.sin(2 * th) * r ** -3
        return Svth * (np.outer(grad_v, grad_th) + np.outer(grad_th, grad_v))
    raise ValueError(which)


def cart_form(X, s_, which, flip=False):
    tau, x = X[0], np.array(X[1:])
    R2 = x @ x
    r = math.sqrt(R2)
    c2, s2 = (x[0] ** 2 + x[1] ** 2) / R2, (x[2] ** 2 + x[3] ** 2) / R2
    H = math.sqrt(2 * R2 * R2 / (R2 * R2 + (x[0] ** 2 + x[1] ** 2 - x[2] ** 2 - x[3] ** 2) ** 2))
    eta1 = np.array([0, x[0], x[1], 0, 0])
    eta2 = np.array([0, 0, 0, x[2], x[3]])
    d12 = np.diag([0, 1.0, 1, 0, 0])
    d34 = np.diag([0, 0, 0, 1.0, 1])
    U = np.concatenate([[1.0], x / r])
    if which == 'TT':
        k = H * R2 ** -0.75
        sg = -1 if flip else 1
        Gc = k / 3 * (4 * c2 * d12 - 2 * c2 * d34 - 2 / R2 * (2 * c2 + 3 * s2) * np.outer(eta1, eta1)
                      + 2 / R2 * c2 * np.outer(eta2, eta2) + sg * 2 * c2 / R2 * (np.outer(eta1, eta2) + np.outer(eta2, eta1)))
        Gs = k / 3 * (-2 * s2 * d12 + 4 * s2 * d34 + 2 / R2 * s2 * np.outer(eta1, eta1)
                      - 2 / R2 * (2 * s2 + 3 * c2) * np.outer(eta2, eta2) + 2 * s2 / R2 * (np.outer(eta1, eta2)
                                                                                     + np.outer(eta2, eta1)))
        return Gc * math.cos(s_) + Gs * math.sin(s_)
    if which == 'S':
        xi = 2 * (c2 * eta2 - s2 * eta1) / R2
        return -4 / 9 * H * H * R2 ** -1.5 * (np.outer(U, xi) + np.outer(xi, U))
    raise ValueError(which)


def x1_check():
    rng = np.random.default_rng(7)
    worst = 0.0
    worst_flip = 0.0
    for _ in range(400):
        r = rng.uniform(0.27, 5.5)
        d = rng.normal(size=4)
        x = r * d / np.linalg.norm(d)
        X = [rng.uniform(-2, 3.9), *x]
        s_ = rng.uniform(0, 2 * math.pi)
        for which in ('TT', 'S'):
            A = ef_pullback(X, s_, which)
            B = cart_form(X, s_, which)
            worst = max(worst, np.abs(A - B).max() / max(1e-300, np.abs(A).max()))
        worst_flip = max(worst_flip, np.abs(ef_pullback(X, s_, 'TT') - cart_form(X, s_, 'TT', flip=True)).max()
                         / np.abs(ef_pullback(X, s_, 'TT')).max())
    # the axes: rho1 = 0 and rho2 = 0
    axes = [np.abs(cart_form([0, 0, 0, 1.0, 0.3], 0.4, w)).max() + np.abs(cart_form([0, 1.0, 0.2, 0, 0], 0.4, w)).max()
            for w in ('TT', 'S')]
    # chi: the transport and the zero data, exactly
    v, r, th, s_, t0 = sp.symbols('v r theta s tau0', real=True)
    E2H2 = sp.Function('Q')(v, th)                                  # E^2 H^2, any
    f = E2H2 / 12 * (4 * sp.cos(2 * th) * sp.cos(2 * s_) - sp.sin(2 * th) ** 2 * sp.sin(2 * s_))
    chi = -E2H2 / 12 * (4 * sp.cos(2 * th) * sp.sin(2 * s_) + sp.sin(2 * th) ** 2 * sp.cos(2 * s_)) * (
        r ** -2 - (v - t0) ** sp.Rational(-1, 2) * r ** sp.Rational(-3, 2))
    transport = sp.simplify(sp.diff(chi, r, s_) + sp.Rational(3, 2) * sp.diff(chi, s_) / r - f / r ** 3) == 0
    zero_data = sp.simplify(chi.subs(r, v - t0)) == 0
    # f as lead5 gives it (getf, run here with the record's H left symbolic): (A^2/24) E^2 H^2 (sin2s (cos4th - 1)
    # - 8 sin^4 cos2s + 8 cos^4 cos2s); equal to the f above
    lead_f = E2H2 / 24 * (sp.sin(2 * s_) * sp.cos(4 * th) - sp.sin(2 * s_) - 8 * sp.sin(th) ** 4 * sp.cos(2 * s_)
                          + 8 * sp.cos(th) ** 4 * sp.cos(2 * s_))
    same_f = sp.simplify(sp.expand_trig(lead_f - f)) == 0
    return worst, worst_flip, axes, transport, zero_data, same_f


def lead_f_from_lead5():
    """the vv second harmonic of R^(0) times r^3, from lead5.py itself (about 25 s), against the closed form"""
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import lead5 as L
    W0 = L.wave(with_chi=False)
    R = L.reduced_ricci(W0)
    cp, cm = L.modes(R[(0, 0)][1])[2]
    F = sp.expand((cp + cm) * sp.cos(2 * L.s) + sp.I * (cp - cm) * sp.sin(2 * L.s))
    f = sp.simplify(F * L.r ** 3)
    want = L.A ** 2 * L.Ef ** 2 * L.Hf ** 2 / 12 * (4 * sp.cos(2 * L.th) * sp.cos(2 * L.s)
                                                    - sp.sin(2 * L.th) ** 2 * sp.sin(2 * L.s))
    return sp.simplify(sp.expand_trig(f - want)) == 0


def main():
    t_start = time.time()
    ok = {}
    worst, worst_flip, axes, transport, zero_data, same_f = x1_check()
    from_lead5 = lead_f_from_lead5()
    ok['X1'] = worst < 1e-10 and transport and zero_data and same_f and from_lead5 and all(np.isfinite(axes))
    ok['C1'] = worst_flip > 1e-3
    say('  X1: Cartesian forms against the EF pullbacks at 400 random points: largest relative error %.2e; components at '
        'the axes finite (%s); chi: (d_r + 3/(2r)) d_s chi = r^-3 f %s, zero on Sigma_tau0 %s; f equals lead5.py\'s vv '
        'second harmonic (recomputed from lead5.py: %s)' % (worst, ['%.3g' % a for a in axes], transport, zero_data,
                                                            same_f and from_lead5))
    say('  C1 (control): Gc\'s cross term with its sign flipped: relative error %.3f' % worst_flip)

    clo, chi_, ek, _, _, _, _ = EV.envelope_bounds()
    E, E2, E2k = env_funcs(ek)
    say('      envelope (envelope5.py): c in [%s, %s]; e_k <= %s' % (mpmath.nstr(clo, 9), mpmath.nstr(chi_, 9),
                                                                    ', '.join(mpmath.nstr(e, 3) for e in ek)))
    g = LZ.geometry()
    a_lo = g['a'][0]
    tau_end_hi = g['tau_end'][1]
    ok['X2'] = R_LO < a_lo and Fr(7, 2) - TAU0 == R_HI and Fr(1, 2) - tau_end_hi < a_lo
    say('  X2: on Omega, E(v) != 0 needs v in (1/2, 7/2) and tau in [tau0, tau_end] (tau_end <= %.6f), so r = v - tau in '
        '[a, 11/2]; a >= %.9f > %s: %s' % (float(tau_end_hi), float(a_lo), float(R_LO), ok['X2']))

    gs = [None, None] + [gegen_sup(m) for m in range(2, KMAX + 1)]
    blocks, G = x_tensors(gs)
    a = fiv(a_lo)
    deg = {'Gc': Fr(-3, 2), 'Gs': Fr(-3, 2), 'Ga_c2': Fr(-2), 'Ga_s2': Fr(-2), 'Gb_c2': Fr(-3, 2), 'Gb_s2': Fr(-3, 2),
           'GS': Fr(-4)}
    Dg = {k: [G[k][m] * a ** (fiv(deg[k]) - m) for m in range(KMAX + 1)] for k in G}   # homogeneity: radius a
    V = [None, iv.sqrt(iv.mpf(2))] + [iv.mpf(math.factorial(m)) * a ** (1 - m) * fiv(gs[m]) for m in range(2, KMAX + 1)]
    B = bell(V, KMAX)
    FE = [fdb(E, B, n) for n in range(KMAX + 1)]
    FE2 = [fdb(E2, B, n) for n in range(KMAX + 1)]
    FE2k = [fdb(E2k, B, n) for n in range(KMAX + 1)]
    DT = [sum((math.comb(m, i) * iv.sqrt(Dg['Gc'][i] ** 2 + Dg['Gs'][i] ** 2) for i in range(m + 1)), iv.mpf(0))
          for m in range(KMAX + 1)]
    Da = [sum((math.comb(m, i) * 2 ** (m - i) * iv.sqrt(Dg['Ga_c2'][i] ** 2 + Dg['Ga_s2'][i] ** 2)
               for i in range(m + 1)), iv.mpf(0)) for m in range(KMAX + 1)]
    Db = [sum((math.comb(m, i) * 2 ** (m - i) * iv.sqrt(Dg['Gb_c2'][i] ** 2 + Dg['Gb_s2'][i] ** 2)
               for i in range(m + 1)), iv.mpf(0)) for m in range(KMAX + 1)]
    best = {}
    best['TT'] = [sum((math.comb(n, j) * FE[j] * DT[n - j] for j in range(n + 1)), iv.mpf(0)) for n in range(KMAX + 1)]
    best['chi'] = [sum((math.comb(n, j) * (FE2[j] * Da[n - j] + FE2k[j] * Db[n - j]) for j in range(n + 1)), iv.mpf(0))
                   for n in range(KMAX + 1)]
    best['W'] = [best['TT'][n] + best['chi'][n] for n in range(KMAX + 1)]
    best['S'] = [sum((math.comb(n, j) * FE2[j] * Dg['GS'][n - j] for j in range(n + 1)), iv.mpf(0))
                 for n in range(KMAX + 1)]
    ok['X3'] = all(hi_end(best['W'][n]) < mpmath.mpf(10) ** 60 for n in range(KMAX + 1))
    say('      the x-tensors on the unit sphere (majorants D[m](1), m = 0..%d): Gc %s; GS %s' % (
        KMAX, ', '.join(mpmath.nstr(hi_end(x), 3) for x in G['Gc']), ', '.join(mpmath.nstr(hi_end(x), 3)
                                                                               for x in G['GS'])))
    for key, label in (('TT', 'W_TT'), ('chi', 'chi dv dv'), ('W', 'W_TT + chi dv dv'), ('S', 'S (stage-1 source)')):
        say('  X3: D[n], n = 0..%d, for %s on Omega x S^1: %s' % (KMAX, label, ', '.join(mpmath.nstr(hi_end(b), 3)
                                                                                   for b in best[key])))

    # C2: the elementary block |x|^(-3/2) is sharp: its majorant (3/2)_m is attained in the radial direction
    exact = [abs(sp.diff((1 + sp.Symbol('t')) ** sp.Rational(-3, 2), sp.Symbol('t'), m).subs(sp.Symbol('t'), 0))
             for m in range(KMAX + 1)]
    maj = blocks['R2^-3/4']
    ok['C2'] = all(lo_end(maj[m]) <= exact[m] <= hi_end(maj[m]) for m in range(KMAX + 1)) and \
        not all(exact[m] <= hi_end(maj[m]) / 2 for m in range(1, KMAX + 1))
    say('  C2 (control): |x|^(-3/2)\'s majorant (3/2)_m equals its radial derivative at every order (sympy, exact), '
        'so the claim "half the majorant bounds it" is refuted: %s' % ok['C2'])

    # C3: finite differences of W_TT at one point against the order-1 bound
    Xp = np.array([1.5, 0.3, 0.0, 0.25, 0.0])
    sp_ = 0.7
    cval = float(clo)
    yv = (2 * (Xp[0] + np.linalg.norm(Xp[1:])) - 4) / 3
    envf = lambda X: cval * math.cos(math.pi * ((2 * (X[0] + np.linalg.norm(X[1:])) - 4) / 3) / 2) ** 12 * math.exp(  # noqa
        -((2 * (X[0] + np.linalg.norm(X[1:])) - 4) / 3) ** 2 / (1 - ((2 * (X[0] + np.linalg.norm(X[1:])) - 4) / 3) ** 2))
    assert abs(yv) < 1
    Wf = lambda X: envf(X) * cart_form(X, sp_, 'TT')  # noqa: E731
    h = 1e-6
    fd = max(np.linalg.norm((Wf(Xp + h * e) - Wf(Xp - h * e)) / (2 * h)) for e in np.eye(5))
    bound1 = float(hi_end(best['TT'][1]))
    ok['C3'] = fd <= bound1 and fd > 0 and not (fd <= bound1 / 10 ** 9)
    say('  C3 (control): a coordinate derivative of W_TT at one point (finite differences) %.4f <= D[1] = %.4f; the '
        'claim D[1]/1e9 is refuted by it: %s' % (fd, bound1, fd > bound1 / 10 ** 9))

    # X4: a lower bound for sup |W_TT|_op, at v = 2 (y = 0, E = c), r = 27/100, th, s on a grid (floating), certified
    best_pt = None
    for th_ in np.linspace(0, math.pi / 2, 61):
        for s_ in np.linspace(0, 2 * math.pi, 121):
            x = 0.27 * np.array([math.cos(th_), 0, math.sin(th_), 0])
            Wm = cart_form([2 - 0.27, *x], s_, 'TT')
            ev_, evec = np.linalg.eigh(Wm)
            i = int(np.argmax(np.abs(ev_)))
            if best_pt is None or abs(ev_[i]) > best_pt[0]:
                best_pt = (abs(ev_[i]), th_, s_, evec[:, i])
    _, th_, s_, u = best_pt
    # certify u^T W_TT u at that point with interval arithmetic (u rounded to rationals, then normalised in iv)
    uq = [fiv(Fr(float(c)).limit_denominator(10 ** 9)) for c in u]
    nu = iv.sqrt(sum((c * c for c in uq), iv.mpf(0)))
    thq = fiv(Fr(float(th_)).limit_denominator(10 ** 6))
    xq = [fiv(Fr(27, 100)) * iv.cos(thq), iv.mpf(0), fiv(Fr(27, 100)) * iv.sin(thq), iv.mpf(0)]
    sq = fiv(Fr(float(s_)).limit_denominator(10 ** 6))
    z = [CI(c) for c in xq]
    p1 = z[0].sq() + z[1].sq()
    p2 = z[2].sq() + z[3].sq()
    R2 = (p1 + p2).re
    c2, s2 = p1.re / R2, p2.re / R2
    H = iv.sqrt(2 * R2 ** 2 / (R2 ** 2 + (p1.re - p2.re) ** 2))
    k = H * R2 ** (-iv.mpf(3) / 4)
    eta1 = [0, xq[0], xq[1], 0, 0]
    eta2 = [0, 0, 0, xq[2], xq[3]]
    Wq = [[iv.mpf(0)] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            gc = (-2 / R2 * (2 * c2 + 3 * s2) * eta1[i] * eta1[j] + 2 / R2 * c2 * eta2[i] * eta2[j]
                  + 2 * c2 / R2 * (eta1[i] * eta2[j] + eta2[i] * eta1[j]))
            gs_ = (2 / R2 * s2 * eta1[i] * eta1[j] - 2 / R2 * (2 * s2 + 3 * c2) * eta2[i] * eta2[j]
                   + 2 * s2 / R2 * (eta1[i] * eta2[j] + eta2[i] * eta1[j]))
            if i == j:
                gc += 4 * c2 * (1 if i in (1, 2) else 0) - 2 * c2 * (1 if i in (3, 4) else 0)
                gs_ += -2 * s2 * (1 if i in (1, 2) else 0) + 4 * s2 * (1 if i in (3, 4) else 0)
            Wq[i][j] = iv.mpf(clo) * k / 3 * (gc * iv.cos(sq) + gs_ * iv.sin(sq))
    quad = sum((uq[i] * Wq[i][j] * uq[j] for i in range(5) for j in range(5)), iv.mpf(0)) / nu ** 2
    capp_lo = min(abs(lo_end(quad)), abs(hi_end(quad))) if (lo_end(quad) > 0 or hi_end(quad) < 0) else 0
    lam_ub = mpmath.mpf('0.60132') / (2 * capp_lo)
    ok['X4'] = capp_lo > 1 and float(capp_lo) <= best_pt[0] * (1 + 1e-6)
    say('  X4: at v = 2, r = 0.27 (tau = 1.73 in [tau0, tau_end], r > a), th = %.4f, s = %.4f: |W_TT|_op >= u^T W_TT u '
        '= %s (certified, E = c taken at c_lo); so every admissible C_app >= %s and lambda0 <= 0.60132/(2 C_app) <= '
        '%s (against lambda_Omega <= 0.026986)' % (th_, s_, mpmath.nstr(capp_lo, 8), mpmath.nstr(capp_lo, 6),
                                                   mpmath.nstr(lam_ub, 6)))
    say('      (%.0f s)' % (time.time() - t_start))
    for kk, vv in ok.items():
        print(kk, 'PASS' if vv else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
