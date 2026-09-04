#!/usr/bin/env python3
# r2-regsweep2.py — R3 (chat 153-R) — SUCCESSOR to r2-regsweep.py: the Register's extent is DATA, read from the front
# matter register_counts.py maintains, where the predecessor asserted 1,635 / 1,628 / 1,660 / 1,792 as invariants and
# printed INSTRUMENT FAULT once the Register grew (DEF-151r3 item 5). Four checks change; every sweep is identical.
# r2-regsweep is seated and never edited in place (chat 68).
# r2-regsweep.py — the Register read: the WHOLE-VOLUME MECHANICAL BASELINE.
#
# NOT a substitute for the source-order read. M ruled the Register is read in full under the chat-81
# cadence, and it is; this instrument exists so that each unit scores its prose against a measured
# baseline instead of rebuilding the same six resolvers thirty-eight times. It answers only the
# questions a machine can answer over all 1,635 entries at once:
#   1. does every pointer resolve -- register, section, lettered, figure, chapter;
#   2. does every entry carry the settled form (a bold capitalised headline, then an italic body);
#   3. which numbers are absent, and of those which are cited;
#   4. is any entry number printed twice.
# Everything a machine cannot answer -- whether a resolved pointer carries the CLAIM, whether a
# figure is superseded-and-preserved or stale-and-colliding, whether a count word counts what it
# says -- stays with the unit reads and is not attempted here.
#
# CONVENTIONS, FIXED BEFORE ANYTHING IS SCORED.
#  - ENTRY: a heading line "### N" or "### N, N, ..." (docket 30). 1,635 of them over 1,660 numbers.
#  - THE APPENDIX F PROTOCOL GOVERNS STALE NUMERALS. "A superseded numeral inside an entry is the
#    record of what was written, not a defect in it", rested on the numeral "colliding with nothing".
#    So a figure numeral is reported in two classes, never one: RESOLVES, or COLLIDES (the numeral is
#    live and denotes something else). Only the second is a candidate finding, and even then the unit
#    read decides it -- reg4-01 is the worked case.
#  - SECTION POINTERS resolve on the exact-token rule, never a prefix, and a chapter heading may
#    carry a trailing period ("## 4. The failures ..."). Both were faults in earlier units.
#  - APPENDIX SUBSECTIONS are plain-text labels, not headings, and are located inside their appendix.
# FAULT SELF-CAUGHT AND NAMED, AND IT IS THE WORST KIND. The section resolver first ended in \s+,
# which matches a NEWLINE, so "### 784" -- a Register ENTRY heading -- satisfied the pattern for
# "§784" and the sweep reported that pointer as resolving. §784 resolves to no section in any volume;
# it is 26b-08, recorded at W-190. An instrument that HIDES a known finding is worse than one that
# invents a false one, and this one hid it for exactly one run. The resolver now requires a title
# after the numeral on the same line ([ \t]+\S), which no bare entry heading can satisfy.
# Deterministic: no wall clock, no randomness.
import os, re, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
REG = 'The_Method_1_6___The_Register-2.md'
T = rd(REG); RL = T.split('\n')
M = rd('The_Method_1_6-2.md'); ML = M.split('\n')
VOLS = {'main': M, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'),
        'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
        'sc': rd('The_Method_1_6___Spectra_Compendium-2.md'),
        'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'reg': T}
FAIL = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-58s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)


