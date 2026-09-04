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
def anyzero(cells,ax,cap=3000):
    k=0
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(len(ax))) for x in cells}
        if len(opR(m,len(ax)))-len(m)==0: return True
        k+=1
        if k>cap: break
    return False
print("  CONTINGENCY — could a 6- or 7-cell set on these grids have refused?\n")
print(f"  {'grid':>12}{'cells':>7}{'trials':>8}{'% refuse':>10}   verdict")
for ax,n,lab in (([3,2,5],7,"ceil x q x srcl"),
                 ([3,2,4],6,"ceil x q x srco"),
                 ([2,2,5],7,"sides x q x srcl"),
                 ([2,4,4],5,"q x srco x srcd"),
                 ([4,4,2],24,"n x l x q  (the parent)")):
    pool=[c for c in product(*[range(a) for a in ax])]
    if n>len(pool): print(f"  {str(ax):>12}{n:>7}   n exceeds box"); continue
    pos=tot=0
    for s in range(150):
        c=set(random.Random(s).sample(pool,n)); tot+=1
        if not anyzero(c,ax): pos+=1
    pct=100*pos/tot
    v="EARNED" if pct>=25 else ("WEAK" if pct>=10 else "FORCED — carries no information")
    print(f"  {str(ax):>12}{n:>7}{tot:>8}{pct:>9.0f}%   {v}   [{lab}]")