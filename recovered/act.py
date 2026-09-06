import numpy as np, random
from itertools import product
random.seed(53)
CONS=[("l<=n-1",  1,lambda x:x[0]-1),
      ("k<=4l+2", 2,lambda x:4*x[1]+2),
      ("q<=k",    3,lambda x:x[2]),
      ("2S<=k",   7,lambda x:x[2]),
      ("f<=e-1",  5,lambda x:x[4]-1),
      ("g<=4f+2", 6,lambda x:4*x[5]+2),
      ("g<=q",    6,lambda x:x[3])]
sat=lambda x,skip=None: all(x[v]<=ub(x) for i,(nm,v,ub) in enumerate(CONS) if i!=skip)
def build(NC,LC,KC,QC,EC_,FC,GC,SC):
    AX=[range(1,NC+1),range(0,LC),range(1,KC+1),range(0,QC+1),
        range(1,EC_+1),range(0,FC),range(0,GC+1),range(0,SC+1)]
    BOX=[z for z in product(*AX)]
    return BOX,{z for z in BOX if sat(z)}
print("="*90)
print("  THE ANOMALY EXPLAINED?  TWO CONSTRAINTS BOUND g, AND ONE DOMINATES")
print("="*90)
print("""
     g <= q        and      g <= 4f+2

  Both bound the SAME variable. If q is usually far smaller than 4f+2,
  then g <= 4f+2 is almost never the ACTIVE bound -- it is dominated, and
  a dominated constraint is nearly free to violate.

  DEFINE:  ACTIVITY(C) = fraction of cells of Lambda where C is the
           TIGHTEST bound on its variable (ties shared)
""")
def activity(LAM):
    byvar={}
    for i,(nm,v,ub) in enumerate(CONS): byvar.setdefault(v,[]).append(i)
    cnt={i:0.0 for i in range(len(CONS))}
    for x in LAM:
        for v,idxs in byvar.items():
            vals=[CONS[i][2](x) for i in idxs]
            m=min(vals); win=[i for i,val in zip(idxs,vals) if val==m]
            for i in win: cnt[i]+=1.0/len(win)
    return {i:cnt[i]/len(LAM) for i in cnt}
CFG=[(3,2,3,3,3,2,3,3),(4,2,3,3,3,2,3,3),(3,2,4,4,3,2,3,4),
     (3,3,3,3,3,2,3,3),(4,2,4,4,3,2,4,4),(3,2,3,3,4,2,3,3),
     (5,2,3,3,3,2,3,3),(3,2,3,3,3,3,6,3)]
ALL=[]
for cfg in CFG:
    BOX,LAM=build(*cfg)
    if len(BOX)>260000 or not LAM: continue
    LL=sorted(LAM); grid=np.array(BOX,dtype=np.int32); d=8
    def csz(A):
        m=np.ones(len(grid),dtype=bool)
        for i in range(d):
            for j in range(d):
                if i==j: continue
                for a in range(7):
                    m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
        return int(m.sum())
    if csz(np.array(LL,dtype=np.int32))!=len(LAM): continue
    act=activity(LAM)
    outside=[z for z in BOX if z not in LAM]
    for i,(nm,v,ub) in enumerate(CONS):
        marg=len({z for z in BOX if sat(z,skip=i)})-len(LAM)
        front=[y for y in outside if [k for k,(n2,v2,u2) in enumerate(CONS) if y[v2]>u2(y)]==[i]
               and y[v]-ub(y)==1]
        if not front or marg==0: continue
        A=[csz(np.array(LL+[y],dtype=np.int32))-len(LAM)-1
           for y in random.sample(front,min(10,len(front)))]
        ALL.append((nm,len(LAM),marg,len(front),act[i],float(np.median(A))))
print("  data points: %d\n"%len(ALL))
N=np.array([a[1] for a in ALL],dtype=float)
M=np.array([a[2] for a in ALL],dtype=float)
Fr=np.array([a[3] for a in ALL],dtype=float)
Ac=np.array([a[4] for a in ALL],dtype=float)
A=np.array([a[5] for a in ALL],dtype=float)
print("  %-30s%12s%12s"%("predictor of A/|Lambda|","Pearson","Spearman"))
print("  "+"-"*54)
y=A/N
for lab,v in [("ACTIVITY",Ac),("MARGINAL/|L|",M/N),("frontier/|L|",Fr/N),
              ("ACTIVITY x MARGINAL/|L|",Ac*M/N)]:
    print("  %-30s%12.3f%12.3f"%(lab,np.corrcoef(v,y)[0,1],
          np.corrcoef(np.argsort(np.argsort(v)),np.argsort(np.argsort(y)))[0,1]))
print("\n  BY CONSTRAINT\n")
print("  %-12s%8s%12s%14s%14s"%("constraint","n","ACTIVITY","median A/|L|","median M/|L|"))
for nm,_,_ in CONS:
    idx=[i for i,a in enumerate(ALL) if a[0]==nm]
    if idx: print("  %-12s%8d%12.3f%14.4f%14.4f"%(nm,len(idx),np.median(Ac[idx]),np.median(y[idx]),np.median(M[idx]/N[idx])))
print("""
{0}
  OUT-OF-SAMPLE ON THE ANOMALY
{0}
""".format("="*90))
for lab,v in [("ACTIVITY",Ac),("frontier/|L|",Fr/N),("MARGINAL/|L|",M/N)]:
    tr=[i for i,a in enumerate(ALL) if a[0]!="g<=4f+2"]
    te=[i for i,a in enumerate(ALL) if a[0]=="g<=4f+2"]
    if not te: continue
    sl,ic=np.polyfit(v[tr],y[tr],1)
    pr=sl*v[te]+ic
    err=100*np.median(np.abs(pr-y[te])/np.maximum(y[te],1e-9))
    print("     %-16s predicts g<=4f+2 with median error %7.1f%%"%(lab,err))
print("""
{0}
  VERDICT
{0}
""".format("="*90))
rA=np.corrcoef(Ac,y)[0,1]
tr=[i for i,a in enumerate(ALL) if a[0]!="g<=4f+2"]; te=[i for i,a in enumerate(ALL) if a[0]=="g<=4f+2"]
sl,ic=np.polyfit(Ac[tr],y[tr],1)
e=100*np.median(np.abs(sl*Ac[te]+ic-y[te])/np.maximum(y[te],1e-9)) if te else float('nan')
if abs(rA)>0.8 and e<60:
    print("""  **ACTIVITY IS THE MEASURE.** r = %+.3f, and it predicts the anomalous
  constraint out of sample to %.0f%%.

  **A DOMINATED CONSTRAINT IS CHEAP TO VIOLATE.** g <= 4f+2 is almost
  never the active bound on g -- g <= q binds first -- so breaking it
  contradicts almost nothing.

  **AND THE RULE IS STRUCTURAL, NOT STATISTICAL: it is about which
  constraint wins the min, cell by cell.**"""%(rA,e))
else:
    print("""  **ACTIVITY r = %+.3f, out-of-sample error %.0f%% -- %s.**
  Compare: frontier/|L| remains the best bulk predictor. The anomaly is
  still not explained by any single measure tested."""%(rA,e,"better" if abs(rA)>0.8 else "not sufficient"))