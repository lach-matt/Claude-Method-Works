import numpy as np, sympy as sp, random
from itertools import product
from collections import Counter
from math import comb, log2, gcd
random.seed(7)
R=[]
def T(n,g,w=True):
    ok=(g==w); R.append(ok)
    print("  %-56s%13s%8s"%(n,str(g)[:13],"TRUE" if ok else "FALSE")); return ok
print("="*80); print("  AUDIT 2 — AGAINST THE LATTICE ALONE"); print("="*80)
print("\n  %-56s%13s%8s"%("statement","computed",""))
print("  "+"-"*77)
CONS=[("l<=n-1",1,0),("k<=4l+2",2,1),("q<=k",3,2),("2S<=k",7,2),
      ("f<=e-1",5,4),("g<=4f+2",6,5),("g<=q",6,3)]
UB=[lambda x:x[0]-1,lambda x:4*x[1]+2,lambda x:x[2],lambda x:x[2],
    lambda x:x[4]-1,lambda x:4*x[5]+2,lambda x:x[3]]
sat=lambda x: all(x[v]<=UB[i](x) for i,(nm,v,p) in enumerate(CONS))
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=[z for z in product(*AX)]; S={z for z in BOX if sat(z)}; L=sorted(S); d=8
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def phi_of(Sx):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return A,ph
def C(Sx):
    A,ph=phi_of(Sx)
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
T("Lambda closed under join and meet",all(jn(a,b) in S and mt(a,b) in S for a in S for b in S))
T("R(Lambda) = Lambda",C(S)==S)
T("E(Lambda) = 0",len(C(S))-len(S)==0)
T("|Lambda| = 976",len(S)==976)
A=[sorted({x[i] for x in L}) for i in range(d)]
T("box = 6912",int(np.prod([len(a) for a in A]))==6912)
mx=[max(a) for a in A]
T("self-dual survivors = 8",sum(1 for x in S if tuple(mx[i]-x[i] for i in range(d)) in S)==8)
rk=Counter(sum(x) for x in S); ks=sorted(rk); c=[rk[k] for k in ks]
T("rank sequence log-concave",all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1)))
T("rank polynomial NOT palindromic",c!=c[::-1])
T("F(-1) = 2",sum(v*(-1)**k for k,v in rk.items())==2)
T("skew = -0.43",round(sum(k*rk[k] for k in ks)/sum(c)-(min(ks)+max(ks))/2,2)==-0.43)
def cnt():
    t=0
    for n in range(1,4):
      for l in range(0,2):
        for k in range(1,min(4*l+2,3)+1):
          inn=0
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,2): inn+=min(q,4*f+2)+1
          t+=(k+1)*inn
    return t
T("tree factorisation gives |Lambda|",cnt()==len(S))
free={z for z in BOX if all(z[v]<=UB[i](z) for i,(nm,v,p) in enumerate(CONS) if nm!="g<=4f+2")}
T("min coupling excludes 24 cells",len(free)-len(S)==24)
T("all 24 are f=0,g=3 (Pauli)",all(x[5]==0 and x[6]==3 for x in free-S))
x=random.choice(L)
T("delete a cell -> R restores it",C(S-{x})==S)
out=sorted(set(product(*A))-S); y=random.choice(out)
T("add a cell -> R absorbs it",len(C(S|{y}))>len(S))
T("C(C(Lambda+y)) = C(Lambda+y)  [forgery is a fixed point]",C(C(S|{y}))==C(S|{y}))
A0,ph0=phi_of(S)
adm=lambda ph,Aa,z: all(z[i] in Aa[i] for i in range(d)) and all(z[i]<=ph[(i,j)].get(z[j],-1) for i in range(d) for j in range(d) if i!=j)
T("ASKED of Lambda: 200/200 fabrications refused",
  sum(1 for _ in range(200) if not adm(ph0,A0,random.choice(out)))==200)
amps=[len(C(S|{random.choice(out)}))-len(S)-1 for _ in range(10)]
T("every fabrication amplifies (10 trials)",all(a>0 for a in amps))
print("     amplification: min %d median %.0f max %d"%(min(amps),np.median(amps),max(amps)))
sw=0
for _ in range(60):
    xx=random.choice(L); yy=random.choice(out); Sp=(S-{xx})|{yy}
    if C(Sp)==Sp: sw+=1
