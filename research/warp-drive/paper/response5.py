#!/usr/bin/env python3
"""response5.py -- re-derives the numbers of RESPONSE-HL-5D.md (the five-dimensional counterpart of Huneau and Luk's
high-frequency theorem), independently of the instruments the proof was built with.

Each check is exact (sympy) and carries negative controls, each run on its own: the same computation with one
ingredient changed must fail, so that a check which passes is not passing vacuously.

  R1 The reduction.  For g5 = g3 + e^(2A) dphi1^2 + e^(2B) dphi2^2 (a generic Lorentzian 3-metric g3, generic A, B),
     with psi := A + B, omega := (B - A)/2 and h := e^(2 psi) g3:
       Ric[h]_ab = Ric[g5]_ab + (3/2) d_a psi d_b psi + 2 d_a omega d_b omega + (e^-2A R11 + e^-2B R22) g3_ab,
       e^(2 psi) box_h psi = -(e^-2A R11 + e^-2B R22),   e^(2 psi) box_h omega = (e^-2A R11 - e^-2B R22)/2,
     R11, R22 the phi1 phi1 and phi2 phi2 components of Ric[g5], and Ric[g5]_(a phi) = Ric[g5]_(phi1 phi2) = 0.  So
     5D vacuum in the class is 2+1 gravity on h coupled to two free waves with target metric (3/2) dpsi^2 + 2 domega^2.
     Exact: the identities are tensorial, so at a point the coordinates are taken normal for g3 (g3 = eta, dg3 = 0), and
     the second derivatives of g3 and the 2-jets of A and B are free symbols.  Control: 3/2 replaced by 1.
  R2 The background.  g0 = -dtau^2 + dr^2 + r^2 dOmega_3^2 + (mu(v)/r^2) dv^2, v = tau + r, is five-dimensional
     Vaidya: Ric(g0) = (3 mu'(v) / (2 r^3)) dv dv, and the (tau, r) block has determinant -1.  Control: mu/r in
     place of mu/r^2 is not of this form.
  R3 The curvature scale.  The Kretschmann scalar is 72 mu^2 / r^8, for constant mu and (in Eddington-Finkelstein
     coordinates) for mu = mu(v); the quantum boundary x = l5^2 sqrt(K) = 1 is r = r_q := (sqrt(72) mu l5^2)^(1/4),
     and r_q <= sqrt(mu) (the boundary lies inside the apparent horizon r = sqrt(mu)) exactly when mu >= sqrt(72)
     l5^2.  Controls: 48 in place of 72, in either computation.
  R4 The domain.  ell := g0^-1 dv is null and geodesic; g0^-1(dtau, dtau) = -1 - mu/r^2,
     g0^-1(dr, dr) = 1 - mu/r^2, g0^-1(dr, dtau) = mu/r^2, g0^-1(d(v + tau), d(v + tau)) = -3 - mu/r^2.  The tau-lines
     are spacelike where r^2 < mu (g0(d_tau, d_tau) = -1 + mu/r^2), which is why the local theory is applied in other
     coordinates.  Control: the outgoing covector dv - 2 dr is not null.
  R5 The constraints as an evolution in r.  On the slice tau = tau0 of g0, with gamma + a dr dr and K + w Pi + q (dth dr
     + dr dth), the linearised constraint map (J, rho) = (2(-div K + d tr K), R - |K|^2 + (tr K)^2) has principal part
     rho: (3 r^3 / (r^2 + mu)^2) d_r a - (1/(r^2 + mu)) d_th^2 a (forward parabolic in r; no d_r^2 a, d_r d_th a, no
     derivative of w, q),  J_r: 6 d_r w - (2/r^2) d_th q,  J_th: -(2 r^2/(r^2 + mu)) d_r q + 4 d_th w; the symmetrizer
     S = diag(1, -1/(2 r^2)) gives S A0 = diag(6, 1/(r^2 + mu)) > 0 and S A^th symmetric; the speeds satisfy
     c^2 = 2 (r^2 + mu)/(3 r^4); and 3 r^3/(r^2 + mu)^2 = theta^3 H with theta^2 = r^2/(r^2 + mu), H = 3/sqrt(r^2 + mu).
     Control: the perturbation a gamma in place of a dr dr brings d_r^2 a into rho.
  R6 The waves' average and the boundary's margin.  With c^2 = (1 + x)/2, s^2 = (1 - x)/2 and h^2 = 2/(1 + x^2),
     h^2 (c^4 + s^4) = 1, so the averaged dust is the same at every x; 4 (a^2 + ab + b^2) = (2a + b)^2 + 3 b^2.  For
     Phi = r - r_q(v), g0^-1(dPhi, dPhi) = 1 - mu/r^2 - 2 r_q' with r_q' = r_q mu'/(4 mu) >= 0, and at r = r_q,
     mu/r_q^2 = sqrt(mu/(sqrt(72) l5^2)); so on x = 1, g0^-1(dPhi, dPhi) <= 1 - sqrt(mu0/(sqrt(72) l5^2)), negative
     when mu0 > sqrt(72) l5^2.  Controls, each run on its own: h = 1; (2a + b)^2 + 2 b^2; Phi = r + r_q; sqrt(48).

python3 response5.py [--selftest] [--full]
--full also runs the selftests of the five proof instruments (about 20 minutes; data5.py takes about 14).
"""
import os
import random
import subprocess
import sys
import time

