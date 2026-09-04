import numpy as np, random
from itertools import product
random.seed(13)
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
def csz(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
CONS=[("l <= n-1",  lambda x:x[1]-(x[0]-1), 1),
      ("k <= 4l+2", lambda x:x[2]-(4*x[1]+2), 2),
      ("q <= k",    lambda x:x[3]-x[2], 3),
      ("2S <= k",   lambda x:x[7]-x[2], 7),
      ("f <= e-1",  lambda x:x[5]-(x[4]-1), 5),
      ("g <= 4f+2", lambda x:x[6]-(4*x[5]+2), 6),
      ("g <= q",    lambda x:x[6]-x[3], 6)]
DEG={0:1,1:2,2:3,3:2,4:1,5:2,6:2,7:1}
NAME={0:'n',1:'l',2:'k',3:'q',4:'e',5:'f',6:'g',7:'2S'}
def viol(x): return [(nm,fn(x)) for nm,fn,_ in CONS if fn(x)>0]
allout=[tuple(int(v) for v in g) for g in grid if tuple(int(v) for v in g) not in LAM]
print("="*84)
print("  IS VULNERABILITY CONCENTRATED AT THE LEAVES?")
print("="*84)
print("""
  TREE:   n --- l --- k --- q --- g --- f --- e
                      |
                      2S
  degrees: n=1  l=2  k=3  q=2  g=2  f=2  e=1  2S=1
  LEAVES: n, e, 2S.  Only ONE constraint bounds a leaf: 2S <= k.

  PREDICTION: cells violating 2S <= k by exactly 1, and nothing else,
  should have the LOWEST amplification.
""")
res=[]
print("  %-14s%8s%8s%10s%12s%10s%10s"%("constraint","bounds","degree","n cells","median A","min A","max A"))
print("  "+"-"*76)
for nm,fn,idx in CONS:
    cand=[y for y in allout if len(viol(y))==1 and viol(y)[0][0]==nm and viol(y)[0][1]==1]
    if not cand: 
        print("  %-14s%8s%8d%10d%12s"%(nm,NAME[idx],DEG[idx],0,"—")); continue
    s=random.sample(cand,min(14,len(cand)))
    A=[csz(np.array(LL+[y],dtype=np.int32))-len(LAM)-1 for y in s]
    res.append((nm,NAME[idx],DEG[idx],len(cand),np.median(A),min(A),max(A)))
    print("  %-14s%8s%8d%10d%12.0f%10d%10d"%(nm,NAME[idx],DEG[idx],len(cand),np.median(A),min(A),max(A)))
print("""
{0}
  VERDICT ON THE LEAF HYPOTHESIS
{0}
""".format("="*84))
if res:
    res.sort(key=lambda r:r[4])
    print("     ranked by median amplification (cheapest lie first):\n")
    for nm,b,dg,nc,md,mn,mx in res:
        print("        %-14s bounds %-3s (degree %d)   median A = %6.0f"%(nm,b,dg,md))
    leafres=[r for r in res if r[2]==1]
    intres=[r for r in res if r[2]>1]
    print()
    if leafres and intres:
        lm=np.median([r[4] for r in leafres]); im=np.median([r[4] for r in intres])
        print("     leaf-bounding constraints  : median A = %.0f"%lm)
        print("     inner-bounding constraints : median A = %.0f"%im)
        cheapest_is_leaf = res[0][2]==1
        print("\n     **CHEAPEST LIE BREAKS A %s CONSTRAINT: %s**"
              %("LEAF" if cheapest_is_leaf else "NON-LEAF", "hypothesis SUPPORTED" if cheapest_is_leaf else "hypothesis REFUTED"))
        corr=np.corrcoef([r[2] for r in res],[r[4] for r in res])[0,1]
        print("     corr( degree of bounded node , median A ) = %+.3f"%corr)
print("="*84)
print("  TEST ON A SECOND INDEX — THE RETRIEVAL LATTICE")
print("="*84)
print("""
  (routes, open, cited) with cited <= open <= routes. A PATH of 3 nodes.
  Leaves: routes and cited. Interior: open.
""")
RET={(r,o,c) for r in range(0,7) for o in range(0,r+1) for c in range(0,o+1)}
RL=sorted(RET)
AX2=[sorted({x[i] for x in RL}) for i in range(3)]
g2=np.array(list(product(*AX2)),dtype=np.int32)
def csz2(A):
    m=np.ones(len(g2),dtype=bool)
    for i in range(3):
        for j in range(3):
            if i==j: continue
            for a in range(4):
                m &= g2[:,i] <= a*g2[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
b2=csz2(np.array(RL,dtype=np.int32))
print("     |RET| = %d   closure = %d   fixed point: %s"%(len(RET),b2,b2==len(RET)))
C2=[("o <= r  [bounds o, degree 2]",lambda x:x[1]-x[0],2),
    ("c <= o  [bounds c, degree 1 LEAF]",lambda x:x[2]-x[1],1)]
out2=[tuple(int(v) for v in z) for z in g2 if tuple(int(v) for v in z) not in RET]
print("\n     %-38s%10s%12s"%("constraint","n cells","median A"))
r2=[]
for nm,fn,dg in C2:
    cand=[y for y in out2 if fn(y)==1 and all(f2(y)<=0 for n2,f2,_ in C2 if n2!=nm)]
    if not cand: continue
    A=[csz2(np.array(RL+[y],dtype=np.int32))-len(RET)-1 for y in cand[:12]]
    r2.append((nm,dg,np.median(A)))
    print("     %-38s%10d%12.0f"%(nm,len(cand),np.median(A)))
if len(r2)==2:
    leaf=[x for x in r2 if x[1]==1][0]; inner=[x for x in r2 if x[1]>1][0]
    print("\n     **%s**"%("LEAF IS CHEAPER — rule holds on a second index"
          if leaf[2]<inner[2] else "LEAF IS NOT CHEAPER — rule does NOT generalise"))