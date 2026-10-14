"""DOCKET 67 -- audit 'astronomical-body-data' (spec.py:65-72, 148, 235-237).
Re-derives, in exact rational arithmetic (sympy Rational) where the input is exact,
every comparison between the tree's body data and the source values READ:
  IAU 2015 Resolution B3 (arXiv:1510.07674v1, cached page text
  d67/src/casmag/all/1510.07674v1.txt, md5 6bdffaf89a7a45b40be462d8b910098f),
  IAU 2012 B2 au (READ-VIA-RESTATEMENT: B3 endnote 4),
  CODATA G (scipy.constants, CODATA 2022 = 2018 value 6.67430(15)e-11).
Imports spec.py READ-ONLY (no bytecode written) to confirm the literals.
Exit 0 iff every check passes.  A check here asserts a MEASUREMENT of a discrepancy,
never that the tree is wrong."""
import sys, os, math, hashlib
sys.dont_write_bytecode = True
from sympy import Rational as Q, Integer, cbrt, N, nsimplify
WD = "/home/user/Claude-Method-Works/research/warp-drive"
SRC = ("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/"
       "scratchpad/d67/src/casmag/all/1510.07674v1.txt")
sys.path.insert(0, WD)
import spec
import scipy.constants as sc

fails = 0
def chk(label, cond, detail=""):
    global fails
    print("  [%s] %s%s" % ("ok" if cond else "FAIL", label, ("  -- " + detail) if detail else ""))
    if not cond:
        fails += 1

def rel(a, b):
    return (a - b) / b

print("0. SOURCE TEXT: the B3 values are the ones printed in the cached arXiv page text")
txt = " ".join(open(SRC, encoding="utf-8").read().split())
chk("cached B3 md5", hashlib.md5(open(SRC, "rb").read()).hexdigest() == "6bdffaf89a7a45b40be462d8b910098f")
for s in ("= 6.957 × 10", "= 6.3781 × 10", "= 6.3568 × 10", "= 7.1492 × 10", "= 6.6854 × 10",
          "= 3.986 004 × 10", "= 1.266 865 3 × 10", "= 1.327 124 4 × 10", "149 597 870 700 m exactly",
          "695 658 (± 140) km", "one-bar equato", "zero tide"):
    chk("B3 text contains %r" % s, s in txt)

# ---- source values (exact rationals as printed) ----
RsN  = Q(6957, 10) * 10**6          # 6.957e8 m
ReE  = Q(63781, 10**4) * 10**6      # 6.3781e6
RpE  = Q(63568, 10**4) * 10**6
ReJ  = Q(71492, 10**4) * 10**7
RpJ  = Q(66854, 10**4) * 10**7
GMs  = Q(13271244, 10**7) * 10**20
GME  = Q(3986004, 10**6) * 10**14
GMJ  = Q(12668653, 10**7) * 10**17
AU_iau = Integer(149597870700)
c = Integer(299792458)
LY_exact = c * Q(36525, 100) * 86400
G = Q("6.67430e-11"); uG = Q("0.00015e-11")
chk("scipy G is CODATA 6.67430(15)e-11", abs(sc.G - 6.6743e-11) < 1e-20 and
    abs(sc.physical_constants['Newtonian constant of gravitation'][2] - 1.5e-15) < 1e-22)

# ---- tree values, from spec.py itself ----
L = {n: (Q(repr(M)), Q(repr(b))) for n, M, b in spec.LENSES}
AU_t = Q(repr(spec.AU)); LY_t = Q(repr(spec.LIGHT_YEAR))
Gt = Q(repr(spec.G_SI)); ct = Q(repr(spec.C_SI))
chk("spec literals as canonical.json records",
    (L["Sun"] == (Q("1.989e30"), Q("6.957e8")) and L["Jupiter"] == (Q("1.898e27"), Q("7.15e7"))
     and L["Earth"] == (Q("5.972e24"), Q("6.371e6")) and L["10 km asteroid"] == (Q("2.25e15"), Q("1.0e4"))
     and AU_t == Q("1.495979e11") and LY_t == Q("9.4607e15") and Gt == G and ct == c))

print("\n1. RADII")
chk("R_sun tree == B3 nominal 6.957e8 exactly", L["Sun"][1] == RsN)
print("     B3 note 2: nominal from Haberreiter 2008 photospheric 695 658 +- 140 km; "
      "nominal - measured = %+.0f km (%.2f sigma)" % (float(RsN/1000 - 695658), float((RsN/1000 - 695658)/140)))
volJ = (ReJ**2 * RpJ) ** Q(1, 3); volE = (ReE**2 * RpE) ** Q(1, 3)
arithE = (2*ReE + RpE) / 3
print("     Jupiter: tree 7.15e7; B3 R_eJ 7.1492e7 (rel %+.3e); R_pJ 6.6854e7; volumetric mean %.6e"
      % (float(rel(L["Jupiter"][1], ReJ)), float(N(volJ))))
