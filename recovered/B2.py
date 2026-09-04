import numpy as np, sympy as sp, random
from itertools import product, combinations
from collections import Counter
from math import comb, log2, gcd
random.seed(31)
R=[]
def T(n,g,w=True):
    ok=(g==w); R.append(ok)
    print("  %-60s%11s%8s"%(n,str(g)[:11],"TRUE" if ok else "FALSE")); return ok
print("="*82); print("  AUDIT 2 — AGAINST THE LATTICE ALONE"); print("="*82)
print("\n  %-60s%11s%8s"%("statement","computed",""))
print("  "+"-"*79)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX)); S={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
L=sorted(S); d=8
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b)); mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
le=lambda a,b: all(p<=q for p,q in zip(a,b))
def C(Sx,dd=8):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(dd)];ph={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
T("Λ closed under join and meet",all(jn(a,b) in S and mt(a,b) in S for a in S for b in S))
T("𝓡(Λ) = Λ  and  E(Λ) = 0",C(S)==S)
T("|Λ| = 976",len(S)==976)
rkf=lambda x: sum(x)
T("rank modular on all 475,800 pairs",all(rkf(jn(a,b))+rkf(mt(a,b))==rkf(a)+rkf(b) for a,b in combinations(L,2)))
QS=sorted({x[3] for x in S})
Aq={q:{tuple(x[i] for i in (0,1,2,7)) for x in S if x[3]==q} for q in QS}
Bq={q:{tuple(x[i] for i in (4,5,6)) for x in S if x[3]==q} for q in QS}
T("Σ_q |A_q||B_q| = |Λ|",sum(len(Aq[q])*len(Bq[q]) for q in QS)==len(S))
T("|A_q| = 33,33,23,8",[len(Aq[q]) for q in QS]==[33,33,23,8])
T("|B_q| = 5,10,15,17",[len(Bq[q]) for q in QS]==[5,10,15,17])
T("|A_q| monotone decreasing",all(len(Aq[QS[i]])>=len(Aq[QS[i+1]]) for i in range(len(QS)-1)))
T("|B_q| monotone increasing",all(len(Bq[QS[i]])<=len(Bq[QS[i+1]]) for i in range(len(QS)-1)))
P=[len(Aq[q])*len(Bq[q]) for q in QS]
T("fibre peaks at q=2, 345 cells",P.index(max(P))==2 and max(P)==345)
T("fibre sequence log-concave",all(P[i]**2>=P[i-1]*P[i+1] for i in range(1,len(P)-1)))
T("⟨q⟩ = 1.4631",round(sum(q*P[i] for i,q in enumerate(QS))/sum(P),4)==1.4631)
T("every A_q closed, E=0, modular",
  all(all(jn(a,b) in Aq[q] and mt(a,b) in Aq[q] for a in Aq[q] for b in Aq[q])
      and len(C(Aq[q],4))-len(Aq[q])==0
      and all(sum(jn(a,b))+sum(mt(a,b))==sum(a)+sum(b) for a in Aq[q] for b in Aq[q]) for q in QS))
T("every B_q closed, E=0, modular",
  all(all(jn(a,b) in Bq[q] and mt(a,b) in Bq[q] for a in Bq[q] for b in Bq[q])
      and len(C(Bq[q],3))-len(Bq[q])==0
      and all(sum(jn(a,b))+sum(mt(a,b))==sum(a)+sum(b) for a in Bq[q] for b in Bq[q]) for q in QS))
is_box=lambda x,y: all(y[v]<=ub(x) for v,p,ub in CONS)
mism=0; tot=0
for _ in range(600):
    x,y=random.choice(L),random.choice(L)
    if not le(x,y): continue
    tot+=1
    I=[v for v in L if le(x,v) and le(v,y)]
    exp=int(np.prod([y[i]-x[i]+1 for i in range(8)]))
    if is_box(x,y)!=(len(I)==exp): mism+=1
T("interval-box criterion exact (%d tested)"%tot,mism==0)
rk=Counter(sum(x) for x in S)
T("largest antichain 122 at rank 11",max(rk.values())==122 and max(rk,key=rk.get)==11)
T("18 rank levels",len(rk)==18)
covers={x:[y for y in L if sum(y)==sum(x)+1 and le(x,y)] for x in L}
bot=min(L,key=sum); top=max(L,key=sum); memo={}
def paths(x):
    if x==top: return 1
    if x in memo: return memo[x]
    memo[x]=sum(paths(c) for c in covers[x]); return memo[x]
T("maximal chains = 1,113,045,672",paths(bot)==1113045672)
T("chain length = 17",sum(top)-sum(bot)==17)
def is_ji(x):
    below=[y for y in L if le(y,x) and y!=x]
    if not below: return False
    mx=[y for y in below if not any(le(y,w) and y!=w for w in below)]
    return len(mx)==1
T("17 join-irreducibles",sum(1 for x in L if is_ji(x))==17)
A=[sorted({x[i] for x in L}) for i in range(8)]
mx=[max(a) for a in A]
T("self-dual survivors = 8",sum(1 for x in S if tuple(mx[i]-x[i] for i in range(8)) in S)==8)
z=sp.symbols('z'); F=sum(v*z**k for k,v in sorted(rk.items()))
T("F(1)=976, F(-1)=2",int(F.subs(z,1))==976 and int(F.subs(z,-1))==2)
T("F_box(-1)=0",int(np.prod([sum((-1)**v for v in a) for a in A]))==0)
free={z2 for z2 in BOX if all(z2[v]<=ub(z2) for i,(v,p,ub) in enumerate(CONS) if i!=5)}
T("Pauli coupling excludes 24",len(free)-len(S)==24)
out=[z2 for z2 in BOX if z2 not in S]; y=random.choice(out)
T("delete → restored; add → amplifies",C(S-{random.choice(L)})==S and len(C(S|{y}))>len(S))
T("C(C(Λ+y)) = C(Λ+y)",C(C(S|{y}))==C(S|{y}))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True); Tt=Z**2*Rs/nu**2
Vab=sp.simplify((Tt.subs(nu,nu-h)-Tt.subs(nu,nu+h))/((Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2-Tt))
T("V = 4ν³/(h(3ν²−h²))",sp.simplify(Vab-4*nu**3/(h*(3*nu**2-h**2)))==0)
T("λ² = (2/3)T",sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2)-sp.Rational(2,3)*Tt)==0)
xs,ps=sp.symbols('x p',positive=True); cur=xs**ps; okm=True
for m2 in range(1,5):
    cur=sp.simplify(cur-sp.diff(cur,xs)**2/sp.diff(cur,xs,2))
    if sp.simplify(cur-(-1)**m2*xs**ps/(ps-1)**m2)!=0: okm=False
T("A^m(x^p) = (−1)^m x^p/(p−1)^m",okm)
kk=sp.symbols('k',positive=True)
Ve=sp.simplify((sp.exp(kk*(xs+h))-sp.exp(kk*(xs-h)))/((sp.exp(kk*(xs-h))+sp.exp(kk*(xs+h)))/2-sp.exp(kk*xs)))
T("exponential V = 2/tanh(kh/2)",sp.simplify(Ve-2/sp.tanh(kk*h/2))==0)
Rn=109737.3; Tn=lambda v: Rn/v**2
T("V floor = 32/11",abs(abs(Tn(3)-Tn(1))/abs(Tn(2)-(Tn(1)+Tn(3))/2)-32/11)<1e-9)
T("KS mirror: 248305*2−495515 = 1095",248305*2-495515==1095)
print("\n  RESULT: %d TRUE, %d FALSE, of %d"%(sum(R),len(R)-sum(R),len(R)))