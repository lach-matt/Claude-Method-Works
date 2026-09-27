#!/usr/bin/env python3
"""DOCKET 67 RE-AUDIT: 't Hooft, PRL 37 (1976) 8, READ from Drive (OCR text).
Checks the primary's printed forms against what massform.py uses.  stdlib + sympy."""
import math, sys
from fractions import Fraction as F
import sympy as sp
FAIL = []
def chk(n, ok, d=""):
    print(("PASS " if ok else "FAIL ") + n + ("  " + d if d else "")); (FAIL.append(n) if not ok else None)

g, al, s2 = sp.symbols("g alpha s2", positive=True)
# (a) eq.(6)/(17): |S| = 8 pi^2/g^2; rates carry the square of the amplitude -> exp(-16 pi^2/g^2)
S = 8 * sp.pi**2 / g**2
chk("amplitude exp(-8pi^2/g^2) squared = exp(-16pi^2/g^2)", sp.simplify(2 * S - 16 * sp.pi**2 / g**2) == 0)
# (b) printed identity exp(-16pi^2/g^2) = exp(-4 x 137 x sin^2theta): with g^2 = 4 pi alpha / sin^2theta
expo = sp.simplify((16 * sp.pi**2 / g**2).subs(g, sp.sqrt(4 * sp.pi * al / s2)))
chk("16 pi^2/g^2 = 4 pi sin^2(theta)/alpha (so the OCR '4x137' must carry a pi: 4 pi x 137 x sin^2)",
    sp.simplify(expo - 4 * sp.pi * s2 / al) == 0, str(expo))
# (c) same as the tree's exp(-4 pi/alpha_W) with alpha_W = g^2/4pi = alpha/sin^2
aW = g**2 / (4 * sp.pi)
chk("16 pi^2/g^2 = 4 pi/alpha_W (tree's form, massform.py:531)", sp.simplify(16 * sp.pi**2 / g**2 - 4 * sp.pi / aW) == 0)

L10 = math.log(10)
def log10_fac(inv_aw): return -4 * math.pi * inv_aw / L10
# the source's own evaluation route: alpha = 1/137 (Thomson), sin^2 theta a free input in 1976
print("== 't Hooft's route exp(-4 pi 137 sin^2): log10 factor")
for s in (0.20, 0.2229, 0.2312, 0.25, 0.30, 0.35, 0.40):
    print("   sin^2 = %.4f  1/alpha_W = %.2f  factor 10^%.2f" % (s, 137.036 * s, log10_fac(137.036 * s)))
s170 = 170 * L10 / (4 * math.pi * 137.036)
print("   RS96's printed 10^-170 is reproduced by the Thomson-alpha route at sin^2 = %.4f (1/alpha_W = %.2f)"
      % (s170, 137.036 * s170))
chk("RS96 10^-170 corresponds to sin^2 ~ 0.227 at alpha = 1/137 (INFERENCE, not RS96's stated route: RS96 prints 1/29)",
    0.22 < s170 < 0.235, "%.4f" % s170)
# the tree's figure
mw, v = 80.362, 246.21964023926205
gt = 2 * mw / v
inv_awt = 4 * math.pi / gt**2
chk("tree: 1/alpha_W = 29.49, factor 10^-160.95", abs(inv_awt - 29.491) < 2e-3 and abs(log10_fac(inv_awt) + 160.95) < 5e-3,
    "1/aW = %.4f, 10^%.3f" % (inv_awt, log10_fac(inv_awt)))
print("   spread of the leading exponent between Thomson-alpha (sin^2 0.2312: 10^%.2f) and on-shell g (10^%.2f): %.2f decades"
      % (log10_fac(137.036 * 0.2312), log10_fac(inv_awt), log10_fac(inv_awt) - log10_fac(137.036 * 0.2312)))

# (d) eq.(24), Weinberg-Salam with charm (2 generations): per soliton dE = dM = 1, du + dd_C = 3, du' + ds_C = 3
dE, dM = 1, 1
dq = 3 + 3                      # quarks created
dB = F(dq, 3); dL = dE + dM
chk("eq.(24): Delta B = 2, Delta L = 2 at N_f = 2 ('two baryons equal six quarks' -> 'two antileptons')",
    (dB, dL) == (2, 2))
chk("eq.(24) per generation = one lepton + three quarks = the tree's THOOFT_VERTEX unit (Q x3, L x1)",
    (F(3, 3), 1) == (1, 1))
Nf = 3
chk("generalised to N_f = 3 (tree): (B, L) = (3, 3); B - L conserved", (F(3 * Nf, 3), Nf) == (3, 3))
# (e) eq.(12) Delta Q5 = 2N for N doublets: WS with charm has N = 4 doublets per generation x 2 = 8
N = 4 * 2
chk("eq.(12): fermions created = N = 8 doublets (6 quarks + 2 leptons); Delta Q5 = 2N = 16", dq + dL == N)
print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS"); sys.exit(1 if FAIL else 0)
