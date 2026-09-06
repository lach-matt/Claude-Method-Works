from itertools import combinations
from collections import defaultdict
# Lambda_8 rebuilt with the value ranges extended below zero
def build(kmin, qmin, gmin, NM=3,EM=3,LM=1,KM=3,FM=1):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(kmin,min(KM,2*(2*l+1))+1):
       for q in range(qmin,k+1):
        for s in range(0,max(0,k)+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(gmin,min(q,2*(2*f+1))+1):
            out.append((n,l,k,q,e,f,g,s))
    return out

def closed(X):
    S=set(X); bad=0
    for a,b in combinations(X,2):
        if tuple(map(max,a,b)) not in S or tuple(map(min,a,b)) not in S: bad+=1
    return bad

print("does admitting negative occupancy or transfer change anything?\n")
for label,(km,qm,gm) in [("as built  k≥1, q≥0, g≥0",(1,0,0)),
                          ("k≥0",(0,0,0)),
                          ("k,q,g ≥ −1",(-1,-1,-1)),
                          ("k,q,g ≥ −2",(-2,-2,-2))]:
    X=build(km,qm,gm)
    bad=closed(X) if len(X)<3000 else None
    rises=sum(1 for c in X if c[6]>c[2])          # target occupancy above source
    viol=sum(1 for c in X if not (c[6]<=c[3]<=c[2]))
    print(f"  {label:<26} |Λ|={len(X):>5}  join/meet failures {bad}  "
          f"cells with g>k {rises}  cells violating g≤q≤k {viol}")

print("\nthe clock, on the extended object:")
X=build(-2,-2,-2)
src=lambda c:(c[0],c[1],c[2]); tgt=lambda c:(c[4],c[5],c[6])
srcs={src(c) for c in X}
edges=[(src(c),tgt(c)) for c in X if tgt(c) in srcs]
up=sum(1 for a,b in edges if b[2]>a[2])
print(f"  composable steps {len(edges)}, steps raising occupancy: {up}")

print("\nand the reversal, on Λ₉ — swap source and target:")
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
L9=[c+(sp,) for c in L8 for sp in range(0,c[6]+1)]
S9=set(L9)
rev=lambda c:(c[4],c[5],c[6],c[3],c[0],c[1],c[2],c[8],c[7])
R=[rev(c) for c in L9]
inter=[c for c in L9 if c in set(R)]
print(f"  |Λ₉| = {len(L9)}   |reverse(Λ₉)| = {len(R)}   |Λ₉ ∩ reverse(Λ₉)| = {len(inter)}")
if inter:
    ok=all(c[6]==c[3]==c[2] for c in inter)
    print(f"  every cell of the intersection has g = q = k: {ok}")
    print(f"  i.e. total transfer, nothing lost — the reversible cells")
    print(f"  sample: {inter[:3]}")
badr=0
Rs=set(R)
for a,b in combinations(R,2):
    if tuple(map(max,a,b)) not in Rs or tuple(map(min,a,b)) not in Rs: badr+=1
print(f"  reverse(Λ₉) is itself closed: {badr} join/meet failures")