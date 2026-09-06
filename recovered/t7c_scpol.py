"""t7c_scpol.py -- session 19: SC-SR spin-POLARISED re-probe of the corridor residues (bridge-18 s3(1')).
Objects on the ion core ground(N_core), tail q=Z-N_core (1-based charge convention), c=137.035999, scf_pol_sr of t7c_pol.py:
  bare : probe eigenvalue on the polarised self-consistent core -- PP0: identical to SC-SR (t7c_scres) on a closed core
         because Vx_pol(rho/2) == Vx_unpol(rho). Gate only.
  ts   : transition state -- probe shell occupied 0.5 in the SCF (the T5->T6->T7c object, on the ion), each member of the
         pair in its own SCF; d = E_ts(second) - E_ts(first).
Predictions PP0-PP3 stated in chat before this file ran. No constant, no measured input. Appends t7c_scpol.jsonl."""
import sys, json, time, numpy as np, warnings; warnings.filterwarnings("ignore")
from t5_scf import ground_occ
from t7c_pol import scf_pol_sr
from t7c_kernel import C0
IONS={"RaII":(88,86,[(7,0),(6,2)],0.055),"ThIV":(90,86,[(6,2),(5,3)],None),"LrI":(103,102,[(6,2),(7,1)],None),
      "SrII":(38,36,[(5,0),(4,2)],0.07),"CeIV":(58,54,[(5,2),(4,3)],-0.227),"PrV":(59,54,[(5,2),(4,3)],-0.524)}
mode=sys.argv[1]; c=1e6 if len(sys.argv)>3 and sys.argv[3]=='nr' else C0; labs=[sys.argv[2]]
for lab in labs:
    Z,N,pairs,meas=IONS[lab]; q=Z-N; g=ground_occ(N); t0=time.time(); e=[]; its=[]
    for n,l in pairs:
        if mode=='bare':
            probe,Es,h=scf_pol_sr(Z,q,occ=g,c=c); e.append(probe(n,l)[0]); its.append(len(h))
        else:
            occ=g+[(n,l,0.5)]
            probe,Es,h=scf_pol_sr(Z,q,occ=occ,c=c); e.append(float(Es[(n,l,'u')])); its.append(len(h))
    row=dict(ion=lab,mode=mode,c=('nr' if c>1e5 else 'sr'),e1=round(e[0],5),e2=round(e[1],5),d=round(e[1]-e[0],5),meas=meas,it=its,sec=round(time.time()-t0))
    open('t7c_scpol.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)
