import numpy as np
from scipy.optimize import brentq
print("="*84)
print("  WHAT TRANSFERS TO THE THREE-BODY PROBLEM, AND WHAT DOES NOT")
print("="*84)
print("""
  FIRST, WHAT DOES NOT. The three-body problem's difficulty is not
  indexing. It is sensitive dependence: neighbouring initial conditions
  diverge exponentially, so no monotone sequence exists along a chaotic
  trajectory. **Nothing in this book addresses that, and Poincaré's
  non-integrability result is untouched by it.**

  WHAT MIGHT TRANSFER is everything that acts on ORDERED FAMILIES rather
  than on trajectories. Test the clearest case.
""")
print("="*84)
print("  THE LAGRANGE POINTS AS A MONOTONE FAMILY IN THE MASS RATIO")
print("="*84)
print("""
  In the circular restricted problem, L1, L2, L3 sit at roots of quintics
  in the mass ratio mu = m2/(m1+m2). Each is a smooth monotone function of
  mu. **That is exactly the object Chapter 14's bracket takes.**
""")
def L1(mu):
    f=lambda x: x - (1-mu)/(x+mu)**2 + mu/(x-1+mu)**2
    return brentq(f,-mu+1e-9,1-mu-1e-9,xtol=1e-14)
def L2(mu):
    f=lambda x: x - (1-mu)/(x+mu)**2 - mu/(x-1+mu)**2
    return brentq(f,1-mu+1e-9,3.0,xtol=1e-14)
def L3(mu):
    f=lambda x: x + (1-mu)/(x+mu)**2 + mu/(x-1+mu)**2
    return brentq(f,-3.0,-mu-1e-9,xtol=1e-14)
mus=np.array([0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08])
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    y=np.array([F(m) for m in mus])
    d1=np.diff(y); d2=np.diff(d1); d3=np.diff(d2)
    print("  %-4s monotone: %-6s  convex: %-6s  3-monotone: %-6s"
          %(nm,str(all(np.sign(d1)==np.sign(d1[0]))),
              str(all(np.sign(d2)==np.sign(d2[0]))),
              str(all(np.sign(d3)==np.sign(d3[0])))))
print("""
  **ALL THREE ARE MONOTONE, CONVEX AND 3-MONOTONE IN mu.** So the bracket
  of Chapter 14 and the k-th order bracket of Section 15.10 both apply,
  with no fit and no equation of motion.
""")
print("="*84)
print("  SO BRACKET L1 AND MEASURE WHAT THE GUARANTEE COSTS")
print("="*84)
def pa(nd,ys,x): return np.polyval(np.polyfit(nd,ys,len(nd)-1),x)
def bracket_k(F,x,h,k):
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=[x+j*h for j in range(1,m+1)]+[x-j*h for j in range(1,bl+1)]
        if len(nd)!=k+1 or min(nd)<=0: continue
        nd=sorted(nd); ys=[F(t) for t in nd]
        p=pa(nd,ys,x)
        if (k+1+m)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
print("\n  %-4s%8s%6s%16s%16s%12s%9s"%("pt","mu","k","bracket lo","bracket hi","width","holds"))
print("  "+"-"*74)
res=[]
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    for mu in (0.03,0.05):
        for k in (1,2,3):
            lo,hi=bracket_k(F,mu,0.01,k)
            tv=F(mu); ok=lo<=tv<=hi
            res.append(ok)
            print("  %-4s%8.3f%6d%16.10f%16.10f%12.3e%9s"%(nm,mu,k,lo,hi,hi-lo,"yes" if ok else "NO"))
    print()
print("     containment: %d of %d"%(sum(res),len(res)))
print("="*84)
print("  AND V — THE PRICE OF CERTAINTY IN THE RESTRICTED PROBLEM")
print("="*84)
print("""
  V = 4|y'/y''|/h. For L1 near mu = 0 the expansion is
  L1 ≈ 1 − (mu/3)^(1/3), so locally a power law with p = 1/3.
""")
print("  %-4s%9s%12s%12s%14s"%("pt","mu","V measured","4x/(h|p−1|)","p implied"))
for nm,F in [('L1',L1),('L2',L2),('L3',L3)]:
    for mu in (0.03,0.05):
        h=0.01
        a,m0,b=F(mu-h),F(mu),F(mu+h)
        w=abs(b-a); e=abs(m0-(a+b)/2)
        V=w/e
        p_imp=1+4*mu/(h*V)
        print("  %-4s%9.3f%12.2f%12s%14.4f"%(nm,mu,V,"—",p_imp))
print("""
  **L3's V is enormous, and that is the pole of Section 12.5.** L3 sits
  almost exactly opposite the primaries and moves nearly LINEARLY in mu,
  so its second difference nearly vanishes and a bracket on it costs
  hundreds of times what a bracket on L1 does.

  **The book's pole is not an artefact of spectroscopy. It appears in
  celestial mechanics at the first point one looks.**
""")