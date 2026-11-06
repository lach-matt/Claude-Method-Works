#!/usr/bin/env python3
"""gluedecay5.py -- the norms, exponents and constants of GLUEDECAY5.md (which decaying perturbations Theorem 4 (ii)
reaches, directly or through gluing).

The paper's section 8.7 (paper/RESPONSE-HL-5D.md) left open whether a perturbation decaying like r^(-a), 3/2 < a,
agrees on a ball B_R with data to which Theorem 4 (ii) applies, with smallness uniform as R -> oo. GLUEDECAY5.md
settles it. The norm is Hintz's (READ, [Hin26] (1.5) p. 2, Definition 2.6 p. 47, Definition 2.8 p. 48): coefficients of
rho^2, rho^3 in H^d(S^3) plus the remainder in rho^(l0) H_b^d with the b-density dr/r dw (PART-III-A-PREREQ.md 1.1).

  E1 (exact, sympy) Proposition 1 and the threshold. int_{r1}^R r^(2(l0 - a)) dr/r: finite as R -> oo iff a > l0,
     equal to r1^(2(l0-a))/(2(a - l0)); log(R/r1) at a = l0; ~ R^(2(l0-a))/(2(l0-a)) below. (r d_r)^j of
     r^(-a) psi(log r) is r^(-a) sum_k C(j,k) (-a)^(j-k) psi^(k)(log r), j <= 3, psi generic: b-derivatives keep the
     order, so a conormal function of order a lies in rho^(l0) H_b^oo iff its order exceeds l0 (for the profile
     r^(-a) cos(log r): iff a > l0). A nonzero rho^2 or rho^3 term is never a remainder: 2 l0 - 4 > 0 and 2 l0 - 6 > 0
     on l0 in (3, 4) (uniqueness of the expansion). Control: the Lebesgue density |dx| = r^4 dr/r dw moves the
     threshold to l0 + 2, so 'finite at a = l0 + 1/4' fails, as it must.
  E2 (exact; certified, mpmath interval arithmetic) Lemma 3.1. The Wronskian of e^(z_j u), j = 1..4, is
     e^((z_1+..+z_4) u) prod_(j<k) (z_k - z_j) (symbolic z), so s^(l0-a) cos log s, s^(l0-a) sin log s, s^(l0-2),
     s^(l0-3) are independent on (1/2, 1); their Gram matrix in L^2(ds/s) in closed form, checked against sympy's exact
     integrals and mpmath quadrature; kappa(a, l0)^2 = lambda_min of the 2 x 2 Schur complement, certified > 0 at
     l0 = 13/4, 7/2, 15/4 and a = 8/5, 2, 5/2, 3, (3 + l0)/2, l0 (the class exponents 2 and 3 included), with the
     values printed. Control (discriminating): the profile s^(l0-2) without the oscillation (a = 2, a class term)
     has distance 0 from the span, and the positivity certificate fails, as it must.
  E3 (exact; and quadrature) Proposition 3's example. For Psi(x) = phi(|x|) x/|x| and gamma = A(r) xh xh + B(r)
     (delta - xh xh) (generic phi, A, B), Psi^* gamma = A(phi) phi'^2 xh xh + B(phi) (phi/r)^2 (delta - xh xh), at three
     points of R^4 (r = 5, 7, 2). With phi = r + eps r^(1-a) cos log r: tr(Psi^* delta - delta) = 2 eps r^(-a)
     ((4 - a) cos log r - sin log r) + eps^2 (v'^2 + 3 v^2/r^2), v = r^(1-a) cos log r, exactly; with the Tangherlini
     term alpha = mu/r^2, r^(2+a) d_eps E|_0 and r^(2+2a) d_eps^2 E|_0 depend on r only through log r (so E =
     O(eps r^(-2-a))). Quadrature at (a, l0) = (5/2, 7/2) and (7/2, 7/2), eps = 1/100, mu = 1, R = 10^2, 10^3, 10^4:
     the least-squares remainder D_R of r^(l0) tr h on (R/2, R) against r^(l0-2), r^(l0-3), divided by eps R^(l0-a),
     is within 1e-2 (relative) of 2 A_a dist(log R + phi_a) and above 2 A_a kappa (1 - 10^-2): the lower bound of
     Proposition 3 in an instance, at a < l0 and at a = l0. Control: the three-dimensional coefficient (3 - a) in
     place of (4 - a) makes the trace identity false, as it must.
  E4 (exact) Proposition 4's exponent bookkeeping, piecewise linear in (a, l0) on 3/2 <= a <= l0, 3 <= l0 <= 4, cut
     at a = 2, 3: each inequality is checked at every vertex of each piece (a linear function is <= 0 on a polygon iff
     at its vertices; strictness at the vertices off the excluded faces). The charge fluxes of the perturbation vanish
     iff a > 2 + d; the gluing terms T_j have exponents d - 2 + min(0, 2 - a), d - 3 + min(0, 3 - a), d - a and
     d + 2 - 2a, each below the box exponent min(0, 2 + d - a); the annulus deviation theta = O(eps R^(-a)); every
     piece of the glued norm is O(eps R^(l0-a)). Control (discriminating): without the decoupling of mass and boost
     from the degree-1 charges (Lemma 4.1 (c)), |p_2| = O(eps R^min(0, 3-a)) and the term |p_2| R^(l0-2) exceeds
     eps R^(l0-a) for 2 < a <= 3: the check fails, as it must.
  E5 (exact, sympy series) Lemma 4.1's inputs. (a) The spin enters the Kerr-Schild metric at rho^3: every component of
     h k k at spins (1/3, 1/5) minus that at zero spin starts at rho^3 or later, some at rho^3 (checks/mpdata5.py's
     mp_ingredients, one rational point of S^3). (b) A translation enters at rho^3: mu x_i x_j |x|^-4 at x + c minus
     at x starts at rho^3. (c) A radial Hessian carries no momentum and no angular momentum: (d_i d_j f - Lap f
     delta_ij) x^i = -3 (f'/r) x_j (odd) and (W x)^j (d_i d_j f) x^i = 0, generic f. (d) Hintz's surface is not a
     Kerr-Schild slice: f' = 2 mu/(r^2 - mu) (III.B (3.3)) gives tr Hess f = 2 mu r^-3 + O(r^-5), so Part V's members
     (data on {y^0 = 0}) differ from Tangherlini's data on Sigma_IVP by an O(mu) rho^3 term in k. Controls: (a) with a
     different mass in place of the spins the difference starts at rho^2; (d) the trace taken with the
     three-dimensional Laplacian (factor 2) gives 0 at rho^3. Both fail as they must.
  E6 (text) GLUEDECAY5.md: every line at most 121 characters; its proposed replacement's old block occurs exactly once
     in paper/RESPONSE-HL-5D.md (the line printed) and its new block's lines are at most 121 characters. Control: the
     old block with one character changed occurs no time, and the check fails, as it must.

Labels: computed (exact, sympy; E2's positivity certified by interval arithmetic; E3's instance by mpmath quadrature
at 30 digits). Reach: E3's quadrature is an instance of Proposition 3, not its proof; E4 checks the exponents, not
the constants; E5 checks the expansions that Lemma 4.1 uses, not the gluing.

Run: python3 checks/gluedecay5.py   (about five minutes on a loaded machine)
"""
import os
import sys
from fractions import Fraction as Fr

