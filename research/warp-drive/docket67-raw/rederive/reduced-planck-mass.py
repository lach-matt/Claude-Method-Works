#!/usr/bin/env python3
"""DOCKET 67 / pass S #19 -- reduced-planck-mass.

Re-derives, independently of the tree's arithmetic:
  (1) the definition Mbar4 = sqrt(hbar c / (8 pi G)) and its inverse G = 1/(8 pi Mbar4^2)
      in natural units (sympy, exact);
  (2) kappa = sqrt(32 pi G) = 2/Mbar4 -- the graviton coupling normalisation that a
      "2/Mbar" metric expansion (Kabat & Nomura eq. 68 as the tree quotes it) implies
      is the REDUCED mass (sympy, exact algebra; the EH normalisation kappa^2 = 32 pi G
      is NAMED, not re-derived here);
  (3) the 5D -> 4D relation Mbar4^2 = (2 pi r) Mbar5^3 is dimensionally consistent;
  (4) the number, from CODATA 2022 (G, hbar, c, e) transcribed in scipy 1.17.1's
      _codata.py, vs the tree's higgs.reduced_planck_gev() and its selftest pin;
  (5) the move of the datum G across CODATA 2006..2022 and what it does to
      branelink's SME null (|c| ~ 1/Mbar4^2, "42 orders short");
  (6) the convention hazard: if Kabat & Nomura's Mbar4 were the NON-reduced Planck
      mass, how far |c| moves (8 pi), and whether the conclusion moves.
Exit 0 iff every check passes.
"""
import math
import os
import re
import sys

import sympy as sp

FAIL = []


def chk(name, ok, detail=""):
    print("  %-4s %s %s" % ("ok" if ok else "FAIL", name, detail))
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ (1)-(3) symbolic
hbar, c, G, M, kap, r, M5 = sp.symbols("hbar c G Mbar kappa r Mbar5", positive=True)
Mbar_def = sp.sqrt(hbar * c / (8 * sp.pi * G))
G_back = sp.solve(sp.Eq(M, Mbar_def), G)[0]
chk("(1) G = hbar c/(8 pi Mbar^2) inverts the definition",
    sp.simplify(G_back - hbar * c / (8 * sp.pi * M ** 2)) == 0, "-> %s" % G_back)
chk("(1) natural units hbar=c=1: G = 1/(8 pi Mbar^2)",
    sp.simplify(G_back.subs({hbar: 1, c: 1}) - 1 / (8 * sp.pi * M ** 2)) == 0)
kappa = sp.sqrt(32 * sp.pi * G_back.subs({hbar: 1, c: 1}))
chk("(2) kappa = sqrt(32 pi G) = 2/Mbar (reduced)", sp.simplify(kappa - 2 / M) == 0,
    "-> %s" % sp.simplify(kappa))
Mpl = sp.sqrt(1 / G)  # non-reduced, natural units, G free
chk("(2) with the NON-reduced M_Pl, kappa = sqrt(32 pi)/M_Pl != 2/M_Pl",
    sp.simplify(sp.sqrt(32 * sp.pi * G) * Mpl - 2) != 0)
# (3) mass dimensions in natural units: [Mbar4]=1, [Mbar5]=1, [r]=-1
dim = {"Mbar4": 1, "Mbar5": 1, "r": -1}
chk("(3) [Mbar4^2] = [r Mbar5^3]", 2 * dim["Mbar4"] == dim["r"] + 3 * dim["Mbar5"])

# ------------------------------------------------------------------ (4) numbers
HERE = os.path.dirname(os.path.abspath(__file__))
CODATA = os.path.join(HERE, "..", "src", "codata", "x", "scipy", "constants", "_codata.py")
txt = open(CODATA).read()


def block(year):
    m = re.search(r'txt%d = """\\\n(.*?)"""' % year, txt, re.S)
    return m.group(1)


def val(year, name):
    for line in block(year).splitlines():
        if line.startswith(name + "  "):
            rest = line[len(name):].strip()
            num = re.split(r"\s{2,}", rest)[0].replace(" ", "").replace("...", "")
            return float(num)
    raise KeyError((year, name))


def unc(year, name):
    for line in block(year).splitlines():
        if line.startswith(name + "  "):
            parts = re.split(r"\s{2,}", line[len(name):].strip())
            u = parts[1].replace(" ", "")
            return 0.0 if "exact" in u else float(u)
    raise KeyError((year, name))


G22 = val(2022, "Newtonian constant of gravitation")
uG22 = unc(2022, "Newtonian constant of gravitation")
HB22 = val(2022, "reduced Planck constant")
C22 = val(2022, "speed of light in vacuum")
E22 = val(2022, "elementary charge")
MPGEV22 = val(2022, "Planck mass energy equivalent in GeV")
print("\n  CODATA 2022 (scipy 1.17.1 table): G = %.5e +- %.2e, hbar = %.9e, c = %.0f, e = %.9e"
      % (G22, uG22, HB22, C22, E22))
mp = math.sqrt(HB22 * C22 ** 5 / G22) / (E22 * 1e9)
mbar = mp / math.sqrt(8 * math.pi)
print("  M_Pl = %.7e GeV (CODATA's own row: %.6e)   Mbar4 = %.7e GeV" % (mp, MPGEV22, mbar))
chk("(4) computed M_Pl agrees with CODATA 2022's GeV row to its 7 digits",
    abs(mp / MPGEV22 - 1) < 5e-7)
