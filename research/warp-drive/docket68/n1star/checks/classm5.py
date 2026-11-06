#!/usr/bin/env python3
"""classm5: the stage-1 mean at W_TT's maximiser, reduced to one number by the symmetry class; and the size of W_TT on
the initial slice (CONSTANTS5.md, Round 8: the round-7 verifier's gap in MAJOR 1, item 2, and its R7.3 finding).
Labels: computed (exact, sympy), certified (Arb balls, python-flint), READ (cited lines), deduced (where said).

The class (READ stage5.py's COMP, lead5.py's coordinates (v, r, th, phi1, phi2), N1STAR-PROOF.md 0.1): a T^2 x Z2 x
Z2-invariant symmetric tensor has the eight components vv, vr, rr, v th, r th, th th, phi1 phi1, phi2 phi2, functions
of (v, r, th). x = r (cos th cos phi1, cos th sin phi1, sin th cos phi2, sin th sin phi2), tau = v - r.

  K1 (exact) In the Cartesian frame (tau, x1, ..., x4) at phi1 = 0 (every th in (0, pi/2), phi2 symbolic), the x2
     column of every class tensor M is (0, 0, M_phi1phi1/(r cos th)^2, 0, 0): d_x2 = d_phi1/(r cos th) there, and no
     other coordinate field has a d_phi1 part. By continuity the same holds on the axis th = 0, at X* = (th = 0, phi1 =
     phi2 = 0, v = 2, r = a). So m_1(X*) e_phi1 = M_22 e_phi1 with M_22 := (m_1)_phi1phi1(X*)/a^2: a single number.
  K2 (exact) At X*, with r7fixes5 R1's frame (e_phi1 = e2, e_th = e3, e_phi2 = e4), W(s) = K cos s diag(0, 0, 4/3, -2/3,
     -2/3) and D = U U^T, U = (1, 1, 0, 0, 0): for every class M (K1's block form), e2 is an eigenvector of g(s) = M +
     W(s) + chi D for every s, with eigenvalue M_22 + (4/3) K cos s. Hence (deduced) sup_s |g(s)|_op >= (4/3) K +
     |M_22|, and a certified enclosure of M_22 excluding 0 is all that stage 1 needs at X*: the verifier's general case
     (M_22 near 0 and an off-diagonal M_2j != 0) cannot occur in the class.
  K3 (exact; certified) The size of W_TT. Its eigenvalues on (th, phi1, phi2) are -2 (a1 + a2), 2 a1, 2 a2 (READ
     lead5.py:58-67), with amplitudes in the phase (2 K/3) (C^4 + S^4)^(1/2), (2 K/3) (4 C^4 + S^4)^(1/2), (2 K/3)
     (4 S^4 + C^4)^(1/2), K = E H r^(-3/2); with q = cos 2th, H^2 (4 C^4 + S^4) = 5/2 + 3 q/(1 + q^2) <= 4 (exact,
     equality at q = 1), so sup_{th, s} |W_TT|_op = (4/3) E(v) r^(-3/2). On Sigma_tau0 (v = r - 2, r in [5/2, 11/2]
     where E != 0): sup |W_TT|_op <= certified bound printed (Arb over cells, E <= c <= 1.3241034918, stage1cap5's
     env_sq_hi), below R7.3's 0.64 (whose factor 2^(1/2) the exact angular maximum 1 replaces).
  K4 (certified; deduced) What an enclosure would give. With (4/3) K >= 12.593464 at X* (r7fixes5 R1's ball, READ) and
     the operator-norm reading lambda0 < eps1/C_app, an enclosure M_22 in [lo, hi], 0 not in it, gives C_app >= (4/3) K
     + min(|lo|, |hi|), so lambda0's operator-norm bound is multiplied by 12.593309/(12.593309 + min(|lo|, |hi|)).
  K5 (certified; READ stage1rate5.out K3) The a posteriori route's amplification on X*'s past. Lemma 2.3's rate for
     stage 1's principal part is kappa <= 13.2197 on Omega (stage1rate5 K3, READ), and X* lies at tau* = 2 - a, so
     Dtau* = tau* - tau0 = 4 - a and e^(kappa Dtau*/2) bounds the energy's growth from Sigma to X* (principal part only;
     the lower-order coefficients' sup norms, which the record does not compute, add to kappa).
  Controls (each mutates the computed path and must fail): C1 K1 with a v phi1 component added (outside the class):
     the x2 column acquires a tau entry; C2 K2 with an off-class entry M_23 = w: e2 is not an eigenvector; C3 K3's
     angular claim H^2 (4 C^4 + S^4) <= 2: refuted at q = 1; C4 K3 on the slice tau = -1 in place of tau0: the bound
     there leaves the pinned interval.

    python3 checks/classm5.py        (seconds)
"""
import builtins
import contextlib
import io
import os
import sys
import textwrap
from fractions import Fraction as Fr

