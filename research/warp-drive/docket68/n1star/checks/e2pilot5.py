#!/usr/bin/env python3
"""e2pilot5.py -- E2's first step at one operator: the scalar wave operator on 5D Tangherlini, harmonic by harmonic,
at real sigma != 0 (E2-PILOT.md).  Labels: computed.

  P1 (computed) The radial equation: phi = r^(-3/2) Phi(r_*) Y_l e^(-i sigma t) gives -Phi_** + V_l Phi = sigma^2 Phi,
     V_l = f ((l(l+2) + 3/4)/r^2 + 9 mu/(4 r^4)), f = 1 - mu/r^2; and I_l := int V_l dr_* = (l(l+2) + 3/2)/sqrt(mu).
     Control: 3/4 in place of 9/4 fails.
  P2 (computed) Lemma E2.1 against numerical solutions (mu = 1; l = 0..6; sigma in {0.3, 0.7, 1.5, 3}): the Wronskian of
     the horizon solution u_h ~ e^(-i sigma r_*) and the outgoing solution u_inf ~ e^(i sigma r_*) (started from the
     exact outgoing solution sqrt(x) H^(1)_(l+1)(sigma x) of the inverse-square tail at x = 400) is constant with
     |W| >= 2|sigma|; Im(conj(u_h) u_h') = -sigma along x (the flux, to rounding relative to |u_h| |u_h'| where u_h
     has grown through the barrier); and |u_h(x)|^2, |u_inf(x)|^2 obey the Gronwall
     bounds 2 exp(int V / |sigma|) at sampled x.  Control: |W| >= 4|sigma| fails somewhere.
Numerical integration (scipy solve_ivp, rtol 1e-11) checks the lemma; the lemma itself is proved in E2-PILOT.md.
"""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import hankel1, h1vp


def p1():
    r, mu, l, sig = sp.symbols('r mu l sigma', positive=True)
    f = 1 - mu / r**2
    Phi = sp.Function('Phi')
    phi = r**sp.Rational(-3, 2) * Phi(r)
    expr = sp.diff(r**3 * f * sp.diff(phi, r), r) / r**3 - l * (l + 2) * phi / r**2 + sig**2 * phi / f
    Pss = f * sp.diff(f * sp.diff(Phi(r), r), r)
    V = sp.simplify(-(sp.expand(expr * f * r**sp.Rational(3, 2)) - Pss - sig**2 * Phi(r)) / Phi(r))
    ok = sp.simplify(V - f * ((l * (l + 2) + sp.Rational(3, 4)) / r**2 + sp.Rational(9, 4) * mu / r**4)) == 0
    bad = sp.simplify(V - f * ((l * (l + 2) + sp.Rational(3, 4)) / r**2 + sp.Rational(3, 4) * mu / r**4)) == 0
    I = sp.integrate(sp.simplify(V / f), (r, sp.sqrt(mu), sp.oo))
    okI = sp.simplify(I - (l * (l + 2) + sp.Rational(3, 2)) / sp.sqrt(mu)) == 0
    return ok and okI, bad


def rstar(r):
    with np.errstate(divide='ignore'):
        return r + 0.5 * np.log((r - 1) / (r + 1))


def V(r, l):
    return (1 - 1 / r**2) * ((l * (l + 2) + 0.75) / r**2 + 2.25 / r**4)


