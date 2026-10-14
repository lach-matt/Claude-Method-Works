"""C10 (companion, fast): tensor structure of KN eq. 76 for boost-like b = (-beta,0,0,0),
signature (+,-,-,-).  In the preferred frame the spatial part is isotropic, so a
Michelson-Morley-type (anisotropic c_JK) bound sees it only through the lab's velocity v
relative to that frame.  Computes the lab-frame spatial anisotropy exactly."""
import sympy as sp, sys
be, v = sp.symbols("beta v", positive=True)
eta = sp.diag(1, -1, -1, -1)
b = sp.Matrix([-be, 0, 0, 0])
bb = (b.T * eta * b)[0]
S = b * b.T - eta * bb / 4                      # b^mu b^nu - eta^{mu nu} b^2/4 (eta^{-1} = eta)
ok1 = sp.simplify(bb - be**2) == 0
spat = S[1:, 1:]
ok2 = sp.simplify(spat - sp.eye(3) * be**2 / 4) == sp.zeros(3)
g = 1 / sp.sqrt(1 - v**2)
L = sp.Matrix([[g, -g*v, 0, 0], [-g*v, g, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Sp = sp.simplify(L * S * L.T)
sp3 = Sp[1:, 1:]
aniso = sp.simplify(sp3 - sp.eye(3) * sp3.trace() / 3)
lead = sp.simplify(aniso[0, 0])
print("b^2 =", sp.simplify(bb), "; T00 =", S[0, 0], "; spatial =", spat.tolist())
print("lab-frame traceless spatial xx component =", lead, "=", sp.series(lead, v, 0, 4).removeO())
num = lead.subs({be: 1, v: sp.Rational(37, 100000)*sp.Rational(1000, 299792458)*1000})
ok3 = sp.simplify(lead - sp.Rational(2, 3) * be**2 * g**2 * v**2) == 0
print("at v = 370 km/s: aniso_xx / T00(beta=1) =", sp.N(lead.subs({be: 1, v: sp.Rational(370000, 299792458)}) / sp.Rational(3, 4)))
print("PASS" if ok1 and ok2 and ok3 else "FAIL", "C10 b^2=beta^2; preferred-frame spatial part = (beta^2/4) delta_ij (isotropic);",
      "lab anisotropy = (2/3) beta^2 gamma_v^2 v^2")
sys.exit(0 if ok1 and ok2 and ok3 else 1)
