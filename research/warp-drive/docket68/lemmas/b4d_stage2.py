#!/usr/bin/env python3
"""b4d_stage2.py -- Warp Theorem lemma B4d, stage 2: the regime window.  Can the corridor's four-dimensional
relations (G1, G3, H1, which use Newton's G at the throat) and B4c's far model (H-FAR-MODEL: ell > 2 R_reach) hold
together?  Computed, READ and deduced; not verified; not seated.

M's words (verbatim in the rulings file): "Continue B4d as well please"; "Continue" (2026-10-08); item 133 (one exact
energy); item 136 answer 8 (k's scale: "leave it to measurement"); item 159 "test both options".

READ
  Maartens & Koyama, 1004.3962: p.9, eq. (27), RS 1-brane M5^3 = Mp^2/ell; p.29, eq. (164), for r << ell
    "V(r) ~ G ell M/r^2 = G5 M/r^2" and "the black hole is so small that it does not 'see' the brane, so that it is
    approximately a 5D Schwarzschild (static) solution"; p.28, eq. (163), the tidal-charge horizon
    r_h = GM [1 + sqrt(1 + 4 ell/(GM))]; p.11, table-top tests: "ell <~ 0.1 mm".
  Ishibashi & Kodama, hep-th/0305185, p.4, eq. (2.3): the (n+2)-dimensional Schwarzschild mass n M A_n/(8 pi G_{n+2}),
    r_h^(n-1) = 2M.
  Figueras & Wiseman, 1105.2558, p.3: "small (compared to ell) braneworld black holes behave like 5d asymptotically
    flat Schwarzschild black holes and large ones recover 4d behaviour".

  S1 THE HORIZON THE README'S ENERGY MAKES (computed from READ).  With G5 = G ell (MK eq. (164)) and m = G E/c^4:
     Tangherlini (IK eq. (2.3), n = 3): r_h^2 = (8/(3 pi)) m ell; MK's tidal form: r_h = m (1 + sqrt(1 + 4 ell/m)) ->
     2 sqrt(m ell).  Two independent forms, the same sqrt(m ell) scaling within a factor ~2.2 (the control); as
     ell -> 0 the tidal form gives 4D Schwarzschild's 2m (the control).
  S2 WHERE THE FOUR-DIMENSIONAL RELATIONS HOLD (computed).  G3 and H1 put the README's horizon at r0 = 2m.  By MK's
     tidal form that holds within 10% only for ell < 0.11 m (m the corridor's mass length) -- FW's "large ones recover
     4d behaviour"; for ell >> m the horizon is ~2 sqrt(m ell) >> 2m, a five-dimensional hole.
  S3 WHAT B4c ASKS (imported).  H-FAR-MODEL needs ell > 2 R_reach: 23 m for the static window's ~11.3 clocks (the hold
     before item 158), 4.0e5 m for the opening's >= 2.0e5 clocks.
  S4 THE WINDOW IS EMPTY (computed).  ell < 0.11 m and ell > 2 R_reach together need R_reach < 0.055 m -- a hold of
     under ~0.055 clocks.  Empty for the window hold (by a factor ~200) and for the opening (~3.6e6).  So the conflict
     predates item 158: the board's B4b and B4c were computed in the flat limit (ell >> r0) while G1/G3/H1 use 4D G at
     the throat -- what KSCALE.md already found from the far field ("Only r0 ~ ell is open").
  S5 IN PHYSICAL UNITS (computed).  At the example README m = G E/c^4 = 2.0e-28 m.  The 4D window needs
     ell < ~2e-29 m (~1.4e6 Planck lengths); B4c's far model needs ell > ~8e-23 m (window hold: ~4.5e-27 m).
     The table-top bound (ell <~ 1e-4 m) is an upper bound only, so measurement (B6', your 136 answer 8) can still
     put ell on either side.
  VERDICT  H-FAR-MODEL -- the board's reading, a single Randall-Sundrum plane with its far surface reaching ell/2 into
     the bulk -- cannot hold together with the corridor's four-dimensional relations at its own scale, for any hold
     longer than ~0.055 clocks.  M's rulings and the proved lemmas stand; the reading gives way: B4c's far model must be
     rebuilt for ell <~ r0, or the bulk must carry more than one plane (KSCALE (b), your 138).  Not decided here: a far
     surface for ell <~ r0 (stage 3) -- in this model any surface reaching R > ell/2 into the bulk is trapped over the
     throat, so it must hug the plane; whether one exists is open.

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
WINDOW_HOLD = 11.28                 # b4_static.py's verified hold (clocks)


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


def ell_4d(eps=sp.Rational(1, 10)):
    """The largest ell/m for which MK's tidal horizon stays within eps of 2m."""
    x = sp.Symbol("x", positive=True)
    return sp.solve(sp.Eq(1 + sp.sqrt(1 + 4 * x), 2 * (1 + eps)), x)[0]


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d2_o3write")
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "b4d2_exactE")
    T = ow._num(ow.t_min(3))
    tang, tidal = horizons()
    ratio_far = sp.limit(tidal / tang, ell, sp.oo)
    zero_limit = sp.limit(tidal, ell, 0)
    x4 = float(ell_4d())
    ell_far_window = 2 * WINDOW_HOLD
    ell_far_opening = 2 * (T + 2)
    E = ex.e_per_sqrt_bit() * math.sqrt(EXAMPLE_N)
    m_si = G_SI * E / C_SI**4
    rh_open = float(tang.subs({m: 1, ell: ell_far_opening}))
    return {"tang": tang, "tidal": tidal, "ratio_far": ratio_far, "zero_limit": zero_limit, "x4": x4,
            "reach_max": x4 / 2, "far_window": ell_far_window, "far_opening": ell_far_opening,
            "gap_window": ell_far_window / x4, "gap_opening": ell_far_opening / x4, "m_si": m_si,
            "ell4_si": x4 * m_si, "far_window_si": ell_far_window * m_si, "far_opening_si": ell_far_opening * m_si,
            "ell4_planck": x4 * m_si / L_PLANCK, "rh_open": rh_open, "T": T}


