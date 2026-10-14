"""switch gen_gauge5_fw.py's one-function driver on at s1 from a run's state and evolve in lambda = ln(1 - s) to
lam_end.  Arguments: src s1 mu lam_end [rtol ramp kap_driven mode], mode "mean" or "brane"."""
import numpy as np, pickle, sys, time
import interior_fw as IF, interior_damp as ID, interior_gauge as IG, interior_gauge5 as G5
src, s1, mu, lam_end = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
rtol = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-8
ramp = float(sys.argv[6]) if len(sys.argv) > 6 else 0.3
kap_d = float(sys.argv[7]) if len(sys.argv) > 7 else None
mode = sys.argv[8] if len(sys.argv) > 8 else "mean"
P = pickle.load(open(src, "rb")); b, Nx = P["b"], P["Nx"]; kap, at = P.get("kap", 0.0), P.get("at", 0.0)
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
kap_g = kap if kap_d is None else kap_d
I = G5.Gauge5(Nx, b, st, kap_g, at, mu, s1, np.ones(Nx + 1), ramp, mode); I.lastbr = ID.static_brane(b); m = I.m
k1 = 0
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); k1 = k
    if s <= s1:
        break
s1, Y1 = P["t"][k1], P["y"][:, k1]
I.s1 = s1; I.Nst = I.lapse(s1, Xf, Vf)[0]                       # the switch slice's lapse, per unit lambda after
print("switch at s1=%.4f (%s, mu %g, kap %g, Nx %d): lapse ax %.4f br %.4f; phi %.2e, phi~ %.2e" % (
    s1, mode, mu, kap_g, Nx, I.Nst[0], I.Nst[-1], np.nanmax(np.abs(IF.phi_at(I, s1, Y1)[1:])),
    np.nanmax(np.abs(I.phi_t(s1, Y1)[1:]))), flush=True)
t0 = time.time()
out = "gauge5%s_%d_%g_mu%g_s%.3g_k%g.pkl" % (mode, Nx, b, mu, s1, kap_g)
meta = dict(t=P["t"][:k1 + 1], y=P["y"][:, :k1 + 1], Nx=Nx, b=b, kap=kap, at=at, mu=mu, s1=s1, Nst=I.Nst, src=src,
            ramp=ramp, kap_driven=kap_g, mode=mode)
lt, ly = IG.run_steps(I, Y1, s1, lam_end, rtol=rtol, save=out, meta=meta)
pickle.dump(dict(lt=lt, ly=ly, **meta), open(out, "wb"))
print("saved %s, lambda %.3f -> %.3f, %.0f s" % (out, lt[0], lt[-1], time.time() - t0), flush=True)
