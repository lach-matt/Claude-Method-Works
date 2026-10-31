"""axisdrift5.py -- CERTIFY-10L5 section 6b (D381): how far dnsolve5.py's shift drags the angle toward each axis.

In dnsolve5.py's metric the angle enters as dx - (1 - x^2) s du, so along an ingoing null generator orthogonal to the
symmetry orbits (the curves of d_u + (1 - x^2) s d_x, which carry the ingoing wave) x obeys dx/du = (1 - x^2) s. Near
x = -1 this gives d ln(1 + x)/du = 2 s(x = -1), and near x = +1, d ln(1 - x)/du = -2 s(x = +1). This script integrates
those rates in u at fixed v from the initial cone, at the Chebyshev nodes next to each axis, on a saved run
(`dnsolve5.py --run ... out.npz`), and prints the most negative value per v: ln of the factor by which a fixed geometric
angle near that axis has been pressed toward it, against ln of the first node's distance from the axis. Labels: computed
(trapezoid in u on the run's grid); a kinematic diagnostic of the coordinate, not of the geometry.

    python3 checks/axisdrift5.py RUN.npz [v ...]
"""
import sys

import numpy as np


def drift(path, vs):
    d = np.load(path)
    u, v, x, s, R = d["u"], d["v"], d["x"], d["s"], d["R"]
    im, ip = np.argmin(x), np.argmax(x)
    du = np.diff(u)[:, None]

    def cum(sx):
        return np.vstack([np.zeros((1, sx.shape[1])), np.cumsum(0.5*(sx[1:] + sx[:-1])*du, axis=0)])

    cm, cp = 2*cum(s[:, :, im]), -2*cum(s[:, :, ip])
    print("%s: first node ln(1 - |x|) = %.2f" % (path, np.log(1 - abs(x[ip]))))
    for vv in vs:
        j = np.argmin(abs(v - vv))
        out = []
        for c, k in ((cm, im), (cp, ip)):
            col = np.where(np.isfinite(c[:, j]), c[:, j], np.nan)
            i = np.nanargmin(col)
            out.append((col[i], u[i], R[i, j, k]))
        print("  v = %.2f  x = -1: %7.2f at u = %.4f (R = %.2f)   x = +1: %7.2f at u = %.4f (R = %.2f)"
              % ((v[j],) + out[0] + out[1]))


if __name__ == "__main__":
    vs = [float(a) for a in sys.argv[2:]] or [1.4, 1.5, 1.6, 1.65, 1.7, 1.8, 2.0, 2.5, 3.0, 3.3]
    drift(sys.argv[1], vs)
