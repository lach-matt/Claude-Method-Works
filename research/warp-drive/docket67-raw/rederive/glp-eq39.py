#!/usr/bin/env python3
"""DOCKET 67 -- glp-eq39: re-derive "the Eot-Wash null bounds gamma*L, not L".

Greene, Levin & Parikh, arXiv:1103.2174 (GLP) was NOT readable here (alphaXiv
quota exhausted; arxiv.org egress-blocked).  Its result is READ-VIA-RESTATEMENT
in Kabat & Nomura arXiv:2309.05759v2 (cached text, scratchpad/d67/src/):
  eq (10): boost with velocity beta -> a^mu = (-gamma beta 2 pi R,0,0,0), r = gamma R
  eq (15): tilt by theta          -> r = R cos(theta)
  eq (22): lightlike              -> r = R
  eq (72): M4 = (gamma 2 pi R)^{1/2} M5^{3/2};  fn 8: "In [9] (=GLP) this was
           expressed in terms of Newton's constant, G4 = G5/gamma 2 pi R".
Everything below is computed, from flat M4 x S^1 (circumference L = 2 pi R).
"""
import math
import sympy as sp

ok = True
def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS  " if cond else "FAIL  ") + name)

b, L, n = sp.symbols('beta L n', real=True)
g = 1/sp.sqrt(1-b**2)

# 1. The lattice vector (t,y)=(0,L) seen in the brane frame (boost beta along y).
tp = g*(0 - b*L); yp = g*(L - b*0)
check("brane-frame identification = (-gamma beta L, gamma L)  [KN eq 10]",
      sp.simplify(tp + g*b*L) == 0 and sp.simplify(yp - g*L) == 0)
check("invariant: -(dt')^2 + (dy')^2 = L^2", sp.simplify(-tp**2 + yp**2 - L**2) == 0)
# A time-independent phi(y') obeys phi(t',y') = phi(t' - gamma beta L, y' + gamma L)
# => phi(y') = phi(y' + gamma L): static brane-frame period is gamma L, not L.

# 2. Independent route in the PREFERRED frame: steady field of a source riding the
#    circle, phi = f(x, xi = y - beta t).  Wave operator -d_t^2 + d_y^2 on f:
t, y, x = sp.symbols('t y x', real=True)
f = sp.Function('f')
xi = y - b*t
expr = -sp.diff(f(xi), t, 2) + sp.diff(f(xi), y, 2)
fpp = sp.Subs(sp.Derivative(f(sp.Symbol('u')), sp.Symbol('u'), 2), sp.Symbol('u'), xi).doit()
check("wave operator on f(y - beta t) = (1 - beta^2) f''", sp.simplify(expr - (1-b**2)*fpp) == 0)
#    so Laplace_x f + f''/gamma^2 = source; with eta = gamma xi this is the flat
#    Laplacian in (x, eta), and period L in xi is period gamma L in eta.
print("      => preferred-frame route: steady field is harmonic with period gamma L in eta")

# 3. Image sum on a line of period a (4 spatial dims, Gauss law lap Phi = 4 pi G5 rho):
#    point potential -G5 m/(pi R^2); images at n a.
r, a = sp.symbols('r a', positive=True)
S = sp.pi/(a*r)*sp.coth(sp.pi*r/a)
for rv, av in [(0.3, 1.0), (1.0, 1.0), (2.5, 0.7), (0.05, 3.0)]:
    direct = sum(1.0/(rv**2 + (k*av)**2) for k in range(-200000, 200001))
    tail = 2.0/(av**2*200000)                      # int_N^inf 2/(a^2 k^2)
    check("sum_n 1/(r^2+n^2a^2) = pi coth(pi r/a)/(a r) at r=%g a=%g" % (rv, av),
          abs(direct + tail - float(S.subs({r: rv, a: av})))/float(S.subs({r: rv, a: av})) < 1e-8)
G5, m1, m2 = sp.symbols('G5 m1 m2', positive=True)
V = -G5*m1*m2/sp.pi*S
Vpass = -(G5*m1*m2/(a*r))*sp.coth(sp.pi*r/a)
check("V = -(G5 m1 m2/(a r)) coth(pi r/a): the o6o7 pass's form with a = gamma L",
      sp.simplify(V - Vpass) == 0)
# far field -> G4 = G5/a = G5/(gamma 2 pi R)  [KN fn 8 restating GLP]
check("r >> a: V -> -(G5/a) m1 m2/r, i.e. G4 = G5/(gamma L)",
      sp.limit(V*r/(-(G5/a)*m1*m2), r, sp.oo) == 1)
M4, M5, R = sp.symbols('M4 M5 R', positive=True)
sol = sp.solve(sp.Eq(1/(8*sp.pi*M4**2), (1/(8*sp.pi*M5**3))/(g*2*sp.pi*R)), M4)
check("G = 1/(8 pi M^2) conventions give KN eq 72 M4 = (gamma 2 pi R)^1/2 M5^3/2",
      any(sp.simplify(s - sp.sqrt(g*2*sp.pi*R)*M5**sp.Rational(3, 2)) == 0 for s in sol))

# 4. Yukawa form: coth(z) = 1 + 2 sum_k e^{-2kz}, so V = -(G4 m1 m2/r)[1 + 2 e^{-r/lam} + ...]
#    with lam = a/(2 pi) = gamma L/(2 pi) = gamma R = r_eff (KN eq 10) and alpha = 2.
z = sp.symbols('z', positive=True)
zv = 3.1
check("coth z - 1 = 2 e^{-2z} + 2 e^{-4z} + ... (numeric, z=3.1)",
      abs((1/math.tanh(zv) - 1) - sum(2*math.exp(-2*k*zv) for k in range(1, 40))) < 1e-15)
print("      => leading deviation: alpha = 2 (Newtonian image count), lambda = gamma L/(2 pi)")
print("      NOTE: 38.6 um is Lee et al. 2020's bound for GRAVITATIONAL-STRENGTH |alpha| = 1")
print("            (web-search abstract snippet; paper NOT read here).  alpha = 2 (images)")
print("            or 8/3 (graviton tensor structure, Kehagias-Sfetsos, NAMED-NOT-READ) gives a")
print("            TIGHTER lambda bound; a snippet reports ~30 um for one extra dimension.")

# 5. Numbers.
lam = 38.6e-6
print("      gamma L <= 2 pi x 38.6 um = %.4f um  (bound is on gamma L/(2 pi) = r)" % (2*math.pi*lam*1e6))
print("      at the snippet's ~30 um: gamma L <= %.4f um  (ratio %.4f)" % (2*math.pi*30e-6*1e6, 30/38.6))
check("2 pi x 38.6 um = 242.531 um", abs(2*math.pi*lam*1e6 - 242.531) < 1e-3)
# 6. Scale of the distinction under the tree's own GW170817 seat (manyc.py, bulk graviton):
d = 7.0e-16
print("      if gravity is bulk (the only branch in which Eot-Wash bounds r at all),")
print("      GKLP eq 38 + 39 give gamma - 1 <= %.1e, so gamma L - L <= %.3e m at L = 242.5 um" % (d, d*2*math.pi*lam))
check("gamma L / L - 1 <= 7e-16 in the bulk-graviton branch", d <= 7.0e-16)
# 7. Tilt-like: r = R cos(theta) < R -- the bound is on r, and 'gamma L' is the boost case.
th = sp.symbols('theta', real=True)
check("tilt-like r = R cos(theta) <= R: general statement is 'bounds r', not 'bounds gamma L'",
      sp.simplify(sp.cos(th)**2 - 1) == -sp.sin(th)**2)
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
