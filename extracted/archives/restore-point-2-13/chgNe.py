import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]
# add the mercury-core captures
ROWS=list(ROWS)+[dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
                 dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
                 dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
print("  DOES THE CHARGE EXPONENT DEPEND ON Nₑ?\n")
print("      fit δ ∝ c^(−x) within each isoelectronic sequence and see how x")
print("      varies with the electron count.\n")
seq=defaultdict(dict)
for r in ROWS: seq[(r["ne"],r["l"])][r["c"]]=r["d"]
pts=[]
print(f"      {'Nₑ':>5}{'ℓ':>3}{'charges':>9}{'x':>9}{'r²':>8}")
L="spdfg"
for (ne,l),d in sorted(seq.items()):
    if len(d)<3: continue
    cs=sorted(d)
    ys=np.array([d[c] for c in cs])
    if ys.min()<0.05: continue
    r=SS.linregress(np.log(cs),np.log(ys))
    if r.rvalue**2<0.8: continue
    print(f"      {ne:>5}{L[l]:>3}{len(cs):>9}{-r.slope:>9.3f}{r.rvalue**2:>8.4f}")
    pts.append((ne,-r.slope))
print()
if len(pts)>=5:
    ne=np.array([a for a,_ in pts],float); x=np.array([b for _,b in pts])
    for nm,f in (("x vs Nₑ",ne),("x vs ln Nₑ",np.log(ne)),
                 ("x vs Nₑ^(-1/3)",ne**-(1/3)),("x vs 1/Nₑ",1/ne)):
        r=SS.linregress(f,x)
        print(f"      {nm:<18}slope {r.slope:+.5f}   r² {r.rvalue**2:.4f}   p {r.pvalue:.4f}")
    print()
    r=SS.linregress(np.log(ne),x)
    print(f"      x(Nₑ) = {r.intercept:.4f} {r.slope:+.4f}·ln Nₑ")
    for n_ in (12,20,40,80):
        print(f"          Nₑ = {n_:>3}:  x = {r.intercept+r.slope*math.log(n_):.3f}")
    print()
    print("      measured directly: Nₑ = 80 gives x = 0.14 from Tl/Pb/Bi")
