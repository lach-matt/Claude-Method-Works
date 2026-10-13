"""switch the lapse driver on at s1 from a run's state and evolve in lambda = ln(1 - s) to lam_end"""
import numpy as np, pickle, sys, time
import interior_fw as IF, interior_damp as ID, interior_gauge as IG
src, s1, mu, lam_end = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
rtol = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-8
P = pickle.load(open(src, "rb")); b, Nx = P["b"], P["Nx"]; kap, at = P.get("kap", 0.0), P.get("at", 0.0)
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I0 = ID.Damped(Nx, b, st, kap, at); I0.lastbr = ID.static_brane(b); m = I0.m
k1 = 0
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    I0.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); k1 = k
    if s <= s1:
        break
s1, Y1 = P["t"][k1], P["y"][:, k1]
N, Fb = IG.lapse_and_Fbar(I0, s1, Y1)
Nst = N + Fb * N ** 3 / mu
Nst[0] = -(I0.D[0, 1:] @ Nst[1:]) / I0.D[0, 0]                     # the axis: even in x
Ig = IG.Gauge(Nx, b, st, kap, at, mu, s1, Nst); Ig.lastbr = I0.lastbr.copy()
ph0 = IF.phi_at(I0, s1, Y1); pht = IG.phi_tilde(Ig, s1, Y1)
print("switch at s1=%.4f: lapse ax %.4f br %.4f; Fbar*N^3/mu ax %.2e br %.2e; phi %.2e, phi~ %.2e" % (
    s1, N[1], N[-1], (Fb * N ** 3 / mu)[1], (Fb * N ** 3 / mu)[-1], np.nanmax(np.abs(ph0[1:])),
    np.nanmax(np.abs(pht[1:]))), flush=True)
t0 = time.time()
sol = IF.run_lambda(Ig, Y1, s1, lam_end, rtol=rtol)
out = "gauge_%d_%g_mu%g_s%g.pkl" % (Nx, b, mu, s1)
pickle.dump(dict(t=P["t"][:k1 + 1], y=P["y"][:, :k1 + 1], lt=sol.t, ly=sol.y, Nx=Nx, b=b, kap=kap, at=at, mu=mu,
                 s1=s1, Nst=Nst, src=src), open(out, "wb"))
print("saved %s, lambda %.3f -> %.3f status %d, %.0f s" % (out, sol.t[0], sol.t[-1], sol.status, time.time() - t0),
      flush=True)
