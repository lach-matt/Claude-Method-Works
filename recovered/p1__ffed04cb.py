import math, statistics as st
import numpy as np
from collections import Counter, defaultdict
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
R=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    R.append(dict(l=l,p=p,d=d,fl=math.floor(d),ne=ne,c=c))
for ne,l,p,d in [(36,0,4,3.0417),(36,1,3,3.0827),(36,2,1,1.5208),
                 (54,0,5,4.0260),(54,1,4,3.5609),(54,2,2,2.4874),
                 (86,0,6,5.0477),(86,1,5,4.5082),(86,2,3,3.4146),
                 (48,0,5,3.6629),(48,1,3,3.0513),(48,2,2,2.0864),
                 (49,0,5,3.7268),(49,1,3,3.2371),(49,2,2,2.2752)]:
    R.append(dict(l=l,p=p,d=d,fl=math.floor(d),ne=ne,c=1))
print("  THE SHORTFALL  s = p − ⌊δ⌋  AGAINST p, AT EACH ℓ\n")
for l in range(4):
    v=[r for r in R if r["l"]==l]
    if len(v)<4: continue
    by=defaultdict(list)
    for r in v: by[r["p"]].append(r["p"]-r["fl"])
    print(f"      ℓ = {L[l]}")
    print(f"          {'p':>3}{'n':>4}{'median shortfall':>19}{'  values'}")
    for p in sorted(by):
        c=Counter(by[p])
        print(f"          {p:>3}{len(by[p]):>4}{st.median(by[p]):>19.1f}"
              f"   " + " ".join(f"{a}×{b}" for a,b in sorted(c.items())))
    print()
print("  THE OLD RULE vs A p-DEPENDENT CAP\n")
def old(l,p): return min(p,max(2-l,0))
def new(l,p):
    # the cap falls to 1 once p is large
    base=max(2-l,0)
    return min(p, base-1 if (l==0 and p>=4) else base)
for nm,f in (("old  min(p, max(2−ℓ,0))",old),
             ("new  cap→1 at s when p≥4",new)):
    ok=sum(1 for r in R if r["fl"]==r["p"]-f(r["l"],r["p"]))
    print(f"      {nm:<30}{ok:>4}/{len(R)}  ({100*ok/len(R):.1f}%)")
print()
print("  WHERE THE TWO DISAGREE\n")
print(f"      {'ℓ':>3}{'p':>3}{'Nₑ':>5}{'c':>3}{'δ':>9}{'⌊δ⌋':>5}{'old':>5}{'new':>5}")
for r in sorted(R,key=lambda z:(z["l"],z["p"],z["ne"])):
    o=r["p"]-old(r["l"],r["p"]); n=r["p"]-new(r["l"],r["p"])
    if o!=n:
        print(f"      {L[r['l']]:>3}{r['p']:>3}{r['ne']:>5}{r['c']:>3}{r['d']:>9.4f}"
              f"{r['fl']:>5}{o:>5}{n:>5}")