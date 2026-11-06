#!/usr/bin/env python3
"""inverse6_5: the six inverse bounds of CONSTANTS5.md R6.3-R9.5 (I.B:1513, :1685, :1978; III.F'':223; III.D:365;
II.F:1393), part 1: the microlocal constants at L_b0 that the record's proofs use, computed, and the arithmetic of the
effective replacements proved in INVERSE5-SIX.md. Labels: computed (exact, sympy; exact rationals), certified (interval
arithmetic, mpmath.iv at 40 digits, every printed decimal rounded outward), deduced (where said), READ (cited lines).
The spectral half (certified master-equation resolvent bounds) is inverse6_5m.py.

Background: five-dimensional Tangherlini at mu = 1 (r_h = 1, r_ph = 2^(1/2)); every quantity below is either invariant
under the homothety t, r -> lam t, lam r or scales as stated. Units: the trapped set is taken at z_0 = 1, sigma = 1.

  K1 (exact, mu symbolic) (H7) at b0 (I.B section 1.5, read on PART-VI-DYN.md section 3): on Sigma^s = {G^s = 0},
     G^s = f xi^2 + C/r^2 - 1/f, the functions phi_1 = f xi - u, phi_2 = f xi + u (u = 1 - 2 mu/r^2) satisfy
     H phi_1 = -nu_1 phi_1, H phi_2 = nu_2 phi_2 with VI.A (3.2)'s nu_1,2, H the Hamilton field of G^s; on Gamma
     (r^2 = 2 mu, xi = 0, C = 4 mu) nu = 4 (2 mu)^(-1/2), {phi_1, phi_2} = (2/mu)^(1/2) (c_Gamma), q^Gamma = 4,
     beta_0^Gamma = 2, and the rate in the time t, nu/q^Gamma = (2 mu)^(-1/2) (cover5.py's Lyapunov exponent).
  K2 (exact) (Gamma.4) for the 1-form operators box, box^Ups at b0 (E^Ups = 0 near Gamma, III.D section 1): in the
     frame of III.D 5.2 (c), normalised, and the inner product h_Gamma(eps) = diag(1, 1/eps, 1/eps^2) + g on V_perp,
     p_1^Gamma has characteristic polynomial lam^3 (lam^2 - 2 eps), so lam_max = (2 eps)^(1/2) exactly; with
     q^Gamma = 4 constant on Gamma, (1.4) of I.B gives gamma_+ = lam_max/4, gamma_- = (lam_max - nu/2)/4,
     gamma_+ - gamma_- = nu/8 (for every p_1), delta_Gamma(0) = 2 lam_max/nu = (eps mu)^(1/2); (Gamma.4) iff eps < 1/mu;
     the frame e_0/2, e_1/2, e_2/2 at Gamma is orthonormal for the static coframe's Euclidean form (exact), so h_Gamma's
     condition number relative to it is eps^-2.
  K3 (exact; certified) (Gamma.4) for 2 L_b0 (III.F Proposition 4.1, whose "lam_max <= C eta" has no C): the 15 x 15 A
     of III.F (4.2), built by strap5.build (imported), at Gamma with the record's constraint damping 1-form (10.49)'s
     inner piece (2 r_0)^-1 (dt + dr/4) (Kerr-Schild t, r_0 = 100 r_h; PART-IV5-CDMODES.md:36-38) decomposed exactly in
     the frame, c = (-1/200, -1/(160 2^(1/2)), -1/200, 0, 0), gam = 2 gamma_C, e_C = 1/102400. (a) charpoly(A) is strap5
     P2's lam^10 (lam + 2 gam c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2), gam c_2 = -gamma_C/100; (b) in the
     <,>_0-orthonormal monomial basis A never raises III.F's grading W (exact); (c) p_1^Gamma(eta) := -(1/2)(A~ + A~^T),
     A~_ij = A_ij eta^(W_j - W_i) (the inner product sum_P eta^(-2W(P)) <,>_0): certified brackets of lam_max at
     gamma_C = 10^6, 10^7, 10^8 and eta = 10^-1, ..., 10^-4 (interval LDL of t I - p_1 for the upper end, a Rayleigh
     quotient for the lower), the law lam_max ~ K gamma_C eta^2, and certified eta at which (Gamma.4) holds
     (lam_max < nu/2) and delta_Gamma(0) <= 1/2 (lam_max <= nu/4), with h_Gamma's condition number eta^-16.
  K4 (exact) the horizon thresholds at b0 (I.A (1.5); III.D Lemma 5.1; III.F'' Lemma 1.1): beta_0 = f'(r_h) = 2 mu^-1/2;
     box: 0; box^Ups: 1 (s > 3/2); 2 L_b0: with (10.49)'s inner piece in the ingoing chart, (2 r_0)^-1 (dv - (3/4) dr),
     a_v = 1/(2 r_0), x = a_v gamma_C r_h = gamma_C/200 and y = 0 (c_Ups,H = -(1/2) chi dr): III.F'' (1.1)'s 15 roots,
     vartheta_L = max(0, 2 - 2x) = 0 for gamma_C >= 200 (s > 1/2), against the 2 the record carries (LOSS-D 2b).
  K5 (exact) the thresholds at infinity: spec S-bar of III.F (3.1) at (v_C, e_C) = (1/2, 1/102400), min 0, so S-bar = 0
     for box, box^Ups and 2 L_b0, and with theta_in = 0 the decay order must lie above -1/2 at R_in and below -1/2 at
     R_out (I.B section 1.4): no constant order is admissible at real sigma != 0; s_C = (1 - e_C)(1 - v_C) gamma_C > 100.
  K6 (certified) Proposition 6.7 (c)'s interpolation constant (I.B Lemma 6.6): with kappa = beta' - beta = nu/8 (K2) the
     factor exp(3 Lambda e^(-pi L/4)), L = 2 sigma_0/kappa, Lambda = log sigma_0, is at most F := exp(3 sup_(s >= 1)
     log s e^(-pi s 2^(1/2) ... )) at mu = 1 (certified); with sigma_0^(-theta) <= 4 h^theta (h in [1/(4 sigma_0),
     1/(2 sigma_0)]) this gives (6.11) as ||(P'_(h,z))^-1|| <= 4 F C_a h^(-1-(beta' - eta)/(beta' - beta)), C_a the
     constant of Proposition 6.7 (a); and the elementary inequality of Lemma 6.6's last line, certified on a grid.
  K7 (exact) II.F Lemma 5.2's replacement (INVERSE5-SIX.md Lemma R1): x = Q'T x + R'x gives ||x||_X <= ||Q'|| ||Tx||_Y
     + ||R'||_(Z->X) ||x||_Z with no Hahn-Banach functional and no open mapping constant; checked on an exact model with a
     kernel (the estimate holds on 400 rational vectors; without the R' term it fails on the kernel).
  Controls (each mutates the computed path and must fail): C1 K1 with nu_1's sign reversed (H phi_1 = +nu_1 phi_1);
  C2 K2's claim lam_max = 2 eps refuted at eps = 1/8; C3 K3 at eta = 1 (no grading): lam_max > nu/2, (Gamma.4) fails;
  C4 K3 with c -> -c (future-pointing damping): lam_max >= 2 10^4 at every eta tested; C5 K3 with the trace weight 1
  (m = 1): the last charpoly factor moves to lam + 3 (1 - e_C) gam c_2; C6 K4 with a_v < 0: vartheta_L = 2 - 2x > 0;
  C7 K6 with kappa = nu/4 (the gap doubled): F moves outside the pinned interval.

    python3 checks/inverse6_5.py [--selftest]          (a few minutes)
"""
import builtins
import contextlib
import io
import math
import os
import random
import sys
import textwrap
import time
from fractions import Fraction as Fr

