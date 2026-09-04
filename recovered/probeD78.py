"""DESIGN PROBE, s78 -- NOT A SCORED INSTRUMENT. NO SCF. Timing flag: seed D's
parameter is chosen AFTER reading these numbers, and that is declared (R 1449 note).
Question: which starting potentials are CONSTRUCTIBLE at Z=89 (all node counts met)
and how far displaced are they from seed A?"""
import sys, os, json
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

Z = int(sys.argv[1]) if len(sys.argv)>1 else 89
rows = NC.load(); cfg = [tuple(x) for x in NC.cfg_from_chain(Z-1, rows)]
h = H.HFC(Z, cfg, c=C0)
occ = list(h.occ)
print(f"Z={Z}  cfg_prev has {len(occ)} orbitals: " + " ".join(f"{n}{L[l]}{k:g}" for n,l,k in occ))

# seed A reference
t7b_hf.HF.seed = lambda self, qtail=1: BASE(self,1)
PA, epsA = H.HFC(Z,cfg,c=C0).seed(1)
print("seed A valence eps: " + "  ".join(f"{n}{L[l]}={epsA[(n,l)]:+.5f}"
      for n,l in sorted(epsA, key=lambda t:(t[0],t[1]))[-3:]))

def try_coulomb(Zeff):
    """pure Coulomb -Zeff/r start. returns (ok, nfail, first_fail, eps)"""
    Vf = lambda rr: -Zeff/np.asarray(rr,float)
    eps={}; fails=[]
    for n,l,q in occ:
        try:
            rr,drr,u,E,nd = numerov_wf(Vf,l,n,1.0,Z)
        except Exception as e:
            fails.append((n,l,"EXC")); continue
        if nd != n-l-1: fails.append((n,l,nd))
        else: eps[(n,l)]=E
    return fails, eps

print("\n  Zeff      nfail   first fail   max|d_eps| vs A (converged orbs only)")
res={}
for Zeff in [89.0, 80.0, 60.0, 44.5, 30.0, 20.0, 10.0, 5.0, 2.0, 1.0]:
    fails, eps = try_coulomb(Zeff)
    if eps:
        d = max(abs(eps[k]-epsA[k]) for k in eps if k in epsA)
    else:
        d = float('nan')
    ff = f"{fails[0][0]}{L[fails[0][1]]}:{fails[0][2]}" if fails else "-"
    print(f"  {Zeff:6.2f}   {len(fails):3d}     {ff:>10s}    {d:10.4f}")
    res[str(Zeff)] = dict(nfail=len(fails), fails=[[a,b,str(c)] for a,b,c in fails], dmax=None if np.isnan(d) else float(d))
json.dump(res, open("../pack78/probeD78.json","w"), indent=1)