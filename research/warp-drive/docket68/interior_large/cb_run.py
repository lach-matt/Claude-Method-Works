"""item 367 step 1: evolve in lambda = ln(1 - s) from a run's state at s1 with every constraint component imposed at
the brane (interior_cb.py).  Arguments: src mode s1 mu lam_end [rtol ramp kap_driven]; mode "damped" (no driver),
"gauge3" (pointwise driver, wF = 0), "gauge5" (one-function driver, x-mean) or "harm" (pure harmonic
time, h^s = -R Fbar^s; mu unused)."""
import numpy as np, pickle, sys, time
import interior_fw as IF, interior_damp as ID, interior_gauge as IG, interior_cb as CB
src, mode, s1, mu, lam_end = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
rtol = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-8
ramp = float(sys.argv[7]) if len(sys.argv) > 7 else 0.3
P = pickle.load(open(src, "rb")); b, Nx = P["b"], P["Nx"]; kap, at = P.get("kap", 0.0), P.get("at", 0.0)
kap_g = float(sys.argv[8]) if len(sys.argv) > 8 else kap
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I0 = ID.Damped(Nx, b, st, kap, at); I0.lastbr = ID.static_brane(b); m = I0.m
k1 = 0
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    I0.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); k1 = k
    if s <= s1:
        break
s1, Y1 = P["t"][k1], P["y"][:, k1]
N, Fb = IG.lapse_and_Fbar(I0, s1, Y1); Nst = N.copy(); Nst[0] = -(I0.D[0, 1:] @ Nst[1:]) / I0.D[0, 0]
if mode == "damped":
    I = CB.DampedCB(Nx, b, st, kap_g, at)
elif mode == "gauge3":
    I = CB.GaugeCB(Nx, b, st, kap_g, at, mu, s1, Nst, ramp, 0.0)
elif mode == "harm":
    I = CB.HarmCB(Nx, b, st, kap_g, at, s1, ramp)
elif mode == "harmold":
    I = CB.HarmOld(Nx, b, st, kap_g, at, s1, ramp)
else:
    I = CB.Gauge5CB(Nx, b, st, kap_g, at, mu, s1, np.ones(Nx + 1), ramp, "mean")
    Xf, Vf = I0.brane_values(s1, Y1[:5 * m].reshape(5, m), Y1[5 * m:].reshape(5, m)); I.Nst = I.lapse(s1, Xf, Vf)[0]
I.lastbr = I0.lastbr.copy()
print("cb %s at s1=%.4f (mu %g, kap %g, Nx %d): lapse ax %.4f br %.4f; phi (old rows) %.2e, phi~ (cb) %.2e" % (
    mode, s1, mu, kap_g, Nx, Nst[0], Nst[-1], np.nanmax(np.abs(IF.phi_at(I0, s1, Y1)[1:])),
    np.nanmax(np.abs(I.phi_t(s1, Y1)[1:]))), flush=True)
I.lastbr = I0.lastbr.copy(); t0 = time.time()
out = "cb_%s_%d_%g_mu%g_s%.3g_k%g.pkl" % (mode, Nx, b, mu, s1, kap_g)
meta = dict(t=P["t"][:k1 + 1], y=P["y"][:, :k1 + 1], Nx=Nx, b=b, kap=kap, at=at, mu=mu, s1=s1, Nst=I.Nst
            if hasattr(I, "Nst") else Nst, src=src, ramp=ramp, kap_driven=kap_g, mode=mode)
lt, ly = IG.run_steps(I, Y1, s1, lam_end, rtol=rtol, save=out, meta=meta, method="DOP853")
pickle.dump(dict(lt=lt, ly=ly, **meta), open(out, "wb"))
print("saved %s, lambda %.3f -> %.3f, %.0f s" % (out, lt[0], lt[-1], time.time() - t0), flush=True)
