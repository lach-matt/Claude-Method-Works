#!/usr/bin/env python3
"""r2-ch14n — computable batch for the §23.10-§23.11.2 section read (main member L6434-L6548).

Chat 97.  Imports heading_line / section_span / has_token / enclosing from r2lib by path;
nothing is copied.  Prints no wall-clock time.  Rounding is Decimal.quantize ROUND_HALF_UP,
never round(); exact rationals are converted numerator/denominator.
"""
import importlib.util, sys
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP

_s = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
section_span = r2lib.section_span

MAIN = open('/home/claude/members/The_Method_1_6-2.md', encoding='utf-8').read().split('\n')

R = F(10973731568, 100000)          # 109737.31568, the only Rydberg constant either bundle prints


def q(x, places):
    """Decimal.quantize ROUND_HALF_UP on an exact Fraction, converted numerator/denominator."""
    if isinstance(x, F):
        d = Decimal(x.numerator) / Decimal(x.denominator)
    else:
        d = Decimal(repr(x))
    return d.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def T(nu, Z=1):
    return F(Z * Z) * R / F(nu) ** 2


def deriv(nu, j, Z=1):
    """j-th derivative of Z^2 R nu^-2:  (-1)^j (j+1)! Z^2 R nu^-(2+j), exact."""
    fact = 1
    for t in range(1, j + 2):
        fact *= t
    return F((-1) ** j * fact) * F(Z * Z) * R / F(nu) ** (2 + j)


def lagrange_at(nodes, x):
    """Exact interpolant of T through `nodes`, evaluated at x."""
    tot = F(0)
    for i, xi in enumerate(nodes):
        term = T(xi)
        for j, xj in enumerate(nodes):
            if i != j:
                term *= F(x - xj, xi - xj)
        tot += term
    return tot


def nodes_for(n, k, m):
    """k+1 nodes adjacent to n: m above, k+1-m below.  n itself is never a node."""
    up = [n + t for t in range(1, m + 1)]
    dn = [n - t for t in range(1, k + 2 - m)]
    return sorted(dn + up)


print('== 23.10.1 the sign rule and the deductive bracket (L6439-L6450) ==')

bad = [(j, nu) for j in range(0, 7) for nu in (8, 40, 119)
       if (deriv(nu, j) > 0) != (((-1) ** j) > 0)]
print('  14n-01  L6439 "every derivative has known sign, sign(f^(j)) = (-1)^j" for T = Z^2R/nu^2 —',
      'EXACT at j = 0..6, nu = 8, 40, 119, %d exceptions' % len(bad), '(OK)' if not bad else '(FAIL)')

# the sign rule of L6443, tested as containment, exactly, over the printed sweep
lo_hi, fails, tested = {}, [], 0
for k in range(1, 6):
    for nu in range(8, 120):
        got = {}
        for m in range(0, k + 2):
            if nu - (k + 1 - m) < 1:
                continue
            p = lagrange_at(nodes_for(nu, k, m), nu)
            par = (k + 1 + m) % 2
            got.setdefault(par, []).append((m, p))
        if 0 not in got or 1 not in got:
            fails.append((k, nu, 'no two-sided choice of m'))
            continue
        tested += 1
        low = max(p for _, p in got[0])           # k+1+m even -> p is a lower bound
        high = min(p for _, p in got[1])          # odd -> an upper bound
        if not (low <= T(nu) <= high):
            fails.append((k, nu, 'containment'))
        if nu == 40:
            lo_hi[k] = (low, high)
print('  14n-02  L6446-L6448 "Tested on nu = 8...119 and k = 1...5: 560 containments, zero failures" —',
      'MEASURED %d target-order pairs, %d containments, %d failures' % (112 * 5, tested, len(fails)))
print('          arithmetic of the count: (119 - 8 + 1) x 5 = %d' % ((119 - 8 + 1) * 5),
      '| every choice of m obeying the parity rule bounds on the stated side: %d exceptions' % len(fails))

print()
print('== 23.10.1 / 23.10.3 the two printed widths at nu = 40 (L6450, L6491-L6493) ==')

