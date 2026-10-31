#!/usr/bin/env python3
"""dnsolve5v.py -- CERTIFY-10L5 section 6b (D386): dnsolve5.py in the swapped gauge, the shift on dv.  Labels: computed.

    g5 = -4 e^{2W} du dv + R^2 [ e^{-2(P+Q)} (dx - (1-x^2) s dv)^2 / (4(1-x^2)) + (1+x)/2 e^{2P} dphi1^2
         + (1-x)/2 e^{2Q} dphi2^2 ]                                         (dnsolve5.py's P, Q, Gx; only du -> dv)

so d_u at fixed x is null and orthogonal to d_x: x is constant along the ingoing null generators orthogonal to the
orbits, the curves that carry the record's ingoing wave, so its angular profile is not dragged toward an axis (D381:
dnsolve5's x moves by dx/du = (1 - x^2) s along them). The drag moves to the outgoing generators, dx/dv = (1 - x^2) s.
The two Ricci tensors are mirror images under u <-> v (V1, exact), so the equations are dnsolve5's mirrored: Ric_11,
Ric_22, Ric_xx and Ric(d_u, Y) = Ric_uv + (1-x^2) s Ric_ux (Y := d_v + (1-x^2) s d_x; its s_uu cancels) give
(R, m, n, W)_uv, and Ric_ux transports s along each ingoing cone v = const (an ODE in u for s, s_u).  Data:
  v = 0      Tangherlini (mu = 1, u := -r), s = s_u = 0, as in dnsolve5;
  u = -R0    the record's wave m, n, W Tangherlini, R by Raychaudhuri, as in dnsolve5; s = 0 there (the gauge: x
             constant along that cone's generators as well); and s_u, the one transverse quantity the u-transport
             needs, from Ric_vx, which on that cone is an ODE in v for s_u once the transverse derivatives
             R_u, m_u, n_u, W_u are carried along it by the uv-equations (from Tangherlini at the corner).
dnsolve5 needed s_v only on v = 0, inside Tangherlini, where it vanishes; the mirror needs s_u on the wave's cone.

  V1 (exact) the mirror: every Ricci component of this metric is dnsolve5's with u and v exchanged; EYu has no s_uu.
  V2 (computed) Tangherlini on the stretched grid at second order (error ratio in [3, 6] at r > 1.5); the spurious s
     the axis rounding of D354 leaves is below 1e-3 (5.3e-5 at 400 x 180; dnsolve5's own s there is 1.0e-4).
  V3 (computed) the transverse ODE on u = -R0 with Tangherlini data returns Tangherlini's R_u there, at second order.
  V4 (computed) the gauges agree: at lambda = 1 the section volume V(u, v) = pi^2 int R^3 dx, invariant under the
     change of angle between the two gauges, agrees with dnsolve5's on v <= 1 at both resolutions, and the agreement
     improves with resolution; the control: R at a node next to an axis, not invariant, does not agree.

  --run lam rcut M Nu Nv out.npz [p] [ld k]   as dnsolve5.py --run (A = 1, envelope [1/2, 7/2], R0 = 10, v to 4.5,
                                             a = 0.002); p the axis filter order (0 for none), ld k as there.
  --drift RUN.npz [v ...]                     ln of the factor by which this gauge's angle presses a fixed outgoing
                                             generator toward each axis: d ln(1 + x)/dv = 2 s(x = -1) and
                                             d ln(1 - x)/dv = -2 s(x = +1), integrated in v from v = 0 at fixed u.
  --compare A.npz B.npz [vmax]                the invariant V(u, v) of two runs on the same (u, v) grid (either gauge).
"""
import sys, time, importlib.util, numpy as np, sympy as sp, warnings
warnings.filterwarnings('ignore')
_spec = importlib.util.spec_from_file_location('dnsolve5', __file__.replace('dnsolve5v.py', 'dnsolve5.py'))
d5 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(d5)

