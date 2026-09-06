import math, statistics as st
import numpy as np
from itertools import product, permutations
from scipy.optimize import curve_fit
from scipy import stats as SS
src=open("/tmp/ritz.py",encoding="utf-8").read()
src=src[:src.index('print("  THE RITZ EXPANSION')]
g={}; exec(src,g)
S=g["S"]; LM=g["LM"]; Rinf=g["Rinf"]; mp=g["mp"]
# p = the core's orbital count at that l, for each species
PMAP={"Cd I":{"s":5,"p":3,"d":2,"f":0},"In I":{"s":5,"p":3,"d":2,"f":0},
      "Rb I":{"s":4,"p":3,"d":1,"f":0},"Sr II":{"s":4,"p":3,"d":1,"f":0}}
OUT=[]
for nm,(c,A,lim,d) in S.items():
    RM=Rinf/(1+1/(A*mp))
    n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
    ns=c*np.sqrt(RM/(lim-E)); dd=n-ns
    if len(n)<4: continue
    def f(_,d0,d2): return d0+d2/(n-d0)**2
    try: pr,_=curve_fit(f,np.arange(len(n)),dd,p0=[dd[-1],0.1],maxfev=200000)
    except Exception: continue
    sp=nm.rsplit(" ",1)[0]; lc=nm[-1]; l=LM[lc]
    OUT.append((nm,sp,l,PMAP[sp][lc],pr[0],pr[1]))
print("  SEATON'S RATIO BY REGIME  —  Λ_phys says its domain is a REGION\n")
print(f"      {'series':<10}{'p':>3}{'δ₀':>9}{'δ₂':>9}{'δ₂/δ₀':>10}{'−ℓ(ℓ+1)/3':>12}{'ratio':>9}")
A_=[];B_=[]
for nm,sp,l,p,d0,d2 in sorted(OUT,key=lambda z:(z[3],z[2])):
    seat=-l*(l+1)/3
    r=(d2/d0)/seat if abs(seat)>1e-9 else float("nan")
    print(f"      {nm:<10}{p:>3}{d0:>9.4f}{d2:>9.4f}{d2/d0:>10.4f}{seat:>12.3f}"
          f"{r:>9.3f}")
    (A_ if p==0 else B_).append((nm,l,p,d0,d2,d2/d0,seat,r))
print()
print(f"      p = 0 : {len(A_)} series · ratio to Seaton "
      f"{st.median([x[7] for x in A_ if x[7]==x[7]]):.3f}"
      f"  sd {st.pstdev([x[7] for x in A_ if x[7]==x[7]]):.3f}")
bb=[x[7] for x in B_ if x[7]==x[7] and abs(x[6])>1e-9]
print(f"      p ≥ 1 : {len(B_)} series · ratio to Seaton "
      f"{st.median(bb):.3f}  sd {st.pstdev(bb):.3f}")
print()
print("  Λ_ryd RESTRICTED TO p = 0  —  does it close?\n")
def opR(X,dd):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(dd)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(dd) for j in range(dd) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(dd) for j in range(dd) if i!=j)}
for lab,SET in (("all 13 series",OUT),("p = 0 only",[o for o in OUT if o[3]==0]),
                ("p ≥ 1 only",[o for o in OUT if o[3]>0])):
    cells=set()
    for nm,sp,l,p,d0,d2 in SET:
        cells.add((0,l,1 if d0>0 else 0)); cells.add((1,l,1 if d2>0 else 0))
    if not cells: continue
    best=None
    for lp in permutations(sorted({c[1] for c in cells})):
        m={v:i for i,v in enumerate(lp)}
        cs={(a,m[b],c) for a,b,c in cells}
        E=len(opR(cs,3))-len(cs)
        if best is None or E<best: best=E
    print(f"      {lab:<16}{len(SET):>3} series · {len(cells)} cells · min E = {best}")
print()
print("  AND THE SIGN RULE THAT EMERGES\n")
for p0 in (0,1,2,3,4,5):
    v=[d2 for nm,sp,l,p,d0,d2 in OUT if p==p0]
    if not v: continue
    print(f"      p = {p0} : {len(v)} series · "
          f"{sum(1 for x in v if x>0)} positive · {sum(1 for x in v if x<0)} negative")
print()
print("      → δ₂ < 0 for p = 0 and δ₂ > 0 for large p. the sign of the")
print("        second Ritz coefficient is the PENETRATION, not the ℓ.")