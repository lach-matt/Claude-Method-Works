"""P3m (item 462): the magnetic corridor with its field on the plane.  The bulk is vacuum Einstein-DeTurck with
Lambda_5 (R_ab = -4 g_ab, ell = 1); the plane's magnetic field F = (Q/2) sin(th) dth^dph solves Maxwell exactly on any
static spherically symmetric plane, so it enters only through Israel's condition, as a stress kappa / g_OmOm^2
(the same as Reissner-Nordstrom's, electric or magnetic).  Figueras and Wiseman's chart in s = r^2.

Plane rows:
  'ell'  (the static solve, elliptic outside): Israel x3, xi^x = 0, F = 0 (Figueras, Lucietti and Wiseman)
  'evo'  (the interior march): Israel x3, xi^x = 0, xi^s = 0 -- both constraint components, F free; Israel with the
         true unit normal, so a nonzero g_sx on the plane is carried exactly
"""
import os, sys, time
import numpy as np
import sympy as sp
import importlib.util

L = "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas"
_spec = importlib.util.spec_from_file_location("cp2m", os.path.join(L, "corridor_p2.py"))
cp2 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(cp2)
DT = cp2.DT
X, u, th = DT.X, DT.u, DT.th                 # X is s = r^2, u is x
bt, kap = sp.symbols("bt kap", positive=True)
GAM = sp.Symbol("gam")
F5 = ["T", "A", "B", "F", "S"]
REF = ["Tq", "Aq", "Bq", "Fq", "Sq"]
COMPS = cp2.COMPS
JETS = DT.JETS


def metric(T, A, B, F, S):
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


def israel_rows(g, gi, D):
    """K_cd = -n_x Gamma^x_cd for c, d tangent to x = const; n_x = 1/sqrt(g^xx); rows K^c_c - 1 -/+ kap/g33^2"""
    nx = 1 / sp.sqrt(gi[2, 2])
    def Gx(c, d):
        return sum(sp.Rational(1, 2) * gi[2, e] * (D(g[e, d], c) + D(g[e, c], d) - D(g[c, d], e))
                   for e in range(5) if gi[2, e] != 0)
    K00, K11, K33 = -nx * Gx(0, 0), -nx * Gx(1, 1), -nx * Gx(3, 3)
    st = kap / g[3, 3]**2
    return [K00 / g[0, 0] - 1 + st, K11 / g[1, 1] - 1 + st, K33 / g[3, 3] - 1 - st]


F5R = ["T", "A", "B", "F", "G"]          # G = Sigma: S = B + x^2 Sigma, regular on the axis by construction
REFR = ["Tq", "Aq", "Bq", "Fq", "Gq"]


def build(mode="ell", moving_ref=False, damp=False, reg=False):
    f5, rf = (F5R, REFR) if reg else (F5, REF)
    names = f5 + (rf if moving_ref else [])
    J = DT.jetsyms(names)
    if reg:
        Tt, Aa, Bb, Ff, Gg = [J[n] for n in f5]
        g = metric(Tt, Aa, Bb, Ff, Bb + u**2 * Gg)
        if moving_ref:
            Tq, Aq, Bq, Fq, Gq = [J[n] for n in rf]
            gb = metric(Tq, Aq, Bq, Fq, Bq + u**2 * Gq)
        else:
            gb = metric(1, 1, 1, 0, 1)
    else:
        g = metric(*[J[n] for n in f5])
        gb = metric(*[J[n] for n in rf]) if moving_ref else metric(1, 1, 1, 0, 1)
    E, xi_up, J = DT.operator(g, gb, names, COMPS, Lam=4)
    gi = DT.inverse(g)
    D = DT.make_D(names, J)
    if damp:
        # Gundlach et al. constraint damping, + gam [n_(a xi_b) - g_ab n.xi/2], n_a = alpha d_a s (future = decreasing s
        # inside); solutions with xi = 0 are unchanged
        xi_lo = [sum(g[a, b] * xi_up[b] for b in range(5) if g[a, b] != 0) for a in range(5)]
        n_lo = [0, 1 / sp.sqrt(-gi[1, 1]), 0, 0, 0]
        nxi = sum(gi[a, b] * n_lo[a] * xi_lo[b] for a in range(5) for b in range(5) if gi[a, b] != 0 and n_lo[a] != 0)
        for (a, b) in COMPS:
            E[(a, b)] = E[(a, b)] + GAM * ((n_lo[a] * xi_lo[b] + n_lo[b] * xi_lo[a]) / 2 - g[a, b] * nxi / 2)
    inner = [E[(0, 0)] / g[0, 0], E[(1, 1)] / g[1, 1], E[(2, 2)] / g[2, 2],
             E[(1, 2)] * X / sp.sqrt(X * g[1, 1] * g[2, 2]), E[(3, 3)] / g[3, 3]]
    isr = israel_rows(g, gi, D)
    T, A, B, F, S = [J[n] for n in f5]
    if reg:
        S = B + u**2 * S
    gauge = [xi_up[2], F] if mode == "ell" else [xi_up[2], xi_up[1]]
    brane = [isr[0], isr[1], gauge[0], gauge[1], isr[2]]
    axis = [J["T_u"], J["A_u"], J["B_u"], J["F_u"], S - B]
    xi2 = sum(g[a, b] * xi_up[a] * xi_up[b] for a in range(5) for b in range(5) if g[a, b] != 0)
    sub = lambda e: e.subs(th, sp.pi / 3) if hasattr(e, "subs") else e
    args = [X, u, bt, kap] + [sp.Symbol(f + j) for f in names for j in JETS] + [GAM]
    lf = lambda e: sp.lambdify(args, sub(e), "numpy", cse=True)
    return dict(inner=[lf(e) for e in inner], brane=[lf(e) for e in brane], axis=[lf(e) for e in axis],
                xi2=lf(xi2), xis=lf(xi_up[1]), xix=lf(xi_up[2]), nf=len(names))


