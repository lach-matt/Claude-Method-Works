#!/usr/bin/env python3
"""support5c.py -- computations behind three deduced steps of the paper (RESPONSE-HL-5D.md), verifier's rows 4, 5, 9.

  C11 (computed, exact: an integer exponent ledger, and sympy for its cost rule) paper section 5.3, "It controls the
      remainder: |w|_7 <= C N" (supplement section 4 Step 1; support5.py C5 takes it as an input rule). w = h + phi G1,
      G1 = [d_th g1]; |w|_7 = sum_(i<=7) lam^i ||d^i w|| (0.3); N is (5.4) = (4.1). Every Leibniz term of d^i w is
      lam^i d^i h, or lam^i (d^a phi)(d^b G1), a + b = i, with each derivative of the oscillating factor costing lam^-1,
      and each derivative d^a phi split by how many of its a derivatives are spatial (sp). Each term is held against
      every term of N that covers it (same unknown, same total order, enough spatial derivatives); its lam-exponent is
      (weight in |w|_7) - (oscillation cost) - (weight in N), and the term is covered when some exponent is >= 0. The
      cost rule itself is computed: d^b [f] of a profile f(x1, x2, th) at the phase v(x1, x2) has lowest lam-power
      exactly -b, b <= 7 (sympy, with the two-scale chain rule of (0.3)). The 128 ledger rows are classes
      (order i, a, number of spatial derivatives among the a) of Leibniz terms, not terms: the terms proper, (unknown,
      i, a), number 44 here (8 of h, 36 of phi G1); the verifier's count was 52, not reproduced. Both are printed.
      Controls, each must leave a term uncovered: (1) N without its ||d^j d phi|| term (this tests only that N has
      the needed terms); (2) |w|_8 measured against N with k = 6 (the verifier found 3 uncovered); (3) one extra lam^-1
      charged on each differentiated oscillating factor, cost lam^-(b+1) for b >= 1, read here as the verifier's "one
      extra lam^-1 per derivative" (it found 7 uncovered; charging lam^-2b instead leaves 57). The control the
      commission named, N without lam ||d^j d_x^2 phi||, is run and printed as well: it leaves no term uncovered, so
      it cannot serve as a control (see the report).
  C12 (computed, exact, rational arithmetic) paper section 5.4, "written as a symmetric hyperbolic first-order system it
      satisfies (A1)-(A4) of [DS23]" (supplement Step 8 (ii)-(iii)). At eight random admissible rational points (lapse
      N > 0, shift beta, spatial metric gamma = L L^T + I/10, half of them convex combinations toward (1, 0, delta)),
      and at Vaidya's own point inside the horizon (mu = 2, r = 1), the metric g = -N^2 dtau^2 + gamma(dx + beta
      dtau)^2 is written in coordinates (tau, y) whose time lines are Z = d_tau - beta (d_y = J d_x, J a random
      invertible rational Jacobian of the flow), g' = E^T g E. With V = (u, d_0 u, d_k u), the reduction of
      g'^ab d_a d_b u = F is A^0 d_0 V + A^k d_k V = lower, A^0 = diag(1, -g'^00, g'^ij), A^k with (u0, u_j) and
      (u_j, u0) entries -g'^kj and (u0, u0) entry -2 g'^0k. Checked exactly: A^0 symmetric positive definite
      (Sylvester: all leading principal minors > 0), every A^k symmetric, and the reduction reproduces -g'^ab d_a d_b u
      on a generic polynomial u (constant coefficients). The unknowns are 15 Cartesian components with one principal
      part, so the system is this scalar block tensored with the identity. Control: Vaidya's constant-x time lines
      inside the horizon (the original coordinates, g0^-1 at mu = 2, r = 1): A^0 is not positive definite.
  C13 (computed, exact, symbolic in every function) paper section 3, Proposition 3.4, "Inside the shell the wave enters
      M only through its trace on the sphere" (supplement Proposition 8.2). M[S] = R^2 (1 + (R^2/9) <Theta>),
      Theta = 2 theta+ theta- / (-g(n+, n-)), is expanded at g = g0 + lam (W + chi dv^2 + m1) on S_(v,r) in horizon5.py's
      coordinates (tau, r, th, p1, p2) with its two-scale derivative and expansion theta_of: W a general symmetric
      tangential profile (six functions of (tau, r, th, Theta)), chi(tau, r, th, Theta) and m1 (eight T^2-invariant
      functions of (tau, r, th)). To O(lam^0): (a) theta+, theta- carry no lam^-2, lam^-1; (b) the area element carries
      the wave only through tr_S W, and only at O(lam); (c) the lam^0 correction of Theta beyond g0's equals
      kappa(r, mu) d_Theta(tr_S W), kappa computed; the correction to theta- is zero; g(n+, n-) has none; (d) for
      lead5.py's W_TT itself it is identically zero, and M[S](g0) = mu (mass5 M1 reproduced). Control: a wave with a
      trace on the spheres (a(tau, r) cos Theta added to W_thth / r^2) gives a nonzero O(1) term in M, its mean over S
      not zero.

Labels: computed (exact; sympy and fractions). Run: python3 checks/support5c.py   (a few minutes)
"""
import os
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import horizon5 as H5                                                           # noqa: E402
import lead5 as L5                                                              # noqa: E402


