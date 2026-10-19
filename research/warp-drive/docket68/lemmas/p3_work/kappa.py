import numpy as np, sys
P3 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
sys.path.insert(0, P3)
from across import Across
A = Across(38, 20, -0.30); U = np.load(P3 + "deep_b_s-0.300.npy")
n = A.n
f = lambda m, j="": (A.D[j] @ U[m * n:(m + 1) * n]).reshape(A.Ns + 1, A.Nx + 1)
T, Aa, S, PX = f(0), f(1), f(4), f(5, "_X")
s = A.s; x = 1.0; bt = 2.0; lam = 64.0
fs = 1 - s
w = bt**2                              # at x = 1
g00 = -w * s * T[:, -1]; g11 = w * Aa[:, -1] / (s * fs**4); g33 = w * 1 * S[:, -1] / fs**2
E2 = -PX[:, -1]**2 / (g00 * g11)
kap = lam * E2 / 2 * g33**2
for i in range(0, A.Ns + 1, 3):
    print("s %+.3f  lam E^2/2 %.5f  g33 %.4f  kappa %.6f" % (s[i], lam * E2[i] / 2, g33[i], kap[i]))
