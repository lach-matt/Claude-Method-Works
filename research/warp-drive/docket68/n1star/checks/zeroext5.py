#!/usr/bin/env python3
"""zeroext5: the scalar model's zero-energy inverse bound carried into the norm of I.C (3.2), at s = 1 and alpha = -1,
on the extended domain through the horizon, with one constant for every harmonic (CONSTANTS5.md, Round 6, item 3).
Labels: computed (exact, sympy; exact rationals), certified (rational enclosures), deduced (the inequalities drawn from
the identities, stated with each item), floating point (where said).

The model (zeroinv5.py, zerohardy5.py; E2-PILOT (1.1) at sigma = 0): on harmonic l of S^3,
    A_l u = -r^-3 (P u')' + L r^-2 u,   P := r^3 f = r^3 - mu r,  L := l (l + 2),
on r in [r_in, oo), r_in = theta r_h, 0 < theta < 1 (the extended domain of I.A: the slice continues inside the horizon
to an artificial boundary at which nothing is imposed; cover5.py used theta = 1/2 at mu = 1). I.C (3.2) reads
||u||_{Hbar^(s, alpha)_b} <= C ||P-hat(0) u||_{Hbar^(s-1, alpha+2)_b}, and Hbar^(0, alpha)_b = rho^alpha L^2(|dx|)
(I.C Remark (a)), |dx| = r^3 dr dOmega. Per harmonic, with the b-fields r d_r and the six Killing fields of S^3 (whose
squares sum to -Delta_S = L on harmonic l):
    N(u)^2 := int_{r_in}^oo (r |u|^2 + r^3 |u'|^2 + L r |u|^2) dr = ||u||^2 of Hbar^(1, -1)_b,
    F^2    := int_{r_in}^oo r^5 |A_l u|^2 dr                   = ||A_l u||^2 of Hbar^(0, 1)_b.
alpha + 2 = 1 lies in the indicial gap (0, 2) of the model at infinity (its roots are -l and l + 2, Z0): (G) holds.

  Z0 (exact) the indicial roots of r^2 A_l at r = oo: -l and l + 2 in rho = 1/r; the gap containing 1 is (0, 2); and
     N, F, A_l are invariant under r -> mu^(1/2) r up to the common factor mu (N^2 and F^2 both scale by mu): mu = 1
     below, r_h = 1, P = r^3 - r.
  Z1 (exact identity, symbolic u and conj(u)) for any weight w(r): with the equation -(P u')' + L r u = r^3 g,
        d/dr[ (1/2) P w |u'|^2 - (1/2) L r w |u|^2 ] + (1/2)(P' w - P w') |u'|^2 + (1/2) L (r w)' |u|^2
          = -Re(r^3 g w conj(u')),
     an identity in u, u', u'' once g := A_l u is substituted (checked as a polynomial identity).
  Z2 (exact) at w = r: P' w - P w' = 2 r^3 > 0 and (r w)' = 2 r > 0 for every r > 0; at a = r_in in (0, 1) the
     boundary terms -(1/2) P(a) w(a) |u'(a)|^2 = (1/2) a^2 (1 - a^2) |u'(a)|^2 and (1/2) L a^2 |u(a)|^2 are >= 0, and at
     b > 1 the term (1/2) P(b) b |u'(b)|^2 >= 0. So (deduced) for every b > 1:
        int_a^b r^3 |u'|^2 + L int_a^b r |u|^2 <= (L/2) b^2 |u(b)|^2 + F (int_a^b r^3 |u'|^2)^(1/2),
     hence X^2 := int_a^b r^3 |u'|^2 <= F^2 + L b^2 |u(b)|^2 and L int_a^b r |u|^2 <= F^2 + L b^2 |u(b)|^2.
     The inside of the horizon enters with the right sign because P < 0 there: the artificial boundary is final.
  Z3 (deduced from zerohardy5.py H1-H2) on the exterior (1, oo), the boundary terms vanishing at r = 1 (P(1) = 0):
        (l + 1)^2 int_1^oo r |u|^2 <= <A_l u, u> = int_1^oo P |u'|^2 + L int_1^oo r |u|^2 <= F_ext^2/(l + 1)^2.
  Z4 (deduced; certified) choosing b in [b1, b2] where b^2 |u(b)|^2 is least, L b^2 |u(b)|^2 <= kappa L int_1^oo r|u|^2
     <= kappa F^2/(l + 1)^2, kappa = b2/(b2 - b1); on (b1, oo), int r^3 |u'|^2 <= int P |u'|^2/f(b1); at l = 0,
     |u(r)| <= |u(b)| + (int_r^b t^3 |u'|^2)^(1/2) (2 r^2)^(-1/2) gives int_a^1 r |u|^2 <= F^2 (kappa (1 - a^2) +
     log(1/a)). Summed: N(u)^2 <= C_l^2 F^2 with
        C_0^2 = 1 + kappa (1 - a^2) + log(1/a) + 1 + 1/f(b1),
        C_l^2 = (l+1)^-4 + (1 + kappa (l+1)^-2)(2 + 1/L) + (l+1)^-2 (1 + 1/f(b1))   (l >= 1),
     certified at a = 1/2, b1 = 6/5, b2 = 2: sup_l C_l^2 = C_0^2 < 7.85, C < 2.802. Summed over harmonics (every term
     of N and F is diagonal in l): ||u||_{Hbar^(1,-1)_b} <= 2.802 ||A u||_{Hbar^(0,1)_b} for the scalar model at b0 on
     [r_h/2, oo) x S^3, every u smooth up to r_in and decaying at oo.
  Z5 (floating point) test functions u (sums of Gaussian bumps, also across r = 1 and at r_in, and a tail r^-2): the
     ratio N/F over 300 of them at l in {0, 2, 4, 6} stays below C; its largest value is printed.
  Z5b (exact) the near-extremal family u = r^(-1-delta) on [1/2, oo) (smooth there): A_l u = c1 r^(-3-delta) + c2
     r^(-5-delta), c1 = (l + 1)^2 - delta^2, c2 = (1 + delta)^2 (mu = 1), N^2 and F^2 integrated exactly; N/F -> 2^(1/2)
     at l = 0 as delta -> 0 (exterior Hardy sharpness), below C: the constant C is within a factor 2 of the best.
  Controls (each mutates the computed path; each must fail): C1 Z2 with w = 1: P' w - P w' = 3 r^2 - 1 < 0 at
  r = 1/2, the positivity test fails; C2 Z1 with the boundary term's L r w |u|^2 sign flipped: the identity fails;
  C3 Z5b's test against the claim C/4: refuted by u = r^(-1-1/100).

    python3 checks/zeroext5.py       (a minute)
"""
import builtins
import math
import sys
import textwrap
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


