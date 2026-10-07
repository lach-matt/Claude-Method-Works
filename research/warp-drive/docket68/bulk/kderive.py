#!/usr/bin/env python3
"""kderive.py -- k from the work (M-RULINGS item 140: "the math in our work should give you pieces to both derive and
prove k. Our math is not dependent on k, k is dependent on our work").

The chain sizes every corridor by four-dimensional quantities: E(N) and the throat r_min(N) come from the 4D horizon
area per bit, A_bit = 4 l_P^2 ln2, and 4D G (chain.py; exactE.py).  In the bulk, a plane object reads four-dimensional
only when it is large against the bulk's curvature length ell = 1/k, and five-dimensional when small:
Figueras-Wiseman, arXiv:1105.2558v2 p.3 (READ): "small (compared to ell) braneworld black holes behave like 5d
asymptotically flat Schwarzschild black holes and large ones recover 4d behaviour"; the 4D corrections go as
O(ell^2/R^2) (p.4).

  K1  the one-bit throat, exactly: r_min(1) = 2 G E(1)/c^4 = l_P sqrt(ln2/pi), two disjoint paths (exactE's coefficient;
      the closed form) -- 7.5918511091462209829e-36 m
  K2  DERIVED BOUND: if every README, down to one bit, has a four-dimensional corridor (the chain's own premise,
      H-FOUR-D-CORRIDOR), then ell <= r_min(1): k >= (1/l_P) sqrt(pi/ln2) = 1.3172e35 1/m
  K3  THE VALUE, under one named hypothesis (H-ONE-BIT-SCALE): the bulk's curvature length IS the one-bit throat,
      ell = r_min(1).  Then, exactly:  r_min(N) = ell sqrt(N)  -- every corridor's throat is sqrt(N) bulk lengths;
      the 4D description's corrections go as ell^2/r0^2 = 1/N;  G5 = G ell (RS: G4 = G5/ell);  the plane's tension
      lambda = 3 c^4 / (4 pi G ell^2) = 3 c^7 / (4 hbar G^2 ln2)
  K4  the checks against measurement: every bound READ (k > 1.25e4 1/m, OUTSIDE.md) is met by 30 orders; it predicts no
      short-range change of Newton's law on any bench
Stdlib + sympy.  python3 kderive.py [--selftest]
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

H = sp.Rational(662607015, 10**42)
HBAR = H / (2 * sp.pi)
C = sp.Integer(299792458)
G = sp.Rational(66743, 10**15)


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


def exactE():
    return _load(os.path.join(D68, "copy", "exactE.py"), "kd_exactE")


def compute():
    e1 = sp.Float(str(exactE().e_per_sqrt_bit()), 25)                # E(1), J (exactE)
    r1_owner = 2 * G * e1 / C**4                                     # path 1: the owner's coefficient
    lP = sp.sqrt(HBAR * G / C**3)
    r1_closed = lP * sp.sqrt(sp.log(2) / sp.pi)                      # path 2: the closed form
    ell = r1_closed                                                  # K3, H-ONE-BIT-SCALE
    k = 1 / ell
    N = sp.Symbol("N", positive=True)
    E_N = sp.sqrt(N * H * C**5 * sp.log(2) / (8 * sp.pi**2 * G))
    r_N = 2 * G * E_N / C**4
    tension = 3 * C**4 / (4 * sp.pi * G * ell**2)
    tension_closed = 3 * C**7 / (4 * HBAR * G**2 * sp.log(2))
    return {"r1_owner": r1_owner, "r1_closed": r1_closed, "lP": lP, "ell": ell, "k": k,
            "rN_over_ell": sp.simplify(r_N / ell), "corr": sp.simplify((ell / r_N) ** 2),
            "G5": G * ell, "tension": tension, "tension_closed": tension_closed,
            "measured_k_bound": sp.Float("1.25e4")}


def report(d):
    print("kderive.py -- k from the work (item 140)\n")
    print("K1 the one-bit throat: r_min(1) = %s m (exactE); l_P sqrt(ln2/pi) = %s m"
          % (sp.N(d["r1_owner"], 20), sp.N(d["r1_closed"], 20)))
    print("K2 DERIVED: a four-dimensional corridor for every README needs ell <= r_min(1): k >= %s 1/m (= 2.1290/l_P)"
          % sp.N(d["k"], 8))
    print("K3 under H-ONE-BIT-SCALE (ell = r_min(1)):")
    print("   k = %s 1/m;  r_min(N)/ell = %s;  4D corrections ell^2/r0^2 = %s" % (sp.N(d["k"], 12), d["rN_over_ell"],
                                                                                  d["corr"]))
    print("   G5 = G ell = %s m^4 kg^-1 s^-2;  the plane's tension = %s J/m^3" % (sp.N(d["G5"], 6), sp.N(d["tension"], 6)))
    print("K4 against the measured bound k > %s 1/m: exceeded by a factor %s; no bench sees it"
          % (d["measured_k_bound"], sp.N(d["k"] / d["measured_k_bound"], 4)))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("K1: the one-bit throat by two disjoint paths agrees (exactE's coefficient; l_P sqrt(ln2/pi)) to 1e-15",
        abs(d["r1_owner"] / sp.N(d["r1_closed"], 30) - 1) < 1e-15)
    chk("K1: it is 7.5918511091462209829e-36 m (EXACTE.md's per-sqrt-bit throat)",
        abs(sp.N(d["r1_closed"], 30) / sp.Float("7.5918511091462209829e-36", 30) - 1) < 1e-18)
    chk("K2: the bound is k >= sqrt(pi/ln2)/l_P, about 2.129 Planck units",
        abs(sp.N(d["k"] * d["lP"], 20) - sp.N(sp.sqrt(sp.pi / sp.log(2)), 20)) < 1e-15)
    chk("K3: every corridor's throat is exactly sqrt(N) bulk lengths, and its 4D corrections go as 1/N",
        sp.simplify(d["rN_over_ell"] - sp.sqrt(sp.Symbol("N", positive=True))) == 0 and
        sp.simplify(d["corr"] - 1 / sp.Symbol("N", positive=True)) == 0)
    chk("K3: the plane's tension in closed form, 3 c^7/(4 hbar G^2 ln2), two paths agree",
        sp.simplify(d["tension"] - d["tension_closed"]) == 0)
    chk("K4: k exceeds every measured lower bound (k > 1.25e4 1/m) -- consistent with all data",
        d["k"] > d["measured_k_bound"])
    Gbad = G * (1 + sp.Rational(1, 10**9))
    r1_bad = sp.sqrt(HBAR * Gbad / C**3) * sp.sqrt(sp.log(2) / sp.pi)
    chk("control: the closed form with G one part in 1e9 high misses exactE's throat (the two-path check can fail)",
        abs(d["r1_owner"] / sp.N(r1_bad, 30) - 1) > 1e-12)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
