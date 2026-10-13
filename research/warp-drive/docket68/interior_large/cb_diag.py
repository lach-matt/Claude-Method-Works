"""why the new brane rows stall the stepper: noise in F_xs(1) against stiffness, at the s = -0.5 state of the damped
Nx = 28 run, the old rows (Damped) against the new (DampedCB)"""
import numpy as np, pickle, sys, time
import interior_damp as ID, interior_cb as CB
P = pickle.load(open("hr_28_1_4_s.pkl", "rb")); b, Nx = P["b"], P["Nx"]
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
Io = ID.Damped(Nx, b, st, P["kap"], P["at"]); Io.lastbr = ID.static_brane(b)
Ic = CB.DampedCB(Nx, b, st, P["kap"], P["at"]); m = Io.m
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Io.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if s <= -0.5:
        break
Ic.lastbr = Io.lastbr.copy()
Xf, Vf = Ic.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); Fxb = Ic.slope(s, Xf, Vf)
X0 = Ic.xss(s, Xf, Vf, Fxb, 0.0)
for d in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
    keep = Ic.lastbr.copy(); Y1 = Y + d * np.concatenate([Y[5 * m:], X0.ravel()])
    Xf1, Vf1 = Ic.brane_values(s + d, Y1[:5 * m].reshape(5, m), Y1[5 * m:].reshape(5, m))
    print("d %.0e  F_xs(1) = %.10f" % (d, (Ic.slope(s + d, Xf1, Vf1) - Fxb) / d)); Ic.lastbr = keep
r0 = Ic.rhs(s, Y); r0b = Ic.rhs(s, Y); print("rhs repeatable to %.1e" % np.max(np.abs(r0 - r0b)))
rng = np.random.default_rng(1); v = rng.standard_normal(Y.size) * np.abs(Y).mean()
for name, I in (("old", Io), ("cb", Ic)):
    keep = I.lastbr.copy(); f0 = I.rhs(s, Y)
    for eps in (1e-4, 1e-6, 1e-8):
        print("%-3s directional derivative eps %.0e: |J v| = %.6e" % (name, eps, np.linalg.norm((I.rhs(s, Y + eps * v)
                                                                                           - f0) / eps)))
        I.lastbr = keep
t0 = time.time()
for name, I in (("old", Io), ("cb", Ic)):
    keep = I.lastbr.copy(); f0 = I.rhs(s, Y); J = np.empty((Y.size, Y.size))
    for j in range(Y.size):
        e = np.zeros(Y.size); h = 1e-7 * max(1.0, abs(Y[j])); e[j] = h
        J[:, j] = (I.rhs(s, Y + e) - f0) / h; I.lastbr = keep
    ev = np.linalg.eigvals(J); i = np.argsort(-np.abs(ev))
    print("%-3s Jacobian: largest |eig| %.3e; most positive Re %.3e; most negative Re %.3e  (%.0f s)" % (
        name, np.abs(ev[i[0]]), ev.real.max(), ev.real.min(), time.time() - t0), flush=True)
    np.save("cbdiag_J_%s.npy" % name, J)
