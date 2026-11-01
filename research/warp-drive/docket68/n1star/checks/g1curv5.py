#!/usr/bin/env python3
"""g1curv5.py -- CERTIFY-10L5 section 6b (D475): the curvature invariant near x = -1 as the amplitude rises.

D445-D446 found G1's angular non-convergence near the x = -1 axis from v ~ 2 at areal radius about 1, beginning between
1/2 and 3/4 of the record's amplitude, and D458-D462 could not tell a singularity, a steep smooth feature and an axis
defect apart from the metric functions. The Kretschmann scalar K = Riem^2 is an invariant, so it does not see the
gauge, and dnsolve5.kretschmann assembles it from exact Christoffels, so the axis terms are not differentiated
numerically. Here it is computed on saved amplitude runs (dnsolve5.py --run 1 0.9 M 800 360 out 0 amp A, A = 1/4,
1/2, 3/4, 7/8, 1, M = 32 and 40; without D445's ld 3, as the cached rows show, verifier 211, D499), on 24 u-rows crossing the failure region (kept cells with areal radius in [0.95, 1.5]
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

Measured (D475, corrected D485 and D499; 24 of the 438 rows with R in [1, 1.4], mask True marking excluded cells; (u, v) at 800 x
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

Corrected D499 (verifier 211): the runs above are plain, without ld 3. They agree with D445's ld 3 runs to three digits
on [1.5, 1.75), not later: at A = 1 the ld 3 runs lose convergence at v = 1.925 to 1.94 at every angle, and off the axis
on [1.75, 2) their dev is 2.9 to 3.2 against 142 to 226 here. The M-difference below 1.3e-3 on [1.5, 1.75) is the floor
of the linear interpolation (M = 32 and 40 have different nodes); with the Chebyshev interpolant it is 1e-6 or less.

Measured with --null (D489, corrected D499; D432's runs at A = 1, with ld 3): on [1.5, 1.75) the 800 x 360 and 1600 x
720 values of K differ by 2.5e-3 to 5.2e-3 of K_0 at x = -0.97 to 0.5 (1.0e-2 at the node x = -0.999), with dev 0.42 to
3.9, against an M-difference of 1.3e-7 to 1.0e-6 with the Chebyshev interpolant (the 2e-4 to 1.3e-3 this printed is the
linear interpolation's): there the null step sets the error. On [1.75, 2) the angular difference, 1.4 to 3, dominates
the null one, 0.045 to 0.74, at the band maxima (v >= 1.95), the same at both null grids there to 15 %; near the axis
the null difference rises first (x = -0.97: 4.4e-3 at v = 1.75 to 4.7e-2 at 1.90) and the angular one overtakes from v
~ 1.9. From v = 2 both are as large as dev (the null difference up to 1.8e5, at x = 0 on [2.25, 2.5)).

Seed-2 mode (--seed2, D515): the same question for the record's second seed (wavelength 0.3162, dnsolve5.py --run 0.3162
0.9 M 800 360 out 0 ld 3, saved as s2_M16/24/32.npz, M = 16, 24, 32), where the angular solution converges to v about 3
to 3.5 and then fails near x = +1: is the steepening at x = +1 the solution's or the scheme's, judged by K? K on 24 u-rows
(the same at all three M) crossing kept cells with R in [0.9, 1.5] and v in [2.5, 4.5], per v-band (2.5, 2.75), (2.75, 3),
(3, 3.25), (3.25, 3.5), (3.5, 4), (4, 4.5) over cells kept at all M with R in [0.9, 1.4], at x = 0.99, 0.97, 0.9, 0.5, 0,
-0.5, -0.97 by the Chebyshev interpolant through all M nodes (barycentric): dev = max |K/K_0 - 1| (M = 32), diff_a =
max |K_32 - K_24|/K_0, diff_b = max |K_24 - K_16|/K_0, their ratio (large = spectral convergence in M, near or below 1 =
not converging), diff_a with the linear interpolant at x = 0.97 as the interpolation-floor cross-check, and the earliest v
at which diff_a exceeds max(1e-2 dev, 1e-3) of K_0 in a cell.
Measured (D515; 24 rows, u indices 271 to 461; 9 s from the caches, 15 minutes cold): up to v = 3.25 K converges
spectrally in M at every x, the M-differences 1e-8 to 1e-5 of K_0 and diff_b/diff_a mostly 2 to 58, with dev 0.2 to 1.9.
From v = 3.25 the ratio falls to about 1 or below at x = 0.9, 0.5, 0 and -0.97, and from v = 3.5 at every x but 0.99 (on
[3.25, 3.5) it is 2.1 to 3.6 at 0.99, 0.97 and -0.5; on [3.5, 4) 1.2 at 0.99; corrected D518). diff_a passes 1e-2 of dev
first off the axis, at v = 3.74 (x = 0.5), 3.75 (0), 3.76 (-0.5) and 3.83 (0.9), and later at the axis, at 4.00 (0.97)
and 4.04 (0.99); not at x = -0.97, which has no kept cells after v = 4. On [3.5, 4) diff_a is 0.037 to 0.077 at x = -0.5
to 0.5 against 0.0022 at 0.99. On [4, 4.5) at x = 0.5 to 0.99, dev is 19 to 206 with diff_a about as large (32 and 32.9
at x = 0.99, 205 and 206 at 0.9), while diff_b is 0.03 to 0.05: the departure is M = 32's alone, which a growth resolved
in M would not show: M = 16 and 24 stay within order 1 of the background over the band (max |K_24/K_0 - 1| 0.72 to
0.92), and at the maxima K_32 is negative, -18 to -205 K_0, where K_24/K_0 is 0.08 to 1.7 (verifier 222, D518). The
linear interpolant's diff_a at x = 0.97 is 1.5e-3 to 5e-3 on the converged bands, against 4e-8 to 3e-6 with the
Chebyshev one (D499's floor). So the invariant does not single out x = +1: K's angular convergence is lost first in the
interior of the angle range, at v about 3.74, and at the axis about 0.26 later; K stays within order 1 of the background
wherever it is resolved; and the large values near x = +1 after v = 4 come from the finest angular grid only. That
points to the scheme rather than the solution at x = +1, without proving it: a feature finer than M = 24 resolves would
also first show at M = 32. (The saved runs record no solver flags: wavelength, cut, grid and M are checked from the
files, `ld 3` only from the stated command; verifier 222.)

Seed-2 at M = 40 (--seed2-40, D524): the same rows, M = 24, 32, 40 at 800 x 360 (s2_M40.npz from dnsolve5.py --run
0.3162 0.9 40 800 360 out 0 ld 3), on cells kept at all three, Chebyshev interpolant; output in
checks/g1curv5seed2_40.out. Measured (D524): the 32-40 difference is 1e-6 to 1e-4 of K_0 on [2.5, 3) and 1e-4 to 3e-3 on
[3, 3.25), 10 to 3000 times the 24-32 one at every angle, and 0.14 to 0.57 on [3.25, 3.5); from v = 3.5 to 3.7 M = 40
departs by 2e2 to 4e3 K_0 at every angle on cells whose K stencil stays inside its kept region (up to 2e4 near x = +1
after v = 4; cells whose stencil reaches M = 40's cut give 1e4 to 2e6; D525), where M = 24 and 32 agree to 4e-4 to 3e-2.
Refining M at the fixed null grid makes K worse from the start, and the large values come earlier the finer the angular
grid, as D418 found at the first seed: it points to the scheme.

Seed-2 jointly refined (--seed2-1600, D543): M = 32 and 40 at 800 x 360 and 1600 x 720 (s2_M32_1600.npz, s2_M40_1600.npz
from dnsolve5.py --run 0.3162 0.9 M 1600 720 out 0 ld 3), on --seed2-40's rows, the fine rows 2i and v nodes subsampled
by 2, cells kept in all four; output in checks/g1curv5seed2_1600.out. Measured: at 1600 x 720 M = 40's |K/K_0 - 1| is at
most 1.95 below v = 4, as M = 32's, and 1.22-3.11 on [4, 4.5) at x = 0.99-0.9, against 2e3-2e6 at 800 x 360; cells above
2 drop from 11-49 per angle and band to none (2 at x = 0.9 on [4, 4.5)); M = 32 and 40 agree to 3e-7-1.4e-2 K_0 below v
= 3.5, 0.02-1.0 on [3.5, 4), 0.39-2.35 on [4, 4.5). The M = 40 departures at 800 x 360 were the two grids together.

Labels: computed (floating point, on saved runs).

    python3 checks/g1curv5.py DIR      (DIR holds ampA_M32.npz and ampA_M40.npz; K on the chosen rows is cached in
                                        DIR/curvA_MM.npz)
    python3 checks/g1curv5.py --seed2 DIR   (D515: DIR holds s2_M16/24/32.npz; K cached in DIR/curvS2_M<M>.npz)
    python3 checks/g1curv5.py --seed2-40 DIR   (D524: also s2_M40.npz; M = 24, 32, 40)
    python3 checks/g1curv5.py --seed2-1600 DIR (D543: also s2_M32_1600.npz, s2_M40_1600.npz)
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


def pick_rows(Z, n=24, vlo=1.5, vhi=3.0, Rlo=0.95, Rhi=1.5):
    R, mask, v = Z["R"], Z["mask"], Z["v"]
    with np.errstate(invalid="ignore"):
        Rm = np.nanmean(R, axis=2)
    vin = (v >= vlo) & (v <= vhi)
    ok = [i for i in range(1, R.shape[0] - 1)                          # mask is True on excluded cells
          if np.any(~mask[i] & vin & (Rm[i] >= Rlo) & (Rm[i] <= Rhi))]
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
        print("\n  at x = %g, A = 1: per v-band over areal radius [1.0, 1.4], cells kept in all four runs: dev = max "
              "|K/K_0 - 1| (M = 40, 1600 x 720); dM = max |K_32 - K_40|/K_0 at 1600 x 720 (in angle); duv = max "
              "|K_800 - K_1600|/K_0 at M = 40 (in the null grid)" % xe)
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

def cheb(K, xnodes, xe):
    """K (..., M) at the Chebyshev-Gauss nodes (xmap 0) -> the collocation polynomial through all M nodes at xe, by the
    barycentric formula with weights (-1)^j sin((2j+1) pi/2M) for the nodes cos((2j+1) pi/2M)"""
    M = len(xnodes)
    j = np.arange(M)
    assert np.allclose(xnodes, np.cos((2 * j + 1) * np.pi / (2 * M)))
    t = (-1.0) ** j * np.sin((2 * j + 1) * np.pi / (2 * M)) / (xe - xnodes)
    return K @ (t / t.sum())


S2BANDS = ((2.5, 2.75), (2.75, 3.0), (3.0, 3.25), (3.25, 3.5), (3.5, 4.0), (4.0, 4.5))
S2XS = (0.99, 0.97, 0.9, 0.5, 0.0, -0.5, -0.97)


def seed2(dirn):
    """--seed2 DIR (D515): K on 24 rows at M = 16, 24, 32 of the seed-2 run, compared by the Chebyshev interpolant"""
    path = {M: os.path.join(dirn, "s2_M%d.npz" % M) for M in (16, 24, 32)}
    Z = dict(np.load(path[32]))
    rows = pick_rows(Z, 24, 2.5, 4.5, 0.9, 1.5)
    del Z
    print("  rows (u indices of the 800 x 360 grid): %s" % rows, flush=True)
    C = {}
    for M in (16, 24, 32):
        cache = os.path.join(dirn, "curvS2_M%d.npz" % M)
        if os.path.exists(cache) and list(np.load(cache)["rows"]) == list(rows):
            C[M] = dict(np.load(cache))
        else:
            Zr, rr = reduced(path[M], rows)
            K = D.kretschmann(Zr, rows=rr)[rr]
            C[M] = dict(rows=np.array(rows), K=K, R=Zr["R"][rr], mask=Zr["mask"][rr], v=Zr["v"], x=Zr["x"])
            np.savez(cache, **C[M])
            del Zr
        print("  M = %d: done (x nodes nearest +1: %.6f, -1: %.6f)" % (M, C[M]["x"].max(), C[M]["x"].min()), flush=True)
    v = C[32]["v"]
    assert np.allclose(v, C[16]["v"]) and np.allclose(v, C[24]["v"])
    mk = {M: C[M]["mask"] for M in C}
    print("\n  per v-band, cells kept at M = 16, 24, 32 (mask True = excluded, per cell) with R in [0.9, 1.4]; dev = max |K_32/K_0 - 1|, diff_a = max "
          "|K_32 - K_24|/K_0, diff_b = max |K_24 - K_16|/K_0 (Chebyshev), ratio = diff_b/diff_a, lin = diff_a with the "
          "linear interpolant (x = 0.97)")
    first = {}
    allkept = ~(mk[16] | mk[24] | mk[32])
    for xe in S2XS:
        Kx = {M: cheb(C[M]["K"], C[M]["x"], xe) for M in C}
        Rr = cheb(C[32]["R"], C[32]["x"], xe)
        K0 = 72.0 / Rr**8
        ok = allkept & (Rr >= 0.9) & (Rr <= 1.4) & np.all([np.isfinite(Kx[M]) for M in Kx], axis=0)
        da = np.abs(Kx[32] - Kx[24]) / K0
        db = np.abs(Kx[24] - Kx[16]) / K0
        dv_ = np.abs(Kx[32] / K0 - 1)
        print("\n  x = %g" % xe)
        for lo, hi in S2BANDS:
            sel = ok & ((v >= lo) & (v < hi))[None, :]
            if not sel.any():
                print("    [%.2f,%.2f): no cells" % (lo, hi))
                continue
            a, b, d = da[sel].max(), db[sel].max(), dv_[sel].max()
            line = "    [%.2f,%.2f): dev %.3g  diff_a %.3g  diff_b %.3g  ratio %.3g  (%d cells)" % (lo, hi, d, a, b, b / a, int(sel.sum()))
            if xe == 0.97:
                Kl = {M: at_x(C[M]["K"], C[M]["x"], xe) for M in (24, 32)}
                okl = sel & np.isfinite(Kl[24]) & np.isfinite(Kl[32])
                line += "  lin %.3g" % (np.abs(Kl[32] - Kl[24])[okl] / K0[okl]).max()
            print(line, flush=True)
        thr = np.maximum(1e-2 * dv_, 1e-3)
        hit = ok & (v >= 2.5)[None, :] & (v <= 4.5)[None, :] & (da > thr)
        vs = [v[np.argmax(h)] for h in hit if h.any()]
        first[xe] = min(vs) if vs else np.nan
        print("    earliest v where diff_a > max(1e-2 dev, 1e-3): %s" % ("%.4f" % first[xe] if vs else "none"))
    print("\n  summary: earliest v where the M = 24 -> 32 difference exceeds 1e-2 of the departure, by x: "
          + ", ".join("%g: %s" % (xe, "%.3f" % f if np.isfinite(f) else "none") for xe, f in first.items()))
    return 0


def s2_curv(dirn, Ms, rows):
    """K on the seed-2 rows at each M of Ms, cached in DIR/curvS2_M<M>.npz as --seed2 does"""
    C = {}
    for M in Ms:
        cache = os.path.join(dirn, "curvS2_M%d.npz" % M)
        if os.path.exists(cache) and list(np.load(cache)["rows"]) == list(rows):
            C[M] = dict(np.load(cache))
        else:
            Zr, rr = reduced(os.path.join(dirn, "s2_M%d.npz" % M), rows)
            K = D.kretschmann(Zr, rows=rr)[rr]
            C[M] = dict(rows=np.array(rows), K=K, R=Zr["R"][rr], mask=Zr["mask"][rr], v=Zr["v"], x=Zr["x"])
            np.savez(cache, **C[M])
            del Zr
        print("  M = %d: done" % M, flush=True)
    return C


def seed2_40(dirn):
    """--seed2-40 DIR (D524): M = 40 beside 24 and 32 at the second seed, on --seed2's rows: whether M = 32's large
    departures near x = +1 after v = 4 persist at M = 40"""
    Z = dict(np.load(os.path.join(dirn, "s2_M32.npz")))
    rows = pick_rows(Z, 24, 2.5, 4.5, 0.9, 1.5)
    del Z
    C = s2_curv(dirn, (24, 32, 40), rows)
    v = C[32]["v"]
    assert np.allclose(v, C[24]["v"]) and np.allclose(v, C[40]["v"])
    allkept = ~(C[24]["mask"] | C[32]["mask"] | C[40]["mask"])
    print("\n  per v-band, cells kept at M = 24, 32, 40 with R in [0.9, 1.4] (Chebyshev interpolant): dev_M = max "
          "|K_M/K_0 - 1|; d32 = max |K_32 - K_24|/K_0, d40 = max |K_40 - K_32|/K_0, ratio d32/d40")
    for xe in S2XS:
        Kx = {M: cheb(C[M]["K"], C[M]["x"], xe) for M in C}
        Rr = cheb(C[32]["R"], C[32]["x"], xe)
        K0 = 72.0 / Rr**8
        ok = allkept & (Rr >= 0.9) & (Rr <= 1.4) & np.all([np.isfinite(Kx[M]) for M in Kx], axis=0)
        dev = {M: np.abs(Kx[M] / K0 - 1) for M in Kx}
        d32 = np.abs(Kx[32] - Kx[24]) / K0
        d40 = np.abs(Kx[40] - Kx[32]) / K0
        print("\n  x = %g" % xe)
        for lo, hi in S2BANDS:
            sel = ok & ((v >= lo) & (v < hi))[None, :]
            if not sel.any():
                print("    [%.2f,%.2f): no cells" % (lo, hi))
                continue
            line = ("    [%.2f,%.2f): dev24 %.3g  dev32 %.3g  dev40 %.3g  d32 %.3g  d40 %.3g  ratio %.3g  (%d cells)"
                    % (lo, hi, dev[24][sel].max(), dev[32][sel].max(), dev[40][sel].max(), d32[sel].max(),
                       d40[sel].max(), d32[sel].max() / d40[sel].max(), int(sel.sum())))
            big = sel & (dev[32] > 2)
            if big.any():
                q = {M: Kx[M][big] / K0[big] for M in Kx}
                line += ("\n        cells with |K_32/K_0 - 1| > 2: %d; K/K_0 there: M = 24 [%.3g, %.3g], M = 32 [%.3g, "
                         "%.3g], M = 40 [%.3g, %.3g]; of them |K_40/K_0 - 1| > 2 at %d"
                         % (int(big.sum()), q[24].min(), q[24].max(), q[32].min(), q[32].max(), q[40].min(),
                            q[40].max(), int((np.abs(q[40] - 1) > 2).sum())))
            big40 = sel & (dev[40] > 2)
            if big40.any():
                line += "\n        cells with |K_40/K_0 - 1| > 2: %d" % int(big40.sum())
            print(line, flush=True)
    return 0


def seed2_1600(dirn):
    """--seed2-1600 DIR (D537): M = 32 and 40 at 800 x 360 and at 1600 x 720 on --seed2-40's rows (the fine run's rows
    2i, its v nodes subsampled by 2, as --null does): whether M = 40's departures after v = 3.5 at 800 x 360 go when the
    null grid is refined with it"""
    Z = dict(np.load(os.path.join(dirn, "s2_M32.npz")))
    rows = pick_rows(Z, 24, 2.5, 4.5, 0.9, 1.5)
    uc, vc = Z["u"], Z["v"]
    del Z
    C = {}
    for M in (32, 40):
        C[(M, 800)] = s2_curv(dirn, (M,), rows)[M]
        cache = os.path.join(dirn, "curvS2_M%d_1600.npz" % M)
        if os.path.exists(cache) and list(np.load(cache)["rows"]) == list(rows):
            c = dict(np.load(cache))
        else:
            Zf, rr = reduced(os.path.join(dirn, "s2_M%d_1600.npz" % M), [2 * r for r in rows])
            assert np.allclose(Zf["u"][rr], uc[rows]) and np.allclose(Zf["v"][::2], vc), M
            Kf = D.kretschmann(Zf, rows=rr)[rr][:, ::2]
            c = dict(rows=np.array(rows), K=Kf, R=Zf["R"][rr][:, ::2], mask=Zf["mask"][rr][:, ::2], v=vc, x=Zf["x"])
            np.savez(cache, **c)
            del Zf
        C[(M, 1600)] = c
        print("  M = %d, 1600 x 720: done" % M, flush=True)
    keep = ~np.any([c["mask"] for c in C.values()], axis=0)
    print("\n  per v-band, cells kept in all four runs with R in [0.9, 1.4] (Chebyshev interpolant): dev(M, N) = max "
          "|K/K_0 - 1|; dM_N = max |K_32 - K_40|/K_0 at N; duv_M = max |K_800 - K_1600|/K_0 at M; n40 = cells with "
          "|K/K_0 - 1| > 2 at M = 40 (800, 1600)")
    for xe in S2XS:
        Kx = {k: cheb(c["K"], c["x"], xe) for k, c in C.items()}
        Rr = cheb(C[(40, 1600)]["R"], C[(40, 1600)]["x"], xe)
        K0 = 72.0 / Rr**8
        ok = keep & (Rr >= 0.9) & (Rr <= 1.4) & np.all([np.isfinite(Kx[k]) for k in Kx], axis=0)
        dev = {k: np.abs(Kx[k] / K0 - 1) for k in Kx}
        print("\n  x = %g" % xe)
        for lo, hi in S2BANDS:
            sel = ok & ((vc >= lo) & (vc < hi))[None, :]
            if not sel.any():
                print("    [%.2f,%.2f): no cells" % (lo, hi))
                continue
            mx = lambda a: float(a[sel].max())
            print("    [%.2f,%.2f): dev 32/800 %.3g  40/800 %.3g  32/1600 %.3g  40/1600 %.3g;  dM_800 %.3g  dM_1600 %.3g;"
                  "  duv_32 %.3g  duv_40 %.3g;  n40 %d, %d  (%d cells)"
                  % (lo, hi, mx(dev[(32, 800)]), mx(dev[(40, 800)]), mx(dev[(32, 1600)]), mx(dev[(40, 1600)]),
                     mx(np.abs(Kx[(32, 800)] - Kx[(40, 800)]) / K0), mx(np.abs(Kx[(32, 1600)] - Kx[(40, 1600)]) / K0),
                     mx(np.abs(Kx[(32, 800)] - Kx[(32, 1600)]) / K0), mx(np.abs(Kx[(40, 800)] - Kx[(40, 1600)]) / K0),
                     int((sel & (dev[(40, 800)] > 2)).sum()), int((sel & (dev[(40, 1600)] > 2)).sum()),
                     int(sel.sum())), flush=True)
    return 0


def main():
    if sys.argv[1:2] == ["--seed2-1600"]:
        return seed2_1600(sys.argv[2])
    if sys.argv[1:2] == ["--null"]:
        return null_refinement(sys.argv[2])
    if sys.argv[1:2] == ["--seed2-40"]:
        return seed2_40(sys.argv[2])
    if sys.argv[1:2] == ["--seed2"]:
        return seed2(sys.argv[2])
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
