"""t5_run.py -- T5 run: TFD-TS, HFS-TS, HFS-DSCF on the 13 served species. Appends t5.jsonl per species (resume-safe)."""
import sys, json, os, io, contextlib, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from hfs import numerov_wf, L
from t5_scf import scf_occ, ground_occ, minus
from t0b_rs import rho_tfd
from t0b_pot import V_from_rho
HA=219474.63
SP=[]
for l in open('/home/claude/work/LOWDIN-PACK-15/LOWDIN-PACK-15/served_prime.tsv'):
    if l[0]=='#' or l.startswith('Z\t'): continue
    f=l.rstrip('\n').split('\t')
    try: SP.append((int(f[0]),f[1],f[2],-(float(f[3])+float(f[7]))/HA))
    except: pass
done=set()
if os.path.exists('t5.jsonl'):
    for l in open('t5.jsonl'): done.add(json.loads(l)['Z'])
want=set(int(a) for a in sys.argv[1:]) if len(sys.argv)>1 else None
for Z,el,sh,meas in SP:
    if Z in done or (want and Z not in want): continue
    n,l=int(sh[0]),"spdf".index(sh[1])
    # TFD-TS: rho_TFD(Z, N=Z-1/2), tail -1/r  (V_from_rho tail uses q=Z-N=0.5; override to 1)
    rho,r0=rho_tfd(Z,Z-0.5); Vr,_=V_from_rho(Z,Z-0.5,rho,r0)
    Vts=lambda rr,Vr=Vr,r0=r0: np.where(np.asarray(rr)<r0, np.minimum(Vr(rr),-1.0/np.asarray(rr,float)), -1.0/np.asarray(rr,float))
    e_tfd_ts=float(numerov_wf(Vts,l,n,1.0,Z)[3])
    g=ground_occ(Z)
    # HFS-TS
    Vf,Es,E,it1=scf_occ(Z,minus(g,n,l,0.5),1); e_hfs_ts=Es[(n,l)]
    # HFS-DSCF
    _,_,E0,it2=scf_occ(Z,g,1); _,_,E1,it3=scf_occ(Z,minus(g,n,l,1.0),2)
    r=dict(Z=Z,el=el,sh=sh,meas=round(meas,4),tfd_ts=round(e_tfd_ts,4),hfs_ts=round(e_hfs_ts,4),dscf=round(E0-E1,4),it=[it1,it2,it3])
    open('t5.jsonl','a').write(json.dumps(r)+'\n'); print(r,flush=True)