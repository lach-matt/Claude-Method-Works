import numpy as np, sys
sys.path.insert(0, "."); import p3m
P3 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
G = p3m.Global(34, 20, -0.30)
U6 = np.load(P3 + "ctrl_s-0.300.npy"); U = U6[:5 * G.n].copy()
p = dict(bt=2.0, kap=0.0)
R, _ = G.residual(U, p, jac=False)
print("old control in the p3m system: |R| %.1e" % np.max(np.abs(R)))
U, r, it = G.solve(U, p, maxit=10)
I0 = p3m.DT.interp_matrix(G.s, np.array([0.0]))
print("kap 0: |R| %.1e (%d) R4 %.5f, xi2 int %.1e" % (r, it, 2 * np.sqrt((I0 @ G.field(U, 4))[0, -1]),
                                                     np.nanmax(G.xi2(U, p)[G.s < -0.02][:, 1:])))
np.save("glob_ctrl0.npy", U)
