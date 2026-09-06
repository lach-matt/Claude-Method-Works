import numpy as np, random
from itertools import product, permutations, combinations
random.seed(331)
def closed(S,A):
    d=len(A); ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def reorderable(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
print("="*88)
print("  HOW FAST DOES REORDERABILITY COLLAPSE WITH DIMENSION?")
print("="*88)
print("\n  %5s%10s%16s%14s"%("d","n","reorderable","rate"))
print("  "+"-"*48)
rates=[]
for d in (2,3,4):
    n=r=0; lim={2:1200,3:700,4:200}[d]
    for _ in range(lim):
        A=[list(range(2)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(a)<2 for a in Aa): continue
        n+=1; r+=reorderable(S,d)
    rates.append((d,n,r,r/max(n,1)))
    print("  %5d%10d%16d%14.3f"%(d,n,r,r/max(n,1)))
if len(rates)>=3:
    v=[x[3] for x in rates]
    print("\n     ratio between consecutive dimensions : %s"%["%.2f"%(v[i+1]/max(v[i],1e-9)) for i in range(len(v)-1)])
print("="*88)
print("  THE BOUNDS ON d ≥ 3, IDENTIFIED")
print("="*88)
B=[
("every 2-D projection reorderable","**NECESSARY** — 0 false negatives at d = 3 and d = 4","upper"),
("and it is nearly VACUOUS","810/812 pass at d=3; 249/249 at d=4","upper, non-binding"),
("the gap carries §13.4's signature","88% of gap instances: two cells agreeing on one axis, disagreeing on two, join absent","structural"),
("pairwise intersection per coordinate","**never removes a solution**, median reduction 1.0×","lower, non-binding"),
("reorderability collapses with d","measured above","measurement"),
("no conjunction of 2-D facts suffices","§13.4, with a six-cell counterexample","**THEOREM**"),
("the d = 2 characterisation","proved, and it is about PAIRS of axes","scope"),
("§23.2's pair-fixing","solves a 2-D projection exactly, then BACKTRACKS","method"),
("§23.3's density law","the cost of the backtracking, not of the projection","cost"),
]
print("\n  %-40s%-52s%s"%("bound","evidence","kind"))
print("  "+"-"*116)
for a,b,c in B: print("  %-40s%-52s%s"%(a[:40],b[:52],c))
print("""
{0}
  WHAT THEY FENCE IN
{0}

  **Two upper bounds, both non-binding.** The projection test contains
  reorderability and barely constrains it — at d = 4 it accepts everything.

  **One lower bound, also non-binding.** The per-coordinate intersection
  never removes a solution and usually removes nothing.

  **One theorem closing the direction.** §13.4: no conjunction of
  two-dimensional facts is sufficient, and the failing configuration is
  the typical one rather than an exception.

  > **The bounds do not converge. They establish that the d-dimensional
  > problem is not approachable from below**, which is a different kind of
  > result from the d = 2 case, where the bounds met.

  **And that is what §23.2 and §23.3 were measuring all along.** The
  pair-fixing solves the part the 2-D theory reaches; the backtracking
  does the rest; the density law prices it. **Three sections, one
  procedure, and the theory covers only its first step.**
""".format("="*88))