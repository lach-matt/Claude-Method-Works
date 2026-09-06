import numpy as np
from collections import defaultdict
NM,EM,LM,KM,FM=3,3,1,3,1
cells=[]
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
          cells.append((n,l,k,q,e,f,g,s,sp,G))
X=np.array(cells,dtype=np.int16); N=len(X)
rad=(X.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
enc=lambda A:(A.astype(np.int64)*mult).sum(1)
S=set(enc(X).tolist())
print(f"cells {N:,}   ambient {int(np.prod(rad)):,}   pairs {N*(N-1)//2:,}")
jf=mf=0
for i in range(N):
    r=X[i]
    for code in (enc(np.maximum(r,X[i+1:])), enc(np.minimum(r,X[i+1:]))):
        miss=len(code)-sum(1 for c in code.tolist() if c in S)
        if code is None: pass
    J=enc(np.maximum(r,X[i+1:])); M=enc(np.minimum(r,X[i+1:]))
    jf+=sum(1 for c in J.tolist() if c not in S)
    mf+=sum(1 for c in M.tolist() if c not in S)
print(f"exhaustive: join {jf}  meet {mf}")
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
by=defaultdict(list)
for c in cells: by[src(c)].append(c)
pairs=rise=0
for a in cells:
    for b in by.get(tgt(a),()):
        pairs+=1
        if b[2]>a[2]: rise+=1
print(f"composable pairs {pairs:,}   steps raising occupancy {rise:,}"
      f"  = {100*rise/pairs:.1f}%" if pairs else "no composable pairs")
print(f"the clock survives: {rise==0}")