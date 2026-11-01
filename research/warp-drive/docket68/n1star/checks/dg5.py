#!/usr/bin/env python3
"""dg5: III.G' Theorem 3.1 (2)'s loss d_G on the iota+ window at admissible l_I (LOSS-D LD16, D562).

LOSS-D section 2, item 6, (2.5): d(lam) = 6 + ceil(max(0, Re lam - 2 + delta)) + ceil(max(0, Re lam - 3/2) + delta)
+ 2 ceil(l_I - Re lam), that is 7 + 2 ceil(l_I - Re lam) for 3/2 - delta < Re lam < 2 - delta. The iota+ window of
III.I''''' Proposition 2.1 runs over Re lam in [lam_sharp, alpha_sharp_+), lam_sharp = 1.5099, alpha_sharp_+ = 2 - eps
(LD14). The weight l_I is to be chosen (E1'a) in (3 + eps_+, min(a_I + 1/2, l_I^max)) ((H4), I11:46-48; I2:251-252),
a_I > 3 + eps_+ ((H4)), the source's a_I = 3 + eps_I with eps_I < 1 (PART-III-I-CONE.md:68, 472-473), l_I^max > 100
(I2:31).

  G1 (exact) for every l_I in (3, 3.5) (sampled at 1/1000 steps) and every Re lam in [lam_sharp, 2 - eps) with delta <
     eps (a free choice), d_G = 11: ceil(l_I - Re lam) = 2 there, l_I - lam_sharp < 1.9901 and l_I - (2 - eps) > 1.
  G2 (exact) with the source's a_I = 3 + eps_I, eps_I < 1, l_I < 4.5: max d_G on the window is 13; if delta >= eps
     the top of the window, Re lam in [2 - delta, 2 - eps), adds the two first ceilings' 1 and gives at most 14.
  G3 (exact) every admissible a_I allows l_I in (3 + eps_+, 3.5): min(a_I + 1/2, l_I^max) > 3.5 + eps_+.

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
    g1 = {d25(l, Fr(3) + Fr(k, 1000), delta) for k in range(1, 500) for l in lams}
    ok['G1'] = g1 == {11}
    print('  G1: d_G over l_I in (3, 3.5), Re lam in [1.5099, 2 - eps), delta < eps: %s' % sorted(g1))
    g2 = max(d25(l, Fr(3) + Fr(k, 1000), delta) for k in range(1, 1500) for l in lams)
    big = Fr(1, 10**5)                                   # delta >= eps
    lams_top = lams + [2 - big + (big - eps) * Fr(k, 10) for k in range(10)]
    g2b = max(d25(l, Fr(3) + Fr(k, 1000), big) for k in range(1, 1500) for l in lams_top)
    ok['G2'] = g2 == 13 and g2b == 14
    print('  G2: l_I up to 4.5 (a_I = 3 + eps_I, eps_I < 1): max d_G %d; with delta >= eps, %d' % (g2, g2b))
    epsp = Fr(1, 10**6)
    ok['G3'] = all(min(a + Fr(1, 2), Fr(100)) > Fr(7, 2) + epsp for a in (Fr(3) + epsp + Fr(1, 10**9), Fr(31, 10), 4))
    print('  G3: (3 + eps_+, 3.5) lies in the admissible range for every a_I > 3 + eps_+: %s' % ok['G3'])
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
