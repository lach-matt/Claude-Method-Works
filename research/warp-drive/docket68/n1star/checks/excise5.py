#!/usr/bin/env python3
"""excise5.py -- deeper excisions on a second grid (verifier 259's item 5, D605; supplement section 10.2, growth5.py G5).

growth5.py G5 found, on single grids, that a deeper excision fails earlier, not later: at mu0 = 100 l5^2 the second
zero of the round spheres' expansion holds from v = 1.40957 (y = 1.6, r = 0.39 r_h) and 1.35298 (y = 2, r = 0.25 r_h),
against 1.4959-1.5 at the standard excision; at mu0 = 1000 l5^2 from 1.52354 (y = 2.2, r = 0.21 r_h, Ny = 16) against
1.58251-1.58294. Here the same runs on the next finer grid (Ny = 28 at mu0 = 100, as the standard excision's second
grid; Ny = 20 at mu0 = 1000), read with growth5.py's own breakdown() (the second zero holding over 0.04 in v).

  E1 (computed, floating point) each deeper run's breakdown on the finer grid beside its single-grid value and the
     standard excision's: the order "deeper is earlier" holds on both grids, and the breakdown moves by the amount
     printed between the grids.
  Control: the standard excision's own two grids (growth5.py's pinned 20 x 16 and 28 x 16 at mu0 = 100), which agree to
     0.005, as the measure of grid dependence the deeper runs are compared with.

Runs (each one to two hours; part files in data/, merged by growth5.py --merge):
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


def e1(control=False):
    R = load_all()
    if control:
        a, b = (G.breakdown(R[k]) for k in STD["L100"])
        return abs(a - b) > 0.005
    ok = True
    for coarse, fine in DEEP:
        if fine not in R:
            print("  E1: %s not run yet" % fine, flush=True)
            ok = False
            continue
        vc, vf = G.breakdown(R[coarse]), G.breakdown(R[fine])
        std = STD[coarse.split("_")[0]]
        vs = [G.breakdown(R[k]) for k in std]
        earlier = vf is not None and vc is not None and vf < min(vs) and vc < min(vs)
        print("  E1: %s: breakdown %.5f (single grid) and %s (finer grid), moved by %s; standard excision %s: deeper is"
              " earlier on both grids: %s" % (coarse.replace("_20x16", "").replace("_16x16", ""), vc,
                                              "%.5f" % vf if vf else "none", "%.5f" % abs(vf - vc) if vf else "-",
                                              ", ".join("%.5f" % x for x in vs), earlier), flush=True)
        ok &= earlier
    return ok


CHECKS = [("E1", e1)]


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
