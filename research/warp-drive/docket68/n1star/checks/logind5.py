#!/usr/bin/env python3
"""logind5: I11 Proposition 3.1 (c), sharpened: the log orders of E^flat and of the level-2 sources, proved by
induction over the construction's steps and recomputed from that induction (CONSTANTS5.md, Round 12, Lemma R12.1;
the round-11 verifier's request). Labels: READ (cited lines, files md5-pinned, lines found by content), deduced (the
induction step, stated with each item), computed (exact integer and rational arithmetic; d1, d0, delta'_1 from
dceiling5's certified root census, as eflat5 uses them).

Lemma R12.1 (I11 Proposition 3.1 (c), sharpened). At the weights of dweights5 W1, with E_ind and E^iota_ind the
write-out's (E_ind: the index sets of III.D'' Proposition 3.1 and III.F''' Proposition 2.2, I5:190, I8:35, built by
III.A Lemma 1.4; E^iota_ind: III.G'' (4.4)'s, from III.D''' Lemma 2.1's towers), in the construction of I11
Proposition 3.1 and I12 Step 3:
  (a) every u-exponent below 2 that the construction meets has log order 0;
  (b) E^flat has log order at most 2 at every exponent of [2, 3 + eps_+) other than the points z of pi_1 E^C_I in
      [2, 3], and at most b(z) at those, b the table of eflat5 F4 (R0: largest 5, excess 23 over 2; R1: largest 14,
      excess 47);
  (c) the level-2 sources of I12 Step 3 have log order at most 2 + e_c at every point of a d1-chain c of Lambda cap
      (2, 3), e_c the excess over 2 at the chain's first point in (2, 3) (dnumber5 K3).
Proof (induction over the steps, in the order the construction takes them):
  S1 (offsets; eflat5 F1-F2, computed) Below 2 - lambda_sharp = 0.4901 the offsets of E_ind u E^iota_ind are {d1},
     with log order 0: E_ind's block-wise Lemma 1.4 offsets below 1 are {d1} (F1) and the towers' offsets in (0,
     1.4901] are {1}, with log order 0 (F2).
  S2 (below 2; I11:367-374, 380-386; G3 (4.5)) The windows run in increasing order of real part. Corollary 4.3 at
     lambda_0 with the source's log order k and pole order l_0 = 0 (spec_iota+ in Re >= 2, I11:373-374) leaves its
     error at lambda_0 + E^iota_ind + (0, k + l_0) and III.I' Proposition 3.1 adds exponents in lambda_0 + E^iota_ind +
     (0, k) or of real part >= 5/2. By S1 the only error exponent below 2 is lambda_0 + d1, of log order k + 0 + 0; so
     by induction over the windows every exponent below 2 has log order 0 (the source's below 2 are pi_1 M with E_++'s
     log orders, I11:384-386, E_++ being the least index set closed under the same steps).
  S3 (the windows' outputs above 2; (4.5), I11:380-383) A window's error joins the source and is not passed through a
     later window's III.I' step (each window's III.I' acts on that window's own error): at a point of real part >= 2
     the log order is the largest over the windows, not their sum: at most max l(w) + 0 = 2 off the points of pi_1
     E^C_I, and at those of real part >= 5/2 the window's III.I' (3.2) raise k(E^C_I, z) + 1 on top (taken as a raise,
     an upper bound).
  S4 (Step 1, I11:352-361; III.I' (3.2), I2:173-177) The extended unions raise the log order only at the points of
     pi_1 E^C_I with Re <= l_I, by k(E^C_I, z) + 1 (or add (z, k(E^C_I, z))), the index set completed by (2.2) between
     the rounds; III.A Lemma 1.4 raises only at the indicial roots (inside S1's offsets). So E^flat's log order at a
     point is the largest of G's (2 at 3), Step 1's rounds and S3's: eflat5 F4's table. This is (b).
  S5 (level 2, I12:278-281, G5 (4.3)) Proposition 4.4 at (alpha_0, k) leaves (alpha_0, k) + E_ind and (4, k + 1) +
     ...; in the window W the only offset is d1, of log order 0 (offset 1 and above leave W: Lambda has no point in
     (2, 2 + m), m = 1.9839e-8 > eta_2, modcount5 M5), so a log order is carried along the d1-chain unchanged and
     maxed with the sources at each point: E^flat's (b), 2 + E_col, u_0's. The sources off the chains' first points
     are <= 2 (an excess point is a chain's first point: a rational start g has g + n d1 irrational for n >= 1, d1
     being irrational; the E_col bases lie on distinct chains, off the other starts' chains, lambdagen5 L5,
     certified), so along a chain the carry is the fixed point 2 + e_c. This is (c).

  L0 (READ) the files at their pinned md5 and the lines found by content.
  L1 (computed) S1: the offsets below 2 - lambda_sharp and their log orders (eflat5's census, imported).
  L2 (computed) S2: the windows below 2, each in turn (their number counted with d1's certified interval, equal to W =
     1,470,302 of dnumber5.out), the induction hypothesis "log order 0" asserted at each.
  L3 (computed) S3-S4: the table recomputed from the induction (Step 1's rounds with the completion, the windows'
     outputs maximised), equal at every point to eflat5 F4's, R0 and R1.
  L4 (computed) S5: every excess point rational; the chain recurrence k_(n+1) = max(src, k_n + l(d1)) reaches its fixed
     point 2 + e_c at once on every chain of dnumber5's (R0, R1; wide and shifted E_col), the e_c equal to dnumber5's.
  Controls (each mutates the induction and must fail): C1 the windows' raises summed instead of maximised (S3): L3
  fails; C2 pole order l_0 = 1 below 2 (S2): the hypothesis fails at the second window; C3 d1 with log order 1 at
  level 2 (S5): the chain carry exceeds 2 + e_c; C4 Step 1's extended unions raising at the completed points too (S4):
  L3 fails.
  [Round 13 (the round-12 reader's nit 5). What L2 and L4 compute and what they cite: given l(d1) = 0, l_0 = 0 and the
  sources' log orders (eflat5's census and F4 table, dnumber5's chains), both loops reduce to identities, so they check
  the bookkeeping, not the premises. The premises are cited: d1's irrationality and the first-point property of the
  chains (dnumber5's chain construction, lambdagen5 L5, certified), and the offsets below 2 - lambda_sharp with
  E^iota_ind computed (checks/iotaind5.py I4). The lemma is proved at the record's computational point, where its
  offsets are computed.]

    python3 checks/logind5.py        (seconds)
"""
import builtins
import contextlib
import hashlib
import io
import os
import re
import sys
import textwrap
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.join(HERE, '..', 'proof5')
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import eflat5 as EF      # noqa: E402  (F1-F4: offsets, Lemma 1.4 sites, the F4 table)
    import dweights5 as DW   # noqa: E402  (W1, data_ECI, d1's interval)
    import dnumber5 as DN    # noqa: E402  (K3: the chains and their excesses)

OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


FILES = {'I11': ('PART-III-I11-SPACETIME.md', '6e227bf7766fbe6b32949939b9235ed7'),
         'G3': ('PART-III-G3-GRAFT.md', 'c450676b3d418757e8ceadb2f1c1f035'),
         'I2': ('PART-III-I2-SCRI.md', '1c292c9ec524a0592373ebb838f4a8b4'),
         'I5': ('PART-III-I5-UNBOOST.md', 'e2fc5cb2a60410dc0699bca2c31b948d'),
         'I8': ('PART-III-I8-UNPARAM.md', '1286e8d0e18434999f4bf7692d728a25'),
         'G5': ('PART-III-G5-TF.md', '52d411a185132b641f4097747aad1e41'),
         'I12': ('PART-III-I12-SPECTRAL.md', '625e9374d22531b41c8e545dbac3427b')}
PINS = [('I11', 368, "in increasing order"),
        ('I11', 369, "of real part, window by window."),
        ('I11', 373, "$l_0 = 0$ ($\\mathrm{spec}_{\\iota^+}(\\bar"),
        ('I11', 383, "$\\lambda_0+\\mathcal E^\\iota_{\\mathrm{ind}}+(0,k)$ or have real part $\\ge\\frac52$"),
        ('I11', 385, "exponents below 2 lie in $\\pi_1\\mathcal M$ with the log orders of $\\mathcal E_{++}$"),
        ('G3', 375, "+\\mathcal E_{\\mathrm{ind}}+(0,k+l_0),\\ \\lambda_0+\\ell_K-\\epsilon}"),
        ('I2', 177, "z\\in\\pi_1\\mathcal E^C_I,\\ m_j\\le\\mathrm{Re}\\,z<m_j+1,\\tag{3.2}"),
        ('I5', 190, "is the index set of III.D$''$ Proposition 3.1 at $b_0$, fixed once"),
        ('I8', 35, "In this part $\\mathcal E_{\\mathrm{ind}}$ is the union of the index sets of"),
        ('G5', 456, "\\quad\\mathcal E_{\\alpha_0,k} :="),
        ('I12', 278, "For each tf-exponent $(\\alpha_0,k)$ of $g_2$ with")]


