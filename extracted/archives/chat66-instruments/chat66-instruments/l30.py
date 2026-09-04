import collections, itertools, time, statistics
from tower2mod import L8,L9
t0=time.time()
A=L9(); N=len(A); S=set(A)
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
objs=set(src(c) for c in A); print('source objects',len(objs),'target sigs',len(set(tgt(c) for c in A)),'union',len(objs|set(tgt(c) for c in A)))
steps=set((src(c),tgt(c)) for c in A if tgt(c) in objs)
print('ordered object pairs joined by a step (targets that are objects):',len(steps),'of',len(objs)**2, '; steps raising k:',sum(1 for s,t in steps if t[2]>s[2]))
# SCCs (Tarjan-equivalent via networkx-free Kosaraju)
adj=collections.defaultdict(set)
for s,t in steps: adj[s].add(t)
nodes=sorted(objs); order=[]; seen=set()
def dfs(u):
    stack=[(u,iter(adj[u]))]; seen.add(u)
    while stack:
        v,it=stack[-1]
        for w in it:
            if w not in seen: seen.add(w); stack.append((w,iter(adj[w]))); break
        else: order.append(v); stack.pop()
for u in nodes:
    if u not in seen: dfs(u)
radj=collections.defaultdict(set)
for s,t in steps: radj[t].add(s)
comp={}; 
for u in reversed(order):
    if u in comp: continue
    st=[u]; comp[u]=u
    while st:
        v=st.pop()
        for w in radj[v]:
            if w not in comp: comp[w]=u; st.append(w)
sccs=collections.defaultdict(list)
for u,r in comp.items(): sccs[r].append(u)
big=[sorted(v) for v in sccs.values() if len(v)>1]
print('SCCs of size>1:',len(big),[ (len(v),set(o[2] for o in v)) for v in big],' singletons:',sum(1 for v in sccs.values() if len(v)==1))
# pair census: comparable ordered pairs (x<=y) and composition-path reachability
idx={c:i for i,c in enumerate(A)}
comp_pairs=sum(1 for x in A for y in A if all(a<=b for a,b in zip(x,y)))
print('comparable ordered pairs (incl. x=y):',comp_pairs, f'{100*comp_pairs/N**2:.1f}%', '; excl x=y:',comp_pairs-N)
# reachability by composition: a->b when tgt(a)==src(b)
bysrc=collections.defaultdict(list)
for c in A: bysrc[src(c)].append(c)
nxt={c:bysrc.get(tgt(c),[]) for c in A}
reach=0; both=0; reach_refl=0
for a in A:
    seen={a}; st=[a]; strict=set()
    while st:
        v=st.pop()
        for w in nxt[v]:
            if w not in seen: seen.add(w); st.append(w)
    seen.discard(a)
    # a reaches itself only if in a cycle
    cyc=any(a in nxt[w] for w in seen) or a in nxt[a]
    reach+=len(seen)+(1 if cyc else 0)
    both+=sum(1 for w in seen if all(p<=q for p,q in zip(a,w)))+(1 if cyc else 0)
print('composition-path ordered pairs (incl. cycles back to self):',reach,f'{100*reach/N**2:.1f}%','; in both:',both,f'{100*both/N**2:.1f}%')
print('time',round(time.time()-t0))
