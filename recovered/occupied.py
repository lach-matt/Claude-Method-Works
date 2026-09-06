from itertools import combinations, product
from collections import defaultdict
NM,EM,LM,KM,FM=3,3,1,3,1
# §17.4's repair: carry (g, G) with g = placed, G = total after arrival, g0 = G - g derived
cells=[]
for n in range(1,NM+1):
 for l in range(0,min(LM,n-1)+1):
  for k in range(1,min(KM,2*(2*l+1))+1):
   for q in range(0,k+1):
    for s in range(0,k+1):
     for e in range(1,EM+1):
      for f in range(0,min(FM,e-1)+1):
       for g in range(0,min(q,2*(2*f+1))+1):          # placed  ≤ q  and ≤ Pauli
        for G in range(g,2*(2*f+1)+1):                # total   ≥ g  and ≤ Pauli
         for sp in range(0,G+1):                      # target spin bounded by TOTAL
          cells.append((n,l,k,q,e,f,g,s,sp,G))
X=cells; S=set(X)
print(f"Λ₉ with occupied destinations: {len(X):,} cells   (Λ₉ as built: 1,654)")
jf=mf=0
for a,b in combinations(X,2):
    if tuple(map(max,a,b)) not in S: jf+=1
    if tuple(map(min,a,b)) not in S: mf+=1
print(f"  exhaustive over {len(X)*(len(X)-1)//2:,} pairs: join {jf}  meet {mf}")
A=[sorted({x[i] for x in X}) for i in range(10)]
phi={(i,j):{v:(max([x[i] for x in X if x[j]<=v]) if any(x[j]<=v for x in X) else None)
            for v in A[j]} for i in range(10) for j in range(10) if i!=j}
out=0
def rec(p):
    global out
    kk=len(p)
    if kk==10: out+=1; return
    for v in A[kk]:
        ok=True
        for j in range(kk):
            b=phi[(kk,j)][p[j]]
            if b is None or v>b: ok=False;break
            b2=phi[(j,kk)][v]
            if b2 is None or p[j]>b2: ok=False;break
        if ok: rec(p+[v])
rec([])
print(f"  |ℛ(X)| = {out:,}   E(X) = {out-len(X)}")

# composition now matches on TOTAL occupancy, not on the number placed
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
srcs={src(c) for c in X}
by=defaultdict(list)
for c in X: by[src(c)].append(c)
pairs=rise=0
for a in X:
    for b in by.get(tgt(a),()):
        pairs+=1
        if b[2] > a[2]: rise+=1     # k_b > k_a  -> the clock runs backwards
print(f"\n  composable pairs {pairs:,}")
print(f"  steps that RAISE occupancy: {rise:,}  = {100*rise/pairs:.1f}%" if pairs else "")
print(f"  the clock survives: {rise==0}")