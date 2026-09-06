import math, statistics as st
from collections import defaultdict
src=open("channels_principle.py",encoding="utf-8").read()
src=src[:src.index('print("  THE PRINCIPAL STRUCTURE')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]; L="spdfghi"
EL={12:"Mg",13:"Al",14:"Si",15:"P",16:"S",20:"Ca",22:"Ti",26:"Fe",11:"Na",19:"K",21:"Sc"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",9:"IX",11:"XI",15:"XV"}
print("  IS THE 'WILD' FRACTION JUST floor() WRAPPING?\n")
print("  Along Nₑ = 12 (Na-like, 3s¹ core), δ ITSELF against charge:\n")
v=[x for x in CH if x["ne"]==12]
byl=defaultdict(dict)
for y in v: byl[y["l"]][y["c"]]=y["d"]
cs=sorted({y["c"] for y in v})
print(f"      {'ℓ':>3}" + "".join(f"{c:>9}" for c in cs))
print(f"      {'':>3}" + "".join(
    f"{EL.get(c+11,'')+RO.get(c,''):>9}" for c in cs))
for l in sorted(byl):
    print(f"      {L[l]:>3}" + "".join(
        f"{byl[l].get(c,float('nan')):>9.3f}" if c in byl[l] else f"{'—':>9}" for c in cs))
print()
print("      and floor(δ):\n")
for l in sorted(byl):
    print(f"      {L[l]:>3}" + "".join(
        f"{math.floor(byl[l][c]):>9}" if c in byl[l] else f"{'—':>9}" for c in cs))
print()
print("  → δ falls SMOOTHLY with charge (Edlén). floor(δ) steps down as it crosses")
print("    each integer, and frac(δ) wraps from 0 back to 1. The 'wild variation'")
print("    at s and p is the wrap, not the physics.\n")
print("  SO THE RIGHT QUESTION IS ABOUT δ, NOT ITS FRACTIONAL PART.\n")
print("  Testing: is δ smooth in charge along the sequence?\n")
from scipy import stats as SS
import numpy as np
print(f"      {'ℓ':>3}{'n':>4}{'δ vs ln(c+1)/c':>20}{'r²':>8}")
for l in sorted(byl):
    d=byl[l]
    if len(d)<4: continue
    xs=np.array([math.log(c+1)/c for c in sorted(d)])
    ys=np.array([d[c] for c in sorted(d)])
    r=SS.linregress(xs,ys)
    print(f"      {L[l]:>3}{len(d):>4}{r.slope:>20.3f}{r.rvalue**2:>8.4f}")
print()
print("  AND THE SAME FOR THE OTHER LONG SEQUENCES\n")
for ne in (11,19,13,4):
    v=[x for x in CH if x["ne"]==ne]
    byl2=defaultdict(dict)
    for y in v: byl2[y["l"]][y["c"]]=y["d"]
    good=[(l,d) for l,d in byl2.items() if len(d)>=3]
    if not good: continue
    print(f"      Nₑ = {ne}:")
    for l,d in sorted(good):
        xs=np.array([math.log(c+1)/c for c in sorted(d)])
        ys=np.array([d[c] for c in sorted(d)])
        r=SS.linregress(xs,ys)
        print(f"          {L[l]}  n={len(d)}  r² = {r.rvalue**2:.4f}")