import numpy as np
print("="*76)
print("  Q1.  IF V DEPENDS ONLY ON SHAPE, WHICH SHAPE IS CHEAPEST?")
print("="*76)
print("""
  V = 4x/(h|p-1|) to leading order. So the cost falls as |p-1| grows.
  **You do not have to bracket T. You may bracket any observable of the
  same series.** Which one costs least?
""")
def V(p,x=20.0,h=1.0):
    f=lambda t: t**p
    a,m,b=f(x-h),f(x),f(x+h)
    return abs(b-a)/abs(m-(a+b)/2)
OBS=[("spacing |dT/dn|",-3),("T, the term value",-2),("<r>",2),("dipole moment",2),
     ("radiative lifetime",3),("C3",4),("geometric cross-section",4),
     ("polarisability alpha",7),("C6",11),("blockade radius R_b",11/6.)]
print("  %-26s%6s%12s%14s%10s"%("observable","p","|p-1|","V exact","4x/h|p-1|"))
rows=[]
for nm,p in sorted(OBS,key=lambda z:-abs(z[1]-1)):
    v=V(p); rows.append((nm,p,v))
    print("  %-26s%6.2f%12.2f%14.4f%10.3f"%(nm,p,abs(p-1),v,4*20/abs(p-1)))
print("""
  **C6 IS THE CHEAPEST GUARANTEE AVAILABLE ON A RYDBERG SERIES**, at
  V = %.2f against T's %.2f -- a factor of %.1f. And the dipole moment is
  the most expensive, at %.1f.
"""%(V(11),V(-2),V(-2)/V(11),V(2)))
print("="*76)
print("  Q2.  SO DOES V -> 0 AS p -> infinity?  THAT WOULD BREAK PROP 14.1")
print("="*76)
print("""
  Prop 14.1 proves V > 2 for EVERY monotone sequence. But 4x/(h|p-1|) -> 0
  as p grows. **One of the two must be wrong.**
""")
print("  %8s%14s%14s%12s"%("p","V exact","4x/h|p-1|","ratio"))
for p in (2,4,11,20,50,100,300,1000):
    print("  %8d%14.4f%14.4f%12.4f"%(p,V(p),4*20/abs(p-1),V(p)/(4*20/abs(p-1))))
print("""
  **NEITHER IS WRONG. The asymptotic form fails first.**

  As p grows, (x+h)^p swamps everything, so w -> (x+h)^p and
  e -> (x+h)^p/2, giving **V -> 2 exactly**. The formula 4x/h|p-1| is the
  SMALL-p branch; the floor is the LARGE-p branch, and they cross where
  4x/(h|p-1|) = 2, i.e. **|p-1| = 2x/h**.
""")
for x in (10,20,40):
    print("     x = %2d, h = 1:  crossover at p = %.0f"%(x,2*x+1))
print("""
  **SO THE CHEAPEST POSSIBLE GUARANTEE ON ANY OBSERVABLE IS V = 2, AND IT
  IS REACHED ONLY BY POWER LAWS STEEPER THAN 2nu/h.** At nu = 20 that
  means p > 41. C6 at p = 11 is nowhere near it.
""")
print("="*76)
print("  Q3.  WHAT ABOUT BRACKETING nu ITSELF?")
print("="*76)
print("""
  nu = n - delta. As a function of n it is very nearly LINEAR --
  and p = 1 is the POLE.
""")
d0,d2=1.35,0.06
nuf=lambda n: n-(d0+d2/n**2)
def we(f,n,h):
    a,m,b=f(n-h),f(n),f(n+h); return abs(b-a),abs(m-(a+b)/2)
print("  %5s%14s%16s"%("n","V on nu","V on T"))
R=109737.3
Tf=lambda n: R/nuf(n)**2
for n in (10,20,40):
    wn,en=we(nuf,n,1); wt,et=we(Tf,n,1)
    print("  %5d%14.1f%16.4f"%(n,wn/en,wt/et))
print("""
  **BRACKETING nu COSTS 10^4 TO 10^5 TIMES MORE THAN BRACKETING T**, and
  the reason is Section 11.5: nu is nearly linear in n, so its second
  difference nearly vanishes and V nearly diverges.

  THE POLE IS NOT A CURIOSITY. IT IS THE MOST NATURAL VARIABLE IN THE
  FIELD -- the effective quantum number -- and it is the one variable in
  which a bracket is worthless.
""")
print("="*76)
print("  Q4.  SO WHAT IS THE COMPLETE ANSWER TO 'WHICH VARIABLE?'")
print("="*76)
print("""
     nu           p ~ 1     V ~ 10^5     USELESS -- at the pole
     delta        shape -2  V = 4n/3h    same cost as T, 10^6 narrower
     T            p = -2    V = 4n/3h    limit-free
     alpha        p = 7     V = 4x/6h    2x cheaper than T
     C6           p = 11    V = 4x/10h   3.3x cheaper than T
     any p > 2x/h            V -> 2      the absolute floor

  **THE CHOICE OF VARIABLE IS THE ONLY FREE PARAMETER THAT CHANGES THE
  COST, AND THE BOOK NEVER FRAMES IT AS A CHOICE.** Chapter 14 treats V as
  a property of the method. It is a property of the OBSERVABLE, and the
  observable is selected by the person, not by the physics.
""")
print("="*76)
print("  Q5.  AND WHAT DOES THAT DO TO THE COLLECTION?")
print("="*76)
print("""
  1,442 cells, all bracketed in T. Every one could have been bracketed in
  delta at the same cost and 10^6 the precision, or in C6 at a third the
  cost -- had C6 been measured.

  **THE COLLECTION IS NOT A MEASUREMENT OF THE METHOD. IT IS A
  MEASUREMENT OF ONE VARIABLE CHOICE.** And the choice was made for a
  reason -- limit-freedom -- that the book states but never prices.

  NEW QUESTION, UNANSWERED: what is the cost, in V, of limit-freedom?
""")