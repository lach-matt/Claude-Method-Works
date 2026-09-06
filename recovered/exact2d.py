import numpy as np
from itertools import product
print("="*84)
print("  COUNTING CLOSED SETS AT d = 2 WITHOUT ENUMERATING SUBSETS")
print("="*84)
print("""
  A closed set is exactly {(i,j) : j ≤ M*(i) and i ≤ N*(j)} with M*, N*
  non-decreasing. **So enumerate the bound pairs, not the 2^(rc) subsets.**

     monotone M* : r values into {−1,…,c−1}   -> C(r+c, r) of them
     monotone N* : c values into {−1,…,r−1}

  Form the set, deduplicate. **Exact, and polynomial in the count rather
  than in 2^(rc).**
""")
def monos(k,hi):
    """non-decreasing sequences of length k with values in -1..hi-1"""
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def count_closed(r,c,cap=400000):
    seen=set(); M=monos(r,c); N=monos(c,r)
    if len(M)*len(N)>cap: return None,len(M)*len(N)
    for m in M:
        for n in N:
            S=frozenset((i,j) for i in range(r) for j in range(c) if j<=m[i] and i<=n[j])
            if S: seen.add(S)
    return len(seen),len(M)*len(N)
print("  %6s%6s%8s%16s%16s%10s"%("r","c","cells","bound pairs","CLOSED sets","b"))
print("  "+"-"*66)
res=[]
for r,c in [(2,2),(2,3),(3,3),(2,4),(3,4),(4,4),(2,5),(3,5),(4,5),(5,5),(4,6),(5,6),(6,6)]:
    n=r*c
    k,pairs=count_closed(r,c)
    if k is None:
        print("  %6d%6d%8d%16d%16s%10s"%(r,c,n,pairs,"— too many","—")); continue
    b=k**(1.0/n); res.append((r,c,n,k,b))
    print("  %6d%6d%8d%16d%16d%10.4f"%(r,c,n,pairs,k,b))
print("="*84)
print("  CHECK AGAINST THE BRUTE-FORCE COUNTS")
print("="*84)
KNOWN={(2,2):12,(3,3):146,(4,4):2102}
print()
for k,v in KNOWN.items():
    got=[t[3] for t in res if (t[0],t[1])==k]
    if got: print("     r=%d c=%d : counted %d   brute force %d   **%s**"%(k[0],k[1],got[0],v,"match" if got[0]==v else "MISMATCH"))
print("="*84)
print("  THE LAW, ON MORE POINTS")
print("="*84)
if len(res)>=8:
    ns=np.array([t[2] for t in res],float); cs=np.array([t[3] for t in res],float)
    lc=np.log(cs)
    print("\n  %-18s%10s"%("model for log(closed)","R²"))
    print("  "+"-"*30)
    best=None
    for lab,x in [("n",ns),("n log n",ns*np.log(ns)),("n^0.75",ns**0.75),
                  ("sqrt(n)",np.sqrt(ns)),("n^0.5 log n",np.sqrt(ns)*np.log(ns))]:
        p=np.polyfit(x,lc,1); pr=np.polyval(p,x)
        r2=1-np.sum((lc-pr)**2)/np.sum((lc-lc.mean())**2)
        print("  %-18s%10.4f"%(lab,r2))
        if best is None or r2>best[1]: best=(lab,r2)
    print("\n     best fit : %s  (R² = %.4f)   on %d exact points"%(best[0],best[1],len(res)))
    print("\n  b by cell count:")
    for r,c,n,k,b in sorted(res,key=lambda t:t[2]): print("     n=%2d  b=%.4f  (%dx%d)"%(n,b,r,c))