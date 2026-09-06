import sys
from itertools import combinations
from collections import defaultdict
sys.setrecursionlimit(50000)
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
names=list(W)
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
    return out
def sccs(cells):
    src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
    srcs={src(c) for c in cells}; E=defaultdict(set)
    for c in cells:
        if tgt(c) in srcs: E[src(c)].add(tgt(c))
    idx={};low={};on={};st=[];n=[0];cnt=[0]
    def s(v):
        idx[v]=low[v]=n[0]; n[0]+=1; st.append(v); on[v]=True
        for w in E.get(v,()):
            if w not in idx: s(w); low[v]=min(low[v],low[w])
            elif on.get(w): low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            while True:
                w=st.pop(); on[w]=False
                if w==v: break
            cnt[0]+=1
    for v in sorted(srcs):
        if v not in idx: s(v)
    return cnt[0], len(srcs)
import sys as S
cp=tuple(int(x) for x in S.argv[1].split(','))
base=build(*cp); res={}
for r in range(5):
    for combo in combinations(names,r):
        C=[c for c in base if all(c[W[w][1]]<=c[W[w][0]] for w in combo)]
        res[frozenset(combo)]=sccs(C)[0]
_,nobj=sccs(base)
edges=[(a,b) for a in res for b in res if a<b and len(b)==len(a)+1]
bad=[(a,b) for a,b in edges if res[b]<res[a]]
singles={n:res[frozenset([n])] for n in names}
print(f"caps {cp}: {len(base):>7,} cells  {nobj:>3} objects   "
      f"singles {singles}   all four = {res[frozenset(names)]}   "
      f"edges {len(edges)}  decreases {len(bad)}  monotone {not bad}")