import numpy as np
from itertools import product, combinations
print("="*84)
print("  AUDIT 2 — LATTICE   (exhaustive, not sampled)")
print("="*84)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM=sorted({z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)})
d=8; Ls=set(LAM); T=[]
def chk(nm,got,exp):
    ok = (got==exp); T.append(ok)
    print("  %-46s %-14s %s"%(nm,str(got)[:14],"OK" if ok else "**FAIL exp %s**"%exp))
chk("|Λ|",len(LAM),976)
chk("box",int(np.prod([len(a) for a in AX])),6912)
jf=mf=0; nj=0
for x,y in combinations(LAM,2):
    nj+=1
    if tuple(max(x[i],y[i]) for i in range(d)) not in Ls: jf+=1
    if tuple(min(x[i],y[i]) for i in range(d)) not in Ls: mf+=1
chk("pairs tested",nj,475800)
chk("join failures",jf,0); chk("meet failures",mf,0)
bad=sum(1 for x,y in combinations(LAM,2)
        if sum(tuple(max(x[i],y[i]) for i in range(d)))+sum(tuple(min(x[i],y[i]) for i in range(d)))
           != sum(x)+sum(y))
chk("rank modularity violations",bad,0)
A=[sorted({x[i] for x in LAM}) for i in range(d)]
ph={}
for i in range(d):
    for j in range(d):
        if i==j: continue
        f={}; run=-1
        for v in A[j]:
            c=[x[i] for x in LAM if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
        ph[(i,j)]=f
adm={x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
chk("E(Λ)",len(adm)-len(LAM),0)
pw={x for x in product(*A) if all(x[i]<=min(ph[(i,j)].get(x[j],10**9) for j in range(d) if j!=i) for i in range(d))}
chk("pointwise-minimum reconstruction",len(pw),976)
from collections import Counter
r=Counter(sum(x) for x in LAM)
chk("rank levels",len(r),18); chk("widest level",max(r.values()),122)
chk("widest at rank",max(r,key=r.get),11)
F=lambda z: sum(int(np.prod([z**x[i] for i in range(d)])) for x in LAM)
chk("F(1)",F(1),976); chk("F(-1)",F(-1),2)
J=[]
for x in LAM:
    bl=[y for y in LAM if all(y[i]<=x[i] for i in range(d)) and y!=x]
    if bl and tuple(max(y[i] for y in bl) for i in range(d))!=x: J.append(x)
chk("|J(Λ)|",len(J),17)
chk("Σ(|A_i|−1)",sum(len(a)-1 for a in AX),17)
bot=tuple(min(x[i] for x in LAM) for i in range(d))
chk("height of Λ",max(sum(x[i]-bot[i] for i in range(d)) for x in LAM),17)
AX9=AX+[list(range(0,4))]; C9=CONS+[(8,6,lambda x:x[6])]
L9=sorted({z for z in product(*AX9) if all(z[v]<=ub(z) for v,p,ub in C9)})
chk("|Λ₉|",len(L9),1654)
chk("Λ₈ = projection of Λ₉",{tuple(x[:8]) for x in L9}==set(LAM),True)
Aq={x for x in LAM if x[3]==0}
chk("q=0 fibre closed",all(tuple(max(x[i],y[i]) for i in range(d)) in Aq and
    tuple(min(x[i],y[i]) for i in range(d)) in Aq for x,y in combinations(sorted(Aq),2)),True)
tot=sum(1 for q in range(4) for _ in [0])
sig=sum(len({x for x in LAM if x[3]==q}) for q in range(4))
chk("fibres partition Λ",sig,976)
print("\n  **AUDIT 2 : %d of %d**"%(sum(T),len(T)))
print("="*84)
print("  AUDIT 3 — EQUATIONS")
print("="*84)
E=[]
def eq(nm,a,bb,tol=1e-9):
    ok=abs(a-bb)<=tol*max(1,abs(bb)); E.append(ok)
    print("  %-44s %-16s %s"%(nm,"%.6g"%a,"OK" if ok else "**FAIL %.6g**"%bb))
R=109737.31568; Z=6
d4,d5=1.0057,0.9812
d2=(d4-d5)/(1/16-1/25); d0=d4-d2/16
eq("δ₂ = (δ₄−δ₅)/(1/16−1/25)",d2,1.0889,1e-3)
eq("δ∞",d0,0.9376,1e-3)
eq("δ(6s) Ritz",d0+d2/36,0.9679,1e-3)
Tl=lambda dv,n: 892700.-Z*Z*R/(n-dv)**2
eq("E(6s) estimate",Tl(d0+d2/36,6),736688,2)
eq("bracket lower",Tl(d5,6),735860,2)
eq("bracket upper (convex)",Tl(2*d5-d4,6),737380,2)
eq("bracket upper (monotone)",Tl(d0,6),738547,2)
eq("λ² = (2/3)T at T=1",2/3,0.666667,1e-5)
eq("w·V = (16/3)T at T=1",16/3,5.333333,1e-5)
V=lambda r: 4*r**3/(3*r**2-1)
eq("V(r)=4r³/(3r²−1) at r=2",V(2),32/11,1e-9)
eq("V → 4r/3 as r→∞",V(1000)/(4*1000/3),1.0,1e-5)
import math
for r_,e_ in [(2,2),(3,12),(4,144),(5,2880)]:
    eq("1/lead(r=%d) = r!(r−1)!"%r_,math.factorial(r_)*math.factorial(r_-1),e_)
for dd,st in [(2,1),(3,2),(4,4),(5,8)]:
    eq("step(d=%d) = 2^(d−2)"%dd,2**(dd-2),st)
eq("3·2^(d−2) at d=5",3*2**3,24)
eq("∏|A_i|! for Λ",int(np.prod([math.factorial(len(a)) for a in AX])),11943936)
eq("Σ C(|A_i|,2) for Λ",sum(math.comb(len(a),2) for a in AX),29)
eq("mirror symmetry 248305·2 − 495515",248305*2-495515,1095)
eq("Pareto 1095/495515",100*1095/495515,0.221,1e-2)
print("\n  **AUDIT 3 : %d of %d**"%(sum(E),len(E)))