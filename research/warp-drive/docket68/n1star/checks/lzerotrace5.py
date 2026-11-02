#!/usr/bin/env python3
"""lzerotrace5: Theorem 1's lambda0 at the paper's point, every factor traced to N1STAR-PROOF.md by line, and the
certified upper bound recomputed from the record's own definitions (CONSTANTS5.md, Round 3, item (i)).

lambda0 is the threshold of N1STAR-PROOF.md sections 0-6 (Theorem E with Theorem D): the minimum of nine terms
(CONSTANTS5.md 1.3 and R2.1 V-m4), each the smallness condition of one step. The point P* is round 1's (l5 = 1/10,
mu0 = 1, A = 1, T = 1, tau0 = -2, K = 6, N = 9, a = q0/2) with round 2's C_c^inf envelope (envelope5.py). Labels:
READ (a quoted fragment asserted on the cited line), deduced (an argument from the cited lines), certified (exact
rationals, square roots in certified rational bounds; mpmath.iv for the envelope constant), computed (floating point,
where said).

  T0 (READ, computed) N1STAR-PROOF.md lines 1-805 have the md5 round 2 pinned (lzeroaudit5.py A0), and every row of
     the trace table carries a fragment found verbatim on its cited line. The table covers the nine terms of the
     minimum and every factor of the two terms that are evaluated.
  T1 (certified) the domain at P*: q0^8 = 9/1250, a = delta0 = q0/2, lam1 := min(1, delta0)/10 = q0/20 (:177).
  T2 (certified, exact) Lemma 1.1 (e)'s eps1 (:159-162) is below lam_n := (3 + mu_end/r^2)/5 = 2591339/4309440 under
     every reading of |.|: at the outer-boundary point with r = 67/5 (in Omega, mu = mu_end) the Lorentzian metric
     g0 - lam_n n n^T, n = (1, -2 xhat)/5^(1/2) in ker d(v + tau), makes that boundary null. Its size is lam_n in the
     Euclidean operator and Frobenius norms (rank one), and lam_n/5 in the largest-entry norm at xhat = (1,1,1,1)/2.
  T3 (deduced, certified) the wave's size at one point of Omega. From lead5.py's definition of W_TT (lead5.py:8-10,
     wave() at :58-67), W_TT has only angular components and is diagonal in (th, phi1, phi2), so its eigenvalues for
     the Euclidean metric are W_thth/r^2, W_p1p1/(r c)^2, W_p2p2/(r s)^2 = -2(a1 + a2), 2 a1, 2 a2 (sympy, exact). At
     th = 0 (H = 1), phase 0, v = 2 (env = c) and r = a: -(2/3) K, (4/3) K, -(2/3) K, K = c a^(-3/2), so |W_TT| >=
     (4/3) c a^(-3/2) (operator and largest entry) and (24)^(1/2)/3 c a^(-3/2) (Frobenius), certified with c's lower
     end from envelope5.py's Riemann sums. Cross-check (floating point): stage0bd5.py's Cartesian form gives the same
     matrix there.
  T4 (deduced) every admissible C_app (|g_app - g0| <= C_app lam on Omega for 0 < lam <= lam0, the bound of (0.4)'s
     profiles that Step 3 (:355-357) uses) is at least sup |W_TT|: g1 = m1 + W(X, th + phi1(X)) with the g_j independent
     of lam (:541, (0.4) at :94-96); W_TT(s + pi) = -W_TT(s) and chi dv dv, m1 are even (sympy: the phase enters W_TT
     only through cos s, sin s, and chi only through 2s, lead5 L3-L4), so g1(X, s) - g1(X, s + pi) = 2 W_TT(X, s +
     phi1); and (g_app - g0)/lam -> g1(X, s0) along lam_j -> 0 with v/lam_j = s0 mod 2 pi.
  T5 (certified) the bound. Step 3 asks |g_app + w - g0| <= eps1 for every w the bootstrap allows, so the proof's
     lambda0 satisfies C_app lambda0 < eps1, whatever split between g_app and w is chosen; with :177, lambda0 <=
     min(lam1, eps1/C_app). Round 1's closed form (1.3) splits eps1 in halves, a choice the proof does not make (Step
     3 states no split), and gives eps1/(2 C_app). Both are printed for the three readings of |.|, which the proof does
     not define for arrays (it states the flat L^2 norm ||.|| of the arrays, :83, whose integrand is the Frobenius one).
  Controls (must fail, and do): C1 every trace row's line shifted by one: the fragments are not found; C2 the claim
  C_app >= 12.6 is refuted at the point: |W_TT| there is at most 12.60 - 0.003 (the certification cannot pass a false
  bound); C3 the parity argument on an even harmonic (cos 2s) gives a zero difference and no bound; C4 a point at r =
  a - 10^-6 is outside Omega (the domain test rejects it); C5 a direction not in ker d(v + tau) does not make the
  boundary null (the restricted form keeps a positive least eigenvalue).

    python3 checks/lzerotrace5.py
"""
import hashlib
import os
import sys
import textwrap
from fractions import Fraction as Fr

