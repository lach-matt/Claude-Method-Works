#!/usr/bin/env python3
"""eflat5: the log orders of E^flat that the construction of III.I'''''''''' Proposition 3.1 writes, from the
write-out's own steps, and what they do to the ceiling on d (CONSTANTS5.md, Round 5, R5.2). Labels: computed (exact:
Fractions; the offsets d0, d1, delta'_1 from dceiling5.py's certified census), deduced (the reading of the cited lines,
stated with each item), READ (cited lines).

The record bounds E^flat's log order at lambda by K(lambda) = L_0 + (N_* + 1)(l_* + 1)(n(lambda) + 1) (I11:339-343,
I11:72-80), which allows a raise in every one of N_* windows at every exponent; that bound is what puts the ceiling at
1e31 (R3.3 D5-D6). Here the construction is followed step by step instead (I11:350-387; III.I' (3.2), I2:165-177;
III.G'' Corollary 4.3, G3:375-400):

  F1 (exact) III.A Lemma 1.4 at the box^Ups sites behind E_ind and E^iota_ind, block by harmonic type at b0 (the
     indicial family at the boundary preserves types, D4:85-87; the sources are of one type each: F4 Lemma 1.1, D3
     (3.4)): s0 with F = (1, 0) (III.F''' Proposition 2.2, mu-dot), v1 with (2, 0) (A-dot; III.D'' rotations), s1 with
     (2, 0) (III.D'' translations, (F1) at k = 2) and with (1, 0) (the boosts). Block roots with real part > 0 (D3:40-44,
     dceiling5.py D1): s0 {2 + d0, 3}, s1 {2 + d1, 3 + delta'_1, 4}, v1 {3}. E_ind of a site is E' - k. Printed: the
     offsets below 1 (block-wise {d1}: the construction reading of LD14, now computed), the log orders at offsets in (0,
     3 + eps_+ - lambda_sharp] (the ones Step 2 adds to an exponent below 2), the largest log order at real part <= 5
     (10, at 5, from v1 with k = 2: round 4's M5 reproduced on the block reading).
     Also the literal reading, E(alpha) from every type's roots (iotapoles5.py M5's choice): there the offsets below 1
     are {d0, d1}, the widest reading of R3.3 D3, under which (G) binds and the floor moves. So M5's log order 10 holds
     on both readings, but M5's root set is not the narrowest reading it names. On that reading too the log orders at
     Step 2's offsets are <= 2 (what changes there is Lambda, not the log orders).
  F2 (exact) the towers of III.D''' (Lemma 2.1, D4:76-100: Lemma 1.5's formal solutions, logarithms where m + n meets a
     root, then Lemma 1.4 above 2 + d1): for each class root mu of D4 (R4) of type tau, mu + 1 is not a type-tau root, so
     a tower's offset 1 carries log order 0; its other offsets in (0, 1.4901] are none (Lemma 1.4's part starts at
     2 + d1 - m >= 2 + d1).
  F3 (deduced; exact check) below 2 every exponent has log order 0: Step 2 treats u-exponents of real part < 2 in
     increasing order (I11:357-361); those are the chain of lambda_sharp under the offsets of E^iota_ind cup E_ind
     below 2 - lambda_sharp = 0.4901 ("the exponents below 2 lie in pi_1 M with the log orders of E_++", I11:384-386),
     which are {d1} (F1, F2) with log order 0, and Corollary 4.3 raises by the pole order l_0 = 0 there
     (spec_iota+ in Re >= 2, I11:366-367).
  F4 (deduced; computed table) E^flat's log orders on [2, 3 + eps_+). Three sources write them: (i) f^(0) (Step 1,
     I11:352-361): G = (2, 0) U (2 + E_ind) and III.I' (3.2), which raises the log order only at the points of
     pi_1 E^C_I (Re <= l_I), by k(E^C_I, z) + 1 where breve E_+ has z, and adds (z, k(E^C_I, z)) where it has not;
     (ii) each window lambda_0 < 2 (I11:376-387): Corollary 4.3's remainder at lambda_0 + E^iota_ind + (0, k + l_0)
     ((4.5), G3:388), k = l_0 = 0 by F3, so log order l(w) at lambda_0 + w; and III.I' Proposition 3.1 on that window's
     error, which again raises only at points of pi_1 E^C_I, now of real part >= 5/2 (I11:385-386); (iii) f_2's E^0_src
     + 2 (G's points). A window's output is added to the source and is not passed through a later window's III.I'
     step (each window's III.I' acts on that window's own error, (4.5)), so at a point of real part >= 2 the log order
     is the largest over the windows, not their sum. Result: log order <= 2 at every exponent of the window except at
     the 26 points of pi_1 E^C_I in [2, 3], where it is at most 5 (R0) or 11 (R1).
     [Round 6, the verifier of round 5 (M1): (3.2)'s extended unions complete by (2.2) between its rounds, so on R1
     the raise at 2 (to 5) reaches 3 before the round at 3: 5 + 8 + 1 = 14 there, not 11; R0 unchanged (the
     completion (3, 1) is below G's (3, 2)). Log order above 2 at 17 points (R0), 18 (R1), not 26. f4_table.]
  F5 (exact) n_iota <= 3 P_iota + excess (the excess over 2 at those 26 points, 23 on R0, 44 on R1 [Round 6: 47]), so dceiling5 D6
     per exponent gives d <= 37,919,137,148,906,758 + 53,244,736 (excess + X_7) + 106,489,470 c': the 3.79e16 that
     round 4 printed as a hypothesis, now with the construction's own log orders.
  F6 (exact; a bound with one reading) L_0, the log order of E^0_src U E_++ U G U (2 + E_col) below 2 lambda_sharp:
     at least 2 (G at 3), at most 7 on round 2's reading that the column shifts are >= -5 (R2.3 (b)): the E_ind log order
     at offset 4 of the s0 site (k = 1), 2 x 4 - 1.
  F7 (deduced; READ I12:389-407) X_7: III.A Proposition 4.2 (2)'s loss is (2.26a)'s twice plus |E_iota,<=| and
     |E_K,<=| (A-PREREQ:650-704); at Step 7 beta_iota = beta'_+ < 3/2 < lambda_sharp <= min Re E_iota, so |E_iota,<=| = 0
     and X_7 = |E_K,<=| + (2.26a)'s losses, E_K the K+-exponents of Step 5 below alpha - 2 - eps.
  Controls (each mutates the computed path and must fail): C1 the windows' raises summed instead of maximised: the log
  order at 3 exceeds 1.5e7 and F4's bound fails [Round 6: F4's own loop rerun so; C4 F4 without the completion]; C2 the v1 site's extended unions counted twice: the log order at
  offset 1 becomes 4 and F4's "<= 2" fails; C3 Lemma 1.4 with every type's roots at k = 2: the offsets below 1 are
  {d0, d1} and F1's block-wise assertion fails on it.

    python3 checks/eflat5.py        (seconds)
"""
import builtins
import os
import sys
import textwrap
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import dceiling5 as DC  # noqa: E402  (round 3: the certified root census)
import dweights5 as DW  # noqa: E402  (round 1: data_ECI, III.C' (3.1))
import iotapoles5 as IP  # noqa: E402  (round 4: lemma14, m6)