dn, FIELDS, names, u, v, x, C, F, tosym = d5.dn, d5.FIELDS, d5.names, d5.u, d5.v, d5.x, d5.C, d5.F, d5.tosym
_R, _m, _n, _W, _s = [F[k] for k in names]
G0 = d5.g
gv = sp.zeros(5)
gv[0, 1] = gv[1, 0] = -2*sp.exp(2*_W); gv[2, 2] = d5.Gx
gv[1, 2] = gv[2, 1] = -d5.Gx*d5.beta; gv[1, 1] = d5.Gx*d5.beta**2
gv[3, 3] = G0[3, 3]; gv[4, 4] = G0[4, 4]
LABELS = (((3, 3), 'E11'), ((4, 4), 'E22'), ((2, 2), 'Exx'), ((0, 1), 'Euv'), ((0, 2), 'Eux'), ((1, 2), 'Evx'))


def components(g):
    Ric = dn.ricci(g, C)
    return {lab: sp.expand(tosym(Ric[i, j])) for (i, j), lab in LABELS}


def mirror(e):
    """u <-> v in a tosym'd expression"""
    sub = {}
    for a in e.free_symbols:
        s_ = str(a)
        if '_' in s_:
            k, combo = s_.split('_')
            sub[a] = sp.Symbol(k + '_' + ''.join(sorted(combo.translate(str.maketrans('uv', 'vu')), key='uvx'.index)))
    return e.xreplace(sub)


class Eqs(d5.Eqs):
    """the mirrored equations; uv() and uv_ld() are dnsolve5's, on this system"""
    def __init__(self):
        E = components(gv)
        self.E = E
        E['EYu'] = sp.expand(E['Euv'] + (1 - x**2)*sp.Symbol('s')*E['Eux'])
        suu, suv = sp.Symbol('s_uu'), sp.Symbol('s_uv')
        e = E['Eux']; cs = e.coeff(suu); rest = sp.expand(e - cs*suu)
        assert not any('v' in str(a).split('_')[1] for a in rest.free_symbols if '_' in str(a))
        self.suu_expr = -rest/cs
        self.eyu_suu = sp.simplify(E['EYu'].coeff(suu))
        tgt = [sp.Symbol(f + '_uv') for f in FIELDS]
        Mm, rhs = [], []
        for lab in ('E11', 'E22', 'Exx', 'EYu'):
            e = E[lab].subs(suu, 0) if lab == 'EYu' else E[lab]
            row = [e.coeff(t) for t in tgt]
            Mm.append(row); rhs.append(-sp.expand(e - sum(c*t for c, t in zip(row, tgt))))
        fs = set()
        for ex in rhs + sum(Mm, []):
            fs |= ex.free_symbols
        self.args = sorted(fs, key=str); self.names = [str(a) for a in self.args]
        assert not any(k.endswith('_vv') or k.endswith('_uv') or k.endswith('_uu') for k in self.names)
        e = E['Evx']; cs = e.coeff(suv); rest = sp.expand(e - cs*suv)      # s_uv on u = -R0 (with R_uv, ... known)
        self.suv_expr = -rest/cs
        self.sargs = sorted(self.suu_expr.free_symbols, key=str); self.snames = [str(a) for a in self.sargs]
        self.vargs = sorted(self.suv_expr.free_symbols, key=str); self.vnames = [str(a) for a in self.vargs]
        self.fs = sp.lambdify(self.sargs, self.suu_expr, 'numpy', cse=True)
        self.fv_ = sp.lambdify(self.vargs, self.suv_expr, 'numpy', cse=True)
        self.fm = sp.lambdify(self.args, rhs + sum(Mm, []), 'numpy', cse=True)
        self._uvexpr, self._fld = rhs + sum(Mm, []), None

    def suu(self, env):
        r = self.fs(*[env[k] for k in self.snames])
        return np.broadcast_to(np.asarray(r, dtype=float), np.shape(env['R']))

    def suv(self, env):
        r = self.fv_(*[env[k] for k in self.vnames])
        return np.broadcast_to(np.asarray(r, dtype=float), np.shape(env['R']))


ALLV = ('R', 'm', 'n', 'W', 's', 'su')
dx, dxx = d5.dx, d5.dxx


