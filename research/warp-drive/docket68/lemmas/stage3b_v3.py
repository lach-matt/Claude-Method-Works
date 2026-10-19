#!/usr/bin/env python3
"""stage3b_v3.py -- item 452, the third rung of stage 3b's validation ladder (BOUNCE-RESEARCH section 19): Maldacena and
Milekhin's Einstein-static-universe wormhole, the five-dimensional solution they sketch and leave ("It is possible to
describe the metric more explicitly and find the solution numerically, but we will not do it here", 2008.06618 section
3.2, READ).  In the throat's conformal units the boundary is two round S^3: the throat (AdS2 x S^2 with equal radii,
radius 1) and the exterior (the Einstein static universe, radius a/ell = d/(pi ell) = epsilon), joined at antipodal
mouths, which pinch to points when the mouths are small beside their separation (d >> r_e, MM's regime).  In V2's strip
chart the mouths are the chart's two ends and the only change from V2 is the exterior edge's time warp, 1/eps^2: at
eps = 1 V3 is V2.  M: "Yes to both".  Labels: READ (MM, quoted; the method, in deturck2d.py), computed (numerical),
deduced.  Worked in the conversation; not verified; not seated.  2026-10-16.

  U0 (read) M's words: 452.
  U1 (computed) At eps = 1 the solve is V2's, number for number.
  U2 (computed) Continuation in eps: Newton converges at every step; the solution depends on X (the AdS2 symmetry
     broken by the exterior) and is symmetric under the mouths' exchange X -> -X to rounding; xi^2 falls with N at
     fixed eps.
  U3 (computed; deduced) The interior is global AdS3 x S^2 closing the field-line circle, of conformal length
     L = pi(1 + eps) in the throat's time; the flux scale is uniform in this frame, so the lapse at the AdS3 centre
     should scale as (2 pi/L)^2, i.e. N^2(eps)/N^2(1) = (2/(1 + eps))^2.  Computed: within 0.69% at eps = 0.5 and
     2.07% at eps = 0.25 (lhat = 0.513), the deviation smooth in eps and converged in N (N = 32 and 40 agree to
     1e-5); at lhat = 0.193, a longer throat, 0.21% and 0.67%, smaller by 3.1-3.3 at every eps: the flow region's
     share, shrinking as the throat lengthens.
  U4 (computed; deduced) Along the mouths' symmetry line X = 0, a geodesic, the S^2's area doubles closer to the AdS3
     centre on the throat side than on the exterior side, the gap growing as L3 log(1/eps) (each boundary point's flow
     starts at a depth proportional to its own S^2 radius, 1 on the throat and eps on the exterior): 1.11 and 1.08
     times L3 log(1/eps) at eps = 0.5 and 0.25 for lhat = 0.513, 1.03 and 1.02 for lhat = 0.193.  MM's purple line
     (READ, Fig. 2).
  U5 (computed) Finite differences beside Chebyshev at eps = 0.5: FD2 at orders 2.2 and 2.0, FD4 at 4.1 and 4.4,
     against Chebyshev N = 40 (6.0e-2 to 3.1e-3 and 7.1e-2 to 2.0e-4 from N = 16 to 64).
  U6 (deduced; READ) The energy.  The AdS3 interior's classical energy is the two-dimensional CFT's Casimir energy
     (MM, READ), -pi c2/(6L) = -c2/(6(1 + eps)) in the throat's flat frame, with c2 = 3 L3/(2 G3) = 6 pi L3
     e^(2 sig0)/G5 at stage 3a's exact fixed point (Brown-Henneaux, READ via u1_bulk.py); the bulk's own AdS3 centre
     gives a c2 above it by the flow region's share, 5.5-11% at lhat = 0.513 and 1.5-2.5% at 0.193; MM's (2.11)
     -c2/(8 ell) is in their AdS2 frame and "includes a contribution due to the conformal anomaly in AdS2" (READ),
     not re-derived here; MM's (2.13)
     E_bind = -c2/(16 ell) is their extremisation with four-dimensional gravity, which a bulk with a fixed boundary
     does not contain.
  U7 (deduced) V3 passes: MM's sketch computed, its AdS3 interior and the 1/L law of its Casimir energy measured.

python3 stage3b_v3.py [--selftest | --mutants]
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
WORDS = ('"Yes to both"',)
LH = 0.513


def _load(name):
    spec = importlib.util.spec_from_file_location("s3b3_" + name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V2 = _load("stage3b_v2")
DT = V2.DT
X, u, th = DT.X, DT.u, DT.th
FUNCS, ORDER = V2.FUNCS, V2.ORDER
e1, e2, e3 = sp.symbols("e1 e2 e3")
EPS = sp.Symbol("eps", positive=True)


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def chart(lh):
    """V2's warps, and the exterior edge's time warp hT = eps^-(1 - sin Y): 1 on the throat, 1/eps^2 on the exterior"""
    W, hA, hS, cY = V2.chart(lh)
    sY = -sp.cos(sp.pi * u)
    if "no_hT" in MUT:
        hT = sp.Integer(1) + 0 * EPS
    elif "hT_up" in MUT:
        hT = sp.exp((1 - sY) * sp.log(EPS))
    else:
        hT = sp.exp(-(1 - sY) * sp.log(EPS))
    return W, hA, hS, hT


def metric(lh, T, A, B, F, S):
    W, hA, hS, hT = chart(lh)
    g = sp.zeros(5, 5)
    g[0, 0] = -W * T * hA * hT * sp.cosh(X) ** 2
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
        W, hA, hS, hT = chart(lh)
        b = sp.sin(sp.pi * u) ** 2 / sp.cosh(X) ** 2
        gbar = metric(lh, 1 + e1 * b, 1 + e2 * b, 1 + e3 * b, 0, 1 + e3 * b)
        E, xi_up, _ = DT.operator(g, gbar, FUNCS)
        R2 = g[3, 3]
        src = {k: (-g[k] / (3 * R2 ** 2) if k != (3, 3) else sp.Rational(2, 3) / R2) for k in ORDER}
        nm = {(0, 0): W * hA * hT * sp.cosh(X) ** 2, (1, 1): W * hA, (2, 2): W * sp.pi ** 2, (1, 2): W * sp.pi,
              (3, 3): W * hS}
        self.eqs = [((E[k] - beta * src[k]) / nm[k]).subs(th, sp.pi / 3) for k in ORDER]
        self.J = J
        self.args = [X, u, e1, e2, e3, EPS] + [J[f + j] for f in FUNCS for j in DT.JETS]
        xi2 = sum(g[a, c] * xi_up[a] * xi_up[c] for a in range(5) for c in range(5) if g[a, c] != 0)
        self.xi2f = sp.lambdify(self.args, xi2.subs(th, sp.pi / 3), "numpy", cse=True)
        self.K = DT.kretschmann_builder(g, FUNCS, self.args)
        self.lapse = sp.lambdify((X, u, EPS), W * hA * hT * sp.cosh(X) ** 2, "numpy")
        self.gS = sp.lambdify((u,), W * hS, "numpy")
        self.gYY = sp.lambdify((u,), W * sp.pi ** 2, "numpy")

    def solve(self, kind, order, N, eps, U0=None, maxit=30):
        ops = DT.Ops(N, N, kind, order, open_axis=False, a=0.5)
        bv = [1.0, 1.0, 1.0, 0.0, 1.0]
        axis = [self.J[f] - bv[i] for i, f in enumerate(FUNCS)]           # Y = -pi/2 is the exterior's boundary
        nw = DT.Newton(list(FUNCS), self.eqs, axis, bv, {e1: 0.0, e2: 0.0, e3: 0.0, EPS: eps}, ops)
        nw.xdirichlet = "x_dirichlet" in MUT
        if U0 is None:
            U0 = np.concatenate([np.ones(ops.n)] * 3 + [np.zeros(ops.n), np.ones(ops.n)])
        t0 = time.time()
        U, hist = nw.solve(U0, maxit=maxit)
        jv = nw.jets(U)
        inner = (ops.ug > 1e-14) & (ops.ug < 1 - 1e-14) & (np.abs(ops.xg) < 1 - 1e-14)
        a = [ops.Xof(ops.xg[inner]), ops.ug[inner], 0.0, 0.0, 0.0, eps] + [v[inner] for v in jv]
        n = int(inner.sum())
        bc = lambda f: np.broadcast_to(np.asarray(f, dtype=float), (n,))           # noqa: E731
        return ops, U, dict(hist=hist, secs=time.time() - t0, xi2=float(np.max(np.abs(bc(self.xi2f(*a))))),
                            jets=jv, inner=inner, eps=eps)

    def continued(self, kind, order, N, steps):
        U, out = None, []
        for eps in steps:
            ops, U, o = self.solve(kind, order, N, eps, U0=U)
            out.append((eps, ops, U, o))
        return out

    def centre(self, ops, U, eps):
        """on the symmetry line X = 0 (a geodesic): the lapse minimum, its S^2 radius, the local AdS3 radius from the
        Kretschmann scalar, and the proper distances to the doubling of the S^2 area on either side"""
        nx, nu = len(ops.x), len(ops.u)
        G = U.reshape(5, nx, nu)
        uf = np.linspace(0.004, 0.996, 4001)
        M = DT.interp_matrix(2 * ops.u - 1, 2 * uf - 1)
        T, B, S = (M @ G[0][nx // 2]), (M @ G[2][nx // 2]), (M @ G[4][nx // 2])
        n2 = T * self.lapse(0.0, uf, eps)
        ic = int(np.argmin(n2))
        Rs = np.sqrt(S * self.gS(uf))
        Rc = float(Rs[ic])
        ds = np.sqrt(B * self.gYY(uf)) * np.gradient(uf)

        def dist(rng):
            acc = 0.0
            for j in rng:
                acc += ds[j]
                if Rs[j] >= math.sqrt(2) * Rc:
                    return acc
            return float("nan")
        # the Kretschmann scalar at the grid node nearest the centre on X = 0, and the AdS3 radius it implies
        jv = [v.reshape(nx, nu)[nx // 2] for v in (ops.D[j] @ U[m * ops.n:(m + 1) * ops.n]
                                                   for m in range(5) for j in DT.JETS)]
        k = int(np.argmin(np.abs(ops.u - uf[ic])))
        K = float(np.asarray(self.K(*([np.array([0.0]), np.array([ops.u[k]]), 0.0, 0.0, 0.0, eps]
                                      + [np.array([v[k]]) for v in jv])))[0])
        Rk = math.sqrt(float((G[4][nx // 2][k]) * self.gS(np.array([ops.u[k]]))[0]))
        L3 = (12 / (K - 4 / Rk ** 4)) ** 0.25 if K > 4 / Rk ** 4 else float("nan")
        return dict(n2=float(n2[ic]), uc=float(uf[ic]), Rc=Rc, d_throat=dist(range(ic + 1, len(uf))),
                    d_ext=dist(range(ic - 1, -1, -1)), K=K, L3=L3)


# ---------------------------------------------------------------------------------------------------- the run
STEPS = (1.0, 0.8, 0.6, 0.5)


def shape(ops, U):
    nx, nu = len(ops.x), len(ops.u)
    G = U.reshape(5, nx, nu)
    xdep = max(np.max(np.abs(G[m] - G[m][nx // 2])) for m in range(5))
    par = max([np.max(np.abs(G[m] - G[m][::-1])) for m in (0, 1, 2, 4)] + [np.max(np.abs(G[3] + G[3][::-1]))])
    return float(xdep), float(par)


def compare(ref_ops, Uref, ops, U):
    Mx = DT.interp_matrix(ref_ops.x, ops.x)
    Mv = DT.interp_matrix(2 * ref_ops.u - 1, 2 * ops.u - 1)
    err = 0.0
    for m in range(5):
        Fr = Uref[m * ref_ops.n:(m + 1) * ref_ops.n].reshape(len(ref_ops.x), len(ref_ops.u))
        err = max(err, float(np.max(np.abs(U[m * ops.n:(m + 1) * ops.n] - (Mx @ Fr @ Mv.T).ravel()))))
    return err


def run(quiet=False, gate=None):
    say = (lambda *a: None) if quiet else print
    go = (lambda st: gate is None or gate(st, res))                             # noqa: E731
    res = {}
    y, s0, L3fp, _ = V2.fp(LH)
    res["fp"] = (s0, L3fp)
    P = Problem(LH)
    one = V2.oned(LH)
    ops, U, o = P.solve("cheb", 2, 24, 1.0)
    c = P.centre(ops, U, 1.0)
    res["u1"] = dict(xi2=o["xi2"], its=len(o["hist"]), Rc=c["Rc"], Rc1d=math.exp(one["sc"]), xdep=shape(ops, U)[0])
    say("U1 eps = 1, N = 24: %d its, xi^2 %.2e (V2's 1.5e-7), centre R_s %.9f (V2's flow %.9f), X-dependence %.1e"
        % (res["u1"]["its"], o["xi2"], c["Rc"], math.exp(one["sc"]), res["u1"]["xdep"]))
    if not go("u1"):
        return res
    res["u2"] = {}
    for N in (24, 32):
        for eps, ops_, U_, o_ in P.continued("cheb", 2, N, STEPS):
            xdep, par = shape(ops_, U_)
            res["u2"][(N, eps)] = dict(its=len(o_["hist"]), R=o_["hist"][-1], xi2=o_["xi2"], xdep=xdep, par=par,
                                       c=P.centre(ops_, U_, eps), ops=ops_, U=U_)
            say("U2 N=%d eps %.2f: %d its, |R| %.1e, xi^2 %.1e, X-dependence %.3f, parity %.1e"
                % (N, eps, len(o_["hist"]), o_["hist"][-1], o_["xi2"], xdep, par))
    if not go("u2"):
        return res
    u2 = res["u2"]
    res["u3"] = {}
    for N in (24, 32):
        base = u2[(N, 1.0)]["c"]["n2"]
        for eps in STEPS[1:]:
            r = u2[(N, eps)]["c"]["n2"] / base
            res["u3"][(N, eps)] = (r, r / (2 / (1 + eps)) ** 2 - 1)
            say("U3 N=%d eps %.2f: N^2_centre ratio %.5f against (2/(1+eps))^2 = %.5f, deviation %+.4f"
                % (N, eps, r, (2 / (1 + eps)) ** 2, res["u3"][(N, eps)][1]))
    if not go("u3"):
        return res
    c1, c5 = u2[(32, 1.0)]["c"], u2[(32, 0.5)]["c"]
    res["u4"] = dict(c1=c1, c5=c5)
    say("U4 eps = 1: d(throat) %.5f, d(exterior) %.5f; eps = 0.5: %.5f, %.5f, gap %.4f against L3 log 2 = %.4f; "
        "centre R_c %.5f (e^sig0 %.5f), L3 from K %.5f (fixed point %.5f)"
        % (c1["d_throat"], c1["d_ext"], c5["d_throat"], c5["d_ext"], c5["d_ext"] - c5["d_throat"],
           L3fp * math.log(2), c5["Rc"], math.exp(s0), c5["L3"], L3fp))
    if not go("u4"):
        return res
    ref_ops, Uref = u2[(32, 0.5)]["ops"], u2[(32, 0.5)]["U"]
    res["u5"] = {}
    for order in (2, 4):
        for N in (16, 32):
            out = P.continued("fd", order, N, STEPS)
            eps, ops_, U_, o_ = out[-1]
            res["u5"][(order, N)] = compare(ref_ops, Uref, ops_, U_)
            say("U5 FD%d N=%d at eps 0.5: against Chebyshev N=32 %.2e" % (order, N, res["u5"][(order, N)]))
    if not go("u5"):
        return res
    c2g = {eps: 6 * math.pi * u2[(32, eps)]["c"]["L3"] * u2[(32, eps)]["c"]["Rc"] ** 2 for eps in STEPS}
    res["u6"] = dict(c2g=c2g, fp=6 * math.pi * L3fp * math.exp(2 * s0))
    say("U6 c2 G5 = 6 pi L3 R_c^2 from the bulk's centre: %s (fixed point %.3f); E_Casimir = -c2/(6(1+eps)) in the "
        "throat's flat frame" % (", ".join("%.3f" % c2g[e] for e in STEPS), res["u6"]["fp"]))
    go("u6")
    return res


def _check(stage, res):
    if stage == "u1":
        v = res["u1"]
        r = v["its"] <= 8 and abs(math.log(v["xi2"] / 1.5e-7)) < 0.1 and abs(v["Rc"] - v["Rc1d"]) < 1e-6 and \
            v["xdep"] < 1e-12
        return r, "U1 eps = 1 is V2: %s" % r
    if stage == "u2":
        u2 = res["u2"]
        r = (all(v["its"] <= 8 and v["R"] < 1e-10 and v["par"] < 1e-12 for v in u2.values())
             and u2[(32, 0.5)]["xdep"] > 0.15 and u2[(32, 0.5)]["xi2"] < u2[(24, 0.5)]["xi2"] / 50)
        return r, "U2 continuation converged, mouths' symmetry, X-dependent, convergent in N: %s" % r
    if stage == "u3":
        u3 = res["u3"]
        r = (abs(u3[(32, 0.8)][1]) < 3e-3 and -1.2e-2 < u3[(32, 0.5)][1] < -3e-3
             and abs(u3[(32, 0.5)][1]) > abs(u3[(32, 0.8)][1])
             and all(abs(u3[(24, e)][0] - u3[(32, e)][0]) < 1e-3 for e in STEPS[1:]))
        return r, "U3 the AdS3 centre's lapse follows (2/(1+eps))^2, within 1.2%% at eps = 0.5: %s" % r
    if stage == "u4":
        s0, L3fp = res["fp"]
        c1, c5 = res["u4"]["c1"], res["u4"]["c5"]
        gap = c5["d_ext"] - c5["d_throat"]
        r = (abs(c1["d_ext"] - c1["d_throat"]) < 1e-6 and 1.0 < gap / (L3fp * math.log(2)) < 1.25
             and abs(c5["Rc"] / math.exp(s0) - 1) < 0.03 and abs(c5["L3"] / L3fp - 1) < 0.05)
        return r, "U4 the exterior's transition farther by about L3 log(1/eps); the centre near the fixed point: %s" % r
    if stage == "u5":
        u5 = res["u5"]
        p2 = math.log2(u5[(2, 16)] / u5[(2, 32)])
        p4 = math.log2(u5[(4, 16)] / u5[(4, 32)])
        r = 1.5 < p2 < 2.6 and 3.0 < p4 < 5.2
        return r, "U5 FD orders %.2f and %.2f against Chebyshev: %s" % (p2, p4, r)
    u6 = res["u6"]
    dev = [u6["c2g"][e] / u6["fp"] - 1 for e in STEPS]
    r = all(0 < d < 0.10 for d in dev) and all(dev[i + 1] > dev[i] for i in range(len(dev) - 1))
    return r, ("U6 the centre's c2 above the fixed point's by %s, rising as the exterior shrinks (the flow region's "
               "share): %s" % (", ".join("%.1f%%" % (100 * d) for d in dev), r))


def selftest(quiet=False):
    """quiet (the mutants) stops at the first failing stage; a run that stops short fails"""
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("U0 words: %s" % r)

    def gate(stage, res):
        r, line = _check(stage, res)
        ok.append(r)
        say(line)
        return r or not quiet
    run(quiet, gate)
    say("%d/%d" % (sum(ok), 7))
    return len(ok) == 7 and all(ok)


def mutants():
    caught = 0
    names = ("no_hT", "hT_up", "x_dirichlet", "no_flux")
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
