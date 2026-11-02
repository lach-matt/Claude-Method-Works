#!/usr/bin/env python3
"""dceiling5: the loss d composed over the levels with every per-level step the record charges, as a ceiling in the
record's own bounds beside the floor; and the indicial roots behind E_ind (CONSTANTS5.md, Round 3, item (ii)).

LOSS-D (1.1) composes d over III.J'' Theorem 4.1's table (PART-III-J3-TAME.md:255-272); rounds 1-2 counted the loops
(dweights5.py W3-W8, lambdagen5.py L5-L8) and left one symbol c per level for "every other step". This program
replaces that c, where the record bounds it, by the record's own ceilings, and keeps as symbols only what the record
does not bound. Labels: READ (cited lines), deduced (the reading), computed (exact integers; d0, d1 and the sl offsets
in certified intervals, mpmath.iv at 200 bits and exact rationals), estimate (where said).

  D1 (exact, sympy; certified) the indicial roots of box^Ups(0) at n = 4, every harmonic type, with real part in
     (0, 7). E_ind's exponents are built from them: E_ind is III.D'' Proposition 3.1's and III.F''' Proposition 2.2's
     index set (I5:190, I8:35), which III.A Lemma 1.4 builds as k + N_0 and the boundary spectrum of box^Ups(0) with
     real part above alpha, shifted by -k and by N_0 (F4:67-80; D3:39-48). From gaugepot5.py G1's factorisation (READ:
     s0 lam (lam - 3)(lam^2 - lam - 2 - z); vl (lam + l)(l + 2 - lam); sl (l + 3 - lam)(l + lam - 1) Q_l(lam (lam - 1)))
     the roots of Q_l are computed in closed form here: at z = 0 they give l + 1 and l + 2, so for z = 4e-6 the
     non-integer roots in (0, 7) are exactly 2 + d0 (s0), l + 1 + delta_l (l = 1..5, delta_1 = d1) and l + 2 + delta'_l
     (l = 1..4): ten, every offset in (0, 1.4e-6). "The indicial roots of E_ind below 5" are no longer open.
  D2 (READ; deduced) which offsets are increments of Lambda (I11:66-71) is a reading the record does not fix: "E_ind
     denotes an index set with min Re E_ind >= eps_ind, which may change from line to line" (D3:46-48; F4:28-30). On
     the construction reading (LOSS-D LD14, three verifiers: the states' types and bases checked family by family)
     the only increment below 1 is d1. On the widest reading (every offset of D1 below 1 admitted at every base) d0,
     delta_l, delta'_l are increments too.
  D3 (certified) (G) on the widest reading: with d0 and d1 alone as increments, 2 + n0 d0 + n1 d1 comes within
     4.679e-13 above 3 (gapsums5.py G2, reproduced here on certified intervals), 4.1e4 times below delta_50: round 1's
     weights are then inadmissible, eps_K < 4.68e-13, the beta-chain has K > 2/eps_K > 4.27e12 levels, and the floor
     of the d this proof delivers rises to the order of 1e20 (estimate: W3's count at that eps_K). On the
     construction reading (G) does not bind (lambdagen5.py L4).
  D4 (exact) on the construction reading, with every generator of rounds 1-2 (the named ones, E^C_I's chains and
     E_col's eleven bases) and the increments d1 and 1: n_0 = |Lambda cap {Re < 2}|, P_iota = |Lambda cap [2, 3 +
     eps_+ - eps]|, P_W = |Lambda cap W| (85,025,783, round 2's container, reproduced) and n_W = |Lambda cap {Re < 2 +
     eta_1}|. Then the record's log-order ceiling K(lambda) = L_0 + (N_* + 1)(l_* + 1)(n(lambda) + 1) (I11:72-80) summed
     over a range of P points above n_below points is P (L_0 + 1) + (N_* + 1)(l_* + 1)(P (n_below + 1) + P (P - 1)/2),
     the real parts being distinct: S_iota and S_W, exact linear forms in L_0 and l_* + 1, N_* = 15,000,015.
  D5 (deduced; READ I12:249-253, I14:120-121, I11:339-343, LOSS-D (2.1)) a per-level step rounds 1-2 left inside c is
     not small. III.I''''''''''' Proposition 3.1's Step 0 applies III.A Proposition 4.2 (1) with E_iota = E^flat + 2,
     beta_iota = w_+ - eps, E_I = E_K = empty, and III.I''''''''''''' repeats that proof at every level above 3; its
     loss is l = 1 + n_iota + 2 max(floor beta_K, floor B) (LOSS-D (2.1), verifier 166), n_iota the number of pairs
     (z, m) of E_iota with Re z <= beta_iota, and the record bounds E^flat only by pi_1 E^flat in Lambda cap [2, 3 +
     eps_+) with log order <= K(lambda) (I11:339-343). So n_iota <= S_iota, and nothing in the record bounds it lower:
     the actual log orders of E^flat are not computed.
  D6 (exact) the ceiling on the record's accounting, construction reading:
       d <= 3 (R2 + R3) + L_above [3 X_2 + 11 + S_iota + 15 W] + L_below [15 W + 58] + L_above X_7 + (K + 1) c',
     W = 1,470,302 (iota+ rounds or windows per level), X_2 the level-2 rounds per level (P_W per exponent, LD16; S_W
     per (alpha_0, k), the procedure as written, LD15), X_7 III.A Proposition 4.2 (2)'s loss at Step 7 (I12:389-394;
     its E_K, Step 5's K+-exponents, not bounded here), c' the per-level fixed steps (FWD: III.I Theorem 5.3's d =
     D_0 + D_1 + d' + d'' + 6, II.F2-TAME:529-535, whose D_0, D_1 are II.E's unnumbered tame orders; BG 2; the
     fixed MODs). Printed exactly as A + B L_0 + C (l_* + 1) and evaluated at the least admissible L_0 = 1 and l_* =
     l_C (D7): the record's ceiling is then at least 1.49e31 (5.97e31 per (alpha_0, k)), against the floor
     8,407,505,890,317,054.
  D7 (exact) l_C: the largest log order of E^C_I at real part <= 5 (III.C' (3.1), dweights5.py data_ECI), on the one
     corner union (R0) and on (3.1) as written (R1); l_* >= l_C by its definition (I11:72-75). E_ind's log orders and
     N_iota+(L-bar)^-1's pole orders at Re <= 5, which l_* also bounds, are not computed: the boundary spectrum
     spec_iota+(L-bar) is known only to be discrete in Re >= 2 (III.G' Lemma 4.2 (a), G2-IOTA:428-431).
  Controls (must fail, and do): C1 D1 at z = 0: every root is an integer, the offsets vanish, and D1's test fails; C2
  D4's closed form against a brute-force sum of n(lambda) + 1 on a scaled Lambda (d1 -> 1/997, a few generators):
  equal; the closed form without its n_below term disagrees; C3 D3's search with d0 removed (the construction
  reading) finds 5.02e-8 > delta_50, so D3's conclusion fails for it; C4 D5's application read with E_iota = empty
  gives l = 11, so the size comes from E^flat's log orders.

    python3 checks/dceiling5.py
"""
import builtins
import os
import sys
import textwrap
from fractions import Fraction as Fr
from math import ceil, floor

