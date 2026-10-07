#!/usr/bin/env python3
"""rearrange.py -- M's item 148: "No, BUT, matter at position 2 can rearrange to accommodate the README, however, after
reconstruct the object is governed entirely by laws of position 2".

The board's reading: exactness is met at the instant of reconstruction; what follows is position 2's.  Two kinds of
value then part ways (on exactcopy.py's H2 Morse model, imported by path; the electrons' energy surface shared, the
board's H-ALPHA-IS-LIGHT, so the curvature k = m w^2 is the same in both universes):

  R1  a STATE value -- the mean bond length <r>, the spread -- can be prepared exactly at the instant: position 2's
      matter can be put in a state with our <r> and our spread whatever its mass.  That state is not position 2's
      ground state: it carries an excess energy, computed in the harmonic approximation as
      (1/2) k (d<r>)^2 + (hbar w'/4)(x + 1/x - 2), x = sqrt(m'/m), and it goes as eps^2.  Control: eps = 0 gives zero
  R2  a LAW value -- a vibrational frequency -- cannot be prepared: it belongs to position 2's Hamiltonian from the
      first instant, w'/w = sqrt(m/m') (STRUCTURAL)
  R3  after the instant, position 2's laws govern: the prepared <r> oscillates at w' about position 2's own mean, and
      the spread breathes at 2 w' (standard, not READ) -- the README's state values hold at the instant only
Imports exactcopy.py by path.  python3 rearrange.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

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
    dr = X.mean_shift(m) - X.mean_shift(m2)                          # our <r> minus position 2's own
    w2 = omega(m2)
    x = math.sqrt(m2 / m)
    disp = 0.5 * K * dr * dr
    width = X.HBAR * w2 / 4 * (x + 1 / x - 2)
    return {"dr": dr, "disp_eV": disp / EV, "width_eV": width / EV, "total_eV": (disp + width) / EV,
            "in_hw": (disp + width) / (X.HBAR * w2), "w_ratio": w2 / omega(m)}


def compute():
    return {e: excess(e) for e in (0.0, 1e-7, 1e-4, 1e-2)}


def report(d):
    print("rearrange.py -- exact at the instant, position 2's after (item 148)\n")
    print("hbar w (ours) = %.4f eV" % (X.HBAR * omega(X.M_RED) / EV))
    for e, v in d.items():
        print("eps = %-6g  d<r> = %+.3e m  excess energy %.3e eV (%.3e hbar w')  [displacement %.2e, width %.2e]  "
              "w'/w = %.9f" % (e, v["dr"], v["total_eV"], v["in_hw"], v["disp_eV"], v["width_eV"], v["w_ratio"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("R1 control: with no mass difference the prepared state is position 2's own, excess zero",
        d[0.0]["total_eV"] == 0.0)
    r = d[1e-2]["total_eV"] / d[1e-4]["total_eV"]
    chk("R1: the excess energy goes as eps^2 (a factor 100 in eps gives ~1e4)", 0.9e4 < r < 1.1e4)
    chk("R1: at eps = 1e-7 the excess is below 1e-14 hbar w -- tiny, but not zero", 0 < d[1e-7]["in_hw"] < 1e-14)
    chk("R2 (STRUCTURAL): position 2's frequency is w sqrt(m/m'), -eps/2 to first order",
        abs((d[1e-4]["w_ratio"] - 1) / 1e-4 + 0.5) < 1e-3)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
