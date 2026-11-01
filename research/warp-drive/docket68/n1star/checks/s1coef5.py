#!/usr/bin/env python3
"""s1coef5: the rho^(2 + d1) coefficient of the s1 state, from the horizon (LOSS-D LD9, D442, D450).

D412 found that the local expansion does not decide whether the s1 state of box^Ups_b carries the root 2 + d1, and D415
deduced that its coefficient depends on the cut-offs the record leaves open. Here the coefficient is computed
for given cut-offs, on five-dimensional Tangherlini (mu = 1), by solving the s1 system from the horizon.

The operator is III.B Definition 6.1's: box^Ups = 2(delta + E^Ups) G delta*, E^Ups = E_inf + E_H with E_inf h = -gam_U
(2 iota_(g^-1 c) h - (2/3)(1 - e_U) c tr h), c = zeta(r) r^-1 dt, and E_H h = gam_H (2 iota_(g^-1 c_H) h - (2/3) c_H tr
h), c_H = -(1/2) eta(r) dr (D3's rotation-invariant choice, eta for its chi). zeta is taken to vanish near the horizon,
where dt is singular (smoothness needs only zeta = O(r - 1)), and is 1 for large r; eta is 1 near the horizon and 0 for
large r. Ingoing coordinates (v, r, chi, theta, phi), f = 1 - 1/r^2; the l = 1 scalar-type 1-form omega = A(r) Y dv +
B(r) Y dr + K(r) r dY, Y = cos chi, and box^Ups omega = 0 is three second-order ODEs for U = (A, B, K).

  S1 (computed, exact) the ODEs reproduce genstates5.boxU in static coordinates (zeta = 1, eta = 0), a dv + (b - a/f) dr
     for a dt + b dr, at two rational points; the theta, phi components vanish.
  S2 (computed, exact) the indicial determinant at infinity is s(s - 4) q(s), with s1reson5's lambda_s1,2 = 2 + d1 a
     root of q; the other roots are 0, 4, lambda_3 in (3, 4) and 1 - lambda_s1,2, 1 - lambda_3.
  S3 (computed) at the horizon (zeta = 0, eta = 1) the exponents are 0 (four times), 1 and -1. The exponent 1 meets
     the power series at n = 1: its solvability condition removes one combination of U(1) and the exponent-1 solution
     takes its place, so the solutions smooth there are three power series in r - 1 (the last term at r = 1.25 is below
     10^-35).
  S4 (computed) the s1 state: the smooth solution equal at infinity to u_0 + A u_(2+d1) + B3 u_lam3 + B4 u_4, u_0 the
     series from dx^1 = (0, 1, 1) (with the logarithm the root pair 0, 4 forces), the other u's Frobenius series in rho
     with unit leading vectors. Matching at r = 3 and at r = 4, and from r = 1.15 at rtol 1e-12, gives the same A to ten
     digits.
  S5 (computed) A for 22 rows of cut-offs (three repeat the baseline): the transition intervals of zeta and eta moved,
     and compactly supported bumps of amplitude up to 100 added to zeta (on [1.6, 2.4] and [2.55, 2.95]) and to eta. A
     changes with every one that differs from the baseline, by up to 1.60 from it at z = 1/2 (a spread of 1.75), against
     S4's agreement of 10^-10. It is positive at every choice: no zero was found in these families. Verifier 190
     reproduced A by Chebyshev collocation to nine digits (D443).

  S6 (computed; --record) the record's point gam_U = e_U = 1/100 (z = 4 x 10^-6, d1 = 3.3 x 10^-7): A = 141.4268935, the
     same to ten digits at both matching radii and the second start (condition 3 x 10^4 to 10^5), and to 1e-9 by verifier
     194's collocation. u_0's rho^2 coefficient there is (0, -99.75, -100.25) (D412's particular solution), with
     component P_v = -141.42138 along the unit vector v of rho^(2+d1); the near-resonance forces A = -P_v + O(1), and the
     state's rho^2 vector A v + c_2 = (0.0133, 0.2473, -0.2395) is close to D412's finite part (0, 1/4, -1/4), nearly
     orthogonal to v, so A + P_v = 0.0055 is small but not forced (D451). The cut-offs move A by 7 x 10^-6 (zeta's
     interval), 1.9 x 10^-3 (a zeta bump of 20) and 0.17 (an eta bump of 20, through gam_H eta); A + P_v by the same.

  (computed; --zeros) whether a cut-off makes A vanish at the record's point (D457). Every variation is supported in
     (1.25, 3), between the horizon series' start and the matching radius. (a) The sensitivities dA/dzeta(r) and
     dA/deta(r), by symmetric differences of unit bumps of half-width 0.1 at 16 centres, per unit integral, with their
     curvature, and their Riemann sum, a first-order estimate (not a bound: it leaves out (1.25, 1.3) and (2.9, 3), and
     eta0 - 1 there moves A by -0.098; D459, verifier 196); (b) A at the extreme cut-offs valued in [0, 1] (zeta
     switching on at once after 1.25 or as late as 2.95, eta switching off at once or as late as 2.95, and their four
     combinations); (c) A along zeta0 + t b and eta0 + t b, b the most sensitive bump, for |t| from 10 to 10^5, each at
     matching radii 3 and 4, kept only where the two agree to 1e-7 and the condition is below 1e12, a zero bracketed and
     located where a kept A changes sign.

  S8 (computed; --zeros-far) the same sensitivities beyond the matching radius of S7 (D465): matching at r = 8 (A0 there
     against r = 3), unit bumps of half-width 0.2 at centres 3.2, 3.6, ..., 7.6, per unit integral, for zeta and eta;
     and how dA/deta behaves as r grows. It levels off near 0.068 (c_H = -eta dr/2 does not decay), so to first order
     an eta within 1 of the record's moves A by about 0.07 per unit of support; the record confines chi to |x| < 5 R_1
     with R_1 = sqrt(mu_end) = 1 here, which gives about 0.22 on (1.25, 5): 0.130 on (3, 5), S7's eta-only 0.0837 on
     (1.3, 2.9), and 0.0015 and 0.0062 on the gaps (1.25, 1.3), (2.9, 3) that neither samples (D468, verifier 199).

  S9 (computed; --zeros-far-amp, D472) beyond first order outside (1.25, 3): (a) the extreme cut-offs valued in [0, 1]
     that the record's support allows (eta switching off as late as [4.75, 4.95], zeta on as late as [7.5, 7.8], and
     both); (b) A along eta0 + t b (b at r = 4.8, the far side's most sensitive) and zeta0 + t b (r = 3.2), for |t| from
     1 to 10^5, matched at radii 8 and 10; and (d) S7's undecided range, eta0 + t b with S7's most sensitive bump (r =
     2.85) for t from -10^3 to -10^5, matched at 3 and 4. Where the plain matching fails (radii disagreeing or the
     condition 1e12 or more: one horizon solution outgrows the others across a bump of large negative eta), A is computed
     with the horizon columns re-orthonormalised at every step of a grid (coefficient_qr; A depends on those columns only
     through their span), at two radii, the second with half the steps, kept where they agree to 1e-7; (c) that matching
     reproduces the plain one to twelve digits where both are reliable. Every value is reliable; the least A is 107.418
     (eta, t = -10^5), with no sign change; the extremes move A by at most +0.168; S7's undecided range gives A = 130.27
     to 130.48.

  S10 (computed; --zeros-near, D479) inside r = 1.25: the integration started at r = 1.05, where the horizon series still
     converges (A0 the same to ten digits as from 1.25, and at matching radii 3 and 4), so that cut-off variations in
     (1.05, 1.25) can be applied: (a) dA/dzeta and dA/deta from bumps of half-width 0.025 at 1.075, ..., 1.225, and their
     first-order sums, 1.2e-6 and 0.0037; (b) A along zeta0 + t b and eta0 + t b at the most sensitive (r = 1.225), |t|
     from 1 to 10^5, with the QR matching where the plain one fails. Every value is reliable, A stays in [140.34,
     141.96], with no sign change. The interval (1, 1.05), where the series itself assumes zeta = O(r - 1) and eta = 1,
     is not varied.

Parameters: mu = 1, gam_H = 1/10, and (gam_U, e_U) = (1/2, 1/2) (z = 1/2, d1 = 0.0375), (1/4, 1/2) and (1/2, 1/8) (both z
= 1/8, d1 = 0.0101). Series at 40 digits (60 terms); the ODE between r = 1.25 and the matching radius in double precision
(DOP853, rtol 1e-13). About 15 minutes; --zeros-far-amp about 20, --zeros-near about 25.
Not computed: whether these gam_U, e_U, gam_H meet III.D' Proposition 4.1's eps_0, eps_1; cut-off variations inside r =
1.05 (the horizon series' own range) or not rotation invariant; the dual state as a function (S7 measures its pairing
through bumps); and whether the record's later steps hold at the bumped cut-offs, beyond the matching being solvable
there.
"""
import os
import math
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import genstates5 as GS  # noqa: E402

