#!/usr/bin/env python3
"""lzeroconst5: Theorem 1's lambda0 as a formula, and its certified leaves at the paper's numerical point (CONSTANTS5.md,
L2-L4).

The point P*: l5 = 1/10, mu0 = 1 (L = mu0/l5^2 = 100, the paper's section 9 and growth5.py), A = 1, the numerics'
envelope sin^4(pi (v - 1/2)/3) on [1/2, 7/2], T = 1, tau0 = -2, K = 6 (so k = 6, N = 9), and the free radius a :=
q0/2 (delta0 = q0/2). Labels: computed (exact rationals; roots and pi in certified rational bounds); computed, floating
point (Z3's test functions, Z4's random check, Z2's control perturbation); deduced (the formula, collected from
N1STAR-PROOF.md section 4 Steps 3 and 7 and Proposition 6.5).

  Z0 (exact) the numerics' envelope is C^3 and not C^4 at its ends (sin^4 x = (3 - 4 cos 2x + cos 4x)/8: derivatives
     0-3 vanish at 0, the fourth is 24), so it is not in C_c^inf as Theorem 1 asks; every leaf below depends on the
     envelope only through mu_end = mu0 + (2/9) A^2 int env^2, so it holds for every smooth envelope with that integral.
  Z1 (certified) the domain of N1STAR-PROOF.md section 1 at P*: q0, a, mu_end = 227/192, q_end, tau_end, b(tau0),
     tau_end - tau0, lam1 = min(1, delta0)/10, and Lemma 1.1 (f)'s b - a >= 1 + delta0.
  Z2 (certified) Lemma 1.1 (e)'s eps1, explicit: for |g - g0|_op <= eps1, |g^-1 - g0^-1| <= n^2 eps/(1 - n eps) with
     n := 1 + 2 mu_end/a^2 >= sup_Omega |g0^-1|_op, and the margins of (a)-(c) are at least 1, mu0/a^2 - 1 and 3/5
     (|d(v + tau)|^2 = 5 against -3 - mu/r^2); so eps1 := (3/5)/(n^2 + (3/5) n). Control: an explicit perturbation at
     r = a making d(v + tau) null has size above eps1, and a claim of 1.01 times its size is refuted by it.
  Z3 (certified) Lemma 2.1's Sobolev constant: ||f||_inf <= C_S sum_{i<=3} ||d^i f||_{L^2(A)} on every annulus A of
     width >= 1 in R^4, by the cone formula with the cut-off p(s) = (1 - s)^3 (1 + 3s + 6s^2), height 1/2, aperture
     pi/3. Controls: test functions stay below C_S (floating point); C_S/10^4 is refuted by one; at m = 2 the cone
     integral diverges (no constant); a cone of height (b - a)/2 + 1/4 leaves the annulus.
  Z4 (deduced; checked in floating point) lambda0 = min of eight closed-form terms; at lambda0 every condition of the
     proof holds and slightly above it one fails, on random inputs. Control: the formula without its Step-7 term fails.
  Z5 the formula at P*: which leaves are certified (Z1-Z3) and which are not computed, with what each needs.

    python3 checks/lzeroconst5.py
"""
import math
import random
import sys
import textwrap
from fractions import Fraction as Fr

import numpy as np

