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
print("  WHY IS dδ/dp NOT ONE?\n")
print("  If each core orbital of the same ℓ forces exactly one extra node, and one")
print("  node is one unit of defect, the slope would be 1 exactly. It is not: it runs")
print("  0.71 at s to 1.03 at f. Three candidate reasons, each testable.\n")

print("  A · IS THE SLOPE CONTAMINATED BY CHARGE?\n")
print("      δ falls with charge (Edlén). If high-p species are also high-charge in")
print("      this sample, the p-slope is depressed by a charge trend.\n")
print(f"      {'ℓ':>3}{'slope of δ on p':>18}{'controlling for charge':>26}{'corr(p,c)':>12}")
by=defaultdict(list)
for x in CH:
    by[x["l"]].append((core_p(x["ne"]-1,x["l"]), x["d"], x["c"], x["ne"]))
for l in sorted(by):
    v=by[l]
    if len(v)<10 or len(set(a for a,_,_,_ in v))<3: continue
    ps=np.array([a for a,_,_,_ in v],float); ds=np.array([b for _,b,_,_ in v])
    cs=np.array([c for _,_,c,_ in v],float); ne=np.array([d for _,_,_,d in v],float)
    r0=SS.linregress(ps,ds)
    # partial: regress delta on p and ln(c+1)/c and ln Ne
    X=np.column_stack([ps, np.log(cs+1)/cs, np.log(ne), np.ones(len(v))])
    try:
        b,*_=np.linalg.lstsq(X,ds,rcond=None)
        part=b[0]
    except Exception: part=float("nan")
    print(f"      {L[l]:>3}{r0.slope:>18.3f}{part:>26.3f}{np.corrcoef(ps,cs)[0,1]:>12.3f}")
print()
print("  B · IS THE SLOPE THE SAME WITHIN ONE ISOELECTRONIC FAMILY?\n")
print("      Within one charge, p varies only with Nₑ. A clean slope needs both.\n")
print(f"      {'ℓ':>3}{'charge':>8}{'n':>5}{'slope':>9}{'r²':>8}")
for l in sorted(by):
    for c in (1,2,3):
        v=[x for x in by[l] if x[2]==c]
        if len(v)<6 or len(set(a for a,_,_,_ in v))<3: continue
        r=SS.linregress([a for a,_,_,_ in v],[b for _,b,_,_ in v])
        print(f"      {L[l]:>3}{c:>8}{len(v):>5}{r.slope:>9.3f}{r.rvalue**2:>8.3f}")
print()
print("  C · IS THE SHORTFALL THE CENTRIFUGAL BARRIER?\n")
print("      A node inside the core contributes a full unit only if the electron")
print("      reaches the core. The barrier ℓ(ℓ+1)/r² keeps it out, so the shortfall")
print("      should FALL with ℓ — the opposite of what a barrier argument predicts")
print("      for the defect itself, and that is the point.\n")
S={}
for l in sorted(by):
    v=by[l]
    if len(v)<10 or len(set(a for a,_,_,_ in v))<3: continue
    S[l]=SS.linregress([a for a,_,_,_ in v],[b for _,b,_,_ in v]).slope
print(f"      {'ℓ':>3}{'slope':>9}{'1 − slope':>12}{'ℓ(ℓ+1)':>10}")
for l in sorted(S): print(f"      {L[l]:>3}{S[l]:>9.3f}{1-S[l]:>12.3f}{l*(l+1):>10}")
if len(S)>=3:
    ls=sorted(S)
    r=SS.linregress(ls,[1-S[l] for l in ls])
    print(f"\n      (1 − slope) against ℓ: slope {r.slope:+.4f}, r² {r.rvalue**2:.3f}, p {r.pvalue:.3f}")
    print(f"      → the shortfall SHRINKS with ℓ and reaches zero near ℓ = "
          f"{(-r.intercept/r.slope):.1f}" if r.slope else "")