import numpy as np
from itertools import product, combinations
print("="*86)
print("  TESTING THE CSP FORMULATION AGAINST Λ ITSELF")
print("="*86)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX))
LAM=sorted({z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)})
d=8
print("\n     |Λ| = %d    d = %d    pairs = %d"%(len(LAM),d,len(LAM)*(len(LAM)-1)//2))
print("="*86)
print("  1.  IS Λ A SUBLATTICE?  (join and meet, all pairs)")
print("="*86)
Ls=set(LAM)
jf=mf=0
for x,y in combinations(LAM,2):
    if tuple(max(x[i],y[i]) for i in range(d)) not in Ls: jf+=1
    if tuple(min(x[i],y[i]) for i in range(d)) not in Ls: mf+=1
print("\n     join failures : %d      meet failures : %d      **sublattice : %s**"
      %(jf,mf,jf==0 and mf==0))
print("="*86)
print("  2.  IS Λ 𝓡-CLOSED?  (the pointwise minimum of recovered bounds)")
print("="*86)
A=[sorted({x[i] for x in LAM}) for i in range(d)]
ph={}
for i in range(d):
    for j in range(d):
        if i==j: continue
        f={}; run=-1
        for v in A[j]:
            c=[x[i] for x in LAM if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
        ph[(i,j)]=f
adm={x for x in product(*A) if all(x[i]<=min(ph[(i,j)].get(x[j],10**9) for j in range(d) if j!=i)
     for i in range(d))}
print("\n     admitted = %d    |Λ| = %d    **E(Λ) = %d**"%(len(adm),len(LAM),len(adm)-len(LAM)))
print("     **the two conditions agree on Λ : %s**"%((jf==0 and mf==0)==(len(adm)==len(LAM))))
print("="*86)
print("  3.  THE ARITY DISTRIBUTION OF Λ's OWN CSP")
print("="*86)
from collections import Counter
kk=Counter()
for x,y in combinations(LAM,2):
    kk[sum(1 for i in range(d) if x[i]!=y[i])]+=1
tot=sum(kk.values())
print("\n  %6s%14s%12s"%("k","pairs","fraction"))
print("  "+"-"*34)
for k in sorted(kk): print("  %6d%14d%12.4f"%(k,kk[k],kk[k]/tot))
print("\n     pairs with k ≤ 2 (binary) : %.4f"%(sum(v for k,v in kk.items() if k<=2)/tot))
print("     pairs with k ≥ 3          : %.4f"%(sum(v for k,v in kk.items() if k>=3)/tot))
print("="*86)
print("  4.  AND EVERY 2-D PROJECTION OF Λ")
print("="*86)
def closed2(P):
    A2=[sorted({p[0] for p in P}),sorted({p[1] for p in P})]
    M={};run=-1
    for v in A2[0]:
        c=[y for (x,y) in P if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A2[1]:
        c=[x for (x,y) in P if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return {(r,c) for r in A2[0] for c in A2[1] if c<=M[r] and r<=N[c]}==P
NM=['n','l','k','q','e','f','g','2S']
bad=[]
for i,j in combinations(range(d),2):
    P={(x[i],x[j]) for x in LAM}
    if not closed2(P): bad.append((NM[i],NM[j]))
print("\n     projections tested : %d"%(d*(d-1)//2))
print("     **closed          : %d**"%(d*(d-1)//2-len(bad)))
print("     not closed        : %s"%(bad if bad else "none"))
print("="*86)
print("  5.  IS Λ's OWN ORDER THE ONLY ONE?  (a sample of relabellings)")
print("="*86)
import random
random.seed(379)
def lat_ok(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
hits=0; T=200
for _ in range(T):
    ps=[list(a) for a in A]
    for p in ps: random.shuffle(p)
    ix=[{v:i for i,v in enumerate(p)} for p in ps]
    R={tuple(ix[k][x[k]] for k in range(d)) for x in LAM}
    if lat_ok(R,d): hits+=1
print("\n     random relabellings tried : %d      still a sublattice : %d"%(T,hits))
print("     (Λ's given order is one of C(orderings); the identity is always among them)")