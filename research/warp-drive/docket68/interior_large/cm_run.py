"""Item 367 step 3: the interior pipeline of the RSII hole run on the AdS4 C-metric (gen_eqs_cm.py), unchanged: Taylor
start at s0 from the static Einstein-DeTurck solution (solver_fw.py under PROB=<tag>), brane rows Israel + xi^x = 0 +
F = 0 (interior_cb.HarmOld), damping kap with the tilted normal; Radau in s from s0 to sm (the horizon's 1/s
stiffness defeats an explicit stepper there, as in the RSII runs, whose explicit phase began at s = -0.5), then
lambda = ln(1 - s) stepping by DOP853, and pure harmonic time ramped in from s1 <= sm (a very negative s1, e.g. -1e9,
keeps the DeTurck slicing throughout).
The Radau phase takes interior_cb.fd_jac, the fixed-step Jacobian: scipy's own meets the brane solve's noise and stalls
(as cb_diag3/4 found for the RSII rows; here on the exact chart it never finished, and with fd_jac takes 25 steps).
Arguments: tag eps Ns Nx_static Nx kap at s0 sm s1 lam_end [rtol ramp]  (eps: the reference's deformation, bt)."""
import os, sys
os.environ["PROB"] = sys.argv[1]
import numpy as np, pickle, time
from scipy.integrate import solve_ivp
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_gauge as IG, interior_cb as CB
tag, b = sys.argv[1], float(sys.argv[2])
Ns, Nxs, Nx = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
kap, at, s0, sm, s1, lam_end = (float(v) for v in sys.argv[6:12])
rtol = float(sys.argv[12]) if len(sys.argv) > 12 else 1e-8
ramp = float(sys.argv[13]) if len(sys.argv) > 13 else 0.3
st = dict(file=C.static_file(b, Ns, Nxs), Ns=Ns, Nx=Nxs)
I = CB.HarmOld(Nx, b, st, kap, at, s1, ramp); I.lastbr = ID.static_brane(b, Ns, Nxs)
Y0 = I.initial(s0, 2); m = I.m
print("cm %s eps %g: Nx %d kap %g at %g s0 %g sm %g, harmonic from s1 = %g; phi at start %.2e" % (
    tag, b, Nx, kap, at, s0, sm, s1, np.nanmax(np.abs(IF.phi_at(I, s0, Y0)[1:]))), flush=True)
out = "cmr_%s_e%g_%d_k%g_s%g.pkl" % (tag, b, Nx, kap, s1)
meta = dict(tag=tag, Nx=Nx, b=b, kap=kap, at=at, s0=s0, sm=sm, s1=s1, ramp=ramp, Ns=Ns, Nxs=Nxs,
            lastbr0=I.lastbr.copy())
t0 = time.time()
sol = solve_ivp(I.rhs, (s0, sm), Y0, method="Radau", rtol=rtol, atol=rtol * 1e-2, jac=CB.fd_jac(I, I.rhs))
print("Radau s %g -> %g: status %d (%s), %d steps, %.0f s; phi %.2e" % (
    s0, sol.t[-1], sol.status, sol.message, len(sol.t), time.time() - t0,
    np.nanmax(np.abs(IF.phi_at(I, sol.t[-1], sol.y[:, -1])[1:]))), flush=True)
meta.update(t=sol.t, y=sol.y, lastbr1=I.lastbr.copy())
lt, ly = IG.run_steps(I, sol.y[:, -1], sol.t[-1], lam_end, rtol=rtol, save=out, meta=meta, method="DOP853")
pickle.dump(dict(lt=lt, ly=ly, **meta), open(out, "wb"))
print("saved %s, lambda %.3f -> %.3f, %.0f s" % (out, lt[0], lt[-1], time.time() - t0), flush=True)
