"""the two-horizon chart: q = 1 - s/sm in g_tt and g_ss of the solution and of its reference, so the reference has
Killing horizons at s = 0 and s = sm"""
import numpy as np, sys, time
import sympy as sp
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import cp2, Across, FUNCS, COMPS, JETS, X, u, th, bt, mu, lam
DT = cp2.DT
SM = sp.Symbol("sm")


def metric_q(J, ref=False):
    T, A, B, F, S = [sp.Integer(1) if ref else J[n] for n in "TABFS"]
    if ref:
        F = sp.Integer(0)
    f, gx, q = 1 - X, 2 - u**2, 1 - ((1 - X) / (1 - SM))**3
    w = 1 / ((f + bt * (1 - u**2)) / (bt * f))**2
    g = sp.zeros(5)
    g[0, 0] = -w * X * q * T
    g[1, 1] = w * A / (X * q * f**4)
    g[2, 2] = w * 4 * B / (f**2 * gx)
    g[1, 2] = g[2, 1] = w * u * F / (2 * f**3)
    g[3, 3] = w * u**2 * gx * S / f**2
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    return g


def system_q():
    J = DT.jetsyms(FUNCS)
    g, gb = metric_q(J), metric_q(J, ref=True)
    E, xi_up, J = DT.operator(g, gb, FUNCS, COMPS, Lam=4)
    gi = DT.inverse(g)
    D = DT.make_D(FUNCS, J)
    src, F2, mx = cp2.maxwell_parts(g, gi, D, J["P_X"], J["P_u"], COMPS)
    inner = [(E[(0, 0)] - src[(0, 0)]) / g[0, 0], (E[(1, 1)] - src[(1, 1)]) / g[1, 1],
             (E[(2, 2)] - src[(2, 2)]) / g[2, 2], (E[(1, 2)] - src[(1, 2)]) * X / sp.sqrt(X * g[1, 1] * g[2, 2]),
             (E[(3, 3)] - src[(3, 3)]) / g[3, 3], mx * X]
    T, A, B, F, S, P = [J[n] for n in FUNCS]
    jt = lambda n, d: J[n + d]
    nu_ = 1 / sp.sqrt(g[2, 2])
    K = {k: sp.Rational(1, 2) * nu_ * D(g[k], 2) for k in ((0, 0), (1, 1), (3, 3))}
    E2 = -J["P_X"]**2 / (g[0, 0] * g[1, 1])
    israel = [K[(0, 0)] / g[0, 0] - 1 + lam * E2 / 2, K[(1, 1)] / g[1, 1] - 1 + lam * E2 / 2,
              K[(3, 3)] / g[3, 3] - 1 - lam * E2 / 2]
    sqh = sp.sqrt(-g[0, 0] * g[1, 1]) * g[3, 3]
    div4 = D(sqh * J["P_X"] / (g[1, 1] * g[0, 0]), 1) / sqh
    maxb = J["P_u"] - (lam / 2) * sp.sqrt(g[2, 2]) * g[0, 0] * div4
    rows = dict(brane=[israel[0], israel[1], xi_up[2], F, israel[2], maxb],
                axis=[jt("T", "_u"), jt("A", "_u"), jt("B", "_u"), jt("F", "_u"), S - B, jt("P", "_u")])
    xi2 = sum(g[a, b] * xi_up[a] * xi_up[b] for a in range(5) for b in range(5) if g[a, b] != 0)
    sub = lambda e: e.subs(th, sp.pi / 3) if hasattr(e, "subs") else e
    args = [X, u, bt, mu, lam, SM] + [sp.Symbol(f + j) for f in FUNCS for j in JETS]
    lf = lambda e: sp.lambdify(args, sub(e), "numpy", cse=True)
    return dict(inner=[lf(e) for e in inner], brane=[lf(e) for e in rows["brane"]],
                axis=[lf(e) for e in rows["axis"]], xi2=lf(xi2))


_C = {}
def CQ():
    if "c" not in _C:
        t0 = time.time(); _C["c"] = system_q(); print("two-horizon system built, %.0fs" % (time.time() - t0), flush=True)
    return _C["c"]


class AcrossQ(Across):
    def __init__(self, Ns, Nx, smin, sm):
        Across.__init__(self, Ns, Nx, smin)
        self.c, self.sm = CQ(), sm

    def residual(self, U, p, jac=True):
        n = self.n
        Jv = self.jets(U)
        Rv = np.zeros(6 * n)
        Jm = np.zeros((6 * n, 6 * n)) if jac else None
        for reg, fl in (("inner", self.c["inner"]), ("axis", self.c["axis"]), ("brane", self.c["brane"])):
            idx = np.where(self.mask[reg])[0]
            a = [self.sg[idx], self.xg[idx], p["bt"], p["mu"], p["lam"], self.sm] + [jv[idx] for jv in Jv]
            for k, fk in enumerate(fl):
                Rv[k * n + idx] = np.real(np.broadcast_to(fk(*a), idx.shape))
                if not jac:
                    continue
                for jj in range(36):
                    ac = list(a)
                    ac[6 + jj] = a[6 + jj] + 1e-30j
                    cf = np.broadcast_to(np.imag(fk(*ac)) / 1e-30, idx.shape)
                    if np.any(cf):
                        m, j = divmod(jj, 6)
                        Jm[k * n + idx, m * n:(m + 1) * n] += cf[:, None] * self.D[JETS[j]][idx]
        idx = np.where(self.mask["dir"])[0]
        for k, v in enumerate([1.0, 1.0, 1.0, 0.0, 1.0, p["mu"]]):
            Rv[k * n + idx] = U[k * n + idx] - v
            if jac:
                Jm[k * n + idx, :] = 0.0
                Jm[k * n + idx, k * n + idx] = 1.0
        it = self.top
        Rv[5 * n + it] = self.I0 @ U[5 * n:6 * n]
        if jac:
            Jm[5 * n + it, :] = 0.0
            Jm[5 * n + it, 5 * n:6 * n] = self.I0
        return Rv, Jm

    def xi2(self, U, p):
        a = [self.sg, self.xg, p["bt"], p["mu"], p["lam"], self.sm] + self.jets(U)
        return np.abs(self.c["xi2"](*a)).reshape(self.Ns + 1, self.Nx + 1)
