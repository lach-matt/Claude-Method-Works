import numpy as np, sympy as sp, random
from itertools import product, combinations
from collections import Counter
from math import comb, log2, gcd
random.seed(37)
P=[];F=[]
def chk(n,g,w,tol=0,rel=False):
    if isinstance(w,bool): ok=(g==w)
    else: ok=abs(g-w)<=(tol*max(abs(w),1e-12) if rel else tol)
    (P if ok else F).append((n,g,w))
    print("  %-46s%17s%17s%7s"%(n,str(g)[:17],str(w)[:17],"ok" if ok else "FAIL"))
print("="*90); print("  AUDIT 3 — EVERY EQUATION"); print("="*90)
print("\n  %-46s%17s%17s%7s"%("equation","computed","stated",""))
print("  "+"-"*86)
R=109737.3
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
S={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
L=sorted(S)
def Rop(Sx,dd):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(dd)];ph={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
chk("E(Λ)=0",len(Rop(S,8))-len(S),0)
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,d2) for m in range(1,13) for d2 in range(1,DAYS[m]+1)}
chk("E(calendar)=7",len(Rop(CAL,2))-len(CAL),7)
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
chk("E(periodic table)=36",len(Rop(PT,2))-len(PT),36)
JAN=set()
for p in range(1,9):
    wd={1:2,2:2,3:8,4:8,5:18,6:18,7:32,8:32}[p]
    for g in range(1,wd+1): JAN.add((p,g))
chk("E(Janet)=0",len(Rop(JAN,2))-len(JAN),0)
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b)); mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
chk("rank modular",all(sum(jn(a,b))+sum(mt(a,b))==sum(a)+sum(b) for a,b in combinations(L,2)),True)
QS=sorted({x[3] for x in S})
Aq={q:{tuple(x[i] for i in (0,1,2,7)) for x in S if x[3]==q} for q in QS}
Bq={q:{tuple(x[i] for i in (4,5,6)) for x in S if x[3]==q} for q in QS}
chk("Σ_q |A_q||B_q|",sum(len(Aq[q])*len(Bq[q]) for q in QS),976)
chk("fibre peak 345 at q=2",max(len(Aq[q])*len(Bq[q]) for q in QS),345)
Pr=[len(Aq[q])*len(Bq[q]) for q in QS]
chk("⟨q⟩=1.4631",round(sum(q*Pr[i] for i,q in enumerate(QS))/sum(Pr),4),1.4631)
z=sp.symbols('z')
def G(a,b,zz=z):
    if b<a: return sp.Integer(0)
    return zz**a*(1-zz**(b-a+1))/(1-zz)
def at1(e,zz=z):
    e=sp.cancel(sp.together(e))
    try:
        v=e.subs(zz,1)
        if v.is_finite and not v.has(sp.nan): return v
    except Exception: pass
    return sp.limit(e,zz,1)
def A_cf(q):
    return sum(z**(n+l+k)*G(0,min(k,3)) for n in range(1,4) for l in range(0,min(n-1,1)+1)
               for k in range(max(q,1),min(4*l+2,3)+1))
def B_cf(q):
    return sum(z**(e+f)*G(0,min(q,4*f+2,3)) for e in range(1,4) for f in range(0,min(e-1,1)+1))
for q in QS:
    chk("A_%d(1) closed form"%q,int(at1(A_cf(q))),len(Aq[q]))
    chk("B_%d(1) closed form"%q,int(at1(B_cf(q))),len(Bq[q]))
PR=[2,3,5,7,11,13,17,19]; N=lambda x:int(np.prod([PR[i]**x[i] for i in range(8)]))
x0,y0=L[500],L[700]
def Om(m):
    c=0
    for p in PR:
        while m%p==0: m//=p;c+=1
    return c
chk("rank=Ω(N(x))",Om(N(x0)),sum(x0))
chk("gcd=N(meet)",gcd(N(x0),N(y0)),N(mt(x0,y0)))
T=lambda v,Z=1: Z*Z*R/v**2
def we(v,h=1,Z=1):
    a,m,b=T(v-h,Z),T(v,Z),T(v+h,Z); return abs(b-a),abs(m-(a+b)/2)
