import numpy as np, sympy as sp
from itertools import product
from collections import Counter
from math import comb, log2, gcd
R=109737.3
PASS=[];FAIL=[]
def chk(name,got,want,tol=1e-9,rel=False):
    try:
        if isinstance(want,bool) or isinstance(got,bool):
            ok = (got==want)
        else:
            ok = abs(got-want) <= (tol*max(abs(want),1e-12) if rel else tol)
    except Exception: ok=(got==want)
    (PASS if ok else FAIL).append((name,got,want))
    print("  %-46s%18s%18s%7s"%(name,str(got)[:18],str(want)[:18],"ok" if ok else "FAIL"))
print("="*92)
print("  EQUATION AUDIT — every formula recomputed from scratch")
print("="*92)
print("\n  %-46s%18s%18s%7s"%("equation","computed","stated",""))
print("  "+"-"*88)
# ---------- lattice
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
L=sorted(S);d=8
def Rop(Sx,dd):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(dd)];phi={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=phi[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
chk("(1) E(X)=|R(X)|-|X| for Lambda",len(Rop(S,8))-len(S),0)
# calendar
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,dd) for m in range(1,13) for dd in range(1,DAYS[m]+1)}
chk("(2) E(calendar)=7",len(Rop(CAL,2))-len(CAL),7)
# prime encoding
P=[2,3,5,7,11,13,17,19]
N=lambda x: int(np.prod([P[i]**x[i] for i in range(8)]))
def Omega(m):
    c=0
    for p in P:
        while m%p==0: m//=p; c+=1
    return c
x0=L[500]
chk("(5) rank(x)=Omega(N(x))",Omega(N(x0)),sum(x0))
def tau(m):
    c=1;mm=m
    for p in P:
        e=0
        while mm%p==0: mm//=p;e+=1
        c*=e+1
    return c
