#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key si-astro-constants-c-g-msun-ly.

Exact rational arithmetic (sympy Rational) on the four constants foliation.py:579-582
types, against the values READ at source:
  c        = 299 792 458 m/s exact            CODATA 2022 (arXiv:2409.03787) Table XXXII
  G        = 6.674 30(15)e-11, u_r 2.2e-5      CODATA 2022 = CODATA 2018 (same paper, Sec. XIV/XV)
  (GM)^N_sun = 1.327 124 4e20 m^3 s^-2 exact  IAU 2015 B3 (arXiv:1510.07674) -- NO kg value defined;
             Recommends 5: SI mass = (GM)/G with the G stated.
  GM_sun best estimate 1.327 124 400 41e20 (+-1e-10 relative? +-1e10 m^3/s^2) Folkner, as restated
             in arXiv:1511.01546 Sec. 1.7 (IAU 2009 system).
  ly       = c x Julian year (365.25 x 86400 s): the Julian-year definition is NAMED-NOT-READ here;
             only the product is computed.
Reads research/warp-drive/foliation.py and overturn.py read-only (import); writes nothing there.
Exit 1 on any failed check.
"""
import sys
sys.dont_write_bytecode = True  # never write __pycache__ into research/warp-drive
from sympy import Rational as R, nsimplify
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import foliation, overturn  # noqa: E402

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails.append(name)

def Q(x):  # exact rational of a decimal literal via repr (no binary float drift)
    return R(repr(x))

c_tree, G_tree, M_tree, ly_tree = map(Q, (foliation.C_LIGHT, foliation.G_NEWTON,
                                          foliation.M_SUN, foliation.LY))
c_src = R(299792458)
G_src, uG = R("6.67430e-11"), R("0.00015e-11")
GMN = R("1.3271244e20")
GM_best = R("1.32712440041e20")
julian_year_s = R("365.25") * 86400

print("1. c")
chk("c tree == CODATA exact 299792458", c_tree == c_src)

print("2. G")
chk("G tree == CODATA 2018/2022 6.67430e-11", G_tree == G_src)
urG = uG / G_src
print("   u_r(G) = %.3e" % float(urG))

print("3. M_sun")
M_nom = GMN / G_src
M_best = GM_best / G_src
print("   (GM)^N/G      = %.9e kg" % float(M_nom))
print("   GM_best/G     = %.9e kg" % float(M_best))
rel = (M_tree - M_nom) / M_nom
print("   tree - (GM)^N/G relative = %.3e  (%.3e kg)" % (float(rel), float(M_tree - M_nom)))
chk("tree M_sun within 1 sigma of G-limited kg value", abs(rel) < urG,
    "|%.2e| < %.2e" % (float(rel), float(urG)))
chk("tree M_sun is NOT the 6-s.f. rounding of (GM)^N/G (1.98841e30) -- discrepancy, expect PASS",
    M_tree != R("1.98841e30"))
chk("(GM)^N/G rounds to 1.98841e30 at 6 s.f.",
    abs(M_nom - R("1.98841e30")) < R("0.000005e30"))
GM_tree = G_tree * M_tree
relGM = (GM_tree - GMN) / GMN
print("   G*M_sun tree  = %.9e m^3/s^2, vs (GM)^N rel %.3e, vs best rel %.3e"
      % (float(GM_tree), float(relGM), float((GM_tree - GM_best) / GM_best)))

print("4. light year")
ly_exact = c_src * julian_year_s
print("   c x 365.25 x 86400 = %s m" % ly_exact)
chk("LY tree == c x Julian year exactly", ly_tree == ly_exact)
import ledger  # noqa: E402  (read-only import; its own module-level code only defines)
chk("ledger.LY_M == foliation.LY", Q(ledger.LY_M) == ly_tree)

print("5. downstream figures (ledger B1/B2) and their sensitivity")
Lam = Q(overturn.LAMBDA)
X = c_src**2 / (G_src * Lam)
print("   EXCHANGE_RATE = c^2/(G Lambda) = %.9e kg/m" % float(X))
chk("reproduces 1.348948e26 at 7 s.f.", round(float(X) / 1e26, 6) == 1.348948)
dX = X * urG
print("   1-sigma from G alone: +-%.2e kg/m -> 7th figure (1e-6 of 1e26 = 1e20) moves by %.0f units"
      % (float(dX), float(dX / R("1e20"))))
chk("7th s.f. of EXCHANGE_RATE is BELOW G's precision (over-precise pin, a discrepancy of "
    "representation, expect PASS)", dX > R("1e20"))
PROX = Q(foliation.PROXIMA_LY) * ly_tree
B2kg = X * PROX
B2ms_tree = B2kg / M_tree
B2ms_GM = c_src**2 * PROX / (Lam * GMN)   # G cancels when M_sun = (GM)/G
print("   B2 demand = %.6e kg ; %.6g M_sun (tree) ; %.6g M_sun^N (G-free, via (GM)^N)"
      % (float(B2kg), float(B2ms_tree), float(B2ms_GM)))
chk("B2 5.4194e42 kg at 5 s.f.", round(float(B2kg) / 1e42, 4) == 5.4194)
relB2 = (B2ms_tree - B2ms_GM) / B2ms_GM
print("   B2 in solar masses: tree vs G-free differ by %.3e relative; printed %%.6g strings: %s vs %s"
      % (float(relB2), "%.6g" % float(B2ms_tree), "%.6g" % float(B2ms_GM)))
# worst case over the G interval for the kg-denominated figure
for k in (-1, 1):
    Gk = G_src + k * uG
    print("   G %+d sigma: EXCHANGE_RATE %.6e, B2 %.4e kg" % (k, float(c_src**2/(Gk*Lam)),
          float(c_src**2/(Gk*Lam)*PROX)))
chk("FINDING reproduced: B2 kg figure's 5th s.f. is NOT stable across G +-1 sigma "
    "(ledger pins 5.4194e42 'to 5 figures'; G supports ~4-5) -- expect PASS",
    not all(round(float(c_src**2/((G_src+k*uG)*Lam)*PROX)/1e42, 4) == 5.4194 for k in (-1, 1)))
chk("FINDING reproduced: printed %.6g solar-mass B2 differs in 6th s.f. between tree M_SUN "
    "and (GM)^N route -- expect PASS", "%.6g" % float(B2ms_tree) != "%.6g" % float(B2ms_GM))
chk("but the refusal does not move: B1/B2 gap is None in ledger.balance()",
    all(r[4] is None for r in ledger.balance() if r[0] in ("B1", "B2")))

print("6. gauge_bill_msun reads only the product G*M_sun")
b = foliation.gauge_bill_msun(1.0, 1.0)
chk("gauge_bill_msun(1,1) == c^2/(G M_sun)", abs(b - float(c_src**2/(G_tree*M_tree))) / b < 1e-14,
    "%.9e" % b)

print("\nRESULT: %d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
