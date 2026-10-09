#!/usr/bin/env python3
"""E-OUTER-MASS spot check (own code, numerical; scan + bisection, tol 1e-30 at 40 digits).
V1-type: ours two-sided at RS (slab ell=1 heavier side, own ell_1=1 lighter side), L2's k=-1 family; P2: slab + own
bulk ell_2=4/3 with free own mass mo2, tau2=-1/8.  Eliminate mo2 via the tt condition, scan u2 for the angular one."""
import mpmath as mp
mp.mp.dps = 40
for D in (mp.mpf('1.2'), mp.mpf(2), mp.mpf(3), mp.mpf('3.3'), mp.mpf('3.5')):
    Sig = -mp.mpf(3)/2*D**(mp.mpf(2)/3)
    mus, mo1 = (Sig + D)/2, (Sig - D)/2
    u1 = 2/D**(mp.mpf(2)/3)
    disc = 1 + 4*mus
    hz = sorted([mp.sqrt((1 + sg*mp.sqrt(disc))/2) for sg in (1, -1)]) if disc > 0 and mus < 0 else \
         ([mp.sqrt((1 + mp.sqrt(disc))/2)] if disc > 0 else [])
    print("Delta=%s mu_slab=%s mu_own1=%s a1=%s slab horizons=%s" % (mp.nstr(D, 4), mp.nstr(mus, 6), mp.nstr(mo1, 6),
          mp.nstr(1/mp.sqrt(u1), 6), [mp.nstr(h, 6) for h in hz]))
    Fs = lambda u: -u + 1 - mus*u**2
    for sg in (1, -1):
        def g(u):
            if Fs(u) <= 0:
                return None
            s = sg*mp.sqrt(Fs(u)); o = mp.mpf(1)/4 - s
            mo = (-u + mp.mpf(9)/16 - o**2)/u**2
            return (-1 - 2*mus*u)*o + (-1 - 2*mo*u)*s, s, o, mo
        grid = [mp.mpf(i)/400 for i in range(1, 400*40)]
        prev = None
        for uu in grid:
            r = g(uu)
            if r is None:
                prev = None; continue
            if prev is not None and prev[1][0]*r[0] < 0:
                a, b = prev[0], uu
                for _ in range(200):
                    m = (a + b)/2
                    if g(a)[0]*g(m)[0] <= 0: b = m
                    else: a = m
                val, s, o, mo = g(a)
                a2 = 1/mp.sqrt(a)
                where = ('inside inner horizon' if len(hz) == 2 and a2 < hz[0] else
                         'between horizons' if len(hz) == 2 and a2 < hz[-1] else 'outside outer horizon')
                print("   P2 a2=%s mu_own2=%s eta_s2=%+d eta_o2=%+d res=%.1e -> %s ; a2<a1: %s" % (
                    mp.nstr(a2, 8), mp.nstr(mo, 8), 1 if s > 0 else -1, 1 if o > 0 else -1, float(abs(val)), where, a2 < 1/mp.sqrt(u1)))
            prev = (uu, r)
