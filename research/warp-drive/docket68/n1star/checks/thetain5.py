#!/usr/bin/env python3
"""thetain5.py -- the incoming threshold of the tf model and the loss l of III.F' Corollary 3.4, at the record's point
(LOSS-D LD16, D588).

III.F' Corollary 3.4 (proof5/PART-III-F2-INDICIAL.md:463-491) inverts N_tf(L_b, +-1) with a loss l: it takes r_out :=
beta_sctf - 2 - eps/2, the orders of I.A Lemma 7.1 with that outgoing value (proof5/PART-I-SPECTRAL.md:1465-1489,
taking values in [r_out, r_in], r_in > (1/2)(-1 + vartheta_in) - alpha_+, alpha_+ = 0), and II.G' Lemma 4.1's l :=
max(ceil(sup r - r_out), ceil((s - 1)_+)), l~ := max(ceil(r_out - inf r), ceil((-s)_+)) (PART-II-G2-DECAY.md:627-633);
its integer is l + l~. The record never evaluates vartheta_in (I.A (1.5), :160-172; :793-794), and fixes s only as
"large" (F2:382). This computes vartheta_in for the tf model 2 L-bar, the spectral family on 4+1 Minkowski (F2:279-292),
and the l it gives.

The reduction (deduced from I.A's definitions). Write 2 L-bar = box + a^t d_t + a^i d_i + (order 0), the first-order
coefficients r^-1 times functions of xhat: a^t = rho beta, a^i xhat_i = rho alpha_r. In t* = t - r (d_t = d_t*, d_i|_t =
d_i|_t* - xhat_i d_t*), the d_t* coefficient is rho (beta - alpha_r) = 2 rho S (sbar5.py S1's S-bar), and the static
operator P(0)'s first-order part is a^i d_i|_t*. By I.A Lemma 4.4 (d_r has symbol i xi), the symbol of rho^-1 Im_h of
a^i d_i at rho = 0 is (1/2)(alpha^i + alpha^i*h) xi_i, so at R_in (xi = -2, eta = 0) p_in = -(alpha_r + alpha_r*h), and
p_in - (S + S*h) = -(M + M*h) with M := S + alpha_r = (beta + alpha_r)/2, the d_t* coefficient's endomorphism in the
incoming time t* = t + r. The order-0 terms and the angular coefficients do not reach the symbol there (rho^2, eta = 0).
So vartheta_in = sup lambda_max(-(M + M*h)), and with h making M self-adjoint (possible when M is semisimple with
constant eigenvalues: its spectral projections are smooth, sbar5.py S4's argument), vartheta_in = -2 min spec M.

  T1 (exact, sympy) M built two ways agrees: sbar5.py's S-bar with t* = t + r, and S + alpha_r, alpha_r := r times the
     static radial coefficient of 2 L - box in t* = t - r, at (R, 0, 0, 0). Control: M - S is not zero.
  T2 (exact) spec M = {0 (5 times), gam_U (3), 2 gam_U, (1 - e_U) gam_U, (1 + v) gam_C (3), 2 (1 + v) gam_C, (1 - e_C)
     (1 + v) gam_C}, every eigenvalue >= 0 for 0 < v, e_U, e_C < 1 and gam_U, gam_C > 0, and 0 among them (the incoming
     counterpart of the record's spec S-bar, III.F (3.1), with 1 - v for 1 + v); at the record's point (v = 1/2, e_C =
     1/102400, gam_C = 10^6, e_U = gam_U = 1/100) M is semisimple. So vartheta_in = 0: the incoming threshold is r_in >
     -1/2, the scalar wave's. Control: the record's outgoing S has the same zero and the same gam_U part.
  T3 (exact, the sign conventions) for the scalar operator -box + r^-1 (beta d_t + alpha d_r) in 4 + 1 dimensions (2 L's
     convention, box = -d_t^2 + Delta), r^-k f(t - r) solves it to leading order iff k = 3/2 + (beta - alpha)/2, the
     record's rho^(3/2 + S) at R_out (I.A Theorem 7.2 (5)), and r^-k f(t + r) iff k = 3/2 - (beta + alpha)/2 = 3/2 - M:
     incoming waves are rho^(3/2 - M), in rho^r L^2(|dx|) near infinity iff r < -1/2 - M, so the incoming estimate needs
     r_in > -1/2 - M = (1/2)(-1 + vartheta_in), as the reduction says. Control: the outgoing exponent with the sign of
     alpha flipped.
  T4 (exact) the loss. Theorem 4.3 and Corollary 5.2 of I.C hold for every s (I.C :586-587, Definition 5.1: tf-
     admissibility does not depend on s), so Corollary 3.4 may take s = 1. With vartheta_in = 0, r_out = beta_sctf - 2 -
     eps/2 < -1/2 < r_in: l = ceil(r_in - r_out) = 1 for r_in in (-1/2, r_out + 1], l~ = 0 (inf r = r_out, s >= 0), so
     the corollary's integer is 1, for every beta_sctf in (1/2 + eps/2, 3/2) and every eps in (0, 1/4) on a grid of
     each, and it cannot be 0 (r_in > -1/2 > r_out). Control: with the sign of the reduction flipped, vartheta_in =
     2 max spec M, l would be about 3 * 10^6.

Labels: T1, T2 and T3 computed (exact); the reduction, the choice s = 1 and T4's reading deduced.

    python3 checks/thetain5.py
"""
import os
import sys
from fractions import Fraction as Fr
from math import ceil

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import sbar5 as B  # noqa: E402

