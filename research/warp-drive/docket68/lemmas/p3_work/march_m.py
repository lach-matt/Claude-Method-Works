"""P3m interior march (462): slabs in s, even in x, moving reference; plane rows 'evo' (xi^x = xi^s = 0) or 'ell'"""
import numpy as np, sys, time
sys.path.insert(0, "."); import p3m
from p3curv import slice_K, jets_from_slice
DT = p3m.DT
src, kap, sb, ds, Ns, Np, send, mode, tag = (sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]),
                                            int(sys.argv[5]), int(sys.argv[6]), float(sys.argv[7]), sys.argv[8], sys.argv[9])
p = dict(bt=2.0, kap=kap)
REG = len(sys.argv) > 11 and sys.argv[11] == "reg"
GAMV = float(sys.argv[12]) if len(sys.argv) > 12 else 0.0
p["gam"] = GAMV
NsG = int(sys.argv[10]) if len(sys.argv) > 10 else 38
G = p3m.Global(NsG, 20, -0.30); U = np.load(src)
xe, De, D2e = p3m.even_grid(Np)
Mx = DT.interp_matrix(G.x, xe); Mi = DT.interp_matrix(G.s, np.array([sb]))
V = [np.stack([Mx @ (Mi @ (np.linalg.matrix_power(G.Ds, k) @ G.field(U, m)))[0] for m in range(5)]) for k in range(3)]
if REG:                                    # S -> Sigma = (S - B)/x^2, on the even nodes (none at x = 0)
    for k in range(3):
        V[k][4] = (V[k][4] - V[k][2]) / xe**2
p3m.C(mode, True, REG, GAMV != 0)


def to_S(W):
    if not REG:
        return W
    W = [w.copy() for w in W]
    for k in range(3):
        W[k][4] = W[k][2] + xe**2 * W[k][4]
    return W


def measure(sv, V):
    W = [np.vstack([v, np.zeros((1, v.shape[1]))]) for v in V]          # P slot unused by slice_K
    J = jets_from_slice(W[0], W[1], W[2], De, D2e)
    K, g = slice_K(sv, xe, J)
    return K, -g[:, 0, 0], np.sqrt(np.abs(g[:, 3, 3]))


slices = []
print("start s %.3f, Np %d, mode %s" % (sb, Np, mode), flush=True)
while sb > send + 1e-9:
    sa = sb - 2 * ds
    tt, _ = p3m.cp2.cheb01(Ns); sg = sb - (sb - sa) * tt; d = (sg - sb)[:, None]
    ref = np.stack([V[0][m] + V[1][m] * d + 0.5 * V[2][m] * d**2 for m in range(5)])
    S = p3m.Slab(Ns, Np, sa, sb, V[0], V[1], ref, mode, REG, GAMV != 0)
    G0 = np.concatenate([(V[0][m] + V[1][m] * d + 0.5 * V[2][m] * d**2).ravel() for m in range(5)])
    t0 = time.time()
    try:
        Us, r, it = S.solve(G0, p, tol=1e-9, maxit=15)
    except np.linalg.LinAlgError:
        print("singular at %.3f" % sa, flush=True); break
    sh = sb - ds
    W = S.at(Us, sh)
    xi = S.xi2(Us, p); kk = S.s >= sh - 1e-12
    WS = to_S(W)
    K, gtt, r2 = measure(sh, WS)
    xprof = np.nanmax(xi[kk], axis=0)
    print("s %+.3f |R| %.0e (%d) | K axis %.4g plane %.4g | gKill axis %.4f plane %.4f | R_S2 plane %.4f | "
          "F plane %+.2e | T axis %.4f plane %.4f (%.0fs)" % (sh, r, it, K[0], K[-1], -gtt[0], -gtt[-1], r2[-1],
                                                            WS[0][3][-1], WS[0][0][0], WS[0][0][-1], time.time() - t0), flush=True)
    print("   xi2 by x: " + " ".join("%.0e" % v for v in xprof), flush=True)
    slices.append((sh, WS[0], WS[1], WS[2], K, gtt, r2, xprof))
    np.save("mm_%s.npy" % tag, np.array(slices, dtype=object), allow_pickle=True)
    if not np.isfinite(r) or r > 1e-6:
        print("stopped: no convergence", flush=True); break
    V = list(W); sb = sh
