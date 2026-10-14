#!/usr/bin/env python3
"""exactcopy.py -- M's item 146 followed through: "1 - no tolerance at all  2 - yes" (the encoding is written in what
every universe shares).

First written claiming the equilibrium geometry as an exactly realizable invariant and offering no-cloning as support
for "only one"; the verifier showed the first is a Hamiltonian parameter, not a state, and the second misreads item 146
(EXACTCOPY.md History).

Under "no tolerance at all", what an invariant encoding can carry exactly is DISCRETE: element identity (Z), electron
configuration, vibrational and rotational quantum numbers.  Continuous values -- a bond's mean length, a frequency --
depend on the nuclear-to-electron mass ratio (and, beyond Born-Oppenheimer, on nuclear size and m_e/M corrections).
Shown on a Morse oscillator with H2-like constants (standard values, not READ here; the board's H-MORSE-MODEL).

  X1  the Morse ground state's mean displacement <x> = (ln 2 lam - psi(2 lam - 1))/a, lam = sqrt(2 m D)/(a hbar):
      derived (the density in z = 2 lam e^{-a x} is a Gamma distribution of shape 2 lam - 1) AND checked by direct
      quadrature of psi_0^2 (genuine).  It is 3.1% of r_e in the model (ab initio H2 is about 3.4%, the verifier's
      figure, not READ: Morse runs ~10% low)
  X2  a continuous value moves: a reduced-mass change of 1e-7 shortens <r> by 1.6e-9 of r_e (-0.51 eps of the shift;
      STRUCTURAL, from lam ~ sqrt(m))
  X3  a discrete label does not: the number of bound vibrational levels is floor(lam - 1/2) + 1 (17 in the model).
      The label set v = 0..16 is exactly the same for every reduced mass between the two values where lam crosses a
      half-integer -- a finite window, computed.  Outside it a level appears or vanishes.  Control: at the window's
      edges the count changes
Stdlib + sympy (digamma).  python3 exactcopy.py [--selftest]
"""
import math
import sys

import sympy as sp

HBAR = 1.054571817e-34                 # J s (SI)
EV = 1.602176634e-19                   # J (SI)
U = 1.66053906660e-27                  # kg, CODATA 2018 (standard, not READ here)
D_E = 4.7446 * EV                      # H2 well depth (standard Morse fit, not READ here)
A_M = 1.9426e10                        # Morse a, m^-1 (standard, not READ here)
R_E = 0.7414e-10                       # equilibrium bond length, m (standard, not READ here)
M_RED = 1.00782503 * U / 2             # H2 reduced mass (standard, not READ here)


def lam(m):
    return math.sqrt(2 * m * D_E) / (A_M * HBAR)


def mean_shift(m):
    L = lam(m)
    return (math.log(2 * L) - float(sp.polygamma(0, 2 * L - 1).evalf(30))) / A_M


def mean_shift_quadrature(m, steps=200000):
    """<x> from psi_0^2 directly: psi_0 ~ z^(lam - 1/2) e^(-z/2), z = 2 lam e^(-a x)."""
    L = lam(m)
    lo, hi = -0.6e-10, 3.0e-10
    h = (hi - lo) / steps
    num = den = 0.0
    for i in range(steps + 1):
        x = lo + i * h
        z = 2 * L * math.exp(-A_M * x)
        w = math.exp((2 * L - 1) * math.log(z) - z)
        f = 0.5 if i in (0, steps) else 1.0
        num += f * w * x
        den += f * w
    return num / den


def n_levels(m):
    return math.floor(lam(m) - 0.5) + 1


def window():
    L = lam(M_RED)
    lo_L, hi_L = math.floor(L - 0.5) + 0.5, math.floor(L - 0.5) + 1.5        # lam where the count changes
    return {"lam": L, "m_lo": M_RED * (lo_L / L) ** 2, "m_hi": M_RED * (hi_L / L) ** 2}


def compute(eps=1e-7):
    s0 = mean_shift(M_RED)
    s1 = mean_shift(M_RED * (1 + eps))
    w = window()
    return {"lam": lam(M_RED), "shift": s0, "quad": mean_shift_quadrature(M_RED), "rel": s0 / R_E,
            "d_shift": s1 - s0, "d_rel": (s1 - s0) / R_E, "eps": eps, "levels": n_levels(M_RED), "win": w,
            "edge": (n_levels(w["m_lo"] * 0.999), n_levels(w["m_lo"] * 1.001), n_levels(w["m_hi"] * 0.999),
                     n_levels(w["m_hi"] * 1.001))}


def report(d):
    w = d["win"]
    print("exactcopy.py -- no tolerance, invariant encoding (item 146)\n")
    print("X1 Morse H2: lambda = %.2f; <r> - r_e = %.4e m by the closed form, %.4e m by quadrature (%.2f%% of r_e)"
          % (d["lam"], d["shift"], d["quad"], 100 * d["rel"]))
    print("X2 reduced mass changed by %.0e: <r> moves by %+.3e m (%+.2e of r_e)" % (d["eps"], d["d_shift"], d["d_rel"]))
    print("X3 bound vibrational levels: %d (v = 0..%d); the same label set holds for reduced mass from %.4f to %.4f of "
          "ours (%+.1f%% to %+.2f%%); at the edges the count goes %d|%d and %d|%d"
          % (d["levels"], d["levels"] - 1, w["m_lo"] / M_RED, w["m_hi"] / M_RED, 100 * (w["m_lo"] / M_RED - 1),
             100 * (w["m_hi"] / M_RED - 1), *d["edge"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("X1: the closed form for the Morse ground state's <x> agrees with direct quadrature to 1e-6",
        abs(d["quad"] / d["shift"] - 1) < 1e-6)
    chk("X2 (STRUCTURAL): a reduced-mass change of eps moves <r> by about -1/2 eps of the shift, shortening it",
        d["d_shift"] < 0 and abs(d["d_shift"] / (d["shift"] * d["eps"]) + 0.5) < 0.05)
    chk("X3: the Morse model holds 17 bound levels, and the label set is unchanged across a finite window of mass",
        d["levels"] == 17 and d["win"]["m_lo"] < M_RED < d["win"]["m_hi"])
    chk("X3 control: just outside each edge of the window the number of levels changes",
        d["edge"][0] == 16 and d["edge"][1] == 17 and d["edge"][2] == 17 and d["edge"][3] == 18)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
