#!/usr/bin/env python3
"""dg5: III.G' Theorem 3.1 (2)'s loss d_G on the iota+ window at admissible l_I (LOSS-D LD16, D562; corrected D565).

LOSS-D section 2, item 6, (2.5): d(lam) = 6 + ceil(max(0, Re lam - 2 + delta)) + ceil(max(0, Re lam - 3/2) + delta)
+ 2 ceil(l_I - Re lam), that is 7 + 2 ceil(l_I - Re lam) for 3/2 - delta < Re lam < 2 - delta. The iota+ window of
the record's III.I (five primes) Proposition 2.1 at the levels below 3 runs over Re lam in [lam_sharp, 2 - eps),
lam_sharp = 1.5099 (LD14). The weight l_I is chosen (E1'a) with l_I > 3 + eps_+ ((H4), I11:46-47) and, on the
record's two upper bounds, l_I < a_I + 1/2 (III.I' Proposition 2.1, I2:251-252) and l_I <= a_I (III.I''''
Proposition 4.1, I5:319, carried by I8:47, I9:31, I10:37, I11:47), both in force from I5 on, the second binding
(D570: not two readings, as D565 had them), and l_I < l_I^max (> 100, I2:31). a_I is free (> 3/2, I-CONE:65); (H4) asks a_I > 3 +
eps_+ on the first reading (I11:47); the source's a_I = 3 + eps_I (I-CONE:68), eps_I bounded only through
min(eps_ind, eps_I) < 1 (I-CONE:472-473).

  G1 (exact, by the breakpoints) ceil(l_I - Re lam) = 2 for every l_I in (3 - eps, lam_sharp + 2] = (3 - eps, 3.5099]
     and every Re lam in [lam_sharp, 2 - eps): l_I - Re lam <= l_I - lam_sharp <= 2 and > l_I - 2 + eps > 1; with
     delta < eps the first ceiling is 0 and the second 1, so d_G = 11. Also sampled (499 l_I in (3, 3.5), 400 lam).
  G2 (sampled) if l_I may reach 4.5 (eps_I < 1, which the record does not state; verifier 246), the window's max
     d_G is 13, and 14 at its top if delta >= eps; eps_I = 1.6 with l_I = 4.55 would give 15 (verifier 246).
  G3 (exact) on either reading, for every a_I > 3 + eps_+ (sampled at a_I = 3 + eps_+ + 1e-9, 3.1, 3.4, 4, 10), the
     admissible l_I meet (3 + eps_+, 3.5099], so some admissible l_I gives d_G = 11; (3 + eps_+, 3.5) itself is
     admissible for every a_I only on the reading l_I < a_I + 1/2 (on l_I <= a_I it needs a_I >= 3.5).

Run: python3 checks/dg5.py
"""
import math
import sys
from fractions import Fraction as Fr


def d25(lam, lI, delta):
    return (6 + math.ceil(max(Fr(0), lam - 2 + delta)) + math.ceil(max(Fr(0), lam - Fr(3, 2)) + delta)
            + 2 * math.ceil(lI - lam))


def main():
    ok = {}
    ls = Fr(15099, 10000)
    eps, delta = Fr(1, 10**6), Fr(1, 10**7)
    lams = [ls + (2 - eps - ls) * Fr(k, 400) for k in range(400)]
    # G1: the breakpoints, then the sample
    top = ls + 2
    lo_ok = (3 - eps) - (2 - eps) == 1 and top - ls == 2          # l_I - lam in (1, 2] on the closed ranges
    g1 = {d25(l, Fr(3) + Fr(k, 1000), delta) for k in range(1, 500) for l in lams}
    g1 |= {d25(l, top, delta) for l in lams}
    ok['G1'] = lo_ok and g1 == {11}
    print('  G1: ceil(l_I - Re lam) = 2 on (3 - eps, 3.5099] x [1.5099, 2 - eps) by the breakpoints; sampled d_G: %s'
          % sorted(g1))
    g2 = max(d25(l, Fr(3) + Fr(k, 1000), delta) for k in range(1, 1500) for l in lams)
    big = Fr(1, 10**5)                                             # delta >= eps
    lams_top = lams + [2 - big + (big - eps) * Fr(k, 10) for k in range(10)]
    g2b = max(d25(l, Fr(3) + Fr(k, 1000), big) for k in range(1, 1500) for l in lams_top)
    g2c = max(d25(l, Fr(455, 100), delta) for l in lams)
    ok['G2'] = g2 == 13 and g2b == 14 and g2c == 15
    print('  G2: l_I up to 4.5 (if eps_I < 1, not stated in the record): max d_G %d; with delta >= eps, %d; at l_I = '
          '4.55 (eps_I = 1.6), %d' % (g2, g2b, g2c))
    epsp = Fr(1, 10**6)
    a_s = (Fr(3) + epsp + Fr(1, 10**9), Fr(31, 10), Fr(34, 10), Fr(4), Fr(10))
    meet = all(min(a, top) > 3 + epsp and min(a + Fr(1, 2), Fr(100), top) > 3 + epsp for a in a_s)
    short = [a for a in a_s if a < Fr(7, 2)]                       # on l_I <= a_I, (3 + eps_+, 3.5) not all admissible
    ok['G3'] = meet and len(short) == 3
    print('  G3: on both readings the admissible l_I meet (3 + eps_+, 3.5099] for a_I in %s: %s; on l_I <= a_I, '
          '(3 + eps_+, 3.5) is not wholly admissible at %d of the five' % ([str(a) for a in a_s], meet, len(short)))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
