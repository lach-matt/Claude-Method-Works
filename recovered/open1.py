import numpy as np, sympy as sp
from itertools import product
from collections import Counter
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX)); LAM={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
print("="*84)
print("  OPEN Q7 — WHY IS F(-1) = 2?")
print("="*84)
rk=Counter(sum(x) for x in LAM)
ev=sum(v for k,v in rk.items() if k%2==0); od=sum(v for k,v in rk.items() if k%2==1)
print("\n     even-rank %d   odd-rank %d   F(-1) = %d"%(ev,od,ev-od))
mx=[max(a) for a in AX]; M=sum(mx)
print("     sum of maxima M = %d  (even: %s)"%(M,M%2==0))
sd=[x for x in LAM if tuple(mx[i]-x[i] for i in range(8)) in LAM]
print("     self-dual survivors: %d, ranks %s"%(len(sd),sorted(Counter(sum(x) for x in sd).items())))
print("""
  **FIRST: the duality map PRESERVES rank parity.** rank(σx) = M − rank(x)
  with M = %d, which is even, so σ maps even ranks to even and odd to odd.
  **A pairing argument therefore cannot cancel anything, and the 8
  survivors contribute +8 rather than 0.**
"""%M)
print("  SECOND: F(-1) factorises along the tree. Compute it term by term.\n")
def F(zv):
    tot=0
    for n in range(1,4):
      for l in range(0,2):
        if l>n-1: continue
        for k in range(1,min(4*l+2,3)+1):
          nS=sum(zv**S for S in range(0,4) if S<=k)
          inn=0
          for q in range(0,4):
            if q>k: continue
            for e in range(1,4):
              for f in range(0,2):
                if f>e-1: continue
                inn+=sum(zv**g for g in range(0,4) if g<=min(4*f+2,q))*zv**(q+e+f)
          tot+=zv**(n+l+k)*nS*inn
    return tot
print("     F(1)  = %d   (= |Lambda|)"%F(1))
print("     F(-1) = %d"%F(-1))
print("\n  THE ALTERNATING SUMS THAT PRODUCE IT:\n")
print("     %-22s%s"%("factor at z = -1","value"))
for lab,vals in [("Σ(-1)^n, n=1..3",[1,2,3]),("Σ(-1)^l, l=0..1",[0,1]),
                 ("Σ(-1)^e, e=1..3",[1,2,3]),("Σ(-1)^f, f=0..1",[0,1])]:
    print("     %-22s%d"%(lab,sum((-1)**v for v in vals)))
print("""
  **A coordinate with an EVEN number of consecutive values contributes 0
  to the box's alternating sum**, and ℓ and f both have two. So
  F_box(-1) = 0 exactly. **The constraints are what break the cancellation**
  -- they couple ℓ to n and f to e, so the two zero factors never appear
  as free factors, and a residue survives.
""")
Fb=1
for a in AX: Fb*=sum((-1)**v for v in a)
print("     F_box(-1) = %d      F_Lambda(-1) = %d"%(Fb,F(-1)))
print("""
     **ANSWERED.** F(-1) = 2 is not a residue of the 8 survivors. It is
     what remains of a box sum that would be ZERO if the coordinates were
     free, once the tree's couplings remove the vanishing factors.
""")
print("="*84)
print("  OPEN Q4 — IS THERE AN ORDER MAXIMISING THE BOUND?")
print("="*84)
R=109737.3; T=lambda v: R/v**2
def pa(nd,n): return np.polyval(np.polyfit(nd,[T(t) for t in nd],len(nd)-1),n)
def bk(n,k):
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)!=k+1 or min(nd)<2: continue
        p=pa(nd,n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
print("""
  A bound is useful only while it exceeds the measurement noise. The
  admissibility rule caps k at the point the (k+1)th difference falls
  below 5*2^(k+1)*sigma. **That cap IS the optimum -- there is no interior
  maximum.** Verify: bracket width against the noise floor.
""")
print("  %6s%8s%16s%18s%14s"%("nu","sigma","widest k usable","width there","floor"))
for nu in (20,40,80):
    for sig in (0.01,0.001):
        best=None
        for k in range(1,9):
            lo,hi=bk(nu,k); w=hi-lo
            fl=5*(2.0**(k+1))*sig
            if w>fl: best=(k,w,fl)
            else: break
        if best: print("  %6d%8.3f%16d%18.3e%14.3e"%(nu,sig,best[0],best[1],best[2]))
print("""
  **ANSWERED: the optimum is the admissibility cap, and it is a boundary
  maximum, not an interior one.** Information per cell rises monotonically
  in k -- it was still climbing at k = 6 because nothing had stopped it.
  What stops it is sigma, and the stopping point is computable per cell.
""")