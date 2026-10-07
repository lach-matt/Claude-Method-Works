#!/usr/bin/env python3
"""exactcopy.py -- M's item 146 followed through: "1 - no tolerance at all  2 - yes" (the encoding is written in what
every universe shares).

What an invariant encoding can carry exactly, and what it cannot.  In the Born-Oppenheimer picture the electrons'
energy surface does not depend on the nuclear masses (Hanneke et al. 2020 p.6: "The electronic energy T_e is
independent of mu", READ in nucleus.py), so a molecule's EQUILIBRIUM geometry, in atomic units, is the same in every
universe sharing alpha (H-ALPHA-IS-LIGHT).  Its quantum GROUND STATE is not: zero-point motion depends on the nuclear
mass.  Shown on a Morse oscillator with H2-like constants (standard values, not READ here).

  X1  the Morse ground state: <r> - r_e = (ln(2 lam) - psi(2 lam - 1))/a, lam = sqrt(2 m D)/(a hbar) (the ground-state
      density is a Gamma distribution in z = 2 lam e^{-a(r - r_e)}; derived here, STRUCTURAL).  Control: as lam grows
      (the classical limit) the shift goes to zero
  X2  change the reduced mass by eps = 1e-7: r_e is unchanged (it is the potential's minimum); <r> moves by a computed,
      non-zero amount -- so under "no tolerance at all" a copy's ground state is exact only where mu is exactly ours
  X3  what the encoding can and cannot fix: an invariant encoding fixes Z, configurations and BO geometry exactly in
      every universe that shares alpha; it cannot fix the copy's motion (zero-point, vibration, rotation), which is
      position 2's
Stdlib + sympy (digamma).  python3 exactcopy.py [--selftest]
"""
import math
import sys

import sympy as sp

HBAR = 1.054571817e-34                 # J s (SI)
EV = 1.602176634e-19                   # J (SI)
U = 1.66053906660e-27                  # kg, CODATA 2018 (standard, not READ here)
D_E = 4.7446 * EV                      # H2 well depth, J (standard Morse fit, not READ here)
A_M = 1.9426e10                        # Morse a, m^-1 (standard, not READ here)
R_E = 0.7414e-10                       # equilibrium bond length, m (standard, not READ here)
M_RED = 1.00782503 * U / 2             # H2 reduced mass (standard, not READ here)


def lam(m):
    return math.sqrt(2 * m * D_E) / (A_M * HBAR)


def mean_shift(m):
    L = lam(m)
    return (math.log(2 * L) - float(sp.polygamma(0, 2 * L - 1).evalf(30))) / A_M


def compute(eps=1e-7):
    s0 = mean_shift(M_RED)
    s1 = mean_shift(M_RED * (1 + eps))
    big = [mean_shift(M_RED * f) for f in (1, 100, 10000)]
    return {"lam": lam(M_RED), "shift": s0, "rel_shift": s0 / R_E, "d_shift": s1 - s0, "d_rel": (s1 - s0) / R_E,
            "eps": eps, "classical": big, "re_change": 0.0}


def report(d):
    print("exactcopy.py -- no tolerance, invariant encoding (item 146)\n")
    print("X1 H2-like Morse: lambda = %.2f; ground-state <r> - r_e = %.4e m (%.3f%% of r_e); heavier and heavier "
          "(x1, x100, x10000): %s" % (d["lam"], d["shift"], 100 * d["rel_shift"],
                                       ["%.2e" % x for x in d["classical"]]))
    print("X2 reduced mass changed by %.0e: r_e changes by %s; <r> changes by %+.3e m (%+.2e of r_e) -- not zero"
          % (d["eps"], d["re_change"], d["d_shift"], d["d_rel"]))
    print("X3 an invariant encoding fixes Z, configuration and BO geometry exactly; the copy's zero-point motion is "
          "position 2's")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("X1: H2's ground-state <r> sits above r_e by about 3 percent (zero-point motion in an anharmonic well)",
        0.015 < d["rel_shift"] < 0.035)
    chk("X1 control: the shift falls toward zero as the mass grows (classical limit), roughly as m^-1/2",
        d["classical"][0] > d["classical"][1] > d["classical"][2] and abs(d["classical"][1] / d["classical"][0] - 0.1) < 0.02)
    chk("X2: a reduced-mass change of 1e-7 moves <r> by about -1/2 eps of the shift (non-zero; r_e fixed)",
        d["d_shift"] < 0 and abs(d["d_shift"] / (d["shift"] * d["eps"]) + 0.5) < 0.05)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
