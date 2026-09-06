import numpy as np, random
from itertools import product
random.seed(3)
CAP=lambda l:2*(2*l+1)
LAM=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(CAP(l),3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): LAM.add((n,l,k,q,e,f,g,S2))
d=8; LL=sorted(LAM); arr=np.array(LL,dtype=np.int32)
AX=[sorted(set(arr[:,i].tolist())) for i in range(d)]
grid=np.array(list(product(*AX)),dtype=np.int32)
print("="*84)
print("  CORRECTED: THE POLYHEDRON IS THE INTERSECTION OF *ALL* VALID BOUNDS")
print("="*84)
print("""
  Previous attempt chose ONE (a,b) per coordinate pair by least slack.
  That is not the tightest polyhedron of the restricted form -- every
  valid (a,b) is a genuine facet, and the polyhedron is their INTERSECTION.
""")
def cons_of(A,amax=6):
    C=[]
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(0,amax+1):
                b=int((A[:,i]-a*A[:,j]).max())
                C.append((i,j,a,b))
    return C
def sel(C):
    m=np.ones(len(grid),dtype=bool)
    for i,j,a,b in C: m &= grid[:,i] <= a*grid[:,j]+b
    return m
m0=sel(cons_of(arr))
P0={tuple(int(v) for v in g) for g in grid[m0]}
print("  %-56s%12s%9s"%("statement","computed","verdict"))
print("  "+"-"*78)
def T(n,g,w=True):
    print("  %-56s%12s%9s"%(n,str(g)[:12],"TRUE" if g==w else "FALSE")); return g==w
r=[T("P(Lambda) cap Z^8 = Lambda   [fixed point]",P0==LAM)]
print("     |P(Lambda)| = %d   |Lambda| = %d"%(len(P0),len(LAM)))
print("\n  DELETE A CELL — 30 TRIALS\n")
fail=0; failed=[]
for _ in range(30):
    x=random.choice(LL)
    sub=np.array([z for z in LL if z!=x],dtype=np.int32)
    S={tuple(int(v) for v in g) for g in grid[sel(cons_of(sub))]}
    if S!=LAM: fail+=1; failed.append((x,len(S)))
print("     failed to restore : %d of 30"%fail)
if failed:
    for x,n in failed[:5]: print("        %s -> %d cells"%(str(x),n))
r.append(T("monotone polyhedron restores EVERY deletion",fail==0))
print("\n  ADD AN INADMISSIBLE CELL — 20 TRIALS\n")
outside=[tuple(int(v) for v in g) for g in grid[~m0]]
grew=0
for _ in range(20):
    y=random.choice(outside)
    sup=np.array(LL+[y],dtype=np.int32)
    if sel(cons_of(sup)).sum()>len(LAM): grew+=1
print("     absorbed (set grew) : %d of 20"%grew)
r.append(T("monotone polyhedron absorbs EVERY addition",grew==20))
print("""
{0}
  VERDICT
{0}
""".format("="*84))
if all(r):
    print("""  **THE REFUTATION IS CONFIRMED.**

     convex hull          fails on deletions   -- unrestricted facets;
                          a vertex is a sole witness
     monotone polyhedron  restores every deletion, absorbs every addition

  The geometric language HAS the property. My operator did not match the
  lattice's own facet form, and a mismatched operator is not a
  counterexample -- it is a mistranslation.

  **SO THE ASYMMETRY IS ESTABLISHED IN ALL FIVE LANGUAGES.**
  CORRECTION 73: 'deletion-repair fails in geometry'.
  CORRECTION 72 WITHDRAWN.""")
else:
    print("""  **NOT YET ESTABLISHED.** %d of %d tests true. The restricted-facet
  polyhedron does not reproduce Lambda exactly, so the correct geometric
  operator is still not in hand -- the linear two-variable family may be
  too coarse where the true bound is a STEP function (min(q,4f+2)).

  That is itself the answer to where the mismatch lies, and it is
  testable: replace the linear facet family by the monotone STAIRCASE
  family and the fixed point should return."""%(sum(r),len(r)))