chk("Jupiter tree radius is R_eJ rounded to 3 s.f. (the 1-bar EQUATORIAL radius)",
    float(ReJ) == float(ReJ) and round(float(ReJ), -5) == float(L["Jupiter"][1]))
chk("  and NOT the volumetric mean (6.99e7 at 3 s.f.)", round(float(N(volJ)), -5) != float(L["Jupiter"][1]))
print("     Earth: tree 6.371e6; B3 R_eE 6.3781e6 (rel %+.3e); R_pE 6.3568e6; (2a+b)/3 = %.6e; volumetric %.6e"
      % (float(rel(L["Earth"][1], ReE)), float(arithE), float(N(volE))))
chk("Earth tree radius is the MEAN radius computed from B3's radii (both means round to 6.371e6)",
    round(float(arithE), -3) == float(L["Earth"][1]) and round(float(N(volE)), -3) == float(L["Earth"][1]))
chk("  and NOT B3's default terrestrial radius R_eE (Explanation 6)", L["Earth"][1] != ReE)
eps = {"Sun(B3 gives one radius)": None, "Earth": 1 - RpE/ReE, "Jupiter": 1 - RpJ/ReJ}
print("     oblateness from B3's own radii: Earth %.5f (1/%.2f), Jupiter %.5f (1/%.2f)"
      % (float(eps["Earth"]), float(1/eps["Earth"]), float(eps["Jupiter"]), float(1/eps["Jupiter"])))

print("\n2. MASSES = (GM)^N / G  (B3 Recommends 5), CODATA G")
for name, GM in (("Sun", GMs), ("Jupiter", GMJ), ("Earth", GME)):
    M = GM / G; sM = M * uG / G
    Mt = L[name][0]
    r4 = float("%.4g" % float(M))
    print("     %-8s tree %.4e  (GM)^N/G = %.6e +- %.1e (G 1 sigma)  rel %+.3e  = %.1f sigma_G;  4-s.f. rounding %.4e"
          % (name, float(Mt), float(M), float(sM), float(rel(Mt, M)), float((Mt - M)/sM), r4))
    if name == "Sun":
        chk("M_sun tree 1.989e30 is NOT the 4-s.f. rounding of (GM)^N/G (which is 1.988e30)", r4 == 1.988e30)
        for Gold, lab in ((Q("6.6720e-11"), "CODATA 1973 G 6.6720e-11"), (Q("6.67259e-11"), "CODATA 1986 G 6.67259e-11")):
            print("       with %s: (GM)^N/G = %.5e" % (lab, float(GMs/Gold)))
        chk("  it IS the 4-s.f. rounding of (GM)^N/G for the CODATA-1973 G (1.98909e30) -- an older-G figure",
            float("%.4g" % float(GMs/Q("6.6720e-11"))) == 1.989e30)
        chk("  relative excess over current value < 3e-4 (i.e. inside spec's 1e-3 selftest pin)", abs(float(rel(Mt, M))) < 3e-4)
    else:
        chk("%s tree mass == 4-s.f. rounding of (GM)^N/G" % name, r4 == float(Mt))

print("\n3. au AND light-year")
print("     au: tree %.7e vs 149 597 870 700 exact; rel %+.3e" % (float(AU_t), float(rel(AU_t, AU_iau))))
chk("tree au is the 7-s.f. rounding of the IAU 2012 au", float("%.7g" % float(AU_iau)) == float(AU_t))
print("     ly: tree %.5e vs c x Julian yr = %d m exactly; rel %+.3e" % (float(LY_t), int(LY_exact), float(rel(LY_t, LY_exact))))
chk("c x 365.25 x 86400 == 9460730472580800 exactly", LY_exact == 9460730472580800)
chk("tree ly is the 5-s.f. rounding of it", float("%.5g" % float(LY_exact)) == float(LY_t))

print("\n4. WHAT THE DATA FEED: f = b^2 c^2 / (4 G M) = b^2 c^2 / (4 GM)")
def f(GM, b): return b*b*c*c / (4*GM)
ft = {n: f(G*M, b) for n, (M, b) in L.items()}
chk("tree focal lengths reproduce spec.focal_length to 1e-12",
    all(abs(float(ft[n]) / spec.focal_length(float(M), float(b)) - 1) < 1e-12 for n, (M, b) in L.items()))
