#!/usr/bin/env python3
"""i101.py -- identity isolation for route (a). Numeric endpoint differences of every Efun piece vs analytic kernels."""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
ROW = 58; ent = (5, 2); Zs = 58
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]
h5 = solve(Zs, setq(cfg2, ent, 0.5))[0]; hp = solve(Zs, setq(cfg2, ent, 0.6))[0]; hm = solve(Zs, setq(cfg2, ent, 0.4))[0]
keys = [(n, l) for n, l, q in h5.occ]; Q5 = {(n, l): q for n, l, q in h5.occ}
r = h5.r; dr = h5.dr
Ip, Im, I5 = Ione(hp), Ione(hm), Ione(h5)
# numeric N1 per shell: q5_c * dI_c/dq  (NOTE: E's weight on I_c in E_orb is occ5)
N1 = {k: Q5[k] * (Ip[k] - Im[k]) / 0.2 for k in keys}
# numeric N2: half-part at occ5 between full-orbital endpoints
def half(hh):
    g = clone(hh, h5.Z, list(h5.occ)); tot = 0.0
    for n, l, q in g.occ:
        a = (n, l); V, X = pot(g, a); P = g.P[a]
        tot += q * 0.5 * (float(np.sum(P * (V + g.Z / r) * P * dr)) - float(np.sum(P * X * dr)))
    return tot
N2 = (half(hp) - half(hm)) / 0.2
# analytic per-shell dI: deps - d<PUP> + d<PX>, endpoint-numeric expectations for the two-electron parts of I
def expUX(hh, c):
    V, X = pot(hh, c); P = hh.P[c]
    return float(np.sum(P * (V + hh.Z / r) * P * hh.dr)), float(np.sum(P * X * hh.dr))
A = {}
for c in keys:
    du = (expUX(hp, c)[0] - expUX(hm, c)[0]) / 0.2
    dx = (expUX(hp, c)[1] - expUX(hm, c)[1]) / 0.2
    de = (hp.eps[c] - hm.eps[c]) / 0.2
    A[c] = dict(de=de, du=du, dx=dx, dI_num=(Ip[c] - Im[c]) / 0.2, dI_rec=de - du + dx)
sum_dE = (Efun(clone(hp, hp.Z, list(hp.occ)), Ip) - Efun(clone(hm, hm.Z, list(hm.occ)), Im)) / 0.2
g5 = None
print("shell  q*dI(num)   q*(de-du+dx)  diff")
t1 = t1r = 0.0
for c in keys:
    a = A[c]; n1 = N1[c]; rec = Q5[c] * a['dI_rec']; t1 += n1; t1r += rec
    print("  %d%s  %+11.4e  %+11.4e  %+.1e" % (c[0], 'spdf'[c[1]], n1, rec, n1 - rec))
print("SUM q*dI = %+11.4e (rec %+11.4e)   N2(half) = %+11.4e" % (t1, t1r, N2))
print("N1+N2 = %+11.4e   [d101: R2=+1.0588e-4]" % (t1 + N2))
print("full dE/dq (Efun own-occ both ends) = %+11.4e" % sum_dE)
json.dump(dict(N1={"%d%s" % (k[0], 'spdf'[k[1]]): N1[k] for k in keys}, N2=N2, sum=t1 + N2), open(os.path.join(HERE, 'i101-58.json'), 'w'), indent=1)