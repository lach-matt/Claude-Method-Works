#!/usr/bin/env python3
"""globalbulk.py -- wall C, third piece: what the global bulk must do, for a held corridor and for a lasting one.

First written with G1 as "the plane's points within ~delta/c of [a slice through the throat] in proper time", that the
global bulk "does not bear on the corridor during the hold", with the series radius copied in as constants, and with
G2 presenting MK eq. 155's coefficient as the RS II far field; the verifier showed static slices never reach the throat,
the boundary makes it an initial-boundary value problem, existence of an extension still matters, the constants broke
import-not-copy, and the coefficient is MK's loose form (GLOBALBULK.md History).

localbulk.py proved a local vacuum Randall-Sundrum bulk carrying the corridor exists; bulkseries.py computed it and
estimated its radius of convergence at the throat (B5).  Two global questions remain, and they part on M's item 136 E,
the hold "Instantaneous or near instantaneous", and item 86 answer 5 (H-BRIEF-HOLD), "incredibly short, maybe even
immeasurable but not zero".

  G1  a held corridor is decided by local data (an estimate of order, H-DELTA-ORDER; and H-IBVP, the board's: the plane
      is a timelike boundary carrying a junction condition, so finite propagation is used for an initial-boundary value
      problem, not the standard Cauchy one).  Stated invariantly: the part of the plane inside the five-dimensional
      domain of dependence of a slab of bulk data around the plane is determined by that slab alone.  Static slices
      never reach the throat (the proper radial distance diverges logarithmically there), so the slab lies on a
      non-static slice through the horizon, in stability.py's (v, rho) chart, and must span the plane laterally; its
      thickness delta(r) is known only at the throat.  There delta is the series radius (bulkseries.radius_estimates(),
      imported): 1.29-1.46m at ell = r0, 2.70-3.16m at ell >> r0.  In units of the corridor's clock m/c, measured along
      the (v, rho) chart's advanced time, that is a span of order one to three clocks -- about 1e-36 s at the example
      README, for ell >~ r0 only (under H-ONE-BIT-SCALE, ell << r0, it shrinks by about sqrt N; OPEN).  What G1 shows is
      that the hold's evolution does not depend on WHICH global extension exists; that SOME regular extension of the slab
      data exists is still needed for there to be a spacetime at all
  G2  a LASTING static corridor -- eq. (17) on the whole plane, in a bulk that is Randall-Sundrum II far away with a
      compact non-linear core, regular at the Poincare horizon -- is excluded.  Computed: the corridor's own Weyl term at
      large r is r^2 E^th_th = -m/(4r), an ell-independent tail.  A black hole on that bulk falls off as ell^2/r^3: in MK
      eq. (155)'s form (READ in throatbulk.py; MK place the eq. (41) correction in H only) +2 ell^2 m/(3 r^3), ratio
      -(3/8)(r/ell)^2; Garriga-Tanaka's full linear metric (not READ; the verifier's) gives +3 ell^2 m/r^3, ratio
      -(1/12)(r/ell)^2.  The robust content is the fall-off, 1/r against ell^2/r^3, unbounded in ratio as r grows; the
      coefficient and sign are not the RS II far field.  Equivalently gamma = 5/4 (kscale.py, CFM eq. 8) against
      gamma = 1 + O(ell^2/r^2) (MK eq. 41, p.10).  So KSCALE's way out (c), as eq. (17) on the whole plane, does not survive
      for a lasting corridor; its weaker form -- eq. (17) in the near zone only, matched to a gamma = 1 exterior -- is not
      addressed.  KSCALE's own "an ell-independent 1/r term. That bulk does not produce it" already held the argument.
      That a compact core acts at r >> ell as a compact source in the linear theory is the board's extension of the READ
      linear results (H-COMPACT-CORE, which includes regularity at the Poincare horizon)
  G3  so the two readings of the hold part: under H-BRIEF-HOLD the hold's evolution is local (G1); a lasting corridor
      needs a bulk whose departure from Randall-Sundrum is not compact -- reaching the bulk's far horizon, as the black
      string's does (MANYPLANES.md, Maartens p.19) -- and none such is built here.  CENSOR5D.md's Theorem W binds the
      whole spacetime however brief the hold, so G1's locality is about the hold's dynamics only; such a departure is
      its escape (b)
Imports throatbulk.py, kscale.py, bulkseries.py and stability.py's clock by path.  Stdlib + sympy.  python3 globalbulk.py [--selftest]
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


def g2():
    tb = _load(os.path.join(HERE, "throatbulk.py"), "gb_throatbulk")
    r, m, ell = tb.r, tb.m, tb.ell
    F, H = tb.FH(2 * m)
    Eth_corr = sp.simplify(tb.E_mk(F, H)[2])
    lead_corr = sp.limit(Eth_corr * r, r, sp.oo)                    # coefficient of 1/r
    Eth_bh = tb.t6()["Eth_big"]                                     # MK eq. 155's black hole, through ell^2
    lead_bh = sp.limit(Eth_bh * r**3, r, sp.oo)                     # coefficient of 1/r^3
    ratio = sp.simplify((lead_corr / r) / (lead_bh / r**3))
    schw = sp.simplify(tb.E_mk(1 - 2 * m / r, 1 - 2 * m / r)[2])    # control: the Schwarzschild member reads 0
    ks = _load(os.path.join(HERE, "kscale.py"), "gb_kscale")
    fp = ks.fingerprint()
    return {"lead_corr": lead_corr, "lead_bh": lead_bh, "ratio": ratio, "schw": schw,
            "gamma_corridor": fp["floor"]["gamma"], "gamma_schw": fp["schw"]["gamma"]}


def g1():
    st = _load(os.path.join(HERE, "stability.py"), "gb_stability")
    d = st.compute()
    be = _load(os.path.join(HERE, "bulkseries.py"), "gb_bulkseries").radius_estimates()
    lo, hi = be["ell_r0_radius_root"], be["flat_radius_range"][1]
    return {"clock_s": d["t_m"], "delta_ell_r0": (be["ell_r0_radius_root"], be["ell_r0_radius_ratio"]),
            "delta_flat": be["flat_radius_range"], "hold_lo_s": lo * d["t_m"], "hold_hi_s": hi * d["t_m"]}


def compute():
    return {"g1": g1(), "g2": g2()}


def report(d):
    a, b = d["g1"], d["g2"]
    print("globalbulk.py -- wall C: the global bulk, for a held corridor and a lasting one\n")
    print("G1 slab thickness at the throat (bulkseries B5): %.2f-%.2f m (ell = r0), %.2f-%.2f m (ell >> r0); clock %.2e s "
          "-> a span of %.1e to %.1e s at the example README, ell >~ r0 (estimate)"
          % (a["delta_ell_r0"] + a["delta_flat"] + (a["clock_s"], a["hold_lo_s"], a["hold_hi_s"])))
    print("G2 far-field Weyl term r^2 E^th_th: corridor %s/r; RS II black hole (MK 155) %s/r^3; ratio %s; "
          "control Schwarzschild member %s" % (b["lead_corr"], b["lead_bh"], b["ratio"], b["schw"]))
    print("   gamma: corridor %s, plain mass %s; RS II far field 1 + O(ell^2/r^2)" % (b["gamma_corridor"], b["gamma_schw"]))
    print("G3 held corridor: the global bulk does not bear on it; lasting corridor: needs a non-compact departure from RS")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b = d["g1"], d["g2"]
    m, ell, r = sp.symbols("m ell r", positive=True)
    chk("G2: the corridor's far-field Weyl term is -m/(4r), independent of ell", sp.simplify(b["lead_corr"] + m / 4) == 0)
    chk("G2: MK eq. 155's black hole reads +2 ell^2 m/(3 r^3) -- an ell^2/r^3 fall-off (MK's form, not the full RS II field)", sp.simplify(b["lead_bh"] - 2 * ell**2 * m / 3) == 0)
    chk("G2: their ratio is -(3/8)(r/ell)^2 in MK's form -- unbounded in r (the fall-off is the robust part)",
        sp.simplify(b["ratio"] + sp.Rational(3, 8) * r**2 / ell**2) == 0)
    chk("G2 control: the Schwarzschild member reads no Weyl term at all", b["schw"] == 0)
    chk("G2: gamma = 5/4 for the corridor against 1 for a plain mass (kscale.py)",
        b["gamma_corridor"] == sp.Rational(5, 4) and b["gamma_schw"] == 1)
    chk("G1 (STRUCTURAL, arithmetic on bulkseries.radius_estimates(), imported): a span of ~1e-36 s at the example README",
        5e-37 < a["hold_lo_s"] < a["hold_hi_s"] < 3e-36)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
