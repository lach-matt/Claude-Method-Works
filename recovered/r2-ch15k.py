#!/usr/bin/env python3
"""r2-ch15k — prose batch for the chat-108 section read: main §28.7.3, L7559-L7643.

Every pointer test carries a claim-locator AND a home-locator: a bare absence is not a finding
until the claim is located where it does live.  Register entries are located by an explicit
numeral heading match, because heading_line requires a trailing space after the number and the
Register's bare '### 96' returns None; an entry's headline is quoted before it is cited.
Prints & Proofs is read as the original-input witness (Ruling 56).

G1 fault, chat 108: the first draft resolved each pointer over body_range alone and returned five
ABSENT verdicts.  A section pointer names the section INCLUDING its subsections, so the test must
run over section_span as well; body_range gave §23.10 four lines and §31.3 two.  Both are printed
and an absence is recorded only when the claim is missing under BOTH.
"""
import importlib.util, re

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span = r2lib.heading_line, r2lib.section_span
has_token, enclosing = r2lib.has_token, r2lib.enclosing

VOL = {'main': 'The_Method_1_6-2.md',
       'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
LINES = {k: open(MEM + v, encoding='utf-8').read().split('\n') for k, v in VOL.items()}
M = LINES['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
A, B = 7559, 7644


def body_range(Ms, sec):
    """OWED TO r2lib. Heading -> next heading of ANY rank."""
    s = heading_line(Ms, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Ms) + 1):
        if re.match(r'^#{1,6}\s', Ms[i - 1]):
            return (s, i)
    return (s, len(Ms) + 1)


def find(Ms, pat, lo=1, hi=None, flags=re.I):
    hi = hi or len(Ms) + 1
    return [i for i in range(lo, min(hi, len(Ms) + 1)) if re.search(pat, Ms[i - 1], flags)]


def reg_entry(n):
    """Register entry N: bare '### N' or grouped '### N, ...'.  heading_line returns None here."""
    R = LINES['reg']
    hits = find(R, r'^#{1,4}\s*%d\s*$' % n, flags=0) + find(R, r'^#{1,4}\s*%d\s*,' % n, flags=0)
    out = []
    for h in sorted(set(hits)):
        head = ''
        for j in range(h + 1, min(h + 6, len(R) + 1)):
            if R[j - 1].strip():
                head = R[j - 1].strip(); break
        out.append((h, R[h - 1].strip(), head[:150]))
    return out


print('=' * 78)
print('r2-ch15k  prose batch  main SS28.7.3')
print('=' * 78)

# ---------------------------------------------------------------- G1 pointers, both resolvers
print('\nG1  every section pointer in the unit, over body_range AND section_span, with a home')
ptrs = sorted({m for i in range(A, B) for m in re.findall(r'§\s*(\d+(?:\.\d+)*)', M[i - 1])},
              key=lambda s: [int(x) for x in s.split('.')])
CLAIM = {
    '2.15': (r'bound', 'tabulates the ten that became bounds'),
    '6.2': (r'janet', "§6.2's Janet table is that test"),
    '16.7.2': (r'fabricat', 'description of a coherent fabrication'),
    '17.2': (r'\bE2\b', "§17.2's E2 forbids arithmetically impossible cells"),
    '23.10': (r'oscillat', 'said matched-order V oscillates about the floor'),
    '23.10.1': (r'sign', 'says read the sign from the data'),
    '23.10.4': (r'admissib', 'the admissibility rule was written here'),
    '23.14.1': (r'hill', 'the Hill-radius correlation measured here'),
    '30.3': (r'reorder', 'reorderability problem'),
    '30.3.1': (r'characteris', 'the characterisation ten of the seventeen produced'),
    '30.4': (r'audit', 'Chapter 30 re-audited against its own §30.4'),
    '31.1': (r'oscillat', 'said matched-order V oscillates about the floor'),
    '31.2': (r'\blist\b|object', 'an object list, missing five'),
    '31.3': (r'pareto', 'Pareto statistic stated against 473.8 million'),
}
for p in ptrs:
    br, sp = body_range(M, p), section_span(M, p)
    pat, why = CLAIM.get(p, (None, ''))
    cite = find(M, r'§\s*' + re.escape(p) + r'(?!\d)', A, B)
    hb = find(M, pat, br[0], br[1]) if (br and pat) else []
    hs = find(M, pat, sp[0], sp[1]) if (sp and pat) else []
    verdict = 'FOUND-body' if hb else ('FOUND-span' if hs else 'ABSENT-both')
    print(f'    §{p:<8} in-unit L{cite}  body {br} span {sp}  /{pat}/ body L{hb[:4]} '
          f'span L{hs[:4]}  {verdict}')
    if not hb and not hs:
        home = {k: find(v, pat)[:4] for k, v in LINES.items()}
        print(f'          claim {why!r} lives at: '
              + '  '.join(f'{k}=L{h}' for k, h in home.items() if h))
        for h in home.get('main', [])[:3]:
            print(f'          main L{h} sits in {enclosing(M, h)}: {M[h-1].strip()[:88]!r}')

# ---------------------------------------------------------------- G2 non-section references
print('\nG2  the unit\'s non-section references')
for tag, pat, where in (('Proposition 23.1', r'Proposition\s*23\.1\b', 'the floor V oscillates about'),
                        ('Figure 15.3', r'Figure\s*15\.3\b', 'withdrawn; floor V = 2 through 0.24'),
                        ('P20', r'\bP20\b', 'forbids the rest'),
                        ('Q9', r'\bQ9\b', "Q9's original conclusion was right"),
                        ('E2', r'\bE2\b', 'the line E2 forbids'),
                        ('L2', r'\bL2\b', 'differences alternate the other way')):
    row = {k: find(v, pat) for k, v in LINES.items()}
    inu = [i for i in range(A, B) if re.search(pat, M[i - 1])]
    print(f'    {tag:<16} in-unit L{inu}  ' + '  '.join(f'{k}={len(row[k])}' for k in VOL)
          + f'   [{where}]')
    for h in row['main'][:6]:
        if not (A <= h < B):
            print(f'          main L{h} in {enclosing(M, h)}: {M[h-1].strip()[:80]!r}')

# ---------------------------------------------------------------- G3 the register self-citations
print('\nG3  the two closing notes that cite the register about itself')
print(f'    L7601-02: {" ".join(M[7600].split()+M[7601].split())[:150]!r}')
print(f'    L7616-17: {" ".join(M[7615].split()+M[7616].split())[:150]!r}')
print('    READING 1 — the Register compendium (headline quoted before it is cited):')
for n in (1, 3, 110, 119):
    e = reg_entry(n)
    if not e:
        print(f'      entry {n:>3}: NOT LOCATED')
    for h, hd, headline in e:
        print(f'      entry {n:>3}: reg L{h} {hd!r}')
        print(f'                headline {headline!r}')
print('    READING 2 — chapter 28\'s own withdrawal numbering:')
ITEM = re.compile(r'^\s*\*{0,2}(\d+)(?:\s*[\u2013\u2014-]\s*(\d+))?\.\s')
ch = section_span(M, '28')
own = {}
for i in range(ch[0] + 1, ch[1]):
    m = ITEM.match(M[i - 1])
    if m:
        lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
        for n in range(lo, hi + 1):
            own.setdefault(n, []).append(i)
for n in (1, 3, 110, 119):
    print(f'      withdrawal item {n:>3}: printed at L{own.get(n, [])}   '
          f'{"NOT PRINTED (the 1-48 gap, 15g-04)" if n not in own else "printed in this section"}')
print('    the phrase itself, across six volumes:')
for k, v in LINES.items():
    hh = find(v, r'past the number beside it')
    if hh:
        print(f'      {k} L{hh}')

# ---------------------------------------------------------------- G4 Prints & Proofs witness
print('\nG4  Prints & Proofs (Ruling 56): the heading, and the twelve missing numerals')
ph = find(PP, r'^#{2,4}\s*28\.7\.3\b', flags=0); pn = find(PP, r'^#{2,4}\s*28\.7\.4\b', flags=0)
for p in ph:
    print(f'    PP P{p}: {PP[p-1][:118]!r}')
print(f'    volume  L{A}: {M[A-1][:118]!r}')
if ph and pn:
    a, b = ph[-1], pn[-1]
    cov = []
    for i in range(a + 1, b):
        m = ITEM.match(PP[i - 1])
        if m:
            lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
            cov += list(range(lo, hi + 1))
    u = sorted(set(cov))
    print(f'    PP body P{a+1}-P{b-1}: numerals {min(u)}-{max(u)}, distinct {len(u)}, '
          f'missing {[n for n in range(min(u), max(u)+1) if n not in u]}')
    print(f'    PP heading is the placeholder form: '
          f'{"From more from" in PP[a-1]}   volume prints a count word: '
          f'{"Seventy-five" in M[A-1]}')
for n in (98, 99, 105, 106, 139, 140, 144, 145):
    print(f'    numeral {n:>3}: PP head P{find(PP, r"^\s*\*{0,2}%d[.\u2013]" % n, flags=0)[:3]}  '
          f'main head L{find(M, r"^\s*\*{0,2}%d[.\u2013]" % n, flags=0)[:3]}')

# ---------------------------------------------------------------- G5 Ruling 45 / 46 sweeps
print('\nG5  Ruling 45 (build/editorial-process remarks) and Ruling 46 (internal references)')
for pat in ('retained in the compendium', r'\bsession\b', r'\bin one hour\b', r'\bfor an hour\b',
            r'\bmessage\b', r'collaborator', r'(?<![A-Za-z])I(?![A-Za-z])',
            r'the person operating it'):
    for i in [i for i in range(A, B) if re.search(pat, M[i - 1])]:
        seg = re.search(pat, M[i - 1]); s = max(0, seg.start() - 40)
        print(f'    R45 /{pat}/ L{i}: ...{M[i-1][s:seg.end()+44].strip()!r}')
for pat in (r'\.py\b', r'BUILD\d+', r'\bchat\s*\d+', r'\bregister\s+\d+', r'\bW-\d+', r'\bhandoff'):
    print(f'    R46 /{pat}/ in unit: L{[i for i in range(A, B) if re.search(pat, M[i-1], re.I)]}')

# ---------------------------------------------------------------- G6 retired-basis class
print('\nG6  the retired-basis class (docket 15): "earlier version" forms in main')
for pat in (r'an earlier version', r'the earlier version', r'earlier version'):
    print(f'    /{pat}/ L{find(M, pat)}')
print(f'    in-unit L{[i for i in range(A, B) if re.search("earlier version", M[i-1], re.I)]}  '
      f'(docket 15 carried eight sites, all "An earlier version")')

# ---------------------------------------------------------------- G7 the three C9 census rows
print('\nG7  census rows 1163 / 1164 / 1165 — the flagged token in its own sentence')
for ln in (7567, 7569, 7637):
    for mm in re.finditer(r'(?<![A-Za-z])never(?![A-Za-z])', M[ln - 1], re.I):
        s = max(0, mm.start() - 76)
        print(f'    L{ln}: ...{M[ln-1][s:mm.end()+80].strip()!r}')
print('    universal test 1 — is the index recorded as deceived anywhere?')
for k, v in LINES.items():
    print(f'      {k}: L{find(v, r"index.{0,24}deceiv")[:6]}')
print('    universal test 2 — is the Hill-radius correlation carried into §31.1?')
b311, s311 = body_range(M, '31.1'), section_span(M, '31.1')
print(f'      §31.1 body {b311} span {s311}; /hill/ body L{find(M, "hill", *b311)} '
      f'span L{find(M, "hill", *s311)}; /23.14.1/ span L{find(M, re.escape("23.14.1"), *s311)}')
print('    universal test 3 — does §31.2 carry an object list?')
b312, s312 = body_range(M, '31.2'), section_span(M, '31.2')
print(f'      §31.2 body {b312} span {s312}; lines in span {s312[1]-s312[0]}')
for i in range(s312[0], min(s312[1], s312[0] + 4)):
    print(f'      L{i}: {M[i-1].strip()[:96]!r}')

# ---------------------------------------------------------------- G8 counted-subset sentences
print('\nG8  every counted-subset sentence in the unit (DEF-107 item 6 class)')
PAT = (r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|seventeen|twenty)'
       r'\s+(?:of\s+(?:these|the|them|its)|lists|produced|constraints)')