L5, MU0, A_AMP = Fr(1, 10), Fr(1), Fr(1)
VS, VE, T, TAU0, K = Fr(1, 2), Fr(7, 2), Fr(1), Fr(-2), 6
NST = K + 3
PI_LO, PI_HI = Fr(333, 106), Fr(355, 113)
S3_LO, S3_HI = Fr(17320, 10000), Fr(17321, 10000)
S2_LO, S2_HI = Fr(14142, 10000), Fr(14143, 10000)


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def iroot(n, k):
    """floor(n^(1/k)) for an integer n >= 0"""
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + k - 1) // k)
    while True:
        y = ((k - 1) * x + n // x ** (k - 1)) // k
        if y >= x:
            break
        x = y
    while x ** k > n:
        x -= 1
    while (x + 1) ** k <= n:
        x += 1
    return x


def root_iv(x, k, S=10 ** 30):
    """certified [lo, hi] for x^(1/k), x a positive Fraction"""
    p, q = x.numerator, x.denominator
    r = iroot(p * q ** (k - 1) * S ** k, k)
    return Fr(r, q * S), Fr(r + 1, q * S)


def env_smoothness():
    """derivatives of sin^4 x = (3 - 4 cos 2x + cos 4x)/8 at 0: d^j cos(cx) at 0 is c^j cos(j pi/2)"""
    def dj(j):
        c = {0: 1, 1: 0, 2: -1, 3: 0}[j % 4]
        return Fr(-4 * 2 ** j * c + 4 ** j * c, 8) + (Fr(3, 8) if j == 0 else 0)
    return [dj(j) for j in range(6)]


def geometry():
    q0 = root_iv(Fr(9, 1250), 8)                       # q0^8 = 72 mu0^2 l5^4 / 10^0 = 9/1250 at P*
    assert q0[0] ** 8 <= 72 * MU0 ** 2 * L5 ** 4 <= q0[1] ** 8
    mu_end = MU0 + Fr(2, 9) * A_AMP ** 2 * Fr(105, 128)   # int sin^8 over [1/2, 7/2] = 3 * 35/128
    m4 = root_iv(mu_end, 4)
    qe = (q0[0] * m4[0], q0[1] * m4[1])
    a = (q0[0] / 2, q0[1] / 2)
    V = VE + T
    # v - r_q(v) increases: 1 - q0 mu^(-3/4) mu'/4 >= 1 - q0 (2/9)/4 > 0 (mu >= 1, mu' <= (2/9) A^2)
    assert 1 - q0[1] * Fr(2, 9) / 4 > 0
    tau_end = (V - qe[1], V - qe[0])
    b0 = (V + 1 + tau_end[0] - 2 * TAU0, V + 1 + tau_end[1] - 2 * TAU0)
    dtau = (tau_end[0] - TAU0, tau_end[1] - TAU0)
    lam1 = (q0[0] / 20, q0[1] / 20)                    # min(1, delta0)/10, delta0 = q0/2 < 1
    seed = VS - TAU0 > 1 + 1                           # v_start - tau0 > sqrt(mu0) + 1
    fwidth = qe[0] - a[1] >= q0[1] - a[0] - Fr(1, 10 ** 25)   # b(tau_end) - a = 1 + q_end - a >= 1 + delta0
    return dict(q0=q0, mu_end=mu_end, qe=qe, a=a, V=V, tau_end=tau_end, b0=b0, dtau=dtau, lam1=lam1, seed=seed,
                fwidth=fwidth)


def eps1_bound(g):
    a_lo = g['a'][0]
    n = 1 + 2 * g['mu_end'] / a_lo ** 2
    margins = {'(a) dtau timelike': Fr(1), '(b) dr timelike at r = a': MU0 / g['a'][1] ** 2 - 1,
               '(b) g^-1(dr, dtau) > 0': MU0 / g['a'][1] ** 2, '(c) d(v + tau) timelike': Fr(3, 5)}
    m = min(margins.values())
    eps1 = m / (n * n + n * m)
    return eps1, n, m, margins


def g0inv(X, mu):
    tau, x = X[0], np.array(X[1:])
    r = np.linalg.norm(x)
    L0 = np.concatenate([[1.0], -x / r])
    return np.diag([-1.0, 1, 1, 1, 1]) - (mu / r ** 2) * np.outer(L0, L0)


def poly_sup(coeffs, N=20000):
    """certified upper bound of sup_[0,1] |p|, p = sum c_i s^i (Fractions): grid maximum plus the Lipschitz slack"""
    der = [i * c for i, c in enumerate(coeffs)][1:]
    lip = sum(abs(c) for c in der)
    best = max(abs(sum(c * Fr(k, N) ** i for i, c in enumerate(coeffs))) for k in range(N + 1))
    return best + lip / (2 * N)


def sobolev(m=3, n=4, h=Fr(1, 2)):
    """C_S of |f(x)| <= C_S sum_{j<=m} ||d^j f||_{L^2(C_x)}, by f(x) = (-1)^m/(m-1)! int_0^h t^(m-1) d_t^m (psi f) dt
    averaged over the cap of aperture pi/3, and Cauchy-Schwarz; returns None when int t^(2(m-n)) t^(n-1) dt diverges"""
    expo = 2 * m - n - 1
    if expo <= -1:
        return None
    p = [Fr(1), Fr(0), Fr(0), Fr(-10), Fr(15), Fr(-6)]          # (1 - s)^3 (1 + 3s + 6s^2)
    ders = [p]
    for _ in range(m):
        ders.append([i * c for i, c in enumerate(ders[-1])][1:])
    sups = [poly_sup(d) for d in ders]
    coef = max(math.comb(m, j) * sups[m - j] / h ** (m - j) for j in range(m + 1))
    cap_lo = 2 * PI_LO * (PI_LO / 3 - S3_HI / 4)                # |S_theta| = 2 pi (pi/3 - sqrt3/4) on S^3
    sq_cap = root_iv(cap_lo, 2)[0]
    integral = h ** (2 * m - n) / (2 * m - n)                   # int_0^h t^(2m-n-1) dt
    sq_int = root_iv(integral, 2)[1]
    C = sq_int / (math.factorial(m - 1) * sq_cap) * coef
    return C, sups, coef, cap_lo


def cone_inside(a, b, h, theta, trials=2000, rng=random.Random(5)):
    """does the cone {x + t w : 0 < t <= h, angle(w, axis) <= theta} stay in {a <= |x| <= b} for |x| in [a, b], the
    axis outward when |x| <= (a + b)/2 and inward otherwise? (floating-point sample, worst points included)"""
    worst = [(a, 1, 1.0), ((a + b) / 2 - 1e-12, 1, 1.0), ((a + b) / 2 + 1e-12, -1, 1.0), (b, -1, 1.0)]
    for rad, sgn, _ in worst + [(rng.uniform(a, b), 0, 0)] * trials:
        if sgn == 0:
            sgn = 1 if rad <= (a + b) / 2 else -1
        for ang in (0.0, theta, theta / 2):
            for t in (h, h / 2, 1e-9):
                # in the plane of x and w: x = (rad, 0), w = sgn (cos ang, sin ang)
                y = (rad + t * sgn * math.cos(ang), t * math.sin(ang))
                ry = math.hypot(*y)
                if ry < a - 1e-12 or ry > b + 1e-12:
                    return False
    return True


def test_ratio(a, b, c, w):
    t = np.linspace(-b, b, 200001)
    S = (4 * np.pi / 3) * (np.clip(b * b - t * t, 0, None) ** 1.5 - np.clip(a * a - t * t, 0, None) ** 1.5)
    u = (t - c) / w
    ph = np.exp(-u * u)
    d = [ph, -2 * u / w * ph, (4 * u * u - 2) / w ** 2 * ph, (-8 * u ** 3 + 12 * u) / w ** 3 * ph]
    norms = [math.sqrt(np.trapezoid(q * q * S, t)) for q in d]
    sup = 1.0 if -b <= c <= b else max(ph)
    return sup / sum(norms)


def lambda0(c):
    """the closed form: lam0 = min of the seven terms (deduced from N1STAR-PROOF.md section 4, Steps 3 and 7, and
    Proposition 6.5, with the standing lam1 of section 2)"""
    C3 = c['Cst'] * c['C2'] * math.exp(c['C2'] * c['dtau']) * (1 + c['dtau'])
    M = C3 * (c['CD'] + 1 + c['CR']) + 1
    terms = {'lam1': c['lam1'],
             'E-a': c['eps1'] / (2 * c['Capp']),
             'E-b': (min(c['eps1'], c['eps2']) / 2 / (2 * c['Cinf'] * M)) ** (1 / (K - 3)),
             'E-c': (1 / (2 * c['Cdw'] * M)) ** (1 / (K - 4)),
             'E-d': 1 / (C3 * c['CN'] * M ** 2),
             'D-a': (c['mc'] / (2 * c['Cc'] * c['C0'])) ** (1 / (NST - 3)),
             'D-b': (1 / (2 * c['Ck'])) ** (1 / (NST - 3)),
             'D-c': c['ms'] / c['Cs']}
    return min(terms.values()), terms, M, C3


def conditions(c, lam, M, C3):
    """the proof's conditions at lam: Step 3 (|g_app - g0| <= C_app lam and |w| <= 2 Cinf M lam^(K-3) within eps1,
    and |w| within eps2/2; |dw| <= 1), Step 7
    (C3 C_N M^2 lam <= 1), Proposition 6.5 (frozen coefficients within the margin; contraction factor <= 1/2), Lemma
    6.3 (c) (signs), and lam <= lam1"""
    return {'lam1': lam <= c['lam1'],
            'E-a': c['Capp'] * lam <= c['eps1'] / 2,
            'E-b': 2 * c['Cinf'] * M * lam ** (K - 3) <= min(c['eps1'], c['eps2']) / 2,
            'E-c': 2 * c['Cdw'] * M * lam ** (K - 4) <= 1,
            'E-d': C3 * c['CN'] * M * M * lam <= 1,
            'D-a': 2 * c['Cc'] * c['C0'] * lam ** (NST - 3) <= c['mc'],
            'D-b': c['Ck'] * lam ** (NST - 3) <= 0.5,
            'D-c': c['Cs'] * lam <= c['ms']}


def main():
    ok = {}
    dj = env_smoothness()
    ok['Z0'] = dj[:4] == [0, 0, 0, 0] and dj[4] == 24
    say('  Z0: d^j sin^4 at 0, j = 0..5: %s: C^3, not C^4 at v_start and v_end (the jump of env\'\'\'\' is 24 (pi/3)^4)'
        % [str(x) for x in dj])

    g = geometry()
    f = lambda iv: '[%.9f, %.9f]' % (float(iv[0]), float(iv[1]))
    say('  Z1: q0 = (sqrt72 mu0 l5^2)^(1/4) in %s; a = delta0 = q0/2 in %s; mu_end = %s = %.6f; q_end in %s; '
        'V = %s; tau_end = V - q_end in %s; b(tau0) in %s; tau_end - tau0 in %s; lam1 = q0/20 in %s; '
        'v_start - tau0 > sqrt(mu0) + 1: %s; Lemma 1.1 (f) width: %s' % (
            f(g['q0']), f(g['a']), g['mu_end'], float(g['mu_end']), f(g['qe']), g['V'], f(g['tau_end']), f(g['b0']),
            f(g['dtau']), f(g['lam1']), g['seed'], g['fwidth']))
    ok['Z1'] = g['seed'] and g['fwidth'] and g['q0'][1] - g['q0'][0] < Fr(1, 10 ** 25)

    eps1, n, m, margins = eps1_bound(g)
    say('  Z2: n = 1 + 2 mu_end/a^2 <= %.4f; margins %s; binding 3/5; eps1 = %.6e in the operator norm (%.6e in the '
        'largest Cartesian entry, |.|_op <= 5 max|entry|)' % (float(n), {k: round(float(v), 4) for k, v in
                                                                         margins.items()}, float(eps1), float(eps1) / 5))
    rng = np.random.default_rng(3)
    worst = 0.0
    a_f, mu_e = float(g['a'][0]), float(g['mu_end'])
    for _ in range(2000):
        r = rng.uniform(a_f, 9.0)
        x = rng.normal(size=4)
        x = r * x / np.linalg.norm(x)
        worst = max(worst, np.linalg.norm(g0inv([0.0, *x], mu_e), 2) / (1 + 2 * mu_e / r ** 2))
    a_hi, mu0 = float(g['a'][1]), 1.0
    G0i = g0inv([0.0, a_hi, 0, 0, 0], mu0)
    xi = np.array([2.0, 1.0, 0, 0, 0])                       # d(v + tau) = 2 dtau + dr at x = (a, 0, 0, 0)
    c_bad = -(xi @ G0i @ xi) / (xi @ xi) ** 2
    Gbad_inv = G0i + c_bad * np.outer(xi, xi)
    eps_bad = np.linalg.norm(np.linalg.inv(Gbad_inv) - np.linalg.inv(G0i), 2)
    null = abs(xi @ Gbad_inv @ xi) < 1e-9
    ok['Z2'] = worst <= 1 + 1e-12 and float(eps1) < eps_bad and null
    say('      check: sup |g0^-1|_op/(1 + 2 mu/r^2) over 2000 random points of {r >= a} = %.6f <= 1; control: a '
        'perturbation at r = a with d(v + tau) null (floating) has |g - g0|_op = %.4e > eps1 = %.4e: %s; the claim '
        '"eps1 = %.4e works" is refuted by it' % (worst, eps_bad, float(eps1), float(eps1) < eps_bad, 1.01 * eps_bad))

    CS, sups, coef, cap = sobolev()
    say('  Z3: sup |p^(j)|, j = 0..3: %s (certified); max_j C(3, j) h^-(3-j) sup|p^(3-j)| = %.4f; |S_pi/3| >= %.5f; '
        'C_S <= %.4f (certified, exact rationals)' % ([round(float(s), 5) for s in sups], float(coef), float(cap),
                                                     float(CS)))
    a_n, b_n = float(g['a'][1]), float(g['a'][0]) + 1.0     # the thinnest annulus of the family (width 1)
    inside = cone_inside(a_n, b_n, 0.5, math.pi / 3)
    outside = not cone_inside(a_n, b_n, (b_n - a_n) / 2 + 0.25, math.pi / 3)
    best = max(test_ratio(a_n, b_n, c, w) for c in np.linspace(-b_n, b_n, 21)
               for w in (0.02, 0.05, 0.1, 0.2, 0.4, 1.0))
    none2 = sobolev(m=2) is None
    ok['Z3'] = inside and outside and best <= float(CS) and best > float(CS) / 1e4 and none2
    say('      cone of height 1/2, aperture pi/3 inside every annulus of width >= 1: %s; height (b - a)/2 + 1/4 leaves '
        'it (control): %s; test functions exp(-((x1 - c)/w)^2): largest ratio %.4f <= C_S (floating point), above '
        'C_S/10^4 = %.5f (control: refuted): %s; m = 2: the cone integral diverges, no constant (control): %s' % (
            inside, outside, best, float(CS) / 1e4, best > float(CS) / 1e4, none2))

    rnd = random.Random(11)
    good = bad = 0
    for _ in range(400):
        c = {k: 10 ** rnd.uniform(-1, 2) for k in ('Cst', 'Cinf', 'Cdw', 'CN', 'CR', 'CD', 'Cc', 'C0', 'Ck', 'Cs',
                                                     'Capp')}
        c.update(C2=10 ** rnd.uniform(-1, 0.3), dtau=6.0, lam1=0.027, eps1=5e-4, eps2=10 ** rnd.uniform(-4, -1),
                 mc=10 ** rnd.uniform(-2, 0), ms=10 ** rnd.uniform(-2, 0))
        lam0, terms, M, C3 = lambda0(c)
        at = conditions(c, lam0 * (1 - 1e-9), M, C3)
        above = conditions(c, lam0 * (1 + 1e-6), M, C3)
        good += all(at.values()) and not all(above.values())
        c2 = dict(c)
        t2 = dict(terms)
        del t2['E-d']
        lam0b = min(t2.values())
        bad += not all(conditions(c, lam0b * (1 - 1e-9), M, C3).values())
    ok['Z4'] = good == 400 and bad > 0
    say('  Z4: on 400 random inputs the closed form meets every condition at lam0 and fails one at lam0 (1 + 1e-6): '
        '%d/400; control, the formula without its Step-7 term violates a condition on %d of them' % (good, bad))

    say('  Z5: lam0 = min{ lam1, eps1/(2 C_app), [min(eps1, eps2)/(4 C_inf M)]^(1/(K-3)), [1/(2 C_dw M)]^(1/(K-4)), '
        '1/(C3 C_N M^2), '
        '[m_c/(2 C_c C0)]^(1/(N-3)), (2 C_k)^(-1/(N-3)), m_s/C_s },  M = C3 (C_D + 1 + C_R) + 1,  C3 = C_st C2 '
        'exp(C2 (tau_end - tau0)) (1 + tau_end - tau0);  K = 6, N = 9')
    say('      certified at P*: lam1 <= %.6f, tau_end - tau0 <= %.6f, eps1 >= %.4e, C_S <= %.3f (inside C_inf, C_dw)' % (
        float(g['lam1'][1]), float(g['dtau'][1]), float(eps1), float(CS)))
    say('      not computed (each a finite expression in the profiles g_1..g_{N+1} and their derivatives on Omega x S^1,'
        ' '
        'which are not computed beyond stage 0): C2 (Steps 4-6), C_N (nonlinear), C_st (Step 2), C_R (E3), C_D (E4, '
        'through C0, C_c, C_k, m_c of Proposition 6.5), C_inf and C_dw (Step 1: C_S times profile bounds), eps2 (the '
        'extension g_ext), m_s and C_s (Lemma 6.3 (c)), C_app (sup |g_app - g0|/lam)')
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
