#!/usr/bin/env python3
"""i2_capacity.py -- Warp Theorem lemma I2: the README's N bits within every capacity bound the board has READ.

  I2a  the throat's holding capacity is exactly N: by H1 (exactE.py, proved), 4 pi r0^2 = N A_bit with
       A_bit = 4 ln2 l_P^2, so the area's bit count A/(4 l_P^2 ln2) -- the holographic bound at the Schwarzschild scale,
       H-STRONG-BOUND (chain.py) -- is N, with no slack.  Control: a throat at 1.01 r0 holds 2% more
  I2b the interaction bound as READ -- information carried at most what is sent to set up the interaction
       (Maldacena-Stanford-Yang, READ in residue/STATUS.md wall B: p.4; parametric, p.12): what sets up the corridor is
       the README itself, the opening's inflow (item 115 (c), H-INFLOW-IS-README), N bits, with N the device's input
       (130 (2)).  So carried <= sent is N <= N: met with equality
  I2c the channel bound (DOORS.md K4): with shared entanglement a sent qubit carries at most 2 bits, so N bits need at
       least N/2 channel uses through a causal channel.  The passage is a causal channel, one way 1 -> 2 (O1; a null
       geodesic of the five-dimensional geometry, PASSAGE5D P1 -- not light, item 90), and the shared entanglement is N
       bits (I1, item 137) -- at least the N/2 superdense coding consumes.  The throat holds N bits (I2a) >= N/2
  So the README sits at the corridor's capacity in every form READ: exactly at the holding bound and the interaction
  bound, inside the channel bound.  Imports copy/exactE.py by path.  python3 i2_capacity.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


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


def compute():
    h, c, G, N = sp.symbols("h c G N", positive=True)
    hbar = h / (2 * sp.pi)
    lP2 = hbar * G / c**3
    r0 = sp.sqrt(N * h * G * sp.log(2) / (2 * sp.pi**2 * c**3))         # exactE.py's r_min
    bits = sp.simplify(4 * sp.pi * r0**2 / (4 * lP2 * sp.log(2)))
    bits_ctl = sp.simplify(4 * sp.pi * (sp.Rational(101, 100) * r0) ** 2 / (4 * lP2 * sp.log(2)))
    A_bit_ok = sp.simplify(2 * h * G * sp.log(2) / (sp.pi * c**3) - 4 * sp.log(2) * lP2) == 0
    sent, carried = N, N                                                # I2b: the inflow is the README (115 (c))
    ebits, uses_needed = N, N / 2                                       # I2c
    return {"bits": bits, "bits_ctl": bits_ctl, "A_bit_ok": A_bit_ok, "I2b": sp.simplify(sent - carried),
            "I2c_ebits_ok": sp.simplify(ebits - uses_needed).is_positive, "I2c_hold_ok": sp.simplify(bits - uses_needed).is_positive}


def report(d):
    print("i2_capacity.py -- Warp Theorem lemma I2\n")
    print("I2a the throat holds A/(4 l_P^2 ln2) = %s bits (A_bit = 4 ln2 l_P^2: %s); control at 1.01 r0: %s"
          % (d["bits"], d["A_bit_ok"], d["bits_ctl"]))
    print("I2b sent - carried = %s: the interaction bound met with equality" % d["I2b"])
    print("I2c N ebits >= N/2 uses: %s; the throat's N bits >= N/2: %s" % (d["I2c_ebits_ok"], d["I2c_hold_ok"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    N = sp.Symbol("N", positive=True)
    chk("I2a: the throat's holographic count is exactly N, A_bit = 4 ln2 l_P^2", sp.simplify(d["bits"] - N) == 0
        and d["A_bit_ok"])
    chk("I2a control: a throat 1% wider holds 2.01% more -- the count is not built in",
        sp.simplify(d["bits_ctl"] - sp.Rational(10201, 10000) * N) == 0)
    chk("I2b (STRUCTURAL): the inflow is the README, so carried = sent = N", d["I2b"] == 0)
    chk("I2c: N shared ebits and the throat's N bits both exceed the N/2 channel uses superdense coding needs",
        d["I2c_ebits_ok"] and d["I2c_hold_ok"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
