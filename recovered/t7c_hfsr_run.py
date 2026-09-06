"""t7c_hfsr_run.py -- s22: SR-HF TS (Janak-consistent, as t7b_run: ts = eps_a(N-1/2) + J~/2) on the T7 species. Appends t7c_hfsr.jsonl.
usage: python3 t7c_hfsr_run.py Z [c] [srcM]"""
import sys, json, os, io, contextlib, time, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t5_scf import ground_occ, minus
from t7b_hf import _c3j0sq
from t7c_hfsr import HFSR, C0
T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
T7B={json.loads(l)['Z']:json.loads(l) for l in open('t7b.jsonl')}
T7C={json.loads(l)['Z']:json.loads(l) for l in open('t7c.jsonl')}
Z=int(sys.argv[1]); c=float(sys.argv[2]) if len(sys.argv)>2 else C0; srcM=(sys.argv[3]!='0') if len(sys.argv)>3 else True
t0=time.time(); t=T5[Z]; sh=t['sh']; n,l=int(sh[0]),"spdf".index(sh[1]); g=ground_occ(Z); w=(2*l+1)/(4*l+1)
h=HFSR(Z,minus(g,n,l,0.5),c=c,srcM=srcM); eps,_,it1,_=h.run('hf',qtail=1)
P=h.P[(n,l)]; r,dr=h.r,h.dr
Fk=lambda k: float(np.sum(P*P*h.Yk(P,P,k)/r*dr))
J=Fk(0)-w*sum(_c3j0sq(l,k,l)*Fk(k) for k in range(2,2*l+1,2)); e_half=float(eps[(n,l)]); ts=e_half+0.5*J
b=T7B[Z]; cc=T7C[Z]
row=dict(Z=Z,el=t['el'],sh=sh,c=c,srcM=srcM,meas=t['meas'],hf_ts=b['hf_ts'],hf_ts_sr=round(ts,4),eps_half=round(e_half,4),J=round(J,4),
         shift_sr=round(ts-b['hf_ts'],4),hfs_ts=t['hfs_ts'],t7c_ts=cc['t7c_ts'],local_shift=round(cc['t7c_ts']-t['hfs_ts'],4),
         dev_meas=round(ts-t['meas'],4),it=it1,sec=round(time.time()-t0))
open('t7c_hfsr.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)