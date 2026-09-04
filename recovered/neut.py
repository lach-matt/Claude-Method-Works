import math
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
print(f"  THE NEUTRALITY COORDINATE  —  {len(R)} channels\n")
print("      Z = Nₑ + c − 1, so Z, Nₑ, c are LINEARLY DEPENDENT.")
print("      only two of the three are independent — the index has been")
print("      carrying a redundant coordinate all along.\n")
def E(cells,d): return len(opR(cells,d))-len(cells)
FORMS=[("(Z, c, ℓ, 2S+1)",[("Z",),("c",),("l",),("S",)]),
       ("(Nₑ, c, ℓ, 2S+1)",[("ne",),("c",),("l",),("S",)]),
       ("(Nₑ, Z, ℓ, 2S+1)",[("ne",),("Z",),("l",),("S",)]),
       ("(Nₑ, ℓ, 2S+1) — c dropped",[("ne",),("l",),("S",)]),
       ("(c, ℓ, 2S+1) — Nₑ dropped",[("c",),("l",),("S",)]),
       ("(Nₑ, c, ℓ)  — 2S+1 dropped",[("ne",),("c",),("l",)])]
print(f"      {'coordinates':<34}{'|X|':>6}{'E':>8}")
for nm,ks in FORMS:
    cells={tuple(r[k[0]] for k in ks) for r in R}
    print(f"      {nm:<34}{len(cells):>6}{E(cells,len(ks)):>8}")
print()
print("  NOW ADD NEUTRALITY EXPLICITLY  (c = 1 vs c ≥ 2 vs c ≥ 3)\n")
def reg(c): return 0 if c==1 else (1 if c==2 else 2)
print(f"      {'coordinates':<40}{'|X|':>6}{'E':>8}")
for nm,ks,extra in (
  ("(Nₑ, c, ℓ, 2S+1)",[("ne",),("c",),("l",),("S",)],None),
  ("(Nₑ, regime, ℓ, 2S+1) — c→regime",[("ne",),("l",),("S",)],"reg"),
  ("(Nₑ, c, regime, ℓ, 2S+1)",[("ne",),("c",),("l",),("S",)],"reg+"),
  ("(Nₑ, regime, ℓ)",[("ne",),("l",)],"reg")):
    if extra=="reg":
        cells={tuple([r[k[0]] for k in ks[:1]]+[reg(r["c"])]+[r[k[0]] for k in ks[1:]])
               for r in R}
        d=len(ks)+1
    elif extra=="reg+":
        cells={tuple([r[k[0]] for k in ks[:2]]+[reg(r["c"])]+[r[k[0]] for k in ks[2:]])
               for r in R}
        d=len(ks)+1
    else:
        cells={tuple(r[k[0]] for k in ks) for r in R}; d=len(ks)
    print(f"      {nm:<40}{len(cells):>6}{E(cells,d):>8}")
print()
print("  AND THE NEUTRALS AND IONS INDEXED SEPARATELY\n")
for lab,sel in (("neutrals only (c = 1)",lambda r:r["c"]==1),
                ("ions only (c ≥ 2)",lambda r:r["c"]>=2),
                ("c = 2 only",lambda r:r["c"]==2),
                ("c ≥ 3 only",lambda r:r["c"]>=3)):
    v=[r for r in R if sel(r)]
    if len(v)<6: continue
    cells={(r["ne"],r["l"],r["S"]) for r in v}
    print(f"      {lab:<26}{len(v):>4} channels · |X| = {len(cells):>4} · E = {E(cells,3)}")