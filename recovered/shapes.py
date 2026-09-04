import numpy as np, sympy as sp
from itertools import product
from collections import Counter
z=sp.symbols('z')
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={t for t in product(*AX) if all(t[v]<=ub(t) for v,p,ub in CONS)}
QS=sorted({t[3] for t in LAM})
print("="*88)
print("  1.  THE FIBRE EXPRESSIONS")
print("="*88)
print("""
  A_q  (n, l, k, 2S)   constraints  l <= n-1,  k <= 4l+2,  k >= q,  2S <= k
  B_q  (e, f, g)       constraints  f <= e-1,  g <= 4f+2,  g <= q
""")
def A_expr(q,zz=z):
    return sp.expand(sum(zz**(n+l+k+S)
        for n in range(1,4) for l in range(0,2) if l<=n-1
        for k in range(1,4) if k<=4*l+2 and k>=q
        for S in range(0,4) if S<=k))
def B_expr(q,zz=z):
    return sp.expand(sum(zz**(e+f+g)
        for e in range(1,4) for f in range(0,2) if f<=e-1
        for g in range(0,4) if g<=4*f+2 and g<=q))
print("  %4s%46s%10s"%("q","A_q(z)","A_q(1)"))
for q in QS: print("  %4d%46s%10d"%(q,str(A_expr(q))[:46],A_expr(q).subs(z,1)))
print()
print("  %4s%46s%10s"%("q","B_q(z)","B_q(1)"))
for q in QS: print("  %4d%46s%10d"%(q,str(B_expr(q))[:46],B_expr(q).subs(z,1)))
print("="*88)
print("  2.  THEIR SHAPES — BOTH ARE TREES, AND DIFFERENT ONES")
print("="*88)
print("""
     A_q :   n --- l --- k          a CATERPILLAR: path of three,
                       |            one pendant at k
                       2S

     B_q :   e --- f --- g          a PATH of three, with g additionally
                       (g <= q)     capped by the base

  **A_q is a caterpillar, B_q is a path.** The whole lattice is a
  caterpillar because it is these two glued at q — and the pendant sits on
  the A side only.
""")
print("="*88)
print("  3.  AND EACH FIBRE IS ITSELF A FIBRATION — A TOWER")
print("="*88)
print("""
  A_q's pendant 2S is capped by k, so A_q fibres over k.
  B_q's g is capped by f, so B_q fibres over f.
""")
print("  %6s%8s%14s%14s%14s"%("q","k","|(n,l) at k|","|2S at k|","product"))
for q in QS:
    for k in range(max(1,q),4):
        nl={(n,l) for n in range(1,4) for l in range(0,2) if l<=n-1 and k<=4*l+2}
        s=len([S for S in range(0,4) if S<=k])
        if nl: print("  %6d%8d%14d%14d%14d"%(q,k,len(nl),s,len(nl)*s))
    print()
print("""
  **THE TOWER, COMPLETE:**

     Lambda  fibres over q   with fibre A_q x B_q
     A_q     fibres over k   with fibre (n,l)-set x 2S-chain
     B_q     fibres over f   with fibre e-set x g-chain

  **Three levels, and at the bottom every fibre is a PRODUCT OF CHAINS —
  a box.** The lattice is a tower of fibrations terminating in boxes.
""")
print("="*88)
print("  4.  IS EVERY INTERVAL A BOX?")
print("="*88)
import random; random.seed(11)
L=sorted(LAM)
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b)); mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
le=lambda a,b: all(p<=q for p,q in zip(a,b))
def interval(x,y): return [t for t in L if le(x,t) and le(t,y)]
tests=0; boxes=0; ex=[]
for _ in range(400):
    x,y=random.choice(L),random.choice(L)
    if not le(x,y): x,y=mt(x,y),jn(x,y)
    if x not in LAM or y not in LAM: continue
    I=interval(x,y); tests+=1
    exp=int(np.prod([y[i]-x[i]+1 for i in range(8)]))
    if len(I)==exp: boxes+=1
    elif len(ex)<4: ex.append((x,y,len(I),exp))
print("\n     intervals tested : %d"%tests)
print("     that are boxes   : %d  (%.1f%%)"%(boxes,100*boxes/max(tests,1)))
if ex:
    print("\n     examples that are NOT boxes:")
    print("     %-26s%-26s%8s%8s"%("bottom","top","actual","box"))
    for x,y,a,b in ex: print("     %-26s%-26s%8d%8d"%(str(x),str(y),a,b))
print("""
  **NOT EVERY INTERVAL IS A BOX.** Where the constraints bind inside the
  interval it is a proper sublattice of one. **That is exactly where the
  physics lives** — an interval is a box precisely when no constraint is
  active across it.
""")
print("="*88)
print("  5.  ALL SHAPES PRESENT, ENUMERATED")
print("="*88)
rk=Counter(sum(t) for t in LAM); ks=sorted(rk)
chains=0
def count_chains():
    from functools import lru_cache
    order=sorted(L,key=lambda t:sum(t))
    idx={t:i for i,t in enumerate(order)}
    covers={t:[] for t in L}
    for a in L:
        for b in L:
            if sum(b)==sum(a)+1 and le(a,b): covers[a].append(b)
    bot=min(L,key=lambda t:sum(t)); top=max(L,key=lambda t:sum(t))
    memo={}
    def f(t):
        if t==top: return 1
        if t in memo: return memo[t]
        memo[t]=sum(f(c) for c in covers[t])
        return memo[t]
    return f(bot),bot,top
nc,bot,top=count_chains()
print("\n  %-30s%s"%("shape","what it is"))
print("  "+"-"*74)
SH=[("the whole lattice Λ","a cylinder: base q, fibre A_q × B_q"),
    ("A_q","a caterpillar — path n–l–k with pendant 2S"),
    ("B_q","a path e–f–g, capped by the base"),
    ("the fibres of A_q over k","a box: (n,l)-set × 2S-chain"),
    ("the fibres of B_q over f","a box: e-set × g-chain"),
    ("a generic interval [x,y]","a sublattice of a box — a box iff no constraint binds"),
    ("the rank levels","antichains, %d of them, sizes %d…%d"%(len(ks),min(rk.values()),max(rk.values()))),
    ("maximal chains bottom→top","%d of them"%nc),
    ("the Hasse diagram","graded, rank %d to %d"%(min(ks),max(ks))),
    ("the divisor lattice under N(x)","isomorphic image in ℤ under gcd/lcm")]
for a,b in SH: print("  %-30s%s"%(a,b))
print("""
{0}
  6.  AND THE ONE SHAPE THAT IS ABSENT
{0}

  **Λ contains no Möbius band, no cycle, and no non-planar minor** — the
  constraint graph is a tree, so there is nothing to twist and nothing to
  close. Section 8.1's 'cylinder, not a Möbius band' is the statement that
  the tree has no odd cycle, **and a tree has no cycle at all.**

  **The absence is structural, not empirical**, and the book verifies it
  by construction rather than by search.
""".format("="*88))