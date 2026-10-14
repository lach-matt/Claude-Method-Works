import numpy as np, pickle, sys, time
import interior_fw as IF, core_fw as C
Nx, b, s_end = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
src = sys.argv[4]
P = pickle.load(open(src, "rb"))
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = IF.Interior(Nx, b, st); m = I.m
U = np.load(st["file"]); n = 25 * 25; sn = C.radau01(24)
static_br = np.array([C.bary_interp(sn, U[e * n:(e + 1) * n].reshape(25, 25), [0.0])[0][-1] for e in range(4)])
# march the brane solve through the source run so the warm start is on the right root
I.lastbr = static_br.copy()
for k in range(len(P["t"])):
    Y = P["y"][:, k]; I.brane_values(P["t"][k], Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
Y = P["y"][:, -1]; s_start = P["t"][-1]
sol = IF.run_lambda(I, Y, s_start, np.log(1 - s_end), rtol=1e-8)
pickle.dump(dict(t=sol.t, y=sol.y, Nx=Nx, b=b, mode="lambda", src=src), open("lam_%d_%g_%g.pkl" % (Nx, b, s_end), "wb"))
print("saved", flush=True)
