#!/usr/bin/env python3
"""nrows5: lambda1 and delta (Theorem 4) -- every non-effective step, its quantitative replacement, and why none is
computed here (CONSTANTS5.md, D3-D4).

  R1 (computed) the 35 rows of class N1-N4 of EFFECTIVE-LEDGER.tsv (6, 15, 1, 13, as EFFECTIVE-CONSTANTS.md section 3
     counts), each given the obstructions below; every row covered, none twice.
  R2 (computed) a kind the ledger's keywords did not search: bounds from the closed graph, open mapping and
     Banach-Steinhaus theorems (Baire category), which give a constant without a value. A census of proof5's PART files
     finds 18 lines (16 in round 1, whose pattern missed "closed-graph" and "Banach and Steinhaus"); each is classified
     (B: a constant or order enters; A: with a constructive alternative beside it; R: a remark, summary, list or
     pointer; Q: a quoted source).
  R3 (deduced; the table is a hand-written reading) the order the replacements must be built in: no N1 base bound
     can be certified in the record's norms before the calculus and covering constants (COVER, BAIRE) and the norm
     passage (NORM) are explicit. Round 3 (the verifier's m2): the test now checks the claim itself, that every N1 row
     needs one of NORM, TENSOR, LOWE, TRAP, each after COVER, not only "after COVER".
  Controls (must fail, and do): C1 a ledger row removed from the table is reported missing; C2 a planted site is
  unclassified, and the pattern itself is tested on planted phrasings (round 1's C2 injected a hit and never tested
  the pattern; round 1's pattern misses three of the five phrasings); C3 (Round 3) R3's test with one N1 row
  re-tagged SIGMA only fails.

Codes. NORM: from per-harmonic L^2 bounds (E2-PILOT's kind) to the record's variable-order b-Sobolev norms, which needs
the elliptic and propagation constants of I.A-I.B, themselves COVER rows. TENSOR: a system on 1-forms or symmetric
2-tensors; certification mode by mode needs its tensor-harmonic decomposition on S^3 (E2-PILOT has the scalar wave
only). BFAM: uniformity over b near b0 (rotating Myers-Perry, no separation at b != b0): a Neumann series about a
certified base, with an explicit Lipschitz bound in b in the record's norm. SIGMA: uniformity in a spectral parameter:
a Neumann series in it, once the base is certified (E2-PILOT does this in its own norm, 3 <= sigma <= 384). COVER: a
finite cover; needs explicit radii from explicit local constants. TRAP: the trapping estimate (E2-PILOT 3e-3j: scalar,
cut-off norm only). LOWE: an inverse bound at zero energy in b-spaces. BAIRE: read the bound off the proof of the
membership statement instead of the theorem.

    python3 checks/nrows5.py
"""
import csv
import glob
import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, '..', 'EFFECTIVE-LEDGER.tsv')
PROOF5 = os.path.join(HERE, '..', 'proof5')

