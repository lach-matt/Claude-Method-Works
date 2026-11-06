"""g1geom5.py -- CERTIFY-10L5 section 6b (D393): angular convergence of G1 runs in the fields the metric contains.

m is absent from the metric's values at x = -1 (P = -2n/3, Q = 4n/3 there) but enters their x-derivative and the
axis curvature (D395, verifier 178); |dP| is damped by (1 + x) near that axis, so P's convergence does not imply the
axis geometry's. This script compares two saved runs on the same (u, v) grid at different M (`dnsolve5.py --run` or
`dnsolve5v.py --run`), interpolating each field to 65 Chebyshev-Lobatto points in x:

  - per v-band, max |dF| for F = m, P, Q, R, W, s over the cells both runs keep, and again with each v-column's last k
    kept rows (those next to the cut) dropped, for each k given (the extent of convergence depends on k, D395);
  - m on the axis x = -1 (geometric through the axis curvature) and off it (x > -0.9);
  - on the axis x = -1, the size g22 = R^2 e^(8n/3) of the circle that survives there, a function of (u, v) that is the
    same in both gauges (their null foliation is the same), as a relative difference;
  - the last Chebyshev coefficient |c_(M-1)| of m and R in each run, per band: an endpoint value carries the tail
    undamped (T_k(-1) = (-1)^k), so it is trusted only where the tail falls with M.
Labels: computed (floating point, on saved runs).

    python3 checks/g1geom5.py LOW.npz HIGH.npz [k ...]
"""
import sys

import numpy as np

BANDS = [(0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 2.0), (2.0, 2.25), (2.25, 2.5), (2.5, 3.0),
         (3.0, 3.5), (3.5, 4.6)]
XE = np.cos(np.linspace(0, np.pi, 65))


def coeffs(vals, x):
    T = np.cos(np.outer(np.arange(len(x)), np.arccos(x)))
    return vals @ np.linalg.inv(T.T).T


def at(vals, x, xe):
    return coeffs(vals, x) @ np.cos(np.outer(np.arange(len(x)), np.arccos(xe)))


def fields(d):
    x = d["x"]
    F = {k: at(np.nan_to_num(d[k]), x, XE) for k in ("m", "n", "R", "W", "s")}
    F["P"] = (2*(1 + XE)*F["m"] - (1 - XE)*F["n"])/3
    F["Q"] = (2*(1 - XE)*F["n"] - (1 + XE)*F["m"])/3
    xm = np.array([-1.0])
    Rm, nm = at(np.nan_to_num(d["R"]), x, xm)[..., 0], at(np.nan_to_num(d["n"]), x, xm)[..., 0]
    with np.errstate(over="ignore"):
        F["g22"] = Rm**2*np.exp(8*nm/3)
    return F


def interior(ok, k):
    out = ok.copy()
    for j in range(ok.shape[1]):
        idx = np.where(ok[:, j])[0]
        if len(idx) and k:
            out[idx[-k:], j] = False
    return out


def band_max(d, ok, v):
    row = []
    for lo, hi in BANDS:
        sel = ok & ((v >= lo) & (v < hi))[None, :]
        row.append(np.nanmax(np.where(sel, d, np.nan)) if sel.any() else np.nan)
    return row


def tail(d, f):
    return np.abs(coeffs(np.nan_to_num(d[f]), d["x"])[..., -1])


def main():
    a, b = np.load(sys.argv[1]), np.load(sys.argv[2])
    ks = [int(q) for q in sys.argv[3:]] or [10]
    v = a["v"]
    ok = ~(a["mask"] | b["mask"])
    Fa, Fb = fields(a), fields(b)
    print("v-bands:", BANDS)
    sets = [("kept cells", ok)] + [("kept cells, last %d rows dropped" % k, interior(ok, k)) for k in ks]
    for tag, sel in sets:
        for f in ("m", "P", "Q", "R", "W", "s"):
            d = np.abs(Fa[f] - Fb[f]).max(-1)
            print("%-34s max |d%s|: %s" % (tag, f, " ".join("%9.2e" % q for q in band_max(d, sel, v))))
    dm = np.abs(Fa["m"] - Fb["m"])
    for tag, cols in (("m on the axis x = -1", XE < -0.9999), ("m off the axis, x > -0.9", XE > -0.9)):
        print("%-34s max |dm|: %s" % (tag, " ".join("%9.2e" % q for q in band_max(dm[..., cols].max(-1), ok, v))))
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs(Fa["g22"] - Fb["g22"])/np.abs(Fb["g22"])
    print("%-34s rel |dg22| on x = -1: %s" % ("kept cells", " ".join("%9.2e" % q for q in band_max(rel, ok, v))))
    for f in ("m", "R"):
        for tag, d in (("low", a), ("high", b)):
            print("%-34s |c_(M-1)| of %s: %s" % ("tail, %s run (M = %d)" % (tag, len(d["x"])), f,
                                                " ".join("%9.2e" % q for q in band_max(tail(d, f), ok, v))))


if __name__ == "__main__":
    main()