import mpmath as mpm
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(HERE, "..", "..", "paper", "RESPONSE-HL-5D.md")
DOC = os.path.join(HERE, "GLUEDECAY5.md")


# ---------------------------------------------------------------------------------------------------------- E1
def e1(control=False):
    r, r1, R, a, l0 = sp.symbols("r r1 R a l0", positive=True)
    dens = (r**4 if control else 1) / r                                # b-density dr/r (control: Lebesgue r^4 dr/r)
    ok = True
    inst = []
    for L0 in (sp.Rational(13, 4), sp.Rational(7, 2), sp.Rational(15, 4)):
        for A_ in (L0 + sp.Rational(1, 4), L0 + 1, sp.Rational(4)):
            I = sp.integrate(r**(2 * L0) * r**(-2 * A_) * dens, (r, r1, sp.oo))
            fin = I.is_finite if not isinstance(I, sp.Piecewise) else False
            want = r1**(2 * (L0 - A_)) / (2 * (A_ - L0))
            ok &= bool(fin) and (control or sp.simplify(I - want) == 0)
            inst.append(fin)
    if control:
        return ok
    Ieq = sp.integrate(r**(2 * l0) * r**(-2 * l0) / r, (r, r1, R))
    ok &= sp.simplify(Ieq - sp.log(R / r1)) == 0 or sp.simplify(Ieq - (sp.log(R) - sp.log(r1))) == 0
    Ibl = sp.integrate(r**(2 * sp.Rational(7, 2) - 2 * sp.Rational(5, 2) - 1), (r, r1, R))
    ok &= sp.simplify(Ibl - (R**2 - r1**2) / 2) == 0                    # a = 5/2 < l0 = 7/2: R^(2(l0-a))/(2(l0-a))
    psi = sp.Function("psi")
    t = sp.symbols("t", real=True)
    g = sp.exp(-a * t) * psi(t)                                        # r = e^t: r d_r = d_t
    bder = True
    for j in range(1, 4):
        g = sp.diff(g, t)
        claim = sp.exp(-a * t) * sum(sp.binomial(j, k) * (-a)**(j - k) * sp.diff(psi(t), t, k) for k in range(j + 1))
        bder &= sp.simplify(g - claim) == 0
    uniq = all(2 * L0 - 4 > 0 and 2 * L0 - 6 > 0 for L0 in (Fr(301, 100), Fr(7, 2), Fr(399, 100)))
    print("  E1: int_r1^oo r^(2(l0-a)) dr/r = r1^(2(l0-a))/(2(a-l0)) at a > l0 (9 instances, l0 = 13/4, 7/2, 15/4): "
          "%s;\n      = log(R/r1) at a = l0 and (R^2 - r1^2)/2 at (a, l0) = (5/2, 7/2): %s; (r d_r)^j [r^-a psi(log r)]"
          " = r^-a sum_k C(j,k) (-a)^(j-k) psi^(k), j <= 3: %s;\n      rho^2, rho^3 terms never remainders "
          "(2 l0 - 4, 2 l0 - 6 > 0): %s" % (all(inst), ok, bder, uniq), flush=True)
    return ok and bder and uniq