def env_v(G, c, fu, fv=None, su=None, sv=None, fuv=None):
    e = {'x': G.x}
    z = np.zeros_like(c['R'])
    for f in FIELDS:
        e[f] = c[f]; e[f + '_x'] = dx(G, c[f]); e[f + '_xx'] = dxx(G, c[f])
        e[f + '_u'] = fu[f]; e[f + '_ux'] = dx(G, fu[f])
        e[f + '_v'] = z if fv is None else fv[f]; e[f + '_vx'] = dx(G, e[f + '_v'])
        if fuv is not None:
            e[f + '_uv'] = fuv[f]
    e['s'] = c['s']; e['s_x'] = dx(G, c['s']); e['s_xx'] = dxx(G, c['s'])
    e['s_u'] = z if su is None else su; e['s_ux'] = dx(G, e['s_u'])
    e['s_v'] = z if sv is None else sv; e['s_vx'] = dx(G, e['s_v'])
    return e


def solve_uv(E, G, env):
    fuv = E.uv(env)
    if G.ld is not None:
        fuv[..., G.ld, :] = E.uv_ld(env, G.ld)
    return fuv


def s_step_u(E, G, a, b, du, iters=3):
    """transport of s along an ingoing cone from a (known) to b (other fields known; s, su updated)"""
    b['su'] = a['su'].copy(); b['s'] = a['s'] + du * a['su']
    for _ in range(iters):
        c = {f: 0.5 * (a[f] + b[f]) for f in FIELDS}
        c['s'] = 0.5 * (a['s'] + b['s'])
        fu = {f: (b[f] - a[f]) / du for f in FIELDS}
        suu = E.suu(env_v(G, c, fu, su=0.5 * (a['su'] + b['su'])))
        b['su'] = a['su'] + du * suu
        b['s'] = a['s'] + 0.5 * du * (a['su'] + b['su'])
    return b


def transverse(E, G, A, fu0):
    """on u = u0 (s = 0): the transverse derivatives f_u and s_u, carried in v by the uv-equations and Ric_vx (Heun)"""
    M = G.M
    z = np.zeros(M)
    fv = {f: np.gradient(A[f][0], G.dv, axis=0, edge_order=2) for f in FIELDS}

    def rate(j, y, su):
        c = {f: A[f][0, j] for f in FIELDS}; c['s'] = z
        env = env_v(G, c, y, {f: fv[f][j] for f in FIELDS}, su, z)
        fuv = solve_uv(E, G, env)
        fuvd = {f: fuv[..., k] for k, f in enumerate(FIELDS)}
        env = env_v(G, c, y, {f: fv[f][j] for f in FIELDS}, su, z, fuvd)
        return fuvd, E.suv(env)

    y, su = {f: fu0[f] * np.ones(M) for f in FIELDS}, z.copy()
    FU = {f: np.empty((G.Nv + 1, M)) for f in FIELDS}; SU = np.empty((G.Nv + 1, M))
    for f in FIELDS:
        FU[f][0] = y[f]
    SU[0] = su
    for j in range(G.Nv):
        k1, l1 = rate(j, y, su)
        yp = {f: y[f] + G.dv * k1[f] for f in FIELDS}; sp_ = su + G.dv * l1
        k2, l2 = rate(j + 1, yp, sp_)
        y = {f: y[f] + 0.5 * G.dv * (k1[f] + k2[f]) for f in FIELDS}; su = su + 0.5 * G.dv * (l1 + l2)
        for f in FIELDS:
            FU[f][j + 1] = y[f]
        SU[j + 1] = su
    return SU, FU


