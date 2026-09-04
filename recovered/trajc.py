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
def anyzero(cells,axes,cap=3000):
    k=0
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        if len(opR(cs,len(axes)))-len(cs)==0: return True
        k+=1
        if k>cap: break
    return False
print("  CONTINGENCY (R 1383) — could these E = 0 results have failed?\n")
print(f"  {'grid':>12}{'cells':>7}{'trials':>8}{'% that REFUSE':>15}   verdict")
for axes,n,lab in (([4,4,2],19,"nodes x L x q"),
                   ([4,4,2],11,"nodes x floor x q"),
                   ([4,2,2],12,"L x q x sides")):
    pool=[c for c in product(*[range(a) for a in axes])]
    if n>len(pool): 
        print(f"  {str(axes):>12}{n:>7}   n exceeds box"); continue
    pos=tot=0
    for s in range(120):
        c=set(random.Random(s).sample(pool,n)); tot+=1
        if not anyzero(c,axes): pos+=1
    pct=100*pos/tot
    v = "EARNED" if pct>=25 else ("WEAK" if pct>=10 else "FORCED — no information")
    print(f"  {str(axes):>12}{n:>7}{tot:>8}{pct:>14.0f}%   {v}   [{lab}]")