import mpmath
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lzeroconst5 as LZ  # noqa: E402  (round 1's certified geometry, imported, not copied)
import envelope5 as EV  # noqa: E402  (round 2's envelope: the Riemann sums that enclose c)

PROOF = os.path.join(HERE, '..', 'N1STAR-PROOF.md')
LEAD = os.path.join(HERE, '..', 'lead5.py')
PIN = '57d896ae1da4845f3c94c66d7b087a41'          # lzeroaudit5.py A0: md5 of lines 1-805 joined by newlines
LAST = 805

# the trace table: (term, factor, line, fragment found verbatim on that line, status)
CERT, OPEN = 'certified here', 'not evaluated'
TRACE = [
    ('lam1', 'lam1 := min(1, delta0)/10', 177, 'lam1 := min(1, delta0)/10', CERT),
    ('lam1', 'q0 = (sqrt72 mu0 l5^2)^(1/4)', 145, 'q0 := r_q(mu0) = (sqrt(72) mu0 l5^2)^(1/4)', CERT),
    ('lam1', 'a := q0 - delta0 (P*: delta0 = q0/2)', 146, 'Fix 0 < delta0 < q0, a := q0 - delta0', CERT),
    ('E-a', 'eps1 of Lemma 1.1 (e)', 160, 'is eps1 > 0 such that for every Lorentzian g with |g - g0| <= eps1', CERT),
    ('E-a', 'the lateral boundaries stay spacelike', 161, 'Sigma_tau and the two lateral boundaries stay spacelike',
     CERT),
    ('E-a', 'the outer boundary {v + tau - tau_end = V + 1}', 150, 'v + (tau - tau_end) <= V + 1', CERT),
    ('E-a', 'g = g_app + w must satisfy Lemma 1.1 (e)', 356, 'so for lam <= lam0(M) the metric g = g_app + w', CERT),
    ('E-a', 'g_app = g0 + lam [g1] + ... (0.4)', 94, 'g_app = g0 + lam [g1] + sum_{j=2}^{N} lam^j [g_j]', CERT),
    ('E-a', 'profiles bounded independently of lam', 96, 'bounded on Omega x S^1 independently of lam', CERT),
    ('E-a', '|g - g0| <= C lam (C_app)', 113, '|g - g0| <= C lam', CERT),
    ('E-a', 'g1 = m1 + W(X, th + phi1(X)), g_j independent of lam', 541,
     'profiles g_j(X, th) independent of lam with g1 = m1 + W(X, th + phi1(X))', CERT),
    ('E-a', 'W := W_TT + chi dv dv', 462, 'W := W_TT + chi dv dv', CERT),
    ('E-a', 'W_TT the record\'s wave (lead5.py)', 461, 'Let W_TT be the record\'s first-order wave', CERT),
    ('E-b', '|w| <= C lam^(-3) N (Step 1, C_inf)', 348, 'C lam^(-3-i) N for i <= 4', OPEN),
    ('E-b', '|w| <= eps2/2 (Step 8 (iii), eps2)', 427, 'agrees with the original where |w| <= eps2/2', OPEN),
    ('E-b', 'eps2 (Step 8 (iii))', 425, 'with eps2 so small that every metric within eps2 of', OPEN),
    ('E-c', '|d w| <= C M lam^(K-4) (C_dw), M1 independent of M', 356, '|d w| <= C M lam^(K-4) <= C M lam^2', OPEN),
    ('E-c', 'M1 independent of M', 357, '|d g| <= M1 with M1 independent of M', OPEN),
    ('E-d', 'C3 := C2 e^{C2 dtau} (1 + dtau) C', 400, 'C3 := C2 e^{C2 (tau_end - tau0)} (1 + tau_end - tau0) C', OPEN),
    ('E-d', 'M := C3 (C_D + 1 + C_R) + 1', 400, 'Take M := C3 (C_D + 1 + C_R) + 1', OPEN),
    ('E-d', 'C3 C M^2 lam0 <= 1 (C_N)', 401, 'small that C3 C M^2 lam0 <= 1 and Step 3 holds', OPEN),
    ('E-d', 'k = 6, K >= 6 (P*: K = 6)', 92, 'Fix k = 6 and K >= 6', CERT),
    ('D-a', 'frozen coefficients within their margin while ||U_i|| <= 2 C0 lam^(N-2)', 769,
     'so while ||U_i||_{X_s}', OPEN),
    ('D-b', 'contraction C lam^(N-3) (C_k)', 772, '<= C lam^(N-3) ||U_i - U_(i-1)||_{X_(s0)}', OPEN),
    ('D-c', 'alpha and S A0 keep their signs for lam small (m_s, C_s)', 692,
     'so alpha and S A0 keep their signs for lam small', OPEN),
    ('D-d', 'iterates stay in the ball of radius 2 C0 lam^(N-2) (C_b)', 771,
     'keeps the iterates in the ball of radius 2 C0 lam^(N-2)', OPEN),
    ('D-a', 'N := K + 3 (P*: N = 9)', 795, 'N := K + 3', CERT),
]
TERMS = ['lam1', 'E-a', 'E-b', 'E-c', 'E-d', 'D-a', 'D-b', 'D-c', 'D-d']
NEEDS = {
    'E-b': 'C_inf (Lemma 2.1 C_S, certified in round 1, times Step 1\'s constant), M, eps2 (g_ext): the profiles',
    'E-c': 'C_dw and M: Step 1\'s constant and the profiles g_1..g_10 to order about 11',
    'E-d': 'C2, C_st, C_N, C_R, C_D: Steps 2, 4-7 written with the profiles\' bounds (R2.2 (d)-(f))',
    'D-a': 'C0, C_c, m_c: Lemma 6.4\'s constant at s0 = 6, s = 8, and the stage data of Lemma 6.2',
    'D-b': 'C_k: the difference estimate of Lemma 6.4 at s0',
    'D-c': 'm_s, C_s: the O(lam) part of alpha and S A0 at the approximant\'s data (needs m_1)',
    'D-d': 'C_b, C0: the quadratic remainder Nl at the approximant\'s data',
}


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def sqrt_lo(x, S=10 ** 30):
    return LZ.root_iv(x, 2, S)[0]


