NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
# (theorem, [terms it names]) - drawn from the chargers and the lattice-side theorems used
THMS={
 'Buniy-Hsu-Murray'      : ['X','NEC','U'],
 'Hartman-Kundu-Tajdini' : ['U','X','SD','NEC'],
 'Wall (GSL)'            : ['X','U','NEC'],
 'Graham-Olum'           : ['NEC'],
 'spin-statistics (Luders-Zumino)': ['X','SD','U','Sc'],
 'Burgoyne (spin-locality)': ['SD'],
 'Tsirelson'             : ['Sc'],
 'Popescu-Rohrlich'      : ['Sc','IC'],
 'Pawlowski (info causality)': ['IC','Sc'],
 'Banks-Susskind-Peskin' : ['U','IC'],
 'Nikolic'               : ['U'],
 'Polchinski / Gisin'    : ['L','IC'],
 'Abrams-Lloyd'          : ['L'],
 'Weinberg (nonlinear QM)': ['L'],
 'Wootters-Zurek / Dieks': ['DNc'],
 'Rastegin'              : ['DNc','DNd'],
 'Simon-Buzek-Gisin'     : ['DNc','IC'],
 'Soulas'                : ['SD','IC'],
 'Sorkin'                : ['SD'],
 'Creminelli et al'      : ['NEC','X'],
 'Ford-Roman'            : ['NEC'],
 'Dubovsky-Sibiryakov'   : ['X','U'],
 'Deutsch / Lloyd (CTC)' : ['X','U','L','DNc','DNd'],
 'Ishibashi-Maeda-Mefford': ['NEC','X'],
}
# pairs actually checked this session, with outcome
CHECKED={
 ('U','spin-statistics (Luders-Zumino)') : 'CONFLATION - metric vs CPTP',
 ('U','Nikolic')                          : 'match - Lindblad rung occupied',
 ('U','Banks-Susskind-Peskin')            : 'match - the rung was graded from it',
 ('L','Weinberg (nonlinear QM)')          : 'CONFLATION - dynamical vs kinematical',
 ('L','Abrams-Lloyd')                     : 'match - Weinberg-type',
 ('L','Polchinski / Gisin')               : 'match - Weinberg-type',
 ('SD','Burgoyne (spin-locality)')        : 'CONFLATION - observables vs fields',
 ('SD','spin-statistics (Luders-Zumino)') : 'CONFLATION - observables vs fields',
 ('NEC','Graham-Olum')                    : 'CONFLATION - ANEC vs achronal ANEC',
 ('NEC','Ford-Roman')                     : 'match - scale grading',
 ('X','Buniy-Hsu-Murray')                 : 'CONFLATION - spontaneous vs explicit; stated vs operative',
 ('X','Creminelli et al')                 : 'CONFLATION - same',
 ('X','Dubovsky-Sibiryakov')              : 'match',
 ('Sc','Tsirelson')                       : 'match - graded by CHSH value',
 ('DNc','Rastegin')                       : 'PARTIAL - deterministic vs probabilistic',
 ('DNd','Rastegin')                       : 'PARTIAL - same',
}
pairs=[(c,t) for t,cs in THMS.items() for c in cs]
print('  AUDIT 22 - TERM MATCH')
print('     coordinates                 : %d' % len(NM))
print('     theorems naming a coordinate: %d' % len(THMS))
print('     term-sharing pairs          : %d' % len(pairs))
print('     pairs checked this session  : %d  (%.0f%%)' % (len(CHECKED), 100*len(CHECKED)/len(pairs)))
print()
conf=sum(1 for v in CHECKED.values() if v.startswith('CONFLATION'))
part=sum(1 for v in CHECKED.values() if v.startswith('PARTIAL'))
ok=len(CHECKED)-conf-part
print('     of those checked: %d conflations, %d partial, %d matches' % (conf,part,ok))
print('     conflation rate among checked: %.0f%%' % (100*(conf+part)/len(CHECKED)))
print()
unchecked=[p for p in pairs if p not in CHECKED]
print('     UNCHECKED PAIRS: %d' % len(unchecked))
est=(conf+part)/len(CHECKED)*len(unchecked)
print('     expected further conflations at the observed rate: %.0f' % est)
print()
print('     (the estimate assumes the checked pairs are representative;')
print('      they are not - they were selected because a question forced them,')
print('      so the true rate among unchecked pairs is probably LOWER)')
print()
from collections import defaultdict
by=defaultdict(list)
for c,t in unchecked: by[c].append(t)
print('  UNCHECKED, BY COORDINATE')
for c in NM:
    if by[c]: print('     %-4s (%d) %s' % (c,len(by[c]),', '.join(by[c])))
print()
print('  WHY THIS CANNOT JOIN AUDITS 1-21')
print('     audits 1-21 compare the index against itself: counts, closure, coherence, arithmetic.')
print('     audit 22 compares a rung against an external theorem\'s meaning of the same word.')
print('     no computation on the index can perform it - the second term is not in the index.')
print('     it is a retrieval-and-judgement audit, and its output is a DEBT, not a pass/fail.')