#!/usr/bin/env python3
"""stage3b_v2.py -- item 451, the second rung of stage 3b's validation ladder (BOUNCE-RESEARCH section 18): stage 3a's
throat section inside the two-dimensional chart.  The boundary is AdS2 x S^2 with equal radii, as the extremal throat
carries, and the device's flux on the S^2.  The comparison flow is stage 3a's with AdS2 slices in place of its flat
ones, and the two-dimensional solve is the Einstein-DeTurck operator of deturck2d.py with the flux's stress as its
source.  M: "Yes to both 1 and 2".  Labels: READ (the method, in deturck2d.py; Maldacena and Milekhin 2008.06618 for
the model, in stage3a_throat.py), computed (sympy exact where marked; numerical otherwise), deduced.  Worked in the
conversation; not verified; not seated.  2026-10-16.

  W0 (read) M's words: 451.
  W1 (computed, exact) Einstein-Maxwell for ds^2 = drho^2 + e^{2 lam} ds^2(AdS2, unit) + e^{2 sig} dOmega_2^2 with
     F = B sin(theta) dtheta ^ dphi, derived from the metric: the AdS2 slices add e^{-2 lam} to the theta-theta and
     rho-rho equations and nothing to the slices' own, and with flat slices the system is stage 3a's.  Global
     AdS3 x S^2 at stage 3a's fixed point solves it exactly.
  W2 (computed; deduced) With flux the S^2 cannot close, so the flow is two-sided: symmetric about a centre where
     lam' = sig' = 0, AdS5 on both sides, the two AdS2 boundaries closing the field-line circle (MM's D^2 x S^2).  A
     centre above the fixed point reaches AdS5; below it the S^2 collapses.  The boundary ratio a/b of the AdS2 and S^2
     radii falls monotonically from infinity, so a/b = 1 fixes the centre: delta_c = sig_c - sig0 = 1.56e-2, 4.22e-3,
     1.22e-3 at lhat = 0.513, 0.193, 0.083, and 5.64e-10 at MM's 5.45e-6.  Deduced from the growing mode: delta_c goes
     as lhat^(k L3), k L3 -> sqrt(19/3) - 1 = 1.517; the computed local exponents climb 1.34, 1.47, 1.515.
  W3 (computed) The bridge: along the flow, sig'(sig) and lam'(sig) differ from stage 3a's planar flow by c lhat^2,
     c = 0.050 and 0.155, the same from lhat = 0.083 to 0.003.  Stage 3a's throat section is this flow's planar
     limit.
  W4 (computed, exact) The flow's Kretschmann scalar in closed form: 40 at AdS5, 12/L3^4 + 4 e^{-4 sig0} at the
     fixed point.
  W5 (computed) The two-dimensional solve, chart (tanh(X/2), Y) with Y in (-pi/2, pi/2), the reference built from
     stage 3a's fixed point (never from the answer), Dirichlet at Y = +-pi/2, the equations themselves at X = +-inf.
     With the undeformed reference, at lhat = 0.513, the solution is X-independent and symmetric in X and Y to
     rounding; from N = 24 to 32 xi^2 falls 1.5e-7 to 5.2e-11, the minimum S^2 radius comes within 2e-9 of the
     flow's, and K and R_s along the throat within 8e-4 and 4e-6 (6e-5 and 9e-7 at N = 40).  At lhat = 0.193, a
     longer throat, it converges the same way, more slowly: xi^2 6e-8 and the minimum radius within 2e-7 at N = 40.
  W6 (computed) With a deformed reference, reached by continuation in two steps, the solution depends on X (by 0.13)
     and every point's invariants lie on the one-dimensional curve: at N = 32 K within 3e-2 and R_s within 5e-5,
     both falling tenfold per eight in N.  From the undeformed start without continuation, Newton failed at a
     stronger deformation (recorded).
  W7 (computed) Finite differences beside Chebyshev on the undeformed problem: xi converges at orders 2.0 and 3.9,
     K at 2 and 4; at N = 64 FD4's minimum radius is off by 7e-6, Chebyshev's by 2e-9 at N = 32.
  W8 (deduced) V2 passes; V3 (MM's Einstein-static-universe wormhole, with the smooth boundary family) is next,
     reported to M first.

python3 stage3b_v2.py [--selftest | --mutants]
"""
import importlib.util
import math
import os
import re
import sys
import time

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ('"Yes to both 1 and 2"',)
FUNCS = "TABFS"
ORDER = [(0, 0), (1, 1), (2, 2), (1, 2), (3, 3)]                          # paired with T, A, B, F, S
LHATS = (0.513, 0.193, 0.083)


