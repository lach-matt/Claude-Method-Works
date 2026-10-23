"""zstates5.py -- [Hin26] section 6.5.1 (asymptotic symmetries) and Proposition 8.9 (gauged linearized Kerr metrics) in
five dimensions: the orders at infinity of Tangherlini against Minkowski, the defects of the asymptotic translations,
boosts and rotations, the linearized Myers-Perry metrics and their gauge sources, and the exponents the constructions
need against the indicial roots of box^Ups(0) (N1STAR-PROOF.md section 10.28; ROUTES-OPEN.md 4.29; D80, D82).  Labels:
computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) section 6.5.1 builds from the Minkowskian symmetries stationary 1-forms in ker box^Ups:
dt, the translations d(rS) (S in S_1), the boosts t* d(rS) + r d(rS) - rS dt and the rotations V (V in V_1), each
corrected by solving box^Ups(0) omega' = -box^Ups(0)(leading term) with his Lemma 6.13; his Lemma 6.14 gives
delta*_g(0) - delta*_gbar(0) in rho^2 Diff^0_b and box^Ups(0) - box^Ups_gbar(0) in rho^3 Diff^2_b in four dimensions,
and the boost's correction carries (log rho) c_b,s1 d(rS) ((6.31)).  His Proposition 8.9 puts the linearized Kerr
metrics into the gauge delta_(g,E) G h = 0, delta_(g,E) = delta_g + E^Ups, E^Ups h = -gam_Ups (2 iota_(g^-1 c) h - (1 -
e_Ups) c tr h), c = r^-1 dt ((4.1)-(4.3)): g-dot(1, 0) in rho C^oo, its gauge 1-form with (log rho) c_b omega-bar_s0
((8.19)), the s0 root 0 met; g-dot(0, a-dot) in rho^2 C^oo, its gauge 1-form at rho^1, 1 no root.  Here five-dimensional
Tangherlini, f = 1 - mu/r^2, with the trace weight 2/3 in E^Ups (10.15), beside four-dimensional Schwarzschild (f = 1 -
2M/r) as the control.  Z1, Z3 and Z4 work in Cartesian coordinates x in R^4, g = -f dt^2 + dx^2 + (mu/(r^2 -
mu))(x.dx)^2/r^2, reading orders along the ray x = R u, u = (2, 4, 5, 6)/9, and again along (1, 2, 4, 10)/11; Z2, Z3's
second part and Z5 in polar or retarded coordinates (t or u = t*, r, chi, theta, phi), reading orders on gbar's
orthonormal frame (dt, dr, r dchi, ...) at sin chi = 3/5, sin theta = 5/13, sin phi = 8/17, and again at 5/13, 8/17,
3/5 -- the same orders, the two frames differing by a rotation bounded with its inverse.

  Z1 (computed, exact) The orders.  g - gbar in rho^2 C^oo and Gamma of order rho^3 (four dimensions: rho, rho^2), so
     that (deduced, as his Lemma 6.14 from his (3.21)) delta*_g(0) - delta*_gbar(0) is in rho^3 Diff^0_b and box(0) -
     box_gbar(0) in rho^4 Diff^2_b in five dimensions; and r* = r + (r_h/2) log((r - r_h)/(r + r_h)) has r* - r -> 0,
     no logarithm (four dimensions: r* - r ~ 2M log r).  Control: the four-dimensional orders claimed.
  Z2 (computed, exact) The translations.  delta*_g dx^1 is of order rho^3 and box dx^1 = 2 delta G delta* dx^1 of order
     rho^4 (his rho^2, rho^3), so the correction solves box^Ups(0) omega' in rho^4, omega' at rho^2: 2 is an s1 root of
     box(0) at z = 0 (the root l + 1 of 10.15(i) at l = 1) and not for z > 0, where the root through 2 is (1 + (17 + 2z
     - 2 (z^2 + 4z + 16)^(1/2))^(1/2))/2 > 2, since (4 + z)^2 - (z^2 + 4z + 16) = 4z.  Control: z = 0.
  Z3 (computed, exact) The boosts.  For B = t dx^1 - x^1 dt, delta*_g B = t delta*_g dx^1 + K with K stationary of order
     rho^2 (his rho); and with his t-bar = t* + r ((6.5)), in retarded coordinates u = t* = t - r*, g = -f du^2 - 2 du
     dr + r^2 (round S^3) and gbar = -du^2 - 2 du dr + r^2 (round S^3), the boost B-bar = t-bar dx^1 - x^1 dt-bar is
     Killing for gbar, K-bar = delta*_g B-bar - t* delta*_g dx^1 is of order rho^2 and the stationary residual
     box^Ups_g B-bar - t* box^Ups_g dx^1 -- his f-breve less the term carrying the translation's correction -- of order
     rho^3 (four dimensions: rho, rho^2); so the boost's stationary correction solves box^Ups(0) omega in rho^3, omega
     at rho^1, and 1 is no s1 root at any z >= 0, the s1 polynomial at 1 being 3 (12 + 3z): no logarithm.  Control:
     four-dimensional Schwarzschild, where K and K-bar are of order rho and the residual of order rho^2, the correction
     at rho^0, and 0 an s1 root ([Hin26] Lemma 6.6), his log.
  Z4 (computed, exact) The rotations.  Each of the six x^i dx^j - x^j dx^i is orthogonal to the radial direction, so g
     gbar^-1 R = R, and delta*_g R = 0: every rotation is Killing on Tangherlini, so omega_v1(V) = V and h_v1(V) = 0
     for all six (V_1 = so(4), of rank 6 as 1-forms), as his Remark 6.17 at a = 0; S_1, the span of x^i/r, has rank
     4.  Control: f R, not Killing.
  Z5 (computed, exact) The linearized Myers-Perry metrics.  h_mu = d_mu g and h_A = (mu/r^4)(dt (x) w + w (x) dt), w =
     x^1 dx^2 - x^2 dx^1 = r^2 sin^2 chi sin^2 theta dphi, solve D Ric(h) = 0, of orders rho^2 and rho^3 (his rho,
     rho^2); the gauge source eta = delta_(g,E) G h is of order rho^3 for h_mu (s0) and, delta G h_A vanishing, eta =
     E^Ups h_A = (2 gam_Ups mu/(f r^5)) w for h_A, of order rho^4 (v1); so the gauge 1-forms solve box^Ups(0) omega =
     -2 eta at rho^1 (s0) and rho^2 (v1), and 1 is no s0 root and 2 no v1 root of box^Ups(0), the s0 polynomial at 1
     being 2 (2 + z) and the v1 polynomial at 2 being 3 (10.15(i)).  Control: four-dimensional Schwarzschild's d_M g, of
     order rho, its source of order rho^2, where his gauge 1-form sits at rho^0, an s0 root, his (8.19)'s log.
  Z6 (computed, exact) The Myers-Perry family.  The one-spin metric of [ER08] (32)-(33) at d = 5, -dt^2 + (mu/Sigma)(dt
     - a sin^2 theta dphi)^2 + (Sigma/Delta) dr^2 + Sigma dtheta^2 + (r^2 + a^2) sin^2 theta dphi^2 + r^2 cos^2 theta
     dpsi^2, Sigma = r^2 + a^2 cos^2 theta, Delta = r^2 + a^2 - mu, has Ric = 0 at three exact points, is Tangherlini
     at a = 0 on the round S^3 (x^1 + i x^2 = r sin theta e^(i phi), x^3 + i x^4 = r cos theta e^(i psi)), and d_a g at
     a = 0 is -h_A with w = r^2 sin^2 theta dphi = x^1 dx^2 - x^2 dx^1: h_mu and h_A are its derivatives at zero
     rotation (h_A with the rotation reversed).  Controls: a^2 dropped from Delta, not Ricci-flat; d_a g = +h_A claimed.

Deduced, not computed here (N1STAR-PROOF.md 10.28): [Hin26] Proposition 6.15 in five dimensions with the orders shifted
by one -- omega_b,s1(S) - d(rS) in A^((2,0) u (2 + E_ind)) and h_b,s1(S) in A^((3,0) u (3 + E_ind)) at z > 0, the
boost's correction without (6.31)'s logarithm, h_b,v1 = 0 -- and his Proposition 8.9 there, the gauge 1-forms without
(8.19)'s logarithm, g-dot^Ups(mu) in A^((2,0) u (2 + E_ind)) and g-dot^Ups(A) in A^((3,0) u (3 + E_ind)); each by his
proof, with his Lemma 6.13 in five dimensions (deduced in 10.29 on the readings of 10.20) and the exponents above.

READ.  [Hin26] pp. 25 (section 1.4.1), 81 (Definition 4.1, (4.1)-(4.3)), 113 (Lemma 6.1), 117 (Lemma 6.6), 124-128
(Lemma 6.13; section 6.5.1: Lemma 6.14, Proposition 6.15, (6.29)-(6.35), Remarks 6.16-6.17, the proof), 154-155
(Proposition 8.9 and its proof, (8.19)-(8.20), Remark 8.10); [ER08] R. Emparan, H. S. Reall, Black holes in higher
dimensions, arXiv:0801.3471v2, p. 14 (section 4.1, (32)-(33)); alphaXiv, 2026-10-23.

sympy.  python3 zstates5.py [--selftest | --mutants] (--verbose lists every sub-check)
"""
import sys
import time
from functools import lru_cache

