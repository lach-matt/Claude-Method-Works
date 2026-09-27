#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for arXiv:2309.05759 (Kabat & Nomura), eqs. 68, 70-73.

Source text: scratchpad/d67/src/2309.05759.cached.txt (alphaXiv page capture of
2309.05759v2, printed pp. 18-19 = capture pages 19-20).  Checks what is closed-form:

  C1  footnote 8 (G4 = G5/(gamma 2 pi R), G4 = 1/8piMbar4^2, G5 = 1/8piMbar5^3) => eq. 72
  C2  r = gamma R in eq. 72 => eq. 73's algebraic form
  C3  mass dimensions of eqs. 68, 70 in 5D (h_AB canonical dim 3/2)
  C4  eq. 68 + the matter-action variation (+,-,-,-) => eq. 70's coefficient -1/Mbar5^{3/2}
  C5  zero-mode reduction: eq. 70 with eq. 73 => the standard 4D coupling -(kappa/2) h T,
      kappa = sqrt(32 pi G)   (Giudice-Rattazzi-Wells normalisation, KN ref. [13])
  C6  eq. 71 vertex from eq. 70's T^{mu nu} on plane waves (non-commutative gamma symbols)
  C7  numerics: Mbar4 from CODATA 2018 = 2022 G against eq. 73's printed 2.4e18 GeV,
      and against branelink.MBAR4_GEV (the tree's own computed value, imported read-only)
  C8  "the coupling is not a free parameter": which couplings depend on the unmeasured r
"""
import math
import sys
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------- C1, C2
G4, G5, M4, M5, R, r, gam = sp.symbols("G4 G5 Mbar4 Mbar5 R r gamma", positive=True)
fn8 = sp.Eq(1 / (8 * sp.pi * M4 ** 2), (1 / (8 * sp.pi * M5 ** 3)) / (gam * 2 * sp.pi * R))
sol = sp.solve(fn8, M4)
eq72 = sp.sqrt(gam * 2 * sp.pi * R) * M5 ** sp.Rational(3, 2)
check("C1 footnote 8 => eq. 72  Mbar4 = (gamma 2 pi R)^{1/2} Mbar5^{3/2}",
      len(sol) == 1 and sp.simplify(sol[0] - eq72) == 0, str(sol))
eq73 = sp.sqrt(2 * sp.pi * r) * M5 ** sp.Rational(3, 2)
check("C2 r = gamma R in eq. 72 => eq. 73  Mbar4 = (2 pi r)^{1/2} Mbar5^{3/2}",
      sp.simplify(eq72.subs(R, r / gam) - eq73) == 0)
# the tilt-like extension (r = cos(theta) R, KN eq. 84) is an ASSUMPTION in KN
# ("We take this relation to hold in general"); nothing here derives it.
print("NOTE C2' eq. 73 for tilt-like branes (r = cos theta R) is KN's stated assumption, "
      "not derived in KN nor here")

# ---------------------------------------------------------------- C3
# 5D action: int d^5x [ Mbar5^3 R_5 ]  -> h_AB with canonical kinetic term has dim 3/2.
dim = {"Mbar5": 1, "h5": sp.Rational(3, 2), "T4": 4, "d4x": -4}
d68 = -sp.Rational(3, 2) * dim["Mbar5"] + dim["h5"]
d70 = -sp.Rational(3, 2) * dim["Mbar5"] + dim["T4"] + dim["h5"]
check("C3 eq. 68: (2/Mbar5^{3/2}) h_AB dimensionless", d68 == 0, "dim=%s" % d68)
check("C3 eq. 70: T h / Mbar5^{3/2} has dim 4 on the brane (4D Lagrangian density)",
      d70 == 4, "dim=%s" % d70)

# ---------------------------------------------------------------- C4
# (+,-,-,-): T_{mu nu} = (2/sqrt(-g)) dS/dg^{mu nu};  dg^{mu nu} = -eta eta dg_{ab}
# => dS = -(1/2) T^{ab} dg_{ab};  dg_{ab} = (2/Mbar5^{3/2}) h_{ab}  (eq. 68)
Tsym, hsym = sp.symbols("T h")
dS = -sp.Rational(1, 2) * Tsym * (2 / M5 ** sp.Rational(3, 2)) * hsym
check("C4 eq. 68 + dS = -(1/2) T dg  => eq. 70 coefficient -1/Mbar5^{3/2}",
      sp.simplify(dS - (-Tsym * hsym / M5 ** sp.Rational(3, 2))) == 0)

# ---------------------------------------------------------------- C5
# zero mode: h(x,z) = h0(x)/sqrt(2 pi r) + ...  => coefficient -1/(sqrt(2 pi r) Mbar5^{3/2})
Gs = sp.symbols("G", positive=True)
coef0 = 1 / (sp.sqrt(2 * sp.pi * r) * M5 ** sp.Rational(3, 2))
coef0_M4 = sp.simplify(coef0.subs(M5, sp.solve(sp.Eq(M4, eq73), M5)[0]))
kappa_half = sp.sqrt(32 * sp.pi * Gs) / 2
check("C5a zero-mode coupling = 1/Mbar4 (r drops out)", sp.simplify(coef0_M4 - 1 / M4) == 0,
      str(coef0_M4))
check("C5b 1/Mbar4 = kappa/2 with kappa = sqrt(32 pi G), Mbar4 = (8 pi G)^{-1/2}",
      sp.simplify(kappa_half - 1 / (1 / sp.sqrt(8 * sp.pi * Gs))) == 0)

# ---------------------------------------------------------------- C6
# T^{mn} = (i/4) psibar(g^m d^n + g^n d^m)psi - (i/4)(d^m psibar g^n + d^n psibar g^m) psi
# psi ~ e^{-i k1 x} (d -> -i k1), psibar ~ e^{+i k2 x} (d -> +i k2); vertex = i x (coeff of h)
I = sp.I
k1m, k1n, k2m, k2n = sp.symbols("k1m k1n k2m k2n")
gm, gn = sp.symbols("gm gn", commutative=False)
T = (I / 4) * (gm * (-I * k1n) + gn * (-I * k1m)) - (I / 4) * ((I * k2m) * gn + (I * k2n) * gm)
vertex = sp.expand(I * (-1 / M5 ** sp.Rational(3, 2)) * T)
eq71 = sp.expand(-I / (4 * M5 ** sp.Rational(3, 2)) * ((k1m + k2m) * gn + (k1n + k2n) * gm))
check("C6 eq. 70's T^{mu nu} on plane waves => eq. 71 vertex "
      "-i/(4 Mbar5^{3/2}) [(k1+k2)^mu g^nu + (k1+k2)^nu g^mu]",
      sp.expand(vertex - eq71) == 0, str(sp.factor(vertex)))

# ---------------------------------------------------------------- C7
HBAR = 1.054571817e-34      # J s, exact-derived (SI 2019)
CL = 299792458.0            # m/s exact
GEV = 1.602176634e-10       # J exact
G_2022 = 6.67430e-11        # CODATA 2018 = CODATA 2022 (u = 0.00015e-11), scipy txt2022 line 1884
MPL = math.sqrt(HBAR * CL / G_2022) * CL ** 2 / GEV
MBAR4 = MPL / math.sqrt(8 * math.pi)
check("C7a Mbar4 (CODATA 2022 G) = %.6e GeV rounds to eq. 73's printed 2.4e18"
      % MBAR4, round(MBAR4 / 1e18, 1) == 2.4, "rel. diff vs 2.4e18 = %+.3e" % (MBAR4 / 2.4e18 - 1))
relG = 0.00015 / 6.67430
print("INFO C7b u_r(G) = %.2e  -> u_r(Mbar4) = %.2e (Mbar4 ~ G^{-1/2})" % (relG, relG / 2))
try:
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import higgs  # read-only import; nothing is written
    tree = higgs.reduced_planck_gev()
    check("C7c tree's Mbar4 (higgs.reduced_planck_gev) agrees with this CODATA-2022 value",
          abs(tree / MBAR4 - 1) < 1e-9, "tree %.9e, here %.9e" % (tree, MBAR4))
except Exception as e:  # pragma: no cover
    print("SKIP C7c tree import failed: %r" % (e,))
HBARC_GEV_M = HBAR * CL / GEV
for rm in (38.6e-6, 1e-3, 1e-15):
    rG = rm / HBARC_GEV_M
    m5 = (MBAR4 ** 2 / (2 * math.pi * rG)) ** (1 / 3)
    print("INFO C7d r = %.3g m -> Mbar5 = %.6e GeV, 5D coupling 1/Mbar5^{3/2} = %.4e GeV^-3/2, "
          "LV coupling 1/(pi r Mbar4)^2 = %.4e" % (rm, m5, m5 ** -1.5, 1 / (math.pi * rG * MBAR4) ** 2))

# ---------------------------------------------------------------- C8
M5_of_r = sp.solve(sp.Eq(M4, eq73), M5)[0]
g5 = sp.simplify(1 / M5_of_r ** sp.Rational(3, 2))
check("C8a 5D coupling 1/Mbar5^{3/2} = (2 pi r)^{1/2}/Mbar4 -- depends on r",
      sp.simplify(g5 - sp.sqrt(2 * sp.pi * r) / M4) == 0 and sp.diff(g5, r) != 0, str(g5))
check("C8b zero-mode (4D GW) coupling 1/Mbar4 independent of r", sp.diff(coef0_M4, r) == 0)
lv = 1 / (sp.pi * r * M4) ** 2
check("C8c eq. 76's dimensionless coupling 1/(pi r Mbar4)^2 depends on r (d/dr = -2/(pi^2 Mbar4^2 r^3))",
      sp.simplify(sp.diff(lv, r) + 2 / (sp.pi ** 2 * M4 ** 2 * r ** 3)) == 0)
print("READING C8: no coupling CONSTANT is free once G is measured -- eq. 73 fixes Mbar5 from "
      "(Mbar4, r) -- but r is an unmeasured geometric parameter (Eot-Wash bounds it above only, "
      "on gamma*L per GLP eq. 39), and every non-zero-mode amplitude carries it.  'Not a free "
      "parameter' holds for the coupling constant, conditional on r.")

print()
print("RESULT: %d FAIL" % len(FAIL) if FAIL else "RESULT: ALL PASS")
sys.exit(1 if FAIL else 0)
