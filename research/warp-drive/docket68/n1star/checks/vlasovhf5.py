#!/usr/bin/env python3
"""vlasovhf5: the high-frequency passage to restricted massless Vlasov limits in the T^2 x Z2 x Z2 class
(FAMILIES5-VLASOV.md).

  H1 (exact, two-scale jets at three random points) the torus polarisation. g = h + G1 e^(2 lam a1 cos s) dphi1^2
     + G2 e^(2 lam a2 cos s) dphi2^2, s = u/lam, h a general Lorentzian metric on the orbit space, every function a
     random polynomial (u not null, so the identities hold for every u). With A := a1 + a2 and E_i := -Ric_ii/g_ii:
     (a) the lam^-1 part of Ric on the orbit block is A cos(s) du (x) du, and Ric(d_a, d_phi_i) = Ric_12 = 0;
     (b) the lam^-1 part of E_i is -a_i <du, du>_h cos s;
     (c) the sin(s) part of E_i at lam^0 is -[2 <da_i, du> + a_i (box_h u + <du, d sigma0>) + A <d psi_i0, du>],
         sigma0 = psi10 + psi20, psi_i0 = (1/2) log G_i.
     Deduced: for a null phase the torus polarisation a2 = -a1 (A = 0) makes the whole lam^-1 part of Ric vanish with h
     unperturbed, and summing (c), A obeys 2 ell(A) + A (box_g u + ell(sigma0)) = 0: A = 0 is transported. Control
     (must fail): the two-scale derivative with its fast part dropped in one direction misses (c).
  H2 (exact, two-scale jets at three random points) the constraints. A general invariant slice gamma = (G, E, F) block
     + G1 dphi1^2 + G2 dphi2^2 (not round), K0 general invariant, a non-radial phase u(R, th), the torus wave
     gamma_ii -> G_i e^(+-2 lam a cos s), K -> K0 + b sin(s) diag(0, 0, G1, -G2), and a lam^2 second harmonic
     chi cos(2s) du du: the lam^-1 part of the linearisation of (J_R, J_th, rho) (J = 2(-div K + d tr K), rho = R -
     |K|^2 + (tr K)^2) is, for every slow h and k,
         d rho^(-1) = -2 <h, p (x) W''p> + h(p, p) tr W'' + |p|^2 <h, W''>,
         d J_i^(-1) = 2 (h^jk p_j K1'_ki - p_i h^jk K1'_jk)          (p = du, W'' = d_s^2 W, K1' = d_s K1),
     the record's formula (FAMILIES5-FULL section 6, S2), now on a non-round slice with a non-radial phase, and for a
     wave that is neither transverse nor traceless (the formula's test bed). For the
     record's corrections (h = a dR^2, k arbitrary) both vanish for the torus wave. Controls (must fail): the second
     polarisation (an orbit component alpha q (x) q, q orthogonal to p) gives d rho^(-1) != 0 for h = a dR^2 when the
     phase is not radial; the formula with the sign of its first term flipped is rejected.
  H3 (exact, rational, three seeds) no shear in the orbit space. For a null u (to first order) on a 2+1 Lorentzian h,
     <Hess_h u, S>_h = (box_h u) tr_h S for every symmetric S with S(ell, .) = 0, ell = h^-1 du: the transport of
     Psi = box phi along a non-radial family closes (FAMILIES5-FULL Lemma 3.4_2's step, with the class's torus
     components first order by classchi5 C1). Controls (must fail): the same in 3+1 (a two-dimensional transverse
     space, with shear), and Hess with its Christoffel term dropped.
  H4 (exact, rational) coherence after hierarchical rescaling. For future null k_1..k_N in 2+1 with pairwise |g(k_A,
     k_B)| >= c and Euclidean frame norms <= M, a_A = Lam^(A-1), every n in Z^N with two or more nonzero entries and
     |n|_1 <= m has |g(K_n, K_n)| >= 2 a_T a_S (c - 2 m M^2/Lam - m^2 M^2/(2 Lam)), K_n = sum n_A a_A k_A, T > S its two
     largest indices: checked over every such n (N <= 4, m <= 5) for random rational configurations, and the bound is
     positive once Lam > (2 m M^2 + m^2 M^2/2)/c. Control (must fail): without the rescaling (Lam = 1) an antipodal
     pair and any third direction have the exactly null combination k_a + k_b - k_c (a resonance no division removes).
     [R6, the verifier of round 5: the random configurations are not resonant, so the main loop passed with a_A = 1.
     The main loop now also runs that resonant configuration (an antipodal pair of equal energies and a third
     label) with the hierarchy, where the bound must hold; with a_A = 1 it fails there (mutation H4_NOHIER).]
  H5 (numpy RK4) separation is kept by the geodesic flow, with constant c/N^2. On the orbit space of Tangherlini
     (mu = 1), h = -f dt^2 + dR^2/f + R^2 dth^2, label phases u_w with initial gradient (cos w/sqrt f, R0 sin w) on
     t = 0: at a point y at t = T, d alpha/d w (alpha the momentum's angle) equals det DPhi / det(dy/dx0) (Phi the
     flow map on (x0, w)) to 1e-6, is positive, and min |g^-1(du_A, du_B)|/(Delta w)^2 over adjacent labels
     converges as N = 8, 16, 32, 64. Control (must fail): d alpha/d w taken at fixed x0 (the Schur term dropped)
     disagrees with the shooting.
  H6 (mpmath; numpy) the background step is uniform in N. (a) The label quadrature of a smooth stress, the periodic
     trapezoid rule, errs faster than any power of 1/N (error N^6 -> 0); control (must fail): a density with a kink
     errs like N^-2. (b) A mean-field model, w_tt - w_xx = sum_A (2 pi/N) q_A, q_A transported with speed
     tanh(2 w + cos w_A) (the source's zero mode removed): the N-label solution differs from the 128-label one by an
     error that falls with N, and its ratio to the quadrature residual of the continuum solution sampled at the N
     labels (the N-system's residual) stays bounded independently of N: the stability constant of Proposition U does
     not grow with N (computed, model). Control (must fail): label weights 2 pi/(N + 1) (a mutated N-system).
     [R6, the verifier of round 5: with the coupling removed (b) still passes, so it did not test stability. Added: the
     N-system's stability constant measured directly, sup|w_N(q0 + d q1) - w_N(q0)|/d for d = 1e-3, within a factor 2
     over N = 4, 8, 16; control (must fail): a mutated N-system whose coupling grows with N (transport speed tanh(2
     (N/4) w + cos w_A)) has a stability constant growing by more than that factor. The model has none of the dust's
     derivative-loss coupling; it is a model of the quadrature step only.]
  H7 (exact, sympy) restricted particles focus at an axis. (a) In the class sqrt|g5| = sqrt|h| e^(psi1 + psi2), so
     the conserved orbit-space density of a restricted current is e^(psi1 + psi2) n5, and near axis 2 e^psi2 = sqrt(a)
     rho2 (1 + O(rho2^2)) (axisloss5 X1 (a)). (b) In the plane of axis 2 restricted momenta move radially (p_phi2 =
     0): the planar continuity equation for inward speed v is solved by n(r, t) = n0(r + v t)(r + v t)/r, so r n ->
     v t n0(v t) > 0 as r -> 0 once the beam reaches the axis: the density, and T5 ~ n v^2 with the non-smooth xhat
     (x) xhat form (vlasov5 V2's control), are unbounded. Control (must fail to blow up): axial momenta (v = 0).

Labels: computed (H1-H4, H7 exact; H5 numpy; H6 mpmath and numpy, its (b) a model). Run: python3 checks/vlasovhf5.py
(a few minutes)
"""
from fractions import Fraction
import itertools
import os
import random
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import twoscale5 as ts                                                        # noqa: E402
from twoscale5 import TS                                                     # noqa: E402