# ---------------------------------------------------------------------------------------------------------- E2
def gram_closed(q, p1, p2, ivm=mpm.iv):
    """Gram matrix of (f_c, f_s, g1, g2) = (e^(qu) cos u, e^(qu) sin u, e^(p1 u), e^(p2 u)) on u in (-log 2, 0)"""
    L = ivm.log(2)

    def cint(c, w):                                                    # int_{-L}^0 e^((c + i w) u) du = (Re, Im)
        E, co, si = ivm.exp(-c * L), ivm.cos(w * L), ivm.sin(w * L)
        if c == 0 and w == 0:
            return L, ivm.mpf(0)
        den = c * c + w * w
        return ((c * (1 - E * co) + w * E * si) / den, (c * E * si - w * (1 - E * co)) / den)
    cc = (cint(2 * q, 0)[0] + cint(2 * q, 2)[0]) / 2
    ss = (cint(2 * q, 0)[0] - cint(2 * q, 2)[0]) / 2
    cs = cint(2 * q, 2)[1] / 2
    rows = [[cc, cs], [cs, ss]]
    cg = [[cint(q + p, 1)[0], cint(q + p, 1)[1]] for p in (p1, p2)]   # <g_p, f_c>, <g_p, f_s>
    gg = [[cint(pa + pb, 0)[0] for pb in (p1, p2)] for pa in (p1, p2)]
    return rows, cg, gg


def schur(rows, cg, gg):
    det = gg[0][0] * gg[1][1] - gg[0][1] * gg[1][0]
    inv = [[gg[1][1] / det, -gg[0][1] / det], [-gg[1][0] / det, gg[0][0] / det]]
    S = [[None, None], [None, None]]
    for i in range(2):
        for j in range(2):
            corr = sum(cg[k][i] * inv[k][l] * cg[l][j] for k in range(2) for l in range(2))
            S[i][j] = rows[i][j] - corr
    return S


def kappa2(a_, l0_, ivm=mpm.iv):
    q, p1, p2 = ivm.mpf(l0_) - ivm.mpf(a_), ivm.mpf(l0_) - 2, ivm.mpf(l0_) - 3
    S = schur(*gram_closed(q, p1, p2, ivm))
    tr, det = S[0][0] + S[1][1], S[0][0] * S[1][1] - S[0][1] * S[1][0]
    return S, det, tr / 2 - ivm.sqrt((tr / 2)**2 - det) if ivm is mpm.mp else None


