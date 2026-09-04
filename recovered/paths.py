from collections import defaultdict
exec(open('/home/claude/timetravel.py').read().split('# --- identities')[0])
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
sources={src(c) for c in cells}
E=defaultdict(set)
for c in cells:
    if tgt(c) in sources: E[src(c)].add(tgt(c))
objs=sorted(sources)
# transitive closure
reach={A:set() for A in objs}
for A in objs:
    st=[A]; seen=set()
    while st:
        u=st.pop()
        for v in E.get(u,()):
            if v not in seen: seen.add(v); st.append(v)
    reach[A]=seen
tot=len(objs)**2
hit=sum(len(reach[A]) for A in objs)
print(f"objects {len(objs)}   ordered pairs {tot}   connected by a composable path {hit}  = {100*hit/tot:.1f}%")
for k in sorted({A[2] for A in objs}):
    grp=[A for A in objs if A[2]==k]
    print(f"  from k={k} ({len(grp)} objects): reach {len(reach[grp[0]])} of {len(objs)} objects")

# quotient of the reachability preorder
comp={}
for A in objs:
    comp[A]=frozenset(B for B in objs if B in reach[A] and A in reach[B])
classes=sorted(set(comp.values()), key=lambda c: -min(A[2] for A in c))
print(f"\nequivalence classes of mutual reachability: {len(classes)} "
      f"(sizes {[len(c) for c in classes]}, occupancies {[sorted({A[2] for A in c}) for c in classes]})")
# is the quotient a chain?
chain=all(classes[i+1] <= set().union(*[reach[A] for A in classes[i]]) for i in range(len(classes)-1))
print(f"quotient is a total order (a chain): {chain}   -> order dimension of the time order = 1")

# cell-level: ordered cell pairs joined by a composable path
cp=0
for a in cells:
    cp+=sum(1 for b in cells if src(b) in reach[tgt(a)] or src(b)==tgt(a))
print(f"\nordered cell pairs (a,b) with a path a -> ... -> b: {cp:,} of {len(cells)**2:,} "
      f"= {100*cp/len(cells)**2:.1f}%")

# lattice order, by contrast: down-sets
le=lambda x,y: all(p<=q for p,q in zip(x,y))
lat=sum(1 for a in cells for b in cells if le(a,b))
print(f"ordered cell pairs comparable in the LATTICE order: {lat:,} = {100*lat/len(cells)**2:.1f}%")