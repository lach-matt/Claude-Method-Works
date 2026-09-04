import math
import numpy as np
from scipy.optimize import curve_fit
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
ROWS=g["ROWS"]; config,core_p,thresh,ORDER=g["config"],g["core_p"],g["thresh"],g["ORDER"]
def outer(ne):
    cfg=config(ne); return cfg[-1] if cfg else (0,0,0)
for r in ROWS:
    n_,l_,o_=outer(r["ne"]-1); r["on"],r["ol"],r["oo"]=n_,l_,o_
PEN=[r for r in ROWS if r["p"]>=1]; OUT=[r for r in ROWS if r["p"]==0]
def arr(rows,k): return np.array([r[k] for r in rows],float)
P,NE,C=arr(PEN,"p"),arr(PEN,"ne"),arr(PEN,"c"); Y=np.array([r["d"] for r in PEN])
OL=arr(PEN,"ol"); T1=np.log(C+1)/C
Z2,T2,NE2,C2=arr(OUT,"Z"),arr(OUT,"T"),arr(OUT,"ne"),arr(OUT,"c")
Y2=np.array([r["d"] for r in OUT]); D=Z2-T2; CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def M(_,a,b,h,w,k):
    return np.concatenate([
      (a+b*OL)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig(D/max(abs(w),1e-6))*((NE2-1)/NE2)*NE2**k*CH2])
best=None
for p0 in ([0.42,0.0,0.64,3.7,0.475],[0.35,0.05,0.7,4,0.5],[0.5,-0.05,0.6,3,0.45]):
    try:
        pr,_=curve_fit(M,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
        rr=YA-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-M(None,*pr); a,b,h,w,k=pr
print(f"  THE EQUATION WITH THE CORE'S OUTERMOST ℓ\n")
print(f"      penetrating :  δ = (a + b·ℓ_core)·√p · Nₑ^k · ln(c+1)/c")
print(f"      outer well  :  δ = h·σ((Z−T)/w) · (Nₑ−1)/Nₑ · Nₑ^k · ln(c+1)/c\n")
print(f"      a = {a:.4f}   b = {b:+.4f}   h = {h:.4f}   w = {w:.4f}   k = {k:.4f}")
print(f"      284 channels · rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}\n")
np.save("/tmp/eqgs2.npy",pr)
def delta(Z,c,l):
    ne=Z-c+1; p=core_p(ne-1,l); t=math.log(c+1)/c
    n_,l_,o_=outer(ne-1)
    if p>=1: return (a+b*l_)*math.sqrt(p)*ne**k*t
    D_=Z-thresh(ne-1,l); x=max(-60.,min(60.,D_/w))
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
print(f"      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
L="spdfg"
if BAD:
    from collections import Counter
    c=Counter(f"{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for _,gt,pk in BAD)
    print("      failures: " + "  ".join(f"{k} ×{v}" for k,v in c.most_common()))
print()
w0=max(abs(delta(Z,Z,l)) for Z in (1,2,8,26,56,90) for l in range(4))
n0=g["n0"]
badp=sum(1 for r in ROWS if math.floor(delta(r["Z"],r["c"],r["l"]))>
         min(r["p"],n0(r["ne"]-1,r["l"])-r["l"]-1))
print(f"      hydrogenic worst {w0:.6f} · Pauli {len(ROWS)-badp}/{len(ROWS)}")
