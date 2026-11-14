#!/usr/bin/env python3
"""iotamut5: the round-4 instrument iotapoles5.py read adversarially (CONSTANTS5.md, Round 5, R5.1). Its computed path
is mutated and rerun, its singleton pole orders are computed instead of assigned, and its control C4 is shown to be
unable to fail on its own. Labels: computed (exact, sympy, unless said), deduced (where said).

iotapoles5.py is imported, never copied; type_analysis, laurent_order and lemma14 are its own functions.

  U1 (exact) the s0 and t2 types are recomputed by iotapoles5.type_analysis (its M3; about six minutes).
  U2 (exact) every singleton candidate lam0 = r + i of M3 (one singular factor N(lam0 - i)) gets its order from the
     same facts the deduction uses, now each computed: r a simple root of an irreducible factor p of det N; for every
     i' != i in 1..j, Res_x(p(x), det N(x + i - i')) != 0 (no second singular factor); for every i' in 1..j,
     Res_x(p(x), det(C - (x + i - i' + 1))) != 0 (every L1 factor invertible). A simple zero of det N gives nullity 1,
     so N^-1 has a pole of order exactly 1 with a rank-1 residue, and the product with invertible holomorphic factors
     keeps order 1 (deduced). iotapoles5 assigned (1, 1) to these candidates without computing them (its M3 assertion
     cannot fail there); here the premises are computed exactly.
  U3 (computed, mpmath, 60 digits) an independent check of the order at lam0 = 5 (s0): the product
     Pi_4(5 + eps)^-1 evaluated at eps = 10^-10, 10^-20, 10^-30; its norm scales as eps^-1 (slope of log norm against
     log eps in [-1.01, -0.99]) and eps times it has two singular values bounded away from zero and two below 10^-8:
     order 1, residue rank 2, as M3's exact Laurent expansion says.
  Mutations of the computed path (each must change the answer, and the program checks that it does):
  X1 the Mellin shift in the s0 product at lam0 = 5 taken as N(lam0 + eps - i + 1): (order, rank) differs from (1, 2).
  X2 a planted double root: N's last row multiplied by (x - 4): det N gains (x - 4)^2 and M3's simplicity test fails.
  X3 laurent_order (the routine M3 and C4 rest on) on matrices of known Laurent structure: diag(eps^-2, 1) -> (2, 1),
     eps^-1 I -> (1, 2), [[eps^-1, eps^-2], [0, 1]] -> (2, 1); and a mutated routine that stops at the first finite
     entry returns a wrong answer on the first.
  X4 lemma14 (M5) with the inner extended union F U-bar (E_j + 1) replaced by a plain union: the log order at real part
     5 changes from 10 (so M5's assertion fails on it).
  C4's dependence (deduced; computed check): det N(2 + eps) has a simple zero at eps = 0, so adj N(2 + eps) = det N(2 +
     eps) N(2 + eps)^-1 lowers the order of the product by exactly one and keeps the residue's rank. So C4's output is
     (order - 1, rank) of the main computation whatever that computation returns, and C4 cannot fail on its own;
     U3 and X1 replace it.

    python3 checks/iotamut5.py        (about seven minutes)
"""
import builtins
import os
import sys
import textwrap
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import iotapoles5 as IP  # noqa: E402  (round 4; imported, not copied)

x, eps = IP.x, IP.eps
OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def product(M1, L1, l0, j, shift=0, drop_L1=False, adj_at=None):
    K = M1.shape[0]
    P = sp.eye(K)
    for i in range(j, 0, -1):
        Ni = M1.subs(x, l0 + eps - i + shift)
        Fi = Ni.adjugate() if adj_at == i else Ni.inv()
        Li = sp.eye(K) if drop_L1 else L1.subs(x, l0 + eps - i + 1)
        P = (P * Fi * Li).applyfunc(sp.cancel)
    return P


def j_of(l0):
    j = 1
    while not (0 < l0 - j < sp.Rational(3, 2)):
        j += 1
    return j


