import math
import numpy as np
from collections import Counter
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
PEN,OUT,ROWS=g["PEN"],g["OUT"],g["ROWS"]
config,core_p,thresh,ORDER=g["config"],g["core_p"],g["thresh"],g["ORDER"]
print("  WHERE IS p CONSTRAINED?\n")
c=Counter(r["p"] for r in PEN)
print("      measured p values: " + "  ".join(f"{k}:{v}" for k,v in sorted(c.items())))
print(f"      max p in data = {max(c)}")
print()
print("      but the filling test reaches p = 7 at 8s for Z ≈ 90-103,")
print("      and p = 6 at 7s. The exponent is UNCONSTRAINED there, so ½ and")
print("      the saturating form agree on the data and differ on extrapolation.\n")
for p in range(1,9):
    print(f"      p = {p}:  √p = {math.sqrt(p):.3f}   p^0.58 = {p**0.58:.3f}   "
          f"p^(0.83−0.09ln30) = {p**(0.83-0.09*math.log(30)):.3f}")
print()
print("  REFIT WITH e FREE, TWO LADDERS, SHARED k\n")
P=np.array([r["p"] for r in PEN],float); NE=np.array([r["ne"] for r in PEN],float)
C=np.array([r["c"] for r in PEN],float); Y=np.array([r["d"] for r in PEN])
T1=np.log(C+1)/C
Z2=np.array([r["Z"] for r in OUT],float); T2=np.array([r["T"] for r in OUT],float)
NE2=np.array([r["ne"] for r in OUT],float); C2=np.array([r["c"] for r in OUT],float)
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def joint(_,a,e,h,w,k):
    p1=a*np.power(np.maximum(P,1e-9),e)*NE**k*T1
    p2=h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2
    return np.concatenate([p1,p2])
best=None
for p0 in ([0.42,0.5,0.64,3.7,0.48],[0.38,0.6,0.6,3.6,0.5],[0.3,0.8,0.55,4,0.5]):
    try:
        pr,_=curve_fit(joint,np.arange(len(YA)),YA,p0=p0,maxfev=800000)
        rr=YA-joint(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-joint(None,*pr)
print(f"      a={pr[0]:.4f}  e={pr[1]:.4f}  h={pr[2]:.4f}  w={pr[3]:.4f}  k={pr[4]:.4f}")
print(f"      FIVE parameters · rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}")
np.save("/tmp/eq5.npy",pr)
a,e,h,w,k=pr
def delta(Z,c,l):
    ne=Z-c+1; p=core_p(ne-1,l); t=math.log(c+1)/c
    if p>=1: return a*p**e*ne**k*t
    D=Z-thresh(ne-1,l); x=max(-60.,min(60.,D/w))
    return h*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for A,B,O in cfg:
        if A==n and B==l: return O
    return 0
ok=bad=0; BAD=[]
for Z in range(3,104):
    ne=Z; cfg=config(ne-1); full=config(ne)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(cfg,n,l)>=cap(l): continue
        if n!=core_p(ne-1,l)+l+1 and occ(cfg,n,l)==0: continue
        cand.append((n,l,n-delta(Z,1,l)))
    if len(cand)<2: continue
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(cfg,n,l): got=(n,l); break
    if got is None: continue
    pick=min(cand,key=lambda x:x[2])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,pick))
print(f"\n      filling order: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
if BAD:
    L="spdfg"
    print("      failures: " + "  ".join(
        f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z,gt,pk in BAD[:12]))