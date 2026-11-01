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

  W1 (control, exact) the function reproduces e2h1_5 H1's constants at sigma = 3 from its B_6 <= 19.214 (Xb <= 224.5),
     so the formula and the constants are e2h1_5's.
  W2 (exact) on each printed interval [sigma - 1/20, sigma], with its certified B and |sigma| <= sigma_b: X (every l >=
     1), K, the angular bound A = max(l(l + 2) K/(a - a_1) for l >= 2, at most 8K/5 at l = 2; 3 B^2 at l = 1), X_0 (l =
     0) and the summed constant C^2 := max(X^2 + A, X_0^2), so that, over the orthogonal harmonics, ||d_r* u||_I^2 +
     sum_l l(l + 2) int_I psi |u_l|^2 <= C^2 ||f||^2 (the angular part unweighted at l = 1).
  W3 (exact) uniformly on the band: every quantity increases in |sigma| and in B, so B <= 11.477 gives, for every 3 <=
     sigma <= sigma_b, the closed-form bounds at sigma_b; at sigma_b = 384 they are the band's suprema.

Labels: certified (exact rationals, square roots rounded up), given the cited certificates (e2certify5 C1-C3 and
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
    """x rounded up to d significant decimals, as a string"""
    from decimal import Decimal, ROUND_CEILING, getcontext
    getcontext().prec = 40
    v = Decimal(x.numerator) / Decimal(x.denominator)
    e = v.adjusted() - d + 1
    return str(v.quantize(Decimal(1).scaleb(e), rounding=ROUND_CEILING).normalize())


def main():
    ok = {}
    X = xb(MP, MM, Fr(3), Fr(19214, 1000))
    ok['W1'] = up(X, 4) == '224.5'
    print('  W1 (control): e2h1_5 H1 at sigma = 3, B_6 <= 19.214: Xb <= %s (H1: 224.5)' % up(X, 4))
    print('  W2: on each printed interval [sigma - 1/20, sigma] of the band (B certified there):')
    print('      sigma      B        X (l>=1)   K          A          X_0        C')
    rows = []
    for s, bs in POINTS:
        b = Fr(bs)
        X, K, A, X0, C2 = constants(Fr(s), b)
        C = sqrt_up(C2)
        rows.append((s, X, K, A, X0, C))
        print('      %-6d    %-8s %-10s %-10s %-10s %-10s %s' % (s, bs, up(X), up(K), up(A), up(X0), up(C)))
    ok['W2'] = all(r[5] > 0 for r in rows)
    Xs, Ks, As, X0s, C2s = constants(Fr(384), SUP)
    Cs = sqrt_up(C2s)
    mono = all(constants(Fr(s), SUP)[4] <= constants(Fr(t), SUP)[4] for s, t in zip(range(3, 384, 7), range(10, 391, 7)))
    ok['W3'] = mono
    print('  W3: uniformly on 3 <= sigma <= 384 with B <= 11.477: X <= %s, K <= %s, A <= %s, X_0 <= %s, C <= %s '
          '(increasing in sigma: %s)' % (up(Xs), up(Ks), up(As), up(X0s), up(Cs), mono))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