def sqrt_hi(x, S=10 ** 30):
    return LZ.root_iv(x, 2, S)[1]


def mpf_fr(x):
    m, e = mpmath.mpf(x).man_exp
    return Fr(int(m)) * Fr(2) ** int(e)


def trace_check(lines, shift=0):
    bad = []
    for term, factor, ln, frag, _ in TRACE:
        i = ln - 1 + shift
        if not (0 <= i < len(lines)) or frag not in lines[i]:
            bad.append((term, ln + shift))
    return bad


def in_omega(tau, r, v, g):
    """exact interval test of Omega's three inequalities ((1.1), :150): True only if certain"""
    te_lo, te_hi = g['tau_end']
    return (tau >= LZ.TAU0 and tau <= te_lo and r >= g['a'][1] and v + (tau - te_lo) <= g['V'] + 1)


def eps1_perturbation(g, xhat, r=None):
    """g0 - lam n n^T at an outer boundary point (default the corner r = b(tau0), taken at the lower end of its
    certified interval, so tau >= tau0) with direction xhat (rational, |xhat| = 1): exact"""
    r = g['b0'][0] if r is None else r
    mu = g['mu_end']
    xh = [Fr(c) for c in xhat]
    assert sum(c * c for c in xh) == 1
    # the outer boundary: v + tau - tau_end = V + 1, v = tau + r, so tau = (V + 1 + tau_end - r)/2 (an interval)
    tau_lo = (g['V'] + 1 + g['tau_end'][0] - r) / 2
    tau_hi = (g['V'] + 1 + g['tau_end'][1] - r) / 2
    inside = tau_lo >= LZ.TAU0 and tau_hi <= g['tau_end'][0] and tau_lo + r >= LZ.VE   # v > v_end: mu = mu_end
    U = sp.Matrix([1] + [sp.Rational(c.numerator, c.denominator) for c in xh])          # dv = dtau + xhat.dx
    eta = sp.diag(-1, 1, 1, 1, 1)
    g0 = eta + sp.Rational(mu.numerator, mu.denominator) / sp.Rational(r.numerator, r.denominator) ** 2 * U * U.T
    nvec = sp.Matrix([1] + [-2 * sp.Rational(c.numerator, c.denominator) for c in xh])   # unnormalised (1, -2 xhat)
    nn = (nvec.T * nvec)[0]                                                               # = 5
    dvt = sp.Matrix([2] + [sp.Rational(c.numerator, c.denominator) for c in xh])         # d(v + tau) covector
    in_ker = (dvt.T * nvec)[0] == 0
    lam_n = (nvec.T * g0 * nvec)[0] / nn
    gp = g0 - lam_n * nvec * nvec.T / nn
    null_dir = (nvec.T * gp * nvec)[0] == 0
    # Lorentzian along g0 - t n n^T, t in [0, lam_n]: det = det g0 (1 - t n^T g0^-1 n / |n|^2), linear in t
    q = (nvec.T * g0.inv() * nvec)[0] / nn
    lorentz = g0.det() < 0 and (1 - lam_n * q) > 0
    op = lam_n                                          # rank one, unit n: operator norm = Frobenius norm = lam_n
    frob = sp.sqrt(sum(e ** 2 for e in (lam_n * nvec * nvec.T / nn)))
    mx = max(abs(e) for e in (lam_n * nvec * nvec.T / nn))
    return dict(inside=inside, in_ker=in_ker, lam_n=lam_n, null_dir=null_dir, lorentz=lorentz, op=op, frob=frob,
                maxe=mx, det=gp.det())


