#!/usr/bin/env python3
"""b4d_stage3.py -- Warp Theorem lemma B4d, stage 3: the opening at once (M-RULINGS item 162).  Computed and deduced;
not verified; not seated.

M's words (verbatim in the rulings file): item 162 "... the whole chain object only every takes on the size that
contains the README upon opening. It is and always will be only the size that is needed to hold the object once and
at once"; item 160 "the corridor and the opening are the same object"; item 115 (c) "The README itself" (the opening's
inflow is the README); item 136 G (the README is the energy); item 122 (3) (position 2's side the time-reverse of
position 1's).

  C1 CAUSALITY (deduced).  The hold is h/(4E) ~ 1e-14 clocks (o3_atonce.py).  Nothing reaches the throat from farther
     than (2 + 1e-14) m in that time, so at the opening the one energy E is already within that radius, or arrives
     there in one instant of advanced time.
  C2 ENERGY AT ONCE: A THIN SHELL (computed).  Ingoing Vaidya with a step, m(v) = m H(v) (opening.py's form, its O1
     energy conditions met as m rises): before v = 0 flat, after it Schwarzschild of mass m; the apparent horizon
     r = 2 m(v) appears at r = 2m at the instant v = 0 -- the size set at once, never grown (162's fixed size).  A null
     shell from any distance arrives at the throat in one instant of v, so the energy can arrive at once.
  C3 THE README CANNOT RIDE IT (computed, from o3_write.py's gas bound).  A carrier arriving within a hold of T clocks
     brings at most N <= 8 Z (T + 2)^3/(3645 ln2) bits.  At T ~ 1e-14 that is ~2.8 bits at Z = 108.75.  So for any
     README above a few bits, an instant and an inflow carrying the README cannot both hold -- the conflict, not a
     forcing of H-TAKEN-NOT-CARRIED (regraded after o3_atonce.py's verifier: that reading runs against causality and
     was circular with o3_atonce.py).  115 (c) and 136 G -- the inflow is the README, the
     README is the energy -- then read as the README's ENERGY arriving at once and its INFORMATION taken (R0); the board
     names that split H-ENERGY-CARRIED-INFO-TAKEN, a reading of M's words to be put to M.
  C4 NO TIME FOR THE STRING'S INSTABILITY (computed).  Over the hold the black string's fastest growth (0.046 per
     clock, o3_readings.py) gives ~5e-16 e-folds; with no ramp (162) there is no band-crossing either.  The instability
     that refuted the long opening has no time to act.
  C5 WHAT STAYS OPEN (deduced).  After the shell the plane is Schwarzschild (opening.py O3: "The Vaidya pieces end in
     Schwarzschild ... not in the corridor"); the corridor is eq. (17).  Within the hold's cone the bulk is eq. (17)'s
     static bulk (o3_atonce.py A6); beyond it, the prior state.  The two must join across the cone's null boundary as
     a null shell carrying non-negative energy (Barrabes-Israel, not READ here) -- the junction between eq. (17)'s
     static bulk and the shell's spacetime is B4d's next computation (stage 4).  And the closing, by 122 (3), is the
     opening run backwards: an outgoing shell at position 2.

Imports lemmas/o3_write.py and lemmas/o3_readings.py by path.  Stdlib + sympy + scipy.  python3 b4d_stage3.py [--selftest]
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
Z_HEAD = 108.75


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


def vaidya_step():
    """Ingoing Vaidya, m(v) = m H(v): apparent horizon radius r = 2 m(v) just before and just after v = 0, and the
    only nonzero Einstein component G_vv = 2 m'(v)/r^2 (a delta at v = 0, positive for a rising step)."""
    v = sp.Symbol("v", real=True)
    r, m = sp.symbols("r m", positive=True)
    mv = m * sp.Heaviside(v)
    ah_before = 2 * mv.subs(v, -sp.Rational(1, 10**20))
    ah_after = 2 * mv.subs(v, sp.Rational(1, 10**20))
    Gvv = 2 * sp.diff(mv, v) / r**2
    return ah_before, ah_after, sp.simplify(Gvv), m, v, r


def bits_carried(T, Z=Z_HEAD):
    """Invert o3_write.py's gas bound T >= (3645 ln2 N/(8Z))^(1/3) - 2 for N."""
    return 8 * Z * (T + 2) ** 3 / (3645 * math.log(2))


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d3_o3write")
    orr = _load(os.path.join(HERE, "o3_readings.py"), "b4d3_readings")
    N_ = sp.Symbol("N", positive=True)
    hold = float(2 * sp.pi**2 / sp.log(2) / EXAMPLE_N)                   # o3_atonce.py's h/(4E) in clocks
    rate = orr.growth(0.35, lo=0.05, hi=0.12, n=8) / 2
    t3 = ow.t_min(3)
    ab, aa, G, m, v, r = vaidya_step()
    return {"hold": hold, "carried": bits_carried(hold), "carried_ctl": bits_carried(ow._num(t3)),
            "efolds": rate * hold, "rate": rate, "ah_before": ab, "ah_after": aa, "Gvv": G, "m": m, "v": v, "r": r}


def report(d):
    print("b4d_stage3.py -- B4d stage 3: the opening at once\n")
    print("C1 the hold %.2e clocks: E within (2 + %.0e) m at the opening" % (d["hold"], d["hold"]))
    print("C2 Vaidya step: apparent horizon %s before, %s after v = 0; G_vv = %s" % (d["ah_before"], d["ah_after"],
                                                                               d["Gvv"]))
    print("C3 a carrier arriving within the hold brings at most %.2f bits (control: within the gas-bound time, %.3g = "
          "the example README)" % (d["carried"], d["carried_ctl"]))
    print("C4 the string's growth over the hold: %.1e e-folds (rate %.4f per clock)" % (d["efolds"], d["rate"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("C2: in a Vaidya step the apparent horizon is absent before v = 0 and at r = 2m just after -- the size set at "
        "once; G_vv is a positive delta at the step", d["ah_before"] == 0 and sp.simplify(d["ah_after"] - 2 * d["m"]) == 0
        and sp.simplify(d["Gvv"] - 2 * d["m"] * sp.DiracDelta(d["v"]) / d["r"]**2) == 0)
    chk("C3: a carrier arriving within the hold brings at most ~2.8 bits; control: inverting the gas bound at its own "
        "time recovers the example README", 2.5 < d["carried"] < 3.0 and abs(d["carried_ctl"] / EXAMPLE_N - 1) < 1e-6)
    chk("C4: the string's growth over the hold is below 1e-15 e-folds", d["efolds"] < 1e-15 and 0.045 < d["rate"] < 0.047)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
