"""both legs of an hr_run (s-time, then lambda = -ln u), the brane solve marched in order; at selected steps: u, proper
time at the near-axis node, mid and brane, phi, K across x, the brane's area radius, and the rescaled fields"""
import numpy as np, pickle, sys
import interior_fw as IF, interior_damp as ID, analyze_damp as AD
P = pickle.load(open(sys.argv[1], "rb")); b, Nx = P["b"], P["Nx"]; nsel = int(sys.argv[2]) if len(sys.argv) > 2 else 24
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, P.get("kap", 0.0), P.get("at", 0.0)); I.lastbr = ID.static_brane(b); m = I.m
seq = [(P["t"][k], P["y"][:, k]) for k in range(len(P["t"]))]
if "lt" in P:
    seq += [IF.state_s(I, P["lt"][k], P["ly"][:, k]) for k in range(1, len(P["lt"]))]
sel = set(np.linspace(0, len(seq) - 1, nsel).astype(int).tolist())
mid = Nx // 2
tau = np.zeros(Nx + 1); prev = None; rows = []
for k, (s, Y) in enumerate(seq):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N, p = AD.geometry(I, s, Xf, Vf)
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
    if k in sel:
        ph = IF.phi_at(I, s, Y); K = AD.kretschmann(I, s, Y); u = 1 / (1 - s)
        Rb = np.sqrt(Xf[1, -1]) * u * b
        rows.append(dict(s=s, u=u, tau=tau.copy(), K=K, phi=ph, X=Xf.copy(), Rb=Rb, N=N.copy()))
        print("u=%.4f s=%9.3f tau ax %.4f mid %.4f br %.4f | phi %.1e | K ax %.3e mid %.3e br %.3e max %.3e | Rb %.4f |"
              " T/u ax %.4f br %.4f  A/u ax %.4f mid %.4f br %.4f  Su2 ax %.3f br %.3f  Bu2 br %.4f  Fu mid %.3f" % (
                  u, s, tau[1], tau[mid], tau[-1], np.nanmax(np.abs(ph[1:])), K[1], K[mid], K[-1], np.nanmax(K[1:]),
                  Rb, Xf[0, 0] / u, Xf[0, -1] / u, Xf[2, 0] / u, Xf[2, mid] / u, Xf[2, -1] / u, Xf[1, 0] * u * u,
                  Xf[1, -1] * u * u, Xf[3, -1] * u * u, Xf[4, mid] * u), flush=True)
pickle.dump(rows, open(sys.argv[1].replace(".pkl", "_an.pkl"), "wb"))
