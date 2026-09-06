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
P=np.array([r["p"] for r in ROWS],float); NE=np.array([r["ne"] for r in ROWS],float)
D=np.array([r["d"] for r in ROWS]); C=np.array([r["c"] for r in ROWS],float)
LL=np.array([r["l"] for r in ROWS],float); RG=np.array([r["reg"] for r in ROWS])
print("  THREE PATHS TO THE CHARGE COEFFICIENT   δ ∝ c^(−x)\n")
print("  PATH 1 · WITHIN-SEQUENCE SLOPES  (Nₑ and ℓ both fixed; p is then fixed too)\n")
seq=defaultdict(dict)
for r in ROWS:
    if r["d"]>0.05: seq[(r["ne"],r["l"])][r["c"]]=r["d"]
pts=[]
for (ne,l),d in sorted(seq.items()):
    if len(d)<3: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.85: continue
    pts.append((ne,l,-rr.slope,rr.rvalue**2,len(cs)))
print(f"      {len(pts)} sequences with r² > 0.85")
xs=np.array([a for a,_,_,_,_ in pts],float); ys=np.array([c for _,_,c,_,_ in pts])
r1=SS.linregress(np.log(xs),ys)
print(f"      x(Nₑ) = {r1.intercept:.4f} {r1.slope:+.4f}·ln Nₑ   r² {r1.rvalue**2:.3f}")
print(f"      weighted by n: ", end="")
w=np.array([e for _,_,_,_,e in pts],float)
b=np.polyfit(np.log(xs),ys,1,w=w)
print(f"x(Nₑ) = {b[1]:.4f} {b[0]:+.4f}·ln Nₑ")
P1=(b[1],b[0])
print()
print("  PATH 2 · FROM THE LOCKED-FIT RESIDUALS  (solve for the x that flattens them)\n")
k=(P>0)&(D>0.02)
S=np.sqrt(P*NE)
# residual ratio must be flat in c:  ln(D/(A·S)) = -x·ln c
Y=np.log(D[k]/S[k]); LC=np.log(C[k]); LN=np.log(NE[k])
Xm=np.column_stack([-LC, -LC*LN, np.ones(len(Y))])
bb,*_=np.linalg.lstsq(Xm,Y,rcond=None)
res=Y-Xm@bb
print(f"      x(Nₑ) = {bb[0]:.4f} {bb[1]:+.4f}·ln Nₑ   (A = {math.exp(bb[2]):.4f})")
print(f"      rms in ln δ {float(np.sqrt(np.mean(res**2))):.4f}")
P2=(bb[0],bb[1])
print()
print("  PATH 3 · THE HYDROGENIC EDGE  (δ → 0 as c → ∞ at fixed Nₑ)\n")
print("      As charge grows at constant electron count the ion becomes hydrogenic,")
print("      so δ must vanish. c^(−x) does that for any x > 0 — the edge fixes the")
print("      FORM, not the value. What it does fix is the RATE, through the")
print("      isoelectronic ladder's own convergence.\n")
print(f"      {'Nₑ':>5}{'ℓ':>3}{'charges':>9}{'δ at max c':>12}{'x':>8}")
p3=[]
for (ne,l),d in sorted(seq.items()):
    if len(d)<4: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.9: continue
    print(f"      {ne:>5}{L[l]:>3}{len(cs):>9}{d[cs[-1]]:>12.4f}{-rr.slope:>8.3f}")
    p3.append((ne,-rr.slope))
if len(p3)>=4:
    r3=SS.linregress(np.log([a for a,_ in p3]),[b_ for _,b_ in p3])
    print(f"\n      restricted to 4+ charge states: x(Nₑ) = {r3.intercept:.4f} "
          f"{r3.slope:+.4f}·ln Nₑ   r² {r3.rvalue**2:.3f}")
    P3=(r3.intercept,r3.slope)
else: P3=None
print()
print("  COMPARISON\n")
print(f"      {'path':<34}{'x(12)':>9}{'x(20)':>9}{'x(40)':>9}{'x(80)':>9}")
for nm,pp in (("1 · within-sequence, weighted",P1),
              ("2 · locked-fit residuals",P2),
              ("3 · sequences with 4+ charges",P3)):
    if pp is None: continue
    print(f"      {nm:<34}" + "".join(
        f"{max(pp[0]+pp[1]*math.log(n),0.02):>9.3f}" for n in (12,20,40,80)))
print(f"      {'measured directly at Nₑ=80':<34}{'':>27}{0.141:>9.3f}")