#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 0710.3755 (Bezrukov-Shaposhnikov 2008,
'The Standard Model Higgs boson as the inflaton', PLB 659 (2008) 703).

Checks, in order, and exits 1 if any assertion fails:
  A. sympy: the large-xi Einstein-frame reduction of eqs (3)-(8); exact epsilon,
     eta, N(x); the paper's leading forms (9), (10), (12); h_end; h_COBE;
     eq (13) xi = sqrt(lambda/3) N / 0.027^2; n = 1 - 8(4N+9)/(4N+3)^2; r.
  B. numeric: eq (13) evaluated with the tree's READ inputs (m_H = 125.13 GeV,
     v from G_F) -- the source prints NO number for xi, only 49000 sqrt(lambda);
     the tree's 1.7e4 is this formula at tree-level lambda.
  C. the current CMB normalisation (Delta_R^2 ~ 2.1e-9, READ in 2412.03284 eq 4)
     with the exact N(x), N* = 55..62.
  D. the range of xi the later literature READ here gives (running lambda,
     metastability, critical point) and what each does to higgs.py's
     'orders short' and xigate.py's 'GUT requirement / Higgs-inflation xi'.
  E. sign convention: Bezrukov-Shaposhnikov's xi against Barcelo-Visser's xi.
Stdlib + sympy only.  Nothing under research/ is imported or written.
"""
import math
import sys
import sympy as sp

FAIL = []


def chk(name, ok, detail=""):
    print("  [%s] %s %s" % ("ok" if ok else "FAIL", name, detail))
    if not ok:
        FAIL.append(name)


# ----------------------------------------------------------------- A. sympy
print("A. large-xi Einstein frame, exact in x = xi h^2 / M^2")
x, M, lam, xi, N = sp.symbols("x M lambda xi N", positive=True)
h = M * sp.sqrt(x / xi)
Omega2 = 1 + x                                   # eq (3)
# eq (4): dchi/dh = sqrt((Omega^2 + 6 xi^2 h^2/M^2) / Omega^4)
dchidh = sp.sqrt((Omega2 + 6 * xi ** 2 * h ** 2 / M ** 2) / Omega2 ** 2)
dhdx = sp.diff(h, x)
dchidx_full = sp.simplify(dchidh * dhdx)
# leading order in 1/xi at fixed x
dchidx = sp.limit(dchidx_full, xi, sp.oo)
chk("dchi/dx -> sqrt(6) M / (2(1+x)) as xi -> oo",
    sp.simplify(dchidx - sp.sqrt(6) * M / (2 * (1 + x))) == 0, str(dchidx))
U = lam * M ** 4 / (4 * xi ** 2) * x ** 2 / (1 + x) ** 2      # eq (6), v -> 0
d = lambda f: sp.diff(f, x) / dchidx             # d/dchi
eps = sp.simplify(M ** 2 / 2 * (d(U) / U) ** 2)
eta = sp.simplify(M ** 2 * d(d(U)) / U)
zeta2 = sp.simplify(M ** 4 * d(d(d(U))) * d(U) / U ** 2)
chk("epsilon = 4/(3x^2) EXACTLY (paper eq 9 leading form is exact here)",
    sp.simplify(eps - sp.Rational(4, 3) / x ** 2) == 0, str(eps))
chk("eta = 4(1-x)/(3x^2); paper eq (10) -4/(3x) is its large-x term",
    sp.simplify(eta - 4 * (1 - x) / (3 * x ** 2)) == 0, str(eta))
chk("zeta^2 large-x term = 16/(9x^2) (paper eq 11)",
    sp.limit(zeta2 * x ** 2, x, sp.oo) == sp.Rational(16, 9), str(sp.factor(zeta2)))
# eq (12): N = int (1/M^2) U / (dU/dchi) dchi
dNdx = sp.simplify(U / d(U) * dchidx / M ** 2)
chk("dN/dx = 3x/(4(1+x))", sp.simplify(dNdx - 3 * x / (4 * (1 + x))) == 0, str(dNdx))
x0, xe = sp.symbols("x0 xe", positive=True)
Nexact = sp.Rational(3, 4) * ((x0 - xe) - sp.log((1 + x0) / (1 + xe)))
chk("N_exact = (3/4)[(x0-xe) - ln((1+x0)/(1+xe))]",
    sp.simplify(sp.integrate(dNdx.subs(x, sp.Symbol("s", positive=True)),
                             (sp.Symbol("s", positive=True), xe, x0)) - Nexact) == 0)
# paper (12): N ~ (6/8)(h0^2 - hend^2)/(M^2/xi) = (3/4)(x0 - xe) -- the log dropped
xend = sp.sqrt(sp.Rational(4, 3))                # eps = 1
chk("h_end = (4/3)^(1/4) M/sqrt(xi) = 1.0746 M/sqrt(xi) (paper: 1.07)",
    abs(float(xend ** sp.Rational(1, 2)) - 1.0746) < 1e-4, "%.4f" % float(xend ** 0.5))
# h_COBE for N = 62: leading (12) and exact
xc_lead = 4 * 62 / 3 + float(xend)
xc_ex = float(sp.nsolve(Nexact.subs({xe: xend}) - 62, x0, 85))
print("      h_COBE/(M/sqrt xi): leading eq(12) %.3f, exact N(x) %.3f; paper prints 9.4"
      % (math.sqrt(xc_lead), math.sqrt(xc_ex)))
chk("paper's h_COBE ~ 9.4 agrees with the EXACT N(x) (9.35), not the leading form (9.16)",
    abs(math.sqrt(xc_ex) - 9.4) < 0.06 and abs(math.sqrt(xc_lead) - 9.4) > 0.2)
# eq (13): U/eps = (0.027 M)^4 with N = (3/4) x  (xend, log dropped)
xN = sp.Rational(4, 3) * N
target = sp.sqrt(lam / 3) * N / sp.Rational(27, 1000) ** 2
# U/eps at large x (x^2/(1+x)^2 -> 1, eps = 4/(3x^2)):
lead = lam * M ** 4 / (4 * xi ** 2) * (3 * xN ** 2 / 4)
xi13 = sp.solve(sp.Eq(lead, (sp.Rational(27, 1000) * M) ** 4), xi)
xi13 = [s for s in xi13 if s.is_positive][0]
chk("eq (13): xi = sqrt(lambda/3) N / 0.027^2", sp.simplify(xi13 - target) == 0, str(xi13))
coef62 = float(target.subs({lam: 1, N: 62}))
chk("coefficient at N = 62 is 49,1xx (paper: 'xi ~ 49000 sqrt(lambda)')",
    49000 <= coef62 < 49200, "%.1f" % coef62)
# n and r
Ns = sp.Symbol("N", positive=True)
xs = (4 * Ns + 3) / 3                            # x0 = (4/3)N + 1
n_exact_eta = sp.simplify(1 - 6 * eps.subs(x, xs) + 2 * eta.subs(x, xs))
n_lead_eta = sp.simplify(1 - 6 * eps.subs(x, xs) + 2 * (-sp.Rational(4, 3) / xs))
chk("n = 1 - 8(4N+9)/(4N+3)^2 follows with the EXACT eta and x0 = (4N+3)/3",
    sp.simplify(n_exact_eta - (1 - 8 * (4 * Ns + 9) / (4 * Ns + 3) ** 2)) == 0)
print("      (with the leading eta of eq (10) one gets 1 - 8(4N+12)/(4N+3)^2: "
      "n(60) = %.5f vs %.5f -- both print as 0.97)"
      % (float(n_lead_eta.subs(Ns, 60)), float(n_exact_eta.subs(Ns, 60))))
r60 = float((16 * eps.subs(x, xs)).subs(Ns, 60))
chk("r = 192/(4N+3)^2 = 0.0033 at N = 60", abs(r60 - 0.00325) < 5e-5, "%.5f" % r60)
chk("n(60) = 0.966 -> prints 0.97", abs(float(n_exact_eta.subs(Ns, 60)) - 0.9663) < 2e-4)

# ---------------------------------------------------------------- B. numeric
print("\nB. eq (13) at the tree's READ inputs")
G_F = 1.1663788e-5                               # GeV^-2 (higgs.py:207)
v = 1 / math.sqrt(math.sqrt(2) * G_F)
M_H = 125.13                                     # GeV, captures/PDG-2026.tsv pdgid 25
lam_tree = M_H ** 2 / (2 * v ** 2)
xi_bs = 49000 * M_H / (math.sqrt(2) * v)         # eq (13) as printed
xi_bs_exact = coef62 * math.sqrt(lam_tree)
print("      v = %.4f GeV, lambda_tree = %.5f, sqrt = %.5f" % (v, lam_tree, math.sqrt(lam_tree)))
print("      xi = 49000 m_H/(sqrt2 v) = %.1f ; with coefficient %.1f: %.1f"
      % (xi_bs, coef62, xi_bs_exact))
chk("the tree's 1.7e4 is eq (13) at tree-level lambda, truncated (1.76e4 -> '1.7e4')",
    1.7e4 <= xi_bs < 1.8e4 and round(xi_bs, -3) == 18000.0, "%.0f" % xi_bs)
chk("m_H 125.13 -> 125.20 (old pin) moves xi by < 0.1%",
    abs(125.20 / 125.13 - 1) < 1e-3)

# ------------------------------------------------- C. current normalisation
print("\nC. Delta_R^2 = 2.1e-9 (2412.03284 eq 4, READ), exact N(x)")
As = 2.1e-9
delta = (24 * math.pi ** 2 * As) ** 0.25
print("      (U/eps)^(1/4) = %.5f M  (paper used 0.027 M, COBE)" % delta)
xe_f = math.sqrt(4 / 3)


def x_of_N(Nv):
    lo, hi = 1.0, 1e4
    f = lambda X: 0.75 * ((X - xe_f) - math.log((1 + X) / (1 + xe_f))) - Nv
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


rows = []
for Nv in (55, 57, 59, 60, 62):
    X = x_of_N(Nv)
    # U/eps = lambda M^4/(4 xi^2) * x^2/(1+x)^2 * 3x^2/4 = delta^4 M^4
    c = math.sqrt((X ** 2 / (1 + X) ** 2) * 3 * X ** 2 / 16 / delta ** 4)
    rows.append((Nv, c))
    print("      N* = %d: xi = %.0f sqrt(lambda)  -> tree lambda: %.0f" % (Nv, c, c * math.sqrt(lam_tree)))
c59 = dict(rows)[59]
# Rubio's (2.40) xi ~ 800 N* sqrt(lambda) is the LEADING form N/sqrt(72 pi^2 A_s)
# at HIS normalisation (2.39) ln(1e10 A_s) = 3.094 (READ); reproduce it:
As_rubio = math.exp(3.094) / 1e10
lead_rubio = 1 / math.sqrt(72 * math.pi ** 2 * As_rubio)
print("      leading N/sqrt(72 pi^2 A_s): %.1f N at Rubio's A_s = %.4g; %.1f N at 2.1e-9"
      % (lead_rubio, As_rubio, 1 / math.sqrt(72 * math.pi ** 2 * As)))
chk("Rubio (2.40) '800 N sqrt(lambda)' reproduced as the leading form at his A_s (within 1%)",
    abs(lead_rubio / 800 - 1) < 0.01, "%.1f" % lead_rubio)
chk("  and (2.42) 47200 = 800 x 59", abs(lead_rubio * 59 / 47200 - 1) < 0.01)
print("      exact N(x) at N*=59, A_s=2.1e-9 gives %.0f: +%.1f%% over 47200, from A_s (%.1f%%) "
      "and the dropped log/x_end (%.1f%%) -- approximation spread, not a discrepancy"
      % (c59, 100 * (c59 / 47200 - 1), 100 * (math.sqrt(As_rubio / As) - 1),
         100 * (c59 / (59 / math.sqrt(72 * math.pi ** 2 * As)) - 1)))
chk("every N* in 55..62, both normalisations, tree lambda: xi in [1.6e4, 2.0e4]",
    all(1.6e4 <= c * math.sqrt(lam_tree) * f <= 2.0e4 for _, c in rows
        for f in (1.0, math.sqrt(As / As_rubio))))

# ------------------------------------------------------ D. what moves the tree
print("\nD. the xi range in later literature READ here, against the tree's uses")
M_red = 2.4353234593382036e18                    # higgs.reduced_planck_gev()
xi_req = (M_red / v) ** 2
print("      xi_required at the VEV = %.6e (higgs.py:637 pins 9.7829068836e31)" % xi_req)
chk("xi_required reproduced", abs(xi_req / 9.7829068836e31 - 1) < 1e-6)
xi_gut = (M_red / 2e16) ** 2
cases = [
    ("tree pin (higgs.py:213)", 1.7e4),
    ("eq (13) at m_H=125.13, tree lambda", xi_bs),
    ("Rubio (2.42) 47200 sqrt(lambda_tree)", 47200 * math.sqrt(lam_tree)),
    ("eq (13) xi at M_W: xi(M_P) ~ 2 xi(M_W), eq (16) text", xi_bs / 2),
    ("Rubio Fig.6 illustration (threshold-restored)", 1500.0),
    ("Masina-Quiros 2412.03284 Fig.2", 800.0),
    ("Masina-Quiros near metastability", 500.0),
    ("critical Higgs inflation, Rubio sec 3.3", 10.0),
]
print("      %-50s %10s %8s %10s" % ("case", "xi", "orders", "GUT/xi"))
for nm, xv in cases:
    print("      %-50s %10.3g %8.2f %10.3g" % (nm, xv, math.log10(xi_req / xv), xi_gut / xv))
chk("higgs.py selftest 'more than 1e27 above Higgs inflation' holds for EVERY case",
    all(xi_req / xv > 1e27 for _, xv in cases))
chk("'TWENTY-EIGHT ORDERS' is the tree-lambda value (27.7-27.8); running lambda gives 28.1-31.0",
    27.7 < math.log10(xi_req / 1.7e4) < 27.8 and math.log10(xi_req / 10) > 30.9)
chk("xigate.py's 'GUT requirement 0.872x, BELOW Higgs inflation's' holds ONLY at tree lambda",
    xi_gut / 1.7e4 < 1 and all(xi_gut / xv > 1 for nm, xv in cases[3:]),
    "GUT xi = %.4g" % xi_gut)

# ------------------------------------------------------ E. sign convention
print("\nE. sign convention: B-S xi against Barcelo-Visser xi")
phi, kap, xBS, xBV = sp.symbols("phi kappa xi_BS xi_BV", real=True)
# B-S eq (2): -(M^2 + xi h^2) R / 2, footnote 1: 'conformal coupling is xi = -1/6'
geff_BS = kap + xBS * phi ** 2
# BV eq (2.1): (1/2) kappa R - (1/2) xi R phi^2, conformal xi = 1/6 (abstract), T_eff ~ kappa/(kappa - xi phi^2) (2.3)
geff_BV = kap - xBV * phi ** 2
# the conformal scalar is convention-free: its effective Planck coefficient is kappa - phi^2/6
chk("B-S conformal xi = -1/6 gives kappa - phi^2/6",
    sp.simplify(geff_BS.subs(xBS, -sp.Rational(1, 6)) - (kap - phi ** 2 / 6)) == 0)
chk("BV conformal xi = +1/6 gives kappa - phi^2/6",
    sp.simplify(geff_BV.subs(xBV, sp.Rational(1, 6)) - (kap - phi ** 2 / 6)) == 0)
chk("hence xi_BV = -xi_BS identically (same h/phi normalisation: B-S H = h/sqrt2)",
    sp.simplify(geff_BS - geff_BV.subs(xBV, -xBS)) == 0)
# Higgs inflation: xi_BS = +1.7e4  ->  xi_BV = -1.7e4 : BV case 1
xbv_hi = -1.7e4
roots = sp.solve(sp.Eq(kap - xbv_hi * phi ** 2, 0), phi)
chk("at xi_BV = -1.7e4, kappa - xi phi^2 has NO real zero (BV sec 2.3 case 1: 'ANEC is satisfied')",
    all(not r.is_real for r in roots), str(roots))
# BV Jordan->Einstein factor: g_m = (1 - 6 xi Phi^2) g_xi, Phi = phi/sqrt(6 kappa)
Phi = phi / sp.sqrt(6 * kap)
chk("BV conformal factor 1 - 6 xi Phi^2 = 1 - xi_BV phi^2/kappa; B-S Omega^2 = 1 + xi_BS h^2/M^2",
    sp.simplify((1 - 6 * xBV * Phi ** 2).subs(xBV, -xBS) - (1 + xBS * phi ** 2 / kap)) == 0)

print()
if FAIL:
    print("FAILED: %d -- %s" % (len(FAIL), FAIL))
    sys.exit(1)
print("ALL CHECKS PASS")
