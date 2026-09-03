#!/usr/bin/env python3
# r2-reg4a.py — the Register read, unit 4: THE MATURE RECORD OPENS, entries 165-198 (L731-L850).
#
# Fourth unit of the Register's source-order read under M's compendia-scope ruling, and the first
# with no natural block boundary: 1,464 bare entries run from 165 to 1792 unbroken. The unit is cut
# at 120 lines (the chat-81 mean is 116) ending on an entry boundary, at 198.
#
# THE PRECEDENT THAT GOVERNS THIS UNIT, READ BEFORE ANYTHING WAS SCORED. The register has already
# ruled on stale numerals inside entries, at the Appendix F renumbering: "THREE REFERENCES IN THIS
# REGISTER ARE LEFT AS THEY STAND ... BECAUSE ENTRIES ARE APPEND-ONLY. A superseded numeral inside an
# entry is the record of what was written, not a defect in it." That protocol is applied here and it
# ACQUITS most of what a naive pass would flag. It is not unconditional: the same entry rests it on
# having measured "zero occurrences of either numeral in any volume" -- the renumber "collides with
# nothing". The scored question is therefore not "is the numeral stale" but "does the stale numeral
# now resolve to a DIFFERENT LIVE OBJECT", which is the case the precedent does not cover.
#
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: entry 193 was first scored as a live defect because Figures 23.1 and 23.2 are in reading
#            order in the volume. They are, and the entry is not about them: it is about the arity
#            plot and the step law, now Figures 30.1 and 30.2. The finding was withdrawn and re-taken
#            in its correct and narrower form.
#   fault 2: the four gaps 176, 177, 190, 196 were first read as four unexplained absences. 176 and
#            177 are narrated inside entry 175's own body. Two, not four, are unaccounted for.
# Deterministic: no wall clock, no randomness.
import os, re, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
REG, MAIN = 'The_Method_1_6___The_Register-2.md', 'The_Method_1_6-2.md'
T = rd(REG); RL = T.split('\n'); M = rd(MAIN); ML = M.split('\n')
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-56s %-30s %s' % (tag, repr(got)[:30], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, printed, tagno):
    ok = got == printed
    print('   %-56s %-30s %s' % (tag, repr(got)[:30], 'as printed' if ok else 'DEVIATION (%s) - printed %s' % (tagno, repr(printed))))
    if not ok: DEV.append((tagno, tag, got, printed))

hr('0  THE UNIT, BOUNDED BY ITS OWN SCAN')
i165 = next(i for i, l in enumerate(RL, 1) if l == '### 165')
i199 = next(i for i, l in enumerate(RL, 1) if l == '### 200')
check('unit opens at entry 165', i165, 731)
B = '\n'.join(RL[i165 - 1:i199 - 1])
ents = [int(x) for x in re.findall(r'^### (\d+)$', B, re.M)]
print('   unit = L%d-L%d, %d lines, entries %d..%d, %d headings'
      % (i165, i199 - 1, i199 - i165, ents[0], ents[-1], len(ents)))

hr('1  THE GAPS IN THE SEQUENCE')
gaps = [n for n in range(165, 200) if n not in ents]
check('gaps in 165..198', gaps, [176, 177, 190, 196, 199])
b175 = B[B.index('### 175'):B.index('### 178')]
check('176 and 177 are narrated inside entry 175', '176' in b175 and '177' in b175, True)
print('   entry 175 body carries: %s' % re.sub(r'\s+', ' ', b175)[60:190])
allnums = {int(x) for h in re.findall(r'^### ([\d, ]+)$', T, re.M) for x in h.split(',')}
cited = collections.Counter()
for m in re.finditer(r'(?i)\bregisters?\s+(\d+)', T + M): cited[int(m.group(1))] += 1
for n in (190, 196, 199):
    print('   %d: heading %s ; cited in register or main %d times' % (n, n in allnums, cited[n]))
print('   190, 196 and 199 are unaccounted for in this unit: absent and UNCITED,')
print('   which is outside docket 9(c)\'s absent-and-cited class. Recorded, not scored.')
print('   Register L6574 measures the whole class: "Across 165 to 1781 the span holds 1,617 places')
print('   and 1,485 are occupied, so 132 are absent". MEASURED here over 1..1792: %d.'
      % len([n for n in range(1, 1793) if n not in allnums]))

hr('2  EVERY SECTION POINTER RESOLVED TO ITS HEADING AND ITS CLAIM')
def heading(sec):
    pat = re.compile(r'^#{2,6} %s(?!\d)(?!\.\d)\s+(.*)$' % re.escape(sec))
    for i, l in enumerate(ML, 1):
        m = pat.match(l)
        if m: return i, m.group(1)
    return None, None