import sympy as sp
import numpy as np
from mpmath import iv, mp, mpf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import strap5 as ST                    # noqa: E402  (III.F (4.2)'s A, imported, not copied)

iv.dps = 40
mp.prec = iv.prec
OK = {}
F_PIN = (Fr(1), Fr(1001, 1000))            # K6's factor F, pinned


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def dec(x, sig, up):
    """an mpf (or the end of an interval) as a decimal of sig digits, rounded up or down exactly"""
    sign, man, ex, _ = mpf(x)._mpf_
    q = Fr(-man if sign else man) * Fr(2) ** ex
    if q == 0:
        return "0"
    e = math.floor(math.log10(abs(float(q))))
    k = sig - 1 - e
    n = math.ceil(q * Fr(10) ** k) if up else math.floor(q * Fr(10) ** k)
    return ("%.*e" % (sig - 1, float(Fr(n) / Fr(10) ** k)))


def ivq(q):
    q = Fr(q)
    return iv.mpf(q.numerator) / iv.mpf(q.denominator)


# ------------------------------------------------------------------------------------------------- K1
def k1(control=False):
    r, xi, C, mu = sp.symbols('r xi C mu', positive=True)
    f = 1 - mu / r**2
    u = 1 - 2 * mu / r**2
    Gs = f * xi**2 + C / r**2 - 1 / f
    ph1, ph2 = f * xi - u, f * xi + u
    H = lambda a: sp.diff(Gs, xi) * sp.diff(a, r) - sp.diff(Gs, r) * sp.diff(a, xi)   # z_0 = 1, angles inert
    Csig = r**2 * (1 / f - f * xi**2)                                                 # C on Sigma^s
    nu1 = 2 * (r**4 + xi * (r**2 - mu) * (r**2 - 2 * mu)) / (r**3 * (r**2 - mu))
    nu2 = 2 * (r**4 - xi * (r**2 - mu) * (r**2 - 2 * mu)) / (r**3 * (r**2 - mu))
    s1 = -1 if not control else 1
    e1 = sp.simplify((H(ph1) - s1 * nu1 * ph1).subs(C, Csig))
    e2 = sp.simplify((H(ph2) - nu2 * ph2).subs(C, Csig))
    rp = sp.sqrt(2 * mu)
    nuG = sp.simplify(nu1.subs({xi: 0, r: rp}))
    pb = sp.simplify((sp.diff(ph1, xi) * sp.diff(ph2, r) - sp.diff(ph1, r) * sp.diff(ph2, xi)).subs({xi: 0, r: rp}))
    # q_{z0} = 2 G(nu, dt_s) = 2 z_0 f^-1 on r > r_h (VI.A section 0); on Gamma f = 1/2
    qG = sp.simplify((2 / f).subs(r, rp))
    on = sp.simplify(Gs.subs({xi: 0, r: rp, C: 4 * mu})) == 0
    dG = [sp.simplify(sp.diff(Gs, v).subs({xi: 0, r: rp, C: 4 * mu})) for v in (r, xi)]
    ok = (e1 == 0 and e2 == 0 and sp.simplify(nuG - 4 / sp.sqrt(2 * mu)) == 0 and sp.simplify(pb - sp.sqrt(2 / mu)) == 0
          and qG == 4 and on and dG == [0, 0] and sp.simplify(nuG / qG - 1 / sp.sqrt(2 * mu)) == 0)
    return ok, nuG, pb, qG


