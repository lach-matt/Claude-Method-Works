#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of GKLM (Greene, Kabat, Levin, Menon, arXiv:2206.13590v2)
eq. (38), Delta c / c = gamma - 1, and of what branelink.py builds on it.

Source text: alphaXiv page text of 2206.13590v2 (all 20 pages), cached from an
earlier alphaXiv read in this session's transcript and saved at
../src/2206.13590.cached.txt (md5 2d15fd1497e73b10f4c703a95d6b85ca).  The GW170817
bound is Abbott et al. arXiv:1710.05834v2 Sec. 4.1 (../src/1710.05834.cached.txt);
the boosted-observer speeds are GKLP arXiv:2208.09014v3 eqs. (20), (22), (25)
(../src/2208.09014.cached.txt); the tilt formula is Polychronakos arXiv:2210.11497v3
eq. (5.3) (../src/2210.11497.cached.txt).

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  C1  GKLM eq. (16) == eq. (17) identically (image-charge hyperboloids on the brane)
  C2  envelope: max over continuous w of eq. (17) is (gamma t')^2 -> |x'| = gamma t'
      (eq. 6/14); integer-w deficit bounded by (pi R)^2; size at GW170817 distances
  C3  GKLM eq. (36) derived from a preferred-frame KK plane wave restricted to the
      moving brane; n = 0, m = 0 zero mode has omega' = gamma |k'| EXACTLY, so
      Delta c/c = gamma - 1 holds at every frequency for the massless zero mode;
      n != 0 or m != 0 group velocity (eq. 37) < gamma
  C4  inversion gamma = 1 + d -> beta = sqrt(d(2+d))/(1+d) (exact), 50-digit value at
      d = 7e-16 vs branelink O7_FIXTURES; the double-precision control
  C5  the 7e-16 / -3e-15 arithmetic of 1710.05834 (1.74 s, 26 Mpc, 10 s window)
  C6  data sensitivity: beta and Proxima saving at the bound's alternatives
  C7  GKLP eqs. (20),(22),(25): the B-dependence of what GW170817 bounds;
      exact d(eps, B) at forward/backward extremes; B at the tree's own values
  C8  Polychronakos eq. (5.3): alpha = 0 reduces to gamma - 1 at O(beta^2);
      tilt-like case has a direction with c_phi = 1 (single-event bound evaded)
"""
import sys
from decimal import Decimal, getcontext
import sympy as sp

FAILS = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- constants
C = Decimal(299792458)                       # m/s, exact
MPC = Decimal("3.0856775814913673e22")      # m (IAU 2015 pc x 1e6)
YR = Decimal(31557600)                       # Julian year, s
L_PROXIMA = Decimal("4.017499195181437e16")  # branelink.L_PROXIMA (foliation), m
getcontext().prec = 50

# ---------------------------------------------------------------- C1
t, R, beta, w = sp.symbols("t R beta w", real=True)
g = 1 / sp.sqrt(1 - beta ** 2)
zw = g * 2 * sp.pi * R * w                 # eq. (9)
eq16 = (t + beta * zw) ** 2 - zw ** 2       # eq. (16): |x'|^2
eq17 = (g * t) ** 2 - (g * beta * t - 2 * sp.pi * R * w) ** 2   # eq. (17)
chk("C1 eq.(16) == eq.(17)", sp.simplify(eq16 - eq17) == 0)

# ---------------------------------------------------------------- C2
wstar = sp.solve(sp.diff(eq17, w), w)[0]
chk("C2a stationary w* = gamma beta t/(2 pi R)", sp.simplify(wstar - g * beta * t / (2 * sp.pi * R)) == 0)
chk("C2b max_w eq.(17) = (gamma t')^2  => |x'| = gamma t' (eq. 14 / bound 6)",
    sp.simplify(eq17.subs(w, wstar) - (g * t) ** 2) == 0)
dl = sp.symbols("delta", real=True)
defic = sp.expand(sp.simplify(eq17.subs(w, wstar + dl) - (g * t) ** 2))
chk("C2c integer-w deficit = -(2 pi R delta)^2, |delta| <= 1/2 -> >= -(pi R)^2",
    sp.simplify(defic + (2 * sp.pi * R * dl) ** 2) == 0)
# fractional speed deficit at GW170817: 1 - sqrt(1 - (pi R/(gamma t'))^2) ~ (pi R)^2/(2 gamma^2 t'^2)
for Rm in (Decimal("38.6e-6"), Decimal("1e-3")):
    tprime = Decimal(26) * MPC               # metres (c = 1 units)
    frac = (Decimal(str(sp.pi.evalf(30))) * Rm) ** 2 / (2 * tprime ** 2)
    print("     R = %s m, D = 26 Mpc: fractional front-speed deficit <= %.3e" % (Rm, frac))
chk("C2d deficit negligible vs 7e-16 for R <= 1 mm", frac < Decimal("1e-40"))

# ---------------------------------------------------------------- C3
k, m, n, tp, xp = sp.symbols("k m n tprime xprime", real=True)
om = sp.sqrt(k ** 2 + m ** 2 + (n / R) ** 2)
# preferred-frame phase k x + (n/R) z - omega t on the brane z' = 0:
#   t = gamma t', z = gamma beta t', x = x'   (eq. 2 inverse with z' = 0)
phase = k * xp + (n / R) * g * beta * tp - om * g * tp
omega_p = -sp.diff(phase, tp)
chk("C3a eq.(36): omega' = gamma sqrt(k^2+m^2+(n/R)^2) - gamma beta n/R",
    sp.simplify(omega_p - (g * om - g * beta * n / R)) == 0)
vg = sp.diff(omega_p, k)
chk("C3b eq.(37): v_g = gamma k / sqrt(k^2+m^2+(n/R)^2)", sp.simplify(vg - g * k / om) == 0)
vg0 = sp.simplify(vg.subs({m: 0, n: 0}).subs(k, sp.Symbol("kk", positive=True)))
chk("C3c massless zero mode: v_g = gamma at EVERY k (eq. 38 exact for n = m = 0)",
    sp.simplify(vg0 - g) == 0, "v_g = %s" % vg0)
kp = sp.Symbol("kp", positive=True)
ratio = sp.simplify((vg / g).subs(k, kp).subs({m: 0, n: 1}))
chk("C3d n = 1 KK mode: v_g/gamma = k/sqrt(k^2+1/R^2) < 1 at finite k",
    sp.simplify(ratio - kp / sp.sqrt(kp ** 2 + 1 / R ** 2)) == 0)

# ---------------------------------------------------------------- C4
d = sp.symbols("d", positive=True)
bexpr = sp.sqrt(d * (2 + d)) / (1 + d)
chk("C4a gamma(bexpr) = 1 + d exactly", sp.simplify(1 / sp.sqrt(1 - bexpr ** 2) - (1 + d)) == 0)
D7 = Decimal("7e-16")


def beta_of(dd):
    return (dd * (2 + dd)).sqrt() / (1 + dd)


def saving_ns(dd, span=L_PROXIMA):
    T = span / C
    return T * dd / (1 + dd) * Decimal(10) ** 9


b7 = beta_of(D7)
print("     beta(7e-16) = %s" % b7)
chk("C4b beta(7e-16) = 3.74165738677e-08 (branelink O7_FIXTURES)", ("%.11e" % b7) == "3.74165738677e-08")
chk("C4c 1/beta = 26726124.1912", ("%.4f" % (1 / b7)) == "26726124.1912")
s7 = saving_ns(D7)
chk("C4d Proxima saving at d = 7e-16 = 93.80654 ns", ("%.5f" % s7) == "93.80654", "%.10f ns" % s7)
import math
bd = math.sqrt(1.0 - 1.0 / (1.0 + 7e-16) ** 2)
chk("C4e double-precision control beta = 3.650024e-08 (tree's withdrawn figure)",
    ("%.6e" % bd) == "3.650024e-08", "%.6e" % bd)

# ---------------------------------------------------------------- C5
T26 = Decimal(26) * MPC / C
up = Decimal("1.74") / T26
up_hi = Decimal("1.79") / T26
lo = (Decimal("1.74") - Decimal(10)) / T26
print("     1.74 s over 26 Mpc: +%.4e ; 1.79 s: +%.4e ; (1.74-10) s: %.4e" % (up, up_hi, lo))
chk("C5a upper bound 1.74 s * c / 26 Mpc = 6.50e-16 <= printed 7e-16", up < D7 and ("%.2e" % up) == "6.50e-16")
chk("C5b lower bound (1.74 - 10) s * c / 26 Mpc = -3.09e-15 ~ printed -3e-15", ("%.2e" % lo) == "-3.09e-15")

# ---------------------------------------------------------------- C6
alts = [
    ("printed bound 7e-16 (tree)", D7),
    ("exact 1.74 s / 26 Mpc", up),
    ("1.74 s / 40.7 Mpc (Cantiello+2018 SBF distance, NAMED-NOT-READ)", Decimal("1.74") / (Decimal("40.7") * MPC / C)),
    ("1.74 s / 40 Mpc (manyc.GW170817_DISTANCE_MPC)", Decimal("1.74") / (Decimal(40) * MPC / C)),
    ("photons up to 100 s BEFORE the GW peak (1710.05834 exotic window)", Decimal("101.74") / T26),
]
for name, dd in alts:
    print("     %-68s d = %.4e  beta = %.4e  saving = %.4f ns" % (name, dd, beta_of(dd), saving_ns(dd)))
chk("C6a a later (larger) distance TIGHTENS the bound: tree's beta, saving remain valid upper bounds",
    beta_of(alts[2][1]) < b7 and saving_ns(alts[2][1]) < s7)
chk("C6b the exotic emission window LOOSENS it by ~54x in d, ~7.4x in beta",
    abs(alts[4][1] / D7 - Decimal("54.3")) < 1 and abs(beta_of(alts[4][1]) / b7 - Decimal("7.37")) < Decimal("0.05"))

# ---------------------------------------------------------------- C7
B, G_, cth, eps = sp.symbols("B Gamma costh epsilon", positive=True)
Gm = 1 / sp.sqrt(1 - B ** 2)
v20 = g * (1 + Gm ** 2 * B ** 2 * beta ** 2) / (1 - Gm ** 2 * B * g * beta ** 2)
v25 = -g * (1 + Gm ** 2 * B ** 2 * beta ** 2) / (1 + Gm ** 2 * B * g * beta ** 2)
v22 = (g * cth - B) / (1 - B * g * cth)
okf = sp.simplify(sp.together(v20 - v22.subs(cth, 1))) == 0
okb = sp.simplify(sp.together(v25 - v22.subs(cth, -1))) == 0
if not (okf and okb):   # numeric fallback at rational points
    pts = [(sp.Rational(3, 5), sp.Rational(2, 5)), (sp.Rational(1, 10), sp.Rational(7, 10))]
    okf = all(abs(sp.N((v20 - v22.subs(cth, 1)).subs({beta: a, B: b}), 30)) < 1e-25 for a, b in pts)
    okb = all(abs(sp.N((v25 - v22.subs(cth, -1)).subs({beta: a, B: b}), 30)) < 1e-25 for a, b in pts)
chk("C7a GKLP eq.(20) == eq.(22) at cos = +1", okf)
chk("C7b GKLP eq.(25) == eq.(22) at cos = -1", okb)
chk("C7c B = 0: eq.(22) speed = gamma in every direction (GKLM eq. 38 is the B = 0 case)",
    sp.simplify(v22.subs(B, 0).subs(cth, 1) - g) == 0 and sp.simplify(-v22.subs(B, 0).subs(cth, -1) - g) == 0)
gam = sp.symbols("gamma", positive=True)
fwd = sp.solve(sp.Eq((gam - B) / (1 - B * gam) - 1, eps), gam)[0] - 1
bwd = sp.solve(sp.Eq((gam + B) / (1 + B * gam) - 1, eps), gam)[0] - 1
chk("C7d forward-propagating GW: gamma - 1 = eps (1-B)/(1+B+B eps)",
    sp.simplify(fwd - eps * (1 - B) / (1 + B + B * eps)) == 0)
chk("C7e backward-propagating GW: gamma - 1 = eps (1+B)/(1-B-B eps)",
    sp.simplify(bwd - eps * (1 + B) / (1 - B - B * eps)) == 0)
Gcmb = Decimal("1") + Decimal("7.6161e-07")     # branelink CMB_GAMMA_MINUS_1
Bcmb = (1 - 1 / Gcmb ** 2).sqrt()
for name, Bv in (("B = 0", Decimal(0)), ("B = CMB-dipole value (Gamma-1 = 7.6161e-7)", Bcmb),
                 ("B = 0.999387630 (branelink one-second escape)", Decimal("0.999387630"))):
    df = D7 * (1 - Bv) / (1 + Bv + Bv * D7)
    db = D7 * (1 + Bv) / (1 - Bv - Bv * D7)
    print("     %-48s d in [%.4e, %.4e]  beta in [%.4e, %.4e]" % (name, df, db, beta_of(df), beta_of(db)))
    if Bv == Decimal("0.999387630"):
        bmax_esc = beta_of(db)
chk("C7f at the tree's own escape B the backward-held beta is ~57x BETA_MAX (bound is B = 0-conditional)",
    Decimal(50) < bmax_esc / b7 < Decimal(60), "ratio %.2f" % (bmax_esc / b7))

# ---------------------------------------------------------------- C8
al, ph = sp.symbols("alpha phi", real=True)
cphi = 1 + sp.Rational(1, 2) * (al * sp.cos(ph) + beta) ** 2         # 2210.11497 eq. (5.3)
gser = sp.series(g - 1, beta, 0, 3).removeO()
chk("C8a alpha = 0: c_phi - 1 = beta^2/2 = gamma - 1 + O(beta^4)", sp.simplify(cphi.subs(al, 0) - 1 - gser) == 0)
chk("C8b tilt-like |beta| < alpha: cos phi_o = -beta/alpha gives c_phi = 1 (no single-event bound)",
    sp.simplify(cphi.subs(sp.cos(ph), -beta / al) - 1) == 0)

print()
print("FAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
