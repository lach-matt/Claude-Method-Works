#!/usr/bin/env python3
"""b4d_stage2.py -- Warp Theorem lemma B4d, stage 2: the regime window.  Can the corridor's four-dimensional readings
and B4c's far model hold together?  Computed, READ and deduced; verified once (findings applied, B4D-STAGE2.md
History); not seated.  First headed "... not verified; not seated" -- and first concluding that H-FAR-MODEL gives way,
which its verifier showed rests on a round far surface.

M's words (verbatim in the rulings file): "Continue B4d as well please"; "Continue" (2026-10-08); item 133 (one exact
energy); item 136 answer 8 (k's scale: "leave it to measurement"); items 160-162 (the corridor is the opening; one
object of fixed size, holding the README at once).

READ
  Maartens & Koyama, 1004.3962: p.9, eq. (27), M5^3 = Mp^2/ell (with eq. (3)'s kappa^2 = 8 pi G: G5 = G ell); p.29,
    eq. (164), for r << ell "V(r) ~ G ell M/r^2 = G5 M/r^2" (order of magnitude) and "approximately a 5D Schwarzschild
    (static) solution"; p.28, eq. (163), the tidal-charge horizon (its Q = -2M from the r << ell limit; "cannot
    describe the end-state of collapse"); p.11, table-top "ell <~ 0.1 mm".
  Ishibashi & Kodama, hep-th/0305185, p.4, eq. (2.3).  Figueras & Wiseman, 1105.2558: p.3, small holes 5d, "large ones
    recover 4d behaviour"; p.4, the plane Ricci-flat "with corrections going as O(ell^2/R4^2)".

  S1 THE README'S ENERGY AS BRANE MATTER (deduced from READ normalisation).  Under H-BRANE-MATTER (the README's E
     gravitates as matter on a single RS II plane, statically -- an unnamed premise of the first draft) with G5 = G ell:
     a 5D hole of radius r_h^2 = (8/(3 pi)) m ell (IK eq. (2.3); convention-independent).  MK's tidal form scales the
     same way (a consistency check, not an independent control: both rest on MK eq. (40)); its ell -> 0 limit 2m is
     STRUCTURAL.
  S2 WHERE THE 4D READINGS HOLD (deduced, order of magnitude).  FW: 4D behaviour for R4 >~ ell, corrections
     O(ell^2/R4^2); so r0 >~ ell -- ell <~ 0.6 m for a 10% correction with an O(1) coefficient.  No READ threshold.
  S3 WHAT B4c ASKS -- ONLY FOR A ROUND T (computed, b4_global.py).  A round far surface needs ell > 2 R_reach; a tipped
     one does not: at ell = 0.11 m a tipped T enclosing the reach is untrapped (b4_global.tipped_far_boundary).
  S4 THE WINDOW IS EMPTY ONLY FOR A ROUND T (computed).  With a round T: ell > 2 R_reach >= 2 (2m) against ell <~ 0.6m
     -- empty for every hold, the conflict predating item 158.  With a tipped T: not shown empty.  And even with a
     round T the inconsistent set is {round-T H-FAR-MODEL, H-RS2-ONE-PLANE, H-STATIC, H-BRANE-MATTER, and the board's 4D
     readings H-EXACT-ENERGY-AT-BOUND / H-PULL-IS-COST / the 4D bit area} -- which member yields is a choice, not forced.
     G3 and H1 are definitions (exactE.py STRUCTURAL) and cannot conflict.
  S5 IN PHYSICAL UNITS (computed).  At the example README m = GE/c^4 = 2.0e-28 m; ell <~ 0.6m is ~1.2e-28 m; a round T
     would need ell > 7.9e-23 m through the old opening, 4.5e-27 m through the old window; table-top ell <~ 1e-4 m
     (upper bound only).
  VERDICT  The regime window is not shown empty: its upper side is a round-T statement.  KSCALE.md, read correctly,
     already closes a STATIC corridor on ONE RS II plane at every ell (gamma = 1 for r0 >> ell; 5D at r0 << ell) -- the
     pressure is on H-RS2-ONE-PLANE and H-STATIC-CORRIDOR, with KSCALE's own way out (a): a corridor that is not
     static -- which items 160-162 give (a hold of h/(4E), o3_atonce.py).  No B4 status moves on this stage's account.

Imports lemmas/o3_write.py and copy/exactE.py by path.  Stdlib + sympy.  python3 b4d_stage2.py [--selftest]
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
G_SI, C_SI = 6.67430e-11, 299792458.0
L_PLANCK = 1.616255e-35
TABLETOP = 1e-4                     # MK p.11: ell <~ 0.1 mm


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


m, ell = sp.symbols("m ell", positive=True)


def horizons():
    """Tangherlini with G5 = G ell (IK eq. (2.3) at n = 3: mass = 3 pi r_h^2/(8 G5)); MK's tidal form eq. (163)."""
    rh = sp.Symbol("r_h", positive=True)
    tang = sp.solve(sp.Eq(3 * sp.pi * rh**2 / (8 * ell), m), rh)[0]           # G = 1 units: E -> m
    tidal = m * (1 + sp.sqrt(1 + 4 * ell / m))
    return tang, tidal


