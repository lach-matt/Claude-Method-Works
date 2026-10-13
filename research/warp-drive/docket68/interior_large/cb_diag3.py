"""stepper behaviour from the s = -0.5 state: old rows against the new rows (plain F_s; flow F_xs(1)), 20 Radau steps in
s, with step sizes, rhs evaluations, Jacobians and LU decompositions"""
import numpy as np, pickle, time, sys
from scipy.integrate import Radau
import interior_damp as ID, interior_cb as CB
P = pickle.load(open("hr_28_1_4_s.pkl", "rb")); b, Nx = P["b"], P["Nx"]
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
Io = ID.Damped(Nx, b, st, P["kap"], P["at"]); Io.lastbr = ID.static_brane(b); m = Io.m
for k in range(len(P["t"])):
    s0, Y0 = P["t"][k], P["y"][:, k]
    Io.brane_values(s0, Y0[:5 * m].reshape(5, m), Y0[5 * m:].reshape(5, m))
    if s0 <= -0.5:
        break
br = Io.lastbr.copy()
which = sys.argv[1]
if which == "old":
    I = Io
else:
    I = CB.DampedCB(Nx, b, st, P["kap"], P["at"]); I.fs_mode = which
I.lastbr = br.copy(); t0 = time.time()
jac = CB.fd_jac(I, I.rhs) if len(sys.argv) > 2 else None
sol = Radau(I.rhs, s0, Y0, -3.0, rtol=1e-8, atol=1e-10, first_step=1e-4, jac=jac)
hs = []
for k in range(20):
    sol.step(); hs.append(sol.step_size)
print("%-6s 20 steps to s=%.5f in %.0f s; nfev %d njev %d nlu %d; step sizes %s" % (
    which, sol.t, time.time() - t0, sol.nfev, sol.njev, sol.nlu, " ".join("%.1e" % h for h in hs[::2])), flush=True)
