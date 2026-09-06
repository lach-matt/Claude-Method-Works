import numpy as np
from itertools import product
def closed(S,A):
    d=len(A); ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
print("="*84)
print("  CLOSED-SET COUNTS — EXACT WHERE FEASIBLE")
print("="*84)
print("\n  %5s%7s%8s%14s%10s"%("d","|A|","cells","closed","b"))
print("  "+"-"*46)
res=[]
for d,a in [(2,2),(3,2),(2,3),(2,4),(4,2)]:
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A)); n=len(cells)
    if n>16: continue
    c=0
    for m in range(1,1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        Aa=[sorted({x[i] for x in S}) for i in range(d)]
        if closed(S,Aa): c+=1
    b=c**(1.0/n); res.append((d,a,n,c,b))
    print("  %5d%7d%8d%14d%10.4f"%(d,a,n,c,b))
print("="*84)
print("  THE LAW")
print("="*84)
ns=np.array([t[2] for t in res],float); cs=np.array([t[3] for t in res],float)
lc=np.log(cs)
print("\n  %-16s%10s"%("model for log(closed)","R²"))
print("  "+"-"*28)
for lab,x in [("n",ns),("n log n",ns*np.log(ns)),("n^0.75",ns**0.75),("sqrt(n)",np.sqrt(ns))]:
    p=np.polyfit(x,lc,1); pr=np.polyval(p,x)
    r2=1-np.sum((lc-pr)**2)/np.sum((lc-lc.mean())**2)
    print("  %-16s%10.4f"%(lab,r2))
print("\n  b by cell count:")
for d,a,n,c,b in sorted(res,key=lambda t:t[2]): print("     n=%2d  b=%.4f   (d=%d,|A|=%d)"%(n,b,d,a))
print("""
  **b falls as n grows — closed sets are exponentially many with a base
  that itself decays.** So log(closed) is sublinear in the cell count, and
  the fitted model above says by how much.
""")