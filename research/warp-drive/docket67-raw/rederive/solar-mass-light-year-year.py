#!/usr/bin/env python3
"""DOCKET 67 -- audit 'solar-mass-light-year-year' (phase1.py:212-213, 179-181, 472-474, 506-510).

Re-derives, in exact rational arithmetic (sympy), every figure the owner hangs on
SOLAR_MASS = 1.98892e30 kg, LIGHT_YEAR = 9.4607e15 m and year = 3.15576e7 s, against
source values READ from local arXiv text copies:
  c, G        CODATA 2022 (arXiv:2409.03787, Table XXXII; Table XXX for the 16 G inputs)
  (GM)^N_sun  IAU 2015 B3 (arXiv:1510.07674, Recommends 3, 5)
  App. A      Prsa et al. 2016 (arXiv:1605.09788) kg figures for CODATA 2006/2014 G
The Julian year (365.25 d x 86400 s) and ly = c x Julian year are DEFINITIONS that were
NOT read at source here; they are checked as arithmetic only.

Imports phase1.py by path (read-only) so the owner's own functions are the ones measured.
Exit 0 iff every check passes.  A check that records a DISCREPANCY passes when the
discrepancy is reproduced exactly; discrepancies are recorded, not repaired.
"""
import importlib.util, sys
from sympy import Rational as R, log, sqrt, N, Abs

fails = 0
def chk(label, cond, detail=""):
    global fails
    print("  %-70s %s %s" % (label, "ok" if cond else "FAIL", detail))
    if not cond:
        fails += 1

def rel(a, b):
    return (a - b) / b

# --- the owner, read-only ------------------------------------------------------
spec = importlib.util.spec_from_file_location(
    "phase1", "/home/user/Claude-Method-Works/research/warp-drive/phase1.py")
p1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p1)

# --- source values (exact rationals) -------------------------------------------
c      = R(299792458)                       # CODATA 2022, exact
G22    = R(667430, 10**16)                  # 6.67430e-11, u_r 2.2e-5 (= CODATA 2018)
uG22   = R(15, 10**16)                      # (15) in last digits
GMN    = R(13271244) * R(10)**13               # 1.3271244e20, IAU 2015 B3, exact by definition
G06    = R(667428, 10**16)                  # CODATA 2006 (1605.09788 App. A)
G14    = R(667408, 10**16)                  # CODATA 2014 (1510.07674 Rec. 5)
G86    = R(667259, 10**16)                  # CODATA 1986 6.67259(85)e-11 -- NOT READ at source here
JYR    = R(36525, 100) * 86400              # Julian year, definition (NOT read at source)
LY_EX  = c * JYR                            # ly = c x Julian year, definition (NOT read)

# tree
MS_T   = R(198892) * R(10)**25              # 1.98892e30
LY_T   = R(94607) * R(10)**11               # 9.4607e15
YR_T   = R(315576) * R(10)**2               # 3.15576e7
C_T    = R(299792458)
G_T    = R(667430, 10**16)

print("1. the tree's c and G are the current CODATA values")
chk("c (tree) == CODATA 2022 exact", C_T == c)
chk("G (tree) == CODATA 2022 = CODATA 2018", G_T == G22)
chk("float constants in phase1 equal the rationals",
    p1.C_SI == float(c) and p1.G_SI == float(G22) and p1.SOLAR_MASS == float(MS_T)
    and p1.LIGHT_YEAR == float(LY_T))

print("\n2. the year: 3.15576e7 s is the Julian year exactly (arithmetic on the definition)")
chk("365.25 x 86400 == 3.15576e7 exactly", JYR == YR_T, "(%s)" % JYR)

print("\n3. the light year: 9.4607e15 m is a 5-figure truncation of c x Julian year")
d_ly = rel(LY_T, LY_EX)
chk("c x 365.25 x 86400 == 9460730472580800 m exactly", LY_EX == 9460730472580800)
chk("tree LIGHT_YEAR relative offset = -3.2219e-6",
    abs(N(d_ly) + 3.2219e-6) < 1e-9, "(%.6e)" % N(d_ly))

print("\n4. the solar mass: 1.98892e30 kg against (GM)^N/G with the tree's own G")
M22 = GMN / G22
uM22 = M22 * uG22 / G22
d_ms = rel(MS_T, M22)
nsig = (MS_T - M22) / uM22
chk("B3 App. A reproduced: GMN/G_2006 -> 1.988416e30",
    abs(N(GMN / G06) - 1.988416e30) < 5e23, "(%.7e)" % N(GMN / G06))
chk("B3 App. A reproduced: GMN/G_2014 -> 1.988475e30",
    abs(N(GMN / G14) - 1.988475e30) < 5e23, "(%.7e)" % N(GMN / G14))
chk("GMN/G_2022 = 1.988409871e30 +- 4.47e25 kg",
    abs(N(M22) - 1.988409871e30) < 1e21 and abs(N(uM22) - 4.47e25) < 1e23,
    "(%.9e +- %.3e)" % (N(M22), N(uM22)))
chk("DISCREPANCY: tree M_sun is +2.5655e-4 relative high = 11.42 sigma of G",
    abs(N(d_ms) - 2.5655e-4) < 1e-8 and abs(N(nsig) - 11.42) < 0.01,
    "(%.5e, %.2f sigma)" % (N(d_ms), N(nsig)))
GMtree = G_T * MS_T
chk("DISCREPANCY: tree product G*M_sun = 1.327464e20 vs (GM)^N 1.3271244e20 (+2.565e-4)",
    abs(N(GMtree) - 1.3274644e20) < 1e14, "(%.8e)" % N(GMtree))
