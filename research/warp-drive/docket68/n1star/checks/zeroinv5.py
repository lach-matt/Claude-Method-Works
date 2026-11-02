#!/usr/bin/env python3
"""zeroinv5: an attempt at one of the seven inverse bounds behind lambda1 and delta, the cheapest by its site: I.C:497,
sigma_min of P-hat(0) at zero energy (CONSTANTS5.md, Round 4, item (iii)). Done here for the scalar model at b0 (the
wave operator of 5D Tangherlini, the operator E2-PILOT.md certifies at sigma != 0), harmonic by harmonic in the T^2
class (class5.py C2: one scalar harmonic at each even l), on the exterior. Labels: computed (exact, sympy), deduced.

At sigma = 0 the radial operator on the degree-l harmonic is A_l u = -r^-3 (r^3 f u')' + l (l + 2) r^-2 u, f = 1 -
     mu/r^2,
r > r_h = mu^(1/2) (READ: E2-PILOT.md (1.1) at sigma = 0, undoing Phi = r^(3/2) u).

  Z1 (exact) The zero-energy solutions in closed form: with y = 2 r^2/mu - 1, u_h = P_(l/2)(y) (a polynomial for even l,
     smooth across the horizon y = 1) solves A_l u = 0 for l = 0, 2, 4, 6, 8; it grows like r^l, so no solution
     regular at
     the horizon decays and the zero-energy family has no kernel on any even l >= 2 in decaying weights (deduced; at l =
     0, u_h = 1). Control C1: Z1's test on the next polynomial, P_((l+2)/2): it fails.
  Z2 (exact) The energy identity r^3 conj(u) A_l u = -(r^3 f conj(u) u')' + r^3 f |u'|^2 + l (l + 2) r |u|^2, symbolic
     in u; integrated over (r_h, oo) the boundary term vanishes at r_h (f = 0) and at oo for u = O(r^-2) with u' =
     O(r^-3). Hence, for l >= 1, with ||.|| the norm of L^2(r^3 dr): l (l + 2) ||r^-1 u||^2 <= <A_l u, u> <= ||r A_l u||
     ||r^-1 u||, so ||r^-1 u|| <= ||r A_l u|| / (l (l + 2)), the inverse bound on the class harmonic l with the explicit
     constant 1/(l (l + 2)) <= 1/8 for every even l >= 2 (certified: exact identity, exact constant). Control C2: the
     identity with l (l + 1) (the four-dimensional eigenvalue): fails.
  Z3 (deduced) What this is not: the norm of I.C (3.2) is H-bar^(s,alpha)_b with s > 1/2 + theta_H, extendible across
     the horizon, with derivatives; Z2 is an exterior L^2 bound with weights r^-1 and r, without the horizon (where f
     vanishes and the identity gives no control of u' at r_h) and without l = 0 (where the term l (l + 2) vanishes and a
     Hardy inequality with f's degeneracy would be needed); and the operator of the settling theorem is L_b0 on 15
     components, whose zero-energy kernel is eleven-dimensional (the record's 10.32 (c)), so I.C:497's sigma_min is on
     the complement of that kernel.

    python3 checks/zeroinv5.py      (seconds)
"""
import builtins
import sys
import textwrap

import sympy as sp

r, mu = sp.symbols('r mu', positive=True)
OK = {}


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(x) for x in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False), **k)


def A(u, l, kap=None):
    f = 1 - mu / r ** 2
    k = l * (l + 2) if kap is None else kap
    return -sp.diff(r ** 3 * f * sp.diff(u, r), r) / r ** 3 + k * u / r ** 2


def z1(shift=0):
    res = {}
    for l in (0, 2, 4, 6, 8):
        y = 2 * r ** 2 / mu - 1
        u = sp.legendre((l + shift) // 2, y)
        res[l] = sp.simplify(A(sp.expand(u), l)) == 0
    return res


def z2(kap_fn=lambda l: l * (l + 2)):
    u = sp.Function('u')(r)
    ub = sp.Function('ub')(r)                          # conj(u), an independent function
    f = 1 - mu / r ** 2
    out = {}
    for l in (1, 2, 4, 10):
        lhs = r ** 3 * ub * A(u, l)
        rhs = -sp.diff(r ** 3 * f * ub * sp.diff(u, r), r) + r ** 3 * f * sp.diff(ub, r) * sp.diff(u, r) + \
            kap_fn(l) * r * ub * u
        out[l] = sp.simplify(sp.expand(lhs - rhs)) == 0
    return out


def main():
    r1 = z1()
    OK['Z1'] = all(r1.values())
    print('  Z1: u_h = P_(l/2)(2 r^2/mu - 1) solves A_l u = 0 (exact): %s' % r1)
    c1 = z1(shift=2)
    OK['C1'] = not any(c1.values())
    print('  C1 (control): the next polynomial, P_((l+2)/2), in Z1\'s test: solves for none: %s' % OK['C1'])
    r2 = z2()
    OK['Z2'] = all(r2.values())
    print('  Z2: r^3 conj(u) A_l u = -(r^3 f conj(u) u\')\' + r^3 f |u\'|^2 + l (l + 2) r |u|^2 (exact, '
        'symbolic u): %s; '
          'so ||r^-1 u|| <= ||r A_l u||/(l (l + 2)) in L^2(r^3 dr) for l >= 1: constants %s at l = 2, 4, 6, 8 (<= 1/8 '
          'for every even l >= 2)' % (r2, [str(sp.Rational(1, l * (l + 2))) for l in (2, 4, 6, 8)]))
    c2 = z2(lambda l: l * (l + 1))
    OK['C2'] = not any(c2.values())
    print('  C2 (control): the identity with l (l + 1): holds for none: %s' % OK['C2'])
    for k, v in OK.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
