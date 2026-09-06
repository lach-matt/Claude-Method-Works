"""t7c_sic_run.py -- SR-pol SIC decomposition per row. Appends t7c_sic.jsonl; resumable."""
import sys, json, os
from t7c_sic import scf_sic_sr
from t5_scf import ground_occ, minus
SH={json.loads(l)['Z']:(json.loads(l)['el'],json.loads(l)['sh']) for l in open('t5.jsonl')}; SH.update({39:('Y','4d'),55:('Cs','6s')})
NR={json.loads(l)['Z']:json.loads(l) for l in open('t7a_dec.jsonl')}
done={json.loads(l)['Z'] for l in open('t7c_sic.jsonl')} if os.path.exists('t7c_sic.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); E={}
    for m in ("none","ent","all"):
        Es,h,s=scf_sic_sr(Z,1,occ=hole,entrant=(n,l),mode=m); E[m]=round(float(Es[(n,l,s,"ent")]),4)
    out=dict(Z=Z,el=el,sh=sh,sr_none=E['none'],sr_ent=E['ent'],sr_all=E['all'],sr_direct=round(E['ent']-E['none'],4),sr_indirect=round(E['all']-E['ent'],4),
             sr_shift=round(E['all']-E['none'],4),nr_shift=NR[Z]['shift'],nr_direct=NR[Z]['direct'])
    open('t7c_sic.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)