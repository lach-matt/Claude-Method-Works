#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key vonlaue-1911-annphys (as used by tolman.py).

Checks, in flat 3-space (gravity stripped, as the tree uses it):
  C1  the product-rule identity behind Wang (arXiv:1206.5618) eq. (20):
        d_l(Theta^{l mu} X^i) = (d_l Theta^{l mu}) X^i + Theta^{i mu}
      symbolically for an arbitrary static tensor field.
  C2  eq. (20) on a ball for a divergence-free, NON-spherical, compactly
      supported stress built from a stress function phi:
        T^{ij} = delta_ij Lap(phi) - d_i d_j phi   (d_i T^{ij} = 0 identically)
      int_{ball R} T^{ii} d^3x  ==  R^3 oint n_i n_j T^{ij} dOmega
                               ==  4 pi R^3 <T^{rr}>(R)
      for R inside the support (nonzero) and R outside (zero).
  C3  the VANISHING form needs the surface term to vanish (compact support /
      Wang's boundary condition).  Counterexample: a bounded device (charged
      conducting shell of radius a, held by a surface tension) whose COMPLETE
      stress (field + shell) is divergence-free everywhere, yet
        int_{ball R} T^{ii} = -Q^2/(8 pi eps0 R)  != 0   for every R > a,
      equal to the surface term 4 pi R^3 p_r(R); -> 0 only as R -> infinity.
      Contrast: +Q/-Q concentric shells (field confined) give exactly 0 for R > b.
  C4  the field-only tensor of the shell (no wall stress) has int T^{ii} != 0
      even over all space (Wang secs. 4-5): 'complete' is load-bearing.
  C3h the finite-ball deviation obeys Pinto-Avelino (2502.10427) |int_ball p| <= m_out.
  C5  z3: the tree's L1 logic -- identity + (p_r = 0 at the cut) => m = 0 --
      and its drift: p_r free => m = 0 not forced.
