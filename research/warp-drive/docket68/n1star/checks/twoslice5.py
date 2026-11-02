#!/usr/bin/env python3
"""twoslice5: the constraints on the two-dust slice, with both families and any radial phases (FAMILIES5-FULL.md
section 6).

The record solves the constraints on Sigma_tau0 outward in r (N1STAR-PROOF.md Lemmas 6.3-6.4, Proposition 6.5), using
three facts computed on its Vaidya slice (data5.py S2-S4, S6): the constraint map (J, rho) = (2(-div K + d tr K), R -
|K|^2 + (tr K)^2) of the corrected data Psi(U) = (gamma + a dr dr, K + w Pi + q (dr dth + dth dr)) is forward parabolic
in a and symmetric hyperbolic in (w, q) with r as time; at the approximant's data its linearisation has no 1/lam
coefficient; and its order-0 principal coefficients are the background's. For two families on the two-dust slice
(FAMILIES5.md 4i, data5two.py) the open points were the slice (not Vaidya), and the outgoing phase: data5two's code
fixes d_tau(d_tau u) = 0 on Sigma, so the dynamic outgoing null phase was outside it. Here, in the class's slice
coordinates (R areal, th, phi1, phi2), exactly (sympy):

  S1 (exact, symbolic) on every round slice, gamma = G(R) dR^2 + R^2 dOmega_3^2 and K = k1(R) dR^2 + k2(R) R^2 dOmega_3^2
     with G, k1, k2 arbitrary: the linearisation of rho in a has no d_R^2 a and no d_R d_th a, the coefficient of d_R a
     is 3/(R G^2) = theta^3 H (theta^2 = gamma^RR = 1/G, H = 3/(R sqrt(G)) the spheres' mean curvature) and that of
     d_th^2 a is -1/(G R^2), independent of K; (J_R, J_th) in (w, q) has principal part J_R = 6 d_R w - (2/R^2) d_th q,
     J_th = -(2/G) d_R q + 4 d_th w; with S = diag(1, -1/(2 R^2)), S A0 = diag(6, 1/(G R^2)) > 0 and S A^th symmetric;
     the speeds are real, c^2 = 2 G^-1... printed. At G = 1 + mu/R^2 these are the record's (5.6). So Lemma 6.3(a)
     holds on every round slice with G > 0, the two-dust slice among them.
     Control: with the correction h = a gamma (conformal) in place of a dR dR, d_R^2 a appears in rho (data5's
     mutant conformal_h): the parabolic structure belongs to Racz's parametrisation, not to the slice.
  S2 (exact at random points) at the approximant's slice data with both families -- the ingoing wave W_TT(s1) with its
     second harmonic chi_in dPv dPv and the outgoing one W'_TT(s2) with chi_out dPu dPu, s1 = Pv/lam, s2 = Pu/lam --
     on a general round spacetime background (lapse N, radial metric G and shift b, all functions of (t, R)), with the
     two phases Pv(t, R), Pu(t, R) arbitrary (null or not; static or dynamic: d_t^2 Pu arbitrary), the linearisation of
     (J_R, J_th, rho) in (a, w, q) has no coefficient of order 1/lam. Three random draws of every function (polynomials
     with rational coefficients), each at a random point and random phases of (s1, s2, th).
     Control: the outgoing wave given an oscillating trace on the spheres produces a 1/lam coefficient (nonzero at the
     same points).
  S3 (exact at random points) there, the order-0 coefficients of the principal terms (d_R a, d_th^2 a, d_R d_th a, d_R^2
     a in rho; d_R w, d_th q in J_R; d_R q, d_th w in J_th) equal the background's: no O(1) oscillation reaches them.
     Control: with the oscillating trace they differ.
  S4 (exact) the constraint map involves only (gamma, K), which involve g and its first t-derivatives: d_t^2 Pu cannot
     enter. Checked: the slice data built by this program are unchanged when Pu is replaced by Pu + c (t - t0)^2 (c a
     symbol). So the dynamic outgoing null phase is covered by S2-S3; its eikonal equation is never used.

With S1-S4, Lemmas 6.3-6.4 and Proposition 6.5 apply on the two-dust slice with both families (FAMILIES5-FULL.md
section 6). Labels: computed (exact, sympy).

Run: python3 checks/twoslice5.py   (a few minutes)
"""
import random
import sys

