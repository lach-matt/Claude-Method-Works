#!/usr/bin/env python3
"""indepcons5.py -- Lemma 6.3 (a) on all fields: the constraint map's principal part in U = (a, w, q) at the data of g0
on Sigma, for fields of every angle (D619; the section 6 reader's n1, its indep_constraints.py made a program).

data5.py S3 computes Lemma 6.3 (a) in the symmetric class (fields of (r, th), q = q_th dth).  Lemma 6.4 commutes the
Killing fields of the round S^3 through (6.4), which leaves that class, so the symmetrizer must serve the system on all
of (a, w, q_th, q_p1, q_p2), functions of (r, th, p1, p2).  This program recomputes the principal part independently of
data5.py: the slice metric gamma = (1 + mu/r^2) dr^2 + r^2 (dth^2 + cos^2 th dp1^2 + sin^2 th dp2^2), K of the static
slice (mu constant: principal parts are algebraic in mu), Psi(U) = (gamma + a dr dr, K + w Pi + q dr + dr q) of (6.3),
the constraint map (J, rho) = (2(-div K + d tr K), R - |K|^2 + (tr K)^2), linearised in U.

  P1 (exact) rho: the coefficient of d_r a is alpha = 3 r^3/(r^2 + mu)^2, the angular second-order part is
     -theta^2 Delta_Pi on all three angles (theta^2 = r^2/(r^2 + mu)), with no d_r^2 a, no d_r d_A a and no derivative
     of (w, q).  Control: the Ricci scalar with its term -d_c Gamma^a_(b a) dropped (a mutation of the code under test)
     fails P1.
  P2 (exact) J: J_r = 6 d_r w - 2 Pi^(AB) d_A q_B + ..., J_A = -2 gamma^(rr) d_r q_A + 4 d_A w + ..., no second
     derivative of a; with S = diag(1, -(1/2) Pi^-1) the matrices S A^B are symmetric for B = th, p1, p2 and S A0 =
     diag(6, gamma^rr Pi^-1) is diagonal and positive (at points inside and outside the horizon r^2 = mu).
     Control: J with its trace term d tr K scaled by 1/3 (the mutation that cancels the w part of the divergence) fails
     P2: S A^B is then not symmetric.
  P3 (exact) Pol(Y) = Y(ell, .) - (1/2) dv tr_g0 Y has rank 5 at r = 1/2, mu = 1 (inside the horizon), in Cartesian
     Kerr-Schild coordinates, with g0^-1(dv, dv) = 0 (the point of data5.py S1, recomputed).  Control (non-vacuity of
     the rank test): on the nine-dimensional space {Y(ell, .) = 0, tr_g0 Y = 0} the same computation gives rank 0.

Labels: P1-P3 computed (exact, sympy).  Run: python3 checks/indepcons5.py   (a few seconds)
"""
import sys
import textwrap

import sympy as sp

