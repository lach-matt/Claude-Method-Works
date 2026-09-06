#!/usr/bin/env python3
"""eps92.py -- S92 ITEM 3. Eigenvalue relation at the own shell: rho_eps = dN/|dZ|. usage: eps92.py ROW [--canfail A|B]"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}
LEV = dict(s=0, p=1, d=2, f=3)
def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return float(E), eps, rung
    raise RuntimeError("no convergence")
Zs = int(sys.argv[1]); cf = sys.argv[3] if len(sys.argv) > 3 else None
rows = NC.load(); t = OWN[Zs]; a = (int(t[0]), LEV[t[1]]); cfg1 = NC.cfg_from_chain(Zs - 1, rows)
sealed = dict(rows[Zs]['order'])[t]; sw = json.load(open(f'../pack91/swing91-{Zs}.json'))['rows'][t]
t0 = time.time()
Er, er, r0 = solve(Zs, cfg1)
EN, eN, r1 = (Er, er, r0) if cf == 'A' else solve(Zs, NC.add(cfg1, a))
Drep = round(EN - Er, 5) + (0.01 if cf == 'B' else 0)
if cf != 'A' and abs(Drep - sealed) > 1.5e-5: print(f"CONTROL INVALID: Drep {Drep} sealed {sealed} rc=4"); sys.exit(4)
dN = float(eN[a] - er[a])
if abs(dN) < 1e-6: print(f"LEVER DEAD: dN={dN} rc=4"); sys.exit(4)
EZ, eZ, r2 = solve(Zs + 1, cfg1); dZ = float(eZ[a] - er[a])
S, P = sw['S'], sw['P']; rho_s = S / abs(P); rho_e = dN / abs(dZ)
res = dict(Z=Zs, own=t, eps_ref=round(float(er[a]), 5), dN=round(dN, 5), dZ=round(dZ, 5), S=S, P=P,
           rho_sealed=round(rho_s, 3), rho_eps=round(rho_e, 3), dN_vs_S=round((dN - S) / S, 3), dZ_vs_P=round((dZ - P) / abs(P), 3),
           Drep=Drep, rungs=[r0, r1, r2], sec=int(time.time() - t0))
print(res, flush=True)
json.dump(res, open(f'../pack92/eps92-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1)