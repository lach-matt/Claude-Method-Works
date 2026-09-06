"""limitcycle.py -- s27 F25.1/F24.1 audit. usage: SIC_NOCLAMP=1 python3 limitcycle.py Z beta [maxit]
Reruns the standing chain-Z TS reference (t7c_cuaudit.scf_sic_corr, corr=Z, mode=all) with the given linear-mixing beta, records the FULL
residual history, its period-5 autocorrelation over the last 40 iterations, terminal amplitude, it, and E. Appends limitcycle.jsonl (key Z,beta).
No constant, no measured input. beta is a numerical damping parameter, not a physical quantity."""
import sys, os, json, time
assert os.environ.get("SIC_NOCLAMP")=="1"
import numpy as np
import t7c_cuaudit as T
from t5_scf import ground_occ, minus
SH={21:('Sc','3d'),22:('Ti','3d'),29:('Cu','3d')}
OUT="limitcycle.jsonl"
Z=int(sys.argv[1]); beta=float(sys.argv[2]); maxit=int(sys.argv[3]) if len(sys.argv)>3 else 100
done={(d['Z'],d['beta']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
if (Z,beta) in done: print("SKIP",Z,beta); sys.exit()
el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
t0=time.time(); Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr="Z",mode="all",beta=beta,maxit=maxit)
E=float(Es[(n,l,s,"ent")]); h=np.array(h,float)
tail=h[-40:] if len(h)>=40 else h
ac={}
if len(tail)>=12:
    t=tail-tail.mean()
    for lag in (1,2,3,4,5,6,7,8,10):
        ac[lag]=round(float(np.dot(t[:-lag],t[lag:])/(np.dot(t,t)+1e-30)),3)
out=dict(Z=Z,el=el,sh=sh,beta=beta,maxit=maxit,it=len(h),converged=bool(h[-1]<2e-5),E=round(E,5),
         d_last=float(h[-1]),d_min_tail=float(tail.min()),d_max_tail=float(tail.max()),ac_tail=ac,
         hist_last20=[round(float(v),6) for v in h[-20:]],sec=int(time.time()-t0))
open(OUT,'a').write(json.dumps(out)+'\n'); print({k:v for k,v in out.items() if k!='hist_last20'},flush=True)