_C = {}
def C(mode="ell", moving_ref=False, reg=False, damp=False):
    k = (mode, moving_ref, reg, damp)
    if k not in _C:
        t0 = time.time()
        _C[k] = build(mode, moving_ref, damp=damp, reg=reg)
        print("p3m system (%s, moving ref %s) built, %.0f s" % (mode, moving_ref, time.time() - t0), flush=True)
    return _C[k]


def newton(res, U, tol=1e-10, maxit=30, quiet=True):
    r = np.inf
    for k in range(maxit):
        R, Jm = res(U, True)
        r = np.max(np.abs(R))
        if not quiet:
            print("   newton %d |R| %.2e" % (k, r), flush=True)
        if r < tol:
            return U, r, k
        dU = np.linalg.solve(Jm, -R)
        st = 1.0
        while st > 1e-3:
            Rn, _ = res(U + st * dU, False)
            if np.max(np.abs(Rn)) < r:
                break
            st /= 2
        U = U + st * dU
    return U, np.max(np.abs(res(U, False)[0])), maxit


def assemble(c, regs, masks, Dm, n, Jv, p, refjets=None, jac=True):
    nfun = 5
    Rv = np.zeros(nfun * n)
    Jm = np.zeros((nfun * n, nfun * n)) if jac else None
    for reg in regs:
        idx = np.where(masks[reg])[0]
        if len(idx) == 0:
            continue
        a = [p["s"][idx], p["x"][idx], p["bt"], p["kap"]] + [jv[idx] for jv in Jv]
        if refjets is not None:
            a += [rj[idx] for rj in refjets]
        a += [p.get("gam", 0.0)]
        for k, fk in enumerate(c[reg]):
            Rv[k * n + idx] = np.real(np.broadcast_to(fk(*a), idx.shape))
            if not jac:
                continue
            for jj in range(nfun * 6):
                ac = list(a)
                ac[4 + jj] = a[4 + jj] + 1e-30j
                cf = np.broadcast_to(np.imag(fk(*ac)) / 1e-30, idx.shape)
                if np.any(cf):
                    m, j = divmod(jj, 6)
                    Jm[k * n + idx, m * n:(m + 1) * n] += cf[:, None] * Dm[JETS[j]][idx]
    return Rv, Jm


class Global:
    """the static hole on s in [smin, 1], exterior and interior in one solve (Chebyshev in s and x)"""
    def __init__(self, Ns, Nx, smin):
        self.Ns, self.Nx, self.smin = Ns, Nx, smin
        t, Dt = cp2.cheb01(Ns)
        self.s = 1 - (1 - smin) * t
        Ds = -Dt / (1 - smin)
        self.Ds = Ds
        self.x, Dx = cp2.cheb01(Nx)
        Is, Ix = np.eye(Ns + 1), np.eye(Nx + 1)
        S, Xx = np.meshgrid(self.s, self.x, indexing="ij")
        self.sg, self.xg = S.ravel(), Xx.ravel()
        self.n = len(self.sg)
        self.D = {"": np.eye(self.n), "_X": np.kron(Ds, Ix), "_u": np.kron(Is, Dx), "_XX": np.kron(Ds @ Ds, Ix),
                  "_Xu": np.kron(Ds, Dx), "_uu": np.kron(Is, Dx @ Dx)}
        e = 1e-12
        far = self.sg > 1 - e
        a0, b1 = self.xg < e, self.xg > 1 - e
        self.mask = {"dir": far, "axis": a0 & ~far, "brane": b1 & ~far, "inner": ~(far | a0 | b1)}
        self.c = C("ell")

    def jets(self, U):
        n = self.n
        return [self.D[j] @ U[m * n:(m + 1) * n] for m in range(5) for j in JETS]

    def residual(self, U, p, jac=True):
        n = self.n
        q = dict(p, s=self.sg, x=self.xg)
        Rv, Jm = assemble(self.c, ("inner", "axis", "brane"), self.mask, self.D, n, self.jets(U), q, jac=jac)
        idx = np.where(self.mask["dir"])[0]
        for k, v in enumerate([1.0, 1.0, 1.0, 0.0, 1.0]):
            Rv[k * n + idx] = U[k * n + idx] - v
            if jac:
                Jm[k * n + idx, :] = 0.0
                Jm[k * n + idx, k * n + idx] = 1.0
        return Rv, Jm

    def solve(self, U, p, **kw):
        return newton(lambda V, jac: self.residual(V, p, jac), U, **kw)

    def field(self, U, m):
        return U[m * self.n:(m + 1) * self.n].reshape(self.Ns + 1, self.Nx + 1)

    def xi2(self, U, p):
        a = [self.sg, self.xg, p["bt"], p["kap"]] + self.jets(U) + [0.0]
        return np.abs(self.c["xi2"](*a)).reshape(self.Ns + 1, self.Nx + 1)


