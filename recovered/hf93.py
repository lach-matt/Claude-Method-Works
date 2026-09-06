#!/usr/bin/env python3
"""hf93.py -- F93.6 test. Compare g(q)=dE/dq|_P (fixed orbitals) with the SCF total-energy derivative dE_SCF/dq by central difference.
Hellmann-Feynman in q holds iff the fractional-q SCF solution is stationary for the reported functional. usage: hf93.py ROW SYS q h [tol]"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt')); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
sys.path.insert(0, '../pack93'); from ffun93 import clone, Ione, Efun
from ts93 import setq, g_of
assert H.CORR is False
Zs, K, q, hstep = int(sys.argv[1]), sys.argv[2], float(sys.argv[3]), float(sys.argv[4]); TOL = float(sys.argv[5]) if len(sys.argv) > 5 else 2e-8
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}; LEV = dict(s=0, p=1, d=2, f=3)
t = OWN[Zs]; a = (int(t[0]), LEV[t[1]]); rows = NC.load()
Z, cfg = {'A': (Zs - 1, NC.cfg_from_chain(Zs - 2, rows)), 'B': (Zs, NC.cfg_from_chain(Zs - 2, rows)), 'C': (Zs, NC.cfg_from_chain(Zs - 1, rows))}[K]
def solve(Z, cfg):
    for beta, maxit in NG.LADDER:
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit * 4, tol=TOL)
        if it < maxit * 4: return h, float(E)
    raise RuntimeError("no convergence")
h0, E0 = solve(Z, setq(cfg, a, q)); g0 = g_of(h0, a); eps0 = float(h0.eps[a])
hp, Ep = solve(Z, setq(cfg, a, q + hstep)); hm, Em = solve(Z, setq(cfg, a, q - hstep))
dE = (Ep - Em) / (2 * hstep)
# also the "g" at the neighbours, to estimate curvature and the fixed-orbital prediction of E(q+-h)
gp, gm = g_of(hp, a), g_of(hm, a)
out = dict(Z=Zs, sys=K, q=q, h=hstep, tol=TOL, E0=round(E0, 7), Ep=round(Ep, 7), Em=round(Em, 7), g0=round(g0, 7), eps0=round(eps0, 6),
           dE_SCF=round(dE, 7), HF_defect=round(dE - g0, 7), g_trap=round((gp + gm) / 2, 7), gp=round(gp, 7), gm=round(gm, 7))
print(out); json.dump(out, open(f'../pack93/hf93-{Zs}{K}-{q:g}-{hstep:g}.json', 'w'), indent=1)