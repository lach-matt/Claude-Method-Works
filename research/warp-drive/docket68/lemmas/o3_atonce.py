#!/usr/bin/env python3
"""o3_atonce.py -- Warp Theorem lemma O3 under M-RULINGS item 162: one object, fixed size, the README held once and
at once.  Computed, READ and deduced; not verified; not seated.

M's words (verbatim in the rulings file): item 162 "I submit that it may be more like a black hole, containing both
mouths and throat at once. The throat doesn't change size because the whole chain object only every takes on the size
that contains the README upon opening. It is and always will be only the size that is needed to hold the object once
and at once"; item 160 "the corridor and the opening are the same object"; item 158 (2) "Exactly as long as the write
needs  I should think"; item 136 E "instantaneous or near instantaneous".

READ
  Margolus & Levitin, quant-ph/9710043: p.4, eq. (4), the time to an orthogonal state tau >= h/(4E), E the average
    energy above the ground state; p.5, "This bound is achievable if the spectrum of energies includes the energy 2E
    (and is very nearly achievable if the spectrum includes a value very close to this, as we would expect, for
    example, for any ordinary macroscopic system)", by (|0> + |2E>)/sqrt(2).
  't Hooft, gr-qc/9310026, p.4, eq. (3): n = 4 pi M^2/ln2 = A/(4 ln2) Boolean degrees of freedom.

  A1 THE SIZE NEEDED TO HOLD THE README ONCE IS r0 = 2m (STRUCTURAL).  The surface that holds N bits once, at 't Hooft's
     density, has A = 4 N ln2 Planck areas -- H1's 4 pi r0^2 = N A_bit -- and with G1's E its radius is 2m: G3.  So
     H-FIXED-SIZE is the board's r0 = 2m held from the opening on, and "containing both mouths and throat at once" is
     H2's horizon on the throat with 127's coinciding planes.  By G1's construction, not a finding.
  A2 THE WRITE AT ONCE (READ, deduced).  Under H-AT-ONCE the write is one collective step: the whole register goes from
     its state before the opening to the README's state, an orthogonal state.  Its least time is Margolus-Levitin's
     h/(4E), and that bound is achievable (p.5).  With 158 (2), the hold is that least time:
            hold = h/(4E) = (2 pi^2/ln2)/N clocks  -- 1.0e-14 clocks at the example README (6.9e-51 s).
     158 (1) is answered by 162: collective.
  A3 WHAT NO LONGER APPLIES (deduced).  The gas bound (O3-WRITE W3, >= 2.0e5 clocks) and the transfer-rate bounds
     (W2; quant-ph/0311049 eq. (26)) bound a README carried in by a signal or by matter (H-WRITE-IS-ARRIVAL).  Under 162
     the object takes the size that holds the README upon opening; the board reads this with R0 ("the corridor takes
     the README at its opening") as the README taken, not carried (H-TAKEN-NOT-CARRIED).  Those bounds then do not
     bind the hold.  The physics cost stays on record: no carrier that has not collapsed can bring N bits within 2m
     faster than W3's bound, so H-TAKEN-NOT-CARRIED is a statement about the corridor, not a delivery.
  A4 THE HOLD IS IN THE STATIC WINDOW (computed).  The window's bottom is now h/(4E) alone, and the hold sits on it --
     ~1e-15 of the static bulk's verified 11.28 clocks.  So H-HOLD-IN-WINDOW follows from 158 (2), 160, 162 and
     Margolus-Levitin; O3c's survival there is o3_hold.py's (linear theory, PROVED for every hold in the window).
  A5 FIXED SIZE (deduced).  No ramp of m(v): H-MASS-RISES fails, and with it o3_readings.py R3/R4 (b)'s mechanism (a
     string crossing the unstable band as its mass rises).  Within the hold's cone the bulk is the static bulk (B4b).
  VERDICT  Under 162 (with 158 (2), 160 and R0) O3 is DERIVED: the hold is Margolus-Levitin's least time for one
     collective step, inside the static window.  It rests on B4b for the bulk in the cone, and B4b's flat-limit regime
     is what b4d_stage2.py questions.  Not decided: how the object comes to hold the README at once -- the formation
     (B7, B4d), now an at-once appearance rather than an inflow.

Imports lemmas/o3_hold.py, lemmas/o3_write.py and lemmas/b4_static.py by path.  Stdlib + sympy.
python3 o3_atonce.py [--selftest]
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
CLOCK_PER_SQRT_BIT_S = 6.67430e-11 * 459404002.42356986 / 299792458.0**5   # G E/c^5 per sqrt(bit): exactE's E


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


def a1_size():
    """N bits at 't Hooft's density on a sphere of radius r0 = 2m, with m^2 = N ln2/(4 pi) (Planck units)."""
    N = sp.Symbol("N", positive=True)
    m2 = N * sp.log(2) / (4 * sp.pi)
    n = sp.simplify(4 * sp.pi * (2 * sp.sqrt(m2))**2 / (4 * sp.log(2)))     # A/(4 ln2)
    return sp.simplify(n - N)


def ml_two_level():
    """Margolus-Levitin's achieving state (|0> + |2E>)/sqrt(2): overlap after time t, in units h = 1."""
    E, t = sp.symbols("E t", positive=True)
    S = sp.Rational(1, 2) * (1 + sp.exp(-sp.I * 2 * sp.pi * 2 * E * t))
    return sp.simplify(S.subs(t, 1 / (4 * E))), sp.simplify(S.subs(t, 1 / (8 * E)))


