import numpy as np
from collections import defaultdict
import sys
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
# object coordinates: source (n,l,k,2S) = idx 0,1,2,7 ; target (e,f,G,2S') = idx 4,5,9,8
SRC={'shell':0,'subshell':1,'occupancy':2,'spin':7}
TGT={'shell':4,'subshell':5,'occupancy':9,'spin':8}
def sub(wfun_s,wfun_t):
    return [c for c in base if wfun_t(c)<=wfun_s(c)]
def closed(cells):
    if not cells: return 0,0,0
    X=np.array(cells,dtype=np.int16); N=len(X)
    rad=(X.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
    for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
    enc=lambda A:(A.astype(np.int64)*mult).sum(1)
    S=set(enc(X).tolist()); jf=mf=0
    for i in range(N):
        r=X[i]
        jf+=sum(1 for c in enc(np.maximum(r,X[i+1:])).tolist() if c not in S)
        mf+=sum(1 for c in enc(np.minimum(r,X[i+1:])).tolist() if c not in S)
    return jf,mf,N
def eras(cells,ws,wt):
    src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
    srcs={src(c) for c in cells}; by=defaultdict(list)
    for c in cells: by[src(c)].append(c)
    pairs=rise=0
    for a in cells:
        for b in by.get(tgt(a),()):
            pairs+=1
            if ws(b)>ws(a): rise+=1
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
    return pairs,rise,len(comp),sorted((len(c) for c in comp),reverse=True)

print(f"ambient (accretion free): {len(base):,} cells\n")
print(f"{'weight':<28} {'cells':>7} {'join':>6} {'meet':>6} {'rises':>8} {'SCCs':>5}  {'sizes':<16} closed")
rows=[]
for nm in SRC:
    ws=lambda c,i=SRC[nm]: c[i]; wt=lambda c,i=TGT[nm]: c[i]
    C=sub(ws,wt); jf,mf,N=closed(C)
    p,r,ns,sz=eras(C,ws,wt) if C else (0,0,0,[])
    print(f"{nm:<28} {N:>7,} {jf:>6} {mf:>6} {r:>8,} {ns:>5}  {str(sz[:4]):<16} {jf==0 and mf==0}")
# composite weights
comps={'shell + occupancy':(lambda c:c[0]+c[2], lambda c:c[4]+c[9]),
       'rank (all four)':(lambda c:c[0]+c[1]+c[2]+c[7], lambda c:c[4]+c[5]+c[9]+c[8]),
       'max(shell,occupancy)':(lambda c:max(c[0],c[2]), lambda c:max(c[4],c[9])),
       'min(shell,occupancy)':(lambda c:min(c[0],c[2]), lambda c:min(c[4],c[9]))}
for nm,(ws,wt) in comps.items():
    C=sub(ws,wt); jf,mf,N=closed(C)
    p,r,ns,sz=eras(C,ws,wt) if C else (0,0,0,[])
    print(f"{nm:<28} {N:>7,} {jf:>6} {mf:>6} {r:>8,} {ns:>5}  {str(sz[:4]):<16} {jf==0 and mf==0}")