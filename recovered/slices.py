import numpy as np
from itertools import product, permutations, combinations
print("="*88)
print("  THE STRUCTURE IN RELATION TO ITSELF — SLICES AND THEIR RELATION")
print("="*88)
print("""
  **The step size doubles with d: 1, 2, 4.** And a d-box is a stack of
  (d−1)-boxes. **So ask whether a reorderable set is determined by its slices
  plus the relation between them** — the recursion the doubling suggests.
""")
def mk(DIMS):
    d=len(DIMS); cells=list(product(*[range(x) for x in DIMS]))
    return d,cells
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
for DIMS in [(2,2,2),(2,2,3),(2,3,3)]:
    d,cells=mk(DIMS)
    print("\n  ---- box %s ----"%"×".join(map(str,DIMS)))
    n=len(cells)
    YES=[]; NO=[]
    for m in range(1,1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        if len(S)<3: continue
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        (YES if reord(S,d) else NO).append(S)
    print("     reorderable %d      not %d"%(len(YES),len(NO)))
    def slices(S,axis=0):
        vals=sorted({x[axis] for x in S})
        return [{tuple(y for k,y in enumerate(x) if k!=axis) for x in S if x[axis]==v} for v in vals]
    def slices_ok(S):
        for ax in range(d):
            for sl in slices(S,ax):
                if len(sl)<1: continue
                A2=[sorted({p[i] for p in sl}) for i in range(d-1)]
                if any(len(a)<2 for a in A2): continue
                if not reord(sl,d-1): return False
        return True
    ys=sum(1 for S in YES if slices_ok(S)); ns=sum(1 for S in NO if slices_ok(S))
    print("     **all slices reorderable** : YES sets %d/%d      NO sets %d/%d"%(ys,len(YES),ns,len(NO)))
    print("        -> necessary : %s      sufficient : %s"%(ys==len(YES),ns==0))
    # and the RELATION: are the slices nested?
    def slices_nested(S,axis=0):
        sl=slices(S,axis)
        return all(a<=b or b<=a for a in sl for b in sl)
    def rel_ok(S):
        return any(slices_nested(S,ax) for ax in range(d))
    yr=sum(1 for S in YES if rel_ok(S)); nr=sum(1 for S in NO if rel_ok(S))
    print("     **some axis has NESTED slices** : YES %d/%d      NO %d/%d"%(yr,len(YES),nr,len(NO)))
    print("        -> necessary : %s      sufficient : %s"%(yr==len(YES),nr==0))
    # combined
    yc=sum(1 for S in YES if slices_ok(S) and rel_ok(S))
    nc=sum(1 for S in NO if slices_ok(S) and rel_ok(S))
    print("     **both together** : YES %d/%d   NO %d/%d   -> exact : %s"%(yc,len(YES),nc,len(NO),yc==len(YES) and nc==0))