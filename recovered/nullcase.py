print('  V3 CONFLATION AUDIT -- the candidate clean null case')
print()
V3=[
 ('FLAT','exactly flat / asymptotically flat / curved',
  'clean','Hawking-Ellis: asymptotic flatness has a precise conformal definition (Penrose). '
  'the three rungs are nested and standard.'),
 ('CONN','simply connected or not',
  'clean','a topological property of the manifold. no approximation, no scheme.'),
 ('HYP','globally hyperbolic or not',
  'clean','Hawking-Ellis: existence of a Cauchy surface. exact.'),
 ('GEN','the generic condition holds or not',
  'clean','Hawking-Ellis: every causal geodesic encounters some curvature. exact, '
  'and it is a hypothesis of the singularity theorems in that form.'),
 ('ASYM','has an asymptotic region / spatially compact',
  'clean','a topological property. exact.'),
]
for a,b,c,d in V3:
    print('  %-6s %-42s %-7s' % (a,b,c))
    print('  %-6s %s' % ('',d))
print()
print('  V6 for comparison')
V6=[('SC','solves the semiclassical Einstein equation','clean','exact statement'),
    ('HAD','Hadamard state','clean','precisely defined short-distance behaviour'),
    ('ACH','achronal geodesic','clean','exact causal-structure definition'),
    ('REG','within the semiclassical regime','CONFLATED',
     'no sharp definition. "curvature below Planck" and "G does not diverge" and '
     '"the expansion parameter is small" are different conditions.')]
for a,b,c,d in V6:
    print('  %-6s %-42s %-10s %s' % (a,b,c,d))
print()
print('  THE 2x2: CLOSURE x CONFLATION')
CELLS={('closed','clean')   :['V3 geometry (5 letters, E=0, 0 conflated)'],
       ('closed','conflated'):['Lambda (13 letters, E=0, 7 conflated, 1 ungrounded, 1 missing)',
                               'V6 solution (4 letters, E=0, 1 conflated)'],
       ('open','conflated')  :['V1 laws (15 letters, E=816, 5 of 9 conflated at nine letters)'],
       ('open','clean')      :[]}
for k in [('closed','clean'),('closed','conflated'),('open','clean'),('open','conflated')]:
    v=CELLS[k]
    print('     %-8s %-10s  %s' % (k[0],k[1], '; '.join(v) if v else 'EMPTY'))
print()
print('  IS THE EMPTY CELL EMPTY FOR A REASON?')
print('     open + clean would be: every letter means exactly what a source means,')
print('     and the index still fails to close.')
print('     nothing forbids it. openness comes from ARITY; conflation comes from')
print('     VOCABULARY. the computation in v1_by_W.py showed those are independent:')
print('     the defect survived every letter being split correctly.')
print('     -> the cell is empty by accident of what was built, not by necessity.')
print('     and the axis index is a near-miss: OPEN, and its letters are ungrounded')
print('        rather than conflated (they are my own constructs, so nothing to')
print('        conflate with) - which is a THIRD status, not a fourth cell.')
print()
print('  THE RESTATED NULL CASE')
print('     the paper uses Lambda for three jobs:')
print('        1  E = 0 is achievable                       -> HOLDS (all four schemes)')
print('        2  a universe is a globally consistent network -> WEAKENED')
print('        3  the clean control for sub-cases A and B    -> FAILS')
print()
print('     job 2 becomes: "one approximation scheme\'s bookkeeping of an atom is a')
print('        globally consistent network." the central-field approximation is not')
print('        a coordinate, so the claim is about the bookkeeping, not the universe.')
print()
print('     job 3 transfers to V3, which closes AND whose letters are exact.')
print()
print('  AND LAMBDA BECOMES A FOURTH INSTANCE, NOT A CONTROL')
print('     closed + conflated is its own category, and it is the interesting one:')
print('     it shows CLOSURE DOES NOT CERTIFY THE LETTERS.')
print('     an index can be globally consistent and still not mean what it says.')
print('     that is a stronger warning than anything the paper currently carries,')
print('     and it is the reason audit 22 exists at all.')