#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for lodders-2003-apj-591-1220.

Reads research/warp-drive/stockgate.py and formation.py by IMPORT ONLY
(sys.dont_write_bytecode, nothing under research/ is written) and checks the
tree's uses of Lodders (2003), ApJ 591, 1220 against the values READ at source
(IOP PDF 10.1086/375492, via alphaXiv answer_pdf_queries, 2026-09-26):

  L03 sec. 3 (p.1236): "The condensation temperatures and the 50% condensation
      temperatures are calculated for all elements at a total pressure of
      10^-4 bar ... characteristic for the total pressure near 1 AU in the solar
      nebula."
  L03 Table 8 (pp.1239-1240): 50% T_C, solar-system composition, 10^-4 bar.
  L03 Table 3 (p.1225): CI chondrite group weighted means, ppm.
Later values, READ:
  Lodders, Fegley, Mezger & Ebel 2024 (arXiv:2411.01362) Table 1: T50 at
      log P = -2, -4, -6, -8 (rows H..Kr read).
  Lodders, Bergemann & Palme 2025 (arXiv:2502.10575) Table 4: CI ppm (H..Sn read).

Exit 0 when every check that is a check passes; the discrepancies are
RECORDED, not repaired, and are printed as DISCREPANCY lines.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import stockgate as sg  # noqa: E402

FAIL = []


