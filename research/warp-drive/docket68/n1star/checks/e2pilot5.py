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
  P3 (computed) E2.5 on I = r in [1.2, 4]: Corollary E2.6's closed-form conditions, the least l_0 from which they hold
     to l = 400 at sigma = 0.3, 1, 3, and Proposition E2.5's conditions by quadrature; at l = 8, 16, 32 (where they
     hold) the numerical kernel's end signs and ||chi R chi|| <= 1/kappa_I^2.  Control: 1/(4 kappa_I^2) fails somewhere.
Numerical integration (scipy solve_ivp, rtol 1e-11) checks the lemmas; the lemmas are proved in E2-PILOT.md.
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


A_, B_ = 1.2, 4.0                       # the interval I of section 4, in r


def closed(s, L):
    """Corollary E2.6's closed-form sufficient conditions at L = l(l+2) (mu = 1, I = r in [1.2, 4]); each constant is
    computed from its formula, lower bounds rounded down and upper bounds up by a relative 1e-9"""
    dn, up = 1 - 1e-9, 1 + 1e-9
    a = L + 0.75
    kap = dn * a * (1 - 1 / B_**2) / B_**2 - s**2                       # min_I f/r^2 is at r = 4
    r11 = dn * a * (1 - 1 / 1.1**2) / 1.1**2 > s**2                      # V_l(1.1) > sigma^2, so r_1 < 1.1
    rate = dn * (6 - 4 * 1.1**2) / 1.1**3                                 # d ln V / dr_* >= rate on (1, 1.1]
    Bl = up * (2 + np.sqrt(2) * s * np.log(2) / rate)
    Al = dn * (A_ - 1.1) / (1 - 1 / A_**2) * np.sqrt(max(a * (1 - 1 / 1.1**2) / A_**2 - s**2, 0))
    cL = dn * a * (1 - 1 / B_**2)
    Br = up * (2 + np.sqrt(2) * np.log(2) * np.sqrt(2 * (L + 1)) / (2 / B_ * (1 - 2 / B_**2) * B_))
    Ar = dn * (np.sqrt(3) / 2) * np.sqrt(cL) * np.log(np.sqrt(cL) / (2 * s) / B_) if np.sqrt(cL) > 2 * s * B_ else 0
    return kap > 0 and r11 and Al > Bl / np.sqrt(2) and Ar > Br / np.sqrt(2), kap


def turning(s, l, lo, hi):
    """the root of V_l(r) = s^2 on [lo, hi] (V_l monotone there), by bisection"""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (V(mid, l) - s**2) * (V(lo, l) - s**2) > 0: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def exact(s, l):
    """Proposition E2.5's conditions evaluated by quadrature: kappa_I^2 > 0, A_left > B_left/sqrt2, A_right >
    B_right/sqrt2 (B: the Ermakov-invariant bound on sqrt N at the turning point, minimised over sample points)"""
    from scipy.integrate import quad
    rr = np.linspace(A_, B_, 4001)
    kap = V(rr, l).min() - s**2
    if kap <= 0 or V(A_, l) <= s**2 or V(B_, l) <= s**2:
        return False, kap
    r1 = turning(s, l, 1 + 1e-15, A_); r2 = turning(s, l, B_, 1e7)
    g = lambda r: np.sqrt(max(V(r, l) - s**2, 0)) / (1 - 1 / r**2)
    Al = quad(g, r1, A_, limit=400)[0]; Ar = quad(g, B_, r2, limit=400)[0]
    tl = 1 + (r1 - 1) * np.linspace(1e-6, 1 - 1e-6, 3000)
    Bl = np.min(np.sqrt(2 * s**2 / (s**2 - V(tl, l))) + np.sqrt(2) * s * (rstar(r1) - rstar(tl)))
    tr = r2 * np.exp(np.linspace(1e-6, 3, 3000))
    Br = np.min(np.sqrt(2 * s**2 / (s**2 - V(tr, l))) + np.sqrt(2) * s * (rstar(tr) - rstar(r2)))
    return (Al > Bl / np.sqrt(2) and Ar > Br / np.sqrt(2)), kap


def p3():
    """E2.5: closed-form l_0 for each sigma and its monotone tail to l = 400; the exact conditions from l_0; against
    the numerical kernels: the end signs and ||chi R chi|| <= 1/kappa_I^2 where the conditions hold"""
    ok, ctl, rep = True, False, []
    for s in (0.3, 1.0, 3.0):
        hold = [closed(s, l * (l + 2))[0] for l in range(401)]
        l0 = next(l for l in range(401) if all(hold[l:]))
        ex = [exact(s, l)[0] for l in range(l0 + 1)]
        le = next(l for l in range(l0 + 1) if all(ex[l:]))
        ok &= hold[l0] and ex[l0]
        rep.append('sigma %.1f: l_0 %d closed form, %d by quadrature' % (s, l0, le))
        a, b = rstar(A_), rstar(B_)
        xs = np.linspace(a, b, 161); h = xs[1] - xs[0]
        for l in (8, 16, 32):
            if l < le: continue
            Uh, Uph = solve(l, s, -40.0, 400.0, 'h', np.concatenate([xs, [400.0]]))
            Ui, Upi = solve(l, s, -40.0, 400.0, 'inf', np.concatenate([[-40.0], xs]))
            Uh, Uph, Ui, Upi = Uh[:-1], Uph[:-1], Ui[1:], Upi[1:]
            W = (Uh * Upi - Uph * Ui).mean()
            i, j = np.meshgrid(np.arange(161), np.arange(161), indexing='ij')
            K = Uh[np.minimum(i, j)] * Ui[np.maximum(i, j)] / W
            nrm = np.linalg.norm(K * h, 2)
            kap = exact(s, l)[1]
            sgn = np.real(np.conj(Uh[0]) * Uph[0]) >= 0 and np.real(np.conj(Ui[-1]) * Upi[-1]) <= 0
            ok &= sgn and nrm <= 1 / kap
            ctl |= nrm > 1 / (4 * kap)
            rep.append('  l %2d: ||chi R chi|| %.3g <= 1/kappa^2 %.3g; signs at the ends %s' % (l, nrm, 1 / kap, sgn))
    return ok, ctl, rep


def main():
    r1, c1 = p1()
    print('P1 V_l and I_l:', 'PASS' if r1 else 'FAIL', '| control 3/4 for 9/4:', c1)
    r2, c2 = p2()
    print('P2 flux, |W| >= 2|sigma|, Gronwall bounds (l <= 6, four sigma):', 'PASS' if r2 else 'FAIL',
          '| control |W| >= 4|sigma| fails somewhere:', c2)
    r3, c3, rep = p3()
    print('\n'.join(rep))
    print('P3 E2.5 conditions and the bound 1/kappa_I^2:', 'PASS' if r3 else 'FAIL',
          '| control 1/(4 kappa_I^2) fails somewhere:', c3)
    ok = r1 and not c1 and r2 and c2 and r3 and c3
    print('e2pilot5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
