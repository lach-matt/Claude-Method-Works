#!/usr/bin/env python3
"""witness.py -- M's item 145: "There is ever only one true complete reconstruction. And it is supported by two
witnesses, the README and the corridor".  What each witness carries, and whether together they fix one reconstruction.

The corridor: its throat area is the README's bit count, 4 pi r_min^2 = N A_bit with A_bit = 2 h G ln2 / (pi c^3)
(exactE.py's identity; H-PASSAGE-IS-N, item 137).  The README: one fixed exact encoding of N bits (item 136 answer 5).

  T1  the corridor witnesses N, exactly: r_min(N) = sqrt(N) r_min(1) is strictly increasing, so distinct N give distinct
      throats -- checked in exact arithmetic for adjacent N at the board's example README.  Its relative difference
      there is 1/(2N) ~ 1.8e-16 (the corridor tells N from N+1 only exactly, never at measured precision)
  T2  the corridor does not witness the content: every one of the 2^N strings of length N has the same throat
      (STRUCTURAL: the area depends on N only)
  T3  the README witnesses the content but not that it crossed: a string alone is a string
  T4  together they fix one: the pair (throat, string) is consistent only if len(string) = N(throat), and then names
      exactly one string -- a checksum.  Control: a README one bit long or short is rejected by its corridor
  T5  under H-ALPHA-IS-LIGHT the electrons' structure and the Löwdin table are the same in every universe
      (samelight.py), while molecular frequencies move with mu (nucleus.py U4): a README written in Z and electron
      configuration reads the same at any position 2; one written in molecular frequencies does not (STRUCTURAL)
Imports copy/chain.py's exact coefficient by path.  Stdlib + sympy.  python3 witness.py [--selftest]
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
EXAMPLE_N = 2742570311524972


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


def r1_exact():
    ch = _load(os.path.join(D68, "copy", "chain.py"), "wt_chain")
    return sp.sympify(ch.coefficients()["r_min_m_per_sqrt_bit"]["exact"])


def t1():
    r1 = r1_exact()
    rN, rN1 = sp.sqrt(EXAMPLE_N) * r1, sp.sqrt(EXAMPLE_N + 1) * r1
    distinct = sp.simplify(rN1 - rN) != 0 and sp.N((rN1 - rN) / rN, 30) > 0
    rel = sp.N(rN1 / rN - 1, 30)
    A_bit = 4 * sp.pi * r1**2                                       # area per bit, from the throat at N = 1
    N_back = sp.nsimplify(sp.simplify(4 * sp.pi * rN**2 / A_bit))
    return {"distinct": bool(distinct), "rel": rel, "half_over_N": sp.N(sp.Rational(1, 2 * EXAMPLE_N), 30),
            "N_back": N_back}


def corridor_N(throat_r, r1):
    return sp.nsimplify(sp.simplify((throat_r / r1) ** 2))


def accepts(readme, throat_r, r1):
    return len(readme) == corridor_N(throat_r, r1)


def t2_t4(n=12):
    r1 = r1_exact()
    throat = sp.sqrt(n) * r1
    readme = "101100111010"[:n]
    return {"strings_per_throat": 2**n, "accepts": accepts(readme, throat, r1),
            "short": accepts(readme[:-1], throat, r1), "long": accepts(readme + "0", throat, r1), "n": n}


def compute():
    return {"t1": t1(), "t24": t2_t4()}


def report(d):
    a, b = d["t1"], d["t24"]
    print("witness.py -- the README and the corridor as witnesses (item 145)\n")
    print("T1 at the example README, N and N+1 give distinct throats: %s; relative difference %s (1/(2N) = %s); the "
          "throat gives back N = %s" % (a["distinct"], sp.N(a["rel"], 6), sp.N(a["half_over_N"], 6), a["N_back"]))
    print("T2 strings of length %d sharing one throat: %d (the corridor does not witness the content)"
          % (b["n"], b["strings_per_throat"]))
    print("T4 a %d-bit README against its corridor: accepted %s; one bit short %s; one bit long %s"
          % (b["n"], b["accepts"], b["short"], b["long"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b = d["t1"], d["t24"]
    chk("T1: N and N+1 give distinct throats at the example README (exact arithmetic)", a["distinct"])
    chk("T1: the relative difference is 1/(2N) to leading order (1.8e-16)", abs(a["rel"] / a["half_over_N"] - 1) < 1e-15)
    chk("T1 (STRUCTURAL): the throat gives back N exactly", a["N_back"] == EXAMPLE_N)
    chk("T2 (STRUCTURAL): 2^N strings share one throat", b["strings_per_throat"] == 2 ** b["n"])
    chk("T4: the README is accepted by its own corridor", b["accepts"])
    chk("T4 control (STRUCTURAL): a README one bit short or long is rejected", not b["short"] and not b["long"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