import sympy as sp

from damping5 import Checklist

t = sp.Symbol("t", real=True)
mu, M = sp.symbols("mu M", positive=True)
R = sp.Symbol("R", positive=True)
z = sp.Symbol("z", nonnegative=True)


@lru_cache(maxsize=None)
def geom(n):
    """Tangherlini (n = 4, f = 1 - mu/r^2) or Schwarzschild (n = 3, f = 1 - 2M/r) in Cartesian coordinates"""
    x = sp.symbols(f"x1:{n + 1}", real=True)
    X = (t,) + x
    r2 = sum(q**2 for q in x)
    m = mu if n == 4 else 2 * M * sp.sqrt(r2)                            # f = 1 - m/r^2
    f = (r2 - m) / r2
    N = n + 1
    g, gi = sp.zeros(N, N), sp.zeros(N, N)
    g[0, 0], gi[0, 0] = -f, -1 / f
    for i in range(n):
        for j in range(n):
            g[1 + i, 1 + j] = (1 if i == j else 0) + m * x[i] * x[j] / (r2 * (r2 - m))
            gi[1 + i, 1 + j] = (1 if i == j else 0) - m * x[i] * x[j] / r2**2
    assert (g * gi).applyfunc(sp.cancel) == sp.eye(N)
    Gam = [[[sp.cancel(sum(gi[l, k] * (sp.diff(g[k, m], X[nn]) + sp.diff(g[k, nn], X[m]) - sp.diff(g[m, nn], X[k]))
                           for k in range(N)) / 2) for nn in range(N)] for m in range(N)] for l in range(N)]
    u = [2, 4, 5, 6] if n == 4 else [1, 4, 8]                            # a generic ray: |u| = 9
    ray = {x[i]: R * sp.Rational(u[i], 9) for i in range(n)}
    return x, X, g, gi, Gam, f, ray