POINT = {B.v: sp.Rational(1, 2), B.eC: sp.Rational(1, 102400), B.gC: sp.Integer(10**6), B.eU: sp.Rational(1, 100),
         B.gU: sp.Rational(1, 100)}
M3 = sp.Rational(2, 3)


def alpha_r():
    C = B.Mink(4, 1)
    h, F = C.tensor()
    Gh = C.G(h)
    eu = C.EU(Gh, M3)
    out = 2 * C.EC(C.delta(Gh), M3) + 2 * (C.dstar(eu) + C.EC(eu, M3))
    R = sp.Symbol('R', positive=True)
    A1 = B.coeffs(C, B.flat(C, out), F, lambda f: sp.diff(f, C.x[0]), [R, 0, 0, 0])
    return (A1 * R).applyfunc(sp.simplify)


def t1():
    M, _ = B.sbar_L(4, M3, sgn=-1)
    S, _ = B.sbar_L(4, M3, sgn=1)
    al = alpha_r()
    ok = (M - (S + al)).applyfunc(sp.simplify) == sp.zeros(*M.shape)
    ctl = (M - S).applyfunc(sp.simplify) != sp.zeros(*M.shape)
    return ok, ctl, M, S


def t2(M, S):
    want = {0: 5, B.gU: 3, 2 * B.gU: 1, (1 - B.eU) * B.gU: 1, (1 + B.v) * B.gC: 3, 2 * (1 + B.v) * B.gC: 1,
            (1 - B.eC) * (1 + B.v) * B.gC: 1}
    got = B.spec(M)
    same = {sp.factor(k): n for k, n in want.items()} == got
    nonneg = all(B.nonneg(k) for k in got)
    Mp = M.subs(POINT)
    prod = sp.eye(Mp.shape[0])
    for s_ in Mp.eigenvals():
        prod = prod * (Mp - s_ * sp.eye(Mp.shape[0]))
    semi = prod.applyfunc(sp.simplify) == sp.zeros(*Mp.shape)
    sS = B.spec(S)
    ctl = sS.get(0) == 5 and sS.get(sp.factor(B.gU)) == 3
    return same and nonneg and semi, ctl, got, min(Mp.eigenvals()), max(Mp.eigenvals())


