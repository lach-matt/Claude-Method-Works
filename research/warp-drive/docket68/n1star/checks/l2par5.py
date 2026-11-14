#!/usr/bin/env python3
"""l2par5: the level-2 loop of III.I''''''''''' Proposition 3.1 (I12 Step 3), read per exponent or per (alpha_0, k): the
applications of III.G'''' Proposition 4.4 at one exponent act in parallel, so the loss follows one chain of exponents
and the bound d of CONSTANTS5.md R10.1 holds on both readings (CONSTANTS5.md, Round 11, the round-10 verifier's minor
1). Labels: READ (cited lines, the files md5-pinned, the lines found by content), deduced (the argument, stated with
each item), computed (exact rational arithmetic on a model of the loop).

The question (READ, I12:278-281): "For each tf-exponent (alpha_0, k) of g_2 with 1 + eta_1 <= Re alpha_0 < 2 + eta_2,
III.G'''' Proposition 4.4 ...; its remainder exponents alpha_0 + E_ind may again lie below 2 + eta_2, and are treated
in turn". Counted per (alpha_0, k), the applications of one level number at least the sum over Lambda_0 cap W of
(K(lambda) + 1), >= 5.83e20 (LOSS-D LD15); counted per exponent, |Lambda cap W| <= P_W, which dnumber5 charges (3 per
application, every application in series: 3 P_W per level above 3). The tame accounting charges loss to compositions,
not to applications: J3 Lemma 1.2 (a) (a sum of families with loss d has loss d) and (b), (e) (a composition adds).

  P0 (READ) the files at their pinned md5 and the lines found by content: I12:278-281 (Step 3), G5:448-461 (Proposition
     4.4 and (4.3): the remainder's tf-index set ((alpha_0, k) + E_ind) u ((4, k + 1) + ...), min Re E_ind >= eps_ind,
     the exponents at 4 above Re alpha_0 + eps_ind), G5:476-481 (its proof: f is a sum of k + 1 terms, one per log
     power, each solved the same way, the remainder at (alpha_0 + 1, k)), J3:62-66 (Lemma 1.2 (a), (b)).
  P1 (deduced) No application at an exponent alpha_0 sees the output of another at alpha_0: each acts on the source's
     term at (alpha_0, j) (its coefficient of rho^alpha_0 (log rho)^j), and its remainder lies at real parts >= Re
     alpha_0 + eps_ind > Re alpha_0 (P0's (4.3)). So, at one exponent, the map source -> (the u's, the remainder) is a
     sum of families, one per log power (or one in all, per exponent), each a coefficient restriction composed with one
     Proposition 4.4: loss that of one application (Lemma 1.2 (a)), whatever the number of log powers. A composition
     arises only through a remainder, which raises the real part; so every chain of compositions visits each exponent
     of Lambda cap W at most once, and the loop's loss is at most 3 x (the longest chain) <= 3 |Lambda cap W| <= 3 P_W on
     either reading, in any order of treatment (revisits included: a term met again is a new sum of contributions, each
     carried along its own chain). dnumber5's 3 P_W is therefore an upper bound on both readings. [Round 12 (the
     round-11 verifier's nit): P1's PASS checks only what a program can: P0's reads and that the model's increments
     have positive real part. The argument itself is the deduction above, and it is not computed.]
  P2 (computed) The model: a scaled loop with exact rational exponents in a window, sources with log powers, E_ind with
     log orders (so that the log powers grow along chains and merge), treated (a) per (alpha_0, k) in increasing real
     part, (b) per exponent in increasing real part, (c) per (alpha_0, k) in a seeded random order (with revisits),
     (d) per exponent in a random order; the loss of each term propagated by Lemma 1.2: a sum takes the largest loss,
     an application adds 3. The loop's loss is the same in all four and equals 3 x the longest chain of exponents,
     while the numbers of applications differ (per (alpha_0, k) far more).
  P3 (computed) In the model, read per (alpha_0, k), every term (alpha_0, j) carries at most the loss its exponent
     carries read per exponent, and the largest over j is that loss (the induction behind P1: a term's loss is set by
     the chains of exponents below it, not by its log power).
  P4 (READ; computed) At the record's weights: the named part of Lambda cap W is three chains of 3,000,002, 1,470,302
     and 3,000,002 points and the point 3 (LOSS-D LD15, C2-C3); a chain of compositions visits distinct points of
     Lambda cap W (the real part rises at each link, and every exponent produced in W lies in Lambda, I11 Lemma 1.2
     (c)), so at most |Lambda cap W| <= P_W = 85,025,783 of them on the reading of Lambda the count uses (read from
     dnumber5.out, md5-pinned): the per-level charge 3 P_W stands on both readings of Step 3.
  Controls (each mutates the model or a pin and must fail): C1 E_ind given an element of real part 0, (0, 1) (a
  remainder at the same exponent, one log power up): the loss then exceeds 3 x the longest chain of exponents, growing
  with the log powers (P1's premise fails, and with it the bound); C2 the parallel sums charged in series (every
  application composed with every earlier one): the loss becomes 3 x the number of applications, LD15's count, and
  differs between the readings; C3 G5:481's text altered in a copy: P0 fails.

    python3 checks/l2par5.py        (seconds)
"""
import builtins
import hashlib
import os
import random
import re
import sys
import textwrap
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.join(HERE, '..', 'proof5')
OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


