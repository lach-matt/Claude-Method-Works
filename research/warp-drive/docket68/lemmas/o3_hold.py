#!/usr/bin/env python3
"""o3_hold.py -- Warp Theorem lemma O3: the hold's length in the corridor's clocks, and that the corridor survives it.

READ (through bulk/crossing.py, P-ML): Margolus & Levitin, quant-ph/9710043v2 -- at least h/(4E) to reach one orthogonal
state (eq. 4, p.4); energies of non-interacting subsystems add, and so do their rates (p.8); the bound is on orthogonal
states, NOT bits (p.2).

  O3a  the hold's least length.  The README's N bits are written onto N holders (the throat and horizons hold it, H1,
       H2: 4 ln2 Planck areas per bit), each written by one step to an orthogonal state (H-ONE-STEP-PER-BIT, the board's,
       crossing.py: exactness, item 146, needs perfect distinguishability, and that is orthogonality -- standard, not
       READ).  With the one exact energy E held during the write (items 111 (b), 133) and split over the N holders,
       eq. 4 per holder gives t >= h/(4 E/N), least when split equally:
           hold >= h N / (4 E) = (2 pi^2 / ln2) m/c = 28.4777 clocks,
       THE SAME NUMBER OF CLOCKS FOR EVERY README, because E^2 is proportional to N (computed exactly).  At the example
       README, 1.89e-35 s: "immeasurable but not zero" (item 86 answer 5).  Control: written one bit after another
       (eq. 2), twice that, 4 pi^2/ln2.
  O3b  the hold IS that length: H-HOLD-AT-BOUND, the board's reading -- the theory's quantities sit at their bounds
       (the one exact energy is the Bekenstein energy at equality, items 133, 136 answer 1), and the hold is
       "instantaneous or near instantaneous" (136 E), so it is the least time the write allows.  Labelled; withdrawn if
       the mathematics refutes it
  O3c  the corridor survives that hold in linear theory: over v = 28.4777 m of the horizon's advanced time,
       stability.py S4's exact rate changes the second derivative by v/(4m) = 7.12 times its natural size, and S5b's
       power-law blueshift is at most (1 + v/(8m))^2 = 20.8 for rays starting within m of the surface.  Finite and
       computed: a perturbation below 1/21 of the non-linear threshold stays linear through the whole hold.  Control:
       the non-extremal r0 = 1.8m member's exponential, e^(kappa v) = 90.6 over the same v
  O3d  what this costs elsewhere: the hold, 28.5 clocks, is longer than GLOBALBULK G1's local span (1.3-3.2 clocks).
       So the hold is NOT decided by the local bulk alone, and lemma B4 (the global bulk) bears on the hold itself
Imports copy/exactE.py and bulk/stability.py by path.  Stdlib + sympy.  python3 o3_hold.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
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


def hold_in_clocks():
    h, c, G, N = sp.symbols("h c G N", positive=True)
    E = sp.sqrt(N * h * c**5 * sp.log(2) / (8 * sp.pi**2 * G))       # G1, the one exact energy (exactE.py's form)
    clock = (G * E / c**4) / c                                       # m/c
    parallel = sp.simplify((h * N / (4 * E)) / clock)
    sequential = sp.simplify((h * N / (2 * E)) / clock)
    return parallel, sequential


def compute():
    par, seq = hold_in_clocks()
    v = float(par)                                                   # in units of m
    st = _load(os.path.join(D68, "bulk", "stability.py"), "o3_stability")
    m = sp.Symbol("m", positive=True)
    c1, _ = st.D_derivatives(sp.Rational(9, 5) * m, 2 * m)            # control member's D'
    kappa_ctl = float((c1 / 2).subs(m, 1))
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "o3_exactE")
    E_ex = ex.e_per_sqrt_bit() * math.sqrt(EXAMPLE_N)
    G, C = 6.67430e-11, 299792458.0
    clock_s = G * E_ex / C**5
    return {"parallel": par, "sequential": seq, "v": v, "hold_s": v * clock_s, "clock_s": clock_s,
            "s4_growth": v / 4, "s5b_blueshift": (1 + v / 8) ** 2, "control_exp": math.exp(kappa_ctl * v),
            "kappa_ctl": kappa_ctl, "g1_span": (1.29, 3.16)}


def report(d):
    print("o3_hold.py -- Warp Theorem lemma O3: the hold\n")
    print("O3a hold >= h N/(4E) = %s m/c = %.4f clocks for every N (sequential control: %s = %.4f)"
          % (d["parallel"], d["v"], d["sequential"], float(d["sequential"])))
    print("    at the example README: clock %.3e s, hold %.3e s" % (d["clock_s"], d["hold_s"]))
    print("O3b H-HOLD-AT-BOUND (the board's): the hold is that least time")
    print("O3c over the hold: S4 change %.2f x natural size; S5b blueshift <= %.1f; control member e^(kappa v) = %.1f"
          % (d["s4_growth"], d["s5b_blueshift"], d["control_exp"]))
    print("O3d the hold (%.1f clocks) exceeds G1's local span (%.2f-%.2f clocks): B4 bears on the hold"
          % ((d["v"],) + d["g1_span"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("O3a: h N/(4E) = (2 pi^2/ln2) m/c exactly -- the same number of clocks for every N",
        sp.simplify(d["parallel"] - 2 * sp.pi**2 / sp.log(2)) == 0)
    chk("O3a control: written one bit after another, twice that (4 pi^2/ln2)",
        sp.simplify(d["sequential"] - 2 * d["parallel"]) == 0)
    chk("O3a: at the example README the hold is ~1.9e-35 s -- immeasurable, not zero", 1e-36 < d["hold_s"] < 1e-34)
    chk("O3c: over the hold S4 changes the second derivative by v/(4m) = 7.12 natural sizes; S5b at most 20.8",
        abs(d["s4_growth"] - 7.119) < 1e-2 and abs(d["s5b_blueshift"] - 20.77) < 0.05)
    chk("O3c control: the non-extremal member grows e^(kappa v) = 90.6, more than the corridor's power law",
        abs(d["control_exp"] - 90.6) < 0.5 and d["control_exp"] > d["s5b_blueshift"])
    chk("O3d (STRUCTURAL): the hold exceeds the local bulk's span, so the global bulk bears on it",
        d["v"] > d["g1_span"][1])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
