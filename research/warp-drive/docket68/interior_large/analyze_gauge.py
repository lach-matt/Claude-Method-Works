"""a driven run: the s-leg before the switch, then the lambda-leg under the lapse driver; brane solve marched in order.
At selected steps: u, proper time (near-axis node, mid, brane), phi~, K across x (from the driven equations), the
brane's area radius, the lapse per unit lambda, and the rescaled fields"""
import numpy as np, pickle, sys
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_gauge as IG, analyze_damp as AD, analyze_fw as AF
P = pickle.load(open(sys.argv[1], "rb")); b, Nx = P["b"], P["Nx"]; nsel = int(sys.argv[2]) if len(sys.argv) > 2 else 24
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I0 = ID.Damped(Nx, b, st, P["kap"], P["at"]); I0.lastbr = ID.static_brane(b); m = I0.m
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]
    I0.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
I = IG.Gauge(Nx, b, st, P["kap"], P["at"], P["mu"], P["s1"], P["Nst"]); I.lastbr = I0.lastbr.copy()

def fields_full(I, s, Y):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    DX = Xf @ I.D.T; DXX = Xf @ I.D2.T; DV = Vf @ I.D.T
    idx = np.arange(1, Nx + 1); xs = I.xn[idx]; k = len(idx); a = []
    for e in range(5):
        a += [Xf[e, idx], Vf[e, idx], DX[e, idx], np.zeros(k), DXX[e, idx], DV[e, idx]]
    bc = lambda L: np.array([np.broadcast_to(np.asarray(r, dtype=float), (k,)) for r in L])
    with np.errstate(all="ignore"):
        rest = bc(IF.f_rest(np.full(k, s), xs, I.b, *a)) + bc(ID.f_damp(np.full(k, s), xs, I.b, I.kap, I.at, *a))
        rest = rest + bc(IG.f_gauge(np.full(k, s), xs, I.b, I.mu, I.s1, I.Nst[idx], I.Nst_x[idx], *a))
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
        return np.asarray(AF.fK()(np.full(Nx + 1, s), I.xn, I.b, *a), dtype=float)

seq = [IF.state_s(I, P["lt"][k], P["ly"][:, k]) for k in range(len(P["lt"]))]
sel = set(np.linspace(0, len(seq) - 1, nsel).astype(int).tolist())
mid = Nx // 2; tau = np.zeros(Nx + 1); prev = None; rows = []
for k, (s, Y) in enumerate(seq):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N, p = AD.geometry(I, s, Xf, Vf)
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
    if k in sel:
        pht = IG.phi_tilde(I, s, Y); K = kretschmann(I, s, Y); u = 1 / (1 - s); Rb = np.sqrt(Xf[1, -1]) * u * b
        rows.append(dict(s=s, u=u, tau=tau.copy(), K=K, phi=pht, X=Xf.copy(), N=N.copy(), Rb=Rb))
        print("lam=%.3f s=%9.3f | tau+ ax %.4f mid %.4f br %.4f | Nlam ax %.4f br %.4f | phi~ %.1e | K ax %.3e mid %.3e "
              "br %.3e max %.3e | Rb %.4f | T ax %.3e br %.3e A ax %.3e br %.3e" % (
                  np.log(1 - s), s, tau[1], tau[mid], tau[-1], N[1] * (1 - s), N[-1] * (1 - s),
                  np.nanmax(np.abs(pht[1:])), K[1], K[mid], K[-1], np.nanmax(K[1:]), Rb, Xf[0, 0], Xf[0, -1],
                  Xf[2, 0], Xf[2, -1]), flush=True)
pickle.dump(rows, open(sys.argv[1].replace(".pkl", "_an.pkl"), "wb"))