# ---------------------------------------------------------------- C11: |w|_7 <= C N, the exponent ledger
def _osc_cost(bmax=7):
    """lowest lam-power of d^b [f] for a profile f at a phase v, b = 1..bmax (two-scale chain rule of (0.3))"""
    x1, x2, lam, th = sp.symbols("x1 x2 lam theta")
    X = (x1, x2)
    v = x1 + x2**2/3 + x1*x2
    f = (x1*x2 + 2)*sp.cos(th) + x1**2*sp.sin(2*th)

    def D(e, k):
        return sp.diff(e, X[k]) + sp.diff(v, X[k])/lam*sp.diff(e, th)
    rnd = random.Random(11)
    out, e = [], f
    for b in range(1, bmax + 1):
        e = sp.expand(D(e, rnd.randint(0, 1)))
        out.append(min(sp.Poly(sp.expand(e*lam**bmax), lam).monoms())[0] - bmax)
    return out


def _n_terms(drop=None, k=6):
    """the terms of (5.4): (unknown, total order, min spatial, lam weight)"""
    t = [("h", 0, 0, 0), ("phi", 0, 0, 0)]
    for j in range(k + 1):
        t.append(("h", j + 1, 0, j))                                    # lam^j ||d^j d h||
        if drop != "dphi":
            t.append(("phi", j + 1, 0, j))                              # lam^j ||d^j d phi||
        if drop != "dx2phi":
            t.append(("phi", j + 2, 2, j + 1))                          # lam^(j+1) ||d^j d_x^2 phi||
    return t                                                            # (Psi = box~ phi covers no single d^a phi)


def _ledger(cost, drop=None, k=6, kw=7, extra=0):
    terms = _n_terms(drop, k)
    rows = []
    for i in range(kw + 1):                                             # |w|_kw: i <= kw (7)
        rows.append(("h", i, 0, i, 0))
        for a in range(i + 1):
            b = i - a
            for sp_ in range(a + 1):
                rows.append(("phi", a, sp_, i, -cost[b - 1] + extra if b else 0))   # cost b (+ extra), as lam^-b
    worst, uncovered = None, []
    for u, a, sp_, wgt, oc in rows:
        exps = [wgt - oc - nw for (nu, na, nsp, nw) in terms if nu == u and na == a and sp_ >= nsp]
        best = max(exps) if exps else None
        if best is None or best < 0:
            uncovered.append((u, a, sp_, wgt - a if u == "phi" else wgt, best))
        else:
            worst = best if worst is None else min(worst, best)
    return len(rows), worst, uncovered


def c11(control=False):
    cost = _osc_cost()
    if control:
        _, _, unc = _ledger(cost, drop="dphi")
        _, _, unc8 = _ledger(_osc_cost(8), kw=8)
        _, _, unce = _ledger(cost, extra=1)
        print("  C11 controls (each must leave a term uncovered): N without ||d^j d phi||: %d (first: %s);\n"
              "      |w|_8 against N with k = 6: %d (%s); one extra lam^-1 on each differentiated oscillating\n"
              "      factor: %d" % (len(unc), unc[:2], len(unc8), unc8, len(unce)), flush=True)
        return not unc or not unc8 or not unce
    rule = cost == [-b for b in range(1, 8)]
    n, worst, unc = _ledger(cost)
    proper = 8 + sum(i + 1 for i in range(8))                           # (h, i) and (phi G1, i, a), i <= 7
    _, _, unc_named = _ledger(cost, drop="dx2phi")
    print("  C11: each derivative of [d_th g1] costs lam^-1, lowest powers for b = 1..7: %s (rule holds: %s);\n"
          "      %d (order, a, spatial count) classes of Leibniz terms of |w|_7 (%d Leibniz terms proper),\n"
          "      uncovered: %d, least lam-exponent over the covered: %d (>= 0);\n"
          "      the commission's control, N without lam ||d^j d_x^2 phi||: %d uncovered (the term is not used here)"
          % (cost, rule, n, proper, len(unc), worst, len(unc_named)), flush=True)
    return rule and not unc and worst >= 0


