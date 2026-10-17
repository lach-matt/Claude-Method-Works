"""P3 double-null evolution in the Einstein frame (item 464).  S, A even, r odd (r = 0 on the axis) on chi in [0, 1];
second-order finite differences with ghosts, RK4.  The Misner-Sharp mass m is integrated from the axis on every slice
(m_x = chi^2 Q, Q piecewise linear, integrated exactly against chi^2), so the axis carries no cancelling 1/chi^2 terms.
Plane (chi = 1): Israel, e^-sig A_chi = 1 - q, e^-sig sig_chi = 1 - q, e^-sig (log R)_chi = 1 + q, q = kap/R^4,
sig = S - A/2, R = e^{-A/2} r."""
import os, sys, pickle, numpy as np, sympy as sp
D = pickle.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dneqE.pkl"), "rb"))
SY = D["syms"]
names = [str(s) for s in SY]
RHS = [sp.lambdify(SY, e, "numpy") for e in D["rhs_m"]]
MX = sp.lambdify(SY, D["mx"], "numpy")
MDEF = sp.lambdify(SY, D["mdef"], "numpy")
CU, CV = sp.lambdify(SY, D["Cu"], "numpy"), sp.lambdify(SY, D["Cv"], "numpy")
F = ["S", "A", "r"]


class DNE:
    def __init__(self, N, kap):
        self.N, self.kap, self.h = N, kap, 1.0 / N
        self.chi = np.arange(N + 1) * self.h

    def plane_slopes(self, Y):
        S, A, r, St, At, rt = (y[-1] for y in Y)
        sig = S - A / 2
        R = np.exp(-A / 2) * r
        q = self.kap / R**4
        es = np.exp(sig)
        d = [1.5 * es * (1 - q), es * (1 - q), r * es * (1.5 + q / 2)]
        sgt = St - At / 2
        qt = -4 * q * (rt / r - At / 2)
        dt = [1.5 * es * (sgt * (1 - q) - qt), es * (sgt * (1 - q) - qt),
              rt * es * (1.5 + q / 2) + r * es * (sgt * (1.5 + q / 2) + qt / 2)]
        return d, dt

    def ext(self, v, slope, odd):
        g0 = -v[1] if odd else v[1]
        return np.concatenate([[g0], v, [v[-2] + 2 * self.h * slope]])

    def jets(self, Y):
        d, dt = self.plane_slopes(Y)
        h, J = self.h, {}
        for k, nm in enumerate(F):
            odd = nm == "r"
            e, et = self.ext(Y[k], d[k], odd), self.ext(Y[k + 3], dt[k], odd)
            J[nm], J[nm + "_t"] = Y[k], Y[k + 3]
            J[nm + "_x"] = (e[2:] - e[:-2]) / (2 * h)
            J[nm + "_xx"] = (e[2:] - 2 * e[1:-1] + e[:-2]) / h**2
            J[nm + "_tx"] = (et[2:] - et[:-2]) / (2 * h)
        return J

    def mass(self, J):
        """m on the slice: m_x = chi^2 Q; Q_0 by the axis limit; m/r^3 on the axis by the limit"""
        chi, h = self.chi, self.h
        J = dict(J, chi=chi, m=0 * chi)
        with np.errstate(all="ignore"):
            mx = MX(*[J[n] for n in names])
        Q = np.empty_like(chi)
        Q[1:] = mx[1:] / chi[1:]**2
        rx0, S0, A0, At0 = J["r_x"][0], J["S"][0], J["A"][0], J["A_t"][0]
        Q[0] = 3 / 8 * rx0**2 * (np.exp(-2 * S0) * rx0 * At0**2 - 8 * rx0 * np.exp(-A0))
        a, b = chi[:-1], chi[1:]
        inc = Q[:-1] * (b**3 - a**3) / 3 + (Q[1:] - Q[:-1]) / h * ((b**4 - a**4) / 4 - a * (b**3 - a**3) / 3)
        m = np.concatenate([[0.0], np.cumsum(inc)])
        mr3 = np.empty_like(chi)
        mr3[1:] = m[1:] / J["r"][1:]**3
        mr3[0] = Q[0] / 3 / rx0**3
        return m, mr3

    def rhs(self, Y):
        Y = list(Y)
        Y[2] = Y[2].copy(); Y[2][0] = 0.0
        Y[5] = Y[5].copy(); Y[5][0] = 0.0
        J = self.jets(Y)
        m, mr3 = self.mass(J)
        J["chi"], J["m"] = self.chi, m
        a = [J[n] for n in names]
        with np.errstate(all="ignore"):
            out = [np.asarray(f(*a)) * np.ones(self.N + 1) for f in RHS]
        # axis rows by their limits (m/r^3, A_x r_x / r -> A_xx, r_t / r -> r_tx / r_x)
        S0, A0 = Y[0][0], Y[1][0]
        out[0][0] = J["S_xx"][0] - 0.75 * J["A_t"][0]**2 + 2 * mr3[0] * np.exp(2 * S0)
        out[1][0] = 3 * J["A_xx"][0] - 2 * J["A_t"][0] * J["r_tx"][0] / J["r_x"][0] - 4 * np.exp(2 * S0 - A0)
        out[2][0] = 0.0
        # the m/r^3 rows off the axis use m/r^3 directly (same values; kept explicit for clarity)
        return [Y[3], Y[4], Y[5]] + out

    def step(self, Y, dt):
        k1 = self.rhs(Y)
        k2 = self.rhs([y + dt / 2 * k for y, k in zip(Y, k1)])
        k3 = self.rhs([y + dt / 2 * k for y, k in zip(Y, k2)])
        k4 = self.rhs([y + dt * k for y, k in zip(Y, k3)])
        Yn = [y + dt / 6 * (a + 2 * b + 2 * c + d) for y, a, b, c, d in zip(Y, k1, k2, k3, k4)]
        Yn[2][0] = 0.0; Yn[5][0] = 0.0
        return Yn

    def diag(self, Y):
        J = self.jets(Y)
        m, mr3 = self.mass(J)
        J["chi"], J["m"] = self.chi, m
        a = [J[n] for n in names]
        with np.errstate(all="ignore"):
            md = MDEF(*a)
            cu, cv = CU(*a), CV(*a)
        S, A, r = Y[0], Y[1], Y[2]
        sig = S - A / 2
        R = np.exp(-A / 2) * r
        sl = slice(max(1, self.N // 10), None)          # constraints away from the axis
        e2 = np.exp(2 * S - A)
        return dict(Cu=np.abs(cu[sl] / e2[sl]).max(), Cv=np.abs(cv[sl] / e2[sl]).max(),
                    dm=np.abs((md - m)[sl] / r[sl]**3).max(), ef=J["r_x"][0] * np.exp(-S[0]) - 1,
                    Nax=np.exp(2 * A[0]), Npl=np.exp(2 * A[-1]), Nmin=np.exp(2 * A).min(), Rpl=R[-1],
                    Rmin_off=R[1:].min(), sig_pl=sig[-1], mpl=m[-1], mr3_ax=mr3[0])


if __name__ == "__main__":
    pass