def first_cone(G, A, data):
    """u = u0: dnsolve5's data (m, n from the record, W Tangherlini, R by Raychaudhuri), lines 272-291 there"""
    M = G.M
    rT, WT = d5.tangherlini(G.u[0], G.v, G.v[0])
    Fd, Gd = data.FG(G.v[:, None], G.x[None, :])
    y3 = rT[:, None]**-1.5
    A['m'][0] = y3 * Gd / 2; A['n'][0] = y3 * Fd / 2; A['W'][0] = WT[:, None]
    m0, n0 = A['m'][0], A['n'][0]
    P = (2 * (1 + G.x) * m0 - (1 - G.x) * n0) / 3; Q = (2 * (1 - G.x) * n0 - (1 + G.x) * m0) / 3
    Pv = np.gradient(P, G.dv, axis=0, edge_order=2); Qv = np.gradient(Q, G.dv, axis=0, edge_order=2)
    Wv = np.gradient(WT, G.dv, edge_order=2)[:, None] * np.ones((1, M))
    shear = Pv**2 + Qv**2 + (Pv + Qv)**2
    R = np.empty((G.Nv + 1, M)); Rv = np.empty((G.Nv + 1, M))
    R[0] = -G.u[0]; Rv[0] = (1 - 1 / R[0]**2) / 2
    for j in range(G.Nv):
        def acc(Rj, Rvj, k):
            return 2 * Wv[k] * Rvj - Rj / 3 * shear[k]
        a1 = acc(R[j], Rv[j], j)
        Rp = R[j] + G.dv * Rv[j]; Rvp = Rv[j] + G.dv * a1
        a2 = acc(Rp, Rvp, j + 1)
        R[j + 1] = R[j] + 0.5 * G.dv * (Rv[j] + Rvp); Rv[j + 1] = Rv[j] + 0.5 * G.dv * (a1 + a2)
    A['R'][0] = R


def run(E, G, data, r_cut, iters=3, log=None):
    Nu, Nv, M = G.Nu, G.Nv, G.M
    A = {f: np.full((Nu + 1, Nv + 1, M), np.nan) for f in ALLV}
    A['R'][:, 0, :] = -G.u[:, None]; A['W'][:, 0, :] = -0.5 * np.log(2)
    for f in ('m', 'n', 's', 'su'):
        A[f][:, 0, :] = 0.0
    first_cone(G, A, data)
    A['s'][0] = 0.0
    A['su'][0], _ = transverse(E, G, A, {'R': -1.0, 'm': 0.0, 'n': 0.0, 'W': 0.0})
    for i in range(Nu):              # v = v0: s by its u-transport (Tangherlini: it stays 0; kept for the check)
        a = {f: A[f][i, 0] for f in ALLV}; b = {f: A[f][i + 1, 0].copy() for f in ALLV}
        b = s_step_u(E, G, a, b, G.du[i])
        A['s'][i + 1, 0] = b['s']; A['su'][i + 1, 0] = b['su']
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
        s_, e_, w_ = ({f: A[f][S] for f in ALLV}, {f: A[f][Ec] for f in ALLV}, {f: A[f][Wc] for f in ALLV})
        du = G.du[n1 - 1][:, None]
        nn = {f: e_[f] + w_[f] - s_[f] for f in ALLV}
        for _ in range(iters):
            nn = s_step_u(E, G, e_, nn, du, iters=2)
            c = {f: 0.25 * (s_[f] + e_[f] + w_[f] + nn[f]) for f in ALLV}
            fu = {f: (w_[f] - s_[f] + nn[f] - e_[f]) / (2 * du) for f in FIELDS}
            fv = {f: (e_[f] - s_[f] + nn[f] - w_[f]) / (2 * G.dv) for f in FIELDS}
            sv = (e_['s'] - s_['s'] + nn['s'] - w_['s']) / (2 * G.dv)
            fuv = solve_uv(E, G, env_v(G, c, fu, fv, c['su'], sv))
            for k, f in enumerate(FIELDS):
                nn[f] = e_[f] + w_[f] - s_[f] + du * G.dv * fuv[..., k]
        if G.Fm is not None:
            nn = {f: nn[f] @ G.Fm.T for f in ALLV}
        for f in ALLV:
            A[f][Nc] = nn[f]
        bad = ~np.isfinite(nn['R']).all(-1) | (nn['R'] < r_cut).any(-1)
        mask[Nc[0][bad], Nc[1][bad]] = True
        if log and d % 50 == 0:
            log(d, int(ok.sum()), float(np.nanmax(np.abs(nn['m']))))
    return A, mask


def kretschmann(Z, rows=None):
    """dnsolve5's assembly on this metric"""
    for k in ('fG', 'fdG', 'fg', 'fgi'):
        d5.__dict__.pop(k, None)
    d5.g = gv
    try:
        return d5.kretschmann(Z, rows)
    finally:
        d5.g = G0
        for k in ('fG', 'fdG', 'fg', 'fgi'):
            d5.__dict__.pop(k, None)