mp.mp.dps = 40
v = sp.Symbol("v", real=True)
r, ch, th, ph = GS.r, GS.ch, GS.th, GS.ph
mu, gU, eU = GS.mu, GS.gU, GS.eU
gH, Zs, Hs, s, rho = sp.symbols("gamma_H Z H s rho")
ANG = {sp.sin(ch): sp.Rational(3, 5), sp.cos(ch): sp.Rational(4, 5), sp.sin(th): sp.Rational(5, 13),
       sp.cos(th): sp.Rational(12, 13)}
ANG2 = {sp.sin(ch): sp.Rational(5, 13), sp.cos(ch): sp.Rational(12, 13), sp.sin(th): sp.Rational(3, 5),
        sp.cos(th): sp.Rational(4, 5)}

def ef_geo():
    X = (v, r, ch, th, ph)
    f = 1 - mu / r**2
    g = sp.zeros(5, 5)
    g[0, 0], g[0, 1], g[1, 0] = -f, 1, 1
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2 * sp.sin(ch)**2, r**2 * sp.sin(ch)**2 * sp.sin(th)**2
    gi = sp.simplify(g.inv())
    Gam = [[[sp.cancel(sum(gi[l, k] * (sp.diff(g[k, m], X[nn]) + sp.diff(g[k, nn], X[m]) - sp.diff(g[m, nn], X[k]))
                           for k in range(5)) / 2) for nn in range(5)] for m in range(5)] for l in range(5)]
    return X, g, gi, Gam, f

def E_full(h, G, Z, H):
    X, g, gi, Gam, f = G
    c = [Z / r, -Z / (r * f), 0, 0, 0]
    cH = [0, -H / 2, 0, 0, 0]
    cs = [sum(gi[a, b] * c[b] for b in range(5)) for a in range(5)]
    cHs = [sum(gi[a, b] * cH[b] for b in range(5)) for a in range(5)]
    tr = GS.trace(h, G)
    return [-gU * (2 * sum(cs[a] * h[a, b] for a in range(5)) - sp.Rational(2, 3) * (1 - eU) * c[b] * tr)
            + gH * (2 * sum(cHs[a] * h[a, b] for a in range(5)) - sp.Rational(2, 3) * cH[b] * tr) for b in range(5)]

def box_ef(w, G, Z, H):
    Gh = GS.Gop(GS.dstar(w, G), G)
    return [2 * (q + e) for q, e in zip(GS.div(Gh, G), E_full(Gh, G, Z, H))]

def derive():
    """M2, M1, M0 with box omega = (M2 U'' + M1 U' + M0 U) times (Y, Y, r dY) componentwise"""
    G = ef_geo()
    Fs = [sp.Function(n)(r) for n in "ABK"]
    C, S = sp.cos(ch), sp.sin(ch)
    w = [Fs[0] * C, Fs[1] * C, -Fs[2] * r * S, 0, 0]
    out = box_ef(w, G, Zs, Hs)
    d2 = sp.symbols("A2 B2 K2")
    d1 = sp.symbols("A1 B1 K1")
    d0 = sp.symbols("A0 B0 K0")
    rep = {}
    for F, a2, a1, a0 in zip(Fs, d2, d1, d0):
        rep[F.diff(r, 2)] = a2
    eqs, eqs2, extra = [], [], []
    for ang, store in ((ANG, eqs), (ANG2, eqs2)):
        comp = [out[0] / C, out[1] / C, out[2] / (-r * S)]
        for q in comp:
            e = q.subs(rep)
            e = e.subs({F.diff(r): a1 for F, a1 in zip(Fs, d1)}).subs({F: a0 for F, a0 in zip(Fs, d0)})
            store.append(sp.cancel(e.subs(ang)))
        extra += [sp.cancel(out[3].subs(rep).subs(ang)), sp.cancel(out[4].subs(rep).subs(ang))]
    same = all(sp.cancel(a - b) == 0 for a, b in zip(eqs, eqs2))
    M = [sp.Matrix(3, 3, lambda i, j: sp.cancel(sp.diff(eqs[i], dd[j]))) for dd in (d2, d1, d0)]
    lin = all(sp.cancel(eqs[i] - sum(M[k][i, j] * (d2, d1, d0)[k][j] for k in range(3) for j in range(3))) == 0
              for i in range(3))
    return M, same and lin, all(sp.cancel(x) == 0 for x in extra)

def check_static(M):
    """S1: zeta = 1, eta = 0 against genstates5.boxU on (a dt + b dr) with a dv + (b - a/f) dr"""
    f = 1 - mu / r**2
    a = 1 / r**2 + 3 / r**3
    b = 2 / r + 1 / r**4
    K = 1 / r + 5 / r**3
    C, S = sp.cos(ch), sp.sin(ch)
    Bsch = GS.boxU([a * C, b * C, -K * r * S, 0, 0], GS.geo(4, False))
    U = [a, b - a / f, K]
    ef = [sum(M[0][i, j] * sp.diff(U[j], r, 2) + M[1][i, j] * sp.diff(U[j], r) + M[2][i, j] * U[j] for j in range(3))
          for i in range(3)]
    ef = [q.subs({Zs: 1, Hs: 0}) for q in ef]
    sch = [Bsch[0] / C, Bsch[1] / C, Bsch[2] / (-r * S)]
    want = [ef[0], ef[1] + ef[0] / f, ef[2]]
    ok = True
    for pt in ({r: sp.Rational(7, 3), mu: 1, gU: sp.Rational(1, 3), eU: sp.Rational(2, 7)},
               {r: sp.Rational(11, 4), mu: sp.Rational(3, 2), gU: sp.Rational(-2, 5), eU: sp.Rational(1, 9)}):
        for x, y in zip(sch, want):
            ok &= sp.nsimplify(sp.cancel(x.subs(ANG).subs(pt) - y.subs(pt))) == 0
    return ok

