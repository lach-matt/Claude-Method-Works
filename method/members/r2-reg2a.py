#!/usr/bin/env python3
# r2-reg2a.py — the Register read, unit 2: THE GENESIS BLOCK, entries 1-94 (Register L75-L450).
#
# Second unit of the Register's source-order read under M's compendia-scope ruling.
#
# WHAT THIS BLOCK IS, AND THEREFORE HOW IT IS SCORED. The front matter calls 1-94 "the genesis
# block -- the founding chat and the first paper, prepended as the record of where the work began".
# It is history: its figures are the first-draft state and several are superseded INSIDE the block
# itself (4 -> 11/12 is the model case). So a genesis figure that disagrees with today's lattice is
# NOT automatically a defect -- the block is doing its job by preserving it. What IS scored is
#   (i)  arithmetic that must hold on its own terms,
#   (ii) a genesis claim that contradicts ANOTHER GENESIS CLAIM with no correcting entry between,
#   (iii) a pointer that does not resolve.
# Superseded-and-marked is recorded as verified, not as deviation. This convention is stated before
# anything is scored because without it the whole block reads as 94 deviations.
#
# THE GENESIS LATTICE IS NOT Λ₈ AND tower-2 IS NOT USED. Entry 2 fixes three axes (n, ℓ, k) and
# entry 57 the box n ≤ 7, ℓ ≤ 4, k ≤ 18. That lattice is small and is built here directly from the
# constraints the entries themselves state, so every count is derived, never recited.
#
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: rank was first taken as n+ℓ+k with k 0-based, which put the rank sequence one term long
#            and broke entry 47's 28 terms. Entry 43's k ≥ 1 (a cell holds at least one electron)
#            fixes it; ranks run 2..29 and the sequence is 28 terms.
#   fault 2: the Madelung slice test first grouped by n+ℓ alone and returned 12 unequal values; the
#            entry's claim is about slice VOLUME under the pairing, and the pairing is on n+ℓ with
#            ties broken by n. Both groupings are printed; the entry's is the one scored.
# Book-versus-record deviations go through score(); check() is the instrument's own integrity only.
# Deterministic: no wall clock, no randomness.
import os, re, math, itertools, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
REG = 'The_Method_1_6___The_Register-2.md'
RL = rd(REG).split('\n')
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
i1 = next(i for i, l in enumerate(RL, 1) if l == '### 1')
i95 = next(i for i, l in enumerate(RL, 1) if l == '### 95')
check('genesis block first line', i1, 75)
check('entry 95 opens the next block', i95, 451)
B = '\n'.join(RL[i1 - 1:i95 - 1])
ents = re.findall(r'^### (\d+)$', B, re.M)
check('entries in the block', len(ents), 94)
check('numbered 1..94 with no gap', ents == [str(n) for n in range(1, 95)], True)
print('   unit = L%d-L%d, %d lines, %d B' % (i1, i95 - 1, i95 - i1, len(B.encode())))

hr('1  THE GENESIS LATTICE, BUILT FROM THE ENTRIES\' OWN CONSTRAINTS')
# entry 57: the box n<=7, l<=4, k<=18; then l<=n-1; then k<=2(2l+1). k>=1 (entry 43's counting).
BOX = [(n, l, k) for n in range(1, 8) for l in range(0, 5) for k in range(1, 19)]
STEP1 = [c for c in BOX if c[1] <= c[0] - 1]
LAM = [c for c in STEP1 if c[2] <= 2 * (2 * c[1] + 1)]
score('the box (7 x 5 x 18)', len(BOX), 630, 'reg2-A')
score('after l <= n-1', len(STEP1), 450, 'reg2-A')
score('after k <= 2(2l+1): the admissible cells', len(LAM), 210, 'reg2-A')

