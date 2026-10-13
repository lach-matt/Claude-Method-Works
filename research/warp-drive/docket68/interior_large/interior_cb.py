"""Every constraint component imposed at the brane (item 367, the first of item 366's proposals: Wang and Choptuik's
cure, LITERATURE-366 L1).  The brane rows for T, S, A, B stay as they were (Israel K_ab = gamma_ab and xi^x = 0, with
F = F_s = 0 on the brane; checked: with those substituted no row involves F_x), and the remaining component is imposed
too: xi~^s = xi^s - h^s = 0 at x = 1.  On the brane xi^s is affine in F_x (checked: coefficient s (1 - s)^3/(8 A B
bt^2), with no x-derivative of T, S, A, B), so the row fixes the brane slope F_x(1).  F(1) = 0 is kept by writing
F = (1 - x) p(x), p the Lobatto interpolant of p_j = F_j/(1 - x_j) at the inner nodes, p(1) = -F_x(1), and p(0) from
F_x(0) = 0 (the axis row).  F_s is treated the same way with q(1) = -F_xs(1), the row's s-derivative taken along the
flow (a second pass that uses the first pass's X_ss).  The state is unchanged: F and F_s at the inner nodes; only the
x-derivatives of F change near the brane."""
import numpy as np
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_gauge as IG, interior_gauge5 as G5

def _bc(L, m):
    return np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in L])

class CB:
    """mixin; the host supplies rest_extra(s, ss, xs, a, Xg, Vg), hs_full(s, Xg, Vg, afull), hs_brane(s, Xf, Vf)"""
    dlt = 1e-3

    def brane_args(self, Xf, Vf, Fxb):
        Nx = self.Nx; a = []
        for e in range(5):
            a += [Xf[e, Nx], Vf[e, Nx], (self.D @ Xf[e])[Nx] if e < 4 else Fxb, 0.0, 0.0, 0.0]
        return a

    def slope(self, s, Xf, Vf):
        """F_x(1) from xi^s - h^s = 0 on the brane"""
        with np.errstate(all="ignore"):
            x0 = float(np.asarray(ID.f_xi(s, 1.0, self.b, 0, 0, *self.brane_args(Xf, Vf, 0.0))[0]))
            x1 = float(np.asarray(ID.f_xi(s, 1.0, self.b, 0, 0, *self.brane_args(Xf, Vf, 1.0))[0]))
        return (self.hs_brane(s, Xf, Vf) - x0) / (x1 - x0)

    def fdx(self, Fv, Fxb):
        """F (or F_s) as (1 - x) p: nodal values, x- and xx-derivatives, with F(1) = 0, F_x(1) = Fxb, F_x(0) = 0"""
        x = self.xn; Nx = self.Nx; p = np.empty(Nx + 1)
        p[1:Nx] = Fv[1:Nx] / (1 - x[1:Nx]); p[Nx] = -Fxb
        p[0] = -(self.D[0, 1:] @ p[1:]) / (self.D[0, 0] - 1.0)
        Dp = self.D @ p
        return (1 - x) * p, -p + (1 - x) * Dp, -2 * Dp + (1 - x) * (self.D2 @ p)

    def derivs(self, Xf, Vf, Fxb, Fxsb):
        Xg = Xf.copy(); Vg = Vf.copy()
        DX = Xg @ self.D.T; DXX = Xg @ self.D2.T; DV = Vg @ self.D.T
        Xg[4], DX[4], DXX[4] = self.fdx(Xf[4], Fxb)
        if Fxsb is not None:                  # None: F_s keeps the plain interpolant (F_s(1) = 0, slope free)
            Vg[4], DV[4], _ = self.fdx(Vf[4], Fxsb)
        return Xg, Vg, DX, DXX, DV

    def xss(self, s, Xf, Vf, Fxb, Fxsb):
        m = self.m; I = self.inner; xs = self.xn[I]; ss = np.full(m, s)
        Xg, Vg, DX, DXX, DV = self.derivs(Xf, Vf, Fxb, Fxsb)
        a = []
        for e in range(5):
            a += [Xg[e, I], Vg[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        with np.errstate(all="ignore"):
            rest = _bc(IF.f_rest(ss, xs, self.b, *a), m) + self.rest_extra(s, ss, xs, a, Xg, Vg)
        co = IF.f_coef(ss, xs, self.b, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        return np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T

    fs_mode = "plain"                         # "plain": F_s by its plain interpolant; "flow": F_xs(1) along the flow

    def rhs(self, s, Y):
        m = self.m; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
        Xf, Vf = self.brane_values(s, Xi, Vi); Fxb = self.slope(s, Xf, Vf)
        if self.fs_mode == "plain":
            return np.concatenate([Y[5 * m:], self.xss(s, Xf, Vf, Fxb, None).ravel()])
        X0 = self.xss(s, Xf, Vf, Fxb, 0.0)
        keep = self.lastbr.copy(); d = self.dlt
        Y1 = Y + d * np.concatenate([Y[5 * m:], X0.ravel()])
        Xf1, Vf1 = self.brane_values(s + d, Y1[:5 * m].reshape(5, m), Y1[5 * m:].reshape(5, m))
        Fxsb = (self.slope(s + d, Xf1, Vf1) - Fxb) / d
        self.lastbr = keep
        Xss = self.xss(s, Xf, Vf, Fxb, Fxsb)
        return np.concatenate([Y[5 * m:], Xss.ravel()])

    def cb_args(self, s, Y):
        m = self.m; n = self.Nx + 1
        Xf, Vf = self.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); Fxb = self.slope(s, Xf, Vf)
        Xg, Vg, DX, DXX, DV = self.derivs(Xf, Vf, Fxb, None)
        a = []
        for e in range(5):
            a += [Xg[e], Vg[e], DX[e], np.zeros(n), DXX[e], DV[e]]
        return Xg, Vg, a, Fxb

    def phi_t(self, s, Y):
        """g(xi~, xi~) at every node, xi~ = xi - h, with the brane slope of F from the constraint row"""
        n = self.Nx + 1; Xg, Vg, a, Fxb = self.cb_args(s, Y)
        with np.errstate(all="ignore"):
            xs_, xx_ = [np.asarray(v, dtype=float) * np.ones(n) for v in ID.f_xi(np.full(n, s), self.xn, self.b, 0, 0,
                                                                                    *a)]
        xt = xs_ - self.hs_full(s, Xg, Vg, a)
        gss, gsx, gxx = C.metric_sx(s, self.xn, self.b, Xg)
        return gss * xt ** 2 + 2 * gsx * xt * xx_ + gxx * xx_ ** 2

class DampedCB(CB, ID.Damped):
    def rest_extra(self, s, ss, xs, a, Xg, Vg):
        return _bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a), self.m) if self.kap else 0.0

    def hs_full(self, s, Xg, Vg, a):
        return np.zeros(self.Nx + 1)

    def hs_brane(self, s, Xf, Vf):
        return 0.0

