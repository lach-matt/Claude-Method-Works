#!/usr/bin/env python3
"""DOCKET 67 -- audit of icrp-23-reference-man (ICRP 23 Reference Man / Emsley).

Read-only against research/warp-drive: stockgate.py and stock.py are IMPORTED
(bytecode writing disabled so nothing is written into the tree).  Stdlib only.

What this checks, each as a numbered block whose verdict is printed:
  R1  stock.HUMAN's 14 fractions are the 59-element stockgate grams renormalised.
  R2  K = 140 g of 70 kg; the superseded 0.0040 is 280 g.
  R3  stockgate's grams against the Emsley column as RESTATED in Wikipedia's
      "Composition of the human body" (mass column cites Emsley 2011 p.83),
      fetched 2026-09-26 and saved as ../wiki_composition_human_body.txt.
  R4  the D25 figures reproduce (P 1911 at photosphere, Li 91.758 %; P 10.70 vs
      N 8.08 at CI chondrite).
  R5  flip thresholds: how far Li, P or N must move to change a binder.
  R6  alternative data READ here: (a) the restatement's own fraction column for
      Li (3.1e-8) and P (5-7e-3); (b) ICRP 110 whole-body composition computed
      from Kanematsu arXiv:1508.00226 Table I (mass-weighted regions, M/F mean);
      (c) the restatement's extra rows (Ru 7 mg, V 20 mg); (d) ICRP 89 73 kg.
"""
import os
import sys

sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import stockgate as sg  # noqa: E402
import stock  # noqa: E402

OK = []


def chk(label, cond, detail=""):
    OK.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + label + ("  -- " + detail if detail else ""))


def grams59():
    g = dict(sg.HUMAN_G_BULK)
    g.update(sg.HUMAN_G_ESSENTIAL_TRACE)
    g.update(sg.HUMAN_G_INCIDENTAL)
    return g


G = grams59()
TOT = sum(G.values())
print("R1  59-element total grams = %.4f ; n = %d" % (TOT, len(G)))
p59 = sg.payload("as-composed")
worst = max(abs(round(p59[e], 6) - stock.HUMAN[e]) for e in stock.HUMAN if e != "Li")
chk("R1 stock.HUMAN (13 non-Li) = 59-element fractions to 6 dp", worst < 1.5e-6,
    "max |diff| = %.2e" % worst)
chk("R1 stock.HUMAN Li = 0.007 g / total", abs(0.007 / TOT - stock.HUMAN["Li"]) < 1e-11,
    "%.4e vs %.4e" % (0.007 / TOT, stock.HUMAN["Li"]))
lsum = sum(stock.HUMAN.values())
chk("R1 listed fraction 0.9999231 (tree)", abs(lsum - 0.9999231) < 5e-7, "%.7f" % lsum)
chk("R1 N = 0.02568, P = 0.011129", abs(p59["N"] - 0.025683) < 1e-6 and abs(p59["P"] - 0.011129) < 1e-6,
    "N %.6f P %.6f" % (p59["N"], p59["P"]))

print()
kg = stock.HUMAN["K"] * 70000
chk("R2 K in 70 kg at stock.HUMAN = 140 g", round(kg) == 140, "%.2f g" % kg)
chk("R2 superseded K 0.0040 = 280 g", round(0.0040 * 70000) == 280)
chk("R2 note: 140 g of 70,088 g total vs 140/70000 differ by 0.13 %",
    abs(140 / TOT - 140 / 70000) / (140 / 70000) < 0.0015)

print()
# ---- R3: Emsley as restated on Wikipedia (Mass (kg) column), rows from N down.
# Transcribed from ../wiki_composition_human_body.txt lines 300-470.
WIKI_KG = {
    "N": 1.8, "Ca": 1.0, "P": 0.78, "K": 0.14, "S": 0.14, "Na": 0.10, "Cl": 0.095,
    "Mg": 0.019, "Fe": 0.0042, "F": 0.0026, "Zn": 0.0023, "Si": 0.0010,
    "Ga": 0.0007, "Rb": 0.00068, "Sr": 0.00032, "Br": 0.00026, "Pb": 0.00012,
    "Cu": 0.000072, "Al": 0.000060, "Cd": 0.000050, "Ce": 0.000040,
    "Ba": 0.000022, "Sn": 0.000020, "I": 0.000020, "Ti": 0.000020,
    "B": 0.000018, "Se": 0.000015, "Ni": 0.000015, "Cr": 0.000014,
    "Mn": 0.000012, "As": 0.000007, "Li": 0.000007, "Hg": 0.000006,
    "Cs": 0.000006, "Mo": 0.000005, "Ge": 5e-6, "Co": 0.000003,
    "Ru": 0.000007, "Sb": 0.000002, "Ag": 0.000002, "Nb": 0.0000015,
    "Zr": 0.000001, "La": 8e-7, "Te": 7e-7, "Y": 6e-7, "Bi": 5e-7, "Tl": 5e-7,
    "In": 4e-7, "Au": 2e-7, "Sc": 2e-7, "Ta": 2e-7, "V": 0.000020, "Th": 1e-7,
    "U": 1e-7, "Sm": 5.0e-8, "W": 2.0e-8, "Be": 3.6e-8, "Ra": 3e-14,
}
# O, C, H cells are run together in the text ("0.654526", "0.18139.5", "0.10763");
# the parse (frac | kg | atom%) is fixed by atom-% consistency, computed here.
cand = {"O": 45.0, "C": 13.0, "H": 7.0}
mol = {e: cand[e] * 1000 / sg.ATOMIC_MASS[e] for e in cand}
mol.update({e: WIKI_KG[e] * 1000 / sg.ATOMIC_MASS[e] for e in WIKI_KG if e in sg.ATOMIC_MASS})
nt = sum(mol.values())
print("R3  parse check O45/C13/H7: atom%% O %.1f (cell 26) C %.1f (cell 9.5) H %.1f (cell 63)"
      % (100 * mol["O"] / nt, 100 * mol["C"] / nt, 100 * mol["H"] / nt))
