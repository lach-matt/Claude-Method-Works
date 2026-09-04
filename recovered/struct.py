import numpy as np, random
from itertools import product, permutations, combinations
random.seed(199)
print("="*88)
print("  THE STRUCTURAL READING")
print("="*88)
print("""
  Every pair of rows is disjoint, overlapping, or nested.

     **disjoint**    — place side by side; the intervals are ≼-comparable
     **overlapping** — [a,b], [c,d] with a<c≤b<d are ≼-comparable
     **nested**      — B inside A is ≼-comparable ONLY if B touches an end

  **So overlap and disjointness never obstruct. All the difficulty is
  nesting**, and nesting lives in the containment forest.

  **STRUCTURAL CLAIM.** For each row A, its IMMEDIATE containment children
  are pairwise non-nested. Grouped into overlap components, each component
  occupies one contiguous block. Only blocks at A's two ends can expose
  their members. **So A may have at most two such components.**
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def overlap(a,b): return bool(a&b) and not(a<=b) and not(b<=a)
def comps(sets):
    n=len(sets); par=list(range(n))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i in range(n):
        for j in range(i+1,n):
            if overlap(sets[i],sets[j]):
                a,b=f(i),f(j)
                if a!=b: par[a]=b
    g={}
    for i in range(n): g.setdefault(f(i),[]).append(i)
    return list(g.values())
def kids_of(A,rows):
    ins=[r for r in rows if r<A]
    return [b for b in ins if not any(c!=b and b<c and c<A for c in ins)]
def struct_test(S,cap=2):
    rows=sorted(set(sup_of(S).values()),key=lambda s:(-len(s),sorted(s)))
    for A in rows:
        K=kids_of(A,rows)
        if not K: continue
        cs=comps(K)
        if len(cs)>cap: return False
    return True
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    NN={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); NN[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=NN[c]}==S
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def c1p(S):
    A=alpha(S); sup=sup_of(S)
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: return True
    return False
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%9s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*54)
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(2500):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=build_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S); b=c1p(S) and struct_test(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:56]))
print("="*88)
print("  COST")
print("="*88)
print("""
     containment forest : O(r² c)
     overlap components : O(r²) per row, union-find
     C1P                : linear (Booth & Lueker)
     **total            : O(r³ + rc)  — POLYNOMIAL, no search, no traversal**
""")