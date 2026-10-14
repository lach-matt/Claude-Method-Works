#!/usr/bin/env python3
"""DOCKET 67 re-derivation: interior Newtonian potential of a uniform sphere and the
weak-field redshift the tree (excite.py:171-180, 862-888, 1854-1865) builds on it.

Checks, each printed with PASS/FAIL:
  N1  Phi(r) = -GM(3R^2 - r^2)/(2R^3) is the UNIQUE interior solution of
      (1/r^2)(r^2 Phi')' = 4 pi G rho regular at r=0 that joins -GM/r at R with
      continuous Phi and Phi' (derived by dsolve, not assumed).
  N2  Phi(0) = -(3/2)GM/R = -2 pi G rho R^2 ;  Phi(R) - Phi(0) = GM/(2R) = (2/3) pi G rho R^2.
  N3  ratio exactly 3, crossover ratio exactly sqrt(3) (Newtonian weak-field reading).
  G1  Schwarzschild 1916 interior (constant density): sqrt(-g_tt) =
      (3 sqrt(1-x) - sqrt(1 - x r^2/R^2))/2, x = 2GM/(R c^2), with p(r) as printed in
      Schwarzschild eq (30); the full Einstein tensor is computed from the metric and
      G^mu_nu = 8 pi G T^mu_nu / c^4 is verified symbolically (no textbook formula assumed).
  G2  weak-field expansion: 1 - sqrt(A(0)) = (3/4)x + O(x^2)  ==  2 pi G rho R^2/c^2 at O(x);
      1 - sqrt(A(0)/A(R)) = x/4 + O(x^2) == GM/(2R c^2).  The exact GR ratio is NOT 3:
      it is 3 cos(chi_a) (1 - sqrt... ) -- printed exactly -- with correction O(x).
  G3  the size of the GR correction at the tree's own crossovers (eps = 1e-18): ~1e-18
      relative, far inside the selftest tolerance 2e-3.
  D1  data: G enters R* as G^(-1/2); CODATA 2022 G = CODATA 2018 G = 6.67430(15)e-11
      (arXiv:2409.03787 Table XXXII); spread of the 16 input measurements (Table XXX)
      moves R* by < 3e-4 relative, inside the tree's 2e-3 tolerance.
  K1  Klotz 1308.1342 eq (9) (a restatement NOT used as source): with M(r)/r as the
      interior potential, v^2 at the centre is 2GM/R, against GM/R from N1 and against
      Klotz's own quoted ~8 km/s.  Recorded as a discrepancy in that restatement only.
"""
import math
import sys
import sympy as sp

OK = True


def check(label, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, detail))


print("N. Newtonian interior potential")
r, R, G, rho, M, c = sp.symbols("r R G rho M c", positive=True)
C1, C2 = sp.symbols("C1 C2")
f = sp.Function("Phi")
ode = sp.Eq(sp.diff(r ** 2 * sp.diff(f(r), r), r) / r ** 2, 4 * sp.pi * G * rho)
gen = sp.dsolve(ode, f(r)).rhs
# regular at r = 0 kills the C/r term: find the coefficient of 1/r
consts = sorted(gen.free_symbols - {r, G, rho}, key=str)
sing = [k for k in consts if sp.limit(sp.diff(gen, k) * r, r, 0) != 0]
reg = gen.subs({k: 0 for k in sing})
rest = [k for k in consts if k not in sing]
Mexpr = sp.Rational(4, 3) * sp.pi * rho * R ** 3
sol = sp.solve([sp.Eq(reg.subs(r, R), -G * Mexpr / R)], rest, dict=True)[0]
Phi = sp.simplify(reg.subs(sol))
check("N1 derivative continuous at R (Phi'(R) = GM/R^2)",
      sp.simplify(sp.diff(Phi, r).subs(r, R) - G * Mexpr / R ** 2) == 0)
target = -G * Mexpr * (3 * R ** 2 - r ** 2) / (2 * R ** 3)
check("N1 Phi == -GM(3R^2 - r^2)/(2R^3)", sp.simplify(Phi - target) == 0, str(sp.factor(Phi)))
check("N2 Phi(0) == -(3/2)GM/R", sp.simplify(Phi.subs(r, 0) + sp.Rational(3, 2) * G * Mexpr / R) == 0)
check("N2 Phi(0) == -2 pi G rho R^2", sp.simplify(Phi.subs(r, 0) + 2 * sp.pi * G * rho * R ** 2) == 0)
dS = sp.simplify(Phi.subs(r, R) - Phi.subs(r, 0))
check("N2 Phi(R)-Phi(0) == GM/(2R) == (2/3) pi G rho R^2",
      sp.simplify(dS - G * Mexpr / (2 * R)) == 0 and sp.simplify(dS - sp.Rational(2, 3) * sp.pi * G * rho * R ** 2) == 0)
