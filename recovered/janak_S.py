"""janak_S.py -- s34 B: Janak f-scan of the local-exchange+SIC+chain-S entrant eigenvalue (E path). usage: SIC_NOCLAMP=1 SUBCELL=1 python3 janak_S.py Z [f ...]
FOCC=FENT=f (as t7c_ownshell_run.py test D), corr="S", mode=all; appends janak_S.jsonl (key Z,f); resumable. No constant beyond c; no measured input."""
import sys,json,os,time
assert os.environ.get("SIC_NOCLAMP")=="1" and os.environ.get("SUBCELL")=="1"
from t5_scf import ground_occ,minus
OUT='janak_S.jsonl'
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
FS=['0.001','0.02','0.05','0.1','0.15','0.25','0.5','0.75','1.0']
done={(d['Z'],d['f']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
Z=int(sys.argv[1]); el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
for f in (sys.argv[2:] or FS):
    if (Z,f) in done: print("SKIP",Z,f); continue
    os.environ['FOCC']=f; os.environ['FENT']=f
    import importlib,t7c_cuaudit_S; importlib.reload(t7c_cuaudit_S)
    t0=time.time(); Es,h,s=t7c_cuaudit_S.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr="S",mode="all")
    out=dict(Z=Z,el=el,sh=sh,f=f,E=round(float(Es[(n,l,s,"ent")]),5),it=len(h),d_last=round(h[-1],6),sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(out)+'\n'); print(out,flush=True)