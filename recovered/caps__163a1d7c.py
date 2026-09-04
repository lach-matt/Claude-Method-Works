from itertools import product
from collections import defaultdict
import sys; sys.setrecursionlimit(200000)

def build(NM,EM,LM,KM,FM):
    cells=[]
    for n in range(1,NM+1):
several=0
def lam9(NM,EM,LM,KM,FM):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            for sp in range(0,g+1):
             out.append((n,l,k,q,e,f,g,s,sp))
    return out

def analyse(caps):
    C=lam9(*caps)
    src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
    sources={src(c) for c in C}
    edges=defaultdict(set)
    for c in C:
        if tgt(c) in sources: edges[src(c)].add(tgt(c))
    rise=sum(1 for A in edges for B in edges[A] if B[2]>A[2])
    idx={};low={};on={};st=[];comp=[];ctr=[0]
    def strong(v):
        idx[v]=low[v]=ctr[0];ctr[0]+=1;st.append(v);on[v]=True
        for w in edges.get(v,()):
            if w not in idx: strong(w);low[v]=min(low[v],low[w])
            elif on.get(w): low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            c=[]
            while True:
                w=st.pop();on[w]=False;c.append(w)
                if w==v:break
            comp.append(c)
    for v in list(edges):
        if v not in idx: strong(v)
    pure=all(len({A[2] for A in c})==1 for c in comp)
    covered=sorted({c[0][2] for c in comp if len(c)>1})
    by_tgt=defaultdict(list)
    for c in C: by_tgt[tgt(c)].append(c)
    ids=[A for A in sources if all(x[3]==x[6] for x in by_tgt[A])]
    kmax=max(A[2] for A in sources)
    cons=sum(1 for c in C if c[3]==c[6])
    print(f"caps {caps}: |L9|={len(C):>7,}  objects={len(sources):>4}  "
          f"occupancy rises={rise}  SCCs={sorted((len(c) for c in comp),reverse=True)[:6]}  "
          f"SCCs pure in k={pure}  cyclic k-levels={covered}  "
          f"identities={len(ids)} all at k={ {A[2] for A in ids} } (kmax={kmax})  "
          f"conservative={100*cons/len(C):.1f}%")

for caps in [(3,3,1,3,1),(4,4,1,6,1),(4,4,2,6,2),(5,5,2,6,2)]:
    analyse(caps)