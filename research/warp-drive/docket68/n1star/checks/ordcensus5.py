#!/usr/bin/env python3
"""ordcensus5: the orders at which the forward-solution chain invokes the calculus that the write-out fixes by the
closed graph theorem (II.A Lemmas 8.5-8.6, II.A' Lemma 1.2 and Proposition 2.4), read site by site (CONSTANTS5.md,
Round 12; the round-11 verifier's request). Labels: READ (the files md5-pinned, every citation found by content,
across line breaks), deduced (each site's Sobolev and symbol orders, read from its lines as functions of the order
of the statement it sits in, and each statement's order range from the statements that invoke it), computed (the
ranges, exact rationals).

The chain: III.I Theorem 5.3 -> II.F' -> II.C Proposition 5.1's order s (s_out = -8 to s_in = 9, d0count5 Q4/Q4b;
s0 = s - 2 and the slab order s + 1 beside it: every order variable in [-10, 10], oscillation 17) -> II.D Theorem 1.2
(its a priori term: |chi u|_(-N) <= |u|_(s_0) needs N >= 10, II.D:1035; N = 14 is taken, rounds 7-11's value) ->
II.D sections 2-4, II.D', II.E -> II.A' Theorems 3.1 (L3), 5.4 (L4), Lemmas 4.1-4.2, Proposition 5.3.

  O0 (READ) the seven files at their pinned md5; the scope: II.A' sections 3-5 (II.A2:358-785) and all of II.D, II.D',
     II.E, II.F', II.C, II.F.
  O1 (READ; census) every citation of II.A Lemmas 8.5-8.6, II.A' Lemma 1.2, II.A' Proposition 2.4 and of the II.A'
     statements that carry them (Theorems 3.1, 5.4, Lemmas 2.3, 2.5, 4.1, 4.2, Proposition 5.3, (L3)-(L5)), and the bare
     "Proposition 2.4", "Lemma 1.2" (and, in II.A', "Theorem 3.1", "Lemma 4.1-4.2", "Proposition 5.3"), classified:
     a calculus site with its orders, a call (sets the orders of the statement called), a statement, or another
     part's own lemma (II.C/II.E/II.F's Lemma 1.2, II.F's Proposition 2.4, [Hin26c] Lemma 8.5). None unclassified.
  O2 (deduced; computed) the statements' order ranges, from their callers:
     - II.A' Proposition 5.3 at the order s takes tau >= sup s + N (II.A2:726-727), so Lemma 4.2 runs Lemma 4.1 at
       s_j = s - tau + j kappa: s' in [inf s - sup s - N, sup s] = [-31, 10];
     - II.A' Theorem 3.1's iteration at the order s runs r' = s - j/2 until J'/2 >= sup s + N (II.A2:399-401): r' in
       [inf s - sup s - N + 1/2, sup s] = [-30.5, 10], its inputs r' - m;
     - the same scheme with B_0^(j) (order s_j + delta) in place of L (Lemma 4.2's parametrix, II.A2:529-533) and with
       E in place of L (Lemma 4.1 Step 2 (b), II.A2:495): v = s_j or s' in [-31, 10];
     - II.D sections 2-4, II.D', II.E, II.F': the chain's orders s, s_0 = s - 2 and s + 1, tau <= 2 (II.D:287,
       691): v in [-10, 10]; II.D's regulariser exponent kappa := 2 (II.D:221-223, 688) where it enters.
  O3 (computed) every site's orders over its range: the Sobolev orders, the symbol orders and the factor orders of
     Proposition 2.4 (f), against round 8's box ([-16, 11] x [-22, 22], factors [-10.49, 9.51]).
  O4 (READ) K' (II.A2:439) is a regularity assumption only: every K' of the chain is the membership w in H^(K') or
     its definition, never an order at which a site of O3 bounds anything.
  O5 (READ; deduced) N: the chain's a priori term is |chi u|_(-N) <= |u|_(s_0) (II.D:1035), s_0 >= -10, so N >= 10;
     N = 14 serves, and every site's -N, -N - m is in O3's range.
  Controls (each must fail): C1 one census row dropped: one hit unclassified; C2 Proposition 5.3's tau and Theorem
  3.1's J' taken without N and the oscillation (tau = 1): the box shrinks inside round 8's, so O3's finding depends on
  them; C3 a pinned file altered in a copy: O0 fails; C4 N = 10 in place of 14: the box moves.

    python3 checks/ordcensus5.py        (seconds)
"""
import bisect
import builtins
import hashlib
import os
import re
import shutil
import sys
import tempfile
import textwrap
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.join(HERE, '..', 'proof5')
OK = {}


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


