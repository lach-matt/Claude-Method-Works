#!/usr/bin/env python3
"""ampresp5.py -- CERTIFY-10L5-RESULT.md round 2, F5: what the record's own runs say about the constants F and G of
CERTIFY-10L5.md section 2(d)'s closing condition, by the response of the computed solution to its data.  Labels:
computed (floating point); every figure here is a lower estimate of a constant that no theorem yet supplies.

The closing condition (CERTIFY-10L5.md 2(d), deduced there): with R' <= K R + G R^2 + eps on an interval of length T,
F = exp int K, the a posteriori argument closes if delta + int eps < 1/(4 G T F^2).  F bounds the linearised solution
map, G the quadratic remainder.  A linear estimate with constant F must hold for the linearisation about every point
of the segment between two data sets, so by the mean-value theorem
    F >= F_low := sup_D |g(A1) - g(A2)| / sup |data(A1) - data(A2)|,
and the second difference g(1) - 2 g(7/8) + g(3/4), divided by the square of the data step, estimates the quadratic
term (G_low).  The data are dnsolve5's m = y^3 G/2, n = y^3 F/2 on u = -10, linear in the amplitude A; g stands for the
metric's values P, Q, W and log R, compared on the cells all runs keep, at least Nu/40 rows from the cut, with areal
radius >= 1.0 (late5b.py: converged there to v ~ 1.9) and v in [0.5, 1.65].  Runs: the record's ld 3 amplitude runs
(CERTIFY-10L5.md D445; M = 32, 800 x 360, cut 0.9) at A = 1, 7/8, 3/4.

  A1 F_low (secant, A = 7/8 to 1) and G_low (second difference), per field and overall.
  A2 the closing condition's demand at those values: eps_max = 1/(4 G_low T F_low^2), T = 10 (the length of the
     data cone's u-range, and CERTIFY-10L5.md 2(d)'s value), against the record's computed residual 2.5e-3
     (resid5.py, relative to the curvature scale): the ratio of the two (reported).  Since F and G can only be larger,
     and since in dnsolve5's formulation no F exists at all (symbol5.py Y3), this is the least the gap can be.
  Control (A1): the second difference applied to the data themselves (linear in A) must vanish to rounding: a G_low of
     the data above 1e-10 of the solution's fails, so A1's G_low is the solution's nonlinearity, not the step.

  python3 checks/ampresp5.py LD3DIR
"""
import os, sys, warnings
import numpy as np
warnings.filterwarnings('ignore')


def load(path):
    Z = np.load(path)
    x = Z['x']
    m, n, W, R = Z['m'], Z['n'], Z['W'], Z['R']
    P = (2 * (1 + x) * m - (1 - x) * n) / 3; Q = (2 * (1 - x) * n - (1 + x) * m) / 3
    M = len(x)
    rA = (np.nansum(R ** 3 * (np.pi / M * np.sqrt(1 - x ** 2)), -1) / 2) ** (1 / 3)
    mask = Z['mask']
    ok = ~mask
    Nu = mask.shape[0]
    last = np.array([np.nonzero(ok[:, j])[0].max() if ok[:, j].any() else -1 for j in range(mask.shape[1])])
    far = np.zeros_like(ok)
    for j in range(mask.shape[1]):
        far[:max(last[j] - (Nu - 1) // 40 + 1, 0), j] = True
    return dict(P=P, Q=Q, W=W, logR=np.log(R), rA=rA, sel=ok & far, v=Z['v'], u=Z['u'], m0=m[0], n0=n[0])


def main():
    D = sys.argv[1]
    runs = {A: load(os.path.join(D, 'amp%s_M32.npz' % s)) for A, s in ((1.0, '1'), (0.875, '0.875'), (0.75, '0.75'))}
    a, b, c = runs[1.0], runs[0.875], runs[0.75]
    v = a['v']
    sel = a['sel'] & b['sel'] & c['sel'] & (a['rA'] >= 1.0) & (v[None, :] >= 0.5) & (v[None, :] < 1.65)
    dd = max(np.abs(a['m0'] - b['m0']).max(), np.abs(a['n0'] - b['n0']).max())
    print('A1 region: %d cells (v in [0.5, 1.65), areal radius >= 1.0, kept by all three runs); data step sup %.3e'
          % (int(sel.sum()), dd))
    Fl, Gl = 0.0, 0.0
    for f in ('P', 'Q', 'W', 'logR'):
        d1 = np.abs(a[f] - b[f])[sel]; d2 = np.abs(a[f] - 2 * b[f] + c[f])[sel]
        F_ = float(np.nanmax(d1)) / dd; G_ = float(np.nanmax(d2)) / dd ** 2
        Fl, Gl = max(Fl, F_), max(Gl, G_)
        print('   %-4s: sup |g(1) - g(7/8)| %.3e -> F_low %.3g;  sup |second difference| %.3e -> G_low %.3g' % (
            f, np.nanmax(d1), F_, np.nanmax(d2), G_))
    print('A1 overall: F_low = %.3g, G_low = %.3g' % (Fl, Gl))
    dctl = max(np.abs(a['m0'] - 2 * b['m0'] + c['m0']).max(), np.abs(a['n0'] - 2 * b['n0'] + c['n0']).max()) / dd ** 2
    ctl = dctl > 1e-10 * Gl
    print('   control (second difference of the data, linear in A): %.2e -> %s' % (
        dctl, 'passed (bad)' if ctl else 'fails (good)'))
    T = 10.0
    eps_max = 1 / (4 * Gl * T * Fl ** 2)
    print('A2 closing condition at F_low, G_low, T = %g: delta + int eps < %.3e; the record\'s residual 2.5e-3 is %.3g '
          'times that (a lower bound on the gap; in dnsolve5\'s formulation the gap is infinite, symbol5.py Y3)' % (
              T, eps_max, 2.5e-3 / eps_max))
    ok = not ctl and Fl > 0 and Gl > 0
    print('ampresp5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
