#!/usr/bin/env python3
"""
D67 re-derivation: le-2026-warpshell-marginal-wall.

Claim as the tree uses it (wall.py:5-9, 362-368, 565-577; warpshell.py:67-80):
  Le's realized tangential-pressure wall sits exactly on V''(R)=0 (neutral radial
  zero mode, e-folds in ~ a light-crossing time); taking tau_efold ~ R/c and
  tau_burn = c*deta/a gives deta <= lambda = aR/c^2, and 1 g, 10 m, deta = 0.2
  fails by 1.8e14.

What is checked here (sympy + numeric):
  A. Lanczos statics for Minkowski-in / Schwarzschild-out (the tree's statics()).
  B. MECHANISM for "sits exactly on V''=0": the slope dp0/dsigma0 along the static
     family at FIXED m equals wall.py's beta^2_crit(x) identically.  So a wall whose
     surface law is the static-family law is exactly marginal, and every nearby radius
     is itself an equilibrium (V = V' = 0 for all R) -> a NEUTRAL zero mode.
     (Whether Le's realized wall has that law is his App. J, NOT read here.)
  C. A neutral zero mode of R_ddot = -V'/2 with V'' = 0 grows LINEARLY, not
     exponentially: tau_efold = sqrt(2/|V''|) diverges at V'' = 0.  An e-folding rate
     needs V'' < 0, which Le attributes to the frozen-background rear-pole redshift,
     i.e. to the burn (lambda != 0).
  D. The tree's arithmetic: lambda(1 g, 10 m), 0.2/lambda, Le App. K 0.24/0.12.
  E. Sensitivity of the 1.8e14 to the UNREAD lambda-scaling of |V''|: if
     |V''| R^2 = k lambda^p, anchored so tau_efold = R/c at Le's lambda_max = 0.12,
     the shortfall deta/deta_max at 1 g, 10 m for p = 0, 1, 2, 3.
     p = 0 is the tree's assumption; continuity of V''(lambda) with V''(0) = 0
     excludes p = 0 with finite k.
"""
import math
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

R, m = sp.symbols("R m", positive=True)
s = sp.sqrt(1 - 2 * m / R)

# A. Lanczos (G = c = 1), Poisson-Visser eq (8) form with [K] = K_out - K_in:
#    K^th_th = s/R (out), 1/R (in);  K^t_t = (m/R^2)/s (out), 0 (in)
Kth = s / R - 1 / R
Ktt = (m / R**2) / s
sigma0 = -Kth / (4 * sp.pi)
p0 = (Ktt + Kth) / (8 * sp.pi)
tree_sigma = (1 - s) / (4 * sp.pi * R)
tree_p = (1 - s) ** 2 / (16 * sp.pi * R * s)
chk("A1 sigma0 == tree statics()", sp.simplify(sigma0 - tree_sigma) == 0)
num = {m: sp.Rational(3, 20), R: 1}   # x = 0.3
chk("A2 p0 == tree statics() (symbolic diff at x=0.3 and generic)",
    abs(float((p0 - tree_p).subs(num))) < 1e-15 and
    abs(float((p0 - tree_p).subs({m: sp.Rational(1, 7), R: 2}))) < 1e-15)

# B. family slope at fixed m
beta2_family = sp.diff(p0, R) / sp.diff(sigma0, R)
x = sp.symbols("x", positive=True)
S = sp.sqrt(1 - x)
beta2_crit_tree = (1 - S) * (3 * S**2 + 2 * S + 1) / (4 * S**2 * (1 + 3 * S))
maxdiff = 0.0
for xv in [1e-6, 1e-3, 0.05, 0.1, 0.3, 0.5, 2/3, 0.8, 0.9, 0.95]:
    xr = sp.nsimplify(xv, rational=True)   # exact x; evaluate at 50 digits (1-s cancels at small x)
    bf = float(beta2_family.subs({m: xr / 2, R: 1}).evalf(50))
    bc = float(beta2_crit_tree.subs(x, xr).evalf(50))
    maxdiff = max(maxdiff, abs(bf - bc) / max(abs(bc), 1e-30))
