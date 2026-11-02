#!/usr/bin/env python3
"""lzeroaudit5: is every step of Theorem 1's lambda0 constructive? (CONSTANTS5.md, L1).

lambda0 is the threshold of N1STAR-PROOF.md sections 0-6 (Theorem E, section 4 Steps 3 and 7; Theorem D, Proposition
6.5; the standing lam1 of section 2), the paper's sections 3-5 restating it. The same three theorems at order k = J + 4
are PART-VII-ASSEMBLY.md Lemma 1.1, so the audit also decides EFFECTIVE-CONSTANTS.md E5's first item (C_J, lambda_1.1).

  A1 (computed) a census of N1STAR-PROOF.md lines 1-812 (sections 0-6; 1-805 before D612 and D614) for the words of
     the four non-effective kinds of
     EFFECTIVE-CONSTANTS.md section 3 (contradiction, compactness, Rellich, Fredholm, subsequence, closed graph, Baire,
     weak limits, open conditions, "small enough") and for every threshold phrase (lam0, lam1, eps1, eps2, "lam small",
     "depending only on", Gronwall, Picard, "there is/are"); every hit is classified by the table below, read in context:
       X  no argument producing a constant (a mention, a support statement, an explicit step);
       G  qualitative compactness with no constant (a weak-* limit whose bound is the uniform estimate);
       E  a threshold or constant with an explicit replacement, computed in lzeroconst5.py;
       T  a threshold, one term of lambda0's formula (lzeroconst5.py Z4);
       N  a step of kind N1-N4 (none found).
  A2 (computed) every T row maps to a term of the formula, and every term has a source row.
  A3 (deduced, READ) every citation in lines 1-812 is listed with whether it enters lambda0 and whether its constant is
     effective.
  Controls (must fail, and do): C1 a planted "by contradiction ... subsequence ... compactness" sentence is not
  classified; C2 the census finds the ledger's N1 site PART-I-C-LOWENERGY.md:495-498 (positive control); C3 a table row
  removed leaves a hit unclassified.

    python3 checks/lzeroaudit5.py
"""
import hashlib
import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
PROOF = os.path.join(HERE, '..', 'N1STAR-PROOF.md')
LOWE = os.path.join(HERE, '..', 'proof5', 'PART-I-C-LOWENERGY.md')
LAST = 812                       # sections 0-6; 805 before D612/D614 added 7 lines at 87-93

NONCON = re.compile(r'contradict|compact|rellich|fredholm|subsequen|closed graph|baire|weak|open condition|'
                    r'finitely many|so small|small enough|sufficiently small|limit', re.I)
THRESH = re.compile(r'open and closed|depending only on|there is |there are |gronwall|picard|uniformly|'
                    r'uniform constant|lam0|lam1|eps1|eps2|delta depending|lam small', re.I)

