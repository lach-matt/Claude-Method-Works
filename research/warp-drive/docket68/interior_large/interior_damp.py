"""The interior evolution with constraint damping (gen_damp_fw.py): rest += D_ab / nrm at the inner nodes."""
import numpy as np, sympy as sp, sys, time, pickle
import core_fw as C, interior_fw as IF
from scipy.integrate import solve_ivp
kap_, at_ = sp.symbols("kap at", real=True)
_raw = pickle.load(open("damp_%s.pkl" % C.PROB, "rb"))
DMP = [C.ev(_raw["D"][k]) for k in C.ORDER]
AUX = {k: C.ev(v) for k, v in _raw["aux"].items()}
f_damp = sp.lambdify([C.s, C.x, C.bt, kap_, at_] + C.VARS, DMP, "numpy", cse=True)
f_xi = sp.lambdify([C.s, C.x, C.bt, kap_, at_] + C.VARS, [AUX["xi_s"], AUX["xi_x"]], "numpy", cse=True)

class Damped(IF.Interior):
    def __init__(self, Nx, b, static, kap=2.0, at=0.5):
        super().__init__(Nx, b, static); self.kap, self.at = kap, at

    def rhs(self, s, Y):
        m = self.m; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
        Xf, Vf = self.brane_values(s, Xi, Vi)
        DX = Xf @ self.D.T; DXX = Xf @ self.D2.T; DV = Vf @ self.D.T
        I = self.inner; xs = self.xn[I]; ss = np.full(m, s); a = []
        for e in range(5):
            a += [Xf[e, I], Vf[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        rest = np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in IF.f_rest(ss, xs, self.b, *a)])
        if self.kap:
            with np.errstate(all="ignore"):
                dm = f_damp(ss, xs, self.b, self.kap, self.at, *a)
            rest = rest + np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in dm])
        co = IF.f_coef(ss, xs, self.b, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        Xss = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
        return np.concatenate([Y[5 * m:], Xss.ravel()])

def xi_at(I, s, Y):
    m = I.m; Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e], np.zeros(I.Nx + 1), I.D2 @ Xf[e], I.D @ Vf[e]]
    with np.errstate(all="ignore"):
        return [np.asarray(v, dtype=float) * np.ones(I.Nx + 1) for v in f_xi(np.full(I.Nx + 1, s), I.xn, I.b, 0, 0, *a)]

def static_brane(b, Ns=24, Nx=24):
    U = np.load(C.static_file(b, Ns, Nx)); n = (Ns + 1) * (Nx + 1); sn = C.radau01(Ns)
    return np.array([C.bary_interp(sn, U[e * n:(e + 1) * n].reshape(Ns + 1, Nx + 1), [0.0])[0][-1] for e in range(4)])

if __name__ == "__main__":
    Nx, b, s0, s1, kap, at = (int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]),
                              float(sys.argv[5]), float(sys.argv[6]))
    rtol = float(sys.argv[7]) if len(sys.argv) > 7 else 1e-8
    st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
    I = Damped(Nx, b, st, kap, at); I.lastbr = static_brane(b); m = I.m
    Y0 = I.initial(s0, 2); t0 = time.time(); log = []
    def mon(s, Y):
        return 0.0
    sol = solve_ivp(I.rhs, (s0, s1), Y0, method="Radau", rtol=rtol, atol=rtol * 1e-2)
    print("damped Nx=%d bt=%g kap=%g at=%g s0=%g -> %g: status %d (%s), %d steps, %.0f s" % (
        Nx, b, kap, at, s0, s1, sol.status, sol.message, len(sol.t), time.time() - t0), flush=True)
    out = "idmp_%d_%g_%g_%g_%g.pkl" % (Nx, b, kap, at, s1)
    pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, b=b, s0=s0, kap=kap, at=at), open(out, "wb"))
    print("saved", out, flush=True)