# --- extent as data (DEF-151r3 item 5): the printed figures are read from the front matter, never asserted ---
import importlib.util as _ilu
_rc = _ilu.module_from_spec(_ilu.spec_from_file_location('register_counts', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'register_counts.py')))
_rc.__spec__.loader.exec_module(_rc)
_PRINTED = _rc.printed(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'The_Method_1_6___The_Register-2.md'), encoding='utf-8').read())
hr('0  THE POPULATION')
heads = re.findall(r'^### ([\d, ]+)$', T, re.M)
bare = [h for h in heads if h.strip().isdigit()]
grouped = [h for h in heads if not h.strip().isdigit()]
allnums = sorted({int(x) for h in heads for x in h.split(',')})
check('entries (heading lines) = the front matter\'s printed total', len(heads), _PRINTED['front_total'])
check('bare / grouped', (len(bare), len(grouped)), (_PRINTED['front_total'] - 7, 7))
check('distinct numbers = headings + the 25 extra numbers the seven grouped headings carry', len(allnums), len(heads) + 25)
flat = [int(x) for h in heads for x in h.split(',')]
dup = [n for n, c in collections.Counter(flat).items() if c > 1]
check('no entry number printed twice', dup, [])

hr('1  THE ENTRY FORM, OVER EVERY ENTRY')
# the settled form: **CAPITALISED HEADLINE** then the body in italics.
blocks = re.split(r'\n### [\d, ]+\n', T)[1:]
ids = [h for h in heads]
bad_open, no_body, unbalanced = [], [], []
for hid, blk in zip(ids, blocks):
    body = blk.strip()
    if not body: continue
    first = body.split('\n')[0]
    if not first.startswith('**'): bad_open.append(hid)
    n = first.count('*')
    if n % 2: unbalanced.append((hid, n))
print('   entries with a body            : %d' % len([b for b in blocks if b.strip()]))
print('   entries whose body is empty    : %d' % len([b for b in blocks if not b.strip()]))
check('every non-empty body opens on a bold headline', bad_open, [])
print('   entries whose first line carries an ODD number of asterisks: %d' % len(unbalanced))
# AN ASTERISK IS ALSO NOTATION IN THIS CORPUS, so the class holds false positives and is a
# CANDIDATE LIST, never a verdict: phi* is Miedema's electronegativity parameter (entry 26) and
# "(3, 0, 1, 1, *, 0, 1, 1)" is a wildcard coordinate (entry 604). Both are correct text with an
# odd count. Entries are labelled, and every verdict is left to the unit read that reaches them.
NOTATION = re.compile(r'[φΦ]\*|\(\s*\*\s*\)|,\s*\*\s*,|\)\*|\d\*')
first = {h: b.strip().split('\n')[0] for h, b in zip(ids, blocks) if b.strip()}
cand = []
for hid, n in unbalanced:
    tag = 'notation present' if NOTATION.search(first[hid]) else 'CANDIDATE'
    if tag == 'CANDIDATE': cand.append(hid)
    print('     entry %-8s %2d asterisks   %s' % (hid, n, tag))
print('   %d carry a recognisable notation token and are very likely correct as printed;' % (len(unbalanced) - len(cand)))
print('   %d carry none and are candidates for the reg3-01 class: %s' % (len(cand), cand))
print('   Entry 313 is the one CONFIRMED by reading (reg3-01). The rest are handed to their units.')

hr('2  REGISTER POINTERS, OVER EVERY VOLUME')
rng = re.compile(r'(?i)\bregisters?\s+(\d+)')
cited = collections.Counter()
where = collections.defaultdict(set)
for vol, txt in VOLS.items():
    for m in rng.finditer(txt):
        cited[int(m.group(1))] += 1; where[int(m.group(1))].add(vol)
absent_cited = sorted(n for n in cited if n not in allnums)
print('   distinct register numbers cited anywhere : %d' % len(cited))
check('cited numbers with no entry, BARE-NUMBER net', absent_cited, [344, 571])
print('   in which volumes: %s' % {n: sorted(where[n]) for n in absent_cited})
print('   register_cites.py reports 31 on a RANGE-AWARE net that also expands "registers 344-346"')
print('   and the "R NNN" form. The two nets are both right about their own convention and the')
print('   difference is the finding of reg1-05: what a sweep sees is decided by the net it uses.')