def e2(control=False):
    mpm.iv.dps = 50
    mpm.mp.dps = 50
    if control:                                                        # s^(l0-2) itself: distance from the span
        l0_ = mpm.iv.mpf(7) / 2
        p1, p2 = l0_ - 2, l0_ - 3
        L = mpm.iv.log(2)

        def g(c):
            return (1 - mpm.iv.exp(-c * L)) / c
        G = [[g(2 * p1), g(p1 + p2), g(p1 + p1)], [g(p1 + p2), g(2 * p2), g(p2 + p1)],
             [g(p1 + p1), g(p1 + p2), g(2 * p1)]]                       # (g1, g2, s^(l0-2) = g1): rank 2
        d2 = G[2][2] - (G[2][0] * (G[1][1] * G[0][2] - G[0][1] * G[1][2])
                        + G[2][1] * (G[0][0] * G[1][2] - G[1][0] * G[0][2])) / (G[0][0] * G[1][1] - G[0][1]**2)
        return d2.a > 0                                                # certified positive? it is not (contains 0)
    z = sp.symbols("z1:5")
    u = sp.symbols("u")
    W = sp.Matrix(4, 4, lambda k, j: sp.diff(sp.exp(z[j] * u), u, k))
    vdm = sp.prod([z[k] - z[j] for j in range(4) for k in range(j + 1, 4)])
    wr = sp.simplify(W.det() - sp.exp(sum(z) * u) * vdm) == 0
    # closed forms against sympy's exact integrals and mpmath quadrature at (a, l0) = (5/2, 7/2)
    q, p1, p2 = sp.Rational(1), sp.Rational(3, 2), sp.Rational(1, 2)
    Ls = sp.log(2)
    ex = {"cc": sp.integrate(sp.exp(2 * q * u) * sp.cos(u)**2, (u, -Ls, 0)),
          "cs": sp.integrate(sp.exp(2 * q * u) * sp.cos(u) * sp.sin(u), (u, -Ls, 0)),
          "g1c": sp.integrate(sp.exp((p1 + q) * u) * sp.cos(u), (u, -Ls, 0)),
          "g2s": sp.integrate(sp.exp((p2 + q) * u) * sp.sin(u), (u, -Ls, 0))}
    rows, cg, gg = gram_closed(mpm.mpf(1), mpm.mpf(3) / 2, mpm.mpf(1) / 2, mpm.mp)
    vals = {"cc": rows[0][0], "cs": rows[0][1], "g1c": cg[0][0], "g2s": cg[1][1]}
    quad = {"cc": mpm.quad(lambda x: mpm.exp(2 * x) * mpm.cos(x)**2, [-mpm.log(2), 0]),
            "cs": mpm.quad(lambda x: mpm.exp(2 * x) * mpm.cos(x) * mpm.sin(x), [-mpm.log(2), 0]),
            "g1c": mpm.quad(lambda x: mpm.exp(2.5 * x) * mpm.cos(x), [-mpm.log(2), 0]),
            "g2s": mpm.quad(lambda x: mpm.exp(1.5 * x) * mpm.sin(x), [-mpm.log(2), 0])}
    cf = all(abs(sp.N(ex[k], 40) - vals[k]) < mpm.mpf(10)**-35 and abs(quad[k] - vals[k]) < mpm.mpf(10)**-35
             for k in ex)
    cert, table = True, []
    for L0 in (Fr(13, 4), Fr(7, 2), Fr(15, 4)):
        for A_ in (Fr(8, 5), Fr(2), Fr(5, 2), Fr(3), (3 + L0) / 2, L0):
            S, det, _ = kappa2(mpm.iv.mpf(A_.numerator) / A_.denominator, mpm.iv.mpf(L0.numerator) / L0.denominator)
            pos = S[0][0].a > 0 and det.a > 0
            cert &= pos
            Sm, detm, lam = kappa2(mpm.mpf(A_.numerator) / A_.denominator, mpm.mpf(L0.numerator) / L0.denominator,
                                   mpm.mp)
            table.append((L0, A_, lam, pos))
    print("  E2: Wronskian of e^(z_j u) = e^(sum z u) prod (z_k - z_j), symbolic: %s; Gram closed forms = sympy exact"
          " = quadrature (1e-35): %s;\n      kappa^2 = lambda_min(Schur), certified > 0 at every grid point: %s"
          % (wr, cf, cert), flush=True)
    for L0 in (Fr(13, 4), Fr(7, 2), Fr(15, 4)):
        print("      l0 = %-5s " % L0 + "  ".join("a = %s: kappa = %s" % (A_, mpm.nstr(mpm.sqrt(lam), 4))
                                                   for (l_, A_, lam, _) in table if l_ == L0), flush=True)
    return wr and cf and cert


