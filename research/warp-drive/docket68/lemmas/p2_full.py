#!/usr/bin/env python3
"""p2_full.py -- M1's open piece: position 2's plane across the whole static bulk, and what seated (Z) asks of a thin
plane (computed, deduced, standard-not-READ; not verified by a separate session; not seated; 2026-10-10).

ITEM197 met M1 in the throat (Kaus-Reall's near-horizon class): facing P2, our plane needs no added matter.  M1 needs a
whole P2 (F1-AUDIT D1).  This takes the simplest whole P2 -- constant Gaussian depth y2 from our plane, mirrored (Z2) --
through the full static bulk of eq. (17) (b4_static.py's exact series, flat limit, imported by path), and asks what the
seated (Z) clause demands of any thin plane.

  TS (deduced; standard-not-READ thin-shell formalism) a light ray crossing a thin plane with surface stress S_ab picks up
     int T(k,k) d lambda = S(k_par, k_par)/|n.k|.  As the ray grazes the plane, k_par tends to a null vector k0 tangent
     to it and |n.k| -> 0: the plane's contribution tends to S(k0,k0) x infinity.  Every other contribution along the
     ray is bounded (a vacuum bulk; other planes crossed at finite angles).  So seated (Z) -- 'never violated', net
     along each light ray (183) -- forces S(k0,k0) >= 0 for every null k0 tangent to a thin plane, at every point: the
     pointwise NEC on the plane.  The exception is a second singular source on the same rays (S15's coincident pair),
     which 198's way in does not supply.  This settles the conditional R1-COVER.md carried (H-POINTWISE-NEC-ON-P2,
     'undecided under (Z)'): for a thin P2 it follows from (Z).  Computed check: the crossing integral at angles
     approaching grazing, with a control of positive S(k0,k0)
  S1 (computed) P2 at constant depth y2, mirrored, in the flat-limit static bulk: rho, rho + p_r and rho + p_theta from
     Israel, normal into the slab, on b4_static's 32 radii (2.005m to 32m), Pade [10/10] against [9/10] in y^2 of the
     order-40 series (agreement to 1e-4 at every reported point):
       rho > 0 at every radius for y2 <= 1.5m;  rho + p_theta > 0 everywhere;
       rho + p_r < 0 at every radius at every depth (small: -6e-4 at the throat column, ~ -0.2 at worst), tending to
       0 at the throat -- where ITEM197's AdS2 symmetry makes it exactly 0 -- and to 0 far out
  S2 (deduced from TS and S1) the constant-depth mirrored P2 breaks (Z) through grazing radial rays: refuted as M1's
     P2.  R1-COVER's members verified across the whole cover, which also break the radial NEC, are refuted the same way.
     What is left for M1: a shaped P2 (y = Y(r)), or P2 joined to position 2's own bulk beyond it (138; 197's "the
     other plane", not a mirror), whose far side adds its own (k_t - k_r); a thick P2.  OPEN.
Imports lemmas/b4_static.py by path.  Stdlib + sympy + mpmath.  python3 p2_full.py [--selftest | --mutants | --full]
"""
import contextlib
import importlib.util
import io
import json
import os
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = {}
SELF_COLS = ("401/200", "21/10", "3", "10")       # the selftest's columns; --full runs all 32
DEPTHS = (0.25, 0.5, 1.0, 1.5, 2.0)


