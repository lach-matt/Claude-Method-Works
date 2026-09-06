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
def anyzero(cells,axes,cap=900):
    k=0
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        if len(opR(cs,len(axes)))-len(cs)==0: return True
        k+=1
        if k>cap: break
    return False
AX=[5,5,3]; pool=[c for c in product(*[range(a) for a in AX])]
for n in (13,14,15):
    pos=tot=0
    for s in range(40):
        c=set(random.Random(s).sample(pool,n)); tot+=1
        if not anyzero(c,AX): pos+=1
    print(f"  n={n:<3} {100*pos/tot:>3.0f}% of comparable sets REFUSE (cannot reach E=0)")