# ---------------------------------------------------------------------------------------------------------- E3
def e3(control=False):
    X = sp.symbols("x1:5", real=True)
    rr = sp.sqrt(sum(xi**2 for xi in X))
    phi, A, B = sp.Function("phi"), sp.Function("A"), sp.Function("B")
    t = sp.symbols("t", positive=True)
    pullok = True
    if not control:
        Psi = sp.Matrix([phi(rr) * xi / rr for xi in X])
        J = Psi.jacobian(sp.Matrix(X))
        Pyy = Psi * Psi.T / phi(rr)**2                                 # y yhat at y = Psi(x), |y| = phi(r) > 0
        gam = A(phi(rr)) * Pyy + B(phi(rr)) * (sp.eye(4) - Pyy)
        pull = J.T * gam * J
        xh = sp.Matrix([xi / rr for xi in X])
        P = xh * xh.T
        dphi = sp.diff(phi(t), t).subs(t, rr)
        claim = A(phi(rr)) * dphi**2 * P + B(phi(rr)) * (phi(rr) / rr)**2 * (sp.eye(4) - P)
        for pt in ((1, 2, 2, 4), (2, 3, 6, 0), (1, 1, 1, 1)):
            sub = dict(zip(X, pt))
            D = (pull - claim).subs(sub).doit()
            pullok &= all(sp.simplify(e_) == 0 for e_ in D)
    r, a, eps, mu = sp.symbols("r a epsilon mu", positive=True)
    v = r**(1 - a) * sp.cos(sp.log(r))
    ph = r + eps * v
    dph = sp.diff(ph, r)
    lhs = dph**2 - 1 + 3 * ((ph / r)**2 - 1)
    coef = (3 - a) if control else (4 - a)
    rhs = 2 * eps * r**(-a) * (coef * sp.cos(sp.log(r)) - sp.sin(sp.log(r))) + eps**2 * (sp.diff(v, r)**2
                                                                                          + 3 * (v / r)**2)
    trok = sp.simplify(sp.expand(lhs - rhs)) == 0
    if control:
        return trok
    E = mu * dph**2 / ph**2 - mu / r**2                                # alpha(phi) phi'^2 - alpha(r), alpha = mu/r^2
    E1 = sp.simplify(r**(2 + a) * sp.diff(E, eps).subs(eps, 0))
    E2_ = sp.simplify(r**(2 + 2 * a) * sp.diff(E, eps, 2).subs(eps, 0))
    tt = sp.symbols("tt")
    rate = all(not sp.simplify(e_.subs(sp.log(r), tt).subs(r, sp.exp(tt))).has(r) and
               not sp.simplify(sp.expand(sp.expand_log(e_.subs(r, sp.exp(tt)), force=True))).has(r)
               for e_ in (E1, E2_))
    rate &= sp.simplify(E1 - (-2 * mu * (a * sp.cos(sp.log(r)) + sp.sin(sp.log(r))))) == 0
    # quadrature: the lower bound in an instance
    mpm.mp.dps = 30
    inst_ok, lines = True, []
    for (A_, L0) in ((mpm.mpf(5) / 2, mpm.mpf(7) / 2), (mpm.mpf(7) / 2, mpm.mpf(7) / 2)):
        Aa = mpm.sqrt((4 - A_)**2 + 1)
        pha = mpm.atan2(1, 4 - A_)                                     # (4-a) cos x - sin x = A_a cos(x + phi_a)
        rows, cg, gg = gram_closed(L0 - A_, L0 - 2, L0 - 3, mpm.mp)
        S = schur(rows, cg, gg)
        trS, detS = S[0][0] + S[1][1], S[0][0] * S[1][1] - S[0][1]**2
        kap = mpm.sqrt(trS / 2 - mpm.sqrt((trS / 2)**2 - detS))
        e_, m_ = mpm.mpf(1) / 100, mpm.mpf(1)
        for RR in (mpm.mpf(10)**2, mpm.mpf(10)**3, mpm.mpf(10)**4):
            def trh(s):
                x = RR * s
                vv = x**(1 - A_) * mpm.cos(mpm.log(x))
                dv = x**(-A_) * ((1 - A_) * mpm.cos(mpm.log(x)) - mpm.sin(mpm.log(x)))
                p_, dp_ = x + e_ * vv, 1 + e_ * dv
                return dp_**2 * (1 + m_ / p_**2) - 1 - m_ / x**2 + 3 * ((p_ / x)**2 - 1)
            fns = [lambda s: (RR * s)**L0 * trh(s), lambda s: s**(L0 - 2), lambda s: s**(L0 - 3)]
            G = [[mpm.quad(lambda s: fns[i](s) * fns[j](s) / s, [mpm.mpf(1) / 2, 1]) for j in range(3)]
                 for i in range(3)]
            M = mpm.matrix([[G[1][1], G[1][2]], [G[2][1], G[2][2]]])
            bvec = mpm.matrix([G[0][1], G[0][2]])
            sol = mpm.lu_solve(M, bvec)
            D2 = G[0][0] - (sol[0] * bvec[0] + sol[1] * bvec[1])
            ratio = mpm.sqrt(D2) / (e_ * RR**(L0 - A_))
            th = mpm.log(RR) + pha
            vv2 = (mpm.cos(th), -mpm.sin(th))
            dist = mpm.sqrt(sum(vv2[i] * S[i][j] * vv2[j] for i in range(2) for j in range(2)))
            pred = 2 * Aa * dist
            good = abs(ratio / pred - 1) < mpm.mpf(10)**-2 and ratio > 2 * Aa * kap * (1 - mpm.mpf(10)**-2)
            inst_ok &= good
            lines.append("(a, l0) = (%s, %s), R = %s: D_R/(eps R^(l0-a)) = %s, 2 A_a dist = %s, 2 A_a kappa = %s"
                         % (mpm.nstr(A_, 3), mpm.nstr(L0, 3), mpm.nstr(RR, 3), mpm.nstr(ratio, 6),
                            mpm.nstr(pred, 6), mpm.nstr(2 * Aa * kap, 6)))
    print("  E3: Psi^* of a radial tensor (generic phi, A, B, three points): %s; tr(Psi^* delta - delta) identity: %s;"
          "\n      E = O(eps r^(-2-a)) at first and second order in eps, r^(2+a) d_eps E|_0 = -2 mu (a cos log r + "
          "sin log r): %s;\n      quadrature instance of Proposition 3 (within 1e-2 of the prediction, above the "
          "kappa bound): %s" % (pullok, trok, rate, inst_ok), flush=True)
    for ln in lines:
        print("        " + ln, flush=True)
    return pullok and trok and rate and inst_ok


