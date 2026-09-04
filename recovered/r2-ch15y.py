#!/usr/bin/env python3
"""r2-ch15y - prose batch for chat 115's unit: main L8238-L8346 (SS29.12, ch30 head, SS30.1).

Pointer resolution under BOTH body_range and section_span, resolved to the CLAIM and not the
heading; the U-block structure against the two universals the section opens with; every count
word against its own body; the attributions against ## References AND against R.7; the
antecedent sweep for L8329's "earlier figure of 139"; the digit-bounded numeral sweep across
six volumes; Ruling 45 and Ruling 46; first person; the duplicated-passage sweep; the one C9
census row with its contiguity witness.

EVERY VOLUME IS INDEXED ONCE and all patterns are tested inside that single pass.
"""
import re, importlib.util
from collections import defaultdict

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

# --- owed to r2lib: body_range ------------------------------------------------
# lifted verbatim from r2-ch15v.py (chat 114).  A section's BODY ends at the next heading of
# ANY rank; section_span runs past subsections.  The two DIFFER wherever a section has
# subsections and COINCIDE where it has none - both are reported for every pointer.
def body_range(Mx, sec):
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,6} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


# --- owed to r2lib: left-bounded stem matcher ---------------------------------
# lifted verbatim from r2-ch15t.py (chat 113) via r2-ch15w.py; has_token is letter-bounded on
# BOTH sides, so a stem scores zero on every inflected form.
def has_stem(text, stem):
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(stem), text, re.I))


# --- owed to r2lib: two-line-join phrase sweep, REPAIRED ----------------------
# lifted verbatim from r2-ch15u.py (chat 113).
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


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


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
LO, HI = 8238, 8346
UNIT = M[LO - 1:HI]
UTXT = '\n'.join(UNIT)

# =============================================================================
# ONE INDEX PASS PER VOLUME.
NAMES = ['Kimura', 'Makino', 'Yamada', 'Yoshizumi', 'Helly', 'Dechter', 'van Beek', 'Freuder',
         'Kurucz', 'VALD', 'BRASS', 'Birkhoff']
PHRASES = ['2-decomposability', '2-decomposable', 'row-convex', 'path consistency',
           'decomposability defect', 'reorderability', 'solution density', 'backtrack',
           'targeted attack', 'E1 puncture', 'transfer q', 'monotone envelope',
           'constraint graph', 'proper projections', 'globally consistent']
NUMS = ['139', '384', '101', '2,862', '12,489', '40,887', '110,229', '8,326', '4,163',
        '73,486', '36,743', '363,384', '181,692', '369', '1,105', '2,465', '1,561', '23.40',
        '6.90', '1.05', '2024']
