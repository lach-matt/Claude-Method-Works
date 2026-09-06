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
print(f"  Λ_spectra WITH THE CHARGE DECLARED  —  {len(R)} channels\n")
def band(v,q):
    return int(np.searchsorted(q,v))
NE=np.array([r["ne"] for r in R],float); C=np.array([r["c"] for r in R],float)
u=np.log(NE)-(2/3)*np.log(C)
x=np.exp(-u/2)                       # the decay rate
qs_u=np.quantile(u,[.25,.5,.75]); qs_x=np.quantile(x,[.25,.5,.75])
base={(r["Z"],r["c"],r["l"],r["S"]) for r in R}
E4=len(opR(base,4))-len(base)
print(f"      4 coordinates (Z, c, ℓ, 2S+1) : |X| = {len(base)}   E = {E4}\n")
# declared: c_screen = u band, c_base = c, c_rate = x band
dec={(r["Z"],band(u[i],qs_u),r["c"],band(x[i],qs_x),r["l"],r["S"])
     for i,r in enumerate(R)}
E6=len(opR(dec,6))-len(dec)
print(f"      6 coordinates (Z, c_screen, c_base, c_rate, ℓ, 2S+1)")
print(f"                                      |X| = {len(dec)}   E = {E6}")
print(f"                                      ΔE = {E6-E4:+d}\n")
print("  AND THE INTERMEDIATE FORMS\n")
for nm,cells,d in (
    ("(Z, c_screen, c, ℓ, 2S+1)",
     {(r["Z"],band(u[i],qs_u),r["c"],r["l"],r["S"]) for i,r in enumerate(R)},5),
    ("(Z, c, c_rate, ℓ, 2S+1)",
     {(r["Z"],r["c"],band(x[i],qs_x),r["l"],r["S"]) for i,r in enumerate(R)},5),
    ("(Z, c_screen, c_rate, ℓ, 2S+1) — c dropped",
     {(r["Z"],band(u[i],qs_u),band(x[i],qs_x),r["l"],r["S"]) for i,r in enumerate(R)},5),
    ("(Nₑ, c, ℓ, 2S+1) — Z→Nₑ",
     {(r["ne"],r["c"],r["l"],r["S"]) for r in R},4),
    ("(Nₑ, c, p, ℓ, 2S+1)",
     {(r["ne"],r["c"],r["p"],r["l"],r["S"]) for r in R},5)):
    E=len(opR(cells,d))-len(cells)
    print(f"      {nm:<44}|X| = {len(cells):>4}   E = {E}")
print()
print("  READING\n")
print("      declaring c's roles ADDS coordinates, and every added coordinate")
print("      can only raise |ℛ(X)|. so E rising is expected — the question is")
print("      whether it rises LESS than a random coordinate would.")
rng=np.random.default_rng(3)
rnd={(r["Z"],int(rng.integers(0,4)),r["c"],int(rng.integers(0,4)),r["l"],r["S"])
     for r in R}
Er=len(opR(rnd,6))-len(rnd)
print(f"\n      declared : E = {E6}")
print(f"      random   : E = {Er}")
print(f"      ratio    : {(E6-E4)/max(Er-E4,1):.3f}")