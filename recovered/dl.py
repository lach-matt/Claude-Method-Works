import math, statistics as st
import numpy as np
from itertools import product
src=open("/tmp/uidx.py",encoding="utf-8").read()
src=src[:src.index('print(f"  Λ_spectra RE-INDEXED')]
g={}; exec(src,g)
R=g["R"]; u=g["u"]; opR=g["opR"]; cfg=g["cfg"]; L="spdfg"
def outer(ne):
    z=cfg(ne,1); return z[-1] if z else (0,0,0)
for r in R:
    n_,l_,o_=outer(r["ne"]-1)
    r["lc"]=l_; r["dl"]=r["l"]-l_; r["nc"]=n_
def E(cells,d): return len(opR(cells,d))-len(cells)
print(f"  THE MISSING COORDINATE: ℓ − ℓ_core   —  {len(R)} channels\n")
q=np.quantile(u,np.linspace(0,1,9)[1:-1])
ub=[int(np.searchsorted(q,v)) for v in u]
rng=np.random.default_rng(23)
def shuf(key,d,n=30):
    base=[key(i,R[i]) for i in range(len(R))]
    out=[]
    for _ in range(n):
        perm=rng.permutation(len(R))
        out.append(E({tuple([base[perm[i]][0]]+list(base[i][1:])) for i in range(len(R))},d))
    return st.median(out)
print(f"      {'coordinates':<34}{'|X|':>6}{'E':>7}{'shuffled':>10}")
FORMS=[("(u, ℓ, 2S+1)",lambda i,r:(ub[i],r["l"],r["S"]),3),
       ("(u, ℓ−ℓ_core, 2S+1)",lambda i,r:(ub[i],r["dl"],r["S"]),3),
       ("(u, ℓ, ℓ_core, 2S+1)",lambda i,r:(ub[i],r["l"],r["lc"],r["S"]),4),
       ("(u, ℓ−ℓ_core, ℓ, 2S+1)",lambda i,r:(ub[i],r["dl"],r["l"],r["S"]),4),
       ("(u, ℓ−ℓ_core)",lambda i,r:(ub[i],r["dl"]),2),
       ("(u, ℓ)",lambda i,r:(ub[i],r["l"]),2)]
for nm,k,d in FORMS:
    cells={k(i,R[i]) for i in range(len(R))}
    print(f"      {nm:<34}{len(cells):>6}{E(cells,d):>7}{shuf(k,d):>10.1f}")
print()
print("  AND WHAT ℓ − ℓ_core DOES TO THE FIT\n")
P=np.array([r["p"] for r in R],float); D=np.array([r["d"] for r in R])
DL=np.array([r["dl"] for r in R],float)
k=(P>0)&(D>0.02)
Y=np.log(D[k]/np.sqrt(P[k])); uu=u[k]; dl=DL[k]
for nm,X in (("quadratic in u",[uu,uu**2]),
             ("+ ℓ−ℓ_core",[uu,uu**2,dl]),
             ("+ ℓ",[uu,uu**2,np.array([r['l'] for r in R],float)[k]]),
             ("+ ℓ−ℓ_core and ℓ",[uu,uu**2,dl,np.array([r['l'] for r in R],float)[k]])):
    Xm=np.column_stack(X+[np.ones(len(Y))])
    b,*_=np.linalg.lstsq(Xm,Y,rcond=None); r=Y-Xm@b
    print(f"      {nm:<22}r² {1-np.var(r)/np.var(Y):>7.4f}"
          f"   rms {float(np.sqrt(np.mean(r**2))):.4f}"
          + (f"   coef {b[2]:+.4f}" if len(X)>2 else ""))