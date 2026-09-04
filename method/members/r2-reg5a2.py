#!/usr/bin/env python3
# r2-reg5a.py — the Register read, unit 5: entries 200-245 (Register L851-L970).
#
# Fifth unit of the Register's source-order read under M's compendia-scope ruling. 120 lines, thirty
# headings, cut on an entry boundary at 245 (246 opens at L971).
#
# THE GAP CONVENTION, FIXED BEFORE ANYTHING IS SCORED. Sixteen numbers between 200 and 245 carry no
# heading in this unit's line range, and reading that as sixteen absences would be wrong twice over.
# Twelve of them are printed later, under the seven grouped headings that stand between entries 361
# and 362 (the front matter's "thirty-two of the earliest fault entries, 203-354"). Only four are
# absent from the register entirely. Gaps are therefore classified against the WHOLE register, never
# against the unit's own span.
#
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: the section-pointer regex was first written to stop at the first dot, which turned
#            §25.6.3 into "25", §12.11.1 into "12" and so on, and would have reported five pointers
#            where the unit carries eight. A pointer regex must take the whole dotted numeral.
#   fault 2: A.2 was first "resolved" at main L8125, which is a reference to it inside §29.10, not
#            the appendix. Appendix subsections are plain-text labels rather than headings, so the
#            resolver must not treat the first textual hit as the target.
# Deterministic: no wall clock, no randomness.
# r2-reg5a2.py — R3 (W-218) — SUCCESSOR to r2-reg5a.py, the positional class on the REGISTER (W-207 / DEF-153N): the unit's
# self-check pinned its opening line as a literal, and its census filter used the same literals; register 1816's two table rows
# moved every Register line below L37 by two. Each literal is now the line its entry heading is at, found by its own text
# (`_R`); the unit's bounds were already scanned by content. Proved byte-exact against r2-reg5a.out on the BUILD102 tree.
# The census rows are still keyed to BUILD188 lines (DEF-153O: a content-keyed census is owed); no row lies within two
# lines of a unit bound at this build, so the selection is unchanged. r2-reg5a is seated and never edited in place (chat 68).

# --- re-anchoring helper (R3, W-218): a Register line found by its own heading text, never by a number ---
def _R(t):
    import os as _o
    global _RM
    try: _RM
    except NameError: _RM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6___The_Register-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_RM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: heading is not unique or is absent', t, h)
    return h[0]
import os, re

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
i200 = next(i for i, l in enumerate(RL, 1) if l == '### 200')
i246 = next(i for i, l in enumerate(RL, 1) if l == '### 246')
check('unit opens at entry 200', i200, _R('### 200'))
check('entry 246 opens the next unit', i246, _R('### 246'))
B = '\n'.join(RL[i200 - 1:i246 - 1])
ents = [int(x) for x in re.findall(r'^### (\d+)$', B, re.M)]
print('   unit = L%d-L%d, %d lines, entries %d..%d, %d headings'
      % (i200, i246 - 1, i246 - i200, ents[0], ents[-1], len(ents)))

hr('1  THE GAPS, CLASSIFIED AGAINST THE WHOLE REGISTER')
heads = re.findall(r'^### ([\d, ]+)$', T, re.M)
grouped = {int(x) for h in heads if not h.strip().isdigit() for x in h.split(',')}
allnums = {int(x) for h in heads for x in h.split(',')}
gaps = [n for n in range(200, 246) if n not in ents]
ing = [n for n in gaps if n in grouped]
miss = [n for n in gaps if n not in allnums]
check('gaps in the unit span', len(gaps), 16)
check('gaps printed under a grouped heading', ing,
      [203, 207, 209, 213, 215, 218, 219, 220, 221, 227, 231, 239])
check('gaps absent from the register entirely', miss, [202, 204, 206, 210])
print('   Register L6574 enumerates eleven numbers "in no group at all" BETWEEN 203 AND 354:')
print('   204, 206, 210, 260, 264, 269, 272, 287, 324, 341, 344. Three of this unit\'s four are')
print('   among them. 202 is below 203 and falls outside that enumeration\'s stated span.')
print('   With 196 and 199 from unit 4, three absent numbers are so far outside any enumeration.')