r, mu, t = sp.symbols('r mu t', positive=True)
Ls = sp.Symbol('L', nonnegative=True)


def z0():
    lam, l = sp.symbols('lambda l')
    rho = sp.Symbol('rho', positive=True)
    # A_l (rho^lambda) at leading order in rho = 1/r, flat part (the mu-terms are lower order at infinity)
    u = r ** (-lam)
    P = r ** 3
    Au = sp.simplify(-r ** -3 * sp.diff(P * sp.diff(u, r), r) + l * (l + 2) * r ** -2 * u)
    ind = sp.factor(sp.simplify(Au / r ** (-lam - 2)))
    roots = sp.solve(ind, lam)
    ok_roots = set(sp.simplify(x) for x in roots) == {-l, l + 2}
    # scaling: u(r) -> u(r / mu^(1/2)): N^2 and F^2 both pick up mu
    uf = sp.Function('U')
    sc = sp.sqrt(mu)
    P_mu = r ** 3 - mu * r
    A_mu = lambda v: -r ** -3 * sp.diff(P_mu * sp.diff(v, r), r) + Ls * r ** -2 * v  # noqa: E731
    v = uf(r / sc)
    lhs = sp.simplify(A_mu(v).subs(r, sc * t))
    rhs = sp.simplify((-t ** -3 * sp.diff((t ** 3 - t) * sp.diff(uf(t), t), t) + Ls * t ** -2 * uf(t)) / mu)
    ok_scale = sp.simplify(lhs - rhs) == 0
    return ok_roots, ok_scale, roots


def identity(sign_flip=False):
    """Z1: the multiplier identity as a polynomial identity in u, u', u'' (and conjugates)"""
    w = sp.Function('w')(r)
    P = r ** 3 - r
    u0, u1, u2, v0, v1, v2 = sp.symbols('u0 u1 u2 v0 v1 v2')        # u, u', u''; conj(u), conj(u'), conj(u'')
    # g := A u, conj(g) = A conj(u) (L, P real)
    g = (-(sp.diff(P, r) * u1 + P * u2) + Ls * r * u0) / r ** 3
    gb = (-(sp.diff(P, r) * v1 + P * v2) + Ls * r * v0) / r ** 3
    s = -1 if sign_flip else 1
    B = sp.Rational(1, 2) * P * w * u1 * v1 - s * sp.Rational(1, 2) * Ls * r * w * u0 * v0
    # d/dr of B along the jet: d/dr u0 = u1, d/dr u1 = u2 (and conjugates)
    dB = sp.diff(B, r) + sp.diff(B, u0) * u1 + sp.diff(B, u1) * u2 + sp.diff(B, v0) * v1 + sp.diff(B, v1) * v2
    bulk = (sp.Rational(1, 2) * (sp.diff(P, r) * w - P * sp.diff(w, r)) * u1 * v1
            + sp.Rational(1, 2) * Ls * sp.diff(r * w, r) * u0 * v0)
    rhs = -sp.Rational(1, 2) * (r ** 3 * g * w * v1 + r ** 3 * gb * w * u1)
    return sp.simplify(sp.expand(dB + bulk - rhs)) == 0


