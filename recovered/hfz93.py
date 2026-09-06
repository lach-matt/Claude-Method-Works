#!/usr/bin/env python3
"""hfz93.py -- F93.6 at INTEGER occupation: Hellmann-Feynman in Z. dE_SCF/dZ vs -sum_a q_a <1/r>_a (fixed orbitals). usage: hfz93.py Z cfgsource h
cfgsource: 'chain:N' = cfg_from_chain(N) ; 'plus:N:nl' = cfg_from_chain(N)+nl"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt')); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
assert H.CORR is False
Z = float(sys.argv[1]); src = sys.argv[2].split(':'); hstep = float(sys.argv[3]); TOL = 2e-8
LEV = dict(s=0, p=1, d=2, f=3); rows = NC.load(); cfg = NC.cfg_from_chain(int(src[1]), rows)
if src[0] == 'plus': cfg = NC.add(cfg, (int(src[2][0]), LEV[src[2][1]]))
def solve(Z):
    for beta, maxit in NG.LADDER:
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit * 4, tol=TOL)
        if it < maxit * 4: return h, float(E)
    raise RuntimeError("no convergence")
h0, E0 = solve(Z); hf = -sum(q * float(np.sum(h0.P[(n, l)] ** 2 / h0.r * h0.dr)) for n, l, q in h0.occ)
out = dict(Z=Z, cfg=src, E0=round(E0, 7), HF=round(hf, 7))
for hh in (hstep, hstep / 2):
    hp, Ep = solve(Z + hh); hm, Em = solve(Z - hh); out[f'dE_h{hh:g}'] = round((Ep - Em) / (2 * hh), 7)
d1, d2 = out[f'dE_h{hstep:g}'], out[f'dE_h{hstep/2:g}']; ext = d2 + (d2 - d1) / 3
out['dE_rich'] = round(ext, 7); out['defect'] = round(ext - hf, 7)
print(out); json.dump(out, open(f'../pack93/hfz93-{Z:g}-{"-".join(src)}.json', 'w'), indent=1)