f_sun_t = ft["Sun"] / AU_t
f_sun_iau = f(GMs, RsN) / AU_iau
print("     Sun: tree %.4f AU; IAU (GM)^N, R^N, au %.4f AU; rel %+.3e" % (float(f_sun_t), float(f_sun_iau), float(rel(f_sun_t, f_sun_iau))))
chk("spec selftest pin |f/547.6 - 1| <= 1e-3 holds for the tree data", abs(float(f_sun_t)/547.6 - 1) <= 1e-3)
chk("  and for the current (IAU 2015 / IAU 2012) data", abs(float(f_sun_iau)/547.6 - 1) <= 1e-3)
for pub, who in ((550, "spec.py:66 '~550 AU' (uncited)"), (546, "Hippke 2018 arXiv:1711.07962 sec 5.6.1 '~546 au' (READ, cached)"),
                 (Q("547.8"), "Turyshev & Toth ~547.8 AU (NOT READ; prior audit's WebSearch summary)")):
    print("     comparator %-7s %-70s tree %+.3f%%  IAU %+.3f%%" % (float(pub), who, float(100*rel(f_sun_t, pub)), float(100*rel(f_sun_iau, pub))))
chk("Hippke's R^2/(2 r_g) with his own rounded r_g=2950 m gives 548.4 AU, not his printed 546: the comparator's own inputs do not reproduce it (a discrepancy in the comparator, recorded; R_sun he used is not stated)",
    abs(float((RsN**2/(2*2950))/AU_iau) - 548.4) < 0.1)
for name, GM, bs in (("Jupiter", GMJ, (("tree 7.15e7", L["Jupiter"][1]), ("R_eJ", ReJ), ("volumetric", volJ), ("R_pJ", RpJ))),
                     ("Earth", GME, (("tree 6.371e6", L["Earth"][1]), ("R_eE", ReE), ("volumetric", volE), ("R_pE", RpE)))):
    row = "     %-8s tree %.5g AU;" % (name, float(ft[name] / AU_t))
    for lab, b in bs:
        row += "  %s %.5g" % (lab, float(N(f(GM, b) / AU_iau)))
    print(row)
rJ = (RpJ/ReJ)**2; rE = (RpE/ReE)**2
print("     polar-plane / equatorial-plane grazing focus: Jupiter %.4f (%.1f%% shorter), Earth %.5f (%.2f%%)"
      % (float(rJ), float(100*(1-rJ)), float(rE), float(100*(1-rE))))
fJ_pole = f(GMJ, RpJ) / AU_iau
chk("Jupiter: a polar-grazing ray (b = R_pJ, through vacuum above the 1-bar level) focuses at < tree's printed minimum 6061 AU",
    float(fJ_pole) < 6061 and abs(float(fJ_pole) - 5300) < 10, "%.1f AU (monopole; J2 quadrupole NOT computed)" % float(fJ_pole))
chk("Earth: polar-grazing focus below the tree's 15295 AU", float(f(GME, RpE)/AU_iau) < 15295,
    "%.1f AU" % float(f(GME, RpE)/AU_iau))
print("     Sun: B3 gives ONE radius. f scales as b^2, so an equator-pole difference eps moves f by ~2 eps;")
print("          the 1e-3 pin tolerates eps up to ~5e-4.  Rotational estimate eps ~ q/2, q = w^2 R^3/GM,")
for P_days in (25.38, 25.05):   # INPUTS NAMED-NOT-READ (Carrington sidereal; equatorial sidereal)
    w = 2*math.pi/(P_days*86400); q = w*w*float(RsN)**3/float(GMs)
    print("          P = %.2f d (NAMED-NOT-READ input) -> q = %.3e, q/2 = %.2e" % (P_days, q, q/2))
    chk("  solar eps estimate << 5e-4 (%.2f d)" % P_days, q/2 < 5e-5)
chk("Sun lies far outside its Schwarzschild radius (S-1/SR2 witness): R_s/R_sun",
    float(2*GMs/c**2/RsN) < 1e-5, "%.3e" % float(2*GMs/c**2/RsN))

print("\n5. THE 10 km ASTEROID -- the owner's figure, not a measured body")
M_a, b_a = L["10 km asteroid"]
rho_r = M_a / (Q(4, 3) * Q(str(math.pi)) * b_a**3)
rho_d = M_a / (Q(4, 3) * Q(str(math.pi)) * (b_a/2)**3)
print("     implied bulk density if b = 1e4 m is the RADIUS: %.0f kg/m^3; if '10 km' were the DIAMETER, same mass: %.0f kg/m^3"
      % (float(rho_r), float(rho_d)))
chk("with b = 1.0e4 the '10 km' is a radius (20 km body) -- a naming ambiguity, recorded", b_a == 10**4)
print("     f_ast (tree) = %.1f ly; with b = 5e3 m it would be %.1f ly (f ~ b^2)"
      % (float(ft["10 km asteroid"]/LY_t), float(f(G*M_a, b_a/2)/LY_t)))
chk("tree f_ast in ly moves < 1e-5 between tree ly and exact ly",
    abs(float(ft["10 km asteroid"]/LY_t / (ft["10 km asteroid"]/LY_exact)) - 1) < 1e-5)

print("\nfailures:", fails)
sys.exit(1 if fails else 0)
