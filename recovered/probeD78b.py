"""DESIGN PROBE 2, s78 -- NOT SCORED. Locate the ITERATION at which a bare-Coulomb
start fails at Z=89, and test whether the failure is in the seed or the first sweep."""
import sys, os, time
import numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
sys.path.insert(0, os.getcwd())
import t7b_hf
from hfs import numerov_wf
import nlchain as NC
import hfc2 as H
from t7c_kernel import C0
H.CORR = False
BASE = t7b_hf.HF.seed
L="spdfg"
Zeff = float(sys.argv[1])
Z=89
rows=NC.load(); cfg=[tuple(x) for x in NC.cfg_from_chain(Z-1,rows)]

def seed_coul(self, qtail=1):
    Vf = lambda rr: -Zeff/np.asarray(rr,float)
    P={};eps={}
    for n,l,q in self.occ:
        rr,drr,u,E,nd = numerov_wf(Vf,l,n,1.0,self.Z)
        if nd!=n-l-1: raise RuntimeError(f"SEEDCTOR Z={self.Z} {n}{L[l]} nodes {nd}")
        ui=np.interp(self.r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*self.dr))
        P[(n,l)]=ui; eps[(n,l)]=E
    return P,eps

t7b_hf.HF.seed = seed_coul
h = H.HFC(Z,cfg,c=C0)
t0=time.time()
try:
    P,eps = h.seed(1); print(f"Zeff={Zeff}: SEED CONSTRUCTOR OK, {len(P)} orbitals, {time.time()-t0:.1f}s")
except Exception as e:
    print(f"Zeff={Zeff}: SEED CONSTRUCTOR FAILED -- {type(e).__name__}: {e}"); sys.exit(0)
t0=time.time()
try:
    E,Ec,it,eps = H.HFC(Z,cfg,c=C0).run2(maxit=2)
    print(f"Zeff={Zeff}: 2 SCF SWEEPS SURVIVED. E={E:.6f} it={it} {time.time()-t0:.0f}s")
except Exception as e:
    print(f"Zeff={Zeff}: SCF SWEEP FAILED -- {type(e).__name__}: {e}   ({time.time()-t0:.0f}s)")