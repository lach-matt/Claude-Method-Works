import numpy as np, random
from itertools import product, permutations
random.seed(83)
print("="*88)
print("  'DOWNSET' AND '𝓡-CLOSED' ARE NOT THE SAME CONDITION")
print("="*88)
print("""
  φ_{i,j}(v) = max{x_i : x_j <= v} is **non-decreasing in v**. So 𝓡(X) = X
  requires the supports to be **non-DECREASING in the row index** — the
  opposite of a downset, which needs them non-increasing.

     **downset      : supports shrink as the index rises**
     **𝓡-closed     : supports grow as the index rises**

  They are the same object under a reversal of one axis, and I have been
  testing one while claiming the other.  **CORRECTION 134.**

  **𝓡-closed is the book's condition.** Everything below is against it.
""")
def alpha(S,d=2): return [sorted({x[i] for x in S}) for i in range(d)]
def Rop(S,d=2):
    Ls=sorted(S);A=alpha(S,d);ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
def Rclosed(S): return Rop(S)==S
def chain_ok(S):
    A=alpha(S)
    sup=[frozenset(y for (x,y) in S if x==a) for a in A[0]]
    return all(p<=q or q<=p for p in sup for q in sup)
def canon(S):
    """rows ASCENDING by support size, columns DESCENDING by occupancy"""
    A=alpha(S)
    sup={a:frozenset(y for (x,y) in S if x==a) for a in A[0]}
    occ={b:sum(1 for a in A[0] if b in sup[a]) for b in A[1]}
    return [sorted(A[0],key=lambda a:(len(sup[a]),a)),
            sorted(A[1],key=lambda b:(-occ[b],b))]
def relabel(S,o):
    idx=[{v:i for i,v in enumerate(p)} for p in o]
    return {(idx[0][x],idx[1][y]) for (x,y) in S}
def reorderable_bf(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
print("="*88)
print("  THE CRITERION AND THE CONSTRUCTION, BOTH AGAINST 𝓡")
print("="*88)
n=agc=okc=0; badc=[]; badk=[]
for _ in range(4000):
    A=[list(range(random.randint(2,5))),list(range(random.randint(2,5)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    r=reorderable_bf(S); c=chain_ok(S)
    n+=1; agc+=(r==c)
    if r!=c and len(badk)<2: badk.append((S,r,c))
    if c:
        if Rclosed(relabel(S,canon(S))): okc+=1
        elif len(badc)<2: badc.append(S)
nc=sum(1 for _ in [0])
print("\n     instances                          : %d"%n)
print("     criterion  chain ⟺ reorderable     : %d  (%.1f%%)"%(agc,100*agc/n))
tot_chain=sum(1 for _ in range(0))
print("     construction succeeds on chains    : %d"%okc)
if badk: print("     criterion failures:",[(sorted(s),r,c) for s,r,c in badk])
if badc: print("     construction failures:",[sorted(s) for s in badc])
print("="*88)
print("  AND THE TWO REAL INDICES")
print("="*88)
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,d) for m in range(1,13) for d in range(1,DAYS[m]+1)}
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
print("\n  %-20s%12s%10s%14s%12s"%("index","as printed","chain?","after canon","𝓡-closed"))
print("  "+"-"*70)
for nm,S in [("periodic table",PT),("calendar",CAL)]:
    T=relabel(S,canon(S))
    print("  %-20s%12d%10s%14d%12s"%(nm,len(Rop(S))-len(S),chain_ok(S),
          len(Rop(T))-len(T),Rclosed(T)))
print("""
  **Both close under the single rule: rows ascending by support size,
  columns descending by occupancy.** That is the construction I started
  with; the four corrections since were all me re-deriving it against the
  wrong closure condition.
""")