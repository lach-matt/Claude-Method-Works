#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: static isotropic weak-field metric and Newtonian limit
as phase1.py Theorem 1 uses it.

    g = -e^{2Phi} dt^2 + e^{-2Phi} (dx^2 + dy^2 + dz^2)      (c = 1)

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  C1  exact for this metric: static observer u = e^{-Phi} d_t is unit; proper length
      on the t-slice is e^{-Phi} dl; coordinate light time along a ray is e^{-2Phi} dl.
  C2  exact identity (1-e^{-2Phi}) = (1-e^{-Phi})(1+e^{-Phi}): the SAVINGS ratio is
      1+e^{-Phi} = 2 - Phi + Phi^2/2 - ..., equal to 2 only at Phi = 0.  The EXPONENT
      ratio is 2 by construction.  Reproduces the tree's 1.9940 (m=2e-2) and 2.0229
      (m=-8e-2) by read-only import.
  C3  PPN match (Will 2014, arXiv:1403.7377 Box 2 p.31: g00 = -1 + 2U - 2 beta U^2 + ...,
      g_ij = (1 + 2 gamma U) delta_ij + O(eps^2)): with Phi = -U the ansatz gives
      beta = 1, gamma = 1; its O(U^2) term in g_ij (coefficient 2) differs from exact
      Schwarzschild in isotropic coordinates (coefficient 3/2) -- an order PPN does not fix.
  C4  Einstein tensor of the ansatz for arbitrary Phi(x,y,z): G_0i = 0; G_ij is purely
      quadratic in grad Phi (so the ansatz is not an exact vacuum solution for
      non-constant Phi, but its stresses are second order -- the Newtonian-limit
      ordering p/rho ~ eps holds).
  C5  light/proper saving ratio under PPN gamma is (1+gamma)/gamma; Cassini
      gamma - 1 = (2.1 +- 2.3)e-5 (Will 2014 p.43) moves 2 by ~2e-5.
  C6  Lambda closed form: exact full-crossing integral
      2 ln((X0+Rs)/B) - 2 X0/Rs  (X0 = sqrt(Rs^2-b^2), B = sqrt(b^2+a^2))
      against the tree's 2[ln(2Rs/B) - 1] and against quadrature.
  C7  SI conversion: G/c^2 with CODATA 2022 G (= CODATA 2018); solar mass via IAU
      nominal GM_sun against the tree's SOLAR_MASS.
  C8  WEAK-FIELD REGIME OF THE PRICE FIGURES (phase1.py:180-181, 508-510): with the
      endpoints outside the shell (which the full-crossing Lambda assumes), the peak
      potential on the ray is Phi_max >= (Delta d / L) * e^2/2 for ANY Rs/b, and
      ~40 * Delta d / L at the tree's Rs/b = 200.  The exact ansatz contraction at
      those m is computed against the linear law m*Lambda.
