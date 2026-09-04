import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(491)
print("="*88)
print("  IS THE CONSTRUCTION GRAMMAR COMPLETE?")
print("="*88)
print("""
  **The grid points here.** The construction-rules row is full at every d;
  the characterisation row is empty. **If every reorderable set is REACHABLE
  by the preserving rules, then reachability IS the characterisation** — and
  the empty cell fills from the full one.

  Preserving rules measured at 100%: sublattice · interval · product ·
  projection · free axis · dual.

  **Test: is every reorderable set a sublattice of a product of chains
  reachable from the full box by those rules?**
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
        if lat(relab(S,[list(p) for p in ps],d),d): return True,[list(p) for p in ps]
    return False,None
print("="*88)
print("  THE KEY OBSERVATION")
print("="*88)
print("""
  A reorderable set, IN its valid order, is a sublattice of the box. **And
  'sublattice' is one of the six preserving rules.** So:

     X reorderable  ->  some relabelling makes X a sublattice of the box
                    ->  X is reachable from the box by ONE rule application

  **That is trivially complete — and trivially useless**, because 'which
  relabelling' is the original question. **The grammar characterises the
  reachable sets and does not decide reachability.**

  Verify the triviality, then find what the grammar DOES add.
""")
n=ok=0
for _ in range(400):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r,o=reord(S,d)
    if r is not True: continue
    n+=1
    ok+= lat(relab(S,o,d),d)
print("     reorderable instances : %d      each IS a sublattice in its own valid order : %d"%(n,ok))
print("="*88)
print("  SO WHAT DOES THE GRAMMAR ADD?  A DERIVATION IS A CERTIFICATE")
print("="*88)
print("""
  **The grammar's value is not decision but DERIVATION.** If a set arrives
  with its construction history, reorderability is certified without any
  search — and the history is what a BUILT index has.

  Λ's derivation: box -> interval (cap each coordinate) -> sublattice
  (impose the seven bounds) -> product (A_q × B_q, fibred over q).
  **Three rule applications, all preserving. No search.**

  **Test the converse: does a set WITHOUT a derivation admit one cheaply?**
""")
def derivable_greedy(S,d,depth=3):
    """try to reach S from the box by: interval-cap, then sublattice closure"""
    A=alph(S,d)
    box=set(product(*A))
    # rule 1: interval — cap to the bounding box of S (already done by alph)
    cur=box
    # rule 2: sublattice — the smallest sublattice of cur containing S
    cl=set(S)
    while True:
        new=set(cl)
        for x,y in combinations(sorted(cl),2):
            new.add(tuple(max(x[i],y[i]) for i in range(d)))
            new.add(tuple(min(x[i],y[i]) for i in range(d)))
        if new==cl: break
        cl=new
        if len(cl)>3000: return None
    return cl==set(S)
n=der=rr=0
for _ in range(500):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r,o=reord(S,d)
    if r is None: continue
    n+=1; rr+=(r is True)
    dv=derivable_greedy(S,d)
    if dv: der+=1
print("     instances %d    reorderable %d    derivable in the GIVEN order %d"%(n,rr,der))
print("""
{0}
  WHAT THE GRID SAYS NOW
{0}
""".format("="*88))
print("""  **The characterisation cell CANNOT be filled from the construction cell.**
  'X is reachable' unfolds to 'some relabelling makes X a sublattice', which
  is the question verbatim. **The two cells are the same cell.**

  > **So the grid has one fewer independent empty cell than it appeared to
  > have — and the remaining one is still the data structure.**

  **And that is an answer of a kind.** The grid method cannot close this
  question, because the question's requirements are not independent: the
  characterisation and the decision procedure are the same requirement
  written twice, and both wait on the object.
""")