#!/usr/bin/env python3
"""envelope5: a C_c^inf envelope for Theorem 1 at the paper's point, with certified bounds on every derivative to order
14 (CONSTANTS5.md, Round 2, item (i)).

Round 1 found the numerics' envelope sin^4(pi (v - 1/2)/3) only C^3 at its ends (lzeroconst5.py Z0), while Theorem 1
asks env in C_c^inf. Here

    env(v) := c beta(y),  y = (2 v - 4)/3,  beta(y) = cos^12(pi y/2) exp(-y^2/(1 - y^2)) on |y| < 1, 0 elsewhere,
    c := ((105/128) / ((3/2) int_{-1}^{1} beta^2))^(1/2),

so supp env = [1/2, 7/2] = [v_start, v_end], env is smooth, and int env^2 = 105/128 = int sin^8 exactly, by the
definition of c: mu_end = mu0 + (2/9) A^2 int env^2 = 227/192 is unchanged, and so is every certified leaf of round 1
(they depend on the envelope only through mu_end; lzeroconst5.py Z0). The factor cos^12 keeps the derivatives small to
order 14: the plain bump exp(1 - 1/(1 - y^2)), normalised the same way, has sup |env^(11)| about 3.29e18 (computed,
floating point, P0 below; round 2 printed 3.6e22 from a first run that no program reproduces, the verifier's nit),
this one about 4e10. Labels: computed (interval arithmetic, mpmath.iv, outward rounded; exact rationals for the
polynomials P_j); deduced (the tail argument at E2).

  E1 (certified) int_{-1}^{1} beta^2 in an interval of relative width < 1e-4 (beta^2 is even and decreasing in |y|,
     so lower and upper Riemann sums at exact points bound it), hence c in a certified interval.
  E2 (certified; deduced tail) e_k := sup_v |env^(k)(v)| for k = 0..14. On |y| <= 1 - delta: Taylor arithmetic with
     interval coefficients (the k-th coefficient computed with y0 an interval encloses beta^(k)(xi)/k! for every xi in
     it), in the centred form of interior_bounds over a graded cover. On 1 - delta <= |y| < 1, t = 1 - |y|: beta =
     e sin^12(pi t/2) phi1(t) phi2(t), phi1 = exp(-1/(2t)), phi2 =
     exp(-1/(2(2 - t))) (y^2/(1 - y^2) = 1/(t(2 - t)) - 1 and 1/(t(2 - t)) = 1/(2t) + 1/(2(2 - t))); phi1^(j) =
     P_j(1/t) exp(-1/(2t)) with P_(j+1)(x) = x^2 (P_j(x)/2 - P_j'(x)), and x^i e^(-x/2) decreases for x > 2i, so with
     delta <= 1/(4K) the sup over t <= delta is at t = delta; the analytic factor by Taylor arithmetic on [0, delta];
     Leibniz.
  E3 (computed) smoothness at the ends: the tail bound at delta/2^m decreases to 0, so every derivative of env
     vanishes at v_start and v_end.
  P0 (computed, floating point) the plain bump's e_11 on a grid refined near its peak (y ~ 0.9758).
  Controls (must fail, and do): C1 (Round 3, the verifier's m2: round 2's C1 tested a polynomial, not E3's procedure)
  E3's shrink test run with the tail bound's flat factor exp(-1/(2t)) removed fails (the bounds grow as delta -> 0);
  the polynomial bump (1 - y^2)^4 is still shown C^3, not C^4, as round 1's sin^4; C2 the bound / 2 is refuted for
  every k <= 14 by a sampled value (mpmath.diff), so the bounds are within a factor 2 of the truth; C3 an envelope with int env^2 off 105/128 by
  1e-4 is refuted by E1's interval.

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
MPOW = 12
DELTA = Fr(1, 150)
SAFE = 1 + mpmath.mpf(10) ** -15     # covers the rounding of the few mpf (not iv) products below


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def lo_end(x):
    return mpmath.mpf(x._mpi_[0])


def hi_end(x):
    return mpmath.mpf(x._mpi_[1])


def ivmax_abs(x):
    """an upper bound of |y| over the interval x (exact endpoints)"""
    return max(abs(lo_end(x)), abs(hi_end(x)))


# ---- truncated Taylor series with interval coefficients ----
def ts_const(c, K=KMAX):
    return [iv.mpf(c)] + [iv.mpf(0)] * K


def ts_var(x0, K=KMAX):
    return [iv.mpf(x0), iv.mpf(1)] + [iv.mpf(0)] * (K - 1)


def ts_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def ts_scale(a, c):
    return [x * c for x in a]


def ts_mul(a, b):
    K = len(a) - 1
    return [sum((a[j] * b[n - j] for j in range(n + 1)), iv.mpf(0)) for n in range(K + 1)]


def ts_ipow(a, m):
    out = ts_const(1, len(a) - 1)
    base = a
    while m:
        if m & 1:
            out = ts_mul(out, base)
        m >>= 1
        if m:
            base = ts_mul(base, base)
    return out


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


def ts_trig(x0, w, phase, K=KMAX):  # noqa: D401
    """Taylor series of sin(w (x0 + h) + phase) in h, x0 an interval: coefficients sin(w x0 + phase + k pi/2) w^k/k!"""
    return [iv.sin(w * x0 + phase + k * iv.pi / 2) * w ** k / math.factorial(k) for k in range(K + 1)]


# ---- the bump ----
def beta_series(y0, K=KMAX):
    """Taylor series of beta about y0 (an interval inside (-1, 1)), to order K"""
    u = ts_sub(ts_const(1, K), ts_mul(ts_var(y0, K), ts_var(y0, K)))
    gauss = ts_scale(ts_exp(ts_scale(ts_recip(u), -1)), iv.e)          # exp(1 - 1/(1 - y^2))
    cosp = ts_ipow(ts_trig(y0, iv.pi / 2, iv.pi / 2, K), MPOW)           # cos(pi y/2)^12
    return ts_mul(cosp, gauss)


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


def tail_phi1_bound(Pj, delta, flat=True):
    """sup_{0 < t <= delta} |P_j(1/t) exp(-1/(2t))| <= sum |p_i| delta^-i e^(-1/(2 delta)), valid when
    1/delta >= 2 deg P_j (each x^i e^(-x/2) is then decreasing on x >= 1/delta)"""
    deg = len(Pj) - 1
    assert 1 / delta >= 2 * deg
    d = iv.mpf(delta.numerator) / delta.denominator
    return sum((iv.mpf(abs(c.numerator)) / c.denominator * d ** (-i) for i, c in enumerate(Pj)),
               iv.mpf(0)) * (iv.exp(-1 / (2 * d)) if flat else 1)          # flat=False: control C1's mutant


def end_bounds(delta, K=KMAX):
    """sup over 1 - delta <= |y| < 1 of |beta^(k)|, k = 0..K"""
    P = Pk_list(K)
    t1 = [tail_phi1_bound(P[j], delta) for j in range(K + 1)]
    t0 = iv.mpf([0, iv.mpf(delta.numerator) / delta.denominator])
    two_minus = ts_sub(ts_const(2), ts_var(t0))
    phi2 = ts_exp(ts_scale(ts_recip(two_minus), iv.mpf(-1) / 2))
    sinp = ts_ipow(ts_trig(t0, iv.pi / 2, 0), MPOW)
    an = ts_mul(sinp, phi2)
    t2 = [iv.mpf(ivmax_abs(an[k]) * math.factorial(k) * SAFE) for k in range(K + 1)]
    out = []
    for k in range(K + 1):
        b = sum((math.comb(k, j) * t1[j] * t2[k - j] for j in range(k + 1)), iv.mpf(0)) * iv.e
        out.append(hi_end(b))
    return out


def interior_cells(delta):
    """a cover of [0, 1 - delta]: 1500 equal cells on [0, 9/10], then cells of width (1 - y)^2/20 up to 1 - delta (the
    scale on which 1/(1 - y^2) varies), so that the interval Taylor coefficients stay tight near the ends"""
    cells = [(mpmath.mpf(i) * 9 / 15000, mpmath.mpf(i + 1) * 9 / 15000) for i in range(1500)]
    y = mpmath.mpf(9) / 10
    top = 1 - mpmath.mpf(delta.numerator) / delta.denominator
    while y < top:
        y2 = min(top, y + (1 - y) ** 2 / 20)
        cells.append((y, y2))
        y = y2
    return cells


def interior_bounds(delta, K=KMAX, J=4):
    """sup over 0 <= y <= 1 - delta of |beta^(k)| (|beta^(k)| is even), k = 0..K, by the centred form: with m the
    cell's midpoint and h <= w/2 its half-width, beta^(k)(m + h) = sum_{j<J} beta^(k+j)(m) h^j/j! + beta^(k+J)(xi)
    h^J/J!, the first terms from the series at the point m (narrow intervals), the last from the series over the cell
    (wide, but multiplied by h^J). Plain interval evaluation over the cell loses the cancellation between the factors'
    large coefficients and overestimated the orders 11-14 by up to 1e4 in a first run."""
    best = [mpmath.mpf(0)] * (K + 1)
    for lo, hi in interior_cells(delta):
        mid = (lo + hi) / 2
        h = (hi - lo) / 2
        sm = beta_series(iv.mpf(mid), K + J)
        sc = beta_series(iv.mpf([lo, hi]), K + J)
        for k in range(K + 1):
            v = sum(ivmax_abs(sm[k + j]) * math.factorial(k + j) / math.factorial(j) * h ** j for j in range(J))
            v += ivmax_abs(sc[k + J]) * math.factorial(k + J) / math.factorial(J) * h ** J
            v *= SAFE
            if v > best[k]:
                best[k] = v
    return best


def beta_sq_integral(N=2 ** 17):
    """int_{-1}^{1} beta^2 = 2 int_0^1 beta^2, beta^2 decreasing on [0, 1): lower sum at right ends, upper at left
    ends, each value enclosed by interval evaluation at exact rational points"""
    vals = []
    for i in range(N + 1):
        y = iv.mpf(i) / N
        if i == N:
            vals.append(iv.mpf(0))
        else:
            vals.append(iv.cos(iv.pi * y / 2) ** (2 * MPOW) * iv.exp(2 - 2 / (1 - y * y)))
    lo = sum(vals[1:], iv.mpf(0))
    hi = sum(vals[:-1], iv.mpf(0))
    return lo_end(2 * lo / N), hi_end(2 * hi / N)


def bump_poly_end_test():
    """control: (1 - y^2)^4 has derivatives 0, 0, 0, 0, nonzero at y = 1 (exact)"""
    p = [Fr(0)] * 9
    for k in range(5):
        p[2 * k] = Fr(math.comb(4, k) * (-1) ** k)
    ders = []
    q = p
    for _ in range(6):
        ders.append(sum(q))                                    # value at y = 1
        q = [i * q[i] for i in range(1, len(q))] or [Fr(0)]
    return ders


def envelope_bounds():
    """(c_lo, c_hi, [e_0..e_14], int beta^2 interval, interior and tail sups of |beta^(k)|)"""
    lo, hi = beta_sq_integral()
    clo = mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * hi)) * (1 - mpmath.mpf(10) ** -20)
    chi_ = mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * lo)) * (1 + mpmath.mpf(10) ** -20)
    inner = interior_bounds(DELTA)
    tail = end_bounds(DELTA)
    bbeta = [max(inner[k], tail[k]) for k in range(KMAX + 1)]
    ek = [chi_ * (mpmath.mpf(2) / 3) ** k * bbeta[k] * SAFE for k in range(KMAX + 1)]
    return clo, chi_, ek, (lo, hi), inner, tail, bbeta


def main():
    ok = {}
    clo, chi_, ek, (lo, hi), inner, tail, bbeta = envelope_bounds()
    ok['E1'] = (hi - lo) / lo < mpmath.mpf(10) ** -4
    say('  E1: int_{-1}^{1} beta^2 in [%s, %s] (relative width %s); c in [%s, %s]; int env^2 = 105/128 and mu_end = '
        '227/192 exactly by the definition of c' % (mpmath.nstr(lo, 12), mpmath.nstr(hi, 12),
                                                     mpmath.nstr((hi - lo) / lo, 2), mpmath.nstr(clo, 12),
                                                     mpmath.nstr(chi_, 12)))
    ok['E2'] = all(tail[k] < inner[k] for k in range(KMAX + 1))
    say('  E2: delta = %s; sup |beta^(k)|, k = 0..%d (certified): %s' % (
        DELTA, KMAX, ', '.join(mpmath.nstr(b, 4) for b in bbeta)))
    say('      the tail bounds (|y| >= 1 - delta) lie below the interior maxima at every k: %s; e_k = sup |env^(k)| = '
        'c (2/3)^k sup|beta^(k)| <= %s' % (ok['E2'], ', '.join(mpmath.nstr(e, 4) for e in ek)))

    P = Pk_list(KMAX)

    def e3_test(flat):
        sh = [max(hi_end(tail_phi1_bound(P[j], DELTA / 2 ** m, flat)) for j in range(KMAX + 1)) for m in (0, 4, 8)]
        return sh, sh[0] > sh[1] > sh[2] and sh[2] < mpmath.mpf(10) ** -100

    shrink, ok['E3'] = e3_test(True)
    say('  E3: max_j sup_{t <= delta/2^m} |phi1^(j)| at m = 0, 4, 8: %s: every derivative of env tends to 0 at the '
        'ends (smooth, compactly supported)' % ', '.join(mpmath.nstr(x, 3) for x in shrink))

    shrink_m, e3_m = e3_test(False)
    ders = bump_poly_end_test()
    ok['C1'] = (not e3_m) and ders[:4] == [0, 0, 0, 0] and ders[4] != 0
    say('  C1 (control): E3 with the factor exp(-1/(2t)) removed: %s at m = 0, 4, 8: E3 fails for it: %s; '
        '(1 - y^2)^4 at y = 1: derivatives 0..5 = %s: C^3, not C^4' % (', '.join(mpmath.nstr(x, 3) for x in shrink_m),
                                                                      not e3_m, [str(d) for d in ders]))

    bp = lambda yy: mpmath.exp(1 - 1 / (1 - yy * yy))  # noqa: E731
    with mpmath.workdps(30):
        cb = mpmath.sqrt(mpmath.mpf(105) / 128 / (mpmath.mpf(3) / 2 * mpmath.quad(lambda yy: bp(yy) ** 2, [-1, 0, 1])))
        grid = [(abs(mpmath.diff(bp, mpmath.mpf(i) / 400, 11)), mpmath.mpf(i) / 400) for i in range(1, 400)]
        y0 = max(grid)[1]
        peak = max(abs(mpmath.diff(bp, y0 + mpmath.mpf(i) / 40000, 11)) for i in range(-200, 201)
                   if y0 + mpmath.mpf(i) / 40000 < 1)
        e11b = cb * (mpmath.mpf(2) / 3) ** 11 * peak
    ok['P0'] = mpmath.mpf('3.2e18') < e11b < mpmath.mpf('3.4e18')
    say('  P0 (computed, floating point): the plain bump exp(1 - 1/(1 - y^2)), normalised to int env^2 = 105/128: '
        'e_11 ~ %s near y = %s (round 2 printed 3.6e22, reproduced by no program)' % (mpmath.nstr(e11b, 4),
                                                                                      mpmath.nstr(y0, 4)))

    f = lambda yy: mpmath.cos(mpmath.pi * yy / 2) ** MPOW * mpmath.exp(-yy * yy / (1 - yy * yy))  # noqa: E731
    pts = [mpmath.mpf(i) / 60 * mpmath.mpf(9) / 10 for i in range(60)]
    pts += [1 - mpmath.mpf(10) ** (-1 - mpmath.mpf(i) / 50) for i in range(60)]     # 1 - y from 1e-1 to 1.6e-3
    refuted = []
    for k in range(KMAX + 1):
        best = max(abs(mpmath.diff(f, y, k)) for y in pts)
        refuted.append(bbeta[k] / 2 < best <= bbeta[k])
    ok['C2'] = all(refuted)
    say('  C2 (control): for every k <= %d a sampled |beta^(k)(y)| (mpmath.diff, 120 points) lies in (bound/2, '
        'bound]: %s %s' % (KMAX, ok['C2'], refuted))
    off = Fr(105, 128) + Fr(1, 10 ** 4)
    c_off = mpmath.sqrt(mpmath.mpf(off.numerator) / off.denominator / (mpmath.mpf(3) / 2 * lo))
    ok['C3'] = not (clo <= c_off <= chi_)
    say('  C3 (control): an envelope normalised to int env^2 = 105/128 + 1e-4 has c >= %s, outside E1\'s interval: %s'
        % (mpmath.nstr(c_off, 10), ok['C3']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