def ray2(n):
    """a second generic ray: (1, 2, 4, 10)/11, four dimensions (2, 3, 6)/7"""
    x = geom(n)[0]
    u, d = ([1, 2, 4, 10], 11) if n == 4 else ([2, 3, 6], 7)
    return {x[i]: R * sp.Rational(u[i], d) for i in range(n)}


r, ch, th, ph = sp.symbols("r chi theta phi", positive=True)
TRIG = {sp.sin(ch): sp.Rational(3, 5), sp.cos(ch): sp.Rational(4, 5), sp.sin(th): sp.Rational(5, 13),
        sp.cos(th): sp.Rational(12, 13), sp.sin(ph): sp.Rational(8, 17), sp.cos(ph): sp.Rational(15, 17)}
TRIG2 = {sp.sin(ch): sp.Rational(5, 13), sp.cos(ch): sp.Rational(12, 13), sp.sin(th): sp.Rational(8, 17),
         sp.cos(th): sp.Rational(15, 17), sp.sin(ph): sp.Rational(3, 5), sp.cos(ph): sp.Rational(4, 5)}


@lru_cache(maxsize=None)
def geomP(n):
    """the same metrics in polar coordinates (t, r, angles), with the scales of gbar's orthonormal frame"""
    ang = (ch, th, ph) if n == 4 else (th, ph)
    X = (t, r) + ang
    f = 1 - mu / r**2 if n == 4 else 1 - 2 * M / r
    sph = [r**2, r**2 * sp.sin(ch)**2, r**2 * sp.sin(ch)**2 * sp.sin(th)**2] if n == 4 else \
        [r**2, r**2 * sp.sin(th)**2]
    g = sp.diag(-f, 1 / f, *sph)
    gi = sp.diag(*[sp.cancel(1 / q) for q in g.diagonal()])
    N = len(X)
    Gam = [[[sp.cancel(sum(gi[l, k] * (sp.diff(g[k, m], X[nn]) + sp.diff(g[k, nn], X[m]) - sp.diff(g[m, nn], X[k]))
                           for k in range(N)) / 2) for nn in range(N)] for m in range(N)] for l in range(N)]
    scale = [sp.Integer(1), sp.Integer(1)] + [sp.sqrt(q) for q in sph]
    return None, X, g, gi, Gam, f, scale


def orderP(e, n, pt=None):
    """the leading power of rho = 1/r of e at the generic angles (None if e vanishes there)"""
    num, den = sp.fraction(sp.cancel(sp.sympify(e).subs(TRIG if pt is None else pt)))
    if num == 0:
        return None
    return sp.degree(den, r) - sp.degree(num, r)


@lru_cache(maxsize=None)
def geomU(n, flat):
    """the metrics in retarded coordinates (u, r, angles), u = t - r*: -f du^2 - 2 du dr + r^2 (round sphere); flat:
    Minkowski, -du^2 - 2 du dr + r^2 (round sphere) with u = t-bar - r ([Hin26] (6.5): t-bar = t* + r)"""
    ang = (ch, th, ph) if n == 4 else (th, ph)
    X = (t, r) + ang                                                      # t here is u = t*
    f = sp.Integer(1) if flat else (1 - mu / r**2 if n == 4 else 1 - 2 * M / r)
    sph = [r**2, r**2 * sp.sin(ch)**2, r**2 * sp.sin(ch)**2 * sp.sin(th)**2] if n == 4 else \
        [r**2, r**2 * sp.sin(th)**2]
    g = sp.diag(0, 0, *sph)
    g[0, 0], g[0, 1], g[1, 0] = -f, -1, -1
    gi = sp.diag(0, 0, *[1 / q for q in sph])
    gi[0, 1], gi[1, 0], gi[1, 1] = -1, -1, f
    N = len(X)
    Gam = [[[sp.cancel(sum(gi[l, k] * (sp.diff(g[k, m], X[nn]) + sp.diff(g[k, nn], X[m]) - sp.diff(g[m, nn], X[k]))
                           for k in range(N)) / 2) for nn in range(N)] for m in range(N)] for l in range(N)]
    scale = [sp.Integer(1), sp.Integer(1)] + [sp.sqrt(q) for q in sph]
    return None, X, g, gi, Gam, f, scale