FILES = {'A2': ('PART-II-A2-STANDARD.md', '7464b99a67d997206371e4f9cf150b38'),
         'D': ('PART-II-D-REGULARITY.md', '4473cfa5f5c50d2a5280c3c79b9bbcc7'),
         'D2': ('PART-II-D2-BREGULARITY.md', '62f9ca0800ce1a930ece45b2c8e5aab3'),
         'E': ('PART-II-E-ENERGY.md', 'f0b65803a82a3fc55e7e98cb70a55efd'),
         'F2': ('PART-II-F2-TAME.md', 'a12fb8761dec8da205476af0c1f0dc8f'),
         'C': ('PART-II-C-OPERATORS.md', 'c9f01086b4499fa0c549fc9b157dcb8c'),
         'F': ('PART-II-F-IOTA.md', '51c14571e7c29685fb8a757713dc2015')}
RANGES = {'A2': (358, 785)}
FAM = [('A85', r"II\.A Lemmas? 8\.[56](?:-8\.6)?(?: \([ab]\))?"),
       ('A2P', r"II\.A\$'\$ Propositions? 2\.4(?: \([a-f]\)(?:, \([a-f]\))*)?"),
       ('A2L', r"II\.A\$'\$ Lemma 1\.2"),
       ('STM', r"II\.A\$'\$ (?:Theorems? (?:3\.1|5\.4)|Lemmas? (?:2\.[35]|4\.[12])(?:-4\.2)?|Proposition 5\.3)|"
               r"\(L[345]\)"),
       ('BP', r"(?<![$'] )(?<!II\.[A-F] )(?<!\]) ?\bPropositions? 2\.4(?: \([a-f]\)(?:, \([a-f]\))*)?"),
       ('BL', r"(?<![$'] )(?<!II\.[A-F] )(?<!\]) ?\bLemma 1\.2(?: \([a-z]+\))?"),
       ('BT', r"(?<![$'] )(?<!II\.[A-F] )(?<!\]) ?\b(?:Theorem (?:3\.1|5\.4)|Lemma 4\.[12]|Proposition 5\.3)")]

# the chain's parameters (READ: d0count5 Q4/Q4b, II.D:1035, II.D:287, 691)
S_LO, S_HI, OSC, NERR, M_OP = Fr(-10), Fr(10), Fr(17), Fr(14), Fr(2)
DELTA_MAX, KAPPA_MAX = Fr(1, 100), Fr(1, 4)          # delta as d0count5's DELTA; kappa <= 1/4 (Lemma 4.1 (i))
KAPPA_D = Fr(2)                                      # II.D's regulariser exponent, kappa := 2 (II.D:221-223, 688)


def domains(N=NERR, tau_full=True):
    """each statement context's order variable v and its range (O2)"""
    low = -OSC - N if tau_full else S_LO - 1
    return {'T31': (low + Fr(1, 2), S_HI),          # Theorem 3.1's r' at the chain's variable orders
            'L41': (low, S_HI),                      # Lemma 4.1 / Proposition 5.3 at s' = s_j
            'L42P': (low, S_HI),                     # Lemma 4.2's parametrix with B_0^(j) (order s_j + delta)
            'T31E': (low, S_HI),                     # Lemma 4.1 Step 2 (b): Theorem 3.1's scheme with E for L
            'T54': (S_LO, S_HI),                     # Theorem 5.4 at the chain's order
            'D': (S_LO, S_HI),                       # II.D sections 2-4, II.D', II.E, II.F' (s and s_0 = s - 2)
            'C0': (Fr(0), Fr(0))}                    # constant orders


def E(a, lo, hi=None):
    return (Fr(a), Fr(lo), Fr(lo if hi is None else hi))


