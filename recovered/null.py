import random
from itertools import product, permutations
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
def minE(cells,axes):
    b=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        b=E if b is None else min(b,E)
        if b==0: return 0
    return b
# NULL MODEL: how often can a 6-cell set on a 5x3x2 grid refuse anything?
grid=[5,3,2]; pool=[c for c in product(*[range(g) for g in grid])]
pos=tot=0
for s in range(300):
    c=set(random.Random(s).sample(pool,6))
    tot+=1
    if minE(c,grid)>0: pos+=1
print(f"random 6-cell sets on a 5x3x2 grid: {pos} of {tot} ({100*pos/tot:.0f}%) have min E > 0")
print("  -> refusal is possible at six cells, so E = 0 there is a RESULT.")
# and the 4-cell null on the grid the held index actually uses
grid4=[3,3,2]; pool4=[c for c in product(*[range(g) for g in grid4])]
pos=tot=0
for s in range(300):
    c=set(random.Random(s+9000).sample(pool4,4)); tot+=1
    if minE(c,grid4)>0: pos+=1
print(f"random 4-cell sets on a 3x3x2 grid: {pos} of {tot} ({100*pos/tot:.0f}%) have min E > 0")
print("  -> refusal is IMPOSSIBLE at four cells, so E = 0 there is an ARTEFACT.")