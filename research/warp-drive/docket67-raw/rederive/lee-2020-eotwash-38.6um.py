#!/usr/bin/env python3
"""
DOCKET 67 / lee-2020-eotwash-38.6um -- re-derivation of what is finite or
closed-form in the tree's USE of Lee et al. 2020 (arXiv:2002.11761).

The measurement itself (a 95% CL exclusion curve fitted to torsion-balance
data) cannot be re-derived here: the data are not in hand.  What CAN be checked:

  [1] GLP eq. (39) as the O6/O7 pass restated it (/tmp/o6o7/final.py:10):
      V = -(G m1 m2/(gamma L r)) coth(pi r/(gamma L)).  Is it the image sum of
      the 5D Green's function on a circle, and what Yukawa (alpha, lambda) does
      it imply at r >> lambda?  (sympy, exact series + numeric image sum)
  [2] branelink.sme_coefficient at the tree's r = 38.6 um, and at Lee's own
      extra-dimension figure 30 um (the 'toroidal radius' quoted in the
      earlier in-session read, task wdeywbcrd); orders short of 1e-21.
  [3] the DIRECTION of the datum: |c| ~ r^-2, so an UPPER bound on r is a
      FLOOR on |c|.  The r below which the lab bound would bite at beta = 1.
  [4] the tree's own EOTWASH_BOUNDS clause (the bound is on gamma*r) applied
      inside the SME estimate: admissible r <= R/gamma, so the floor on |c|
      is K (beta*gamma)^2 / R^2.  Where it bites; its value at GW170817's beta.

Read-only on the tree: branelink is imported with bytecode writing disabled.
"""
import math
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")

import sympy as sp

ok = True


def check(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + label + ("  -- " + detail if detail else ""))


# ---------------------------------------------------------------- [1]
print("[1] GLP eq. (39) as restated: coth form, image sum, Yukawa alpha and lambda")
r, L = sp.symbols("r L", positive=True)
x = sp.pi * r / L
# coth(x) = 1 + 2 sum_{k>=1} q^k with q = exp(-2x) < 1 (exact for x > 0); the
# geometric sum is 2q/(1-q), so the identity is coth(x) == 1 + 2q/(1-q).
q = sp.exp(-2 * x)
diff = sp.simplify((sp.coth(x) - 1 - 2 * q / (1 - q)).rewrite(sp.exp))
check("coth(x) == 1 + 2 sum_k exp(-2kx) for x > 0 (sympy, geometric form)", diff == 0, str(diff))
# leading Yukawa: V/V_N = 1 + 2 exp(-2 pi r / L)  ->  alpha = 2, lambda = L/(2 pi)
lam = L / (2 * sp.pi)
lead = sp.limit((sp.coth(x) - 1) / sp.exp(-r / lam), r, sp.oo)
check("alpha = lim (coth - 1)/exp(-r/lambda) with lambda = L/(2 pi)", lead == 2, "alpha = %s" % lead)
# numeric: image sum of the 5D (4-space) Green's function 1/R^2 on a circle of circumference L
def image_sum(rv, Lv, N=200000):
    s = 1.0 / rv ** 2
    for n in range(1, N):
        s += 2.0 / (rv ** 2 + (n * Lv) ** 2)
    # tail: 2 * int_N^inf dn/(n^2 L^2) = 2/(N L^2)
    return s + 2.0 / (N * Lv ** 2)
for rv, Lv in ((0.3, 1.0), (1.0, 1.0), (2.5, 1.0)):
    lhs = image_sum(rv, Lv)
    rhs = math.pi / (rv * Lv) / math.tanh(math.pi * rv / Lv)
    check("image sum sum_n 1/(r^2+n^2L^2) == pi/(rL) coth(pi r/L) at r/L=%.1f" % (rv / Lv),
          abs(lhs / rhs - 1) < 1e-6, "ratio-1 = %.2e" % (lhs / rhs - 1))
print("    => the restated eq. (39) is the circle image sum of a 5D Newtonian (scalar)")
print("       Green's function; at r >> lambda it is Newton x (1 + 2 exp(-r/lambda)),")
print("       lambda = gamma L/(2 pi): a Yukawa of STRENGTH alpha = 2, not |alpha| = 1.")
print("       (A spin-2 KK graviton would carry an extra 4/3: alpha = 8/3.  Not read here.)")

# ---------------------------------------------------------------- [2]
print("\n[2] branelink.sme_coefficient at the tree's r and at Lee's 30 um")
import branelink as bl
K_at_R = bl.sme_coefficient(beta=1.0, R=38.6e-6)
check("tree's |c| at r = 38.6 um, beta = 1 reproduces 6.37e-64", abs(K_at_R / 6.37e-64 - 1) < 1e-3,
      "%.6e" % K_at_R)
