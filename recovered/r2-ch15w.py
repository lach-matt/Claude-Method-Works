#!/usr/bin/env python3
"""r2-ch15w - prose batch for chat 114's unit: main L8098-L8221 (SS29.9-SS29.11.2).

Pointer resolution under BOTH body_range and section_span; every attribution in the
unit against Appendix F; single-witness site counts across six volumes; count words
against their own bodies; the Ruling 45 and Ruling 46 sweeps; first person; the
duplicated-passage sweep, including SS14.1 against SS29.11; the three C9 census rows;
universals; the two-line-join phrase sweep (repaired form).

EVERY VOLUME IS INDEXED ONCE and all patterns are tested inside that single pass -
chat 113's prose batch timed out under gate.py bank at 51 x 6 full volume passes.
"""
import re, importlib.util
from collections import defaultdict

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
LO, HI = 8098, 8221
UNIT = M[LO - 1:HI]


# --- owed to r2lib: body_range ----------------------------------------------
# lifted verbatim from r2-ch15t.py (chat 113)
def body_range(Mx, sec):
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,6} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


# --- owed to r2lib: left-bounded stem matcher --------------------------------
# lifted verbatim from r2-ch15t.py (chat 113); has_token is letter-bounded on BOTH
# sides, so a stem scores zero on every inflected form.
def has_stem(text, stem):
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(stem), text, re.I))


# --- owed to r2lib: two-line-join phrase sweep, REPAIRED ---------------------
# lifted verbatim from r2-ch15u.py (chat 113).  The r2-ch15r/s form double-reports.
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


# =============================================================================
# ONE INDEX PASS PER VOLUME.  Every name and phrase below is tested inside this
# single loop; nothing rescans a volume afterwards.
NAMES = ['Bergman', 'Baker', 'Pixley', 'Racah', 'Birkhoff', 'Kurucz', 'VALD', 'BRASS',
         'Sansonetti', 'Kaufman', 'Kramida', 'Martin', 'Montanari', 'Dechter', 'Hasse',
         'NIST ASD', 'QSAR']
PHRASES = ['double-projection', 'majority term', 'partial order in chemistry',
           'unobserved lines', 'missing lines', 'staircase', 'seniority',
           'jK coupling', 'particle-hole', 'E(search)', 'referee flag 5',
           'parent term', 'coupling parent', 'specificity, not sensitivity']
