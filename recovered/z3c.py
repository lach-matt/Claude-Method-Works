import json, sys
tag=sys.argv[1]; cond=sys.argv[2]
P=json.load(open(f"prep_{tag}.json"))
X=[tuple(c) for c in P["cells"]]
els=[set(e) for e in P["elements"]]
NE=len(els); FULL=(1<<NE)-1
k0=json.load(open(f"seed_{tag}.json"))["seed"]
lmax=max(c[1] for c in X); fmax=max(c[5] for c in X)
kmx=max(c[2] for c in X); gmx=max(c[6] for c in X)
conds={
 "ss": lambda c:c[1]==0 and c[5]==0, "sp": lambda c:c[1]==0 and c[5]==1,
 "ps": lambda c:c[1]==1 and c[5]==0, "pp": lambda c:c[1]==1 and c[5]==1,
 "null": lambda c:c[3]==0, "full": lambda c:c[3]==c[2],
 "c3": lambda c:(c[1]==lmax and c[2]==kmx and c[3]==c[2] and c[5]==fmax and c[6]==gmx and c[7]==0),
}
p=conds[cond]
sig=set()
for ci,c in enumerate(X):
    if p(c): continue
    m=0
    for ei,e in enumerate(els):
        if ci in e: m|=1<<ei
    if m: sig.add(m)
masks=sorted(sig, key=lambda m:-bin(m).count("1"))
agg=0
for m in masks: agg|=m
if agg!=FULL:
    print(f"{cond}: INFEASIBLE -> UNIVERSAL"); sys.exit()
pc=[bin(m).count("1") for m in masks]
maxpc=pc[0]
elem_classes=[[i for i,m in enumerate(masks) if m>>e&1] for e in range(NE)]
import math
def bb(cov,depth,banned):
    if cov==FULL: return True
    rem=NE-bin(cov).count("1")
    if depth + math.ceil(rem/maxpc) > k0: return False
    e=min((x for x in range(NE) if not cov>>x&1), key=lambda x:len(elem_classes[x]))
    nb=set(banned)
    for ci in elem_classes[e]:
        if ci in banned: continue
        if bb(cov|masks[ci],depth+1,nb): return True
        nb.add(ci)
    return False
ok=bb(0,0,set())
print(f"{cond}: size-{k0} cover without it {'EXISTS -> not universal' if ok else 'NONE -> UNIVERSAL'}")