FILES = {'I12': ('PART-III-I12-SPECTRAL.md', '625e9374d22531b41c8e545dbac3427b'),
         'G5': ('PART-III-G5-TF.md', '52d411a185132b641f4097747aad1e41'),
         'J3': ('PART-III-J3-TAME.md', '441cb3b68d52b1f5472e262e6cf29ef1')}
PINS = [('I12', 278, "For each tf-exponent $(\\alpha_0,k)$ of $g_2$ with"),
        ('I12', 280, "its remainder exponents $\\alpha_0+\\mathcal E_{\\mathrm{ind}}$ may again lie below "
                     "$2+\\eta_2$, and are treated in turn"),
        ('G5', 448, "**Proposition 4.4 ([Hin26] Proposition 9.30 at n = 4).**"),
        ('G5', 456, "\\quad\\mathcal E_{\\alpha_0,k} :="),
        ('G5', 459, "$\\min\\mathrm{Re}\\,\\mathcal E_{\\mathrm{ind}}\\ge\\epsilon_{\\mathrm{ind}}$ not "
                    "depending on $b$, $\\alpha_0$, $k$"),
        ('G5', 461, "their real part exceeds $\\mathrm{Re}\\,\\alpha_0+\\epsilon_{\\mathrm{ind}}$"),
        ('G5', 479, "$f$ is a sum of $k+1$ such terms"),
        ('G5', 481, "and terms with lower log powers are treated the same way."),
        ('J3', 62, "(a) Sums of families tame with loss $d$ are tame with loss $d$"),
        ('J3', 66, "$(S_\\beta T_\\beta)$ is tame with loss $d+d'$.")]
DN_OUT = os.path.join(HERE, 'dnumber5.out')
DN_OUT_MD5 = '3db10f0e1cea470f903b38060a8b352c'
LOSSD = os.path.join(HERE, '..', 'LOSS-D.md')
LD15 = ['the chains λ_♯ + n d1 (3,000,002 points in W), λ_♯ + 1 + n d1', '(1,470,302) and 2 + n d1 (3,000,002), and '
        'the point 3, no two sharing a point']


def lines_of(key, root=P5):
    return open(os.path.join(root, FILES[key][0]), encoding='utf-8').read().split('\n')


def pins_ok(root=P5):
    md5 = all(hashlib.md5(open(os.path.join(root, f), 'rb').read()).hexdigest() == m for f, m in FILES.values())
    found = []
    for k, i, t in PINS:
        L = lines_of(k, root)
        found.append(t in L[i - 1])
    return md5, all(found), len(found)


# ------------------------------------------------------------------------------------------------ the model
ALPHA_LO, ALPHA_HI = Fr(11, 10), Fr(21, 10)          # the tf-window [1 + eta_1, 2 + eta_2), scaled
D1 = Fr(1, 8)
EIND = [(D1, 1), (Fr(3, 8), 0), (Fr(1), 0)]          # E_ind with log orders: (d1, 1), a second offset, (1, 0)
SOURCES = {Fr(11, 10): 2, Fr(6, 5): 0, Fr(5, 4): 1}  # g_2's tf-exponents and log orders (chains merge at 6/5 + 3/8)
COST = 3                                             # one Proposition 4.4: L_b 2 + III.F' Corollary 3.4's 1 (D588)


