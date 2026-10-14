"""Chebyshev tails in x of each field along a driven run (gauge_run.py checkpoint) and along its undriven source run at
the same s: does the lapse driver lose x-resolution where the constraint grows?"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, interior_gauge as IG
from cheb_tail_fn import cheb
fn = sys.argv[1]; targets = [float(v) for v in sys.argv[2:]]
P = pickle.load(open(fn, "rb")); b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
S = pickle.load(open(P["src"], "rb"))
I0 = ID.Damped(Nx, b, st, P["kap"], P["at"]); I0.lastbr = ID.static_brane(b); m = I0.m
I = IG.Gauge(Nx, b, st, P.get("kap_driven", P["kap"]), P["at"], P["mu"], P["s1"], P["Nst"], P.get("ramp", 0.3), 0.0)
def tails(Xf):
    return "  ".join("%s %.1e" % (n, np.max((cheb(Xf[e]) / cheb(Xf[e]).max())[-3:])) for e, n in enumerate("TSABF"))
und = {}
tg = list(targets)
for k in range(len(S["t"])):                                     # the undriven run, brane marched in order
    s, Y = S["t"][k], S["y"][:, k]
    Xf, _ = I0.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if tg and s <= tg[0]:
        und[tg.pop(0)] = (s, tails(Xf), np.nanmax(np.abs(IF.phi_at(I0, s, Y)[1:])))
I0b = ID.Damped(Nx, b, st, P["kap"], P["at"]); I0b.lastbr = ID.static_brane(b)
for k in range(len(P["t"])):                                     # the driven run's own s-leg up to the switch
    I0b.brane_values(P["t"][k], P["y"][:5 * m, k].reshape(5, m), P["y"][5 * m:, k].reshape(5, m))
I.lastbr = I0b.lastbr.copy()
tg = list(targets)
for k in range(len(P["lt"])):
    s, Y = IF.state_s(I, P["lt"][k], P["ly"][:, k])
    Xf, _ = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    if tg and s <= tg[0]:
        t = tg.pop(0); pa = np.abs(IG.phi_tilde(I, s, Y)); j = 1 + int(np.nanargmax(pa[1:])); ph = pa[j]
        print("s %.3f driven   phi~ %.1e at x %.2f (brane %.1e)  last-3 max |c_k|/max: %s" % (
            s, ph, I.xn[j], pa[-1], tails(Xf)))
        if t in und:
            print("s %.3f undriven phi  %.1e  last-3 max |c_k|/max: %s" % (und[t][0], und[t][2], und[t][1]))
