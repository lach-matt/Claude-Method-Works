"""Along a gauge5_run.py checkpoint, at the target s values: phi~ and where it peaks, E, the lapse per unit lambda
against the switch slice's, N (1 - s) / (Nst (1 - s1)), at the axis, x = 1/2 and the brane, and the largest of the
last three Chebyshev coefficients of each field relative to its largest (the x-resolution test)."""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, interior_gauge5 as G5
from cheb_tail_fn import cheb
P = pickle.load(open(sys.argv[1], "rb")); targets = [float(v) for v in sys.argv[2:]]
b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = G5.Gauge5(Nx, b, st, P["kap_driven"], P["at"], P["mu"], P["s1"], P["Nst"], P["ramp"], P["mode"])
I.lastbr = ID.static_brane(b); m = I.m
for k in range(len(P["t"])):
    I.brane_values(P["t"][k], P["y"][:5 * m, k].reshape(5, m), P["y"][5 * m:, k].reshape(5, m))
jh = int(np.argmin(np.abs(I.xn - 0.5)))
print("mode %s mu %g kap %g Nx %d s1 %.4f; checkpoint reaches lambda %.4f (s %.3f)" % (
    P["mode"], P["mu"], P["kap_driven"], Nx, P["s1"], P["lt"][-1], 1 - np.exp(P["lt"][-1])))
for k in range(len(P["lt"])):
    s, Y = IF.state_s(I, P["lt"][k], P["ly"][:, k])
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if targets and (s <= targets[0] or k == len(P["lt"]) - 1):
        targets.pop(0)
        keep = I.lastbr.copy(); ph = np.abs(I.phi_t(s, Y)); I.lastbr = keep
        j = 1 + int(np.nanargmax(ph[1:])); N, Ns = I.lapse(s, Xf, Vf); E, Es = I.E(s, Xf, Vf)
        rat = N * (1 - s) / (I.Nst * (1 - I.s1))
        tl = " ".join("%s%.0e" % (n, np.max((cheb(Xf[e]) / cheb(Xf[e]).max())[-3:])) for e, n in enumerate("TSABF"))
        print("s %7.3f phi~ %.1e (x %.2f)  E %+.2e  N(1-s) ratio ax %.3f mid %.3f br %.3f  tails %s" % (
            s, ph[j], I.xn[j], E, rat[0], rat[jh], rat[-1], tl), flush=True)
