#!/usr/bin/env python3
"""AUDIT 28 -- CONTENTS. Every substantive claim in the paper, graded.
AUDIT 29 -- THE PAPER. Structure, delivery, and ratios."""
import re, json
from collections import Counter, defaultdict

MD=open('/mnt/user-data/outputs/Transitions.md').read()
D=json.load(open('/home/claude/paper/data.json'))
E=json.load(open('/home/claude/paper/data3.json'))
F=json.load(open('/home/claude/paper/data4.json'))
M=json.load(open('/home/claude/paper/math.json'))

# ---------------------------------------------------------------- structure
parts=re.findall(r'^## (Part [^\n·]+·[^\n]+)$',MD,re.M)
apps=re.findall(r'^## (Appendix [^\n]+)$',MD,re.M)
subs=re.findall(r'^### ([\d.]+[a-z]?) ([^\n]+)$',MD,re.M)
tables=MD.count('|---')
figs=len(set(re.findall(r'figures/([^)]+)',MD)))
quotes=len(re.findall(r'^> ',MD,re.M))
code=MD.count('```')//2
words=len(MD.split())

print('  AUDIT 28 -- CONTENTS')
print()
print('  STRUCTURE')
print('     parts %d   appendices %d   numbered subsections %d' % (len(parts),len(apps),len(subs)))
print('     tables %d   figures %d   display quotes %d   code blocks %d' % (tables,figs,quotes,code))
print('     words %d   chars %d' % (words,len(MD)))
print()

# ---------------------------------------------------------------- claim ledger
CLAIMS={
 'PROVED here':[
  'E(X) >= 0, i.e. X subset R(X)',
  'the girth of the unit-step graph is exactly 4',
  'R(A x B) = R(A) x R(B) with no linking constraint',
  'E(A x B) = |A|E_B + |B|E_A + E_A E_B',
 ],
 'COMPUTED here':[
  'E = 0 at every level of the tower, for parastatistics m = 1, 2, 3, to Lambda_13',
  'Lambda closes in all four coupling schemes under a uniform looseness convention',
  'the violation index: 2,370 cells E=30 at nine letters; 18,072 cells E=816 at fifteen',
  'core exactly one cell at both alphabets; collapse exact',
  'arity exactly 3; two minimal supports at fifteen letters',
  'six repair operations all fail; 0 of 5,760 relabellings close',
  'the frontier formulas exact on 1,500 sampled cells',
  'the periodic table: E=36, and E=0 on dropping group for l',
  'V3 geometry, V6 solution, the null-surface index and the ANEC proof index all CLOSE',
  'the cylinder factorisation |Lambda| = SUM_q |A_q||B_q| = 976, and every cross-section closed',
  'the measure: a faithful measure exists with 18 values; Coulomb resolves 47.7%',
  'C1: the induced bracket is diagonal in y; off-generator block 0.000e+00',
  'ten published LS term tables reproduced exactly (audit 23)',
  '8,856 exceeds its operation\'s bound of 40 (audit 27)',
 ],
 'CITED, correctly attributed':[
  'Freuder 1982; Montanari 1974; van Beek-Dechter',
  'Buniy-Hsu-Murray; Creminelli et al; Hartman-Kundu-Tajdini; Wall; Graham-Olum',
  'Brunetti-Fredenhagen-Verch: the four-part functor',
  'Tomita-Takesaki; Borchers; Wiesbrock; Araki-Zsido; Takesaki 1973',
  'Petz 1986; Hayden-Jozsa-Petz-Winter 2004; Casini-Teste-Torroba 2017',
  'Chandrasekaran-Flanagan 2026; Sorce 2024',
 ],
 'HELD, not promoted':[
  'B.3.1 as a general law about all indices',
  'pair-completion as a method for finding missing axes',
  'the four predicted axes',
  'defect 30 / 816 as physical numbers',
  'macroscopic locality as a candidate sixteenth letter',
  'the repair taxonomy: split / dictionary / translator',
 ],
 'OPEN, stated as such':[
  'C2: sigma_t(M(u2)) subset M(u2) on an isolated horizon',
  'HSMI on isolated horizons generally',
  'Graham-Olum in 4d (a CONJECTURE, not a theorem)',
  'a completeness criterion for any coordinate set',
  'the 26 term pairs checked at stated-subject grade only',
 ],
 'WITHDRAWN':[w[0] for w in E['withdrawals']]+[w[0] for w in F['withdrawals_2']],
}
print('  CLAIM LEDGER')
tot=0
for k,v in CLAIMS.items():
    print('     %-28s %d' % (k,len(v))); tot+=len(v)
