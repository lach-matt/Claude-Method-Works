#!/usr/bin/env python3
"""DOCKET 67 re-derivation: sphaleron-instanton-and-collider-dispute (ledger S11).

What the tree uses (ledger.py:1656 via massform.PROPOSED_ROWS['S11'];
massform.py:176-192, 520-543, 570-613, 898-904):
  (a) INSTANTON: exp(-4 pi/alpha_W) per transition, alpha_W = g^2/4pi, g = 2 m_W/v,
      printed 10^-160.95 at 1/alpha_W = 29.49.
  (b) SPHALERON: E_sph = (2 m_W/alpha_W) B = (4 pi v/g) B = 4.740 TeV x B; ~9 TeV;
      9.08 TeV / (3 m_p) = 3226 ("~3.2e3").
  (c) COLLIDER RATE: CONTESTED (BLRRT, Khoze-Milne, FFS vs Tye-Wong; CMS 0.021).

Everything below is checked against page text READ at source (alphaXiv page text
recovered verbatim from this session's transcripts into ../src/sph/*.pages.txt).
Checks are arithmetic on the sources' OWN printed numbers, plus the one finite
field computation available here (the KM spherically symmetric SU(2) saddle, via
the solver of the sibling audit 1612.05431-1505.03690-esph.py) to quantify the
Higgs-mass datum BLRRT (2003) lacked.  The collider rate itself (the holy-grail
function F(E) above E_sph) is NOT computable here: it needs the BLRRT complex-time
boundary-value problem or the KM optical-theorem saddle, neither of which is a
finite/closed-form object.
"""
import math, sys, importlib.util, os
import sympy as sp

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))

def rec(name, detail):  # recorded discrepancy, not a pass/fail on the tree
    print("RECORDED " + name + "  -- " + detail)

L10 = math.log(10)
def log10_exp(x): return x / L10

# ---------------------------------------------------------------- (0) symbolic identities
g, v, mW, a = sp.symbols('g v m_W alpha', positive=True)
alpha_of_g = g**2 / (4 * sp.pi)
check("4pi/alpha_W == 16 pi^2/g^2 (massform.py:530)",
      sp.simplify(4 * sp.pi / alpha_of_g - 16 * sp.pi**2 / g**2) == 0)
check("S_inst = 8pi^2/g^2 = 2pi/alpha_W, so exp(-2 S_inst) = exp(-4pi/alpha_W) (TW15 printed p.7)",
      sp.simplify(2 * (8 * sp.pi**2 / g**2) - 4 * sp.pi / alpha_of_g) == 0)
gsub = 2 * mW / v
check("E_sph prefactor: 2 m_W/alpha_W == 4 pi v/g == 2 pi v^2/m_W when g = 2 m_W/v (massform.py:522)",
      sp.simplify((2 * mW / alpha_of_g).subs(g, gsub) - (4 * sp.pi * v / g).subs(g, gsub)) == 0
      and sp.simplify((4 * sp.pi * v / g).subs(g, gsub) - 2 * sp.pi * v**2 / mW) == 0)

# ---------------------------------------------------------------- (1) tree inputs
GF = 1.1663788e-5          # GeV^-2, as held in higgs.py (NAMED-NOT-READ in the tree)
V = (math.sqrt(2) * GF) ** -0.5
MW_TREE = 80.362           # captures/PDG-2026.tsv, as massform uses
gT = 2 * MW_TREE / V
ainvT = 4 * math.pi / gT**2
check("v from G_F = 246.2196 GeV", abs(V - 246.2196) < 1e-3, "%.5f" % V)
check("1/alpha_W (tree) = 29.49", abs(ainvT - 29.49) < 0.01, "%.4f" % ainvT)
lg = -log10_exp(4 * math.pi * ainvT)
check("exp(-4pi/alpha_W) = 10^-160.95 (massform.py:531)", abs(lg + 160.95) < 0.006, "%.4f" % lg)
MP = 0.938272089           # GeV
B_TOT = 4.2109e28
ntr = math.ceil(B_TOT / 3)
check("B/3 transitions = 1.4036e28 (massform.py:180)", abs(ntr / 1.4036e28 - 1) < 1e-4, "%.5e" % ntr)
need = math.log10(ntr) - lg
check("(attempts x prefactor) >= 10^189.10 (massform.py:533)", abs(need - 189.10) < 0.006, "%.4f" % need)

