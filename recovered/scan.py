import math
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/hfix.py",encoding="utf-8").read()
src=src[:src.index("H0=0.37/math.sqrt(6)")]
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
YA=np.concatenate([Y,Y2]); BAR=np.sqrt(np.maximum(L2*(L2+1),1e-9))
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for X,Yl,O in cfg:
        if X==n and Yl==l: return O
    return 0
print("  SCANNING h(d) OVER ITS MEASUREMENT RANGE\n")
print("      the charge-normalised table gave y = 0.291, 0.342, 0.373 at D = −1, 0, +1")
print("      and was STILL RISING, so h(d) is at least 0.373 and plausibly 0.37–0.45\n")
print(f"      {'h(d)':>7}{'h(f)':>8}{'rms':>9}{'filling':>10}   failures")
BESTREC=None
for hd in (0.37,0.38,0.39,0.40,0.41,0.42,0.44,0.46):
    H0=hd/math.sqrt(6)
    def M(_,a,q,k):
        return np.concatenate([
          (a+q*DN)*np.sqrt(np.maximum(P,1e-9))*NE**k*T1,
          H0*BAR*sig((D+1.5)/0.40)*((NE2-1)/NE2)*NE2**k*CH2])
    best=None
    for p0 in ([0.49,-0.040,0.45],[0.5,-0.03,0.5]):
        try:
            pr,_=curve_fit(M,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
            rr=YA-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: continue
    pr,s=best; a,q,k=pr
    def delta(Z,c,l):
        ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
        n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
        if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
        T=thr_(ne-1,l,c); x=max(-60.,min(60.,(Z-T+1.5)/0.40))
        return H0*math.sqrt(l*(l+1))*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
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
    f=" ".join(f"Z{Z}" for Z,_,_ in BAD)
    print(f"      {hd:>7.2f}{H0*math.sqrt(12):>8.3f}{s:>9.4f}"
          f"{f'{ok}/{ok+bad}':>10}   {f}")
    if BESTREC is None or ok>BESTREC[0]: BESTREC=(ok,hd,a,q,k,s)
print()
if BESTREC:
    ok,hd,a,q,k,s=BESTREC
    print(f"      best: h(d) = {hd}, filling {ok}/101, rms {s:.4f}")
    print(f"            a = {a:.4f}  q = {q:+.4f}  k = {k:.4f}")
    np.save("/tmp/eqwin.npy",np.array([a,q,k,hd/math.sqrt(6)]))