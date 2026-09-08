#!/usr/bin/env python3
# r2-bib3.py — R4 — SUCCESSOR to r2-bib2.py after register 1891 removed six generated bibliography rows.
# r2-bib2 is seated and never edited in place (chat 68); it is superseded, not withdrawn, and it was HELD in the
# live set (W-308) with this file as the successor it was owed.
#
# WHY IT WAS HELD RATHER THAN RE-BANKED. r2-bib2 pins "the table prints 162 data rows, as the volume states"
# as an INTEGRITY check and EXITS NONZERO on it, so the gate reports ERROR rather than a diff. A re-bank runs
# the instrument; running one that reports its own pinned figure as failed would bank that failure as the record.
#
# TWO CHECKS MOVE, AND THE SECOND IS THE ONE WORTH READING.
#   162 -> 156. Register 1891 removed five rows the generator had made by pairing a real author with a
#   neighbouring citation's year, and merged one work that had been printed as two rows.
#
#   "EVERY ONE OF THE 286 LINES STILL CARRIES ITS HANDLE" WAS A UNIVERSAL AND IS NOW A SPLIT. Seven of the 286
#   census rows were retired at W-307 on M's ruling, because the lines they sat on no longer exist: ids 431
#   (`L.def`), 493 (`L.bits`), 534 (`Q.delta`), 553 (`G.book`), 609 (`T.trad`), and 646 and 649 (`A.orient`,
#   `T.tight`, on the Hentenryck row the merge absorbed). This successor asserts the split rather than the
#   universal: EXACTLY those seven carry the RETIRED mark, and ALL 279 others still point at a line that
#   carries the handle. A universal that has one exception is worth less than a split that names it.
#
# AND THE FINDING THE PREDECESSOR RECORDED IS UNCHANGED. bib-01 stands: the `objects` column prints handles a
# reader cannot follow to an object the volume states, and the repair is the generator's, which is not held as
# a member. Register 1891 removed rows whose (name, year) no object attributes; it did not touch the handles.
#
# --- r2-bib2.py's own header, carried verbatim ---
# r2-bib2.py — R3 (W-223) — SUCCESSOR to r2-bib.py, the constant-carrying class (DEF-151r3 item 5): three of the census
# reading's own measured figures — handles resolving nowhere 93, only outside the compendium 86, rows resolving nowhere
# 133 — were pinned as checks, and registers 1824 and 1825, which name K.peak and K.deadend, moved them by one and
# made the instrument exit 1. The successor prints the three as measurements beside the closing reading's figures
# and changes nothing else; on the BUILD104 tree its output differs from r2-bib.out in exactly those three lines and
# the integrity summary. r2-bib is seated and never edited in place (chat 68).
# r2-bib.py — R3 (chat 153-R) — the two census bodies DEF-152 item 10 carried open from chat 151-B, taken:
# mc 387–672  the 286 C13-HANDLE-LEAK rows of the Mathematical Compendium's bibliography table, its `objects` column
# mc 293      the C6-NUMBERS-NOT-IN-SOURCE row on the modular-ledger block's eleven numerals
# The question for the 286 is computable and was never computed: does a handle printed in that column RESOLVE —
# to an object stated anywhere in the compendium outside the table, or to any site in any other volume? A handle
# that resolves nowhere is a generator identifier printed for a reader who cannot follow it. The question for 293
# is what the nine numerals census.py could not find in the block's sources ARE, reproduced under census.py's own
# extraction rule and then read.
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness.
import os, re, sys, hashlib, collections
H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
def hr(t): print('\n== ' + t)
def norm(s): return re.sub(r'\s+', ' ', s).strip()
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
VOLS = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md', 'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
        'sc': 'The_Method_1_6___Spectra_Compendium-2.md', 'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md'}
C = rd(MC); V = {k: '\n'.join(rd(v)) for k, v in VOLS.items()}
CEN = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv') if l.strip()]
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-70s %-24s %s' % (tag, repr(got)[:24], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-70s %-24s %s' % (tag, repr(got)[:24], 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))
print('r2-bib.py — census mc 387–672 (the bibliography\'s `objects` column) and mc 293 (the modular ledger\'s numerals)')
print('members: %s %s | %s | census %s' % (MC, md5(MC), ' | '.join('%s %s' % (k, md5(v)) for k, v in VOLS.items()), md5('DEFECT-CENSUS.tsv')))

# ------------------------------------------------------------------ §1
hr('§1 THE TABLE, located by scan — the census rows point into it and every one of them is a handle')
h = [i for i, l in enumerate(C, 1) if l.startswith('| year | work | objects |')]
check('exactly one bibliography table header', len(h), 1); h = h[0]
e = h + 1
while e < len(C) and C[e].startswith('|'): e += 1
data = [l for l in C[h + 1:e] if not l.startswith('|---')]
print('   header L%d, rows L%d–L%d, DATA rows %d' % (h, h + 2, e, len(data)))
check('the table prints 156 data rows, as the volume states', len(data), 156)
rows = [r for r in CEN[1:] if 387 <= int(r[0]) <= 672]
check('census ids 387–672 are 286 rows', len(rows), 286)
check('all 286 are C13-HANDLE-LEAK in mc', sorted({(r[1], r[2]) for r in rows}), [('C13-HANDLE-LEAK', 'mc')])
check('every one of the 286 points at a line of this table', all(h + 2 <= int(r[3]) <= e for r in rows), True)
RETIRED = [r for r in rows if r[5].startswith('RETIRED')]
LIVE_ROWS = [r for r in rows if not r[5].startswith('RETIRED')]
check('seven of the 286 are retired at W-307, their lines removed by register 1891',
      sorted(int(r[0]) for r in RETIRED), [431, 493, 534, 553, 609, 646, 649])
