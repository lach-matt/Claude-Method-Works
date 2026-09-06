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
A0=np.array(base,dtype=np.int16)
rad=(A0.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
enc=lambda M:(M.astype(np.int64)*mult).sum(1)
dec={int(c):t for c,t in zip(enc(A0).tolist(),base)}
BASE=set(dec)
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
names=list(W)
def Xcodes(combo):
    m=np.ones(len(base),dtype=bool)
    for w in combo:
        i,j=W[w]; m &= (A0[:,j]<=A0[:,i])
    return set(enc(A0[m]).tolist())
def generate(codes):
    cur=set(codes)
    while True:
        arr=np.array([dec[c] for c in cur],dtype=np.int16)
        new=set()
        for i in range(len(arr)):
            r=arr[i]
            new|=set(enc(np.maximum(r,arr[i+1:])).tolist())
            new|=set(enc(np.minimum(r,arr[i+1:])).tolist())
        new-=cur
        if not new: return cur
        cur|=new
print(f"ambient {len(base):,}")
for a,b in combinations(names,2):
    U=Xcodes((a,))|Xcodes((b,))
    g=generate(U)
    print(f"  {a+' ∪ '+b:<26} union {len(U):>6,}  generated {len(g):>6,}  "
          f"= ambient: {g==BASE}")