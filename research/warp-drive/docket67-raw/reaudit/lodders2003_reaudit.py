"""DOCKET 67 re-audit: Lodders 2003 (ApJ 591, 1220) READ from M's Drive copy
(fileId 1dxtorrPjr43Bu7Jaq3TdGI8t0ADCd22N).  Imports the tree READ-ONLY.
Table 3 (PDF pp.6-7 = journal pp.1225-1226) and Table 8 (PDF pp.20-21 =
journal pp.1239-1240) transcribed from the Drive text extraction.
"""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import stockgate as sg
import stock as st

FAIL = []
def chk(label, ok):
    print(("  PASS " if ok else "  FAIL ") + label)
    if not ok: FAIL.append(label)

# ---- L03 Table 3: CI group weighted mean, 1 sigma, N_met (ppm by mass)
T3 = {  # e: (mean, sigma, n_met)   sigma None where extraction ambiguous
 "H": (21015, 1770, 4), "Li": (1.46, 0.03, 2), "Be": (0.0252, 0.005, None),
 "B": (0.713, 0.072, 2), "C": (35180, 4810, 5), "N": (2940, 20, 2),
 "O": (458200, 5750, 2), "F": (60.6, 4.1, 2), "Na": (5010, 33, 3),
 "Mg": (95870, 780, 3), "Al": (8500, 130, 3), "Si": (106500, 1250, 2),
 "P": (920, 100, 1), "S": (54100, 3650, 5), "Cl": (704, 10, 2),
 "K": (530, 24, 4), "Ca": (9070, 20, 3), "Sc": (5.83, 0.06, 4),
 "Ti": (440, None, None), "V": (55.7, 1.3, 3), "Cr": (2590, 80, 4),
 "Mn": (1910, 40, 3), "Fe": (182800, 1470, 4), "Co": (502, 17, 3),
 "Ni": (10640, 210, 3), "Cu": (127, 6, 4), "Zn": (310, 12, 4),
 "Ga": (9.51, 0.31, 4), "Ge": (33.2, 0.3, 3), "As": (1.73, 0.06, 4),
 "Se": (19.7, 0.4, 4), "Br": (3.43, 0.75, 3), "Rb": (2.13, 0.02, 2),
 "Sr": (7.74, 0.10, 2), "Y": (1.53, 0.12, 2), "Zr": (3.96, 0.11, 2),
 "Nb": (0.265, 0.016, 2), "Mo": (1.02, 0.11, 2), "Ag": (0.201, 0.004, 3),
 "Cd": (0.675, 0.006, 3), "In": (0.0788, 0.002, 3), "Sn": (1.68, 0.04, 3),
 "Sb": (0.152, 0.009, 3), "Te": (2.33, 0.18, 3), "I": (0.48, 0.16, 1),
 "Cs": (0.185, 0.002, 3), "Ba": (2.31, 0.03, 2), "La": (0.232, 0.010, 4),
 "Ce": (0.621, 0.022, 3), "Nd": (0.457, 0.011, 3), "Sm": (0.145, 0.002, 4),
 "Ta": (0.0144, 0.0001, 2), "W": (0.089, 0.007, 1), "Au": (0.146, 0.002, 2),
 "Hg": (0.314, 0.029, 2), "Tl": (0.143, 0.002, 3), "Pb": (2.56, 0.03, 2),
 "Bi": (0.110, 0.003, 2), "Th": (0.0309, None, None), "U": (0.0084, None, None),
}
ORGUEIL_N = (2948, 535, 5)   # Table 3, Orgueil column: mean, 1 sigma, N analyses
ALAIS_N = (2900, None, 1)
# ---- L03 Table 8: 50% T_C (K), solar-system composition, 1e-4 bar
T8 = {"Li":1142,"Be":1452,"B":908,"C":40,"N":123,"O":180,"F":734,"Ne":9.1,
 "Na":958,"Mg":1336,"Al":1653,"Si":1310,"P":1229,"S":664,"Cl":948,"Ar":47,
 "K":1006,"Ca":1517,"Sc":1659,"Ti":1582,"V":1429,"Cr":1296,"Mn":1158,
 "Fe":1334,"Co":1352,"Ni":1353,"Cu":1037,"Zn":726,"Ga":968,"Ge":883,
 "As":1065,"Se":697,"Br":546,"Kr":52,"Rb":800,"Sr":1464,"Y":1659,"Zr":1741,
 "Nb":1559,"Mo":1590,"Ru":1551,"Rh":1392,"Pd":1324,"Ag":996,"Cd":652,
 "In":536,"Sn":704,"Sb":979,"Te":709,"I":535,"Xe":68,"Cs":799,"Ba":1455,
 "La":1578,"Ce":1478,"Pr":1582,"Nd":1602,"Sm":1590,"Eu":1356,"Gd":1659,
 "Tb":1659,"Dy":1659,"Ho":1659,"Er":1659,"Tm":1659,"Yb":1487,"Lu":1659,
 "Hf":1684,"Ta":1573,"W":1789,"Re":1821,"Os":1812,"Ir":1603,"Pt":1408,
 "Au":1060,"Hg":252,"Tl":532,"Pb":727,"Bi":746,"Th":1659,"U":1610}