def t3():
    t, r, k, be, al = sp.symbols('t r k beta alpha', real=True)
    f = sp.Function('f')

    out = {}
    for sign in (-1, 1):
        u = r**(-k) * f(t + sign * r)
        box = -sp.diff(u, t, 2) + sp.diff(u, r, 2) + 3 / r * sp.diff(u, r)
        e = sp.expand((-box + (be * sp.diff(u, t) + al * sp.diff(u, r)) / r) * r**(k + 1))
        ph = sp.Symbol('ph')
        e = e.subs(t, ph - sign * r).doit()
        e = sp.expand(e)
        # the leading order: the coefficient of f'(phase) at r^0 after multiplying by r^(k+1)
        fd = sp.Derivative(f(ph), ph)
        lead_c = sp.expand(e).coeff(fd)
        lead_c = sp.limit(lead_c, r, sp.oo)
        out[sign] = sp.solve(sp.Eq(lead_c, 0), k)
    ok_out = sp.simplify(out[-1][0] - (sp.Rational(3, 2) + (be - al) / 2)) == 0
    ok_in = sp.simplify(out[1][0] - (sp.Rational(3, 2) - (be + al) / 2)) == 0
    ctl = sp.simplify(out[-1][0] - (sp.Rational(3, 2) + (be + al) / 2)) != 0
    rr, M_ = sp.symbols('rr M_', real=True)
    # rho^(3/2 - M) in rho^rr L^2(rho^-5 drho) near rho = 0 iff 2 (3/2 - M - rr) - 5 > -1
    thr = sp.solve(sp.Eq(2 * (sp.Rational(3, 2) - M_ - rr) - 5, -1), rr)[0]
    ok_thr = sp.simplify(thr - (-sp.Rational(1, 2) - M_)) == 0
    return ok_out and ok_in and ok_thr, ctl, out


def lemma41(r_in, r_out, s):
    l = max(ceil(r_in - r_out), ceil(max(s - 1, 0)))
    lt = max(ceil(r_out - r_out), ceil(max(-s, 0)))
    return l, lt


def t4(minM, maxM):
    theta_in = -2 * Fr(int(minM))
    ls = set()
    for i in range(1, 20):
        eps = Fr(i, 80)
        for j in range(1, 40):
            bs = Fr(1, 2) + eps / 2 + Fr(j, 40) * (1 - eps / 2)
            if not (Fr(1, 2) + eps / 2 < bs < Fr(3, 2)):
                continue
            r_out = bs - 2 - eps / 2
            lo = (Fr(-1) + theta_in) / 2
            r_in = min(max(lo + Fr(1, 10**6), r_out), r_out + 1)
            assert r_in > lo and r_in >= r_out
            l, lt = lemma41(r_in, r_out, Fr(1))
            ls.add(l + lt)
    ok = ls == {1}
    bad = (Fr(-1) + 2 * Fr(int(maxM))) / 2 - (Fr(3, 2) - Fr(1, 80) - 2 - Fr(1, 160))
    return ok, ceil(bad), ls


def main():
    res = {}
    a, c, M, S = t1()
    res['T1'], res['T1ctl'] = a, c
    print('  T1: M (t* = t + r) = S + alpha_r (t* = t - r) at (R, 0, 0, 0): %s; control M != S: %s' % (a, c))
    a, c, got, mn, mx = t2(M, S)
    res['T2'], res['T2ctl'] = a, c
    print('  T2: spec M = %s; all >= 0, min 0, semisimple at the record\'s point: %s (min %s, max %s); control (the '
          'record\'s S shares the zero and the gam_U part): %s' % (got, a, mn, mx, c))
    a, c, out = t3()
    res['T3'], res['T3ctl'] = a, c
    print('  T3: outgoing k = %s, incoming k = %s; incoming waves rho^(3/2 - M) leave rho^r L^2 iff r > -1/2 - M: %s; '
          'control: %s' % (out[-1], out[1], a, c))
    a, bad, ls = t4(mn, mx)
    res['T4'], res['T4ctl'] = a, bad > 10**6
    print('  T4: with vartheta_in = 0 and s = 1, Corollary 3.4\'s l + l~ over the grid of (beta_sctf, eps): %s; it '
          'cannot be 0; control (vartheta_in = 2 max spec M): l = %d' % (sorted(ls), bad))
    for k, val in res.items():
        print(k, 'PASS' if val else 'FAIL')
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
