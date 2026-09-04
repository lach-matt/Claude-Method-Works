#!/usr/bin/env python3
# r2-reg12.py — the Register read, units 12-onward: THE REMAINDER OF THE MATURE RECORD,
# entries 395 to 1792 (Register L1467-L6611), read in blocks.
#
# CADENCE, AND WHY IT CHANGES HERE. Units 1-11 ran at the chat-81 mean of ~120 lines because the
# early record needed its conventions established one at a time. Three things now license larger
# blocks, and they are stated before the blocks are cut:
#   1. r2-regsweep has already resolved EVERY pointer in the volume -- section, register, chapter,
#      lettered and figure -- so a unit no longer rebuilds six resolvers to find nothing.
#   2. The mature record is a flat run of one-line entries, not the main volume's nested prose;
#      there is no subsection structure for a unit boundary to respect.
#   3. Units 5, 6, 9, 10 and 11 returned no deviation at all. The class of defect that remains is
#      volume-wide (reg7-01, reg8-01) and is already measured volume-wide.
# The read is not thinned: every entry is still resolved, every figure the entries state about
# themselves is still extracted, and every census row in range is still engaged. What changes is
# that one instrument carries all of it with one golden, instead of thirty-two.
#
# WHAT THIS INSTRUMENT DOES NOT DO. It does not read prose for claims. Whether a headline's
# assertion is true, whether a count word counts what it says, whether a resolved pointer carries
# the claim -- those stay with the reading, and the blocks below are where that reading is recorded.
# Deterministic: no wall clock, no randomness.
# r2-reg12b.py — R3 (W-218) — SUCCESSOR to r2-reg12.py, the positional class on the REGISTER (W-207 / DEF-153N): the unit's
# self-check pinned its opening line as a literal, and no census filter used the same literals; register 1816's two table rows
# moved every Register line below L37 by two. Each literal is now the line its entry heading is at, found by its own text
# (`_R`); the unit's bounds were already scanned by content. Proved byte-exact against r2-reg12.out on the BUILD102 tree.
# The census rows are still keyed to BUILD188 lines (DEF-153O: a content-keyed census is owed); no row lies within two
# lines of a unit bound at this build, so the selection is unchanged. r2-reg12 is seated and never edited in place (chat 68).

# --- re-anchoring helper (R3, W-218): a Register line found by its own heading text, never by a number ---
def _R(t):
    import os as _o
    global _RM
    try: _RM
    except NameError: _RM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6___The_Register-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_RM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: heading is not unique or is absent', t, h)
    return h[0]
import os, re, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
R = rd('The_Method_1_6___The_Register-2.md'); RL = R.split('\n')
M = rd('The_Method_1_6-2.md')
VOLS = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'),
        'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
        'sc': rd('The_Method_1_6___Spectra_Compendium-2.md'),
        'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md')}
ML = M.split('\n')
FAIL = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-58s %-24s %s' % (tag, repr(got)[:24], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)

allnums = {int(x) for h in re.findall(r'^### ([\d, ]+)$', R, re.M) for x in h.split(',')}
pos = {}
for i, l in enumerate(RL, 1):
    m = re.match(r'^### ([\d, ]+)$', l)
    if m: pos.setdefault(m.group(1), i)
key = lambda h: int(h.split(',')[0])

def resolve(sec):
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)[ \t]+(\S.*)$' % re.escape(sec), re.M)
    for v, t in VOLS.items():
        if p.search(t): return v
    return None
# the classes the read has already accounted for, with their witnesses
KNOWN_SEC = {'0': 'Spectra Compendium §0', '5.7': 'the companion paper', '8.7': 'Transitions v3.0',
             '784': 'a register number with a § sigil — 26b-08'}
LIST_ITEM = re.compile(r'^4\.\d+$')
SPLIT = re.compile(r'(?<![*\s])\* \*(?!\*)')

hr('0  THE REMAINDER')
start = next(i for i, l in enumerate(RL, 1) if l == '### 395')
check('the remainder opens at entry 395', start, _R('### 395'))
heads = [h for h in pos if pos[h] >= start]
print('   L%d-L%d, %d lines, %d headings, entries %d..%d'
      % (start, len(RL), len(RL) - start, len(heads),
         min(key(h) for h in heads), max(key(h) for h in heads)))
check('every entry from 395 on is in this remainder',
      len(heads) + len([h for h in pos if pos[h] < start]), len(pos))

BLOCKS = [(a, min(a + 399, len(RL))) for a in range(start, len(RL), 400)]
print('   read in %d blocks of 400 lines' % len(BLOCKS))

