#!/usr/bin/env python3
"""lambdagen5: Lambda's three unlisted generators (I11 Definition 1.1) at n = 4, and what they do to (G) and to the
level-2 container (CONSTANTS5.md, Round 2, item (ii)).

Lambda is the least conjugation-closed set containing pi_1(E_++ u G u E^C_I) u {lambda_sharp, 3} u (2 + pi_1 E_col) and
closed under + w, w in Inc := pi_1(E_ind u E^iota_ind) u {1} (PART-III-I11-SPACETIME.md:66-71). Round 1 counted the
chains of {lambda_sharp, 2, 3} and of the least E^C_I with the increments d1 and 1 (dweights5.py W2, W4) and left
E_++, G and E_col open. Labels: READ (the cited lines), deduced, computed (exact rationals; d1, d0 and the sl offsets in
certified intervals, mpmath.iv at 200 bits; floating point where said).

  L1 (deduced; READ I9:37-46, I11:127-134, I2:177-190) E_++. The least choice of III.I'''''''' (1.1) agrees below
     2 lambda_sharp = 3.0198 with the least index set containing E^sharp_+ cap {Re < 2} and closed under
     + (E^iota_ind u E_ind) (I11 Lemma 1.2 (b)'s proof; the other closures land at real part >= 2 lambda_sharp), and
     E^sharp_+ = {lambda_sharp} u pi_1 E^C_I by III.I' (3.2) with breve E_+ empty. So pi_1 E_++ cap {Re < 3.0198} =
     ({lambda_sharp} u (pi_1 E^C_I cap {Re < 2})) + N_0 Inc: its bases are generators of Lambda already, and Lambda is
     closed under the same increments. E_++ adds no chain. Computed: the least E^C_I has no point below 2 (its least
     point is 2), so E_++ below 3.0198 is the chain of lambda_sharp alone.
  L2 (deduced; READ I8:37-41) G = (2, 0) u (2 + E_ind): pi_1 G lies in the chain of 2. No chain added.
  L3 (deduced; READ I12:79-110) E_col. The column terms' F(s, x) is a finite sum of phi(s) s^m r^(4 - k + m) (Q w_m)(x),
     m in {0, 1}, k in {0, 1, 2}, Q in rho^q Diff_b (q >= 0), w_m with index sets (2, 0) u (2 + E_ind), (3, 0) u
     (3 + E_ind) or the tower's (contained in E_ind); so its exponents are e_w + sigma, sigma = q - 4 + k - m >= -5, and
     E_col keeps those of real part >= 0. Hence 2 + pi_1 E_col lies in {2, 3, ...} u {e - 1 + j : e in pi_1 E_ind,
     j >= 0}: a base that is not a chain of 2 or 3 needs an exponent of E_ind whose fractional part is not an integer
     combination of the increments below 1. With the record's computed roots (LOSS-D LD9; gapsums5.py: d1 = delta_1,
     1 + d0, the sl roots entering as (l - 1) + delta_l and l + delta'_l) the candidate new bases in W's range are
     2 + d0, 2 + delta_l (l = 2, 3, 4), 3 + delta_5, 2 + delta'_l (l = 1, 2, 3) and 3 + delta'_4. Whether their
     coefficients are non-zero the record does not decide; for an upper bound on d they must be admitted.
  L4 (certified) (G) with L3's bases admitted: the least value above 2 or 3 over their chains (increments d1 and 1),
     against eps_ind <= delta_50 = 1.94137e-8 and round 1's eps_K = 1.88e-8.
  L5 (certified) the level-2 container |Lambda cap W| per level above 3 with L3's bases (on round 1's weights), and the
     change it makes to the conditional bound W8.
  L6 (deduced; READ I11:369-386, I12:63-66) the windows of III.I'''''''''' Proposition 3.1 (b)'s Step 2 run at every
     level, those above 3 included ("the new point is alpha <= 4 + eps_K", I11:347); there are at most
     ceil((2 - eps - lambda_sharp)/d1) = 1,470,302 per call (each of width >= eta_0 = d1 below 2, I11:103-104), each an
     iota+ round (one III.G'' Corollary 4.3 and one III.I' Proposition 3.1, charged 4 + d_G = 15 as in dweights5.py
     W7). Round 1's H2 charged them below 3 only; above 3 they add 15 x 1,470,302 x 53,244,736 (computed).
  L7 (deduced; READ J2:95-145, I13:234-266) two of round 1's uncounted steps cost no derivatives: the exponents of
     Lambda_* in III.J' are an induction in the proof that D_U Phi is injective (no map is built), and the pairs of
     III.I'''''''''''' Lemma 2.4 are removed by subtracting explicit tensors chi_K T_rho(a Y) with coefficients read off
     the expansion (linear and bounded at fixed index sets, no order spent). They enter C_k only.
  Controls (must fail, and do): N1 a planted base 3 - n d1 + 1e-8 (n large) is caught by L4's search; N2 with the
  shift bound -4 in place of -5 the bases 2 + delta_4, 3 + delta_5 and 3 + delta'_4 drop out, so L3's list depends on
  the bound read at I12:93-96; N3 the container counted without deduplicating L3's bases against round 1's starts
  differs.

    python3 checks/lambdagen5.py
"""
import os
import sys
import textwrap
from fractions import Fraction as Fr
from math import ceil

