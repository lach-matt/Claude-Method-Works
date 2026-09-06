import math, statistics as st
from collections import defaultdict
from scipy import stats as SS
import numpy as np
src=open("madelung.py",encoding="utf-8").read()
src=src[:src.index('print(f"  {len(CH)} measured channels')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]
L="spdfghi"
def core_p(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
print("  δ ≈ p + κ(ℓ)  —  ON THE MEASURED DEFECTS\n")
print("  n₀ = p + ℓ + 1 is orthogonality: p core orbitals of the same ℓ force p")
print("  nodes, and an nℓ function has n−ℓ−1 of them. If δ ≈ p, the two cancel")
print("  and n* = n₀ − δ ≈ ℓ + 1 − κ(ℓ) — nearly independent of p.\n")
by=defaultdict(list)
for x in CH:
    p=core_p(x["ne"]-1,x["l"])
    by[x["l"]].append((p, x["d"], x["c"], x["ne"]))
print(f"      {'ℓ':>3}{'channels':>10}{'median p−δ':>13}{'sd':>8}{'slope of δ on p':>18}")
K={}
for l in sorted(by):
    v=by[l]
    if len(v)<6: continue
    diff=[p-d for p,d,c,ne in v]
    ps=[p for p,d,c,ne in v]; ds=[d for p,d,c,ne in v]
    r=SS.linregress(ps,ds) if len(set(ps))>1 else None
    K[l]=st.median(diff)
    sl=f"{r.slope:+.3f} (r² {r.rvalue**2:.2f})" if r else "—"
    print(f"      {L[l]:>3}{len(v):>10}{st.median(diff):>13.3f}{st.pstdev(diff):>8.3f}{sl:>18}")
print()
print("      κ(ℓ) = −median(p−δ):")
for l in sorted(K): print(f"          κ({L[l]}) = {-K[l]:+.3f}")
if len(K)>=4:
    ls=sorted(K); r=SS.linregress(ls,[-K[l] for l in ls])
    print(f"\n      κ against ℓ: slope {r.slope:+.4f} per unit ℓ, r² {r.rvalue**2:.4f}, p {r.pvalue:.2e}")
print()
print("  AND THE CONSEQUENCE — n* for the first member of each series\n")
print(f"      {'ℓ':>3}{'n':>5}{'median n* = n₀ − δ':>21}{'sd':>8}{'ℓ+1':>6}")
for l in sorted(by):
    v=[x for x in CH if x["l"]==l]
    if len(v)<6: continue
    ns=[x["nstar"] for x in v]
    print(f"      {L[l]:>3}{len(v):>5}{st.median(ns):>21.3f}{st.pstdev(ns):>8.3f}{l+1:>6}")
print()
print("  THE SPLIT — penetrating against non-penetrating\n")
pen=[x for x in CH if core_p(x["ne"]-1,x["l"])>0]
non=[x for x in CH if core_p(x["ne"]-1,x["l"])==0]
for lab,v in (("penetrating (p ≥ 1)",pen),("non-penetrating (p = 0)",non)):
    if not v: continue
    print(f"      {lab:<26}{len(v):>5} channels   median n* {st.median([x['nstar'] for x in v]):.3f}"
          f"   sd {st.pstdev([x['nstar'] for x in v]):.3f}")
print()
print("      and within each, how does n* depend on ℓ?\n")
for lab,v in (("penetrating",pen),("non-penetrating",non)):
    if len(v)<8: continue
    r=SS.linregress([x["l"] for x in v],[x["nstar"] for x in v])
    print(f"      {lab:<18}n* on ℓ: slope {r.slope:+.3f}, r² {r.rvalue**2:.3f}, p {r.pvalue:.1e}")