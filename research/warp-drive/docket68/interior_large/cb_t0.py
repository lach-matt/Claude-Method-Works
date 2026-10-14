"""T0: along the undriven damped run, the brane slope of F set by xi^s = 0 against the slope of the plain Lobatto
interpolant (F(1) = 0), and phi under each representation of F's derivatives"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, interior_cb as CB
P = pickle.load(open(sys.argv[1], "rb")); b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = CB.DampedCB(Nx, b, st, P["kap"], P["at"]); I.lastbr = ID.static_brane(b); m = I.m
targets = [float(v) for v in sys.argv[2:]]
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and s <= targets[0]:
        targets.pop(0)
        Fx_plain = (I.D @ Xf[4])[Nx]; Fx_cb = I.slope(s, Xf, Vf)
        keep = I.lastbr.copy(); ph0 = np.abs(IF.phi_at(I, s, Y)); I.lastbr = keep
        ph1 = np.abs(I.phi_t(s, Y)); I.lastbr = keep
        print("s %7.3f  F_x(1): plain %+.6e  constraint row %+.6e  (diff %.1e)  max phi: plain %.1e (brane %.1e)  "
              "cb %.1e (brane %.1e)" % (s, Fx_plain, Fx_cb, Fx_cb - Fx_plain, np.nanmax(ph0[1:]), ph0[-1],
                                        np.nanmax(ph1[1:]), ph1[-1]), flush=True)