X, G, E, T, N = 'X', 'G', 'E', 'T', 'N'
# (line, keyword) -> (class, the formula term or the reason)
TABLE = {
    (20, 'weak'): (X, 'editorial ("stated more weakly")'),
    (41, 'compact'): (X, 'compactly supported mollifier: a support statement'),
    (106, 'there are '): (T, 'statement of lam0 (Theorem E)'), (106, 'lam0'): (T, 'statement of lam0 (Theorem E)'),
    (107, 'lam0'): (T, 'statement of lam0 (Theorem E)'),
    (117, 'there are '): (X, 'Theorem A: profiles by linear transports and wave equations, no threshold'),
    (124, 'there is '): (T, 'lam_D (Theorem D)'), (124, 'lam small'): (T, 'lam_D (Theorem D)'),
    (133, 'gronwall'): (X, 'D = 0 by uniqueness: no threshold'),
    (140, 'weak'): (X, 'weak convergence in the conclusion: no constant'),
    (160, 'eps1'): (E, 'eps1: explicit margins (lzeroconst5 Z2)'),
    (170, 'open condition'): (E, 'eps1: open conditions with explicit margins on compact Omega (Z2)'),
    (170, 'compact'): (E, 'eps1: as above'),
    (177, 'lam1'): (T, 'lam1 = min(1, delta0)/10'),
    (182, 'uniformly'): (E, 'Sobolev constant C_S, uniform over the annuli (Z3)'),
    (183, 'uniform constant'): (E, 'Sobolev constant C_S (Z3)'),
    (215, 'eps1'): (E, 'eps1 (Z2)'),
    (226, 'uniformly'): (X, 'energy flux comparable to |du|^2: explicit through eps1 margins'),
    (228, 'gronwall'): (X, 'Lemma 2.3: explicit exponential'), (235, 'gronwall'): (X, 'Lemma 2.4: explicit exponential'),
    (319, 'there is '): (X, '"There is no 1/lam coefficient"'),
    (356, 'lam0'): (T, 'E-a, E-b and E-c (Step 3)'),
    (399, 'gronwall'): (X, 'Step 7: C3 = C2 exp(C2 dtau)(1 + dtau) C, explicit'),
    (400, 'lam0'): (T, 'E-d (Step 7)'), (401, 'lam0'): (T, 'E-d (Step 7)'),
    (402, 'open and closed'): (X, 'continuity of N in tau: connectedness, no constant'),
    (418, 'compact'): (X, 'support statement'), (420, 'compact'): (X, 'support statement'),
    (422, 'uniformly'): (X, 'positive definite spatial metric: explicit'),
    (425, 'so small'): (E, 'eps2: margin of (1.3) for g_ext, explicit'), (425, 'eps2'): (E, 'eps2 (E-b)'),
    (427, 'eps2'): (T, 'E-b (|w| <= eps2/2 on Omega)'),
    (431, 'compact'): (X, 'support statement'),
    (440, 'finitely many'): (X, 'chain and product rules: explicit'),
    (441, 'delta depending'): (X, 'local existence time: continuation only, not in lam0'),
    (444, 'eps2'): (X, 'uniqueness while |w| <= eps2/2: no new threshold'),
    (446, 'gronwall'): (X, 'uniqueness by Lemma 2.3: no threshold'),
    (530, 'picard'): (X, 'Lemma 5.3: Picard iteration for a linear system, constructive'),
    (538, 'uniformly'): (X, 'residual lam^N times a bounded profile'),
    (587, 'small enough'): (X, "Touati's method, quoted and not used"),
    (624, 'there are '): (X, 'Lemma 6.2: stage data by pointwise algebra and Lemma 6.4, constructive'),
    (690, 'uniformly'): (X, 'angular derivatives bounded uniformly in lam'),
    (692, 'lam small'): (T, 'D-c (coefficients keep their signs)'),
    (693, 'uniformly'): (X, 'first derivatives bounded uniformly in lam'),
    (705, 'there is '): (X, 'Lemma 6.4: existence; its constant explicit in M_s'),
    (709, 'depending only on'): (X, 'Lemma 6.4: C explicit in s, R - a, alpha0, delta0, A00, M_s'),
    (715, 'depending only on'): (X, 'tame form: explicit'),
    (718, 'gronwall'): (X, 'explicit'), (729, 'gronwall'): (X, 'explicit'),
    (736, 'finitely many'): (X, 'Galerkin dimension'),
    (738, 'picard'): (X, 'Picard for an ODE system: constructive'),
    (744, 'uniformly'): (G, 'the Galerkin bound, uniform in L'),
    (744, 'weak'): (G, 'weak-* limit: existence, the bound is the uniform one'),
    (745, 'limit'): (G, 'weak-* limit: as above'),
    (750, 'lam0'): (T, 'lam_D (Proposition 6.5)'), (750, 'there is '): (T, 'lam_D (Proposition 6.5)'),
    (771, 'lam small'): (T, 'D-a, D-b and D-d (Proposition 6.5)'),
    (782, 'depending only on'): (X, 'tame recursion: explicit'),
    (785, 'gronwall'): (X, 'explicit'),
    (787, 'limit'): (X, 'limit of a contraction: constructive'),
    (790, 'lam0'): (T, 'lam_D (Proposition 6.5)'),
}
TERMS = {'statement of lam0 (Theorem E)': None, 'lam1 = min(1, delta0)/10': 'lam1',
         'E-a, E-b and E-c (Step 3)': 'E-a,E-b,E-c',
         'E-d (Step 7)': 'E-d', 'E-b (|w| <= eps2/2 on Omega)': 'E-b', 'lam_D (Theorem D)': None,
         'D-c (coefficients keep their signs)': 'D-c', 'lam_D (Proposition 6.5)': None,
         'D-a, D-b and D-d (Proposition 6.5)': 'D-a,D-b,D-d'}
FORMULA = {'lam1', 'E-a', 'E-b', 'E-c', 'E-d', 'D-a', 'D-b', 'D-c', 'D-d'}   # D-d added in round 2 (V-m4): the
# ball invariance of Proposition 6.5 (N1STAR-PROOF.md:771-772)
PIN = '6e8947ad2005ac587f9b632d0a1e8025'        # md5 of lines 1-812 at D614 (round 1's 57d896ae... of lines 1-805)
FILE_PIN = '02e7617602841a350a75349c44ab5fb6'   # the whole file at D614 (10853 lines)
TABLE = {((ln + 7 if ln > 86 else ln), kw): val for (ln, kw), val in TABLE.items()}   # D612 + D614: +7 above 86
TABLE.update({(89, 'eps1'): (E, 'eps1: the pointwise norm (D612), Lemma 1.1 (e) at 3/5 (lzerotrace5 T6)'),
              (90, 'eps1'): (E, 'eps1: Lemma 2.3 below g0\'s least absolute eigenvalue (D614; lzerotrace5 T7)')})
