#!/usr/bin/env python3
"""g1curv5.py -- CERTIFY-10L5 section 6b (D475): the curvature invariant near x = -1 as the amplitude rises.

D445-D446 found G1's angular non-convergence near the x = -1 axis from v ~ 2 at areal radius about 1, beginning between
1/2 and 3/4 of the record's amplitude, and D458-D462 could not tell a singularity, a steep smooth feature and an axis
defect apart from the metric functions. The Kretschmann scalar K = Riem^2 is an invariant, so it does not see the
gauge, and dnsolve5.kretschmann assembles it from exact Christoffels, so the axis terms are not differentiated
numerically. Here it is computed on the saved runs of D445 (dnsolve5.py --run 1 0.9 M 800 360 out 0 ld 3 amp A, A = 1/4,
1/2, 3/4, 7/8, 1, M = 32 and 40), on 24 u-rows crossing the failure region (kept cells with areal radius in [0.95, 1.5]
and v in [1.5, 3]), and reported per v-band, over the kept cells of those rows with areal radius in [1.0, 1.4]:

    - dev_M = max |K/K_0 - 1| at x = -0.97, K_0 = 72/R^8 Tangherlini's at the same areal radius, K interpolated linearly
    between the two nearest collocation nodes (a global interpolant would carry the near-axis alternation to every
    angle): how far the curvature departs from the background near the axis;
  - diff = max |K_32 - K_40|/K_0 there: whether the invariant itself converges in angle;
  - p = the exponent of dev in A between successive amplitudes (1 for a linear response, 2 for a quadratic one);
    - the same three at x = -0.9, -0.5, 0 and 0.5, away from the axis.

If K converges near the axis where P does not, the non-convergence sits in the gauge functions, not in the geometry; if
K's difference grows with dev, the angular structure of the geometry itself outruns the resolution; if dev grows faster
than any fixed power of A as A -> 1, the solution may be heading for a singularity there.

Measured (D475, corrected D485; 24 of the 438 rows with R in [1, 1.4], mask True marking excluded cells; (u, v) at 800 x
360 throughout, so 'converges' means in M, in angle): wherever K converges in M its departure from the background stays
of order 1, growing like A^p with p from 0.58 to 2.22 over the converged bands (dev at x = -0.97 from 0.51 at A = 1/4 to
3.9 at A = 1 on [1.5, 1.75), diff below 1.3e-3): on v < 1.75 at every A, and on v < 2.25 at A <= 1/2, with no resolved
growth before the failure. dev also carries the rise in mass the ingoing wave brings. At A = 1/2 the convergence weakens
from v = 2.25 (diff up to 0.4 of dev at x = 0.5). Convergence is lost at A = 3/4 inside [2, 2.25) (at x = -0.97 K
converges to v = 2.1), at A = 7/8 off the axis on [1.75, 2), and at A = 1 first off the axis (v about 1.875 to 1.9 at x =
0 and 0.5, 1.95 to 1.975 at x = -0.97). Beyond, K is unresolved at every angle computed, x = -0.97 to 0.5: dev from about
3 to 10^7 with diff as large, so those values are not a resolved growth of the curvature. The angular derivatives in K
are the collocation's, global in x, so this does not localise the cause at the axis or exclude it: the invariant does not
tell a singularity from a defect of the scheme, but it shows the failure is not only in the gauge functions, and that the
curvature is moderate wherever it is resolved in angle.

Labels: computed (floating point, on saved runs).

    python3 checks/g1curv5.py DIR      (DIR holds ampA_M32.npz and ampA_M40.npz; K on the chosen rows is cached in
                                        DIR/curvA_MM.npz)
    python3 checks/g1curv5.py --null DIR    (D489: DIR holds D432's l1_rc0.9_M32/40.npz and their _1600 runs)
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import dnsolve5 as D                                                   # noqa: E402

AMPS = ("0.25", "0.5", "0.75", "0.875", "1")
BANDS = ((1.5, 1.75), (1.75, 2.0), (2.0, 2.25), (2.25, 2.5), (2.5, 3.0))
XS = (-0.97, -0.9, -0.5, 0.0, 0.5)


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
    """K (..., M) at the nodes -> linear interpolation at xe between the two nearest nodes; a global interpolant
    would carry the near-axis nodes' alternation (D458) to every angle"""
    o = np.argsort(xnodes)
    xs, Ks = xnodes[o], K[..., o]
    j = min(max(int(np.searchsorted(xs, xe)), 1), len(xs) - 1)
    w = (xe - xs[j - 1]) / (xs[j] - xs[j - 1])
    return (1 - w) * Ks[..., j - 1] + w * Ks[..., j]


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


