#!/usr/bin/env python3
"""twodt5: the curvature region D_T for two null dusts, and Lemma 1.1 (b), (f) from one mass condition (FAMILIES5 4i,
D546).

The record's D_T is {v <= V, r >= r_q(v)}, r_q(mu) := (sqrt72 mu l5^2)^(1/4), the radius at which the Kretschmann
scalar 72 mu^2/r^8 of 5D Vaidya reaches l5^-4 (N1STAR-PROOF.md:145-152). For two dusts (FAMILIES5 4c, 4i; g0 = -2 e^(2s)
du dv + R^2 dOmega_3^2, K_in R^3 = A(v), K_out R^3 = B(u)) the Kretschmann scalar is no longer the mass's alone.

  T1 (exact, sympy) on the solutions of twodust5's B1 (the evolution) with the constraints C_u, C_v:
         R_abcd R^abcd = 72 mu^2/R^8 + (8/3) e^(-4s) A B/R^6,
     mu the Misner-Sharp mass of B3; at B = 0 it is the record's 72 mu^2/r^8. The dust term is >= 0: one null dust has
     R_ab R^ab = 0, two crossing ones 2 (g^uv)^2 Ric_uu Ric_vv.
  T2 (exact) so K <= l5^-4 implies R >= r_q(mu): with D_T := {vhat <= V, K <= l5^-4} and r_q^flat(vhat) the least
     r_q(mu) over the points of D_T on the ingoing ray vhat, D_T lies in {R >= r_q^flat(vhat)}, and the record's proof
     of (f) runs with r_q^flat for r_q and q0 := min r_q^flat. If mu >= mu_min >= sqrt72 l5^2 there (the record's seed
     condition, for the Misner-Sharp mass), then q0^4 = sqrt72 mu_min l5^2 <= mu_min^2, so q0 <= sqrt(mu_min), and a :=
     q0 - delta0 gives a^2 < mu on R = a: Lemma 1.1' (b) as well. Checked symbolically: q0^2 <= mu_min under the
     condition, and a control at mu_min below sqrt72 l5^2 where q0^2 > mu_min.

Run: python3 checks/twodt5.py   (about 10 seconds)
"""
import sys

import sympy as sp


def kretschmann():
    u, v, c, th, ph = sp.symbols('u v chi theta phi')
    X = [u, v, c, th, ph]
    R = sp.Function('R')(u, v)
    s = sp.Function('s')(u, v)
    g = sp.zeros(5, 5)
    g[0, 1] = g[1, 0] = -sp.exp(2 * s)
    g[2, 2] = R**2
    g[3, 3] = R**2 * sp.sin(c)**2
    g[4, 4] = R**2 * sp.sin(c)**2 * sp.sin(th)**2
    gi = g.inv()
    n = 5
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[k]) + sp.diff(g[d, k], X[b]) - sp.diff(g[b, k], X[d]))
                             for d in range(n)) / 2) for k in range(n)] for b in range(n)] for a in range(n)]

    def riem(a, b, k, d):
        e = sp.diff(Gam[a][b][d], X[k]) - sp.diff(Gam[a][b][k], X[d])
        return e + sum(Gam[a][k][m] * Gam[m][b][d] - Gam[a][d][m] * Gam[m][b][k] for m in range(n))

    Rm = {}
    for a in range(n):
        for b in range(n):
            for k in range(n):
                for d in range(k + 1, n):
                    val = sp.simplify(riem(a, b, k, d))
                    if val != 0:
                        Rm[(a, b, k, d)] = val

    def full(a, b, k, d):
        if k < d:
            return Rm.get((a, b, k, d), 0)
        if k > d:
            return -Rm.get((a, b, d, k), 0)
        return 0

    K = 0
    for a in range(n):
        for b in range(n):
            for k in range(n):
                for d in range(n):
                    low = sum(g[a, m] * full(m, b, k, d) for m in range(n))
                    if low == 0:
                        continue
                    up = sum(gi[b, i] * gi[k, j] * gi[d, l] * full(a, i, j, l) for i in range(n) for j in range(n)
                             for l in range(n) if gi[b, i] != 0 and gi[k, j] != 0 and gi[d, l] != 0)
                    K += low * up
    A, B = sp.symbols('A B')
    Ru, Rv, su, sv = sp.diff(R, u), sp.diff(R, v), sp.diff(s, u), sp.diff(s, v)
    on_shell = {sp.Derivative(R, (u, 2)): 2 * su * Ru - B / (3 * R**2),
                sp.Derivative(R, (v, 2)): 2 * sv * Rv - A / (3 * R**2),
                sp.Derivative(R, u, v): -(sp.exp(2 * s) + 2 * Ru * Rv) / R,
                sp.Derivative(s, u, v): 3 * (sp.exp(2 * s) + 2 * Ru * Rv) / (2 * R**2)}
    K = sp.simplify(sp.simplify(K).subs(on_shell))
    mu = R**2 * (1 + 2 * sp.exp(-2 * s) * Ru * Rv)
    target = 72 * mu**2 / R**8 + sp.Rational(8, 3) * sp.exp(-4 * s) * A * B / R**6
    return sp.simplify(sp.expand(K - target)) == 0, sp.simplify((K - 72 * mu**2 / R**8).subs(B, 0)) == 0


def mass_condition():
    mu, l5 = sp.symbols('mu_min l5', positive=True)
    q0 = (sp.sqrt(72) * mu * l5**2)**sp.Rational(1, 4)
    # q0^2 <= mu  <=>  sqrt72 mu l5^2 <= mu^2  <=>  mu >= sqrt72 l5^2
    cond = sp.simplify(q0**4 - mu**2)          # <= 0 iff mu >= sqrt72 l5^2
    ok = sp.simplify(cond.subs(mu, sp.sqrt(72) * l5**2 * 2)) < 0 and sp.simplify(
        cond.subs(mu, sp.sqrt(72) * l5**2)) == 0
    ctl = sp.simplify(cond.subs(mu, sp.sqrt(72) * l5**2 / 2)) > 0
    return ok, ctl


def main():
    ok = {}
    t1, vaidya = kretschmann()
    ok['T1'] = t1 and vaidya
    print('  T1: K = 72 mu^2/R^8 + (8/3) e^(-4s) A B/R^6 on shell: %s; at B = 0 the record\'s 72 mu^2/r^8: %s'
          % (t1, vaidya), flush=True)
    t2, ctl = mass_condition()
    ok['T2'] = t2 and ctl
    print('  T2: q0^2 <= mu_min exactly when mu_min >= sqrt72 l5^2 (equality at the bound): %s; control mu_min = '
          'sqrt72 l5^2/2 gives q0^2 > mu_min: %s' % (t2, ctl))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
