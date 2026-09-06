import numpy as np, math
from itertools import product, combinations
from collections import Counter
print("="*86)
print("  MATHEMATICS AUDIT — BATCH 1 : Λ's STRUCTURE AS THE BOOK STATES IT")
print("="*86)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM=sorted({z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)})
d=8; Ls=set(LAM); R=[]
def ck(nm,got,exp,tol=0):
    ok = (abs(got-exp)<=tol) if isinstance(got,(int,float)) and isinstance(exp,(int,float)) else got==exp
    R.append((nm,ok,got,exp))
    print("  %-44s %-16s %s"%(nm,str(got)[:16],"OK" if ok else "**FAIL — book says %s**"%exp))
print("\n  --- the fibration §7.6 ---")
Aidx=[0,1,2,3,7]; Bidx=[4,5,6]
tot=0; Aq={}; Bq={}
for q in range(4):
    Aq[q]=len({tuple(x[i] for i in [0,1,2,7]) for x in LAM if x[3]==q})
    Bq[q]=len({tuple(x[i] for i in Bidx) for x in LAM if x[3]==q})
ck("|A_q| for q=0..3",[Aq[q] for q in range(4)],[33,33,23,8])
ck("|B_q| for q=0..3",[Bq[q] for q in range(4)],[5,10,15,17])
ck("Σ |A_q|·|B_q|",sum(Aq[q]*Bq[q] for q in range(4)),976)
ck("bare product Σ|A_q| · Σ|B_q|",sum(Aq.values())*sum(Bq.values()),97*47)
print("\n  --- the cylinder cross-sections §7.6 ---")
cs=[len([x for x in LAM if x[3]==q]) for q in range(4)]
ck("cells per q",cs,[165,330,345,136])
ck("cross-sections sum",sum(cs),976)
ck("peak at q=2 fraction",round(100*max(cs)/976,1),35.3,0.1)
qs=[x[3] for x in LAM]
ck("⟨q⟩",round(float(np.mean(qs)),4),1.4631,0.0002)
ck("sd(q)",round(float(np.std(qs)),3),0.930,0.002)
print("\n  --- rank structure §3.4 ---")
rk=Counter(sum(x) for x in LAM)
ck("rank levels",len(rk),18)
ck("largest antichain",max(rk.values()),122)
ck("at rank",max(rk,key=rk.get),11)
lc=all(rk[k]**2>=rk.get(k-1,0)*rk.get(k+1,0) for k in sorted(rk)[1:-1])
ck("rank sequence log-concave",lc,True)
print("\n  --- maximal chains §7.9 ---")
J=[]
for x in LAM:
    bl=[y for y in LAM if all(y[i]<=x[i] for i in range(d)) and y!=x]
    if bl and tuple(max(y[i] for y in bl) for i in range(d))!=x: J.append(x)
ck("|J(Λ)|",len(J),17)
le=lambda a,c: all(a[i]<=c[i] for i in range(d))
def linext(P):
    memo={}
    Pset=list(P)
    def rec(rem):
        if not rem: return 1
        k=frozenset(rem)
        if k in memo: return memo[k]
        s=0
        for e in rem:
            if not any(le(f,e) and f!=e for f in rem): s+=rec(rem-{e})
        memo[k]=s; return s
    return rec(frozenset(Pset))
ck("linear extensions of J(Λ)",linext(J),1113045672)
print("\n  --- the void §5 ---")
box=int(np.prod([len(a) for a in AX]))
ck("box",box,6912); ck("void",box-976,5936)
ck("density",round(976/box,4),0.1412,0.0002)
print("\n  --- intervals §3.5 ---")
import random
random.seed(11)
n=0; boxes=0
for _ in range(60):
    a,c=random.sample(LAM,2)
    lo=tuple(min(a[i],c[i]) for i in range(d)); hi=tuple(max(a[i],c[i]) for i in range(d))
    I=[x for x in LAM if all(lo[i]<=x[i]<=hi[i] for i in range(d))]
    if len(I)<2: continue
    n+=1
    full=int(np.prod([hi[i]-lo[i]+1 for i in range(d)]))
    if len(I)==full: boxes+=1
print("     intervals sampled %d   are full boxes %d   (%.0f%%)"%(n,boxes,100*boxes/max(n,1)))
print("     book: 'exact on 60/60, 27%% qualify'")
print("\n  **BATCH 1 : %d of %d**"%(sum(1 for _,o,_,_ in R if o),len(R)))
for nm,o,g,e in R:
    if not o: print("     FAIL %-40s got %s  book %s"%(nm,g,e))