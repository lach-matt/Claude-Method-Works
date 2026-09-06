import math
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
R=g["R"]; cfg_c,cp,out_,n0_,thr_,ORDER=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"],g["ORDER"]
L="spdfg"
PEN=[r for r in R if r["p"]>=1]; OUT=[r for r in R if r["p"]==0]
def A(rows,k_): return np.array([r[k_] for r in rows],float)
P,NE,C=A(PEN,"p"),A(PEN,"ne"),A(PEN,"c"); DN=A(PEN,"n0")-A(PEN,"on")
Y=np.array([r["d"] for r in PEN]); T1=np.log(C+1)/C
NE2,C2,L2=A(OUT,"ne"),A(OUT,"c"),A(OUT,"l")
Z2,T2=A(OUT,"Z"),A(OUT,"T"); D=Z2-T2
Y2=np.array([r["d"] for r in OUT]); CH2=np.log(C2+1)/C2
YA=np.concatenate([Y,Y2])
BAR=np.sqrt(np.maximum(L2*(L2+1),1e-9))          # the centrifugal barrier scale
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def rep(name,f,p0s,npar):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
            rr=YA-f(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {name:<44}{npar:>3}   failed"); return None
    pr,s=best; rr=YA-f(None,*pr)
    print(f"      {name:<44}{npar:>3}{s:>10.4f}{1-np.var(rr)/np.var(YA):>9.4f}")
    return pr
print("  THE SWITCH HEIGHT SCALED BY THE BARRIER\n")
print("      h(ℓ) = h₀·√(ℓ(ℓ+1))    →  h(d)/h(f) = √(6/12) = 0.707")
print("      measured: h(d) = 0.37 from K→Ca, h(f) ≈ 0.52 from La\n")
print(f"      {'model':<44}{'par':>3}{'rms':>10}{'R²':>9}")
rep("h constant  (current)",
    lambda _,a,q,h,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*sig((D+1.5)/0.40)*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.475,-0.040,0.37,0.467]],4)
pr=rep("h = h₀·√(ℓ(ℓ+1))",
    lambda _,a,q,h0,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h0*BAR*sig((D+1.5)/0.40)*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.475,-0.040,0.151,0.467],[0.5,-0.03,0.2,0.5]],4)
rep("h = h₀·ℓ(ℓ+1)",
    lambda _,a,q,h0,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h0*L2*(L2+1)*sig((D+1.5)/0.40)*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.475,-0.040,0.06,0.467]],4)
if pr is not None:
    a,q,h0,k=pr
    print(f"\n      a={a:.4f}  q={q:+.4f}  h₀={h0:.4f}  k={k:.4f}")
    print(f"      h(d)={h0*math.sqrt(6):.3f}   h(f)={h0*math.sqrt(12):.3f}   "
          f"h(g)={h0*math.sqrt(20):.3f}")
    def delta(Z,c,l):
        ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
        n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
        if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
        T=thr_(ne-1,l,c); x=max(-60.,min(60.,(Z-T+1.5)/0.40))
        return h0*math.sqrt(l*(l+1))*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
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
    np.save("/tmp/eqbar.npy",pr)