import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; L="spdfg"
for r in ROWS:
    r["nl"]=r["n0"]+r["l"]; r["nstar"]=r["n0"]-r["d"]
    r["a"]=r["nstar"]-0.5*r["nl"]          # a = n* - (n+l)/2
print("  THE IDENTITY:  a = p/2 − δ + ½\n")
bad=sum(1 for r in ROWS if abs(r["a"]-(r["p"]/2-r["d"]+0.5))>1e-9)
print(f"      checked on all {len(ROWS)} channels: {bad} failures\n")
print("      so 'a' is the defect measured from HALF the orbital count, and the")
print("      whole regime equation is a model for a single number per channel.\n")
print("  WHAT IS a?\n")
A=np.array([r["a"] for r in ROWS])
print(f"      {'grouping':<26}{'groups':>8}{'variance of a explained':>26}")
tot=A.var()
def ve(key):
    gr=defaultdict(list)
    for r in ROWS: gr[key(r)].append(r["a"])
    gr={k:v for k,v in gr.items() if len(v)>=2}
    if not gr: return None,0
    w=sum(np.var(v)*len(v) for v in gr.values())/sum(len(v) for v in gr.values())
    return 100*(1-w/tot), len(gr)
for lab,k in (("species (Z, charge)",lambda r:(r["Z"],r["c"])),
              ("ℓ alone",lambda r:r["l"]),
              ("p alone",lambda r:r["p"]),
              ("regime",lambda r:r["reg"]),
              ("(ℓ, p)",lambda r:(r["l"],r["p"])),
              ("(regime, ℓ)",lambda r:(r["reg"],r["l"])),
              ("charge",lambda r:r["c"]),
              ("Nₑ",lambda r:r["ne"])):
    v,n=ve(k)
    if v is None: continue
    print(f"      {lab:<26}{n:>8}{v:>25.1f}%")
print()
print("  a BY REGIME\n")
print(f"      {'regime':>7}{'n':>5}{'median a':>11}{'sd':>8}")
NM={1:"new shell",2:"same shell",3:"outer well",4:"collapsed"}
for rg in (1,2,3,4):
    v=[r["a"] for r in ROWS if r["reg"]==rg]
    if len(v)<4: continue
    print(f"      {rg:>7}{len(v):>5}{st.median(v):>11.3f}{st.pstdev(v):>8.3f}   {NM[rg]}")
print()
print("  AND a FOR THE HYDROGEN-LIKE AND HELIUM-LIKE CORES\n")
v=[r["a"] for r in ROWS if r["ne"]<=2]
if v: print(f"      Nₑ ≤ 2 : {len(v):>4} channels   median a = {st.median(v):.4f}"
            f"   sd {st.pstdev(v):.4f}")
v=[r["a"] for r in ROWS if r["p"]==0 and r["ne"]<=4]
if v: print(f"      p = 0, Nₑ ≤ 4 : {len(v):>3} channels   median a = {st.median(v):.4f}")
print()
print("      for a bare core, δ = 0 and p = 0, so a = ½ exactly.")
print("      the measured hydrogen-like value tests that.\n")
print("  a AGAINST THE MEASURED COORDINATES\n")
P=np.array([r["p"] for r in ROWS],float); NE=np.array([r["ne"] for r in ROWS],float)
C=np.array([r["c"] for r in ROWS],float); LL=np.array([r["l"] for r in ROWS],float)
for nm,X in (("p/2",P/2),("√p",np.sqrt(P)),("ℓ",LL),("ln Nₑ",np.log(NE)),
             ("c^-0.3",C**-0.3)):
    r=SS.linregress(X,A)
    print(f"      a vs {nm:<10}slope {r.slope:+.4f}   r² {r.rvalue**2:.4f}")
X=np.column_stack([P/2,-np.sqrt(P)*NE**0.45*C**-0.3,np.ones(len(A))])
b,*_=np.linalg.lstsq(X,A,rcond=None); res=A-X@b
print(f"\n      a ≈ {b[0]:+.3f}·(p/2) {b[1]:+.4f}·√p·Nₑ^0.45·c^-0.3 {b[2]:+.3f}")
print(f"      r² {1-np.var(res)/np.var(A):.4f}   rms {float(np.sqrt(np.mean(res**2))):.4f}")