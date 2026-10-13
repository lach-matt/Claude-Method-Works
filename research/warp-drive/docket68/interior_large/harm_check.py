"""item 367 step 2's check: in pure harmonic slicing N / sqrt(gamma) is constant along the normals (Alcubierre
gr-qc/0210050 eq. (11)).  Along the old (DeTurck) damped Nx = 28 run: N, sqrt(gamma) of the s-slices (tau, x, theta,
phi; theta's sine dropped) and their ratio at the near-axis node, mid-bulk and the brane, along the coordinate lines
(the shift, g_sx proportional to x F, is reported beside it)"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, interior_gauge as IG
S = pickle.load(open(sys.argv[1], "rb")); L = pickle.load(open(sys.argv[2], "rb"))
targets = [float(v) for v in sys.argv[3:]]
b, Nx = S["b"], S["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, S["kap"], S["at"]); I.lastbr = ID.static_brane(b); m = I.m; mid = Nx // 2
def geo(s, Y):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    keep = I.lastbr.copy(); N, Fb = IG.lapse_and_Fbar(I, s, Y); I.lastbr = keep
    x = I.xn; f = 1 - s; g = 2 - x ** 2; Dl = 1 / b + (1 - x ** 2) / f
    T, S_, A, B, F = Xf
    gtt = np.abs(s * T) / Dl ** 2; gxx = 4 * B / (f ** 2 * g) / Dl ** 2; gth = x ** 2 * g * S_ / f ** 2 / Dl ** 2
    sg = np.sqrt(gtt * gxx) * gth
    shift = np.abs(x * F / (2 * f ** 3) / Dl ** 2) / np.sqrt(np.abs(A / (f ** 4 * s)) / Dl ** 2 * gxx)
    return N, sg, shift
seq = [(S["t"][k], S["y"][:, k]) for k in range(len(S["t"]))]
seq += [IF.state_s(I, L["lt"][k], L["ly"][:, k]) for k in range(1, len(L["lt"]))]
ref = None
for s, Y in seq:
    if not targets:
        break
    if s <= targets[0]:
        targets.pop(0); N, sg, sh = geo(s, Y)
        r = N / sg
        if ref is None:
            ref = r.copy()
        print("s %7.3f | N ax %.4f mid %.4f br %.4f | sqrt(gamma) ax %.3e mid %.3e br %.3e | (N/sqrt g)/(at s=-0.1) ax "
              "%.3f mid %.3f br %.3f | max |g_sx|/sqrt(g_ss g_xx) %.2e" % (
                  s, N[1], N[mid], N[-1], sg[1], sg[mid], sg[-1],
                                                                         (r / ref)[1], (r / ref)[mid], (r / ref)[-1],
                                                                         np.nanmax(sh[1:])), flush=True)
    else:
        Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
