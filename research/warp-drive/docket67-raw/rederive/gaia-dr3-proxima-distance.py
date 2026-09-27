#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'gaia-dr3-proxima-distance'.

Reads the tree's constants READ-ONLY by regex (no import, so no __pycache__
is written under research/warp-drive), then:
  1. inverts the Gaia EDR3=DR3 parallax of Proxima (as READ in Reyle et al.
     2021, arXiv:2104.14972, Table 1: 768.066539187357 +- 0.049872905 mas,
     bibcode 2020yCat.1350 = Gaia EDR3; DR3 astrometry = EDR3 astrometry per
     Gaia Collaboration, Vallenari et al. 2022, arXiv:2208.00211 Sec. 3) with
     exact IAU units (sympy rationals), and checks the tree's 4.2465 ly;
  2. propagates the formal parallax error;
  3. evaluates the Lindegren et al. 2021 (arXiv:2012.01742) zero-point Z5/Z6
     at Proxima's G, colour and ecliptic latitude, from Table 9 / Table 10 and
     Appendix A as READ -- Proxima lies OUTSIDE the recipe's validity range
     (nu_eff < 1.24), so this is an ILLUSTRATIVE bracket, not a correction;
  4. compares Gaia DR2 (Kervella+2020, arXiv:2003.13106, corrected
     768.529 +- 0.220) and HST (Libralato+2025, arXiv:2512.08533,
     768.373 +0.194/-0.162; chromatic fit 768.240 +0.180/-0.267);
  5. recomputes every downstream figure the tree prints from PROXIMA_LY and
     measures how far each moves under the moved/contested parallax data.