def chk(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAIL.append(label)


# ---------------------------------------------------------------- L03 Table 8
# 50% T_C (K) at 1e-4 bar, solar-system composition.  None = the table gives
# no 50% value (H: TC 182 only; He: "<3", TC only).
L03_T50 = {
    "H": None, "He": None, "Li": 1142, "Be": 1452, "B": 908, "C": 40, "N": 123,
    "O": 180, "F": 734, "Ne": 9.1, "Na": 958, "Mg": 1336, "Al": 1653,
    "Si": 1310, "P": 1229, "S": 664, "Cl": 948, "Ar": 47, "K": 1006,
    "Ca": 1517, "Sc": 1659, "Ti": 1582, "V": 1429, "Cr": 1296, "Mn": 1158,
    "Fe": 1334, "Co": 1352, "Ni": 1353, "Cu": 1037, "Zn": 726, "Ga": 968,
    "Ge": 883, "As": 1065, "Se": 697, "Br": 546, "Rb": 800, "Sr": 1464,
    "Y": 1659, "Zr": 1741, "Nb": 1559, "Mo": 1590, "Ag": 996, "Cd": 652,
    "In": 536, "Sn": 704, "Sb": 979, "Te": 709, "I": 535, "Cs": 799,
    "Ba": 1455, "La": 1578, "Ce": 1478, "Nd": 1602, "Sm": 1590, "Ta": 1573,
    "W": 1789, "Au": 1060, "Hg": 252, "Tl": 532, "Pb": 727, "Bi": 746,
    "Th": 1659, "U": 1610,
}
L03_TC_APPEARANCE = {"H": 182, "He": 3}   # He printed as "<3"

# ---------------------------------------------------------------- L03 Table 3
# CI chondrite group weighted mean, ppm (rows H..Ag read at source).
L03_CI_PPM = {
    "H": 21015, "C": 35180, "N": 2940, "O": 458200, "F": 60.6, "Na": 5010,
    "Mg": 95870, "Al": 8500, "Si": 106500, "P": 920, "S": 54100, "Cl": 704,
    "K": 530, "Ca": 9070, "Sc": 5.83, "Ti": 440, "V": 55.7, "Cr": 2590,
    "Mn": 1910, "Fe": 182800, "Co": 502, "Ni": 10640, "Cu": 127, "Zn": 310,
    "Ga": 9.51, "Ge": 33.2, "As": 1.73, "Se": 19.7, "Br": 3.43, "Rb": 2.13,
    "Sr": 7.74, "Y": 1.53, "Zr": 3.96, "Nb": 0.265, "Mo": 1.02, "Ag": 0.201,
    "Li": 1.46, "B": 0.713, "Be": 0.0252,
}
L03_CI_P_SIGMA = 100.0

# ------------------------------------------------ LBP 2025 Table 4 (later datum)
LBP25_CI_PPM = {
    "H": 18598, "Li": 1.48, "Be": 0.0225, "B": 0.744, "C": 37813, "N": 1965,
    "O": 465700, "F": 92, "Na": 4960, "Mg": 95600, "Al": 8470, "Si": 106600,
    "P": 989, "S": 51800, "Cl": 717, "K": 544, "Ca": 9148, "Sc": 5.76,
    "Ti": 442, "V": 53.1, "Cr": 2616, "Mn": 1936, "Fe": 185000, "Co": 514,
    "Ni": 11180, "Cu": 133, "Zn": 310, "Ga": 9.54, "Ge": 33.5, "As": 1.75,
    "Se": 21.5, "Br": 3.77, "Rb": 2.26, "Sr": 8.04, "Y": 1.52, "Zr": 3.65,
    "Nb": 0.271, "Mo": 0.947, "Ag": 0.206, "Cd": 0.682, "In": 0.0781,
    "Sn": 1.67,
}
LBP25_CI_P_SIGMA = 89.0

# -------------------------------- LFME 2024 Table 1: T50 at log P = -2,-4,-6,-8
LFME24_T50 = {
    "H": (10.6, 7.4, 5.7, 4.6), "Li": (1319, 1152, 1003, 891),
    "Be": (1566, 1451, 1349, 1253), "B": (1027, 945, 875, 814),
    "C": (48, 40, 34, 30), "N": (139, 124, 111, 101), "O": (210, 182, 160, 143),
    "F": (775, 717, 699, 697), "Ne": (10.8, 9.1, 7.7, 6.8),
    "Na": (1077, 978, 895, 826), "Mg": (1476, 1330, 1214, 1115),
    "Al": (1795, 1655, 1533, 1427), "Si": (1451, 1313, 1201, 1111),
    "P": (1421, 1273, 1142, 1029), "S": (661, 661, 661, 660),
    "Cl": (460, 418, 383, 354), "Ar": (54, 46, 41, 36),
    "K": (1063, 975, 899, 834), "Ca": (1683, 1517, 1382, 1269),
    "Sc": (1704, 1629, 1505, 1398), "Ti": (1742, 1581, 1449, 1337),
    "V": (1711, 1429, 1371, 1208), "Cr": (1490, 1299, 1152, 1036),
    "Mn": (1290, 1165, 1049, 966), "Fe": (1531, 1334, 1182, 1063),
    "Co": (1552, 1352, 1200, 1078), "Ni": (1552, 1353, 1200, 1078),
    "Cu": (1200, 1041, 916, 817), "Zn": (720, 697, 668, 611),
    "Ga": (1206, 965, 730, 665), "Ge": (1076, 887, 755, 658),
    "As": (1230, 1069, 943, 839), "Se": (693, 693, 693, 693),
    "Br": (466, 423, 387, 357),
}


def main():
    print("=== 1. the pressure hypothesis, as the tree carries it")
    import formation as fm
    chk("formation.LODDERS_PRESSURE_BAR == 1e-4 (L03 sec.3: 'total pressure of 10^-4 bar')",
        fm.LODDERS_PRESSURE_BAR == 1.0e-4)
    chk("stockgate.SOURCES['L03'] names 1e-4 bar", "1e-4 bar" in sg.SOURCES["L03"])

    print("\n=== 2. stockgate.TCOND against L03 Table 8 (50% T_C, solar-system comp.)")
    match, disc = 0, []
    for e, v in sg.TCOND.items():
        if e.endswith("_"):
            continue                      # sentinel keys (Ni_), not data
        ref = L03_T50.get(e, "ABSENT")
        if ref is None:
            disc.append((e, v, "no 50%% value in Table 8; TC column = %s"
                         % L03_TC_APPEARANCE[e]))
        elif ref == "ABSENT":
            disc.append((e, v, "not read"))
        elif abs(v - ref) <= 0.5 or (e == "Ne" and round(ref) == v):
            match += 1
        else:
            disc.append((e, v, "L03 50%% T_C = %s" % ref))
    n = sum(1 for e in sg.TCOND if not e.endswith("_"))
    print("  %d of %d TCOND entries equal L03 Table 8's 50%% T_C (Ne 9.1 -> 9 rounded)"
          % (match, n))
    for d in disc:
        print("  DISCREPANCY  %-3s tree %s : %s" % d)
    chk("every TCOND entry except H, He equals L03 Table 8", match == n - 2 and
        {d[0] for d in disc} == {"H", "He"})

    print("\n=== 3. stockgate.CHONDRITE against L03 Table 3 (CI weighted mean)")
    rows = []
    for e, ppm in sorted(L03_CI_PPM.items(), key=lambda kv: -kv[1]):
        t = sg.CHONDRITE.get(e)
        if t is None:
            continue
        r = t * 1e6 / ppm
        rows.append((e, t * 1e6, ppm, r))
    exact = [r for r in rows if abs(r[3] - 1) < 0.005]
    for e, t, ref, r in rows:
        flag = "" if abs(r - 1) < 0.02 else "   <-- DISCREPANCY"
        print("  %-3s tree %12.4g ppm   L03 %12.4g ppm   tree/L03 %.4f%s"
              % (e, t, ref, r, flag))
    print("  %d of %d compared entries within 0.5%% of L03 Table 3" % (len(exact), len(rows)))
    s = sum(v for k, v in sg.CHONDRITE.items() if not k.endswith("_"))
    print("  sum of stockgate.CHONDRITE mass fractions = %.5f (not renormalised by DESTS)" % s)

    print("\n=== 4. the binder the tree prices on the CI chondrite, re-derived")
    pk = "as-composed 59"
    p = sg.PAYLOADS[pk]()
    base_e, base_f = sg.processing_factor(p, sg.CHONDRITE)
    print("  tree:  binder %s, factor %.5f, feedstock(70 kg) = %.2f kg"
          % (base_e, base_f, 70 * base_f))
    chk("tree binder is P at 10.7012 (stockgate prints 1.07012e+01)",
        base_e == "P" and abs(base_f - 10.7012) < 5e-4)
    chk("70 kg x factor = 749.08 kg (formation [W1] figure)",
        abs(70 * base_f - 749.08) < 0.01)

    def variant(label, repl):
        d = dict(sg.CHONDRITE)
        for e, ppm in repl.items():
            if e in d:
                d[e] = ppm * 1e-6
        e, f = sg.processing_factor(p, d)
        top = sg.ranked(p, d, 3)
        print("  %-44s binder %-2s factor %8.4f  feedstock %7.2f kg  (x%.4f)  next: %s"
              % (label, e, f, 70 * f, f / base_f,
                 ", ".join("%s %.3f" % kv for kv in top[1:])))
        return e, f

    e1, f1 = variant("P only -> L03 920 ppm", {"P": 920})
    e1a, f1a = variant("P only -> L03 920+100 (1 sigma high)", {"P": 1020})
    e1b, f1b = variant("P only -> L03 920-100 (1 sigma low)", {"P": 820})
    e2, f2 = variant("all read L03 Table 3 rows substituted", L03_CI_PPM)
    e3, f3 = variant("P only -> LBP 2025 989 ppm", {"P": 989})
    e4, f4 = variant("all read LBP 2025 Table 4 rows substituted", LBP25_CI_PPM)
    chk("binder stays P under every L03-internal variant (920, 920+-100, all L03 rows)",
        {e1, e1a, e1b, e2} == {"P"})
    print("  MEASURED (a moved datum, not a check): with LBP 2025 Table 4 the binder is %s;"
          " P alone at 989 keeps %s" % (e4, e3))
    fN = sg.factors(p, sg.CHONDRITE)["N"]
    nN = sg.CHONDRITE["N"] * 1e6
    for lab, fP in (("tree P 1040", base_f), ("L03 P 920", f1), ("LBP25 P 989", f3)):
        print("  N overtakes P when CI N < %.0f ppm  (%s)" % (fN * nN / fP, lab))
    print("  CI N read: L03 2940+-20 ppm (2 meteorites); LBP25 1965+-970 ppm (quality D, 49% SD)")
    print("  under LBP25 N the CI chondrite's regime label is %s (N T_c 123 K < cut %.0f K)"
          % ("VOLATILITY-LIMITED" if e4 == "N" else "ABUNDANCE-LIMITED", sg.VOLATILE_CUT))
    tree_P = sg.CHONDRITE["P"] * 1e6
    z03 = (tree_P - 920) / L03_CI_P_SIGMA
    z25 = (tree_P - 989) / LBP25_CI_P_SIGMA
    print("  tree P = %.0f ppm: %+.2f sigma from L03 (920+-100); %+.2f sigma from LBP25 (989+-89)"
          % (tree_P, z03, z25))

    # the conclusion that rests on it in formation.py: Proxima b min mass / need
    need_tree = sg.feedstock_kg(70.0, pk, "CI chondrite")
    lo, hi = 70 * min(f1, f2, f1a, f1b, f3, f4), 70 * max(f1, f2, f1a, f1b, f3, f4)
    print("  feedstock range over the variants: %.1f .. %.1f kg (tree %.2f)" % (lo, hi, need_tree))
    M_EARTH = 5.9722e24
    mpb = 1.07 * M_EARTH     # Proxima b m sin i ~1.07 M_E (order of magnitude only)
    print("  log10(Proxima b min mass / need): tree %.2f, worst variant %.2f"
          % (math.log10(mpb / need_tree), math.log10(mpb / hi)))
    print("  largest move of the comparison: %.3f dex" % max(abs(math.log10(need_tree / hi)),
                                                           abs(math.log10(need_tree / lo))))
    chk("Proxima b min mass exceeds the need by > 20 dex under every variant",
        math.log10(mpb / hi) > 20)

    print("\n=== 5. the refusal D25 rests on: T_c moves with total pressure (LFME 2024 Table 1)")
    for e in ("P", "Fe", "Mg", "Si", "N", "O", "C", "S", "Se"):
        t = LFME24_T50[e]
        print("  %-2s T50 at 1e-2/1e-4/1e-6/1e-8 bar: %s   span %.0f K" % (e, t, t[0] - t[-1]))
    moving = [e for e, t in LFME24_T50.items() if (t[0] - t[-1]) > 1.0]
    print("  %d of %d elements read move by >1 K over 1e-2..1e-8 bar; constant: %s"
          % (len(moving), len(LFME24_T50),
             [e for e in LFME24_T50 if e not in moving]))
    chk("S and Se are pressure-independent (L03 sec.3.3.7 troilite; LFME24 'except for S and Se')",
        set(LFME24_T50) - set(moving) == {"S", "Se"})

    print("\n=== 6. L03 (2003) vs LFME 2024 at the SAME 1e-4 bar: the datum that moved")
    cut = sg.VOLATILE_CUT
    crossers, deltas = [], []
    for e, t in LFME24_T50.items():
        old = sg.TCOND.get(e)
        if old is None:
            continue
        new = t[1]
        deltas.append((abs(new - old), e, old, new))
        if (old >= cut) != (new >= cut):
            crossers.append((e, old, new))
    for d, e, old, new in sorted(deltas, reverse=True)[:8]:
        print("  %-2s L03/tree %6s K -> LFME24 %6s K  (|d| %.0f K)" % (e, old, new, d))
    print("  crossing stockgate.VOLATILE_CUT = %.0f K: %s" % (cut, crossers))
    # regime of the four destinations under LFME24 T50
    tc2 = dict(sg.TCOND)
    for e, t in LFME24_T50.items():
        if e in tc2:
            tc2[e] = t[1]
    reg_old = sg.volatility_regime()
    saved = sg.TCOND
    sg.TCOND = tc2
    try:
        reg_new = sg.volatility_regime()
        bud_new = sg.condensed_budget()
    finally:
        sg.TCOND = saved
    bud_old = sg.condensed_budget()
    for a, b in zip(reg_old, reg_new):
        print("  %-24s %s %5s K %-19s -> %5s K %s" % (a[0], a[1], a[3], a[4], b[3], b[4]))
    chk("no destination changes regime under LFME24 T50",
        all(a[4] == b[4] for a, b in zip(reg_old, reg_new)))
    for k in ("refractory", "rock", "rock+ice"):
        print("  condensed_budget %-10s L03 %.5e  LFME24 %.5e  (x%.4f)"
              % (k, bud_old[k], bud_new[k], bud_new[k] / bud_old[k]))

    print("\n=== 7. sympy: T50 is linear in log P in LFME24's own fit form 1e4/T = A + B logP")
    import sympy as S
    A, B, x = S.symbols("A B x")
    fitO = 1e4 / (S.Float("40.12654") - S.Float("3.72440") * x)
    print("  LFME24 appendix O fit at log P=-4: %.1f K (Table 1: 182)" % float(fitO.subs(x, -4)))
    chk("LFME24 O fit reproduces its own Table 1 at 1e-4 bar within 1 K",
        abs(float(fitO.subs(x, -4)) - 182) < 1.0)
    tP = LFME24_T50["P"]
    sol = S.solve([A + B * (-2) - 1e4 / tP[0], A + B * (-8) - 1e4 / tP[3]], [A, B])
    t4 = 1e4 / (sol[A] + sol[B] * (-4))
    print("  P: two-point fit (1e-2, 1e-8) predicts T50(1e-4) = %.0f K (Table 1: 1273)" % float(t4))
    print("  so a factor-100 error in the assumed disc pressure moves P's T50 by ~%.0f K"
          % ((tP[0] - tP[2]) / 2))

    print("\nRESULT: %s" % ("ALL CHECKS PASS" if not FAIL else "FAILED: %s" % FAIL))
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
