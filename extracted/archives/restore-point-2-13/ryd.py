import math
import numpy as np
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
H=g["H"]; OPEN=g["OPEN"]; ORDER=g["ORDER"]; L="spdfg"
MAD=list(ORDER); HYD=sorted(MAD,key=lambda t:(t[0],t[1]))
def build(ne,order):
    left,out=ne,[]
    for n,l in order:
        if left<=0: break
        cap=2*(2*l+1); o=min(left,cap); out.append((n,l,o)); left-=o
    return out
def cfg_c(ne,c): return build(ne, MAD if c<=2 else HYD)
def cp(ne,l,c): return sum(1 for n,ll,o in cfg_c(ne,c) if ll==l and o>0)
def out_(ne,c):
    z=cfg_c(ne,c); return z[-1] if z else (0,0,0)
def n0_(ne,l,c):
    v=[n for n,ll,o in cfg_c(ne,c) if ll==l and o>0]
    return (max(v)+1) if v else l+1
def thr_(ne,l,c): return OPEN.get((n0_(ne,l,c),l),9999)
def parents(cfg):
    if not cfg: return 1
    n,l,occ=cfg[-1]; cap=2*(2*l+1)
    return 1 if occ in (0,cap,1,cap-1) else {0:1,1:3,2:16,3:119}.get(l,8)
R=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if parents(cfg_c(ne-1,c))>1: continue
    n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
    R.append(dict(Z=Z,c=c,l=l,d=d,ne=ne,p=cp(ne-1,l,c),ol=l_,on=n_,
                  n0=n0,T=thr_(ne-1,l,c),dn=n0-n_,dl=l-l_))
PEN=[r for r in R if r["p"]>=1]; OUT=[r for r in R if r["p"]==0]
def A(rows,k): return np.array([r[k] for r in rows],float)
P,NE,C,OL,DN,DL=A(PEN,"p"),A(PEN,"ne"),A(PEN,"c"),A(PEN,"ol"),A(PEN,"dn"),A(PEN,"dl")
N0=A(PEN,"n0"); Y=np.array([r["d"] for r in PEN]); T1=np.log(C+1)/C
Z2,T2,NE2,C2=A(OUT,"Z"),A(OUT,"T"),A(OUT,"ne"),A(OUT,"c")
DN2,DL2,N02=A(OUT,"dn"),A(OUT,"dl"),A(OUT,"n0")
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
print("  A VARIABLE FOR THE RYDBERG ELECTRON ITSELF\n")
print("      angular : ℓ − ℓ_core   — the gate, already used")
print("      RADIAL  : n₀ − n_out   — how many shells above the core it starts\n")
from collections import Counter
print("      distribution of n₀ − n_out: " + "  ".join(
    f"{k}:{v}" for k,v in sorted(Counter(r["dn"] for r in R).items())))
print()
def rep(name,f,p0s,npar):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
            rr=YA-f(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {name:<44}{npar:>4}    failed"); return None
    pr,s=best; rr=YA-f(None,*pr)
    print(f"      {name:<44}{npar:>4}{s:>10.4f}{1-np.var(rr)/np.var(YA):>9.4f}")
    return pr
print(f"      {'model':<44}{'par':>4}{'rms':>10}{'R²':>9}")
rep("current: (a+b·ℓ_core)√p·Nₑ^k | h·σ(D/w)",
    lambda _,a,b,h,w,k: np.concatenate([
      (a+b*OL)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.425,-0.022,0.584,3.92,0.489]],5)
pr=rep("+ (n₀−n_out) in the penetrating amplitude",
    lambda _,a,b,q,h,w,k: np.concatenate([
      (a+b*OL+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.425,-0.022,0.0,0.584,3.92,0.489]],6)
rep("(n₀−n_out) INSTEAD of ℓ_core",
    lambda _,a,q,h,w,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.425,0.0,0.584,3.92,0.489]],5)
rep("+ (n₀−n_out) in the outer-well amplitude too",
    lambda _,a,b,h,u,w,k: np.concatenate([
      (a+b*OL)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      (h+u*DN2)*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.425,-0.022,0.584,0.0,3.92,0.489]],6)
rep("√(p/(n₀−n_out+1)) — a radial dilution",
    lambda _,a,b,h,w,k: np.concatenate([
      (a+b*OL)*np.sqrt(np.maximum(P,1e-9)/(DN+1))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.425,-0.022,0.584,3.92,0.489]],5)
if pr is not None: np.save("/tmp/eqr.npy",pr)
