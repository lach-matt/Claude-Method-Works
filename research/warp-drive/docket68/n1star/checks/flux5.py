#!/usr/bin/env python3
"""flux5.py -- c2: the b_e0 flux 6 pi^2 m and the glued mass bound (supplement Part VII Lemma 2.1 (c), Proposition 2.2
step (6); Part V Lemma 1.2 at X = e0), computed.

b_e0 = (d_j h_ij - d_i tr h) nu^i dS, h = gamma - delta, the flux of the linearised Hamiltonian constraint at flat data
paired with the Killing initial data e0 = (lapse 1, shift 0); q_e0 := DR_delta(h) - (R(gamma) - |K|^2 + (tr K)^2), so
that on vacuum data d_i b^i = q (Part V Lemma 1.2's identity, integrated over an annulus).

  F1 (exact) Tangherlini's data on {t_KS = 0} (the Kerr-Schild slice, gamma = delta + (m/r^2) x^ x^, K from the shift
     (m/r^2) x^): d_j h_ij - d_i tr h = 3 m x_i/r^4, so the flux over S_rho is 3 m rho^-3 times the area 2 pi^2 rho^3,
     6 pi^2 m at every radius; at three points (|x| = 5, 9, 13, m symbolic) the Hamiltonian constraint R(gamma) - |K|^2
     + (tr K)^2 vanishes and q_e0 = 0, as a flux independent of the radius requires of a radial q.
  F2 (exact) For generic h and K (polynomials with random rational coefficients) R(delta + eps h) = eps d_i (d_j h_ij -
     d_i tr h) + O(eps^2) at a random point, so d_i b^i = DR(h) and q_e0(eps h, eps K) = O(eps^2): q vanishes to second
     order at flat data, as step (6) uses.
  F3 (exact) The scaling of step (6): q of data h(x) = A H(x/R)/R^2, K(x) = A k(x/R)/R^3 is A^2 R^-6 qhat(x/R) + O(A^3)
     (computed: q at order A^1 vanishes, and R^6 q at order A^2 is the exact rational -10294529/36000 at the sampled
     point, independent of R). The volume of Gamma(R, 4R) is 255 pi^2 R^4/2 (computed exactly). The inequality
     6 pi^2 |dm| <= C (eta + |dm|)/R^2 + C eta, dm = m - mubar, is linear in |dm| with coefficient (6 pi^2 R^2 - C)/R^2,
     positive exactly when C < 6 pi^2 R^2 (checked: positive for C = 6 pi^2 R^2/(1 + s), s > 0), and then it gives
     |dm| <= C eta (R^2 + 1)/(6 pi^2 R^2 - C) (checked exactly: the bound is the equality's root).
  F4 (exact) The bilinear difference bound of step (6), |q(xhat) - q(gamma^mubar)| <= C (eta + |dm|) R^-6 on Gamma(R,
     4R): for data x2 = B (H, K)(x/R) scaled R^-2, R^-3 (gamma^mubar - delta is of this form, B = mubar) and a
     perturbation eps (D, E) of the same scaling, all generic, q(x2 + eps d) - q(x2) has no term linear in the data
     (no order-A term), at order A^2 no eps B^0 term and its eps B, eps^2 coefficients exactly R^-6 times constants,
     and at order A^3 coefficients exactly R^-8 times constants: so it is <= C eps (|B| + eps) R^-6 + C eps R^-8, with
     eps of the size of eta + |dm| as step (6) has it.
  Controls: F1, F2, the flux built with + d_i tr h in place of - d_i tr h is not the divergence of DR(h) (F2's identity
     fails), and on F1's slice it gives -2 pi^2 m, not 6 pi^2 m. F3, the same computation with every Gamma.Gamma term of
     the scalar curvature deleted: R^6 q at order A^2 is still independent of R (that test alone is blind to it), but its
     value is not -10294529/36000, and F3 rejects it. F4, q without its linear part DR(h): an order-A term appears and
     the bound fails.

Sign convention: q_e0 here is DR_delta(h) - (R - |K|^2 + (tr K)^2), the negative of Part V (1.1)'s, and it omits the
factor sqrt(det g); F1-F3 test vanishing, R-independence and a magnitude, so they are blind to both.

Labels: computed (exact, sympy).

Run: python3 checks/flux5.py   (about twenty minutes, F4 most of it)
"""
import random
import sys

import sympy as sp

