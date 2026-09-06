from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
NM,EM,LM,KM,FM=3,3,1,3,1
cells=[]
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
          cells.append((n,l,k,q,e,f,g,s,sp,G))
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[9],c[8])
srcs={src(c) for c in cells}
E=defaultdict(set)
for c in cells:
    if tgt(c) in srcs: E[src(c)].add(tgt(c))
objs=sorted(srcs)
print(f"cells {len(cells):,}   objects {len(objs)}   edges {sum(len(v) for v in E.values()):,}")
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
for v in objs:
    if v not in idx: strong(v)
sizes=sorted((len(c) for c in comp),reverse=True)
print(f"strongly connected components: {len(comp)}   sizes {sizes[:8]}")
print(f"strongly connected overall: {len(comp)==1}")
if sizes[0]>1:
    big=[c for c in comp if len(c)==sizes[0]][0]
    print(f"  largest SCC covers {100*sizes[0]/len(objs):.1f}% of objects, "
          f"occupancies present {sorted({o[2] for o in big})}")
# any monotone coordinate at all?
print("\nis any single coordinate monotone along composition?")
NAME=['n','l','k','q','e','f','g','2S',"2S'",'G']
by=defaultdict(list)
for c in cells: by[src(c)].append(c)
comps=[]
for a in cells:
    for b in by.get(tgt(a),()): comps.append((a,b))
print(f"  composable pairs {len(comps):,}")
for i,nm in enumerate(NAME):
    up=sum(1 for a,b in comps if b[i]>a[i]); dn=sum(1 for a,b in comps if b[i]<a[i])
    if up==0 or dn==0:
        print(f"  {nm:>4}: rises {up:>9,}  falls {dn:>9,}   MONOTONE")
    else:
        print(f"  {nm:>4}: rises {up:>9,}  falls {dn:>9,}")