# ---------------------------------------------------------------- (2) printed pairings in the sources
pairs = [
    ("Rubakov-Shaposhnikov hep-ph/9603208 eq.(2.8) [tree capture; not in recovered pages]", 29.0, -170),
    ("Tye-Wong 1505.03690 printed p.2 (alphaXiv p.3): exp(-4pi/alpha_W) ~ 10^-162, alpha_W ~ 1/30", 30.0, -162),
    ("Tye-Wong 1505.03690 printed p.7 (alphaXiv p.8): exp(-2S) ~ 10^-162, alpha_W ~ 1/29.7", 29.7, -162),
]
for name, ai, printed in pairs:
    val = -log10_exp(4 * math.pi * ai)
    gap = val - printed
    (check if abs(gap) < 0.5 else rec)(name, "arithmetic 10^%.2f vs printed 10^%d (gap %.2f decades)" % (val, printed, gap))
# Matchev-Verner 2505.05607 p.12: alpha_W ~ 0.034, exp(-370) ~ 10^-161
mv = 4 * math.pi / 0.034
check("Matchev-Verner 2025 (2505.05607 p.12): 4pi/0.034 ~ 370, exp(-370) ~ 10^-161",
      abs(mv - 370) < 1 and abs(-log10_exp(mv) + 161) < 0.5, "4pi/0.034 = %.1f -> 10^%.2f" % (mv, -log10_exp(mv)))
# FFS 1612.05431 p.1: "suppressed by e^{-S_instanton} ~ 10^-162"
s_inst = 2 * math.pi * ainvT
rec("FFS 1612.05431 p.1 'e^{-S_instanton} ~ 10^-162'",
    "with S_instanton = 2pi/alpha_W (TW15 p.7; sympy above) e^{-S} = 10^%.2f and e^{-2S} = 10^%.2f; "
    "the printed 10^-162 matches e^{-2S}, so the printed exponent omits the factor 2 (misprint-class; "
    "the tree does not use this sentence)" % (-log10_exp(s_inst), -log10_exp(2 * s_inst)))

# ---------------------------------------------------------------- (3) sphaleron numbers
pref = 2 * math.pi * V**2 / MW_TREE / 1000
check("prefactor 4pi v/g = 4.740 TeV at tree inputs (massform.py:537)", abs(pref - 4.740) < 0.0006, "%.5f TeV" % pref)
b12 = 1.313 + 0.603   # FFS eq.(8): beta1 + beta2, E_sph = g2 v V(pi/2) = (4pi v/g)(beta1+beta2)
e_ffs_tree = pref * b12
check("FFS eq.(8)-(10): (4pi v/g)(beta1+beta2) at tree inputs ~ 9.08 TeV", abs(e_ffs_tree - 9.08) < 0.01, "%.4f TeV" % e_ffs_tree)
g_impl = 4 * math.pi * 0.246 / (9.08 / b12)
rec("FFS input implied by eq.(10) with v = 246 GeV", "g2 = %.4f, m_W = g v/2 = %.2f GeV (FFS do not print m_W)" % (g_impl, g_impl * 246 / 2))
tw = 2 * math.pi * 246**2 / 80 / 1000
rec("TW15 eq.(1.2) prefactor at their v=246, m_W=80", "4pi v/g = %.4f TeV (printed 4.75); 4.75 x (1.31+0.60) = %.4f vs printed 9.11 "
    "(sibling audit: saddle B = 1.9170 at these inputs gives 9.111; the 0.4%% is in the two-decimal coefficients)" % (tw, 4.75 * 1.91))
ratio = 9.08 / (3 * MP) * 1000
check("9.08 TeV / (3 m_p c^2) = 3226 ('~3.2e3', ledger S11)", round(ratio) == 3226, "%.2f" % ratio)
rec("TW15 printed p.4 (alphaXiv p.5)", "'turning on the U(1) coupling (sin^2 theta_W = 0.23) will lower the sphaleron energy by about a percent. "
    "So it is reasonable to use E_sph = 9.0 TeV': 9.11 x 0.99 = %.2f TeV (consistent)" % (9.11 * 0.99))

# ---------------------------------------------------------------- (4) FFS overlap and multi-W numbers (1612.05431 p.4)
for mw in (80.24, 80.362, 80.385, 80.3692):
    x = -log10_exp(math.pi * 9080.0 / mw)
    print("      FFS overlap e^{-pi E_sph/m_W} at E_sph = 9.08 TeV, m_W = %.4f: 10^%.2f" % (mw, x))