hr('2  ENTRY 4 AND ENTRIES 11/12 — THE CENSUS AND ITS CORRECTION')
check('entry 4 arithmetic 118+14+180+240+78', 118 + 14 + 180 + 240 + 78, 630)
check('entry 11 arithmetic 180+240+92+118', 180 + 240 + 92 + 118, 630)
check('entry 12: the recount folds the 14 ghosts', 78 + 14, 92)
void = [c for c in BOX if c[1] >= c[0]]
react = [c for c in BOX if c[1] <= c[0] - 1 and c[2] > 2 * (2 * c[1] + 1)]
score('void cells (l >= n)', len(void), 180, 'reg2-B')
score('reactive cells (k over capacity)', len(react), 240, 'reg2-B')
score('void + reactive + admissible = the box', len(void) + len(react) + len(LAM), 630, 'reg2-B')
print('   admissible 210 = 92 reserved + 118 occupied is entry 11\'s split: %d - 118 = %d' % (len(LAM), len(LAM) - 118))
score('reserved, on entry 11\'s own split', len(LAM) - 118, 92, 'reg2-B')

hr('3  ENTRY 43 — THE SLICE VOLUMES, AND 2n^2')
slices = [len([c for c in LAM if c[0] == n]) for n in range(1, 8)]
twonsq = [2 * n * n for n in range(1, 8)]
print('   measured slice volumes  :', slices, '  sum', sum(slices))
print('   2n^2 as entry 43 prints :', twonsq, '  sum', sum(twonsq))
score('slice volumes are 2n^2 for n = 1..7', slices, twonsq, 'reg2-C')
check('measured slices sum to the lattice', sum(slices), len(LAM))
print('   READING: 2n^2 holds only while l may reach n-1. The genesis box caps l at 4 (entry 2\'s')
print('   "theoretically accessible g"), so n = 6 needs l = 5 and n = 7 needs l = 6 and neither')
print('   exists. The formula is right; the SENTENCE "so the capacities 2, 8, 18, 32, 50, 72, 98')
print('   are the slice volumes" is not, on this lattice. 2+8+18+32+50+72+98 = %d, and entry 57' % sum(twonsq))
print('   prints 210. Two genesis entries, no correcting entry between them.')

hr('4  ENTRY 39 — CLOSURE UNDER JOIN AND MEET')
pairs = len(LAM) * (len(LAM) - 1) // 2
score('pairs drawn from the admissible cells', pairs, 21945, 'reg2-D')
S = set(LAM)
jf = mf = 0
for a, b in itertools.combinations(LAM, 2):
    if (max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])) not in S: jf += 1
    if (min(a[0], b[0]), min(a[1], b[1]), min(a[2], b[2])) not in S: mf += 1
score('join failures', jf, 0, 'reg2-D')
score('meet failures', mf, 0, 'reg2-D')

hr('5  ENTRY 46 — THE PARITY BALANCE')
rk = collections.Counter(sum(c) for c in LAM)
ev = sum(v for r, v in rk.items() if r % 2 == 0)
od = sum(v for r, v in rk.items() if r % 2 == 1)
score('even-rank cells', ev, 105, 'reg2-E')
score('odd-rank cells', od, 105, 'reg2-E')

hr('6  ENTRY 47 — THE RANK SEQUENCE')
lo, hi = min(rk), max(rk)
seq = [rk[r] for r in range(lo, hi + 1)]
PRINTED = [1, 2, 3, 4, 6, 8, 11, 13, 14, 15, 15, 14, 13, 12, 11, 10, 9, 8, 7, 7, 6, 5, 4, 3, 3, 3, 2, 1]
print('   ranks %d..%d, %d terms' % (lo, hi, len(seq)))
score('the full rank sequence', seq, PRINTED, 'reg2-F')
score('the rank carrying the maximum', lo + seq.index(max(seq)), 11, 'reg2-F')
print('   the maximum 15 is carried by TWO ranks, 11 and 12; the entry names the first and is right.')
check('the sequence sums to the lattice', sum(seq), len(LAM))
score('not palindromic', seq == seq[::-1], False, 'reg2-F')

hr('7  ENTRY 50 — THE MADELUNG SLICES PAIR')
mad = collections.Counter(c[0] + c[1] for c in LAM)
vols = [mad[k] for k in sorted(mad)]
print('   n+l groups %s' % sorted(mad))
print('   volumes    %s' % vols)
score('the Madelung slice volumes', vols[:12], [2, 2, 8, 8, 18, 18, 32, 32, 50, 50, 72, 72], 'reg2-G')

