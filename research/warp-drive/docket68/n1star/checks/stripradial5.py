#!/usr/bin/env python3
"""stripradial5: the strip's term inherits the sources' radial expansion at fixed v (BEYOND5 3(b), D530).

D508 put the strip's term in rho^3 C^infinity for a source r^-4 sigma(v, omega) with sigma independent of r; D521 left
open the radial dependence, since the record bounds every Cartesian and rotation derivative of e = g_lambda - g_app in
E_2 (Lemma 11.0) but gives no structure in r along the strip, where the sources sit at bounded v as r -> infinity,
that is, toward past null infinity at fixed v, u = v - 2r -> -infinity. This is the scalar model of strip5.py (flat
4 + 1, harmonic l, box phi = S, zero data on N = {v = 0}, s := v/r, t = 0 at s = 1), at every radial degree.

  R1 (exact, sympy) for phi = r^-p F(s) Y_l: -(1/2) r^(p+2) box phi = (s - s^2/2) F'' + (p - 1/2)(1 - s) F'
     - (1/2)(p^2 - 2p - l(l + 2)) F, for symbolic p and l; in x = s/2 this is Gauss's equation with (a, b, c) =
     (p + l, p - l - 2, p - 1/2). So M1(0) = p - 1/2, D487's 5/2 at p = 3, and the jump of a sheet source
     r^-(p+2) sigma delta(s) (= r^-(4+q) sigma delta(v) with p = 3 + q) is F(0+) = -sigma/(2p - 3), D487's -d/3 at
     p = 3. The regular branch is 2F1(a, b; c; s/2) with c = p - 1/2 > 0 for p > 1/2, the other exponent 1 - c = 3/2 -
     p < 0 being excluded as in D487 (F = H(s) F_reg): no logarithm at any p, half-integers included.
  R2 (exact, mpmath, 30 digits) the strip coefficient K_(p,l) := F(1) for sigma = 1, -2F1(p + l, p - l - 2; p - 1/2;
     1/2)/(2p - 3), equals Gauss's second summation theorem, -sqrt(pi) Gamma(p - 1/2)/((2p - 3) Gamma((p + l + 1)/2)
     Gamma((p - l - 1)/2)), at p = 3, 3.25, 3.5, 4, 4.5, 5, 6 and l = 0-6; at p = 3 it is strip5's C_l; at
     half-integer p it vanishes at no l (Gamma((p - l - 1)/2) has no pole there).
  R3 (computed) strip5's diamond scheme with S = r^-(4+q) on v in [0, 1], q = 0, 1/2, 1, l = 0, 1:
     r^(3+q) phi on t = 0, extrapolated as A + B/r from r = 200 and 400, matches K_(3+q,l) to 0.1 %.
  R4 (computed, the stake) S = r^-4 cos(2r/lambda) on the strip, a source oscillating in u at fixed v (r^4 S =
     cos(2/(lambda rho)) is not smooth in rho), lambda = 10 and 30: r^3 phi on t = 0 tends to 0 (under 0.06 and 0.13 on
     [300, 400], against |K_(3,0)| = 0.785), while r^4 phi oscillates as A cos(R/lambda) + B sin(R/lambda) with
     amplitude sqrt(2) lambda to leading order in lambda/R (integration by parts in u: 1.39 lambda and 1.31 lambda
     measured, within 3 % and 10 %). So the strip's term is about sqrt(2) lambda rho^4 sin(1/(lambda rho)): no rho^3
     term, and a rho^4 term that is C^1 but not C^2 in rho, its t-derivative rho^4 cos(1/(lambda rho)) not C^1 after
     the factor rho^3.

Run: python3 checks/stripradial5.py   (under a minute)
"""
import sys

import mpmath
import numpy as np
import sympy as sp


def r1():
    r, t, p, l = sp.symbols('r t p l', positive=True)
    F = sp.Function('F')
    s = (t + r) / r
    phi = r**(-p) * F(s)
    box = -sp.diff(phi, t, 2) + sp.diff(phi, r, 2) + 3 / r * sp.diff(phi, r) - l * (l + 2) / r**2 * phi
    S = sp.Symbol('S')
    lhs = sp.simplify((-sp.Rational(1, 2) * r**(p + 2) * box).subs(t, (S - 1) * r))
    f0, f1, f2 = sp.Function('F')(S), sp.Derivative(sp.Function('F')(S), S), sp.Derivative(sp.Function('F')(S), S, 2)
    want = (S - S**2 / 2) * f2 + (p - sp.Rational(1, 2)) * (1 - S) * f1 - sp.Rational(1, 2) * (p**2 - 2 * p - l * (l + 2)) * f0
    diff = sp.simplify(sp.expand(lhs.doit() - want))
    # hypergeometric form: x = s/2, x(1-x)F_xx + (c - (a+b+1)x)F_x - ab F = 0 is 2 * (the above) / ... check a, b, c
    a, b, c = p + l, p - l - 2, p - sp.Rational(1, 2)
    hyp_ok = sp.simplify(a + b + 1 - (2 * p - 1)) == 0 and sp.simplify(a * b - (p**2 - 2 * p - l * (l + 2))) == 0
    return diff == 0 and hyp_ok


def K_hyp(p, l):
    p = mpmath.mpf(p)
    return -mpmath.hyp2f1(p + l, p - l - 2, p - mpmath.mpf(1) / 2, mpmath.mpf(1) / 2, zeroprec=400) / (2 * p - 3)


