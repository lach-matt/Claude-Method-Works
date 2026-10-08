#!/usr/bin/env python3
"""b4d_stage1.py -- Warp Theorem lemma B4d, stage 1: what bulk can stand through the write.  Computed, READ and
deduced; not verified; not seated.

M's words (verbatim in the rulings file): "Continue B4d as well please" (2026-10-08); item 157 "we already have at
least half the model, our current universe"; items 117/120 (null energy at every point; Z3); item 127 (1) "yes" (the
planes coincide); item 138 (the bulk is multi-universal); item 141 (the planes are static); item 159 "test both
options".

READ
  Ishibashi & Kodama, hep-th/0305185, p.16 (Summary): "higher-dimensional Schwarzschild black holes are stable with
    respect to all tensorial types of linear perturbations"; p.6, kappa = (n - 1)/(2 r_h).
  Figueras & Wiseman, 1105.2558, p.1 (abstract): static Randall-Sundrum II black holes constructed for brane radius
    R4/ell in [0.07, 20], "dynamically stable for axisymmetric perturbations for all radii"; p.3 (Fig. 1): "small
    (compared to ell) braneworld black holes behave like 5d asymptotically flat Schwarzschild black holes and large ones
    recover 4d behaviour"; p.4: the horizon "has too little extent into the bulk to experience a Gregory-Laflamme type
    instability".
  Gregory, hep-th/0004101, p.7: "very small mass black holes are roughly hyperspherical ... look like a five-dimensional
    black hole"; Gregory & Laflamme, hep-th/9301052, pp.8-9: the string is "stabilized if the extra dimensions are
    compactified to a scale smaller than the minimum wavelength for which instability occurs".

  D1 THE REGIME (computed).  B4c's far model (H-FAR-MODEL, b4_global.py) needs ell > 2 R_reach.  Through the write
     the reach is the write's (o3_write.py: 2.0e5 clocks at the example README), so ell > 4.0e5 m: ell/r0 > 2e5.  The
     corridor sits deep in the flat limit, where gravity at its scale is five-dimensional.
  D2 ONE PLANE: WHAT CAN STAND (computed and READ).  Three candidates the board can name:
     - the black string (the Vaidya opening's bulk): Gregory-Laflamme unstable, o3_readings.py -- ends in a naked
       singularity (Lehner-Pretorius, READ);
     - eq. (17)'s static bulk: its singular surface by ~18 clocks (b4_static.py);
     - the localized black hole: in this regime the Z2-cut 5D Schwarzschild hole (Gregory p.7; Figueras-Wiseman's small
       limit), stable (Ishibashi-Kodama).  Its plane slice is computed here: g_tt = -(1 - r_h^2/r^2), no 1/r term (a 5D
       potential); surface gravity 1/r_h, not 0; areal radius monotonic outside the horizon -- no throat.  It stands,
       and it is not the corridor: O2 (extremal) fails on it, and so does eq. (17)'s 1/r tail.
  D3 A CLOSING PLANE BELOW THE SINGULAR SURFACE (computed).  One of 138's planes at y_w, closing the bulk under Z2,
     would cut eq. (17)'s static bulk off below its singular surface and switch the string's instability off.  The
     Israel condition fixes the matter that plane must carry from the static bulk's own extrinsic curvature at y_w
     (b4_static.py's exact series, Padé in y^2, two orders).  In units 2/kappa^2: rho + p_r = -A_y/(2A) + B_y/(2B).
     It is negative at every r from 2.1m to 6m and every y_w from 0.25m to 2.3m -- the closing plane needs matter that
     breaks the null energy condition, which your 117/120 forbid at every point (Z3).  Controls: the RS1 second brane
     comes out at negative tension with rho + p = 0 exactly; a closing plane on the flat-limit black string carries
     nothing.
  D4 THE SLAB FOR THE STRING (computed and deduced).  The same plane on the Vaidya opening's black string costs nothing
     (D3's control) and switches the instability off when y_w < pi r+/mu_c = 3.59 r+ (o3_readings.py's mu_c; GL
     pp.8-9).  Early in the opening r+ is small: the hole there is a localized 5D hole in the slab (stable, READ), and
     it becomes a string once it spans the slab -- the board's reading of the slab's phases (H-SLAB-PHASES, not READ).
     The end of that opening is a black string, Schwarzschild on the plane at r >> y_w -- non-extremal, not eq. (17).
  VERDICT  Through the write, every bulk the board can show standing is a black hole or a black string; none is
     eq. (17)'s extremal corridor.  The corridor's own static bulk can be closed below its singular surface only by a
     plane breaking the null energy condition, which your rulings forbid.  Not decided here: a plane with bulk on both
     sides (H-TWO-SIDED); finite ell (B6', nature's), which the far model now excludes unless B4c's reading changes.

Imports o3_write.py, o3_readings.py, b4_static.py by path.  numpy, scipy, sympy, mpmath, python-flint.
python3 b4d_stage1.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
WALL_R = ["21/10", "43/20", "9/4", "5/2", "3", "4", "6"]
WALL_Y = [0.25, 0.5, 1.0, 1.5, 2.0, 2.3]
ORDER = 40


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


def tangherlini_slice():
    """The Z2-cut 5D Schwarzschild hole: its slice through the plane (the equator of S^3), surface gravity, and
    whether the plane's areal radius has a minimum outside the horizon."""
    r, rh = sp.symbols("r r_h", positive=True)
    f = 1 - rh**2 / r**2
    kappa = sp.simplify(sp.diff(f, r).subs(r, rh) / 2)
    one_over_r = sp.limit(r * (f - 1 + rh**2 / r**2), r, sp.oo)        # coefficient of 1/r in g_tt
    tail = sp.series(f, r, sp.oo, 3).removeO()
    throat = sp.solve(sp.Eq(sp.diff(r, r), 0), r)                        # areal radius r: d(r)/dr never 0
    return {"f": f, "kappa": kappa, "one_over_r": one_over_r, "tail": tail, "throat": throat}


