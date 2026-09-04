import math
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
R=g["R"]; cfg_c,cp,out_,n0_,thr_,ORDER=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"],g["ORDER"]
L="spdfg"
H0=0.37/math.sqrt(6)          # h(d) = 0.37 MEASURED at K -> Ca; scaled by sqrt(l(l+1))
PEN=[r for r in R if r["p"]>=1]; OUT=[r for r in R if r["p"]==0]
def A(rows,k_): return np.array([r[k_] for r in rows],float)
P,NE,C=A(PEN,"p"),A(PEN,"ne"),A(PEN,"c"); DN=A(PEN,"n0")-A(PEN,"on")
Y=np.array([r["d"] for r in PEN]); T1=np.log(C+1)/C
NE2,C2,L2=A(OUT,"ne"),A(OUT,"c"),A(OUT,"l")
Z2,T2=A(OUT,"Z"),A(OUT,"T"); D=Z2-T2
Y2=np.array([r["d"] for r in OUT]); CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2]); BAR=np.sqrt(np.maximum(L2*(L2+1),1e-9))
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def M(_,a,q,k):
    return np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      H0*BAR*sig((D+1.5)/0.40)*((NE2-1)/NE2)*NE2**k*CH2])
best=None
for p0 in ([0.475,-0.040,0.467],[0.5,-0.03,0.5]):
    try:
        pr,_=curve_fit(M,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
        rr=YA-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; rr=YA-M(None,*pr); a,q,k=pr
print("  h(d) FIXED AT ITS MEASURED VALUE, SCALED BY THE BARRIER\n")
print(f"      h₀ = 0.37/√6 = {H0:.4f}   →   h(d)=0.370  h(f)={H0*math.sqrt(12):.3f}"
      f"  h(g)={H0*math.sqrt(20):.3f}")
print(f"      a = {a:.4f}   q = {q:+.4f}   k = {k:.4f}     THREE fitted numbers")
print(f"      rms {s:.4f} · R² {1-np.var(rr)/np.var(YA):.4f}\n")
def delta(Z,c,l):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
    if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
    T=thr_(ne-1,l,c); x=max(-60.,min(60.,(Z-T+1.5)/0.40))
    return H0*math.sqrt(l*(l+1))*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
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
if BAD: print("      failures: " + "  ".join(
    f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z,gt,pk in BAD))
wz=max(abs(delta(Z,Z,l)) for Z in (1,2,8,26,56,90) for l in range(4))
badp=sum(1 for r in R if math.floor(delta(r["Z"],r["c"],r["l"]))>
         min(r["p"],n0_(r["ne"]-1,r["l"],r["c"])-r["l"]-1))
print(f"      hydrogenic {wz:.6f} · Pauli {len(R)-badp}/{len(R)}")
np.save("/tmp/eqbest.npy",np.array([a,q,k,H0]))
