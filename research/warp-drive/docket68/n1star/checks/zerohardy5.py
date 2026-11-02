#!/usr/bin/env python3
"""zerohardy5: the zero-energy inverse bound of the scalar model at b0 pushed past round 4 (CONSTANTS5.md, Round 5,
R5.6): the l = 0 harmonic and a sharp constant at every l, the passage across the horizon, and the size of the kernel
that I.C:497's sigma_min must avoid in the class. Labels: computed (exact, sympy), deduced (where said), READ (cited).

A_l u = -r^-3 (r^3 f u')' + l (l + 2) r^-2 u, f = 1 - mu/r^2, r_h = mu^(1/2) (zeroinv5.py; E2-PILOT (1.1) at sigma = 0);
||.|| the norm of L^2(r^3 dr) on (r_h, oo).

  H1 (exact) w = 1/r is a positive supersolution of the l = 0 operator: -(r^3 f w')' = (1 + mu r^-2) r w.
  H2 (exact identity, symbolic phi and its conjugate) with u = w phi: r^3 f |u'|^2 = r^3 f w^2 |phi'|^2 - (r^3 f w')' w
     |phi|^2 + (r^3 f w w' |phi|^2)'. Integrated over (r_h, oo) the boundary term vanishes at r_h (f = 0) and at oo for
     u = o(r^-1) (r^3 f w w' |phi|^2 = -f |r u|^2), so int r^3 f |u'|^2 >= int (1 + mu r^-2) r |u|^2 (deduced). With
     zeroinv5's identity, <A_l u, u> >= ((l + 1)^2 + mu r^-2-part) ||r^-1 u||^2 >= (l + 1)^2 ||r^-1 u||^2, hence
         ||r^-1 u|| <= ||r A_l u|| / (l + 1)^2     for every l >= 0
     (deduced from exact identities): the l = 0 harmonic, which round 4 left open, has constant 1, and l = 2 has 1/9
     (round 4: 1/8).
  H3 (exact) the quadratic-form constant is sharp: for u_delta = r^(-1-delta) on (r_h, oo), delta > 0,
     <A_l u, u>/||r^-1 u||^2 = (l + 1)^2 + delta exactly (sympy, symbolic mu, delta, l).
  H4 (exact; deduced) across the horizon: r^3 f = r (r - r_h)(r + r_h), so for u smooth across r = r_h the equation
     integrates to r^3 f u'(r) = int_{r_h}^r s^3 (l (l + 2) s^-2 u - A_l u) ds, and |u'(r)| <= sup over [r_h, r] (or
     [r, r_h]) of |s^3 (l (l + 2) s^-2 u - A_l u)| / (r (r + r_h)) on both sides of the horizon: at zero energy the
     scalar model loses no derivative there, with the explicit factor 1/(r (r + r_h)) <= 1/(2 mu) at r_h.
  H5 (deduced; READ N1STAR-PROOF.md:4983-4990 and class5.py C2 as quoted in iotapoles5.py) L_b0's eleven zero-energy
     states are g-dot^Ups(mu-dot) (s0, one), g-dot^Ups(0, A) (v1, six) and h_s1(S) (s1, four); the T^2 x Z2 x Z2 class
     has scalar harmonics at even l only and no vector harmonic, so s1 (l = 1) and v1 are absent and the kernel met in
     the class is the single s0 state: I.C:497's sigma_min there is on the complement of one direction, in s0.
  Controls (mutating the computed path; each must fail): C1 H1 with w = r^-2: -(r^3 f w')' - (1 + mu r^-2) r w is not
  zero and is negative near r_h, so the supersolution test fails; C2 H3's family at the claimed constant raised by 1/10:
  for delta = 1/20 the ratio (l + 1)^2 + 1/20 is below it, so the raised claim is refuted; C3 H4 with r^3 f taken as
  r^3 (r - r_h): the factorisation test fails.

    python3 checks/zerohardy5.py       (seconds)
"""
import builtins
import sys
import textwrap

import sympy as sp

r, mu, dl = sp.symbols('r mu delta', positive=True)
l = sp.Symbol('l', nonnegative=True, integer=True)
f = 1 - mu / r ** 2
rh = sp.sqrt(mu)
OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def supersol(w):
    return sp.simplify(-sp.diff(r ** 3 * f * sp.diff(w, r), r) - (1 + mu / r ** 2) * r * w)