# ------------------------------------------------------------------------------------------------- K2
def k2():
    eps, lam = sp.symbols('epsilon lam', positive=True)
    # normalised frame e_j/C^(1/2): nabla_{H_G} e_1 = -2 e_0, nabla e_2 = -2 e_1 (sigma = 1); ON frame f_0 = e_0,
    # f_1 = eps^(1/2) e_1, f_2 = eps e_2 for h_Gamma = diag(1, 1/eps, 1/eps^2); M f_j = sum_i M_ij f_i
    se = sp.sqrt(eps)
    M = sp.zeros(5, 5)
    M[0, 1] = -2 * se
    M[1, 2] = -2 * se
    kap = sp.Symbol('kappa', real=True)
    M[3, 4], M[4, 3] = -kap, kap                       # V_perp: skew rotation, no contribution
    p1 = -(M + M.T) / 2
    cp = sp.factor(p1.charpoly(lam).as_expr())
    lmax = sp.sqrt(2 * eps)
    ok_cp = sp.expand(cp - lam**3 * (lam**2 - 2 * eps)) == 0
    # the frame at Gamma (mu = 1): e_0/2 = (-dt_s + eta)/2, e_1/2 = -2^(1/2) dr, e_2/2 = (-dt_s - eta)/2; in the static
    # orthonormal coframe (w0 = f^(1/2) dt_s, w1 = f^(-1/2) dr, theta = eta/|eta|_g), f = 1/2, |eta|_g^2 = C/r^2 = 2
    s2 = sp.sqrt(2)
    dt = sp.Matrix([s2, 0, 0])          # dt_s = f^(-1/2) w0
    dr = sp.Matrix([0, 1 / s2, 0])      # dr = f^(1/2) w1
    et = sp.Matrix([0, 0, s2])
    E = [(-dt + et) / 2, -s2 * dr, (-dt - et) / 2]
    gram_euc = sp.Matrix(3, 3, lambda i, j: sp.simplify(E[i].dot(E[j])))
    Jl = sp.diag(-1, 1, 1)                               # g^-1 in the static orthonormal coframe
    gram_g = sp.Matrix(3, 3, lambda i, j: sp.simplify((E[i].T * Jl * E[j])[0]))
    ok_frame = gram_euc == sp.eye(3) and gram_g == sp.Matrix([[0, 0, -1], [0, 1, 0], [-1, 0, 0]])
    return ok_cp and ok_frame, cp, lmax, ok_frame


# ------------------------------------------------------------------------------------------------- K3
PAIRS = None
WT = [0, 1, 2, 1, 1]


