import math
import numpy as np
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
H=g["H"]; OPEN=g["OPEN"]; ORDER=g["ORDER"]
L="spdfg"
MAD=list(ORDER); HYD=sorted(MAD,key=lambda t:(t[0],t[1]))
def build(ne,order):
    left,out=ne,[]
    for n,l in order:
        if left<=0: break
        cap=2*(2*l+1); o=min(left,cap); out.append((n,l,o)); left-=o
    return out
def cfg_c(ne,c): return build(ne, MAD if c<=1 else HYD)
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
    R.append(dict(Z=Z,c=c,l=l,d=d,ne=ne,p=cp(ne-1,l,c),
                  ol=out_(ne-1,c)[1],T=thr_(ne-1,l,c)))
PEN=[r for r in R if r["p"]>=1]; OUT=[r for r in R if r["p"]==0]
print(f"  REFIT WITH CHARGE-DEPENDENT CONFIGURATIONS\n")
print(f"      {len(R)} channels · {len(PEN)} penetrating · {len(OUT)} outer-well\n")
def A(rows,k): return np.array([r[k] for r in rows],float)
P,NE,C,OL=A(PEN,"p"),A(PEN,"ne"),A(PEN,"c"),A(PEN,"ol")
Y=np.array([r["d"] for r in PEN]); T1=np.log(C+1)/C
Z2,T2,NE2,C2=A(OUT,"Z"),A(OUT,"T"),A(OUT,"ne"),A(OUT,"c")
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def M(_,a,b,h,w,k):
    return np.concatenate([
      (a+b*OL)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2])
best=None
for p0 in ([0.376,-0.026,0.537,3.60,0.535],[0.4,0.0,0.6,4,0.5]):
    try:
        pr,_=curve_fit(M,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
        rr=YA-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-M(None,*pr); a,b,h,w,k=pr
print(f"      a={a:.4f}  b={b:+.4f}  h={h:.4f}  w={w:.4f}  k={k:.4f}")
print(f"      rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}")
print(f"      (aufbau-input version: rms 0.1176 · R² 0.9814)\n")
np.save("/tmp/eqc.npy",pr)
def delta(Z,c,l):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    if p>=1: return (a+b*out_(ne-1,c)[1])*math.sqrt(p)*ne**k*t
    Dd=Z-thr_(ne-1,l,c); x=max(-60.,min(60.,Dd/w))
    return h*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for X,Yl,O in cfg:
        if X==n and Yl==l: return O
    return 0
ok=bad=0; BAD=[]
for Z in range(3,104):
    ne=Z; c1=cfg_c(ne-1,1); full=cfg_c(ne,1)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(c1,n,l)>=cap(l): continue
        if n!=cp(ne-1,l,1)+l+1 and occ(c1,n,l)==0: continue
        cand.append((n,l,n-delta(Z,1,l)))
    if len(cand)<2: continue
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(c1,n,l): got=(n,l); break
    if got is None: continue
    pick=min(cand,key=lambda x:x[2])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,pick))
print(f"      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)   "
      f"(was 91.1%)")
if BAD:
    from collections import Counter
    cnt=Counter(f"{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for _,gt,pk in BAD)
    print("      failures: " + "  ".join(f"{a_} ×{v}" for a_,v in cnt.most_common()))