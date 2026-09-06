import numpy as np, random
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
BASE=set(base)
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
X=lambda combo:{c for c in base if all(c[W[w][1]]<=c[W[w][0]] for w in combo)}
names=list(W)

def generate(S):
    """close a set under join and meet inside the ambient"""
    cur=set(S)
    while True:
        new=set()
        cur_l=list(cur)
        for a,b in combinations(cur_l,2):
            j=tuple(map(max,a,b)); m=tuple(map(min,a,b))
            if j not in cur: new.add(j)
            if m not in cur: new.add(m)
        if not new: return cur
        cur|=new

print("CLAIM 1 — the join of two arrows: union not closed, but what does it generate?\n")
print(f"ambient {len(base):,}")
for a,b in combinations(names,2):
    A=X((a,)); B=X((b,)); U=A|B
    gen=generate(U)
    print(f"  {a+' ∪ '+b:<26} |union| {len(U):>6,}  |generated| {len(gen):>6,}  "
          f"= ambient: {gen==BASE}")

print("\nCLAIM 2 — the extraction X ↦ X_w is an interior operator\n")
def extract(S,w):
    i,j=W[w]; return {c for c in S if c[j]<=c[i]}
random.seed(3)
subs=[set(random.sample(base,random.randint(50,400))) for _ in range(200)]
for w in names:
    contractive=all(extract(S,w)<=S for S in subs)
    idem=all(extract(extract(S,w),w)==extract(S,w) for S in subs)
    mono=all(extract(P,w)<=extract(Q,w) for P,Q in
             [(subs[i],subs[i]|subs[i+1]) for i in range(len(subs)-1)])
    fixed = extract(X((w,)),w)==X((w,))
    print(f"  {w:<11} contractive {contractive}  monotone {mono}  idempotent {idem}  "
          f"X_w is a fixed point {fixed}")