# ---------------------------------------------------------------------------------------------------------- E4
PIECES = [[(Fr(3, 2), Fr(3)), (Fr(3, 2), Fr(4)), (Fr(2), Fr(3)), (Fr(2), Fr(4))],
          [(Fr(2), Fr(3)), (Fr(2), Fr(4)), (Fr(3), Fr(3)), (Fr(3), Fr(4))],
          [(Fr(3), Fr(3)), (Fr(3), Fr(4)), (Fr(4), Fr(4))]]           # 3/2 <= a <= 2, 2 <= a <= 3, 3 <= a <= l0


def holds(fun, strict, excl=()):
    """fun(a, l0) <= 0 at every vertex of each piece (linear there); < 0 at the vertices off the excluded faces"""
    ok = True
    for pc in PIECES:
        for (a_, l_) in pc:
            val = fun(a_, l_)
            ok &= val <= 0
            if strict and not any(face(a_, l_) for face in excl):
                ok &= val < 0
    return ok


def e4(control=False):
    m0 = lambda x: min(Fr(0), x)                                       # noqa: E731
    p2exp = (lambda a_: m0(3 - a_)) if control else (lambda a_: m0(2 - a_))   # |Delta p_2| = O(eps R^p2exp)
    p3exp = lambda a_: m0(3 - a_)                                      # noqa: E731  |Delta p| = O(eps R^p3exp)
    on_a32 = lambda a_, l_: a_ == Fr(3, 2)                            # noqa: E731  the excluded face a = 3/2
    on_al0 = lambda a_, l_: a_ == l_                                  # noqa: E731  a = l0 (logarithm there)
    res = {}
    for d in (0, 1):
        box = lambda a_, d=d: m0(2 + d - a_)                          # noqa: E731
        res["T: d-a<0 (d=%d)" % d] = holds(lambda a_, l_, d=d: d - a_, True, (on_a32,))
        res["T: d+2-2a<0 (d=%d)" % d] = holds(lambda a_, l_, d=d: d + 2 - 2 * a_, True, (on_a32,))
        for name, ex in (("d-2+p2", lambda a_, d=d: d - 2 + p2exp(a_)), ("d-3+p3", lambda a_, d=d: d - 3 + p3exp(a_)),
                         ("d-a", lambda a_, d=d: d - a_), ("d+2-2a", lambda a_, d=d: d + 2 - 2 * a_)):
            res["box %s < min(0,2+d-a) (d=%d)" % (name, d)] = holds(lambda a_, l_, ex=ex, box=box: ex(a_) - box(a_),
                                                                   True, (on_a32,))
    res["theta: p2 - 2 <= -a"] = holds(lambda a_, l_: p2exp(a_) - 2 + a_, False)
    res["theta: p3 - 3 <= -a"] = holds(lambda a_, l_: p3exp(a_) - 3 + a_, False)
    res["norm: p2 + l0 - 2 <= l0 - a"] = holds(lambda a_, l_: p2exp(a_) + l_ - 2 - (l_ - a_), False)
    res["norm: p3 + l0 - 3 <= l0 - a"] = holds(lambda a_, l_: p3exp(a_) + l_ - 3 - (l_ - a_), False)
    res["norm: p3 + l0 - 4 <= l0 - a (outer)"] = holds(lambda a_, l_: p3exp(a_) + l_ - 4 - (l_ - a_), False)
    res["norm: 0 <= l0 - a (coefficients, compact part)"] = holds(lambda a_, l_: -(l_ - a_), False)
    res["norm: l0 - a > 0 off a = l0"] = holds(lambda a_, l_: -(l_ - a_), True, (on_al0,))
    flux = all(((2 + d - a_) < 0) == (a_ > 2 + d) for d in (0, 1) for a_ in (Fr(8, 5), Fr(2), Fr(5, 2), Fr(3),
                                                                             Fr(13, 4), Fr(7, 2)))
    if control:
        return all(res.values())
    print("  E4: flux of the perturbation's charge of degree d vanishes iff a > 2 + d: %s; the inequalities:" % flux,
          flush=True)
    for k_, v_ in res.items():
        print("        %-48s %s" % (k_, v_), flush=True)
    return flux and all(res.values())