X = sp.symbols("x1:5", real=True)
m, eps, A, Rr = sp.symbols("m epsilon A R", positive=True)


def jets_at(g, pt):
    """(g, dg[k], ddg[k][l]) of a matrix field at a point, exact"""
    n = len(X)
    g0 = g.subs(pt)
    dg = [g.diff(X[k]).subs(pt) for k in range(n)]
    ddg = [[g.diff(X[k]).diff(X[l]).subs(pt) for l in range(n)] for k in range(n)]
    return g0, dg, ddg


def curvature_at(g, pt, inverse=None, gg=True):
    """scalar curvature, Christoffel symbols and the inverse at a point, from the jets (no symbolic simplification);
    gg=False deletes every Gamma.Gamma term (F3's control)"""
    n = len(X)
    g0, dg, ddg = jets_at(g, pt)
    gi = inverse if inverse is not None else g0.inv()
    dgi = [-gi*dg[k]*gi for k in range(n)]
    low = [[[(dg[c][d, b] + dg[b][d, c] - dg[d][b, c])/2 for c in range(n)] for b in range(n)] for d in range(n)]
    dlow = [[[[(ddg[k][c][d, b] + ddg[k][b][d, c] - ddg[k][d][b, c])/2 for c in range(n)] for b in range(n)]
             for d in range(n)] for k in range(n)]
    G = [[[sum(gi[a, d]*low[d][b][c] for d in range(n)) for c in range(n)] for b in range(n)] for a in range(n)]
    dG = [[[[sum(dgi[k][a, d]*low[d][b][c] + gi[a, d]*dlow[k][d][b][c] for d in range(n)) for c in range(n)]
            for b in range(n)] for a in range(n)] for k in range(n)]
    R = 0
    for b in range(n):
        for c in range(n):
            e = 0
            for a in range(n):
                e += dG[a][a][b][c] - dG[c][a][b][a]
                for d in range(n if gg else 0):
                    e += G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a]
            R += gi[b, c]*e
    return sp.expand(R), G, gi


def flux_vector(h, sign=-1):
    return [sum(sp.diff(h[i, j], X[j]) for j in range(4)) + sign*sp.diff(h.trace(), X[i]) for i in range(4)]


PTS = [(1, 2, 2, 4), (2, 4, 5, 6), (3, 4, 0, 12)]                       # |x| = 5, 9, 13


def f1(control=False):
    r2 = sum(x**2 for x in X)
    r = sp.sqrt(r2)
    xh = sp.Matrix([x/r for x in X])
    hs = m/r2
    h = hs*xh*xh.T
    gam = sp.eye(4) + h
    F = flux_vector(h, +1 if control else -1)
    radial = sp.simplify(sum(F[i]*X[i] for i in range(4))/r)            # F . nu
    flux = sp.simplify(radial*2*sp.pi**2*r**3)
    if control:
        return sp.simplify(flux - 6*sp.pi**2*m) == 0
    beta = [hs*X[i]/r for i in range(4)]                                 # the shift (lowered), lapse (1 + m/r^2)^(-1/2)
    Nf = 1/sp.sqrt(1 + hs)
    DR = sum(sp.diff(F[i], X[i]) for i in range(4))
    hams, moms, qs = [], [], []
    for p_ in PTS:
        pt = dict(zip(X, p_))
        R, G, gi = curvature_at(gam, pt)
        N = Nf.subs(pt)
        bet0 = [b_.subs(pt) for b_ in beta]
        dbet = [[sp.diff(beta[j], X[i]).subs(pt) for j in range(4)] for i in range(4)]
        Db = [[dbet[i][j] - sum(G[k][i][j]*bet0[k] for k in range(4)) for j in range(4)] for i in range(4)]
        K = sp.Matrix(4, 4, lambda i, j: -(Db[i][j] + Db[j][i])/(2*N))   # K = (1/2N)(d_t gamma - L_beta gamma)
        Ku = gi*K
        trK = Ku.trace()
        ham = sp.simplify(R - sum(Ku[i, j]*Ku[j, i] for i in range(4) for j in range(4)) + trK**2)
        hams.append(ham)
        qs.append(sp.simplify(DR.subs(pt) - ham))
    print("  F1: (d_j h_ij - d_i tr h) . nu = %s; flux over S_rho = %s; at |x| = 5, 9, 13: Hamiltonian constraint %s;"
          " q_e0 = DR(h) - (R - |K|^2 + (tr K)^2) = %s" % (radial, flux, hams, qs), flush=True)
    return sp.simplify(flux - 6*sp.pi**2*m) == 0 and all(x == 0 for x in hams) and all(x == 0 for x in qs)


