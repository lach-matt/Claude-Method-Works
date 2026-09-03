#!/usr/bin/env python3
# r2-reg7a.py — the Register read, unit 7: THE EMPHASIS CLASS, taken out of source order at M's
# direction (entries 1642-1699 were flagged as a cluster by r2-regsweep; the read jumps to them and
# returns to entry 290 afterwards).
#
# THE CLUSTER IS NOT A CLUSTER. The sweep's odd-asterisk test flagged eleven entries between 1642
# and 1699 and that looked like one authoring session. Reading them shows the shape is "X* *Y" -- a
# bold "**" split so one asterisk attached to the preceding word and one to the following, which is
# exactly entry 313's "is* *iterate**" (reg3-01). Measured for that shape rather than for parity,
# the class holds 275 of 1,635 entries at 429 sites, spread from entry 238 to entry 1729. The
# cluster was an artefact of the parity test, not a property of the record.
#
# THE PARITY TEST WAS ALSO WRONG ABOUT WHICH ENTRIES ARE BROKEN. An asterisk is notation here --
# 2P* and 2P*<1/2> are odd-parity term symbols, phi* is Miedema's electronegativity parameter,
# "(3, 0, 1, 1, *, 0, 1, 1)" is a wildcard coordinate. Of the 22 entries with an odd total, 11 carry
# the split shape and 11 carry only notation. The sweep's "14 candidates" is superseded by this
# measurement: the true set is 11, and r2-regsweep's classifier was too narrow because it required a
# digit before the asterisk and so missed 2P*.
#
# WHAT IS SCORED, AND WHAT IS NOT. That the intended emphasis is LOST is measurable and is scored:
# a sub-phrase meant to stand out inside an italic body cannot be marked with single asterisks, and
# renders as continuous italic. That a LITERAL asterisk reaches the printed page is measurable only
# where the total is odd, and those eleven are scored separately. The cause is NOT claimed: the
# class is consistent with the ruling-C normalisation REGISTER_AUDIT R4 records, but that pass is
# recorded at entry 1725 and entry 1725 does not exist (reg1-05), so nothing seated attests it.
# FAULT SELF-CAUGHT: an earlier draft asserted the flagged band held 51 entries, a number nobody had
# measured, and the instrument failed its own integrity check on it. A check() takes a figure the
# record states or the instrument derives -- never one the author guessed.
# Deterministic: no wall clock, no randomness.
import os, re, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
T = rd('The_Method_1_6___The_Register-2.md'); RL = T.split('\n')
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-56s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def note(tagno, tag, got, printed):
    DEV.append((tagno, tag, got, printed))
    print('   %-56s %-26s FINDING (%s)' % (tag, repr(got)[:26], tagno))

pos = {}
for i, l in enumerate(RL, 1):
    m = re.match(r'^### ([\d, ]+)$', l)
    if m: pos.setdefault(m.group(1), i)
body = {h: RL[i + 1] for h, i in pos.items()}
key = lambda h: int(h.split(',')[0])

hr('0  THE UNIT, AND WHY IT IS OUT OF SOURCE ORDER')
print('   M directed the read to jump to the 1642-1699 cluster and return to entry 290 after it.')
print('   Recorded as a directed departure from the chat-81 source order, not a drift.')
print('   entries in the flagged band 1642..1699: %d (measured, not asserted -- an earlier draft'
      % len([h for h in pos if 1642 <= key(h) <= 1699]))
print('   of this instrument checked it against a guessed 51 and failed its own gate. Fault 1.)')

hr('1  THE SHAPE, MEASURED RATHER THAN THE PARITY')
SPLIT = re.compile(r'(?<![*\s])\* \*(?!\*)')
split_e = {h for h in pos if SPLIT.search(body[h])}
sites = sum(len(SPLIT.findall(body[h])) for h in split_e)
odd_e = {h for h in pos if body[h].count('*') % 2}
check('entries carrying the split shape "X* *Y"', len(split_e), 275)
check('sites', sites, 429)
check('entries with an odd asterisk total', len(odd_e), 22)
lo, hi = min(split_e, key=key), max(split_e, key=key)
note('reg7-A', 'the split class spans the record, %s to %s' % (lo, hi), len(split_e), 0)
print('   %.1f%% of the 1,635 entries. The 1642-1699 "cluster" holds %d of them.'
      % (100 * len(split_e) / len(pos), len([h for h in split_e if 1642 <= key(h) <= 1699])))

hr('2  THE TWO SUB-CLASSES')
both = sorted(odd_e & split_e, key=key)
nota = sorted(odd_e - split_e, key=key)
check('odd AND split: a literal asterisk must reach the page', len(both), 11)
check('odd but NOT split: notation, correct as printed', len(nota), 11)
note('reg7-B', 'entries leaving a literal asterisk on the page', len(both), 0)
print('   scored: %s' % both)
print('   acquitted as notation: %s' % nota)
print('   Entry 313 is the case confirmed by reading at reg3-01 and is in the scored set.')

hr('3  WHAT THE SHAPE COSTS, SHOWN FROM THE RECORD')
for h in ['289', '290', '238']:
    print('   entry %-4s %s' % (h, re.sub(r'\s+', ' ', body[h])[:150]))
print('   Each intends emphasis on a sub-phrase inside an italic body -- *fifteen*, *made* and')
print('   *selection*, *blocks: novelty* and *blocks: nothing*. Single asterisks cannot nest inside')
print('   an italic run: each pair CLOSES the body and opens a new italic, so the page shows one')
print('   continuous italic and the distinction the author made is not on it. The markup is not')
print('   merely untidy -- it is emphasis that does not arrive.')

hr('4  THE PASS THIS IS CONSISTENT WITH, AND WHY NOTHING ATTESTS IT')
print('   REGISTER_AUDIT R4: "Five forms of entry across the record ... Closed - ruling C. Every')
print('   entry normalised to the settled form (caps headline, italic body); tags removed; no')
print('   content changed. Recorded as entry 1725 with Register-1 named as the witness."')
check('entry 1725 exists', '1725' in pos, False)
print('   The pass that normalised every entry to the form this class disfigures is recorded at an')
print('   entry that is NOT IN THE REGISTER (reg1-05). Causation is NOT claimed here: what is')
print('   measured is a 275-entry class, a normalisation that matches its shape, and no seated')
print('   entry attesting the normalisation. R3 reads the three together.')

hr('5  SPREAD, SO THE CLASS IS NOT MISTAKEN FOR A CLUSTER AGAIN')
band = collections.Counter((key(h) // 200) * 200 for h in split_e)
for b in sorted(band):
    print('     %4d-%4d  %3d entries  %s' % (b, b + 199, band[b], '#' * band[b]))

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   findings recorded        : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-52s %s' % (t, tag, repr(got)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
