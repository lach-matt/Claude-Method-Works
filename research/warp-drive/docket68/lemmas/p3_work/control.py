"""negative control: the uncharged hole (bt = 2) solved across its horizon and continued inward"""
import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import Across, C, cp2
DT = cp2.DT
SC = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
P2 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p2/"
p = dict(bt=2.0, mu=0.0, lam=0.0)
Uext = np.load(P2 + "E20_bt2_mu0.000.npy").reshape(6, 21, 21)
r20, _ = cp2.cheb01(20)
C()
def guess_from_ext(A):
    G = np.zeros((6, A.Ns + 1, 21))
    pos = A.s >= 0
    Mr = DT.interp_matrix(r20, np.sqrt(A.s[pos]))
    M0 = DT.interp_matrix(r20, np.array([0.0, 0.1]))
    for m in range(6):
        G[m, pos] = Mr @ Uext[m]
        f0, f1 = M0 @ Uext[m]
        G[m, ~pos] = f0[None, :] + ((f1 - f0) / 0.01)[None, :] * A.s[~pos][:, None]
    return G.ravel()
smin = -0.05
A = Across(24, 20, smin)
U, r, it = A.solve(guess_from_ext(A), p, quiet=True, maxit=40, tol=1e-9)
print("first: |R| %.1e (%d its)" % (r, it), flush=True)
base, per, ds, smax = 22, 40, 0.05, 3.0
while True:
    T, Aa, B, F, S, P = (A.field(U, m) for m in range(6))
    xi = np.abs(C()["xi2"](*([A.sg, A.xg, 2.0, 0.0, 0.0] + A.jets(U))).reshape(A.Ns + 1, 21))
    I0 = DT.interp_matrix(A.s, np.array([0.0]))
    R4 = 2 * np.sqrt((I0 @ S)[0, -1])
    Rk = 2 * np.sqrt(abs(S[-1, -1])) / (1 - A.s[-1])
    print("smin %+.3f (Ns %d): R4 %.5f | plane T %.5f A %.5f R %.5f  g_tt(phys) %.5f  Schw 2M/R-1 %.5f | xi2 int %.1e" % (
        A.s[-1], A.Ns, R4, T[-1, -1], Aa[-1, -1], Rk, abs(A.s[-1]) * T[-1, -1], R4 / Rk - 1,
        np.nanmax(xi[A.s < 0][:, 1:])), flush=True)
    if smin <= -smax + 1e-9:
        break
    snew = smin - ds
    An = Across(int(base + per * abs(snew)), 20, snew)
    inside = An.s >= smin
    M = DT.interp_matrix(A.s, An.s[inside])
    t, Dt = cp2.cheb01(A.Ns); Ds1 = -Dt / (1 - A.smin)
    parts = []
    for m in range(6):
        Fm = A.field(U, m); G = np.zeros((An.Ns + 1, 21)); G[inside] = M @ Fm
        f0, f1, f2 = Fm[-1], (Ds1 @ Fm)[-1], (Ds1 @ Ds1 @ Fm)[-1]
        d = (An.s[~inside] - smin)[:, None]; G[~inside] = f0 + f1 * d + 0.5 * f2 * d**2
        parts.append(G.ravel())
    try:
        Un, r, it = An.solve(np.concatenate(parts), p, quiet=True, maxit=30, tol=1e-9)
    except np.linalg.LinAlgError:
        print("singular at %.3f" % snew); break
    if not np.isfinite(r) or r > 1e-6:
        print("stopped at %.3f: |R| %.1e" % (snew, r)); break
    A, U, smin = An, Un, snew
    np.save(SC + "ctrl_s%.3f.npy" % smin, U)
