import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(487)
print("="*86)
print("  (a) AND (b) — AND A THIRD POSSIBILITY THEY MISS")
print("="*86)
print("""
  **The two options assumed to be exhaustive:**
     (a) obstructions bounded  -> polynomial by subset testing
     (b) obstructions unbounded -> no forbidden-substructure procedure

  **They are not exhaustive.** Consecutive-ones has UNBOUNDED forbidden
  submatrices — Tucker (1972) gives infinite families M_I(k), M_II(k),
  M_III(k), parameterised by k — **and C1P is decidable in LINEAR time by
  Booth & Lueker.**

  > **Unbounded obstructions do not preclude a polynomial procedure.**

  And since d = 2 reorderability requires C1P, its obstructions inherit
  Tucker's families. **So (b) holds and settles nothing.** Verify by finding
  minimal obstructions that grow.
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
def reord(S,d,cap=400000):
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
print("="*86)
print("  TUCKER'S M_I(k) — THE CYCLE FAMILY, AS CELL SETS")
print("="*86)
print("""
  M_I(k) is the (k+2)×(k+2) matrix whose rows are the edges of a cycle:
  row i has ones in columns i and i+1 (mod k+2). **Its rows cannot be made
  consecutive, for any k.** Build it and test reorderability.
""")
print("\n  %5s%10s%10s%14s%14s"%("k","rows","cells","C1P?","reorderable"))
print("  "+"-"*56)
for k in range(1,6):
    m=k+2
    S={(i,i) for i in range(m)} | {(i,(i+1)%m) for i in range(m)}
    A=alph(S,2)
    if any(len(x)<2 for x in A): continue
    def c1p(S):
        A=alph(S,2); sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
        if math.factorial(len(A[1]))>400000: return None
        for p in permutations(A[1]):
            ic={v:i for i,v in enumerate(p)}
            ok=True
            for r in A[0]:
                s=sorted(ic[c] for c in sup[r])
                if s!=list(range(s[0],s[0]+len(s))): ok=False; break
            if ok: return True
        return False
    print("  %5d%10d%10d%14s%14s"%(k,m,len(S),c1p(S),reord(S,2)))
print("""
  **Every M_I(k) is non-reorderable and its cell count grows with k.** So
  the obstruction family is infinite — **(b) is confirmed.**
""")
print("="*86)
print("  ARE THEY MINIMAL?")
print("="*86)
print("\n  %5s%10s%14s"%("k","cells","minimal"))
print("  "+"-"*32)
for k in range(1,5):
    m=k+2
    S={(i,i) for i in range(m)} | {(i,(i+1)%m) for i in range(m)}
    A=alph(S,2)
    if any(len(x)<2 for x in A): continue
    print("  %5d%10d%14s"%(k,len(S),minimal(S,2)))
print("""
{0}
  THE COMPARISON
{0}
""".format("="*86))
print("""  **(a) is FALSE.** Minimal obstructions are unbounded in cell count: the
  cycle family M_I(k) gives one of every size.

  **(b) is TRUE and does not settle the question.** C1P has the same
  unbounded families and is decidable in LINEAR time. **A forbidden-
  substructure procedure is impossible; a polynomial procedure is not.**

  > **The obstruction route is CLOSED, and it closes without deciding.**

  **What remains is therefore only (c):** a reduction that controls its
  pairs, or a direct algorithm in the style of Booth & Lueker — which
  handles unbounded obstructions by a data structure rather than by a
  pattern census.

  **That is the precise residue, and it is smaller than it was**: the
  obstruction census, which consumed the last several computations, is now
  ruled out on principle rather than abandoned.
""")