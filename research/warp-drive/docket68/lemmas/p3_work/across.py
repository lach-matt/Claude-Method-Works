"""P3 (a): exterior and interior as one analytic solution in s = r^2 on [-sigma_max, 1] (Figueras-Wiseman chart)."""
import importlib.util, os, sys, time
import numpy as np
import sympy as sp
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from inner import cp2
DT, X, u, th = cp2.DT, cp2.X, cp2.u, cp2.th          # here X is s = r^2
bt, mu, lam = cp2.bt, cp2.mu, cp2.lam
FUNCS, COMPS, JETS = cp2.FUNCS, cp2.COMPS, cp2.DT.JETS


def metric_s(J, ref=False):
    T, A, B, F, S = [sp.Integer(1) if ref else J[n] for n in "TABFS"]
    if ref:
        F = sp.Integer(0)
    f, gx = 1 - X, 2 - u**2
    w = 1 / ((f + bt * (1 - u**2)) / (bt * f))**2
    g = sp.zeros(5)
    g[0, 0] = -w * X * T
    g[1, 1] = w * A / (X * f**4)
    g[2, 2] = w * 4 * B / (f**2 * gx)
    g[1, 2] = g[2, 1] = w * u * F / (2 * f**3)
    g[3, 3] = w * u**2 * gx * S / f**2
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    return g


def system_s():
    J = DT.jetsyms(FUNCS)
    g, gb = metric_s(J), metric_s(J, ref=True)
    E, xi_up, J = DT.operator(g, gb, FUNCS, COMPS, Lam=4)
    gi = DT.inverse(g)
    D = DT.make_D(FUNCS, J)
    src, F2, mx = cp2.maxwell_parts(g, gi, D, J["P_X"], J["P_u"], COMPS)
    # rows scaled to stay finite through s = 0 (each E_ab over a component of the same order in s)
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
    args = [X, u, bt, mu, lam] + [sp.Symbol(f + j) for f in FUNCS for j in JETS]
    lf = lambda e: sp.lambdify(args, sub(e), "numpy", cse=True)
    return dict(inner=[lf(e) for e in inner], brane=[lf(e) for e in rows["brane"]],
                axis=[lf(e) for e in rows["axis"]], xi2=lf(xi2), xi=[lf(xi_up[1]), lf(xi_up[2])])


_C = {}
def C():
    if "c" not in _C:
        _C["c"] = system_s()
    return _C["c"]


class Across:
    def __init__(self, Ns, Nx, smin):
        self.Ns, self.Nx, self.smin = Ns, Nx, smin
        t, Dt = cp2.cheb01(Ns)                       # t = 0 at s = 1 (the far end), t = 1 at smin
        self.s = 1 - (1 - smin) * t
        Ds = -Dt / (1 - smin)
        assert np.min(np.abs(self.s)) > 1e-6, "a node at the horizon"
        self.x, Dx = cp2.cheb01(Nx)
        Is, Ix = np.eye(Ns + 1), np.eye(Nx + 1)
        S, Xx = np.meshgrid(self.s, self.x, indexing="ij")
        self.sg, self.xg = S.ravel(), Xx.ravel()
        self.n = len(self.sg)
        self.D = {"": np.eye(self.n), "_X": np.kron(Ds, Ix), "_u": np.kron(Is, Dx), "_XX": np.kron(Ds @ Ds, Ix),
                  "_Xu": np.kron(Ds, Dx), "_uu": np.kron(Is, Dx @ Dx)}
        # interpolation to s = 0 along each x line, for P's gauge
        self.I0 = np.kron(DT.interp_matrix(self.s, np.array([0.0])), Ix)      # (Nx+1) x n
        e = 1e-12
        far, top = self.sg > 1 - e, self.sg < smin + e
        a0, b1 = self.xg < e, self.xg > 1 - e
        self.mask = {"dir": far, "axis": a0 & ~far, "brane": b1 & ~far, "inner": ~(far | a0 | b1)}
        self.top = np.where(top)[0]
        self.c = C()

    def jets(self, U):
        n = self.n
        return [self.D[j] @ U[m * n:(m + 1) * n] for m in range(6) for j in JETS]

    def residual(self, U, p, jac=True):
        n = self.n
        Jv = self.jets(U)
        Rv = np.zeros(6 * n)
        Jm = np.zeros((6 * n, 6 * n)) if jac else None
        for reg, fl in (("inner", self.c["inner"]), ("axis", self.c["axis"]), ("brane", self.c["brane"])):
            idx = np.where(self.mask[reg])[0]
            a = [self.sg[idx], self.xg[idx], p["bt"], p["mu"], p["lam"]] + [jv[idx] for jv in Jv]
            for k, fk in enumerate(fl):
                Rv[k * n + idx] = np.real(np.broadcast_to(fk(*a), idx.shape))
                if not jac:
                    continue
                for jj in range(36):
                    ac = list(a)
                    ac[5 + jj] = a[5 + jj] + 1e-30j
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
        # P's constant (the gauge): P = 0 on the horizon, in place of P's rows at the interior's last nodes
        it = self.top
        Rv[5 * n + it] = self.I0 @ U[5 * n:6 * n]
        if jac:
            Jm[5 * n + it, :] = 0.0
            Jm[5 * n + it, 5 * n:6 * n] = self.I0
        return Rv, Jm

    def solve(self, U, p, tol=1e-10, maxit=30, quiet=False):
        for k in range(maxit):
            R, Jm = self.residual(U, p)
            r = np.max(np.abs(R))
            if not quiet:
                print("   newton %d |R| %.2e" % (k, r), flush=True)
            if r < tol:
                return U, r, k
            dU = np.linalg.solve(Jm, -R)
            st = 1.0
            while st > 1e-3:
                Rn, _ = self.residual(U + st * dU, p, jac=False)
                if np.max(np.abs(Rn)) < r:
                    break
                st /= 2
            U = U + st * dU
        return U, np.max(np.abs(self.residual(U, p, jac=False)[0])), maxit

    def field(self, U, m):
        return U[m * self.n:(m + 1) * self.n].reshape(self.Ns + 1, self.Nx + 1)


if __name__ == "__main__":
    t0 = time.time(); C(); print("system in s built, %.1f s" % (time.time() - t0))
