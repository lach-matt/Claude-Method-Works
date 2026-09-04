from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
d=8; X=L8; S=set(X)

def Rset(Y,d):
    A=[sorted({y[i] for y in Y}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for v in A[j]:
                c=[y[i] for y in Y if y[j]<=v]
                m[v]=max(c) if c else None
            phi[(i,j)]=m
    from itertools import product as pr
    out=[]
    for y in pr(*A):
        ok=True
        for i in range(d):
            for j in range(d):
                if i==j: continue
                b=phi[(i,j)][y[j]]
                if b is None or y[i]>b: ok=False;break
            if not ok: break
        if ok: out.append(y)
    return set(out)

# fast screen: which single deletions can possibly change R?
valcount=[defaultdict(int) for _ in range(d)]
for x in X:
    for i in range(d): valcount[i][x[i]]+=1
crit=set()
for x in X:
    for i in range(d):
        if valcount[i][x[i]]==1: crit.add(x)
A=[sorted({y[i] for y in X}) for i in range(d)]
for i in range(d):
    for j in range(d):
        if i==j: continue
        for v in A[j]:
            sub=[y for y in X if y[j]<=v]
            m=max(y[i] for y in sub)
            arg=[y for y in sub if y[i]==m]
            if len(arg)==1: crit.add(arg[0])
print(f"cells whose removal could alter a value set or an envelope: {len(crit)} of {len(X)}")

repaired=0; lost=[]
for x in X:
    if x not in crit:
        repaired+=1; continue
    if x in Rset(S-{x}, d): repaired+=1
    else: lost.append(x)
print(f"EXHAUSTIVE single-deletion repair on L8: {repaired} of {len(X)} restored, "
      f"{len(lost)} unrecoverable")
if lost: print("  unrecoverable:", lost[:10])

# --- composition side, on L9 ---
exec(open('/home/claude/timetravel.py').read().split('# --- identities')[0])
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
by_src=defaultdict(list)
for c in cells: by_src[src(c)].append(c)
comp=lambda a,b:(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8])
decomposable=set()
for a in cells:
    for b in by_src.get(tgt(a),()):
        z=comp(a,b)
        if z!=a and z!=b: decomposable.add(z)
print(f"\nL9 cells expressible as a composite of two OTHER cells: "
      f"{len(decomposable):,} of {len(cells):,} = {100*len(decomposable)/len(cells):.1f}%")
gen=[c for c in cells if c not in decomposable]
print(f"composition-irreducible (generators): {len(gen):,}")
from collections import Counter
print("  generators by transfer q:", dict(sorted(Counter(g[3] for g in gen).items())))
print("  generators by source occupancy k:", dict(sorted(Counter(g[2] for g in gen).items())))