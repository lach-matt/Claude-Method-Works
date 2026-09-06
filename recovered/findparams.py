import numpy as np
from scipy.optimize import brentq
def L1(mu):
    g=lambda z: z-(1-mu)/(z+mu)**2+mu/(z-1+mu)**2
    return brentq(g,-mu+1e-9,1-mu-1e-9,xtol=1e-14)
def L2(mu):
    g=lambda z: z-(1-mu)/(z+mu)**2-mu/(z-1+mu)**2
    return brentq(g,1-mu+1e-9,3,xtol=1e-13)
def L3(mu):
    g=lambda z: z+(1-mu)/(z+mu)**2+mu/(z-1+mu)**2
    return brentq(g,-2,-mu-1e-9,xtol=1e-13)
def V(f,x,h):
    a,m,c=f(x-h),f(x),f(x+h); e=abs(m-(a+c)/2)
    return abs(c-a)/e if e>1e-300 else float('inf')
print("="*84)
print("  RECOVERING THE PARAMETERS FOR THE BOOK'S V VALUES")
print("="*84)
print("\n  %10s%10s%14s%14s%14s"%("mu","h","V(L1)","V(L2)","V(L3)"))
print("  "+"-"*62)
best=None
for mu in [0.01,0.02,0.03,0.05,0.1,0.2,0.3]:
    for h in [0.001,0.005,0.01,0.02,0.05]:
        if mu-h<=0 or mu+h>=0.5: continue
        try:
            v1=V(L1,mu,h); v2=V(L2,mu,h); v3=V(L3,mu,h)
        except Exception: continue
        print("  %10.3f%10.3f%14.1f%14.1f%14.1f"%(mu,h,v1,v2,v3))
        if abs(v1-24.6)<1.0 and best is None: best=(mu,h,v1,v3)
print()
if best:
    print("     **V(L1) ≈ 24.6 at μ = %.3f, h = %.3f  ->  V(L3) = %.0f**"%best)
else:
    print("     no (μ,h) in this grid gives V(L1) ≈ 24.6")
print("""
  **Either way the book must state the evaluation point.** V is a local
  quantity — it depends on where and at what step it is measured — and a
  stated V with no (μ, h) is not a checkable claim.
""")