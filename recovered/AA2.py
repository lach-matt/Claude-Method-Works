import numpy as np, sympy as sp, random
from itertools import product, combinations
from collections import Counter
from math import comb, log2, gcd
random.seed(23)
R=[]
def T(n,g,w=True):
    ok=(g==w); R.append(ok)
    print("  %-58s%12s%8s"%(n,str(g)[:12],"TRUE" if ok else "FALSE")); return ok
print("="*82); print("  AUDIT 2 — AGAINST THE LATTICE ALONE"); print("="*82)
print("\n  %-58s%12s%8s"%("statement","computed",""))
print("  "+"-"*78)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX)); S={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
L=sorted(S); d=8
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def C(Sx):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
T("Λ closed under join and meet",all(jn(a,b) in S and mt(a,b) in S for a in S for b in S))
T("𝓡(Λ) = Λ",C(S)==S)
T("E(Λ) = 0",len(C(S))-len(S)==0)
T("|Λ| = 976",len(S)==976)
rkf=lambda x: sum(x)
T("RANK IS MODULAR on all 475,800 pairs",
  all(rkf(jn(a,b))+rkf(mt(a,b))==rkf(a)+rkf(b) for a,b in combinations(L,2)))
PA={tuple(z[i] for i in (0,1,2,7)) for z in S}; PB={tuple(z[i] for i in (4,5,6)) for z in S}
tot=0
for qv in sorted({z[3] for z in S}):
    Sq={z for z in S if z[3]==qv}
    a={tuple(z[i] for i in (0,1,2,7)) for z in Sq}; bq={tuple(z[i] for i in (4,5,6)) for z in Sq}
    tot+=len(a)*len(bq)
T("Σ_q |A(q)|·|B(q)| = |Λ|  [two-body separation]",tot==len(S))
T("bare product ≠ |Λ|  [coupled]",len(PA)*len(PB)*4!=len(S))
A=[sorted({x[i] for x in L}) for i in range(d)]
mx=[max(a) for a in A]
T("self-dual survivors = 8",sum(1 for x in S if tuple(mx[i]-x[i] for i in range(d)) in S)==8)
rk=Counter(sum(x) for x in S); ks=sorted(rk); c=[rk[k] for k in ks]
T("rank log-concave",all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1)))
T("F(-1) = 2",sum(v*(-1)**k for k,v in rk.items())==2)
T("F_box(-1) = 0  [ℓ and f have even alphabets]",int(np.prod([sum((-1)**v for v in a) for a in A]))==0)
def cnt():
    t=0
    for n in range(1,4):
      for l in range(0,2):
        if l>n-1: continue
        for k in range(1,min(4*l+2,3)+1):
          inn=0
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,2):
                if f>e-1: continue
                inn+=min(q,4*f+2)+1
          t+=(k+1)*inn
    return t
T("tree factorisation = |Λ|",cnt()==len(S))
free={z for z in BOX if all(z[v]<=ub(z) for i,(v,p,ub) in enumerate(CONS) if i!=5)}
T("Pauli coupling excludes 24",len(free)-len(S)==24)
def build(dd):
    Cn=[c for c in CONS if c[0]<dd and c[1]<dd]
    return {z for z in product(*AX[:dd]) if all(z[v]<=ub(z) for v,p,ub in Cn)}
T("closes at every dimension 2..8",all(len(C0)>0 and all(jn(a,b)[:dd] in C0 and mt(a,b)[:dd] in C0 for a in C0 for b in C0)
   for dd in range(2,9) for C0 in [build(dd)]))
T("each Λ_d is the projection of Λ_{d+1}",
  all({z[:dd] for z in build(dd+1)}==build(dd) for dd in range(2,8)))
x=random.choice(L); out=sorted(set(product(*A))-S); y=random.choice(out)
T("delete a cell → 𝓡 restores it",C(S-{x})==S)
T("add a cell → 𝓡 absorbs it",len(C(S|{y}))>len(S))
T("C(C(Λ+y)) = C(Λ+y)  [forgery is a fixed point]",C(C(S|{y}))==C(S|{y}))
A0=[sorted({z[i] for z in L}) for i in range(d)]
def phi_of(Sx):
    Ls=sorted(Sx);Aa=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in Aa[j]:
                cc=[x[i] for x in Ls if x[j]<=v];run=max(run,max(cc) if cc else -1);f[v]=run
            ph[(i,j)]=f
    return Aa,ph