print('     %-28s %d' % ('TOTAL',tot))
print()
print('  THE RATIO THAT MATTERS')
p=len(CLAIMS['PROVED here'])+len(CLAIMS['COMPUTED here'])
w=len(CLAIMS['WITHDRAWN'])
print('     established here (proved + computed) : %d' % p)
print('     withdrawn                            : %d' % w)
print('     ratio                                : %.2f established per withdrawal' % (p/w))
print()

# ---------------------------------------------------------------- coverage
print('  COVERAGE OF THE PAPER\'S OWN PROMISES')
PROM=[('two failure modes and no third','four objects demonstrated, plus V2 showing some vocabularies '
       'cannot be indexed at all','DELIVERED'),
      ('E measures whether an index can carry a constraint','the identification with global consistency, '
       'plus the density qualification','DELIVERED with a stated limit'),
      ('the core survives doubling the alphabet','computed at 9 and 15 letters','DELIVERED'),
      ('the vocabulary partition','DERIVED from BFV, not chosen','DELIVERED, and it supersedes the '
       'seven-vocabulary version the paper originally claimed'),
      ('the defect is a property of the system graph','WITHDRAWN. the graph is complete on T/M/A/S. '
       'the defect is arity.','NOT DELIVERED, and marked'),
      ('Lambda as the clean control','WITHDRAWN. 7 of 13 letters conflated. V3 is the clean case.',
       'NOT DELIVERED, and marked'),
      ('audit 22 is necessary and cannot be automated','21 audits passed on a document with five '
       'conflations; the debt is now discharged at 47 of 47 pairs','DELIVERED'),
      ('the axis set is open','E > 0 at 9 and 15 axes; ML added and inert','DELIVERED')]
print('  %-44s %s' % ('promise','status'))
for a,b,c in PROM: print('  %-44s %s' % (a,c))
print()
n_del=sum(1 for _,_,c in PROM if c.startswith('DELIVERED'))
print('     %d of %d delivered; %d withdrawn and marked in the text' % (n_del,len(PROM),len(PROM)-n_del))
print()

# ---------------------------------------------------------------- paper audit
print('  AUDIT 29 -- THE PAPER ITSELF')
print()
Q=[('does the abstract match the body?',
    'the abstract now states the four-vocabulary derivation and the complete graph. '
    'the severance claim was removed from it. YES.'),
   ('is every number backed or marked?',
    'audit 24: 10%% unbacked, of which the substantive residue is 43.1 (recorded as prose) '
    'and nothing else. audit 27: no impossible values remain. YES.'),
   ('is every equation stated with its hypotheses?',
    'NO. 15 of 50 have none recorded. this is the largest open defect in the document.'),
   ('does any part contradict another?',
    'audit 26 passes. the severance survived in three places after a local patch and was '
    'propagated on the second attempt.'),
   ('is the promotion ledger honest?',
    'five promoted, six held, and everything promoted is about the METHOD while everything '
    'held is a general claim or a physical number. the split was not planned.'),
   ('is the register complete?',
    'UNKNOWN and unknowable from inside. 30 entries, one of them an arithmetic error and 29 '
    'wrong inferences. audit 24 was built to estimate what remains and estimates provenance, '
    'not truth.'),
   ('would a reader be misled?',
    'the physics line ends at a named open problem in someone else\'s literature, with the '
    'one computed contribution (C1) clearly marked as one link and not the open one. '
    'the risk is that the volume of apparatus suggests more was established than was.')]
for a,b in Q:
    print('     %s' % a); print('        %s' % b); print()
print('  THE SINGLE LARGEST DEFECT')
print('     15 of 50 equations carry no recorded hypotheses.')
print('     that is the same failure audit 22 found at the level of COORDINATES,')
print('     appearing at the level of EQUATIONS, and it was not looked for until now.')
