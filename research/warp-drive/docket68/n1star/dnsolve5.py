#!/usr/bin/env python3
"""dnsolve5.py -- F2 of CERTIFY-10L5.md: a prototype double-null solver for the class at 10 l5.  Labels: computed.

The class in double-null gauge (dnull5.py), with the record's regular combinations built in (hf_mirror5.py's F, G):
    g5 = -4 e^{2W} du dv + R^2 [ e^{-2(P+Q)} (dx - (1-x^2) s du)^2 / (4(1-x^2)) + (1+x)/2 e^{2P} dphi1^2
         + (1-x)/2 e^{2Q} dphi2^2 ],   x = cos 2 th,   P = (2(1+x) m - (1-x) n)/3,   Q = (2(1-x) n - (1+x) m)/3,
so 2P + Q = (1+x) m and P + 2Q = (1-x) n: the axis conditions hold identically for smooth m, n.  Unknowns R, m, n, W,
s of (u, v, x).  Equations, from the exact Ricci tensor (dnull5.ricci): Ric_11, Ric_22, Ric_xx give (R, m, n)_uv;
Ric(Y, d_v) = Ric_uv + (1-x^2) s Ric_vx gives W_uv (its second v-derivatives cancel); Ric_vx transports s along each
outgoing cone.  Scheme: second-order diamond in (u, v), vectorised over anti-diagonals; Chebyshev-Gauss collocation in x.
Data: on v = 0, Tangherlini (mu = 1) with u := -r; on u = -R0, the record's wave m = y^3 G/2, n = y^3 F/2 (y = r^-1/2
along the Tangherlini cone), W Tangherlini, R from Raychaudhuri.  The u-grid is logarithmic in |1 + u|
(u = -1 + a sinh xi): a uniform grid squeezes the late interior into an exponentially thin u-interval.  The Kretschmann
scalar is assembled from exact Christoffels and their exact derivatives in the fields, so the singular axis terms are
never differentiated numerically.

  S1 (computed) Tangherlini reproduced on the stretched grid at second order (error ratio in [3, 6] at r > 1.5).
  S2 (computed) Kretschmann: flat space gives 0 (below 1e-12); Tangherlini gives 72/r^8 (median relative error < 1e-2).
  S3 (computed, control) W on u = -R0 shifted by 0.01 v (a lapse off the Tangherlini normalisation along that cone):
     the error against Tangherlini's R(u, v) does not fall with resolution.  (A constant shift of W along the cone,
     corner included, cancels exactly in the diamond update, so it is no control.)

  --run lam rcut M Nu Nv out.npz [p]   the record's data at wavelength lam (A = 1, envelope [1/2, 7/2], R0 = 10, v to
                                   4.5, a = 0.002), cut at R < rcut; the solution and the cut mask are written to
                                   out.npz.  With p, an exponential filter of order p on the Chebyshev coefficients in x
                                   is applied to every new diamond (the axis filter); p = 0 for none.  With a
                                   further argument reg, the axis regularisation: near x = -1 the equations fix only
                                   (1 + x) m_uv and near x = +1 only (1 - x) n_uv (m drops out of the metric at x = -1,
                                   n at x = +1), so m_uv, n_uv are recovered by exact division in Chebyshev space
                                   (D352).  Without it the 4 x 4 solve divides rounding by about 1 - |x|.
"""
import sys, importlib.util, numpy as np, sympy as sp, warnings
warnings.filterwarnings('ignore')
_spec = importlib.util.spec_from_file_location('dnull5', __file__.replace('dnsolve5.py', 'dnull5.py'))
dn = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(dn)

