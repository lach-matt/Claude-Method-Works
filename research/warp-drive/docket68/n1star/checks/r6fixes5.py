#!/usr/bin/env python3
"""r6fixes5: two of the round-5 verifier's minor findings, re-derived before they are seated (CONSTANTS5.md, Round 6,
R6.0). Labels: computed (exact, sympy), certified (exact rationals and outward-rounded enclosures), READ (the cited
.out lines).

  F1 (minor 2; exact, certified) the largest-entry reading of lambda0. At xhat = e1, g0 = eta + m U U^T, U = (1, 1, 0,
     0, 0), eta = diag(-1, 1, 1, 1, 1); with v = e_tau - e_1, det(g0 + t v v^T) = 4 m t - 1 (sympy, every m, t). At
     t = 1/(4 m) the metric degenerates, and t v v^T has every entry of absolute value t or 0: so in the largest-entry
     reading Lemma 2.3's eps1 is below 1/(4 m*), m* = mu_end/a^2 in [16.234970, 16.234971] (READ lzerotrace5.out T7,
     certified there), that is eps1 < 0.0153989, and with C_app >= 12.593309 (READ lzerotrace5.out T3, operator and
     largest entry) lambda0 < 0.0012228. Round 5's 0.0012968 (lzerorank5.py R2) is valid; this one is smaller. Not
     claimed sharp.
  F2 (minor 3; deduced, computed) stage1rate5's inhomogeneous constant. From dE/dtau <= kappa E + c_Y E^(1/2) ||box~ u||
     and box~ u = -2 f: y := E^(1/2) obeys y' <= (kappa/2) y + (c_Y/2) ||box~ u|| = (kappa/2) y + c_Y ||f||, so
     ||du(tau)|| <= q_lo^(-1/2) e^(kappa Dtau/2) (y(tau0) + c_Y int ||f||): the coefficient is c_Y q_lo^(-1/2)
     e^(kappa Dtau/2), not 2 c_Y q_lo^(-1/2) e^(kappa Dtau/2). With stage1rate5.out K3's enclosures (READ: c_Y^2 <= 2,
     q_lo >= 0.196683, e^(kappa Dtau/2) <= 1.105e17, and its own product 7.048e17 for the factor 2) the coefficient
     is < 3.525e17. [Round 7, m3: those inputs were rounded the wrong way (q_lo >= 0.1966827, e^(...) <= 1.1051725e17,
     7.04843e17); recomputed in Arb, r7fixes5.py R5: < 3.52422e17, so 3.525e17 stands as a bound.] The homogeneous
     factor q^(1/2) e^(kappa Dtau/2) <= 4.174e18 stands.
  F3 (M2 and minor 8; exact) D4 Proposition 3.1's towers at -k and D4 (R4)'s class roots: every leading exponent m
     there is <= -1, so Lemma 2.1's Lemma 1.4 part, whose exponents are >= lambda_s1,2 = 2 + d1 (D4 Lemma 2.1's
     proof), sits at offsets >= 3 + d1 from m, beyond (0, 1.4901]; and at offset 1 the formal solutions (Lemma 1.5)
     meet no root: with box^Ups(0)'s indicial polynomials at z = 4e-6 (gaugepot5.py G1's factors, READ: s0 lam (lam -
     3)(lam^2 - lam - 2 - z); v1 (lam + 1)(3 - lam); s1 (4 - lam) lam Q_1(lam (lam - 1))), -k + 1 (k = 2, 3, 4) is not
     an s0 or s1 root, and 0 (the v1 tower at -1) is not a v1 root. So every tower's offset-1 log order is 0 at the
     record's point; at z = 0, -1 is an s1 root (control C3), which is the verifier's remark at z = 0.
     [Round 7, the round-6 verifier's m1: this list is incomplete -- the s0 and s1 terms at -1 and the v1 terms at
     -2, -3, -4 (D4 Proposition 3.1 (1)-(3)) were missed, and (s0, -1), (s1, -1), (v1, -2) land on roots. F3 below
     tests the partial list only; the full list, the resonances and why R5.2's table is unchanged are r7fixes5.py R3.]
  Controls (each mutates the computed path; each must fail): C1 F1 with v = e_tau + e_1 (the other sign): the
  determinant is -1 for every t, no degeneration, so F1's test (a root in t > 0) fails; C2 F2's recursion with
  box~ u = -f (the factor 2 dropped): the coefficient is c_Y/2, and F2's identity fails; C3 F3 at z = 0: -1 is an s1
  root and F3's test fails.

    python3 checks/r6fixes5.py       (seconds)
"""
import builtins
import sys
import textwrap
from fractions import Fraction as Fr

import sympy as sp

OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def det_form(sign):
    m, t = sp.symbols('m t', real=True)
    eta = sp.diag(-1, 1, 1, 1, 1)
    U = sp.Matrix([1, 1, 0, 0, 0])
    v = sp.Matrix([1, sign, 0, 0, 0])
    g = eta + m * U * U.T + t * v * v.T
    return sp.expand(g.det()), m, t


def f2_coeff(factor):
    """y' <= (kappa/2) y + (c_Y/2) ||box~ u||, box~ u = -factor f: the coefficient of int ||f|| in y"""
    cY, f = sp.symbols('c_Y f', positive=True)
    return sp.simplify(cY / 2 * factor * f / f)


def tower_roots(z):
    lam = sp.Symbol('lam')
    kap = 3
    Q = lambda S: S ** 2 - (2 + 2 * kap + z) * S + kap * (kap + 1) + z * kap  # noqa: E731
    s0 = lam * (lam - 3) * (lam ** 2 - lam - 2 - z)
    s1 = (4 - lam) * lam * Q(lam * (lam - 1))
    v1 = (lam + 1) * (3 - lam)
    ok = all(s0.subs(lam, 1 - k) != 0 and s1.subs(lam, 1 - k) != 0 for k in (2, 3, 4)) and v1.subs(lam, 0) != 0
    return ok


def main():
    print('r6fixes5: the round-5 verifier\'s minor findings 2 and 3, re-derived')
    D, m, t = det_form(-1)
    OK['F1'] = sp.simplify(D - (4 * m * t - 1)) == 0
    mlo = Fr(16234970, 10 ** 6)
    tstar_hi = 1 / (4 * mlo)                      # 1/(4 m*) <= 1/(4 m_lo)
    capp_lo = Fr(12593309, 10 ** 6)
    lam_hi = tstar_hi / capp_lo
    OK['F1'] = OK['F1'] and tstar_hi < Fr(153989, 10 ** 7) and lam_hi < Fr(12228, 10 ** 7)
    print('  F1: det(g0 + t v v^T) = %s with v = e_tau - e_1 (exact); t* = 1/(4 m*) <= %.7f (m* >= 16.234970), the '
          'largest entry of t* v v^T being t*; lambda0 < t*/C_app <= %.7f (largest-entry reading; C_app >= 12.593309): '
          '%s' % (D, float(tstar_hi), float(lam_hi), OK['F1']))
    Dc, _, _ = det_form(1)
    roots = sp.solve(sp.Eq(Dc, 0), t)
    OK['C1'] = not (sp.simplify(Dc - (4 * m * t - 1)) == 0) and roots == []
    print('  C1 (control): v = e_tau + e_1: det = %s, no root in t: F1\'s test fails: %s' % (Dc, OK['C1']))
    c2 = f2_coeff(2)
    cY = sp.Symbol('c_Y', positive=True)
    OK['F2'] = sp.simplify(c2 - cY) == 0
    # Round 8 (the round-7 verifier): the inputs rounded outward, q_lo down to 0.1966827 and e^(kappa Dtau/2) up to
    # 1.1051725e17 (r7fixes5 R5); before, 0.196683 and 1.105e17 printed 3.5237e17, below the certified 3.52422e17
    qlo, cY2, fac = Fr(1966827, 10 ** 7), 2, Fr(11051725, 10 ** 7) * 10 ** 17
    import math
    coeff = math.sqrt(cY2) / math.sqrt(float(qlo)) * float(fac)
    OK['F2'] = OK['F2'] and coeff < 3.525e17 and abs(2 * coeff - 7.048e17) / 7.048e17 < 1e-3
    up5 = math.ceil(coeff / 10 ** 13) * 10 ** 13        # Round 9 (the round-8 verifier's minor 4): printed rounded up
    print('  F2: the coefficient of int ||f|| in y is %s (exact); c_Y q_lo^(-1/2) e^(kappa Dtau/2) <= %.4e (floating '
          'point on READ enclosures rounded outward, r7fixes5 R5; Arb there: < 3.52422e17), half of stage1rate5\'s '
          '7.048e17: %s' % (
              c2, up5, OK['F2']))
    c2b = f2_coeff(1)
    OK['C2'] = not (sp.simplify(c2b - cY) == 0)
    print('  C2 (control): box~ u = -f: coefficient %s, not c_Y: F2\'s identity fails: %s' % (c2b, OK['C2']))
    OK['F3'] = tower_roots(Fr(4, 10 ** 6))
    print('  F3: at z = 4e-6, -1, -2, -3 are not s0 or s1 roots of box^Ups(0) and 0 is not a v1 root (exact), on the '
          'partial list of round 6 (Round 7: the full list has three resonances, r7fixes5.py R3): %s' % OK['F3'])
    OK['C3'] = not tower_roots(0)
    print('  C3 (control): at z = 0, -1 is an s1 root and F3\'s test fails: %s' % OK['C3'])
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
