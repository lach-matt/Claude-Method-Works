"""P3 (a): the interior as a space-time spectral initial-value problem in sigma = rho^2, data U0 on the horizon."""
import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from inner import cp2, system_in, FUNCS
DT = cp2.DT
JETS = DT.JETS                                   # "", _X, _u, _XX, _Xu, _uu  (X = rho)
_C = {}


def C():
    if "c" not in _C:
        _C["c"] = system_in()
    return _C["c"]


class InSolver:
    def __init__(self, Ns, Nx, s0, s1, bottom):
        """sigma in [s0, s1]; bottom = ('values', U0) on sigma = 0, or ('cauchy', U, U_sigma) at s0 > 0"""
        self.Ns, self.Nx, self.s0, self.s1 = Ns, Nx, s0, s1
        t, Dt = cp2.cheb01(Ns)
        self.s = s0 + (s1 - s0) * t
        Ds = Dt / (s1 - s0)
        self.x, Dx = cp2.cheb01(Nx)
        Is, Ix = np.eye(Ns + 1), np.eye(Nx + 1)
        S, Xx = np.meshgrid(self.s, self.x, indexing="ij")
        self.sg, self.xg = S.ravel(), Xx.ravel()
        self.rg = np.sqrt(self.sg)
        self.n = len(self.sg)
        Ks, Kss = np.kron(Ds, Ix), np.kron(Ds @ Ds, Ix)
        self.Ks = Ks
        self.D = {"": np.eye(self.n), "_X": (2 * self.rg)[:, None] * Ks, "_u": np.kron(Is, Dx),
                  "_XX": 2 * Ks + (4 * self.sg)[:, None] * Kss, "_Xu": (2 * self.rg)[:, None] * np.kron(Ds, Dx),
                  "_uu": np.kron(Is, Dx @ Dx)}
        e = 1e-12
        b0 = self.sg < s0 + e * max(1, s1)
        a0, b1 = self.xg < e, self.xg > 1 - e
        self.bottom = bottom
        if bottom[0] == "values":
            self.mask = {"bot": b0, "axis": a0 & ~b0, "brane": b1 & ~b0, "inner": ~(b0 | a0 | b1)}
        else:   # value at s0, sigma-derivative at s0 in place of the equations at the top nodes
            top = self.sg > s1 - e * max(1, s1)
            self.mask = {"bot": b0, "dsig": top, "axis": a0 & ~b0 & ~top, "brane": b1 & ~b0 & ~top,
                         "inner": ~(b0 | a0 | b1 | top)}
        self.c = C()

    def jets(self, U):
        n = self.n
        return [self.D[j] @ U[m * n:(m + 1) * n] for m in range(6) for j in JETS]

    def residual(self, U, p, jac=True):
        n = self.n
        Jv = self.jets(U)
        Rv = np.zeros(6 * n)
        Jm = np.zeros((6 * n, 6 * n)) if jac else None
        funs = dict(inner=self.c["inner"], axis=self.c["axis"], brane=self.c["brane"])
        for reg, fl in funs.items():
            idx = np.where(self.mask[reg])[0]
            if len(idx) == 0:
                continue
            a = [self.rg[idx], self.xg[idx], p["bt"], p["mu"], p["lam"]] + [jv[idx] for jv in Jv]
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
        idx = np.where(self.mask["bot"])[0]
        if self.bottom[0] == "values":
            # the horizon's free data (Fuchsian, read in Euclidean polar form): T, B, F, S there, and the sigma-
            # coefficients of T - A (an m = 2 component) and of P (A_t, m = 1); A = T and P = 0 the equations force
            U0, dTA, dP = self.bottom[1], self.bottom[2], self.bottom[3]
            for k in (0, 2, 3, 4):
                Rv[k * n + idx] = U[k * n + idx] - U0[k]
                if jac:
                    Jm[k * n + idx, :] = 0.0
                    Jm[k * n + idx, k * n + idx] = 1.0
            KT, KA, KP = (self.Ks[idx] @ U[m * n:(m + 1) * n] for m in (0, 1, 5))
            Rv[1 * n + idx] = (KT - KA) - dTA
            Rv[5 * n + idx] = U[5 * n + idx]                 # P = 0 on the horizon (the gauge's constant)
            if jac:
                Jm[1 * n + idx, :] = 0.0
                Jm[1 * n + idx, 0:n] = self.Ks[idx]
                Jm[1 * n + idx, n:2 * n] = -self.Ks[idx]
                Jm[5 * n + idx, :] = 0.0
                Jm[5 * n + idx, 5 * n + idx] = 1.0
            # P's sigma^1 branch is regular too (A_t = c0 + c1 rho^2): its coefficient replaces P's rows at the top
            it = np.where(self.sg > self.s1 - 1e-12 * max(1, self.s1))[0]
            Rv[5 * n + it] = KP - dP
            if jac:
                Jm[5 * n + it, :] = 0.0
                Jm[5 * n + it, 5 * n:6 * n] = self.Ks[idx]
        else:
            for k in range(6):
                Rv[k * n + idx] = U[k * n + idx] - self.bottom[1][k]
                if jac:
                    Jm[k * n + idx, :] = 0.0
                    Jm[k * n + idx, k * n + idx] = 1.0
        if "dsig" in self.mask:
            it = np.where(self.mask["dsig"])[0]            # one row per x at the top: carry the derivative condition
            ib = np.where(self.mask["bot"])[0]
            for k in range(6):
                d = self.Ks[ib] @ U[k * n:(k + 1) * n]
                Rv[k * n + it] = d - self.bottom[2][k]
                if jac:
                    Jm[k * n + it, :] = 0.0
                    Jm[k * n + it, k * n:(k + 1) * n] = self.Ks[ib]
        return Rv, Jm

    def solve(self, U, p, tol=1e-10, maxit=30, quiet=False):
        for it in range(maxit):
            R, Jm = self.residual(U, p)
            r = np.max(np.abs(R))
            if not quiet:
                print("   newton %d |R| %.2e" % (it, r), flush=True)
            if r < tol:
                return U, r, it
            dU = np.linalg.solve(Jm, -R)
            lam_ = 1.0
            while lam_ > 1e-3:
                Rn, _ = self.residual(U + lam_ * dU, p, jac=False)
                if np.max(np.abs(Rn)) < r:
                    break
                lam_ /= 2
            U = U + lam_ * dU
        return U, np.max(np.abs(self.residual(U, p, jac=False)[0])), maxit

    def field(self, U, m):
        return U[m * self.n:(m + 1) * self.n].reshape(self.Ns + 1, self.Nx + 1)
