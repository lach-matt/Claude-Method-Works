import numpy as np
from itertools import product
print("="*86)
print("  Q1.  Λ HAS A CAPACITY BOUND.  DOES CELESTIAL MECHANICS?")
print("="*86)
print("""
  Λ's one physical constraint is a CAPACITY: g <= 2(2f+1), a subshell holds
  only so many. I said gravity has no such bound. **Test it.**

  A planet holds satellites only inside its Hill sphere:
        r_H = a (m / 3M)^(1/3)
  and a moon must have a_moon < r_H. **That is a monotone bound of exactly
  Section 9.4's form: one variable capped by a function of another.**
""")
Msun=1.989e30
PL={'Earth':(1.000,5.972e24),'Mars':(1.524,6.417e23),'Jupiter':(5.203,1.898e27),
    'Saturn':(9.537,5.683e26),'Uranus':(19.191,8.681e25),'Neptune':(30.07,1.024e26)}
MOONS={'Earth':1,'Mars':2,'Jupiter':95,'Saturn':146,'Uranus':28,'Neptune':16}
print("  %-9s%10s%14s%12s%10s"%("planet","a (AU)","r_H (AU)","r_H/a","moons"))
print("  "+"-"*56)
rows=[]
for p,(a,m) in PL.items():
    rH=a*(m/(3*Msun))**(1/3)
    rows.append((p,a,rH,rH/a,MOONS[p]))
    print("  %-9s%10.3f%14.5f%12.5f%10d"%(p,a,rH,rH/a,MOONS[p]))
rH=np.array([r[2] for r in rows]); nm=np.array([r[4] for r in rows],float)
print("\n     corr(Hill radius, moon count)          %+.3f"%np.corrcoef(rH,nm)[0,1])
print("     corr(log Hill radius, log moon count)  %+.3f"%np.corrcoef(np.log(rH),np.log(nm))[0,1])
print("""
  **THE CAPACITY BOUND EXISTS AND IT IS MONOTONE.** Not exclusion — nothing
  forbids two moons from sharing an orbit — but a CAP, and the cap is a
  function of one coordinate exactly as 2(2f+1) is a function of f.

  **So Section 6.5 is wrong to call its one coupling 'the only bound with
  no gravitational analogue'.** The analogue is the Hill sphere. What has
  no analogue is EXCLUSION — the cap being reached by indistinguishable
  fermions — not the cap itself.  CORRECTION 112.
""")
print("="*86)
print("  Q2.  IS THE POLE THE SIGNATURE OF CLOSED-FORM SOLVABILITY?")
print("="*86)
print("""
  L4 and L5 sit on the pole exactly, and they are the two Lagrange points
  with a CLOSED-FORM solution: (1/2 − mu, ±sqrt(3)/2). L1, L2, L3 are roots
  of quintics with no closed form, and their V is finite.

  **Conjecture: V = infinity iff the family has an exact linear closed
  form in the parameter.** Test it on cases where the answer is known.
""")
from scipy.optimize import brentq
def V_of(F,x,h=1e-3):
    a,m,b=F(x-h),F(x),F(x+h)
    e=abs(m-(a+b)/2)
    return abs(b-a)/e if e>1e-300 else float('inf')
CASES=[
 ("L4 x-coord, exact",lambda mu:0.5-mu,"closed form, LINEAR"),
 ("L4 y-coord, exact",lambda mu:np.sqrt(3)/2,"closed form, CONSTANT"),
 ("L1, quintic root",lambda mu:brentq(lambda x:x-(1-mu)/(x+mu)**2+mu/(x-1+mu)**2,-mu+1e-9,1-mu-1e-9,xtol=1e-15),"no closed form"),
 ("L3, quintic root",lambda mu:brentq(lambda x:x+(1-mu)/(x+mu)**2+mu/(x-1+mu)**2,-3,-mu-1e-9,xtol=1e-15),"no closed form"),
 ("circular orbit period, a^3/2",lambda a:a**1.5,"closed form, NONLINEAR"),
 ("escape velocity, r^-1/2",lambda r:r**-0.5,"closed form, NONLINEAR"),
 ("2-body energy, -1/2a",lambda a:-0.5/a,"closed form, NONLINEAR"),
]
print("  %-30s%16s%24s"%("family","V","solvability"))
print("  "+"-"*72)
for nm2,F,tag in CASES:
    x=0.04 if 'L' in nm2 else 2.0
    v=V_of(F,x)
    print("  %-30s%16s%24s"%(nm2,("%.4g"%v) if np.isfinite(v) else "INFINITE",tag))
print("""
  **THE CONJECTURE IS FALSE, AND USEFULLY SO.** Escape velocity and the
  two-body energy have closed forms and FINITE V. Kepler's third law has a
  closed form and finite V.

  **V detects LINEARITY, not solvability.** The pole says the family is
  exactly determined by two points — which is a statement about the SHAPE
  of the dependence, not about whether a formula exists.

  **And that is the sharper reading of Section 12.5:**

     V infinite  <=>  linear in the parameter  <=>  two points suffice
     V finite    <=>  curved  <=>  a bracket is needed and costs something

  L4 and L5 are on the pole because their coordinates are LINEAR in mu,
  and they happen also to have closed forms. **The two properties coincide
  there and are not the same property.**
""")
print("="*86)
print("  Q3.  SO WHAT IS THE BOOK'S POLE, STATED CORRECTLY?")
print("="*86)
print("""
     a family with V = infinity needs no bracket, because interpolation is
     EXACT

     a family with V large needs a bracket that is nearly worthless,
     because interpolation is nearly exact

     **the cost of a guarantee is high exactly where the guarantee is
     least needed**

  **That is not a defect of the method. It is the method reporting that
  the question has become easy.** Chapter 12.5 reads the pole as a warning;
  it is a dismissal.
""")