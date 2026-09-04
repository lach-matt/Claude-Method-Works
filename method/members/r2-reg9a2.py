#!/usr/bin/env python3
# r2-reg9a.py — the Register read, unit 9: entries 290-326 (Register L1091-L1210).
#
# Source order resumed after units 7 and 8, which M directed out of order. 120 lines, cut on an
# entry boundary at 326 (327 opens at L1211).
#
# FAULT SELF-CAUGHT AND NAMED, AND IT IS THE THIRD OF ITS KIND IN THIS READ. Entry 301 prints
# "(3,3,2,3) gives 1,548, and only (3,3,1,3) with k >= 1 gives 976". Rebuilding L8 from tower-2.py's
# own loops, (3,3,1,3) reproduced 976 exactly and (3,3,2,3) returned 1,284 -- and that was recorded
# as a deviation for as long as it took to search the cap space for 1,548. It is there, and the book
# is right: entry 301's tuple is (n, e, l, k) and does NOT carry f, and in tower-2.py the l and f
# caps are PARALLEL -- "min(1, n-1)" for l and "min(1, e-1)" for f, both hard-set to 1. Raising l to
# 2 raises f to 2 with it. Holding f at 1 while lifting l is an asymmetric change the book never
# made. Under the symmetric lift (3,3,2,3) gives 1,548 to the unit. Book right, instrument wrong.
# Deterministic: no wall clock, no randomness.
# r2-reg9a2.py — R3 (W-218) — SUCCESSOR to r2-reg9a.py, the positional class on the REGISTER (W-207 / DEF-153N): the unit's
# self-check pinned its opening line as a literal, and its census filter used the same literals; register 1816's two table rows
# moved every Register line below L37 by two. Each literal is now the line its entry heading is at, found by its own text
# (`_R`); the unit's bounds were already scanned by content. Proved byte-exact against r2-reg9a.out on the BUILD102 tree.
# The census rows are still keyed to BUILD188 lines (DEF-153O: a content-keyed census is owed); no row lies within two
# lines of a unit bound at this build, so the selection is unchanged. r2-reg9a is seated and never edited in place (chat 68).

# --- re-anchoring helper (R3, W-218): a Register line found by its own heading text, never by a number ---
def _R(t):
    import os as _o
    global _RM
    try: _RM
    except NameError: _RM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6___The_Register-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_RM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: heading is not unique or is absent', t, h)
    return h[0]
import os, re, itertools

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
a = next(i for i, l in enumerate(RL, 1) if l == '### 290')
b = next(i for i, l in enumerate(RL, 1) if l == '### 327')
check('unit opens at entry 290', a, _R('### 290'))
B = '\n'.join(RL[a - 1:b - 1])
ents = [int(x) for x in re.findall(r'^### (\d+)$', B, re.M)]
print('   unit = L%d-L%d, %d lines, entries %d..%d, %d headings' % (a, b - 1, b - a, ents[0], ents[-1], len(ents)))

hr('1  THE GAPS, CLASSIFIED AGAINST THE WHOLE REGISTER')
heads = re.findall(r'^### ([\d, ]+)$', R, re.M)
grouped = {int(x) for h in heads if not h.strip().isdigit() for x in h.split(',')}
allnums = {int(x) for h in heads for x in h.split(',')}
gaps = [n for n in range(290, 327) if n not in ents]
print('   gaps %s' % gaps)
print('   under a grouped heading : %s' % [n for n in gaps if n in grouped])
print('   absent entirely         : %s' % [n for n in gaps if n not in allnums])

hr('2  ENTRY 301 — THE CAPS, RE-DERIVED FROM tower-2.py\'s OWN LOOPS')
def L8(nmax, emax, lmax, kmax, fmax, kmin=1):
    out = 0
    for n in range(1, nmax + 1):
      for l in range(0, min(lmax, n - 1) + 1):
        for k in range(kmin, min(kmax, 4 * l + 2) + 1):
          for q in range(0, k + 1):
            for e in range(1, emax + 1):
              for f in range(0, min(fmax, e - 1) + 1):
                for g in range(0, min(4 * f + 2, q) + 1):
                  for _ in range(0, k + 1): out += 1
    return out
tower = int(re.search(r'\|Λ8\| = (\d+)', rd('tower-2.out')).group(1))
check('tower-2 prints Λ8', tower, 976)
score('(3,3,1,3) with k >= 1', L8(3, 3, 1, 3, 1), 976, 'reg9-A')
score('(3,3,2,3) under the SYMMETRIC l/f lift', L8(3, 3, 2, 3, 2), 1548, 'reg9-A')
print('   for the record, the asymmetric lift this instrument first took: (3,3,2,3) f held at 1 -> %d'
      % L8(3, 3, 2, 3, 1))
print('   and k >= 0 instead of k >= 1: (3,3,1,3) -> %d, which is entry 301\'s other half:'
      % L8(3, 3, 1, 3, 1, 0))
score('only k >= 1 gives 976', L8(3, 3, 1, 3, 1, 0) != 976, True, 'reg9-A')
print('   Both halves of entry 301 reproduce. The eighth condition it says the construction is')
print('   short of is k >= 1, and the caps that give 976 are the seated ones.')

hr('3  EVERY SECTION POINTER RESOLVED TO ITS HEADING AND ITS CLAIM')
WANT = {'2.19.1': '', '3.8': '', '4': 'failures of the assistant', '6.2': '', '8.3': 'generators',
        '12.5': '', '12.6': '', '18.4.1': '', '23.1': '', '28.7.4': 'Forty more'}
for s in sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)', B)), key=lambda x: [int(y) for y in x.split('.')]):
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)[ \t]+(\S.*)$' % re.escape(s))
    hit = [(i, m.group(1)) for i, l in enumerate(ML, 1) if (m := p.match(l))]
    if not hit:
        print('   §%-8s ABSENT' % s); DEV.append(('reg9-B', '§%s absent' % s, None, True)); continue
    i, h = hit[0]; w = WANT.get(s, '')
    ok = (not w) or w.lower() in h.lower()
    print('   §%-8s L%-6d %-46s %s' % (s, i, h[:46], '' if not w else ('carries the claim' if ok else 'CHECK')))
    if w and not ok: DEV.append(('reg9-B', '§%s claim' % s, h, w))

hr('4  ENTRY 315 — THE FILL, AND WHAT IS NOT ON THE PAGE')
print('   315: "E = 0 at every stage, and fill falling monotonically 14.12%% to ..."')
check('976 / 6,912 rounds to the 14.12% three entries state', round(100 * 976 / 6912, 2), 14.12)
print('   the rest of the fall needs the AMBIENT box at each stage; tower-2 prints the lattice')
print('   sizes only and no ambient. Budget with its witness, as at reg6 and unit 5. Docket 10.')

hr('5  REGISTER POINTERS IN THE UNIT')
for n in sorted({int(x) for x in re.findall(r'(?i)\bregisters?\s+(\d+)', B)}):
    print('   register %-5d exists %s' % (n, n in allnums))
    if n not in allnums: DEV.append(('reg9-C', 'register %d absent' % n, False, True))

hr('6  CENSUS')
rows = [l for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()
        and l.split('\t')[2] == 'reg' and _R('### 290') <= int(l.split('\t')[3]) <= _R('### 327') - 1]
print('   census rows in range: %d' % len(rows))
for l in rows: print('     %s' % l[:140])

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-50s measured %-12s printed %s' % (t, tag, repr(got)[:12], repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
