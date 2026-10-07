#!/usr/bin/env python3
"""o3_hold.py -- Warp Theorem lemma O3: the hold's window in the corridor's clocks, and that the corridor survives it.

READ (through bulk/crossing.py, P-ML): Margolus & Levitin, quant-ph/9710043v2 -- at least h/(4E) to reach one orthogonal
state (eq. 4, p.4); energies of non-interacting subsystems add, and so do their rates (p.8); the bound is on orthogonal
states, NOT bits (p.2).

  O3a  THE HOLD'S LOWER BOUNDS (READ + computed).  Margolus-Levitin's eq. 4 applied to the whole register -- the README
       written onto the throat and horizons (H1, H2) as one system holding the one exact energy E (items 111 (b), 133)
       -- gives hold >= h/(4E) = (2 pi^2/ln2)/N clocks.  Bremermann's bound as Bekenstein states it (quant-ph/0311049,
       eq. (26), p.10: I-dot < 8 pi xi E/hbar log2 e, xi "of order a few"; READ) gives, for the N bits with the same E,
       hold >= 1/(2 xi) clocks (computed: E^2 is proportional to N, so the clocks are the same for every N).  Neither is
       an exact value: the first falls with N, the second carries xi
  O3a' THE PER-BIT FIGURE, WITHDRAWN AS THE HOLD.  First derived here: each of N holders flipped to an orthogonal state on
       its own share E/N (H-ONE-STEP-PER-BIT), eq. 4 per holder, hold >= hN/(4E) = 2 pi^2/ln2 = 28.4777 clocks for every
       N, and the hold equal to it (H-HOLD-AT-BOUND).  b4_static.py shows the bulk cannot carry that hold: with eq. (17)
       held on the plane, the hold's double cone reaches K = 2.3e4 and the static bulk's curvature singularity above the
       throat.  Both readings were the board's and were labelled "withdrawn if the mathematics refutes it"; they are
       withdrawn.  The figure is kept as a control (still computed exactly, and refuted).  What the refutation says of
       the write: the README's bits are not written as independent orthogonal flips each powered by E/N
  O3b  THE HOLD'S WINDOW (computed).  From below the READ bounds of O3a; from above the bulk -- b4_static.py certifies
       every hold shorter than 13.0 clocks regular (its whole double cone in the verified static bulk) and finds the
       curved layer reached from 15.9 clocks on.  The window [h/(4E), 13.0 clocks) is not empty: at the example README
       it runs from ~1e-14 clocks to 13.0 clocks = 8.6e-36 s, "instantaneous or near instantaneous" (136 E),
       "immeasurable but not zero" (86 answer 5).  The theorem needs no exact value of the hold, only that it lies there
  O3c  the corridor survives any hold in the window, in linear theory: at the window's top, v = 13.0 m of the horizon's
       advanced time, stability.py S4's exact rate changes the second derivative by v/(4m) = 3.25 times its natural
       size, and S5b's power-law blueshift is at most (1 + v/(8m))^2 = 6.89 for rays starting within m of the surface.
       Control: the non-extremal r0 = 1.8m member's exponential over the same v, e^(kappa v)
  O3d  the window's top, 13.0 clocks, still exceeds GLOBALBULK G1's local span (1.3-3.2 clocks): the hold is decided by
       the bulk beyond the local data, which is what b4_static.py computes
Imports copy/exactE.py, bulk/stability.py and lemmas/b4_static.py by path.  Stdlib + sympy.  python3 o3_hold.py [--selftest]
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
    v_bit = float(par)                                               # the per-bit figure, in units of m
    b4 = _load(os.path.join(HERE, "b4_static.py"), "o3_b4static").compute(live=False)
    v = round(b4["cone"]["t_cert"], 2)                               # the window's top
    st = _load(os.path.join(D68, "bulk", "stability.py"), "o3_stability")
    m = sp.Symbol("m", positive=True)
    c1, _ = st.D_derivatives(sp.Rational(9, 5) * m, 2 * m)            # control member's D'
    kappa_ctl = float((c1 / 2).subs(m, 1))
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "o3_exactE")
    E_ex = ex.e_per_sqrt_bit() * math.sqrt(EXAMPLE_N)
    G, C = 6.67430e-11, 299792458.0
    clock_s = G * E_ex / C**5
    h_, c_, G_, N_, xi = sp.symbols("h c G N xi", positive=True)
    E = sp.sqrt(N_ * h_ * c_**5 * sp.log(2) / (8 * sp.pi**2 * G_))
    clock = G_ * E / c_**5
    whole = sp.simplify((h_ / (4 * E)) / clock)
    transfer = sp.simplify((N_ * sp.log(2) * h_ / (2 * sp.pi) / (8 * sp.pi * xi * E)) / clock)   # N bits at eq. (26)
    return {"parallel": par, "sequential": seq, "v_bit": v_bit, "v": v, "whole": whole, "transfer": transfer,
            "t_fail_2": b4["cone"]["t_fail_2"], "Kmax_bit": b4["Kmax_o3"], "clock_s": clock_s,
            "hold_top_s": v * clock_s, "whole_example": float(whole.subs(N_, EXAMPLE_N)),
            "s4_growth": v / 4, "s5b_blueshift": (1 + v / 8) ** 2, "control_exp": math.exp(kappa_ctl * v),
            "kappa_ctl": kappa_ctl, "g1_span": (1.29, 3.16)}


def report(d):
    print("o3_hold.py -- Warp Theorem lemma O3: the hold\n")
    print("O3a whole register: hold >= h/(4E) = %s clocks (%.3g at the example README); transfer (eq. (26)): >= %s"
          % (d["whole"], d["whole_example"], d["transfer"]))
    print("O3a' the per-bit figure h N/(4E) = %s = %.4f clocks: withdrawn as the hold -- its cone reaches K = %.3g "
          "(b4_static.py)" % (d["parallel"], d["v_bit"], d["Kmax_bit"]))
    print("O3b the window: from the READ bounds up to %.2f clocks (= %.2e s at the example README); curved layer from "
          "%.2f" % (d["v"], d["hold_top_s"], d["t_fail_2"]))
    print("O3c at the window's top: S4 change %.2f x natural size; S5b blueshift <= %.2f; control e^(kappa v) = %.1f"
          % (d["s4_growth"], d["s5b_blueshift"], d["control_exp"]))
    print("O3d the window's top (%.1f clocks) exceeds G1's local span (%.2f-%.2f): the bulk decides it"
          % ((d["v"],) + d["g1_span"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    N_, xi = sp.symbols("N xi", positive=True)
    chk("O3a: whole register, hold >= h/(4E) = (2 pi^2/ln2)/N clocks; transfer bound (eq. (26)) >= 1/(2 xi) clocks",
        sp.simplify(d["whole"] - 2 * sp.pi**2 / sp.log(2) / N_) == 0 and sp.simplify(d["transfer"] - 1 / (2 * xi)) == 0)
    chk("O3a' control: the per-bit figure is h N/(4E) = 2 pi^2/ln2 = 28.48 clocks exactly (sequential: twice)",
        sp.simplify(d["parallel"] - 2 * sp.pi**2 / sp.log(2)) == 0 and sp.simplify(d["sequential"] - 2 * d["parallel"]) == 0)
    chk("O3a': the bulk refutes the per-bit hold -- its cone reaches K > 2e4 (b4_static.py)", d["Kmax_bit"] > 2e4)
    chk("O3b: the window is not empty -- READ lower bounds far below the bulk's certified 13.0 clocks; at the example "
        "README the top is ~8.6e-36 s, immeasurable, not zero", d["whole_example"] < 1e-10 and abs(d["v"] - 13.0) < 0.1
        and 1e-36 < d["hold_top_s"] < 1e-34 and d["v"] < d["t_fail_2"])
    chk("O3c: at the window's top S4 changes the second derivative by 3.25 natural sizes; S5b at most 6.89",
        abs(d["s4_growth"] - 3.25) < 1e-2 and abs(d["s5b_blueshift"] - 6.891) < 0.01)
    chk("O3c control: the non-extremal member's exponential over the same v exceeds the corridor's power law",
        d["control_exp"] > d["s5b_blueshift"])
    chk("O3d (STRUCTURAL): the window's top exceeds the local bulk's span, so the global bulk bears on it",
        d["v"] > d["g1_span"][1])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
