import numpy as np, random, math
from itertools import product, permutations, combinations
from collections import defaultdict, Counter
random.seed(601)
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
def canon(T,d):
    """lexicographically least relabelling — the full isomorphism invariant"""
    A=alph(T,d); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        c=tuple(sorted(relab(T,[list(p) for p in ps],d)))
        if best is None or c<best: best=c
    return best
def sigk(S,d,k):
    """multiset of canonical forms of the k-subsets — FULL structure, not counts"""
    return tuple(sorted(Counter(canon(set(T),d) for T in combinations(sorted(S),k)).items()))
print("="*88)
print("  THE FIXED SIGNATURE — CANONICAL FORMS, NOT FEATURE COUNTS")
print("="*88)
print("""
  **The defect.** My level-k signature recorded (differing axes, join present,
  meet present, inner count). **For a set where every pair differs on every
  axis, those numbers coincide across structurally different sets.**

  **The fix.** Record the ISOMORPHISM CLASS of each k-subset — the
  lexicographically least relabelling. Relabelling-invariant, and it
  discards nothing.
""")
for d,a,lim in [(3,3,1400),(4,2,900)]:
    print("\n  ---- d = %d, |A| = %d ----"%(d,a))
    data=[]
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(d)]
        cl=list(product(*Ax))
        S=set(random.sample(cl,random.randint(3,min(len(cl),8))))
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        r=reord(S,d)
        if r is None: continue
        data.append((S,r))
    print("  %-14s%12s%16s%12s%12s"%("levels","classes","multi-inst","MIXED","purity"))
    print("  "+"-"*62)
    LEV=[("3",lambda S,dd:sigk(S,dd,3)),
         ("3+4",lambda S,dd:(sigk(S,dd,3),sigk(S,dd,4))),
         ("3+4+5",lambda S,dd:(sigk(S,dd,3),sigk(S,dd,4),sigk(S,dd,5)))]
    for nm,f in LEV:
        cls=defaultdict(list)
        for S,r in data:
            try: cls[f(S,d)].append(r)
            except Exception: pass
        multi=[v for v in cls.values() if len(v)>1]
        mixed=[v for v in multi if len(set(v))>1]
        print("  %-14s%12d%16d%12d%12.3f"%(nm,len(cls),len(multi),len(mixed),
              1-len(mixed)/max(len(multi),1)))
    print("     instances : %d"%len(data))
print("="*88)
print("  AND WHAT LEVEL IS NEEDED?")
print("="*88)
print("""
  **The k-subset canonical forms at level k are exactly the 'sub-instance'
  necessary conditions from §23.4** — every k-subset of a reorderable set is
  reorderable, so the multiset of classes is constrained. **This makes that
  generator into a signature.**
""")
data=[]
for _ in range(1600):
    d=3; a=3
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(3,8)))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r=reord(S,d)
    if r is None: continue
    data.append((S,r))
print("\n  %-10s%12s%14s%12s%14s"%("level k","classes","multi-inst","MIXED","purity"))
print("  "+"-"*58)
for k in (3,4,5,6):
    cls=defaultdict(list)
    for S,r in data:
        if len(S)<k: continue
        try: cls[sigk(S,3,k)].append(r)
        except Exception: pass
    multi=[v for v in cls.values() if len(v)>1]
    mixed=[v for v in multi if len(set(v))>1]
    if multi: print("  %-10d%12d%14d%12d%14.3f"%(k,len(cls),len(multi),len(mixed),
                     1-len(mixed)/max(len(multi),1)))