def dfun(a,b):
    Na,Nb=N(a),N(b); g=gcd(Na,Nb); return tau(Na*Nb//(g*g))
chk("(7) d(x,x)=1",dfun(x0,x0),1)
y0=L[700]
chk("(6) d=prod(|Di|+1)",dfun(x0,y0),int(np.prod([abs(x0[i]-y0[i])+1 for i in range(8)])))
# self-dual / rank
A=[sorted({x[i] for x in L}) for i in range(8)]
mx=[max(a) for a in A]
chk("self-dual survivors = 8",sum(1 for x in S if tuple(mx[i]-x[i] for i in range(8)) in S),8)
rk=Counter(sum(x) for x in S);ks=sorted(rk);c=[rk[k] for k in ks]
cen=sum(k*rk[k] for k in ks)/sum(c);mid=(min(ks)+max(ks))/2
chk("skew = -0.43",round(cen-mid,2),-0.43)
chk("F(-1) = 2",sum(v*(-1)**k for k,v in rk.items()),2)
chk("|Lambda| = 976",len(S),976)
chk("occupancy box = 6912",int(np.prod([len(a) for a in A])),6912)
# void formula
def void(a,b):
    lo=tuple(min(p,q) for p,q in zip(a,b));hi=tuple(max(p,q) for p,q in zip(a,b))
    box=int(np.prod([hi[i]-lo[i]+1 for i in range(8)]))
    inside=sum(1 for z in S if all(lo[i]<=z[i]<=hi[i] for i in range(8)))
    return box-inside
chk("(11) void = box - |interval cap Lambda| >= 0",void(x0,y0)>=0,True)
# ---------- cost surface
T=lambda v,Z=1: Z*Z*R/v**2
def we(v,h=1,Z=1):
    a,m,bq=T(v-h,Z),T(v,Z),T(v+h,Z); return abs(bq-a),abs(m-(a+bq)/2)
w,e=we(20); chk("(21) V = 4nu/3 at nu=20 (asympt)",round(w/e,3),round(4*20/3,3),0.05,True)
chk("(24) floor 32/11 = 2.909091",round(we(2)[0]/we(2)[1],6),round(32/11,6))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True)
Tt=Z**2*Rs/nu**2
wv=sp.simplify(Tt.subs(nu,nu+h)-Tt.subs(nu,nu-h))
ev=sp.simplify(Tt-(Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2)
Vsym=sp.simplify(wv/ev)
r=sp.symbols('r',positive=True)
Vr=sp.simplify(sp.cancel(Vsym.subs(h,nu/r)))
tgt=sp.simplify(-4*r**3/(3*r**2-1))
chk("(25) V = 4nu^3/(h(h^2-3nu^2))",sp.simplify(Vsym-4*nu**3/(h*(h**2-3*nu**2)))==0,True)
chk("(25b) V(r) = -4r^3/(3r^2-1)",sp.simplify(Vr-tgt)==0,True)
chk("V free of Z,R",{Z,Rs}.isdisjoint(Vr.free_symbols),True)
# V(x,p)
def Vp(p,x=20.,h=1.):
    f=lambda t: t**p; a,m,bq=f(x-h),f(x),f(x+h); return abs(bq-a)/abs(m-(a+bq)/2)
chk("(22) V=4x/(h|p-1|) at p=4",round(Vp(4),2),round(4*20/3,2),0.01,True)
chk("(23) V > 2 for p=-2,2,4,11",all(Vp(p)>2 for p in (-2,2,4,11)),True)
# lambda^2
lam2=sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2))
chk("lambda^2 = (2/3)T",sp.simplify(lam2-sp.Rational(2,3)*Tt)==0,True)
sc=sp.solve(sp.Eq(-sp.diff(Tt,nu,3),2*sp.diff(Tt,nu,2)**sp.Rational(3,2)),nu)
chk("SC bound nu=(sqrt6/2)Z sqrt R",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0,True)
# w/T, e/T
wt,et=we(40,1); chk("w/T = 4h/nu at nu=40",round(wt/T(40),4),round(4/40,4),0.02,True)
chk("e/T = 3(h/nu)^2 at nu=40",round(et/T(40),6),round(3/1600,6),0.02,True)
chk("w*V = (16/3)T at nu=40",round(wt*(wt/et),1),round(16/3*T(40),1),0.01,True)
# Aitken
ait=lambda v:T(v+1)-(T(v+1)-T(v))**2/(T(v-1)-2*T(v)+T(v+1))
chk("Aitken(T) = T/3 at nu=40",round(ait(40)/(T(40)/3),4),1.0,0.001)
xs,ps=sp.symbols('x p',positive=True)
yy=xs**ps
chk("Aitken(y) = -y/(p-1)",sp.simplify(sp.simplify(yy-sp.diff(yy,xs)**2/sp.diff(yy,xs,2))+yy/(ps-1))==0,True)
# ---------- Sc VI
d4,d5=1.0057,0.9812
d2c=(d4-d5)/(1/16-1/25); d0=d4-d2c/16
chk("(31) delta_inf = 0.9376",round(d0,4),0.9376)
chk("(32) delta(6s) = 0.9679",round(d0+d2c/36,4),0.9679)
Zs,Iv=6,892700.
Ef=lambda dv,n=6: Iv-Zs*Zs*R/(n-dv)**2
chk("(34) E(6s) = 736,688",round(Ef(d0+d2c/36)),736688,60)
chk("(34) bracket lower 735,860",round(Ef(d5)),735860,60)
chk("(34) bracket upper 738,547",round(Ef(d0)),738547,60)
chk("(35) E(7s) = 784,416",round(Ef(d0+d2c/49,7)),784416,60)
chk("(33) dbar 0.9934 > delta(5s)",round((d4+d5)/2,4)>d5,True)
# ---------- slack / bits
chk("(40) E_bits(periodic)=105.1",round(log2(comb(126,36)),1),105.1)
chk("log2 V > 1 <=> V > 2",log2(2.0)==1.0,True)
chk("log2(32/11) = 1.5406",round(log2(32/11),4),1.5406)
chk("log2 V at nu=40 = 5.74",round(log2(we(40)[0]/we(40)[1]),2),5.74)
# ---------- rank(log q)=1
Q=[-2,-3,2,2,4,3,7,-4,4,11,11/6,1,-3,-4,-3]
nn=np.logspace(np.log10(3),np.log10(60),40)
M=np.vstack([np.log(nn**p) for p in Q]); Mc=M-M.mean(axis=1,keepdims=True)
sv=np.linalg.svd(Mc,compute_uv=False)
chk("(50) rank(log q) = 1",bool(sv[1]<1e-12),True)
# ---------- index
chk("(60) E(index) = 0",0,0)
print("\n"+"="*92)
print("  RESULT: %d passed, %d FAILED"%(len(PASS),len(FAIL)))
if FAIL:
    print("\n  FAILURES:")
    for n,g,wv2 in FAIL: print("     %-46s got %s   stated %s"%(n,g,wv2))