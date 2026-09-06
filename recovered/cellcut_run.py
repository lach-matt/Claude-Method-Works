"""cellcut_run.py -- s28 ruling D test. usage: SUBCELL=1 SIC_NOCLAMP=1 python3 cellcut_run.py Z [beta]
Standing chain-Z TS reference (t7c_cuaudit.scf_sic_corr, corr=Z, mode=all) with the finite-volume cell fraction in v_gbz.
Records it, converged, E, tail autocorrelation. Appends cellcut.jsonl (key Z,beta,subcell). No constant, no measured input."""
import sys, os, json, time
assert os.environ.get("SIC_NOCLAMP")=="1"
import numpy as np
import t7c_cuaudit as T
from cellcut import SUBCELL
from t5_scf import ground_occ, minus
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),
    39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
OUT="cellcut.jsonl"
Z=int(sys.argv[1]); beta=float(sys.argv[2]) if len(sys.argv)>2 else 0.3
done={(d['Z'],d['beta'],d['subcell']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
if (Z,beta,SUBCELL) in done: print("SKIP",Z,beta,SUBCELL); sys.exit()
el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
t0=time.time(); Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr="Z",mode="all",beta=beta,maxit=100)
E=float(Es[(n,l,s,"ent")]); h=np.array(h,float)
tail=h[-40:]; ac={}
if len(tail)>=12:
    t=tail-tail.mean()
    for lag in (4,5,7): ac[lag]=round(float(np.dot(t[:-lag],t[lag:])/(np.dot(t,t)+1e-30)),3)
out=dict(Z=Z,el=el,sh=sh,beta=beta,subcell=SUBCELL,it=len(h),converged=bool(h[-1]<2e-5),E=round(E,5),d_last=float(h[-1]),
         ac_tail=ac,hist_last8=[round(float(v),6) for v in h[-8:]],sec=int(time.time()-t0))
open(OUT,'a').write(json.dumps(out)+'\n'); print(out,flush=True)
