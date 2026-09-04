"""t7c_ownshell_run.py -- s24 item (2): Sc tests C (mode) and D (Janak f-scan). usage: SIC_NOCLAMP=1 python3 t7c_ownshell_run.py Z ; appends t7c_ownshell.jsonl (key Z,test,par); resumable."""
import sys, json, os, time
assert os.environ.get("SIC_NOCLAMP")=="1"
from t5_scf import ground_occ, minus
OUT='t7c_ownshell.jsonl'
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),68:('Er','4f')}
done={(d['Z'],d['test'],d['par']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
Z=int(sys.argv[1]); el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
def run(test,par,env,**kw):
    if (Z,test,par) in done: return
    for k,v in env.items(): os.environ[k]=v
    import importlib, t7c_cuaudit; importlib.reload(t7c_cuaudit)
    t0=time.time(); Es,h,s=t7c_cuaudit.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr="Z",**kw)
    out=dict(Z=Z,el=el,sh=sh,test=test,par=par,E=round(float(Es[(n,l,s,"ent")]),5),it=len(h),d_last=round(h[-1],6),sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(out)+'\n'); print(out,flush=True)
if sys.argv[2]=='C':
    for mode in ('none','ent','all'): run('C',mode,{'FOCC':'0.5','FENT':'0.5'},mode=mode)
if sys.argv[2]=='D':
    for f in sys.argv[3:]: run('D',f,{'FOCC':f,'FENT':f},mode='all')