import sympy as sp

t, R, th = sp.symbols('t R theta')
c1, d1, c2, d2, Ct, St = sp.symbols('c1 d1 c2 d2 Ct St')
eps, IL, eU = sp.symbols('eps il eU')
ZERO = sp.Integer(0)


def Ds(e, c, d):
    return -d * sp.diff(e, c) + c * sp.diff(e, d)


class Fast:
    """derivatives along the slice and in t, with the phases' fast parts: D_R -> d_R + il Pv_R D_s1 + il Pu_R D_s2"""

    def __init__(self, Pv, Pu):
        self.Pv, self.Pu = Pv, Pu

    def D(self, e, k):
        if k == 0:
            return (sp.diff(e, R) + IL * sp.diff(self.Pv, R) * Ds(e, c1, d1)
                    + IL * sp.diff(self.Pu, R) * Ds(e, c2, d2))
        if k == 1:
            return sp.diff(e, th) - St * sp.diff(e, Ct) + Ct * sp.diff(e, St)
        return ZERO

    def Dt(self, e):
        return (sp.diff(e, t) + IL * sp.diff(self.Pv, t) * Ds(e, c1, d1)
                + IL * sp.diff(self.Pu, t) * Ds(e, c2, d2))


def trunc(e, top_eps=1, top_eU=1):
    """drop eps^k, k > top_eps, and eU^k, k > top_eU (il is kept; il eps = 1 is applied at the end)"""
    e = sp.expand(e)
    p = sp.Poly(e, eps, eU)
    out = ZERO
    for (ke, ku), cf in p.terms():
        if ke <= top_eps and ku <= top_eU:
            out += cf * eps**ke * eU**ku
    return out


def inv_diag(x, top=2):
    """1/x for x = x0 + (eps, eU)-terms, truncated: 1/x0 - y/x0^2 + y^2/x0^3"""
    x = sp.expand(x)
    x0 = x.subs({eps: 0, eU: 0})
    y = sp.expand(x - x0)
    return trunc(1 / x0 - y / x0**2 + (y**2 / x0**3 if top >= 2 else 0), 2, 1)


