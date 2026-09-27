import sympy as sp
x,y,z=sp.symbols('x y z',real=True)
r=sp.sqrt(x**2+y**2+z**2)
I=sp.I
# U^inf (Klinkhamer-Manton): U = (1/r) [[z, x+iy],[-x+iy, z]]
U=sp.Matrix([[z,x+I*y],[-x+I*y,z]])/r
Ud=U.H
chi=sp.Matrix([0,1])
for i,c in enumerate((x,y,z)):
    M=sp.simplify(Ud*U.diff(c))
    val=sp.simplify((chi.H*M*chi)[0])
    print('d_%s: chi^dag U^dag d U chi ='%c, sp.simplify(val))
print('U unitary:', sp.simplify(Ud*U))
