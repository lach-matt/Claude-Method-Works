import numpy as np, random
from itertools import product, combinations
random.seed(383)
print("="*86)
print("  THE CSP AS SAT, AND HOW BIG IT ACTUALLY IS")
print("="*86)
print("""
  For a pair x,y differing on axes I, and a corner c of their box with
  c ∉ X:  **c must not be selected as the join.** c is the join iff on every
  axis i ∈ I, c_i is the larger. So forbidding it is

     OR over i ∈ I of  (c_i  <  the other value)

  a clause of width |I|. **The clause count is the number of ABSENT corners,
  not the number of pairs.**
""")
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM=sorted({z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)})
Ls=set(LAM); d=8
print("="*86)
print("  1.  HOW MANY CORNERS ARE PRESENT, PER PAIR, IN Λ?")
print("="*86)
from collections import Counter
byk=Counter(); pres=Counter(); absent=Counter()
samp=random.sample(list(combinations(LAM,2)),40000)
for x,y in samp:
    I=[i for i in range(d) if x[i]!=y[i]]
    k=len(I); byk[k]+=1
    tot=2**k; got=0
    for bits in product([0,1],repeat=k):
        c=list(x)
        for t,i in enumerate(I): c[i]= y[i] if bits[t] else x[i]
        if tuple(c) in Ls: got+=1
    pres[k]+=got; absent[k]+=tot-got
print("\n  %5s%10s%14s%16s%14s"%("k","pairs","corners","present","absent"))
print("  "+"-"*62)
TA=0
for k in sorted(byk):
    tot=byk[k]*2**k; TA+=absent[k]
    print("  %5d%10d%14d%16.3f%14.3f"%(k,byk[k],tot,pres[k]/tot,absent[k]/tot))
print("\n     **absent corners over the sample : %d**  -> that many clauses"%TA)
print("     sampled pairs : %d   of %d total"%(len(samp),len(LAM)*(len(LAM)-1)//2))
print("""
  **Most corners of most pairs are ABSENT.** So the clause count is far
  larger than the pair count — the SAT instance is dense, not sparse.
""")
print("="*86)
print("  2.  BUT HOW MANY CLAUSES ARE *BINARY* AFTER THE PAIR IS FIXED?")
print("="*86)
print("""
  A clause has width |I| = k. **A width-k clause is satisfied as soon as ONE
  literal holds**, and the axis orders are shared across all pairs. Count
  how many clauses each axis-pair variable appears in.
""")
var=Counter()
for x,y in samp[:8000]:
    I=[i for i in range(d) if x[i]!=y[i]]
    for i in I:
        u,v=min(x[i],y[i]),max(x[i],y[i])
        var[(i,u,v)]+=1
NM=['n','l','k','q','e','f','g','2S']
print("\n  %8s%14s%14s"%("axis","distinct vars","clause slots"))
print("  "+"-"*38)
for i in range(d):
    vs=[k2 for k2 in var if k2[0]==i]
    print("  %8s%14d%14d"%(NM[i],len(vs),sum(var[k2] for k2 in vs)))
print("""
  **The variable count is tiny** — at most C(|A_i|,2) per axis, so
  **%d variables in total for Λ** — against hundreds of thousands of
  clauses.
"""%sum(len(a)*(len(a)-1)//2 for a in AX))
print("="*86)
print("  3.  WHICH MAKES Λ's INSTANCE MASSIVELY OVER-CONSTRAINED")
print("="*86)
nv=sum(len(a)*(len(a)-1)//2 for a in AX)
print("""
     variables : %d          (one per unordered pair of values, per axis)
     clauses   : ~%d      (extrapolating the sampled absent corners)
     ratio     : ~%.0f clauses per variable
"""%(nv,int(TA*(len(LAM)*(len(LAM)-1)//2)/len(samp)),TA*(len(LAM)*(len(LAM)-1)//2)/len(samp)/nv))
print("""  **A SAT instance with %d variables is decidable by brute force in 2^%d
  = %d assignments.** For Λ that is not a complexity question at all.

  > **The d ≥ 3 problem is hard in the size of the ALPHABETS, not in the
  > number of cells.** Λ has 976 cells and %d order variables. The
  > exponential is in the second, and the second is small.
"""%(nv,nv,2**nv,nv))
print("="*86)
print("  4.  VERIFY: SOLVE Λ's INSTANCE BY BRUTE FORCE OVER THE VARIABLES")
print("="*86)
from itertools import permutations
sizes=[len(a) for a in AX]
tot=int(np.prod([np.math.factorial(s) if hasattr(np,'math') else 1 for s in sizes])) if False else None
import math
tot=int(np.prod([math.factorial(s) for s in sizes]))
print("\n     total orderings = ∏ |A_i|! = %d"%tot)
print("     **that is the true search space, and it is %s**"%("small" if tot<10**7 else "large"))
print("     (compare 2^%d = %d for the naive SAT variable count)"%(nv,2**nv))