import math, statistics as st
import numpy as np
from collections import deque
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,op_S,region=g["load"],g["op_S"],g["region"]
config,mults,H=load()
Hin={k:v for k,v in H.items() if region(k[0],k[1],k[2],config)}
S=op_S(Hin,config)
def corb(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
def n0f(ne,l):
    v=[n for n,ll,o in config(ne) if ll==l and o>0]
    return (max(v)+1) if v else l+1
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN={}; z=0
for n,l in ORDER: OPEN[(n,l)]=z+1; z+=2*(2*l+1)
a,e0,e1,k,h=np.load("/tmp/region.npy")
def eq(Z,c,l):
    ne=Z-c+1; p=corb(ne-1,l); t=math.log(c+1)/c
    if p>0: return a*(p**max(e0+e1*math.log(max(ne,2)),0.05))*ne**k*t
    thr=OPEN.get((n0f(ne-1,l),l),999)
    return h*min(max((Z-thr+4.0)/8.0,0.0),1.0)*ne**k*t
def adm(Z,c,l,Sm):
    if c>Z or c<1 or l<0: return False
    ne=Z-c+1
    return ne>=1 and Sm in mults(ne) and l<n0f(ne-1,l)
def walk(tau=3.0,extend=True):
    val={kk:(v,1.0) for kk,v in Hin.items()}; q=deque(sorted(Hin))
    while q:
        kk=q.popleft(); v0,er=val[kk]
        for nm,(f,sc,n,dv) in S.items():
            for sg in (1,-1):
                t=(kk[0]+sg*dv[0],kk[1]+sg*dv[1],kk[2]+sg*dv[2],
                   kk[3]+2*sg if dv[3] else kk[3])
                if not adm(*t) or t[0]>103: continue
                e=er*sc
                if e>tau: continue
                if t not in val or e<val[t][1]:
                    val[t]=(v0*(f if sg>0 else 1/f),e); q.append(t)
    return val
W=walk(6.0)
print("  EXTERIOR VERIFICATION — the walk and the equation, outside the sample\n")
LIT=[("Cs I  np",55,1,1,2,3.5667,"arXiv:1706.06237, n = 70–100"),
     ("Th/U ns",90,1,0,3,5.2,"actinide theory, arXiv:2508.06733"),
     ("Th/U np",90,1,1,3,4.75,"same"),
     ("Th/U nd",90,1,2,3,3.8,"same"),
     ("Th/U nf",90,1,3,3,2.0,"same"),
     ("Ac ns",89,1,0,2,5.2,"same, Z = 89"),
     ("Ac nd",89,1,2,2,3.8,"same")]
print(f"  {'channel':<11}{'walk':>9}{'equation':>10}{'published':>11}"
      f"{'walk err':>10}{'eq err':>9}   source")
we=[];ee=[]
for nm,Z,c,l,Sm,lit,src2 in LIT:
    kk=(Z,c,l,Sm)
    wv=W[kk][0] if kk in W else None
    ev=eq(Z,c,l)
    ws=f"{wv:.3f}" if wv is not None else "—"
    wer=f"{wv-lit:+.3f}" if wv is not None else "—"
    if wv is not None: we.append(abs(wv-lit))
    ee.append(abs(ev-lit))
    print(f"  {nm:<11}{ws:>9}{ev:>10.3f}{lit:>11.3f}{wer:>10}{ev-lit:>+9.3f}   {src2[:26]}")
print()
if we: print(f"      walk     : median |error| {st.median(we):.3f}  ({len(we)} reached)")
print(f"      equation : median |error| {st.median(ee):.3f}  ({len(ee)} values)")