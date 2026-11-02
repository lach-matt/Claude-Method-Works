#!/usr/bin/env python3
"""jordan5.py -- CERTIFY-10L5-RESULT.md round 2, F5: symbol5.py Y3's frozen-coefficient growth, measured in the two
double-null schemes with their variable coefficients.  Labels: computed (floating point).

symbol5.py Y1: in dnsolve5.py's formulation the principal symbol has a 2 x 2 Jordan block at the eigenvalue 0, whose
left null vector is d zeta, zeta = W + 2 log R + P + Q; so a source with a component along d zeta (a W_uv source has
it, with weight 1) drives the partner, which is then driven by the source's second x-derivative: at angular frequency
k the response grows like k^2 (Y3).  In cpsolve5.py's constraint-preserving formulation (symbol5.py Y2) W is a wave
mode, and the same source has a response bounded in k.

The experiment.  Tangherlini (dnsolve5's data with amplitude 0), M = 16, 200 x 30 cells (dnsolve5's grid for
v <= 1.5, Nv = 90 for v to 4.5), cut 0.54.  A source eps phi(u, v) T_k(x) is added to the W_uv row (phi = sin^2 bump on
u in [-6, -3], v in [0.2, 0.5]; eps = 1e-7), at k = 0, 2, 4, 6, 8; the response is the largest |delta f|/eps over
f in (R, m, n, W) and the kept cells with u <= -1.5, v in [0.6, 1.5], delta f the difference from the unperturbed run.

  J1 free scheme (dnsolve5's equations, its diamond loop reproduced here with the source hook): the response at k = 8
     is at least 8 times that at k = 2 (Y3 predicts 16).
  J2 constraint-preserving scheme (cpsolve5.run with the same source): the response at k = 8 is at most twice that at
     k = 2.
  Control (J1): in the free scheme a source along a right eigenvector of the semisimple eigenvalue (symbol5.py Y1, the
     wave sector, computed per node from A at Tangherlini's R), which has no component along d zeta: its response at
     k = 8 must stay within twice that at k = 2, so the growth of J1 is the Jordan block's, not any source's.

  python3 checks/jordan5.py
"""
import os, sys, time, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


d5 = _load('dnsolve5', os.path.join(TOP, 'dnsolve5.py'))
cp = _load('cpsolve5', os.path.join(HERE, 'cpsolve5.py'))
EPS = 1e-7
KS = (0, 2, 4, 6, 8)


def free_run(E, G, data, r_cut, source=None, iters=3):
    """dnsolve5.run's diamond loop, unchanged except for the added source in (R, m, n, W)_uv"""
    Nu, Nv, M = G.Nu, G.Nv, G.M
    A = {f: np.full((Nu + 1, Nv + 1, M), np.nan) for f in d5.ALL}
    tmp = {f: np.full((Nu + 1, Nv + 1, M), np.nan) for f in cp.ALL}
    cp.data_cone(E, G, data, tmp)
    for f in d5.ALL:
        A[f][:, 0] = tmp[f][:, 0]; A[f][0] = tmp[f][0]
    mask = np.zeros((Nu + 1, Nv + 1), bool)
    mask[:, 0] = A['R'][:, 0, 0] < r_cut
    mask[0, :] = (A['R'][0] < r_cut).any(-1)
    for d in range(2, Nu + Nv + 1):
        n1 = np.arange(max(1, d - Nv), min(Nu, d - 1) + 1)
        m1 = d - n1
        S = (n1 - 1, m1 - 1); Ec = (n1 - 1, m1); Wc = (n1, m1 - 1); Nc = (n1, m1)
        ok = ~(mask[S] | mask[Ec] | mask[Wc])
        mask[Nc[0][~ok], Nc[1][~ok]] = True
        if not ok.any():
            continue
        n1, m1 = n1[ok], m1[ok]
        S = (n1 - 1, m1 - 1); Ec = (n1 - 1, m1); Wc = (n1, m1 - 1); Nc = (n1, m1)
        s_, e_, w_ = ({f: A[f][S] for f in d5.ALL}, {f: A[f][Ec] for f in d5.ALL}, {f: A[f][Wc] for f in d5.ALL})
        du = G.du[n1 - 1][:, None]
        nn = {f: e_[f] + w_[f] - s_[f] for f in d5.ALL}
        for _ in range(iters):
            nn = d5.s_step(E, G, w_, nn, iters=2)
            c = {f: 0.25 * (s_[f] + e_[f] + w_[f] + nn[f]) for f in d5.ALL}
            fu = {f: (w_[f] - s_[f] + nn[f] - e_[f]) / (2 * du) for f in d5.FIELDS}
            fv = {f: (e_[f] - s_[f] + nn[f] - w_[f]) / (2 * G.dv) for f in d5.FIELDS}
            env = d5.env_from(G, c, fu, fv, c['sv'])
            fuv = E.uv(env)
            if source is not None:
                fuv = fuv + source(n1, m1, G)
            for k, f in enumerate(d5.FIELDS):
                nn[f] = e_[f] + w_[f] - s_[f] + du * G.dv * fuv[..., k]
        for f in d5.ALL:
            A[f][Nc] = nn[f]
        bad = ~np.isfinite(nn['R']).all(-1) | (nn['R'] < r_cut).any(-1)
        mask[Nc[0][bad], Nc[1][bad]] = True
    return A, mask


