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
s=[3,3,2,0,0,0,3,3,3,3,1,0]; k=[0,0,0,0,0,0,0,0,1,1,1,0]; z=[1,1,0,0,1,1,0,0,0,0,0,0]
cells={(s[i],k[i],z[i]) for i in range(12)}
axes=[4,2,2]
best=None; hits=Counter(); orders=[]
for p in product(*[permutations(range(a)) for a in axes]):
    cs={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
    ex=opR(cs,3)-cs; E=len(ex)
    if best is None or E<best: best=E; hits.clear(); orders=[]
    if E==best:
        inv=[{p[i].index(v):v for v in range(axes[i])} for i in range(3)]
        for x in ex: hits[tuple(inv[i][x[i]] for i in range(3))]+=1
        orders.append(p)
tot=len(orders)
print(f"minimum over all {4*2*2*  (1)} axis orderings...  min E = {best}")
print(f"orderings achieving it: {tot} of {24*2*2}")
print(f"\nthe defect cell, across every optimal ordering:")
for c,n in hits.most_common():
    print(f"   ({SEAT[c[0]]}, {KIND[c[1]]}, {ZC[c[2]]})   in {n} of {tot} optimal orderings")
p=orders[0]
print(f"\none optimal ordering:")
print(f"   seat   : {' < '.join(SEAT[i] for i in p[0])}")
print(f"   kind   : {' < '.join(KIND[i] for i in p[1])}")
print(f"   Zcross : {' < '.join(ZC[i]   for i in p[2])}")