ROWS = {
    ('PART-III-G-SPECTRAL.md', 342): 'COVER', ('PART-I-SPECTRAL.md', 1570): 'COVER',
    ('PART-I-SPECTRAL.md', 1602): 'COVER', ('PART-I-SPECTRAL.md', 1693): 'SIGMA NORM',
    ('PART-I-SPECTRAL.md', 1801): 'SIGMA NORM', ('PART-I-SPECTRAL.md', 1884): 'COVER BFAM',
    ('PART-I-B-HIGHENERGY.md', 1513): 'TRAP TENSOR NORM', ('PART-I-B-HIGHENERGY.md', 1685): 'TRAP NORM',
    ('PART-I-B-HIGHENERGY.md', 1836): 'COVER', ('PART-I-B-HIGHENERGY.md', 1913): 'COVER',
    ('PART-I-B-HIGHENERGY.md', 1978): 'TRAP NORM TENSOR', ('PART-I-B-HIGHENERGY.md', 2046): 'COVER BFAM',
    ('PART-I-B-HIGHENERGY.md', 2047): 'BFAM TRAP', ('PART-I-C-LOWENERGY.md', 497): 'LOWE NORM TENSOR',
    ('PART-I-C-LOWENERGY.md', 686): 'SIGMA LOWE', ('PART-I-C-LOWENERGY.md', 748): 'SIGMA LOWE',
    ('PART-I-C-LOWENERGY.md', 1414): 'BFAM LOWE', ('PART-I-C-LOWENERGY.md', 1421): 'BFAM SIGMA LOWE',
    ('PART-II-A2-STANDARD.md', 772): 'COVER', ('PART-II-D-REGULARITY.md', 1032): 'COVER',
    ('PART-II-E-ENERGY.md', 615): 'COVER', ('PART-II-F-IOTA.md', 1063): 'SIGMA TENSOR',
    ('PART-II-F-IOTA.md', 1329): 'SIGMA TENSOR', ('PART-II-F-IOTA.md', 1393): 'NORM TENSOR',
    ('PART-II-G-NASHMOSER.md', 299): 'COVER', ('PART-II-G2-DECAY.md', 716): 'COVER SIGMA',
    ('PART-III-F4-ZERO.md', 439): 'BFAM LOWE TENSOR', ('PART-III-F3-MODES.md', 223): 'TENSOR NORM',
    ('PART-III-H-AUGMENT.md', 326): 'BFAM TENSOR', ('PART-III-H2-ADMISS.md', 211): 'SIGMA TENSOR',
    ('PART-III-H3-UNIFORM.md', 189): 'BFAM SIGMA TENSOR', ('PART-III-H3-UNIFORM.md', 215): 'COVER BFAM',
    ('PART-III-D-GAUGEPOT.md', 365): 'TENSOR NORM LOWE', ('PART-III-D2-ZEROENERGY.md', 256): 'SIGMA LOWE TENSOR',
    ('PART-IV7-TFACE.md', 383): 'SIGMA TENSOR',
}
# Round 2 (verifier, V-m2): round 1's pattern (BAIRE_PAT_R1 below)
# missed "closed-graph" (J4-EXACT:655) and "Banach and Steinhaus" (II.A2:186); any dash or space is allowed now.
_D = r'[\s\-\u2010\u2011\u2012\u2013\u2014]*'
BAIRE_PAT = re.compile(r'closed' + _D + 'graph|open' + _D + 'mapping|uniform' + _D + 'boundedness|steinhaus|baire', re.I)
BAIRE_PAT_R1 = re.compile(r'closed graph|open mapping|uniform boundedness|banach[- ]steinhaus|baire', re.I)
BAIRE = {  # B: a constant (or an order) enters through the theorem; A: the theorem with a constructive alternative
    # stated beside it; R: a remark, a summary, a list of theorems or a pointer to a B row; Q: a quoted source.
    # Round 2 (V-m2): II.A:986, 1538 and II.A2:811 are summaries (B -> R); I4:274 offers III.I' Proposition 2.1's
    # constructive bound beside the closed graph theorem (B -> A); II.A2:186 and J4:655 are the new hits.
    ('PART-II-A-SETUP.md', 960): 'B', ('PART-II-A-SETUP.md', 986): 'R', ('PART-II-A-SETUP.md', 1538): 'R',
    ('PART-II-A2-STANDARD.md', 130): 'B', ('PART-II-A2-STANDARD.md', 186): 'B', ('PART-II-A2-STANDARD.md', 188): 'B',
    ('PART-II-A2-STANDARD.md', 276): 'B', ('PART-II-A2-STANDARD.md', 281): 'B', ('PART-II-A2-STANDARD.md', 811): 'R',
    ('PART-II-A2-STANDARD.md', 832): 'R', ('PART-II-C2-TRAPPING.md', 406): 'Q', ('PART-II-F-IOTA.md', 1400): 'B',
    ('PART-III-H-AUGMENT.md', 425): 'B', ('PART-III-I3-ALMOST.md', 436): 'R', ('PART-III-I4-BOOST.md', 274): 'A',
    ('PART-III-J3-TAME.md', 41): 'B', ('PART-III-J3-TAME.md', 82): 'B', ('PART-III-J4-EXACT.md', 655): 'R',
}
ORDER = ['COVER', 'NORM', 'TENSOR', 'LOWE', 'TRAP', 'SIGMA', 'BFAM']


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def ledger_rows():
    rows = list(csv.reader(open(LEDGER, encoding='utf-8'), delimiter='\t'))[1:]
    return {(r[0], int(r[1])): r[2] for r in rows if r[2] in ('N1', 'N2', 'N3', 'N4')}


def baire_census(extra=()):
    hits = []
    for f in sorted(glob.glob(os.path.join(PROOF5, 'PART-*.md'))):
        for i, l in enumerate(open(f, encoding='utf-8'), 1):
            if BAIRE_PAT.search(l):
                hits.append((os.path.basename(f), i))
    return hits + list(extra)


