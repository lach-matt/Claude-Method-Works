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

  P1 (certified) log10 2 > 59/196 (2^196 > 10^59, exact integers, tested on the ratio the bound uses), so log10 delta <
     -(59/196)(32 d + 9).
  P2 (certified) at d = 7.959e15: log10 delta < -7.66e16; at dweights5's floor: < -8.09e16.
  P3 the same bound for lambda1 (C_R >= 1).
  Controls (must fail, and do; rewritten in round 2, V-m3, so that each can fail on its own): C1 an unsound ratio,
  31/100 > log10 2, is refused by the same test that admits 59/196; C2 at d = 1 (no loss) the same formula allows
  delta up to about 10^-12, so the size comes from d; C3 (Round 3, the verifier's m2: round 2's C3 was forced by the
  code) P2's test run with A_2d >= 2^-(32 d + 9) in place of the convention A_2d >= 1 fails, so the printed number
  rests on that convention; C4 (Round 3, m2: round 2's C4 was implied by P2) P2's test run with theta0 >= 1 in place of
  Proposition 2.1's theta0 >= 16 fails, so the size comes from theta0's base together with d.

    python3 checks/deltacap5.py
"""
import sys
from fractions import Fraction as Fr

D_LOSSD = Fr(7959, 10 ** 3) * 10 ** 15          # READ: LOSS-D.md LD16 [D588], d > 7.959e15
D_W3 = 8407505890317054                          # computed: dweights5.out W3


def log10_delta_cap(d, ratio=Fr(59, 196), k_A=0, log2_theta0=4):
    """an upper bound for log10 delta from delta <= 2^-(32 d + 9)/A_2d with A_2d >= 2^-k_A (k_A = 0: the convention
    A_2d >= 1): -(32 d + 9) log10 2 + k_A log10 2 <= -ratio (32 d + 9) + k_A UP. Round 2 (V-m3): the soundness of
    ratio is checked on ratio itself (ratio < log10 2 iff 10^num < 2^den), not on a separate constant; an unsound
    ratio returns None."""
    if not 10 ** ratio.numerator < 2 ** ratio.denominator:
        return None
    assert 2 ** UP.denominator < 10 ** UP.numerator          # UP > log10 2
    return -ratio * (log2_theta0 * (8 * Fr(d) + 2) + 1) + k_A * UP     # 32 d + 9 at theta0 = 16


UP = Fr(30103, 100000)


def main():
    ok = {}
    R = Fr(59, 196)
    a = log10_delta_cap(D_LOSSD, R)
    b = log10_delta_cap(D_W3, R)
    print('  P1: the ratio used, 59/196 = %.10f, is below log10 2: 10^59 < 2^196: %s' % (float(R), 10 ** 59 < 2 ** 196))
    print('  P2: d >= 7.959e15 (LOSS-D LD16): log10 delta < %.6e' % float(a))
    print('      d >= %d (dweights5 W3): log10 delta < %.6e' % (D_W3, float(b)))
    print('  P3: lambda1 < delta: the same bounds (C_R >= 1)')
    def p2(x, y):
        return x is not None and y is not None and x < -Fr(766, 10) * 10 ** 15 and y < -Fr(809, 10) * 10 ** 15

    ok['P2'] = p2(a, b)
    bad = log10_delta_cap(D_LOSSD, Fr(31, 100))
    ok['C1'] = bad is None
    print('  C1 (control): the unsound ratio 31/100 > log10 2 is refused (no bound returned): %s' % ok['C1'])
    c = log10_delta_cap(1, R)
    ok['C2'] = c > -13
    print('  C2 (control): at d = 1 the formula allows log10 delta up to %.3f' % float(c))
    sa = log10_delta_cap(D_LOSSD, R, k_A=32 * D_LOSSD + 9)
    sb = log10_delta_cap(D_W3, R, k_A=32 * D_W3 + 9)
    ok['C3'] = not p2(sa, sb)
    print('  C3 (control): P2 with A_2d >= 2^-(32 d + 9) in place of A_2d >= 1: log10 delta < %.4e: P2 fails: %s'
          % (float(sa), ok['C3']))
    ta = log10_delta_cap(D_LOSSD, R, log2_theta0=0)
    tb = log10_delta_cap(D_W3, R, log2_theta0=0)
    ok['C4'] = not p2(ta, tb)
    print('  C4 (control): P2 with theta0 >= 1 in place of theta0 >= 16: log10 delta < %.4f: P2 fails: %s'
          % (float(ta), ok['C4']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
