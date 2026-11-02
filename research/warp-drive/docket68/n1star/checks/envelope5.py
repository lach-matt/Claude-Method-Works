#!/usr/bin/env python3
"""envelope5: a C_c^inf envelope for Theorem 1 at the paper's point, with certified bounds on every derivative to order
14 (CONSTANTS5.md, Round 2, item (i)).

Round 1 found the numerics' envelope sin^4(pi (v - 1/2)/3) only C^3 at its ends (lzeroconst5.py Z0), while Theorem 1
asks env in C_c^inf. Here

    env(v) := c beta(y),  y = (2 v - 4)/3,  beta(y) = exp(1 - 1/(1 - y^2)) on |y| < 1, 0 elsewhere,
    c := ((105/128) / ((3/2) int_{-1}^{1} beta^2))^(1/2),

so supp env = [1/2, 7/2] = [v_start, v_end], env is smooth, and int env^2 = 105/128 = int sin^8, exactly, by the
definition of c: mu_end = mu0 + (2/9) A^2 int env^2 = 227/192 is unchanged, and so is every certified leaf of round 1
(they depend on the envelope only through mu_end; lzeroconst5.py Z0). Labels: computed (interval arithmetic, mpmath.iv,
outward rounded; exact integers for the polynomials P_k); deduced (the tail argument, stated at E2).

  E1 (certified) int_{-1}^{1} beta^2 in an interval of relative width < 1e-6 (beta^2 is even and decreasing in |y|,
     so lower and upper Riemann sums at exact points bound it), hence c in a certified interval.
  E2 (certified; deduced tail) e_k := sup_v |env^(k)(v)| for k = 0..14. On |y| <= 1 - delta: Taylor arithmetic in
     interval coefficients (the k-th coefficient computed with y0 an interval encloses beta^(k)(xi)/k! for every xi in
     it), over 4000 cells. On 1 - delta <= |y| < 1, t = 1 - |y|: beta = e phi1(t) phi2(t), phi1 = exp(-1/(2t)),
     phi2 = exp(-1/(2(2 - t))) (1/(t(2 - t)) = (1/(2t) + 1/(2(2 - t)))); phi1^(j) = P_j(1/t) exp(-1/(2t)) with
     P_(j+1)(x) = x^2 (P_j(x)/2 - P_j'(x)) (exact integer-rational coefficients), and x^i e^(-x/2) decreases for
     x > 2i, so with delta <= 1/(4 K) the sup over t <= delta is at t = delta; phi2 by Taylor arithmetic on [0, delta];
     Leibniz.
  E3 (computed) smoothness at the ends: phi1^(j)(t) -> 0 as t -> 0+ for every j (the tail bound at delta/2^m decreases
     to 0), so every derivative of env vanishes at v_start and v_end.
  Controls (must fail, and do): C1 the polynomial bump (1 - y^2)^4, run through E3's end test, has a nonzero 4th
  derivative at y = 1 (C^3, not C^4, as round 1's sin^4); C2 the bound e_k / 2 is refuted for every k <= 14 by a
  sample point (so the bounds are within a factor 2 of the truth); C3 an envelope with int env^2 off 105/128 by 1e-4 is
  refuted by E1's interval.

    python3 checks/envelope5.py
"""
import math
import sys
import textwrap
from fractions import Fraction as Fr

import mpmath
from mpmath import iv

iv.prec = 80
mpmath.mp.prec = 80
KMAX = 14


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


# ---- truncated Taylor series with interval coefficients (also used by stage0bd5.py) ----
def ts_const(c, K=KMAX):
    return [iv.mpf(c)] + [iv.mpf(0)] * K


def ts_var(x0, K=KMAX):
    return [iv.mpf(x0), iv.mpf(1)] + [iv.mpf(0)] * (K - 1)


def ts_add(a, b):
    return [x + y for x, y in zip(a, b)]


def ts_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def ts_scale(a, c):
    return [x * c for x in a]


def ts_mul(a, b):
    K = len(a) - 1
    return [sum((a[j] * b[n - j] for j in range(n + 1)), iv.mpf(0)) for n in range(K + 1)]


def ts_recip(a):
    K = len(a) - 1
    if 0 in a[0]:
        raise ZeroDivisionError('series constant term contains 0')
    b = [1 / a[0]]
    for n in range(1, K + 1):
        b.append(-sum((a[j] * b[n - j] for j in range(1, n + 1)), iv.mpf(0)) / a[0])
    return b


def ts_exp(a):
    K = len(a) - 1
    e = [iv.exp(a[0])]
    for n in range(1, K + 1):
        e.append(sum((j * a[j] * e[n - j] for j in range(1, n + 1)), iv.mpf(0)) / n)
    return e


