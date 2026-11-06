#!/usr/bin/env python3
"""modcount5: the fixed per-level steps of the beta-levels (the MODs, with every other step a level charges beyond the
counted loops), read and counted at the record's weights, so that c' and d become integers (CONSTANTS5.md, Round 8,
item 1). Labels: READ (cited lines, every one pinned: the file's md5, the line number, the matched text), deduced (the
reading: which map a cited line applies, and the losses of J3 Lemma 2.1 and LOSS-D section 2b at that site), computed
(exact rational and integer arithmetic).

What a level is (READ, I15:323-352). III.I'''''''''''''' Theorem 3.1's Step 2 treats each beta-level: it forms
G~ = F - Delta_q(p') - R_q u (BG) and G' (rows: FIN), and applies III.I''''''''''''' Lemma 2.2 (levels above 3) or
III.I'''''''' Lemma 3.2 (levels below 3) to u. Lemma 2.2 is III.I''''''''''' Lemma 3.2's proof (I14:163-170) with
III.I'''''''''' Proposition 3.1 at beta (I11:349-403) and III.I''''''''''''' Proposition 2.1 (I14:101-150, which is
III.I''''''''''' Proposition 3.1's proof, I12:246-401, with the changes of I14:108-150), whose Lemmas 2.1-2.5 are
I12:110-236. Lemma 3.2 below 3 is I9:239-342 with Lemma 3.1's Steps 1-2 (I9:219-234) and III.I'''''' Proposition
2.1's Steps 3-3.3 and 4-6 (I7:190-253, 287-333; its Steps 3.4-3.5 replaced by I9's 3.4'-3.5'). Those ranges are
scanned here.

  M0 (READ) the files are pinned by md5 (FILES); the ranges are found by content (ANCHORS), so a moved line fails.
  M1 (READ; computed census) every invocation in the ranges of a family that J3 Lemma 2.1 (PART-III-J3-TAME.md:
     96-180) lists -- FWD, BG, the transforms and model inverses of (e)-(g) (III.A Proposition 4.2 and Lemma 1.4,
     (2.25a)-(2.26a), III.H Proposition 3.2 and Corollary 4.x, III.I'' Lemmas 2.1-4.3, III.I' Propositions 2.1, 3.1,
     the III.G-type propositions, III.F' Corollary 3.4, II.G' Corollaries 4.2, 4.5), the order-2 operator L-hat(sigma)
     and L_b applied, the parts' own lemmas and the routing citations -- is matched by FAM's patterns (212 hits) and
     classified by TABLE: charged here (a charge id), counted in the constant A' of dnumber5 (rounds, the level-2
     container, X_7, Step 0's III.A Proposition 4.2 (1), the windows and the iota+ loop, below 3 the one-off
     application and III.I' Proposition 2.1 of the 58), a statement or a lemma's own text (charged where it is
     applied), FIN or INT of loss 0 (J3 (c)-(d)), base level or top level only, replaced at this use, or routing to a
     range scanned in its own right. 0 unclassified; every TABLE row is hit (no stale row).
  M2 (deduced; computed) the charges, at the record's weights (dweights5 W1, imported) and, where a loss depends on
     the level, at the worst level of its range:
     - FWD: III.I Theorem 5.3's loss D_0 + D_1 + d' + d'' + 6, from d0count5 as corrected in Round 8 (the round-7
       verifier's A and A2: D_0 <= 399 and D_1 <= 52 on the order box, Q3b): 474 (round 7's 248 withdrawn); Round 9
       (the round-8 verifier's MAJOR 1: the Peetre exponents over the factors' orders): D_0 <= 435, FWD <= 510;
     - BG: 2 per order-2 application (J3 (b)): I15's R_q u, Delta_q and Lemma 3.2's (L - L_b0) u;
     - III.I' Proposition 3.1 at I11's Step 1, the one-off application to the general class E^C_I: 2 (1 + J + L) by
       prop31loss5's chain on dweights5's data_ECI, 12 (R0), 30 (R1, 4 rounds), 48 (R1, 7 rounds): charged 48;
     - III.I'' Lemma 4.1 (v_hi, u_hi): J3 (f)'s l + 1 for II.G' Corollary 4.5, l = 2 l_3 + l_4 + l_5 (II.G2:847-859;
       l_4 = l_1 + l_2 + 2N + 0, II.G2:776-790, with s <= 3, r_in - r_out <= 2, N = 1), plus every map of (e) its proof
       uses, summed although they act on disjoint pieces: (2.25a) 1, (2.25b) l_5, II.G' Corollary 4.2 (2)'s (2.3)
       (2 at beta_scf in [1, 3/2), thetain5 T6), Proposition 3.5 (1)'s l_F and (2)'s l (II.G2:526-537), at the
       output weights (3/2 - eps, N_o, N_o), N_o = 21/10 (any N_o > alpha - 2 serves the use);
     - III.H Proposition 3.2 (L~(0)^-1): 1 per zero-energy solve (J3 (e)); III.A Lemma 1.4 within I12 Lemma 2.1, which
       J3 does not list: 2 per application (the order of A), (ceil(mu' - mu) + 1) applications (each gains < 1);
     - L-hat(sigma) applied in I12 Lemma 2.2 and in I7's Steps 3.1, 3.3: 2 each;
     - III.G'''' Proposition 4.4 at level 1 (the exponent 2): 3 per application (LD16, thetain5 T4), per (alpha_0, k):
       k_1(2) + 1 = 11 applications (dnumber5 K3, imported), 33; Proposition 5.1 once at I7 Step 3.2: 3;
     - III.I'' Lemma 4.2: (2.4) = 2 (LOSS-D 2b, thetain5 T6);
     - II.G' Proposition 3.5 (1) ((2.26a)) at I12 Step 5 (iii) and I7 Steps 4-5: l_F at the site's weights; III.A
       Proposition 4.2 (2) for the last level's column pieces (I12 Lemma 2.4 at j = 3): (2.2) with n_iota = n_K = 0
       (plain weights, III.I'' Lemma 4.3) and l_F, both pieces;
     - III.I' Proposition 2.1 (I12 Step 7, I9 Step 8): 2 x steps, dweights5.prop21_steps (5) plus one for Step 1: 12.
  M3 (computed) c'_above = FWD + the charges at a level above 3 (the beta > 4 extras included), c'_below likewise,
     c' := max, and d <= A' + 106,489,470 c' with A' = dnumber5's R1 constant 45,661,383,902,649,727 (imported);
     N = 21 d + 6. Pinned: c' and d.
  M4 (deduced on the reading; computed) the steps of III.I with fourteen primes, Theorem 3.1, outside its levels
     (I15:296-452), which round 7's chain omitted. Round 8 bounded them coarsely by 2 (M_a + 4 M_b) + 1000; Round 9
     (the round-8 verifier's minor 1) itemises them (one_offs): Step 0 FWD; Step 1, the base, at most six below-3
     level totals; Steps 3 and 4' FIN; Step 4, the top's expansion theorem, one level above 3 for its Step 0 and three
     III.A Proposition 4.2 (2) applications in its Step 1 (vi), (viii), (ix), each <= 3 P_iota + 47 + X_7(alpha) + 5.
     M_a, M_b are the largest totals of one level above and below 3 with their loops (the per-level maxima of the
     rounds at the record's weights, P_W, P_iota, W, the excess 47 and X_7(alpha) = (Sum X_7 + the uniform bound's
     excess)/L_above, read from dnumber5.out, pinned by md5). Pinned: B_once and d <= A' + (K + 1) c' + B_once.
  M5 (READ; computed; Round 9, the round-8 verifier's MAJOR 2) the four admissibility conditions dweights5 W1 left
     undecided: (G) and eta_1, eta_2 off Re Lambda are decided (admissibility()); the levels off I11:156-160's
     exclusion sets and eps, eps' off I9:290-291's and I14:124-126's are not (they need the roots -mu as numbers).
  Controls (each mutates the computed path and must fail): C1 TABLE with one row dropped: one hit unclassified;
  C2 FAM with the L-hat pattern dropped: the census's hit count and the charged sites change; C3 Corollary 4.5
  charged at J3's l instead of l + 1: c' leaves its pin; C4 the level-1 Proposition 4.4 read per exponent (3, the
  constant's level-2 reading) instead of per (alpha_0, k): c' leaves its pin; C5 the one-off application on R0 (12):
  c' leaves its pin; C6 a moved anchor (a range's opening line searched one line off): the range check fails; C7 M_a
  without its X_7(alpha) term: B_once leaves its pin.

    python3 checks/modcount5.py        (seconds)
"""
import builtins
import contextlib
import hashlib
import io
import math
import os
import re
import sys
import textwrap
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.join(HERE, '..', 'proof5')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import dweights5 as DW        # noqa: E402  (W1 weights, data_ECI, prop21_steps)
    import prop31loss5 as P31     # noqa: E402  (the chain of III.I' Proposition 3.1)
    import d0count5 as DC         # noqa: E402  (FWD's D_0 and D_1)
    import dnumber5 as DN         # noqa: E402  (A', K + 1, k_1(2))

OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def ceil(x):
    return -((-x.numerator) // x.denominator) if isinstance(x, Fr) else math.ceil(x)


def pos(x):
    return x if x > 0 else Fr(0)


# ------------------------------------------------------------------------------------------------ M0: files, ranges
FILES = {'I15': ('PART-III-I15-AUGMENT5.md', '4f0a21de68ee1dc4da5b7b6543aab524'),
         'I14': ('PART-III-I14-LEVELS.md', 'd9a6893d2e57709d38ceae41b2b441ea'),
         'I12': ('PART-III-I12-SPECTRAL.md', '625e9374d22531b41c8e545dbac3427b'),
         'I11': ('PART-III-I11-SPACETIME.md', '6e227bf7766fbe6b32949939b9235ed7'),
         'I9': ('PART-III-I9-COMMOTION.md', 'ac9ba304de45a96da478856a208681fb'),
         'I7': ('PART-III-I7-PARAMS.md', '3d1b9f6fd0893d64fad5b6e522da3901'),
         'J3': ('PART-III-J3-TAME.md', '441cb3b68d52b1f5472e262e6cf29ef1'),
         'G2': ('PART-II-G2-DECAY.md', '7569ccfeffdb1aad0d3f35723ce5d2c8'),
         'I6': ('PART-III-I6-ALMOSTBDD.md', 'ee25c6f61f93e6e5187f370f7ba85133'),       # Round 10: the base
         'I4': ('PART-III-I4-BOOST.md', 'ccac9618387c9344f4e96974b33759e4'),
         'I3': ('PART-III-I3-ALMOST.md', '3dacc6ad937d509274579b06253cae5d')}
# (key, first line, last line, the text the first line must contain)
ANCHORS = [('I15', 323, 352, '*Step 2 (one level).*'),
           ('I14', 101, 170, "*Proof.* III.I$''''''''''$ Proposition 3.1 holds at the admissible $\\beta$"),
           ('I12', 110, 236, '**Lemma 2.1 (zero energy with expansions).**'),
           ('I12', 246, 428, '*Proof.* *Step 0 (decomposition and transform;'),
           ('I11', 349, 403, "*Proof.* The construction is III.I$'''''$'s Steps 1-2"),
           ('I9', 206, 342, "*Proof.* Steps 0-2 of III.I$''''''$ Proposition 2.1's proof change."),
           ('I7', 190, 333, '*Step 3 (the decomposition).*')]
# lines whose content pins a weight or a loss formula used below (READ)
PINS = [('J3', 'III.I$\'\'$ Lemma 4.1 composes this with (e) and the invertibility of III.H Corollary 4.4'),
        ('J3', 'III.H Proposition 3.2 ($\\widetilde{L_b}(0)^{-1}$, loss\n1)'),
        ('J3', '$\\|Au\\|_k\\le C_k(\\|u\\|_{k+2}+\\|\\beta\\|_{k+d}\\|u\\|_{d})$'),
        ('G2', 'So $\\ell := 2\\ell_3+\\ell_4+\\ell_5$.'),
        ('G2', '(4.4) holds with $\\ell := \\ell_1+\\ell_2+2N+\\lceil(\\delta_2-\\delta_1)_+\\rceil$.'),
        ('G2', '(1) (*Low energies.*) Let $\\ell := \\lceil(\\max(\\beta_\\iota-\\beta_{\\mathrm{scf}},\\beta_K)+'
               '\\epsilon-\\frac12)_+\\rceil$.'),
        ('I12', 'III.I$\'\'$ Lemma 4.1 ($\\beta^f_I = \\ell_I$, $\\beta_\\iota = w_+-2-\\epsilon$,'),
        ('I12', 'Lemma 2.1 with $\\mu_0 := 3-\\epsilon$, $\\mu\' := w_+-1-\\epsilon$'),
        ('I12', 'Lemma 2.1 with $\\mu_1 :=\n2+\\eta_1$, $\\mu\' := 3+\\epsilon_+-\\epsilon$'),
        ('I12', 'Then Lemma 2.1 with $\\mu_2 := 2+\\eta_2$, $\\mu\' := 2+\\epsilon_+-\\epsilon$'),
        ('I12', 'Lemma 2.1 with $\\mu_3 := \\tau-\\epsilon$, $\\mu\' := \\tau$'),
        ('I7', 'III.I$\'\'$ Lemma 4.1 ($\\beta^f_I = \\ell_I$, $\\beta_\\iota = 2-\\epsilon$,'),
        ('I14', 'the zero-energy solve of level 3 (III.I$\'\'\'\'\'\'\'\'\'\'\'$ Lemma\n2.1 with $\\mu_3$) is omitted')]


def lines_of(key):
    return open(os.path.join(P5, FILES[key][0]), encoding='utf-8').read().split('\n')


def file_ok():
    out = {}
    for k, (f, m) in FILES.items():
        out[k] = hashlib.md5(open(os.path.join(P5, f), 'rb').read()).hexdigest() == m
    return out


def ranges_ok(anchors=ANCHORS, shift=0):
    return all(t in lines_of(k)[a - 1 + shift] for k, a, b, t in anchors)


def pins_ok():
    res = []
    for k, t in PINS:
        txt = '\n'.join(lines_of(k))
        res.append(txt.count(t) >= 1)
    return all(res), len(res)


# ------------------------------------------------------------------------------------------------ M1: the census
FAM = [('FWD', r"forward solution"),
       ('BG', r"\(L-L_\{?b(?:_0)?\}?\)u|R_qu|\\Delta_q\(|\(L_j-L_\{b_0\}\)u_j"),
       ('LHAT', r"\\widehat\{L_\{?b(?:_0)?\}?\}\(\\sigma\)|\\widehat\{L_b\}\(\\sigma\)|L_\{?b(?:_0)?\}?\(u_|"
                r"L_\{?b(?:_0)?\}?u_\{?[IF\\]|L_bu\^\\flat|L_\{b_0\}v"),
       ('ZE', r"III\.H Proposition 3\.2|\\tilde L_\{?b(?:_0)?\}?\(0\)\^\{-1\}"),
       ('LF', r"\\tilde L_\{?b(?:_0)?\}?\(\\sigma\)\^\{-1\}|III\.H Corollary 4\.[0-9]"),
       ('A42', r"III\.A Proposition 4\.2(?: \([12]\))?|\(2\.2[56][ab]\)|II\.G\$'\$ Propositions? 3\.[35](?: \([12]\))?"),
       ('A14', r"III\.A Lemma 1\.4"),
       ('INTA', r"III\.A Lemmas? (?:1\.2|3\.2)"),
       ('I3', r"III\.I\$''\$ Lemmas? [1-4]\.[0-9](?: \([12]\))?"),
       ('I2', r"III\.I\$'\$ Propositions? [23]\.1"),
       ('GM', r"III\.G\$'+\$ (?:Propositions?|Corollary|Theorem) [0-9.]+[0-9]"),
       ('FC', r"III\.F\$'\$ Corollary 3\.4|II\.G\$'\$ Corollary 4\.[25]"),
       ('ROUTE', r"III\.I\$'{5,13}\$ (?:Propositions?|Lemmas?|Steps?|Theorem) [0-9.]+[0-9]+(?:-[0-9.]+)?"),
       ('INT', r"(?<![$'] )(?<!III\.H )(?<!III\.A )\bLemmas? [1-5]\.[0-9](?: \([a-z0-9]\))?")]


def hits(fam=FAM, anchors=ANCHORS):
    for k, a, b, _ in anchors:
        L = lines_of(k)
        for i in range(a, b + 1):
            seen = []
            for tag, p in fam:
                for m in re.finditer(p, L[i - 1]):
                    if any(s <= m.start() < e for s, e in seen):
                        continue
                    seen.append((m.start(), m.end()))
                    yield k, i, tag, m.group(0)


S, F0, BASE, TOP, REPL, RT = 'stmt', 'fin0', 'base', 'top', 'replaced', 'route'
CNT = 'counted'
# (file, line, tag): class or ('charge', id) or ('counted', what)
TABLE = {
    # I15 Step 2 (one level)
    ('I15', 327, 'BG'): ('charge', 'BG_I15'), ('I15', 328, 'BG'): S, ('I15', 329, 'INT'): S, ('I15', 330, 'BG'): S,
    ('I15', 330, 'INT'): S, ('I15', 331, 'ROUTE'): F0, ('I15', 332, 'BG'): S, ('I15', 333, 'INT'): S,
    ('I15', 340, 'ROUTE'): F0, ('I15', 342, 'ROUTE'): RT, ('I15', 342, 'INT'): TOP, ('I15', 346, 'ROUTE'): RT,
    # I14 Proposition 2.1 and Lemma 2.2 (the changes at every level)
    ('I14', 101, 'ROUTE'): RT, ('I14', 104, 'ROUTE'): RT, ('I14', 104, 'INT'): S,
    ('I14', 110, 'GM'): S, ('I14', 116, 'ROUTE'): S, ('I14', 122, 'GM'): (CNT, 'R3 (level-3 rounds, 3 each)'),
    ('I14', 129, 'I3'): S, ('I14', 137, 'ROUTE'): S, ('I14', 139, 'ROUTE'): F0, ('I14', 152, 'ROUTE'): S,
    ('I14', 152, 'INT'): S, ('I14', 161, 'ROUTE'): S, ('I14', 163, 'ROUTE'): RT, ('I14', 164, 'ROUTE'): RT,
    ('I14', 165, 'BG'): S, ('I14', 167, 'ROUTE'): S, ('I14', 170, 'INT'): S,
    # I12 Lemmas 2.1-2.5 (their content; charged where applied)
    ('I12', 110, 'INT'): S, ('I12', 112, 'ZE'): S, ('I12', 115, 'A14'): S, ('I12', 118, 'ROUTE'): S,
    ('I12', 120, 'ZE'): S, ('I12', 121, 'ROUTE'): S, ('I12', 123, 'INT'): S, ('I12', 131, 'INT'): S,
    ('I12', 133, 'INT'): S, ('I12', 135, 'LHAT'): S, ('I12', 145, 'LHAT'): S, ('I12', 154, 'INT'): S,
    ('I12', 163, 'GM'): S, ('I12', 163, 'INT'): S, ('I12', 168, 'ROUTE'): S, ('I12', 169, 'ROUTE'): S,
    ('I12', 186, 'ROUTE'): S, ('I12', 193, 'INT'): S, ('I12', 204, 'INT'): S, ('I12', 212, 'A42'): S,
    ('I12', 212, 'I3'): S, ('I12', 216, 'I3'): S, ('I12', 220, 'INT'): S, ('I12', 221, 'LHAT'): S,
    ('I12', 222, 'ROUTE'): S, ('I12', 224, 'LF'): S, ('I12', 226, 'LHAT'): S, ('I12', 229, 'LHAT'): S,
    ('I12', 232, 'LHAT'): S, ('I12', 232, 'ROUTE'): S, ('I12', 233, 'LHAT'): S, ('I12', 236, 'INT'): S,
    # I12 Proposition 3.1 (Steps 0-7) and Lemma 3.2
    ('I12', 247, 'I3'): ('charge', 'L41_above'), ('I12', 249, 'A42'): (CNT, "Step 0's 11 + n_iota"),
    ('I12', 255, 'INT'): S, ('I12', 257, 'INT'): ('charge', 'ZE_0'), ('I12', 260, 'ROUTE'): S,
    ('I12', 261, 'ROUTE'): S, ('I12', 262, 'INT'): ('charge', 'LH_0'), ('I12', 266, 'GM'): ('charge', 'P44_L1'),
    ('I12', 269, 'LHAT'): S, ('I12', 271, 'INT'): ('charge', 'ZE_1'), ('I12', 274, 'INT'): ('charge', 'LH_1'),
    ('I12', 279, 'GM'): (CNT, 'X_2 = P_W (level-2 rounds, 3 each)'), ('I12', 282, 'INT'): ('charge', 'ZE_2'),
    ('I12', 283, 'INT'): ('charge', 'LH_2'), ('I12', 288, 'GM'): (CNT, 'R3 (level-3 rounds, 3 each)'),
    ('I12', 299, 'INT'): ('charge', 'ZE_3'), ('I12', 302, 'LHAT'): ('charge', 'LH_3'), ('I12', 304, 'INT'): S,
    ('I12', 305, 'I3'): ('charge', 'L42_L3'), ('I12', 310, 'INT'): S, ('I12', 316, 'INT'): S,
    ('I12', 325, 'INT'): S, ('I12', 327, 'A42'): S, ('I12', 330, 'INT'): F0, ('I12', 340, 'INT'): F0,
    ('I12', 348, 'INT'): ('charge', 'A422_col'), ('I12', 350, 'A42'): ('charge', 'A26_iii'),
    ('I12', 352, 'INT'): S, ('I12', 359, 'ROUTE'): F0, ('I12', 374, 'ROUTE'): S, ('I12', 382, 'ROUTE'): F0,
    ('I12', 390, 'GM'): S, ('I12', 392, 'A42'): S, ('I12', 392, 'ROUTE'): S,
    ('I12', 393, 'A42'): (CNT, 'X_7 (III.A Proposition 4.2 (2) at Step 7)'), ('I12', 397, 'ROUTE'): S,
    ('I12', 399, 'I2'): ('charge', 'P21_above'), ('I12', 399, 'ROUTE'): S, ('I12', 400, 'GM'): S,
    ('I12', 400, 'INT'): S, ('I12', 401, 'A42'): S, ('I12', 403, 'INT'): S,
    ('I12', 414, 'BG'): ('charge', 'BG_L32'), ('I12', 415, 'BG'): S, ('I12', 415, 'INT'): S,
    ('I12', 418, 'ROUTE'): RT, ('I12', 419, 'FWD'): ('charge', 'FWD_above'), ('I12', 419, 'LHAT'): S,
    ('I12', 422, 'ROUTE'): S,
    # I11 Proposition 3.1 at beta (Steps 1-2, the rows)
    ('I11', 349, 'ROUTE'): S, ('I11', 354, 'I2'): ('charge', 'P31_I11'), ('I11', 365, 'INT'): S,
    ('I11', 381, 'I2'): (CNT, 'the windows, 15 W per level (R2.3 (c))'), ('I11', 384, 'INT'): S,
    ('I11', 386, 'ROUTE'): S, ('I11', 390, 'INT'): F0, ('I11', 395, 'ROUTE'): S, ('I11', 398, 'ROUTE'): S,
    ('I11', 403, 'FWD'): S,
    # I9 Lemma 3.1 (Step 0 base only; Steps 1-2 used by Lemma 3.2) and Lemma 3.2
    ('I9', 206, 'ROUTE'): BASE, ('I9', 209, 'LHAT'): BASE, ('I9', 213, 'BG'): BASE, ('I9', 214, 'FWD'): BASE,
    ('I9', 215, 'BG'): BASE, ('I9', 215, 'LHAT'): BASE, ('I9', 216, 'FWD'): BASE, ('I9', 217, 'ROUTE'): BASE,
    ('I9', 218, 'BG'): BASE, ('I9', 220, 'BG'): S, ('I9', 220, 'I2'): (CNT, "the one-off application (48 of the 58)"),
    ('I9', 221, 'LHAT'): S, ('I9', 222, 'LHAT'): S, ('I9', 229, 'GM'): (CNT, 'the iota+ loop, 15 W per level'),
    ('I9', 236, 'ROUTE'): BASE, ('I9', 236, 'INT'): BASE, ('I9', 237, 'BG'): BASE, ('I9', 239, 'INT'): S,
    ('I9', 241, 'FWD'): S, ('I9', 251, 'BG'): ('charge', 'BG_L32b'), ('I9', 252, 'INT'): S, ('I9', 256, 'INT'): RT,
    ('I9', 260, 'LHAT'): ('charge', 'FWD_below'), ('I9', 263, 'GM'): (CNT, 'the iota+ loop, 15 W per level'),
    ('I9', 266, 'GM'): S, ('I9', 268, 'INT'): S, ('I9', 272, 'INT'): S, ('I9', 278, 'A42'): S, ('I9', 278, 'I3'): S,
    ('I9', 278, 'GM'): S, ('I9', 285, 'GM'): (CNT, 'R2 (tf rounds, 3 each)'), ('I9', 293, 'LHAT'): S,
    ('I9', 296, 'ROUTE'): S, ('I9', 297, 'LHAT'): S, ('I9', 299, 'LHAT'): S, ('I9', 305, 'I3'): ('charge', 'L42_34'),
    ('I9', 311, 'LF'): F0, ('I9', 314, 'LF'): S, ('I9', 315, 'LHAT'): S, ('I9', 316, 'LHAT'): S,
    ('I9', 317, 'ROUTE'): S, ('I9', 318, 'ROUTE'): F0, ('I9', 320, 'ROUTE'): S, ('I9', 338, 'I2'): ('charge',
                                                                                              'P21_below'),
    ('I9', 341, 'ROUTE'): S, ('I9', 341, 'INT'): S,
    # I7 Proposition 2.1, Steps 3-3.3 and 4-6 (Steps 3.4-3.5 replaced by I9's 3.4'-3.5')
    ('I7', 191, 'LF'): S, ('I7', 194, 'I3'): ('charge', 'L41_below'), ('I7', 196, 'A42'): ('charge', 'A25a_b'),
    ('I7', 202, 'ZE'): ('charge', 'ZE_31'), ('I7', 205, 'ROUTE'): S, ('I7', 212, 'LHAT'): ('charge', 'LH_31'),
    ('I7', 215, 'INT'): S, ('I7', 224, 'ZE'): S, ('I7', 225, 'GM'): ('charge', 'P51_32'), ('I7', 231, 'LHAT'): S,
    ('I7', 236, 'INT'): S, ('I7', 237, 'LHAT'): S, ('I7', 238, 'LHAT'): S, ('I7', 239, 'INT'): S,
    ('I7', 240, 'INT'): S, ('I7', 244, 'ZE'): ('charge', 'ZE_33'), ('I7', 246, 'ZE'): S, ('I7', 247, 'INT'): S,
    ('I7', 249, 'LHAT'): ('charge', 'LH_33'), ('I7', 254, 'I3'): REPL, ('I7', 257, 'LF'): REPL,
    ('I7', 261, 'LF'): F0, ('I7', 270, 'INT'): S, ('I7', 272, 'INT'): S, ('I7', 274, 'INT'): S,
    ('I7', 287, 'A42'): ('charge', 'A26_4'), ('I7', 292, 'I3'): F0, ('I7', 302, 'A42'): S,
    ('I7', 307, 'A42'): ('charge', 'A26_5'), ('I7', 308, 'I3'): F0, ('I7', 324, 'I2'): S, ('I7', 326, 'FWD'): S,
    ('I7', 331, 'A42'): S, ('I7', 331, 'I3'): S, ('I7', 331, 'GM'): S, ('I7', 331, 'INT'): S,
}


def census(table=TABLE, fam=FAM, anchors=ANCHORS):
    rows, uncl, used = [], [], set()
    for k, i, tag, t in hits(fam, anchors):
        key = (k, i, tag)
        if key not in table:
            uncl.append((k, i, tag, t))
            continue
        used.add(key)
        rows.append((key, t, table[key]))
    stale = [key for key in table if key not in used]
    return rows, uncl, stale


# ------------------------------------------------------------------------------------------------ M2: the charges
def the_weights():
    w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))   # dweights5 W1
    w['w_plus'] = 5 + w['eps_p']                                            # I11:32
    return w


