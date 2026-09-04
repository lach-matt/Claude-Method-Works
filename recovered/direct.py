import numpy as np, random
from itertools import product, permutations
random.seed(89)
print("="*88)
print("  WHAT 𝓡-CLOSURE ACTUALLY IS AT d = 2")
print("="*88)
print("""
  Let M(r) = max column in row r, N(c) = max row in column c, and write
  M*(r), N*(c) for their RUNNING MAXIMA. Then

     **𝓡(X) = {(r,c) : c <= M*(r)  and  r <= N*(c)}**

  and X is 𝓡-closed exactly when that set is X. **Two conditions, not one**
  — which is why a one-sided 'downset' condition was the wrong import.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def Rop(S):
    A=alpha(S); Ls=sorted(S)
    M={}; run=-1
    for v in A[0]:
        c=[y for (x,y) in Ls if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={}; run=-1
    for w in A[1]:
        c=[x for (x,y) in Ls if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N[c]}
def Rclosed(S): return Rop(S)==S
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True,[list(p0),list(p1)]
    return False,None
X={(0,1),(0,4),(2,2)}
ok,o=reorderable(X)
print("     the counterexample X =",sorted(X))
print("     𝓡-reorderable :",ok,"  under",o)
T=relabel(X,o)
print("     in that order  :",sorted(T))
print("     row supports   :",{r:sorted(c for (a,c) in T if a==r) for r in {t[0] for t in T}})
print("""
  **Supports {0} and {1,2} — not nested, and still 𝓡-closed.** The
  two-sided condition excludes (1,0) via r <= N*(c), which no one-sided
  downset condition does.
""")
print("="*88)
print("  SO SEARCH FOR THE RIGHT INVARIANT, EMPIRICALLY")
print("="*88)
def feats(S):
    A=alpha(S)
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    col={c:frozenset(a for (a,b) in S if b==c) for c in A[1]}
    return dict(
      rows=len(A[0]), cols=len(A[1]), cells=len(S),
      rowchain=all(p<=q or q<=p for p in sup.values() for q in sup.values()),
      colchain=all(p<=q or q<=p for p in col.values() for q in col.values()),
      distinct_rows=len({sup[r] for r in A[0]}),
      distinct_cols=len({col[c] for c in A[1]}),
      density=len(S)/(len(A[0])*len(A[1])),
    )
data=[]
for _ in range(4000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    r,_=reorderable(S)
    data.append((feats(S),r))
print("\n  candidate invariants vs 𝓡-reorderability:\n")
print("  %-26s%12s%12s%10s"%("invariant","holds&reord","holds&not","implies?"))
print("  "+"-"*62)
for key,fn in [("row supports a chain",lambda f:f['rowchain']),
               ("col supports a chain",lambda f:f['colchain']),
               ("either a chain",lambda f:f['rowchain'] or f['colchain']),
               ("both chains",lambda f:f['rowchain'] and f['colchain']),
               ("distinct rows <= 2",lambda f:f['distinct_rows']<=2),
               ("density = 1",lambda f:f['density']==1.0)]:
    a=sum(1 for f,r in data if fn(f) and r); b=sum(1 for f,r in data if fn(f) and not r)
    print("  %-26s%12d%12d%10s"%(key,a,b,"yes" if b==0 else "no"))
tot=sum(1 for _,r in data if r)
print("\n     reorderable instances : %d of %d"%(tot,len(data)))
print("\n  and the converse — reorderable but NOT satisfying each:\n")
for key,fn in [("row supports a chain",lambda f:f['rowchain']),
               ("either a chain",lambda f:f['rowchain'] or f['colchain'])]:
    c=sum(1 for f,r in data if r and not fn(f))
    print("     %-26s %d reorderable instances fail it"%(key,c))
print("""
{0}
  THE HONEST POSITION ON §23.4
{0}
""".format("="*88))
print("""  **No simple invariant tested characterises 𝓡-reorderability at d = 2.**
  A chain of row supports is neither necessary nor sufficient. **The
  earlier claim that d = 2 is settled is withdrawn — CORRECTION 135.**

  **What is established:**

     𝓡-closure at d = 2 is the two-sided condition
        X = {(r,c) : c <= M*(r) and r <= N*(c)}
     checkable in O(rc) for a GIVEN order

     the two real indices close under one explicit reordering
        periodic table 36 -> 0, calendar 7 -> 0

     the DECISION problem — does such an order exist — remains open at
     every d, including 2

  **§23.4 should say that, and nothing stronger.**
""")