import sympy as sp


def christoffel(g, X):
    n = len(X)
    gi = g.inv()
    d = [[[sp.diff(g[i, j], X[k]) for k in range(n)] for j in range(n)] for i in range(n)]
    return gi, [[[sum(gi[a, m]*(d[m][b][c] + d[m][c][b] - d[b][c][m]) for m in range(n))/2
                  for c in range(n)] for b in range(n)] for a in range(n)]


def ricci(g, X):
    n = len(X)
    gi, G = christoffel(g, X)
    R = sp.zeros(n)
    for b in range(n):
        for c in range(b, n):
            e = sum(sp.diff(G[a][b][c], X[a]) for a in range(n)) - sum(sp.diff(G[a][b][a], X[c]) for a in range(n))
            e += sum(G[a][a][m]*G[m][b][c] - G[a][c][m]*G[m][b][a] for a in range(n) for m in range(n))
            R[b, c] = R[c, b] = e
    return R, gi, G


# ---------------------------------------------------------------- R1 the reduction

def jet_ricci(g, X, pt, dps=50, exact=False):
    """Ricci tensor, inverse metric and Christoffel symbols of g at the point pt, from the 2-jet of g there (exact,
    or to dps digits): R_bc = d_a G^a_bc - d_c G^a_ba + G^a_am G^m_bc - G^a_cm G^m_ba."""
    n, sub = len(X), dict(zip(X, pt))
    ev = (lambda e: e.subs(sub)) if exact else (lambda e: sp.N(e.subs(sub), dps))
    G0 = g.applyfunc(ev)
    d1 = [g.diff(X[k]).applyfunc(ev) for k in range(n)]
    d2 = [[g.diff(X[k]).diff(X[l]).applyfunc(ev) for l in range(n)] for k in range(n)]
    gi = G0.inv()
    low = [[[(d1[c][m, b] + d1[b][m, c] - d1[m][b, c])/2 for c in range(n)] for b in range(n)] for m in range(n)]
    dlow = [[[[(d2[k][c][m, b] + d2[k][b][m, c] - d2[k][m][b, c])/2 for c in range(n)] for b in range(n)]
             for m in range(n)] for k in range(n)]
    dgi = [-gi*d1[k]*gi for k in range(n)]
    Gam = [[[sum(gi[a, m]*low[m][b][c] for m in range(n)) for c in range(n)] for b in range(n)] for a in range(n)]
    dGam = [[[[sum(dgi[k][a, m]*low[m][b][c] + gi[a, m]*dlow[k][m][b][c] for m in range(n)) for c in range(n)]
              for b in range(n)] for a in range(n)] for k in range(n)]
    R = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            R[b, c] = (sum(dGam[a][a][b][c] - dGam[c][a][b][a] for a in range(n))
                       + sum(Gam[a][a][m]*Gam[m][b][c] - Gam[a][c][m]*Gam[m][b][a] for a in range(n) for m in range(n)))
    return R, gi, Gam


