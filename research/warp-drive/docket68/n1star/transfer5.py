#!/usr/bin/env python3
"""transfer5.py -- five-dimensional Tangherlini against its Minkowski model at infinity: the transfers of 10.12,
10.15, 10.24 and 10.38-10.42 (Phase B's B9; N1STAR-PROOF.md section 10.55; D125).  Labels: computed (exact, sympy).

The record computed every indicial family, tf-normal operator and I+ structure on 4+1 Minkowski and carried it to
Tangherlini on [Hin26]'s word that these "only see the Minkowskian model" (10.12; his Theorem 7.1's proof) and that
the differences are of lower order ([Hin26c] Example 5.4: box_(g_m,a) - box_(g-bar) in rho^3 Diff^2_3b, by his Lemma
4.4(2)).  Here the five-dimensional orders, from the metric itself.

  T1 (computed, exact) Kerr-Schild form.  With t the Kerr-Schild time, x in R^4, r = |x|, k = dt + dr (lower index),
     g = eta + (mu/r^2) k (x) k: k is null for eta and for g, g^-1 = eta^-1 - (mu/r^2) k# (x) k# exactly (k# = eta^-1
     k), and Ric(g) = 0 at three points of R^5 (exact, mu = 7/5).  The static time is t_s = t - int mu/(r^2 - mu) dr.
  T2 (computed, exact) The orders.  Every Christoffel symbol of g is mu G_3 + mu^2 G_5 with G_j homogeneous of degree
     -j in x (Euler's identity x . grad G_j = -j G_j, checked at a point): the connection differs from Minkowski's by
     terms two orders below its own -1 (scattering) -- in four dimensions, mu/r, one order.  With t* = t - r: g^-1(dt*,
     dt*) = -4 mu/r^2, g^-1(dt*, dr) = -1 + 2 mu/r^2, g^-1(dr, dr) = 1 - mu/r^2.  The constraint damping 1-form with
     the static time, r^-1 (dt_s - v dr), differs from Minkowski's r^-1 (dt - v dr) by -mu dr/(r (r^2 - mu)), of order
     r^-3; so does c_Ups = r^-1 dt_s.
  Controls: Ric(g) = 0 fails for the four-dimensional profile mu/r in five dimensions (T1); with mu/r the mu
     coefficient is homogeneous of degree -2, not -3 (T2).

sympy.  python3 transfer5.py [--selftest | --mutants]   (about five minutes)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

t, x1, x2, x3, x4, MU, V = sp.symbols("t x1 x2 x3 x4 mu v", real=True)
X = [t, x1, x2, x3, x4]
XS = X[1:]
R = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
ETA = sp.diag(-1, 1, 1, 1, 1)
PTS = ([0, sp.Rational(3, 2), sp.Rational(1, 2), sp.Rational(-2, 3), sp.Rational(5, 4)],
       [1, 2, 1, 1, sp.Rational(1, 3)], [sp.Rational(-1, 2), 1, -2, sp.Rational(3, 5), 2])
MU0 = sp.Rational(7, 5)


def metric(power=2):
    k = sp.Matrix([1] + [xi / R for xi in XS])
    g = ETA + MU / R**power * k * k.T
    ks = ETA.inv() * k
    gi = ETA.inv() - MU / R**power * ks * ks.T
    return k, ks, g, gi


def christoffel(g, gi):
    dg = [[[sp.diff(g[a, b], X[c]) for c in range(5)] for b in range(5)] for a in range(5)]
    return [[[sum(gi[a, d] * (dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(5)) / 2 for c in range(5)]
             for b in range(5)] for a in range(5)]


def zero_at(expr, pt):
    return sp.simplify(expr.subs(dict(zip(X, pt))).subs(MU, MU0)) == 0


def ricci_zero(gam, pt):
    sub = dict(zip(X, pt))
    sub[MU] = MU0
    G = [[[gam[a][b][c].subs(sub) for c in range(5)] for b in range(5)] for a in range(5)]
    dG = [[[[sp.diff(gam[a][b][c], X[e]).subs(sub) for e in range(5)] for c in range(5)] for b in range(5)]
          for a in range(5)]
    for b in range(5):
        for c in range(b, 5):
            rbc = sum(dG[a][b][c][a] - dG[a][b][a][c] + sum(G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
                                                            for d in range(5)) for a in range(5))
            if sp.simplify(rbc) != 0:
                return False
    return True


def t1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k, ks, g, gi = metric(1 if control == 1 else 2)
    chk("g g^-1 = I with g^-1 = eta^-1 - (mu/r^2) k# k#; k null for eta",
        sp.simplify(g * gi - sp.eye(5)) == sp.zeros(5) and sp.simplify((k.T * ETA.inv() * k)[0]) == 0)
    gam = christoffel(g, gi)
    chk("Ric(g) = 0 at three points (mu = 7/5)", all(ricci_zero(gam, p) for p in PTS))
    return chk.ok


def t2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k, ks, g, gi = metric(1 if control == 1 else 2)
    gam = christoffel(g, gi)
    ok = True
    for a in range(5):
        for b in range(5):
            for c in range(b, 5):
                G = sp.expand(gam[a][b][c])
                if G == 0:
                    continue
                P = sp.Poly(G, MU)
                for (m,), co in zip(P.monoms(), P.coeffs()):
                    euler = sum(xi * sp.diff(co, xi) for xi in XS) + (1 + 2 * m) * co
                    ok &= zero_at(euler, PTS[0])
    chk("every Christoffel symbol is mu G_3 + mu^2 G_5, G_j homogeneous of degree -j (Euler at a point)", ok)
    tstar = t - R
    dts = sp.Matrix([sp.diff(tstar, xx) for xx in X])
    dr = sp.Matrix([sp.diff(R, xx) for xx in X])
    vals = [sp.simplify((dts.T * gi * dts)[0]), sp.simplify((dts.T * gi * dr)[0]), sp.simplify((dr.T * gi * dr)[0])]
    chk(f"t* = t - r: g^-1(dt*, dt*), g^-1(dt*, dr), g^-1(dr, dr) = {vals}",
        [sp.simplify(vv - w) for vv, w in zip(vals, (-4 * MU / R**2, -1 + 2 * MU / R**2, 1 - MU / R**2))] == [0] * 3)
    rr = sp.Symbol("r", positive=True)
    diff_c = sp.simplify((1 / rr) * (-MU / (rr**2 - MU)))
    chk(f"c with the static time less Minkowski's c: {diff_c} dr, of order r^-3",
        sp.limit(diff_c * rr**3, rr, sp.oo) == -MU)
    return chk.ok


CHECKS = [("T1 Kerr-Schild: g^-1 exact, k null, Ric(g) = 0 at three points", t1),
          ("T2 the connection two orders below Minkowski's; g^00 = -4 mu/r^2; c to r^-3", t2)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"transfer5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"transfer5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