def G(n):
    if isinstance(n, tuple):
        return geomU(n[1], n[2]) if n[0] == "U" else geomP(n[1])
    return geom(n)


def boxU(w, key):
    """box^Ups w = 2 (delta + E^Ups) G delta* w in retarded coordinates, c = r^-1 dt (dt = du + dr/f; dt-bar = du + dr),
    E^Ups h = -gam (2 iota_(g^-1 c) h - (2/(D - 2))(1 - e) c tr h)"""
    x, X, g, gi, Gam, f, sc = G(key)
    N = len(X)
    gU, eU = sp.symbols("gamma_Ups e_Ups", positive=True)
    c = [1 / r, 1 / (r * f)] + [0] * (N - 2)
    cs = [sum(gi[a, b] * c[b] for b in range(N)) for a in range(N)]
    Gh = Gop(dstar(w, key), key)
    tr = sum(gi[a, b] * Gh[a, b] for a in range(N) for b in range(N))
    E = [-gU * (2 * sum(cs[a] * Gh[a, b] for a in range(N)) - sp.Rational(2, N - 2) * (1 - eU) * c[b] * tr)
         for b in range(N)]
    return [sp.cancel(2 * (q + e)) for q, e in zip(div(Gh, key), E)]


def order(e, n, second=False):
    """the leading power of rho = 1/R of e along the ray (None if e vanishes there): e is rational in R there (r = R)"""
    x, X, g, gi, Gam, f, ray = geom(n)
    num, den = sp.fraction(sp.cancel(sp.sympify(e).subs(ray2(n) if second else ray)))
    if num == 0:
        return None
    return sp.degree(den, R) - sp.degree(num, R)


def dstar(w, n):
    x, X, g, gi, Gam, f, ray = G(n)
    N = len(X)
    return sp.Matrix(N, N, lambda a, b: sp.cancel((sp.diff(w[b], X[a]) + sp.diff(w[a], X[b])) / 2
                                                  - sum(Gam[c][a][b] * w[c] for c in range(N))))


def div(h, n):
    """(delta h)_b = -g^ac nabla_c h_ab"""
    x, X, g, gi, Gam, f, ray = G(n)
    N = len(X)
    Dh = lambda c, a, b: (sp.diff(h[a, b], X[c]) - sum(Gam[s][c][a] * h[s, b] + Gam[s][c][b] * h[a, s]
                                                       for s in range(N)))
    return [sp.cancel(-sum(gi[a, c] * Dh(c, a, b) for a in range(N) for c in range(N))) for b in range(N)]


def Gop(h, n):
    x, X, g, gi, Gam, f, ray = G(n)
    N = len(X)
    tr = sum(gi[a, b] * h[a, b] for a in range(N) for b in range(N))
    return (h - g * tr / 2).applyfunc(sp.cancel)


def dric(h, n):
    x, X, g, gi, Gam, f, ray = G(n)
    N = len(X)
    dG = [[[sp.cancel(sum(gi[l, k] * (sp.diff(h[nn, k], X[m]) + sp.diff(h[m, k], X[nn]) - sp.diff(h[m, nn], X[k])) / 2
                          - gi[l, k] * sum(Gam[s][m][nn] * h[s, k] for s in range(N)) for k in range(N)))
            for nn in range(N)] for m in range(N)] for l in range(N)]
    tr = [sum(dG[l][l][m] for l in range(N)) for m in range(N)]
    Rm = sp.zeros(N, N)
    for m in range(N):
        for nn in range(m, N):
            e = sum(sp.diff(dG[l][m][nn], X[l]) for l in range(N))
            e += sum(Gam[l][l][s] * dG[s][m][nn] for l in range(N) for s in range(N))
            e -= sum(Gam[s][l][m] * dG[l][s][nn] + Gam[s][l][nn] * dG[l][m][s] for l in range(N) for s in range(N))
            e -= sp.diff(tr[m], X[nn]) - sum(Gam[s][nn][m] * tr[s] for s in range(N))
            Rm[m, nn] = Rm[nn, m] = sp.cancel(e)
    return Rm


def maxorder(es, n, second=False):
    """the least leading power over the nonzero entries (the order of the whole object)"""
    ps = [order(e, n, second) for e in es]
    ps = [p for p in ps if p is not None]
    return min(ps) if ps else None


