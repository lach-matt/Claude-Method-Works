#!/usr/bin/env python3
"""DOCKET 67 re-derivation: xi_required = (M_red/phi)^2 at phi = 2e16 GeV.

Independent of the tree's arithmetic (constants retyped from CODATA 2022,
arXiv:2409.03787 Table XXXIII, READ), then cross-checked against the tree's
own higgs.py / xigate.py by import (read-only; nothing under research/ is
written).  Exits 1 if any assertion fails.

Sources READ for the symbolic content:
  Barcelo-Visser gr-qc/0003025 eq (2.1): S = (1/2) int kappa R + int(-1/2 (dphi)^2
      - V - 1/2 xi R phi^2), kappa = 1/(8 pi G_N); eq (2.3) prefactor
      kappa/(kappa - xi phi^2); sect 2.3 case 3: xi>0 and phi^2 > kappa/xi.
      Conformal coupling is xi = +1/6 (abstract, sect 1).
  Bezrukov-Shaposhnikov 0710.3755 eq (2): -(M^2 + xi h^2)/2 R, H = h/sqrt2;
      footnote 1: "In our notations the conformal coupling is xi = -1/6";
      eq (13): xi ~ 49000 sqrt(lambda) = 49000 m_H/(sqrt2 v); h_end ~ 1.07 M_P/sqrt(xi),
      h_COBE ~ 9.4 M_P/sqrt(xi); M_P = (8 pi G)^-1/2 = 2.4e18 GeV.
  Nath & Fileviez Perez hep-ph/0601023 eq (2): M_G ~ 2e16 GeV, MSSM unification,
      "presented here as empirical"; SM couplings do not unify (Fig 7, eq 156);
      MSSM unification at ~1e16 "if the supersymmetric particles are around 1 TeV";
      non-SUSY SU(5) extensions "slightly above 1e14 GeV".
"""
import math
import sys
import sympy as sp

FAIL = []


def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------- 1. symbolic
kappa, xi, phi, G, Mred, M, h, xiBS, xiBV = sp.symbols(
    "kappa xi phi G M_red M h xi_BS xi_BV", real=True)
# BV eq (2.3): effective prefactor kappa/(kappa - xi phi^2); critical where denominator vanishes
crit = sp.solve(sp.Eq(kappa - xi * phi ** 2, 0), phi ** 2)
chk("BV critical phi^2 = kappa/xi", sp.simplify(crit[0] - kappa / xi) == 0)
# kappa = 1/(8 pi G) = M_red^2 in hbar=c=1 (definition of the reduced Planck mass)
xi_req = sp.solve(sp.Eq(kappa - xi * phi ** 2, 0), xi)[0].subs(kappa, 1 / (8 * sp.pi * G))
chk("xi_required = 1/(8 pi G phi^2) = (M_red/phi)^2",
    sp.simplify(xi_req - (Mred / phi) ** 2).subs(Mred, 1 / sp.sqrt(8 * sp.pi * G)) == 0)
# Sign map BV <-> BS.  BS effective 'Planck mass squared' multiplying R/2: M^2 + xi_BS h^2.
# BV: coefficient multiplying R/2 (after moving the xi term): kappa - xi_BV phi^2.
# Same physical quantity (the effective 1/(8 pi G_eff)), with phi = h (both canonical:
# BV -1/2 (dphi)^2, BS (dh)^2/2 with H = h/sqrt2 so xi H^dag H R = xi h^2 R/2).
sol = sp.solve(sp.Eq(M ** 2 + xiBS * h ** 2, M ** 2 - xiBV * h ** 2), xiBV)[0]
chk("xi_BV = -xi_BS (same field normalisation)", sp.simplify(sol + xiBS) == 0)
# cross-check with the two papers' conformal values: BS -1/6 <-> BV +1/6
chk("conformal: BS -1/6 maps to BV +1/6", sol.subs(xiBS, sp.Rational(-1, 6)) == sp.Rational(1, 6))

# ---------------------------------------------------------------- 2. numeric
c = 299792458.0
HBAR = 1.054571817e-34
G_2022 = 6.67430e-11            # CODATA 2022 = CODATA 2018 (READ, 2409.03787 sect XIV)
GEV = 1.602176634e-10
MP = math.sqrt(HBAR * c ** 5 / G_2022) / GEV
MRED = MP / math.sqrt(8 * math.pi)
print("M_Planck = %.6e GeV (CODATA 2022 table: 1.220890(14)e19)" % MP)
print("M_red    = %.6e GeV" % MRED)
chk("M_P matches CODATA 2022 1.220890e19 to 1e-6", abs(MP / 1.220890e19 - 1) < 1e-6)
PHI_GUT = 2e16
XI_GUT = (MRED / PHI_GUT) ** 2
print("xi_required(2e16) = %.6f" % XI_GUT)
chk("xi_required(2e16) ~ 1.48e4 within 5e-3 (excite.py:1398)", abs(XI_GUT / 1.48e4 - 1) < 5e-3)
XI_UNRED = (MP / PHI_GUT) ** 2
print("same with UNREDUCED Planck mass: %.4e (x %.4f = 8 pi)" % (XI_UNRED, XI_UNRED / XI_GUT))
chk("unreduced/reduced = 8 pi", abs(XI_UNRED / XI_GUT - 8 * math.pi) < 1e-9)
# G uncertainty 2.2e-5 relative -> xi moves 2.2e-5 relative (xi ~ 1/G)
print("G at +-1 sigma moves xi by +-%.1e relative" % 2.2e-5)

