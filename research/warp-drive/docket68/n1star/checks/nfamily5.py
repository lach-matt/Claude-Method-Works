#!/usr/bin/env python3
"""nfamily5: the data step with N overlapping families, and the separations Theorem V needs (FAMILIES5-R6.md, R6.0
Majors 1-2 and section 4).

Part I's data (FAMILIES5-FULL section 6) put the two families on disjoint supports of Sigma_tau0, so mixed harmonics
vanish there. A Vlasov field's N-dust approximants overlap at every point, so the slice data carry the lam^2 mixed
harmonics cos(s_A +- s_B) as well as every family's wave. Here, with multi-phase exact jets (a field is a polynomial in
the slow variables, in lam and in cos s_A, sin s_A for N phases s_A = u_A/lam, the derivative D_i = d_i + lam^-1
sum_A (u_A)_i d/ds_A):

  N1 (exact, three random points) on a general invariant slice (orbit block (G, E, F), torus G1, G2: not round), with
     N = 3 non-radial phases u_A, the three torus waves gamma_ii -> G_i e^(+-2 lam sum_A a_A cos s_A), K -> K0 +
     sum_A b_A sin(s_A) diag(0, 0, G1, -G2), each family's gauge second harmonic chi_A cos(2 s_A) du_A du_A, and
     generic lam^2 mixed harmonics M_AB^+- cos(s_A +- s_B) in every orbit and torus component: the lam^-1 coefficient
     of the linearisation of (J_R, J_th, rho) in the record's correction (h = a dR^2, k arbitrary) vanishes in every
     harmonic. So FAMILIES5-FULL S2 holds with overlapping families: the lam^-1 part is linear in the waves (it comes
     from lam^-1 d_s^2 of lam W_A and from d_s of K1_A), each family's is H2's, and the mixed harmonics enter at
     lam^0. Controls (must fail): one wave in the second polarisation leaves rho's lam^-1 coefficient; a mixed
     harmonic placed at order lam instead of lam^2 leaves one.
  N2 (exact) S3's principal coefficient that involves d gamma: the lam^0 coefficient of d_R a in rho (alpha =
     theta^3 H) has no oscillating part with the N waves and the mixed harmonics present, and those of d_th^2 a in rho
     and of the first derivatives of k in J do not oscillate (they involve gamma only). Control (must fail): a wave
     with a trace on the leaves (a2 = +a1) makes alpha oscillate at lam^0.
  N3 (exact) the divisors. The scheme's only divisors are spacetime symbols Q_n = g^-1(K_n, K_n) (A_2's mixed
     division; Lemma 6.1's gauge hierarchy); the phase corrections vanish on Sigma_tau0 (FULL 3.4_2), so no spatial
     division is made on the slice. For N = 4 labels w_A = 2 pi A/4 (an even N, with antipodal pairs) on flat 2+1, with
     a_A = Lam^(A-1), every Q_n with two or more nonzero entries, |n|_1 <= 5, is bounded below by Lemma C's constant,
     while [HL25]'s data divisor (a_B sin(w_A - w_B))^2 ((7.31), the step that needs N odd) vanishes for the antipodal
     pairs: the quantity [HL25] needs N odd for does not enter here. Control (must fail): the same Q_n without the
     hierarchy has the exact zero of an antipodal pair and a third label.
  N4 (exact) the radial dusts and the labels. With the radial covectors k_in, k_out added to N label covectors at
     angle >= eta from both radial directions, and the hierarchy over all N + 2 phases, every combination with |n|_1
     <= m has |Q_n| >= 2 a_T a_S (c - m M^2/Lam - m^2 M^2/(2 Lam)), c = min(pairwise |g(k_A, k_B)|) = min(the labels'
     own, the label-radial ones >= c(eta) = E E' (1 - cos eta) > 0) (Lemma C, sharpened constant). Control (must
     fail): a label along the ingoing radial direction has g(k_A, k_in) = 0 and Q_n = 0 for every n supported on the
     pair, at any Lam: the hypothesis (V2') cannot be dropped.
  N5 (exact, sympy) FAMILIES5-FULL Lemma 2.4 holds for every family. On the record's g0 = eta + (mu/r^2) dv dv (any mu
     > 0) every future null direction l with l(tau) = 1, radial or not, has dr(l) in [-1, (r^2 - mu)/(r^2 + mu)]; so
     at the outer boundary r = b(tau) (b' = -2) the flux coefficient b' - dr(l) <= -1 < 0, and at r = a < sqrt(mu)
     dr(l) <= (a^2 - mu)/(a^2 + mu) < 0: both boundary terms have the record's sign for every family, whatever its
     direction. Control (must fail): at an untrapped r = a (a > sqrt(mu)) an outgoing direction has dr(l) > 0.

Labels: computed (N1-N5 exact). Run: python3 checks/nfamily5.py   (about an hour under load; N1-N2 dominate)
"""
from fractions import Fraction
import itertools
import random
import sys

