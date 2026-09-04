import sys
from itertools import product, permutations, combinations
DIMS=tuple(int(x) for x in sys.argv[1].split(','))
d=len(DIMS); cells=list(product(*[range(x) for x in DIMS])); n=len(cells)
def alph(S,dd): return [sorted({x[i] for x in S}) for i in range(dd)]
def relab(S,o,dd):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(dd)) for x in S}
def lat(S,dd):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(dd)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(dd)) not in Ss: return False
    return True
MEMO={}
def reord(S,dd):
    key=(dd,tuple(sorted(S)))
    if key in MEMO: return MEMO[key]
    A=alph(S,dd); r=False
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],dd),dd): r=True; break
    MEMO[key]=r; return r
YES=[];NO=[]
for m in range(1,1<<n):
    S={cells[i] for i in range(n) if m>>i & 1}
    if len(S)<3: continue
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    (YES if reord(S,d) else NO).append(S)
def slices(S,ax):
    vals=sorted({x[ax] for x in S})
    return [{tuple(y for k,y in enumerate(x) if k!=ax) for x in S if x[ax]==v} for v in vals]
def slices_ok(S):
    for ax in range(d):
        for sl in slices(S,ax):
            A2=[sorted({p[i] for p in sl}) for i in range(d-1)]
            if any(len(a)<2 for a in A2): continue
            if not reord(sl,d-1): return False
    return True
def nested(S):
    for ax in range(d):
        sl=slices(S,ax)
        if all(a<=b or b<=a for a in sl for b in sl): return True
    return False
ys=sum(1 for S in YES if slices_ok(S)); ns=sum(1 for S in NO if slices_ok(S))
yn=sum(1 for S in YES if nested(S));    nn=sum(1 for S in NO if nested(S))
yb=sum(1 for S in YES if slices_ok(S) and nested(S))
nb=sum(1 for S in NO if slices_ok(S) and nested(S))
print("  box %-10s YES %5d  NO %6d"%("×".join(map(str,DIMS)),len(YES),len(NO)))
print("     slices all reorderable : YES %5d/%5d   NO %6d/%6d   nec %-5s suff %s"%(ys,len(YES),ns,len(NO),ys==len(YES),ns==0))
print("     some axis nested       : YES %5d/%5d   NO %6d/%6d   nec %-5s suff %s"%(yn,len(YES),nn,len(NO),yn==len(YES),nn==0))
print("     both                   : YES %5d/%5d   NO %6d/%6d   **exact %s**"%(yb,len(YES),nb,len(NO),yb==len(YES) and nb==0))