def r1(control=False):
    """exact: the identities are tensorial, so at a point take coordinates in which g3 = eta and dg3 = 0 (normal
    coordinates of g3); the second derivatives of g3 and the 2-jets of A and B are free symbols"""
    t, x, y, p1, p2 = sp.symbols("t x y p1 p2")
    X3 = [t, x, y]
    eta = sp.diag(-1, 1, 1)
    g3 = sp.Matrix(eta)
    for a_ in range(3):
        for b_ in range(a_, 3):
            q = 0
            for c_ in range(3):
                for d_ in range(c_, 3):
                    w_ = sp.Symbol(f"G{a_}{b_}_{c_}{d_}")
                    q += w_*X3[c_]*X3[d_]*(sp.Rational(1, 2) if c_ == d_ else 1)
            g3[a_, b_] = g3[b_, a_] = eta[a_, b_] + q

    def jet(nm):
        f = sp.Symbol(nm + "0") + sum(sp.Symbol(f"{nm}{c_}")*X3[c_] for c_ in range(3))
        for c_ in range(3):
            for d_ in range(c_, 3):
                f += sp.Symbol(f"{nm}{c_}{d_}")*X3[c_]*X3[d_]*(sp.Rational(1, 2) if c_ == d_ else 1)
        return f
    A, B = jet("A"), jet("B")
    g5 = sp.zeros(5)
    g5[:3, :3] = g3
    g5[3, 3] = sp.exp(2*A)
    g5[4, 4] = sp.exp(2*B)
    psi, om = A + B, (B - A)/2
    h = sp.exp(2*psi)*g3
    c32 = sp.Integer(1) if control else sp.Rational(3, 2)
    origin = (0, 0, 0)
    sub = dict(zip(X3, origin))
    ev = lambda e: e.subs(sub)
    R5, _, _ = jet_ricci(g5, X3 + [p1, p2], origin + (0, 0), exact=True)
    Rh, hi, Gh = jet_ricci(h, X3, origin, exact=True)
    dpsi = [ev(sp.diff(psi, z)) for z in X3]
    dom = [ev(sp.diff(om, z)) for z in X3]

    def boxh(f):
        df = [ev(sp.diff(f, z)) for z in X3]
        return sum(hi[a_, b_]*(ev(sp.diff(f, X3[a_], X3[b_])) - sum(Gh[c_][a_][b_]*df[c_] for c_ in range(3)))
                   for a_ in range(3) for b_ in range(3))
    e2A, e2B = ev(sp.exp(-2*A)), ev(sp.exp(-2*B))
    S = e2A*R5[3, 3] + e2B*R5[4, 4]
    G3, e2psi = g3.applyfunc(ev), ev(sp.exp(2*psi))
    vals = [Rh[a_, b_] - R5[a_, b_] - c32*dpsi[a_]*dpsi[b_] - 2*dom[a_]*dom[b_] - S*G3[a_, b_]
            for a_ in range(3) for b_ in range(a_, 3)]
    vals += [e2psi*boxh(psi) + S, e2psi*boxh(om) - (e2A*R5[3, 3] - e2B*R5[4, 4])/2]
    vals += [R5[a_, b_] for a_ in range(3) for b_ in (3, 4)] + [R5[3, 4]]
    return all(sp.simplify(sp.expand(v_)) == 0 for v_ in vals)


# ---------------------------------------------------------------- the background

tau, r, th, p1, p2 = sp.symbols("tau r theta phi1 phi2", real=True)
v = tau + r
X5 = [tau, r, th, p1, p2]


def g0_of(mu, power=2):
    m = mu/r**power
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0], g[1, 1] = -1 + m, m, m, 1 + m
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2
    return g


def r2(control=False):
    muf = sp.Function("mu")
    g = g0_of(muf(v), 1 if control else 2)
    R, _, _ = ricci(g, X5)
    dv = sp.Matrix([1, 1, 0, 0, 0])
    target = 3*sp.diff(muf(v), tau)/(2*r**3)*dv*dv.T
    ok = all(sp.simplify(R[i, j] - target[i, j]) == 0 for i in range(5) for j in range(5))
    det = sp.simplify(g[0, 0]*g[1, 1] - g[0, 1]**2)
    return ok and det == -1