def ell_4d(eps=0.1, coeff=1.0):
    """FW: corrections O(ell^2/R4^2) with R4 = r0 = 2m; an O(1) coefficient: ell/m below 2 sqrt(eps/coeff)."""
    return 2 * math.sqrt(eps / coeff)


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d2_o3write")
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "b4d2_exactE")
    gl = _load(os.path.join(HERE, "b4_global.py"), "b4d2_global")
    b4 = _load(os.path.join(HERE, "b4_static.py"), "b4d2_static").compute(live=False)
    window = float(b4["cone"]["t_cert"])
    T = ow._num(ow.t_min(3))
    tang, tidal = horizons()
    ratio_far = sp.limit(tidal / tang, ell, sp.oo)
    zero_limit = sp.limit(tidal, ell, 0)
    x4 = ell_4d()
    far_window, far_opening = 2 * (window + 2), 2 * (T + 2)           # one convention: R_reach = (2 + hold) m
    tipped = gl.tipped_far_boundary(sp.Rational(11, 100), 24, 2.4e4)
    round_ctl = gl.far_boundary()["min"](0.11, 24.0, 2.0)
    E = ex.e_per_sqrt_bit() * math.sqrt(EXAMPLE_N)
    m_si = G_SI * E / C_SI**4
    return {"tang": tang, "tidal": tidal, "ratio_far": ratio_far, "zero_limit": zero_limit, "x4": x4,
            "far_window": far_window, "far_opening": far_opening, "far_zero": 2 * 2.0, "window": window,
            "tipped": tipped, "round_ctl": round_ctl, "m_si": m_si, "ell4_si": x4 * m_si,
            "far_window_si": far_window * m_si, "far_opening_si": far_opening * m_si, "T": T}


def report(d):
    print("b4d_stage2.py -- B4d stage 2: the regime window\n")
    print("S1 under H-BRANE-MATTER, G5 = G ell: r_h = %s; MK tidal %s (consistency ratio at large ell %.3f; ell -> 0: %s)"
          % (d["tang"], d["tidal"], float(d["ratio_far"]), d["zero_limit"]))
    print("S2 4D readings at the throat (FW, O(ell^2/r0^2), O(1) coefficient, 10%%): ell <~ %.2f m" % d["x4"])
    print("S3 a round T needs ell > 2 R_reach: %.1f m at a zero hold, %.1f m (window), %.3g m (old opening); a tipped T "
          "at ell = 0.11m: min theta+ %+.3f, distance %.1f (a round T there: %+.3f)"
          % (d["far_zero"], d["far_window"], d["far_opening"], d["tipped"][0], d["tipped"][1], d["round_ctl"]))
    print("S5 m = %.3g m; ell <~ %.2g m; round T ell > %.2g m (old opening), %.2g m (window); table-top < %.0e m"
          % (d["m_si"], d["ell4_si"], d["far_opening_si"], d["far_window_si"], TABLETOP))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("S1 (deduced): under H-BRANE-MATTER, Tangherlini with G5 = G ell gives r_h = sqrt((8/(3 pi)) m ell); MK's tidal "
        "form shares the scaling (consistency ratio ~2.17)", sp.simplify(d["tang"] - sp.sqrt(8 * m * ell / (3 * sp.pi))) == 0
        and 2.1 < float(d["ratio_far"]) < 2.2)
    chk("S1 (STRUCTURAL, by construction): MK's tidal horizon -> 2m as ell -> 0", sp.simplify(d["zero_limit"] - 2 * m) == 0)
    chk("S3: a round T needs ell > 2 R_reach (>= 4m even at a zero hold), but a tipped T enclosing the reach is untrapped "
        "at ell = 0.11m where a round one is trapped -- the window is empty only for a round T",
        d["far_zero"] > d["x4"] and d["tipped"][0] > 0 and d["tipped"][1] > 22.6 and d["round_ctl"] < 0)
    chk("S5 (arithmetic): m ~ 2.0e-28 m at the example README; the table-top bound is above every figure here",
        1.9e-28 < d["m_si"] < 2.1e-28 and d["far_opening_si"] < TABLETOP)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
