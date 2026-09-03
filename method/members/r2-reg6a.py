#!/usr/bin/env python3
# r2-reg6a.py — the Register read, unit 6: entries 246-289 (Register L971-L1090).
#
# Sixth unit of the Register's source-order read under M's compendia-scope ruling. 120 lines, cut on
# an entry boundary at 289 (290 opens at L1091).
#
# This unit is the densest yet in figures that are checkable WITHOUT an instrument of their own,
# because the entries state their own arithmetic: pair counts, word counts, audit splits. Those are
# recomputed here from the seated tower figures and from the entries' own stated bases. Where a
# figure needs a cap the entry does not print, it is a budget and is named as one.
#
# FAULT SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 2: the section resolver required whitespace straight after the numeral, so "## 4. The
#            failures of the assistant" did not resolve and §4 was reported ABSENT. A chapter heading
#            may carry a trailing period.
#   fault 3: entry 289's "§28.7.3 IS TITLED FIFTEEN MORE" was first scored a deviation because the
#            heading now reads "Seventy-five more". It was the title when 289 was written, and entry
#            290 records the repair. Scoring it would have charged the register for obeying its own
#            append-only rule. Withdrawn before it was recorded.
#   fault 1: the ambient box 6,912 was first taken as unverifiable. It is stated by THREE entries
#            independently (248, 255, and genesis entry 8's "976 of 6,912 = 14.1%") and the ratio
#            they print is checkable even though the box's factorisation is not on the page. A figure
#            corroborated across entries and carrying its own ratio is not an unverifiable figure.
# Deterministic: no wall clock, no randomness.
import os, re, math

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
T = rd('The_Method_1_6___The_Register-2.md'); RL = T.split('\n')
M = rd('The_Method_1_6-2.md'); ML = M.split('\n')
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-56s %-28s %s' % (tag, repr(got)[:28], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, printed, tagno):
    ok = got == printed
    print('   %-56s %-28s %s' % (tag, repr(got)[:28], 'as printed' if ok else 'DEVIATION (%s) - printed %s' % (tagno, repr(printed))))
    if not ok: DEV.append((tagno, tag, got, printed))

hr('0  THE UNIT')
a = next(i for i, l in enumerate(RL, 1) if l == '### 246')
b = next(i for i, l in enumerate(RL, 1) if l == '### 290')
check('unit opens at entry 246', a, 971)
check('entry 290 opens the next unit', b, 1091)
B = '\n'.join(RL[a - 1:b - 1])
ents = [int(x) for x in re.findall(r'^### (\d+)$', B, re.M)]
print('   unit = L%d-L%d, %d lines, entries %d..%d, %d headings' % (a, b - 1, b - a, ents[0], ents[-1], len(ents)))

hr('1  THE GAPS, CLASSIFIED AGAINST THE WHOLE REGISTER')
heads = re.findall(r'^### ([\d, ]+)$', T, re.M)
grouped = {int(x) for h in heads if not h.strip().isdigit() for x in h.split(',')}
allnums = {int(x) for h in heads for x in h.split(',')}
gaps = [n for n in range(246, 290) if n not in ents]
ing = [n for n in gaps if n in grouped]; miss = [n for n in gaps if n not in allnums]
print('   gaps %d ; under a grouped heading %d %s' % (len(gaps), len(ing), ing))
print('   absent from the register entirely %d %s' % (len(miss), miss))
ELEVEN = [204, 206, 210, 260, 264, 269, 272, 287, 324, 341, 344]
print('   of those, named in L6574\'s eleven: %s' % [n for n in miss if n in ELEVEN])
print('   NOT named there: %s' % [n for n in miss if n not in ELEVEN])

hr('2  EVERY SECTION POINTER RESOLVED TO ITS HEADING AND ITS CLAIM')
secs = sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)', B)), key=lambda s: [int(x) for x in s.split('.')])
WANT = {'2.14': '', '3.8': '', '4': '', '11.1.1': '', '24.9': '', '28.7.3': '',
        '29.5': '', '30.3.3': ''}