import flint
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import stage1cap5 as SC          # noqa: E402  (env_sq_hi, C_HI: envelope5 E1)

OK = {}
KBALL_LO = flint.arb('12.593464') - flint.arb('2.75e-7')     # READ r7fixes5.out R1: (4/3) K >= [12.593464 +/- 2.75e-7]
CAPP = Fr(12593309, 10 ** 6)                                # the certified operator-norm C_app (round 4)


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def k1(extra_vphi1=False):
    v, r, th, p1, p2 = sp.symbols('v r theta phi1 phi2', real=True)
    names = ['vv', 'vr', 'rr', 'vth', 'rth', 'thth', 'p1p1', 'p2p2']
    m = dict(zip(names, sp.symbols('m_' + ' m_'.join(names))))
    Mc = sp.zeros(5)                                   # in (v, r, th, phi1, phi2)
    Mc[0, 0], Mc[0, 1], Mc[1, 1], Mc[0, 2], Mc[1, 2] = m['vv'], m['vr'], m['rr'], m['vth'], m['rth']
    Mc[2, 2], Mc[3, 3], Mc[4, 4] = m['thth'], m['p1p1'], m['p2p2']
    if extra_vphi1:
        Mc[0, 3] = sp.Symbol('m_vp1')
    Mc = Mc + Mc.T - sp.diag(*[Mc[i, i] for i in range(5)])
    X = [v - r, r * sp.cos(th) * sp.cos(p1), r * sp.cos(th) * sp.sin(p1), r * sp.sin(th) * sp.cos(p2),
         r * sp.sin(th) * sp.sin(p2)]
    Jf = sp.Matrix([[sp.diff(Xi, y) for y in (v, r, th, p1, p2)] for Xi in X])     # d(tau, x)/d(v, r, th, phi1, phi2)
    Jf0 = sp.simplify(Jf.subs(p1, 0))
    Jinv = sp.simplify(Jf0.inv())                                                   # d(v, ...)/d(tau, x) at phi1 = 0
    Mcart = sp.simplify(Jinv.T * Mc.subs(p1, 0) * Jinv)
    col = [sp.simplify(Mcart[i, 2]) for i in range(5)]
    target = [0, 0, m['p1p1'] / (r * sp.cos(th)) ** 2, 0, 0]
    return all(sp.simplify(c - t) == 0 for c, t in zip(col, target)), col


def k2(off_class=False):
    K, s, chi, w = sp.symbols('K s chi w', real=True)
    A = sp.Matrix(5, 5, lambda i, j: sp.Symbol('A%d%d' % (min(i, j), max(i, j))) if 2 not in (i, j) else 0)
    M = A.copy()
    M[2, 2] = sp.Symbol('M22')
    if off_class:
        M[2, 3] = M[3, 2] = w
    W = K * sp.cos(s) * sp.diag(0, 0, sp.Rational(4, 3), -sp.Rational(2, 3), -sp.Rational(2, 3))
    U = sp.Matrix([1, 1, 0, 0, 0])
    g = M + W + chi * U * U.T
    e2 = sp.Matrix([0, 0, 1, 0, 0])
    ge = sp.simplify(g * e2 - (sp.Symbol('M22') + sp.Rational(4, 3) * K * sp.cos(s)) * e2)
    return all(x == 0 for x in ge)


def k3_angular(claim=4):
    q = sp.Symbol('q', real=True)
    C2, S2 = (1 + q) / 2, (1 - q) / 2
    H2 = 2 / (1 + q ** 2)
    expr = sp.simplify(H2 * (4 * C2 ** 2 + S2 ** 2))
    form = sp.simplify(expr - (sp.Rational(5, 2) + 3 * q / (1 + q ** 2)))
    gap = sp.factor(sp.simplify(claim - expr))
    other = sp.simplify(H2 * (C2 ** 2 + S2 ** 2))                    # the th th amplitude's square, without 2K/3
    return form == 0, gap, expr.subs(q, 1), sp.simplify(sp.Rational(4, 1) - other)


