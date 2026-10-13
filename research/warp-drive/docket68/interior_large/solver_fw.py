"""FW's static RSII large hole in (s, x): Radau in s, Lobatto in x; brane at x = 1."""
import numpy as np, sympy as sp, sys
import core_fw as C
fres = C.lam(C.RES); fjac = C.lam([[sp.diff(e, v) for v in C.VARS] for e in C.RES])
fbc = C.lam(C.BCS); fbcj = C.lam([[sp.diff(e, v) for v in C.VARS] for e in C.BCS])
fphi = C.lam(C.PHI)

def setup(Ns, Nx):
    sn, xn = C.radau01(Ns), C.lobatto01(Nx)
    Ds, Dx = C.bary_D(sn), C.bary_D(xn)
    Is, Ix = np.eye(Ns + 1), np.eye(Nx + 1)
    Ds2, Dx2 = np.kron(Ds, Ix), np.kron(Is, Dx)
    S_, X_ = np.meshgrid(sn, xn, indexing="ij")
    return dict(Ns=Ns, Nx=Nx, sn=sn, xn=xn, Ds=Ds2, Dx=Dx2, Dss=Ds2 @ Ds2, Dxx=Dx2 @ Dx2, Dsx=Ds2 @ Dx2,
                S=S_.ravel(), X=X_.ravel())

def dv(G, U):
    n = len(G["S"]); out = []
    for i in range(5):
        u = U[i * n:(i + 1) * n]
        out += [u, G["Ds"] @ u, G["Dx"] @ u, G["Dss"] @ u, G["Dxx"] @ u, G["Dsx"] @ u]
    return out

def assemble(G, Jl, rows_n):
    n = len(G["S"]); mats = [np.eye(n), G["Ds"], G["Dx"], G["Dss"], G["Dxx"], G["Dsx"]]
    J = np.zeros((rows_n * n, 5 * n))
    for e in range(rows_n):
        for i in range(5):
            blk = np.zeros((n, n))
            for t in range(6):
                c = np.broadcast_to(np.asarray(Jl[e][i * 6 + t], dtype=float), (n,))
                if np.any(c != 0):
                    blk += c[:, None] * mats[t]
            J[e * n:(e + 1) * n, i * n:(i + 1) * n] = blk
    return J

def residual_and_jac(G, U, b, want_jac=True):
    n = len(G["S"]); vals = dv(G, U)
    with np.errstate(all="ignore"):
        R = np.array([np.broadcast_to(np.asarray(r, dtype=float), (n,)) for r in fres(G["S"], G["X"], b, *vals)])
        Rb = np.array([np.broadcast_to(np.asarray(r, dtype=float), (n,)) for r in fbc(G["S"], G["X"], b, *vals)])
    J = Jb = None
    if want_jac:
        with np.errstate(all="ignore"):
            J = assemble(G, fjac(G["S"], G["X"], b, *vals), 5)
            Jb = assemble(G, fbcj(G["S"], G["X"], b, *vals), 4)
    on = lambda m: np.where(m)[0]
    top = on(np.abs(G["S"] - 1) < 1e-14)
    ax = on((np.abs(G["X"]) < 1e-14) & (np.abs(G["S"] - 1) > 1e-14))
    br = on((np.abs(G["X"] - 1) < 1e-14) & (np.abs(G["S"] - 1) > 1e-14))
    fields = [U[i * n:(i + 1) * n] for i in range(5)]
    Id = np.eye(n)
    def setrow(e, idx, val, parts=None, jrows=None):
        R[e, idx] = val
        if want_jac:
            J[e * n + idx, :] = 0
            if parts is not None:
                for fi, M in parts:
                    J[e * n + idx, fi * n:(fi + 1) * n] += M[idx]
            if jrows is not None:
                J[e * n + idx, :] = jrows
    target = [1, 1, 1, 1, 0]
    for e in range(5):
        setrow(e, top, fields[e][top] - target[e], [(e, Id)])
    setrow(1, ax, fields[1][ax] - fields[3][ax], [(1, Id), (3, -Id)])
    for e in (0, 2, 3, 4):
        setrow(e, ax, (G["Dx"] @ fields[e])[ax], [(e, G["Dx"])])
    # brane: T <- K_tt, S <- K_thth, A <- K_ss, B <- xi^x, F <- F = 0
    for e in range(4):
        setrow(e, br, Rb[e, br], jrows=(Jb[e * n + br, :] if want_jac else None))
    setrow(4, br, fields[4][br], [(4, Id)])
    return R.ravel(), J

def newton(G, U, b, tol=1e-10, maxit=60, verbose=False):
    nr = np.inf
    for it in range(maxit):
        R, J = residual_and_jac(G, U, b)
        nr = np.abs(R).max()
        if verbose:
            print("  it %d |R| %.3e" % (it, nr), flush=True)
        if nr < tol or not np.isfinite(nr):
            break
        dU = np.linalg.solve(J, -R); lam = 1.0
        n0 = np.linalg.norm(R)
        while lam > 1e-4:
            Rt = residual_and_jac(G, U + lam * dU, b, False)[0]
            if np.all(np.isfinite(Rt)) and np.linalg.norm(Rt) < n0:
                break
            lam /= 2
        U = U + lam * dU
    return U, nr

def phimax(G, U, b):
    vals = dv(G, U)
    with np.errstate(all="ignore"):
        p = np.asarray(fphi(G["S"], G["X"], b, *vals), dtype=float)
    m = (G["S"] < 1) & (G["X"] > 0)
    return np.nanmax(np.abs(p[m]))

def regrid(Gf, U, Gt):
    n = len(Gf["S"]); out = []
    for i in range(5):
        Fm = U[i * n:(i + 1) * n].reshape(Gf["Ns"] + 1, Gf["Nx"] + 1)
        a = C.bary_interp(Gf["sn"], Fm, Gt["sn"]); out.append(C.bary_interp(Gf["xn"], a.T, Gt["xn"]).T.ravel())
    return np.concatenate(out)

def R4(G, U, b):
    """the horizon's proper radius on the brane: sqrt(g_thth) at (s = 0, x = 1) = bt sqrt(S(0, 1))"""
    n = len(G["S"]); Sm = U[n:2 * n].reshape(G["Ns"] + 1, G["Nx"] + 1)
    return b * np.sqrt(C.bary_interp(G["sn"], Sm, [0.0])[0][-1])

if __name__ == "__main__":
    b = float(sys.argv[1]); Ns, Nx = int(sys.argv[2]), int(sys.argv[3])
    G = setup(Ns, Nx); n = len(G["S"])
    U = np.concatenate([np.ones(4 * n), np.zeros(n)])
    U, nr = newton(G, U, b, verbose=True)
    print("bt=%g Ns=%d Nx=%d |R|=%.2e phi_max=%.2e R4/ell=%.5f" % (b, Ns, Nx, nr, phimax(G, U, b), R4(G, U, b)))
    np.save("fw_bt%g_%d_%d.npy" % (b, Ns, Nx), U)
