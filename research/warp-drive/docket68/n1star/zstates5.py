"""zstates5.py -- [Hin26] section 6.5.1 (asymptotic symmetries) and Proposition 8.9 (gauged linearized Kerr metrics) in
five dimensions: the orders at infinity of Tangherlini against Minkowski, the defects of the asymptotic translations,
boosts and rotations, the linearized Myers-Perry metrics and their gauge sources, and the exponents the constructions
need against the indicial roots of box^Ups(0) (N1STAR-PROOF.md section 10.28; ROUTES-OPEN.md 4.29; D80).  Labels:
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
mu))(x.dx)^2/r^2, reading orders along the ray x = R u, u = (2, 4, 5, 6)/9; Z2 and Z5 in polar coordinates (t, r, chi,
theta, phi), reading orders on gbar's orthonormal frame (dt, dr, r dchi, ...) at sin chi = 3/5, sin theta = 5/13, sin
phi = 8/17 -- the same orders, the two frames differing by a rotation bounded with its inverse.

  Z1 (computed, exact) The orders.  g - gbar in rho^2 C^oo and Gamma of order rho^3 (four dimensions: rho, rho^2), so
     that his Lemma 6.14 reads delta*_g(0) - delta*_gbar(0) in rho^3 Diff^0_b and box(0) - box_gbar(0) in rho^4
     Diff^2_b in five dimensions; and r* = r + (r_h/2) log((r - r_h)/(r + r_h)) has r* - r -> 0, no logarithm (four
     dimensions: r* - r ~ 2M log r).  Control: the four-dimensional orders claimed.
  Z2 (computed, exact) The translations.  delta*_g dx^1 is of order rho^3 and box dx^1 = 2 delta G delta* dx^1 of order
     rho^4 (his rho^2, rho^3), so the correction solves box^Ups(0) omega' in rho^4, omega' at rho^2: 2 is an s1 root of
     box(0) at z = 0 (the root l + 1 of 10.15(i) at l = 1) and not for z > 0, where the root through 2 is (1 + (17 + 2z
     - 2 (z^2 + 4z + 16)^(1/2))^(1/2))/2 > 2, since (4 + z)^2 - (z^2 + 4z + 16) = 4z.  Control: z = 0.
  Z3 (computed, exact) The boosts.  For B = t dx^1 - x^1 dt, delta*_g B = t delta*_g dx^1 + K with K stationary of order
     rho^2 (his rho), so the boost's stationary correction solves box^Ups(0) omega in rho^3, omega at rho^1, and 1 is
     no s1 root at any z >= 0, the s1 polynomial at 1 being 3 (12 + 3z): no logarithm.  Control: four-dimensional
     Schwarzschild, where K is of order rho, the correction at rho^0, and 0 an s1 root ([Hin26] Lemma 6.6), his log.
  Z4 (computed, exact) The rotations.  R = x^1 dx^2 - x^2 dx^1 is orthogonal to the radial direction, so g gbar^-1 R =
     R, and delta*_g R = 0: R is Killing on Tangherlini, so omega_v1(V) = V and h_v1(V) = 0 for all six rotations of
     R^4 (V_1 = so(4)), as his Remark 6.17 at a = 0; S_1, the span of x^i/r, is four-dimensional.  Control: f R, not
     Killing.
  Z5 (computed, exact) The linearized Myers-Perry metrics.  h_mu = d_mu g and h_A = (mu/r^4)(dt (x) w + w (x) dt), w =
     x^1 dx^2 - x^2 dx^1 = r^2 sin^2 chi sin^2 theta dphi, solve D Ric(h) = 0, of orders rho^2 and rho^3 (his rho,
     rho^2); the gauge source eta = delta_(g,E) G h is of order rho^3 for h_mu (s0) and, delta G h_A vanishing, eta =
     E^Ups h_A = (2 gam_Ups mu/(f r^5)) w for h_A, of order rho^4 (v1); so the gauge 1-forms solve box^Ups(0) omega =
     -2 eta at rho^1 (s0) and rho^2 (v1), and 1 is no s0 root and 2 no v1 root of box^Ups(0) (10.15(i): s0 0, 3, (1 +-
     (9 + 4z)^(1/2))/2; v1 -1, 3).  Control: four-dimensional Schwarzschild's d_M g, of order rho, its source of order
     rho^2, where his gauge 1-form sits at rho^0, an s0 root, his (8.19)'s log.

Deduced, not computed here (N1STAR-PROOF.md 10.28): [Hin26] Proposition 6.15 in five dimensions with the orders shifted
by one -- omega_b,s1(S) - d(rS) in A^((2,0) u (2 + E_ind)) and h_b,s1(S) in A^((3,0) u (3 + E_ind)) at z > 0, the
boost's correction without (6.31)'s logarithm, h_b,v1 = 0 -- and his Proposition 8.9 there, the gauge 1-forms without
(8.19)'s logarithm, g-dot^Ups(mu) in A^((2,0) u (2 + E_ind)) and g-dot^Ups(A) in A^((3,0) u (3 + E_ind)); each by his
proof, with his Lemma 6.13 in five dimensions (10.20) and the exponents above.

READ.  [Hin26] pp. 25 (section 1.4.1), 81 (Definition 4.1, (4.1)-(4.3)), 117 (Lemma 6.6), 124-127 (Lemma 6.13; section
6.5.1: Lemma 6.14, Proposition 6.15, (6.29)-(6.33), Remarks 6.16-6.17, the proof), 154-155 (Proposition 8.9 and its
proof, (8.19)-(8.20), Remark 8.10); alphaXiv, 2026-10-23.

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


r, ch, th, ph = sp.symbols("r chi theta phi", positive=True)
TRIG = {sp.sin(ch): sp.Rational(3, 5), sp.cos(ch): sp.Rational(4, 5), sp.sin(th): sp.Rational(5, 13),
        sp.cos(th): sp.Rational(12, 13), sp.sin(ph): sp.Rational(8, 17), sp.cos(ph): sp.Rational(15, 17)}


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


def orderP(e, n):
    """the leading power of rho = 1/r of e at the generic angles (None if e vanishes there)"""
    num, den = sp.fraction(sp.cancel(sp.sympify(e).subs(TRIG)))
    if num == 0:
        return None
    return sp.degree(den, r) - sp.degree(num, r)


def G(n):
    return geomP(n[1]) if isinstance(n, tuple) else geom(n)


def order(e, n):
    """the leading power of rho = 1/R of e along the ray (None if e vanishes there): e is rational in R there (r = R)"""
    x, X, g, gi, Gam, f, ray = geom(n)
    num, den = sp.fraction(sp.cancel(sp.sympify(e).subs(ray)))
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


def maxorder(es, n):
    """the least leading power over the nonzero entries (the order of the whole object)"""
    ps = [order(e, n) for e in es]
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


# ------------------------------------------------------------------------------------------------- Z1
def z1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    want = {4: (2, 3), 3: (1, 2)}
    ok = True
    for n in (4, 3):
        x, X, g, gi, Gam, f, ray = geom(n)
        N = n + 1
        gbar = sp.diag(-1, *([1] * n))
        og = maxorder([g[a, b] - gbar[a, b] for a in range(N) for b in range(N)], n)
        oG = maxorder([Gam[l][m][k] for l in range(N) for m in range(N) for k in range(N)], n)
        w = want[3] if control == 1 else want[n]
        ok &= (og, oG) == w
        chk(f"n + 1 = {n + 1}: g - gbar of order rho^{og}, Gamma - Gamma-bar of order rho^{oG}", (og, oG) == w)
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
    N = len(X)
    x1 = r * sp.sin(ch) * sp.sin(th) * sp.cos(ph)
    w = [sp.diff(x1, q) for q in X]                                       # dx^1
    hs = dstar(w, key)
    oh = min(p for p in (orderP(hs[a, b] / (sc[a] * sc[b]), 4) for a in range(N) for b in range(N)) if p is not None)
    boxw = [2 * q for q in div(Gop(hs, key), key)]                        # box = 2 delta G delta*
    ob = min(p for p in (orderP(boxw[a] / sc[a], 4) for a in range(N)) if p is not None)
    zval = 0 if control == 1 else sp.Rational(1, 100)
    root0 = is_root("s", 1, 2, 0)
    rootz = is_root("s", 1, 2, zval)
    sq = sp.sqrt(z**2 + 4 * z + 16)
    lam_s12 = (1 + sp.sqrt(17 + 2 * z - 2 * sq)) / 2                    # lam (lam - 1) = (8 + z - sq)/2
    q_ok = sp.simplify(poly5("s", 1).subs(lam, lam_s12)) == 0 and lam_s12.subs(z, 0) == 2
    q_ok &= sp.expand((4 + z)**2 - sq**2) == 4 * z                      # (8 + z - sq)/2 > 2 iff z > 0
    chk(f"delta*_g dx^1 of order rho^{oh}, box dx^1 of order rho^{ob}; 2 is an s1 root at z = 0 ({root0}) and not at z "
        f"= {zval} ({not rootz}); the root through 2 is (1 + (17 + 2 z - 2 (z^2 + 4 z + 16)^(1/2))^(1/2))/2, > 2 for "
        f"z > 0 ({q_ok})",
        oh == 3 and ob == 4 and root0 and not rootz and q_ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z3
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
        if n == 4:
            noroot = all(not is_root("s", 1, 1, zz) for zz in (0, sp.Rational(1, 100), 1))
            noroot &= sp.simplify(poly5("s", 1).subs(lam, 1)) == 3 * (12 + 3 * z)
            ok &= stationary and oK == 2 and noroot
            chk(f"n + 1 = 5: delta*_g (t dx^1 - x^1 dt) = t delta*_g dx^1 + K, K stationary of order rho^{oK}; the "
                f"correction at rho^1, and 1 is no s1 root of box^Ups(0) for z >= 0 (the s1 polynomial at 1 is 3 (12 + "
                f"3 z))", stationary and oK == 2 and noroot)
        else:                                                             # control: four dimensions, K of order rho
            ok &= stationary and oK == 2
            chk(f"n + 1 = 4: K of order rho^{oK}, the correction at rho^0, an s1 root there ([Hin26] Lemma 6.6)",
                stationary and oK == 2)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Z4
def z4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    n = 4
    x, X, g, gi, Gam, f, ray = geom(n)
    N = n + 1
    Rbar = [0, -x[1], x[0], 0, 0]                                         # x^1 dx^2 - x^2 dx^1, gbar-dual of a rotation
    vec = [0] + Rbar[1:]                                                  # the rotation vector field's components
    Rg = [sp.cancel(sum(g[a, b] * vec[b] for b in range(N))) for a in range(N)]
    same = all(sp.cancel(Rg[a] - Rbar[a]) == 0 for a in range(N))        # R orthogonal to x: g- and gbar-duals agree
    w = [f * q for q in Rg] if control == 1 else Rg                       # control: f R
    killing = all(q == 0 for q in dstar(w, n))
    dims = (len([(i, j) for i in range(4) for j in range(i + 1, 4)]), 4)
    chk(f"R = x^1 dx^2 - x^2 dx^1: g gbar^-1 R = R ({same}), and R is Killing (delta*_g R = 0); dim V_1 = {dims[0]} "
        f"(so(4)), dim S_1 = {dims[1]}", same and killing and dims == (6, 4))
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
    fr2 = lambda h: [h[a, b] / (sc[a] * sc[b]) for a in range(N) for b in range(N)]
    fr1 = lambda w: [w[a] / sc[a] for a in range(N)]
    om = min(p for p in (orderP(q, n) for q in fr2(hmu)) if p is not None)
    oA = min((p for p in (orderP(q, n) for q in fr2(hA)) if p is not None), default=None)
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
    odmu = min(p for p in (orderP(q, n) for q in fr1(dmu)) if p is not None)
    dA0 = all(sp.simplify(q) == 0 for q in div(Gop(hA, key), key))
    if n == 4:                                                           # eta(h_A) = (2 gam mu/(f r^5)) w
        wv = [0, 0, 0, 0, r**2 * sp.sin(ch)**2 * sp.sin(th)**2]
        dA0 &= all(sp.simplify(dA[a] - 2 * gU * mu / (f * r**5) * wv[a]) == 0 for a in range(N))
        dA0 &= min(p for p in (orderP(q, n) for q in fr1(dA)) if p is not None) == 4
    s0_1 = not any(is_root("s0", 0, 1, zz) for zz in (0, sp.Rational(1, 100), 1))
    v1_2 = not is_root("v", 1, 2, 0) and not any(is_root("v", 1, 2, zz) for zz in (sp.Rational(1, 100), 1))
    ok = vac and (om, odmu) == (2, 3) and (oA == 3 or n == 3) and dA0 and s0_1 and v1_2
    chk(f"n + 1 = {n + 1}: D Ric(d_mu g) = D Ric(h_A) = 0 ({vac}); orders rho^{om}, rho^{oA}; delta_(g,E) G d_mu g of "
        f"order rho^{odmu}; delta G h_A = 0 and delta_(g,E) G h_A = E^Ups h_A = (2 gam mu/(f r^5)) w, of order rho^4 "
        f"({dA0}); 1 no s0 root ({s0_1}), 2 no v1 root ({v1_2}) of box^Ups(0)", ok)
    return chk.ok


CHECKS = [("Z1 the orders: g - gbar rho^2, Gamma rho^3 (four dimensions rho, rho^2); r* without a logarithm", z1, 1),
          ("Z2 the translations: delta* dx^1 rho^3, box dx^1 rho^4; 2 an s1 root of box(0), not of box^Ups(0)", z2, 1),
          ("Z3 the boosts: the stationary defect rho^2, the correction at rho^1, no s1 root at 1: no logarithm", z3, 1),
          ("Z4 the rotations: Killing on Tangherlini; V_1 = so(4) six-dimensional, S_1 four-dimensional", z4, 1),
          ("Z5 the linearized metrics: vacuum, rho^2, rho^3; gauge sources rho^3, rho^4; exponents off the roots", z5, 1)]


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
