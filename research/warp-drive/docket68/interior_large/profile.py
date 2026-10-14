"""proper time, phi and K at every x node at chosen s along a run (marched in order), with dtau/ds"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, analyze_damp as AD
fn = sys.argv[1]; targets = [float(v) for v in sys.argv[2:]]
P = pickle.load(open(fn, "rb")); b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, P.get("kap", 0.0), P.get("at", 0.0)); I.lastbr = ID.static_brane(b); m = I.m
tau = np.zeros(Nx + 1); prev = None
cols = [1, 3, 5, 8, 10, 12, 15, 17, 19, 20] if Nx == 20 else list(range(1, Nx + 1, 2)) + [Nx]
print("x     " + " ".join("%9.4f" % I.xn[c] for c in cols))
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N, p = AD.geometry(I, s, Xf, Vf)
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
    if targets and s <= targets[0]:
        targets.pop(0); ph = IF.phi_at(I, s, Y); K = AD.kretschmann(I, s, Y)
        print("s=%.3f" % s)
        for lab, v in (("tau", tau), ("N", N), ("K", K), ("|phi|", np.abs(ph)), ("S2", (p ** 2).sum(0) + p[2] ** 2)):
            print("  %-5s" % lab + " ".join("%9.3e" % v[c] for c in cols))