def _load(name):
    spec = importlib.util.spec_from_file_location("s3b2_" + name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DT = _load("deturck2d")
S3A = _load("stage3a_throat")
X, u, th = DT.X, DT.u, DT.th
e1, e2, e3 = sp.symbols("e1 e2 e3")


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


# ---------------------------------------------------------------------------------------------------- one dimension
def flow_equations():
    """Einstein-Maxwell for the throat ansatz with AdS2 (k = 1) or flat (k = 0) slices, from the metric (W1)"""
    t, x, ph, r = sp.symbols("t x phi rho")
    C = (t, x, th, ph, r)
    lam, sig = sp.Function("lam")(r), sp.Function("sig")(r)
    beta = sp.Symbol("beta")
    out = {}
    for k, warp in ((1, sp.cosh(x) ** 2), (0, sp.Integer(1))):
        g = sp.diag(-sp.exp(2 * lam) * warp, sp.exp(2 * lam), sp.exp(2 * sig), sp.exp(2 * sig) * sp.sin(th) ** 2, 1)
        gi = g.inv()
        G = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], C[c]) + sp.diff(g[d, c], C[b]) - sp.diff(g[b, c], C[d]))
                               for d in range(5)) / 2) for c in range(5)] for b in range(5)] for a in range(5)]

        def ric(a):
            return sp.simplify(sum(sp.diff(G[c][a][a], C[c]) for c in range(5)) - sum(sp.diff(G[c][a][c], C[a])
                                                                                       for c in range(5))
                               + sum(G[c][c][d] * G[d][a][a] for c in range(5) for d in range(5))
                               - sum(G[c][a][d] * G[d][a][c] for c in range(5) for d in range(5)))
        Rd = [ric(i) for i in range(5)]
        Rs = sp.simplify(sum(gi[i, i] * Rd[i] for i in range(5)))
        F2 = 2 * sp.exp(-4 * sig)
        res = {}
        for i, name in ((0, "tt"), (1, "xx"), (2, "thth"), (4, "rr")):
            T = (sp.exp(-2 * sig) if i == 2 else 0) - g[i, i] * F2 / 4
            res[name] = sp.simplify((Rd[i] - g[i, i] * Rs / 2 - 6 * g[i, i] - beta * T) / g[i, i])
        d = {sp.Derivative(lam, (r, 2)): sp.Symbol("lpp"), sp.Derivative(sig, (r, 2)): sp.Symbol("spp")}
        d2 = {sp.Derivative(lam, r): sp.Symbol("lp"), sp.Derivative(sig, r): sp.Symbol("sp"), sig: sp.Symbol("s"),
              lam: sp.Symbol("l")}
        out[k] = {n: sp.expand(sp.simplify(v.subs(d).subs(d2).rewrite(sp.exp))) for n, v in res.items()}
    return out


def w1():
    """the AdS2 term, stage 3a's system at k = 0, and global AdS3 x S^2 at the fixed point (exact)"""
    E = flow_equations()
    l = sp.Symbol("l")
    diff_ok = (sp.simplify(E[1]["xx"] - E[0]["xx"]) == 0 and sp.simplify(E[1]["tt"] - E[1]["xx"]) == 0
               and sp.simplify(E[1]["thth"] - E[0]["thth"] - sp.exp(-2 * l)) == 0
               and sp.simplify(E[1]["rr"] - E[0]["rr"] - sp.exp(-2 * l)) == 0)
    E3 = S3A.einstein_s2()
    subs3 = {sp.Symbol("lp"): sp.Symbol("lp"), sp.Symbol("sp"): sp.Symbol("sp")}
    same3a = all(sp.simplify(E[0][n] - E3[n].subs(subs3)) == 0 for n in ("tt", "thth", "rr"))
    # global AdS3 x S^2: sig = sig0, lam = log(L cosh(q)), q = rho/L, at y = e^{-2 sig0} with 4 y^2/lh^4 - y - 4 = 0
    q, lh = sp.symbols("q lhat", positive=True)
    y = (lh ** 4 + sp.sqrt(lh ** 8 + 64 * lh ** 4)) / 8
    L = 1 / sp.sqrt(3 + y / 4)
    sub = {sp.Symbol("s"): -sp.log(y) / 2, sp.Symbol("sp"): 0, sp.Symbol("spp"): 0, sp.Symbol("beta"): 6 / lh ** 4,
           sp.Symbol("lp"): sp.tanh(q) / L, sp.Symbol("lpp"): 1 / (L ** 2 * sp.cosh(q) ** 2),
           sp.Symbol("l"): sp.log(L * sp.cosh(q))}
    fp_ok = True
    for n in ("xx", "thth", "rr"):
        for qv, lv in ((0.3, 0.513), (1.7, 0.083), (-0.9, 0.193)):
            fp_ok &= abs(float(E[1][n].subs(sub).subs({q: qv, lh: lv}))) < 1e-10
    return diff_ok, same3a, fp_ok


