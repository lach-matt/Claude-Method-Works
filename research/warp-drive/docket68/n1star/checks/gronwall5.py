#!/usr/bin/env python3
"""gronwall5: the Gronwall factor of Lemma 2.4 for Step 6's transport, explicit at the paper's point (CONSTANTS5.md,
Round 2, item (i): a stage-independent piece of C2).

Lemma 2.4 (N1STAR-PROOF.md:230-235): L0 phi - c phi = f on Omega gives ||phi(tau)|| <= e^(C (tau - tau0))(||phi(tau0)||
+ int ||f||); its proof bounds d_tau ||phi||^2 by 2 <phi, f + c phi> (the boundary terms have a sign), so C = sup |c|.
Step 6 applies it to (3.6), L0 Psi - (2/r) Psi = ..., so c = 2/r <= 2/a. Labels: computed (certified rationals from
lzeroconst5.py's geometry); deduced (the reading of the proof).

  G1 (certified) at P*: 2/a = 7.41128..., tau_end - tau0 = 5.93720825, so Lemma 2.4's factor for Psi is
     exp((2/a)(tau_end - tau0)) in a certified interval, about 1.3e19 (e^44.0): the proof's C2 is at least 2/a as Steps
     6-7 derive it, and C3 = C_st C2 e^(C2 (tau_end - tau0)) (1 + tau_end - tau0) carries this factor at least.
  G2 (deduced; certified number) the exponential is the proof's, not the equation's: along an integral curve of L0 (r
     decreasing at unit rate), Psi' = (2/r) Psi + f gives the homogeneous factor (r(tau0)/r(tau))^2 <= (b(tau0)/a)^2,
     about 2.48e3: a weighted energy (r^2 Psi) would replace e^44 by this polynomial factor.
  G3 (deduced reading; certified numbers) Step 6 writes the Psi-part as "at most C (N(tau0) + int (N + ...))", and that
     C carries Lemma 2.4's factor, so C2 >= exp((2/a)(tau_end - tau0)) as written; Step 7's C3 contains
     exp(C2 (tau_end - tau0)), so the literal constants are doubly exponential: ln C3 >= 1.288e19 x 5.937 = 7.65e19.
     With C_N, C_st >= 1 (assumed here, not shown), lambda0 <= 1/(C3 C_N M^2) <= C3^-3 gives ln lambda0 <= -2.29e20;
     one Gronwall on the summed differential inequalities (rate >= 2/a) would give ln C3 of order 48 instead, and ln
     lambda0 <= -143.8 on the same assumption (an estimate of what a rewritten Step 7 delivers, not a bound).
  Controls (must fail, and do): C1 the claim "the factor is below 1e18" is refuted by G1's lower end; C2 the claim
  "the homogeneous growth exceeds 1e4" is refuted by G2's bound; C3 the single-exponential reading's ln C3 is refuted
  as a bound for the literal reading's.

    python3 checks/gronwall5.py
"""
import os
import sys
from fractions import Fraction as Fr

from mpmath import iv, mpf, nstr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lzeroconst5 as LZ  # noqa: E402

iv.prec = 120


def fiv(q):
    return iv.mpf(q.numerator) / q.denominator


def main():
    ok = {}
    g = LZ.geometry()
    a_lo, a_hi = g['a']
    dt_lo, dt_hi = g['dtau']
    rate = iv.mpf([fiv(2 / a_hi).a, fiv(2 / a_lo).b])
    dt = iv.mpf([fiv(dt_lo).a, fiv(dt_hi).b])
    fac = iv.exp(rate * dt)
    lo, hi = mpf(fac._mpi_[0]), mpf(fac._mpi_[1])
    ok['G1'] = lo > mpf(10) ** 19 and hi < mpf(2) * mpf(10) ** 19
    print('  G1: 2/a in [%s, %s]; tau_end - tau0 in [%.8f, %.8f];\n      Lemma 2.4\'s factor for Psi, '
          'exp((2/a)(tau_end - tau0)), in [%s, %s] (= e^%s)' % (
              nstr(mpf(rate._mpi_[0]), 8), nstr(mpf(rate._mpi_[1]), 8), float(dt_lo), float(dt_hi), nstr(lo, 6),
              nstr(hi, 6), nstr(mpf((rate * dt)._mpi_[0]), 6)))
    b_lo, b_hi = g['b0']
    poly = (b_hi / a_lo) ** 2
    ok['G2'] = poly < 2500 and (b_lo / a_hi) ** 2 > 2470
    print('  G2: along L0 the homogeneous factor is (r(tau0)/r)^2 <= (b(tau0)/a)^2 <= %.2f: the exponential exceeds '
          'it\n      by a factor above %s' % (float(poly), nstr(lo / poly, 3)))
    rate_lo = mpf(rate._mpi_[0])
    dtl = mpf(fiv(dt_lo)._mpi_[0])
    lnC3_lit = lo * dtl                                    # ln C3 >= C2 (tau_end - tau0) with C2 >= the factor
    lnlam_lit = -3 * lnC3_lit
    import mpmath
    lnC3_one = rate_lo * dtl + mpmath.log(rate_lo) + mpmath.log(1 + dtl)   # C3 >= C2 e^(C2 dt)(1 + dt)
    ok['G3'] = lnC3_lit > mpf('7.6e19') and -3 * lnC3_one < -143
    print('  G3 (C_N, C_st >= 1 assumed): literal reading: ln C3 >= %s, ln lambda0 <= %s;\n'
          '      one Gronwall: ln C3 >= %s, ln lambda0 <= %s' % (nstr(lnC3_lit, 4), nstr(lnlam_lit, 4),
                                                             nstr(lnC3_one, 5),
                                                             nstr(-3 * lnC3_one, 5)))
    ok['C3'] = not (lnC3_lit <= lnC3_one)
    print('  C3 (control): "ln C3 <= %s" (the single-exponential value) refuted for the literal reading: %s' % (
        nstr(lnC3_one, 5), ok['C3']))
    ok['C1'] = lo > mpf(10) ** 18
    print('  C1 (control): "the factor is below 1e18" refuted: %s' % ok['C1'])
    ok['C2'] = poly < 10 ** 4
    print('  C2 (control): "the homogeneous growth exceeds 1e4" refuted: %s' % ok['C2'])
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
