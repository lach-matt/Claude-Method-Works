#!/usr/bin/env python3
"""twodt5: the curvature region D_T for two null dusts, and Lemma 1.1 (b), (f) (FAMILIES5 4i, D546; corrected D549).

The record's D_T is radial, {v <= V, r >= r_q(v)} (N1STAR-PROOF.md:172-173), r_q(mu) := (sqrt72 mu l5^2)^(1/4)
(N1STAR-PROOF.md:145-148), with q0 := r_q(mu0) <= sqrt(mu0) by the seed condition mu0 >= sqrt72 l5^2. Read through the
Kretschmann scalar 72 mu^2/r^8 of 5D Vaidya (CERTIFY-10L5's K_0 normalisation), r_q is where it reaches l5^-4; that
reading is ours, not the record's. For two dusts (FAMILIES5 4c, 4i; g0 = -2 e^(2s) du dv + R^2 dOmega_3^2, K_in R^3 =
A(v), K_out R^3 = B(u)) the Kretschmann scalar is no longer the mass's alone.

  T1 (exact, sympy) on the solutions of twodust5's B1 (the evolution) with the constraints C_u, C_v:
         R_abcd R^abcd = 72 mu^2/R^8 + (8/3) e^(-4s) A B/R^6,
     mu the Misner-Sharp mass of B3; at B = 0 it is the record's 72 mu^2/r^8. The dust term is >= 0 when A B >= 0, as
     for the record's dusts (A, B >= 0, positive null energy): one null dust has R_ab R^ab = 0, two crossing ones
     2 (g^uv)^2 Ric_uu Ric_vv.
  T2 (exact, sympy) (i) 72 mu^2/R^8 <= l5^-4 iff R >= r_q(mu) (R^8 - r_q^8 = R^8 - 72 mu^2 l5^4), so with A B >= 0,
     {K <= l5^-4} lies in {R >= r_q(mu)}, the two-dust form of the record's D_T, mu at the point; (ii) q0^4 - mu^2 =
     mu (sqrt72 l5^2 - mu) for q0 := r_q(mu), so q0 <= sqrt(mu) exactly when mu >= sqrt72 l5^2 (control: at mu = sqrt72
     l5^2/2, q0 > sqrt(mu)). (f) needs no mass condition: a point of D_T has R >= r_q(mu) >= q0 for any q0 at most the
     least r_q over D_T. (b) needs q0 := r_q(mu_min) with mu_min a lower bound of mu on the region, R = a included
     (the record's mu0, Vaidya's mu being non-decreasing): then mu_min >= sqrt72 l5^2 gives a^2 < q0^2 <= mu_min <= mu
     on R = a, a := q0 - delta0.
  T3 (exact, control; verifier 238, D549) q0 taken as D_T's least r_q fails (b) when the outgoing flux lowers mu on R =
     a below D_T's least mass: l5 = 1, mu = 10 on D_T, 8.6 on R = a (both >= sqrt72 = 8.485): q0 = r_q(10) = 3.0351 >
     sqrt(8.6) = 2.9326, and a^2 > 8.6 at delta0 = 0.01 and 0.1; with q0 := r_q(8.6) = 2.9227 it holds.

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
    mu, l5, R = sp.symbols('mu l5 R', positive=True)
    rq = (sp.sqrt(72) * mu * l5**2)**sp.Rational(1, 4)
    region = sp.expand(rq**8 - 72 * mu**2 * l5**4) == 0             # R >= r_q  <=>  R^8 >= 72 mu^2 l5^4
    fac = sp.expand(rq**4 - mu**2 - mu * (sp.sqrt(72) * l5**2 - mu)) == 0
    ctl = sp.simplify((rq**2 - sp.sqrt(mu)**2).subs(mu, sp.sqrt(72) * l5**2 / 2)) > 0
    return region and fac, ctl


def control_t3():
    rq = lambda m: (sp.sqrt(72) * m)**sp.Rational(1, 4)               # l5 = 1
    mD, ma = sp.Integer(10), sp.Rational(86, 10)
    bad = rq(mD) > sp.sqrt(ma) and all((rq(mD) - d)**2 > ma for d in (sp.Rational(1, 100), sp.Rational(1, 10)))
    good = rq(ma) < sp.sqrt(ma) and all((rq(ma) - d)**2 < ma for d in (sp.Rational(1, 100), sp.Rational(1, 10)))
    return bad and good and min(mD, ma) >= sp.sqrt(72), [sp.N(x, 5) for x in (rq(mD), sp.sqrt(ma), rq(ma))]


def main():
    ok = {}
    t1, vaidya = kretschmann()
    ok['T1'] = t1 and vaidya
    print('  T1: K = 72 mu^2/R^8 + (8/3) e^(-4s) A B/R^6 on shell: %s; at B = 0 the record\'s 72 mu^2/r^8: %s'
          % (t1, vaidya), flush=True)
    t2, ctl = mass_condition()
    ok['T2'] = t2 and ctl
    print('  T2: R >= r_q(mu) iff 72 mu^2/R^8 <= l5^-4, and q0^4 - mu^2 = mu (sqrt72 l5^2 - mu): %s; control mu = '
          'sqrt72 l5^2/2 gives q0 > sqrt(mu): %s' % (t2, ctl))
    t3, nums = control_t3()
    ok['T3'] = t3
    print('  T3: q0 from D_T\'s least mass (10) is %s > sqrt(8.6) = %s on R = a, so (b) fails; q0 = r_q(8.6) = %s '
          'holds: %s' % (nums[0], nums[1], nums[2], t3))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