def singletons(info):
    """U2: exact premises of order 1 at every singleton candidate"""
    M1, L1 = info['M1'], info['L1']
    K = M1.shape[0]
    detN = sp.Poly(sp.numer(sp.together(M1.det())), x)
    C = (L1 + x * sp.eye(K)).applyfunc(sp.expand)
    chiC = sp.Poly((C - x * sp.eye(K)).det(), x)
    out = []
    for f, mult in sp.factor_list(detN)[1]:
        for (a, b), _ in f.intervals(eps=sp.Rational(1, 10 ** 12)):
            if not (b > 0 and a <= 4):
                continue
            for i in range(1, 6):
                if a + i > 5:
                    continue
                l0 = (sp.Rational(a) + sp.Rational(b)) / 2 + i      # inside (r + i)'s isolating interval
                j = j_of(sp.Rational(a) + i) if a == b else j_of(l0)
                if a == b and a + i == 5 and K > 1:
                    continue                                       # the group at 5 (two singular factors): M3, U3
                others = []
                for ip in range(1, j + 1):
                    if ip != i:
                        q = sp.Poly(detN.as_expr().subs(x, x + i - ip), x)
                        others.append(sp.resultant(f, q) != 0)
                l1s = [sp.resultant(f, sp.Poly(chiC.as_expr().subs(x, x + i - ip + 1), x)) != 0
                       for ip in range(1, j + 1)]
                out.append(dict(root=(float(a), float(b)), i=i, j=j, simple=(mult == 1 and f.degree() >= 1
                                and sp.gcd(f, f.diff(x)).degree() == 0), others=all(others), l1=all(l1s)))
    return out


def numeric_order(M1, L1, l0=5, j=4, dps=60):
    mp.mp.dps = dps
    fM = sp.lambdify(x, M1, 'mpmath')
    fL = sp.lambdify(x, L1, 'mpmath')
    norms, svs = [], None
    for k in (10, 20, 30):
        e = mp.mpf(10) ** (-k)
        P = mp.eye(M1.shape[0])
        for i in range(j, 0, -1):
            P = P * mp.inverse(mp.matrix(fM(l0 + e - i))) * mp.matrix(fL(l0 + e - i + 1))
        norms.append((e, mp.mnorm(P, 'F')))
        if k == 30:
            svs = sorted(mp.svd_r(P * e, compute_uv=False), reverse=True)
    slope = (mp.log(norms[-1][1]) - mp.log(norms[0][1])) / (mp.log(norms[-1][0]) - mp.log(norms[0][0]))
    return float(slope), [float(s) for s in svs]


def laurent_bad(Pinv):
    """a mutated laurent_order: stops when the (0, 0) entry is finite"""
    m = 0
    while True:
        if sp.limit(Pinv[0, 0] * eps ** m, eps, 0).is_finite:
            return m, (Pinv * eps ** m).applyfunc(lambda q: sp.limit(q, eps, 0)).rank()
        m += 1