def run(per_pair, order, eind=EIND, serial=False, seed=11):
    """the loop on the model. per_pair: one application per (alpha_0, j) (else one per exponent, all its log powers).
    order: 'up' (least real part first) or 'random' (any pending term, revisits allowed). Each pending term carries the
    loss of the family source -> term (Lemma 1.2: a sum takes the largest, an application adds COST); serial charges
    every application after every earlier one (the series reading of control C2). Returns (loss, applications,
    loss by term). [Round 12 (the round-11 verifier): an increment of real part <= 0 is refused (ValueError) rather
    than looped on, since the loop then does not end; run_zero treats that case, with a cap.]"""
    if any(w <= 0 for w, _ in eind):
        raise ValueError('run: an increment of real part <= 0; the loop would not end (P1\'s premise fails)')
    rnd = random.Random(seed)
    pend = {(a, j): 0 for a, k in SOURCES.items() for j in range(k + 1)}
    seen = {}
    apps, top, clock = 0, 0, 0
    while pend:
        keys = sorted(pend)
        if order == 'up':
            a0 = keys[0][0]
        else:
            a0 = rnd.choice(keys)[0]
        batch = [kk for kk in keys if kk[0] == a0]
        if per_pair:
            if order != 'up':
                batch = [rnd.choice(batch)]
            groups = [[kk] for kk in batch]
        else:
            groups = [batch]
        for g in groups:
            lin = max(pend.pop(kk) for kk in g)
            if serial:
                lin = max(lin, clock)
            out = lin + COST
            apps += 1
            clock = out
            top = max(top, out)
            for kk in g:
                seen[kk] = max(seen.get(kk, 0), lin)
                a, j = kk
                for w, m in eind:
                    b = a + w
                    if b < ALPHA_HI:
                        for jj in range(j + m + 1):
                            pend[(b, jj)] = max(pend.get((b, jj), 0), out)
    return top, apps, seen


def longest_chain(eind=EIND):
    """the longest chain of exponents in the window, from a source exponent, by the increments' real parts"""
    pts = set(SOURCES)
    frontier = sorted(SOURCES)
    while frontier:
        new = []
        for a in frontier:
            for w, _ in eind:
                b = a + w
                if b < ALPHA_HI and b not in pts:
                    pts.add(b)
                    new.append(b)
        frontier = new
    pts = sorted(pts)
    depth = {}
    for a in pts:
        depth[a] = 1 + max([depth[a - w] for w, _ in eind if a - w in depth and w > 0] + [0])
    return max(depth.values()), len(pts)


