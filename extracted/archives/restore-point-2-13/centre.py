import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
OUT=g["OUT"]; L="spdfg"
print("  WHERE IS THE COLLAPSE CENTRE, MEASURED FROM THE DEFECTS?\n")
print("      The outer-well branch is δ = h·σ((Z−T+Δ)/w)·(...). The 163 measured")
print("      outer-well channels can locate Δ without any reference to filling.\n")
print("      the four block openings, T = OPEN[(n₀,ℓ)]:\n")
print("          3d → 21    4d → 39    4f → 57    5f → 89\n")
by=defaultdict(list)
for r in OUT: by[r["l"]].append(r)
print(f"      {'ℓ':>3}{'n':>5}{'Z range':>12}{'T range':>12}{'median D':>10}")
for l in sorted(by):
    v=by[l]
    if len(v)<6: continue
    Zs=[r["Z"] for r in v]; Ts=[r["T"] for r in v]
    print(f"      {L[l]:>3}{len(v):>5}{f'{min(Zs)}–{max(Zs)}':>12}"
          f"{f'{min(Ts)}–{max(Ts)}':>12}{st.median([r['Z']-r['T'] for r in v]):>10.1f}")
print()
print("  FITTING THE OUTER-WELL BRANCH ALONE, WITH A FREE CENTRE\n")
def A(rows,k): return np.array([r[k] for r in rows],float)
Z2,T2,NE2,C2=A(OUT,"Z"),A(OUT,"T"),A(OUT,"ne"),A(OUT,"c")
L2=A(OUT,"l"); Y2=np.array([r["d"] for r in OUT])
D=Z2-T2; CH2=np.log(C2+1)/C2
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def rep(name,f,p0s,npar):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(Y2)),Y2,p0=p0,maxfev=900000)
            rr=Y2-f(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {name:<40}{npar:>4}   failed"); return None
    pr,s=best; rr=Y2-f(None,*pr)
    print(f"      {name:<40}{npar:>4}{s:>10.4f}{1-np.var(rr)/np.var(Y2):>9.4f}")
    return pr
print(f"      {'model':<40}{'par':>4}{'rms':>10}{'R²':>9}")
rep("centre at T  (Δ = 0)",
    lambda _,h,w,k: h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2,
    [[0.62,3.94,0.467]],3)
pr=rep("centre free  (Δ fitted)",
    lambda _,h,w,dd,k: h*sig((D+dd)/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2,
    [[0.62,3.94,2.0,0.467],[0.7,4,5,0.5],[0.6,3,8,0.45]],4)
if pr is not None:
    h,w,dd,k=pr
    print(f"\n      h = {h:.4f}   w = {w:.4f}   Δ = {dd:+.4f}   k = {k:.4f}")
    print(f"      the collapse is centred {dd:.2f} in Z BELOW the block opening")
    print(f"      so at Z = T the sigmoid reads σ({dd/w:.2f}) = {sig(dd/w):.3f}"
          f"  rather than 0.500")
    np.save("/tmp/eqcen.npy",pr)
print()
prl=rep("centre free, Δ proportional to ℓ",
    lambda _,h,w,d1,k: h*sig((D+d1*L2)/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2,
    [[0.62,3.94,1.0,0.467],[0.7,4,2,0.5]],4)
if prl is not None:
    h,w,d1,k=prl
    print(f"\n      Δ(ℓ) = {d1:.3f}·ℓ   →  Δ(d) = {2*d1:.2f}   Δ(f) = {3*d1:.2f}")
    np.save("/tmp/eqcenl.npy",prl)