def reduced(path, rows):
    """the saved run at path cut to the u-rows r - 1, r, r + 1 of each r in rows (kretschmann needs only those), read
    one array at a time; returns the cut dict and the rows' indices in it"""
    with np.load(path) as F:
        Nu = F["u"].shape[0]
        idx = np.array([r + d for r in rows for d in (-1, 0, 1)])
        Z = {}
        for k in F.files:
            a = F[k]
            Z[k] = a[idx] if (a.ndim >= 1 and a.shape[0] == Nu) else a
    return Z, [3 * k + 1 for k in range(len(rows))]


def null_refinement(dirn):
    """--null DIR (D489): K at A = 1 on D432's runs, M = 32, 40 at 800 x 360 (l1_rc0.9_M32/40.npz) and 1600 x 720
    (..._1600.npz), on 24 u-rows of the coarse grid and the same rows (2i) of the fine one, compared at the coarse grid's
    nodes: whether K converges in the null grid as well as in angle"""
    Zc = dict(np.load(os.path.join(dirn, "l1_rc0.9_M40.npz")))
    rows = pick_rows(Zc)
    uc, vc = Zc["u"], Zc["v"]
    del Zc
    print("  rows (u indices of the 800 x 360 grid): %s" % rows, flush=True)
    K, R, MK = {}, {}, {}
    for M in (32, 40):
        for N, fac in ((800, 1), (1600, 2)):
            cache = os.path.join(dirn, "curvnull_M%d_%d.npz" % (M, N))
            if os.path.exists(cache) and list(np.load(cache)["rows"]) == list(rows):
                c = dict(np.load(cache))
            else:
                name = "l1_rc0.9_M%d%s.npz" % (M, "" if N == 800 else "_1600")
                Z, rr = reduced(os.path.join(dirn, name), [fac * r for r in rows])
                assert np.allclose(Z["u"][rr], uc[rows]), name
                assert np.allclose(Z["v"][::fac], vc), name
                Kf = D.kretschmann(Z, rows=rr)[rr][:, ::fac]
                c = dict(rows=np.array(rows), K=Kf, R=Z["R"][rr][:, ::fac], mask=Z["mask"][rr][:, ::fac], x=Z["x"])
                np.savez(cache, **c)
                del Z
            K[(M, N)] = c
            print("  M = %d, %d: done" % (M, N), flush=True)
    for xe in XS:
        print("\n  at x = %g, A = 1: per v-band over areal radius [1.0, 1.4], cells kept in all four runs: dev = max |K/K_0 "
              "- 1| (M = 40, 1600 x 720); dM = max |K_32 - K_40|/K_0 at 1600 x 720 (in angle); duv = max |K_800 - "
              "K_1600|/K_0 at M = 40 (in the null grid)" % xe)
        Kx = {k: at_x(c["K"], c["x"], xe) for k, c in K.items()}
        Rr = at_x(K[(40, 1600)]["R"], K[(40, 1600)]["x"], xe)
        keep = ~K[(32, 800)]["mask"] & ~K[(40, 800)]["mask"] & ~K[(32, 1600)]["mask"] & ~K[(40, 1600)]["mask"]
        K0 = 72.0 / Rr**8
        for lo, hi in BANDS:
            sel = keep & ((vc >= lo) & (vc < hi))[None, :] & (Rr >= 1.0) & (Rr <= 1.4)
            sel &= np.all([np.isfinite(Kx[k]) for k in Kx], axis=0)
            if not sel.any():
                print("    [%.2f,%.2f): no cells" % (lo, hi))
                continue
            dev = np.max(np.abs(Kx[(40, 1600)] / K0 - 1)[sel])
            dM = np.max(np.abs(Kx[(32, 1600)] - Kx[(40, 1600)])[sel] / K0[sel])
            duv = np.max(np.abs(Kx[(40, 800)] - Kx[(40, 1600)])[sel] / K0[sel])
            dM8 = np.max(np.abs(Kx[(32, 800)] - Kx[(40, 800)])[sel] / K0[sel])
            print("    [%.2f,%.2f): dev %.3g  dM %.2g  duv %.2g  (dM at 800 x 360: %.2g; %d cells)"
                  % (lo, hi, dev, dM, duv, dM8, int(sel.sum())), flush=True)
    return 0

def main():
    if sys.argv[1:2] == ["--null"]:
        return null_refinement(sys.argv[2])
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
