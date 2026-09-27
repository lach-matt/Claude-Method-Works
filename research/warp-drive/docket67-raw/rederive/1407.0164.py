#!/usr/bin/env python3
"""D67 audit 1407.0164 (Godun et al. 2014, PRL 113 210801) -- re-derivation.

Inputs are the numbers PRINTED in 1407.0164v2 (page text cached verbatim in
scratchpad/d67/src/1407.0164.cached.txt) and the tree's own address.py, imported
READ-ONLY (nothing under research/ is written).  Every check prints PASS/FAIL or
INFO; exit 1 on any FAIL.
"""
import math, sys
from decimal import Decimal, getcontext
import sympy as sp
getcontext().prec = 40
fails = []
def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok: fails.append(label)
def info(label, detail): print("INFO " + label + "  " + detail)
q = lambda *xs: math.sqrt(sum(x * x for x in xs))

# ---------------------------------------------------------------- A. Table I / II arithmetic
print("A. Table I and Table II quadrature (units 1e-16)")
E2 = [2.91, 0.99, 0.13, 0.77, 0.41, 0.02, 0.07, 0.06, 0.07]
E3 = [0.06, 0.45, 0.03, 0.04, 0.09, 0.20, 0.08, 0.06, 0.08]
R  = [2.97, 1.09, 0.11, 0.80, 0.33, 0.20, 0.11, 0.09, 0.0]  # '<0.01' taken as 0
T2 = [0.16, 0.10, 1.90, 1.00]
for lab, rows, printed in (("E2 subtotal", E2, 3.19), ("E3 subtotal", E3, 0.52),
                           ("ratio subtotal", R, 3.29), ("Table II subtotal", T2, 2.16)):
    v = q(*rows); check(lab + " = %.2f (printed %.2f)" % (v, printed), abs(v - printed) <= 0.011)
tot = {"E2": q(3.19, 2.16, 4.77), "E3": q(0.52, 2.16, 5.35), "ratio": q(3.29, 0.68)}
for k, printed in (("E2", 6.13), ("E3", 5.79), ("ratio", 3.36)):
    check("%s TOTAL = %.3f (printed %.2f)" % (k, tot[k], printed), abs(tot[k] - printed) <= 0.011)
# shifts: subtotal sums
check("E2 shift subtotal 70.49", abs(sum([0, -4.86, 0, 75.76, -0.41, 0, 0, 0, 0]) - 70.49) < 1e-9)
check("E3 shift subtotal -4.31", abs(sum([0, -0.98, 0, -3.24, -0.09, 0, 0, 0, 0]) - (-4.31)) < 1e-9)
check("E2 TOTAL shift 69.68 = 70.49 - 0.81", abs(70.49 - 0.81 - 69.68) < 1e-9)
check("E3 TOTAL shift -5.12 = -4.31 - 0.81", abs(-4.31 - 0.81 + 5.12) < 1e-9)

# ---------------------------------------------------------------- B. printed digits
print("B. printed values and their stated uncertainties")
r = Decimal("0.93282940453096465"); ur = Decimal("31e-17")
nE3, uE3 = Decimal("642121496772644.91"), Decimal("0.37")
nE2, uE2 = Decimal("688358979309308.42"), Decimal("0.42")
fr, f3, f2 = float(ur / r), float(uE3 / nE3), float(uE2 / nE2)
info("fractional unc from digits", "ratio %.3e, E3 %.3e, E2 %.3e" % (fr, f3, f2))
check("ratio digits (31) ~ 3e-16 as printed on p.1", 2.5e-16 < fr < 3.5e-16)
check("absolute digits ~ 6e-16 as printed in abstract", 5.5e-16 < f3 < 6.5e-16 and 5.5e-16 < f2 < 6.5e-16)
rabs = nE3 / nE2
dev = float((rabs - r) / r)
sig = math.sqrt(f3 ** 2 + f2 ** 2)  # upper bound: ignores the correlated Table II part
info("abs-frequency ratio vs direct ratio", "nuE3/nuE2 from absolutes = %s ; fractional diff %.2e" % (str(rabs)[:22], dev))
check("absolute frequencies consistent with direct ratio (|diff| < 1 sigma of absolutes)", abs(dev) < sig,
      "|diff| = %.2e vs %.2e" % (abs(dev), sig))

