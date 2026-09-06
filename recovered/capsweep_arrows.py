import numpy as np, math
from itertools import combinations
from collections import deque
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
names=list(W)
adj={'shell':['subshell'],'subshell':['shell','occupancy'],
     'occupancy':['subshell','spin'],'spin':['occupancy']}
def dist(a,b):
    q=deque([(a,0)]); seen={a}
    while q:
        u,d=q.popleft()
        if u==b: return d
        for v in adj[u]:
            if v not in seen: seen.add(v); q.append((v,d+1))
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
caps=[(3,3,1,3,1),(4,4,1,3,1),(3,3,1,4,1),(4,4,2,4,2)]
for cp in caps:
    A=build(*cp); N=len(A)
    mask=lambda combo: np.logical_and.reduce([A[:,W[w][1]]<=A[:,W[w][0]] for w in combo])
    frac={w:mask((w,)).sum()/N for w in names}
    rows=[]
    for a,b in combinations(names,2):
        act=mask((a,b)).sum(); ind=N*frac[a]*frac[b]
        rows.append((dist(a,b), act/ind, a, b))
    ds=[r[0] for r in rows]; fs=[math.log(r[1]) for r in rows]
    mu=sum(ds)/len(ds); mv=sum(fs)/len(fs)
    num=sum((x-mu)*(y-mv) for x,y in zip(ds,fs))
    den=(sum((x-mu)**2 for x in ds)*sum((y-mv)**2 for y in fs))**0.5
    byd={d:[f for dd,f,_,_ in rows if dd==d] for d in (1,2,3)}
    mono=all(max(byd[d])<min(byd[d-1]) for d in (2,3) if byd[d] and byd[d-1])
    allfour=mask(tuple(names)).sum()
    indep=N
    for w in names: indep*=frac[w]
    print(f"caps {cp}: |X|={N:>7,}  corr(dist, log factor) {num/den:+.3f}  "
          f"strictly monotone in distance: {mono}")
    print(f"      d=1 {[round(x,3) for x in sorted(byd[1],reverse=True)]}  "
          f"d=2 {[round(x,3) for x in sorted(byd[2],reverse=True)]}  "
          f"d=3 {[round(x,3) for x in byd[3]]}   all four: {allfour/indep:.2f}")