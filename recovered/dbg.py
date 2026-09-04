from itertools import product
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
def alphabet(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
A=alphabet(PT,2)
sup={a:frozenset(y for (x,y) in PT if x==a) for a in A[0]}
occ={b:sum(1 for a in A[0] if b in sup[a]) for b in A[1]}
o0=sorted(A[0],key=lambda a:(-len(sup[a]),a))
o1=sorted(A[1],key=lambda b:(-occ[b],b))
print("row order (periods, desc by support):",o0)
print("col order (groups, desc by occupancy):",o1)
i0={v:i for i,v in enumerate(o0)}; i1={v:i for i,v in enumerate(o1)}
T={(i0[x],i1[y]) for (x,y) in PT}
print("\nsupports in the new order:")
for a in sorted({t[0] for t in T}):
    s=sorted(t[1] for t in T if t[0]==a)
    init = s==list(range(len(s)))
    print("   row %d : %2d cols, initial segment: %s   %s"%(a,len(s),init,s[:8]))
def is_downset(T):
    for x in T:
        for y in product(*[range(v+1) for v in x]):
            if y not in T: return False,x,y
    return True,None,None
ok,x,y=is_downset(T)
print("\n  is a downset:",ok)
if not ok: print("  first violation: %s in T but %s is not"%(x,y))