# ---------------------------------------------------------------- C12: the symmetric hyperbolic reduction
def _spd(rnd):
    Lm = sp.Matrix(4, 4, lambda i, j: sp.Rational(rnd.randint(-4, 4), rnd.randint(1, 5)) if j <= i else 0)
    return Lm*Lm.T + sp.eye(4)/10


def _metric(Nl, be, G):
    g = sp.zeros(5)
    bl = G*be
    g[0, 0] = -Nl**2 + (be.T*G*be)[0]
    for i in range(4):
        g[0, i + 1] = g[i + 1, 0] = bl[i]
        for j in range(4):
            g[i + 1, j + 1] = G[i, j]
    return g


def _reduce(gi):
    """A^0, A^1..A^4 of the first-order reduction of g^ab d_a d_b u = F in V = (u, u0, u1..u4)"""
    A0 = sp.zeros(6)
    A0[0, 0], A0[1, 1] = 1, -gi[0, 0]
    for i in range(4):
        for j in range(4):
            A0[2 + i, 2 + j] = gi[1 + i, 1 + j]
    Ak = []
    for k in range(4):
        A = sp.zeros(6)
        A[1, 1] = -2*gi[0, 1 + k]
        for j in range(4):
            A[1, 2 + j] = -gi[1 + k, 1 + j]                             # row u0: -g^kj d_k u_j
            A[2 + j, 1] = -gi[1 + j, 1 + k]                             # row u_j: g^ji (d0 u_i - d_i u0), summed
        Ak.append(A)
    return A0, Ak


def _sylvester(A):
    return all(A[:m, :m].det() > 0 for m in range(1, A.shape[0] + 1))


def _reproduces(gi, A0, Ak):
    """with constant g^ab: row u0 of A^0 d_0 V + A^k d_k V, V = (u, d0 u, d u), is -g^ab d_a d_b u; rows u_j vanish"""
    y = sp.symbols("y0:5")
    u = sum(sp.Rational(c + 1, 7)*y[a]*y[b]*y[(a + b + c) % 5] for a in range(5) for b in range(5) for c in range(2))
    V = sp.Matrix([u] + [sp.diff(u, y[a]) for a in range(5)])
    lhs = A0*V.diff(y[0]) + sum((Ak[k]*V.diff(y[1 + k]) for k in range(4)), sp.zeros(6, 1))
    box = sum(gi[a, b]*sp.diff(u, y[a], y[b]) for a in range(5) for b in range(5))
    return sp.expand(lhs[1] + box) == 0 and all(sp.expand(lhs[r_]) == 0 for r_ in range(2, 6))


