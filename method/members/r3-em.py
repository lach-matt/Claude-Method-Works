#!/usr/bin/env python3
# r3-em.py — R3 CLASS: THE SPLIT-EMPHASIS CLASS (reg7-01 / reg7-02). SPECIFICATION AND DRY RUN.
#
# NOTHING HERE IS APPLIED. This instrument computes the repair, asserts it site by site, measures
# what the repaired member would be, and proves the reverse guard recovers the seated bytes. It
# writes no file and changes no member. It is the r3-wl.py model: the withdrawn-law class was
# specified, dry-run and banked at chat 128 and HELD for R3, and M's chat-128 ruling puts prose
# after the mathematics, so this class waits behind the same gate. The chat-67 hold stands.
#
# THE DEFECT. 275 entries carry "X* *Y": a bold "**" split so one asterisk attached to the preceding
# word and one to the following. Inside an italic body a single-asterisk pair cannot nest -- it
# CLOSES the body and opens a new italic -- so the sub-phrase the author marked renders as more
# continuous italic and the distinction is not on the page. Where the split also makes the line's
# asterisk total odd, a literal asterisk survives into print.
#
# THE REPAIR RULE, STATED BEFORE IT IS APPLIED. For an entry whose body is a single italic run:
# split the body's interior on the split sites; the segments alternate body / emphasis, beginning
# with body; re-emit each emphasis segment as **bold**, which is the only nesting Markdown allows
# inside an italic run, and rejoin with single spaces. The headline is never touched.
#
# WHAT THE RULE MAY NOT DO, AND DOES NOT. It declines any entry whose body is not one clean italic
# run -- 18 of the 275 -- because there the segments do not alternate and the rule would corrupt
# correct markup. Those go to R3 by hand, with both texts, and are listed here. A repair that cannot
# state which sites it is sure of is not a repair.
# FAULT SELF-CAUGHT BY THE REVERSE GUARD, AND IT IS THE REASON THE GUARD EXISTS. An earlier draft
# READ each body at RL[pos+1] and WROTE the repair to NL[pos] -- one line up, the blank line. The
# "repaired" member duplicated every body onto the blank above it (+195,358 B) and left the originals
# untouched, and reversing the substitutions did not recover the seated md5. Nothing was written,
# because this instrument writes nothing; the guard failed the run and the fault was found in the
# dry run rather than in a build. Read and write must use one index.
# Deterministic: no wall clock, no randomness.
import os, re, hashlib

H = os.path.dirname(os.path.abspath(__file__))
REG = 'The_Method_1_6___The_Register-2.md'
raw = open(os.path.join(H, REG), 'rb').read()
T = raw.decode('utf-8'); RL = T.split('\n')
def hr(t): print('\n== ' + t)
FAIL = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-56s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)

SPLIT = re.compile(r'(?<![*\s])\* \*(?!\*)')
pos = {}
for i, l in enumerate(RL, 1):
    m = re.match(r'^### ([\d, ]+)$', l)
    if m: pos.setdefault(m.group(1), i)
key = lambda h: int(h.split(',')[0])

def repair(line):
    m = re.match(r'^(\*\*.*?\*\*)(.*)$', line)
    if not m: return None, 'no bold headline'
    head, rest = m.group(1), m.group(2).strip()
    if not (rest.startswith('*') and rest.endswith('*') and not rest.startswith('**')):
        return None, 'body is not one clean italic run'
    segs = SPLIT.split(rest[1:-1])
    if len(segs) < 2: return None, 'no interior split site'
    return head + ' *' + ' '.join(('**%s**' % s) if k % 2 else s for k, s in enumerate(segs)) + '*', 'ok'

hr('0  THE SEATED MEMBER')
print('   %s  %d B  md5 %s  %d lines' % (REG, len(raw), hashlib.md5(raw).hexdigest(), T.count('\n')))

hr('1  THE CLASS')
affected = sorted([h for h in pos if SPLIT.search(RL[pos[h] + 1])], key=key)
sites = sum(len(SPLIT.findall(RL[pos[h] + 1])) for h in affected)
check('entries carrying the split', len(affected), 275)
check('split sites', sites, 429)
odd = [h for h in affected if RL[pos[h] + 1].count('*') % 2]
check('of those, leaving a literal asterisk in print', len(odd), 11)
print('   %s' % odd)

hr('2  THE SUBSTITUTIONS, COUNT-ASSERTED SITE BY SITE')
subs, decline = {}, {}
for h in affected:
    line = RL[pos[h] + 1]
    new, why = repair(line)
    if new is None: decline[h] = why; continue
    before, after = SPLIT.findall(line), SPLIT.findall(new)
    if after: decline[h] = 'split survived the repair'; continue
    if new.count('*') % 2: decline[h] = 'repair leaves an odd total'; continue
    subs[h] = (line, new)
check('entries the rule repairs', len(subs), 246)
check('entries the rule declines', len(decline), 29)
check('no repaired line still carries a split site',
      [h for h, (o, n) in subs.items() if SPLIT.search(n)], [])
check('every repaired line closes its own emphasis',
      [h for h, (o, n) in subs.items() if n.count('*') % 2], [])
print('   declined, and why: %s' % sorted(set(decline.values())))
print('   declined entries: %s' % sorted(decline, key=key))

hr('3  THE REPAIRED MEMBER, MEASURED (NOT WRITTEN)')
NL = list(RL)
for h, (o, n) in subs.items(): NL[pos[h] + 1] = n
new_text = '\n'.join(NL); new_raw = new_text.encode('utf-8')
print('   would become %d B  md5 %s  %d lines' % (len(new_raw), hashlib.md5(new_raw).hexdigest(), new_text.count('\n')))
print('   delta %+d B, %+d lines' % (len(new_raw) - len(raw), new_text.count('\n') - T.count('\n')))
check('line count unchanged', new_text.count('\n'), T.count('\n'))
check('only the %d repaired lines differ' % len(subs),
      sum(1 for a, b in zip(RL, NL) if a != b), len(subs))

hr('4  THE REVERSE GUARD')
BACK = list(NL)
for h, (o, n) in subs.items(): BACK[pos[h] + 1] = o
back_raw = '\n'.join(BACK).encode('utf-8')
check('reversing every substitution recovers the seated bytes',
      hashlib.md5(back_raw).hexdigest(), hashlib.md5(raw).hexdigest())

hr('5  WHAT R3 MUST DO BEYOND THIS INSTRUMENT')
print('   1. The 29 declined entries are repaired by hand, with both texts, not by this rule.')
print('   2. The change is a volume change, so under "no silent change" it needs a Register entry')
print('      in the same build recording it -- and the entry that records the FORM (1725) does not')
print('      exist (reg1-05), so the form has no seated statement to cite.')
print('   3. RUL-128 item 1 puts the mathematics first and the prose after it. This class is prose.')
print('   4. It runs through close.py with the member and bundle reverse guards, never in place.')

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   APPLIED: NOTHING. This is a specification and a dry run.')
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
