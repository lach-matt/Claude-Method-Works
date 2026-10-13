"""phi along an hr_resume checkpoint (brane solve marched in order): where the old-gauge lambda leg leaves the
constraint surface"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID
S = pickle.load(open(sys.argv[1], "rb")); L = pickle.load(open(sys.argv[2], "rb"))
b, Nx = S["b"], S["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, S["kap"], S["at"]); I.lastbr = ID.static_brane(b); m = I.m
for k in range(len(S["t"])):
    I.brane_values(S["t"][k], S["y"][:5 * m, k].reshape(5, m), S["y"][5 * m:, k].reshape(5, m))
sel = set(np.linspace(0, len(L["lt"]) - 1, 16).astype(int).tolist())
for k in range(len(L["lt"])):
    s, Y = IF.state_s(I, L["lt"][k], L["ly"][:, k])
    I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if k in sel:
        ph = np.abs(IF.phi_at(I, s, Y)); j = 1 + int(np.nanargmax(ph[1:]))
        print("k %3d lambda %.4f s %7.3f  max|phi| %.2e at x=%.3f" % (k, L["lt"][k], s, ph[j], I.xn[j]), flush=True)
