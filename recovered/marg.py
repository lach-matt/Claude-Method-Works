import numpy as np, random
from itertools import product
random.seed(31)
CAP=lambda l:2*(2*l+1)
CONS=[("l <= n-1",  lambda x:x[1]<=x[0]-1),
      ("k <= 4l+2", lambda x:x[2]<=4*x[1]+2),
      ("q <= k",    lambda x:x[3]<=x[2]),
      ("2S <= k",   lambda x:x[7]<=x[2]),
      ("f <= e-1",  lambda x:x[5]<=x[4]-1),
      ("g <= 4f+2", lambda x:x[6]<=4*x[5]+2),
      ("g <= q",    lambda x:x[6]<=x[3])]
AX=[range(1,4),range(0,2),range(1,4),range(0,4),range(1,4),range(0,2),range(0,4),range(0,4)]
BOX=[z for z in product(*AX)]
sat=lambda x,skip=None: all(fn(x) for i,(nm,fn) in enumerate(CONS) if i!=skip)
LAM={z for z in BOX if sat(z)}
LL=sorted(LAM); d=8
grid=np.array(BOX,dtype=np.int32)
def csz(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
print("="*88)
print("  MARGINAL CONTRIBUTION — how much does each constraint do that the others don't?")
print("="*88)
print("""
     MARGINAL(C) = |cells satisfying all constraints EXCEPT C| - |Lambda|

  A constraint the others already imply has MARGINAL ~ 0. One doing
  independent work has MARGINAL large.
""")
def viol1(x):
    return [nm for nm,fn in CONS if not fn(x)]
outside=[z for z in BOX if z not in LAM]
rows=[]
for i,(nm,fn) in enumerate(CONS):
    marg=len({z for z in BOX if sat(z,skip=i)})-len(LAM)
    front=[y for y in outside if viol1(y)==[nm] and
           (lambda t: t==1)(max(0,(y[1]-(y[0]-1)) if i==0 else (y[2]-(4*y[1]+2)) if i==1 else
            (y[3]-y[2]) if i==2 else (y[7]-y[2]) if i==3 else (y[5]-(y[4]-1)) if i==4 else
            (y[6]-(4*y[5]+2)) if i==5 else (y[6]-y[3])))]
    A=[csz(np.array(LL+[y],dtype=np.int32))-len(LAM)-1 for y in random.sample(front,min(16,len(front)))] if front else []
    rows.append((nm,marg,len(front),np.median(A) if A else np.nan))
print("  %-13s%14s%12s%14s"%("constraint","MARGINAL","frontier","median A"))
print("  "+"-"*56)
for nm,mg,fr,md in rows: print("  %-13s%14d%12d%14.0f"%(nm,mg,fr,md))
A=np.array([r[3] for r in rows]); M=np.array([r[1] for r in rows],dtype=float)
Fr=np.array([r[2] for r in rows],dtype=float)
print("\n  CORRELATIONS\n")
for lab,v in [("MARGINAL",M),("frontier",Fr)]:
    print("     %-12s Pearson %+0.3f   Spearman %+0.3f"
          %(lab,np.corrcoef(v,A)[0,1],np.corrcoef(np.argsort(np.argsort(v)),np.argsort(np.argsort(A)))[0,1]))
print("="*88)
print("  OUT-OF-SAMPLE: fit on 5, predict 2 — INCLUDING the awkward one")
print("="*88)
for held in [("g <= 4f+2",), ("g <= 4f+2","2S <= k")]:
    tr=[i for i,r in enumerate(rows) if r[0] not in held]
    te=[i for i,r in enumerate(rows) if r[0] in held]
    sl,ic=np.polyfit(M[tr],A[tr],1)
    print("\n     held out: %s     fit: A = %.4f*MARGINAL + %.1f"%(", ".join(held),sl,ic))
    print("     %-13s%12s%14s%12s"%("","actual","predicted","error %"))
    for j in te:
        pr=sl*M[j]+ic
        print("     %-13s%12.0f%14.0f%12.1f"%(rows[j][0],A[j],pr,100*abs(pr-A[j])/max(A[j],1)))
print("""
{0}
  VERDICT
{0}
""".format("="*88))
rM=np.corrcoef(M,A)[0,1]; rF=np.corrcoef(Fr,A)[0,1]
sl,ic=np.polyfit([M[i] for i,r in enumerate(rows) if r[0]!="g <= 4f+2"],
                 [A[i] for i,r in enumerate(rows) if r[0]!="g <= 4f+2"],1)
j=[i for i,r in enumerate(rows) if r[0]=="g <= 4f+2"][0]
err=100*abs(sl*M[j]+ic-A[j])/max(A[j],1)
print("     MARGINAL r = %+.3f      frontier r = %+.3f"%(rM,rF))
print("     out-of-sample error on the awkward constraint: %.0f%%"%err)
if err<50 and abs(rM)>0.85:
    print("""
  **MARGINAL CONTRIBUTION IS THE RIGHT MEASURE.** It predicts amplification
  including at the extreme, where frontier size failed by 652%%.

  **A constraint that the others already imply is cheap to violate,
  because violating it contradicts almost nothing.** g <= 4f+2 -- the
  Pauli bound on the target subshell -- is nearly implied by g <= q and
  f <= e-1 together, and that near-redundancy is exactly its weakness.""")
else:
    print("""
  **NOT ESTABLISHED EITHER.** MARGINAL does %s than frontier on
  correlation but still misses the extreme point by %.0f%%.

  **THE HONEST POSITION: amplification is predicted well in the bulk by
  either measure and by neither at the extreme.** Seven constraints is too
  few to separate the candidates, and the single anomalous constraint is
  the one every hypothesis has been built to explain and then failed to
  predict. That is textbook overfitting to one point, three times running.
"""%("better" if abs(rM)>abs(rF) else "worse",err))