Aa,ph0=phi_of(S)
adm=lambda z: all(z[i] in Aa[i] for i in range(d)) and all(z[i]<=ph0[(i,j)].get(z[j],-1) for i in range(d) for j in range(d) if i!=j)
T("ASKED of Λ: 200/200 fabrications refused",sum(1 for _ in range(200) if not adm(random.choice(out)))==200)
amps=[len(C(S|{random.choice(out)}))-len(S)-1 for _ in range(8)]
T("every fabrication amplifies",all(a>0 for a in amps))
bind={(i,j) for (i,j) in ph0 if any(ph0[(i,j)][v]<max(Aa[i]) for v in Aa[j])}
E={(j,i) for (i,j) in bind}
def reach(E,src,skip):
    seen={src}; st=[src]
    while st:
        u=st.pop()
        for (a2,b2) in E:
            if (a2,b2)==skip: continue
            if a2==u and b2 not in seen: seen.add(b2); st.append(b2)
    return seen
red={e for e in E if e[1] not in reach(E,e[0],e)}
T("transitive reduction recovers the 7-edge tree",red=={(p,v) for v,p,_ in CONS})
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True); Tt=Z**2*Rs/nu**2
Vab=sp.simplify((Tt.subs(nu,nu-h)-Tt.subs(nu,nu+h))/((Tt.subs(nu,nu-h)+Tt.subs(nu,nu+h))/2-Tt))
T("V = 4ν³/(h(3ν²−h²))",sp.simplify(Vab-4*nu**3/(h*(3*nu**2-h**2)))==0)
r=sp.symbols('r',positive=True)
T("V(r) = 4r³/(3r²−1)",sp.simplify(sp.cancel(Vab.subs(h,nu/r))-4*r**3/(3*r**2-1))==0)
T("λ² = (2/3)T",sp.simplify(sp.diff(Tt,nu)**2/sp.diff(Tt,nu,2)-sp.Rational(2,3)*Tt)==0)
sc=sp.solve(sp.Eq(-sp.diff(Tt,nu,3),2*sp.diff(Tt,nu,2)**sp.Rational(3,2)),nu)
T("self-concordant for ν ≤ (√6/2)Z√R",sp.simplify(sc[0]-sp.sqrt(6)*Z*sp.sqrt(Rs)/2)==0)
xs,ps=sp.symbols('x p',positive=True); cur=xs**ps; okm=True
for m2 in range(1,5):
    cur=sp.simplify(cur-sp.diff(cur,xs)**2/sp.diff(cur,xs,2))
    if sp.simplify(cur-(-1)**m2*xs**ps/(ps-1)**m2)!=0: okm=False
T("A^m(x^p) = (−1)^m x^p/(p−1)^m",okm)
kk=sp.symbols('k',positive=True)
Ve=sp.simplify((sp.exp(kk*(xs+h))-sp.exp(kk*(xs-h)))/((sp.exp(kk*(xs-h))+sp.exp(kk*(xs+h)))/2-sp.exp(kk*xs)))
T("exponential: V = 2/tanh(kh/2) → 2",sp.simplify(sp.limit(Ve.subs(h,sp.Symbol('t')/kk),sp.Symbol('t'),sp.oo))==2)
Rn=109737.3; Tn=lambda v: Rn/v**2
Vn=lambda v,hh=1: abs(Tn(v+hh)-Tn(v-hh))/abs(Tn(v)-(Tn(v-hh)+Tn(v+hh))/2)
T("V floor = 32/11",abs(Vn(2)-32/11)<1e-9)
def pa(nd,n): return np.polyval(np.polyfit(nd,[Tn(t) for t in nd],len(nd)-1),n)
def bk(n,k):
    lo,hi=-np.inf,np.inf
    for m2 in range(0,k+2):
        bl=k+1-m2
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m2+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)!=k+1 or min(nd)<2: continue
        p=pa(nd,n)
        if (k+1+m2)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
T("k-th order bracket contains, 560 tests",
  sum(1 for n in range(8,120) for k in (1,2,3,4,5) if not (bk(n,k)[0]<=Tn(n)<=bk(n,k)[1]))==0)
Vs,ws,es,Ts,hs,nus,lams=sp.symbols('V w e T h nu lam',positive=True)
G=[3*hs*Vs-4*nus,3*lams**2-2*Ts,ws*Vs-8*lams**2,ws*nus-4*Ts*hs,es*nus**2-3*Ts*hs**2,Vs*es-ws]
gb=sp.groebner(G,Vs,ws,es,lams,Ts,hs,nus,order='lex')
T("Gröbner basis size 8",len(gb.exprs)==8)
T("E_bits(periodic) = 105.1",round(log2(comb(126,36)),1)==105.1)
PR=[2,3,5,7,11,13,17,19]; N=lambda v:int(np.prod([PR[i]**v[i] for i in range(8)]))
a2,b2=random.choice(L),random.choice(L)
T("gcd = N(meet), lcm = N(join)",gcd(N(a2),N(b2))==N(mt(a2,b2)) and N(a2)*N(b2)//gcd(N(a2),N(b2))==N(jn(a2,b2)))
print("\n  RESULT: %d TRUE, %d FALSE, of %d"%(sum(R),len(R)-sum(R),len(R)))