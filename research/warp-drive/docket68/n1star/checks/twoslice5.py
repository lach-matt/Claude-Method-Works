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
     second harmonic chi_in cos(2 s1) dPv dPv and the outgoing one W'_TT(s2) with chi_out cos(2 s2) dPu dPu, s1 =
     Pv/lam, s2 = Pu/lam -- on a general round spacetime background (lapse N, radial metric G and shift b, functions of
     (t, R)), the two phases Pv(t, R), Pu(t, R) arbitrary (null or not; static or dynamic: d_t^2 Pu arbitrary), the
     linearisation of (J_R, J_th, rho) in a generic direction (a, w, q) has no coefficient of order 1/lam, in any
     harmonic e^(i(n1 s1 + n2 s2)). Every function is a random polynomial with rational coefficients (three draws, each
     at a random point and angle); the fields are carried as exact jets (Gaussian-rational coefficients, total degree 2
     in (t - t0, R - R0, th - th0), every harmonic, lam-order <= 2), which is exact at the point since the constraint
     map takes at most two derivatives along any path.
     Control: the outgoing wave given an oscillating trace on the spheres produces a 1/lam coefficient.
  S3 (exact at random points) there, the order-0 coefficients of the principal terms (d_R a, d_th^2 a, d_R d_th a, d_R^2
     a in rho; d_R w, d_th q in J_R; d_R q, d_th w in J_th) equal the background's in every harmonic: no O(1)
     oscillation reaches them. Control: with the oscillating trace some differ.
  S4 (exact) the constraint map involves only (gamma, K), that is g and its first t-derivatives, so d_t^2 Pu cannot
     enter: the slice data built here are unchanged when Pu -> Pu + c (t - t0)^2. Control: Pu -> Pu + c (t - t0)(R - R0)
     changes K. So the dynamic outgoing null phase is covered by S2-S3; its eikonal equation is never used.

With S1-S4, Lemmas 6.3-6.4 and Proposition 6.5 apply on the two-dust slice with both families (FAMILIES5-FULL.md
section 6). Labels: computed (exact, sympy).

Run: python3 checks/twoslice5.py   (about twenty minutes)
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
# A field is a dict {(dT, dX, dY, n1, n2, o, lab): c}: the monomial T^dT X^dX Y^dY e^(i n1 s1) e^(i n2 s2) lam^o,
# (T, X, Y) = (t - t0, R - R0, th - th0), c a Gaussian rational (re, im). lab = 0 for the data, k >= 1 for the part
# linear in the k-th correction direction (two labelled factors are dropped: the linearisation). Truncation: total
# degree in (T, X, Y) <= 2 and lam-order o <= 2. The constraint map takes at most two derivatives along any path and
# no factor has lam-order below -1, so its value at the point, at orders lam^-1 and lam^0, is exact.
from fractions import Fraction as Fr                                            # noqa: E402

TJ, XJ, YJ = sp.symbols('T X Y')
CAPD, CAPO = 2, 2


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def jadd(*ps, scale=None):
    out = {}
    for k, p in enumerate(ps):
        s = scale[k] if scale else (Fr(1), Fr(0))
        for m, c in p.items():
            c = cmul(c, s) if scale else c
            o = out.get(m)
            out[m] = c if o is None else (o[0] + c[0], o[1] + c[1])
    return {m: c for m, c in out.items() if c[0] or c[1]}


def jsub(a, b):
    return jadd(a, b, scale=[(Fr(1), Fr(0)), (Fr(-1), Fr(0))])


def jscale(a, s):
    s = (Fr(s), Fr(0)) if not isinstance(s, tuple) else s
    return {m: cmul(c, s) for m, c in a.items()}


def jmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            d = ma[0] + mb[0] + ma[1] + mb[1] + ma[2] + mb[2]
            o = ma[5] + mb[5]
            if d > CAPD or o > CAPO or (ma[6] and mb[6]):
                continue
            m = (ma[0] + mb[0], ma[1] + mb[1], ma[2] + mb[2], ma[3] + mb[3], ma[4] + mb[4], o, ma[6] or mb[6])
            c = cmul(ca, cb)
            x = out.get(m)
            out[m] = c if x is None else (x[0] + c[0], x[1] + c[1])
    return {m: c for m, c in out.items() if c[0] or c[1]}


