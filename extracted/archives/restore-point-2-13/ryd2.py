import math
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
PEN,OUT=g["PEN"],g["OUT"]; cfg_c,cp,out_,n0_,thr_=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"]
ORDER=g["ORDER"]; L="spdfg"
P,NE,C,DN=g["P"],g["NE"],g["C"],g["DN"]; Y=g["Y"]; T1=g["T1"]
Z2,T2,NE2,C2,Y2,D,CH2=g["Z2"],g["T2"],g["NE2"],g["C2"],g["Y2"],g["D"],g["CH2"]
YA=g["YA"]; sig=g["sig"]
def M(_,a,q,h,w,k):
    return np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2])
best=None
for p0 in ([0.425,0.0,0.584,3.92,0.489],[0.4,0.05,0.6,4,0.5],[0.5,-0.05,0.55,3.5,0.47]):
    try:
        pr,_=curve_fit(M,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
        rr=YA-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-M(None,*pr); a,q,h,w,k=pr
print("  THE RYDBERG-RADIAL EQUATION\n")
print("      penetrating :  δ = (a + q·(n₀−n_out))·√p · Nₑ^k · ln(c+1)/c")
print("      outer well  :  δ = h·σ((Z−T)/w) · (Nₑ−1)/Nₑ · Nₑ^k · ln(c+1)/c\n")
print(f"      a = {a:.4f}   q = {q:+.4f}   h = {h:.4f}   w = {w:.4f}   k = {k:.4f}")
print(f"      rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}\n")
np.save("/tmp/eqrad.npy",pr)
def delta(Z,c,l):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
    if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
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
print(f"      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
if BAD:
    print("      failures: " + "  ".join(
        f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z,gt,pk in BAD))
n0f=g["n0_"]
wz=max(abs(delta(Z,Z,l)) for Z in (1,2,8,26,56,90) for l in range(4))
badp=sum(1 for r in PEN+OUT if math.floor(delta(r["Z"],r["c"],r["l"]))>
         min(r["p"],n0f(r["ne"]-1,r["l"],r["c"])-r["l"]-1))
print(f"\n      hydrogenic worst {wz:.6f} · Pauli {len(PEN)+len(OUT)-badp}/{len(PEN)+len(OUT)}")
