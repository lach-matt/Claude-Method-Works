import numpy as np, random
from itertools import product, permutations
random.seed(139)
print("="*88)
print("  STEP 1 — WHAT 'MONOTONE ENDPOINTS' MEANS ABOUT THE INTERVALS")
print("="*88)
print("""
  Rows can be ordered with lo and hi both non-decreasing **iff the
  intervals are totally ordered by**

     [a,b] ≼ [c,d]   iff   a ≤ c  and  b ≤ d

  Two intervals are INCOMPARABLE iff a < c and b > d — that is, one lies
  STRICTLY INSIDE the other at both ends.

  > **monotone endpoints ⟺ no interval is strictly inside another**
""")
def mono(spans):
    o=sorted(spans)
    return all(o[i][0]<=o[i+1][0] and o[i][1]<=o[i+1][1] for i in range(len(o)-1))
def nostrict(spans):
    return not any(a<c and d<b for (a,b) in spans for (c,d) in spans)
n=ag=0; bad=[]
for _ in range(20000):
    k=random.randint(2,5)
    sp=[]
    for _ in range(k):
        a=random.randint(0,6); b=random.randint(a,6); sp.append((a,b))
    n+=1
    m=mono(sp); s=nostrict(sp)
    ag+=(m==s)
    if m!=s and len(bad)<3: bad.append((sp,m,s))
print("     %d random interval families : %d agree  (%.2f%%)"%(n,ag,100*ag/n))
for sp,m,s in bad: print("       %s  mono=%s  nostrict=%s"%(sp,m,s))
print("="*88)
print("  STEP 2 — SO THE SEARCH IS: A C1P ORDER WITH NO STRICT NESTING")
print("="*88)
print("""
  If row A's column SET strictly contains row B's, then in any C1P order
  A's interval contains B's. **The nesting is strict only if B fails to
  touch either end of A.** So the search asks: can every contained row be
  pushed to an END of its container?
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def c1p_spans(S,pc):
    ic={v:i for i,v in enumerate(pc)}
    sp={}
    for r in alpha(S)[0]:
        s=sorted(ic[c] for (a,c) in S if a==r)
        if not s or s!=list(range(s[0],s[0]+len(s))): return None
        sp[r]=(s[0],s[-1])
    return sp
def searchable(S):
    A=alpha(S)
    for pc in permutations(A[1]):
        sp=c1p_spans(S,pc)
        if sp and nostrict(list(sp.values())): return True
    return False
def anyc1p(S):
    A=alpha(S)
    return any(c1p_spans(S,pc) is not None for pc in permutations(A[1]))
print("  check: is 'no strict nesting achievable' the same as reorderable?\n")
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
n=ag=0; mism=[]
for _ in range(2500):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    a=reorderable(S); b=searchable(S)
    n+=1; ag+=(a==b)
    if a!=b and len(mism)<3: mism.append((sorted(S),a,b))
print("     %d instances : %d agree  (%.2f%%)"%(n,ag,100*ag/n))
for S,a,b in mism: print("       X=%s reorderable=%s searchable=%s"%(S,a,b))
print("="*88)
print("  STEP 3 — AND SET CONTAINMENT IS ORDER-INDEPENDENT")
print("="*88)
print("""
  Whether row B's SET is contained in row A's does not depend on any
  ordering. **So the containment structure is fixed before the search
  begins**, and only the question of touching an end is order-dependent.
""")
def contain_pairs(S):
    A=alpha(S)
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    return [(x,y) for x in A[0] for y in A[0] if x!=y and sup[y]<sup[x]]
tot=0; withc=0; reord=0; cr=0
for _ in range(2000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not anyc1p(S): continue
    tot+=1
    cp=contain_pairs(S); r=reorderable(S)
    if cp: withc+=1; cr+= r
    else: reord+= r
print("     C1P instances                          : %d"%tot)
print("     with at least one strict set-containment: %d,  of which reorderable %d  (%.0f%%)"%(withc,cr,100*cr/max(withc,1)))
print("     with none                               : %d,  of which reorderable %d"%(tot-withc,reord))
print("""
  **If no row's set strictly contains another's, the instance is
  reorderable whenever it is C1P** — nothing can nest, so nothing can nest
  strictly. **The whole difficulty lives in the containment pairs.**
""")