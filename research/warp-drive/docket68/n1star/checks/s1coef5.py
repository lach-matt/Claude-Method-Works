#!/usr/bin/env python3
"""s1coef5: the rho^(2 + d1) coefficient of the s1 state, from the horizon (LOSS-D LD9, D442).

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

Parameters: mu = 1, gam_H = 1/10, and (gam_U, e_U) = (1/2, 1/2) (z = 1/2, d1 = 0.0375), (1/4, 1/2) and (1/2, 1/8)
(both z = 1/8, d1 = 0.0101). Series at 40 digits (60 terms); the ODE between r = 1.25 and the matching radius in double
precision (DOP853, rtol 1e-13). About 15 minutes.
Not computed: the record's point (z = 4 x 10^-6, where d1 is near 3 x 10^-7 and the terms rho^2 and rho^(2+d1) are nearly
parallel); whether these gam_U, e_U, gam_H meet III.D' Proposition 4.1's eps_0, eps_1; whether some zeta makes A vanish;
the dual state; and whether the record's later steps hold at the bumped cut-offs, beyond the matching being solvable
there.
"""
import os
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

def main():
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
