import numpy as np, solver as S
from numpy.polynomial import chebyshev as C
N = 24; G = S.setup(N); n = len(G["R"]); U = np.load("sol_N%d.npy" % N); y = G["y"]
V = C.chebvander(2 * y - 1, N)
def coef(i):
    Fm = U[i * n:(i + 1) * n].reshape(N + 1, N + 1)
    return np.linalg.solve(V, np.linalg.solve(V, Fm).T).T
cT = coef(0)
def T(r, x):
    return (C.chebvander(np.atleast_1d(2 * r - 1), N) @ cT @ C.chebvander(np.atleast_1d(2 * x - 1), N).T)
print(" r     q2=(1-T)/w^2 vs 1-r^2      t4      t4*R (-> -1/4)")
for r in (0.3, 0.5, 0.7, 0.8, 0.9, 0.95):
    ws = np.linspace(0.02, 0.12, 12); xs = np.sqrt(1 - ws)
    vals = np.array([T(r, xx)[0, 0] for xx in xs])
    # fit T - 1 = a2 w^2 + a3 w^3 + a4 w^4 + a5 w^5 (+ log at w^5 in F only)
    M = np.vstack([ws**2, ws**3, ws**4, ws**5, ws**6]).T
    a = np.linalg.lstsq(M, vals - 1, rcond=None)[0]
    t4 = a[2]; R = 1 / (1 - r * r)
    print("%.2f   %.6f vs %.6f   a3=%.1e   %.5f   %.4f" % (r, -a[0], 1 - r * r, a[1], t4, t4 * R))