FIELDS = ('R', 'm', 'n', 'W')
names = ('R', 'm', 'n', 'W', 's')
u, v, x, p1, p2 = sp.symbols('u v x phi1 phi2', real=True)
C = [u, v, x, p1, p2]
F = {k: sp.Function(k)(u, v, x) for k in names}
_R, _m, _n, _W, _s = [F[k] for k in names]
P = (2*(1+x)*_m - (1-x)*_n)/3; Q = (2*(1-x)*_n - (1+x)*_m)/3
Gx = _R**2*sp.exp(-2*(P+Q))/(4*(1-x**2)); beta = (1-x**2)*_s
g = sp.zeros(5)
g[0, 1] = g[1, 0] = -2*sp.exp(2*_W); g[2, 2] = Gx; g[0, 2] = g[2, 0] = -Gx*beta; g[0, 0] = Gx*beta**2
g[3, 3] = _R**2*(1+x)/2*sp.exp(2*P); g[4, 4] = _R**2*(1-x)/2*sp.exp(2*Q)


def tosym(e):
    e = e.doit()
    sub = {}
    for d in e.atoms(sp.Derivative):
        k = str(d.expr.func)
        combo = ''.join(sorted([str(vv) for vv, c in d.variable_count for _ in range(c)], key='uvx'.index))
        sub[d] = sp.Symbol(k + '_' + combo)
    return e.xreplace(sub).xreplace({f: sp.Symbol(k) for k, f in F.items()})


class Eqs:
    """the evolution equations, from the exact Ricci tensor of the ansatz"""
    def __init__(self):
        Ric = dn.ricci(g, C)
        E = {lab: tosym(Ric[i, j]) for (i, j), lab in (((3, 3), 'E11'), ((4, 4), 'E22'), ((2, 2), 'Exx'),
                                                         ((0, 1), 'Euv'), ((1, 2), 'Evx'))}
        E['EYv'] = sp.expand(E['Euv'] + (1 - x**2)*sp.Symbol('s')*E['Evx'])
        tgt = [sp.Symbol(f + '_uv') for f in FIELDS]
        svv = sp.Symbol('s_vv')
        e = sp.expand(E['Evx']); cs = e.coeff(svv); rest = sp.expand(e - cs*svv)
        assert not any('_u' in str(a) for a in rest.free_symbols)
        self.svv_expr = -rest/cs
        Mm, rhs = [], []
        for lab in ('E11', 'E22', 'Exx', 'EYv'):
            e = sp.expand(E[lab])
            if lab == 'EYv':
                e = e.subs(svv, 0)
            row = [e.coeff(t) for t in tgt]
            Mm.append(row); rhs.append(-sp.expand(e - sum(c*t for c, t in zip(row, tgt))))
        fs = set()
        for ex in rhs + sum(Mm, []):
            fs |= ex.free_symbols
        self.args = sorted(fs, key=str); self.names = [str(a) for a in self.args]
        assert not any(k.endswith('_uu') or k.endswith('_uv') for k in self.names)
        self.sargs = sorted(self.svv_expr.free_symbols, key=str); self.snames = [str(a) for a in self.sargs]
        self.fs = sp.lambdify(self.sargs, self.svv_expr, 'numpy', cse=True)
        self.fm = sp.lambdify(self.args, rhs + sum(Mm, []), 'numpy', cse=True)

    def svv(self, env):
        r = self.fs(*[env[k] for k in self.snames])
        return np.broadcast_to(np.asarray(r, dtype=float), np.shape(env['R']))

    def uv(self, env):
        shape = np.shape(env['R'])
        vals = [np.broadcast_to(np.asarray(v_, dtype=float), shape) for v_ in self.fm(*[env[k] for k in self.names])]
        rhs = np.stack(vals[:4], -1)
        M = np.stack(vals[4:], -1).reshape(shape + (4, 4))
        return np.linalg.solve(M, rhs[..., None])[..., 0]


def cheb_gauss(M):
    j = np.arange(M)
    x = np.cos((j + 0.5) * np.pi / M)
    # values -> Chebyshev coefficients (DCT-II), derivative of the series, back to values
    T = np.cos(np.outer(np.arange(M), np.arccos(x)))          # T[k, j] = T_k(x_j)
    Tinv = np.linalg.inv(T.T)                                 # coeffs = Tinv @ values
    Dc = np.zeros((M, M))                                     # derivative in coefficient space
    for k in range(M):
        for l in range(k - 1, -1, -2):
            Dc[l, k] = 2 * k
        if k % 2 == 1:
            Dc[0, k] = k
    D1 = T.T @ Dc @ Tinv
    return x, D1, D1 @ D1