def norm_proposal():
    """the pointwise norm Lemma 1.1 (e) needs (exact, sympy, m = mu/r^2 symbolic; xhat = e1 by O(4) invariance):
    least eigenvalues of (g0 - eps I) on ker dtau, ker dr, ker d(v + tau), and the signature of g0 - eps I"""
    m, e = sp.symbols('m eps', nonnegative=True)
    U = sp.Matrix([1, 1, 0, 0, 0])
    g0 = sp.diag(-1, 1, 1, 1, 1) + m * U * U.T
    out = {}
    for name, cov in (('ker dtau', [1, 0, 0, 0, 0]), ('ker dr', [0, 1, 0, 0, 0]), ('ker d(v + tau)', [2, 1, 0, 0, 0])):
        B = sp.Matrix([cov]).nullspace()
        Q, _ = sp.Matrix.hstack(*B).QRdecomposition()
        Gr = sp.simplify(Q.T * (g0 - e * sp.eye(5)) * Q)
        out[name] = sorted(set(sp.simplify(x) for x in Gr.eigenvals()), key=str)
    full = [sp.simplify(x) for x in (g0 - e * sp.eye(5)).eigenvals()]
    return out, full, m, e


def restricted_least(xhat, mu, r, vec):
    """least eigenvalue of (g0 - lam w w^T) restricted to ker d(v + tau) (floating; control C5)"""
    import numpy as np
    xh = np.array(xhat, float)
    U = np.concatenate([[1.0], xh])
    g0 = np.diag([-1.0, 1, 1, 1, 1]) + (mu / r ** 2) * np.outer(U, U)
    w = np.array(vec, float) / np.linalg.norm(vec)
    lam = (3 + mu / r ** 2) / 5
    gp = g0 - lam * np.outer(w, w)
    d = np.concatenate([[2.0], xh])
    _, _, vt = np.linalg.svd(d.reshape(1, 5))
    B = vt[1:].T
    return float(min(np.linalg.eigvalsh(B.T @ gp @ B)))


