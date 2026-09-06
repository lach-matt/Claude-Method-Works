import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(263)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Ev(S,o):
    T=relabel(S,o); A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=N[c])-len(T)
def Rclosed(S): return Ev(S,alpha(S))==0
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Ev(S,[list(p0),list(p1)])==0: return True
    return False
def descend(S,maxit=400,patience=3):
    A=alpha(S); o=[list(A[0]),list(A[1])]
    e=Ev(S,o); it=0; bad=0
    while e>0 and it<maxit:
        cands=[]
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                cands.append((Ev(S,p),p))
        cands.sort(key=lambda t:t[0])
        if cands[0][0]<e: e,o=cands[0]; bad=0
        else:
            bad+=1
            if bad>patience: break
            e,o=random.choice(cands[:max(2,len(cands)//2)])
        it+=1
    return e==0,it
def chain(S,ax=0):
    if ax==0: v=[frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]]
    else: v=[frozenset(a for (a,b) in S if b==c) for c in alpha(S)[1]]
    return all(p<=q or q<=p for p in v for q in v)
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
def width2(S):
    rows=sorted(set(sup_of(S).values()),key=len,reverse=True)
    for A in rows:
        ins=[b for b in rows if b<A]
        for t in combinations(ins,3):
            if all(not(x<=y or y<=x) for x,y in combinations(t,2)): return False
    return True
print("="*88)
print("  THE PROOF ASKED FOR IS OF A FALSE STATEMENT")
print("="*88)
print("""
  **Claim:** step 6 (descent with bounded uphill) always succeeds where
  step 7 (enumeration) would.

  **Measured earlier: 96.7%.** It fails 3.3% of the time. A proof is not
  available because the statement is false, and saying so is the finding.

  **So measure the residual instead: after the cascade AND the descent,
  what actually reaches step 7, and what does it cost there?**
""")
tot=0; c_dec=0; d_dec=0; resid=[]
for _ in range(3000):
    A=[list(range(random.randint(2,5))),list(range(random.randint(2,5)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    tot+=1
    if chain(S,0) or chain(S,1): c_dec+=1; continue
    if not c1p(S): c_dec+=1; continue
    if not width2(S): c_dec+=1; continue
    ok,_=descend(S)
    if ok: d_dec+=1; continue
    resid.append(S)
print("     instances                       : %d"%tot)
print("     decided by the cascade (1–5)    : %d  (%.1f%%)"%(c_dec,100*c_dec/tot))
print("     decided by the descent (6)      : %d  (%.1f%%)"%(d_dec,100*d_dec/tot))
print("     **reaching step 7**             : %d  (%.2f%%)"%(len(resid),100*len(resid)/tot))
print("="*88)
print("  AND WHAT STEP 7 COSTS ON THE RESIDUAL")
print("="*88)
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
def c1p_ord(cols,rows,cap=3000):
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
class Nd:
    def __init__(s,t,lv,k=None,o=None): s.t=t; s.leaves=frozenset(lv); s.kids=k or []; s.orders=o
def build(cols,rows):
    rows=[r for r in rows if r and r!=frozenset(cols)]
    if not rows: return Nd('P',cols,[Nd('L',{c}) for c in sorted(cols)])
    kids=[]; cov=set()
    for cs in comps(rows):
        sub=[rows[i] for i in cs]; u=frozenset().union(*sub); cov|=set(u)
        if len(sub)==1: kids.append(build(set(u),[r for r in rows if r<u]))
        else: kids.append(Nd('Q',u,o=c1p_ord(set(u),sub)))
    for c in sorted(set(cols)-cov): kids.append(Nd('L',{c}))
    return Nd('P',cols,kids)
def frontier_count(S,cap=500000):
    A=alpha(S); root=build(set(A[1]),list(sup_of(S).values()))
    def f(v):
        if v.t=='L': return 1
        if v.t=='Q': return len(v.orders or [])
        from math import factorial
        n=len(v.kids); p=factorial(n)
        for k in v.kids: p*=f(k)
        return min(p,cap)
    return f(root)
if resid:
    fc=[frontier_count(S) for S in resid]
    print("\n     residual instances : %d"%len(resid))
    print("     frontier count     : median %d   max %d"%(int(np.median(fc)),max(fc)))
    print("     all reorderable?   : %s"%all(reorderable(S) for S in resid[:40]))
    A0=[len(alpha(S)[0]) for S in resid]; A1=[len(alpha(S)[1]) for S in resid]
    print("     sizes              : rows %d–%d, cols %d–%d"%(min(A0),max(A0),min(A1),max(A1)))
else:
    print("\n     **nothing reached step 7 in this sample**")
print("="*88)
print("  WHAT CAN BE PROVED INSTEAD")
print("="*88)
print("""
  **Not** that descent always succeeds — measured false at 96.7%.

  **But this, which is provable and useful:** step 7's cost is bounded by
  the PQ-tree's frontier count, and that count is
  **∏_P (children!) × ∏_Q (admissible orders)** — a product over the tree,
  computable BEFORE running it. **So the fallback's cost is known in
  advance**, and an instance can be rejected as too expensive rather than
  attempted.

  That is a bound on step 7, which is the second thing asked for. **It is
  not a polynomial bound**, and no measurement here makes it one.
""")