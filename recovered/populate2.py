import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from collections import defaultdict
import ground as G
L="spdfg"
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]
def cap(l): return 2*(2*l+1)
def brack(ne,c):
    """the corridor for the species with ne electrons at charge c"""
    pr=cfg(ne-1,c); prd={(n,l):o for n,l,o in pr}
    cu=cfg(ne,c);   cud={(n,l):o for n,l,o in cu}
    got=[k for k in cud if cud[k]>prd.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if prd.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if prd.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    gp=gn-gl-1; lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return lo,hi,gl
def t(l): return math.sqrt(l*(l+1)/2)
print("  POPULATING Λ_spectra FROM THE LÖWDIN SOLUTION\n")
print("      a = L + t(ℓ_g)·(U − L),  t(ℓ) = √(ℓ(ℓ+1)/2)")
print("      δ = a·√(p + q/2(2ℓ+1)),  q = 0 for a Rydberg channel\n")
OK=[]; SK=0
for (Z,c,l,S),dm in sorted(H.items()):
    ne=Z-c+1
    if Z>92 or c>10 or l>5 or dm<=0.02: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    b=brack(ne,c)
    if b is None: SK+=1; continue
    lo,hi,gl=b
    if lo<-1e8 or hi>1e8: SK+=1; continue
    a=lo+t(gl)*(hi-lo)
    dp=a*math.sqrt(p)
    OK.append((Z,c,l,S,p,dm,dp,a))
print(f"      {len(OK)} channels predicted · {SK} skipped (one-sided corridor)\n")
r=np.array([o[6]/o[5] for o in OK])
print(f"      predicted/measured : median {st.median(r):.4f}  sd {st.pstdev(r):.4f}")
print(f"      within 20% : {sum(1 for x in r if 0.8<x<1.2)}/{len(r)}")
print(f"      within 50% : {sum(1 for x in r if 0.5<x<1.5)}/{len(r)}\n")
print(f"      {'ℓ':>3}{'n':>5}{'median pred/meas':>19}{'sd':>9}")
BY=defaultdict(list)
for o in OK: BY[o[2]].append(o[6]/o[5])
for l in sorted(BY):
    v=BY[l]
    print(f"      {L[l]:>3}{len(v):>5}{st.median(v):>19.4f}{st.pstdev(v):>9.4f}")
print()
print("  A SAMPLE\n")
print(f"      {'Z':>4}{'c':>3}{'ℓ':>3}{'p':>3}{'a':>9}{'δ meas':>10}{'δ pred':>10}{'ratio':>9}")
for o in sorted(OK,key=lambda x:(x[0],x[1],x[2]))[:18]:
    print(f"      {o[0]:>4}{o[1]:>3}{L[o[2]]:>3}{o[4]:>3}{o[7]:>9.4f}"
          f"{o[5]:>10.4f}{o[6]:>10.4f}{o[6]/o[5]:>9.3f}")