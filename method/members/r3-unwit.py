#!/usr/bin/env python3
"""r3-unwit.py — R3: law · physics recorded as unwitnessed. BUILD97 -> BUILD98 main.

M's ruling: A. The fibre's closure is recorded as what it measures as, in the vocabulary M built
for exactly this shape at BUILD95 — proved and exhaustive over what it holds, wanting a witness and
nothing else. Nothing is promoted, re-fibred or reordered to make it close.

MEASURED (DEF-153I, K, L, M), at BUILD97 under §D.2's declared value orders:
  - 23 of 24 fibres close. law · physics stands at E = 3.
  - The whole defect is one element: without the observability boundary the fibre closes;
    without any other element it does not move.
  - With the boundary's verification exhaustive, one want remains, and it differs from the cell
    the fibre already holds (LS.law, proved · exhaustive · none found) on PRECEDENT alone.
    Precedent is the witness in this index (M's ruling; §D.5.2). So: unwitnessed.
  - The witness it wants is one the book's thesis says cannot exist: a precedent found for the
    ordering law would mean the Löwdin challenge had been answered before Chapter 35.
  - No ordering of §D.2's three axes closes the appendix: 0 of 8,640 (DEF-153K).
  - Re-fibring the boundary closes all 24 only into eight fibres it does not belong to; the one
    defensible home, measurement · physics, gives E = 2 (DEF-153M). §D.5.5's own warning.

FOUR SITES:
  1. §D.5's fibre census, the law · physics row: E printed 0, measured 3.
  2. §D.5.10's sum: "E = 0" -> "E = 0 in twenty-three of them".
  3. §D.5.10's caption on the observability boundary — this also repairs DEF-153H item 1, the
     regression r3-vocab left at BUILD95: the caption still called the boundary "the second element
     to enter as conjectured" after its row had moved to verified · sampled · found on M's ruling
     (register 1802), and its closure argument was computed from coordinates the row no longer
     carried. Rewritten to state the measured closure and the fibre's status.
  4. Register entry 1806.

NOT DONE, recorded: the census column headed `cells` counts ELEMENTS (theorem · order prints 21;
that fibre holds 5 cells). A mislabel of long standing and not this class. And the census's
theorem · physics E = 0 was false from register 1460 until BUILD97 and is true now; left as printed.

Grammar: §D.2 defines `status` for an element. This entry uses the word `unwitnessed` of a fibre's
closure in prose, and adds no column and no value — M's ruling A, taken at its narrowest.

Line shift: main +9 below §D.5.10 (the caption and the sum grow), reported not hidden. Register +4.

Usage:  python3 r3-unwit.py            dry run
        python3 r3-unwit.py --write    writes staging members + the BUILD98 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD97_main_and_register.md')
OLD_MD5 = '8e2ab973ecf7c5dbef0b922b30d22fef'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD98_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build98') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')

SUBS = [
 # 1. the census row — E measured 3
 ('  law · physics                                                                           4           0\n',
  '  law · physics                                                                           4           3\n'),
 # 2. the sum
 (' **Sixty-five elements become seventy-seven over twenty-four fibres, and E = 0 — after the index named\n'
  ' one cell and the cell was filled by reading one entry honestly.** Two fibres open for the first time,\n',
  ' **Sixty-five elements become seventy-seven over twenty-four fibres, and E = 0 in twenty-three of\n'
  ' them — after the index named one cell and the cell was filled by reading one entry honestly.** Two\n'
  ' fibres open for the first time,\n'),
 # 3. the caption
 (" The observability boundary is the second element to enter as *conjectured* (§D.5.7's slack = kernel\n"
  " was the first): one confirming instance, falsifiable, tested once — the compendium says so in those\n"
  " words, and *conjectured · sampled* is what those words are. Law · physics now holds four elements over\n"
  " three cells and closes; the box it spans admits *conjectured · exhaustive* and *proved · sampled*, and\n"
  " §6.1's bounds exclude both, which is the closure doing its work rather than the count.\n",
  " The observability boundary entered as *conjectured* and does not stay there. Its two halves are the\n"
  " literature's and the boundary between them is this work's, and outside attribution is what witness\n"
  " means in this index, so it stands *verified · sampled · found* (register 1802). Law · physics now\n"
  " holds four elements over three cells **and does not close: E = 3.** The whole of that is the one\n"
  " element — without the boundary the fibre closes, without any other it does not move. What the\n"
  " closure admits and nothing holds is *proved · exhaustive · found*, against the ordering law's\n"
  " *proved · exhaustive · none found*: the same status, the same verification, wanting a witness and\n"
  " nothing else. That is §D.2's sixth value read of a fibre rather than a row — **law · physics is\n"
  " unwitnessed.** And the witness it wants is one this book's thesis says cannot exist, since a\n"
  " precedent found for the ordering law would mean the Löwdin challenge had been answered before\n"
  " Chapter 35. The mechanical routes were measured and refused: no ordering of §D.2's three axes\n"
  " closes the appendix, 0 of 8,640, and re-fibring the boundary closes it only into fibres it does\n"
  " not belong to (register 1806).\n"),
]
for i, (o, n) in enumerate(SUBS, 1):
    c = m.count(o); print('site %d: anchor occurs %d time(s)' % (i, c)); assert c == 1
    m = m.replace(o, n)

# the census column: E must still sit under the header's E
_h = m[m.index('  fibre') : m.index('\n', m.index('  fibre'))]
_hdr_line = next(l for l in m.split('\n') if l.startswith('  fibre') and l.rstrip().endswith('E'))
_row = next(l for l in m.split('\n') if l.startswith('  law · physics') and l.rstrip().endswith('3') and '·' in l and 'exhaustive' not in l)
assert _row.rstrip().rindex('3') == _hdr_line.rstrip().rindex('E'), 'E column misaligned'
print('census E column preserved at col %d' % _hdr_line.rstrip().rindex('E'))

E1806 = """