def wtt_symbolic():
    """lead5.py's W_TT (READ :8-10, :58-67): eigenvalues for the Euclidean metric, and the parity in the phase"""
    r, th, s, A, E, H = sp.symbols('r th s A E H', positive=True)
    C, S = sp.cos(th), sp.sin(th)
    y3 = r ** sp.Rational(-3, 2)
    a1 = A * E * H * y3 * (2 * C ** 2 * sp.cos(s) - S ** 2 * sp.sin(s)) / 3
    a2 = A * E * H * y3 * (2 * S ** 2 * sp.sin(s) - C ** 2 * sp.cos(s)) / 3
    Wd = [-2 * r ** 2 * (a1 + a2), 2 * r ** 2 * C ** 2 * a1, 2 * r ** 2 * S ** 2 * a2]
    gd = [r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2]               # the Euclidean metric on (th, phi1, phi2)
    eig = [sp.simplify(w / gg) for w, gg in zip(Wd, gd)]
    ok_eig = all(sp.simplify(e - t) == 0 for e, t in zip(eig, [-2 * (a1 + a2), 2 * a1, 2 * a2]))
    odd = all(sp.simplify(e.subs(s, s + sp.pi) + e) == 0 for e in eig)
    at0 = [sp.simplify(e.subs({th: 0, s: 0, H: 1, A: 1})) for e in eig]
    even_ctrl = sp.simplify(sp.cos(2 * (s + sp.pi)) - sp.cos(2 * s)) == 0      # control C3: an even harmonic
    return ok_eig, odd, at0, even_ctrl, (r, E)


