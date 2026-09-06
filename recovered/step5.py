from itertools import combinations
from collections import defaultdict
import sys, time
def lam(NM,EM,LM,KM):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(1,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            out.append((n,l,k,q,e,f,g,s))
    return out
X=lam(4,4,1,3); d=8; S=set(X)
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
t0=time.time(); best=None
for a in X:
    if time.time()-t0>900: break
    for k in (2,3):
        for coords in combinations(range(d),k):
            hi=list(a); ok=True
            for c in coords:
                vs=vals[c]; i=vs.index(a[c])
                if i+1>=len(vs): ok=False;break
                hi[c]=vs[i+1]
            if not ok: continue
            box=[y for y in X if all(a[i]<=y[i]<=hi[i] for i in range(d))]
            if len(box)>16: continue
            if (best is None or len(box)<len(best)) and removable(box):
                best=box
print(f"caps (4,4,1,3): |Λ|={len(X)}")
if best:
    free=[i for i in range(d) if len({c[i] for c in best})>1]
    print(f"  smallest removable unit box found: {len(best)} cells, free in {free}")
    print(f"  corners {best[0]} .. {best[-1]}")
else:
    print("  no removable unit box of ≤16 cells with 2 or 3 free coordinates")