def kretschmann_vaidya(c):
    """K = c mu(v)^2/r^8 for 5D Vaidya with mu = mu(v), computed in ingoing Eddington-Finkelstein coordinates"""
    vv = sp.Symbol("v", real=True)
    Y = [vv, r, th, p1, p2]
    muf = sp.Function("mu")(vv)
    f = 1 - muf/r**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -f, 1, 1
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2
    gi, G = christoffel(g, Y)
    n = 5
    low = {}
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                for d in range(n):
                    e = sp.diff(G[a][b][d], Y[c_]) - sp.diff(G[a][b][c_], Y[d])
                    e += sum(G[a][c_][m]*G[m][b][d] - G[a][d][m]*G[m][b][c_] for m in range(n))
                    low[a, b, c_, d] = e
    lo = {}
    for k in low:
        a, b, c_, d = k
        lo[k] = sp.simplify(sum(g[a, m]*low[m, b, c_, d] for m in range(n)))
    up = {}
    for k, val in lo.items():
        if val == 0:
            continue
        a, b, c_, d = k
        up[k] = sum(gi[a, i]*gi[b, j]*gi[c_, kk]*gi[d, l]*lo[i, j, kk, l] for i in range(n) for j in range(n)
                    for kk in range(n) for l in range(n) if lo[i, j, kk, l] != 0 and gi[a, i] != 0 and gi[b, j] != 0
                    and gi[c_, kk] != 0 and gi[d, l] != 0)
    K = sp.simplify(sum(lo[k]*up[k] for k in up))
    return sp.simplify(K - c*muf**2/r**8) == 0


def r3(control=False):
    mu, l5 = sp.symbols("mu l5", positive=True)
    g = g0_of(mu)
    gi, G = christoffel(g, X5)
    n = 5
    Riem = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(G[a][b][d], X5[c]) - sp.diff(G[a][b][c], X5[d])
                    e += sum(G[a][c][m]*G[m][b][d] - G[a][d][m]*G[m][b][c] for m in range(n))
                    Riem[a, b, c, d] = sp.simplify(e)
    low = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    low[a, b, c, d] = sum(g[a, m]*Riem[m, b, c, d] for m in range(n))
    up = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    up[a, b, c, d] = sum(gi[a, i]*gi[b, j]*gi[c, k]*gi[d, l]*low[i, j, k, l]
                                         for i in range(n) for j in range(n) for k in range(n) for l in range(n)
                                         if low[i, j, k, l] != 0)
    K = sp.simplify(sum(low[k]*up[k] for k in low if low[k] != 0))
    c = 48 if control == 1 else 72
    if not kretschmann_vaidya(48 if control == 2 else 72):
        return False
    okK = sp.simplify(K - c*mu**2/r**8) == 0
    rq = (sp.sqrt(72)*mu*l5**2)**sp.Rational(1, 4)
    okx = sp.simplify(l5**2*sp.sqrt(c*mu**2/rq**8) - 1) == 0
    # r_q <= sqrt(mu)  <=>  r_q^4 <= mu^2  <=>  sqrt(72) mu l5^2 <= mu^2  <=>  mu >= sqrt(72) l5^2
    oki = sp.simplify(rq**4 - mu**2 - mu*(sp.sqrt(72)*l5**2 - mu)) == 0
    return okK and okx and oki


def r4(control=False):
    muf = sp.Function("mu")
    g = g0_of(muf(v))
    gi, G = christoffel(g, X5)
    dt_ = sp.Matrix([1, 0, 0, 0, 0])
    dr_ = sp.Matrix([0, 1, 0, 0, 0])
    dv_ = dt_ + dr_
    q = lambda a, b: sp.simplify((a.T*gi*b)[0, 0])
    m = muf(v)/r**2
    probe = dv_ - 2*dr_ if control else dv_
    ok = q(probe, probe) == 0
    ell = gi*dv_
    acc = [sp.simplify(sum(ell[b]*sp.diff(ell[a], X5[b]) for b in range(5))
                       + sum(G[a][b][c]*ell[b]*ell[c] for b in range(5) for c in range(5))) for a in range(5)]
    ok = ok and all(x == 0 for x in acc)
    ok = ok and sp.simplify(q(dt_, dt_) - (-1 - m)) == 0 and sp.simplify(q(dr_, dr_) - (1 - m)) == 0
    ok = ok and sp.simplify(q(dr_, dt_) - m) == 0 and sp.simplify(q(dv_ + dt_, dv_ + dt_) - (-3 - m)) == 0
    ok = ok and sp.simplify(g[0, 0] - (-1 + m)) == 0
    return ok


# ---------------------------------------------------------------- R5 the constraints at the background

