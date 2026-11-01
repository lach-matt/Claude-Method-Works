#!/usr/bin/env python3
"""sources5: the quadratic sources of static r^-2 means are r^-6 (BEYOND5 section 3(b), D413's condition, D447).

BEYOND5's list of what Lemma 6.5's carrying to I_0 does not give includes the condition on the sources between N and S:
an r^(-q) source contributes at rho^(q - 2), so the r^-2 coefficient at I_0 needs them o(r^-4), and "after the shell the
leading means are static, so their products are probably r^-6, but this is not checked". After the shell the means'
leading terms r^-2 M_m(x^) are static (M_m = 2 int S_(m,3) dv' stops changing when S_(m,3) does).

Here, on 4 + 1 Minkowski in Cartesian coordinates (t, x1..x4), for h = r^-2 H(x^) static with H a symmetric matrix of
homogeneous functions of degree 0 (random rational combinations of 1, x1/r, x3/r, x1 x2/r^2, x4^2/r^2), the part of the
record's operator P(g, eta) = Ric(g) - delta*_(eta, E_C) Upsilon^(E_Ups)(g, eta) (III.B Definition 6.1, (6.3)-(6.4); E_C
and E_Ups built on c = r^-1 dt) quadratic in h is computed at a point p and at 2p from the jets of h there (50 digits;
the e^2 coefficient by a degree-16 polynomial fit, exact as the inverse metric is truncated at e^2 and every component is
then a polynomial in e of lower degree). E^Ups G (g - eta) is linear in h, so the quadratic part comes from Ric and from
Upsilon^0(g, eta) = g g^-1 Gamma(g) alone, then through delta*_(eta,E_C), which is linear and built on eta and c.

  Q1 (omputed) Ric's quadratic part at 2p is 2^-6 times its value at p, in every component;
  Q2 (omputed) so is delta*_(eta,E_C) applied to Upsilon^0's quadratic part, its E_C term (c homogeneous of degree -1)
      included;
  Q3 (omputed) control: the linear part of Ric at 2p is 2^-4 times its value at p, and a non-static h (sin t added to
      H_tt) breaks Q1.

Deduced: every term of P quadratic in a static h homogeneous of degree -2 has derivative order plus c-order two, so it is
homogeneous of degree -6 on Minkowski, and higher orders of degree -8 or less (D449); on Tangherlini (g0 - eta = O(mu
r^-2) with derivatives) the corrections are of degree -8 or less. So the products of the leading means are O(r^-6),
o(r^-4) as the condition needs. Not computed: the cross terms with the means' remainder in E_(5/2), which need that
class's derivative bounds (if each derivative gains r^-1 they are O(r^(-13/2))), and the sources from g_lambda - g_app.

Run: python3 checks/sources5.py   (about 90 s; the jets by sympy, the rest at 50 digits)
"""
import random
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 50

X = sp.symbols("t x1 x2 x3 x4", real=True)
t, xs = X[0], X[1:]
r = sp.sqrt(sum(x**2 for x in xs))
eta = sp.diag(-1, 1, 1, 1, 1)
eps = sp.Symbol("eps")
gU, eU, gC, eC, vC = sp.Rational(1, 3), sp.Rational(2, 7), sp.Rational(5, 4), sp.Rational(1, 6), mp.mpf(3) / 5


def random_h(rng, static=True):
    basis = [sp.Integer(1), xs[0] / r, xs[2] / r, xs[0] * xs[1] / r**2, xs[3]**2 / r**2]
    H = sp.zeros(5, 5)
    for a in range(5):
        for b in range(a, 5):
            e = sum(sp.Rational(rng.randint(-4, 4), 3) * f for f in basis)
            if not static and (a, b) == (0, 0):
                e += sp.sin(t)
            H[a, b] = H[b, a] = e
    return H / r**2


def jets(h, pt):
    """h_ab, d_c h_ab, d_c d_d h_ab at the point, at 50 digits"""
    f = lambda e: mp.mpf(str(sp.N(e.subs(pt), 60)))
    H0 = [[f(h[a, b]) for b in range(5)] for a in range(5)]
    H1 = [[[f(sp.diff(h[a, b], X[c])) for c in range(5)] for b in range(5)] for a in range(5)]
    H2 = [[[[f(sp.diff(h[a, b], X[c], X[d])) for d in range(5)] for c in range(5)] for b in range(5)] for a in range(5)]
    return H0, H1, H2, f(1 / r), [f(x) for x in xs]


