import math, statistics as st
import numpy as np
from scipy.optimize import curve_fit
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,region=g["load"],g["region"]
config,mults,H=load()
def corb(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
def n0f(ne,l):
    v=[n for n,ll,o in config(ne) if ll==l and o>0]
    return (max(v)+1) if v else l+1
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN={}; z=0
for n,l in ORDER: OPEN[(n,l)]=z+1; z+=2*(2*l+1)
# in-region measured, plus the FAR anchors the literature now supplies
Hin={k:v for k,v in H.items() if region(k[0],k[1],k[2],config)}
FAR=[(55,1,1,2,3.5667,"Cs I np, arXiv:1706.06237"),
     (90,1,0,3,5.20,"Th ns, actinide theory"),
     (90,1,1,3,4.75,"Th np"),
     (90,1,2,3,3.80,"Th nd"),
     (90,1,3,3,2.00,"Th nf"),
     (89,1,0,2,5.20,"Ac ns"),
     (89,1,2,2,3.80,"Ac nd")]
def build(rows):
    P=np.array([corb(x[0]-x[1],x[2]) for x in rows],float)
    NE=np.array([x[0]-x[1]+1 for x in rows],float)
    CH=np.array([x[1] for x in rows],float)
    L=np.array([x[2] for x in rows],float)
    ZZ=np.array([x[0] for x in rows],float)
    T=np.array([OPEN.get((n0f(x[0]-x[1],x[2]),x[2]),999) for x in rows],float)
    y=np.array([x[4] for x in rows])
    return P,NE,CH,L,ZZ,T,y
IN=[(k[0],k[1],k[2],k[3],v) for k,v in Hin.items()]
ALL=IN+[(a,b,c,d,e) for a,b,c,d,e,_ in FAR]
print("  ANCHORING THE EQUATION AT BOTH ENDS\n")
print(f"      in-region measured   {len(IN)}")
print(f"      far anchors          {len(FAR)}  (Cs I at Z=55, Th and Ac at Z=89–90)")
print(f"      the sample ran Z = 2–83; the anchors extend it to 90\n")
for lab,rows in (("in-region only",IN),("in-region + far anchors",ALL)):
    P,NE,CH,L,ZZ,T,y=build(rows)
    COL=np.clip((ZZ-T+4.0)/8.0,0.0,1.0)
    def M(_,a,e0,e1,kk,h):
        e=np.maximum(e0+e1*np.log(np.maximum(NE,2)),0.05)
        pen=a*np.where(P>0,np.power(np.maximum(P,1e-9),e),0.0)*NE**kk*np.log(CH+1)/CH
        col=np.where(P<=0,h*COL*NE**kk*np.log(CH+1)/CH,0.0)
        return pen+col
    best=None
    for p0 in ([0.3736,0.5828,-0.0266,0.5137,0.5169],[0.24,1.33,-0.28,0.66,0.58],
               [0.4,0.5,0.0,0.5,0.5]):
        try:
            pr,_=curve_fit(M,np.arange(len(y)),y,p0=p0,maxfev=900000)
            r=y-M(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    pr,rms=best; r=y-M(None,*pr)
    print(f"  {lab}")
    print(f"      a={pr[0]:.4f} e₀={pr[1]:.4f} e₁={pr[2]:.4f} k={pr[3]:.4f} h={pr[4]:.4f}")
    print(f"      rms {rms:.4f}   R² {1-np.var(r)/np.var(y):.4f}")
    a,e0,e1,kk,h=pr
    def eq(Z,c,l):
        ne=Z-c+1; p=corb(ne-1,l); t=math.log(c+1)/c
        if p>0: return a*(p**max(e0+e1*math.log(max(ne,2)),0.05))*ne**kk*t
        thr=OPEN.get((n0f(ne-1,l),l),999)
        return h*min(max((Z-thr+4.0)/8.0,0.0),1.0)*ne**kk*t
    fe=[abs(eq(Z,c,l)-lit) for Z,c,l,Sm,lit,_ in FAR]
    ie=[abs(eq(x[0],x[1],x[2])-x[4]) for x in IN]
    print(f"      on the 7 far anchors : median |err| {st.median(fe):.4f}")
    print(f"      on the 277 in-region : median |err| {st.median(ie):.4f}")
    print()
    if "far" in lab: np.save("/tmp/anchored.npy",pr)