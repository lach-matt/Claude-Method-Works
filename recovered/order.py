import math, statistics as st
import numpy as np
from itertools import product
from scipy.optimize import curve_fit
src=open("/tmp/cross.py",encoding="utf-8").read()
src=src[:src.index('print("  PLUGGING δ INTO')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; op_R=g["op_R"]
rows=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5 or d<=0.02: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    rows.append((Z,c,l,S,ne,p,d,p+l+1))
Z=np.array([r[0] for r in rows],float); C=np.array([r[1] for r in rows],float)
LL=np.array([r[2] for r in rows],float); SS_=np.array([r[3] for r in rows],float)
NE=np.array([r[4] for r in rows],float); P=np.array([r[5] for r in rows],float)
D=np.array([r[6] for r in rows]); N0=np.array([r[7] for r in rows],float)
NS=N0-D
base={(int(a),int(b),int(c_),int(d_)) for a,b,c_,d_ in zip(Z,C,LL,SS_)}
E4=len(op_R(base,4))-len(base)
rng=np.random.default_rng(7)
def cost(vals,nb=8):
    qs=np.quantile(vals,np.linspace(0,1,nb+1)[1:-1])
    X={(int(a),int(b),int(c_),int(d_),int(np.searchsorted(qs,v)))
       for a,b,c_,d_,v in zip(Z,C,LL,SS_,vals)}
    E=len(op_R(X,5))-len(X)
    Xr={(int(a),int(b),int(c_),int(d_),int(rng.integers(0,nb)))
        for a,b,c_,d_ in zip(Z,C,LL,SS_)}
    Er=len(op_R(Xr,5))-len(Xr)
    return (E-E4)/max(Er-E4,1)
print(f"  {len(rows)} channels · E of the 4 base coordinates = {E4}\n")
print("  FORMS TESTED ON BOTH AXES: fit quality AND closure cost\n")
print(f"      {'form':<30}{'rms':>9}{'R²':>8}{'cost/noise':>12}")
def run(nm,f,p0,tgt):
    best=None
    for q in p0:
        try:
            pr,_=curve_fit(f,np.arange(len(tgt)),tgt,p0=q,maxfev=800000)
            r=tgt-f(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {nm:<30}  failed"); return
    pr,s=best; pred=f(None,*pr); r=tgt-pred
    # closure cost of the PREDICTION as a coordinate
    print(f"      {nm:<30}{s:>9.4f}{1-np.var(r)/np.var(tgt):>8.4f}{cost(pred):>12.3f}")
    return pr
print("      — fitting δ —")
run("δ = A√p·Nₑ^k·c^(−C/√Nₑ)",
    lambda _,A,k: A*np.sqrt(P)*NE**k*C**(-1.362/np.sqrt(NE)), [[0.38,0.39]], D)
print("      — fitting n* directly —")
run("n* = n₀ − A√p·Nₑ^k·c^(−C/√Nₑ)",
    lambda _,A,k: N0-A*np.sqrt(P)*NE**k*C**(-1.362/np.sqrt(NE)), [[0.38,0.39]], NS)
run("n* = a + b·(n₀+ℓ)",
    lambda _,a,b: a+b*(N0+LL), [[0.5,0.5]], NS)
run("n* = a·(n₀+ℓ)^m",
    lambda _,a,m: a*(N0+LL)**m, [[0.6,0.9]], NS)
run("n* = a·n₀^m·c^t",
    lambda _,a,m,t: a*N0**m*C**t, [[0.8,0.9,0.1]], NS)
run("n* = a·n₀^m·(c/Nₑ)^t",
    lambda _,a,m,t: a*N0**m*(C/NE)**t, [[0.8,0.9,0.1]], NS)
print()
print("      — the raw coordinates, for scale —")
for nm,v in (("n₀",N0),("n₀+ℓ",N0+LL),("δ measured",D),("n* measured",NS)):
    print(f"      {nm:<30}{'':>17}{cost(v):>12.3f}")