def fp(lh):
    y, lp0, k = S3A.fixed_point(lh)
    return y, -0.5 * math.log(y), 1 / lp0, k


def rhs(r, z, beta, k=1):
    l, s, lp, sp_ = z
    kk = 0 if "flat" in MUT else k
    xx = -beta * math.exp(-4 * s) / 2 - lp * lp - 2 * lp * sp_ - 3 * sp_ * sp_ + 6 + math.exp(-2 * s)
    tt = beta * math.exp(-4 * s) / 2 - 3 * lp * lp - 2 * lp * sp_ - sp_ * sp_ + 6 - kk * math.exp(-2 * l)
    return [lp, sp_, (2 * tt - xx) / 3, (2 * xx - tt) / 3]


def constraint(z, beta, k=1):
    l, s, lp, sp_ = z
    return (beta * math.exp(-4 * s) / 2 + lp * lp + 4 * lp * sp_ + sp_ * sp_ - 6 - math.exp(-2 * s)
            + k * math.exp(-2 * l))


def shoot(lh, d):
    """the symmetric flow from a centre sig_c = sig0 + d; returns a/b, the solution, lam_c, sig_c"""
    y, s0, L3, _ = fp(lh)
    beta = 6 * lh ** -4
    sc = s0 + d
    q = 6 + math.exp(-2 * sc) - beta * math.exp(-4 * sc) / 2
    if q <= 0:
        return None
    lc = -0.5 * math.log(q)
    stop = lambda r, z, *a: (abs(z[2] - 1) + abs(z[3] - 1)) - 1e-10              # noqa: E731
    stop.terminal = True
    blow = lambda r, z, *a: abs(z[2]) + abs(z[3]) - 50                            # noqa: E731
    blow.terminal = True
    sol = solve_ivp(rhs, (0, 60), [lc, sc, 0.0, 0.0], args=(beta, 1), rtol=1e-13, atol=1e-14, method="DOP853",
                    events=(stop, blow), dense_output=True)
    z = sol.y[:, -1]
    return math.exp(z[0] - z[1]), sol, lc, sc


def centre(lh):
    f = lambda ld: math.log(shoot(lh, math.exp(ld))[0])                         # noqa: E731
    return math.exp(brentq(f, math.log(1e-14), math.log(0.2), xtol=1e-14, rtol=1e-14))


def planar(lh, eps=1e-9):
    """stage 3a's flow: from the fixed point along the growing mode, flat slices, lam' from the constraint"""
    y, s0, L3, k = fp(lh)
    beta = 6 * lh ** -4
    s, sp_ = s0 + eps, k * eps
    lp = -2 * sp_ + math.sqrt(3 * sp_ * sp_ + 6 + math.exp(-2 * s) - beta * math.exp(-4 * s) / 2)
    stop = lambda r, z, *a: (abs(z[2] - 1) + abs(z[3] - 1)) - 1e-10              # noqa: E731
    stop.terminal = True
    return solve_ivp(rhs, (0, 80), [0.0, s, lp, sp_], args=(beta, 0), rtol=1e-13, atol=1e-14, method="DOP853",
                     events=(stop,), dense_output=True)


def dense(sol, n=40000):
    return sol.sol(np.linspace(sol.t[0], sol.t[-1], n))


def bridge(lh):
    y, s0, L3, _ = fp(lh)
    _, sa, _, _ = shoot(lh, centre(lh))
    za, zp = dense(sa), dense(planar(lh))
    grid = np.linspace(s0 + 0.5, min(za[1, -1], zp[1, -1]) - 0.5, 2000)
    g = lambda z, j: np.interp(grid, z[1], z[j])                                 # noqa: E731
    return float(np.max(np.abs(g(za, 3) - g(zp, 3)))), float(np.max(np.abs(g(za, 2) - g(zp, 2))))


