"""lambdacount5.py -- the level-2 rounds through the record's own Lambda (LOSS-D LD15, D550).

LD13 (D529, D531) counted the level-2 rounds of III.I(11) Step 3 per chain, at most 3,000,003 on LD9's reading, and
left two factors open: (c) N_2, the number of g_2's tf-exponents in the window, which "the record does not bound", and
(d) the log orders, a round being per (alpha_0, k). The record bounds both, through III.I'''''''''' (I11) Definition 1.1
and Lemma 1.2:

  Lambda is the smallest set, closed under conjugation, containing pi_1(E_++ u G u E^C_I) u {lambda_sharp, 3} u (2 +
  pi_1 E_col) with Lambda + w in Lambda for w in pi_1(E_ind u E^iota_ind) u {1} (I11:66-72); 2 is in it (I11:155).
  Lemma 1.2 (c): every exponent (lambda, k) produced with 2 <= Re lambda <= 3 + eps_+ has lambda in Lambda and k <=
  K(lambda) := L_0 + (N_* + 1)(l_* + 1)(n(lambda) + 1), N_* := ceil(5/eta_0) + 2, eta_0 := min Re of the increments,
  n(lambda) := #{lambda' in Lambda : Re lambda' < Re lambda} (I11:72-79, 96-107).
  Level 2's window, in u-exponents, is W = [2 + eta_1, 3 + eta_2): I12:58-60 chooses eta_1, eta_2 so that no lambda in
  Lambda has real part at either end, the tf-window [1 + eta_1, 2 + eta_2) shifted by one.

So chains merge (a chain's points alpha_0 + n d1 lie in Lambda) and a level's level-2 rounds number at most |Lambda cap
W| (one per exponent) or the sum over Lambda cap W of K(lambda) + 1 (one per exponent and log order). Lemma 1.2 (a) makes
these finite; the record does not number them, since E_++, G, E^C_I and E_col are not listed. This script counts the
part of Lambda the record names and computes, at the record's point z = 4e-6, on the construction's reading (D542-D544:
E_ind and E^iota_ind meet (0, 1) in {d1} alone, A != 0, so d1 is an increment and eta_0 = d1).

  C1 (exact, 40 digits) lambda_sharp = 3/2 + (1 - e_Ups) gam_Ups = 1.5099 (e_Ups = gam_Ups = 1/100), d1 (LD9, from
     level2loop5), N_* = ceil(5/d1) + 2.
  C2 Lambda_0 := the generators lambda_sharp, 2, 3 with the increments d1 and 1, a subset of Lambda. Its points in W:
     the chains lambda_sharp + n d1, lambda_sharp + 1 + n d1, 2 + n d1 and the point 3; no two chains share a point
     (no difference of bases is a multiple of d1 to 1e-25); the count is the same at (eta_1, eta_2) = (1e-30, 2e-30),
     (delta_50/3, delta_50/2) and (delta_50/2, 0.999 delta_50), eta_1 < eta_2 as I12:58 asks (eta_1, eta_2 lie in
     (eps_K, eps_+), below delta_50; verifier 239: the count is fixed for eta_1 < 2.45e-7, eta_2 < 5.02e-8). So
     |Lambda cap W| >= |Lambda_0 cap W|.
  C3 the same with LD9 G7's increments 1 + d0, 1 + delta_2, 1 + delta'_1 added (at most one increment of integer part
     >= 1 reaches W from a generator >= 3/2), on LD9's reading that they lie in E_ind.
  C4 against one beta-level's level-3 rounds, on average 1/(2 eps_ind) >= 1/(2 delta_50) = 2.5755e7 (LD11): the ratios
     are at eps_ind = delta_50 and fall as eps_ind for smaller eps_ind, the container not depending on it (D554).
  C5 the log ceiling: n(lambda) >= the number of Lambda_0's points below W (lambda_sharp + n d1 < 2, and 2), so on W
     K(lambda) >= 1 + (N_* + 1)(n(lambda) + 1) (L_0 >= 1, l_* >= 0), and the sum over Lambda_0 cap W of K + 1, the ranks
     there being consecutive, a count of rounds per (alpha_0, k), against the counted loops' 1.3266e15 rounds (LD11;
     their loss is 2.65e15; corrected D554, verifier 239).
  Control: 1/d1 is not an integer (so lambda_sharp + 1 is not on lambda_sharp's chain), and with eta_0 = 1 (no
     increment below 1) N_* would be 7.

Labels: computed (exact decimal arithmetic) and deduced (the reading of I11 and I12 above).

    python3 checks/lambdacount5.py
"""
import sys
from decimal import Decimal, getcontext, ROUND_CEILING, ROUND_FLOOR

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import level2loop5 as L2                                                          # noqa: E402

getcontext().prec = 60


