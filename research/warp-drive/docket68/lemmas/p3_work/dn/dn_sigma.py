"""P3 double-null evolution (item 464): sig, A, psi on chi in [0, 1] (axis, plane), second-order finite differences
with ghost points, RK4 in tau.  Axis: sig, A even, psi even with psi(0) = 0 (elementary flatness), RHS there by the
chi -> 0 limits.  Plane (chi = 1): Israel, e^-sig A_chi = e^-sig sig_chi = 1 - kap/R^4, e^-sig (log R)_chi = 1 + kap/R^4."""
import sys, pickle, numpy as np, sympy as sp
D = pickle.load(open(__import__("os").path.join(__import__("os").path.dirname(__file__) or ".", "dn_sigma_eq.pkl"), "rb"))
SY = D["syms"]
RHS = [sp.lambdify(SY, r, "numpy") for r in D["rhs"]]
RHS0 = [sp.lambdify(SY, r, "numpy") for r in D["rhs0"]]
CU, CV = sp.lambdify(SY, D["Cu"], "numpy"), sp.lambdify(SY, D["Cv"], "numpy")
KR = sp.lambdify(SY, D["K"], "numpy")
NM = ["sig", "A", "psi"]


class DN:
    def __init__(self, N, kap):
        self.N, self.kap, self.h = N, kap, 1.0 / N
        self.chi = np.arange(N + 1) * self.h

    def plane_slopes(self, f):
        """Israel's Neumann values at chi = 1 for (sig, A, psi) and their tau-derivatives"""
        s, p, st, pt = f[0][-1], f[2][-1], f[3][-1], f[5][-1]
        q = self.kap * np.exp(-4 * (s + p))
        es = np.exp(s)
        d = [es * (1 - q), es * (1 - q), 2 * es * q - 1]
        dq = -4 * q * (st + pt)
        dt = [es * st * (1 - q) - es * dq, es * st * (1 - q) - es * dq, 2 * es * (st * q + dq)]
        return d, dt

    def ext(self, v, slope):
        """ghosts: even at the axis, Neumann at the plane"""
        return np.concatenate([[v[1]], v, [v[-2] + 2 * self.h * slope]])

    def jets(self, Y):
        d, dt = self.plane_slopes(Y)
        h, J = self.h, {}
        for m, nm in enumerate(NM):
            e = self.ext(Y[m], d[m])
            et = self.ext(Y[m + 3], dt[m])
            J[nm] = Y[m]
            J[nm + "_t"] = Y[m + 3]
            J[nm + "_x"] = (e[2:] - e[:-2]) / (2 * h)
            J[nm + "_xx"] = (e[2:] - 2 * e[1:-1] + e[:-2]) / h**2
            J[nm + "_tx"] = (et[2:] - et[:-2]) / (2 * h)
        return J

    def args(self, J, sl=slice(None)):
        chi = self.chi[sl]
        return [chi] + [J[str(s)][sl] for s in SY[1:]]

    def rhs(self, Y):
        Y = list(Y)
        Y[2] = Y[2].copy(); Y[2][0] = 0.0
        Y[5] = Y[5].copy(); Y[5][0] = 0.0
        J = self.jets(Y)
        a1 = self.args(J, slice(1, None))
        a0 = [np.array([0.0])] + [J[str(s)][:1] for s in SY[1:]]
        out = []
        for m in range(3):
            r = np.empty(self.N + 1)
            r[1:] = RHS[m](*a1)
            r[0] = RHS0[m](*a0)[0] if m < 2 else 0.0
            out.append(r)
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
        a1 = self.args(J, slice(1, None))
        with np.errstate(all="ignore"):
            cu, cv = CU(*a1), CV(*a1)
            K = KR(*a1)
        e2s = np.exp(2 * Y[0][1:])
        R = self.chi * np.exp(Y[0] + Y[2])
        ax = RHS0[2](*([np.array([0.0])] + [J[str(s)][:1] for s in SY[1:]]))[0]    # psi_tt on the axis: 0 if consistent
        return dict(Cu=np.abs(cu / e2s).max(), Cv=np.abs(cv / e2s).max(), Cu_l2=np.sqrt(np.mean((cu / e2s)**2)),
                    Cv_l2=np.sqrt(np.mean((cv / e2s)**2)), Kmax=np.abs(K).max(), Kplane=K[-1], Kaxis1=K[0],
                    Nax=np.exp(2 * Y[1][0]), Npl=np.exp(2 * Y[1][-1]), Rpl=R[-1], sig_ax=Y[0][0], sig_pl=Y[0][-1],
                    axis_c=ax, Nmin=np.exp(2 * Y[1]).min(), Rmax=R.max())


def initial(fn, s0, N, kap, Ns):
    import dninit
    U = np.load(fn)
    chi, d, chk = dninit.conformal(U, s0, N, kap, Ns=Ns)
    return [d["sig"], d["A"], d["psi"], d["sig_t"], d["A_t"], d["psi_t"]], chk


def run(fn, s0, N, kap, Ns, tmax, cfl=0.25, every=None, quiet=False, stop=None):
    Y, chk = initial(fn, s0, N, kap, Ns)
    ev = DN(N, kap)
    dt = cfl * ev.h
    nst = int(round(tmax / dt))
    every = every or max(1, nst // 20)
    hist = []
    for n in range(nst + 1):
        if n % every == 0 or n == nst:
            dg = ev.diag(Y); dg["tau"] = n * dt
            hist.append(dg)
            if not quiet:
                print("tau %.4f  Cuu %.1e Cvv %.1e (L2 %.1e %.1e) | N axis %.3e plane %.3e min %.3e | R plane %.4f | "
                      "Kmax %.3e K plane %.3e | axis cons %.1e" % (
                          dg["tau"], dg["Cu"], dg["Cv"], dg["Cu_l2"], dg["Cv_l2"], dg["Nax"], dg["Npl"], dg["Nmin"],
                          dg["Rpl"], dg["Kmax"], dg["Kplane"], dg["axis_c"]), flush=True)
            if not np.isfinite(dg["Kmax"]) or (stop and stop(dg)):
                break
        if n < nst:
            Y = ev.step(Y, dt)
    return Y, hist, chk


if __name__ == "__main__":
    fn, s0, kap, Ns, N, tmax = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    Y, hist, chk = run(fn, s0, N, kap, Ns, tmax)
    np.save(sys.argv[7] if len(sys.argv) > 7 else "dn_out.npy", np.array(Y))
    pickle.dump(hist, open((sys.argv[7] if len(sys.argv) > 7 else "dn_out") + ".hist", "wb"))
