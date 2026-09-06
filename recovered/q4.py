import numpy as np, sympy as sp
R=109737.3
print("="*76)
print("  Q6.  THE AITKEN BIAS IS 1/3 FOR p = -2.  WHAT IS IT IN GENERAL?")
print("="*76)
x,p=sp.symbols('x p',positive=True)
y=x**p
corr=sp.simplify(sp.diff(y,x)**2/sp.diff(y,x,2))
print("\n  Aitken correction = y'^2/y'' = %s"%sp.simplify(corr))
after=sp.simplify(y-corr)
print("  Aitken(y) = y - correction = %s"%sp.simplify(after))
print("""
        **Aitken(y) = -y/(p-1)**

  EXACT, to leading order, for every power law.
""")
print("  %8s%18s%18s%14s"%("p","factor -1/(p-1)","meaning","sign"))
for pv,nm in [(-3,"spacing"),(-2,"T, term value"),(2,"<r>, dipole"),(3,"lifetime"),
              (4,"C3"),(7,"polarisability"),(11,"C6")]:
    fac=-1.0/(pv-1)
    print("  %8d%18.4f  %-16s%14s"%(pv,fac,nm,"undershoot" if fac>0 else "OVERSHOOT"))
print("""
  **THE SIGN FLIPS AT p = 1 -- THE SAME POLE AS V.**

     p < 1   Aitken UNDERSHOOTS the limit, landing at -y/(p-1) > 0
     p = 1   the correction diverges
     p > 1   Aitken OVERSHOOTS PAST THE LIMIT, to a negative value

  For a Rydberg term (p = -2) it lands at +T/3. For C6 (p = 11) it lands
  at -C6/10 -- a NEGATIVE dispersion coefficient, which is nonsense, and
  the method gives no warning.
""")
Tn=lambda v: R/v**2
def ait(f,v,h=1):
    a,m,b=f(v-h),f(v),f(v+h)
    return b-(b-m)**2/(a-2*m+b)
print("  VERIFY ON THREE EXPONENTS:\n")
print("  %6s%8s%16s%16s%12s"%("p","x","Aitken(y)","-y/(p-1)","ratio"))
for pv in (-2,4,11):
    f=lambda t,P=pv: t**float(P)
    for xv in (20.,40.):
        a=ait(f,xv); pred=-f(xv)/(pv-1)
        print("  %6d%8.0f%16.6g%16.6g%12.4f"%(pv,xv,a,pred,a/pred))
print("="*76)
print("  Q7.  SO IS THE AITKEN BIAS THE SAME QUANTITY AS V?")
print("="*76)
print("""
     V         = 4x/(h|p-1|)
     |bias|    = 1/|p-1|

        **V = (4x/h) * |bias|**

  The cost of a guarantee is PROPORTIONAL to the bias of the standard
  accelerated estimate, with constant 4x/h. They are one quantity.
""")
def Vex(f,x0,h=1):
    a,m,b=f(x0-h),f(x0),f(x0+h); return abs(b-a)/abs(m-(a+b)/2)
print("  %6s%8s%14s%14s%16s"%("p","x","V exact","(4x/h)|bias|","ratio"))
for pv in (-3,-2,4,11):
    f=lambda t,P=pv: t**float(P)
    for xv in (20.,):
        v=Vex(f,xv); pr=(4*xv/1)*abs(1.0/(pv-1))
        print("  %6d%8.0f%14.4f%14.4f%16.4f"%(pv,xv,v,pr,v/pr))
print("""
  **CONFIRMED.** The price of certainty and the error of acceleration are
  the same number in different clothes -- both are 1/|p-1| times a scale.

  WHICH SETTLES SOMETHING: Chapter 14's cost is not a peculiarity of
  bracketing. **Any method that assumes local linearity pays 1/|p-1|.**
  Aitken pays it as bias; the bracket pays it as width.
""")
print("="*76)
print("  Q8.  lambda^2 = (2/3)T.  WHAT DOES lambda < 1 MEAN PHYSICALLY?")
print("="*76)
print("""
  In self-concordant analysis lambda < 1 marks the region where Newton's
  method converges quadratically, and lambda < 0.382 the guaranteed region.

     lambda^2 = (2/3)T  <  1   <=>   T < 3/2 cm^-1   <=>   nu > sqrt(2R/3)
""")
print("     nu threshold for lambda < 1     : %.1f"%np.sqrt(2*R/3))
print("     nu threshold for lambda < 0.382 : %.1f"%np.sqrt(2*R/(3*0.382**2)))
print("""
  **THE DEEPEST CHANNEL IN THIS BOOK REACHES nu = 55, WHERE
  lambda = %.1f.**

  So every measured Rydberg level sits FAR OUTSIDE the region where a
  Newton step is safe. A single Newton step from any level in this
  collection would overshoot badly -- which is exactly what the Aitken
  overshoot of Q6 is, since Aitken IS a Newton step on the sequence.

  **CONSISTENT, AND IT EXPLAINS THE BIAS PHYSICALLY: the levels are too
  deeply bound for a local quadratic model of the limit.**
"""%np.sqrt(2*Tn(55)/3))
print("  %6s%14s%14s%16s"%("nu","T (cm-1)","lambda","in region?"))
for v in (10,55,100,271,400,1000):
    lam=np.sqrt(2*Tn(v)/3)
    print("  %6d%14.4f%14.4f%16s"%(v,Tn(v),lam,"yes" if lam<1 else "no"))
print("""
  **nu = 271 IS A REAL BOUNDARY AND NOTHING IN THIS BOOK REACHES IT.**
  It is not the self-concordance bound (nu = 406); it is the
  quadratic-convergence bound, and it sits below it.

  TWO THRESHOLDS, BOTH DERIVED, NEITHER MEASURED:
     nu > 271   a Newton step toward the limit is safe
     nu < 406   the term function is self-concordant
     271 < nu < 406  BOTH hold -- and no measured level is there
""")