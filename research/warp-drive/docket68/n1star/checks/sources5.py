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

  Q1 (computed) Ric's quadratic part at 2p is 2^-6 times its value at p, in every component;
  Q2 (computed) so is delta*_(eta,E_C) applied to Upsilon^0's quadratic part, its E_C term (c homogeneous of degree -1)
      included;
  Q3 (computed) control: the linear part of Ric at 2p is 2^-4 times its value at p, and a non-static h (sin t added to
      H_tt) breaks Q1.
  Q4 (computed) the cross terms with a remainder: for rho = r^-5/2 G(x^) (G as H, so every derivative gains r^-1) the
      part of P bilinear in (h, rho) at 2p is 2^-13/2 times its value at p, in every component of both operators;
  Q5 (computed) rho in E_(5/2) as the record defines the class (N1STAR-PROOF.md, the classes before Lemma 9.7: every
      Cartesian derivative and every rotation derivative Omega bounded by C r^-5/2, so tangential derivatives gain r^-1
      and radial and time derivatives need not; D456), rho = r^-5/2 G(x^) sin(r + t), which Omega leaves as r^-5/2 (Omega
      G) sin(r + t): over radii 8 to 128, at 8 directions each, R^(9/2) times the largest bilinear (h, rho) component has
      a fitted exponent within 0.2 of zero, so it falls like r^-9/2 and not like r^-5 (which D454's factor-5 test could
      not exclude), against Q4's R^-2; and R^5 times the largest component quadratic in rho likewise.

Deduced: every term of P quadratic in a static h homogeneous of degree -2 has derivative order plus c-order two, so it is
homogeneous of degree -6 on Minkowski, and higher orders of degree -8 or less (D449); on Tangherlini (g0 - eta = O(mu
r^-2) with derivatives) the corrections are of degree -8 or less. So the products of the leading means are O(r^-6),
o(r^-4) as the condition needs. The cross terms with the means' remainder in E_(5/2) (D454, corrected D456): every term
of P quadratic in g - eta has two derivatives (or a factor c, of degree -1, per derivative missing) shared between its
two factors, so with h's derivatives gaining r^-1, and rho's tangential ones too but its radial and time ones not, the
largest is h d_r^2 rho, O(r^(-2 - 5/2)) = O(r^(-9/2)) (Q5), the others O(r^(-11/2)) or less, and the terms quadratic in
rho O(r^-5); with a gaining rho they would be O(r^(-13/2)) (Q4). Both are o(r^-4), the first with a margin of only
r^(-1/2): by D413's rule an r^(-9/2) source contributes at rho^(5/2), a half-integer power, which bears on BEYOND5 3(b)
(v)'s open question whether half-integer exponents occur. Not computed: the sources from g_lambda - g_app.

Run: python3 checks/sources5.py   (a few minutes; the jets by sympy, the rest at 50 digits)
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


def jet_fn(h):
    """h's jets as a function of the point (the derivatives taken once, then evaluated at 50 digits)"""
    syms = list(X)
    ex = [h[a, b] for a in range(5) for b in range(5)]
    d1 = [sp.diff(h[a, b], X[c]) for a in range(5) for b in range(5) for c in range(5)]
    d2 = [sp.diff(h[a, b], X[c], X[d]) for a in range(5) for b in range(5) for c in range(5) for d in range(5)]
    f = sp.lambdify(syms, ex + d1 + d2 + [1 / r], "mpmath")

    def at(ptv):
        vals = f(*ptv)
        I5 = range(5)
        H0 = [[vals[5 * a + b] for b in I5] for a in I5]
        H1 = [[[vals[25 + 25 * a + 5 * b + c] for c in I5] for b in I5] for a in I5]
        H2 = [[[[vals[150 + 125 * a + 25 * b + 5 * c + d] for d in I5] for c in I5] for b in I5] for a in I5]
        return H0, H1, H2, vals[-1], list(ptv[1:])
    return at


def combine(Ja, Jb, ea, eb):
    """the jets of ea h_a + eb h_b"""
    lin = lambda A, B: [lin(a, b) for a, b in zip(A, B)] if isinstance(A, list) else ea * A + eb * B
    return lin(Ja[0], Jb[0]), lin(Ja[1], Jb[1]), lin(Ja[2], Jb[2]), Ja[3], Ja[4]


