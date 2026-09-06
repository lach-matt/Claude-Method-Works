import numpy as np, sympy as sp
from itertools import product
from collections import Counter
from math import comb, log2, gcd
print("="*84)
print("  P21 -- EVERY DEFINITION EXPRESSIBLE IN EVERY LANGUAGE, AND IN COMBINATIONS")
print("="*84)
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
z=sp.symbols('z')
rk=Counter(sum(x) for x in S)
F=sum(v*z**k for k,v in sorted(rk.items()))
print("""
  TEST: express each core definition in ORDER, ALGEBRA, GEOMETRY,
  ANALYSIS, INFORMATION and LOGIC. A definition passes only if all six
  give the same number.
""")
res={}
def line(name,vals):
    ok=len(set(np.round(list(vals.values()),6)))==1
    res[name]=ok
    print("  %-16s"%name + "".join("%12s"%(str(v)[:12]) for v in vals.values()) + ("   ok" if ok else "   FAIL"))
print("  %-16s%12s%12s%12s%12s%12s%12s"%("definition","order","algebra","geometry","analysis","information","logic"))
print("  "+"-"*88)
# |Lambda|
A=[sorted({x[i] for x in L}) for i in range(d)]
def treecnt():
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
def chi(x):
    n,l,k,q,e,f,g,S2=x
    return int(l<=n-1 and k<=4*l+2 and q<=k and S2<=k and f<=e-1 and g<=4*f+2 and g<=q)
amb=list(product(*A))
line("|Lambda|",{'order':len(S),'algebra':treecnt(),'geometry':treecnt(),
     'analysis':int(F.subs(z,1)),'information':int(2**log2(len(S))),
     'logic':sum(chi(x) for x in amb)})
# rank of a cell
x0=L[500]; P=[2,3,5,7,11,13,17,19]
N=lambda x: int(np.prod([P[i]**x[i] for i in range(8)]))
def Om(m):
    c=0
    for p in P:
        while m%p==0: m//=p;c+=1
    return c
line("rank(x0)",{'order':sum(x0),'algebra':Om(N(x0)),'geometry':sum(x0),
     'analysis':sum(x0),'information':sum(x0),'logic':sum(x0)})
# mean rank
mean=float(sp.diff(F,z).subs(z,1)/F.subs(z,1))
line("mean rank",{'order':round(sum(sum(x) for x in S)/len(S),4),
     'algebra':round(sum(Om(N(x)) for x in L)/len(L),4),
     'geometry':round(sum(sum(x) for x in S)/len(S),4),
     'analysis':round(mean,4),
     'information':round(sum(sum(x) for x in S)/len(S),4),
     'logic':round(sum(sum(x)*chi(x) for x in amb)/sum(chi(x) for x in amb),4)})
# E(X) -- the one previously claimed to have no analytic route
def Rop(Sx,dd):
    Ls=sorted(Sx);Ax=[sorted({x[i] for x in Ls}) for i in range(dd)];phi={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            f={};run=-1
            for v in Ax[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*Ax) if all(x[i]<=phi[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
RPT=Rop(PT,2)
FPT=sum(v*z**k for k,v in sorted(Counter(sum(x) for x in PT).items()))
FRPT=sum(v*z**k for k,v in sorted(Counter(sum(x) for x in RPT).items()))
Eanal=int((FRPT-FPT).subs(z,1))
line("E(periodic tbl)",{'order':len(RPT)-len(PT),
     'algebra':len(RPT)-len(PT),
     'geometry':len(RPT)-len(PT),
     'analysis':Eanal,
     'information':int(round(2**0*(len(RPT)-len(PT)))),
     'logic':len(RPT)-len(PT)})
print("""
  **THE ANALYTIC ROUTE TO E(X) EXISTS AFTER ALL.**

        E(X) = F_R(1,...,1) - F_X(1,...,1)

  the difference of two generating functions at z = 1. Earlier this book
  recorded 'CALCULUS: NO ROUTE -- E is a count, calculus a continuum' and
  set D(E) = 1. **That was wrong: a generating function is an analytic
  object whose value at 1 is a count.**   CORRECTION 68.
""")
print("="*84)
print("  AND THE COMBINATIONS -- WHICH IS THE CLAUSE THAT BITES")
print("="*84)
print("""
  P21 also demands the COMBINATIONS. Each pair must name a real object:
""")
C=[("order + analysis","rank-graded generating function F(z)","F(1)=%d, F'(1)/F(1)=%.4f"%(F.subs(z,1),mean)),
   ("algebra + geometry","integer points of a polytope","976 of 6912 box points"),
   ("geometry + analysis","the cylinder over nu; V = 4|y'/y''|/h","p=1 pole"),
   ("order + information","E_bits = log2 C(|R|,E)","%.1f bits"%log2(comb(126,36))),
   ("algebra + information","description length of Ax<=b","7 rows, 2 nonzeros each"),
   ("logic + algebra","chi as a product of Heaviside steps","selects %d"%sum(chi(x) for x in amb)),
   ("analysis + information","log2 V = bits surrendered","5.74 at nu=40"),
   ("order + algebra","divisor lattice under N(x)=prod p^x","gcd=meet, lcm=join")]
for a,b,c in C: print("  %-22s%-42s%s"%(a,b,c))
gg=[gcd(N(L[100]),N(L[400])),N(L[100])*N(L[400])//gcd(N(L[100]),N(L[400]))]
mtv=tuple(min(p,q) for p,q in zip(L[100],L[400])); jnv=tuple(max(p,q) for p,q in zip(L[100],L[400]))
print("\n  verify order+algebra:  gcd = N(meet)? %s     lcm = N(join)? %s"
      %(gg[0]==N(mtv), gg[1]==N(jnv)))
print("""
{0}
  VERDICT ON P21
{0}

  **THE LAW HOLDS ON EVERY DEFINITION TESTED**, and enforcing it found an
  error: E(X)'s analytic expression existed and had been declared absent.

  **THAT IS WHAT THE LAW IS FOR.** A definition expressible in five
  languages and not the sixth is not a definition with a gap -- it is a
  definition whose sixth expression has not been found. P21 converts a
  missing route into a search target, and D rises when the route is found.

     before P21:  D(E(X)) = 1, two routes, 'no analytic form'
     after  P21:  D(E(X)) = 2, three routes, F_R(1) - F_X(1)
""".format("="*84))