import sys, math, random; sys.path.insert(0,"/home/claude/work")
import ground as G
from itertools import product, permutations, combinations
LS="spdfg"; cap=lambda l:2*(2*l+1)
def cell(Z):
    """the walk's step as Λ's own cell: a SOURCE subshell, a TARGET subshell,
    and q moving between them. Where no subshell empties, the source is the
    notional outside — recorded as such, not omitted."""
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    tgt=got[0]
    lost=[k for k in pr if pr[k]>cu.get(k,0)]
    src=lost[0] if lost else None
    q=cu[tgt]-pr.get(tgt,0)
    return dict(Z=Z, e=tgt[0], f=tgt[1], g=cu[tgt],
                n=(src[0] if src else 0), l=(src[1] if src else 0),
                k=(pr.get(src,0) if src else 0), q=q, outside=(src is None))
S=[c for c in (cell(Z) for Z in range(3,109)) if c]
print(f"  A5c — THE WALK'S CELL AS A TRANSITION.  {len(S)} steps\n")
print(f"      with a real source subshell : {sum(1 for c in S if not c['outside'])}")
print(f"      from the outside            : {sum(1 for c in S if c['outside'])}")
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
def minE(cells,cap_=20000):
    d=len(next(iter(cells)))
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(d)]
    cs={tuple(rel[i][c[i]] for i in range(d)) for c in cells}
    ax=[len({c[i] for c in cs}) for i in range(d)]
    b=None;kk=0
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(d)) for x in cs}
        E=len(opR(m,d))-len(m)
        b=E if b is None else min(b,E)
        if b==0: return 0,len(cs),ax
        kk+=1
        if kk>cap_: break
    return b,len(cs),ax
print(f"\n  Λ's OWN ALPHABET for a transition: source (n,ℓ,k) · q · target (e,f,g)\n")
print(f"  {'axes':<30}{'cells':>6}{'box':>7}{'E':>4}")
for lab,keys in (("target only (e,f,g)",("e","f","g")),
                 ("source only (n,ℓ,k)",("n","l","k")),
                 ("(e,f,q)",("e","f","q")),
                 ("(n,ℓ,q)  source + q",("n","l","q")),
                 ("(f,q,l)  both ℓ's + q",("f","q","l")),
                 ("(e,f,g,q)",("e","f","g","q")),
                 ("(n,ℓ,q,f)",("n","l","q","f")),
                 ("(n,ℓ,k,q,e,f,g) — full Λ",("n","l","k","q","e","f","g"))):
    cells={tuple(c[x] for x in keys) for c in S}
    E,n,ax=minE(cells)
    box=1
    for a in ax: box*=a
    print(f"  {lab:<30}{n:>6}{box:>7}{E:>4}")