G_F = 1.1663787e-5              # CODATA 2022 (from PDG 2022), READ; tree pins 1.1663788e-5
v = 1 / math.sqrt(math.sqrt(2) * G_F)
print("v = %.6f GeV; xi_required(v) = %.10e" % (v, (MRED / v) ** 2))
chk("xi_required(v) ~ 9.7829e31 (tree 9.7829068836e31) to 1e-6",
    abs((MRED / v) ** 2 / 9.7829068836e31 - 1) < 1e-6)

# ---------------------------------------------------------------- 3. the GUT-scale choice
print("\nsensitivity to the unstated scale choice (xi ~ phi^-2):")
for nm, p in [("MSSM 1e16 (hep-ph/0601023 p.66)", 1e16), ("MSSM 2e16 (eq 2)", 2e16),
              ("3e16", 3e16), ("non-SUSY SU(5) ext ~1e14 (p.72)", 1e14),
              ("1e15", 1e15), ("h_end of Higgs inflation 1.07 M_red/sqrt(1.7e4)",
                               1.07 * MRED / math.sqrt(1.7e4))]:
    print("   %-48s phi=%.3e  xi_req=%.4e  /1.7e4=%.3g" % (nm, p, (MRED / p) ** 2, (MRED / p) ** 2 / 1.7e4))
chk("1e16 gives 4x the 2e16 value", abs((MRED / 1e16) ** 2 / XI_GUT - 4) < 1e-12)
# the scale at which xi_required equals 1.7e4 exactly
phi_eq = MRED / math.sqrt(1.7e4)
print("phi at which xi_required = 1.7e4: %.4e GeV  (= M_red/sqrt(xi_HI))" % phi_eq)
chk("M_red/sqrt(1.7e4) lies within 10 pct of 2e16", abs(phi_eq / 2e16 - 1) < 0.10)

# ---------------------------------------------------------------- 4. Higgs-inflation xi and its sign
MH = 125.20
lam = MH ** 2 / (2 * v ** 2)
xi_BS = 49000 * math.sqrt(lam)
print("\nBS eq (13) at m_h=125.20, tree-level lambda=%.4f: xi_BS = %.4e" % (lam, xi_BS))
print("xi_required(2e16)/xi_BS(eq13) = %.4f ; /1.7e4 = %.4f" % (XI_GUT / xi_BS, XI_GUT / 1.7e4))
chk("tree ratio 0.8722 reproduced against 1.7e4", abs(XI_GUT / 1.7e4 - 0.8722) < 1e-4)
# In BV's sign, Higgs inflation's coupling is xi_BV = -xi_BS < 0 -> BV case 1: no critical field,
# ANEC integrand positive.  Effective Planck mass^2 at h = 2e16 with the BS sign:
ratio = 1 + xi_BS * (PHI_GUT / MRED) ** 2
print("BS sign at h=2e16: M_eff^2/M_red^2 = 1 + xi h^2/M^2 = %.4f (grows; never vanishes)" % ratio)
chk("BS-sign coupling increases M_eff^2 at the GUT field (>1)", ratio > 1)
ratio_bv = 1 - XI_GUT * (PHI_GUT / MRED) ** 2
chk("BV-sign xi_required makes kappa - xi phi^2 = 0 exactly at 2e16", abs(ratio_bv) < 1e-12)

# ---------------------------------------------------------------- 5. robustness of excite.py's refusal
# excite.py:215-219 refuses the xi escape because the GUT field is above Degrassi's
# instability scale 10^(11+-1) GeV (endpoint.DEGRASSI_LOG10_LI; NOT re-read here).
# Whatever scale is chosen for 'GUT', a field BELOW that band needs:
for L in (12, 11, 10):
    print("   phi = 1e%d GeV (Degrassi band) -> xi_required = %.3e" % (L, (MRED / 10 ** L) ** 2))
chk("below the upper Degrassi edge 1e12 the gate needs xi > 5.9e12 (>3e8 x 1.7e4)",
    (MRED / 1e12) ** 2 > 5.9e12 and (MRED / 1e12) ** 2 / 1.7e4 > 3e8)

print("\n%d failure(s)" % len(FAIL))
sys.exit(1 if FAIL else 0)