def ceil(x):
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def floor(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def chain(base, d1, lo, hi):
    """the n >= 0 with lo <= base + n d1 < hi: (first, last) or None"""
    n0 = max(0, ceil((lo - base) / d1))
    n1 = ceil((hi - base) / d1) - 1
    return (n0, n1) if n1 >= n0 else None


def count(bases, d1, lo, hi):
    tot = 0
    for b in bases:
        c = chain(b, d1, lo, hi)
        tot += 0 if c is None else c[1] - c[0] + 1
    return tot


def main():
    ok = True

    def check(name, cond, msg):
        nonlocal ok
        print(f'  {name} {"PASS" if cond else "FAIL"}: {msg}')
        ok = ok and cond

    # C1
    d0 = L2.s0_root() - 2
    l1a, l1b = L2.sl_roots(1)
    d1, dp1, de2 = l1a - 2, l1b - 3, L2.sl_roots(2)[0] - 3
    de50 = L2.sl_roots(50)[0] - 51
    ls = Decimal(3) / 2 + (1 - Decimal('0.01')) * Decimal('0.01')
    Nstar = ceil(5 / d1) + 2
    print(f'  lambda_sharp = {ls}, d1 = {d1:.10e}, 1/d1 = {1 / d1:.6f}, N_* = ceil(5/d1) + 2 = {Nstar:,}')
    check('C1', ls == Decimal('1.5099') and abs(d1 - Decimal('3.3333305e-7')) < Decimal('1e-14') and Nstar == 15000015,
          'lambda_sharp = 1.5099, d1 = 3.3333305e-7 (LD9), N_* = 15,000,015')

    # C2
    two, three = Decimal(2), Decimal(3)
    bases0 = [ls, ls + 1, two, three]
    counts = {}
    for e1, e2 in ((Decimal('1e-30'), Decimal('2e-30')), (de50 / 3, de50 / 2), (de50 / 2, de50 * Decimal('0.999'))):
        lo, hi = two + e1, three + e2
        per = [chain(b, d1, lo, hi) for b in bases0]
        # 3 is 2's chain + 1 and a generator: count it once (2 + n d1 never equals 3, 1/d1 not an integer)
        counts[(e1, e2)] = (per, count(bases0, d1, lo, hi))
    per, n0 = counts[(Decimal('1e-30'), Decimal('2e-30'))]
    same = len({v[1] for v in counts.values()}) == 1

    def distinct(bases):
        for i in range(len(bases)):
            for j in range(i + 1, len(bases)):
                q = abs(bases[i] - bases[j]) / d1
                f = q - floor(q)
                if f < Decimal('1e-25') or 1 - f < Decimal('1e-25'):
                    return False
        return True
    dis0 = distinct(bases0)
    print('    Lambda_0 in W: lambda_sharp + n d1, n = %s..%s (%s); lambda_sharp + 1 + n d1, n = %s..%s (%s); 2 + n d1, '
          'n = %s..%s (%s); 3 (%s)' % (tuple(x for c in per for x in (f'{c[0]:,}', f'{c[1]:,}', f'{c[1] - c[0] + 1:,}'))[:9]
                                       + (f'{per[3][1] - per[3][0] + 1}',)))
    check('C2', dis0 and same and n0 == sum(c[1] - c[0] + 1 for c in per),
          f'|Lambda_0 cap W| = {n0:,}, the same at the three (eta_1, eta_2) tested; no shared points')

    # C3
    bases1 = bases0 + [ls + 1 + d0, ls + 1 + de2, ls + 1 + dp1]
    n1 = count(bases1, d1, two + de50 / 2, three + de50 / 2)
    check('C3', distinct(bases1) and n1 > n0,
          f"with LD9 G7's increments 1 + d0, 1 + delta_2, 1 + delta'_1: {n1:,} (each adds "
          f"{count([ls + 1 + d0], d1, two, three):,})")

    # C4
    lvl3 = 1 / (2 * de50)
    r0, r1 = n0 / lvl3, n1 / lvl3
    print(f'    one beta-level\'s level-3 rounds, on average 1/(2 delta_50) = {lvl3:.5e}; ratios {r0:.4f} and {r1:.4f}; '
          f'one more chain of {floor(1 / d1) + 1:,} points adds {(floor(1 / d1) + 1) / lvl3:.4f}')
    check('C4', Decimal('0.28') < r0 < Decimal('0.30') and Decimal('0.45') < r1 < Decimal('0.47'),
          'at eps_ind = delta_50 the named part of Lambda already gives 0.29 (0.46) of a level\'s level-3 rounds, '
          'less for smaller eps_ind: the record\'s container leaves "shorter" to the unlisted generators')

    # C5
    below = count([ls], d1, Decimal(0), two) + 1                 # lambda_sharp + n d1 < 2, and the point 2
    kmin = 1 + (Nstar + 1) * (below + 1)
    # the sum over Lambda_0 cap W of K + 1 >= sum of 2 + (N_* + 1)(rank + 1), ranks below .. below + n0 - 1
    ranks = n0 * below + n0 * (n0 - 1) // 2
    ksum = 2 * n0 + (Nstar + 1) * (ranks + n0)
    print(f'    n(lambda) >= {below:,} on W; K(lambda) >= {kmin:,} = {Decimal(kmin):.5e}; sum over Lambda_0 cap W of '
          f'K + 1 >= {Decimal(ksum):.5e}')
    check('C5', below == 1470303 and Decimal(kmin) > Decimal('2.2e13') and Decimal(ksum) > Decimal('1.3266e15'),
          'the record\'s log ceiling is above 2.2e13 at every exponent of W, and its per-(alpha_0, k) count of one '
          'level\'s level-2 rounds above the counted loops\' 1.3266e15 rounds in total (their loss 2.65e15)')

    # control
    q = 1 / d1
    check('Ctl', q - floor(q) > Decimal('0.1') and ceil(Decimal(5) / 1) + 2 == 7,
          f'1/d1 = {q:.4f} is not an integer; with eta_0 = 1, N_* = 7')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
