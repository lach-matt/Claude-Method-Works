#!/usr/bin/env python3
"""DOCKET 67, result 19/36: cmb-dipole-370kms.

Re-derives, exactly (sympy rationals, 50 digits) and by an independent float
route, every number the tree takes from the CMB dipole:
  (1) Gamma - 1 at V_CMB = 3.7e5 m/s (branelink.py:150, 270-272, 463-464),
  (2) the Planck 2018 dipole amplitude -> beta -> v (the published chain),
  (3) Gamma - 1 at the Planck 2018 velocity and its 1-sigma band,
  (4) the Solar-System-barycentre vs EARTH distinction (annual +-29 km/s),
  (5) whether any of that moves O7's conclusion (B_cmb vs B_for_one_second).
Inputs are labelled: TREE (as the tree types it), RESTATED (Planck 2018
figures as restated by a secondary source -- see the audit JSON), EXACT (SI
definitions), CONVENTION (IAU constants).  Exit 1 on any failed assertion.
"""
import math, sys
import sympy as sp

sp.init_printing()
D = 50
ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok &= bool(cond)

c = sp.Integer(299792458)                       # EXACT, m/s
# ---- (1) the tree's figure ---------------------------------------------
V_tree = sp.Rational(370000)                    # TREE branelink.py:150
b = V_tree / c
gm1_exact = 1 / sp.sqrt(1 - b**2) - 1
g_tree = sp.N(gm1_exact, D)
g_float = math.expm1(-0.5 * math.log1p(-(3.7e5 / 299792458.0) ** 2))   # tree's route
print("beta(3.7e5)          =", sp.N(b, 20))
print("Gamma-1 (exact,50d)  =", g_tree)
print("Gamma-1 (tree route) = %.12e" % g_float)
check("tree route agrees with exact to 1e-12 rel", abs(g_float / float(g_tree) - 1) < 1e-12)
check("branelink selftest pin 7.6161e-07 within 1e-4", abs(float(g_tree) / 7.6161e-07 - 1) < 1e-4)
check("canonical data_used 7.616098e-07 to 7 figures", abs(float(g_tree) - 7.616098e-07) < 5e-14)
# series: b^2/2 + 3 b^4/8
ser = sp.N(b**2 / 2 + 3 * b**4 / 8 + 5 * b**6 / 16, D)
check("three-term series b^2/2+3b^4/8+5b^6/16 matches to 1e-15 rel", abs(float(ser) / float(g_tree) - 1) < 1e-15)

# ---- (2) Planck 2018 chain: amplitude / T0 -> beta -> v -----------------
A_uK = sp.Rational('3362.08'); sA = sp.Rational('0.99')   # RESTATED Planck 2018 I
beta_pub = sp.Rational('1.23357e-3'); sb = sp.Rational('0.00036e-3')
v_pub = sp.Rational('369.82e3'); sv = sp.Rational('0.11e3')
for T0 in (sp.Rational('2.7255'), sp.Rational('2.72548')):   # Fixsen 2009 (both roundings)
    beta = A_uK * sp.Rational(1, 10**6) / T0
    print("T0=%s  beta=A/T0=%s  v=%s km/s" % (T0, sp.N(beta, 8), sp.N(beta * c / 1000, 8)))
    check("A/T0 reproduces published beta within its sigma (T0=%s)" % T0,
          abs(beta - beta_pub) <= sb)
    check("beta*c reproduces published v within its sigma (T0=%s)" % T0,
          abs(beta * c - v_pub) <= sv)
# relativistic dipole coefficient of T(theta)=T0/(Gamma(1-beta cos)) is beta + O(beta^3)
th, B = sp.symbols('theta beta', positive=True)
T = 1 / (sp.sqrt(1 - B**2) ** -1 * (1 - B * sp.cos(th)))
a1 = sp.integrate(sp.series(T, B, 0, 4).removeO() * sp.cos(th) * sp.sin(th), (th, 0, sp.pi)) * sp.Rational(3, 2)
a1 = sp.simplify(a1)
print("dipole coefficient of the boosted blackbody temperature to O(beta^3):", a1)
check("dipole = beta + O(beta^3) (so A/T0 = beta to 1e-6 rel)", sp.simplify(a1 - B) != 0 and
      sp.Poly(sp.expand(a1 - B), B).degree() >= 3)

# ---- (3) Gamma-1 at the Planck velocity ---------------------------------
def gm1(v):
    x = sp.Rational(v) / c
    return sp.N(1 / sp.sqrt(1 - x**2) - 1, D)
