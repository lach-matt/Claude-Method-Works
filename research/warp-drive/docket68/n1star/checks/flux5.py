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
     (computed: R^6 q at order A^2 depends on x/R alone), so a difference of two such data of sizes 1 and eta + |m -
     mubar| gives |q(xhat) - q(gamma^mubar)| <= C (eta + |m - mubar|) R^-6 on Gamma(R, 4R), whose volume is 255 pi^2
     R^4/2: the integral is O((eta + |m - mubar|) R^-2); with 6 pi^2 (m - mubar) = that + O(|m - mubar| R^-2) + O(eta),
     |m - mubar| <= C eta once C R^-2 < 3 pi^2 (the inequality solved exactly).
  Control: the flux built with + d_i tr h in place of - d_i tr h is not the divergence of DR(h) (F2's identity fails),
     and on F1's slice it gives -2 pi^2 m, not 6 pi^2 m.

Labels: computed (exact, sympy).

Run: python3 checks/flux5.py   (a few minutes)
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


def curvature_at(g, pt, inverse=None):
    """scalar curvature, Christoffel symbols and the inverse at a point, from the jets (no symbolic simplification)"""
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
                for d in range(n):
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
        # the momentum constraint needs dK: from the symbolic K's derivatives at the point
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
    if control:
        return False
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
    R, _, _ = curvature_at(sp.eye(4) + h, pt, inverse=gi)
    F = flux_vector(h)
    DR = sp.expand(sum(sp.diff(F[i], X[i]) for i in range(4)).subs(pt))
    Ku = gi*K.subs(pt)
    q = sp.expand(DR - (R - sum(Ku[i, j]*Ku[j, i] for i in range(4) for j in range(4)) + Ku.trace()**2))
    q1 = sp.simplify(q.coeff(A, 1))
    scal = sp.simplify(q.coeff(A, 2)*Rr**6)
    ok = q1 == 0 and scal != 0 and not scal.has(Rr)
    C, d, mm, R_ = sp.symbols("C eta dm R_", positive=True)
    sol = sp.solve(sp.Eq(6*sp.pi**2*mm, C*(d + mm)/R_**2 + C*d), mm)[0]
    print("  F3: q at order A^1: %s; R^6 q at order A^2 = %s (independent of R: %s); 6 pi^2 |dm| <= C (eta + |dm|)/R^2 +"
          " C eta solves to |dm| <= %s" % (q1, str(scal)[:30] + "...", ok, sp.simplify(sol)), flush=True)
    return ok


CHECKS = [("F1", f1), ("F2", f2), ("F3", f3)]


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