def main():
    ok = {}
    with open(PROOF) as fh:
        all_lines = fh.read().split('\n')
    lines = all_lines[:LAST]
    md5 = hashlib.md5('\n'.join(lines).encode()).hexdigest()
    bad = trace_check(all_lines)
    terms_seen = {t for t, *_ in TRACE}
    ok['T0'] = md5 == PIN and not bad and terms_seen == set(TERMS)
    say('lzerotrace5: lambda0 at P*, every factor traced, the bound certified')
    say('  T0: md5 of N1STAR-PROOF.md lines 1-%d = %s (pinned %s); %d trace rows, every fragment on its line: %s; the '
        'nine terms covered: %s' % (LAST, md5, PIN, len(TRACE), not bad, terms_seen == set(TERMS)))
    for term in TERMS:
        rows = [x for x in TRACE if x[0] == term]
        say('      %-5s %s' % (term, '; '.join('%s (N1STAR-PROOF.md:%d, %s)' % (f, ln, st)
                                               for _, f, ln, _, st in rows)))
        if term in NEEDS:
            say('            to evaluate: %s' % NEEDS[term])

    # T1 the domain
    g = LZ.geometry()
    q0lo, q0hi = g['q0']
    alo, ahi = g['a']
    lam1 = g['lam1']
    ok['T1'] = q0lo ** 8 <= Fr(9, 1250) <= q0hi ** 8 and lam1 == (q0lo / 20, q0hi / 20) and alo == q0lo / 2
    say('  T1: q0 in [%.12f, %.12f] (q0^8 = 9/1250), a = delta0 = q0/2 in [%.12f, %.12f], lam1 = q0/20 in [%.12f, '
        '%.12f] (certified)' % (q0lo, q0hi, alo, ahi, lam1[0], lam1[1]))

    # T2 eps1
    p_op = eps1_perturbation(g, (1, 0, 0, 0))
    p_mx = eps1_perturbation(g, (Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2)))
    lam_n = Fr(int(sp.fraction(p_op['lam_n'])[0]), int(sp.fraction(p_op['lam_n'])[1]))
    eps_op = lam_n
    eps_mx = Fr(int(sp.fraction(p_mx['maxe'])[0]), int(sp.fraction(p_mx['maxe'])[1]))
    p67 = eps1_perturbation(g, (1, 0, 0, 0), Fr(67, 5))
    lam_67 = Fr(int(sp.fraction(p67['lam_n'])[0]), int(sp.fraction(p67['lam_n'])[1]))
    ok['T2'] = (all(p[k] for p in (p_op, p_mx, p67) for k in ('inside', 'in_ker', 'null_dir', 'lorentz'))
                and lam_67 == Fr(2591339, 4309440) and lam_n < Fr(60131, 10 ** 5) and p_op['frob'] == p_op['op']
                and eps_mx == lam_n / 5)
    say('  T2: the corner of the outer boundary, r = b(tau0) (lower end of its interval, %.9f; tau = tau0), in Omega '
        'with mu = mu_end: %s; n in ker d(v + tau): %s; g0 - lam_n n n^T Lorentzian (det %.6f) with n null on the '
        'boundary: %s; lam_n = (3 + mu_end/r^2)/5 = %.7f (exact rational; round 2\'s r = 67/5 gave %.7f); size of the '
        'perturbation: operator = Frobenius = %.7f, largest entry %.7f at xhat = (1,1,1,1)/2 (%.7f at xhat = e1). So '
        'eps1 < %.7f (operator, Frobenius) and eps1 < %.7f (largest entry) (exact)'
        % (float(g['b0'][0]), p_op['inside'], p_op['in_ker'], float(p_op['det']), p_op['null_dir'], float(lam_n),
           float(lam_67), float(eps_op), float(eps_mx), float(p_op['maxe']), float(eps_op), float(eps_mx)))

    # T3 the wave at (v, th, s, r) = (2, 0, 0, a)
    ok_eig, odd, at0, even_ctrl, _ = wtt_symbolic()
    ratios = [sp.nsimplify(sp.simplify(e * sp.Symbol('r', positive=True) ** sp.Rational(3, 2) /
                                       sp.Symbol('E', positive=True))) for e in at0]
    lo_sum, hi_sum = EV.beta_sq_integral(2 ** 16)
    c_lo = mpf_fr(mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * hi_sum)) * (1 - mpmath.mpf(10) ** -20))
    c_hi = mpf_fr(mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * lo_sum)) * (1 + mpmath.mpf(10) ** -20))
    # a^(-3/2) >= 1/sqrt(a_hi^3); the point r = a lies in Omega (|x| >= a), tau = 2 - a, v = 2
    am32_lo = 1 / sqrt_hi(ahi ** 3)
    am32_hi = 1 / sqrt_lo(alo ** 3)
    K_lo, K_hi = c_lo * am32_lo, c_hi * am32_hi
    w_op_lo, w_op_hi = Fr(4, 3) * K_lo, Fr(4, 3) * K_hi
    w_fr_lo = sqrt_lo(Fr(24, 9)) * K_lo
    tau_p = 2 - ahi
    dom = (tau_p >= LZ.TAU0 and 2 - alo <= g['tau_end'][0] and 2 + (2 - alo - g['tau_end'][0]) <= g['V'] + 1)
    # floating cross-check against round 2's Cartesian form
    import numpy as np
    import stage0bd5 as SB
    rp = float(ahi)
    Wc = SB.cart_form([2 - rp, rp, 0.0, 0.0, 0.0], 0.0, 'TT') * float(c_lo)
    cross = np.allclose(np.diag(Wc), np.array([0, 0, 4, -2, -2]) * float(c_lo) * rp ** -1.5 / 3, rtol=1e-12)
    ok['T3'] = (ok_eig and ratios == [-sp.Rational(2, 3), sp.Rational(4, 3), -sp.Rational(2, 3)] and dom and cross
                and w_op_lo > 12)
    say('  T3: eigenvalues of W_TT (Euclidean) = (-2(a1 + a2), 2 a1, 2 a2) from lead5.py\'s definition: %s; at th = 0, '
        'phase 0: %s x env(v) r^(-3/2); the point (v, r) = (2, a), tau = 2 - a, lies in Omega: %s; c in [%.10f, '
        '%.10f] (envelope5 sums at 2^16 cells); |W_TT| there: operator and largest entry in [%.6f, %.6f], Frobenius >= '
        '%.6f (certified); Cartesian cross-check (floating point): %s'
        % (ok_eig, [str(x) for x in ratios], dom, float(c_lo), float(c_hi), float(w_op_lo), float(w_op_hi),
           float(w_fr_lo), cross))

    # T4 the parity argument
    ok['T4'] = odd
    say('  T4: W_TT(s + pi) = -W_TT(s) in every eigenvalue (sympy): %s; chi dv dv and m1 even (chi in the second '
        'harmonic, lead5 L3-L4; m1 the mean), so g1(s) - g1(s + pi) = 2 W_TT(s + phi1) and every admissible C_app >= '
        'sup |W_TT| (deduced)' % odd)

    # T5 the bound
    out = {}
    for name, eps1, capp in (('operator', eps_op, w_op_lo), ('Frobenius', eps_op, w_fr_lo),
                             ('largest entry', eps_mx, w_op_lo)):
        e_a = eps1 / capp
        out[name] = (min(lam1[1], e_a), e_a, min(lam1[1], e_a / 2))
    split_free = max(v[0] for v in out.values())
    halves = max(v[2] for v in out.values())
    ok['T5'] = (split_free == lam1[1] and out['largest entry'][0] < Fr(96, 10000)
                and out['operator'][2] < Fr(239, 10 ** 4) and out['operator'][1] < Fr(478, 10 ** 4))
    say('  T5: lambda0 <= min(lam1, eps1/C_app) (split-free, Step 3) and <= min(lam1, eps1/(2 C_app)) (round 1\'s '
        'halves), certified upper ends:')
    for name, (sf, ea, hv) in out.items():
        say('      |.| = %-13s eps1/C_app <= %.6f; lambda0 <= %.6f (split-free); <= %.6f (halves)' % (
            name, float(ea), float(sf), float(hv)))
    say('      every reading: lambda0 <= %.6f = lam1 at a = q0/2 (certified); round 2\'s 0.0239 holds with the halves '
        '(operator norm: %.6f), not split-free' % (float(split_free), float(out['operator'][2])))

    # T6 the pointwise norm the supplement should state
    eigs, full, m, e = norm_proposal()
    at = {name: [sp.simplify(x.subs(e, sp.Rational(3, 5))) for x in v] for name, v in eigs.items()}
    neg = [x for x in full if sp.simplify(x.subs(e, sp.Rational(3, 5)).subs(m, 0)) < 0]
    sig_ok = all(sp.simplify(x.subs(e, sp.Rational(3, 5))).subs(m, mv) != 0 for x in full for mv in (0, 1, 10))
    one_neg = all(sum(1 for x in full if float(x.subs({e: sp.Rational(3, 5), m: mv})) < 0) == 1
                  for mv in (0, Fr(1, 100), 1, 13, 1000))
    m_a_lo = LZ.MU0 / ahi ** 2                         # mu/a^2 >= mu0/a^2 on {r = a}
    least_dr = min(Fr(1), m_a_lo - 1) - Fr(3, 5)
    ok['T6'] = (sp.Rational(2, 5) in at['ker dtau'] and least_dr == Fr(2, 5) and one_neg
                and any(sp.simplify(x - m / 5) == 0 for x in at['ker d(v + tau)']) and eps_op > Fr(3, 5)
                and eps_mx > Fr(3, 25))
    say('  T6 (proposed definition, checked): |A| := the Euclidean operator norm of the array of Cartesian components '
        '(for symmetric A, its largest absolute eigenvalue). For |g - g0| <= eps, g >= g0 - eps I as forms, so each '
        'hypersurface stays spacelike if (g0 - eps I) is positive definite on its kernel; at eps = 3/5 (m = mu/r^2) the '
        'restricted eigenvalues are %s on ker dtau, %s on ker dr (least %s at r = a, P*), %s on ker d(v + tau) '
        '(least m/5 > 0) (exact); g0 - (3/5) I has exactly one negative eigenvalue for every m >= 0: %s, so its '
        'causal set is a double cone of two convex halves on which dtau, dr (at r = a) and d(v + tau) keep their '
        'signs, which gives the causal containment and the transversality (deduced). So Lemma 1.1 (e) holds with '
        'eps1 = 3/5 and fails above %.7f (T2): eps1* in [3/5, %.7f]. The Frobenius norm dominates it (same eps1); '
        'the largest-entry norm satisfies |A|_op <= 5 |A|_max, so there eps1* in [3/25, %.7f]'
        % ([str(x) for x in at['ker dtau']], [str(x) for x in at['ker dr']], least_dr,
           [str(x) for x in at['ker d(v + tau)']], one_neg, float(eps_op), float(eps_op), float(eps_mx)))

    # controls
    bad1 = trace_check(all_lines, shift=1)
    ok['C1'] = len(bad1) >= len(TRACE) - 1
    say('  C1 (control): every trace line shifted by one: %d of %d fragments not found' % (len(bad1), len(TRACE)))
    ok['C2'] = w_op_hi < Fr(126, 10) - Fr(3, 1000)
    say('  C2 (control): "C_app >= 12.6 at this point" refuted: |W_TT|_op there <= %.6f < 12.6' % float(w_op_hi))
    ok['C3'] = even_ctrl
    say('  C3 (control): an even harmonic, cos 2s: g(s) - g(s + pi) = 0, so the parity argument gives no bound: %s'
        % even_ctrl)
    bad_r = alo - Fr(1, 10 ** 6)
    ok['C4'] = not in_omega(2 - bad_r, bad_r, Fr(2), g)
    say('  C4 (control): the point r = a - 1e-6 is rejected by the domain test: %s' % ok['C4'])
    lm = restricted_least((1, 0, 0, 0), float(g['mu_end']), 13.4, (1, 2, 0, 0, 0))
    ln = restricted_least((1, 0, 0, 0), float(g['mu_end']), 13.4, (1, -2, 0, 0, 0))
    ok['C5'] = lm > 1e-3 and abs(ln) < 1e-12
    say('  C5 (control): least eigenvalue on ker d(v + tau) after the same-size perturbation along (1, 2 xhat), not in '
        'the kernel: %.4f > 0 (floating point); along (1, -2 xhat): %.1e' % (lm, ln))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
