# Checks for Part VI.A (sympy): separatrix rates (3.2), bracket (c), escape function (5.1).
import sympy as sp
r,xi,C,mu=sp.symbols('r xi C mu',positive=True); z0=sp.Symbol('z0')
f=1-mu/r**2; G=-1/f+f*xi**2+C/r**2; u=1-2*mu/r**2
Cs=sp.solve(sp.Eq(G,0),C)[0]
H=lambda F: z0*(sp.diff(G,xi)*sp.diff(F,r)-sp.diff(G,r)*sp.diff(F,xi))
n1=2*z0*(r**4+xi*(r**2-mu)*(r**2-2*mu))/(r**3*(r**2-mu)); n2=2*z0*(r**4-xi*(r**2-mu)*(r**2-2*mu))/(r**3*(r**2-mu))
assert sp.simplify(H(f*xi-u).subs(C,Cs)+n1*(f*xi-u))==0
assert sp.simplify(H(f*xi+u).subs(C,Cs)-n2*(f*xi+u))==0
pb=sp.diff(f*xi-u,xi)*sp.diff(f*xi+u,r)-sp.diff(f*xi-u,r)*sp.diff(f*xi+u,xi)
assert sp.simplify(pb.subs({xi:0,r:sp.sqrt(2*mu)})-sp.sqrt(2/mu))==0
F=(r**2-2*mu)*xi
HF=(sp.diff(G,xi)*sp.diff(F,r)-sp.diff(G,r)*sp.diff(F,xi)).subs(C,Cs)
assert sp.simplify(HF-2*r*(xi**2*(r**2-mu)**2+(r**2-2*mu)**2)/(r**2-mu)**2)==0
assert sp.simplify(F-r**2/(4*f)*((f*xi+u)**2-(f*xi-u)**2))==0
print('dyn5 checks pass')
