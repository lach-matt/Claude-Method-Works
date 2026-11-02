#!/usr/bin/env python3
"""cpsolve5.py -- CERTIFY-10L5-RESULT.md round 2: the constraint-preserving double-null scheme, for the late region.
Labels: computed (floating point); the principal-symbol facts it rests on are exact in symbol5.py.

dnsolve5.py evolves (R, m, n, W) by the four uv-equations Ric_11, Ric_22, Ric_xx and Ric(Y, d_v) and never imposes the
Raychaudhuri constraint Ric_vv.  symbol5.py Y1 shows that this system's principal symbol has a 2 x 2 Jordan block at
the eigenvalue 0 (the sector of zeta = W + 2 log R + P + Q and its partner), so it is only weakly hyperbolic.  This
scheme drops Ric_xx and imposes Ric_vv instead:
  - R and R_v are marched along every outgoing generator (fixed u, x) by the Raychaudhuri equation
        R_vv = 2 W_v R_v - (R/3) (P_v^2 + Q_v^2 + (P_v + Q_v)^2)        (sectexp5.py X1; Ric_vv = 0 exactly),
    by the implicit midpoint rule between the cells (u_i, v_{j-1}) and (u_i, v_j), the coefficients W_v, P_v, Q_v
    taken as the centred differences across that step (second order);
  - m, n, W by Ric_11, Ric_22 and Ric(Y, d_v) in the diamond scheme of dnsolve5, with R_uv taken from the marched R
    by the diamond's own difference (R_N - R_E - R_W + R_S)/(du dv); symbol5.py Y2: their principal part is then
    lambda I, three uncoupled wave operators (lambda = e^{2W}/Gx);
  - s and s_v as in dnsolve5 (Ric_vx along each outgoing cone);
  - Ric_xx, no longer imposed, is monitored: at each new cell the residual of its row with the scheme's own
    (R, m, n, W)_uv, stored as the field 'cx' (Ric_xx in coordinates).
Data, grid, cut and mask are dnsolve5's (u := -r on v = 0 with R_v = (1 - 1/R^2)/2 there; the record's wave on
u = -R0 with R from Raychaudhuri, as in dnsolve5).  The k nodes next to each axis are solved in long double when the
option ld k is given, as in dnsolve5 (D354).

  P1 (computed) Tangherlini reproduced on dnsolve5's stretched grid at second order (error ratio of R in [3, 6] at
     r > 1.5 between 200 x 90 and 400 x 180), and the monitored Ric_xx falling at least threefold between them.
  P2 (computed) on the record's data (seed 1, M = 8, v <= 1.5) the scheme and dnsolve5 converge to one solution: their
     difference in (R, m, n, W) falls at least threefold from 100 x 45 to 200 x 90 (two schemes, one limit).
  Control (P1): the Raychaudhuri march with 2 W_v replaced by W_v; the Tangherlini error must not fall with
     resolution (ratio below 2): the march imposes the constraint, not any second-order ODE.

  python3 checks/cpsolve5.py                       selftest (P1, P2, control)
  python3 checks/cpsolve5.py --run lam rcut M Nu Nv vend out.npz [ld k] [amp A] [R0 r] [pert f k eps]
        a run stopped at v = vend, on dnsolve5's grid for v up to 4.5 (as checks/szrun5.py); with pert, the field f
        (W or m) on the data cone u = -R0 gets eps T_k(x) env(v) added (symbol5.py's witness, jordan5.py)
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
FIELDS = d5.FIELDS
ALL = ('R', 'm', 'n', 'W', 's', 'sv', 'Rv', 'cx')
ROWS = [0, 1, 3]                 # Ric_11, Ric_22, Ric(Y, d_v); Ric_xx (row 2) is monitored


def _ld_eval(E, env, idx):
    """rhs (4) and matrix (4 x 4) at the x-nodes idx in long double (dnsolve5.uv_ld's evaluation)"""
    if E._fld is None:
        E.uv_ld(env, idx)                         # builds E._fld
    sub = {k: np.asarray(env[k], np.longdouble)[..., idx] for k in E.names}
    shape = np.broadcast_shapes(*[np.shape(q) for q in sub.values()])
    vals = [np.broadcast_to(np.asarray(v_, np.longdouble), shape) for v_ in E._fld(*[sub[k] for k in E.names])]
    return np.stack(vals[:4], -1), np.stack(vals[4:], -1).reshape(shape + (4, 4))


def _gauss(A, b):
    """batched Gaussian elimination with partial pivoting (works in long double, which LAPACK does not)"""
    A = A.copy(); b = b.copy(); n = b.shape[-1]
    r = np.arange(len(b))
    for k in range(n):
        p = k + np.argmax(np.abs(A[:, k:, k]), axis=1)
        A[r, k], A[r, p] = A[r, p].copy(), A[r, k].copy(); b[r, k], b[r, p] = b[r, p].copy(), b[r, k].copy()
        for i in range(k + 1, n):
            f = A[:, i, k] / A[:, k, k]; A[:, i, k:] -= f[:, None] * A[:, k, k:]; b[:, i] -= f * b[:, k]
    y = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        y[:, i] = (b[:, i] - (A[:, i, i + 1:] * y[:, i + 1:]).sum(-1)) / A[:, i, i]
    return y


def solve_mnw(E, env, Ruv, G):
    """(m, n, W)_uv from rows ROWS with R_uv given; and the monitored Ric_xx row residual"""
    shape = np.shape(env['R'])
    vals = [np.broadcast_to(np.asarray(v_, dtype=float), shape) for v_ in E.fm(*[env[k] for k in E.names])]
    rhs = np.stack(vals[:4], -1); Mx = np.stack(vals[4:], -1).reshape(shape + (4, 4))
    b = rhs[..., ROWS] - Mx[..., ROWS, 0] * Ruv[..., None]
    A3 = Mx[..., ROWS, :][..., 1:]
    with np.errstate(all='ignore'):
        try:
            sol = np.linalg.solve(A3, b[..., None])[..., 0]
        except np.linalg.LinAlgError:
            sol = np.full(shape + (3,), np.nan)
            for q in np.ndindex(shape):
                try:
                    sol[q] = np.linalg.solve(A3[q], b[q])
                except np.linalg.LinAlgError:
                    pass
    if G.ld is not None:
        rl, Ml = _ld_eval(E, env, G.ld)
        Rl = np.asarray(Ruv, np.longdouble)[..., G.ld]
        bl = (rl[..., ROWS] - Ml[..., ROWS, 0] * Rl[..., None]).reshape(-1, 3)
        Al = Ml[..., ROWS, :][..., 1:].reshape(-1, 3, 3)
        sol[..., G.ld, :] = _gauss(Al, bl).astype(float).reshape(sol[..., G.ld, :].shape)
    full = np.concatenate([Ruv[..., None], sol], -1)
    cx = (Mx[..., 2, :] * full).sum(-1) - rhs[..., 2]
    return sol, cx


def ray_step(Rw, Rvw, Ww, Wn, Pw, Pn, Qw, Qn, dv, wcoef=2.0):
    """implicit midpoint step of R_vv = wcoef W_v R_v - (R/3) sh along v, solved exactly for (R_n, Rv_n)"""
    Wv = (Wn - Ww) / dv; Pv = (Pn - Pw) / dv; Qv = (Qn - Qw) / dv
    sh = Pv ** 2 + Qv ** 2 + (Pv + Qv) ** 2
    c = 0.5 * wcoef * Wv * dv
    # Rv_n (1 - c) + dv sh/6 R_n = Rv_w (1 + c) - dv sh/6 R_w ;  R_n - dv/2 Rv_n = R_w + dv/2 Rv_w
    a11, a12, b1 = dv * sh / 6, 1 - c, Rvw * (1 + c) - dv * sh / 6 * Rw
    a21, a22, b2 = 1.0, -dv / 2, Rw + dv / 2 * Rvw
    det = a11 * a22 - a12 * a21
    Rn = (b1 * a22 - a12 * b2) / det
    Rvn = (a11 * b2 - a21 * b1) / det
    return Rn, Rvn


def PQ(G, m, n):
    return (2 * (1 + G.x) * m - (1 - G.x) * n) / 3, (2 * (1 - G.x) * n - (1 + G.x) * m) / 3


def data_cone(E, G, data, A, pert=None):
    """the two data cones, as in dnsolve5.run, with R_v stored; pert = (field, k, eps) adds eps T_k(x) env(v) to W or m
    on u = -R0 before R is solved from Raychaudhuri there"""
    Nv, M = G.Nv, G.M
    A['R'][:, 0, :] = -G.u[:, None]; A['W'][:, 0, :] = -0.5 * np.log(2)
    A['Rv'][:, 0, :] = (1 - 1 / G.u[:, None] ** 2) / 2
    for f in ('m', 'n', 's', 'sv', 'cx'):
        A[f][:, 0, :] = 0.0
    rT, WT = d5.tangherlini(G.u[0], G.v, G.v[0])
    Fd, Gd = data.FG(G.v[:, None], G.x[None, :])
    y3 = rT[:, None] ** -1.5
    A['m'][0] = y3 * Gd / 2; A['n'][0] = y3 * Fd / 2; A['W'][0] = WT[:, None]
    if pert is not None:
        f, k, eps = pert
        Tk = np.cos(k * np.arccos(G.x))
        A[f][0] = A[f][0] + eps * data.env(G.v)[:, None] * Tk[None, :]
    m0, n0 = A['m'][0], A['n'][0]
    P, Q = PQ(G, m0, n0)
    Pv = np.gradient(P, G.dv, axis=0, edge_order=2); Qv = np.gradient(Q, G.dv, axis=0, edge_order=2)
    Wv = np.gradient(A['W'][0], G.dv, axis=0, edge_order=2)
    shear = Pv ** 2 + Qv ** 2 + (Pv + Qv) ** 2
    R = np.empty((Nv + 1, M)); Rv = np.empty((Nv + 1, M))
    R[0] = -G.u[0]; Rv[0] = (1 - 1 / R[0] ** 2) / 2
    for j in range(Nv):            # RK2 (Heun), as dnsolve5
        def acc(Rj, Rvj, k):
            return 2 * Wv[k] * Rvj - Rj / 3 * shear[k]
        a1 = acc(R[j], Rv[j], j)
        Rp = R[j] + G.dv * Rv[j]; Rvp = Rv[j] + G.dv * a1
        a2 = acc(Rp, Rvp, j + 1)
        R[j + 1] = R[j] + 0.5 * G.dv * (Rv[j] + Rvp); Rv[j + 1] = Rv[j] + 0.5 * G.dv * (a1 + a2)
    A['R'][0] = R; A['Rv'][0] = Rv; A['cx'][0] = 0.0
    A['s'][0, 0] = 0.0; A['sv'][0, 0] = 0.0
    for j in range(Nv):
        a = {f: A[f][0, j] for f in A}; b = {f: A[f][0, j + 1] for f in A}
        b = d5.s_step(E, G, a, b)
        A['s'][0, j + 1] = b['s']; A['sv'][0, j + 1] = b['sv']


def run(E, G, data, r_cut, iters=3, wcoef=2.0, pert=None, source=None):
    Nu, Nv, M = G.Nu, G.Nv, G.M
    A = {f: np.full((Nu + 1, Nv + 1, M), np.nan) for f in ALL}
    data_cone(E, G, data, A, pert)
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
        s_, e_, w_ = ({f: A[f][S] for f in ALL}, {f: A[f][Ec] for f in ALL}, {f: A[f][Wc] for f in ALL})
        du = G.du[n1 - 1][:, None]
        nn = {f: e_[f] + w_[f] - s_[f] for f in ALL}
        Pw, Qw = PQ(G, w_['m'], w_['n'])
        for _ in range(iters):
            nn = d5.s_step(E, G, w_, nn, iters=2)
            Pn, Qn = PQ(G, nn['m'], nn['n'])
            nn['R'], nn['Rv'] = ray_step(w_['R'], w_['Rv'], w_['W'], nn['W'], Pw, Pn, Qw, Qn, G.dv, wcoef)
            c = {f: 0.25 * (s_[f] + e_[f] + w_[f] + nn[f]) for f in ALL}
            fu = {f: (w_[f] - s_[f] + nn[f] - e_[f]) / (2 * du) for f in FIELDS}
            fv = {f: (e_[f] - s_[f] + nn[f] - w_[f]) / (2 * G.dv) for f in FIELDS}
            env = d5.env_from(G, c, fu, fv, c['sv'])
            Ruv = (nn['R'] - e_['R'] - w_['R'] + s_['R']) / (du * G.dv)
            sol, cx = solve_mnw(E, env, Ruv, G)
            if source is not None:            # an added source in the (m, n, W)_uv rows (jordan5.py's witness)
                sol = sol + source(n1, m1, G)[..., 1:]
            for k, f in enumerate(('m', 'n', 'W')):
                nn[f] = e_[f] + w_[f] - s_[f] + du * G.dv * sol[..., k]
            nn['cx'] = cx
        for f in ALL:
            A[f][Nc] = nn[f]
        bad = ~np.isfinite(nn['R']).all(-1) | (nn['R'] < r_cut).any(-1)
        mask[Nc[0][bad], Nc[1][bad]] = True
    return A, mask


def tangherlini_error(E, Nu, Nv, wcoef=2.0):
    G = d5.Grid(8, -10.0, -0.54, Nu, 0.0, 4.5, Nv, a=0.002)
    A, mask = run(E, G, d5.Data(1.0, 0.0), 0.54, wcoef=wcoef)
    U2, V2 = np.meshgrid(G.u, G.v, indexing='ij')
    rT, _ = d5.tangherlini(U2, V2)
    return G, A, mask, A['R'][..., 0] - rT, rT


def selftest():
    ok = True
    E = d5.Eqs()
    res = {Nu: tangherlini_error(E, Nu, Nv) for Nu, Nv in ((200, 90), (400, 180))}
    _, Ac, mc, ec, rc = res[200]
    _, Af, mf, ef, rf = res[400]
    sel = (~mc) & (rc > 1.5)
    ratio = np.nanmax(np.abs(ec[sel])) / np.nanmax(np.abs(ef[::2, ::2][sel]))
    cxc = np.nanmax(np.abs(Ac['cx'][sel])); cxf = np.nanmax(np.abs(Af['cx'][::2, ::2][sel]))
    r1 = 3 <= ratio <= 6 and cxc / cxf >= 3
    print('P1 Tangherlini: error ratio %.2f at r > 1.5 (second order: 4); Ric_xx monitor %.1e -> %.1e (ratio %.2f) ->'
          % (ratio, cxc, cxf, cxc / cxf), 'PASS' if r1 else 'FAIL', flush=True)
    ok &= r1
    ctl = {Nu: tangherlini_error(E, Nu, Nv, wcoef=1.0) for Nu, Nv in ((200, 90), (400, 180))}
    a_, b_ = ctl[200], ctl[400]
    sel = (~a_[2]) & (a_[4] > 1.5)
    ratio3 = np.nanmax(np.abs(a_[3][sel])) / np.nanmax(np.abs(b_[3][::2, ::2][sel]))
    r3 = ratio3 < 2
    print('   control (W_v in place of 2 W_v in the march): error ratio %.2f, errors %.1e, %.1e ->' % (
        ratio3, np.nanmax(np.abs(a_[3][sel])), np.nanmax(np.abs(b_[3][::2, ::2][sel]))),
        'fails (good)' if r3 else 'passed (bad)', flush=True)
    ok &= r3
    diffs = []
    for Nu, Nv in ((100, 45), (200, 90)):
        nv = int(round(Nv * 1.5 / 4.5))
        G = d5.Grid(8, -10.0, -0.3, Nu, 0.0, 4.5 * nv / Nv, nv, a=0.002)
        Acp, mcp = run(E, G, d5.Data(1.0, 1.0), 0.3)
        Ad, md = d5.run(E, G, d5.Data(1.0, 1.0), 0.3)
        diffs.append({f: (Acp[f] - Ad[f]) for f in ('R', 'm', 'n', 'W')})
        keep = (~mcp) & (~md) if Nu == 100 else keep
    dc = max(np.nanmax(np.abs(diffs[0][f][keep])) for f in diffs[0])
    df = max(np.nanmax(np.abs(diffs[1][f][::2, ::2][keep])) for f in diffs[1])
    r2 = dc / df >= 3
    print('P2 record\'s data, v <= 1.5: |cpsolve5 - dnsolve5| %.2e (100 x 45) -> %.2e (200 x 90), ratio %.2f ->'
          % (dc, df, dc / df), 'PASS' if r2 else 'FAIL', flush=True)
    ok &= r2
    print('cpsolve5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--run':
        a = sys.argv[2:]
        lam, rcut, M, Nu, Nv, vend, out = float(a[0]), float(a[1]), int(a[2]), int(a[3]), int(a[4]), float(a[5]), a[6]
        opts = a[7:]
        ld = int(opts[opts.index('ld') + 1]) if 'ld' in opts else 0
        amp = float(opts[opts.index('amp') + 1]) if 'amp' in opts else 1.0
        R0 = float(opts[opts.index('R0') + 1]) if 'R0' in opts else 10.0
        pert = None
        if 'pert' in opts:
            i = opts.index('pert'); pert = (opts[i + 1], int(opts[i + 2]), float(opts[i + 3]))
        nv = int(round(Nv * vend / 4.5)); vend = 4.5 * nv / Nv
        E = d5.Eqs()
        G = d5.Grid(M, -R0, -rcut, Nu, 0.0, vend, nv, a=0.002, ld=ld)
        t0 = time.time()
        A, mask = run(E, G, d5.Data(lam, amp), rcut, pert=pert)
        np.savez_compressed(out, mask=mask, u=G.u, v=G.v, x=G.x, xmap=0.0, lam=lam, rcut=rcut, amp=amp, R0=R0,
                            gauge='cp', **{f: A[f] for f in ALL})
        print('written', out, 'cells', int((~mask).sum()), 'of', mask.size, '%.0f s' % (time.time() - t0), flush=True)
        return 0
    return selftest()


if __name__ == '__main__':
    sys.exit(main())