mis = []
for e, v in sorted(WIKI_KG.items()):
    if e in G:
        if abs(G[e] - v * 1000) > 1e-9 + 1e-6 * v * 1000:
            mis.append((e, G[e], v * 1000))
print("R3  tree-vs-restatement mismatches (tree g, page g):", mis)
print("R3  O/C/H: tree 43000/16000/7000 g ; page (parsed) 45000/13000/7000 g")
extra_page = sorted(e for e in WIKI_KG if e not in G)
extra_tree = sorted(e for e in G if e not in WIKI_KG and e not in ("O", "C", "H"))
print("R3  on page not in tree:", extra_page, " in tree not on page:", extra_tree)
chk("R3 of 56 shared rows below H, exactly two differ (Ga x1000, V x182)", [m[0] for m in mis] == ["Ga", "V"])
for lab, ov in (("O 45 kg, C 13 kg (page parse)", {"O": 45000.0, "C": 13000.0}),
                ("Ga 0.7 g (page) not 0.7 mg", {"Ga": 0.7})):
    g = dict(G); g.update(ov); p = sg.mass_fractions(g)
    ph_ = sg.DESTS["stellar photosphere"](); ci_ = sg.DESTS["CI chondrite"]()
    f = sg.factors(p, ph_)
    print("R3  %-30s photosphere %s %.5g ; CI %s %.5g ; factor(Ga) %.3g"
          % ((lab,) + sg.processing_factor(p, ph_) + sg.processing_factor(p, ci_) + (f["Ga"],)))

print()
# ---- R4: reproduce D25.
ph = sg.DESTS["stellar photosphere"]()
ci = sg.DESTS["CI chondrite"]()
e1, f1 = sg.processing_factor(p59, ph)
r = sg.ranked(p59, ph, 3)
chk("R4 photosphere binds on P at 1.9109e3", e1 == "P" and abs(f1 - 1910.9) < 0.6, "%s %.5g" % (e1, f1))
chk("R4 runner-up Li at 91.758 %", r[1][0] == "Li" and abs(100 * r[1][1] / f1 - 91.758) < 0.001,
    "%s %.3f %%" % (r[1][0], 100 * r[1][1] / f1))
e2, f2 = sg.processing_factor(p59, ci)
rc = sg.ranked(p59, ci, 2)
chk("R4 CI chondrite binds on P at 10.70, N second 8.08",
    e2 == "P" and abs(f2 - 10.701) < 0.01 and rc[1][0] == "N" and abs(rc[1][1] - 8.0763) < 0.01,
    "%s %.4g ; %s %.4g" % (e2, f2, rc[1][0], rc[1][1]))

print()
# ---- R5: flip thresholds (fractions renormalise, so solve by bisection).


def with_grams(**kw):
    g = dict(G)
    g.update(kw)
    return sg.mass_fractions(g)


def binder(g_over, dest):
    return sg.processing_factor(with_grams(**g_over), dest)


def bisect(elem, lo, hi, dest, want_binder):
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if binder({elem: mid}, dest)[0] == want_binder:
            hi = mid
        else:
            lo = mid
    return hi


li_flip = bisect("Li", 0.007, 0.02, ph, "Li")
print("R5  photosphere: Li flips the binder above %.4f mg (tree 7 mg; +%.2f %%)"
      % (li_flip * 1e3, 100 * (li_flip / 0.007 - 1)))
# P must fall for Li to bind: search P downward
lo, hi = 300.0, 780.0
for _ in range(80):
    mid = 0.5 * (lo + hi)
    if binder({"P": mid}, ph)[0] == "Li":
        lo = mid
    else:
        hi = mid
p_flip_ph = hi
print("R5  photosphere: P below %.1f g (tree 780 g; -%.2f %%) hands the binder to Li"
      % (p_flip_ph, 100 * (1 - p_flip_ph / 780)))
lo, hi = 300.0, 780.0
for _ in range(80):
    mid = 0.5 * (lo + hi)
    if binder({"P": mid}, ci)[0] == "N":
        lo = mid
    else:
        hi = mid
