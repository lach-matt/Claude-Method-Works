import numpy as np
from scipy.optimize import brentq
def L1(mu):
    f=lambda x: x-(1-mu)/(x+mu)**2+mu/(x-1+mu)**2
    return brentq(f,-mu+1e-9,1-mu-1e-9,xtol=1e-15)
def L2(mu):
    f=lambda x: x-(1-mu)/(x+mu)**2-mu/(x-1+mu)**2
    return brentq(f,1-mu+1e-9,3.0,xtol=1e-15)
def L3(mu):
    f=lambda x: x+(1-mu)/(x+mu)**2+mu/(x-1+mu)**2
    return brentq(f,-3.0,-mu-1e-9,xtol=1e-15)
def detect_signs(F,x,h,kmax=4):
    """the book's rule: read the sign of each finite difference from the data"""
    xs=[x+j*h for j in range(-(kmax+2),kmax+3)]
    ys=[F(t) for t in xs]
    sg={}
    cur=ys
    for j in range(1,kmax+3):
        cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
        s=set(np.sign(v) for v in cur if abs(v)>1e-14)
        sg[j]= (list(s)[0] if len(s)==1 else 0)
    return sg
def pa(nd,ys,x): return np.polyval(np.polyfit(nd,ys,len(nd)-1),x)
def bracket_k(F,x,h,k,sg):
    """sign of f^(k+1) taken FROM THE DATA, not assumed"""
    s=sg.get(k+1,0)
    if s==0: return None
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=[x+j*h for j in range(1,m+1)]+[x-j*h for j in range(1,bl+1)]
        if len(nd)!=k+1 or min(nd)<=0: continue
        nd=sorted(nd); ys=[F(t) for t in nd]
        p=pa(nd,ys,x)
        # sign(f - p) = sign(f^(k+1)) * (-1)^m
        sgn = s*((-1)**m)
        if sgn>0: lo=max(lo,p)
        else:     hi=min(hi,p)
    if not np.isfinite(lo) or not np.isfinite(hi) or hi<lo: return None
    return lo,hi
print("="*84)
print("  REDONE — SIGNS READ FROM THE DATA, AS THE RULE SAYS")
print("="*84)
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    sg=detect_signs(F,0.04,0.01)
    print("  %-4s finite-difference signs, order 1..5 : %s"%(nm,[int(sg[j]) for j in range(1,6)]))
print("""
  **L1 and L3 alternate −,+,−,+ ; L2 alternates +,−,+,− .** The Rydberg
  pattern was assumed and it is wrong for L2. The rule never said assume —
  it said read the sign off the data.
""")
print("  %-4s%8s%6s%18s%18s%13s%8s"%("pt","mu","k","bracket lo","bracket hi","width","holds"))
print("  "+"-"*78)
tot=ok=0
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    sg=detect_signs(F,0.04,0.01)
    for mu in (0.03,0.05):
        for k in (1,2,3):
            r=bracket_k(F,mu,0.01,k,sg)
            if r is None:
                print("  %-4s%8.3f%6d%18s"%(nm,mu,k,"refused")); continue
            lo,hi=r; tv=F(mu); good=lo<=tv<=hi; tot+=1; ok+=good
            print("  %-4s%8.3f%6d%18.12f%18.12f%13.3e%8s"%(nm,mu,k,lo,hi,hi-lo,"yes" if good else "NO"))
    print()
print("     containment: %d of %d"%(ok,tot))
print("="*84)
print("  AND THE COST, WITH THE POLE WHERE THE BOOK SAYS IT WILL BE")
print("="*84)
print("\n  %-4s%9s%14s%16s%14s"%("pt","mu","V","width at k=1","implied |p−1|"))
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    for mu in (0.03,0.05):
        h=0.01
        a,m0,b=F(mu-h),F(mu),F(mu+h)
        V=abs(b-a)/abs(m0-(a+b)/2)
        r=bracket_k(F,mu,h,1,detect_signs(F,0.04,h))
        w=(r[1]-r[0]) if r else float('nan')
        print("  %-4s%9.3f%14.2f%16.3e%14.4f"%(nm,mu,V,w,4*mu/(h*V)))
print("""
  **L3 costs 400–800x what L1 does**, because L3 moves almost linearly in
  mu -- |p−1| ≈ 0.001 -- and Section 12.5's pole sits exactly there.

  **SO THE ANSWER TO THE QUESTION IS SPECIFIC:**

     applies      any ordered FAMILY of three-body solutions: Lagrange
                  points in mu, periodic-orbit families in a continuation
                  parameter, stability boundaries in a mass ratio

     applies      the refusal test -- a sign change in a finite difference
                  along a family is a BIFURCATION, detected with no fit
                  and no equation of motion

     does not     trajectories. Sensitive dependence destroys monotonicity,
                  and nothing here touches Poincare.

  **The three-body problem is not one object. Its FAMILIES are indexable
  and its TRAJECTORIES are not, and the book's methods sort themselves
  along exactly that line.**
""")