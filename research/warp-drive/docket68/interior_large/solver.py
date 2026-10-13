"""Stage A: FLW's static AdS5-CFT4 solution with Schwarzschild boundary (1104.4489 (4.6)), ell = R0 = 1, by Newton."""
import pickle, numpy as np, sympy as sp, time, sys
names = ["T", "S", "A", "B", "F"]
tags = ["", "_r", "_x", "_rr", "_xx", "_rx"]
r, x = sp.symbols("r x", real=True)
th = sp.Symbol("theta", real=True)
raw = pickle.load(open("eqs.pkl", "rb"))
ns = {**{n + t: sp.Symbol(n + t) for n in names for t in tags}, "r": r, "x": x}
E = {k: sp.sympify(eval(v, {**sp.__dict__})) for k, v in raw.items()}
for k, e in E.items():
    assert not e.atoms(sp.Derivative), k
    assert th not in e.free_symbols, k
f = 1 - r**2; g = 2 - x**2; z = (1 - x**2) / f
Ts, Ss, As, Bs, Fs = [ns[n] for n in names]
Gtt = r**2 * Ts / z**2; Grr = 4 * As / f**4 / z**2; Gxx = 4 * Bs / (f**2 * g) / z**2; Gth = x**2 * g * Ss / f**2 / z**2
res = [E["tt"] / Gtt, E["thth"] / Gth, E["rr"] / Grr, E["xx"] / Gxx, E["rx"] / sp.sqrt(Grr * Gxx)]
vars_ = [ns[n + t] for n in names for t in tags]
t0 = time.time()
fres = sp.lambdify([r, x] + vars_, res, "numpy", cse=True)
fjac = sp.lambdify([r, x] + vars_, [[sp.diff(e, v) for v in vars_] for e in res], "numpy", cse=True)
print("lambdified", time.time() - t0, flush=True)

def cheb(N):
    """Chebyshev-Gauss-Lobatto on [0,1] (ascending) and the differentiation matrix"""
    k = np.arange(N + 1); xc = np.cos(np.pi * k / N)
    c = np.ones(N + 1); c[0] = c[-1] = 2; c *= (-1) ** k
    X = np.tile(xc, (N + 1, 1)).T
    D = np.outer(c, 1 / c) / (X - X.T + np.eye(N + 1)); D -= np.diag(D.sum(1))
    # map [-1,1] -> [0,1] ascending: y = (1 - xc)/2
    y = (1 - xc) / 2
    return y, -2 * D

def setup(N):
    y, D = cheb(N)
    I = np.eye(N + 1)
    Dr = np.kron(D, I); Dx = np.kron(I, D)          # grid ordering: index = i_r*(N+1) + i_x
    R, Xg = np.meshgrid(y, y, indexing="ij")
    return dict(N=N, y=y, D=D, Dr=Dr, Dx=Dx, Drr=Dr @ Dr, Dxx=Dx @ Dx, Drx=Dr @ Dx, R=R.ravel(), X=Xg.ravel())

def derivs(G, u):
    return [u, G["Dr"] @ u, G["Dx"] @ u, G["Drr"] @ u, G["Dxx"] @ u, G["Drx"] @ u]

def residual_and_jac(G, U, want_jac=True):
    n = len(G["R"]); N = G["N"]
    fields = [U[i * n:(i + 1) * n] for i in range(5)]
    dv = []
    for u in fields:
        dv += derivs(G, u)
    rr, xx = G["R"], G["X"]
    with np.errstate(all="ignore"):
        Rv = np.array(fres(rr, xx, *dv), dtype=float)                  # 5 x n
        J = np.zeros((5 * n, 5 * n)) if want_jac else None
        if want_jac:
            Jl = fjac(rr, xx, *dv)
            mats = [np.eye(n), G["Dr"], G["Dx"], G["Drr"], G["Dxx"], G["Drx"]]
            for e in range(5):
                for i in range(5):
                    blk = np.zeros((n, n))
                    for t in range(6):
                        c = np.broadcast_to(np.asarray(Jl[e][i * 6 + t], dtype=float), (n,))
                        if np.any(c != 0):
                            blk += c[:, None] * mats[t]
                    J[e * n:(e + 1) * n, i * n:(i + 1) * n] = blk
    # boundary conditions replace the equations on the edges
    Ri = Rv.copy()
    on = lambda m: np.where(m)[0]
    ir = np.round(rr * 1e12) / 1e12; ix = np.round(xx * 1e12) / 1e12
    dir_ = on((ix == 1) | (ir == 1)); r0 = on((ir == 0) & (ix < 1)); x0 = on((ix == 0) & (ir > 0) & (ir < 1))
    T, S, A, B, F = fields
    target = [1, 1, 1, 1, 0]
    def setrow(e, idx, val, rows_from):
        Ri[e, idx] = val
        if want_jac:
            J[e * n + idx, :] = 0
            for (fi, M) in rows_from:
                J[e * n + idx, fi * n:(fi + 1) * n] += M[idx]
    Id = np.eye(n)
    for e in range(5):
        setrow(e, dir_, fields[e][dir_] - target[e], [(e, Id)])
    # r = 0 (the horizon): T = A, and d_r of S, A, B, F zero
    setrow(0, r0, T[r0] - A[r0], [(0, Id), (2, -Id)])
    for e in (1, 2, 3, 4):
        setrow(e, r0, (G["Dr"] @ fields[e])[r0], [(e, G["Dr"])])
    # x = 0 (the axis): S = B, and d_x of T, A, B, F zero
    setrow(1, x0, S[x0] - B[x0], [(1, Id), (3, -Id)])
    for e in (0, 2, 3, 4):
        setrow(e, x0, (G["Dx"] @ fields[e])[x0], [(e, G["Dx"])])
    return Ri.ravel(), J

def newton(G, U, tol=1e-11, maxit=30, verbose=True):
    for it in range(maxit):
        Rv, J = residual_and_jac(G, U)
        nr = np.max(np.abs(Rv))
        if verbose:
            print("  it %d  |R| = %.3e" % (it, nr), flush=True)
        if nr < tol:
            return U, nr
        dU = np.linalg.solve(J, -Rv)
        lam = 1.0
        while lam > 1e-3:
            U2 = U + lam * dU
            if np.max(np.abs(residual_and_jac(G, U2, False)[0])) < nr * (1 - 1e-4 * lam) or lam < 0.05:
                break
            lam /= 2
        U = U2
    return U, nr

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    G = setup(N); n = len(G["R"])
    U = np.concatenate([np.ones(n), np.ones(n), np.ones(n), np.ones(n), np.zeros(n)])
    U, nr = newton(G, U)
    np.save("sol_N%d.npy" % N, U)
    print("N=%d final |R| = %.3e" % (N, nr))
