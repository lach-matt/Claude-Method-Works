import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(461)
print("="*88)
print("  THE OBSTRUCTION SET — WHAT A 'NO' LOOKS LIKE")
print("="*88)
print("""
  A YES has a certificate: the order, checkable in O(|X|²).
  **A NO has none at d ≥ 3.** At d = 2 it is a strictly nested interval
  pair — small, local, proved.

  **Question: is there a MINIMAL non-reorderable substructure**, so that
  every NO contains one? That is the Kuratowski form of the question, and it
  is what a co-NP certificate would be.
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
def canon(S,d):
    """canonical form under relabelling — for counting up to isomorphism"""
    A=alph(S,d); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        T=tuple(sorted(relab(S,[list(p) for p in ps],d)))
        if best is None or T<best: best=T
    return best
print("="*88)
print("  1.  MINIMAL NON-REORDERABLE INSTANCES AT d = 3")
print("="*88)
print("""
  An instance is MINIMAL if it is not reorderable and every proper subset
  (that still uses ≥2 values per axis) IS reorderable.
""")
def minimal(S,d):
    if reord(S,d) is not False: return False
    for z in sorted(S):
        T=S-{z}
        A=alph(T,d)
        if any(len(x)<2 for x in A): continue
        if reord(T,d) is False: return False
    return True
found={}
tries=0
while tries<9000 and len(found)<40:
    tries+=1
    a=random.choice([2,3])
    A=[list(range(a)) for _ in range(3)]
    cells=list(product(*A))
    k=random.randint(3,min(7,len(cells)))
    S=set(random.sample(cells,k))
    Aa=alph(S,3)
    if any(len(x)<2 for x in Aa): continue
    if reord(S,3) is not False: continue
    if not minimal(S,3): continue
    c=canon(S,3)
    if c not in found: found[c]=S
print("\n     minimal obstructions found (up to relabelling) : %d"%len(found))
sizes=sorted(len(v) for v in found.values())
print("     sizes : %s"%sizes)
print("\n     the smallest ones:")
for c,S in sorted(found.items(),key=lambda t:len(t[1]))[:6]:
    print("        %d cells : %s"%(len(S),sorted(S)))
print("="*88)
print("  2.  DOES EVERY 'NO' CONTAIN ONE?")
print("="*88)
obs=list(found.values())
def contains_obstruction(S,d,obs):
    """does S contain a subset isomorphic to some obstruction?"""
    cs={canon(o,d) for o in obs}
    for k in sorted({len(o) for o in obs}):
        for T in combinations(sorted(S),k):
            Ts=set(T); A=alph(Ts,d)
            if any(len(x)<2 for x in A): continue
            if canon(Ts,d) in cs: return True
    return False
n=no=hit=0
for _ in range(500):
    a=random.choice([2,3])
    A=[list(range(a)) for _ in range(3)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(3,min(8,len(cells)))))
    Aa=alph(S,3)
    if any(len(x)<2 for x in Aa): continue
    r=reord(S,3)
    if r is not False: continue
    n+=1; no+=1
    if contains_obstruction(S,3,obs): hit+=1
print("\n     non-reorderable instances tested : %d"%no)
print("     containing a known obstruction   : %d  (%.0f%%)"%(hit,100*hit/max(no,1)))
print("""
{0}
  WHAT NEEDS DEFINING
{0}
""".format("="*88))
print("""  **The obstruction set.** If it is FINITE and its members are SMALL, then
  a NO has a bounded certificate and the problem is in co-NP with an
  explicit witness — which is a real result and a different one from a
  polynomial procedure.

  **If it is infinite**, that is also a theorem, and it explains why
  twenty-one local criteria all failed: there is no bounded family of
  forbidden patterns to test for.
""")