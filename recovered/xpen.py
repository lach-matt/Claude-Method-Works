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
seq=defaultdict(dict); pmap={}
for r in ROWS:
    if r["d"]>0.05:
        seq[(r["ne"],r["l"])][r["c"]]=r["d"]; pmap[(r["ne"],r["l"])]=r["p"]
PTS=[]
for k,d in sorted(seq.items()):
    if len(d)<3 or pmap[k]==0: continue        # PENETRATING only
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.85: continue
    PTS.append((k[0],k[1],-rr.slope,len(cs),rr.rvalue**2))
print("  x MEASURED ON PENETRATING CHANNELS ONLY  (p ≥ 1)\n")
print(f"      {'Nₑ':>5}{'ℓ':>3}{'p':>3}{'chg':>5}{'x':>9}{'r²':>8}")
for ne,l,x,n,r2 in PTS:
    print(f"      {ne:>5}{L[l]:>3}{pmap[(ne,l)]:>3}{n:>5}{x:>9.3f}{r2:>8.4f}")
NE=np.array([a for a,_,_,_,_ in PTS],float); X=np.array([c for _,_,c,_,_ in PTS])
W=np.array([d for _,_,_,d,_ in PTS],float)
print(f"\n      {len(PTS)} measurements, Nₑ {int(NE.min())} to {int(NE.max())}"
      f"   ·   all x > 0, monotone\n")
print("  THE CARRIER, ON THESE ALONE\n")
print(f"      {'form':<28}{'wrms':>9}{'β or x₀':>10}{'α or x₁':>10}{'x(80)':>8}")
def go(nm,f,p0s):
    best=None
    for q in p0s:
        try:
            pr,_=curve_fit(f,NE,X,p0=q,sigma=1/np.sqrt(W),maxfev=800000)
            r=X-f(NE,*pr); s=float(np.sqrt(np.sum(W*r**2)/np.sum(W)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: return None
    pr,s=best
    print(f"      {nm:<28}{s:>9.4f}{pr[0]:>10.4f}{pr[1]:>10.4f}"
          f"{f(np.array([80.]),*pr)[0]:>8.3f}")
    return pr
lg=go("x₀ + x₁·ln Nₑ", lambda n,a,b: a+b*np.log(n), [[0.86,-0.18]])
pw=go("β·Nₑ^(−α)", lambda n,b,a: b*n**(-a), [[1.5,0.4],[2.0,0.5]])
print()
if pw is not None:
    b,al=pw
    print(f"      x(Nₑ) = {b:.4f}·Nₑ^(−{al:.4f})\n")
    print(f"      {'Nₑ':>6}{'measured':>11}{'power':>9}{'log':>9}")
    for ne,l,x,n,r2 in PTS:
        print(f"      {ne:>6}{x:>11.3f}{b*ne**-al:>9.3f}"
              f"{(lg[0]+lg[1]*math.log(ne) if lg is not None else float('nan')):>9.3f}")
    print()
    print(f"      α = {al:.3f}   ·   compare: ⅓ = 0.333, ½ = 0.500, ⅖ = 0.400")
    np.save("/tmp/xpen.npy",pw)
print()
print("  AND THE LOCKED EQUATION WITH THIS x\n")
P=np.array([r["p"] for r in ROWS],float); NEa=np.array([r["ne"] for r in ROWS],float)
D=np.array([r["d"] for r in ROWS]); C=np.array([r["c"] for r in ROWS],float)
RG=np.array([r["reg"] for r in ROWS]); LL=np.array([r["l"] for r in ROWS],float)
k=(P>0)&(D>0.02)
if pw is not None:
    xv=pw[0]*NEa**(-pw[1])
    B=np.sqrt(P*NEa)*C**(-xv)
    A=float(np.sum(B[k]*D[k])/np.sum(B[k]**2))
    r=D[k]-A*B[k]
    print(f"      δ = A·√(pNₑ)·c^(−βNₑ^(−α))     ONE free number\n")
    print(f"      A = {A:.4f}   β = {pw[0]:.4f}   α = {pw[1]:.4f}")
    print(f"      {int(k.sum())} channels · rms {float(np.sqrt(np.mean(r**2))):.4f}"
          f" · R² {1-np.var(r)/np.var(D[k]):.4f}")
    print(f"      (log carrier gave rms 0.2810 · R² 0.9136)\n")
    pred=A*B
    print(f"      {'charge':>7}{'n':>5}{'median δ/pred':>15}")
    for c_ in (1,2,3,4,5):
        m=k&(C==c_)
        if m.sum()<5: continue
        print(f"      {c_:>7}{int(m.sum()):>5}{st.median(D[m]/pred[m]):>15.3f}")