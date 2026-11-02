#!/usr/bin/env python3
"""deltacap5: how small the proof's own formulas make delta and lambda1 (Theorem 4), certified (CONSTANTS5.md, D5).

EFFECTIVE-CONSTANTS.md Proposition 2.1 puts eps_NM := theta0^-(8d+2) with theta0 >= 16 (its first entry), and
Proposition 2.2 takes every admissible eps <= eps_NM/A_2d and delta := eps/2, lambda1 with C_R lambda1 < eps/2. So, with
the constants of upper bounds taken >= 1 (as Proposition 2.2's proof takes the tame constants; an upper-bound constant
may always be enlarged),

    delta <= 16^-(8d+2)/(2 A_2d) <= 2^-(32 d + 9),    lambda1 < eps/(2 C_R) <= delta.

These are upper bounds on what the proof's formulas can deliver, not lower bounds: the thresholds themselves stay
unevaluated (nrows5.py). With d at least the floor of LOSS-D.md LD16 (d > 7.959e15 at every admissible weight of the
record's point, READ) or of dweights5.py W3 at its weights (8,407,505,890,317,054, computed):

  P1 (certified) log10 2 > 59/196 (2^196 > 10^59, exact integers), so log10 delta < -(59/196)(32 d + 9).
  P2 (certified) at d = 7.959e15: log10 delta < -7.66e16; at dweights5's floor: < -8.09e16.
  P3 the same bound for lambda1 (C_R >= 1).
  Controls (must fail, and do): C1 the claim delta >= 10^(-7 x 10^16) is refuted; C2 at d = 1 (no loss) the same
  formula allows delta up to about 10^-12, so the size comes from d; C3 without the convention A_2d >= 1 no number is
  printed (the function refuses).

    python3 checks/deltacap5.py
"""
import sys
from fractions import Fraction as Fr

D_LOSSD = Fr(7959, 10 ** 3) * 10 ** 15          # READ: LOSS-D.md LD16 [D588], d > 7.959e15
D_W3 = 8407505890317054                          # computed: dweights5.out W3


def log10_delta_cap(d, A2d_at_least_one=True):
    """an upper bound for log10 delta from delta <= 2^-(32 d + 9)/A_2d, A_2d >= 1; None without the convention"""
    if not A2d_at_least_one:
        return None
    assert 2 ** 196 > 10 ** 59                   # log10 2 > 59/196
    return -Fr(59, 196) * (32 * Fr(d) + 9)


def main():
    ok = {}
    a = log10_delta_cap(D_LOSSD)
    b = log10_delta_cap(D_W3)
    print('  P1: 2^196 > 10^59: %s, so log10 2 > 59/196 = %.10f' % (2 ** 196 > 10 ** 59, 59 / 196))
    print('  P2: d >= 7.959e15 (LOSS-D LD16): log10 delta < %.6e' % float(a))
    print('      d >= %d (dweights5 W3): log10 delta < %.6e' % (D_W3, float(b)))
    print('  P3: lambda1 < delta: the same bounds (C_R >= 1)')
    ok['P2'] = a < -Fr(766, 10) * 10 ** 15 and b < -Fr(809, 10) * 10 ** 15
    ok['C1'] = a < -7 * 10 ** 16
    print('  C1 (control): the claim delta >= 10^(-7e16) contradicts log10 delta < %.4e: refuted' % float(a))
    c = log10_delta_cap(1)
    ok['C2'] = c > -13
    print('  C2 (control): at d = 1 the formula allows log10 delta up to %.3f' % float(c))
    ok['C3'] = log10_delta_cap(D_LOSSD, A2d_at_least_one=False) is None
    print('  C3 (control): without A_2d >= 1 no bound is printed: %s' % ok['C3'])
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