def volume(R, xg):
    """pi^2 int_{-1}^{1} R^3 dx by Gauss-Chebyshev quadrature on the nodes xg"""
    M = len(xg)
    return np.pi**2 * (np.pi / M) * (R**3 * np.sqrt(1 - xg**2)).sum(-1)


def drift(path, vs):
    d = np.load(path)
    uu, vv, xg, s, R = d["u"], d["v"], d["x"], d["s"], d["R"]
    im, ip = np.argmin(xg), np.argmax(xg)
    dv = vv[1] - vv[0]

    def cum(sx):
        return np.concatenate([np.zeros((sx.shape[0], 1)), np.cumsum(0.5 * (sx[:, 1:] + sx[:, :-1]) * dv, axis=1)], 1)

    cm, cp = 2 * cum(s[:, :, im]), -2 * cum(s[:, :, ip])
    print("%s: first node ln(1 - |x|) = %.2f" % (path, np.log(1 - abs(xg[ip]))))
    for v_ in vs:
        j = np.argmin(abs(vv - v_))
        out = []
        for c, k in ((cm, im), (cp, ip)):
            col = np.where(np.isfinite(c[:, j]), c[:, j], np.nan)
            if not np.isfinite(col).any():
                out.append((np.nan, np.nan, np.nan)); continue
            i = np.nanargmin(col)
            out.append((col[i], uu[i], R[i, j, k]))
        print("  v = %.2f  x = -1: %7.2f at u = %.4f (R = %.2f)   x = +1: %7.2f at u = %.4f (R = %.2f)"
              % ((vv[j],) + out[0] + out[1]))


def compare(pa, pb, vmax=None):
    a, b = np.load(pa), np.load(pb)
    va, vb = volume(a['R'], a['x']), volume(b['R'], b['x'])
    ok = ~(a['mask'] | b['mask']) & np.isfinite(va) & np.isfinite(vb)
    if vmax is not None:
        ok &= (a['v'] <= vmax)[None, :]
    rel = np.abs(va - vb)[ok] / np.abs(va)[ok]
    return float(rel.max()), float(np.median(rel)), int(ok.sum())


def tangherlini_error(E, Nu, Nv):
    G = d5.Grid(8, -10.0, -0.54, Nu, 0.0, 4.5, Nv, a=0.002)
    A, mask = run(E, G, d5.Data(1.0, 0.0), 0.54)
    U2, V2 = np.meshgrid(G.u, G.v, indexing='ij')
    rT, _ = d5.tangherlini(U2, V2)
    return G, A, mask, A['R'][..., 0] - rT, rT