def r_of(x):
    """invert r_*(r) = x for r > 1 (mu = 1) by bisection"""
    lo, hi = 1 + 1e-300, max(2.0, x + 5)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if rstar(mid) < x: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def solve(l, s, x0, x1, start, xs):
    """integrate u'' = (V - s^2) u in x = r_* from `start` ('h' at x0 or 'inf' at x1) through the points xs"""
    def rhs(x, y):
        r = r_of(x)
        u = y[0] + 1j * y[1]; up = y[2] + 1j * y[3]
        upp = (V(r, l) - s**2) * u
        return [up.real, up.imag, upp.real, upp.imag]
    if start == 'h':
        u0 = np.exp(-1j * s * x0); up0 = -1j * s * u0; span = (x0, x1); ev = np.sort(xs)
    else:
        # outgoing data from the inverse-square tail: sqrt(pi s x/2) e^{i(nu pi/2 + pi/4)} H1_nu(s x)
        nu = l + 1; c = np.sqrt(np.pi * s / 2) * np.exp(1j * (nu * np.pi / 2 + np.pi / 4))
        u0 = c * np.sqrt(x1) * hankel1(nu, s * x1)
        up0 = c * (0.5 / np.sqrt(x1) * hankel1(nu, s * x1) + np.sqrt(x1) * s * h1vp(nu, s * x1))
        span = (x1, x0); ev = np.sort(xs)[::-1]
    sol = solve_ivp(rhs, span, [u0.real, u0.imag, up0.real, up0.imag], t_eval=ev, rtol=1e-11, atol=1e-13,
                    method='DOP853')
    U = sol.y[0] + 1j * sol.y[1]; UP = sol.y[2] + 1j * sol.y[3]
    if start != 'h':
        U, UP = U[::-1], UP[::-1]
    return U, UP


def p2():
    ok, ctl = True, False
    x0, x1 = -40.0, 400.0
    xs = np.linspace(-20, 60, 41)
    for l in range(7):
        for s in (0.3, 0.7, 1.5, 3.0):
            Uh, Uph = solve(l, s, x0, x1, 'h', np.concatenate([xs, [x1]]))
            Ui, Upi = solve(l, s, x0, x1, 'inf', np.concatenate([[x0], xs]))
            W = Uh[:-1] * Upi[1:] - Uph[:-1] * Ui[1:]
            # flux: Im(conj(u_h) u_h') = -s along x; |W| = 2 s |A| >= 2 s
            fl = np.imag(np.conj(Uh[:-1]) * Uph[:-1])
            scale = s + 1e-9 * np.abs(Uh[:-1]) * np.abs(Uph[:-1])        # rounding of conj(u) u' where u is large
            flux = np.max(np.abs(fl + s) / scale)
            Wc = np.abs(W).std() / np.abs(W).mean()
            okW = np.abs(W).min() >= 2 * s * (1 - 1e-6)
            # Gronwall bounds at the sampled x
            rr = np.array([r_of(x) for x in xs])
            # int_1^r V/f and int_r^inf V/f
            Vleft = np.array([(l * (l + 2) + 0.75) * (1 - 1 / r) + 0.75 * (1 - 1 / r**3) for r in rr])
            Vright = np.array([(l * (l + 2) + 0.75) / r + 0.75 / r**3 for r in rr])
            gh = np.all(np.abs(Uh[:-1])**2 <= 2 * np.exp(Vleft / s) * (1 + 1e-6))
            gi = np.all(np.abs(Ui[1:])**2 <= 2 * np.exp(Vright / s) * (1 + 1e-6))
            ok &= flux < 1e-3 and Wc < 1e-6 and okW and gh and gi
            if not (flux < 1e-3 and Wc < 1e-6 and okW and gh and gi):
                print('  l=%d s=%.1f flux %.1e Wvar %.1e |W|/2s %.4f gh %s gi %s'
                      % (l, s, flux, Wc, np.abs(W).min() / (2 * s), gh, gi))
            ctl |= np.abs(W).min() < 4 * s
    return ok, ctl


def main():
    r1, c1 = p1()
    print('P1 V_l and I_l:', 'PASS' if r1 else 'FAIL', '| control 3/4 for 9/4:', c1)
    r2, c2 = p2()
    print('P2 flux, |W| >= 2|sigma|, Gronwall bounds (l <= 6, four sigma):', 'PASS' if r2 else 'FAIL',
          '| control |W| >= 4|sigma| fails somewhere:', c2)
    ok = r1 and not c1 and r2 and c2
    print('e2pilot5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
