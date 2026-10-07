#!/usr/bin/env python3
"""values.py -- M's item 147 followed through: the copy's motion is not in the README ("No"); the README carries labels
AND values ("both"); with item 146's "no tolerance at all".

First written with a parameter/state split and an uncertainty argument; the verifier showed the split revived a claim
exactcopy.py had withdrawn and the uncertainty argument addressed sharp positions, not the values M was asked about
(mean lengths, frequencies).  Withdrawn (VALUES.md History).

The values put to M were a molecule's mean bond length and its frequencies (EXACTCOPY.md).  Those are consequences of
the copy's motion under its laws.  If the README states them exactly and the motion is supplied at position 2, the
laws there must reproduce them exactly.  On the board's H2 Morse model (exactcopy.py, imported by path):

  V1  the mean bond length <r>(m) is strictly monotonic in the reduced mass across a factor of 100 either side: one
      value of <r> pins one mass.  The harmonic frequency (~ m^-1/2) likewise (STRUCTURAL)
  V2  contrast: a label (the number of bound levels) is the same across a finite window of mass (exactcopy.py X3) --
      labels leave the mass free inside the window; values do not
  V3  so with labels AND values exact, the window collapses to one point: position 2's reduced mass for each pair of
      nuclei the README names must equal ours exactly.  Control: a mass 1e-9 off ours fails the value test while
      passing the label test
Imports exactcopy.py by path.  Stdlib + sympy (through exactcopy).  python3 values.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


X = _load(os.path.join(HERE, "exactcopy.py"), "vl_exactcopy")


def mean_r(m):
    return X.R_E + X.mean_shift(m)


def compute():
    m0 = X.M_RED
    grid = [m0 * 10 ** (k / 20) for k in range(-40, 41)]           # a factor of 100 either side
    rs = [mean_r(m) for m in grid]
    mono = all(b < a for a, b in zip(rs, rs[1:]))                   # heavier -> shorter
    test_m = m0 * (1 + 1e-9)
    label_ok = X.n_levels(test_m) == X.n_levels(m0)
    value_ok = mean_r(test_m) == mean_r(m0)
    w = X.window()
    return {"monotonic": mono, "label_same_at_1e-9": label_ok, "value_same_at_1e-9": value_ok,
            "dr_at_1e-9": mean_r(test_m) - mean_r(m0), "win": (w["m_lo"] / m0, w["m_hi"] / m0)}


def report(d):
    print("values.py -- labels and values under no tolerance (item 147)\n")
    print("V1 <r>(m) strictly monotonic over m/100 to 100 m: %s -- one value pins one mass" % d["monotonic"])
    print("V2 the label set holds from %.4f to %.4f of our reduced mass (exactcopy.py X3)" % d["win"])
    print("V3 a reduced mass 1e-9 off ours: label test passes %s; value test passes %s (<r> moves %+.2e m)"
          % (d["label_same_at_1e-9"], d["value_same_at_1e-9"], d["dr_at_1e-9"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("V1: the mean bond length is strictly monotonic in the reduced mass over a factor of 100 either side",
        d["monotonic"])
    chk("V2: the label set holds over a finite window around our mass", d["win"][0] < 1 < d["win"][1])
    chk("V3 control: a mass 1e-9 off ours passes the label test and fails the value test",
        d["label_same_at_1e-9"] and not d["value_same_at_1e-9"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
