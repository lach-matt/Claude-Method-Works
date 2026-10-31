"""g1axis5.py -- CERTIFY-10L5 section 6b (D413): does G1's failure at the x = -1 axis depend on the axis treatment?

Four dnsolve5.py runs at lambda = 1, r_cut = 0.9, 800 x 360, on one (u, v) grid: M = 24 and 32 with the plain axis
treatment, and M = 24 and 32 with the `reg` option (m_uv recovered at the axis by exact division, D352). Cells kept by
all four are compared. The event is the cell and Lobatto node of largest |m_24 - m_32| (plain) over areal radius >= 1
on v in [1.8, 2) (D410; the areal radius as in g1cut5.py). Printed:

  - |m_24 - m_32| at the event for each treatment, and per v-band (areal radius >= 1.0 and 1.2);
  - |m_plain - m_reg| at M = 24 and 32, at the event and per v-band: how far the two treatments agree;
  - with a fifth run (plain, M = 40, same grid), |m_32 - m_40| at the event and per band: the angular convergence.

Labels: computed (floating point, on saved runs).

    python3 checks/g1axis5.py PLAIN24 PLAIN32 REG24 REG32 [PLAIN40]
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g1geom5 as GA   # noqa: E402
import g1cut5 as GC    # noqa: E402


def load(paths):
    runs = [np.load(p) for p in paths]
    for r in runs[1:]:
        assert np.allclose(r["u"], runs[0]["u"]) and np.allclose(r["v"], runs[0]["v"]), "one (u, v) grid"
    ok = ~np.any([r["mask"] for r in runs], axis=0)
    return runs, ok, [GA.fields(r)["m"] for r in runs]


def bands(name, d, ok, rad, v):
    for rho in (1.0, 1.2):
        sel = ok & (rad >= rho)
        print("  %-22s areal >= %.1f: %s" % (name, rho, " ".join("%8.1e" % q for q in GA.band_max(d.max(-1), sel, v))))


def main():
    paths = sys.argv[1:]
    assert len(paths) in (4, 5), __doc__
    runs, ok, m = load(paths)
    u, v = runs[0]["u"], runs[0]["v"]
    rad = GC.areal(runs[1])
    d_plain, d_reg = np.abs(m[0] - m[1]), np.abs(m[2] - m[3])
    sel = ok & (rad >= 1.0) & ((v >= 1.8) & (v < 2.0))[None, :]
    i, j, k = np.unravel_index(np.argmax(np.where(sel[..., None], d_plain, 0)), d_plain.shape)
    print("v-bands:", GA.BANDS)
    print("kept by all runs: %d cells" % ok.sum())
    print("event: u = %.3f, v = %.3f, x = %+.4f (node %d), areal radius %.3f" % (u[i], v[j], GA.XE[k], k, rad[i, j]))
    print("  |m24 - m32| there: plain %.3g, reg %.3g" % (d_plain[i, j, k], d_reg[i, j, k]))
    bands("plain M24-M32", d_plain, ok, rad, v)
    bands("reg M24-M32", d_reg, ok, rad, v)
    for M, (a, b) in ((24, (0, 2)), (32, (1, 3))):
        d = np.abs(m[a] - m[b])
        print("  |m_plain - m_reg| at M = %d, event: %.3g" % (M, d[i, j, k]))
        bands("plain-reg M%d" % M, d, ok, rad, v)
    if len(paths) == 5:
        d40 = np.abs(m[1] - m[4])
        print("  |m32 - m40| (plain) at the event: %.3g (against %.3g for M24-M32)" % (d40[i, j, k], d_plain[i, j, k]))
        bands("plain M32-M40", d40, ok, rad, v)


if __name__ == "__main__":
    main()
