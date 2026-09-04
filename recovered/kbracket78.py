"""kbracket78.py -- s78 ITEM 3, second lever. The INTEGER poison (kpoison78) shifts which
ZERO the bisection hunts and raises. This one perturbs the BRACKET SEED CONTINUOUSLY,
eh -> eh*(1+d), which cannot change the node count. It asks a different question:
IS THE CONVERGED ANSWER A FUNCTION OF THE SEED, OR ONLY OF THE ZERO?
"""
import sys, os, json, time
import numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
sys.path.insert(0, os.getcwd())
import t7c_hfsr as HS
import nlchain as NC
import hfc2 as H
from t7c_kernel import C0
H.CORR = False
Z = int(sys.argv[1])
rows = NC.load(); cfg = [tuple(x) for x in NC.cfg_from_chain(Z-1, rows)]
ORIG = HS.eigen_sr; CALLS=[0]
def mk(d):
    def f(*a, **k):
        CALLS[0]+=1
        return ORIG(*a, **k)*(1.0+d)
    return f
out={}
print(f"BRACKET-SEED LEVER -- Z={Z}.  eh -> eh*(1+d)")
for d in (0.0, 1e-3, 1e-2, 5e-2):
    HS.eigen_sr = mk(d); CALLS[0]=0; t0=time.time()
    try:
        E,Ec,it,eps = H.HFC(Z,cfg,c=C0).run2()
        out[str(d)]=dict(E=float(E),it=it,calls=CALLS[0])
        print(f"  d={d:<7g} E = {E:.12f} Ha  it={it} calls={CALLS[0]} {time.time()-t0:.0f}s")
    except Exception as e:
        out[str(d)]=dict(E=None,err=f"{type(e).__name__}: {e}",calls=CALLS[0])
        print(f"  d={d:<7g} RAISED {type(e).__name__}: {e}  calls={CALLS[0]}")
E0=out["0.0"]["E"]
for d,v in out.items():
    if d!="0.0" and v.get("E") is not None:
        print(f"  dE(d={d}) = {v['E']-E0:+.3e} Ha")
json.dump(out, open(f"../pack78/kbracket78_{Z}.json","w"), indent=1)