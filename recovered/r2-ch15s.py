#!/usr/bin/env python3
"""r2-ch15s — prose batch for chat 112's unit: main L7940-L8028 (SS29.3-SS29.5.5).

Pointer resolution under BOTH body_range and section_span; claim tests, not token tests;
Ruling 45/46 sweeps; PP witness; two-line-join sweep.  Reads members, never a bundle.
"""
import re, importlib.util

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOL = {
    'main': 'The_Method_1_6-2.md',
    'reg':  'The_Method_1_6___The_Register-2.md',
    'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
    'sc':   'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(MEM + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
LO, HI = 7940, 8028
UNIT = M[LO - 1:HI]


# --- owed to r2lib: body_range (heading -> next heading of ANY rank) ---------
def body_range(Mx, sec):
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,6} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


# --- owed to r2lib: left-bounded stem matcher --------------------------------
def has_stem(text, stem):
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(stem), text, re.I))


# --- owed to r2lib: grouped-aware register lookup ----------------------------
def register_entry(n):
    R = V['reg']
    for i, t in enumerate(R, 1):
        s = t.strip()
        if re.match(r'^#{1,4}\s*%d\s*$' % n, s):
            return ('bare', i)
        m = re.match(r'^#{1,4}\s*([\d,\s]+)$', s)
        if m and str(n) in [x.strip() for x in m.group(1).split(',')]:
            return ('grouped', i)
    return (None, None)


# --- owed to r2lib: two-line-join phrase sweep -------------------------------
def phrase_sites(lines, phrase):
    p = re.escape(phrase).replace(r'\ ', r'\s+')
    out = []
    for i in range(1, len(lines) + 1):
        if re.search(p, lines[i - 1], re.I):
            out.append(i)
        elif i < len(lines) and re.search(p, lines[i - 1] + ' ' + lines[i], re.I):
            out.append(i)
    return out


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


# =============================================================================
head('P1  the unit\'s only section pointer: SS23.3 at L7995, resolved under BOTH resolvers')
print('  citing text L7995:', M[7994].strip())
print('  citing text L7996:', M[7995].strip())
br, sp = body_range(M, '23.3'), section_span(M, '23.3')
print(f'  SS23.3 heading_line {heading_line(M, "23.3")}  body_range {br}  section_span {sp}')
print('  heading:', M[heading_line(M, '23.3') - 1].strip())
for lab, rng in (('body_range', br), ('section_span', sp)):
    txt = '\n'.join(M[rng[0]:rng[1] - 1])          # excludes the heading line
    print(f'  --- {lab} {rng}, heading line EXCLUDED, {rng[1]-rng[0]-1} body lines ---')
    for tok in ('fitting', 'fit', 'paradigm', 'use', 'useless', 'V'):
        print(f'      token {tok!r:<10} {has_token(txt, tok)}   stem {has_stem(txt, tok)}')
    print(f'      raw symbol "V" {txt.count("V")}   raw "4ν/3" {txt.count("4ν/3")}')
print('  --- SS23.3 body, printed in full ---')
for i in range(br[0], br[1]):
    if M[i - 1].strip():
        print(f'   L{i}  {M[i-1].strip()[:150]}')
print('  --- where the claim DOES live: "fitting paradigm" across six volumes ---')
for k in V:
    for i in phrase_sites(V[k], 'fitting paradigm'):
        print(f'   {k} L{i} [{enclosing(V[k], i) if k == "main" else "-"}]  '
              f'{V[k][i-1].strip()[:120]}')

# =============================================================================
head('P2  Principle 8 at L7947 — existence and content')
print('  citing text L7947:', M[7946].strip())
for k in V:
    for i in phrase_sites(V[k], 'Principle 8'):
        print(f'   {k} L{i} [{enclosing(V[k], i) if k == "main" else "-"}]  '
              f'{V[k][i-1].strip()[:150]}')
print('  --- does any Principle 8 site assign "superseded" to a bound? ---')
for k in V:
    for i in phrase_sites(V[k], 'Principle 8'):
        seg = ' '.join(V[k][max(0, i - 3):i + 3])
        print(f'   {k} L{i}  supersed* {has_stem(seg, "supersed")}  bound {has_token(seg, "bound")}'
              f'  every {has_token(seg, "every")}')

# =============================================================================
head('P3  docket 16 — what L6683 "sixty-five years" attaches to (read, not tokenised)')
for i in range(6674, 6692):
    print(f'   L{i} [{enclosing(M, i)}]  {M[i-1].strip()[:160]}')
print('  --- every "N years old" age statement about the chapter, six volumes ---')
for k in V:
    for i, t in enumerate(V[k], 1):
        if re.search(r'(sixty|fifty|forty|seventy)[- ]?\w*\s+years', t, re.I):
            print(f'   {k} L{i}  {t.strip()[:150]}')

# =============================================================================
head('P4  the bibliography — how many Edlen entries, and under which dates')
for k in V:
    for i, t in enumerate(V[k], 1):
        if has_stem(t, 'Edl') and re.search(r'\(\d{4}\)', t):
            print(f'   {k} L{i} [{enclosing(V[k], i) if k == "main" else "-"}]  {t.strip()[:170]}')
