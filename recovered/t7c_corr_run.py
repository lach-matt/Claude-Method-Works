import sys, json, os
from t7c_corr import scf_sic_corr
from t5_scf import ground_occ, minus
SH={57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),39:('Y','4d')}
B={json.loads(l)['Z']:json.loads(l) for l in open('t7c_sic.jsonl')}
done={json.loads(l)['Z'] for l in open('t7c_corr.jsonl')} if os.path.exists('t7c_corr.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); E={}
    for cr in ("U","P"):
        Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr=cr); E[cr]=round(float(Es[(n,l,s,"ent")]),4)
    out=dict(Z=Z,el=el,sh=sh,sr_sic=B[Z]['sr_all'],corrU=E['U'],corrP=E['P'],shiftU=round(E['U']-B[Z]['sr_all'],4),shiftP=round(E['P']-B[Z]['sr_all'],4))
    open('t7c_corr.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)