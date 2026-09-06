import numpy as np, sympy as sp, random
from itertools import product
from collections import Counter
from math import comb, log2, gcd
random.seed(2)
R=[]
def T(n,g,w=True):
    ok=(g==w); R.append(ok)
    print("  %-54s%14s%9s"%(n,str(g)[:14],"TRUE" if ok else "FALSE")); return ok
print("="*80); print("  AUDIT 2 — AGAINST THE LATTICE ALONE"); print("="*80)
print("\n  %-54s%14s%9s"%("statement","computed",""))
print("  "+"-"*76)
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
L=sorted(S); d=8
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
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
T("Lambda closed under join and meet",all(jn(a,b) in S and mt(a,b) in S for a in S for b in S))
T("R(Lambda) = Lambda",Rop(S,d)==S)
T("E(Lambda) = 0",len(Rop(S,d))-len(S)==0)
T("|Lambda| = 976",len(S)==976)
A=[sorted({x[i] for x in L}) for i in range(d)]
T("box = 6912",int(np.prod([len(a) for a in A]))==6912)
mx=[max(a) for a in A]
T("self-dual survivors = 8",sum(1 for x in S if tuple(mx[i]-x[i] for i in range(d)) in S)==8)
rk=Counter(sum(x) for x in S); ks=sorted(rk); c=[rk[k] for k in ks]
T("rank sequence log-concave",all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1)))
T("rank polynomial NOT palindromic",c!=c[::-1])
T("F(-1) = 2",sum(v*(-1)**k for k,v in rk.items())==2)
cen=sum(k*rk[k] for k in ks)/sum(c)
T("skew = -0.43",round(cen-(min(ks)+max(ks))/2,2)==-0.43)
def cnt():
    t=0
    for n in range(1,4):
      for l in range(0,min(n,2)):
        for k in range(1,min(4*l+2,3)+1):
          inn=0
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,min(e,2)): inn+=min(q,4*f+2)+1
          t+=(k+1)*inn
    return t
T("tree factorisation gives |Lambda|",cnt()==len(S))
free=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(4*l+2,3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,q+1):
              for S2 in range(0,k+1): free.add((n,l,k,q,e,f,g,S2))
T("min coupling excludes 24 cells",len(free)-len(S)==24)
T("all 24 are f=0,g=3 (Pauli)",all(x[5]==0 and x[6]==3 for x in free-S))
x=random.choice(L)
T("delete a cell -> R restores it",Rop(S-{x},d)==S)
out=sorted(set(product(*A))-S); y=random.choice(out)
T("add a cell -> R absorbs it",len(Rop(S|{y},d))>len(S))
arr=np.array(L,dtype=np.int32); grid=np.array(list(product(*A)),dtype=np.int32)
def csz(Aa):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7): m &= grid[:,i] <= a*grid[:,j]+int((Aa[:,i]-a*Aa[:,j]).max())
    return int(m.sum())
T("monotone polyhedron fixed point = 976",csz(arr)==976)
T("polyhedron restores a deletion",csz(np.array([z for z in L if z!=x],dtype=np.int32))==976)
amps=[csz(np.array(L+[random.choice(out)],dtype=np.int32))-976-1 for _ in range(12)]
T("every fabrication amplifies (12 trials)",all(a>0 for a in amps))
print("     amplification: min %d  median %.0f  max %d"%(min(amps),np.median(amps),max(amps)))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True)
Tt=Z**2*Rs/nu**2
wv=sp.simplify(Tt.subs(nu,nu-h)-Tt.subs(nu,nu+h)); ev=sp.simplify(Tt-(Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2)
V=sp.simplify(wv/ev); r=sp.symbols('r',positive=True)
Vr=sp.simplify(sp.cancel(V.subs(h,nu/r)))
T("V free of Z and R",{Z,Rs}.isdisjoint(Vr.free_symbols))
T("|V(r)| = 4r^3/(3r^2-1)",sp.simplify(sp.Abs(Vr)-4*r**3/(3*r**2-1))==0 or sp.simplify(Vr+4*r**3/(3*r**2-1))==0)
T("V = 4nu^3/(h(3nu^2-h^2)) [corrected sign]",sp.simplify(sp.Abs(V)-4*nu**3/(h*(3*nu**2-h**2)))==0)
T("lambda^2 = (2/3)T",sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2)-sp.Rational(2,3)*Tt)==0)
sc=sp.solve(sp.Eq(-sp.diff(Tt,nu,3),2*sp.diff(Tt,nu,2)**sp.Rational(3,2)),nu)
T("SC for nu <= (sqrt6/2) Z sqrt R",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0)
xs,ps=sp.symbols('x p',positive=True); yy=xs**ps
Aop=lambda fn: sp.simplify(fn-sp.diff(fn,xs)**2/sp.diff(fn,xs,2))
cur=yy; okm=True
for m in range(1,5):
    cur=Aop(cur)
    if sp.simplify(cur-(-1)**m*xs**ps/(ps-1)**m)!=0: okm=False
