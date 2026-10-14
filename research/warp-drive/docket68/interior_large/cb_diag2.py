"""the Jacobian's spectrum at the s = -0.5 state, old rows against the new rows with F_s plain and with F_xs(1) along the
flow (d = 1e-3); and the directional-derivative consistency of each"""
import numpy as np, pickle, time
import interior_damp as ID, interior_cb as CB
P = pickle.load(open("hr_28_1_4_s.pkl", "rb")); b, Nx = P["b"], P["Nx"]
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
Io = ID.Damped(Nx, b, st, P["kap"], P["at"]); Io.lastbr = ID.static_brane(b); m = Io.m
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Io.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if s <= -0.5:
        break
Ip = CB.DampedCB(Nx, b, st, P["kap"], P["at"]); Ip.lastbr = Io.lastbr.copy(); Ip.fs_mode = "plain"
If = CB.DampedCB(Nx, b, st, P["kap"], P["at"]); If.lastbr = Io.lastbr.copy(); If.fs_mode = "flow"
rng = np.random.default_rng(1); v = rng.standard_normal(Y.size) * np.abs(Y).mean()
for name, I in (("old", Io), ("cb plain", Ip), ("cb flow", If)):
    keep = I.lastbr.copy(); f0 = I.rhs(s, Y); out = []
    for eps in (1e-4, 1e-6, 1e-8):
        out.append(np.linalg.norm((I.rhs(s, Y + eps * v) - f0) / eps)); I.lastbr = keep
    J = np.empty((Y.size, Y.size))
    for j in range(Y.size):
        e = np.zeros(Y.size); h = 1e-7 * max(1.0, abs(Y[j])); e[j] = h
        J[:, j] = (I.rhs(s, Y + e) - f0) / h; I.lastbr = keep
    ev = np.linalg.eigvals(J)
    print("%-9s |Jv| at eps 1e-4/1e-6/1e-8: %.6e %.6e %.6e | eig: max|.| %.3e, Re max %+.3e, Re min %+.3e "
          "(growth toward decreasing s: %.3e)" % (name, *out, np.abs(ev).max(), ev.real.max(), ev.real.min(),
                                                   -ev.real.min()), flush=True)
    np.save("cbdiag2_ev_%s.npy" % name.replace(" ", "_"), ev)
