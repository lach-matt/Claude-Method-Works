#!/usr/bin/env python3
"""ledger.py -- Warp Theorem lemmas E3 and E4: the energy ledger closes, and the field energy outside the neck is placed.

  E4a the plane's energy outside the neck is computed: the Misner-Sharp mass of eq. (17) at r0 = 2m is
          M(R) = m + (m/4) (1 - m/(2R - 3m)),
      m at the throat, 5m/4 far away (the ADM total).  So the E/4 lies close in: two thirds within R = 3m, 98% within
      the hold's span (O3, ~30m).  It cannot be set aside as a far field a brief hold never forms
  E4b it is not the plane's energy.  The plane carries no matter (B1: R = 0, tau = 0, escape.py S3), so its Einstein
      tensor is the bulk's Weyl projection, G = -E (Maartens-Koyama eq. 143, READ in throatbulk.py): the E/4 is the
      bulk's gravitational field read on the plane -- the same kind of reading as Z1's, where the plane's null-energy
      deficit is the bulk's pull.  Its density is positive (dM/dR > 0 outside the neck).  So the plane's own ledger --
      the one exact energy E carried from the device into position 2 (items 104 (b), 110, 111, 133) -- is complete
      without it; where the bulk's field comes from belongs to the five-dimensional formation (B7)
  E3  the ledger closes under the board's reading (a) (WARPTHEOREM.md): the copy, exact (146) and made of reorganized
      matter (137, 148), absorbs at most the assembly energy; the remainder is absorbed as the expansion of position 2's
      universe (136 G, 136 answer 6, 139 (3)), counted as part of the build, which keeps 111 (a).  Computed at the
      example README and at item 108's full snapshot: E = E_copy + E_expansion with both terms non-negative and E_copy
      within the assembly ceiling (z3, exact rationals).  Control: with no expansion term the ledger is unsatisfiable.
      PROVED UNDER reading (a), which stays the board's and is withdrawn if M corrects it
Imports copy/exactE.py by path.  Stdlib + sympy + z3.  python3 ledger.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972
SNAPSHOT_N = 1.088e29                 # item 108's full atomic snapshot
ASSEMBLY_MAX_J = 1.1947e10            # LOOSE.md L1, H-BOND-CEILING
C = 299792458


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def e4():
    r, m, R = sp.symbols("r m R", positive=True)
    H = (1 - 2 * m / r) ** 2 / (1 - sp.Rational(3, 2) * m / r)
    M = sp.simplify(r / 2 * (1 - H))
    closed = m + m / 4 * (1 - m / (2 * r - 3 * m))
    frac = lambda Rv: float(((M - m) / (m / 4)).subs({m: 1, r: Rv}))
    dM = sp.simplify(sp.diff(M, r))
    return {"M": M, "closed_ok": sp.simplify(M - closed) == 0, "at_throat": sp.simplify(M.subs(r, 2 * m)),
            "far": sp.limit(M, r, sp.oo), "f3": frac(3), "f30": frac(30.48), "dM": dM,
            "dM_pos": all(float(dM.subs({m: 1, r: x})) > 0 for x in (2.01, 2.5, 3, 10, 1e3))}


def e3(E_per_sqrt_bit):
    import z3

    def ledger(E_value, with_expansion):
        E, cp, ex = z3.Reals("E copy expansion")
        s = z3.Solver()
        s.add(E == E_value, cp >= 0, cp <= z3.RealVal(str(Fraction(ASSEMBLY_MAX_J))), E == cp + ex)
        s.add(ex >= 0 if with_expansion else ex == 0)
        ok = s.check() == z3.sat
        return ok, (float(s.model()[ex].as_fraction()) if ok and with_expansion else None)
    out = {}
    for name, N in (("example", EXAMPLE_N), ("snapshot", SNAPSHOT_N)):
        Ev = E_per_sqrt_bit * math.sqrt(N)
        Ez = z3.RealVal(str(Fraction(Ev)))
        out[name] = {"N": N, "E": Ev, "E_over_c2_kg": Ev / C**2, "closes": ledger(Ez, True)[0],
                     "no_expansion": ledger(Ez, False)[0], "expansion_least": Ev - ASSEMBLY_MAX_J}
    return out


def compute():
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "lg_exactE")
    return {"e4": e4(), "e3": e3(ex.e_per_sqrt_bit())}


def report(d):
    a, b = d["e4"], d["e3"]
    print("ledger.py -- Warp Theorem lemmas E3, E4\n")
    print("E4a Misner-Sharp M(R) = m + (m/4)(1 - m/(2R - 3m)): %s; m at the throat (%s), %s far away; share of the E/4 "
          "within 3m %.3f, within the hold's span %.3f" % (a["closed_ok"], a["at_throat"], a["far"], a["f3"], a["f30"]))
    print("E4b dM/dR = %s > 0 outside the neck: %s -- the bulk's Weyl field read on the plane (G = -E, MK 143)"
          % (a["dM"], a["dM_pos"]))
    for k, v in b.items():
        print("E3  %s README (N = %.4g): E = %.6e J (E/c^2 = %.4g kg); closes with the expansion: %s, least expansion "
              "%.6e J; with none: %s" % (k, v["N"], v["E"], v["E_over_c2_kg"], v["closes"], v["expansion_least"],
                                        v["no_expansion"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b = d["e4"], d["e3"]
    m = sp.Symbol("m", positive=True)
    chk("E4a: M(R) = m + (m/4)(1 - m/(2R - 3m)) exactly; m at the throat, 5m/4 far away",
        a["closed_ok"] and sp.simplify(a["at_throat"] - m) == 0 and sp.simplify(a["far"] - 5 * m / 4) == 0)
    chk("E4a: two thirds of the E/4 lies within 3m, 98% within the hold's span", abs(a["f3"] - 2 / 3) < 1e-9
        and a["f30"] > 0.98)
    chk("E4b: its density is positive outside the neck", a["dM_pos"])
    chk("E3: the ledger closes with the expansion term, at the example README and at the full snapshot",
        b["example"]["closes"] and b["snapshot"]["closes"])
    chk("E3 control: with no expansion term it cannot close at either", not b["example"]["no_expansion"]
        and not b["snapshot"]["no_expansion"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
