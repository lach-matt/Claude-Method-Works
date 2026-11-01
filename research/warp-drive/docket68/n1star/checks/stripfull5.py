#!/usr/bin/env python3
"""stripfull5.py -- BEYOND5 3(b) (D487): the strip for the record's full flat operator.

A source supported on a strip of bounded v along N, of Cartesian size r^-4 (the sources from g_lambda - g_app, D464),
under the record's full flat operator L = D Ric + dstar_(E^C) delta_(E^Ups) G at its point (coulombL5.POINT, gamma_C
= 10^6), harmonic by harmonic. At radius r the strip occupies s = v/r in [0, d/r], so for the degree -3 profile
h = r^-3 F(s) it is a delta at N: with r^(wt + 1) L h = M2 F'' + M1 F' + M0 F (harmonics5's reduction at degree -3,
M2 = (s - s^2/2) I) and the source sigma d delta(s), integrating (s F')' + (M1(0) - I) F' = sigma d delta over the
strip, with F = 0 on N, gives F(0+) = (M1(0) - I)^-1 sigma d (distributionally: F = H(s) F_reg and s delta' = -delta; the
delta is the strip's leading term in d), and beyond it the solution is the regular one (exponent 0) with that value,
which needs every eigenvalue of M1(0) to have real part > 1 (else a logarithm, or no solution). So the strip enters at
rho^3 with coefficient K sigma d, K = T_3 (M1(0) - I)^-1, T_3 the degree -3 transfer F(0) -> F(1) (s = 1 is I_0), and the
r^-2 coefficient at I_0 is not touched. The width corrections are analytic in d (D491, after verifier 208): the operator
is invariant under t -> t + c, so a sheet at v = v0 gives r^-3 F(1 - v0/r) at t = 0, and over a uniform strip r^3 h(I_0)
= d K sigma + (d^2/r) K4 sigma + O(d^3/r^2), K4 = -(1/2) T_3' (M1(0) - I)^-1, T_3' the transfer F(0) -> F'(1): rho^4,
rho^5, ..., integer powers. This is for a source r^-4 sigma(v) with sigma independent of r; a source only bounded by r^-4
is not covered, the kernel having no sign.

  P1 (exact) the scalar model (strip5.py's box phi = S): at degree -3, M1(0) = 5/2, F(0+) = -d/3, and the regular
     solution is 2F1(3 + l, 1 - l; 5/2; s/2), so by Gauss's second summation theorem F(1) = -pi/(4 Gamma(1 - l/2)
     Gamma(2 + l/2)) = C_l, verifier 202's coefficient (D481) and strip5's T5; checked here through the same series
     transfer as P3, to 10^-25, for l = 0 ... 6; and the rho^4 coefficient K4 = -(1/2) F'(1), from (ab/2c) 2F1(a +
     1, b + 1; c + 1; 1/2), 1/2, 0, -1/6, 0, 1/10, ... (strip5's rho^4 at l = 2 and 4, D474).
  P2 (exact) the degree -p reduction of the full operator, scalar and vector types: at p = 2 it is harmonics5's (S1,
     S2); at p = 3, M2 = (s - s^2/2) I, the coefficients are polynomials in s, and M1(0) is M1(0) at p = 2 plus I.
  P3 (computed, series at 30 digits, 400 against 600 terms) for l = 0 ... LMAX, scalar and vector types, at gamma_C
     = 10^6 and 10^5: the eigenvalues of M1(0) at p = 3 (every real part > 1), the norm of K in each harmonic's
     normalised basis (harmonics5's weights), and its convergence; the same for K4 (D491).

Measured (D487, corrected D491): P1 to 1.2e-30; at degree -3 the eigenvalues of M1(0) are 2.5, 2.51, 2.52 and the
damping's 1.5e6, 3e6 at every 2 <= l <= 12 (at l = 0 and 1 the least is 2.5099), scalar and vector types; the normalised
norm of K is 1.97 to 2.99 (scalar) and 0.17 to 1.14 (vector), the series at 400 and 600 terms agreeing to 30 digits; K at
gamma_C = 10^5 differs by up to 6.5e-2 (scalar, l = 12); K4, normalised, 1.70 to 3.31 (scalar) and 0.063 to 0.58
(vector), nonzero at every harmonic.

Labels: P1, P2 exact; P3 computed (K4 too). The tensor type, where the damping drops out (harmonics5 S3), is not
reduced here.
"""
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp

