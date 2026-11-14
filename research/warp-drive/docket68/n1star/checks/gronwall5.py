#!/usr/bin/env python3
"""gronwall5: the Gronwall factor of Lemma 2.4 for Step 6's transport, explicit at the paper's point (CONSTANTS5.md,
Round 2, item (i): a stage-independent piece of C2; corrected in Round 3 after the verifier's M2).

Lemma 2.4 (N1STAR-PROOF.md, "**Lemma 2.4 (transport; deduced, `ks5.py` K4).**"; Round 8: re-pointed by content, the
line numbers having moved with D623): L0 phi - c phi = f on Omega gives ||phi(tau)|| <= e^(C (tau - tau0))(||phi(tau0)||
+ int ||f||). Its proof's identity (from "d_tau phi = L0 phi + xhat.d_x phi") is d_tau ||phi||^2 = 2 <phi, f + c phi>
- int (3/r) phi^2 + (1 + b')
int_{|x|=b} phi^2 - int_{|x|=a} phi^2, the 3/r being div xhat in R^4 and the boundary terms <= 0. Step 6 applies it to
(3.6), L0 Psi - (2/r) Psi = ..., so c = 2/r and 2c - 3/r = 1/r <= 1/a: the identity gives d_tau ||Psi|| <= ||f|| +
(1/(2a)) ||Psi||, rate 1/(2a). Round 2 took C = sup |c| = 2/a and dropped the -int (3/r) phi^2 term, which overstated
the rate four times (e^44.0 for e^11.0006; verifier of rounds 1-2, M2). Labels: computed (certified rationals from
lzeroconst5.py's geometry, mpmath.iv); deduced (the reading of the proof); estimate (where an assumption is not shown).

  G0 (exact, sympy) div(x/|x|) = 3/|x| in R^4, and 2 (2/r) - 3/r = 1/r: the identity's rate for Step 6 is 1/(2a).
  G1 (certified) at P*: 1/(2a) = 1.85282..., tau_end - tau0 = 5.93720825, so the identity's factor for Psi is
     exp((tau_end - tau0)/(2a)) = e^11.0006 = 5.99e4. That is a valid C for Lemma 2.4 at Step 6; the proof's C is any
     valid constant, so no lower bound on C2 is forced by it.
  G2 (deduced; certified number) the equation's own growth: along an integral curve of L0 (r decreasing at unit rate,
     r >= a on Omega) Psi' = (2/r) Psi gives (r(tau0)/r(tau))^2 = (1 + (tau - tau0)/r)^2 <= ((a + dtau)/a)^2 = 529.3
     (round 2 printed the looser (b(tau0)/a)^2 = 2479); the identity's exponential exceeds it about 113 times, not
     5.2e15.
  G3 (deduced reading; estimate) if Step 6's C carries G1's factor and Step 7's C3 = C_st C2 exp(C2 dtau)(1 + dtau)
     is read literally, ln C3 >= e^11.0006 x 5.937 = 3.56e5 (round 2: 7.65e19, from e^44); with C_N, C_st >= 1
     (assumed, not shown) ln lambda0 <= -3 ln C3 = -1.07e6. One Gronwall at the identity's rate (C2 ~ 1/(2a)) gives
     ln C3 ~ 13.56 and ln lambda0 <= -40.7 on the same assumption. Neither is a bound on lambda0: the proof does not
     fix C2.
  Controls (must fail, and do; each runs the code path it tests with one mutation): C1 the identity without its
  -int (3/r) phi^2 term (round 2's reading) is fed to G1's computation: its factor e^44.0 fails G1's enclosure; C2 G2's
  computation with r(tau0) bounded by b(tau0) instead of a + dtau (round 2's) fails G2's bound; C3 G0 in R^3 (div xhat
  = 2/r) gives 2c - 2/r = 2/r, not 1/r: the rate depends on the dimension, as the identity says.

    python3 checks/gronwall5.py
"""
import builtins
import os
import sys
import textwrap

import mpmath
import sympy as sp
from mpmath import iv, mpf, nstr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lzeroconst5 as LZ  # noqa: E402

iv.prec = 120


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(x) for x in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def fiv(q):
    return iv.mpf(q.numerator) / q.denominator


def identity_rate(dim):
    """2c - div xhat with c = 2/r, from the identity's terms (sympy, exact): returns (div xhat * r, (2c - div) * r)"""
    xs = sp.symbols('x1:%d' % (dim + 1), real=True)
    r = sp.sqrt(sum(x ** 2 for x in xs))
    div = sp.simplify(sum(sp.diff(x / r, x) for x in xs))
    return sp.simplify(div * r), sp.simplify((2 * 2 / r - div) * r)


