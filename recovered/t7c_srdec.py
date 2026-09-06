#!/usr/bin/env python3
"""t7c_srdec.py -- session 20, candidate (b) of bridge-19 s6 (second half): WHERE does the SR shift of the 5d TS removal energy enter?
Source-patch of t7c_pol.scf_pol_sr: the SR kernel's c is chosen PER ORBITAL by CSEL(n,l,c) (both the SCF loop and the probe).
modes:  all    -> c for every orbital (GATE: must equal banked t7c_pol)
        5d     -> only 5d SR, all other shells nonrel (c=1e6)     [direct]
        not5d  -> every shell SR except 5d nonrel                  [indirect]
        6s     -> only 6s SR                                       [6s-contraction share of indirect]
        core   -> everything SR except 6s and 5d                   [core share of indirect]
PREDICTION PB2 (before run): |E(5d)-E(nr)| < 0.005 and negative; E(not5d)-E(nr) > +0.020 at La (>= 75 % of the +0.0265 SR shift).
usage: python3 t7c_srdec.py 57 all 5d not5d 6s core     (appends to t7c_srdec.jsonl)
"""
import sys, json, numpy as np
import t7c_pol
from t5_scf import ground_occ, minus
src = open('t7c_pol.py').read()
old = "numerov_wf_sr(Vf[s][0],l,n,1.0,Z,c,"
assert src.count(old) == 2
new = "numerov_wf_sr(Vf[s][0],l,n,1.0,Z,CSEL(n,l,c),"
g = dict(t7c_pol.__dict__)
exec(compile(src.replace(old, new).split('if __name__')[0], 't7c_pol_srdec', 'exec'), g)
scf = g['scf_pol_sr']
C0 = t7c_pol.C0; NR = 1e6
T5 = {json.loads(l)['Z']: json.loads(l) for l in open('t5.jsonl')}
T7P = {json.loads(l)['Z']: json.loads(l) for l in open('t7c_pol.jsonl')}
Z = int(sys.argv[1]); modes = sys.argv[2:]
r = T5[Z]; n, l = int(r['sh'][0]), "spdf".index(r['sh'][1]); occ = minus(ground_occ(Z), n, l, 0.5)
s = "d" if dict(((a, b), k) for a, b, k in occ)[(n, l)] >= 2*l+1 else "u"
nmax = max(a for a, b, k in occ)   # outer s shell principal number
sel = {'all': lambda a, b: True, '5d': lambda a, b: (a, b) == (n, l), 'not5d': lambda a, b: (a, b) != (n, l),
       '6s': lambda a, b: (a, b) == (nmax, 0), 'core': lambda a, b: (a, b) not in ((n, l), (nmax, 0))}
b = T7P.get(Z, {})
for m in modes:
    f = sel[m]; g['CSEL'] = lambda a, bb, c, f=f: c if f(a, bb) else NR
    _, Es, h = scf(Z, 1, occ=occ, c=C0)
    e = round(float(Es[(n, l, s)]), 4)
    out = dict(Z=Z, el=r['el'], sh=r['sh'], mode=m, E=e, nr_banked=b.get('ts_pol'), sr_banked=b.get('t7c_pol'),
               shift_vs_nr=round(e - b['ts_pol'], 4), it=len(h))
    open('t7c_srdec.jsonl', 'a').write(json.dumps(out)+'\n'); print(out, flush=True)
