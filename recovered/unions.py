import numpy as np
from itertools import combinations
NM,EM,LM,KM,FM=3,3,1,3,1
base=[]
for n in range(1,NM+1):
 for l in range(0,min(LM,n-1)+1):
  for k in range(1,min(KM,2*(2*l+1))+1):
   for q in range(0,k+1):
    for s in range(0,k+1):
     for e in range(1,EM+1):
      for f in range(0,min(FM,e-1)+1):
       for g in range(0,min(q,2*(2*f+1))+1):
        for G in range(g,2*(2*f+1)+1):
         for sp in range(0,G+1):
          base.append((n,l,k,q,e,f,g,s,sp,G))
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
X=lambda combo:[c for c in base if all(c[W[w][1]]<=c[W[w][0]] for w in combo)]
def fails(cells):
    A=np.array(cells,dtype=np.int16); N=len(A)
    rad=(np.array(base,dtype=np.int16).max(0)+1).astype(np.int64)
    mult=np.ones(10,dtype=np.int64)
    for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
    enc=lambda M:(M.astype(np.int64)*mult).sum(1)
    S=set(enc(A).tolist()); jf=mf=0
    for i in range(N):
        r=A[i]
        jf+=sum(1 for c in enc(np.maximum(r,A[i+1:])).tolist() if c not in S)
        mf+=sum(1 for c in enc(np.minimum(r,A[i+1:])).tolist() if c not in S)
    return jf,mf
names=list(W)
print("UNIONS — is the join of two arrows a closed index?\n")
print(f"{'pair':<26} {'|A|':>6} {'|B|':>6} {'|A∪B|':>7} {'join':>7} {'meet':>7}  closed")
for a,b in combinations(names,2):
    A=set(X((a,))); B=set(X((b,))); U=sorted(A|B)
    jf,mf=fails(U)
    print(f"{a+' ∪ '+b:<26} {len(A):>6,} {len(B):>6,} {len(U):>7,} {jf:>7,} {mf:>7,}  {jf==0 and mf==0}")
print("\nINTERSECTIONS against independence — are the arrows correlated?\n")
amb=len(base)
frac={n:len(X((n,)))/amb for n in names}
print(f"  ambient {amb:,}")
for n in names: print(f"    {n:<11} {len(X((n,))):>6,}  = {100*frac[n]:.1f}%")
for r in (2,3,4):
    for combo in combinations(names,r):
        actual=len(X(combo)); indep=amb
        for n in combo: indep*=frac[n]
        print(f"  {' ∩ '.join(combo):<40} actual {actual:>6,}   independent {indep:>8.0f}"
              f"   factor {actual/indep:>5.2f}")