def c12(control=False):
    mu, rr = sp.Integer(2), sp.Integer(1)                                # inside the horizon: r^2 < mu
    k = sp.Matrix([1, 1, 0, 0, 0])
    eta = sp.diag(-1, 1, 1, 1, 1)
    g0v = eta + mu/rr**2*k*k.T                                           # Vaidya at xhat = e1 (Cartesian, by rotation)
    if control:                                                          # its own constant-x time lines
        gi = g0v.inv()
        A0, Ak = _reduce(gi)
        pd, sym = _sylvester(A0), all(A == A.T for A in Ak)
        print("  C12 control: Vaidya's constant-x lines at r^2 < mu: g^11 = %s, A^0 positive definite: %s"
              % (gi[1, 1], pd), flush=True)
        return pd and sym
    rnd = random.Random(12)
    pts = []
    for n in range(8):
        Nl = sp.Rational(rnd.randint(1, 8), 4)
        be = sp.Matrix([sp.Rational(rnd.randint(-8, 8), 4) for _ in range(4)])
        G = _spd(rnd)
        if n % 2:                                                        # convex combination toward (1, 0, delta)
            s = sp.Rational(rnd.randint(1, 9), 10)
            Nl, be, G = (1 - s)*Nl + s, (1 - s)*be, (1 - s)*G + s*sp.eye(4)
        pts.append(("random %d" % n, _metric(Nl, be, G)))
    pts.append(("Vaidya r^2 < mu", g0v))
    ok, mins = True, []
    for name, g in pts:
        G = g[1:, 1:]
        be = G.inv()*g[1:, 0]                                            # beta^i from g_0i = gamma_ij beta^j
        Nl2 = -(g[0, 0] - (be.T*G*be)[0])
        assert Nl2 > 0 and _sylvester(G)                                 # admissible: lapse real, gamma positive
        J = sp.Matrix(4, 4, lambda i, j: sp.Rational(rnd.randint(-3, 3), 2) + (2 if i == j else 0))
        if J.det() == 0:
            J = J + sp.eye(4)
        E = sp.zeros(5)
        E[0, 0] = 1
        for i in range(4):
            E[1 + i, 0] = -be[i]                                         # Z = d_tau - beta
            for j in range(4):
                E[1 + i, 1 + j] = J[i, j]                                # d_y_j = J_ij d_x_i
        gp = E.T*g*E
        gpi = gp.inv()
        A0, Ak = _reduce(gpi)
        block = gpi[0, 0] == -1/Nl2 and all(gpi[0, 1 + i] == 0 for i in range(4))
        good = (A0 == A0.T and _sylvester(A0) and all(A == A.T for A in Ak) and block
                and _reproduces(gpi, A0, Ak))
        mins.append(min(A0[:m, :m].det() for m in range(1, 7)))
        ok &= bool(good)
    print("  C12: %d admissible points (8 random, 4 of them convex combinations toward Minkowski, and Vaidya at\n"
          "      r^2 < mu): along Z, g'^00 = -N^-2 and g'^0i = 0; A^0 symmetric positive definite (Sylvester),\n"
          "      every A^k symmetric, the reduction reproducing g'^ab d_a d_b u: %s (least leading minor %s)"
          % (len(pts), ok, min(mins)), flush=True)
    return ok


# ---------------------------------------------------------------- C13: M[S] to O(lam^0)
def _mass_terms(Wtan, mu, m1=True, chi=True):
    tau, r, th, TH, lam = H5.tau, H5.r, H5.th, H5.TH, H5.lam
    W = sp.zeros(5)
    for (i, j), e in Wtan.items():
        W[i, j] = W[j, i] = e
    if chi:
        dvv = sp.Matrix([1, 1, 0, 0, 0])
        W = W + sp.Function("chi")(tau, r, th, TH)*dvv*dvv.T
    if m1:
        idx = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]
        for n_, (i, j) in enumerate(idx):
            f = sp.Function("m%d" % n_)(tau, r, th)
            W[i, j] += f
            if i != j:
                W[j, i] += f
    g0 = H5.g0_of(mu)
    g = g0 + lam*W
    g0i = g0.inv()
    gi = g0i - lam*g0i*W*g0i
    A = [2, 3, 4]
    gam0 = sp.Matrix([[g0[a, b] for b in A] for a in A])
    gam0i = gam0.inv()
    Ws = sp.Matrix([[W[a, b] for b in A] for a in A])
    gami = gam0i - lam*gam0i*Ws*gam0i
    roots = H5.roots_g0(mu)
    alo = [x for x in roots if sp.simplify(x - 1) != 0][0]
    ali = [x for x in roots if sp.simplify(x - 1) == 0][0]
    al, a1 = sp.symbols("al a1")
    kk = sp.Matrix([al, 1, 0, 0, 0])

    def alpha(a0):
        q = sp.expand((kk.T*gi*kk)[0, 0].subs(al, a0 + lam*a1))
        return a0 + lam*sp.solve(sp.expand(sp.series(q, lam, 0, 2).removeO()).coeff(lam, 1), a1)[0]
    ap, am = alpha(alo), alpha(ali)

    def coeffs(e, lo=-2, hi=0):
        e = sp.expand(e)
        return {n: e.coeff(lam, n) for n in range(lo, hi + 1)}
    tp = coeffs(H5.theta_of(g, ap, gi=gi, gami=gami))
    tm = coeffs(H5.theta_of(g, am, gi=gi, gami=gami))
    kp, km = sp.Matrix([ap, 1, 0, 0, 0]), sp.Matrix([am, 1, 0, 0, 0])
    gnn = coeffs((kp.T*gi*km)[0, 0], 0, 1)
    tp0, tm0 = H5.theta_of(g0, alo), H5.theta_of(g0, ali)
    gnn0 = (sp.Matrix([alo, 1, 0, 0, 0]).T*g0i*sp.Matrix([ali, 1, 0, 0, 0]))[0, 0]
    det = sp.expand((gam0 + lam*Ws).det())
    area1 = sp.simplify(det.coeff(lam, 1)/gam0.det())                    # = tr_S W at O(lam)
    trS = sp.simplify(sum(gam0i[i, j]*Ws[i, j] for i in range(3) for j in range(3)))
    return dict(tp=tp, tm=tm, gnn=gnn, tp0=tp0, tm0=tm0, gnn0=gnn0, area0=sp.simplify(det.coeff(lam, 0) - gam0.det()),
                area1=area1, trS=trS)