def pins_ok(root=P5):
    md5 = all(hashlib.md5(open(os.path.join(root, f), 'rb').read()).hexdigest() == m for f, m in FILES.values())
    found = [t in open(os.path.join(root, FILES[k][0]), encoding='utf-8').read().split('\n')[i - 1] for k, i, t in PINS]
    return md5, all(found), len(found)


def offsets():
    """S1's data, from eflat5 (its F1 union of the Lemma 1.4 sites, block by type; F2's tower offset 1, log order 0)"""
    off, _, census_ok = EF.offsets()
    d0, d1, dp1 = off[('s0', 0)][1], off[('sl-', 1)][1], off[('sl+', 1)][1]
    blocks = {'s0': [2 + d0, Fr(3)], 's1': [2 + d1, 3 + dp1, Fr(4)], 'v1': [Fr(3)]}
    union = {}
    for b, k in (('s0', 1), ('v1', 2), ('s1', 2), ('s1', 1)):
        for w, lo in EF.site_eind(blocks[b], k).items():
            union[w] = max(union.get(w, -1), lo)
    union[Fr(1)] = max(union.get(Fr(1), -1), 0)                 # the towers' offset 1 (F2), log order 0
    return census_ok, d1, union


def below_two(union, d1lo, d1hi, l0=0, extra_d1=0):
    """S2: the windows below 2 in increasing order; returns (number of windows, hypothesis held, largest log order
    met, largest log order of an output above 2 from offsets w >= 2 - lambda_sharp)"""
    ls = DW.LSHARP
    nlo, nhi = (2 - ls) / d1hi, (2 - ls) / d1lo
    nwin = int(nlo) + 1
    assert int(nhi) + 1 == nwin
    small = {w: lo for w, lo in union.items() if 0 < w < 2 - ls}
    big = {w: lo for w, lo in union.items() if 2 - ls <= w <= EF.TOP_W}
    ld1 = small[min(small)] + extra_d1
    k, held, top, out = 0, True, 0, 0
    for n in range(nwin):
        if n > 0:
            k = max(0, k + ld1 + l0)                             # the source below 2 (E_++, 0) and the carried error
        if k > 0:
            held = False
            top = max(top, k)
            break
        top = max(top, k)
        out = max(out, max(k + l0 + lo for lo in big.values()))
    return nwin, held, top, out, len(small), sorted(small.items())