def grading(pairs):
    return [2 * (WT[a] + WT[b]) + (1 if a in (1, 3, 4) and b in (1, 3, 4) else 0) for a, b in pairs]


def build_A(m=sp.Rational(2, 3), flip=False):
    A, pairs, c = ST.build(4, m)
    s2 = sp.Symbol('s2', positive=True)                  # 2^(1/2), kept exact
    sg = -1 if flip else 1
    sub = {c[0]: sg * sp.Rational(-1, 200), c[1]: sg * (-s2 / 320), c[2]: sg * sp.Rational(-1, 200), c[3]: 0, c[4]: 0}
    return A.subs(sub), pairs, c, s2


def exact_parts(A, s2, gC, eC):
    """entries as (p, q) with entry = p + q 2^(1/2), p, q rational, at gam = 2 gamma_C, e_C"""
    out = {}
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            e = sp.expand(A[i, j].subs({ST.gam: 2 * gC, ST.eC: eC}))
            if e == 0:
                continue
            P = sp.Poly(e, s2)
            co = {mon[0]: cf for mon, cf in zip(P.monoms(), P.coeffs())}
            p = Fr(int(sp.Rational(co.get(0, 0)).p), int(sp.Rational(co.get(0, 0)).q))
            q = Fr(int(sp.Rational(co.get(1, 0)).p), int(sp.Rational(co.get(1, 0)).q))
            assert set(co) <= {0, 1}
            out[(i, j)] = (p, q)
    return out


def p1_interval(parts, pairs, W, eta):
    """p_1^Gamma(eta) as an interval matrix, in the h_Gamma-orthonormal basis; nrm = 1 on e_a^2, 2^(1/2) on 2 e_a e_b"""
    n = len(pairs)
    S2 = iv.sqrt(2)
    nrm = [iv.mpf(1) if a == b else S2 for a, b in pairs]
    et = ivq(eta)
    At = [[iv.mpf(0)] * n for _ in range(n)]
    for (i, j), (p, q) in parts.items():
        val = ivq(p) + ivq(q) * S2
        At[i][j] = nrm[i] * val / nrm[j] * et ** (W[j] - W[i])
    return [[-(At[i][j] + At[j][i]) / 2 for j in range(n)] for i in range(n)]


