#!/usr/bin/env python3
"""
DOCKET 67, pass S, result 20 -- planck-energy.

Re-derives E_P = sqrt(hbar c^5 / G) as warpfolder.py:292-293 uses it, checks it
against the CODATA 2022 table (as transcribed in scipy 1.17.1 _codata.py, the
copy held in this scratchpad), and tests whether warpfolder's conclusion
REACHES_PLANCK_THRESHOLD = False survives every convention and every reading of
the document's words "Optical Intensity Spikes to Planck Threshold".

Stdlib + sympy.  Exits 1 on any failed assertion.
"""
import math
import re
import sys
import os

import sympy as sp

FAIL = []


def chk(label, ok, detail=""):
    print("  [%s] %-62s %s" % ("ok" if ok else "FAIL", label, detail))
    if not ok:
        FAIL.append(label)


# ------------------------------------------------------------------ 1. sympy
print("1. DIMENSIONAL UNIQUENESS (sympy)")
a, b, d = sp.symbols("a b d")
# [hbar] = M L^2 T^-1, [c] = L T^-1, [G] = M^-1 L^3 T^-2 ; target energy M L^2 T^-2
eqs = [sp.Eq(a - d, 1),                 # M
       sp.Eq(2 * a + b + 3 * d, 2),     # L
       sp.Eq(-a - b - 2 * d, -2)]       # T
sol = sp.solve(eqs, [a, b, d], dict=True)
chk("hbar^a c^b G^d is an energy only for (1/2, 5/2, -1/2)",
    sol == [{a: sp.Rational(1, 2), b: sp.Rational(5, 2), d: sp.Rational(-1, 2)}],
    str(sol))
M = sp.Matrix([[1, 0, -1], [2, 1, 3], [-1, -1, -2]])
chk("the exponent system is non-singular (det != 0) -> unique",
    M.det() != 0, "det=%s" % M.det())
print("     => E_P is fixed up to a DIMENSIONLESS factor; h vs hbar vs 8piG is")
print("        exactly that freedom and nothing else.")

# ------------------------------------------------------------ 2. constants
print("\n2. CONSTANTS: tree (ladder.py) vs CODATA 2022 (scipy 1.17.1 transcription)")
c = 2.99792458e8           # ladder.py:53
G_tree = 6.67430e-11       # ladder.py:54
HBAR = 1.054571817e-34     # ladder.py:55
H = 6.62607015e-34         # SI exact
EV = 1.602176634e-19       # SI exact

here = os.path.dirname(os.path.abspath(__file__))
cod = os.path.join(here, "..", "src", "codata", "x", "scipy", "constants",
                   "_codata.py")
txt = open(cod).read()
t22 = txt[txt.index('txt2022 = """'):]
t22 = t22[:t22.index('"""', 15)]
t18 = txt[txt.index('txt2018 = """'):]
t18 = t18[:t18.index('"""', 15)]


def row(t, name):
    for line in t.splitlines():
        if line.startswith(name + "  "):
            f = re.split(r"\s{2,}", line.strip())
            v = float(f[1].replace(" ", "").replace("...", ""))
            u = f[2]
            u = None if "exact" in u else float(u.replace(" ", ""))
            return v, u
    raise KeyError(name)


G22, uG22 = row(t22, "Newtonian constant of gravitation")
G18, _ = row(t18, "Newtonian constant of gravitation")
mP22, umP22 = row(t22, "Planck mass")
EPGeV22, uEPGeV22 = row(t22, "Planck mass energy equivalent in GeV")
lP22, _ = row(t22, "Planck length")
hb22, _ = row(t22, "reduced Planck constant")
chk("G(tree) == G(CODATA 2022) == G(CODATA 2018)",
    G_tree == G22 == G18, "%.5e, u_r=%.1e" % (G22, uG22 / G22))
chk("hbar(tree) == CODATA 2022 (exact since the 2019 SI)",
    abs(HBAR / hb22 - 1) < 1e-9)

EP = math.sqrt(HBAR * c ** 5 / G_tree)
print("     E_P (tree formula)            = %.6e J" % EP)
chk("E_P matches the canonical 'E_P ~ 1.956e9 J'", abs(EP / 1.956e9 - 1) < 1e-3)
chk("CODATA m_P c^2 reproduces it (CODATA m_P = (hbar c/G)^1/2)",
    abs(mP22 * c ** 2 / EP - 1) < 2e-6,
    "m_P c^2 = %.6e J" % (mP22 * c ** 2))
chk("CODATA E_P in GeV reproduces it",
    abs(EPGeV22 * 1e9 * EV / EP - 1) < 2e-6,
    "%.6e J" % (EPGeV22 * 1e9 * EV))
chk("CODATA l_P = (hbar G/c^3)^1/2 -> hbar convention confirmed",
    abs(math.sqrt(HBAR * G_tree / c ** 3) / lP22 - 1) < 2e-6)
urel = 0.5 * uG22 / G22
print("     relative standard uncertainty of E_P = u_r(G)/2 = %.2e" % urel)
chk("E_P uncertainty cannot move a ratio at the 1e-3 level", urel < 1e-4)

# ------------------------------------------------------ 3. device energies
print("\n3. THE DEVICE SIDE (warpfolder.py constants; document re-read on Drive)")
marx = 10 * 0.5 * 100e-9 * (50e3) ** 2
area_cm2 = math.pi * (0.1e-3 * 100 / 2) ** 2
laser_tree = 1e20 * area_cm2 * 30e-15
laser_10PW = 10e15 * 30e-15            # document header "PEAK POWER: 10 Petawatts"
I_10PW = 10e15 / area_cm2
print("     Marx 10 x 100 nF @ 50 kV       = %.1f J" % marx)
print("     laser, tree (1e20 W/cm^2)      = %.1f J" % laser_tree)
print("     laser, doc 10 PW x 30 fs       = %.1f J  (I = %.3e W/cm^2 at 0.1 mm)"
      % (laser_10PW, I_10PW))
