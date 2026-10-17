import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import Across, cp2
from acrossref import AcrossRef, chi, extend
from refslab import CR
DT = cp2.DT
SC = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
p = dict(bt=2.0, mu=0.105375, lam=64.0)
CR(False)
fw = np.array([1, 1, 1, 0, 1.0])
def report(B, U, tag):
    xi = B.xi2(U, p); T, Aa, S = B.field(U, 0), B.field(U, 1), B.field(U, 4)
    print("%s: interior xi2 max %.1e" % (tag, np.nanmax(xi[B.s < 0][:, 1:])), flush=True)
    for k in np.where(B.s < 0)[0][::-1][::max(1, B.Ns // 10)][::-1]:
        R = 2 * np.sqrt(abs(S[k, -1])) / (1 - B.s[k])
        print("    s %+.3f  R %.5f  g_tt %.5f  plane T %.5f A %.4f  xi2 %.1e" % (B.s[k], R, abs(B.s[k]) * T[k, -1], T[k, -1],
              Aa[k, -1], np.nanmax(xi[k, 1:])), flush=True)
A = Across(40, 20, -0.35); U = np.load(SC + "deep_b_s-0.350.npy")
smin, edge = -0.35, -0.30
while smin > -3.0:
    # 1. on the current domain, turn the solution-adapted reference on in stages
    sol = extend(A, U, A.s, edge)
    c = chi(A.s, -0.10, edge)[:, None]
    for eps in (0.25, 0.5, 0.75, 1.0):
        ref = np.stack([(1 - eps * c) * fw[m] + eps * c * sol[m] for m in range(5)])
        B = AcrossRef(A.Ns, 20, A.smin, ref)
        U, r, it = B.solve(U, p, quiet=True, maxit=25, tol=1e-8)
        print("  domain %.2f, eps %.2f: |R| %.1e (%d its)" % (A.smin, eps, r, it), flush=True)
        if r > 1e-5:
            break
    if r > 1e-5:
        print("stopped in the reference continuation"); break
    report(B, U, "re-referenced on [%.2f, 1]" % A.smin)
    # 2. extend the domain with the same reference, extrapolated
    snew = smin - 0.1
    Ns = int(26 + 40 * abs(snew))
    An = Across(Ns, 20, snew)
    G = extend(B, U, An.s, smin)
    refn = extend(B, np.concatenate([ref[m].ravel() for m in range(5)] + [U[5 * B.n:]]), An.s, smin)[:5]
    Bn = AcrossRef(Ns, 20, snew, refn)
    try:
        Un, r, it = Bn.solve(G.ravel(), p, quiet=True, maxit=25, tol=1e-8)
    except np.linalg.LinAlgError:
        print("singular extending to %.2f" % snew); break
    print("  extended to %.2f: |R| %.1e (%d its)" % (snew, r, it), flush=True)
    if r > 1e-5:
        print("stopped extending"); break
    report(Bn, Un, "extended")
    np.save(SC + "ar2_s%.3f.npy" % snew, Un); np.save(SC + "ar2_ref_s%.3f.npy" % snew, refn)
    xi = Bn.xi2(Un, p)
    good = [Bn.s[k] for k in range(Bn.Ns + 1) if Bn.s[k] < 0 and np.nanmax(xi[k, 1:]) < 1e-4]
    edge = min(good) if good else smin
    A, U, smin = Bn, Un, snew
    print("  trusted edge %.3f" % edge, flush=True)
