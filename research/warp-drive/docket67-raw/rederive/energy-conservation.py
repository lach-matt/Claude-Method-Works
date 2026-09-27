#!/usr/bin/env python3
"""DOCKET 67, pass S, 17/36 -- energy-conservation.
Re-derives massform.py:445-448 ("the carrier must deliver at least Mc^2 ...
1.9975 Mc^2 with B and L conserved ... That is energy conservation. THEOREM")
and machine-checks WHICH hypotheses the floor needs.  Reads the tree's modules
read-only (imports); writes nothing under research/.

C1  Mc^2 and megatons, exact (sympy; c exact SI, 1 Mt = 4.184e15 J by definition).
C2  Pair floor Mc^2 + B mu_min c^2 recomputed from the tree's AME2020 capture,
    once with the tree's CODATA-2018 u and once with CODATA 2022 (scipy 1.17.1).
C3  The same floor with ELECTRIC CHARGE also conserved (a hypothesis the tree
    does not name): the antibaryons must be neutralised by the lightest B = 0
    positive carrier, the positron, so the per-nucleon cost is the least
    ATOMIC mass per nucleon.  The tree's floor stays a floor, and is lower.
C4  Where the energy is counted: Killing energy at infinity for a body formed
    at rest at Earth's surface (Schwarzschild exterior), fractional deficit
    below Mc^2.  Shows the floor is a LOCAL-frame statement.
C5  z3 (linear real arithmetic): the floor follows from the balance
    E_carrier + E_store = Mc^2 + E_anti + E_rad + E_other  exactly when
    E_store = 0, E_rad >= 0, E_other >= 0 and E_anti >= B mu; dropping any one
    of E_store = 0 or E_other >= 0 makes 'E_carrier < Mc^2' satisfiable.
C6  sympy: Noether's energy needs time-translation invariance.  For
    L = q'^2/2 - w(t)^2 q^2/2, dH/dt = -dL/dt|explicit = +w w' q^2 != 0;
    for constant w it is 0.  (The hypothesis the tree's word 'conservation'
    presupposes: a time-translation symmetry -- Minkowski, or a stationary
    spacetime's timelike Killing vector.)
"""
import sys, math
from fractions import Fraction
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import sympy as sp
import z3

