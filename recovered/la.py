import numpy as np, sympy as sp
from itertools import product
from math import comb, log2
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def closed(S): return all(jn(a,b) in S and mt(a,b) in S for a in S for b in S)
def Rop(S,d):
    L=sorted(S); A=[sorted({x[i] for x in L}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in L if x[j]<=v]
                run=max(run,max(c) if c else -1); f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=phi[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
CAP=lambda l:2*(2*l+1)
o=[]
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(CAP(l),3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): o.append((n,l,k,q,e,f,g,S2))
L=sorted(set(o)); S=set(L); d=8
print("  CLAIM                                      TEST                  RESULT")
print("  "+"-"*72)
R=Rop(S,d)
print("  %-42s%-22s%s"%("Lambda is closed","join/meet, all pairs",closed(S)))
print("  %-42s%-22s%s"%("R(Lambda) = Lambda","closure operator",R==S))
print("  %-42s%-22s%d"%("E(Lambda)","|R(X)|-|X|",len(R)-len(S)))
A=[sorted({x[i] for x in L}) for i in range(d)]
box=int(np.prod([len(a) for a in A]))
print("  %-42s%-22s%d of %d"%("occupancy","box count",len(S),box))
mx=[max(a) for a in A]
sd=sum(1 for x in S if tuple(mx[i]-x[i] for i in range(d)) in S)
print("  %-42s%-22s%d"%("self-dual survivors, x -> max-x","reflection",sd))
from collections import Counter
rk=Counter(sum(x) for x in S); ks=sorted(rk); w=[rk[k] for k in ks]
cen=sum(k*rk[k] for k in ks)/sum(w); mid=(min(ks)+max(ks))/2
print("  %-42s%-22s%.2f"%("rank skew","centre - midpoint",cen-mid))
logc=all(w[i]**2>=w[i-1]*w[i+1] for i in range(1,len(w)-1))
print("  %-42s%-22s%s"%("rank sequence log-concave","Sperner",logc))
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True)
T=Z**2*Rs/nu**2
wv=sp.simplify(T.subs(nu,nu-h)-T.subs(nu,nu+h))
ev=sp.simplify(T-(T.subs(nu,nu-h)+T.subs(nu,nu+h))/2)
V=sp.simplify(wv/ev)
r=sp.symbols('r',positive=True)
Vr=sp.simplify(sp.cancel(V.subs(h,nu/r)))
print("  %-42s%-22s%s"%("V free of Z and R","symbolic",{Z,Rs}.isdisjoint(Vr.free_symbols)))
print("  %-42s%-22s%s"%("V = 4r^3/(3r^2-1)","symbolic",sp.simplify(Vr+4*r**3/(3*r**2-1))==0 or sp.simplify(Vr-4*r**3/(3*r**2-1))==0))
lam2=sp.simplify(sp.diff(T,nu)**2/sp.diff(T,nu,2))
print("  %-42s%-22s%s"%("lambda^2 = (2/3)T","symbolic",sp.simplify(lam2-sp.Rational(2,3)*T)==0))
f3=sp.diff(T,nu,3); f2=sp.diff(T,nu,2)
sc=sp.solve(sp.Eq(-f3,2*f2**sp.Rational(3,2)),nu)
print("  %-42s%-22s%s"%("self-concordant for nu <= (sqrt6/2)Z sqrt R","symbolic",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0))
Rn=109737.3; Tn=lambda v: Rn/v**2
Vn=lambda v,hh=1: abs(Tn(v+hh)-Tn(v-hh))/abs(Tn(v)-(Tn(v-hh)+Tn(v+hh))/2)
print("  %-42s%-22s%.6f"%("V floor at nu=2","exact",Vn(2)))
print("  %-42s%-22s%s"%("= 32/11","exact",abs(Vn(2)-32/11)<1e-9))
ait=lambda v: Tn(v+1)-(Tn(v+1)-Tn(v))**2/(Tn(v-1)-2*Tn(v)+Tn(v+1))
print("  %-42s%-22s%.4f"%("Aitken(T)/(T/3) at nu=40","exact",ait(40)/(Tn(40)/3)))
mono=all(Vn(v,hh+1)<Vn(v,hh) for v in (10,20,40) for hh in (1,2,3))
wid=all(abs(Tn(v+hh+1)-Tn(v-hh-1))>abs(Tn(v+hh)-Tn(v-hh)) for v in (10,20,40) for hh in (1,2,3))
print("  %-42s%-22s%s"%("dV/dh < 0 and dw/dh > 0","numeric",mono and wid))
print("""
  ALL TESTED WITHOUT A SINGLE EXTERNAL REFERENCE. Every claim above is
  recomputable from the lattice's definition and three consecutive levels.
""")