for i in range(A, B):
    for mm in re.finditer(PAT, M[i - 1], re.I):
        s = max(0, mm.start() - 30)
        print(f'    L{i}: ...{M[i-1][s:mm.end()+92].strip()!r}')

# ---------------------------------------------------------------- G9 formatting sweeps
print('\nG9  formatting sweeps carried into every unit')
print(f'    lower-case section openings: L{[i for i in range(A, B) if re.match(r"^#{2,4}\s+[a-z]", M[i-1])]}')
long_lines = [(i, M[i - 1].strip()) for i in range(A, B) if len(M[i - 1].strip()) > 90]
seen = {}
for i, t in long_lines:
    seen.setdefault(t, []).append(i)
hitc = 0
for t, ii in seen.items():
    other = [j for j in range(1, len(M) + 1) if j not in ii and M[j - 1].strip() == t]
    if other:
        hitc += 1; print(f'    L{ii} also at L{other[:4]}')
print(f'    duplicated-line sweep (DEF-105 item 1): {hitc} of {len(seen)} long lines recur')
mid = [i for i in range(A, B - 1) if M[i - 1].strip() and M[i].strip() == ''
       and not M[i - 1].rstrip().endswith(('.', '!', '?', ':', '**', '*', '—'))]
print(f'    block ends without terminal punctuation: L{mid}')
for i in mid:
    print(f'      L{i}: {M[i-1].strip()[-60:]!r}  ->  L{i+2}: {M[i+1].strip()[:60]!r}')

# ---------------------------------------------------------------- G10 single-witness figures
print('\nG10  witnesses per figure across the six volumes')
for s in ('1,548', '652', '560', '1,156', '241', '570', '593', '956', '473.8', '495,515',
          '71.8', '0.606', '0.31', '0.24'):
    per = {k: len(re.findall(r'(?<![\d.,])' + re.escape(s) + r'(?![\d])', '\n'.join(v)))
           for k, v in LINES.items()}
    tot = sum(per.values())
    print(f'    {s:>8}: {tot} site(s)  ' + '  '.join(f'{k}={per[k]}' for k in VOL)
          + ('   SINGLE-WITNESS' if tot <= 1 else ''))
print('\nEND r2-ch15k')
