"""Stage B1: the static exterior in (s, y), Radau nodes excluding the horizon s = 0 and the axis y = 0."""
import numpy as np, sympy as sp, sys, time
import core_sy as C
fres = C.lam(C.RES)
fjac = C.lam([[sp.diff(e, v) for v in C.VARS] for e in C.RES])
fphi = C.lam(C.PHI)

def setup(Ns, Ny):
    sn, yn = C.radau01(Ns), C.radau01(Ny)
    Ds, Dy = C.bary_D(sn), C.bary_D(yn)
    Is, Iy = np.eye(Ns + 1), np.eye(Ny + 1)
    Ds2, Dy2 = np.kron(Ds, Iy), np.kron(Is, Dy)
    S_, Y_ = np.meshgrid(sn, yn, indexing="ij")
    return dict(Ns=Ns, Ny=Ny, sn=sn, yn=yn, Ds=Ds2, Dy=Dy2, Dss=Ds2 @ Ds2, Dyy=Dy2 @ Dy2, Dsy=Ds2 @ Dy2,
                S=S_.ravel(), Y=Y_.ravel())

def dv(G, U):
    n = len(G["S"]); out = []
    for i in range(5):
        u = U[i * n:(i + 1) * n]
        out += [u, G["Ds"] @ u, G["Dy"] @ u, G["Dss"] @ u, G["Dyy"] @ u, G["Dsy"] @ u]
    return out

def residual_and_jac(G, U, want_jac=True):
    n = len(G["S"]); vals = dv(G, U)
    with np.errstate(all="ignore"):
        R = np.array(fres(G["S"], G["Y"], *vals), dtype=float)
    J = None
    if want_jac:
        with np.errstate(all="ignore"):
            Jl = fjac(G["S"], G["Y"], *vals)
        mats = [np.eye(n), G["Ds"], G["Dy"], G["Dss"], G["Dyy"], G["Dsy"]]
        J = np.zeros((5 * n, 5 * n))
        for e in range(5):
            for i in range(5):
                blk = np.zeros((n, n))
                for t in range(6):
                    c = np.broadcast_to(np.asarray(Jl[e][i * 6 + t], dtype=float), (n,))
                    if np.any(c != 0):
                        blk += c[:, None] * mats[t]
                J[e * n:(e + 1) * n, i * n:(i + 1) * n] = blk
    dirn = np.where((np.abs(G["S"] - 1) < 1e-14) | (np.abs(G["Y"] - 1) < 1e-14))[0]
    target = [1, 1, 1, 1, 0]
    for e in range(5):
        R[e, dirn] = U[e * n + dirn] - target[e]
        if want_jac:
            J[e * n + dirn, :] = 0
            J[e * n + dirn, e * n + dirn] = 1
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
    n = len(G["S"]); vals = dv(G, U)
    with np.errstate(all="ignore"):
        p = np.asarray(fphi(G["S"], G["Y"], *vals), dtype=float)
    m = (G["S"] < 1) & (G["Y"] < 1)
    return np.nanmax(np.abs(p[m]))

def regrid(Gf, U, Gt):
    n = len(Gf["S"]); out = []
    for i in range(5):
        Fm = U[i * n:(i + 1) * n].reshape(Gf["Ns"] + 1, Gf["Ny"] + 1)
        a = C.bary_interp(Gf["sn"], Fm, Gt["sn"])                       # (Ns_t+1, Ny_f+1)
        b = C.bary_interp(Gf["yn"], a.T, Gt["yn"]).T
        out.append(b.ravel())
    return np.concatenate(out)

if __name__ == "__main__":
    prev = None
    for N in (8, 12, 16, 20, 24, 28):
        G = setup(N, N); n = len(G["S"])
        U = np.concatenate([np.ones(4 * n), np.zeros(n)]) if prev is None else regrid(prev[0], prev[1], G)
        U, nr = newton(G, U, verbose=prev is None)
        np.save("solsy_N%d.npy" % N, U)
        T0 = C.bary_interp(G["yn"], C.bary_interp(G["sn"], U[:n].reshape(N + 1, N + 1), [0.0])[0], [0.0])[0]
        A0 = C.bary_interp(G["yn"], C.bary_interp(G["sn"], U[2 * n:3 * n].reshape(N + 1, N + 1), [0.0])[0], [0.0])[0]
        TA = C.bary_interp(G["sn"], (U[:n] - U[2 * n:3 * n]).reshape(N + 1, N + 1), [0.0])[0]
        print("N=%d |R|=%.2e phi_max=%.2e  T(0,0)=%.10f A(0,0)=%.10f  max|T-A| on s=0: %.2e"
              % (N, nr, phimax(G, U), T0, A0, np.abs(TA).max()), flush=True)
        prev = (G, U)
