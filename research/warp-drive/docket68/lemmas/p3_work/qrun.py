import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import Across, cp2
from across_q import AcrossQ, CQ
from acrossref import extend
DT = cp2.DT
SC = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
p = dict(bt=2.0, mu=0.105375, lam=64.0)
sm = float(sys.argv[1]); tag = sys.argv[2]
CQ()
# start: the FW-gauge solution on [-0.1, 1], its T and A rescaled into the q-chart (T -> T/q, A -> A q), then solved
A0 = Across(24, 20, -0.1); U0 = np.load(SC + "across_-0.10_Ns24.npy")
B = AcrossQ(24, 20, -0.1, sm)
q = (1 - ((1 - B.s) / (1 - sm))**3)[:, None]
G = np.stack([A0.field(U0, m) for m in range(6)]); G[0] = G[0] / q; G[1] = G[1] * q
U, r, it = B.solve(G.ravel(), p, quiet=True, maxit=30, tol=1e-8)
print("sm %.2f: first solve on [-0.1, 1]: |R| %.1e (%d its)" % (sm, r, it), flush=True)
smin = -0.1
while smin > sm + 0.02:
    snew = max(smin - 0.05, sm + 0.02)
    Ns = int(26 + 40 * abs(snew))
    Bn = AcrossQ(Ns, 20, snew, sm)
    Gn = extend(B, U, Bn.s, smin)
    try:
        Un, r, it = Bn.solve(Gn.ravel(), p, quiet=True, maxit=25, tol=1e-8)
    except np.linalg.LinAlgError:
        print("singular at %.3f" % snew); break
    xi = Bn.xi2(Un, p); T, Aa, S = Bn.field(Un, 0), Bn.field(Un, 1), Bn.field(Un, 4)
    qe = 1 - ((1 - snew) / (1 - sm))**3
    R = 2 * np.sqrt(abs(S[-1, -1])) / (1 - snew)
    print("to %+.3f (Ns %d): |R| %.1e (%d) | plane T %.4f A %.4f R %.5f g_tt %.5f | xi2 int %.1e" % (snew, Ns, r, it,
          T[-1, -1], Aa[-1, -1], R, abs(snew) * qe * T[-1, -1], np.nanmax(xi[Bn.s < 0][:, 1:])), flush=True)
    if not np.isfinite(r) or r > 1e-5:
        print("stopped"); break
    B, U, smin = Bn, Un, snew
    np.save(SC + "q_%s_s%.3f.npy" % (tag, smin), U)
