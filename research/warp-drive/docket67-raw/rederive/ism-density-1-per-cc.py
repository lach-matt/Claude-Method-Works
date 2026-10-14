#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key ism-density-1-per-cc.

Reads research/warp-drive/{arrival,stock,stockgate}.py READ-ONLY (bytecode
writing disabled, nothing under research/ is touched) and recomputes every
number that rests on RHO_ISM = 1e6 * 1.67262192e-27 kg/m^3 against the
densities READ at source:
  Ferriere 2001 (astro-ph/0106359) p.5, Table I p.36-37, Fig.2 caption p.38
  Crawford 2011 (arXiv:1010.4823) Table 4 p.22, sec.3 p.7-8, concl.(3) p.15
  Frisch & Mueller 2011 (arXiv:1010.4507) p.3 (SF08 Model 26), p.4
  Gros 2017 (arXiv:1707.02801) sec.2.1-2.2 p.2-3
  CODATA 2022 (arXiv:2409.03787) Table XXXII p.50
Exit 0 when every assertion holds.
"""
import sys, math, importlib.util
sys.dont_write_bytecode = True
from fractions import Fraction as F

WD = "/home/user/Claude-Method-Works/research/warp-drive/"
def load(name):
    spec = importlib.util.spec_from_file_location("d67_" + name, WD + name + ".py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

arr, stk, sg = load("arrival"), load("stock"), load("stockgate")
AU, LY = arr.AU, arr.LY

print("1. The tree's datum, exactly")
rho_tree = F(10**6) * F("1.67262192e-27")
chk("arrival/stock/stockgate RHO_ISM agree exactly",
    arr.RHO_ISM == stk.RHO_ISM == sg.RHO_ISM == float(rho_tree), "%.9e kg/m^3" % float(rho_tree))

print("2. Proton mass: tree vs CODATA 2018 / 2022, and m_p vs m_H")
mp_tree, mp18, mp22 = 1.67262192e-27, 1.67262192369e-27, 1.67262192595e-27
mH = 1.00782503223 * 1.66053906892e-27      # 1H atomic mass (AME) x u (CODATA 2022)
for lab, v in (("CODATA2018", mp18), ("CODATA2022", mp22), ("m(1H atom)", mH)):
    print("     tree/%s - 1 = %.3e" % (lab, mp_tree / v - 1))
chk("proton-mass truncation moves rho by < 1e-8 (immaterial)", abs(mp_tree / mp22 - 1) < 1e-8)
chk("m_p vs m_H moves rho by < 1e-3 (immaterial)", abs(mp_tree / mH - 1) < 1e-3)

print("3. Ferriere 2001: 'average of about 2.7e-24 g cm^-3 ... approximately one H atom per cm^3'")
rho_avg = 2.7e-24 * 1e3                       # kg/m^3
n_equiv = rho_avg / (1.42 * mp22) / 1e6       # Ferriere's own rho = 1.42 m_P n
print("     2.7e-24 g/cc = %.3e kg/m^3 = %.3f x tree rho; n_H = %.3f cm^-3 at 1.42 m_p"
      % (rho_avg, rho_avg / float(rho_tree), n_equiv))
chk("Ferriere average is ~1 H/cc (0.8 < n_H < 1.3) -- the tree's number as a SPACE AVERAGE",
    0.8 < n_equiv < 1.3)
chk("but mass density with He (x1.42) is 1.4-1.7x the tree's n*m_p",
    1.4 < rho_avg / float(rho_tree) < 1.7)

print("4. The phases and the local medium, READ values of n_H (cm^-3)")
MEDIA = [  # label, n_H total (nuclei), n_ion (protons), source
    ("tree (arrival.py:26)",              1.0,    1.0,   "tree: all protons"),
    ("Ferriere WNM lo",                    0.2,    None,  "astro-ph/0106359 Table I"),
    ("Ferriere WNM hi",                    0.5,    None,  "astro-ph/0106359 Table I"),
    ("CHISM (Crawford T4)",                0.26,   0.07,  "1010.4823 Table 4"),
    ("CHISM SF08 Model 26",                0.19 + 0.055, 0.055, "1010.4507 p.3"),
    ("LIC n_e Redfield&Falcon",            None,   0.12,  "1010.4823 p.7"),
    ("Icarus range lo",                    0.15,   0.05,  "1010.4823 Table 4"),
    ("Icarus range hi",                    0.43,   0.21,  "1010.4823 Table 4"),
    ("Local Bubble (hot)",                 0.005,  0.005, "1010.4823 Table 4 note"),
    ("Local Bubble (Welsh-Shelton alt.)",  0.04,   0.04,  "1010.4823 Table 4 note"),
]
chk("the tree's n=1 lies ABOVE Ferriere's WNM range 0.2-0.5 (label 'warm neutral medium' is a discrepancy)",
    1.0 > 0.5)
chk("the tree's n=1 lies above every READ local total density (max 0.43)", 1.0 > 0.43)

print("5. What rests on it: recompute each consequent at each READ density")
v0, r0 = stk.ism_sweep_volume()
print("     stock.ism_sweep_volume() now returns %.4e m^3, r = %.4e km" % (v0, r0 / 1e3))
print("     DISCREPANCY (tree-internal, not density-caused): stock.py:119-120 and stockgate.py:201"
      " print 7.18e25 m^3 / 2.58e5 km; the function returns %.3fx that volume at the SAME RHO_ISM"
      % (v0 / 7.18e25))
chk("stock sweep volume is within 15% of its prose 7.18e25 (same order; the gap is not from RHO_ISM)",
    abs(v0 / 7.18e25 - 1) < 0.15)
chk("stock sweep equals feedstock/RHO_ISM exactly (the density enters only as 1/rho)",
    abs(v0 - stk.feedstock_kg(70.0, None, stk.cosmic()) / stk.RHO_ISM) < 1e-6 * v0)
L0 = arr.magsail_distance(1e6, 0.0476, 1e12) / AU
chk("arrival.py magsail floor at the tree's density reproduced (selftest pins 2001.64 AU)",
    abs(L0 - 2001.64) < 0.01, "%.2f AU" % L0)
print("     %-34s %9s %9s %12s %12s %14s" % ("medium", "n_H", "n_ion", "V/V_tree", "r (km)",
                                             "magsail AU(ion)"))
worst_stock = 0; mags = {}
for lab, nH, ni, src in MEDIA:
    if nH is not None:
        rho = 1.42 * mp22 * nH * 1e6 if lab[:4] != "tree" else float(rho_tree)
        ratio = float(rho_tree) / rho
        r = r0 * ratio ** (1 / 3)
        worst_stock = max(worst_stock, 1 / ratio)
    else:
        ratio, r = float("nan"), float("nan")
    if ni is not None:
        Lm = L0 * 1.0 / ni        # L ∝ 1/n at fixed drag law F = rho v^2 A, ions only
        mags[lab] = Lm
    else:
        Lm = float("nan")
    print("     %-34s %9s %9s %12.3f %12.4e %14.0f" % (lab, nH, ni, ratio, r / 1e3, Lm))

print("6. Does the move change the conclusions?")
# stock: the conclusion is 'the diffuse medium fails' because the sweep is enormous.
chk("stock.py: at every READ diffuse density (He included) the sweep is LARGER or within 1.5x smaller"
    " -- the most favourable diffuse medium (WNM hi, 0.5 x 1.42) gives V/V_tree >= 1.40",
    min(float(rho_tree) / (1.42 * mp22 * n * 1e6) for n in (0.2, 0.5, 0.26, 0.15, 0.43, 0.245)) >= 1.40)
chk("stock.py 'sweep radius > 1e5 km' (stockgate :1076) holds at every READ diffuse density",
    all(r0 * (float(rho_tree) / (1.42 * mp22 * n * 1e6)) ** (1 / 3) / 1e3 > 1e5
        for n in (0.2, 0.5, 0.26, 0.15, 0.43, 0.245, 0.005, 0.04)))
# Break-even for stock: what density would bring the sweep radius under 1e5 km?
n_break = (r0 / 1e8) ** 3 * float(rho_tree) / (1.42 * mp22) / 1e6
print("     stock radius falls below 1e5 km only above n_H = %.1f cm^-3 (a cold-cloud density,"
      " Ferriere CNM 20-50)" % n_break)
chk("that break-even density (>1 cm^-3) is outside every diffuse phase READ", n_break > 1.0)
# arrival: 'inside 810 AU (prose) / 2002 AU (computed) -- comfortably within a target system'
alpha_cen_AU = 4.37 * LY / AU
for lab in ("CHISM (Crawford T4)", "LIC n_e Redfield&Falcon", "Icarus range lo", "Local Bubble (hot)"):
    print("     magsail floor on the ionised component, %-26s %9.0f AU = %.3f ly"
          % (lab, mags[lab], mags[lab] * AU / LY))
chk("arrival.py: on the READ ionised density the floor rises >= 4.7x (Icarus hi 0.21) to 200x (LB)",
    min(mags[k] for k in mags if k[:4] != "tree") / L0 >= 1 / 0.21 - 1e-9)
chk("arrival.py: in the hot Local Bubble the floor (~4e5 AU) EXCEEDS the whole 4.37 ly trip",
    mags["Local Bubble (hot)"] > alpha_cen_AU, "%.0f AU vs %.0f AU" % (mags["Local Bubble (hot)"], alpha_cen_AU))
chk("arrival.py: on the CHISM ion density the floor is still < trip length (braking still possible,"
    " but ~0.45 ly out -- not 'within a target system')",
    L0 < mags["CHISM (Crawford T4)"] < alpha_cen_AU)

print("7. Tree-internal discrepancy (recorded, NOT caused by the external datum)")
print("     arrival.py prose :151/:159 says 810 AU; its own selftest (:95) pins %.2f AU at the"
      " same RHO_ISM. ratio %.3f" % (L0, L0 / 810))
chk("810 AU is NOT what magsail_distance returns at the tree's density", abs(L0 - 810) > 100)
print("\n  REDERIVE %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
