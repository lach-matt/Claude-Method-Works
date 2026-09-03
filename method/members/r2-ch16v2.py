#!/usr/bin/env python3
# r2-ch16v2.py — chat 153 — SUCCESSOR to r2-ch16v.py, re-anchored. Identical measurements; one address moves.
# r2-ch16v read MAIN[9891] — the `## 36.` heading — by fixed index. r3-wl2's +8 shift at main L9608 moved that
# heading to 9900, so the seated instrument prints the wrong line where register 1359's cut chapter is
# reported, and re-banking it would bank that wrong line. The heading is now resolved with heading_line,
# which this instrument already imports and which the standing method requires (exact token, body
# occurrence, never prefix). r2-ch16v is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: reproduces r2-ch16v.out byte-exact on the pre-shift bundles (G0c).
# r2-ch16v -- PROSE batch for the chat-125 section read: main L9393-L9493
# (# PART VII divider, ch.33 head, 33.1-33.5).  Reads MEMBERS and the Prints & Proofs original.
# Deterministic; prints no wall-clock time.
import os, re, sys, importlib.util

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def norm(s): return re.sub(r'\s+', ' ', s.strip())

# owed to r2lib (DEFERRED): body_range, carried with provenance from r2-ch16m (chat 121).
def body_range(M, sec):
    s = heading_line(M, sec)
    if s is None: return None
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1].strip()): return (s, i)
    return (s, len(M) + 1)

MAIN = rd('The_Method_1_6-2.md')
REG  = rd('The_Method_1_6___The_Register-2.md')
MC   = rd('The_Method_1_6___Mathematical_Compendium-2.md')
PC   = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI  = rd('The_Method_1_6___The_Index_of_Indices-2.md')
SC   = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOL  = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
PP   = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
U0, U1 = 9393, 9493
UNIT = list(range(U0, U1 + 1))

# ---------------------------------------------------------------- 1. pointers, both resolvers
hr('1. EVERY POINTER IN THE UNIT, resolved to the CLAIM and under BOTH resolvers')
ptr = {}
for i in UNIT:
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)', MAIN[i - 1]):
        ptr.setdefault(m.group(1), []).append(i)
    for m in re.finditer(r'Chapters? (\d+)', MAIN[i - 1]):
        ptr.setdefault('ch' + m.group(1), []).append(i)
for k in sorted(ptr, key=lambda z: (z.startswith('ch'), z)):
    sites = sorted(set(ptr[k]))
    if k.startswith('ch'):
        n = k[2:]
        occ = [j + 1 for j, s in enumerate(MAIN) if s.startswith(f'## {n}.')]
        body = occ[-1] if occ else None
        end = ([j + 1 for j, s in enumerate(MAIN) if s.startswith('## ') and body and j + 1 > body]
               or [len(MAIN) + 1])[0]
        print(f'  Chapter {n:3s} cited at {sites}: occurrences {occ} -> BODY {body}, '
              f'span {body}-{end - 1}: {norm(MAIN[body - 1]) if body else "NO TARGET"}')
    else:
        br, ss = body_range(MAIN, k), section_span(MAIN, k)
        hl = heading_line(MAIN, k)
        print(f'  §{k:8s} cited at {sites}: heading_line={hl}  body_range={br}  '
              f'section_span={ss}  {"COINCIDE" if br == ss else "DIFFER"}')
        if hl is None:
            occ = [j + 1 for j, s in enumerate(MAIN) if s.startswith(f'## {k}.')]
            print(f'      numeric resolver returns None; "## {k}." occurrences {occ}')

# ---------------------------------------------------------------- 2. the duplicated epigraph
hr('2. THE LÖWDIN EPIGRAPH, PRINTED TWICE SEVEN LINES APART')
a = norm(' '.join(MAIN[9488:9492]))
b = norm(' '.join(MAIN[9495:9498]))
print(f'  §33.5 tail  L9489-L9492: {a}')
print(f'  ch.34 head  L9496-L9498: {b}')
pre = os.path.commonprefix([a, b])
print(f'  common prefix, {len(pre)} chars: {pre}')
print(f'  divergence -> §33.5: "...{a[len(pre):][:80]}"')
print(f'  divergence -> ch.34: "...{b[len(pre):][:80]}"')
print(f'  identical: {a == b}')
print('  the Part VII epigraph the §33.5 tail also echoes, L9395-L9397:')
print('    ' + norm(' '.join(MAIN[9394:9397])))
print('  register 1359 (reg L5105) fixes Part VII\'s structure:')
print('    ' + norm(REG[5104])[:260])

# ---------------------------------------------------------------- 3. attributions
hr('3. EVERY ATTRIBUTION IN THE UNIT against the References BODY occurrence and R.7')
refs = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## References')]
RB = refs[-1]
r7 = [i + 1 for i, s in enumerate(MAIN) if re.match(r'^#{1,4}\s*R\.7', s.strip())]
print(f'  "## References" occurrences {refs}; BODY = L{RB}; R.7 heading {r7}')
names = set()
for i in UNIT:
    for m in re.finditer(r'\b([A-ZÄÖÜ][a-zäöüé]+(?:[-–][A-ZÄÖÜ][a-zäöüé]+)?)\b', MAIN[i - 1]):
        names.add(m.group(1))
