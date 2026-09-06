"""t7c_cuaudit_run.py -- s24: Cu audit test B. usage: FENT=x SIC_NOCLAMP=1 python3 t7c_cuaudit_run.py Z... ; appends t7c_cuaudit.jsonl (key Z,FENT); resumable."""
import sys, json, os, time
assert os.environ.get("SIC_NOCLAMP")=="1"
from t7c_cuaudit import scf_sic_corr, FENT
from t5_scf import ground_occ, minus
SH={55:('Cs','6s'),21:('Sc','3d'),29:('Cu','3d')}
R={json.loads(l)['Z']:json.loads(l) for l in open('t7c_corrz.jsonl')}
T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
OUT='t7c_cuaudit.jsonl'
done={(json.loads(l)['Z'],json.loads(l)['FENT']) for l in open(OUT)} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if (Z,FENT) in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr="Z"); E=round(float(Es[(n,l,s,"ent")]),4)
    out=dict(Z=Z,el=el,sh=sh,FENT=FENT,E=E,EZ_standing=R[Z]['EZ'],dE=round(E-R[Z]['EZ'],4),meas=T5[Z]['meas'],resid=round(E-T5[Z]['meas'],4),it=len(h),sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(out)+'\n'); print(out,flush=True)