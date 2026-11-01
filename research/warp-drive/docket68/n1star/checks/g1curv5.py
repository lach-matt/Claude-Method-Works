#!/usr/bin/env python3
"""g1curv5.py -- CERTIFY-10L5 section 6b (D475): the curvature invariant near x = -1 as the amplitude rises.

D445-D446 found G1's angular non-convergence near the x = -1 axis from v ~ 2 at areal radius about 1, beginning between
1/2 and 3/4 of the record's amplitude, and D458-D462 could not tell a singularity, a steep smooth feature and an axis
defect apart from the metric functions. The Kretschmann scalar K = Riem^2 is an invariant, so it does not see the
gauge, and dnsolve5.kretschmann assembles it from exact Christoffels, so the axis terms are not differentiated
numerically. Here it is computed on the saved runs of D445 (dnsolve5.py --run 1 0.9 M 800 360 out 0 ld 3 amp A, A = 1/4,
1/2, 3/4, 7/8, 1, M = 32 and 40), on 24 u-rows crossing the failure region (kept cells with areal radius in [0.95, 1.5]
and v in [1.5, 3]), and reported per v-band, over the kept cells of those rows with areal radius in [1.0, 1.4]:

  - dev_M = max |K/K_0 - 1| at x = -0.99, K_0 = 72/R^8 Tangherlini's at the same areal radius, K interpolated in x from
    the collocation nodes (Chebyshev in each run's own nodes): how far the curvature departs from the background near the
    axis;
  - diff = max |K_32 - K_40|/K_0 there: whether the invariant itself converges in angle;
  - p = the exponent of dev in A between successive amplitudes (1 for a linear response, 2 for a quadratic one);
  - the same three at x = -0.9 and x = 0, away from the axis.

If K converges near the axis where P does not, the non-convergence sits in the gauge functions, not in the geometry; if
K's difference grows with dev, the angular structure of the geometry itself outruns the resolution; if dev grows faster
than any fixed power of A as A -> 1, the solution may be heading for a singularity there.

Labels: computed (floating point, on saved runs).

    python3 checks/g1curv5.py DIR      (DIR holds ampA_M32.npz and ampA_M40.npz; K on the chosen rows is cached in
                                        DIR/curvA_MM.npz)
"""
import os
import sys

import numpy as np
from numpy.polynomial import chebyshev as Ch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import dnsolve5 as D                                                   # noqa: E402

AMPS = ("0.25", "0.5", "0.75", "0.875", "1")
BANDS = ((1.5, 1.75), (1.75, 2.0), (2.0, 2.25), (2.25, 2.5), (2.5, 3.0))
XS = (-0.99, -0.9, 0.0)


def pick_rows(Z, n=24):
    R, mask, v = Z["R"], Z["mask"], Z["v"]
    with np.errstate(invalid="ignore"):
        Rm = np.nanmean(R, axis=2)
    vin = (v >= 1.5) & (v <= 3.0)
    ok = [i for i in range(1, R.shape[0] - 1)                          # mask is True on excluded cells
          if np.any(~mask[i] & vin & (Rm[i] >= 0.95) & (Rm[i] <= 1.5))]
    if len(ok) <= n:
        return ok
    return [ok[k] for k in np.linspace(0, len(ok) - 1, n).round().astype(int)]


def at_x(K, xnodes, xe):
    """K (..., M) at the nodes -> its Chebyshev interpolant at xe (each run's own nodes are Chebyshev-Gauss in x)"""
    M = len(xnodes)
    V = Ch.chebvander(xnodes, M - 1)
    c = np.linalg.solve(V, np.moveaxis(K, -1, 0).reshape(M, -1))
    return Ch.chebval(xe, c).reshape(K.shape[:-1])


def curv(dirn, A, M, rows=None):
    cache = os.path.join(dirn, "curv%s_M%d.npz" % (A, M))
    if os.path.exists(cache):
        c = dict(np.load(cache))
        if rows is None or list(c["rows"]) == list(rows):
            return c
    Z = dict(np.load(os.path.join(dirn, "amp%s_M%d.npz" % (A, M))))
    if rows is None:
        rows = pick_rows(Z)
    K = D.kretschmann(Z, rows=rows)[rows]
    out = dict(rows=np.array(rows), K=K, R=Z["R"][rows], mask=Z["mask"][rows], v=Z["v"], x=Z["x"])
    np.savez(cache, **out)
    return out


def main():
    dirn = sys.argv[1]
    Z40 = dict(np.load(os.path.join(dirn, "amp1_M40.npz")))
    rows = pick_rows(Z40)
    del Z40
    print("  rows (u indices): %s" % rows, flush=True)
    res = {}
    for A in AMPS:
        for M in (32, 40):
            c = curv(dirn, A, M, rows)
            Rx = {xe: at_x(c["R"], c["x"], xe) for xe in XS}
            Kx = {xe: at_x(c["K"], c["x"], xe) for xe in XS}
            res[(A, M)] = (c, Rx, Kx)
            print("  A = %s, M = %d: done" % (A, M), flush=True)
    v = res[("1", 40)][0]["v"]
    for xe in XS:
        print("\n  at x = %g: per v-band, dev_40 = max |K/K_0 - 1| (areal radius in [1.0, 1.4], cells kept at both M), "
              "diff = max |K_32 - K_40|/K_0, and p, dev's exponent in A" % xe)
        prev = None
        for A in AMPS:
            c32, R32, K32 = res[(A, 32)]
            c40, R40, K40 = res[(A, 40)]
            cells = []
            for lo, hi in BANDS:
                vin = (v >= lo) & (v < hi)
                sel = ~c32["mask"] & ~c40["mask"] & vin[None, :]             # kept at both M
                Rr = R40[xe]
                sel &= (Rr >= 1.0) & (Rr <= 1.4) & np.isfinite(K32[xe]) & np.isfinite(K40[xe])
                K0 = 72.0 / Rr**8
                if not sel.any():
                    cells.append((np.nan, np.nan))
                    continue
                dev = np.nanmax(np.abs(K40[xe] / K0 - 1)[sel])
                diff = np.nanmax(np.abs(K32[xe] - K40[xe])[sel] / K0[sel])
                cells.append((dev, diff))
            line = "    A = %-5s " % A + "  ".join("[%.2f,%.2f): dev %.3g diff %.2g" % (lo, hi, d, f)
                                               for (lo, hi), (d, f) in zip(BANDS, cells))
            if prev is not None:
                Ap, cp = prev
                ps = [np.log(d / dp) / np.log(float(A) / float(Ap)) if d > 0 and dp > 0 else np.nan
                      for (d, _), (dp, _) in zip(cells, cp)]
                line += "  p: " + " ".join("%.2f" % q for q in ps)
            print(line, flush=True)
            prev = (A, cells)
    return 0


if __name__ == "__main__":
    sys.exit(main())
