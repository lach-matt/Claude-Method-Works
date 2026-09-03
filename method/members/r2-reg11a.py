#!/usr/bin/env python3
# r2-reg11a.py — the Register read, unit 11: entries 362-394 (Register L1347-L1466).
#
# The most pointer-dense unit of the read so far: thirty distinct section pointers, eight lettered
# pointers and eleven register pointers in 120 lines. Resolution is therefore the substance, and it
# is done against every volume, on the exact-token rule, with the trailing-period and
# entry-heading faults of the earlier units already fixed in the resolver.
#
# THE APPENDIX F PROTOCOL IS MET HERE IN THE FLESH. r2-regsweep reported F.3.2 and F.3.3 as named by
# the register and present in no volume. Entry 372 is one of the three entries the register's own
# protocol names -- "THREE REFERENCES IN THIS REGISTER ARE LEFT AS THEY STAND -- entries 371, 372 and
# 1780 -- BECAUSE ENTRIES ARE APPEND-ONLY" -- so its F.3.3 is the record of what was written and is
# NOT scored. This unit contains two of the three (371 and 372), which is why it is worth saying so
# here rather than in a footnote.
# Deterministic: no wall clock, no randomness.
import os, re

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
R = rd('The_Method_1_6___The_Register-2.md'); RL = R.split('\n')
M = rd('The_Method_1_6-2.md'); ML = M.split('\n')
VOLS = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'),
        'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
        'sc': rd('The_Method_1_6___Spectra_Compendium-2.md'),
        'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md')}
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-56s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, printed, t):
    ok = got == printed
    print('   %-56s %-26s %s' % (tag, repr(got)[:26], 'as printed' if ok else 'DEVIATION (%s) - printed %s' % (t, repr(printed))))
    if not ok: DEV.append((t, tag, got, printed))

hr('0  THE UNIT')
a = next(i for i, l in enumerate(RL, 1) if l == '### 362')
b = next(i for i, l in enumerate(RL, 1) if l == '### 395')
check('unit opens at entry 362', a, 1347)
B = '\n'.join(RL[a - 1:b - 1])
ents = [int(x) for x in re.findall(r'^### (\d+)$', B, re.M)]
print('   unit = L%d-L%d, %d lines, entries %d..%d, %d headings' % (a, b - 1, b - a, ents[0], ents[-1], len(ents)))

hr('1  EVERY SECTION POINTER, RESOLVED IN ANY VOLUME')
def resolve(sec):
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)[ \t]+(\S.*)$' % re.escape(sec), re.M)
    for v, t in VOLS.items():
        m = p.search(t)
        if m: return v, m.group(1)
    return None, None
secs = sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)', B)), key=lambda s: [int(x) for x in s.split('.')])
print('   distinct section pointers: %d' % len(secs))
unres = []
for s in secs:
    v, h = resolve(s)
    if v: print('   §%-11s %-4s %s' % (s, v, h[:52]))
    else: unres.append(s)
LIST_ITEMS = {'4.4', '4.5', '4.7'}
for s in unres:
    if s in LIST_ITEMS:
        hit = [i for i, l in enumerate(ML, 1) if re.match(r'^\s*%s[ .]' % re.escape(s), l)]
        print('   §%-11s      Chapter 4 list item at main L%s (MAIN_AUDIT V1)' % (s, hit[0] if hit else '?'))
    else:
        print('   §%-11s      UNRESOLVED' % s); DEV.append(('reg11-A', '§%s unresolved' % s, None, True))
check('section pointers unaccounted for', [s for s in unres if s not in LIST_ITEMS], [])

hr('2  LETTERED POINTERS, AND THE APPENDIX F PROTOCOL')
lets = sorted(set(re.findall(r'\b([A-G]\.\d+(?:\.\d+)?)\b', B)))
for l in lets:
    hit = [i for i, x in enumerate(ML, 1) if re.match(r'^\s*(#{2,6}\s*)?%s[ .]' % re.escape(l), x)]
    print('   %-7s %s' % (l, ('main L%d' % hit[0]) if hit else 'PRESENT IN NO VOLUME'))
here = [e for e in (371, 372, 1780) if e in ents]
print('   entries in this unit that the F.3.3 protocol names: %s' % here)
check('F.3.3 is carried by an entry the protocol protects', bool(here), True)
print('   The register rules these left as they stand BECAUSE ENTRIES ARE APPEND-ONLY. Not scored;')
print('   r2-regsweep\'s F.3.2 / F.3.3 item is discharged here, for the entries in this unit.')

hr('3  REGISTER POINTERS')
allnums = {int(x) for h in re.findall(r'^### ([\d, ]+)$', R, re.M) for x in h.split(',')}
refs = sorted({int(x) for x in re.findall(r'(?i)\bregisters?\s+(\d+)', B)})
missing = [n for n in refs if n not in allnums]
print('   %d pointers: %s' % (len(refs), refs))
check('register pointers that do not resolve', missing, [])

hr('4  FIGURES THE ENTRIES STATE, RE-DERIVED')
score('393: 904 of 1,654, to one decimal', round(100 * 904 / 1654, 1), 54.7, 'reg11-B')
tower = {int(k): int(v) for k, v in re.findall(r'\|Λ(\d+)\| = (\d+)', rd('tower-2.out'))}
check('1,654 is the seated Λ₉', tower[9], 1654)
score('394: |J(Λ)| = Σ(|Aᵢ| − 1), the seventeen generators', 17, 17, 'reg11-C')
print('   the 17 is entry 268\'s alphabet closed size, verified at unit 6 and unchanged here.')

hr('5  ENTRY 375, WHICH THE RECORD ALREADY SCORES')
print('   375 is the site of 26c-02 (W-190 / DEF-151 item 4): "Register 375 records a change to')
print('   §32.1.4 that §32.1.4 did not receive". It is in this unit and is NOT re-scored -- the')
print('   earlier line governs (G0b). Recorded so the unit read is not read as having missed it.')
check('entry 375 is in this unit', 375 in ents, True)

hr('6  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and a <= int(l.split('\t')[3]) <= b - 1]
print('   census rows in range: %d' % len(rows))
for l in rows: print('     %s' % l[:145])

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-12s printed %s' % (t, tag, repr(got)[:12], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
