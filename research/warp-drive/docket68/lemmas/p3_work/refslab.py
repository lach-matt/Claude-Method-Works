"""interior slabs in the s-chart with a moving DeTurck reference: at each joint the reference is the solution's
second-order Taylor extension in s, so the computed solution stays a solution and the gauge follows the geometry"""
import numpy as np, sys, time
import sympy as sp
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import cp2, metric_s, FUNCS, COMPS, JETS, X, u, th, bt, mu, lam
DT = cp2.DT
REF = ["Tq", "Aq", "Bq", "Fq", "Sq"]


def metric_ref(J):
    T, A, B, F, S = [J[n] for n in REF]
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


GAM = sp.Symbol("gam")


def system_ref(damp=True):
    J = DT.jetsyms(FUNCS + REF)
    g, gb = metric_s(J), metric_ref(J)
    E, xi_up, J = DT.operator(g, gb, FUNCS + REF, COMPS, Lam=4)
    gi = DT.inverse(g)
    # constraint damping (Gundlach et al.): + gam [n_(a xi_b) - g_ab n.xi / 2], n the future unit normal to s = const,
    # future being decreasing s inside; solutions with xi = 0 are unchanged
    xi_lo = [sum(g[a, b] * xi_up[b] for b in range(5) if g[a, b] != 0) for a in range(5)]
    n_lo = [0, 1 / sp.sqrt(-gi[1, 1]), 0, 0, 0]
    nxi = sum(gi[a, b] * n_lo[a] * xi_lo[b] for a in range(5) for b in range(5) if gi[a, b] != 0 and n_lo[a] != 0)
    for (a, b) in COMPS:
        if damp:
            E[(a, b)] = E[(a, b)] + GAM * ((n_lo[a] * xi_lo[b] + n_lo[b] * xi_lo[a]) / 2 - g[a, b] * nxi / 2)
    D = DT.make_D(FUNCS + REF, J)
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
    args = ([X, u, bt, mu, lam] + [sp.Symbol(f + j) for f in FUNCS for j in JETS]
            + [sp.Symbol(f + j) for f in REF for j in JETS] + [GAM])
    lf = lambda e: sp.lambdify(args, sub(e), "numpy", cse=True)
    return dict(inner=[lf(e) for e in inner], brane=[lf(e) for e in rows["brane"]],
                axis=[lf(e) for e in rows["axis"]], xi2=lf(xi2))


_C = {}
def CR(damp=True):
    if damp not in _C:
        t0 = time.time()
        _C[damp] = system_ref(damp)
        print("reference system built (damping %s), %.0fs" % (damp, time.time() - t0), flush=True)
    return _C[damp]


class RefSlab:
    def __init__(self, Ns, Nx, sa, sb, Ub, dUb, ref):
        """ref: (5, Ns+1, Nx+1) reference fields T, A, B, F, S on this slab's grid"""
        self.Ns, self.Nx, self.sa, self.sb = Ns, Nx, sa, sb
        t, Dt = cp2.cheb01(Ns)
        self.s = sb - (sb - sa) * t
        self.Ds = -Dt / (sb - sa)
        self.x, Dx = cp2.cheb01(Nx)
        Is, Ix = np.eye(Ns + 1), np.eye(Nx + 1)
        S, Xx = np.meshgrid(self.s, self.x, indexing="ij")
        self.sg, self.xg = S.ravel(), Xx.ravel()
        self.n = len(self.sg)
        self.Ks = np.kron(self.Ds, Ix)
        self.D = {"": np.eye(self.n), "_X": self.Ks, "_u": np.kron(Is, Dx), "_XX": np.kron(self.Ds @ self.Ds, Ix),
                  "_Xu": np.kron(self.Ds, Dx), "_uu": np.kron(Is, Dx @ Dx)}
        e = 1e-12
        b0, top = np.abs(self.sg - sb) < 1e-11, np.abs(self.sg - sa) < 1e-11
        a0, b1 = self.xg < e, self.xg > 1 - e
        self.mask = {"axis": a0 & ~b0 & ~top, "brane": b1 & ~b0 & ~top, "inner": ~(b0 | a0 | b1 | top)}
        self.ib, self.it = np.where(b0)[0], np.where(top)[0]
        self.Ub, self.dUb = Ub, dUb
        self.c = CR()
        self.refjets = [self.D[j] @ ref[m].ravel() for m in range(5) for j in JETS]

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
            if len(idx) == 0:
                continue
            a = ([self.sg[idx], self.xg[idx], p["bt"], p["mu"], p["lam"]] + [jv[idx] for jv in Jv]
                 + [rj[idx] for rj in self.refjets] + [p.get("gam", 0.0)])
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

    def at(self, U, s0):
        """values, first and second s-derivatives of all six fields at s0"""
        M = DT.interp_matrix(self.s, np.array([s0]))
        F = [self.field(U, m) for m in range(6)]
        return (np.stack([(M @ f)[0] for f in F]), np.stack([(M @ (self.Ds @ f))[0] for f in F]),
                np.stack([(M @ (self.Ds @ self.Ds @ f))[0] for f in F]))

    def xi2(self, U, p):
        a = [self.sg, self.xg, p["bt"], p["mu"], p["lam"]] + self.jets(U) + self.refjets + [p.get("gam", 0.0)]
        return np.abs(self.c["xi2"](*a)).reshape(self.Ns + 1, self.Nx + 1)