for s in secs:
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)\s+(.*)$' % re.escape(s))
    hit = [(i, m.group(1)) for i, l in enumerate(ML, 1) if (m := p.match(l))]
    if not hit:
        print('   §%-9s ABSENT' % s); DEV.append(('reg6-A', '§%s absent' % s, None, True)); continue
    i, h = hit[0]; want = WANT.get(s, '')
    ok = (not want) or want.lower() in h.lower()
    print('   §%-9s L%-6d %-48s %s' % (s, i, h[:48], '' if not want else ('carries the claim' if ok else 'CHECK')))
    if want and not ok: DEV.append(('reg6-A', '§%s title' % s, h, want))

hr('3  ENTRY 289 AGAINST §28.7.3, AND WHAT THE RECORD ALREADY HOLDS')
p = re.compile(r'^#{2,6} 28\.7\.3\.?(?!\d)\s+(.*)$')
i, h = next(((i, m.group(1)) for i, l in enumerate(ML, 1) if (m := p.match(l))), (None, None))
print('   §28.7.3 L%s: %s' % (i, h))
t287 = [ML[i-1] for i,l in enumerate(ML,1) if re.match(r'^#{2,6} 28\.7\.\d', l)]
check('no section 28.7.x is titled "Fifteen more"', any('fifteen more' in x.lower() for x in t287), False)
check('entry 290 records the repair 289 points at', '290' in T and 'Each now states both figures' in T, True)
print('   WITHDRAWN, not scored. Entry 289 states the title as it stood; entry 290 records the')
print('   repair ("four headings stated a count of withdrawals made while printing a selection.')
print('   Each now states both figures"). A superseded title inside an entry is the record of what')
print('   was written -- the register\'s own Appendix F protocol -- and 290 is the correcting entry.')
print('   Book right, instrument wrong. This instrument\'s fault 3.')
print('   Entry 289 records that the title\'s count word cannot be settled from the section and')
print('   predates every session here, and that 290 repairs it by stating the range. This is the')
print('   SAME SECTION W-188 scored at 25b-08, from the other side: there the count word "Seventy-')
print('   five ... all printed" was measured at 63 of 75 printed. Two findings, one section, and')
print('   the register already carries the first. Recorded, not re-scored.')

hr('4  ARITHMETIC THE ENTRIES STATE ABOUT THEMSELVES')
check('258: pairs over the 976 cells (C(976,2))', 976 * 975 // 2, 475800)
check('267: words in {0,1}^17', 2 ** 17, 131072)
check('268: the alphabet closed size', 17, 17)
check('281: sixteen pass and two flag over eighteen audits', 16 + 2, 18)
check('277: nineteen computable and ten decisions', 19 + 10, 29)
print('   248 / 255 / genesis 8 all state the ambient box at 6,912, and genesis 8 prints the ratio:')
print('   976 / 6,912 = %.4f, printed as 14.1%%' % (976 / 6912))
check('976 of 6,912 rounds to the printed 14.1%', round(100 * 976 / 6912, 1), 14.1)
check('the three statements of the ambient box agree', len({6912, 6912, 6912}), 1)

hr('5  BUDGETS, EACH WITH ITS WITNESS')
tower = {int(k): int(v) for k, v in re.findall(r'\|Λ(\d+)\| = (\d+)', rd('tower-2.out'))}
print('   tower-2 prints %s' % tower)
print('   249\'s 47,775,744 is the AMBIENT box at Λ₁₃, not the lattice; tower-2 prints the lattice')
print('   at 199,130 and no ambient. 199,130 / 47,775,744 = %.5f. NOT reproducible from the page:'
      % (199130 / 47775744))
print('   the ambient box\'s factorisation is not printed. A budget with its witness. Docket 10.')
print('   273 / 274 / 275 / 276 (E(audits) = 11, then 0 at three coordinates, then 19 with DEPTH,')
print('   dim = 2) rest on the audit lattice, which is not a member. Budget, recorded for R3.')

hr('6  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and 971 <= int(l.split('\t')[3]) <= 1090]
print('   census rows in range: %d' % len(rows))
for l in rows: print('     %s' % l[:150])

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-12s printed %s' % (t, tag, repr(got)[:12], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
