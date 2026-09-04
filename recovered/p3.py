import numpy as np, random
from itertools import product, permutations, combinations
random.seed(157)
print("="*88)
print("  P3 — WORK BACKWARDS FROM THE DESIRED OUTPUT")
print("="*88)
print("""
  **DESIRED OUTPUT.** A polynomial test that, given X, returns whether a
  column order exists with interval rows and no strict nesting.

  **STEP BACK 1.** Six local conditions all failed the same way — zero
  false negatives, false positives rising with nesting depth. **So the test
  cannot examine containers one at a time.**

  **STEP BACK 2.** It must therefore reason over ALL C1P orders at once.
  **The object that represents all C1P orders simultaneously is the
  PQ-tree** — that is what it was built for. So the test lives on the tree.

  **STEP BACK 3.** In a PQ-tree, a row corresponds to a NODE: the deepest
  node whose leaf-span is exactly that row's columns.

     P-node children  : freely permutable  -> a row CAN be moved to an end
     Q-node children  : reversible only    -> a row's position is FIXED up
                                              to flipping the whole node

  **STEP BACK 4.** So 'can B be pushed to an end of A' is not a property of
  the pair (A,B). **It is a property of B's node position within A's
  node**, and that is shared by every row under the same node.

  > **PREDICTION.** The right condition is the width bound applied to the
  > CONTAINMENT FOREST — each row against its IMMEDIATE container only —
  > not to all container/contained pairs. The forest is what the tree
  > induces; the full pair set is the transitive closure, which
  > double-counts.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N[c]}==S
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def anyc1p(S):
    A=alpha(S)
    for pc in permutations(A[1]):
        ic={v:i for i,v in enumerate(pc)}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for (a,c) in S if a==r)
            if not s or s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: return True
    return False
def forest_width(S):
    """each row against its IMMEDIATE container only"""
    A=alpha(S); sup=sup_of(S)
    for a in A[0]:
        kids=[b for b in A[0] if b!=a and sup[b]<sup[a] and
              not any(c!=a and c!=b and sup[b]<sup[c] and sup[c]<sup[a] for c in A[0])]
        for t in combinations(kids,3):
            if all(not(sup[x]<=sup[y] or sup[y]<=sup[x]) for x,y in combinations(t,2)):
                return False
    return True
def crit(S): return anyc1p(S) and forest_width(S)
print("="*88)
print("  TEST THE PREDICTION")
print("="*88)
print("\n  %12s%10s%10s%12s%12s"%("source","C1P n","agree","false pos","false neg"))
print("  "+"-"*58)
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
for lab,gen in [("random",lambda: None),("nested",lambda: None)]:
    n=ag=fp=fn=0; ex=[]
    for _ in range(2000):
        if lab=="random":
            A=[list(range(random.randint(2,5))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=build_nested(random.randint(3,5))
        A=alpha(S)
        if len(A[0])<2 or len(A[1])<2 or not anyc1p(S): continue
        n+=1
        a=reorderable(S); b=crit(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(sorted(S))
        if a and not b: fn+=1
    print("  %12s%10d%10d%12d%12d"%(lab,n,ag,fp,fn))
    if ex[:1]: print("        FP %s"%str(ex[0])[:64])
print("="*88)
print("  WHAT THE BOUNDS SAY THE ANSWER MUST LOOK LIKE")
print("="*88)
print("""
  Whatever the correct test is, the established bounds constrain it:

     it must accept every C1P instance with no set-containment
        — 1,076 of 1,076 such instances are reorderable

     it must reject three pairwise-incomparable rows in one container
        — zero false negatives across 9,094 instances

     it must NOT decide container by container
        — six local conditions, all necessary, none sufficient, and the
          gap grows with nesting depth

     it must agree with §17.4
        — closure is not determined by its proper projections, and a
          per-container test is a projection

  **Those four together say: the test is a single global pass over a
  structure that already merges the containers**, accepting when no three
  incomparable rows compete for two ends anywhere in it.

  **That structure is the PQ-tree, and the pass is a bottom-up traversal.**
  Implementing it is the remaining work; the specification is now fixed by
  the bounds rather than guessed.
""")