import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, interior_gauge as IG
P = pickle.load(open(sys.argv[1], "rb")); b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I0 = ID.Damped(Nx, b, st, P["kap"], P["at"]); I0.lastbr = ID.static_brane(b); m = I0.m
for k in range(len(P["t"])):
    I0.brane_values(P["t"][k], P["y"][:5 * m, k].reshape(5, m), P["y"][5 * m:, k].reshape(5, m))
I = IG.Gauge(Nx, b, st, P.get("kap_driven", P["kap"]), P["at"], P["mu"], P["s1"], P["Nst"], P.get("ramp", 0.3), 0.0)
I.lastbr = I0.lastbr.copy()
targets = [float(v) for v in sys.argv[2:]]
print("x   " + " ".join("%8.3f" % v for v in I.xn))
for k in range(len(P["lt"])):
    s, Y = IF.state_s(I, P["lt"][k], P["ly"][:, k])
    I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and s <= targets[0]:
        targets.pop(0); ph = np.abs(IG.phi_tilde(I, s, Y)); N, Fb = IG.lapse_and_Fbar(I, s, Y)
        print("s=%.3f |phi~| " % s + " ".join("%8.1e" % v for v in ph))
        print("        N*(1-s) " + " ".join("%8.4f" % v for v in N * (1 - s)), "  target",
              "%.4f" % (I.Nst[1] * (1 - I.s1)))
