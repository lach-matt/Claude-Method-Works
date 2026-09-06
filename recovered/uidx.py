import math, statistics as st
import numpy as np
from itertools import product
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
R=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    R.append(dict(Z=Z,c=c,l=l,S=S,ne=ne,p=cp_(ne-1,l,c),d=d))
u=np.array([math.log(r["ne"])-(2/3)*math.log(r["c"]) for r in R])
print(f"  Λ_spectra RE-INDEXED ON u  —  {len(R)} channels\n")
print("      if the neutral/ion break is an artifact of indexing on c,")
print("      then replacing (Nₑ, c) by u should reduce E.\n")
def E(cells,d): return len(opR(cells,d))-len(cells)
for nb in (8,12,16,24):
    q=np.quantile(u,np.linspace(0,1,nb+1)[1:-1])
    ub=[int(np.searchsorted(q,v)) for v in u]
    cells={(ub[i],r["l"],r["S"]) for i,r in enumerate(R)}
    cells4={(ub[i],r["p"],r["l"],r["S"]) for i,r in enumerate(R)}
    print(f"      u in {nb:>2} bands : (u,ℓ,2S+1) |X|={len(cells):>3} E={E(cells,3):>5}"
          f"    (u,p,ℓ,2S+1) |X|={len(cells4):>3} E={E(cells4,4):>5}")
print()
print("      for comparison:")
for nm,cells,d in (("(Z, c, ℓ, 2S+1)",{(r["Z"],r["c"],r["l"],r["S"]) for r in R},4),
                   ("(Nₑ, c, ℓ, 2S+1)",{(r["ne"],r["c"],r["l"],r["S"]) for r in R},4),
                   ("(Nₑ, Z, ℓ, 2S+1)",{(r["ne"],r["Z"],r["l"],r["S"]) for r in R},4)):
    print(f"          {nm:<22}|X| = {len(cells):>4}   E = {E(cells,d)}")
print()
print("  AND THE NEUTRAL/ION SPLIT UNDER u\n")
q=np.quantile(u,np.linspace(0,1,13)[1:-1])
ub=[int(np.searchsorted(q,v)) for v in u]
for lab,sel in (("neutrals",lambda i:R[i]["c"]==1),("ions",lambda i:R[i]["c"]>=2)):
    bands=sorted({ub[i] for i in range(len(R)) if sel(i)})
    print(f"      {lab:<10}occupy u-bands {bands}")
print()
ov=len(set(b for i,b in enumerate(ub) if R[i]["c"]==1) &
       set(b for i,b in enumerate(ub) if R[i]["c"]>=2))
print(f"      overlapping bands : {ov} of 12")
print("      → under u the two sets INTERLEAVE. there is no boundary to cross.")