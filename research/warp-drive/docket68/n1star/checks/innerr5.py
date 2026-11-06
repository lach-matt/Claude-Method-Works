#!/usr/bin/env python3
"""innerr5.py -- the inner boundary of D_T at an arbitrary curvature scale (the paper's section 2.5 and section 9).

D_T = {v <= v_end + T, r >= r_q(v)}, with r_q(v) := (sqrt72 mu(v) l5^2)^(1/4) the surface x_K := l5^2 sqrt(K) = 1, K
= 72 mu^2/r^8 the Kretschmann scalar of the Vaidya limit (the paper's R3), and Theorems 1-3 hold for every l5 > 0 with
mu0 >= sqrt72 l5^2, their constants depending on l5. So the region below the inner boundary is not a region the
theorems leave out: it is reached by a smaller l5.

  I1 (exact) For every a with 0 < a^4 < mu0 mu_end and every 0 < th < 1, the scale l5 := th a^2 / (72^(1/4)
     mu_end^(1/2)) gives r_q(v) <= th^(1/2) a < a for every v (mu(v) <= mu_end) and the strict seed condition
     mu0 > sqrt72 l5^2, so D_T for that l5 contains {v <= v_end + T, r >= a}; in particular every point with r > 0
     of the limit's domain lies in D_T for some l5 > 0. At r = 0 the limit is singular: K = 72 mu^2/r^8 is unbounded.
  I2 (exact) The Kretschmann scalar of 5D Vaidya, g0 = -(1 - mu(v)/r^2) dv^2 + 2 dv dr + r^2 dOmega_3^2, is 72 mu^2/r^8
     for every mass function mu(v): computed from the metric with mu symbolic, so x_K = 1 is r = r_q(v) at every v.
  Controls: I1 with l5 proportional to a (not a^2) fails, r_q then exceeding a for small a; I2 with the 4D exponent,
     mu/r (Schwarzschild-like) in place of mu/r^2, fails to give 72 mu^2/r^8.

Labels: computed (exact, sympy). Deduced: the theorems' constants depend on l5, and lambda_0 may shrink as l5 -> 0.

Run: python3 checks/innerr5.py   (about half a minute)
"""
import sys

import sympy as sp

a, th, mu0, mue, mu, l5 = sp.symbols("a theta mu0 mu_end mu l5", positive=True)


def i1(control=False):
    l = th * (a if control else a**2) / (72**sp.Rational(1, 4) * sp.sqrt(mue))
    rq_end = (sp.sqrt(72) * mue * l**2)**sp.Rational(1, 4)               # r_q is increasing in mu: worst case mu_end
    ok_r = sp.simplify(rq_end - sp.sqrt(th) * a) == 0
    seed = sp.simplify(sp.sqrt(72) * l**2 - th**2 * a**4 / mue)          # sqrt72 l5^2 = th^2 a^4/mu_end < mu0
    ok_s = seed == 0
    if control:                                                          # a small: r_q/a -> infinity
        ratio = sp.simplify(rq_end / a)
        return sp.limit(ratio.subs({th: sp.Rational(1, 2), mue: 1}), a, 0, "+") <= 1
    print("  I1: l5 = th a^2/(72^(1/4) mu_end^(1/2)) gives r_q(mu_end) = th^(1/2) a: %s;\n      sqrt72 l5^2 = th^2 "
          "a^4/mu_end, below mu0 when a^4 < mu0 mu_end: %s" % (ok_r, ok_s), flush=True)
    return ok_r and ok_s


def i2(control=False):
    v, r = sp.symbols("v r", positive=True)
    t1, t2, t3 = sp.symbols("t1 t2 t3")
    M = sp.Function("M")(v)
    F = 1 - (M / r if control else M / r**2)
    X = [v, r, t1, t2, t3]
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -F, 1, 1
    g[2, 2] = r**2
    g[3, 3] = r**2 * sp.sin(t1)**2
    g[4, 4] = r**2 * sp.sin(t1)**2 * sp.sin(t2)**2
    gi = sp.simplify(g.inv())
    n = 5
    Gam = [[[sp.simplify(sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                                 for l in range(n)) / 2) for k in range(n)] for j in range(n)] for i in range(n)]

    def riem(i, j, k, l):                                                # R^i_jkl
        e = sp.diff(Gam[i][j][l], X[k]) - sp.diff(Gam[i][j][k], X[l])
        e += sum(Gam[i][k][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][k] for m in range(n))
        return sp.simplify(e)
    R = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(k + 1, n):
                    val = riem(i, j, k, l)
                    if val != 0:
                        R[(i, j, k, l)] = val
                        R[(i, j, l, k)] = -val
    low = {}
    for (i, j, k, l), val in R.items():                                  # R_ijkl = g_im R^m_jkl
        for m in range(n):
            if g[m, i] != 0:
                low[(m, j, k, l)] = low.get((m, j, k, l), 0) + g[m, i] * val
    K = 0
    keys = list(low.keys())
    for (i, j, k, l) in keys:
        up = 0
        for (p, q, s, t) in keys:                                        # R^ijkl = g^ip g^jq g^ks g^lt R_pqst
            c = gi[i, p] * gi[j, q] * gi[k, s] * gi[l, t]
            if c != 0:
                up += c * low[(p, q, s, t)]
        K += low[(i, j, k, l)] * up
    K = sp.simplify(K)
    ok = sp.simplify(K - 72 * M**2 / r**8) == 0
    if not control:
        print("  I2: Kretschmann of 5D Vaidya with mu(v) symbolic = %s; equals 72 mu^2/r^8: %s" % (K, ok), flush=True)
    return ok


CHECKS = [("I1", i1), ("I2", i2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
