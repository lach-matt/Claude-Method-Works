import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=list(g["ROWS"])+[
  dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
L="spdfg"
print("  RE-MEASURING THE CHARGE COEFFICIENT, PROPERLY\n")
print("      x is the slope of ln δ against ln c WITHIN one isoelectronic")
print("      sequence at one ℓ. Nothing else varies there — p is fixed by Nₑ")
print("      and ℓ, so x is measured cleanly. My earlier pass took ALL such")
print("      sequences including ones with two points and low δ.\n")
seq=defaultdict(dict)
for r in ROWS: seq[(r["ne"],r["l"])][r["c"]]=r["d"]
print(f"      {'Nₑ':>5}{'ℓ':>3}{'pts':>5}{'δ range':>16}{'x':>8}{'r²':>8}{'  keep'}")
pts=[]
for (ne,l),d in sorted(seq.items()):
    cs=sorted(d); y=np.array([d[c] for c in cs])
    if len(cs)<3: continue
    keep = (y.min()>0.05) and (max(cs)/min(cs)>=2)
    r=SS.linregress(np.log(cs),np.log(y))
    flag = keep and r.rvalue**2>0.90
    print(f"      {ne:>5}{L[l]:>3}{len(cs):>5}{f'{y.min():.3f}–{y.max():.3f}':>16}"
          f"{-r.slope:>8.3f}{r.rvalue**2:>8.4f}{'   yes' if flag else '   no'}")
    if flag: pts.append((ne,-r.slope,len(cs)))
print()
print(f"  {len(pts)} clean sequences\n")
if len(pts)>=6:
    ne=np.array([a for a,_,_ in pts],float); x=np.array([b for _,b,_ in pts])
    w=np.array([c for _,_,c in pts],float)
    for nm,f in (("x vs ln Nₑ",np.log(ne)),("x vs Nₑ^(−1/3)",ne**-(1/3)),
                 ("x vs Nₑ^(−1/2)",ne**-0.5),("x vs 1/Nₑ",1/ne)):
        r=SS.linregress(f,x)
        print(f"      {nm:<20}r² {r.rvalue**2:.4f}   p {r.pvalue:.2e}"
              f"   → x = {r.intercept:+.4f} {r.slope:+.4f}·f")
    print()
    r=SS.linregress(np.log(ne),x)
    X=np.column_stack([np.log(ne),np.ones(len(x))])
    W=np.diag(w)
    b=np.linalg.solve(X.T@W@X, X.T@W@x)
    print(f"      unweighted : x = {r.intercept:.4f} {r.slope:+.4f}·ln Nₑ")
    print(f"      weighted   : x = {b[1]:.4f} {b[0]:+.4f}·ln Nₑ   (by point count)")
    print()
    print(f"      {'Nₑ':>5}{'unweighted':>13}{'weighted':>11}{'measured':>11}")
    byne=defaultdict(list)
    for a,bb,_ in pts: byne[a].append(bb)
    for n_ in sorted(byne):
        print(f"      {n_:>5}{r.intercept+r.slope*math.log(n_):>13.3f}"
              f"{b[1]+b[0]*math.log(n_):>11.3f}{st.median(byne[n_]):>11.3f}")
    np.save("/tmp/xcoef.npy",np.array([b[1],b[0]]))