def main():
    print('l2par5: the level-2 loop per exponent or per (alpha_0, k): the applications at one exponent act in parallel')
    md5, found, n = pins_ok()
    OK['P0'] = md5 and found
    print('  P0 (READ): %d files at their pinned md5: %s; %d lines found by content: %s (I12:278-281 Step 3 "for each '
          'tf-exponent (alpha_0, k) ... treated in turn"; G5:448-461 Proposition 4.4, (4.3), min Re E_ind >= eps_ind, '
          'the exponents at 4 above Re alpha_0 + eps_ind; G5:479-481 "f is a sum of k+1 such terms ... terms with lower '
          'log powers are treated the same way"; J3:62-66 Lemma 1.2 (a), (b))' % (len(FILES), md5, n, found))
    pos = all(w > 0 for w, _ in EIND)
    OK['P1'] = pos and OK['P0']
    print('  P1 (deduced): each application at alpha_0 acts on the source\'s terms at alpha_0 and leaves its remainder '
          'at real parts >= Re alpha_0 + eps_ind, so no application at alpha_0 sees another\'s output: at one exponent '
          'the applications are a sum of families (Lemma 1.2 (a): the loss of one), and compositions arise only through '
          'remainders, which raise the real part; the loop\'s loss is at most 3 x the longest chain of exponents <= 3 '
          '|Lambda cap W| <= 3 P_W on either reading and in any order. The PASS checks only P0 and that the model\'s '
          'increments all have positive real part (%s); the argument is deduced, not computed' % pos)
    L, npts = longest_chain()
    res = {}
    if not pos:
        print('  P2: the model has an increment of real part <= 0, which run() refuses: P1\'s premise fails')
        for k in ('P2', 'P3', 'P4'):
            OK[k] = False
        for k, v in OK.items():
            builtins.print(k, 'PASS' if v else 'FAIL')
        return 1
    for name, pp, od in (('(a) per (alpha_0, k), up', True, 'up'), ('(b) per exponent, up', False, 'up'),
                         ('(c) per (alpha_0, k), random', True, 'random'), ('(d) per exponent, random', False,
                                                                             'random')):
        res[name] = run(pp, od)
    losses = {k: v[0] for k, v in res.items()}
    apps = {k: v[1] for k, v in res.items()}
    OK['P2'] = len(set(losses.values())) == 1 and set(losses.values()) == {COST * L} and \
        apps['(a) per (alpha_0, k), up'] > apps['(b) per exponent, up']
    print('  P2 (computed, exact): the model (window [%s, %s), d1 = %s, E_ind = %s, sources %s): %d exponents, the '
          'longest chain %d; the loop\'s loss %s; applications %s: the loss is 3 x the longest chain in all four, the '
          'counts differ: %s' % (ALPHA_LO, ALPHA_HI, D1, [(str(w), m) for w, m in EIND],
                                 {str(a): k for a, k in SOURCES.items()}, npts, L, losses, apps, OK['P2']))
    _, _, sp = res['(a) per (alpha_0, k), up']
    _, _, se = res['(b) per exponent, up']
    le = {}
    for (a, j), v in se.items():
        le[a] = max(le.get(a, 0), v)
    lp = {}
    for (a, j), v in sp.items():
        lp[a] = max(lp.get(a, 0), v)
    OK['P3'] = all(v <= le[a] for (a, j), v in sp.items()) and lp == le
    print('  P3 (computed): per (alpha_0, k), every term (alpha_0, j) carries at most its exponent\'s loss read per '
          'exponent, and the largest over j equals it (%d exponents, %d terms): %s' % (len(le), len(sp), OK['P3']))
    txt = open(DN_OUT, encoding='utf-8').read()
    dmd5 = hashlib.md5(txt.encode('utf-8')).hexdigest() == DN_OUT_MD5
    m = re.search(r'P_W = (\d+)', ' '.join(txt.split()))
    PW = int(m.group(1))
    ld = ' '.join(open(LOSSD, encoding='utf-8').read().split())
    ldok = all(' '.join(x.split()) in ld for x in LD15)
    OK['P4'] = dmd5 and ldok and 3000002 + 1470302 + 3000002 + 1 <= PW
    print('  P4 (READ; computed): LOSS-D LD15 C2-C3 found: %s (the named part of Lambda cap W: chains of 3,000,002, '
          '1,470,302, 3,000,002 points and the point 3, %d in all); P_W = %d (dnumber5.out, md5 pinned: %s) bounds '
          'every chain of compositions in W, so the per-level charge 3 P_W = %d holds on both readings: %s' % (
              ldok, 7470307, PW, dmd5, 3 * PW, OK['P4']))
    # controls
    e1 = EIND + [(Fr(0), 1)]
    rz = run_zero(e1)
    OK['C1'] = rz[0] > COST * L
    print('  C1 (control): E_ind with (0, 1) added (a remainder at the same exponent, one log power up; log powers '
          'capped at 6): loss %d > 3 x the longest chain of exponents, %d: %s' % (rz[0], COST * L, OK['C1']))
    s_a = run(True, 'up', serial=True)
    s_b = run(False, 'up', serial=True)
    OK['C2'] = s_a[0] == COST * s_a[1] and s_a[0] != s_b[0] and s_a[0] != COST * L
    print('  C2 (control): the parallel sums charged in series: loss per (alpha_0, k) %d = 3 x %d applications, per '
          'exponent %d: the readings differ and neither is 3 x the longest chain: %s' % (s_a[0], s_a[1], s_b[0],
                                                                                          OK['C2']))
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp()
    try:
        for f, _ in FILES.values():
            shutil.copy(os.path.join(P5, f), tmp)
        p = os.path.join(tmp, FILES['G5'][0])
        s = open(p, encoding='utf-8').read()
        s = s.replace('and terms with lower log powers are treated the same way.', 'and terms with lower log powers '
                      'are treated in turn.')
        open(p, 'w', encoding='utf-8').write(s)
        md5c, foundc, _ = pins_ok(tmp)
        OK['C3'] = not (md5c and foundc)
    finally:
        shutil.rmtree(tmp)
    print('  C3 (control): G5:481 altered in a copy: P0 fails: %s' % OK['C3'])
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


def run_zero(eind, cap=6):
    """the loop per (alpha_0, k), least real part first, with an increment of real part 0 allowed (control C1): a term's
    remainder may land at its own exponent, one log power up, capped at log power `cap`. Returns (loss,
    applications)."""
    pend = {(a, j): 0 for a, k in SOURCES.items() for j in range(k + 1)}
    seen = {}
    apps, top = 0, 0
    while pend:
        kk = min(pend)
        lin = pend.pop(kk)
        out = lin + COST
        apps += 1
        top = max(top, out)
        seen[kk] = max(seen.get(kk, 0), lin)
        a, j = kk
        for w, m in eind:
            b = a + w
            if b < ALPHA_HI:
                for jj in range(j + m + 1) if w > 0 else [j + 1]:
                    if jj <= cap and (b, jj) not in seen:
                        pend[(b, jj)] = max(pend.get((b, jj), 0), out)
    return top, apps


if __name__ == '__main__':
    sys.exit(main())
