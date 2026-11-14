"""e2band5.py -- E2-PILOT section 3d: the cut-off resolvent of the scalar wave on 5D Tangherlini (mu = 1, r_h = 1), one
harmonic at a time, at real sigma, on I = {r in [1.2, 4]}, by e2pilot5.py's solver (computed; a numerical ODE solve,
not certified). For each l it prints max V_l, kappa_I^2 = min_I (V_l - sigma^2), |W|/(2 sigma), the norm and the
Hilbert-Schmidt norm of chi_I R chi_I on a 161-point grid, E2.5's bound 1/kappa_I^2 where kappa_I^2 > 0, and
max |u_h|^2, max |u_inf|^2 on I.

    python3 checks/e2band5.py SIGMA L_FROM L_TO        (about 45 s per harmonic)
"""
import importlib.util
import os
import sys
import time

import numpy as np

spec = importlib.util.spec_from_file_location('e2', os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                 'e2pilot5.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
V, solve, rstar = m.V, m.solve, m.rstar


def main(s, ls):
    rr = np.linspace(1 + 1e-6, 50, 400001)
    a, b = rstar(m.A_), rstar(m.B_)
    xs = np.linspace(a, b, 161)
    h = xs[1] - xs[0]
    rI = np.linspace(m.A_, m.B_, 2001)
    print('sigma', s, 'I r in [%g,%g], r* in [%.4f,%.4f], Lambda %.4f' % (m.A_, m.B_, a, b, b - a), flush=True)
    i, j = np.meshgrid(np.arange(161), np.arange(161), indexing='ij')
    for l in ls:
        t0 = time.time()
        Vr = V(rr, l)
        vmax, rpk = Vr.max(), rr[Vr.argmax()]
        k2 = (V(rI, l) - s * s).min()
        Uh, Uph = solve(l, s, -40.0, 400.0, 'h', np.concatenate([xs, [400.0]]))
        Ui, Upi = solve(l, s, -40.0, 400.0, 'inf', np.concatenate([[-40.0], xs]))
        Uh, Uph, Ui, Upi = Uh[:-1], Uph[:-1], Ui[1:], Upi[1:]
        Wv = Uh * Upi - Uph * Ui
        W = Wv.mean()
        K = Uh[np.minimum(i, j)] * Ui[np.maximum(i, j)] / W
        nrm, hs = np.linalg.norm(K * h, 2), np.linalg.norm(K) * h
        bound = ('%.4g' % (1 / k2)) if k2 > 0 else '-'
        print('l %2d Vmax %8.3f r_pk %.3f kI2 %9.3f |W|/2s %9.3g Wspread %.1e ||chiRchi|| %.4g HS %.4g 1/kI2 %s '
              'max|uh|^2 %.3g max|ui|^2 %.3g (%.0fs)' % (l, vmax, rpk, k2, abs(W) / (2 * s), np.ptp(np.abs(Wv)) / abs(W),
                                                        nrm, hs, bound, np.abs(Uh).max()**2, np.abs(Ui).max()**2,
                                                        time.time() - t0), flush=True)


if __name__ == '__main__':
    main(float(sys.argv[1]), range(int(sys.argv[2]), int(sys.argv[3])))