def ts_pow(a, p):
    """a^p, p a rational (Fraction); a[0] > 0"""
    K = len(a) - 1
    if not a[0].a > 0:
        raise ValueError('power of a series with non-positive constant term')
    pp = iv.mpf(p.numerator) / p.denominator
    b = [iv.exp(pp * iv.log(a[0]))]
    for n in range(1, K + 1):
        s = sum((((pp + 1) * j - n) * a[j] * b[n - j] for j in range(1, n + 1)), iv.mpf(0))
        b.append(s / (n * a[0]))
    return b


SAFE = 1 + mpmath.mpf(10) ** -15     # covers the rounding of the few mpf (not iv) products below


def lo_end(x):
    return mpmath.mpf(x._mpi_[0])


def hi_end(x):
    return mpmath.mpf(x._mpi_[1])


def ivmax_abs(x):
    """an upper bound of |y| over the interval x (exact endpoints)"""
    return max(abs(lo_end(x)), abs(hi_end(x)))


# ---- the bump ----
def beta_series(y0):
    """Taylor series of beta about y0 (an interval inside (-1, 1))"""
    u = ts_sub(ts_const(1), ts_mul(ts_var(y0), ts_var(y0)))
    return ts_scale(ts_exp(ts_scale(ts_recip(u), -1)), iv.e)


def Pk_list(K):
    """phi1^(j)(t) = P_j(1/t) exp(-1/(2t)): P_(j+1)(x) = x^2 (P_j(x)/2 - P_j'(x)); coefficient lists (exact)"""
    P = [[Fr(1)]]
    for _ in range(K):
        p = P[-1]
        dp = [i * p[i] for i in range(1, len(p))] + [Fr(0)]
        q = [Fr(0), Fr(0)] + [p[i] / 2 - dp[i] for i in range(len(p))]
        while len(q) > 1 and q[-1] == 0:
            q.pop()
        P.append(q)
    return P


def tail_phi1_bound(Pj, delta):
    """sup_{0 < t <= delta} |P_j(1/t) exp(-1/(2t))| <= sum |p_i| delta^-i e^(-1/(2 delta)), valid when
    1/delta >= 2 deg P_j (each x^i e^(-x/2) is then decreasing on x >= 1/delta)"""
    deg = len(Pj) - 1
    assert 1 / delta >= 2 * deg
    d = iv.mpf(delta)
    return sum((iv.mpf(abs(c.numerator)) / c.denominator * d ** (-i) for i, c in enumerate(Pj)),
               iv.mpf(0)) * iv.exp(-1 / (2 * d))


def end_bounds(delta, K=KMAX):
    """sup over 1 - delta <= |y| < 1 of |beta^(k)|, k = 0..K"""
    P = Pk_list(K)
    t1 = [tail_phi1_bound(P[j], delta) for j in range(K + 1)]
    # phi2(t) = exp(-1/(2(2 - t))) on t in [0, delta]: Taylor arithmetic with t0 the interval [0, delta]
    t0 = iv.mpf([0, delta])
    two_minus = ts_sub(ts_const(2), ts_var(t0))
    s2 = ts_exp(ts_scale(ts_recip(two_minus), iv.mpf(-1) / 2))
    t2 = [iv.mpf(ivmax_abs(s2[k]) * math.factorial(k) * SAFE) for k in range(K + 1)]
    out = []
    for k in range(K + 1):
        b = sum((math.comb(k, j) * t1[j] * t2[k - j] for j in range(k + 1)), iv.mpf(0)) * iv.e
        out.append(hi_end(b))
    return out


def interior_bounds(delta, cells=4000, K=KMAX):
    """sup over 0 <= y <= 1 - delta of |beta^(k)| (beta is even, |beta^(k)| is even), k = 0..K"""
    best = [mpmath.mpf(0)] * (K + 1)
    top = 1 - mpmath.mpf(delta)
    for i in range(cells):
        lo, hi = top * i / cells, top * (i + 1) / cells
        s = beta_series(iv.mpf([lo, hi]))
        for k in range(K + 1):
            v = ivmax_abs(s[k]) * math.factorial(k) * SAFE
            if v > best[k]:
                best[k] = v
    return best


def beta_sq_integral(N=2 ** 17):
    """int_{-1}^{1} beta^2 = 2 int_0^1 beta^2, beta^2 decreasing on [0, 1): lower sum at right ends, upper at left
    ends, each value enclosed by interval evaluation at exact rational points"""
    lo = iv.mpf(0)
    hi = iv.mpf(0)
    vals = []
    for i in range(N + 1):
        y = iv.mpf(i) / N
        if i == N:
            vals.append(iv.mpf(0))
        else:
            vals.append(iv.exp(2 - 2 / (1 - y * y)))
    for i in range(N):
        lo += vals[i + 1]
        hi += vals[i]
    return lo_end(2 * lo / N), hi_end(2 * hi / N)