w,e=we(20); chk("V=4ν/3 asympt",round(w/e,3),round(80/3,3),0.05,True)
chk("floor 32/11",round(we(2)[0]/we(2)[1],6),round(32/11,6))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True); Tt=Z**2*Rs/nu**2
Vab=sp.simplify((Tt.subs(nu,nu-h)-Tt.subs(nu,nu+h))/((Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2-Tt))
chk("V=4ν³/(h(3ν²−h²))",sp.simplify(Vab-4*nu**3/(h*(3*nu**2-h**2)))==0,True)
r=sp.symbols('r',positive=True)
chk("V(r)=4r³/(3r²−1)",sp.simplify(sp.cancel(Vab.subs(h,nu/r))-4*r**3/(3*r**2-1))==0,True)
chk("λ²=(2/3)T",sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2)-sp.Rational(2,3)*Tt)==0,True)
sc=sp.solve(sp.Eq(-sp.diff(Tt,nu,3),2*sp.diff(Tt,nu,2)**sp.Rational(3,2)),nu)
chk("SC ν≤(√6/2)Z√R",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0,True)
wt,et=we(40,1)
chk("w/T=4h/ν",round(wt/T(40),4),0.1,0.02,True)
chk("e/T=3(h/ν)²",round(et/T(40),6),round(3/1600,6),0.02,True)
ait=lambda v: T(v+1)-(T(v+1)-T(v))**2/(T(v-1)-2*T(v)+T(v+1))
chk("Aitken(T)=T/3",round(ait(40)/(T(40)/3),4),1.0,0.001)
xs,ps=sp.symbols('x p',positive=True); cur=xs**ps; okm=True
for m in range(1,5):
    cur=sp.simplify(cur-sp.diff(cur,xs)**2/sp.diff(cur,xs,2))
    if sp.simplify(cur-(-1)**m*xs**ps/(ps-1)**m)!=0: okm=False
chk("A^m(y)=(−1)^m y/(p−1)^m",okm,True)
kk=sp.symbols('k',positive=True)
Ve=sp.simplify((sp.exp(kk*(xs+h))-sp.exp(kk*(xs-h)))/((sp.exp(kk*(xs-h))+sp.exp(kk*(xs+h)))/2-sp.exp(kk*xs)))
chk("exp V=2/tanh(kh/2)",sp.simplify(Ve-2/sp.tanh(kk*h/2))==0,True)
d4,d5=1.0057,0.9812; d2c=(d4-d5)/(1/16-1/25); d0=d4-d2c/16
Ef=lambda dv,n=6: 892700.-36*R/(n-dv)**2
chk("δ∞=0.9376",round(d0,4),0.9376)
chk("E(6s)=736,688",round(Ef(d0+d2c/36)),736688,60)
chk("convex bracket [735860,737380] lo",round(Ef(d5)),735860,60)
chk("convex bracket hi",round(Ef(2*d5-d4)),737380,60)
chk("E_bits(periodic)=105.1",round(log2(comb(126,36)),1),105.1)
rk=Counter(sum(x) for x in S); Fp=sum(v*z**k for k,v in sorted(rk.items()))
chk("F(1)=976",int(Fp.subs(z,1)),976)
chk("F(−1)=2",int(Fp.subs(z,-1)),2)
A=[sorted({x[i] for x in L}) for i in range(8)]
chk("F_box(−1)=0",int(np.prod([sum((-1)**v for v in a) for a in A])),0)
chk("F′(1)/F(1)=mean rank",round(float(sp.diff(Fp,z).subs(z,1)/Fp.subs(z,1)),4),round(sum(sum(x) for x in S)/len(S),4))
chk("largest antichain",max(rk.values()),122)
le=lambda a,b: all(p<=q for p,q in zip(a,b))
covers={x:[y for y in L if sum(y)==sum(x)+1 and le(x,y)] for x in L}
bot=min(L,key=sum); top=max(L,key=sum); memo={}
def paths(x):
    if x==top: return 1
    if x in memo: return memo[x]
    memo[x]=sum(paths(c) for c in covers[x]); return memo[x]
chk("maximal chains",paths(bot),1113045672)
Msun=1.989e30
chk("Hill radius Jupiter",round(5.203*(1.898e27/(3*Msun))**(1/3),3),0.355,0.002)
chk("3:1 resonance",round(5.2028*(1/3)**(2/3),2),2.50,0.01)
chk("KS mirror closure",248305*2-495515,1095)
print("\n"+"="*90)
print("  RESULT: %d passed, %d FAILED, of %d"%(len(P),len(F),len(P)+len(F)))
for n,g,w in F: print("     FAIL %-44s got %s  stated %s"%(n,g,w))