def compute():
    o3 = _load(os.path.join(HERE, "o3_hold.py"), "o3a_o3hold")
    b4 = _load(os.path.join(HERE, "b4_static.py"), "o3a_b4static").compute(live=False)
    h_, c_, G_, N_ = sp.symbols("h c G N", positive=True)
    E = sp.sqrt(N_ * h_ * c_**5 * sp.log(2) / (8 * sp.pi**2 * G_))
    hold = sp.simplify((h_ / (4 * E)) / (G_ * E / c_**5))                   # clocks
    hold_ex = float(hold.subs(N_, EXAMPLE_N))
    seconds = hold_ex * CLOCK_PER_SQRT_BIT_S * math.sqrt(EXAMPLE_N)
    v = float(b4["cone"]["t_cert"])
    zero, half = ml_two_level()
    return {"a1": a1_size(), "hold": hold, "hold_ex": hold_ex, "seconds": seconds, "v": v,
            "ratio": hold_ex / v, "ml_zero": zero, "ml_half": half,
            "s4": hold_ex / 4, "s5b": (1 + hold_ex / 8)**2}


def report(d):
    print("o3_atonce.py -- O3 under item 162: one object, fixed size, the README held at once\n")
    print("A1 (STRUCTURAL) N bits once at 't Hooft's density on r0 = 2m: n - N = %s" % d["a1"])
    print("A2 the write at once: hold = h/(4E) = %s clocks = %.3g clocks = %.2g s at the example README; ML's state "
          "reaches overlap %s at h/(4E) (half-way: %s)" % (d["hold"], d["hold_ex"], d["seconds"], d["ml_zero"],
                                                            d["ml_half"]))
    print("A4 the static window holds %.2f clocks; the hold is %.2g of it; O3c factors S4 %.2g, S5b %.6f" %
          (d["v"], d["ratio"], d["s4"], d["s5b"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    N = sp.Symbol("N", positive=True)
    chk("A1 (STRUCTURAL, G1's construction): the size that holds N bits once at 't Hooft's density is r0 = 2m",
        d["a1"] == 0)
    chk("A2: Margolus-Levitin's achieving state is orthogonal at exactly h/(4E) and not before (control: overlap 1/2 "
        "in modulus half-way)", d["ml_zero"] == 0 and abs(complex(d["ml_half"])) > 0.7)
    chk("A2: the hold is h/(4E) = (2 pi^2/ln2)/N clocks -- 1.0e-14 clocks at the example README",
        sp.simplify(d["hold"] - 2 * sp.pi**2 / sp.log(2) / N) == 0 and 1.0e-14 < d["hold_ex"] < 1.1e-14)
    chk("A4: the hold sits inside the static window (~1e-15 of its 11.28 clocks); O3c's factors there are ~1",
        10.5 < d["v"] < 12 and d["ratio"] < 1e-14 and d["s5b"] < 1 + 1e-14 and d["s4"] < 1e-14)
    chk("A2 control: in seconds the hold is ~7e-51 s, far below a Planck time -- the README held at once",
        1e-51 < d["seconds"] < 1e-50)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