def bump_poly_end_test():
    """control: (1 - y^2)^4 has derivatives 0, 0, 0, 0, nonzero at y = 1 (exact)"""
    p = [Fr(0)] * 9
    for k in range(5):
        p[2 * k] = Fr(math.comb(4, k) * (-1) ** k)
    ders = []
    q = p
    for d in range(6):
        ders.append(sum(q))                                    # value at y = 1
        q = [i * q[i] for i in range(1, len(q))] or [Fr(0)]
    return ders


def main():
    ok = {}
    delta = Fr(1, 4 * KMAX)
    lo, hi = beta_sq_integral()
    clo = mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * hi)) * (1 - mpmath.mpf(10) ** -20)
    chi_ = mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * lo)) * (1 + mpmath.mpf(10) ** -20)
    ok['E1'] = (hi - lo) / lo < 1e-5
    say('  E1: int_{-1}^{1} beta^2 in [%s, %s] (relative width %.1e); c in [%s, %s]; int env^2 = 105/128 and mu_end = '
        '227/192 exactly by the definition of c' % (mpmath.nstr(lo, 12), mpmath.nstr(hi, 12), float((hi - lo) / lo),
                                                     mpmath.nstr(clo, 12), mpmath.nstr(chi_, 12)))

    inner = interior_bounds(float(delta))
    tail = end_bounds(float(delta))
    bbeta = [max(inner[k], tail[k]) for k in range(KMAX + 1)]
    ek = [chi_ * (mpmath.mpf(2) / 3) ** k * bbeta[k] * SAFE for k in range(KMAX + 1)]
    ok['E2'] = all(tail[k] < inner[k] for k in range(KMAX + 1))
    say('  E2: delta = 1/%d; sup |beta^(k)|, k = 0..%d (certified): %s' % (
        4 * KMAX, KMAX, ', '.join(mpmath.nstr(b, 4) for b in bbeta)))
    say('      the tails (|y| >= 1 - delta) are below the interior maxima at every k: %s; e_k = sup |env^(k)| = c '
        '(2/3)^k sup|beta^(k)| <= %s' % (ok['E2'], ', '.join(mpmath.nstr(e, 4) for e in ek)))

    P = Pk_list(KMAX)
    shrink = [max(hi_end(tail_phi1_bound(P[j], float(delta) / 2 ** m)) for j in range(KMAX + 1)) for m in (0, 4, 8)]
    ok['E3'] = shrink[0] > shrink[1] > shrink[2] and shrink[2] < 1e-100
    say('  E3: max_j sup_{t <= delta/2^m} |phi1^(j)| at m = 0, 4, 8: %s: every derivative of env tends to 0 at the '
        'ends (smooth, compactly supported)' % ', '.join(mpmath.nstr(x, 3) for x in shrink))

    ders = bump_poly_end_test()
    ok['C1'] = ders[:4] == [0, 0, 0, 0] and ders[4] != 0
    say('  C1 (control): (1 - y^2)^4 at y = 1: derivatives 0..5 = %s: the end test fails at order 4' % [str(d) for d in ders])

    # C2: sample the true derivatives (mpmath.diff at 80 bits) on a grid of the interior; bound/2 refuted
    refuted = []
    for k in range(KMAX + 1):
        best = 0
        for i in range(1, 120):
            y = mpmath.mpf(i) / 120 * (1 - mpmath.mpf(1) / 30)
            val = abs(mpmath.diff(lambda yy: mpmath.exp(1 - 1 / (1 - yy * yy)), y, k))
            best = max(best, val)
        refuted.append(best > bbeta[k] / 2 and best <= bbeta[k])
    ok['C2'] = all(refuted)
    say('  C2 (control): for every k <= %d a sampled |beta^(k)(y)| lies in (bound/2, bound]: %s' % (KMAX, ok['C2']))
    off = Fr(105, 128) + Fr(1, 10 ** 4)
    c_off = mpmath.sqrt(mpmath.mpf(off.numerator) / off.denominator / (mpmath.mpf(3) / 2 * lo))
    ok['C3'] = not (clo <= c_off <= chi_)
    say('  C3 (control): an envelope normalised to int env^2 = 105/128 + 1e-4 has c = %s, outside E1\'s interval: %s'
        % (mpmath.nstr(c_off, 10), ok['C3']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1, ek


if __name__ == '__main__':
    sys.exit(main()[0])