T8_APPEAR = {"H": 182, "He": "<3"}   # Table 8 col (2); col (4) printed "..."

print("=== 1. stockgate.TCOND vs L03 Table 8 (read)")
match, disc = 0, []
for e, v in sg.TCOND.items():
    if e.endswith("_"):
        disc.append((e, v, "sentinel key, not an element")); continue
    ref = T8.get(e)
    if ref is None:
        disc.append((e, v, "Table 8 50%% T_C '...'; appearance T_C = %s" % T8_APPEAR.get(e)))
    elif abs(v - ref) <= 0.5 or (e == "Ne" and round(ref) == v):
        match += 1
    else:
        disc.append((e, v, ref))
print("  %d TCOND element entries equal Table 8's 50%% T_C (Ne 9.1 -> 9)" % match)
for d in disc: print("  DISC", d)
chk("61 of 63 element entries match; H, He are not 50% values", match == 61)

print("\n=== 2. stockgate.CHONDRITE vs L03 Table 3 (read, all rows the tree carries)")
rows = []
for e, frac in sg.CHONDRITE.items():
    if e.endswith("_") or e not in T3: continue
    m, s, n = T3[e]
    tree = frac * 1e6
    r = tree / m
    z = (tree - m) / s if s else None
    rows.append((e, tree, m, s, n, r, z))
within = [r for r in rows if abs(r[5] - 1) <= 0.005]
within1s = [r for r in rows if r[6] is not None and abs(r[6]) <= 1]
out3s = [r for r in rows if r[6] is not None and abs(r[6]) > 3]
for e, tree, m, s, n, r, z in sorted(rows, key=lambda x: -abs(x[5]-1)):
    print("  %-2s tree %11.4g  L03 %11.4g +- %-8s Nmet %-4s ratio %.4f  z %s" %
          (e, tree, m, s, n, r, "%.1f" % z if z is not None else "-"))
print("  compared %d; within 0.5%%: %d; within 1 sigma: %d; beyond 3 sigma: %d" %
      (len(rows), len(within), len(within1s), len(out3s)))
print("  beyond 3 sigma:", [(r[0], round(r[6], 1)) for r in out3s])
print("  stock.CHONDRITE subset equal to stockgate:",
      all(abs(st.CHONDRITE[e] - sg.CHONDRITE[e]) < 1e-12 for e in st.CHONDRITE))
print("  sum(stockgate.CHONDRITE) = %.6f" % sum(v for k, v in sg.CHONDRITE.items()))

print("\n=== 3. Binder under the tree payload ('as-composed 59')")
p = sg.payload("as-composed")
def binder(stock):
    return sg.processing_factor(p, stock)
eT, fT = binder(sg.CHONDRITE)
print("  tree CHONDRITE: %s %.6f -> %.2f kg per 70 kg" % (eT, fT, 70 * fT))
chk("tree binder P at 10.7012 (749.08 kg)", eT == "P" and abs(fT - 10.70115) < 1e-3)
def variant(sub):
    s = dict(sg.CHONDRITE); s.update(sub); return binder(s)
