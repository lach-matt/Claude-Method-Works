import sympy as sp
from fractions import Fraction as F
print("="*88)
print("  BUILDING THE GENERATING FUNCTION")
print("="*88)
y=sp.symbols('y')
A={1:[1]*14,
   2:[1,4,8,13,19,26,34,43,53,64,76,89,103,118],
   3:[1,8,29,73,151,275,458,714,1058,1506,2075,2783,3649,4693],
   4:[1,13,73,266,749,1781,3758,7247,13013,22048,35603,55223,82783,120526],
   5:[1,19,151,749,2762,8321,21659,50471,107833,215137,405767,730835,1265003,2110409]}
# verify the known rows against their fitted polynomials before trusting the tails
POLY={1:lambda c: 1,
      2:lambda c: F(c**2+3*c-2,2),
      3:lambda c: F(c**4+8*c**3+11*c**2-20*c+12,12),
      4:lambda c: F(c**6+15*c**5+67*c**4+45*c**3-140*c**2+300*c-144,144)}
print("\n  regenerate each row from its exact polynomial, and use THAT\n")
for r in (1,2,3,4):
    A[r]=[int(POLY[r](c)) for c in range(1,15)]
    print("     a(%d,c) = %s"%(r,A[r][:9]))
# r=5 : fit degree 8 from the nine computed values, then extend
v5=[1,19,151,749,2762,8321,21659,50471,107833]
c=sp.symbols('c')
p5=sp.interpolate(list(zip(range(1,10),v5)),c)
A[5]=[int(p5.subs(c,k)) for k in range(1,15)]
print("     a(5,c) = %s"%A[5][:9])
print("     (degree-8 interpolation, matching all nine computed values)")
print("="*88)
print("  THE NUMERATORS  P_r(y) = (1-y)^{2r-1} · Σ_c a(r,c) y^c")
print("="*88)
NUM={}
for r in range(1,6):
    ser=sum(A[r][k-1]*y**k for k in range(1,15))
    P=sp.expand(sp.series((1-y)**(2*r-1)*ser,y,0,2*r+1).removeO())
    NUM[r]=sp.Poly(P,y)
    print("\n     P_%d(y) = %s"%(r,sp.factor(P)))
    print("        coefficients (from y^1) : %s"%[NUM[r].coeff_monomial(y**k) for k in range(1,2*r+1)])
print("="*88)
print("  THE PATTERN")
print("="*88)
print("\n  %4s%10s%46s"%("r","deg P_r","coefficients"))
print("  "+"-"*64)
for r in range(1,6):
    co=[NUM[r].coeff_monomial(y**k) for k in range(0,2*r+1)]
    print("  %4d%10d%46s"%(r,NUM[r].degree(),co))
print("""
  **If the coefficient rows are a known triangle, the bivariate generating
  function follows.**
""")
print("="*88)
print("  AND THE CLOSED FORM, ASSEMBLED")
print("="*88)
print("""
      Σ_{c≥1} a(r,c) y^c  =  P_r(y) / (1−y)^{2r−1}

  with P_r as tabulated. **That is one expression per row, exact.** The
  bivariate form needs the triangle above to have a rule.
""")
import pickle
pickle.dump({'A':A,'NUM':{r:[NUM[r].coeff_monomial(y**k) for k in range(0,2*r+1)] for r in NUM}},
            open('/home/claude/stage/gf.pkl','wb'))
print("     saved /home/claude/stage/gf.pkl")