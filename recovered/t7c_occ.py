"""t7c_occ.py -- occupation dependence of the local TS object (session 21, bridge-20 s3(2)).
scf_occ (t5_scf) verbatim; ground(Z-1)+entrant at occupation q, tail fixed -1/r, nonrel.
Writes one row per (Z,q) to t7c_occ.jsonl; resumable. Usage: python3 t7c_occ.py Z [Z ...]"""
import sys, json, os, numpy as np
from t5_scf import scf_occ, ground_occ, minus
T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
QS=[i/8 for i in range(9)]
done={(json.loads(l)['Z'],json.loads(l)['q']) for l in open('t7c_occ.jsonl')} if os.path.exists('t7c_occ.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    r=T5[Z]; n,l=int(r['sh'][0]),"spdf".index(r['sh'][1])
    for q in QS:
        if (Z,q) in done: continue
        occ=minus(ground_occ(Z),n,l,1.0-q)              # ground(Z) with entrant reduced to q
        if q==0.0: occ=occ+[(n,l,1e-9)]                  # keep the entrant channel present at q->0 (probe eigenvalue)
        Vf,Es,Et,it=scf_occ(Z,occ,1.0)
        out=dict(Z=Z,el=r['el'],sh=r['sh'],q=q,eps=round(float(Es[(n,l)]),6),Etot=round(float(Et),6),it=it)
        open('t7c_occ.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)