if __name__ == "__main__":
    CR()


def even_grid(Np):
    """Np positive nodes of the Gauss-Lobatto grid of degree 2 Np - 1 on [-1, 1] (no node at 0), with first and
    second differentiation matrices for even functions; x ascending, x[-1] = 1"""
    M = 2 * Np - 1
    i = np.arange(M + 1)
    z = np.cos(np.pi * i / M)
    c = np.hstack([2, np.ones(M - 1), 2]) * (-1) ** i
    Z = np.tile(z, (M + 1, 1)).T
    D = np.outer(c, 1 / c) / (Z - Z.T + np.eye(M + 1))
    D = D - np.diag(D.sum(axis=1))
    D2 = D @ D
    pos = np.where(z > 0)[0][::-1]                     # ascending x
    mir = np.array([np.argmin(np.abs(z + z[k])) for k in pos])
    De = D[np.ix_(pos, pos)] + D[np.ix_(pos, mir)]
    D2e = D2[np.ix_(pos, pos)] + D2[np.ix_(pos, mir)]
    return z[pos], De, D2e


class EvenRefSlab(RefSlab):
    """RefSlab with every field even in x: no axis node and no axis rows"""
    def __init__(self, Ns, Np, sa, sb, Ub, dUb, ref):
        self.Ns, self.Nx, self.sa, self.sb = Ns, Np - 1, sa, sb
        t, Dt = cp2.cheb01(Ns)
        self.s = sb - (sb - sa) * t
        self.Ds = -Dt / (sb - sa)
        self.x, Dx, Dxx = even_grid(Np)
        Is, Ix = np.eye(Ns + 1), np.eye(Np)
        S, Xx = np.meshgrid(self.s, self.x, indexing="ij")
        self.sg, self.xg = S.ravel(), Xx.ravel()
        self.n = len(self.sg)
        self.Ks = np.kron(self.Ds, Ix)
        self.D = {"": np.eye(self.n), "_X": self.Ks, "_u": np.kron(Is, Dx), "_XX": np.kron(self.Ds @ self.Ds, Ix),
                  "_Xu": np.kron(self.Ds, Dx), "_uu": np.kron(Is, Dxx)}
        b0, top = np.abs(self.sg - sb) < 1e-11, np.abs(self.sg - sa) < 1e-11
        b1 = self.xg > 1 - 1e-12
        self.mask = {"axis": np.zeros(self.n, bool), "brane": b1 & ~b0 & ~top, "inner": ~(b0 | b1 | top)}
        self.ib, self.it = np.where(b0)[0], np.where(top)[0]
        self.Ub, self.dUb = Ub, dUb
        self.c = CR()
        self.refjets = [self.D[j] @ ref[m].ravel() for m in range(5) for j in JETS]
