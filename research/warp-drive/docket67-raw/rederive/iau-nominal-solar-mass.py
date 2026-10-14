#!/usr/bin/env python3
"""DOCKET 67 re-derivation: the warp board's M_SUN = 1.98840e30 kg 'IAU nominal'.

Source READ: Prsa et al. 2016, arXiv:1605.09788 (IAU 2015 Resolution B3).
  Table 1:  1 (GM)_sun^N = 1.3271244e20 m^3 s^-2, exact by definition.
  Rec. 5:   SI masses as (GM)_object / G, with the G used specified.
  App. A:   G = 6.67428e-11 (CODATA 2006, NSFA) -> M_sun^N = 1.988416e30 kg
            G = (6.67408 +- 0.00031)e-11 (CODATA 2014) -> M_sun = (1.988475 +- 0.000092)e30 kg
Current G READ: CODATA 2022, arXiv:2409.03787 Table XXXII: G = 6.67430(15)e-11,
  identical to CODATA 2018 (Sec. I.B.11: 'no new value ... identical').
Tree: nonstatic.py:254-255 G = 6.67430e-11, M_SUN = 1.98840e30; foliation.py:580-581 same;
  ledger.py:332 reads foliation.M_SUN.  Exits 1 if any asserted check fails.
Exact rational arithmetic (sympy.Rational) throughout; no floats in the checks.
"""
import sys
from sympy import Rational as Q, N, sqrt

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-72s %s %s" % (label, "ok" if cond else "FAIL", detail))

GM_N = Q(13271244) * 10**13                   # 1.3271244e20 exact (B3 Table 1)
G06  = Q(667428, 10**5) * Q(1, 10**11)        # CODATA 2006
G14  = Q(667408, 10**5) * Q(1, 10**11)        # CODATA 2014
uG14 = Q(31, 10**5) * Q(1, 10**11)
G18  = Q(667430, 10**5) * Q(1, 10**11)        # CODATA 2018 = CODATA 2022
uG18 = Q(15, 10**5) * Q(1, 10**11)
TREE = Q(198840, 10**5) * 10**30              # nonstatic.py:255, foliation.py:581
C    = Q(299792458)
LY   = Q(94607304725808, 10**13) * 10**15
PROX = Q(42465, 10**4)
LAMBDA = Q("9.982529174194637")              # overturn.py:397 (asked, as ledger.py does)

print("1. B3 APPENDIX A, REPRODUCED")
m06 = GM_N / G06; m14 = GM_N / G14; u14 = m14 * uG14 / G14
print("   GM_N/G_2006 = %s ; GM_N/G_2014 = %s +- %s" % (N(m06, 10), N(m14, 10), N(u14, 3)))
chk("GM_N/G_2006 rounds to the printed 1.988416e30", abs(m06 - Q(1988416, 10**6) * 10**30) < Q(5, 10**7) * 10**30)
chk("GM_N/G_2014 rounds to the printed 1.988475e30", abs(m14 - Q(1988475, 10**6) * 10**30) < Q(5, 10**7) * 10**30)
chk("its G-propagated uncertainty is the printed 0.000092e30", abs(u14 - Q(92, 10**6) * 10**30) < Q(5, 10**7) * 10**30)

print("\n2. THE TREE'S VALUE AGAINST GM_N / G_2018 (the G the tree itself declares)")
m18 = GM_N / G18; u18 = m18 * uG18 / G18
rel = (TREE - m18) / m18
print("   GM_N/G_2018 = %s +- %s kg ; tree 1.98840e30 ; (tree - derived)/derived = %s"
      % (N(m18, 10), N(u18, 3), N(rel, 4)))
chk("derived value to 6 figures is 1.98841e30 (tree prints 1.98840e30: truncation)",
    abs(m18 - Q(198841, 10**5) * 10**30) < Q(5, 10**6) * 10**30)
chk("|tree - derived| < 1 sigma of G (2.2e-5 relative)", abs(rel) < uG18 / G18, "(%s sigma)" % N(abs(rel) / (uG18 / G18), 3))
chk("G*M_SUN in the tree = 1.3271138e20, differs from GM_N by the same -4.96e-6",
    abs((G18 * TREE - GM_N) / GM_N - rel) < Q(1, 10**15))

