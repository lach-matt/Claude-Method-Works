#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key pdg-g_fermi.

G_F = 1.1663788e-5 GeV^-2 (higgs.py:209), the vev v = (sqrt2 G_F)^(-1/2)
(higgs.py:262-264), and alpha_W = g^2/4pi with g = 2 m_W / v (massform.py
alpha_w, S11 via ledger.py:1656), and rho_EW = |V_min| (D20, ledger.py:526-540).

Every numerical input below is READ at source this pass (page cited) or taken
from the owner by import (read-only, bytecode writing disabled).  Nothing in
research/warp-drive is written.

Sections:
 A  sympy: tree relations (MuLan eq.2 without sum r_i; Buttazzo eq.17-18)
 B  MuLan 1211.0960 eq.23 re-run from its printed inputs (pp.28-29)
 C  Eberhart et al. 2607.02657 eq.21 re-run from its printed inputs (eqs.4,17,20)
 D  Buttazzo 1307.3536 eq.27: the W-propagator convention
 E  the owner's figures reproduced independently
 F  sensitivity of v, rho_EW, alpha_W exponent to every READ G_F
 G  scheme dependence of alpha_W (the hypothesis the owner does not name)
Exit 1 on any FAIL.
"""
import math, os, sys

sys.dont_write_bytecode = True
import sympy as sp

FAILS = []


def chk(name, got, want, rel):
    ok = abs(got - want) <= rel * abs(want)
    print("%-4s %-62s got %.10g want %.10g (rel tol %g)" % (
        "ok" if ok else "FAIL", name, got, want, rel))
    if not ok:
        FAILS.append(name)


# --------------------------------------------------------------------- A
print("== A  sympy tree relations")
G, g, MW, v, mh, lam = sp.symbols("G_F g M_W v m_h lambda", positive=True)
# MuLan eq.(2) at tree level (sum r_i = 0): G_F/sqrt2 = g^2/(8 M_W^2); M_W = g v / 2
tree = sp.Eq(G / sp.sqrt(2), g**2 / (8 * MW**2))
sol_v = sp.solve(tree.subs(MW, g * v / 2), v)
vexpr = [s for s in sol_v if s.is_positive][0]
A1 = sp.simplify(vexpr - (sp.sqrt(2) * G) ** sp.Rational(-1, 2)) == 0
print("A1 v = (sqrt2 G_F)^(-1/2) from tree eq.2 + M_W = g v/2 :", A1)
# alpha_W = g^2/4pi with g = 2 M_W / v and v tree  ->  sqrt2 G_F M_W^2 / pi
aw_expr = sp.simplify(((2 * MW / vexpr) ** 2 / (4 * sp.pi)))
A2 = sp.simplify(aw_expr - sp.sqrt(2) * G * MW**2 / sp.pi) == 0
print("A2 alpha_W(g=2M_W/v, tree v) = sqrt2 G_F M_W^2/pi       :", A2)
# V_min = -lambda v^4/4 with lambda = m_h^2/(2 v^2)  ->  -m_h^2 v^2/8
A3 = sp.simplify((-lam * v**4 / 4).subs(lam, mh**2 / (2 * v**2)) + mh**2 * v**2 / 8) == 0
print("A3 V_min = -m_h^2 v^2/8                                   :", A3)
# Buttazzo eq.(18): g2_OS = 2 (sqrt2 G_mu)^(1/2) M_W is the same relation
A4 = sp.simplify(2 * MW / vexpr - 2 * sp.sqrt(sp.sqrt(2) * G) * MW) == 0
print("A4 g = 2 M_W / v  ==  Buttazzo eq.18 g2_OS                :", A4)
for n, ok in (("A1", A1), ("A2", A2), ("A3", A3), ("A4", A4)):
    if not ok:
        FAILS.append(n)

# --------------------------------------------------------------------- B
print("\n== B  MuLan 1211.0960 eq.(23) from printed inputs (pp.28-29)")
HBAR_2010 = 6.58211928e-25          # GeV s, CODATA 2010, printed p.28
TAU_MULAN = 2196980.3e-12           # s, eq.(22)
MMU_2010 = 0.1056583715             # GeV, printed p.28
DQ_MULAN = (-187.1 - 4233.7 + 36.3 - 0.4) * 1e-6   # p.29, incl. Pak-Czarnecki -0.4
G_PRINT_MULAN = 1.1663787e-5        # eq.(24)


def gf(tau_s, mmu_gev, dq, hbar):
    tau_nat = tau_s / hbar          # GeV^-1
    return math.sqrt(192 * math.pi**3 / (tau_nat * mmu_gev**5) / (1 + dq))


gB = gf(TAU_MULAN, MMU_2010, DQ_MULAN, HBAR_2010)
gB_noPC = gf(TAU_MULAN, MMU_2010, DQ_MULAN + 0.4e-6, HBAR_2010)
print("B  G_F re-run              = %.10e   printed 1.1663787(6)e-5" % gB)
print("B  offset from print       = %+.3f ppm  (%.2f sigma of the 0.5 ppm)" % (
    (gB / G_PRINT_MULAN - 1) * 1e6, (gB / G_PRINT_MULAN - 1) / 0.51e-6))
print("B  without -0.4 ppm term   = %.10e" % gB_noPC)
chk("B MuLan eq.23 re-run within its own 0.6e-11 error", gB, G_PRINT_MULAN, 0.6e-11 / 1.1663787e-5)

# --------------------------------------------------------------------- C
print("\n== C  Eberhart et al. 2607.02657 eq.(21) from eqs.(4),(17),(20)")
HBAR_EXACT = 6.582119569e-25        # GeV s, exact (PDG 2024 Table 1.1: 6.582 119 569e-22 MeV s)
TAU_2026 = 2.1969811e-6             # s, eq.(20)
MMU_2026 = 0.1056583755             # GeV, eq.(4)
DQ_2026 = -4384678e-9               # eq.(17)
gC = gf(TAU_2026, MMU_2026, DQ_2026, HBAR_EXACT)
print("C  G_F re-run = %.10e  printed 1.16637859(59)e-5" % gC)
chk("C Eberhart eq.21 reproduced", gC, 1.16637859e-5, 1e-8)

# --------------------------------------------------------------------- D
print("\n== D  Buttazzo 1307.3536 eq.(27): W-propagator term removed")
MW_BUTTAZZO = 80.384                # Table 2
gD = G_PRINT_MULAN / math.sqrt(1 + 3 * MMU_2010**2 / (5 * MW_BUTTAZZO**2))
print("D  1.1663787e-5/sqrt(1+3m_mu^2/5M_W^2) = %.10e ; printed 1.1663781(6)e-5" % gD)
chk("D Buttazzo G_mu without dim-8 term", gD, 1.1663781e-5, 1e-7)

# --------------------------------------------------------------------- E
print("\n== E  owner figures reproduced (owner imported read-only)")
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
cwd = os.getcwd()
os.chdir(WD)
import higgs, massform, excite      # noqa: E402
os.chdir(cwd)
G_TREE = higgs.G_FERMI
chk("E owner G_FERMI == PDG 2024 Table 1.1 1.166 378 8e-5", G_TREE, 1.1663788e-5, 0.0)
v_ind = (math.sqrt(2) * G_TREE) ** -0.5
chk("E v independent vs higgs.vev()", v_ind, higgs.vev(), 1e-14)
chk("E v vs Buttazzo Table 2 V=246.21971 (G_mu=1.1663787)", (math.sqrt(2) * G_PRINT_MULAN) ** -0.5, 246.21971, 3e-7)
mh = higgs.M_HIGGS
vmin_ind = -mh**2 * v_ind**2 / 8
chk("E V_min = -m_h^2 v^2/8 vs higgs.v_min_gev4()", vmin_ind, higgs.v_min_gev4(), 1e-12)
lam_tree = G_PRINT_MULAN * 125.15**2 / math.sqrt(2)
print("E  Buttazzo eq.11 lambda_OS at M_h=125.15 = %.6f ; Table 3 prints LO 0.12917 "
      "(DISCREPANCY RECORDED: 0.129177 rounds to 0.12918; 5.7e-5 relative, a last-digit "
      "rounding/truncation matter, not adjudicated)" % lam_tree)
chk("E Buttazzo LO lambda 0.12917 (eq.11, to its printed 5 digits)", lam_tree, 0.12917, 1e-4)
mw = massform.M_W_GEV
aw_ind = math.sqrt(2) * G_TREE * mw**2 / math.pi
aw_own = massform.alpha_w()[0]
chk("E alpha_W = sqrt2 G_F m_W^2/pi vs massform.alpha_w()", aw_ind, aw_own, 1e-13)
print("E  m_W (massform, capture READ) = %.4f GeV ; 1/alpha_W = %.4f" % (mw, 1 / aw_ind))
l10 = -(4 * math.pi / aw_ind) / math.log(10)
chk("E log10 exp(-4pi/alpha_W) vs massform (-160.95 printed)", l10, massform.log10_suppression(), 1e-12)
chk("E printed '10^-160.95' in massform docstring", round(l10, 2), -160.95, 0.0)

# --------------------------------------------------------------------- F
print("\n== F  sensitivity to every READ G_F")
READ_GF = [
    ("PDG 2024 Table 1.1 (tree pin)", 1.1663788e-5),
    ("MuLan 2013 eq.24 / Crivellin eq.1", 1.1663787e-5),
    ("Eberhart 2026 eq.21", 1.16637859e-5),
    ("Buttazzo eq.27 convention", 1.1663781e-5),
    ("G_F^EW Crivellin eq.5 (+2 sigma)", 1.16716e-5),
    ("G_F^CKM Crivellin eq.9 (-3 sigma)", 1.16550e-5),
]
base_v = v_ind
base_rho = abs(vmin_ind)
base_exp = 4 * math.pi / aw_ind / math.log(10)
print("%-36s %12s %12s %12s %14s" % ("G_F source", "value", "dv/v", "drho/rho", "d log10 supp"))
maxmu = 0.0
for name, gval in READ_GF:
    vv = (math.sqrt(2) * gval) ** -0.5
    rho = mh**2 * vv**2 / 8
    aw = math.sqrt(2) * gval * mw**2 / math.pi
    de = -(4 * math.pi / aw / math.log(10)) + base_exp
    print("%-36s %12.8e %+12.3e %+12.3e %+14.4f" % (name, gval, vv / base_v - 1, rho / base_rho - 1, de))
    if "EW" not in name and "CKM" not in name:
        maxmu = max(maxmu, abs(vv / base_v - 1))
chk("F every muon-decay G_F moves v by <= 3.1e-7", min(maxmu, 3.1e-7), maxmu, 0.0)

# --------------------------------------------------------------------- G
print("\n== G  scheme dependence of alpha_W and of exp(-4pi/alpha_W)")
ALPHA0 = 1 / 137.035999084          # PDG 2024 Table 1.1
ALPHA_MW = 1 / 128.0                # PDG 2024 Table 1.1 footnote: 'At Q^2 ~ m_W^2 the value is ~1/128'
MW24, MZ24 = 80.3692, 91.1880       # PDG 2024 Table 1.1
S2_MSBAR = 0.23129                  # PDG 2024 Table 1.1, sin^2 theta-hat(M_Z) MS-bar
s2_os = 1 - MW24**2 / MZ24**2
cands = [
    ("owner: sqrt2 G_F m_W^2/pi, m_W=%.3f" % mw, aw_ind),
    ("G_mu scheme with PDG 2024 m_W=80.3692", math.sqrt(2) * G_TREE * MW24**2 / math.pi),
    ("on-shell alpha(0)/s2_W, s2=1-mW^2/mZ^2", ALPHA0 / s2_os),
    ("alpha(m_W)~1/128 / MS-bar s2(M_Z)", ALPHA_MW / S2_MSBAR),
    ("Buttazzo NNLO MS-bar g2(M_t)=0.64779", 0.64779**2 / (4 * math.pi)),
    ("Buttazzo LO g2=0.65294", 0.65294**2 / (4 * math.pi)),
    ("Rubakov-Shaposhnikov printed 1/29", 1 / 29.0),
]
for name, aw in cands:
    print("%-44s 1/alpha_W = %8.4f   log10 exp(-4pi/aW) = %9.3f   shift %+7.3f decades" % (
        name, 1 / aw, -(4 * math.pi / aw) / math.log(10),
        -(4 * math.pi / aw) / math.log(10) - l10))
sum_r = math.sqrt(2) * G_TREE * MW24**2 * s2_os / (math.pi * ALPHA0) - 1
print("G  MuLan eq.(3) solved for (1+sum r_i) with PDG 2024 inputs: sum r_i = %.5f" % sum_r)
spread = [-(4 * math.pi / aw) / math.log(10) for _n, aw in cands[:6]]
print("G  spread of the exponent over the six SM-scheme values: %.2f decades" % (max(spread) - min(spread)))
gf_digit_move = abs(READ_GF[2][1] / G_TREE - 1) * base_exp
print("G  for comparison, the 2026 G_F update moves the exponent by %.2e decades" % gf_digit_move)
ratio = (max(spread) - min(spread)) / gf_digit_move
print("G  ratio scheme spread / G_F-update move = %.3g" % ratio)
chk("G scheme spread exceeds the G_F-update move by more than 1e5", min(ratio, 1e5), 1e5, 0.0)

# --------------------------------------------------------------------- H
print("\n== H  tree-level V_min (D20's rho_EW) against Buttazzo's MS-bar(M_t) parameters")
m_ms, lam_ms = 131.55, 0.12604      # Buttazzo eq.(56), eq.(55)
depth_tree_B = 125.15**2 * 246.21971**2 / 8
depth_ms = m_ms**4 / (16 * lam_ms)  # tree-FORM depth m^4/(16 lambda) with MS-bar(M_t) values
print("H  tree depth (M_h=125.15, V=246.21971) = %.5e GeV^4 ; tree-form with MS-bar(M_t) = %.5e ; ratio %.4f" % (
    depth_tree_B, depth_ms, depth_ms / depth_tree_B))
print("H  ILLUSTRATIVE ONLY: V_min is not an observable; CW loop terms are omitted in both")
print("H  lambda NNLO/LO = %.4f ; m^2/M_h^2 = %.4f" % (0.12604 / 0.12917, m_ms**2 / 125.15**2))
chk("H scheme ratio is O(1), not an order of magnitude", min(depth_ms / depth_tree_B, 10.0), depth_ms / depth_tree_B, 0.0)

print("\n%d FAIL" % len(FAILS), FAILS)
sys.exit(1 if FAILS else 0)
