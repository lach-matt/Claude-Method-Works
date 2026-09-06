import numpy as np
from scipy.optimize import brentq
from itertools import product
print("="*84)
print("  RUN IT THROUGH THE INDEX — WHAT IS ADMITTED AND NOT PRESENT?")
print("="*84)
print("""
  The collection was L1, L2, L3. **There are five Lagrange points.** The
  index's first question is always the same: what does the structure admit
  that the collection does not hold?
""")
def L1(mu):
    f=lambda x: x-(1-mu)/(x+mu)**2+mu/(x-1+mu)**2
    return brentq(f,-mu+1e-9,1-mu-1e-9,xtol=1e-15)
def L2(mu):
    f=lambda x: x-(1-mu)/(x+mu)**2-mu/(x-1+mu)**2
    return brentq(f,1-mu+1e-9,3.0,xtol=1e-15)
def L3(mu):
    f=lambda x: x+(1-mu)/(x+mu)**2+mu/(x-1+mu)**2
    return brentq(f,-3.0,-mu-1e-9,xtol=1e-15)
L4x=lambda mu: 0.5-mu
L4y=lambda mu: np.sqrt(3)/2
print("  %-6s%-14s%16s%16s%14s"%("point","type","x(mu)","2nd difference","V"))
print("  "+"-"*68)
h=0.01
for nm,F,ty in [('L1',L1,'collinear'),('L2',L2,'collinear'),('L3',L3,'collinear'),
                ('L4x',L4x,'equilateral'),('L4y',L4y,'equilateral')]:
    mu=0.04
    a,m0,b=F(mu-h),F(mu),F(mu+h)
    d2=a-2*m0+b
    V=abs(b-a)/abs(m0-(a+b)/2) if abs(d2)>1e-300 else float('inf')
    print("  %-6s%-14s%16.10f%16.3e%14s"%(nm,ty,m0,d2,("%.1f"%V) if np.isfinite(V) else "INFINITE"))
print("""
  **L4 AND L5 SIT EXACTLY ON THE POLE.** Their coordinates are
  (1/2 − mu, ±sqrt(3)/2): the first is exactly linear in mu and the second
  is constant. **The second difference is not small. It is zero.**
""")
print("="*84)
print("  AND THAT REFRAMES THE POLE")
print("="*84)
print("""
  Section 12.5 treats p = 1 as the place a bracket becomes worthless — the
  cost diverges, the guarantee buys nothing. **True, and incomplete.**

     a function with vanishing second difference is EXACTLY determined by
     two points

  **So at the pole a bracket is not merely worthless. It is unnecessary.**
  Interpolation is exact there, with error zero, and V = w/0 = infinity is
  the correct answer to a question nobody needs to ask.
""")
print("  verify: linear interpolation error at L4x, over a wide span\n")
for span in (0.01,0.1,0.3):
    a,m0,b=L4x(0.4-span),L4x(0.4),L4x(0.4+span)
    print("     span %.2f :  |interp − true| = %.3e"%(span,abs(m0-(a+b)/2)))
print("""
  **EXACT AT EVERY SPAN.** The pole is the signature of exactness, and the
  book has been reading it as the signature of failure.
""")
print("="*84)
print("  THE INDEX, BUILT — AND ITS DEFECT")
print("="*84)
print("""
  Coordinates: (point, geometry, |p−1| class, highest deductive order
  available). Order each so larger means more structure.
""")
def clsp(v):
    if v==0: return 0
    if v<0.01: return 1
    if v<0.6: return 2
    return 3
DATA=[]
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    mu=0.04; a,m0,b=F(mu-h),F(mu),F(mu+h)
    V=abs(b-a)/abs(m0-(a+b)/2)
    DATA.append((nm,1,clsp(4*mu/(h*V)),3))
DATA.append(('L4',0,clsp(0),0))
DATA.append(('L5',0,clsp(0),0))
print("  %-6s%10s%12s%14s"%("point","collinear","|p−1| class","max order"))
for nm,g,c,k in DATA: print("  %-6s%10d%12d%14d"%(nm,g,c,k))
X={(g,c,k) for _,g,c,k in DATA}
A=[sorted({t[i] for t in X}) for i in range(3)]
def Rop(S,d=3):
    Ls=sorted(S);Ax=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in Ax[j]:
                cc=[x[i] for x in Ls if x[j]<=v];run=max(run,max(cc) if cc else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*Ax) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
R=Rop(X)
print("\n     cells present : %d"%len(X))
print("     R(X)          : %d"%len(R))
print("     **E(X)        : %d**"%(len(R)-len(X)))
if len(R)>len(X):
    print("\n     admitted and absent:")
    for c in sorted(R-X): print("        (collinear=%d, |p−1| class=%d, max order=%d)"%c)
print("""
{0}
  WHAT WE DID NOT SEE
{0}

  1. **L4 and L5 were never tested**, and they are the two points that sit
     exactly on the pole. Three of five is not a collection; it is the
     three that were easy.

  2. **The pole means exactness, not failure.** A vanishing second
     difference makes linear interpolation exact, so the infinite cost is
     the price of a guarantee nobody needs. Section 12.5 states half of
     this.

  3. **L3 is the interesting case and the book has no name for it.**
     |p−1| = 0.0007 is neither the pole nor a normal channel: it is a
     near-degenerate family where a bracket is nearly worthless and
     interpolation is nearly exact. **The same regime as He II's delta = 0
     edge in Chapter 16**, reached from a different subject.

  4. **E(X) = %d.** The index admits combinations the five points do not
     realise, and each is a question: is there a three-body family that is
     collinear yet exactly linear, or equilateral yet curved?
""".format("="*84)%(len(R)-len(X)))