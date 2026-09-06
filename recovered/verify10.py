import numpy as np
from itertools import product
NM,EM,LM,KM,FM=3,3,1,3,1
cells=[]
for n in range(1,NM+1):
 for l in range(0,min(LM,n-1)+1):
  for k in range(1,min(KM,2*(2*l+1))+1):
   for q in range(0,k+1):
    for s in range(0,k+1):
     for w in range(s,k+1):
      for e in range(1,EM+1):
       for f in range(0,min(FM,e-1)+1):
        for g in range(0,min(q,2*(2*f+1))+1):
         for sp in range(0,g+1):
          for v in range(sp,g+1):
           cells.append((n,l,k,q,e,f,g,s,sp,v,w))
X=np.array(cells,dtype=np.int16); N=len(X)
rad=(X.max(0)+1).astype(np.int64)
mult=np.ones(len(rad),dtype=np.int64)
for i in range(len(rad)-2,-1,-1): mult[i]=mult[i+1]*rad[i+1]
enc=lambda A: (A.astype(np.int64)*mult).sum(1)
S=set(enc(X).tolist())
print(f"|Λ₁₀ with source seniority| = {N:,}   ambient box = {int(np.prod(rad)):,}   "
      f"pairs = {N*(N-1)//2:,}")
jf=mf=0
for i in range(N):
    row=X[i]
    J=np.maximum(row,X[i+1:]); M=np.minimum(row,X[i+1:])
    for code,label in ((enc(J),'j'),(enc(M),'m')):
        miss=sum(1 for c in code.tolist() if c not in S)
        if label=='j': jf+=miss
        else: mf+=miss
print(f"EXHAUSTIVE: join failures {jf}   meet failures {mf}")
# and the closure operator, independently
A=[sorted(set(X[:,i].tolist())) for i in range(11)]
phi={}
for i in range(11):
    for j in range(11):
        if i==j: continue
        m={}
        for v in A[j]:
            sel=X[X[:,j]<=v]
            m[v]=int(sel[:,i].max()) if len(sel) else None
        phi[(i,j)]=m
out=0
def rec(p):
    global out
    k=len(p)
    if k==11: out+=1; return
    for v in A[k]:
        ok=True
        for j in range(k):
            b=phi[(k,j)][p[j]]
            if b is None or v>b: ok=False;break
            b2=phi[(j,k)][v]
            if b2 is None or p[j]>b2: ok=False;break
        if ok: rec(p+[v])
rec([])
print(f"|ℛ(X)| = {out:,}   E(X) = {out-N}")