w1 = lo_hi[1][1] - lo_hi[1][0]
w5 = lo_hi[5][1] - lo_hi[5][0]
print('  14n-03  printed width order 1 = 0.362, order 5 = 8.9e-6 (both sites, L6450 and L6491 agree)')
print('          bracket width from the section\'s own sign rule, nearest nodes: order 1 = %s, order 5 = %s'
      % (q(w1, 4), q(w5, 8)))

err1 = -deriv(40, 2) / F(2)                       # |f''|/2! x |(40-39)(40-41)| = 3R/nu^4
print('  14n-04  L6492 "tolerates a displacement of 0.129 cm-1" (order 1) — classical order-1',
      'interpolation error 3R/nu^4 at nu = 40 = %s -> %s  REPRODUCES' % (q(err1, 6), q(err1, 3)))

f6 = deriv(40, 6)
prod = F(3 * 2 * 1 * 1 * 2 * 3)
e5 = abs(f6) / F(720) * prod
lo6 = abs(deriv(43, 6)) / F(720) * prod
hi6 = abs(deriv(37, 6)) / F(720) * prod
print('  14n-05  L6492 "4.3e-6" (order 5) — classical order-5 term |f^(6)(xi)|/6! x 36 at nu = 40:',
      'xi = 40 gives %.4e; over the node span xi in [37, 43] it runs %.4e to %.4e (printed 4.3e-6 lies inside)'
      % (float(e5), float(lo6), float(hi6)))

for lab, num, den in (('order 1', w1, err1), ('order 5', w5, e5)):
    print('          width / displacement, %s: %s' % (lab, q(num / den, 4)))

print('  14n-06  L6493 "cells from a 10-member channel: 8 / 4" — a two-sided bracket at order k needs',
      'k+1 nodes off the target: 10 - 2 = %d at order 1, 10 - 6 = %d at order 5  REPRODUCES' % (10 - 2, 10 - 6))

print()
print('== 23.10.2 the V table and its caption (L6459-L6465, L6481-L6483) ==')

VT = {20: [157, 495, 1212, 2582, 3629],
      40: [673, 4037, 2.2e4, 8.5e4, 3.2e6],
      80: [2785, 3.2e4, 3.7e5, None, None]}
mono_k = all(all(r[i] < r[i + 1] for i in range(len(r) - 1) if r[i + 1] is not None)
             for r in VT.values())
cols = [[VT[n][i] for n in (20, 40, 80) if VT[n][i] is not None] for i in range(5)]
mono_nu = all(all(c[i] < c[i + 1] for i in range(len(c) - 1)) for c in cols)
flat = [v for r in VT.values() for v in r if v is not None]
print('  14n-07  L6467 "V grows with order, and steeply" — monotone in k across every printed row:', mono_k)
print('          also monotone in nu at fixed k (not claimed, measured):', mono_nu)
print('  14n-08  L6481 caption "from 157 to 3.2 x 10^6" — table min = %g, table max = %g  REPRODUCES'
      % (min(flat), max(flat)))
print('          ratio max/min = %s; the caption\'s two endpoints sit in different rows (nu = 20 k = 1, nu = 40 k = 5)'
      % q(max(flat) / min(flat), 1))

print()
print('== 23.10.4 the admissibility table (L6503-L6517) ==')

rows = [(1, 499, 499, 19, F(2596, 100)), (3, 187, 187, 101, F(715, 1000)), (6, 34, 34, 145, F(164, 10000))]
print('  14n-09  L6514 "the refusals rise from 3.7% to 81%" — refused/(admitted+refused):',
      ', '.join('order %d = %s%%' % (k, q(F(r, a + r) * 100, 1)) for k, a, _h, r, _m in rows))
tighten = rows[0][4] / rows[2][4]
print('  14n-10  L6514 "the bound tightens 1,585-fold" — 25.96 / 0.0164 = %s, and to the printed',
      )
print('          precision %s.  1,585 is not the quotient of the table\'s own two figures.' % q(tighten, 0))
print('          MEASURED %s ; printed 1,585 ; difference %s' % (q(tighten, 4), q(F(1585) - tighten, 4)))
print('  14n-11  the "held" column repeats the "admitted" column in every row:',
      all(a == h for _k, a, h, _r, _m in rows),
      '(499/499, 187/187, 34/34) — three categories that should partition the collection do not:',
      ', '.join('order %d sums %d' % (k, a + h + r) for k, a, h, r, _m in rows))
