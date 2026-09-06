import math, statistics as st
from collections import Counter, defaultdict
src=open("madelung.py",encoding="utf-8").read()
src=src[:src.index('print(f"  {len(CH)} measured channels')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]
L="spdfghi"
def core_p(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
print("  IS THE PAULI BOUND TIGHT?\n")
print("      ORDER language     : floor(δ) ≤ p            (Q.bound, exceptionless)")
print("      ANALYSIS language  : dδ/dp = 1               (measured 0.81–0.99)")
print()
print("      If floor(δ) = p EXACTLY, the second is an identity: δ = p + frac,")
print("      so dδ/dp = 1 by construction and κ(ℓ) = −median frac(δ).\n")
rows=[]
for x in CH:
    p=core_p(x["ne"]-1,x["l"])
    rows.append((x["l"], x["c"], p, x["d"], math.floor(x["d"])))
print(f"      {'ℓ':>3}{'n':>6}{'floor(δ) = p':>15}{'= p−1':>8}{'= p−2':>8}{'< p−2':>8}{'> p':>6}")
for l in sorted({r[0] for r in rows}):
    v=[r for r in rows if r[0]==l]
    c=Counter(r[4]-r[2] for r in v)
    print(f"      {L[l]:>3}{len(v):>6}{c.get(0,0):>15}{c.get(-1,0):>8}{c.get(-2,0):>8}"
          f"{sum(n for k,n in c.items() if k<-2):>8}{sum(n for k,n in c.items() if k>0):>6}")
allc=Counter(r[4]-r[2] for r in rows)
print(f"\n      overall: floor(δ) = p in {allc.get(0,0)} of {len(rows)} "
      f"({100*allc.get(0,0)/len(rows):.1f}%)")
print(f"               floor(δ) = p−1 in {allc.get(-1,0)} ({100*allc.get(-1,0)/len(rows):.1f}%)")
print(f"               floor(δ) > p  in {sum(n for k,n in allc.items() if k>0)}   "
      f"← would violate Q.bound")
print()
print("  RESTRICTED TO NEUTRALS, WHERE THE RULE LIVES\n")
neu=[r for r in rows if r[1]==1]
c=Counter(r[4]-r[2] for r in neu)
print(f"      {len(neu)} channels: " + "  ".join(
    f"floor−p = {k}: {v}" for k,v in sorted(c.items())))
print()
print("  AND THE PENETRATING ONES ONLY (p ≥ 1)\n")
pen=[r for r in rows if r[2]>=1]
c=Counter(r[4]-r[2] for r in pen)
print(f"      {len(pen)} channels: " + "  ".join(
    f"{k}: {v}" for k,v in sorted(c.items())))
print()
print("  THE FRACTIONAL PART — is it κ(ℓ)?\n")
print(f"      {'ℓ':>3}{'n':>6}{'median frac(δ)':>17}{'sd':>8}{'median p−δ':>13}")
for l in sorted({r[0] for r in rows}):
    v=[r for r in rows if r[0]==l and r[2]>=1]
    if len(v)<5: continue
    fr=[r[3]-math.floor(r[3]) for r in v]
    pd=[r[2]-r[3] for r in v]
    print(f"      {L[l]:>3}{len(v):>6}{st.median(fr):>17.3f}{st.pstdev(fr):>8.3f}{st.median(pd):>13.3f}")