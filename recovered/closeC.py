from itertools import combinations, product
from collections import defaultdict
import sys

# ---------- O3: is the density a vanishing trend or a cone-volume ratio? ----------
def exact(n,N):
    out=[]
    def rec(p,prev,tot):
        if len(p)==n:
            S=[];r=0
            for m in p: r+=m; S.append(r)
            out.append(tuple(S)); return
        for m in range(0,min(prev,N-tot)+1): rec(p+[m],m,tot+m)
    rec([],N,0); return out
def chain(n,N):
    c=[(s,) for s in range(N+1)]
    for k in range(1,n):
        c=[x+(t,) for x in c for t in range(x[-1],min((k+1)*x[-1]//k,N)+1)]
    return c
print("O3 — the density against the cap, at fixed n")
for n in (3,4):
    row=[]
    for N in (20,40,60,80,120):
        row.append(100*len(exact(n,N))/len(chain(n,N)))
    print(f"  n={n}: " + "  ".join(f"N={N}: {d:.2f}%" for N,d in zip((20,40,60,80,120),row)))
    print(f"        successive differences: {[round(row[i+1]-row[i],3) for i in range(len(row)-1)]}")
sys.stdout.flush()

# ---------- O4: does a source seniority restore composability at Λ10? ----------
NM,EM,LM,KM,FM=3,3,1,3,1
L10s=[]
for n in range(1,NM+1):
 for l in range(0,min(LM,n-1)+1):
  for k in range(1,min(KM,2*(2*l+1))+1):
   for q in range(0,k+1):
    for s in range(0,k+1):
     for w in range(s,k+1):                      # source seniority w: 2S <= w <= k
      for e in range(1,EM+1):
       for f in range(0,min(FM,e-1)+1):
        for g in range(0,min(q,2*(2*f+1))+1):
         for sp in range(0,g+1):
          for v in range(sp,g+1):
           L10s.append((n,l,k,q,e,f,g,s,sp,v,w))
S=set(L10s)
bad=0
for a,b in combinations(L10s[:1200],2):
    if tuple(map(max,a,b)) not in S or tuple(map(min,a,b)) not in S: bad+=1
src=lambda c:(c[0],c[1],c[2],c[7],c[10]); tgt=lambda c:(c[4],c[5],c[6],c[8],c[9])
srcs={src(c) for c in L10s}; tgts={tgt(c) for c in L10s}
by=defaultdict(list)
for c in L10s: by[src(c)].append(c)
comp=lambda a,b:(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8],b[9],a[10])
pairs=fail=0
for a in L10s:
    for b in by.get(tgt(a),()):
        pairs+=1
        if comp(a,b) not in S: fail+=1
print(f"\nO4 — Λ₁₀ with a source seniority (2S ≤ w ≤ k)")
print(f"  cells {len(L10s):,}  join/meet failures on 1,200-cell sample: {bad}")
print(f"  targets that are legal sources: {len(tgts & srcs)} of {len(tgts)}")
print(f"  composable pairs {pairs:,}  closure failures {fail}")
print(f"  COMPOSES: {pairs>0 and fail==0}")
sys.stdout.flush()

# ---------- O8: which pairwise sums may be adjoined under E2? ----------
def nbody(N):
    return [(a,a+b,a+b+c) for a in range(N+1) for b in range(a+1) for c in range(b+1) if a+b+c<=N]
X=nbody(12)
def adjoin(h):
    Y=[x+(h(x),) for x in X]; S=set(Y); j=m=0
    for a,b in combinations(Y,2):
        if tuple(map(max,a,b)) not in S: j+=1
        if tuple(map(min,a,b)) not in S: m+=1
    return j,m
print("\nO8 — adjoining each pairwise sum as a coordinate (E2 / A.6)")
for nm,h in [("S₁₂ = m₁+m₂  (already a coordinate)", lambda x:x[1]),
             ("S₁₃ = m₁+m₃  = M − S + m₁",           lambda x:x[2]-x[1]+x[0]),
             ("S₂₃ = m₂+m₃  = M − m₁",               lambda x:x[2]-x[0]),
             ("M    (already a coordinate)",          lambda x:x[2]),
             ("min(m₁, M−S)  a meet-morphism",        lambda x:min(x[0],x[2]-x[1]))]:
    j,m=adjoin(h)
    print(f"  {nm:<38} join failures {j:>5}  meet failures {m:>5}  admissible: {j==0 and m==0}")