x = -log10_exp(math.pi * 9080.0 / 80.385)
rec("FFS p.4 'e^{-pi E_sph/m_W} ~ 10^-155'", "arithmetic 10^%.2f at m_W = 80.385 (range -154.0..-154.2 over m_W 80.24-80.39); "
    "printed 10^-155 is ~0.9 decade stronger -- rounding-class under '~', recorded, not a refutation; "
    "the tree quotes 'about 10^-155' (massform.py:598)" % x)
nW = 9080.0 / (math.sqrt(2) * 80.385)
check("FFS p.4 'about 80 W bosons': E_sph/(sqrt2 m_W) with |k| ~ m_W each", abs(nW - 80) < 1.5, "%.1f" % nW)
ps = -80 * 2 * math.log10(4 * math.pi)
check("FFS p.4 (1/(4pi)^2)^80 ~ 10^-176", abs(ps + 176) < 0.5, "10^%.2f" % ps)

# ---------------------------------------------------------------- (5) BLRRT printed numbers (hep-ph/0304180)
check("BLRRT p.7: e^-60 ~ 10^-26", abs(-log10_exp(60) + 26) < 0.1, "10^%.3f" % -log10_exp(60))
e8 = 8 * 80.4 * 30 / 1000
check("BLRRT p.7: 8 M_W/alpha_W ~ 20 TeV at alpha_W = 1/30", abs(e8 - 20) < 1, "%.2f TeV (M_W = 80.4)" % e8)
rec("BLRRT abstract: '30 sphaleron masses (250 TeV)' and 'sphaleron energy (8 TeV)'",
    "250/30 = %.2f TeV per sphaleron mass, i.e. their model's E_sph ~ 8.3 TeV; computed below for m_H = m_W" % (250 / 30))

# BLRRT scope: 'lambda = 0.125, which corresponds to M_H = M_W' (p.3).  The datum they lacked: m_H = 125 GeV.
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("esph", os.path.join(here, "1612.05431-1505.03690-esph.py"))
try:
    esph = importlib.util.module_from_spec(spec); spec.loader.exec_module(esph)
    B1 = esph.solve(1.0)[4]
    Bphys = esph.solve(125.20 / 80.3692)[4]
    B1b = esph.solve(1.0, L=90.0, n=6000)[4]
    check("KM saddle solver converged at m_H = m_W (B stable under L 60->90)", abs(B1 - B1b) < 2e-4, "B(1) = %.5f / %.5f" % (B1, B1b))
    e_blrrt_model = 2 * 80.4 * 30 * B1 / 1000
    rec("E_sph in BLRRT's model (m_H = m_W, alpha_W = 1/30, M_W = 80.4)",
        "B(1) = %.4f -> E_sph = %.2f TeV; 30 x that = %.0f TeV (their '8 TeV' and '250 TeV' are rounded low by ~5-6%%)" % (B1, e_blrrt_model, 30 * e_blrrt_model))
    shift = Bphys / B1 - 1
    rec("Higgs-mass datum BLRRT lacked (m_H/m_W 1 -> 1.558)",
        "B moves %.4f -> %.4f (%+.1f%%): the barrier they measured energies against is %.1f%% lower than today's; "
        "their exponent F(E/E_sph) is stated to depend 'very weakly' on M_H (p.3) -- asserted, not computed there, and not computable here" %
        (B1, Bphys, 100 * shift, 100 * shift))
    check("B(m_H/m_W = 1.558) reproduces the sibling audit's 1.916 (FFS beta1+beta2)", abs(Bphys - 1.916) < 0.003, "%.4f" % Bphys)
except Exception as exc:
    rec("KM saddle solver", "NOT RUN: %r" % (exc,))

# ---------------------------------------------------------------- (6) Khoze-Milne 2011.07167 printed numbers
Tab1 = {30: .735, 20: .727, 10: .713, 7.0: .707, 5.0: .702, 4.0: .701, 3.0: .704, 2.0: .720, 0.5: .891}
Tab2 = {30: .735, 20: .727, 10: .713, 7.0: .706, 5.0: .700, 4.0: .697, 3.0: .696, 2.0: .699, 0.5: .861}
m1, m2 = min(Tab1.values()), min(Tab2.values())
check("KM Table 1 (simplified F) min F* = 0.701 at eps = 4 -> 'F ~ 0.70, loosing only 30%' (printed p.9)", m1 == 0.701)
rec("KM Table 2 (full saddle equations) min F* = %.3f at eps = 3" % m2,
    "below the 0.70 of 'suppressed by at least e^{-(4pi/alpha_w) 0.70}' (printed p.9) by %.3f; in exponent: %.2f decades at the tree's alpha_W. "
    "KM p.10 says F 'still does not drop far below 0.7'. The 'at least' is Table 1's, not Table 2's -- a wording discrepancy, "
    "recorded; '~30%%' (p.16) holds for both (%.1f%%, %.1f%%)" % (0.70 - m2, (0.70 - m2) * 4 * math.pi * ainvT / L10, 100 * (1 - m1), 100 * (1 - m2)))