r, th, p1, p2, mu, eps = sp.symbols('r theta p1 p2 mu epsilon', positive=True)
X = [r, th, p1, p2]
n = 4
m = mu/r**2
gam = sp.diag(1 + m, r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2)
gi = gam.inv()
a = sp.Function('a')(*X)
w = sp.Function('w')(*X)
q = [sp.Function('q%d' % k)(*X) for k in range(3)]       # q_th, q_p1, q_p2
POINTS = [{mu: sp.Rational(1, 2), r: sp.Rational(1, 3), th: sp.Rational(1, 3)},     # inside the horizon
          {mu: sp.Rational(1, 2), r: sp.Integer(2), th: sp.Rational(6, 5)}]          # outside


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def chris(g, ginv):
    return [[[sp.expand(sum(ginv[i, l]*(sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                           for l in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]


def ricci_scalar(g, ginv, mutate=False):
    G = chris(g, ginv)
    R = 0
    for b in range(n):
        for c in range(n):
            if ginv[b, c] == 0:
                continue
            e = 0
            for aa in range(n):
                e += sp.diff(G[aa][b][c], X[aa]) - (0 if mutate else sp.diff(G[aa][b][aa], X[c]))
                for d in range(n):
                    e += G[aa][aa][d]*G[d][b][c] - G[aa][c][d]*G[d][b][aa]
            R += ginv[b, c]*e
    return R


def background_K():
    """K of g0's slice: N^2 = 1/(1 + m), beta_r = m (covariant), K = -(1/2N) L_beta gamma (d_tau gamma = 0)"""
    N = 1/sp.sqrt(1 + m)
    beta_low = [m, 0, 0, 0]
    G0 = chris(gam, gi)
    Kb = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            Dij = sp.diff(beta_low[j], X[i]) - sum(G0[k][i][j]*beta_low[k] for k in range(n))
            Dji = sp.diff(beta_low[i], X[j]) - sum(G0[k][j][i]*beta_low[k] for k in range(n))
            Kb[i, j] = sp.simplify(-(Dij + Dji)/(2*N))
    return Kb


def linearised(mutate_R=False, trace_coef=1):
    h = sp.zeros(n)
    h[0, 0] = a
    Q = sp.zeros(n)
    for A in (1, 2, 3):
        Q[A, A] = w*gam[A, A]
        Q[0, A] = Q[A, 0] = q[A - 1]
    gp = gam + eps*h
    gpi = gi - eps*gi*h*gi
    Kp = background_K() + eps*Q
    G = chris(gp, gpi)
    trK = sum(gpi[i, j]*Kp[i, j] for i in range(n) for j in range(n))
    K2 = sum(gpi[i, k]*gpi[j, l]*Kp[i, j]*Kp[k, l] for i in range(n) for j in range(n) for k in range(n)
             for l in range(n))
    rho = ricci_scalar(gp, gpi, mutate_R) - K2 + trK**2
    J = []
    for i in range(n):
        divK = 0
        for j in range(n):
            for k in range(n):
                cov = sp.diff(Kp[i, j], X[k]) - sum(G[l][k][i]*Kp[l, j] + G[l][k][j]*Kp[i, l] for l in range(n))
                divK += gpi[j, k]*cov
        J.append(2*(-divK + trace_coef*sp.diff(trK, X[i])))
    lin = [sp.expand(sp.diff(e, eps).subs(eps, 0)) for e in J + [rho]]
    return lin[:4], lin[4]


def co(e, f, *vars_):
    d = f if not vars_ else sp.Derivative(f, *vars_)
    return sp.simplify(sp.expand(e).coeff(d))


def p1(control=False):
    _, rhol = linearised(mutate_R=control)
    alpha = co(rhol, a, r)
    ok = sp.simplify(alpha - 3*r**3/(r**2 + mu)**2) == 0
    ok &= co(rhol, a, r, r) == 0 and all(co(rhol, a, r, x) == 0 for x in (th, p1, p2))
    theta2 = r**2/(r**2 + mu)
    for A in (1, 2, 3):
        ok &= sp.simplify(co(rhol, a, X[A], X[A]) + theta2*gi[A, A]) == 0
    ok &= all(co(rhol, a, X[A], X[B]) == 0 for A in (1, 2, 3) for B in (1, 2, 3) if A < B)
    ok &= all(co(rhol, f, x) == 0 for f in [w] + q for x in X)
    if not control:
        out("  P1 rho: alpha = %s; -theta^2 Delta_Pi on th, p1, p2; no d_r^2 a, no d_r d_A a, no d(w, q): %s; lower"
            " order (for the record): a_th %s, a %s, w %s" % (sp.factor(alpha), ok, co(rhol, a, th),
                                                            sp.factor(co(rhol, a)), sp.factor(co(rhol, w))))
    return ok


def p2(control=False):
    Jl, _ = linearised(trace_coef=sp.Rational(1, 3) if control else 1)
    cols = [w] + q
    A0 = sp.Matrix(4, 4, lambda i, j: co(Jl[i], cols[j], r))
    AB = [sp.Matrix(4, 4, lambda i, j, B=B: co(Jl[i], cols[j], X[B])) for B in (1, 2, 3)]
    second_a = all(co(Jl[i], a, x, y) == 0 for i in range(4) for x in X for y in X)
    S = sp.diag(1, *[-gi[A, A]/2 for A in (1, 2, 3)])
    SA0 = sp.simplify(S*A0)
    sym = all(sp.simplify(S*M - (S*M).T) == sp.zeros(4) for M in AB)
    diag = sp.simplify(SA0 - sp.diag(*[SA0[i, i] for i in range(4)])) == sp.zeros(4)
    pos = diag and all(sp.N(SA0[i, i].subs(P)) > 0 for i in range(4) for P in POINTS)
    form = (sp.simplify(A0 - sp.diag(6, *[-2*gi[0, 0]]*3)) == sp.zeros(4)
            and all(sp.simplify(AB[B - 1][0, B] + 2*gi[B, B]) == 0 and sp.simplify(AB[B - 1][B, 0] - 4) == 0
                    for B in (1, 2, 3)))
    ok = second_a and sym and pos and form
    if not control:
        out("  P2 A0 = %s; A^th = %s; A^p1 = %s; S A0 = %s.  J_r = 6 d_r w - 2 Pi^(AB) d_A q_B, J_A = -2 gamma^rr d_r q_A"
            " + 4 d_A w: %s; no second derivative of a in J: %s; S A^B symmetric for B = th, p1, p2: %s; S A0 diagonal"
            " positive at r^2 < mu and r^2 > mu: %s" % (
                sp.simplify(A0).tolist(), sp.simplify(AB[0]).tolist(), sp.simplify(AB[1]).tolist(),
                [sp.factor(SA0[i, i]) for i in range(4)], form, second_a, sym, pos))
    return ok


def pol_matrix(rv, muv, basis=None):
    xs = sp.Matrix([rv, 0, 0, 0])
    xh = xs/rv
    eta = sp.diag(-1, 1, 1, 1, 1)
    dv = sp.Matrix([1] + list(xh))
    g = eta + (muv/rv**2)*dv*dv.T
    ginv = g.inv()
    ell = ginv*dv
    Ys = []
    for i in range(5):
        for j in range(i, 5):
            Y = sp.zeros(5)
            Y[i, j] = Y[j, i] = 1
            Ys.append(Y)

    def pol(Y):
        tr = sum(ginv[aa, bb]*Y[aa, bb] for aa in range(5) for bb in range(5))
        return [sum(ell[aa]*Y[aa, bb] for aa in range(5)) - dv[bb]*tr/2 for bb in range(5)]

    if basis == "W":          # the subspace Y(ell, .) = 0, tr Y = 0, as combinations of the 15 basis elements
        cons = sp.Matrix([[sum(ell[aa]*Y[aa, bb] for aa in range(5)) for Y in Ys] for bb in range(5)]
                         + [[sum(ginv[aa, bb]*Y[aa, bb] for aa in range(5) for bb in range(5)) for Y in Ys]])
        Ys = [sum((c*Y for c, Y in zip(v, Ys)), sp.zeros(5)) for v in cons.nullspace()]
    return sp.Matrix([pol(Y) for Y in Ys]), sp.simplify((dv.T*ginv*dv)[0]), len(Ys)


def p3(control=False):
    if control:
        M, _, dim = pol_matrix(sp.Rational(1, 2), 1, basis="W")
        return dim == 9 and M.rank() == 5
    M, null, dim = pol_matrix(sp.Rational(1, 2), 1)
    rk = M.rank()
    out("  P3 Pol rank at r = 1/2, mu = 1 (inside the horizon), Cartesian Kerr-Schild: %d on %d basis elements;"
        " g0^-1(dv, dv) = %s" % (rk, dim, null))
    return rk == 5 and null == 0


def main():
    ok = True
    for name, f in (("P1", p1), ("P2", p2), ("P3", p3)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("indepcons5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
