#!/usr/bin/env python3
"""excise5.py -- deeper excisions on a second grid (verifier 259's item 5, D605; supplement section 10.2, growth5.py G5).

growth5.py G5 found, on single grids, that a deeper excision fails earlier, not later: at mu0 = 100 l5^2 the second
zero of the round spheres' expansion holds from v = 1.40957 (y = 1.6, r = 0.39 r_h) and 1.35298 (y = 2, r = 0.25 r_h),
against 1.4959-1.5 at the standard excision; at mu0 = 1000 l5^2 from 1.52354 (y = 2.2, r = 0.21 r_h, Ny = 16) against
1.58251-1.58294. Here the same runs on the next finer grid (Ny = 28 at mu0 = 100, as the standard excision's second
grid; Ny = 20 at mu0 = 1000), read with growth5.py's own breakdown(): the first v from which the second zero of the
expansion holds over an interval `hold` in v (growth5.py's default 0.01), or W at the boundary is >= 0.

  E1 (computed, floating point) at hold = 0.01: each deeper run's breakdown on both grids, beside the standard
     excision's on its two grids; deeper is earlier on both grids. The grid moves are printed beside the standard
     excision's own (0.0041 at mu0 = 100, 0.0004 at mu0 = 1000), not tested against them.
  E2 (computed) the order "deeper is earlier on both grids" for every hold in {0.005, 0.01, 0.02, 0.04, 0.06}; the
     breakdowns at hold = 0.04 are printed (there the second zero of the y = 2 runs lasts 0.017 before W >= 0, so their
     breakdown is where W turns, and the grid moves are larger).
  Control (both checks): each deeper run replaced by the standard run of its seed (a data swap); the order must then
     fail, so a test that cannot tell deeper from standard is rejected.

Runs (each one to three hours; part files in data/, merged into data/growth5_runs.json by growth5.py --merge):
    python3 growth5.py --run 100 1 28 16 0 4.5 --yex 1.6
    python3 growth5.py --run 100 1 28 16 0 4.5 --yex 2
    python3 growth5.py --run 1000 0.316228 20 16 0 4.5 --yex 2.2

Labels: computed (floating point; the solver's scheme, not certified).

Run: python3 checks/excise5.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import growth5 as G                                                             # noqa: E402

DEEP = [("L100_lam1_20x16_d0_y1.6", "L100_lam1_28x16_d0_y1.6"), ("L100_lam1_20x16_d0_y2", "L100_lam1_28x16_d0_y2"),
        ("L1000_lam0.3162_16x16_d0_y2.2", "L1000_lam0.3162_20x16_d0_y2.2")]
STD = {"L100": ("L100_lam1_20x16_d0", "L100_lam1_28x16_d0"), "L1000": ("L1000_lam0.3162_20x16_d0",
                                                                         "L1000_lam0.3162_28x16_d0")}


def load_all():
    R = G.load()
    d = os.path.dirname(G.RUNS)
    for f in sorted(os.listdir(d)):
        if f.startswith("growth5_runs_") and f.endswith(".json"):
            R.update(json.load(open(os.path.join(d, f))))
    return R


def order(R, hold, swap=False, show=False):
    """deeper is earlier on both grids, at a given hold; swap: each deeper run replaced by its seed's standard run"""
    ok = True
    for coarse, fine in DEEP:
        std = STD[coarse.split("_")[0]]
        rc, rf = (R[std[0]], R[std[1]]) if swap else (R[coarse], R[fine])
        vc, vf = G.breakdown(rc, hold), G.breakdown(rf, hold)
        vs = [G.breakdown(R[k], hold) for k in std]
        earlier = vf is not None and vc is not None and vf < min(vs) and vc < min(vs)
        if show:
            name = coarse.replace("_20x16", "").replace("_16x16", "")
            stds = ", ".join("%.5f" % x for x in vs)
            print("  %s: breakdown %.5f (single grid), %.5f (finer grid), moved by %.5f; standard excision %s (moved "
                  "%.5f); deeper is earlier on both grids: %s" % (name, vc, vf, abs(vf - vc), stds, abs(vs[0] - vs[1]),
                                                                  earlier), flush=True)
        ok &= earlier
    return ok


def e1(control=False):
    R = load_all()
    if control:
        return order(R, 0.01, swap=True)
    print("  E1 (hold = 0.01):", flush=True)
    return order(R, 0.01, show=True)


HOLDS = [0.005, 0.01, 0.02, 0.04, 0.06]


def e2(control=False):
    R = load_all()
    res = [order(R, h, swap=control) for h in HOLDS]
    if control:
        return any(res)
    print("  E2: deeper is earlier on both grids at hold = %s: %s" % (HOLDS, res), flush=True)
    print("  E2 at hold = 0.04:", flush=True)
    order(R, 0.04, show=True)
    return all(res)


CHECKS = [("E1", e1), ("E2", e2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
