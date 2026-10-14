#!/usr/bin/env python3
"""DOCKET 67 / 1508.07161 (D'Onofrio & Rummukainen, PRD 93 (2016) 025003).
Re-derivation of what is finite here.  Stdlib + sympy.  Exits 1 on any failure.

(1) the tree's GeV -> K conversion (massform.py:545, t_kelvin at :2165), exactly,
    from the SI-exact e and k_B;
(2) the tree's two quotations of the source against each other (abstract
    159.5 +/- 1.5 vs Sec. VII 159.6 +/- 0.1 +/- 1.5, both as the tree quotes
    them at massform.py:1116-1125), and against the companion 1404.3565's
    T_c = 159 +/- 1 (massform.py:556-557);
(3) the margin by which every use the tree makes of T_c survives the quoted
    error: the only inequality it computes is T* = 131.7 < T_c
    (massform.py:2190);
(4) a SENSITIVITY ESTIMATE, labelled RECONSTRUCTED and NOT the paper's method:
    the one-loop high-T mass-parameter zero T_0 = m_H / sqrt(2c),
    c = (3 g^2 + g'^2)/16 + lambda/2 + y_t^2/4, used only for the logarithmic
    derivatives d ln T / d ln m_i, to ask whether moving input masses
    (whatever values the authors used; NOT READ here) could shift T_c by an
    amount comparable to the quoted +/-1.5 GeV.
"""
import sys
import sympy as sp

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        fails.append(name)

# (1) conversion ---------------------------------------------------------------
e = sp.Rational("1.602176634e-19")      # C, SI exact
kB = sp.Rational("1.380649e-23")        # J/K, SI exact
GeV_J = e * 10**9
Tc = sp.Rational("159.5")
TK = Tc * GeV_J / kB
print("T_c = 159.5 GeV =", sp.N(TK, 12), "K")
chk("159.5 GeV rounds to 1.851e15 K (massform.py:545)", "%.3e" % float(TK) == "1.851e+15",
    "%.6e" % float(TK))
band = [float(sp.Rational(x) * GeV_J / kB) for x in ("158.0", "161.0")]
print("  +/-1.5 GeV band in K: %.4e .. %.4e" % tuple(band))
chk("band edges print as 1.834e15 / 1.868e15 K", ("%.3e" % band[0], "%.3e" % band[1]) == ("1.834e+15", "1.868e+15"))

# (2) internal consistency of the quoted figures ---------------------------------
import math
abs_c, abs_e = 159.5, 1.5
sec7_c, sec7_e = 159.6, math.hypot(0.1, 1.5)
drt_c, drt_e = 159.0, 1.0
d1 = abs(sec7_c - abs_c)
chk("abstract vs Sec.VII differ by 0.1 GeV, 0.07 of the quoted error (a rounding-level discrepancy, not a conflict)",
    abs(d1 - 0.1) < 1e-12 and d1 / abs_e < 0.1, "%.3f GeV = %.3f sigma" % (d1, d1 / abs_e))
d2 = abs(abs_c - drt_c) / math.hypot(abs_e, drt_e)
chk("1508.07161's 159.5+/-1.5 agrees with 1404.3565's 159+/-1 within 1 sigma", d2 < 1.0, "%.3f sigma" % d2)

# (3) the tree's only computed inequality on T_c --------------------------------
Tstar, Tstar_e = 131.7, None   # T* error not quoted in the tree; 2.3 GeV in 1404.3565 is NOT READ here
margin = abs_c - Tstar
chk("T* < T_c survives the quoted T_c error by > 10 sigma", margin / abs_e > 10, "%.1f GeV = %.1f sigma" % (margin, margin / abs_e))
chk("T* < T_c survives even T_c lowered to the crossover's quoted ~5 GeV width below", abs_c - 5.0 > Tstar)

