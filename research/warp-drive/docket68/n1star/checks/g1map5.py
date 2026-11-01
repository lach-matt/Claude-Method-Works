#!/usr/bin/env python3
"""g1map5.py -- CERTIFY-10L5 section 6b (D458): G1's failure at x = -1 on an angular grid concentrated at the axis.

D445-D446 left three readings of the non-convergence near x = -1 at the record's amplitude A = 1 apart: a singularity,
a steep smooth feature, and an axis defect of the scheme. D458 measured on the saved runs that the failure starts at
the node next to the axis in m (the field the metric multiplies by 1 + x there) and becomes a node-to-node alternation
with a flat Chebyshev spectrum; that the jump of the angular tail does not move when the rounding at the axis nodes
rises about 800-fold (M = 32 with and without the long-double axis solve); and (D432) that halving the null step does
not move it either. Here the same runs are repeated on dnsolve5's mapped grid (`map 0.3`: the angular spacing at x = -1
0.7 times the plain one, as a plain M of 46 and 57 would give there), at A = 1 and 3/4, M = 32 (ld 3) and 40 (ld 4,
since the mapped node next to the axis sits closer to it), and compared with the plain ld 3 runs on the cells all four
keep at that amplitude:

  - per v-band, at areal radius >= 1.0, the largest |P_32 - P_40| on each grid (P = (2(1 + x) m - (1 - x) n)/3 on a
    common set of 65 angles, each run interpolated in its own collocation variable), and |P_40 mapped - P_40 plain|;
  - the angular tail of the parts that enter the metric, (1 + x) m and (1 - x) n: the largest of the last four
    Chebyshev coefficients (in each run's own variable), maximised per band;
  - the invariant size of the circle that does not shrink at x = -1, g_22 = R^2 e^(8 n / 3) there, compared between
    M = 32 and 40 on each grid (relative difference), per band.

If the failure is a steep smooth feature that M = 40 fails to resolve, concentrating the nodes delays the tail's jump
and shrinks the M-difference; if it is a singularity of the solution or a defect of the axis treatment, it does not.

Measured (D458, corrected D462): the mapped pair's difference is carried by its M = 40 run alone, whose axis-node
rounding is 40 times plain M = 40's and whose error peaks near x = +1, the coarser side; the mapped M = 32 run tracks the
plain runs. The onset tail grows with node proximity and with axis rounding together. So the mapped grid does not
separate the readings; the alternatives found are the scheme's, but no mechanism is shown.

Labels: computed (floating point, on saved runs).

    python3 checks/g1map5.py PLAIN MAPPED   (PLAIN holds ampA_M32.npz and ampA_M40.npz of dnsolve5.py --run 1 0.9 M
                                             800 360 out 0 ld 3 amp A; MAPPED the same with ld 3 / ld 4 and map 0.3)
    python3 checks/g1map5.py --onset DIR ...  (the onset tails and the alternation, per directory)
"""
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g1geom5 as GA   # noqa: E402

_spec = importlib.util.spec_from_file_location("dnsolve5", os.path.join(HERE, "..", "dnsolve5.py"))
DN = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(DN)


def load(fn):
    d = np.load(fn)
    a = float(d["xmap"]) if "xmap" in d.files else 0.0
    M = len(d["x"])
    xi = DN.cheb_gauss(M)[0]
    assert np.allclose(DN.xgrid(M, a)[0], d["x"]), "nodes"
    out = {k: d[k] for k in ("u", "v", "mask")}
    out.update(a=a, M=M, xi=xi, x=d["x"])
    for k in ("R", "m", "n"):
        out[k] = np.nan_to_num(d[k])
    return out


def at(r, vals, xe):
    """vals at the angles xe, interpolated in the run's own collocation variable"""
    return GA.at(vals, r["xi"], DN.xi_of(xe, r["a"]) if r["a"] else xe)


def areal(r):
    """(the mean of R^3 over x in [-1, 1])^(1/3), by Clenshaw-Curtis-type weights in xi with dx/dxi included"""
    ph = np.arccos(r["xi"]); a = r["a"]
    jac = np.sin(ph + a * np.sin(ph)) * (1 + a * np.cos(ph)) / np.sin(ph)
    c = GA.coeffs(r["R"]**3 * jac, r["xi"])
    k = np.arange(r["M"])
    with np.errstate(divide="ignore"):
        w = np.where(k % 2 == 0, 2.0 / (1.0 - k.astype(float)**2), 0.0)
    return np.cbrt(np.maximum(c @ w, 0) / 2)


def P_of(r):
    m, n = at(r, r["m"], GA.XE), at(r, r["n"], GA.XE)
    return (2 * (1 + GA.XE) * m - (1 - GA.XE) * n) / 3


def tail(r):
    t = 0
    for f, wgt in (("m", 1 + r["x"]), ("n", 1 - r["x"])):
        c = np.abs(GA.coeffs(r[f] * wgt, r["xi"]))
        t = np.maximum(t, c[..., -4:].max(-1))
    return t


