import random
from itertools import product, permutations, combinations
random.seed(719)
print("="*90)
print("  DOES REORDERABILITY DEPEND ONLY ON THE PARTITION SYSTEM?")
print("="*90)
print("""
  **The labelling-independent data of X is d PARTITIONS of X** — cells grouped
  by their value on each axis. A relabelling permutes the blocks of each
  partition and nothing else.

  **If two cell sets with isomorphic partition systems always agree on
  reorderability, the problem reduces to a question about d partitions** —
  and that is the object Siggers' correspondence is about.
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
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def partsig(S,d):
    """canonical form of the partition system: for each axis, the multiset of
       blocks written as sets of cell-indices, canonicalised over cell relabelling"""
    cs=sorted(S); idx={c:i for i,c in enumerate(cs)}
    best=None
    for perm in permutations(range(len(cs))):
        sysd=[]
        for i in range(d):
            blocks=set()
            for v in {x[i] for x in S}:
                blocks.add(frozenset(perm[idx[x]] for x in S if x[i]==v))
            sysd.append(frozenset(blocks))
        cand=tuple(sorted(map(lambda b: tuple(sorted(map(lambda s: tuple(sorted(s)), b))), sysd)))
        if best is None or cand<best: best=cand
    return best
from collections import defaultdict
print("="*90)
print("  TEST — GROUP BY PARTITION SIGNATURE")
print("="*90)
for d,a,lim,mx in [(2,3,900,6),(3,2,700,6),(3,3,400,6)]:
    cls=defaultdict(set)
    for _ in range(lim):
        cells=list(product(*[range(a)]*d))
        S=set(random.sample(cells,random.randint(3,min(len(cells),mx))))
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        try: sg=partsig(S,d)
        except Exception: continue
        cls[sg].add(reord(S,d))
    multi=[v for v in cls.values() if len(v)>1]
    print("\n     d=%d |A|=%d : %d partition classes    MIXED : %d"%(d,a,len(cls),len(multi)))
    print("        -> reorderability determined by the partition system : %s"%(len(multi)==0))
print("="*90)
print("  AND THE DILWORTH TEST — IS width(J(X)) ≤ d NECESSARY?")
print("="*90)
print("""
  If X is reorderable then under the valid order it IS a distributive lattice,
  and by Larson/Siggers a TIGHT embedding into d chains needs a chain
  decomposition of J(X) into d chains — **so width(J(X)) ≤ d.**
""")
def joinirr(T,d):
    Ts=set(T); J=[]
    for x in Ts:
        below=[y for y in Ts if all(y[i]<=x[i] for i in range(d)) and y!=x]
        if not below: continue
        if tuple(max(y[i] for y in below) for i in range(d))!=x: J.append(x)
    return J
def width(P,d):
    if not P: return 0
    inc=[(x,y) for x,y in combinations(P,2)
         if not all(x[i]<=y[i] for i in range(d)) and not all(y[i]<=x[i] for i in range(d))]
    best=1
    for k in range(2,min(len(P),6)+1):
        for T in combinations(P,k):
            if all((x,y) in inc or (y,x) in inc for x,y in combinations(T,2)): best=max(best,k)
    return best
n=ok=0; viol=[]
for _ in range(500):
    d=random.choice([2,3]); a=random.choice([2,3])
    cells=list(product(*[range(a)]*d))
    S=set(random.sample(cells,random.randint(3,min(len(cells),7))))
    if any(len({x[k] for x in S})<2 for k in range(d)): continue
    A=alph(S,d); found=None
    for ps in product(*[list(permutations(x)) for x in A]):
        T=relab(S,[list(p) for p in ps],d)
        if lat(T,d): found=T; break
    if found is None: continue
    n+=1
    J=joinirr(found,d); w=width(J,d)
    if w<=d: ok+=1
    elif len(viol)<3: viol.append((sorted(found),w,d))
print("\n     reorderable instances : %d      width(J(X)) ≤ d : %d  (%.1f%%)"%(n,ok,100*ok/max(n,1)))
for T,w,d in viol: print("        width %d > d=%d : %s"%(w,d,str(T)[:44]))