F_ = Fraction


def fr(x):
    return sp.Rational(x.numerator, x.denominator)


# ---------------------------------------------------------------- H1
def h1_point(seed, a2_opposite=False, drop=None):
    ts.NV, ts.DEG, ts.LMAX = 3, 2, 2
    rng = random.Random(seed)
    # orbit metric h: diag(-1, 1, 1) + small random polynomial
    base = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
    h = [[None] * 3 for _ in range(3)]
    for a in range(3):
        for b in range(a, 3):
            p = ts.rpoly(rng, scale=6, const=F_(base[a][b]) + F_(rng.randint(-2, 2), 10))
            h[a][b] = h[b][a] = p
    G = [ts.rpoly(rng, scale=5, const=F_(rng.randint(4, 9), 4)) for _ in range(2)]
    a = [ts.rpoly(rng, scale=3, const=F_(rng.randint(1, 5), 3)) for _ in range(2)]
    if a2_opposite:
        a[1] = -a[0]
    # the phase: a cubic with a gradient of order 1
    ts.DEG = 3
    u = ts.rpoly(rng, deg=3, scale=4)
    u = u + TS.var(0) * F_(rng.randint(2, 5), 2) + TS.var(1) * F_(rng.randint(-3, 3), 2) + TS.var(2) * F_(1, 3)
    du3 = [u.slow_d(i) for i in range(3)]
    ts.DEG = 2
    du = [TS({k: v for k, v in d.c.items() if sum(k[0]) <= 2}) for d in du3]
    C = TS.const(1, 1, 1, 0)                                                   # lam cos s
    g = [[TS()] * 5 for _ in range(5)]
    for i in range(3):
        for j in range(3):
            g[i][j] = h[i][j]
    g[3][3] = G[0] * ts.expo(a[0] * C * 2)
    g[4][4] = G[1] * ts.expo(a[1] * C * 2)
    gi = ts.matinv(g)
    Fd = ts.Fast(du + [TS(), TS()], drop=drop)
    Fd.D = (lambda f, i, _F=Fd: TS() if i >= 3 else ts.Fast.D(_F, f, i))
    R, _ = ts.ricci(Fd, g, gi)
    # point values of the slow data
    h0 = sp.Matrix(3, 3, lambda i, j: fr(h[i][j].at0().get((0, 0, 0), 0)))
    hi = h0.inv()
    dh = [[[fr(h[i][j].slow_d(c).at0().get((0, 0, 0), 0)) for c in range(3)] for j in range(3)] for i in range(3)]
    Gam = [[[sum(hi[x, d] * (dh[d][b][c] + dh[d][c][b] - dh[b][c][d]) for d in range(3)) / 2 for c in range(3)]
            for b in range(3)] for x in range(3)]
    p = [fr(du[i].at0().get((0, 0, 0), 0)) for i in range(3)]
    upp = [[fr(du[i].slow_d(j).at0().get((0, 0, 0), 0)) for j in range(3)] for i in range(3)]
    boxu = sum(hi[i, j] * (upp[i][j] - sum(Gam[c][i][j] * p[c] for c in range(3))) for i in range(3) for j in range(3))
    ip = lambda x, y: sum(hi[i, j] * x[i] * y[j] for i in range(3) for j in range(3))          # noqa: E731
    av = [fr(a[k].at0().get((0, 0, 0), 0)) for k in range(2)]
    dav = [[fr(a[k].slow_d(i).at0().get((0, 0, 0), 0)) for i in range(3)] for k in range(2)]
    Gv = [fr(G[k].at0().get((0, 0, 0), 0)) for k in range(2)]
    dpsi = [[fr(G[k].slow_d(i).at0().get((0, 0, 0), 0)) / (2 * Gv[k]) for i in range(3)] for k in range(2)]
    dsig = [dpsi[0][i] + dpsi[1][i] for i in range(3)]
    A = av[0] + av[1]
    # (a)
    oka = True
    for i in range(3):
        for j in range(3):
            v = {k: fr(x) for k, x in R[i][j].at0().items() if k[0] == -1}
            want = {(-1, 1, 0): A * p[i] * p[j]} if A * p[i] * p[j] != 0 else {}
            oka &= v == want
    okmix = all(not R[i][j].at0() for i in range(5) for j in range(5) if (i < 3) != (j < 3)) and not R[3][4].at0()
    # (b), (c)
    okb, okc = True, True
    for k in range(2):
        Ek = -(R[3 + k][3 + k] * g[3 + k][3 + k].inv())
        vals = Ek.at0()
        lm1 = {kk: fr(x) for kk, x in vals.items() if kk[0] == -1}
        wantb = -av[k] * ip(p, p)
        okb &= lm1 == ({(-1, 1, 0): wantb} if wantb != 0 else {})
        sin0 = fr(vals.get((0, 0, 1), 0))
        wantc = -(2 * ip(dav[k], p) + av[k] * (boxu + ip(p, dsig)) + A * ip(dpsi[k], p))
        okc &= sp.simplify(sin0 - wantc) == 0
    return oka, okmix, okb, okc, A


