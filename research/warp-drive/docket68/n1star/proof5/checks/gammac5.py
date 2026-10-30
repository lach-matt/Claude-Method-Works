# The uses of the constraint damping parameter gamma_C in the parts (VI.C section 3; D327, D328).
# Every statement derived from III.E Theorem 1.1 (III.E sections 2-3, III.E', (C1)-(C5)) concerns Box^C_b at the
# parameters fixed in III.E (PART-III-E-CONSTRAINT.md:69, VI.C rows c1-c4). To apply one at another value a part must
# write an operator with another damping parameter, and the damping enters Box^C_b, delta^*_{g,E_C} and E^C only
# through gamma_C: such a use names gamma_C, s_C := gamma_C (1 - e_C)(1 - v_C), h := 1/gamma_C (the variable of
# Parts IV''''-IV'''''', which prove the theorem), or a rescaled E_C. So:
#   G1  every occurrence in PART-*.md of \gamma_C, of s_C, and of a citation of III.E Theorem 1.1 (also split over a
#       line break, either way) is listed below with its class, and every listed line is such an occurrence;
#   G2  the theorem is applied only at the one fixed value (classes F and T). The one family over a range,
#       (tau gamma_C, tau gamma_Upsilon), tau in [0, 1], in III.F' section 3 (class H), uses III.F Lemma 2.1's proof and
#       III.E section 1, not the theorem;
#   G3  no rescaled damping operator occurs elsewhere: every line naming E_C, E^C or Box^C together with tau, a family
#       or a homotopy is listed below with what it is (spectral families in the frequency, a time range).
# Classes: D an identity or definition valid for every gamma_C; F a condition on, or a use of, the one fixed value;
# T a citation of III.E Theorem 1.1 at that value; H the tau-family of III.F'; S III.E's statement; P Parts IV'''' and
# IV'''''' (IV''''', written in h, names neither); R the records of VI.C and VII, and the record's computation at its
# own point gamma_C = 10^6 (III.F' line 55), which lies outside the proved set.
import glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.dirname(HERE)
PAT = re.compile(r"\\gamma_C|(?<![A-Za-z_\\])s_C\b|III\.E Theorem 1\.1")

FILE_CLASS = {'PART-III-B-FAMILY.md': 'D', 'PART-IV5-CDMODES.md': 'P', 'PART-IV7-TFACE.md': 'P',
              'PART-VI4-PARAMS.md': 'R', 'PART-VII-ASSEMBLY.md': 'R'}
LINE_CLASS = {}
for row in open(os.path.join(HERE, 'gammac5.tsv')):
    if not row.startswith('#'):
        f, c, x = row.rstrip('\n').split('\t', 2)
        LINE_CLASS.setdefault(f, []).append((x, c))
FAM = {('PART-III-F-LINEARISED.md', r'The spectral family is'): 'the spectral family in the frequency',
       ('PART-IV-EB.md', r'the $\tau$-range'): 'a range of the time variable tau',
       ('PART-IV5-CDMODES.md', r'(PART-I-SPECTRAL.md after (1.3)) of the spectral family'):
           'the spectral family (proof)',
       ('PART-IV5-CDMODES.md', r'**Lemma 1.6 (the hypotheses of Part I).**'): 'the spectral family (proof)',
       ('PART-IV7-TFACE.md', r'the spectral family of the dilation-invariant'): 'the spectral family of the tf model',
       ('PART-IV7-TFACE.md', r'the spectral family at $-\sigma$'): 'the spectral family at -sigma (proof)'}
RECORDS = {'PART-VI4-PARAMS.md', 'PART-VII-ASSEMBLY.md'}


def hits(path):
    L = open(path).read().split('\n')
    out = set()
    for i, l in enumerate(L, 1):
        if PAT.search(l):
            out.add(i)
        elif i < len(L) and ((l.rstrip().endswith('III.E') and L[i].startswith('Theorem 1.1')) or
                             (l.rstrip().endswith('III.E Theorem') and L[i].startswith('1.1'))):
            out.add(i)
    return out


found = {}
for f in sorted(glob.glob(os.path.join(P5, 'PART-*.md'))):
    h = hits(f)
    if h:
        found[os.path.basename(f)] = h
listed = set(FILE_CLASS) | set(LINE_CLASS)
assert set(found) == listed, (sorted(set(found) - listed), sorted(listed - set(found)))
n = {}
for f, h in found.items():
    if f in FILE_CLASS:
        n[FILE_CLASS[f]] = n.get(FILE_CLASS[f], 0) + len(h)
        continue
    L = open(os.path.join(P5, f)).read().split('\n')
    have = sorted(L[i - 1] for i in h)
    want = sorted(x for x, c in LINE_CLASS[f])
    assert have == want, (f, [x for x in have if x not in want][:3], [x for x in want if x not in have][:3])
    for x, c in LINE_CLASS[f]:
        n[c] = n.get(c, 0) + 1
print('G1 occurrences:', sum(len(h) for h in found.values()), 'lines in', len(found), 'parts; by class',
      dict(sorted(n.items())))
F2 = open(os.path.join(P5, 'PART-III-F2-INDICIAL.md')).read().split('\n')
Hl = [F2.index(x) for x, c in LINE_CLASS['PART-III-F2-INDICIAL.md'] if c == 'H']
assert len(Hl) == 3 and all('III.E Theorem 1.1' not in F2[i] for i in Hl)
assert 'proof of III.F Lemma 2.1' in ' '.join(F2[Hl[0]:Hl[0] + 3]) and 'III.E section 1' in ' '.join(F2[Hl[0]:Hl[0] + 5])
print('G2 III.E Theorem 1.1 is applied at the one fixed gamma_C only; the tau-family uses III.F Lemma 2.1 and III.E '
      'section 1')
op = re.compile(r"E_C|E\^C|E\^\{C\}|\\Box\^C")
fam = re.compile(r"\\tau|homotop|family|families")
seen = [(os.path.basename(f), l) for f in glob.glob(os.path.join(P5, 'PART-*.md'))
        if os.path.basename(f) not in RECORDS
        for l in open(f).read().split('\n') if op.search(l) and fam.search(l)]
assert len(seen) == len(FAM), seen
for f, l in seen:
    assert sum(1 for (g, key) in FAM if g == f and key in l) == 1, (f, l)
print('G3 no rescaled damping operator: the', len(FAM), 'lines pairing E_C, E^C or Box^C with a family are spectral '
      'families or a time range')
print('gammac5 checks pass')
