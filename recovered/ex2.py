import numpy as np, math, time
from itertools import product, permutations, combinations
from collections import defaultdict, Counter
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
CAN={}
def canon(T,d):
    k=(d,tuple(sorted(T)))
    if k in CAN: return CAN[k]
    A=alph(T,d); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        c=tuple(sorted(relab(T,[list(p) for p in ps],d)))
        if best is None or c<best: best=c
    CAN[k]=best; return best
def sig3(S,d):
    return tuple(sorted(Counter(canon(set(T),d) for T in combinations(sorted(S),3)).items()))
print("="*84)
print("  EXHAUSTIVE OVER EVERY SUBSET")
print("="*84)
print("\n  %12s%7s%11s%11s%11s%9s%9s"%("box","cells","subsets","tested","classes","multi","MIXED"))
print("  "+"-"*76)
for dims in [(2,2,2),(2,2,3)]:
    d=len(dims); cells=list(product(*[range(x) for x in dims])); n=len(cells)
    cls=defaultdict(list); tested=0
    for m in range(1,1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        if len(S)<3: continue
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        tested+=1
        cls[sig3(S,d)].append(reord(S,d))
    multi=[v for v in cls.values() if len(v)>1]
    mixed=[v for v in multi if len(set(v))>1]
    print("  %12s%7d%11d%11d%11d%9d%9d"%("×".join(map(str,dims)),n,2**n,tested,len(cls),len(multi),len(mixed)))
    if mixed:
        print("        **MIXED CLASS EXISTS — signature incomplete**")
        g=mixed[0]
        for S,r in []: pass