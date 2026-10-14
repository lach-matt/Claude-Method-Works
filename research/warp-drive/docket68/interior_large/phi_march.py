"""march the brane solve in order through a run; print T, the DeTurck norm phi and the metric functions at 12 steps"""
import numpy as np, pickle, sys
import interior_fw as IF, core_fw as C
fn, Nx, b = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
P = pickle.load(open(fn, "rb")); st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); m = I.m
U = np.load(st["file"]); n = 25 * 25; sn = C.radau01(24)
I.lastbr = np.array([C.bary_interp(sn, U[e * n:(e + 1) * n].reshape(25, 25), [0.0])[0][-1] for e in range(4)])
sel = set(np.linspace(0, len(P["t"]) - 1, 14).astype(int).tolist())
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if k in sel:
        ph = IF.phi_at(I, s, Y)
        print("s=%8.4f T ax %.4e br %.4e | S ax %.3e br %.3e | A ax %.3e br %.3e | B ax %.3e br %.3e | F max %.2e"
              " | phi max %.2e at x=%.2f" % (s, Xf[0, 0], Xf[0, -1], Xf[1, 0], Xf[1, -1], Xf[2, 0], Xf[2, -1],
                                             Xf[3, 0], Xf[3, -1], np.abs(Xf[4]).max(), np.nanmax(np.abs(ph)),
                                             I.xn[np.nanargmax(np.abs(ph))]), flush=True)
