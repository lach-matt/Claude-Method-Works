import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(431)
print("="*90)
print("  WHICH OF TODAY'S BOUNDS WERE SEED-INDEPENDENT BREAKS ALL ALONG?")
print("="*90)
print("""
  A break is a quantity invariant under relabelling of the axes. **Checking
  the twenty-one bounds against that definition:**
""")
T=[("chain of row supports","**fibre containment at d = 2**","YES — break #2, named"),
   ("C1P-ness","a decision, invariant under relabelling","YES"),
   ("width ≤ 2 per container","the containment poset only","YES"),
   ("≤ 2 immediate children","the containment forest only","YES"),
   ("overlap components ≤ 2","overlap is a set relation","YES"),
   ("distinct row supports (§23.3)","a count of distinct fibres","YES"),
   ("nesting pairs / overlap pairs","set relations","YES"),
   ("**the arity k per pair**","axes on which two cells differ","YES — and complete-ish"),
   ("**the corner-presence pattern**","which corners of a pair's box are in X","YES — the CSP itself"),
   ("Γ-free / totally balanced","a decision, invariant","YES"),
   ("row/col-deleted sub-instances","invariant","YES"),
   ("E as a potential","**depends on the order**","no"),
   ("descent steps","depends on the seed","no"),
   ("join/meet failure counts","depend on the order","no"),
   ("cyclomatic k of the binding graph","φ needs an order","no"),
   ("frontier count of a PQ-tree","tree built from set relations","YES"),
   ("anchor-completeness","a property of the tree","YES")]
print("  %-34s%-42s%s"%("bound","what it actually measures","invariant?"))
print("  "+"-"*104)
for a,b,c in T: print("  %-34s%-42s%s"%(a[:34],b[:42],c))
yes=sum(1 for *_,c in T if c.startswith("YES"))
print("\n     **%d of %d were seed-independent invariants.** I treated them as"%(yes,len(T)))
print("     candidate criteria and never as a family of breaks.")
print("="*90)
print("  AND THE COMPLETE ONE: THE CORNER-PRESENCE PATTERN")
print("="*90)
print("""
  For each pair x,y let I = the axes where they differ, and record WHICH of
  the 2^|I| corners of their box lie in X. **That is exactly the CSP's
  constraint set, and it is relabelling-invariant.**

  Every other break is a summary of it:
     fibre cardinality   — counts cells, forgets corners
     fibre containment   — one bit per fibre pair
     arity k             — |I| only, forgets which corners
     overlap components  — connectivity of the pattern

  **Test whether it DETERMINES reorderability.**
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
def reord(S,d):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>10**6: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def corner_sig(S,d):
    """canonical, relabelling-invariant signature of the corner pattern"""
    Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=tuple(i for i in range(d) if x[i]!=y[i])
        if not I: continue
        pat=[]
        for bits in product([0,1],repeat=len(I)):
            c=list(x)
            for t,i in enumerate(I): c[i]= y[i] if bits[t] else x[i]
            pat.append(1 if tuple(c) in Ss else 0)
        out.append((len(I),tuple(sorted(pat))))
    return tuple(sorted(out))
print("  build classes of instances sharing a corner signature, then check")
print("  whether reorderability is constant within each class:\n")
from collections import defaultdict
cls=defaultdict(list)
for _ in range(2500):
    d=3; a=random.choice([2,3])
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,d)
    if any(len(x)<2 for x in Aa): continue
    rr=reord(S,d)
    if rr is None: continue
    cls[corner_sig(S,d)].append(rr)
multi=[v for v in cls.values() if len(v)>1]
mixed=[v for v in multi if len(set(v))>1]
print("     signatures seen           : %d"%len(cls))
print("     signatures with >1 instance : %d"%len(multi))
print("     of those, MIXED verdicts  : %d"%len(mixed))
print("     **corner signature determines reorderability : %s**"%(len(mixed)==0))
if mixed: print("     (so it is a summary, not the complete invariant)")