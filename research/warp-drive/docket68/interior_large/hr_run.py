"""high-resolution damped run: s-time from s0 to s_mid, then lambda = ln(1 - s) = -ln u to lam_end; saves both legs"""
import numpy as np, pickle, sys, time
import interior_fw as IF, interior_damp as ID
from scipy.integrate import solve_ivp
Nx, b, kap, at, s_mid, lam_end = (int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]),
                                  float(sys.argv[5]), float(sys.argv[6]))
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, kap, at); I.lastbr = ID.static_brane(b); m = I.m
Y0 = I.initial(-0.002, 2); t0 = time.time()
sol = solve_ivp(I.rhs, (-0.002, s_mid), Y0, method="Radau", rtol=1e-8, atol=1e-10)
print("leg 1: Nx=%d bt=%g kap=%g s -> %g status %d, %d steps, %.0f s" % (Nx, b, kap, s_mid, sol.status, len(sol.t),
                                                                        time.time() - t0), flush=True)
tag = "hr_%d_%g_%g" % (Nx, b, kap)
pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, b=b, s0=-0.002, kap=kap, at=at), open(tag + "_s.pkl", "wb"))
sl = IF.run_lambda(I, sol.y[:, -1], sol.t[-1], lam_end, rtol=1e-8)
pickle.dump(dict(t=sol.t, y=sol.y, lt=sl.t, ly=sl.y, Nx=Nx, b=b, s0=-0.002, kap=kap, at=at), open(tag + ".pkl", "wb"))
print("leg 2 saved %s.pkl: lambda %.3f -> %.3f status %d" % (tag, sl.t[0], sl.t[-1], sl.status), flush=True)
