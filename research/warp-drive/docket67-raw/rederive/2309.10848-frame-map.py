#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 2309.10848-frame-map:
FFKP (Fliss, Freivogel, Kontou, Pardo Santos, arXiv:2309.10848v1) Jordan -> Einstein frame map,
as used at research/warp-drive/candidates.py:233-237.

Checks (PASS/FAIL, or MEASURED numbers with no verdict implied):
  K1  conformal transformation of the Ricci scalar in n dims, R[g] with g~ = Omega^2 g:
      R = Omega^2 [ R~ + 2(n-1) box~ ln Omega - (n-2)(n-1) (d~ ln Omega)^2 ]
      verified by sympy on explicit metrics for n = 3 and n = 4 (not assumed).
  K2  with Omega^(n-2) = 1 - k xi phi^2 (FFKP eq. 99), the Einstein-frame kinetic coefficient is
      F'(phi)^2 = [1 - k xi (1 - xi/xi_c) phi^2] / (1 - k xi phi^2)^2,  xi_c = (n-2)/(4(n-1))
      (FFKP eq. 100), derived here from K1 + integration by parts.
  K3  Einstein-frame NEC: T~_{mu nu} l^mu l^nu = (l.d phi~)^2 for any potential V~, because a null
      vector of g is null for g~ = Omega^2 g (FFKP eqs. 23-24).  sympy.
  K4  exact factor Omega^2 = (1-x)^(2/(n-2)) against the tree's exp(-2x/(n-2)) (FFKP eq. 3 '≈'):
      series agree to O(x); the relative gap is MEASURED on a grid.
  K5  what 'small x' means in Planck units: phi^2 ~ M_c^(n-2) (FFKP eq. 2) gives
      x = 8 pi xi (M_c/M_P)^(n-2) [non-reduced M_P] = xi (M_c/Mbar_P)^(n-2) [reduced]; MEASURED at
      Planckian cutoff, and at the tree's own NMC crossover l_UV = 3.159514 l_P (candidates.py 4c).
  K6  FFKP eq. (18): Jordan-frame effective null energy on a flat null geodesic,
      rho_eff = [ (phi')^2 - xi (phi^2)'' ] / (1 - k xi phi^2); a smooth profile with
      k xi phi^2 << 1 everywhere and rho_eff < 0 somewhere is exhibited (sympy/numeric) -- the
      local classical effective-NEC violation does NOT need large field values.
  K8  the violation in K6 does not vanish as kappa -> 0: closeness of the metrics (a C^0 statement)
      does not control the effective null energy (second derivatives of phi^2).
  K7  FFKP eq. (20): the effective-ANEC integrand after integration by parts,
      [1 - k xi (1-4 xi) phi^2] / (1 - k xi phi^2)^2 (phi')^2, from eq. (19) by sympy.
"""
import math, sys
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------------------------------------------------------- geometry helpers
def ricci_scalar(g, X):
    n = len(X)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                            - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    R = 0
    for b in range(n):
        for c in range(n):
            Rbc = 0
            for a in range(n):
                Rbc += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    Rbc += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            R += ginv[b, c] * Rbc
    return sp.simplify(R)

def box(f, g, X):
    n = len(X); ginv = g.inv(); sg = sp.sqrt(abs(g.det()))
    sg = sp.sqrt(sp.simplify(-g.det())) if sp.simplify(g.det()).could_extract_minus_sign() else sp.sqrt(sp.simplify(g.det()))
    return sp.simplify(sum(sp.diff(sg * ginv[a, b] * sp.diff(f, X[b]), X[a]) for a in range(n) for b in range(n)) / sg)

def grad2(f, g, X):
    n = len(X); ginv = g.inv()
    return sp.simplify(sum(ginv[a, b] * sp.diff(f, X[a]) * sp.diff(f, X[b]) for a in range(n) for b in range(n)))

# ---------------------------------------------------------------- K1
print("K1  conformal transformation of R (explicit metrics)")
t, x, y, z = sp.symbols('t x y z', real=True)
for n, X, gdiag, w in [
        (3, [t, x, y], [-(1 + x**2), sp.exp(t), 1 + y**2], x * t + y),
        (4, [t, x, y, z], [-(1 + x**2), sp.exp(t), 1 + y**2, 1 + z**2 * x**2], x * t + y * z)]:
    g = sp.diag(*gdiag)
    lnO = w / 7                     # ln Omega, arbitrary smooth function
    Om2 = sp.exp(2 * lnO)
    gt = Om2 * g
    R, Rt = ricci_scalar(g, X), ricci_scalar(gt, X)
    rhs = Om2 * (Rt + 2 * (n - 1) * box(lnO, gt, X) - (n - 2) * (n - 1) * grad2(lnO, gt, X))
    # evaluate at a few numeric points (the full simplify is slow in n = 4)
    pts = [{t: 0.3, x: 0.7, y: -0.2, z: 0.5}, {t: -1.1, x: 0.2, y: 0.9, z: -0.4}]
    diff = max(abs(float(sp.N((R - rhs).subs(p)))) for p in pts)
    chk(f"K1 n={n}: R = Omega^2[R~ + 2(n-1) box~lnOmega - (n-2)(n-1)(d~lnOmega)^2]  (max|diff|={diff:.1e})", diff < 1e-10)

# ---------------------------------------------------------------- K2
print("K2  Einstein-frame kinetic coefficient F'(phi)^2 (FFKP eq. 100)")
nn, k, xi, ph = sp.symbols('n kappa xi phi', positive=True)
A = 1 - k * xi * ph**2                         # Omega^(n-2)
lnOm = sp.log(A) / (nn - 2)
# Jordan action: sqrt(-g)[ A R/(2k) - (1/2)(d phi)^2 ].  sqrt(-g) = Omega^-n sqrt(-g~), g^{mn} = Omega^2 g~^{mn}.
# gravity: Omega^-n * A * Omega^2 [R~ - (n-1)(n-2)(d~ lnOmega)^2]/(2k) (box term is a total derivative)
#        = [R~ - (n-1)(n-2) (dlnOmega/dphi)^2 (d~phi)^2]/(2k)   since Omega^(2-n) A = 1
# scalar : -(1/2) Omega^(2-n) (d~phi)^2 = -(1/2) (d~phi)^2 / A
Fp2 = 1 / A + (nn - 1) * (nn - 2) / k * sp.diff(lnOm, ph)**2
xic = (nn - 2) / (4 * (nn - 1))
Fp2_paper = (1 - k * xi * (1 - xi / xic) * ph**2) / A**2
chk("K2 F'^2 derived == FFKP (100) squared", sp.simplify(Fp2 - Fp2_paper) == 0)
chk("K2 Omega^(2-n) * A == 1 (Planck mass canonical in Einstein frame)",
    sp.simplify(sp.exp((2 - nn) * lnOm) * A - 1) == 0)
# FFKP (103) at xi = xi_c: F = arctanh(sqrt(k xi_c) phi)/sqrt(k xi_c)
Fc = sp.atanh(sp.sqrt(k * xic) * ph) / sp.sqrt(k * xic)
chk("K2 FFKP (103): d/dphi arctanh(sqrt(k xi_c) phi)/sqrt(k xi_c) == F' at xi = xi_c",
    sp.simplify(sp.diff(Fc, ph)**2 - Fp2_paper.subs(xi, xic)) == 0)
# domain of the map
for n_ in (3, 4, 5):
    xc = sp.Rational(n_ - 2, 4 * (n_ - 1))
    print(f"    n={n_}: xi_c = {xc};  for xi>0 the map needs 1 - k xi phi^2 > 0 (Omega real, nonzero);"
          f" for xi<0 it exists at every phi")

# ---------------------------------------------------------------- K3
print("K3  Einstein-frame NEC (FFKP eqs. 23-24)")
l = sp.Matrix(sp.symbols('l0:4', real=True))
dph = sp.Matrix(sp.symbols('p0:4', real=True))
O2, Vt = sp.symbols('Omega2 Vt', positive=True)
eta = sp.diag(-1, 1, 1, 1)
gt = O2 * eta
null_cond = (l.T * eta * l)[0]                     # l null for g
Tll = (l.dot(dph))**2 - sp.Rational(1, 2) * (l.T * gt * l)[0] * (2 * Vt + (dph.T * (gt.inv()) * dph)[0])
Tll_on_null = sp.simplify(Tll.subs(l[0], sp.sqrt(l[1]**2 + l[2]**2 + l[3]**2)))
chk("K3 l null for g  =>  null for g~ = Omega^2 g, and T~_ll = (l.dphi~)^2 >= 0 for any V~",
    sp.simplify(Tll_on_null - (l.dot(dph))**2).subs(l[0], sp.sqrt(l[1]**2 + l[2]**2 + l[3]**2)) == 0)

# ---------------------------------------------------------------- K4
print("K4  exact (1-x)^(2/(n-2)) vs the tree's exp(-2x/(n-2))")
X_ = sp.symbols('x')
for n_ in (3, 4, 5, 6):
    p = sp.Rational(2, n_ - 2)
    ex, ap = (1 - X_)**p, sp.exp(-p * X_)
    s = sp.series(ex - ap, X_, 0, 3).removeO()
    chk(f"K4 n={n_}: exact - exp = {sp.simplify(s)} + O(x^3)  (agree to O(x); gap -p x^2/2 at O(x^2))",
        sp.simplify(sp.series(ex - ap, X_, 0, 2).removeO()) == 0)
print("    MEASURED relative gap |exact/exp - 1| at n = 4:")
for xv in (0.01, 0.05, 0.1, 0.2, 0.5, 0.9, 0.99):
    e = 1 - xv; a = math.exp(-xv)
    print(f"      x={xv:<5} exact={e:.6f} exp={a:.6f}  |exact/exp-1|={abs(e/a-1):.4%}")
print("    and at x -> 1 (xi>0) the exact factor -> 0 (map degenerates) while exp -> e^-2/(n-2); for x<0 (xi<0)"
      " both > 1")

# ---------------------------------------------------------------- K5
print("K5  size of x = 8 pi G xi phi^2 under FFKP eq. (2), phi^2_max ~ M_c^(n-2)")
for xv_name, xv in (("xi=1/6 (conformal, n=4)", 1 / 6), ("xi=1", 1.0), ("xi=0.01", 0.01)):
    xP = 8 * math.pi * xv          # M_c = M_P (non-reduced), n = 4
    xPbar = xv                     # M_c = reduced Planck mass
    print(f"    {xv_name}: M_c=M_P -> x={xP:.4f}; M_c=Mbar_P -> x={xPbar:.4f}")
chk("K5 at M_c = M_P (non-reduced) x = 8 pi xi = 4.18879 for xi = 1/6: NOT small; > 1 so Omega^2 < 0 at n=4",
    abs(8 * math.pi / 6 - 4.18879) < 1e-5)
luv = 3.159514                  # candidates.py 4c, NMC crossover in l_P
xcross = 8 * math.pi / luv**2
print(f"    tree's NMC crossover l_UV = {luv} l_P: x = 8 pi xi (l_P/l_UV)^2 = {xcross:.6f} xi")
for xv in (1 / 6, 0.4642, 1.0):
    xx = xcross * xv
    fac_exact = (1 - xx) if xx < 1 else float('nan')
    print(f"      xi={xv:.4f}: x={xx:.4f}  exp(-x)={math.exp(-xx):.4f}  exact (1-x)={fac_exact:.4f}")
chk("K5 at the tree's crossover with |xi| = 1, x = 2.5177 > 1: the metric factor is NOT close to one there",
    abs(xcross - 2.5177) < 1e-3)
print("    l_UV at which x = 1 : sqrt(8 pi |xi|) l_P = %.4f sqrt|xi| l_P" % math.sqrt(8 * math.pi))

# ---------------------------------------------------------------- K6
print("K6  FFKP eq. (18): local effective-NEC violation at SMALL field values")
lam = sp.symbols('lambda', real=True)
eps, a0 = sp.Rational(1, 10), sp.Rational(1, 2)
kxi = sp.Rational(1, 100)       # k*xi (xi>0); phi below is O(1) so k xi phi^2 <= 0.01*... small
xi_v = sp.Rational(1, 6)
kk = kxi / xi_v
phi_prof = a0 + eps * lam**2 * sp.exp(-lam**2)        # local minimum of phi^2 at lambda = 0
rho_eff = (sp.diff(phi_prof, lam)**2 - xi_v * sp.diff(phi_prof**2, lam, 2)) / (1 - kk * xi_v * phi_prof**2)
r0 = sp.nsimplify(rho_eff.subs(lam, 0))
maxx = max(float((kk * xi_v * phi_prof**2).subs(lam, v)) for v in [i / 10 for i in range(-50, 51)])
print(f"    profile phi = 1/2 + (1/10) lam^2 exp(-lam^2), xi = 1/6, k xi = 1/100: max k xi phi^2 = {maxx:.5f}")
print(f"    rho_eff(lam=0) = {r0} = {float(r0):.6f}")
chk("K6 rho_eff < 0 at a local minimum of phi^2 with k xi phi^2 <= 0.003 (EFT-valid field values)",
    float(r0) < 0 and maxx < 0.01)
# ANEC for this profile (eq. 20) stays >= 0
integrand20 = (1 - kk * xi_v * (1 - 4 * xi_v) * phi_prof**2) / (1 - kk * xi_v * phi_prof**2)**2 * sp.diff(phi_prof, lam)**2
anec = sp.Integral(rho_eff, (lam, -12, 12)).evalf(30)
anec20 = sp.Integral(integrand20, (lam, -12, 12)).evalf(30)
print(f"    effective ANEC for the same profile: int rho_eff = {float(anec):.6e};  eq.(20) form = {float(anec20):.6e}")
chk("K6 same profile: effective ANEC >= 0 (eq. 19 == eq. 20 numerically)",
    float(anec) >= 0 and abs(float(anec) - float(anec20)) < 1e-12)

# ---------------------------------------------------------------- K7
print("K7  FFKP eq. (20) from eq. (19) by parts")
f = sp.Function('f')(lam)
lhs = (sp.diff(f, lam)**2 - xi * sp.diff(f**2, lam, 2)) / (1 - k * xi * f**2)
# subtract the total derivative d/dlam[ -xi (f^2)' /(1-k xi f^2) ]
td = sp.diff(-xi * sp.diff(f**2, lam) / (1 - k * xi * f**2), lam)
rhs20 = (1 - k * xi * (1 - 4 * xi) * f**2) / (1 - k * xi * f**2)**2 * sp.diff(f, lam)**2
chk("K7 eq.(19) integrand - total derivative == eq.(20) integrand (the 4 is correct for this rho_eff)",
    sp.simplify(lhs - td - rhs20) == 0)

# ---------------------------------------------------------------- K8
print("K8  metric closeness is C^0; the effective-NEC violation is second-order in phi and survives kappa -> 0")
kap = sp.symbols('kap', nonnegative=True)
rho_k = (sp.diff(phi_prof, lam)**2 - xi_v * sp.diff(phi_prof**2, lam, 2)) / (1 - kap * xi_v * phi_prof**2)
r_k = sp.simplify(rho_k.subs(lam, 0))
r_lim = sp.limit(r_k, kap, 0)
print(f"    rho_eff(0) as a function of kappa: {r_k};  kappa -> 0 limit (metric factor exactly 1): {r_lim}")
chk("K8 as kappa -> 0 (Omega^2 -> 1 exactly) the local effective-NEC violation tends to -xi (phi^2)'' = -1/30 != 0",
    r_lim == sp.Rational(-1, 30))

print("\nRESULT:", "ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
