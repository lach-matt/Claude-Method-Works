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
    python3 checks/g1axis5.py --sweep PLAIN24 PLAIN32 PLAIN40 ... (D418)
    python3 checks/g1axis5.py --nodes A B C ... (D420: m and the metric combination P near the axis)
    python3 checks/g1axis5.py --refine C32 C40 F32 F40 (D425: 800 x 360 against 1600 x 720, in P)
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


def sweep(paths):
    """--sweep P24 P32 P40 ...: plain runs at increasing M on one grid; successive |m_M - m_M'| at the event (fixed
    by the first pair, as above) and per v-band, kept by all runs (D418)"""
    runs, ok, m = load(paths)
    u, v = runs[0]["u"], runs[0]["v"]
    rad = GC.areal(runs[1])
    d01 = np.abs(m[0] - m[1])
    sel = ok & (rad >= 1.0) & ((v >= 1.8) & (v < 2.0))[None, :]
    i, j, k = np.unravel_index(np.argmax(np.where(sel[..., None], d01, 0)), d01.shape)
    print("v-bands:", GA.BANDS)
    print("kept by all %d runs: %d cells" % (len(runs), ok.sum()))
    print("event: u = %.3f, v = %.3f, x = %+.4f (node %d), areal radius %.3f" % (u[i], v[j], GA.XE[k], k, rad[i, j]))
    for n in range(len(runs) - 1):
        d = np.abs(m[n] - m[n + 1])
        print("  run %d - run %d: at the event %.3g; max over x at that cell %.3g" % (n, n + 1, d[i, j, k],
                                                                                 d[i, j].max()))
        bands("run %d - run %d" % (n, n + 1), d, ok, rad, v)


def nodes(paths):
    """--nodes A B C ...: at the event (fixed by the first pair, as above), the values of m and of the metric
    combination P = (2(1 + x) m - (1 - x) n)/3 at the nine nodes nearest x = -1, run by run; and per v-band the maxima
    of |P_A - P_B| between consecutive runs. Near x = -1 the equations fix only (1 + x) m_uv, and m drops out of the
    metric there (dnsolve5.py docstring), so m's value at the axis node is not a property of the solution; P is
    (D420)."""
    runs = [np.load(p) for p in paths]
    ok = ~np.any([r["mask"] for r in runs], axis=0)
    F = [GA.fields(r) for r in runs]
    u, v = runs[0]["u"], runs[0]["v"]
    rad = GC.areal(runs[1])
    d01 = np.abs(F[0]["m"] - F[1]["m"])
    sel = ok & (rad >= 1.0) & ((v >= 1.8) & (v < 2.0))[None, :]
    i, j, k = np.unravel_index(np.argmax(np.where(sel[..., None], d01, 0)), d01.shape)
    print("event cell: u = %.3f, v = %.3f, areal radius %.3f; nodes %d-%d (x = %+.4f ... %+.4f)"
          % (u[i], v[j], rad[i, j], len(GA.XE) - 9, len(GA.XE) - 1, GA.XE[-9], GA.XE[-1]))
    for name in ("m", "P"):
        for n, f in enumerate(F):
            print("  %s run %d: %s" % (name, n, " ".join("%+.4f" % q for q in f[name][i, j, -9:])))
    for n in range(len(runs) - 1):
        bands("|P| run %d - run %d" % (n, n + 1), np.abs(F[n]["P"] - F[n + 1]["P"]), ok, rad, v)


def refine(paths):
    """--refine C32 C40 F32 F40: runs at M = 32, 40 on the 800 x 360 grid (C) and on 1600 x 720 (F), whose nodes contain
    the coarse ones (u uniform in arcsinh, v uniform, both doubled). On the coarse nodes kept by all four, per v-band
    over areal radius >= 1 and 1.2, the maxima of |dP| for: the null-grid refinement at fixed M (C32 - F32, C40 - F40)
    and the angular refinement on each grid (C32 - C40, F32 - F40). P is the metric combination (D420). (D425)"""
    c32, c40, f32, f40 = [np.load(p) for p in paths]
    for f in (f32, f40):
        assert np.allclose(f["u"][::2], c32["u"]) and np.allclose(f["v"][::2], c32["v"]), "nested grids"

    def P_of(d, step):
        m = GA.at(np.nan_to_num(d["m"])[::step, ::step], d["x"], GA.XE)
        n = GA.at(np.nan_to_num(d["n"])[::step, ::step], d["x"], GA.XE)
        return (2*(1 + GA.XE)*m - (1 - GA.XE)*n)/3

    ok = ~(c32["mask"] | c40["mask"] | f32["mask"][::2, ::2] | f40["mask"][::2, ::2])
    P = [P_of(c32, 1), P_of(c40, 1), P_of(f32, 2), P_of(f40, 2)]
    v = c32["v"]
    rad = GC.areal(c40)
    print("v-bands:", GA.BANDS)
    print("coarse cells kept by all four: %d" % ok.sum())
    for name, (a, b) in (("(u,v) refinement, M32", (0, 2)), ("(u,v) refinement, M40", (1, 3)),
                         ("M refinement, 800x360", (0, 1)), ("M refinement, 1600x720", (2, 3))):
        bands("|P| " + name, np.abs(P[a] - P[b]), ok, rad, v)


def main():
    if sys.argv[1:2] == ["--sweep"]:
        sweep(sys.argv[2:])
        return
    if sys.argv[1:2] == ["--refine"]:
        refine(sys.argv[2:])
        return
    if sys.argv[1:2] == ["--nodes"]:
        nodes(sys.argv[2:])
        return
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
