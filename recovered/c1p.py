import numpy as np, random
from itertools import product, permutations
random.seed(113)
print("="*88)
print("  WHAT SHAPE IS A ROW OF AN 𝓡-CLOSED SET?")
print("="*88)
print("""
  X = {(r,c) : c <= M*(r)  and  r <= N*(c)}, both running maxima
  non-decreasing.

     c <= M*(r)      caps the row from ABOVE
     r <= N*(c)      and since N* is non-decreasing, this says c >= some
                     threshold — caps it from BELOW

  **So every row is an INTERVAL [t(r), M*(r)].** Not an initial segment —
  an interval. Verify.
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
            T=relabel(S,[list(p0),list(p1)])
            if Rclosed(T): return True,[list(p0),list(p1)]
    return False,None
def rows_are_intervals(S):
    A=alpha(S)
    idx={v:i for i,v in enumerate(A[1])}
    for r in A[0]:
        s=sorted(idx[c] for (a,c) in S if a==r)
        if s and s!=list(range(s[0],s[0]+len(s))): return False
    return True
n=ok=0
for _ in range(3000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not Rclosed(S): continue
    n+=1; ok+=rows_are_intervals(S)
print("     𝓡-closed instances : %d"%n)
print("     every row an interval : %d  (%.1f%%)"%(ok,100*ok/max(n,1)))
print("="*88)
print("  WHICH IS THE CONSECUTIVE ONES PROPERTY")
print("="*88)
print("""
  A 0-1 matrix has the **consecutive ones property for rows (C1P)** if the
  columns can be permuted so every row's 1s are contiguous.

  **C1P is decidable in LINEAR time by PQ-trees** (Booth & Lueker 1976),
  and it is the interval / matching literature — not the order-dimension
  literature §23.4 cited.

  **So: reorderable ⟹ C1P.** Test the implication and its converse.
""")
def has_c1p(S):
    A=alpha(S)
    for p in permutations(A[1]):
        idx={v:i for i,v in enumerate(p)}
        good=True
        for r in A[0]:
            s=sorted(idx[c] for (a,c) in S if a==r)
            if s and s!=list(range(s[0],s[0]+len(s))): good=False; break
        if good: return True
    return False
n=0; imp=0; conv=0; both=0; ex=[]
for _ in range(2500):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    r,_=reorderable(S); c=has_c1p(S)
    n+=1
    if r and c: both+=1
    if r and not c: imp+=1
    if c and not r: conv+=1
    if c and not r and len(ex)<3: ex.append(S)
print("     instances                       : %d"%n)
print("     reorderable AND C1P             : %d"%both)
print("     reorderable but NOT C1P         : %d   <- would refute the implication"%imp)
print("     C1P but NOT reorderable         : %d   <- the gap"%conv)
if ex:
    print("\n     C1P but not reorderable, examples:")
    for S in ex: print("       ",sorted(S))
print("="*88)
print("  SO WHAT DOES REORDERABILITY ADD TO C1P?")
print("="*88)
print("""
  C1P gives intervals. **𝓡-closure needs the intervals to be NESTED-BY-
  ENDPOINT: both endpoints non-decreasing in the row order.**
""")
def endpoints_monotone(S):
    ok,o=reorderable(S)
    if not ok: return None
    T=relabel(S,o); A=[sorted({t[i] for t in T}) for i in range(2)]
    lo=[];hi=[]
    for r in A[0]:
        s=sorted(c for (a,c) in T if a==r)
        if s: lo.append(s[0]); hi.append(s[-1])
    return all(lo[i]<=lo[i+1] for i in range(len(lo)-1)) and all(hi[i]<=hi[i+1] for i in range(len(hi)-1))
res=[]
for _ in range(400):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    v=endpoints_monotone(S)
    if v is not None: res.append(v)
print("     of reorderable instances, both endpoints monotone : %d of %d  (%.1f%%)"
      %(sum(res),len(res),100*sum(res)/max(len(res),1)))
print("""
{0}
  THE LEAD
{0}

  **Reorderability at d = 2 is C1P plus monotone endpoints**, and C1P alone
  is decidable in LINEAR time by PQ-trees. **That is a concrete route to a
  decision procedure and it is in the interval literature**, which §23.4
  never cited because it was pointed at order dimension instead.

     C1P                      Booth & Lueker 1976, linear time
     + endpoints monotone     the extra condition 𝓡 imposes
     = 𝓡-reorderable          conjectured; testable directly
""".format("="*88))