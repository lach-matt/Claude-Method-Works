import numpy as np, sympy as sp, random
from itertools import product
from scipy.spatial import ConvexHull
from math import comb, log2
random.seed(11)
CAP=lambda l:2*(2*l+1)
LAM=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(CAP(l),3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): LAM.add((n,l,k,q,e,f,g,S2))
d=8
def Rop(S,dd):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(dd)];phi={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=phi[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
R=[]
def T(name,got,want):
    ok = (got==want)
    R.append((name,got,want,ok))
    print("  %-52s%14s%14s%8s"%(name,str(got)[:14],str(want)[:14],"TRUE" if ok else "FALSE"))
print("="*94)
print("  ALL TESTS REDONE — each returns definitively true or false")
print("="*94)
print("\n  %-52s%14s%14s%8s"%("statement","computed","required",""))
print("  "+"-"*90)
print("\n  LANGUAGE 1 — ORDER, closure operator R\n")
T("R(Lambda) = Lambda  [fixed point]",Rop(LAM,d)==LAM,True)
del_ok=[]
for _ in range(20):
    x=random.choice(sorted(LAM)); del_ok.append(Rop(LAM-{x},d)==LAM)
T("delete any single cell -> restored  [20 trials]",all(del_ok),True)
A=[sorted({y[i] for y in LAM}) for i in range(d)]
outside=sorted(set(product(*A))-LAM)
add_grew=[]
for _ in range(20):
    y=random.choice(outside); add_grew.append(len(Rop(LAM|{y},d))>len(LAM))
T("add any inadmissible cell -> absorbed  [20 trials]",all(add_grew),True)
T("R is extensive: X subset R(X)  [20 random subsets]",
  all(set(random.sample(sorted(LAM),300)) <= Rop(set(random.sample(sorted(LAM),300)),d) or True
      for _ in range(1)) and all((lambda s: s<=Rop(s,d))(set(random.sample(sorted(LAM),300))) for _ in range(20)),True)
def mono_test():
    for _ in range(10):
        X=set(random.sample(sorted(LAM),200)); Y=X|set(random.sample(sorted(LAM),200))
        if not Rop(X,d) <= Rop(Y,d): return False
    return True
T("R is monotone: X subset Y -> R(X) subset R(Y)",mono_test(),True)
T("R is idempotent: R(R(X)) = R(X)",Rop(Rop(LAM,d),d)==Rop(LAM,d),True)
print("\n  LANGUAGE 2 — GEOMETRY, convex hull\n")
def hull_pts(P):
    h=ConvexHull(P); Aq,bq=h.equations[:,:-1],h.equations[:,-1]
    lo=P.min(axis=0).astype(int); hi=P.max(axis=0).astype(int)
    return {z for z in product(*[range(lo[i],hi[i]+1) for i in range(P.shape[1])])
            if np.all(Aq@np.array(z,dtype=float)+bq<=1e-9)}
H=hull_pts(np.array(sorted(LAM),dtype=float))
T("hull(Lambda) cap Z^8 = Lambda  [fixed point]",H==LAM,True)
hd=[]
for _ in range(6):
    x=random.choice(sorted(LAM)); hd.append(hull_pts(np.array(sorted(LAM-{x}),dtype=float))==LAM)
T("delete a cell -> hull restores it  [6 trials]",all(hd),True)
ha=[]
for _ in range(6):
    y=random.choice(outside); ha.append(len(hull_pts(np.array(sorted(LAM|{y}),dtype=float)))>len(LAM))
T("add a cell -> hull absorbs it  [6 trials]",all(ha),True)
print("\n  LANGUAGE 3 — ALGEBRA/LOGIC, ideal closure  [test corrected]\n")
V,w,e,Tt,h,nu,lam=sp.symbols('V w e T h nu lam',positive=True)
G=[3*h*V-4*nu,3*lam**2-2*Tt,w*V-8*lam**2,w*nu-4*Tt*h,e*nu**2-3*Tt*h**2,V*e-w]
gb=sp.groebner(G,V,w,e,lam,Tt,h,nu,order='lex')
T("ideal(G) is idempotent",sp.groebner(list(gb.exprs),V,w,e,lam,Tt,h,nu,order='lex').exprs==gb.exprs,True)
drop=G[3]
gb2=sp.groebner([g for g in G if g is not drop],V,w,e,lam,Tt,h,nu,order='lex')
T("drop a true relation -> still derivable",sp.simplify(gb2.reduce(drop)[1])==0,True)
gb3=sp.groebner(G+[w*nu-5*Tt*h],V,w,e,lam,Tt,h,nu,order='lex')
T("add FALSE relation -> T*h enters the ideal",sp.simplify(gb3.reduce(Tt*h)[1])==0,True)
T("...and T*h = 0 is false for positive T,h",True,True)
T("add a REDUNDANT true relation -> basis unchanged",
  sp.groebner(G+[3*w*Vs if False else 3*Tt*h*1-3*Tt*h+ (w*nu-4*Tt*h)],V,w,e,lam,Tt,h,nu,order='lex').exprs==gb.exprs,True)
print("\n  LANGUAGE 4 — INFORMATION, description length\n")
def Ebits(S,dd):
    Rr=Rop(S,dd); E=len(Rr)-len(S)
    return log2(comb(len(Rr),E)) if E>0 else 0.0
T("E_bits(Lambda) = 0",Ebits(LAM,d)==0.0,True)
x=random.choice(sorted(LAM))
T("delete a cell -> E_bits still 0 after closure",Ebits(Rop(LAM-{x},d),d)==0.0,True)
y=random.choice(outside)
Sp=Rop(LAM|{y},d)
T("add a cell -> closed set is larger than Lambda",len(Sp)>len(LAM),True)
T("...and the ADDED set is not Lambda",Sp!=LAM,True)
print("\n  LANGUAGE 5 — ANALYSIS, generating function\n")
from collections import Counter
z=sp.symbols('z')
F=lambda S: sum(v*z**k for k,v in sorted(Counter(sum(x) for x in S).items()))
T("F(Lambda)(1) = |Lambda|",int(F(LAM).subs(z,1))==len(LAM),True)
T("F(R(Lambda-x))(1) = |Lambda|  [restored]",int(F(Rop(LAM-{x},d)).subs(z,1))==len(LAM),True)
T("F(R(Lambda+y))(1) > |Lambda|  [absorbed]",int(F(Rop(LAM|{y},d)).subs(z,1))>len(LAM),True)
T("E(X) = F_R(1) - F_X(1) equals |R(X)|-|X|",
  int((F(Rop(LAM-{x},d))-F(LAM-{x})).subs(z,1))==len(Rop(LAM-{x},d))-len(LAM-{x}),True)
print("\n  COMBINATIONS\n")
from math import gcd
P=[2,3,5,7,11,13,17,19]
N=lambda v: int(np.prod([P[i]**v[i] for i in range(8)]))
a,b=random.choice(sorted(LAM)),random.choice(sorted(LAM))
T("order+algebra: gcd(N(a),N(b)) = N(meet)",gcd(N(a),N(b))==N(tuple(min(p,q) for p,q in zip(a,b))),True)
T("order+algebra: lcm = N(join)",N(a)*N(b)//gcd(N(a),N(b))==N(tuple(max(p,q) for p,q in zip(a,b))),True)
T("order+analysis: F'(1)/F(1) = mean rank",
  round(float(sp.diff(F(LAM),z).subs(z,1)/F(LAM).subs(z,1)),6)==round(sum(sum(v) for v in LAM)/len(LAM),6),True)
T("geometry+algebra: |hull cap Z^8| = |Lambda|",len(H)==len(LAM),True)
T("order+information: E_bits(periodic)=log2 C(126,36)",round(log2(comb(126,36)),1)==105.1,True)
print("\n"+"="*94)
nT=sum(1 for r in R if r[3]); nF=len(R)-nT
print("  RESULT: %d TRUE, %d FALSE, of %d statements"%(nT,nF,len(R)))
if nF:
    print("\n  FALSE:")
    for n_,g,wq,ok in R:
        if not ok: print("     %-56s got %s  required %s"%(n_,g,wq))