def K_gauss(p, l):
    p = mpmath.mpf(p)
    return (-mpmath.sqrt(mpmath.pi) * mpmath.gamma(p - mpmath.mpf(1) / 2) / (2 * p - 3)
            * mpmath.rgamma((p + l + 1) / 2) * mpmath.rgamma((p - l - 1) / 2))


def run(prof, d=1.0, V=420.0, dv=0.02, U=1e5, n=6000, targets=(200, 400), l=0):
    """strip5.run with the source profile prof(r) on v in [0, d]; returns phi on t = 0 at the targets"""
    u = -np.geomspace(U, 1.0, n)
    du = np.diff(u)
    psi = np.zeros(n)
    out = {}
    v = 0.0
    while v < V:
        vm = v + dv / 2
        um = (u[:-1] + u[1:]) / 2
        r = (vm - um) / 2
        S = prof(r) * (vm <= d)
        pc = (psi[:-1] + psi[1:]) / 2
        F = -0.25 * (r**1.5 * S + (l * (l + 2) + 0.75) * pc / r**2)
        psi = np.concatenate([[0.0], np.cumsum(np.diff(psi) + du * dv * F)])
        v += dv
        for R in targets:
            if R not in out and v >= R:
                i = np.argmin(abs(u + R))
                rr = (v - u[i]) / 2
                out[R] = rr**-1.5 * psi[i]
    return out


def main():
    mpmath.mp.dps = 30
    ok = {}
    ok['R1'] = r1()
    print('  R1: -(1/2) r^(p+2) box(r^-p F(s) Y_l) = (s - s^2/2)F\'\' + (p - 1/2)(1 - s)F\' - (1/2)(p^2 - 2p - l(l+2))F, '
          'Gauss (a, b, c) = (p + l, p - l - 2, p - 1/2):', 'PASS' if ok['R1'] else 'FAIL')

    worst, cl_ok, half_ok = mpmath.mpf(0), True, True
    for p in ('3', '3.25', '3.5', '4', '4.5', '5', '6'):
        row = []
        for l in range(7):
            kh, kg = K_hyp(p, l), K_gauss(p, l)
            worst = max(worst, abs(kh - kg))
            row.append(kg)
            if p == '3':
                cl = -mpmath.pi / 4 * mpmath.rgamma(1 - mpmath.mpf(l) / 2) * mpmath.rgamma(2 + mpmath.mpf(l) / 2)
                cl_ok &= abs(kg - cl) < mpmath.mpf('1e-25')
            if p in ('3.5', '4.5'):
                half_ok &= abs(kg) > mpmath.mpf('1e-3')
        print('    K_(%s, l), l = 0-6: %s' % (p, ', '.join(mpmath.nstr(x, 6) for x in row)))
    ok['R2'] = worst < mpmath.mpf('1e-25') and cl_ok and half_ok
    print('  R2: 2F1 against Gauss to %s; C_l at p = 3; nonzero at p = 3.5, 4.5 for every l:' % mpmath.nstr(worst, 2),
          'PASS' if ok['R2'] else 'FAIL', flush=True)

    r3 = True
    for q in (0.0, 0.5, 1.0):
        for l in (0, 1):
            o = run(lambda r: r**(-4.0 - q), l=l)
            f = {R: R**(3 + q) * o[R] for R in o}
            ext = 2 * f[400] - f[200]
            k = float(K_gauss(3 + q, l))
            rel = abs(ext / k - 1)
            r3 &= rel < 1e-3
            print('    q = %.1f, l = %d: r^(3+q) phi %.5f (r = 200), %.5f (r = 400), extrapolated %.5f, K = %.5f, '
                  'relative %.1e' % (q, l, f[200], f[400], ext, k, rel), flush=True)
    ok['R3'] = r3
    print('  R3: the PDE carries r^-(4+q) on the strip to rho^(3+q) K_(3+q,l):', 'PASS' if r3 else 'FAIL')

    r4 = True
    T = tuple(range(200, 401, 4))
    for lam, tol3, tolA in ((10.0, 0.06, 0.03), (30.0, 0.13, 0.10)):
        o = run(lambda r: r**-4.0 * np.cos(2 * r / lam), targets=T)
        Rs = np.array(T, float)
        a3 = np.array([R**3 * o[R] for R in T])
        a4 = np.array([R**4 * o[R] for R in T])
        M = np.c_[np.cos(Rs / lam), np.sin(Rs / lam), np.ones_like(Rs)]
        co = np.linalg.lstsq(M, a4, rcond=None)[0]
        amp = float(np.hypot(co[0], co[1]))
        m3 = float(abs(a3[Rs >= 300]).max())
        good = m3 < tol3 and abs(amp / (2**0.5 * lam) - 1) < tolA
        r4 &= good
        print('    lambda = %g: max |r^3 phi| on [300, 400] %.4f; r^4 phi = A cos(R/lambda) + B sin(R/lambda) + C, '
              'amplitude %.3f = %.4f lambda (sqrt 2 = 1.4142), C = %.3f' % (lam, m3, amp, amp / lam, co[2]), flush=True)
    ok['R4'] = r4
    print('  R4: a source oscillating in u at fixed v leaves no rho^3 term and a rho^4 term ~ sqrt(2) lambda rho^4 '
          'sin(1/(lambda rho)):', 'PASS' if r4 else 'FAIL')
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
