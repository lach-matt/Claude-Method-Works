import numpy as np
from fractions import Fraction

# ---------- Exact three-point V for a Rydberg triple starting at nu ----------
def V3(nu):
    d0 = 1/nu**2 - 1/(nu+1)**2
    d1 = 1/(nu+1)**2 - 1/(nu+2)**2
    return 2*(d0+d1)/abs(d0-d1)

def Vcell(nuc):          # V at a cell whose own effective qn is nuc
    return V3(nuc-1.0)

# check Prop 14.3 anchor
f0 = Fraction(3,4); f1 = Fraction(5,36)
print("exact V at nu=1 :", 2*(f0+f1)/abs(f0-f1), "=", float(2*(f0+f1)/abs(f0-f1)))

# ---------- asymptotic 4 nu/3 ----------
print("\nnu_cell   V_exact   4nu/3    ratio")
for nuc in [2,3,4,5,8,12,21,40,80]:
    print(f"{nuc:7.1f} {Vcell(nuc):9.4f} {4*nuc/3:8.4f} {Vcell(nuc)/(4*nuc/3):8.4f}")

# fit the offset:  V_exact - 4nu/3 -> ?
nus = np.arange(20,2000,1.0)
print("\nV_exact - 4nu/3 at nu = 20,100,1000,1999:",
      [round(float(Vcell(x)-4*x/3),4) for x in [20,100,1000,1999]])

# ---------- generic continuum check: V ~ 4|y'|/(h|y''|) ----------
def Vtriple(y0,y1,y2):
    d0=y1-y0; d1=y2-y1
    return 2*(d0+d1)/abs(d0-d1)
print("\ngeneric shapes, h=1, x=10 :  V_exact   4|y'|/|y''|")
shapes = {
 "x^-2"      : (lambda x: x**-2.0,  lambda x: -2*x**-3.0, lambda x: 6*x**-4.0),
 "exp(-x/5)" : (lambda x: np.exp(-x/5), lambda x: -np.exp(-x/5)/5, lambda x: np.exp(-x/5)/25),
 "log x"     : (lambda x: np.log(x), lambda x: 1/x, lambda x: -1/x**2),
 "x^1.5"     : (lambda x: x**1.5, lambda x: 1.5*x**0.5, lambda x: 0.75*x**-0.5),
 "sqrt x"    : (lambda x: np.sqrt(x), lambda x: 0.5*x**-0.5, lambda x: -0.25*x**-1.5),
}
for k,(y,yp,ypp) in shapes.items():
    x=10.0
    ve = Vtriple(y(x-1),y(x),y(x+1))
    va = 4*abs(yp(x))/abs(ypp(x))
    print(f"  {k:10s} {ve:9.3f} {va:9.3f}   rel.err {abs(ve-va)/ve:6.3%}")