def k1d(l, s, lp, sp_, lpp, spp):
    """the flow's Kretschmann scalar (W4; derived in closed form from the metric, the AdS2 dependence cancelling)"""
    return (12 * lp ** 4 + 16 * lp ** 2 * lpp + 16 * lp ** 2 * sp_ ** 2 + 8 * lp ** 2 * np.exp(-2 * l) + 8 * lpp ** 2
            + 12 * sp_ ** 4 + 16 * sp_ ** 2 * spp - 8 * sp_ ** 2 * np.exp(-2 * s) + 8 * spp ** 2 + 4 * np.exp(-4 * s)
            + 4 * np.exp(-4 * l))


def oned(lh):
    """the a/b = 1 flow and its invariants along the outgoing branch"""
    d = centre(lh)
    _, sol, lc, sc = shoot(lh, d)
    r = np.linspace(0, sol.t[-1], 60000)
    z = sol.sol(r)
    beta = 6 * lh ** -4
    dz = np.array([rhs(rr, z[:, i], beta, 1) for i, rr in enumerate(r)]).T
    K = k1d(z[0], z[1], z[2], z[3], dz[2], dz[3])
    return dict(Rs=np.exp(z[1]), K=K, grad=(np.exp(z[1]) * z[3]) ** 2, sc=sc, lc=lc, d=d,
                cons=max(abs(constraint(z[:, i], beta)) for i in range(0, z.shape[1], 50)))


# ---------------------------------------------------------------------------------------------------- two dimensions
def chart(lh):
    """Y = pi (u - 1/2); the reference's warps from the fixed point: AdS3 x S^2 at the centre, AdS5 at the ends"""
    y, s0, L3, _ = fp(lh)
    cY, sY = sp.sin(sp.pi * u), -sp.cos(sp.pi * u)
    W = 1 / cY ** 2
    hA = sp.Float(L3 ** 2) * cY ** 2 + sY ** 2
    hS = sp.Float(math.exp(2 * s0)) * cY ** 2 + sY ** 2
    return W, hA, hS, cY


def metric(lh, T, A, B, F, S):
    W, hA, hS, cY = chart(lh)
    g = sp.zeros(5, 5)
    g[0, 0] = -W * T * hA * sp.cosh(X) ** 2
    g[1, 1] = W * A * hA
    g[2, 2] = W * B * sp.pi ** 2
    g[1, 2] = g[2, 1] = W * F * sp.pi
    g[3, 3] = W * S * hS
    g[4, 4] = W * S * hS * sp.sin(th) ** 2
    return g


