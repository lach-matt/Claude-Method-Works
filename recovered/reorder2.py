import numpy as np, random
from itertools import permutations
random.seed(43)
print("="*86)
print("  THE CONJECTURE WAS WRONG.  FINDING THE RIGHT CONDITION.")
print("="*86)
print("""
  Γ-free is NECESSARY but not sufficient: the identity matrix is Γ-free and
  is not a staircase. **Correction 123.**

  **The right condition is visible from what a staircase IS.** In a Young
  diagram, row i's support CONTAINS row i+1's — the row supports form a
  CHAIN under inclusion. Sorting by size then realises it.
""")
def closed_2d(M):
    for i in range(M.shape[0]):
        o=np.where(M[i]==1)[0]
        if len(o) and not np.array_equal(o,np.arange(len(o))): return False
    for j in range(M.shape[1]):
        o=np.where(M[:,j]==1)[0]
        if len(o) and not np.array_equal(o,np.arange(len(o))): return False
    return True
def reorderable_bf(M):
    r,c=M.shape
    for pr in permutations(range(r)):
        Mr=M[list(pr),:]
        for pc in permutations(range(c)):
            if closed_2d(Mr[:,list(pc)]): return True
    return False
def chain_test(M):
    """row supports totally ordered by inclusion"""
    sup=[frozenset(np.where(M[i]==1)[0]) for i in range(M.shape[0])]
    for a in sup:
        for b in sup:
            if not (a<=b or b<=a): return False
    return True
print("  %8s%9s%16s%14s%10s"%("size","tested","reorderable","chain test","agree"))
print("  "+"-"*58)
TOT=0; AG=0; ex=[]
for r,c in [(3,3),(3,4),(4,4),(4,5),(5,5)]:
    t=ag=nr=0
    for _ in range(120):
        M=np.random.randint(0,2,(r,c))
        a=reorderable_bf(M) if r<=4 and c<=5 else None
        if a is None: continue
        b=chain_test(M); t+=1; ag+=(a==b); nr+=a
        if a!=b and len(ex)<3: ex.append((M.copy(),a,b))
    if t:
        TOT+=t; AG+=ag
        print("  %8s%9d%16d%14s%10s"%("%dx%d"%(r,c),t,nr,"—","%d/%d"%(ag,t)))
print("\n     total %d   agree %d   (%.1f%%)"%(TOT,AG,100*AG/max(TOT,1)))
if ex:
    print("\n  DISAGREEMENTS:")
    for M,a,b in ex:
        print("    reorderable=%s  chain=%s"%(a,b)); print(M); print()
else:
    print("\n  **NO DISAGREEMENTS.**")
print("="*86)
print("  AND THE COLUMN CONDITION IS IMPLIED, NOT SEPARATE")
print("="*86)
print("""
  If the row supports form a chain, the column supports do too — a Young
  diagram is symmetric under transposition of the condition. Verify.
""")
both=0; rowonly=0; n=0
for _ in range(500):
    r,c=random.choice([(3,3),(3,4),(4,4),(4,5),(5,5),(6,4)])
    M=np.random.randint(0,2,(r,c))
    rr=chain_test(M); cc=chain_test(M.T)
    n+=1
    if rr and cc: both+=1
    if rr and not cc: rowonly+=1
print("     rows chain AND cols chain : %d"%both)
print("     rows chain but cols NOT   : %d"%rowonly)
print("     **row condition alone suffices : %s**"%(rowonly==0))
print("="*86)
print("  COMPLEXITY, AND WHAT IT SETTLES")
print("="*86)
print("""
     the test        : compare every pair of row supports for inclusion
     cost            : O(r² c)   -- POLYNOMIAL
     the reordering  : sort rows by support size, columns by column sum

  **§23.4 asks whether reorderability reduces to a known NP-complete
  problem. At d = 2 the answer is that it does not need to: the problem is
  in P**, and the certificate is a chain of row supports.

  **The NP-completeness results the book cites — Stahl & Wille 1984,
  Yannakakis 1982 — are about ORDER DIMENSION and lattice embedding, which
  are different questions.** The book placed reorderability in that family
  by association rather than by reduction.
""")
print("="*86)
print("  DOES IT EXTEND ABOVE d = 2?")
print("="*86)
print("""
  In d dimensions the analogous condition is that for each axis, the
  'slices' orthogonal to it form a chain under inclusion. Test at d = 3.
""")
from itertools import product as iproduct
def closed_d(S,A):
    d=len(A)
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                cc=[x[i] for x in S if x[j]<=v]; run=max(run,max(cc) if cc else -1); f[v]=run
            ph[(i,j)]=f
    return all(x[i]<=ph[(i,j)].get(x[j],-1) for x in iproduct(*A) if x in S for i in range(d) for j in range(d) if i!=j) and \
           len({x for x in iproduct(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)})==len(S)
def slice_chain(S,d,A):
    for i in range(d):
        sl=[frozenset(tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==v) for v in A[i]]
        for a in sl:
            for b in sl:
                if not (a<=b or b<=a): return False
    return True
ag=0; n=0; bad=[]
for _ in range(300):
    A=[list(range(random.randint(2,3))) for _ in range(3)]
    cells=[x for x in iproduct(*A)]
    S=set(random.sample(cells,random.randint(1,len(cells))))
    best=False
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            for p2 in permutations(A[2]):
                mp=[{v:i for i,v in enumerate(p)} for p in (p0,p1,p2)]
                T={(mp[0][x[0]],mp[1][x[1]],mp[2][x[2]]) for x in S}
                AT=[sorted({t[i] for t in T}) for i in range(3)]
                if closed_d(T,AT): best=True; break
            if best: break
        if best: break
    ch=slice_chain(S,3,A)
    n+=1; ag+= (best==ch)
    if best!=ch and len(bad)<3: bad.append((sorted(S),best,ch))
print("     d = 3 : %d tested, %d agree (%.0f%%)"%(n,ag,100*ag/max(n,1)))
if bad:
    print("     disagreements (first): reorderable=%s chain=%s"%(bad[0][1],bad[0][2]))
    print("       ",bad[0][0][:8])