def table(M, G, lmax_w, c_gen, windows='max', raise_completed=False):
    """S3-S4: E^flat's bound at the points of pi_1 E^C_I in [2, 3 + eps_+], recomputed from the induction"""
    Ec = {z: kz for z, kz in DW.data_ECI(M, top=Fr(4)).items() if 2 <= z <= 3 + EF.EPS_P}
    S = {}
    for z0, lo in G.items():
        n = 0
        while z0 + n <= 4:
            S[z0 + n] = max(S.get(z0 + n, -1), lo)
            n += 1
    for mj in (Fr(2), Fr(3)):                                     # the rounds of (3.2) over [2, 3) and [3, 4)
        raised = [z for z in sorted(Ec) if mj <= z < mj + 1 and z <= EF.L_I]
        for z in raised:
            S[z] = S[z] + Ec[z] + 1 if z in S else Ec[z]
        for z in raised:                                          # the completion (2.2) before the next round
            n = 1
            while z + n <= 4:
                S[z + n] = max(S.get(z + n, -1), S[z] + (Ec[z] + 1 if raise_completed and z + n in Ec else 0))
                n += 1
    out = {}
    for z in sorted(Ec):
        win = lmax_w + Ec[z] + 1 if z >= Fr(5, 2) else 0
        if windows == 'sum':
            win = win * EF.NSTAR
        out[z] = max(c_gen, S.get(z, Ec[z]), win)
    return out


def chain_carry(e, ld1, steps=10 ** 6):
    """S5: along a d1-chain, k_(n+1) = max(2, k_n + l(d1)) from k_0 = 2 + e; returns (fixed point reached, largest)"""
    k, top = 2 + e, 2 + e
    for _ in range(steps):
        nk = max(2, k + ld1)
        top = max(top, nk)
        if nk == k:
            return True, top
        k = nk
    return False, top


