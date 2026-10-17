import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import Across, cp2
from refslab import EvenRefSlab, CR, even_grid
DT = cp2.DT
SC = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
mu_ = float(sys.argv[1]); src, NsA, sminA = sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
sb, ds, Ns, Np, send, tag = (float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]),
                             float(sys.argv[9]), sys.argv[10])
gam = float(sys.argv[11]) if len(sys.argv) > 11 else 0.0
p = dict(bt=2.0, mu=mu_, lam=(64.0 if mu_ > 0 else 0.0), gam=gam)
CR()
A = Across(NsA, 20, sminA); U = np.load(SC + src)
t, Dt = cp2.cheb01(A.Ns); Ds = -Dt / (1 - A.smin)
xe, _, _ = even_grid(Np)
Mx = DT.interp_matrix(A.x, xe)
Mi = DT.interp_matrix(A.s, np.array([sb]))
V = [np.stack([Mx @ (Mi @ (np.linalg.matrix_power(Ds, k) @ A.field(U, m)))[0] for m in range(6)]) for k in range(3)]
print("start at s = %.3f, %d even nodes in x" % (sb, Np), flush=True)
rows = []
while sb > send + 1e-9:
    sa = sb - 2 * ds
    tt, _ = cp2.cheb01(Ns); sg = sb - (sb - sa) * tt; d = (sg - sb)[:, None]
    ref = np.stack([V[0][m] + V[1][m] * d + 0.5 * V[2][m] * d**2 for m in range(5)])
    S = EvenRefSlab(Ns, Np, sa, sb, V[0], V[1], ref)
    G = np.concatenate([(V[0][m] + V[1][m] * d + 0.5 * V[2][m] * d**2).ravel() for m in range(6)])
    t0 = time.time()
    try:
        Us, r, it = S.solve(G, p)
    except np.linalg.LinAlgError:
        print("singular at %.3f" % sa); break
    sh = sb - ds
    W = S.at(Us, sh)
    xi = S.xi2(Us, p); kk = S.s >= sh - 1e-12
    T, Aa, Sf, P = W[0][0], W[0][1], W[0][4], W[0][5]
    R = 2 * np.sqrt(abs(Sf[-1])) / (1 - sh)
    rec = (sh, T[-1], Aa[-1], R, abs(sh) * T[-1], P[-1], T.min(), S.x[np.argmin(T)], np.nanmax(xi[kk]), r, it,
           time.time() - t0)
    rows.append(rec)
    print("s %+.3f plane T %.5f A %9.4f R %.5f g_tt %.5f P %+.5f | min_x T %.5f @x=%.2f | xi2 %.1e |R| %.0e (%d, %.0fs)" % rec,
          flush=True)
    if not np.isfinite(r) or r > 1e-6:
        print("stopped: no convergence"); break
    V = list(W); sb = sh
    np.save(SC + "em_%s_rows.npy" % tag, np.array(rows))
    np.save(SC + "em_%s_last.npy" % tag, np.stack(V))
