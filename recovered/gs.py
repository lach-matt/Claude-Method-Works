import math
import numpy as np
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
PEN,OUT,ROWS=g["PEN"],g["OUT"],g["ROWS"]
config,core_p,thresh,ORDER=g["config"],g["core_p"],g["thresh"],g["ORDER"]
def outer(ne):
    cfg=config(ne); return cfg[-1] if cfg else (0,0,0)
print("  WHAT THE GROUND STATE KNOWS THAT THE EQUATION DOES NOT\n")
print("      currently used : p (count at this ℓ) · Nₑ · c · T (a lookup in the")
print("                       aufbau order — the sequence we are trying to derive)")
print("      NOT used       : the core's outermost subshell (n, ℓ, occupancy),")
print("                       which carries 46% of frac(δ)'s variance\n")
for r in ROWS:
    n_,l_,o_=outer(r["ne"]-1)
    r["on"],r["ol"],r["oo"]=n_,l_,o_
    r["dl"]=r["l"]-l_
    r["dn"]=r["ne"]-1 - 0
    r["fill"]=o_/(2*(2*l_+1)) if l_<=6 else 0.0
PEN=[r for r in ROWS if r["p"]>=1]; OUT=[r for r in ROWS if r["p"]==0]
def arr(rows,k): return np.array([r[k] for r in rows],float)
P,NE,C,Y=arr(PEN,"p"),arr(PEN,"ne"),arr(PEN,"c"),np.array([r["d"] for r in PEN])
OL,OO,FI,DL=arr(PEN,"ol"),arr(PEN,"oo"),arr(PEN,"fill"),arr(PEN,"dl")
T1=np.log(C+1)/C
Z2,T2,NE2,C2=arr(OUT,"Z"),arr(OUT,"T"),arr(OUT,"ne"),arr(OUT,"c")
L2,OL2,FI2,DL2=arr(OUT,"l"),arr(OUT,"ol"),arr(OUT,"fill"),arr(OUT,"dl")
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def rep(name,f,p0s,npar):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
            rr=YA-f(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {name:<46}{npar:>4}   failed"); return None
    pr,s=best; rr=YA-f(None,*pr)
    print(f"      {name:<46}{npar:>4}{s:>10.4f}{1-np.var(rr)/np.var(YA):>9.4f}")
    return pr
print(f"      {'model':<46}{'par':>4}{'rms':>10}{'R²':>9}")
rep("baseline: √p · Nₑ^k · t  |  h·σ(D/w)",
    lambda _,a,h,w,k: np.concatenate([
      a*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.42,0.64,3.7,0.475]],4)
rep("+ core-outer ℓ in the penetrating amplitude",
    lambda _,a,b,h,w,k: np.concatenate([
      (a+b*OL)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.42,0.0,0.64,3.7,0.475]],5)
rep("+ core-outer FILLING fraction in both",
    lambda _,a,b,h,q,w,k: np.concatenate([
      (a+b*FI)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      (h+q*FI2)*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.42,0.0,0.64,0.0,3.7,0.475]],6)
pr=rep("+ ℓ−ℓ_core shifts the collapse centre",
    lambda _,a,h,w,u,k: np.concatenate([
      a*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig((D+u*DL2)/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.42,0.64,3.7,1.0,0.475],[0.4,0.7,4,3.0,0.5]],5)
pr2=rep("+ collapse centre shifted by ℓ itself",
    lambda _,a,h,w,u,k: np.concatenate([
      a*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig((D+u*L2)/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.42,0.64,3.7,1.0,0.475],[0.4,0.7,4,3.0,0.5]],5)
if pr2 is not None:
    np.save("/tmp/eqgs.npy",pr2)
    a,h,w,u,k=pr2
    print(f"\n      a={a:.4f} h={h:.4f} w={w:.4f} u={u:.4f} k={k:.4f}")
    print(f"      the collapse centre sits {u:.2f}·ℓ BELOW the block opening")