def christoffel(F, g, gi):
    n = 4
    dg = [[[F.D(g[a][b], k) for k in range(n)] for b in range(n)] for a in range(n)]
    G = [[[ZERO] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                e = sum(gi[a][d] * (dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(n) if gi[a][d] != 0) / 2
                G[a][b][c] = G[a][c][b] = trunc(e, 2, 1)
    return G


def constraints(F, g, gi, K):
    n = 4
    G = christoffel(F, g, gi)
    Rs = ZERO
    for b in range(n):
        for c in range(n):
            if gi[b][c] == 0:
                continue
            e = ZERO
            for a in range(n):
                e += F.D(G[a][b][c], a) - F.D(G[a][b][a], c)
                for d in range(n):
                    e += G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
            Rs += gi[b][c] * e
    trK = sum(gi[i][j] * K[i][j] for i in range(n) for j in range(n) if gi[i][j] != 0)
    K2 = sum(gi[i][k] * gi[j][l] * K[i][j] * K[k][l] for i in range(n) for j in range(n) for k in range(n)
             for l in range(n) if gi[i][k] != 0 and gi[j][l] != 0)
    rho = Rs - K2 + trK**2
    J = []
    for i in range(2):
        divK = ZERO
        for j in range(n):
            for k in range(n):
                if gi[j][k] == 0:
                    continue
                cov = F.D(K[i][j], k) - sum(G[l][k][i] * K[l][j] + G[l][k][j] * K[i][l] for l in range(n))
                divK += gi[j][k] * cov
        J.append(2 * (-divK + F.D(trK, i)))
    return J[0], J[1], rho


# ---------------------------------------------------------------- S1: every round slice, symbolic
def s1(control=False):
    Gf = sp.Function('G')(R)
    k1, k2 = sp.Function('k1')(R), sp.Function('k2')(R)
    a, w, q = sp.Function('a')(R, th), sp.Function('w')(R, th), sp.Function('q')(R, th)
    F = Fast(ZERO, ZERO)
    sph = [R**2, R**2 * Ct**2, R**2 * St**2]
    cf_ = (1 + eU * a) if control else 1                 # control: h = a gamma (conformal) in place of a dR dR
    g = [[Gf * cf_ + (0 if control else eU * a), 0, 0, 0], [0, sph[0] * cf_, 0, 0], [0, 0, sph[1] * cf_, 0],
         [0, 0, 0, sph[2] * cf_]]
    gi = [[ZERO] * 4 for _ in range(4)]
    for i in range(4):
        gi[i][i] = inv_diag(g[i][i], 1)
    K = [[k1 + 0 * eU, eU * q, 0, 0], [eU * q, (k2 + eU * w) * R**2, 0, 0], [0, 0, (k2 + eU * w) * sph[1], 0],
         [0, 0, 0, (k2 + eU * w) * sph[2]]]
    JR, Jth, rho = constraints(F, g, gi, K)
    lin = [sp.expand(sp.diff(e, eU).subs(eU, 0)) for e in (JR, Jth, rho)]

    def cf(e, d):
        return sp.simplify(sp.expand(e).coeff(d)) if e.has(d) else ZERO

    aR, ath2, aRth, aRR = sp.diff(a, R), sp.diff(a, th, 2), sp.diff(a, R, th), sp.diff(a, R, 2)
    rho_l = lin[2].subs(Ct**2, 1 - St**2)
    out = {}
    out['no d_R^2 a'] = cf(rho_l, aRR) == 0
    out['no d_R d_th a'] = sp.simplify(cf(rho_l, aRth)) == 0
    if control:
        return out
    out['d_R a'] = sp.simplify(cf(rho_l, aR) - 3 / (R * Gf**2)) == 0
    out['d_th^2 a'] = sp.simplify(cf(rho_l, ath2) + 1 / (Gf * R**2)) == 0
    JR_l, Jth_l = (sp.expand(x.subs(Ct**2, 1 - St**2)) for x in lin[:2])
    A0 = sp.Matrix([[cf(JR_l, sp.diff(w, R)), cf(JR_l, sp.diff(q, R))], [cf(Jth_l, sp.diff(w, R)),
                                                                         cf(Jth_l, sp.diff(q, R))]])
    Ath = sp.Matrix([[cf(JR_l, sp.diff(w, th)), cf(JR_l, sp.diff(q, th))], [cf(Jth_l, sp.diff(w, th)),
                                                                           cf(Jth_l, sp.diff(q, th))]])
    out['J principal'] = (sp.simplify(A0 - sp.Matrix([[6, 0], [0, -2 / Gf]])) == sp.zeros(2, 2)
                          and sp.simplify(Ath - sp.Matrix([[0, -2 / R**2], [4, 0]])) == sp.zeros(2, 2))
    S = sp.diag(1, -1 / (2 * R**2))
    out['symmetrizer'] = (sp.simplify(S * A0 - sp.diag(6, 1 / (Gf * R**2))) == sp.zeros(2, 2)
                          and sp.simplify((S * Ath) - (S * Ath).T) == sp.zeros(2, 2))
    lam_ = sp.Symbol('c')
    speeds = sp.solve(sp.det(Ath - lam_ * A0), lam_)
    out['speeds real'] = all(sp.simplify(s_**2).is_positive is not False for s_ in speeds)
    mu = sp.Symbol('mu', positive=True)
    rec = sp.simplify((3 / (R * Gf**2)).subs(Gf, 1 + mu / R**2) - 3 * R**3 / (R**2 + mu)**2) == 0
    out["record's (5.6) at G = 1 + mu/R^2"] = rec
    out['_speeds'] = [sp.simplify(s_**2) for s_ in speeds]
    return out


# ---------------------------------------------------------------- S2-S4: the approximant's data, as exact jets
# Every field is a polynomial in (T, X, Y) = (t - t0, R - R0, th - th0), truncated at total degree 2, with coefficients
# polynomial in the fast variables (c_k, d_k) = (cos s_k, sin s_k), eps = lam, il = 1/lam and eU (the linearisation
# parameter). The constraint map takes at most two derivatives along any path, so its value at the point is exact.
TJ, XJ, YJ = sp.symbols('T X Y')
GENS = (TJ, XJ, YJ, c1, d1, c2, d2, eps, IL, eU)
QQ = sp.QQ


def P(e):
    return sp.Poly(sp.expand(e), *GENS, domain=QQ)


def tr(p):
    d = {m: c for m, c in p.as_dict().items() if m[0] + m[1] + m[2] <= 2 and m[7] <= 2 and m[9] <= 1}
    return sp.Poly.from_dict(d, *GENS, domain=QQ) if d else sp.Poly(0, *GENS, domain=QQ)


def mul(a, b):
    return tr(a * b)


def inv(x):
    """1/x, x a jet with a nonzero constant term"""
    d = x.as_dict()
    c = d.get((0,) * 10, 0)
    assert c != 0
    y = tr(x * QQ(1, 1) * sp.Rational(1) / c - P(1)) if False else tr(sp.Poly.from_dict(
        {m: v / c for m, v in d.items()}, *GENS, domain=QQ) - P(1))
    s, pw = P(1), P(1)
    for _ in range(6):
        pw = mul(pw, -y)
        s = s + pw
    return tr(sp.Poly.from_dict({m: v / c for m, v in s.as_dict().items()}, *GENS, domain=QQ))


def Dsk(p, c, d):
    return -P(d) * p.diff(c) + P(c) * p.diff(d)


class JetFast:
    def __init__(self, Pv, Pu):
        self.vR, self.uR = P(sp.diff(Pv, XJ)), P(sp.diff(Pu, XJ))
        self.vT, self.uT = P(sp.diff(Pv, TJ)), P(sp.diff(Pu, TJ))

    def D(self, p, k):
        if k == 0:
            return tr(p.diff(XJ) + P(IL) * (mul(self.vR, Dsk(p, c1, d1)) + mul(self.uR, Dsk(p, c2, d2))))
        if k == 1:
            return tr(p.diff(YJ))
        return P(0)

    def Dt(self, p):
        return tr(p.diff(TJ) + P(IL) * (mul(self.vT, Dsk(p, c1, d1)) + mul(self.uT, Dsk(p, c2, d2))))


def jconstraints(F, g, gi, K):
    """(J_R, J_th, rho) for diagonal gamma (g, gi lists of jets) and symmetric K"""
    n = 4
    dg = [[F.D(g[a][a], k) for k in range(n)] for a in range(n)]

    def dgf(a, b, k):
        return dg[a][k] if a == b else P(0)
    G = [[[P(0)] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                e = dgf(a, c, b) + dgf(a, b, c) - dgf(b, c, a)
                G[a][b][c] = G[a][c][b] = mul(gi[a][a], e) * QQ(1, 2)
    Rs = P(0)
    for b in range(n):
        e = P(0)
        for a in range(n):
            e = e + F.D(G[a][b][b], a) - F.D(G[a][b][a], b)
            for d in range(n):
                e = e + mul(G[a][a][d], G[d][b][b]) - mul(G[a][b][d], G[d][b][a])
        Rs = Rs + mul(gi[b][b], e)
    trK = P(0)
    for i in range(n):
        trK = trK + mul(gi[i][i], K[i][i])
    K2 = P(0)
    for i in range(n):
        for j in range(n):
            K2 = K2 + mul(mul(gi[i][i], gi[j][j]), mul(K[i][j], K[i][j]))
    rho = tr(Rs - K2 + mul(trK, trK))
    J = []
    for i in range(2):
        divK = P(0)
        for j in range(n):
            cov = F.D(K[i][j], j) - sum((mul(G[l][j][i], K[l][j]) + mul(G[l][j][j], K[i][l]) for l in range(n)), P(0))
            divK = divK + mul(gi[j][j], cov)
        J.append(tr((F.D(trK, i) - divK) * 2))
    return J[0], J[1], rho


def rp(rng, vars_, deg, const=None, scale=1):
    mons = [sp.Integer(1)]
    for _ in range(deg):
        mons = list({m * v for m in mons for v in [sp.Integer(1)] + list(vars_)})
    e = sum(sp.Rational(rng.randint(-4, 4), 7) * m for m in mons) * scale
    if const is not None:
        e = sp.expand(e) - sp.expand(e).subs({v: 0 for v in vars_}) + const
    return sp.expand(e)


def circle(rng):
    k = sp.Rational(rng.randint(1, 9), rng.randint(2, 11))
    return (1 - k**2) / (1 + k**2), 2 * k / (1 + k**2)


def jslice(seed, trace_out=False, waves=True, pu_extra=0):
    """the approximant's slice data at the point (as jets): gamma (diagonal), K, the operator, and R0"""
    rng = random.Random(seed)
    R0 = sp.Rational(rng.randint(15, 30), 10)
    ct, st = circle(rng)
    Rj = R0 + XJ
    Cj = ct - st * YJ - ct * YJ**2 / 2
    Sj = st + ct * YJ - st * YJ**2 / 2
    N = rp(rng, [TJ, XJ], 2, const=1)
    Gb = rp(rng, [TJ, XJ], 2, const=sp.Rational(3, 2))
    b = rp(rng, [TJ, XJ], 2, scale=sp.Rational(1, 3))
    Pv = TJ + XJ + rp(rng, [TJ, XJ], 3, scale=sp.Rational(1, 5))
    Pu = TJ - XJ + rp(rng, [TJ, XJ], 3, scale=sp.Rational(1, 5)) + pu_extra
    F = JetFast(Pv, Pu)
    amp = lambda: rp(rng, [TJ, XJ, YJ], 1)                                      # noqa: E731
    a1, a2 = amp() * c1 + amp() * d1, amp() * c1 + amp() * d1
    b1, b2 = amp() * c2 + amp() * d2, amp() * c2 + amp() * d2
    chi_in, chi_out = amp() * (c1**2 - d1**2), amp() * (c2**2 - d2**2)
    Ftr = amp() * c2
    w = 1 if waves else 0
    sph = [Rj**2, Rj**2 * Cj**2, Rj**2 * Sj**2]
    Wang = [-2 * Rj**2 * (a1 + a2 + b1 + b2), 2 * sph[1] * (a1 + b1), 2 * sph[2] * (a2 + b2)]
    if trace_out:
        Wang = [Wang[0] + sph[0] * Ftr, Wang[1] + sph[1] * Ftr, Wang[2] + sph[2] * Ftr]
    vT, vR, uT, uR = sp.diff(Pv, TJ), sp.diff(Pv, XJ), sp.diff(Pu, TJ), sp.diff(Pu, XJ)
    W_tR = chi_in * vT * vR + chi_out * uT * uR
    W_RR = chi_in * vR**2 + chi_out * uR**2
    gam = [tr(P(Gb + w * eps * W_RR))] + [tr(P(sph[i] + w * eps * Wang[i])) for i in range(3)]
    gi = [inv(x) for x in gam]
    beta = tr(P(Gb * b + w * eps * W_tR))
    two_n_inv = inv(tr(P(2 * N)))
    dg = [[F.D(gam[a], k) for k in range(4)] for a in range(4)]

    def Gam(a, b_, c):                                   # Christoffel symbols of the diagonal gamma
        e = (dg[a][b_] if a == c else P(0)) + (dg[a][c] if a == b_ else P(0)) - (dg[b_][a] if b_ == c else P(0))
        return mul(gi[a], e) * QQ(1, 2)
    K = [[P(0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            dtg = F.Dt(gam[i]) if i == j else P(0)
            lie = (F.D(beta, i) if j == 0 else P(0)) + (F.D(beta, j) if i == 0 else P(0)) - mul(Gam(0, i, j), beta) * 2
            K[i][j] = K[j][i] = mul(two_n_inv, dtg - lie)
    # the slice is t = t0: drop T
    sl = lambda p: tr(sp.Poly.from_dict({m: v for m, v in p.as_dict().items() if m[0] == 0} or {(0,) * 10: 0},  # noqa
                                         *GENS, domain=QQ))
    return F, [sl(x) for x in gam], [[sl(x) for x in row] for row in K], rng


def jlinear(seed, a_, w_, q_, trace_out=False, waves=True, pt=None):
    """the 1/lam and order-0 parts, at the point, of the linearisation of (J_R, J_th, rho) in (a, w, q)"""
    F, gam, K, rng = jslice(seed, trace_out, waves)
    g = [tr(gam[0] + P(eU * a_))] + gam[1:]
    gi = [inv(x) for x in g]
    Kp = [row[:] for row in K]
    for i in (1, 2, 3):
        Kp[i][i] = tr(Kp[i][i] + mul(P(eU * w_), gam[i]))
    Kp[0][1] = tr(Kp[0][1] + P(eU * q_))
    Kp[1][0] = Kp[0][1]
    out = []
    for e in jconstraints(F, g, gi, Kp):
        e1, e0 = sp.Integer(0), sp.Integer(0)
        for m, v in e.as_dict().items():
            if m[0] or m[1] or m[2] or m[9] != 1:
                continue
            net = m[7] - m[8]                                                   # power of lam
            mono = v * c1**m[3] * d1**m[4] * c2**m[5] * d2**m[6]
            if net == -1:
                e1 += mono
            elif net == 0:
                e0 += mono
        red = lambda x: sp.reduced(sp.expand(x), [d1**2 + c1**2 - 1, d2**2 + c2**2 - 1], d1, d2, c1, c2)[1]  # noqa
        out.append((sp.expand(red(e1)), sp.expand(red(e0))))
    return out


def s2_s3(seeds=(11, 12, 13)):
    res = {'S2': True, 'S2c': True, 'S3': True, 'S3c': True}
    for sd in seeds:
        rng = random.Random(sd + 500)
        gen = [rp(rng, [XJ, YJ], 2) for _ in range(3)]
        lin = jlinear(sd, *gen)
        linc = jlinear(sd, *gen, trace_out=True)
        z = [x[0] == 0 for x in lin]
        zc = [x[0] == 0 for x in linc]
        print('    draw %d: the 1/lam coefficient of (J_R, J_th, rho) vanishes: %s; with the outgoing trace: %s'
              % (sd, z, zc), flush=True)
        res['S2'] &= all(z)
        res['S2c'] &= not all(zc)
        tests = {'d_R a (rho)': ((XJ, 0, 0), 2), 'd_th^2 a (rho)': ((YJ**2 / 2, 0, 0), 2),
                 'd_R d_th a (rho)': ((XJ * YJ, 0, 0), 2), 'd_R^2 a (rho)': ((XJ**2 / 2, 0, 0), 2),
                 'd_R w (J_R)': ((0, XJ, 0), 0), 'd_th q (J_R)': ((0, 0, YJ), 0), 'd_R q (J_th)': ((0, 0, XJ), 1),
                 'd_th w (J_th)': ((0, YJ, 0), 1)}
        same, samec, bad = True, True, []
        for name, (aw, k) in tests.items():
            full = jlinear(sd, *aw)[k][1]
            bg = jlinear(sd, *aw, waves=False)[k][1]
            ctl = jlinear(sd, *aw, trace_out=True)[k][1]
            if sp.expand(full - bg) != 0:
                same = False
                bad.append(name)
            samec &= sp.expand(ctl - bg) == 0
        print('    draw %d: order-0 principal coefficients equal the background\'s: %s %s; with the trace: %s'
              % (sd, same, bad, samec), flush=True)
        res['S3'] &= same
        res['S3c'] &= not samec
    return res


def s4():
    """d_t^2 of the outgoing phase does not reach the slice data"""
    c = sp.Rational(5, 3)
    _, g1, K1, _ = jslice(21)
    _, g2, K2, _ = jslice(21, pu_extra=c * TJ**2)
    same = all((g1[i] - g2[i]).is_zero for i in range(4)) and all((K1[i][j] - K2[i][j]).is_zero for i in range(4)
                                                                    for j in range(4))
    _, g3, K3, _ = jslice(21, pu_extra=c * TJ * XJ)                       # control: d_t d_R Pu does reach K
    ctl = not all((K1[i][j] - K3[i][j]).is_zero for i in range(4) for j in range(4))
    return same, ctl


def main():
    ok = {}
    o = s1()
    sp_ = o.pop('_speeds')
    print('  S1 (every round slice):', {k: v for k, v in o.items()}, '; speeds^2 =', sp_, flush=True)
    oc = s1(control=True)
    ctl1 = not oc['no d_R^2 a']
    print('  S1 control (h = a gamma): no d_R^2 a in rho -> %s (must be False)' % oc['no d_R^2 a'], flush=True)
    ok['S1'] = all(o.values()) and ctl1
    r = s2_s3()
    ok['S2'] = r['S2'] and r['S2c']
    ok['S3'] = r['S3'] and r['S3c']
    same, ctl4 = s4()
    print('  S4: slice data unchanged under Pu -> Pu + c (t - t0)^2: %s; control (Pu -> Pu + c (t - t0)(R - R0) '
          'changes K) %s' % (same, ctl4), flush=True)
    ok['S4'] = same and ctl4
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
