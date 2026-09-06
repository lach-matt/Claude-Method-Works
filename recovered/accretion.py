import numpy as np
from collections import defaultdict
NM,EM,LM,KM,FM=3,3,1,3,1
def build(bound):
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
             if bound and G>k: continue
             for sp in range(0,G+1):
              out.append((n,l,k,q,e,f,g,s,sp,G))
    return out
def closed(cells):
    X=np.array(cells,dtype=np.int16); N=len(X)
    rad=(X.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
    for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
    enc=lambda A:(A.astype(np.int64)*mult).sum(1)
    S=set(enc(X).tolist()); jf=mf=0
    for i in range(N):
        r=X[i]
        jf+=sum(1 for c in enc(np.maximum(r,X[i+1:])).tolist() if c not in S)
        mf+=sum(1 for c in enc(np.minimum(r,X[i+1:])).tolist() if c not in S)
    return jf,mf,N*(N-1)//2
def clock(cells):
    src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
    srcs={src(c) for c in cells}; by=defaultdict(list)
    for c in cells: by[src(c)].append(c)
    pairs=rise=0
    for a in cells:
        for b in by.get(tgt(a),()):
            pairs+=1
            if b[2]>a[2]: rise+=1
    E=defaultdict(set)
    for c in cells:
        if tgt(c) in srcs: E[src(c)].add(tgt(c))
    import sys; sys.setrecursionlimit(100000)
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
    pure=all(len({o[2] for o in c})==1 for c in comp)
    return pairs,rise,len(comp),sorted((len(c) for c in comp),reverse=True),pure

for name,bnd in (("extended, accretion unbounded",False),("extended + G ≤ k",True)):
    C=build(bnd); jf,mf,np_=closed(C)
    pr,ri,ns,sz,pure=clock(C)
    print(f"{name}")
    print(f"  cells {len(C):,}   pairs {np_:,}   join {jf}  meet {mf}")
    print(f"  composable pairs {pr:,}   steps raising occupancy {ri:,}"
          f"  = {100*ri/pr:.1f}%" if pr else "")
    print(f"  SCCs {ns}  sizes {sz[:6]}  pure in occupancy: {pure}")
    print()
print("Λ₉ as built is the sub-index G = g (empty destinations): "
      f"{len(build(True))} cells with G ≤ k against 1,654 with G = g")