import math
import numpy as np
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
PEN,OUT=g["PEN"],g["OUT"]
config,core_p,thresh,ORDER=g["config"],g["core_p"],g["thresh"],g["ORDER"]
P=np.array([r["p"] for r in PEN],float); NE=np.array([r["ne"] for r in PEN],float)
C=np.array([r["c"] for r in PEN],float); Y=np.array([r["d"] for r in PEN])
T1=np.log(C+1)/C
Z2=np.array([r["Z"] for r in OUT],float); T2=np.array([r["T"] for r in OUT],float)
NE2=np.array([r["ne"] for r in OUT],float); C2=np.array([r["c"] for r in OUT],float)
L2=np.array([r["l"] for r in OUT],float)
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
print("  THE COLLAPSE WIDTH AGAINST ℓ\n")
print("      The barrier is ℓ(ℓ+1)/r². A higher barrier makes a deeper outer well")
print("      and a SHARPER transition when the inner well finally wins. So w should")
print("      FALL with ℓ, and 4f should collapse more abruptly than 3d.\n")
def joint(_,a,h,w0,w1,k):
    p1=a*np.sqrt(np.maximum(P,1e-9))*NE**k*T1
    W=np.maximum(w0+w1*L2,0.3)
    p2=h*sig(D/W)*((NE2-1)/NE2)*NE2**k*CH2
    return np.concatenate([p1,p2])
best=None
for p0 in ([0.42,0.64,6.0,-1.0,0.475],[0.4,0.6,8,-1.5,0.5],[0.39,0.7,5,-0.8,0.48]):
    try:
        pr,_=curve_fit(joint,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
        rr=YA-joint(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-joint(None,*pr)
a,h,w0,w1,k=pr
print(f"      a={a:.4f}  h={h:.4f}  w(ℓ)={w0:.3f}{w1:+.3f}·ℓ  k={k:.4f}")
print(f"      rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}")
print(f"      w(d)={w0+2*w1:.2f}   w(f)={w0+3*w1:.2f}   w(g)={w0+4*w1:.2f}")
np.save("/tmp/eqw.npy",pr)
def delta(Z,c,l):
    ne=Z-c+1; p=core_p(ne-1,l); t=math.log(c+1)/c
    if p>=1: return a*math.sqrt(p)*ne**k*t
    D_=Z-thresh(ne-1,l); W=max(w0+w1*l,0.3)
    x=max(-60.,min(60.,D_/W))
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
print(f"\n      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
L="spdfg"
if BAD:
    print("      failures: " + "  ".join(
        f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z,gt,pk in BAD[:14]))