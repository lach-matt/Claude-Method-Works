import numpy as np, sympy as sp
from itertools import product
from collections import Counter
from math import comb, log2, gcd
R=109737.3; P=[];F=[]
def chk(n,g,w,tol=0,rel=False):
    if isinstance(w,bool): ok=(g==w)
    else:
        ok = abs(g-w)<=(tol*max(abs(w),1e-12) if rel else tol)
    (P if ok else F).append((n,g,w))
    print("  %-46s%18s%18s%7s"%(n,str(g)[:18],str(w)[:18],"ok" if ok else "FAIL"))
print("="*92); print("  AUDIT 3 — EVERY EQUATION"); print("="*92)
print("\n  %-46s%18s%18s%7s"%("equation","computed","stated",""))
print("  "+"-"*88)
CAP=lambda l:2*(2*l+1)
S=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(CAP(l),3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): S.add((n,l,k,q,e,f,g,S2))
L=sorted(S)
def Rop(Sx,dd):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(dd)];phi={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            fq={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);fq[v]=run
            phi[(i,j)]=fq
    return {x for x in product(*A) if all(x[i]<=phi[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
chk("(1) E(Lambda)=|R|-|X|=0",len(Rop(S,8))-len(S),0)
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,dd) for m in range(1,13) for dd in range(1,DAYS[m]+1)}
chk("(2) E(calendar)=7",len(Rop(CAL,2))-len(CAL),7)
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
chk("E(Janet left-step)=0",len(Rop(JAN,2))-len(JAN),0)
PR=[2,3,5,7,11,13,17,19]; N=lambda x:int(np.prod([PR[i]**x[i] for i in range(8)]))
def Om(m):
    c=0
    for p in PR:
        while m%p==0: m//=p;c+=1
    return c
x0=L[500]; y0=L[700]
chk("(5) rank(x)=Omega(N(x))",Om(N(x0)),sum(x0))
def tau(m):
    c=1
    for p in PR:
        e2=0
        while m%p==0: m//=p;e2+=1
        c*=e2+1
    return c
g0=gcd(N(x0),N(y0))
chk("(6) d(x,y)=prod(|Di|+1)",tau(N(x0)*N(y0)//(g0*g0)),int(np.prod([abs(x0[i]-y0[i])+1 for i in range(8)])))
chk("(7) d(x,x)=1",tau(1),1)
T=lambda v,Z=1: Z*Z*R/v**2
def we(v,h=1,Z=1):
    a,m,b=T(v-h,Z),T(v,Z),T(v+h,Z); return abs(b-a),abs(m-(a+b)/2)
w,e=we(20); chk("(21) V=4nu/3 (asympt, nu=20)",round(w/e,3),round(4*20/3,3),0.05,True)
chk("(24) floor 32/11",round(we(2)[0]/we(2)[1],6),round(32/11,6))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True); Tt=Z**2*Rs/nu**2
Vabs=sp.simplify((Tt.subs(nu,nu-h)-Tt.subs(nu,nu+h))/((Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2-Tt))
chk("(25) V=4nu^3/(h(3nu^2-h^2)) CORRECTED",sp.simplify(Vabs-4*nu**3/(h*(3*nu**2-h**2)))==0,True)
r=sp.symbols('r',positive=True)
chk("(25b) V(r)=4r^3/(3r^2-1)",sp.simplify(sp.cancel(Vabs.subs(h,nu/r))-4*r**3/(3*r**2-1))==0,True)
chk("V free of Z,R",{Z,Rs}.isdisjoint(sp.simplify(sp.cancel(Vabs.subs(h,nu/r))).free_symbols),True)
def Vp(p,x=20.,h=1.):
    fq=lambda t: t**p; a,m,b=fq(x-h),fq(x),fq(x+h); return abs(b-a)/abs(m-(a+b)/2)
chk("(22) V=4x/(h|p-1|), p=4",round(Vp(4),2),round(80/3,2),0.01,True)
chk("(23) V>2 for p=-2,2,4,11",all(Vp(p)>2 for p in (-2,2,4,11)),True)
chk("lambda^2=(2/3)T",sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2)-sp.Rational(2,3)*Tt)==0,True)
sc=sp.solve(sp.Eq(-sp.diff(Tt,nu,3),2*sp.diff(Tt,nu,2)**sp.Rational(3,2)),nu)
chk("SC bound (sqrt6/2)Z sqrtR",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0,True)
wt,et=we(40,1)
chk("w/T=4h/nu at nu=40",round(wt/T(40),4),0.1,0.02,True)
chk("e/T=3(h/nu)^2 at nu=40",round(et/T(40),6),round(3/1600,6),0.02,True)
chk("w*V=(16/3)T at nu=40",round(wt*wt/et,1),round(16/3*T(40),1),0.01,True)
ait=lambda v: T(v+1)-(T(v+1)-T(v))**2/(T(v-1)-2*T(v)+T(v+1))
chk("Aitken(T)=T/3 at nu=40",round(ait(40)/(T(40)/3),4),1.0,0.001)
xs,ps=sp.symbols('x p',positive=True); yy=xs**ps
chk("Aitken(y)=-y/(p-1)",sp.simplify(yy-sp.diff(yy,xs)**2/sp.diff(yy,xs,2)+yy/(ps-1))==0,True)
cur=yy; okm=True
for m in range(1,5):
    cur=sp.simplify(cur-sp.diff(cur,xs)**2/sp.diff(cur,xs,2))
    if sp.simplify(cur-(-1)**m*xs**ps/(ps-1)**m)!=0: okm=False
chk("A^m(y)=(-1)^m y/(p-1)^m",okm,True)
d4,d5=1.0057,0.9812
d2c=(d4-d5)/(1/16-1/25); d0=d4-d2c/16
chk("(31) delta_inf=0.9376",round(d0,4),0.9376)
chk("(32) delta(6s)=0.9679",round(d0+d2c/36,4),0.9679)
Zs,Iv=6,892700.
Ef=lambda dv,n=6: Iv-Zs*Zs*R/(n-dv)**2
chk("E(6s)=736,688",round(Ef(d0+d2c/36)),736688,60)
chk("convex lower delta = 0.9567",round(2*d5-d4,4),0.9567)
chk("convex bracket upper = 737,380",round(Ef(2*d5-d4)),737380,60)
chk("convex bracket lower = 735,860",round(Ef(d5)),735860,60)
chk("(40) E_bits(periodic)=105.1",round(log2(comb(126,36)),1),105.1)
chk("log2(32/11)=1.5406",round(log2(32/11),4),1.5406)
chk("log2 V at nu=40 = 5.74",round(log2(we(40)[0]/we(40)[1]),2),5.74)
Q=[-2,-3,2,2,4,3,7,-4,4,11,11/6,1,-3,-4,-3]
nn=np.logspace(np.log10(3),np.log10(60),40)
M=np.vstack([np.log(nn**p) for p in Q]); Mc=M-M.mean(axis=1,keepdims=True)
chk("(50) rank(log q)=1",bool(np.linalg.svd(Mc,compute_uv=False)[1]<1e-12),True)
z=sp.symbols('z'); rk=Counter(sum(x) for x in S)
Fp=sum(v*z**k for k,v in sorted(rk.items()))
chk("F(1)=|Lambda|",int(Fp.subs(z,1)),len(S))
chk("F(-1)=2",int(Fp.subs(z,-1)),2)
chk("F'(1)/F(1)=mean rank",round(float(sp.diff(Fp,z).subs(z,1)/Fp.subs(z,1)),4),round(sum(sum(x) for x in S)/len(S),4))
print("\n"+"="*92)
print("  RESULT: %d passed, %d FAILED, of %d"%(len(P),len(F),len(P)+len(F)))
for n,g,w in F: print("     FAIL %-44s got %s  stated %s"%(n,g,w))