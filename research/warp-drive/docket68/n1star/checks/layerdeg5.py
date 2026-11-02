#!/usr/bin/env python3
"""layerdeg5.py -- the degree bookkeeping of EQUALITY5-LAYER.md round 2 (Lemmas L.2(a) and L.3 written out).

  D1 (exact, every component, every harmonic k) The seed's linearised operators on a harmonic H(v, r, th) e^(i k v/lam):
     the lam^-2 part of dRic^H is zero (g0^-1(dv, dv) = 0), its lam^-1 part is k T(H) with T the table of layerlin5.py
     (N1), its lam^0 part R_X(H) does not depend on k, and the lam^-1 part of dD is i k Pol(H).  Hence the fast part of
     the seed's stage operator is d_th composed with an operator in X alone: it maps the k-th harmonic to the k-th
     harmonic, annihilates th-means (k = 0) and has th-mean zero on every profile (round 2, R2.1 (F2), L.3).
     Control: the phase tau = v - r, whose differential is timelike (g0^-1(dtau, dtau) = -1 - mu0/r^2), gives a nonzero
     lam^-2 part.
  D2 (exact) Harmonic algebra: Re[a e^(i th)] Re[b e^(i th)] has harmonics 0 and 2 only; the th-mean of (th-independent)
     times (first harmonic) is 0; so a th-mean of a product with at most one first-harmonic factor and no other
     oscillating factor vanishes.  Control: Re[a e^(i th)] Re[b e^(2 i th)] has a first harmonic.
  D3 (exact) The shifts at equality are of degree 2, with constants: with x := mu/mu0 >= 1, sqrt(x) - 1 <= (x - 1)/2 and
     x^(1/4) - 1 <= (x - 1)/4, so on the boundary  0 <= r_q - sqrt(mu0) <= (mu - mu0)/(4 sqrt(mu0)),
     |beta0| <= (mu - mu0)/(2 mu0) + r_q mu'/(4 mu0),  0 <= m0 <= (mu - mu0)/(2 mu0) + r_q mu'/(2 mu0),  with beta0 :=
     F(r_q) - r_q' and m0 := -g0^-1(dPhi0, dPhi0) computed from g0 (EQUALITY5 (0.2)).  Control: (x - 1)/3 in place of
     (x - 1)/2 fails near x = 1.
  D4 (exact on samples) The zero-mean antiderivative: if Z is 2 pi-periodic with mean 0 and Y' = Z, <Y> = 0, then
     sup |Y| <= pi sup |Z| (used to make the stage transport an ODE in the Banach space C(S^1)); checked on random
     trigonometric polynomials and a square wave.  Control: the constant pi/4 fails on cos.
  D5 (exact) The chain rule (0.3) of the supplement to order four: for a profile f(v, th) and m >= 0, d_v^j (lam^m f(v,
     v/lam)) = sum_l binom(j, l) lam^(m - l) (d_th^l d_v^(j - l) f)(v, v/lam), so |d^j(lam^m [f])| <= C sum_l lam^(m-l)
     |d_th^l d_X^(j-l) f|: a derivative of a profile costs lam^-1 only through d_th.  Control: without the lam^-l weights
     the identity fails.

Labels: computed (exact, sympy).  Run: python3 checks/layerdeg5.py   (about a minute; imports layerlin5.py)
"""
import os
import random
import sys
import textwrap
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerlin5 as L  # noqa: E402


def out(msg, flush=True):
    """print, wrapped at 121 characters"""
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=flush)

T0 = time.time()
r, v, th, mu0, lam, I, n = L.r, L.v, L.th, L.mu0, L.lam, L.I, L.n
k = sp.Symbol('k')


