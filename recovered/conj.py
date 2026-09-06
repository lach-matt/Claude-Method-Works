import numpy as np, random
from itertools import product, permutations
random.seed(127)
print("="*88)
print("  THE CONJECTURE, TESTED DIRECTLY")
print("="*88)
print("""
  **CONJECTURE.** X is 𝓡-reorderable at d = 2 iff there is a column order
  making every row an interval (C1P) AND a row order making both interval
  endpoints non-decreasing.

  Test: for each X, search column orders for C1P; for each C1P column
  order, ask whether the rows can be sorted so lo and hi are both
  non-decreasing. Compare with brute-force reorderability.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def Rop(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N[c]}
def Rclosed(S): return Rop(S)==S
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def conj(S):
    """C1P column order + a row order with both endpoints non-decreasing"""
    A=alpha(S)
    for pc in permutations(A[1]):
        ic={v:i for i,v in enumerate(pc)}
        spans={}
        good=True
        for r in A[0]:
            s=sorted(ic[c] for (a,c) in S if a==r)
            if not s: spans[r]=None; continue
            if s!=list(range(s[0],s[0]+len(s))): good=False; break
            spans[r]=(s[0],s[-1])
        if not good: continue
        rows=[r for r in A[0] if spans[r] is not None]
        if len(rows)!=len(A[0]): continue
        # sort rows by (lo, hi); both must then be non-decreasing
        order=sorted(rows,key=lambda r:(spans[r][0],spans[r][1]))
        lo=[spans[r][0] for r in order]; hi=[spans[r][1] for r in order]
        if all(lo[i]<=lo[i+1] for i in range(len(lo)-1)) and \
           all(hi[i]<=hi[i+1] for i in range(len(hi)-1)):
            return True
    return False
print("  %10s%14s%14s%14s%12s"%("instances","agree","conj TRUE/reord F","conj FALSE/reord T","accuracy"))
print("  "+"-"*66)
for lo,hi in [(2,3),(2,4),(3,5)]:
    n=ag=fp=fn=0; ex=[]
    for _ in range(1500):
        A=[list(range(random.randint(lo,hi))),list(range(random.randint(lo,hi)))]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,len(cells))))
        r=reorderable(S); c=conj(S)
        n+=1; ag+=(r==c)
        if c and not r: fp+=1; ex.append(('FP',S))
        if r and not c: fn+=1; ex.append(('FN',S))
    print("  %10s%14d%14d%14d%12.1f%%"%("%d-%d"%(lo,hi),ag,fp,fn,100*ag/n))
    if ex[:2]:
        for k,S in ex[:2]: print("        %s : %s"%(k,sorted(S)))
print("="*88)
print("  AND ON THE 25 GAP CASES SPECIFICALLY")
print("="*88)
def has_c1p(S):
    A=alpha(S)
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for (a,c) in S if a==r)
            if s and s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: return True
    return False
gap=[]
while len(gap)<40:
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if has_c1p(S) and not reorderable(S): gap.append(S)
wrong=sum(1 for S in gap if conj(S))
print("\n     C1P-but-not-reorderable instances : %d"%len(gap))
print("     conjecture wrongly says TRUE      : %d"%wrong)
print("     conjecture correctly says FALSE   : %d"%(len(gap)-wrong))
print("="*88)
print("  VERDICT")
print("="*88)
tot=0; agr=0
for _ in range(3000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    tot+=1; agr+= (reorderable(S)==conj(S))
print("\n     overall on a fresh sample : %d of %d  (%.2f%%)"%(agr,tot,100*agr/tot))
if agr==tot:
    print("""
  **THE CONJECTURE HOLDS ON EVERY INSTANCE TESTED.**

     𝓡-reorderable  ⟺  C1P columns AND monotone row endpoints

  **C1P is linear-time by PQ-trees. The endpoint condition is a sort.**
  That is a decision procedure, and §23.4's open question becomes: does
  the PQ-tree admit a leaf whose induced row order is monotone?""")
else:
    print("""
  **NOT EXACT — %d of %d.** The conjecture is close and not right; the
  remaining disagreements are the next thing to characterise."""%(agr,tot))