class Problem:
    def __init__(self, lh):
        self.lh = lh
        beta = 0.0 if "no_flux" in MUT else 6 * lh ** -4
        J = DT.jetsyms(FUNCS)
        g = metric(lh, *[J[f] for f in FUNCS])
        W, hA, hS, cY = chart(lh)
        b = cY ** 2 / sp.cosh(X) ** 2
        gbar = metric(lh, 1 + e1 * b, 1 + e2 * b, 1 + e3 * b, 0, 1 + e3 * b)
        E, xi_up, _ = DT.operator(g, gbar, FUNCS)
        R2 = g[3, 3]
        sg = -1 if "src_sign" in MUT else 1
        # beta (T_ab - T g_ab/3) for F = sin(theta) dtheta^dphi: -g_ab/(3 R^4) off the sphere, 2/(3 R^2) on it
        src = {k: (-g[k] / (3 * R2 ** 2) if k != (3, 3) else sg * sp.Rational(2, 3) / R2) for k in ORDER}
        nm = {(0, 0): W * hA * sp.cosh(X) ** 2, (1, 1): W * hA, (2, 2): W * sp.pi ** 2, (1, 2): W * sp.pi,
              (3, 3): W * hS}
        self.eqs = [((E[k] - beta * src[k]) / nm[k]).subs(th, sp.pi / 3) for k in ORDER]
        self.J = J
        self.args = [X, u, e1, e2, e3] + [J[f + j] for f in FUNCS for j in DT.JETS]
        xi2 = sum(g[a, c] * xi_up[a] * xi_up[c] for a in range(5) for c in range(5) if g[a, c] != 0)
        self.xi2f = sp.lambdify(self.args, xi2.subs(th, sp.pi / 3), "numpy", cse=True)
        self.K = DT.kretschmann_builder(g, FUNCS, self.args)
        D = DT.make_D(FUNCS, J)
        gi = DT.inverse(g)
        dR = [D(R2, c) for c in range(5)]
        grad = sum(gi[a, c] * dR[a] * dR[c] for a in range(5) for c in range(5) if gi[a, c] != 0) / (4 * R2)
        self.Rsf = sp.lambdify(self.args, sp.sqrt(R2), "numpy")
        self.gradf = sp.lambdify(self.args, grad.subs(th, sp.pi / 3), "numpy", cse=True)

    def solve(self, kind, order, N, ev, U0=None, maxit=30):
        ops = DT.Ops(N, N, kind, order, open_axis=False, a=0.5)
        bv = [1.0, 1.0, 1.0, 0.0, 1.0]
        axis = [self.J[f] - bv[i] for i, f in enumerate(FUNCS)]           # u = 0 is the second boundary
        nw = DT.Newton(list(FUNCS), self.eqs, axis, bv, {e1: ev[0], e2: ev[1], e3: ev[2]}, ops)
        nw.xdirichlet = "x_dirichlet" in MUT
        if U0 is None:
            U0 = np.concatenate([np.ones(ops.n)] * 3 + [np.zeros(ops.n), np.ones(ops.n)])
        t0 = time.time()
        U, hist = nw.solve(U0, maxit=maxit)
        jv = nw.jets(U)
        inner = (ops.ug > 1e-14) & (ops.ug < 1 - 1e-14) & (np.abs(ops.xg) < 1 - 1e-14)
        a = [ops.Xof(ops.xg[inner]), ops.ug[inner], ev[0], ev[1], ev[2]] + [v[inner] for v in jv]
        n = int(inner.sum())
        bc = lambda f: np.broadcast_to(np.asarray(f, dtype=float), (n,))           # noqa: E731
        return ops, U, dict(hist=hist, secs=time.time() - t0, xi2=float(np.max(np.abs(bc(self.xi2f(*a))))),
                            K=bc(self.K(*a)), Rs=bc(self.Rsf(*a)), grad=bc(self.gradf(*a)))

    def continued(self, N, tgt, steps, kind="cheb", order=2):
        ops, U, o = self.solve(kind, order, N, (0.0, 0.0, 0.0))
        its = [len(o["hist"])]
        for i in range(1, steps + 1):
            ops, U, o = self.solve(kind, order, N, tuple(c * i / steps for c in tgt), U0=U)
            its.append(len(o["hist"]))
        o["its"] = its
        return ops, U, o


def against(o, one):
    """each point's invariants against the one-dimensional curve, parametrised by |grad R_s|^2 (monotone on the
    branch and linear in rho^2 at the centre, where R_s itself is not a good parameter)"""
    g1 = one["grad"]
    ok = o["grad"] < g1[-1] * 0.5
    Kp, Rp = np.interp(o["grad"], g1, one["K"]), np.interp(o["grad"], g1, one["Rs"])
    return float(np.max(np.abs(o["K"] - Kp)[ok])), float(np.max(np.abs(o["Rs"] - Rp)[ok]))