def main():
    t0 = time.time()
    print('iotamut5: iotapoles5.py read adversarially -- singleton orders computed, an independent order check at 5, '
          'four mutations of the computed path')
    info = {t: IP.type_analysis(t, t) for t in ('s0', 't2')}
    s0 = info['s0']
    OK['U1'] = s0['orders'][(5.0, 5.0)] == (1, 2) and info['t2']['orders'] == {(5.0, 5.0): (1, 1)}
    print('  U1: iotapoles5.type_analysis rerun: s0 order at 5 %s, t2 %s (%.0f s)' % (
        s0['orders'][(5.0, 5.0)], info['t2']['orders'], time.time() - t0))
    # U2
    rows = singletons(s0) + singletons(info['t2'])
    OK['U2'] = len(rows) >= 6 and all(r_['simple'] and r_['others'] and r_['l1'] for r_ in rows)
    print('  U2: singleton candidates (root interval, i, j: simple root, no second singular factor, every L1 '
          'invertible), exact resultants: %s' % [('[%.10f, %.10f]' % r_['root'], r_['i'], r_['j'], r_['simple'],
                                                   r_['others'], r_['l1']) for r_ in rows])
    # U3
    slope, svs = numeric_order(s0['M1'], s0['L1'])
    OK['U3'] = -1.01 < slope < -0.99 and svs[1] > 1e-6 and svs[2] < 1e-8
    print('  U3: Pi_4(5 + eps)^-1 at eps = 1e-10, 1e-20, 1e-30 (mpmath, 60 digits): slope of log |.|_F against log '
          'eps %.6f; singular values of eps Pi^-1 at 1e-30: %s: order 1, residue rank 2' % (
              slope, ['%.3e' % q for q in svs]))
    # X1
    o1 = IP.laurent_order(product(s0['M1'], s0['L1'], 5, 4, shift=1))
    OK['X1'] = o1 != (1, 2)
    print('  X1 (mutation): the shift N(lam0 + eps - i + 1) in the s0 product at 5: (order, rank) = %s, not (1, 2): %s'
          % (o1, OK['X1']))
    o1b = IP.laurent_order(product(s0['M1'], s0['L1'], 5, 4, drop_L1=True))
    print('      (beside it, not a control: the product with the L1 factors dropped gives %s)' % (o1b,))
    # X2
    M1d = s0['M1'].copy()
    M1d[M1d.shape[0] - 1, :] = M1d[M1d.shape[0] - 1, :] * (x - 4)
    num = sp.numer(sp.together(M1d.det()))
    pos = [(a, b, m) for a, b, m, f in IP.real_roots_in(num, 0, 4) if b > 0 and a <= 4]
    simple_d = all(m == 1 for _, _, m in pos)
    OK['X2'] = not simple_d
    print('  X2 (mutation): last row of N times (x - 4): roots in (0, 4] with multiplicities %s; M3\'s simplicity '
          'test fails: %s' % ([('%.6f' % a, m) for a, _, m in pos], OK['X2']))
    # X3
    t1 = IP.laurent_order(sp.diag(eps ** -2, 1))
    t2 = IP.laurent_order(sp.eye(2) / eps)
    t3 = IP.laurent_order(sp.Matrix([[1 / eps, eps ** -2], [0, 1]]))
    bad = laurent_bad(sp.Matrix([[1 / eps, eps ** -2], [0, 1]]))
    OK['X3'] = t1 == (2, 1) and t2 == (1, 2) and t3 == (2, 1) and bad != (2, 1)
    print('  X3: laurent_order on known matrices: diag(eps^-2, 1) %s, eps^-1 I %s, [[eps^-1, eps^-2], [0, 1]] %s; '
          'the mutated routine (stops at a finite (0, 0) entry) returns %s on the last: wrong, as it must be' % (
              t1, t2, t3, bad))
    # X4
    def lemma14_plain_inner(roots, k, top):
        def closure(pts):
            out = {}
            for z0, lo in pts.items():
                n = 0
                while z0 + n <= top:
                    out[z0 + n] = max(out.get(z0 + n, -1), lo)
                    n += 1
            return out

        def ubar(A, B, ext=True):
            out = dict(A)
            for z0, lo in B.items():
                out[z0] = (out[z0] + lo + 1) if (z0 in out and ext) else max(out.get(z0, -1), lo)
            return out
        Ea = closure({r_: 0 for r_ in roots})
        F = closure({sp.Rational(k): 0})
        E = ubar(Ea, F)
        U = dict(E)
        for _ in range(int(top) + 3):
            sh = {z0 + 1: lo for z0, lo in E.items() if z0 + 1 <= top}
            E = ubar(Ea, ubar(F, sh, ext=False))
            for z0, lo in E.items():
                U[z0] = max(U.get(z0, -1), lo)
        return U
    roots = [sp.Rational(i) for i in range(3, 11)]
    U = lemma14_plain_inner(roots, 2, 7)
    lo5 = U[sp.Rational(7)]
    Uref = IP.lemma14([__import__('fractions').Fraction(i) for i in range(3, 11)], 2,
                      __import__('fractions').Fraction(7))
    OK['X4'] = lo5 != 10 and Uref[__import__('fractions').Fraction(7)] == 10
    print('  X4 (mutation): Lemma 1.4 at k = 2 with F U-bar (E_j + 1) a plain union: log order at E_ind\'s 5 is %d '
          '(iotapoles5.lemma14 on the same roots: %d): M5 fails on it: %s' % (
              lo5, Uref[__import__('fractions').Fraction(7)], OK['X4']))
    # C4's dependence
    dN2 = sp.Poly(sp.numer(sp.together(s0['M1'].subs(x, 2 + eps).det())), eps)
    ordz = min(m[0] for m in dN2.monoms())
    c4 = IP.laurent_order(product(s0['M1'], s0['L1'], 5, 4, adj_at=3))
    OK['C4dep'] = ordz == 1 and c4 == (s0['orders'][(5.0, 5.0)][0] - 1, s0['orders'][(5.0, 5.0)][1])
    print('  C4 (deduced, checked): det N(2 + eps) vanishes to order %d at eps = 0, and the adjugate product gives %s = '
          '(order - 1, rank) of the main one: C4 is a function of M3\'s answer and cannot fail on its own: %s' % (
              ordz, c4, OK['C4dep']))
    print('  (%.0f s)' % (time.time() - t0))
    for k_, val in OK.items():
        builtins.print(k_, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
