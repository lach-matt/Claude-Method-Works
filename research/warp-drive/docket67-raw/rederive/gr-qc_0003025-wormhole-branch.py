#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation / machine check for gr-qc/0003025 (Barcelo-Visser 2000),
the wormhole branch and its gate, as used by research/warp-drive/higgs.py.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  C1  sympy: BV eq. (2.8) -> (2.10), the ANEC integration by parts, is an identity.
  C2  sympy: the potential V drops out of T_mn k^m k^n (null contraction) for the
      nonminimal T_eff of eq. (2.3) in a general metric -> the gate is V-independent.
      (done in flat space with a general phi(x), where the G_mn phi^2 term is absent
      from T_eff by construction and the V term multiplies g_mn k^m k^n = 0.)
  C3  z3: BV case 1 (xi<0) and case 2 (xi>0, phi^2<kappa/xi): integrand
      kappa[kappa - xi(1-4xi)phi^2]/(kappa-xi phi^2)^2 > 0 -- no counterexample.
  C4  z3: BV case 3 remark: for xi in (0,1/4) and phi^2 > kappa/[xi(1-4xi)] the
      integrand numerator is negative (a witness exists); and for xi >= 1/4 the
      numerator is positive for all phi (so negativity needs xi<1/4, as BV say).
  C5  sympy: BV's exact gate |Phi| = 1/sqrt(6 xi), Phi = phi/sqrt(6 kappa)  ==>
      phi = sqrt(kappa/xi); with kappa = 1/(8 pi G) = M_red^2 (hbar=c=1) the gate is
      M_red/sqrt(xi) EXACTLY. BV's prose "~ m_p/sqrt(xi)" is the order-of-magnitude
      form; the owner's reduced-Planck substitution is the exact one.
  C6  numeric: xi_required = (M_red/v)^2 with CODATA G and PDG G_F; spread over the
      data's quoted uncertainties; and the literal-m_p reading for comparison.
  C7  sign convention: Bezrukov-Shaposhnikov (0710.3755) action -(M^2+xi_BS h^2)R/2,
      conformal at xi_BS = -1/6 (their footnote 1); BV action (1/2)(kappa - xi_BV phi^2)R,
      conformal at xi_BV = +1/6.  Matching the effective Planck mass gives
      xi_BV = -xi_BS.  Higgs inflation's xi_BS = 49000 sqrt(lambda) ~ +1.76e4 is
      xi_BV ~ -1.76e4: BV's case 1 (ANEC satisfied at every field value).