STOP = {'The','This','That','An','And','Where','Across','Two','Six','Its','How','What','Only',
        'Ask','Then','Chapter','Chapters','Part','Every','Never','Each','In','It','Half','Λ',
        'Parts','But','For','A','Rydberg','Nine','Five','Four','Three','One','No','Whether'}
cand = sorted(n for n in names - STOP if n not in ('Schrödinger',) or True)
bib = '\n'.join(MAIN[RB - 1:])
for n in cand:
    sites = [i for i in UNIT if re.search(r'\b' + re.escape(n) + r'\b', MAIN[i - 1])]
    inbib = bool(re.search(r'\b' + re.escape(n) + r'\b', bib))
    if n in ('Löwdin', 'Demkov', 'Ostrovsky', 'Schrödinger', 'Olov', 'Per'):
        print(f'    {n:14s} unit sites {sites}  in References body: {inbib}')
print('  the two that fail, given their own witnesses across all six volumes:')
for n in ('Schrödinger', 'Demkov'):
    tot = {k: [i + 1 for i, s in enumerate(M) if re.search(r'\b' + n + r'\b', s)] for k, M in VOL}
    print(f'    {n}: ' + ', '.join(f'{k} {len(v)}' for k, v in tot.items()))
    inref = [i for i in tot['main'] if i >= RB]
    print(f'      inside the References body (L{RB}+): {inref if inref else "NONE -- unbibliographed"}')
print('  and where the Demkov-Ostrovsky claim of L9468 does live:')
for k, M in VOL:
    for i, s in enumerate(M):
        if re.search(r'Demkov', s) and re.search(r'slope|½|1/2|identity', s, re.I):
            print(f'    {k} L{i + 1}: ' + norm(s)[:150])

# ---------------------------------------------------------------- 4. Ruling 45 and Ruling 46
hr('4. RULING 45 (build / editorial-process prose) and RULING 46 (script and file names)')
R45 = [r'\bthis book\b', r'\bthe author\b', r'\ban earlier (draft|version)\b', r'\ba previous draft\b',
       r'\bwas arrived at\b', r'\bhad to be restated\b', r'\bit is enforced in code\b',
       r'\bthis work\b', r'\bwas not designed\b', r'\bafter audit\b', r'\bcut after\b']
hits45 = []
for i in UNIT:
    for p in R45:
        if re.search(p, MAIN[i - 1], re.I): hits45.append((i, p, norm(MAIN[i - 1])[:96]))
print(f'  Ruling 45 candidate sites in {len(UNIT)} lines: {len(hits45)}')
for i, p, t in hits45: print(f'    L{i}  [{p}]  {t}')
R46 = [r'\b\w+\.py\b', r'\bBUILD\d+\b', r'\bregister_cites\b', r'\bgate\.py\b', r'\.md\b',
       r'\bmembers/\b', r'\bgolden\b']
hits46 = [(i, p) for i in UNIT for p in R46 if re.search(p, MAIN[i - 1])]
print(f'  Ruling 46 sites in the unit (case-sensitive, word-bounded): {len(hits46)} {hits46}')
print('  for contrast, the SAME protocol names a script in the Register (permitted there):')
print('    reg L5017 tail: ' + norm(REG[5016])[-60:])

# ---------------------------------------------------------------- 5. first person
hr('5. FIRST-PERSON PROSE (guarded against the Roman numeral in species names)')
fp = []
for i in UNIT:
    s = MAIN[i - 1]
    for m in re.finditer(r'\b(I|my|we|our)\b', s):
        if m.group(1) == 'I':
            ctx = s[max(0, m.start() - 6):m.end() + 3]
            if re.search(r'[A-Z][a-z]{0,2}\s+I\b', ctx) or re.search(r'\bI+[IVX]*\b', ctx):
                continue                      # He I, Sc I, C IV ... a species, not a pronoun
        fp.append((i, m.group(1), norm(s)[:90]))
print(f'  first-person sites in the unit: {len(fp)}')
for x in fp: print(f'    L{x[0]}  "{x[1]}"  {x[2]}')

# ---------------------------------------------------------------- 6. Prints & Proofs anchors
hr('6. PRINTS & PROOFS -- every unit line anchored on its own text')
off = None
probe = [i for i in UNIT if len(MAIN[i - 1]) > 40]
for i in probe[:6]:
    t = norm(MAIN[i - 1])
    for j, s in enumerate(PP):
        if norm(s) == t: off = j + 1 - i; break
    if off is not None: break
