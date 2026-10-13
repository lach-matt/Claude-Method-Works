"""The interior with gen_gauge5_fw.py's driver: one function of s steers the slicing (item 365, first step).  On each
slice E(s) = -<ln(N / (Nst c(s)))>, the average taken by Clenshaw-Curtis weights over x (mode "mean") or the brane
node alone (mode "brane"), with c(s) = (1 - s1)/(1 - s); E_s is its exact s-derivative from the fields' s-derivatives.
Every x then gets the same relative push mu E, so the driver rescales the lapse without pinning its x-profile.
rest += D(xi) - D(h) + nabla h, the damping acting on xi~ = xi - h."""
import numpy as np, sympy as sp, pickle
import core_fw as C, interior_fw as IF, interior_damp as ID
mu_ = sp.Symbol("mu", real=True); kap_, at_ = sp.symbols("kap at", real=True)
EE, EES, RR, RRS = sp.Symbol("E"), sp.Symbol("E_s"), sp.Symbol("R"), sp.Symbol("R_s")
import os
ARGS = [C.s, C.x, C.bt, mu_, EE, EES, RR, RRS] + C.VARS
f_gauge = f_damph = f_hs = f_N = f_Ns = None              # absent for a problem without gauge5_<PROB>.pkl
if C.PROB == "fw" or os.path.exists("gauge5_%s.pkl" % C.PROB):
    _raw = pickle.load(open("gauge5_%s.pkl" % C.PROB, "rb"))
    f_gauge = sp.lambdify(ARGS, [C.ev(_raw["D"][k]) for k in C.ORDER], "numpy", cse=True)
    f_damph = sp.lambdify([C.s, C.x, C.bt, kap_, at_, mu_, EE, RR] + C.VARS, [C.ev(_raw["DH"][k]) for k in C.ORDER],
                          "numpy", cse=True)
    AX = {k: C.ev(v) for k, v in _raw["aux"].items()}
    f_hs = sp.lambdify(ARGS, AX["hs"], "numpy", cse=True)
    f_N = sp.lambdify(ARGS, AX["N"], "numpy", cse=True)
    f_Ns = sp.lambdify(ARGS, AX["N_s"], "numpy", cse=True)

def cc_weights(Nx):
    """Clenshaw-Curtis weights on lobatto01(Nx) (x in [0, 1], ascending), normalised to sum 1"""
    th = np.pi * np.arange(Nx + 1) / Nx; w = np.zeros(Nx + 1)
    for j in range(Nx + 1):
        acc = 1.0
        for k in range(1, Nx // 2 + 1):
            bk = 1.0 if 2 * k == Nx else 2.0
            acc -= bk * np.cos(2 * k * th[j]) / (4 * k * k - 1)
        w[j] = acc * (1.0 if j in (0, Nx) else 2.0) / Nx
    w = w[::-1]                                                  # lobatto01 sorts ascending: x = (1 - cos th)/2
    return w / w.sum()

def full_args(I, Xf, Vf):
    a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e], np.zeros(I.Nx + 1), I.D2 @ Xf[e], I.D @ Vf[e]]
    return a

class Gauge5(ID.Damped):
    def __init__(self, Nx, b, static, kap, at, mu, s1, Nst, ramp=0.3, mode="mean"):
        super().__init__(Nx, b, static, kap, at); self.mu, self.s1, self.ramp, self.mode = mu, s1, ramp, mode
        self.Nst = np.asarray(Nst, dtype=float)
        self.w = cc_weights(Nx) if mode == "mean" else np.eye(Nx + 1)[Nx]
        self.last_E = (0.0, 0.0)

    def R(self, s):
        q = min(max((self.s1 - s) / self.ramp, 0.0), 1.0)
        return 3 * q * q - 2 * q ** 3, -(6 * q - 6 * q * q) / self.ramp

    def lapse(self, s, Xf, Vf):
        """N and N_s at every node, the axis node from evenness in x as gauge_run.py takes Nst there"""
        n = self.Nx + 1; a = full_args(self, Xf, Vf); z = np.zeros(n)
        with np.errstate(all="ignore"):
            N = np.asarray(f_N(np.full(n, s), self.xn, self.b, 0, z, z, 0, 0, *a), dtype=float) * np.ones(n)
            Ns = np.asarray(f_Ns(np.full(n, s), self.xn, self.b, 0, z, z, 0, 0, *a), dtype=float) * np.ones(n)
        for v in (N, Ns):
            v[0] = -(self.D[0, 1:] @ v[1:]) / self.D[0, 0]
        return N, Ns

    def E(self, s, Xf, Vf):
        N, Ns = self.lapse(s, Xf, Vf)
        c = (1 - self.s1) / (1 - s)
        r = self.w @ np.log(N / (self.Nst * c))
        r_s = self.w @ (Ns / N) - 1.0 / (1 - s)
        self.last_E = (-r, -r_s)
        return -r, -r_s

    def rhs(self, s, Y):
        m = self.m; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
        Xf, Vf = self.brane_values(s, Xi, Vi)
        DX = Xf @ self.D.T; DXX = Xf @ self.D2.T; DV = Vf @ self.D.T
        I = self.inner; xs = self.xn[I]; ss = np.full(m, s); a = []
        for e in range(5):
            a += [Xf[e, I], Vf[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        bc = lambda L: np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in L])
        rest = bc(IF.f_rest(ss, xs, self.b, *a))
        R, Rs = self.R(s)
        E, Es = self.E(s, Xf, Vf) if (R or Rs) else (0.0, 0.0)
        with np.errstate(all="ignore"):
            if self.kap:
                rest = rest + bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a))
                rest = rest - bc(f_damph(ss, xs, self.b, self.kap, self.at, self.mu, E, R, *a))
            rest = rest + bc(f_gauge(ss, xs, self.b, self.mu, E, Es, R, Rs, *a))
        co = IF.f_coef(ss, xs, self.b, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        Xss = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
        return np.concatenate([Y[5 * m:], Xss.ravel()])

    def phi_t(self, s, Y):
        """g(xi~, xi~) with xi~ = xi - h"""
        m = self.m; n = self.Nx + 1
        Xf, Vf = self.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); a = full_args(self, Xf, Vf)
        R, Rs = self.R(s); E, Es = self.E(s, Xf, Vf)
        with np.errstate(all="ignore"):
            xs_, xx_ = [np.asarray(v, dtype=float) * np.ones(n) for v in ID.f_xi(np.full(n, s), self.xn, self.b, 0, 0,
                                                                                    *a)]
            hs = np.asarray(f_hs(np.full(n, s), self.xn, self.b, self.mu, E, Es, R, Rs, *a), dtype=float) * np.ones(n)
        f = 1 - s; Dl = 1 / self.b + (1 - self.xn ** 2) / f; g = 2 - self.xn ** 2
        gss = Xf[2] / (f ** 4 * s) / Dl ** 2; gxx = 4 * Xf[3] / (f ** 2 * g) / Dl ** 2
        gsx = self.xn * Xf[4] / (2 * f ** 3) / Dl ** 2
        xt = xs_ - hs
        return gss * xt ** 2 + 2 * gsx * xt * xx_ + gxx * xx_ ** 2
