"""explicit RK45 over s in [-0.5033, -0.53] from the same state: old rows against the new rows; the step count shows
whether the solution itself carries fast dynamics; and the new rows' slope F_x(1) along the way"""
import numpy as np, pickle, time, sys
from scipy.integrate import solve_ivp
import interior_damp as ID, interior_cb as CB
P = pickle.load(open("hr_28_1_4_s.pkl", "rb")); b, Nx = P["b"], P["Nx"]
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
Io = ID.Damped(Nx, b, st, P["kap"], P["at"]); Io.lastbr = ID.static_brane(b); m = Io.m
for k in range(len(P["t"])):
    s0, Y0 = P["t"][k], P["y"][:, k]
    Io.brane_values(s0, Y0[:5 * m].reshape(5, m), Y0[5 * m:].reshape(5, m))
    if s0 <= -0.5:
        break
br = Io.lastbr.copy(); which = sys.argv[1]
I = Io if which == "old" else CB.DampedCB(Nx, b, st, P["kap"], P["at"])
I.lastbr = br.copy(); t0 = time.time()
sol = solve_ivp(I.rhs, (s0, -0.53), Y0, method="RK45", rtol=1e-8, atol=1e-10)
dt = np.diff(sol.t)
print("%-5s RK45 to s=-0.53: status %d, %d steps, nfev %d, step min %.1e median %.1e, %.0f s" % (
    which, sol.status, len(sol.t), sol.nfev, np.abs(dt).min(), np.median(np.abs(dt)), time.time() - t0), flush=True)
