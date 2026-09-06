import sys, math, random
sys.path.insert(0,"/home/claude/work")
import ground as G
from itertools import product, permutations
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def step(Z):
    if Z<3 or Z>108: return None
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    return gn,gl,gn-gl-1,min(cu[(gn,gl)]-pr.get((gn,gl),0),2)
S=[step(Z) for Z in range(3,109)]; S=[s for s in S if s]
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
def minE(cells,axes,cap_=6000):
    b=None;k=0
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        b=E if b is None else min(b,E)
        if b==0: return 0
        k+=1
        if k>cap_: break
    return b
def rep(lab,cells):
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(3)]
    cs={tuple(rel[i][c[i]] for i in range(3)) for c in cells}
    axes=[len({c[i] for c in cs}) for i in range(3)]
    E=minE(cs,axes)
    print(f"  {lab:<28} cells {len(cs):>3} · box {axes[0]*axes[1]*axes[2]:>3} · E = {E}")
    return E,cs,axes
print("  IS nodes A RE-COORDINATISATION OR AN ADJUNCTION?\n")
print("  A.derived forbids ADJOINING a derived coordinate to repair closure.")
print("  A.erel permits RE-COORDINATISING: E = 0 is a statement about coordinates.\n")
E1,_,_ = rep("(n, ℓ, q)   — Λ's letters", {(a,b,d) for a,b,c,d in S})
E2,c2,ax2 = rep("(nodes, ℓ, q) — replaced", {(c,b,d) for a,b,c,d in S})
E3,_,_ = rep("(n, nodes, ℓ) — ADJOINED", {(a,c,b) for a,b,c,d in S})
print()
if E1==0 and E2==0:
    print("  BOTH close: nodes is a relabelling and adds nothing. Λ_traj is a")
    print("  PROJECTION of Λ, not a new index. A.derived is not engaged.")
elif E1>0 and E2==0:
    print("  ONLY the replaced form closes. That is RE-COORDINATISATION repairing")
    print("  closure — A.erel's statement, not A.derived's, since nothing was")
    print("  ADJOINED: n was REPLACED by n−ℓ−1, same information, different order.")
print("\n  and the adjunction test proper — does adding nodes to (n, ℓ) help?")
base={(a,b) for a,b,c,d in S}
def E2d(cells):
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(2)]
    cs={tuple(rel[i][c[i]] for i in range(2)) for c in cells}
    ax=[len({c[i] for c in cs}) for i in range(2)]
    b=None
    for p in product(*[permutations(range(a)) for a in ax]):
        s={tuple(p[i].index(x[i]) for i in range(2)) for x in cs}
        E=len(opR(s,2))-len(s)
        b=E if b is None else min(b,E)
    return b,len(cs),ax
e,n,ax=E2d(base); print(f"      (n, ℓ)          cells {n} · box {ax[0]*ax[1]} · E = {e}")
e,n,ax=E2d({(a,b) for a,b,c,d in S})   # same
E3b,_,_ = rep("(n, ℓ, nodes) adjoined", {(a,b,c) for a,b,c,d in S})
print(f"\n      A.derived: the box grows by the new coordinate's value count while")
print(f"      |X| is fixed, so E cannot fall. Check: does it?")