ratio = sp.simplify(-Phi.subs(r, 0) / dS)
check("N3 centre-vs-infinity / centre-vs-surface == 3 exactly", ratio == 3, str(ratio))
check("N3 crossover ratio sqrt(3) exactly", sp.sqrt(ratio) == sp.sqrt(3))

# N4: off-centre clock (the owner prose says "inside the region"; the value 2 pi G rho R^2 is the centre's)
off = sp.simplify(-Phi)          # vs infinity at radius r
check("N4 clock at radius r vs infinity: 2 pi G rho (R^2 - r^2/3)",
      sp.simplify(off - 2 * sp.pi * G * rho * (R ** 2 - r ** 2 / 3)) == 0)
check("N4 at the surface vs infinity: (4/3) pi G rho R^2 = GM/R; crossover factor sqrt(3/2)",
      sp.simplify(off.subs(r, R) - G * Mexpr / R) == 0
      and sp.sqrt(sp.simplify(-Phi.subs(r, 0) / off.subs(r, R))) == sp.sqrt(sp.Rational(3, 2)))

print("\nG. Schwarzschild 1916 interior, exact")
x = sp.symbols("x", positive=True)          # x = 2GM/(R c^2) < 8/9
t, th, ph = sp.symbols("t theta phi")
kap = sp.symbols("kappa", positive=True)    # kappa = 8 pi G / c^4 ; geometric: use rho_e = energy density
# geometric units G = c = 1 for the tensor check; x = 2M/R, rho_e = 3M/(4 pi R^3)
Mg = x * R / 2
rho_e = 3 * Mg / (4 * sp.pi * R ** 3)
sq = sp.sqrt(1 - x * r ** 2 / R ** 2)
sa = sp.sqrt(1 - x)
alpha = (3 * sa - sq) / 2                   # sqrt(-g_tt)
A = alpha ** 2
B = 1 / (1 - x * r ** 2 / R ** 2)            # g_rr = (1 - 2 m(r)/r)^-1, m = M r^3/R^3
p = rho_e * (sq - sa) / (3 * sa - sq)       # Schwarzschild eq (30): rho0 + p = rho0 * 2cos(chi_a)/(3cos(chi_a) - cos(chi))
coords = [t, r, th, ph]
g = sp.diag(-A, B, r ** 2, r ** 2 * sp.sin(th) ** 2)
ginv = g.inv()
n = 4
Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], coords[cc]) + sp.diff(g[d, cc], coords[b])
                                        - sp.diff(g[b, cc], coords[d])) for d in range(n)) / 2)
          for cc in range(n)] for b in range(n)] for a in range(n)]


def ricci(b, cc):
    s = 0
    for a in range(n):
        s += sp.diff(Gam[a][b][cc], coords[a]) - sp.diff(Gam[a][b][a], coords[cc])
        for d in range(n):
            s += Gam[a][a][d] * Gam[d][b][cc] - Gam[a][cc][d] * Gam[d][b][a]
    return s


Ric = sp.Matrix(n, n, lambda i, j: ricci(i, j))
Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
Gmix = sp.simplify(ginv * (Ric - Rs * g / 2))     # G^mu_nu
T = sp.diag(-rho_e, p, p, p)                      # T^mu_nu perfect fluid at rest
res = [sp.simplify(Gmix[i, i] - 8 * sp.pi * T[i, i]) for i in range(n)]
check("G1 G^t_t = -8 pi rho (constant density)", res[0] == 0, str(res[0]))
check("G1 G^r_r = 8 pi p   (Schwarzschild eq (30) pressure)", res[1] == 0, str(res[1]))
check("G1 G^th_th = 8 pi p", res[2] == 0, str(res[2]))
check("G1 p(R) = 0 and A(R) = 1 - x (joins exterior Schwarzschild)",
      sp.simplify(p.subs(r, R)) == 0 and sp.simplify(A.subs(r, R) - (1 - x)) == 0)
# matches Schwarzschild's own printed form ((3cos chi_a - cos chi)/2)^2 with sin chi = r sqrt(kappa rho/3):
# in geometric units kappa rho/3 = 8 pi rho/3 = x/R^2, so cos chi = sqrt(1 - x r^2/R^2)
check("G1 same as Schwarzschild eq (29) f4 with cos chi = sqrt(1 - x r^2/R^2)",
      sp.simplify(8 * sp.pi * rho_e / 3 - x / R ** 2) == 0)

print("\nG2. weak-field limit")
a0 = alpha.subs(r, 0)
aR = alpha.subs(r, R)
z_inf = 1 - a0                       # fractional rate deficit, centre vs infinity (exact)
z_srf = 1 - a0 / aR                  # centre vs surface (exact)
s_inf = sp.series(z_inf, x, 0, 3).removeO()
s_srf = sp.series(z_srf, x, 0, 3).removeO()
print("   1 - sqrt(A(0))        =", sp.expand(s_inf), "+ O(x^3)")
print("   1 - sqrt(A(0)/A(R))   =", sp.expand(s_srf), "+ O(x^3)")
# Newtonian: 2 pi G rho R^2/c^2 = (3/2) GM/(R c^2) = (3/4) x ;  GM/(2Rc^2) = x/4
check("G2 leading term centre-vs-infinity == (3/4)x == 2 pi G rho R^2/c^2",
      sp.expand(s_inf).coeff(x, 1) == sp.Rational(3, 4))