CITES = {
    'BH17': ('Sobolev H^3 -> L^inf in 4D', 'enters (C_S)', 'effective: certified constant, lzeroconst5 Z3'),
    'DS23': ('local existence Thms 2.4, 2.6; Remark 2.3 commutators', 'Thm 2.4/2.6 no; Remark 2.3 via Lemma 6.4',
             'existence time unused by lam0; integer-order commutators effective'),
    'AO14': ('local theory (1.3); Kato-Majda scheme section 4.1', 'scheme yes (Prop 6.5)',
             'contraction with explicit factor'),
    'LY22': ('Seeley extension Thm 26, Lemma 27', 'no (restarts only)', '-'),
    'SY21': ('Stein/Rychkov extension of the profiles', 'through eps2', 'explicit operator'),
    'GO13': ('Moser and Kato-Ponce on S^3', 'through Lemma 6.4', 'effective at integer orders'),
    'CBCM10': ('form of Ric^H', 'no', 'identity'), 'LR05': ('contracted Bianchi', 'no', 'identity'),
    'CBCL06': ('contracted Bianchi, n+1', 'no', 'identity'), 'CD03': ('constraint map form', 'no', 'identity'),
    'Rac16': ('constraints as evolution in r', 'no', 'structure'), 'Tou23a': ('comparison', 'no', '-'),
    'Hua15': ('withdrawn citation (D18)', 'no', '-'), 'MM10': ('withdrawn citation (D18)', 'no', '-'),
}


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def census(lines, table, offset=0):
    hits, uncl = [], []
    for i, l in enumerate(lines, 1 + offset):
        for pat in (NONCON, THRESH):
            for kw in sorted(set(m.group(0).lower() for m in pat.finditer(l))):
                key = (i, kw)
                hits.append(key)
                if key not in table:
                    uncl.append((key, l.strip()[:90]))
    return hits, uncl


def main():
    ok = {}
    lines = open(PROOF, encoding='utf-8').read().split('\n')[:LAST]
    md5 = hashlib.md5('\n'.join(lines).encode()).hexdigest()
    full = open(PROOF, encoding='utf-8').read().split('\n')
    fmd5 = hashlib.md5('\n'.join(full).encode()).hexdigest()
    ok['A0'] = md5 == PIN and fmd5 == FILE_PIN
    say('  A0: md5 of N1STAR-PROOF.md lines 1-%d = %s, the pinned %s; whole file %s, the pinned %s: %s' % (
        LAST, md5, PIN, fmd5, FILE_PIN, ok['A0']))
    hits, uncl = census(lines, TABLE)
    cls = {}
    for h in hits:
        if h in TABLE:
            cls.setdefault(TABLE[h][0], []).append(h)
    say('  A1: N1STAR-PROOF.md lines 1-%d (md5 %s): %d hits, %d unclassified; classes %s; class N (kinds N1-N4): %d'
        % (LAST, md5, len(hits), len(uncl), {k: len(v) for k, v in sorted(cls.items())}, len(cls.get(N, []))))
    for k, l in uncl:
        say('      unclassified %s: %s' % (k, l))
    stale = [k for k in TABLE if k not in set(hits)]
    ok['A1'] = not uncl and not cls.get(N) and not stale
    if stale:
        say('      stale table rows: %s' % stale)
    terms = set()
    for h in cls.get(T, []):
        t = TERMS[TABLE[h][1]]
        if t:
            terms |= set(t.split(','))
    ok['A2'] = terms == FORMULA
    say('  A2: the T rows reach the formula terms %s; every term has a source row: %s' % (sorted(terms),
                                                                                       terms == FORMULA))
    cites = set(m.group(1) for l in lines for m in re.finditer(r'\[([A-Z][A-Za-z]+\d\d[a-z]?)\]', l))
    ok['A3'] = cites == set(CITES)
    say('  A3: citations in lines 1-%d: %s; all listed: %s' % (LAST, sorted(cites), cites == set(CITES)))
    for c in sorted(CITES):
        say('      %-7s %s | enters lam0: %s | %s' % (c, *CITES[c]))
    planted = lines + ['By contradiction, a subsequence converges by compactness, so the constant exists.']
    _, u1 = census(planted, TABLE)
    ok['C1'] = len(u1) >= 3
    say('  C1 (control): a planted sentence leaves %d hits unclassified: %s' % (len(u1), [k for k, _ in u1]))
    low = open(LOWE, encoding='utf-8').read().split('\n')[494:498]
    hl, _ = census(low, {}, offset=494)
    kws = sorted(set(k for _, k in hl))
    ok['C2'] = 'subsequen' in kws and 'contradict' in kws
    say('  C2 (control): the census on PART-I-C-LOWENERGY.md:495-498 (EFFECTIVE-LEDGER N1 at 497) finds %s' % kws)
    t2 = dict(TABLE)
    del t2[(752, 'limit')]
    _, u3 = census(lines, t2)
    ok['C3'] = len(u3) == 1 and not uncl
    say('  C3 (control): with the row (752, limit) removed (745 before D612/D614), %d hit unclassified' % len(u3))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
