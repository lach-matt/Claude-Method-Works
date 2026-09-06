import numpy as np, random
from itertools import product, permutations, combinations
random.seed(149)
print("="*88)
print("  WHEN DOES A CONTAINMENT BLOCK?")
print("="*88)
print("""
  Row B strictly inside row A must TOUCH AN END of A's interval. There are
  two ends. Rows that nest among themselves can share an end.

  > **So the rows strictly inside A must be coverable by TWO CHAINS —
  > one left-anchored, one right-anchored.**

  **By Dilworth's theorem that is exactly: the inclusion poset of the rows
  inside A has WIDTH ≤ 2**, i.e. no three of them are pairwise
  incomparable. **Width is computed by bipartite matching.**
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S):
    A=alpha(S)
    return {r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
def width_le_2(elems,sup):
    """no three pairwise-incomparable"""
    for t in combinations(elems,3):
        if all(not(sup[a]<=sup[b] or sup[b]<=sup[a]) for a,b in combinations(t,2)):
            return False
    return True
def criterion(S):
    A=alpha(S); sup=sup_of(S)
    for a in A[0]:
        inside=[b for b in A[0] if b!=a and sup[b]<sup[a]]
        if not width_le_2(inside,sup): return False
    return True
def c1p_spans(S,pc):
    ic={v:i for i,v in enumerate(pc)}
    sp={}
    for r in alpha(S)[0]:
        s=sorted(ic[c] for (a,c) in S if a==r)
        if not s or s!=list(range(s[0],s[0]+len(s))): return None
        sp[r]=(s[0],s[-1])
    return sp
def anyc1p(S):
    return any(c1p_spans(S,pc) is not None for pc in permutations(alpha(S)[1]))
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
print("  TEST — on C1P instances, does 'C1P AND width ≤ 2' decide it?\n")
print("  %10s%10s%14s%14s%12s"%("alphabets","n","agree","false pos","false neg"))
print("  "+"-"*62)
for lo,hi in [(2,4),(2,5),(3,5)]:
    n=ag=fp=fn=0; ex=[]
    for _ in range(2500):
        A=[list(range(random.randint(lo,hi))),list(range(random.randint(lo,hi)))]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,len(cells))))
        if not anyc1p(S): continue
        n+=1
        a=reorderable(S); b=criterion(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %10s%10d%14d%14d%12d"%("%d-%d"%(lo,hi),n,ag,fp,fn))
    for k,S in ex[:2]: print("        %s : %s"%(k,str(S)[:70]))
print("="*88)
print("  AND THE COST")
print("="*88)
print("""
     C1P                : LINEAR, by PQ-trees (Booth & Lueker 1976)
     width ≤ 2 per row  : the inclusion poset on ≤ r elements; width by
                          Dilworth = bipartite matching, **O(r^2.5)**
     total              : **polynomial**

  **That is a decision procedure**, if the criterion is exact.
""")
print("="*88)
print("  A HARDER TEST — INSTANCES BUILT TO HAVE DEEP CONTAINMENT")
print("="*88)
def build_nested(ncols):
    """rows chosen to create many containments"""
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,ncols-1); b=random.randint(a,ncols-1)
        rows.append(set(range(a,b+1)))
    S=set()
    for i,rw in enumerate(rows):
        for c in rw: S.add((i,c))
    return S
n=ag=fp=fn=0; ex=[]
for _ in range(2000):
    S=build_nested(random.randint(3,5))
    if not S: continue
    A=alpha(S)
    if len(A[0])<2 or len(A[1])<2: continue
    if not anyc1p(S): continue
    n+=1
    a=reorderable(S); b=criterion(S)
    ag+=(a==b)
    if b and not a: fp+=1; ex.append(('FP',sorted(S)))
    if a and not b: fn+=1; ex.append(('FN',sorted(S)))
print("\n     nested-by-construction, C1P : %d"%n)
print("     agree : %d   false pos %d   false neg %d"%(ag,fp,fn))
for k,S in ex[:3]: print("       %s : %s"%(k,str(S)[:70]))