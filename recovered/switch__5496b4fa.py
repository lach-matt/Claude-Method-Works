import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit
src=open("shellsum.py",encoding="utf-8").read()
src=src[:src.index("# every shell the sum runs over")]
g={}; exec(src,g)
H=g["H"]; cfg_c=g["cfg_c"]; OPEN=g["OPEN"]; parents=g["parents"]
L="spdfgh"
EL={19:"K",20:"Ca",21:"Sc",22:"Ti",26:"Fe",30:"Zn",37:"Rb",38:"Sr",39:"Y",
    48:"Cd",55:"Cs",56:"Ba",57:"La",80:"Hg",83:"Bi",12:"Mg",13:"Al",14:"Si",
    11:"Na",18:"Ar",31:"Ga",32:"Ge",5:"B",6:"C",4:"Be",3:"Li",2:"He",1:"H",
    15:"P",16:"S",17:"Cl",7:"N",8:"O",9:"F",10:"Ne"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
rows=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l<2 or l>3: continue
    cfg=cfg_c(ne-1,c)
    if parents(cfg)>1: continue
    p=sum(1 for n,ll,o in cfg if ll==l and o>0)
    if p>0: continue                       # outer-well only
    v=[n for n,ll,o in cfg if ll==l and o>0]
    n0=(max(v)+1) if v else l+1
    T=OPEN.get((n0,l),9999)
    if T>9000: continue
    rows.append(dict(Z=Z,c=c,l=l,d=d,ne=ne,T=T,D=Z-T))
print("  THE SWITCH, MEASURED — every outer-well d and f channel\n")
for l in (2,3):
    v=sorted([r for r in rows if r["l"]==l],key=lambda r:r["D"])
    if not v: continue
    print(f"  ℓ = {L[l]}   threshold T = {v[0]['T']}   {len(v)} channels\n")
    print(f"      {'D = Z−T':>9}{'species':>11}{'charge':>8}{'δ':>10}")
    for r in v:
        if r["D"]<-30: continue
        print(f"      {r['D']:>9}{EL.get(r['Z'],'Z'+str(r['Z'])):>11}"
              f"{RO.get(r['c'],r['c']):>8}{r['d']:>10.4f}")
    print()
print("  THE SWITCH FITTED, ON THESE CHANNELS ALONE\n")
for l in (2,3):
    v=[r for r in rows if r["l"]==l]
    if len(v)<8: continue
    D=np.array([r["D"] for r in v],float)
    NE=np.array([r["ne"] for r in v],float)
    C=np.array([r["c"] for r in v],float)
    Y=np.array([r["d"] for r in v])
    T_=np.log(C+1)/C
    def M(_,h,w,m,k):
        x=np.clip((D+m)/max(abs(w),1e-6),-60,60)
        return h*0.5*(1+np.tanh(0.5*x))*((NE-1)/NE)*NE**k*T_
    best=None
    for p0 in ([0.6,4,0,0.47],[1.0,2,5,0.5],[0.5,8,-5,0.45],[2.0,1,10,0.4]):
        try:
            pr,_=curve_fit(M,np.arange(len(Y)),Y,p0=p0,maxfev=900000)
            r=Y-M(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: continue
    pr,s=best; r=Y-M(None,*pr)
    h,w,m,k=pr
    print(f"      ℓ = {L[l]}:  h={h:.4f}  w={abs(w):.3f}  centre at D = {-m:+.2f}  k={k:.3f}")
    print(f"                rms {s:.4f}  ·  R² {1-np.var(r)/np.var(Y):.4f}  ·  {len(v)} channels")
    print(f"                at D = 0 the switch reads "
          f"{0.5*(1+math.tanh(0.5*(0+m)/abs(w))):.3f}")
    print()