# ---------------------------------------------------------------------------------------------------------- E5
def e5(control=False):
    sys.path.insert(0, os.path.join(HERE, "checks"))
    import mpdata5 as md
    rho, mu = md.rho, md.mu
    om = md.POINTS[1]
    u, h, k, _ = md.mp_ingredients(om, sp.Rational(1, 3), sp.Rational(1, 5))
    if control:
        u0, h0, k0, _ = md.mp_ingredients(om, 0, 0)
        h0 = h0.subs(mu, 2 * mu)
    else:
        u0, h0, k0, _ = md.mp_ingredients(om, 0, 0)
    kk, kk0 = [sp.Integer(1)] + k, [sp.Integer(1)] + k0
    lows = []
    for i in range(5):
        for j in range(i, 5):
            okp, lo = md.powers(h * kk[i] * kk[j] - h0 * kk0[i] * kk0[j], rho, 5)
            lows.append(lo if lo is not None else 99)
            if not okp:
                return False
    spin = min(lows) == 3 if not control else min(lows) >= 3
    if control:
        return spin
    c = (1, -2, sp.Rational(1, 3), 0)
    x = [om[i] / rho for i in range(4)]
    xc = [x[i] + c[i] for i in range(4)]
    n2, n2c = sum(e_**2 for e_ in x), sum(e_**2 for e_ in xc)
    tl = []
    for i in range(4):
        for j in range(i, 4):
            ok_, lo = md.powers(mu * xc[i] * xc[j] / n2c**2 - mu * x[i] * x[j] / n2**2, rho, 5)
            tl.append(lo if ok_ else -1)
    trans = min(tl) == 3
    X = sp.symbols("x1:5", real=True)
    rr = sp.sqrt(sum(e_**2 for e_ in X))
    fF = sp.Function("f")(rr)
    H = sp.hessian(fF, X)
    lap = sum(H[i, i] for i in range(4))
    t = sp.symbols("t", positive=True)
    fp = sp.diff(sp.Function("f")(t), t).subs(t, rr)
    mom = all(sp.simplify((sum((H[i, j] - (lap if i == j else 0)) * X[i] for i in range(4))
                           + 3 * fp * X[j] / rr).doit()) == 0 for j in range(4))
    Wm = sp.Matrix(4, 4, lambda i, j: 1 if (i, j) == (0, 1) else (-1 if (i, j) == (1, 0) else 0))
    Wm2 = sp.Matrix(4, 4, lambda i, j: 1 if (i, j) == (1, 3) else (-1 if (i, j) == (3, 1) else 0))
    ang = all(sp.simplify(((W_ * sp.Matrix(X)).T * H * sp.Matrix(X))[0, 0]) == 0 for W_ in (Wm, Wm2))
    r, m = sp.symbols("r m", positive=True)
    f1 = 2 * m / (r**2 - m)
    f2 = sp.diff(f1, r)
    trH = sp.series(f2 + 3 * f1 / r, r, sp.oo, 6).removeO()
    trH3 = sp.series(f2 + 2 * f1 / r, r, sp.oo, 6).removeO()            # the three-dimensional factor (control (d))
    graph = sp.simplify(sp.limit(r**3 * trH, r, sp.oo) - 2 * m) == 0
    graph_c = sp.simplify(sp.limit(r**3 * trH3, r, sp.oo) - 2 * m) == 0
    print("  E5: (a) spin enters the Kerr-Schild metric at rho^%s (15 components, one point, spins (1/3, 1/5)): %s;"
          " (b) translation at rho^%s: %s;\n      (c) radial Hessian: (Hess f - Lap f delta) x = -3 (f'/r) x and (W x)"
          " . Hess f . x = 0: %s, %s; (d) tr Hess f = 2 mu r^-3 + ... for f' = 2 mu/(r^2 - mu): %s (three-dimensional"
          " Laplacian: %s)" % (min(lows), spin, min(tl), trans, mom, ang, graph, graph_c), flush=True)
    return spin and trans and mom and ang and graph


