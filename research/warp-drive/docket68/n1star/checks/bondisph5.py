#!/usr/bin/env python3
"""bondisph5.py -- library for CERTIFY-10L5-RESULT.md section 1: the round spheres of growth5.py's Bondi chart, rebuilt
on dnsolve5.py's double-null solution, and their outgoing expansion.  Labels: computed (floating point).

growth5.py counts the zeros, along each Bondi column, of the outgoing expansion of the spheres {v, r} of its Bondi chart:
the sections of the ingoing cone C_v on which the areal radius r, defined with angular labels constant along the cone's
ingoing null generators (Bondi's labels, fixed at past null infinity), is constant.  The same sections are rebuilt here
from a double-null run, so that the second zero can be looked for in an independent formulation and gauge:
  - on C_{v_j} the ingoing generators of dnsolve5's gauge obey dx/du = (1 - x^2) s (CERTIFY-10L5.md D381); their labels
    xi are their angles on the outer cone u = -R0 = -10 (Bondi's at past null infinity are not available to a run that
    starts at R0; the angular drift between R0 and infinity is the difference, of the order of the shift there);
  - the areal radius in those labels is R_B = R (dx/dxi)^(1/3), since the section volume density is R^3/4 in x
    (sectexp5.py) and dx/dxi is carried by d(dx/dxi)/du = d_x((1 - x^2) s) dx/dxi along each generator;
  - the sphere R_B = r is the section u = U(xi), x = X(xi), and its expansion is sectexp5.py's X2 formula.
Masked cells (dnsolve5's cut) and cells next to them are never used.  The library has no check of its own; its checks
are in secondzero5.py (B1: on Tangherlini the rebuilt spheres are the leaves and their expansion is 3 R_v/R).
"""
import os, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('sectexp5', os.path.join(HERE, 'sectexp5.py'))
SE = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(SE)
NAMES = SE.NAMES
_THETA = None


def theta_fn():
    global _THETA
    if _THETA is None:
        _THETA = SE.theta_numeric(True)
    return _THETA


def cheb_nodes(M):
    return np.cos((np.arange(M) + 0.5) * np.pi / M)


def bary_matrix(xn, xe):
    """values at Chebyshev-Gauss nodes xn -> values at points xe (barycentric, first kind)"""
    M = len(xn)
    w = (-1.0) ** np.arange(M) * np.sin((2 * np.arange(M) + 1) * np.pi / (2 * M))
    d = xe[:, None] - xn[None, :]
    exact = np.isclose(d, 0.0, atol=1e-15)
    d = np.where(exact, 1.0, d)
    B = w[None, :] / d
    B = B / B.sum(1, keepdims=True)
    rows = exact.any(1)
    if rows.any():
        B[rows] = exact[rows].astype(float)
    return B


def diff_matrix(M):
    xn = cheb_nodes(M)
    T = np.cos(np.outer(np.arange(M), np.arccos(xn)))
    Tinv = np.linalg.inv(T.T)
    Dc = np.zeros((M, M))
    for k in range(M):
        for l in range(k - 1, -1, -2):
            Dc[l, k] = 2 * k
        if k % 2 == 1:
            Dc[0, k] = k
    return T.T @ Dc @ Tinv


def load(path):
    Z = dict(np.load(path, allow_pickle=True))
    Z['M'] = len(Z['x'])
    return Z


def derivatives(Z):
    """F, F_u, F_v, F_x for every field on the run's nodes; NaN wherever a stencil touches a masked cell"""
    u, v, x = Z['u'], Z['v'], Z['x']
    M = len(x)
    D1 = diff_matrix(M)
    mask = Z['mask']
    out = {}
    h1 = np.r_[np.nan, np.diff(u)][:, None, None]; h2 = np.r_[np.diff(u), np.nan][:, None, None]
    for k in NAMES:
        A = np.where(mask[..., None], np.nan, Z[k])
        Au = np.full_like(A, np.nan)
        Au[1:-1] = (-h2[1:-1] / (h1[1:-1] * (h1[1:-1] + h2[1:-1])) * A[:-2]
                    + (h2[1:-1] - h1[1:-1]) / (h1[1:-1] * h2[1:-1]) * A[1:-1]
                    + h1[1:-1] / (h2[1:-1] * (h1[1:-1] + h2[1:-1])) * A[2:])
        Av = np.full_like(A, np.nan)
        dv = v[1] - v[0]
        Av[:, 1:-1] = (A[:, 2:] - A[:, :-2]) / (2 * dv)
        out[k] = A; out[(k, 'u')] = Au; out[(k, 'v')] = Av; out[(k, 'x')] = A @ D1.T
    return out