def report(d):
    print("b4d_stage2.py -- B4d stage 2: the regime window\n")
    print("S1 the README's horizon with G5 = G ell: Tangherlini %s; MK tidal %s (-> 2m as ell -> 0: %s); ratio at "
          "large ell %s = %.3f" % (d["tang"], d["tidal"], d["zero_limit"], d["ratio_far"], float(d["ratio_far"])))
    print("S2 G3/H1's horizon at 2m within 10%%: ell < %.4f m" % d["x4"])
    print("S3 H-FAR-MODEL: ell > %.1f m (window hold), %.3g m (opening)" % (d["far_window"], d["far_opening"]))
    print("S4 empty: needs R_reach < %.4f m; gaps x%.0f (window hold), x%.2g (opening); at the opening's ell the "
          "README's 5D horizon is %.0f m against 2 m" % (d["reach_max"], d["gap_window"], d["gap_opening"], d["rh_open"]))
    print("S5 example README: m = %.3g m; 4D window ell < %.2g m (%.2g Planck lengths); far model ell > %.2g m "
          "(window hold %.2g m); table-top ell < %.0e m" % (d["m_si"], d["ell4_si"], d["ell4_planck"],
                                                             d["far_opening_si"], d["far_window_si"], TABLETOP))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("S1: Tangherlini with G5 = G ell gives r_h = sqrt((8/(3 pi)) m ell)",
        sp.simplify(d["tang"] - sp.sqrt(8 * m * ell / (3 * sp.pi))) == 0)
    chk("S1 controls: MK's tidal horizon -> 2m (4D Schwarzschild) as ell -> 0, and shares Tangherlini's sqrt(m ell) "
        "scaling at large ell, within a factor ~2.2", sp.simplify(d["zero_limit"] - 2 * m) == 0
        and 2.0 < float(d["ratio_far"]) < 2.4)
    chk("S2: G3/H1's horizon at 2m holds within 10% only for ell < 0.11 m", abs(d["x4"] - 0.11) < 1e-9)
    chk("S3/S4: H-FAR-MODEL needs ell > 23 m (window hold) and 4.0e5 m (opening); against ell < 0.11 m the window is "
        "empty by ~200 and ~3.6e6", 22 < d["far_window"] < 23 and 3.9e5 < d["far_opening"] < 4.1e5
        and 190 < d["gap_window"] < 215 and 3.5e6 < d["gap_opening"] < 3.8e6)
    chk("S4: at the opening's ell the README's 5D horizon (~580 m) dwarfs r0 = 2 m", 550 < d["rh_open"] < 610)
    chk("S5: at the example README m ~ 2.0e-28 m; the 4D window needs ell ~< 2e-29 m, below the table-top bound, "
        "which bounds ell from above only", 1.9e-28 < d["m_si"] < 2.1e-28 and d["ell4_si"] < 3e-29
        and d["far_opening_si"] < TABLETOP)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