OK = {}
E_UPS = G_UPS = Fr(1, 100)
LSHARP = Fr(3, 2) + (1 - E_UPS) * G_UPS                 # 1.5099 (LD8)
EPS_P = Fr(189, 10 ** 10)                                # eps_+ (dweights5 W1)
TOP_W = 3 + EPS_P - LSHARP                               # Step 2's offsets: (0, 3 + eps_+ - lambda_sharp]
L_I = Fr(13, 4)
P_IOTA = 85025784
NSTAR = 15000015


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def mpf_fr(q):
    m, e = q.man_exp
    return Fr(int(m)) * Fr(2) ** int(e)


def offsets():
    out, ints, ok = DC.root_census(Fr(4, 10 ** 6), top=10)
    off = {}
    for tag, l, n, lo, hi in out:
        lo, hi = mpf_fr(lo), mpf_fr(hi)
        off[(tag, l)] = (n, (lo + hi) / 2, lo, hi)
    return off, ints, ok


def lemma14(roots, k, top, extra=0):
    """III.A Lemma 1.4's E' (iotapoles5.lemma14's rule); extra > 0 is control C2's mutation"""
    if not extra:
        return IP.lemma14(roots, k, top)

    def closure(pts):
        o = {}
        for z0, lo in pts.items():
            n = 0
            while z0 + n <= top:
                o[z0 + n] = max(o.get(z0 + n, -1), lo)
                n += 1
        return o

    def ubar(A, B):
        o = dict(A)
        for z0, lo in B.items():
            o[z0] = (o[z0] + lo + 1 + extra) if z0 in o else lo
        return o
    Ea, F = closure({r: 0 for r in roots}), closure({Fr(k): 0})
    E = ubar(Ea, F)
    U = dict(E)
    for _ in range(int(top) + 3):
        E = ubar(Ea, ubar(F, {z0 + 1: lo for z0, lo in E.items() if z0 + 1 <= top}))
        for z0, lo in E.items():
            U[z0] = max(U.get(z0, -1), lo)
    return U