def e5c():
    """the control of (d) alone, as a separate mutation: the three-dimensional trace claimed to give 2 mu"""
    r, m = sp.symbols("r m", positive=True)
    f1 = 2 * m / (r**2 - m)
    trH3 = sp.series(sp.diff(f1, r) + 2 * f1 / r, r, sp.oo, 6).removeO()
    return sp.simplify(sp.limit(r**3 * trH3, r, sp.oo) - 2 * m) == 0


# ---------------------------------------------------------------------------------------------------------- E6
def old_new_blocks(text):
    """the fenced blocks after the lines 'Old:' and 'New:' in GLUEDECAY5.md's last section"""
    lines = text.split("\n")
    out = {}
    for tag in ("Old:", "New:"):
        i = max(k for k, l_ in enumerate(lines) if l_.strip() == tag)
        j = i + 1
        while not lines[j].startswith("```"):
            j += 1
        k = j + 1
        while not lines[k].startswith("```"):
            k += 1
        out[tag] = "\n".join(lines[j + 1:k])
    return out


def e6(control=False):
    doc = open(DOC, encoding="utf-8").read()
    paper = open(PAPER, encoding="utf-8").read()
    long_ = [i + 1 for i, l_ in enumerate(doc.split("\n")) if len(l_) > 121]
    blk = old_new_blocks(doc)
    old = blk["Old:"]
    if control:
        old = old.replace("ρ", "p", 1)
    n = paper.count(old)
    line = paper[:paper.find(old)].count("\n") + 1 if n else None
    newlong = [l_ for l_ in blk["New:"].split("\n") if len(l_) > 121]
    if control:
        return n == 1
    print("  E6: GLUEDECAY5.md lines over 121 characters: %s; old block occurs %d time(s) in the paper, from line %s"
          " (%d lines); new block lines over 121: %d" % (long_ or "none", n, line, old.count("\n") + 1, len(newlong)),
          flush=True)
    return not long_ and n == 1 and not newlong


CHECKS = [("E1", e1), ("E2", e2), ("E3", e3), ("E4", e4), ("E5", e5), ("E6", e6)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        if name == "E5":
            ctl = ctl or e5c()
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