def axis_quotients(M):
    """values -> values maps Q_-, Q_+: a polynomial f of degree < M to (f - f(-1))/(1 + x), resp. (f - f(1))/(1 - x),
    by division in Chebyshev space (1 + x = T_0 + T_1, 1 - x = T_0 - T_1)"""
    from numpy.polynomial import chebyshev as Ch
    x = np.cos((np.arange(M) + 0.5) * np.pi / M)
    T = np.cos(np.outer(np.arange(M), np.arccos(x)))
    Tinv = np.linalg.inv(T.T)
    Qm, Qp = np.zeros((M, M)), np.zeros((M, M))
    for k in range(M):
        c = Tinv @ np.eye(M)[k]
        qm, _ = Ch.chebdiv(c, [1.0, 1.0]); qp, _ = Ch.chebdiv(c, [1.0, -1.0])
        Qm[:, k] = Ch.chebval(x, qm); Qp[:, k] = Ch.chebval(x, qp)
    return Qm, Qp


def cheb_filter(M, p):
    """exponential filter exp(-36 (k/(M-1))^p) on the Chebyshev coefficients, as a map of values to values"""
    x = np.cos((np.arange(M) + 0.5) * np.pi / M)
    T = np.cos(np.outer(np.arange(M), np.arccos(x)))
    sig = np.exp(-36.0 * (np.arange(M) / (M - 1))**p)
    return T.T @ np.diag(sig) @ np.linalg.inv(T.T)



# ---------------------------------------------------------------- Tangherlini, mu = 1, in (U, v) with U = -r on v = v0
def rstar(r):
    return r + 0.5 * np.log(np.abs((r - 1) / (r + 1)))


def tangherlini(U, v, v0=0.0):
    U, v = np.broadcast_arrays(np.asarray(U, float), np.asarray(v, float))
    r0 = -U
    tgt = (v - v0) + 2 * rstar(r0)
    out = np.empty_like(r0)
    ins = r0 < 1
    lo = np.where(ins, 1e-12, r0); hi = np.where(ins, r0, r0 + (v - v0) + 1.0)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        f = 2 * rstar(mid) - tgt
        # outside: 2r* increasing in r; inside: decreasing
        go_up = np.where(ins, f > 0, f < 0)
        lo = np.where(go_up, mid, lo); hi = np.where(go_up, hi, mid)
    r = 0.5 * (lo + hi)
    F = lambda z: 1 - 1 / z**2
    W = 0.5 * np.log(F(r) / (2 * F(r0)))
    return r, W


# ---------------------------------------------------------------- the record's data on u = u0
class Data:
    def __init__(self, lam, A, v1=0.5, v2=3.5):
        self.lam, self.A, self.v1, self.v2 = lam, A, v1, v2

    def env(self, v):
        w = (v - self.v1) / (self.v2 - self.v1)
        return np.where((w > 0) & (w < 1), np.sin(np.pi * np.clip(w, 0, 1))**4, 0.0)

    def FG(self, v, x):
        h = np.sqrt(2 / (1 + x**2))
        e = self.lam * self.A * self.env(v) * h
        return e * np.sin(v / self.lam), e * np.cos(v / self.lam)


class Grid:
    def __init__(self, M, u0, u1, Nu, v0, v1, Nv, a=None, filt=None, reg=False):
        self.x, self.D1, self.D2 = cheb_gauss(M)
        self.M = M
        self.Fm = None if filt is None else cheb_filter(M, filt)      # axis filter of order filt, or none
        self.Q = axis_quotients(M) if reg else None                     # axis regularisation of m_uv, n_uv, or none
        if a is None:
            self.u = np.linspace(u0, u1, Nu + 1)
        else:                       # logarithmic in |1 + u| about the horizon generator u = -1 of the first cone
            xi = np.linspace(np.arcsinh((u0 + 1) / a), np.arcsinh((u1 + 1) / a), Nu + 1)
            self.u = -1 + a * np.sinh(xi)
        self.v = np.linspace(v0, v1, Nv + 1)
        self.du = np.diff(self.u); self.dv = self.v[1] - self.v[0]
        self.Nu, self.Nv = Nu, Nv


