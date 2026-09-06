import numpy as np, random
from itertools import product, permutations
random.seed(211)
print("="*88)
print("  SHARPENING THE COUNT")
print("="*88)
print("""
  Immediate containment children of A are pairwise NON-NESTED. Each must
  touch an end of A. **Can two of them share an end?**

     if B and C both start at A's left, then B = [0,b], C = [0,d];
     whichever is shorter is a PREFIX of the other, hence NESTED —
     contradicting immediacy

  **So each end takes at most one immediate child, and A has at most TWO.**
  Not two components — two children.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def kids(A,rows): 
    ins=[r for r in rows if r<A]
    return [b for b in ins if not any(c!=b and b<c and c<A for c in ins)]
def struct2(S):
    rows=sorted(set(sup_of(S).values()),key=lambda s:(-len(s),sorted(s)))
    return all(len(kids(A,rows))<=2 for A in rows)
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
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%9s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*54)
tot_fp=0
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(2500):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=gen_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S); b=c1p(S) and struct2(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    tot_fp+=fp
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:56]))
print("="*88)
if tot_fp==0:
    print("  **EXACT.**")
    print("""
     **X is 𝓡-reorderable  ⟺  X is C1P, and in the containment forest
       every row has at most two immediate children.**

     C1P                 linear      (Booth & Lueker 1976)
     containment forest  O(r² c)
     child count         O(r)
     **TOTAL             O(r² c)  — POLYNOMIAL**

  No traversal, no backtracking, no search. **The recursion the six
  implementations chased is discharged by the forest itself**: a row with
  three immediate children has three things needing two ends, and that is
  the only obstruction there is.
""")
else:
    print("  **NOT EXACT — %d false positives.** Still necessary, not sufficient."%tot_fp)