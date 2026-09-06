import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(479)
print("="*88)
print("  ANALYSING WHAT REMAINS")
print("="*88)
print("""
  **First, a correction.** I said the obstruction set 'grows with alphabet
  size, not cell count'. But a k-cell instance has AT MOST k distinct values
  on any axis. **So the alphabet of a minimal obstruction is bounded by its
  cell count**, and the census is parameterised by cells alone.

  The four-cell obstruction on alphabets [2,4,2] is a four-cell instance; its
  '4' comes from four cells taking four values. **It has no image in a
  3×3×3 BOX, but that is a statement about boxes, not about obstructions.**
  CORRECTION 170.

  > **So the only question is: is the minimal obstruction CELL COUNT
  > bounded?**  If yes, the problem is in P — test all k-subsets, each
  > decidable in time bounded by k.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d,cap=10**6):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def minimal(S,d):
    if reord(S,d) is not False: return False
    for z in sorted(S):
        T=S-{z}; A=alph(T,d)
        if any(len(x)<2 for x in A): continue
        if reord(T,d) is False: return False
    return True
print("="*88)
print("  VERIFY: |A_i| ≤ cell count, always")
print("="*88)
bad=0; n=0
for _ in range(400):
    d=3; a=random.randint(2,5)
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(3,7)))
    n+=1
    if max(len(x) for x in alph(S,d))>len(S): bad+=1
print("\n     instances %d    violations %d   **|A_i| ≤ |X| always : %s**"%(n,bad,bad==0))
print("="*88)
print("  IS THE MINIMAL OBSTRUCTION SIZE BOUNDED?")
print("="*88)
print("""
  Search for minimal obstructions in progressively larger boxes and track
  the LARGEST one found. **If it saturates, the problem is in P.**
""")
print("\n  %10s%12s%16s%16s%14s"%("box","found","min size","MAX size","sizes seen"))
print("  "+"-"*74)
for a,kmax,tries in [(3,6,4000),(4,7,4000),(5,8,3500),(6,8,3000)]:
    Ax=[list(range(a)) for _ in range(3)]
    cl=list(product(*Ax))
    sizes=set(); cnt=0
    for _ in range(tries):
        k=random.randint(3,kmax)
        S=set(random.sample(cl,k))
        Aa=alph(S,3)
        if any(len(x)<2 for x in Aa): continue
        r=reord(S,3)
        if r is not False: continue
        if not minimal(S,3): continue
        sizes.add(len(S)); cnt+=1
    if sizes:
        print("  %10s%12d%16d%16d%14s"%("%d³"%a,cnt,min(sizes),max(sizes),sorted(sizes)))
print("""
  **If MAX size stops growing as the box grows, the obstruction set is
  bounded in cells** — and testing all k-subsets for that k decides the
  problem in O(|X|^k). **If it keeps growing, no such k exists.**
""")
print("="*88)
print("  WHAT REMAINS, PRECISELY")
print("="*88)
print("""
  **To close the polynomial question, one of these:**

     (a) a BOUND K on minimal obstruction cell count
         -> then the procedure is: test all subsets of size ≤ K.
            O(|X|^K), polynomial for fixed d.

     (b) a PROOF that minimal obstructions grow without bound
         -> then no forbidden-substructure procedure exists, and the
            twenty-one failures are explained as a theorem

     (c) a reduction from a known NP-hard problem that CONTROLS its pairs
         -> two attempts failed structurally: in a lattice-closure problem
            every pair constrains, so clauses cannot be isolated

  **(a) and (b) are the same computation run far enough.** The table above
  is that computation at four box sizes.
""")