def h1():
    print("H1 (exact, two-scale jets) the torus polarisation: Ric's lam^-1 part and the amplitudes' transport")
    ok = True
    for seed in (11, 12, 13):
        oka, okmix, okb, okc, A = h1_point(seed)
        oka2, okmix2, okb2, okc2, A2 = h1_point(seed, a2_opposite=True)
        print("   seed %d: (a) lam^-1 Ric_orbit = A cos(s) du du (A = %s): %s, mixed components 0: %s; (b) %s; (c) %s;"
              " with a2 = -a1 (A = %s): (a)-(c) %s" % (seed, A, oka, okmix, okb, okc, A2,
                                                      oka2 and okmix2 and okb2 and okc2))
        ok &= oka and okmix and okb and okc and oka2 and okmix2 and okb2 and okc2 and A2 == 0
    _, _, _, okc_m, _ = h1_point(11, drop=1)
    print("   control (fast derivative dropped along y1) rejected by (c): %s" % (not okc_m))
    return ok and not okc_m


# ---------------------------------------------------------------- H2
class FastSlice(ts.Fast):
    """slice coordinates (R, th, phi1, phi2); jet variables (R, th, e); e (the linearisation parameter) is never
    differentiated"""

    def D(self, f, i):
        if i >= 2:
            return TS()
        out = f.slow_d(i)
        out = out + (self.du[i] * f.ds()).lam_shift(-1)
        return out


def constraints(Fd, g, K):
    n = 4
    gi = ts.matinv(g)
    G = ts.christoffel(Fd, g, gi)
    R, _ = ts.ricci(Fd, g, gi, G)
    Rs = sum((gi[b][c] * R[b][c] for b in range(n) for c in range(n)), TS())
    trK = sum((gi[i][j] * K[i][j] for i in range(n) for j in range(n)), TS())
    Kup = [[sum((gi[i][a] * K[a][j] for a in range(n)), TS()) for j in range(n)] for i in range(n)]   # K^i_j
    K2 = sum((Kup[i][j] * Kup[j][i] for i in range(n) for j in range(n)), TS())
    rho = Rs - K2 + trK * trK
    J = []
    for i in range(2):
        divK = TS()
        for j in range(n):
            for k in range(n):
                cov = Fd.D(K[i][j], k) - sum((G[l][k][i] * K[l][j] + G[l][k][j] * K[i][l] for l in range(n)), TS())
                divK = divK + gi[j][k] * cov
        J.append((Fd.D(trK, i) - divK) * 2)
    return J[0], J[1], rho


def lin_lm1(e):
    """the coefficient of e^1 lam^-1 at R = th = 0: {(kc, kn): Fraction}"""
    out = {}
    for (ey, l, kc, kn), v in e.c.items():
        if ey == (0, 0, 1) and l == -1:
            out[(kc, kn)] = out.get((kc, kn), 0) + v
    return {k: v for k, v in out.items() if v != 0}


