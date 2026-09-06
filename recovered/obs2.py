import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(463)
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
    A=alph(S,d); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        T=tuple(sorted(relab(S,[list(p) for p in ps],d)))
        if best is None or T<best: best=T
    return best
def minimal(S,d):
    if reord(S,d) is not False: return False
    for z in sorted(S):
        T=S-{z}; A=alph(T,d)
        if any(len(x)<2 for x in A): continue
        if reord(T,d) is False: return False
    return True
print("="*88)
print("  EXHAUSTIVE OBSTRUCTION SEARCH AT d = 3")
print("="*88)
print("""
  **Enumerate ALL subsets of the 3×3×3 box up to 5 cells**, keep the minimal
  non-reorderable ones, and count them up to relabelling. That is a complete
  census at this size, not a sample.
""")
A=[list(range(3)) for _ in range(3)]
cells=list(product(*A))
OBS={}
for k in (3,4,5):
    cnt=0
    for T in combinations(cells,k):
        S=set(T); Aa=alph(S,3)
        if any(len(x)<2 for x in Aa): continue
        if reord(S,3) is not False: continue
        if not minimal(S,3): continue
        c=canon(S,3)
        if c not in OBS: OBS[c]=S; cnt+=1
    print("     size %d : %d new minimal obstructions   (running total %d)"%(k,cnt,len(OBS)))
print("\n     **complete census up to 5 cells in a 3×3×3 box : %d obstructions**"%len(OBS))
bysz={}
for c,S in OBS.items(): bysz[len(S)]=bysz.get(len(S),0)+1
print("     by size :",dict(sorted(bysz.items())))
print("="*88)
print("  DO FRESH NON-REORDERABLE INSTANCES CONTAIN ONE?")
print("="*88)
print("""
  **The independent test.** Draw instances that were NOT used to build the
  census — larger boxes and more cells — and ask whether each contains a
  member of the census.
""")
CS={canon(o,3) for o in OBS.values()}
def has_obs(S,d,maxk=5):
    for k in (3,4,5):
        if k>maxk: break
        for T in combinations(sorted(S),k):
            Ts=set(T); Aa=alph(Ts,d)
            if any(len(x)<2 for x in Aa): continue
            if canon(Ts,d) in CS: return True
    return False
print("\n  %14s%10s%14s%16s%14s"%("box","tested","not reord.","contains one","misses"))
print("  "+"-"*70)
for a,kmax,lim in [(3,8,300),(4,7,200)]:
    Ax=[list(range(a)) for _ in range(3)]
    cl=list(product(*Ax))
    n=nr=hit=0
    for _ in range(lim):
        S=set(random.sample(cl,random.randint(3,kmax)))
        Aa=alph(S,3)
        if any(len(x)<2 for x in Aa): continue
        r=reord(S,3)
        if r is None or r is not False: continue
        n+=1; nr+=1
        if has_obs(S,3): hit+=1
    print("  %14s%10d%14d%16d%14d"%("%d×%d×%d"%(a,a,a),n,nr,hit,nr-hit))
print("""
{0}
  THE RESULT
{0}
""".format("="*88))
print("""  **If every fresh NO contains a census member, the obstruction set at
  d = 3 is complete at ≤ 5 cells** — and the problem is decidable in
  O(|X|^5) by testing all 5-subsets. **That is polynomial.**

  **If some miss, the set is larger**, and the census must go to 6 cells.
""")