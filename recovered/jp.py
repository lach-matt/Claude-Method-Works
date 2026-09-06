import numpy as np, sys
from itertools import combinations
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
names=list(W)
def build(NM,EM,LM,KM,FM):
    out=[]
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
              out.append((n,l,k,q,e,f,g,s,sp,G))
    return np.array(out,dtype=np.int16)
cp=tuple(int(x) for x in sys.argv[1].split(','))
A=build(*cp); N=len(A)
rad=(A.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
enc=lambda M:(M.astype(np.int64)*mult).sum(1)
dec=dict(zip(enc(A).tolist(),map(tuple,A.tolist())))
def codes(w):
    i,j=W[w]; return set(enc(A[A[:,j]<=A[:,i]]).tolist())
def gen(cs):
    cur=set(cs); front=np.array([dec[c] for c in cur],dtype=np.int16); allarr=front
    while True:
        new=set()
        for i in range(len(front)):
            r=front[i]
            new|=set(enc(np.maximum(r,allarr)).tolist())
            new|=set(enc(np.minimum(r,allarr)).tolist())
        new-=cur
        if not new: return cur
        cur|=new
        front=np.array([dec[c] for c in new],dtype=np.int16)
        allarr=np.array([dec[c] for c in cur],dtype=np.int16)
print(f"caps {cp}  ambient {N:,}")
worst=0
for a,b in combinations(names,2):
    g=gen(codes(a)|codes(b))
    frac=len(g)/N; worst=max(worst,frac)
    print(f"  {a+' ∪ '+b:<24} generated {len(g):>7,}  = {100*frac:>6.2f}%  proper {len(g)<N}")
print(f"  worst case {100*worst:.2f}% of the ambient — all joins proper: {worst<1.0}")