def selftest():
    ok = True
    t0 = time.time()
    E = Eqs()
    E0 = components(G0)
    r1 = all(sp.expand(mirror(E.E[a]) - E0[b]) == 0 for a, b in (('E11', 'E11'), ('E22', 'E22'), ('Exx', 'Exx'),
                                                              ('Euv', 'Euv'), ('Eux', 'Evx'), ('Evx', 'Eux')))
    r1c = sp.expand(mirror(E.E["Eux"]) - E0["Eux"]) != 0                       # control: not the same component
    r1 = r1 and r1c and E.eyu_suu == 0
    print('V1 mirror u <-> v of all six components, exact; EYu free of s_uu; control Eux vs Eux differs ->',
          'PASS' if r1 else 'FAIL', '(%.0fs)' % (time.time() - t0), flush=True)
    ok &= r1
    res = {N: tangherlini_error(E, *N) for N in ((200, 90), (400, 180))}
    _, _, mc, ec, rc = res[(200, 90)]
    G, A, mf, ef, rf = res[(400, 180)]
    sel = (~mc) & (rc > 1.5)
    ratio = np.nanmax(np.abs(ec[sel])) / np.nanmax(np.abs(ef[::2, ::2][sel]))
    smax = max(np.nanmax(np.abs(res[N][1]['s'])) for N in res)
    r2 = 3 <= ratio <= 6 and smax < 1e-3          # dnsolve5's own: 1.7e-4, 1.0e-4 here (axis rounding, D354)
    print('V2 Tangherlini, stretched grid: error ratio %.2f at r > 1.5 (second order: 4); max |s| %.1e ->'
          % (ratio, smax), 'PASS' if r2 else 'FAIL', '(%.0fs)' % (time.time() - t0), flush=True)
    ok &= r2
    errs = []
    for Nv in (90, 180):
        G3 = d5.Grid(8, -10.0, -0.54, 10, 0.0, 4.5, Nv)
        A3 = {f: np.zeros((1, Nv + 1, 8)) for f in ALLV}
        first_cone(G3, A3, d5.Data(1.0, 0.0))
        _, FU = transverse(E, G3, A3, {'R': -1.0, 'm': 0.0, 'n': 0.0, 'W': 0.0})
        h = 1e-5
        rp, _ = d5.tangherlini(G3.u[0] + h, G3.v); rm, _ = d5.tangherlini(G3.u[0] - h, G3.v)
        errs.append(np.abs(FU['R'][:, 0] - (rp - rm) / (2 * h)).max())
    r3 = 3 <= errs[0] / errs[1] <= 6
    print('V3 transverse R_u on u = -R0, Tangherlini: errors %.1e, %.1e (ratio %.2f) ->' % (errs[0], errs[1],
          errs[0] / errs[1]), 'PASS' if r3 else 'FAIL', flush=True)
    ok &= r3
    E5 = d5.Eqs()
    rel, ctl = [], []
    for Nu, Nv in ((200, 90), (400, 180)):
        Gs = d5.Grid(8, -10.0, -0.54, Nu, 0.0, 4.5, Nv, a=0.002)
        Aa, ma = d5.run(E5, Gs, d5.Data(1.0, 1.0), 0.54)
        Ab, mb = run(E, Gs, d5.Data(1.0, 1.0), 0.54)
        good = ~(ma | mb) & (Gs.v <= 1.0)[None, :]
        va, vb = volume(Aa['R'], Gs.x), volume(Ab['R'], Gs.x)
        rel.append(np.nanmax(np.abs(va - vb)[good] / va[good]))
        ctl.append(np.nanmax(np.abs(Aa['R'][..., 0] - Ab['R'][..., 0])[good] / Aa['R'][..., 0][good]))
    r4 = rel[1] < rel[0] / 2 and rel[1] < 1e-3 and ctl[1] > 10 * rel[1]
    print('V4 lambda = 1, v <= 1: section volume, relative difference of the gauges %.1e, %.1e; control R at the node'
          ' next to x = +1: %.1e ->' % (rel[0], rel[1], ctl[1]), 'PASS' if r4 else 'FAIL',
          '(%.0fs)' % (time.time() - t0), flush=True)
    ok &= r4
    print('dnsolve5v:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--run':
        lam, rcut = float(sys.argv[2]), float(sys.argv[3])
        M, Nu, Nv = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
        filt = int(sys.argv[8]) if len(sys.argv) > 8 and sys.argv[8] not in ('0', 'ld') else None
        opts = sys.argv[8:]
        ld = int(opts[opts.index('ld') + 1]) if 'ld' in opts else 0
        E = Eqs()
        G = d5.Grid(M, -10.0, -rcut, Nu, 0.0, 4.5, Nv, a=0.002, filt=filt, ld=ld)
        A, mask = run(E, G, d5.Data(lam, 1.0), rcut)
        np.savez_compressed(sys.argv[7], mask=mask, u=G.u, v=G.v, x=G.x, **{f: A[f] for f in ALLV})
        print('written', sys.argv[7], 'cells', int((~mask).sum()), 'of', mask.size)
        return 0
    if len(sys.argv) > 1 and sys.argv[1] == '--drift':
        drift(sys.argv[2], [float(a) for a in sys.argv[3:]] or [1.4, 1.5, 1.6, 1.65, 1.7, 1.8, 2.0, 2.5, 3.0, 3.3])
        return 0
    if len(sys.argv) > 1 and sys.argv[1] == '--compare':
        vmax = float(sys.argv[4]) if len(sys.argv) > 4 else None
        mx, md, n = compare(sys.argv[2], sys.argv[3], vmax)
        print('section volume, relative difference: max %.2e, median %.2e over %d cells' % (mx, md, n))
        return 0
    return selftest()


if __name__ == '__main__':
    sys.exit(main())
