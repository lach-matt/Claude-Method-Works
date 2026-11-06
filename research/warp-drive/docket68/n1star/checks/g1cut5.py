"""g1cut5.py -- CERTIFY-10L5 section 6b (D410): does G1's failure in angle follow the cut, or stay at the same events?

For each cut r_cut, two dnsolve5.py runs at M = 24 and 32 on the same (u, v) grid (u in [-10, -r_cut], so the grids
differ between cuts and cells are compared by event through an invariant). The invariant is the areal radius of the
section, (V/2pi^2)^(1/3) with V = pi^2 int R^3 dx (section 6b, D392), computed from R's Chebyshev coefficients. Per
cut this prints:

  - the onset: the least v at which a kept cell has max_x |m_24 - m_32| > tau (tau = 1e-3, 1e-2), with that cell's
    u, its number of rows from its column's last kept row, and its areal radius;
  - per v-band, max |dm| and |dP| over the kept cells with areal radius >= rho, for rho = 0.9, 1.0, 1.2: the same
    physical region for every cut, as long as each cut keeps it.

If the failure is the solution's (or the axis treatment's at a given geometry), it appears at the same areal radius
for every cut; if the cut drives it, it moves with the cut and the fixed-radius region converges. Labels: computed
(floating point, on saved runs).

    python3 checks/g1cut5.py RC1 LOW1 HIGH1 [RC2 LOW2 HIGH2 ...]
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g1geom5 as GA   # noqa: E402


def areal(d):
    x = d["x"]
    c = GA.coeffs(np.nan_to_num(d["R"])**3, x)
    k = np.arange(len(x))
    with np.errstate(divide="ignore"):
        w = np.where(k % 2 == 0, 2.0/(1.0 - k.astype(float)**2), 0.0)
    return np.cbrt(np.maximum(c @ w, 0)/2)


def analyse(rc, lo, hi):
    a, b = np.load(lo), np.load(hi)
    assert np.allclose(a["u"], b["u"]) and np.allclose(a["v"], b["v"]), "the pair must share its (u, v) grid"
    u, v = a["u"], a["v"]
    ok = ~(a["mask"] | b["mask"])
    Fa, Fb = GA.fields(a), GA.fields(b)
    dm = np.abs(Fa["m"] - Fb["m"]).max(-1)
    dP = np.abs(Fa["P"] - Fb["P"]).max(-1)
    rad = areal(b)
    print("r_cut = %s: kept %d cells" % (rc, ok.sum()))
    for tau in (1e-3, 1e-2):
        bad = ok & (dm > tau)
        if not bad.any():
            print("  onset |dm| > %g: none" % tau)
            continue
        j = np.where(bad.any(0))[0][0]
        i = np.where(bad[:, j])[0][0]
        last = np.where(ok[:, j])[0][-1]
        print("  onset |dm| > %g: v = %.3f, u = %.3f, %d rows from the cut, areal radius %.3f, R at x = -1 node %.3f"
              % (tau, v[j], u[i], last - i, rad[i, j], float(np.nan_to_num(b["R"])[i, j, -1])))
    for rho in (0.9, 1.0, 1.2):
        sel = ok & (rad >= rho)
        print("  areal >= %.1f: max |dm| %s" % (rho, " ".join("%8.1e" % q for q in GA.band_max(dm, sel, v))))
        print("  %15s max |dP| %s" % ("", " ".join("%8.1e" % q for q in GA.band_max(dP, sel, v))))


def main():
    args = sys.argv[1:]
    print("v-bands:", GA.BANDS)
    for k in range(0, len(args), 3):
        analyse(*args[k:k + 3])


if __name__ == "__main__":
    main()