_argv, sys.argv = sys.argv, sys.argv[:1]
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import harmonics5 as H  # noqa: E402
import coulombL5 as C  # noqa: E402
import genstates5 as GS  # noqa: E402
sys.argv = _argv

t, r, ch, th = GS.t, GS.r, GS.ch, GS.th
S, gC = C.S, C.gC
kap, lam, y0, y1 = H.kap, H.lam, H.y0, H.y1
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12


def reduce_scalar_p(p):
    """harmonics5.reduce_scalar with every component of h multiplied by r^(2 - p): h = r^-p (Cartesian weight)"""
    G = GS.geo(4, True)
    X, g, gi, Gam, f_ = G
    N = 5
    w = r**(2 - p)
    sx = (t + r)/r
    a, b, c, d, e, f, k = H.FS
    Y = sp.Function("Y")(ch)
    dY = sp.diff(Y, ch)
    h = sp.zeros(N)
    h[0, 0], h[1, 1] = w*Y*a(sx)/r**2, w*Y*c(sx)/r**2
    h[0, 1] = h[1, 0] = w*Y*b(sx)/r**2
    for i in (2, 3, 4):
        h[i, i] = w*g[i, i]*Y*d(sx)/r**2
    Hcc = sp.diff(Y, ch, 2) + kap*Y/3
    Htt = sp.sin(ch)*sp.cos(ch)*dY + kap*Y*sp.sin(ch)**2/3
    h[2, 2] += w*k(sx)*Hcc
    h[3, 3] += w*k(sx)*Htt
    h[4, 4] += w*k(sx)*Htt*sp.sin(th)**2
    h[0, 2] = h[2, 0] = w*dY*e(sx)/r
    h[1, 2] = h[2, 1] = w*dY*f(sx)/r
    L, _ = H.full_L(h, G)
    rule = H.ode_rules(Y, -2*sp.cot(ch)*y1 - kap*y0)
    R = {(i, j): rule(L[i, j]) for i in range(N) for j in range(i, N)}
    out, checks = {}, []
    q = p - 2
    for (i, j), wt in (((0, 0), 4), ((0, 1), 4), ((1, 1), 4)):
        c0, c1 = H.coeffs(R[(i, j)]*r**(wt + q))
        checks.append(c1 == 0)
        out[(i, j)] = c0
    for (i, j), name in (((0, 2), "e"), ((1, 2), "f")):
        c0, c1 = H.coeffs(R[(i, j)]*r**(3 + q))
        checks.append(c0 == 0)
        out[name] = c1
    t0, t1 = H.coeffs(R[(3, 3)]*r**(2 + q)/sp.sin(ch)**2)
    B = H.simp_lin(t1*sp.sin(ch)/sp.cos(ch))
    A = H.simp_lin(t0 - kap*B/3)
    x0, x1 = H.coeffs(R[(2, 2)]*r**(2 + q))
    checks.append(H.simp_lin(x0 - (A - 2*kap*B/3)) == 0)
    checks.append(H.simp_lin(x1 + 2*B*sp.cos(ch)/sp.sin(ch)) == 0)
    checks.append(H.simp_lin(R[(4, 4)] - sp.sin(th)**2*R[(3, 3)]) == 0)
    for (i, j) in ((0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)):
        checks.append(H.simp_lin(R[(i, j)]) == 0)
    eqs = [out[(0, 0)], out[(0, 1)], out[(1, 1)], A, out["e"], out["f"], B]
    eqs = [H.to_s(qq) for qq in eqs]
    free = all(qq.free_symbols <= {S, C.gU, C.eU, gC, C.eC, C.vC, kap} for qq in eqs)
    return eqs, all(checks) and free