Exit 0 if every check passes.
"""
import math
import re
import sys
from pathlib import Path

import sympy as sp

TREE = Path("/home/user/Claude-Method-Works/research/warp-drive")
fails = []


def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (("  -- " + detail) if detail else ""))
    if not ok:
        fails.append(label)


def grab(fname, pattern):
    txt = (TREE / fname).read_text()
    m = re.search(pattern, txt, re.M)
    if not m:
        raise SystemExit("pattern not found in %s: %s" % (fname, pattern))
    return m.group(1)


# ------------------------------------------------------------- tree constants
PROX_FOL = float(grab("foliation.py", r"^PROXIMA_LY\s*=\s*([0-9.eE+-]+)"))
PROX_NS = float(grab("nonstatic.py", r"^PROXIMA_LY\s*=\s*([0-9.eE+-]+)"))
LY_FOL = float(grab("foliation.py", r"^LY\s*=\s*([0-9.eE+-]+)"))
LY_LED = float(grab("ledger.py", r"^LY_M\s*=\s*([0-9.eE+-]+)"))
C = float(grab("foliation.py", r"^C_LIGHT\s*=\s*([0-9.eE+-]+)"))
G = float(grab("foliation.py", r"^G_NEWTON\s*=\s*([0-9.eE+-]+)"))
MSUN = float(grab("foliation.py", r"^M_SUN\s*=\s*([0-9.eE+-]+)"))
LAMBDA = float(grab("overturn.py", r"^LAMBDA\s*=\s*([0-9.eE+-]+)"))
YR = float(grab("manyc.py", r"^YR\s*=\s*([0-9.eE+-]+)"))
print("tree: PROXIMA_LY foliation=%r nonstatic=%r  LY=%r ledger LY_M=%r  YR=%r"
      % (PROX_FOL, PROX_NS, LY_FOL, LY_LED, YR))
chk("foliation and nonstatic carry the same PROXIMA_LY", PROX_FOL == PROX_NS)

# ------------------------------------------------------- exact IAU units (sympy)
c_ex = sp.Integer(299792458)                 # m/s, SI definition
jyr = sp.Integer(36525) * 864                # Julian year, s  (365.25 d x 86400 s)
ly_ex = c_ex * jyr                           # IAU light year, exact
au_ex = sp.Integer(149597870700)             # IAU 2012 B2, exact
pc_ex = au_ex * 648000 / sp.pi               # IAU 2015 B2, exact
chk("tree LY = c x Julian year exactly", sp.Integer(int(LY_FOL)) == ly_ex and LY_FOL == LY_LED,
    "c*365.25*86400 = %s m" % ly_ex)
chk("manyc.YR = Julian year", YR == float(jyr))
pc_per_ly = sp.N(pc_ex / ly_ex, 30)
print("pc / ly = %s" % pc_per_ly)


def dist_ly(plx_mas):
    """1/parallax, exact units; returns float ly."""
    return float(sp.N(sp.Rational(1000) / sp.nsimplify(plx_mas, rational=True) * pc_ex / ly_ex, 20))


# ------------------------------------------------------ 1. the DR3 inversion
PLX = 768.066539187357          # mas, Gaia EDR3 = DR3 (READ via Reyle+2021 Table 1)
SIG = 0.049872905               # mas
d3 = dist_ly(PLX)
d3_pc = 1000.0 / PLX
print("\nGaia DR3: plx = %.9f +- %.9f mas -> %.9f pc = %.9f ly" % (PLX, SIG, d3_pc, d3))
chk("1/plx rounds to the tree's 4.2465 ly at 5 s.f.", round(d3, 4) == PROX_FOL,
    "computed %.7f ly, residual %.2e ly" % (d3, d3 - PROX_FOL))
rel_sig = SIG / PLX
sig_ly = d3 * rel_sig
print("formal: sigma_d/d = %.3e  -> sigma_d = %.6f ly  (%.3e m)" % (rel_sig, sig_ly, sig_ly * LY_FOL))
# which rounded values the 1-sigma interval admits
lo, hi = dist_ly(PLX + SIG), dist_ly(PLX - SIG)
chk("the 1-sigma interval spans more than one 5th-digit value", round(lo, 4) != round(hi, 4),
    "[%.5f, %.5f] ly" % (lo, hi))
# Lutz-Kelker / prior-free inversion is safe at fractional error 6.5e-5
chk("fractional parallax error < 1e-3 (inversion bias ~ (sig/plx)^2 negligible)", rel_sig < 1e-3,
    "bias ~ %.1e" % (rel_sig ** 2))

# ------------------------------------------ 3. Lindegren+2021 zero point (illustrative)
Gmag, BP, RP = 8.984749, 11.373116, 7.5685353      # Reyle+2021 Table 1 (Gaia EDR3)
ra, dec = math.radians(217.392321472009), math.radians(-62.6760751167667)
bprp = BP - RP
nu = 1.76 - (1.61 / math.pi) * math.atan(0.531 * bprp)      # L21 Eq. (1), valid -0.5..7
sinb = 0.9174820621 * math.sin(dec) - 0.3977771559 * math.cos(dec) * math.sin(ra)  # L21 Eq. (3)
print("\nProxima: G=%.4f  BP-RP=%.4f  nu_eff(Eq.1)=%.4f um^-1  sin(beta)=%.4f  beta=%.2f deg"
      % (Gmag, bprp, nu, sinb, math.degrees(math.asin(sinb))))
chk("Proxima's colour lies OUTSIDE the L21 validity interval 1.24 < nu_eff < 1.72", nu < 1.24)


def c_basis(n):
    c1 = -0.24 if n <= 1.24 else (n - 1.48 if n <= 1.72 else 0.24)
    c2 = 0.24 ** 3 if n <= 1.24 else ((1.48 - n) ** 3 if n <= 1.48 else 0.0)
    c3 = (n - 1.24) if n <= 1.24 else 0.0
    c4 = (n - 1.72) if n > 1.72 else 0.0
    return [1.0, c1, c2, c3, c4]


b = [1.0, sinb, sinb * sinb - 1.0 / 3.0]
# Table 9 (Z5) rows at G = 6.0 and 10.8: q00 q01 q02 q10 q11 q20 (q30,q40 are '-')
T9 = {6.0: dict(q00=-26.98, q01=-9.62, q02=27.40, q10=-25.1, q11=-0.0, q20=-1257),
      10.8: dict(q00=-27.23, q01=-3.07, q02=23.04, q10=35.3, q11=15.7, q20=-1257)}
# Table 10 (Z6) rows: q00 q01 q02 q10 q11 q12 q20
T10 = {6.0: dict(q00=-27.85, q01=-7.78, q02=27.47, q10=-32.1, q11=14.4, q12=9.5, q20=-67),
       10.8: dict(q00=-28.91, q01=-3.57, q02=22.92, q10=7.7, q11=12.6, q12=1.6, q20=-572)}


def interp(tab, g):
    w = (g - 6.0) / (10.8 - 6.0)
    return {k: (1 - w) * tab[6.0][k] + w * tab[10.8][k] for k in tab[6.0]}


def Z(tab, g, n):
    q = interp(tab, g)
    cb = c_basis(n)
    z = 0.0
    for key, val in q.items():
        j, k = int(key[1]), int(key[2])
        z += val * cb[j] * b[k]
    return z


z5 = Z(T9, Gmag, nu)
z6 = Z(T10, Gmag, nu)
print("L21 Z5 = %+.2f uas   Z6 = %+.2f uas   (both OUTSIDE validity: illustrative only)" % (z5, z6))
for name, z in (("Z5", z5), ("Z6", z6), ("global QSO median -17 uas", -17.0)):
    dc = dist_ly(PLX - z / 1000.0)
    print("  corrected by %-26s -> %.9f ly (shift %+.2e ly, %+.2e rel); 5 s.f. %.4f"
          % (name, dc, dc - d3, (dc - d3) / d3, round(dc, 4)))

# ------------------------------------------ 4. other releases / instruments
others = [("Gaia DR2 (Kervella+2020, +29 uas ZP applied)", 768.529, 0.220),
          ("HST WFC3 (Libralato+2025, Table 2)", 768.373, 0.178),
          ("HST WFC3 chromatic fit (Libralato+2025, Tab A.1)", 768.240, 0.224)]
print()
for name, p, s in others:
    d = dist_ly(p)
    z = (p - PLX) / math.hypot(s, SIG)
    print("%-50s plx %.3f +- %.3f -> %.5f ly  (vs DR3 %+.2e rel, %+.2f sigma)"
          % (name, p, s, d, (d - d3) / d3, z))
dDR2 = dist_ly(768.529)
chk("DR2 does NOT give 4.2465 (attribution to DR3 is discriminating)", round(dDR2, 4) != PROX_FOL,
    "DR2 -> %.4f ly" % dDR2)
chk("HST (Libralato+2025) agrees with DR3 within 2 sigma",
    abs(768.373 - PLX) / math.hypot(0.178, SIG) < 2.0)

# ------------------------------------------ geometry / epoch hypotheses
rv = -22.345e3          # m/s, Reyle+2021 Table 1 (Barnes+2014)
dt = (2026.74 - 2016.0) * float(jyr)
d_m = d3 * LY_FOL
print("\nepoch drift J2016.0 -> 2026.74: %.3e m = %.2e rel" % (rv * dt, rv * dt / d_m))
print("Earth-orbit (1 au) vs barycentric distance: %.2e rel" % (float(au_ex) / d_m))
chk("MEASURED: the 1-au origin offset is < formal sigma (heliocentric vs barycentric immaterial)",
    float(au_ex) / d_m < rel_sig)
chk("MEASURED: the epoch drift J2016.0 -> today EXCEEDS the formal sigma (epoch is load-bearing at the 5th digit)",
    abs(rv * dt / d_m) > rel_sig, "distance at 2026.74 = %.5f ly vs J2016.0 %.5f ly" % (d3 * (1 + rv * dt / d_m), d3))

# ------------------------------------------ 5. downstream figures from PROXIMA_LY
print("\nDOWNSTREAM (tree figures recomputed from PROXIMA_LY = %.4f)" % PROX_FOL)
R = PROX_FOL * LY_FOL
chk("span 4.017499195e16 m", abs(R / 4.017499195e16 - 1) < 1e-9, "%.10e" % R)
E = R * C * C / G / MSUN
chk("E = R c^2/G at dGamma=1 is 2.720744289e13 Msun", abs(E / 2.720744289e13 - 1) < 1e-9, "%.10e" % E)
chk("crossing at W=2 is 2.12325 yr", abs(R / (2 * C) / YR - 2.12325) < 1e-9)
band = 2 * 0.01 * R / (C * math.sqrt(3.0)) / 86400
chk("band time W=2, eps=0.01 is 17.909799392 d", abs(band / 17.909799392 - 1) < 1e-9, "%.9f" % band)
lt = R / C
chk("light time 134009348.4 s = 4.2465 Julian yr exactly (given the input)",
    abs(lt - 134009348.4) < 0.05 and abs(lt / YR - PROX_FOL) < 1e-12, "%.3f s" % lt)
xr = C * C / (G * LAMBDA)
chk("EXCHANGE_RATE c^2/(G Lambda) = 1.348948e26 kg/m", abs(xr / 1.348948e26 - 1) < 1e-6, "%.7e" % xr)
chk("B2 Proxima demand 5.4194e42 kg", abs(R * xr / 5.4194e42 - 1) < 1e-4, "%.5e" % (R * xr))

print("\nSENSITIVITY: every downstream figure above is LINEAR in R (orders_short is log10 R).")
moves = {"formal 1 sigma": rel_sig, "L21 Z5 (illustr.)": abs(dist_ly(PLX - z5 / 1000) / d3 - 1),
         "L21 Z6 (illustr.)": abs(dist_ly(PLX - z6 / 1000) / d3 - 1),
         "DR3 vs DR2": abs(dDR2 / d3 - 1), "DR3 vs HST": abs(dist_ly(768.373) / d3 - 1)}
for k, v in moves.items():
    print("  %-20s rel %.2e  -> span shift %.2e m; log10 shift %.2e orders; "
          "5.4194e42 -> %.5e; 2.720744289e13 -> %.9e"
          % (k, v, v * R, v / math.log(10), 5.4194e42 * (1 + v), E * (1 + v)))
worst = max(moves.values())
chk("no moved/contested datum shifts any order-of-magnitude figure (throatmass 48.92 at 2 dp)",
    worst / math.log(10) < 0.005, "worst log10 shift %.1e" % (worst / math.log(10)))
chk("but the tree's 10-significant-figure prints exceed the datum's precision",
    rel_sig > 1e-9, "physical precision ~%.0e rel vs printed 1e-9/1e-10" % rel_sig)
chk("MEASURED: the 5th figure of the demand 5.4194e42 kg is NOT fixed by the datum (1-sigma band crosses it)",
    round(5.4194e42 * (1 + rel_sig) / 1e38) != 54194 or round(5.4194e42 * (1 - rel_sig) / 1e38) != 54194,
    "1+sigma -> %.5e, 1-sigma -> %.5e" % (5.4194e42 * (1 + rel_sig), 5.4194e42 * (1 - rel_sig)))

print("\n%d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
