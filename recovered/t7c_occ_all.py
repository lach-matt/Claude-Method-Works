"""t7c_occ_all.py -- untailed (qtail=0) eps(q), Etot(q) at q=0,1/4,1/2,3/4,1 for every banked t5 row + Y 4d + Cs 6s. Session 21.
Appends to t7c_occ_diag.jsonl (same schema as t7c_occ_diag.py); resumable. Usage: python3 t7c_occ_all.py Z [Z ...]"""
import sys, json, os
from t7c_occ_diag import scf_occ_diag
from t5_scf import ground_occ, minus
SH={json.loads(l)['Z']:json.loads(l)['sh'] for l in open('t5.jsonl')}; SH.update({39:'4d',55:'6s'})
done={(json.loads(l)['Z'],json.loads(l)['q']) for l in open('t7c_occ_diag.jsonl') if json.loads(l)['qtail']==0} if os.path.exists('t7c_occ_diag.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1])
    for q in (0.0,0.25,0.5,0.75,1.0):
        if (Z,q) in done: continue
        occ=minus(ground_occ(Z),n,l,1.0-q)
        if q==0.0: occ=occ+[(n,l,1e-9)]
        Es,Et,tail,it=scf_occ_diag(Z,occ,0.0)
        out=dict(Z=Z,sh=sh,q=q,qtail=0.0,eps=round(float(Es[(n,l)]),6),Etot=round(float(Et),6),tail=round(tail,6),E_hfs=round(float(Et-tail),6),it=it)
        open('t7c_occ_diag.jsonl','a').write(json.dumps(out)+'\n'); print(Z,sh,q,out['eps'],out['it'],flush=True)