def ops_k(H, phase):
    """(dRic^H, dD lowered) of h = H e^(i k phase/lam), divided by the phase factor; phase = 'v' or 'tau' (= v - r)"""
    dph = [1, 0, 0, 0, 0] if phase == 'v' else [1, -1, 0, 0, 0]
    X, Gam, gi, g = L.X, L.Gam, L.gi, L.g
    D = lambda e, j: sp.diff(e, X[j]) + I*k/lam*dph[j]*e                       # noqa: E731
    Dh = [[[D(H[i, j], cc) - sum(Gam[d][cc][i]*H[d, j] + Gam[d][cc][j]*H[i, d] for d in range(n))
            for j in range(n)] for i in range(n)] for cc in range(n)]
    dG = [[[sum(gi[i, d]*(Dh[j][d][cc] + Dh[cc][d][j] - Dh[d][j][cc]) for d in range(n))/2 for cc in range(n)]
           for j in range(n)] for i in range(n)]
    DdG = [[[[D(dG[i][j][cc], e) + sum(Gam[i][e][d]*dG[d][j][cc] - Gam[d][e][j]*dG[i][d][cc]
                                       - Gam[d][e][cc]*dG[i][j][d] for d in range(n))
              for cc in range(n)] for j in range(n)] for i in range(n)] for e in range(n)]
    dRic = [[sum(DdG[i][i][j][cc] for i in range(n)) - sum(DdG[cc][i][i][j] for i in range(n)) for cc in range(n)]
            for j in range(n)]
    dD = [sum(gi[i, j]*dG[rho][i][j] for i in range(n) for j in range(n)) for rho in range(n)]
    dDl = [sum(g[m, rho]*dD[rho] for rho in range(n)) for m in range(n)]
    DD = [[D(dDl[m], nn) - sum(Gam[d][nn][m]*dDl[d] for d in range(n)) for m in range(n)] for nn in range(n)]
    R = sp.Matrix(n, n, lambda m, nn: dRic[m][nn] - (DD[nn][m] + DD[m][nn])/2)
    return R, sp.Matrix(dDl)


def d1(control=False):
    H = L.general_H()
    R, Dd = ops_k(H, 'tau' if control else 'v')
    m2 = all(L.is_zero(sp.expand(R[i, j]).coeff(lam, -2)) for i in range(n) for j in range(i, n))
    if control:
        return m2
    Tt = L.T_tab(H)
    m1 = all(L.is_zero(sp.expand(R[i, j]).coeff(lam, -1) - k*Tt[i, j]) for i in range(n) for j in range(i, n))
    m0 = all(L.is_zero(sp.diff(sp.expand(R[i, j]).coeff(lam, 0), k)) for i in range(n) for j in range(i, n))
    pt = L.pol_tab(H)
    p1 = all(L.is_zero(sp.expand(Dd[j]).coeff(lam, -1) - I*k*pt[j]) for j in range(n))
    p0 = all(L.is_zero(sp.diff(sp.expand(Dd[j]).coeff(lam, 0), k)) for j in range(n))
    out("  D1 on H e^(i k v/lam), k symbolic: lam^-2 part 0: %s; lam^-1 part = k T(H) (15): %s; lam^0 part free of k:"
          " %s; dD: lam^-1 part = i k Pol(H): %s, lam^0 part free of k: %s  [%.0f s]"
          % (m2, m1, m0, p1, p0, time.time() - T0), flush=True)
    return m2 and m1 and m0 and p1 and p0


def d2(control=False):
    a1, a2, b1, b2, t = sp.symbols('a1 a2 b1 b2 t', real=True)
    kb = 2 if control else 1
    ReA = a1*sp.cos(t) - a2*sp.sin(t)
    ReB = b1*sp.cos(kb*t) - b2*sp.sin(kb*t)
    prod = ReA*ReB
    harmonics = [j for j in range(0, 5)
                 if sp.simplify(sp.integrate(sp.expand(prod*sp.exp(-I*j*t)), (t, 0, 2*sp.pi))) != 0]
    first = 1 in harmonics
    if control:
        return not first
    mean = sp.simplify(sp.integrate(sp.Symbol('m')*ReA, (t, 0, 2*sp.pi)))
    out("  D2 harmonics j >= 0 of Re[a e^(i th)] Re[b e^(i th)]: %s; mean of (mean) x (first harmonic): %s"
          % (harmonics, mean), flush=True)
    return set(harmonics) <= {0, 2} and mean == 0