def r5(control=False):
    tau0 = sp.Symbol("tau0", real=True)
    muf = sp.Function("mu")
    Y = [r, th, p1, p2]
    m = muf(tau + r)/r**2
    gam = sp.diag(1 + m, r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2)
    beta_low = [m, 0, 0, 0]
    gi = gam.inv()
    N = 1/sp.sqrt(1 + m)
    _, G = christoffel(gam, Y)
    K = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            lie = sp.diff(beta_low[j], Y[i]) + sp.diff(beta_low[i], Y[j])
            lie -= 2*sum(G[k][i][j]*beta_low[k] for k in range(4))
            K[i, j] = (sp.diff(gam[i, j], tau) - lie)/(2*N)
    eps = sp.Symbol("eps")
    a, w, q = [sp.Function(nm)(r, th) for nm in ("a", "w", "q")]
    h = gam*a if control else sp.diag(a, 0, 0, 0)
    Q = sp.zeros(4)
    for i in (1, 2, 3):
        Q[i, i] = w*gam[i, i]
    Q[0, 1] = Q[1, 0] = q
    gp = gam + eps*h
    gpi = gi - eps*gi*h*gi
    Kp = K + eps*Q
    _, Gp = christoffel(gp, Y)

    def ric_scalar(g_, gi_, G_):
        n = 4
        Rs = 0
        for b in range(n):
            for c in range(n):
                if gi_[b, c] == 0:
                    continue
                e = sum(sp.diff(G_[a_][b][c], Y[a_]) - sp.diff(G_[a_][b][a_], Y[c]) for a_ in range(n))
                e += sum(G_[a_][a_][mm]*G_[mm][b][c] - G_[a_][c][mm]*G_[mm][b][a_] for a_ in range(n) for mm in range(n))
                Rs += gi_[b, c]*e
        return Rs
    trK = sum(gpi[i, j]*Kp[i, j] for i in range(4) for j in range(4))
    Kup = gpi*Kp*gpi
    KK = sum(Kp[i, j]*Kup[i, j] for i in range(4) for j in range(4))
    rho = ric_scalar(gp, gpi, Gp) - KK + trK**2
    # div K_j = gp^{ik} nabla_k K_ij
    J = []
    for j in (0, 1):
        div = 0
        for i in range(4):
            for k in range(4):
                if gpi[i, k] == 0:
                    continue
                nab = sp.diff(Kp[i, j], Y[k]) - sum(Gp[l][k][i]*Kp[l, j] + Gp[l][k][j]*Kp[i, l] for l in range(4))
                div += gpi[i, k]*nab
        J.append(2*(-div + sp.diff(trK, Y[j])))
    lin = [sp.diff(e, eps).subs(eps, 0) for e in (J[0], J[1], rho)]
    lin = [e.subs(tau, tau0) for e in lin]
    mu0 = muf(tau0 + r)
    D = sp.Derivative
    cf = lambda e, d: sp.simplify(sp.expand(e).coeff(d))
    Jr, Jt, rh = lin
    ok = True
    ok &= sp.simplify(cf(rh, D(a, r)) - 3*r**3/(r**2 + mu0)**2) == 0
    ok &= sp.simplify(cf(rh, D(a, (th, 2))) + 1/(r**2 + mu0)) == 0
    ok &= all(cf(rh, d) == 0 for d in (D(a, (r, 2)), D(a, r, th), D(w, r), D(w, th), D(q, r), D(q, th)))
    A0 = sp.Matrix([[cf(Jr, D(w, r)), cf(Jr, D(q, r))], [cf(Jt, D(w, r)), cf(Jt, D(q, r))]])
    At = sp.Matrix([[cf(Jr, D(w, th)), cf(Jr, D(q, th))], [cf(Jt, D(w, th)), cf(Jt, D(q, th))]])
    ok &= sp.simplify(A0 - sp.diag(6, -2*r**2/(r**2 + mu0))) == sp.zeros(2)
    ok &= sp.simplify(At - sp.Matrix([[0, -2/r**2], [4, 0]])) == sp.zeros(2)
    S = sp.diag(1, -1/(2*r**2))
    SA0, SAt = sp.simplify(S*A0), sp.simplify(S*At)
    ok &= sp.simplify(SA0 - sp.diag(6, 1/(r**2 + mu0))) == sp.zeros(2)
    ok &= sp.simplify(SAt - SAt.T) == sp.zeros(2)
    ev = (A0.inv()*At).eigenvals()
    ok &= all(sp.simplify(e**2 - 2*(r**2 + mu0)/(3*r**4)) == 0 for e in ev)
    theta3, H = r**3/(r**2 + mu0)**sp.Rational(3, 2), 3/sp.sqrt(r**2 + mu0)   # theta = r/sqrt(r^2 + mu) > 0
    ok &= sp.simplify(theta3*H - 3*r**3/(r**2 + mu0)**2) == 0
    return bool(ok)


