import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import Across, C, cp2, FUNCS
DT = cp2.DT
SC = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
p = dict(bt=2.0, mu=0.843 / 8, lam=64.0)
C()
tag = sys.argv[1]; ds = float(sys.argv[2]); smax_in = float(sys.argv[3]); base = int(sys.argv[4]); per = float(sys.argv[5])
smin = -0.1
A = Across(24, 20, smin)
U = np.load(SC + "across_-0.10_Ns24.npy")
rows = []
while True:
    T, Aa, B, F, S, P = (A.field(U, m) for m in range(6))
    xi = np.abs(C()["xi2"](*([A.sg, A.xg, 2.0, p["mu"], 64.0] + A.jets(U))).reshape(A.Ns + 1, 21))
    k = -1
    rec = (A.s[k], T[k, -1], Aa[k, -1], 2 * np.sqrt(abs(S[k, -1])) / (1 - A.s[k]), P[k, -1], T[k].min(),
           A.x[np.argmin(T[k])], np.nanmax(xi[A.s < 0][:, 1:]))
    rows.append(rec)
    print("smin %+.3f (Ns %d): plane T %.5f A %.5f R %.5f P %+.5f | min_x T %.5f @x=%.2f | interior xi2 max %.1e" % (
        (rec[0], A.Ns) + rec[1:]), flush=True)
    np.save(SC + "deep_%s_rows.npy" % tag, np.array(rows))
    if smin <= -smax_in + 1e-9:
        break
    snew = smin - ds
    Nn = int(base + per * abs(snew))
    An = Across(Nn, 20, snew)
    inside = An.s >= smin
    M = DT.interp_matrix(A.s, An.s[inside])
    Ds = A.D["_X"][::21, ::21] if False else None
    t, Dt = cp2.cheb01(A.Ns); Ds1 = -Dt / (1 - A.smin)
    parts = []
    for m in range(6):
        Fm = A.field(U, m)
        G = np.zeros((An.Ns + 1, 21))
        G[inside] = M @ Fm
        f0, f1, f2 = Fm[-1], (Ds1 @ Fm)[-1], (Ds1 @ Ds1 @ Fm)[-1]
        d = (An.s[~inside] - smin)[:, None]
        G[~inside] = f0 + f1 * d + 0.5 * f2 * d**2
        parts.append(G.ravel())
    Ug = np.concatenate(parts)
    t0 = time.time()
    try:
        Un, r, it = An.solve(Ug, p, quiet=True, maxit=30, tol=1e-9)
    except np.linalg.LinAlgError:
        print("singular at smin %.3f" % snew); break
    print("   solved to %+.3f: |R| %.1e in %d its (%.0fs)" % (snew, r, it, time.time() - t0), flush=True)
    if not np.isfinite(r) or r > 1e-6:
        print("stopped: no convergence at smin %.3f" % snew); break
    A, U, smin = An, Un, snew
    np.save(SC + "deep_%s_s%.3f.npy" % (tag, smin), U)
