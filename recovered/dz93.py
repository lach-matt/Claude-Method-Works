#!/usr/bin/env python3
"""dz93.py -- S93 ITEM 1. dZ at the SEALED pair and core, Koopmans ionization form on the N+1 systems.
   A=(Z*-1, cfg(Z*-2)+c)  B=(Z*, cfg(Z*-2)+c)  C=(Z*, cfg(Z*-1)+c)  R=(Z*, cfg(Z*-1))
   dZ' = eps_c[B]-eps_c[A];  dN' = eps_c[C]-eps_c[B];  Drep = E[C]-E[R]  (sealed reproduction)
usage: dz93.py ROW [--canfail A|B]   ROW in 38 56 58 90 91"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
assert H.CORR is False, "sealed field is CORR=False"
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}
LEV = dict(s=0, p=1, d=2, f=3)
def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return float(E), eps, rung
    raise RuntimeError("no convergence")
Zs = int(sys.argv[1]); cf = sys.argv[3] if len(sys.argv) > 3 else None
rows = NC.load(); t = OWN[Zs]; a = (int(t[0]), LEV[t[1]])
assert tuple(rows[Zs - 1]['ent_nl']) == a, "own channel must be the entrant at Z*-1"
cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows)
sealed = dict(rows[Zs]['order'])[t]; sw = json.load(open(f'../pack91/swing91-{Zs}.json'))['rows'][t]
t0 = time.time()
ER, eR, rR = solve(Zs, cfg1)
EC, eC, rC = solve(Zs, NC.add(cfg1, a))
Drep = round(EC - ER, 5) + (0.01 if cf == 'B' else 0)
if abs(Drep - sealed) > 1.5e-5: print(f"CONTROL INVALID: Drep {Drep} sealed {sealed} rc=4"); sys.exit(4)
EA, eA, rA = solve(Zs - 1, NC.add(cfg2, a))
EB, eB, rB = (EA, eA, rA) if cf == 'A' else solve(Zs, NC.add(cfg2, a))
dZ = float(eB[a] - eA[a]); dN = float(eC[a] - eB[a])
if abs(dZ) < 1e-6: print(f"LEVER DEAD: dZ'={dZ} rc=4"); sys.exit(4)
S, P = sw['S'], sw['P']
# total-energy cross-check of the same pair: P_rep = (EB - E[Z*,cfg2]) - (EA - E[Z*-1,cfg2]) is P itself (swing91); not re-solved here.
res = dict(Z=Zs, own=t, epsA=round(float(eA[a]), 5), epsB=round(float(eB[a]), 5), epsC=round(float(eC[a]), 5),
           dZp=round(dZ, 5), dNp=round(dN, 5), S=S, P=P, rho_sealed=round(S / abs(P), 3), rho_p=round(dN / abs(dZ), 3),
           P_minus_dZp=round(P - dZ, 5), rel_P=round((P - dZ) / abs(P), 3), rel_S=round((dN - S) / S, 3),
           Drep=Drep, rungs=[rR, rC, rA, rB], sec=int(time.time() - t0))
print(res, flush=True)
json.dump(res, open(f'../pack93/dz93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1)