# ---------------------------------------------------------------- C. CS_CHANNEL_COARSER_BY
print("C. the tree's CS_CHANNEL_COARSER_BY = GODUN_ABS_UNC / GODUN_RATIO_UNC")
info("printed rounded 6e-16/3e-16", "%.3f" % (6.0 / 3.0))
info("Table I TOTALs", "E2 6.13/3.36 = %.3f ; E3 5.79/3.36 = %.3f" % (6.13 / 3.36, 5.79 / 3.36))
info("printed digits", "E2 %.3f ; E3 %.3f" % (f2 / fr, f3 / fr))
check("factor is ~2 (between 1.5 and 2.5), NOT ~100 -- the W10 correction stands",
      all(1.5 < x < 2.5 for x in (2.0, 6.13 / 3.36, 5.79 / 3.36, f2 / fr, f3 / fr)))
check("but the exact '2' is a rounding of the printed 6 and 3 (table gives 1.72-1.82)",
      abs(6.13 / 3.36 - 2) > 0.1 and abs(5.79 / 3.36 - 2) > 0.2)

# ---------------------------------------------------------------- D. what limits the 6e-16
print("D. composition of the absolute-frequency uncertainty")
for k, stat in (("E2", 4.77), ("E3", 5.35)):
    t = tot[k]
    info(k, "statistical %.2f of total %.2f -> %.0f%% of variance; Cs fountain systematics 1.90 -> %.0f%%"
         % (stat, t, 100 * stat ** 2 / t ** 2, 100 * 1.90 ** 2 / t ** 2))
# ratio statistical 0.68 from the same ion over the same run bounds the optical part of the
# absolute statistics; the rest is the Cs reference chain (inference, labelled as such)
for k, stat in (("E2", 4.77), ("E3", 5.35)):
    info(k + " share of absolute statistical variance NOT explained by optical noise (>=)",
         "%.1f%%" % (100 * (stat ** 2 - 0.68 ** 2) / stat ** 2))
check("absolute unc is dominated by the Cs-referenced statistics, not by Cs systematics",
      4.77 > 2 * 1.90 and 5.35 > 2 * 1.90)

# ---------------------------------------------------------------- E. the B coefficients
print("E. B_opt = 0 is 'negligible', not zero: order of the reduced-mass term for 171Yb+")
me_over_mp = 1 / 1836.15267343
M_over_mp = 171 * 1.0073  # crude, nucleon masses; order only
B_nms = (me_over_mp / M_over_mp) / (1 + me_over_mp / M_over_mp)
info("normal-mass-shift d ln nu / d ln mu", "%.2e  (specific mass shift same order, not computed)" % B_nms)
check("|B_opt| from recoil << 1 = |B_Cs| (Godun's 'negligible')", B_nms < 1e-4)

print("F. A_Cs = 2 + 0.83: Casimir relativistic factor for an s1/2 hyperfine level")
Z, al = sp.symbols("Z alpha", positive=True)
lam = sp.sqrt(1 - (Z * al) ** 2)
Frel = 3 / (lam * (4 * lam ** 2 - 1))
dlnF = sp.simplify(sp.diff(sp.log(Frel), al) * al)
ALPHA = 1 / 137.035999084
vCs = float(dlnF.subs({Z: 55, al: ALPHA}))
vH = float(dlnF.subs({Z: 1, al: ALPHA}))
vHg = float(dlnF.subs({Z: 80, al: ALPHA}))
info("d ln F_rel / d ln alpha", "Z=1 %.2e ; Z=55 (Cs) %.4f ; Z=80 %.3f" % (vH, vCs, vHg))
check("Casimir estimate for Cs is O(1) and below the published many-body 0.83 by ~11%",
      0.70 < vCs < 0.80, "Casimir %.3f vs published remainder 0.83" % vCs)
check("the tree's 'remainder 0.83' is 2.83 - 2 arithmetic, not a derivation",
      abs((2.83 - 2.0) - 0.83) < 1e-12)

