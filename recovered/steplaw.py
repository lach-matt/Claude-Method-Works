from itertools import combinations
from collections import defaultdict
from functools import reduce
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
le=lambda a,b: all(p<=q for p,q in zip(a,b))

def analyse(X,label,verify=False):
    d=len(X[0]); S=set(X)
    bot=min(X,key=sum); top=max(X,key=sum)
    JI=[];MI=[]
    for x in X:
        B=[y for y in X if le(y,x) and y!=x]
        A=[y for y in X if le(x,y) and y!=x]
        if x!=bot and reduce(lambda p,q:tuple(map(max,p,q)),B)!=x: JI.append(x)
        if x!=top and reduce(lambda p,q:tuple(map(min,p,q)),A)!=x: MI.append(x)
    best=None
    for a in JI:
        for b in MI:
            if le(a,b):
                n=sum(1 for y in X if le(a,y) and le(y,b))
                if best is None or n<best[0]: best=(n,a,b)
    print(f"{label}: |Λ|={len(X):>5}  |J|={len(JI)} |M|={len(MI)} both={len(set(JI)&set(MI))}  "
          f"predicted step = {best[0]}")
    print(f"    interval {best[1]} .. {best[2]}")
    if verify:
        prod=defaultdict(list)
        for u,v in combinations(X,2):
            j=tuple(map(max,u,v)); m=tuple(map(min,u,v))
            if j!=u and j!=v: prod[j].append((u,v))
            if m!=u and m!=v: prod[m].append((u,v))
        def removable(R):
            Rs=set(R)
            return all(not(u not in Rs and v not in Rs) for z in R for u,v in prod[z])
        JIs,MIs=set(JI),set(MI); agree=dis=0
        for a in X:
            for b in X:
                if not le(a,b): continue
                R=[y for y in X if le(a,y) and le(y,b)]
                pred = (a in JIs) and (b in MIs)
                if pred==removable(R): agree+=1
                else: dis+=1
        print(f"    criterion tested on all {agree+dis:,} intervals: {dis} disagreements")
        box=[y for y in X if le(best[1],y) and le(y,best[2])]
        rest=[y for y in X if y not in set(box)]; RS=set(rest)
        bad=sum(1 for u,v in combinations(rest,2)
                if tuple(map(max,u,v)) not in RS or tuple(map(min,u,v)) not in RS)
        print(f"    removing it leaves {len(rest)} cells with {bad} join/meet failures")

analyse(lam(3,3,1,3),"caps (3,3,1,3)",verify=True)
for caps in [(3,3,1,4),(4,4,1,3),(4,4,1,4),(5,5,1,3)]:
    analyse(lam(*caps),f"caps {caps}")