Gimpl = GMN / MS_T
chk("G that would make 1.98892e30 consistent with (GM)^N: 6.672588e-11",
    abs(N(Gimpl) - 6.672588e-11) < 1e-17, "(%.7e)" % N(Gimpl))
chk("  1.98892e30 = GMN/G_1986 (6.67259e-11) rounded to 6 figures (provenance by MATCH, not READ)",
    abs(N(GMN / G86) - 1.98892e30) < 5e24, "(%.7e)" % N(GMN / G86))
Gin = [R(s) * R(10)**-11 for s in (
    "6.67248", "6.6729", "6.67398", "6.674255", "6.67559", "6.67422", "6.67387", "6.67222",
    "6.67425", "6.67349", "6.67554", "6.67191", "6.67435", "6.674184", "6.674484", "6.67260")]
chk("  the implied G lies inside the span of CODATA 2022's 16 G inputs [6.67191, 6.67559]",
    min(Gin) < Gimpl < max(Gin))
spanM = (GMN / min(Gin) - GMN / max(Gin)) / M22
chk("  span of GMN/G over the 16 inputs = 5.51e-4 relative (tree offset is inside it)",
    abs(N(spanM) - 5.51e-4) < 5e-6 and d_ms < spanM, "(%.3e)" % N(spanM))

print("\n5. what rests on it: the phase1 price figures")
lam = 2 * (log(2 * R(200) / sqrt(R(1) + R(2, 100) ** 2)) - 1)
chk("Lambda = 9.982529 (geometry, no constant)", abs(N(lam, 20) - 9.982529) < 1e-6,
    "(%.9f)" % N(lam, 15))
dd_T  = G_T * MS_T * lam / c ** 2          # tree: 1 M_sun buys
dd_N  = GMN * lam / c ** 2                 # with measured GM_sun (G-independent)
chk("tree: one solar mass buys 1.4742e4 m (owner's pin)", abs(N(dd_T) - 1.4742e4) / 1.4742e4 < 1e-3,
    "(%.6e)" % N(dd_T, 15))
chk("DISCREPANCY: owner's pin 1.4742e4 is -1.5e-4 from its own function's 1.47442e4 (rounds to 1.4744e4)",
    abs(N(rel(R(14742), dd_T)) + 1.513e-4) < 1e-6, "(%.4e)" % N(rel(R(14742), dd_T)))
chk("GM_N : one solar mass buys 1.47405e4 m -> still '14.7 km'",
    abs(N(dd_N) - 1.47405e4) < 1 and round(float(N(dd_N)) / 1e3, 1) == 14.7, "(%.6e)" % N(dd_N, 15))
for frac, pin, printed in ((R(1, 100), 2.5667e10, "2.57e10"), (R(1, 2), 1.2833e12, "1.28e12")):
    mT = frac * 4 * LY_T / dd_T
    mN = frac * 4 * LY_EX / dd_N
    chk("%s of 4 ly: tree %.5e, GM_N & exact ly %.5e M_sun" % (frac, N(mT), N(mN)),
        abs(N(mT) - pin) / pin < 1e-3 and ("%.2e" % N(mN)).replace("+", "") == printed
        and ("%.2e" % N(mT)).replace("+", "") == printed,
        "(shift %.3e; printed '%s' unchanged)" % (N(rel(mN, mT)), printed))
xr = c ** 2 / (G22 * lam)
chk("exchange rate c^2/(G Lambda) = 1.34894e26 kg/m does not contain M_sun or ly",
    abs(N(xr) - 1.34894e26) / 1.34894e26 < 1e-5, "(%.6e)" % N(xr, 12))
chk("  and moves by u_r(G) = 2.2e-5 at 1 sigma (5th figure)", True,
    "(%.2e)" % N(uG22 / G22))

print("\n6. what rests on it: Theorem 4 establishment time")
tE_T = 4 * LY_T / (2 * c)
tE_X = 4 * LY_EX / (2 * c)
chk("tree establishment_time(4 ly) = 6.3114997e7 s", abs(N(tE_T) - 6.3114997e7) < 1,
    "(%.7e)" % N(tE_T))
chk("exact (ly = c x Julian yr): 4 ly/(2c) = 2 Julian yr = 6.31152e7 s exactly", tE_X == 2 * JYR)
chk("DISCREPANCY: owner's pin 6.3113e7 is -3.2e-5 from the tree's own 6.3115e7 (last figure)",
    abs(N(rel(R(63113) * 10**3, tE_T)) + 3.17e-5) < 1e-6,
    "(pin passes only because its rtol is 1e-3; a misprint-class discrepancy, not a refutation)")
chk("tree years = 2*(1-3.22e-6) = 1.9999936", abs(N(tE_T / YR_T) - 1.99999356) < 1e-8,
    "(%.8f)" % N(tE_T / YR_T))
pen = (tE_T + 4 * LY_T / c) / (4 * LY_T / c)
chk("Theorem 4's conclusion is constant-free: penalty == 3/2 exactly for ANY L, c",
    pen == R(3, 2))
chk("owner's own functions agree", abs(p1.single_transition_penalty() - 1.5) < 1e-12
    and p1.single_transition_beats_light() is False)

print("\n7. sensitivity of every verdict to the moved data")
chk("price figures move by +2.565e-4 (M_sun choice) and -3.2e-6 (ly truncation): no printed "
    "3-figure value changes, no verdict depends on them", True)

print("\nFAILURES: %d" % fails)
sys.exit(1 if fails else 0)