bad = []
def check(name, ok, detail=""):
    print(("OK   " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        bad.append(name)

# ---------------------------------------------------------------- C1
c = sp.Integer(299792458)
M = sp.Integer(70)
E = M * c**2
MT = sp.Rational(4184, 1) * sp.Integer(10)**12
print("C1 Mc^2 =", E, "J =", sp.N(E, 8), "J;  megatons =", sp.N(E / MT, 8))
check("C1 Mc^2 = 6.2913e18 J (4 s.f.)", abs(float(E) / 6.2913e18 - 1) < 5e-5)
check("C1 1504 megatons (rounded)", round(float(E / MT)) == 1504)

# ---------------------------------------------------------------- C2
import massform as m
import gravity
import scipy.constants as sc
B = m.COUNTS["B"]
Ne = m.COUNTS["N_e"]
Mc2 = m.rest_energy_j()
check("C2 tree Mc^2 equals exact", abs(Mc2 - float(E)) / float(E) < 1e-15)
MEV_J = 1.602176634e-13            # SI exact (e exact)
me_tree = m.MASS_MEV["e"]
u18 = m.U_MEV
u22 = sc.physical_constants["atomic mass constant energy equivalent in MeV"][0]
me22 = sc.physical_constants["electron mass energy equivalent in MeV"][0]

def mins(u, me):
    best_nuc = best_atom = None
    for Z, _N, A, sym, d_kev, q in gravity.nuclides():
        if q != "M" or A < 1:
            continue
        atom = (A * u + d_kev / 1000.0) / A
        nuc = atom - Z * me / A
        if best_nuc is None or nuc < best_nuc[0]:
            best_nuc = (nuc, sym, A, Z)
        if best_atom is None or atom < best_atom[0]:
            best_atom = (atom, sym, A, Z)
    return best_nuc, best_atom

nuc18, atom18 = mins(u18, me_tree)
nuc22, atom22 = mins(u22, me22)
ratio18 = 1 + B * nuc18[0] * MEV_J / Mc2
ratio22 = 1 + B * nuc22[0] * MEV_J / Mc2
print("C2 u (tree, CODATA 2018) = %.8f MeV; u (CODATA 2022) = %.8f MeV" % (u18, u22))
print("C2 mu_min nuclear: %s-%d %.7f MeV (2018 u), %.7f MeV (2022 u)" % (nuc18[1], nuc18[2], nuc18[0], nuc22[0]))
print("C2 pair floor / Mc^2 = %.7f (2018 u), %.7f (2022 u); shift %.2e" % (ratio18, ratio22, ratio22 - ratio18))
check("C2 tree MU_MIN reproduced", abs(nuc18[0] - m.MU_MIN[0]) < 1e-9 and nuc18[1] == "Fe" and nuc18[2] == 56)
check("C2 1.9975 reproduced", round(ratio18, 4) == 1.9975 and abs(m.pair_floor_j() / Mc2 - ratio18) < 1e-12)
check("C2 CODATA 2022 leaves 1.9975", round(ratio22, 4) == 1.9975)
print("C2 B vs M/m_u: B m_u c^2 / Mc^2 = %.6f" % (B * u18 * MEV_J / Mc2))

# ---------------------------------------------------------------- C3
ratioQ = 1 + B * atom18[0] * MEV_J / Mc2
positrons = B * atom18[3] / atom18[2]
print("C3 least ATOMIC mass per nucleon: %s-%d %.7f MeV" % (atom18[1], atom18[2], atom18[0]))
print("C3 floor with Q conserved (neutral anti-atoms) / Mc^2 = %.7f  (+%.3e over the tree's)" % (ratioQ, ratioQ - ratio18))
print("C3 positrons needed %.4e vs payload L = N_e %.4e; residual antilepton number %.4e carried by antineutrinos"
      % (positrons, Ne, Ne - positrons))
check("C3 tree floor <= Q-floor (still a valid floor)", ratio18 <= ratioQ)
check("C3 Q-floor rounds to 1.9977", round(ratioQ, 4) == 1.9977)
check("C3 L budget allows the positrons (positrons <= N_e)", positrons <= Ne)

# ---------------------------------------------------------------- C4
from ladder import G, M_EARTH
R_EARTH = 6.371e6        # mean radius, m (illustrative; not a READ datum)
phi = G * M_EARTH / (R_EARTH * 2.99792458e8 ** 2)
killing = math.sqrt(1 - 2 * phi)
print("C4 GM/(R c^2) at Earth's surface = %.4e; Killing energy of a body at rest there = (1 - %.4e) Mc^2"
      % (phi, 1 - killing))
check("C4 deficit is ~7e-10 (negligible, but nonzero)", 6e-10 < 1 - killing < 8e-10)
# self-binding the tree names (H-AME note)
check("C4 tree self-binding 5.2e-26 reproduced", abs(m.gravitational_binding_order() / 5.2e-26 - 1) < 0.01)

# ---------------------------------------------------------------- C5
Ec, Es, Mc, Ea, Er, Eo, Bmu = z3.Reals("Ec Es Mc Ea Er Eo Bmu")
balance = Ec + Es == Mc + Ea + Er + Eo
base = [balance, Mc > 0, Bmu > 0]
def valid(hyps, concl):
    s = z3.Solver(); s.add(*hyps); s.add(z3.Not(concl)); return s.check() == z3.unsat
def sat(hyps):
    s = z3.Solver(); s.add(*hyps); return s.check() == z3.sat
full = base + [Es == 0, Er >= 0, Eo >= 0, Ea >= Bmu]
check("C5a full hypotheses |= Ec >= Mc + Bmu", valid(full, Ec >= Mc + Bmu))
free = base + [Es == 0, Er >= 0, Eo >= 0, Ea >= 0]
check("C5b B free (Ea >= 0) |= Ec >= Mc", valid(free, Ec >= Mc))
check("C5c drop Es = 0 (energy stored at the seat): Ec < Mc SAT",
      sat(base + [Es >= 0, Er >= 0, Eo >= 0, Ea >= 0, Ec < Mc]))
check("C5d drop Eo >= 0 (negative-energy by-product, DEC failing): Ec < Mc SAT",
      sat(base + [Es == 0, Er >= 0, Ea >= 0, Ec < Mc]))
check("C5e with Eo >= 0 and Es = 0, Ec < Mc UNSAT",
      not sat(base + [Es == 0, Er >= 0, Eo >= 0, Ea >= 0, Ec < Mc]))

# ---------------------------------------------------------------- C6
t = sp.symbols("t")
q = sp.Function("q")(t)
w = sp.Function("w")(t)
L = sp.diff(q, t) ** 2 / 2 - w ** 2 * q ** 2 / 2
p = sp.diff(L, sp.diff(q, t))
H = p * sp.diff(q, t) - L
eom = sp.Eq(sp.diff(q, t, 2), -w ** 2 * q)
dH = sp.diff(H, t).subs(sp.diff(q, t, 2), eom.rhs)
dH = sp.simplify(dH)
print("C6 dH/dt on shell =", dH)
check("C6 dH/dt = -dL/dt|explicit = +w w' q^2 (energy not conserved without time translation)",
      sp.simplify(dH - w * sp.diff(w, t) * q ** 2) == 0)
w0 = sp.symbols("w0", positive=True)
check("C6 constant w: dH/dt = 0", sp.simplify(dH.subs(w, w0).doit()) == 0)

print()
print("OVERALL", "OK" if not bad else "FAIL: " + ", ".join(bad))
sys.exit(1 if bad else 0)