g_pl = gm1('369820'); g_lo = gm1('369710'); g_hi = gm1('369930')
g_hfi = gm1('369816')                           # RESTATED HFI 369.8160 (litebird_sim)
print("Gamma-1 @369.82 km/s  =", sp.N(g_pl, 10), " band [", sp.N(g_lo, 8), ",", sp.N(g_hi, 8), "]")
print("Gamma-1 @369.816 km/s =", sp.N(g_hfi, 10))
rel = float(g_tree / g_pl - 1)
print("tree / Planck - 1     = %.4e   (v: %.4e)" % (rel, 370000 / 369820 - 1))
check("tree's 3.7e5 is 2-figure rounding of 369.82 (|dv| = 0.18 km/s < 5 km/s, the 2-figure half-unit)",
      abs(370000 - 369820) < 5000)
check("tree Gamma-1 outside Planck 1-sigma band (discrepancy of rounding, not error)",
      not (g_lo <= g_tree <= g_hi))
check("4-figure print 7.6161e-07 would read 7.6087e-07 at Planck value",
      round(float(g_pl) * 1e11) / 1e4 == 7.6087 or abs(float(g_pl) - 7.6087e-07) < 5e-12)

# ---- (4) barycentre vs Earth: galactic -> ecliptic, annual modulation ----
l, bb = math.radians(264.021), math.radians(48.253)       # RESTATED Planck 2018
rg = (math.cos(bb) * math.cos(l), math.cos(bb) * math.sin(l), math.sin(bb))
M = ((-0.0548755604162154, +0.4941094278755837, -0.8676661490190047),   # CONVENTION: columns = galactic x,y,z axes in ICRS
     (-0.8734370902348850, -0.4448296299600112, -0.1980763734312015),   # (Hipparcos / ESA 1997)
     (-0.4838350155487132, +0.7469822444972189, +0.4559837761750669))
req = tuple(sum(M[i][j] * rg[j] for j in range(3)) for i in range(3))  # r_icrs = M r_gal
ra = math.degrees(math.atan2(req[1], req[0])) % 360; dec = math.degrees(math.asin(req[2]))
eps = math.radians(23.4392911)                                     # CONVENTION J2000 obliquity
recl = (req[0], req[1] * math.cos(eps) + req[2] * math.sin(eps), -req[1] * math.sin(eps) + req[2] * math.cos(eps))
lam = math.degrees(math.atan2(recl[1], recl[0])) % 360; bet = math.degrees(math.asin(recl[2]))
print("dipole apex: RA %.3f Dec %.3f ; ecliptic lon %.3f lat %.3f" % (ra, dec, lam, bet))
check("apex RA/Dec near the textbook (168, -7)", abs(ra - 168.0) < 1.0 and abs(dec + 7.0) < 1.0)
AU = 149597870700.0; YR = 365.25 * 86400                            # EXACT (IAU 2012), Julian year
u = 2 * math.pi * AU / YR                                           # circular-orbit hypothesis
V = 369820.0
cb = math.cos(math.radians(bet))
vmax = math.sqrt(V**2 + u**2 + 2 * V * u * cb); vmin = math.sqrt(V**2 + u**2 - 2 * V * u * cb)
print("mean orbital speed u = %.3f km/s ; Earth vs CMB: %.2f .. %.2f km/s" % (u / 1e3, vmin / 1e3, vmax / 1e3))
gmin = float(gm1(repr(round(vmin)))); gmax = float(gm1(repr(round(vmax))))
print("Earth's Gamma-1 over a year: %.4e .. %.4e  (%.1f%% .. %+.1f%% of the barycentre value)"
      % (gmin, gmax, 100 * (gmin / float(g_pl) - 1), 100 * (gmax / float(g_pl) - 1)))
check("Earth's annual spread (~16 pct) dwarfs the 0.1 pct rounding", (gmax - gmin) / float(g_pl) > 0.1)

# ---- (5) does it move O7?  B_cmb against the tree's own priced escape ----
B_cmb = float(sp.N(sp.Rational(369820) / c, 20))
B_one_second = 0.999387630                                           # TREE ledger O7 / branelink
print("B_cmb = %.6e ; B needed for 1 s = %.9f ; ratio %.1f" % (B_cmb, B_one_second, B_one_second / B_cmb))
check("B at Earth's annual max is < 1/500 of the priced escape B", vmax / 299792458.0 < B_one_second / 500)
# tree's own saving model as inverted in branelink.b_for_saving: saving = T d ((1+B)/(1-B))^2
d = 7.0e-16; T = 1.3400934840e8
for lab, Bv in (("B=0", 0.0), ("B=B_cmb", B_cmb), ("B=Earth max", vmax / 299792458.0)):
    print("  tree model saving at %-12s = %.4f ns" % (lab, T * d * ((1 + Bv) / (1 - Bv)) ** 2 * 1e9))
print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
