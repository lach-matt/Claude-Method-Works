import math
import numpy as np
from scipy.optimize import curve_fit
from collections import Counter
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
R=g["R"]; cfg_c,cp,out_,n0_,thr_,ORDER=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"],g["ORDER"]
L="spdfg"
for r in R:
    r["inside"] = 1 if (r["p"]>=1 and r["n0"]<=r["on"]) else 0
    r["reg"] = (1 if (r["p"]>=1 and r["n0"]>r["on"]) else
                2 if r["p"]>=1 else
                3 if r["Z"]<r["T"] else 4)
print("  THE FOUR REGIMES, IN THE MEASURED SET\n")
c=Counter(r["reg"] for r in R)
NM={1:"penetrating, outside the core",2:"penetrating, radially INSIDE",
    3:"outer well, uncollapsed",4:"outer well, collapsed"}
for k in sorted(c): print(f"      {k}  {NM[k]:<34}{c[k]:>5} channels")
print()
PEN1=[r for r in R if r["reg"]==1]; PEN2=[r for r in R if r["reg"]==2]
OUTa=[r for r in R if r["reg"]>=3]
def A(rows,k_): return np.array([r[k_] for r in rows],float)
def blk(rows):
    return (A(rows,"p"),A(rows,"ne"),A(rows,"c"),A(rows,"n0")-A(rows,"on"),
            np.array([r["d"] for r in rows]))
P1,N1,C1,D1,Y1=blk(PEN1); P2,N2,C2_,D2,Y2_=blk(PEN2)
Zo,To,No,Co=A(OUTa,"Z"),A(OUTa,"T"),A(OUTa,"ne"),A(OUTa,"c")
Yo=np.array([r["d"] for r in OUTa]); Do=Zo-To
t1=np.log(C1+1)/C1; t2=np.log(C2_+1)/C2_; to=np.log(Co+1)/Co
YA=np.concatenate([Y1,Y2_,Yo])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def rep(name,f,p0s,npar):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
            rr=YA-f(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {name:<40}{npar:>4}   failed"); return None
    pr,s=best; rr=YA-f(None,*pr)
    print(f"      {name:<40}{npar:>4}{s:>10.4f}{1-np.var(rr)/np.var(YA):>9.4f}")
    return pr
print(f"      {'model':<40}{'par':>4}{'rms':>10}{'R²':>9}")
rep("one penetrating amplitude (current)",
    lambda _,a,q,k: np.concatenate([
      (a+q*D1)*np.sqrt(np.maximum(P1,1e-9))*N1**k*t1,
      (a+q*D2)*np.sqrt(np.maximum(P2,1e-9))*N2**k*t2,
      0.37*sig((Do+1.5)/0.40)*((No-1)/No)*No**k*to]),
    [[0.475,-0.040,0.467]],3)
pr=rep("SEPARATE amplitude for the inside regime",
    lambda _,a,q,a2,k: np.concatenate([
      (a+q*D1)*np.sqrt(np.maximum(P1,1e-9))*N1**k*t1,
      a2*np.sqrt(np.maximum(P2,1e-9))*N2**k*t2,
      0.37*sig((Do+1.5)/0.40)*((No-1)/No)*No**k*to]),
    [[0.475,-0.040,0.55,0.467],[0.5,-0.03,0.7,0.5]],4)
if pr is not None:
    a,q,a2,k=pr
    print(f"\n      a = {a:.4f}  q = {q:+.4f}  a₂ = {a2:.4f}  k = {k:.4f}")
    print(f"      the INSIDE regime's amplitude is {a2/a:.2f}× the outside one")
    np.save("/tmp/eqreg.npy",pr)
    def delta(Z,c,l):
        ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
        n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
        if p>=1:
            if n0>n_: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
            return a2*math.sqrt(p)*ne**k*t
        T=thr_(ne-1,l,c); x=max(-60.,min(60.,(Z-T+1.5)/0.40))
        return 0.37*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
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
    print(f"\n      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
    if BAD: print("      failures: " + "  ".join(
        f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z,gt,pk in BAD))