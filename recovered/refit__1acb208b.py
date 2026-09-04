import math, statistics as st
import numpy as np
from scipy.optimize import curve_fit
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=list(g["ROWS"])+[
  dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
P=np.array([r["p"] for r in ROWS],float); NE=np.array([r["ne"] for r in ROWS],float)
D=np.array([r["d"] for r in ROWS]); C=np.array([r["c"] for r in ROWS],float)
RG=np.array([r["reg"] for r in ROWS]); LL=np.array([r["l"] for r in ROWS],float)
k=(P>0)&(D>0.02)
Pk,Nk,Ck,Dk,Rk,Lk=P[k],NE[k],C[k],D[k],RG[k],LL[k]
S=np.sqrt(Pk*Nk); G2=(Rk==2).astype(float)
print("  REFITTING A AND THE REGIME-2 FACTOR TOGETHER\n")
def M(_,A,b,x0,x1):
    x=np.maximum(x0+x1*np.log(Nk),0.02)
    return A*(1+b*G2)*S*Ck**(-x)
best=None
for p0 in ([0.255,0.23,0.86,-0.18],[0.25,0.2,0.9,-0.2],[0.3,0.3,0.8,-0.15]):
    try:
        pr,_=curve_fit(M,np.arange(len(Dk)),Dk,p0=p0,maxfev=900000)
        r=Dk-M(None,*pr); s=float(np.sqrt(np.mean(r**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; r=Dk-M(None,*pr); A,b,x0,x1=pr
print(f"      δ = A·(1 + b·[regime 2])·√(pNₑ)·c^(−x₀−x₁lnNₑ)\n")
print(f"      A = {A:.4f}   b = {b:+.4f}   x(Nₑ) = {x0:.4f} {x1:+.4f}·ln Nₑ")
print(f"      {len(Dk)} channels · rms {s:.4f} · R² {1-np.var(r)/np.var(Dk):.4f}")
print(f"      (one amplitude, no regime factor: rms 0.2457 · R² 0.9310)\n")
print(f"      {'ℓ':>3}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
pred=M(None,*pr)
for l in range(5):
    m=Lk==l
    if m.sum()<5: continue
    q=Dk[m]/pred[m]
    print(f"      {'spdfg'[l]:>3}{int(m.sum()):>5}{st.median(q):>15.3f}{st.pstdev(q):>8.3f}")
print()
print(f"      {'regime':>7}{'n':>5}{'median δ/pred':>15}")
for rg in (1,2):
    m=Rk==rg
    if m.sum()<5: continue
    print(f"      {rg:>7}{int(m.sum()):>5}{st.median(Dk[m]/pred[m]):>15.3f}")
np.save("/tmp/final_pen.npy",pr)
print()
print("  AND THE OUTER-WELL BRANCH, UNCHANGED\n")
print("      δ = h(ℓ)·σ((Z−T+1.5)/0.40)·(Nₑ−1)/Nₑ·√Nₑ·c^(−x)")
print("      h(d) = 0.40 measured at K→Ca · h(f) = 0.468 from La's ⟨r⟩ = 0.7 a₀")