def h2_point(seed, polar='torus', hdir='dR2', flip=False):
    ts.NV, ts.DEG, ts.LMAX = 3, 3, 2
    rng = random.Random(seed)
    e = TS.var(2)

    def slow(const, scale=6):
        p = ts.rpoly(rng, scale=scale, const=const)
        return TS({k: v for k, v in p.c.items() if k[0][2] == 0})            # no e-dependence
    Gs, Es, Fs = slow(F_(rng.randint(5, 9), 4)), slow(F_(rng.randint(-2, 2), 8)), slow(F_(rng.randint(5, 9), 4))
    G1, G2 = slow(F_(rng.randint(3, 8), 4)), slow(F_(rng.randint(3, 8), 4))
    Kc = [slow(F_(rng.randint(-4, 4), 5)) for _ in range(5)]
    am, bm, chi, al = slow(F_(rng.randint(1, 4), 3)), slow(F_(rng.randint(1, 4), 3)), slow(F_(1, 5)), \
        slow(F_(rng.randint(1, 4), 4))
    ah = slow(F_(rng.randint(1, 4), 2))
    kk = [slow(F_(rng.randint(-3, 3), 2)) for _ in range(5)]
    hh = [slow(F_(rng.randint(-3, 3), 2)) for _ in range(5)]
    # the phase u(R, th): non-radial
    ts.DEG = 4
    u = ts.rpoly(rng, deg=4, scale=5)
    u = TS({k: v for k, v in u.c.items() if k[0][2] == 0})
    u = u + TS.var(0) * F_(rng.randint(2, 4), 2) + TS.var(1) * F_(rng.randint(2, 4), 3)
    du = [u.slow_d(0), u.slow_d(1)]
    ts.DEG = 3
    du = [TS({k: v for k, v in d.c.items() if sum(k[0]) <= 3}) for d in du]
    C1, S1 = TS.const(1, 1, 1, 0), TS.const(1, 0, 0, 1)                        # lam cos s, sin s
    C2 = TS.const(1, 2, 2, 0) - TS.const(1, 2, 0, 2)                           # lam^2 cos 2s
    g = [[TS()] * 4 for _ in range(4)]
    g[0][0], g[0][1], g[1][0], g[1][1] = Gs, Es, Es, Fs
    g[2][2], g[3][3] = G1 * ts.expo(am * C1 * 2), G2 * ts.expo(-(am * C1 * 2))
    K = [[TS()] * 4 for _ in range(4)]
    K[0][0], K[0][1], K[1][0], K[1][1], K[2][2], K[3][3] = Kc[0], Kc[1], Kc[1], Kc[2], Kc[3], Kc[4]
    K[2][2] = K[2][2] + bm * S1 * G1
    K[3][3] = K[3][3] - bm * S1 * G2
    for i in range(2):                                                            # the gauge second harmonic
        for j in range(2):
            g[i][j] = g[i][j] + chi * C2 * du[i] * du[j]
    p0 = [fr(du[i].at0().get((0, 0, 0), 0)) for i in range(2)]
    gam0 = sp.Matrix(2, 2, lambda i, j: fr([[Gs, Es], [Es, Fs]][i][j].at0().get((0, 0, 0), 0)))
    if polar == 'second':
        # an orbit component alpha q (x) q, q the gamma0-unit covector orthogonal to p, traceless with the torus part
        gi0 = gam0.inv()
        pu = gi0 * sp.Matrix(p0)
        # q with gi0(q, p) = 0: q = (-pu[1], pu[0]) up to normalisation (q_i pu^i = 0)
        q = sp.Matrix([-pu[1], pu[0]])
        qn = (q.T * gi0 * q)[0]
        qq = [[TS.const(q[i] * q[j] / qn) for j in range(2)] for i in range(2)]
        for i in range(2):
            for j in range(2):
                g[i][j] = g[i][j] + al * C1 * qq[i][j]
        # trace balance: the torus part becomes G1 (2 a - alpha/2), G2 (-2 a - alpha/2) at order lam
        g[2][2] = G1 * ts.expo((am * 2 - al * F_(1, 2)) * C1)
        g[3][3] = G2 * ts.expo((-(am * 2) - al * F_(1, 2)) * C1)
    if polar == 'generic':
        # a wave that is neither transverse nor traceless, with a generic K oscillation: the formula's test bed
        wo = [slow(F_(rng.randint(-3, 3), 4)) for _ in range(3)]
        wt = [slow(F_(rng.randint(-3, 3), 4)) for _ in range(2)]
        ko = [slow(F_(rng.randint(-3, 3), 4)) for _ in range(5)]
        g[0][0], g[0][1], g[1][1] = g[0][0] + wo[0] * C1, g[0][1] + wo[1] * C1, g[1][1] + wo[2] * C1
        g[1][0] = g[0][1]
        g[2][2], g[3][3] = G1 * ts.expo(wt[0] * C1), G2 * ts.expo(wt[1] * C1)
        K[0][0], K[0][1], K[1][1] = K[0][0] + ko[0] * S1, K[0][1] + ko[1] * S1, K[1][1] + ko[2] * S1
        K[1][0] = K[0][1]
        K[2][2], K[3][3] = K[2][2] + ko[3] * S1, K[3][3] + ko[4] * S1
    # the linearisation direction
    if hdir == 'dR2':
        dh = [[ah, TS()], [TS(), TS()]]
        dht = [TS(), TS()]
    else:
        dh = [[hh[0], hh[1]], [hh[1], hh[2]]]
        dht = [hh[3], hh[4]]
    g2 = [[g[i][j] for j in range(4)] for i in range(4)]
    K2 = [[K[i][j] for j in range(4)] for i in range(4)]
    for i in range(2):
        for j in range(2):
            g2[i][j] = g2[i][j] + e * dh[i][j]
    g2[2][2], g2[3][3] = g2[2][2] + e * dht[0], g2[3][3] + e * dht[1]
    K2[0][0], K2[0][1], K2[1][0], K2[1][1] = K2[0][0] + e * kk[0], K2[0][1] + e * kk[1], K2[1][0] + e * kk[1], \
        K2[1][1] + e * kk[2]
    K2[2][2], K2[3][3] = K2[2][2] + e * kk[3], K2[3][3] + e * kk[4]
    Fd = FastSlice(du + [TS(), TS()])
    JR, Jt, rho = constraints(Fd, g2, K2)
    got = [lin_lm1(x) for x in (rho, JR, Jt)]
    # the predicted formula at the point
    s = sp.Symbol('s')
    gfull = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            gfull[i, j] = fr(g[i][j].at0().get((0, 0, 0), 0))
    gi = gfull.inv()
    P = sp.Matrix([p0[0], p0[1], 0, 0])

    def prof(tsr):
        """the full s-profile at the point of the lam^1 (W) or lam^0 (K1) oscillation"""
        return tsr
    Wm = sp.zeros(4)
    K1m = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            for (l, kc, kn), v in g[i][j].at0().items():
                if l == 1:
                    Wm[i, j] += fr(v) * sp.cos(s)**kc * sp.sin(s)**kn
            for (l, kc, kn), v in K[i][j].at0().items():
                if l == 0 and (kc or kn):
                    K1m[i, j] += fr(v) * sp.cos(s)**kc * sp.sin(s)**kn
    W2 = Wm.diff(s, 2)
    K1p = K1m.diff(s)
    H = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            H[i, j] = fr(dh[i][j].at0().get((0, 0, 0), 0))
    H[2, 2], H[3, 3] = fr(dht[0].at0().get((0, 0, 0), 0)), fr(dht[1].at0().get((0, 0, 0), 0))
    Hup = gi * H * gi
    ipm = lambda X, Y: sum(gi[i, a] * gi[j, b] * X[i, j] * Y[a, b] for i in range(4) for j in range(4)   # noqa
                           for a in range(4) for b in range(4))
    p2 = (P.T * gi * P)[0]
    W2p = W2 * gi * P
    sgn = -1 if flip else 1
    pred_rho = (-2 * sgn * (P.T * Hup * W2p)[0] + (P.T * Hup * P)[0] * (gi * W2).trace() + p2 * ipm(H, W2))
    pred_J = [2 * (sum(Hup[j, k] * P[j] * K1p[k, i] for j in range(4) for k in range(4))
                   - P[i] * sum(Hup[j, k] * K1p[j, k] for j in range(4) for k in range(4))) for i in range(2)]

    def as_trig(d):
        return sum(fr(v) * sp.cos(s)**kc * sp.sin(s)**kn for (kc, kn), v in d.items())
    match = [sp.simplify(sp.expand_trig(as_trig(got[0]) - pred_rho)) == 0] + \
        [sp.simplify(sp.expand_trig(as_trig(got[1 + i]) - pred_J[i])) == 0 for i in range(2)]
    zero = [not x for x in got]
    return match, zero, p0