print("R5  CI chondrite: P below %.1f g (-%.2f %%) hands the binder to N" % (hi, 100 * (1 - hi / 780)))
chk("R5 Li threshold ~7.63 mg", abs(li_flip * 1e3 - 7.629) < 0.01, "%.4f mg" % (li_flip * 1e3))

print()
# ---- R6: alternative data READ in this audit.
print("R6a restatement fraction column: Li 3.1e-8 x 70 kg = %.2f mg ; P 5-7e-3 x 70 kg = %.0f-%.0f g"
      % (3.1e-8 * 70e6, 5e-3 * 70e3, 7e-3 * 70e3))
for lab, ov in (("Li 2.17 mg", {"Li": 3.1e-8 * 70e3}),
                ("P 350 g", {"P": 350.0}), ("P 490 g", {"P": 490.0}),
                ("P 490 g + Li 2.17 mg", {"P": 490.0, "Li": 3.1e-8 * 70e3})):
    a = binder(ov, ph)
    b = binder(ov, ci)
    rr = sg.ranked(with_grams(**ov), ph, 2)
    print("     %-22s photosphere %s %.4g (2nd %s %.4g) | CI %s %.4g"
          % (lab, a[0], a[1], rr[1][0], rr[1][1], b[0], b[1]))

# ICRP 110 via Kanematsu Table I (m %, w_H, w_C, w_N, w_O, w_P, w_Ca), READ.
K110 = [  # region: m%, H, C, N, O, P, Ca
    ("lung", 1.4, 10.3, 10.7, 3.2, 74.6, 0.2, 0.0),
    ("adipose/marrow", 34.3, 11.40, 58.92, 0.74, 28.64, 0.00, 0.00),
    ("muscle/organ", 46.5, 10.25, 14.58, 3.20, 70.87, 0.21, 0.02),
    ("miscellaneous", 6.3, 9.94, 20.90, 3.84, 63.73, 0.45, 0.27),
    ("spongiosa", 5.7, 9.30, 39.15, 2.22, 41.71, 2.36, 4.60),
    ("mineral bone", 5.7, 3.6, 15.9, 4.2, 44.8, 9.4, 21.3),
    ("tooth", 0.1, 2.2, 9.5, 2.9, 42.1, 13.7, 28.9),
]
msum = sum(r_[1] for r_ in K110)
wb = {}
for i, el in enumerate(("H", "C", "N", "O", "P", "Ca")):
    wb[el] = sum(r_[1] * r_[2 + i] for r_ in K110) / msum / 100.0
print("R6b ICRP 110 whole body (Kanematsu Table I, m sums to %.1f %%):" % msum,
      {k: round(v, 5) for k, v in wb.items()})
print("     vs tree (ICRP 23/Emsley):",
      {k: round(p59[k], 5) for k in ("H", "C", "N", "O", "P", "Ca")})
g110 = {el: wb[el] * TOT for el in wb}
a = binder(g110, ph)
b = binder(g110, ci)
rr = sg.ranked(with_grams(**g110), ph, 3)
rc = sg.ranked(with_grams(**g110), ci, 3)
print("     ICRP-110 bulk: photosphere %s %.4g ; ranking %s" % (a[0], a[1], [(x, round(y, 1)) for x, y in rr]))
print("     ICRP-110 bulk: CI chondrite %s %.4g ; ranking %s" % (b[0], b[1], [(x, round(y, 3)) for x, y in rc]))
chk("R6b ICRP 110 P fraction is below the photosphere Li-flip threshold",
    wb["P"] * TOT < p_flip_ph, "P %.4f vs threshold %.4f" % (wb["P"], p_flip_ph / TOT))

for lab, ov in (("+Ru 7 mg (page row)", {"Ru": 0.007}), ("V 20 mg (page) not 0.11 mg", {"V": 0.020})):
    g = dict(G)
    g.update(ov)
    p = sg.mass_fractions(g)
    if "Ru" in ov:
        # A09 Ru is not in the tree's table; A09 Table 1 (Asplund 2009) gives
        # photospheric 1.75 -- NAMED here, not READ in this audit: flagged.
        n = {e: 10 ** ((v[0] if v[0] is not None else v[1]) - 12) for e, v in sg.A09.items()
             if (v[0] if v[0] is not None else v[1]) is not None}
        n["Ru"] = 10 ** (1.75 - 12)
        am = dict(sg.ATOMIC_MASS, Ru=101.07)
        s = sg._norm({e: n[e] * am[e] for e in n})
    else:
        s = ph
    f = sg.factors(p, s)
    el = list(ov)[0]
    print("R6c %-28s factor(%s) = %.3g against binder %.4g -> binder %s"
          % (lab, el, f[el], max(f.values()), max(f, key=f.get)))

print("R6d ICRP 89 reference male 73 kg: factor per kg unchanged; feedstock x %.4f" % (73 / 70))

print()
print("%d of %d checks pass" % (sum(OK), len(OK)))
sys.exit(0 if all(OK) else 1)