# ---------------------------------------------------------------- G. the tree's use
print("G. the tree (address.py, imported read-only)")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import address as a
check("GODUN dict equals the printed p.4 coefficients",
      a.GODUN == {"A_E3": -5.95, "A_E2": 0.88, "A_Cs": 2.83, "B_E3": 0.0, "B_E2": 0.0, "B_Cs": -1.0})
check("GODUN_RATIO_UNC = 3e-16 and GODUN_ABS_UNC = 6e-16 (as printed)",
      a.GODUN_RATIO_UNC == 3e-16 and a.GODUN_ABS_UNC == 6e-16)
S = 0.06
KaH1 = a.K_alpha("H1")
for h in ("H1", "H2"):
    Kmu = a.K_mu(S, h); Ka = a.K_alpha(h)
    base = a.eps_det_stationary(h)
    info(h + " tree eps_det (B-only, 6e-16)", "%.4e  |K_mu| = %.4f" % (base, abs(Kmu)))
    for lab, dA in (("E3/Cs", -5.95 - 2.83), ("E2/Cs", 0.88 - 2.83)):
        full = dA * Ka + 1.0 * Kmu  # Godun's full linear relation, dB = 0 - (-1) = +1
        info("  %s with Godun's alpha term too" % lab,
             "k = %.5f -> eps_det %.4e (%.2f%% from tree)" % (full, 6e-16 / abs(full), 100 * (abs(full) / abs(Kmu) - 1)))
    # g_Cs quark-mass sensitivity, exponent kappa_q ~ 0.009 (search snippet of physics/0309107, NOT READ);
    dlnXq = 1 - float(a.dln_lambda_dln_v()) if h == "H1" else 1.0
    for kq in (0.009, -0.009):
        full = -8.78 * Ka + Kmu - kq * dlnXq
        info("  E3/Cs + g_Cs term kappa_q=%+.3f" % kq, "eps_det moves %.2f%%" % (100 * (abs(Kmu) / abs(full) - 1)))
    ratio = a.EPS_NUCLEAR_OVER_DET[h]
    worst = ratio * (1 - 0.035)
    check("  EPS_NUCLEAR_OVER_DET[%s] = %.1f stays >> 1 under a 3.5%% sensitivity shift (%.1f)" % (h, ratio, worst), worst > 10)
# A_E2 value: 0.88 printed by Godun (ref [35], DFM 2003); 1.00 appears in later Yb+ analyses
# (search snippet only, NOT READ).  Effect on the optical/optical alpha row:
for AE2 in (0.88, 1.00):
    dA = AE2 - (-5.95)
    info("A_E2 = %.2f" % AE2, "dA = %.2f; optical/optical k(H1) = %.5f; eps_det_alpha = %.4e; F7 sign-flip value %.5f"
         % (dA, dA * KaH1, 3e-16 / (dA * KaH1), dA * -a.K_alpha_as_first_written("H1")))
check("A_E2 0.88 -> 1.00 moves the optical/optical eps_det by < 2%", abs(6.83 / 6.95 - 1) < 0.02)
check("RULING_F7_IS_THE_SIGN_FLIP reproduces with Godun's printed 0.88 (the tree's input)",
      a.rounds_to_printed(6.83 * -a.K_alpha_as_first_written("H1"), "+0.0682"))
check("CS_CHANNEL_COARSER_BY in tree = 2.0", a.CS_CHANNEL_COARSER_BY == 2.0)

print("H. later value of the same ratio (Lange et al. 2021, PRL 126 011102 = arXiv:2010.06620;")
print("   value from a web-search abstract summary ONLY -- NOT READ at source)")
rL, uL = Decimal("0.932829404530965376"), Decimal("32e-18")
d = float((rL - r) / r)
s = math.sqrt(float(ur / r) ** 2 + float(uL / rL) ** 2)
info("Lange 2021 - Godun 2014", "fractional %.3e = %.2f combined sigma (Godun digits sigma %.2e; Table-I 3.36e-16 -> %.2f sigma)"
     % (d, d / s, float(ur / r), d / 3.36e-16))
check("difference is a recorded 2-3 sigma discrepancy in the ratio VALUE, which the tree does not use", 2.0 < d / s < 3.0)

print()
print("ALL CHECKS PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