def even_grid(Np):
    M = 2 * Np - 1
    i = np.arange(M + 1)
    z = np.cos(np.pi * i / M)
    cc = np.hstack([2, np.ones(M - 1), 2]) * (-1) ** i
    Z = np.tile(z, (M + 1, 1)).T
    Dd = np.outer(cc, 1 / cc) / (Z - Z.T + np.eye(M + 1))
    Dd = Dd - np.diag(Dd.sum(axis=1))
    D2 = Dd @ Dd
    pos = np.where(z > 0)[0][::-1]
    mir = np.array([np.argmin(np.abs(z + z[k])) for k in pos])
    return z[pos], Dd[np.ix_(pos, pos)] + Dd[np.ix_(pos, mir)], D2[np.ix_(pos, pos)] + D2[np.ix_(pos, mir)]


class Slab:
    """one interior slab s in [sa, sb] (sa < sb), Cauchy data at sb, fields even in x (no axis node), a moving
    DeTurck reference (the data's Taylor extension), plane rows of the chosen mode"""
    def __init__(self, Ns, Np, sa, sb, U0, U1, ref, mode="evo", reg=False, damp=False):
        self.Ns, self.Np, self.sa, self.sb = Ns, Np, sa, sb
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
        self.mask = {"brane": b1 & ~b0 & ~top, "inner": ~(b0 | b1 | top)}
        self.ib, self.it = np.where(b0)[0], np.where(top)[0]
        self.U0, self.U1 = U0, U1
        self.c = C(mode, moving_ref=True, reg=reg, damp=damp)
        self.refjets = [self.D[j] @ ref[m].ravel() for m in range(5) for j in JETS]

    def jets(self, U):
        n = self.n
        return [self.D[j] @ U[m * n:(m + 1) * n] for m in range(5) for j in JETS]

    def residual(self, U, p, jac=True):
        n = self.n
        q = dict(p, s=self.sg, x=self.xg)
        Rv, Jm = assemble(self.c, ("inner", "brane"), self.mask, self.D, n, self.jets(U), q, self.refjets, jac)
        for k in range(5):
            Rv[k * n + self.ib] = U[k * n + self.ib] - self.U0[k]
            Rv[k * n + self.it] = self.Ks[self.ib] @ U[k * n:(k + 1) * n] - self.U1[k]
            if jac:
                Jm[k * n + self.ib, :] = 0.0
                Jm[k * n + self.ib, k * n + self.ib] = 1.0
                Jm[k * n + self.it, :] = 0.0
                Jm[k * n + self.it, k * n:(k + 1) * n] = self.Ks[self.ib]
        return Rv, Jm

    def solve(self, U, p, **kw):
        return newton(lambda V, jac: self.residual(V, p, jac), U, **kw)

    def field(self, U, m):
        return U[m * self.n:(m + 1) * self.n].reshape(self.Ns + 1, self.Np)

    def at(self, U, s0):
        M = DT.interp_matrix(self.s, np.array([s0]))
        Fs = [self.field(U, m) for m in range(5)]
        return (np.stack([(M @ f)[0] for f in Fs]), np.stack([(M @ (self.Ds @ f))[0] for f in Fs]),
                np.stack([(M @ (self.Ds @ self.Ds @ f))[0] for f in Fs]))

    def xi2(self, U, p):
        a = [self.sg, self.xg, p["bt"], p["kap"]] + self.jets(U) + self.refjets + [p.get("gam", 0.0)]
        return np.abs(self.c["xi2"](*a)).reshape(self.Ns + 1, self.Np)


if __name__ == "__main__":
    for mode in ("ell", "evo"):
        C(mode, False)