def h2():
    print("H2 (exact, two-scale jets) the constraints on a non-round slice, non-radial phase: the lam^-1 coefficient")
    ok = True
    for seed in (21, 22, 23):
        m_gen, z_gen, p0 = h2_point(seed, hdir='general')
        m_r, z_r, _ = h2_point(seed, hdir='dR2')
        m_s, z_s, _ = h2_point(seed, polar='second', hdir='dR2')
        m_g, _, _ = h2_point(seed, polar='generic', hdir='general')
        m_f, _, _ = h2_point(seed, polar='generic', hdir='general', flip=True)
        print("   seed %d (p = %s): formula, general h, torus wave (rho, J_R, J_th): %s; a generic wave (neither "
              "transverse nor traceless): %s; torus wave, h = a dR^2: lam^-1 coefficients vanish: %s; second "
              "polarisation, h = a dR^2: formula %s, rho's lam^-1 vanishes: %s (control); flipped formula rejected: %s"
              % (seed, p0, m_gen, m_g, z_r, m_s, z_s[0], not m_f[0]))
        ok &= all(m_gen) and all(m_g) and all(z_r) and all(m_r) and all(m_s) and not z_s[0] and not m_f[0]
    return ok


# ---------------------------------------------------------------- H3
def h3_point(seed, dim=3, drop_gamma=False):
    rng = random.Random(seed)
    n = dim
    R = lambda lo=-3, hi=3, d=5: sp.Rational(rng.randint(lo, hi), rng.randint(1, d))          # noqa: E731
    while True:
        hm = sp.diag(-1, *([1] * (n - 1))) + sp.Matrix(n, n, lambda i, j: 0)
        for i in range(n):
            for j in range(i, n):
                x = R(-1, 1, 6)
                hm[i, j] += x
                if i != j:
                    hm[j, i] += x
        pp = [R() for _ in range(n)]
        hi = hm.inv()
        # make p null: adjust p0 by solving the quadratic exactly is irrational; instead adjust h^-1_00 (rational)
        rest = sum(hi[i, j] * pp[i] * pp[j] for i in range(n) for j in range(n) if (i, j) != (0, 0))
        if pp[0] == 0:
            continue
        hi[0, 0] = -rest / pp[0]**2
        import numpy as np
        evs = np.linalg.eigvalsh(np.array(hi.tolist(), dtype=float))
        if hi.det() != 0 and int(np.sum(evs < 0)) == 1 and np.min(np.abs(evs)) > 1e-3:
            break
    hm = hi.inv()
    p = sp.Matrix(pp)
    # first derivatives of h (random, symmetric), Christoffels, d(h^-1)
    dh = [[[0] * n for _ in range(n)] for _ in range(n)]
    for c in range(n):
        for i in range(n):
            for j in range(i, n):
                dh[i][j][c] = dh[j][i][c] = R()
    Gam = [[[sum(hi[x, d] * (dh[d][b][c] + dh[d][c][b] - dh[b][c][d]) for d in range(n)) / 2 for c in range(n)]
            for b in range(n)] for x in range(n)]
    dhi = [sp.Matrix(n, n, lambda a, b: -sum(hi[a, i] * dh[i][j][c] * hi[j, b] for i in range(n) for j in range(n)))
           for c in range(n)]
    # second partials of u with d_c (h^ab u_a u_b) = 0
    U = sp.Matrix(n, n, lambda i, j: sp.Symbol('u%d%d' % (min(i, j), max(i, j))))
    eqs = [2 * (U[:, c].T * hi * p)[0] + (p.T * dhi[c] * p)[0] for c in range(n)]
    syms = sorted(U.free_symbols, key=str)
    sol = sp.solve(eqs, syms[:n], dict=True)[0]
    free = {x: R() for x in syms[n:]}
    Uv = U.subs(sol).subs(free)
    Hs = sp.Matrix(n, n, lambda a, b: Uv[a, b] - (0 if drop_gamma else sum(Gam[c][a][b] * p[c] for c in range(n))))
    ell = hi * p
    boxu = (hi * Hs).trace()
    # S symmetric with S ell = 0
    Sm = sp.Matrix(n, n, lambda i, j: sp.Symbol('s%d%d' % (min(i, j), max(i, j))))
    ssy = sorted(Sm.free_symbols, key=str)
    con = list(Sm * ell)
    sol2 = sp.solve(con, ssy[:n], dict=True)[0]
    ok = True
    for _ in range(3):
        fr2 = {x: R() for x in ssy[n:]}
        Sv = Sm.subs(sol2).subs(fr2)
        lhs = (hi * Hs * hi * Sv).trace()
        rhs = boxu * (hi * Sv).trace()
        ok &= sp.simplify(lhs - rhs) == 0
    hell = sp.simplify(Hs * ell)
    return ok, hell == sp.zeros(n, 1)


def h3():
    print("H3 (exact) the orbit space has no shear: <Hess u, S> = (box u) tr S for S(ell, .) = 0")
    ok = True
    for seed in (31, 32, 33):
        o3, hl = h3_point(seed)
        o4, _ = h3_point(seed, dim=4)
        om, _ = h3_point(seed, drop_gamma=True)
        print("   seed %d: 2+1: %s (Hess u (ell, .) = 0: %s); control 3+1 rejected: %s; control Hess without "
              "Christoffels rejected: %s" % (seed, o3, hl, not o4, not om))
        ok &= o3 and hl and not o4 and not om
    return ok


# ---------------------------------------------------------------- H4
def null2(t, E):
    """a future null covector in 2+1 (orthonormal frame, metric diag(-1, 1, 1)), rational: E (-1, cos, sin)"""
    t = sp.Rational(t)
    return sp.Matrix([-E, E * (1 - t**2) / (1 + t**2), E * 2 * t / (1 + t**2)])


ETA = sp.diag(-1, 1, 1)


def gq(x, y):
    return (x.T * ETA * y)[0]


H4_NOHIER = False                                                              # mutation: a_A = 1