def fwd_loss():
    """III.I Theorem 5.3's loss D_0 + D_1 + d' + d'' + 6, from d0count5 as corrected in Round 8 (the verifier's A, A2):
    Sobolev orders Q4R, every operator order in the box BOX (Q3b)"""
    c = DC.counts(*DC.Q4R, MU_BOX=DC.BOX)
    return c['FWD'], c['D0'], c['D1']


def lF(b_scf, b_iota, b_K, eps):
    """II.G' Proposition 3.5 (1)'s loss, at the target weights (b_scf of the source, b_iota, b_K of the target)"""
    return ceil(pos(max(b_iota - b_scf, b_K) + eps - Fr(1, 2)))


def lemma41(bI, b_iota, bK_lo, bK_hi, eps, No=Fr(21, 10), s_hi=3, rgap=2, plus_one=True):
    """III.I'' Lemma 4.1 at input weights (bI + 1, b_iota + 2, b_K), b_K in [bK_lo, bK_hi], output
    (3/2 - eps, No, No): every map it uses, summed"""
    bIo = Fr(3, 2) - eps
    l5 = max(ceil(pos(Fr(1, 2) - min(bK, b_iota + 1 - bI))) for bK in (bK_lo, bK_hi))
    l3 = 1 + ceil(pos(max(No, No - bIo) - Fr(1, 2)))
    l1 = max(ceil(pos(Fr(s_hi) - 1)), rgap)
    l2 = 0                                                                   # inf r = r_out, s >= 0
    Nb = max(ceil(pos(Fr(0)) + 1), 0)                                        # N_0 = 1 (b = 0), N_1 = 0
    l4 = l1 + l2 + 2 * Nb + 0
    cor45 = 2 * l3 + l4 + l5 + (1 if plus_one else 0)                       # J3 (f): l + 1
    l23 = max(ceil(pos(0 + 3 - (Fr(3, 2) - eps))), ceil(pos(Fr(s_hi) - 1)))  # (2.3), theta_in = 0
    p35a = lF(Fr(3, 2) - 2 * eps, No, No, eps)
    p35b = 0 + ceil(pos(max(No, No - bI) - Fr(1, 2)))                       # delta >= 3/2: every sigma-weight
    parts = dict(cor45=cor45, l3=l3, l4=l4, l5=l5, a225=1, b225=l5, cor42=l23, p35_1=p35a, p35_2=p35b)
    return sum(v for k, v in parts.items() if k in ('cor45', 'a225', 'b225', 'cor42', 'p35_1', 'p35_2')), parts


