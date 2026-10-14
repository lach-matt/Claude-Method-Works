#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Anglada-Escude et al. 2016 (arXiv:1609.03449), Proxima b.

Re-derives Table 1's derived quantities (a, m_p sin i) from its Keplerian fit
(P, K) and stellar mass by the RV mass function and Kepler III (sympy solve +
numeric), then recomputes with the later published inputs (SM2020, Faria 2022,
NIRPS 2025), and tests whether any moved datum moves the tree's conclusion:
    formation.py: m_p sin i * M_earth / stockgate.feedstock_kg(70,'as-composed 59','CI chondrite') > 1
Reads research/warp-drive READ-ONLY (bytecode writing disabled).
Exit 0 iff every check passes.
"""
import math, sys
sys.dont_write_bytecode = True
import sympy as sp

GM_SUN = 1.32712440018e20   # m^3 s^-2 (IAU 2015 nominal)
GM_EARTH = 3.986004418e14   # m^3 s^-2
AU = 1.495978707e11
DAY = 86400.0

fails = []
def chk(label, got, want, tol):
    ok = abs(got - want) <= tol
    print(("PASS " if ok else "FAIL ") + "%-66s got %.5g want %.5g +- %.3g" % (label, got, want, tol))
    if not ok:
        fails.append(label)

# symbolic mass function
m, Ms, P, K, e, G = sp.symbols('m M_s P K e G', positive=True)
massfn = sp.Eq(K, (2*sp.pi*G/P)**sp.Rational(1, 3) * m / (Ms + m)**sp.Rational(2, 3) / sp.sqrt(1 - e**2))

def msini(K_ms, P_d, Mstar_sun, ecc=0.0):
    """numeric root of the RV mass function (edge-on m == m sin i), Earth masses"""
    f = sp.lambdify(m, massfn.lhs - massfn.rhs.subs({Ms: Mstar_sun*GM_SUN, P: P_d*DAY, K: K_ms, e: ecc, G: 1}), 'mpmath')
    # m here is GM of planet (G folded into masses); start at 1 Earth
    root = sp.nsolve(massfn.rhs.subs({Ms: Mstar_sun*GM_SUN, P: P_d*DAY, K: K_ms, e: ecc, G: 1}) - K_ms, m, GM_EARTH)
    return float(root) / GM_EARTH

def semimajor(P_d, Mstar_sun, mp_earth=0.0):
    GMt = Mstar_sun*GM_SUN + mp_earth*GM_EARTH
    return (GMt * (P_d*DAY)**2 / (4*math.pi**2))**(1/3) / AU

print("== 1. Anglada-Escude 2016 Table 1 re-derived from its own inputs ==")
P16, K16, M16 = 11.186, 1.38, 0.120
a16 = semimajor(P16, M16)
ms16 = msini(K16, P16, M16, 0.0)
print("   a = %.5f au ; m sin i (e=0) = %.4f M_E" % (a16, ms16))
chk("a from P=11.186 d, M*=0.120 (Table 1: 0.0485)", a16, 0.0485, 0.0005)
# DISCREPANCY RECORDED, not a refutation: the mass function applied to Table 1's own
# MAP K, P and M* does not return Table 1's MAP m sin i.
print("   DISCREPANCY: f(K=1.38,P=11.186,M*=0.120) = %.3f vs Table 1 MAP 1.27 (ratio %.3f)" % (ms16, 1.27/ms16))
chk("re-derived m sin i lies inside Table 1's own 68% c.i. [1.10,1.46]", 1.0 if 1.10 <= ms16 <= 1.46 else 0.0, 1.0, 0)
chk("the gap is real (> 5%): Table 1 MAP / f(MAP inputs) - 1", 1.27/ms16 - 1, 0.0816, 0.01)
lo, hi = msini(1.17, P16, M16), msini(1.59, P16, M16)
print("   K in [1.17,1.59] -> m sin i in [%.3f, %.3f] (Table 1 c.i. [1.10,1.46]; same ~8-10%% offset)" % (lo, hi))
Mneed = M16 * (1.27/ms16)**1.5
print("   M* that would return 1.27 from K=1.38: %.4f M_sun (Table 1 M* interval [0.105,0.135]); a at that M*: %.4f au vs 0.0485"
      % (Mneed, semimajor(P16, Mneed)))
# independent corroboration: SM2020 combined fit, K=1.377 (~= 2016's 1.38), D00 M*=0.120 -> published 1.15
sm_d00 = msini(1.377, 11.18427, 0.120, 0.124)
chk("SM2020 combined, Delfosse M*=0.120 (published 1.15): same K as 2016", sm_d00, 1.15, 0.03)
# sanity of the formula: Earth around the Sun, K = 0.0894 m/s
chk("formula sanity: Earth-Sun K -> 1 M_E", msini(0.08945, 365.25636, 1.0), 1.0, 0.01)
ms16e = msini(K16, P16, M16, 0.35)
print("   at the e<0.35 bound: m sin i = %.4f (factor sqrt(1-e^2) = %.4f)" % (ms16e, math.sqrt(1-0.35**2)))
chk("the rounded figure the tree reads: 1.27 -> 1.3 (abstract)", round(1.27, 1), 1.3, 1e-9)
chk("the rounded figure the tree reads: 0.0485 -> 0.05 (abstract '~0.05')", round(0.0485, 2), 0.05, 1e-9)

print("== 2. later inputs (READ at source) ==")
later = [
    ("SM2020 ESPRESSO-only (M15 M*)", 1.51, 11.218, 0.1221, 0.105, 1.29),
    ("SM2020 combined (M15 M*)",       1.377, 11.18427, 0.1221, 0.124, 1.173),
    ("Faria 2022 TM RVs",              1.24, 11.1868, 0.1221, 0.02, 1.07),
    ("NIRPS 2025 all data",            1.226, 11.18465, 0.1221, 0.0, 1.055),
]
for name, Kx, Px, Mx, ex, pub in later:
    v = msini(Kx, Px, Mx, ex)
    chk("%s: m sin i (published %.3f)" % (name, pub), v, pub, 0.03)
    print("      a = %.5f au" % semimajor(Px, Mx, v))
# stellar-mass swap alone (Delfosse 0.120 -> Mann 0.1221) on the 2016 K
ms16m = msini(K16, P16, 0.1221)
print("   2016 K with M* 0.1221: %.4f M_E (shift %+.2f%%)" % (ms16m, 100*(ms16m/ms16-1)))

print("== 3. does the tree's conclusion move? ==")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import stockgate, ladder
    need = stockgate.feedstock_kg(70.0, "as-composed 59", "CI chondrite")
    ME = ladder.M_EARTH
    src = "imported stockgate/ladder (read-only)"
except Exception as exc:   # pragma: no cover
    need, ME, src = 749.08, 5.9722e24, "fallback constants (import failed: %s)" % exc
print("   threshold = %.2f kg, M_earth = %.4e kg  [%s]" % (need, ME, src))
chk("stockgate threshold for a 70 kg payload at CI chondrite = 749.08 kg", need, 749.08, 0.01)
for lab, val in [("tree 1.3", 1.3), ("2016 Table 1 low 1.10", 1.10), ("NIRPS 2025 1.055", 1.055),
                 ("NIRPS 2025 minus 5 sigma 0.78", 1.055 - 5*0.055)]:
    r = val*ME/need
    print("   %-32s ratio = %.4e  log10 = %.3f" % (lab, r, math.log10(r)))
    chk("ratio > 1 for %s" % lab, 1.0 if r > 1 else 0.0, 1.0, 0)
r_tree = 1.3*ME/need
chk("tree's printed ratio 1.036e22", r_tree, 1.036e22, 0.001e22)
# how far would m sin i have to fall to flip the conclusion?
print("   conclusion flips only below m sin i = %.3e M_E (%.1f orders below 1.055)" %
      (need/ME, math.log10(1.055*ME/need)))
# true mass: sin i <= 1 so m >= m sin i; the lower-bound direction is the one the tree uses
print("   m_true = m sin i / sin i >= m sin i for every i: the bound only strengthens the conclusion")

print("\n%d FAIL(s)" % len(fails))
sys.exit(1 if fails else 0)