def jconst(c, o=0, lab=0):
    return {(0, 0, 0, 0, 0, o, lab): (Fr(c), Fr(0))} if c else {}


def jpoly(e, n1=0, n2=0, o=0, lab=0, coef=(1, 0)):
    """a sympy polynomial in (T, X, Y) times e^(i (n1 s1 + n2 s2)) lam^o"""
    out = {}
    for mon, c in sp.Poly(sp.expand(e), TJ, XJ, YJ).as_dict().items():
        if sum(mon) <= CAPD and o <= CAPO:
            c = Fr(int(sp.numer(c)), int(sp.denom(c)))
            out[(mon[0], mon[1], mon[2], n1, n2, o, lab)] = cmul((c, Fr(0)), (Fr(coef[0]), Fr(coef[1])))
    return out


def jcos(e, k, n, o=0):
    """e cos(n s_k) lam^o"""
    a = [0, 0]
    a[k] = n
    b = [0, 0]
    b[k] = -n
    return jadd(jpoly(e, a[0], a[1], o, coef=(Fr(1, 2), 0)), jpoly(e, b[0], b[1], o, coef=(Fr(1, 2), 0)))


def jsin(e, k, n, o=0):
    a = [0, 0]
    a[k] = n
    b = [0, 0]
    b[k] = -n
    return jadd(jpoly(e, a[0], a[1], o, coef=(0, Fr(-1, 2))), jpoly(e, b[0], b[1], o, coef=(0, Fr(1, 2))))


def jdiff(a, var):
    """d/dT (var 0), d/dX (1), d/dY (2)"""
    out = {}
    for m, c in a.items():
        if m[var]:
            mm = list(m)
            mm[var] -= 1
            out[tuple(mm)] = (c[0] * m[var], c[1] * m[var])
    return out


def jfast(a, k):
    """d/ds_k: multiply mode n_k by i n_k"""
    return {m: (-c[1] * m[3 + k], c[0] * m[3 + k]) for m, c in a.items() if m[3 + k]}


def jil(a):
    """multiply by 1/lam"""
    return {m[:5] + (m[5] - 1, m[6]): c for m, c in a.items()}


def jinv(x):
    c = x.get((0, 0, 0, 0, 0, 0, 0))
    assert c and c[1] == 0 and c[0] != 0
    ci = Fr(1) / c[0]
    y = jsub(jscale(x, ci), jconst(1))
    s, pw = jconst(1), jconst(1)
    for _ in range(CAPD + CAPO + 2):
        pw = jscale(jmul(pw, y), -1)
        s = jadd(s, pw)
    return jscale(s, ci)


class JF:
    def __init__(self, vT, vR, uT, uR):
        self.vT, self.vR, self.uT, self.uR = vT, vR, uT, uR

    def D(self, p, k):
        if k == 0:
            return jadd(jdiff(p, 1), jil(jadd(jmul(self.vR, jfast(p, 0)), jmul(self.uR, jfast(p, 1)))))
        if k == 1:
            return jdiff(p, 2)
        return {}

    def Dt(self, p):
        return jadd(jdiff(p, 0), jil(jadd(jmul(self.vT, jfast(p, 0)), jmul(self.uT, jfast(p, 1)))))


