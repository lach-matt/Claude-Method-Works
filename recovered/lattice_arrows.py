import numpy as np, sys
from collections import defaultdict
from itertools import combinations
sys.setrecursionlimit(100000)
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
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
names=list(W)
def closed(cells):
    if len(cells)<2: return 0,0
    X=np.array(cells,dtype=np.int16); N=len(X)
    rad=(X.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
    for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
    enc=lambda A:(A.astype(np.int64)*mult).sum(1)
    S=set(enc(X).tolist()); jf=mf=0
    for i in range(N):
        r=X[i]
        jf+=sum(1 for c in enc(np.maximum(r,X[i+1:])).tolist() if c not in S)
        mf+=sum(1 for c in enc(np.minimum(r,X[i+1:])).tolist() if c not in S)
    return jf,mf
def structure(cells):
    src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
    srcs={src(c) for c in cells}; by=defaultdict(list)
    for c in cells: by[src(c)].append(c)
    pairs=sum(len(by.get(tgt(a),())) for a in cells)
    E=defaultdict(set)
    for c in cells:
        if tgt(c) in srcs: E[src(c)].add(tgt(c))
    idx={};low={};on={};st=[];comp=[];ctr=[0]
    def strong(v):
        idx[v]=low[v]=ctr[0];ctr[0]+=1;st.append(v);on[v]=True
        for w in E.get(v,()):
            if w not in idx: strong(w);low[v]=min(low[v],low[w])
            elif on.get(w): low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            c=[]
            while True:
                w=st.pop();on[w]=False;c.append(w)
                if w==v:break
            comp.append(c)
    for v in sorted(srcs): 
        if v not in idx: strong(v)
    nontriv=[c for c in comp if len(c)>1]
    loops=sum(1 for A in E if A in E[A])
    return pairs,len(comp),sorted((len(c) for c in comp),reverse=True),len(nontriv),loops
print(f"{'arrows imposed':<34} {'cells':>7} {'join':>7} {'meet':>7} {'pairs':>9} "
      f"{'SCCs':>5} {'multi':>6} {'loops':>6}")
seen={}
for r in range(0,5):
    for combo in combinations(names,r):
        C=[c for c in base if all(c[W[w][1]]<=c[W[w][0]] for w in combo)]
        jf,mf=closed(C); p,ns,sz,nt,lp=structure(C)
        lab="none (ambient)" if not combo else " ∩ ".join(combo)
        print(f"{lab:<34} {len(C):>7,} {jf:>7} {mf:>7} {p:>9,} {ns:>5} {nt:>6} {lp:>6}")
        seen[combo]=len(C)
print(f"\ndistinct sub-indices among the 16 subsets: {len(set(seen.values()))}")