def site_eind(roots, k, top=Fr(8), extra=0):
    U = lemma14(roots, k, top, extra)
    return {z - k: lo for z, lo in U.items() if z > k}


def f4_table(M, G, lmax_w, c_gen, windows='max', completion=True, top=Fr(4)):
    """F4 (Round 6, the verifier of round 5, M1): E^flat's bound at the points z of pi_1 E^C_I in [2, 3] (R0: M = 1,
    R1: M = 4). Step 1 runs III.I' (3.2) in rounds over the windows [m_j, m_j + 1), m_j = 2 + j - 1, from G; each
    extended union raises the log order at z by k(E^C_I, z) + 1 (or puts (z, k(E^C_I, z)) where G has no z) and
    completes the index set by (2.2), adding (z + m, its order), m >= 1, so a raise at 2 reaches 3 before the round
    at 3 (A-PREREQ:122-130; round 5's rule took each z alone, completion=False). The windows' own III.I' steps raise
    only at real part >= 5/2 (I11:382-386) and are maximised (windows='max'), or summed over N_* windows (control).
    Returns (rows (z, k(E^C_I, z), bound) for every z, excess over c_gen, count of points)."""
    Ec = {z: kk for z, kk in DW.data_ECI(M, top=top).items() if 2 <= z <= 3 + EPS_P}
    S = {}
    for z0, lo in G.items():                       # G as an index set (closed under + N_0 by (2.2))
        n = 0
        while z0 + n <= top:
            S[z0 + n] = max(S.get(z0 + n, -1), lo)
            n += 1
    j = 1
    while 2 + j - 1 <= 3:
        mj = 2 + j - 1
        raised = []
        for z in sorted(Ec):
            if mj <= z < mj + 1 and z <= L_I:
                S[z] = S[z] + Ec[z] + 1 if z in S else Ec[z]
                raised.append(z)
        if completion:
            for z in raised:
                n = 1
                while z + n <= top:
                    S[z + n] = max(S.get(z + n, -1), S[z])
                    n += 1
        j += 1
    rows, excess = [], 0
    for z in sorted(Ec):
        kz = Ec[z]
        step1 = S.get(z, kz)
        win = (lmax_w + kz + 1) if z >= Fr(5, 2) else 0
        if windows == 'sum':
            b = max(c_gen, step1 + NSTAR * win)
        else:
            b = max(c_gen, step1, win)
        excess += b - c_gen
        rows.append((float(z), kz, b))
    return rows, excess, len(Ec)


def f4_ok(res, c_gen):
    """F4's test (Round 6): excess 23 (R0) and 47 (R1) over the 26 points, largest bounds 5 and 14, at 17 and 18
    points above c_gen = 2"""
    above = {nm: len([r for r in res[nm][0] if r[2] > c_gen]) for nm in res}
    return (c_gen == 2 and res['R0'][1] == 23 and res['R1'][1] == 47 and res['R0'][2] == 26
            and max(b for _, _, b in res['R0'][0]) == 5 and max(b for _, _, b in res['R1'][0]) == 14
            and above == {'R0': 17, 'R1': 18})


