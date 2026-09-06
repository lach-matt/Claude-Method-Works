from itertools import combinations, product
from collections import defaultdict

def lam(NM,EM,LM,KM,FM=1):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            out.append((n,l,k,q,e,f,g,s))
    return out

def step(X):
    d=len(X[0]); S=set(X)
    prod=defaultdict(list)
    for a,b in combinations(X,2):
        j=tuple(map(max,a,b)); m=tuple(map(min,a,b))
        if j!=a and j!=b: prod[j].append((a,b))
        if m!=a and m!=b: prod[m].append((a,b))
    def removable(R):
        Rs=set(R)
        for z in R:
            for a,b in prod[z]:
                if a not in Rs and b not in Rs: return False
        return True
    vals=[sorted({x[i] for x in X}) for i in range(d)]
    best=None
    for size in range(2,33):
        # boxes of exactly this cell-count, built from a corner and an extent vector
        for a in X:
            # extents: choose which coordinates are free and by how much
            for k in range(1,4):
                for coords in combinations(range(d),k):
                    hi=list(a)
                    ok=True
                    for c in coords:
                        vs=vals[c]; i=vs.index(a[c])
                        if i+1>=len(vs): ok=False;break
                        hi[c]=vs[i+1]
                    if not ok: continue
                    box=tuple(sorted(y for y in X if all(a[i]<=y[i]<=hi[i] for i in range(d))))
                    if len(box)!=size: continue
                    if removable(box):
                        free=[i for i in range(d) if len({c[i] for c in box})>1]
                        return len(box), free, box[0], box[-1]
    return None

for caps in [(3,3,1,3),(4,4,1,3),(3,3,1,4),(4,4,1,4)]:
    X=lam(*caps)
    r=step(X)
    if r:
        n,free,lo,hi=r
        print(f"caps {caps}: |Λ|={len(X):>5}  step = {n}  free in {len(free)} coordinates {free}")
        print(f"    from {lo}  to {hi}   survivor {len(X)-n} = {100*(len(X)-n)/len(X):.2f}%")
    else:
        print(f"caps {caps}: |Λ|={len(X):>5}  no removable box of size ≤ 32 with ≤3 free coordinates")