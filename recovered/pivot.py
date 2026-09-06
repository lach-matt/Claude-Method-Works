from itertools import product, permutations
from collections import Counter
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}

SEAT=["nucleus","core","subvalence","valence"]; KIND=["counting","coupling"]
ZC=["within one element","across elements"]
LAD=["isoelectronic","the walk","ionisation","isotopic","isotonic","isobaric",
     "Rydberg series","l-ladder","term ladder","outer-j","parent-term","isomeric"]
s=[3,3,2,0,0,0,3,3,3,3,1,0]; k=[0,0,0,0,0,0,0,0,1,1,1,0]; z=[1,1,0,0,1,1,0,0,0,0,0,0]
occ={}
for i,n in enumerate(LAD): occ.setdefault((s[i],k[i],z[i]),[]).append(n)
cells=set(occ)

print("THE SEVEN CELLS")
for c in sorted(cells):
    print(f"   ({SEAT[c[0]]:<11} {KIND[c[1]]:<9} {ZC[c[2]]:<18}) : {', '.join(occ[c])}")

mod=[Counter(c[i] for c in cells).most_common(1)[0][0] for i in range(3)]
print(f"\nmodal value per axis : {SEAT[mod[0]]} | {KIND[mod[1]]} | {ZC[mod[2]]}")
pivot=tuple(mod)
print(f"cell at the modal value of ALL THREE axes : "
      f"{'EXISTS' if pivot in cells else 'absent'}  -> {occ.get(pivot)}")

# how many cells does each cell share a value with, per axis?  the pivot should
# be the one adjacent to every other along at least one axis.
print(f"\n{'cell':<46}{'shares an axis value with':>26}")
for c in sorted(cells):
    n=sum(1 for d in cells if d!=c and any(c[i]==d[i] for i in range(3)))
    print(f"   ({SEAT[c[0]]:<11} {KIND[c[1]]:<9} {ZC[c[2]]:<18}){n:>20} of 6")

# now: shuffle with the pivot FIXED at the corner R works from.
def minE_fixed(cells,axes,pivot,corner):
    best=None;arg=None
    for p in product(*[permutations(range(a)) for a in axes]):
        if tuple(p[i].index(pivot[i]) for i in range(3))!=corner: continue
        cs={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
        E=len(opR(cs,3))-len(cs)
        if best is None or E<best: best,arg=E,p
    return best,arg
axes=[4,2,2]
for corner,label in (((0,0,0),"the (<=,<=) origin"),((3,1,1),"the far corner")):
    E,p=minE_fixed(cells,axes,pivot,corner)
    print(f"\npivot pinned at {label}: min E = {E}")
    if E is not None and p:
        inv=[{p[i].index(v):v for v in range(axes[i])} for i in range(3)]
        cs={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
        extra=opR(cs,3)-cs
        for x in sorted(extra):
            a,b,c=[inv[i][x[i]] for i in range(3)]
            print(f"    defect: ({SEAT[a]}, {KIND[b]}, {ZC[c]})")