def operator_at(J, e):
    """Ric(eta + e h) and delta*_(eta,E_C) Upsilon^0(eta + e h, eta) at the point, the inverse metric truncated at e^2
    (exact for the coefficients up to e^2)"""
    H0, H1, H2, cr, xv = J
    I5 = range(5)
    et = [[(-1 if a == b == 0 else (1 if a == b else 0)) for b in I5] for a in I5]
    g = [[et[a][b] + e * H0[a][b] for b in I5] for a in I5]
    hs = [[sum(et[a][c] * H0[c][d] * et[d][b] for c in I5 for d in I5) for b in I5] for a in I5]
    hh = [[sum(hs[a][c] * H0[c][d] * et[d][b] for c in I5 for d in I5) for b in I5] for a in I5]
    gi = [[et[a][b] - e * hs[a][b] + e**2 * hh[a][b] for b in I5] for a in I5]
    d1 = [[[e * H1[a][b][c] for c in I5] for b in I5] for a in I5]
    d2 = [[[[e * H2[a][b][c][d] for d in I5] for c in I5] for b in I5] for a in I5]
    dgi = [[[-sum(gi[a][i] * d1[i][k][c] * gi[k][b] for i in I5 for k in I5) for b in I5] for a in I5] for c in I5]
    cr_ = [[[d1[b][d][a] + d1[a][d][b] - d1[a][b][d] for d in I5] for b in I5] for a in I5]
    G = [[[sum(gi[c][d] * cr_[a][b][d] for d in I5) / 2 for b in I5] for a in I5] for c in I5]
    dG = [[[[(sum(dgi[ee][c][d] * cr_[a][b][d] for d in I5)
              + sum(gi[c][d] * (d2[b][d][a][ee] + d2[a][d][b][ee] - d2[a][b][d][ee]) for d in I5)) / 2
             for b in I5] for a in I5] for c in I5] for ee in I5]
    Ric = [[sum(dG[c][c][a][b] - dG[b][c][a][c] for c in I5)
            + sum(G[c][c][k] * G[k][a][b] - G[c][b][k] * G[k][a][c] for c in I5 for k in I5) for b in I5] for a in I5]
    gG = [sum(gi[a][b] * G[c][a][b] for a in I5 for b in I5) for c in I5]
    dgG = [[sum(dgi[ee][a][b] * G[c][a][b] + gi[a][b] * dG[ee][c][a][b] for a in I5 for b in I5) for c in I5]
           for ee in I5]
    U = [sum(g[m][c] * gG[c] for c in I5) for m in I5]
    dU = [[sum(d1[m][c][ee] * gG[c] + g[m][c] * dgG[ee][c] for c in I5) for m in I5] for ee in I5]
    cc = [cr] + [-vC * x * cr**2 for x in xv]
    cs = [sum(et[a][b] * cc[b] for b in I5) for a in I5]
    cU = sum(cs[a] * U[a] for a in I5)
    D = [[(dU[a][b] + dU[b][a]) / 2 + gC * (cc[a] * U[b] + cc[b] * U[a] - mp.mpf(2) / 3 * (1 - eC) * et[a][b] * cU)
          for b in I5] for a in I5]
    return Ric, D


def coefficients(J, k, deg=16):
    """the e^k Taylor coefficient of every component, from a polynomial fit at deg + 1 points"""
    es = [mp.mpf(j) / 4 for j in range(1, deg + 2)]
    vals = [operator_at(J, e) for e in es]
    V = mp.matrix([[e**i for i in range(deg + 1)] for e in es])
    Vi = mp.inverse(V)
    out = []
    for which in (0, 1):
        M = [[sum(Vi[k, j] * vals[j][which][a][b] for j in range(deg + 1)) for b in range(5)] for a in range(5)]
        out.append(M)
    return out


def main():
    rng = random.Random(7)
    ok = {}
    p = {t: sp.Rational(1, 3), xs[0]: sp.Rational(2, 5), xs[1]: sp.Rational(-1, 2), xs[2]: sp.Rational(3, 7),
         xs[3]: sp.Rational(1, 4)}
    p2 = {k: 2 * v for k, v in p.items()}
    h = random_h(rng)
    J1, J2 = jets(h, p), jets(h, p2)
    R1, D1 = coefficients(J1, 2)
    R2, D2 = coefficients(J2, 2)
    comps = [(a, b) for a in range(5) for b in range(a, 5)]
    tol = mp.mpf(10)**-30

    def ratio_ok(A, B, pw):
        big = max(abs(A[a][b]) for a, b in comps)
        return big > mp.mpf(10)**-10 and all(abs(B[a][b] - A[a][b] / 2**pw) < tol * (1 + abs(A[a][b])) for a, b in comps)
    ok["Q1"] = ratio_ok(R1, R2, 6)
    ok["Q2"] = ratio_ok(D1, D2, 6)
    print("  Q1 Ric's quadratic part at 2p is 2^-6 times its value at p (all 15 components, 30 digits): %s; largest %s"
          % (ok["Q1"], mp.nstr(max(abs(R1[a][b]) for a, b in comps), 5)), flush=True)
    print("  Q2 delta*_(eta,E_C) Upsilon^0's quadratic part likewise: %s; largest %s"
          % (ok["Q2"], mp.nstr(max(abs(D1[a][b]) for a, b in comps), 5)), flush=True)
    L1, _ = coefficients(J1, 1)
    L2, _ = coefficients(J2, 1)
    lin = ratio_ok(L1, L2, 4)
    hn = random_h(random.Random(7), static=False)
    N1, _ = coefficients(jets(hn, p), 2)
    N2, _ = coefficients(jets(hn, p2), 2)
    broken = not ratio_ok(N1, N2, 6)
    ok["Q3"] = lin and broken
    print("  Q3 controls: the linear part scales as 2^-4: %s; with sin t added to H_tt the 2^-6 scaling fails: %s"
          % (lin, broken))
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
