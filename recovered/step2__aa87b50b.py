from itertools import combinations
from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])

def analyse(X,label):
    S=set(X); le=lambda a,b: all(p<=q for p,q in zip(a,b))
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
    # size 1 and 2, exhaustive
    one=[x for x in X if removable([x])]
    two=[p for p in combinations(X,2) if removable(p)]
    # size 3: for z in R the other two must hit every producing pair of z
    three=[]
    for z in X:
        pairs=prod[z]
        if not pairs: continue
        cand=set()
        for a,b in pairs: cand.add(a); cand.add(b)
        cand={c for c in cand if c!=z}
        for u,v in combinations(sorted(cand),2):
            if removable([z,u,v]): three.append((z,u,v))
    # smallest removable coordinate box
    d=len(X[0]); best=None
    los=[sorted({x[i] for x in X}) for i in range(d)]
    seen=set()
    for a in X:
        for b in X:
            if not le(a,b) or a==b: continue
            box=tuple(sorted(y for y in X if all(a[i]<=y[i]<=b[i] for i in range(d))))
            if box in seen: continue
            seen.add(box)
            if (best is None or len(box)<len(best)) and removable(box):
                best=box
    free=[i for i in range(d) if len({c[i] for c in best})>1] if best else []
    print(f"{label}: |X|={len(X):>6}  removable singletons {len(one)}  pairs {len(two)}  "
          f"triples {len(three)}  smallest removable box {len(best)} "
          f"free in {len(free)} coordinates {free}")
    return len(best)

analyse(L8,"Lambda_8 caps (3,3,1,3)      ")

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
for caps in [(4,4,1,3),(4,4,1,4),(5,5,1,3)]:
    Y=lam(*caps)
    if len(Y)<=1600: analyse(Y,f"Lambda_8 caps {caps}")