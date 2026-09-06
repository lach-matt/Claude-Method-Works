import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
from itertools import product, permutations
LS="spdfg"; cap=lambda l:2*(2*l+1)
def cell(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    t=got[0]; lost=[k for k in pr if pr[k]>cu.get(k,0)]
    src=lost[0] if lost else None
    return dict(e=t[0],f=t[1],g=cu[t],
                n=(src[0] if src else 0),l=(src[1] if src else 0),
                k=(pr.get(src,0) if src else 0),q=cu[t]-pr.get(t,0))
S=[c for c in (cell(Z) for Z in range(3,109)) if c]
COMBOS=[("target only (e,f,g)",("e","f","g")),
        ("source only (n,ℓ,k)",("n","l","k")),
        ("(e,f,q)",("e","f","q")),
        ("(n,ℓ,q)",("n","l","q")),
        ("(f,q,ℓ) both ℓ's + q",("f","q","l")),
        ("(e,f,g,q)",("e","f","g","q")),
        ("(n,ℓ,q,f)",("n","l","q","f")),
        ("(e,f,q,ℓ)",("e","f","q","l"))]
print("  BOX SIZES FIRST — opR materialises the ambient product.\n")
print(f"  {'axes':<26}{'cells':>6}{'rungs':>18}{'box':>9}")
runnable=[]
for lab,keys in COMBOS:
    cells={tuple(c[x] for x in keys) for c in S}
    ax=[len({c[i] for c in cells}) for i in range(len(keys))]
    box=1
    for a in ax: box*=a
    print(f"  {lab:<26}{len(cells):>6}{str(ax):>18}{box:>9}")
    if box<=20000: runnable.append((lab,keys,cells,ax,box))
print(f"\n  running the {len(runnable)} with box <= 20000\n")
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
print(f"  {'axes':<26}{'cells':>6}{'box':>7}{'E':>5}")
for lab,keys,cells,ax,box in runnable:
    d=len(keys)
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(d)]
    cs={tuple(rel[i][c[i]] for i in range(d)) for c in cells}
    b=None; kk=0
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(d)) for x in cs}
        E=len(opR(m,d))-len(m)
        b=E if b is None else min(b,E)
        if b==0: break
        kk+=1
        if kk>2000: break
    print(f"  {lab:<26}{len(cs):>6}{box:>7}{b:>5}")