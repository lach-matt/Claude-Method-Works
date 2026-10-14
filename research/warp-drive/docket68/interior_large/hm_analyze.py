"""along an interior_cb checkpoint: phi~ and where it peaks; the lapse N and N (1 - s); sqrt(gamma) of the s-slices and
N/sqrt(gamma) against the switch slice (constant along the normals in harmonic slicing; read here along the coordinate
lines, the shift reported); proper time since the horizon; the brane's area radius; the Kretschmann scalar at the
near-axis node, mid-bulk and the node next to the brane (X_ss from the evolution equations); Chebyshev tails"""
import numpy as np, pickle, sys
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_cb as CB, analyze_fw as AF
from cheb_tail_fn import cheb
P = pickle.load(open(sys.argv[1], "rb")); targets = [float(v) for v in sys.argv[2:]]
b, Nx = P["b"], P["Nx"]; st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24); mode = P["mode"]
cls = {"harm": CB.HarmCB, "harmold": CB.HarmOld}[mode]
I = cls(Nx, b, st, P["kap_driven"], P["at"], P["s1"], P["ramp"]); I.lastbr = ID.static_brane(b); m = I.m; mid = Nx // 2
def geo(s, Xg):
    x = I.xn; f = 1 - s; g = 2 - x ** 2; Dl = 1 / b + (1 - x ** 2) / f; T, S_, A, B, F = Xg
    gss = A / (f ** 4 * s) / Dl ** 2; gxx = 4 * B / (f ** 2 * g) / Dl ** 2; gsx = x * F / (2 * f ** 3) / Dl ** 2
    N = 1 / np.sqrt(-gxx / (gss * gxx - gsx ** 2))
    sg = np.sqrt(np.abs(s * T) / Dl ** 2 * gxx) * x ** 2 * g * S_ / f ** 2 / Dl ** 2
    return N, sg, np.abs(gsx) / np.sqrt(np.abs(gss) * gxx), np.sqrt(S_[-1]) * b / f
tau = np.zeros(Nx + 1); prev = None
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m)); N = geo(s, Xf)[0]
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
r0 = None
print("%s Nx %d s1 %.4f ramp %g; checkpoint to s %.3f; proper time at the switch ax %.4f mid %.4f br %.4f "
      "(old chart's totals 0.2658, 0.5185, 1.0723)" % (mode, Nx, P["s1"], P["ramp"], 1 - np.exp(P["lt"][-1]),
                                                    tau[1], tau[mid], tau[-1]))
for k in range(len(P["lt"])):
    s, Y = IF.state_s(I, P["lt"][k], P["ly"][:, k])
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    Fxb = I.slope(s, Xf, Vf); Xg = I.derivs(Xf, Vf, Fxb, None)[0]
    N, sg, sh, Rb = geo(s, Xg)
    tau += 0.5 * (N + prev[1]) * abs(s - prev[0]); prev = (s, N)
    if r0 is None:
        r0 = N / sg
    if targets and (s <= targets[0] or k == len(P["lt"]) - 1):
        targets.pop(0); keep = I.lastbr.copy()
        ph = np.abs(I.phi_t(s, Y)); j = 1 + int(np.nanargmax(ph[1:]))
        Xss_in = I.xss(s, Xf, Vf, Fxb, None); Xg2, Vg2, DX, DXX, DV = I.derivs(Xf, Vf, Fxb, None)
        Xss = np.zeros_like(Xg2); Xss[:, 1:Nx] = Xss_in
        for e in range(5):
            Xss[e, 0] = C.bary_interp(I.xn[1:Nx], Xss_in[e], [I.xn[0]])[0]
            Xss[e, Nx] = C.bary_interp(I.xn[1:Nx], Xss_in[e], [1.0])[0]
        a = []
        for e in range(5):
            a += [Xg2[e], Vg2[e], DX[e], Xss[e], DXX[e], DV[e]]
        with np.errstate(all="ignore"):
            K = np.asarray(AF.fK()(np.full(Nx + 1, s), I.xn, b, *a), dtype=float)
        I.lastbr = keep; q = (N / sg) / r0
        tl = max(np.max((cheb(Xg2[e]) / cheb(Xg2[e]).max())[-3:]) for e in range(5))
        print("s %7.3f phi~ %.1e (x %.2f) | N(1-s) ax %.4f mid %.4f br %.4f | sqrt g ax %.2e mid %.2e br %.2e | "
              "N/sqrt g rel ax %.3f mid %.3f br %.3f | tau ax %.4f mid %.4f br %.4f | Rb %.4f | K ax %.2e mid %.2e "
              "nbr %.2e | tail %.0e | shift %.2f" % (
                  s, ph[j], I.xn[j], N[1] * (1 - s), N[mid] * (1 - s), N[-1] * (1 - s),
                                              sg[1], sg[mid], sg[-1], q[1], q[mid], q[-1], tau[1], tau[mid], tau[-1],
                                              Rb, K[1], K[mid], K[Nx - 1], tl, np.nanmax(sh[1:])), flush=True)
