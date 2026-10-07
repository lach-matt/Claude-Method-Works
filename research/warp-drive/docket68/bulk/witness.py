#!/usr/bin/env python3
"""witness.py -- M's item 145: "There is ever only one true complete reconstruction. And it is supported by two
witnesses, the README and the corridor".  What each witness carries.

The corridor: its throat area is the README's bit count, 4 pi r_min^2 = N A_bit with A_bit = 2 h G ln2 / (pi c^3)
(exactE.py's identity; the coefficient is chain.py's, loaded by path).  The README: one fixed exact encoding of N bits
(item 136 answer 5).

First written with "the corridor witnesses N, exactly" and "the pair names exactly one string: a checksum"; the
verifier showed the first fails by the board's own K2 estimate and the second hides that a length check catches no
substitution (WITNESS.md History).

  T1  (STRUCTURAL) one bit adds exactly one A_bit of throat area; N and N+1 give distinct classical throats
  T2  but the classical throat cannot carry that distinction: the board's quantum-correction estimate (l_P/r_min)^2 =
      pi/(N ln2) (kderive.py K2, not READ) against one bit's 1/N of area is pi/ln2 = 4.53 at EVERY N -- the throat is
      uncertain by about 4.5 bits.  And measured G (u_r = 2.2e-5, chain.py) fixes N from a measured throat only to
      ~6e10 bits at the example README.  Exactness of N can come only from H-PASSAGE-IS-N (item 137), not from geometry
  T3  (STRUCTURAL) the corridor does not witness the content: 2^N strings share one throat
  T4  (STRUCTURAL) what the pair adds: a length check.  A README one bit short or long is rejected; none of the 2^N - 1
      same-length substitutions is.  The string is fixed by the README alone, under the fixed encoding
Stdlib + sympy.  python3 witness.py [--selftest]
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
_C = {}


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


def chain_coeff():
    if not _C:
        ch = _load(os.path.join(D68, "copy", "chain.py"), "wt_chain")
        _C["r1"] = sp.sympify(ch.coefficients()["r_min_m_per_sqrt_bit"]["exact"])
        _C["u_G"] = ch.U_R_G                                        # chain.py's relative uncertainty of G
    return _C


def t1():
    r1 = chain_coeff()["r1"]
    A_bit = 4 * sp.pi * r1**2
    dA = sp.simplify(4 * sp.pi * ((sp.sqrt(EXAMPLE_N + 1) * r1) ** 2 - (sp.sqrt(EXAMPLE_N) * r1) ** 2))
    return {"one_bit_is_A_bit": sp.simplify(dA - A_bit) == 0,
            "distinct": sp.simplify(sp.sqrt(EXAMPLE_N + 1) - sp.sqrt(EXAMPLE_N)) != 0}


def t2():
    N = sp.Symbol("N", positive=True)
    qcorr = sp.pi / (N * sp.log(2))                                 # kderive.py K2's estimate, (l_P/r_min)^2
    ratio = sp.simplify(qcorr / (1 / N))                            # against one bit's fractional area 1/N
    dN_G = EXAMPLE_N * chain_coeff()["u_G"]                         # area ~ G, so a measured throat fixes N to N u_r(G)
    return {"ratio": ratio, "ratio_value": float(ratio), "dN_from_G": dN_G}


def accepts(readme, N):
    return len(readme) == N


def t34(n=12):
    readme = "101100111010"[:n]
    flipped = readme[:3] + ("0" if readme[3] == "1" else "1") + readme[4:]
    return {"strings": 2**n, "accepts": accepts(readme, n), "short": accepts(readme[:-1], n),
            "long": accepts(readme + "0", n), "substitution": accepts(flipped, n), "n": n}


def compute():
    return {"t1": t1(), "t2": t2(), "t34": t34()}


def report(d):
    a, b, c = d["t1"], d["t2"], d["t34"]
    print("witness.py -- the README and the corridor as witnesses (item 145)\n")
    print("T1 one bit adds exactly one A_bit of throat area: %s; N and N+1 distinct classically: %s"
          % (a["one_bit_is_A_bit"], a["distinct"]))
    print("T2 quantum-correction estimate against one bit's area: %s = %.3f at every N; measured G fixes N to ~%.1e bits "
          "at the example README" % (b["ratio"], b["ratio_value"], b["dN_from_G"]))
    print("T3 strings of length %d sharing one throat: %d" % (c["n"], c["strings"]))
    print("T4 length check: accepted %s; one bit short %s; one bit long %s; one bit substituted %s (not caught)"
          % (c["accepts"], c["short"], c["long"], c["substitution"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b, c = d["t1"], d["t2"], d["t34"]
    chk("T1 (STRUCTURAL): one bit adds exactly one A_bit; N and N+1 are distinct classically",
        a["one_bit_is_A_bit"] and a["distinct"])
    chk("T2: the quantum-correction estimate is pi/ln2 = 4.53 bits' worth of area at every N (N cancels)",
        sp.simplify(b["ratio"] - sp.pi / sp.log(2)) == 0)
    chk("T2: measured G fixes N from a throat only to ~6e10 bits at the example README", 5e10 < b["dN_from_G"] < 7e10)
    chk("T3 (STRUCTURAL): 2^N strings share one throat", c["strings"] == 2 ** c["n"])
    chk("T4 (STRUCTURAL): the length check rejects a bit dropped or added", c["accepts"] and not c["short"] and not c["long"])
    chk("T4 (STRUCTURAL): the length check does not catch a substituted bit", c["substitution"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
