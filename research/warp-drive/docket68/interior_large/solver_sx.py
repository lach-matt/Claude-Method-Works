"""Stage B1': the static exterior in (s, x): Radau in s (the horizon s = 0 excluded), Lobatto in x with stage A's axis
conditions (d_x X = 0, S = B at x = 0), Dirichlet at s = 1 and x = 1."""
import numpy as np, sympy as sp, sys
import core_sx as C
fres = C.lam(C.RES)
fjac = C.lam([[sp.diff(e, v) for v in C.VARS] for e in C.RES])
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

def residual_and_jac(G, U, want_jac=True):
    n = len(G["S"]); vals = dv(G, U)
    with np.errstate(all="ignore"):
        R = np.array(fres(G["S"], G["X"], *vals), dtype=float)
    J = None
    if want_jac:
        with np.errstate(all="ignore"):
            Jl = fjac(G["S"], G["X"], *vals)
        mats = [np.eye(n), G["Ds"], G["Dx"], G["Dss"], G["Dxx"], G["Dsx"]]
        J = np.zeros((5 * n, 5 * n))
        for e in range(5):
            for i in range(5):
                blk = np.zeros((n, n))
                for t in range(6):
                    c = np.broadcast_to(np.asarray(Jl[e][i * 6 + t], dtype=float), (n,))
                    if np.any(c != 0):
                        blk += c[:, None] * mats[t]
                J[e * n:(e + 1) * n, i * n:(i + 1) * n] = blk
    Id = np.eye(n)
    def setrow(e, idx, val, parts):
        R[e, idx] = val
        if want_jac:
            J[e * n + idx, :] = 0
            for fi, M in parts:
                J[e * n + idx, fi * n:(fi + 1) * n] += M[idx]
    on = lambda m: np.where(m)[0]
    dirn = on((np.abs(G["S"] - 1) < 1e-14) | (np.abs(G["X"] - 1) < 1e-14))
    ax = on((np.abs(G["X"]) < 1e-14) & (np.abs(G["S"] - 1) > 1e-14))
    fields = [U[i * n:(i + 1) * n] for i in range(5)]
    target = [1, 1, 1, 1, 0]
    for e in range(5):
        setrow(e, dirn, fields[e][dirn] - target[e], [(e, Id)])
    setrow(1, ax, fields[1][ax] - fields[3][ax], [(1, Id), (3, -Id)])         # S = B on the axis
    for e in (0, 2, 3, 4):
        setrow(e, ax, (G["Dx"] @ fields[e])[ax], [(e, G["Dx"])])
    return R.ravel(), J

def newton(G, U, tol=1e-10, maxit=40, verbose=False):
    for it in range(maxit):
        R, J = residual_and_jac(G, U)
        nr = np.abs(R).max()
        if verbose:
            print("  it %d |R| %.3e" % (it, nr), flush=True)
        if nr < tol:
            break
        dU = np.linalg.solve(J, -R); lam = 1.0
        while lam > 1e-4:
            if np.linalg.norm(residual_and_jac(G, U + lam * dU, False)[0]) < np.linalg.norm(R):
                break
            lam /= 2
        U = U + lam * dU
    return U, nr

def phimax(G, U):
    vals = dv(G, U)
    with np.errstate(all="ignore"):
        p = np.asarray(fphi(G["S"], G["X"], *vals), dtype=float)
    m = (G["S"] < 1) & (G["X"] < 1) & (G["X"] > 0)
    return np.nanmax(np.abs(p[m]))

def regrid(Gf, U, Gt):
    n = len(Gf["S"]); out = []
    for i in range(5):
        Fm = U[i * n:(i + 1) * n].reshape(Gf["Ns"] + 1, Gf["Nx"] + 1)
        a = C.bary_interp(Gf["sn"], Fm, Gt["sn"])
        b = C.bary_interp(Gf["xn"], a.T, Gt["xn"]).T
        out.append(b.ravel())
    return np.concatenate(out)

def from_rx(Nrx, Gt):
    """initial guess from the stage A (r, x) solution, sampled at r = sqrt(s)"""
    import solver as SA, run_conv as RC
    from numpy.polynomial import chebyshev as Ch
    GA = SA.setup(Nrx); UA = np.load("sol_N%d.npy" % Nrx); nA = len(GA["R"]); yA = GA["y"]
    V = Ch.chebvander(2 * yA - 1, Nrx); out = []
    for i in range(5):
        Fm = UA[i * nA:(i + 1) * nA].reshape(Nrx + 1, Nrx + 1)
        cf = np.linalg.solve(V, np.linalg.solve(V, Fm).T).T
        Vr = Ch.chebvander(2 * np.sqrt(Gt["sn"]) - 1, Nrx); Vx = Ch.chebvander(2 * Gt["xn"] - 1, Nrx)
        out.append((Vr @ cf @ Vx.T).ravel())
    return np.concatenate(out)

if __name__ == "__main__":
    Ns = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    for Nx in (20, 24, 28, 32):
        G = setup(Ns, Nx); n = len(G["S"])
        U, nr = newton(G, from_rx(32, G))
        np.save("solsx_%d_%d.npy" % (Ns, Nx), U)
        T00 = C.bary_interp(G["sn"], U[:n].reshape(Ns + 1, Nx + 1), [0.0])[0][0]
        TA = np.abs(C.bary_interp(G["sn"], (U[:n] - U[2 * n:3 * n]).reshape(Ns + 1, Nx + 1), [0.0])[0]).max()
        print("Ns=%d Nx=%d |R|=%.1e phi_max=%.2e T(0,0)=%.10f max|T-A|(s=0)=%.1e" % (Ns, Nx, nr, phimax(G, U), T00, TA),
              flush=True)