"""
import sympy as sp

ok = True
def check(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + label)

x, y, z = sp.symbols('x y z', real=True)
X = [x, y, z]

# ---------------------------------------------------------------- C1
Th = [[sp.Function(f'T{l}{m}')(x, y, z) for m in range(4)] for l in range(3)]
allzero = True
for mu in range(4):
    for i in range(3):
        lhs = sum(sp.diff(Th[l][mu] * X[i], X[l]) for l in range(3))
        rhs = sum(sp.diff(Th[l][mu], X[l]) for l in range(3)) * X[i] + Th[i][mu]
        allzero &= sp.simplify(lhs - rhs) == 0
check("C1 product-rule identity under eq.(20), all i, mu (symbolic)", allzero)

# ---------------------------------------------------------------- C2
r, th, ph, R = sp.symbols('r theta phi R', positive=True)
bump = (1 - x**2 - y**2 - z**2)**4           # C^3 at r = 1, zero outside
phi = bump * (1 + x*z + sp.Rational(1, 3)*y**2)   # non-spherical
lap = sum(sp.diff(phi, v, 2) for v in X)
T = [[sp.expand((lap if i == j else 0) - sp.diff(phi, X[i], X[j])) for j in range(3)] for i in range(3)]
div = [sp.simplify(sum(sp.diff(T[i][j], X[i]) for i in range(3))) for j in range(3)]
check("C2a T^{ij} = delta Lap(phi) - dd phi is divergence-free identically", all(d == 0 for d in div))
sph = {x: r*sp.sin(th)*sp.cos(ph), y: r*sp.sin(th)*sp.sin(ph), z: r*sp.cos(th)}
trace = sp.expand((T[0][0] + T[1][1] + T[2][2]).subs(sph))
vol = sp.integrate(sp.integrate(sp.integrate(trace * r**2 * sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi)), (r, 0, R))
vol = sp.simplify(vol)
n = [sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)]
Trr = sp.expand(sum(n[i]*n[j]*T[i][j] for i in range(3) for j in range(3)).subs(sph).subs(r, R))
surf = sp.simplify(R**3 * sp.integrate(sp.integrate(Trr * sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi)))
check("C2b int_{ball R} T^ii == R^3 oint T^rr dOmega for 0<R<1 (sympy residual 0)", sp.simplify(vol - surf) == 0)
Rhalf = sp.Rational(1, 2)
check("C2c ... and it is NONZERO inside the support (R=1/2): value %s" % vol.subs(R, Rhalf),
      vol.subs(R, Rhalf) != 0)
check("C2d ... and ZERO on the support boundary R=1 (compact support => vanishing form)",
      sp.simplify(vol.subs(R, 1)) == 0)

# ---------------------------------------------------------------- C3 / C4
Q, a, b, e0 = sp.symbols('Q a b epsilon_0', positive=True)
E = Q / (4*sp.pi*e0*r**2)
# static radial field: p_r = T^{rr} = -e0 E^2/2 (tension), p_t = +e0 E^2/2; trace = e0 E^2/2
p_r_field = -e0*E**2/2
trace_field = e0*E**2/2
# conservation outside the shell: p_r' + 2(p_r - p_t)/r = 0
check("C3a radial Maxwell stress is conserved for r > a: p_r' + 2(p_r-p_t)/r = 0",
      sp.simplify(sp.diff(p_r_field, r) + 2*(p_r_field - (-p_r_field))/r) == 0)
sigma = Q/(4*sp.pi*a**2)
tau = a*sigma**2/(4*e0)          # surface tension balancing outward pressure sigma^2/(2 e0): 2 tau/a
check("C3b shell equilibrium 2 tau / a == sigma^2/(2 eps0)", sp.simplify(2*tau/a - sigma**2/(2*e0)) == 0)
wall_trace_integral = -2*tau * 4*sp.pi*a**2      # T^thth = T^phph = -tau delta(r-a), p_r = 0 in the wall
field_part = sp.integrate(trace_field*4*sp.pi*r**2, (r, a, R))
total = sp.simplify(field_part + wall_trace_integral)
surface = sp.simplify(4*sp.pi*R**3*p_r_field.subs(r, R))
check("C3c complete (field+shell) int_{ball R>a} T^ii == 4 pi R^3 p_r(R) == %s" % total,
      sp.simplify(total - surface) == 0)
check("C3d ... which is NONZERO for every finite R > a (bounded device, non-compact T)",
      sp.simplify(total + Q**2/(8*sp.pi*e0*R)) == 0)
check("C3e ... and -> 0 only in the limit R -> infinity (all-space von Laue condition)",
      sp.limit(total, R, sp.oo) == 0)
# contrast: +Q at a, -Q at b > a, field confined to a<r<b; tensions on both shells
sig_a = Q/(4*sp.pi*a**2); sig_b = Q/(4*sp.pi*b**2)
# inner shell: field only outside -> outward pull sigma^2/(2e0) -> tension tau_a
# outer shell: field only inside -> inward pull sigma^2/(2e0) -> COMPRESSION (tau_b < 0)
tau_a = a*sig_a**2/(4*e0); tau_b = -b*sig_b**2/(4*e0)
tot2 = sp.simplify(sp.integrate(trace_field*4*sp.pi*r**2, (r, a, b)) - 2*tau_a*4*sp.pi*a**2 - 2*tau_b*4*sp.pi*b**2)
check("C3f contrast: +Q/-Q shells (field confined, compact T) give int T^ii = 0 for R > b", tot2 == 0)
m_out = sp.integrate(e0*E**2/2*4*sp.pi*r**2, (r, R, sp.oo))   # field energy outside the ball
check("C3h Pinto-Avelino arXiv:2502.10427 eq.(42)-(43) bound |int_ball p| <= m_out holds, ratio = %s (=1/3, w=1/3 for EM)"
      % sp.simplify(sp.Abs(total/3)/m_out), sp.simplify(sp.Abs(total/3)/m_out) == sp.Rational(1, 3))
check("C4  field-only tensor (walls omitted) over all space: int T^ii = Q^2/(8 pi eps0 a) != 0",
      sp.simplify(sp.integrate(trace_field*4*sp.pi*r**2, (r, a, sp.oo)) - Q**2/(8*sp.pi*e0*a)) == 0)
# ---------------------------------------------------------------- C5
try:
    import z3
    F, Rc, m, pr = z3.Reals('F Rc m pr')
    CUT = z3.And(F > 0, Rc > 0, m == F*Rc**3*pr)
    s = z3.Solver(); s.add(CUT, pr == 0, m != 0)
    check("C5a z3: identity + p_r=0 at cut => m = 0 (negation unsat)", s.check() == z3.unsat)
    s = z3.Solver(); s.add(CUT, m != 0)
    check("C5b z3: p_r at cut free => m = 0 NOT forced (sat)", s.check() == z3.sat)
    s = z3.Solver(); s.add(CUT, pr == 0)
    check("C5c z3 vacuity guard: premise set with p_r = 0 is satisfiable", s.check() == z3.sat)
except ImportError:
    print("SKIP C5 (z3 not installed)")

print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
