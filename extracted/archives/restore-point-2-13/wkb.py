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
LL=np.array([r["l"] for r in ROWS],float); D=np.array([r["d"] for r in ROWS])
C=np.array([r["c"] for r in ROWS],float); RG=np.array([r["reg"] for r in ROWS])
print("  THE SINGLE-VARIABLE FORM,  δ = A·√(p·Nₑ)·c^(−x)\n")
print("      the WKB phase inside the core is ∫√(2Z_eff/r)dr ~ √(Z·r_core).")
print("      p counts the core shells the Rydberg function must cross, so it")
print("      stands for the radial reach; Nₑ stands for the charge seen.\n")
k=(P>0)&(D>0.02)
x=0.86-0.18*np.log(NE)
T=C**(-np.maximum(x,0.02))
Y=D/T
S=np.sqrt(P*NE)
A=float(np.sum(S[k]*Y[k])/np.sum(S[k]**2))
r=Y[k]-A*S[k]
print(f"      A = {A:.4f}   {int(k.sum())} channels")
print(f"      rms {float(np.sqrt(np.mean(r**2))):.4f}   R² {1-np.var(r)/np.var(Y[k]):.4f}\n")
print("  WHERE IT MISSES — by regime and by ℓ\n")
print(f"      {'regime':>7}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
for rg in (1,2):
    m=k&(RG==rg)
    if m.sum()<5: continue
    q=Y[m]/(A*S[m])
    print(f"      {rg:>7}{int(m.sum()):>5}{st.median(q):>15.3f}{st.pstdev(q):>8.3f}")
print()
print(f"      {'ℓ':>3}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
for l in range(5):
    m=k&(LL==l)
    if m.sum()<5: continue
    q=Y[m]/(A*S[m])
    print(f"      {L[l]:>3}{int(m.sum()):>5}{st.median(q):>15.3f}{st.pstdev(q):>8.3f}")
print()
print("  ADDING ONE ℓ FACTOR — the centrifugal correction the WKB integral wants\n")
print("      the barrier term is (ℓ+½)²/2r², so the phase is reduced by a factor")
print("      depending on (ℓ+½)²/(p·Nₑ) — the ratio of barrier to attraction.\n")
print(f"      {'model':<38}{'rms':>9}{'R²':>9}")
def fit(nm,f,p0):
    from scipy.optimize import curve_fit
    best=None
    for q in p0:
        try:
            pr,_=curve_fit(f,np.arange(int(k.sum())),Y[k],p0=q,maxfev=800000)
            rr=Y[k]-f(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {nm:<38}  failed"); return
    pr,s=best; rr=Y[k]-f(None,*pr)
    print(f"      {nm:<38}{s:>9.4f}{1-np.var(rr)/np.var(Y[k]):>9.4f}   "
          + " ".join(f"{z:+.4f}" for z in pr))
Sk=S[k]; Lk=LL[k]; Pk=P[k]; Nk=NE[k]
fit("A·√(pNₑ)", lambda _,a: a*Sk, [[0.4]])
fit("A·√(pNₑ) − b·(ℓ+½)²/√(pNₑ)",
    lambda _,a,b: a*Sk - b*(Lk+0.5)**2/Sk, [[0.4,0.5],[0.5,1.0]])
fit("A·√(pNₑ − b(ℓ+½)²)",
    lambda _,a,b: a*np.sqrt(np.maximum(Pk*Nk-b*(Lk+0.5)**2,1e-6)), [[0.4,1.0],[0.5,4.0]])
fit("A·√(pNₑ)·exp(−b(ℓ+½)²/(pNₑ))",
    lambda _,a,b: a*Sk*np.exp(-b*(Lk+0.5)**2/(Pk*Nk)), [[0.4,1.0],[0.5,5.0]])