# (4) sensitivity estimate (RECONSTRUCTED; not the paper's method) --------------
mH, mW, mZ, mt, v = sp.symbols("m_H m_W m_Z m_t v", positive=True)
g2 = 4 * mW**2 / v**2
gp2 = 4 * (mZ**2 - mW**2) / v**2
lam = mH**2 / (2 * v**2)
yt2 = 2 * mt**2 / v**2
c = (3 * g2 + gp2) / 16 + lam / 2 + yt2 / 4
T0 = mH / sp.sqrt(2 * c)
T0s = sp.simplify(T0)
print("  T_0 =", T0s)
# The closed form: T_0^2 = 2 m_H^2 v^2 / (2 m_W^2 + m_Z^2 + m_H^2 + 2 m_t^2)
chk("closed form T_0^2 = 2 m_H^2 v^2/(2 m_W^2 + m_Z^2 + m_H^2 + 2 m_t^2)",
    sp.simplify(T0**2 - 2 * mH**2 * v**2 / (2 * mW**2 + mZ**2 + mH**2 + 2 * mt**2)) == 0)
def val(sub):
    return float(T0.subs(sub))
# Two input sets: an assumed 2015-era set and PDG 2024 central values.  The
# 2015 set is ASSUMED (the paper's inputs were not READ here: alphaXiv quota).
set15 = {mH: 125.0, mW: 80.4, mZ: 91.19, mt: 173.0, v: 246.0}
set24 = {mH: 125.20, mW: 80.3692, mZ: 91.1880, mt: 172.57, v: 246.22}
t15, t24 = val(set15), val(set24)
print("  one-loop T_0: assumed-2015 inputs %.2f GeV, PDG-2024 inputs %.2f GeV, shift %+.3f GeV" % (t15, t24, t24 - t15))
chk("one-loop T_0 is 12% below the lattice 159.5: the crude estimate is in the regime but is NOT a re-derivation of the value",
    0.10 < (159.5 - t15) / 159.5 < 0.15, "%.1f GeV" % t15)
elas = {s: float((sp.diff(sp.log(T0), s) * s).subs(set24)) for s in (mH, mW, mZ, mt)}
for s, x in elas.items():
    print("  d ln T_0 / d ln %s = %+.3f" % (s, x))
shift = abs(t24 - t15)
chk("input movement assumed-2015 -> PDG-2024 shifts T_0 by less than the quoted 1.5 GeV (0.54 GeV, a third of it)", shift < 1.5, "%.3f GeV" % shift)
for s_ in (mH, mW, mZ, mt, v):
    one = dict(set15); one[s_] = set24[s_]
    print("    from %s alone: %+.3f GeV" % (s_, val(one) - t15))
# m_H = 125.13 +/- 0.11 (RPP 2026, READ by the sibling audit pdg-2026-m_h.json)
set26 = dict(set24); set26[mH] = 125.13
t26 = val(set26)
print("  one-loop T_0 with RPP-2026 m_H = 125.13: %.2f GeV (vs PDG-2024 set %+.3f GeV)" % (t26, t26 - t24))
chk("RPP-2024 -> RPP-2026 m_H move (-0.07 GeV) shifts T_0 by < 0.1 GeV", abs(t26 - t24) < 0.1, "%.3f GeV" % (t26 - t24))
# m_t / m_W values in set24 are NOT READ this stage (alphaXiv quota; arXiv/PDG egress-blocked);
# a +/-1 GeV band on m_t bounds any plausible top-mass choice:
for dm in (-1.0, 1.0):
    one = dict(set24); one[mt] = set24[mt] + dm
    print("    m_t %+.0f GeV: %+.3f GeV" % (dm, val(one) - t24))
# scaled shift: apply the same fractional shift to the lattice figure
frac = (t24 - t15) / t15
print("  same fractional move applied to 159.5: %+.3f GeV" % (159.5 * frac))
# m_H uncertainty today (PDG 2024: +/-0.11 GeV) propagated through the elasticity
dT_mH = 159.5 * elas[mH] * 0.11 / 125.20
print("  PDG-2024 m_H error propagates to %.3f GeV on T_c" % dT_mH)
chk("today's m_H error moves T_c by ~0.12 GeV, < 1/10 of the quoted 1.5", abs(dT_mH) < 0.15)

print("\n%d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
