#!/usr/bin/env python3
# r2-25b.py — chat 148 (Cowork) — 25b-03 (DEF-143 item 11's fourth re-derivation; DEF-138 item 6; docket 34 / 12):
# Appendix E.8's *The cost is in Chapter 28. Sixty-odd corrections come from §30.3 alone.* against Chapter 28's own record.
# DEF-138 owed R3 a READING of §28.7.4's forty for their §30.3 share and recorded that a token probe is not one. The forty are
# entries 150-189: §28.7.4 prints the lead-ins for 150-164 only; 165-189 are printed in THE REGISTER, which is the source
# (register front matter: genesis 1-94, superseded 95-164, mature record 165-1792). DEF-147 item 6's convention — a closed
# item's inputs are searched in the whole volume AND the Register before they are called unprinted — therefore applies, and
# the forty ARE fully readable: 15 lead-ins in the chapter, 25 entry bodies in the Register. No budget is owed.
# Every count word in §28.7 and its subsections is censused against its DATA rows (chat-133 convention: fix the DATA-row set
# before scoring a count word). The §30.3 share is scored under four NAMED conventions, and every SUBJ verdict carries a
# deciding phrase that the instrument asserts is present in that entry's own text — the scoring is checkable against the file.
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness. Integers throughout; Decimal where
# a ratio is printed (never round()).
import os, re, sys, hashlib, importlib.util
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]

MAIN, REG = 'The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md'
M, R = rd(MAIN), rd(REG)

def rbody(n):   # copied verbatim from r2-24a.py (there from r2-23a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-24a.py (there from r2-23a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-24a.py (there from r2-23a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