import mpmath
import sympy as sp
from mpmath import iv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dweights5 as DW  # noqa: E402  (round 1: d1, chain counts, weights, the loop counts, data_ECI)
import lambdagen5 as LG  # noqa: E402  (round 2: d0, the sl offsets, E_col's bases)
import prop31loss5 as P31  # noqa: E402

iv.prec = 200
mpmath.mp.prec = 260
DELTA50 = Fr(1941370568, 10 ** 17)
FLOOR_W3 = 8407505890317054                          # dweights5.out W3 (computed there)
NSTAR = 15000015                                      # dweights5.out W4: ceil(5/d1) + 2
W_IOTA = 1470302                                      # dweights5.out W4, LD14: iota+ rounds (windows) per level


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(x) for x in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def root_census(zval, top=7):
    """box^Ups(0)'s roots with 0 < Re < top, every type (gaugepot5.py G1's factors, READ); Q_l's roots in closed form
    (sympy), then certified at z = zval (mpmath.iv). Returns (non-integer roots, integer roots, checks)"""
    lam, s, z, kap = sp.symbols('lam s z kappa')
    Q = s ** 2 - (2 + 2 * kap + z) * s + kap * (kap + 1) + z * kap
    sroots = sp.solve(Q, s)
    disc = (z + 2) ** 2 + 4 * kap
    disc_ok = all(any(sp.simplify(r - ((2 + 2 * kap + z) + sg * sp.sqrt(disc)) / 2) == 0 for r in sroots)
                  for sg in (1, -1))
    l = sp.symbols('l', positive=True, integer=True)
    # at z = 0 the discriminant is 4 (l + 1)^2, so s = kappa + 1 -+ (l + 1) = l (l + 1), (l + 1)(l + 2)
    d0_ok = sp.expand(disc.subs({z: 0, kap: l * (l + 2)}) - 4 * (l + 1) ** 2) == 0
    at0 = [sp.expand(l * (l + 2) + 1 + sg * (l + 1)) for sg in (-1, 1)]
    z0_ok = d0_ok and at0 == [sp.expand(l * (l + 1)), sp.expand((l + 1) * (l + 2))]
    zi = iv.mpf(zval.numerator) / zval.denominator if isinstance(zval, Fr) else iv.mpf(zval)
    nonint, ints = [], set()
    # s0: 0, 3, (1 +- (9 + 4z)^(1/2))/2
    ints.update({3})
    r_s0 = (1 + iv.sqrt(9 + 4 * zi)) / 2
    nonint.append(('s0', 0, r_s0))
    for li in range(1, top + 2):
        ints.update({li + 2})                                         # vl: -l, l + 2
        ints.update({li + 3})                                         # sl: l + 3, 1 - l
        k = li * (li + 2)
        b, c = 2 + 2 * k + zi, k * (k + 1) + zi * k
        dsc = iv.sqrt(b * b - 4 * c)
        for tag, sv in (('sl-', (b - dsc) / 2), ('sl+', (b + dsc) / 2)):
            nonint.append((tag, li, iv.mpf(1) / 2 + iv.sqrt(iv.mpf(1) / 4 + sv)))
    out = []
    for tag, li, r in nonint:
        lo, hi = mpmath.mpf(r._mpi_[0]), mpmath.mpf(r._mpi_[1])
        if lo >= top or hi <= 0:
            continue
        n = int(mpmath.floor(lo))
        out.append((tag, li, n, lo - n, hi - n))
    ints = sorted(i for i in ints if 0 < i < top)
    return out, ints, disc_ok and z0_ok


