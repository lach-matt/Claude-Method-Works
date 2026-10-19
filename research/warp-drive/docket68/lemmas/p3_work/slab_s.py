"""interior-only Cauchy slabs in the s-chart of across.py: data (U, U_s) at s = sb, solve down to sa < sb"""
import numpy as np, sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import C, cp2, JETS
DT = cp2.DT


class SlabS:
    def __init__(self, Ns, Nx, sa, sb, Ub, dUb):
        self.Ns, self.Nx, self.sa, self.sb = Ns, Nx, sa, sb
        t, Dt = cp2.cheb01(Ns)                 # t = 0 at sb (data), t = 1 at sa
        self.s = sb - (sb - sa) * t
        Ds = -Dt / (sb - sa)
        self.Ds = Ds
        self.x, Dx = cp2.cheb01(Nx)
        Is, Ix = np.eye(Ns + 1), np.eye(Nx + 1)
        S, Xx = np.meshgrid(self.s, self.x, indexing="ij")
        self.sg, self.xg = S.ravel(), Xx.ravel()
        self.n = len(self.sg)
        self.Ks = np.kron(Ds, Ix)
        self.D = {"": np.eye(self.n), "_X": self.Ks, "_u": np.kron(Is, Dx), "_XX": np.kron(Ds @ Ds, Ix),
                  "_Xu": np.kron(Ds, Dx), "_uu": np.kron(Is, Dx @ Dx)}
        e = 1e-12
        b0 = np.abs(self.sg - sb) < e * 10
        top = np.abs(self.sg - sa) < e * 10
        a0, b1 = self.xg < e, self.xg > 1 - e
        self.mask = {"axis": a0 & ~b0 & ~top, "brane": b1 & ~b0 & ~top, "inner": ~(b0 | a0 | b1 | top)}
        self.ib, self.it = np.where(b0)[0], np.where(top)[0]
        self.Ub, self.dUb = Ub, dUb
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
        for k in range(6):
            Rv[k * n + self.ib] = U[k * n + self.ib] - self.Ub[k]
            Rv[k * n + self.it] = self.Ks[self.ib] @ U[k * n:(k + 1) * n] - self.dUb[k]
            if jac:
                Jm[k * n + self.ib, :] = 0.0
                Jm[k * n + self.ib, k * n + self.ib] = 1.0
                Jm[k * n + self.it, :] = 0.0
                Jm[k * n + self.it, k * n:(k + 1) * n] = self.Ks[self.ib]
        return Rv, Jm

    def solve(self, U, p, tol=1e-9, maxit=15):
        r = np.inf
        for k in range(maxit):
            R, Jm = self.residual(U, p)
            r = np.max(np.abs(R))
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

    def edge(self, U, at=None):
        """values and s-derivatives at s = at (default sa), for the next slab"""
        F = [self.field(U, m) for m in range(6)]
        if at is None:
            return np.stack([f[-1] for f in F]), np.stack([(self.Ds @ f)[-1] for f in F])
        M = DT.interp_matrix(self.s, np.array([at]))
        return np.stack([(M @ f)[0] for f in F]), np.stack([(M @ (self.Ds @ f))[0] for f in F])