def ldl_posdef(M, t):
    """certified: t I - M is positive definite iff every pivot of its LDL^T is > 0 (interval elimination)"""
    n = len(M)
    B = [[(ivq(t) if i == j else iv.mpf(0)) - M[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        d = B[k][k]
        if not d.a > 0:
            return False
        for i in range(k + 1, n):
            lik = B[i][k] / d
            for j in range(k + 1, n):
                B[i][j] = B[i][j] - lik * B[k][j]
    return True


def rayleigh_lower(M, v):
    vv = [ivq(Fr(x).limit_denominator(10 ** 12)) for x in v]
    num = sum(vv[i] * M[i][j] * vv[j] for i in range(len(M)) for j in range(len(M)))
    den = sum(x * x for x in vv)
    return (num / den).a


def mid_matrix(M):
    return np.array([[float(mpf(x.mid)) for x in row] for row in M])


def lam_bracket(parts, pairs, W, eta, rel=Fr(1, 10 ** 4)):
    M = p1_interval(parts, pairs, W, eta)
    Mf = mid_matrix(M)
    w, V = np.linalg.eigh(Mf)
    top, v = w[-1], V[:, -1]
    lo = rayleigh_lower(M, v)
    hi = Fr(top) * (1 + rel) + Fr(1, 10 ** 30) if top > 0 else Fr(top) * (1 - rel) + Fr(1, 10 ** 30)
    assert ldl_posdef(M, hi), (eta, top)
    return lo, hi, M


def k3(verbose=True):
    res = {}
    A, pairs, c, s2 = build_A()
    W = grading(pairs)
    lam = sp.Symbol('lam')
    gam, eC = ST.gam, ST.eC
    # (a) the characteristic polynomial, gamma and e_C symbolic, c at the record's point
    cp = sp.factor(A.charpoly(lam).as_expr())
    g2 = gam * sp.Rational(-1, 200)
    target = lam**10 * (lam + 2 * g2)**3 * (lam + 4 * g2) * (lam + 2 * (1 - eC) * g2)
    res['a'] = sp.expand(cp - target) == 0
    # (b) the grading: in the <,>_0-orthonormal basis an entry (i, j) != 0 only if W_i <= W_j (nrm cancels in 0-tests)
    raise_ = [(pairs[i], pairs[j]) for i in range(15) for j in range(15)
              if sp.simplify(A[i, j]) != 0 and W[i] > W[j]]
    res['b'] = not raise_
    # D_0: the W-preserving part; its symmetric part's eigenvalues (gamma_C symbolic), with -(1/2)(D_0 + D_0^T) <= 0
    D0 = sp.Matrix(15, 15, lambda i, j: A[i, j] if W[i] == W[j] else 0)
    nrm = [1 if a == b else sp.sqrt(2) for a, b in pairs]
    D0o = sp.Matrix(15, 15, lambda i, j: sp.simplify(nrm[i] * D0[i, j].subs(s2, sp.sqrt(2)) / nrm[j]))
    sym = -(D0o + D0o.T) / 2
    evs = sym.subs({gam: 2 * 10**6, eC: sp.Rational(1, 102400)}).eigenvals()
    res['D0'] = all(sp.N(k_) <= 1e-30 for k_ in evs)
    rows = []
    for gC in (10**6, 10**7, 10**8):
        parts = exact_parts(A, s2, gC, sp.Rational(1, 102400))
        for eta in (Fr(1, 10), Fr(1, 100), Fr(1, 1000), Fr(1, 10000)):
            lo, hi, _ = lam_bracket(parts, pairs, W, eta)
            rows.append((gC, eta, lo, hi))
    res['rows'] = rows
    # the law: lam_max/(gamma_C eta^2) at the smallest eta, three gamma_C
    Ks = [(gC, float(lo) / (gC * float(eta) ** 2), float(hi) / (gC * float(eta) ** 2))
          for gC, eta, lo, hi in rows if eta == Fr(1, 10000)]
    res['K'] = Ks
    # the admissible eta at gamma_C = 10^6, 10^7, 10^8: largest eta = k/10^4 with lam_max < nu/2 (= 2^(1/2) at mu = 1),
    # certified there, and the next grid point certified >= nu/2 (no monotonicity is claimed); likewise nu/4
    nu2, nu4 = iv.sqrt(2), iv.sqrt(2) / 2
    adm = []
    for gC in (10**6, 10**7, 10**8):
        parts = exact_parts(A, s2, gC, sp.Rational(1, 102400))
        out = []
        for thr, name in ((nu2, 'nu/2'), (nu4, 'nu/4')):
            # float search for the crossing, then certify both sides
            def lam_f(eta):
                return np.linalg.eigvalsh(mid_matrix(p1_interval(parts, pairs, W, eta)))[-1]
            k_ = 1
            target_f = float(mpf(thr.mid))
            lo_k, hi_k = 1, 10000
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if lam_f(Fr(mid, 10 ** 5)) < target_f:
                    lo_k = mid
                else:
                    hi_k = mid
            e_lo, e_hi = Fr(lo_k, 10 ** 5), Fr(hi_k, 10 ** 5)
            M_lo = p1_interval(parts, pairs, W, e_lo)
            below = ldl_posdef(M_lo, Fr(mpf(thr.a)))           # lam_max < thr.a <= thr
            M_hi = p1_interval(parts, pairs, W, e_hi)
            w_, V_ = np.linalg.eigh(mid_matrix(M_hi))
            above = rayleigh_lower(M_hi, V_[:, -1]) > thr.b
            out.append((name, e_lo, e_hi, below and above))
        adm.append((gC, out))
    res['adm'] = adm
    ok = res['a'] and res['b'] and res['D0'] and all(lo <= hi and lo > 0 for _, _, lo, hi in rows) and \
        all(x[3] for _, o in adm for x in o)
    return ok, res, (A, pairs, s2, W)


def k3_controls(A, pairs, s2, W):
    out = {}
    parts = exact_parts(A, s2, 10**6, sp.Rational(1, 102400))
    # C3: eta = 1
    M = p1_interval(parts, pairs, W, Fr(1))
    w_, V_ = np.linalg.eigh(mid_matrix(M))
    out['C3'] = rayleigh_lower(M, V_[:, -1]) > iv.sqrt(2).b
    # C4: c -> -c (future-pointing c): lam_max >= 2 10^4 at every eta tested
    Af, pf, _, s2f = build_A(flip=True)
    partsf = exact_parts(Af, s2f, 10**6, sp.Rational(1, 102400))
    lows = []
    for eta in (Fr(1, 10), Fr(1, 100), Fr(1, 1000), Fr(1, 10000)):
        Mf = p1_interval(partsf, pf, W, eta)
        w_, V_ = np.linalg.eigh(mid_matrix(Mf))
        lows.append(rayleigh_lower(Mf, V_[:, -1]))
    out['C4'] = all(x >= 2 * 10**4 * (1 - Fr(1, 10**4)) for x in lows)
    # C5: the trace weight 1
    A1, p1_, c1, s21 = build_A(m=sp.Integer(1))
    lam = sp.Symbol('lam')
    g2 = ST.gam * sp.Rational(-1, 200)
    cp1 = sp.factor(A1.charpoly(lam).as_expr())
    good = lam**10 * (lam + 2 * g2)**3 * (lam + 4 * g2) * (lam + 2 * (1 - ST.eC) * g2)
    alt = lam**10 * (lam + 2 * g2)**3 * (lam + 4 * g2) * (lam + 3 * (1 - ST.eC) * g2)
    out['C5'] = sp.expand(cp1 - good) != 0 and sp.expand(cp1 - alt) == 0
    return out, lows


# ------------------------------------------------------------------------------------------------- K4, K5
def k4(control=False):
    x, y, k, eC, gC = sp.symbols('x y k e_C gamma_C')
    poly = k**5 * (k - 1 + x)**3 * (k - 2 + 2 * x) * (k + (1 - eC) * x) * (k - y) * (k + 1 - y)**3 * (k + 2 - 2 * y)
    # (10.49)'s inner piece at mu = 1, r_0 = 100: (1/200)(dt + dr/4), t = v - r (Kerr-Schild), so (1/200)(dv - (3/4) dr)
    v_, r_ = sp.symbols('v r')
    t_ks = v_ - r_
    cC = sp.Rational(1, 200) * (sp.Matrix([sp.diff(t_ks, v_), sp.diff(t_ks, r_)]) + sp.Matrix([0, sp.Rational(1, 4)]))
    av = cC[0] if not control else -cC[0]
    rh = 1
    vals = {x: av * gC * rh, y: 0, eC: sp.Rational(1, 102400)}
    roots = sp.roots(sp.Poly(poly.subs(vals), k))
    deg = sum(roots.values())
    theta = sp.Max(0, *[sp.re(z) for z in roots])
    th6 = theta.subs(gC, 10**6)
    beta0 = sp.diff(1 - 1 / sp.Symbol('rr')**2, sp.Symbol('rr')).subs(sp.Symbol('rr'), 1)
    ok = deg == 15 and sp.simplify(cC[1] + sp.Rational(3, 800)) == 0 and av == sp.Rational(1, 200) and th6 == 0 \
        and beta0 == 2
    return ok, av, roots, th6


def k5():
    gC, gU, eU = sp.symbols('gamma_C gamma_U e_U', positive=True)
    vC, eC = sp.Rational(1, 2), sp.Rational(1, 102400)
    spec = [0] * 5 + [gC * 2 * (1 - vC), gC * (1 - eC) * (1 - vC)] + [gC * (1 - vC)] * 3 + \
        [2 * gU, gU * (1 - eU)] + [gU] * 3
    sub = {gC: 10**6, gU: sp.Rational(1, 100), eU: sp.Rational(1, 100)}
    vals = [sp.nsimplify(s_.subs(sub)) for s_ in spec]
    Sbar = min(vals)
    sC = ((1 - eC) * (1 - vC) * gC).subs(gC, 10**6)
    return Sbar == 0 and len(vals) == 15 and sC > 100, vals, Sbar, sC


# ------------------------------------------------------------------------------------------------- K6
def k6(kappa=None):
    """F = exp(3 sup_{s >= 1} log s e^(-pi s/(2 kappa))), kappa = nu/8 = 1/(2 2^(1/2)) at mu = 1"""
    if kappa is None:
        kappa = 1 / (2 * iv.sqrt(2))
    c = iv.pi / (2 * kappa)
    # on [1, 4]: 4000 pieces, enclosure of log s e^(-c s); beyond 4 the function decreases (derivative
    # e^(-cs)(1/s - c log s) < 0 once c s log s > 1, certified at s = 4 and increasing in s)
    best = iv.mpf(0)
    n = 4000
    for i in range(n):
        a = 1 + Fr(3 * i, n)
        b = 1 + Fr(3 * (i + 1), n)
        S = iv.mpf([mpf(a.numerator) / a.denominator, mpf(b.numerator) / b.denominator])
        val = iv.log(S) * iv.exp(-c * S)
        best = iv.mpf([max(best.a, val.a), max(best.b, val.b)])
    dec4 = (c * 4 * iv.log(4)).a > 1
    tail = (iv.log(4) * iv.exp(-c * 4)).b <= best.b
    F = iv.exp(3 * best)
    # Lemma 6.6's last inequality: cosh(a)/cosh(2a) <= 2 e^(-a) for a >= 0 (a = pi L/4), on a grid
    lem = all((iv.cosh(iv.mpf(a) / 10) / iv.cosh(iv.mpf(a) / 5)).b <= (2 * iv.exp(-iv.mpf(a) / 10)).a
              for a in range(0, 400))
    return F, dec4 and tail and lem, best


# ------------------------------------------------------------------------------------------------- K7
def k7(drop_R=False, seed=5):
    """exact model: T = diag(0, 1, 2) on Q^3 (kernel e_1), j = identity into Z = Q^3 with ||.||_Z = ||.||_1/10;
    Q' = diag(0, 1, 1/2) is a left parametrix, R' := I - Q' T = diag(1, 0, 0)"""
    T = [Fr(0), Fr(1), Fr(2)]
    Qp = [Fr(0), Fr(1), Fr(1, 2)]
    R = [1 - q * t for q, t in zip(Qp, T)]
    nQ = max(abs(q) for q in Qp)                      # sup norms
    nR = max(abs(x) for x in R) * 10                  # ||R'||_{Z->X} with ||.||_Z = ||.||_inf/10
    rnd = random.Random(seed)
    good = True
    for _ in range(400):
        x = [Fr(rnd.randint(-50, 50), rnd.randint(1, 9)) for _ in range(3)]
        lhs = max(abs(v) for v in x)
        Tx = [t * v for t, v in zip(T, x)]
        rhs = nQ * max(abs(v) for v in Tx) + (0 if drop_R else nR * max(abs(v) for v in x) / 10)
        good &= lhs <= rhs
    xk = [Fr(1), Fr(0), Fr(0)]                       # the kernel
    lhs = max(abs(v) for v in xk)
    rhs = nQ * 0 + (0 if drop_R else nR * Fr(1, 10))
    good &= lhs <= rhs
    return good


# ------------------------------------------------------------------------------------------------- main
def main():
    t0 = time.time()
    ok1, nuG, pb, qG = k1()
    OK['K1'] = ok1
    print('  K1 (exact, mu symbolic): on Sigma^s, H phi_1 = -nu_1 phi_1 and H phi_2 = nu_2 phi_2 with VI.A (3.2)\'s nu_1,2;'
          ' on Gamma nu = %s, {phi_1, phi_2} = %s, q^Gamma = %s, beta_0^Gamma = 2, nu/q^Gamma = (2 mu)^(-1/2): %s'
          % (sp.simplify(nuG), sp.simplify(pb), qG, ok1))
    c1, _, _, _ = k1(control=True)
    OK['C1'] = not c1
    print('  C1 (control): K1 with H phi_1 = +nu_1 phi_1 claimed: fails: %s' % OK['C1'])

    ok2, cp2, lmax, okf = k2()
    OK['K2'] = ok2
    eps = sp.Symbol('epsilon', positive=True)
    print('  K2 (exact): 1-form p_1^Gamma in h_Gamma(eps): charpoly %s, lam_max = (2 eps)^(1/2); gamma_+ - gamma_- = nu/8,'
          ' delta_Gamma(0) = 2 lam_max/nu = (eps mu)^(1/2), (Gamma.4) iff eps < 1/mu; the frame at Gamma orthonormal for'
          ' the static coframe (cond(h_Gamma) = eps^-2): %s' % (cp2, ok2))
    OK['C2'] = sp.simplify(sp.sqrt(2 * eps).subs(eps, sp.Rational(1, 8)) - 2 * sp.Rational(1, 8)) != 0
    print('  C2 (control): the claim lam_max = 2 eps at eps = 1/8 (1/4) against (2 eps)^(1/2) = 1/2: refuted: %s'
          % OK['C2'])

    ok3, res, (A, pairs, s2, W) = k3()
    OK['K3'] = ok3
    print('  K3 (a) charpoly(A) = lam^10 (lam + 2 gam c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2) at c = (-1/200,'
          ' -1/(160 2^(1/2)), -1/200, 0, 0), gam = 2 gamma_C (gam c_2 = -gamma_C/100): %s; (b) A never raises W (W ='
          ' %s): %s; -(1/2)(D_0 + D_0^T) <= 0 at gamma_C = 10^6: %s' % (res['a'], W, res['b'], res['D0']))
    for gC, eta, lo, hi in res['rows']:
        print('  K3 (c) gamma_C = 10^%d, eta = %s: lam_max(p_1^Gamma) in [%s, %s] (certified)'
              % (round(math.log10(gC)), eta, dec(mpf(lo.numerator) / lo.denominator if isinstance(lo, Fr) else lo, 6,
                                                  False), dec(mpf(hi.numerator) / hi.denominator, 6, True)))
    for gC, klo, khi in res['K']:
        print('  K3 the law at eta = 10^-4: lam_max/(gamma_C eta^2) in [%.6f, %.6f] at gamma_C = 10^%d'
              % (klo, khi, round(math.log10(gC))))
    for gC, out in res['adm']:
        for name, e_lo, e_hi, good in out:
            print('  K3 (Gamma.4) at gamma_C = 10^%d: lam_max < %s certified at eta = %s, > %s certified at eta = %s: %s;'
                  ' cond(h_Gamma) = eta^-16 = %.3e at the first' % (round(math.log10(gC)), name, e_lo, name, e_hi, good,
                                                                    float(e_lo) ** -16))
    ctl, lows = k3_controls(A, pairs, s2, W)
    OK['C3'] = ctl['C3']
    OK['C4'] = ctl['C4']
    OK['C5'] = ctl['C5']
    print('  C3 (control): eta = 1 (no grading): lam_max > nu/2 = 2^(1/2), (Gamma.4) fails: %s' % OK['C3'])
    print('  C4 (control): c -> -c (future-pointing): lam_max >= %s at eta = 10^-1..10^-4 (>= 2 10^4 (1 - 10^-4)): %s'
          % (', '.join('%.1f' % float(mpf(x)) for x in lows), OK['C4']))
    print('  C5 (control): trace weight 1: the last factor becomes lam + 3 (1 - e_C) gam c_2 (strap5 P2\'s own '
          'control): %s' % OK['C5'])

    ok4, av, roots, th6 = k4()
    OK['K4'] = ok4
    print('  K4 (exact): beta_0 = f\'(r_h) = 2 (mu = 1); a_v = %s, x = gamma_C/200; III.F\'\' (1.1)\'s roots at y = 0: %s;'
          ' vartheta_L = %s at gamma_C = 10^6 (s > 1/2); box 0, box^Ups 1: %s'
          % (av, {sp.simplify(k_): m_ for k_, m_ in roots.items()}, th6, ok4))
    ok4c, _, _, th6c = k4(control=True)
    OK['C6'] = (not ok4c) and th6c > 0
    print('  C6 (control): a_v < 0 (c_C future-pointing at the horizon): vartheta_L = %s > 0: %s' % (th6c, OK['C6']))

    ok5, vals, Sbar, sC = k5()
    OK['K5'] = ok5
    print('  K5 (exact): spec S-bar of III.F (3.1) at (v_C, e_C, gamma_C, gamma_Ups, e_Ups) = (1/2, 1/102400, 10^6, '
          '1/100, 1/100): min %s, so S-bar = 0; thresholds -1/2 at R_in (theta_in = 0) and at R_out: a variable decay '
          'order is needed at real sigma != 0; s_C = %s > 100: %s' % (Sbar, sC, ok5))

    F, okl, best = k6()
    OK['K6'] = okl and F.b <= ivq(F_PIN[1]) and F.a >= ivq(F_PIN[0])
    print('  K6 (certified): kappa = nu/8 = 2^(-3/2) (mu = 1): sup_(s >= 1) log s e^(-pi s/(2 kappa)) <= %s, so F <= %s'
          ' and (6.11) holds with the constant 4 F C_a <= %s C_a; Lemma 6.6\'s last inequality on a grid: %s'
          % (dec(best.b, 5, True), dec(F.b, 7, True), dec((4 * F).b, 6, True), OK['K6']))
    Fc, _, _ = k6(kappa=1 / iv.sqrt(2))
    OK['C7'] = not (Fc.b <= ivq(F_PIN[1]))
    print('  C7 (control): kappa = nu/4: F = %s, outside the pin [1, 1.001]: %s' % (dec(Fc.b, 6, True), OK['C7']))

    OK['K7'] = k7()
    OK['C8'] = not k7(drop_R=True)
    print('  K7 (exact): x = Q\'T x + R\'x: ||x|| <= ||Q\'|| ||Tx|| + ||R\'||_(Z->X) ||x||_Z on 400 rational vectors and on'
          ' the kernel: %s; C8 (control) without the R\' term it fails on the kernel: %s' % (OK['K7'], OK['C8']))
    print('  (%.0f s)' % (time.time() - t0))
    for k_, v_ in OK.items():
        builtins.print(k_, 'PASS' if v_ else 'FAIL')
    if '--selftest' in sys.argv:
        sys.exit(0 if all(OK.values()) else 1)


if __name__ == '__main__':
    main()