# indicial roots of box^Ups(0) in five dimensions, 10.15(i): s0 lam (lam - 3)(lam^2 - lam - 2 - z); vl (lam + l)(l + 2 -
# lam); sl (l + 3 - lam)(l + lam - 1) Q, Q = s^2 - (2 + 2 kap + z) s + kap (kap + 1) + z kap, s = lam (lam - 1), kap = l
# (l + 2).  In four dimensions ([Hin26] Lemma 6.6) the s0 roots include 0 and the s1 roots include 0.
lam = sp.Symbol("lam")


def poly5(typ, l):
    if typ == "s0":
        return lam * (lam - 3) * (lam**2 - lam - 2 - z)
    if typ == "v":
        return (lam + l) * (l + 2 - lam)
    kap = l * (l + 2)
    s = lam * (lam - 1)
    return (l + 3 - lam) * (l + lam - 1) * (s**2 - (2 + 2 * kap + z) * s + kap * (kap + 1) + z * kap)


def is_root(typ, l, value, zval):
    return sp.simplify(poly5(typ, l).subs({lam: value, z: zval})) == 0


def minP(es, n, pt=None):
    """the order of an object from its frame components at the generic angles TRIG (or pt)"""
    ps = [p for p in (orderP(q, n, pt) for q in es) if p is not None]
    return min(ps) if ps else None


def frame1(w, sc):
    return [w[a] / sc[a] for a in range(len(w))]


def frame2(h, sc):
    N = len(sc)
    return [h[a, b] / (sc[a] * sc[b]) for a in range(N) for b in range(N)]


# ------------------------------------------------------------------------------------------------- Z1
def z1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    want = {4: (2, 3), 3: (1, 2)}
    ok = True
    for n in (4, 3):
        x, X, g, gi, Gam, f, ray = geom(n)
        N = n + 1
        gbar = sp.diag(-1, *([1] * n))
        dg = [g[a, b] - gbar[a, b] for a in range(N) for b in range(N)]
        Gs = [Gam[l][m][k] for l in range(N) for m in range(N) for k in range(N)]
        og, oG = maxorder(dg, n), maxorder(Gs, n)
        same = (maxorder(dg, n, True), maxorder(Gs, n, True)) == (og, oG)
        w = want[3] if control == 1 else want[n]
        ok &= (og, oG) == w and same
        chk(f"n + 1 = {n + 1}: g - gbar of order rho^{og}, Gamma - Gamma-bar of order rho^{oG}, the same on a second "
            f"ray ({same})", (og, oG) == w and same)
    rr = sp.Symbol("r", positive=True)
    rh = sp.sqrt(mu)
    rs5 = rr + rh / 2 * sp.log((rr - rh) / (rr + rh))
    rs4 = rr + 2 * M * sp.log(rr / (2 * M) - 1)
    nolog5 = sp.limit(rs5 - rr, rr, sp.oo) == 0
    log4 = sp.limit((rs4 - rr) / sp.log(rr), rr, sp.oo) == 2 * M
    chk("r* - r -> 0 in five dimensions, ~ 2M log r in four", nolog5 and log4)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z2
