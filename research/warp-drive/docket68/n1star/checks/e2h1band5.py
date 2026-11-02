#!/usr/bin/env python3
"""e2h1band5.py -- E2-PILOT section 3i's H^1 constants on the certified band [3, 384] (D581).

Corollary E2.11 (section 3i) bounds ||u'||_I and the angular part from any valid bound B of ||chi_I R_l(sigma) chi_I||
("any valid bound for Y serves, whichever multiplier gave it"), with m', M' those of phi_*, which do not depend on sigma
or l: for real sigma, l >= 1,

    X <= (1 + (1 + 2 m' (M' + 2|sigma|) B)^(1/2)) / (2 m'),   (a - a_1) int_I psi |u|^2 <= K ||f||^2,
    K := 2 X + (M' + 2|sigma|) B,

and for l = 0 the same algebra with section 3g's multiplier (m0', M0') gives X_0 (e2h1_5 H4). Section 3j certifies B
for every l >= 0 on the band: ||chi_I R_l(sigma) chi_I|| <= 11.477 for 3 <= sigma <= 384 (D567, saved as
checks/e2trapband5_384.out), with the interval bounds at the printed points (checks/e2trapband5_384.out to sigma = 192,
checks/e2bandtop5.out and checks/e2bandtop5_24.out above). D528 and D567 left these constants "not redone".

  W1 (control, exact) the function reproduces e2h1_5's constants at sigma = 3: H1's Xb <= 224.5 from B_6 <= 19.214 and
     H4's X_0 <= 808.6 from B_0 <= 275.2, so the formulas and the multipliers are e2h1_5's.
  W2 (exact) on each printed interval of the band, [3, 3.05] at sigma = 3 (corrected D586, verifier 253: [2.95, 3] was
     printed) and [sigma - 1/20, sigma] after, with its certified B and |sigma| at most the interval's top: X (every l >=
     1), K, the angular bound A = max(l(l + 2) K/(a - a_1) for l >= 2, at most 8K/5 at l = 2; 3 B^2 at l = 1), X_0 (l =
     0) and the summed constant C^2 := max(X^2 + A, X_0^2), so that, over the orthogonal harmonics, ||d_r* u||_I^2 +
     sum_l l(l + 2) int_I psi |u_l|^2 <= C^2 ||f||^2 (the angular part unweighted at l = 1). It checks that every row's
     C^2 is X_0^2 (l = 0 sets it) and lies below W3's uniform bounds (D586: it passed whenever C > 0 before).
  W3 (exact) uniformly on the band: every quantity increases in |sigma| and in B, so B <= 11.477 gives, for every 3 <=
     sigma <= sigma_b, the closed-form bounds at sigma_b; at sigma_b = 384 they are the band's suprema.

Labels: certified (exact rationals, square roots and printed decimals rounded up exactly; the decimals were rounded
after a 40-digit division before D586, no printed value changing), given the cited certificates (e2certify5 C1-C3 and
e2lzero5 Z2-Z4 for the multipliers, section 3j for B). Real sigma only (Lemma E2.10's 4|sigma| for Im sigma > 0 is
not taken).

    python3 checks/e2h1band5.py
"""
import sys
from fractions import Fraction as Fr
from math import isqrt

MP, MM = Fr(5793, 10**6), Fr(102041, 10**5)          # phi_*: m' >= 0.005793, M' <= 1.02041 (e2certify5 C3)
M0P, M0M = Fr(2580, 10**6), Fr(3809, 10**4)          # l = 0: m0' >= 0.002580, M0' <= 0.3809 (e2lzero5 Z4)
SUP = Fr(11477, 1000)
# (sigma, B, top of the band's interval): B2's interval at the first printed point is [3, 3.05], the rest [sigma - 1/20, sigma]
# (checks/e2trapband5_384.out; verifier 253); every quantity increases in sigma, so it is taken at the interval's top
TOP = {3: Fr(61, 20)}
POINTS = [(3, "11.086"), (6, "5.8726"), (12, "3.7719"), (24, "2.3724"), (48, "1.5222"), (96, "0.99697"),
          (128, "0.83951"), (160, "0.73083"), (192, "0.66429"), (256, "0.56257"), (320, "0.49119"), (384, "0.43792")]


