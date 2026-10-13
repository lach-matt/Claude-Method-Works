"""The interior with the lapse driver (gen_gauge_fw.py) on top of the damping: rest += (D_ab + G_ab) / nrm.  Switched
on at s1 from a run's state, with Nst(x) = N + Fbar^s N^3 / mu there, so that xi~ = xi - h vanishes on the switch
slice."""
import numpy as np, sympy as sp, sys, time, pickle
import core_fw as C, interior_fw as IF, interior_damp as ID
from scipy.integrate import solve_ivp
mu_, s1_ = sp.symbols("mu s1", real=True)
NS, NSX = sp.Symbol("Nst"), sp.Symbol("Nst_x")
_raw = pickle.load(open("gauge_fw.pkl", "rb"))
GG = [C.ev(_raw["D"][k]) for k in C.ORDER]
AX = {k: C.ev(v) for k, v in _raw["aux"].items()}
ARGS = [C.s, C.x, C.bt, mu_, s1_, NS, NSX] + C.VARS
f_gauge = sp.lambdify(ARGS, GG, "numpy", cse=True)
f_hs = sp.lambdify(ARGS, AX["hs"], "numpy", cse=True)
f_N = sp.lambdify(ARGS, AX["N"], "numpy", cse=True)
f_Fb = sp.lambdify(ARGS, AX["Fbar_s"], "numpy", cse=True)

class Gauge(ID.Damped):
    def __init__(self, Nx, b, static, kap, at, mu, s1, Nst):
        super().__init__(Nx, b, static, kap, at); self.mu, self.s1 = mu, s1
        self.Nst = np.asarray(Nst, dtype=float); self.Nst_x = self.D @ self.Nst

    def rhs(self, s, Y):
        m = self.m; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
        Xf, Vf = self.brane_values(s, Xi, Vi)
        DX = Xf @ self.D.T; DXX = Xf @ self.D2.T; DV = Vf @ self.D.T
        I = self.inner; xs = self.xn[I]; ss = np.full(m, s); a = []
        for e in range(5):
            a += [Xf[e, I], Vf[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        bc = lambda L: np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in L])
        rest = bc(IF.f_rest(ss, xs, self.b, *a))
        with np.errstate(all="ignore"):
            if self.kap:
                rest = rest + bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a))
            rest = rest + bc(f_gauge(ss, xs, self.b, self.mu, self.s1, self.Nst[I], self.Nst_x[I], *a))
        co = IF.f_coef(ss, xs, self.b, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        Xss = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
        return np.concatenate([Y[5 * m:], Xss.ravel()])

def nodal_args(I, s, Y):
    m = I.m; Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e], np.zeros(I.Nx + 1), I.D2 @ Xf[e], I.D @ Vf[e]]
    return Xf, Vf, a

def lapse_and_Fbar(I, s, Y, mu=1.0, s1=0.0):
    Xf, Vf, a = nodal_args(I, s, Y); n = I.Nx + 1; z = np.zeros(n)
    with np.errstate(all="ignore"):
        N = np.asarray(f_N(np.full(n, s), I.xn, I.b, mu, s1, z, z, *a), dtype=float) * np.ones(n)
        Fb = np.asarray(f_Fb(np.full(n, s), I.xn, I.b, mu, s1, z, z, *a), dtype=float) * np.ones(n)
    return N, Fb

def phi_tilde(I, s, Y):
    """g(xi~, xi~) with xi~ = xi - h, the constraint the driven evolution keeps"""
    Xf, Vf, a = nodal_args(I, s, Y); n = I.Nx + 1
    with np.errstate(all="ignore"):
        xs_, xx_ = [np.asarray(v, dtype=float) * np.ones(n) for v in ID.f_xi(np.full(n, s), I.xn, I.b, 0, 0, *a)]
        hs = np.asarray(f_hs(np.full(n, s), I.xn, I.b, I.mu, I.s1, I.Nst, I.Nst_x, *a), dtype=float) * np.ones(n)
    f = 1 - s; Dl = 1 / I.b + (1 - I.xn ** 2) / f; g = 2 - I.xn ** 2
    gss = Xf[2] / (f ** 4 * s) / Dl ** 2; gxx = 4 * Xf[3] / (f ** 2 * g) / Dl ** 2
    gsx = I.xn * Xf[4] / (2 * f ** 3) / Dl ** 2
    xt = xs_ - hs
    return gss * xt ** 2 + 2 * gsx * xt * xx_ + gxx * xx_ ** 2