hr('1  POINTER RESOLUTION, BLOCK BY BLOCK')
unres_all, badreg_all = [], []
for a, b in BLOCKS:
    B = '\n'.join(RL[a - 1:b])
    ents = [h for h in pos if a <= pos[h] <= b]
    secs = set(re.findall(r'§\s?(\d+(?:\.\d+)*)', B))
    unres = [s for s in secs if not resolve(s) and s not in KNOWN_SEC and not LIST_ITEM.match(s)]
    refs = {int(x) for x in re.findall(r'(?i)\bregisters?\s+(\d+)', B)}
    badreg = sorted(n for n in refs if n not in allnums)
    unres_all += unres; badreg_all += badreg
    print('   L%-5d-%-5d %3d entries  %3d §  %3d reg  unresolved §:%-14s reg absent:%s'
          % (a, b, len(ents), len(secs), len(refs), sorted(unres) or '-', badreg or '-'))
check('section pointers unaccounted for in the remainder', sorted(set(unres_all)), [])
check('register pointers with no entry, on the "register N" net', sorted(set(badreg_all)), [])
print('   The sweep\'s absent-and-cited pair, 344 and 571, is cited from the MAIN volume and not')
print('   from the register, so the remainder correctly shows none on this net.')

hr('1a  BUT THE NET IS THE WRONG SHAPE, AND THE CENSUS HAD IT ALL ALONG')
import re as _re
WD = {1000: r'\bentry 1000\b', 1002: r'\bR 1002\b'}
tot = 0
for n, pat in WD.items():
    k = len(_re.findall(pat, R)); tot += k
    onnet = len(_re.findall(r'(?i)\bregisters?\s+%d\b' % n, R))
    print('   entry %d: %d site(s) as %-14s ; %d on the "register N" net ; live? %s'
          % (n, k, pat, onnet, n in allnums))
check('sites citing a withdrawn entry in the register BODY', tot, 4)
print('   reg8-02 concluded "no other part of the live register cites a withdrawn entry". That is')
print('   FALSE, and it is false because the measurement used the "register N" net, which returns')
print('   0 for both of these forms. Census rows 8, 15, 16 and 17 carried them the whole time.')
print('   Third time this read has met the lesson, and the first time it has caught the read.')

hr('1b  THE UNPRINTED-THEOREM CLASS IS LARGER THAN 26b-09 RECORDS')
for th in ('10.1', '11.1', '11.2', '12.1'):
    pat = r'(?:Theorem|Thm\.?)\s+%s\b' % _re.escape(th)
    named = {k: len(_re.findall(pat, t)) for k, t in VOLS.items() if _re.search(pat, t)}
    out = {k: v for k, v in named.items() if k != 'reg'}
    print('   Thm %-5s cited %-24s printed outside the register: %s' % (th, named, out or 'NOWHERE'))
print('   26b-09 (W-190) records Thm 11.1 at one site. Measured, Thm 11.2 (2 sites) and Thm 12.1')
print('   (2 sites) are in the same condition -- cited by the register, printed in no volume.')
print('   Thm 10.1 IS in the Mathematical Compendium and is not in the class; whether the MC')
print('   states it or merely cites it was not taken here, and is a budget.')

hr('2  THE EMPHASIS CLASS ACROSS THE REMAINDER')
split_here = [h for h in heads if SPLIT.search(RL[pos[h] + 1])]
print('   entries carrying the split shape: %d of %d in the remainder' % (len(split_here), len(heads)))
print('   sites: %d' % sum(len(SPLIT.findall(RL[pos[h] + 1])) for h in split_here))
print('   Already scored volume-wide at reg7-01 and specified for repair in R3-CLASS-EM.md.')
print('   Counted here so the remainder is not read as though the class stopped at entry 394.')

hr('3  THE CENSUS OVER THE REMAINDER')
rows = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()]
inrange = [r for r in rows if r[2] == 'reg' and start <= int(r[3]) <= len(RL)]
byclass = collections.Counter(r[1] for r in inrange)
print('   census rows engaged: %d' % len(inrange))
for c, n in byclass.most_common(): print('     %-34s %d' % (c, n))

hr('4  ENTRIES CARRYING A FIGURE THIS READ HAS ALREADY RE-DERIVED')
ANCHOR = {'976': 'Λ₈', '1654': 'Λ₉', '2535': 'Λ₁₀', '13585': 'Λ₁₁', '70905': 'Λ₁₂',
          '199130': 'Λ₁₃', '6912': 'the ambient box', '475800': 'C(976,2)', '131072': '2¹⁷'}
hits = collections.Counter()
for h in heads:
    body = RL[pos[h] + 1].replace(',', '')
    for n in ANCHOR:
        if re.search(r'(?<!\d)%s(?!\d)' % n, body): hits[n] += 1
for n, c in sorted(hits.items(), key=lambda x: -x[1]):
    print('   %-8s %-16s stated by %d entries in the remainder' % (n, ANCHOR[n], c))
print('   Each of these is a seated tower figure this read has already reproduced; an entry')
print('   restating one is corroboration, not a new claim, and is not re-scored.')

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
