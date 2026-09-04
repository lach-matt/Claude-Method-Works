import math, statistics as st
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/sw2.py",encoding="utf-8").read()
src=src[:src.index('print("  THE SWITCH, CHARGE-NORMALISED')]
g={}; exec(src,g)
rows=g["rows"]; L="spdfgh"
for r in rows:
    ne=r["ne"]; t=math.log(r["c"]+1)/r["c"]
    den=((ne-1)/ne)*math.sqrt(ne)*t
    r["y"]=r["d"]/den if den>1e-9 else float("nan")
print("  THE SWITCH, FITTED PER ℓ ON THE CHARGE-NORMALISED DEFECTS\n")
P={}
for l in (2,3):
    v=[x for x in rows if x["l"]==l and x["y"]==x["y"]]
    if len(v)<8: continue
    D=np.array([x["D"] for x in v],float); Yv=np.array([x["y"] for x in v])
    def M(_,h,w,m): return h*0.5*(1+np.tanh(0.5*np.clip((D-m)/max(abs(w),1e-9),-60,60)))
    best=None
    for p0 in ([0.38,0.5,-1.5],[0.4,1.0,-2.0],[0.35,0.3,-1.0],[0.5,2.0,-4.0],
               [0.2,3.0,-6.0]):
        try:
            pr,_=curve_fit(M,np.arange(len(Yv)),Yv,p0=p0,maxfev=900000)
            rr=Yv-M(None,*pr); s=float(np.sqrt(np.mean(rr**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: continue
    pr,s=best; rr=Yv-M(None,*pr); h,w,m=pr
    print(f"      ℓ = {L[l]}   h = {h:.4f}   w = {abs(w):.3f}   centre D = {m:+.3f}")
    print(f"              rms {s:.4f} · R² {1-np.var(rr)/np.var(Yv):.4f} · {len(v)} channels")
    P[l]=(h,abs(w),m)
print()
print("  WHAT THE TWO CENTRES AND WIDTHS SAY\n")
for l in sorted(P):
    h,w,m=P[l]
    print(f"      ℓ = {L[l]}:  saturates at y = {h:.3f}, centred {m:+.2f} from the")
    print(f"               threshold, e-folding over {w:.2f} protons")
print()
if 2 in P and 3 in P:
    print(f"      centre:  d {P[2][2]:+.2f}   f {P[3][2]:+.2f}")
    print(f"      width :  d {P[2][1]:.2f}    f {P[3][1]:.2f}")
    print(f"      height:  d {P[2][0]:.3f}   f {P[3][0]:.3f}")
np.save("/tmp/swP.npy",np.array([[l,*P[l]] for l in sorted(P)]))
print()
print("  PREDICTED AGAINST MEASURED, NEAR EACH THRESHOLD\n")
print(f"      {'ℓ':>3}{'D':>5}{'species':>11}{'measured':>11}{'predicted':>11}")
for l in sorted(P):
    h,w,m=P[l]
    for x in sorted([z for z in rows if z["l"]==l and -4<=z["D"]<=2],
                    key=lambda z:z["D"]):
        ne=x["ne"]; t=math.log(x["c"]+1)/x["c"]
        pred=h*0.5*(1+math.tanh(0.5*(x["D"]-m)/w))*((ne-1)/ne)*math.sqrt(ne)*t
        sp=f"{g['EL'].get(x['Z'],x['Z'])} {g['RO'].get(x['c'],x['c'])}"
        print(f"      {L[l]:>3}{x['D']:>5}{sp:>11}{x['d']:>11.4f}{pred:>11.4f}")
