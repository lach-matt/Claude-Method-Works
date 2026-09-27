#!/usr/bin/env python3
"""DOCKET 67 -- massive-matter-subluminal.  Re-derivation / machine check.

The result as the tree uses it (candidates.py:80-84, 448-450): moving the
Casimir plates is mechanical, therefore slower than c, therefore the Casimir
lead FAILS the teardown deadline "switches off in ~R/c" (candidates.py:23,320).

Checked here, in four parts:
  A. the theorem itself: from E^2 = p^2 c^2 + m^2 c^4 with m > 0, the group
     velocity v = dE/dp = p c^2 / E satisfies v < c for every finite p, and the
     work to reach v, (gamma - 1) m c^2, diverges as v -> c.  (sympy + z3)
  B. what the theorem gives for a clearing time: any element that must be
     displaced by l takes t >= l / c (strictly >).  That is a bound in l, not R.
  C. the tree's own geometry (gap d = region size R, candidates.py:144,388-392):
     reducing |rho| ~ d^-4 by a factor k^4 needs the gap opened from R to kR, a
     displacement (k-1)R, so t > (k-1) R / c.  The deadline failure FOLLOWS here,
     but only by the factor c / v: "by a lot" needs the datum v << c.
  D. a microstructured geometry (gap d << R, many plate pairs filling the
     region; each top tile of width w slides laterally by w off its partner):
     displacement w, independent of R, so t = w / v can be << R / c with v << c.
     The deadline failure does NOT follow from subluminality here.  Magnitude
     is re-computed in the same geometry: it still fails by ~34 orders at R=1 m.
Nothing here edits the tree.  Exit 0 iff every assertion holds.
"""
import math
import sympy as sp
import z3

ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))


# ---------------------------------------------------------------- A. theorem
print("A. THE THEOREM: massive worldlines are timelike (v < c)")
p, m, c = sp.symbols("p m c", positive=True)
E = sp.sqrt(p**2 * c**2 + m**2 * c**4)
v = sp.diff(E, p)
check("group velocity dE/dp == p c^2 / E", sp.simplify(v - p * c**2 / E) == 0)
gap = sp.simplify(c**2 - v**2)
check("c^2 - v^2 == m^2 c^6 / E^2  (> 0 for m > 0)",
      sp.simplify(gap - m**2 * c**6 / E**2) == 0)
check("lim_{p->oo} v == c (approached, never reached)",
      sp.limit(v, p, sp.oo) == c)
u = sp.symbols("u", positive=True)
gamma = 1 / sp.sqrt(1 - u**2 / c**2)
KE = (gamma - 1) * m * c**2
eps = sp.symbols("epsilon", positive=True)
KE_eps = sp.simplify(KE.subs(u, c * (1 - eps)))
check("work (gamma-1) m c^2 -> oo as v = c(1-eps), eps -> 0+",
      sp.limit(KE_eps, eps, 0, dir="+") == sp.oo)
check("massless limit m=0 gives v == c exactly", sp.simplify(v.subs(m, 0) - c) == 0)

# z3: no real p with m>0, c>0 has v >= c.  v >= c  <=>  p c^2 >= c E  <=>  p c >= E
# (E>0), and squaring (both sides >= 0 when p >= 0): p^2 c^2 >= p^2 c^2 + m^2 c^4.
zp, zm, zc, zE = z3.Reals("p m c E")
s = z3.Solver()
s.add(zm > 0, zc > 0, zE > 0, zE * zE == zp * zp * zc * zc + zm * zm * zc**4)
s.add(zp * zc * zc >= zc * zE)          # v >= c, multiplied through by E > 0
check("z3: {m>0, c>0, E=sqrt(p^2c^2+m^2c^4), v>=c} is UNSAT",
      s.check() == z3.unsat)
s2 = z3.Solver()                        # vacuity guard: m = 0 admits v = c
s2.add(zm == 0, zc > 0, zE > 0, zp > 0,
       zE * zE == zp * zp * zc * zc + zm * zm * zc**4, zp * zc * zc >= zc * zE)
check("z3 vacuity guard: with m = 0 the same constraints are SAT", s2.check() == z3.sat)

# ------------------------------------------------------ B. clearing-time bound
print("\nB. WHAT IT BOUNDS: t_clear > l / c, l = displacement required")
C = 299792458.0                          # exact (SI, 1983)
HBAR = 1.054571817e-34                   # exact (SI, 2019)


