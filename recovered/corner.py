import numpy as np, random
from itertools import product, permutations, combinations
random.seed(373)
print("="*86)
print("  THE CORNER FORMULATION")
print("="*86)
print("""
  X is a sublattice iff for every pair x,y the JOIN and MEET are in X.
  **The join is the corner of x,y's box selected by the axis orders**, so:

     for each pair, let I = axes where x,y differ, |I| = k
     the orders pick one of 2^k orientations
     **the orientation is ALLOWED only if both selected corners are in X**

  So each pair contributes an allowed-set of orientations, and the problem
  is a CSP on the orders with constraint arity k.

     k = 1  ->  no constraint (join = the larger cell, always present)
     k = 2  ->  BINARY constraints  -> 2-SAT-like -> polynomial
     k ≥ 3  ->  higher arity        -> the hardness enters here
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in S: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in S: return False
    return True
def reord(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(x)) for x in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
print("="*86)
print("  MEASURE THE ARITY DISTRIBUTION")
print("="*86)
print("\n  %5s%7s%10s%12s%12s%12s%12s"%("d","|A|","pairs","k=1","k=2","k=3","k≥4"))
print("  "+"-"*70)
for d,a,lim in [(2,3,300),(2,4,200),(3,2,300),(3,3,150),(4,2,150)]:
    kk={1:0,2:0,3:0,4:0}; tot=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        for x,y in combinations(sorted(S),2):
            k=sum(1 for i in range(d) if x[i]!=y[i])
            kk[min(k,4)]+=1; tot+=1
    if tot: print("  %5d%7d%10d%12.3f%12.3f%12.3f%12.3f"%(d,a,tot,kk[1]/tot,kk[2]/tot,kk[3]/tot,kk[4]/tot))
print("""
  **At d = 2 every pair has k ≤ 2, so every constraint is binary.** That is
  why d = 2 is tractable — not because of intervals, but because the CSP is
  binary. **At d ≥ 3 the k ≥ 3 constraints appear, and they are the whole
  difficulty.**
""")
print("="*86)
print("  AND THE ALLOWED-ORIENTATION TEST")
print("="*86)
def corner_feasible(S,d):
    """necessary: every pair must have at least one allowed orientation"""
    Sset=set(S)
    for x,y in combinations(sorted(S),2):
        I=[i for i in range(d) if x[i]!=y[i]]
        if not I: continue
        ok=False
        for bits in product([0,1],repeat=len(I)):
            hi=list(x); lo=list(x)
            for t,i in enumerate(I):
                if bits[t]: hi[i]=y[i]; lo[i]=x[i]
                else: hi[i]=x[i]; lo[i]=y[i]
            if tuple(hi) in Sset and tuple(lo) in Sset: ok=True; break
        if not ok: return False
    return True
print("\n  %5s%7s%9s%14s%16s%12s%12s"%("d","|A|","n","reorderable","corner-feasible","FN","FP"))
print("  "+"-"*76)
for d,a,lim in [(2,3,250),(2,4,120),(3,2,250),(3,3,60)]:
    n=r=c=fn=fp=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        n+=1
        rr=reord(S,d); cc=corner_feasible(S,d)
        r+=rr; c+=cc
        if rr and not cc: fn+=1
        if cc and not rr: fp+=1
    print("  %5d%7d%9d%14d%16d%12d%12d"%(d,a,n,r,c,fn,fp))
print("""
  **Zero false negatives is required** — if a pair has no allowed
  orientation, no order can work. **The false positives measure how much
  the pairwise constraints leave undetermined.**
""")