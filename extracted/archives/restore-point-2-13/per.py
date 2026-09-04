import math, statistics as st
import numpy as np
from itertools import product
from collections import defaultdict
src=open("/tmp/cross.py",encoding="utf-8").read()
src=src[:src.index('print("  PLUGGING δ INTO')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; op_R=g["op_R"]; delta=g["delta"]
L="spdfg"
sp=defaultdict(list)
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    sp[(Z,c)].append(dict(l=l,S=S,d=d,p=p,n0=p+l+1,ne=ne,pred=delta(Z,c,l)))
print("  PER ELEMENT — is δ monotone in the coordinates that vary INSIDE one species?\n")
print("      within a species only ℓ and 2S+1 vary. δ should fall with ℓ.\n")
ok=bad=0; OKS=0; TOT=0
for k,v in sorted(sp.items()):
    if len(v)<3: continue
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            a,b=v[i],v[j]
            if a["l"]==b["l"]: continue
            lo,hi=(a,b) if a["l"]<b["l"] else (b,a)
            TOT+=1
            if lo["d"]>=hi["d"]: OKS+=1
print(f"      measured δ falls with ℓ : {OKS}/{TOT}  ({100*OKS/TOT:.1f}%)\n")
print("  AND THE CLOSURE COST, COMPUTED PER SPECIES AND AVERAGED\n")
rng=np.random.default_rng(11)
def cost_one(v,key,nb=4):
    if len(v)<4: return None
    base={(x["l"],x["S"]) for x in v}
    E0=len(op_R(base,2))-len(base)
    vals=[key(x) for x in v]
    if len(set(vals))<2: return None
    qs=np.quantile(vals,np.linspace(0,1,nb+1)[1:-1])
    X={(x["l"],x["S"],int(np.searchsorted(qs,key(x)))) for x in v}
    E=len(op_R(X,3))-len(X)
    Xr={(x["l"],x["S"],int(rng.integers(0,nb))) for x in v}
    Er=len(op_R(Xr,3))-len(Xr)
    return (E-E0), (Er-E0)
for nm,key in (("δ measured",lambda x:x["d"]),
               ("δ predicted",lambda x:x["pred"]),
               ("n* measured",lambda x:x["n0"]-x["d"]),
               ("n₀",lambda x:x["n0"])):
    num=den=0; n=0
    for k,v in sp.items():
        r=cost_one(v,key)
        if r is None: continue
        num+=r[0]; den+=max(r[1],1); n+=1
    if n: print(f"      {nm:<16}{n:>4} species   cost/noise = {num/max(den,1):.3f}")
print()
print("  THE SAME, POOLED ACROSS ALL SPECIES  (what I measured before)\n")
print("      δ predicted : 0.680     δ measured : 0.588")
print()
print("  READING\n")
print("      if the per-species cost is near zero, δ IS a monotone function of")
print("      the coordinates inside one atom, and the pooled cost was measuring")
print("      differences BETWEEN atoms — which the equation is supposed to supply.")
