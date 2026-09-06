import random
from itertools import product, permutations, combinations
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
def minE(cells,axes,stop0=True):
    b=None;arg=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        if b is None or E<b: b,arg=E,p
        if b==0 and stop0: return 0,arg
    return b,arg

AX={
 "seat":   (["nucleus","core","subvalence","valence"],[3,3,2,0,0,0,3,3,3,3,1,0]),
 "kind":   (["counting","coupling"],                  [0,0,0,0,0,0,0,0,1,1,1,0]),
 "Zcross": (["within one element","across elements"], [1,1,0,0,1,1,0,0,0,0,0,0]),
 "relation":(["Lambda","nuclide chart"],              [0,0,0,1,1,1,0,0,0,0,0,1]),
 "domain": (["all elements","a region","one species"],[0,0,0,1,1,1,2,2,2,2,2,1]),
}
print(f"{'axes':<34}{'cells':>6}{'box':>5}{'minE':>6}{'null: % able to refuse':>24}{'verdict':>12}")
for tri in combinations(AX,3):
    vals=[AX[t][0] for t in tri]; asg=[AX[t][1] for t in tri]
    cells={tuple(asg[i][k] for i in range(3)) for k in range(12)}
    axes=[len(v) for v in vals]; n=len(cells); box=axes[0]*axes[1]*axes[2]
    E,_=minE(cells,axes)
    pool=[c for c in product(*[range(a) for a in axes])]
    pos=tot=0
    for s in range(120):
        c=set(random.Random(s).sample(pool,n)); tot+=1
        if minE(c,axes)[0]>0: pos+=1
    pct=100*pos/tot
    verdict = ("EARNED" if pct>=25 else "forced") if E==0 else "DEFECT"
    print(f"{' x '.join(tri):<34}{n:>6}{box:>5}{E:>6}{pct:>22.0f}%{verdict:>12}")