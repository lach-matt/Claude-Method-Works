"""Curvature and proper time along an interior evolution (FW's RSII hole)."""
import numpy as np, sympy as sp, pickle
import core_fw as C
_K = None
def fK():
    global _K
    if _K is None:
        K = sp.sympify(eval(pickle.load(open("kretsch_fw.pkl", "rb")), {**sp.__dict__}))
        _K = sp.lambdify([C.s, C.x, C.bt] + C.VARS, K, "numpy", cse=True)
    return _K

def fields_full(I, s, Y):
    """all nodal fields with first and second derivatives at s; X_ss from the field equations at the inner nodes and
    at the brane node (the equations are regular there, Delta = 1/bt), and at the axis node by interpolating the
    inner and brane values (the equations carry 1/x there)"""
    import interior_fw as IF
    m = I.m; Nx = I.Nx; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
    Xf, Vf = I.brane_values(s, Xi, Vi)
    DX = Xf @ I.D.T; DXX = Xf @ I.D2.T; DV = Vf @ I.D.T
    idx = np.arange(1, Nx + 1); xs = I.xn[idx]; k = len(idx); a = []
    for e in range(5):
        a += [Xf[e, idx], Vf[e, idx], DX[e, idx], np.zeros(k), DXX[e, idx], DV[e, idx]]
    rest = np.array([np.broadcast_to(np.asarray(r, dtype=float), (k,)) for r in IF.f_rest(np.full(k, s), xs, I.b, *a)])
    co = IF.f_coef(np.full(k, s), xs, I.b, *a)
    M = np.empty((k, 5, 5))
    for e in range(5):
        for q in range(5):
            M[:, e, q] = np.broadcast_to(np.asarray(co[e][q], dtype=float), (k,))
    Xss_part = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
    Xss = np.zeros_like(Xf); Xss[:, 1:] = Xss_part
    for e in range(5):
        Xss[e, 0] = C.bary_interp(I.xn[1:], Xss_part[e], [I.xn[0]])[0]
    return Xf, Vf, Xss

def kretschmann(I, s, Y):
    Xf, Vf, Xss = fields_full(I, s, Y); a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e], Xss[e], I.D2 @ Xf[e], I.D @ Vf[e]]
    with np.errstate(all="ignore"):
        return np.asarray(fK()(np.full(I.Nx + 1, s), I.xn, I.b, *a), dtype=float)

def gss(I, s, Y):
    """|g_ss| at the nodes: A/(f^4 |s|)/Delta^2"""
    m = I.m; Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    f = 1 - s; Dl = 1 / I.b + (1 - I.xn ** 2) / f
    return Xf[2] / (f ** 4 * abs(s)) / Dl ** 2
