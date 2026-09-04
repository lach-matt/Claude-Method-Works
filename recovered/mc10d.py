from itertools import combinations
from lam8 import L8
import numpy as np
cells=L8()
# indices: 0n 1l 2k 3q 4e 5f 6g 7S
lo=[];hi=[]
for a,b in combinations(cells,2):
    lo.append([min(u,v) for u,v in zip(a,b)]); hi.append([max(u,v) for u,v in zip(a,b)])
LO=np.array(lo,dtype=np.int8); HI=np.array(hi,dtype=np.int8); N=len(LO)
C={'l<=n-1':HI[:,1]<=LO[:,0]-1,'k<=2(2l+1)':HI[:,2]<=4*LO[:,1]+2,'q<=k':HI[:,3]<=LO[:,2],
   'g<=q':HI[:,6]<=LO[:,3],'g<=2(2f+1)':HI[:,6]<=4*LO[:,5]+2,'f<=e-1':HI[:,5]<=LO[:,4]-1,
   '2S<=k':HI[:,7]<=LO[:,2]}
def lift(a,b,cond=None):
    A,B=C[a],C[b]
    m=np.ones(N,bool) if cond is None else cond
    n=m.sum()
    if n==0: return float('nan')
    pa=A[m].mean(); pb=B[m].mean(); pab=(A&B)[m].mean()
    return pab/(pa*pb) if pa*pb>0 else float('nan')
print("TEST 1 — conditional independence given the SHARED coordinate's interval")
tests=[('q<=k','g<=q',3,'q'),('k<=2(2l+1)','q<=k',2,'k'),('q<=k','2S<=k',2,'k'),
       ('l<=n-1','k<=2(2l+1)',1,'l'),('g<=q','g<=2(2f+1)',6,'g')]
for a,b,ci,cn in tests:
    raw=lift(a,b)
    ls=[]; ws=[]
    for v_lo in range(0,4):
        for v_hi in range(0,4):
            m=(LO[:,ci]==v_lo)&(HI[:,ci]==v_hi)
            if m.sum()<500: continue
            l=lift(a,b,m)
            if not np.isnan(l): ls.append(l); ws.append(m.sum())
    avg=np.average(ls,weights=ws) if ls else float('nan')
    print(f"  {a:11s} & {b:11s} share {cn}: raw lift {raw:.4f} -> mean lift given ({cn}lo,{cn}hi) {avg:.4f}  (strata {len(ls)})")
print()
print("TEST 2 — non-adjacent constraint pairs (no shared coordinate)")
for a,b in [('l<=n-1','g<=q'),('l<=n-1','f<=e-1'),('f<=e-1','2S<=k'),('l<=n-1','2S<=k'),('k<=2(2l+1)','f<=e-1')]:
    print(f"  {a:11s} & {b:11s}: lift {lift(a,b):.4f}")
print()
print("TEST 3 — narrowness mechanism: containment vs box width in the shared coordinate")
for nm,ci in [('q<=k',2),('g<=q',3),('2S<=k',2)]:
    w=(HI[:,ci]-LO[:,ci])
    print(f"  P({nm:11s}) by width of coord {ci}: "+" ".join(f"w={v}:{C[nm][w==v].mean():.3f}" for v in range(0,4) if (w==v).sum()>200))