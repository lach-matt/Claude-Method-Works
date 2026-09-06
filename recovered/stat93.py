#!/usr/bin/env python3
"""stat93.py -- is the fractional-q SCF solution stationary for Efun? usage: stat93.py ROW SYS q"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt')); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
from ts93 import setq
assert H.CORR is False
Zs, K, q = int(sys.argv[1]), sys.argv[2], float(sys.argv[3])
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}; LEV = dict(s=0, p=1, d=2, f=3)
t = OWN[Zs]; a = (int(t[0]), LEV[t[1]]); rows = NC.load()
Z, cfg = {'A': (Zs - 1, NC.cfg_from_chain(Zs - 2, rows)), 'B': (Zs, NC.cfg_from_chain(Zs - 2, rows)), 'C': (Zs, NC.cfg_from_chain(Zs - 1, rows))}[K]
h, E, r = solve(Z, setq(cfg, a, q)); I = Ione(h); E0 = Efun(h, I); dr = h.dr
print(f"q={q} E_run2={E:.7f} Efun={E0:.7f} diff={E0-E:+.1e}")
# perturb shell a: P -> (P + s*r*P)/norm  (radial scaling direction), recompute I_a exactly via kinetic integral? Use: I_a = <T> - Z<1/r>;
# <T> for P: 1/2 int (P')^2 + l(l+1)/2 int P^2/r^2. Compute I for every shell this way and check vs Ione (consistency), then scan s.
def Tkin(P, l):
    dP = np.gradient(P, h.r); return 0.5 * float(np.sum(dP ** 2 * dr)) + 0.5 * l * (l + 1) * float(np.sum(P ** 2 / h.r ** 2 * dr))
def Ikin(P, l, Z): return Tkin(P, l) - Z * float(np.sum(P ** 2 / h.r * dr))
print("I_a Ione vs kinetic:", round(I[a], 6), round(Ikin(h.P[a], a[1], Z), 6))
out = []
for s in (-0.02, -0.01, 0.0, 0.01, 0.02):
    g = clone(h, Z, h.occ); Pn = h.P[a] * (1 + s * h.r / np.sum(h.P[a] ** 2 * h.r * dr)); Pn /= np.sqrt(np.sum(Pn ** 2 * dr)); g.P[a] = Pn
    Ik = dict(I); Ik[a] = I[a] + (Ikin(Pn, a[1], Z) - Ikin(h.P[a], a[1], Z))
    Es = Efun(g, Ik); out.append((s, round(Es - E0, 7))); 
print("scan (s, E(s)-E(0)):", out)
json.dump(dict(Z=Zs, sys=K, q=q, E_run2=E, Efun=E0, I_Ione=I[a], I_kin=Ikin(h.P[a], a[1], Z), scan=out), open(f'../pack93/stat93-{Zs}{K}-{q:g}.json', 'w'), indent=1)