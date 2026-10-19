"""P3 (a): the interior of P2's lam = 64 hole, r^2 -> -rho^2 in Figueras and Wiseman's chart."""
import importlib.util, os, sys, time
import numpy as np
import sympy as sp

L = "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas"
spec = importlib.util.spec_from_file_location("cp2", os.path.join(L, "corridor_p2.py"))
cp2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp2)
DT, X, u, th = cp2.DT, cp2.X, cp2.u, cp2.th
bt, mu, lam = cp2.bt, cp2.mu, cp2.lam
FUNCS, COMPS = cp2.FUNCS, cp2.COMPS


def metric_in(J, ref=False):
    """the chart inside the horizon: X is rho, r = i rho; every component real"""
    T, A, B, F, S = [sp.Integer(1) if ref else J[n] for n in "TABFS"]
    if ref:
        F = sp.Integer(0)
    f, gx = 1 + X**2, 2 - u**2
    w = 1 / ((f + bt * (1 - u**2)) / (bt * f))**2
    g = sp.zeros(5)
    g[0, 0] = w * X**2 * T
    g[1, 1] = -w * 4 * A / f**4
    g[2, 2] = w * 4 * B / (f**2 * gx)
    g[1, 2] = g[2, 1] = -w * X * u * F / f**3
    g[3, 3] = w * u**2 * gx * S / f**2
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    return g


def system_in():
    J = DT.jetsyms(FUNCS)
    g, gb = metric_in(J), metric_in(J, ref=True)
    E, xi_up, J = DT.operator(g, gb, FUNCS, COMPS, Lam=4)
    gi = DT.inverse(g)
    D = DT.make_D(FUNCS, J)
    src, F2, mx = cp2.maxwell_parts(g, gi, D, J["P_X"], J["P_u"], COMPS)
    inner = [(E[(0, 0)] - src[(0, 0)]) / g[0, 0], (E[(1, 1)] - src[(1, 1)]) / g[1, 1],
             (E[(2, 2)] - src[(2, 2)]) / g[2, 2], (E[(1, 2)] - src[(1, 2)]) / sp.sqrt(-g[1, 1] * g[2, 2]),
             (E[(3, 3)] - src[(3, 3)]) / g[3, 3], mx * g[0, 0]]
    T, A, B, F, S, P = [J[n] for n in FUNCS]
    jt = lambda n, d: J[n + d]
    nu_ = 1 / sp.sqrt(g[2, 2])
    K = {k: sp.Rational(1, 2) * nu_ * D(g[k], 2) for k in ((0, 0), (1, 1), (3, 3))}
    E2 = -J["P_X"]**2 / (g[0, 0] * g[1, 1])
    israel = [K[(0, 0)] / g[0, 0] - 1 + lam * E2 / 2, K[(1, 1)] / g[1, 1] - 1 + lam * E2 / 2,
              K[(3, 3)] / g[3, 3] - 1 - lam * E2 / 2]
    sqh = sp.sqrt(-g[0, 0] * g[1, 1]) * g[3, 3]
    div4 = D(sqh * J["P_X"] / (g[1, 1] * g[0, 0]), 1) / sqh
    maxb = J["P_u"] - (lam / 2) * sp.sqrt(g[2, 2]) * g[0, 0] * div4
    rows = dict(brane=[israel[0], israel[1], xi_up[2], F, israel[2], maxb],
                axis=[jt("T", "_u"), jt("A", "_u"), jt("B", "_u"), jt("F", "_u"), S - B, jt("P", "_u")])
    xi2 = sum(g[a, b] * xi_up[a] * xi_up[b] for a in range(5) for b in range(5) if g[a, b] != 0)
    sub = lambda e: e.subs(th, sp.pi / 3) if hasattr(e, "subs") else e
    args = [X, u, bt, mu, lam] + [sp.Symbol(f + j) for f in FUNCS for j in DT.JETS]
    lf = lambda e: sp.lambdify(args, sub(e), "numpy", cse=True)
    return dict(inner=[lf(e) for e in inner], brane=[lf(e) for e in rows["brane"]],
                axis=[lf(e) for e in rows["axis"]], xi2=lf(xi2), xi=[lf(xi_up[1]), lf(xi_up[2])])


if __name__ == "__main__":
    t0 = time.time()
    C = system_in()
    print("built in %.1f s" % (time.time() - t0))