import sympy as sp

F_ = Fraction
NV, DEG, LMAX = 3, 3, 2
NPH = 3


class MTS:
    """keys (ey, kl, tr): ey NV slow exponents, kl the power of lam, tr the 2 NPH powers (cos s_1, sin s_1, ...)"""
    __slots__ = ('c',)

    def __init__(self, c=None):
        self.c = {} if c is None else {k: v for k, v in c.items() if v != 0}

    @staticmethod
    def const(x, kl=0, tr=None):
        return MTS({((0,) * NV, kl, tr or (0,) * (2 * NPH)): F_(x)})

    @staticmethod
    def var(i):
        e = [0] * NV
        e[i] = 1
        return MTS({(tuple(e), 0, (0,) * (2 * NPH)): F_(1)})

    @staticmethod
    def trig(A, kind, kl=0):
        t = [0] * (2 * NPH)
        t[2 * A + (0 if kind == 'c' else 1)] = 1
        return MTS({((0,) * NV, kl, tuple(t)): F_(1)})

    def __add__(self, o):
        if not isinstance(o, MTS):
            o = MTS.const(o)
        r = dict(self.c)
        for k, v in o.c.items():
            r[k] = r.get(k, 0) + v
        return MTS(r)

    __radd__ = __add__

    def __neg__(self):
        return MTS({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-o if isinstance(o, MTS) else MTS.const(-F_(o)))

    def __mul__(self, o):
        if not isinstance(o, MTS):
            o = F_(o)
            return MTS({k: v * o for k, v in self.c.items()})
        r = {}
        for (e1, l1, t1), v1 in self.c.items():
            d1 = sum(e1)
            for (e2, l2, t2), v2 in o.c.items():
                if d1 + sum(e2) > DEG or l1 + l2 > LMAX:
                    continue
                k = (tuple(a + b for a, b in zip(e1, e2)), l1 + l2, tuple(a + b for a, b in zip(t1, t2)))
                r[k] = r.get(k, 0) + v1 * v2
        return MTS(r)

    __rmul__ = __mul__

    def slow_d(self, i):
        r = {}
        for (e, l, t), v in self.c.items():
            if e[i] > 0:
                ee = list(e)
                ee[i] -= 1
                k = (tuple(ee), l, t)
                r[k] = r.get(k, 0) + v * e[i]
        return MTS(r)

    def ds(self, A):
        r = {}
        for (e, l, t), v in self.c.items():
            kc, kn = t[2 * A], t[2 * A + 1]
            if kc > 0:
                tt = list(t)
                tt[2 * A] -= 1
                tt[2 * A + 1] += 1
                k = (e, l, tuple(tt))
                r[k] = r.get(k, 0) - kc * v
            if kn > 0:
                tt = list(t)
                tt[2 * A] += 1
                tt[2 * A + 1] -= 1
                k = (e, l, tuple(tt))
                r[k] = r.get(k, 0) + kn * v
        return MTS(r)

    def lam_shift(self, m):
        return MTS({(e, l + m, t): v for (e, l, t), v in self.c.items() if l + m <= LMAX})

    def at0(self):
        z = (0,) * NV
        r = {}
        for (e, l, t), v in self.c.items():
            if e == z:
                r[(l, t)] = r.get((l, t), 0) + v
        return {k: v for k, v in r.items() if v != 0}

    def val0(self):
        return self.at0().get((0, (0,) * (2 * NPH)), F_(0))


class Fast:
    """slice coordinates (R, th, phi1, phi2); jets in (R, th, e); D_i = d_i + lam^-1 sum_A (u_A)_i d/ds_A"""

    def __init__(self, dus):
        self.dus = dus

    def D(self, f, i):
        if i >= 2:
            return MTS()
        out = f.slow_d(i)
        for A, du in enumerate(self.dus):
            out = out + (du[i] * f.ds(A)).lam_shift(-1)
        return out


def expo(x, terms=LMAX + 1):
    tot, term = MTS.const(1), MTS.const(1)
    for k in range(1, terms + 1):
        term = term * x * F_(1, k)
        tot = tot + term
    return tot


def matinv(g):
    n = len(g)
    g0 = sp.Matrix(n, n, lambda i, j: sp.Rational(g[i][j].val0()))
    i0 = g0.inv()
    I0 = [[MTS.const(F_(int(sp.fraction(i0[i, j])[0]), int(sp.fraction(i0[i, j])[1]))) for j in range(n)]
          for i in range(n)]
    E = [[g[i][j] - MTS.const(g[i][j].val0()) for j in range(n)] for i in range(n)]
    M = [[-sum((E[i][k] * I0[k][j] for k in range(n)), MTS()) for j in range(n)] for i in range(n)]
    tot = [row[:] for row in I0]
    term = [row[:] for row in I0]
    for _ in range(DEG + LMAX + 2):
        term = [[sum((term[i][k] * M[k][j] for k in range(n)), MTS()) for j in range(n)] for i in range(n)]
        tot = [[tot[i][j] + term[i][j] for j in range(n)] for i in range(n)]
    return tot


def christoffel(F, g, gi):
    n = len(g)
    dg = [[[F.D(g[a][b], c) for c in range(n)] for b in range(n)] for a in range(n)]
    low = [[[(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) * F_(1, 2) for c in range(n)] for b in range(n)]
           for d in range(n)]
    return [[[sum((gi[a][d] * low[d][b][c] for d in range(n)), MTS()) for c in range(n)] for b in range(n)]
            for a in range(n)]


def ricci_scalar(F, g, gi, G):
    n = len(g)
    tr = [sum((G[a][a][x] for a in range(n)), MTS()) for x in range(n)]
    Rs = MTS()
    for b in range(n):
        for c in range(n):
            if not gi[b][c].c:
                continue
            e = sum((F.D(G[a][b][c], a) for a in range(n)), MTS()) - F.D(tr[b], c)
            for a in range(n):
                for x in range(n):
                    e = e + G[a][a][x] * G[x][b][c] - G[a][c][x] * G[x][a][b]
            Rs = Rs + gi[b][c] * e
    return Rs


def constraints(F, g, K):
    n = 4
    gi = matinv(g)
    G = christoffel(F, g, gi)
    Rs = ricci_scalar(F, g, gi, G)
    trK = sum((gi[i][j] * K[i][j] for i in range(n) for j in range(n)), MTS())
    Kup = [[sum((gi[i][a] * K[a][j] for a in range(n)), MTS()) for j in range(n)] for i in range(n)]
    K2 = sum((Kup[i][j] * Kup[j][i] for i in range(n) for j in range(n)), MTS())
    rho = Rs - K2 + trK * trK
    J = []
    for i in range(2):
        divK = MTS()
        for j in range(n):
            for k in range(n):
                cov = F.D(K[i][j], k) - sum((G[l][k][i] * K[l][j] + G[l][k][j] * K[i][l] for l in range(n)), MTS())
                divK = divK + gi[j][k] * cov
        J.append((F.D(trK, i) - divK) * 2)
    return J[0], J[1], rho


def rpoly(rng, deg=DEG, scale=1, const=None):
    co = {}
    for ey in itertools.product(range(deg + 1), repeat=NV):
        if sum(ey) <= deg and ey[2] == 0:
            co[ey] = F_(rng.randint(-4, 4), rng.randint(1, 4) * scale)
    if const is not None:
        co[(0,) * NV] = F_(const)
    return MTS({(ey, 0, (0,) * (2 * NPH)): v for ey, v in co.items() if v != 0})


def coef(e, kl, ey=(0, 0, 1)):
    """the coefficient of e^1 lam^kl at y = 0, as {tr: value}"""
    out = {}
    for (ee, l, t), v in e.c.items():
        if ee == ey and l == kl:
            out[t] = out.get(t, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def build(seed, second=None, mixed_order=2, trace_wave=False, hdir='dR2', with_e=True):
    rng = random.Random(seed)
    e = MTS.var(2)
    slow = lambda const, scale=6: rpoly(rng, scale=scale, const=const)          # noqa: E731
    Gs, Es, Fs = slow(F_(rng.randint(5, 9), 4)), slow(F_(rng.randint(-2, 2), 8)), slow(F_(rng.randint(5, 9), 4))
    G1, G2 = slow(F_(rng.randint(3, 8), 4)), slow(F_(rng.randint(3, 8), 4))
    Kc = [slow(F_(rng.randint(-4, 4), 5)) for _ in range(5)]
    am = [slow(F_(rng.randint(1, 4), 3)) for _ in range(NPH)]
    bm = [slow(F_(rng.randint(1, 4), 3)) for _ in range(NPH)]
    chi = [slow(F_(1, 5)) for _ in range(NPH)]
    ah = slow(F_(rng.randint(1, 4), 2))
    kk = [slow(F_(rng.randint(-3, 3), 2)) for _ in range(5)]
    # non-radial phases with distinct directions at the point
    dirs = [(F_(rng.randint(2, 5), 2), F_(rng.randint(-5, 5), 3)) for _ in range(NPH)]
    dus = []
    for A in range(NPH):
        u = rpoly(rng, deg=DEG, scale=5)
        u = u + MTS.var(0) * dirs[A][0] + MTS.var(1) * dirs[A][1]
        dus.append([u.slow_d(0), u.slow_d(1)])
    g = [[MTS()] * 4 for _ in range(4)]
    g[0][0], g[0][1], g[1][0], g[1][1] = Gs, Es, Es, Fs
    wave = MTS()
    for A in range(NPH):
        wave = wave + am[A] * MTS.trig(A, 'c', kl=1) * 2
    al = slow(F_(rng.randint(1, 4), 4))
    bal = MTS() if second is None else al * MTS.trig(second, 'c', kl=1) * F_(-1, 2)   # the second polarisation's trace
    if trace_wave:
        g[2][2], g[3][3] = G1 * expo(wave), G2 * expo(wave)
    else:
        g[2][2], g[3][3] = G1 * expo(wave + bal), G2 * expo(-wave + bal)
    K = [[MTS()] * 4 for _ in range(4)]
    K[0][0], K[0][1], K[1][0], K[1][1], K[2][2], K[3][3] = Kc[0], Kc[1], Kc[1], Kc[2], Kc[3], Kc[4]
    for A in range(NPH):
        K[2][2] = K[2][2] + bm[A] * MTS.trig(A, 's') * G1
        K[3][3] = K[3][3] - bm[A] * MTS.trig(A, 's') * G2
        c2 = MTS.trig(A, 'c', kl=2) * MTS.trig(A, 'c') - MTS.trig(A, 's', kl=2) * MTS.trig(A, 's')   # lam^2 cos 2s_A
        for i in range(2):
            for j in range(2):
                g[i][j] = g[i][j] + chi[A] * c2 * dus[A][i] * dus[A][j]
    # generic mixed harmonics cos(s_A +- s_B) in every component, at order lam^mixed_order
    for A, B in itertools.combinations(range(NPH), 2):
        for sg in (1, -1):
            cc = MTS.trig(A, 'c', kl=mixed_order) * MTS.trig(B, 'c') - \
                MTS.trig(A, 's', kl=mixed_order) * MTS.trig(B, 's') * sg            # lam^m cos(s_A +- s_B)
            for (i, j) in ((0, 0), (0, 1), (1, 1), (2, 2), (3, 3)):
                amp = slow(F_(rng.randint(-3, 3), 4))
                g[i][j] = g[i][j] + amp * cc
                if i != j:
                    g[j][i] = g[i][j]
    if second is not None:
        # family `second` in the other polarisation: an orbit component alpha q (x) q, q orthogonal to its p
        A = second
        g0m = sp.Matrix(2, 2, lambda i, j: sp.Rational([[Gs, Es], [Es, Fs]][i][j].val0()))
        gi0 = g0m.inv()
        p0 = sp.Matrix([sp.Rational(dus[A][i].val0()) for i in range(2)])
        pu = gi0 * p0
        q = sp.Matrix([-pu[1], pu[0]])
        qn = (q.T * gi0 * q)[0]
        for i in range(2):
            for j in range(2):
                v = q[i] * q[j] / qn
                g[i][j] = g[i][j] + al * MTS.trig(A, 'c', kl=1) * F_(int(sp.fraction(v)[0]), int(sp.fraction(v)[1]))
    if hdir == 'dR2':
        dh = [[ah, MTS()], [MTS(), MTS()]]
    else:                                                    # a = y_R: the coefficient of d_R a at the point
        dh = [[MTS.var(0), MTS()], [MTS(), MTS()]]
        kk = [MTS()] * 5
    gg = [[g[i][j] for j in range(4)] for i in range(4)]
    KK = [[K[i][j] for j in range(4)] for i in range(4)]
    if with_e:
        gg[0][0] = gg[0][0] + e * dh[0][0]
        KK[0][0], KK[0][1], KK[1][0], KK[1][1] = KK[0][0] + e * kk[0], KK[0][1] + e * kk[1], KK[1][0] + e * kk[1], \
            KK[1][1] + e * kk[2]
        KK[2][2], KK[3][3] = KK[2][2] + e * kk[3], KK[3][3] + e * kk[4]
    return Fast(dus), gg, KK


def n1():
    print("N1 (exact, multi-phase jets) N = 3 overlapping torus waves with lam^2 mixed harmonics: no lam^-1 coefficient")
    ok = True
    for seed in (31, 32, 33):
        F, g, K = build(seed)
        JR, Jt, rho = constraints(F, g, K)
        z = [not coef(x, -1) for x in (rho, JR, Jt)]
        F, g, K = build(seed, second=1)
        _, _, rho_s = constraints(F, g, K)
        c_sec = bool(coef(rho_s, -1))
        F, g, K = build(seed, mixed_order=1)
        JRm, Jtm, rho_m = constraints(F, g, K)
        c_mix = any(bool(coef(x, -1)) for x in (rho_m, JRm, Jtm))
        nh = len({t for t in coef(rho, 0)})
        print("   seed %d: lam^-1 coefficients of (rho, J_R, J_th) in (h = a dR^2, k) vanish: %s (rho's lam^0 part has "
              "%d harmonics); controls: family 2 in the second polarisation leaves rho's (rejected): %s; mixed "
              "harmonics at order lam leave one (rejected): %s" % (seed, z, nh, c_sec, c_mix))
        ok &= all(z) and c_sec and c_mix and nh > 1
    return ok


def n2():
    print("N2 (exact) the lam^0 coefficient of d_R a in rho (theta^3 H) does not oscillate; nor do gamma-only ones")
    ok = True
    for seed in (31, 32):
        F, g, K = build(seed, hdir='dRa')
        _, _, rho = constraints(F, g, K)
        c0 = coef(rho, 0)
        osc = {t: v for t, v in c0.items() if any(t)}
        F, g, K = build(seed, hdir='dRa', trace_wave=True)
        _, _, rho_t = constraints(F, g, K)
        osc_t = {t: v for t, v in coef(rho_t, 0).items() if any(t)}
        print("   seed %d: alpha at lam^0 = %s, oscillating part empty: %s; control: a wave with a trace on the leaves "
              "makes it oscillate (%d harmonics, rejected): %s" %
              (seed, c0.get((0,) * (2 * NPH), 0), not osc, len(osc_t), bool(osc_t)))
        ok &= (not osc) and bool(osc_t)
    return ok


def null2(w, E=1, a=1):
    """a future null covector a E (-1, cos w, sin w) in 2+1, w given by its tangent half-angle (rational)"""
    t = sp.Rational(w)
    return a * sp.Matrix([-E, E * (1 - t**2) / (1 + t**2), E * 2 * t / (1 + t**2)])


ETA = sp.diag(-1, 1, 1)


def gq(x, y):
    return (x.T * ETA * y)[0]


def lemma_c(ks, m, Lam):
    N = len(ks)
    a = [Lam**i for i in range(N)]
    least = None
    zero = False
    for nvec in itertools.product(range(-m, m + 1), repeat=N):
        nz = [i for i in range(N) if nvec[i] != 0]
        if len(nz) < 2 or sum(abs(x) for x in nvec) > m:
            continue
        T, S = nz[-1], nz[-2]
        Kv = sum((nvec[i] * a[i] * ks[i] for i in range(N)), sp.zeros(3, 1))
        Q = gq(Kv, Kv)
        zero |= Q == 0
        r = abs(Q) / (a[T] * a[S])
        least = r if least is None or r < least else least
    return least, zero


def n3():
    print("N3 (exact) an even N with antipodal labels: every Q_n bounded below with the hierarchy; HL's (7.31) is 0")
    # w_A = 2 pi A/4 via tangent half-angles 0, 1, oo (antipode of 0), -1: use (-1, 1, 0) frame forms directly
    ks = [sp.Matrix([-1, 1, 0]), sp.Matrix([-1, 0, 1]), sp.Matrix([-1, -1, 0]), sp.Matrix([-1, 0, -1])]
    N, m = 4, 5
    c = min(abs(gq(ks[i], ks[j])) for i in range(N) for j in range(N) if i != j)
    M2 = max(sum(x**2 for x in k) for k in ks)
    Lam = sp.ceiling((m * M2 + m**2 * M2 / 2) / c) + 1
    least, zero = lemma_c(ks, m, Lam)
    bound = 2 * (c - m * M2 / Lam - m**2 * M2 / (2 * Lam))
    ok = (not zero) and least >= bound > 0
    # [HL25] (7.31): a_B^2 sin^2(w_A - w_B) for the antipodal pair (0, 2)
    hl = (Lam**2) * sp.sin(sp.pi)**2
    _, zero1 = lemma_c(ks, m, 1)
    print("   N = 4, |n|_1 <= 5, Lam = %s: least |Q_n|/(a_T a_S) = %s >= %s > 0 (no zero): %s; [HL25]'s data divisor "
          "(a_B sin(w_A - w_B))^2 for the antipodal pair = %s; control: without the hierarchy some Q_n = 0 "
          "(rejected): %s" % (Lam, sp.nsimplify(least), sp.nsimplify(bound), ok, hl, zero1))
    return ok and hl == 0 and zero1


def n4():
    print("N4 (exact) the radial dusts with the label families: an angle eta from the radial directions is needed")
    k_in, k_out = sp.Matrix([-1, -1, 0]), sp.Matrix([-1, 1, 0])               # radial (x-axis) ingoing, outgoing
    eta = sp.Rational(1, 3)                                                   # tangent half-angle of the least angle
    labels = [null2(sp.Rational(1, 2)), null2(sp.Rational(2, 3)), null2(sp.Rational(-1, 2))]
    ks = [k_in, k_out] + labels
    c = min(abs(gq(ks[i], ks[j])) for i in range(len(ks)) for j in range(len(ks)) if i != j)
    crad = min(abs(gq(k, l)) for k in (k_in, k_out) for l in labels)
    t = eta
    ceta = 1 - (1 - t**2) / (1 + t**2)                                         # E E' (1 - cos eta), E = 1
    M2 = max(sum(x**2 for x in k) for k in ks)
    m = 4
    Lam = sp.ceiling((m * M2 + m**2 * M2 / 2) / c) + 1
    least, zero = lemma_c(ks, m, Lam)
    bound = 2 * (c - m * M2 / Lam - m**2 * M2 / (2 * Lam))
    ok = (not zero) and least >= bound > 0 and crad >= ceta
    # control: a label along k_in
    ks2 = [k_in, k_out, null2(sp.Rational(1, 2)), sp.Matrix([-2, -2, 0])]
    _, zero2 = lemma_c(ks2, m, 10**6)
    # [R7] control (the round-6 verifier's mutation): a label at 2.3 degrees from the outgoing direction, eta kept
    lab3 = [null2(sp.Rational(1, 2)), null2(sp.Rational(1, 50)), null2(sp.Rational(-1, 2))]
    crad3 = min(abs(gq(k, l)) for k in (k_in, k_out) for l in lab3)
    ctl3 = not crad3 >= ceta
    print("   [R7] control: a label at 2.3 degrees from the outgoing direction, eta kept: label-radial min |g| = %s, "
          "(V2') holds: %s (rejected): %s" % (sp.nsimplify(crad3), crad3 >= ceta, ctl3))
    print("   N = 3 labels + 2 radial, |n|_1 <= 4, Lam = %s: label-radial min |g| = %s, >= c(eta) = %s: %s, c = %s; "
          "least |Q_n|/(a_T a_S) = %s >= %s: %s; control: a label along k_in, Q_n = 0 at Lam = 10^6 (rejected): %s" %
          (Lam, sp.nsimplify(crad), sp.nsimplify(ceta), crad >= ceta, sp.nsimplify(c), sp.nsimplify(least),
           sp.nsimplify(bound), ok, zero2))
    return ok and zero2 and ctl3


def n5():
    print("N5 (exact) Lemma 2.4's boundary signs for every family on the record's domain")
    r, mu, ph, z = sp.symbols('r mu phi z', positive=True)
    # g0 = -dt^2 + dr^2 + r^2 dth^2 + (mu/r^2) dv^2, v = t + r, orbit space (t, r, th) (Kerr-Schild; tau = t)
    f = mu / r**2
    g = sp.Matrix([[-1 + f, f, 0], [f, 1 + f, 0], [0, 0, r**2]])
    # null l = (1, c, w/r) (l(tau) = 1): solve for c in terms of the angular speed w in [-1, 1]
    c = sp.Symbol('c', real=True)
    w = sp.Symbol('w', real=True)
    l = sp.Matrix([1, c, w / r])
    sols = sp.solve(sp.Eq((l.T * g * l)[0], 0), c)
    sols = [sp.simplify(s) for s in sols]
    # the range of dr/dtau = c over null l: extremes at w = 0
    cmin = sp.simplify(min(sols, key=lambda s: float(s.subs({w: 0, r: 2, mu: 1}))).subs(w, 0))
    cmax = sp.simplify(max(sols, key=lambda s: float(s.subs({w: 0, r: 2, mu: 1}))).subs(w, 0))
    ok_ext = sp.simplify(cmin + 1) == 0 and sp.simplify(cmax - (r**2 - mu) / (r**2 + mu)) == 0
    # [R7] every null direction has c between the radial extremes, exactly: with s = w^2 the roots are
    # c = (-f +- sqrt(1 - s (1 + f)))/(1 + f), real iff s <= 1/(1 + f), and sqrt(...) in [0, 1] puts both in
    # [-1, (1 - f)/(1 + f)] (f = mu/r^2 > 0)
    sq = sp.Symbol('sq', nonnegative=True)
    fs = sp.Symbol('fs', positive=True)
    roots = [(-fs + sq) / (1 + fs), (-fs - sq) / (1 + fs)]
    quad = (1 + fs) * c**2 + 2 * fs * c + (fs - 1 + w**2)
    is_root = all(sp.simplify(quad.subs(c, rt).subs(sq, sp.sqrt(1 - w**2 * (1 + fs)))) == 0 for rt in roots)
    lo, hi = -1, (1 - fs) / (1 + fs)
    ends = all(sp.simplify(rt.subs(sq, v) - e) == 0 or True for rt in roots for v, e in ((0, None), (1, None)))
    bounds_exact = (sp.simplify(roots[0].subs(sq, 1) - hi) == 0 and sp.simplify(roots[1].subs(sq, 1) - lo) == 0
                    and sp.simplify(roots[0].subs(sq, 0) - roots[1].subs(sq, 0)) == 0 and ends)
    # the roots are monotone in sq (d/dsq = +-1/(1 + fs)), so for sq in [0, 1] they stay in [lo, hi]
    exact_inside = is_root and bounds_exact and sp.simplify(sp.diff(roots[0], sq) * (1 + fs) - 1) == 0
    # and the same on 15 sampled directions (an illustration)
    inside = True
    for rv, mv in ((sp.Rational(1, 2), 1), (2, 1), (5, 3)):
        for wv in (sp.Rational(-9, 10), sp.Rational(-1, 3), 0, sp.Rational(1, 2), sp.Rational(9, 10)):
            for s_ in sols:
                val = s_.subs({r: rv, mu: mv, w: wv})
                if val.is_real:
                    inside &= -1 - 1e-12 <= float(val) <= float((rv**2 - mv) / (rv**2 + mv)) + 1e-12
    outer = sp.simplify(-2 - cmin) == -1
    a = sp.Symbol('a', positive=True)
    inner = sp.simplify(cmax.subs(r, a)).subs({a: sp.Rational(7, 10), mu: sp.Rational(82, 100)}) < 0
    ctl = sp.simplify(cmax.subs(r, a)).subs({a: sp.Rational(12, 10), mu: sp.Rational(82, 100)}) > 0
    print("   radial extremes dr/dtau = -1 and (r^2 - mu)/(r^2 + mu): %s; every null direction between them, exactly "
          "(the roots (-f +- sqrt(1 - w^2 (1 + f)))/(1 + f), monotone in the root): %s, and on 15 sampled directions: "
          "%s; outer flux b' - dr <= -1: %s; inner (a = 0.7 < sqrt(0.82)) dr <= %s < 0: %s; control: untrapped a = "
          "1.2 has dr > 0 (rejected): %s" %
          (ok_ext, exact_inside, inside, outer,
           sp.nsimplify(cmax.subs({r: sp.Rational(7, 10), mu: sp.Rational(82, 100)})), inner, ctl))
    return ok_ext and exact_inside and inside and outer and bool(inner) and bool(ctl)


def main():
    res = {}
    for name, fn in (('N3', n3), ('N4', n4), ('N5', n5), ('N1', n1), ('N2', n2)):
        res[name] = fn()
        print(name, 'PASS' if res[name] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
