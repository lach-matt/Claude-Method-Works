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
LINE_CLASS = {}
for row in open(os.path.join(HERE, 'admiss5.tsv')):
    if not row.startswith('#'):
        f, c, x = row.rstrip('\n').split('\t', 2)
        LINE_CLASS.setdefault(f, []).append((x, c))
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
    have = sorted(L[i - 1] for i in h)
    want = sorted(x for x, c in LINE_CLASS[f])
    assert have == want, (f, [x for x in have if x not in want][:3], [x for x in want if x not in have][:3])
    for x, c in LINE_CLASS[f]:
        n[c] = n.get(c, 0) + 1
print('A1 occurrences:', sum(n.values()), 'lines in', len(PARTS), 'parts; by class', dict(sorted(n.items())))
cls = {(f, x): c for f in LINE_CLASS for x, c in LINE_CLASS[f]}
tri = [(f, l) for f in PARTS for l in text[f] if 'triangular' in l]
assert len(tri) == 1 and cls[tri[0]] == 'S', tri
H = {f: {x for x, c in LINE_CLASS[f] if c == 'H'} for f in ('PART-II-D-REGULARITY.md', 'PART-II-E-ENERGY.md')}
D, E = text['PART-II-D-REGULARITY.md'], text['PART-II-E-ENERGY.md']
assert any('II.C Lemma 2.5' in D[i] and 'Jordan' in D[i + 1] and {D[i], D[i + 1]} <= H['PART-II-D-REGULARITY.md']
           for i in range(len(D) - 1))
assert any('II.D Proposition 3.6' in E[i] and E[i] in H['PART-II-E-ENERGY.md']
           and any('not needed' in E[j] for j in range(i + 1, min(i + 6, len(E)))) for i in range(len(E)))
print('A2 "triangular" only in the statement of (3); h_I by Jordan scalings (II.D Proposition 3.6, II.E (1.2))')
print('admiss5 checks pass')
