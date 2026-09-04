import math
import numpy as np
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
PEN,OUT,ROWS=g["PEN"],g["OUT"],g["ROWS"]
core_p,thresh,n0=g["core_p"],g["thresh"],g["n0"]
P=np.array([r["p"] for r in PEN],float); NE=np.array([r["ne"] for r in PEN],float)
C=np.array([r["c"] for r in PEN],float); Y=np.array([r["d"] for r in PEN])
T1=np.log(C+1)/C
Z2=np.array([r["Z"] for r in OUT],float); T2=np.array([r["T"] for r in OUT],float)
NE2=np.array([r["ne"] for r in OUT],float); C2=np.array([r["c"] for r in OUT],float)
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def fitit(name, f, p0s, Yv):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(Yv)),Yv,p0=p0,maxfev=800000)
            r=Yv-f(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: return None
    pr,s=best; r=Yv-f(None,*pr)
    print(f"      {name:<42}{len(pr):>3}{s:>10.4f}{1-np.var(r)/np.var(Yv):>9.4f}")
    return pr,s
print("  REDUCING THE PENETRATING LADDER\n")
print(f"      {'form':<42}{'par':>3}{'rms':>10}{'R²':>9}")
fitit("a·p^(e₀+e₁lnNₑ)·Nₑ^k·t", lambda _,a,e0,e1,k:
      a*np.power(np.maximum(P,1e-9),np.maximum(e0+e1*np.log(np.maximum(NE,2)),.05))*NE**k*T1,
      [[0.42,0.49,0.003,0.474]], Y)
fitit("a·p^e·Nₑ^k·t   (e free, constant)", lambda _,a,e,k:
      a*np.power(np.maximum(P,1e-9),e)*NE**k*T1, [[0.42,0.49,0.474]], Y)
r_half=fitit("a·√p·Nₑ^k·t   (e = ½ EXACTLY)", lambda _,a,k:
      a*np.sqrt(np.maximum(P,1e-9))*NE**k*T1, [[0.42,0.474]], Y)
fitit("a·√p·√Nₑ·t    (both = ½ EXACTLY)", lambda _,a:
      a*np.sqrt(np.maximum(P,1e-9))*np.sqrt(NE)*T1, [[0.42]], Y)
print()
print("  REDUCING THE OUTER-WELL LADDER\n")
print(f"      {'form':<42}{'par':>3}{'rms':>10}{'R²':>9}")
fitit("h·σ((Z−T)/w)·(Nₑ−1)/Nₑ·Nₑ^k·t", lambda _,h,w,k:
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2, [[0.7,3.7,0.44]], Y2)
fitit("h·σ((Z−T)/w)·(Nₑ−1)/Nₑ·√Nₑ·t  (k = ½)", lambda _,h,w:
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*np.sqrt(NE2)*CH2, [[0.7,3.7]], Y2)
print()
print("  THE SHARED-k TEST — one exponent for both ladders\n")
def joint(_,a,h,w,k):
    p1=a*np.sqrt(np.maximum(P,1e-9))*NE**k*T1
    p2=h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2
    return np.concatenate([p1,p2])
YA=np.concatenate([Y,Y2])
best=None
for p0 in ([0.42,0.7,3.7,0.47],[0.5,0.8,4.0,0.5]):
    try:
        pr,_=curve_fit(joint,np.arange(len(YA)),YA,p0=p0,maxfev=800000)
        rr=YA-joint(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-joint(None,*pr)
print(f"      a = {pr[0]:.4f}  h = {pr[1]:.4f}  w = {pr[2]:.4f}  k = {pr[3]:.4f}")
print(f"      FOUR parameters · {len(YA)} channels · rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}")
np.save("/tmp/eq4.npy",pr)
print()
def joint3(_,a,h,w):
    p1=a*np.sqrt(np.maximum(P,1e-9))*np.sqrt(NE)*T1
    p2=h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*np.sqrt(NE2)*CH2
    return np.concatenate([p1,p2])
best=None
for p0 in ([0.42,0.7,3.7],[0.5,0.8,4.0]):
    try:
        pr3,_=curve_fit(joint3,np.arange(len(YA)),YA,p0=p0,maxfev=800000)
        rr3=YA-joint3(None,*pr3); s3=float(np.sqrt(np.mean(rr3**2)))
        if best is None or s3<best[1]: best=(pr3,s3)
    except Exception: pass
pr3,s3=best; rr3=YA-joint3(None,*pr3)
print(f"      with k = ½ FIXED: a = {pr3[0]:.4f}  h = {pr3[1]:.4f}  w = {pr3[2]:.4f}")
print(f"      THREE parameters · rms {s3:.4f} · R² {1-np.var(rr3)/np.var(YA):.4f}")
np.save("/tmp/eq3.npy",pr3)
