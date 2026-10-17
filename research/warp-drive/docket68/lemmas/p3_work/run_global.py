import numpy as np, sys, time
sys.path.insert(0, "."); import p3m
P3 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
kap = float(sys.argv[1]) if len(sys.argv) > 1 else 0.2908
Ns, Nx, smin = 38, 20, -0.30
G = p3m.Global(Ns, Nx, smin)
U6 = np.load(P3 + "deep_b_s-0.300.npy")
n = G.n
U = U6[:5 * n].copy()
p = dict(bt=2.0, kap=kap)
t0 = time.time()
U, r, it = G.solve(U, p, quiet=False, maxit=25)
print("kap %.4f: |R| %.2e (%d its, %.0f s)" % (kap, r, it, time.time() - t0))
T, A, B, F, S = (G.field(U, m) for m in range(5))
I0 = p3m.DT.interp_matrix(G.s, np.array([0.0]))
R4 = 2 * np.sqrt((I0 @ S)[0, -1])
xi = G.xi2(U, p)
print("R4 %.5f (P2 member 1.7914); plane T at horizon %.5f (P2 1.1884); xi2 max ext %.1e int %.1e" % (
    R4, (I0 @ T)[0, -1], np.nanmax(xi[G.s > 0.02][:, 1:]), np.nanmax(xi[G.s < -0.02][:, 1:])))
for i in range(0, Ns + 1, 4):
    print("  s %+.3f plane T %.5f A %.5f S %.5f F %.2e | axis T %.5f" % (G.s[i], T[i, -1], A[i, -1], S[i, -1], F[i, -1], T[i, 0]))
np.save("glob_kap%.4f.npy" % kap, U)
