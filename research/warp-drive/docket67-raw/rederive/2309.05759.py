#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for arXiv:2309.05759 (Kabat & Nomura), eqs. 68, 70-73.
(run 2 adds C9 boost geometry, C10 radion hypothesis, C11 action-level reduction)

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

# ---------------------------------------------------------------- C9 (added, run 2)
# KN eq. 10: a brane moving with velocity beta along the S^1 sees the identification
# vector a = (-gamma beta 2 pi R, gamma 2 pi R) and effective radius r = gamma R.
# Boost the bulk identification (Dt, Dx5) = (0, 2 pi R) into the brane frame.
b = sp.symbols("beta", positive=True)
gb = 1 / sp.sqrt(1 - b ** 2)
Dt, Dx = 0, 2 * sp.pi * R
Dtp = gb * (Dt - b * Dx)
Dzp = gb * (Dx - b * Dt)
check("C9a boosted identification = (-gamma beta 2 pi R, gamma 2 pi R)  (KN eq. 10, r = gamma R)",
      sp.simplify(Dtp + gb * b * 2 * sp.pi * R) == 0 and sp.simplify(Dzp - gb * 2 * sp.pi * R) == 0)
check("C9b its invariant length is 2 pi R (the motion is not a change of the circle)",
      sp.simplify(-Dtp ** 2 + Dzp ** 2 - (2 * sp.pi * R) ** 2) == 0)
d_tree = 7.0e-16   # manyc GW170817 bound on gamma - 1, as the tree uses it
print("INFO C9c at the tree's gamma - 1 <= %.1e, r/R - 1 <= %.1e: the r-vs-R label moves no figure"
      % (d_tree, d_tree))

# ---------------------------------------------------------------- C10 (added, run 2)
# A NAMED HYPOTHESIS neither KN nor the tree states: the radion.  Eq. 69's n = 0 term
# keeps the 5-D tensor structure (eta eta + eta eta - (2/3) eta eta), i.e. it contains a
# massless radion coupled to the trace.  Static-source exchange with eq. 70 vertices and
# eq. 73's normalisation, against 4-D GR with vertex -1/Mbar4:
def contract(c_trace, T1, T2):
    # (1/2)(T1_mn T2^mn + T1_mn T2^nm - c T1 T2), diagonal T in (+,-,-,-), indices lowered by eta
    eta = [1, -1, -1, -1]
    TT = sum(T1[i] * T2[i] for i in range(4))          # T1_mn T2^mn for diagonal T^mn
    tr1 = sum(eta[i] * T1[i] for i in range(4))
    tr2 = sum(eta[i] * T2[i] for i in range(4))
    return sp.Rational(1, 2) * (2 * TT - c_trace * tr1 * tr2)
m1, m2, q, rr = sp.symbols("m1 m2 q rr", positive=True)
Tm1 = [2 * m1 ** 2, 0, 0, 0]; Tm2 = [2 * m2 ** 2, 0, 0, 0]     # <p|T^00|p> = 2 m^2 at rest
P4 = contract(1, Tm1, Tm2); P5 = contract(sp.Rational(2, 3), Tm1, Tm2)
Mamp4 = P4 / (M4 ** 2 * q ** 2)
Vq4 = -Mamp4 / (4 * m1 * m2)
Vr4 = sp.simplify(Vq4 * q ** 2 / (4 * sp.pi * rr))     # FT of 1/q^2 is 1/(4 pi r)
Gs4 = 1 / (8 * sp.pi * M4 ** 2)
check("C10a control: 4-D GR with vertex -1/Mbar4 gives V = -G m1 m2/r, G = 1/(8 pi Mbar4^2)",
      sp.simplify(Vr4 + Gs4 * m1 * m2 / rr) == 0, str(Vr4))
# 5-D zero mode: vertex 1/Mbar5^{3/2} each, propagator 1/(2 pi r) -> 1/Mbar4^2 by eq. 73
ratio = sp.simplify(P5 / P4)
check("C10b eq. 69 at n = 0 (flat S^1, massless radion) gives static G_N = (4/3) G4, "
      "G4 := 1/(8 pi Mbar4^2) of eqs. 72-73", ratio == sp.Rational(4, 3), "ratio %s" % ratio)
# light: traceless T -> the -(2/3) term drops, deflection is 4-D GR's with G4
k0 = sp.symbols("k0", positive=True)
Tph = [2 * k0 ** 2, 0, 0, 2 * k0 ** 2]                 # null momentum along z, traceless
Tph_lower_ok = sum([1, -1, -1, -1][i] * Tph[i] for i in range(4)) == 0
ratio_light = sp.simplify(contract(sp.Rational(2, 3), Tm1, Tph) / contract(1, Tm1, Tph))
gam_ppn = sp.symbols("gamma_PPN")
# deflection = 2(1+gamma_PPN) G_N M/b; GR (gamma=1) with G4: 4 G4 M/b; 5-D: ratio_light*4 G4 M/b
sol_g = sp.solve(sp.Eq(2 * (1 + gam_ppn) * sp.Rational(4, 3), 4 * ratio_light), gam_ppn)
check("C10c with a massless radion light bending is unchanged (traceless T) while G_N is 4/3 x: "
      "gamma_PPN = 1/2", Tph_lower_ok and ratio_light == 1 and sol_g == [sp.Rational(1, 2)],
      "gamma_PPN = %s" % sol_g)
print("READING C10: a flat S^1 with an UNSTABILISED radion is excluded observationally "
      "(gamma_PPN = 1/2 against Cassini's |gamma - 1| ~ 1e-5, Bertotti-Iess-Tortora 2003, "
      "NAMED-NOT-READ here; even a 10% light-deflection test excludes it).  So identifying the "
      "MEASURED G with 1/(8 pi Mbar4^2) of eq. 73 -- which the tree does (branelink MBAR4_GEV "
      "from higgs.reduced_planck_gev) -- needs a stabilised (massive) radion, a hypothesis "
      "neither KN nor the tree states.  It does NOT touch the coupling as used: eq. 73 is the "
      "action-level relation (C11) and the TT gravitational-wave coupling is 1/Mbar4 either way. "
      "Whether GLP's 'Newtonian potential' relation (72) carries this 4/3 is NOT decidable here "
      "(GLP 1103.2174 unread): recorded as a question, not a discrepancy.")

# ---------------------------------------------------------------- C11 (added, run 2)
# action-level: (Mbar5^3/2) int d^4x dz sqrt(g) R5 with z-independent zero mode, z in [0, 2 pi r)
z = sp.symbols("z")
eff = sp.integrate(M5 ** 3 / 2, (z, 0, 2 * sp.pi * r))
check("C11 Einstein-Hilbert reduction over a circle of length 2 pi r gives Mbar4^2/2 = pi r Mbar5^3, "
      "i.e. eq. 73's Mbar4 = (2 pi r)^{1/2} Mbar5^{3/2}",
      sp.simplify(eff - (eq73 ** 2) / 2) == 0)

print()
print("RESULT: %d FAIL" % len(FAIL) if FAIL else "RESULT: ALL PASS")
sys.exit(1 if FAIL else 0)
