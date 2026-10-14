import numpy as np, pickle, sys
import interior_fw as IF, core_fw as C
fn, Nx, b = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
P = pickle.load(open(fn, "rb")); st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); m = I.m
# brane values at s = 0 from the static solution
U = np.load(st["file"]); n = 25 * 25; sn, xn = C.radau01(24), C.lobatto01(24)
I.lastbr = np.array([C.bary_interp(sn, U[e * n:(e + 1) * n].reshape(25, 25), [0.0])[0][-1] for e in range(4)])
print("static brane values at s=0:", I.lastbr)
rows = []
for k in range(len(P["t"])):
    s = P["t"][k]; Y = P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    rows.append((s, Xf[0, 0], Xf[0, -1], Xf[0].min(), np.abs(I._r(s, Xf[:4, -1], Y[:5 * m].reshape(5, m))).max()))
for k in np.linspace(0, len(rows) - 1, 12).astype(int):
    Y = P["y"][:, k]
    # re-solve to set lastbr consistently along the march (already marched above in order)
    print("s=%8.4f T(ax)=%.6f T(brane)=%.6f minT=%.4e  brane residual %.1e" % rows[k], flush=True)