def lemma14_apps(mu, mup):
    return ceil(mup - mu) + 1


def charges(w, oneoff_reading=7, level1_per_exponent=False, cor45_plus_one=True):
    eps, ep, eK, lI = w['eps'], w['eps_p'], w['eps_K'], w['lI']
    alpha_hi = 4 + eK                                                        # the top level, I15:37
    wp = w['w_plus']
    fwd, D0, D1 = fwd_loss()
    T = DN.logs_tables()
    k12 = DN.special_logs(T, 'R1', 'wide')['k12']
    oneoff = {M: 2 * P31.chain(DW.data_ECI(M), lI)[2] for M in (1, 4, 7)}
    steps21, floor21 = DW.prop21_steps(lI, eps)
    ch = {}
    # above 3
    ch['FWD_above'] = ('above', fwd, 'FWD: D_0 + D_1 + d\' + d\'\' + 6 = %d + %d + 8 + 9 + 6' % (D0, D1))
    ch['BG_I15'] = ('both', 2, "BG: R_q u, Delta_q(p') (I15:327-332)")
    ch['BG_L32'] = ('above', 2, 'BG: (L - L_b0) u (I12:414, I14:165)')
    ch['P31_I11'] = ('above', oneoff[oneoff_reading], "III.I' Proposition 3.1, the one-off application to E^C_I "
                     "(R0 %d, R1 4 rounds %d, 7 rounds %d)" % (oneoff[1], oneoff[4], oneoff[7]))
    la, pa = lemma41(lI, wp - 2 - eps, 3 - eps, alpha_hi - eps, eps, plus_one=cor45_plus_one)
    ch['L41_above'] = ('above', la, "III.I'' Lemma 4.1 (Cor 4.5 %d = 2 l_3 + l_4 + l_5 + 1, l_3 %d, l_4 %d, l_5 %d; "
                       "(2.25a) 1, (2.25b) %d, Cor 4.2 (2) %d, Prop 3.5 (1) %d, (2) %d)" % (
                           pa['cor45'], pa['l3'], pa['l4'], pa['l5'], pa['b225'], pa['cor42'], pa['p35_1'],
                           pa['p35_2']))
    mus = {0: (3 - eps, wp - 1 - eps), 1: (2 + w['eta1'], 3 + ep - eps), 2: (2 + w['eta2'], 2 + ep - eps),
           3: (3 - eps - eps, 3 - eps)}                                      # level 3: mu_3 = tau - eps, mu' = tau < 3
    for j in range(4):
        n = lemma14_apps(*mus[j])
        lv = 'above>4' if j == 3 else 'above'
        ch['ZE_%d' % j] = (lv, 1 + 2 * n, 'level %d: III.H Proposition 3.2 1 + III.A Lemma 1.4 2 x %d' % (j, n))
        ch['LH_%d' % j] = (lv, 2, 'level %d: L-hat(sigma) applied (Lemma 2.2%s)' % (j, '' if j < 3 else ', g_J'))
    ch['P44_L1'] = ('above', 3 * (1 if level1_per_exponent else k12 + 1),
                    'level 1: III.G\'\'\'\' Proposition 4.4 at the exponent 2, 3 x %s' % (
                        '1 (per exponent)' if level1_per_exponent else '(k_1(2) + 1) = 3 x %d' % (k12 + 1)))
    ch['L42_L3'] = ('above', 2, "level 3: III.I'' Lemma 4.2, (2.4)")
    # Step 5 (iii): sigma^3 u_f etc.: b_scf = 3/2 - 3 eps, b_iota = tau + 2 - eps, tau < beta - 1 - eps or < 3,
    # b_K = l_3 + 4 = beta - eps, worst at the top level
    tau_hi = max(alpha_hi - 1 - eps, Fr(3))
    ch['A26_iii'] = ('above', lF(Fr(3, 2) - 3 * eps, tau_hi + 2 - eps, alpha_hi - eps, eps),
                     "Step 5 (iii): (2.26a) at the last level's pieces")
    a3 = alpha_hi - 4 - eps                                                  # l_3 at the top level (a of Lemma 2.4)
    colb = lF(Fr(10 ** 6), a3 + 5 - eps, a3 + 3, eps)     # sigma^2 G_1: K+-weight a + 3 (Lemma 2.4), iota+ a + 5 - eps
    cols = lF(Fr(10 ** 6), a3 + 5 - eps, a3 + 2, eps)     # sigma G_2: K+-weight a + 2, iota+ taken a + 5 - eps too
    ch['A422_col'] = ('above', colb + cols, 'Lemma 2.4 at j = 3: III.A Proposition 4.2 (2), n_iota = n_K = 0, l_F '
                      '%d + %d' % (colb, cols))
    ch['P21_above'] = ('above', 2 * (steps21 + 1), "III.I' Proposition 2.1 at Step 7: 2 x (%d + 1)" % steps21)
    # below 3: beta in (2, 3), alpha_K = beta - eps' in (2, 3)
    ch['FWD_below'] = ('below', fwd, 'FWD (u^flat)')
    ch['BG_L32b'] = ('below', 2, 'BG: (L - L_b) u (I9:251)')
    lb, pb = lemma41(lI, 2 - eps, Fr(2), Fr(3), eps, plus_one=cor45_plus_one)
    ch['L41_below'] = ('below', lb, "III.I'' Lemma 4.1 (Cor 4.5 %d, l_5 %d; the rest as above)" % (pb['cor45'],
                                                                                                  pb['l5']))
    ch['A25a_b'] = ('below', 1, '(2.25a): II.G\' Proposition 3.3 (1), loss 1 (J3 (e))')
    ch['ZE_31'] = ('below', 1, 'Step 3.1: III.H Proposition 3.2')
    ch['LH_31'] = ('below', 2, 'Step 3.1: L-hat(sigma) in f_2')
    ch['P51_32'] = ('below', 3, 'Step 3.2: III.G\'\'\'\' Proposition 5.1, one application (2 + 1)')
    ch['ZE_33'] = ('below', 1, 'Step 3.3: III.H Proposition 3.2')
    ch['LH_33'] = ('below', 2, 'Step 3.3: L-hat(sigma) in f_5')
    ch['L42_34'] = ('below', 2, "Step 3.4': III.I'' Lemma 4.2, (2.4)")
    ch['A26_4'] = ('below', lF(Fr(3, 2) - 3 * eps, 2 - 2 * eps, Fr(3) - 1, eps), 'Step 4: (2.26a), b_K = alpha_K - 1')
    ch['A26_5'] = ('below', lF(Fr(10 ** 6), 3 - eps, Fr(3) - 1, eps), 'Step 5: (2.26a) on d_t u_sing')
    ch['P21_below'] = ('below', 2 * (steps21 + 1), "III.I' Proposition 2.1 at Step 8: 2 x (%d + 1)" % steps21)
    meta = dict(fwd=fwd, D0=D0, D1=D1, k12=k12, oneoff=oneoff, steps21=steps21, floor21=floor21)
    return ch, meta


