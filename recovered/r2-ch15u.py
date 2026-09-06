#!/usr/bin/env python3
"""r2-ch15u - prose batch for chat 113's unit: main L8029-L8097 (SS29.6-SS29.8).

Every pointer resolved under BOTH body_range and section_span and against the
CLAIM, not the heading; the Chapter 19 authority read against what SS29.6 cites
it for; Ruling 45/46 sweeps; the Prints & Proofs witness; the duplicated-section
sweep; bibliography presence for every attribution.  Reads members, never a bundle.
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
LO, HI = 8029, 8097
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


# --- owed to r2lib: two-line-join phrase sweep (double-report repaired ch113) -
def phrase_sites(lines, phrase):
    p = re.escape(phrase).replace(r'\ ', r'\s+')
    out = []
    for i in range(1, len(lines) + 1):
        if re.search(p, lines[i - 1], re.I):
            out.append(i)
        elif (i < len(lines) and re.search(p, lines[i - 1] + ' ' + lines[i], re.I)
              and not re.search(p, lines[i], re.I)):
            out.append(i)
    return out


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


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


def body_text(Mx, sec, rng):
    """Body of a section with the HEADING LINE EXCLUDED."""
    return '\n'.join(Mx[rng[0]:rng[1] - 1])


# =============================================================================
head('P0  every section pointer and every register citation the unit carries')
ptr = {}
for off, t in enumerate(UNIT):
    ln = LO + off
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', t):
        ptr.setdefault(m.group(1), []).append(ln)
    for m in re.finditer(r'\bChapter (\d+)(?!\d)', t):
        ptr.setdefault('Ch' + m.group(1), []).append(ln)
print('  section/chapter pointers in L8029-L8097:')
for k, v in ptr.items():
    print(f'   {k:<10} at {v}')
regcites = [LO + o for o, t in enumerate(UNIT)
            if re.search(r'\bregisters?\s+\d', t, re.I)]
print(f'  register citations in the unit: {len(regcites)} {regcites}')

# =============================================================================
head('P1  SS23.8.4 - cited TWICE in this unit as setting out the four owners')
for i in (8064, 8085, 8086):
    print(f'  L{i}  {M[i-1].strip()[:170]}')
hl = heading_line(M, '23.8.4')
br, sp = body_range(M, '23.8.4'), section_span(M, '23.8.4')
print(f'  SS23.8.4 heading_line {hl}  body_range {br}  section_span {sp}')
print(f'  heading: {M[hl-1].strip()}')
for lab, rng in (('body_range', br), ('section_span', sp)):
    txt = body_text(M, '23.8.4', rng)
    print(f'  --- {lab} {rng}, heading EXCLUDED, {rng[1]-rng[0]-1} lines ---')
    for tok in ('Moore', 'IEEE', 'Manski', 'Shannon', 'credibility', 'zero-error', 'owners'):
        print(f'      {tok!r:<14} token {has_token(txt, tok)}  stem {has_stem(txt, tok)}')
print(f'  the two resolvers {"COINCIDE" if br == sp else "DIFFER"} for SS23.8.4.')
print('  --- SS23.8.4 body printed in full ---')
for i in range(br[0], br[1]):
    if M[i - 1].strip():
        print(f'   L{i}  {M[i-1].strip()[:150]}')
print('  carried MEASURED (chat 111, 15k-04), not re-derived: SS23.8.4 carries Moore')
print('  and IEEE but not Manski and Shannon.  This unit holds the CITING sites.')

# =============================================================================
head('P2  SS29.6 L8039 cites "the analysis of Chapter 19" - what Chapter 19 says')
print('  the citing claim L8039:', M[8038].strip())
for sec in ('19.5', '19.5.1'):
    h = heading_line(M, sec)
    b = body_range(M, sec)
    print(f'  --- SS{sec} heading_line {h} body_range {b} section_span {section_span(M, sec)}')
    print(f'      {M[h-1].strip()}')
    for i in range(b[0], b[1]):
        if M[i - 1].strip():
            print(f'   L{i}  {M[i-1].strip()[:165]}')
print('  --- token test: does Chapter 19 support "every route closed"? ---')
c19 = section_span(M, '19')
txt19 = '\n'.join(M[c19[0]:c19[1] - 1]) if c19 else ''
print(f'  chapter 19 section_span {c19}')
for tok in ('closed', 'unknown', 'retrievable', 'not retrieved', 'route'):
    print(f'      {tok!r:<16} {has_stem(txt19, tok.split()[0])}')
for ph in ('every route closed', 'UNKNOWN, not closed', 'Three of the four are retrievable',
           'Four documents in this work were not retrieved'):
    print(f'   {ph!r}: ' + '  '.join(f'{k} {phrase_sites(V[k], ph)}' for k in ('main',)))

# =============================================================================
head('P3  SS29.7.1 L8070 cites SS29.7 for "7/7 on controls" - resolve to the CLAIM')
print('  citing text L8070:', M[8069].strip())
b7, s7 = body_range(M, '29.7'), section_span(M, '29.7')
print(f'  SS29.7 body_range {b7}  section_span {s7}  '
      f'{"COINCIDE" if b7 == s7 else "DIFFER - section_span takes in SS29.7.1 itself"}')
for lab, rng in (('body_range', b7), ('section_span', s7)):
    txt = body_text(M, '29.7', rng)
    print(f'  --- {lab} {rng}, heading EXCLUDED ---')
    for tok in ('control', 'controls', 'calibration', 'calibrated'):
        print(f'      {tok!r:<14} {has_token(txt, tok)}')
    print(f'      raw "7/7" {txt.count("7/7")}')
print('  --- where "7/7" and "controls" DO live, six volumes ---')
for ph in ('7/7', 'control'):
    for k in V:
        s = phrase_sites(V[k], ph)
        if s:
            print(f'   {ph!r} {k}: {s[:14]}')
for i in phrase_sites(M, '7/7'):
    print(f'   main L{i} [{enclosing(M, i)}]  {M[i-1].strip()[:160]}')
print('  --- the section SS29.7 body, printed in full, as the witness ---')
for i in range(b7[0] + 1, b7[1]):
    if M[i - 1].strip():
        print(f'   L{i}  {M[i-1].rstrip()[:150]}')

# =============================================================================
head('P4  SS29.7.1 L8080 - the two pointers SS2.13 and SS28.6')
print('  citing text L8080:', M[8079].strip())
for sec, want in (('2.13', ['commit', 'look']), ('28.6', ['anchor', 'anchoring'])):
    h = heading_line(M, sec)
    if h is None:
        print(f'  SS{sec}: heading_line None - NO SUCH HEADING')
        continue
    b, s = body_range(M, sec), section_span(M, sec)
    print(f'  --- SS{sec} heading_line {h} body_range {b} section_span {s} '
          f'{"COINCIDE" if b == s else "DIFFER"}')
    print(f'      heading: {M[h-1].strip()}')
    for lab, rng in (('body_range', b), ('section_span', s)):
        txt = body_text(M, sec, rng)
        print(f'      {lab}: ' + '  '.join(f'{w!r} {has_stem(txt, w)}' for w in want))
print('  --- every "anchoring" site in the main volume, with its section ---')
for i in phrase_sites(M, 'anchoring'):
    print(f'   L{i} [{enclosing(M, i)}]  {M[i-1].strip()[:140]}')

# =============================================================================
head('P5  docket 7 - does SS29.7 L8052 carry the affine-invariance REASON?')
h = heading_line(M, '23.8.3')
b = body_range(M, '23.8.3')
print(f'  SS23.8.3 heading_line {h} body_range {b}')
for i in range(b[0], b[1]):
    if M[i - 1].strip():
        print(f'   L{i}  {M[i-1].strip()[:160]}')
print('  --- the two live targets, read ---')
for i in (8052, 8053):
    print(f'   L{i}  {M[i-1].rstrip()[:150]}')
for i in range(10374, 10382):
    print(f'   L{i} [{enclosing(M, i)}]  {M[i-1].strip()[:150]}')
print('  --- token test for the REASON, not the attribution ---')
for lab, txt in (('SS29.7 body', body_text(M, '29.7', body_range(M, '29.7'))),
                 ('App D.4.1 body', body_text(M, 'D.4.1', body_range(M, 'D.4.1'))
                  if heading_line(M, 'D.4.1') else '')):
    if txt:
        print(f'   {lab}: ' + '  '.join(
            f'{w!r} {has_stem(txt, w)}' for w in ('affine', 'invarian', 'reason', 'self-concordance')))
    else:
        print(f'   {lab}: heading_line returned None (lettered appendix heading)')
print('   App D.4.1 by line window instead:')
w = '\n'.join(M[10370:10395])
print('   ' + '  '.join(f'{x!r} {has_stem(w, x)}' for x in ('affine', 'invarian', 'reason')))

# =============================================================================
head('P6  Ruling 45 (build/editorial process to a reader) and Ruling 46, one pass')
R45 = ['audit', 'draft', 'earlier version', 'recollection', 'we read', 'we could not',
       'the search', 'this book cites', 'was done before', 'retained only']
R46 = [r'\.py\b', r'BUILD\d', r'register\s+\d', r'chat \d', r'\.md\b', r'MANIFEST']
for off, t in enumerate(UNIT):
    ln = LO + off
    hits = [w for w in R45 if has_stem(t, w.split()[0]) and w.lower() in t.lower()]
    r46 = [p for p in R46 if re.search(p, t, re.I)]
    if hits or r46:
        print(f'   L{ln}  R45{hits} R46{r46}')
        print(f'         {t.strip()[:150]}')
print('  first-person process statements in the unit:')
for off, t in enumerate(UNIT):
    if re.search(r'\b(we|our|I)\b', t) and not t.lstrip().startswith('#'):
        print(f'   L{LO+off}  {t.strip()[:150]}')

# =============================================================================
head('P7  Prints & Proofs witness - is the unit original, and were counts filled in?')
for h in ('29.6 The three documents', '29.7 What the entered literatures',
          '29.7.1 The calibration', '29.8 The other claims'):
    s = [i for i, t in enumerate(PP, 1) if h in t]
    print(f'   PP {h!r}: {s}')
    for i in s:
        print(f'      P{i}  {PP[i-1].strip()[:120]}')
pp0 = [i for i, t in enumerate(PP, 1) if '29.6 The three documents' in t]
if pp0:
    a = pp0[0]
    b = next((i for i in range(a + 1, len(PP) + 1)
              if re.match(r'^#{1,6} ', PP[i - 1].strip()) and '29.6' not in PP[i - 1]), a + 1)
    print(f'  --- PP SS29.6 body P{a}-P{b-1} ---')
    for i in range(a, b):
        if PP[i - 1].strip():
            print(f'   P{i}  {PP[i-1].strip()[:150]}')
print('  --- line-for-line: every non-blank unit line present verbatim in PP? ---')
ppset = set(t.strip() for t in PP if t.strip())
miss = [(LO + o, t.strip()) for o, t in enumerate(UNIT) if t.strip() and t.strip() not in ppset]
print(f'  unit non-blank lines {sum(1 for t in UNIT if t.strip())}; NOT found verbatim in PP: {len(miss)}')
for ln, t in miss:
    print(f'   L{ln}  {t[:140]}')

# =============================================================================
head('P8  duplicated-section sweep, and bibliography presence for every attribution')
longs = [(LO + o, t.strip()) for o, t in enumerate(UNIT) if len(t.strip()) > 80]
dup = 0
for ln, t in longs:
    for k in V:
        for i in phrase_sites(V[k], t[:70]):
            if not (k == 'main' and i == ln):
                dup += 1
                print(f'   L{ln} recurs at {k} L{i}')
print(f'  long lines swept {len(longs)}; recurrences {dup}')
print('  --- App F presence for every attribution named in the unit ---')
for name in ('Stahl', 'Wille', 'Yannakakis', 'Habib', 'Nourine', 'Raynaud', 'Thierry',
             'Paschen', 'Götze', 'Dunz', 'Manski', 'Körner', 'Orlitsky', 'Moore',
             'Aitken', 'Seki', 'Ritz', 'Edlén', 'Nesterov'):
    tot = {k: len(phrase_sites(V[k], name)) for k in V}
    appf = [i for i in phrase_sites(M, name) if i > 11380]
    print(f'   {name:<12} ' + '  '.join(f'{k} {v}' for k, v in tot.items()) +
          f'   App-F-range sites {appf}')
print('  --- the two near-identical German titles ---')
for ph in ('Seriengesetze der Linienspektren', 'Seriengesetze der Linienspektra'):
    print(f'   {ph!r}: ' + '  '.join(f'{k} {phrase_sites(V[k], ph)}' for k in ('main', 'reg', 'mc')))

print('\nr2-ch15u complete.')
