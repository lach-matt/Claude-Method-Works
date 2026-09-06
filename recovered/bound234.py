import numpy as np, random
from itertools import product, permutations
from math import factorial
random.seed(227)
print("="*88)
print("  DOES §23.3's INVARIANT BOUND §23.4's SEARCH?")
print("="*88)
print("""
  Distinct row supports correlates 0.606 with backtracking steps. **If the
  steps are bounded by a polynomial in that count, the search is
  polynomial** — because the count is at most the number of rows.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Esize(S,o):
    T=relabel(S,o); A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=N[c])-len(T)
def Rclosed(S): return Esize(S,[sorted({x[i] for x in S}) for i in range(2)])==0
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Esize(S,[list(p0),list(p1)])==0: return True
    return False
def steps_to_zero(S,maxit=500):
    A=alpha(S); o=[list(A[0]),list(A[1])]
    e=Esize(S,o); it=0; bad=0
    while e>0 and it<maxit:
        cands=[]
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                cands.append((Esize(S,p),p))
        cands.sort(key=lambda t:t[0])
        if cands[0][0]<e: e,o=cands[0]; bad=0
        else:
            bad+=1
            if bad>3: return None
            e,o=random.choice(cands[:max(2,len(cands)//2)])
        it+=1
    return it if e==0 else None
DATA=[]
for _ in range(2500):
    nr=random.randint(2,6); nc=random.randint(2,6)
    A=[list(range(nr)),list(range(nc))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    if len(Aa[0])>5 or len(Aa[1])>5:
        ok=None
    else:
        ok=reorderable(S)
        if not ok: continue
    st=steps_to_zero(S)
    if st is None: continue
    dr=len({v for v in sup_of(S).values()})
    DATA.append((dr,len(Aa[0]),len(Aa[1]),st))
print("     usable instances : %d"%len(DATA))
print("\n  %14s%8s%14s%12s%12s"%("distinct rows","n","mean steps","max steps","p95"))
print("  "+"-"*62)
for d in sorted({x[0] for x in DATA}):
    g=[x[3] for x in DATA if x[0]==d]
    if len(g)>=8:
        print("  %14d%8d%14.2f%12d%12.0f"%(d,len(g),np.mean(g),max(g),np.percentile(g,95)))
D=np.array([x[0] for x in DATA],float); ST=np.array([x[3] for x in DATA],float)
print("\n     corr(distinct rows, steps) : %+.3f"%np.corrcoef(D,ST)[0,1])
m=D>0
for name,tr in [("linear     steps ~ a·d",D),("quadratic  steps ~ a·d²",D**2),("cubic      steps ~ a·d³",D**3)]:
    a=np.polyfit(tr[m],ST[m],1)
    pred=np.polyval(a,tr[m])
    ss=1-np.sum((ST[m]-pred)**2)/np.sum((ST[m]-ST[m].mean())**2)
    print("     %-26s R² = %.3f"%(name,ss))
print("="*88)
print("  AND THE DECISIVE QUESTION — DOES max STEPS GROW POLYNOMIALLY?")
print("="*88)
mx=[]; ds=sorted({x[0] for x in DATA})
for d in ds:
    g=[x[3] for x in DATA if x[0]==d]
    if len(g)>=8: mx.append((d,max(g)))
if len(mx)>=3:
    dd=np.array([a for a,_ in mx],float); mm=np.array([b for _,b in mx],float)
    print("\n  %14s%12s%16s"%("distinct rows","max steps","max / d²"))
    for a,b in mx: print("  %14d%12d%16.3f"%(a,b,b/(a*a)))
    lg=np.polyfit(np.log(dd),np.log(np.maximum(mm,1)),1)
    print("\n     log-log slope of max steps vs distinct rows : %.2f"%lg[0])
    print("""
  **A slope near or below 2 means the worst case grows no faster than the
  square of the row count** — which would be a polynomial bound. A slope
  that climbs with the range means it does not.
""")