NN = 'N'      # placeholder for -N (and -N - m) in a site's Sobolev orders
S, CALL, OTHER = 'stmt', 'call', 'other'
d, k_ = DELTA_MAX, Fr(1, 2)                          # (m - 1)/2 = 1/2 at m = 2
# (file, line, tag): class, or ('site', context, Sobolev orders, symbol orders, factor orders of (f))
TABLE = {
    # II.A' Theorem 3.1 (the elliptic estimate), at r' (A of order r = 0, delta = 1/2)
    ('A2', 360, 'BT'): S, ('A2', 360, 'STM'): S,
    ('A2', 379, 'BP'): ('site', 'T31', [E(1, 0), E(1, -1, -k_)], [E(0, -k_), E(0, -2), E(0, 2)], []),
    ('A2', 385, 'A85'): ('site', 'T31', [E(1, -2, 0)], [E(0, -2, 0)], []),
    ('A2', 385, 'BP'): ('site', 'T31', [E(1, -2, 0)], [E(0, -2), E(0, 0)], []),
    ('A2', 389, 'BP'): ('site', 'T31', [E(1, -2, 0)], [E(0, -2), E(0, 0)], []),
    ('A2', 394, 'A85'): ('site', 'T31', [NN], [E(0, 2)], []),
    ('A2', 397, 'BP'): ('site', 'T31', [E(1, -k_, 0)], [E(0, -k_), E(0, 0)], []),
    ('A2', 410, 'BP'): ('site', 'T31', [E(1, -2, 0)], [E(0, -2, 2)], []),
    # Lemma 4.1 (one step), at s' (k = s' - 1/2)
    ('A2', 416, 'BP'): ('site', 'L41', [E(0, -k_, k_)], [E(0, 1, 1 + d)], []),
    ('A2', 420, 'BT'): S, ('A2', 425, 'BT'): S,
    ('A2', 458, 'A85'): ('site', 'L41', [E(1, -1), NN], [E(0, 2)], []),
    ('A2', 460, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(1, -k_), E(0, 0), E(0, 2)], []),
    ('A2', 462, 'BP'): ('site', 'L41', [E(0, -k_), E(1, -1)], [E(1, -k_)], []),
    ('A2', 469, 'BP'): ('site', 'L41', [E(1, -KAPPA_MAX, 0), E(0, k_)], [E(1, -k_ - KAPPA_MAX, -k_)], []),
    ('A2', 474, 'BP'): ('site', 'L41', [E(1, -1), E(0, -k_)], [E(0, 2), E(0, 0), E(0, 1, 1 + d)], []),
    ('A2', 487, 'BP'): ('site', 'L41', [E(0, k_), E(1, -1, -1 + 2 * d)], [E(1, -Fr(3, 2), -Fr(3, 2) + 2 * d),
                                                                          E(0, -k_), E(1, 0, d)], []),
    ('A2', 489, 'BP'): ('site', 'L41', [E(0, k_), E(0, 0)], [E(0, -k_)], []),
    ('A2', 493, 'BP'): ('site', 'L41', [E(1, 0)], [E(1, 0)], []),
    ('A2', 495, 'BT'): CALL,
    ('A2', 502, 'BP'): ('site', 'L41', [E(0, 0)], [E(1, 0, d)], []),
    ('A2', 505, 'BP'): ('site', 'L41', [E(0, 0)], [E(1, 0, d)], []),
    # Lemma 4.2 (iteration) and its parametrix
    ('A2', 510, 'BT'): S, ('A2', 512, 'BT'): CALL, ('A2', 529, 'BT'): CALL,
    ('A2', 531, 'BP'): ('site', 'L42P', [E(1, 0), E(0, 0)], [E(-1, -d, 0), E(1, 0, d), E(0, -1, -1 + 2 * d)], []),
    ('A2', 533, 'BT'): CALL, ('A2', 539, 'BT'): CALL,
    # section 5: the operator, Proposition 5.3 at s' (k = s' - 1/2), Theorem 5.4
    ('A2', 547, 'STM'): S, ('A2', 572, 'BL'): S, ('A2', 612, 'BT'): S,
    ('A2', 673, 'BP'): ('site', 'L41', [E(0, k_)], [E(0, -k_)], []),
    ('A2', 682, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(0, 1), E(0, 2)], [E(0, 1, 2)]),
    ('A2', 685, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(1, 0, k_)], []),
    ('A2', 687, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(2, -1, -1 + d)], []),
    ('A2', 689, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(1, -Fr(3, 2), -Fr(3, 2) + d)], []),
    ('A2', 690, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(2, -1, -1 + d)], [E(1, -k_, -k_ + d), E(0, 2)]),
    ('A2', 695, 'BP'): ('site', 'L41', [E(1, -1, 0)], [E(2, -1, -1 + d), E(0, 1)], [E(1, -k_, -k_ + d), E(0, 1)]),
    ('A2', 701, 'BP'): ('site', 'L41', [E(1, -k_, -k_ + d), NN], [E(2, -1, -1 + d)], []),
    ('A2', 703, 'BP'): ('site', 'L41', [E(1, -k_, 0)], [E(2, -1, 2 * d), E(1, 0, d)], []),
    ('A2', 710, 'BP'): ('site', 'L41', [E(1, -1, 0), E(0, k_)], [E(1, -1, -1 + 2 * d), E(0, k_)], []),
    ('A2', 716, 'BP'): ('site', 'L41', [E(0, -k_, -k_ + d / 2)], [E(1, 0, d / 2)], []),
    ('A2', 722, 'BT'): CALL, ('A2', 723, 'BP'): S, ('A2', 725, 'BT'): CALL,
    ('A2', 746, 'BT'): S, ('A2', 746, 'STM'): S, ('A2', 766, 'BT'): CALL, ('A2', 770, 'BT'): CALL,
    ('A2', 775, 'BT'): CALL, ('A2', 776, 'BT'): S, ('A2', 778, 'BT'): CALL, ('A2', 780, 'BT'): S,
    # II.D: section 1, Lemmas 2.1-2.5, sections 3-4, the global estimate
    ('D', 105, 'A2P'): ('site', 'D', [E(1, -1, 0)], [E(0, -1, 0)], []),
    ('D', 158, 'STM'): S, ('D', 165, 'STM'): S, ('D', 167, 'STM'): CALL,
    ('D', 170, 'A2P'): ('site', 'D', [E(-1, 2, 2 + KAPPA_D), E(1, -KAPPA_D, 0)], [E(2, -2 - 2 * KAPPA_D, -2)], []),
    ('D', 171, 'BP'): ('site', 'D', [E(1, -1), NN], [E(2, -2), E(0, 0)], []),
    ('D', 179, 'STM'): CALL,
    ('D', 194, 'A2P'): ('site', 'D', [E(1, -k_)], [E(2, -1, 0)], []),
    ('D', 195, 'STM'): S,
    ('D', 198, 'BP'): ('site', 'D', [E(1, -k_)], [E(2, -1, 0)], [E(1, -k_), E(0, 1)]),
    ('D', 200, 'BP'): ('site', 'D', [E(1, -k_)], [E(2, -1, 0), E(2, -2)], []),
    ('D', 203, 'BP'): ('site', 'D', [E(1, -k_), NN], [E(2, -1, 0)], []),
    ('D', 213, 'STM'): S, ('D', 214, 'A2P'): ('site', 'C0', [E(0, -k_, 0)], [E(0, -1, 0)], []),
    ('D', 223, 'STM'): CALL, ('D', 235, 'STM'): S,
    ('D', 239, 'A2P'): ('site', 'D', [E(1, -k_, 0)], [E(1, -1, 0)], []),
    ('D', 247, 'STM'): S, ('D', 252, 'STM'): S, ('D', 278, 'STM'): S, ('D', 294, 'A2P'): S,
    ('D', 688, 'A2P'): ('site', 'D', [E(1, -1, 0)], [E(1, -1, 0), E(0, -2, 0)], []),
    ('D', 691, 'STM'): CALL,
    ('D', 720, 'A2P'): ('site', 'D', [E(1, -1, 0)], [E(0, 0, 2)], [E(0, 0, 2)]),
    ('D', 747, 'STM'): CALL, ('D', 766, 'STM'): S, ('D', 771, 'STM'): S,
    ('D', 775, 'A2P'): ('site', 'D', [E(1, -1, 0)], [E(0, -1, 0)], []),
    ('D', 808, 'A2P'): ('site', 'D', [E(1, -k_)], [E(2, -1, 0)], []),
    ('D', 824, 'A2P'): ('site', 'D', [E(1, -k_, 0)], [E(1, -1, 0), E(2, -1, 0)], []),
    ('D', 910, 'STM'): CALL, ('D', 926, 'STM'): S, ('D', 942, 'STM'): CALL, ('D', 947, 'STM'): CALL,
    ('D', 1037, 'STM'): S, ('D', 1100, 'BP'): S,
    # II.D' (b-regularity; the tame versions II.A Propositions 9.1, 9.2, 9.8, 9.9 replace (L3)-(L4) there)
    ('D2', 216, 'A85'): ('site', 'D', [E(1, -2, 0)], [E(0, 2)], []),
    ('D2', 219, 'A85'): ('site', 'D', [E(1, -1, 0)], [E(0, 0, 2)], []),
    ('D2', 226, 'A85'): ('site', 'D', [E(1, -1, 0)], [E(0, 2)], []),
    ('D2', 523, 'STM'): S, ('D2', 524, 'STM'): S, ('D2', 679, 'STM'): S,
    # II.E, II.F'
    ('E', 545, 'STM'): S, ('E', 605, 'STM'): CALL, ('E', 608, 'STM'): CALL,
    ('E', 748, 'A85'): ('site', 'D', [E(1, -2, 0)], [E(0, 0, 2)], []),
    ('E', 1005, 'STM'): CALL, ('E', 1008, 'STM'): CALL,
    ('F2', 487, 'A85'): ('site', 'D', [E(1, -2, 0)], [E(0, 0, 2)], []),
}
# other parts' own Lemma 1.2 / Proposition 2.4, and [Hin26c] Lemma 8.5 (II.E's extension)
for key, lines in (('C', (55, 58, 176, 645, 817)),
                   ('E', (48, 118, 164, 429, 437, 488, 573, 581, 606, 744, 886, 1104, 1189, 1238)),
                   ('F', (82, 108, 117, 275, 761, 1453, 1907, 2133, 2189, 2299, 2667, 2762)),
                   ('F2', (39, 147, 157, 163, 293, 295, 360, 475))):
    for i in lines:
        TABLE[(key, i, 'BL')] = OTHER
