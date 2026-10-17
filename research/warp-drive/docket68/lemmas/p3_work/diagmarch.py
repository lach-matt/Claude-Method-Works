"""evenmarch with every slice kept and its curvature measured (P3 under 462)"""
import numpy as np, sys, time
P3 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
sys.path.insert(0, P3)
sys.path.insert(0, "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3e")
from across import Across, cp2
from refslab import EvenRefSlab, CR, even_grid
from p3curv import slice_K, jets_from_slice
DT = cp2.DT
OUT = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3e/"
mu_ = float(sys.argv[1]); src, NsA, sminA = sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
sb, ds, Ns, Np, send, tag = (float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]),
                             float(sys.argv[9]), sys.argv[10])
p = dict(bt=2.0, mu=mu_, lam=(64.0 if mu_ > 0 else 0.0), gam=0.0)
CR()
A = Across(NsA, 20, sminA); U = np.load(P3 + src)
t, Dt = cp2.cheb01(A.Ns); Ds = -Dt / (1 - A.smin)
xe, De, D2e = even_grid(Np)
Mx = DT.interp_matrix(A.x, xe)
Mi = DT.interp_matrix(A.s, np.array([sb]))
V = [np.stack([Mx @ (Mi @ (np.linalg.matrix_power(Ds, k) @ A.field(U, m)))[0] for m in range(6)]) for k in range(3)]


def measure(sv, V):
    J = jets_from_slice(V[0], V[1], V[2], De, D2e)
    K, g = slice_K(sv, xe, J)
    gtt = -g[:, 0, 0]
    r2 = np.sqrt(np.abs(g[:, 3, 3]))
    return K, gtt, r2


K0, g0, r0 = measure(sb, V)
print("start s %.3f, Np %d: K axis..plane %s" % (sb, Np, np.array2string(K0[[0, Np // 2, -1]], precision=3)), flush=True)
slices = [(sb, V[0], V[1], V[2], K0, g0, r0)]
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
        print("singular at %.3f" % sa, flush=True); break
    sh = sb - ds
    W = S.at(Us, sh)
    xi = S.xi2(Us, p); kk = S.s >= sh - 1e-12
    K, gtt, r2 = measure(sh, W)
    print("s %+.3f |R| %.0e xi2 %.1e | K axis %.4g mid %.4g plane %.4g max %.4g | g_tt axis %.4f plane %.4f | "
          "r_S2 plane %.4f | T axis %.4f plane %.4f | A axis %.3f plane %.3f (%.0fs)" % (
              sh, r, np.nanmax(xi[kk]), K[0], K[Np // 2], K[-1], K.max(), gtt[0], gtt[-1], r2[-1], W[0][0][0],
              W[0][0][-1], W[0][1][0], W[0][1][-1], time.time() - t0), flush=True)
    slices.append((sh, W[0], W[1], W[2], K, gtt, r2))
    np.save(OUT + "dm_%s.npy" % tag, np.array(slices, dtype=object), allow_pickle=True)
    if not np.isfinite(r) or r > 1e-6:
        print("stopped: no convergence", flush=True); break
    V = list(W); sb = sh
