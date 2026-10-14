"""March a damped interior run in order (brane solve warm-started from the static brane values) and report, at
selected steps: proper time along s-lines, T, the DeTurck norm phi, the Kretschmann scalar, and the generalized Kasner
exponents p_i = K^i_i / tr K of the s = const slices (lapse and shift from g_ss, g_sx), with sum p^2 -> 1 marking the
vacuum Kasner approach."""
import numpy as np, pickle, sys
import core_fw as C, interior_fw as IF, interior_damp as ID, analyze_fw as AF

def fields_full(I, s, Y):
    m = I.m; Nx = I.Nx; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
    Xf, Vf = I.brane_values(s, Xi, Vi)
    DX = Xf @ I.D.T; DXX = Xf @ I.D2.T; DV = Vf @ I.D.T
    idx = np.arange(1, Nx + 1); xs = I.xn[idx]; k = len(idx); a = []
    for e in range(5):
        a += [Xf[e, idx], Vf[e, idx], DX[e, idx], np.zeros(k), DXX[e, idx], DV[e, idx]]
    bc = lambda L: np.array([np.broadcast_to(np.asarray(r, dtype=float), (k,)) for r in L])
    rest = bc(IF.f_rest(np.full(k, s), xs, I.b, *a))
    if I.kap:
        with np.errstate(all="ignore"):
            rest = rest + bc(ID.f_damp(np.full(k, s), xs, I.b, I.kap, I.at, *a))
    co = IF.f_coef(np.full(k, s), xs, I.b, *a)
    M = np.empty((k, 5, 5))
    for e in range(5):
        for q in range(5):
            M[:, e, q] = np.broadcast_to(np.asarray(co[e][q], dtype=float), (k,))
    Xp = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
    Xss = np.zeros_like(Xf); Xss[:, 1:] = Xp
    for e in range(5):
        Xss[e, 0] = C.bary_interp(I.xn[1:], Xp[e], [I.xn[0]])[0]
    return Xf, Vf, Xss

def kretschmann(I, s, Y):
    Xf, Vf, Xss = fields_full(I, s, Y); a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e], Xss[e], I.D2 @ Xf[e], I.D @ Vf[e]]
    with np.errstate(all="ignore"):
        return np.asarray(AF.fK()(np.full(I.Nx + 1, s), I.xn, I.b, *a), dtype=float)

def geometry(I, s, Xf, Vf):
    """lapse N, and the Kasner exponents (t, x, theta) at every node; the Lorentzian g_tt = -s T / Delta^2"""
    xn = I.xn; f = 1 - s; g = 2 - xn ** 2; Dl = 1 / I.b + (1 - xn ** 2) / f
    T, S, A, B, F = Xf; Ts, Ss, As, Bs, Fs = Vf
    DX = Xf @ I.D.T
    # metric pieces and their s-derivatives (product rule on the explicit s-dependence by finite difference)
    def pieces(sv, T, S, A, B, F):
        f = 1 - sv; Dl = 1 / I.b + (1 - xn ** 2) / f
        return (-sv * T / Dl ** 2, A / (f ** 4 * sv) / Dl ** 2, 4 * B / (f ** 2 * g) / Dl ** 2,
                xn * F / (2 * f ** 3) / Dl ** 2, xn ** 2 * g * S / f ** 2 / Dl ** 2)
    h = 1e-6
    p0 = pieces(s, T, S, A, B, F)
    p1 = pieces(s + h, T + h * Ts, S + h * Ss, A + h * As, B + h * Bs, F + h * Fs)
    gtt, gss, gxx, gsx, gth = p0
    dtt, dss, dxx, dsx, dth = [(b_ - a_) / h for a_, b_ in zip(p0, p1)]
    # x-derivatives
    ex = lambda q: I.D @ q
    with np.errstate(all="ignore"):
        N = np.sqrt(gsx ** 2 / gxx - gss); bx = gsx
        # D_i beta_j: tt -Gamma^x_tt beta_x = (1/2) g^xx d_x g_tt beta_x, theta the same; xx d_x b - Gamma^x_xx b
        Ktt = (-dtt + 2 * 0.5 / gxx * ex(gtt) * bx) / (2 * N)
        Kth = (-dth + 2 * 0.5 / gxx * ex(gth) * bx) / (2 * N)
        Kxx = (-dxx + 2 * (ex(bx) - 0.5 / gxx * ex(gxx) * bx)) / (2 * N)
        kt, kx, kth = Ktt / gtt, Kxx / gxx, Kth / gth
        tr = kt + kx + 2 * kth
        p = np.array([kt / tr, kx / tr, kth / tr])
    return N, p

def tau4(R4, R):
    """four-dimensional Schwarzschild, r0 = R4: proper time along t = const from the horizon to area radius R"""
    M = R4 / 2; eta = np.arccos(np.clip(1 - R / M, -1, 1))
    return np.pi * M - M * (eta - np.sin(eta))

def run(fn):
    P = pickle.load(open(fn, "rb")); b, Nx = P["b"], P["Nx"]
    st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
    I = ID.Damped(Nx, b, st, P.get("kap", 0.0), P.get("at", 0.0)); I.lastbr = ID.static_brane(b); m = I.m
    sel = set(np.linspace(0, len(P["t"]) - 1, 16).astype(int).tolist())
    U = np.load(st["file"]); n = 625; sn = C.radau01(24)
    R4 = b * np.sqrt(C.bary_interp(sn, U[n:2 * n].reshape(25, 25), [0.0])[0][-1])
    tau = np.zeros(Nx + 1); prev = None; rows = []
    for k in range(len(P["t"])):
        s, Y = P["t"][k], P["y"][:, k]
        Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
        N, p = geometry(I, s, Xf, Vf)
        if prev is not None:
            tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
        prev = (s, N)
        if k in sel:
            ph = IF.phi_at(I, s, Y); K = kretschmann(I, s, Y)
            sp2 = (p ** 2).sum(0) + p[2] ** 2
            rows.append(dict(s=s, tau=tau.copy(), T=Xf[0].copy(), phi=ph, K=K, p=p, sp2=sp2))
            Rb = np.sqrt(Xf[1, -1] / (1 - s) ** 2) * I.b         # the brane's area radius, x = 1, Delta = 1/bt
            print("s=%8.4f tau ax1 %.4f br %.4f Rb %.4f (4D %.4f) | T ax %.3e br %.3e | phi %.1e | K ax1 %.3e br "
                  "%.3e max %.3e | "
                  "p(ax1) %+.3f %+.3f %+.3f S2 %.3f | p(br) %+.3f %+.3f %+.3f S2 %.3f" % (
                      s, tau[1], tau[-1], Rb, tau4(R4, Rb), Xf[0, 0], Xf[0, -1], np.nanmax(np.abs(ph[1:])), K[1], K[-1],
                      np.nanmax(K[1:]), *p[:, 1], sp2[1], *p[:, -1], sp2[-1]), flush=True)
    return rows

if __name__ == "__main__":
    rows = run(sys.argv[1])
    pickle.dump(rows, open(sys.argv[1].replace(".pkl", "_an.pkl"), "wb"))