check('and all 279 others still point at a line that carries the handle',
      all(r[4] in C[int(r[3]) - 1] for r in LIVE_ROWS), True)
HANDLES = sorted({r[4] for r in rows})
fam = collections.Counter(x.split('.')[0] for x in HANDLES)
print('   distinct handles %d in %d families: %s' % (len(HANDLES), len(fam), dict(sorted(fam.items()))))
check('every item is an object handle (family.name), none a BUILD, chat, W or MC token', all(re.fullmatch(r'(?:3B|[A-Z]{1,2})\.[a-z]{3,6}', x) for x in HANDLES), True)
# the table's own handle set, read from the column — the census rows are a subset because census.py's pattern
# admits only 3–6 lowercase letters after the dot (`A.E`, `A.R`, `L.E0`, `S.bounds` are not in it)
allh = sorted({m for l in data for m in re.findall(r'`([^`]+)`', l.split('|')[3])})
print('   handles the column actually prints: %d; of which the census pattern admits %d' % (len(allh), len(HANDLES)))
check('the census handles are a subset of the column\'s', sorted(set(HANDLES) - set(allh)), [])

# ------------------------------------------------------------------ §2
hr('§2 RESOLUTION — where else, if anywhere, each handle is printed')
rest = '\n'.join(C[:h - 1] + C[e:])
def sites(hd, text): return len(re.findall(r'(?<![\w.`])`?' + re.escape(hd) + r'`?(?![\w.])', text))
RESOLVE = {}
for hd in allh:
    RESOLVE[hd] = {'mc': sites(hd, rest), **{k: sites(hd, v) for k, v in V.items()}}
inmc = [hd for hd in allh if RESOLVE[hd]['mc']]
elsewhere = [hd for hd in allh if not RESOLVE[hd]['mc'] and sum(RESOLVE[hd][k] for k in VOLS)]
nowhere = [hd for hd in allh if not sum(RESOLVE[hd].values())]
print('   in the compendium outside the table: %d | elsewhere only: %d | nowhere: %d' % (len(inmc), len(elsewhere), len(nowhere)))
for hd in inmc:
    where = [(i, norm(l)[:90]) for i, l in enumerate(C, 1) if not (h + 2 <= i <= e) and sites(hd, l)]
    print('   %-12s in the compendium outside the table at: %s' % (hd, where[:2]))
check('handles the compendium prints outside the table', inmc, ['A.staircls', 'C.Aq', 'E.nuclide', 'L.F', 'M.C1', 'M.C2'])
check('every one of those six is printed as a REFERENCE inside another entry, not as the name of its own', all(not any(re.match(r'^#', l) for i, l in enumerate(C, 1) if not (h + 2 <= i <= e) and sites(hd, l)) for hd in inmc), True)
byvol = collections.Counter(k for hd in elsewhere for k in VOLS if RESOLVE[hd][k])
print('   the elsewhere-only handles resolve in: %s' % dict(byvol))
GA = [i for i, l in enumerate(rd(VOLS['main']), 1) if re.match(r'^#{1,4}\s', l) and l.strip().endswith('Appendix G — Transitions, indexed')][-1]
gtext = '\n'.join(rd(VOLS['main'])[GA - 1:GA + 60])
ing = [hd for hd in elsewhere if sites(hd, gtext)]
print('   of those, printed in Appendix G\'s "what rests on it" column: %d' % len(ing))
print('   nowhere: %s' % ' '.join(nowhere))
cn = [hd for hd in HANDLES if hd in nowhere]; ce = [hd for hd in HANDLES if hd in elsewhere]
# The three figures below are the class defect's MEASUREMENT, not an invariant: an entry that names a handle makes it
# resolve (registers 1824 and 1825 name K.peak and K.deadend, and the figures moved 93 / 86 / 133 -> 92 / 87 / 132 at
# BUILD105). r2-bib pinned them as checks and exited 1 on the first Register entry to name a handle; the successor
# prints them as measurements beside the figures the class was closed on (DEF-152 item 10, BUILD100).
def measured(tag, got, then): print('   %-70s %-24s measured (%d at the closing reading)' % (tag, repr(got), then))
measured('census handles resolving nowhere', len(cn), 93)
measured('census handles resolving only outside the compendium', len(ce), 86)
measured('census rows whose handle resolves nowhere', len([r for r in rows if r[4] in nowhere]), 133)
check('census rows whose handle the compendium prints outside the table', len([r for r in rows if r[4] in inmc]), 0)
check('mathreg.py, where the handle -> object map lives, is a member of this build', os.path.exists(os.path.join(H, 'mathreg.py')), False)
score('a reader can follow every handle in the `objects` column to an object the volume states', len(nowhere) == 0 and len(inmc) == len(allh), True, 'bib-01')