frac_tree = (marx + laser_tree) / EP
chk("warpfolder fraction 7.595e-7 re-derived", abs(frac_tree / 7.595e-7 - 1) < 1e-3,
    "%.4e" % frac_tree)
chk("10 PW over the 0.1 mm spot is consistent with 'exceeding 1e20'",
    I_10PW > 1e20, "%.3e" % I_10PW)

budgets = {"Marx only (lasers driven by Marx pulse)": marx,
           "tree: Marx + laser(1e20)": marx + laser_tree,
           "Marx + laser(10 PW)": marx + laser_10PW}
conv = {"hbar (CODATA)": EP,
        "h (Planck 1899 form, x sqrt(2pi))": math.sqrt(H * c ** 5 / G_tree),
        "reduced, 8piG": math.sqrt(HBAR * c ** 5 / (8 * math.pi * G_tree))}
lo, hi = 1e99, 0
for kc, Ec in conv.items():
    for kb, Eb in budgets.items():
        f = Eb / Ec
        lo, hi = min(lo, f), max(hi, f)
        print("     %-34s %-40s %.3e" % (kc, kb, f))
chk("every convention x budget stays below 1 (energy reading)", hi < 1,
    "range %.2e .. %.2e" % (lo, hi))
print("     orders short, best case for the device: %.2f" % -math.log10(hi))

# -------------------------------------------- 4. the other readings of the doc
print("\n4. THE DOCUMENT SAYS 'OPTICAL INTENSITY', NOT ENERGY")
P_P = c ** 5 / G_tree
lP = math.sqrt(HBAR * G_tree / c ** 3)
I_P = P_P / lP ** 2                      # = c^8/(hbar G^2), W/m^2
u_P = EP / lP ** 3                       # = c^7/(hbar G^2), J/m^3
chk("I_P = c^8/(hbar G^2) identity", abs(I_P / (c ** 8 / (HBAR * G_tree ** 2)) - 1) < 1e-12)
I_doc = max(1e20, I_10PW) * 1e4          # W/m^2, the generous figure
r_I = I_doc / I_P
u_doc = I_doc / c
r_u = u_doc / u_P
E_ph = H * c / 800e-9                    # 800 nm Ti:Sapphire, document sect. 2.1
r_ph = E_ph / EP
eps0 = 8.8541878188e-12
E_laser_field = math.sqrt(2 * I_doc / (c * eps0))
E_planck_field = math.sqrt(c ** 7 / (4 * math.pi * eps0 * HBAR * G_tree ** 2))
r_F = E_laser_field / E_planck_field
print("     Planck intensity c^8/(hbar G^2) = %.3e W/cm^2 ; doc %.3e -> ratio %.2e"
      % (I_P * 1e-4, I_doc * 1e-4, r_I))
print("     Planck energy density           = %.3e J/m^3 ; laser %.3e -> ratio %.2e"
      % (u_P, u_doc, r_u))
print("     per quantum: 800 nm photon %.3f eV / E_P %.4e eV -> ratio %.2e"
      % (E_ph / EV, EP / EV, r_ph))
print("     field: laser %.2e V/m / Planck field %.2e V/m -> ratio %.2e"
      % (E_laser_field, E_planck_field, r_F))
chk("intensity reading: short by > 90 orders", r_I < 1e-90, "%.2e" % r_I)
chk("energy-density reading: short by > 90 orders", r_u < 1e-90)
chk("per-quantum reading: short by > 25 orders", r_ph < 1e-25)
chk("field reading: short by > 45 orders", r_F < 1e-45)
chk("the energy reading the tree uses is the MOST generous of the five",
    frac_tree > max(r_I, r_u, r_ph, r_F))

# ------------------------------------ 5. is E_P a threshold on TOTAL energy?
print("\n5. E_P AS A TOTAL-ENERGY THRESHOLD: a computed counterexample")
mP = EP / c ** 2
kg_tnt = EP / 4.184e6                    # TNT 4.184 MJ/kg, by definition
print("     E_P is the rest energy of %.2f micrograms" % (mP * 1e9))
print("     and the yield of %.0f kg TNT" % kg_tnt)
chk("a 1 mg grain has rest energy > E_P with no Planck-scale physics",
    1e-6 * c ** 2 > EP, "%.2e J" % (1e-6 * c ** 2))
print("     => E_P as a TOTAL energy is exceeded by ordinary matter, so it is not")
print("        a threshold for Planck-scale physics read that way.  The usual")
print("        reading (per quantum / localised within l_P) is the standard")
print("        dimensional heuristic -- NAMED-NOT-READ here (alphaXiv/arXiv down).")
print("        The tree's conclusion survives it (sect. 4); its 7.6e-7 figure")
print("        is a statement about total energy only.")

# ------------------------------------------- 6. M's hypothesis: moved data
print("\n6. WHAT WOULD A MOVED DATUM HAVE TO DO?  (E_P ~ G^-1/2)")
need_tree = (1 / frac_tree) ** 2
need_best = (1 / hi) ** 2
print("     G must grow x%.3e (tree case) or x%.3e (most generous case)"
      % (need_tree, need_best))
print("     for the energy reading to reach 1; CODATA u_r(G) = %.1e" % (uG22 / G22))
chk("no plausible revision of G moves the conclusion", need_best > 1e10)
print()
if FAIL:
    print("FAILED: %d" % len(FAIL))
    sys.exit(1)
print("ALL CHECKS PASS")