"""
import math, os, sys
import sympy as sp

sys.dont_write_bytecode = True
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)

FAIL = []
def ok(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not cond:
        FAIL.append(name)

# ---------------------------------------------------------------- C1
t, x, y, z = sp.symbols("t x y z", real=True)
P = sp.Function("Phi")(x, y, z)
g = sp.diag(-sp.exp(2 * P), sp.exp(-2 * P), sp.exp(-2 * P), sp.exp(-2 * P))
u = sp.Matrix([sp.exp(-P), 0, 0, 0])
ok("C1a u = e^{-Phi} d_t is unit timelike", sp.simplify((u.T * g * u)[0]) == -1)
ok("C1b static: g_0i = 0, so the rest space of u is the t = const slice",
   all(g[0, i] == 0 for i in (1, 2, 3)))
dl, dt = sp.symbols("dl dt", positive=True)
# proper length of a coordinate step dl along x on the slice
# ds^2 = e^{-2Phi} dl^2 and e^{-Phi} dl > 0, so ds = e^{-Phi} dl (compare squares of positives)
ok("C1c proper length on the slice = e^{-Phi} dl",
   sp.simplify(g[1, 1] * dl**2 - (sp.exp(-P) * dl)**2) == 0)
sol = sp.solve(sp.Eq(g[0, 0] * dt**2 + g[1, 1] * dl**2, 0), dt)
ok("C1d null ray: coordinate time dt = e^{-2Phi} dl",
   any(sp.simplify(s - sp.exp(-2 * P) * dl) == 0 for s in sol), str(sol))

# ---------------------------------------------------------------- C2
f = sp.symbols("phi", real=True)
ratio = sp.simplify((1 - sp.exp(-2 * f)) / (1 - sp.exp(-f)))
ok("C2a savings ratio integrand = 1 + e^{-Phi} exactly",
   sp.simplify(ratio - (1 + sp.exp(-f))) == 0)
ser = sp.series(1 + sp.exp(-f), f, 0, 3).removeO()
ok("C2b series 2 - Phi + Phi^2/2: ratio = 2 only to first order",
   sp.simplify(ser - (2 - f + f**2 / 2)) == 0, str(ser))
ok("C2c ratio = 2 iff Phi = 0 (1 + e^{-Phi} = 2 <=> Phi = 0)",
   sp.solve(sp.Eq(1 + sp.exp(-f), 2), f) == [0])
try:
    import phase1, unified
    r1 = phase1.exponent_ratio()
    ok("C2d tree's phase1.exponent_ratio() = 1.9940 (< 2, Phi > 0)", abs(r1 - 1.9940) < 1e-4, "%.6f" % r1)
    r2 = unified.exponent_ratio(-8e-2)
    ok("C2e tree's unified ratio at m = -8e-2 = 2.0229 (> 2, Phi < 0)", abs(r2 - 2.0229) < 1e-4, "%.6f" % r2)
    # effective Phi from 1 + e^{-Phi_eff} = ratio
    print("     effective Phi: %.4e (m=2e-2), %.4e (m=-8e-2); first-order departure of the"
          " ratio from 2 is -Phi, as C2b says" % (-math.log(r1 - 1), -math.log(r2 - 1)))
except Exception as e:  # pragma: no cover
    ok("C2d/e tree import", False, repr(e))

# ---------------------------------------------------------------- C3
U = sp.symbols("U", positive=True)
g00 = sp.series(-sp.exp(2 * (-U)), U, 0, 3).removeO()
gij = sp.series(sp.exp(-2 * (-U)), U, 0, 3).removeO()
beta, gamma = sp.symbols("beta gamma")
ppn00 = -1 + 2 * U - 2 * beta * U**2
ppnij = 1 + 2 * gamma * U
ok("C3a g00 matches PPN with beta = 1", sp.solve(sp.Eq(sp.expand(g00 - ppn00), 0), beta) == [1], str(g00))
ok("C3b g_ij matches PPN with gamma = 1 at O(U)",
   sp.solve(sp.Eq(gij.coeff(U, 1), ppnij.coeff(U, 1)), gamma) == [1], str(gij))
# exact Schwarzschild, isotropic coordinates: g00 = -((1-M/2r)/(1+M/2r))^2, gij = (1+M/2r)^4, U = M/r
Mr = U
s00 = sp.series(-((1 - Mr / 2) / (1 + Mr / 2))**2, U, 0, 3).removeO()
sij = sp.series((1 + Mr / 2)**4, U, 0, 3).removeO()
ok("C3c Schwarzschild isotropic g00 = ansatz g00 through O(U^2)", sp.expand(s00 - g00) == 0, str(s00))
ok("C3d Schwarzschild isotropic g_ij U^2 coefficient 3/2 vs ansatz 2 (differ at O(U^2), beyond PPN order)",
   sij.coeff(U, 2) == sp.Rational(3, 2) and gij.coeff(U, 2) == 2)

# C3e: the isotropic Schwarzschild form used in C3c/C3d is itself checked, not quoted:
# its Ricci tensor vanishes identically (r > M/2).
r_, th, ph_, M_ = sp.symbols("r theta varphi M", positive=True)
A_ = ((1 - M_ / (2 * r_)) / (1 + M_ / (2 * r_)))**2
Bf = (1 + M_ / (2 * r_))**4
gs = sp.diag(-A_, Bf, Bf * r_**2, Bf * r_**2 * sp.sin(th)**2)
Xs4 = (t, r_, th, ph_)
gsi = gs.inv()
Gs = [[[sp.simplify(sum(gsi[a, d] * (sp.diff(gs[d, b], Xs4[c]) + sp.diff(gs[d, c], Xs4[b])
                                      - sp.diff(gs[b, c], Xs4[d])) for d in range(4)) / 2)
        for c in range(4)] for b in range(4)] for a in range(4)]
def Rics(b, c):
    return sp.simplify(sum(sp.diff(Gs[a][b][c], Xs4[a]) - sp.diff(Gs[a][b][a], Xs4[c])
                           + sum(Gs[a][a][d] * Gs[d][b][c] - Gs[a][c][d] * Gs[d][b][a]
                                 for d in range(4)) for a in range(4)))
ok("C3e isotropic Schwarzschild is Ricci-flat (so C3d compares against an exact vacuum solution)",
   all(Rics(b, c) == 0 for b in range(4) for c in range(b, 4)))

# ---------------------------------------------------------------- C4
X = (t, x, y, z)
ginv = g.inv()
Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                           + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                 for d in range(4)) for a in range(4)))
R = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
Rs_ = sp.simplify(sum(ginv[a, b] * R[a, b] for a in range(4) for b in range(4)))
G = sp.simplify(R - g * Rs_ / 2)
ok("C4a G_0i = 0 identically for static Phi", all(sp.simplify(G[0, i]) == 0 for i in (1, 2, 3)))
Px, Py, Pz = sp.diff(P, x), sp.diff(P, y), sp.diff(P, z)
lap = sp.diff(P, x, 2) + sp.diff(P, y, 2) + sp.diff(P, z, 2)
grad2 = Px**2 + Py**2 + Pz**2
# expected forms (derived by hand, confirmed symbolically here)
G00_exp = sp.exp(4 * P) * (2 * lap - grad2)
Gxx_exp = -Px**2 + Py**2 + Pz**2
Gxy_exp = -2 * Px * Py
ok("C4b G_tt = e^{4Phi}(2 lap Phi - |grad Phi|^2)", sp.simplify(G[0, 0] - G00_exp) == 0)
ok("C4c G_xx = |grad Phi|^2 - 2 Phi_x^2 (no second derivatives: purely quadratic)",
   sp.simplify(G[1, 1] - Gxx_exp) == 0, str(sp.simplify(G[1, 1])))
ok("C4d G_xy = -2 Phi_x Phi_y", sp.simplify(G[1, 2] - Gxy_exp) == 0)
print("     so a harmonic Phi (vacuum Newtonian potential) leaves G_tt = -e^{4Phi}|grad Phi|^2 != 0"
      " and G_ij != 0: the single-Phi ansatz is GR-vacuum only to first order; its stresses"
      " are O(Phi^2) -- second order, which is the Newtonian-limit ordering.")

# ---------------------------------------------------------------- C5
gam_c, dgam = 1 + 2.1e-5, 2.3e-5
for gv in (gam_c - dgam, gam_c, gam_c + dgam):
    print("     gamma = %.6f -> light/proper saving ratio (1+gamma)/gamma = %.7f" % (gv, (1 + gv) / gv))
ok("C5 Cassini 1-sigma band moves the ratio by < 5e-5, 100x inside the tree's rtol 5e-3",
   max(abs((1 + gv) / gv - 2) for gv in (gam_c - dgam, gam_c + dgam)) < 5e-5)

# ---------------------------------------------------------------- C6
b_, a_, R_ = 1.0, 0.02, 200.0
B = math.hypot(b_, a_); X0 = math.sqrt(R_**2 - b_**2)
lam_exact = 2 * math.log((X0 + R_) / B) - 2 * X0 / R_
lam_tree = 2 * (math.log(2 * R_ / B) - 1)
import mpmath as mp
mp.mp.dps = 30
inner = lambda s: 1 / mp.sqrt(s * s + B * B)
q = 2 * (mp.quad(lambda s: inner(s) - 1 / R_, [0, 1, X0])
         + mp.quad(lambda s: inner(s) - 1 / mp.sqrt(s * s + b_ * b_), [X0, 10 * X0, mp.inf]))
ok("C6a full-crossing closed form = quadrature", abs(float(q) - lam_exact) < 1e-12,
   "exact %.9f, quad %.9f" % (lam_exact, float(q)))
ok("C6b tree's 2[ln(2Rs/B) - 1] = %.6f agrees with exact to %.1e (relative)" % (lam_tree, abs(lam_tree / lam_exact - 1)),
   abs(lam_tree / lam_exact - 1) < 1e-5, "exact %.7f" % lam_exact)
# symbolic: exact closed form -> tree form as b/Rs -> 0
bb, RR, BB = sp.symbols("b R_s B", positive=True)
Xs = sp.sqrt(RR**2 - bb**2)
lam_sym = 2 * sp.log((Xs + RR) / BB) - 2 * Xs / RR
ok("C6c limit b/Rs -> 0 of the exact form is 2[ln(2Rs/B) - 1]",
   sp.simplify(sp.limit(lam_sym - (2 * sp.log(2 * RR / BB) - 2), bb, 0)) == 0)

# ---------------------------------------------------------------- C7
C_SI = 299792458.0
G18 = G22 = 6.67430e-11          # CODATA 2018 = CODATA 2022 (arXiv:2409.03787 Table XXXII, read in sibling audit)
GM_SUN = 1.3271244e20            # IAU 2015 Resolution B3 nominal (NAMED here; not re-read this stage)
M_TREE = 1.98892e30
per_msun_tree = G18 * M_TREE / C_SI**2 * lam_tree
per_msun_iau = GM_SUN / C_SI**2 * lam_tree
print("     1 solar mass buys %.2f m (tree M_sun) vs %.2f m (IAU GM_sun/c^2); relative %.2e"
      % (per_msun_tree, per_msun_iau, per_msun_tree / per_msun_iau - 1))
ok("C7 SI conversion: M_sun datum moves 14.7 km by < 1e-3 (tree selftest rtol 1e-3)",
   abs(per_msun_tree / per_msun_iau - 1) < 1e-3)

# ---------------------------------------------------------------- C8
fmin = min(math.exp((L + 2) / 2) / L for L in [0.5 + 0.001 * k for k in range(20000)])
ok("C8a min over Lambda of e^{(Lambda+2)/2}/Lambda = e^2/2 = %.4f (at Lambda = 2)" % (math.e**2 / 2),
   abs(fmin - math.e**2 / 2) < 1e-6)
f_tree = math.exp((lam_tree + 2) / 2) / lam_tree
print("     at the tree's Rs/b = 200 (Lambda = %.4f) the factor is %.2f" % (lam_tree, f_tree))
for frac in (0.01, 0.50):
    print("     Delta d/L = %.2f: Phi_max >= %.3f for ANY shell; = %.2f at the tree's geometry"
          % (frac, frac * math.e**2 / 2, frac * f_tree))
ok("C8b the 50 % figure needs Phi_max >= 1.85 for any geometry (not weak field)",
   0.5 * math.e**2 / 2 > 1)
# exact ansatz contraction at the tree geometry, units of b, endpoints at the shell (X = Rs)
try:
    import phase1
    for frac in (0.01, 0.50):
        L = 2 * R_                      # corridor length = 2 Rs = 400 b (Rs <= L/2)
        m = frac * L / lam_tree         # m the linear law demands
        exact = phase1.proper_contraction(m, b=1.0, X=R_, n=200001)
        phimax = phase1.phi_device(0.0, 1.0, m)
        print("     Delta d/L = %.2f: m = %.4f b, Phi_max = %.3f; linear law m*Lambda = %.3f b;"
              " exact ansatz int(1-e^{-Phi}) = %.3f b (ratio %.3f)"
              % (frac, m, phimax, m * lam_tree, exact, exact / (m * lam_tree)))
        if frac == 0.50:
            ok("C8c at 50 % the exact ansatz contraction falls far short of the linear law",
               exact / (m * lam_tree) < 0.5, "%.3f" % (exact / (m * lam_tree)))
        else:
            ok("C8d at 1 % the nonlinear shortfall is < 20 % (marginal weak field)",
               0.8 < exact / (m * lam_tree) < 1.0, "%.3f" % (exact / (m * lam_tree)))
except Exception as e:  # pragma: no cover
    ok("C8c/d tree import", False, repr(e))

print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