def jconstraints(F, g, gi, K):
    """(J_R, J_th, rho) for diagonal gamma (g, gi: lists of the diagonal jets) and symmetric K"""
    n = 4
    dg = [[F.D(g[a], k) for k in range(n)] for a in range(n)]
    G = [[[{}] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                e = jadd(dg[a][b] if a == c else {}, dg[a][c] if a == b else {})
                if b == c:
                    e = jsub(e, dg[b][a])
                G[a][b][c] = G[a][c][b] = jscale(jmul(gi[a], e), Fr(1, 2))
    Rs = {}
    for b in range(n):
        e = {}
        for a in range(n):
            e = jadd(e, F.D(G[a][b][b], a), jscale(F.D(G[a][b][a], b), -1))
            for d in range(n):
                e = jadd(e, jmul(G[a][a][d], G[d][b][b]), jscale(jmul(G[a][b][d], G[d][b][a]), -1))
        Rs = jadd(Rs, jmul(gi[b], e))
    trK = {}
    for i in range(n):
        trK = jadd(trK, jmul(gi[i], K[i][i]))
    K2 = {}
    for i in range(n):
        for j in range(n):
            if K[i][j]:
                K2 = jadd(K2, jmul(jmul(gi[i], gi[j]), jmul(K[i][j], K[i][j])))
    rho = jadd(Rs, jscale(K2, -1), jmul(trK, trK))
    J = []
    for i in range(2):
        divK = {}
        for j in range(n):
            cov = F.D(K[i][j], j)
            for l in range(n):
                cov = jsub(cov, jadd(jmul(G[l][j][i], K[l][j]), jmul(G[l][j][j], K[i][l])))
            divK = jadd(divK, jmul(gi[j], cov))
        J.append(jscale(jsub(F.D(trK, i), divK), 2))
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
    k = sp.Integer(1)
    while k == 1:                                     # off the axes: cos and sin both nonzero
        k = sp.Rational(rng.randint(1, 9), rng.randint(2, 11))
    return (1 - k**2) / (1 + k**2), 2 * k / (1 + k**2)


TESTS = [('generic', None, None), ('d_R a (rho)', 0, XJ), ('d_th^2 a (rho)', 0, YJ**2 / 2),
         ('d_R d_th a (rho)', 0, XJ * YJ), ('d_R^2 a (rho)', 0, XJ**2 / 2), ('d_R w (J_R)', 1, XJ),
         ('d_th w (J_th)', 1, YJ), ('d_R q (J_th)', 2, XJ), ('d_th q (J_R)', 2, YJ)]


def jrun(seed, trace_out=False, waves=True, pu_extra=0, slice_only=False):
    """the approximant's slice data and the linearisation of (J_R, J_th, rho) in the labelled directions"""
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
    vT, vR, uT, uR = (sp.diff(Pv, TJ), sp.diff(Pv, XJ), sp.diff(Pu, TJ), sp.diff(Pu, XJ))
    F = JF(jpoly(vT), jpoly(vR), jpoly(uT), jpoly(uR))
    amp = lambda: rp(rng, [TJ, XJ, YJ], 1)                                      # noqa: E731
    A = [amp() for _ in range(8)]
    chi_in, chi_out, Ftr = amp(), amp(), amp()
    w = 1 if waves else 0
    o = 1                                                                       # the waves carry one power of lam

    def osc(c_, s_, k):
        return jadd(jcos(c_, k, 1, o), jsin(s_, k, 1, o))
    a1, a2, b1, b2 = osc(A[0], A[1], 0), osc(A[2], A[3], 0), osc(A[4], A[5], 1), osc(A[6], A[7], 1)
    sph = [sp.expand(Rj**2), sp.expand(Rj**2 * Cj**2), sp.expand(Rj**2 * Sj**2)]
    Wang = [jmul(jpoly(-2 * sph[0]), jadd(a1, a2, b1, b2)), jmul(jpoly(2 * sph[1]), jadd(a1, b1)),
            jmul(jpoly(2 * sph[2]), jadd(a2, b2))]
    if trace_out:
        tr_ = jcos(Ftr, 1, 1, o)
        Wang = [jadd(Wang[i], jmul(jpoly(sph[i]), tr_)) for i in range(3)]
    ci, co = jcos(chi_in, 0, 2, o), jcos(chi_out, 1, 2, o)
    W_RR = jadd(jmul(ci, jpoly(vR**2)), jmul(co, jpoly(uR**2)))
    W_tR = jadd(jmul(ci, jpoly(vT * vR)), jmul(co, jpoly(uT * uR)))
    if not w:
        Wang, W_RR, W_tR = [{}, {}, {}], {}, {}
    gam = [jadd(jpoly(Gb), W_RR)] + [jadd(jpoly(sph[i]), Wang[i]) for i in range(3)]
    gi = [jinv(x) for x in gam]
    beta = jadd(jpoly(Gb * b), W_tR)
    tni = jinv(jpoly(2 * N))
    dg = [[F.D(gam[a], k) for k in range(4)] for a in range(4)]

    def Gam(a, b_, c):
        e = jadd(dg[a][b_] if a == c else {}, dg[a][c] if a == b_ else {})
        if b_ == c:
            e = jsub(e, dg[b_][a])
        return jscale(jmul(gi[a], e), Fr(1, 2))
    K = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            dtg = F.Dt(gam[i]) if i == j else {}
            lie = jadd(F.D(beta, i) if j == 0 else {}, F.D(beta, j) if i == 0 else {},
                       jscale(jmul(Gam(0, i, j), beta), -2))
            K[i][j] = K[j][i] = jmul(tni, jsub(dtg, lie))
    sl = lambda p: {m: c for m, c in p.items() if m[0] == 0}                    # noqa: E731
    gam = [sl(x) for x in gam]
    K = [[sl(x) for x in row] for row in K]
    if slice_only:
        return gam, K
    # the labelled correction directions: lab 1 generic, lab 2.. the principal-coefficient probes
    rng2 = random.Random(seed + 500)
    gen = [rp(rng2, [XJ, YJ], 2) for _ in range(3)]
    U = [jpoly(gen[k], lab=1) for k in range(3)]
    for lab, (name, comp, mono) in enumerate(TESTS[1:], start=2):
        U[comp] = jadd(U[comp], jpoly(mono, lab=lab))
    g = [jadd(gam[0], U[0])] + gam[1:]
    gi = [jinv(x) for x in g]
    Kp = [row[:] for row in K]
    for i in (1, 2, 3):
        Kp[i][i] = jadd(Kp[i][i], jmul(U[1], gam[i]))
    Kp[0][1] = jadd(Kp[0][1], U[2])
    Kp[1][0] = Kp[0][1]
    res = []
    for e in jconstraints(F, g, gi, Kp):
        part = {}
        for m, c in e.items():
            if m[0] or m[1] or m[2] or not m[6] or m[5] > 0:
                continue
            part.setdefault((m[6], m[5]), {})[(m[3], m[4])] = c
        res.append(part)
    return res


def s2_s3(seeds=(11, 12, 13)):
    res = {'S2': True, 'S2c': True, 'S3': True, 'S3c': True}
    comp_of = {'rho': 2, 'J_R': 0, 'J_th': 1}
    for sd in seeds:
        full, bg, ctl = jrun(sd), jrun(sd, waves=False), jrun(sd, trace_out=True)
        z = [not any(c[0] or c[1] for c in full[k].get((1, -1), {}).values()) for k in range(3)]
        zc = [not any(c[0] or c[1] for c in ctl[k].get((1, -1), {}).values()) for k in range(3)]
        print('    draw %d: the 1/lam coefficient of (J_R, J_th, rho) in a generic direction vanishes: %s; with the '
              'outgoing trace: %s' % (sd, z, zc), flush=True)
        res['S2'] &= all(z)
        res['S2c'] &= not all(zc)
        same, samec, bad = True, True, []
        for lab, (name, comp, mono) in enumerate(TESTS[1:], start=2):
            k = comp_of[name.split('(')[1].rstrip(')')]
            f0, b0, c0 = (r[k].get((lab, 0), {}) for r in (full, bg, ctl))
            eq = lambda x, y: all(x.get(m, (0, 0)) == y.get(m, (0, 0)) for m in set(x) | set(y))  # noqa: E731
            if not eq(f0, b0):
                same = False
                bad.append(name)
            samec &= eq(c0, b0)
        print('    draw %d: the order-0 principal coefficients (%s) equal the background\'s, every harmonic: %s %s; '
              'with the outgoing trace: %s' % (sd, ', '.join(n for n, _, _ in TESTS[1:]), same, bad, samec),
              flush=True)
        res['S3'] &= same
        res['S3c'] &= not samec
    return res


def s4():
    """d_t^2 of the outgoing phase does not reach the slice data; d_t d_R of it does (control)"""
    c = sp.Rational(5, 3)
    g1, K1 = jrun(21, slice_only=True)
    g2, K2 = jrun(21, slice_only=True, pu_extra=c * TJ**2)
    g3, K3 = jrun(21, slice_only=True, pu_extra=c * TJ * XJ)
    same = all(g1[i] == g2[i] for i in range(4)) and all(K1[i][j] == K2[i][j] for i in range(4) for j in range(4))
    ctl = not all(K1[i][j] == K3[i][j] for i in range(4) for j in range(4))
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