def taylor(expr, var, N):
    """exact Taylor coefficients 0..N at var = 0 of a rational function regular there"""
    nu, de = sp.fraction(sp.cancel(sp.together(expr)))
    pn = sp.Poly(sp.expand(nu), var)
    pd = sp.Poly(sp.expand(de), var)
    n = [sp.expand(pn.coeff_monomial(var**k)) for k in range(N + 1)]
    d = [sp.expand(pd.coeff_monomial(var**k)) for k in range(N + 1)]
    assert d[0] != 0, "not regular at 0"
    q = []
    for k in range(N + 1):
        q.append(sp.expand((n[k] - sum(d[i] * q[k - i] for i in range(1, k + 1))) / d[0]))
    return q

def mpq(x):
    x = sp.Rational(x)
    return mp.mpf(x.p) / x.q

def smoothstep(x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    a, b = np.exp(-1 / x), np.exp(-1 / (1 - x))
    return a / (a + b)

class Problem:
    def __init__(self, M, gam, e, gamH):
        self.par = {mu: 1, gU: gam, eU: e, gH: gamH}
        self.M = [m.subs(self.par) for m in M]
        self.num = [sp.lambdify((r, Zs, Hs), m, "numpy") for m in self.M]
        self.asym = self.infinity_series()
        self.hor = self.horizon_series()

    # infinity
    def infinity_series(self, N=60):
        Q = (self.M[0] * s * (s + 1) - self.M[1] * s * r + self.M[2] * r**2).subs({Zs: 1, Hs: 0})
        P = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                P[i][j] = taylor(Q[i, j].subs(r, 1 / rho), rho, N)
        self.P = P
        self.N = N
        P0 = sp.Matrix(3, 3, lambda i, j: P[i][j][0])
        det = sp.factor(P0.det())
        return det

    def Pk(self, k, sv, der=False):
        return mp.matrix([[self._ev(i, j, k, sv, der) for j in range(3)] for i in range(3)])

    def _ev(self, i, j, k, sv, der):
        key = (i, j, k, der)
        if not hasattr(self, "_cache"):
            self._cache = {}
        if key not in self._cache:
            p = sp.Poly(sp.diff(self.P[i][j][k], s) if der else self.P[i][j][k], s)
            self._cache[key] = [mpq(c) for c in p.all_coeffs()]
        return mp.polyval(self._cache[key], sv)

    def frob(self, s0, v0, resonant_at=None):
        """sum c_k rho^(s0+k) + log(rho) sum d_k rho^(s0+k); a log enters only at resonant_at"""
        N = self.N
        c = [v0] + [None] * N
        d = [mp.matrix(3, 1) for _ in range(N + 1)]
        alpha = mp.mpf(0)
        for k in range(1, N + 1):
            rhs = mp.matrix(3, 1)
            rhsd = mp.matrix(3, 1)
            for j in range(1, k + 1):
                rhs -= self.Pk(j, s0 + k - j) * c[k - j] + self.Pk(j, s0 + k - j, der=True) * d[k - j]
                rhsd -= self.Pk(j, s0 + k - j) * d[k - j]
            P0, P0d = self.Pk(0, s0 + k), self.Pk(0, s0 + k, der=True)
            if k == resonant_at:
                U_, S_, V_ = mp.svd_r(P0)
                assert S_[2] < mp.mpf(10)**-25 * S_[0]
                nvec, lvec = V_.T[:, 2], U_[:, 2]
                alpha = (lvec.T * rhs)[0] / (lvec.T * P0d * nvec)[0]
                d[k] = alpha * nvec
                rhs2 = rhs - P0d * d[k]
                c[k] = sum((V_.T[:, i] * ((U_[:, i].T * rhs2)[0] / S_[i]) for i in range(2)), mp.matrix(3, 1))
                assert mp.norm(P0 * c[k] - rhs2) < mp.mpf(10)**-25 * (1 + mp.norm(rhs2))
            else:
                d[k] = mp.lu_solve(P0, rhsd)
                c[k] = mp.lu_solve(P0, rhs - P0d * d[k])
        self.alpha_log = alpha
        return c, d

    def eval_inf(self, s0, cd, rv):
        """U and dU/dr at r = rv"""
        c, d = cd
        x = mp.mpf(1) / rv
        U = mp.matrix(3, 1)
        dU = mp.matrix(3, 1)
        L = mp.log(x)
        for k in range(self.N + 1):
            p = s0 + k
            U += c[k] * x**p + d[k] * (x**p * L)
            dU += c[k] * (p * x**(p - 1)) + d[k] * (p * x**(p - 1) * L + x**(p - 1))
        return U, -dU * x**2

    # horizon
    def horizon_series(self, N=60):
        x = sp.Symbol("x")
        Ms = [m.subs({Zs: 0, Hs: 1}).subs(r, 1 + x) for m in self.M]
        coef = []
        for m in Ms:
            ser = [[taylor(m[i, j], x, N + 1) for j in range(3)] for i in range(3)]
            coef.append([sp.Matrix(3, 3, lambda i, j: ser[i][j][k]) for k in range(N + 2)])
        self.hc = [[mp.matrix([[mpq(q) for q in row] for row in Mk.tolist()]) for Mk in cl] for cl in coef]
        m2, m1 = coef[0], coef[1]
        assert m2[0] == sp.zeros(3, 3)
        # R0(s) = s (m2_1 (s - 1) + m1_0): exponents 0 (three times) and 1 + eig(-m2_1^-1 m1_0)
        Am = -mp.inverse(self.hc[0][1]) * self.hc[1][0]
        ev = mp.eig(Am)[0]
        roots = [0j] * 3 + [complex(1 + q) for q in ev]
        self.hroots = roots
        self.Nh = N
        return roots

    def horizon_solutions(self, xv):
        """a basis of the solutions smooth at r = 1 (power series in x = r - 1), U and U' at x = xv. Where R(n) is
        singular (an exponent n among the positive integers), the solvability condition removes one combination of
        the basis and the null vector of R(n) starts a new one, so the count stays three."""
        N = self.Nh
        m2, m1, m0 = self.hc
        basis = []
        for i in range(3):
            c = [mp.matrix(3, 1) for _ in range(N + 1)]
            c[0][i] = 1
            basis.append(c)
        self.hres = []
        for n in range(1, N + 1):
            R = m2[1] * (n * (n - 1)) + m1[0] * n
            rhs = []
            for c in basis:
                rr = mp.matrix(3, 1)
                for k in range(0, n):
                    T = m2[n + 1 - k] * (k * (k - 1)) + m1[n - k] * k
                    if n - 1 - k >= 0:
                        T += m0[n - 1 - k]
                    rr -= T * c[k]
                rhs.append(rr)
            U_, S_, V_ = mp.svd_r(R)
            if S_[2] < mp.mpf(10)**-25 * S_[0]:
                self.hres.append(n)
                lv, nv = U_[:, 2], V_.T[:, 2]
                p = [(lv.T * rr)[0] for rr in rhs]
                piv = max(range(len(basis)), key=lambda i: abs(p[i]))
                assert abs(p[piv]) > mp.mpf(10)**-20
                nb, nr = [], []
                for i, (c, rr) in enumerate(zip(basis, rhs)):
                    if i == piv:
                        continue
                    t = p[i] / p[piv]
                    nb.append([ci - t * cp for ci, cp in zip(c, basis[piv])])
                    nr.append(rr - t * rhs[piv])
                for c, rr in zip(nb, nr):
                    c[n] = sum((V_.T[:, j] * ((U_[:, j].T * rr)[0] / S_[j]) for j in range(2)), mp.matrix(3, 1))
                    assert mp.norm(R * c[n] - rr) < mp.mpf(10)**-25 * (1 + mp.norm(rr))
                new = [mp.matrix(3, 1) for _ in range(N + 1)]
                new[n] = nv
                basis = nb + [new]
            else:
                for c, rr in zip(basis, rhs):
                    c[n] = mp.lu_solve(R, rr)
        sols = []
        for c in basis:
            U = sum((c[k] * mp.mpf(xv)**k for k in range(N + 1)), mp.matrix(3, 1))
            dU = sum((c[k] * (k * mp.mpf(xv)**(k - 1)) for k in range(1, N + 1)), mp.matrix(3, 1))
            sols.append((U, dU, c[N]))
        return sols

    def rhs_fun(self, zeta, eta):
        M2f, M1f, M0f = self.num

        def fun(rv, y):
            Z, H = zeta(rv), eta(rv)
            A2 = np.array(M2f(rv, Z, H), dtype=float)
            A1 = np.array(M1f(rv, Z, H), dtype=float)
            A0 = np.array(M0f(rv, Z, H), dtype=float)
            u, du = y[:3], y[3:]
            return np.concatenate([du, -np.linalg.solve(A2, A1 @ du + A0 @ u)])
        return fun

    def coefficient(self, zeta, eta, rm, r0=1.25, rtol=1e-13):
        if not hasattr(self, "_hs"):
            self._hs = {}
        if r0 not in self._hs:
            self._hs[r0] = self.horizon_solutions(r0 - 1)
        hs = self._hs[r0]
        fun = self.rhs_fun(zeta, eta)
        cols = []
        for U, dU, _ in hs:
            y0 = np.array([float(q) for q in U] + [float(q) for q in dU])
            sol = solve_ivp(fun, (r0, rm), y0, method="DOP853", rtol=rtol, atol=1e-15)
            cols.append(sol.y[:, -1])
        inf = [self.eval_inf(s0, cd, mp.mpf(rm)) for s0, cd in self.modes]
        vec = lambda UdU: np.array([float(q) for q in UdU[0]] + [float(q) for q in UdU[1]])
        Amat = np.column_stack(cols + [-vec(inf[k]) for k in (1, 2, 3)])
        sol = np.linalg.solve(Amat, vec(inf[0]))
        return sol[3], np.linalg.cond(Amat)

def null_vec(P0):
    U_, S_, V_ = mp.svd_r(P0)
    vv = V_.T[:, 2]
    k = max(range(3), key=lambda i: abs(vv[i]))
    return vv * (1 if vv[k] > 0 else -1) / mp.norm(vv)

def setup(M, gam, e, gamH):
    pb = Problem(M, gam, e, gamH)
    z = 4 * e * gam**2
    lam2 = (1 + mp.sqrt(17 + 2 * mp.mpf(z) - 2 * mp.sqrt(mp.mpf(z)**2 + 4 * mp.mpf(z) + 16))) / 2
    det = sp.Poly(pb.asym, s)
    rts = sorted(complex(x).real for x in det.nroots(n=40))
    lam3 = [x for x in rts if 3 < x < 4][0]
    lam3 = mp.findroot(lambda y: mp.polyval([mpq(c) for c in det.all_coeffs()], y), lam3)
    modes = []
    for s0, res in ((mp.mpf(0), 4), (lam2, None), (lam3, None), (mp.mpf(4), None)):
        P0 = pb.Pk(0, s0)
        v0 = mp.matrix([[0], [1], [1]]) if s0 == 0 else null_vec(P0)
        modes.append((s0, pb.frob(s0, v0, resonant_at=res)))
        if s0 == 0:
            alpha = pb.alpha_log
    pb.modes = modes
    return pb, lam2, lam3, rts, alpha

def record_point():
    """--record: A at the record's point gam_U = e_U = 1/100 (z = 4e-6), baseline cut-offs and four variations"""
    M, _, _ = derive()
    gam = e = sp.Rational(1, 100)
    pb, lam2, lam3, rts, alpha = setup(M, gam, e, sp.Rational(1, 10))
    print("  record's point: z = %s, d1 = %.6g, lambda_3 - 3 = %.6g, log coefficient %.4g"
          % (4 * e * gam**2, float(lam2 - 2), float(lam3 - 3), float(alpha)), flush=True)
    zeta0 = lambda x, a=1.5, b=2.5: smoothstep((x - a) / (b - a))
    eta0 = lambda x, a=1.3, b=1.8: 1 - smoothstep((x - a) / (b - a))
    v2 = pb.modes[1][1][0][0]
    Pv = float((v2.T * pb.modes[0][1][0][2])[0])
    print("  u_0's rho^2 coefficient: %s; its component along the unit vector of rho^(2+d1): %.10g"
          % ([mp.nstr(x, 8) for x in pb.modes[0][1][0][2]], Pv), flush=True)
    A3, c3 = pb.coefficient(zeta0, eta0, 3.0)
    A4, c4 = pb.coefficient(zeta0, eta0, 4.0)
    A3b, c3b = pb.coefficient(zeta0, eta0, 3.0, r0=1.15, rtol=1e-12)
    print("  A = %.10g (r = 3, condition %.2g), %.10g (r = 4, %.2g), %.10g (start 1.15, rtol 1e-12, %.2g); "
          "A + P_v = %.6g" % (A3, c3, A4, c4, A3b, c3b, A3 + Pv), flush=True)
    bump = lambda c, w: (lambda x: np.exp(1 - 1 / (1 - ((x - c) / w)**2)) if abs(x - c) < w else 0.0)
    rows = [("zeta on [1.5, 2.0]", lambda x: smoothstep((x - 1.5) / 0.5), eta0),
            ("zeta on [1.5, 2.75]", lambda x: smoothstep((x - 1.5) / 1.25), eta0),
            ("zeta0 + 20 bump on [1.6, 2.4]", lambda x, b_=bump(2.0, 0.4): zeta0(x) + 20 * b_(x), eta0),
            ("eta0 + 20 bump on [1.35, 1.75]", zeta0, lambda x, b_=bump(1.55, 0.2): eta0(x) + 20 * b_(x))]
    for lab, zf, ef in rows:
        Ar = pb.coefficient(zf, ef, 3.0)[0]
        print("      %-32s A = %+.10g, A + P_v = %+.6g" % (lab, Ar, Ar + Pv), flush=True)
    return 0


def zeros_scan():
    """--zeros: S7, whether some cut-off makes A vanish at the record's point"""
    from scipy.integrate import quad
    M, _, _ = derive()
    gam = e = sp.Rational(1, 100)
    pb = setup(M, gam, e, sp.Rational(1, 10))[0]
    v2 = pb.modes[1][1][0][0]
    Pv = float((v2.T * pb.modes[0][1][0][2])[0])
    zeta0 = lambda x: smoothstep((x - 1.5) / 1.0)
    eta0 = lambda x: 1 - smoothstep((x - 1.3) / 0.5)
    Acoef = lambda zf, ef: pb.coefficient(zf, ef, 3.0)[0]
    A0 = Acoef(zeta0, eta0)
    print("  record's point, baseline cut-offs: A = %.10g, P_v = %.10g" % (A0, Pv), flush=True)
    bump = lambda c, w: (lambda x: float(np.exp(1 - 1 / (1 - ((x - c) / w)**2))) if abs(x - c) < w else 0.0)
    w = 0.1
    norm = quad(bump(0.0, w), -w, w, epsabs=1e-14)[0]
    centres = [1.35 + 0.1 * k for k in range(16)]
    sens = {}
    for name in ("zeta", "eta"):
        rows = []
        for c in centres:
            b = bump(c, w)
            if name == "zeta":
                Ap = Acoef(lambda x: zeta0(x) + b(x), eta0); Am = Acoef(lambda x: zeta0(x) - b(x), eta0)
            else:
                Ap = Acoef(zeta0, lambda x: eta0(x) + b(x)); Am = Acoef(zeta0, lambda x: eta0(x) - b(x))
            rows.append(((Ap - Am) / (2 * norm), (Ap + Am - 2 * A0)))
        sens[name] = rows
        tot = sum(abs(s_) for s_, _ in rows) * 0.1
        print("  (a) dA/d%s(r) at r = 1.35 ... 2.85: %s" % (name, " ".join("%.2e" % s_ for s_, _ in rows)), flush=True)
        print("      curvature (A(+b) + A(-b) - 2 A0): largest %.1e; sum of |dA/d%s| dr = %.3e"
              % (max(abs(q) for _, q in rows), name, tot), flush=True)
    bound = sum(abs(s_) for s_, _ in sens["zeta"]) * 0.1 + sum(abs(s_) for s_, _ in sens["eta"]) * 0.1
    print("      first-order estimate of |A - A0| over cut-offs with |zeta - zeta0|, |eta - eta0| <= 1: %.3e"
          % bound, flush=True)
    z_early = lambda x: smoothstep((x - 1.26) / 0.2)
    z_late = lambda x: smoothstep((x - 2.75) / 0.2)
    e_short = lambda x: 1 - smoothstep((x - 1.26) / 0.1)
    e_long = lambda x: 1 - smoothstep((x - 2.75) / 0.2)
    ext = []
    for lab, zf, ef in (("zeta early, eta0", z_early, eta0), ("zeta late, eta0", z_late, eta0),
                        ("zeta0, eta short", zeta0, e_short), ("zeta0, eta long", zeta0, e_long),
                        ("zeta early, eta short", z_early, e_short), ("zeta early, eta long", z_early, e_long),
                        ("zeta late, eta short", z_late, e_short), ("zeta late, eta long", z_late, e_long)):
        Ax = Acoef(zf, ef)
        ext.append(Ax)
        print("  (b) %-24s A = %.10g (A - A0 = %+.3e)" % (lab, Ax, Ax - A0), flush=True)
    for name in ("zeta", "eta"):
        k = max(range(len(centres)), key=lambda i: abs(sens[name][i][0]))
        b = bump(centres[k], w)
        fns = lambda t: (((lambda x, t_=t: zeta0(x) + t_ * b(x)), eta0) if name == "zeta"
                         else (zeta0, (lambda x, t_=t: eta0(x) + t_ * b(x))))

        def A_rel(t):
            """A at matching radii 3 and 4, and whether they agree to 1e-7 relative with the condition below 1e12"""
            try:
                a3, c3 = pb.coefficient(*fns(t), 3.0)
                a4, c4 = pb.coefficient(*fns(t), 4.0)
            except Exception:                                           # noqa: BLE001
                return float("nan"), False, float("inf")
            good = np.isfinite(a3) and abs(a3 - a4) < 1e-7 * abs(a3) and max(c3, c4) < 1e12
            return a3, good, max(c3, c4)
        At = {t: A_rel(t) for t in (-1e5, -3e4, -1e4, -1e3, -1e2, -10, 10, 1e2, 1e3, 1e4, 3e4, 1e5)}
        ts = sorted(At)
        print("  (c) %s + t b (b at r = %.2f; * marks a value whose two matching radii disagree or whose condition is "
              "1e12 or more): %s" % (name, centres[k], "; ".join("t = %g: A = %.6g%s" % (t, At[t][0], "" if At[t][1]
                                                                  else "*") for t in ts)), flush=True)
        good = [t for t in ts if At[t][1]]
        print("      reliable over t in %s: A from %.6g to %.6g" % (good, min(At[t][0] for t in good),
                                                                  max(At[t][0] for t in good)), flush=True)
        for t1, t2 in zip(good[:-1], good[1:]):
            a1, a2 = At[t1][0], At[t2][0]
            if a1 * a2 < 0:
                lo, hi = t1, t2
                for _ in range(40):
                    mid = 0.5 * (lo + hi)
                    am = A_rel(mid)[0]
                    if am * a1 < 0:
                        hi = mid
                    else:
                        lo, a1 = mid, am
                print("      A changes sign between t = %g and %g: zero at t = %.6g" % (t1, t2, 0.5 * (lo + hi)),
                      flush=True)
    return 0


def zeros_far():
    """--zeros-far: S8, the sensitivities of A to zeta and eta on (3, 8) at the record's point"""
    from scipy.integrate import quad
    M, _, _ = derive()
    gam = e = sp.Rational(1, 100)
    pb = setup(M, gam, e, sp.Rational(1, 10))[0]
    zeta0 = lambda x: smoothstep((x - 1.5) / 1.0)
    eta0 = lambda x: 1 - smoothstep((x - 1.3) / 0.5)
    A3 = pb.coefficient(zeta0, eta0, 3.0)[0]
    A8, c8 = pb.coefficient(zeta0, eta0, 8.0)
    print("  record's point: A0 = %.10g matched at r = 3, %.10g at r = 8 (condition %.1e)" % (A3, A8, c8), flush=True)
    bump = lambda c, w: (lambda x: float(np.exp(1 - 1 / (1 - ((x - c) / w)**2))) if abs(x - c) < w else 0.0)
    w = 0.2
    norm = quad(bump(0.0, w), -w, w, epsabs=1e-14)[0]
    centres = [3.2 + 0.4 * k for k in range(12)]
    dens = {}
    for name in ("zeta", "eta"):
        rows = []
        for c in centres:
            b = bump(c, w)
            if name == "zeta":
                Ap = pb.coefficient(lambda x: zeta0(x) + b(x), eta0, 8.0)[0]
                Am = pb.coefficient(lambda x: zeta0(x) - b(x), eta0, 8.0)[0]
            else:
                Ap = pb.coefficient(zeta0, lambda x: eta0(x) + b(x), 8.0)[0]
                Am = pb.coefficient(zeta0, lambda x: eta0(x) - b(x), 8.0)[0]
            rows.append((Ap - Am) / (2 * norm))
        dens[name] = rows
        print("  dA/d%s(r) at r = 3.2 ... 7.6: %s" % (name, " ".join("%.3e" % q for q in rows)), flush=True)
    rr = np.array(centres); de = np.array(dens["eta"])
    p_fit = np.polyfit(np.log(rr), np.log(np.abs(de)), 1)
    print("  dA/deta ~ %.3g r^%.3f on (3, 8) (log-log fit), levelling off: c_H = -eta dr/2 carries no decay"
          % (math.exp(p_fit[1]), p_fit[0]), flush=True)
    inner = np.array(centres) < 5.0
    e5 = float(np.sum(np.abs(de[inner])) * 0.4)
    z8 = float(np.sum(np.abs(np.array(dens["zeta"]))) * 0.4)
    gaps = []                                  # the two intervals neither S7 nor S8 samples (verifier 199)
    for a_, b_ in ((1.25, 1.3), (2.9, 3.0)):
        c, wg = (a_ + b_) / 2, (b_ - a_) / 2
        bg = bump(c, wg)
        ng = quad(bump(0.0, wg), -wg, wg, epsabs=1e-14)[0]
        Ap = pb.coefficient(zeta0, lambda x: eta0(x) + bg(x), 8.0)[0]
        Am = pb.coefficient(zeta0, lambda x: eta0(x) - bg(x), 8.0)[0]
        gaps.append(abs(Ap - Am) / (2 * ng) * (b_ - a_))
    s7 = 0.0837                                # S7's eta-only sum on (1.3, 2.9) (--zeros, (a))
    print("  first-order estimates: eta within 1 of eta0 on (3, 5) moves A by %.3f; on the gaps (1.25, 1.3) and "
          "(2.9, 3) by %.4f and %.4f; so on (1.25, 5R_1) = (1.25, 5) (R_1 = sqrt(mu_end) = 1 here, the record's "
          "chi supported in |x| < 5 R_1) by about %.3f with S7's eta-only %.4f on (1.3, 2.9); zeta within 1 on "
          "(3, 8) by %.1e (dA/dzeta falls only like r^-0.9, so on (3, R) this grows like log R)"
          % (e5, gaps[0], gaps[1], s7 + sum(gaps) + e5, s7, z8), flush=True)
    return 0


def coefficient_qr(pb, zeta, eta, rm, grid, r0=1.25, rtol=1e-12):
    """A by the same matching as Problem.coefficient, with the horizon columns re-orthonormalised (QR) at every grid
    point: A is the coefficient of an infinity column, so it depends on the horizon columns only through their span,
    and the QR keeps that span resolved where one solution outgrows the others (D472)"""
    if not hasattr(pb, "_hs"):
        pb._hs = {}
    if r0 not in pb._hs:
        pb._hs[r0] = pb.horizon_solutions(r0 - 1)
    fun = pb.rhs_fun(zeta, eta)
    Y = np.column_stack([np.array([float(q) for q in U] + [float(q) for q in dU]) for U, dU, _ in pb._hs[r0]])
    Y = np.linalg.qr(Y)[0]
    for a, b in zip(grid[:-1], grid[1:]):
        cols = [solve_ivp(fun, (a, b), Y[:, j], method="DOP853", rtol=rtol, atol=1e-15).y[:, -1] for j in range(3)]
        Y = np.linalg.qr(np.column_stack(cols))[0]
    inf = [pb.eval_inf(s0, cd, mp.mpf(rm)) for s0, cd in pb.modes]
    vec = lambda UdU: np.array([float(q) for q in UdU[0]] + [float(q) for q in UdU[1]])
    Amat = np.column_stack([Y[:, j] for j in range(3)] + [-vec(inf[k]) for k in (1, 2, 3)])
    return np.linalg.solve(Amat, vec(inf[0]))[3], np.linalg.cond(Amat)


def qr_grid(r0, rm, c, w, t, h=0.05, scale=1.0):
    """chunks of h, and of 1/(0.05 |t| + 1) across the bump [c - w, c + w], where c_H's growth rate is about |t|/20"""
    hf = min(h, 1.0 / (abs(t) * 0.05 + 1.0)) * scale
    pts = (list(np.arange(r0, c - w, h * scale)) + list(np.arange(c - w, c + w, hf)) +
           list(np.arange(c + w, rm, h * scale)) + [rm])
    return np.array(sorted(set(round(float(q), 12) for q in pts)))


def A_qr(pb, zf, ef, c, w, t, r1, r2):
    """A by coefficient_qr at matching radius r1 and at r2 with half the chunks: value, agreement to 1e-7, condition"""
    a1, c1 = coefficient_qr(pb, zf, ef, r1, qr_grid(1.25, r1, c, w, t))
    a2, c2 = coefficient_qr(pb, zf, ef, r2, qr_grid(1.25, r2, c, w, t, scale=0.5))
    return a1, bool(np.isfinite(a1) and abs(a1 - a2) < 1e-7 * abs(a1) and max(c1, c2) < 1e12), max(c1, c2)


def zeros_far_amp():
    """--zeros-far-amp: S9, A beyond first order for cut-off variations in (3, 8) at the record's point"""
    M, _, _ = derive()
    gam = e = sp.Rational(1, 100)
    pb = setup(M, gam, e, sp.Rational(1, 10))[0]
    zeta0 = lambda x: smoothstep((x - 1.5) / 1.0)
    eta0 = lambda x: 1 - smoothstep((x - 1.3) / 0.5)

    def A_rel(zf, ef):
        """A at matching radii 8 and 10, and whether they agree to 1e-7 relative with the condition below 1e12"""
        try:
            a8, c8 = pb.coefficient(zf, ef, 8.0)
            a10, c10 = pb.coefficient(zf, ef, 10.0)
        except Exception:                                               # noqa: BLE001
            return float("nan"), False, float("inf")
        good = bool(np.isfinite(a8) and abs(a8 - a10) < 1e-7 * abs(a8) and max(c8, c10) < 1e12)
        return a8, good, max(c8, c10)
    A0, g0, c0 = A_rel(zeta0, eta0)
    print("  record's point: A0 = %.10g (radii 8 and 10 agree: %s; condition %.1e)" % (A0, g0, c0), flush=True)
    e_long = lambda x: 1 - smoothstep((x - 4.75) / 0.2)           # eta off as late as the record's support allows
    z_late = lambda x: smoothstep((x - 7.5) / 0.3)                 # zeta on as late as the matching allows
    z_mid = lambda x: smoothstep((x - 4.5) / 0.3)
    ext = {}
    for lab, zf, ef in (("eta off on [4.75, 4.95]", zeta0, e_long), ("zeta on [4.5, 4.8]", z_mid, eta0),
                        ("zeta on [7.5, 7.8]", z_late, eta0), ("both, zeta on [7.5, 7.8]", z_late, e_long)):
        ext[lab] = A_rel(zf, ef)
        print("  (a) %-28s A = %.10g (A - A0 = %+.4g; reliable: %s)" % (lab, ext[lab][0], ext[lab][0] - A0,
                                                                         ext[lab][1]), flush=True)
    bump = lambda c, w: (lambda x: float(np.exp(1 - 1 / (1 - ((x - c) / w)**2))) if abs(x - c) < w else 0.0)
    ts = (-1e5, -3e4, -1e4, -3e3, -1e3, -1e2, -10, -1, 1, 10, 1e2, 1e3, 3e3, 1e4, 3e4, 1e5)
    scans = {}
    for name, c in (("eta", 4.8), ("zeta", 3.2)):
        b = bump(c, 0.2)
        fns = lambda t_: (((lambda x: zeta0(x) + t_ * b(x)), eta0) if name == "zeta"
                          else (zeta0, (lambda x: eta0(x) + t_ * b(x))))
        At = {t_: A_rel(*fns(t_)) for t_ in ts}
        qr = {t_: A_qr(pb, *fns(t_), c, 0.2, t_, 8.0, 10.0) for t_ in ts if not At[t_][1]}
        scans[name] = At
        print("  (b) %s + t b (b of half-width 0.2 at r = %.1f; * marks a value whose radii disagree or whose condition "
              "is 1e12 or more): %s" % (name, c, "; ".join("t = %g: %.6g%s" % (t_, At[t_][0], "" if At[t_][1] else "*")
                                                           for t_ in ts)), flush=True)
        if qr:
            print("      QR matching where those fail (radii 8 and 10, the second with half the chunks): %s"
                  % "; ".join("t = %g: %.10g%s" % (t_, v[0], "" if v[1] else "*") for t_, v in sorted(qr.items())),
                  flush=True)
            At.update(qr)
        good = [t_ for t_ in ts if At[t_][1]]
        lin = [(At[t_][0] - A0) / t_ for t_ in good if abs(t_) <= 10]
        print("      reliable over %d of %d amplitudes: A from %.6g to %.6g; (A - A0)/t at |t| <= 10 from %.4g to %.4g"
              % (len(good), len(ts), min(At[t_][0] for t_ in good), max(At[t_][0] for t_ in good), min(lin), max(lin)),
              flush=True)
        for t1, t2 in zip(good[:-1], good[1:]):
            if At[t1][0] * At[t2][0] < 0:
                print("      A changes sign between t = %g and %g" % (t1, t2), flush=True)
    val = [(t_, A_qr(pb, zeta0, (lambda x, t_=t_: eta0(x) + t_ * bump(4.8, 0.2)(x)), 4.8, 0.2, t_, 8.0, 10.0)[0],
            A_rel(zeta0, (lambda x, t_=t_: eta0(x) + t_ * bump(4.8, 0.2)(x)))[0]) for t_ in (0.0, -100.0)]
    qr_ok = all(abs(a - b_) < 1e-8 * abs(b_) for _, a, b_ in val)
    print("  (c) QR against plain matching where both are reliable: %s"
          % "; ".join("t = %g: %.12g against %.12g" % v for v in val), flush=True)
    Acoef3 = lambda zf, ef: pb.coefficient(zf, ef, 3.0)[0]
    centres = [1.35 + 0.1 * k for k in range(16)]
    sens = [(Acoef3(zeta0, lambda x, c=c: eta0(x) + bump(c, 0.1)(x))
             - Acoef3(zeta0, lambda x, c=c: eta0(x) - bump(c, 0.1)(x))) for c in centres]
    cn = centres[max(range(16), key=lambda i: abs(sens[i]))]
    bn = bump(cn, 0.1)
    near = {}
    for t_ in (-1e3, -3e3, -1e4, -3e4, -1e5):
        near[t_] = A_qr(pb, zeta0, (lambda x, t_=t_: eta0(x) + t_ * bn(x)), cn, 0.1, t_, 3.0, 4.0)
    print("  (d) S7's undecided range, eta + t b with b of half-width 0.1 at r = %.2f (S7's most sensitive), by QR "
          "matching at radii 3 and 4: %s" % (cn, "; ".join("t = %g: %.10g%s" % (t_, v[0], "" if v[1] else "*")
                                                         for t_, v in sorted(near.items()))), flush=True)
    ok = g0 and all(v[1] for v in ext.values()) and qr_ok and all(v[1] for v in near.values()) \
        and all(v[1] for At in scans.values() for v in At.values())
    allA = ([v[0] for v in ext.values()] + [v[0] for At in scans.values() for v in At.values() if v[1]] +
            [v[0] for v in near.values() if v[1]])
    print("  S9: every value reliable: %s; least A over (a), (b) and (d): %.6g; a sign change: %s"
          % (ok, min(allA), "yes" if min(allA) <= 0 else "none"), flush=True)
    return 0 if ok else 1


def zeros_near():
    """--zeros-near: S10, cut-off variations inside r = 1.25, between the horizon series and S7's range"""
    from scipy.integrate import quad
    M, _, _ = derive()
    gam = e = sp.Rational(1, 100)
    pb = setup(M, gam, e, sp.Rational(1, 10))[0]
    zeta0 = lambda x: smoothstep((x - 1.5) / 1.0)
    eta0 = lambda x: 1 - smoothstep((x - 1.3) / 0.5)
    r0 = 1.05
    A125 = pb.coefficient(zeta0, eta0, 3.0)[0]
    A105, c105 = pb.coefficient(zeta0, eta0, 3.0, r0=r0)
    A105b = pb.coefficient(zeta0, eta0, 4.0, r0=r0)[0]
    base_ok = abs(A105 - A125) < 1e-7 * abs(A125) and abs(A105b - A105) < 1e-7 * abs(A105)
    print("  record's point: A0 = %.10g started at r = 1.25, %.10g at r = %.2f (matched at 3; %.10g at 4; condition "
          "%.1e)" % (A125, A105, r0, A105b, c105), flush=True)
    bump = lambda c, w: (lambda x: float(np.exp(1 - 1 / (1 - ((x - c) / w)**2))) if abs(x - c) < w else 0.0)
    w = 0.025
    norm = quad(bump(0.0, w), -w, w, epsabs=1e-14)[0]
    centres = [1.075, 1.125, 1.175, 1.225]
    sens = {}
    for name in ("zeta", "eta"):
        rows = []
        for c in centres:
            b = bump(c, w)
            if name == "zeta":
                Ap = pb.coefficient(lambda x: zeta0(x) + b(x), eta0, 3.0, r0=r0)[0]
                Am = pb.coefficient(lambda x: zeta0(x) - b(x), eta0, 3.0, r0=r0)[0]
            else:
                Ap = pb.coefficient(zeta0, lambda x: eta0(x) + b(x), 3.0, r0=r0)[0]
                Am = pb.coefficient(zeta0, lambda x: eta0(x) - b(x), 3.0, r0=r0)[0]
            rows.append((Ap - Am) / (2 * norm))
        sens[name] = rows
        print("  (a) dA/d%s(r) at r = %s: %s; first-order sum over (1.05, 1.25): %.3g"
              % (name, ", ".join("%.3f" % c for c in centres), " ".join("%.3e" % q for q in rows),
                 sum(abs(q) for q in rows) * 2 * w), flush=True)
    ts = (-1e5, -1e4, -1e3, -1e2, -10, -1, 1, 10, 1e2, 1e3, 1e4, 1e5)
    near = {}
    for name in ("zeta", "eta"):
        k = max(range(len(centres)), key=lambda i: abs(sens[name][i]))
        c = centres[k]
        b = bump(c, w)
        fns = lambda t_: (((lambda x: zeta0(x) + t_ * b(x)), eta0) if name == "zeta"
                          else (zeta0, (lambda x: eta0(x) + t_ * b(x))))
        At = {}
        for t_ in ts:
            try:
                a3, c3 = pb.coefficient(*fns(t_), 3.0, r0=r0)
                a4, c4 = pb.coefficient(*fns(t_), 4.0, r0=r0)
                good = bool(np.isfinite(a3) and abs(a3 - a4) < 1e-7 * abs(a3) and max(c3, c4) < 1e12)
            except Exception:                                           # noqa: BLE001
                a3, good = float("nan"), False
            if not good:
                a1, cq1 = coefficient_qr(pb, *fns(t_), 3.0, qr_grid(r0, 3.0, c, w, t_), r0=r0)
                a2, cq2 = coefficient_qr(pb, *fns(t_), 4.0, qr_grid(r0, 4.0, c, w, t_, scale=0.5), r0=r0)
                good = bool(np.isfinite(a1) and abs(a1 - a2) < 1e-7 * abs(a1) and max(cq1, cq2) < 1e12)
                a3 = a1
            At[t_] = (a3, good)
        near[name] = At
        print("  (b) %s + t b (b of half-width %.3f at r = %.3f; QR matching where the plain one fails; "
              "* unreliable): %s"
              % (name, w, c, "; ".join("t = %g: %.6g%s" % (t_, v[0], "" if v[1] else "*") for t_, v in At.items())),
              flush=True)
    vals = [v for At in near.values() for v in At.values()]
    ok = base_ok and all(g for _, g in vals)
    print("  S10: baseline consistent: %s; every value reliable: %s; least A: %.6g; a sign change: %s"
          % (base_ok, all(g for _, g in vals), min(a for a, _ in vals), "yes" if min(a for a, _ in vals) <= 0
             else "none"), flush=True)
    return 0 if ok else 1


def main():
    if sys.argv[1:2] == ["--zeros-far"]:
        return zeros_far()
    if sys.argv[1:2] == ["--zeros-far-amp"]:
        return zeros_far_amp()
    if sys.argv[1:2] == ["--zeros-near"]:
        return zeros_near()
    if sys.argv[1:2] == ["--record"]:
        return record_point()
    if sys.argv[1:2] == ["--zeros"]:
        return zeros_scan()
    ok = {}
    M, lin_ok, ang_ok = derive()
    ok["S1 form"] = lin_ok and ang_ok
    ok["S1 static"] = check_static(M)
    print("  S1: ODEs linear and chi-independent, theta/phi components zero: %s; static coordinates reproduce "
          "genstates5.boxU: %s" % (ok["S1 form"], ok["S1 static"]), flush=True)
    res = {}
    for gam, e in ((sp.Rational(1, 2), sp.Rational(1, 2)), (sp.Rational(1, 4), sp.Rational(1, 2)),
                   (sp.Rational(1, 2), sp.Rational(1, 8))):
        z = 4 * e * gam**2
        key = "z=%s (gam_U %s, e_U %s)" % (z, gam, e)
        pb, lam2, lam3, rts, alpha = setup(M, gam, e, sp.Rational(1, 10))
        q = sp.cancel(pb.asym / (s * (s - 4)))
        is_poly = sp.fraction(sp.together(q))[1].free_symbols == set()
        lam2_root = abs(mp.polyval([mpq(c) for c in sp.Poly(q, s).all_coeffs()], lam2)) < mp.mpf(10)**-30
        ok["S2 %s" % key] = is_poly and lam2_root
        print("  S2 (z = %s): det = s(s - 4) q(s): %s; lambda_s1,2 = %s (d1 = %.6g) a root of q: %s; roots %s; "
              "log coefficient at the 0, 4 resonance %.4g" % (z, is_poly, mp.nstr(lam2, 12), float(lam2 - 2),
                                                              lam2_root, ", ".join("%.6g" % x for x in rts),
                                                              float(alpha)), flush=True)
        hr = pb.hroots
        n0 = sum(1 for x in hr if abs(x) < 1e-12)
        hs = pb.horizon_solutions(mp.mpf(1) / 4)
        tail = max(float(mp.norm(cN)) for _, _, cN in hs) * 0.25**pb.Nh
        ok["S3 %s" % key] = n0 >= 3 and len(hs) == 3 and pb.hres == [1] and tail < 1e-20
        print("  S3: horizon exponents %s; resonance at n = %s handled, three smooth solutions, last series term at "
              "x = 1/4: %.1e" % (", ".join("%.6g%+.3gi" % (x.real, x.imag) for x in hr), pb.hres, tail), flush=True)
        zeta0 = lambda x, a=1.5, b=2.5: smoothstep((x - a) / (b - a))
        eta0 = lambda x, a=1.3, b=1.8: 1 - smoothstep((x - a) / (b - a))
        A3, cnd = pb.coefficient(zeta0, eta0, 3.0)
        A4, _ = pb.coefficient(zeta0, eta0, 4.0)
        A3b, _ = pb.coefficient(zeta0, eta0, 3.0, r0=1.15, rtol=1e-12)
        ok["S4 %s" % key] = abs(A3 - A4) < 1e-7 * max(1, abs(A3)) and abs(A3 - A3b) < 1e-7 * max(1, abs(A3))
        print("  S4: A = %.10g (match at r = 3), %.10g (r = 4), %.10g (start 1.15, rtol 1e-12); condition %.2g"
              % (A3, A4, A3b, cnd), flush=True)
        rows = []
        for b in (2.0, 2.25, 2.5, 2.75):
            rows.append(("zeta on [1.5, %.2f]" % b, pb.coefficient(lambda x, b=b: smoothstep((x - 1.5) / (b - 1.5)),
                                                                   eta0, 3.0)[0]))
        for b in (1.6, 1.8, 2.0):
            rows.append(("eta off on [1.3, %.1f]" % b, pb.coefficient(zeta0, lambda x, b=b: 1 - smoothstep(
                (x - 1.3) / (b - 1.3)), 3.0)[0]))
        def bump(c, w):
            return lambda x: np.exp(1 - 1 / (1 - ((x - c) / w)**2)) if abs(x - c) < w else 0.0
        fams = [("zeta0 + eps bump on [1.6, 2.4]", lambda ep, b_=bump(2.0, 0.4): (lambda x: zeta0(x) + ep * b_(x), eta0),
                 (-100.0, -50.0, -20.0, -10.0, -5.0, 0.0, 5.0, 10.0, 20.0, 50.0, 100.0)),
                ("zeta0 + eps bump on [2.55, 2.95]", lambda ep, b_=bump(2.75, 0.2): (lambda x: zeta0(x) + ep * b_(x),
                                                                                    eta0), (-20.0, 20.0)),
                ("eta0 + eps bump on [1.35, 1.75]",
                 lambda ep, b_=bump(1.55, 0.2): (zeta0, lambda x: eta0(x) + ep * b_(x)),
                 (-20.0, 20.0))]
        signs = []
        for lab, mk, epss in fams:
            vals = []
            for ep in epss:
                zf, ef = mk(ep)
                vals.append(pb.coefficient(zf, ef, 3.0)[0])
                rows.append(("%s, eps = %g" % (lab, ep), vals[-1]))
            for i in range(len(vals) - 1):
                if vals[i] * vals[i + 1] < 0:
                    lo, hi, flo = epss[i], epss[i + 1], vals[i]
                    for _ in range(25):
                        mid = (lo + hi) / 2
                        fm = pb.coefficient(*mk(mid), 3.0)[0]
                        if fm * flo > 0:
                            lo, flo = mid, fm
                        else:
                            hi = mid
                    signs.append((lab, (lo + hi) / 2))
        for lab, val in rows:
            print("      %-50s A = %+.10g" % (lab, val))
        spread = max(val for _, val in rows) - min(val for _, val in rows)
        print("      spread of A over these cut-offs %.4g; A = 0 found: %s" % (
            spread, ", ".join("%s at eps = %.6g" % sg for sg in signs) if signs else "no, in none of these families"))
        ok["S5 %s" % key] = spread > 1e4 * max(abs(A3 - A4), abs(A3 - A3b), 1e-12)
        res[(gam, e)] = (A3, spread, signs)
    print("  at z = 1/8: A = %.8g with (gam_U, e_U) = (1/4, 1/2) and %.8g with (1/2, 1/8)"
          % (res[(sp.Rational(1, 4), sp.Rational(1, 2))][0], res[(sp.Rational(1, 2), sp.Rational(1, 8))][0]))
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    return 0 if all(ok.values()) else 1

if __name__ == "__main__":
    sys.exit(main())
