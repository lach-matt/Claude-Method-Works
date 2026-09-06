#!/usr/bin/env python3
"""tight93.py -- declared follow-up to T1 failure at 58-B: re-measure D and the 3-pt quadrature at SCF tol=TOL. usage: tight93.py ROW SYS TOL"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt')); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
sys.path.insert(0, '../pack93'); from ffun93 import clone, Ione, Efun
from ts93 import setq, g_of
assert H.CORR is False
Zs, K, TOL = int(sys.argv[1]), sys.argv[2], float(sys.argv[3])
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}; LEV = dict(s=0, p=1, d=2, f=3)
t = OWN[Zs]; a = (int(t[0]), LEV[t[1]]); rows = NC.load()
core = {'A': (Zs - 1, NC.cfg_from_chain(Zs - 2, rows)), 'B': (Zs, NC.cfg_from_chain(Zs - 2, rows)), 'C': (Zs, NC.cfg_from_chain(Zs - 1, rows))}[K]
def solve(Z, cfg):
    for beta, maxit in NG.LADDER:
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit * 4, tol=TOL)
        if it < maxit * 4: return h, float(E), it
    raise RuntimeError("no convergence")
Z, cfg = core
hN1, EN1, i1 = solve(Z, setq(cfg, a, 1.0)); hN, EN, i0 = solve(Z, cfg); D = EN1 - EN
x, w = np.polynomial.legendre.leggauss(3); nodes = 0.5 + 0.5 * x; W = 0.5 * w
g = []; its = [i1, i0]
for q in nodes:
    h, E, it = solve(Z, setq(cfg, a, float(q))); g.append(g_of(h, a)); its.append(it)
quad = float(sum(W * np.array(g)))
out = dict(Z=Zs, sys=K, tol=TOL, D=round(D, 7), quad=round(quad, 7), T1=round(quad - D, 7), g=[round(v, 6) for v in g], iters=its, eps1=round(float(hN1.eps[a]), 6))
print(out); json.dump(out, open(f'../pack93/tight93-{Zs}{K}-{TOL:g}.json', 'w'), indent=1)