print("\n3. WHAT RESTS ON IT: nonstatic.build_energy(Proxima span, dW=1) in solar masses")
R = PROX * LY
msun_tree = R * C**2 / (G18 * TREE)
msun_nom  = R * C**2 / GM_N                   # G-free when the nominal GM is used
print("   tree: %s  (selftest pins 2.720744289e13) ; with GM_N exact: %s ; shift %s"
      % (N(msun_tree, 10), N(msun_nom, 10), N((msun_nom - msun_tree) / msun_tree, 4)))
chk("tree arithmetic reproduces the selftest pin 2.720744289e13 to 1e-9",
    abs(msun_tree / Q(2720744289, 10**9) / 10**13 - 1) < Q(1, 10**9))
chk("using GM_N instead moves it by exactly rel = -4.96e-6 (beyond the selftest's 1e-9 pin)",
    abs((msun_nom - msun_tree) / msun_tree - rel) < Q(1, 10**15))
dW = Q(27254, 10**4) * 10**12 / msun_tree
chk("H83d match dW = 0.100171 (nonstatic.py:699, abs tol 1e-5) holds", abs(dW - Q(100171, 10**6)) < Q(1, 10**5), "(%s)" % N(dW, 8))
dWn = Q(27254, 10**4) * 10**12 / msun_nom
chk("and still holds with GM_N", abs(dWn - Q(100171, 10**6)) < Q(1, 10**5), "(%s)" % N(dWn, 8))

print("\n4. B2 (ledger.py:2124-2129): negative enclosed mass for the Proxima span")
PM = PROX * LY
B2_kg = C**2 / (G18 * LAMBDA) * PM
B2_tree = B2_kg / TREE
B2_nom = C**2 * PM / (LAMBDA * GM_N)          # G cancels in solar-mass units
print("   B2 = %s kg = %s M_sun (tree) ; %s M_sun with GM_N" % (N(B2_kg, 6), N(B2_tree, 6), N(B2_nom, 6)))
chk("B2 in tree units is 2.7255e12 (canonical data_used)", abs(B2_tree / (Q(27255, 10**4) * 10**12) - 1) < Q(2, 10**5))
chk("B2 in solar masses is G-independent when GM_N is used (differs from tree by exactly rel)",
    abs((B2_nom - B2_tree) / B2_tree - rel) < Q(1, 10**15))
print("   paper/CLAIMS.md H82c prints 5.4194e42 kg and 2.7254e12 M_sun; the implied M_sun is:")
implied = Q(54194, 10**4) * 10**42 / (Q(27254, 10**4) * 10**12)
print("   5.4194e42 / 2.7254e12 = %s kg" % N(implied, 7))
for lab, M in (("1.98840e30 (nonstatic/foliation)", TREE), ("1.98847e30 (ladder/warpenergy)", Q(198847, 10**5) * 10**30)):
    print("   5.4194e42 kg / %-34s = %s M_sun" % (lab, N(Q(54194, 10**4) * 10**42 / M, 6)))
chk("the 2.7254e12 (H83d) vs 2.7255e12 (B2) last-digit split is the M_SUN choice alone",
    round(float(Q(54194, 10**4) * 10**42 / TREE / 10**8)) == 27255 and
    round(float(Q(54194, 10**4) * 10**42 / (Q(198847, 10**5) * 10**30) / 10**8)) == 27254)

print("\n5. TREE-INTERNAL SPREAD OF M_SUN (grep of research/warp-drive/*.py, recorded not repaired)")
vals = {"1.98840e30": TREE, "1.98847e30": Q(198847, 10**5) * 10**30,
        "1.98892e30": Q(198892, 10**5) * 10**30, "1.989e30": Q(1989, 10**3) * 10**30}
for k, v in vals.items():
    print("   %-11s implies G = GM_N/M = %s ; vs GM_N/G_2018: %s" % (k, N(GM_N / v, 7), N((v - m18) / m18, 3)))
spread = (vals["1.98892e30"] - TREE) / TREE
chk("max spread across modules 2.6e-4 relative: far below any verdict (orders of magnitude)", spread < Q(3, 10**4), "(%s)" % N(spread, 3))

print("\n6. SECULAR DRIFT (Pitjeva et al. 2022, arXiv:2201.09804, READ)")
rate = Q(-102, 10) * Q(1, 10**14)   # d(GM)/dt / GM per year
yrs = 2026 - 2015
chk("GM_sun drift 2015->2026 is ~1.1e-12 relative, 6 orders below the tree's 4.96e-6 truncation",
    abs(rate * yrs) < Q(2, 10**12), "(%s)" % N(rate * yrs, 3))

print("\nALL CHECKS PASS" if ok else "\nA CHECK FAILED")
sys.exit(0 if ok else 1)
