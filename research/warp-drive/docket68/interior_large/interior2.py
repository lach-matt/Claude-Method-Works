"""Stage B2 (vectorised): the interior, s = r^2 < 0, method of lines in x, implicit integration in s."""
import numpy as np, sympy as sp, sys, time, pickle, os
import core_sx as C
from scipy.integrate import solve_ivp
SSVARS = [sp.Symbol(n + "_ss") for n in C.names]
CACHE = "interior_funcs.pkl"
REST = [e.subs({v: 0 for v in SSVARS}) for e in C.RES]
COEF = [[sp.diff(e, v) for v in SSVARS] for e in C.RES]
f_rest = C.lam(REST)
f_coef = C.lam(COEF)
NAMES3 = [sp.Symbol(n + t) for n in C.names for t in ("", "_s", "_x")]
f_phi = sp.lambdify([C.s, C.x] + NAMES3, C.PHI, "numpy", cse=True)

def static_setup(Ns, Nx):
    return dict(Ns=Ns, Nx=Nx, sn=C.radau01(Ns), xn=C.lobatto01(Nx))

class Interior:
    def __init__(self, Nx, static_file, Ns_static, Nx_static):
        self.Nx = Nx; self.xn = C.lobatto01(Nx); self.D = C.bary_D(self.xn); self.D2 = self.D @ self.D
        self.inner = np.arange(1, Nx); self.m = Nx - 1
        self.st = dict(file=static_file, Ns=Ns_static, Nx=Nx_static)
        self.target = np.array([1, 1, 1, 1, 0.0])
        D = self.D
        # axis rows as linear maps from inner values
        self.ax = -D[0, 1:Nx] / D[0, 0]; self.axb = -D[0, Nx] / D[0, 0]

    def fill(self, Xi, V=False):
        Nx = self.Nx; Xf = np.zeros((5, Nx + 1)); Xf[:, 1:Nx] = Xi
        Xf[:, Nx] = 0 if V else self.target
        for e in (0, 2, 3, 4):
            Xf[e, 0] = self.ax @ Xi[e] + self.axb * Xf[e, Nx]
        Xf[1, 0] = Xf[3, 0]
        return Xf

    def pieces(self, s, Y):
        m = self.m
        Xf = self.fill(Y[:5 * m].reshape(5, m)); Vf = self.fill(Y[5 * m:].reshape(5, m), V=True)
        DX = Xf @ self.D.T; DXX = Xf @ self.D2.T; DV = Vf @ self.D.T
        I = self.inner
        a = []
        for e in range(5):
            a += [Xf[e, I], Vf[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        return Xf, Vf, a

    def rhs(self, s, Y):
        m = self.m; xs = self.xn[self.inner]; ss = np.full(m, s)
        Xf, Vf, a = self.pieces(s, Y)
        rest = np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in f_rest(ss, xs, *a)])   # 5 x m
        co = f_coef(ss, xs, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        Xss = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
        return np.concatenate([Y[5 * m:], Xss.ravel()])

    def initial(self, s0):
        G = static_setup(self.st["Ns"], self.st["Nx"]); U = np.load(self.st["file"])
        n = (G["Ns"] + 1) * (G["Nx"] + 1); Ds1 = C.bary_D(G["sn"])
        X0 = np.zeros((5, self.Nx + 1)); V0 = np.zeros((5, self.Nx + 1))
        for e in range(5):
            Fm = U[e * n:(e + 1) * n].reshape(G["Ns"] + 1, G["Nx"] + 1)
            X0[e] = C.bary_interp(G["xn"], C.bary_interp(G["sn"], Fm, [s0])[0], self.xn)
            V0[e] = C.bary_interp(G["xn"], C.bary_interp(G["sn"], Ds1 @ Fm, [s0])[0], self.xn)
        return np.concatenate([X0[:, self.inner].ravel(), V0[:, self.inner].ravel()])

    def phi(self, s, Y):
        m = self.m; xs = self.xn[self.inner]
        Xf, Vf, a6 = self.pieces(s, Y)
        a = []
        for e in range(5):
            a += [a6[6 * e], a6[6 * e + 1], a6[6 * e + 2]]
        return np.asarray(f_phi(np.full(m, s), xs, *a), dtype=float)

def run(Nx, s0, s1, rtol=1e-8, method="Radau", static=("solsx_28_28.npy", 28, 28), verbose=True):
    I = Interior(Nx, *static); Y0 = I.initial(s0)
    t0 = time.time()
    sol = solve_ivp(I.rhs, (s0, s1), Y0, method=method, rtol=rtol, atol=rtol * 1e-2, dense_output=True)
    if verbose:
        print("Nx=%d s0=%g -> %g: status %d (%s), %d steps, %.0f s" % (Nx, s0, s1, sol.status, sol.message, len(sol.t),
                                                                  time.time() - t0), flush=True)
    return I, sol

if __name__ == "__main__":
    Nx = int(sys.argv[1]); s0 = float(sys.argv[2]); s1 = float(sys.argv[3])
    I, sol = run(Nx, s0, s1)
    m = I.m
    for sv in np.linspace(s0, sol.t[-1], 9):
        Y = sol.sol(sv); Xf = I.fill(Y[:5 * m].reshape(5, m))
        print("s=%9.4f  T(ax)=%.6f A(ax)=%.6f B(ax)=%.6f F(mid)=%+.4f  max|phi| %.2e" %
              (sv, Xf[0, 0], Xf[2, 0], Xf[3, 0], Xf[4, Nx // 2], np.abs(I.phi(sv, Y)).max()), flush=True)
    pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, s0=s0), open("int2_%d_%g_%g.pkl" % (Nx, s0, s1), "wb"))
