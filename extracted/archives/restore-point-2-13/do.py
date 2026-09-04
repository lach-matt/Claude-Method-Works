import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; L="spdfg"
print("  THE DEMKOV–OSTROVSKY TEST\n")
print("      V(ρ) = −w·E₀ / [ρ(1+ρ)²]     ρ = r/R,  κ = ½")
print("      Coulomb at small ρ, ρ⁻³ at large ρ. Its levels depend on n+ℓ ALONE.\n")
print("      So the testable claim is about n* = n − δ, not about δ:\n")
print("          n* should be a function of (n+ℓ) alone, within one species.\n")
for r in ROWS:
    r["nl"]=r["n0"]+r["l"]; r["nstar"]=r["n0"]-r["d"]
bysp=defaultdict(list)
for r in ROWS: bysp[(r["Z"],r["c"])].append(r)
print("  1 · HOW MUCH OF n*'s VARIANCE DOES n+ℓ EXPLAIN, WITHIN A SPECIES?\n")
W=[];T=[]
for k,v in bysp.items():
    if len(v)<3: continue
    y=np.array([x["nstar"] for x in v])
    gr=defaultdict(list)
    for x in v: gr[x["nl"]].append(x["nstar"])
    within=sum(np.var(z)*len(z) for z in gr.values())/len(v)
    W.append(within); T.append(float(np.var(y)))
W=np.array(W); T=np.array(T)
ok=T>1e-9
print(f"      {int(ok.sum())} species with 3+ channels")
print(f"      variance of n* explained by n+ℓ : {100*(1-W[ok].sum()/T[ok].sum()):.1f}%")
print()
print("  2 · AND THE SAME FOR δ, FOR COMPARISON\n")
W2=[];T2=[]
for k,v in bysp.items():
    if len(v)<3: continue
    y=np.array([x["d"] for x in v])
    gr=defaultdict(list)
    for x in v: gr[x["nl"]].append(x["d"])
    W2.append(sum(np.var(z)*len(z) for z in gr.values())/len(v)); T2.append(float(np.var(y)))
W2=np.array(W2); T2=np.array(T2); ok2=T2>1e-9
print(f"      variance of δ explained by n+ℓ  : {100*(1-W2[ok2].sum()/T2[ok2].sum()):.1f}%")
print()
print("  3 · IS n* MONOTONE IN n+ℓ?  the Madelung claim itself\n")
ag=dis=0
for k,v in bysp.items():
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            a,b=v[i],v[j]
            if a["nl"]==b["nl"]: continue
            lo,hi=(a,b) if a["nl"]<b["nl"] else (b,a)
            if lo["nstar"]<hi["nstar"]: ag+=1
            else: dis+=1
print(f"      {ag+dis} pairs · monotone in {ag} ({100*ag/(ag+dis):.1f}%)")
print()
print("  4 · THE FORM OF n*(n+ℓ)  —  what the DO potential would fix\n")
gr=defaultdict(list)
for r in ROWS: gr[r["nl"]].append(r["nstar"])
print(f"      {'n+ℓ':>5}{'n':>5}{'median n*':>12}{'sd':>8}")
xs=[];ys=[]
for nl in sorted(gr):
    v=gr[nl]
    if len(v)<4: continue
    print(f"      {nl:>5}{len(v):>5}{st.median(v):>12.3f}{st.pstdev(v):>8.3f}")
    xs.append(nl); ys.append(st.median(v))
if len(xs)>=4:
    r=SS.linregress(xs,ys)
    print(f"\n      n* ≈ {r.intercept:+.3f} {r.slope:+.4f}·(n+ℓ)   r² {r.rvalue**2:.4f}")
    r2=SS.linregress(np.sqrt(xs),ys)
    print(f"      n* ≈ {r2.intercept:+.3f} {r2.slope:+.4f}·√(n+ℓ)  r² {r2.rvalue**2:.4f}")
    r3=SS.linregress(np.log(xs),ys)
    print(f"      n* ≈ {r3.intercept:+.3f} {r3.slope:+.4f}·ln(n+ℓ)  r² {r3.rvalue**2:.4f}")
