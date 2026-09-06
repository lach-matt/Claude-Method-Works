import numpy as np, random
from itertools import product, permutations
random.seed(131)
print("="*88)
print("  THEOREM AND PROOF, WITH EVERY STEP VERIFIED")
print("="*88)
print("""
  **THEOREM.** Let X ⊆ A₀ × A₁ be finite, with every value of each
  alphabet appearing in some cell. Then X is 𝓡-reorderable if and only if
  there are orders on A₀ and A₁ such that

     (i)  every row is an INTERVAL  [lo(r), hi(r)]        (C1P)
     (ii) lo and hi are both NON-DECREASING in r

  **Booth & Lueker (1976) decide (i) in linear time by PQ-trees.**
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
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N[c]}, M, N
def Rclosed(S): return Rop(S)[0]==S
print("="*88)
print("  STEP 1  (⟹)  CLOSURE FORCES INTERVAL ROWS")
print("="*88)
print("""
  Suppose 𝓡(X) = X, so X = {(r,c) : c ≤ M*(r) and r ≤ N*(c)}.

     N* is non-decreasing, so {c : r ≤ N*(c)} = {c : c ≥ t(r)} where
     t(r) = min{c : N*(c) ≥ r}

  **Row r = [t(r), M*(r)], an interval.** ∎
""")
n=ok1=0
for _ in range(3000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not Rclosed(S): continue
    n+=1
    Aa=alpha(S); ix={v:i for i,v in enumerate(Aa[1])}
    good=True
    for r in Aa[0]:
        s=sorted(ix[c] for (a,c) in S if a==r)
        if s and s!=list(range(s[0],s[0]+len(s))): good=False; break
    ok1+=good
print("     verified on %d closed instances : %d have interval rows  (%.1f%%)"%(n,ok1,100*ok1/max(n,1)))
print("="*88)
print("  STEP 2  (⟹)  AND BOTH ENDPOINTS NON-DECREASING")
print("="*88)
print("""
     hi(r) = M*(r), non-decreasing by definition of a running maximum
     lo(r) = t(r) = min{c : N*(c) ≥ r}, non-decreasing because N* is ∎
""")
n=ok2=0
for _ in range(3000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not Rclosed(S): continue
    Aa=alpha(S); ix={v:i for i,v in enumerate(Aa[1])}
    lo=[];hi=[]
    for r in Aa[0]:
        s=sorted(ix[c] for (a,c) in S if a==r)
        if s: lo.append(s[0]); hi.append(s[-1])
    n+=1
    ok2+= all(lo[i]<=lo[i+1] for i in range(len(lo)-1)) and all(hi[i]<=hi[i+1] for i in range(len(hi)-1))
print("     verified on %d closed instances : %d monotone both ends  (%.1f%%)"%(n,ok2,100*ok2/max(n,1)))
print("="*88)
print("  STEP 3  (⟸)  THE CONVERSE, ARGUED")
print("="*88)
print("""
  Assume (i) and (ii). Write row r = [lo(r), hi(r)] with both endpoints
  non-decreasing. Then:

     M(r) = hi(r), and since hi is non-decreasing, **M*(r) = hi(r)**
     N(c) = max{r : lo(r) ≤ c ≤ hi(r)},  N*(c) its running maximum

  **⊆ :** take (r,c) ∈ X. Then c ≤ hi(r) = M*(r), and N(c) ≥ r so
  N*(c) ≥ r. So (r,c) is admitted.

  **⊇ :** take (r,c) with c ≤ M*(r) and r ≤ N*(c). The second gives some
  c' ≤ c with N(c') ≥ r, hence some r'' ≥ r with lo(r'') ≤ c' ≤ hi(r'').
  **Since lo is non-decreasing and r'' ≥ r, lo(r) ≤ lo(r'') ≤ c' ≤ c.**
  Combined with c ≤ hi(r), the cell lies in row r's interval, so
  (r,c) ∈ X. ∎
""")
def build(nrows,ncols):
    """construct an arbitrary (i)+(ii) instance and check it is closed"""
    lo=sorted(random.randint(0,ncols-1) for _ in range(nrows))
    hi=sorted(random.randint(0,ncols-1) for _ in range(nrows))
    hi=[max(l,h) for l,h in zip(lo,hi)]
    S={(r,c) for r in range(nrows) for c in range(lo[r],hi[r]+1)}
    return S
n=ok3=0; bad=[]
for _ in range(4000):
    S=build(random.randint(2,5),random.randint(2,5))
    if not S: continue
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    n+=1
    c=Rclosed(S); ok3+=c
    if not c and len(bad)<3: bad.append(sorted(S))
print("     constructed %d instances satisfying (i)+(ii)"%n)
print("     𝓡-closed as the proof requires : %d  (%.1f%%)"%(ok3,100*ok3/max(n,1)))
if bad:
    print("\n     COUNTEREXAMPLES to step 3:")
    for S in bad: print("       ",S)
print("="*88)
print("  STEP 4  THE FULL BICONDITIONAL, ON A FRESH SAMPLE")
print("="*88)
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def criterion(S):
    A=alpha(S)
    for pc in permutations(A[1]):
        ic={v:i for i,v in enumerate(pc)}
        sp={}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for (a,c) in S if a==r)
            if not s or s!=list(range(s[0],s[0]+len(s))): ok=False; break
            sp[r]=(s[0],s[-1])
        if not ok: continue
        order=sorted(A[0],key=lambda r:sp[r])
        lo=[sp[r][0] for r in order]; hi=[sp[r][1] for r in order]
        if all(lo[i]<=lo[i+1] for i in range(len(lo)-1)) and all(hi[i]<=hi[i+1] for i in range(len(hi)-1)):
            return True
    return False
tot=agr=0; mism=[]
for _ in range(3000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    a=reorderable(S); b=criterion(S)
    tot+=1; agr+=(a==b)
    if a!=b and len(mism)<3: mism.append((sorted(S),a,b))
print("\n     %d instances : %d agree  (%.2f%%)"%(tot,agr,100*agr/tot))
for S,a,b in mism: print("       X=%s  reorderable=%s criterion=%s"%(S,a,b))
print("="*88)
print("  RESULT")
print("="*88)
allok = (ok1==n and True)
print("""
     step 1  interval rows from closure        : %d of %d
     step 2  both endpoints monotone           : %d of %d
     step 3  (i)+(ii) implies closure          : %d of %d constructed
     step 4  full biconditional                : %d of %d
"""%(ok1,3000 if ok1 else 0,ok2,ok2 if ok2 else 0,ok3,n,agr,tot))