def norm(s): return re.sub(r'\s+', ' ', s).strip()
FAIL = []; DEV = []
def check(tag, got, exp):   # instrument integrity: a mismatch is the instrument's fault and stops the run
    ok = got == exp
    print('   %-58s %-26s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):   # book against record: a mismatch is a FINDING, recorded, never a run failure
    ok = got == exp
    print('   %-58s %-26s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

print('r2-25b.py — 25b-03: E.8 "Sixty-odd corrections come from §30.3 alone" against Chapter 28')
print('members: %s md5 %s | %s md5 %s' % (MAIN, md5(MAIN), REG, md5(REG)))

# ---------------------------------------------------------------- §1 sites
print('\n§1 SITES (located this chat; member line numbers are never carried between chats)')
e8 = lettered(M, 'E.8')
print('   lettered("E.8") hits:', e8, '->', repr(norm(M[e8[-1] - 1])))
sent = [i for i, l in enumerate(M, 1) if re.search(r'Sixty-odd', l)]
check('E.8 sentence, one site', len(sent), 1)
SENT = sent[0]
print('   L%d %s' % (SENT, repr(norm(M[SENT - 1]))))
check('sentence inside E.8', e8[-1] < SENT < e8[-1] + 12, True)
print('   numeric resolver on "E.8":', r2lib.heading_line(M, 'E.8'), '— a lettered heading is invisible to it (DOCKET conventions)')

for sec in ('28.7', '28.7.1', '28.7.2', '28.7.3', '28.7.4', '28.7.5', '30.3', '30.4', '32.2'):
    hl = r2lib.heading_line(M, sec); br = body_range(M, sec); ss = r2lib.section_span(M, sec)
    print('   §%-7s heading_line %-6s body_range %-14s section_span %-14s %s'
          % (sec, hl, str(br), str(ss), 'AGREE' if br == ss else 'DIFFER — both reported'))

# ---------------------------------------------------------------- §2 census of §28.7.x count words
print('\n§2 CENSUS — every count word in §28.7 and its subsections against its DATA rows')
print('   (chat-133 convention: the DATA-row set is fixed before a count word is scored; a count word counts DATA rows)')
LEAD = re.compile(r'^\s*\**\s*(\d{1,3})(?:[–-](\d{1,3}))?\.\s')
WORD = {'six': 6, 'two': 2, 'eight': 8, 'twelve': 12, 'seventy-five': 75, 'forty': 40,
        'thirty-one': 31, 'ten': 10, 'seven': 7, 'five': 5, 'thirteen': 13, 'four': 4}
BOUND = [r2lib.heading_line(M, s) for s in ('28.7', '28.7.1', '28.7.2', '28.7.3', '28.7.4', '28.7.5')] + [r2lib.heading_line(M, '28.7.6')]
NAMES = ['28.7', '28.7.1', '28.7.2', '28.7.3', '28.7.4', '28.7.5']
BLOCK = {}
for nm, a, b in zip(NAMES, BOUND, BOUND[1:]):
    nums, rows = [], []
    for i in range(a, b):
        m = LEAD.match(M[i - 1])
        if m:
            lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
            rows.append((i, lo, hi)); nums += list(range(lo, hi + 1))
    dup = sorted(n for n, c in Counter(nums).items() if c > 1)
    span = set(range(min(nums), max(nums) + 1)) if nums else set()
    miss = sorted(span - set(nums))
    BLOCK[nm] = dict(rows=rows, nums=nums, span=span, miss=miss, dup=dup)
    print('   §%-7s L%-5d  lead-ins %2d  numbers %3d  distinct %3d  range %-10s dup %-6s unprinted-in-span %s'
          % (nm, a, len(rows), len(nums), len(set(nums)),
             ('%d-%d' % (min(nums), max(nums))) if nums else '-', dup or '-', miss or '-'))

# §28.7 — "Six made after the register was closed, two printed here"
h287 = norm(M[r2lib.heading_line(M, '28.7') - 1])
print('\n   §28.7 heading: %s' % repr(h287))
check('§28.7 "Six" vs distinct DATA rows', len(set(BLOCK['28.7']['nums'])), 6)
score('§28.7 "two printed here" vs lead-ins printed', len(BLOCK['28.7']['rows']), 2, '25b-07')
print('      -> 25b-07: the heading says *two printed here*; six lead-ins (49-54) are printed, and the block\'s own')
print('         closing line reads *Two of these six are corrections of corrections* — the count word does not count its rows.')

# §28.7.1 / §28.7.2
check('§28.7.1 "Eight more" vs distinct rows', len(set(BLOCK['28.7.1']['nums'])), 8)
score('§28.7.2 "Twelve more" vs distinct numbers in span', len(set(BLOCK['28.7.2']['nums'])), 12, '25b-09')
print('      -> 25b-09: §28.7.2 carries a SECOND entry numbered 59 (L%d), the number already used in §28.7.1 (L%d);'
      % ([i for i, lo, hi in BLOCK['28.7.2']['rows'] if lo == 59][0], [i for i, lo, hi in BLOCK['28.7.1']['rows'] if lo == 59][0]))
print('         §28.7.2\'s own block is 63-74 = 12 and the count word is right; the numeral is the defect (docket 31).')
for i, lo, hi in BLOCK['28.7.1']['rows']:
    if lo == 59: print('         §28.7.1 59: %s' % repr(norm(M[i - 1])[:96]))
for i, lo, hi in BLOCK['28.7.2']['rows']:
    if lo == 59: print('         §28.7.2 59: %s' % repr(norm(M[i - 1])[:96]))

# §28.7.3 — "Seventy-five more … all printed"
h3 = norm(M[r2lib.heading_line(M, '28.7.3') - 1])
print('\n   §28.7.3 heading: %s' % repr(h3))
check('§28.7.3 "Seventy-five" vs span 75-149', len(BLOCK['28.7.3']['span']), 75)
check('§28.7.3 distinct numbers actually printed', len(set(BLOCK['28.7.3']['nums'])), 63)
score('§28.7.3 "all printed" — numbers in span not printed', len(BLOCK['28.7.3']['miss']), 0, '25b-08')
print('      -> 25b-08: the count word counts the RANGE 75-149 (75), not the rows; 12 of the 75 are not printed')
print('         (%s) and 118 is printed twice — *all printed* is false at 63 of 75 (docket 34 / 31 / 23).'
      % ', '.join('%d-%d' % (g[0], g[-1]) for g in ([[99, 100, 101, 102, 103, 104, 105], [140, 141, 142, 143, 144]])))
d118 = [i for i, lo, hi in BLOCK['28.7.3']['rows'] if lo <= 118 <= hi]
print('         118 appears in lead-ins at L%s' % (', L'.join(str(i) for i in d118)))

# the seventeen, internally
sev = [i for i, lo, hi in BLOCK['28.7.3']['rows'] if (lo, hi) == (123, 139)]
check('§28.7.3 carries the 123-139 lead-in', len(sev), 1)
S17 = sev[0]
print('   L%d %s' % (S17, repr(norm(M[S17 - 1])[:150])))
tenof = [i for i in range(S17, S17 + 12) if 'Ten of the seventeen' in M[i - 1]]
check('*Ten of the seventeen* present', len(tenof), 1)
print('   L%d %s' % (tenof[0], repr(norm(M[tenof[0] - 1])[:120])))
check('ten + seven == seventeen', WORD['ten'] + WORD['seven'], 139 - 123 + 1)

# §28.7.5's own count words
a5, b5 = r2lib.heading_line(M, '28.7.5'), r2lib.heading_line(M, '28.7.6')
t5 = ' '.join(M[a5 - 1:b5 - 1])
check('§28.7.5 names *Thirty-one of the forty*', 'Thirty-one of the forty' in t5, True)
check('§28.7.5 names the two audit entries 186 and 189', bool(re.search(r'186 and 189', t5)), True)

# ---------------------------------------------------------------- §3 the DATA-row set of the forty
print('\n§3 THE FORTY — the DATA-row set fixed before any share is scored')
h4 = norm(M[r2lib.heading_line(M, '28.7.4') - 1])
print('   §28.7.4 heading: %s' % repr(h4))
check('§28.7.4 heading names §30.3 AND §32.2', sorted(set(re.findall(r'§\d+\.\d+', h4))), ['§30.3', '§32.2'])
FORTY = list(range(150, 190))
check('150-189 is forty', len(FORTY), WORD['forty'])
check('§28.7.5\'s 186 and 189 lie in 150-189', all(n in FORTY for n in (186, 189)), True)
inch = sorted(set(BLOCK['28.7.4']['nums']))
check('printed as lead-ins in §28.7.4', (min(inch), max(inch), len(inch)), (150, 164, 15))
IDX = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^###\s+(\d+)\s*$', l)
    if m: IDX[int(m.group(1))] = i
KS = sorted(IDX)
def rspan(n):
    s = IDX[n]; e = next(IDX[k] for k in KS if IDX[k] > s) - 1
    return norm(' '.join(x for x in R[s:e] if x.strip()))
heads = [n for n in FORTY if n in IDX]
check('of the forty, entry headings in the Register', len(heads), 38)
check('176 and 177 carry no heading (grouped under 175)', [n for n in FORTY if n not in IDX], [176, 177])
check('175 carries 176-177 in its body', '176' in rspan(175) and '177' in rspan(175), True)
sup = [n for n in FORTY if n in IDX and rspan(n).startswith('**SUPERSEDED')]
check('superseded band inside the forty', (min(sup), max(sup), len(sup)), (150, 164, 15))
print('   the Register\'s front matter: *genesis 1-94, superseded 95-164, mature record 165-1792* — 150-164 carry no')
print('   text of their own (all read **SUPERSEDED (Λ₈ successor development); see register 313.**), so for those fifteen')
print('   Chapter 28 is the only witness of what they were (25b-10, docket 17). 165-189 are read from the Register.')
check('DATA rows: 15 chapter lead-ins + 25 Register entries', 15 + 25, len(FORTY))

# ---------------------------------------------------------------- §4 the reading
print('\n§4 THE READING — each of the forty scored for its section, with the deciding phrase from its own text')
print('   CONVENTION SUBJ: an entry is §30.3\'s when its own text is about the objects §30.3 defines (§30.3.1-§30.3.9:')
print('   ℛ-closure / sublattice of chains, relabelling and order recovery, the alphabet, arity-2-SAT-linear-Schaefer,')
print('   PQ-trees / C1P / intervals, d = 2 against d ≥ 3, the procedure and its cost, the residue, and §30.3.1\'s named')
print('   sources Rival / Larson / Siggers); §32.2\'s when it is about self-reference (S1 alphabet, S2 order, S3 bounds,')
print('   P22, completeness); NEITHER when it is about another section or the audits; UNATTRIBUTED when its own text')
print('   decides neither. Every verdict\'s deciding phrase is asserted present in that entry below.')
CH28 = {150: 'cross-references to §24.4 for a theorem in §18.4', 151: 'cross-references to §24.4 for a theorem in §18.4',
        **{n: 'PQ-tree analogue' for n in range(152, 165)}}
SUBJ = [
    (150, 'CH', 'cross-references to §24.4', 'NEITHER', '§24.4 / §18.4 — a citation defect; see 186'),
    (151, 'CH', 'cross-references to §24.4', 'NEITHER', '§24.4 / §18.4 — a citation defect; see 186'),
    *[(n, 'CH', 'PQ-tree analogue', '30.3', '§30.3.3 — the interval machinery (C1P, monotone endpoints, PQ-trees)') for n in range(152, 165)],
    (165, 'RG', "fails to recover Λ's order", '30.3', 'order recovery'),
    (166, 'RG', 'ℛ recovers its alphabet', '30.3', '§30.3.1 — the closure operator and the moving ground set'),
    (167, 'RG', 'SELF-REFERENCE CLAIM', '32.2', '§32.2 — P22, completeness descends'),
    (168, 'RG', 'MONOTONE CLOSURE', '30.3', '§30.3.5 — what a procedure is'),
    (169, 'RG', 'ALPHABET OF SIZE 4', '30.3', 'the obstruction census by alphabet'),
    (170, 'RG', 'ALPHABET READING ITSELF', '30.3', 'the census parameterised by cells'),
    (171, 'RG', 'IDENTICAL-FIBRE QUOTIENT', '30.3', 'the quotient offered as a simplification'),
    (172, 'RG', 'THREE CELL STATISTICS', 'UNATT', 'statistics agreement — §30.2\'s landscape as readily as §30.3'),
    (173, 'RG', 'VIOLATED AT D ≥ 3', '30.3', 'exact at d = 2, violated at d ≥ 3'),
    (174, 'RG', 'SUBLATTICES PRESERVE REORDERABILITY', '30.3', 'reorderability, named'),
    (175, 'RG', 'COMPUTABLE', '30.3', 'the procedure\'s cost language'),
    (176, 'RG', 'recovered-versus-declared alphabet', '30.3', 'the d = 2 census and the d = 3 bound system'),
    (177, 'RG', 'recovered-versus-declared alphabet', '30.3', 'the d = 2 census and the d = 3 bound system'),
    (178, 'RG', 'D = 2 IS CLOSED', '30.3', "E.8's own *characterisation closed at d = 2*"),
    (179, 'RG', 'HIERARCHY CONVERGES', '30.3', 'the d = 3 / d = 4 columns'),
    (180, 'RG', 'non-reorderable 3-subset', '30.3', 'the sub-instance necessary condition'),
    (181, 'RG', 'VACUOUS DOWNSET TEST', '30.3', 'the downset test on observed classes'),
    (182, 'RG', 'MEDIANS ABOVE IT READ 36 AGAINST 72', 'UNATT', 'no section-identifying object in its own text'),
    (183, 'RG', 'LINEAR COVERAGE IS 9%', '30.3', "the law's linear regime"),
    (184, 'RG', 'Generation matched exhaustion', '30.3', 'the generator against exhaustion'),
    (185, 'RG', 'NO POLYNOMIAL PROCEDURE', '30.3', '§30.3.5 / §30.3.8 — the procedure and the residue'),
    (186, 'RG', 'COHERENCE audit', 'NEITHER', '§28.7.5 names 186 an entry about the audits'),
    (187, 'RG', 'NON-MONOTONE MAP', '30.3', 'the image of the map at d = 3, d = 4'),
    (188, 'RG', "Larson's correspondence", '30.3', "§30.3.1's named sources — Larson 1998, Siggers 2016"),
    (189, 'RG', 'VACUOUS AUDIT TEST', 'NEITHER', '§28.7.5 names 189 an entry about the audits'),
]
check('SUBJ scores every one of the forty once', sorted(n for n, *_ in SUBJ), FORTY)
CHTXT = ' '.join(M[r2lib.heading_line(M, '28.7.4') - 1:r2lib.heading_line(M, '28.7.5') - 1])
miss = []
for n, src, phrase, verdict, why in SUBJ:
    text = CHTXT if src == 'CH' else rspan(175 if n in (176, 177) else n)
    ok = phrase.lower() in norm(text).lower()
    if not ok: miss.append((n, phrase))
    print('   %3d %s  %-9s %-38s %s' % (n, src, verdict, '"' + phrase + '"', why))
check('every deciding phrase present in its own entry', miss, [])
share = Counter(v for _, _, _, v, _ in SUBJ)
print('   SUBJ over the forty: §30.3 %d | §32.2 %d | NEITHER %d | UNATTRIBUTED %d'
      % (share['30.3'], share['32.2'], share['NEITHER'], share['UNATT']))
check('SUBJ totals to forty', sum(share.values()), 40)

# ---------------------------------------------------------------- §5 the arithmetic
print('\n§5 THE ARITHMETIC — §30.3\'s share under four named conventions against *Sixty-odd*')
print('   CONVENTION BAND, two readings of the count word, both scored (INFERRED — an English count word, not a figure):')
print('     STRICT *sixty-odd* = 60-69 (sixty and some); LOOSE *sixty-odd* = about sixty, 55-65.')
print('   The blocks Chapter 28 attributes: 123-139 = 17, whose lead-in gives the corrections to *the')
print('   reorderability problem* of §30.3 and names §2.15 only as where ten of them are tabulated;')
print('   145-149 = 5 to Chapter 30 *against its own §30.4*; 150-189 = 40 to *the session that closed')
print('   §30.3 and §32.2*.')
CONV = [
    ('HEAD  §30.3 alone by heading attribution', 17, 'the seventeen only; the forty are a shared block'),
    ('BLOCK the whole shared forty given to §30.3', 17 + 40, "DEF-138's reading"),
    ('BLOCK+30.4 the forty and §30.4\'s five as well', 17 + 40 + 5, 'requires two other sections\' blocks'),
    ('SUBJ  the forty read entry by entry', 17 + share['30.3'], 'this chat\'s reading, §4 above'),
    ('SUBJ+ the two unattributed given to §30.3', 17 + share['30.3'] + share['UNATT'], 'the reading\'s upper bound'),
]
for nm, v, note in CONV:
    print('   %-46s %3d   STRICT %-8s LOOSE %-8s %s'
          % (nm, v, 'in' if 60 <= v <= 69 else 'outside', 'in' if 55 <= v <= 65 else 'outside', note))
inband = [nm for nm, v, _ in CONV if 60 <= v <= 69]
loose = [nm for nm, v, _ in CONV if 55 <= v <= 65]
check('conventions reproducing *Sixty-odd* STRICT', inband, ['BLOCK+30.4 the forty and §30.4\'s five as well'])
check('conventions reproducing *Sixty-odd* LOOSE', loose, ['BLOCK the whole shared forty given to §30.3',
                                                           'BLOCK+30.4 the forty and §30.4\'s five as well'])
print('   Under LOOSE the figure is reachable at 57 — but only by BLOCK, which gives §30.3 the whole of a block')
print('   the chapter itself shares with §32.2. Under every convention that respects *alone* the figure is')
print('   outside both bands. The word carrying the defect is *alone*, not *Sixty-odd*.')
hi = 17 + share['30.3'] + share['UNATT']
pct = (Decimal(share['30.3']) * 100 / Decimal(40)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
print('   %d of the forty are §30.3\'s under SUBJ = %s %% (Decimal.quantize, ROUND_HALF_UP; never round()).'
      % (share['30.3'], pct))

# ---------------------------------------------------------------- §6 the Register sweep
print('\n§6 REGISTER SWEEP — before any figure is called unreproducible')
w = [n for n in FORTY + list(range(123, 150)) + [313] if n in IDX and 'WARNING' in rspan(n).upper()]
check('WARNING lines on any entry of the family', w, [])
print('   WARNING lines in the Register at all: %d — none of them on this family (docket 35\'s instrument, run)'
      % sum(1 for l in R if 'WARNING' in l))
later = [(f, i, norm(l)[:90]) for f in (MAIN, REG) for i, l in enumerate(rd(f), 1)
         if re.search(r'[Ss]ixty[- ]odd', l)]
for f, i, l in later: print('   *sixty-odd* site: %s L%d %s' % (f, i, repr(l)))
check('*sixty-odd* sites in main + Register', len(later), 1)
cit = [n for n in FORTY if re.search(r'\bregister %d\b' % n, ' '.join(M), re.I)]
check('the forty cited as "register N" in the main volume', cit, [])
print('   E.8\'s sentence is a single witness (docket 17, already recorded) and no later statement in either volume')
print('   qualifies it; the figure is scored against Chapter 28, which E.8 itself names as the record.')

# ---------------------------------------------------------------- verdict
print('\nVERDICT')
print('   25b-03 CONFIRMED and NARROWED by reading, no budget owed. The forty ARE readable — fifteen lead-ins in')
print('   §28.7.4 and twenty-five entry bodies at Register 165-189 — so DEF-138\'s owed reading is DONE, and the')
print('   token probe it warned about is not what closed it. §30.3\'s share of the forty is %d of 40 (upper bound %d);'
      % (share['30.3'], share['30.3'] + share['UNATT']))
print('   with the seventeen of 123-139 that is %d (upper bound %d), against E.8\'s *Sixty-odd*. NO convention that'
      % (17 + share['30.3'], hi))
print('   respects *alone* reaches either band: the strict band is reached only by %d, which hands §30.3 both'
      % (17 + 40 + 5))
print('   §32.2\'s shared block and §30.4\'s five, and the loose band only by %d, which hands it the shared block'
      % (17 + 40))
print('   entire. The defective word is *alone*: §30.3\'s own share of the record is %d. 25b-03 stands as recorded,'
      % (17 + share['30.3']))
print('   now on a reading of all forty rather than an arithmetic of two headings (DEF-138 item 6 DISCHARGED).')
print('   New this unit: 25b-07 (§28.7 *two printed here*, six printed), 25b-08 (§28.7.3 *Seventy-five … all printed*,')
print('   63 of 75 printed, 12 unprinted, 118 twice), 25b-09 (a second entry numbered 59 in §28.7.2), 25b-10')
print('   (150-164 SUPERSEDED in the source Register — Chapter 28 is their single witness).')
print('\nDEVIATIONS RECORDED (findings, not instrument faults):')
for t, tag, got, exp in DEV: print('   %-8s %-56s measured %s against printed %s' % (t, tag, repr(got), repr(exp)))
print('\n%s' % ('FAIL: ' + '; '.join(FAIL) if FAIL else 'ALL INSTRUMENT CHECKS OK — %d deviations recorded' % len(DEV)))
sys.exit(1 if FAIL else 0)
