import numpy as np, sympy as sp
from itertools import product
from collections import Counter
from math import comb, log2
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def closed(S): return all(jn(a,b) in S and mt(a,b) in S for a in S for b in S)
def Rop(S,d):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]
                run=max(run,max(c) if c else -1); f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=phi[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
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
print("="*74); print("  AUDIT II — AGAINST THE LATTICE ALONE"); print("="*74)
print("\n  %-46s%-14s%s"%("claim","test","result"))
print("  "+"-"*72)
def row(c,t,r): print("  %-46s%-14s%s"%(c,t,r))
R=Rop(S,d)
row("Lambda closed under join and meet","all pairs",closed(S))
row("R(Lambda) = Lambda","closure op",R==S)
row("E(Lambda) = 0","count",len(R)-len(S)==0)
A=[sorted({x[i] for x in L}) for i in range(d)]
box=int(np.prod([len(a) for a in A]))
row("occupancy 976 of 6912","box",f"{len(S)} of {box}")
mx=[max(a) for a in A]
row("self-dual survivors = 8","reflection",sum(1 for x in S if tuple(mx[i]-x[i] for i in range(d)) in S))
rk=Counter(sum(x) for x in S); ks=sorted(rk); c=[rk[k] for k in ks]
row("rank sequence log-concave","c_i^2>=c_-c_+",all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1)))
cen=sum(k*rk[k] for k in ks)/sum(c); mid=(min(ks)+max(ks))/2
row("skew = -0.43","centre-mid",round(cen-mid,2))
row("rank polynomial NOT palindromic","c vs rev(c)",c!=c[::-1])
row("F(-1) = 2","alt sum",sum(v*(-1)**k for k,v in rk.items()))
def cnt():
    t=0
    for n in range(1,4):
      for l in range(0,min(n,2)):
        for k in range(1,min(4*l+2,3)+1):
          inn=0
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,min(e,2)):
                inn+=min(q,4*f+2)+1
          t+=(k+1)*inn
    return t
row("tree factorisation gives |Lambda|","nested sum",cnt()==len(S))
free=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(4*l+2,3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,q+1):
              for S2 in range(0,k+1): free.add((n,l,k,q,e,f,g,S2))
row("min coupling excludes 24 cells","free-Lambda",len(free)-len(S))
row("all excluded have f=0, g=3 (Pauli)","inspect",all(x[5]==0 and x[6]==3 for x in free-S))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True)
T=Z**2*Rs/nu**2
wv=sp.simplify(T.subs(nu,nu-h)-T.subs(nu,nu+h)); ev=sp.simplify(T-(T.subs(nu,nu-h)+T.subs(nu,nu+h))/2)
V=sp.simplify(wv/ev); r=sp.symbols('r',positive=True)
Vr=sp.simplify(sp.cancel(V.subs(h,nu/r)))
row("V free of Z and R","symbolic",{Z,Rs}.isdisjoint(Vr.free_symbols))
row("V = 4r^3/(3r^2-1)","symbolic",sp.simplify(Vr-4*r**3/(3*r**2-1))==0)
lam2=sp.simplify(sp.diff(T,nu)**2/sp.diff(T,nu,2))
row("lambda^2 = (2/3)T","symbolic",sp.simplify(lam2-sp.Rational(2,3)*T)==0)
sc=sp.solve(sp.Eq(-sp.diff(T,nu,3),2*sp.diff(T,nu,2)**sp.Rational(3,2)),nu)
row("SC for nu <= (sqrt6/2)Z sqrt(R)","symbolic",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0)
Rn=109737.3; Tn=lambda v: Rn/v**2
Vn=lambda v,hh=1: abs(Tn(v+hh)-Tn(v-hh))/abs(Tn(v)-(Tn(v-hh)+Tn(v+hh))/2)
row("V floor = 32/11","exact",abs(Vn(2)-32/11)<1e-9)
ait=lambda v: Tn(v+1)-(Tn(v+1)-Tn(v))**2/(Tn(v-1)-2*Tn(v)+Tn(v+1))
row("Aitken(T) -> T/3","exact",round(ait(40)/(Tn(40)/3),4))
row("dV/dh<0 and dw/dh>0","numeric",
    all(Vn(v,hh+1)<Vn(v,hh) for v in (10,20,40) for hh in (1,2,3)))
def poly_at(nd,ys,n):
    return np.polyval(np.polyfit(nd,ys,len(nd)-1),n)
def bk(n,k):
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)!=k+1 or min(nd)<2: continue
        p=poly_at(nd,[Tn(x) for x in nd],n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
bad=sum(1 for n in range(8,120) for k in (1,2,3,4,5) if not (bk(n,k)[0]<=Tn(n)<=bk(n,k)[1]))
row("k-th order bracket contains, k=1..5","560 tests",f"{bad} failures")
Vm=[abs(bk(n,k)[1]-bk(n,k)[0])/abs(poly_at(sorted([n+j for j in range(-k,k+1) if j],
     ),[Tn(x) for x in sorted([n+j for j in range(-k,k+1) if j])],n)-Tn(n)) for n in (20,40,80) for k in (1,2,3)]
row("V at matched order ~ 2","median",round(float(np.median(Vm)),3))
Vs,ws,es,Ts,hs,nus,lams=sp.symbols('V w e T h nu lam',positive=True)
G=[3*hs*Vs-4*nus,3*lams**2-2*Ts,ws*Vs-8*lams**2,ws*nus-4*Ts*hs,es*nus**2-3*Ts*hs**2,Vs*es-ws]
gb=sp.groebner(G,Vs,ws,es,lams,Ts,hs,nus,order='lex')
row("claim set closes (Groebner)","basis size",len(gb.exprs))
row("w*V=(16/3)T reduces to 0","ideal member",sp.simplify(gb.reduce(3*ws*Vs-16*Ts)[1])==0)
Ebits=log2(comb(126,36))
row("E(periodic table) = 105 bits","log2 C(126,36)",round(Ebits,1))
print("""
  **EVERY LINE RECOMPUTED FROM THE LATTICE DEFINITION AND THREE
  CONSECUTIVE LEVELS. NO CITATION, NO FETCH, NO SEARCH RESULT.**
""")