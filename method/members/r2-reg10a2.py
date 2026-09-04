#!/usr/bin/env python3
# r2-reg10a.py — the Register read, unit 10: entries 327-361 AND the seven grouped headings
# (Register L1211-L1346).
#
# The unit is 136 lines rather than the usual 120 because the seven grouped fault headings stand
# between entries 361 and 362 and are read WITH the entry that precedes them. The chat-81 cadence
# does not split a section read, and the grouped block is one object: splitting it would leave a
# heading in one unit and its mechanism in the next.
#
# WHAT THIS UNIT CAN RE-DERIVE. Entries 334 and 336 state information-theoretic figures about the
# tower that follow from the seated cell counts alone, so they are recomputed here rather than
# carried. Neither needs an instrument that is not already a member.
# Deterministic: no wall clock, no randomness.
# r2-reg10a2.py — R3 (W-218) — SUCCESSOR to r2-reg10a.py, the positional class on the REGISTER (W-207 / DEF-153N): the unit's
# self-check pinned its opening line as a literal, and its census filter used the same literals; register 1816's two table rows
# moved every Register line below L37 by two. Each literal is now the line its entry heading is at, found by its own text
# (`_R`); the unit's bounds were already scanned by content. Proved byte-exact against r2-reg10a.out on the BUILD102 tree.
# The census rows are still keyed to BUILD188 lines (DEF-153O: a content-keyed census is owed); no row lies within two
# lines of a unit bound at this build, so the selection is unchanged. r2-reg10a is seated and never edited in place (chat 68).

# --- re-anchoring helper (R3, W-218): a Register line found by its own heading text, never by a number ---
def _R(t):
    import os as _o
    global _RM
    try: _RM
    except NameError: _RM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6___The_Register-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_RM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: heading is not unique or is absent', t, h)
    return h[0]
import os, re, math

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
R = rd('The_Method_1_6___The_Register-2.md'); RL = R.split('\n')
M = rd('The_Method_1_6-2.md'); ML = M.split('\n')
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
a = next(i for i, l in enumerate(RL, 1) if l == '### 327')
b = next(i for i, l in enumerate(RL, 1) if l == '### 362')
check('unit opens at entry 327', a, _R('### 327'))
check('entry 362 opens the next unit', b, _R('### 362'))
B = '\n'.join(RL[a - 1:b - 1])
bare = [int(x) for x in re.findall(r'^### (\d+)$', B, re.M)]
grp = re.findall(r'^### (\d+(?:\s*,\s*\d+)+)$', B, re.M)
print('   unit = L%d-L%d, %d lines; %d bare entries %d..%d; %d grouped headings'
      % (a, b - 1, b - a, len(bare), bare[0], bare[-1], len(grp)))
check('the grouped block is whole in this unit', len(grp), 7)

hr('1  THE GROUPED BLOCK, AND THE MECHANISM EACH HEADING NAMES')
gpos = [i for i, l in enumerate(RL, 1) if re.match(r'^### \d+(?:\s*,\s*\d+)+$', l)]
check('all seven stand after entry 361', all(p > next(i for i, l in enumerate(RL, 1) if l == '### 361') for p in gpos), True)
nums = sorted(int(x) for g in grp for x in g.split(','))
check('numbers the seven headings hold', len(nums), 32)
check('their range', (min(nums), max(nums)), (203, 354))
secs = []
for p in gpos:
    body = RL[p + 1]
    m = re.match(r'^\*\*(§(\d+\.\d+) — )?(.*?)\*\*', body)
    s = m.group(2) if m and m.group(2) else None
    secs.append(s)
    print('   L%-5d %-10s %s' % (p, s or '(unnumbered)', re.sub(r'\s+', ' ', body)[:78]))
named = [s for s in secs if s]
print('   five headings name a §4.x mechanism: %s' % named)
print('   two name a mechanism without a §4.x number.')
for s in named:
    hit = [i for i, l in enumerate(ML, 1) if re.match(r'^\s*%s[ .]' % re.escape(s), l)]
    print('   %-6s located in the volume at %s' % (s, hit[:1] or 'NO LIST ITEM'))
print('   §4.x are Chapter 4\'s list items and not headings (MAIN_AUDIT V1, re-measured at the')
print('   sweep), so they are located as items, never by the heading resolver.')

hr('2  ENTRY 334 — Λ₁₃ AS A CHAIN OF 44 RANK VALUES, RE-DERIVED')
tower = {int(k): int(v) for k, v in re.findall(r'\|Λ(\d+)\| = (\d+)', rd('tower-2.out'))}
n13 = tower[13]
check('tower-2 prints Λ₁₃', n13, 199130)
tot, ch = math.log2(n13), math.log2(44)
print('   log2(%d) = %.4f ; log2(44) = %.4f' % (n13, tot, ch))
score('bits lost per cell, to two decimals', round(tot - ch, 2), 12.14, 'reg10-A')
score('percentage surviving, to the unit', round(100 * ch / tot), 31, 'reg10-A')

hr('3  ENTRY 336 — WHAT Λ REFUSES')
score('refused fraction of the ambient box, to one decimal',
      round(100 * (1 - 976 / 6912), 1), 85.9, 'reg10-B')
print('   1 - 976/6,912 = %.4f. The ambient box is the figure three entries corroborate'
      % (1 - 976 / 6912))
print('   (248, 255, genesis 8) and which unit 6 verified through its own printed ratio.')

hr('4  SECTION POINTERS')
for s in sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)', B)), key=lambda x: [int(y) for y in x.split('.')]):
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)[ \t]+(\S.*)$' % re.escape(s))
    hit = [(i, m.group(1)) for i, l in enumerate(ML, 1) if (m := p.match(l))]
    if hit:
        print('   §%-8s L%-6d %s' % (s, hit[0][0], hit[0][1][:52]))
    elif re.match(r'^4\.\d+$', s):
        print('   §%-8s Chapter 4 list item (not a heading) — MAIN_AUDIT V1' % s)
    else:
        print('   §%-8s ABSENT' % s); DEV.append(('reg10-C', '§%s absent' % s, None, True))

hr('5  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and _R('### 327') <= int(l.split('\t')[3]) <= _R('### 362') - 1]
print('   census rows in range: %d' % len(rows))
for l in rows: print('     %s' % l[:145])

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-12s printed %s' % (t, tag, repr(got)[:12], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