def h4():
    print("H4 (exact) coherence of every combination after hierarchical rescaling; the resonance without it")
    rng = random.Random(41)
    ok = True
    for trial in range(5):
        N = 3 + trial % 2
        m = 4 + trial % 2
        ts_ = sorted({sp.Rational(rng.randint(-40, 40), rng.randint(1, 9)) for _ in range(N)})[:N]
        while len(ts_) < N:
            ts_.append(sp.Rational(rng.randint(41, 80), 7))
        Es = [sp.Rational(rng.randint(2, 9), 4) for _ in range(N)]
        ks = [null2(t, E) for t, E in zip(ts_, Es)]
        if trial == 4:                       # [R6] the resonant configuration: an antipodal pair and a third label
            N, m = 3, 4
            ka = null2(sp.Rational(1, 3), 1)
            ks = [ka, sp.Matrix([-1, -ka[1], -ka[2]]), null2(sp.Rational(5, 2), 1)]
        c = min(abs(gq(ks[i], ks[j])) for i in range(N) for j in range(N) if i != j)
        M = max(sp.sqrt(sum(x**2 for x in k)) for k in ks)
        M2 = max(sum(x**2 for x in k) for k in ks)
        Lam = sp.ceiling((2 * m * M2 + m**2 * M2 / 2) / c) + 1
        a = [1] * N if H4_NOHIER else [Lam**i for i in range(N)]
        worst, cnt = None, 0
        for nvec in itertools.product(range(-m, m + 1), repeat=N):
            nz = [i for i in range(N) if nvec[i] != 0]
            if len(nz) < 2 or sum(abs(x) for x in nvec) > m:
                continue
            T, S = nz[-1], nz[-2]
            K = sum((nvec[i] * a[i] * ks[i] for i in range(N)), sp.zeros(3, 1))
            Q = gq(K, K)
            bound = 2 * a[T] * a[S] * (c - 2 * m * M2 / Lam - m**2 * M2 / (2 * Lam))
            cnt += 1
            if not abs(Q) >= bound:
                ok = False
            r = abs(Q) / (a[T] * a[S])
            worst = r if worst is None or r < worst else worst
        ok &= c > 2 * m * M2 / Lam + m**2 * M2 / (2 * Lam)
        print("   %sN = %d, m = %d: c = %s, M^2 = %s, Lam = %s; %d combinations, least |Q|/(a_T a_S) = %.4g >= "
              "2(c - ...) = %.4g: %s" % ('[R6] resonant (antipodal pair + third): ' if trial == 4 else '', N, m,
                                         sp.nsimplify(c), M2, Lam, cnt, float(worst),
                                         float(2 * (c - 2 * m * M2 / Lam - m**2 * M2 / (2 * Lam))), ok))
    # control: no rescaling, an antipodal pair and a third direction
    ka, kb, kc = null2(sp.Rational(1, 3), 1), None, null2(sp.Rational(5, 2), 1)
    kb = sp.Matrix([-1, -ka[1], -ka[2]])                                     # the antipode of ka, same energy
    K = ka + kb - kc
    res = gq(K, K)
    print("   control (Lam = 1): k_a + k_antipode - k_c has g(K, K) = %s (exact resonance), so coherence fails "
          "without the rescaling: %s" % (res, res == 0))
    return ok and res == 0


# ---------------------------------------------------------------- H5
def h5_flow(R0, th0, w, T=0.5, nst=400, Rref=2.0, mu=1.0):
    """vectorised RK4 for the null geodesics of h = -f dt^2 + dR^2/f + R^2 dth^2 (t as parameter); returns R, th,
    alpha (the momentum's angle in the orthonormal frame) and the frame energy at time T"""
    import numpy as np
    R0, th0, w = np.broadcast_arrays(np.asarray(R0, float), np.asarray(th0, float), np.asarray(w, float))
    f = lambda R: 1 - mu / R**2                                               # noqa: E731
    fp = lambda R: 2 * mu / R**3                                              # noqa: E731
    pR = np.cos(w) / np.sqrt(f(R0))
    pth = Rref * np.sin(w)
    pt = -np.sqrt(f(R0) * (f(R0) * pR**2 + pth**2 / R0**2))

    def rhs(y):
        R, th, pr = y
        fr_ = f(R)
        dR = -fr_**2 * pr / pt
        dth = -fr_ * pth / (R**2 * pt)
        dHdR = 0.5 * (pt**2 * fp(R) / fr_**2 + fp(R) * pr**2 - 2 * pth**2 / R**3)
        dpr = fr_ * dHdR / pt
        return np.array([dR, dth, dpr])
    y = np.array([R0, th0, pR])
    hstep = T / nst
    for _ in range(nst):
        k1 = rhs(y)
        k2 = rhs(y + hstep / 2 * k1)
        k3 = rhs(y + hstep / 2 * k2)
        k4 = rhs(y + hstep * k3)
        y = y + hstep / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    R, th, pr = y
    al = np.arctan2(pth / R, np.sqrt(f(R)) * pr)
    E = -pt / np.sqrt(f(R))
    return R, th, al, E


def h5_shoot(y, w, guess):
    """x0 with flow(x0, w) = y, by Newton (vectorised in w)"""
    import numpy as np
    x = np.array(guess, float).copy()
    d = 1e-6
    for _ in range(30):
        R, th, _, _ = h5_flow(x[0], x[1], w)
        F0 = np.array([R - y[0], th - y[1]])
        if np.max(np.abs(F0)) < 1e-13:
            break
        J = np.zeros((2, 2) + np.shape(w))
        for k in range(2):
            xp = x.copy()
            xp[k] = xp[k] + d
            Rp, thp, _, _ = h5_flow(xp[0], xp[1], w)
            J[0, k], J[1, k] = (Rp - R) / d, (thp - th) / d
        det = J[0, 0] * J[1, 1] - J[0, 1] * J[1, 0]
        dx0 = (J[1, 1] * F0[0] - J[0, 1] * F0[1]) / det
        dx1 = (-J[1, 0] * F0[0] + J[0, 0] * F0[1]) / det
        x = x - np.array([dx0, dx1])
    return x