rel_u = 0.5 * uG22 / G22
print("  relative standard uncertainty of Mbar4 (from G alone): %.2e" % rel_u)

# The tree's own numbers, ASKED of the tree (read-only import, no write).
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
sys.dont_write_bytecode = True
try:
    import higgs  # noqa: E402
    tree = higgs.reduced_planck_gev()
    print("  tree higgs.reduced_planck_gev() = %.7e GeV" % tree)
    chk("(4) tree value agrees with CODATA-2022 recomputation to 1e-9",
        abs(tree / mbar - 1) < 1e-9, "(rel %.2e)" % (tree / mbar - 1))
    chk("(4) tree's selftest pin 2.435323e18 within its 1e-5 tolerance",
        abs(tree / 2.435323e18 - 1) < 1e-5)
    chk("(4) tree G == CODATA 2022 G", higgs.G == G22)
    print("  tree HBAR = %.12e vs CODATA exact %.12e (rel %.1e: truncation, not a move)"
          % (higgs.HBAR, 1.054571817646e-34, higgs.HBAR / 1.054571817646e-34 - 1))
except Exception as ex:  # pragma: no cover
    tree = None
    chk("(4) tree import", False, repr(ex))

typed = 2.435e18
rel_typed = (mbar - typed) / mbar
chk("(4) branelink's note: the formerly typed 2.435e18 is 1.3e-4 relative low",
    abs(rel_typed - 1.3e-4) < 0.05e-4, "(%.3e)" % rel_typed)

# ------------------------------------------------------------------ (5) datum history
print("\n  G across CODATA releases, and Mbar4 from it:")
rows = []
for yr in (2006, 2010, 2014, 2018, 2022):
    g = val(yr, "Newtonian constant of gravitation")
    ug = unc(yr, "Newtonian constant of gravitation")
    # in GeV: Mbar c^2 = sqrt(hbar c^5/(8 pi G)) / (e*1e9)
    m_ = math.sqrt(HB22 * C22 ** 5 / (8 * math.pi * g)) / (E22 * 1e9)
    rows.append((yr, g, ug, m_))
    print("    %d  G = %.5e +- %.1e   Mbar4 = %.6e GeV  (vs 2022: %+.2e)"
          % (yr, g, ug, m_, m_ / mbar - 1))
spread = max(abs(x[3] / mbar - 1) for x in rows)
chk("(5) Mbar4 moves < 1e-4 relative across CODATA 2006-2022", spread < 1e-4,
    "(max %.2e)" % spread)

# branelink's SME null |c| ~ 1/Mbar4^2 at fixed r, beta: recompute the scaling.
try:
    import branelink  # noqa: E402
    c0 = branelink.sme_coefficient()
    orders = math.log10(branelink.SME_LAB_BOUND / c0)
    print("\n  branelink |c| = %.3e ; bound %.1e ; orders short %.2f" % (c0, branelink.SME_LAB_BOUND, orders))
    worst = max(abs((mbar / x[3]) ** 2 - 1) for x in rows)
    chk("(5) the G history moves |c| by < 2e-4 relative; 42 orders unmoved",
        worst < 2e-4 and round(math.log10(branelink.SME_LAB_BOUND / (c0 * (1 + worst)))) == 42,
        "(%.2e)" % worst)
    # (6) convention hazard: Mbar4 -> M_Pl (non-reduced) multiplies Mbar4 by sqrt(8 pi),
    # so |c| ~ 1/Mbar4^2 is divided by 8 pi.
    c_nonred = c0 / (8 * math.pi)
    o6 = math.log10(branelink.SME_LAB_BOUND / c_nonred)
    print("  if Mbar4 were the NON-reduced M_Pl: |c| = %.3e, orders short %.2f" % (c_nonred, o6))
    chk("(6) the convention choice moves the null by log10(8 pi) = 1.40 orders, never toward the bound",
        abs((o6 - orders) - math.log10(8 * math.pi)) < 1e-9 and o6 > orders)
    # the other direction (a hypothetical Mbar4 smaller by sqrt(8 pi)) still leaves > 40 orders
    o_rev = math.log10(branelink.SME_LAB_BOUND / (c0 * 8 * math.pi))
    chk("(6) even the adverse direction (x 8 pi) leaves > 40 orders", o_rev > 40,
        "(%.2f)" % o_rev)
    # (5b) sensitivity: |c| ~ 1/Mbar4^2 ~ G, so orders short shift by -log10(G'/G).
    # Factor in G needed to lose one order of the 42: 10.  CODATA 2022's relative
    # uncertainty on G is 2.2e-5; a hypothetical 1e-3 (far beyond any published
    # scatter the tree relies on) shifts the orders by 4.3e-4.
    shift = math.log10(1 + 1e-3)
    chk("(5b) a 1e-3 change in G shifts the SME null by < 1e-3 orders", shift < 1e-3,
        "(%.1e orders)" % shift)
except Exception as ex:  # pragma: no cover
    chk("(5/6) branelink import", False, repr(ex))

print("\n  %s" % ("ALL CHECKS PASS" if not FAIL else "FAILED: %s" % FAIL))
sys.exit(1 if FAIL else 0)
