"""along an interior_cb run's checkpoint: phi~ with the constraint row's brane slope, where it peaks, the largest of the
last three Chebyshev coefficients of each field (relative), at target s"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, interior_cb as CB
from cheb_tail_fn import cheb
P = pickle.load(open(sys.argv[1], "rb")); targets = [float(v) for v in sys.argv[2:]]
b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
mode = P["mode"]
if mode == "damped":
    I = CB.DampedCB(Nx, b, st, P["kap_driven"], P["at"])
elif mode == "gauge3":
    I = CB.GaugeCB(Nx, b, st, P["kap_driven"], P["at"], P["mu"], P["s1"], P["Nst"], P["ramp"], 0.0)
elif mode == "harm":
    I = CB.HarmCB(Nx, b, st, P["kap_driven"], P["at"], P["s1"], P["ramp"])
else:
    I = CB.Gauge5CB(Nx, b, st, P["kap_driven"], P["at"], P["mu"], P["s1"], P["Nst"], P["ramp"], "mean")
I.lastbr = ID.static_brane(b); m = I.m
for k in range(len(P["t"])):
    I.brane_values(P["t"][k], P["y"][:5 * m, k].reshape(5, m), P["y"][5 * m:, k].reshape(5, m))
print("%s mu %g Nx %d; checkpoint to s %.3f" % (mode, P["mu"], Nx, 1 - np.exp(P["lt"][-1])))
for k in range(len(P["lt"])):
    s, Y = IF.state_s(I, P["lt"][k], P["ly"][:, k])
    I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and (s <= targets[0] or k == len(P["lt"]) - 1):
        targets.pop(0); keep = I.lastbr.copy()
        ph = np.abs(I.phi_t(s, Y)); Xg, Vg, a, Fxb = I.cb_args(s, Y); I.lastbr = keep
        j = 1 + int(np.nanargmax(ph[1:]))
        tl = " ".join("%s%.0e" % (n, np.max((cheb(Xg[e]) / cheb(Xg[e]).max())[-3:])) for e, n in enumerate("TSABF"))
        print("s %7.3f phi~ %.1e at x %.3f (next to brane %.1e)  tails %s" % (s, ph[j], I.xn[j], ph[-2], tl), flush=True)