print(f'  offset measured from the first matching unit line: {off}')
ok = miss = 0; missing = []
for i in UNIT:
    t = norm(MAIN[i - 1])
    if not t: continue
    j = i + (off or 0)
    got = norm(PP[j - 1]) if 0 < j <= len(PP) else ''
    if got == t: ok += 1
    else:
        found = [k + 1 for k, s in enumerate(PP) if norm(s) == t]
        if found: ok += 1
        else: miss += 1; missing.append((i, t[:80]))
print(f'  unit lines matching PP verbatim: {ok};  not matching: {miss}')
# FAULT 2, self-caught: a heading that fails a verbatim match is not absent from PP.  The volume
# NUMBERS the section headings and PP does not, so compare the heading's TITLE, not its whole line.
unnum = []
for i, t in list(missing):
    m = re.match(r'^(#{2,4}) (\d+(?:\.\d+)*) (.+)$', norm(MAIN[i - 1]))
    if m:
        want = f'{m.group(1)} {m.group(3)}'
        hit = [k + 1 for k, s in enumerate(PP) if norm(s) == want]
        if hit:
            unnum.append((i, hit[0], m.group(2), m.group(3)))
            missing.remove((i, t))
print(f'  of those, headings PRESENT in PP but UNNUMBERED: {len(unnum)}')
for i, p, num, title in unnum:
    print(f'    L{i} "### {num} {title}"  ->  PP P{p} "### {title}"  (number added at production)')
print(f'  genuinely absent from PP: {len(missing)}')
for i, t in missing: print(f'    ABSENT L{i}: {t}')

# ---------------------------------------------------------------- 7. census rows
hr('7. DEFECT-CENSUS.tsv ROWS IN RANGE (classes main AND all)')
C = open(os.path.join(H, 'DEFECT-CENSUS.tsv'), encoding='utf-8').read().split('\n')
hdr = C[0].split('\t'); mi = hdr.index('member'); li = hdr.index('line')
rows = []
for r in C[1:]:
    if not r.strip(): continue
    f = r.split('\t')
    if len(f) <= max(mi, li): continue
    if f[mi] in ('main', 'all'):
        try: ln = int(f[li])
        except ValueError: continue
        if U0 <= ln <= U1: rows.append(r)
print(f'  header: {hdr}')
print(f'  rows with member in (main, all) and line in [{U0},{U1}]: {len(rows)}')
for r in rows: print('    ' + r[:150])

# ---------------------------------------------------------------- 8. duplicated-section sweep
hr('8. DUPLICATED-SECTION SWEEP (DEF-105 item 1) -- long unit lines recurring elsewhere')
long = [i for i in UNIT if len(norm(MAIN[i - 1])) >= 60]
rec = []
for i in long:
    t = norm(MAIN[i - 1])
    other = [j + 1 for j, s in enumerate(MAIN) if norm(s) == t and not (U0 <= j + 1 <= U1)]
    if other: rec.append((i, other, t[:70]))
print(f'  long lines examined: {len(long)};  recurring outside the unit: {len(rec)}')
for i, o, t in rec: print(f'    L{i} also at {o}: {t}')

# ---------------------------------------------------------------- 9. unmarked sub-headings
hr('9. PLACEHOLDER / UNMARKED-HEADING SWEEP inside the unit')
for i in UNIT:
    s = MAIN[i - 1]
    if s.startswith('#'):
        nxt = MAIN[i] if i < len(MAIN) else ''
        body = [k for k in range(i + 1, min(i + 6, len(MAIN))) if MAIN[k - 1].strip()
                and not MAIN[k - 1].startswith('#')]
        print(f'  L{i} {"HEADING":8s} {s[:60]:62s} body within 5 lines: {"yes" if body else "NO"}')
# FAULT 3, self-caught: without a blank line above, this caught the WRAP TAILS of italic
# sentences ("made explicit.*") and reported three sub-headings where the unit has none.
print('  plain body lines reading as sub-headings (short, bold-free, no terminal stop,')
print('  and starting a paragraph -- a blank line above, which is what makes it a heading):')
found_sub = 0
for i in UNIT:
    t = norm(MAIN[i - 1])
    above = norm(MAIN[i - 2]) if i > 1 else ''
    if t and above == '' and not t.startswith(('#', '|', '>', '*', '-')) and len(t) < 55 \
       and not t.endswith(('.', ':', ',')) and '**' not in t:
        print(f'    L{i}: {t}'); found_sub += 1
print(f'    unmarked sub-headings in the unit: {found_sub}  '
      f'(chat 124 found two in §32.7 by the same test)')

# ---------------------------------------------------------------- 10. the §33 structure
hr('10. THE PRINTED §33 STRUCTURE against register 1359')
for i in UNIT:
    if MAIN[i - 1].startswith('### '): print(f'  L{i}  {MAIN[i - 1]}')
print('  register 1359 names, in order: where it came from · its purpose · how it is used · '
      'the singleton criterion · what it cost to learn')
print('  register 1359 also states a three-body chapter was CUT; the volume now carries:')
print('    ' + norm(MAIN[heading_line(MAIN, '36') - 1]))
