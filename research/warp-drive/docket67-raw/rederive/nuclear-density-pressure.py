#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'nuclear-density-pressure' (seatindex.py:95, :370-375, :406).

The tree compares T_kk_required(l) = pi c^4/(4 G l^2) against 'nuclear ~1e35 Pa'.
Inputs whose status matters:
  c, G, m_n c^2, m_p c^2 : CODATA 2018 via scipy.constants (READ from the scipy
                           1.17.1 wheel already in the scratchpad, no network).
  n0 (saturation number density) and E/A (energy per nucleon at saturation):
                           NOT READ AT SOURCE in this stage (alphaXiv quota exhausted,
                           arxiv.org egress-blocked).  Treated as a SCANNED PARAMETER,
                           and the script reports the break-even n0 below which the
                           tree's conclusion would flip -- so the verdict does not rest
                           on any one quoted value.
  2.3e17 kg/m^3          : the tree's OWN saturation density (warpdrive.py:148,
                           emwarp.py:225, drivespec.py:39).
"""
import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "codata", "x"))
try:
    from scipy.constants import physical_constants as pc, c, G, eV
    MN = pc["neutron mass energy equivalent in MeV"][0]
    MP = pc["proton mass energy equivalent in MeV"][0]
    SRC = "CODATA-2018 via scipy 1.17.1"
except Exception:
    c, G, eV = 299792458.0, 6.67430e-11, 1.602176634e-19
    MN, MP = 939.56542194, 938.27208943
    SRC = "CODATA-2018 hard-coded fallback"
import sympy as sp

ok = True
def chk(label, got, want=True):
    global ok
    flag = (got == want)
    ok &= flag
    print("  [%s] %s -> %s" % ("PASS" if flag else "FAIL", label, got))

MEVFM3 = 1e6 * eV / 1e-45          # 1 MeV fm^-3 in J m^-3 (= Pa)
TREE_NUC = 1.0e35                  # seatindex.py:370,375
TREE_RHO = 2.3e17                  # kg m^-3, warpdrive.py:148
print("constants:", SRC, " c=%.0f G=%.5e  1 MeV/fm^3 = %.6e Pa" % (c, G, MEVFM3))

# 1. the tree's coefficient and the 100 km figure
T_COEFF = math.pi * c**4 / (4 * G)
t100 = T_COEFF / 1e10
print("\n1. T_COEFF = %.6e Pa m^2 ; tkk_required(100 km) = %.6e Pa = %.2f MeV/fm^3"
      % (T_COEFF, t100, t100 / MEVFM3))
chk("T_COEFF matches tree 9.50536e43 to 1e39", abs(T_COEFF - 9.50536e43) < 1e39)
chk("tkk(1e5) matches canonical data_used 9.5054e33", abs(t100 - 9.5054e33) / 9.5054e33 < 1e-4)

# 2. what 1e35 Pa is, in nuclear units
print("\n2. the tree's 1e35 Pa = %.1f MeV/fm^3" % (TREE_NUC / MEVFM3))
mN = 0.5 * (MN + MP)
EA = -16.0   # MeV, conventional binding per nucleon at saturation (NOT READ here)
print("   saturation energy density eps0 = n0 (m_N c^2 + E/A), m_N = %.4f MeV, E/A = %g MeV" % (mN, EA))
print("   %6s %14s %14s %12s %14s" % ("n0", "eps0 (Pa)", "rho0 (kg/m3)", "1e35/eps0", "tkk100/eps0"))
rows = []
for n0 in (0.145, 0.150, 0.155, 0.160, 0.165, 0.170):
    eps0 = n0 * (mN + EA) * MEVFM3
    rho0 = n0 * 1e45 * mN * 1e6 * eV / c**2
    rows.append((n0, eps0))
    print("   %6.3f %14.4e %14.4e %12.3f %14.3f" % (n0, eps0, rho0, TREE_NUC / eps0, t100 / eps0))
eps_tree = TREE_RHO * c**2
print("   tree's own rho=2.3e17 kg/m^3 -> eps = %.4e Pa ; 1e35/eps = %.3f ; tkk100/eps = %.3f"
      % (eps_tree, TREE_NUC / eps_tree, t100 / eps_tree))
chk("1e35 Pa exceeds saturation energy density for every scanned n0 (overstated)",
    all(TREE_NUC > e for _, e in rows))
chk("1e35 overstates eps0 by a factor between 3.9 and 4.7 over the scan",
    all(3.9 < TREE_NUC / e < 4.7 for _, e in rows))
chk("1e35 is 4.84x the tree's own 2.3e17 kg/m^3 (internal inconsistency)",
    round(TREE_NUC / eps_tree, 2) == 4.84)

# 3. does the conclusion move?  'at 100 km the requirement is BELOW nuclear density'
chk("VERDICT with tree's 1e35: tkk(100 km) < 1e35", t100 < TREE_NUC)
chk("VERDICT with every scanned n0: tkk(100 km) < eps0", all(t100 < e for _, e in rows))
chk("VERDICT with tree's own 2.3e17 kg/m^3: tkk(100 km) < rho c^2", t100 < eps_tree)
n0_star = t100 / ((mN + EA) * MEVFM3)
print("   break-even n0 (conclusion flips below it) = %.4f fm^-3 = %.2f of 0.16" % (n0_star, n0_star / 0.16))
chk("break-even n0 < 0.10 fm^-3 (far below any quoted saturation density)", n0_star < 0.10)
# with p added (T_kk = eps + p): p >= 0 at and above saturation only helps
print("   margin at 100 km: 1e35 gives x%.2f ; eps0(0.16) gives x%.2f ; tree 2.3e17 gives x%.2f"
      % (TREE_NUC / t100, rows[3][1] / t100, eps_tree / t100))

# 4. where the crossover really sits ('below nuclear density beyond about 100 km', :406)
for lab, e in (("1e35 Pa", TREE_NUC), ("eps0(n0=0.16)", rows[3][1]),
               ("eps0(n0=0.15)", rows[1][1]), ("eps0(n0=0.17)", rows[5][1]),
               ("tree 2.3e17 c^2", eps_tree)):
    print("   crossover l* = sqrt(T_COEFF/eps) for %-16s = %6.1f km" % (lab, math.sqrt(T_COEFF / e) / 1e3))
lstar = [math.sqrt(T_COEFF / e) / 1e3 for _, e in rows]
chk("true crossover lies in 60-70 km for all scanned n0 (tree's 1e35 implies 30.8 km)",
    all(60 < x < 70 for x in lstar))
chk("100 km lies beyond the crossover in every case", all(x < 100 for x in lstar))

# 5. sympy: T_kk for a perfect fluid, and what a region at threshold density weighs
e, p, g, v = sp.symbols("epsilon p gamma v", positive=True)
# fluid rest frame u=(1,0,0,0); null k=(w,w,0,0); T_ab = (e+p) u_a u_b + p eta_ab, eta=diag(-1,1,1,1)
w = sp.symbols("w", positive=True)
eta = sp.diag(-1, 1, 1, 1)
u = sp.Matrix([1, 0, 0, 0]); k = sp.Matrix([w, w, 0, 0])
ul = eta * u
T = (e + p) * ul * ul.T + p * eta
Tkk = sp.simplify((k.T * T * k)[0])
print("\n5. perfect fluid: T_kk =", Tkk, " (k^0 = w in the fluid frame)")
chk("T_kk = (eps + p) w^2 -- equals eps only if p=0 and w=1 (named normalisation)",
    sp.simplify(Tkk - (e + p) * w**2) == 0)
l, a = sp.symbols("l a", positive=True)
Gs, cs = sp.symbols("G c", positive=True)
eps_th = sp.pi * cs**4 / (4 * Gs * l**2)
M_ball = sp.Rational(4, 3) * sp.pi * (l / 2)**3 * eps_th / cs**2
compact = sp.simplify(2 * Gs * M_ball / ((l / 2) * cs**2))
print("   uniform ball of DIAMETER l at threshold: 2GM/(Rc^2) =", compact, "=", float(compact))
chk("ball compactness pi^2/6 > 1 for EVERY l (beyond Buchdahl 8/9) -- a geometry hypothesis",
    compact == sp.pi**2 / 6)
mu = sp.pi * a**2 * eps_th / cs**2
rod = sp.simplify(Gs * mu / cs**2)
print("   thin rod radius a, length l: G mu/c^2 =", rod, "(small when a << l)")
chk("rod G mu/c^2 = pi^2 a^2/(4 l^2)", sp.simplify(rod - sp.pi**2 * a**2 / (4 * l**2)) == 0)
# canonical NS (1.4 Msun, R=12 km; values NOT READ here, illustrative only)
Msun = 1.98841e30
M, R = 1.4 * Msun, 1.2e4
eps_avg = M * c**2 / (4 / 3 * math.pi * R**3)
print("   illustrative NS 1.4 Msun, R 12 km: <eps> = %.3e Pa = %.2f x eps0(0.16); threshold at l=2R = %.3e; Sturm ratio = %.3f"
      % (eps_avg, eps_avg / rows[3][1], T_COEFF / (2 * R)**2, eps_avg / (T_COEFF / (2 * R)**2)))

print("\nSELFTEST %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