PAT = {n: re.compile(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', re.I) for n in NAMES}
PAT.update({p: re.compile(re.escape(p).replace(r'\ ', r'\s+'), re.I) for p in PHRASES})
PAT.update({n: re.compile(r'(?<![\d,.])' + re.escape(n) + r'(?![\d])') for n in NUMS})
IDX = {k: defaultdict(list) for k in VOL}
FIRST = re.compile(r'(?<![A-Za-z])(I|we|our|us|my|me)(?![A-Za-z])')
first_hits = []
for vk, lines in V.items():
    for i, t in enumerate(lines, 1):
        for key, pat in PAT.items():
            if pat.search(t):
                IDX[vk][key].append(i)
        if vk == 'main' and LO <= i <= HI and FIRST.search(t):
            first_hits.append(i)


def sites(key):
    return {k: IDX[k][key] for k in VOL if IDX[k][key]}


def total(key):
    return sum(len(IDX[k][key]) for k in VOL)


# =============================================================================
head('POINTERS  resolved under BOTH resolvers, and to the CLAIM not the heading')
CLAIMS = [
    ('29.1',    8239, 'forbids the author to make a claim of novelty', ['novel', 'priority', 'claim']),
    ('29.10',   8271, 'physics-vocabulary searches',                   ['vocabulary', 'physic']),
    ('7.1',     8310, 'the constraint system',                         ['constraint']),
    ('7.4',     8310, 'the caps',                                      ['cap']),
    ('12.11.1', 8311, 'the bounds, and three exact sets',              ['exact', 'bound']),
    ('30.2',    8329, 'search hardest when the solution is nearly unique', ['unique', 'hard', 'densit']),
    ('18.4',    8344, 'closure is not determined by its proper projections', ['projection', 'closure']),
]
for sec, site, claim, stems in CLAIMS:
    br, ss = body_range(M, sec), section_span(M, sec)
    same = 'COINCIDE' if br == ss else 'DIFFER'
    print(f'\n  SS{sec}  cited at L{site} for: {claim}')
    print(f'    body_range={br}  section_span={ss}  -> {same}')
    for label, rng in (('body', br), ('span', ss)):
        if rng is None:
            print(f'    {label}: heading NOT FOUND'); continue
        txt = '\n'.join(M[rng[0]:rng[1] - 1])          # excludes the heading line itself
        hits = {s: has_stem(txt, s) for s in stems}
        print(f'    {label} L{rng[0]}-L{rng[1]-1}, heading excluded: {hits}  '
              f'{"CARRIES" if any(hits.values()) else "*** CARRIES NONE ***"}')

print('\n  A.18 (L8293) - heading_line returns None for lettered headings; line window used:')
ap = [i for i, t in enumerate(M, 1) if re.match(r'^#{2,4}\s*A\.18(?!\d)', t.strip())]
print(f'    heading_line(M, "A.18") = {heading_line(M, "A.18")}   window scan -> {ap}')
if ap:
    end = next((i for i in range(ap[0] + 1, len(M) + 1) if re.match(r'^#{1,6} ', M[i - 1].strip())),
               len(M) + 1)
    t = '\n'.join(M[ap[0]:end - 1])
    print(f'    A.18 body L{ap[0]}-L{end-1}: '
          f'{{join: {has_stem(t, "join")}, meet: {has_stem(t, "meet")}, '
          f'triangle: {has_stem(t, "triangl")}, proof/proved: {has_stem(t, "prov")}}}')
    print(f'    heading: {M[ap[0]-1].strip()[:88]}')

print('\n  Chapter 15 (L8317, L8322) "recovers Lambda\'s order from its own cells":')
c15 = heading_line(M, '15')
sp15 = section_span(M, '15')
t15 = '\n'.join(M[c15:sp15[1] - 1]) if c15 else ''
print(f'    chapter 15 heading L{c15}: {M[c15-1].strip()[:70] if c15 else "NOT FOUND"}')
print(f'    span {sp15}  {{recover: {has_stem(t15, "recover")}, order: {has_stem(t15, "order")}, '
      f'tree: {has_stem(t15, "tree")}}}')

# =============================================================================
head('THE U-BLOCKS against the two universals L8241-L8243 opens with')
# "Each carries a definition, the search already run, the test that would confirm it, and the
# observation that would destroy it."  And: "A result with no stated falsifier is not on this list."
starts = [i for i in range(LO, HI + 1) if re.match(r'^\s*\*\*U\d+\b', M[i - 1])]
vc = next(i for i in range(LO, HI + 1) if 'Verification common' in M[i - 1])
bounds = starts + [vc]
print(f'  U-blocks found at {starts}; block list ends at L{vc}')
rows = []
for n, s in enumerate(starts):
    e = bounds[n + 1]
    body = '\n'.join(M[s - 1:e - 1])
    r = dict(
        u=re.match(r'^\s*\*\*(U\d+)', M[s - 1]).group(1), line=s,
        definition=bool(re.search(r'\*Definition\.\*', body)),
        search=bool(re.search(r'\*(Searched|Located)\.\*', body)),
        test=bool(re.search(r'\*Test[^*]*\.\*', body)),
        falsifier=bool(re.search(r'\*Falsifier\.\*', body)),
        located=bool(re.search(r'\bLOCATED\b', body)))
    rows.append(r)
for r in rows:
    miss = [k for k in ('definition', 'search', 'test', 'falsifier') if not r[k]]
    print(f"  {r['u']} L{r['line']:5d}  definition={r['definition']}  search={r['search']}  "
          f"test={r['test']}  falsifier={r['falsifier']}  LOCATED={r['located']}"
          f"{'   *** MISSING: ' + ', '.join(miss) + ' ***' if miss else ''}")
print(f"\n  falsifier on every block: {all(r['falsifier'] for r in rows)}  "
      f"-> L8243's universal HOLDS" if all(r['falsifier'] for r in rows) else '')
print(f"  all four elements on every block: {all(all(r[k] for k in ('definition','search','test','falsifier')) for r in rows)}")
print(f"  blocks printed: {len(rows)}   blocks marked LOCATED: "
      f"{sum(1 for r in rows if r['located'])}   still unlocated: "
      f"{len(rows) - sum(1 for r in rows if r['located'])}")
print(f"  heading L8238 count word: 'Five unlocated results' -> "
      f"{'MATCHES the body' if len(rows) - sum(1 for r in rows if r['located']) == 5 else '*** the body prints ' + str(len(rows)) + ' results, ' + str(len(rows) - sum(1 for r in rows if r[chr(39)+'located'+chr(39)] if False) ) + ' ***'}")

# =============================================================================
head('COUNT WORDS against their own bodies')
five_pres = re.search(r'Five presentations were tried here and all failed\s*[-\u2014]\s*(.+?)\.',
                      ' '.join(M[8272:8275]), re.S)
if five_pres:
    items = [x.strip() for x in re.split(r',| and ', five_pres.group(1)) if x.strip()]
    print(f'  L8273 "Five presentations ... 2S\', parity alone, the min-cap, pair count, '
          f'and (2S,2L,2J)" -> {len(items)} items: {items}  '
          f'{"MATCHES" if len(items) == 5 else "*** MISMATCH ***"}')
b1211 = body_range(M, '12.11.1'); s1211 = section_span(M, '12.11.1')
t1211 = '\n'.join(M[b1211[0]:b1211[1] - 1]) if b1211 else ''
t1211s = '\n'.join(M[s1211[0]:s1211[1] - 1]) if s1211 else ''
print(f'  L8311 "the three exact sets SS12.11.1 now states": body {b1211} span {s1211} '
      f'{"COINCIDE" if b1211 == s1211 else "DIFFER"}')
for lab, tt in (('body', t1211), ('span', t1211s)):
    print(f'    {lab}: "exact" x{has_stem(tt, "exact")}  "three" x{has_stem(tt, "three")}  '
          f'exact-set lines: {[l.strip()[:58] for l in tt.split(chr(10)) if re.search("exact", l, re.I)][:4]}')
cellnums = re.findall(r'(?<![\d,.])\d[\d,]*(?![\d])', M[8311])
print(f'  L8312 cell-count list -> {cellnums}  ({len(cellnums)} figures)')
print(f'  L8326 "384 of 384" / L8330 "101 of the 384": '
      f'384 sites in six volumes {sites("384")};  101 sites {sites("101")}')

# =============================================================================
head('ATTRIBUTIONS against ## References AND against R.7')
rs = next(i for i, t in enumerate(M, 1) if t.strip() == '## References')
re_end = next((i for i in range(rs + 1, len(M) + 1)
               if re.match(r'^#{1,2} ', M[i - 1].strip())), len(M) + 1)
r7 = [i for i in range(rs, re_end) if re.match(r'^#{3,4}\s*R\.7\b', M[i - 1].strip())]
r7s = r7[0] if r7 else None
r7e = next((i for i in range(r7s + 1, re_end) if re.match(r'^#{1,4} ', M[i - 1].strip())),
           re_end) if r7s else None
REFT = '\n'.join(M[rs:re_end - 1])
R7T = '\n'.join(M[r7s:r7e - 1]) if r7s else ''
print(f'  ## References L{rs}-L{re_end-1};  R.7 L{r7s}-L{r7e-1 if r7e else "?"}: '
      f'{M[r7s-1].strip()[:60] if r7s else "NOT FOUND"}')
for n in ['Kimura', 'Makino', 'Yamada', 'Yoshizumi', 'Helly', 'Dechter', 'van Beek', 'Freuder']:
    inunit = len(PAT[n].findall(UTXT))
    print(f'  {n:11s} unit x{inunit}  refs x{len(PAT[n].findall(REFT))}  R.7 x{len(PAT[n].findall(R7T))}  '
          f'six-volume sites {sites(n)}')
for p in ['2-decomposab', 'row-convex', 'path consistency']:
    print(f'  phrase {p!r}: unit x{has_stem(UTXT, p)}  refs x{has_stem(REFT, p)}  '
          f'R.7 x{has_stem(R7T, p)}')

# =============================================================================
head('L8329  "The earlier figure of 139" - antecedent sweep')
print(f'  139 sites, digit-bounded, six volumes: {sites("139")}')
for vk, ls in sites('139').items():
    for i in ls:
        print(f'    {vk} L{i}: {V[vk][i-1].strip()[:96]}')
print('  a reorderable-instance count of 139 anywhere other than L8329: '
      f'{[ (vk,i) for vk,ls in sites("139").items() for i in ls if i != 8329 and re.search(r"instanc|reorder|sample", V[vk][i-1], re.I)] or "NONE"}')

# =============================================================================
head('NUMERAL SWEEP, digit-bounded, six volumes')
for n in NUMS:
    s = sites(n)
    print(f'  {n:9s} total {total(n):3d}  {s}')

# =============================================================================
head('RULING 45 / RULING 46 / FIRST PERSON / DUPLICATED PASSAGE')
R45 = ['earlier figure', 'were re-drawn', 'now states', 'printed here', 'tried here',
       'done to 20 here', 'this book', 'the author', 'left open', 'should say so',
       'the guess that preceded it', 'is not on this list']
for p in R45:
    hits = [i for i in phrase_sites(M, p) if LO <= i <= HI]
    if hits:
        for i in hits:
            print(f'  R45? L{i}: {M[i-1].strip()[:92]}')
R46 = ['.py', 'BUILD', 'build.py', 'script', 'tower-2', 'register.py']
r46hits = [(p, [i for i in phrase_sites(M, p) if LO <= i <= HI]) for p in R46]
print(f'  Ruling 46 tokens in unit: {[(p, h) for p, h in r46hits if h] or "ZERO"}')
print(f'  first-person pronouns in unit: {first_hits or "ZERO"}')
long_unit = [(i, M[i - 1].strip()) for i in range(LO, HI + 1) if len(M[i - 1].strip()) > 60]
dup = []
for i, t in long_unit:
    for vk, lines in V.items():
        for j, u in enumerate(lines, 1):
            if u.strip() == t and not (vk == 'main' and j == i):
                dup.append((i, vk, j))
print(f'  duplicated-passage sweep: {len(dup)} of {len(long_unit)} long lines recur  '
      f'{dup if dup else ""}')

# =============================================================================
head('CENSUS ROW IN RANGE, with its contiguity witness')
import csv
rows = list(csv.DictReader(open(MEM + 'DEFECT-CENSUS.tsv', encoding='utf-8'), delimiter='\t'))
mn = [r for r in rows if r['member'] == 'main']


def ln(r):
    try:
        return int(r['line'])
    except Exception:
        return -1


inr = [r for r in mn if LO <= ln(r) <= HI]
ids = sorted(int(r['id']) for r in inr)
print(f'  rows keyed member="main" with line in [{LO},{HI}]: {len(inr)}  ids {ids}')
for r in inr:
    print(f"    id {r['id']}  L{r['line']}  {r['class']}  token={r['item']!r}")
    print(f"      line: {M[int(r['line'])-1].strip()[:92]}")
byid = {int(r['id']): r for r in rows}
for i in (ids[0] - 1, ids[-1] + 1):
    r = byid.get(i)
    print(f'  witness id {i}: '
          f'{"member=" + r["member"] + " L" + str(r["line"]) + " " + r["class"] if r else "ABSENT"}')
print(f'  ids contiguous either side: {all(i in byid for i in (ids[0]-1, ids[-1]+1))}')

# =============================================================================
head('UNIVERSALS AND SUPERLATIVES IN THE UNIT')
for p in ['universally known', 'One suffices', 'at every cap', 'nothing else', 'no proof',
          'not removable', 'least likely to be general', 'zero defect', 'and nothing else']:
    for i in [i for i in phrase_sites(M, p) if LO <= i <= HI]:
        print(f'  L{i}  {p!r}: {M[i-1].strip()[:88]}')
print('\n  L8309-L8311 "reproducible from the definitions printed in this book and nothing '
      'else: SS7.1, SS7.4, SS12.11.1" - the list at L8312 includes 1,561 = Lambda9\', which '
      'needs the constraint 2S\' <= 2f+1:')
for sec in ('7.1', '7.4', '12.11.1'):
    br = body_range(M, sec); ss = section_span(M, sec)
    t = '\n'.join(M[ss[0]:ss[1] - 1]) if ss else ''
    print(f"    SS{sec} span {ss}: \"2S'\" x{len(re.findall(chr(39)+r'2S.\u2032|2S\u2032'+chr(39), t))}  "
          f"'2f+1' x{t.count('2f+1')}  'Pauli' x{has_stem(t, 'Pauli')}")
pauli = [(vk, i) for vk in VOL for i, t in enumerate(V[vk], 1) if '2f+1' in t]
print(f"    sites printing '2f+1' in six volumes: {pauli[:12]}  (total {len(pauli)})")