def t_min(l):
    return l / C


print("     (a statement, not a test: the bound t > l/c contains l, and R enters only")
print("      through the geometry that fixes l)")

# ------------------------------------------- C. the tree's geometry, d = R
print("\nC. TREE GEOMETRY: gap d = R (candidates.py:144, 388-392)")
for R in (1e-9, 1e-6, 1.0):
    k = 2.0                              # |rho| down by k^4 = 16
    print("     R = %-8.0e  open gap R -> 2R: t > %.3e s = R/c (x 1); at v = 1e3 m/s:"
          " %.3e s = %.1e R/c" % (R, t_min((k - 1) * R), (k - 1) * R / 1e3,
                                   ((k - 1) * R / 1e3) / (R / C)))
check("d = R: t_clear > R/c for a 16-fold reduction, for every v < c",
      all(((2 - 1) * R) / vv > R / C for R in (1e-9, 1.0) for vv in (0.5 * C, 0.99 * C, 1e3)))
check("  but at v = 0.5c the excess is only x2 -- '~R/c' is not failed 'by a lot'",
      abs(((2 - 1) * 1.0 / (0.5 * C)) / (1.0 / C) - 2.0) < 1e-12)

# ------------------------------------ D. microstructured geometry, d << R
print("\nD. MICROSTRUCTURED GEOMETRY: plate pairs, gap d, tile width w, filling R")


def casimir(d):
    return math.pi**2 * HBAR * C / (720.0 * d**4)


RHO_NEEDED_1M = 1.2124e43                # candidates.py:133 table, R = 1 m (READ, not recomputed)
cases = [
    # (R, d, w, v)
    (1.0, 1e-9, 1e-7, 100.0),
    (1.0, 1e-7, 1e-5, 1e4),
    (1e3, 1e-7, 1e-5, 10.0),
]
for R, d, w, vv in cases:
    t = w / vv
    edge = d / w                         # PFA edge correction scale
    print("     R=%-6.0e d=%-6.0e w=%-6.0e v=%-6.0e m/s: t=w/v=%.2e s  R/c=%.2e s"
          "  t/(R/c)=%.2e  v_needed=w c/R=%.1e m/s  edge~%.0e"
          % (R, d, w, vv, t, R / C, t / (R / C), w * C / R, edge))
R, d, w, vv = cases[0]
check("d=1nm, w=100nm, v=100 m/s, R=1m: t = 1.0e-9 s < R/c = 3.34e-9 s",
      w / vv < R / C)
check("  with v << c (v/c = %.1e) -- subluminality alone does not fail ~R/c" % (vv / C),
      vv / C < 1e-6)
check("  and at the tree's d = R the same v gives t/(R/c) = c/v = %.1e" % (C / vv),
      (R / vv) / (R / C) > 1e6)
# magnitude in the microstructured geometry (volume-averaged |rho| <= casimir(d))
short = RHO_NEEDED_1M / casimir(1e-9)
print("     magnitude at R = 1 m with d = 1 nm: need/have = %.3e (%.1f orders)"
      % (short, math.log10(short)))
check("casimir(1 nm) == 4.33375e8 J/m^3 (tree candidates.py:542)",
      abs(casimir(1e-9) / 4.33375e8 - 1) < 1e-4)
check("MAGNITUDE still fails in the microstructured class (> 30 orders at R=1 m)",
      math.log10(short) > 30)

# relativistic work to throw plates: positive, and diverges -- a cost, not a bar
M_plate = 1.0                            # kg, illustrative
for beta in (1e-6, 0.1, 0.9):
    g = 1 / math.sqrt(1 - beta**2)
    print("     plate 1 kg at v = %.0e c: work (gamma-1) M c^2 = %.3e J" % (beta, (g - 1) * M_plate * C**2))

print("\nVERDICT OF THE CHECK: theorem re-derived (A, z3 UNSAT with vacuity guard SAT);")
print("the tree's inference 'mechanical => fails ~R/c' holds in its own d = R geometry")
print("(C) and fails to follow in a microstructured geometry (D), where the Casimir")
print("lead still fails MAGNITUDE.  'by a lot' is a datum (v << c), not the theorem.")
print("ALL OK" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