# ---------------------------------------------------------------- R6 the waves' average and the boundary's margin

def r6(control=0):
    """control 1: h = 1; 2: a wrong form for the dust; 3: Phi = r + r_q; 4: sqrt(48) in place of sqrt(72)"""
    x, a, b = sp.symbols("x a b", real=True)
    c2, s2 = (1 + x)/2, (1 - x)/2
    h2 = sp.Integer(1) if control == 1 else 2/(1 + x**2)
    ok = sp.simplify(h2*(c2**2 + s2**2) - 1) == 0                       # the dust is round: h^2 (c^4 + s^4) = 1
    rhs = (2*a + b)**2 + (2 if control == 2 else 3)*b**2
    ok &= sp.expand(4*(a**2 + a*b + b**2) - rhs) == 0                    # the dust's form is positive definite
    muf = sp.Function("mu")
    l5 = sp.Symbol("l5", positive=True)
    rho = (sp.sqrt(72)*muf(v)*l5**2)**sp.Rational(1, 4)
    g = g0_of(muf(v))
    gi = g.inv()
    Phi = r + rho if control == 3 else r - rho
    dPhi = sp.Matrix([sp.diff(Phi, z) for z in X5])
    q = sp.simplify((dPhi.T*gi*dPhi)[0, 0])
    drho = sp.diff(muf(v), tau)*sp.diff(rho, muf(v))                    # d rho / dv
    ok &= sp.simplify(q - (1 - muf(v)/r**2 - 2*drho)) == 0
    ok &= sp.simplify(drho - rho*sp.diff(muf(v), tau)/(4*muf(v))) == 0
    mu, L = sp.symbols("mu L", positive=True)           # at r = r_q: mu/r_q^2 = sqrt(mu/(sqrt(72) l5^2))
    rq = (sp.sqrt(72)*mu*L**2)**sp.Rational(1, 4)
    c72 = 48 if control == 4 else 72
    ok &= sp.simplify(mu/rq**2 - sp.sqrt(mu/(sp.sqrt(c72)*L**2))) == 0
    return bool(ok)

CHECKS = [("R1 the reduction: 2+1 gravity on h = e^(2 psi) g3 with target (3/2) dpsi^2 + 2 domega^2", r1, 1),
          ("R2 the background is 5D Vaidya, Ric(g0) = (3 mu'/(2 r^3)) dv dv", r2, 1),
          ("R3 Kretschmann 72 mu^2/r^8 (mu constant, and mu(v)); x = 1 at r_q; r_q <= sqrt(mu) iff ...", r3, 2),
          ("R4 ell null geodesic; the contractions of the domain; tau-lines spacelike where r^2 < mu", r4, 1),
          ("R5 the constraints at the background: parabolic in a, symmetric hyperbolic in (w, q)", r5, 1),
          ("R6 the dust is round and positive; g0^-1(dPhi, dPhi) = 1 - mu/r^2 - 2 r_q' at x = 1", r6, 4)]

INSTRUMENTS = ["ks5.py", "foliation5.py", "lead5.py", "ansatz5.py", "data5.py"]


def selftest(full=False):
    ok_all = True
    for name, f, nc in CHECKS:
        t0 = time.time()
        good = f()
        control = any(f(control=k) for k in range(1, nc + 1))      # each control must be rejected on its own
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<104} {state} {time.time() - t0:5.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    if full:
        here = os.path.dirname(os.path.abspath(__file__))
        inst = os.path.join(here, "..", "docket68", "n1star")
        for f in INSTRUMENTS:
            p = subprocess.run([sys.executable, os.path.join(inst, f), "--selftest"], cwd=inst,
                               capture_output=True, text=True)
            last = (p.stdout.strip().splitlines() or ["(no output)"])[-1]
            ok_all &= p.returncode == 0
            print(f"instrument {f:<14} {last}")
    print(f"response5.py: {'all checks pass' if ok_all else 'FAILED'}")
    return ok_all


if __name__ == "__main__":
    random.seed(0)
    sys.exit(0 if selftest("--full" in sys.argv) else 1)
