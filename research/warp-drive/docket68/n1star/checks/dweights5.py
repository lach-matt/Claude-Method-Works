#!/usr/bin/env python3
"""dweights5: the loss d (LOSS-D.md section 4, E1'a-E1'c) at one explicit choice of the weights (CONSTANTS5.md, D2).

Labels: computed (exact rationals; d1 and every quantity built on it in certified rational intervals); deduced (the
readings cited at each item); READ (delta_50 from checks/eindcert5.out I1, the formulas quoted from LOSS-D.md).

  W1 (exact) the weights: one rational choice at the record's point (gamma_Ups = e_Ups = 1/100), with every inequality of
     LOSS-D section 3, VII (0.1) and I11 Definition 1.3 that the record's computed data can decide checked, and the
     ones they cannot decide listed with the missing input.
  W2 (certified) (G) through the generators pi_1 E^C_I of Lambda (I11 Definition 1.1): with the increments d1 and 1
     only, the least value of Re lambda above 2 or 3 over the chains of {lambda_sharp, 2, 3} reproduces LOSS-D LD9 G7's
     5.02e-8; the points of the least E^C_I of III.C Definition 3.1 (contained in every admissible E^C_I) add 24 chains
     and lower nothing: (G) does not bind on these generators, eps_ind stays the binding cap.
  W3 (exact) the loop counts at these weights by an exact floor-sum: the beta-levels, the tf rounds of III.I'''''''' Step
     3.4' at the levels below 3 and the level-3 rounds of III.I''''''''''''' at the levels above 3; the floor 3 x rounds.
  W4 (certified) the per-level ceilings on the construction's reading: iota+ rounds, N_*, and the level-2 container
     |Lambda' cap W| (reproducing LD15's 7,470,307 for the named generators) with E^C_I's chains added.
  W5 (exact) the log terms of the data's E^C_I: III.C' (3.1)'s construction (PART-III-C2-POLYHOM.md:247-259) with the
     assembly's E_0 = {(j, 0): j >= 2} (PART-VII-ASSEMBLY.md:45) puts logarithms below l_I; III.I' Proposition 3.1's
     count 1 + J + L on it, read two ways, against 6 for the log-free set (control: E_0 empty reproduces it).
  W6 (exact) III.I' Proposition 2.1's count where III.I''''' applies it (I6:214-218), at l_I = 13/4: 5 steps, loss 10,
     against the floor 4 steps, 8 (LD16 D582).
  W7 the elementary losses at these weights: d_G = 11 on the iota+ window, III.G''' Lemma 2.2's l = 18, Proposition
     2.4's l' = 30, Corollary 3.4's l = 1 (READ, thetain5 T4).
  W8 (conditional) the composition (1.1) over the levels with every count above, on hypotheses H1-H4 of CONSTANTS5.md
     D2.6, the uncounted steps left as one symbol c per level: d <= D_cond + (K + 1) c.
  Negative controls (must fail, and do): N1 a weight choice with eps_+ >= eps_ind; N2 the floor-sum against brute force
  with a perturbed formula; N3 the extended union without its +1 gives no logarithm; N4 l_I = 3.6 changes W6 and W7;
  N5 (added in round 2) round 1's chain list, which excluded only the named generators and so counted the chain of
  lambda_sharp + 1 = 2.5099 twice, disagrees with the count on the deduplicated union of the chain starts.

    python3 checks/dweights5.py
"""
import os
import sys
from fractions import Fraction as Fr
from math import isqrt, ceil, floor, lcm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prop31loss5 as P31  # noqa: E402  (least_ECI, chain: the record's own instrument, reused, not copied)
import builtins  # noqa: E402
import textwrap  # noqa: E402


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(x) for x in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False) if len(line) > 121 else line, **k)

E_UPS = G_UPS = Fr(1, 100)
Z = 4 * E_UPS * G_UPS ** 2                      # det I(2) = 16 e g^2 = 4z (LOSS-D LD9)
SIGMA = [Fr(0), (1 - E_UPS) * G_UPS, G_UPS, 2 * G_UPS]
LSHARP = Fr(3, 2) + (1 - E_UPS) * G_UPS          # 1.5099
DSHARP = LSHARP - Fr(3, 2)                       # 2 lambda_sharp = 3 + 2 delta_sharp
DELTA50_LO = Fr(1941370568, 10 ** 17)            # READ: eindcert5.out I1, [1.94137056846e-8 +- 3e-48]
D1_READ = Fr(33333305, 10 ** 14)                 # READ: LOSS-D LD9, d1 = 3.3333305e-7 (a check on W0)