def dx(G, a):
    return a @ G.D1.T


def dxx(G, a):
    return a @ G.D2.T


ALL = ('R', 'm', 'n', 'W', 's', 'sv')


def env_from(G, c, fu=None, fv=None, sv=None):
    """c: dict of centre values (shape (..., M)); fu, fv: u- and v-derivatives of R, m, n, W"""
    e = {'x': G.x}
    for f in FIELDS:
        e[f] = c[f]; e[f + '_x'] = dx(G, c[f]); e[f + '_xx'] = dxx(G, c[f])
        e[f + '_v'] = fv[f]; e[f + '_vx'] = dx(G, fv[f])
        e[f + '_u'] = fu[f] if fu is not None else np.zeros_like(c[f])
    e['s'] = c['s']; e['s_x'] = dx(G, c['s']); e['s_v'] = sv; e['s_vx'] = dx(G, sv)
    return e


def s_step(E, G, a, b, iters=3):
    """transport of s along an outgoing cone from a (known) to b (other fields known; s, sv updated in place)"""
    dv = G.dv
    b['sv'] = a['sv'].copy(); b['s'] = a['s'] + dv * a['sv']
    for _ in range(iters):
        c = {f: 0.5 * (a[f] + b[f]) for f in FIELDS}
        c['s'] = 0.5 * (a['s'] + b['s'])
        fv = {f: (b[f] - a[f]) / dv for f in FIELDS}
        svm = 0.5 * (a['sv'] + b['sv'])
        svv = E.svv(env_from(G, c, None, fv, svm))
        b['sv'] = a['sv'] + dv * svv
        b['s'] = a['s'] + 0.5 * dv * (a['sv'] + b['sv'])
    return b


