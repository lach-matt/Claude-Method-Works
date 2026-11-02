#!/usr/bin/env python3
"""resid5.py -- CERTIFY-10L5-RESULT.md section 2: the Einstein residual of a smoothed approximant built from a
double-null run, on a box where the run converges, in floating point.  Labels: computed (floating point; NOT certified:
the certified version is what section 2 finds out of reach, and why).

The approximant: on the box Q = {u in [u_a, u_b], v in [v_a, v_b]} x [-1, 1] of dnsolve5.py's coordinates, every field
F in (R, m, n, W, s) is fitted, at each angular node, by a tensor Chebyshev series of degrees (D_xi, D_v) in
(xi, v), xi = arcsinh((u + 1)/a) the run's own uniform coordinate, least squares over the run's nodes; in x it is the
run's own Chebyshev-Gauss interpolant.  So g_app is an explicit smooth metric of the class.  Its Ricci tensor, all
eight nonzero components from the exact symbolic Ricci tensor of the ansatz (dnull5.ricci), is evaluated at the
midpoints between the run's (u, v) nodes and at its angular nodes, in the null-orthonormal frame
    l = d_v,  nhat = e^{-2W} (d_u + beta d_x)/2  (g(l, nhat) = -1),  e_x = d_x/sqrt(Gx),  e_i = d_phi_i/sqrt(g_ii),
and compared with the curvature scale sqrt(K_0) = sqrt(72)/R^4 of Tangherlini at the same areal radius.

  Q1 the fit: max |F_app - F_run| over the run's nodes in Q, per field (the fit must be well below the run's own (u, v)
     error, about 1e-3 in P on this region at 800 x 360, CERTIFY-10L5.md D399).
  Q2 the residual: max over Q of each frame component of Ric[g_app], absolute and over sqrt(K_0); and the same for the
     next coarser run (400 x 180), so that the ratio shows whether the residual is the discretisation's (ratio ~ 4).
  Control: the same approximant with W replaced by W + 0.01 v (a lapse off the solution, dnsolve5.py S3's control):
     its residual must exceed the approximant's by a factor of at least 10.

  python3 checks/resid5.py RUNDIR fine_run coarse_run [u_a u_b v_a v_b D_xi D_v]
"""
import os, sys, time, warnings, importlib.util
import numpy as np
import sympy as sp
from numpy.polynomial import chebyshev as Ch
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import bondisph5 as B                                                           # noqa: E402

_spec = importlib.util.spec_from_file_location('dnsolve5', os.path.join(TOP, 'dnsolve5.py'))
d5 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(d5)
NAMES = d5.names
COMPS = [((0, 0), 'uu'), ((0, 1), 'uv'), ((0, 2), 'ux'), ((1, 1), 'vv'), ((1, 2), 'vx'), ((2, 2), 'xx'),
         ((3, 3), '11'), ((4, 4), '22')]
A_GRID = 0.002


def ricci_funcs():
    Ric = d5.dn.ricci(d5.g, d5.C)
    exprs = [d5.tosym(Ric[i, j]) for (i, j), _ in COMPS]
    syms = sorted(set().union(*[e.free_symbols for e in exprs]), key=str)
    f = sp.lambdify(syms, exprs, 'numpy', cse=True)
    return f, [str(s) for s in syms]


def fit(Z, ua, ub, va, vb, Dxi, Dv):
    u, v = Z['u'], Z['v']
    iu = np.nonzero((u >= ua) & (u <= ub))[0]; jv = np.nonzero((v >= va) & (v <= vb))[0]
    assert not Z['mask'][np.ix_(iu, jv)].any(), 'the box contains masked cells'
    xi = np.arcsinh((u[iu] + 1) / A_GRID)
    xa, xb = np.arcsinh((ua + 1) / A_GRID), np.arcsinh((ub + 1) / A_GRID)
    t = (2 * xi - xa - xb) / (xb - xa); s = (2 * v[jv] - va - vb) / (vb - va)
    T, S = np.meshgrid(t, s, indexing='ij')
    V = Ch.chebvander2d(T.ravel(), S.ravel(), [Dxi, Dv])
    coef, err = {}, {}
    pinv = np.linalg.pinv(V)
    for k in NAMES:
        A = Z[k][np.ix_(iu, jv)]                     # (nu, nv, M)
        C = pinv @ A.reshape(-1, A.shape[-1])          # ((Dxi+1)(Dv+1), M)
        coef[k] = C.reshape(Dxi + 1, Dv + 1, -1)
        err[k] = float(np.abs(V @ C - A.reshape(-1, A.shape[-1])).max())
    geo = dict(xa=xa, xb=xb, va=va, vb=vb, iu=iu, jv=jv)
    return coef, err, geo


def evaluate(coef, geo, Z, t, s, wshift=0.0):
    """fields and derivatives (u, v, x up to second order) at the points (t, s) x the angular nodes"""
    M = len(Z['x'])
    D1 = B.diff_matrix(M)
    hx = (geo['xb'] - geo['xa']) / 2; hv = (geo['vb'] - geo['va']) / 2
    xi = geo['xa'] + (t + 1) * hx
    J = A_GRID * np.cosh(xi)                          # du/dxi
    th = np.tanh(xi)
    out = {'x': Z['x'][None, :]}
    vv = geo['va'] + (s + 1) * hv
    for k in NAMES:
        C = coef[k]
        val = {}
        for a in range(3):
            for b in range(3 - a):
                Cd = C
                for _ in range(a):
                    Cd = Ch.chebder(Cd, axis=0)
                for _ in range(b):
                    Cd = Ch.chebder(Cd, axis=1)
                Vt = Ch.chebvander(t, Cd.shape[0] - 1); Vs = Ch.chebvander(s, Cd.shape[1] - 1)
                val[(a, b)] = np.einsum('pi,pj,ijm->pm', Vt, Vs, Cd) / hx ** a / hv ** b
        if k == 'W' and wshift:
            val[(0, 0)] = val[(0, 0)] + wshift * vv[:, None]
            val[(0, 1)] = val[(0, 1)] + wshift
        f = val[(0, 0)]; f_xi = val[(1, 0)]; f_xixi = val[(2, 0)]
        out[k] = f
        out[k + '_u'] = f_xi / J[:, None]
        out[k + '_uu'] = (f_xixi - th[:, None] * f_xi) / J[:, None] ** 2
        out[k + '_v'] = val[(0, 1)]
        out[k + '_vv'] = val[(0, 2)]
        out[k + '_uv'] = val[(1, 1)] / J[:, None]
        out[k + '_x'] = f @ D1.T
        out[k + '_xx'] = f @ D1.T @ D1.T
        out[k + '_ux'] = out[k + '_u'] @ D1.T
        out[k + '_vx'] = out[k + '_v'] @ D1.T
    return out


