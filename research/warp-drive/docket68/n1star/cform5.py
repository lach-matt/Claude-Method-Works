#!/usr/bin/env python3
"""cform5.py -- a constraint damping 1-form c on five-dimensional Tangherlini of [Hin26a] Proposition 5.1's kind,
explicit, with its conditions (1), (3) and (6) checked on the Tangherlini metric itself and (4)-(6) on sf
(N1STAR-PROOF.md section 10.14; ROUTES-OPEN.md 4.15; D56).  Labels: computed (exact, sympy; C6 a measurement),
deduced, READ.

[Hin26a] (arXiv:2606.27658v2) glues c on Kerr from the Minkowski pieces of its section 4 (Proposition 5.1): c is
stationary and r c past timelike (1); c = (1/2) r_0^-2 (r_0 dt - v (r - r_0) dr) on [r_0/2, 2 r_0] (its interior saddle
at r = r_0) and r^-1 (dt - v dr) for r >= 3 r_0 (2), r >= 2 r_0 before smoothing ((5.11)); S_{g,c,e} positive definite
for |r - r_0| <= (6/5) r_0 e^(1/2)/v (3); positivity at the corner dK+ and the sink R_v of sf for the weights (4)-(5);
and -l(-dr) positive definite for m <= r <= r_0 - r_0 e^(1/2)/v, -l(dr) for r >= r_0 + r_0 e^(1/2)/v, with conditions
on sf (6).  Near the horizon it uses three pieces and a partition of unity, Boyer-Lindquist t being singular there.  Here
Tangherlini, g = -f dt^2 + 2 (1 - f) dt dr + (2 - f) dr^2 + r^2 dOmega_3^2 in Kerr-Schild time t, f = 1 - mu/r^2, mu =
1 (r_h = 1; [r_h/2, oo) stands for his m <= r, m = r_+/2 at a = 0), v = 1/2, e = 1/102400 (semiclass5.py W4's
admissible e), and

    c = dt + (v/2) dr  (r <= r_0/2),   r_0 dt - v (r - r_0) dr  ([r_0/2, 2 r_0]),   dt - v dr  (r >= 2 r_0),

each piece up to a positive factor (none of the conditions sees it), the factors (2 r_0)^-1, (1/2) r_0^-2 and r^-1
making c continuous; r_0 = 100.  The Kerr-Schild t differs from the static t by int (f^-1 - 1) dr, so the outer piece
is r^-1 (dt - v dr) up to O(mu r^-3) dr.

  C1 (computed, exact) S on Tangherlini, from its definition: S = (L - L*)/(2ih) for L/(2ih) = 2 delta_g(c (x)_s .) +
     e d iota_{c#}, the adjoint with |dg| = r^3 cos th sin th and B, in polar Kerr-Schild coordinates with Christoffel
     symbols; it is of order zero, free of the angles, block diagonal (the (t, r) block and v-type angular entries,
     equal), and at mu = 0 it is semiclass5.py's Minkowski S (trace, determinant and angular entry at the saddle).
     Control: the adjoint taken with g^-1 for B (not of order zero).
  C2 (computed, exact) Condition (1): each piece is past timelike (G(c) < 0, <c, dt> < 0) on its interval of [r_h/2,
     oo), and the pieces join continuously at r_0/2 and 2 r_0.  The inner piece is past timelike for every r > 0 and
     every v in (0, 1): G = (1 - v/2)(-2 + f (1 - v/2)) and <c, dt> = -(2 - v/2) + f (1 - v/2), f < 1 -- one piece,
     where his construction, in Boyer-Lindquist time, uses three: the saving is the horizon-regular time.  Control: the
     inner piece dt + dr (b = 1), null.
  C3 (computed, exact) Condition (6) on [r_h/2, oo): <c, dr> > 0 for r <= r_0 - r_0 e^(1/2)/v -- -c# points into the
     black hole there -- and < 0 for r >= r_0 + r_0 e^(1/2)/v, with Lemma 3.8's f e G(c) + 2 (1 - e) <c, dr>^2 > 0
     (G(dr) = f), so -l(-dr), resp. -l(dr), is positive definite (semiclass5.py W1: Lemma 3.8 holds in five
     dimensions).  Control: r_0 = 30, where the condition fails just outside the saddle.
  C4 (computed, exact) Condition (3): on Tangherlini, S is positive definite on |r - r_0| <= (6/5) r_0 e^(1/2)/v at r_0
     = 100 (Sturm on the block's trace and determinant and on the angular entry).  Control: the window 12/5.
  C5 (computed, exact) Condition (6) on sf, which sees only Minkowski: his (5.8), -rho^4 + rho^2 < 2 (1 - e)/(e (1 -
     v^2)) rho^2 (v - rho)^2, for rho = r/t in [delta, v (1 - delta)] and [v (1 + delta), 10], delta = 1/100 -- the
     quantities G(rho^2 dt - rho dr) and <r c, .> involve no dimension; on (0, 10] it fails exactly on an interval
     about v of half-width under 0.00166, so delta_sf may be any number above 0.0034 and delta_r any positive number.
     Control: e = 1/2.
  C6 (computed; a measurement) The smallest integer r_0 >= 2 for which C2-C4 hold at (mu, v, e) = (1, 1/2, 1/102400) is
     86, by every integer in [2, 86]: (1) holds at each, (6) from 33 on, (3) at 86 alone; 87, 200 and 1000 pass.  At
     e/4 it is 137.  By scaling (deduced: with mu = u r_0^2 every condition depends on u and r/r_0 alone) the bound is
     86 mu^(1/2) = 86 r_h at this e.  Control: the scan with the window of (3) widened to (121/100) r_0 e^(1/2)/v.
  C7 (computed, exact) Conditions (4)-(5) on sf at e = 1/102400.  There the symbol T = r^2 (-l(dw/w) + S) of c = r^-1
     (dt - v dr), w = rho_sf^b_sf rho_K^b_K, depends on rho_K = r/t and the weights only, is B-self-adjoint, and at
     b_K = 0 (the sink's w') is free of rho_K.  Its characteristic polynomial is (2 - d - lam)^3 q(d, lam), d = b_sf -
     b_K at dK+ and b_sf at R_v; all its roots are positive iff d < b* = 0.99340731..., a root of 204795 d^2 - 409605 d
     + 204801: (4) at dK+ iff b_K > b_sf - b*, (5) iff b_sf < b*, against semiclass5.py W3's 1 at e = 0.  At (alpha_K,
     alpha_sf) = (1, -102), his Theorem 6.2's proof's weights at C_0 = 100 (b_K = alpha_K, b_sf = alpha_sf + 1, his p.
     39), T is positive definite on all of sf with rho_K <= 10.  Control: b_sf = 1, W3's e = 0 threshold, at this e.

Not checked here, and deduced by his arguments: conditions (4)-(5) off sf, for 0 < rho_sf <= 2 delta_r, where Tangherlini
differs from its Minkowski model by rho_sf C^oo terms, so that C7's positivity persists for some delta_r > 0 (not made
explicit, here or in his proof); and the smoothing of c at r_0/2 and 2 r_0, where only (1) and (6) are asked, open
conditions on c at each point.  Not touched: h_0 of his Theorem 5.2, which his proof does not make explicit.

READ (alphaXiv, 2026-10-21). [Hin26a] pp. 38-41 (Proposition 5.1 and its proof: (5.1)-(5.13), footnote 14, "roughly r_2
>= 81m/e^(1/2)" on Schwarzschild), 25-27 (Lemmas 3.3, 3.5, 3.8), 28-33 (section 4.1-4.2), 41 (Theorem 5.2, (5.14)), 53
(Proposition 5.1 (4) and (6) in its use), 67 (Theorem 6.2's proof: alpha_K = 1, alpha_sf = -C_0 - 2).

sympy.  python3 cform5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import semiclass5 as SC
from damping5 import Checklist

t, r, th, p1, p2 = sp.symbols("t r theta p1 p2", real=True)
XS = [t, r, th, p1, p2]
V, E, SE, MU = sp.Rational(1, 2), sp.Rational(1, 102400), sp.Rational(1, 320), 1
R0 = sp.Symbol("R0", positive=True)
RIN = sp.Rational(1, 2)


def metric(mu):
    f = 1 - mu / r**2
    g = sp.zeros(5, 5)
    g[0, 0], g[0, 1], g[1, 0], g[1, 1] = -f, 1 - f, 1 - f, 2 - f
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2 * sp.cos(th)**2, r**2 * sp.sin(th)**2
    return g, r**3 * sp.cos(th) * sp.sin(th)


def S_tangherlini(alpha, beta, e, mu, adjoint_B=True):
    """S for c = alpha dt + beta dr on Tangherlini (mu = 0: Minkowski), from the definition."""
    N = 5
    g, vol = metric(mu)
    gi = g.inv().applyfunc(sp.cancel)
    Gam = [[[sp.cancel(sum(gi[a, d] * (sp.diff(g[d, b], XS[c]) + sp.diff(g[d, c], XS[b]) - sp.diff(g[b, c], XS[d]))
                           for d in range(N)) / 2) for c in range(N)] for b in range(N)] for a in range(N)]
    c = sp.Matrix([alpha, beta, 0, 0, 0])
    cu = (gi * c).applyfunc(sp.cancel)
    M = [sp.zeros(N, N) for _ in range(N)]
    N0 = sp.zeros(N, N)
    for a in range(N):
        for k in range(N):
            for q in range(N):
                for b in range(N):
                    co = -gi[b, q]                     # (A w)_a = -g^{bq} nabla_q (c_a w_b + c_b w_a) + e d_a(c#.w)
                    if co == 0:
                        continue
                    if k == b:
                        M[q][a, k] += co * c[a]
                    if k == a:
                        M[q][a, k] += co * c[b]
                    N0[a, k] += co * ((sp.diff(c[a], XS[q]) if k == b else 0) + (sp.diff(c[b], XS[q]) if k == a else 0))
                    for d in range(N):
                        G1, G2 = Gam[d][q][a], Gam[d][q][b]
                        if G1 != 0:
                            N0[a, k] -= co * G1 * ((c[d] if k == b else 0) + (c[b] if k == d else 0))
                        if G2 != 0:
                            N0[a, k] -= co * G2 * ((c[a] if k == d else 0) + (c[d] if k == a else 0))
            M[a][a, k] += e * cu[k]
            N0[a, k] += e * sp.diff(cu[k], XS[a])
    Gc = sp.cancel((c.T * gi * c)[0])
    B = (gi - (1 + e) / Gc * (cu * cu.T)).applyfunc(sp.cancel) if adjoint_B else gi
    zeroth = all((B * M[q] - (B * M[q]).T).applyfunc(lambda z: sp.simplify(sp.cancel(z))) == sp.zeros(N, N)
                 for q in range(N))
    T = -sum((sp.diff(vol * M[q].T * B, XS[q]) for q in range(N)), sp.zeros(N, N)) / vol + N0.T * B
    T = T.applyfunc(lambda z: sp.simplify(sp.cancel(z)))
    S = N0 + B.inv() * T
    return S.applyfunc(lambda z: sp.simplify(sp.cancel(z))), zeroth


def saddle_invariants(mu, e=E, adjoint_B=True):
    S, zeroth = S_tangherlini(R0 + 0 * r, -V * (r - R0), e, mu, adjoint_B)
    blk = S[:2, :2]
    return sp.cancel(blk.trace()), sp.cancel(blk.det()), [sp.cancel(S[i, i]) for i in range(2, 5)], S, zeroth


def sign_on(ex, lo, hi, want):
    """ex has the sign of want on [lo, hi] (hi None: [lo, oo)), exactly: no root of numerator or denominator there."""
    num, den = sp.fraction(sp.cancel(sp.together(ex)))
    P, Q = sp.Poly(num, r), sp.Poly(den, r)
    if P.count_roots(lo, hi) or Q.count_roots(lo, hi):
        return False
    mid = lo + 1 if hi is None else (lo + hi) / 2
    val = P.eval(mid) * Q.eval(mid)
    return val > 0 if want > 0 else val < 0


f_ = 1 - sp.Integer(MU) / r**2
gtt, gtr, grr = -(2 - f_), 1 - f_, f_


def Gn(a, b):
    return sp.cancel(gtt * a**2 + 2 * gtr * a * b + grr * b**2)


def c_dr(a, b):
    return sp.cancel(gtr * a + grr * b)


def c_dt(a, b):
    return sp.cancel(gtt * a + gtr * b)


def pieces(r0, b_in=V / 2):
    return [("inner", (1, b_in), RIN, r0 / 2), ("middle", (r0, -V * (r - r0)), r0 / 2, 2 * r0),
            ("outer", (1, -V), 2 * r0, None)]


def cond1(r0, b_in=V / 2):
    return {nm: sign_on(Gn(a, b), lo, hi, -1) and sign_on(c_dt(a, b), lo, hi, -1)
            for nm, (a, b), lo, hi in pieces(r0, b_in)}


def cond6(r0, e=E):
    w = r0 * sp.sqrt(e) / V
    segs = [("inner", (1, V / 2), RIN, r0 / 2, +1), ("middle, inside", (r0, -V * (r - r0)), r0 / 2, r0 - w, +1),
            ("middle, outside", (r0, -V * (r - r0)), r0 + w, 2 * r0, -1), ("outer", (1, -V), 2 * r0, None, -1)]
    return {nm: sign_on(c_dr(a, b), lo, hi, sg) and sign_on(f_ * e * Gn(a, b) + 2 * (1 - e) * c_dr(a, b)**2, lo, hi, +1)
            for nm, (a, b), lo, hi, sg in segs}


_INV = {}


def invariants(e=E):
    if e not in _INV:
        _INV[e] = saddle_invariants(MU, e=e)
    return _INV[e]


def cond3(r0, factor=sp.Rational(6, 5), e=E):
    tr, dt, ang, _, _ = invariants(e)
    w = factor * r0 * sp.sqrt(e) / V
    return all(sign_on(z.subs(R0, r0), r0 - w, r0 + w, +1) for z in (tr, dt, ang[0]))


# ------------------------------------------------------------------------------------------------- C1
def c1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    tr, dt, ang, S, zeroth = saddle_invariants(MU, adjoint_B=(control != 1))
    chk("on Tangherlini (mu = 1) A + A* is of order zero (B M^mu symmetric)", zeroth)
    if control == 1:
        return chk.ok
    chk("S is free of the angles", all(not (S[i, j].free_symbols & {th}) for i in range(5) for j in range(5)))
    chk("S is block diagonal: the (t, r) block and three equal angular entries",
        all(sp.simplify(S[i, j]) == 0 for i in range(5) for j in range(5) if i != j and not (i < 2 and j < 2))
        and sp.simplify(ang[0] - ang[1]) == 0 and sp.simplify(ang[0] - ang[2]) == 0)
    trm, dtm, angm, _, _ = saddle_invariants(0)
    Sd, _ = SC.saddle_S(4)
    x = SC.xr
    sub = {r: R0 * (1 + x * SC.s / SC.v)}
    mink = (sp.cancel(Sd[0, 0] + Sd[1, 1]), sp.cancel(Sd[0, 0] * Sd[1, 1] - Sd[0, 1] * Sd[1, 0]), sp.cancel(Sd[2, 2]))
    ours = [sp.cancel(z.subs(sub).subs({SC.v: V})) for z in (trm, dtm, angm[0])]
    want = [sp.cancel((z / R0**k).subs({SC.v: V, SC.s: SC.s})) for z, k in zip(mink, (0, 0, 0))]
    ok = all(sp.simplify((o - w_).subs(SC.s, SE)) == 0 for o, w_ in zip(ours, want))
    chk("at mu = 0 the saddle's trace, determinant and angular entry are semiclass5.py's Minkowski ones (e = 1/102400)",
        ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- C2
def c2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    r0 = sp.Integer(100)
    b_in = 1 if control == 1 else V / 2
    res = cond1(r0, b_in)
    chk("condition (1): each piece past timelike on its interval of [r_h/2, oo) (%s)" % ", ".join(res),
        all(res.values()))
    if control != 0:
        return chk.ok
    bb, ff = sp.symbols("b f", real=True)
    Gin = -(2 - ff) + 2 * (1 - ff) * bb + ff * bb**2
    chk("the inner piece dt + b dr: G = (1 - b)(-2 + f (1 - b)) and <c, dt> = -(2 - b) + f (1 - b), negative for f < 1, "
        "0 < b < 1, every r > 0", sp.expand(Gin - (1 - bb) * (-2 + ff * (1 - bb))) == 0
        and sp.expand((-(2 - ff) + (1 - ff) * bb) - (-(2 - bb) + ff * (1 - bb))) == 0)
    m1 = sp.Matrix([1, V / 2]) / (2 * r0)
    m2 = sp.Matrix([r0, -V * (r0 / 2 - r0)]) / (2 * r0**2)
    m3 = sp.Matrix([r0, -V * (2 * r0 - r0)]) / (2 * r0**2)
    m4 = sp.Matrix([1, -V]) / (2 * r0)
    chk("continuous joins: (2 r_0)^-1 (dt + (v/2) dr) at r_0/2 and (2 r_0)^-1 (dt - v dr) at 2 r_0",
        m1 == m2 and m3 == m4)
    return chk.ok


# ------------------------------------------------------------------------------------------------- C3
def c3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    r0 = sp.Integer(30) if control == 1 else sp.Integer(100)
    res = cond6(r0)
    chk("condition (6) at r_0 = %s: <c, dr> of the right sign and Lemma 3.8's inequality on %s" % (r0, ", ".join(res)),
        all(res.values()))
    return chk.ok


# ------------------------------------------------------------------------------------------------- C4
def c4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    fac = sp.Rational(12, 5) if control == 1 else sp.Rational(6, 5)
    chk("condition (3) at r_0 = 100: S positive definite on |r - r_0| <= %s r_0 e^(1/2)/v (Sturm)" % fac,
        cond3(sp.Integer(100), fac))
    return chk.ok


# ------------------------------------------------------------------------------------------------- C5
def c5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    rho = sp.Symbol("rho", positive=True)
    e = sp.Rational(1, 2) if control == 1 else E
    dl = sp.Rational(1, 100)
    ex = 2 * (1 - e) / (e * (1 - V**2)) * rho**2 * (V - rho)**2 - (-rho**4 + rho**2)
    P = sp.Poly(sp.expand(ex * e * (1 - V**2)), rho)
    ok = all(P.count_roots(lo, hi) == 0 and P.eval((lo + hi) / 2) > 0
             for lo, hi in ((dl, V * (1 - dl)), (V * (1 + dl), 10)))
    chk("his (5.8) on rho = r/t in [1/100, v (1 - 1/100)] and [v (1 + 1/100), 10] at e = %s" % e, ok)
    if control != 0:
        return chk.ok
    Q = sp.Poly(sp.cancel(P.as_expr() / rho**2), rho)
    w = sp.Rational(166, 100000)
    chk("on (0, 10] (5.8) fails exactly on an interval about v of half-width < 0.00166: rho^-2 times it has one root "
        "in (v - 0.00166, v), one in (v, v + 0.00166), none else in [0, 10], and is positive at 0",
        Q.count_roots(V - w, V) == 1 and Q.count_roots(V, V + w) == 1 and Q.count_roots(0, 10) == 2
        and Q.eval(0) > 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- C6
def c6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ks = list(range(2, 87))
    s1 = [k for k in ks if all(cond1(sp.Integer(k)).values())]
    s6 = [k for k in ks if all(cond6(sp.Integer(k)).values())]
    fac3 = sp.Rational(121, 100) if control == 1 else sp.Rational(6, 5)     # control: the window of (3) widened
    s3 = [k for k in ks if cond3(sp.Integer(k), factor=fac3)]
    both = sorted(set(s1) & set(s6) & set(s3))
    if verbose:
        print("        r_0 in [2, 86]: (1) at %d of %d, (6) from %d, (3) at %s" % (len(s1), len(ks), s6[0], s3))
    chk("every integer r_0 in [2, 86]: (1) holds at each, (6) exactly from 33 on, (3) only at 86",
        s1 == ks and s6 == list(range(33, 87)) and s3 == [86])
    chk("the smallest integer r_0 >= 2 with C2-C4 at (1, 1/2, 1/102400) is 86; 87, 200 and 1000 pass",
        bool(both) and both[0] == 86
        and all(all(cond1(sp.Integer(k)).values()) and all(cond6(sp.Integer(k)).values()) and cond3(sp.Integer(k))
                for k in (87, 200, 1000)))
    if control != 0:
        return chk.ok
    e4 = E / 4
    s3 = [k for k in range(2, 138) if cond3(sp.Integer(k), e=e4)]
    k = sp.Integer(137)
    chk("at e/4 = 1/409600 the smallest such r_0 is 137: (3) holds at no integer in [2, 136] and at 137, where (1) "
        "and (6) hold; 137/86 = 1.59, between 4^(1/4) and 4^(1/2)",
        s3 == [137] and all(cond1(k).values()) and all(cond6(k, e=e4).values()))
    return chk.ok


# ------------------------------------------------------------------------------------------------- C7
def sf_symbol():
    """T = r^2 (-l(dw/w) + S) on sf for c = r^-1 (dt - v dr), w = rho_sf^b_sf rho_K^b_K, at (v, e) = (1/2, 1/102400):
    Minkowski, since g and its Minkowski model agree at sf as 3sc-metrics (semiclass5.py's S at n = 4, undivided)."""
    n = 4
    S, _ = SC.S_matrix(n, SC.c_far(n), E, SC.at_radius(n, SC.T))
    cvec = sp.Matrix([1 / SC.R, -SC.v / SC.R] + [0] * (n - 1))
    zeta = sp.Matrix([-SC.rk * SC.bk / SC.R, -(SC.bs - SC.bk) / SC.R] + [0] * (n - 1))
    Tm = (SC.R**2 * (-SC.ell(n, cvec, zeta, E) + S)).applyfunc(sp.cancel).subs(SC.v, V).applyfunc(sp.cancel)
    return Tm, SC.B_of(n, sp.Matrix([1, -V] + [0] * (n - 1)), E)


def c7(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Tm, Bm = sf_symbol()
    bk, bs, rk = SC.bk, SC.bs, SC.rk
    lam, d = sp.symbols("lam d")
    if control == 1:                                            # control: W3's e = 0 threshold b_sf < 1, at e > 0
        cp = sp.Poly((Tm.subs({bk: 0, bs: 1}) - lam * sp.eye(5)).det(), lam)
        chk("T' at b_sf = 1 is positive definite (no eigenvalue <= 0)", cp.count_roots(None, 0) == 0)
        return chk.ok
    chk("T depends on rho_K = r/t and the weights only, is B-self-adjoint, and T' (b_K = 0) is free of rho_K",
        Tm.free_symbols <= {bk, bs, rk} and sp.simplify(Bm * Tm - (Bm * Tm).T) == sp.zeros(5, 5)
        and rk not in Tm.subs(bk, 0).free_symbols)
    q = 102400 * lam**2 - (307202 - 307199 * d) * lam + 204795 * d**2 - 409605 * d + 204801
    ok = (sp.expand((Tm.subs(rk, 0) - lam * sp.eye(5)).det() * 102400
                    - (2 - (bs - bk) - lam)**3 * q.subs(d, bs - bk)) == 0
          and sp.expand((Tm.subs(bk, 0) - lam * sp.eye(5)).det() * 102400 - (2 - bs - lam)**3 * q.subs(d, bs)) == 0)
    chk("the characteristic polynomials: at dK+ (2 - d - lam)^3 q(d, lam), d = b_sf - b_K; at R_v the same with d = "
        "b_sf; q = 102400 lam^2 - (307202 - 307199 d) lam + 204795 d^2 - 409605 d + 204801", ok)
    q0 = sp.Poly(q.subs(lam, 0), d)
    bstar = [z for z in q0.nroots(n=20) if z < 1][0]
    chk("q's roots in lam are positive iff d < b* = 0.99340731..., the smaller root of q(d, 0) (the larger, "
        "1.00666..., exceeds 307202/307199, where their sum turns negative): so (4) at dK+ iff b_K > b_sf - b*, (5) "
        "at R_v iff b_sf < b*, against W3's b* = 1 at e = 0",
        q0.count_roots(sp.Rational(9934, 10000), sp.Rational(9935, 10000)) == 1 and q0.count_roots(-10, 1) == 1
        and q0.count_roots(1, sp.Rational(307202, 307199)) == 0 and abs(bstar - 0.99340731) < 1e-8)
    T1 = Tm.subs({bk: 1, bs: -101})
    blk = T1[:2, :2]
    ok = all(sign_on(z.subs(rk, r), 0, 10, +1) for z in (blk.trace(), blk.det(), T1[2, 2]))
    chk("at (alpha_K, alpha_sf) = (1, -102) (b_K = 1, b_sf = -101), T is positive definite for every rho_K in [0, 10] "
        "(Sturm), and T' on all of sf: (4)-(5) on sf hold there for any delta'_r <= 5 and any delta_sf", ok)
    return chk.ok


CHECKS = [("C1 S on Tangherlini from its definition: order zero, angle-free, block diagonal; mu = 0 as semiclass5",
           c1, 1),
          ("C2 condition (1): the glued c is past timelike from r_h/2; one inner piece (his, Boyer-Lindquist: three)",
           c2, 1),
          ("C3 condition (6) on [r_h/2, oo) at r_0 = 100: -c# points into the black hole inside the saddle", c3, 1),
          ("C4 condition (3) at r_0 = 100: S positive definite on the saddle window (6/5) r_0 e^(1/2)/v", c4, 1),
          ("C5 condition (6) on sf: his (5.8), dimension-free, at e = 1/102400", c5, 1),
          ("C6 the smallest integer r_0 for (1), (3), (6) at (mu, v, e) = (1, 1/2, 1/102400): 86, a measurement",
           c6, 1),
          ("C7 conditions (4)-(5) on sf at e = 1/102400: the thresholds b_sf < b* ~ 0.99341, and positive at (1, -102)",
           c7, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"cform5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"cform5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
