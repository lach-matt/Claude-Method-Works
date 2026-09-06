import numpy as np, random, itertools
from itertools import product, permutations
random.seed(173)
print("="*88)
print("  THE PROOF")
print("="*88)
print("""
  **NOTATION.** X ⊆ A₀ × A₁ finite, every alphabet value used. For a column
  order, S(r) is row r's column set, M(r) = max S(r), N(c) = max{r : c ∈ S(r)},
  and M*, N* their running maxima. 𝓡(X) = {(r,c) : c ≤ M*(r) and r ≤ N*(c)}.

  ────────────────────────────────────────────────────────────────────────
  **LEMMA 1.** If 𝓡(X) = X then every row is an interval and both interval
  endpoints are non-decreasing in r.

  *Proof.* N* is non-decreasing, so {c : r ≤ N*(c)} = {c : c ≥ t(r)} with
  t(r) = min{c : N*(c) ≥ r}. Hence row r = [t(r), M*(r)], an interval.
  M* is non-decreasing by construction; t is non-decreasing because N* is. ∎

  ────────────────────────────────────────────────────────────────────────
  **LEMMA 2.** Conversely, if every row is an interval [lo(r), hi(r)] with
  lo and hi both non-decreasing, then 𝓡(X) = X.

  *Proof.* hi non-decreasing gives M* = hi. (⊆) For (r,c) ∈ X: c ≤ hi(r)
  = M*(r), and N(c) ≥ r so N*(c) ≥ r. (⊇) Given c ≤ M*(r) and r ≤ N*(c),
  the latter yields c′ ≤ c and r″ ≥ r with lo(r″) ≤ c′ ≤ hi(r″). Since lo
  is non-decreasing and r″ ≥ r, **lo(r) ≤ lo(r″) ≤ c′ ≤ c**. With
  c ≤ hi(r) this puts (r,c) in row r's interval, so (r,c) ∈ X. ∎

  ────────────────────────────────────────────────────────────────────────
  **LEMMA 3.** A family of intervals admits an ordering with both endpoints
  non-decreasing **iff no interval is strictly inside another.**

  *Proof.* Define [a,b] ≼ [c,d] iff a ≤ c and b ≤ d; this is a partial
  order. A monotone ordering is exactly a linear extension of ≼ that is
  also a total order, i.e. ≼ is total. Two intervals are ≼-incomparable
  precisely when a < c and d < b — strict containment. ∎

  ────────────────────────────────────────────────────────────────────────
  **LEMMA 4 (Booth & Lueker 1976).** The column orders in which every row
  is an interval are exactly the frontiers of the PQ-tree T(X), which is
  unique and constructible in O(\\|X\\|). *Cited.*

  ────────────────────────────────────────────────────────────────────────
  **THEOREM.** X is 𝓡-reorderable **iff T(X) exists and has a frontier in
  which no row interval is strictly inside another.**

  *Proof.* By Lemmas 1–2, reorderable ⟺ some column order gives interval
  rows with monotone endpoints. By Lemma 3, monotone ⟺ no strict nesting.
  By Lemma 4, the column orders giving interval rows are the frontiers of
  T(X). ∎
""")
print("="*88)
print("  THE ALGORITHM THE PROOF SPECIFIES")
print("="*88)
print("""
  Enumerating frontiers is exponential. **The theorem's condition is local
  to each node once the right state is carried**, so a bottom-up pass
  suffices.

  **STATE.** For each node v, the set of ends v can offer:

     E(v) ⊆ {L, R}   — 'in some admissible arrangement of v's subtree with
                       no strict nesting inside it, the row anchored at v
                       can be placed touching v's left / right end'

  **P-node**: children permute freely, so any child may take an end; at
  most TWO children may demand one. **Q-node**: only the first and last
  children touch the ends, up to reversal.
""")
def overlap(a,b): return bool(a&b) and not (a<=b) and not (b<=a)
def components(sets):
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
def c1p_orders(cols,rows,cap=5000):
    out=[]
    for p in permutations(sorted(cols)):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for rw in rows:
            s=sorted(ic[c] for c in rw)
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok:
            out.append(p)
            if len(out)>=cap: break
    return out
