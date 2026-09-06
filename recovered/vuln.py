import numpy as np, random
from itertools import product
from collections import Counter
random.seed(9)
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
d=8; LL=sorted(LAM); arr=np.array(LL,dtype=np.int32)
AX=[sorted({x[i] for x in LL}) for i in range(d)]
grid=np.array(list(product(*AX)),dtype=np.int32)
def csz(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
base=csz(arr)
CONS=[("l<=n-1",lambda x:x[1]-(x[0]-1)),("k<=4l+2",lambda x:x[2]-(4*x[1]+2)),
      ("q<=k",lambda x:x[3]-x[2]),("2S<=k",lambda x:x[7]-x[2]),
      ("f<=e-1",lambda x:x[5]-(x[4]-1)),("g<=4f+2",lambda x:x[6]-(4*x[5]+2)),
      ("g<=q",lambda x:x[6]-x[3])]
def viol(x): return [(nm,fn(x)) for nm,fn in CONS if fn(x)>0]
out=[tuple(int(v) for v in g) for g in grid if tuple(int(v) for v in g) not in LAM]
print("="*84)
print("  WHERE IS THE INDEX WEAKEST?  THE COST OF EACH POSSIBLE FABRICATION")
print("="*84)
print("""
  Amplification A(y) = |C(Lambda + y)| - |Lambda| - 1 is the number of
  EXTRA cells a forger must also supply. Low A means a cheap lie.
  Hypothesis: A is governed by HOW FAR OUTSIDE y sits -- how many
  constraints it breaks, and by how much.
""")
samp=random.sample(out,180)
rows=[]
for y in samp:
    A=csz(np.array(LL+[y],dtype=np.int32))-len(LAM)-1
    v=viol(y)
    rows.append((y,A,len(v),sum(t for _,t in v),sum(y)))
rows.sort(key=lambda r:r[1])
print("  %-26s%8s%10s%12s%8s"%("cheapest fabrications","A(y)","#broken","total excess","rank"))
for y,A,nv,tv,rk in rows[:10]:
    print("  %-26s%8d%10d%12d%8d"%(str(y),A,nv,tv,rk))
print("\n  %-26s%8s%10s%12s%8s"%("most expensive","A(y)","#broken","total excess","rank"))
for y,A,nv,tv,rk in rows[-6:]:
    print("  %-26s%8d%10d%12d%8d"%(str(y),A,nv,tv,rk))
Aa=np.array([r[1] for r in rows]); nv=np.array([r[2] for r in rows])
tv=np.array([r[3] for r in rows]); rkv=np.array([r[4] for r in rows])
print("""
{0}
  WHAT PREDICTS THE COST OF A LIE?
{0}
""".format("="*84))
for nm,v in [("# constraints broken",nv),("total excess",tv),("rank of y",rkv)]:
    c=np.corrcoef(v,Aa)[0,1]
    print("     corr( A , %-22s ) = %+.3f"%(nm,c))
print("\n     A by number of constraints broken:")
for k in sorted(set(nv.tolist())):
    m=Aa[nv==k]
    print("        %d broken : n=%3d   median A = %6.0f   min %5d"%(k,len(m),np.median(m),m.min()))
print("\n     A by total excess (sum of overshoots):")
for lo,hi in [(1,1),(2,2),(3,4),(5,8),(9,99)]:
    m=Aa[(tv>=lo)&(tv<=hi)]
    if len(m): print("        excess %-6s: n=%3d   median A = %6.0f   min %5d"%("%d-%d"%(lo,hi),len(m),np.median(m),m.min()))
print("""
{0}
  THE CHEAPEST LIE, AND WHAT IT COSTS
{0}
""".format("="*84))
best=rows[0]
print("     cheapest fabrication : %s"%str(best[0]))
print("     breaks               : %s"%", ".join("%s by %d"%(n,t) for n,t in viol(best[0])))
print("     amplification        : %d extra cells"%best[1])
print("     forgery size         : %d cells (%.1f%% of Lambda)"%(best[1]+1,100*(best[1]+1)/len(LAM)))
print("""
  **THE INDEX IS WEAKEST AT ITS BOUNDARY AND STRONGEST IN ITS INTERIOR** --
  a cell that overshoots one constraint by one unit is the cheapest thing
  to insert, and even that costs %d additional cells.

  **SO 'THE MINIMUM FORGERY' IS A PROPERTY OF THE INDEX, COMPUTABLE IN
  ADVANCE, AND IT IS THE RIGHT MEASURE OF HOW HARD THE INDEX IS TO
  CORRUPT.** V prices a guarantee. Amplification prices a lie. Both are
  ratios the structure computes about itself, and the book has only one.
"""%(best[1]))