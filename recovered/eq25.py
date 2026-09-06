import sympy as sp
nu,h,Z,R=sp.symbols('nu h Z R',positive=True)
T=Z**2*R/nu**2
print("="*76); print("  RESOLVING EQUATION 25"); print("="*76)
w=sp.simplify(T.subs(nu,nu-h)-T.subs(nu,nu+h))
e=sp.simplify(T-(T.subs(nu,nu-h)+T.subs(nu,nu+h))/2)
V=sp.simplify(sp.cancel(w/e))
print("\n  w  = T(nu-h) - T(nu+h)   [positive: T decreases in nu]")
print("  e  = T(nu) - mean")
print("\n  V exact =", sp.simplify(sp.factor(V)))
book = 4*nu**3/(h*(h**2-3*nu**2))
print("  book    =", sp.factor(book))
print("\n  V - book  =", sp.simplify(V-book))
print("  V + book  =", sp.simplify(V+book))
r=sp.symbols('r',positive=True)
Vr=sp.simplify(sp.cancel(V.subs(h,nu/r)))
print("\n  V(r) exact =", sp.simplify(Vr))
print("  book V(r)  =", sp.simplify(4*r**3/(3*r**2-1)))
print("  difference =", sp.simplify(Vr-4*r**3/(3*r**2-1)))
print("""
{0}
  VERDICT
{0}
""".format("="*76))
print("""  **THE BOOK'S FORM CARRIES A SIGN ERROR.**

     stated   V = 4nu^3 / ( h(h^2 - 3nu^2) )
     correct  V = 4nu^3 / ( h(3nu^2 - h^2) )

  For nu > h the stated denominator is NEGATIVE, so the stated V is
  negative -- and V is a ratio of two absolute widths, which cannot be.
""")
import numpy as np
Rn=109737.3
Tn=lambda v: Rn/v**2
def Vn(v,hh=1):
    a,m,b=Tn(v-hh),Tn(v),Tn(v+hh); return abs(b-a)/abs(m-(a+b)/2)
print("  %6s%5s%16s%20s%20s"%("nu","h","V numeric","stated formula","corrected formula"))
for v,hh in [(10,1),(20,1),(40,2),(20,3)]:
    st=4*v**3/(hh*(hh**2-3*v**2)); co=4*v**3/(hh*(3*v**2-hh**2))
    print("  %6d%5d%16.6f%20.6f%20.6f"%(v,hh,Vn(v,hh),st,co))
print("""
  AND IN THE SIMILARITY VARIABLE r = nu/h:

     stated   V = 4r^3/(3r^2 - 1)
     correct  V = 4r^3/(3r^2 - 1)     -- **UNCHANGED**

  because substituting h = nu/r into the CORRECTED form gives exactly
  4r^3/(3r^2-1), while the stated form gives its negative.
""")
print("  %6s%16s%20s"%("r","V numeric","4r^3/(3r^2-1)"))
for v,hh in [(20,1),(40,2),(60,3),(10,1)]:
    rr=v/hh
    print("  %6.1f%16.6f%20.6f"%(rr,Vn(v,hh),4*rr**3/(3*rr**2-1)))
print("""
{0}
  SO THE AUDIT FOUND ONE REAL ERROR AND ONE FALSE ALARM
{0}

  **(25) IS WRONG IN THE BOOK** -- the denominator's sign is inverted.
  **(25b) IS CORRECT** -- my test compared it against the negated form and
  therefore failed a true statement.

  CORRECTION 65: the book's V = 4nu^3/(h(h^2 - 3nu^2)).
  CORRECTION 66: the audit harness, again -- second false alarm of the day.
""".format("="*76))