import mpmath
from mpmath import iv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dweights5 as DW  # noqa: E402  (round 1's instrument: d1, residues, chain counts, weights)
import prop31loss5 as P31  # noqa: E402

iv.prec = 200
Z = Fr(4, 10 ** 6)
DELTA50 = Fr(1941370568, 10 ** 17)


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def to_fr_interval(x):
    """an iv interval as a pair of Fractions (exact endpoints)"""
    lo = mpmath.mpf(x._mpi_[0])
    hi = mpmath.mpf(x._mpi_[1])
    return Fr(*lo.as_integer_ratio()) if hasattr(lo, 'as_integer_ratio') else Fr(str(lo)), \
        Fr(*hi.as_integer_ratio()) if hasattr(hi, 'as_integer_ratio') else Fr(str(hi))


def mpf_fr(x):
    m, e = mpmath.mpf(x).man_exp
    return Fr(int(m)) * Fr(2) ** int(e)


def ivfr(x):
    return mpf_fr(x._mpi_[0] and mpmath.mpf(x._mpi_[0])), mpf_fr(mpmath.mpf(x._mpi_[1]))


def sl_offsets_iv(l):
    """delta_l, delta'_l (certified): the sl roots 1/2 + (1/4 + s)^(1/2), s the roots of Q_l(s) = s^2 - (2 + 2 kappa +
    z) s + kappa (kappa + 1) + z kappa, kappa = l (l + 2) (GAUGEPOT:200-206, as gapsums5.py sl_offsets)"""
    z = iv.mpf(Z.numerator) / Z.denominator
    k = l * (l + 2)
    b, c = 2 + 2 * k + z, k * (k + 1) + z * k
    disc = iv.sqrt(b * b - 4 * c)
    lam = [iv.mpf(1) / 2 + iv.sqrt(iv.mpf(1) / 4 + s) for s in ((b - disc) / 2, (b + disc) / 2)]
    return lam[0] - (l + 1), lam[1] - (l + 2)


def d0_iv():
    z = iv.mpf(Z.numerator) / Z.denominator
    return (1 + iv.sqrt(9 + 4 * z)) / 2 - 2


def frpair(x):
    lo, hi = mpmath.mpf(x._mpi_[0]), mpmath.mpf(x._mpi_[1])
    return mpf_fr(lo), mpf_fr(hi)


def ecol_bases(shift_min=-5):
    """L3: the candidate bases e - 1 + j (>= 2, < 3 + 1/10) from E_ind's computed exponents e, which enter F through
    the classes 2 + E_ind (j >= 0 with e + 2 + sigma >= 0, sigma >= shift_min); returned as (name, lo, hi)"""
    out = []
    d0 = frpair(d0_iv())
    exps = [('1 + d0', (1 + d0[0], 1 + d0[1]))]
    for l in range(1, 8):
        dl, dpl = sl_offsets_iv(l)
        exps.append(('(l-1) + delta_%d' % l, tuple(l - 1 + x for x in frpair(dl))))
        exps.append(('l + delta\'_%d' % l, tuple(l + x for x in frpair(dpl))))
    for name, (lo, hi) in exps:
        # exponents of F: 2 + e + sigma, sigma >= shift_min, kept at real part >= 0; base = 2 + that
        n_int = int(lo)                                       # integer part of e (lo and hi share it here)
        assert int(hi) == n_int
        frac = (lo - n_int, hi - n_int)
        least_exp_int = max(0, 2 + n_int + shift_min)         # the least integer part an F-exponent can keep
        base_int = 2 + least_exp_int
        for bi in range(max(base_int, 2), 4):
            out.append((name, bi + frac[0], bi + frac[1]))
    return out


