#!/usr/bin/env python3
"""values.py -- M's item 147: the copy's motion is not in the README; the README carries both labels and values.
With item 146's "no tolerance at all", which values can be exact?

Two kinds of continuous value a README could carry about a molecule:
  (P) a PARAMETER the copy is built around -- e.g. its equilibrium shape, the minimum of the electrons' energy surface;
      in the point-nucleus Born-Oppenheimer picture with alpha shared (the board's H-ALPHA-IS-LIGHT) it is the same in
      every universe, so it can be exact by construction (corrections of order m_e/M and nuclear size aside)
  (S) a STATE value -- where the copy's nuclei actually are.  Quantum mechanics forbids an exact one: localizing a
      nucleus to a width d costs kinetic energy ~ hbar^2/(2 m d^2) (the uncertainty principle; standard, not READ here)

  V1  the localization cost against the bond: for H2's reduced mass, the width d* at which hbar^2/(2 m d^2) equals the
      bond's well depth D_e (4.7446 eV, standard, not READ) -- localize better than d* and the molecule comes apart
  V2  at a nuclear-size width (1e-15 m) the cost is ~40 MeV, millions of times the bond (STRUCTURAL arithmetic)
  V3  d* is the same order as the zero-point width the copy's own motion supplies (exactcopy.py: <r> - r_e ~ 2.3e-12 m)
      -- the motion item 147 leaves to position 2 is exactly what keeps a state value from being exact
Stdlib only.  python3 values.py [--selftest]
"""
import math
import sys

HBAR = 1.054571817e-34
EV = 1.602176634e-19
U = 1.66053906660e-27
D_E = 4.7446 * EV                      # H2 well depth (standard, not READ here)
M_RED = 1.00782503 * U / 2             # H2 reduced mass (standard, not READ here)
ZP_SHIFT = 2.2648e-12                  # exactcopy.py X1's Morse <r> - r_e, m


def cost(d, m=M_RED):
    return HBAR**2 / (2 * m * d * d)


def compute():
    d_star = HBAR / math.sqrt(2 * M_RED * D_E)
    return {"d_star": d_star, "cost_nuclear_MeV": cost(1e-15) / EV / 1e6, "ratio_nuclear": cost(1e-15) / D_E,
            "zp": ZP_SHIFT, "dstar_over_zp": d_star / ZP_SHIFT}


def report(d):
    print("values.py -- labels and values under no tolerance (item 147)\n")
    print("V1 localizing H2's nuclei better than d* = %.3e m costs more than the bond (D_e = 4.7446 eV)" % d["d_star"])
    print("V2 at a nuclear-size width, 1e-15 m: %.1f MeV, %.1e times the bond" % (d["cost_nuclear_MeV"], d["ratio_nuclear"]))
    print("V3 d* against the zero-point shift the copy's own motion supplies (exactcopy.py): %.2f" % d["dstar_over_zp"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("V1: localizing H2's nuclei better than about 3 pm costs more than the bond energy", 2e-12 < d["d_star"] < 4e-12)
    chk("V1 control: at d* the cost equals the bond energy (to 1e-12)", abs(cost(d["d_star"]) / D_E - 1) < 1e-12)
    chk("V2 (STRUCTURAL): at a nuclear-size width the cost is ~40 MeV (H2 reduced mass), over a million times the bond",
        35 < d["cost_nuclear_MeV"] < 50 and d["ratio_nuclear"] > 1e6)
    chk("V3: d* is the same order as the copy's own zero-point shift (ratio between 0.3 and 3)", 0.3 < d["dstar_over_zp"] < 3)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