class GaugeCB(CB, IG.Gauge):
    """gauge3's pointwise driver (wF = 0), its damping acting on xi~"""
    def rest_extra(self, s, ss, xs, a, Xg, Vg):
        m = self.m; I = self.inner; R, Rs = self.R(s); out = 0.0
        if self.kap:
            out = out + _bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a), m)
            out = out - _bc(IG.f_damph(ss, xs, self.b, self.kap, self.at, self.mu, self.s1, self.Nst[I], R, *a), m)
        return out + _bc(IG.f_gauge(ss, xs, self.b, self.mu, self.s1, self.wF, self.Nst[I], self.Nst_x[I], R, Rs, *a),
                         m)

    def hs_full(self, s, Xg, Vg, a):
        n = self.Nx + 1; R, Rs = self.R(s)
        with np.errstate(all="ignore"):
            return np.asarray(IG.f_hs(np.full(n, s), self.xn, self.b, self.mu, self.s1, self.wF, self.Nst, self.Nst_x,
                                      R, Rs, *a), dtype=float) * np.ones(n)

    def hs_brane(self, s, Xf, Vf):
        R, Rs = self.R(s)
        if not (R or Rs):
            return 0.0
        with np.errstate(all="ignore"):
            return float(np.asarray(IG.f_hs(s, 1.0, self.b, self.mu, self.s1, self.wF, self.Nst[-1], self.Nst_x[-1],
                                            R, Rs, *self.brane_args(Xf, Vf, 0.0))))