def z2(w):
    P = r ** 3 - r
    pos = sp.simplify(sp.diff(P, r) * w - P * sp.diff(w, r))
    rw = sp.simplify(sp.diff(r * w, r))
    a = sp.Symbol('a', positive=True)
    bd = sp.simplify(-(P * w).subs(r, a))
    return pos, rw, bd


def constants(a=Fr(1, 2), b1=Fr(6, 5), b2=Fr(2), lmax=200):
    """certified C_l^2 (rational upper bounds; log(1/a) by an upper rational)"""
    kappa = b2 / (b2 - b1)
    finv = 1 / (1 - 1 / b1 ** 2)
    log_hi = Fr(693148, 10 ** 6)                           # log 2 = 0.693147... < 0.693148
    assert a == Fr(1, 2) and math.log(2) < float(log_hi)
    C0 = 1 + kappa * (1 - a * a) + log_hi + 1 + finv
    Cl = {0: C0}
    for l in range(1, lmax + 1):
        L = l * (l + 2)
        q = Fr(1, (l + 1) ** 2)
        Cl[l] = q * q + (1 + kappa * q) * (2 + Fr(1, L)) + q * (1 + finv)
    # for l > lmax the expression decreases to 2 (monotone: each term decreases in l)
    tail = 2 + Fr(0)
    return kappa, finv, Cl, tail


def norms_numeric(u_fn, du_fn, Au_fn, L, a=0.5, R=60.0, n=24001):
    x = np.linspace(a, R, n)
    u, du, Au = u_fn(x), du_fn(x), Au_fn(x)
    N2 = np.trapezoid(x * u ** 2 + x ** 3 * du ** 2 + L * x * u ** 2, x)
    F2 = np.trapezoid(x ** 5 * Au ** 2, x)
    return math.sqrt(N2), math.sqrt(F2)


def test_functions(seed=7, count=300):
    rng = np.random.default_rng(seed)
    rs = sp.Symbol('r', positive=True)
    out = []
    for i in range(count):
        k = rng.integers(1, 4)
        expr = 0
        for _ in range(k):
            c = float(rng.uniform(0.5, 6.0))
            wdt = float(rng.uniform(0.05, 1.5))
            amp = float(rng.normal())
            expr += amp * sp.exp(-((rs - c) / wdt) ** 2)
        if i % 5 == 0:
            expr += float(rng.normal()) * rs ** -2 * (1 - sp.exp(-rs ** 4))
        out.append(expr)
    return rs, out


