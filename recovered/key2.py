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
def minE(cells,axes,cap=4000):
    best=None; k=0
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        best=E if best is None else min(best,E)
        if best==0: return 0
        k+=1
        if k>cap: break
    return best
print(f"{'cells':>6}{'grid':>12}{'trials':>8}{'minE>0':>8}")
for dims,n in [([4,4,2],4),([5,4,3],5),([6,4,3],6),([7,5,3],7)]:
    got=tot=0
    for s in range(60):
        r=random.Random(s); rows=r.sample(range(dims[0]),n)
        c={(rows[i],)+tuple(r.randrange(d) for d in dims[1:]) for i in range(n)}
        if len(c)!=n: continue
        tot+=1
        if minE(c,dims)>0: got+=1
    print(f"{n:>6}{str(dims):>12}{tot:>8}{got:>8}")