def h5():
    import numpy as np
    print("H5 (numpy RK4, Newton) separation is kept by the flow: d alpha/d w = det DPhi/det(dy/dx0) > 0")
    ys = [(2.3, 0.7), (2.5, 0.8), (2.4, 0.65), (2.6, 0.75)]
    ok = True
    worst_rel, minslope, ctl_bad = 0.0, None, False
    for y in ys:
        for w0 in (-0.5, 0.0, 0.4):
            x0 = h5_shoot(y, np.array(w0), [y[0] - 0.4, y[1]])
            dw = 1e-4
            xp = h5_shoot(y, np.array(w0 + dw), x0)
            xm = h5_shoot(y, np.array(w0 - dw), x0)
            ap = h5_flow(xp[0], xp[1], w0 + dw)[2]
            am = h5_flow(xm[0], xm[1], w0 - dw)[2]
            dadw = float((ap - am) / (2 * dw))
            # the flow map's Jacobian DPhi (3x3) at (x0, w0) by central differences
            e = 1e-5
            cols = []
            for k in range(3):
                vp = [float(x0[0]), float(x0[1]), w0]
                vm = list(vp)
                vp[k] += e
                vm[k] -= e
                Fp = np.array(h5_flow(*vp)[:3])
                Fm = np.array(h5_flow(*vm)[:3])
                cols.append((Fp - Fm) / (2 * e))
            D = np.array(cols).T
            schur = np.linalg.det(D) / np.linalg.det(D[:2, :2])
            rel = abs(schur - dadw) / abs(dadw)
            worst_rel = max(worst_rel, rel)
            minslope = dadw if minslope is None else min(minslope, dadw)
            ctl_bad |= abs(D[2, 2] - dadw) / abs(dadw) > 1e-3                 # the Schur term dropped
    ok = worst_rel < 1e-6 and minslope > 0 and ctl_bad
    print("   12 (y, w) pairs: max relative |Schur - shooting| = %.2e; least d alpha/d w = %.4f > 0; control (d "
          "alpha/d w at fixed x0) differs: %s" % (worst_rel, minslope, ctl_bad))
    # the symbol over adjacent labels: |g^-1(du_A, du_B)|/(Delta w)^2 = E_A E_B (1 - cos(alpha_A - alpha_B))/dw^2
    res = []
    for N in (8, 16, 32, 64):
        ws = -0.6 + 1.2 * (np.arange(N) + 0.5) / N
        dwN = 1.2 / N
        mins = []
        for y in ys:
            xs = h5_shoot(y, ws, np.array([np.full(N, y[0] - 0.4), np.full(N, y[1])]))
            _, _, al, E = h5_flow(xs[0], xs[1], ws)
            sym = E[1:] * E[:-1] * (1 - np.cos(al[1:] - al[:-1]))
            mins.append(float(np.min(sym) / dwN**2))
        res.append((N, min(mins)))
    conv = abs(res[-1][1] - res[-2][1]) / res[-1][1] < 0.05 and all(r[1] > 0 for r in res)
    print("   least symbol/(Delta w)^2 over adjacent labels and four points: %s; converged to 5 %%: %s"
          % (", ".join("N = %d: %.4f" % r for r in res), conv))
    return ok and conv


