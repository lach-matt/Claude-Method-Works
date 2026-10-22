#!/usr/bin/env python3
"""solv5.py -- the five-dimensional inputs of [Hin26a] Theorem 5.2, the solvability of the constraint propagation
operator on weighted 3b-spaces, that 10.13 and 10.14 did not compute: the 3sc structure of Tangherlini, the geometry
of his energy estimates near X and Sigma#, and his Proposition 5.1 (4)-(5) at the weights of 10.21 (N1STAR-PROOF.md
section 10.22; ROUTES-OPEN.md 4.23; D67).  Labels: computed (exact, sympy), deduced, READ.

[Hin26a] (arXiv:2606.27658v2) proves Theorem 5.2 by: Lemma 5.3, h^2 box_g in h^2 rho^2 Diff^2_3b and L in h rho^2
Diff^1_3b, from (2.12)-(2.14) -- the Christoffel symbols of a 3sc-metric lie in rho_sf C^oo -- and c in rho_sf C^oo;
elliptic estimates and estimates at fiber infinity (Propositions 5.5-5.6, from Lemmas 3.5 and 3.7); propagation at
the three critical sets of -r c# and between them (Propositions 5.8, 5.9, 5.11, 5.12, from his Proposition 5.1); energy
estimates near the initial surface X = {t = 0} and the final surface Sigma# = {r = m} inside the black hole
(Proposition 5.16, from Lemma 5.14 and Corollary 5.15, stated on R^(1+n) and for n-dimensional manifolds of bounded
geometry, p. 59-60), which ask that d tau, tau = t/r, be past timelike for g_3b = rho^2 g on tau in [0, T], and that m
- r be a time function near Sigma#; and the combination of section 5.2.7.  10.13 computed his section 3 and 4 inputs in
five dimensions, 10.14 a c on Tangherlini with his Proposition 5.1 (1)-(6), (4)-(5) at the four-dimensional weights (1,
-102).  Tangherlini in Kerr-Schild time is g = eta + mu r^-2 k (x) k, k = dt + dr ((10.48)), mu = 1, r_h = 1, m = r_h/2.

  Q1 (computed, exact; what follows "so" is deduced) In Cartesian coordinates (t, x_1, ..., x_4) of 4+1 dimensions, g^-1
     = eta^-1 - mu r^-2 k# (x) k# exactly (k is null for eta); the Christoffel symbols are polynomials in mu of degree 2
     with no constant term and satisfy Gamma(lam x; mu) = lam^-1 Gamma(x; mu lam^-2), so Gamma lies in mu rho^3 C^oo(S^3
     x [0, 4]_(mu rho^2)), mu rho^2 = 4 at r = m = r_h/2, in rho_sf C^oo with two powers to spare: (2.12) and hence
     (2.14) and Lemma 5.3 hold, and c = r^-1 (dt - v dr) has the Cartesian components r^-1 (1, -v x/r), in rho_sf C^oo.
     Four-dimensional control: Schwarzschild, 2m r^-1 in place of mu r^-2, with Gamma(lam x; m) = lam^-1 Gamma(x;
     m/lam), in rho^2.  Control: the four-dimensional profile with the five-dimensional scaling.
  Q2 (computed, exact; what follows "so" is deduced) On (10.48), r^2 g^-1(d tau, d tau) = -(1 - tau^2) - mu r^-2 (1 +
     tau)^2 and r g^-1(d tau, dt) = -1 - mu r^-2 (1 + tau), so d tau is timelike for g_3b and in the cone of dt -- past
     timelike -- on tau^-1([0, T]) for every T < 1, with g_3b^-1(d tau, d tau) <= -(1 - T^2) uniformly in r in [m, oo]:
     at tau = T s the difference -(1 - T^2) - g_3b^-1(d tau, d tau) is T^2 (1 - s^2) + mu r^-2 (1 + T s)^2, a sum of
     nonnegative terms for s in [0, 1], the bound attained as r -> oo at tau = T (computed); X = {t = 0} is spacelike.
     Four-dimensional control: the same with 2m/r.  Control: T = 1, where the bound degenerates at infinity.
  Q3 (computed, exact; what follows "so" is deduced) On r in [r_h/2, r_h): g^-1(dr, dr) = f < 0 and g^-1(dr, dt) = mu
     r^-2 > 0, with dt timelike everywhere, so dr is timelike and in the cone opposite to the past timelike dt: dr is
     future timelike, m - r is a time function near Sigma# = {r = r_h/2}, which is spacelike, and future timelike
     vectors leave Omega there. Four-dimensional control: the same with 2m/r on [m, 2m).  Control: r = 2 r_h, outside
     the horizon.
  Q4 (computed, exact; what follows "so" is deduced) His Proposition 5.1 (4)-(5) at the weights of 10.21, (alpha_K,
     alpha_sf) = (1, -C_0 - 5/2), i.e. b_K = 1, b_sf = -C_0 - 3/2 in cform5.py's symbol T = r^2 (-l(dw/w) + S) on sf at
     (v, e) = (1/2, 1/102400): at dK+ and at R_v the characteristic polynomials (2 - d - lam)^3 q(d, lam) of cform5.py
     C7, with d = b_sf - b_K = -C_0 - 5/2 and d = b_sf = -C_0 - 3/2, have positive roots for every C_0 >= 0; and at C_0
     = 100, the largest C_0 10.21 uses, T is positive definite for every rho_K in [0, 10] (Sturm).  So the
     five-dimensional (5.14) at this e, alpha_sf < b* - 1 and alpha_K > alpha_sf + 1 - b*, b* = 0.99340731... (cform5.py
     C7), holds at these weights for every C_0 >= 0. Control: alpha_K = alpha_sf, below the threshold, where T at dK+
     has a negative eigenvalue.

Deduced, not computed here: with 10.13 (his section 3: Lemmas 3.3-3.8, and so Propositions 5.5-5.6; the symbols at
the critical sets), 10.14 (c with his Proposition 5.1 (1)-(6)) and Q1-Q4, every input [Hin26a] section 5.2 takes from
the metric and from c is computed on five-dimensional Tangherlini or deduced from computed quantities -- (4)-(5) off the
critical points and the smoothing of c (10.14(a)-(b)), and the bounded-geometry uniformity his Corollary 5.15 asks (p.
60), from Q1 and c in rho_sf C^oo; on the reading that his 3b-analysis (sections 2.3 and
5.2) holds in five dimensions as its arguments do -- not verified here line by line -- his Theorem 5.2 holds there at
(v, e) = (1/2, 1/102400) and 10.14's c, for weights with alpha_sf < b* - 1 and alpha_K > alpha_sf + 1 - b*, for h in
(0, h_0) with h_0 not made explicit, as in his.

READ.  [Hin26a] pp. 9 (section 1.2.2), 12-16 (Definition 2.1, the charts, (2.4), (2.7)-(2.10), Definitions 2.2 and 2.5,
(2.11)-(2.14)), 25-27 (Lemmas 3.3, 3.5, 3.7, 3.8, Remark 3.4, Corollary 3.6), 38 (Proposition 5.1), 41-44 (Theorem 5.2,
footnote 15, Lemma 5.3, (5.18)-(5.20), Lemma 5.4, Propositions 5.5-5.6), 47-48 and 51 (Proposition 5.8 and its proof),
51-52 and 54 (Proposition 5.9, (5.53)-(5.54), the remark after its proof), 54 (Proposition 5.11), 56 (Proposition 5.12),
58-60 (Remark 5.13, Lemma 5.14, Corollary 5.15, Proposition 5.16), 64 (Proposition 5.17 and its proof), 66 (the end of
section 5.2.7); alphaXiv, 2026-10-22.

sympy.  python3 solv5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import cform5 as CF
from damping5 import Checklist

mu, lam = sp.symbols("mu lam", positive=True)


def ks_metric(n, prof):
    """eta + prof k (x) k on R^(1+n), k = dt + dr, in Cartesian coordinates, with r an independent symbol (r^2 = |x|^2
    is not needed for homogeneity in (x, r) jointly) and d_i = d/dx_i + (x_i/r) d/dr; prof a function of r and mu"""
    x = sp.symbols("x1:%d" % (n + 1), real=True)
    r = sp.Symbol("r", positive=True)
    k = sp.Matrix([1] + [xi / r for xi in x])
    eta = sp.diag(-1, *([1] * n))
    P = prof(r)
    g = eta + P * k * k.T
    gi = eta - P * (eta * k) * (eta * k).T
    return x, r, g, gi


def christoffel(x, r, g, gi):
    N = len(x) + 1

    def d(F, mu_):                                                     # stationary: d_t = 0
        return 0 if mu_ == 0 else sp.diff(F, x[mu_ - 1]) + x[mu_ - 1] / r * sp.diff(F, r)

    dg = [[[d(g[a, b], c) for c in range(N)] for b in range(N)] for a in range(N)]
    return [[[sp.cancel(sum(gi[a, e] * (dg[e][b][c] + dg[e][c][b] - dg[b][c][e]) for e in range(N)) / 2)
              for c in range(N)] for b in range(N)] for a in range(N)]


# ------------------------------------------------------------------------------------------------- Q1
def q1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    cases = [(4, lambda r: mu / r**2, 2), (3, lambda r: 2 * mu / r, 1)]
    if control == 1:                                              # control: 4D profile, 5D scaling claimed
        cases = [(4, lambda r: 2 * mu / r, 2)]
    for n, prof, s in cases:
        x, r, g, gi = ks_metric(n, prof)
        on = {r: sp.sqrt(sum(xi**2 for xi in x))}
        inv = (g * gi - sp.eye(n + 1)).subs(on).applyfunc(sp.simplify) == sp.zeros(n + 1, n + 1)
        Gam = christoffel(x, r, g, gi)
        flat = [Gam[a][b][c] for a in range(n + 1) for b in range(n + 1) for c in range(n + 1)]
        poly = all(sp.Poly(sp.numer(z), mu).degree() <= 2 and sp.numer(z).subs(mu, 0) == 0
                   and mu not in sp.denom(z).free_symbols for z in flat if z != 0)
        scl = {**{xi: lam * xi for xi in x}, r: lam * r}
        scal = all(sp.cancel(z.subs(scl, simultaneous=True) - z.subs(mu, mu * lam**-s) / lam) == 0 for z in flat)
        nz = sum(1 for z in flat if z != 0)
        v = sp.Symbol("v", positive=True)
        cvec = [1 / r] + [-v * xi / r**2 for xi in x]                  # c = r^-1 (dt - v dr), Cartesian components
        c_ok = all(sp.cancel(z.subs(scl, simultaneous=True) - z / lam) == 0 for z in cvec)
        chk(f"n + 1 = {n + 1}: g^-1 = eta^-1 - prof k# k# exactly; {nz} nonzero Gamma, polynomials in mu with no "
            f"constant term; Gamma(lam x; mu) = lam^-1 Gamma(x; mu lam^-{s}): Gamma in mu rho^{s + 1} C^oo; c(lam x) = "
            f"c(x)/lam", inv and poly and scal and nz > 0 and c_ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Q2
def polar_inverse(n):
    r, tau = sp.symbols("r tau", positive=True)
    if n == 4:
        P = mu / r**2
    else:
        P = 2 * mu / r
    gi = sp.Matrix([[-1 - P, P], [P, 1 - P]])                       # (t, r) block of g^-1 for eta + P (dt + dr)^2
    return r, tau, P, gi


def q2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    T = sp.Integer(1) if control == 1 else sp.Rational(9, 10)
    for n in ((4,) if control else (4, 3)):
        r, tau, P, gi = polar_inverse(n)
        dtau = sp.Matrix([1, -tau])                                   # r d tau = dt - tau dr
        dt = sp.Matrix([1, 0])
        G33 = sp.expand((dtau.T * gi * dtau)[0])
        Gdt = sp.expand((dtau.T * gi * dt)[0])
        forms = sp.expand(G33 - (-(1 - tau**2) - P * (1 + tau)**2)) == 0 and sp.expand(Gdt - (-1 - P * (1 + tau))) == 0
        bound = -(1 - T**2)
        s_ = sp.Symbol("s", nonnegative=True)                       # tau = T s, s in [0, 1]
        # bound - G33 = T^2 (1 - s^2) + P (1 + T s)^2: each term >= 0 for s in [0, 1] and P = prof(r) >= 0
        split = sp.expand(bound - G33.subs(tau, T * s_) - (T**2 * (1 - s_**2) + P * (1 + T * s_)**2)) == 0
        sharp = sp.simplify(sp.limit(G33.subs(tau, T), r, sp.oo) - bound) == 0
        unif = bound < 0 and split and P.is_positive is True and sharp
        spacelike_X = sp.simplify((dt.T * gi * dt)[0] + 1 + P) == 0
        chk(f"n + 1 = {n + 1}: r^2 G(d tau) = -(1 - tau^2) - P (1 + tau)^2, r G(d tau, dt) = -1 - P (1 + tau), P = {P};"
            f" so on tau in [0, {T}] d tau is past timelike for g_3b, G_3b(d tau) <= {bound} uniformly; G(dt) < 0",
            forms and unif and spacelike_X)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Q3
def q3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        r, tau, P, gi = polar_inverse(n)
        rh = sp.sqrt(mu) if n == 4 else 2 * mu
        f = gi[1, 1]
        lo, hi = (rh / 2, rh) if n == 4 else (mu, 2 * mu)
        if control == 1:
            lo, hi = 2 * rh, 3 * rh                                    # control: outside the horizon
        # f increasing for every r > 0 and f(r_h) = 0, so f < 0 exactly on (0, r_h); the interval must lie in it
        inc = sp.simplify(sp.diff(f, r)).is_positive is True and sp.simplify(f.subs(r, rh)) == 0
        inside = bool(sp.simplify(hi - rh) <= 0) and bool(lo > 0)
        # G(dr, dt) = P > 0 and G(dt, dt) = -1 - P < 0 for every r > 0: dr in the cone opposite to dt
        cross = sp.simplify(gi[0, 1] - P) == 0 and P.is_positive is True and (-gi[0, 0]).is_positive is True
        chk(f"n + 1 = {n + 1}: on [{lo}, {hi}) G(dr) = f < 0 (f increasing, f(r_h) = 0), G(dr, dt) = {P} > 0, "
            f"G(dt) < 0: dr future timelike, m - r a time function, Sigma# spacelike", inc and inside and cross)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Q4
def q4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Tm, Bm = CF.sf_symbol()
    bk, bs, rk = CF.SC.bk, CF.SC.bs, CF.SC.rk
    C0, lm, d = sp.symbols("C0 lam d")
    q = 102400 * lm**2 - (307202 - 307199 * d) * lm + 204795 * d**2 - 409605 * d + 204801
    aK, asf = (sp.Integer(1), -C0 - sp.Rational(5, 2))
    if control == 1:
        aK = asf                                                     # control: alpha_K = alpha_sf
    BK, BS = aK, asf + 1
    ok_poly = (sp.expand((Tm.subs(rk, 0) - lm * sp.eye(5)).det() * 102400 - (2 - (bs - bk) - lm)**3 * q.subs(d, bs - bk))
               == 0)
    roots_pos = True
    for dd in (BS - BK, BS):
        qq = sp.Poly(q.subs(d, dd), lm)
        a2, a1, a0 = qq.all_coeffs()
        # both roots positive iff product > 0 and sum > 0 (real: T is B-self-adjoint); and 2 - d > 0
        conds = [sp.expand(a0 / a2), sp.expand(-a1 / a2), sp.expand(2 - dd)]
        for cnd in conds:
            P = sp.Poly(cnd, C0)
            pos = (P.count_roots(0, None) == 0 and P.eval(0) > 0) if P.degree() > 0 else cnd > 0
            roots_pos &= bool(pos)
    if control == 1:
        chk("at alpha_K = alpha_sf the roots at dK+ are positive for every C_0 >= 0", roots_pos)
        return chk.ok
    chk("the characteristic polynomial at dK+ is (2 - d - lam)^3 q(d, lam) (cform5.py C7), and at d = -C_0 - 5/2 "
        "(dK+) and d = -C_0 - 3/2 (R_v) its roots are positive for every C_0 >= 0", ok_poly and roots_pos)
    T100 = Tm.subs({bk: 1, bs: -sp.Rational(203, 2)})
    blk = T100[:2, :2]
    ok = all(CF.sign_on(z.subs(rk, CF.r), 0, 10, +1) for z in (blk.trace(), blk.det(), T100[2, 2]))
    chk("at C_0 = 100 ((alpha_K, alpha_sf) = (1, -205/2)) T is positive definite for every rho_K in [0, 10] (Sturm)",
        ok)
    return chk.ok


CHECKS = [("Q1 Tangherlini a 3sc-metric: Gamma in mu rho^3 C^oo by scaling, (2.12)-(2.14) with two powers to spare",
           q1, 1),
          ("Q2 near X: d tau past timelike for g_3b on tau in [0, T], every T < 1, uniformly to infinity", q2, 1),
          ("Q3 near Sigma#: dr future timelike on [r_h/2, r_h), m - r a time function, Sigma# spacelike", q3, 1),
          ("Q4 his Proposition 5.1 (4)-(5) at 10.21's weights (1, -C_0 - 5/2): positive for every C_0 >= 0", q4, 1)]


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
    print(f"solv5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"solv5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
