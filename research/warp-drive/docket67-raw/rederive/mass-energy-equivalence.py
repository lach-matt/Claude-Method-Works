#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'mass-energy-equivalence' (E = M c^2).

Owner: research/warp-drive/warpfolder.py:55-58, 301-302, 314-316, 490-518.
Read-only: imports warpfolder with bytecode writing disabled; writes nothing
under research/.  Exit 0 iff every check passes.

Parts
  A  Einstein 1905 two-pulse argument, EXACT in sympy (not only to O(v^2)):
     a body emitting total energy L in its rest frame loses rest mass L/c^2.
  B  The additive constant: if (E/c, p) is a four-vector and E = gamma m c^2 + C,
     then C = 0 -- the ABSOLUTE rest energy is m c^2, not only differences.
  C  z3: no nonzero C survives the four-vector condition on a boost (rational box).
  D  The tree's arithmetic: rest energies at the folder's three payloads, the
     printed-table ratios, megatons, shortfall, Planck fraction.
  E  Data sensitivity: c is SI-exact; the empirical test bound (Rainville et al.
     2005, NAMED-NOT-READ, 1 - dm c^2/E = (-1.4 +- 4.4)e-7) moved through every
     tree conclusion.
"""
import math
import os
import sys

import sympy as sp

sys.dont_write_bytecode = True
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)

FAIL = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("   " + str(detail)) if detail != "" else ""))
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ Part A
print("== A. Einstein 1905 two-pulse argument, exact")
L, c, v, phi = sp.symbols("L c v phi", positive=True)
beta = v / c
gam = 1 / sp.sqrt(1 - beta ** 2)
# energies of the two pulses in the moving frame (relativistic Doppler for energy)
Lp = (L / 2) * gam * (1 - beta * sp.cos(phi))
Lm = (L / 2) * gam * (1 + beta * sp.cos(phi))
total_moving = sp.simplify(Lp + Lm)
chk("A1 total emitted energy in moving frame = gamma L", sp.simplify(total_moving - gam * L) == 0, total_moving)
# E0 = E1 + L (rest frame), H0 = H1 + gamma L (moving frame)
# K0 - K1 = (H0 - E0) - (H1 - E1) = gamma L - L
dK = sp.simplify(total_moving - L)
chk("A2 K0 - K1 = L (gamma - 1)", sp.simplify(dK - L * (gam - 1)) == 0, dK)
# Einstein's step: expand to O(v^2): (1/2)(L/c^2) v^2
ser = sp.series(dK, v, 0, 4).removeO()
chk("A3 to O(v^2): K0 - K1 = (1/2)(L/c^2) v^2  (Einstein's printed form)",
    sp.simplify(ser - sp.Rational(1, 2) * L / c ** 2 * v ** 2) == 0, ser)
# exact: with K = (gamma - 1) m c^2, dK = (gamma - 1) dm c^2 => dm = L/c^2 at ALL v
dm = sp.symbols("dm")
sol = sp.solve(sp.Eq((gam - 1) * dm * c ** 2, dK), dm)
chk("A4 exact at every v (given K = (gamma-1) m c^2): dm = L/c^2", len(sol) == 1 and sp.simplify(sol[0] - L / c ** 2) == 0, sol)
# note: using only the Newtonian K = (1/2) m v^2 gives dm = L/c^2 only as v -> 0
solN = sp.solve(sp.Eq(sp.Rational(1, 2) * dm * v ** 2, dK), dm)[0]
chk("A5 with Newtonian K the identification is exact only as v->0",
    sp.limit(solN, v, 0) == L / c ** 2 and sp.simplify(solN - L / c ** 2) != 0, sp.limit(solN, v, 0))

# ------------------------------------------------------------------ Part B
print("== B. The additive constant")
m, u, C = sp.symbols("m u C", real=True)
bu = u / c
gu = 1 / sp.sqrt(1 - bu ** 2)
# body at rest in S: E = m c^2 + C, p = 0.  In S' (S moves at +u relative to S'),
# the four-vector law gives E' = gu (E + u p) = gu (m c^2 + C);
# the ansatz applied in S' gives E' = gu m c^2 + C.
eq = sp.Eq(gu * (m * c ** 2 + C), gu * m * c ** 2 + C)
solC = sp.solve(eq, C)
chk("B1 four-vector law + ansatz forces C = 0 for u != 0", solC == [0], solC)
# invariant: E^2 - p^2 c^2 = m^2 c^4 with p = gamma m v
E = gam * sp.Symbol("M", positive=True) * c ** 2
p = gam * sp.Symbol("M", positive=True) * v
chk("B2 E^2 - p^2 c^2 = M^2 c^4 (so E(p=0) = M c^2)",
    sp.simplify(E ** 2 - p ** 2 * c ** 2 - sp.Symbol("M", positive=True) ** 2 * c ** 4) == 0)

# ------------------------------------------------------------------ Part C
print("== C. z3: no nonzero C survives (rational box)")
try:
    import z3
    Cz, gz, mc2 = z3.Reals("C g mc2")
    s = z3.Solver()
    s.add(gz > 1, gz < 100, mc2 > 0, Cz != 0, gz * (mc2 + Cz) == gz * mc2 + Cz)
    r = s.check()
    chk("C1 z3: {g>1, C!=0, g(mc2+C) = g mc2 + C} is UNSAT", r == z3.unsat, r)
    s2 = z3.Solver()
    s2.add(gz > 1, gz < 100, mc2 > 0, gz * (mc2 + Cz) == gz * mc2 + Cz)
    chk("C2 vacuity guard: without C!=0 it is SAT (the box is not empty)", s2.check() == z3.sat)
except ImportError:
    print("SKIP C: z3 not installed (pip install z3-solver)")

# ------------------------------------------------------------------ Part D
print("== D. The tree's arithmetic (warpfolder imported read-only)")
import warpfolder as wf  # noqa: E402

cS = 2.99792458e8
chk("D0 tree c is the SI-exact 299 792 458", wf.c == cS, wf.c)
E100, E5k, E1e5 = (wf.rest_energy_j(x) for x in (100.0, 5000.0, 1.0e5))
chk("D1 100 kg -> 8.98755e18 J", abs(E100 / 8.987551787e18 - 1) < 1e-9, E100)
chk("D2 printed 8.98e18 within 2e-3", abs(E100 / 8.98e18 - 1) < 2e-3, E100 / 8.98e18 - 1)
chk("D3 printed 4.49e20 (5000 kg) within 2e-3", abs(E5k / 4.49e20 - 1) < 2e-3, E5k / 4.49e20 - 1)
ratio = 8.98e22 / E1e5
chk("D4 1e5 kg: 8.98755e21, printed 8.98e22 is x9.9916 (one slipped decade)",
    abs(E1e5 / 8.987551787e21 - 1) < 1e-9 and abs(ratio - 9.9916) < 1e-3, ratio)
mt = E100 / 4.184e15
chk("D5 100 kg = 2148 Mt = 2.15 Gt ('2.1 GIGATONS', 2 s.f. truncation-consistent)", 2140 < mt < 2150, mt)
stored = wf.stored_joules()
chk("D6 stored = Marx 1250 J + laser 235.6 J = 1485.6 J",
    abs(wf.marx_joules() - 1250.0) < 1e-9 and abs(stored - 1485.62) < 0.01, (wf.marx_joules(), wf.laser_joules(), stored))
sf = E100 / stored
chk("D7 shortfall 6.050e15 = 15.78 orders", abs(sf / 6.050e15 - 1) < 1e-3 and abs(math.log10(sf) - 15.7818) < 1e-4,
    (sf, math.log10(sf)))
# the flash duration is short: Hawking lifetime at 100 kg (context only; that
# formula is a different external result audited elsewhere)
tau = wf.hawking_lifetime_s(100.0)
print("     context: tau_Hawking(100 kg) =", tau, "s")

# ------------------------------------------------------------------ Part E
print("== E. Data sensitivity")
eps_lo, eps_hi = -1.4e-7 - 3 * 4.4e-7, -1.4e-7 + 3 * 4.4e-7  # 3 sigma band on 1 - dm c^2/E
for eps in (eps_lo, eps_hi):
    E_alt = E100 / (1 - eps)  # E = dm c^2 / (1 - eps)
    chk("E1 at 3 sigma (eps=%.2e) shortfall orders move by < 1e-5" % eps,
        abs(math.log10(E_alt / stored) - math.log10(sf)) < 1e-5, math.log10(E_alt / stored))
    chk("E2 at 3 sigma the 1e5-row factor stays 9.99 (not 1)",
        abs(8.98e22 / (E1e5 / (1 - eps)) - 9.9916) < 1e-3)
# where would the table's decade be 'right'? only if c were sqrt(10) larger -- excluded, c is exact
chk("E3 the 8.98e22 row would need c x sqrt(10) = 9.48e8 m/s (c is SI-exact: no datum can supply it)",
    abs(math.sqrt(8.98e22 / 1e5) / cS - math.sqrt(9.9916)) < 1e-3, math.sqrt(8.98e22 / 1e5))
# binding-energy self-correction to M for a 100 kg body (R ~ 0.3 m): negligible
Ug = 0.6 * wf.G * 100.0 ** 2 / 0.3
chk("E4 Newtonian self-binding of 100 kg at R=0.3 m is < 1e-24 of M c^2", Ug / E100 < 1e-24, Ug / E100)

print()
print("RESULT:", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
