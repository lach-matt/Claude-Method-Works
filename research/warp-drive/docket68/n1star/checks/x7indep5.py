#!/usr/bin/env python3
"""x7indep5: SUM X_7, d and N of dnumber5.py (K4, K5) reproduced by an independent route, and dnumber5's production
path tested against brute force and under mutation (CONSTANTS5.md, Round 7, R7.0, the round-6 verifier's MAJOR 3; its
scratch script x7indep.py, adopted here with its route unchanged). Labels: computed (exact integers and rationals).

  I1 (computed) an independently written floor sum fs(n, m, a, b) = sum_{i<n} floor((a i + b)/m) (Euclid-like
     recursion) agrees with brute force and with dweights5.floor_sum on 3000 random cases.
  I2 (computed) dnumber5.chain_level_sum (the production function) against brute-force enumeration over the levels on
     600 random small instances (alpha1, s, eps, alpha, k3, K, g, n_a, d1 rationals): equal on every one.
  I3 (computed) the swapped order: for each chain of dnumber5.chains, the sum over its points g + n d1 in (2, 3) of the
     number of levels counting them (levels k3..K-1 with beta_k - 1 - eps >= the point, and the top), with fs, at both
     ends of the d1 and base intervals (equal), equal to chain_level_sum chain by chain; the special points z = 1, 2 and
     ceil(beta - 5/2) recomputed directly. The four totals equal dnumber5's pins X7_PIN, and d = A + max over the E_col
     readings equals D_PIN (A of K1, READ), N = 21 d + 6.
  I4 (deduced; computed at one chain) the two-ends certification: with n_a fixed, each indicator is nonincreasing in g
     and in d1, so the true sum lies between its values at (g_hi, d1_hi) and (g_lo, d1_lo); checked at the midpoint of
     the d1 interval for the first E_col chain (equal to both ends).
  Controls (mutations of dnumber5's production path, x7_totals; each must change a pinned total, and does): M1 the top
  level dropped from every chain sum; M2 the ceil(beta - 5/2) term set to 1 at every level; M3 two per point instead of
  three; M4 E^flat's excess set to 0 on every chain. And M5: chain_level_sum with the top level dropped disagrees with
  I2's brute force.

    python3 checks/x7indep5.py       (about twenty seconds)
"""
import builtins
import contextlib
import io
import os
import random
import sys
import textwrap
from fractions import Fraction as Fr
from math import floor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import dnumber5 as DN       # noqa: E402
    import dweights5 as DW      # noqa: E402

OK = {}
A_K1 = {'R0': 37919138373535686, 'R1': 37919139651409350}     # READ dnumber5.out K1 (pinned there)


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def fs(n, m, a, b):
    """sum_{i=0}^{n-1} floor((a i + b)/m), m > 0, written independently (Euclid-like recursion)"""
    if n <= 0:
        return 0
    res = 0
    qa, a = divmod(a, m)
    qb, b = divmod(b, m)
    res += qa * n * (n - 1) // 2 + qb * n
    if a == 0:
        return res
    ymax = a * (n - 1) + b
    t = ymax // m
    if t == 0:
        return res
    res += t * n - fs(t, a, m, m - b + a - 1)
    return res


