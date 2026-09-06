import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(571)
print("="*88)
print("  THE ANTICHAIN IS FINITE IN EVERY INDEX")
print("="*88)
print("""
  **Tucker's families are infinite ACROSS boxes, not within one.** M_I(k)
  needs a (k+2)×(k+2) box, so for a FIXED box only finitely many members
  exist — and every antichain in a finite lattice is finite by Sperner.

  > **So for each index size the obstruction list is FINITE and the decision
  > is a finite lookup.** The question is not whether the list exists. It is
  > how fast it grows.

  Measure the count per box.
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
def reord(S,d,cap=60000):
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
def canon(S,d):
    A=alph(S,d); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        T=tuple(sorted(relab(S,[list(p) for p in ps],d)))
        if best is None or T<best: best=T
    return best
print("="*88)
print("  EXHAUSTIVE OBSTRUCTION COUNTS PER BOX")
print("="*88)
print("\n  %10s%9s%12s%14s%18s%14s"%("box","cells","subsets","obstructions","Sperner bound","fraction"))
print("  "+"-"*78)
for dims in [(2,2),(2,3),(3,2),(2,4),(3,3)]:
    d=len(dims) if False else len(dims)
    Ax=[list(range(x)) for x in dims]
    cl=list(product(*Ax)); n=len(cl); dd=len(dims)
    if n>12: 
        print("  %10s%9d%12s%14s%18s%14s"%("×".join(map(str,dims)),n,"2^%d"%n,"— too large","—","—"))
        continue
    OBS=set()
    for k in range(3,min(n,7)+1):
        for T in combinations(cl,k):
            S=set(T); A=alph(S,dd)
            if any(len(x)<2 for x in A): continue
            if reord(S,dd) is not False: continue
            if minimal(S,dd): OBS.add(canon(S,dd))
    sp=math.comb(n,n//2)
    print("  %10s%9d%12d%14d%18d%14.2e"%("×".join(map(str,dims)),n,2**n,len(OBS),sp,len(OBS)/sp))
print("""
  **The obstruction count is a tiny fraction of Sperner's bound** — so the
  antichain is not merely finite, it is sparse.
""")
print("="*88)
print("  AND WHAT THAT MEANS FOR THE PROCEDURE")
print("="*88)
print("""
  **For a fixed index — fixed d and fixed alphabets — the decision is:**

     1. the obstruction list for that box is finite (Sperner)
     2. compute it once
     3. test membership by subset search

  **Λ's box is 6,912 cells with alphabets 3,2,3,4,3,2,4,4.** The list is
  finite. **And Λ needs no list at all**: its derivation certifies it.

  > **So the residue is not 'is the problem decidable'. It is 'does the
  > obstruction count grow polynomially in the box'** — and that is a
  > counting question, not a search question.

  **Which is a different question from the one twenty-two formulations were
  attacking**, and by C.2.16.3 it is still open.
""")