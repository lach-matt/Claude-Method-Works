import math, statistics as st
import numpy as np
from itertools import product
from collections import Counter
src=open("/tmp/AC.py",encoding="utf-8").read()
src=src[:src.index('print("  THE TWO-CONSTANT FORM')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
A,K,C0=0.3795,0.3876,1.362
def delta(Z,c,l):
    ne=Z-c+1; p=cp_(ne-1,l,c)
    if p<1: return 0.0
    return A*math.sqrt(p)*ne**K*c**(-C0/math.sqrt(ne))
def op_R(X,d):
    X=set(X)
    if not X: return set()
    vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals)
            if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
print("  PLUGGING δ INTO Λ_spectra AS A NINTH COORDINATE\n")
print("      A.derived: a coordinate that is a FUNCTION of the others adds no")
print("      join-irreducibles and cannot enlarge the closed family. δ is a")
print("      function of (Z, c, ℓ). So E must not change.\n")
cells=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    cells.append((Z,c,l,S,delta(Z,c,l)))
print(f"      {len(cells)} in-region channels\n")
X4={(a,b,c_,d_) for a,b,c_,d_,e in cells}
R4=op_R(X4,4)
print(f"      4 coordinates (Z, c, ℓ, 2S+1):")
print(f"          |X| = {len(X4)}   |ℛ(X)| = {len(R4)}   E = {len(R4)-len(X4)}\n")
# bin delta into ordinal levels so it can be a lattice coordinate
for nb in (4,8,16):
    qs=np.quantile([e for *_,e in cells],np.linspace(0,1,nb+1)[1:-1])
    def bin_(v): return int(np.searchsorted(qs,v))
    X5={(a,b,c_,d_,bin_(e)) for a,b,c_,d_,e in cells}
    R5=op_R(X5,5)
    print(f"      5 coordinates, δ binned into {nb}:")
    print(f"          |X| = {len(X5)}   |ℛ(X)| = {len(R5)}   E = {len(R5)-len(X5)}"
          f"   ΔE = {len(R5)-len(X5)-(len(R4)-len(X4)):+d}")
print()
print("  AND THE CONTROL — a RANDOM ninth coordinate at the same granularity\n")
rng=np.random.default_rng(7)
for nb in (4,8,16):
    Xr={(a,b,c_,d_,int(rng.integers(0,nb))) for a,b,c_,d_,e in cells}
    Rr=op_R(Xr,5)
    print(f"      random, {nb} bins:  |X| = {len(Xr)}   E = {len(Rr)-len(Xr)}")
print()
print("  READING\n")
print("      if δ's E matches the 4-coordinate E, δ is genuinely derived —")
print("      it is a relabelling of what (Z, c, ℓ) already say.")
print("      if δ's E is much SMALLER than random's, δ is ORDER-COMPATIBLE:")
print("      it rises and falls with the existing coordinates rather than")
print("      cutting across them.")