print('  14n-12  L6517 "619 refusals" — the section\'s own refusal counts are 19 + 101 + 145 = %d;'
      % sum(r for _k, _a, _h, r, _m in rows),
      'and 1,061 - 619 = %d, 1,061 - 34 = %d.  619 is not derivable from any printed pair here.'
      % (1061 - 619, 1061 - 34))

print()
print('== 23.10.3 V = 4nu/3 against the book\'s own exact V (L6497) ==')

for nu in (10, 40, 100):
    ex = F(4 * nu ** 3, 3 * nu ** 2 - 1)
    ap = F(4 * nu, 3)
    print('  14n-13  nu = %-3d exact V = 4r^3/(3r^2-1) = %s   printed form 4nu/3 = %s   relative gap %s%%'
          % (nu, q(ex, 6), q(ap, 6), q((ex - ap) / ex * 100, 4)))
print('          L6497 prints "V = 4nu/3" as an equality; it is the asymptote, not the value —',
      'the same class as chat 96\'s 14l-02 / 14l-03.')

sp = T(40) - T(41)
print('  14n-14  L6497 "survives a perturbation of half the local spacing" — local spacing at nu = 40',
      '= %s cm-1, half = %s; the printed tolerance is 0.129 = %s of half the spacing'
      % (q(sp, 4), q(sp / 2, 4), q(err1 / (sp / 2), 4)))

print()
print('== 23.11 the refusal-pattern classifier (L6519-L6547) ==')

tab = [('none', 'infinite', 'exact'), ('none', 'finite', 'a smooth channel'),
       ('one', 'finite', 'a bifurcation'), ('regularly spaced', 'finite', 'an oscillation'),
       ('dense and irregular', 'undefined', 'chaotic')]
pats = sorted({p for p, _v, _w in tab})
verds = sorted({w for _p, _v, w in tab})
print('  14n-15  L6519 heading "carries four verdicts, not one" and L6521 "the PATTERN is four" —',
      'the table prints %d rows, %d distinct refusal patterns, %d distinct verdicts'
      % (len(tab), len(pats), len(verds)))
print('          patterns: %s' % '; '.join(pats))
print('          verdicts: %s' % '; '.join(verds))

# the logistic map witness of L6546
x, r = 0.3, 2.5
for _ in range(4000):
    x = r * x * (1 - x)
fp = 1 - 1 / r
seq = [x]
for _ in range(12):
    x = r * x * (1 - x)
    seq.append(x)
d1 = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
signs = [(0 if d == 0 else (1 if d > 0 else -1)) for d in d1]
alt = sum(1 for i in range(len(signs) - 1) if signs[i] * signs[i + 1] < 0)
print('  14n-16  L6546 "failing on the logistic map at r = 2.5, a fixed point, which it called an',
      'oscillation" — orbit converges to 1 - 1/r = %s (measured %.15f); the residual first differences'
      % (fp, seq[-1]), 'are float noise of size %.3e and change sign %d times in %d steps, which an'
      % (max(abs(d) for d in d1), alt, len(signs) - 1))
print('          exact-zero test reads as a periodic signal  REPRODUCES')

print()
print('== 23.10.4 the admissibility rule as one rule (L6501-L6503) ==')
for k in (1, 3, 6):
    print('  14n-17  order %d: the printed rule |D^(k+1)T| > 5 * 2^(k+1) * sigma has noise factor 2^(k+1) = %d,'
          % (k, 2 ** (k + 1)), 'so it is r > 5 with r = |D^(k+1)T| / (2^(k+1) sigma) — one rule, k-indexed')

span = section_span(MAIN, '23.10')
print()
print('span of 23.10 including subsections (measured, not ranked): L%d-L%d' % (span[0], span[1] - 1))
span11 = section_span(MAIN, '23.11')
print('span of 23.11 including subsections: L%d-L%d' % (span11[0], span11[1] - 1))