class Gauge5CB(CB, G5.Gauge5):
    """gen_gauge5_fw.py's one-function driver, its damping acting on xi~"""
    def rest_extra(self, s, ss, xs, a, Xg, Vg):
        m = self.m; R, Rs = self.R(s); E, Es = self.E(s, Xg, Vg) if (R or Rs) else (0.0, 0.0); out = 0.0
        if self.kap:
            out = out + _bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a), m)
            out = out - _bc(G5.f_damph(ss, xs, self.b, self.kap, self.at, self.mu, E, R, *a), m)
        return out + _bc(G5.f_gauge(ss, xs, self.b, self.mu, E, Es, R, Rs, *a), m)

    def hs_full(self, s, Xg, Vg, a):
        n = self.Nx + 1; R, Rs = self.R(s); E, Es = self.E(s, Xg, Vg)
        with np.errstate(all="ignore"):
            return np.asarray(G5.f_hs(np.full(n, s), self.xn, self.b, self.mu, E, Es, R, Rs, *a),
                              dtype=float) * np.ones(n)

    def hs_brane(self, s, Xf, Vf):
        R, Rs = self.R(s)
        if not (R or Rs):
            return 0.0
        E, Es = self.E(s, Xf, Vf)
        with np.errstate(all="ignore"):
            return float(np.asarray(G5.f_hs(s, 1.0, self.b, self.mu, E, Es, R, Rs, *self.brane_args(Xf, Vf, 0.0))))

import pickle as _pk, sympy as _sp
_kap, _at, _R, _Rs = _sp.symbols("kap at", real=True) + (_sp.Symbol("R"), _sp.Symbol("R_s"))
_rawh = _pk.load(open("harm_%s.pkl" % C.PROB, "rb"))
_HA = [C.s, C.x, C.bt, _R, _Rs] + C.VARS
fh_gauge = _sp.lambdify(_HA, [C.ev(_rawh["D"][k]) for k in C.ORDER], "numpy", cse=True)
fh_damph = _sp.lambdify([C.s, C.x, C.bt, _kap, _at, _R] + C.VARS, [C.ev(_rawh["DH"][k]) for k in C.ORDER], "numpy",
                        cse=True)
fh_hs = _sp.lambdify(_HA, C.ev(_rawh["aux"]["hs"]), "numpy", cse=True)

class HarmCB(CB, ID.Damped):
    """gen_harm_fw.py's pure harmonic time, h^s = -R(s) Fbar^s, ramped in from s1; damping acting on xi~"""
    def __init__(self, Nx, b, static, kap, at, s1, ramp=0.3):
        super().__init__(Nx, b, static, kap, at); self.s1, self.ramp = s1, ramp

    def R(self, s):
        q = min(max((self.s1 - s) / self.ramp, 0.0), 1.0)
        return 3 * q * q - 2 * q ** 3, -(6 * q - 6 * q * q) / self.ramp

    def rest_extra(self, s, ss, xs, a, Xg, Vg):
        m = self.m; R, Rs = self.R(s); out = 0.0
        if self.kap:
            out = out + _bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a), m)
            if R:
                out = out - _bc(fh_damph(ss, xs, self.b, self.kap, self.at, R, *a), m)
        return out + _bc(fh_gauge(ss, xs, self.b, R, Rs, *a), m) if (R or Rs) else out

    def hs_full(self, s, Xg, Vg, a):
        n = self.Nx + 1; R, Rs = self.R(s)
        with np.errstate(all="ignore"):
            return np.asarray(fh_hs(np.full(n, s), self.xn, self.b, R, Rs, *a), dtype=float) * np.ones(n)

    def hs_brane(self, s, Xf, Vf):
        R, Rs = self.R(s)
        if not (R or Rs):
            return 0.0
        with np.errstate(all="ignore"):
            return float(np.asarray(fh_hs(s, 1.0, self.b, R, Rs, *self.brane_args(Xf, Vf, 0.0))))

def fd_jac(I, f, hrel=1e-7):
    """a forward-difference Jacobian of f(t, y) with a fixed relative step: scipy's own (steps near 1.5e-8) meets the
    brane solve's finite-difference noise and starves Radau's Newton iteration (cb_diag3/4: RK45 takes 5e-3 steps where
    Radau with its own Jacobian takes 1e-5)"""
    def jac(t, y):
        keep = I.lastbr.copy(); f0 = f(t, y); J = np.empty((y.size, y.size))
        for j in range(y.size):
            h = hrel * max(1.0, abs(y[j])); yj = y.copy(); yj[j] += h
            J[:, j] = (f(t, yj) - f0) / h; I.lastbr = keep
        return J
    return jac

class HarmOld(HarmCB):
    """pure harmonic time with the old brane rows (Israel, xi^x = 0, F = 0; F's slope from its plain interpolant):
    item 367 step 1 found the new rows no better, so step 2 runs both"""
    def slope(self, s, Xf, Vf):
        return (self.D @ Xf[4])[self.Nx]
