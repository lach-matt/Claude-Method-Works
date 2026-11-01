#!/usr/bin/env python3
"""g1amp5.py -- CERTIFY-10L5 section 6b (D445): is G1's failure near the x = -1 axis linear in the waves' amplitude?

D432 found that from v = 2, at areal radius in [1.0, 1.2), neither the angular (M) nor the null-grid refinement
converges, and the section's next step is to separate the axis treatment from the geometry. Here the record's first
seed is run at amplitude A = 1, 7/8, 3/4, 1/2 and 1/4 (dnsolve5.py --run 1 0.9 M 800 360 out 0 ld 3 amp A, D432's
options with the amplitude added; the background, m = n = s = 0, is Tangherlini and has no x-dependence, so the metric
combination P = (2(1 + x) m - (1 - x) n)/3 of D420 is carried by the waves alone) at M = 32 and 40, and compared on the
cells all the runs keep:

  - per v-band, over areal radius >= 1.0 and >= 1.2, the largest |P_32 - P_40| at each A (the angular non-convergence),
    and its exponent in A between successive amplitudes, log2 of the ratio: about 1 if the failure is a property of
    the linearised problem (its discretisation or the axis treatment), larger if it needs the waves' own geometry;
  - the departure from linear response, max |P_A / A - P_A' / A'| at M = 40 for successive amplitudes, against
    max |P_A / A|: how nonlinear the solution itself is in that band;
  - the relative Chebyshev tail of m and n at M = 40 (the largest of the last four coefficients in x over the largest, on
    cells where the largest exceeds 1e-6; as the waves switch on the fields are near rounding noise, D446): how close the
    angular structure comes to M = 40's resolution.

Labels: computed (floating point, on saved runs).

    python3 checks/g1amp5.py DIR      (DIR holds ampA_M32.npz and ampA_M40.npz for each amplitude A run)
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g1geom5 as GA   # noqa: E402
import g1cut5 as GC    # noqa: E402

AMPS = ("1", "0.5", "0.25")


def amps_in(base):
    """the amplitudes with both M = 32 and 40 runs in base, largest first"""
    import glob
    got = [os.path.basename(f)[3:-8] for f in glob.glob(os.path.join(base, "amp*_M32.npz"))]
    return tuple(sorted((a for a in got if os.path.exists(os.path.join(base, "amp%s_M40.npz" % a))),
                        key=float, reverse=True))


def P_of(d):
    m = GA.at(np.nan_to_num(d["m"]), d["x"], GA.XE)
    n = GA.at(np.nan_to_num(d["n"]), d["x"], GA.XE)
    return (2 * (1 + GA.XE) * m - (1 - GA.XE) * n) / 3


def main():
    base = sys.argv[1]
    global AMPS
    AMPS = amps_in(base)
    runs = {(a, M): np.load(os.path.join(base, "amp%s_M%d.npz" % (a, M))) for a in AMPS for M in (32, 40)}
    ref = runs[("1", 32)]
    for d in runs.values():
        assert np.allclose(d["u"], ref["u"]) and np.allclose(d["v"], ref["v"]), "one (u, v) grid"
    ok = ~np.any([d["mask"] for d in runs.values()], axis=0)
    v = ref["v"]
    P = {k: P_of(d) for k, d in runs.items()}
    rad = {a: GC.areal(runs[(a, 40)]) for a in AMPS}
    print("v-bands:", GA.BANDS)
    print("cells kept by all runs: %d of %d" % (ok.sum(), ok.size))
    for a in AMPS:
        print("  cells cut at A = %s: M32 %d, M40 %d" % (a, runs[(a, 32)]["mask"].sum(), runs[(a, 40)]["mask"].sum()))
    for rho in (1.0, 1.2):
        print("areal radius >= %.1f" % rho)
        rows = {}
        for a in AMPS:
            sel = ok & (rad[a] >= rho)
            rows[a] = GA.band_max(np.abs(P[(a, 32)] - P[(a, 40)]).max(-1), sel, v)
            print("  |P_32 - P_40|, A = %-4s %s" % (a, " ".join("%8.1e" % q for q in rows[a])))
        pairs = list(zip(AMPS[:-1], AMPS[1:]))
        for a, b in pairs:
            ex = [math.log(x / y) / math.log(float(a) / float(b)) if (x > 0 and y > 0) else float("nan")
                  for x, y in zip(rows[a], rows[b])]
            print("  exponent in A, %s/%s:   %s" % (a, b, " ".join("%8.2f" % q for q in ex)))
        for a, b in pairs:
            sel = ok & (rad[a] >= rho)
            dev = np.abs(P[(a, 40)] / float(a) - P[(b, 40)] / float(b)).max(-1)
            lin = np.abs(P[(a, 40)] / float(a)).max(-1)
            print("  |P_A/A - P_A'/A'|, %s/%s: %s" % (a, b, " ".join("%8.1e" % q for q in GA.band_max(dev, sel, v))))
            print("  |P_A/A|,       A = %-4s %s" % (a, " ".join("%8.1e" % q for q in GA.band_max(lin, sel, v))))
    print("relative Chebyshev tail of m and n at M = 40 (largest of the last four coefficients over the largest), "
          "areal radius >= 1.0")
    for a in AMPS:
        d = runs[(a, 40)]
        rel = 0
        for f in ("m", "n"):
            c = np.abs(GA.coeffs(np.nan_to_num(d[f]), d["x"]))
            rel = np.maximum(rel, np.where(c.max(-1) > 1e-6, c[..., -4:].max(-1) / (c.max(-1) + 1e-300), np.nan))
        sel = ok & (rad[a] >= 1.0)
        print("  A = %-5s %s" % (a, " ".join("%8.1e" % q for q in GA.band_max(rel, sel, v))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