def d3(control=False):
    x = sp.Symbol('x', positive=True)
    den = 3 if control else 2
    f1 = (x - 1)/den - (sp.sqrt(x) - 1)
    f2 = (x - 1)/4 - (x**sp.Rational(1, 4) - 1)
    # both vanish at x = 1 and have nonnegative derivative on x >= 1
    ok1 = sp.simplify(f1.subs(x, 1)) == 0 and all(sp.diff(f1, x).subs(x, xv) >= 0 for xv in
                                                    [1 + sp.Rational(j, 7) for j in range(0, 60)])
    ok1 &= sp.solve(sp.Eq(sp.diff(f1, x), 0), x) in ([1], [])
    ok2 = sp.simplify(f2.subs(x, 1)) == 0 and sp.solve(sp.Eq(sp.diff(f2, x), 0), x) in ([1], [])
    ok2 &= all(sp.diff(f2, x).subs(x, xv) >= 0 for xv in [1 + sp.Rational(j, 7) for j in range(0, 60)])
    if control:
        return ok1
    # beta0 and m0 from g0 at equality (EQUALITY5 (0.2)): Phi0 = r - r_q(v), r_q = (mu0 mu)^(1/4)
    vv = sp.Symbol('v')
    mu = sp.Function('mu')(vv)
    rq = (mu0*mu)**sp.Rational(1, 4)
    Fq = 1 - mu/rq**2
    rqp = sp.diff(rq, vv)
    beta0 = Fq - rqp
    m0 = -(Fq - 2*rqp)                       # Lemma E.1 (a): g0^-1(dPhi, dPhi) = F(rho) - 2 rho' on r = rho
    form_b = sp.simplify(beta0 - (1 - sp.sqrt(mu/mu0) - rq*sp.diff(mu, vv)/(4*mu))) == 0
    form_m = sp.simplify(m0 - (sp.sqrt(mu/mu0) - 1 + rq*sp.diff(mu, vv)/(2*mu))) == 0
    out("  D3 sqrt(x) - 1 <= (x - 1)/2: %s; x^(1/4) - 1 <= (x - 1)/4: %s; beta0 = 1 - sqrt(mu/mu0) - r_q mu'/(4 mu):"
          " %s; m0 = sqrt(mu/mu0) - 1 + r_q mu'/(2 mu): %s (so, with mu >= mu0, the stated bounds)"
          % (ok1, ok2, form_b, form_m), flush=True)
    return ok1 and ok2 and form_b and form_m


def d4(control=False):
    t = sp.Symbol('t', real=True)
    rng = random.Random(4)
    const = sp.pi/4 if control else sp.pi
    samples = [sp.cos(t)]
    for _ in range(4):
        Z = sum(sp.Rational(rng.randint(-5, 5), rng.randint(1, 4))*(sp.cos(j*t) if rng.random() < .5 else sp.sin(j*t))
                for j in range(1, 5))
        samples.append(Z)
    ok = True
    worst = 0
    grid = [2*sp.pi*j/400 for j in range(400)]
    for Z in samples:
        Y = sp.integrate(Z, t)
        Y = Y - sp.integrate(Y, (t, 0, 2*sp.pi))/(2*sp.pi)
        supY = max(abs(float(Y.subs(t, g_))) for g_ in grid)
        supZ = max(abs(float(Z.subs(t, g_))) for g_ in grid)
        if supZ == 0:
            continue
        worst = max(worst, supY/supZ)
        ok &= supY <= float(const)*supZ*(1 + 1e-9)
    # the square wave Z = sign(sin t): Y a triangle of amplitude pi/2
    if not control:
        ok &= sp.pi/2 <= sp.pi
        out("  D4 sup|Y|/sup|Z| over the samples: %.4f <= pi; square wave: pi/2 <= pi" % worst, flush=True)
    return ok


def d5(control=False):
    f = sum(sp.Rational(j + 1, 3)*v**(j % 3)*th**(j % 4) for j in range(7)) + sp.sin(2*th)*v**2

    def der(e, l, jl):
        for _ in range(l):
            e = sp.diff(e, th)
        for _ in range(jl):
            e = sp.diff(e, v)
        return e
    m = 2
    ok = True
    for j in range(1, 5):
        lhs = sp.diff(lam**m*f.subs(th, v/lam), v, j)
        rhs = sum(sp.binomial(j, l)*lam**(m - (0 if control else l))*der(f, l, j - l).subs(th, v/lam)
                  for l in range(j + 1))
        ok &= sp.simplify(lhs - rhs) == 0
    if not control:
        out("  D5 d_v^j (lam^m f(v, v/lam)) = sum_l binom(j, l) lam^(m-l) (d_th^l d_v^(j-l) f)(v, v/lam), j <= 4: %s"
              % ok, flush=True)
    return ok


def main():
    ok = True
    for name, f in (("D1", d1), ("D2", d2), ("D3", d3), ("D4", d4), ("D5", d5)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    out("layerdeg5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