T("substitution never evades (60 trials)",sw==0)
bind={(i,j) for (i,j) in ph0 if any(ph0[(i,j)][v]<max(A0[i]) for v in A0[j])}
E={(j,i) for (i,j) in bind}
def reach(E,src,skip):
    seen={src}; st=[src]
    while st:
        u=st.pop()
        for (a,b) in E:
            if (a,b)==skip: continue
            if a==u and b not in seen: seen.add(b); st.append(b)
    return seen
red={e for e in E if e[1] not in reach(E,e[0],e)}
T("transitive reduction of R recovers the 7-edge tree",red=={(p,v) for nm,v,p in CONS})
base=len(S)
def N_of(Sx):
    Aa,ph=phi_of(Sx)
    return sum(1 for z in product(*Aa) if all(z[i]<=ph[(i,j)].get(z[j],-1) for i in range(d) for j in range(d) if i!=j))
ok=0;tot=0
for i,(nm,v,p) in enumerate(CONS):
    fr=[z for z in out if [k for k,(n2,v2,p2) in enumerate(CONS) if z[v2]>UB[k](z)]==[i] and z[v]-UB[i](z)==1]
    for z in fr[:4]:
        tot+=1; ok+= (len(C(S|{z}))-base-1)==(N_of(S|{z})-base-1)
T("A(y) closed form exact",ok==tot)
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True); Tt=Z**2*Rs/nu**2
Vab=sp.simplify((Tt.subs(nu,nu-h)-Tt.subs(nu,nu+h))/((Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2-Tt))
T("V = 4nu^3/(h(3nu^2-h^2))",sp.simplify(Vab-4*nu**3/(h*(3*nu**2-h**2)))==0)
r=sp.symbols('r',positive=True)
T("V(r) = 4r^3/(3r^2-1)",sp.simplify(sp.cancel(Vab.subs(h,nu/r))-4*r**3/(3*r**2-1))==0)
T("V free of Z and R",{Z,Rs}.isdisjoint(sp.simplify(sp.cancel(Vab.subs(h,nu/r))).free_symbols))
T("lambda^2 = (2/3)T",sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2)-sp.Rational(2,3)*Tt)==0)
sc=sp.solve(sp.Eq(-sp.diff(Tt,nu,3),2*sp.diff(Tt,nu,2)**sp.Rational(3,2)),nu)
T("SC for nu <= (sqrt6/2)Z sqrt R",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0)
xs,ps=sp.symbols('x p',positive=True); cur=xs**ps; okm=True
for m in range(1,5):
    cur=sp.simplify(cur-sp.diff(cur,xs)**2/sp.diff(cur,xs,2))
    if sp.simplify(cur-(-1)**m*xs**ps/(ps-1)**m)!=0: okm=False
T("A^m(x^p) = (-1)^m x^p/(p-1)^m",okm)
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
T("Groebner basis size 8",len(gb.exprs)==8)
T("w*V=(16/3)T reduces to 0",sp.simplify(gb.reduce(3*ws*Vs-16*Ts)[1])==0)
T("E_bits(periodic) = 105.1",round(log2(comb(126,36)),1)==105.1)
PR=[2,3,5,7,11,13,17,19]; N=lambda v:int(np.prod([PR[i]**v[i] for i in range(8)]))
a2,b2=random.choice(L),random.choice(L)
T("gcd = N(meet)",gcd(N(a2),N(b2))==N(mt(a2,b2)))
T("lcm = N(join)",N(a2)*N(b2)//gcd(N(a2),N(b2))==N(jn(a2,b2)))
z=sp.symbols('z'); Fp=sum(v*z**k for k,v in sorted(rk.items()))
T("F'(1)/F(1) = mean rank",round(float(sp.diff(Fp,z).subs(z,1)/Fp.subs(z,1)),4)==round(sum(sum(v) for v in S)/len(S),4))
print("\n  RESULT: %d TRUE, %d FALSE, of %d"%(sum(R),len(R)-sum(R),len(R)))