def totals(ch):
    ab = sum(v for lv, v, _ in ch.values() if lv in ('above', 'above>4', 'both'))
    be = sum(v for lv, v, _ in ch.values() if lv in ('below', 'both'))
    return ab, be, max(ab, be)


C_PIN, D_PIN = 668, 45661455037615687


# ------------------------------------------------------------------------------------------------ M4: the one-off steps
DN_OUT = os.path.join(HERE, 'dnumber5.out')
DN_OUT_MD5 = '3db10f0e1cea470f903b38060a8b352c'


def dn_counts():
    """P_W, P_iota, W, Sum X_7 (R1, wide) and the uniform bound's excess, read from dnumber5.out (pinned by md5)"""
    txt = open(DN_OUT, encoding='utf-8').read()
    flat = ' '.join(txt.split())
    m1 = re.search(r'P_W = (\d+), P_iota = (\d+), W = (\d+)', flat)
    m2 = re.search(r'K4 R1/wide: sum over the levels above 3 of X_7 = (\d+)', flat)
    m3 = re.search(r'would give (\d+) more', flat)
    ok = hashlib.md5(txt.encode('utf-8')).hexdigest() == DN_OUT_MD5 and m1 and m2 and m3
    return ok, dict(P_W=int(m1.group(1)), P_iota=int(m1.group(2)), W=int(m1.group(3)), SX7=int(m2.group(1)),
                    unif=int(m3.group(1)))


