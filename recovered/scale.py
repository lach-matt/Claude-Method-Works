import numpy as np, random
from itertools import product
random.seed(41)
CONS=[("l<=n-1",  lambda x:x[1]<=x[0]-1),
      ("k<=4l+2", lambda x:x[2]<=4*x[1]+2),
      ("q<=k",    lambda x:x[3]<=x[2]),
      ("2S<=k",   lambda x:x[7]<=x[2]),
      ("f<=e-1",  lambda x:x[5]<=x[4]-1),
      ("g<=4f+2", lambda x:x[6]<=4*x[5]+2),
      ("g<=q",    lambda x:x[6]<=x[3])]
EXC=[lambda y:y[1]-(y[0]-1), lambda y:y[2]-(4*y[1]+2), lambda y:y[3]-y[2],
     lambda y:y[7]-y[2], lambda y:y[5]-(y[4]-1), lambda y:y[6]-(4*y[5]+2), lambda y:y[6]-y[3]]
def build(NC,LC,KC,EC_,FC,QC,GC,SC):
    AX=[range(1,NC+1),range(0,LC),range(1,KC+1),range(0,QC+1),
        range(1,EC_+1),range(0,FC),range(0,GC+1),range(0,SC+1)]
    BOX=[z for z in product(*AX)]
    sat=lambda x,skip=None: all(fn(x) for i,(nm,fn) in enumerate(CONS) if i!=skip)
    LAM={z for z in BOX if sat(z)}
    return BOX,LAM,sat
def run(cfg,nsamp=10):
    BOX,LAM,sat=build(*cfg)
    if not LAM or len(BOX)>260000: return None
    LL=sorted(LAM); grid=np.array(BOX,dtype=np.int32); d=8
    def csz(A):
        m=np.ones(len(grid),dtype=bool)
        for i in range(d):
            for j in range(d):
                if i==j: continue
                for a in range(7):
                    m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
        return int(m.sum())
    if csz(np.array(LL,dtype=np.int32))!=len(LAM): return None
    outside=[z for z in BOX if z not in LAM]
    res=[]
    for i,(nm,fn) in enumerate(CONS):
        marg=len({z for z in BOX if sat(z,skip=i)})-len(LAM)
        if marg==0: continue
        front=[y for y in outside if [k for k,(n2,f2) in enumerate(CONS) if not f2(y)]==[i] and EXC[i](y)==1]
        if not front: continue
        A=[csz(np.array(LL+[y],dtype=np.int32))-len(LAM)-1
           for y in random.sample(front,min(nsamp,len(front)))]
        res.append((nm,len(LAM),len(BOX),marg,len(front),float(np.median(A))))
    return res
CFG=[(3,2,3,3,2,3,3,3),(4,2,3,3,2,3,3,3),(3,2,4,3,2,4,3,4),
     (3,3,3,3,2,3,3,3),(4,2,4,3,2,4,4,4),(3,2,3,4,2,3,3,3),
     (5,2,3,3,2,3,3,3),(3,2,3,3,3,3,6,3)]
print("="*88)
print("  SCALING THE LATTICE — many (MARGINAL, A) pairs from seven constraints")
print("="*88)
print("\n  %-30s%9s%9s%8s"%("configuration","|Lambda|","|box|","points"))
ALL=[]
for cfg in CFG:
    r=run(cfg)
    if r is None:
        print("  %-30s%9s"%(str(cfg),"skipped")); continue
    print("  %-30s%9d%9d%8d"%(str(cfg),r[0][1],r[0][2],len(r)))
    for row in r: ALL.append((cfg,)+row)
print("\n  total data points: %d  (was 7)"%len(ALL))
if len(ALL)>=14:
    M=np.array([a[4] for a in ALL],dtype=float)
    Fr=np.array([a[5] for a in ALL],dtype=float)
    N=np.array([a[2] for a in ALL],dtype=float)
    A=np.array([a[6] for a in ALL],dtype=float)
    print("\n  %-28s%12s%12s"%("predictor","Pearson","Spearman"))
    print("  "+"-"*52)
    for lab,v in [("MARGINAL",M),("frontier",Fr),("|Lambda|",N),
                  ("MARGINAL/|Lambda|",M/N),("frontier/|Lambda|",Fr/N)]:
        print("  %-28s%12.3f%12.3f"%(lab,np.corrcoef(v,A)[0,1],
              np.corrcoef(np.argsort(np.argsort(v)),np.argsort(np.argsort(A)))[0,1]))
    print("\n  NORMALISED: A/|Lambda| against MARGINAL/|Lambda|\n")
    y=A/N; x=M/N
    print("  %-28s%12.3f%12.3f"%("A/|L| vs MARGINAL/|L|",np.corrcoef(x,y)[0,1],
          np.corrcoef(np.argsort(np.argsort(x)),np.argsort(np.argsort(y)))[0,1]))
    sl,ic=np.polyfit(x,y,1)
    pred=sl*x+ic
    err=100*np.abs(pred-y)/np.maximum(y,1e-9)
    print("\n     fit  A/|L| = %.3f * (MARGINAL/|L|) + %.3f"%(sl,ic))
    print("     median absolute error : %.1f%%"%np.median(err))
    print("     90th percentile error : %.1f%%"%np.percentile(err,90))
    print("     worst error           : %.1f%%"%err.max())
    k=int(np.argmax(err))
    print("     worst point           : %s  in %s"%(ALL[k][1],str(ALL[k][0])))
    print("\n  BY CONSTRAINT — is g<=4f+2 still the outlier?\n")
    print("  %-12s%8s%16s%16s"%("constraint","n","median A/|L|","median M/|L|"))
    for nm,_ in CONS:
        idx=[i for i,a in enumerate(ALL) if a[1]==nm]
        if idx: print("  %-12s%8d%16.4f%16.4f"%(nm,len(idx),np.median(y[idx]),np.median(x[idx])))