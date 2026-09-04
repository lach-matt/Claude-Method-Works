import lam8
from itertools import product as iprod
from collections import defaultdict
L8=lam8.L8(); S=set(L8)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
# seven constraint edges as (u, phi(xv), v) with criterion y_u <= phi(x_v)
# l<=n-1, k<=4l+2, q<=k, 2S<=k, f<=e-1, g<=4f+2, g<=q   (idx n0 l1 k2 q3 e4 f5 g6 S7)
edges=[(1,lambda v:v-1,0),(2,lambda v:4*v+2,1),(3,lambda v:v,2),(7,lambda v:v,2),
       (5,lambda v:v-1,4),(6,lambda v:4*v+2,5),(6,lambda v:v,3)]
def crit(x,y): return all(y[u]<=phi(x[v]) for u,phi,v in edges)
def isbox(x,y):
    for z in iprod(*[range(x[i],y[i]+1) for i in range(8)]):
        if z not in S: return False
    return True
# 1) criterion exactness over ALL comparable pairs
tot=0; agree=0; boxes=0
for a in L8:
    for b in L8:
        if a is b or not leq(a,b) or a==b: continue
        tot+=1; c=crit(a,b); ib=isbox(a,b)
        if c==ib: agree+=1
        if ib: boxes+=1
print(f"criterion exactness: {agree}/{tot} agree; boxes {boxes} = {100*boxes/tot:.1f}%")
# 2) meet-join basis over all 475,800 unordered pairs (criterion now proven; use it)
Ll=L8; n=len(Ll); totmj=0; boxmj=0
bind=defaultdict(int)   # per named constraint, over all intervals
bindnb=defaultdict(int) # over non-box intervals only
named={'g<=q':(6,lambda v:v,3), 'q<=k':(3,lambda v:v,2), 'g<=4f+2':(6,lambda v:4*v+2,5)}
for i in range(n):
    a=Ll[i]
    for j in range(i+1,n):
        b=Ll[j]
        lo=tuple(min(x,y) for x,y in zip(a,b)); hi=tuple(max(x,y) for x,y in zip(a,b))
        totmj+=1
        isb=crit(lo,hi)
        if isb: boxmj+=1
        for nm,(u,phi,v) in named.items():
            if hi[u]>phi(lo[v]):
                bind[nm]+=1
                if not isb: bindnb[nm]+=1
print(f"meet-join basis: {totmj} intervals, boxes {boxmj} = {100*boxmj/totmj:.1f}%")
for nm in named:
    print(f"  {nm}: binds {100*bind[nm]/totmj:.1f}% of all | {100*bindnb[nm]/(totmj-boxmj):.1f}% of non-box  (record: g<=q 35.6, q<=k 33.0, g<=4f+2 4.9)")
# 3) |J(Lambda)| = elements with exactly one lower cover
def lower_covers(x):
    cnt=0
    for i in range(8):
        y=list(x); y[i]-=1; y=tuple(y)
        if y in S and sum(y)==sum(x)-1: cnt+=1
    return cnt
J=[x for x in L8 if lower_covers(x)==1]
print("join-irreducibles |J(Lambda)| =", len(J), "(claim 17)")
# 4) Mirsky: 18 rank levels (antichain partition) vs maximal chain of 18 cells
ranks={sum(x) for x in L8}
print("rank levels:", len(ranks), "; chain cells:", max(ranks)-min(ranks)+1, "; chain length (steps):", max(ranks)-min(ranks))
# 5) tree: 8 vertices, 7 edges, connected, acyclic
verts=set(range(8)); E=[(u,v) for u,_,v in edges]
parent=list(range(8))
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
acyc=True
for u,v in E:
    ru,rv=find(u),find(v)
    if ru==rv: acyc=False
    parent[ru]=rv
print("constraint graph: 8 vertices,",len(E),"edges, acyclic:",acyc,", connected:",len({find(i) for i in range(8)})==1)