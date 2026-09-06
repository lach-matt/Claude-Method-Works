import numpy as np, random
from itertools import product
random.seed(21)
CAP=lambda l:2*(2*l+1)
LAM=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(CAP(l),3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): LAM.add((n,l,k,q,e,f,g,S2))
d=8; LL=sorted(LAM)
AX=[sorted({x[i] for x in LL}) for i in range(d)]
grid=np.array(list(product(*AX)),dtype=np.int32)
BOX=[tuple(int(v) for v in z) for z in grid]
def csz(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
CONS=[("l <= n-1",  lambda x:x[1]-(x[0]-1)),
      ("k <= 4l+2", lambda x:x[2]-(4*x[1]+2)),
      ("q <= k",    lambda x:x[3]-x[2]),
      ("2S <= k",   lambda x:x[7]-x[2]),
      ("f <= e-1",  lambda x:x[5]-(x[4]-1)),
      ("g <= 4f+2", lambda x:x[6]-(4*x[5]+2)),
      ("g <= q",    lambda x:x[6]-x[3])]
def viol(x): return [(nm,fn(x)) for nm,fn in CONS if fn(x)>0]
outside=[y for y in BOX if y not in LAM]
print("="*90)
print("  TESTING THE LOAD RULE — three candidate definitions")
print("="*90)
print("""
  L1  TIGHTNESS : cells of Lambda where the constraint holds with EQUALITY
  L2  EXCLUSION : cells of the box removed by this constraint ALONE
  L3  FRONTIER  : cells outside violating ONLY this constraint, by 1
""")
rows=[]
for nm,fn in CONS:
    L1=sum(1 for x in LAM if fn(x)==0)
    L2=sum(1 for y in BOX if fn(y)>0)
    front=[y for y in outside if len(viol(y))==1 and viol(y)[0][0]==nm and viol(y)[0][1]==1]
    L3=len(front)
    A=[csz(np.array(LL+[y],dtype=np.int32))-len(LAM)-1 for y in random.sample(front,min(16,len(front)))] if front else []
    rows.append((nm,L1,L2,L3,np.median(A) if A else np.nan,min(A) if A else np.nan))
print("  %-13s%10s%10s%10s%12s%10s"%("constraint","L1 tight","L2 excl","L3 front","median A","min A"))
print("  "+"-"*68)
for nm,L1,L2,L3,md,mn in rows:
    print("  %-13s%10d%10d%10d%12.0f%10.0f"%(nm,L1,L2,L3,md,mn))
A=np.array([r[4] for r in rows]); 
print("\n  CORRELATIONS WITH MEDIAN AMPLIFICATION\n")
for i,lab in [(1,"L1 tightness"),(2,"L2 exclusion"),(3,"L3 frontier")]:
    v=np.array([r[i] for r in rows],dtype=float)
    c=np.corrcoef(v,A)[0,1]
    cs=np.corrcoef(np.argsort(np.argsort(v)),np.argsort(np.argsort(A)))[0,1]
    print("     %-16s  Pearson %+0.3f    Spearman %+0.3f"%(lab,c,cs))
print("""
{0}
  AND THE CLAIM THAT PROMPTED THIS
{0}

  I asserted: 'A is governed by how many cells the violated constraint is
  tight on' -- and pointed at g <= 4f+2 having only 24 frontier cells.
""".format("="*90))
g_row=[r for r in rows if r[0]=="g <= 4f+2"][0]
print("     g <= 4f+2 :  L1 = %d   L2 = %d   L3 = %d   median A = %.0f"%(g_row[1],g_row[2],g_row[3],g_row[4]))
others=[r for r in rows if r[0]!="g <= 4f+2"]
print("     others    :  L1 median %d   L2 median %d   L3 median %d   A median %.0f"
      %(np.median([r[1] for r in others]),np.median([r[2] for r in others]),
        np.median([r[3] for r in others]),np.median([r[4] for r in others])))
best=max([(abs(np.corrcoef(np.array([r[i] for r in rows],dtype=float),A)[0,1]),lab,i)
          for i,lab in [(1,"L1 tightness"),(2,"L2 exclusion"),(3,"L3 frontier")]])
print("\n     **STRONGEST PREDICTOR: %s, |r| = %.3f**"%(best[1],best[0]))
print("="*90)
print("  DIRECT TEST — DOES THE RULE PREDICT A ON UNSEEN CELLS?")
print("="*90)
print("""
  Fit A against the best predictor on 5 constraints, predict the other 2.
""")
i=best[2]
v=np.array([r[i] for r in rows],dtype=float)
idx=list(range(len(rows))); random.shuffle(idx)
tr,te=idx[:5],idx[5:]
sl,ic=np.polyfit(v[tr],A[tr],1)
print("     fit on 5:  A = %.3f * %s + %.1f"%(sl,best[1].split()[0],ic))
print("\n     %-13s%12s%14s%12s"%("held out","actual A","predicted A","error %"))
for j in te:
    pr=sl*v[j]+ic
    print("     %-13s%12.0f%14.0f%12.1f"%(rows[j][0],A[j],pr,100*abs(pr-A[j])/A[j]))
print("""
{0}
  VERDICT
{0}
""".format("="*90))
r_all=np.corrcoef(v,A)[0,1]
if abs(r_all)>0.8:
    print("  **THE LOAD RULE HOLDS.** %s predicts amplification at r = %+.3f\n  across all seven constraints."%(best[1],r_all))
else:
    print("""  **THE LOAD RULE IS NOT ESTABLISHED.** The strongest of three candidate
  definitions reaches only |r| = %.3f over seven points -- too few points
  and too weak a correlation to claim a law.

  **WHAT IS ESTABLISHED IS THE SINGLE OBSERVATION**: g <= 4f+2 is both the
  least-binding constraint and the cheapest to violate. One constraint is
  an anecdote, not a rule, and CORRECTION 75 stands with 76 beside it:
  the load rule was asserted on the same single data point that refuted
  the leaf rule."""%abs(r_all))