"""
import math
import sys

import sympy as sp
import z3

FAILS = []


def check(name, ok, detail=""):
    print("  [%s] %s %s" % ("PASS" if ok else "FAIL", name, detail))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- C1
lam, kap, xi = sp.symbols("lambda kappa xi", real=True)
phi = sp.Function("phi")(lam)
dphi = sp.diff(phi, lam)
den = kap - xi * phi**2
lhs = kap / den * (dphi**2 - 2 * xi * sp.diff(phi * dphi, lam))  # (2.8) integrand
rhs = (kap * (kap - xi * (1 - 4 * xi) * phi**2) / den**2 * dphi**2
       - sp.diff(2 * xi * kap / den * phi * dphi, lam))              # (2.10)
check("C1 BV (2.8) == (2.10) integrand (integration by parts)",
      sp.simplify(lhs - rhs) == 0)

# ---------------------------------------------------------------- C2
# flat-space T_eff (2.3) numerator: d_m phi d_n phi - 1/2 g (dphi)^2 - g V
#   - xi[2 d_m(phi d_n phi) - 2 g d^l(phi d_l phi)] ; contract with null k
t, x, y, z = sp.symbols("t x y z", real=True)
X = (t, x, y, z)
f = sp.Function("f")(*X)
Vs = sp.Function("V")(f)
g = sp.diag(-1, 1, 1, 1)
th, ph_ = sp.symbols("theta varphi", real=True)
k = [1, sp.sin(th) * sp.cos(ph_), sp.sin(th) * sp.sin(ph_), sp.cos(th)]
grad = [sp.diff(f, X[m]) for m in range(4)]
dsq = sum(g[m, m] * grad[m] ** 2 for m in range(4))
box = sum(g[m, m] * sp.diff(f * grad[m], X[m]) for m in range(4))
T = sp.zeros(4, 4)
for m in range(4):
    for n in range(4):
        T[m, n] = (grad[m] * grad[n] - sp.Rational(1, 2) * g[m, n] * dsq - g[m, n] * Vs
                   - xi * (2 * sp.diff(f * grad[n], X[m]) - 2 * g[m, n] * box))
Tkk = sp.expand(sum(T[m, n] * k[m] * k[n] for m in range(4) for n in range(4)))
check("C2 null k is null", sp.simplify(sum(g[m, m] * k[m] ** 2 for m in range(4))) == 0)
check("C2 V absent from T_eff k k (gate is potential-independent)",
      sp.simplify(sp.diff(Tkk, Vs)) == 0 and not sp.simplify(Tkk).has(Vs))

# ---------------------------------------------------------------- C3/C4 (z3)
K, XI, P2 = z3.Reals("K XI P2")  # kappa>0, xi, phi^2>=0
num = K - XI * (1 - 4 * XI) * P2
base = [K > 0, P2 >= 0]
s = z3.Solver()
s.add(base + [XI < 0, num <= 0])
check("C3 case 1 (xi<0): numerator > 0, no counterexample", s.check() == z3.unsat)
s = z3.Solver()
s.add(base + [XI > 0, XI * P2 < K, num <= 0])
check("C3 case 2 (xi>0, phi^2<kappa/xi): numerator > 0, no counterexample",
      s.check() == z3.unsat)
s = z3.Solver()
s.add(base + [XI > 0, XI < z3.RealVal("1/4"), P2 * XI * (1 - 4 * XI) > K, num >= 0])
check("C4 case 3, xi in (0,1/4), phi^2>kappa/[xi(1-4xi)] => numerator < 0 (unsat of >=0)",
      s.check() == z3.unsat)
s = z3.Solver()
s.add(base + [XI >= z3.RealVal("1/4"), num <= 0])
check("C4 xi>=1/4: numerator > 0 for every phi (negativity needs xi<1/4)",
      s.check() == z3.unsat)
# vacuity guard: case-3 hypotheses are satisfiable
s = z3.Solver()
s.add(base + [XI > 0, XI < z3.RealVal("1/4"), P2 * XI * (1 - 4 * XI) > K])
check("C4 vacuity guard: case-3 region is non-empty", s.check() == z3.sat)

# ---------------------------------------------------------------- C5
Phi_c, kk, xx, G_, pi = sp.symbols("Phi_c kappa xi G pi", positive=True)
phi_gate = sp.sqrt(6 * kk) / sp.sqrt(6 * xx)          # phi = sqrt(6 kappa) * Phi, Phi=1/sqrt(6xi)
check("C5 BV gate phi = sqrt(kappa/xi)", sp.simplify(phi_gate - sp.sqrt(kk / xx)) == 0)
Mred = sp.sqrt(1 / (8 * sp.pi * G_))                   # hbar=c=1
check("C5 kappa=1/(8 pi G) ==> gate = M_red/sqrt(xi) exactly",
      sp.simplify(sp.sqrt((1 / (8 * sp.pi * G_)) / xx) - Mred / sp.sqrt(xx)) == 0)
check("C5 kappa - xi phi^2 = 0 exactly at the gate (effective 1/G_eff -> 0)",
      sp.simplify(kk - xx * phi_gate**2) == 0)

# ---------------------------------------------------------------- C6
HBAR = 1.054571817e-34      # SI exact (2019)
C = 299792458.0             # exact
GEV = 1.602176634e-10       # exact
G_CODATA, dG = 6.67430e-11, 0.00015e-11       # CODATA 2018 (= 2022 value)
GF, dGF = 1.1663788e-5, 0.0000006e-5          # PDG 2024 G_F
def mpl(Gv): return math.sqrt(HBAR * C**5 / Gv) / GEV
def mred(Gv): return mpl(Gv) / math.sqrt(8 * math.pi)
def vev(gf): return 1 / math.sqrt(math.sqrt(2) * gf)
v = vev(GF)
xr = (mred(G_CODATA) / v) ** 2
print("      v = %.6f GeV   M_Pl = %.6e   M_red = %.6e GeV" % (v, mpl(G_CODATA), mred(G_CODATA)))
print("      v/M_red = %.6e   xi_required = (M_red/v)^2 = %.6e" % (v / mred(G_CODATA), xr))
lo = (mred(G_CODATA + dG) / vev(GF - dGF)) ** 2
hi = (mred(G_CODATA - dG) / vev(GF + dGF)) ** 2
print("      xi_required spread over 1-sigma(G, G_F): [%.6e, %.6e]  rel %.1e" % (lo, hi, (hi - lo) / xr))
check("C6 xi_required = 9.78e31 (tree 9.8e31)", abs(xr / 9.7829e31 - 1) < 1e-4)
check("C6 data spread moves xi_required < 1e-3 relative", (hi - lo) / xr < 1e-3)
xr_literal = (mpl(G_CODATA) / v) ** 2
print("      literal-'m_p' reading: (M_Pl/v)^2 = %.4e  (= 8 pi x exact = %.4e)" % (xr_literal, 8 * math.pi * xr))
check("C6 literal m_p reading differs by exactly 8 pi", abs(xr_literal / xr / (8 * math.pi) - 1) < 1e-12)
# a hypothetical v=246 vs 246.22 or M_red=2.4e18 (the tree's rounded prose value)
print("      with M_red rounded to 2.4e18: xi_required = %.4e" % ((2.4e18 / v) ** 2))

# ---------------------------------------------------------------- C7
xbs, xbv, M2, h = sp.symbols("xi_BS xi_BV M2 h", real=True)
sol = sp.solve(sp.Eq(M2 + xbs * h**2, M2 - xbv * h**2), xbv)
check("C7 matching effective Planck mass: xi_BV = -xi_BS", sol == [-xbs])
check("C7 conformal points map: xi_BS=-1/6 -> xi_BV=+1/6",
      sol[0].subs(xbs, sp.Rational(-1, 6)) == sp.Rational(1, 6))
MH, dMH = 125.20, 0.11                       # PDG 2024 m_H
lam_h = MH**2 / (2 * v**2)
xi_hi = 49000 * math.sqrt(lam_h)             # BS eq. (13), tree level
print("      lambda = m_H^2/(2v^2) = %.5f ; BS eq.(13) xi_BS = 49000 sqrt(lambda) = %.4e" % (lam_h, xi_hi))
print("      => xi_BV = %.4e : BV case 1 (xi<0), ANEC satisfied at EVERY field value;" % (-xi_hi))
print("         BV sect. 3.6: xi<0 solutions are naked singularities, no wormholes.")
check("C7 Higgs-inflation xi in BV convention is negative", -xi_hi < 0)
print("      magnitude-only comparison (the tree's): log10(xi_req/|xi_HI|) = %.2f"
      % math.log10(xr / xi_hi))
# the gate in BS normalisation: M^2 + xi_BS h^2 = 0 has no real h for xi_BS > 0
hh = sp.symbols("hh", real=True)
check("C7 BS sign, xi_BS>0: M^2 + xi_BS h^2 = 0 has no real solution (gate unreachable)",
      sp.solve(sp.Eq(1 + sp.Rational(17618) * hh**2, 0), hh) == [])

print()
print("RESULT:", "ALL PASS" if not FAILS else "FAIL: %s" % FAILS)
sys.exit(1 if FAILS else 0)