def frame(env, R8):
    """Ricci components -> the null-orthonormal frame's"""
    x = env['x']
    R, W, m, n, s = env['R'], env['W'], env['m'], env['n'], env['s']
    P = (2 * (1 + x) * m - (1 - x) * n) / 3; Q = (2 * (1 - x) * n - (1 + x) * m) / 3
    Gx = R ** 2 * np.exp(-2 * (P + Q)) / (4 * (1 - x ** 2)); be = (1 - x ** 2) * s
    g11 = R ** 2 * (1 + x) / 2 * np.exp(2 * P); g22 = R ** 2 * (1 - x) / 2 * np.exp(2 * Q)
    Ruu, Ruv, Rux, Rvv, Rvx, Rxx, R11, R22 = R8
    e2 = np.exp(-2 * W) / 2
    return {'ll': Rvv, 'ln': e2 * (Ruv + be * Rvx), 'nn': e2 ** 2 * (Ruu + 2 * be * Rux + be ** 2 * Rxx),
            'lx': Rvx / np.sqrt(Gx), 'nx': e2 * (Rux + be * Rxx) / np.sqrt(Gx), 'xx': Rxx / Gx, '11': R11 / g11,
            '22': R22 / g22}


def residual(Z, args, ricf, names, wshift=0.0):
    ua, ub, va, vb, Dxi, Dv = args
    coef, err, geo = fit(Z, ua, ub, va, vb, Dxi, Dv)
    u, v = Z['u'], Z['v']
    iu, jv = geo['iu'], geo['jv']
    um = 0.5 * (u[iu[:-1]] + u[iu[1:]]); vm = 0.5 * (v[jv[:-1]] + v[jv[1:]])
    xi = np.arcsinh((um + 1) / A_GRID)
    t = (2 * xi - geo['xa'] - geo['xb']) / (geo['xb'] - geo['xa']); s = (2 * vm - va - vb) / (vb - va)
    T, S = np.meshgrid(t, s, indexing='ij')
    env = evaluate(coef, geo, Z, T.ravel(), S.ravel(), wshift)
    vals = ricf(*[np.broadcast_to(env[k], env['R'].shape) if k != 'x' else env['x'] for k in names])
    R8 = [np.broadcast_to(np.asarray(a, float), env['R'].shape) for a in vals]
    fr = frame(env, R8)
    scale = np.sqrt(72) / env['R'] ** 4
    res = {k: (float(np.abs(a).max()), float((np.abs(a) / scale).max())) for k, a in fr.items()}
    return res, err


def main():
    rundir, fine, coarse = sys.argv[1:4]
    args = [float(a) for a in sys.argv[4:8]] + [int(a) for a in sys.argv[8:10]] if len(sys.argv) > 4 else \
        [-4.0, -1.1, 0.55, 1.6, 24, 30]
    t0 = time.time()
    ricf, names = ricci_funcs()
    print('box: u in [%.2f, %.2f], v in [%.2f, %.2f], x in [-1, 1] (angular nodes); degrees D_xi %d, D_v %d'
          % tuple(args), flush=True)
    out = {}
    for nm in (fine, coarse):
        Z = B.load(os.path.join(rundir, nm + '.npz'))
        res, err = residual(Z, args, ricf, names)
        out[nm] = res
        print('  %s: Q1 fit error per field: %s' % (nm, ', '.join('%s %.1e' % (k, e) for k, e in err.items())),
              flush=True)
        print('      Q2 residual, frame components, max |.| and (max |.|/sqrt(K_0)):', flush=True)
        items = ['%s %.2e (%.2e)' % (k, a, b) for k, (a, b) in res.items()]
        for q in range(0, len(items), 4):
            print('         ' + ', '.join(items[q:q + 4]), flush=True)
    worst_f = max(b for a, b in out[fine].values()); worst_c = max(b for a, b in out[coarse].values())
    print('  worst relative residual: %.2e (%s), %.2e (%s), ratio %.2f' % (worst_f, fine, worst_c, coarse,
                                                                       worst_c / worst_f), flush=True)
    Z = B.load(os.path.join(rundir, fine + '.npz'))
    resc, _ = residual(Z, args, ricf, names, wshift=0.01)
    worst_ctl = max(b for a, b in resc.values())
    good = worst_ctl > 10 * worst_f
    print('  control (W + 0.01 v): worst relative residual %.2e, %.0f times the approximant\'s -> %s'
          % (worst_ctl, worst_ctl / worst_f, 'fails (good)' if good else 'passed (bad)'), flush=True)
    print('resid5: %s (%.0f s)' % ('control behaves' if good else 'CONTROL FAILED', time.time() - t0))
    return 0 if good else 1


if __name__ == '__main__':
    sys.exit(main())
