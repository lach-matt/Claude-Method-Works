"""The interior with the lapse driver (gen_gauge_fw.py) on top of the damping: rest += (D_ab + G_ab) / nrm.  Switched
on at s1 from a run's state, with Nst(x) = N + Fbar^s N^3 / mu there, so that xi~ = xi - h vanishes on the switch
slice."""
import numpy as np, sympy as sp, sys, time, pickle
import core_fw as C, interior_fw as IF, interior_damp as ID
from scipy.integrate import solve_ivp
mu_, s1_, wF_ = sp.symbols("mu s1 wF", real=True)
NS, NSX, RR, RRS = sp.Symbol("Nst"), sp.Symbol("Nst_x"), sp.Symbol("R"), sp.Symbol("R_s")
import os
_raw = pickle.load(open(os.environ.get("GAUGE_PKL", "gauge3_fw.pkl"), "rb"))
GG = [C.ev(_raw["D"][k]) for k in C.ORDER]
AX = {k: C.ev(v) for k, v in _raw["aux"].items()}
ARGS = [C.s, C.x, C.bt, mu_, s1_, wF_, NS, NSX, RR, RRS] + C.VARS
f_gauge = sp.lambdify(ARGS, GG, "numpy", cse=True)
f_hs = sp.lambdify(ARGS, AX["hs"], "numpy", cse=True)
f_N = sp.lambdify(ARGS, AX["N"], "numpy", cse=True)
f_Fb = sp.lambdify(ARGS, AX["Fbar_s"], "numpy", cse=True)
# the damping must act on xi~ = xi - h: subtract its action on h (gen_damph_fw.py; the untapered driver, wF = 0)
_rh = pickle.load(open("damph_fw.pkl", "rb"))
DH = [C.ev(_rh["D"][k]) for k in C.ORDER]
f_damph = sp.lambdify([C.s, C.x, C.bt, sp.Symbol("kap", real=True), sp.Symbol("at", real=True), mu_, s1_, NS, RR]
                      + C.VARS, DH, "numpy", cse=True)

class Gauge(ID.Damped):
    def __init__(self, Nx, b, static, kap, at, mu, s1, Nst, ramp=0.3, wF=0.0):
        super().__init__(Nx, b, static, kap, at); self.mu, self.s1, self.ramp, self.wF = mu, s1, ramp, wF
        self.Nst = np.asarray(Nst, dtype=float); self.Nst_x = self.D @ self.Nst

    def R(self, s):
        """C^1 smoothstep from 0 at s1 to 1 at s1 - ramp, and its s-derivative"""
        q = min(max((self.s1 - s) / self.ramp, 0.0), 1.0)
        return 3 * q * q - 2 * q ** 3, -(6 * q - 6 * q * q) / self.ramp

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
            R, Rs = self.R(s)
            if self.kap:
                rest = rest + bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a))
                if os.environ.get("GAUGE_PKL", "gauge3_fw.pkl") == "gauge3_fw.pkl":       # damph is the untapered h's
                    rest = rest - bc(f_damph(ss, xs, self.b, self.kap, self.at, self.mu, self.s1, self.Nst[I], R, *a))
            rest = rest + bc(f_gauge(ss, xs, self.b, self.mu, self.s1, self.wF, self.Nst[I], self.Nst_x[I], R, Rs, *a))
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
        N = np.asarray(f_N(np.full(n, s), I.xn, I.b, mu, s1, 0, z, z, 0, 0, *a), dtype=float) * np.ones(n)
        Fb = np.asarray(f_Fb(np.full(n, s), I.xn, I.b, mu, s1, 0, z, z, 0, 0, *a), dtype=float) * np.ones(n)
    return N, Fb

def phi_tilde(I, s, Y):
    """g(xi~, xi~) with xi~ = xi - h, the constraint the driven evolution keeps"""
    Xf, Vf, a = nodal_args(I, s, Y); n = I.Nx + 1
    with np.errstate(all="ignore"):
        xs_, xx_ = [np.asarray(v, dtype=float) * np.ones(n) for v in ID.f_xi(np.full(n, s), I.xn, I.b, 0, 0, *a)]
        R, Rs = I.R(s)
        hs = np.asarray(f_hs(np.full(n, s), I.xn, I.b, I.mu, I.s1, I.wF, I.Nst, I.Nst_x, R, Rs, *a),
                        dtype=float) * np.ones(n)
    f = 1 - s; Dl = 1 / I.b + (1 - I.xn ** 2) / f; g = 2 - I.xn ** 2
    gss = Xf[2] / (f ** 4 * s) / Dl ** 2; gxx = 4 * Xf[3] / (f ** 2 * g) / Dl ** 2
    gsx = I.xn * Xf[4] / (2 * f ** 3) / Dl ** 2
    xt = xs_ - hs
    return gss * xt ** 2 + 2 * gsx * xt * xx_ + gxx * xx_ ** 2


def run_steps(I, Y_s, s_start, lam_end, rtol=1e-8, every=25, save=None, meta=None):
    """lambda-time evolution stepped by hand (Radau), printing lambda, s, the step and the brane lapse every `every`
    steps and pickling the trajectory so far, so a long run can be followed and resumed"""
    from scipy.integrate import Radau
    m = I.m; f0 = 1.0 - s_start
    Z0 = np.concatenate([Y_s[:5 * m], -f0 * Y_s[5 * m:]])
    sol = Radau(lambda l, z: IF.rhs_lambda(I, l, z), np.log(f0), Z0, lam_end, rtol=rtol, atol=rtol * 1e-2)
    ts, ys = [sol.t], [sol.y.copy()]
    t0 = time.time(); k = 0
    while sol.status == "running":
        msg = sol.step(); k += 1
        ts.append(sol.t); ys.append(sol.y.copy())
        if k % every == 0 or sol.status != "running":
            s, Y = IF.state_s(I, sol.t, sol.y)
            keep = I.lastbr.copy()
            try:
                ph = phi_tilde(I, s, Y) if hasattr(I, "Nst") else IF.phi_at(I, s, Y)
                phm = float(np.nanmax(np.abs(ph[1:])))
            except Exception:
                phm = float("nan")
            I.lastbr = keep
            print("step %d lambda %.4f s %.3f h %.2e phi %.1e  %.0f s" % (k, sol.t, s, sol.step_size or 0, phm,
                                                                        time.time() - t0), flush=True)
            if save:
                pickle.dump(dict(lt=np.array(ts), ly=np.array(ys).T, **(meta or {})), open(save, "wb"))
    print("run_steps: status %s %s, lambda %.4f, %d steps, %.0f s" % (sol.status, msg, sol.t, k, time.time() - t0),
          flush=True)
    return np.array(ts), np.array(ys).T
