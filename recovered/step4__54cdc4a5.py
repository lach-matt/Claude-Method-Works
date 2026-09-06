from itertools import combinations
from collections import defaultdict
import sys

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

def step(X):
    d=len(X[0]); S=set(X)
    # producers, stored per cell as a list of the OTHER member for quick hitting tests
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
    # candidate: unit-step boxes free in exactly two coordinates -> 4 cells
    for a in X:
        for c1,c2 in combinations(range(d),2):
            hi=list(a); ok=True
            for c in (c1,c2):
                vs=vals[c]; i=vs.index(a[c])
                if i+1>=len(vs): ok=False;break
                hi[c]=vs[i+1]
            if not ok: continue
            box=[y for y in X if all(a[i]<=y[i]<=hi[i] for i in range(d))]
            if len(box)==4 and removable(box):
                return 4,(c1,c2),tuple(a),tuple(hi)
    return None

for caps in [(3,3,1,3),(4,4,1,3),(3,3,1,4),(4,4,1,4),(5,5,1,3)]:
    X=lam(*caps)
    r=step(X)
    print(f"caps {caps}: |Λ|={len(X):>5}  ", end="")
    if r:
        n,free,lo,hi=r
        print(f"step {n}, free in coordinates {free}  survivor {len(X)-n} = {100*(len(X)-n)/len(X):.2f}%")
    else:
        print("no 4-cell unit box removable")
    sys.stdout.flush()