import numpy as np, sys
import interior2 as I2
Nx = int(sys.argv[1]); s0 = float(sys.argv[2])
I = I2.Interior(Nx, "solsx_28_28.npy", 28, 28); Y0 = I.initial(s0); m = I.m; n = len(Y0)
f0 = I.rhs(s0, Y0); J = np.zeros((n, n)); h = 1e-7
for k in range(n):
    e = np.zeros(n); e[k] = h
    J[:, k] = (I.rhs(s0, Y0 + e) - I.rhs(s0, Y0 - e)) / (2 * h)
w, V = np.linalg.eig(J)
# integrating towards more negative s: growth for modes with Re(lambda) < 0 in d/ds (since ds < 0)
order = np.argsort(w.real)
print("most growing (towards s -> -inf): lambda (per unit s), growth rate = -Re")
xs = I.xn[I.inner]
for k in order[:8]:
    v = np.abs(V[:5 * m, k]).reshape(5, m); fld, j = np.unravel_index(np.argmax(v), v.shape)
    print("  lambda=%+.3e%+.3ei  peak field %s at x=%.4f" % (w[k].real, w[k].imag, "TSABF"[fld], xs[j]))
print("most decaying:", ["%+.2e" % w[k].real for k in order[-3:]])