def bump(t):
    return np.where((t > 0) & (t < 1), np.sin(np.pi * np.clip(t, 0, 1)) ** 2, 0.0)


def make_source(k, direction):
    """eps phi(u, v) T_k(x) along 'W' (the W_uv row) or 'wave' (a right eigenvector of the eigenvalue -1 of A)"""
    def src(n1, m1, G):
        uc = 0.5 * (G.u[n1] + G.u[n1 - 1]); vc = G.v[m1] - 0.5 * G.dv
        phi = bump((uc + 6) / 3) * bump((vc - 0.2) / 0.3)
        Tk = np.cos(k * np.arccos(G.x))
        out = np.zeros((len(n1), G.M, 4))
        if direction == 'W':
            out[..., 3] = EPS * phi[:, None] * Tk[None, :]
        else:
            r, _ = d5.tangherlini(uc, vc)
            for q in range(len(n1)):
                if phi[q] == 0:
                    continue
                for j, xx in enumerate(G.x):
                    out[q, j] = EPS * phi[q] * Tk[j] * wave_vector(r[q], xx)
        return out
    return src


def wave_vector(R, x):
    """a unit right eigenvector of A (symbol5.py Y1) for the eigenvalue -1, at m = n = 0, with the largest m entry"""
    A = np.array([[-4 / 3, -2 * R * (x + 1) / 9, 2 * R * (x - 1) / 9, -2 * R / 3],
                  [1 / (R * (x + 1)), -1 / 3, 2 * (1 - x) / (3 * (x + 1)), 2 / (x + 1)],
                  [-1 / (R * (x - 1)), 2 * (-x - 1) / (3 * (x - 1)), -1 / 3, -2 / (x - 1)],
                  [2 / R, x / 3 + 1 / 3, 1 / 3 - x / 3, 0.0]])
    _, sv, Vt = np.linalg.svd(A + np.eye(4))
    ns = Vt[-2:]                                   # the two right null vectors of A + I
    v = ns[np.argmax(np.abs(ns[:, 1]))]
    l0 = np.array([2 / R, (1 + x) / 3, (1 - x) / 3, 1.0])
    assert sv[-2] < 1e-10 * sv[0] and abs(l0 @ v) < 1e-10 * np.abs(l0).max()
    return v / np.abs(v).max()


def response(A0, m0, A1, m1, G, fields):
    U, V = np.meshgrid(G.u, G.v, indexing='ij')
    sel = (~m0) & (~m1) & (U <= -1.5) & (V >= 0.6) & (V <= 1.5)
    return max(float(np.nanmax(np.abs(A1[f][sel] - A0[f][sel]))) / EPS for f in fields)


def main():
    t0 = time.time()
    E = d5.Eqs()
    nv = int(round(90 * 1.5 / 4.5))
    G = d5.Grid(16, -10.0, -0.54, 200, 0.0, 4.5 * nv / 90, nv, a=0.002)
    data = d5.Data(1.0, 0.0)
    fields = ('R', 'm', 'n', 'W')
    Af, mf = free_run(E, G, data, 0.54)
    Ac, mc = cp.run(E, G, data, 0.54)
    res = {'free W': [], 'cp W': [], 'free wave': []}
    for k in KS:
        A1, m1 = free_run(E, G, data, 0.54, source=make_source(k, 'W'))
        res['free W'].append(response(Af, mf, A1, m1, G, fields))
        A1, m1 = cp.run(E, G, data, 0.54, source=make_source(k, 'W'))
        res['cp W'].append(response(Ac, mc, A1, m1, G, fields))
        A1, m1 = free_run(E, G, data, 0.54, source=make_source(k, 'wave'))
        res['free wave'].append(response(Af, mf, A1, m1, G, fields))
        print('  k = %d: response (max |delta f|/eps): free, W source %.3e; constraint-preserving, W source %.3e;'
              ' free, wave-vector source %.3e' % (k, res['free W'][-1], res['cp W'][-1], res['free wave'][-1]),
              flush=True)
    i2, i8 = KS.index(2), KS.index(8)
    g1 = res['free W'][i8] / res['free W'][i2]
    g2 = res['cp W'][i8] / res['cp W'][i2]
    gc = res['free wave'][i8] / res['free wave'][i2]
    ok1, ok2, ctl = g1 >= 8, g2 <= 2, gc <= 2
    print('J1 free scheme, W source: response(k = 8)/response(k = 2) = %.2f (Y3: 16) -> %s' % (
        g1, 'PASS' if ok1 else 'FAIL'))
    print('   control, wave-vector source: ratio %.2f -> %s' % (gc, 'fails (good)' if ctl else 'passed (bad)'))
    print('J2 constraint-preserving scheme, W source: ratio %.2f -> %s' % (g2, 'PASS' if ok2 else 'FAIL'))
    ok = ok1 and ok2 and ctl
    print('jordan5: %s (%.0f s)' % ('all checks pass' if ok else 'FAILURES', time.time() - t0))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
