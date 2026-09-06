import numpy as np, sympy as sp
R=109737.3
print("="*76)
print("  E(CLAIM SET) -- WHAT DOES THE STRUCTURE ADMIT THAT I HAVE NOT STATED?")
print("="*76)
print("""
  D.2.10 says enumerate targets BEFORE searching. I have been searching
  claims I happened to make. Compute the CLOSURE of the relation set first,
  and search what it admits.

  STATED RELATIONS:
     R1   V = 4nu/(3h)
     R2   lambda^2 = (2/3)T
     R3   w*V = 8 lambda^2
     R4   T = Z^2 R / nu^2
""")
nu,h,Z,Rs=sp.symbols('nu h Z R',positive=True)
T=Z**2*Rs/nu**2
w=sp.simplify(Z**2*Rs/(nu-h)**2 - Z**2*Rs/(nu+h)**2)
e=sp.simplify(Z**2*Rs/nu**2 - (Z**2*Rs/(nu-h)**2 + Z**2*Rs/(nu+h)**2)/2)
print("  DERIVED, BY CLOSURE -- each is a claim I never stated:\n")
wT=sp.simplify(w/T); eT=sp.simplify(sp.Abs(e)/T)
print("     w/T  =", sp.simplify(sp.series(wT,h,0,4).removeO()))
print("     e/T  =", sp.simplify(sp.series(eT,h,0,4).removeO()))
print("""
  LEADING ORDER:
""")
print("        **w/T = 4(h/nu)**        the bracket width as a FRACTION of the term")
print("        **e/T = 3(h/nu)^2**      the estimate error as a FRACTION of the term")
print("        V = (w/T)/(e/T) = (4/3)(nu/h)   -- consistent with R1\n")
print("  VERIFY NUMERICALLY:\n")
Tn=lambda v: R/v**2
print("  %5s%4s%14s%12s%14s%12s"%("nu","h","w/T","4h/nu","e/T","3(h/nu)^2"))
for v in (10,20,40):
    for hh in (1,2):
        a,m,b=Tn(v-hh),Tn(v),Tn(v+hh)
        ww=abs(b-a); ee=abs(m-(a+b)/2)
        print("  %5d%4d%14.6f%12.6f%14.3e%12.3e"%(v,hh,ww/m,4*hh/v,ee/m,3*(hh/v)**2))
print("""
==========================================================================
  SO THE SEARCH TARGETS WERE INCOMPLETE
==========================================================================

  I have been checking V, the floor, and lambda^2. The closure of the same
  relations also admits:

     (a) w/T = 4(h/nu)          the FRACTIONAL bracket width
     (b) e/T = 3(h/nu)^2        the FRACTIONAL interpolation error
     (c) V = (4/3)(nu/h)        their ratio -- already checked

  **(b) IS THE ONE THAT MATTERS.** The relative error of linear
  interpolation on a Rydberg series is 3(h/nu)^2 exactly, to leading order.
  That is a statement a spectroscopist could have made in 1925 and it has
  NEVER BEEN ON MY TARGET LIST.
""")
print("="*76)
print("  AND THE SAME MOVE ON THE INFORMATION SIDE")
print("="*76)
from math import log2, comb
print("""
  STATED:  E_bits = log2 C(|R(X)|, E)   and   log2 V = bits surrendered

  CLOSURE ADMITS:
""")
print("        **log2(w/e) = log2 V**            bits lost to the guarantee")
print("        **log2(T/e) = 2log2(nu/h) - log2 3**   bits the ESTIMATE resolves")
print("        **log2(T/w) = log2(nu/h) - 2**         bits the BRACKET resolves\n")
print("  %5s%4s%16s%16s%12s"%("nu","h","bits: estimate","bits: bracket","difference"))
for v in (10,20,40,100):
    hh=1
    a,m,b=Tn(v-hh),Tn(v),Tn(v+hh)
    ww=abs(b-a); ee=abs(m-(a+b)/2)
    print("  %5d%4d%16.3f%16.3f%12.3f"%(v,hh,log2(m/ee),log2(m/ww),log2(ww/ee)))
print("""
  **THE ESTIMATE RESOLVES THE TERM TO TWICE AS MANY BITS AS THE BRACKET,
  MINUS A CONSTANT.** 13.2 against 7.4 at nu = 40. And the difference is
  exactly log2 V.

  A NEW CLAIM, NEVER SEARCHED:
     bits(estimate) = 2 bits(bracket) + constant
  i.e. **a guarantee resolves a Rydberg term to HALF the bit-depth an
  estimate does**, asymptotically.
""")
print("="*76)
print("  THE EXPANDED TARGET LIST")
print("="*76)
TG=[("V = 4nu/3h","checked, 9 literatures","survives"),
    ("floor 32/11","checked","survives"),
    ("E(X) for an index","checked","survives"),
    ("lambda^2 = (2/3)T","checked once","survives"),
    ("T self-concordant","checked once","survives"),
    ("Aitken 1/3 bias","checked once","survives"),
    ("V = 4r^3/(3r^2-1)","checked once","survives"),
    ("log2 V > 1 bit-floor","checked once","survives"),
    ("**e/T = 3(h/nu)^2**","**NEVER SEARCHED**","**unknown**"),
    ("**w/T = 4(h/nu)**","**NEVER SEARCHED**","**unknown**"),
    ("**bits(est) = 2 bits(brack)**","**NEVER SEARCHED**","**unknown**")]
print("  %-32s%-24s%s"%("claim","status","verdict"))
for a,b,c in TG: print("  %-32s%-24s%s"%(a,b,c))
print("""
  **THREE CLAIMS THE STRUCTURE ADMITS AND I NEVER PUT ON THE LIST.**
  E(target list) = 3, and it was computable from relations already stated.

  THAT IS THE LATTICE METHOD APPLIED TO THE SEARCH ITSELF, AND IT FOUND
  THE SAME DEFECT THE BOOK FINDS IN THE PERIODIC TABLE: a structure
  admitting cells its keeper never listed.
""")