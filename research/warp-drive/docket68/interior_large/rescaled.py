"""the fields rescaled by their u = 1/(1 - s) powers, across x, along a run (brane solve marched in order)"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID
fn = sys.argv[1]; targets = [float(v) for v in sys.argv[2:]]
P = pickle.load(open(fn, "rb")); b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); I.lastbr = ID.static_brane(b); m = I.m
cols = [0, 1, 3, 6, 10, 14, 17, 18, 19, 20] if Nx == 20 else list(range(0, Nx + 1, 2))
print("x        " + " ".join("%8.4f" % I.xn[c] for c in cols))
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and s <= targets[0]:
        targets.pop(0); u = 1 / (1 - s); T, S, A, B, F = Xf
        print("s=%.3f u=%.4f" % (s, u))
        for lab, v in (("T/u", T / u), ("A/u", A / u), ("S u^2", S * u * u), ("B u^2", B * u * u), ("F u", F * u),
                       ("A/T", A / T)):
            print("  %-6s " % lab + " ".join("%8.4f" % v[c] for c in cols))