def _b4():
    spec = importlib.util.spec_from_file_location("p2f_b4_static", os.path.join(HERE, "b4_static.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["p2f_b4_static"] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE, os.path.dirname(HERE)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def _pade(c, L, M):
    return mp.pade([mp.mpf(Fr(v).numerator) / Fr(v).denominator for v in c[:L + M + 1]], L, M)


def _ev(p, s):
    return sum(cf * s**k for k, cf in enumerate(p))


def _dev(p, s):
    return sum(k * cf * s**(k - 1) for k, cf in enumerate(p) if k)


def column(b4, rc, N=40):
    mp.mp.dps = 40
    ser = b4.series(rc, N)
    cols = {}
    for X in "ABC":
        c = ser[X][0]
        even = [c[2 * j] for j in range(N // 2 + 1)]
        for (a1, b1, a2, b2) in ((10, 10, 9, 10), (8, 8, 7, 8), (6, 6, 5, 6)):
            try:
                cols[X] = {"hi": _pade(even, a1, b1), "lo": _pade(even, a2, b2)}
                break
            except ZeroDivisionError:
                continue
    rows = []
    for y2 in DEPTHS:
        s = mp.mpf(y2) ** 2
        res = {}
        for tag in ("hi", "lo"):
            k = {}
            for X in "ABC":
                num, den = cols[X][tag]
                g = _ev(num, s) / _ev(den, s)
                dg = (_dev(num, s) * _ev(den, s) - _ev(num, s) * _dev(den, s)) / _ev(den, s) ** 2 * 2 * y2
                sgn = -1 if not MUT.get("normal_out") else 1
                k[X] = sgn * dg / (2 * g)
            if MUT.get("swap_tr"):
                k["A"], k["B"] = k["B"], k["A"]
            rho = -(k["B"] + 2 * k["C"])                 # units 2/kappa^2 (mirror junction), m = 1
            res[tag] = (float(rho), float(k["A"] - k["B"]), float(k["A"] - k["C"]))
        agree = all(abs(res["hi"][i] - res["lo"][i]) < 1e-4 * max(1.0, abs(res["hi"][i])) for i in range(3))
        rows.append({"y2": y2, "rho": res["hi"][0], "nec_r": res["hi"][1], "nec_t": res["hi"][2], "agree": agree})
    return rows


def thin_shell(S_k0k0=-0.01, rho=0.1):
    """TS: crossing integral S(k_par,k_par)/|n.k| for a ray at angle -> grazing in the (t, r, n) plane, unit metric:
    k = (1, cos a, sin a); n = (0, 0, 1); k_par = (1, cos a, 0); S = diag(rho, p_r) with rho + p_r = S_k0k0."""
    p_r = S_k0k0 - rho
    out = []
    for a in (0.5, 0.1, 0.01, 0.001):
        import math
        kpar_t, kpar_r, nk = 1.0, math.cos(a), math.sin(a)
        Skk = rho * kpar_t**2 + p_r * kpar_r**2
        out.append((a, Skk / nk))
    return out


def compute(cols=SELF_COLS):
    b4 = _b4()
    t0 = time.time()
    data = {rc: column(b4, rc) for rc in cols}
    return {"cols": data, "ts_neg": thin_shell(-0.01), "ts_pos": thin_shell(+0.01), "secs": time.time() - t0}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    neg, pos = d["ts_neg"], d["ts_pos"]
    add("TS a thin plane with S(k0,k0) < 0 gives grazing rays an unboundedly negative crossing integral (more negative "
        "as the angle falls); control S(k0,k0) > 0 grows positive", all(neg[i][1] > neg[i + 1][1] for i in range(3))
        and neg[-1][1] < -5 and all(pos[i][1] < pos[i + 1][1] for i in range(3)) and pos[-1][1] > 5)
    C = d["cols"]
    allrows = [r for rc in C for r in C[rc]]
    add("S1a every reported point is Pade-stable ([10/10] against [9/10], 1e-4)", all(r["agree"] for r in allrows))
    add("S1b rho > 0 at every sampled radius for y2 <= 1.5m; rho + p_theta > 0 everywhere",
        all(r["rho"] > 0 for r in allrows if r["y2"] <= 1.5) and all(r["nec_t"] > 0 for r in allrows))
    add("S1c rho + p_r < 0 at every sampled radius for y2 <= 1.5m, small at the throat column (|.| < 2e-3) and far out",
        all(r["nec_r"] < 0 for r in allrows if r["y2"] <= 1.5)
        and all(abs(r["nec_r"]) < 2e-3 for r in C["401/200"] if r["y2"] <= 1.5)
        and all(abs(r["nec_r"]) < 2e-3 for r in C["10"]))
    return res


MUTANTS = {"normal_out": "P2's normal pointing out of the slab", "swap_tr": "t and r curvatures swapped"}


def selftest():
    d = compute()
    r = checks(d)
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d  (%.0f s)" % (k, len(r), d["secs"]))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-11s %-38s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("p2_full.py -- P2 at constant depth, mirrored, in the full static bulk (flat limit; units 2/kappa^2, m = 1)\n")
    for rc, rows in d["cols"].items():
        print("r=%-7s " % rc + "  ".join("y%.2f: rho%+.3g r%+.2g t%+.2g%s" % (r["y2"], r["rho"], r["nec_r"], r["nec_t"],
                                                                         "" if r["agree"] else "?") for r in rows))
    print("\nTS grazing crossing integrals, S(k0,k0) = -0.01:", ["%.3g at %g" % (v, a) for a, v in d["ts_neg"]])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--full" in sys.argv:
        b4 = _b4()
        cols = json.load(open(os.path.join(HERE, "b4_static.json")))["r"]
        report(compute(cols))
    else:
        report(compute())
