"""proper time along the s-lines in the old (undriven) gauge, from the damped Nx = 28 s-leg and its lambda leg, to the
end of the trusted range; the remainder to s = -infinity from the lapse's power law fitted over the last unit of s"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, analyze_damp as AD
S = pickle.load(open(sys.argv[1], "rb")); L = pickle.load(open(sys.argv[2], "rb")); s_end = float(sys.argv[3])
b, Nx = S["b"], S["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, S["kap"], S["at"]); I.lastbr = ID.static_brane(b); m = I.m; mid = Nx // 2
tau = np.zeros(Nx + 1); prev = None; hist = []
def step(s, Y):
    global prev, tau
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N, p = AD.geometry(I, s, Xf, Vf)
    if prev is not None:
        tau = tau + 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N); hist.append((s, N.copy(), tau.copy()))
for k in range(len(S["t"])):
    step(S["t"][k], S["y"][:, k])
for k in range(1, len(L["lt"])):
    s, Y = IF.state_s(I, L["lt"][k], L["ly"][:, k])
    if s < s_end:
        break
    step(s, Y)
s_l = np.array([h[0] for h in hist]); Nn = np.array([h[1] for h in hist]); T = np.array([h[2] for h in hist])
w = s_l <= s_l[-1] + 1.0
for name, j in (("near-axis node", 1), ("mid", mid), ("brane", Nx)):
    p, c = np.polyfit(np.log(-s_l[w]), np.log(Nn[w, j]), 1)
    rem = Nn[-1, j] * abs(s_l[-1]) / (-p - 1) if p < -1 else float("inf")
    print("%-15s tau to s = %.3f: %.4f; lapse ~ |s|^%.2f over the last unit; remainder to -infinity %.4f; "
          "total %.4f" % (name, s_l[-1], T[-1, j], p, rem, T[-1, j] + rem))