def main():
    print('zeroext5: the scalar zero-energy bound in the norm of I.C (3.2), s = 1, alpha = -1, through the horizon')
    ok_roots, ok_scale, roots = z0()
    OK['Z0'] = ok_roots and ok_scale
    print('  Z0: indicial roots of r^2 A_l at infinity in rho = 1/r: %s; the gap containing alpha + 2 = 1 is (0, 2); '
          'scale invariance under r -> mu^(1/2) r (A_l -> A_l/mu): %s' % (roots, ok_scale))
    OK['Z1'] = identity()
    print('  Z1: d/dr[(1/2) P w |u\'|^2 - (1/2) L r w |u|^2] + (1/2)(P\'w - P w\')|u\'|^2 + (1/2) L (r w)\' |u|^2 = '
          '-Re(r^3 g w conj u\'), g = A_l u, for every weight w (exact, polynomial in the jet): %s' % OK['Z1'])
    pos, rw, bd = z2(r)
    a = sp.Symbol('a', positive=True)
    OK['Z2'] = (sp.simplify(pos - 2 * r ** 3) == 0 and sp.simplify(rw - 2 * r) == 0
                and sp.simplify(bd - a ** 2 * (1 - a ** 2)) == 0)
    print('  Z2: at w = r: P\'w - P w\' = %s, (r w)\' = %s, -P(a) w(a) = %s (>= 0 for 0 < a < 1): %s' % (
        pos, rw, sp.factor(bd), OK['Z2']))
    kappa, finv, Cl, tail = constants()
    sup = max(Cl.values())
    lsup = max(Cl, key=lambda q: Cl[q])
    mono = all(Cl[q] >= Cl[q + 1] for q in range(1, 200))
    OK['Z4'] = sup < Fr(785, 100) and lsup == 0 and mono and Cl[200] > tail
    C = math.sqrt(float(sup))
    print('  Z4 (certified, exact rationals): kappa = %s, 1/f(b1) = %s; C_0^2 <= %.6f, C_1^2 <= %.6f, C_2^2 <= %.6f, '
          'C_l^2 decreasing to 2 (checked to l = 200, each term decreasing beyond): sup_l C_l^2 = C_0^2 < 7.85, so '
          '||u||_(1,-1) <= %.4f ||A u||_(0,1) on [r_h/2, oo) x S^3: %s' % (
              kappa, finv, float(Cl[0]), float(Cl[1]), float(Cl[2]), C, OK['Z4']))
    # Z5 floating point tests
    rs, fns = test_functions()
    worst = 0.0
    for l in (0, 2, 4, 6):
        L = l * (l + 2)
        for e in fns:
            Pm = rs ** 3 - rs
            Ae = -rs ** -3 * sp.diff(Pm * sp.diff(e, rs), rs) + L * rs ** -2 * e
            fu = sp.lambdify(rs, e, 'numpy')
            fd = sp.lambdify(rs, sp.diff(e, rs), 'numpy')
            fA = sp.lambdify(rs, Ae, 'numpy')
            Nn, Fn = norms_numeric(fu, fd, fA, L)
            if Fn > 0:
                worst = max(worst, Nn / Fn)
    OK['Z5'] = worst <= 2.802
    print('  Z5 (floating point): 300 test functions x l in {0, 2, 4, 6}: largest N(u)/F = %.4f <= 2.802: %s' % (
        worst, OK['Z5']))
    # controls
    pos1, _, _ = z2(sp.Integer(1))
    OK['C1'] = sp.simplify(pos1.subs(r, sp.Rational(1, 2))) < 0
    print('  C1 (control): w = 1: P\'w - P w\' = %s, at r = 1/2 it is %s < 0: Z2\'s positivity fails: %s' % (
        pos1, pos1.subs(r, sp.Rational(1, 2)), OK['C1']))
    OK['C2'] = not identity(sign_flip=True)
    print('  C2 (control): Z1 with the sign of the boundary term L r w |u|^2 flipped: the identity fails: %s' % OK['C2'])
    # Z5b exact power laws
    dlt = sp.Symbol('delta', positive=True)
    ex = {}
    for dv in (sp.Rational(1, 100), sp.Rational(1, 10), sp.Rational(1, 2)):
        for l in (0, 2):
            L = l * (l + 2)
            u = r ** (-1 - dv)
            Au = sp.simplify(-r ** -3 * sp.diff((r ** 3 - r) * sp.diff(u, r), r) + L * r ** -2 * u)
            form = ((l + 1) ** 2 - dv ** 2) * r ** (-3 - dv) + (1 + dv) ** 2 * r ** (-5 - dv)
            assert sp.simplify(Au - form) == 0
            N2 = sp.integrate(sp.expand(r * u ** 2 + r ** 3 * sp.diff(u, r) ** 2 + L * r * u ** 2),
                              (r, sp.Rational(1, 2), sp.oo))
            F2 = sp.integrate(sp.expand(r ** 5 * form ** 2), (r, sp.Rational(1, 2), sp.oo))
            ex[(str(dv), l)] = float(sp.sqrt(N2 / F2))
    lim0 = sp.limit((1 + (1 + dlt) ** 2) / (1 - dlt ** 2) ** 2, dlt, 0)
    OK['Z5b'] = max(ex.values()) <= 2.802 and lim0 == 2
    print('  Z5b (exact): N/F for u = r^(-1-delta): %s; at l = 0 the leading-order ratio^2 (1 + (1 + delta)^2)/(1 - '
          'delta^2)^2 -> %s: %s' % ({k_: round(v_, 4) for k_, v_ in ex.items()}, lim0, OK['Z5b']))
    best = ex[('1/100', 0)]
    OK['C3'] = best > 2.802 / 4
    print('  C3 (control): the claim N(u) <= (2.802/4) F: refuted by u = r^(-1.01) at l = 0 (ratio %.4f): %s' % (
        best, OK['C3']))
    for k_, v in OK.items():
        builtins.print(k_, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