def main():
    print('logind5: Lemma R12.1, E^flat\'s and the level-2 sources\' log orders by induction over the construction')
    md5, found, n = pins_ok()
    OK['L0'] = md5 and found
    print('  L0 (READ): %d files at their pinned md5: %s; %d lines found by content: %s (I11:368-369 the windows in '
          'increasing order; I11:373 l_0 = 0; I11:383 the windows\' III.I\' exponents; I11:385 the exponents below 2; '
          'G3 (4.5); I2 (3.2); I5:190, I8:35 E_ind fixed; G5 (4.3); I12:278 Step 3)' % (len(FILES), md5, n, found))
    census_ok, d1, union = offsets()
    d1lo, d1hi = DW.d1_interval()
    small = sorted((float(w), lo) for w, lo in union.items() if 0 < w < 2 - DW.LSHARP)
    OK['L1'] = census_ok and len(small) == 1 and small[0][1] == 0 and d1lo <= d1 <= d1hi
    print('  L1 (computed; eflat5 F1-F2): offsets of E_ind u E^iota_ind below 2 - lambda_sharp = %.4f: %s (d1 = %.10e '
          'in its certified interval: %s)' % (float(2 - DW.LSHARP), small, float(d1), d1lo <= d1 <= d1hi))
    nwin, held, top, out, nsmall, _ = below_two(union, d1lo, d1hi)
    txt = open(os.path.join(HERE, 'dnumber5.out'), encoding='utf-8').read()
    W = int(re.search(r'(?<![\w])W = (\d+)', ' '.join(txt.split())).group(1))
    OK['L2'] = held and top == 0 and nwin == W and out == 2
    print('  L2 (computed): the windows below 2, each in turn: %d (W of dnumber5.out: %d); the hypothesis "log order 0" '
          'holds at every one: %s; the largest log order of an output above 2: %d' % (nwin, W, held, out))
    big = {w: lo for w, lo in union.items() if 0 < w <= EF.TOP_W}
    lmax_w = max(big.values())
    G = {Fr(2): 0}
    for w, lo in union.items():
        if 0 < w <= 1 + EF.EPS_P:
            G[2 + w] = max(G.get(2 + w, -1), lo)
    c_gen = max(lmax_w, max(G.values()))
    same, rows = True, {}
    for nm, M in (('R0', 1), ('R1', 4)):
        mine = table(M, G, lmax_w, c_gen)
        ef = EF.f4_table(M, G, lmax_w, c_gen)
        efd = {Fr(z).limit_denominator(10 ** 6): b for z, kz, b in ef[0]}
        mined = {z.limit_denominator(10 ** 6): b for z, b in mine.items()}
        same = same and mined == efd and sum(b - c_gen for b in mine.values()) == ef[1]
        rows[nm] = (max(mine.values()), sum(b - c_gen for b in mine.values()), len(mine))
    OK['L3'] = same and c_gen == 2 and rows['R0'][:2] == (5, 23) and rows['R1'][:2] == (14, 47)
    print('  L3 (computed): the table from the induction (Step 1\'s rounds of (3.2) with the completion, the windows\' '
          'outputs maximised, the windows\' (3.2) raise at Re >= 5/2): off pi_1 E^C_I at most %d; at its %d points in '
          '[2, 3 + eps_+] largest %d, excess %d (R0), largest %d, excess %d (R1); equal at every point to eflat5 F4\'s: '
          '%s' % (c_gen, rows['R0'][2], rows['R0'][0], rows['R0'][1], rows['R1'][0], rows['R1'][1], same))
    w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))
    with contextlib.redirect_stdout(io.StringIO()):
        T = DN.logs_tables()
    ld1 = union[min(union)]
    l4, nch, exc = True, 0, set()
    for reading in ('R0', 'R1'):
        for ecol_rd in ('wide', 'shifted'):
            chs, sp = DN.chains(w, T, reading, ecol_rd, d1lo, d1hi)
            for ch in chs:
                nch += 1
                fixed, tp = chain_carry(ch['e'], ld1)
                l4 = l4 and fixed and tp == 2 + ch['e']
                if ch['e'] > 0:
                    exc.add((ch['name'], ch['e']))
    rational_starts = all(isinstance(z, Fr) and z.denominator < 10 ** 6 for z in DW.data_ECI(4, top=Fr(4)))
    OK['L4'] = l4 and ld1 == 0 and rational_starts
    print('  L4 (computed): l(d1) = %d at level 2; the chain recurrence reaches its fixed point 2 + e_c at once on all '
          '%d chains (R0/R1 x wide/shifted E_col): %s; the excess points are their chains\' first points (the rational '
          'starts (rational: %s) by d1\'s irrationality; the E_col bases by lambdagen5 L5); chains with an excess: '
          '%s' % (
              ld1, nch, l4, rational_starts, sorted(exc)))
    # controls
    res_sum = table(4, G, lmax_w, c_gen, windows='sum')
    OK['C1'] = max(res_sum.values()) > 14
    print('  C1 (control): the windows\' raises summed over N_* windows: largest %d > 14: L3 fails: %s' % (
        max(res_sum.values()), OK['C1']))
    _, held2, top2, _, _, _ = below_two(union, d1lo, d1hi, l0=1)
    OK['C2'] = not held2
    print('  C2 (control): pole order l_0 = 1 below 2: the hypothesis fails (log order %d at the second window): %s' % (
        top2, OK['C2']))
    fixed3, tp3 = chain_carry(1, 1, steps=10 ** 4)
    OK['C3'] = not fixed3 and tp3 > 3
    print('  C3 (control): d1 with log order 1 at level 2: no fixed point, the carry reaches %d > 2 + e_c = 3 within '
          '10^4 points: %s' % (tp3, OK['C3']))
    res_rc = table(4, G, lmax_w, c_gen, raise_completed=True)
    ef4 = {Fr(z).limit_denominator(10 ** 6): b for z, kz, b in EF.f4_table(4, G, lmax_w, c_gen)[0]}
    OK['C4'] = {z.limit_denominator(10 ** 6): b for z, b in res_rc.items()} != ef4
    print('  C4 (control): Step 1\'s extended unions raising at the completed points too: the table differs from F4\'s '
          '(largest %d): %s' % (max(res_rc.values()), OK['C4']))
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
