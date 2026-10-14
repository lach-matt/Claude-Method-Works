"""Chebyshev coefficients of each field in x along a run (brane solve marched in order): is the x-structure resolved?"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID
fn, Nx, b = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]); targets = [float(v) for v in sys.argv[4:]]
P = pickle.load(open(fn, "rb")); st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); I.lastbr = ID.static_brane(b); m = I.m
def cheb(v):          # nodal values at x_j = (1 - cos(pi j/N))/2, j = 0..N  ->  Chebyshev coefficients
    N = len(v) - 1; j = np.arange(N + 1); c = np.zeros(N + 1)
    w = np.ones(N + 1); w[0] = w[-1] = 0.5
    for k in range(N + 1):
        c[k] = (2.0 / N) * np.sum(w * v * np.cos(np.pi * k * j / N)) * (0.5 if k in (0, N) else 1.0)
    return np.abs(c)
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and s <= targets[0]:
        targets.pop(0)
        print("s=%.3f  |c_k| relative to max, last 4 of each field:" % s)
        for e, n in enumerate("TSABF"):
            c = cheb(Xf[e]); print("   %s  %s" % (n, " ".join("%.1e" % q for q in (c / c.max())[-4:])))
