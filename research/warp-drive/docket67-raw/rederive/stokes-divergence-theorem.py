#!/usr/bin/env python3
"""DOCKET 67 -- audit rederivation: the divergence (Gauss-Ostrogradsky / 'Stokes')
theorem underlying tolman.py's Laue step (tolman.py:129-139, 937-939; family F
LAUE at 2196-2198).  Reads nothing under research/ or the corpus; writes nothing.

Checks
  D1  product rule under Wang eq.(20): d_l(T^{lj} x^i) = (d_l T^{lj}) x^i + T^{ij}
  D2  classical theorem, smooth NON-spherical divergence-free T on a ball:
      int_B T^ii dV == 4 pi R^3 <T^rr>(R)   (sympy residual 0)
  D3  tree's F5 class: constant anisotropic stress, the Laue residual is 0
  D4  tree's W3 (p_r = -2 + 10 r^{-5/2}): NOT C^1 at the centre, yet the
      identity holds -- inner flux -> 0.  'smooth' is sufficient, not necessary.
  D5  tree's independence_witness (p_r = A/r^3, p_t = -A/2r^3): divergence-free
      pointwise on the punctured ball (Cartesian residual 0), int_B T^ii = 0, but
      4 pi R^3 <T^rr> = 4 pi A.  The theorem on the SHELL B_R \\ B_eps is exact;
      the discrepancy is the inner flux; the distributional divergence at the
      origin is nonzero (test-field pairing = -4 pi A).  The ball form FAILS
      because its hypothesis fails -- a counterexample to the tree's unguarded
      wording, not to the theorem.
  D6  Whitney's example as READ in Chen-Torres 2005.10949 Example 2:
      F = y/|y|^2 on (0,1)^2: div F = 0 inside, outward flux = pi/2.
  D7  interface hypothesis: two-pressure ball, pointwise-divergence-free on each
      side; the ball identity fails by 4 pi a^3 (p1 - p2) and is restored
      exactly by a Laplace surface tension sigma = a (p1 - p2)/2 (distributional
      divergence-free total tensor).
  D8  z3: family F's LAUE conjunct (sum I_ii == F R^3 Trr) EXCLUDES the
      independence witness (unsat), and a LAUE with the centre term C admits it
      (sat) -- the regular-interior hypothesis is baked into LAUE.
"""
import sys
import sympy as sp

FAIL = []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAIL.append(label)


x, y, z = sp.symbols("x y z", real=True)
X = (x, y, z)
r, R, th, ph, eps, A, a = sp.symbols("r R theta phi epsilon A a", positive=True)

# ---------------------------------------------------------------- D1
T = [[sp.Function(f"T{i}{j}")(x, y, z) for j in range(3)] for i in range(3)]
ok = True
for i in range(3):
    for j in range(3):
        lhs = sum(sp.diff(T[l][j] * X[i], X[l]) for l in range(3))
        rhs = sum(sp.diff(T[l][j], X[l]) for l in range(3)) * X[i] + T[i][j]
        ok &= sp.simplify(lhs - rhs) == 0
check("D1  d_l(T^{lj} x^i) = (d_l T^{lj}) x^i + T^{ij}  (all i,j; arbitrary T)", ok)

# ------------------------------------------------ helpers on a ball
sph = {x: r * sp.sin(th) * sp.cos(ph), y: r * sp.sin(th) * sp.sin(ph), z: r * sp.cos(th)}
nvec = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]


def ball_volume_trace(Tm, Rr):
    tr = sp.expand(sum(Tm[i][i] for i in range(3)).subs(sph))
    return sp.integrate(sp.integrate(sp.integrate(tr * r**2 * sp.sin(th), (ph, 0, 2 * sp.pi)),
                                     (th, 0, sp.pi)), (r, 0, Rr))


def surface_term(Tm, Rr):
    # oint dS_l T^{lj} x^j over |x| = Rr  =  Rr^3 oint n_l n_j T^{lj} dOmega
    Trr = sp.expand(sum(nvec[l] * nvec[j] * Tm[l][j] for l in range(3) for j in range(3)).subs(sph))
    return sp.integrate(sp.integrate((Trr * sp.sin(th)).subs(r, Rr), (ph, 0, 2 * sp.pi)),
                        (th, 0, sp.pi)) * Rr**3


# ---------------------------------------------------------------- D2
phi = x**4 + 3 * x * y * z**2 + y**2 * z + 2 * x**2 * y**2 - z**3 * x + x * y
Tm = [[(sp.KroneckerDelta(i, j) * sum(sp.diff(phi, v, 2) for v in X) - sp.diff(phi, X[i], X[j]))
       for j in range(3)] for i in range(3)]