for i in (592, 647, 810, 846, 863, 997, 1245, 1313):
    TABLE[('F', i, 'BP')] = OTHER
KPRIME = [('A2', 420, "for $w\\in H^{K'}_{e3b}$"), ('A2', 439, "where $K'\\ge\\sup|\\mathsf s|+m+2$ is a fixed integer"),
          ('A2', 466, "\\subset H^{K'}$ for $t>0$"), ('A2', 695, "for $w\\in H^{K'}$"),
          ('D', 160, "for every $w\\in H^{K'}_{e3b}$"), ('D', 230, "for $w\\in H^{K'}_{e3b}$")]
READS = [('A2', 727, "Take $\\tau\\ge\\sup\\mathsf s+N$"), ('A2', 403, "once $J'/2\\ge\\sup\\mathsf s+N$"),
         ('A2', 394, "Finally $\\|\\chi Lu\\|_{-N-m}\\le C\\|\\chi u\\|_{-N}$"),
         ('A2', 522, "and $\\mathsf s_j := \\mathsf"), ('D', 1035, "\\|_{-N}\\le\\|u\\|_{\\mathsf s_0}$"),
         ('D', 287, "$\\tau := s-s_0$"), ('D', 691, "for $\\tau = 1$")]


def lines_of(key, root=P5):
    return open(os.path.join(root, FILES[key][0]), encoding='utf-8').read().split('\n')


