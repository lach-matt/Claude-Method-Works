#!/usr/bin/env python3
"""escape_outer_mass.py -- Model A's escape E-OUTER-MASS (numerical, tolerances stated): the bulks beyond the planes
(each universe's own bulk) allowed to carry their own mass parameters, against 129/130 and 179's "exclusive to the bulk".

Our plane at the RS value, two-sided (slab + our own bulk, one ell, both decaying): by sads5_balance L2 (exact; Kraus
eq. 18, READ) it is static only at k = -1, on the family Delta = mu_slab - mu_far > 1 (in ell^2), a1^6 = ell^2 Delta^2/8,
mu_slab + mu_far = -(3/2) ell^(2/3) Delta^(2/3); the slab carries a horizon (mu_slab >= -ell^2/4) for every Delta > 1,
the far side is naked (mu_far < -5 ell^2/4).  Here: for each Delta, does position 2's plane (T1: -1/8 on one sheet,
outer 1/L^2 = 9/16; T2: -1/4, outer 1/4), with ITS outer mass mu_o2 free, balance?  Unknowns (u2, mu_o2); mu_o2 is
eliminated through the tt balance and the angular balance is root-found in u2 on a 20000-point grid then refined by
brentq (xtol 1e-14); every root is re-checked in both junction equations to 1e-10.  Numerical, not exact.
python3 escape_outer_mass.py
"""
import math

import numpy as np
from scipy.optimize import brentq

K = -1


def ours(D):
    a2 = (D * D / 8.0) ** (1.0 / 3.0)
    ssum = -1.5 * D ** (2.0 / 3.0)
    return 1.0 / a2, (ssum + D) / 2.0, (ssum - D) / 2.0     # u1, mu_slab, mu_far


def p2_roots(mu, lam2, tau2, es, eo):
    def parts(u):
        Fs = K * u + 1 - mu * u * u
        if Fs <= 0:
            return None
        s = math.sqrt(Fs)
        t = eo * (-2 * tau2 - es * s)
        if t <= 0:
            return None
        muo = (K * u + lam2 - t * t) / (u * u)
        Fsp = K - 2 * mu * u
        Fop = K - 2 * muo * u
        return es * Fsp * t + eo * Fop * s, s, t, muo

    us = np.linspace(1e-4, 40.0, 20000)
    vals = [parts(x) for x in us]
    roots = []
    for i in range(len(us) - 1):
        a, b = vals[i], vals[i + 1]
        if a is None or b is None:
            continue
        if a[0] == 0 or a[0] * b[0] < 0:
            r = brentq(lambda x: parts(x)[0], us[i], us[i + 1], xtol=1e-14)
            N, s, t, muo = parts(r)
            Fo = K * r + lam2 - muo * r * r
            T = es * s + eo * t + 2 * tau2
            if abs(N) < 1e-10 and abs(T) < 1e-10 and abs(t * t - Fo) < 1e-10:
                roots.append((r, muo, s, t))
    return roots


def horizons(mu):
    """k = -1, f = -1 + R^2 - mu/R^2: x = R^2 roots of x^2 - x - mu = 0 (ell = 1)."""
    disc = 1 + 4 * mu
    if disc < 0:
        return []
    r = [(1 + math.sqrt(disc)) / 2, (1 - math.sqrt(disc)) / 2]
    return sorted(x for x in r if x > 0)


def connected(es1, es2, u1, u2, mu):
    """H-SLAB-CONNECTED: (-1,+1) needs a2 < a1; (+1,-1) a1 < a2 (either may pass through the black hole's interior);
    (-1,-1) is the two-exterior bridge: both planes outside the outer horizon, which must exist; (+1,+1) never."""
    a1s, a2s = 1 / u1, 1 / u2
    if (es1, es2) == (-1, 1):
        return a2s < a1s
    if (es1, es2) == (1, -1):
        return a1s < a2s
    if (es1, es2) == (-1, -1):
        h = horizons(mu)
        return bool(h) and a1s > max(h) and a2s > max(h)
    return False


def main():
    convs = {"T1": (9.0 / 16.0, -1.0 / 8.0), "T2": (0.25, -0.25)}
    print("E-OUTER-MASS (numerical): our plane on L2's k = -1 family; position 2 with its outer mass free\n")
    for D in (1.05, 1.5, 2.0, 27.0 / 8.0, 4.0, 10.0, 100.0):
        u1, mus, muf = ours(D)
        line = []
        for name, (lam2, tau2) in convs.items():
            for es in (1, -1):
                for eo in (1, -1):
                    for (u2, muo, s, t) in p2_roots(mus, lam2, tau2, es, eo):
                        if abs(u2 - u1) < 1e-9 * u1:
                            geom = "COINCIDING (a2 = a1: no slab, the corridor has no room)"
                        else:
                            geom = "CONNECTED slab" if connected(-1, es, u1, u2, mus) else "NOT CONNECTED"
                            geom += " (%s)" % ("a2 < a1" if u2 > u1 else "a2 > a1")
                        hz_o = "horizon" if muo >= -0.25 else "naked"
                        line.append("%s(%+d,%+d) u2=%.6f mu_o2=%.6f [%s; outer %s]" % (name, es, eo, u2, muo, geom, hz_o))
        hz = horizons(mus)
        print("Delta=%.4f  u1=%.6f (a1^2=%.6f ell^2) mu_slab=%.6f (horizons R^2 = %s) mu_far=%.6f (naked)"
              % (D, u1, 1 / u1, mus, ", ".join("%.4f" % x for x in hz), muf))
        for x in line:
            print("     ", x)
        if not line:
            print("      no position-2 balance")


if __name__ == "__main__":
    main()
