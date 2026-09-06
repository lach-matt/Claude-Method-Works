"""t7c_scres.py -- session 18: SELF-CONSISTENT SR re-probe of the corridor residues (bridge-18 s3(1)).
Object: probe eigenvalue on the self-consistent HFS potential of the ion core: scf_occ(Z, ground(N_core), qtail=Z-N_core),
probe pair by eigen (zeta=2) — the T0b_pairs SCF column's object on ions. SR: scf_occ_sr (c=137.035999) + eigen_sr; same core/tail.
Gate: c=1e6 regenerates the nonrel probe to 1e-4. Predictions PS1-PS4 stated in chat before this file ran. Appends t7c_scres.jsonl."""
import sys, json, os, io, contextlib, time, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
import eigen_fix
from t5_scf import scf_occ, ground_occ
from t7c_kernel import scf_occ_sr, eigen_sr
IONS={"RaII":(88,86,[(7,0),(6,2)],0.055),"ThIV":(90,86,[(6,2),(5,3)],None),"LrI":(103,102,[(6,2),(7,1)],None),
      "SrII":(38,36,[(5,0),(4,2)],0.07),"CeIV":(58,54,[(5,2),(4,3)],-0.227),"PrV":(59,54,[(5,2),(4,3)],-0.524)}
mode=sys.argv[1]; labs=sys.argv[2:]
for lab in labs:
    Z,N,pairs,meas=IONS[lab]; q=Z-N; g=ground_occ(N); t0=time.time()
    if mode=='nr':
        Vf,Es,E,it=scf_occ(Z,g,q); e=[eigen_fix.eigen(Vf,l,n,2.0,Z) for n,l in pairs]
    elif mode=='gate':
        Vf,Es,E,it=scf_occ_sr(Z,g,q,c=1e6); e=[eigen_sr(Vf,l,n,2.0,Z,c=1e6) for n,l in pairs]
    else:
        Vf,Es,E,it=scf_occ_sr(Z,g,q); e=[eigen_sr(Vf,l,n,2.0,Z) for n,l in pairs]
    row=dict(ion=lab,mode=mode,e1=round(e[0],5),e2=round(e[1],5),d=round(e[1]-e[0],5),meas=meas,it=it,sec=round(time.time()-t0))
    open('t7c_scres.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)