def main():
    print('eflat5: E^flat\'s log orders as the construction writes them; the ceiling on d with them')
    off, ints, census_ok = offsets()
    d0 = off[('s0', 0)][1]
    d1 = off[('sl-', 1)][1]
    dp1 = off[('sl+', 1)][1]
    blocks = {'s0': [2 + d0, Fr(3)], 's1': [2 + d1, 3 + dp1, Fr(4)], 'v1': [Fr(3)]}
    sites = [('III.F\'\'\' (1,0), mu-dot', 's0', 1), ('III.F\'\'\' (0,A), A-dot; III.D\'\' rotations', 'v1', 2),
             ('III.D\'\' translations', 's1', 2), ('III.D\'\' boosts', 's1', 1)]
    E = {}
    for name, b, k in sites:
        E[name] = site_eind(blocks[b], k)
    union = {}
    for e in E.values():
        for w, lo in e.items():
            union[w] = max(union.get(w, -1), lo)
    below1 = sorted(w for w in union if 0 < w < 1)
    win = {w: lo for w, lo in union.items() if 0 < w <= TOP_W}
    max5 = max(lo for w, lo in union.items() if w <= 5)
    arg5 = [w for w, lo in union.items() if w <= 5 and lo == max5]
    # the literal reading: every type's roots (iotapoles5 M5's census)
    allroots = sorted({Fr(n) + q for (n, q, _, _) in off.values()} | {Fr(i) for i in range(3, 11)})
    Efull = site_eind(allroots, 2)
    below1_full = sorted(w for w in Efull if 0 < w < 1)
    max5_full = max(lo for w, lo in Efull.items() if w <= 5)
    win_full = max(max(lo for w, lo in site_eind(allroots, k).items() if 0 < w <= TOP_W) for k in (1, 2))
    OK['F1'] = (census_ok and below1 == [d1] and max5 == 10 and arg5 == [Fr(5)] and max(win.values()) == 2
                and max5_full == 10 and win_full == 2)
    print('  F1: Lemma 1.4 per site (block by type at b0): offsets below 1 %s (d1 = %.4e); log orders at the offsets in '
          '(0, %.4f] (Step 2\'s): %s; largest log order at Re <= 5: %d at %s (round 4\'s M5 reproduced on the block '
          'reading). Every type\'s roots (M5\'s census): offsets below 1 %s (d0 = %.4e, d1), largest at Re <= 5: %d, '
          'largest at Step 2\'s offsets (k = 1, 2): %d' % (['%.4e' % w for w in below1], d1, float(TOP_W),
             sorted(('%.7f' % w, lo) for w, lo in win.items()), max5, [str(w) for w in arg5],
             ['%.4e' % w for w in below1_full], d0, max5_full, win_full))
    for name, b, k in sites:
        e = E[name]
        print('      %s (%s, k = %d): log orders at offsets 1, 2, 3, 4, 5: %s' % (
            name, b, k, [e.get(Fr(i), None) for i in range(1, 6)]))
    # F2 the towers: mu + 1 is not a type-tau root (D4 (R4))
    lam_s02 = 2 + d0
    tower = []
    for l in (1, 2, 3):
        dl, dpl = off[('sl-', l)], off[('sl+', l)]
        rl = [Fr(l + 3), Fr(1 - l), Fr(dl[0]) + dl[1], -(Fr(dl[0]) - 1 + dl[1]), Fr(dpl[0]) + dpl[1],
              -(Fr(dpl[0]) - 1 + dpl[1])]
        for mu in (1 - (Fr(dl[0]) + dl[1]), 1 - (Fr(dpl[0]) + dpl[1])):
            tower.append(('s%d' % l, float(mu), mu + 1 in rl))
    for l in range(2, 6):
        dl, dpl = off.get(('sl-', l)), off.get(('sl+', l))
        rl = [Fr(l + 3), Fr(1 - l)]
        tower.append(('s%d' % l, float(1 - l), Fr(2 - l) in rl))
    for l in range(2, 5):
        tower.append(('v%d' % l, float(-l), Fr(1 - l) in [Fr(-l), Fr(l + 2)]))
    s0r = [Fr(0), Fr(3), lam_s02, 1 - lam_s02]
    tower.append(('s0', float(1 - lam_s02), (1 - lam_s02) + 1 in s0r))
    OK['F2'] = not any(t[2] for t in tower)
    print('  F2: towers (D4 (R4)): class roots mu with mu + 1 a root of the same type: %s (of %d checked): offset 1 has '
          'log order 0 in every tower' % ([t for t in tower if t[2]], len(tower)))
    # F3 below 2: log order 0
    small = [w for w in union if 0 < w < 2 - LSHARP]
    OK['F3'] = small == [d1] and union[d1] == 0
    print('  F3: offsets below 2 - lambda_sharp = %.4f: %s with log orders %s; pole order 0 below 2: every exponent '
          'below 2 has log order 0' % (float(2 - LSHARP), ['%.4e' % w for w in small], [union[w] for w in small]))
    # F4 E^flat's table
    G = {Fr(2): 0}
    for w, lo in union.items():
        if 0 < w <= 1 + EPS_P:
            G[2 + w] = max(G.get(2 + w, -1), lo)
    lmax_w = max(win.values())
    c_gen = max(lmax_w, max(G.values()))
    res = {}
    for name, M in (('R0', 1), ('R1', 4)):
        res[name] = f4_table(M, G, lmax_w, c_gen)
    OK['F4'] = f4_ok(res, c_gen)
    print('  F4: E^flat\'s log order on [2, 3 + eps_+): at most %d off pi_1 E^C_I (Step 2: max l(w) = %d; G: %s); at '
          'the %d points of pi_1 E^C_I in [2, 3] at most (z, k(E^C_I, z), bound): R0 %s; R1 %s' % (
              c_gen, lmax_w, sorted((float(z), lo) for z, lo in G.items()), res['R0'][2],
              [r_ for r_ in res['R0'][0] if r_[2] > c_gen], [r_ for r_ in res['R1'][0] if r_[2] > c_gen]))
    # F5 the ceiling
    ok_A, at, hyp, (La, K1) = IP.m6()
    ceil = {nm: hyp + La * res[nm][1] for nm in ('R0', 'R1')}
    OK['F5'] = (ok_A and hyp == 37919137148906758 and ceil['R0'] == hyp + La * 23
                and ceil['R1'] == 37919139651409350)          # Round 6: R1 + 159,734,208 (completion)
    print('  F5: n_iota <= 3 P_iota + excess (excess %d on R0, %d on R1); per exponent: d <= %d (R0), %d (R1) + '
          '%d X_7 + %d c\' (%.6e + ...; N = 21 d + 6 <= %.6e + ...), against the floor 8,407,505,890,317,054 '
          '(ratio %.3f)' % (
              res['R0'][1], res['R1'][1], ceil['R0'], ceil['R1'], La, K1, ceil['R1'], 21 * ceil['R1'] + 6,
              ceil['R1'] / 8407505890317054))
    # F6 L_0
    l0_hi = max(E['III.F\'\'\' (1,0), mu-dot'].get(w, -1) for w in E['III.F\'\'\' (1,0), mu-dot']
                if w <= 2 * LSHARP - 2 - 2 + 5)
    l0_hi = max(l0_hi, max(E['III.F\'\'\' (0,A), A-dot; III.D\'\' rotations'][w] for w in
                           E['III.F\'\'\' (0,A), A-dot; III.D\'\' rotations'] if w <= 2 * LSHARP - 2 - 3 + 5),
                max(E['III.D\'\' translations'][w] for w in E['III.D\'\' translations'] if w <= 2 * LSHARP - 2 - 3 + 5))
    l0_lo = G[Fr(3)]
    OK['F6'] = l0_lo == 2 and l0_hi == 7
    print('  F6: L_0 in [%d, %d] (G at 3; the column classes (2, 0) U (2 + E_ind), (3, 0) U (3 + E_ind) at shifts '
          '>= -5, round 2\'s reading)' % (l0_lo, l0_hi))
    # F7 X_7
    bp_hi = Fr(3, 2)
    OK['F7'] = bp_hi < LSHARP
    print('  F7: Step 7\'s beta_iota = beta\'_+ < 3/2 < lambda_sharp = %s <= min Re E_iota: |E_iota,<=| = 0, X_7 = '
          '|E_K,<=| + (2.26a)\'s losses' % LSHARP)
    # controls
    # Round 6 (verifier of round 5, minor 1): C1 reruns F4's own loop with the windows summed, and F4's test on it
    res_sum = {nm: f4_table(M, G, lmax_w, c_gen, windows='sum') for nm, M in (('R0', 1), ('R1', 4))}
    at3 = [b for z, _, b in res_sum['R0'][0] if z == 3.0][0]
    OK['C1'] = not f4_ok(res_sum, c_gen) and at3 > 15 * 10 ** 6
    print('  C1 (control): F4\'s loop rerun with the windows\' raises summed instead of maximised: log order %d at 3; '
          'F4\'s test fails on it: %s' % (at3, OK['C1']))
    res_nc = {nm: f4_table(M, G, lmax_w, c_gen, completion=False) for nm, M in (('R0', 1), ('R1', 4))}
    OK['C4'] = not f4_ok(res_nc, c_gen) and res_nc['R1'][1] == 44 and res_nc['R0'][1] == 23
    print('  C4 (control, Round 6): F4 without the completion (2.2) between the rounds of (3.2) (round 5\'s rule): '
          'excess %d (R0), %d (R1), log order %d at 3 on R1: F4\'s test fails on it: %s' % (
              res_nc['R0'][1], res_nc['R1'][1], max(b for _, _, b in res_nc['R1'][0]), OK['C4']))
    Ebad = site_eind(blocks['v1'], 2, extra=1)
    OK['C2'] = Ebad[Fr(1)] > 2
    print('  C2 (control): the v1 site\'s extended unions counted twice: log order %d at offset 1 > 2: F4 fails: %s' % (
        Ebad[Fr(1)], OK['C2']))
    OK['C3'] = below1_full != [d1]
    print('  C3 (control): Lemma 1.4 with every type\'s roots at k = 2: offsets below 1 %s, not {d1}: F1\'s block '
          'assertion fails on it: %s' % (['%.4e' % w for w in below1_full], OK['C3']))
    for k_, val in OK.items():
        builtins.print(k_, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
