"""the s-leg of hr_run.py alone: damped, from the horizon (s0 = -0.002) to s_mid, saved as hr_<Nx>_<b>_<kap>_s.pkl"""
import numpy as np, pickle, sys, time
import interior_damp as ID
from scipy.integrate import solve_ivp
Nx, b, kap, at, s_mid = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, kap, at); I.lastbr = ID.static_brane(b)
Y0 = I.initial(-0.002, 2); t0 = time.time()
sol = solve_ivp(I.rhs, (-0.002, s_mid), Y0, method="Radau", rtol=1e-8, atol=1e-10)
print("leg 1: Nx=%d bt=%g kap=%g s -> %g status %d, %d steps, %.0f s" % (Nx, b, kap, s_mid, sol.status, len(sol.t),
                                                                        time.time() - t0), flush=True)
out = "hr_%d_%g_%g_s.pkl" % (Nx, b, kap)
pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, b=b, s0=-0.002, kap=kap, at=at), open(out, "wb"))
