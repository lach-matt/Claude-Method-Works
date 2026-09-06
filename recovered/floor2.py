import math, statistics as st
import numpy as np
from collections import Counter, defaultdict
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
# the noble-gas closures
NOB={2,10,18,36,54,86}
def closed(ne_core):
    """is the CORE a closed shell (noble gas) or one short of one?"""
    return ne_core in NOB
R=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    R.append(dict(Z=Z,c=c,l=l,d=d,ne=ne,p=p,fl=math.floor(d),core=ne-1))
# add the three closures
NEW=[(36,0,4,3.0417),(36,1,3,3.0827),(36,2,1,1.5208),
     (54,0,5,4.0260),(54,1,4,3.5609),(54,2,2,2.4874),
     (86,0,6,5.0477),(86,1,5,4.5082),(86,2,3,3.4146)]
for ne,l,p,d in NEW:
    R.append(dict(Z=ne,c=1,l=l,d=d,ne=ne,p=p,fl=math.floor(d),core=ne-1))
print("  THE FLOOR RULE RE-EXAMINED  —  is it p−1 or p−2 at s?\n")
def free_old(l,p): return min(p,max(2-l,0))
print(f"      {'ℓ':>3}{'p':>3}{'n':>5}{'⌊δ⌋−p':>9}{'  distribution'}")
by=defaultdict(list)
for r in R: by[(r["l"],r["p"])].append(r["fl"]-r["p"])
for k in sorted(by):
    v=by[k]
    if len(v)<3: continue
    c=Counter(v)
    print(f"      {L[k[0]]:>3}{k[1]:>3}{len(v):>5}{st.median(v):>9.1f}"
          f"   " + "  ".join(f"{a}:{b}" for a,b in sorted(c.items())))
print()
print("  SPLIT BY WHETHER THE CORE IS A CLOSED SHELL\n")
print(f"      {'ℓ':>3}{'core':>10}{'n':>5}{'median ⌊δ⌋−p':>15}")
for l in range(3):
    for lab,sel in (("closed",lambda r: r["core"] in NOB),
                    ("open",lambda r: r["core"] not in NOB)):
        v=[r["fl"]-r["p"] for r in R if r["l"]==l and sel(r)]
        if len(v)<3: continue
        print(f"      {L[l]:>3}{lab:>10}{len(v):>5}{st.median(v):>15.1f}")
    print()
print("  THE CORRECTED RULE\n")
print("      free(ℓ, core) = max(2−ℓ, 0)  if the core is OPEN")
print("                    = max(1−ℓ, 0)  if the core is CLOSED\n")
def free_new(l,p,cl): return min(p, max((1 if cl else 2)-l, 0))
for nm,f in (("old: max(2−ℓ,0) always", lambda r: free_old(r["l"],r["p"])),
             ("new: 1 if closed core", lambda r: free_new(r["l"],r["p"],r["core"] in NOB))):
    ok=sum(1 for r in R if r["fl"]==r["p"]-f(r))
    print(f"      {nm:<28}{ok:>4}/{len(R)}  ({100*ok/len(R):.1f}%)")
print()
print("  AND THE CLOSURES THEMSELVES\n")
print(f"      {'':<8}{'ℓ':>3}{'p':>3}{'δ':>9}{'⌊δ⌋':>6}{'p−1':>6}{'p−2':>6}")
for ne,l,p,d in NEW:
    nm={36:"Kr I",54:"Xe I",86:"Rn I"}[ne]
    print(f"      {nm:<8}{L[l]:>3}{p:>3}{d:>9.4f}{math.floor(d):>6}{p-1:>6}{p-2:>6}")