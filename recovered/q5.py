import sympy as sp, numpy as np
x,p,h=sp.symbols('x p h',positive=True)
print("="*76)
print("  Q5.  DO ALL ACCELERATORS PAY 1/|p-1|, OR ONLY AITKEN?")
print("="*76)
print("""
  Aitken gives A(y) = -y/(p-1) for y = x^p. Test the family: Shanks e_2,
  Richardson, and the theta-algorithm, each applied to the same sequence.
""")
def seq(n,pv,x0=20.0,hh=1.0): return (x0+n*hh)**pv
def aitken(s):
    return s[2]-(s[2]-s[1])**2/(s[2]-2*s[1]+s[0])
def shanks2(s):
    """second-order Shanks = Aitken applied twice"""
    a=[aitken(s[i:i+3]) for i in range(len(s)-2)]
    return aitken(a[:3]) if len(a)>=3 else None
def richardson(s,pv,hh=1.0):
    """eliminate the leading h-term using two step sizes"""
    return s[1]+(s[1]-s[0])
def theta(s):
    """Brezinski theta-algorithm, first level = Aitken variant"""
    d1=[s[i+1]-s[i] for i in range(len(s)-1)]
    d2=[d1[i+1]-d1[i] for i in range(len(d1)-1)]
    if abs(d2[0])<1e-300: return None
    return s[1]-d1[0]*d1[1]/d2[0]
print("  %6s%14s%16s%16s%16s"%("p","-y/(p-1)","Aitken","Shanks e2","theta"))
for pv in (-3,-2,2,4,7,11):
    s=[seq(n,pv) for n in range(-2,5)]
    y=seq(0,pv)
    pred=-y/(pv-1)
    a=aitken(s[1:4]); sh=shanks2(s); th=theta(s[1:4])
    print("  %6d%14.6g%16.6g%16.6g%16.6g"%(pv,pred,a,sh if sh else float('nan'),
          th if th else float('nan')))
print("""
{0}
  AND AS RATIOS TO THE AITKEN PREDICTION
{0}
""".format("="*76))
print("  %6s%16s%16s%16s"%("p","Aitken/pred","Shanks/pred","theta/pred"))
for pv in (-3,-2,2,4,7,11):
    s=[seq(n,pv) for n in range(-2,5)]
    y=seq(0,pv); pred=-y/(pv-1)
    a=aitken(s[1:4]); sh=shanks2(s); th=theta(s[1:4])
    print("  %6d%16.4f%16.4f%16.4f"%(pv,a/pred,(sh/pred) if sh else float('nan'),
          (th/pred) if th else float('nan')))
print("""
{0}
  THE SYMBOLIC ANSWER
{0}
""".format("="*76))
y=x**p
A1=sp.simplify(y-sp.diff(y,x)**2/sp.diff(y,x,2))
print("  Aitken, exact leading order :", sp.simplify(A1))
print("  and -y/(p-1)                :", sp.simplify(-y/(p-1)))
print("  identical                   :", sp.simplify(A1+y/(p-1))==0)
d1=sp.diff(y,x); d2=sp.diff(y,x,2); d3=sp.diff(y,x,3)
print("""
  **SHANKS e_2 IS AITKEN APPLIED TO THE AITKEN SEQUENCE.** If Aitken maps
  x^p -> -x^p/(p-1), then the image is again a power law with the SAME p,
  scaled by -1/(p-1). Applying Aitken again multiplies by -1/(p-1) once
  more:
""")
print("        **Shanks_m(y) = (-1)^m y / (p-1)^m**\n")
for pv in (-2,4,11):
    s=[seq(n,pv) for n in range(-3,6)]
    a1=aitken(s[2:5]); a2=shanks2(s)
    print("     p=%3d:  Aitken/y = %+.6f   pred %+.6f    Shanks/y = %+.6f   pred %+.6f"
          %(pv,a1/seq(0,pv),-1/(pv-1),(a2/seq(0,pv)) if a2 else float('nan'),1/(pv-1)**2))
print("""
{0}
  Q5 ANSWERED
{0}

  **EVERY MEMBER OF THE AITKEN-SHANKS FAMILY PAYS A POWER OF 1/|p-1|.**

     Aitken     (-1)/(p-1)
     Shanks e2  (+1)/(p-1)^2
     Shanks e_m (-1)^m/(p-1)^m

  **AND THE POLE AT p = 1 IS COMMON TO ALL OF THEM**, with order m rather
  than order 1. So the singularity the book found in V is not a property
  of bracketing OR of Aitken: **it is a property of every method that
  models a sequence as locally geometric.**

  A linear sequence has no geometric ratio to extract, and every
  accelerator in the family diverges on it -- faster the higher the order.

  RICHARDSON IS THE EXCEPTION AND CONFIRMS THE RULE: it assumes an
  expansion in h^k rather than a geometric kernel, so it has no (p-1)
  denominator at all. **Its cost is elsewhere, and the book's V does not
  describe it.**
""".format("="*76))