def sqrt_up(x, digits=12):
    """an upper bound of sqrt(x), x >= 0 rational, to 10^-digits"""
    s = 10**digits
    n = x.numerator * s * s
    q = isqrt(n // x.denominator)
    while Fr(q * q, s * s) < x:
        q += 1
    return Fr(q, s)


def xb(mp, mm, sig, b):
    return (1 + sqrt_up(1 + 2 * mp * (mm + 2 * sig) * b)) / (2 * mp)


def constants(sig, b):
    X = xb(MP, MM, sig, b)
    K = 2 * X + (MM + 2 * sig) * b
    A = max(Fr(8, 5) * K, 3 * b * b)
    X0 = xb(M0P, M0M, sig, b)
    C2 = max(X * X + A, X0 * X0)
    return X, K, A, X0, C2


def up(x, d=4):
    """x > 0 rounded up to d significant decimals, exactly (rational arithmetic), as a string"""
    e = 0
    while Fr(10)**e > x:
        e -= 1
    while Fr(10)**(e + 1) <= x:
        e += 1
    q = Fr(10)**(e - d + 1)
    n = -((-x) // q)                          # ceil(x / q)
    k = d - 1 - e
    if k <= 0:
        return str(int(n * q))
    s = str(int(n)).rjust(k + 1, '0')
    return (s[:-k] + '.' + s[-k:]).rstrip('0').rstrip('.')


def main():
    ok = {}
    X = xb(MP, MM, Fr(3), Fr(19214, 1000))
    X0 = xb(M0P, M0M, Fr(3), Fr(2752, 10))
    ok['W1'] = up(X, 4) == '224.5' and up(X0, 4) == '808.6'
    print('  W1 (control): at sigma = 3, e2h1_5 H1 from B_6 <= 19.214: Xb <= %s (H1: 224.5); H4 from B_0 <= 275.2: X_0 <= '
          '%s (H4: 808.6)' % (up(X, 4), up(X0, 4)))
    print('  W2: on each printed interval of the band (B certified there; [3, 3.05] at the first, [sigma - 1/20, sigma] after):')
    print('      interval          B        X (l>=1)   K          A          X_0        C')
    rows = []
    for s, bs in POINTS:
        b = Fr(bs)
        top = TOP.get(s, Fr(s))
        X, K, A, X0, C2 = constants(top, b)
        C = sqrt_up(C2)
        rows.append((s, X, K, A, X0, C, C2))
        lo = Fr(s) if s in TOP else Fr(s) - Fr(1, 20)
        print('      [%-7s %-7s]  %-8s %-10s %-10s %-10s %-10s %s' % (str(float(lo)) + ',', float(top), bs, up(X), up(K), up(A),
                                                                   up(X0), up(C)))
    Xs, Ks, As, X0s, C2s = constants(Fr(384), SUP)
    ok['W2'] = all(r[5] * r[5] >= r[6] and r[6] >= max(r[1]**2 + r[3], r[4]**2) and r[6] == r[4]**2 and r[1] <= Xs
                   and r[4] <= X0s for r in rows)
    print('      every row: C^2 = max(X^2 + A, X_0^2) = X_0^2 (set by l = 0), and below the uniform bounds of W3: %s; X from '
          '%s to %s, A from %s to %s over the rows (the least on [5.95, 6], not at an end)' % (ok['W2'], up(min(r[1] for r in rows)),
          up(max(r[1] for r in rows)), up(min(r[3] for r in rows)), up(max(r[3] for r in rows))))
    Cs = sqrt_up(C2s)
    mono = all(constants(Fr(s), SUP)[4] <= constants(Fr(t), SUP)[4] for s, t in zip(range(3, 384, 7), range(10, 391, 7)))
    ok['W3'] = mono
    print('  W3: uniformly on 3 <= sigma <= 384 with B <= 11.477: X <= %s, K <= %s, A <= %s, X_0 <= %s, C <= %s '
          '(a grid check of C^2 increasing in sigma: %s; that each is increasing in sigma and B is read off the closed '
          'forms, deduced)' % (up(Xs), up(Ks), up(As), up(X0s), up(Cs), mono))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
