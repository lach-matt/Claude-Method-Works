import time, numpy as np, sys
from scipy.integrate import solve_ivp
import interior2 as I2
Nx = int(sys.argv[1]); s0 = float(sys.argv[2]); s1 = float(sys.argv[3]); meth = sys.argv[4]
I = I2.Interior(Nx, "solsx_28_28.npy", 28, 28)
Y0 = I.initial(s0); cnt = [0]
def f(s, Y):
    cnt[0] += 1
    return I.rhs(s, Y)
t0 = time.time()
sol = solve_ivp(f, (s0, s1), Y0, method=meth, rtol=1e-7, atol=1e-9)
print("%s: status %d, %d steps, %d rhs calls, %.1f s; s reached %.5f" % (meth, sol.status, len(sol.t), cnt[0], time.time() - t0, sol.t[-1]))
m = I.m
for k in np.linspace(0, len(sol.t) - 1, 6).astype(int):
    Y = sol.y[:, k]; Xf = I.fill(Y[:5 * m].reshape(5, m))
    print("  s=%.5f T(ax)=%.6f minT=%.4e max|X_s|=%.3e max|phi|=%.2e" % (sol.t[k], Xf[0, 0], Xf[0].min(),
          np.abs(Y[5 * m:]).max(), np.abs(I.phi(sol.t[k], Y)).max()))
dt = np.diff(sol.t); print("  step sizes: first %.2e  median %.2e  last %.2e" % (dt[0], np.median(dt), dt[-1]))
