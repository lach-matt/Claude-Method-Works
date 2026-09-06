import numpy as np, random
from itertools import product, permutations
random.seed(137)
print("="*88)
print("  IS THE CAVEAT REAL?")
print("="*88)
print("""
  The theorem says: reorderable iff SOME column order gives interval rows
  with monotone endpoints. **If every C1P order works whenever one does,
  there is no search and the caveat vanishes. If not, it is real.**
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def c1p_orders(S):
    A=alpha(S); out=[]
    for pc in permutations(A[1]):
        ic={v:i for i,v in enumerate(pc)}
        sp={}; ok=True
        for r in A[0]:
            s=sorted(ic[c] for (a,c) in S if a==r)
            if not s or s!=list(range(s[0],s[0]+len(s))): ok=False; break
            sp[r]=(s[0],s[-1])
        if ok: out.append((pc,sp))
    return out
def monotone(sp,A0):
    order=sorted(A0,key=lambda r:sp[r])
    lo=[sp[r][0] for r in order]; hi=[sp[r][1] for r in order]
    return all(lo[i]<=lo[i+1] for i in range(len(lo)-1)) and all(hi[i]<=hi[i+1] for i in range(len(hi)-1))
allwork=0; somework=0; n=0; split=[]
for _ in range(4000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    ords=c1p_orders(S)
    if not ords: continue
    A0=alpha(S)[0]
    flags=[monotone(sp,A0) for _,sp in ords]
    if not any(flags): continue
    n+=1
    if all(flags): allwork+=1
    else:
        somework+=1
        if len(split)<3: split.append((sorted(S),len(ords),sum(flags)))
print("     instances where SOME C1P order is monotone : %d"%n)
print("     of those, EVERY C1P order is monotone      : %d  (%.1f%%)"%(allwork,100*allwork/max(n,1)))
print("     only SOME orders work                      : %d  (%.1f%%)"%(somework,100*somework/max(n,1)))
if split:
    print("\n     instances where the choice matters:")
    for S,tot,good in split:
        print("       X=%-46s  %d C1P orders, %d monotone"%(str(S)[:46],tot,good))
print("="*88)
print("  SO THE CAVEAT IS %s"%("REAL" if somework else "NOT REAL"))
print("="*88)
if somework:
    print("""
  **A C1P column order can exist and fail the endpoint test while another
  C1P order passes it.** So the decision is not 'test C1P, then sort' — it
  is 'search the C1P orders for one that sorts', and PQ-trees represent
  those orders as a tree with exponentially many leaves.

  **The characterisation is proved. The decision problem is NOT settled**,
  because no polynomial search of the PQ-tree has been exhibited.

  **§23.4 must say that**, and the honest status is:

     the CHARACTERISATION  : proved, 10,540 + 3,746 instances, and a proof
     the DECISION PROBLEM  : open — the search over C1P orders is unbounded
     the LITERATURE        : corrected to interval matrices / PQ-trees
""")
    print("="*88)
    print("  AND HOW BIG IS THE SEARCH?")
    print("="*88)
    sizes=[]
    for _ in range(600):
        A=[list(range(random.randint(3,5))),list(range(random.randint(3,5)))]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,len(cells))))
        o=c1p_orders(S)
        if o: sizes.append(len(o))
    if sizes:
        print("\n     C1P orders per instance : median %d   max %d   mean %.1f"
              %(int(np.median(sizes)),max(sizes),np.mean(sizes)))
        print("     (a PQ-tree stores these in linear space; enumerating them is not linear)")
else:
    print("""
  **Every C1P order that exists is monotone whenever any is.** Then the
  procedure is: run PQ-trees to get one C1P order, sort the rows, check.
  **Linear plus a sort, and the decision problem closes.**
""")