def k3_sigma(tau0=-2, cells=3000):
    """certified sup over Sigma_tau0 of (4/3) E(v) r^(-3/2), v = tau0 + r, E^2 bounded by stage1cap5 (E = 0 off
    [1/2, 7/2])"""
    r_lo, r_hi = Fr(1, 2) - tau0, Fr(7, 2) - tau0
    best = flint.arb(0)
    for i in range(cells):
        a, b = r_lo + (r_hi - r_lo) * Fr(i, cells), r_lo + (r_hi - r_lo) * Fr(i + 1, cells)
        va, vb = a + tau0, b + tau0
        if vb <= Fr(1, 2) or va >= Fr(7, 2):
            continue
        E2 = SC.env_sq_hi(max(va, Fr(1, 2)), min(vb, Fr(7, 2)))
        rr = SC.fa(a)
        val = flint.arb((flint.arb(4) / 3 * flint.arb(E2).sqrt() * rr ** flint.arb(-1.5)).upper())
        if val > best:
            best = val
    return best


SIG_PIN = (flint.arb('0.22'), flint.arb('0.23'))


def main():
    print('classm5: the stage-1 mean at X* reduced to M_22 by the class; W_TT on Sigma_tau0')
    ok1, col = k1()
    OK['K1'] = ok1
    print('  K1 (exact): at phi1 = 0 the x2 column of a class tensor is %s: %s' % ([str(c) for c in col], ok1))
    OK['K2'] = k2()
    print('  K2 (exact): at X*, g(s) e2 = (M_22 + (4/3) K cos s) e2 for every class M, every s, every chi: %s; so '
          'sup_s |g(s)|_op >= (4/3) K + |M_22| (deduced)' % OK['K2'])
    form, gap, at1, oth = k3_angular()
    sig = k3_sigma()
    OK['K3'] = form and sp.simplify(gap.subs(sp.Symbol('q', real=True), 1)) == 0 and at1 == 4 and \
        SIG_PIN[0] < sig < SIG_PIN[1]
    print('  K3 (exact; certified): H^2 (4 C^4 + S^4) = 5/2 + 3 q/(1 + q^2): %s, 4 - it = %s >= 0, = 4 at q = 1; '
          'H^2 (C^4 + S^4) is 4 - (%s) <= 4; so sup_{th, s} |W_TT|_op = (4/3) E r^(-3/2); on Sigma_tau0, '
          'sup |W_TT|_op <= %s (certified; R7.3 printed < 0.64 with a factor 2^(1/2)); pinned in %s: %s' % (
              form, gap, oth, sig.str(6), [x.str(3) for x in SIG_PIN], OK['K3']))
    for mlo in (Fr(1, 10), Fr(1), Fr(5)):
        fac = CAPP / (CAPP + mlo)
        print('      K4: an enclosure with min |M_22| = %s would multiply the operator-norm bound 0.0024433 by %.6f '
              '(< %.7f)' % (mlo, float(fac), float(Fr(24433, 10 ** 7) * fac)))
    OK['K4'] = KBALL_LO > flint.arb(CAPP.numerator) / CAPP.denominator
    print('  K4: (4/3) K at X* >= %s > 12.593309: %s' % (KBALL_LO.str(9), OK['K4']))
    a = SC.a_ball()
    kap = flint.arb('13.2197')                                  # READ stage1rate5.out K3 (upper bound)
    dts = 4 - a
    amp = (kap * dts / 2).exp()
    OK['K5'] = flint.arb('5.0e10') < amp < flint.arb('5.3e10')
    print('  K5: Dtau* = 4 - a = %s; e^(kappa Dtau*/2) <= %s (kappa <= 13.2197, READ stage1rate5.out K3): an '
          'enclosure of M_22 through Lemma 2.3 needs the residual of an approximate stage-1 solution below |M_22| '
          'times about 2e-11 in the energy norm, before the lower-order coefficients and the Sobolev constant of the '
          'evaluation at X*: %s' % (dts.str(8), amp.str(4), OK['K5']))
    ok_c1, col1 = k1(extra_vphi1=True)
    OK['C1'] = not ok_c1
    print('  C1 (control): a v phi1 component added: the x2 column is %s: K1 fails: %s' % ([str(c) for c in col1],
                                                                                        OK['C1']))
    OK['C2'] = not k2(off_class=True)
    print('  C2 (control): an off-class entry M_23 = w: e2 is no longer an eigenvector: %s' % OK['C2'])
    _, gap2, _, _ = k3_angular(claim=2)
    OK['C3'] = sp.simplify(gap2.subs(sp.Symbol('q', real=True), 1)) < 0
    print('  C3 (control): the angular claim <= 2: 2 - H^2 (4 C^4 + S^4) at q = 1 is %s < 0: %s' % (
        sp.simplify(gap2.subs(sp.Symbol('q', real=True), 1)), OK['C3']))
    sig4 = k3_sigma(tau0=-1)
    OK['C4'] = not (SIG_PIN[0] < sig4 < SIG_PIN[1])
    print('  C4 (control): K3 on the slice tau = -1 instead of tau0 = -2: bound %s, outside the pin: %s' % (
        sig4.str(6), OK['C4']))
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
