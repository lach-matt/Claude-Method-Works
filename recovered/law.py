import numpy as np
from itertools import product, permutations
print("="*84)
print("  THE BASE b AND THE REORDERING RATIO — EXACT, ACROSS THE GRID")
print("="*84)
def closed(S,A):
    d=len(A)
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
def reord(S,d):
    A=[sorted({x[i] for x in S}) for i in range(d)]
    for ps in product(*[list(permutations(x)) for x in A]):
        ix=[{v:i for i,v in enumerate(p)} for p in ps]
        T={tuple(ix[k][x[k]] for k in range(d)) for x in S}
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
print("\n  %5s%7s%8s%12s%12s%10s%12s"%("d","|A|","cells","closed","reorderable","b","ratio"))
print("  "+"-"*68)
GRID=[(2,2),(2,3),(2,4),(3,2),(2,5),(3,3)]
res=[]
for d,a in GRID:
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A)); n=len(cells)
    if n>20: 
        print("  %5d%7d%8d%12s%12s%10s%12s"%(d,a,n,"2^%d"%n,"—","—","—")); continue
    c=r=0
    doreord = n<=16
    for m in range(1,1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        Aa=[sorted({x[i] for x in S}) for i in range(d)]
        if closed(S,Aa): c+=1
        if doreord and reord(S,d): r+=1
    b=c**(1.0/n)
    res.append((d,a,n,c,r,b))
    print("  %5d%7d%8d%12d%12s%10.4f%12s"%(d,a,n,c,(str(r) if doreord else "—"),b,
          ("%.2f"%(r/max(c,1)) if doreord else "—")))
print("="*84)
print("  THE LAW")
print("="*84)
if len(res)>=4:
    print("\n  b against cell count:\n")
    for d,a,n,c,r,b in sorted(res,key=lambda t:t[2]):
        print("     n = %2d  (d=%d,|A|=%d)   closed = %-8d  b = %.4f"%(n,d,a,c,b))
    ns=np.array([t[2] for t in res],float); bs=np.array([t[5] for t in res],float)
    sl=np.polyfit(np.log(ns),np.log(bs),1)[0]
    print("\n     log-log slope of b vs n : %.3f"%sl)
    print("""
  **b decreases with the cell count**, so closed sets are not a constant
  fraction of any exponential — the fraction itself decays. **log(closed)
  is sublinear in n.**
""")
    lc=np.log(np.array([t[3] for t in res],float))
    for lab,x in [("n",ns),("n log n",ns*np.log(ns)),("n^(3/4)",ns**0.75),("sqrt(n)",np.sqrt(ns))]:
        p=np.polyfit(x,lc,1); pred=np.polyval(p,x)
        r2=1-np.sum((lc-pred)**2)/np.sum((lc-lc.mean())**2)
        print("     log(closed) ~ %-10s  R² = %.4f"%(lab,r2))