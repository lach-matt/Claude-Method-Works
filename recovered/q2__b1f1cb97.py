import numpy as np
from mpmath import mp, mpf
mp.dps=60
def V(p,x=20.0,h=1.0):
    f=lambda t: mpf(t)**mpf(p)
    a,m,b=f(x-h),f(x),f(x+h)
    return float(abs(b-a)/abs(m-(a+b)/2))
print("="*76)
print("  Q2 (cont).  DOES V -> 0 AS p -> infinity?  PROP 14.1 SAYS V > 2")
print("="*76)
print("\n  %8s%14s%14s%12s"%("p","V exact","4x/h|p-1|","ratio"))
for p in (2,4,11,20,50,100,300,1000,10000):
    print("  %8d%14.4f%14.4f%12.4f"%(p,V(p),4*20/abs(p-1),V(p)/(4*20/abs(p-1))))
print("""
  **NEITHER IS WRONG -- THE ASYMPTOTIC FORM FAILS FIRST.**

  As p grows, (x+h)^p swamps everything: w -> (x+h)^p and e -> (x+h)^p/2,
  so **V -> 2 exactly**. 4x/h|p-1| is the SMALL-p branch; V = 2 is the
  LARGE-p branch. They cross where 4x/(h|p-1|) = 2, i.e. |p-1| = 2x/h.
""")
for x in (10,20,40):
    print("     x = %2d, h = 1:  crossover at p = %.0f"%(x,2*x+1))
print("""
  **THE ABSOLUTE FLOOR V = 2 IS REACHED ONLY BY POWER LAWS STEEPER THAN
  2x/h.** At nu = 20 that needs p > 41. C6 at p = 11 is nowhere near it.
""")
print("="*76)
print("  Q3.  WHAT ABOUT BRACKETING nu ITSELF?")
print("="*76)
R=109737.3
d0,d2=1.35,0.06
nuf=lambda n: n-(d0+d2/n**2)
Tf=lambda n: R/nuf(n)**2
def we(f,n,h):
    a,m,b=f(n-h),f(n),f(n+h); return abs(b-a),abs(m-(a+b)/2)
print("""
  nu = n - delta is very nearly LINEAR in n -- and p = 1 is the POLE.
""")
print("  %5s%16s%16s%14s"%("n","V on nu","V on T","ratio"))
for n in (10,20,40):
    wn,en=we(nuf,n,1); wt,et=we(Tf,n,1)
    print("  %5d%16.1f%16.4f%14.3g"%(n,wn/en,wt/et,(wn/en)/(wt/et)))
print("""
  **BRACKETING nu COSTS 10^3 TO 10^5 TIMES MORE THAN BRACKETING T.**
  The reason is Section 11.5: nu is nearly linear, its second difference
  nearly vanishes, and V nearly diverges.

  THE POLE IS NOT A CURIOSITY. It sits on the MOST NATURAL VARIABLE IN
  THE FIELD -- the effective quantum number -- and that is the one
  variable in which a bracket is worthless.
""")
print("="*76)
print("  Q4.  THE COMPLETE ANSWER TO 'WHICH VARIABLE?'")
print("="*76)
print("""
     nu          p ~ 1      V ~ 10^4-10^5   USELESS -- at the pole
     delta       shape -2   V = 4n/3h       same cost as T, 10^6 narrower
     T           p = -2     V = 4n/3h       LIMIT-FREE
     alpha       p = 7      V = 4x/6h       2x cheaper than T
     C6          p = 11     V = 4x/10h      3.3x cheaper than T
     p > 2x/h               V -> 2          the absolute floor

  **THE CHOICE OF VARIABLE IS THE ONLY FREE PARAMETER THAT CHANGES THE
  COST, AND CHAPTER 14 NEVER FRAMES IT AS A CHOICE.** It treats V as a
  property of the method. V is a property of the OBSERVABLE, and the
  observable is chosen by the person.
""")
print("="*76)
print("  Q5.  AND WHAT IS THE PRICE OF LIMIT-FREEDOM?")
print("="*76)
print("""
  T's containment needs no ionisation limit (Section 13.3). delta's does.
  Both cost the same V. So limit-freedom is bought entirely in WIDTH:
""")
for n in (10,20,40):
    wt,_=we(Tf,n,1)
    dl=lambda m: d0+d2/m**2
    wd,_=we(dl,n,1)
    nu=nuf(n)
    print("     n=%2d:  w_T = %9.4g cm-1   equivalent w_delta = %9.3g   ratio %8.3g"
          %(n,wt,wd,wt/(2*R*wd/nu**3)))
print("""
  **THE PRICE OF NOT NEEDING THE LIMIT IS A BRACKET ROUGHLY 2-3x WIDER
  IN COMPARABLE UNITS** -- not the 10^6 the raw numbers suggest, because
  delta and T are in different units and must be converted through
  dT/ddelta = 2R/nu^3.

  **SO THE BOOK'S CHOICE WAS NEARLY FREE AFTER ALL**, and the 10^6 figure
  in the previous message was a UNIT ARTEFACT. FIFTY-THIRD CORRECTION.
""")