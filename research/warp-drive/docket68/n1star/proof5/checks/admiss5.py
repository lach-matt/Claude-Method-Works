# II.F' Lemma 2.1 (b): condition (3) of II.C Definition 3.3 is not used by II.D, II.D' and II.E (D327).
#   A1  Condition (3) is a statement about p_1 = S|dX + p~_1 and p_0 over dX: a lower triangular splitting. A step
#       can use it only where it names p_0, p_1 (with p~_1, p-bar_1), the fibre inner product h_I built from p_1, the
#       triangular structure, or the condition itself. Every such line of II.C, II.C', II.D, II.D' and II.E is listed
#       below with its class, and every listed line is such a line: the enumeration is exact.
#   A2  "triangular" occurs only in the statement of (3); h_I is built by Jordan scalings at points, continuity and a
#       partition of unity, which needs no triangular structure; the remaining classes use (1)-(2), the definition of
#       p-bar_1, or the threshold Re_{h_I} p_1 >= p-bar_1 - delta'.
# Classes: S the statement of (3); Df the data (3.1)-(3.2) and Definition 3.5; N normal forms and commutators, which
# use (1)-(2); Th the threshold and its consequences; H the construction of h_I; R remarks on the source;
# U another object named p_1 (I.B's symbol at the trapped set, II.C''s dual metric function).
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.dirname(HERE)
PAT = re.compile(r"(?<![a-zA-Z])p_0|(?<![a-zA-Z])p_1|h_I|triangular|Definition 3\.3 \(3\)|condition \(3\)|"
                 r"\(3\) of II\.C")

FILE_CLASS = {'PART-II-C2-TRAPPING.md': 'U'}
LINE_CLASS = {
    'PART-II-C-OPERATORS.md': {193: 'U', 194: 'U', 198: 'U', 208: 'U', 475: 'Df', 477: 'Df', 478: 'Df', 480: 'S',
                               481: 'S', 489: 'N', 490: 'N', 491: 'N', 495: 'N', 497: 'N', 503: 'Df', 504: 'Df',
                               507: 'R', 511: 'Df'},
    'PART-II-D-REGULARITY.md': {54: 'N', 121: 'Th', 122: 'Th', 411: 'Th', 412: 'Th', 423: 'N', 434: 'N', 435: 'N',
                                436: 'N', 438: 'N', 493: 'Th', 494: 'Th', 498: 'H', 499: 'H', 500: 'H', 501: 'H',
                                504: 'Th', 505: 'Th', 506: 'Th', 568: 'U'},
    'PART-II-D2-BREGULARITY.md': {328: 'N', 330: 'N', 331: 'N', 333: 'N', 337: 'N', 661: 'R'},
    'PART-II-E-ENERGY.md': {23: 'R', 24: 'R', 79: 'N', 80: 'N', 81: 'N', 91: 'N', 92: 'N', 98: 'N', 101: 'R',
                            102: 'R', 106: 'H', 109: 'H', 110: 'R', 122: 'N', 134: 'N', 135: 'H', 329: 'Th',
                            341: 'Th', 357: 'N', 359: 'Th', 362: 'Th', 363: 'Th', 364: 'Th', 375: 'Th', 378: 'Th',
                            380: 'Th', 396: 'Th', 402: 'Th', 403: 'Th', 423: 'Th', 442: 'Th', 506: 'Th', 520: 'Th',
                            521: 'Th', 537: 'Th', 539: 'Th', 648: 'Th', 802: 'N', 803: 'N', 810: 'Th', 1210: 'R',
                            1212: 'R', 1215: 'R', 1216: 'R', 1217: 'R', 1218: 'R', 1257: 'R', 1273: 'R'},
}
PARTS = ['PART-II-C-OPERATORS.md', 'PART-II-C2-TRAPPING.md', 'PART-II-D-REGULARITY.md', 'PART-II-D2-BREGULARITY.md',
         'PART-II-E-ENERGY.md']

text, n = {}, {}
for f in PARTS:
    L = open(os.path.join(P5, f)).read().split('\n')
    text[f] = L
    h = {i for i, l in enumerate(L, 1) if PAT.search(l)}
    if f in FILE_CLASS:
        n[FILE_CLASS[f]] = n.get(FILE_CLASS[f], 0) + len(h)
        continue
    assert h == set(LINE_CLASS[f]), (f, sorted(h - set(LINE_CLASS[f])), sorted(set(LINE_CLASS[f]) - h))
    for c in LINE_CLASS[f].values():
        n[c] = n.get(c, 0) + 1
print('A1 occurrences:', sum(n.values()), 'lines in', len(PARTS), 'parts; by class', dict(sorted(n.items())))
tri = [(f, i) for f in PARTS for i, l in enumerate(text[f], 1) if 'triangular' in l]
assert tri == [('PART-II-C-OPERATORS.md', 481)], tri
D = text['PART-II-D-REGULARITY.md']
assert 'Jordan' in D[499] and 'II.C Lemma 2.5' in D[498]
E = text['PART-II-E-ENERGY.md']
assert 'II.D Proposition 3.6' in E[105] and 'not needed' in E[109]
print('A2 "triangular" only in the statement of (3); h_I by Jordan scalings (II.D Proposition 3.6, II.E (1.2))')
print('admiss5 checks pass')