for F in (0.70, m2):
    print("      exp(-(4pi/alpha_W) F) at tree alpha_W, F = %.3f: 10^%.2f" % (F, -log10_exp(4 * math.pi * ainvT * F)))
e_unit = math.pi * 80.3692 * ainvT / 1000
print("      KM eps = E/(pi m_W/alpha_W): unit = %.3f TeV; eps = 4 -> %.1f TeV; eps = 30 -> %.0f TeV; E_sph = 9.08 TeV -> eps = %.2f"
      % (e_unit, 4 * e_unit, 30 * e_unit, 9.08 / e_unit))

# ---------------------------------------------------------------- (7) Tye-Wong 1710.07223 printed numbers
E0 = math.sqrt(6) * math.pi * 80 * 30 / 1000
rec("TW17 printed p.4: 'E_0 = sqrt(6) pi m_W/alpha_W ~ 15 TeV'",
    "at their own m_W ~ 80 GeV, alpha_W ~ 1/30 (p.1): %.2f TeV; at tree inputs %.2f TeV. Printed 15 is ~19%% low "
    "(misprint-class; not used by the tree; the same E_0 formula is BLRRT-PLB eq.(8))" % (E0, math.sqrt(6) * math.pi * 80.362 * ainvT / 1000))
check("TW17 p.1: g ~ 0.645 <-> alpha_W = g^2/4pi ~ 1/30", abs(4 * math.pi / 0.645**2 - 30.2) < 0.1, "1/alpha = %.2f" % (4 * math.pi / 0.645**2))
check("TW17 p.1: m_W = g v/2 ~ 80 GeV at g = 0.645, v = 246", abs(0.645 * 246 / 2 - 79.3) < 0.1, "%.2f GeV" % (0.645 * 246 / 2))
# eq.(4)/(41): kappa ~ (2^{d/2}/d)(1 - sqrt(E_sph/E_qq))^{d/2}; exact solid-angle fraction for d = 4
c, t = sp.symbols('c t', positive=True)
d = 4
frac_exact = 1 - sp.integrate((1 - t**2)**sp.Rational(d - 2, 2), (t, 0, c)) / sp.integrate((1 - t**2)**sp.Rational(d - 2, 2), (t, 0, 1))
lead = sp.limit(frac_exact / (1 - c)**2, c, 1)
tw_lead = sp.Rational(2**(d // 2), d)
check("TW17 eq.(41) solid-angle fraction, d = 4: exact = (1-c)^2 (2+c)/2", sp.simplify(frac_exact - (1 - c)**2 * (2 + c) / 2) == 0)
rec("TW17 eq.(4)/(41) leading coefficient, d = 4",
    "exact near threshold: %s (1-c)^2; TW's (2^{d/2}/d)(1-c)^{d/2}: %s (1-c)^2 -- order-unity factor dropped under their '~'" % (lead, tw_lead))
for E in (9.5, 10.0, 11.0, 13.0):
    cc = math.sqrt(9.0 / E)
    print("      TW17 kappa(E_qq = %.1f TeV; E_sph = 9.0, d = 4): TW form %.2e, exact fraction %.2e" % (E, (1 - cc)**2, (1 - cc)**2 * (2 + cc) / 2))
rec("TW17 p.1 eq.(3) vs eq.(4)", "prevalent kappa < 10^-70 vs TW kappa ~ 10^-3: the '~70 orders of magnitude' (p.1, p.3) is >= 67 decades by their own figures (70 - 3)")

# ---------------------------------------------------------------- (8) CMS 1805.06013 vs the two sides
rec("CMS 1805.06013 abstract: PEF < 0.021 (95% CL) at 13 TeV, E_sph = 9 TeV",
    "TW's own kappa ~ 1e-3 (eq.(4), for 14 TeV) lies below 0.021, and the prevalent < 1e-70 lies below it; "
    "the limit excludes neither side (the tree: 'the experiment does not decide it', massform.py:608-610)")

print("\n%d PASS, %d FAIL" % (PASS, FAIL))
sys.exit(1 if FAIL else 0)