class N:
    def __init__(s,t,leaves,kids=None,orders=None):
        s.t=t; s.leaves=leaves; s.kids=kids or []; s.orders=orders
def build(cols,rows):
    rows=[r for r in rows if r and r!=frozenset(cols)]
    if not rows: return N('P',set(cols),[N('L',{c}) for c in sorted(cols)])
    kids=[]; covered=set()
    for cs in components(rows):
        sub=[rows[i] for i in cs]
        u=frozenset().union(*sub); covered|=set(u)
        if len(sub)==1: kids.append(build(set(u),[r for r in rows if r<u]))
        else: kids.append(N('Q',set(u),orders=c1p_orders(set(u),sub)))
    for c in sorted(set(cols)-covered): kids.append(N('L',{c}))
    return N('P',set(cols),kids)
def frontiers(node,cap=200000):
    if node.t=='L': return [tuple(node.leaves)]
    if node.t=='Q': return [tuple(o) for o in (node.orders or [])][:cap]
    kid=[frontiers(k,cap) for k in node.kids]
    out=[]
    for perm in permutations(range(len(kid))):
        for combo in product(*[kid[i] for i in perm]):
            out.append(tuple(itertools.chain(*combo)))
            if len(out)>=cap: return out
    return out
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def nostrict(sp): return not any(a<c and d<b for (a,b) in sp for (c,d) in sp)
def enum_test(S):
    A=alpha(S); sup=sup_of(S)
    root=build(set(A[1]),list(sup.values()))
    for f in frontiers(root):
        ic={v:i for i,v in enumerate(f)}
        sp=[]; ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
            sp.append((s[0],s[-1]))
        if ok and nostrict(sp): return True
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
print("  VERIFY EACH LEMMA SEPARATELY\n")
print("  %-46s%s"%("lemma","verification"))
print("  "+"-"*70)
n1=ok1=0
for _ in range(4000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    if not Rclosed(S): continue
    n1+=1
    Aa=alpha(S); ix={v:i for i,v in enumerate(Aa[1])}
    lo=[];hi=[];good=True
    for r in Aa[0]:
        s=sorted(ix[c] for (a,c) in S if a==r)
        if s!=list(range(s[0],s[0]+len(s))): good=False; break
        lo.append(s[0]); hi.append(s[-1])
    ok1+= good and all(lo[i]<=lo[i+1] for i in range(len(lo)-1)) and all(hi[i]<=hi[i+1] for i in range(len(hi)-1))
print("  %-46s%d of %d"%("L1  closure ⟹ intervals + monotone",ok1,n1))
n2=ok2=0
for _ in range(4000):
    nc=random.randint(2,5); k=random.randint(2,5)
    lo=sorted(random.randint(0,nc-1) for _ in range(k))
    hi=sorted(random.randint(0,nc-1) for _ in range(k))
    hi=[max(a,b) for a,b in zip(lo,hi)]
    S={(r,c) for r in range(k) for c in range(lo[r],hi[r]+1)}
    if len(alpha(S)[0])<2 or len(alpha(S)[1])<2: continue
    n2+=1; ok2+=Rclosed(S)
print("  %-46s%d of %d"%("L2  intervals + monotone ⟹ closure",ok2,n2))
n3=ok3=0
for _ in range(20000):
    k=random.randint(2,5)
    sp=[]
    for _ in range(k):
        a=random.randint(0,6); b=random.randint(a,6); sp.append((a,b))
    o=sorted(sp)
    m=all(o[i][0]<=o[i+1][0] and o[i][1]<=o[i+1][1] for i in range(len(o)-1))
    n3+=1; ok3+= (m==nostrict(sp))
print("  %-46s%d of %d"%("L3  monotone ⟺ no strict nesting",ok3,n3))
n4=ok4=0
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
for _ in range(700):
    S=build_nested(random.randint(3,5)) if random.random()<0.5 else None
    if S is None:
        A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
        cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    A=alpha(S)
    if len(A[0])<2 or len(A[1])<2: continue
    n4+=1; ok4+= (reorderable(S)==enum_test(S))
print("  %-46s%d of %d"%("THM reorderable ⟺ good frontier exists",ok4,n4))