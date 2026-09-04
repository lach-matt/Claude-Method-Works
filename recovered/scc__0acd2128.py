from collections import defaultdict
exec(open('/home/claude/timetravel.py').read().split('# --- identities')[0])
edges=defaultdict(set)
for c in cells: edges[src(c)].add(tgt(c))
edges={A:{B for B in edges[A] if B in sources} for A in edges}   # composable steps only
import sys; sys.setrecursionlimit(100000)
idx={};low={};on={};st=[];comp=[];ctr=[0]
def strong(v):
    idx[v]=low[v]=ctr[0]; ctr[0]+=1; st.append(v); on[v]=True
    for w in edges.get(v,()):
        if w not in idx: strong(w); low[v]=min(low[v],low[w])
        elif on.get(w): low[v]=min(low[v],idx[w])
    if low[v]==idx[v]:
        c=[]
        while True:
            w=st.pop(); on[w]=False; c.append(w)
            if w==v: break
        comp.append(c)
for v in list(edges):
    if v not in idx: strong(v)
print("SCC sizes:",sorted((len(c) for c in comp),reverse=True))
big=[c for c in comp if len(c)>1]
print(f"multi-object SCCs: {len(big)}")
for c in big:
    print(f"  size {len(c)}  occupancies {sorted({A[2] for A in c})}")
    for A in sorted(c): print("     ",A)
drop=defaultdict(int)
for A in edges:
    for B in edges[A]: drop[(A[2],B[2])]+=1
print("\nedges by occupancy step:")
for (a,b),n in sorted(drop.items()): print(f"  k {a} -> k {b}: {n}")
by_tgt=defaultdict(list)
for c in cells: by_tgt[tgt(c)].append(c)
ids=[A for A in sources if all(c[3]==c[6] for c in by_tgt[A])]
print(f"\nobjects whose every incoming transition is conservative: {len(ids)}")
for A in sorted(ids): print("   ",A)