import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(569)
print("="*88)
print("  IS THE RESIDUE AN INTERVAL?")
print("="*88)
print("""
  **An interval [a,b] in a lattice is determined by two elements.** If the
  undecided instances form an interval under INCLUSION — X ⊆ Y ⊆ Z with X, Z
  undecided implies Y undecided — then the residue is characterised by its
  endpoints, and the problem shrinks to two objects.

  **Test the convexity directly.**
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
print("="*88)
print("  TEST 1 — IS REORDERABILITY MONOTONE UNDER INCLUSION?")
print("="*88)
print("""
  **The prior question.** If X ⊆ Y and Y is reorderable, is X? (Yes — that is
  the SUBLATTICE rule, measured 100%.) **And if X is NOT reorderable, is Y
  not?** That would make non-reorderability upward-closed, and the two
  classes would be an up-set and a down-set — **an interval structure by
  construction.**
""")
n=up=dn=0; exu=[]
for _ in range(1200):
    d=3; a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    Y=set(random.sample(cl,random.randint(4,min(len(cl),8))))
    AY=alph(Y,d)
    if any(len(x)<2 for x in AY): continue
    rY=reord(Y,d)
    if rY is None: continue
    X=set(random.sample(sorted(Y),len(Y)-1))
    AX=alph(X,d)
    if any(len(x)<2 for x in AX): continue
    rX=reord(X,d)
    if rX is None: continue
    n+=1
    if rY is True and rX is True: dn+=1
    if rX is False and rY is False: up+=1
    if rX is False and rY is True and len(exu)<3: exu.append((sorted(X),sorted(Y)))
tot_y=n
print("     pairs X ⊂ Y tested : %d"%n)
print("     Y reorderable AND X reorderable      : %d"%dn)
print("     X NOT reorderable AND Y NOT          : %d"%up)
print("     **X NOT but Y IS  (breaks upward-closure) : %d**"%len(exu))
for X,Y in exu[:2]:
    print("        X=%s"%str(X)[:44])
    print("        Y=%s"%str(Y)[:44])
print("="*88)
print("  TEST 2 — SO WHAT IS THE TRUE SHAPE OF THE CLASSES?")
print("="*88)
print("""
  Count the four cases on X ⊂ Y with |Y| = |X| + 1.
""")
cases={(True,True):0,(True,False):0,(False,True):0,(False,False):0}
n=0
for _ in range(1500):
    d=3; a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    Y=set(random.sample(cl,random.randint(4,min(len(cl),8))))
    AY=alph(Y,d)
    if any(len(x)<2 for x in AY): continue
    rY=reord(Y,d)
    if rY is None: continue
    z=random.choice(sorted(Y)); X=Y-{z}
    AX=alph(X,d)
    if any(len(x)<2 for x in AX): continue
    rX=reord(X,d)
    if rX is None: continue
    n+=1; cases[(rX is True,rY is True)]+=1
print("\n  %-30s%10s%10s"%("X reorderable / Y reorderable","count","rate"))
print("  "+"-"*52)
for k,v in cases.items():
    print("  %-30s%10d%9.3f"%("%s / %s"%k,v,v/max(n,1)))
print("""
  **(False, True) is the case that breaks convexity** — removing a cell makes
  a reorderable set non-reorderable. **Its rate is the answer to whether the
  classes are interval-shaped.**
""")
print("="*88)
print("  WHAT AN INTERVAL WOULD HAVE GIVEN")
print("="*88)
print("""
  **If reorderability were monotone under inclusion**, the two classes would
  be a down-set and an up-set, the boundary would be an ANTICHAIN, and by
  Dilworth/Sperner the boundary would be characterised by its minimal
  non-reorderable elements — **exactly the minimal obstructions.**

  **And Tucker already told us those are unbounded.** So the boundary
  antichain is infinite, and an interval characterisation would have needed
  infinitely many endpoints.

  > **An interval tells us: closed, E = 0, two determining elements. The
  > residue is not one — and the reason is the same unbounded family that
  > closed the obstruction route.**
""")