divT = [sp.simplify(sum(sp.diff(Tm[l][j], X[l]) for l in range(3))) for j in range(3)]
check("D2a smooth non-spherical T = delta Lap(phi) - dd phi is divergence-free", all(d == 0 for d in divT))
aniso = sp.simplify(Tm[0][0] - Tm[1][1]) != 0 or sp.simplify(Tm[0][1]) != 0
check("D2b ... and is genuinely anisotropic / non-spherical", aniso)
vol = sp.simplify(ball_volume_trace(Tm, R))
sur = sp.simplify(surface_term(Tm, R))
print("      int_B T^ii =", vol, "   surface =", sur)
check("D2c int_B T^ii == 4 pi R^3 <T^rr>(R)  (residual 0)", sp.simplify(vol - sur) == 0)
check("D2d ... and it is nonzero for this T (the identity is not 0 = 0)", sp.simplify(vol) != 0)

# ---------------------------------------------------------------- D3
pt_, pz_ = sp.symbols("p_t p_z", real=True)
Tc = [[pt_, 0, 0], [0, pt_, 0], [0, 0, pz_]]
vol3 = sp.simplify(ball_volume_trace(Tc, R))
sur3 = sp.simplify(surface_term(Tc, R))
check("D3  constant plate stress: Laue residual 0; <T^rr> = (2 p_t + p_z)/3",
      sp.simplify(vol3 - sur3) == 0 and sp.simplify(sur3 / (4 * sp.pi * R**3) - (2 * pt_ + pz_) / 3) == 0)
# F6 numbers: p_t=-5, p_z=+1 -> <T^rr> = -3
check("D3b F6 witness p_t=-5, p_z=1 gives <T^rr> = -3",
      sp.simplify((sur3 / (4 * sp.pi * R**3)).subs({pt_: -5, pz_: 1})) == -3)


# --------------------------------------- radial (spherical) sources helper
def radial_checks(pr, ptt):
    cons = sp.simplify(sp.diff(pr, r) + 2 * (pr - ptt) / r)
    trace = sp.simplify(pr + 2 * ptt)          # T^ii (spatial trace)
    return cons, trace


# ---------------------------------------------------------------- D4  W3
pr3 = -2 + 10 * r**sp.Rational(-5, 2)
pt3 = sp.simplify(pr3 + r * sp.diff(pr3, r) / 2)      # from conservation
u3 = sp.simplify(pr3 + 2 * pt3)                       # traceless: u = p_r + 2 p_t
cons3, tr3 = radial_checks(pr3, pt3)
check("D4a W3 conserved (residual 0), u(1) = -1, p_r(1) = +8 (tree's numbers)",
      cons3 == 0 and u3.subs(r, 1) == -1 and pr3.subs(r, 1) == 8)
# the vector field W^l = T^{lj} x_j has |W| = r p_r ~ r^{-3/2}: not C^1, not bounded at 0
check("D4b W3's W = T.x is UNBOUNDED at the centre (r p_r -> oo): outside 'smooth'",
      sp.limit(r * pr3, r, 0) == sp.oo)
vol4 = sp.integrate(4 * sp.pi * r**2 * tr3, (r, 0, R))        # improper, converges
inner4 = sp.limit(4 * sp.pi * eps**3 * pr3.subs(r, eps), eps, 0)
check("D4c W3: int_B T^ii == 4 pi R^3 p_r(R) (improper integral converges; inner flux -> 0)",
      sp.simplify(vol4 - 4 * sp.pi * R**3 * pr3.subs(r, R)) == 0 and inner4 == 0)

# ---------------------------------------------------------------- D5  independence witness
prI = A / r**3
ptI = -A / (2 * r**3)
consI, trI = radial_checks(prI, ptI)
check("D5a independence witness conserved and trace-free (u = 0): residuals 0", consI == 0 and trI == 0)
rr = sp.sqrt(x**2 + y**2 + z**2)
TI = [[(-A / (2 * rr**3)) * sp.KroneckerDelta(i, j) + (A / rr**3 + A / (2 * rr**3)) * X[i] * X[j] / rr**2
       for j in range(3)] for i in range(3)]
divI = [sp.simplify(sum(sp.diff(TI[l][j], X[l]) for l in range(3))) for j in range(3)]
check("D5b Cartesian d_l T^{lj} = 0 identically on the punctured ball", all(d == 0 for d in divI))
volI = sp.integrate(4 * sp.pi * r**2 * trI, (r, 0, R))
surI = 4 * sp.pi * R**3 * prI.subs(r, R)
check("D5c BALL form FAILS: int_B T^ii = 0 but 4 pi R^3 <T^rr>(R) = 4 pi A",
      sp.simplify(volI) == 0 and sp.simplify(surI - 4 * sp.pi * A) == 0)
