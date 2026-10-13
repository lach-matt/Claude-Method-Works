import numpy as np, pickle, sys
import interior_fw as IF, analyze_fw as AF, core_fw as C
fn, Nx, b = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]); lam_mode = len(sys.argv) > 4
P = pickle.load(open(fn, "rb")); st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); m = I.m
U = np.load(st["file"]); n = 25 * 25; sn = C.radau01(24)
I.lastbr = np.array([C.bary_interp(sn, U[e * n:(e + 1) * n].reshape(25, 25), [0.0])[0][-1] for e in range(4)])
if lam_mode:
    src = pickle.load(open(P["src"], "rb"))
    for k in range(len(src["t"])):
        Y = src["y"][:, k]; I.brane_values(src["t"][k], Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
tau_ax = tau_br = 0.0; prev = None
sel = set(np.linspace(0, len(P["t"]) - 1, 12).astype(int).tolist())
for k in range(len(P["t"])):
    if lam_mode:
        s, Y = IF.state_s(I, P["t"][k], P["y"][:, k])
    else:
        s, Y = P["t"][k], P["y"][:, k]
    g = AF.gss(I, s, Y)
    if prev is not None:
        ds = abs(s - prev[0]); tau_ax += 0.5 * (np.sqrt(g[1]) + np.sqrt(prev[1][1])) * ds
        tau_br += 0.5 * (np.sqrt(g[-1]) + np.sqrt(prev[1][-1])) * ds
    prev = (s, g)
    if k in sel:
        K = AF.kretschmann(I, s, Y)
        j = 1 + np.nanargmax(K[1:])
        print("s=%10.4f  proper time from s0: near-axis node %.4f, brane %.4f  K: brane %.4e, near-axis %.4e, max %.4e"
              " at x=%.3f" % (s, tau_ax, tau_br, K[-1], K[1], np.nanmax(K[1:]), I.xn[j]), flush=True)