def frac_iv(x):
    return LG.frpair(x)


def g_widest(d0, d1, T=3, base=2):
    """least base + n0 d0 + n1 d1 above T, n0, n1 >= 0, certified (d0, d1 rational intervals)"""
    best = None
    n0 = 0
    gap = T - base
    while n0 * d0[0] <= gap + d0[1]:
        rem_lo, rem_hi = gap - n0 * d0[1], gap - n0 * d0[0]
        if rem_hi < 0:
            break
        qa, qb = floor(rem_lo / d1[1]), floor(rem_hi / d1[0])
        if qa != qb:
            raise ValueError('undecided at n0 = %d' % n0)
        n1 = qa + 1
        v = (n0 * d0[0] + n1 * d1[0] - gap, n0 * d0[1] + n1 * d1[1] - gap)
        assert v[0] > 0
        if best is None or v[1] < best[0][1]:
            best = (v, n0, n1)
        n0 += 1
    return best


def range_count(starts, d1lo, d1hi, lo, hi):
    tot = 0
    for g in starts:
        if isinstance(g, tuple):
            a = DW.chain_points(g[0], d1lo, d1hi, lo, hi)
            b = DW.chain_points(g[1], d1lo, d1hi, lo, hi)
            assert a == b
            tot += a
        else:
            tot += DW.chain_points(g, d1lo, d1hi, lo, hi)
    return tot


def ksum(P, n_below):
    """sum over P points of distinct real parts above n_below points of (n(lambda) + 1): exact"""
    return P * (n_below + 1) + P * (P - 1) // 2


def brute_ksum(points, n_below):
    pts = sorted(points)
    return sum(n_below + i + 1 for i in range(len(pts)))