for lab, sub in (("P -> 920 (L03)", {"P": 920e-6}), ("P -> 1020 (L03 +1s)", {"P": 1020e-6}),
                 ("P -> 820 (L03 -1s)", {"P": 820e-6}),
                 ("all L03 Table 3 rows", {e: v[0] * 1e-6 for e, v in T3.items()})):
    e, f = variant(sub)
    print("  %-24s binder %s %.4f  -> %.2f kg" % (lab, e, f, 70 * f))
eL, fL = variant({e: v[0] * 1e-6 for e, v in T3.items()})
chk("under all L03 rows the binder is P", eL == "P")
hN, hP = p["N"], p["P"]
print("  payload N/P mass ratio = %.4f" % (hN / hP))
for Pci in (1040, 920, 989):
    print("  crossover CI N (N binds below) at CI P %d ppm: %.1f ppm" % (Pci, Pci * hN / hP))
cross03 = 920 * hN / hP
print("  L03 N 2940 +- 20 (group, Nmet 2): (2940-%.0f)/20 = %.1f sigma above crossover" %
      (cross03, (2940 - cross03) / 20))
print("  Orgueil N 2948 +- 535 (5 analyses): (2948-%.0f)/535 = %.2f sigma above crossover" %
      (cross03, (2948 - cross03) / 535))
# P sigma: L03 P rests on Orgueil alone (Nmet 1); range of other CI P 500-1800 ppm
for Pci in (500, 1800):
    s = dict(sg.CHONDRITE); s.update({e: v[0] * 1e-6 for e, v in T3.items()}); s["P"] = Pci * 1e-6
    print("  L03 rows with P at %d ppm (L03's quoted older range): binder %s %.3f" % ((Pci,) + binder(s)))
# LBP25 (read this session via alphaXiv, 2502.10575 Table 4 p.70; text p.29/p.33)
for lab, N, P in (("LBP25 N 1965, P 989", 1965, 989),):
    s = dict(sg.CHONDRITE); s.update({e: v[0] * 1e-6 for e, v in T3.items()})
    s["N"] = N * 1e-6; s["P"] = P * 1e-6
    e, f = binder(s)
    print("  L03 rows + %s: binder %s %.3f (%.1f kg)" % (lab, e, f, 70 * f))
cross25 = 989 * hN / hP
print("  LBP25 N: (1965-%.0f)/970 = %.2f SD (Table 4); /447 = %.2f (text p.29); /206 = %.2f SE" %
      (cross25, (1965 - cross25) / 970, (1965 - cross25) / 447, (1965 - cross25) / 206))

print("\n=== 4. Regime labels (T_c alone) with L03 Table 8 as read")
for d in ("stellar photosphere", "Jupiter (3x solar)", "CI chondrite", "Earth cont. crust"):
    e, f, tc, lab = sg.regime_of(d)
    print("  %-20s %s %.4g  T_c %s (Table 8: %s) %s" % (d, e, f, tc, T8.get(e), lab))
chk("P T_c 1229 and N T_c 123 as Table 8 prints", T8["P"] == 1229 and T8["N"] == 123)
b = sg.condensed_budget()
print("  condensed_budget: refractory %.4e rock %.4e rock+ice %.4e gas %.6f" %
      (b["refractory"], b["rock"], b["rock+ice"], 1 - b["rock+ice"]))

print("\n=== 5. Craft (DECLARED) binder: Ta, tree 10 ppb vs L03 14.4 +- 0.1 ppb")
c = sg._norm(sg.CRAFT)
e0, f0 = sg.processing_factor(c, sg.CHONDRITE)
sL = dict(sg.CHONDRITE); sL.update({e: v[0] * 1e-6 for e, v in T3.items()})
e1, f1 = sg.processing_factor(c, sL)
print("  tree: %s %.5g ; all L03 rows: %s %.5g (x%.4f)" % (e0, f0, e1, f1, f1 / f0))
chk("craft binder stays Ta under L03 rows", e0 == e1 == "Ta")
print("\nFAILS:", FAIL)
sys.exit(1 if FAIL else 0)
