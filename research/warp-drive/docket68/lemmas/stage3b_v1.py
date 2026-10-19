#!/usr/bin/env python3
"""stage3b_v1.py -- item 450, the first rung of stage 3b's validation ladder (BOUNCE-RESEARCH section 17): global AdS5
recovered by the Einstein-DeTurck method, solved by spectral collocation and by finite differences, and the two
compared.  The chart is global AdS5 sliced as AdS2 x S^3 (standard), ds^2 = (1/cos^2 Y)[-cosh^2 X dt^2 + dX^2 + dY^2
+ sin^2 Y dOmega_2^2], whose conformal boundary Y = pi/2 is AdS2 x S^2 -- conformal to R x S^3 less two antipodal
worldlines, which sit at X -> +-inf -- the boundary stage 3's throat carries.  M: "1 - both, and compare", "3 - yes".
Labels: READ (the method, quoted in deturck2d.py), computed (sympy exact at sample points; numerical otherwise),
deduced.  Worked in the conversation; not verified; not seated.  2026-10-16.

  V0 (read) M's words: 450.
  V1 (computed) The unknowns: with w = 1 - cos Y and zeta = tanh(X/2) on the grid, ds^2 = (1-w)^-2 [-T cosh^2 X dt^2
     + A dX^2 + B dw^2/(w(2-w)) + 2F dX dw + S w(2-w) dOmega_2^2]; exact AdS5 is T = A = B = S = 1, F = 0.  The
     operator vanishes there against the undeformed reference; AdS5 pulled back by a diffeomorphism that keeps the
     ansatz has R_ab + 4 g_ab = 0; against the undeformed reference that pullback's E is O(1) (not vacuous).
  V2 (computed; deduced) The reference Tbar = 1 + e1 b, Abar = 1 + e2 b, Bbar = Sbar = 1 + e3 b, b = w(2-w)(1-w)^2
     sech^2 X, smooth at the axis and equal to AdS5 at the boundary.  At e3 = 0 the drive of xi along w depends on
     e1 + e2 alone and the drive along X vanishes, since d_X b = -2 b tanh X: at (e1, e2, e3) = (-3, 3, 0) the exact
     chart already has xi = 0 and is the solution.  The runs use (1, 0.5, -0.7), which drives both.
  V3 (computed) From a perturbed start with the undeformed reference, Newton returns to the exact chart to rounding
     on both discretizations: global AdS5 recovered from a perturbed start.
  V4 (computed) With the deformed reference, Newton converges quadratically to AdS5 in a gauge the reference
     chooses: max|B - 1| = 0.18; T, A, B, S even in X and F odd; xi^2, the Einstein residual and |K - 40| fall
     geometrically with N on the Chebyshev grid (K = R_abcd R^abcd = 40 for unit AdS5; for a static Einstein metric
     40 holds exactly when the Weyl tensor vanishes).
  V5 (computed) The comparison M asked for, both discretizations against a Chebyshev N = 28 solution interpolated to
     their nodes: finite differences converge at order 2.0 and 4.0; Chebyshev exponentially.  At N = 32 FD4 is at
     1.7e-5; Chebyshev reaches 1.3e-6 at N = 20, where FD4 needs N = 64 and about twelve times the time.
  V6 (computed; deduced) The chart matters.  In (tanh X, sin^2 Y) xi^2 falls only algebraically, its log-log slope
     constant at about 9; in (tanh(X/2), 1 - cos Y) the slope rises with N -- exponential -- and by N = 24 it is
     below the first.  It starts higher: sech^2 X is a polynomial in tanh X but has poles at +-i in tanh(X/2), which
     costs a constant, not a rate.  Deduced: the DeTurck solution carries odd powers of the defining
     function (cos Y at the boundary, e^-X at the poles), which the first chart's variables enter as square roots
     and the second's linearly; the axis is even in Y in both.
  V7 (deduced) V1 passes: AdS5 is recovered both ways, the two agree to the finite differences' truncation, and the
     chart of V6 and the open axis carry to V2, stage 3a's throat in this chart, which is reported to M first.

python3 stage3b_v1.py [--selftest | --mutants]
"""
import importlib.util
import math
import os
import re
import sys
import time

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ('"1 - both, and compare', '3 - yes"')
FUNCS = "TABFS"
ORDER = [(0, 0), (1, 1), (2, 2), (1, 2), (3, 3)]                          # paired with T, A, B, F, S
EREF = (1.0, 0.5, -0.7)
V6N = (12, 16, 20, 24)