def rand_poly(rng):
    mons = [1] + list(X) + [X[i]*X[j] for i in range(4) for j in range(i, 4)]
    return sum(sp.Rational(rng.randint(-5, 5), rng.randint(1, 4))*mo for mo in mons)


def f2(control=False):
    rng = random.Random(7)
    h = sp.zeros(4)
    for i in range(4):
        for j in range(i, 4):
            h[i, j] = h[j, i] = rand_poly(rng)
    pt = {X[i]: sp.Rational(rng.randint(-3, 3), 7) for i in range(4)}
    g = sp.eye(4) + eps*h
    h0 = h.subs(pt)
    gi = sp.eye(4) - eps*h0 + eps**2*h0*h0 - eps**3*h0**3                  # the inverse to eps^3 at the point
    R, _, _ = curvature_at(g, pt, inverse=gi)
    R0, R1 = R.coeff(eps, 0), R.coeff(eps, 1)
    F = flux_vector(h, +1 if control else -1)
    div = sp.expand(sum(sp.diff(F[i], X[i]) for i in range(4)).subs(pt))
    ok = R0 == 0 and sp.simplify(R1 - div) == 0
    if control:
        return ok
    print("  F2: at a random point, R(delta + eps h) has eps^0 term %s and eps^1 term %s = d_i b^i %s" % (R0, R1, div),
          flush=True)
    return ok


def f3(control=False):
    rng = random.Random(11)
    Yv = sp.symbols("y1:5", real=True)
    Hm, Km = sp.zeros(4), sp.zeros(4)
    for i in range(4):
        for j in range(i, 4):
            Hm[i, j] = Hm[j, i] = rand_poly(rng).subs(dict(zip(X, Yv)))
            Km[i, j] = Km[j, i] = rand_poly(rng).subs(dict(zip(X, Yv)))
    scale = {Yv[i]: X[i]/Rr for i in range(4)}
    h = A*Hm.subs(scale)/Rr**2
    K = A*Km.subs(scale)/Rr**3
    pt = {X[i]: Rr*sp.Rational(rng.randint(-3, 3), 5) for i in range(4)}   # a point x with x/R fixed
    h0 = h.subs(pt)
    gi = sp.eye(4) - h0 + h0*h0 - h0**3
    R, _, _ = curvature_at(sp.eye(4) + h, pt, inverse=gi, gg=not control)
    F = flux_vector(h)
    DR = sp.expand(sum(sp.diff(F[i], X[i]) for i in range(4)).subs(pt))
    Ku = gi*K.subs(pt)
    q = sp.expand(DR - (R - sum(Ku[i, j]*Ku[j, i] for i in range(4) for j in range(4)) + Ku.trace()**2))
    q1 = sp.simplify(q.coeff(A, 1))
    scal = sp.simplify(q.coeff(A, 2)*Rr**6)
    ok = q1 == 0 and not scal.has(Rr) and scal == sp.Rational(-10294529, 36000)
    if control:
        print("  F3 control (Gamma.Gamma deleted): R^6 q at order A^2 = %s, independent of R: %s"
              % (scal, not scal.has(Rr)), flush=True)
        return ok
    C, d, mm, s_ = sp.symbols("C eta dm s", positive=True)
    lin = 6*sp.pi**2*mm - C*(d + mm)/Rr**2 - C*d                    # <= 0 is the inequality
    coef = sp.expand(lin).coeff(mm)
    bound = C*d*(Rr**2 + 1)/(6*sp.pi**2*Rr**2 - C)
    ok_coef = sp.simplify(coef*Rr**2 - (6*sp.pi**2*Rr**2 - C)) == 0
    ok_sign = sp.simplify(coef.subs(C, 6*sp.pi**2*Rr**2/(1 + s_))).is_positive is True
    ok_bound = sp.simplify(lin.subs(mm, bound)) == 0
    r_ = sp.Symbol("r", positive=True)
    vol = sp.integrate(2*sp.pi**2*r_**3, (r_, Rr, 4*Rr))
    ok_vol = sp.simplify(vol - sp.Rational(255, 2)*sp.pi**2*Rr**4) == 0
    print("  F3: q at order A^1: %s; R^6 q at order A^2 = %s (independent of R: %s); vol Gamma(R, 4R) = %s; coefficient"
          " of |dm| (6 pi^2 R^2 - C)/R^2: %s, positive for C < 6 pi^2 R^2: %s; |dm| <= %s: %s"
          % (q1, scal, not scal.has(Rr), vol, ok_coef, ok_sign, bound, ok_bound), flush=True)
    return ok and ok_coef and ok_sign and ok_bound and ok_vol