def md5_ok(root=P5):
    return all(hashlib.md5(open(os.path.join(root, f), 'rb').read()).hexdigest() == m for f, m in FILES.values())


def hits(root=P5):
    """every family match, across line breaks; the line is that of the match's first character"""
    out = []
    for key in FILES:
        L = lines_of(key, root)
        a, b = RANGES.get(key, (1, len(L)))
        starts, pos = [], 0
        for i in range(a, b + 1):
            starts.append(pos)
            pos += len(L[i - 1]) + 1
        T = ' '.join(L[a - 1:b])
        seen = []
        for tag, p in FAM:
            if tag == 'BT' and key != 'A2':
                continue
            for m in re.finditer(p, T):
                if any(s <= m.start() < e for s, e in seen):
                    continue
                seen.append((m.start(), m.end()))
                st = m.start() + (1 if T[m.start()] == ' ' else 0)
                out.append((key, a + bisect.bisect_right(starts, st) - 1, tag, m.group(0).strip()))
    return out


def census(table=TABLE, root=P5):
    rows, uncl, used = [], [], set()
    for k, i, tag, t in hits(root):
        key = (k, i, tag)
        if key not in table:
            uncl.append((k, i, tag, t))
            continue
        used.add(key)
        rows.append((key, t, table[key]))
    stale = [key for key in table if key not in used]
    return rows, uncl, stale


