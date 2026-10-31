"""g1uv5.py -- CERTIFY-10L5 section 6b (D399): convergence in (u, v) of G1 runs at one M, in the metric's fields.

Three saved runs at the same M (`dnsolve5.py --run` or `dnsolve5v.py --run`) on (u, v) grids N, 2N, 4N: the grids
are nested (the stretched u-grid is linspace in arcsinh, the v-grid linspace), so every second point of a finer grid
is a point of the coarser one, and the x-nodes are the same. On the cells all three keep, per v-band, this prints
max |F_N - F_2N| and max |F_2N - F_4N| for F = P, Q, R, W, s, m and their ratio, about 4 for second order; and the
same with each v-column's last k kept rows of the coarsest grid (those next to the cut) dropped. Labels: computed
(floating point, on saved runs).

    python3 checks/g1uv5.py COARSE.npz MID.npz FINE.npz [k]
"""
import sys

import numpy as np

BANDS = [(0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 2.0), (2.0, 2.25), (2.25, 2.5), (2.5, 3.0),
         (3.0, 3.5), (3.5, 4.6)]


def fields(d, step):
    x = d["x"]
    F = {k: np.nan_to_num(d[k][::step, ::step]) for k in ("m", "n", "R", "W", "s")}
    F["P"] = (2*(1 + x)*F["m"] - (1 - x)*F["n"])/3
    F["Q"] = (2*(1 - x)*F["n"] - (1 + x)*F["m"])/3
    return F, d["mask"][::step, ::step]


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
    return np.array(row)


def main():
    c, m, f = (np.load(p) for p in sys.argv[1:4])
    k = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    assert np.allclose(c["x"], m["x"]) and np.allclose(c["x"], f["x"]), "the runs must share M"
    assert np.allclose(c["u"], m["u"][::2]) and np.allclose(c["u"], f["u"][::4]), "the u-grids must be nested"
    assert np.allclose(c["v"], m["v"][::2]) and np.allclose(c["v"], f["v"][::4]), "the v-grids must be nested"
    Fc, mc = fields(c, 1)
    Fm, mm = fields(m, 2)
    Ff, mf = fields(f, 4)
    v = c["v"]
    ok = ~(mc | mm | mf)
    print("v-bands:", BANDS)
    for tag, sel in (("kept cells", ok), ("last %d coarse rows dropped" % k, interior(ok, k))):
        if tag.startswith("last") and not k:
            continue
        for name in ("P", "Q", "R", "W", "s", "m"):
            d1 = band_max(np.abs(Fc[name] - Fm[name]).max(-1), sel, v)
            d2 = band_max(np.abs(Fm[name] - Ff[name]).max(-1), sel, v)
            with np.errstate(divide="ignore", invalid="ignore"):
                ratio = d1/d2
            print("%-28s %s  N-2N: %s" % (tag, name, " ".join("%9.2e" % q for q in d1)))
            print("%-28s %s 2N-4N: %s" % ("", name, " ".join("%9.2e" % q for q in d2)))
            print("%-28s %s ratio: %s" % ("", name, " ".join("%9.2f" % q for q in ratio)))


if __name__ == "__main__":
    main()