### 1806

**LAW · PHYSICS IS UNWITNESSED, AND THE APPENDIX SAYS SO INSTEAD OF SAYING IT CLOSES.** *At BUILD97 Appendix D closed in twenty-three of twenty-four fibres, and the one open fibre was law · physics at E = 3. M's ruling, A of five: record the fibre's closure as what it measures as, in the vocabulary built at register 1801 for this shape, and promote, re-fibre or reorder nothing. Measured first. The whole defect is one element — without the observability boundary the fibre closes at E = 0, without any other of its four it does not move. With the boundary's verification exhaustive one want remains, and it differs from the cell the fibre already holds, the ordering law at proved · exhaustive · none found, on PRECEDENT alone: the same status, the same verification, a witness and nothing else. Precedent is the witness in this index (register 1802; §D.5.2), so the fibre is proved and exhaustive over what it holds and wanting only observation, which is §D.2's sixth value word for word.* **AND THE WITNESS IT WANTS IS ONE THIS BOOK'S THESIS SAYS CANNOT EXIST. The only proved element in the fibre is the ordering law, and a precedent found for it would mean the Löwdin challenge had been answered before Chapter 35 — which is the claim Chapter 35 exists to deny. Closing the fibre through that cell would falsify the achievement it indexes.** *The mechanical routes were run and refused. All 6! × 3! × 2! = 8,640 orderings of §D.2's three axes were swept with ℛ imported from cypher.py: 1,440 close both fibres that were open at BUILD96 and NONE closes the appendix, every one breaking a fibre that closes today. The boundary was moved to each of the other twenty-three fibres: eight close all twenty-four and not one is a home for it, while the one defensible home — measurement · physics, since §D.5.10 describes the boundary as a survey of eleven indexes returning nine of eleven — gives E = 2. That is §D.5.5's warning instantiated, and the section's own governing claim, that E falls as the fibration is refined, is false at seventy-seven elements: one fibre 4, language 6, kind 9, kind × language 5.* **Four sites: the census row (E printed 0, measured 3); §D.5.10's sum; §D.5.10's caption, which also repairs the regression the sixth-value build left there — it still called the boundary the second element to enter as conjectured after register 1802 had moved its row, and argued a closure from coordinates the row no longer carried; and this entry.** *Left as printed and recorded: the census column headed `cells` counts elements. §D.2 defines status for an element; this entry uses the word of a fibre's closure in prose and adds no column and no value.* Registers 1460; 1734; 1801; 1802; 1805. (a correction.)"""

assert r.count('### 1806') == 0; assert r.rstrip().endswith('(a correction.)')
r = r.rstrip() + E1806 + '\n'

for probe, want in (('second element to enter as *conjectured*', 0),
                    ('three cells and closes', 0),
                    ('law · physics is\n unwitnessed', 1),
                    ('E = 0 in twenty-three of', 1)):
    got = m.count(probe); print('  main after: %-44s %d (want %d)' % (repr(probe)[:44], got, want)); assert got == want

new_m = m.encode('utf-8'); new_r = r.encode('utf-8')
print('main %d -> %d B, lines %+d' % (len(old_main), len(new_m), m.count('\n') - old_main.decode('utf-8').count('\n')))
print('reg  %d -> %d B, lines %+d' % (len(old_reg), len(new_r), r.count('\n') - old_reg.decode('utf-8').count('\n')))

src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, old_main.decode('utf-8'), m), (REG, old_reg.decode('utf-8'), r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved)); assert not moved

if WRITE:
    assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT):
    os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m); open(OUT + REG, 'wb').write(new_r)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD97 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(old_b))
assert ms[MAIN] == old_main and ms[REG] == old_reg
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
nb = old_b
for n_, body in ((MAIN, new_m), (REG, new_r)):
    ob = block(n_, ms[n_]); assert nb.count(ob) == 1; nb = nb.replace(ob, block(n_, body))
rv = nb
for n_, body in ((MAIN, new_m), (REG, new_r)):
    assert rv.count(block(n_, body)) == 1; rv = rv.replace(block(n_, body), block(n_, ms[n_]))
assert md5(rv) == OLD_MD5, 'bundle reverse FAILED'
print('bundle reverse recovers md5 %s == old: True' % md5(rv))
print('new BUILD98  %s B  md5 %s  %s lines  %d members' % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE); open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE)
else:
    print('DRY RUN — nothing installed')
