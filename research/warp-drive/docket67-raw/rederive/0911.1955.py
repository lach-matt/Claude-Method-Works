"""DOCKET 67 re-derivation for 0911.1955 (Fixsen 2009, T_0 = 2.72548 +/- 0.00057 K).
Read-only on the tree: imports permute / massform / nopath from research/warp-drive, writes nothing there.
Checks
 R1  permute section 3: T_rec/T_0 = T_0(1+z)/T_0 is 1+z IDENTICALLY (sympy) -- T_0 cancels.
 R2  numeric: 2.7255 * 1090.92 = 2973.3 K (permute.py:66-68, 427)
 R3  rounding: Fixsen's 2.72548 rounds to the tree's 2.7255 at 4 dp; offset in sigma.
 R4  Landauer at T_0: k_B T ln2 = 2.608e-23 J (massform.py:456); bit count 2.4120e41 and its
     movement under every T_0 value in play (Fixsen combined, FIRAS-recal, non-FIRAS compilation,
     values quoted in restatements only -- flagged).
 R5  massform 'ratio of section 3' (2 pi R k_B T/(hbar c)) is linear in T (sympy) -- confirms
     massform.py:910-911 as written (it refers to massform's OWN section 3, not permute's).
 R6  z_rec is NOT from Fixsen: Planck z_* is a fit conditional on a fixed T_0; the tree's 1090.92
     would move only through that fit, and permute's arithmetic cannot see T_0 at all.
"""
import math, sys
import sympy as sp
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
out = []
def rec(tag, ok, msg):
    out.append((tag, ok, msg)); print(("PASS " if ok else "FAIL ") + tag + ": " + msg)

# R1
T0, z, Trec = sp.symbols("T0 z T_rec", positive=True)
ratio = (T0 * (1 + z)) / T0
rec("R1", sp.simplify(ratio - (1 + z)) == 0 and sp.diff(ratio, T0) == 0,
    "T0(1+z)/T0 - (1+z) = %s ; d/dT0 = %s  -> the 1090.92 carries NO dependence on T_CMB"
    % (sp.simplify(ratio - (1 + z)), sp.simplify(sp.diff(ratio, T0))))
# physical alternative: T_rec fixed by atomic physics, then 1+z = T_rec/T0, d ln(1+z)/d ln T0 = -1
alt = Trec / T0
rec("R1b", sp.simplify(sp.diff(sp.log(alt), T0) * T0) == -1,
    "if instead T_rec is held (atomic physics) then 1+z = T_rec/T0 and dln(1+z)/dlnT0 = -1 (inverse, not linear)")

import permute
rec("R1c", permute.ratio_from_temperature(1089.92, 2.0) == permute.ratio_from_temperature(1089.92, 3.0)
    or abs(permute.ratio_from_temperature(1089.92, 2.0) - permute.ratio_from_temperature(1089.92, 3.0)) < 1e-12,
    "permute.ratio_from_temperature(T0=2 K) = %.12f, (T0=3 K) = %.12f -- identical"
    % (permute.ratio_from_temperature(1089.92, 2.0), permute.ratio_from_temperature(1089.92, 3.0)))

# R2
Tr = permute.T_CMB * (1 + permute.Z_REC)
rec("R2", abs(round(Tr, 1) - 2973.3) < 1e-9 and abs((1 + permute.Z_REC) - 1090.92) < 1e-9,
    "T_CMB=%.4f, Z_REC=%.2f, T_rec=%.4f K (printed 2973.3), 1+z=%.2f" % (permute.T_CMB, permute.Z_REC, Tr, 1 + permute.Z_REC))

# R3
F, sF = 2.72548, 0.00057
rec("R3", round(F, 4) == permute.T_CMB,
    "round(2.72548,4)=%.4f == tree %.4f ; offset %.5f K = %.3f sigma" % (round(F, 4), permute.T_CMB, permute.T_CMB - F, (permute.T_CMB - F) / sF))

# R4
import nopath, massform
kB = 1.380649e-23
e_bit = kB * permute.T_CMB * math.log(2)
rec("R4a", abs(e_bit - nopath.landauer_energy(1.0, permute.T_CMB)) / e_bit < 1e-9 and f"{e_bit:.3e}" == "2.608e-23",
    "k_B T ln2 = %.6e J (nopath %.6e), printed 2.608e-23" % (e_bit, nopath.landauer_energy(1.0, permute.T_CMB)))
N = massform.landauer_bits()
E = massform.rest_energy_j()
rec("R4b", f"{N:.4e}" == "2.4120e+41", "Mc^2 = %.6e J (M = %.4f kg); bits = %.6e (printed 2.4120e41)" % (E, E / 299792458.0**2, N))
cases = [("tree 2.7255", 2.7255), ("Fixsen combined 2.72548 (abstract, via restatement)", 2.72548),
         ("Fixsen +1 sigma 2.72605", 2.72605), ("Fixsen -1 sigma 2.72491", 2.72491),
         ("FIRAS recal. via WMAP 2.7260 (abstract, via restatement)", 2.7260),
         ("non-FIRAS compilation 2.729 (search restatement only)", 2.729)]
for name, T in cases:
    n = massform.landauer_bits(T=T)
    print("      %-55s bits = %.5e  (%+.4f %% vs tree; 5-sig-fig print %s)" % (name, n, 100 * (n / N - 1), f"{n:.4e}"))
n_hi, n_lo = massform.landauer_bits(T=2.72605), massform.landauer_bits(T=2.72491)
nF = massform.landauer_bits(T=2.72548)
rec("R4c", f"{nF:.4e}" == "2.4121e+41" and f"{N:.4e}" == "2.4120e+41",
    "PRECISION NOTE (discrepancy of digits, not of physics): at Fixsen's unrounded 2.72548 the count is %.6e, printing 2.4121e41 not the tree's 2.4120e41; the 1-sigma band %.4e..%.4e (+/-0.021 %%) spans the 4th-5th digit, so the tree's fifth significant figure is below the input's precision" % (nF, n_hi, n_lo))

# R5
R, k, hb, c = sp.symbols("R k_B hbar c", positive=True)
T = sp.symbols("T", positive=True)
bl = 2 * sp.pi * R * k * T / (hb * c)
rec("R5", sp.diff(bl, T, 2) == 0 and sp.simplify(bl.subs(T, 2 * T) / bl) == 2,
    "2 pi R k_B T/(hbar c) is linear in T: massform.py:910-911 'moves linearly with T' is CORRECT for massform's section-3 ratio; value at tree T = %.6e"
    % massform.bek_over_landauer_closed())

# R6 -- documentary: nothing numeric to compute; record
rec("R6", True, "Z_REC=1089.92 is labelled 'Planck 2018' (permute.py:179); it is not an input of Fixsen 2009 and Fixsen's number cannot move it through permute's arithmetic (R1).")

# R7 robustness of the obstruct/permute verdict (ratio != 1) to ANY T_0 in a deliberately wide band
lo, hi = 2973.3025 / 3.0, 2973.3025 / 2.4
rec("R7", lo > 100 and hi > 100,
    "holding T_rec = 2973.3 K (atomic physics) and letting T_0 range over [2.4, 3.0] K (about -12 %%/+10 %% around 2.7255; no tension value was READ here) gives 1+z in [%.1f, %.1f]; the verdict needs only 1+z != 1" % (lo, hi))

bad = [t for t, ok, _ in out if not ok]
print("\nRESULT:", "ALL PASS" if not bad else "FAIL " + ",".join(bad))
sys.exit(1 if bad else 0)
