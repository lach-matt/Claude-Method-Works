#!/usr/bin/env python3
"""globalbulk.py -- wall C, third piece: what the global bulk must do, for a held corridor and for a lasting one.

localbulk.py proved a local vacuum Randall-Sundrum bulk carrying the corridor exists; bulkseries.py computed it and put
its radius of convergence at the throat at ~0.73 r0 when ell = r0 and ~1.4 r0 when ell >> r0.  Two global questions
remain, and they part on M's item 136 E, the hold "Instantaneous or near instantaneous", and item 86 answer 5
(H-BRIEF-HOLD), "incredibly short, maybe even immeasurable but not zero".

  G1  a held corridor needs only the local bulk.  Finite propagation (standard, not READ: the Einstein equations in
      harmonic gauge are hyperbolic, and a region's development depends only on the data in its past domain of
      dependence).  Take a spacelike slice through the throat inside the local bulk, of radius delta in the bulk
      direction; the plane's points within ~delta/c of it in proper time lie in that slice's domain of dependence, so
      nothing in the global bulk can reach them.  With delta the series radius (bulkseries B5), the corridor's clock
      m/c (stability.py S3): a hold up to ~1.46 clocks (ell = r0) or ~2.8 clocks (ell >> r0) is decided by the local bulk
      alone -- about 1e-36 s at the board's example README.  An estimate of order, from a ratio test (H-DELTA-ORDER)
  G2  a LASTING static corridor -- eq. (17) on the whole plane, in a bulk that is Randall-Sundrum II far away with a
      compact non-linear core -- is excluded.  Computed: the corridor's own Weyl term at large r is r^2 E^th_th = -m/(4r),
      an ell-independent tail; a black hole on that bulk reads +2 ell^2 m/(3 r^3) (Maartens-Koyama eq. 155, READ in
      throatbulk.py).  Their ratio is -(3/8)(r/ell)^2: opposite in sign and unbounded as r grows.  Equivalently gamma =
      5/4 (kscale.py, CFM eq. 8) against gamma = 1 + O(ell^2/r^2) (MK p.26, eq. 41).  This holds at every r0, so
      KSCALE's way out (c), r0 ~ ell, does not survive for a lasting corridor: the far field is always at r >> ell.  That
      a compact non-linear core acts at r >> ell as a compact source in the linear theory is the board's extension of
      the READ linear results (H-COMPACT-CORE)
  G3  so the two readings of the hold part: under H-BRIEF-HOLD the global bulk does not bear on the corridor during the
      hold (G1); a lasting corridor needs a bulk whose departure from Randall-Sundrum is not compact -- reaching the
      bulk's far horizon, as the black string's does (MANYPLANES.md, Maartens p.19) -- and none such is built here
Imports throatbulk.py, kscale.py and stability.py's clock by path.  Stdlib + sympy.  python3 globalbulk.py [--selftest]
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

# bulkseries.py B5, measured by its ratio test (--inv-ell 1/2 --order 8; --flat --order 10); restated, not recomputed:
# a full run takes ~30 min.  Units of m (r0 = 2m).
DELTA_ELL_R0 = 1.46            # radius at the throat, ell = r0 (ratios 0.684, 0.686 per order)
DELTA_FLAT = 2.8               # radius at the throat, ell >> r0 (~1.4 r0)


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
    return {"clock_s": d["t_m"], "clocks_ell_r0": DELTA_ELL_R0, "clocks_flat": DELTA_FLAT,
            "hold_ell_r0_s": DELTA_ELL_R0 * d["t_m"], "hold_flat_s": DELTA_FLAT * d["t_m"]}


def compute():
    return {"g1": g1(), "g2": g2()}


def report(d):
    a, b = d["g1"], d["g2"]
    print("globalbulk.py -- wall C: the global bulk, for a held corridor and a lasting one\n")
    print("G1 a hold within the local bulk's domain of dependence: up to ~%.2f clocks (ell = r0) or ~%.1f (ell >> r0); "
          "clock %.2e s -> %.1e s or %.1e s at the example README (estimate)"
          % (a["clocks_ell_r0"], a["clocks_flat"], a["clock_s"], a["hold_ell_r0_s"], a["hold_flat_s"]))
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
    chk("G2: an RS II black hole's is +2 ell^2 m/(3 r^3) (MK eq. 155)", sp.simplify(b["lead_bh"] - 2 * ell**2 * m / 3) == 0)
    chk("G2: their ratio is -(3/8)(r/ell)^2 -- opposite sign, unbounded in r",
        sp.simplify(b["ratio"] + sp.Rational(3, 8) * r**2 / ell**2) == 0)
    chk("G2 control: the Schwarzschild member reads no Weyl term at all", b["schw"] == 0)
    chk("G2: gamma = 5/4 for the corridor against 1 for a plain mass (kscale.py)",
        b["gamma_corridor"] == sp.Rational(5, 4) and b["gamma_schw"] == 1)
    chk("G1 (STRUCTURAL, arithmetic on bulkseries B5): at the example README the local bulk decides a hold of ~1e-36 s",
        5e-37 < a["hold_ell_r0_s"] < a["hold_flat_s"] < 3e-36)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
