#!/usr/bin/env python3
"""t7c_tail.py -- session 20, candidate (c) of bridge-19 s6.
The TS system (entrant at 0.5, Z-0.5 electrons) has asymptotic charge q-1/2, but scf_pol_sr floors V at -q/r (q=1).
Test: floor at -(q-1/2)/r.  Exactly one line of t7c_pol.scf_pol_sr is changed, by source patch, so the diff is auditable:
    Vn[s]=np.minimum(-Z/r+VH+Vx,-q/r)   ->   Vn[s]=np.minimum(-Z/r+VH+Vx,-(q-QS)/r)
PREDICTION (stated before the run, threshold CHOSEN 0.005 Ha): |dE_5d| < 0.005 at La/Gd/Lu, same for SR and nonrel; (c) does not close the 5d edge.
usage: python3 t7c_tail.py 57 64 71      (appends to t7c_tail.jsonl)
"""
import sys, json, os, re, numpy as np
import t7c_pol
src = open('t7c_pol.py').read()
old = "Vn[s]=np.minimum(-Z/r+VH+Vx,-q/r)"
assert src.count(old) == 1
new = "Vn[s]=np.minimum(-Z/r+VH+Vx,-(q-QS)/r)"
g = dict(t7c_pol.__dict__); g['QS'] = 0.5
exec(compile(src.replace(old, new).split('if __name__')[0], 't7c_pol_tail', 'exec'), g)
scf_tail = g['scf_pol_sr']
from t5_scf import ground_occ, minus
C0 = t7c_pol.C0
T5 = {json.loads(l)['Z']: json.loads(l) for l in open('t5.jsonl')}
T7P = {json.loads(l)['Z']: json.loads(l) for l in open('t7c_pol.jsonl')}
for Z in map(int, sys.argv[1:]):
    r = T5[Z]; n, l = int(r['sh'][0]), "spdf".index(r['sh'][1]); occ = minus(ground_occ(Z), n, l, 0.5)
    s = "d" if dict(((a, b), k) for a, b, k in occ)[(n, l)] >= 2*l+1 else "u"
    _, Es_sr, h1 = scf_tail(Z, 1, occ=occ, c=C0)
    _, Es_nr, h2 = scf_tail(Z, 1, occ=occ, c=1e6)
    b = T7P.get(Z, {})
    out = dict(Z=Z, el=r['el'], sh=r['sh'], meas=r['meas'], floor='-(q-0.5)/r',
               sr_tail=round(float(Es_sr[(n, l, s)]), 4), sr_banked=b.get('t7c_pol'),
               nr_tail=round(float(Es_nr[(n, l, s)]), 4), nr_banked=b.get('ts_pol'),
               d_sr=round(float(Es_sr[(n, l, s)]) - b.get('t7c_pol', float('nan')), 4),
               d_nr=round(float(Es_nr[(n, l, s)]) - b.get('ts_pol', float('nan')), 4),
               it=[len(h1), len(h2)])
    open('t7c_tail.jsonl', 'a').write(json.dumps(out)+'\n'); print(out, flush=True)
