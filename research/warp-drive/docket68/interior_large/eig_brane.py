"""linearised spectrum of the interior right-hand side at chosen s along an undamped run (brane solve marched in
order); growing modes toward decreasing s have Re mu < 0.  Prints the most negative and their localisation in x."""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID
fn, Nx, b = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]); targets = [float(v) for v in sys.argv[4:]]
P = pickle.load(open(fn, "rb")); st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); I.lastbr = ID.static_brane(b); m = I.m
names = "TSABF"
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and s <= targets[0]:
        targets.pop(0); br = I.lastbr.copy(); f0 = I.rhs(s, Y); n = len(Y); J = np.empty((n, n))
        for j in range(n):
            h = 1e-7 * max(1.0, abs(Y[j])); Yp = Y.copy(); Yp[j] += h; I.lastbr = br.copy()
            J[:, j] = (I.rhs(s, Yp) - f0) / h
        I.lastbr = br
        mu, V = np.linalg.eig(J); o = np.argsort(mu.real)
        print("s=%.4f  five most negative Re mu:" % s)
        for q in o[:5]:
            v = np.abs(V[:5 * m, q]).reshape(5, m); e, i = np.unravel_index(np.argmax(v), v.shape)
            print("   mu = %+.3e %+.3ei   peak in %s at x=%.4f" % (mu[q].real, mu[q].imag, names[e], I.xn[1 + i]))
        print("   most positive Re mu: %+.3e" % mu.real.max(), flush=True)