def evaluate(rows, N=NERR, tau_full=True):
    dom = domains(N, tau_full)
    sob, sym, fac, where = [], [], [], {}
    for key, _, cls in rows:
        if not (isinstance(cls, tuple) and cls[0] == 'site'):
            continue
        _, ctx, so, sy, fa = cls
        lo, hi = dom[ctx]
        for lst, out, nm in ((so, sob, 'sob'), (sy, sym, 'sym'), (fa, fac, 'fac')):
            for e in lst:
                if e == NN:
                    vals = [-N, -N - M_OP]
                else:
                    a, b0, b1 = e
                    vals = [a * lo + b0, a * hi + b0, a * lo + b1, a * hi + b1]
                out.extend(vals)
                for v in vals:
                    where.setdefault((nm, v), key)
    return dict(sob=(min(sob), max(sob)), sym=(min(sym), max(sym)), fac=(min(fac), max(fac)), where=where)


def box(N=NERR):
    """the census's box (O3), for d0count5: Sobolev range, symbol range, factor range of (f)"""
    rows, _, _ = census()
    r = evaluate(rows, N)
    return r['sob'], r['sym'], r['fac']


def main():
    print('ordcensus5: the orders at which the forward-solution chain invokes the closed-graph calculus, site by site')
    md5 = md5_ok()
    reads = all(t in lines_of(k)[i - 1] for k, i, t in READS)
    OK['O0'] = md5 and reads
    print('  O0 (READ): %d files at their pinned md5: %s; the scope II.A2:358-785, II.D, II.D\', II.E, II.F\', II.C, '
          'II.F; %d order statements found by content (II.A2:726 tau >= sup s + N; II.A2:400 J\'/2 >= sup s + N; '
          'II.A2:394 -N - m; II.A2:520 s_j; II.D:1035 |chi u|_(-N) <= |u|_(s_0); II.D:287 tau := s - s_0; II.D:691 '
          'tau = 1): %s' % (len(FILES), md5, len(READS), reads))
    rows, uncl, stale = census()
    by = {}
    for _, _, cls in rows:
        c = cls if isinstance(cls, str) else cls[0]
        by[c] = by.get(c, 0) + 1
    OK['O1'] = not uncl and not stale and len(rows) == 153
    print('  O1 (census): %d hits, %d unclassified, %d stale rows; by class %s' % (len(rows), len(uncl), len(stale),
                                                                                  dict(sorted(by.items()))))
    for u in uncl:
        print('      unclassified %s' % (u,))
    dom = domains()
    OK['O2'] = dom['L41'] == (Fr(-31), Fr(10)) and dom['T31'] == (Fr(-61, 2), Fr(10)) and dom['D'] == (Fr(-10),
                                                                                                      Fr(10))
    print('  O2 (deduced): the order ranges, from the callers: Lemma 4.1 / Proposition 5.3 / the parametrix at s\' in '
          '[%s, %s] (tau >= sup s + N); Theorem 3.1\'s r\' in [%s, %s] (J\'/2 >= sup s + N); II.D-II.F\' sites in '
          '[%s, %s] (s, s_0, s + 1): %s' % (dom['L41'][0], dom['L41'][1], dom['T31'][0], dom['T31'][1], dom['D'][0],
                                       dom['D'][1], OK['O2']))
    r = evaluate(rows)
    old = dict(sob=(Fr(-16), Fr(11)), sym=(Fr(-22), Fr(22)), fac=(Fr(-1049, 100), Fr(951, 100)))
    inside = {nm: old[nm][0] <= r[nm][0] and r[nm][1] <= old[nm][1] for nm in ('sob', 'sym', 'fac')}
    OK['O3'] = r['sob'] == (Fr(-65, 2), Fr(14)) and r['sym'] == (Fr(-63), Fr(31)) and r['fac'] == (Fr(-63, 2),
                                                                                                  Fr(951, 100))
    wl = r['where'][('sob', r['sob'][0])]
    ws = r['where'][('sym', r['sym'][0])]
    wh = r['where'][('sym', r['sym'][1])]
    print('  O3 (computed): over the sites, the Sobolev orders lie in [%s, %s], the symbol orders in [%s, %s], the '
          'factor orders of (f) in [%s, %s]; inside round 8\'s box ([-16, 11] x [-22, 22], factors [-10.49, 9.51]): '
          'Sobolev %s, symbol %s, factors %s. The extremes: Sobolev %s at %s:%d (Theorem 3.1\'s iteration at r\' = '
          '-61/2, its input r\' - m), symbol %s at %s:%d (Proposition 5.3 at s\' = -31, 2k), %s at %s:%d (Lemma 4.2\'s '
          'parametrix q of order r - s_j at s_j = -31). Pinned: %s' % (
              r['sob'][0], r['sob'][1], r['sym'][0], r['sym'][1], r['fac'][0], r['fac'][1], inside['sob'],
              inside['sym'], inside['fac'], r['sob'][0], wl[0], wl[1], r['sym'][0], ws[0], ws[1], r['sym'][1], wh[0],
              wh[1], OK['O3']))
    kp = [t in lines_of(k)[i - 1] for k, i, t in KPRIME]
    allk = [(k, i) for k in FILES for i, x in enumerate(lines_of(k), 1) if "K'" in x and ('H^{K' in x or "K'\\ge" in x
                                                                                         or "$K'$" in x)]
    OK['O4'] = all(kp) and set(allk) <= {(k, i) for k, i, _ in KPRIME}
    print('  O4 (READ): every K\' of the chain (%d lines) is the membership w in H^(K\') or its definition K\' >= sup|s| '
          '+ m + 2 (II.A2:439), none an order of an O3 site: %s' % (len(allk), OK['O4']))
    OK['O5'] = OK['O0'] and -NERR <= S_LO and r['sob'][0] <= -NERR - M_OP
    print('  O5 (READ; deduced): the a priori term |chi u|_(-N) <= |u|_(s_0) asks N >= -inf s_0 = 10 (II.D:1035); N = '
          '%s <= 14 serves, and -N, -N - m = %s, %s lie in O3\'s Sobolev range: %s' % (NERR, -NERR, -NERR - M_OP,
                                                                                     OK['O5']))
    # controls
    t1 = dict(TABLE)
    t1.pop(('A2', 690, 'BP'))
    _, u1, _ = census(table=t1)
    OK['C1'] = len(u1) == 1
    print('  C1 (control): the row II.A2:690 dropped: %d unclassified: %s' % (len(u1), OK['C1']))
    r2 = evaluate(rows, tau_full=False)
    OK['C2'] = r2['sob'][0] >= -16 and r2['sym'][0] >= -26 and r2 != r
    print('  C2 (control): tau and J\'/2 without N and the oscillation (tau = 1): Sobolev [%s, %s], symbol [%s, %s]: '
          'the finding of O3 depends on them: %s' % (r2['sob'][0], r2['sob'][1], r2['sym'][0], r2['sym'][1], OK['C2']))
    tmp = tempfile.mkdtemp()
    try:
        for f, _ in FILES.values():
            shutil.copy(os.path.join(P5, f), tmp)
        p = os.path.join(tmp, FILES['A2'][0])
        s = open(p, encoding='utf-8').read().replace('Take $\\tau\\ge\\sup\\mathsf s+N$', 'Take $\\tau = 1$')
        open(p, 'w', encoding='utf-8').write(s)
        OK['C3'] = not md5_ok(tmp)
    finally:
        shutil.rmtree(tmp)
    print('  C3 (control): II.A2:726 altered in a copy: O0 fails: %s' % OK['C3'])
    r4 = evaluate(rows, N=Fr(10))
    OK['C4'] = r4['sob'] != r['sob'] and r4['sym'] != r['sym']
    print('  C4 (control): N = 10: Sobolev [%s, %s], symbol [%s, %s], not O3\'s: %s' % (
        r4['sob'][0], r4['sob'][1], r4['sym'][0], r4['sym'][1], OK['C4']))
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
