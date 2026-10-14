"""Stage B/C: the RSII hole's interior (s < 0), method of lines in x with the brane conditions at x = 1 (K_ab = gamma_ab,
xi^x = 0, F = 0) and the axis conditions at x = 0 solved as algebraic rows at every evaluation."""
import numpy as np, sympy as sp, sys, time, pickle
import core_fw as C
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
SS = [sp.Symbol(n + "_ss") for n in C.names]
f_rest = C.lam([e.subs({v: 0 for v in SS}) for e in C.RES])
f_coef = C.lam([[sp.diff(e, v) for v in SS] for e in C.RES])
f_bc = C.lam(C.BCS)
N3 = [sp.Symbol(n + t) for n in C.names for t in ("", "_s", "_x")]
f_phi = sp.lambdify([C.s, C.x, C.bt] + N3, C.PHI, "numpy", cse=True)

class Interior:
    def __init__(self, Nx, b, static):
        self.Nx, self.b = Nx, b; self.xn = C.lobatto01(Nx); self.D = C.bary_D(self.xn); self.D2 = self.D @ self.D
        self.inner = np.arange(1, Nx); self.m = Nx - 1; self.static = static
        self.lastbr = None

    def axis(self, Xf):
        D = self.D
        for e in (0, 2, 3, 4):
            Xf[e, 0] = -(D[0, 1:] @ Xf[e, 1:]) / D[0, 0]
        Xf[1, 0] = Xf[3, 0]

    def _full(self, xb, Xi, V=False):
        Nx = self.Nx; Xf = np.zeros((5, Nx + 1)); Xf[:, 1:Nx] = Xi; Xf[:4, Nx] = xb; Xf[4, Nx] = 0
        self.axis(Xf)
        return Xf

    def _r(self, s, xb, Xi):
        """the four brane conditions at x = 1, as functions of the brane values xb (T, S, A, B) and the inner
        values; with F = 0 and F_s = 0 on the brane they involve no s-derivatives (checked)"""
        Nx = self.Nx; Xf = self._full(xb, Xi); a = []
        for e in range(5):
            a += [Xf[e, Nx], 0.0, (self.D @ Xf[e])[Nx], 0.0, 0.0, 0.0]
        return np.array([float(r) for r in f_bc(s, 1.0, self.b, *a)])

    def brane_values(self, s, Xi, Vi):
        x0 = self.lastbr if self.lastbr is not None else Xi[:4, -1].copy()
        xb, info, ier, msg = fsolve(lambda q: self._r(s, q, Xi), x0, xtol=1e-13, full_output=True)
        self.lastbr = xb
        # V at the brane by implicit differentiation: J_b V_b + J_in . V_in + dr/ds = 0 (finite differences)
        h = 1e-7; r0 = self._r(s, xb, Xi)
        Jb = np.array([(self._r(s, xb + h * np.eye(4)[k], Xi) - r0) / h for k in range(4)]).T
        dr_in = (self._r(s, xb, Xi + h * Vi) - r0) / h
        dr_s = (self._r(s + h, xb, Xi) - r0) / h
        try:
            vb = np.linalg.solve(Jb, -(dr_in + dr_s))
        except np.linalg.LinAlgError:
            vb = np.linalg.lstsq(Jb, -(dr_in + dr_s), rcond=None)[0]
        Xf = self._full(xb, Xi)
        Nx = self.Nx; Vf = np.zeros((5, Nx + 1)); Vf[:, 1:Nx] = Vi; Vf[:4, Nx] = vb; Vf[4, Nx] = 0
        self.axis(Vf)
        return Xf, Vf

    def rhs(self, s, Y):
        m = self.m; Nx = self.Nx
        Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
        Xf, Vf = self.brane_values(s, Xi, Vi)
        DX = Xf @ self.D.T; DXX = Xf @ self.D2.T; DV = Vf @ self.D.T
        I = self.inner; xs = self.xn[I]; ss = np.full(m, s); a = []
        for e in range(5):
            a += [Xf[e, I], Vf[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        rest = np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in f_rest(ss, xs, self.b, *a)])
        co = f_coef(ss, xs, self.b, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        Xss = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
        return np.concatenate([Y[5 * m:], Xss.ravel()])

    def initial(self, s0, order=4):
        """X and X_s at s0 < 0 by a Taylor expansion about s = 0, the derivatives taken at s = 0 from the static
        solution's polynomial in s (extrapolating the high-degree polynomial itself amplifies its error)"""
        Gf = self.static; U = np.load(Gf["file"]); n = (Gf["Ns"] + 1) * (Gf["Nx"] + 1)
        sn, xn = C.radau01(Gf["Ns"]), C.lobatto01(Gf["Nx"]); Ds1 = C.bary_D(sn)
        X0 = np.zeros((5, self.Nx + 1)); V0 = np.zeros((5, self.Nx + 1))
        import math
        for e in range(5):
            Fm = U[e * n:(e + 1) * n].reshape(Gf["Ns"] + 1, Gf["Nx"] + 1)
            ders = []; M = Fm.copy()
            for k in range(order + 2):
                ders.append(C.bary_interp(xn, C.bary_interp(sn, M, [0.0])[0], self.xn)); M = Ds1 @ M
            X0[e] = sum(ders[k] * s0 ** k / math.factorial(k) for k in range(order + 1))
            V0[e] = sum(ders[k + 1] * s0 ** k / math.factorial(k) for k in range(order + 1))
        return np.concatenate([X0[:, self.inner].ravel(), V0[:, self.inner].ravel()])


def run(Nx, b, static, s0, s1, rtol=1e-8, method="Radau", order=2):
    I = Interior(Nx, b, static); Y0 = I.initial(s0, order); t0 = time.time()
    sol = solve_ivp(I.rhs, (s0, s1), Y0, method=method, rtol=rtol, atol=rtol * 1e-2, dense_output=True)
    print("Nx=%d bt=%g s0=%g -> %g: status %d (%s), %d steps, %.0f s" % (Nx, b, s0, s1, sol.status, sol.message,
                                                                    len(sol.t), time.time() - t0), flush=True)
    return I, sol

def phi_at(I, s, Y):
    m = I.m; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
    Xf, Vf = I.brane_values(s, Xi, Vi); a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e]]
    with np.errstate(all="ignore"):
        return np.asarray(f_phi(np.full(I.Nx + 1, s), I.xn, I.b, *a), dtype=float)

