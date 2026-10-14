import numpy as np, sympy as sp, pickle, solver as S, sys
from numpy.polynomial import chebyshev as C
names = ["T", "S", "A", "B", "F"]; tags = ["", "_r", "_x", "_rr", "_xx", "_rx"]
r, x = sp.symbols("r x", real=True)
K = sp.sympify(eval(pickle.load(open("kretsch.pkl", "rb")), {**sp.__dict__}))
fK = sp.lambdify([r, x] + [sp.Symbol(n + t) for n in names for t in tags], K, "numpy", cse=True)
N = int(sys.argv[1]); G = S.setup(N); n = len(G["R"]); U = np.load("sol_N%d.npy" % N); y = G["y"]
# fine evaluation grid via the Chebyshev interpolant of each field and its derivatives
V = C.chebvander(2 * y - 1, N)
M = 121; yy = np.linspace(0.0005, 0.9995, M)
Vt = C.chebvander(2 * yy - 1, N)
def ev(coef, dr, dx):
    cr = C.chebder(coef, dr, axis=0, scl=2.0) if dr else coef
    cc = C.chebder(cr, dx, axis=1, scl=2.0) if dx else cr
    Vr = C.chebvander(2 * yy - 1, cc.shape[0] - 1); Vx = C.chebvander(2 * yy - 1, cc.shape[1] - 1)
    return (Vr @ cc @ Vx.T).ravel()
vals = []
for i in range(5):
    Fm = U[i * n:(i + 1) * n].reshape(N + 1, N + 1)
    cf = np.linalg.solve(V, np.linalg.solve(V, Fm).T).T
    for (dr, dx) in ((0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (1, 1)):
        vals.append(ev(cf, dr, dx))
RR, XX = np.meshgrid(yy, yy, indexing="ij")
with np.errstate(all="ignore"):
    Kv = np.asarray(fK(RR.ravel(), XX.ravel(), *vals), dtype=float)
C2 = Kv - 40.0
Lw = C2 ** (-0.25)
j = np.nanargmin(Lw)
print("N=%d  K at AdS-like corner check: min K %.3f max K %.3f; Weyl length min = %.4f at r=%.3f x=%.3f; C2 max %.3f"
      % (N, np.nanmin(Kv), np.nanmax(Kv), Lw[j], RR.ravel()[j], XX.ravel()[j], np.nanmax(C2)))
