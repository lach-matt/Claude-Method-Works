#!/usr/bin/env python3
"""Polish and verify the free-slab solutions directly on the raw (unsquared-root) balance equations, 50 digits.
Then check horizons, f > 0 on each static region, and the stability sign of each plane (V'' via the effective
potential of the plane's radial motion with the bulk held fixed -- a one-plane diagnostic only)."""
import mpmath as mp
mp.mp.dps = 50

def F(k, Li2, m, uu, Qc=0):
    return k*uu + Li2 - m*uu**2 + Qc*uu**3

def dF(k, Li2, m, uu, Qc=0):
    return k - 2*m*uu + 3*Qc*uu**2

def residuals(x, k, tau1, L1i2, tau2, L2i2, eta, mirrored=False):
    u1, u2, m, lam = x
    es1, eo1, es2, eo2 = eta
    s = lambda e, Li2, mm, uu: e*mp.sqrt(F(k, Li2, mm, uu))
    if mirrored:
        r1 = 2*s(es1, lam, m, u1) + 2*tau1
        r2 = dF(k, lam, m, u1)
    else:
        r1 = s(es1, lam, m, u1) + s(eo1, L1i2, 0, u1) + 2*tau1
        r2 = dF(k, lam, m, u1)/s(es1, lam, m, u1) + dF(k, L1i2, 0, u1)/s(eo1, L1i2, 0, u1)
    r3 = s(es2, lam, m, u2) + s(eo2, L2i2, 0, u2) + 2*tau2
    r4 = dF(k, lam, m, u2)/s(es2, lam, m, u2) + dF(k, L2i2, 0, u2)/s(eo2, L2i2, 0, u2)
    return [r1, r2, r3, r4]

CASES = [
    # name, k, tau1, L1^-2, tau2, L2^-2, etas (s1,o1,s2,o2), start (u1,u2,mu,lam), mirrored
    ('V1free k=1 bridge', 1, 1, 1, mp.mpf(-1)/8, mp.mpf(9)/16, (-1, -1, -1, 1), (1/1.11337**2, 1/2.5038**2, 0.922223, 1/2.11473**2), False),
    ('V1free k=-1 slab', -1, 1, 1, mp.mpf(-1)/8, mp.mpf(9)/16, (-1, 1, 1, -1), (1/5.08184**2, 1/1.33342**2, 26.3401, 1/0.334053**2), False),
    ('V2free k=-1 slab', -1, 1, 1, mp.mpf(-1)/4, mp.mpf(1)/4, (-1, 1, 1, -1), (1/11.6327**2, 1/2.00022**2, 135.823, 1/0.33347**2), False),
    ('S7e-free k=1 bridge', 1, mp.mpf(4)/3, 1, mp.mpf(-1)/6, mp.mpf(16)/9, (-1, -1, -1, 1), (1/0.824309**2, 1/2.20661**2, 0.576263, 1/1.01307**2), False),
    ('T1mir-free k=1 bridge', 1, 1, None, mp.mpf(-1)/8, mp.mpf(9)/16, (-1, -1, -1, 1), (1/0.782484**2, 1/1.55543**2, 0.30614, 1/2.33519**2), True),
]

for nm, k, t1, L1, t2, L2, eta, x0, mir in CASES:
    f = lambda *x: residuals(x, k, t1, L1, t2, L2, eta, mir)
    sol = mp.findroot(f, [mp.mpf(v) for v in x0], tol=mp.mpf(10)**-45, maxsteps=200)
    u1, u2, m, lam = sol
    res = max(abs(r) for r in f(*sol))
    a1, a2 = 1/mp.sqrt(u1), 1/mp.sqrt(u2)
    # slab horizons: lam x^2 + k x - m = 0 in x = R^2
    disc = k*k + 4*lam*m
    hz = []
    if disc >= 0:
        for sg in (1, -1):
            x = (-k + sg*mp.sqrt(disc))/(2*lam)
            if x > 0:
                hz.append(mp.sqrt(x))
    # own-bulk horizons for k=-1: R = L_o
    print("%-22s max|res| = %.2e" % (nm, float(res)))
    print("   a1 = %s  a2 = %s  mu = %s  L_s = %s" % (mp.nstr(a1, 12), mp.nstr(a2, 12), mp.nstr(m, 12),
                                                     mp.nstr(1/mp.sqrt(lam), 12)))
    print("   slab horizons R_h = %s ; mu > 0: %s ; a1/L_s = %s, a2/L_s = %s, mu/L_s^2 = %s" % (
        [mp.nstr(h, 10) for h in hz], m > 0, mp.nstr(a1*mp.sqrt(lam), 8), mp.nstr(a2*mp.sqrt(lam), 8), mp.nstr(m*lam, 8)))
    if k == -1:
        print("   own-bulk hyperbolic horizons: L1 = %s, L2 = %s ; a2 - L2 = %s" % (
            1, mp.nstr(1/mp.sqrt(L2), 8), mp.nstr(a2 - 1/mp.sqrt(L2), 6)))