if __name__ == "__main__":
    Nx, b, s0, s1 = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    Ns_st, Nx_st = int(sys.argv[5]), int(sys.argv[6])
    rtol = float(sys.argv[7]) if len(sys.argv) > 7 else 1e-8
    static = dict(file="fw_bt%g_%d_%d.npy" % (b, Ns_st, Nx_st), Ns=Ns_st, Nx=Nx_st)
    I, sol = run(Nx, b, static, s0, s1, rtol=rtol)
    m = I.m
    pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, b=b, s0=s0), open("ifw_%d_%g_%g_%g.pkl" % (Nx, b, s0, s1), "wb"))
    for sv in np.linspace(s0, sol.t[-1], 9):
        Y = sol.sol(sv); Xf, Vf = I.brane_values(sv, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
        print("s=%9.4f  T(ax)=%.6f T(brane)=%.6f minT=%.3e  max|V|=%.2e  max|phi|=%.2e" %
              (sv, Xf[0, 0], Xf[0, -1], Xf[0].min(), np.abs(Vf).max(), np.nanmax(np.abs(phi_at(I, sv, Y)))), flush=True)
    pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, b=b, s0=s0), open("ifw_%d_%g_%g_%g.pkl" % (Nx, b, s0, s1), "wb"))


def rhs_lambda(I, lam, Z):
    """lambda = log(1 - s): state (X, W = X_lambda = -(1 - s) X_s); X' = W, W' = W + (1 - s)^2 X_ss"""
    m = I.m; s = 1.0 - np.exp(lam); f = 1.0 - s
    X = Z[:5 * m]; W = Z[5 * m:]
    Y = np.concatenate([X, -W / f])
    d = I.rhs(s, Y)
    Xss = d[5 * m:]
    return np.concatenate([W, W + f * f * Xss])

def run_lambda(I, Y_s, s_start, lam_end, rtol=1e-8, method="Radau", events=None):
    m = I.m; f0 = 1.0 - s_start
    Z0 = np.concatenate([Y_s[:5 * m], -f0 * Y_s[5 * m:]])
    t0 = time.time()
    sol = solve_ivp(lambda l, z: rhs_lambda(I, l, z), (np.log(f0), lam_end), Z0, method=method, rtol=rtol,
                    atol=rtol * 1e-2, dense_output=True, events=events)
    print("lambda-run: %.4f -> %.4f status %d (%s), %d steps, %.0f s" % (np.log(f0), sol.t[-1], sol.status, sol.message,
                                                                    len(sol.t), time.time() - t0), flush=True)
    return sol

def state_s(I, lam, Z):
    m = I.m; s = 1.0 - np.exp(lam); f = 1.0 - s
    return s, np.concatenate([Z[:5 * m], -Z[5 * m:] / f])