def run(E, G, data, r_cut, iters=3, log=None):
    Nu, Nv, M = G.Nu, G.Nv, G.M
    A = {f: np.full((Nu + 1, Nv + 1, M), np.nan) for f in ALL}
    U2, V2 = np.meshgrid(G.u, G.v, indexing='ij')
    # v = v0 cone: Tangherlini with u := -r
    A['R'][:, 0, :] = -G.u[:, None]; A['W'][:, 0, :] = -0.5 * np.log(2)
    for f in ('m', 'n', 's', 'sv'):
        A[f][:, 0, :] = 0.0
    # u = u0 cone: m, n from the record's data (y from Tangherlini r along u0); W Tangherlini; R by Raychaudhuri
    rT, WT = tangherlini(G.u[0], G.v, G.v[0])
    Fd, Gd = data.FG(G.v[:, None], G.x[None, :])
    y3 = rT[:, None]**-1.5
    A['m'][0] = y3 * Gd / 2; A['n'][0] = y3 * Fd / 2; A['W'][0] = WT[:, None]
    m0, n0 = A['m'][0], A['n'][0]
    P = (2 * (1 + G.x) * m0 - (1 - G.x) * n0) / 3; Q = (2 * (1 - G.x) * n0 - (1 + G.x) * m0) / 3
    Pv = np.gradient(P, G.dv, axis=0, edge_order=2); Qv = np.gradient(Q, G.dv, axis=0, edge_order=2)
    Wv = np.gradient(WT, G.dv, edge_order=2)[:, None] * np.ones((1, M))
    shear = Pv**2 + Qv**2 + (Pv + Qv)**2
    R = np.empty((Nv + 1, M)); Rv = np.empty((Nv + 1, M))
    R[0] = -G.u[0]; Rv[0] = (1 - 1 / R[0]**2) / 2
    for j in range(Nv):           # RK2 (Heun) on the 2nd-order ODE, coefficients interpolated linearly
        def acc(Rj, Rvj, k):
            return 2 * Wv[k] * Rvj - Rj / 3 * shear[k]
        a1 = acc(R[j], Rv[j], j)
        Rp = R[j] + G.dv * Rv[j]; Rvp = Rv[j] + G.dv * a1
        a2 = acc(Rp, Rvp, j + 1)
        R[j + 1] = R[j] + 0.5 * G.dv * (Rv[j] + Rvp); Rv[j + 1] = Rv[j] + 0.5 * G.dv * (a1 + a2)
    A['R'][0] = R
    A['s'][0, 0] = 0.0; A['sv'][0, 0] = 0.0
    for j in range(Nv):
        a = {f: A[f][0, j] for f in ALL}; b = {f: A[f][0, j + 1] for f in ALL}
        b = s_step(E, G, a, b)
        A['s'][0, j + 1] = b['s']; A['sv'][0, j + 1] = b['sv']
    mask = np.zeros((Nu + 1, Nv + 1), bool)          # True = excluded
    mask[:, 0] = A['R'][:, 0, 0] < r_cut
    mask[0, :] = (A['R'][0] < r_cut).any(-1)
    # anti-diagonals
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
        for _ in range(iters):
            nn = s_step(E, G, w_, nn, iters=2)
            c = {f: 0.25 * (s_[f] + e_[f] + w_[f] + nn[f]) for f in ALL}
            fu = {f: (w_[f] - s_[f] + nn[f] - e_[f]) / (2 * du) for f in FIELDS}
            fv = {f: (e_[f] - s_[f] + nn[f] - w_[f]) / (2 * G.dv) for f in FIELDS}
            fuv = E.uv(env_from(G, c, fu, fv, c['sv']))
            if G.Q is not None:       # only (1 + x) m_uv and (1 - x) n_uv are determined near x = -1, +1: divide exactly
                fuv[..., 1] = ((1 + G.x) * fuv[..., 1]) @ G.Q[0].T
                fuv[..., 2] = ((1 - G.x) * fuv[..., 2]) @ G.Q[1].T
            for k, f in enumerate(FIELDS):
                nn[f] = e_[f] + w_[f] - s_[f] + du * G.dv * fuv[..., k]
        if G.Fm is not None:
            nn = {f: nn[f] @ G.Fm.T for f in ALL}
        for f in ALL:
            A[f][Nc] = nn[f]
        bad = ~np.isfinite(nn['R']).all(-1) | (nn['R'] < r_cut).any(-1)
        mask[Nc[0][bad], Nc[1][bad]] = True
        if log and d % 50 == 0:
            log(d, int(ok.sum()), float(np.nanmax(np.abs(nn['m']))))
    return A, mask


def _setup_curvature():
    global keys, dkeys, fG, fdG, fg, fgi, ARGS
    gi = sp.zeros(5); gi[:3, :3] = sp.simplify(g[:3, :3].inv()); gi[3, 3] = 1/g[3, 3]; gi[4, 4] = 1/g[4, 4]
    Gam, dGam = {}, {}
    for a in range(5):
        for b in range(5):
            for c in range(b, 5):
                e = sum(gi[a, d]*(sp.diff(g[d, c], C[b]) + sp.diff(g[d, b], C[c]) - sp.diff(g[b, c], C[d]))
                        for d in range(5) if gi[a, d] != 0)/2
                if e != 0:
                    Gam[(a, b, c)] = tosym(e)
                    for k in range(3):
                        de = tosym(sp.diff(e, C[k]))
                        if de != 0:
                            dGam[(k, a, b, c)] = de
    SECOND = [k + '_' + d for k in names for d in ('uu', 'uv', 'ux', 'vv', 'vx', 'xx')]
    ARGS = ['x'] + [k for k in names] + [k + '_' + d for k in names for d in 'uvx'] + SECOND
    syms = [sp.Symbol(a) if a != 'x' else x for a in ARGS]
    keys = sorted(Gam)
    dkeys = sorted(dGam)
    fG = sp.lambdify(syms, [Gam[k] for k in keys], 'numpy', cse=True)
    fdG = sp.lambdify(syms, [dGam[k] for k in dkeys], 'numpy', cse=True)
    fg = sp.lambdify(syms, [tosym(g[i, j]) for i in range(5) for j in range(5)], 'numpy', cse=True)
    fgi = sp.lambdify(syms, [tosym(gi[i, j]) for i in range(5) for j in range(5)], 'numpy', cse=True)