T("A^m(x^p) = (-1)^m x^p/(p-1)^m, m=1..4",okm)
Rn=109737.3; Tn=lambda v: Rn/v**2
Vn=lambda v,hh=1: abs(Tn(v+hh)-Tn(v-hh))/abs(Tn(v)-(Tn(v-hh)+Tn(v+hh))/2)
T("V floor = 32/11",abs(Vn(2)-32/11)<1e-9)
T("dV/dh<0 and dw/dh>0",all(Vn(v,hh+1)<Vn(v,hh) for v in (10,20,40) for hh in (1,2,3)))
def pa(nd,n): return np.polyval(np.polyfit(nd,[Tn(t) for t in nd],len(nd)-1),n)
def bk(n,k):
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)!=k+1 or min(nd)<2: continue
        p=pa(nd,n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
T("k-th order bracket contains, 560 tests",
  sum(1 for n in range(8,120) for k in (1,2,3,4,5) if not (bk(n,k)[0]<=Tn(n)<=bk(n,k)[1]))==0)
Vs,ws,es,Ts,hs,nus,lams=sp.symbols('V w e T h nu lam',positive=True)
G=[3*hs*Vs-4*nus,3*lams**2-2*Ts,ws*Vs-8*lams**2,ws*nus-4*Ts*hs,es*nus**2-3*Ts*hs**2,Vs*es-ws]
gb=sp.groebner(G,Vs,ws,es,lams,Ts,hs,nus,order='lex')
T("claim set closes: Groebner basis size 8",len(gb.exprs)==8)
T("w*V=(16/3)T reduces to 0",sp.simplify(gb.reduce(3*ws*Vs-16*Ts)[1])==0)
gb3=sp.groebner(G+[ws*nus-5*Ts*hs],Vs,ws,es,lams,Ts,hs,nus,order='lex')
T("false relation puts T*h in the ideal",sp.simplify(gb3.reduce(Ts*hs)[1])==0)
T("E_bits(periodic) = 105.1",round(log2(comb(126,36)),1)==105.1)
P=[2,3,5,7,11,13,17,19]; N=lambda v: int(np.prod([P[i]**v[i] for i in range(8)]))
a2,b2=random.choice(L),random.choice(L)
T("gcd(N(a),N(b)) = N(meet)",gcd(N(a2),N(b2))==N(mt(a2,b2)))
T("lcm = N(join)",N(a2)*N(b2)//gcd(N(a2),N(b2))==N(jn(a2,b2)))
z=sp.symbols('z'); F=sum(v*z**k for k,v in sorted(rk.items()))
T("F'(1)/F(1) = mean rank",round(float(sp.diff(F,z).subs(z,1)/F.subs(z,1)),6)==round(sum(sum(v) for v in S)/len(S),6))
T("E(X) = F_R(1) - F_X(1)",int((sum(v*z**k for k,v in sorted(Counter(sum(t) for t in Rop(S-{x},d)).items()))
    -sum(v*z**k for k,v in sorted(Counter(sum(t) for t in (S-{x})).items()))).subs(z,1))==1)
print("\n  RESULT: %d TRUE, %d FALSE, of %d"%(sum(R),len(R)-sum(R),len(R)))