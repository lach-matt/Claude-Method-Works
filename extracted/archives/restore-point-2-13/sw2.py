import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit
src=open("/tmp/switch.py",encoding="utf-8").read()
src=src[:src.index('print("  THE SWITCH, MEASURED')]
g={}; exec(src,g)
rows=[x for x in g["rows"] if x["ne"]>1]; L="spdfgh"; EL=g["EL"]; RO=g["RO"]
print("  THE SWITCH, CHARGE-NORMALISED   y = δ / [ (Nₑ−1)/Nₑ · √Nₑ · ln(c+1)/c ]\n")
for r in rows:
    ne=r["ne"]; t=math.log(r["c"]+1)/r["c"]
    den=((ne-1)/ne)*math.sqrt(ne)*t
    r["y"]=r["d"]/den if den>1e-9 else float("nan")
for l in (2,3):
    v=sorted([x for x in rows if x["l"]==l],key=lambda x:x["D"])
    if not v: continue
    print(f"  ℓ = {L[l]}   T = {v[0]['T']}\n")
    by=defaultdict(list)
    for x in v: by[x["D"]].append(x["y"])
    print(f"      {'D':>5}{'n':>4}{'median y':>11}{'  species'}")
    for D in sorted(by):
        if D<-12: continue
        sp=" ".join(sorted({EL.get(x['Z'],str(x['Z']))+RO.get(x['c'],str(x['c']))
                            for x in v if x['D']==D}))[:44]
        print(f"      {D:>5}{len(by[D]):>4}{st.median(by[D]):>11.4f}   {sp}")
    print()
print("  FITTING THE SWITCH ON y — the charge and Nₑ factors already removed\n")
for l in (2,3):
    v=[x for x in rows if x["l"]==l]
    if len(v)<8: continue
    D=np.array([x["D"] for x in v],float); Yv=np.array([x["y"] for x in v])
    def M(_,h,w,m):
        return h*0.5*(1+np.tanh(0.5*np.clip((D+m)/max(abs(w),1e-6),-60,60)))
    best=None
    for p0 in ([0.3,1.0,2.0],[0.4,0.5,1.5],[0.25,2.0,3.0],[0.35,0.3,1.0]):
        try:
            pr,_=curve_fit(M,np.arange(len(Yv)),Yv,p0=p0,maxfev=900000)
            rr=Yv-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: continue
    pr,s=best; rr=Yv-M(None,*pr); h,w,m=pr
    print(f"      ℓ = {L[l]}:  h = {h:.4f}   w = {abs(w):.3f}   centre at D = {-m:+.3f}")
    print(f"               rms {s:.4f} · R² {1-np.var(rr)/np.var(Yv):.4f} · {len(v)} channels")
    print(f"               σ at D = 0: {0.5*(1+math.tanh(0.5*m/abs(w))):.3f}")
    np.save(f"/tmp/sw_{l}.npy",pr)
    print()