# ---------------------------------------------------------------- H6
def h6():
    import mpmath as mp
    import numpy as np
    print("H6 (mpmath; numpy) the label quadrature, and an N-uniform mean-field model")
    mp.mp.dps = 40
    q = lambda w: mp.exp(mp.cos(w - mp.mpf('0.3'))) * (mp.mpf('1.5') + mp.sin(2 * w))        # noqa: E731
    qk = lambda w: abs(mp.sin(w)) * (2 + mp.cos(w))                                          # noqa: E731
    comp = lambda qq: (lambda w: qq(w) * mp.cos(w)**2)                                       # noqa: E731
    ex = mp.quad(comp(q), [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
    exk = mp.quad(comp(qk), [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
    errs, errk = [], []
    for N in (4, 8, 16, 32):
        wa = [2 * mp.pi * (A + mp.mpf(1) / 2) / N for A in range(N)]
        errs.append(abs(2 * mp.pi / N * sum(comp(q)(w) for w in wa) - ex))
        errk.append(abs(2 * mp.pi / N * sum(comp(qk)(w) for w in wa) - exk))
    sup = all(errs[i + 1] * (8 * 2**i)**6 < errs[i] * (4 * 2**i)**6 for i in range(3)) and errs[-1] < mp.mpf('1e-12')
    kink = not (all(errk[i + 1] * (8 * 2**i)**6 < errk[i] * (4 * 2**i)**6 for i in range(3)) and errk[-1] < 1e-12)
    print("   smooth density, T_11 error at N = 4, 8, 16, 32: %s; faster than N^-6: %s" %
          (", ".join("%.2e" % float(e) for e in errs), sup))
    print("   control (a kink, |sin w|): %s, about N^-2: rejected by the test: %s" %
          (", ".join("%.2e" % float(e) for e in errk), kink))
    # (b) the model: w_tt = w_xx + sum_A (2 pi/N) q_A, q_A,t + (c_A q_A)_x = 0, c_A = tanh(2 w + cos w_A)
    nx, T, nt = 64, 1.5, 600
    x = 2 * np.pi * np.arange(nx) / nx
    kx = np.fft.fftfreq(nx, 1.0 / nx) * 1j

    def dx(f):
        return np.real(np.fft.ifft(kx * np.fft.fft(f, axis=-1), axis=-1))

    def solve(N, weight=None, kick=0.0, grow=False):
        wa = 2 * np.pi * np.arange(N) / N
        wt = 2 * np.pi / N if weight is None else weight
        q0 = np.exp(-3 * (1 - np.cos(x)))[None, :] * (1 + 0.5 * np.cos(wa) + 0.3 * np.sin(2 * wa))[:, None]
        q0 = q0 * (1 + kick * np.sin(x)[None, :] * np.cos(wa)[:, None])
        cg = N / 4.0 if grow else 1.0
        state = [np.zeros(nx), np.zeros(nx), q0.copy()]
        dt = T / nt
        hist = []

        def rhs(st):
            w, v, qq = st
            src = wt * qq.sum(axis=0)
            c = np.tanh(2 * cg * w[None, :] + np.cos(wa)[:, None])
            wxx = np.real(np.fft.ifft(-(np.fft.fftfreq(nx, 1.0 / nx)**2) * np.fft.fft(w)))
            return [v, wxx + src - src.mean(), -dx(c * qq)]                      # the zero mode of the source removed
        for _ in range(nt):
            k1 = rhs(state)
            k2 = rhs([a + dt / 2 * b for a, b in zip(state, k1)])
            k3 = rhs([a + dt / 2 * b for a, b in zip(state, k2)])
            k4 = rhs([a + dt * b for a, b in zip(state, k3)])
            state = [a + dt / 6 * (b1 + 2 * b2 + 2 * b3 + b4) for a, b1, b2, b3, b4 in zip(state, k1, k2, k3, k4)]
            hist.append(state[2].copy())
        return state, hist, wa
    ref, href, _ = solve(128)
    rows = []
    for N in (4, 8, 16):
        st, _, wa = solve(N)
        err = float(np.max(np.abs(st[0] - ref[0])))
        step = 128 // N
        # the quadrature residual of the continuum (the 128-label solution) sampled at N labels, over the history
        qerr = max(float(np.max(np.abs((2 * np.pi / N) * h[::step].sum(axis=0) - (2 * np.pi / 128) * h.sum(axis=0))))
                   for h in href[::10])
        rows.append((N, err, qerr, err / max(qerr, 1e-300)))
    fall = rows[1][1] < rows[0][1] / 4 and rows[2][1] < rows[1][1] / 4
    ratio = max(r[3] for r in rows) < 10 * min(r[3] for r in rows) and max(r[3] for r in rows) < 10
    print("   model: %s" % "; ".join("N = %d: |w_N - w_ref| = %.2e, quadrature residual %.2e, ratio %.3f" % r
                                       for r in rows))
    print("   errors fall at least like N^-2 at each doubling: %s; ratio to the residual bounded independently of N "
          "(within a factor 10, and below 10): %s" % (fall, ratio))
    # control (must fail): a mutated N-system whose label weight is 2 pi/(N + 1): its error does not fall like N^-2
    errm = [float(np.max(np.abs(solve(N, weight=2 * np.pi / (N + 1))[0][0] - ref[0]))) for N in (4, 8, 16)]
    ctl = not (errm[1] < errm[0] / 4 and errm[2] < errm[1] / 4)
    print("   control (weights 2 pi/(N + 1)): errors %s, rejected: %s" % (", ".join("%.2e" % e for e in errm), ctl))
    # [R6] the stability constant of the N-system itself, and a mutated system whose coupling grows with N
    dk = 1e-3

    def stab(N, grow=False):
        a = solve(N, grow=grow)[0][0]
        b = solve(N, kick=dk, grow=grow)[0][0]
        return float(np.max(np.abs(b - a))) / dk
    st = [stab(N) for N in (4, 8, 16)]
    stg = [stab(N, grow=True) for N in (4, 8, 16)]
    uni = max(st) < 2 * min(st)
    ctl2 = max(stg) > 2 * min(stg)
    print("   [R6] stability constant sup|w_N(q0 + d q1) - w_N(q0)|/d at N = 4, 8, 16: %s (within a factor 2: %s); "
          "control (coupling growing with N): %s (rejected): %s" %
          (", ".join("%.4f" % v for v in st), uni, ", ".join("%.4f" % v for v in stg), ctl2))
    return sup and kink and fall and ratio and ctl and uni and ctl2


# ---------------------------------------------------------------- H7
def h7():
    print("H7 (exact) restricted particles focus at an axis")
    y0, y1, y2 = sp.symbols('y0:3')
    Y = [y0, y1, y2]
    hfun = [[sp.Function('h%d%d' % (min(a, b), max(a, b)))(*Y) for b in range(3)] for a in range(3)]
    p1, p2 = sp.Function('psi1')(*Y), sp.Function('psi2')(*Y)
    g = sp.zeros(5)
    for a in range(3):
        for b in range(3):
            g[a, b] = hfun[a][b]
    g[3, 3], g[4, 4] = sp.exp(2 * p1), sp.exp(2 * p2)
    detok = sp.simplify(g.det() - sp.Matrix(hfun).det() * sp.exp(2 * p1 + 2 * p2)) == 0
    J = [sp.Function('J%d' % a)(*Y) for a in range(3)]
    sq = sp.sqrt(-sp.Matrix(hfun).det())
    div5 = sum(sp.diff(sq * sp.exp(p1 + p2) * J[a], Y[a]) for a in range(3)) / (sq * sp.exp(p1 + p2))
    orb = sum(sp.diff(sq * sp.exp(p1 + p2) * J[a], Y[a]) for a in range(3)) / sq
    curr = sp.simplify(div5 * sp.exp(p1 + p2) - orb) == 0
    print("   (a) sqrt|g5| = sqrt|h| e^(psi1 + psi2): %s; the 5D divergence of a restricted current is e^-(psi1 + psi2)"
          " times the orbit divergence of e^(psi1 + psi2) J: %s" % (detok, curr))
    # (b) flat orbit plane of the axis: particles with p_phi = 0 move radially in the (x3, x4) plane with speed v
    r, t, v, r0 = sp.symbols('r t v r0', positive=True)
    n0 = sp.Function('n0')
    nrt = n0(r + v * t) * (r + v * t) / r                                    # the 2D continuity equation's solution
    cont = sp.simplify(sp.diff(r * nrt, t) - sp.diff(r * v * nrt, r)) == 0  # d_t (r n) = d_r (r v n): inward flow
    lim = (r * nrt).subs(r, 0)
    blow = sp.simplify(lim - v * t * n0(v * t)) == 0
    # control: axial momenta (no planar velocity) keep the density
    nax = n0(r)
    ctl = sp.limit(r * nax.subs(n0(r), sp.exp(-(r - r0)**2)), r, 0) == 0
    print("   (b) inward restricted flow solves the planar continuity equation: %s; r n(r, t) -> v t n0(v t) as r -> 0 "
          "(so T5 ~ n v^2 is unbounded once the beam reaches the axis): %s; control (axial momenta) bounded: %s"
          % (cont, blow, ctl))
    return detok and curr and cont and blow and ctl


def main():
    res = {}
    for name, fn in (('H1', h1), ('H2', h2), ('H3', h3), ('H4', h4), ('H5', h5), ('H6', h6), ('H7', h7)):
        res[name] = fn()
        print(name, 'PASS' if res[name] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