def factor(rate_num, g):
    """exp(rate_num/a * dtau) as a certified interval; rate_num/a is the identity's rate times 2 (d||phi||^2)"""
    a_lo, a_hi = g['a']
    dt = iv.mpf([fiv(g['dtau'][0]).a, fiv(g['dtau'][1]).b])
    rate = iv.mpf([fiv(rate_num / a_hi / 2).a, fiv(rate_num / a_lo / 2).b])   # d||phi||/dtau <= ... + rate ||phi||
    return iv.exp(rate * dt), rate, dt


def growth(g, r0_bound):
    a_lo = g['a'][0]
    return (r0_bound / a_lo) ** 2


def main():
    ok = {}
    g = LZ.geometry()
    divr, net = identity_rate(4)
    ok['G0'] = divr == 3 and net == 1
    print('  G0: div xhat = %s/r in R^4; 2c - div xhat = %s/r with c = 2/r (sympy): the rate of ||Psi|| is 1/(2a)'
          % (divr, net))
    fac, rate, dt = factor(net, g)
    lo, hi = mpf(fac._mpi_[0]), mpf(fac._mpi_[1])
    ok['G1'] = mpf('5.9e4') < lo and hi < mpf('6.0e4')
    print('  G1: 1/(2a) in [%s, %s]; tau_end - tau0 in [%s, %s]; the identity\'s factor exp(dtau/(2a)) in [%s, %s] '
          '(= e^%s)' % (nstr(mpf(rate._mpi_[0]), 8), nstr(mpf(rate._mpi_[1]), 8), nstr(mpf(dt._mpi_[0]), 9),
                        nstr(mpf(dt._mpi_[1]), 9), nstr(lo, 6), nstr(hi, 6), nstr(mpf((rate * dt)._mpi_[0]), 6)))
    a_lo, a_hi = g['a']
    poly = growth(g, a_hi + g['dtau'][1])
    ok['G2'] = poly < 530 and (a_lo + g['dtau'][0]) ** 2 / a_hi ** 2 > 529
    print('  G2: along L0 the equation\'s own factor (r(tau0)/r)^2 <= ((a + dtau)/a)^2 <= %.2f; the identity\'s '
          'exponential exceeds it by a factor in [%s, %s]' % (float(poly), nstr(lo / poly, 4),
                                                              nstr(hi / poly * 1.0001, 4)))
    dtl = mpf(dt._mpi_[0])
    lnC3_lit = lo * dtl                                     # ln C3 >= C2 dtau, C2 >= the factor (literal reading)
    r_lo = mpf(rate._mpi_[0])
    lnC3_one = r_lo * dtl + mpmath.log(r_lo) + mpmath.log(1 + dtl)     # C3 >= C2 e^(C2 dt)(1 + dt), C2 = 1/(2a)
    ok['G3'] = mpf('3.5e5') < lnC3_lit < mpf('3.6e5') and 13 < lnC3_one < 14
    print('  G3 (deduced reading; C_N, C_st >= 1 assumed, an estimate): literal: ln C3 >= %s, ln lambda0 <= %s; one '
          'Gronwall at the identity\'s rate: ln C3 ~ %s, ln lambda0 <= %s' % (
              nstr(lnC3_lit, 4), nstr(-3 * lnC3_lit, 4), nstr(lnC3_one, 5), nstr(-3 * lnC3_one, 5)))
    # controls: the same code paths, mutated
    fac_m, _, _ = factor(4, g)                              # round 2's reading: 2c with the -3/r term dropped
    lo_m, hi_m = mpf(fac_m._mpi_[0]), mpf(fac_m._mpi_[1])
    ok['C1'] = not (mpf('5.9e4') < lo_m and hi_m < mpf('6.0e4'))
    print('  C1 (control): the identity without -int (3/r) phi^2 gives exp((2/a) dtau) in [%s, %s]: G1\'s enclosure '
          'fails for it: %s' % (nstr(lo_m, 6), nstr(hi_m, 6), ok['C1']))
    poly_m = growth(g, g['b0'][1])
    ok['C2'] = not (poly_m < 530)
    print('  C2 (control): G2 with r(tau0) <= b(tau0) (round 2) gives %.2f: G2\'s bound fails for it: %s' % (
        float(poly_m), ok['C2']))
    divr3, net3 = identity_rate(3)
    ok['C3'] = not (divr3 == 3 and net3 == 1)
    print('  C3 (control): in R^3, div xhat = %s/r and 2c - div xhat = %s/r: G0 fails for it: %s' % (divr3, net3,
                                                                                                   ok['C3']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