def f4(control=False):
    """step (6)'s bilinear difference bound: data x2 = B (H, K)(x/R) scaled R^-2, R^-3, a perturbation eps (D, E) of
    the same scaling, and A the amplitude's bookkeeping; Delta q := q(x2 + eps d) - q(x2) at a point with x/R fixed"""
    rng = random.Random(13)
    Yv = sp.symbols("y1:5", real=True)
    B, e = sp.symbols("B e", real=True)
    Hm, Km, Dm, Em = (sp.zeros(4) for _ in range(4))
    for M_ in (Hm, Km, Dm, Em):
        for i in range(4):
            for j in range(i, 4):
                M_[i, j] = M_[j, i] = rand_poly(rng).subs(dict(zip(X, Yv)))
    scale = {Yv[i]: X[i]/Rr for i in range(4)}
    pt = {X[i]: Rr*sp.Rational(rng.randint(-3, 3), 5) for i in range(4)}

    def q_of(hY, KY):
        h = A*hY.subs(scale)/Rr**2
        K = A*KY.subs(scale)/Rr**3
        h0 = h.subs(pt)
        gi = sp.eye(4) - h0 + h0*h0 - h0**3
        R, _, _ = curvature_at(sp.eye(4) + h, pt, inverse=gi)
        Ku = gi*K.subs(pt)
        ham = R - sum(Ku[i, j]*Ku[j, i] for i in range(4) for j in range(4)) + Ku.trace()**2
        if control:                                                  # q without its linear part: not quadratic at 0
            return sp.expand(-ham)
        F = flux_vector(h)
        DR = sum(sp.diff(F[i], X[i]) for i in range(4)).subs(pt)
        return sp.expand(DR - ham)
    dq = sp.expand(q_of(B*Hm + e*Dm, B*Km + e*Em) - q_of(B*Hm, B*Km))
    dq = sum(dq.coeff(A, k)*A**k for k in (1, 2, 3))                      # through the cubic part
    c = {}
    for k in (1, 2, 3):
        ck = sp.expand(dq.coeff(A, k))
        for (i, j) in [(1, 0), (1, 1), (2, 0), (1, 2), (2, 1), (3, 0)]:
            c[(k, i, j)] = sp.simplify(ck.coeff(e, i).coeff(B, j))
    lin0 = c[(1, 1, 0)] == 0 and c[(1, 1, 1)] == 0 and c[(1, 2, 0)] == 0     # q has no linear part
    eB0 = c[(2, 1, 0)] == 0                                                  # no eps^1 B^0 term at order A^2
    r6 = [sp.simplify(c[(2, i, j)]*Rr**6) for (i, j) in [(1, 1), (2, 0)]]
    r8 = [sp.simplify(c[(3, i, j)]*Rr**8) for (i, j) in [(1, 2), (2, 1), (3, 0)]]
    sc6 = all(not x.has(Rr) for x in r6) and any(x != 0 for x in r6)
    sc8 = all(not x.has(Rr) for x in r8) and any(x != 0 for x in r8)
    ok = lin0 and eB0 and sc6 and sc8
    if control:
        return ok
    print("  F4: Delta q has no order-A term: %s; at order A^2 no eps B^0 term: %s, and R^6 times the eps B and eps^2"
          " coefficients = %s, independent of R: %s;\n      at order A^3, R^8 times the eps B^2, eps^2 B, eps^3"
          " coefficients = %s, independent of R: %s.\n      So |q(x2 + eps d) - q(x2)| <= C eps (|B| + eps) R^-6"
          " + C eps R^-8 near flat data: step (6)'s bound, with eps ~ eta + |dm|."
          % (lin0, eB0, r6, sc6, r8, sc8), flush=True)
    return ok


CHECKS = [("F1", f1), ("F2", f2), ("F3", f3), ("F4", f4)]


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
