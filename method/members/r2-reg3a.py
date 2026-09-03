#!/usr/bin/env python3
# r2-reg3a.py — the Register read, unit 3: THE SUPERSEDED BLOCK, entries 95-164 (Register L451-L730).
#
# Third unit of the Register's source-order read under M's compendia-scope ruling.
#
# THE HYPOTHESIS THIS UNIT OPENED WITH WAS WRONG, AND IT IS RECORDED AS WRONG. Seventy entries carry
# a supersession stub and no content. Read against the front matter's own discipline -- "A correction
# never replaces what it corrects. Both states are kept ... a register that tidied itself would be
# evidence of nothing" -- and against the standing rule that entries are append-only and a superseded
# entry keeps both states, that looks like seventy deletions. It is not. Under the chat-95 ruling the
# Prints & Proofs witness is searched BEFORE the question is asked, and it answers it: the PP Register
# (96b5fc2a, 1,145,832 B) runs 165 to 1700 and contains NO entry below 165. Entries 1-164 were
# PREPENDED after the witness, so 95-164 were created as markers and never held content in this
# volume. Nothing was deleted. The finding is about the reconstruction (G0c), and the reconstruction
# was mine.
#
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: the deletion hypothesis above, formed before the witness was read. Recorded, not hidden:
#            it is the reason PP is searched first and not after.
#   fault 2: the PP witness was first looked for in PP_The_Method_1_6.md, which is the MAIN volume and
#            carries no register entries at all (0 headings for 95, 120, 164, 313). The Register's own
#            witness is a separate file in the mirror. A negative from the wrong file is not a
#            negative.
# Deterministic: no wall clock, no randomness.
import os, re, hashlib, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
REG = 'The_Method_1_6___The_Register-2.md'
T = rd(REG); RL = T.split('\n')
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-58s %-28s %s' % (tag, repr(got)[:28], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, printed, tagno):
    ok = got == printed
    print('   %-58s %-28s %s' % (tag, repr(got)[:28], 'as printed' if ok else 'DEVIATION (%s) - printed %s' % (tagno, repr(printed))))
    if not ok: DEV.append((tagno, tag, got, printed))

hr('0  THE UNIT, BOUNDED BY ITS OWN SCAN')
i95 = next(i for i, l in enumerate(RL, 1) if l == '### 95')
i165 = next(i for i, l in enumerate(RL, 1) if l == '### 165')
check('block opens at entry 95', i95, 451)
check('entry 165 opens the mature record', i165, 731)
B = RL[i95 - 1:i165 - 1]
ents = re.findall(r'^### (\d+)$', '\n'.join(B), re.M)
check('entries in the block', len(ents), 70)
check('numbered 95..164 with no gap', ents == [str(n) for n in range(95, 165)], True)
print('   unit = L%d-L%d, %d lines' % (i95, i165 - 1, i165 - i95))

hr('1  UNIFORMITY, MEASURED RATHER THAN SAMPLED')
bodies = collections.Counter(l.strip() for l in B if l.startswith('**'))
check('distinct body lines in seventy entries', len(bodies), 1)
body, n = bodies.most_common(1)[0]
check('that body appears once per entry', n, 70)
print('   the single body: %s' % body)
other = [l for l in B if l.strip() and not l.startswith('### ') and not l.startswith('**')]
check('any other non-empty content', other, [])

hr('2  THE PRINTS & PROOFS WITNESS (Ruling 56), WHICH SETTLES THE UNIT')
PPR = os.path.join(os.path.dirname(H), '..', 'drive', 'The Method Prints & Proofs',
                   'The Method 1.6 — The Register.md')
if not os.path.exists(PPR):
    PPR = '/home/user/Claude-Method-Works/drive/The Method Prints & Proofs/The Method 1.6 — The Register.md'
pb = open(PPR, 'rb').read(); P = pb.decode('utf-8')
print('   PP Register %d B  md5 %s' % (len(pb), hashlib.md5(pb).hexdigest()))
pn = sorted({int(x) for h in re.findall(r'^### ([\d, ]+)$', P, re.M) for x in h.split(',')})
check('PP Register lowest entry', min(pn), 165)
check('PP Register highest entry', max(pn), 1700)
check('PP entries below 165', [n for n in pn if n < 165], [])
print('   PP holds %d headings / %d numbers; the seated Register holds 1,635 / 1,660.' % (
    len(re.findall(r'^### [\d, ]+$', P, re.M)), len(pn)))
print('   READING: entries 1-164 are POST-WITNESS. The superseded block was created as markers,')
print('   not emptied of content. The append-only rule is not engaged and nothing was deleted.')

hr('3  THE TARGET ENTRY 313')
i313 = next(i for i, l in enumerate(RL, 1) if l == '### 313')
line = RL[i313 + 1]
check('register 313 exists', i313 > 0, True)
print('   L%d: %s' % (i313 + 2, line[:150]))
# settled form: a bold capitalised headline, then the body in italics (front matter).
m = re.match(r'^\*\*([^*]+)\*\*\s*\*(.*)\*$', line)
score('entry 313 parses as headline + italic body', bool(m), True, 'reg3-A')
stray = line.count('*')
print('   asterisks on the line: %d ; a clean "**head** *body*" carries 4' % stray)
print('   the headline reads "TIME MUST NOT ENTER Λ*" -- the emphasis marker stands where the')
print('   quotation closes; the body then opens "*, refuted by computation" with a leading comma,')
print('   and carries "is* *iterate**" mid-sentence. The emphasis is scrambled, not merely odd.')

hr('4  THE CITATION DIRECTION, AND WHAT THE LOAD-BEARING TABLE CANNOT SEE')
ent = re.split(r'\n### (\d+(?:, \d+)*)\n', T)
inc = exc = 0
for i in range(1, len(ent), 2):
    ids = {int(x) for x in ent[i].split(', ')}
    k = len(re.findall(r'(?i)\bregisters?\s+313\b', ent[i + 1]))
    inc += k
    if not (ids and min(ids) >= 95 and max(ids) <= 164): exc += k
check('313 cited by entries, counting all entries', inc, 71)
check('313 cited, with 95-164 dropped (the convention)', exc, 1)
back = re.findall(r'(?i)\bregisters?\s+(\d+)', ent[ent.index('313') + 1]) if '313' in ent else []
print('   entries 313 itself cites: %s' % (back or 'none'))
print('   READING: the link is ONE-WAY. The standing rule words it the other way -- "a superseded')
print('   entry is corrected by a new entry that cites it" -- and 313 cites none of the seventy.')
print('   At 71 citations 313 is the most-cited entry in the volume, and it appears nowhere in the')
print('   load-bearing table, because register_cites.py drops 95-164. The exclusion is the chat-52')
print('   ruling and is correct; the table\'s own sentence does not state it.')

hr('5  THE FRONT MATTER\'S CLAIM ABOUT THIS BLOCK')
print('   "entries 95 to 164 are the superseded Λ₈ successor-development stretch, each marking the')
print('   later entry that supersedes it"')
check('every entry marks a later entry', all('register 313' in l for l in B if l.startswith('**')), True)
check('313 is later than every entry in the block', 313 > 164, True)
check('all seventy mark the SAME entry', len(bodies), 1)
print('   Exact as printed. "Each marking the later entry" is true of every one; measured, they all')
print('   mark one entry, which the sentence permits and does not state.')

hr('6  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and 451 <= int(l.split('\t')[3]) <= 730]
check('census rows in range', len(rows), 0)
print('   No row engages the block. CENSUS-CLOSURES-reg3.tsv is header-only.')

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-14s printed %s' % (t, tag, repr(got)[:14], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