hr('3  ABSENT NUMBERS, AND WHETHER ANYTHING CITES THEM')
absent = [n for n in range(1, max(allnums) + 1) if n not in allnums]
check('numbers absent in 1..1792 (the predecessor\'s measurement, unchanged)', len([n for n in absent if n <= 1792]), 132)
print('   numbers absent above 1792, in 1..%d: %s (staged, not seated — register 1797 is queued in REGISTER-QUEUE-APPEND-cypher-audit.md)' % (max(allnums), [n for n in absent if n > 1792]))
ac = [n for n in absent if n in cited]; au = [n for n in absent if n not in cited]
print('   absent AND cited   : %d %s' % (len(ac), ac))
print('   absent and uncited : %d' % len(au))
ELEVEN = [204, 206, 210, 260, 264, 269, 272, 287, 324, 341, 344]
print('   L6574 enumerates eleven "in no group at all", scoped between 203 and 354: %s' % ELEVEN)
out = [n for n in absent if not (203 <= n <= 354)]
print('   absent numbers OUTSIDE that scope: %d -> %s' % (len(out), out[:24]))

hr('4  SECTION POINTERS FROM THE REGISTER INTO THE MAIN VOLUME')
def resolves(sec):
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)\s+' % re.escape(sec))
    return any(p.match(l) for l in ML)
def resolves_any(sec):
    p = re.compile(r'^#{2,6} %s\.?(?!\d)(?!\.\d)[ \t]+\S' % re.escape(sec), re.M)
    return [v for v, txt in VOLS.items() if p.search(txt)]
secs = sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)', T)), key=lambda s: [int(x) for x in s.split('.')])
unres = [s for s in secs if not resolves_any(s)]
print('   distinct section pointers in the register : %d' % len(secs))
print('   resolving in NO volume: %s' % unres)
KNOWN = {'784': 'a REGISTER NUMBER printed with a § sigil - 26b-08, recorded at W-190',
         '0': 'the Spectra Compendium\'s own §0, where δ is defined (entry at reg L6311)',
         '4.1': "Chapter 4's list items, not headings (MAIN_AUDIT V1)",
         '4.2': 'ditto', '4.3': 'ditto', '4.4': 'ditto', '4.5': 'ditto', '4.6': 'ditto', '4.7': 'ditto',
         '5.7': 'the companion paper, not this volume (IOI_SPEC_AUDIT I1)',
         '8.7': 'a section of Transitions v3.0, among the forty-seven this work does not use (reg L6559)',
         '784': 'a REGISTER NUMBER printed with a § sigil - 26b-08, recorded at W-190'}
resid = [s for s in unres if s not in KNOWN]
for s in unres: print('     §%-6s %s' % (s, KNOWN.get(s, 'UNACCOUNTED')))
check('section pointers unaccounted for', resid, [])

hr('5  FIGURE NUMERALS: RESOLVES, OR COLLIDES')
figs = sorted(set(re.findall(r'Figure\s+(\d+\.\d+)', T)))
live = set(re.findall(r'!\[Figure (\d+\.\d+)\]', M))
print('   figure numerals named in the register : %d' % len(figs))
print('   figures actually embedded in the main volume : %d' % len(live))
missing = [f for f in figs if f not in live]
print('   named by the register, NOT embedded : %s' % missing)
print('   every other numeral the register names is live; whether it names the RIGHT figure is a')
print('   claim question and belongs to the unit read (reg4-01 is the worked case at 23.1 / 23.2).')

hr('6  CHAPTER AND LETTERED POINTERS')
chs = sorted({int(x) for x in re.findall(r'(?i)\bchapters?\s+(\d+)', T)})
maxch = max(int(m.group(1)) for m in re.finditer(r'^## (\d+)\.', M, re.M))
print('   chapters cited by the register: %d..%d ; the volume runs to %d' % (min(chs), max(chs), maxch))
check('no chapter cited above the volume\'s last', [c for c in chs if c > maxch], [])
lets = sorted(set(re.findall(r'\b([A-G]\.\d+(?:\.\d+)?)\b', T)))
deadl = [l for l in lets if l not in M]
print('   lettered pointers: %d ; not found anywhere in the main volume: %s' % (len(lets), deadl))

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