PAT = {n: re.compile(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', re.I) for n in NAMES}
PAT.update({p: re.compile(re.escape(p).replace(r'\ ', r'\s+'), re.I) for p in PHRASES})
IDX = {k: defaultdict(list) for k in VOL}
for k, lines in V.items():
    for i, t in enumerate(lines, 1):
        if not t.strip():
            continue
        for key, rx in PAT.items():
            if rx.search(t):
                IDX[k][key].append(i)

# =============================================================================
head('W1  every section pointer in the unit, under BOTH resolvers')
ptr = defaultdict(list)
for off, t in enumerate(UNIT):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', t):
        ptr[m.group(1)].append(LO + off)
for sec in sorted(ptr, key=lambda s: [int(x) for x in s.split('.')]):
    br, sp = body_range(M, sec), section_span(M, sec)
    same = 'COINCIDE' if br == sp else 'DIFFER'
    print(f'  ->SS{sec:<8} cited from {ptr[sec]}   body_range {br}   section_span {sp}   {same}')
    if br:
        print(f'      target heading: {M[br[0]-1].strip()[:86]}')
print('  chapter/appendix pointers in the unit:')
for m in sorted(set(re.findall(r'Appendix [A-F]|Chapter \d+|A\.\d+', '\n'.join(UNIT)))):
    print(f'    {m:14s} lines {[LO + i for i, t in enumerate(UNIT) if m in t]}')

# =============================================================================
head('W2  every attribution in the unit against Appendix F (the 15m-07 sweep)')
fs = None
for i, t in enumerate(M, 1):
    if re.match(r'^##\s*Appendix F', t.strip()):
        fs = i
fe = len(M) + 1
for i in range(fs + 1, len(M) + 1):
    if re.match(r'^##\s', M[i - 1].strip()) and i > fs:
        fe = i
        break
print(f'  Appendix F spans main L{fs}-L{fe - 1}')
FA = '\n'.join(M[fs:fe - 1])
for n in NAMES:
    inF = len(re.findall(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', FA, re.I))
    unit = [i for i in IDX['main'][n] if LO <= i <= HI]
    tot = sum(len(IDX[k][n]) for k in VOL)
    flag = '' if inF else '   <-- NO APPENDIX F ENTRY'
    if unit:
        print(f'  {n:12s} unit {unit}   AppF hits {inF}   six-volume sites {tot}{flag}')

# =============================================================================
head('W3  single-witness sweep: six-volume site counts for the unit\'s names')
for n in NAMES:
    if not [i for i in IDX['main'][n] if LO <= i <= HI]:
        continue
    per = {k: len(IDX[k][n]) for k in VOL}
    tot = sum(per.values())
    mark = '   <-- SINGLE WITNESS' if tot == 1 else ''
    print(f'  {n:12s} total {tot:4d}   ' + ' '.join(f'{k}:{v}' for k, v in per.items()) + mark)

# =============================================================================
head('W4  count words against their own bodies')
CW = [('Two searches were run', 8109, 8112, r'one for '),
      ('Two categories entered', 8152, 8178, r'\*\*(Quantum mechanics|Astrophysics)'),
      ('two failure modes by name', 8166, 8171, r'\*(Missing lines|\*Unobserved lines)'),
      ('Ten tested, ten pass', 8189, 8193, r'ten|Ten')]
for label, a, b, rx in CW:
    hits = [i for i in range(a, b + 1) if re.search(rx, M[i - 1])]
    print(f'  "{label}" L{a}-L{b}: constituent lines {hits}')
    for i in hits[:4]:
        print(f'      L{i}: {M[i-1].strip()[:92]}')
print('  "The three documents and one section" L8100 - names them in SS29.6 (read chat 113):')
for i in range(8029, 8041):
    if re.search(r'^\s*[-*]|document', M[i - 1], re.I):
        print(f'      L{i}: {M[i-1].strip()[:92]}')

# =============================================================================
head('W5  Ruling 45 (process remarks) and Ruling 46 (script / file names); first person')
R45 = ['was attempted rather than deferred', 'could not be addressed through the interface',
       'requires registration', 'did not happen', 'was retrieved', 'this chapter was written',
       'defined instead of discarded', 'the run was not looking for', 'this book could do']
for p in R45:
    s = phrase_sites(UNIT, p)
    if s:
        for i in s:
            print(f'  R45? L{LO - 1 + i}: {UNIT[i-1].strip()[:96]}')
R46 = [r'\.py\b', r'BUILD\d+', r'gfall', r'register \d', r'\bscript\b']
for p in R46:
    for i, t in enumerate(UNIT, 1):
        if re.search(p, t):
            print(f'  R46? /{p}/ L{LO - 1 + i}: {t.strip()[:92]}')
fp = [(LO - 1 + i, t.strip()[:80]) for i, t in enumerate(UNIT, 1)
      if re.search(r'(?<![A-Za-z])(I|we|our|us|my)(?![A-Za-z])', t)]
print(f'  first-person pronoun sites in the unit: {[l for l, _ in fp]}')

# =============================================================================
head('W6  duplicated-passage sweep (DEF-105 item 1), and SS14.1 against SS29.11')
subst = [(LO + i, t) for i, t in enumerate(UNIT) if len(t.strip()) > 90]
print(f'  substantive long lines in the unit: {len(subst)}')
dup = 0
KEYS = {}
for ln, t in subst:
    key = re.sub(r'[^a-z ]', '', t.lower())
    key = ' '.join(key.split()[:9])
    if len(key) > 30:
        KEYS[key] = ln
for k, lines in V.items():
    for i, t in enumerate(lines, 1):
        key = ' '.join(re.sub(r'[^a-z ]', '', t.lower()).split()[:9])
        if key in KEYS and not (k == 'main' and i == KEYS[key]):
            print(f'  RECURS  unit L{KEYS[key]}  also {k} L{i}: {t.strip()[:74]}')
            dup += 1
print(f'  duplicated-section sweep: {dup} of {len(subst)} substantive long lines recur')
print('  SS14.1 (L3682-3710) against SS29.11 (L8123-8151), by shared claim:')
for a, b in ((3686, 8132), (3691, 8135), (3708, 8143), (3709, 8144)):
    print(f'    ch14 L{a}: {M[a-1].strip()[:74]}')
    print(f'    ch29 L{b}: {M[b-1].strip()[:74]}')

# =============================================================================
head('W7  the three C9 census rows in range, tested not assumed')
for cid, ln in (('1175', 8140), ('1176', 8182), ('1177', 8215)):
    print(f'  {cid}  L{ln}: {M[ln-1].strip()[:100]}')
print('  1175 asserts the book never claimed novelty.  Priority/novelty claims in the main volume:')
for p in ('claims priority', 'is not new mathematics', 'new mathematics', 'not first',
          'claimed novelty', 'first to'):
    s = phrase_sites(M, p)
    if s:
        print(f'    "{p}": main {s[:8]}')

# =============================================================================
head('W8  universals and superlatives in the unit (docket 19)')
UNIV = ['nothing else', 'the only one it can', 'every index', 'must change 2S by exactly one',
        'none is unexplained', 'in every index', 'is doubly occupied', 'stronger position',
        'systematically unreachable', 'a hard ceiling', 'about half']
for p in UNIV:
    s = phrase_sites(UNIT, p)
    for i in s:
        print(f'  L{LO - 1 + i}: {UNIT[i-1].strip()[:98]}')

# =============================================================================
head('W9  the withdrawn-figure sweep (15m-01 class) on this unit\'s cited figures')
print('  L8189 cites Appendix B for 153 channels.  Appendix B\'s own following section:')
for i in (10169, 10195, 10203, 10205, 10209):
    print(f'    L{i}: {M[i-1].strip()[:98]}')
print('  sc totals line, the arbiter for every species figure:')
print(f'    sc L900: {V["sc"][899].strip()[:98]}')
print('  E(search) sites, unit then six volumes:')
for k in VOL:
    s = IDX[k]['E(search)']
    if s:
        print(f'    {k}: {s[:12]}')