def sqrt_iv(lo, hi, S=10 ** 45):
    """certified rational bounds for sqrt over [lo, hi] (lo, hi >= 0 Fractions)"""
    a = isqrt(lo.numerator * lo.denominator * S * S)
    b = isqrt(hi.numerator * hi.denominator * S * S) + 1
    return Fr(a, lo.denominator * S), Fr(b, hi.denominator * S)


def d1_interval():
    """d1 = lambda_s1,2 - 2, lambda_s1,2 = (1 + sqrt(17 + 2z - 2 sqrt(z^2 + 4z + 16)))/2 (III.D (4.1))"""
    ilo, ihi = sqrt_iv(Z * Z + 4 * Z + 16, Z * Z + 4 * Z + 16)
    olo, ohi = sqrt_iv(17 + 2 * Z - 2 * ihi, 17 + 2 * Z - 2 * ilo)
    return (1 + olo) / 2 - 2, (1 + ohi) / 2 - 2


def floor_sum(n, m, a, b):
    """sum_{i=0}^{n-1} floor((a i + b)/m), exact, m >= 1"""
    ans = 0
    if n <= 0:
        return 0
    if a < 0:
        a2 = a % m
        ans -= n * (n - 1) // 2 * ((a2 - a) // m)
        a = a2
    if b < 0:
        b2 = b % m
        ans -= n * ((b2 - b) // m)
        b = b2
    while True:
        if a >= m:
            ans += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y = a * n + b
        if y < m:
            return ans
        n, b, m, a = y // m, y % m, a, m


def residues(gens, d1lo, d1hi, targets=(2, 3), shifts=(0, 1)):
    """least value of g + m + n d1 - T in (0, oo) over generators g, m in shifts, n >= 0, T in targets with
    g + m <= T, certified: the least n with n d1 > T - g - m is decided on the interval [d1lo, d1hi] (an undecided n
    raises); returns (lo, hi, g, m, n, T) for the least"""
    best = None
    for g in gens:
        for m in shifts:
            for T in targets:
                gap = T - g - m
                if gap < 0:
                    continue
                qa, qb = floor(gap / d1hi), floor(gap / d1lo)
                if gap > 0 and (qa != qb or gap / d1lo == qb or gap / d1hi == qa):
                    raise ValueError('undecided residue at g = %s' % g)
                n = qa + 1
                lo, hi = n * d1lo - gap, n * d1hi - gap
                assert lo > 0
                if best is None or hi < best[1]:
                    best = (lo, hi, g, m, n, T)
    return best


def chain_points(g, d1lo, d1hi, wlo, whi):
    """#{n >= 0 : wlo <= g + n d1 < whi}, certified"""
    def nmax(x, d):          # largest n with g + n d < x, or -1
        if x <= g:
            return -1
        q = (x - g) / d
        n = floor(q)
        return n - 1 if q == n else n
    def nmin(x, d):          # least n >= 0 with g + n d >= x
        if g >= x:
            return 0
        return int(ceil((x - g) / d))
    hi_a, hi_b = nmax(whi, d1hi), nmax(whi, d1lo)
    lo_a, lo_b = nmin(wlo, d1hi), nmin(wlo, d1lo)
    if hi_a != hi_b or lo_a != lo_b:
        raise ValueError('undecided chain count at g=%s' % g)
    return max(0, hi_a - lo_a + 1)


def ext_union(E, F):
    """III.A Definition 2.7's extended union: log orders add plus one where both sets have the exponent
    (PART-III-A-PREREQ.md:467, k(F, c) + k(Z + w, c) + 1 = k((Z + w) bar-cup F, c))"""
    out = dict(E)
    for z, k in F.items():
        out[z] = E[z] + k + 1 if z in E else k
    return out


def data_ECI(rounds, plus_one=True, top=Fr(36, 10)):
    """III.C' (3.1) (C2:247-259): E^(0) the least set of III.C Definition 3.1 containing E_0, then rounds of
    E' := least set containing E_0 bar-cup E^C_I; E_0 = {(j, 0): j >= 2} (VII (0.1)) below top"""
    E0 = {Fr(j): 0 for j in range(2, int(top) + 1)}
    E = P31.least_ECI(tuple(E0.items()), top)
    for _ in range(rounds):
        U = ext_union(E0, E) if plus_one else {**E, **{z: max(E.get(z, 0), k) for z, k in E0.items()}}
        E = P31.least_ECI(tuple(U.items()), top)
    return E


def prop21_steps(lI, eps):
    """III.I' Proposition 2.1 where III.I''''' Step 4 applies it (I6:214-218): the a priori I+-weight of u is
    min(3/2, alpha_+^sharp) - 3 eps (u^flat, I6:205-208; u_I, u_iota carry I+-expansions from 3/2), above
    l_+ := min(3/2, alpha_+^sharp) - 4 eps, so Step 1 (I2:136-152) takes no step; Step 2 (I2:154-161) integrates
    forward as in Lemma 2.2: its Step 2 (I2:95-104) one step to 3/2 + eta', eta' < (1 - e) gamma (it needs only the
    weight above 1 + eta'), and its Step 3 (I2:111-134) steps eta < 1/2 to l_I, each one application of L~ (loss 2).
    The supremum of eta' and eta are not attained: the count is 1 + the least number of steps of length < 1/2 from
    3/2 + eta' to l_I, minimised over eta' < (1 - e) gamma."""
    start = Fr(3, 2) + (1 - E_UPS) * G_UPS          # supremum of 3/2 + eta'
    span = lI - start
    q = span / Fr(1, 2)
    step3 = int(q) + 1 if q == int(q) else int(ceil(q))   # strict eta < 1/2
    if span <= 0:
        step3 = 0
    floor_ = int(floor(2 * (lI - (Fr(3, 2) - 4 * eps)))) + 1
    return 1 + step3, floor_


def dG_window(lI, delta, eps):
    """LOSS-D (2.5): d(lambda) = 6 + ceil(max(0, Re l - 2 + delta)) + ceil(max(0, Re l - 3/2) + delta)
    + 2 ceil(l_I - Re l), maximised over the iota+ window [lambda_sharp, 2 - eps) on a fine rational grid plus the
    breakpoints"""
    def d(x):
        return (6 + ceil(max(Fr(0), x - 2 + delta)) + ceil(max(Fr(0), x - Fr(3, 2)) + delta) + 2 * ceil(lI - x))
    pts = [LSHARP + (2 - eps - LSHARP) * Fr(i, 4000) for i in range(4000)]
    pts += [x for x in (lI - 1, lI - 2, 2 - delta) if LSHARP <= x < 2 - eps]
    pts += [x - Fr(1, 10 ** 15) for x in list(pts) if x - Fr(1, 10 ** 15) >= LSHARP]
    return max(d(x) for x in pts)


def counts(w):
    """the beta-chain (I15:323-324) and its loops, exactly, in units 1/D (D the lcm of the denominators); returns K,
    R2 (tf rounds at the levels below 3), R3 (level-3 rounds at the levels above 3, the top level included)"""
    keys = ('alpha', 'alpha1', 's', 'tau0', 'tau3', 'step', 'epsp')
    D = 1
    for k in keys:
        D = lcm(D, w[k].denominator)
    al, a1, s, t0, t3, st, ep = (int(w[k] * D) for k in keys)
    K = -(-(al - a1) // s)                        # beta_k = a1 + k s, k < K; beta_K = alpha
    three, two = 3 * D, 2 * D
    assert (three - a1) % s != 0                  # no level at 3
    k3 = (three - a1) // s + 1                    # the first level above 3
    assert a1 + (K - 1) * s > 4 * D and 0 < al - (a1 + (K - 1) * s) <= s < al - 4 * D
    A3 = a1 - two - t3                            # level-3 rounds: #{i : tau3 + i step <= beta - 2}
    kA = max(k3, -(A3 // s))
    n3 = (K - 1) - kA + 1
    R3 = floor_sum(n3, st, s, A3 + kA * s) + n3
    R3 += (al - two - t3) // st + 1               # the top level beta_K = alpha
    A2 = a1 - ep - t0                             # tf rounds: #{i : tau0 + i step <= beta - eps'}
    kB = max(0, -(A2 // s))
    n2 = (k3 - 1) - kB + 1
    R2 = floor_sum(n2, st, s, A2 + kB * s) + n2
    return dict(K=K, k3=k3, R2=R2, R3=R3, levels_below3=k3, levels_above3=K + 1 - k3)


def brute_counts(w):
    """the same sums level by level (for a scaled-down instance only)"""
    beta, k = [], 0
    while w['alpha1'] + k * w['s'] < w['alpha']:
        beta.append(w['alpha1'] + k * w['s'])
        k += 1
    beta.append(w['alpha'])
    R2 = R3 = 0
    for b in beta:
        if b > 3:
            x = b - 2 - w['tau3']
            R3 += int(floor(x / w['step'])) + 1 if x >= 0 else 0
        else:
            x = b - w['epsp'] - w['tau0']
            R2 += int(floor(x / w['step'])) + 1 if x >= 0 else 0
    return R2, R3, len(beta) - 1


def weights(eps_ind, eps_p, eps_K, eps, lI=Fr(13, 4), aI=Fr(13, 4), l0=Fr(7, 2)):
    eta2 = eps_p - 3 * eps                        # III.J' Lemma 1.1, read in J3 section 1: eta_2 := eps_+ - 3 eps
    eta1 = (eps_K + eta2) / 2
    alpha = 4 + eps_K
    w = dict(eps_ind=eps_ind, eps_p=eps_p, eps_K=eps_K, eps=eps, lI=lI, aI=aI, l0=l0, eta1=eta1, eta2=eta2,
             alpha=alpha, alpha1=2 + eps_K / 2, s=eps_K - eps_K / 1000, tau0=2 + eps_ind - 2 * eps,
             tau3=1 + eta2 - 2 * eps, step=eps_ind - eps, epsp=eps)
    return w


def check_weights(w):
    """the inequalities the computed data decide; returns (failures, undecided)"""
    c = [('0 < eps_K < eps_+', 0 < w['eps_K'] < w['eps_p']),
         ('eps_+ < delta_sharp', w['eps_p'] < DSHARP),
         ('eps_+ < eps_ind', w['eps_p'] < w['eps_ind']),
         ('eps_ind <= delta_50 (READ, certified lower end)', w['eps_ind'] <= DELTA50_LO),
         ('eps_+ < eps_I = a_I - 3 < 1', w['eps_p'] < w['aI'] - 3 < 1),
         ('3 + eps_+ < l_I <= a_I', 3 + w['eps_p'] < w['lI'] <= w['aI']),
         ('l_I < a_I + 1/2 (III.I\' (I\'2))', w['lI'] < w['aI'] + Fr(1, 2)),
         ('l_I in (3, l_0), l_0 in (3, 4) (VII (0.1))', 3 < w['lI'] < w['l0'] < 4),
         ('eps_+ < l_I - 3 (VI.C step (4))', w['eps_p'] < w['lI'] - 3),
         ('l_I off 3/2 + sigma_Ups', all(w['lI'] != Fr(3, 2) + s for s in SIGMA)),
         ('l_I off Re pi_1 E^C_I (least set)', w['lI'] not in P31.least_ECI()),
         ('eta_1 < eta_2 in (eps_K, eps_+)', w['eps_K'] < w['eta1'] < w['eta2'] < w['eps_p']),
         ('0 < eps < eps_ind, eps < 1/4', 0 < w['eps'] < w['eps_ind'] and w['eps'] < Fr(1, 4)),
         ('alpha in (4, 4 + eps_K]', 4 < w['alpha'] <= 4 + w['eps_K']),
         ('alpha_1 in (2, alpha - 2)', 2 < w['alpha1'] < w['alpha'] - 2),
         ('beta-step s < alpha - 4', 0 < w['s'] < w['alpha'] - 4),
         ('l_I^max = 3/2 + s_C > 100 > l_I (I2:31)', w['lI'] < 100)]
    undecided = ['(G) over the generators the record does not list: pi_1 E_++, pi_1 G, 2 + pi_1 E_col (I11:66-68)',
                 'eta_1, eta_2 off Re Lambda at W\'s ends (I12:58-60): needs Lambda',
                 'the levels admissible: off the finite exclusion sets of I11:156-160 (needs Lambda below 2)',
                 'eps, eps\' off the finite sets of I9:290-291 and I14:124-126 (roots -mu of L_b(0) hat)']
    return [n for n, ok in c if not ok], c, undecided


def main():
    ok = {}
    d1lo, d1hi = d1_interval()
    print('  W0: d1 in [%.12e, %.12e] (width %.1e); READ 3.3333305e-7: %s' % (
        float(d1lo), float(d1hi), float(d1hi - d1lo), abs(float(d1lo) - float(D1_READ)) < 1e-14))
    x = Z * Z + 4 * Z + 16
    sq = lambda n: isqrt(n) ** 2 == n
    irr = not (sq(x.numerator) and sq(x.denominator))   # sqrt(x) irrational, so d1 is (sqrt of an irrational)
    print('      z^2 + 4z + 16 = %s is not a rational square: %s, so d1 is irrational and chains from rational '
          'generators never meet' % (x, irr))
    ok['W0'] = d1hi - d1lo < Fr(1, 10 ** 40) and abs(d1lo - D1_READ) < Fr(1, 10 ** 14) and irr

    # W2: (G)
    named = [LSHARP, Fr(2), Fr(3)]
    r_named = residues(named, d1lo, d1hi)
    E = P31.least_ECI()
    ec = sorted(z for z in E if z < 3 + Fr(1, 10 ** 6))
    gens = sorted(set(named) | set(ec))
    r_all = residues(gens, d1lo, d1hi)
    print('  W2: (G), increments d1 and 1: named generators {lambda_sharp, 2, 3}: least value above 2 or 3 is %d + '
          '%.4e (from %s + %d + %d d1); LD9 G7 printed 5.02e-8' % (r_named[5], float(r_named[1]), float(r_named[2]),
                                                                   r_named[3], r_named[4]))
    print('      with the least E^C_I\'s %d points below 3 (every admissible E^C_I contains them): %d + %.4e, from '
          'g = %s + %d + %d d1' % (len(ec), r_all[5], float(r_all[1]), r_all[2], r_all[3], r_all[4]))
    deltaG = r_all[0]
    ok['W2'] = (abs(float(r_named[1]) - 5.02e-8) < 0.01e-8 and r_all[:2] == r_named[:2] and r_all[0] > DELTA50_LO)
    print('      E^C_I\'s chains lower nothing: their least residues sit near d1/2 and 3 d1/4 (1/d1 = 3000002.5...); '
          '(G) does not bind on these generators (%.4e > delta_50): %s' % (float(r_all[0]), r_all[0] > DELTA50_LO))

    # W1: the weights, eps_K below the (G) bound just found
    eps_ind = Fr(19, 10 ** 9)
    eps_p = Fr(189, 10 ** 10)
    eps_K = min(Fr(188, 10 ** 10), Fr(int(deltaG * 10 ** 13) - 1, 10 ** 13))   # below eps_+ and below delta_G
    eps = Fr(1, 10 ** 12)
    w = weights(eps_ind, eps_p, eps_K, eps)
    fails, rows, undecided = check_weights(w)
    print('  W1: eps_ind = %s, eps_+ = %s, eps_K = %s, eps = eps\' = %s, l_I = a_I = %s, l_0 = %s, eta_1 = %s, eta_2 = '
          '%s, alpha = 4 + eps_K, alpha_1 = 2 + eps_K/2, beta-step s = 0.999 eps_K' % (
              float(eps_ind), float(eps_p), float(eps_K), float(eps), w['lI'], w['l0'], float(w['eta1']),
              float(w['eta2'])))
    print('      %d inequalities decided by computed data, all hold: %s; not decidable from the record (%d): %s' % (
        len(rows), not fails, len(undecided), '; '.join(undecided)))
    ok['W1'] = not fails and w['eps_K'] < deltaG

    # W3: the counts
    c = counts(w)
    floor_d = 3 * (c['R2'] + c['R3'])
    print('  W3: beta-levels K = %d (%d below 3, %d above); tf rounds below 3 R2 = %d; level-3 rounds above 3 R3 = %d'
          % (c['K'], c['levels_below3'], c['levels_above3'], c['R2'], c['R3']))
    print('      floor: d >= 3 (R2 + R3) = %d = %.4e; N = 21 d + 6 >= %.4e; against LOSS-D\'s 7.959e15 at eps_ind -> '
          'delta_50 without (G): x %.2f' % (floor_d, floor_d, 21 * floor_d + 6, floor_d / 7.959e15))
    est = Fr(1, 2) / (w['eps_K'] * w['step']) * 2 * 3
    ok['W3'] = abs(Fr(floor_d) / est - 1) < Fr(1, 100) and floor_d > 7.959e15
    # W3 control: floor_sum against brute force on a scaled-down instance
    ws = weights(Fr(19, 10 ** 3), Fr(189, 10 ** 4), Fr(17, 10 ** 3), Fr(1, 10 ** 6))
    cs = counts(ws)
    b2, b3, bK = brute_counts(ws)
    ok['W3c'] = (cs['R2'], cs['R3'], cs['K']) == (b2, b3, bK)
    print('      control: exact floor-sum = level-by-level sum on a scaled instance (eps_K = 0.017): R2 %d = %d, '
          'R3 %d = %d, K %d = %d' % (cs['R2'], b2, cs['R3'], b3, cs['K'], bK))

    # W4: per-level ceilings
    iota = int(ceil((2 - eps - LSHARP) / d1lo))
    assert iota == int(ceil((2 - eps - LSHARP) / d1hi))
    Nstar = int(ceil(5 / d1lo)) + 2
    assert Nstar == int(ceil(5 / d1hi)) + 2
    wlo, whi = 2 + w['eta1'], 3 + w['eta2']
    starts = sorted({g + m for g in named for m in (0, 1) if g + m < whi})
    cnt_named = sum(chain_points(g, d1lo, d1hi, wlo, whi) for g in starts)
    # Round 2 (verifier, R2-V1): the chains already started are `starts` (named generators and their +1 shifts), and
    # lambda_sharp + 1 = 2.5099 lies in the least E^C_I as well; round 1 excluded only `named` here and counted that
    # chain twice. Exclude every start, and check the count on the deduplicated union of all chain starts.
    extra = [g for g in ec if g not in starts]
    cnt_ec = sum(chain_points(g, d1lo, d1hi, wlo, whi) for g in extra)
    union = sorted(set(starts) | {g for g in ec if g < whi})
    cnt_union = sum(chain_points(g, d1lo, d1hi, wlo, whi) for g in union)
    extra_r1 = [g for g in ec if g not in named]                    # round 1's list (the double count)
    cnt_r1 = sum(chain_points(g, d1lo, d1hi, wlo, whi) for g in extra_r1)
    dup = sorted(set(extra_r1) & set(starts))
    lev3 = (Fr(1, 2) / w['step'])
    print('  W4: iota+ rounds per level below 3 <= ceil((2 - eps - lambda_sharp)/d1) = %d (LD14: 1,470,302); N_* = '
          'ceil(5/d1) + 2 = %d' % (iota, Nstar))
    print('      level-2 container per level above 3, |Lambda\' cap W|, W = [2 + eta_1, 3 + eta_2): named generators '
          '%d (LD15: 7,470,307); E^C_I\'s %d further chains add %d: %d, %.2f x a level\'s mean level-3 rounds %.4e' % (
              cnt_named, len(extra), cnt_ec, cnt_named + cnt_ec, float((cnt_named + cnt_ec) / lev3), float(lev3)))
    ok['W4'] = (iota == 1470302 and cnt_named == 7470307 and cnt_ec > 0 and cnt_union == cnt_named + cnt_ec
                and len(union) == len(starts) + len(extra))
    print('      deduplicated union of the chain starts: %d starts, %d points = named %d + E^C_I %d (control on the '
          'union); '
          'round 1 listed %d E^C_I chains, counting %s (lambda_sharp + 1) twice: %d points per level' % (
              len(union), cnt_union, cnt_named, cnt_ec, len(extra_r1), [float(x) for x in dup], cnt_named + cnt_r1))
    ok['N5'] = cnt_named + cnt_r1 != cnt_union and len(dup) == 1
    print('  N5 (control): round 1\'s list (E^C_I minus the named generators only) does not match the union: %s' %
          ok['N5'])

    # W5: the log terms of the data's E^C_I
    lI = w['lI']
    E_free = P31.least_ECI()
    base = P31.chain(E_free, lI)
    R0 = data_ECI(1)
    R1 = {M: data_ECI(M) for M in (4, 7)}
    logs0 = sorted((z, k) for z, k in R0.items() if z <= lI and k > 0)
    ch0 = P31.chain(R0, lI)
    ch1 = {M: P31.chain(E1, lI) for M, E1 in R1.items()}
    print('  W5: control, E_0 empty: (J, log steps, applications) = %s, loss %d (prop31loss5 Q2)' % (base,
                                                                                                      2 * base[2]))
    print('      E_0 = {(j, 0): j >= 2}, one corner union (R0): %d exponents below l_I carry logs, max log order %d at '
          '%s; (J, L, applications) = %s, loss %d' % (len(logs0), max(k for _, k in logs0),
                                                     [float(z) for z, k in logs0 if k == max(k for _, k in logs0)],
                                                     ch0, 2 * ch0[2]))
    for M in (4, 7):
        print('      as written, M = %d rounds of III.C\' (3.1) (R1; M = 4 at eta = 9/20, 7 the bound 4(l_I - '
              'l_flat_I) + 1): (J, L, applications) = %s, loss %d' % (M, ch1[M], 2 * ch1[M][2]))
    nolog = data_ECI(4, plus_one=False)
    ok['W5'] = (base == (2, 0, 3) and ch0[1] > 0 and all(ch1[M][1] >= ch0[1] for M in ch1)
                and P31.chain(nolog, lI)[1] == 0)

    # W6: Proposition 2.1's count
    st, fl = prop21_steps(lI, eps)
    print('  W6: III.I\' Proposition 2.1 at I6:216, l_I = %s: %d steps, loss %d (floor %d steps, %d: LD16 D582)' % (
        lI, st, 2 * st, fl, 2 * fl))
    ok['W6'] = (st, fl) == (5, 4)

    # W7: elementary losses
    dG = dG_window(lI, eps / 2, eps)
    l22 = 2 * int(ceil(lI)) + 10
    supd = max(7 + 2 * int(ceil(lI - (Fr(3, 2) - Fr(1, 10 ** 9)))), 12)
    print('  W7: d_G = %d on the iota+ window; III.G\'\'\' Lemma 2.2 l = %d, Proposition 2.4 l\' = l + sup d = %d; '
          'an iota+ round 4 + d_G = %d (l_I < 3.5); Corollary 3.4\'s l = 1, a tf round 3 (READ, thetain5 T4)' % (
              dG, l22, l22 + supd, 4 + dG))
    ok['W7'] = (dG, l22, l22 + supd) == (11, 18, 30)

    # W8: the composition (1.1), conditional on H1-H4 (CONSTANTS5.md D2.6), every count above exact
    above, below = c['levels_above3'], c['levels_below3']
    oneoff = 2 * ch1[7][2]
    dcond = (3 * (c['R2'] + c['R3']) + 3 * (cnt_named + cnt_ec) * above + (4 + dG) * iota * below
             + (2 * st + oneoff) * below)
    print('  W8 (conditional on H1-H4): d <= %d + (K + 1) c = %.4e + %d c, c the per-level loss of the steps not '
          'counted (FWD, BG, FIN, INT, III.I\'\'\'\'\'\'\'\'\'\'\'s windows (<= N_* = %d per call), the pairs '
          'of III.I\'\'\'\'\'\'\'\'\'\'\'\', Lambda_* of III.J\'); terms: rounds %.3e, level-2 container %.3e, '
          'iota+ %.3e, Proposition 2.1 and the one-off application %.3e' % (
              dcond, dcond, c['K'] + 1, Nstar, 3 * (c['R2'] + c['R3']), 3 * (cnt_named + cnt_ec) * above,
              (4 + dG) * iota * below, (2 * st + oneoff) * below))
    ok['W8'] = floor_d < dcond < 3 * floor_d

    # negative controls
    bad = weights(eps_ind, eps_ind, eps_K, eps)
    n1 = check_weights(bad)[0]
    ok['N1'] = bool(n1)
    print('  N1 (control): eps_+ = eps_ind rejected by: %s' % n1)
    wrong = sum(int(floor((ws['alpha1'] + k * ws['s'] - 2 - ws['tau3']) / ws['step'])) for k in range(cs['k3'],
                                                                                                     cs['K']))
    ok['N2'] = wrong != cs['R3']
    print('  N2 (control): the level-3 sum without its +1 per level and without the top level: %d != %d' % (
        wrong, cs['R3']))
    ok['N3'] = P31.chain(nolog, lI)[1] == 0 and ch0[1] > 0
    print('  N3 (control): the extended union without its +1 gives no log below l_I (L = %d), with it L = %d' % (
        P31.chain(nolog, lI)[1], ch0[1]))
    st2, _ = prop21_steps(Fr(36, 10), eps)
    dG2 = dG_window(Fr(36, 10), eps / 2, eps)
    ok['N4'] = st2 != st and dG2 != dG
    print('  N4 (control): l_I = 3.6 gives %d steps and d_G = %d' % (st2, dG2))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