def shape(ops, U):
    nx, nu = len(ops.x), len(ops.u)
    Ug = U.reshape(5, nx, nu)
    xdep = max(np.max(np.abs(Ug[m] - Ug[m][nx // 2])) for m in range(5))
    par = max([np.max(np.abs(Ug[m] - Ug[m][::-1])) for m in (0, 1, 2, 4)] + [np.max(np.abs(Ug[3] + Ug[3][::-1]))]
              + [np.max(np.abs(Ug[m] - Ug[m][:, ::-1])) for m in (0, 1, 2, 4)]
              + [np.max(np.abs(Ug[3] + Ug[3][:, ::-1]))])
    return float(xdep), float(par)


# ---------------------------------------------------------------------------------------------------- the run
LH2 = 0.513                                    # the two-dimensional solves run at the plane's 10-ell mouth
EDEF = (0.2, 0.1, -0.15)                       # the deformed reference, reached in two continuation steps


def run(quiet=False, gate=None):
    """gate(stage, res), when given, is asked after each stage and ends the run on False (the mutants' fast fail)"""
    say = (lambda *a: None) if quiet else print
    go = (lambda st: gate is None or gate(st, res))                             # noqa: E731
    res = {"w1": w1()}
    say("W1 AdS2 term in theta-theta and rho-rho only; stage 3a's system at k = 0; global AdS3 x S^2 solves: %s"
        % (res["w1"],))
    if not go("w1"):
        return res
    res["w2"] = {}
    for lh in LHATS + (5.45e-6,):
        d = centre(lh)
        r, sol, lc, sc = shoot(lh, d)
        y, s0, L3, k = fp(lh)
        below = shoot(lh, -min(d, 1e-3))
        # below the fixed point the run ends on the blow-up event, sig' turned negative: the S^2 collapsing
        collapse = below is None or (len(below[1].t_events[1]) > 0 and below[1].y[3, -1] < 0)
        res["w2"][lh] = dict(d=d, ab=r, kL=k * L3, collapse=collapse,
                             above=[shoot(lh, d * f)[0] for f in (0.5, 2.0)])
        say("W2 lhat %-8g delta_c %.4e, a/b %.9f, a/b at delta_c/2 and 2 delta_c %.3f, %.3f; k L3 %.4f"
            % (lh, d, r, res["w2"][lh]["above"][0], res["w2"][lh]["above"][1], k * L3))
    if not go("w2"):
        return res
    res["w3"] = {lh: bridge(lh) for lh in (0.083, 0.03, 0.01)}
    for lh, (ds, dl) in res["w3"].items():
        say("W3 lhat %-6g max|d sig'| %.3e (/lhat^2 %.4f), max|d lam'| %.3e (/lhat^2 %.4f)"
            % (lh, ds, ds / lh ** 2, dl, dl / lh ** 2))
    if not go("w3"):
        return res
    one = oned(LH2)
    y, s0, L3, _ = fp(LH2)
    res["w4"] = (float(k1d(np.log(L3), s0, 0.0, 0.0, 1 / L3 ** 2, 0.0) - (12 / L3 ** 4 + 4 * math.exp(-4 * s0))),
                 float(one["K"][-1] - 40), one["cons"])
    say("W4 K at the fixed point's centre minus 12/L3^4 + 4e^-4sig0: %.1e; K at the flow's end minus 40: %.1e; "
        "the flow's constraint %.1e" % res["w4"])
    if not go("w4"):
        return res
    P = Problem(LH2)
    res["w5"] = {}
    for N in (24, 32):
        ops, U, o = P.solve("cheb", 2, N, (0.0, 0.0, 0.0))
        dK, dR = against(o, one)
        xdep, par = shape(ops, U)
        res["w5"][N] = dict(o=o, dK=dK, dR=dR, xdep=xdep, par=par, dmin=abs(o["Rs"].min() - math.exp(one["sc"])))
        say("W5 cheb N=%d: %d its, |R| %.1e; xi^2 %.1e; min R_s off the flow by %.1e; K %.1e, R_s %.1e along it; "
            "X-dependence %.1e, parity %.1e" % (N, len(o["hist"]), o["hist"][-1], o["xi2"], res["w5"][N]["dmin"],
                                                dK, dR, xdep, par))
    if not go("w5"):
        return res
    res["w6"] = {}
    for N in (24, 32):
        ops, U, o = P.continued(N, EDEF, 2)
        dK, dR = against(o, one)
        xdep, par = shape(ops, U)
        res["w6"][N] = dict(o=o, dK=dK, dR=dR, xdep=xdep, par=par, dmin=abs(o["Rs"].min() - math.exp(one["sc"])))
        say("W6 deformed, cheb N=%d: Newton %s, |R| %.1e; xi^2 %.1e; K %.1e, R_s %.1e on the flow; X-dependence %.3f, "
            "parity %.1e" % (N, o["its"], o["hist"][-1], o["xi2"], dK, dR, xdep, par))
    if not go("w6"):
        return res
    res["w7"] = {}
    for order in (2, 4):
        for N in (16, 32):
            ops, U, o = P.solve("fd", order, N, (0.0, 0.0, 0.0))
            dmin = abs(o["Rs"].min() - math.exp(one["sc"]))
            res["w7"][(order, N)] = dict(xi2=o["xi2"], dmin=dmin, its=len(o["hist"]), secs=o["secs"])
            say("W7 FD%d N=%d: xi^2 %.1e, min R_s off the flow by %.1e (%.0fs)" % (order, N, o["xi2"], dmin, o["secs"]))
    go("w7")
    return res


def _check(stage, res):
    """the selftest's verdict on one stage, and its line"""
    if stage == "w1":
        r = all(res["w1"])
        return r, "W1 exact: %s" % r
    if stage == "w2":
        w2 = res["w2"]
        r = (all(abs(v["ab"] - 1) < (1e-9 if lh > 1e-3 else 1e-5) for lh, v in w2.items())
             and all(v["above"][0] > 1 > v["above"][1] for v in w2.values())
             and all(v["collapse"] for v in w2.values())
             and abs(w2[0.513]["d"] - 1.5634e-2) < 2e-6 and abs(w2[0.083]["d"] - 1.2233e-3) < 2e-7)
        ex = [math.log(w2[a]["d"] / w2[b]["d"]) / math.log(a / b) for a, b in ((0.513, 0.193), (0.193, 0.083),
                                                                            (0.083, 5.45e-6))]
        r = r and ex[0] < ex[1] < ex[2] and abs(ex[2] - (math.sqrt(19 / 3) - 1)) < 5e-3
        return r, ("W2 two-sided, monotone a/b, collapse below, delta_c; exponents %s -> %.4f: %s"
                   % ("/".join("%.3f" % e for e in ex), math.sqrt(19 / 3) - 1, r))
    if stage == "w3":
        c = [(ds / lh ** 2, dl / lh ** 2) for lh, (ds, dl) in res["w3"].items()]
        r = all(abs(a - 0.050) < 2e-3 and abs(b - 0.155) < 4e-3 for a, b in c)
        return r, "W3 stage 3a's flow recovered at order lhat^2: %s" % r
    if stage == "w4":
        r = abs(res["w4"][0]) < 1e-10 and abs(res["w4"][1]) < 1e-6 and res["w4"][2] < 1e-9
        return r, "W4 the flow's Kretschmann at both ends, constraint held: %s" % r
    if stage == "w5":
        w5 = res["w5"]
        r = (all(len(v["o"]["hist"]) <= 8 and v["o"]["hist"][-1] < 1e-10 and v["xdep"] < 1e-12 and v["par"] < 1e-12
                 for v in w5.values())
             and w5[32]["o"]["xi2"] < w5[24]["o"]["xi2"] / 100 and w5[32]["o"]["xi2"] < 1e-9
             and w5[32]["dmin"] < 1e-7 and w5[32]["dK"] < 5e-3 and w5[32]["dR"] < 2e-5)
        return r, "W5 undeformed: X-independent, symmetric, geometric in N, on the flow: %s" % r
    if stage == "w6":
        w6 = res["w6"]
        r = (all(max(v["o"]["its"]) <= 8 and v["o"]["hist"][-1] < 1e-10 and v["xdep"] > 0.1 and v["par"] < 1e-12
                 for v in w6.values())
             and w6[32]["o"]["xi2"] < w6[24]["o"]["xi2"] / 30 and w6[32]["dK"] < w6[24]["dK"] / 5
             and w6[32]["dK"] < 0.05 and w6[32]["dR"] < 1e-4 and w6[32]["dmin"] < 1e-7)
        return r, "W6 deformed: X-dependent and on the flow pointwise: %s" % r
    w7, w5 = res["w7"], res["w5"]
    p2 = math.log2(w7[(2, 16)]["xi2"] / w7[(2, 32)]["xi2"]) / 2
    p4 = math.log2(w7[(4, 16)]["xi2"] / w7[(4, 32)]["xi2"]) / 2
    r = (1.7 < p2 < 2.4 and 3.3 < p4 < 4.5 and w7[(4, 32)]["dmin"] < w7[(2, 32)]["dmin"]
         and w5[32]["dmin"] < w7[(4, 32)]["dmin"] / 100)
    return r, "W7 FD orders (in xi) %.2f and %.2f; Chebyshev far below both at N = 32: %s" % (p2, p4, r)


def selftest(quiet=False):
    """quiet (the mutants) stops at the first failing stage; a run that stops short fails"""
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("W0 words: %s" % r)

    def gate(stage, res):
        r, line = _check(stage, res)
        ok.append(r)
        say(line)
        return r or not quiet
    run(quiet, gate)
    say("%d/%d" % (sum(ok), 8))
    return len(ok) == 8 and all(ok)


def mutants():
    caught = 0
    names = ("flat", "no_flux", "src_sign", "x_dirichlet")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-11s %s" % (m, "caught" if bad else "MISSED"), flush=True)
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    run()
