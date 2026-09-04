import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("channels_principle.py",encoding="utf-8").read()
src=src[:src.index('print("  THE PRINCIPAL STRUCTURE')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]; L="spdfghi"
def outer(ne):
    cfg=config(ne); return cfg[-1] if cfg else (0,0,0)
for x in CH:
    n_,l_,o_=outer(x["ne"]-1)
    x["on"],x["ol"]=n_,l_
    x["dl"]=x["l"]-l_
print("  THE GATE:  frac(δ) = 0 when ℓ − ℓ_core ≥ 2\n")
print(f"      {'ℓ − ℓ_core':>12}{'n':>6}{'median frac':>14}{'sd':>9}{'|frac|<0.05':>14}")
by=defaultdict(list)
for x in CH: by[x["dl"]].append(x["frac"])
for k in sorted(by):
    v=by[k]
    if len(v)<4: continue
    print(f"      {k:>12}{len(v):>6}{st.median(v):>14.3f}{st.pstdev(v):>9.3f}"
          f"{sum(1 for z in v if abs(z)<0.05):>9}/{len(v)}")
print()
lo=[x["frac"] for x in CH if x["dl"]>=2]
hi=[x["frac"] for x in CH if x["dl"]<2]
print(f"      ℓ − ℓ_core ≥ 2 : {len(lo):>4} channels   median {st.median(lo):.4f}   "
      f"sd {st.pstdev(lo):.4f}")
print(f"      ℓ − ℓ_core < 2 : {len(hi):>4} channels   median {st.median(hi):.4f}   "
      f"sd {st.pstdev(hi):.4f}")
u=SS.mannwhitneyu(hi,lo,alternative="greater")
print(f"      Mann-Whitney: p = {u.pvalue:.2e}")
print()
print("  AND THE WHOLE DEFECT UNDER THE GATE\n")
print("      If frac(δ) = 0 above the gate, then δ is an INTEGER there — the")
print("      channel is hydrogenic up to a whole number of nodes.\n")
above=[x for x in CH if x["dl"]>=2]
print(f"      {len(above)} channels with ℓ − ℓ_core ≥ 2")
print(f"      how many have |δ − round(δ)| < 0.05 : "
      f"{sum(1 for x in above if abs(x['d']-round(x['d']))<0.05)}")
print(f"      how many have δ < 0.05 outright     : "
      f"{sum(1 for x in above if x['d']<0.05)}")
print()
print("  THE ORDERING CONSEQUENCE — s AGAINST p AT A NEUTRAL ATOM\n")
print("      Madelung puts ns below np. Under the gate, both are BELOW the gate")
print("      (ℓ − ℓ_core is 0 or negative for s, and ≤ 1 for p), so both carry a")
print("      fractional part and the ordering turns on which is larger.\n")
print(f"      {'core outer':>12}{'ns frac':>10}{'np frac':>10}{'np − ns':>10}{'n':>5}")
pairs=defaultdict(lambda: {0:[],1:[]})
for x in CH:
    if x["l"] in (0,1) and x["c"]==1:
        pairs[(x["on"],x["ol"])][x["l"]].append(x["frac"])
tot=[]
for k in sorted(pairs):
    a=pairs[k][0]; b=pairs[k][1]
    if not a or not b: continue
    d=st.median(b)-st.median(a); tot.append(d)
    print(f"      {f'{k[0]}{L[k[1]]}':>12}{st.median(a):>10.3f}{st.median(b):>10.3f}"
          f"{d:>10.3f}{len(a)+len(b):>5}")
if tot:
    print(f"\n      np frac exceeds ns frac in {sum(1 for d in tot if d>0)} of {len(tot)} cores")
    print(f"      median difference {st.median(tot):+.3f}")
    print(f"      → n*(np) = 2 − frac(np) < n*(ns) = 3 − frac(ns) requires")
    print(f"        frac(np) − frac(ns) > −1, which always holds. The s–p ordering")
    print(f"        is NOT set by the fraction at all — it is set by the INTEGER.")
