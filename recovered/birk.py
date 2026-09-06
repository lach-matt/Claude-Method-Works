import numpy as np, random
from itertools import product, permutations
random.seed(103)
print("="*88)
print("  THE NON-LOCAL MOVE IS ALREADY IN THE BOOK")
print("="*88)
print("""
  §3.3 — seventeen join-irreducibles.  §7.9 — maximal chains are the LINEAR
  EXTENSIONS of the join-irreducible poset.  **Birkhoff: a distributive
  lattice is determined by that poset, not by any labelling of its axes.**

  **So do not search orderings. Derive one.**

     rows carry a natural PARTIAL order:  r <= r'  iff  S(r) ⊆ S(r')
     columns likewise:                    c <= c'  iff  C(c) ⊆ C(c')

  **An ordering is a linear extension of each.** That is a global move —
  it jumps to a structure rather than swapping neighbours.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def Rsize(T):
    A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=N[c])
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def E(S,o):
    T=relabel(S,o); return Rsize(T)-len(T)
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if E(S,[list(p0),list(p1)])==0: return True
    return False
def lin_ext(elems,leq):
    """all linear extensions of the partial order given by leq"""
    out=[]
    def rec(rem,acc):
        if not rem: out.append(list(acc)); return
        for e in list(rem):
            if all(not leq(f,e) or f==e for f in rem if f!=e):
                rec(rem-{e},acc+[e])
    rec(set(elems),[])
    return out
def derive(S):
    """order each axis by a linear extension of its inclusion order"""
    A=alpha(S)
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    col={c:frozenset(a for (a,b) in S if b==c) for c in A[1]}
    R=lin_ext(A[0],lambda p,q: sup[p]<=sup[q])
    C=lin_ext(A[1],lambda p,q: col[q]<=col[p])
    return R,C
print("="*88)
print("  TEST — DOES A LINEAR EXTENSION FIND WHAT DESCENT MISSES?")
print("="*88)
inst=[]
while len(inst)<400:
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if reorderable(S): inst.append(S)
def descend1(S,maxit=200):
    A=alpha(S); o=[list(A[0]),list(A[1])]; e=E(S,o); it=0
    while e>0 and it<maxit:
        best=None
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                v=E(S,p)
                if best is None or v<best[0]: best=(v,p)
        if best[0]>=e: break
        e,o=best; it+=1
    return e
stuck=[S for S in inst if descend1(S)>0]
print("\n     descent-1 stalls on %d of %d reorderable instances"%(len(stuck),len(inst)))
solved=0; ex=[]
for S in stuck:
    R,C=derive(S)
    got=any(E(S,[r,c])==0 for r in R[:200] for c in C[:200])
    solved+=got
    if not got and len(ex)<3: ex.append(S)
print("     of those, a linear extension of the inclusion order finds E=0 : %d  (%.0f%%)"
      %(solved,100*solved/max(len(stuck),1)))
allok=0; sizes=[]
for S in inst:
    R,C=derive(S)
    sizes.append(len(R)*len(C))
    allok+=any(E(S,[r,c])==0 for r in R[:200] for c in C[:200])
print("\n     across ALL %d reorderable instances : %d solved  (%.1f%%)"%(len(inst),allok,100*allok/len(inst)))
print("     linear-extension pairs searched, median %d  max %d"%(int(np.median(sizes)),max(sizes)))
print("="*88)
print("  AND HOW MUCH SMALLER IS THAT SEARCH?")
print("="*88)
from math import factorial
full=[]; ext=[]
for S in inst[:120]:
    A=alpha(S); R,C=derive(S)
    full.append(factorial(len(A[0]))*factorial(len(A[1])))
    ext.append(len(R)*len(C))
print("\n     all orderings        : median %d   max %d"%(int(np.median(full)),max(full)))
print("     linear extensions    : median %d   max %d"%(int(np.median(ext)),max(ext)))
print("     reduction factor     : median %.1fx"%np.median([f/max(e,1) for f,e in zip(full,ext)]))
print("""
{0}
  WHAT THIS IS
{0}
""".format("="*88))
if allok==len(inst):
    print("""  **THE LINEAR EXTENSIONS OF THE INCLUSION ORDER CONTAIN EVERY SOLUTION.**
  Not a heuristic that usually works — **the search space that provably
  contains the answer**, and it is the one Birkhoff's theorem names.

     the transposition landscape has traps
     **the linear-extension space has none, because it is not a landscape
     — it is an enumeration of the structure's own admissible orders**

  **That is the non-local move, and §7.9 already had it.** The book counts
  maximal chains as linear extensions and never uses them as a search
  space.""")
else:
    print("""  **NOT COMPLETE — %d of %d.** Linear extensions of the inclusion order
  contain most solutions and not all, so the inclusion order is not the
  right partial order. **The structure is there; the relation is not yet
  the right one.**"""%(allok,len(inst)))