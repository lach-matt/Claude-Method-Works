"""The static exterior of the C-metric test (gen_eqs_cm.py) by solver_fw.py's Newton, continued in the reference's
deformation eps from the exact chart (eps = 0, where T = S = A = B = 1, F = 0 is the solution), and checked against the
exact solution: at every grid point the exact (r, xc) recovered from the two Killing norms (cm_exact.py), the computed
Kretschmann scalar against the exact one there, the brane's xc against 0, the horizon's r against mu, and phi.
Arguments: tag N eps1 eps2 ...  (each solve starts from the previous; a solution is saved under C.static_file)."""
import os, sys
os.environ["PROB"] = sys.argv[1]
import numpy as np, sympy as sp, pickle
import core_fw as C, solver_fw as SF, cm_exact as M
tag, N = sys.argv[1], int(sys.argv[2]); epss = [float(v) for v in sys.argv[3:]]
E = M.Exact(tag); G = SF.setup(N, N); n = len(G["S"])
NM = [sp.Symbol(k) for k in C.names]
fg = sp.lambdify([C.s, C.x, C.bt] + NM, [C.ev(C._raw["metric"][k]) for k in ("gtt", "gpp")], "numpy")
fK = sp.lambdify([C.s, C.x, C.bt] + C.VARS, C.ev(pickle.load(open("kretsch_%s.pkl" % tag, "rb"))), "numpy",
                 cse=True)
U = np.concatenate([np.ones(4 * n), np.zeros(n)])
r_g, xc_g = E.chart(G["S"], G["X"])
for eps in epss:
    if os.path.exists(C.static_file(eps, N, N)):
        U = np.load(C.static_file(eps, N, N)); nr = np.abs(SF.residual_and_jac(G, U, eps, False)[0]).max()
    else:
        U, nr = SF.newton(G, U, eps)
        if nr < 1e-8:
            np.save(C.static_file(eps, N, N), U)
    vals = SF.dv(G, U)
    with np.errstate(all="ignore"):
        gt, gp = [np.asarray(v, dtype=float) * np.ones(n) for v in fg(G["S"], G["X"], eps, *vals[0::6])]
        K = np.asarray(fK(G["S"], G["X"], eps, *vals), dtype=float) * np.ones(n)
    inner = np.where(G["S"] < 1 - 1e-12)[0]; r = np.full(n, np.nan); xc = np.full(n, np.nan)
    for i in inner:
        r[i], xc[i] = E.invert(gt[i], gp[i], r_g[i], xc_g[i], axis=abs(G["X"][i]) < 1e-14)
    r_g, xc_g = np.where(np.isfinite(r), r, r_g), np.where(np.isfinite(xc), xc, xc_g)
    dK = np.abs(K / E.K(r, xc) - 1); br = inner[np.abs(G["X"][inner] - 1) < 1e-14]
    s0 = inner[np.argmin(G["S"][inner])]                                    # the Radau row nearest the horizon
    near = inner[np.abs(G["S"][inner] - G["S"][s0]) < 1e-14]
    Uf = [U[e * n:(e + 1) * n] for e in range(5)]
    print("eps %.3f N %d |R| %.1e phi_max %.1e | T-1 in [%.3f, %.3f], F in [%.3f, %.3f] | max|K/Kex-1| %.1e | "
          "max|xc(brane)| %.1e | r/mu on the row s = %.4f: %.5f-%.5f" % (
              eps, N, nr, SF.phimax(G, U, eps), Uf[0].min() - 1, Uf[0].max() - 1, Uf[4].min(), Uf[4].max(),
              np.nanmax(dK[inner]), np.nanmax(np.abs(xc[br])), G["S"][s0], np.nanmin(r[near]) / E.mu,
              np.nanmax(r[near]) / E.mu), flush=True)
