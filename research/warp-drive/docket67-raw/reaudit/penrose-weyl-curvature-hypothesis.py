#!/usr/bin/env python3
"""DOCKET 67 re-audit: penrose-weyl-curvature-hypothesis against Penrose, 'Singularities and time-asymmetry',
ch. 12 of Hawking & Israel (eds.) 1979, pp. 581-638, READ in full (58 pages, text + page images).

  P1  p.629-630 entropy-per-baryon figures vs the Bekenstein-Hawking formula printed on p.602
      (S = k A c^3 / 4 hbar G, i.e. S/k = 4 pi G M^2/(hbar c)):
        printed: M_sun hole 1e18; 1e10 M_sun galaxy with 1e6 M_sun core 1e20; whole galaxy in hole 1e28;
                 final state of a closed universe of 1e80 baryons ~1e40.
      Computed, and the ratio computed/printed reported.  (A finding about the source's arithmetic, not
      used by the owner: permute.py uses no number from Penrose.)
  P2  p.629-630 internal arithmetic: 1e9 / 1e40 = 1e-31 ('at most ~1e-31 of the available chaos').
  P3  p.614 Kantowski-Sachs ('cigar') scaling inside Schwarzschild: comoving volume ~ r^(3/2), so density
      and a typical Ricci component ~ r^(-3/2), against Weyl ~ M/r^3: Weyl/Ricci -> infinity as r -> 0.
  P4  p.614 'the magnitude of the Weyl curvature diverging as the inverse cube of the distance':
      Schwarzschild Weyl component M/r^3 (C_abcd C^abcd = 48 M^2/r^6, recomputed by the first audit, C2).
  P5  the gap between the radiation entropy and the maximal (black-hole) entropy, with Penrose's own
      printed inputs (1e9 per baryon, 1e80 baryons, 1e40 per baryon) and with the computed BH value.
Exit 0 iff all pass.
"""
import sys, math
import sympy as sp

ok = []
def chk(name, cond, extra=""):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name + (("   " + extra) if extra else ""))

G = 6.67430e-11; hbar = 1.054571817e-34; c = 2.99792458e8
Msun = 1.98892e30; mp = 1.67262192e-27     # nucleon mass as the baryon mass
def S_over_k(M): return 4*math.pi*G*M*M/(hbar*c)

cases = [
    ("M_sun hole",                        Msun,        Msun/mp,        1e18),
    ("1e6 M_sun core in 1e10 M_sun gal.", 1e6*Msun,    1e10*Msun/mp,   1e20),
    ("1e10 M_sun galaxy all in hole",     1e10*Msun,   1e10*Msun/mp,   1e28),
    ("1e80 baryons in one hole",          1e80*mp,     1e80,           1e40),
]
ratios = []
for name, M, N, printed in cases:
    per = S_over_k(M)/N
    ratios.append(per/printed)
    print("     %-36s computed %.2e per baryon, printed %.0e, ratio %.0f (%.2f dex)" % (name, per, printed, per/printed, math.log10(per/printed)))
chk("P1 three galactic figures are low by one common factor (~88, 1.94 dex)",
    max(ratios[:3])/min(ratios[:3]) < 1.01 and 80 < ratios[0] < 95)
chk("P1 the final ~1e40 is low by ~740 (2.87 dex): a further ~0.9 dex beyond the common factor",
    700 < ratios[3] < 780)
chk("P1 every printed figure is within 3 dex BELOW the BH formula (all order-of-magnitude underestimates)",
    all(0 < math.log10(x) < 3 for x in ratios))
chk("P1 the common factor is close to 8 pi^2 = 79 (formula with h for hbar and no 4 pi would give it)",
    abs(ratios[0]/(8*math.pi**2) - 1) < 0.15, "ratio/8pi^2 = %.3f" % (ratios[0]/(8*math.pi**2)))

chk("P2 1e9/1e40 = 1e-31", abs(math.log10(1e9/1e40) + 31) < 1e-12)

r, m = sp.symbols('r m', positive=True)
# inside r < 2m: ds^2 = -(2m/r - 1)^{-1} dr^2 + (2m/r - 1) dt^2 + r^2 dOmega^2 ; comoving volume along t, theta, phi
vol = sp.sqrt(2*m/r - 1)*r**2
lead = sp.limit(vol/r**sp.Rational(3, 2), r, 0)
chk("P3 comoving volume element ~ r^(3/2) near r = 0 (coefficient sqrt(2m))", sp.simplify(lead - sp.sqrt(2*m)) == 0)
ricci_like = r**sp.Rational(-3, 2); weyl = m/r**3
chk("P3 Weyl/Ricci ~ r^(-3/2) -> infinity: 'the Weyl tensor dominates near the singularity'",
    sp.limit(weyl/ricci_like, r, 0) == sp.oo)
chk("P4 C_abcd C^abcd = 48 m^2/r^6 = 48 (m/r^3)^2: component ~ inverse cube", sp.simplify(48*m**2/r**6 - 48*weyl**2) == 0)

S_rad = 1e9*1e80
S_max_printed = 1e40*1e80
S_max_bh = S_over_k(1e80*mp)
g1 = math.log10(S_max_printed/S_rad); g2 = math.log10(S_max_bh/S_rad)
chk("P5 gap radiation -> maximal entropy: 31 dex with Penrose's printed figures, 33.9 dex with the BH formula",
    abs(g1 - 31) < 1e-9 and 33.5 < g2 < 34.0, "printed %.1f dex, BH %.2f dex; S_max(BH) = %.2e" % (g1, g2, S_max_bh))

n = sum(ok); print("\n%d/%d PASS" % (n, len(ok)))
sys.exit(0 if n == len(ok) else 1)
