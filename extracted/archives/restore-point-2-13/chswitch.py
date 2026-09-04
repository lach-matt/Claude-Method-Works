import math
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
R=g["R"]; cfg_c,cp,out_,n0_,thr_,ORDER=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"],g["ORDER"]
OPEN=g["OPEN"]; L="spdfg"
# THE SWITCH ON CHARGE, not on Z.  A collapsing orbital is one with p = 0 whose
# shell has begun to open in the isoelectronic sequence.  The captures say that
# happens at charge 3 for every electron count tested.
def collapsed(ne,l,c,Z):
    """has the outer-well orbital dropped into the inner well?"""
    T=thr_(ne-1,l,c)
    return 1.0 if (c>=3 and ne>=T-2) or (Z>=T) else 0.0
for r in R:
    r["col"]=collapsed(r["ne"],r["l"],r["c"],r["Z"])
PEN=[r for r in R if r["p"]>=1]; OUT=[r for r in R if r["p"]==0]
def A(rows,k_): return np.array([r[k_] for r in rows],float)
P,NE,C=A(PEN,"p"),A(PEN,"ne"),A(PEN,"c"); DN=A(PEN,"n0")-A(PEN,"on")
Y=np.array([r["d"] for r in PEN]); T1=np.log(C+1)/C
NE2,C2=A(OUT,"ne"),A(OUT,"c"); COL=A(OUT,"col")
Z2,T2=A(OUT,"Z"),A(OUT,"T"); D=Z2-T2
Y2=np.array([r["d"] for r in OUT]); CH2=np.log(C2+1)/C2
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
    if best is None: print(f"      {name:<42}{npar:>3}   failed"); return None
    pr,s=best; rr=YA-f(None,*pr)
    print(f"      {name:<42}{npar:>3}{s:>10.4f}{1-np.var(rr)/np.var(YA):>9.4f}")
    return pr
print("  THE SWITCH KEYED ON CHARGE\n")
print(f"      {'model':<42}{'par':>3}{'rms':>10}{'R²':>9}")
rep("sigmoid in Z − T  (h, m, w measured)",
    lambda _,a,q,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      0.37*sig((D+1.5)/0.40)*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.475,-0.040,0.467]],3)
pr=rep("BINARY on collapse, keyed by charge",
    lambda _,a,q,h,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      h*COL*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.475,-0.040,0.37,0.467],[0.5,-0.03,0.5,0.5]],4)
pr2=rep("binary + a floor for the uncollapsed",
    lambda _,a,q,h,f0,k: np.concatenate([
      (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
      (h*COL+f0*(1-COL))*((NE2-1)/NE2)*NE2**k*CH2]),
    [[0.475,-0.040,0.37,0.03,0.467]],5)
best=pr2 if pr2 is not None else pr
if best is not None:
    if len(best)==5: a,q,h,f0,k=best
    else: a,q,h,k=best; f0=0.0
    print(f"\n      a={a:.4f}  q={q:+.4f}  h={h:.4f}  floor={f0:.4f}  k={k:.4f}")
    def delta(Z,c,l):
        ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
        n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
        if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
        col=collapsed(ne,l,c,Z)
        return (h*col+f0*(1-col))*((ne-1)/ne)*ne**k*t
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