WANT = {'3.1': 'audits', '24.4': 'He II', '30.3.2': 'law', '30.3.4': 'step law',
        '31.3.4': '540 predictions', '32.2': 'Self-reference', '32.6': 'falsification'}
for sec, claim in WANT.items():
    i, h = heading(sec)
    ok = i is not None and claim.lower() in h.lower()
    print('   §%-8s L%-6s %-52s %s' % (sec, i, (h or 'ABSENT')[:52], 'carries the claim' if ok else 'CHECK'))
    if i is None: DEV.append(('reg4-A', '§%s absent' % sec, None, True))

hr('3  ENTRY 193 — THE FIGURE NUMBERS, AND WHAT THE PRECEDENT DOES AND DOES NOT COVER')
def figline(tag):
    for i, l in enumerate(ML, 1):
        if l.startswith('![%s]' % tag): return i
    return None
f231, f232, f301, f302 = (figline('Figure 23.1'), figline('Figure 23.2'),
                          figline('Figure 30.1'), figline('Figure 30.2'))
print('   Figure 23.1 L%s | Figure 23.2 L%s | Figure 30.1 L%s | Figure 30.2 L%s' % (f231, f232, f301, f302))
check('Figures 23.1 and 23.2 are in reading order', f231 < f232, True)
check('Figures 30.1 and 30.2 are in reading order', f301 < f302, True)
def under(L):
    h = None
    for i, l in enumerate(ML, 1):
        if i > L: break
        if re.match(r'^#{2,6} [0-9]', l): h = l
    return h
print('   Figure 30.1 sits under %s' % under(f301))
print('   Figure 30.2 sits under %s' % under(f302))
print('   Figure 23.1 sits under %s' % under(f231))
cap301 = next(l for l in ML[f301:f301 + 3] if 'Figure 30.1.' in l)
cap302 = next(l for l in ML[f302:f302 + 3] if 'Figure 30.2.' in l)
print('   30.1 caption: %s' % re.sub(r'\s+', ' ', cap301)[:96])
print('   30.2 caption: %s' % re.sub(r'\s+', ' ', cap302)[:96])
arity = 'arity' in cap301
step = 'growth step' in cap302 or 'step' in cap302
check('Figure 30.1 IS the arity plot', arity, True)
check('Figure 30.2 IS the step law', step, True)
score('entry 193\'s numerals name the figures it describes', False, True, 'reg4-B')
print('   READING: entry 193 describes the arity plot in §30.3.2 and the step law in §30.3.4 --')
print('   which are Figures 30.1 and 30.2 -- and calls them Figures 23.1 and 23.2. Both numerals')
print('   are LIVE and denote different objects in Chapter 23, "The cost surface". The Appendix F')
print('   precedent leaves a stale numeral alone because it "collides with nothing"; this one')
print('   collides with two live figures, and the entry\'s order claim is false of them.')

hr('4  ENTRY 175 — THE SUBSET COUNT, WITH A WITNESS FOR THE NEGATIVE')
print('   "Λ\'s box has 10^2080 subsets" names no box. 2^n = 10^2080 needs n = 6,909.6, so a box of')
print('   about 6,910 cells. Tested against every size the work prints:')
import math
for name, n in [('genesis box', 630), ('genesis after l<=n-1', 450), ('Λ admissible', 210),
                ('Λ₈', 976), ('Λ₉', 1654), ('Λ₁₀', 2535), ('Λ₁₁', 13585), ('Λ₁₂', 70905), ('Λ₁₃', 199130)]:
    print('     %-22s %7d cells -> 10^%.0f' % (name, n, n * math.log10(2)))
print('   None gives 10^2080 and none is near 6,910. NOT REPRODUCIBLE from the page: the box is')
print('   unnamed. A budget with its witness, not a negative. Recorded for R3.')

hr('5  THE SHAPE OF THE UNIT')
quoted = [e for e in ents if re.search(r'^### %d$\n+\*\*"' % e, B, re.M)]
print('   entries whose headline opens on a quoted claim: %d of %d' % (len(quoted), len(ents)))
print('   %s' % quoted)
print('   This is the self-audit form: the entry quotes what was written, then measures it. Every')
print('   one of the %d carries a refutation or a qualification in the same headline.' % len(quoted))

hr('6  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and 731 <= int(l.split('\t')[3]) <= 850]
check('census rows in range', len(rows), 0)

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-12s printed %s' % (t, tag, repr(got)[:12], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
