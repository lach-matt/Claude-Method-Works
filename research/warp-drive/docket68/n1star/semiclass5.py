#!/usr/bin/env python3
"""semiclass5.py -- the semiclassical inputs of [Hin26a]'s constraint damping in five dimensions: its fibrewise theory
(section 3) and its symbol calculations on Minkowski space (Lemmas 4.1-4.4), recomputed on 4+1 Minkowski, and the
indicial admissibility of damping5.py's certificate point (N1STAR-PROOF.md section 10.13; ROUTES-OPEN.md
4.14; D55).  Labels: computed (exact, sympy; the e_0 of W4 numerical), READ.

[Hin26a] (arXiv:2606.27658v2) proves mode stability and zero energy invertibility of box^C = 2 delta_g G_g (delta*_g +
C_h), C_h omega = h^-1 (2 c (x)_s omega - (1 - e) g iota_{c#} omega), by semiclassical estimates in h whose inputs are
fibrewise linear algebra (section 3, stated for "dim M = 4") and the symbols of the zero section transport operator at
the critical sets of -r^2 c# on Minkowski space (section 4.1-4.2), and by the indicial roots (section 4.3, Theorem
4.9; damping5.py).  In five dimensions the trace weight is 2/(D - 2) (damping5.py U2), after which G C has his form
2 c (x)_s omega - e g <c, omega> and L = 4ih delta(c (x)_s .) + 2ihe d iota_{c#}, his (3.2), in any dimension.

  W1 (computed, exact) The fibrewise theory carries.  In a frame with c = (c_0, 0, ...), for generic zeta, B = g^-1 -
     (1 + e) G(c)^-1 c# (x) c# makes l(zeta) self-adjoint (Lemma 3.3) and is positive definite for e > 0; the
     characteristic polynomial of l(zeta)/2 is (lam - G(c) zeta_0)^(n-1) times the quadratic with trace (3 - e) G(c)
     zeta_0 and determinant (2 - e) G(c)^2 zeta_0^2 + e G(c) G(zeta'), his (3.8) with the multiplicity n - 1 for 2:
     so Lemmas 3.5-3.8, which use only this, hold verbatim at n = 4.  Control: the effective e (3e - 1)/2 < 0 -- the
     weight 1 at n = 4, the weight 3/2 at n = 3 -- where B is indefinite.
  W2 (computed, exact) The subprincipal symbol S = (L - L*)/(2ih), from the definition in Cartesian coordinates
     (adjoint with |dg| and B), not from Lemma 3.9's formula.  Four-dimensional control: his (4.6) for every e, and
     at the interior saddle his Lemma 4.4's a_00, a_10, a_11, a_22 and his e = 0 determinant 2 v^2 (3 - 2x^2); his
     printed a_01 is the computed one times e, which his own determinant refutes (at e = 0 it would give 2 v^2 (1 -
     x^2)(3 + 2x^2)): a misprint, x sqrt(e) for x/sqrt(e).  Control: the adjoint taken with g^-1 for B.
  W3 (computed, exact) Lemmas 4.1-4.2 in five dimensions.  At the saddle dK+ the eigenvalues of r^2 (-l(dw/w) + S)/2 at
     e = 0 are v (1 + b_K - b_sf), 2v (1 + b_K - b_sf) and v (2 + b_K - b_sf) (3x), at the sink R_v (b_K = 0) v (1 -
     b_sf), 2v (1 - b_sf) and v (2 - b_sf) (3x): positive iff b_K > b_sf - 1 and b_sf < 1, where his are b_K > b_sf -
     1/2 and b_sf < 1/2 -- the thresholds -(n - 2)/2 and (n - 2)/2 at n = 3 and 4.  Deduced, his section 5 being open in
     five dimensions: with b_K = a_K, b_sf = a_sf + 1 (his p. 39), his (5.14), a_sf < -1/2 and a_K > a_sf + 1/2, would
     read a_sf < 0 and a_K > a_sf.  Four-dimensional control: his (4.7) and Lemma 4.2.  Control: his thresholds claimed
     at n = 4.
  W4 (computed, exact; e_0 numerical) Lemma 4.4 in five dimensions.  At e = 0 the interior saddle's S is his: a_22 = v,
     trace 5v, determinant 2 v^2 (3 - 2x^2), positive on |x| <= 6/5 < (3/2)^(1/2); at v = 1/2 and damping5.py's e =
     1/102400 it is positive definite on [-6/5, 6/5] (Sturm, exact).  The largest admissible e (grid of 1201 points in
     x, bisection) is e_0 ~ 0.000069 v^2 in five dimensions and ~ 0.000154 v^2 in four (his ~ 0.000152 v^2).  Control: e
     = 1/40000, above e_0 at v = 1/2, where positivity fails.
  W5 (computed, exact) Lemma 4.3 is dimension-free: its proof is Lemma 3.8's condition, 2(1 - e) w/(e (1 - w)) >= 2 >
     1 = G(+-dr) for e <= w = v^2 (r - r_0)^2/r_0^2 < 1, which involves no dimension (w < 1 on his range [r_0/2, 2 r_0];
     beyond r_0 (1 + 1/v) c is not timelike); checked exactly at n = 4, ell(+-dr) negative definite at the edge
     points r = r_0 (1 +- sqrt(e)/v) and at r_0/2, 2 r_0.  Control: inside, at r = r_0 (1 + sqrt(e)/(2v)), where it is
     not.
  W6 (computed, exact) The two points.  damping5.py's certificate point (1/2, 1/102400, 10^-6) has W4's admissible e and
     h < e; the point of section 10.12's first version, e = 1/100, is not admissible: S fails positivity on |x| <=
     6/5 there, so that point was an indicial statement only.  Control: e = 1/100 claimed admissible.

READ (alphaXiv, 2026-10-21).  [Hin26a] pp. 1-3 (Theorem 1.1), 7, 9-10 (section 1.2.2), 25-28 (section 3: Definition
3.1, Lemmas 3.2-3.9, Remark 3.4, Corollary 3.6), 28-33 (section 4.1-4.2: (4.1)-(4.9), Lemmas 4.1-4.4), 38-41
(Proposition 5.1 and its proof), 43, 53, 66-68 (Definition 6.1, Theorem 6.2 and its proof), 96.  [Hin26] pp. 26,
120-121 (Lemmas 6.10-6.11, Proposition 6.12), 134-137 (section 7.1, (7.3)-(7.8), Theorem 7.1 and its proof), 144-145.

sympy, mpmath.  python3 semiclass5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import mpmath as mpm
import sympy as sp

import damping5 as DMP
from damping5 import Checklist

v, s = sp.symbols("v s", positive=True)          # s = sqrt(e)
xr = sp.Symbol("x", real=True)
R, T = sp.symbols("R T", positive=True)
bs, bk = sp.symbols("b_sf b_K", real=True)
rk = sp.Symbol("rho_K", positive=True)


def eta_(n):
    return sp.diag(-1, *([1] * n))


def ell(n, c, zeta, e):
    """l(zeta) w = 2 (<c, zeta> w + <zeta, w> c - e <w, c> zeta) as a matrix on covectors ([Hin26a] (3.3))."""
    et = eta_(n)
    ip = lambda a, b: (a.T * et * b)[0]                                                     # noqa: E731
    cols = []
    for k in range(n + 1):
        w = sp.zeros(n + 1, 1)
        w[k] = 1
        cols.append(2 * (ip(c, zeta) * w + ip(zeta, w) * c - e * ip(w, c) * zeta))
    return sp.Matrix.hstack(*cols)


def B_of(n, c, e):
    et = eta_(n)
    cu = et * c
    return et - (1 + e) / (c.T * et * c)[0] * (cu * cu.T)


def S_matrix(n, cfun, e, point, adjoint_B=True):
    """S = A + A^* for A = L/(2ih) = 2 delta(c (x)_s .) + e d iota_{c#} on Minkowski^{n+1}, Cartesian coordinates, with
    (A w)_a = M^mu_ak d_mu w_k + N0_ak w_k; the adjoint w.r.t. dx and B (or g^-1 when adjoint_B is False)."""
    N = n + 1
    X = sp.symbols("x0:%d" % N, real=True)
    et = eta_(n)
    c = sp.Matrix([cfun(X, k) for k in range(N)])
    cu = et * c
    M = [sp.Matrix(N, N, lambda a, k: -et[k, mu] * c[a] - (1 if a == k else 0) * cu[mu]
                   + e * (1 if a == mu else 0) * cu[k]) for mu in range(N)]
    div = sum(sp.diff(cu[m], X[m]) for m in range(N))
    N0 = sp.Matrix(N, N, lambda a, k: -sum(et[k, q] * sp.diff(c[a], X[q]) for q in range(N))
                   - (1 if a == k else 0) * div + e * sp.diff(cu[k], X[a]))
    Bm = B_of(n, c, e) if adjoint_B else et
    P = point(X)
    zeroth = all(sp.simplify((Bm * M[mu] - (Bm * M[mu]).T).subs(P)) == sp.zeros(N, N) for mu in range(N))
    Tm = (-sum((sp.diff(M[mu].T * Bm, X[mu]) for mu in range(N)), sp.zeros(N, N)) + N0.T * Bm).subs(P)
    S = N0.subs(P) + Bm.subs(P).inv() * Tm
    return S.applyfunc(sp.cancel), zeroth


def c_saddle(n):
    """r_0^2 c_{r0,v} = r_0 dt - v (r - r_0) dr with r_0 = 1 ([Hin26a] (4.8))."""
    def cfun(X, k):
        r = sp.sqrt(sum(X[i]**2 for i in range(1, n + 1)))
        return sp.Integer(1) if k == 0 else -v * (r - 1) * X[k] / r
    return cfun


def c_far(n):
    """c_v = r^-1 (dt - v dr) ([Hin26a] (4.2))."""
    def cfun(X, k):
        r = sp.sqrt(sum(X[i]**2 for i in range(1, n + 1)))
        return 1 / r if k == 0 else -v * X[k] / r**2
    return cfun


def at_radius(n, t0=0):
    return lambda X: {X[0]: t0, X[1]: R, **{X[i]: 0 for i in range(2, n + 1)}}


def saddle_S(n, adjoint_B=True):
    S, zeroth = S_matrix(n, c_saddle(n), s**2, at_radius(n), adjoint_B)
    return S.subs(R, 1 + xr * s / v).applyfunc(sp.factor), zeroth


# ------------------------------------------------------------------------------------------------- W1
def w1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    e = sp.Symbol("e", positive=True)
    c0 = sp.Symbol("c0", positive=True)
    for n in (3, 4):
        z = sp.symbols("z0:%d" % (n + 1), real=True)
        c = sp.Matrix([c0] + [0] * n)
        zeta = sp.Matrix(z)
        eff = e if control == 0 else (3 * e - 1) / 2                     # control: weight 1 at n = 4, 3/2 at n = 3
        L = ell(n, c, zeta, eff)
        Bm = B_of(n, c, eff)
        chk("n = %d: B l(zeta) is symmetric for generic zeta (Lemma 3.3)" % n,
            sp.simplify(Bm * L - (Bm * L).T) == sp.zeros(n + 1, n + 1))
        chk("n = %d: B is positive definite for e > 0 (B_00 = %s)" % (n, sp.factor(Bm[0, 0])),
            all(sp.simplify(Bm[i, i]) > 0 for i in range(n + 1)) if control == 0 else
            (sp.simplify(Bm[0, 0]).subs(e, sp.Rational(1, 100)) > 0))
        if control != 0:
            continue
        lam = sp.Symbol("lam")
        Gc = -c0**2
        z0 = (c.T * eta_(n) * zeta)[0] / Gc                               # zeta = z0 c + zeta'
        Gp = (zeta.T * eta_(n) * zeta)[0] - Gc * z0**2
        quad = lam**2 - (3 - e) * Gc * z0 * lam + (2 - e) * Gc**2 * z0**2 + e * Gc * Gp
        cp = (L / 2).charpoly(lam).as_expr()
        chk("n = %d: charpoly of l(zeta)/2 = (lam - G(c) zeta_0)^%d (his (3.8) quadratic)" % (n, n - 1),
            sp.expand(cp - (lam - Gc * z0)**(n - 1) * quad) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W2
def w2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    e = s**2
    adjB = control != 1
    S, zeroth = S_matrix(3, c_far(3), e, at_radius(3, T), adjB)
    half = (R**2 * S / 2).applyfunc(sp.cancel)
    w2_ = 1 - v**2
    printed46 = sp.Matrix([[v * (3 - v**2 + 2 * e) / (2 * w2_), (1 + v**2 + 2 * e * v**2) / (2 * w2_), 0, 0],
                           [(-2 * v**2 + e * (1 - 3 * v**2)) / (2 * w2_),
                            (-2 * v**3 + e * v * (1 - 3 * v**2)) / (2 * w2_),
                            0, 0], [0, 0, 3 * v / 2, 0], [0, 0, 0, 3 * v / 2]])
    chk("n = 3: the operator A + A* is of order zero (B M^mu symmetric)", zeroth or control == 1)
    chk("n = 3: (1/2) r^2 S for c_v is his (4.6), for every e", sp.simplify(half - printed46) == sp.zeros(4, 4))
    Sd, _ = saddle_S(3, adjB)
    x = xr
    Dl = (1 + x * s / v) * (1 - e * x**2)**2
    a00 = (v * (2 * (1 - x**2) + e * (1 - 3 * x**2) + e**2 * x**2 * (x**2 + 1))
           + x * s * (2 * (3 - x**2) + e * (1 - 3 * x**2) * (3 - e * x**2))) / Dl
    a01 = (1 + e) * x * s * (v * (-2 + e + e**2 * x**2) + x * s * (-2 + 3 * e - e**2 * x**2)) / Dl
    a10 = (1 + e) * x * s * (v * (-1 + 2 * x**2 - e * x**2) + x * s * (-3 + 2 * x**2 + e * x**2)) / Dl
    a11 = (v * (3 + 2 * x**2 - 5 * e * x**2 - e**2 * x**2 * (1 - (2 - e) * x**2))
           + x * s * (5 + 2 * x**2 - 11 * e * x**2 + e**2 * (-3 * x**2 + (6 + e) * x**4))) / Dl
    a22 = v * (5 - 4 * v / (v + x * s))
    z = lambda ex: sp.simplify(sp.cancel(ex)) == 0                                          # noqa: E731
    chk("n = 3: the interior saddle's a_00, a_10, a_11, a_22 are his Lemma 4.4's",
        z(Sd[0, 0] - a00) and z(Sd[1, 0] - a10) and z(Sd[1, 1] - a11) and z(Sd[2, 2] - a22))
    det0 = sp.factor(sp.cancel(Sd[0, 0] * Sd[1, 1] - Sd[0, 1] * Sd[1, 0]).subs(s, 0))
    chk("n = 3: its e = 0 determinant is his 2 v^2 (3 - 2x^2)", z(det0 - 2 * v**2 * (3 - 2 * x**2)))
    printed_det0 = sp.factor(sp.cancel(a00 * a11 - a01 * a10).subs(s, 0))
    chk("his printed a_01 is the computed one times e, and with it the e = 0 determinant would be 2 v^2 (1 - x^2)(3 + "
        "2x^2), not his: a misprint", z(a01 - e * Sd[0, 1]) and z(printed_det0 - 2 * v**2 * (1 - x**2) * (3 + 2 * x**2)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- W3
def total_symbol(n):
    e = s**2
    S, _ = S_matrix(n, c_far(n), e, at_radius(n, T))
    cvec = sp.Matrix([1 / R, -v / R] + [0] * (n - 1))
    zeta = sp.Matrix([-rk * bk / R, -(bs - bk) / R] + [0] * (n - 1))       # dw/w, w = rho_sf^b_sf rho_K^b_K
    Tm = (R**2 * (-ell(n, cvec, zeta, e) + S)).applyfunc(sp.cancel).subs(s, 0)
    dK = (Tm.subs(rk, 0) / 2).applyfunc(sp.factor)
    Rv = (Tm.subs({rk: v, bk: 0}) / 2).applyfunc(sp.factor)
    return dK, Rv


def eig_set(Mx):
    return sorted(((sp.factor(k), m) for k, m in Mx.eigenvals().items()), key=lambda p: (str(p[0]), p[1]))


def w3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    q = sp.Rational(1, 2) if control == 1 else 1                         # control: his thresholds claimed at n = 4
    d = bk - bs
    for n, half in ((3, sp.Rational(1, 2)), (4, q)):
        dK, Rv = total_symbol(n)
        wantK = eig_set(sp.diag(v * (half + d), 2 * v * (half + d), *([v * (half + 1 + d)] * (n - 1))))
        wantR = eig_set(sp.diag(v * (half - bs), 2 * v * (half - bs), *([v * (half + 1 - bs)] * (n - 1))))
        chk("n = %d: at dK+ the eigenvalues are v (%s + b_K - b_sf), 2v (...), v (%s + b_K - b_sf) (%dx)"
            % (n, half, half + 1, n - 1), eig_set(dK) == wantK)
        chk("n = %d: at R_v they are v (%s - b_sf), 2v (...), v (%s - b_sf) (%dx): b_K > b_sf - %s, b_sf < %s"
            % (n, half, half + 1, n - 1, half, half), eig_set(Rv) == wantR)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W4
def positive_on_interval(ex, lo, hi):
    num, den = sp.fraction(sp.cancel(sp.together(ex)))
    P, Q = sp.Poly(num, xr), sp.Poly(den, xr)
    mid = (lo + hi) / 2
    return (P.count_roots(lo, hi) == 0 and Q.count_roots(lo, hi) == 0
            and (P.eval(mid) > 0) == (Q.eval(mid) > 0))


def e0_numeric(n, vv, grid=1201):
    Sd, _ = saddle_S(n)
    tr = sp.lambdify((v, s, xr), sp.cancel(Sd[0, 0] + Sd[1, 1]), "mpmath")
    dt = sp.lambdify((v, s, xr), sp.cancel(Sd[0, 0] * Sd[1, 1] - Sd[0, 1] * Sd[1, 0]), "mpmath")
    a2 = sp.lambdify((v, s, xr), sp.cancel(Sd[2, 2]), "mpmath")
    mpm.mp.dps = 30
    xs = [mpm.mpf(-6) / 5 + mpm.mpf(12) / 5 * i / (grid - 1) for i in range(grid)]

    def ok(ee):
        ss = mpm.sqrt(ee)
        return all(tr(vv, ss, x) > 0 and dt(vv, ss, x) > 0 and a2(vv, ss, x) > 0 for x in xs)
    lo, hi = mpm.mpf("1e-9"), mpm.mpf("1e-2")
    for _ in range(30):
        mid = mpm.sqrt(lo * hi)
        lo, hi = (mid, hi) if ok(mid) else (lo, mid)
    return float(lo / vv**2)


def w4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Sd, zeroth = saddle_S(4)
    chk("n = 4: the operator A + A* is of order zero at the interior saddle", zeroth)
    lim = lambda ex: sp.factor(sp.cancel(ex).subs(s, 0))                                   # noqa: E731
    chk("n = 4: at e = 0 it is his: a_22 = v (all three angular entries), trace 5v, determinant 2 v^2 (3 - 2x^2)",
        all(sp.simplify(lim(Sd[i, i]) - v) == 0 for i in range(2, 5))
        and sp.simplify(lim(Sd[0, 0] + Sd[1, 1]) - 5 * v) == 0
        and sp.simplify(lim(Sd[0, 0] * Sd[1, 1] - Sd[0, 1] * Sd[1, 0]) - 2 * v**2 * (3 - 2 * xr**2)) == 0)
    sv = sp.Rational(1, 200) if control == 1 else sp.sqrt(DMP.PARAMS[DMP.e])  # control: e = 1/40000 > e_0
    Sv = Sd.subs({v: sp.Rational(1, 2), s: sv})
    lo, hi = sp.Rational(-6, 5), sp.Rational(6, 5)
    good = (positive_on_interval(Sv[0, 0] + Sv[1, 1], lo, hi)
            and positive_on_interval(Sv[0, 0] * Sv[1, 1] - Sv[0, 1] * Sv[1, 0], lo, hi)
            and all(positive_on_interval(Sv[i, i], lo, hi) for i in range(2, 5)))
    chk("n = 4, v = 1/2, e = %s: S positive definite on |x| <= 6/5 (Sturm; trace, determinant, angular block)"
        % (sv**2), good)
    if control == 0:
        r5, r4 = e0_numeric(4, mpm.mpf(1) / 2), e0_numeric(3, mpm.mpf(1) / 2)
        if verbose:
            print("        e_0/v^2 at v = 1/2: %.6f (n = 4), %.6f (n = 3)" % (r5, r4))
        chk("the largest admissible e: ~ 0.000069 v^2 at n = 4, ~ 0.000154 v^2 at n = 3 (his ~ 0.000152)",
            abs(r5 - 0.000069) < 0.000002 and abs(r4 - 0.000154) < 0.000002)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W5
def w5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    e, w = sp.symbols("e w", positive=True)
    chk("for 0 < e <= w < 1: 2(1 - e) w/(e (1 - w)) - 2 = 2(w - e)/(e (1 - w)) >= 0 (no dimension enters)",
        sp.simplify(2 * (1 - e) * w / (e * (1 - w)) - 2 - 2 * (w - e) / (e * (1 - w))) == 0)
    n, vv, ee = 4, sp.Rational(1, 2), sp.Rational(1, 102400)
    se = sp.sqrt(ee)
    pts = [(1 + se / vv, 1), (1 - se / vv, -1), (sp.Rational(1, 2), -1), (2, 1)]
    if control == 1:
        pts = [(1 + se / (2 * vv), 1)]
    ok = True
    for r, sg in pts:
        c = sp.Matrix([1, -vv * (r - 1)] + [0] * (n - 1))
        L = ell(n, c, sp.Matrix([0, sg] + [0] * (n - 1)), ee)
        ok &= all(sp.re(k) < 0 for k in L.eigenvals())
    chk("n = 4, v = 1/2, e = 1/102400: l(+-dr) negative definite at r_0 (1 +- sqrt(e)/v), r_0/2 and 2 r_0", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W6
def w6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    P = DMP.PARAMS
    chk("damping5.py's point: v = 1/2, e = 1/102400 (W4's admissible e), h = 10^-6 < e",
        P[DMP.v] == sp.Rational(1, 2) and P[DMP.e] == sp.Rational(1, 102400) and P[DMP.h] < P[DMP.e])
    Sv = saddle_S(4)[0].subs({v: sp.Rational(1, 2), s: sp.Rational(1, 10)})               # e = 1/100
    lo, hi = sp.Rational(-6, 5), sp.Rational(6, 5)
    adm = (positive_on_interval(Sv[0, 0] + Sv[1, 1], lo, hi)
           and positive_on_interval(Sv[0, 0] * Sv[1, 1] - Sv[0, 1] * Sv[1, 0], lo, hi))
    chk("e = 1/100 (section 10.12's first point) is %s for Lemma 4.4" % ("admissible" if control else "not admissible"),
        adm if control == 1 else not adm)
    return chk.ok


CHECKS = [("W1 the fibrewise theory (Lemmas 3.3-3.8) in five dimensions at the weight 2/3; his (3.8)", w1, 1),
          ("W2 the subprincipal symbol from the definition; his (4.6) and Lemma 4.4 at n = 3, a_01 misprinted", w2, 1),
          ("W3 Lemmas 4.1-4.2 at n = 4: the weight thresholds b_K > b_sf - 1, b_sf < 1", w3, 1),
          ("W4 Lemma 4.4 at n = 4: positive on |x| <= 6/5 for e below e_0 ~ 0.000069 v^2", w4, 1),
          ("W5 Lemma 4.3 is dimension-free; l(+-dr) definite at n = 4", w5, 1),
          ("W6 damping5.py's point is admissible; section 10.12's first point, e = 1/100, is not", w6, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<108} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"semiclass5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"semiclass5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