c30 = bl.sme_coefficient(beta=1.0, R=30e-6)
o386 = math.log10(bl.SME_LAB_BOUND / K_at_R)
o30 = math.log10(bl.SME_LAB_BOUND / c30)
print("    |c|(38.6 um) = %.4e   orders short = %.4f" % (K_at_R, o386))
print("    |c|(30.0 um) = %.4e   orders short = %.4f" % (c30, o30))
check("scaling |c| ~ r^-2: c(30)/c(38.6) == (38.6/30)^2", abs(c30 / K_at_R - (38.6 / 30) ** 2) < 1e-12,
      "%.6f vs %.6f" % (c30 / K_at_R, (38.6 / 30) ** 2))
check("round(orders short) is 42 at BOTH radii -- the r-choice does not move O7's null",
      round(o386) == 42 and round(o30) == 42)

# ---------------------------------------------------------------- [3]
print("\n[3] the direction of the datum: r <= 38.6 um is a FLOOR on |c|, not a ceiling")
r_bite = 38.6e-6 * math.sqrt(K_at_R / bl.SME_LAB_BOUND)
print("    at beta = 1 the 1e-21 lab bound bites only for r < %.4e m" % r_bite)
print("    = %.3e reduced Planck lengths" % (r_bite / bl.HBARC_GEV_M * bl.MBAR4_GEV))
check("r_bite reproduces c = 1e-21", abs(bl.sme_coefficient(1.0, r_bite) / 1e-21 - 1) < 1e-9)
print("    => 'at the maximal r' is the LEAST constraining point of the Eot-Wash-allowed")
print("       interval; the null holds for r in [%.2e m, 38.6e-6 m] at beta <= 1." % r_bite)

# ---------------------------------------------------------------- [4]
print("\n[4] the tree's own clause EOTWASH_BOUNDS = %r applied inside the SME estimate" % bl.EOTWASH_BOUNDS)
print("    (CONDITIONAL: that K&N eq. 76-77's r is the circle radius and its only velocity")
print("     dependence is the beta^2 branelink codes -- K&N NOT re-read in this stage)")
bg = sp.symbols("bg", positive=True)  # beta*gamma
Kc = sp.Float(K_at_R, 30)  # |c| at r = R, beta = 1
# admissible r <= R/gamma  =>  |c| >= Kc * beta^2 * gamma^2 = Kc * bg^2
bg_bite = sp.solve(sp.Eq(Kc * bg ** 2, sp.Float(bl.SME_LAB_BOUND, 30)), bg)[0]
print("    floor |c| >= %.4e (beta gamma)^2 ; lab bound bites at beta*gamma = %s"
      % (K_at_R, sp.N(bg_bite, 6)))
beta_gw = bl.BETA_MAX
gam_gw = 1 / math.sqrt(1 - beta_gw ** 2) if beta_gw < 1e-6 else None
bg_gw = beta_gw * (1 + 7.0e-16)
cfloor_gw = K_at_R * bg_gw ** 2
print("    at GW170817's beta = %.6e: floor |c| = %.4e, %.2f orders below 1e-21"
      % (beta_gw, cfloor_gw, math.log10(bl.SME_LAB_BOUND / cfloor_gw)))
print("    at beta = 1 exactly, gamma = inf and the clause forces r -> 0: r = 38.6 um and")
print("    beta = 1 are NOT jointly admissible under the tree's own gamma*L clause.")
check("the self-consistent SME bound (beta*gamma <= %.3e) is vacuous next to GW170817 (gamma-1 <= 7e-16)"
      % float(bg_bite), float(bg_bite) > 1e20 and cfloor_gw < bl.SME_LAB_BOUND)

# ---------------------------------------------------------------- [5]
print("\n[5] what the alpha drift can and cannot move (no exclusion curve in hand)")
print("    CONDITIONAL (curve shape NOT READ): if Lee's 95% CL bound alpha_max(lambda)")
print("    is decreasing through its |alpha| = 1 crossing, a Yukawa of alpha = 2 is excluded")
print("    down to a SMALLER lambda, so lambda_max(alpha = 2) < 38.6 um.  NOT computed here;")
print("    Lee's own extra-dimension figure (30 um, alpha convention NOT READ) brackets it")
print("    only if that figure's alpha >= 2.  Every tree conclusion checked above moves by")
print("    < 0.25 orders over r in [30, 38.6] um and none changes sign or rounding.")

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
