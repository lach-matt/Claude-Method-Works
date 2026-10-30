# The uses of the constraint damping parameter gamma_C in the parts (VI.C section 3, D327).
#   G1  every occurrence in PART-*.md of \gamma_C, of s_C := gamma_C (1 - e_C)(1 - v_C), the one quantity defined from
#       it under another name, and of a citation of III.E Theorem 1.1 (also split over a line break), is listed below
#       with its class, and every listed line is such an occurrence: the enumeration is exact.
#   G2  III.E Theorem 1.1, proved at n = 4 for gamma_C = 1/h, h in Part IV''''s set H (co-countable in (0, h_*)),
#       is applied only at the one value of gamma_C fixed in III.F section 1 and III.K section 0 (classes F and T);
#       no line applies it over a range of values. The one family over a range, (tau gamma_C, tau gamma_Upsilon),
#       tau in [0, 1], in III.F' section 3 (class H), uses III.F Lemma 2.1's proof and III.E section 1, not the theorem.
# Classes: D an identity or definition valid for every gamma_C; F a condition on, or a use of, the one fixed value;
# T a citation of III.E Theorem 1.1 at that value; H the tau-family of III.F'; S III.E's statement; P Part IV''''
# and IV'''''', which prove the theorem; R the records of VI.C and VII.
import glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.dirname(HERE)
PAT = re.compile(r"\\gamma_C|(?<![A-Za-z_\\])s_C\b|III\.E Theorem 1\.1")

FILE_CLASS = {'PART-III-B-FAMILY.md': 'D', 'PART-III-E2-V1STATES.md': 'D', 'PART-IV5-CDMODES.md': 'P',
              'PART-IV7-TFACE.md': 'P', 'PART-VI4-PARAMS.md': 'R', 'PART-VII-ASSEMBLY.md': 'R'}
LINE_CLASS = {
    'PART-III-C-EXTERIOR.md': {35: 'F', 296: 'D', 514: 'F'},
    'PART-III-C2-POLYHOM.md': {135: 'F', 224: 'F'},
    'PART-III-E-CONSTRAINT.md': {21: 'D', 24: 'D', 39: 'S', 56: 'S', 57: 'S', 63: 'D', 69: 'F'},
    'PART-III-F-LINEARISED.md': {23: 'F', 24: 'F', 38: 'D', 96: 'D', 116: 'D', 118: 'D', 165: 'D', 171: 'D',
                                 247: 'T'},
    'PART-III-F2-INDICIAL.md': {23: 'D', 24: 'T', 31: 'F', 37: 'T', 38: 'T', 53: 'T', 55: 'F', 75: 'D', 89: 'D',
                                90: 'D', 95: 'D', 96: 'D', 101: 'D', 118: 'D', 149: 'D', 166: 'D', 276: 'H', 277: 'H',
                                384: 'H', 412: 'T', 419: 'D', 430: 'F', 506: 'T'},
    'PART-III-F3-MODES.md': {21: 'F', 26: 'F', 28: 'F', 29: 'D', 38: 'D', 231: 'T', 281: 'F'},
    'PART-III-F4-ZERO.md': {348: 'T'},
    'PART-III-F5-PAIRINGS.md': {328: 'T'},
    'PART-III-G2-IOTA.md': {47: 'D', 55: 'D', 57: 'D', 59: 'D', 68: 'D', 72: 'D', 74: 'D', 116: 'D', 208: 'F',
                            215: 'F', 220: 'F', 263: 'F', 279: 'F', 493: 'F'},
    'PART-III-G3-GRAFT.md': {30: 'F', 33: 'F', 34: 'F', 37: 'F', 68: 'F', 282: 'F', 390: 'F', 401: 'F', 402: 'F',
                             403: 'F'},
    'PART-III-G4-RESONANT.md': {10: 'D', 11: 'F', 19: 'F', 34: 'F', 37: 'F', 71: 'F', 144: 'F', 145: 'F'},
    'PART-III-H3-UNIFORM.md': {30: 'F', 50: 'T', 116: 'D', 118: 'D', 125: 'D', 143: 'F', 380: 'T'},
    'PART-III-I11-SPACETIME.md': {43: 'F', 49: 'F', 374: 'F', 413: 'F'},
    'PART-III-I2-SCRI.md': {17: 'F', 29: 'F', 30: 'F', 31: 'F', 253: 'F', 254: 'F'},
    'PART-III-I6-ALMOSTBDD.md': {30: 'F', 125: 'F', 132: 'F'},
    'PART-III-I9-COMMOTION.md': {258: 'F'},
    'PART-III-J-PARAM.md': {43: 'F'},
    'PART-III-K-NONLINEAR.md': {7: 'T', 49: 'F', 50: 'F', 513: 'T', 568: 'T'},
    'PART-IV2-TAME.md': {111: 'D'},
    'PART-IV3-NM.md': {27: 'D', 29: 'F'},
}


def hits(path):
    L = open(path).read().split('\n')
    out = set()
    for i, l in enumerate(L, 1):
        if PAT.search(l):
            out.add(i)
        elif l.rstrip().endswith('III.E') and i < len(L) and L[i].startswith('Theorem 1.1'):
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
    assert h == set(LINE_CLASS[f]), (f, sorted(h - set(LINE_CLASS[f])), sorted(set(LINE_CLASS[f]) - h))
    for c in LINE_CLASS[f].values():
        n[c] = n.get(c, 0) + 1
print('G1 occurrences:', sum(len(h) for h in found.values()), 'lines in', len(found), 'parts; by class',
      dict(sorted(n.items())))
# G2: the classes that apply the theorem are F and T only; H is the one range, and it does not cite the theorem.
F2 = open(os.path.join(P5, 'PART-III-F2-INDICIAL.md')).read().split('\n')
for i in (276, 277, 384):
    assert 'III.E Theorem 1.1' not in F2[i - 1]
assert 'proof of III.F Lemma 2.1' in ' '.join(F2[275:279]) and 'III.E section 1' in ' '.join(F2[275:281])
print('G2 III.E Theorem 1.1 is applied at the one fixed gamma_C only; the tau-family uses III.F Lemma 2.1 and III.E '
      'section 1')
print('gammac5 checks pass')