def bilinear(Ja, Jb, eps=mp.mpf(10)**-16):
    """the parts of Ric and of delta*_(eta,E_C) Upsilon^0 bilinear in (h_a, h_b) and quadratic in h_b, by symmetric
    differences in the two amplitudes (error O(eps^2) relative; operator_at is exact to second order)"""
    P = {s: operator_at(combine(Ja, Jb, s[0] * eps, s[1] * eps), 1) for s in ((1, 1), (1, -1), (-1, 1), (-1, -1),
                                                                              (0, 1), (0, -1))}
    out = []
    for w in (0, 1):
        cross = [[(P[(1, 1)][w][a][b] - P[(1, -1)][w][a][b] - P[(-1, 1)][w][a][b] + P[(-1, -1)][w][a][b]) / (4 * eps**2)
                  for b in range(5)] for a in range(5)]
        quad = [[(P[(0, 1)][w][a][b] + P[(0, -1)][w][a][b]) / (2 * eps**2) for b in range(5)] for a in range(5)]
        out.append((cross, quad))
    return out


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
    # Q4-Q5: a remainder rho beside the static h
    hf = jet_fn(h)
    G = random_h(random.Random(11)) * r**2 / r**sp.Rational(5, 2)
    gf = jet_fn(G)
    osc = jet_fn(G * sp.sin(r + t))
    mpq = lambda q: mp.mpf(q.p) / q.q
    pt = [mpq(p[k]) for k in X]; pt2 = [mpq(p2[k]) for k in X]
    B1, B2 = bilinear(hf(pt), gf(pt)), bilinear(hf(pt2), gf(pt2))
    ok["Q4"] = all(ratio_ok(B1[w][0], B2[w][0], mp.mpf(13) / 2) for w in (0, 1))
    print("  Q4 a remainder whose derivatives gain: the (h, rho) parts of both operators scale as 2^-13/2 at 2p: %s"
          % ok["Q4"], flush=True)
    rr = random.Random(5)
    dirs = []
    for _ in range(8):
        q = [rr.gauss(0, 1) for _ in range(4)]
        nq = sum(z * z for z in q)**0.5
        dirs.append([z / nq for z in q])
    Cx, Cq, Ch = [], [], []
    radii = (8, 16, 32, 64, 128)
    for R in radii:
        bx = bq = bh = mp.mpf(0)
        for k, dv in enumerate(dirs):
            ptv = [mp.mpf(k) / 3] + [R * mp.mpf(z) for z in dv]
            Bo, Bg = bilinear(hf(ptv), osc(ptv)), bilinear(hf(ptv), gf(ptv))
            bx = max(bx, max(abs(Bo[w][0][a][b]) for w in (0, 1) for a, b in comps))
            bq = max(bq, max(abs(Bo[w][1][a][b]) for w in (0, 1) for a, b in comps))
            bh = max(bh, max(abs(Bg[w][0][a][b]) for w in (0, 1) for a, b in comps))
        Cx.append(bx * R**mp.mpf(4.5)); Cq.append(bq * R**5); Ch.append(bh * R**mp.mpf(4.5))
        print("    R = %3d: R^(9/2) max |(h, rho) part| %s; R^5 max |(rho, rho) part| %s; gaining rho: R^(9/2) %s"
              % (R, mp.nstr(Cx[-1], 4), mp.nstr(Cq[-1], 4), mp.nstr(Ch[-1], 4)), flush=True)
    ex_x = mp.log(Cx[-1] / Cx[0]) / mp.log(16); ex_q = mp.log(Cq[-1] / Cq[0]) / mp.log(16)
    print("    fitted exponents over R = 8 to 128: R^(9/2) max |(h, rho)| %s, R^5 max |(rho, rho)| %s (r^-5 would give "
          "-0.5 for the first)" % (mp.nstr(ex_x, 3), mp.nstr(ex_q, 3)), flush=True)
    bounded = abs(ex_x) < 0.2 and abs(ex_q) < 0.2 and max(Cx) / min(Cx) < 5 and max(Cq) / min(Cq) < 5
    control = Ch[-1] / Ch[0] < mp.mpf(1) / 100
    ok["Q5"] = bounded and control
    print("  Q5 a remainder in E_(5/2), its radial derivatives not gaining: the (h, rho) part is O(r^-9/2) and "
          "attains it, the (rho, rho) part O(r^-5): %s; control, the gaining remainder falls a further %s from R = 8 "
          "to 128: %s"
          % (bounded, mp.nstr(Ch[-1] / Ch[0], 3), control))
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