def main():
    ok = {}
    led = ledger_rows()
    counts = {}
    for v in led.values():
        counts[v] = counts.get(v, 0) + 1
    missing = sorted(set(led) - set(ROWS))
    extra = sorted(set(ROWS) - set(led))
    ok['R1'] = not missing and not extra and counts == {'N1': 6, 'N2': 15, 'N3': 1, 'N4': 13}
    say('  R1: ledger N-rows %d %s; covered %d; missing %s; not in the ledger %s' % (
        len(led), dict(sorted(counts.items())), len(set(led) & set(ROWS)), missing, extra))
    by = {}
    for k, codes in ROWS.items():
        for c in codes.split():
            by.setdefault(c, []).append(k)
    say('      rows per obstruction: %s' % {c: len(by.get(c, [])) for c in ORDER})
    for cls in ('N1', 'N2', 'N3', 'N4'):
        ks = sorted(k for k in led if led[k] == cls)
        say('      %s: %s' % (cls, '; '.join('%s:%d %s' % (f.replace('PART-', '').replace('.md', ''), l, ROWS[(f, l)])
                                            for f, l in ks)))
    hits = baire_census()
    uncl = [h for h in hits if h not in BAIRE]
    kinds = {}
    for h in hits:
        kinds[BAIRE.get(h, '?')] = kinds.get(BAIRE.get(h, '?'), 0) + 1
    in_ledger = [h for h in hits if h in led]
    ok['R2'] = len(hits) == 18 and not uncl and not in_ledger and kinds == {'B': 10, 'R': 6, 'Q': 1, 'A': 1}
    say('  R2: Baire-category sites in proof5: %d (%s), none among the ledger\'s N-rows: %s; the B rows: %s' % (
        len(hits), kinds, not in_ledger, '; '.join('%s:%d' % (f.replace('PART-', '').replace('.md', ''), l)
                                                   for (f, l) in hits if BAIRE.get((f, l)) == 'B')))
    dep = {c: i for i, c in enumerate(ORDER)}
    n1_first = sorted(k for k in led if led[k] == 'N1')
    need = {'NORM', 'TENSOR', 'LOWE', 'TRAP'}

    def r3_test(rows):
        # Round 3 (the verifier's m2): the claim itself -- every N1 row needs one of NORM, TENSOR, LOWE, TRAP, each
        # after COVER in the order -- not only the weaker "after COVER"
        return all(set(rows[k].split()) & need and min(dep[c] for c in rows[k].split()) > dep['COVER']
                   for k in n1_first)

    blocked = r3_test(ROWS)
    ok['R3'] = blocked and len(by['COVER']) == 13
    say('  R3: every N1 row needs at least one of NORM, TENSOR, LOWE, TRAP, all after COVER in the order %s: %s; the '
        'COVER rows (%d) and the B rows (%d) come first' % (' < '.join(ORDER), blocked, len(by['COVER']),
                                                            sum(1 for h in hits if BAIRE.get(h) == 'B')))
    t3 = dict(ROWS)
    t3[('PART-I-C-LOWENERGY.md', 497)] = 'SIGMA'
    ok['C3'] = not r3_test(t3)
    say('  C3 (control; Round 3): R3\'s test with I-C:497 re-tagged SIGMA only (no NORM, TENSOR, LOWE or TRAP) fails: %s'
        % ok['C3'])
    t2 = dict(ROWS)
    del t2[('PART-I-C-LOWENERGY.md', 497)]
    ok['C1'] = sorted(set(led) - set(t2)) == [('PART-I-C-LOWENERGY.md', 497)]
    say('  C1 (control): with I-C:497 removed from the table it is reported missing: %s' % ok['C1'])
    planted = baire_census(extra=[('PART-PLANTED.md', 1)])
    texts = ['by the closed-graph theorem', 'by the closed graph theorem', 'the open\u2013mapping theorem',
             'the theorem of Banach and Steinhaus', 'uniform boundedness principle']
    pat_ok = all(BAIRE_PAT.search(t) for t in texts) and not BAIRE_PAT.search('a closed curve in the graph')
    r1_miss = [t for t in texts if not BAIRE_PAT_R1.search(t)]
    ok['C2'] = [h for h in planted if h not in BAIRE] == [('PART-PLANTED.md', 1)] and pat_ok and len(r1_miss) == 3
    say('  C2 (control): a planted site is unclassified; the pattern finds %d planted phrasings (every dash) and not '
        '"a closed curve in the graph"; round 1\'s pattern misses %d of them (%s): %s' % (
            len(texts), len(r1_miss), '; '.join(r1_miss), ok['C2']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