def _load(name):
    spec = importlib.util.spec_from_file_location("s3b1_" + name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DT = _load("deturck2d")
X, u, th = DT.X, DT.u, DT.th
e1, e2, e3 = sp.symbols("e1 e2 e3")


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def metric(chart, T, A, B, F, S):
    """'w': w = 1 - cos Y; 'u': u = sin^2 Y (the variable is named u in both)"""
    g = sp.zeros(5, 5)
    W = 1 / (1 - u) ** 2 if chart == "w" else 1 / (1 - u)
    sw = u * (2 - u) if chart == "w" else u
    g[0, 0] = -W * T * sp.cosh(X) ** 2
    g[1, 1] = W * A
    g[2, 2] = W * B / (u * (2 - u)) if chart == "w" else W * B / (4 * u * (1 - u))
    g[1, 2] = g[2, 1] = W * F
    g[3, 3] = W * S * sw
    g[4, 4] = W * S * sw * sp.sin(th) ** 2
    return g


def bump(chart):
    """sin^2 Y cos^4 Y sech^2 X in either variable"""
    return (u * (2 - u) * (1 - u) ** 2 if chart == "w" else u * (1 - u) ** 2) / sp.cosh(X) ** 2


def norms(chart):
    """each equation over the factor that makes it smooth at the axis and O(1) at the boundary"""
    W = 1 / (1 - u) ** 2 if chart == "w" else 1 / (1 - u)
    guu = W / (u * (2 - u)) if chart == "w" else W / (4 * u * (1 - u))
    return {(0, 0): W * sp.cosh(X) ** 2, (1, 1): W, (2, 2): guu, (1, 2): W,
            (3, 3): W * (u * (2 - u) if chart == "w" else u)}


class Problem:
    def __init__(self, chart):
        self.chart, self.a = chart, (0.5 if chart == "w" else 1.0)
        J = DT.jetsyms(FUNCS)
        self.J = J
        self.g = metric(chart, *[J[f] for f in FUNCS])
        b = bump(chart)
        gbar = metric(chart, 1 + e1 * b, 1 + e2 * b, 1 + e3 * b, 0, 1 + e3 * b)
        lam = 3 if "lam3" in MUT else 4
        E, xi_up, _ = DT.operator(self.g, gbar if "no_deturck" not in MUT else self.g, FUNCS, Lam=lam)
        nm = norms(chart)
        self.eqs = [(E[k] / nm[k]).subs(th, sp.pi / 3) for k in ORDER]
        self.Ef = sp.lambdify([X, u, e1, e2, e3] + [J[f + j] for f in FUNCS for j in DT.JETS], self.eqs, "numpy",
                              cse=True)
        Es, _, _ = DT.operator(self.g, self.g, FUNCS)
        self.js = [J[f + j] for f in FUNCS for j in DT.JETS]
        self.args = [X, u, e1, e2, e3] + self.js
        xi2 = sum(self.g[a, c] * xi_up[a] * xi_up[c] for a in range(5) for c in range(5) if self.g[a, c] != 0)
        self.xi2f = sp.lambdify(self.args, xi2.subs(th, sp.pi / 3), "numpy", cse=True)
        self.einf = sp.lambdify(self.args, [(Es[k] / nm[k]).subs(th, sp.pi / 3) for k in ORDER], "numpy", cse=True)
        self.K = DT.kretschmann_builder(self.g, FUNCS, self.args)

    def solve(self, kind, order, N, ev, U0=None):
        ops = DT.Ops(N, N, kind, order, open_axis=True, a=self.a)
        nw = DT.Newton(list(FUNCS), self.eqs, [sp.Integer(0)] * 5, [1.0, 1.0, 1.0, 0.0, 1.0],
                       {e1: ev[0], e2: ev[1], e3: ev[2]}, ops)
        if U0 is None:
            U0 = np.concatenate([np.ones(ops.n)] * 3 + [np.zeros(ops.n), np.ones(ops.n)])
        t0 = time.time()
        U, hist = nw.solve(U0(ops) if callable(U0) else U0, maxit=25)
        jv = nw.jets(U)
        inner = (np.abs(ops.xg) < 1 - 1e-14) & (ops.ug < 1 - 1e-14)
        a = [ops.Xof(ops.xg[inner]), ops.ug[inner], ev[0], ev[1], ev[2]] + [v[inner] for v in jv]
        n = int(inner.sum())
        out = {"its": len(hist), "hist": hist, "secs": time.time() - t0,
               "xi2": float(np.max(np.abs(np.broadcast_to(self.xi2f(*a), (n,))))),
               "ein": float(max(np.max(np.abs(np.broadcast_to(r, (n,)))) for r in self.einf(*a))),
               "K40": float(np.max(np.abs(self.K(*a) - 40))),
               "dev": [float(np.max(np.abs(U[m * ops.n:(m + 1) * ops.n] - (0 if m == 3 else 1)))) for m in range(5)]}
        return ops, U, out


def pulled_back():
    """AdS5 under (X, w) -> (X + a, v) keeping the ansatz, the identity at w = 1 and X -> +-inf (chart w)"""
    a = sp.Rational(1, 5) * u * (2 - u) * (1 - u) ** 2 * sp.tanh(X) / sp.cosh(X) ** 2
    v = u + sp.Rational(3, 10) * u * (2 - u) * (1 - u) ** 2 / sp.cosh(X) ** 2
    Xp = X + a
    k = (1 - u) ** 2 / (1 - v) ** 2
    h = v * (2 - v)
    return {"T": k * sp.cosh(Xp) ** 2 / sp.cosh(X) ** 2,
            "A": k * (sp.diff(Xp, X) ** 2 + sp.diff(v, X) ** 2 / h),
            "B": k * (sp.diff(Xp, u) ** 2 + sp.diff(v, u) ** 2 / h) * u * (2 - u),
            "F": k * (sp.diff(Xp, X) * sp.diff(Xp, u) + sp.diff(v, X) * sp.diff(v, u) / h),
            "S": k * v * (2 - v) / (u * (2 - u))}


def v1_checks(P):
    """at sample points: E at the exact chart with the undeformed reference; R + 4 g at the pulled-back chart; E at
    the pulled-back chart with the undeformed reference (the last must not vanish)"""
    one = {"T": sp.Integer(1), "A": sp.Integer(1), "B": sp.Integer(1), "F": sp.Integer(0), "S": sp.Integer(1)}
    pb = pulled_back()
    pts = np.array([(0.3, 0.2), (-1.1, 0.55), (2.0, 0.9), (0.0, 0.05)])

    def jv(fd):
        out = []
        for f in FUNCS:
            for j in DT.JETS:
                d = fd[f]
                for ch in j[1:]:
                    d = sp.diff(d, X if ch == "X" else u)
                out.append(np.broadcast_to(sp.lambdify((X, u), d, "numpy")(pts[:, 0], pts[:, 1]), (len(pts),)))
        return out
    a1 = [pts[:, 0], pts[:, 1], 0.0, 0.0, 0.0] + jv(one)
    a2 = [pts[:, 0], pts[:, 1], 0.0, 0.0, 0.0] + jv(pb)
    worst = lambda rs: float(max(np.max(np.abs(np.broadcast_to(r, (len(pts),)))) for r in rs))
    return [worst(P.Ef(*a1)), worst(P.einf(*a2)), worst(P.Ef(*a2))]


def perturbed(ops):
    x, w = ops.xg, ops.ug
    b = w * (2 - w) * (1 - w) ** 2 * (1 - x ** 2) ** 2 / (1 + x ** 2) ** 2        # sech^2 X at zeta = tanh(X/2)
    return np.concatenate([1 + 0.3 * b, 1 - 0.2 * b, 1 + 0.25 * b, 0.15 * x * b, 1 - 0.3 * b])


def parity(ops, U):
    F = U.reshape(5, len(ops.x), len(ops.u))
    return max([np.max(np.abs(F[m] - F[m][::-1])) for m in (0, 1, 2, 4)] + [np.max(np.abs(F[3] + F[3][::-1]))])


def compare(ref, ref_ops, Uref, ops, U):
    Mx = DT.interp_matrix(ref_ops.x, ops.x)
    Mv = DT.interp_matrix(2 * ref_ops.u - 1, 2 * ops.u - 1)
    err = 0.0
    for m in range(5):
        Fr = Uref[m * ref_ops.n:(m + 1) * ref_ops.n].reshape(len(ref_ops.x), len(ref_ops.u))
        err = max(err, float(np.max(np.abs(U[m * ops.n:(m + 1) * ops.n] - (Mx @ Fr @ Mv.T).ravel()))))
    return err


def run(quiet=False):
    say = (lambda *a: None) if quiet else print
    res = {}
    P = Problem("w")
    res["v1"] = v1_checks(P)
    say("V1 exact AdS5 E %.1e; pulled-back R+4g %.1e; pulled-back vs undeformed reference %.1e" % tuple(res["v1"]))
    _, _, o = P.solve("cheb", 2, 12, (-3.0, 3.0, 0.0))
    res["v2"] = o["hist"][0]
    say("V2 (e1, e2, e3) = (-3, 3, 0): |E| at the exact chart %.1e" % res["v2"])
    res["v3"] = []
    for kind, order, N in (("cheb", 2, 16), ("fd", 2, 32), ("fd", 4, 32)):
        ops, U, o = P.solve(kind, order, N, (0.0, 0.0, 0.0), U0=perturbed)
        dev0 = float(np.max(np.abs(perturbed(ops) - np.concatenate([np.ones(ops.n)] * 3 + [np.zeros(ops.n),
                                                                                             np.ones(ops.n)]))))
        res["v3"].append((kind, order, N, dev0, max(o["dev"]), o["its"]))
        say("V3 %s%d N=%d: start off by %.3f, returned to within %.1e in %d iterations"
            % (kind, order, N, dev0, max(o["dev"]), o["its"]))
    ev = (0.0, 0.0, 0.0) if "no_deform" in MUT else EREF
    res["v4"] = []
    for N in V6N:
        ops, U, o = P.solve("cheb", 2, N, ev)
        res["v4"].append((N, o, parity(ops, U)))
        say("V4 cheb N=%d: %d its, |R| %.1e; xi^2 %.1e, Einstein %.1e, |K-40| %.1e; parity %.1e; max|B-1| %.3f"
            % (N, o["its"], o["hist"][-1], o["xi2"], o["ein"], o["K40"], parity(ops, U), o["dev"][2]))
    v4 = res["v4"]
    ref_ops, Uref, oref = P.solve("cheb", 2, 28, ev)
    res["v5"] = {}
    for kind, order, N in (("cheb", 2, 20), ("fd", 2, 16), ("fd", 2, 32), ("fd", 4, 16), ("fd", 4, 32)):
        ops, U, o = P.solve(kind, order, N, ev)
        res["v5"][(kind, order, N)] = (compare("ref", ref_ops, Uref, ops, U), o)
        say("V5 %s%d N=%d vs Chebyshev N=28: %.1e (%.1fs); xi^2 %.1e, |K-40| %.1e"
            % (kind, order, N, res["v5"][(kind, order, N)][0], o["secs"], o["xi2"], o["K40"]))
    Pu = Problem("u")
    res["v6"] = {"u": [Pu.solve("cheb", 2, N, EREF)[2]["xi2"] for N in V6N]}
    res["v6"]["w"] = res["v6"]["u"] if "half_chart" in MUT else [o["xi2"] for N, o, _ in v4]
    for name in ("u", "w"):
        say("V6 chart %s: xi^2 at N = 12, 16, 20, 24: %s" % ("(tanh X, sin^2 Y)" if name == "u" else
                                                               "(tanh(X/2), 1 - cos Y)",
                                                               ", ".join("%.1e" % x for x in res["v6"][name])))
    return res


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("V0 words: %s" % r)
    res = run(quiet)
    v1 = res["v1"]
    r = v1[0] < 1e-10 and v1[1] < 1e-10 and v1[2] > 0.1
    ok.append(r); say("V1 the operator on exact and pulled-back AdS5, not vacuous: %s" % r)
    r = res["v2"] < 1e-10
    ok.append(r); say("V2 the degenerate direction e1 + e2 = 0 (e3 = 0): %s" % r)
    r = all(d0 > 0.05 and d < 1e-10 and its <= 8 for (_, _, _, d0, d, its) in res["v3"])
    ok.append(r); say("V3 recovered from a perturbed start, both discretizations: %s" % r)
    v4 = res["v4"]
    geo = all(v4[i + 1][1][q] < v4[i][1][q] / 3 for i in range(3) for q in ("xi2", "ein", "K40"))
    r = (geo and all(o["its"] <= 8 and o["hist"][-1] < 1e-10 for _, o, _ in v4) and all(p < 1e-12 for _, _, p in v4)
         and v4[-1][1]["xi2"] < 1e-9 and v4[-1][1]["K40"] < 1e-3 and v4[-1][1]["dev"][2] > 0.1)
    ok.append(r); say("V4 converged, geometric in N, parity, nontrivial gauge (max|B-1| > 0.1): %s" % r)
    v5 = res["v5"]
    p2 = math.log2(v5[("fd", 2, 16)][0] / v5[("fd", 2, 32)][0])
    p4 = math.log2(v5[("fd", 4, 16)][0] / v5[("fd", 4, 32)][0])
    r = 1.7 < p2 < 2.3 and 3.6 < p4 < 4.4 and v5[("cheb", 2, 20)][0] < v5[("fd", 4, 32)][0] / 5
    ok.append(r); say("V5 FD orders %.2f and %.2f; Chebyshev N=20 below FD4 N=32: %s" % (p2, p4, r))
    slope = lambda v: [math.log(v[i] / v[i + 1]) / math.log(V6N[i + 1] / V6N[i]) for i in range(3)]
    su, sw = slope(res["v6"]["u"]), slope(res["v6"]["w"])
    r = (6 < min(su) and max(su) < 12 and max(su) / min(su) < 1.15
         and sw[1] > 1.25 * sw[0] and sw[2] > 1.15 * sw[1] and res["v6"]["w"][-1] < res["v6"]["u"][-1])
    ok.append(r); say("V6 log-log slopes %s in (tanh X, sin^2 Y), constant: algebraic; %s in (tanh(X/2), 1 - cos Y), "
                      "rising: exponential, and below the first at N = 24: %s"
                      % ("/".join("%.1f" % x for x in su), "/".join("%.1f" % x for x in sw), r))
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("lam3", "no_deturck", "no_deform", "half_chart")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"), flush=True)
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    run()
