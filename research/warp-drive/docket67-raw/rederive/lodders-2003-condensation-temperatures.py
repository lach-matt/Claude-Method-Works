#!/usr/bin/env python3
"""DOCKET 67 -- audit of Lodders (2003) 50% condensation temperatures as stockgate.py uses them.

Read-only against the tree: imports research/warp-drive/stockgate.py with bytecode writing
disabled, never modifies it.  Every external number below is READ from an arXiv source:
  L09   = Lodders, Palme & Gail 2009, arXiv:0901.1149, Table 1 ("taken from [03L]" = Lodders 2003)
  LF23  = Lodders & Fegley 2023, arXiv:2301.03674 (restates Lodders 2003 halogen values; updates them)
  WLI19 = Wang, Lineweaver & Ireland 2019, arXiv:1810.12741 (quotes Lodders 2003 Mg, Si, C, O)
  L24   = Lodders, Fegley, Mezger & Ebel 2024, arXiv:2411.01362, Table 1 (updated T50, logP=-2..-8)
Checks:
  (1) tree TCOND vs Lodders-2003 restatements (transcription)
  (2) Finding F regime labels under the 2003 table, the 2024 table, and at every tabulated pressure
  (3) Finding G condensed budget under the 2024 table, under filled-in missing refractories, and
      under alternative cuts (Lodders' own highly-volatile boundary 660 K)
  (4) the stated 99.06 % "gas" figure recomputed
"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import stockgate as sg  # noqa: E402

T = sg.TCOND

# ---- (1) Lodders 2003 restatements, READ ----------------------------------------------
# L09 Table 1, rows whose name/number pairing is unambiguous in the extraction
L09 = {"Re": 1821, "Os": 1812, "W": 1789, "Sc": 1659, "Y": 1659, "Th": 1659, "Al": 1653,
       "U": 1610, "Ir": 1603, "Nd": 1602, "Mo": 1590, "Sm": 1590, "Ti": 1582, "La": 1578,
       "Ta": 1573, "Nb": 1559, "Fe": 1334, "Co": 1352, "Ni": 1353, "Li": 1142, "As": 1065,
       "Au": 1060, "Cu": 1037, "Ag": 996, "Sb": 979, "Ga": 968, "Na": 958, "B": 908, "Ge": 883,
       "Rb": 800, "Cs": 799, "Bi": 746, "F": 734, "Pb": 727, "Zn": 726, "Te": 709, "Sn": 704,
       "Se": 697, "S": 664, "Cd": 652, "Br": 546, "In": 536, "I": 535, "Tl": 532, "Hg": 252,
       "O": 180, "N": 123, "C": 40, "H": 182}
# rows where the L09 extraction disagrees with the tree (column offset / possible update):
L09_DISAGREE = {"Zr": 1764, "Mg": 1354, "Si": 1354, "Ca": "1659 (row offset in extraction)",
                "V": "1452 (row offset)", "Be": "1464 (row offset)", "Sr": "1478 (row offset)",
                "Ce": "1487 (row offset)"}
LF23_2003 = {"Cl": 948, "Br": 546, "I": 535, "Ca": 1517}   # LF23 quoting Lodders (2003)
WLI19 = {"Mg": 1330, "Si": 1310, "C": 40, "O": 180}

print("(1) TRANSCRIPTION: tree TCOND vs Lodders-2003 restatements")
agree, dis = 0, []
for src, tab in (("L09", L09), ("LF23", LF23_2003), ("WLI19", WLI19)):
    for e, v in tab.items():
        if T.get(e) == v:
            agree += 1
        else:
            dis.append((src, e, T.get(e), v))
print("   agreements:", agree)
for d in dis:
    print("   DISCREPANCY", d)
for e, v in L09_DISAGREE.items():
    print("   L09-extraction vs tree", e, T.get(e), v)
print("   tree He =", T["He"], "; source: '<3' (upper bound)   tree carries sentinel 'Ni_':", T.get("Ni_"))

# ---- 2024 update, READ (L24 Table 1) ----------------------------------------------------
L24 = {  # log P = -4
 "H": 7.4, "He": 3, "Li": 1152, "Be": 1451, "B": 945, "C": 40, "N": 124, "O": 182, "F": 717,
 "Ne": 9.1, "Na": 978, "Mg": 1330, "Al": 1655, "Si": 1313, "P": 1273, "S": 661, "Cl": 418,
 "Ar": 46, "K": 975, "Ca": 1517, "Sc": 1629, "Ti": 1581, "V": 1429, "Cr": 1299, "Mn": 1165,
 "Fe": 1334, "Co": 1352, "Ni": 1353, "Cu": 1041, "Zn": 697, "Ga": 965, "Ge": 887, "As": 1069,
 "Se": 693, "Br": 423, "Kr": 56, "Rb": 1019, "Sr": 1515, "Y": 1607, "Zr": 1742, "Nb": 1559,
 "Mo": 1592, "Ru": 1551, "Rh": 1390, "Pd": 1324, "Ag": 999, "Cd": 540, "In": 430, "Sn": 706,
 "Sb": 983, "Te": 712, "I": 316, "Xe": 72, "Cs": 857, "Ba": 1490, "La": 1583, "Ce": 1538,
 "Pr": 1583, "Nd": 1613, "Sm": 1590, "Eu": 1366, "Gd": 1619, "Tb": 1619, "Dy": 1619,
 "Ho": 1619, "Er": 1619, "Tm": 1619, "Yb": 1487, "Lu": 1619, "Hf": 1683, "Ta": 1577,
 "W": 1793, "Re": 1821, "Os": 1813, "Ir": 1603, "Pt": 1408, "Au": 1065, "Hg": 248, "Tl": 404,
 "Pb": 730}
L24P = {  # binders at log P = -2, -4, -6, -8
 "N": (139, 124, 111, 101), "P": (1421, 1273, 1142, 1029), "Li": (1319, 1152, 1003, 891)}

cut = sg.VOLATILE_CUT
print("\n(2) FINDING F regime labels (cut =", cut, "K)")
rows = sg.volatility_regime()
ok = True
for d, e, f, tc, reg in rows:
    labs = []
    for name, tab in (("2003", T), ("2024", L24)):
        labs.append((name, tab[e], "VOL" if tab[e] < cut else "ABU"))
    for i, lp in enumerate((-2, -4, -6, -8)):
        v = L24P[e][i]
        labs.append(("2024 logP=%d" % lp, v, "VOL" if v < cut else "ABU"))
    same = len({l[2] for l in labs}) == 1
    ok &= same
    print("  ", d, "binds on", e, "->", reg, "| unchanged across all tables/pressures:", same)
    print("      ", labs)
# margin: the cut window that preserves all four labels, over every table and pressure
lo = max([T["N"], L24["N"]] + list(L24P["N"]))
hi = min([T["P"], L24["P"]] + list(L24P["P"]))
print("   cut window preserving every label, all tables, logP -2..-8: (%s K, %s K]" % (lo, hi))
print("   REGIME LABELS ROBUST:", ok)

# the binder itself is chosen from abundances only (processing_factor); TCOND never enters it
print("   binder selection uses TCOND? ", "TCOND" in sg.processing_factor.__code__.co_names)

# ---- (3) Finding G --------------------------------------------------------------------
def budget(tc, vcut):
    X = sg.solar_hybrid()
    A = sg.ATOMIC_MASS
    refr = [e for e in X if tc.get(e, -1.0) >= vcut]
    rb = sum(X[e] for e in refr)
    bo = sum((X[e] / A[e]) * sg.OXIDE_O.get(e, 0.0) * A["O"] for e in refr)
    rock = rb + bo
    ice = max(0.0, X["O"] - bo) * (2 * A["H"] + A["O"]) / A["O"]
    return dict(refractory=rb, boundO=bo, rock=rock, ice=ice, rockice=rock + ice,
                gas=1.0 - rock - ice, refr=set(refr))

base = budget(T, cut)
print("\n(3) FINDING G condensed budget")
print("   tree table, cut 500: refractory %.4e rock %.4e rock+ice %.4e gas %.4f%%"
      % (base["refractory"], base["rock"], base["rockice"], 100 * base["gas"]))
X = sg.solar_hybrid()
missing = sorted(e for e in X if e not in T and e not in ("H", "He"))
print("   elements in the abundance column with NO T_c in the tree (counted as non-refractory):",
      missing)
print("   their summed mass fraction: %.3e" % sum(X[e] for e in missing))
filled = dict(T)
for e in missing:
    if e in L24:
        filled[e] = L24[e]
still = [e for e in missing if e not in L24]
print("   not fillable from L24 read here:", still)
for name, tab, vc in (("tree + missing filled (L24)", filled, cut),
                      ("L24 2024 table (Bi,Th,U kept from tree)", {**T, **L24}, cut),
                      ("tree table, cut 660 K (Lodders' HV boundary)", T, 660.0),
                      ("tree table, cut 400 K", T, 400.0),
                      ("L24 table, cut 660 K", {**T, **L24}, 660.0)):
    b = budget(tab, vc)
    moved = sorted(base["refr"] ^ b["refr"])
    print("   %-45s refr %.4e (%+.3f%%) rock %.4e rock+ice %.4e (%+.4f%%) gas %.4f%%  moved: %s"
          % (name, b["refractory"], 100 * (b["refractory"] / base["refractory"] - 1),
             b["rock"], b["rockice"], 100 * (b["rockice"] / base["rockice"] - 1),
             100 * b["gas"], moved))

# ---- (4) the stated 99.06 % ------------------------------------------------------------
cb = sg.condensed_budget()
print("\n(4) stockgate.condensed_budget():", {k: "%.4e" % v for k, v in cb.items()})
print("   1 - rock - ice = %.5f  (stated in the docstring: 99.06 %%)" % (1 - cb["rock+ice"]))
print("   H+He alone      = %.5f" % cb["H+He"])