def generators(Z, F, j, MB):
    """ingoing generators of C_{v_j} with labels xi (MB Chebyshev-Gauss nodes) at u = u[0]: X[i, b], J[i, b] = dx/dxi
    on every row i up to the first row where a needed value is missing"""
    u, x = Z['u'], Z['x']
    xi = cheb_nodes(MB)
    D1 = diff_matrix(len(x))
    Nu = len(u)
    X = np.full((Nu, MB), np.nan); J = np.full((Nu, MB), np.nan)
    X[0] = xi; J[0] = 1.0
    s_row = lambda i: F['s'][i, j]

    def beta_and_bx(i, Xc):
        s = s_row(i)
        if not np.all(np.isfinite(s)):
            return None, None
        B = bary_matrix(x, Xc)
        sx = s @ D1.T
        sv, sxv = B @ s, B @ sx
        return (1 - Xc ** 2) * sv, -2 * Xc * sv + (1 - Xc ** 2) * sxv
    for i in range(Nu - 1):
        du = u[i + 1] - u[i]
        b1, bx1 = beta_and_bx(i, X[i])
        if b1 is None:
            break
        Xs = X[i] + du * b1; Js = J[i] * (1 + du * bx1)
        b2, bx2 = beta_and_bx(i + 1, Xs)
        if b2 is None:
            break
        X[i + 1] = X[i] + 0.5 * du * (b1 + b2)
        J[i + 1] = J[i] * np.exp(0.5 * du * (bx1 + bx2))
    return xi, X, J


def field_at(Z, F, j, rows_frac, Xpts):
    """all fields and first derivatives at (u, v_j, X) with u given as a fractional row index (cubic Lagrange in the
    row index, which is a smooth coordinate: u = -1 + a sinh(linear)), Chebyshev interpolation in x"""
    x = Z['x']
    out = {}
    i0 = np.clip(np.floor(rows_frac).astype(int) - 1, 0, len(Z['u']) - 4)
    t = rows_frac - i0
    L = np.stack([-(t - 1) * (t - 2) * (t - 3) / 6, t * (t - 2) * (t - 3) / 2, -t * (t - 1) * (t - 3) / 2,
                  t * (t - 1) * (t - 2) / 6], -1)
    B = bary_matrix(x, Xpts)
    keys = list(NAMES) + [(k, c) for k in NAMES for c in 'uvx']
    for key in keys:
        A = F[key][:, j]                      # (Nu, M)
        vals = np.stack([A[i0 + q] for q in range(4)], 1)      # (npts, 4, M)
        rowv = np.einsum('pqm,pq->pm', vals, L)
        out[key] = np.einsum('pm,pm->p', rowv, B)
    return out


def sphere(Z, F, j, r, MB=32, gen=None):
    """the sphere R_B = r on C_{v_j}: xi, U(xi), X(xi), theta(xi); NaN where it is not inside the usable rows"""
    xi, X, J = gen if gen is not None else generators(Z, F, j, MB)
    u = Z['u']
    Nu = len(u)
    Rrow = F['R'][:, j]
    RB = np.full_like(X, np.nan)
    for i in range(Nu):
        if np.all(np.isfinite(X[i])) and np.all(np.isfinite(Rrow[i])):
            RB[i] = (bary_matrix(Z['x'], X[i]) @ Rrow[i]) * J[i] ** (1 / 3)
    fr = np.full(len(xi), np.nan)
    for b in range(len(xi)):
        col = RB[:, b]
        ok = np.isfinite(col)
        idx = np.nonzero(ok[:-1] & ok[1:] & (col[:-1] >= r) & (col[1:] < r))[0]
        if len(idx) == 0:
            continue
        i = idx[0]
        fr[b] = i + (col[i] - r) / (col[i] - col[i + 1])
    # usable: four rows around and their u-, v-stencils finite
    need = np.isfinite(fr)
    for b in np.nonzero(need)[0]:
        i0 = max(int(np.floor(fr[b])) - 1, 0)
        blk = F[('R', 'u')][i0:i0 + 4, j]
        blk2 = F[('R', 'v')][i0:i0 + 4, j]
        if blk.shape[0] < 4 or not (np.all(np.isfinite(blk)) and np.all(np.isfinite(blk2))):
            need[b] = False
    fr = np.where(need, fr, np.nan)
    if np.isnan(fr).any():
        return xi, None, None, np.full(len(xi), np.nan)
    # U(xi) and X(xi): interpolate the generators' u and x at the fractional rows
    iA = np.floor(fr).astype(int); t = fr - iA
    Ux = u[iA] + t * (u[iA + 1] - u[iA])               # u is smooth in the row index; refined below
    # u as a cubic in the row index
    i0 = np.clip(iA - 1, 0, Nu - 4); tt = fr - i0
    L = np.stack([-(tt - 1) * (tt - 2) * (tt - 3) / 6, tt * (tt - 2) * (tt - 3) / 2, -tt * (tt - 1) * (tt - 3) / 2,
                  tt * (tt - 1) * (tt - 2) / 6], -1)
    Ux = np.einsum('pq,pq->p', np.stack([u[i0 + q] for q in range(4)], 1), L)
    Xx = np.einsum('pq,pq->p', np.stack([X[i0 + q, np.arange(len(xi))] for q in range(4)], 1), L)
    Dxi = diff_matrix(len(xi))
    U1, U2 = Dxi @ Ux, Dxi @ (Dxi @ Ux)
    X1, X2 = Dxi @ Xx, Dxi @ (Dxi @ Xx)
    f = field_at(Z, F, j, fr, Xx)
    Fd = {k: f[k] for k in NAMES}
    dF = {(k, c): f[(k, c)] for k in NAMES for c in 'uvx'}
    th = theta_fn()(Xx, Fd, dF, U1, X1, U2, X2)
    return xi, Ux, Xx, np.asarray(th, float)