# ------------------------------------------------------------------ §3
hr('§3 CENSUS 293 — the modular ledger\'s numerals under census.py\'s own rule, then read')
r293 = [r for r in CEN[1:] if r[0] == '293'][0]
print('   census 293: %s' % '\t'.join(r293)[:160])
check('293 is C6-NUMBERS-NOT-IN-SOURCE on "The modular ledger"', (r293[1], r293[4]), ('C6-NUMBERS-NOT-IN-SOURCE', 'The modular ledger'))
led = [i for i, l in enumerate(C, 1) if l.strip() == '### The modular ledger'][0]
nh = [i for i, l in enumerate(C, 1) if i > led and (l.startswith('### ') or l.startswith('## '))][0]
body = '\n'.join(C[led:nh - 1])
def nums(s): return set(re.findall(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w])', s))
yr = lambda x: re.fullmatch(r'1[5-9]\d\d|20[0-2]\d', x)
en = sorted((x for x in nums(body) if not yr(x) and not re.fullmatch(r'\d{1,2}', x)), key=lambda z: (len(z), z))
print('   block L%d–L%d; numerals under the rule (years and 1–2 digit figures excluded): %s' % (led, nh - 1, en))
check('eleven numerals, as the census counted', len(en), 11)
rr = sorted({int(x) for x in re.findall(r'\b(?:R|[Rr]egister)\s(\d{1,4})\b', body)})
check('the block\'s Register pointers', rr, [1019, 1020, 1022, 1035, 1483, 1484])
R = rd(VOLS['reg']); regtext = {}; cur = None
for l in R:
    m = re.match(r'^### (\d+)\s*$', l)
    if m: cur = int(m.group(1)); regtext[cur] = []
    elif cur is not None: regtext[cur].append(l)
src = '\n'.join('\n'.join(regtext[n]) for n in rr); sn = nums(src)
miss = [x for x in en if x not in sn]
print('   not in the cited entries\' text: %s' % miss)
check('nine of the eleven, as the census counted', len(miss), 9)
check('the two that are in source are the pointers other cited entries name', sorted(set(en) - set(miss)), ['1020', '1022'])
POINTERS = [x for x in miss if int(x.rstrip(',')) in rr]
prior = [norm(l) for l in C[led:nh - 1] if l.startswith('> **Prior art')]
LOCATORS = [x for x in miss if x not in POINTERS and any(x.rstrip(',') in p for p in prior)]
print('   Register pointers among the nine: %s' % POINTERS)
print('   locators of the block\'s own prior-art line among the nine: %s' % LOCATORS)
print('   prior art: %s' % prior[0][:150])
check('the nine are four Register pointers and five journal locators, nothing else', (sorted(POINTERS), sorted(LOCATORS), sorted(set(miss) - set(POINTERS) - set(LOCATORS))),
      (['1019,', '1035', '1483', '1484'], ['107', '114', '143', '315', '332'], []))
print('   (census.py\'s rule keeps a trailing comma on "1019," — the numeral is 1019, the block\'s first pointer)')
check('the locators are Borchers 1992 (CMP 143, 315–332) and Wiesbrock 1993 (LMP 28, 107–114)', all(t in prior[0] for t in ('143 (1992) 315-332', '28 (1993) 107-114')), True)
score('the block states a figure about its object that its sources do not carry', len(set(miss) - set(POINTERS) - set(LOCATORS)) > 0, False, 'bib-02')

# ------------------------------------------------------------------ verdict
hr('VERDICT')
print('   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
print('   deviations recorded: %d' % len(DEV))
for tagno, tag, got, exp in DEV: print('      %s  %s — measured %r, printed %r' % (tagno, tag, got, exp))
print('   mc 387–672: DEFECT, one class at one site. The `objects` column prints %d handles; the compendium prints' % len(allh))
print('   %d of them outside the table and only as references inside other entries, never as an object\'s own name;' % len(inmc))
print('   %d resolve only to another volume — the Register and the main volume, Appendix G\'s column among the sites —' % len(elsewhere))
print('   and %d resolve nowhere.' % len(nowhere))
print('   nowhere. The map from handle to object is mathreg.py\'s, and mathreg.py is not a member — docket 38 as much')
print('   as docket 28. Recorded, not repaired: the repair is the generator\'s, printing each handle beside the object')
print('   it names, and the generator is not held.')
print('   mc 293: NOT A DEFECT. The nine numerals are the block\'s four Register pointers and the five journal locators')
print('   of its own prior-art line; the class asks for a figure the block states about its object that its sources')
print('   do not carry, and there is none. The two "in source" are 1020 and 1022 because 1483 and 1484 name them.')
sys.exit(1 if FAIL else 0)
