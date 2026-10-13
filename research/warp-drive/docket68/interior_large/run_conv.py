import numpy as np, sympy as sp, pickle, solver as S
from numpy.polynomial import chebyshev as C
names = ["T", "S", "A", "B", "F"]
ns = {n + t: sp.Symbol(n + t) for n in names for t in ("", "_r", "_x")}
phi = sp.sympify(eval(pickle.load(open("phi.pkl", "rb")), {**sp.__dict__}))
r, x = sp.symbols("r x", real=True)
fphi = sp.lambdify([r, x] + [ns[n + t] for n in names for t in ("", "_r", "_x")], phi, "numpy")

def interp(Gfrom, U, Gto):
    """evaluate the tensor Chebyshev interpolant of each field on the new grid"""
    N = Gfrom["N"]; y = Gfrom["y"]; out = []
    n = len(Gfrom["R"])
    for i in range(5):
        F = U[i * n:(i + 1) * n].reshape(N + 1, N + 1)
        # fit in t = 2y - 1
        V = C.chebvander(2 * y - 1, N)
        coef = np.linalg.solve(V, np.linalg.solve(V, F).T).T      # c_ij with F = V c V^T
        Vt = C.chebvander(2 * Gto["y"] - 1, N)
        out.append((Vt @ coef @ Vt.T).ravel())
    return np.concatenate(out)

def phimax(G, U):
    n = len(G["R"]); vals = []
    for i in range(5):
        u = U[i * n:(i + 1) * n]; vals += [u, G["Dr"] @ u, G["Dx"] @ u]
    with np.errstate(all="ignore"):
        p = np.asarray(fphi(G["R"], G["X"], *vals), dtype=float)
    m = (G["R"] > 0) & (G["X"] > 0) & (G["X"] < 1) & (G["R"] < 1)
    return np.nanmax(np.abs(p[m]))

prev = None
for N in (8, 12, 16, 20, 24):
    G = S.setup(N); n = len(G["R"])
    if prev is None:
        U = np.load("dbg_U8.npy")
    else:
        U = interp(prev[0], prev[1], G)
    for it in range(15):
        R, J = S.residual_and_jac(G, U)
        if np.abs(R).max() < 1e-10: break
        U = U + np.linalg.solve(J, -R)
    np.save("sol_N%d.npy" % N, U)
    T = U[:n].reshape(N + 1, N + 1)
    print("N=%d |R|=%.2e phi_max=%.3e  T(r=0,x=0)=%.10f A(0,0)=%.10f" % (N, np.abs(R).max(), phimax(G, U), T[0, 0],
          U[2 * n:3 * n].reshape(N + 1, N + 1)[0, 0]), flush=True)
    prev = (G, U)