def wall_stress(b4, rc, ys, N=ORDER):
    """Israel stress of a Z2 plane at y = y_w closing eq. (17)'s static bulk (bulk below; normal -d_y), in units
    2/kappa^2: S^mu_nu = -(K^mu_nu - K delta), K^mu_nu = -(1/2) h^-1 dh/dy.  Two Padé orders."""
    S = b4.series(rc, N)
    n = N // 2
    out = []
    for o in [(n // 2 - 1, n // 2), (n // 2, n // 2)]:
        F = {X: b4.pade(S[X][0][0::2], *o) for X in "ABC"}

        def ev(X, y):
            p, q = F[X]
            s = y * y
            return (mp.polyval([mp.mpf(v.numerator) / v.denominator for v in reversed(p)], s)
                    / mp.polyval([mp.mpf(v.numerator) / v.denominator for v in reversed(q)], s))
        row = []
        for yw in ys:
            y = mp.mpf(yw)
            h = {X: ev(X, y) for X in "ABC"}
            d = {X: mp.diff(lambda t, X=X: ev(X, t), y) for X in "ABC"}
            Kt, Kr, Kq = (-d[X] / (2 * h[X]) for X in "ABC")
            K = Kt + Kr + 2 * Kq
            rho, pr, pq = Kt - K, -(Kr - K), -(Kq - K)
            row.append({"y": yw, "rho": float(rho), "pr": float(pr), "pq": float(pq), "nec_r": float(rho + pr),
                        "nec_q": float(rho + pq)})
        out.append(row)
    return out


def rs_control():
    """RS1's second brane: h = e^(-2y/ell) eta at y = y_w, bulk below: negative tension, rho + p = 0."""
    y, ell = sp.symbols("y ell", positive=True)
    h = sp.exp(-2 * y / ell)
    K1 = -sp.diff(h, y) / (2 * h)
    K = 4 * K1
    rho, p = sp.simplify(K1 - K), sp.simplify(-(K1 - K))
    return rho, p


def string_control():
    """The flat-limit black string: h independent of y, so a closing plane carries nothing."""
    r, y, m = sp.symbols("r y m", positive=True)
    hs = [1 - 2 * m / r, 1 / (1 - 2 * m / r), r**2]
    return [sp.simplify(sp.diff(x, y)) for x in hs]


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d_o3write")
    orr = _load(os.path.join(HERE, "o3_readings.py"), "b4d_readings")
    b4 = _load(os.path.join(HERE, "b4_static.py"), "b4d_b4static")
    T = ow._num(ow.t_min(3))
    m1, m2 = 0.86, 0.865
    o1, o2 = orr.growth(m1, lo=1e-4, hi=0.01, n=30), orr.growth(m2, lo=1e-4, hi=0.01, n=30)
    mu_c = m2 + o2 * (m2 - m1) / (o1 - o2)
    walls = {rc: wall_stress(b4, rc, WALL_Y) for rc in WALL_R}
    pade_gap = max(abs(a["nec_r"] - b["nec_r"]) for w in walls.values() for a, b in zip(*w))
    nec_r = {rc: [c["nec_r"] for c in w[1]] for rc, w in walls.items()}
    every_fails = all(v < 0 for vals in nec_r.values() for v in vals)
    rho_c, p_c = rs_control()
    return {"T": T, "ell_min": 2 * T, "ratio": T, "tang": tangherlini_slice(), "mu_c": mu_c,
            "slab": math.pi / mu_c, "walls": walls, "nec_r": nec_r, "every_fails": every_fails, "pade_gap": pade_gap,
            "rs": (rho_c, p_c), "string": string_control()}


def report(d):
    print("b4d_stage1.py -- B4d stage 1: what bulk can stand through the write\n")
    print("D1 B4c's far model through the write: ell > 2 R_reach = %.3g m; ell/r0 > %.3g -- the flat limit" %
          (d["ell_min"], d["ratio"]))
    t = d["tang"]
    print("D2 the localized 5D hole's plane slice: g_tt = -(%s); 1/r coefficient %s; surface gravity %s; throat %s" %
          (t["f"], t["one_over_r"], t["kappa"], t["throat"] or "none"))
    print("D3 a closing plane on eq. (17)'s static bulk: rho + p_r (units 2/kappa^2) at y_w = %s" % WALL_Y)
    for rc, v in d["nec_r"].items():
        print("     r = %-6s %s" % (rc, "  ".join("%+.4f" % x for x in v)))
    print("     negative everywhere: %s (Padé orders differ by at most %.1e)" % (d["every_fails"], d["pade_gap"]))
    print("     control RS1 second brane: rho = %s, p = %s; flat-limit string: d h/dy = %s" %
          (d["rs"][0], d["rs"][1], d["string"]))
    print("D4 the slab switches the string's instability off for y_w < pi r+/mu_c = %.3f r+" % d["slab"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    rh = sp.Symbol("r_h", positive=True)
    t = d["tang"]
    chk("D1: through the write B4c's far model needs ell > 2 R_reach ~ 4.0e5 m, ell/r0 > 1e5 -- the flat limit",
        3.9e5 < d["ell_min"] < 4.1e5 and d["ratio"] > 1e5)
    chk("D2: the localized 5D hole's plane slice has no 1/r term, surface gravity 1/r_h (not extremal), no throat",
        t["one_over_r"] == 0 and sp.simplify(t["kappa"] - 1 / rh) == 0 and not t["throat"])
    chk("D3: a Z2 plane closing eq. (17)'s static bulk at any y_w in 0.25-2.3m needs rho + p_r < 0 at every r in "
        "2.1-6m; two Padé orders differ by less than a tenth of the smallest value",
        d["every_fails"] and d["pade_gap"] < 0.1 * min(abs(v) for vals in d["nec_r"].values() for v in vals))
    chk("D3 controls: RS1's second brane is negative tension with rho + p = 0; the flat-limit string's plane carries "
        "nothing", sp.simplify(d["rs"][0] + d["rs"][1]) == 0 and sp.simplify(d["rs"][0]) != 0
        and float(d["rs"][0].subs(sp.Symbol("ell", positive=True), 1)) < 0 and all(x == 0 for x in d["string"]))
    chk("D3 control: the sign is not forced -- near the throat (r = 2.1m) rho + p_theta > 0 on the same plane",
        all(c["nec_q"] > 0 for c in d["walls"]["21/10"][1]))
    chk("D4: the slab switches the string's instability off below pi/mu_c = 3.59 r+", 3.55 < d["slab"] < 3.63)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
