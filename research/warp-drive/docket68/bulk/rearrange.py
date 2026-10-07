#!/usr/bin/env python3
"""rearrange.py -- M's item 148: "No, BUT, matter at position 2 can rearrange to accommodate the README, however, after
reconstruct the object is governed entirely by laws of position 2".

First written with a displacement term that does not belong (the harmonic mean does not depend on mass) and a
cancellation-prone width formula; corrected, and an exact Morse check added (REARRANGE.md History).

On exactcopy.py's H2 Morse model (imported by path), with the electrons' energy surface shared (the board's
H-ALPHA-IS-LIGHT) so the curvature k = m w^2 is the same in both universes, and eps the reduced-mass ratio in atomic
units (the README's own units, H-INVARIANT-ENCODING):

  R1  a STATE value -- the bond's mean and spread -- can be prepared at the instant in position 2's matter.  The state
      with our exact values is not position 2's ground state; its excess energy is the width term
      (hbar w'/4)(sqrt(x) - 1/sqrt(x))^2, x = sqrt(m'/m), ~ hbar w' eps^2 / 16.  Checked independently by the exact Morse
      identity (Hellmann-Feynman: <T> = -m dE0/dm; excess = E0(m) - E0(m') + <T>(m/m' - 1)), in which the anharmonic
      term contributes exactly zero.  Control: eps = 0 gives zero
  R2  a LAW value -- a vibrational frequency -- is position 2's from the first instant: w'/w = sqrt(m/m') (STRUCTURAL)
  R3  after the instant, in the harmonic approximation, the spread breathes at 2 w' (standard, not READ)
Imports exactcopy.py by path; sympy for the exact check.  python3 rearrange.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
EV = 1.602176634e-19


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


X = _load(os.path.join(HERE, "exactcopy.py"), "ra_exactcopy")
K = 2 * X.D_E * X.A_M**2                                            # Morse curvature at r_e, shared


def omega(m):
    return math.sqrt(K / m)


def excess(eps):
    m, m2 = X.M_RED, X.M_RED * (1 + eps)
    w2 = omega(m2)
    x = math.sqrt(m2 / m)
    width = X.HBAR * w2 / 4 * (math.sqrt(x) - 1 / math.sqrt(x)) ** 2
    return {"total_eV": width / EV, "in_hw": width / (X.HBAR * w2), "w_ratio": w2 / omega(m)}


def excess_morse_exact(eps, digits=50):
    m = sp.Symbol("m", positive=True)
    hb, k, D = sp.Float(X.HBAR, digits), sp.Float(K, digits), sp.Float(X.D_E, digits)
    E0 = hb * sp.sqrt(k / m) / 2 - (hb * sp.sqrt(k / m)) ** 2 / (16 * D)
    T = -m * sp.diff(E0, m)
    m1 = sp.Float(X.M_RED, digits)
    m2 = m1 * (1 + sp.Float(eps, digits))
    val = E0.subs(m, m1) - E0.subs(m, m2) + T.subs(m, m1) * (m1 / m2 - 1)
    return float(sp.N(val / sp.Float(EV, digits), digits))


def compute():
    return {e: dict(excess(e), exact=(excess_morse_exact(e) if e else 0.0)) for e in (0.0, 1e-7, 1e-4, 1e-2)}


def report(d):
    print("rearrange.py -- the instant and after (item 148)\n")
    print("hbar w (ours) = %.4f eV; eps is the reduced-mass ratio in atomic units" % (X.HBAR * omega(X.M_RED) / EV))
    for e, v in d.items():
        print("eps = %-6g  excess %.4e eV (%.4e hbar w'); exact Morse %.4e eV; w'/w = %.9f"
              % (e, v["total_eV"], v["in_hw"], v["exact"], v["w_ratio"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("R1 control: with no mass difference the excess is zero", d[0.0]["total_eV"] == 0.0)
    chk("R1: at eps = 1e-7 the excess is eps^2/16 of a quantum, 6.25e-16 (to 1 percent)",
        abs(d[1e-7]["in_hw"] / 6.25e-16 - 1) < 0.01)
    chk("R1: the exact Morse excess (Hellmann-Feynman, independent) equals the width term to 1e-6 at eps = 1e-7, 1e-4, 1e-2",
        all(abs(d[e]["exact"] / d[e]["total_eV"] - 1) < 1e-6 for e in (1e-7, 1e-4, 1e-2)))
    chk("R2 (STRUCTURAL): position 2's frequency is w sqrt(m/m'), -eps/2 to first order",
        abs((d[1e-4]["w_ratio"] - 1) / 1e-4 + 0.5) < 1e-3)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
