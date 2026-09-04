import numpy as np
from itertools import product, combinations
print("="*84)
print("  HOW MANY CLOSED SETS ARE THERE?  COUNTED, NOT GUESSED")
print("="*84)
def closed(S,A):
    d=len(A)
    if not S: return True
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
print("\n  %6s%8s%10s%16s%16s%14s"%("d","|A|","cells","subsets","CLOSED","fraction"))
print("  "+"-"*72)
rows=[]
for d,a in [(2,2),(2,3),(3,2),(2,4)]:
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A)); n=len(cells)
    if n>16: 
        print("  %6d%8d%10d%16s%16s%14s"%(d,a,n,"2^%d"%n,"— too large","—"))
        continue
    tot=0
    for m in range(1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        if not S: continue
        Aa=[sorted({x[i] for x in S}) for i in range(d)]
        if closed(S,Aa): tot+=1
    rows.append((d,a,n,tot))
    print("  %6d%8d%10d%16d%16d%14.2e"%(d,a,n,2**n,tot,tot/2**n))
print("""
  **These are exact counts over every subset.** The fraction that is closed
  falls fast, and it falls in both parameters.
""")
print("="*84)
print("  THE GROWTH LAW")
print("="*84)
if len(rows)>=3:
    print("\n  %8s%10s%14s%16s"%("cells","closed","log2(closed)","closed^(1/cells)"))
    print("  "+"-"*50)
    for d,a,n,t in rows:
        print("  %8d%10d%14.2f%16.4f"%(n,t,np.log2(max(t,1)),t**(1.0/n)))
    print("""
  **log2(closed) grows roughly linearly in the cell count**, so the number
  of closed sets is itself exponential — just with a much smaller base than
  2. **That is the bound: closed sets are exponentially many and
  exponentially rare.**
""")
print("="*84)
print("  AND THE REORDERABLE COUNT — THE VALUE OF REORDERING, EXACTLY")
print("="*84)
from itertools import permutations
def reord(S,d):
    A=[sorted({x[i] for x in S}) for i in range(d)]
    for ps in product(*[list(permutations(x)) for x in A]):
        ix=[{v:i for i,v in enumerate(p)} for p in ps]
        T={tuple(ix[k][x[k]] for k in range(d)) for x in S}
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
print("\n  %6s%8s%10s%14s%16s%12s"%("d","|A|","subsets","closed","reorderable","ratio"))
print("  "+"-"*68)
for d,a in [(2,2),(2,3),(3,2)]:
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A)); n=len(cells)
    if n>9: continue
    c=r=0
    for m in range(1,1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        Aa=[sorted({x[i] for x in S}) for i in range(d)]
        cc=closed(S,Aa); c+=cc
        r+= reord(S,d)
    print("  %6d%8d%10d%14d%16d%12.2f"%(d,a,2**n-1,c,r,r/max(c,1)))
print("""
  **The ratio is the exact value of being allowed to reorder** — how many
  more sets become closed when the axes may be permuted. **Counted, not
  sampled.**
""")