def ceil_q(x):
    return -((-x.numerator) // x.denominator)


def chain_sum_swapped(g, n_a, d1, w, c):
    """sum over n in [n_a, n_b] of #levels counting g + n d1 (levels k3..K-1 and the top)"""
    a1, s, eps, al = w['alpha1'], w['s'], w['eps'], w['alpha']
    k3, K = c['k3'], c['K']
    q = (3 - g) / d1
    n_b = ceil_q(q) - 1
    if n_b < n_a:
        return 0, 0
    npts = n_b - n_a + 1
    qnb = ceil_q((g + n_b * d1 + 1 + eps - a1) / s)
    assert qnb <= K - 1 and al - 1 - eps > 3
    thr = (k3 - 1) * s + a1 - 1 - eps - g
    nstar = n_a if thr < 0 else max(n_a, floor(thr / d1) + 1)
    below = max(0, min(nstar, n_b + 1) - n_a)
    tot = below * ((K - 1) - k3 + 2)
    n2 = n_b - nstar + 1
    if n2 > 0:
        A = -(g + 1 + eps - a1 + nstar * d1) / s
        B = -d1 / s
        D = A.denominator * B.denominator
        sm = fs(n2, D, int(B * D), int(A * D))
        tot += n2 * ((K - 1) + 2) + sm
    return tot, npts


def brute_chain(g, n_a, d1, w, c, top_level=True):
    a1, s, eps, al = w['alpha1'], w['s'], w['eps'], w['alpha']
    pts = []
    n = n_a
    while g + n * d1 < 3:
        pts.append(g + n * d1)
        n += 1
    tot = 0
    for k in range(c['k3'], c['K']):
        beta = a1 + k * s
        tot += sum(1 for x in pts if x <= beta - 1 - eps)
    if top_level:
        tot += sum(1 for x in pts if x <= al - 1 - eps)
    return tot


def independent_totals(w, c, T, d1lo, d1hi):
    res, per_chain_ok = {}, True
    for reading in ('R0', 'R1'):
        for rd in ('wide', 'shifted'):
            chs, sp = DN.chains(w, T, reading, rd, d1lo, d1hi)
            tot = 0
            for ch in chs:
                v1, p1 = chain_sum_swapped(ch['hi'], ch['n_a'], d1hi, w, c)
                v2, p2 = chain_sum_swapped(ch['lo'], ch['n_a'], d1lo, w, c)
                ref = DN.chain_level_sum(dict(g=ch['lo'], n_a=ch['n_a']), w, c, d1lo)[0]
                per_chain_ok = per_chain_ok and v1 == v2 and p1 == p2 and ref == v1
                tot += (3 + ch['e']) * v1
            a1, s, eps, K, k3, al = w['alpha1'], w['s'], w['eps'], c['K'], c['k3'], w['alpha']

            def nlev(thr):
                qq = ceil_q((thr - a1) / s)
                return (K - 1) - max(k3, qq) + 1 + (1 if al >= thr else 0)
            spec = nlev(3 + eps) * (sp['z1'] + 1) + nlev(4 + eps) * (sp['z2'] + 1)
            x72 = (Fr(7, 2) - a1) / s
            k72 = ceil_q(x72) if x72.denominator != 1 else int(x72) + 1
            lF = (K + 1 - k3) + ((K - 1) - max(k3, k72) + 1 + 1)
            res[(reading, rd)] = tot + spec + lF
    return res, per_chain_ok


def main():
    print('x7indep5: SUM X_7, d and N by an independent route; dnumber5\'s production path under test')
    random.seed(1)
    ok1 = True
    for _ in range(3000):
        n, m = random.randint(0, 60), random.randint(1, 40)
        a, b = random.randint(-50, 50), random.randint(-50, 50)
        bf = sum((a * i + b) // m for i in range(n))
        ok1 = ok1 and fs(n, m, a, b) == bf == DW.floor_sum(n, m, a, b)
    OK['I1'] = ok1
    print('  I1: the independent floor sum agrees with brute force and dweights5.floor_sum on 3000 random cases: %s'
          % ok1)
    ok2, ok5 = True, True
    for _ in range(600):
        a1 = Fr(random.randint(150, 250), 100)
        s = Fr(random.randint(1, 30), 997)
        eps = Fr(1, random.randint(10 ** 3, 10 ** 4))
        K = random.randint(5, 60)
        k3 = random.randint(0, K - 1)
        al = Fr(9, 2) + Fr(random.randint(0, 99), 100)
        g = Fr(random.randint(150, 299), 100)
        d1 = Fr(random.randint(1, 40), 997)
        n_a = 0 if g > 2 else (floor((2 - g) / d1) + 1)
        w = dict(alpha1=a1, s=s, eps=eps, alpha=al)
        c = dict(k3=k3, K=K)
        prod = DN.chain_level_sum(dict(g=g, n_a=n_a), w, c, d1)[0]
        ok2 = ok2 and prod == brute_chain(g, n_a, d1, w, c)
        mut = DN.chain_level_sum(dict(g=g, n_a=n_a), w, c, d1, top_level=False)[0]
        if brute_chain(g, n_a, d1, w, c) > 0:
            ok5 = ok5 and mut != brute_chain(g, n_a, d1, w, c)
    OK['I2'] = ok2
    print('  I2: dnumber5.chain_level_sum equals brute-force enumeration on 600 random small instances: %s' % ok2)
    w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))
    c = DW.counts(w)
    d1lo, d1hi = DW.d1_interval()
    with contextlib.redirect_stdout(io.StringIO()):
        T = DN.logs_tables()
    res, per_chain = independent_totals(w, c, T, d1lo, d1hi)
    dd = {r_: A_K1[r_] + max(res[(r_, 'wide')], res[(r_, 'shifted')]) for r_ in ('R0', 'R1')}
    OK['I3'] = per_chain and res == DN.X7_PIN and dd == DN.D_PIN
    for key in sorted(res):
        print('  I3 %s/%s: SUM X_7 = %d (swapped order), pinned in dnumber5: %d' % (key[0], key[1], res[key],
                                                                                 DN.X7_PIN[key]))
    print('      every chain sum equal at both ends and to chain_level_sum: %s; d <= %d (R0), %d (R1) + %d c\', N = 21 d '
          '+ 6 <= %d + %d c\' (R1); equal to dnumber5\'s pins: %s' % (
              per_chain, dd['R0'], dd['R1'], c['K'] + 1, 21 * dd['R1'] + 6, 21 * (c['K'] + 1), OK['I3']))
    chs, _ = DN.chains(w, T, 'R1', 'wide', d1lo, d1hi)
    ch = [x for x in chs if x['lo'] != x['hi']][0]
    mid = (d1lo + d1hi) / 2
    vm = DN.chain_level_sum(dict(g=(ch['lo'] + ch['hi']) / 2, n_a=ch['n_a']), w, c, mid)[0]
    OK['I4'] = vm == ch['sum'] if 'sum' in ch else vm == DN.certified_chain_sum(ch, w, c, d1lo, d1hi)[0]
    print('  I4: the chain %s at the midpoint of its base and d1 intervals: %d, equal to both ends: %s' % (
        ch['name'], vm, OK['I4']))
    open23 = sum(DN.certified_chain_sum(x, w, c, d1lo, d1hi)[2] for x in chs)
    muts = {'M1 top level dropped': dict(top_level=False), 'M2 ceil term 1': dict(lF_on=False),
            'M3 two per point': dict(per_point=2), 'M4 excess 0': dict(excess_on=False)}
    for name, kw in muts.items():
        r = DN.x7_totals(w, c, T, d1lo, d1hi, open23, **kw)
        changed = any(r[key]['X7'] != DN.X7_PIN[key] for key in DN.X7_PIN)
        OK[name.split()[0]] = changed
        print('  %s (control): x7_totals changes a pinned total: %s (R1/wide %d)' % (
            name, changed, r[('R1', 'wide')]['X7']))
    OK['M5'] = ok5
    print('  M5 (control): chain_level_sum with the top level dropped disagrees with brute force on every instance '
          'with a point: %s' % ok5)
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