print('  --- Handbuch der Physik / Encyclopedia of Physics title forms ---')
for k in V:
    for i, t in enumerate(V[k], 1):
        if re.search(r'Handbuch der Physik|Encyclopedia of Physics', t):
            print(f'   {k} L{i}  {t.strip()[:150]}')

# =============================================================================
head('P5  Ruling 45 sweep of the unit — build / editorial-process remarks to a reader')
R45 = ['recollection', 'earlier draft', 'earlier version', 'previous draft', 'we read',
       'we have read', 'this book cites', 'stated from', 'having previously',
       'we record it', 'we have not established', 'we state']
for p in R45:
    s = [i for i in phrase_sites(UNIT, p)]
    if s:
        for j in s:
            print(f'   {p!r:<26} L{LO + j - 1}  {UNIT[j-1].strip()[:130]}')
print('  --- first-person process verbs in the unit ---')
for i, t in zip(range(LO, HI + 1), UNIT):
    if re.search(r'\b(we|our)\b', t, re.I):
        print(f'   L{i}  {t.strip()[:150]}')

# =============================================================================
head('P6  Ruling 46 sweep of the unit — script names, build numbers, file references')
R46 = re.compile(r'\.py\b|BUILD\d|\.md\b|\.tsv\b|register\.py|gate\.py|W-\d+|HANDOFF', re.I)
hits = [(i, t) for i, t in zip(range(LO, HI + 1), UNIT) if R46.search(t)]
print(f'  Ruling 46 candidate sites in unit: {len(hits)}')
for i, t in hits:
    print(f'   L{i}  {t.strip()[:150]}')

# =============================================================================
head('P7  false universals and superlatives in the unit (docket 19)')
UNIV = ['every', 'no ', 'not one', 'nothing', 'any kind', 'all ', 'never', 'most likely',
        'closest thing', 'principal']
for i, t in zip(range(LO, HI + 1), UNIT):
    got = [w for w in UNIV if re.search(r'(?<![A-Za-z])' + re.escape(w.strip()) +
                                        r'(?![A-Za-z])', t, re.I)]
    if got:
        print(f'   L{i} {got}  {t.strip()[:135]}')

# =============================================================================
head('P8  PP witness — is the unit in the original input, and is SS29.5.4 an addition?')
def pp_find(phrase):
    return phrase_sites(PP, phrase)
for lab, ph in (('SS29.3 heading', 'The word for it'),
                ('SS29.4 heading', 'On priority for'),
                ('SS29.5 heading', 'examined at one remove'),
                ('SS29.5.1 heading', 'Every equation in the review is a fit'),
                ('SS29.5.2 heading', 'the paradigm is stated twice'),
                ('SS29.5.3 heading', 'One near miss'),
                ('SS29.5.4 heading', 'A bibliographic correction'),
                ('SS29.5.5 heading', 'What this establishes'),
                ('Curtis citation', 'Physica Scripta'),
                ('the 1960 note', 'delivered in final form'),
                ('140 pages', '140 pages'),
                ('six-page', 'six-page'),
                ('from recollection', 'from recollection'),
                ('Seven equations', 'Seven equations')):
    print(f'   {lab:<20} PP {pp_find(ph)}   main {phrase_sites(M, ph)}')

# =============================================================================
head('P9  duplicated-section sweep on the unit (docket 27) — long lines recurring')
longs = [(i, t.strip()) for i, t in zip(range(LO, HI + 1), UNIT) if len(t.strip()) >= 60]
rec = 0
for i, t in longs:
    key = t[:60]
    hits = [(k, j) for k in V for j, u in enumerate(V[k], 1) if key in u and not (k == 'main' and j == i)]
    if hits:
        rec += 1
        print(f'   L{i} recurs at {hits[:6]}   {t[:80]}')
print(f'  {rec} of {len(longs)} long lines recur elsewhere in the six volumes')

# =============================================================================
head('P10  two-line-join sweep of the unit\'s load-bearing phrases')
for ph in ('unprecedented rather than novel', 'two lines of algebra',
           'No error bound of any kind', 'the principle the bracket formalises',
           'flat, not ν-dependent', 'Not one is a bound', 'Predictions. Not bounds',
           'no accuracy ratio', 'a 1960 manuscript', 'Absence from 140 pages',
           'the one person most likely'):
    print(f'   {ph!r:<40} main {phrase_sites(M, ph)}  reg {phrase_sites(V["reg"], ph)}')

# =============================================================================
head('P11  every section pointer and register citation in the unit')
for i, t in zip(range(LO, HI + 1), UNIT):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', t):
        sec = m.group(1)
        print(f'   L{i} pointer §{sec}  heading_line {heading_line(M, sec)}  '
              f'body_range {body_range(M, sec)}')
    for m in re.finditer(r'(?i)\bregisters?\s+(\d+)', t):
        n = int(m.group(1))
        print(f'   L{i} register citation {n} -> {register_entry(n)}')

print('\nr2-ch15s complete.')
