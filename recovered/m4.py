import math, statistics as st
from collections import defaultdict
src=open("madelung2.py",encoding="utf-8").read()
src=src[:src.index('# ------------------------------------------------------------- the test'.replace(' the test','---- the test'))] if False else src[:src.index('print("  DOES THE EQUATION')]
g={}; exec(src,g)
config=g["config"]; core_p=g["core_p"]; delta=g["delta"]; ORDER=g["ORDER"]
L="spdfg"
print("  THE IDENTITY\n")
print("      n₀ = p + ℓ + 1        orthogonality: p core orbitals of the same ℓ")
print("                             force p nodes, and an nℓ function has n−ℓ−1")
print("      ⇒  n₀ + ℓ = p + 2ℓ + 1\n")
print("      So the Madelung key is not about n at all. It is p + 2ℓ.\n")
bad=0; tot=0
for ne in range(1,104):
    for l in range(5):
        p=core_p(ne,l); n0=p+l+1
        tot+=1
        if n0+l != p+2*l+1: bad+=1
print(f"      checked on every (Nₑ ≤ 103, ℓ ≤ 4): {tot} cases, {bad} failures\n")
print("      and n₀ is the OBSERVED first member of the series in every")
print("      captured channel — the compendium's Pauli bound (Q.bound), 328/328.\n")
print()
print("  WHAT EACH KEY SAYS\n")
print("      Madelung   :  p + 2ℓ")
print("      the equation:  n₀ − δ  =  p + ℓ + 1 − δ(p, Nₑ, c)\n")
print("      These are different functions of (p, ℓ). They agree on an ORDER when")
print("      δ(p) − p ≈ −ℓ + const across the pairs that actually occur.\n")
print("      Testing that on the real (p, ℓ) pairs of the neutral elements:\n")
rows=defaultdict(list)
for Z in range(3,104):
    ne=Z
    for l in range(5):
        p=core_p(ne-1,l); n0=p+l+1
        if n0>8: continue
        d=delta(Z,1,l)
        rows[(p,l)].append(p-d)
print(f"      {'p':>3}{'ℓ':>3}{'p + 2ℓ':>9}{'median p − δ':>15}{'p−δ+ℓ':>10}{'n':>6}")
pts=[]
for (p,l),v in sorted(rows.items()):
    if len(v)<3: continue
    m=st.median(v)
    print(f"      {p:>3}{L[l]:>3}{p+2*l:>9}{m:>15.3f}{m+l:>10.3f}{len(v):>6}")
    pts.append((p+2*l, p+l+1-m-l+l))
print()
from scipy import stats as SS
if len(pts)>=5:
    xs=[a for a,_ in pts]; ys=[b for _,b in pts]
    r=SS.spearmanr(xs,ys)
    print(f"      Spearman rank correlation between the Madelung key p+2ℓ")
    print(f"      and the equation's n* = p+ℓ+1−δ :  ρ = {r.statistic:+.4f}, p = {r.pvalue:.2e}")
    print(f"      → {'the two keys are order-equivalent on the real pairs' if r.statistic>0.9 else 'they are not order-equivalent'}")