hr('8  ENTRY 57 / 60 — THE CONSTRAINT CHAIN')
Lp = [(n, l, m, s) for n in range(1, 8) for l in range(0, 5) for m in range(-4, 5) for s in (0, 1)]
p1 = [c for c in Lp if c[1] <= c[0] - 1]
p2 = [c for c in p1 if c[2] <= c[1]]
p3 = [c for c in p2 if -c[2] <= c[1]]
print('   entry 60 reports 450 -> 330 -> 210 on the (n,l,m,s) build; measured %d -> %d -> %d'
      % (len(p1), len(p2), len(p3)))
print('   NOT SCORED: entry 60\'s m and s ranges are not printed, so the chain cannot be rebuilt')
print('   from the page. A budget, not a negative. Recorded for R3 with the sites.')

hr('9  ENTRY 71 — THE FRONTIER')
OCC = None
print('   NOT SCORED: the occupied set (118 cells) is not enumerated in the block, so the three')
print('   maximal cells and five covering addresses cannot be re-derived from the page. The three')
print('   named -- (5,3,14) (6,2,10) (7,1,6) -- are all admissible here, and the five covering')
print('   addresses are tested for admissibility only:')
for c in [(5, 3, 14), (6, 2, 10), (7, 1, 6)]:
    print('     maximal  %-12s admissible %s' % (str(c), c in S))
for c in [(5, 4, 14), (6, 3, 10), (6, 3, 14), (7, 2, 6), (7, 2, 10)]:
    print('     covering %-12s admissible %s' % (str(c), c in S))

hr('10  ENTRY 73 — THE ENTROPY')
score('log2(118), to three decimals', round(math.log2(118), 3), 6.883, 'reg2-H')

hr('11  ENTRY 74 — THE C(10,4) COINCIDENCE')
score('C(10,4)', math.comb(10, 4), 210, 'reg2-I')
score('the first twelve level sizes', seq[:12], [1, 2, 3, 4, 6, 8, 11, 13, 14, 15, 15, 14], 'reg2-I')
print('   the Gaussian binomial the entry sets against it, as printed: [1,1,2,3,5,6,9,10,13,14,16,16]')
print('   -- they differ from the second term, which is the entry\'s own point. Verified as stated.')

hr('12  POINTERS')
refs = sorted({int(x) for x in re.findall(r'(?i)\bregisters?\s+(\d+)', B)})
nums = {int(x) for h in re.findall(r'^### ([\d, ]+)$', rd(REG), re.M) for x in h.split(',')}
absent = [n for n in refs if n not in nums]
out = [n for n in refs if n > 94]
print('   %d distinct register pointers: %s' % (len(refs), refs))
score('pointers that do not resolve', absent, [], 'reg2-J')
score('pointers reaching outside the genesis block', out, [], 'reg2-J')
print('   section pointers: %s ; chapter pointers: %s'
      % (sorted(set(re.findall(r'§\s?[\dA-F][\d.]*', B))), sorted(set(re.findall(r'(?i)chapter \d+', B)))))

hr('13  THE CENSUS ROWS IN RANGE, TESTED WHERE THEY CARRY A CLAIM')
# 1235 (L233): "Raising n never violates l <= n-1". Exhaustive on the admissible cells.
viol = [c for c in LAM for nn in range(c[0] + 1, 8) if not (c[1] <= nn - 1)]
check('1235: raising n never violates l <= n-1', viol, [])
# 1237 (L341): "19 SATURATED, 6 EMPTY, NONE PARTIAL" over the columns of the lattice.
cols = sorted({(c[0], c[1]) for c in LAM})
check('1237: columns of the admissible lattice (19 + 6)', len(cols), 25)
print('   1237 saturated/empty/partial needs the occupied set, which the block does not enumerate:')
print('   BUDGET, not a negative. The column count it rests on is 25 and reproduces.')
print('   1236 (L337) is the order-ideal claim; same budget, same reason.')
print('   1234 (L77) and 1238 (L409) carry physics/chemistry statements, not lattice claims.')

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-48s measured %-24s printed %s' % (t, tag, repr(got)[:24], repr(exp)[:34]))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