def kretschmann(Z, rows=None):
    if 'fG' not in globals():
        _setup_curvature()
    uu, vv, xx = Z['u'], Z['v'], Z['x']
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    _, D1, _ = cheb_gauss(len(xx))
    Nu, Nv, M = Z['R'].shape
    out = np.full((Nu, Nv, M), np.nan)

    def fields(i):
        e = {'x': xx}
        for k in names:
            a, ap, aq = Z[k][i], Z[k][i + 1], Z[k][i - 1]
            h1, h2 = uu[i] - uu[i - 1], uu[i + 1] - uu[i]
            e[k] = a
            e[k + '_x'] = a @ D1.T
            e[k + '_xx'] = a @ D1.T @ D1.T
            e[k + '_v'] = np.gradient(a, dv, axis=0)
            e[k + '_vv'] = np.gradient(e[k + '_v'], dv, axis=0)
            e[k + '_vx'] = e[k + '_v'] @ D1.T
            e[k + '_u'] = -h2 / (h1 * (h1 + h2)) * aq + (h2 - h1) / (h1 * h2) * a + h1 / (h2 * (h1 + h2)) * ap
            e[k + '_uu'] = 2 * (aq / (h1 * (h1 + h2)) - a / (h1 * h2) + ap / (h2 * (h1 + h2)))
            e[k + '_uv'] = np.gradient(e[k + '_u'], dv, axis=0)
            e[k + '_ux'] = e[k + '_u'] @ D1.T
        return e

    def gam(i):
        e = fields(i)
        vals = fG(*[np.broadcast_to(e[a], (Nv, M)) if a != 'x' else xx for a in ARGS])
        Gm = np.zeros((Nv, M, 5, 5, 5))
        for k, val in zip(keys, vals):
            a, b, c = k
            Gm[..., a, b, c] = val; Gm[..., a, c, b] = val
        return Gm, e
    rng = rows if rows is not None else range(1, Nu - 1)
    for i in rng:
        Gm, e = gam(i)
        args = [np.broadcast_to(e[a], (Nv, M)) if a != 'x' else xx for a in ARGS]
        dG = np.zeros((Nv, M, 5, 5, 5, 5))          # dG[..., c, a, b, d] = d_c Gamma^a_bd
        for k, val in zip(dkeys, fdG(*args)):
            c, a, b, d = k
            dG[..., c, a, b, d] = val; dG[..., c, a, d, b] = val
        # Riemann R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce} G^e_{db} - G^a_{de} G^e_{cb}
        Rm = (np.einsum('...cadb->...abcd', dG) - np.einsum('...dacb->...abcd', dG)
              + np.einsum('...ace,...edb->...abcd', Gm, Gm) - np.einsum('...ade,...ecb->...abcd', Gm, Gm))
        args = [np.broadcast_to(e[a], (Nv, M)) if a != 'x' else xx for a in ARGS]
        gg = np.stack([np.broadcast_to(np.asarray(q, float), (Nv, M)) for q in fg(*args)], -1).reshape(Nv, M, 5, 5)
        gI = np.stack([np.broadcast_to(np.asarray(q, float), (Nv, M)) for q in fgi(*args)], -1).reshape(Nv, M, 5, 5)
        Rl = np.einsum('...ae,...ebcd->...abcd', gg, Rm)
        Ru = np.einsum('...abcd,...bf,...cg,...dh->...afgh', Rm, gI, gI, gI)
        out[i] = np.einsum('...abcd,...abcd->...', Rl, Ru)
    return out


def tangherlini_error(E, Nu, Nv, w_shift=0.0):
    """S1/S3: run Tangherlini data on the stretched grid; error of R against the exact solution, on the coarse points"""
    G = Grid(8, -10.0, -0.54, Nu, 0.0, 4.5, Nv, a=0.002)
    exact = globals()['tangherlini']
    if w_shift:
        globals()['tangherlini'] = lambda U, V, v0=0.0: (exact(U, V, v0)[0], exact(U, V, v0)[1] + w_shift * V)
    try:
        A, mask = run(E, G, Data(1.0, 0.0), 0.54)
    finally:
        globals()['tangherlini'] = exact
    U2, V2 = np.meshgrid(G.u, G.v, indexing='ij')
    rT, _ = exact(U2, V2)
    return G, A, mask, A['R'][..., 0] - rT, rT


