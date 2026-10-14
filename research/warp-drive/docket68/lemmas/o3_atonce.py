#!/usr/bin/env python3
"""o3_atonce.py -- Warp Theorem lemma O3 under M-RULINGS item 162: what holds IF the README is held at once.
Computed, READ and deduced; verified once (findings applied, O3-ATONCE.md History); not seated.  First headed "...
not verified; not seated" -- and first concluding "O3 DERIVED", which its verifier showed does not follow.

M's words (verbatim in the rulings file): item 162 "I submit that it may be more like a black hole, containing both
mouths and throat at once. The throat doesn't change size because the whole chain object only every takes on the size
that contains the README upon opening. It is and always will be only the size that is needed to hold the object once
and at once"; item 160; item 158 (2) "Exactly as long as the write needs  I should think"; 158 (1) "This is for the
math to decide, not myself"; 115 (c) "The README itself" (the opening's inflow is the README); 133 (one exact energy).

READ
  Margolus & Levitin, quant-ph/9710043: p.4, eq. (4), tau >= h/(4E), E above the ground state (p.3, footnote 2: the
    zero at the lowest allowed energy); p.5, achievable by (|0> + |2E>)/sqrt(2), which oscillates back after another
    h/(4E); p.9, an exact-energy eigenstate "never transitions to an orthogonal state"; App. B, achievability shown for
    "ordinary macroscopic" spectra.
  't Hooft, gr-qc/9310026, p.4, eq. (3).

  A1 (STRUCTURAL) the size that holds N bits once at 't Hooft's density is r0 = 2m -- G1, H1, G3 by construction.
  A2 A LOWER BOUND ONLY (READ).  Read as one collective orthogonal step (H-AT-ONCE-IS-ONE-ORTHOGONAL-STEP, the board's;
     158 (1) stays the math's), with E the energy above the register's ground (H-ML-ENERGY-IS-E, the board's choice of
     ground), Margolus-Levitin give hold >= h/(4E) = (2 pi^2/ln2)/N clocks, 1.0e-14 at the example README.  Their
     achieving state needs an energy spread E and a level at 2E -- against 133's one exact energy (an exact-energy
     state never turns orthogonal, p.9) and 162's fixed size (a level at 2E is an object of radius 4m) -- and it
     oscillates back, so it would not hold the README.  So h/(4E) is a floor, not the hold (H-WRITE-SATURATES-ML would
     be needed and conflicts with 133 and 162).
  A3 CARRIED OR TAKEN: A CONFLICT TO PUT TO M (deduced).  The gas bound (>= 2.0e5 clocks), the transfer bounds and
     opening.py O5's 4-clock floor bind a README carried in -- and 115 (c), with R0 and E1 as axioms.py words them
     ("takes the README as its inflow"), says it is carried.  Read as an instant, 162's "at once" leaves no time for
     that: a carrier arriving within ~1e-14 clocks brings at most ~2.8 bits (b4d_stage3.py C3).  The board's way
     through -- the README taken, not carried (H-TAKEN-NOT-CARRIED) -- runs against causality and no-signalling (the
     bits would have to correlate with a distant object without a carrier) and leaves only pre-loading, which is
     against 162's "upon opening".  The alternative reading of "at once" -- together, as one whole, not an instant --
     removes the conflict and keeps the gas bound.  This is M's to settle.
  A4 CONDITIONAL.  IF the README and E are present within 2m at the opening and the write saturates Margolus-Levitin,
     THEN the hold is ~1e-14 clocks and lies in the static window.  A floor alone cannot place it under the window's
     ceiling.
  A5 fixed size removes o3_readings.py's band-crossing mechanism only; a string at fixed mass is still unstable in 127's
     single-wall case -- what defuses it is a short lifetime, ~5e-16 e-folds over 1e-14 clocks, returning for ~20 clocks.
  A6 (STRUCTURAL) in a cone 5e-15 mass lengths deep any bulk C^2 at the plane matches its plane value to double precision
     (Padé [4/5], [5/5] of the order-20 series); it assumes eq. (17) on the plane across the cone through the hold
     (H-EQ17-ON-PLANE-THROUGH-HOLD), which b4d_stage3.py C5 leaves open.
  PLANCK CAVEAT  For E above the Planck energy h/(4E) is below the Planck time: the hold is 6.9e-51 s (1.3e-7 Planck
     times), the cone 1e-42 m.  Margolus-Levitin (non-relativistic, fixed background) and the classical bulk do not
     apply there; opening.py O5 already marks such figures as where "the model breaks down".
  VERDICT  O3 stays OPEN.  Banked: the conditional A4, and the conflict A3 -- 162's "at once" read as an instant against
     115 (c)'s README carried in -- which is M's.

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
    b4s = _load(os.path.join(HERE, "b4_static.py"), "o3a_b4series")
    depth = hold_ex / 2
    kcone = {rc: b4s.branch_and_K(rc, 20, [0.0, depth])["K"][1] for rc in ("201/100", "43/20", "3", "8")}
    return {"a1": a1_size(), "hold": hold, "hold_ex": hold_ex, "seconds": seconds, "v": v,
            "ratio": hold_ex / v, "ml_zero": zero, "ml_half": half,
            "s4": hold_ex / 4, "s5b": (1 + hold_ex / 8)**2, "depth": depth, "kcone": kcone}


def report(d):
    print("o3_atonce.py -- O3 under item 162: one object, fixed size, the README held at once\n")
    print("A1 (STRUCTURAL) N bits once at 't Hooft's density on r0 = 2m: n - N = %s" % d["a1"])
    print("A2 the write at once: hold = h/(4E) = %s clocks = %.3g clocks = %.2g s at the example README; ML's state "
          "reaches overlap %s at h/(4E) (half-way: %s)" % (d["hold"], d["hold_ex"], d["seconds"], d["ml_zero"],
                                                            d["ml_half"]))
    print("A6 the hold's cone reaches %.1e m into the bulk; K there vs on the plane: %s" % (d["depth"], ", ".join(
        "%s: %.6g/%.6g" % (rc, k[1], k[0]) for rc, k in d["kcone"].items())))
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
    chk("A2 (READ check): Margolus-Levitin's achieving state is orthogonal at h/(4E); half-way its overlap has modulus "
        "1/sqrt(2)", d["ml_zero"] == 0 and abs(complex(d["ml_half"])) > 0.7)
    chk("A2 (arithmetic): the floor h/(4E) = (2 pi^2/ln2)/N clocks -- 1.0e-14 clocks at the example README",
        sp.simplify(d["hold"] - 2 * sp.pi**2 / sp.log(2) / N) == 0 and 1.0e-14 < d["hold_ex"] < 1.1e-14)
    chk("A4 (conditional, arithmetic): IF the hold is the floor, it is ~1e-15 of the window's 11.28 clocks; O3c's "
        "relative changes there ~1e-15",
        10.5 < d["v"] < 12 and d["ratio"] < 1e-14 and d["s5b"] < 1 + 1e-14 and d["s4"] < 1e-14)
    chk("PLANCK CAVEAT: the floor in seconds, ~7e-51 s, is below a Planck time -- outside the domain of the physics used",
        1e-51 < d["seconds"] < 1e-50)
    chk("A6 (STRUCTURAL): in the hold's cone (~5e-15 m deep) K equals its value on the plane to 1e-12 at r = 2.01-8m, at most 1.39 "
        "-- STRUCTURAL (any C^2 bulk at that depth)", all(abs(k[1] / k[0] - 1) < 1e-12 for k in d["kcone"].values())
        and max(k[1] for k in d["kcone"].values()) < 1.4 and d["depth"] < 1e-14)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
