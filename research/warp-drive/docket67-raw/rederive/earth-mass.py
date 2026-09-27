#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'earth-mass' (ladder.M_EARTH = 5.9722e24 kg).
Read-only against research/warp-drive (no bytecode written).  Exits 1 on a failed check."""
import sys, math
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import sympy as sp

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok: fails.append(name)

TREE_M = 5.9722e24
# --- inputs, with their read status -------------------------------------------------
GM_NOM   = 3.986004e14      # READ: Prsa et al. 2016 (arXiv:1605.09788) Table 1, (GM)^N_E, exact by definition
GM_TCG   = 3.986004419e14   # READ-VIA-RESTATEMENT: Jentschura 2026 (arXiv:2609.09485) p.3 "398600.4419(2) km^3/s^2" (citing Dunn & Torrence 1999); IAU 2009 3.986004418e14+-8e5 (Luzum 2011) NAMED-NOT-READ
U_GM     = 0.0002e9 * 1e0   # 0.0002 km^3/s^2 = 2e5 m^3/s^2 (Jentschura's quoted uncertainty)
GM_DE440 = 3.98600435507e14 # restated: Jentschura 2026 p.3 quoting DE440 Table 2 (TDB-compatible)
L_B      = 1.550519768e-8   # IAU 2006 B3 defining constant TCB->TDB (recalled, standard)
G = {"CODATA2006": (6.67428e-11, None),              # READ via Prsa 2016 App. A (NSFA recommendation)
     "CODATA2014": (6.67408e-11, 0.00031e-11),       # READ: Prsa 2016 rec. 5
     "CODATA2018=2022": (6.67430e-11, 0.00015e-11)}  # READ: CODATA 2022 (arXiv:2409.03787) Table XXXII; identical to 2018 (sec XIV)

print("1. M_E = GM_E / G  (IAU 2015 B3 recommendation 5: SI mass must be (GM)/G with G stated)")
for k, (g, ug) in G.items():
    for gmname, gm in (("GM_TCG", GM_TCG), ("GM_nominal", GM_NOM)):
        m = gm / g
        um = m * math.hypot(ug / g if ug else 0.0, U_GM / gm if gmname == "GM_TCG" else 0.0)
        print("   %-16s %-11s M = %.6e kg  +- %s   rounds(5sf)-> %.4e" %
              (k, gmname, m, ("%.1e" % um) if ug else "n/a", float("%.4e" % m)))

g18, ug18 = G["CODATA2018=2022"]
m18 = GM_TCG / g18
um18 = m18 * ug18 / g18
chk("tree 5.9722e24 equals GM_E/G(CODATA2018/2022) rounded to 5 s.f.",
    float("%.4e" % m18) == TREE_M, "M=%.6e +- %.1e" % (m18, um18))
chk("tree value within 1 sigma(G) of GM_E/G(CODATA2018/2022)",
    abs(TREE_M - m18) < um18, "|diff|=%.2e vs sigma=%.2e (%.2f sigma)" % (abs(TREE_M - m18), um18, abs(TREE_M - m18) / um18))
m14 = GM_TCG / G["CODATA2014"][0]
chk("with CODATA 2014 G the 5-s.f. value would be 5.9724e24 (tree value is NOT CODATA-2014 based)",
    float("%.4e" % m14) == 5.9724e24, "%.6e" % m14)
chk("relative uncertainty of M_E is set by G, not GM: u_r(G)/u_r(GM) > 1e4",
    (ug18 / g18) / (U_GM / GM_TCG) > 1e4, "u_r(G)=%.1e  u_r(GM)=%.1e" % (ug18 / g18, U_GM / GM_TCG))

print("\n2. Internal consistency of the tree's pair (G, M_EARTH) against GM_E")
gm_tree = g18 * TREE_M
print("   G*M_EARTH = %.9e ; GM_E(TCG) = %.9e ; ratio-1 = %.2e" % (gm_tree, GM_TCG, gm_tree / GM_TCG - 1))
chk("tree's G*M_EARTH reproduces GM_E to the 5-s.f. rounding of M (|ratio-1| < 1e-5)",
    abs(gm_tree / GM_TCG - 1) < 1e-5)

print("\n3. The DE440 'disagreement' restated by Jentschura 2026 vs the TCB->TDB scaling")
gm_tdb = GM_TCG * (1 - L_B)
print("   GM_TCG*(1-L_B) = %.9e ; DE440 = %.9e ; rel diff = %.2e" % (gm_tdb, GM_DE440, gm_tdb / GM_DE440 - 1))
chk("DE440 GM_E agrees with the SLR/TCG value after the TDB scaling to < 1e-9 (not a physical disagreement)",
    abs(gm_tdb / GM_DE440 - 1) < 1e-9)
chk("either GM_E moves M_E by far less than the tree's 5-s.f. rounding (5e-6)",
    abs(GM_DE440 / GM_TCG - 1) < 5e-6, "%.1e" % abs(GM_DE440 / GM_TCG - 1))

print("\n4. The tree's uses")
import ladder, stockgate, formation
chk("ladder.M_EARTH is 5.9722e24", ladder.M_EARTH == TREE_M)
need = stockgate.feedstock_kg(70.0, "as-composed 59", "CI chondrite")
r = formation.proxima_b_over_threshold()
print("   need = %.6g kg ; ratio = %.6e ; log10 = %.4f" % (need, r, math.log10(r)))
chk("formation.proxima_b_over_threshold() == 1.3*M_EARTH/need", abs(r - 1.3 * TREE_M / need) / r < 1e-15)
# sensitivity (symbolic)
M, ms, nd = sp.symbols("M m_sini need", positive=True)
R = ms * M / nd
el = sp.simplify(sp.diff(sp.log(R), M) * M)
chk("elasticity d ln(ratio)/d ln(M_E) = 1 (sympy)", el == 1, str(el))
flip = 1.0 / r   # factor by which M_E would have to shrink to flip '> 1'
chk("the comparison '> 1' flips only if M_E were smaller by a factor ~1e22", flip < 1e-21, "factor %.2e" % flip)
lo, hi = [GM_TCG / (g18 + s * 5 * ug18) for s in (+1, -1)]
chk("across M_E(5 sigma of G) the verdict log10(ratio) > 0 is unchanged",
    all(math.log10(1.3 * m / need) > 0 for m in (lo, hi, GM_TCG / 6.67191e-11, GM_TCG / 6.67559e-11)),
    "log10 ratio spread %.2e" % (math.log10(hi / lo)))
# ladder's own 4-decimal pin EXCHANGE_KG/M_EARTH = 22.5871
pin_tree = float("%.4f" % (ladder.EXCHANGE_KG / ladder.M_EARTH))
pin_gm = float("%.4f" % (ladder.c ** 2 / (ladder.LAMBDA * GM_TCG)))   # G-free form
print("   ladder pin: tree %.4f ; G-free c^2/(Lambda*GM_E) %.4f" % (pin_tree, pin_gm))
chk("ladder.py's pin 22.5871 reproduces with the tree's own constants", pin_tree == 22.5871)
print("   NOTE (context, not the entry's use; recorded, not a failure): the 4th decimal of ladder's pin is an artefact"
      " of rounding M_EARTH to 5 s.f.: tree %.6f vs G-free %.6f -> %s" % (ladder.EXCHANGE_KG / ladder.M_EARTH,
      ladder.c ** 2 / (ladder.LAMBDA * GM_TCG), "DIFFERS at 4th decimal" if pin_gm != pin_tree else "same"))

print("\n%d check(s) failed" % len(fails) if fails else "\nALL CHECKS PASS")
sys.exit(1 if fails else 0)