def selftest():
    ok = True
    E = Eqs()
    res = {}
    for Nu, Nv in ((200, 90), (400, 180)):
        res[Nu] = tangherlini_error(E, Nu, Nv)
    _, _, mc, ec, rc = res[200]
    G, A, mf, ef, rf = res[400]
    sel = (~mc) & (rc > 1.5)
    ratio = np.nanmax(np.abs(ec[sel])) / np.nanmax(np.abs(ef[::2, ::2][sel]))
    r1 = 3 <= ratio <= 6
    print('S1 Tangherlini, stretched grid: error ratio %.2f at r > 1.5 (second order: 4) ->' % ratio,
          'PASS' if r1 else 'FAIL')
    ok &= r1
    # S2: Kretschmann
    uu = np.linspace(-6, -2, 41); vv = np.linspace(0, 3, 31); xx, _, _ = cheb_gauss(8)
    U, V = np.meshgrid(uu, vv, indexing='ij')
    Rf = ((V - U) / 2)[..., None] * np.ones(8)
    Zf = dict(u=uu, v=vv, x=xx, mask=np.zeros(U.shape, bool), R=Rf, W=np.full_like(Rf, -np.log(2)), m=0 * Rf,
              n=0 * Rf, s=0 * Rf)
    Kf = kretschmann(Zf, rows=[10, 20])
    kf = np.nanmax(np.abs(Kf[[10, 20]][:, 2:-2]))
    Zt = dict(u=G.u, v=G.v, x=G.x, mask=mf, **{k: A[k] for k in names})
    rows = range(20, 380, 40)
    Kt = kretschmann(Zt, rows=rows)
    sel = np.zeros(mf.shape, bool); sel[list(rows), 2:-2] = True
    sel &= (~mf) & np.isfinite(Kt).all(-1)
    rel = np.abs(Kt[sel] / (72 / rf[sel][:, None]**8) - 1)
    r2 = kf < 1e-12 and np.median(rel) < 1e-2
    print('S2 Kretschmann: flat %.1e; Tangherlini median relative error %.1e ->' % (kf, np.median(rel)),
          'PASS' if r2 else 'FAIL')
    ok &= r2
    # S3: control
    ctl = {Nu: tangherlini_error(E, Nu, Nv, w_shift=0.01) for Nu, Nv in ((200, 90), (400, 180))}
    a_, b_ = ctl[200], ctl[400]
    sel = (~a_[2]) & (a_[4] > 1.5)
    ratio3 = np.nanmax(np.abs(a_[3][sel])) / np.nanmax(np.abs(b_[3][::2, ::2][sel]))
    r3 = ratio3 < 2
    print('S3 control, W + 0.01 v on u = -R0: error ratio %.2f (no convergence expected) ->' % ratio3,
          'PASS' if r3 else 'FAIL')
    ok &= r3
    print('dnsolve5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--run':
        lam, rcut = float(sys.argv[2]), float(sys.argv[3])
        M, Nu, Nv = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
        filt = int(sys.argv[8]) if len(sys.argv) > 8 and sys.argv[8] != '0' else None
        reg = len(sys.argv) > 9 and sys.argv[9] == 'reg'
        E = Eqs()
        G = Grid(M, -10.0, -rcut, Nu, 0.0, 4.5, Nv, a=0.002, filt=filt, reg=reg)
        A, mask = run(E, G, Data(lam, 1.0), rcut)
        np.savez_compressed(sys.argv[7], mask=mask, u=G.u, v=G.v, x=G.x, **{f: A[f] for f in ALL})
        print('written', sys.argv[7], 'cells', int((~mask).sum()), 'of', mask.size)
        return 0
    return selftest()


if __name__ == '__main__':
    sys.exit(main())
