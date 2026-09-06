import json, math, statistics as st
import numpy as np
from scipy.optimize import curve_fit
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,region=g["load"],g["region"]
config,mults,H=load()
AL={}
for kk,v in json.load(open("/tmp/alpha_full.json")).items():
    z,c=kk.split(","); AL[(int(z),int(c))]=v
def corb(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
def n0f(ne,l):
    v=[n for n,ll,o in config(ne) if ll==l and o>0]
    return (max(v)+1) if v else l+1
def Kf(l): return l*(l+1)*(2*l-1)*(2*l+1)*(2*l+3) if l>=1 else 1e9
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN={}; z=0
for n,l in ORDER: OPEN[(n,l)]=z+1; z+=2*(2*l+1)
Hin={kk:v for kk,v in H.items() if region(kk[0],kk[1],kk[2],config)}
FAR=[(55,1,1,2,3.5667),(90,1,0,3,5.20),(90,1,1,3,4.75),(90,1,2,3,3.80),
     (90,1,3,3,2.00),(89,1,0,2,5.20),(89,1,2,2,3.80)]
rows=[(kk[0],kk[1],kk[2],kk[3],v) for kk,v in Hin.items()]+list(FAR)
P=np.array([corb(x[0]-x[1],x[2]) for x in rows],float)
NE=np.array([x[0]-x[1]+1 for x in rows],float)
CH=np.array([x[1] for x in rows],float); L=np.array([x[2] for x in rows],float)
ZZ=np.array([x[0] for x in rows],float)
T=np.array([OPEN.get((n0f(x[0]-x[1],x[2]),x[2]),999) for x in rows],float)
AA=np.array([AL.get((x[0],x[1]),np.nan) for x in rows])
y=np.array([x[4] for x in rows]); KF=np.array([Kf(int(l)) for l in L])
have=~np.isnan(AA); Af=np.nan_to_num(AA)
COL=np.clip((ZZ-T+4.0)/8.0,0.0,1.0)
GATE=(NE-1)/NE                     # the hydrogenic boundary, register 1182
print("  TWO REPAIRS AT ONCE\n")
print("      1. the collapse term gated by (Nₑ−1)/Nₑ — zeroes at Nₑ = 1 and nowhere else")
print("      2. the α term restored alongside it — does Λ_α still earn its place?\n")
def fit(name,f,p0s):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(y)),y,p0=p0,maxfev=900000)
            r=y-f(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"  {name:<38}  fit failed"); return None
    pr,rms=best; r=y-f(None,*pr)
    hi=L>=4
    hyd=[]
    a=pr[0];e0=pr[1];e1=pr[2];k=pr[3];h=pr[4]
    for Z in (1,2,8,26,56,90):
        for l in range(4):
            ne=1; p=corb(0,l); thr=OPEN.get((n0f(0,l),l),999)
            C=min(max((Z-thr+4.0)/8.0,0.0),1.0)
            hyd.append(abs(h*C*((ne-1)/ne if "gated" in name else 1.0)*ne**k*math.log(Z+1)/Z))
    print(f"  {name:<38}{rms:>8.4f}{1-np.var(r)/np.var(y):>8.4f}"
          f"{np.sqrt(np.mean(r[hi]**2)):>10.5f}{max(hyd):>10.4f}")
    return pr,rms
print(f"  {'model':<38}{'rms':>8}{'R²':>8}{'ℓ≥4 rms':>10}{'hydro':>10}")
def M0(_,a,e0,e1,k,h):
    e=np.maximum(e0+e1*np.log(np.maximum(NE,2)),0.05)
    return (a*np.where(P>0,np.power(np.maximum(P,1e-9),e),0.0)*NE**k*np.log(CH+1)/CH
            + np.where(P<=0,h*COL*NE**k*np.log(CH+1)/CH,0.0))
def M1(_,a,e0,e1,k,h):
    e=np.maximum(e0+e1*np.log(np.maximum(NE,2)),0.05)
    return (a*np.where(P>0,np.power(np.maximum(P,1e-9),e),0.0)*NE**k*np.log(CH+1)/CH
            + np.where(P<=0,h*COL*GATE*NE**k*np.log(CH+1)/CH,0.0))
def M2(_,a,e0,e1,k,h,q):
    e=np.maximum(e0+e1*np.log(np.maximum(NE,2)),0.05)
    pol=np.where((P<=0)&have,q*3.0*Af*CH**2/KF,0.0)
    return (a*np.where(P>0,np.power(np.maximum(P,1e-9),e),0.0)*NE**k*np.log(CH+1)/CH
            + np.where(P<=0,h*COL*GATE*NE**k*np.log(CH+1)/CH,0.0) + pol)
r0=fit("as anchored",M0,[[0.377,0.830,-0.090,0.494,0.542]])
r1=fit("+ gated by (Nₑ−1)/Nₑ",M1,[[0.377,0.830,-0.090,0.494,0.542]])
r2=fit("+ gated + α restored",M2,[[0.377,0.830,-0.090,0.494,0.542,1.0],
                                  [0.377,0.830,-0.090,0.494,0.542,0.2]])
if r2: print(f"\n      the α coefficient q = {r2[0][5]:.4f}   "
             f"{'α still earns its place' if abs(r2[0][5])>0.3 else 'α is SUBSUMED by the Janet term'}")
if r1: np.save("/tmp/final6.npy",r1[0])