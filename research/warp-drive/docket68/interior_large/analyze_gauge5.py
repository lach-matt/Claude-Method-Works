"""a gauge5_run.py checkpoint: the s-leg before the switch, then the lambda-leg under the one-function driver; brane
solve marched in order.  At selected steps: proper time along the s-lines since the horizon (near-axis node, mid,
brane), phi~, the Kretschmann scalar from the driven equations, the brane's area radius, the lapse per unit lambda.
The undriven s-leg's own proper time is integrated the same way, so the driven run can be set against the old chart."""
import numpy as np, pickle, sys
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_gauge5 as G5, analyze_damp as AD, analyze_fw as AF
P = pickle.load(open(sys.argv[1], "rb")); b, Nx = P["b"], P["Nx"]; nsel = int(sys.argv[2]) if len(sys.argv) > 2 else 24
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = G5.Gauge5(Nx, b, st, P["kap_driven"], P["at"], P["mu"], P["s1"], P["Nst"], P["ramp"], P["mode"])
I.lastbr = ID.static_brane(b); m = I.m; mid = Nx // 2

def fields_full(s, Y):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    DX = Xf @ I.D.T; DXX = Xf @ I.D2.T; DV = Vf @ I.D.T
    idx = np.arange(1, Nx + 1); xs = I.xn[idx]; k = len(idx); a = []
    for e in range(5):
        a += [Xf[e, idx], Vf[e, idx], DX[e, idx], np.zeros(k), DXX[e, idx], DV[e, idx]]
    bc = lambda L: np.array([np.broadcast_to(np.asarray(r, dtype=float), (k,)) for r in L])
    R, Rs = I.R(s); E, Es = I.E(s, Xf, Vf); ss = np.full(k, s)
    with np.errstate(all="ignore"):
        rest = bc(IF.f_rest(ss, xs, I.b, *a)) + bc(ID.f_damp(ss, xs, I.b, I.kap, I.at, *a))
        rest = rest - bc(G5.f_damph(ss, xs, I.b, I.kap, I.at, I.mu, E, R, *a))
        rest = rest + bc(G5.f_gauge(ss, xs, I.b, I.mu, E, Es, R, Rs, *a))
    co = IF.f_coef(ss, xs, I.b, *a)
    M = np.empty((k, 5, 5))
    for e in range(5):
        for q in range(5):
            M[:, e, q] = np.broadcast_to(np.asarray(co[e][q], dtype=float), (k,))
    Xp = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
    Xss = np.zeros_like(Xf); Xss[:, 1:] = Xp
    for e in range(5):
        Xss[e, 0] = C.bary_interp(I.xn[1:], Xp[e], [I.xn[0]])[0]
    return Xf, Vf, Xss

def kretschmann(s, Y):
    Xf, Vf, Xss = fields_full(s, Y); a = []
    for e in range(5):
        a += [Xf[e], Vf[e], I.D @ Xf[e], Xss[e], I.D2 @ Xf[e], I.D @ Vf[e]]
    with np.errstate(all="ignore"):
        return np.asarray(AF.fK()(np.full(Nx + 1, s), I.xn, I.b, *a), dtype=float)

tau = np.zeros(Nx + 1); prev = None
for k in range(len(P["t"])):                                   # the s-leg to the switch: proper time so far
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N, p = AD.geometry(I, s, Xf, Vf)
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
print("at the switch s1 = %.4f: proper time since the horizon ax %.4f mid %.4f br %.4f" % (P["s1"], tau[1], tau[mid],
                                                                                          tau[-1]))
seq = [IF.state_s(I, P["lt"][k], P["ly"][:, k]) for k in range(len(P["lt"]))]
targets = [float(v) for v in sys.argv[3:]] if len(sys.argv) > 3 else None
sel = set(np.linspace(0, len(seq) - 1, nsel).astype(int).tolist())
rows = []
for k, (s, Y) in enumerate(seq):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N, p = AD.geometry(I, s, Xf, Vf)
    tau += 0.5 * (N + prev[1]) * abs(s - prev[0]); prev = (s, N)
    hit = (targets and s <= targets[0]) if targets is not None else (k in sel)
    if hit:
        if targets:
            targets.pop(0)
        keep = I.lastbr.copy(); pht = I.phi_t(s, Y); K = kretschmann(s, Y); I.lastbr = keep
        Rb = np.sqrt(Xf[1, -1]) * b / (1 - s)
        rows.append(dict(s=s, tau=tau.copy(), K=K, phi=pht, N=N.copy(), Rb=Rb))
        print("s %7.3f | tau ax %.4f mid %.4f br %.4f | Nlam ax %.4f br %.4f | phi~ %.1e | K ax %.3e mid %.3e br %.3e "
              "max %.3e | Rb %.4f" % (s, tau[1], tau[mid], tau[-1], N[1] * (1 - s), N[-1] * (1 - s),
                                     np.nanmax(np.abs(pht[1:])), K[1], K[mid], K[-1], np.nanmax(K[1:]), Rb), flush=True)
pickle.dump(rows, open(sys.argv[1].replace(".pkl", "_an.pkl"), "wb"))
