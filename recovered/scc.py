from collections import defaultdict
exec(open('/home/claude/timetravel.py').read().split('# --- identities')[0])

# strongly connected components of the object graph
import sys; sys.setrecursionlimit(100000)
nodes=list(edges); idx={};low={};on={};st=[];comp=[];ctr=[0]
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
for v in nodes:
    if v not in idx: strong(v)
sizes=sorted((len(c) for c in comp),reverse=True)
print("SCC sizes:",sizes)
big=[c for c in comp if len(c)>1]
print(f"multi-object strongly connected components: {len(big)}")
for c in big:
    ks={A[2] for A in c}
    print(f"  size {len(c)}  occupancies present: {sorted(ks)}")
    for A in sorted(c): print("   ",A)

# does any composable chain visit two objects of different occupancy and return?
print("\noccupancy along every edge:")
drop=defaultdict(int)
for A in edges:
    for B in edges[A]: drop[(A[2],B[2])]+=1
for (a,b),n in sorted(drop.items()): print(f"  k {a} -> k {b}: {n} edges")

# which 8 objects carry an identity
by_tgt=defaultdict(list)
for c in cells: by_tgt[tgt(c)].append(c)
ids=[A for A in sources if all(c[3]==c[6] for c in by_tgt[A])]
print(f"\nobjects whose every incoming transition is conservative (q==g): {len(ids)}")
for A in sorted(ids): print("   ",A)