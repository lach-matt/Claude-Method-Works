#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 2309.05759-eqs76-77 (Kabat & Nomura eqs. 76-77 as branelink.py uses them).

The source PDF could NOT be read this stage (alphaXiv quota exhausted; arxiv.org, inspirehep.net,
journals.aps.org, link.springer.com all refused by the egress proxy).  The formula checked here is the
RESTATEMENT recorded by the DOCKET 62 O6/O7 pass (session task outputs wnvrkn658 / ww5njxx5t):
    c^{mu nu} = -(1/16 pi^2) (1/(pi r Mbar4)^2) (b^mu b^nu - eta^{mu nu} b^2/4) I_gravity      (76)
    I_gravity -> -zeta(3)/4  as mu r -> 0                                                       (77)
    boost-like case b^mu = (-beta,0,0,0), b^2 = beta^2, r = gamma R                             (84)
What is checkable WITHOUT the source: (a) the tensor factor 0.75 beta^2 the tree uses, (b) zeta(3),
(c) the tree's number 6.372e-64 and its 42 orders, from CODATA constants independently of higgs.py,
(d) the DIRECTION of the tree's inequality over the Eot-Wash-allowed region, (e) how large a change in
any unread factor (I_gravity at b^2 = 1, the mu r regime, the alpha = 2 Eot-Wash edge, beta branch)
would have to be to move the conclusion.  I_gravity itself is NOT re-derived: its integral is not read.
"""
import math
import sys

import sympy as sp
import mpmath as mp

ok = True


def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))


# (a) tensor factor, signature (+,-,-,-) -- the only one in which b^mu = (-beta,0,0,0) gives b^2 = +beta^2
beta = sp.symbols('beta', positive=True)
eta = sp.diag(1, -1, -1, -1)
b_up = sp.Matrix([-beta, 0, 0, 0])
b2 = sp.simplify((b_up.T * eta * b_up)[0])
etainv = eta.inv()
T = sp.simplify(b_up * b_up.T - etainv * b2 / 4)
chk("b^2 = +beta^2 in (+,-,-,-)", sp.simplify(b2 - beta ** 2) == 0, str(b2))
chk("T^{00} = 3 beta^2/4 (the tree's 0.75 beta^2)", sp.simplify(T[0, 0] - sp.Rational(3, 4) * beta ** 2) == 0, str(T[0, 0]))
chk("T^{ii} = beta^2/4, traceless: eta_{mu nu}T^{mu nu} = 0",
    sp.simplify(T[1, 1] - beta ** 2 / 4) == 0 and sp.simplify(sum(eta[i, i] * T[i, i] for i in range(4))) == 0)
eta_mp = sp.diag(-1, 1, 1, 1)
b2_mp = (b_up.T * eta_mp * b_up)[0]
chk("control: in (-,+,+,+) the same b^mu gives b^2 = -beta^2 (so the restated b^2 = beta^2 fixes the signature)",
    sp.simplify(b2_mp + beta ** 2) == 0)

# (b) zeta(3): the tree's series vs mpmath
def tree_zeta3(n=200000):
    return sum(1.0 / k ** 3 for k in range(1, n)) + 1.0 / (2 * n * n)
z3 = float(mp.zeta(3))
chk("tree zeta3 series vs mpmath zeta(3) to 1e-11 (float accumulation, ascending k, leaves ~1.4e-12)", abs(tree_zeta3() - z3) < 1e-11, "%.16f vs %.16f" % (tree_zeta3(), z3))
chk("zeta(3)/4 = 0.3005142...", abs(z3 / 4 - 0.30051422578989857) < 1e-15)

# (c) the number, from CODATA 2018 (= CODATA 2022 for G: 6.67430(15)e-11) independently of higgs.py
HBAR = 1.054571817e-34; C = 299792458.0; G = 6.67430e-11; E = 1.602176634e-19
GEV = E * 1e9
HBARC_GEV_M = HBAR * C / GEV
MBAR4 = math.sqrt(HBAR * C ** 5 / G) / GEV / math.sqrt(8 * math.pi)
R = 38.6e-6
def c_abs(beta=1.0, r=R, Irat=1.0, M4=MBAR4):
    rG = r / HBARC_GEV_M
    return (1 / (16 * math.pi ** 2)) / (math.pi * rG * M4) ** 2 * 0.75 * beta ** 2 * (z3 / 4) * Irat
cval = c_abs()
chk("|c_00| at r = 38.6 um, beta = 1 = 6.372e-64 (tree)", abs(cval / 6.372e-64 - 1) < 5e-4, "%.6e, Mbar4 = %.6e GeV" % (cval, MBAR4))
orders = math.log10(1e-21 / cval)
chk("orders short = 42 (tree rounds %.3f)" % orders, round(orders) == 42)
# G uncertainty 22 ppm -> |c| moves 22 ppm (|c| ~ G): nil
chk("G at +/- 1 sigma moves orders by < 1e-4", abs(math.log10(c_abs(M4=MBAR4 * math.sqrt(6.67430 / 6.67445))) - math.log10(cval)) < 1e-4)
# cross-check against the tree's own function (read-only import, nothing written)
try:
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import branelink
    chk("tree branelink.sme_coefficient() agrees with this independent evaluation",
        abs(branelink.sme_coefficient() / cval - 1) < 1e-9, "%.10e vs %.10e" % (branelink.sme_coefficient(), cval))
except Exception as ex:  # pragma: no cover
    print("NOTE could not import branelink: %r" % ex)
# prior pass's two quoted points (Mbar4 = 2.4e18): r = 1e-5 m -> 9.78e-63, r = 1e-19 m -> 9.78e-35
chk("prior pass's |c_00|(1e-5 m, Mbar4 2.4e18) = 9.78e-63 reproduces", abs(c_abs(r=1e-5, M4=2.4e18) / 9.78e-63 - 1) < 2e-3, "%.4e" % c_abs(r=1e-5, M4=2.4e18))

# (d) DIRECTION.  |c| ~ beta^2 / r^2.  Eot-Wash gives r <= 38.6 um (an UPPER bound on r), so over the
# allowed region |c| is bounded BELOW at fixed beta, not above: 6.37e-64 is the infimum over r at beta=1.
rs = sp.symbols('r', positive=True)
expr = beta ** 2 / rs ** 2
chk("d|c|/dr < 0: the maximal r gives the MINIMAL |c| at fixed beta", sp.simplify(sp.diff(expr, rs)) == -2 * beta ** 2 / rs ** 3)
r_bite_b1 = R * math.sqrt(cval / 1e-21)
print("INFO  r at which |c_00| = 1e-21 (beta = 1): %.4e m  (prior pass: 3.126645e-26 m at Mbar4 2.4e18 -> %.4e)"
      % (r_bite_b1, R * math.sqrt(c_abs(M4=2.4e18) / 1e-21)))
BETA_GW = 3.74165738677e-08
r_bite_bulk = r_bite_b1 * BETA_GW
print("INFO  same at beta = 3.74e-8 (bulk-graviton branch, GW170817): %.4e m; Planck length 1.616e-35 m" % r_bite_bulk)
print("INFO  |c_00| at r = 38.6 um, beta = 3.74e-8: %.4e  (%.1f orders short)" % (c_abs(beta=BETA_GW), math.log10(1e-21 / c_abs(beta=BETA_GW))))
chk("the '|c| <= 6.37e-64' holds as an upper bound over beta<=1 AT r = 38.6 um only (if |I(b^2)| <= zeta(3)/4); "
    "over the whole Eot-Wash-allowed r it is a lower bound", c_abs(r=R / 2) > cval and c_abs(beta=0.5) < cval)

# (e) what an unread factor would have to be to move the conclusion
print("INFO  factor on |c| needed to reach 1e-21 at r = 38.6 um: %.3e" % (1e-21 / cval))
me = 0.51099895e-3  # GeV (PDG)
mu_r_e = me * R / HBARC_GEV_M
print("INFO  IF mu is the electron mass, mu r at r = 38.6 um = %.4e (the mu r -> 0 hypothesis would be violated by %.1f orders)"
      % (mu_r_e, math.log10(mu_r_e)))
print("INFO  mu r = 1 for the electron at r = %.4e m" % (HBARC_GEV_M / me))
M5 = (MBAR4 / math.sqrt(2 * math.pi * R / HBARC_GEV_M)) ** (2 / 3)
print("INFO  Mbar5 from eqs. 72-73 at r = 38.6 um: %.5e GeV (prior pass: 1.68968e8)" % M5)
for rp in (30e-6, 20e-6):
    print("INFO  if the alpha = 2 Eot-Wash edge were %.0f um: |c| = %.3e, %.2f orders short" % (rp * 1e6, c_abs(r=rp), math.log10(1e-21 / c_abs(r=rp))))

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
