#!/usr/bin/env python3
"""genstates5.py -- [Hin26] Proposition 6.18 (1)-(3) in five dimensions: the generalized zero energy states of box^Ups
built on the time translation, the translations and boosts, and the rotations, and the indicial gap of his Lemma 6.13
(N1STAR-PROOF.md section 10.29; ROUTES-OPEN.md 4.30; D81).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 6.18 builds generalized zero energy states, polynomials in t*, whose symmetric
gradients carry the roots of L-hat(0) that are not stationary pure gauge: (1) the s0 root 0, h_s0^(0) = delta*(t*
omega_s0 + omega-breve^(0),1_s0), the correction in A^((-1,0) u (0,1) u (1 + E_ind)), "with s0 leading- and
sub-leading- order term" in its source; (2) the s1 root -1, the boost carried to second order, t*^2 omega_s1 + 2 t*
omega-breve^1 + 2 omega-breve^2, its leading term h-bar^2_s1 stationary; (3) the v1 root -1, t* V + omega-breve^1_v1,
his (6.40): omega-breve-bar^1_v1 = rho^-2 (0, 0, (1 + gam/2) rho V) and h-bar^1_v1 = (1/4)(0, 0, (1 + gam/2) V, 0, (1 -
gam/2) V, 0) in his splitting (2.37b) on d xbar^0, d xbar^1, r T*S^2 (xbar^0 = t + r, xbar^1 = t - r = t*).  Here on 4+1
Minkowski, with E^Ups at the trace weight 2/3 and c = r^-1 dt (10.15), in polar coordinates (t, r, chi, theta, phi),
and on five-dimensional Tangherlini, f = 1 - mu/r^2, for part (1)'s source; four-dimensional Minkowski and
Schwarzschild (trace weight 1) are the control, reproducing his printed numbers.

  H1 (computed, exact) Part (1).  On Minkowski, t* omega-bar + W, omega-bar = -dt, W = r(-dt + b dr), b = (2 - e)/(4 e)
     (four dimensions (2 - e)/(3 e)), solves box^Ups = 0; h-bar^(0)_s0 = delta*(t* omega-bar + W) is stationary,
     nonzero, of degree 0, (a, b, e, p) = (2 - 5e, -(2 + 3e), 2 - 5e, 4 (2 - e))/(16 e), and in the kernels of D Ric
     and of the gauge operator.  On Tangherlini the source box^Ups(t* omega_s0) = 2 delta_(g,E) G (dt* (x)_s omega_s0),
     omega_s0 = -f dt, has the rho^1 term (2 e gam - 4 gam - 3, 2 gam) on (dt, dr), no rho^2 term, and the rho^3 term
     (mu, 2 mu (gam + 1)), so that (deduced, with zstates5.py Z1's orders) the correction is rho^-1 W + O(rho), with no
     log rho -- four dimensions: the rho^2 term (2M, 2M (2 gam + 1)), his sub-leading term and his log.  -1, -2, -3, -4
     are no s0 roots for z > 0.  Control: the five-dimensional claim (no rho^2 term) on Schwarzschild.
  H2 (computed, exact) Part (2).  On Minkowski, t*^2 dx^1 + 2 t* B + 2 W, B = r d(rS) - rS dt, S = x^1/r, W = r^2
     (alpha S d(t + r) + beta S d(t - r)) + kappa r^3 dS, (alpha, beta, kappa) = (4 - 7e, -(4 + 17e), (2/3)(25e - 4))/(24
     e), solves box^Ups = 0; h-bar^2_s1 = dt* (x)_s B + delta* W is stationary, nonzero, of degree -1, and in both
     kernels.  -2, -3, -4 are no s1 roots for z > 0; -2 is one at z = 0.  Control: the factor 2 on B dropped, where no W
     exists.
  H3 (computed, exact) Part (3).  On Minkowski, t* V + kappa r V, V = r^2 sin^2 chi sin^2 theta dphi = x^1 dx^2 - x^2
     dx^1, solves box^Ups = 0 exactly at kappa = 1 + 2 gam/5, and h-bar^1_v1 = (1/4)(0, 0, (1 + 2 gam/5) V, 0, (1 - 2
     gam/5) V, 0), stationary and in both kernels: his (6.40) in five dimensions.  -2, -3, -4 are no v1 roots.  Control:
     his kappa = 1 + gam/2 in five dimensions.
  H4 (computed, exact) The four-dimensional control.  dt* (x)_s omega-bar = (0, -1/4, -1/2, 0) at s0 and dt* (x)_s B =
     rho^-1 (0, 0, 0, -1, 1/2) S at s1 in his splitting (pp. 132-133), and kappa = 1 + gam/2 with h-bar^1_v1 = (1/4)(1 +
     gam/2, 1 - gam/2) rho^-1, his (6.40) (p. 134); the same two splittings in five dimensions.  Control: the
     five-dimensional kappa claimed in four.
  H5 (computed, exact) Lemma 6.13's indicial gap.  The s1 root through 2 and the s0 root through 2 of box^Ups(0) (10.15)
     are 2 + z/12 + O(z^2) and 2 + z/3 + O(z^2), and lam_s1,2 < lam_s0 for 0 < z < 4 (4 - z < (z^2 + 4z + 16)^(1/2)), his
     (6.17b); so the exponents 1 and 2 of 10.28 lie in the gap (0, lam_s1,2) for z > 0, 2 at its edge at z = 0.
     Control: z = 0.

Deduced, not computed here (N1STAR-PROOF.md 10.29): his Lemma 6.13 in five dimensions, from 10.12(i)'s gap, 10.20's
Fredholm property, index 0 and mode stability at sigma = 0, and his Lemma 2.13; his Proposition 6.18 (1)-(3) there, with
the corrections at rho^-1 (s0), rho^-2 (s1 and v1) and part (1) without his log, the six rotations Killing on
Tangherlini so that h^(<=1)_v1 is stationary for each (his Remark 6.19 at a = 0).

READ.  [Hin26] pp. 51-52 (Lemmas 2.13 and 2.15), 64-67 (Definition 2.28, (2.37b), Lemma 2.29, (2.43)-(2.46)), 81
(Definition 4.1 and its remark on e_Ups), 113 (section 6, Lemma 6.1), 117-119 (Lemma 6.6, (6.17a)-(6.17b), Lemma 6.8,
(6.20)), 121 (Proposition 6.12), 124-125 (Lemma 6.13), 128-134 (section 6.5.2: Proposition 6.18, Remark 6.19 and the
proof); alphaXiv, 2026-10-23.

sympy.  python3 genstates5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time
from functools import lru_cache

import sympy as sp

from damping5 import Checklist
from zstates5 import is_root, poly5, lam, z

t = sp.Symbol("t", real=True)
r, ch, th, ph = sp.symbols("r chi theta phi", positive=True)
mu, M = sp.symbols("mu M", positive=True)
gU, eU = sp.symbols("gamma_Ups e_Ups", positive=True)
TRIG = {sp.sin(ch): sp.Rational(3, 5), sp.cos(ch): sp.Rational(4, 5), sp.sin(th): sp.Rational(5, 13),
        sp.cos(th): sp.Rational(12, 13), sp.sin(ph): sp.Rational(8, 17), sp.cos(ph): sp.Rational(15, 17)}


@lru_cache(maxsize=None)
def geo(n, flat):
    """polar coordinates (t, r, angles) on Tangherlini (n = 4) or Schwarzschild (n = 3); flat: Minkowski"""
    ang = (ch, th, ph) if n == 4 else (th, ph)
    X = (t, r) + ang
    f = sp.Integer(1) if flat else (1 - mu / r**2 if n == 4 else 1 - 2 * M / r)
    sph = [r**2, r**2 * sp.sin(ch)**2, r**2 * sp.sin(ch)**2 * sp.sin(th)**2] if n == 4 else \
        [r**2, r**2 * sp.sin(th)**2]
    g = sp.diag(-f, 1 / f, *sph)
    gi = sp.diag(*[sp.cancel(1 / q) for q in g.diagonal()])
    N = len(X)
    Gam = [[[sp.cancel(sum(gi[l, k] * (sp.diff(g[k, m], X[nn]) + sp.diff(g[k, nn], X[m]) - sp.diff(g[m, nn], X[k]))
                           for k in range(N)) / 2) for nn in range(N)] for m in range(N)] for l in range(N)]
    return X, g, gi, Gam, f


def dstar(w, G):
    X, g, gi, Gam, f = G
    N = len(X)
    return sp.Matrix(N, N, lambda a, b: (sp.diff(w[b], X[a]) + sp.diff(w[a], X[b])) / 2
                     - sum(Gam[c][a][b] * w[c] for c in range(N)))


def div(h, G):
    """(delta h)_b = -g^ac nabla_c h_ab"""
    X, g, gi, Gam, f = G
    N = len(X)
    Dh = lambda c, a, b: (sp.diff(h[a, b], X[c]) - sum(Gam[s][c][a] * h[s, b] + Gam[s][c][b] * h[a, s]
                                                       for s in range(N)))
    return [-sum(gi[a, c] * Dh(c, a, b) for a in range(N) for c in range(N)) for b in range(N)]


def trace(h, G):
    X, g, gi, Gam, f = G
    return sum(gi[a, b] * h[a, b] for a in range(len(X)) for b in range(len(X)))


def Gop(h, G):
    X, g, gi, Gam, f = G
    return h - g * trace(h, G) / 2


def Eups(h, G):
    """E^Ups h = -gam (2 iota_(g^-1 c) h - w (1 - e) c tr h), c = r^-1 dt, w = 2/(D - 2) (10.15; his 1 at D = 4)"""
    X, g, gi, Gam, f = G
    N = len(X)
    wgt = sp.Rational(2, N - 2)
    c = [1 / r] + [0] * (N - 1)
    cs = [sum(gi[a, b] * c[b] for b in range(N)) for a in range(N)]
    tr = trace(h, G)
    return [-gU * (2 * sum(cs[a] * h[a, b] for a in range(N)) - wgt * (1 - eU) * c[b] * tr) for b in range(N)]


def boxU(w, G):
    """box^Ups w = 2 (delta + E^Ups) G delta* w"""
    Gh = Gop(dstar(w, G), G)
    return [2 * (q + e) for q, e in zip(div(Gh, G), Eups(Gh, G))]


def dric(h, G):
    X, g, gi, Gam, f = G
    N = len(X)
    dG = [[[sum(gi[l, k] * (sp.diff(h[nn, k], X[m]) + sp.diff(h[m, k], X[nn]) - sp.diff(h[m, nn], X[k])) / 2
                - gi[l, k] * sum(Gam[s][m][nn] * h[s, k] for s in range(N)) for k in range(N))
             for nn in range(N)] for m in range(N)] for l in range(N)]
    tr = [sum(dG[l][l][m] for l in range(N)) for m in range(N)]
    Rm = sp.zeros(N, N)
    for m in range(N):
        for nn in range(m, N):
            e = sum(sp.diff(dG[l][m][nn], X[l]) for l in range(N))
            e += sum(Gam[l][l][s] * dG[s][m][nn] for l in range(N) for s in range(N))
            e -= sum(Gam[s][l][m] * dG[l][s][nn] + Gam[s][l][nn] * dG[l][m][s] for l in range(N) for s in range(N))
            e -= sp.diff(tr[m], X[nn]) - sum(Gam[s][nn][m] * tr[s] for s in range(N))
            Rm[m, nn] = Rm[nn, m] = e
    return Rm


def zero(e):
    return sp.simplify(sp.cancel(sp.together(sp.sympify(e)))) == 0


def at_pt(e):
    return sp.cancel(sp.together(sp.sympify(e).subs(TRIG)))


def solve_coeffs(exprs, unknowns, polyvars=(r, t)):
    """the unknowns making every expression vanish identically in r and t at the generic angles"""
    eqs = []
    for e in exprs:
        num = sp.numer(sp.together(at_pt(e)))
        if num == 0:
            continue
        eqs += sp.Poly(sp.expand(num), *polyvars).coeffs()
    sol = sp.solve(eqs, unknowns, dict=True)
    return sol


def split1(w, G):
    """1-form components (omega_0, omega_1) on d xbar^0, d xbar^1, xbar^0 = t + r, xbar^1 = t - r ([Hin26] (2.37b))"""
    return [sp.cancel((w[0] + w[1]) / 2), sp.cancel((w[0] - w[1]) / 2)]


def split2(h, G, A):
    """2-tensor components a = h(e0, e0), b = h(e0, e1), h(e0, d_A)/r, e = h(e1, e1), h(e1, d_A)/r, e0 = (d_t + d_r)/2,
    e1 = (d_t - d_r)/2 ([Hin26] (2.37b): h = a dx0^2 + 2 b dx0 dx1 + 2 dx0 (x)_s r c + e dx1^2 + 2 dx1 (x)_s r f
    + ...)"""
    e0 = [sp.Rational(1, 2), sp.Rational(1, 2)]
    e1 = [sp.Rational(1, 2), -sp.Rational(1, 2)]
    hv = lambda u, v: sum(u[i] * v[j] * h[i, j] for i in range(2) for j in range(2))
    hA = lambda u: sum(u[i] * h[i, A] for i in range(2))
    return [sp.cancel(q) for q in (hv(e0, e0), hv(e0, e1), hA(e0) / r, hv(e1, e1), hA(e1) / r)]


def tang_source(n):
    """box^Ups(t* omega_s0) = 2 (delta + E) G (dt* (x)_s omega_s0) on Tangherlini / Schwarzschild, by powers of 1/r"""
    G = geo(n, False)
    X, g, gi, Gam, f = G
    N = len(X)
    dts, om = [1, -1 / f] + [0] * (N - 2), [-f, 0] + [0] * (N - 2)
    hh = sp.Matrix(N, N, lambda i, j: (dts[i] * om[j] + dts[j] * om[i]) / 2)
    Gh = Gop(hh, G)
    F = [sp.cancel(2 * (q + e)) for q, e in zip(div(Gh, G), Eups(Gh, G))]
    rho = sp.Symbol("rho", positive=True)
    ser = [sp.series(F[i].subs(r, 1 / rho), rho, 0, 4).removeO() for i in range(2)]
    return [[sp.factor(q.coeff(rho, k)) for q in ser] for k in range(4)], all(zero(q) for q in F[2:])


def kernels(h, G):
    return all(zero(q) for q in dric(h, G)) and all(zero(q + e) for q, e in zip(div(Gop(h, G), G), Eups(Gop(h, G), G)))


def stationary(h):
    return all(zero(sp.diff(q, t)) for q in h)


def part1(n):
    G = geo(n, True)
    N = len(G[0])
    a, b = sp.symbols("a b")
    w = [-(t - r) + a * r, b * r] + [0] * (N - 2)
    sol = solve_coeffs(boxU(w, G), [a, b])
    if len(sol) != 1:
        return None
    wv = [sp.sympify(q).subs(sol[0]) for q in w]
    h = dstar(wv, G).applyfunc(sp.cancel)
    hd = dstar([-(t - r), 0] + [0] * (N - 2), G).applyfunc(sp.cancel)
    sd, sh = split2(hd, G, 2), split2(h, G, 2)
    return dict(sol=sol[0], box=all(zero(q) for q in boxU(wv, G)), stat=stationary(h), ker=kernels(h, G),
                hd=[sd[0], sd[1], sd[3], sp.cancel(hd[2, 2] / r**2)],
                hb=[sp.factor(q) for q in (sh[0], sh[1], sh[3], sp.cancel(h[2, 2] / r**2))])


def part2(n, factor=2):
    G = geo(n, True)
    X = G[0]
    N = len(X)
    al, be, ka = sp.symbols("alpha beta kappa")
    Sf = sp.sin(ch) * sp.sin(th) * sp.cos(ph) if n == 4 else sp.sin(th) * sp.cos(ph)
    dx1 = [sp.diff(r * Sf, q) for q in X]
    B = [r * dx1[i] - (r * Sf if i == 0 else 0) for i in range(N)]
    dS = [sp.diff(Sf, q) for q in X]
    W = [r**2 * (al + be) * Sf, r**2 * (al - be) * Sf] + [ka * r**3 * dS[i] for i in range(2, N)]
    w = [(t - r)**2 * dx1[i] + factor * (t - r) * B[i] + 2 * W[i] for i in range(N)]
    sol = solve_coeffs(boxU(w, G), [al, be, ka])
    if len(sol) != 1:
        return None
    wv = [sp.sympify(q).subs(sol[0]) for q in w]
    h = (dstar(wv, G) / 2).applyfunc(sp.cancel)
    hd = (dstar([(t - r) * q for q in B], G) - (t - r) * dstar(B, G)).applyfunc(sp.cancel)
    A = N - 1
    norm = [r * Sf, r * Sf, r * dS[A], r * Sf, r * dS[A]]
    return dict(sol={k: sp.factor(v) for k, v in sol[0].items()}, box=all(zero(q) for q in boxU(wv, G)),
                stat=stationary(h), ker=kernels(h, G), nonzero=not all(zero(q) for q in h),
                hd=[sp.simplify(q / m) for q, m in zip(split2(hd, G, A), norm)])


def part3(n, kappa=None):
    G = geo(n, True)
    N = len(G[0])
    VS = sp.sin(ch)**2 * sp.sin(th)**2 if n == 4 else sp.sin(th)**2
    V = [0] * (N - 1) + [r**2 * VS]
    k = sp.Symbol("kappa")
    w = [(t - r) * q + k * r * q for q in V]
    if kappa is None:
        sol = solve_coeffs(boxU(w, G), [k])
        if len(sol) != 1:
            return None
        kappa = sol[0][k]
    wv = [q.subs(k, kappa) for q in w]
    box = all(zero(q) for q in boxU(wv, G))
    h = dstar(wv, G).applyfunc(sp.cancel)
    sp2 = split2(h, G, N - 1)
    return dict(kappa=sp.expand(kappa), box=box, stat=stationary(h), ker=kernels(h, G),
                hb=[sp.expand(sp.simplify(q)) for q in (sp2[0], sp2[1], sp2[2] / (r * VS), sp2[3], sp2[4] / (r * VS))])


def not_roots(typ, l, values, zs):
    return all(not is_root(typ, l, v, zz) for v in values for zz in zs)


ZS = (sp.Rational(1, 100), sp.Rational(1, 2), 1)
e = eU


# ------------------------------------------------------------------------------------------------- H1
def h1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    if control == 0:
        P = part1(4)
        okm = P is not None and P["sol"] == {sp.Symbol("a"): -1, sp.Symbol("b"): (2 - e) / (4 * e)} and P["box"] \
            and P["stat"] and P["ker"]
        want = [(2 - 5 * e) / (16 * e), -(2 + 3 * e) / (16 * e), (2 - 5 * e) / (16 * e), (2 - e) / (4 * e)]
        okm &= all(zero(x - y) for x, y in zip(P["hb"], want))
        chk(f"Minkowski: W = r(-dt + b dr), b = {P['sol'][sp.Symbol('b')]}; h-bar^(0)_s0 (a, b, e, p) = {P['hb']}, "
            f"stationary, in both kernels", okm)
    n = 4 if control == 0 else 3
    co, ang = tang_source(n)
    gm = gU
    if n == 4:
        oks = co[0] == [0, 0] and co[2] == [0, 0] and all(q != 0 for q in co[1]) and ang
        oks &= zero(co[1][0] - (2 * e * gm - 4 * gm - 3)) and zero(co[1][1] - 2 * gm)
        oks &= zero(co[3][0] - mu) and zero(co[3][1] - 2 * mu * (gm + 1))
    else:                                                                # control: the five-dimensional claim
        oks = co[0] == [0, 0] and co[2] == [0, 0] and ang
    chk(f"n + 1 = {n + 1}: the source on (dt, dr) by powers of rho: rho^1 {co[1]}, rho^2 {co[2]}, rho^3 {co[3]}; "
        f"no rho^2 term", oks)
    okr = not_roots("s0", 0, (-1, -2, -3, -4), ZS)
    if control == 0:
        chk("-1, -2, -3, -4 are no s0 roots of box^Ups(0) for z > 0", okr)
    return chk.ok


# ------------------------------------------------------------------------------------------------- H2
def h2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    P = part2(4, factor=2 if control == 0 else 1)
    al, be, ka = sp.symbols("alpha beta kappa")
    ok = P is not None
    if ok:
        want = {al: (4 - 7 * e) / (24 * e), be: -(4 + 17 * e) / (24 * e), ka: (25 * e - 4) / (36 * e)}
        ok = all(zero(P["sol"][k] - v) for k, v in want.items()) and P["box"] and P["stat"] and P["ker"] \
            and P["nonzero"]
    chk(f"Minkowski: t*^2 dx^1 + 2 t* B + 2 W solves box^Ups = 0 with (alpha, beta, kappa) = "
        f"{None if P is None else P['sol']}; h-bar^2_s1 stationary, nonzero, in both kernels", ok)
    okr = not_roots("s", 1, (-2, -3, -4), ZS) and is_root("s", 1, -2, 0)
    chk("-2, -3, -4 are no s1 roots of box^Ups(0) for z > 0; -2 is one at z = 0", okr)
    return chk.ok


# ------------------------------------------------------------------------------------------------- H3
def h3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    P = part3(4, kappa=None if control == 0 else 1 + gU / 2)
    ok = P is not None and P["box"] and zero(P["kappa"] - (1 + 2 * gU / 5)) and P["stat"] and P["ker"]
    ok = ok and all(zero(x - y) for x, y in zip(P["hb"], [0, 0, (1 + 2 * gU / 5) / 4, 0, (1 - 2 * gU / 5) / 4]))
    chk(f"Minkowski: t* V + kappa r V solves box^Ups = 0 at kappa = {None if P is None else P['kappa']}; h-bar^1_v1 = "
        f"(a, b, c rho, e, f rho) {None if P is None else P['hb']}, stationary, in both kernels", ok)
    okr = not_roots("v", 1, (-2, -3, -4), ZS + (0,))
    chk("-2, -3, -4 are no v1 roots of box^Ups(0)", okr)
    return chk.ok


# ------------------------------------------------------------------------------------------------- H4
def h4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    P1, P2 = part1(3), part2(3)
    P3 = part3(3, kappa=None if control == 0 else 1 + 2 * gU / 5)
    q = sp.Rational(1, 4)
    ok1 = P1["hd"] == [0, -q, -2 * q, 0] and P1["box"] and P1["ker"]
    ok2 = P2["hd"] == [0, 0, 0, -1, sp.Rational(1, 2)] and P2["box"] and P2["ker"]
    ok3 = P3["box"] and zero(P3["kappa"] - (1 + gU / 2))
    ok3 = ok3 and all(zero(x - y) for x, y in zip(P3["hb"], [0, 0, q * (1 + gU / 2), 0, q * (1 - gU / 2)]))
    chk(f"n + 1 = 4: dt* (x)_s omega-bar = {P1['hd']}, dt* (x)_s B = {P2['hd']} rho^-1 S, his pp. 132-133; kappa = "
        f"{P3['kappa']}, h-bar^1_v1 = {P3['hb']}, his (6.40)", ok1 and ok2 and ok3)
    if control == 0:
        P1b, P2b = part1(4), part2(4)
        ok5 = P1b["hd"] == [0, -q, -2 * q, 0] and P2b["hd"] == [0, 0, 0, -1, sp.Rational(1, 2)]
        chk("n + 1 = 5: the same two splittings", ok5)
    return chk.ok


# ------------------------------------------------------------------------------------------------- H5
def h5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    zz = sp.Symbol("z", positive=True)
    sq = sp.sqrt(zz**2 + 4 * zz + 16)
    l1 = (1 + sp.sqrt(17 + 2 * zz - 2 * sq)) / 2
    l0 = (1 + sp.sqrt(9 + 4 * zz)) / 2
    roots = sp.simplify(poly5("s", 1).subs({lam: l1, z: zz})) == 0 and sp.simplify(poly5("s0", 0).subs({lam: l0,
                                                                                                        z: zz})) == 0
    ser = sp.series(l1, zz, 0, 2).removeO() == 2 + zz / 12 and sp.series(l0, zz, 0, 2).removeO() == 2 + zz / 3
    order = sp.expand(sq**2 - (4 - zz)**2) == 12 * zz                    # lam_s1,2 < lam_s0 iff 4 - z < sq
    zv = sp.Rational(1, 100) if control == 0 else 0
    gap = all(0 < x < l1.subs(zz, zv) for x in (1, 2))
    chk(f"lam_s1,2 = 2 + z/12 + O(z^2) < lam_s0 = 2 + z/3 + O(z^2) for 0 < z < 4; the exponents 1, 2 in (0, "
        f"lam_s1,2) at z = {zv}", roots and ser and order and gap)
    return chk.ok


CHECKS = [("H1 part (1): the s0 state, W at rho^-1, the Tangherlini source without a rho^2 term: no log", h1, 1),
          ("H2 part (2): the boost to second order, W at rho^-2, h-bar^2_s1 stationary; -2 a root only at z = 0", h2, 1),
          ("H3 part (3): the rotation's state, kappa = 1 + 2 gam/5, h-bar^1_v1 his (6.40) in five dimensions", h3, 1),
          ("H4 the four-dimensional control: his (0, -1/4, -1/2, 0), (0, 0, 0, -1, 1/2), kappa and (6.40)", h4, 1),
          ("H5 Lemma 6.13's gap: lam_s1,2 = 2 + z/12 < lam_s0 = 2 + z/3; the exponents 1, 2 inside it", h5, 1)]


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
    print(f"genstates5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"genstates5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