def c13(control=False):
    t0 = time.time()
    tau, r, th, TH = H5.tau, H5.r, H5.th, H5.TH
    mu = sp.Symbol("mu", positive=True)
    WT = L5.wave(with_chi=False).subs({L5.v: tau + r, L5.r: r, L5.th: th, L5.s: TH})
    WTT = {(i, j): WT[i, j] for i in (2, 3, 4) for j in (2, 3, 4) if i <= j and WT[i, j] != 0}
    if control:                                                          # a trace on the spheres
        a = sp.Function("a")(tau, r)
        WTT[(2, 2)] = WTT[(2, 2)] + r**2*a*sp.cos(TH)
    o = _mass_terms(WTT, mu)
    Th0 = 2*o["tp0"]*o["tm0"]/(-o["gnn0"])
    M0 = sp.simplify(r**2*(1 + r**2/9*Th0))                              # mass5 M1: M[S](g0) = mu
    corr = sp.simplify(2*((o["tp"][0] - o["tp0"])*o["tm0"] + o["tp0"]*(o["tm"][0] - o["tm0"]))/(-o["gnn0"])
                       - 2*o["tp0"]*o["tm0"]*(o["gnn"][0] - o["gnn0"])/o["gnn0"]**2)
    Mcorr = sp.simplify(r**4/9*corr)                                     # lam^0 of M beyond mu (R = r at lam^0)
    if control:
        mean = sp.simplify(2*sp.integrate(Mcorr*sp.cos(th)*sp.sin(th), (th, 0, sp.pi/2)))   # S-measure c s, total 1/2
        print("  C13 control: a(tau, r) cos Theta added to W_thth/r^2: lam^0 term of M = %s, its S-mean %s"
              % (Mcorr, mean), flush=True)
        return Mcorr == 0
    low = all(sp.simplify(o[x][n]) == 0 for x in ("tp", "tm") for n in (-2, -1))
    tt_zero = Mcorr == 0 and sp.simplify(M0 - mu) == 0
    # the general tangential wave: six functions of (tau, r, th, Theta)
    gen = {}
    for i in (2, 3, 4):
        for j in (2, 3, 4):
            if i <= j:
                gen[(i, j)] = sp.Function("w%d%d" % (i, j))(tau, r, th, TH)
    og = _mass_terms(gen, mu)
    lowg = all(sp.simplify(og[x][n]) == 0 for x in ("tp", "tm") for n in (-2, -1))
    dtp = sp.simplify(og["tp"][0] - og["tp0"])
    dtm = sp.simplify(og["tm"][0] - og["tm0"])
    dgnn = sp.simplify(og["gnn"][0] - og["gnn0"])
    dtr = sp.diff(og["trS"], TH)
    kappa = sp.simplify(dtp/dtr)
    only_trace = sp.simplify(dtp - kappa*dtr) == 0 and not kappa.has(TH) and not any(
        kappa.has(sp.Function("w%d%d" % (i, j))) for i in (2, 3, 4) for j in (2, 3, 4))
    area = og["area0"] == 0 and sp.simplify(og["area1"] - og["trS"]) == 0
    print("  C13: M[S](g0) = mu: %s; theta+- carry no lam^-2, lam^-1 (W_TT: %s; general tangential W: %s);\n"
          "      area element: no wave at lam^0, at lam^1 exactly tr_S W: %s; lam^0 corrections for the general W:\n"
          "      theta+ = kappa d_Theta(tr_S W) with kappa = %s: %s; theta- %s; g(n+, n-) %s;\n"
          "      so the wave enters M at O(1) only through d_Theta(tr_S W); for lead5's W_TT the lam^0 term of M is %s"
          " [%.0fs]" % (sp.simplify(M0 - mu) == 0, low, lowg, area, kappa, only_trace, dtm, dgnn, Mcorr,
                        time.time() - t0), flush=True)
    return low and lowg and tt_zero and only_trace and dtm == 0 and dgnn == 0 and area


CHECKS = [("C11", c11), ("C12", c12), ("C13", c13)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