def main():
    ok = {}
    Z = Fr(4, 10 ** 6)
    roots, ints, sym_ok = root_census(Z)
    d1lo, d1hi = DW.d1_interval()
    offs = {(t, l): (lo, hi) for t, l, n, lo, hi in roots}
    labels = []
    for t, l, n, lo, hi in roots:
        name = {'s0': '2 + d0', 'sl-': '%d + delta_%d' % (l + 1, l), 'sl+': "%d + delta'_%d" % (l + 2, l)}[t]
        labels.append('%s (%.4e)' % (name, float(lo)))
    expect = 1 + 5 + 4
    in_range = all(0 < lo and hi < mpmath.mpf('1.4e-6') for _, _, _, lo, hi in roots)
    d1_is_delta1 = abs(mpmath.mpf(offs[('sl-', 1)][0]) - mpmath.mpf(float(d1lo))) < mpmath.mpf('1e-20')
    ok['D1'] = sym_ok and len(roots) == expect and in_range and d1_is_delta1
    print('  D1: Q_l\'s roots in closed form (discriminant (z + 2)^2 + 4 kappa) and l (l + 1), (l + 1)(l + 2) at z = 0: '
          '%s; non-integer roots of box^Ups(0) in (0, 7) at z = 4e-6: %d (expected 1 + 5 + 4 = %d): %s; integer '
          'roots in (0, 7): %s; every offset in (0, 1.4e-6): %s; delta_1 = d1: %s'
          % (sym_ok, len(roots), expect, '; '.join(labels), ints, in_range, d1_is_delta1))

    # D3: (G) on the widest reading
    d0 = LG.frpair(LG.d0_iv())
    gw = g_widest(d0, (d1lo, d1hi))
    ok['D3'] = gw[0][1] < DELTA50 and abs(float(gw[0][0]) - 4.679e-13) < 1e-15
    kmin = 2 / gw[0][1]
    print('  D3: widest reading, increments d0 and d1: least 2 + n0 d0 + n1 d1 above 3 is 3 + [%.6e, %.6e] at (n0, n1) '
          '= (%d, %d), %.3g times below delta_50 (certified): (G) forces eps_K < %.4e and K > 2/eps_K > %.3e; at '
          'that eps_K the floor of W3 scales to about %.1e (estimate)' % (
              float(gw[0][0]), float(gw[0][1]), gw[1], gw[2], float(DELTA50 / gw[0][1]), float(gw[0][1]),
              float(kmin), float(FLOOR_W3 * Fr(188, 10 ** 10) / gw[0][1])))
    g_con = LG.g_search([('2', Fr(2), Fr(2)), ('lambda_sharp', DW.LSHARP, DW.LSHARP)], d1lo, d1hi)
    ok['C3'] = not (g_con[1][1] < DELTA50)
    print('  C3 (control): the same search with d0 removed (construction reading): 3 + %.4e > delta_50: D3\'s '
          'conclusion fails for it: %s' % (float(g_con[1][0]), ok['C3']))

    # D4: Lambda's counts on the construction reading
    w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))
    named = [DW.LSHARP, Fr(2), Fr(3)]
    E = P31.least_ECI()
    top_i = 3 + w['eps_p'] - w['eps'] + Fr(1, 10 ** 40)
    starts = sorted({g + m for g in named for m in (0, 1)} | {z for z in E if z < 4})
    bases = [(lo, hi) for _, lo, hi in LG.ecol_bases()]
    allst = list(starts) + bases
    wlo, whi = 2 + w['eta1'], 3 + w['eta2']
    n0 = range_count(allst, d1lo, d1hi, Fr(0), Fr(2))
    P_i = range_count(allst, d1lo, d1hi, Fr(2), top_i)
    P_W = range_count(allst, d1lo, d1hi, wlo, whi)
    nW = range_count(allst, d1lo, d1hi, Fr(0), wlo)
    T_i, T_W = ksum(P_i, n0), ksum(P_W, nW)
    ok['D4'] = P_W == 85025783 and n0 == W_IOTA and P_i == P_W + 1 and nW == n0 + 1
    print('  D4: construction reading: n_0 = |Lambda cap {Re < 2}| = %d; P_iota = |Lambda cap [2, 3 + eps_+ - eps]| = '
          '%d; P_W = |Lambda cap W| = %d (round 2\'s container: %s); n_W = %d' % (n0, P_i, P_W, P_W == 85025783, nW))
    print('      S_iota = %d (L_0 + 1) + %d (N_* + 1)(l_* + 1); S_W = %d (L_0 + 1) + %d (N_* + 1)(l_* + 1) (exact)' % (
        P_i, T_i, P_W, T_W))

    # C2: closed form against brute force on a scaled instance
    dsm = Fr(1, 997)
    gens = [Fr(3, 2) + Fr(1, 100), Fr(2), Fr(5, 2) + Fr(1, 300), Fr(13, 5) + Fr(1, 7)]
    pts_b = sorted({g + n * dsm for g in gens for n in range(0, 2000) if 0 <= g + n * dsm < 2})
    pts = sorted({g + n * dsm for g in gens for n in range(0, 2000) if 2 <= g + n * dsm < 3})
    bf = brute_ksum(pts, len(pts_b))
    cf = ksum(len(pts), len(pts_b))
    bad = len(pts) + len(pts) * (len(pts) - 1) // 2
    ok['C2'] = bf == cf and bad != bf
    print('  C2 (control): scaled Lambda (%d points below 2, %d in [2, 3)): brute force %d = closed form %d; without '
          'the n_below term %d: differs' % (len(pts_b), len(pts), bf, cf, bad))

    # D7: l_C
    lC = {}
    for name, M in (('R0', 1), ('R1, M = 4', 4)):
        Ed = DW.data_ECI(M, top=Fr(5))
        lC[name] = max(k for zz, k in Ed.items() if zz <= 5)
    ok['D7'] = lC['R0'] >= 1
    print('  D7: the largest log order of E^C_I at Re <= 5: %s (exact; dweights5 data_ECI): l_* >= l_C' % lC)

    # D5-D6: the ceiling
    c = DW.counts(w)
    La, Lb, K = c['levels_above3'], c['levels_below3'], c['K']
    L0, ls1 = sp.symbols('L_0 l_star_plus_1', positive=True)
    S_i = P_i * (L0 + 1) + T_i * (NSTAR + 1) * ls1
    S_W = P_W * (L0 + 1) + T_W * (NSTAR + 1) * ls1
    floorB = floor(5 + w['eps_p'] - w['eps'])          # B = max(beta_K, beta_iota) = w_+ - eps = 5 + eps_+ - eps
    prop42 = 1 + S_i + 2 * floorB
    base = 3 * (c['R2'] + c['R3']) + Lb * (15 * W_IOTA + 10 + 48)
    per_exp = sp.expand(base + La * (3 * P_W + prop42 + 15 * W_IOTA))
    per_ak = sp.expand(base + La * (3 * S_W + prop42 + 15 * W_IOTA))
    vals = {}
    for nm, form in (('per exponent (LD16)', per_exp), ('per (alpha_0, k) (LD15)', per_ak)):
        least = form.subs({L0: 1, ls1: lC['R0'] + 1})
        vals[nm] = least
        print('  D6: d <= %s + %d X_7 + %d c\'  [level-2 rounds %s]' % (form, La, K + 1, nm))
        print('      at the least admissible L_0 = 1, l_* = l_C(R0) = %d: d <= %.6e + %d X_7 + %d c\'; N = 21 d + 6 '
              '<= %.6e + ... (exact integer %d)' % (lC['R0'], float(least), La, K + 1, float(21 * least + 6),
                                                       int(least)))
    # Round 4 (verifier): D6 asserts the exact forms (reproduced by the round-3 reader, R3.1) and its constant term
    # rebuilt from its parts, so a mutated step changes the result and fails
    R2_, R3_ = c['R2'], c['R3']
    A_parts = 3 * (R2_ + R3_) + La * (3 * P_W + 11 + P_i + 15 * W_IOTA) + Lb * (15 * W_IOTA + 58)
    ok['D6'] = (per_exp.coeff(L0) == 4527175422273024 and per_exp.coeff(ls1) == 2986797742916004835692267122688
                and per_exp.subs({L0: 0, ls1: 0}) == 28864786304360710 == A_parts
                and per_ak.coeff(L0) == 18108701529357888
                and per_ak.coeff(ls1) == 11947190968141150306670744890368 and La * P_i == 4527175422273024)
    ratio = float(min(vals.values())) / FLOOR_W3
    print('      against the floor d >= %d (W3): the record\'s accounting leaves a factor of at least %.2e between '
          'floor and ceiling; III.A Proposition 4.2\'s n_iota alone is <= %.3e per level' % (
              FLOOR_W3, ratio, float(prop42.subs({L0: 1, ls1: lC['R0'] + 1}))))
    ok['D5'] = (prop42 - S_i == 1 + 2 * 5 and floorB == 5 and La == 53244736
                and float(S_i.subs({L0: 1, ls1: 1})) > 5.6e22)      # Round 4: computed, not hard-coded
    e_empty = 1 + 0 + 2 * floorB
    ok['C4'] = e_empty == 11 and float(prop42.subs({L0: 1, ls1: 1})) > 10 ** 20
    print('  C4 (control): III.A Proposition 4.2 (1) at Step 0 read with E_iota empty: l = %d; with E^flat bounded by '
          'K(lambda): >= %.3e: the size is E^flat\'s log orders' % (e_empty, float(prop42.subs({L0: 1, ls1: 1}))))
    zr, _, _ = root_census(Fr(0))
    z0_fail = all(lo == 0 and hi == 0 for _, _, _, lo, hi in zr) or not all(0 < lo for _, _, _, lo, hi in zr)
    ok['C1'] = z0_fail
    print('  C1 (control): D1 at z = 0: offsets %s: not all positive, D1\'s test fails: %s' % (
        sorted({float(hi) for _, _, _, lo, hi in zr})[:3], z0_fail))
    for k, v in ok.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