def main():
    ok = {}
    d1lo, d1hi = DW.d1_interval()
    E = P31.least_ECI()
    below2 = sorted(z for z in E if z < 2)
    named = [DW.LSHARP, Fr(2), Fr(3)]
    ok['L1'] = below2 == []
    say('  L1: the least E^C_I has %d points below 2 (least point %s): E^sharp_+ cap {Re < 2} = {lambda_sharp}, and '
        'E_++ below 2 lambda_sharp = 3.0198 is lambda_sharp + N_0 Inc, a chain Lambda has already: no base added'
        % (len(below2), min(E)))
    say('  L2: G = (2, 0) u (2 + E_ind) lies in the chain of 2: no base added')

    bases = ecol_bases()
    new = [b for b in bases if b[2] < 3 + Fr(1, 10)]
    w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))
    wlo, whi = 2 + w['eta1'], 3 + w['eta2']
    in_w = [b for b in new if b[1] < whi]
    say('  L3: candidate bases from E_col with the record\'s computed roots (certified intervals): %s' % '; '.join(
        '%s -> %.10f' % (n, float(lo)) for n, lo, hi in in_w))

    # L4: (G) over these bases' chains: least value above 2 or 3 (increments d1 and 1), certified on intervals
    best = None
    for name, lo, hi in in_w:
        for T in (2, 3):
            for m in (0, 1):
                gap_lo, gap_hi = T - hi - m, T - lo - m
                if gap_hi < 0:
                    if lo + m > T:                              # the base itself is above T
                        val = (lo + m - T, hi + m - T)
                        if best is None or val[1] < best[1][1]:
                            best = (name, val, T, m, 0)
                    continue
                if gap_lo < 0:
                    continue
                qa, qb = int(gap_lo / d1hi), int(gap_hi / d1lo)
                if qa != qb:
                    raise ValueError('undecided at %s' % name)
                n = qa + 1
                val = (lo + m + n * d1lo - T, hi + m + n * d1hi - T)
                assert val[0] > 0
                if best is None or val[1] < best[1][1]:
                    best = (name, val, T, m, n)
    r_old = DW.residues(sorted(set(named) | {z for z in E if z < 3 + Fr(1, 10 ** 6)}), d1lo, d1hi)
    binds = best[1][0] < DELTA50
    ok['L4'] = best is not None and not binds and best[1][0] > w['eps_K']
    say('  L4: (G) over L3\'s bases: least value above %d is %.4e (from %s, + %d + %d d1); round 1\'s generators give '
        '%.4e; eps_ind <= delta_50 = 1.9414e-8: (G) %s on these bases' % (
            best[2], float(best[1][0]), best[0], best[3], best[4], float(r_old[0]),
            'binds' if binds else 'does not bind'))

    # L5: the container per level above 3 with L3's bases, deduplicated against round 1's starts
    starts = sorted({g + m for g in named for m in (0, 1) if g + m < whi})
    ec = sorted(z for z in E if z < 3 + Fr(1, 10 ** 6))
    union_r1 = sorted(set(starts) | {g for g in ec if g < whi})
    cnt_r1 = sum(DW.chain_points(g, d1lo, d1hi, wlo, whi) for g in union_r1)
    add = 0
    seen = []
    for name, lo, hi in in_w:
        # a base is a new chain unless it differs from an existing start by a multiple of d1 (impossible: rational
        # starts, irrational offsets) -- the offsets are irrational (not rational squares), so each is new
        c_lo = DW.chain_points(lo, d1lo, d1hi, wlo, whi)
        c_hi = DW.chain_points(hi, d1lo, d1hi, wlo, whi)
        assert c_lo == c_hi
        add += c_lo
        seen.append((name, c_lo))
    c = DW.counts(w)
    above = c['levels_above3']
    say('  L5: container per level above 3: round 1 (corrected) %d; L3\'s %d bases add %d (%s): %d; over the %d levels '
        'above 3 at 3 per point the conditional bound grows by %d = %.4e' % (
            cnt_r1, len(in_w), add, ', '.join('%d' % x for _, x in seen), cnt_r1 + add, above, 3 * add * above,
            3 * add * above))
    ok['L5'] = cnt_r1 == 52025761 and add > 0

    # L6: the windows above 3
    iota = int(ceil((2 - w['eps'] - DW.LSHARP) / d1lo))
    assert iota == int(ceil((2 - w['eps'] - DW.LSHARP) / d1hi))
    win = 15 * iota * above
    say('  L6: windows of III.I\'\'\'\'\'\'\'\'\'\' Proposition 3.1 (b) per call <= %d; at the %d levels above 3, 15 per '
        'window: %d = %.4e, not in round 1\'s W8' % (iota, above, win, win))
    ok['L6'] = iota == 1470302

    w8 = 17892090290788934                                   # dweights5.out W8 (corrected, round 2)
    new_bound = w8 + 3 * add * above + win
    say('  L8: the conditional bound (H1-H4 with H1 widened to admit L3\'s bases and H2 to the windows above 3): d <= '
        '%d + %d c = %.4e + %.4e c' % (new_bound, c['K'] + 1, new_bound, c['K'] + 1))
    ok['L8'] = new_bound > w8

    # controls
    planted = 3 - 2900000 * d1lo + Fr(1, 10 ** 8)
    gap = 3 - planted
    n = int(gap / d1lo) + 1
    v_ = planted + n * d1lo - 3
    ok['N1'] = 0 < v_ < Fr(2, 10 ** 8) and v_ < DELTA50
    say('  N1 (control): a planted base 3 - 2,900,000 d1 + 1e-8 reaches 3 + %.3e < delta_50: the search catches a '
        'binding base' % float(v_))
    b4 = {n for n, lo, hi in ecol_bases(-4) if hi < 3 + Fr(1, 10)}
    b5 = {n for n, lo, hi in ecol_bases(-5) if hi < 3 + Fr(1, 10)}
    ok['N2'] = b4 != b5
    say('  N2 (control): shift bound -4 in place of -5 drops %s' % sorted(b5 - b4))
    double = sum(DW.chain_points(g, d1lo, d1hi, wlo, whi) for g in list(starts) + [g for g in ec if g < whi])
    ok['N3'] = double != cnt_r1
    say('  N3 (control): starts and E^C_I counted without deduplication: %d != %d' % (double, cnt_r1))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