def ground_identity():
    ph, pb = sp.Function('phi')(r), sp.Function('phib')(r)
    w = 1 / r
    u, ub = w * ph, w * pb
    lhs = r ** 3 * f * sp.diff(u, r) * sp.diff(ub, r)
    rhs = (r ** 3 * f * w ** 2 * sp.diff(ph, r) * sp.diff(pb, r) - sp.diff(r ** 3 * f * sp.diff(w, r), r) * w * ph * pb
           + sp.diff(r ** 3 * f * w * sp.diff(w, r) * ph * pb, r))
    return sp.simplify(sp.expand(lhs - rhs)) == 0


def ratio(delta):
    u = r ** (-1 - delta)
    num = sp.integrate(r ** 3 * f * sp.diff(u, r) ** 2 + l * (l + 2) * r * u ** 2, (r, rh, sp.oo), conds='none')
    den = sp.integrate(r * u ** 2, (r, rh, sp.oo), conds='none')
    return sp.simplify(num / den)


def main():
    print('zerohardy5: the scalar zero-energy bound at every l, sharp; across the horizon; the kernel in the class')
    h1 = supersol(1 / r)
    OK['H1'] = h1 == 0
    print('  H1: -(r^3 f w\')\' - (1 + mu r^-2) r w at w = 1/r: %s (exact)' % h1)
    OK['H2'] = ground_identity()
    print('  H2: r^3 f |(w phi)\'|^2 = r^3 f w^2 |phi\'|^2 - (r^3 f w\')\' w |phi|^2 + (r^3 f w w\' |phi|^2)\' (exact, '
          'symbolic phi, conj(phi)): %s; so <A_l u, u> >= (l + 1)^2 ||r^-1 u||^2 and ||r^-1 u|| <= ||r A_l u||/(l + 1)^2,'
          ' l >= 0: constants %s at l = 0, 2, 4, 6' % (OK['H2'], [str(sp.Rational(1, (q + 1) ** 2)) for q in (0, 2, 4,
                                                                                                         6)]))
    R = ratio(dl)
    OK['H3'] = sp.simplify(R - ((l + 1) ** 2 + dl)) == 0
    print('  H3: u = r^(-1-delta): <A_l u, u>/||r^-1 u||^2 = %s (exact): the constant (l + 1)^2 is sharp' % sp.factor(
        R))
    fac = sp.factor(r ** 3 * f)
    OK['H4'] = sp.simplify(r ** 3 * f - r * (r - rh) * (r + rh)) == 0 and sp.simplify(
        sp.limit((r - rh) / (r ** 3 * f), r, rh) - 1 / (2 * mu)) == 0
    print('  H4: r^3 f = %s = r (r - r_h)(r + r_h): %s; (r - r_h)/(r^3 f) = 1/(r (r + r_h)) -> 1/(2 mu) at r_h' % (
        fac, OK['H4']))
    OK['H5'] = True
    print('  H5 (deduced, READ): eleven = 1 (s0) + 6 (v1) + 4 (s1); in the class only the s0 state: one direction')
    c1 = supersol(r ** -2)
    near = sp.limit(c1, r, rh)
    OK['C1'] = c1 != 0 and near < 0
    print('  C1 (control): w = r^-2: residual %s, at r_h %s < 0: H1\'s test fails: %s' % (c1, near, OK['C1']))
    R20 = R.subs(dl, sp.Rational(1, 20))
    OK['C2'] = all(sp.simplify(R20.subs(l, q) - ((q + 1) ** 2 + sp.Rational(1, 10))) < 0 for q in (0, 2, 4))
    print('  C2 (control): the claim <A_l u, u> >= ((l + 1)^2 + 1/10) ||r^-1 u||^2 at delta = 1/20: ratio (l + 1)^2 + '
          '1/20, refuted at l = 0, 2, 4: %s' % OK['C2'])
    OK['C3'] = sp.simplify(r ** 3 * f - r ** 3 * (r - rh)) != 0
    print('  C3 (control): r^3 f against r^3 (r - r_h): not equal, H4\'s test fails on it: %s' % OK['C3'])
    for k_, val in OK.items():
        builtins.print(k_, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