def g22(r):
    xm = np.array([-1.0])
    R, n = at(r, r["R"], xm)[..., 0], at(r, r["n"], xm)[..., 0]
    with np.errstate(over="ignore"):
        return R**2 * np.exp(8 * n / 3)


def row(label, vals):
    print("  %-34s %s" % (label, " ".join("%8.1e" % q for q in vals)))


def onset(dirs):
    """--onset: per band of 0.1 in v, the tail of (1 + x) m and (1 - x) n at areal radius >= 1 for every amplitude and M
    in each directory (the seed test, D458: the same scan with and without the long-double axis solve), and m at the
    eight nodes next to x = -1 where |P_32 - P_40| is largest in [2, 2.25) at A = 1 (the alternation)"""
    vs = np.arange(1.0, 2.55, 0.1)
    for b in dirs:
        print("  %s" % b)
        for a in ("0.25", "0.5", "0.75", "0.875", "1"):
            for M in (32, 40):
                fn = os.path.join(b, "amp%s_M%d.npz" % (a, M))
                if not os.path.exists(fn):
                    continue
                rr = load(fn)
                sel = ~rr["mask"] & (areal(rr) >= 1.0)
                t = np.where(sel, tail(rr), np.nan)
                v = rr["v"]
                row = [np.nanmax(t[:, (v >= lo) & (v < lo + 0.1)]) if np.any(sel[:, (v >= lo) & (v < lo + 0.1)])
                       else np.nan for lo in vs]
                print("    A %-5s M %d: %s" % (a, M, " ".join("%.0e" % q for q in row)), flush=True)
                del rr
        f32, f40 = (os.path.join(b, "amp1_M%d.npz" % M) for M in (32, 40))
        if os.path.exists(f32) and os.path.exists(f40):
            r32, r40 = load(f32), load(f40)
            ok = ~(r32["mask"] | r40["mask"]) & (areal(r40) >= 1.0) & ((r40["v"] >= 2.0) & (r40["v"] < 2.25))[None, :]
            dP = np.where(ok[..., None], np.abs(P_of(r32) - P_of(r40)), -1)
            i, k, _ = np.unravel_index(np.argmax(dP), dP.shape)
            print("    A = 1, M = 40, the cell of largest |P_32 - P_40| in [2, 2.25) (v = %.3f): m at the eight nodes "
                  "next to x = -1: %s" % (r40["v"][k], " ".join("%.3f" % q for q in r40["m"][i, k][-8:])), flush=True)
    print("  v-bands from", " ".join("%.1f" % q for q in vs))
    return 0


def main():
    if sys.argv[1] == "--onset":
        return onset(sys.argv[2:])
    plain, mapped = sys.argv[1], sys.argv[2]
    amps = [a for a in ("1", "0.75") if all(os.path.exists(os.path.join(b, "amp%s_M%d.npz" % (a, M)))
                                           for b in (plain, mapped) for M in (32, 40))]
    print("v-bands:", " ".join("[%g, %g)" % b for b in GA.BANDS))
    for a in amps:
        runs = {(g, M): load(os.path.join(b, "amp%s_M%d.npz" % (a, M)))
                for g, b in (("plain", plain), ("mapped", mapped)) for M in (32, 40)}
        ref = runs[("plain", 40)]
        for r in runs.values():
            assert np.allclose(r["u"], ref["u"]) and np.allclose(r["v"], ref["v"]), "one (u, v) grid"
        ok = ~np.any([r["mask"] for r in runs.values()], axis=0)
        rad = areal(runs[("mapped", 40)])
        sel = ok & (rad >= 1.0)
        v = ref["v"]
        print("A = %s: cells kept by all four runs %d of %d; at areal radius >= 1.0: %d"
              % (a, ok.sum(), ok.size, sel.sum()))
        P = {k: P_of(r) for k, r in runs.items()}
        for g in ("plain", "mapped"):
            row("|P_32 - P_40|, %s" % g, GA.band_max(np.abs(P[(g, 32)] - P[(g, 40)]).max(-1), sel, v))
        row("|P_40 mapped - P_40 plain|", GA.band_max(np.abs(P[("mapped", 40)] - P[("plain", 40)]).max(-1), sel, v))
        for k, r in sorted(runs.items()):
            row("tail of (1+x)m, (1-x)n: %s M %d" % k, GA.band_max(tail(r), sel, v))
        for g in ("plain", "mapped"):
            q32, q40 = g22(runs[(g, 32)]), g22(runs[(g, 40)])
            row("g_22(x = -1), M32 vs 40, %s" % g, GA.band_max(np.abs(q32 / q40 - 1), sel, v))
        row("g_22(x = -1), mapped vs plain, M40",
            GA.band_max(np.abs(g22(runs[("mapped", 40)]) / g22(runs[("plain", 40)]) - 1), sel, v))
        del runs, P
    return 0


if __name__ == "__main__":
    sys.exit(main())