def one_offs(w, cab, cbe, x7_term=True, fwd=None, nb=2, ch=None, meta=None, aK2=None, windows=True):
    """the steps of III.I with fourteen primes, Theorem 3.1, outside its levels (I15:296-452), itemised (Round 9, the
    round-8 verifier's minor 1; Round 10, the round-9 verifier's MAJOR A: the base counted; deduced on the reading,
    each term an upper bound):
      Step 0, the forward solution: FWD;
      Step 1, the base level, Proposition 4.1 of III.I with eight primes at alpha_1 = 2 + eps_K/2 on the background
        h + h_rem(q) of K+-order (alpha - 2)- (I15:305-308): N = 0 (alpha_0 := alpha_1 < a_K), so its base, Lemma 3.1
        (I9:201-237), with Corollary 4.6 of III.I with seven primes (FIN). Lemma 3.1's Step 0 runs the rounds of
        Proposition 2.1 of III.I with five primes, their Start and its Step 0's loop (M6, base_total: B_base's loops);
        u_F (Step 2 on F_2, the windows) and Steps 1-2 with Steps 3-6 of III.I with six primes, Proposition 2.1, are
        one below-3 level's maps each: nb = 2 totals M_b (Round 9's six, two of them for two rounds, withdrawn);
      Steps 3 and 4': the finite-dimensional inverses (-id + A_k)^-1 and the rotation coordinates: FIN, 0;
      Step 4, Theorem 3.1 of III.I with twelve primes at the top (I13:298-447): its Step 0 runs one more level's maps
        (M_a); its Step 1 (vi), (viii) and (ix) each apply III.A Proposition 4.2 (2) to a zf-remainder (parallel over
        the pieces, Lemma 1.2 (a)), each at most (2.2)'s n_iota + n_K + l_F <= (3 P_iota + 47) + X_7(alpha) + 5
        (n_iota as Step 0's count of E^flat's pairs, n_K at most the top level's X_7, l_F <= 5); (ii)-(v), (vii) and
        Steps 2-6 are statements, Lemma 2.1 (b)'s identities, convolutions in t_* and the subtraction of explicit
        towers (FIN, 0).
    B_once := FWD + B_base + M_a + 3 (3 P_iota + 47 + X_7(alpha) + 5), B_base := the loops + nb M_b."""
    ok, n = dn_counts()
    c = DW.counts(w)
    step = w['eps_ind'] - w['eps']
    r3max = int((w['alpha'] - 2 - w['tau3']) // step) + 1
    r2max = int((3 - w['epsp'] - w['tau0']) // step) + 1
    x7top = (n['unif'] + n['SX7']) // c['levels_above3']
    ok = ok and x7top * c['levels_above3'] == n['unif'] + n['SX7']
    Ma = 3 * r3max + 3 * n['P_W'] + 11 + 3 * n['P_iota'] + 47 + 15 * n['W'] + (x7top if x7_term else 0) + cab
    Mb = 3 * r2max + 15 * n['W'] + 58 + cbe
    zf = 3 * n['P_iota'] + 47 + x7top + 5
    bt = base_total(w, ch, meta, Mb, n['W'], nb=nb, aK2=aK2, windows=windows)
    B = (fwd if fwd is not None else 0) + bt['total'] + Ma + 3 * zf
    return ok, dict(r3max=r3max, r2max=r2max, x7top=x7top, Ma=Ma, Mb=Mb, zf=zf, B=B, levels=c, n=n, base=bt)


def admissibility(w):
    """Round 9 (the round-8 verifier's MAJOR 2): the four admissibility conditions dweights5 W1 left undecided. (G)
    over E_++, G and E_col: decided in rounds 1-2 (dweights5 W2, lambdagen5 L4). eta_1, eta_2 off Re Lambda at W's
    ends (I12:58-60): Lambda has no point with real part in (2, 2 + m) or (3, 3 + m), m = 1.9841e-8 the least offset
    above 2 or 3 (lambdagen5.out L4 over E_col's bases; dweights5.out W2 over the named generators and E^C_I's
    chains, 5.0191e-8; both read and pinned), and 0 < eta_1 < eta_2 < m. The levels off I11:156-160's exclusion sets
    and eps, eps' off I9:290-291's and I14:124-126's: not decided (they need the roots -mu of the class operators and
    of L-hat_b0(0) as numbers, against the rational levels and rounds)."""
    lg = open(os.path.join(HERE, 'lambdagen5.out'), encoding='utf-8').read()
    dw = open(os.path.join(HERE, 'dweights5.out'), encoding='utf-8').read()
    pins = (hashlib.md5(lg.encode('utf-8')).hexdigest() == '03645ae643b694197578381ea7614063'
            and hashlib.md5(dw.encode('utf-8')).hexdigest() == 'db05eeb3a4b5afcc8c18abf8ac837730')
    m1 = re.search(r"L4: \(G\) over L3's bases: least value above 3 is ([0-9.e+-]+)", ' '.join(lg.split()))
    m2 = re.search(r'least value above 2 or 3 is 3 \+ ([0-9.e+-]+)', ' '.join(dw.split()))
    mlo = min(Fr(m1.group(1)), Fr(m2.group(1))) * Fr(9999, 10000)        # rounded down (4 printed digits)
    ok = pins and 0 < w['eta1'] < w['eta2'] < mlo
    return ok, dict(m=mlo, eta1=w['eta1'], eta2=w['eta2'])


# ------------------------------------------------------------------------------------------------ M6: the base level
# Round 10 (the round-9 verifier's MAJOR A). I15 Step 1 runs III.I'''''''' Proposition 4.1 at alpha_1 on the background
# h + h_rem(q), whose K+-order is (alpha - 2)- (I15:305-308, Remark 3.2 (1)), so a_K - 2 < alpha - 4 = eps_K there, not
# h's a_K >= 4 + eps_K (I15:332). Its base, Lemma 3.1 (I9:201-237), runs at its Step 0 the rounds of III.I''''' Proposition
# 2.1 (I6:77-227) up to alpha'_K > alpha_0 + 2 - a_K; their Start is III.I'''' Proposition 4.1 (1), that is III.I'''
# Proposition 2.1 (I5:340-346; I4:132-275), whose Steps 2-3 every round reruns (I6:179-181) and whose Step 0 is III.I''
# Proposition 5.1 (I3:325-427), itself a loop in steps a_K - 2. Those three ranges are scanned here.
BASE_ANCHORS = [('I6', 77, 227, '*Proof of Proposition 2.1.* The proof raises the $K^+$-weight in steps.'),
                ('I4', 132, 275, "*Proof.* *Step 0 (the source's (11.65)).*"),
                ('I3', 325, 427, '*Proof.* *Step 0 (the start).*')]
FAM_B = FAM + [('T53', r"III\.I Theorem 5\.3"), ('P51', r"III\.I\$''\$ Proposition 5\.1"),
               ('LOWI', r"III\.I\$'{3,4}\$ (?:Propositions?|Lemmas?|Steps?) [0-9.]+[0-9]")]
# a citation split over two lines, which no pattern sees: (file, line, the text on that line, class)
XSITES = [('I4', 262, "Proposition 2.1 with $\\ell_+ := \\min(\\ell'_+,", ('start', 'S_P21'))]
# the statements the counts rest on (READ)
BASE_READ = [('I15', 305, "Fix an admissible $\\alpha_1\\in(2,\\alpha-2)$"),
             ('I15', 308, "$K^+$-order $(\\alpha-2)-$ and with the other data of $\\mathcal X$"),
             ('I15', 447, "has $K^+$-order $(\\alpha-2)-$ only, against $a_K\\ge4+\\epsilon_K$ for $h$"),
             ('I9', 201, "Let $\\alpha_0\\in(2,\\min(a_K,2+\\epsilon_{\\mathrm{ind}},\\frac52))$ be admissible"),
             ('I9', 218, "With $\\alpha'_K>\\alpha_0+2-a_K$ (possible, as $a_K>\\alpha_0$)"),
             ('I9', 375, "$\\alpha_{i+1}-\\alpha_i<a_K-2$"),
             ('I6', 81, "with $K^+$-weight $\\alpha'_K\\in(1,\\min(a_K-1,\\frac32,\\alpha_K))$"),
             ('I6', 90, "\\min(\\alpha'_K+a_K-2,\\alpha_K)\\ge\\alpha'_K"),
             ('I6', 110, "If $\\alpha^\\sharp_+<\\lambda_\\sharp$,"),
             ('I6', 223, "Each round raises $\\alpha'_K$ to $\\min(\\alpha'_K+a_K-2,\\alpha_K)$"),
             ('I4', 132, "Fix $\\alpha'_K\\in[\\frac12,1)$ with $\\alpha'_K\\ge\\alpha_K-(a_K-2)$"),
             ('I3', 337, "holds with $(\\alpha'_K,\\beta'_+) = (\\frac12,\\beta^{(0)}_+)$"),
             ('I3', 423, "Each step raises $\\alpha'_K$ by $\\min(a_K-2,\\alpha_K-\\alpha'_K)$")]
WIN = (CNT, 'the iota+ windows of a round with alpha~_K >= lambda_sharp: 15 per window, at most W (15 W per level)')
# (file, line, tag): class, or (kind, charge id): kind 'round' (each round of I6, Steps 0, 1, 4 and u^flat), 'start'
# (the Start's III.I''' pass, Steps 0, 1, 4 and u^flat), 'steps23' (III.I''' Steps 2-3: in every round and in the
# Start), 'zero' (III.I'' Proposition 5.1's Step 0, once), 'iter' (one step of its iteration)
BASE_TABLE = {
    # I6, Proposition 2.1's proof: the Start, Steps 0-4 of a round, the conclusion and continuity
    ('I6', 81, 'LOWI'): RT, ('I6', 87, 'BG'): ('round', 'R_BG'), ('I6', 100, 'BG'): S,
    ('I6', 103, 'I2'): ('round', 'R_P31'), ('I6', 107, 'LHAT'): S, ('I6', 115, 'LHAT'): S, ('I6', 125, 'GM'): WIN,
    ('I6', 129, 'GM'): WIN, ('I6', 134, 'INT'): S, ('I6', 136, 'LHAT'): WIN, ('I6', 143, 'LHAT'): WIN,
    ('I6', 146, 'GM'): WIN, ('I6', 156, 'I2'): WIN, ('I6', 167, 'LHAT'): WIN, ('I6', 175, 'LHAT'): S,
    ('I6', 177, 'FWD'): ('round', 'R_FWD'), ('I6', 180, 'LOWI'): RT, ('I6', 184, 'A42'): S, ('I6', 185, 'I3'): S,
    ('I6', 188, 'ZE'): S, ('I6', 188, 'I3'): S, ('I6', 193, 'LOWI'): S, ('I6', 197, 'I3'): S, ('I6', 199, 'I3'): S,
    ('I6', 209, 'ZE'): S, ('I6', 212, 'LOWI'): S, ('I6', 216, 'I2'): ('round', 'R_P21'), ('I6', 226, 'I2'): S,
    ('I6', 226, 'LOWI'): S,
    # I4, III.I''' Proposition 2.1's proof: Steps 0-1 and 4 (the Start), Steps 2-3 (the Start and every round)
    ('I4', 133, 'P51'): RT, ('I4', 136, 'BG'): ('start', 'S_BG'), ('I4', 142, 'BG'): S,
    ('I4', 145, 'I2'): ('start', 'S_P31'), ('I4', 149, 'LHAT'): S, ('I4', 153, 'LHAT'): S,
    ('I4', 157, 'FWD'): ('start', 'S_FWD'), ('I4', 157, 'LHAT'): S, ('I4', 161, 'ZE'): S,
    ('I4', 162, 'I3'): ('steps23', 'T_L41'), ('I4', 165, 'A42'): ('steps23', 'T_A25'),
    ('I4', 172, 'ZE'): ('steps23', 'T_ZE'), ('I4', 176, 'ZE'): S, ('I4', 184, 'LHAT'): ('steps23', 'T_LH'),
    ('I4', 188, 'INT'): F0, ('I4', 190, 'INT'): F0, ('I4', 196, 'LF'): S, ('I4', 197, 'I3'): ('steps23', 'T_L42'),
    ('I4', 203, 'A42'): ('steps23', 'T_A26'), ('I4', 204, 'A42'): S, ('I4', 209, 'I3'): F0, ('I4', 209, 'INT'): F0,
    ('I4', 215, 'INT'): F0, ('I4', 224, 'I3'): ('steps23', 'T_L31'), ('I4', 228, 'I3'): S, ('I4', 233, 'I3'): F0,
    ('I4', 245, 'A42'): S, ('I4', 271, 'P51'): S,
    # I3, III.I'' Proposition 5.1's proof: Step 0 (once) and the iteration's Steps 1-3
    ('I3', 329, 'T53'): ('zero', 'Z_FWD'), ('I3', 330, 'I2'): ('zero', 'Z_P21'), ('I3', 347, 'BG'): ('iter', 'P_BG'),
    ('I3', 351, 'BG'): S, ('I3', 354, 'I2'): ('iter', 'P_P31'), ('I3', 359, 'LHAT'): S,
    ('I3', 361, 'FWD'): ('iter', 'P_FWD'), ('I3', 361, 'LHAT'): S, ('I3', 364, 'A42'): ('iter', 'P_A25'),
    ('I3', 373, 'INT'): ('iter', 'P_L41'), ('I3', 376, 'INT'): ('iter', 'P_L42'), ('I3', 381, 'A42'): S,
    ('I3', 382, 'A42'): ('iter', 'P_A26'), ('I3', 385, 'INT'): F0, ('I3', 397, 'INT'): ('iter', 'P_L31'),
    ('I3', 402, 'INT'): S, ('I3', 409, 'INT'): F0, ('I3', 417, 'I2'): ('iter', 'P_P21'),
}


def base_reads_ok():
    return all(t in lines_of(k)[i - 1] for k, i, t in BASE_READ)


def base_census(table=BASE_TABLE, fam=FAM_B, anchors=BASE_ANCHORS, xsites=XSITES):
    rows, uncl, stale = census(table, fam, anchors)
    for k, i, t, cls in xsites:
        if t in lines_of(k)[i - 1]:
            rows.append(((k, i, 'X'), t, cls))
        else:
            uncl.append((k, i, 'X', t))
    return rows, uncl, stale


def lemma31(bI, b_iota, bK, eps):
    """III.I'' Lemma 3.1's l (read at source, I3:115-189; J3 (d): "loss l, independent of k, as stated"): the largest
    of II.G' Proposition 2.8 (2)'s l_+ = ceil(beta - 1/2) at beta = gamma + 1, gamma = beta_iota - beta_I (lowered off
    N), for F_1; (2.26a)'s l_F at the K-weight beta_K + 1 on (1 - chi_scf) F f, which vanishes near scf, for F_2; and
    1 (the Sobolev embedding in log |sigma| behind (3.4)); at the given ends of the weights' ranges"""
    out = 1
    for bi in b_iota:
        g = bi - bI
        g = g - eps if g.denominator == 1 else g
        out = max(out, ceil(pos(g + 1 - Fr(1, 2))))
    for k in bK:
        out = max(out, ceil(pos(k + 1 + eps - Fr(1, 2))))
    return out


def base_charges(w, ch, meta, cor45_plus_one=True):
    """the charge of each base site, from the per-step charges of M2 (the same maps) and, where the weights differ,
    the same formulas at the base's weights (deduced; computed), each at the worst end of its range:
    a round (I6): alpha~_K in (1, 2), alpha#_+ in [3/2 - eps, 2); the Start's III.I''' pass: alpha_K in (1, a_K - 1);
    III.I'' Proposition 5.1's iteration: alpha~_K in [1/2, 1), gamma_+ := 3/2 - 6 eps (5.4)"""
    eps, lI = w['eps'], w['lI']
    fwd, p31, p21 = meta['fwd'], ch['P31_I11'][1], ch['P21_below'][1]
    l41r = lemma41(lI, Fr(3, 2) - eps, Fr(1), Fr(2), eps, plus_one=cor45_plus_one)[0]
    l41p = lemma41(lI, Fr(3, 2) - 6 * eps, Fr(1, 2), Fr(1), eps, plus_one=cor45_plus_one)[0]
    b = {}
    for kind, pre in (('round', 'R'), ('start', 'S')):
        b[pre + '_BG'] = (kind, 2, "BG: (L - L_b) u, III.I Proposition 4.1 (4.2) (J3 (b))")
        b[pre + '_P31'] = (kind, p31, "III.I' Proposition 3.1, the one-off application (as P31_I11)")
        b[pre + '_FWD'] = (kind, fwd, 'FWD: u^flat the forward solution (as FWD_below)')
        b[pre + '_P21'] = (kind, p21, "III.I' Proposition 2.1 (as P21_below)")
    b['T_L41'] = ('steps23', l41r, "III.I'' Lemma 4.1 at beta_iota = alpha#_+ >= 3/2 - eps, beta_K in (1, 2)")
    b['T_A25'] = ('steps23', 1, "(2.25a): II.G' Proposition 3.3 (1) (J3 (e))")
    b['T_ZE'] = ('steps23', 1, 'Step 3.1: III.H Proposition 3.2 (J3 (e))')
    b['T_LH'] = ('steps23', 2, 'Step 3.1: L-hat(sigma) in f_2 (as LH_31)')
    b['T_L42'] = ('steps23', 2, "Step 3.2: III.I'' Lemma 4.2, (2.4) (as L42_34)")
    b['T_A26'] = ('steps23', lF(Fr(3, 2) - 2 * eps, Fr(2), Fr(2), eps), 'Step 3.2: (2.26a), beta_K = alpha~_K < 2')
    b['T_L31'] = ('steps23', lemma31(Fr(3, 2), (Fr(5, 2) - eps, Fr(3)), (Fr(0), Fr(1)), eps),
                  "Step 3.3: III.I'' Lemma 3.1 (beta_iota = alpha#_+ + 1, beta_K = alpha~_K - 1 in (0, 1))")
    b['Z_FWD'] = ('zero', fwd, 'Step 0: III.I Theorem 5.3, FWD')
    b['Z_P21'] = ('zero', p21, "Step 0: III.I' Proposition 2.1")
    b['P_BG'] = ('iter', 2, 'Step 1: BG')
    b['P_P31'] = ('iter', p31, "Step 2a: III.I' Proposition 3.1, the one-off application")
    b['P_FWD'] = ('iter', fwd, 'Step 2a: u^flat the forward solution, FWD')
    b['P_A25'] = ('iter', 1, 'Step 2b: (2.25a)')
    b['P_L41'] = ('iter', l41p, "Step 2b: III.I'' Lemma 4.1 at beta_iota = gamma_+, beta_K in [1/2, 1)")
    b['P_L42'] = ('iter', 2, "Step 2b: III.I'' Lemma 4.2, (2.4)")
    b['P_A26'] = ('iter', lF(Fr(3, 2) - 2 * eps, Fr(3, 2) - 6 * eps, Fr(1), eps), 'Step 2b: (2.26a), beta_K < 1')
    b['P_L31'] = ('iter', lemma31(Fr(3, 2), (Fr(2), Fr(5, 2) - 6 * eps), (-Fr(1, 2), Fr(0)), eps),
                  "Step 2b: III.I'' Lemma 3.1 (beta_iota = gamma_+ + 1, beta_K = alpha~_K - 1 in [-1/2, 0))")
    b['P_P21'] = ('iter', p21, "Step 3: III.I' Proposition 2.1")
    tot = {k: sum(v for kd, v, _ in b.values() if kd == k) for k in ('round', 'start', 'steps23', 'zero', 'iter')}
    return b, dict(c_r=tot['round'] + tot['steps23'], c_S=tot['start'] + tot['steps23'], z=tot['zero'],
                   c_51=tot['iter'], steps23=tot['steps23'])


def base_counts(w, aK2=None, theta=Fr(1, 10 ** 9), eta=Fr(1, 10 ** 6)):
    """the loops of the base at an explicit admissible choice (exact rationals), every choice at the economical end of
    its open range: a_K - 2 = (1 - theta) eps_K < alpha - 4 (the background's (alpha - 2)-); Lemma 3.1's alpha_0 :=
    alpha_1 (III.I'''''''' Proposition 4.1 with N = 0: alpha_1 < a_K as a_K - 2 > eps_K / 2); the Start at s_0 := 1 +
    d - eta d < a_K - 1; the target tau := alpha_1 - d + eta d > alpha_0 + 2 - a_K; III.I''''' Proposition 2.1's rounds
    s_i = min(s_0 + i d, tau) up to tau (I6:223), those with s_i >= lambda_sharp running Step 2's windows (I6:110);
    III.I'' Proposition 5.1 at the target t := 1 - eta d / 2 in [s_0 - d, 1) (I4:132), from 1/2 (I3:337) in steps
    min(d, t - alpha'_K) (I3:423). aK2 (a control) replaces a_K - 2."""
    d = aK2 if aK2 is not None else (1 - theta) * w['eps_K']
    a1, ls = w['alpha1'], DW.LSHARP
    s0 = min(1 + d, Fr(3, 2)) - eta * d
    tau = max(a1 - d, Fr(1)) + eta * d
    t = max(min(Fr(1) - eta * d / 2, s0 - d + eta * d / 2), Fr(1, 2))
    R = max(0, ceil((tau - s0) / d))
    i0 = max(1, ceil((ls - s0) / d))
    Rw = R - i0 + 1 if i0 <= R else 0
    n51 = max(0, ceil((t - Fr(1, 2)) / d))
    req = (0 < d < w['alpha'] - 4 and a1 < 2 + d and 1 < s0 < min(1 + d, Fr(3, 2), tau) and a1 - d < tau < 2
           and s0 - d <= t < 1 and s0 + (R - 1) * d < tau <= s0 + R * d and s0 + (i0 - 1) * d < ls <= s0 + i0 * d)
    return dict(d=d, s0=s0, tau=tau, t=t, R=R, Rw=Rw, i0=i0, n51=n51, req=req)


def base_total(w, ch, meta, Mb, W, nb=2, aK2=None, windows=True):
    """B_base := z + n_51 c_51 + c_S + R c_r + R_w 15 W + nb M_b (the two one-level parts of Lemma 3.1: u_F's windows
    on F_2, and its Steps 1-2 with III.I'''''' Proposition 2.1's Steps 3-6), III.I''''''' Corollary 4.6's inverses FIN"""
    b, c = base_charges(w, ch, meta)
    n = base_counts(w, aK2=aK2)
    loops = c['z'] + n['n51'] * c['c_51'] + c['c_S'] + n['R'] * c['c_r'] + (n['Rw'] * 15 * W if windows else 0)
    return dict(b=b, c=c, n=n, loops=loops, total=loops + nb * Mb, win=n['Rw'] * 15 * W)


B_PIN, DTOT_PIN = 3943746411, 45661458981362098


def main():
    print('modcount5: the fixed per-level steps of the beta-levels, read and counted; c\' and d as integers')
    fo = file_ok()
    OK['M0'] = all(fo.values()) and ranges_ok() and pins_ok()[0]
    print('  M0 (READ): %d files at their pinned md5: %s; %d ranges found by content: %s; %d formula lines found: %s'
          % (len(fo), all(fo.values()), len(ANCHORS), ranges_ok(), pins_ok()[1], pins_ok()[0]))
    rows, uncl, stale = census()
    by = {}
    for key, t, cls in rows:
        c = cls if isinstance(cls, str) else cls[0]
        by[c] = by.get(c, 0) + 1
    charged_ids = sorted({cls[1] for _, _, cls in rows if isinstance(cls, tuple) and cls[0] == 'charge'})
    OK['M1'] = not uncl and not stale and len(rows) == 212
    print('  M1 (census): %d hits of the families in the per-level ranges, %d unclassified, %d stale rows; by class: '
          '%s; %d charge ids' % (len(rows), len(uncl), len(stale), dict(sorted(by.items())), len(charged_ids)))
    for u in uncl:
        print('      unclassified %s' % (u,))
    w = the_weights()
    ch, meta = charges(w)
    OK['M2'] = set(charged_ids) == set(ch)
    print('  M2 (charges, at dweights5 W1\'s weights; eps_K = %s < the (G) bound 5.0191e-8): every charged site has a '
          'charge and every charge a site: %s' % (w['eps_K'], OK['M2']))
    for k in sorted(ch, key=lambda x: (ch[x][0], x)):
        lv, v, how = ch[k]
        print('      %-10s %-8s %4d  %s' % (k, lv, v, how))
    ab, be, cp = totals(ch)
    A1 = DN.D_PIN['R1']
    d = A1 + DN.KPLUS1 * cp
    N = 21 * d + 6
    OK['M3'] = (cp, d) == (C_PIN, D_PIN) and meta['fwd'] == 510 and meta['k12'] == 10 and meta['oneoff'][7] == 48
    print('  M3: c\'_above = %d (FWD %d + %d), c\'_below = %d (FWD + %d): c\' = %d; d <= A\' + %d c\' = %d + %d = %d '
          '(%.6e); N = 21 d + 6 <= %d (%.6e); pinned: %s' % (
              ab, meta['fwd'], ab - meta['fwd'], be, be - meta['fwd'], cp, DN.KPLUS1, A1, DN.KPLUS1 * cp, d, d, N, N,
              OK['M3']))
    print('      against round 7\'s c\' in [62, 250 + MODs]: the MODs are %d above 3 and %d below; c\' moves d by %.2e '
          'of itself; the floor 8,407,505,890,317,054 is %.4f of the bound' % (
              ab - meta['fwd'], be - meta['fwd'], DN.KPLUS1 * cp / d, 8407505890317054 / d))
    okb, ob = one_offs(w, ab, be, fwd=meta['fwd'])
    dtot = d + ob['B']
    OK['M4'] = okb and (ob['B'], dtot) == (B_PIN, DTOT_PIN)
    print('  M4 (deduced on the reading; computed; Round 9: itemised): the steps outside the levels, I15 Step 0 (FWD), '
          'Step 1 (the base: at most six below-3 level totals), Steps 3, 4\' (FIN), Step 4 (the top\'s Step 0: one '
          'level above 3; its Step 1 (vi), (viii), (ix): three III.A Proposition 4.2 (2) applications, each <= 3 P_iota '
          '+ 47 + X_7(alpha) + 5 = %d). A level\'s largest totals: above 3 M_a = 3 x %d (level-3 rounds) + 3 P_W + 11 '
          '+ 3 P_iota + 47 + 15 W + X_7(alpha) %d + c\'_above = %d, below 3 M_b = 3 x %d (tf rounds) + 15 W + 58 + '
          'c\'_below = %d (P_W, P_iota, W, Sum X_7 read from dnumber5.out, md5 pinned: %s); B_once := FWD + 6 M_b + '
          'M_a + 3 x %d = %d' % (ob['zf'], ob['r3max'], ob['x7top'], ob['Ma'], ob['r2max'], ob['Mb'], okb, ob['zf'],
                                ob['B']))
    print('      d <= A\' + (K + 1) c\' + B_once = %d (%.10e); N = 21 d + 6 <= %d; B_once is %.2e of d: pinned: %s' % (
        dtot, dtot, 21 * dtot + 6, ob['B'] / dtot, OK['M4']))
    oka, ad = admissibility(w)
    OK['M5'] = oka
    print('  M5 (READ; computed; Round 9): admissibility. (G): decided in rounds 1-2; eta_1 = %.6e < eta_2 = %.6e < '
          '%.4e, the least real part of Lambda above 2 or 3 minus 2 or 3 (lambdagen5.out L4, dweights5.out W2, md5 '
          'pinned), so 2 + eta_1 and 3 + eta_2 are off Re Lambda: decided: %s; the levels off I11:156-160\'s sets and '
          'eps, eps\' off I9:290-291\'s and I14:124-126\'s: not decided (the roots -mu as numbers)' % (
              float(ad['eta1']), float(ad['eta2']), float(ad['m']), oka))
    # controls
    t1 = dict(TABLE)
    t1.pop(('I12', 247, 'I3'))
    _, u1, _ = census(table=t1)
    OK['C1'] = len(u1) == 1
    print('  C1 (control): the row I12:247 (III.I\'\' Lemma 4.1) dropped: %d unclassified: %s' % (len(u1), OK['C1']))
    f2 = [x for x in FAM if x[0] != 'LHAT']
    r2, u2, s2 = census(fam=f2)
    ids2 = {cls[1] for _, _, cls in r2 if isinstance(cls, tuple) and cls[0] == 'charge'}
    OK['C2'] = len(r2) + len(u2) != 212 and set(charged_ids) - ids2 != set()
    print('  C2 (control): the L-hat pattern dropped: %d hits (not 212), charge ids lost %s: %s' % (
        len(r2) + len(u2), sorted(set(charged_ids) - ids2), OK['C2']))
    c3 = totals(charges(w, cor45_plus_one=False)[0])[2]
    OK['C3'] = c3 != C_PIN
    print('  C3 (control): Corollary 4.5 charged l, not l + 1: c\' = %d, not %d: %s' % (c3, C_PIN, OK['C3']))
    c4 = totals(charges(w, level1_per_exponent=True)[0])[2]
    OK['C4'] = c4 != C_PIN
    print('  C4 (control): level 1 per exponent: c\' = %d, not %d: %s' % (c4, C_PIN, OK['C4']))
    c5 = totals(charges(w, oneoff_reading=1)[0])[2]
    OK['C5'] = c5 != C_PIN
    print('  C5 (control): the one-off application on R0 (12): c\' = %d, not %d: %s' % (c5, C_PIN, OK['C5']))
    OK['C7'] = one_offs(w, ab, be, x7_term=False, fwd=meta['fwd'])[1]['B'] != B_PIN
    print('  C7 (control): M_a without X_7(alpha): B_once leaves its pin: %s' % OK['C7'])
    OK['C6'] = not ranges_ok(shift=1)
    print('  C6 (control): every range\'s opening line searched one line off: the anchors fail: %s' % OK['C6'])
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