def z2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    key = ("P", 4)
    x, X, g, gi, Gam, f, sc = geomP(4)
    x1 = r * sp.sin(ch) * sp.sin(th) * sp.cos(ph)
    w = [sp.diff(x1, q) for q in X]                                       # dx^1
    hs = dstar(w, key)
    boxw = [2 * q for q in div(Gop(hs, key), key)]                        # box = 2 delta G delta*
    oh, ob = minP(frame2(hs, sc), 4), minP(frame1(boxw, sc), 4)
    same = (minP(frame2(hs, sc), 4, TRIG2), minP(frame1(boxw, sc), 4, TRIG2)) == (oh, ob)
    zval = 0 if control == 1 else sp.Rational(1, 100)
    root0 = is_root("s", 1, 2, 0)
    rootz = is_root("s", 1, 2, zval)
    sq = sp.sqrt(z**2 + 4 * z + 16)
    lam_s12 = (1 + sp.sqrt(17 + 2 * z - 2 * sq)) / 2                    # lam (lam - 1) = (8 + z - sq)/2
    q_ok = sp.simplify(poly5("s", 1).subs(lam, lam_s12)) == 0 and lam_s12.subs(z, 0) == 2
    q_ok &= sp.expand((4 + z)**2 - sq**2) == 4 * z                      # (8 + z - sq)/2 > 2 iff z > 0
    chk(f"delta*_g dx^1 of order rho^{oh}, box dx^1 of order rho^{ob} (the same at a second angle: {same}); 2 is an "
        f"s1 root at z = 0 ({root0}) and not at z = {zval} ({not rootz}); the root through 2 is (1 + (17 + 2 z - 2 (z^2 "
        f"+ 4 z + 16)^(1/2))^(1/2))/2, > 2 for z > 0 ({q_ok})",
        oh == 3 and ob == 4 and same and root0 and not rootz and q_ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z3
def tbar_boost(n):
    """his boost t-bar dx^1 - x^1 dt-bar, t-bar = t* + r, in retarded coordinates on g: the stationary defect K-bar =
    delta*_g B - t* delta*_g dx^1 and the stationary residual F = box^Ups_g B - t* box^Ups_g dx^1 (B Killing for gbar)"""
    key, keyb = ("U", n, False), ("U", n, True)
    x, X, g, gi, Gam, f, sc = geomU(n, False)
    Sf = sp.sin(ch) * sp.sin(th) * sp.cos(ph) if n == 4 else sp.sin(th) * sp.cos(ph)
    x1 = r * Sf
    dx1 = [sp.diff(x1, q) for q in X]
    B = [(t + r) * dx1[i] - x1 * (1 if i < 2 else 0) for i in range(len(X))]     # (u + r) dx^1 - x^1 (du + dr)
    Kb = (dstar(B, key) - t * dstar(dx1, key)).applyfunc(sp.cancel)
    Fb = [sp.cancel(p - t * q) for p, q in zip(boxU(B, key), boxU(dx1, key))]
    killing = all(sp.simplify(q) == 0 for q in dstar(B, keyb))
    stat = all(sp.diff(q, t) == 0 for q in list(Kb) + Fb)
    o = (minP(frame2(Kb, sc), n), minP(frame1(Fb, sc), n))
    same = (minP(frame2(Kb, sc), n, TRIG2), minP(frame1(Fb, sc), n, TRIG2)) == o
    return killing and stat and same, o


def z3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    for n in ((4,) if control == 0 else (3,)):
        x, X, g, gi, Gam, f, ray = geom(n)
        N = n + 1
        B = [-x[0], t] + [0] * (n - 1)                                    # t dx^1 - x^1 dt
        hB = dstar(B, n)
        h1 = dstar([0, 1] + [0] * (n - 1), n)
        K = (hB - t * h1).applyfunc(sp.cancel)
        stationary = all(not sp.diff(q, t).has(t) and sp.diff(q, t) == 0 for q in K)
        oK = maxorder(list(K), n)
        stationary &= maxorder(list(K), n, True) == oK
        good, (oKb, oF) = tbar_boost(n)
        if n == 4:
            noroot = all(not is_root("s", 1, 1, zz) for zz in (0, sp.Rational(1, 100), 1))
            noroot &= sp.simplify(poly5("s", 1).subs(lam, 1)) == 3 * (12 + 3 * z)
            res = stationary and oK == 2 and good and (oKb, oF) == (2, 3) and noroot
            chk(f"n + 1 = 5: delta*_g (t dx^1 - x^1 dt) = t delta*_g dx^1 + K, K stationary of order rho^{oK}; with his "
                f"t-bar = t* + r, K-bar of order rho^{oKb} and the residual box^Ups_g B - t* box^Ups_g dx^1 of order "
                f"rho^{oF}, B Killing for gbar; the correction at rho^1, and 1 is no s1 root of box^Ups(0) for z >= 0 "
                f"(the s1 polynomial at 1 is 3 (12 + 3 z))", res)
        else:                                                             # control: four dimensions, K of order rho
            res = stationary and oK == 2 and (oKb, oF) == (2, 3)
            chk(f"n + 1 = 4: K of order rho^{oK}, K-bar rho^{oKb}, the residual rho^{oF}: the correction at rho^0, an "
                f"s1 root there ([Hin26] Lemma 6.6)", res)
        ok &= res
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z4
def z4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    n = 4
    x, X, g, gi, Gam, f, ray = geom(n)
    N = n + 1
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    allok = True
    rows = []
    for (i, j) in pairs:
        Rbar = [0] * N                                                    # x^i dx^j - x^j dx^i, gbar-dual of a rotation
        Rbar[1 + j], Rbar[1 + i] = x[i], -x[j]
        Rg = [sp.cancel(sum(g[a, b] * Rbar[b] for b in range(N))) for a in range(N)]   # R orthogonal to x
        same = all(sp.cancel(Rg[a] - Rbar[a]) == 0 for a in range(N))
        w = [f * q for q in Rg] if (control == 1 and (i, j) == (0, 1)) else Rg       # control: f R
        allok &= same and all(q == 0 for q in dstar(w, n))
        rows.append([sp.diff(Rbar[1 + l], x[k]) for k in range(4) for l in range(4)])
    dimV = sp.Matrix(rows).rank()
    pts = [[2, 4, 5, 6], [1, 2, 4, 10], [3, 4, 0, 0], [0, 0, 3, 4]]          # S_1 = span x^i/r at four points
    dimS = sp.Matrix([[sp.Rational(u[i]) / sp.sqrt(sum(v**2 for v in u)) for i in range(4)] for u in pts]).rank()
    chk(f"the six rotations x^i dx^j - x^j dx^i: g gbar^-1 R = R and delta*_g R = 0 for each ({allok}); dim V_1 = rank "
        f"{dimV} (so(4)), dim S_1 = rank {dimS}", allok and (dimV, dimS) == (6, 4))
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z5
def z5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    n = 4 if control == 0 else 3                                         # control: four-dimensional Schwarzschild
    key = ("P", n)
    x, X, g, gi, Gam, f, sc = geomP(n)
    N = len(X)
    hmu = sp.diff(g, mu if n == 4 else M).applyfunc(sp.cancel)
    hA = sp.zeros(N, N)
    if n == 4:                                                           # (mu/r^4)(dt w + w dt), w = r^2 sin^2 chi
        hA[0, 4] = hA[4, 0] = mu * sp.sin(ch)**2 * sp.sin(th)**2 / r**2  # sin^2 theta dphi = x^1 dx^2 - x^2 dx^1
    vac = all(sp.simplify(q) == 0 for q in list(dric(hmu, key)) + list(dric(hA, key)))
    om, oA = minP(frame2(hmu, sc), n), minP(frame2(hA, sc), n)
    gU, eU = sp.symbols("gamma_Ups e_Ups", positive=True)
    c = [1 / r] + [0] * (N - 1)                                          # c = r^-1 dt; trace weight 2/(D - 2) (10.15)
    cs = [sum(gi[a, b] * c[b] for b in range(N)) for a in range(N)]

    def eta(h):                                                          # delta_(g,E) G h = delta G h + E^Ups G h
        Gh = Gop(h, key)
        tr = sum(gi[a, b] * Gh[a, b] for a in range(N) for b in range(N))
        E = [-gU * (2 * sum(cs[a] * Gh[a, b] for a in range(N)) - sp.Rational(2, n - 1) * (1 - eU) * c[b] * tr)
             for b in range(N)]
        return [sp.cancel(q + e) for q, e in zip(div(Gh, key), E)]
    dmu, dA = eta(hmu), eta(hA)
    odmu = minP(frame1(dmu, sc), n)
    same = (minP(frame2(hmu, sc), n, TRIG2), minP(frame2(hA, sc), n, TRIG2), minP(frame1(dmu, sc), n, TRIG2)) == \
        (om, oA, odmu)
    dA0 = all(sp.simplify(q) == 0 for q in div(Gop(hA, key), key))
    if n == 4:                                                           # eta(h_A) = (2 gam mu/(f r^5)) w
        wv = [0, 0, 0, 0, r**2 * sp.sin(ch)**2 * sp.sin(th)**2]
        dA0 &= all(sp.simplify(dA[a] - 2 * gU * mu / (f * r**5) * wv[a]) == 0 for a in range(N))
        dA0 &= minP(frame1(dA, sc), n) == 4 and minP(frame1(dA, sc), n, TRIG2) == 4
    s0_1 = sp.expand(poly5("s0", 0).subs(lam, 1) - 2 * (2 + z)) == 0     # 2 (2 + z) > 0 at lam = 1
    v1_2 = sp.expand(poly5("v", 1).subs(lam, 2)) == 3
    ok = vac and (om, odmu) == (2, 3) and (oA == 3 or n == 3) and same and dA0 and s0_1 and v1_2
    chk(f"n + 1 = {n + 1}: D Ric(d_mu g) = D Ric(h_A) = 0 ({vac}); orders rho^{om}, rho^{oA}; delta_(g,E) G d_mu g of "
        f"order rho^{odmu}, the same at a second angle ({same}); delta G h_A = 0 and delta_(g,E) G h_A = E^Ups h_A = (2 "
        f"gam mu/(f r^5)) w, of order rho^4 ({dA0}); the s0 polynomial at 1 is 2 (2 + z), the v1 polynomial at 2 is 3 "
        f"({s0_1 and v1_2})", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z6
def z6(control=0, verbose=False):
    """the one-spin Myers-Perry metric, [ER08] (32)-(33) at d = 5: Ricci-flat (at three exact points), Tangherlini at a =
    0 on the round S^3 dtheta^2 + sin^2 theta dphi^2 + cos^2 theta dpsi^2, and d_a g at a = 0 = -h_A"""
    chk = Checklist(verbose, quiet=control != 0)
    tt, rr, q, p_, s_ = sp.symbols("t r theta phi psi", real=True)
    a = sp.Symbol("a", positive=True)
    Y = (tt, rr, q, p_, s_)
    Sig = rr**2 + a**2 * sp.cos(q)**2
    Dl = rr**2 + a**2 - mu if control != 1 else rr**2 - mu              # control 1: a^2 dropped from Delta
    g = sp.zeros(5, 5)
    g[0, 0] = -1 + mu / Sig
    g[0, 3] = g[3, 0] = -mu * a * sp.sin(q)**2 / Sig
    g[3, 3] = mu * a**2 * sp.sin(q)**4 / Sig + (rr**2 + a**2) * sp.sin(q)**2
    g[1, 1], g[2, 2], g[4, 4] = Sig / Dl, Sig, rr**2 * sp.cos(q)**2
    N = 5
    dg = [[[sp.diff(g[i, j], Y[k]) for k in range(N)] for j in range(N)] for i in range(N)]
    flat = True
    pts = [(2, sp.Rational(1, 3), 1, sp.Rational(3, 5), sp.Rational(4, 5)),
           (3, sp.Rational(1, 2), 2, sp.Rational(5, 13), sp.Rational(12, 13)),
           (sp.Rational(5, 2), sp.Rational(2, 7), sp.Rational(3, 2), sp.Rational(8, 17), sp.Rational(15, 17))]
    for rv, av, mv, sv, cv in (pts if control != 2 else []):
        pt = {rr: rv, a: av, mu: mv, sp.sin(q): sv, sp.cos(q): cv}
        Gm = g.subs(pt)
        Gi = Gm.inv()
        D = [[[dg[i][j][k].subs(pt) for k in range(N)] for j in range(N)] for i in range(N)]
        DD = [[[[sp.diff(dg[i][j][k], Y[l]).subs(pt) for l in range(N)] for k in range(N)] for j in range(N)]
              for i in range(N)]
        dGi = [-(Gi * sp.Matrix(N, N, lambda i, j: D[i][j][m]) * Gi) for m in range(N)]
        lo = lambda k, n_, m: D[k][n_][m] + D[k][m][n_] - D[m][n_][k]
        Gam = [[[sum(Gi[l, k] * lo(k, n_, m) for k in range(N)) / 2 for n_ in range(N)] for m in range(N)]
               for l in range(N)]
        dGam = [[[[sum(dGi[pp][l, k] * lo(k, n_, m) + Gi[l, k] * (DD[k][n_][m][pp] + DD[k][m][n_][pp]
                                                                   - DD[m][n_][k][pp]) for k in range(N)) / 2
                   for pp in range(N)] for n_ in range(N)] for m in range(N)] for l in range(N)]
        for m in range(N):
            for n_ in range(N):
                Rmn = sum(dGam[l][m][n_][l] - dGam[l][m][l][n_] for l in range(N))
                Rmn += sum(Gam[l][l][s] * Gam[s][m][n_] - Gam[l][n_][s] * Gam[s][m][l]
                           for l in range(N) for s in range(N))
                flat &= sp.simplify(Rmn) == 0
    f5 = 1 - mu / rr**2
    tang = (g.subs(a, 0) - sp.diag(-f5, 1 / f5, rr**2, rr**2 * sp.sin(q)**2, rr**2 * sp.cos(q)**2)).applyfunc(
        sp.simplify) == sp.zeros(5, 5)
    ga = sp.diff(g, a).subs(a, 0).applyfunc(sp.simplify)
    w = [0, 0, 0, rr**2 * sp.sin(q)**2, 0]                                # x^1 dx^2 - x^2 dx^1
    hA = sp.Matrix(5, 5, lambda i, j: (mu / rr**4) * ((1 if i == 0 else 0) * w[j] + (1 if j == 0 else 0) * w[i]))
    lin = (ga + (hA if control != 2 else -hA)).applyfunc(sp.simplify) == sp.zeros(5, 5)   # control 2: d_a g = +h_A
    xs = [rr * sp.sin(q) * sp.cos(p_), rr * sp.sin(q) * sp.sin(p_), rr * sp.cos(q) * sp.cos(s_),
          rr * sp.cos(q) * sp.sin(s_)]
    J = sp.Matrix([[sp.diff(xi, v) for v in Y[1:]] for xi in xs])
    eucl = (J.T * J).applyfunc(sp.simplify) == sp.diag(1, rr**2, rr**2 * sp.sin(q)**2, rr**2 * sp.cos(q)**2)
    wx = [sp.simplify(xs[0] * sp.diff(xs[1], v) - xs[1] * sp.diff(xs[0], v)) for v in Y]
    chk(f"[ER08] (32)-(33) at d = 5: Ricci-flat at three exact points ({flat}); Tangherlini at a = 0 ({tang}); d_a g "
        f"at a = 0 = -h_A, w = r^2 sin^2 theta dphi ({lin}); the angles round on S^3 ({eucl}) and w = x^1 dx^2 - x^2 "
        f"dx^1 ({wx == w})", flat and tang and lin and eucl and wx == w)
    return chk.ok


CHECKS = [("Z1 the orders: g - gbar rho^2, Gamma rho^3 (four dimensions rho, rho^2); r* without a logarithm", z1, 1),
          ("Z2 the translations: delta* dx^1 rho^3, box dx^1 rho^4; 2 an s1 root of box(0), not of box^Ups(0)", z2, 1),
          ("Z3 the boosts: the stationary defect rho^2, the residual rho^3, no s1 root at 1: no logarithm", z3, 1),
          ("Z4 the rotations: all six Killing on Tangherlini; V_1 = so(4) of rank 6, S_1 of rank 4", z4, 1),
          ("Z5 the linearized metrics: vacuum, rho^2, rho^3; gauge sources rho^3, rho^4; exponents off the roots",
           z5, 1),
          ("Z6 the one-spin Myers-Perry metric: Ricci-flat, Tangherlini at a = 0, d_a g = -h_A", z6, 2)]


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
    print(f"zstates5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"zstates5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