hr('2  EVERY SECTION POINTER RESOLVED TO ITS HEADING AND ITS CLAIM')
secs = sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)', B)))
check('section pointers in the unit', len(secs), 8)
WANT = {'12.11.1': 'axes', '12.11.2': '', '16.3.1': 'D1 tripwire', '25.6.3': 'not a prediction',
        '29.1': 'novelty', '29.10': 'searches run', '29.12': 'unlocated', '32.1.1': 'referee'}
for s in secs:
    p = re.compile(r'^#{2,6} %s(?!\d)(?!\.\d)\s+(.*)$' % re.escape(s))
    hit = [(i, m.group(1)) for i, l in enumerate(ML, 1) if (m := p.match(l))]
    if not hit:
        print('   §%-9s ABSENT' % s); DEV.append(('reg5-A', '§%s absent' % s, None, True)); continue
    i, h = hit[0]
    want = WANT.get(s, '')
    ok = (not want) or want.lower() in h.lower()
    print('   §%-9s L%-6d %-50s %s' % (s, i, h[:50], 'carries the claim' if ok else 'HEADING ONLY'))
    if not ok: DEV.append(('reg5-A', '§%s does not carry the claim' % s, h, want))

hr('3  THE LETTERED POINTERS')
print('   Appendix subsections are plain-text labels, not headings (MAIN_AUDIT V11), so each is')
print('   located in Appendix A / E by its label line, never by the first textual hit.')
appA = next(i for i, l in enumerate(ML, 1) if re.match(r'^#{1,2} Appendix A', l) and i > 9000)
for lab in ['A.2', 'A.5']:
    hit = [i for i, l in enumerate(ML, 1) if i > appA and re.match(r'^\s*%s\s' % re.escape(lab), l)]
    print('   %-5s in Appendix A (from L%d): %s' % (lab, appA, hit[:1] or 'ABSENT'))
    if not hit: DEV.append(('reg5-B', '%s absent in Appendix A' % lab, None, True))
e41 = [i for i, l in enumerate(ML, 1) if l.startswith('### E.4.1')]
check('E.4.1 has a heading of its own', bool(e41), True)
print('   E.4.1 L%d: %s' % (e41[0], ML[e41[0] - 1]))

hr('4  ARITHMETIC THAT MUST HOLD ON ITS OWN TERMS')
check('234: one well + three partly + three not at all = seven flags', 1 + 3 + 3, 7)
check('229: four passed + consistency + redundancy = the six-audit pass', 4 + 2, 6)
d233 = [4, 3, 2, 0]
check('233: E falls monotonically as the fibration refines', d233 == sorted(d233, reverse=True), True)
d241 = [64.4, 64.5, 65.7, 66.1]
check('241: the density rises with the caps', d241 == sorted(d241), True)
check('241: every value stays below the nominal two-thirds', all(x < 200 / 3 for x in d241), True)
print('   241 approaches 66.667 from below and does not reach it: %s' % d241)
check('242: 150 rejected of 216 offered leaves 66 admitted', 216 - 150, 66)

hr('5  ENTRY 236 — THE CELL COUNTS, WITH A WITNESS FOR THE NEGATIVE')
tower = dict(re.findall(r'\|Λ(\d+)\| = (\d+)', rd('tower-2.out')))
print('   tower-2 prints: %s' % {('Λ' + k): int(v) for k, v in tower.items()})
for n in (8853, 89438, 267858, 499246):
    print('     entry 236\'s %-7d appears in the tower: %s' % (n, str(n) in tower.values()))
print('   NOT REPRODUCIBLE from the page: 236 states E(Λ) = 0 "through the F shell" at four cell')
print('   counts, and names no caps. tower-2 rebuilds at the seated caps only and none of the four')
print('   is among Λ₈..Λ₁₃. A budget with its witness, not a negative. Docket 10.')

hr('6  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and _R('### 200') <= int(l.split('\t')[3]) <= _R('### 246') - 1]
check('census rows in range', len(rows), 0)

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-12s printed %s' % (t, tag, repr(got)[:12], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