def reduce_vector_p(p):
    U, second, ok_div, ok_kill = H.vector_ode()
    G = GS.geo(4, True)
    X, g, gi, Gam, f_ = G
    N = 5
    w = r**(2 - p)
    sx = (t + r)/r
    pp, qq, k = H.FV
    dU = sp.diff(U, ch)
    h = sp.zeros(N)
    h[0, 4] = h[4, 0] = w*pp(sx)*U*sp.sin(th)**2/r
    h[1, 4] = h[4, 1] = w*qq(sx)*U*sp.sin(th)**2/r
    h[2, 4] = h[4, 2] = w*k(sx)*(dU - 2*sp.cot(ch)*U)*sp.sin(th)**2
    L, _ = H.full_L(h, G)
    rule = H.ode_rules(U, second.subs({sp.diff(U, ch): y1, U: y0}))
    R = {(i, j): rule(L[i, j]) for i in range(N) for j in range(i, N)}
    checks = [ok_div, ok_kill]
    eqs = []
    q = p - 2
    for (i, j), wt in (((0, 4), 3), ((1, 4), 3)):
        c0, c1 = H.coeffs(R[(i, j)]*r**(wt + q)/sp.sin(th)**2)
        checks.append(c1 == 0)
        eqs.append(c0)
    c0, c1 = H.coeffs(R[(2, 4)]*r**(2 + q)/sp.sin(th)**2)
    checks.append(H.simp_lin(c0 + 2*sp.cos(ch)/sp.sin(ch)*c1) == 0)
    eqs.append(c1)
    for (i, j) in ((0, 0), (0, 1), (1, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (3, 3), (4, 4), (2, 3), (3, 4)):
        checks.append(H.simp_lin(R[(i, j)]) == 0)
    eqs = [H.to_s(e) for e in eqs]
    free = all(e.free_symbols <= {S, C.gU, C.eU, gC, C.eC, C.vC, lam} for e in eqs)
    return eqs, all(checks) and free


def scalar_model(p):
    """-(1/2) r^(p + 2) box phi for phi = r^-p F(s) on 4+1 Minkowski at harmonic l, in s"""
    F = sp.Function("F")
    ls = sp.Symbol("l")
    phi = r**(-p)*F((t + r)/r)
    box = -sp.diff(phi, t, 2) + sp.diff(phi, r, 2) + 3/r*sp.diff(phi, r) - ls*(ls + 2)*phi/r**2
    e = H.to_s(sp.expand(-sp.Rational(1, 2)*box*r**(p + 2)))
    M, rest = H.matrices_n([e], [F])
    return M, rest, ls


def kmap(M, sub, nterms):
    """K = T_3 (M1(0) - I)^-1 and K4 = -(1/2) T_3' (M1(0) - I)^-1 at 30 digits, and the eigenvalues of M1(0)"""
    n = M[0].shape[0]
    m10 = sp.Matrix(M[1].subs(S, 0).subs(sub))
    T, last, Td = H.series_transfer_n(M, sub, nterms, nder=1)
    mp.mp.dps = 30
    A = mp.matrix([[mp.mpf(sp.Rational(m10[i, j]).p)/sp.Rational(m10[i, j]).q - (1 if i == j else 0)
                    for j in range(n)] for i in range(n)])
    Ai = mp.inverse(A)
    K, K4 = T*Ai, -Td[1]*Ai/2
    ev = np.linalg.eigvals(np.array(m10.evalf(), dtype=float))
    return K, K4, ev, float(last)


def k4_exact(l):
    """-(1/2) F'(1) for the scalar model's F = -(1/3) 2F1(3 + l, 1 - l; 5/2; s/2)"""
    a, b, c = 3 + l, 1 - l, mp.mpf(5)/2
    if b == 0:
        return mp.mpf(0)
    if b + 1 <= 0:                      # terminates (b + 1 = 2 - l)
        g = mp.fsum(mp.rf(a + 1, j)*mp.rf(b + 1, j)/(mp.rf(c + 1, j)*mp.factorial(j))/2**j for j in range(l - 1))
    else:
        g = mp.hyp2f1(a + 1, b + 1, c + 1, mp.mpf(1)/2)
    return -(-mp.mpf(1)/3*a*b/(2*c)*g)/2


def rng(out, k):
    """'scalar lo to hi, vector lo to hi' for entry k of P3's rows"""
    return ", ".join("%s %.4g to %.4g" % (ty, min(q[k] for q in out if q[1] == ty), max(q[k] for q in out if q[1] == ty))
                     for ty in ("scalar", "vector"))


def main():
    t0 = time.time()
    ok = {}
    # P1 the scalar model
    M, rest, ls = scalar_model(3)
    okm = rest == [0] and sp.expand(M[0][0, 0] - (S - S**2/2)) == 0 and \
        sp.expand(M[1][0, 0].subs(S, 0)) == sp.Rational(5, 2)
    worst = worst4 = 0
    rows, rows4 = [], []
    for l in range(0, 7):
        K, K4, ev, _ = kmap(M, {ls: l}, 400)
        F1 = K[0, 0]*mp.mpf(-0.5)
        F4 = K4[0, 0]*mp.mpf(-0.5)
        worst4 = max(worst4, float(abs(F4 - k4_exact(l))))
        rows4.append("%d: %s" % (l, mp.nstr(F4, 10)))
        Cl = -mp.pi/(4*mp.gamma(1 - mp.mpf(l)/2)*mp.gamma(2 + mp.mpf(l)/2)) if l % 2 or l == 0 else mp.mpf(0)
        if l == 0:
            g = mp.hyp2f1(3, 1, mp.mpf(5)/2, mp.mpf(1)/2)*(-mp.mpf(1)/3)
        else:                           # b = 1 - l <= 0: the series terminates (and is exactly 0 at even l)
            g = -mp.fsum(mp.rf(3 + l, j)*mp.rf(1 - l, j)/(mp.rf(mp.mpf(5)/2, j)*mp.factorial(j))*mp.mpf(1)/2**j
                         for j in range(l))/3
        worst = max(worst, float(abs(F1 - Cl)), float(abs(g - Cl)))
        rows.append("%d: %s" % (l, mp.nstr(F1, 12)))
    ok["P1"] = okm and worst < 1e-25 and worst4 < 1e-25
    print("  P1 %s: scalar model at degree -3: M2 = s - s^2/2, M1(0) = 5/2: %s; F(1) = T (M1(0) - 1)^-1 (-1/2) against "
          "C_l = -pi/(4 Gamma(1 - l/2) Gamma(2 + l/2)) and -(1/3) 2F1(3 + l, 1 - l; 5/2; 1/2), l = 0 ... 6: max "
          "difference %.1e; F(1) = %s; rho^4: K4 against -(1/2) F'(1) exact, max difference %.1e, K4 = %s"
          % ("PASS" if ok["P1"] else "FAIL", okm, worst, ", ".join(rows), worst4, ", ".join(rows4)), flush=True)
    # P2 the reductions
    red = {}
    for p in (2, 3):
        es, oks = reduce_scalar_p(p)
        ev_, okv = reduce_vector_p(p)
        Ms, rs = H.matrices_n(es, H.FS)
        Mv, rv = H.matrices_n(ev_, H.FV)
        red[p] = (Ms, Mv, oks and okv and all(x == 0 for x in rs + rv))
        print("    degree -%d reduced (%.0f s)" % (p, time.time() - t0), flush=True)
    es2, _, _ = H.reduce_scalar()
    ev2, _, _ = H.reduce_vector()
    Ms2, _ = H.matrices_n(es2, H.FS)
    Mv2, _ = H.matrices_n(ev2, H.FV)
    same = all(sp.expand(red[2][0][o] - Ms2[o]) == sp.zeros(7) for o in range(3)) and \
        all(sp.expand(red[2][1][o] - Mv2[o]) == sp.zeros(3) for o in range(3))
    Ms3, Mv3 = red[3][0], red[3][1]
    m2 = S - S**2/2
    okm2 = sp.expand(Ms3[0] - m2*sp.eye(7)) == sp.zeros(7) and sp.expand(Mv3[0] - m2*sp.eye(3)) == sp.zeros(3)
    poly = all(X[i, j].is_polynomial(S) for X in (Ms3[1], Ms3[2]) for i in range(7) for j in range(7)) and \
        all(X[i, j].is_polynomial(S) for X in (Mv3[1], Mv3[2]) for i in range(3) for j in range(3))
    shift = sp.expand(Ms3[1].subs(S, 0) - red[2][0][1].subs(S, 0) - sp.eye(7)) == sp.zeros(7) and \
        sp.expand(Mv3[1].subs(S, 0) - red[2][1][1].subs(S, 0) - sp.eye(3)) == sp.zeros(3)
    ok["P2"] = red[2][2] and red[3][2] and same and okm2 and poly and shift
    print("  P2 %s: sectors close at degrees -2 and -3: %s, %s; degree -2 = harmonics5's S1 and S2: %s; at degree -3 "
          "M2 = (s - s^2/2) I: %s, polynomial: %s, M1(0) = M1(0) at degree -2 plus I: %s"
          % ("PASS" if ok["P2"] else "FAIL", red[2][2], red[3][2], same, okm2, poly, shift), flush=True)
    # P3 the full operator at degree -3
    good, out = True, []
    for l in range(0, LMAX + 1):
        cases = [("scalar", Ms3, 4 if l == 0 else (6 if l == 1 else 7), {kap: l*(l + 2)})]
        if l >= 1:
            cases.append(("vector", Mv3, 2 if l == 1 else 3, {lam: l*(l + 2) - 1}))
        for typ, Mx, n, par in cases:
            Ml = [sp.Matrix(n, n, lambda i, j: Mx[o][i, j].subs(par)) for o in range(3)]
            res = {}
            for gc in (10**6, 10**5):
                sub = dict(C.POINT)
                sub[gC] = gc
                res[gc] = (kmap(Ml, sub, 400), kmap(Ml, sub, 600) if gc == 10**6 else None)
            (Ka, Q4, ev, _), (K6, Q6, _, last) = res[10**6]
            K5 = res[10**5][0][0]
            Wt = H.weights(typ, max(l, 1), n) if l else np.diag([1, 2**0.5, 1, 3**0.5])
            A6 = np.array([[float(K6[i, j]) for j in range(n)] for i in range(n)])
            A4 = np.array([[float(Ka[i, j]) for j in range(n)] for i in range(n)])
            B6 = np.array([[float(Q6[i, j]) for j in range(n)] for i in range(n)])
            B4 = np.array([[float(Q4[i, j]) for j in range(n)] for i in range(n)])
            A5 = np.array([[float(K5[i, j]) for j in range(n)] for i in range(n)])
            nrm = float(np.linalg.norm(Wt @ A6 @ np.linalg.inv(Wt), 2))
            nrm4 = float(np.linalg.norm(Wt @ B6 @ np.linalg.inv(Wt), 2))
            d46 = float(max(np.max(np.abs(A6 - A4)), np.max(np.abs(B6 - B4))))
            dg = float(np.max(np.abs(A6 - A5)))
            mre = float(min(ev.real))
            good &= mre > 1 and d46 < 1e-12 and np.isfinite(nrm) and np.isfinite(nrm4)
            out.append((l, typ, n, nrm, d46, dg, mre, sorted(ev.real), nrm4))
            print("    l = %2d %s (%d): least Re eig M1(0) = %.6g (eigenvalues %s); ||K|| normalised = %.6g, ||K4|| "
                  "%.6g; series 400 vs 600 %.1e (last term %.1e); |K(1e6) - K(1e5)| = %.2e"
                  % (l, typ, n, mre, ", ".join("%.4g" % x for x in sorted(ev.real)), nrm, nrm4, d46, last, dg),
                  flush=True)
    ok["P3"] = good
    print("  P3 %s: every harmonic l <= %d of scalar and vector type: M1(0) at degree -3 has every eigenvalue's "
          "real part > 1 (least %.6g), K finite (largest normalised norm %.6g, at l = %d %s); normalised ||K|| %s; "
          "||K4|| %s" % ("PASS" if good else "FAIL", LMAX, min(q[6] for q in out), max(q[3] for q in out),
                         max(out, key=lambda q: q[3])[0], max(out, key=lambda q: q[3])[1],
                         rng(out, 3), rng(out, 8)),
          flush=True)
    print("  %s (%.0f s)" % ("all pass" if all(ok.values()) else "FAILED", time.time() - t0))
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