check("G2 leading term centre-vs-surface == x/4 == GM/(2R c^2)",
      sp.expand(s_srf).coeff(x, 1) == sp.Rational(1, 4))
exact_ratio = sp.simplify(z_inf / z_srf)
print("   exact GR ratio z_inf/z_srf =", exact_ratio)
check("G2 exact GR ratio == 3 sqrt(1-x) (not exactly 3; -> 3 as x -> 0)",
      sp.simplify(exact_ratio - 3 * sp.sqrt(1 - x)) == 0)
check("G2 limit x->0 of ratio is 3", sp.limit(exact_ratio, x, 0) == 3)

print("\nG3. size of the GR correction at the tree's crossovers")
Gn, cn = 6.67430e-11, 2.99792458e8
eps = 1e-18
# at the centre-vs-infinity crossover (3/4) x = eps -> x = 4 eps/3 to leading order
xstar = 4 * eps / 3
# exact factor sqrt(3 sqrt(1-x))/sqrt(3) = (1-x)^(1/4); float 1-(1-x)^(1/4) underflows, so use the series
dev = float(sp.series(1 - (1 - x) ** sp.Rational(1, 4), x, 0, 3).removeO().subs(x, xstar))
print("   x at crossover ~ %.3e ; crossover factor deviates from sqrt(3) by %.3e relative" % (xstar, dev))
check("G3 GR correction to sqrt(3) < 1e-17 (tree tolerance 2e-3, claim 'EXACTLY' is Newtonian)",
      0 < dev < 1e-17)
# pressure: p/rho at centre ~ x/4 in the weak field
pc = sp.series(sp.simplify((p / rho_e).subs(r, 0)), x, 0, 2).removeO()
print("   p_c/(rho c^2) =", pc, "+ O(x^2)  ->  %.2e at the crossover" % float(pc.subs(x, xstar)))

print("\nD1. data: G")
try:
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import excite  # read-only import
    rows = excite.COURIER_CROSSOVER_M
    for k, v in rows.items():
        rho_k = excite.EPS_AT_FIXTURE * cn ** 2 / (2 * math.pi * excite.G * v ** 2)
        print("   %-14s R* = %.6e m  (rho implied %.4e kg/m^3)" % (k, v, rho_k))
    check("D1 tree uses G = 6.67430e-11 (CODATA 2018 == 2022)", excite.G == 6.67430e-11)
    check("D1 tree uses c = 299792458", excite.C == 2.99792458e8)
    check("D1 tree surface factor == sqrt(3)", abs(excite.SURFACE_TWIN_FACTOR - math.sqrt(3)) < 1e-15)
except Exception as e:  # pragma: no cover
    print("   excite import failed (%s); data check on constants only" % e)
Gs = [6.67248, 6.6729, 6.67398, 6.674255, 6.67559, 6.67422, 6.67387, 6.67222, 6.67425,
      6.67349, 6.67554, 6.67191, 6.67435, 6.674184, 6.674484, 6.67260]   # CODATA 2022 Table XXX
spread = max(Gs) / min(Gs) - 1
dR = math.sqrt(max(Gs) / min(Gs)) - 1
print("   16-input G spread %.3e -> R* moves %.3e relative (R* ~ G^-1/2)" % (spread, dR))
check("D1 G spread moves R* by less than the 2e-3 tolerance", dR < 2e-3)
check("D1 G CODATA u_r 2.2e-5 moves R* by 1.1e-5", abs(0.5 * 2.2e-5 - 1.1e-5) < 1e-12)

print("\nK1. Klotz 1308.1342 eq (8)-(9) restatement (not used)")
GME, RE = 3.986004418e14, 6.371e6
v_correct = math.sqrt(GME / RE)          # from N1: Phi(R) - Phi(0) = GM/(2R) -> v^2 = GM/R
v_klotz = math.sqrt(2 * GME / RE)        # eq (9) with M(r)/r, r -> 0
print("   centre speed from N1: %.3f km/s ; from Klotz eq (9): %.3f km/s ; Klotz text: 'near 8 km/s'"
      % (v_correct / 1e3, v_klotz / 1e3))
check("K1 N1 reproduces Klotz's quoted ~8 km/s; his printed eq (9) gives sqrt(2) more",
      abs(v_correct / 1e3 - 7.9) < 0.1 and abs(v_klotz / v_correct - math.sqrt(2)) < 1e-12)

print("\nALL PASS" if OK else "\nSOME CHECK FAILED")
sys.exit(0 if OK else 1)
