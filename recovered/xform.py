import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
from scipy.optimize import curve_fit
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=list(g["ROWS"])+[
  dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
L="spdfg"
# the DIRECT measurements of x: within-sequence slopes, one per (Ne, l)
seq=defaultdict(dict)
for r in ROWS:
    if r["d"]>0.05: seq[(r["ne"],r["l"])][r["c"]]=r["d"]
PTS=[]
for (ne,l),d in sorted(seq.items()):
    if len(d)<3: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.85: continue
    PTS.append((ne,l,-rr.slope,len(cs)))
print("  THE DIRECT x MEASUREMENTS — one per (Nₑ, ℓ), nothing fitted through them\n")
print(f"      {'Nₑ':>5}{'ℓ':>3}{'charges':>9}{'x':>9}")
for ne,l,x,n in PTS: print(f"      {ne:>5}{L[l]:>3}{n:>9}{x:>9.3f}")
NEp=np.array([a for a,_,_,_ in PTS],float); XP=np.array([c for _,_,c,_ in PTS])
W=np.array([d for _,_,_,d in PTS],float)
print(f"\n      {len(PTS)} measurements, Nₑ from {int(NEp.min())} to {int(NEp.max())}\n")
print("  FITTING x(Nₑ) — the carrier, weighted by the number of charge states\n")
print(f"      {'form':<34}{'wrms':>9}{'x(12)':>8}{'x(80)':>8}{'x(∞)':>8}")
def wr(f,pr):
    r=(XP-f(NEp,*pr)); return float(np.sqrt(np.sum(W*r**2)/np.sum(W)))
def go(nm,f,p0s,inf):
    best=None
    for q in p0s:
        try:
            pr,_=curve_fit(f,NEp,XP,p0=q,sigma=1/np.sqrt(W),maxfev=800000)
            s=wr(f,pr)
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {nm:<34}  failed"); return None
    pr,s=best
    print(f"      {nm:<34}{s:>9.4f}{f(np.array([12.]),*pr)[0]:>8.3f}"
          f"{f(np.array([80.]),*pr)[0]:>8.3f}{inf(pr):>8.3f}")
    return pr
a=go("x₀ + x₁·ln Nₑ", lambda n,a_,b_: a_+b_*np.log(n),
     [[0.86,-0.18]], lambda p:-999)
b=go("x∞ + (x₀−x∞)·Nₑ^(−α)", lambda n,xi,d_,al: xi+d_*n**(-al),
     [[0.1,1.0,0.5],[0.05,2.0,0.8],[0.15,0.8,0.3]], lambda p:p[0])
c=go("β·Nₑ^(−α)", lambda n,be,al: be*n**(-al),
     [[2.0,0.5],[1.5,0.4]], lambda p:0.0)
d=go("x∞ + (x₀−x∞)/(1+Nₑ/N₀)", lambda n,xi,d_,N0: xi+d_/(1+n/max(abs(N0),1e-3)),
     [[0.1,0.5,20.],[0.12,0.6,15.]], lambda p:p[0])
print()
print("  AGAINST THE Tl/Pb/Bi MEASUREMENT AT Nₑ = 80,  x = 0.141\n")
for nm,f,pr in (("ln form",lambda n,p:p[0]+p[1]*np.log(n),a),
                ("saturating power",lambda n,p:p[0]+p[1]*n**(-p[2]),b),
                ("pure power",lambda n,p:p[0]*n**(-p[1]),c),
                ("saturating rational",lambda n,p:p[0]+p[1]/(1+n/abs(p[2])),d)):
    if pr is None: continue
    v=f(np.array([80.]),pr)[0]
    print(f"      {nm:<22}x(80) = {v:.3f}   error {v-0.141:+.3f}")
np.save("/tmp/xfit.npy",b if b is not None else a)