print("   max rel |beta2_family - beta2_crit| over x in [1e-6, 0.95] = %.3e" % maxdiff)
chk("B1 dp0/dsigma0 at fixed m == beta^2_crit(x) (wall.py:281-284)", maxdiff < 1e-12)
# symbolic identity via s: R = 2m/(1-s^2)
ss = sp.symbols("s", positive=True)
bf_s = sp.simplify(beta2_family.subs(R, 2 * m / (1 - ss**2)))
bc_s = (1 - ss) * (3 * ss**2 + 2 * ss + 1) / (4 * ss**2 * (1 + 3 * ss))
chk("B2 identity holds symbolically in s", sp.simplify(bf_s - bc_s) == 0)

# B3. With that law every radius is an equilibrium: V(R) = 1 - (ms/2R + m/ms)^2
#     evaluated on the static family (sigma(R) = sigma0(R) at fixed m) vanishes identically.
ms = 4 * sp.pi * R**2 * sigma0
V = 1 - (ms / (2 * R) + m / ms) ** 2
Vs = sp.simplify(V.subs(R, 2 * m / (1 - ss**2)))
chk("B3 V(R) == 0 for all R on the static-family law (neutral zero mode)", sp.simplify(Vs) == 0)

# C. linear vs exponential at V'' = 0
#    R_ddot = -V''(R0) (R-R0)/2 ; V''=0 -> R-R0 = v0 t (linear)
t, v0, w = sp.symbols("t v0 w", positive=True)
sol0 = v0 * t
chk("C1 V''=0: displacement v0*t solves R_ddot = 0 (linear drift, no e-folding)",
    sp.diff(sol0, t, 2) == 0)
#    V'' = -w^2*2 <0 -> growth rate w, tau_efold = 1/w = sqrt(2/|V''|)
Vpp_neg = -2 * w**2
tau = sp.sqrt(2 / sp.Abs(Vpp_neg))
chk("C2 tau_efold = sqrt(2/|V''|) = 1/w, diverges as V''->0",
    sp.simplify(tau - 1 / w) == 0 and sp.limit(tau, w, 0, "+") == sp.oo)

# D. arithmetic
C = 299792458.0
g0 = 9.80665
lam = g0 * 10.0 / C**2
sf = 0.2 / lam
print("   lambda(1 g, 10 m) = %.6e ; 0.2/lambda = %.6e" % (lam, sf))
chk("D1 shortfall 1.8e14 as printed (wall.py:5-9)", abs(sf / 1.8e14 - 1) < 0.02)
chk("D2 Le App. K: 0.24/0.12 = 2.0 (warpshell.py:72)", abs(0.24 / 0.12 - 2.0) < 1e-12)

# E. sensitivity to the unread lambda-scaling of |V''|
lam0 = 0.12
print("   p   k            tau_efold(1g,10m)/(R/c)   deta_max      shortfall 0.2/deta_max")
res = {}
for p in (0, 1, 2, 3):
    k = 2.0 / lam0**p                      # tau_efold = R/c at lambda0
    tau_s = math.sqrt(2.0 / (k * lam**p))  # units R/c
    deta_max = lam * tau_s                 # tau_burn = c deta / a  -> deta = lambda * tau/(R/c)
    res[p] = 0.2 / deta_max
    print("   %d   %-11.4g  %-24.4e  %-12.4e  %.4e" % (p, k, tau_s, deta_max, res[p]))
chk("E1 p=0 reproduces the tree's 1.8e14", abs(res[0] / sf - 1) < 1e-12)
chk("E2 p=1 (generic first-order redshift) shortfall ~1.7e7, still > 1", 1e7 < res[1] < 3e7)
chk("E3 p=2 shortfall 1.67, still > 1 (fails by the same factor as Le's own burn)",
    abs(res[2] - 0.2 / 0.12) < 1e-9)
chk("E4 p=3 passes (<1): the SIGN of the verdict is not fixed without App. J", res[3] < 1)
chk("E5 every p>0 gives a smaller shortfall than the tree's p=0", all(res[q] < res[0] for q in (1, 2, 3)))

print("\nOVERALL:", "ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