shell_vol = sp.integrate(4 * sp.pi * r**2 * trI, (r, eps, R))
shell_sur = surI - 4 * sp.pi * eps**3 * prI.subs(r, eps)
check("D5d SHELL form exact: int_{eps<r<R} T^ii == outer flux - inner flux (4 pi A - 4 pi A = 0)",
      sp.simplify(shell_vol - shell_sur) == 0)
# distributional divergence: pair with phi_j = x_j g(r), g(0)=1, g compactly supported
g = sp.Function("g")
# int T^{ij} d_i(x_j g) dV = int (T^ii g + r p_r g') dV  (T^ii = 0 here)
pairing = sp.integrate(4 * sp.pi * r**2 * (trI * g(r) + r * prI * sp.diff(g(r), r)), (r, 0, R))
pairing = sp.simplify(pairing.doit())
# with g(R) = 0 (support inside the ball), g(0) = 1
pairing_val = sp.simplify(pairing.subs({g(R): 0, g(0): 1}))
check("D5e distributional divergence at the origin is NONZERO: <T, grad(x g)> = -4 pi A",
      sp.simplify(pairing_val + 4 * sp.pi * A) == 0)

# ---------------------------------------------------------------- D6  Whitney via Chen-Torres
s = sp.symbols("s", real=True)
F2 = sp.Matrix([x, y]) / (x**2 + y**2)
div2 = sp.simplify(sp.diff(F2[0], x) + sp.diff(F2[1], y))
flux = (sp.integrate(F2[0].subs({x: 1, y: s}), (s, 0, 1))      # x = 1, n = +e_x
        + sp.integrate(F2[1].subs({x: s, y: 1}), (s, 0, 1)))   # y = 1, n = +e_y
# x = 0 and y = 0 edges: F.n = -x/r^2 = 0 and -y/r^2 = 0 there (off the corner)
check("D6  Whitney/Chen-Torres Ex.2: div F = 0 in (0,1)^2 yet outward flux = pi/2",
      div2 == 0 and sp.simplify(flux - sp.pi / 2) == 0)

# ---------------------------------------------------------------- D7  interface / jump
p1, p2 = sp.symbols("p1 p2", real=True)
# isotropic pressure p1 (r<a), p2 (a<r<R): pointwise divergence-free on each side
vol7 = 3 * p1 * sp.Rational(4, 3) * sp.pi * a**3 + 3 * p2 * sp.Rational(4, 3) * sp.pi * (R**3 - a**3)
sur7 = 4 * sp.pi * R**3 * p2
gap = sp.simplify(vol7 - sur7)
check("D7a jump without surface stress: ball identity off by exactly 4 pi a^3 (p1 - p2)",
      sp.simplify(gap - 4 * sp.pi * a**3 * (p1 - p2)) == 0)
sigma = a * (p1 - p2) / 2                      # Laplace: p1 - p2 = 2 sigma / a
surface_stress_trace = -2 * sigma * 4 * sp.pi * a**2   # tension = negative tangential stress, 2 tangential dirs
check("D7b Laplace surface tension (total tensor distributionally conserved) restores it exactly",
      sp.simplify(vol7 + surface_stress_trace - sur7) == 0)

# ---------------------------------------------------------------- D8  z3
try:
    import z3
    F, Rz, Vb, Ixx, Iyy, Izz, Trr, Cz, Az = z3.Reals("F R Vb Ixx Iyy Izz Trr C A")
    LAUE = z3.And(F > 0, Rz > 0, 3 * Vb == F * Rz**3, Ixx + Iyy + Izz == F * Rz**3 * Trr)
    sI = z3.Solver()
    sI.add(LAUE, Ixx + Iyy + Izz == 0, Trr == Az / Rz**3, Az != 0)
    r1 = sI.check()
    check("D8a LAUE (no centre term) EXCLUDES the independence witness: unsat", r1 == z3.unsat)
    LAUE_C = z3.And(F > 0, Rz > 0, 3 * Vb == F * Rz**3, Ixx + Iyy + Izz == F * Rz**3 * Trr - F * Cz)
    sC = z3.Solver()
    sC.add(LAUE_C, Ixx + Iyy + Izz == 0, Trr == Az / Rz**3, Az != 0, Cz == Az)
    r2 = sC.check()
    check("D8b LAUE with the centre term C = lim r^3 p_r ADMITS it: sat", r2 == z3.sat)
    sV = z3.Solver()
    sV.add(LAUE, Ixx + Iyy + Izz != 0)
    check("D8c vacuity guard: LAUE itself satisfiable with nonzero trace", sV.check() == z3.sat)
except ImportError:
    print("SKIP  D8 (pip install z3-solver)")

print()
if FAIL:
    print(f"{len(FAIL)} FAIL")
    sys.exit(1)
print("ALL PASS")
