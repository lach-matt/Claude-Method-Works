#!/usr/bin/env python3
"""r2-ch15i — prose / pointer batch for main L7458-L7558 (§28.6-§28.7.2).

Chat 107.  Imports heading_line / section_span / has_token / enclosing from r2lib by path;
copies nothing; reads MEMBERS and the Prints & Proofs original (as r2-ch15e does), never a
bundle; passes the resolvers the LINE LIST.  Every pointer is resolved to the CLAIM and, where it
fails, the claim's true home is located.  Phrases are swept on the two-line join as well as raw.

Fault log (self-caught, rewritten before banking):
  * G1 first form tested a target for one guessed token and printed a bare absence.  A missing
    token is not a missing claim: the test now carries, per pointer, the claim token, the rival
    section, and the located home, so an absence is reported with what was swept.
  * G3 first form ran an item block to the next item start, which swallowed the indented closing
    note of §28.7.1 and made item 62 appear to cite item 58 (the note does).  Blocks now stop at
    an indented note, and a numeral inside the item's own printed range, or followed by a unit
    noun ("60 cells"), is not a cross-reference.
"""
import importlib.util, os, re

H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOL = {'main': 'The_Method_1_6-2.md',
       'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
M = {k: r2lib.read_member(v).split('\n') for k, v in VOL.items()}
main = M['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
LO, HI = 7458, 7558

# owed to r2lib (DEFERRED): sweep a phrase on the raw line AND on the two-line join — this book
# wraps mid-phrase ("10 of 16" is split across L7416-17; chat 106's G-batch fault).
def sweep(lines, phrase, ci=True):
    p = re.compile(re.escape(phrase), re.IGNORECASE if ci else 0)
    raw = [i for i, t in enumerate(lines, 1) if p.search(t)]
    join = [i for i in range(1, len(lines)) if p.search(lines[i - 1].rstrip() + ' ' + lines[i].lstrip())
            and i not in raw and i + 1 not in raw]
    return raw, join

def anywhere(phrase):
    return {k: sweep(M[k], phrase)[0] for k in VOL}

def tot(d):
    return sum(len(v) for v in d.values())

print('r2-ch15i — main L7458-L7558 (§28.6-§28.7.2), prose and pointers')
print('=' * 96)

# ---------------------------------------------------------------- G1 pointers -> claim, and the home
print('G1  each pointer resolved to its CLAIM; where it fails, the claim\'s home is located')
POINT = re.compile(r'§\s*(\d+(?:\.\d+)*)|Chapter\s+(\d+)')
cites = {}
for i in range(LO, HI + 1):
    for m in POINT.finditer(main[i - 1]):
        cites.setdefault(m.group(1) or m.group(2), []).append(i)
print(f'G1  pointers {sum(len(v) for v in cites.values())}; targets ' +
      str({k: v for k, v in sorted(cites.items(), key=lambda x: [int(y) for y in x[0].split('.')])}))

# (target, claim regex swept inside the target, phrase swept volume-wide to locate the home)
TESTS = [('32.5', r'falsif', 'falsification conditions'),
         ('32.1', r'dominant pattern', 'dominant pattern'),
         ('32.3', r'four clauses', 'four clauses'),
         ('16.3', r'five recorded failures|five .{0,20}failures', 'five recorded failures'),
         ('25.6', r'bracket', 'no point estimate'),
         ('23.4', r'4\u03bd', '4\u03bd\u00b3')]
for tgt, claim, phrase in TESTS:
    lo, hi = section_span(main, tgt)
    inside = [j for j in range(lo, hi) if re.search(claim, main[j - 1], re.I)]
    home = anywhere(phrase)
    print(f'G1  §{tgt:<5} L{lo}-{hi} cited from {cites.get(tgt)} | claim /{claim}/ inside target: '
          f'{len(inside)} {inside[:4]}')
    print(f'      home of "{phrase}" across six volumes: ' +
          ('; '.join(f'{k} {v[:6]}' for k, v in home.items() if v) or 'ABSENT everywhere'))
    for k, v in home.items():
        for i in v[:2]:
            print(f'        {k} L{i} §{enclosing(M[k], i) if k == "main" else "-"}: {M[k][i-1].strip()[:82]}')

for s, lab in (('32.6', 'falsification tests'), ('28.1', 'the dominant pattern')):
    print(f'G1b rival target §{s} = "{main[heading_line(main, s) - 1].strip()[:70]}"')
r4a = anywhere('Rule 4a')
print(f'G1b "Rule 4a" sites {tot(r4a)}: ' + '; '.join(f'{k} {v}' for k, v in r4a.items() if v))
print(f'      main L7068 (§25.6): {main[7067].strip()[:88]}')

# ---------------------------------------------------------------- G2 the "first forty-eight"
print('-' * 96)
r, j = sweep(main, 'first forty-eight')
print(f'G2  "first forty-eight" raw {r} join {j} (wrapped across L7482-83)')
for k in VOL:
    rr, jj = sweep(M[k], 'forty-eight')
    print(f'G2  {k:<5} "forty-eight" raw {rr} join {jj}')
print('G2  antecedent 1-48: r2-ch15h F1b measures 0 numbered items below 49 in chapter 28 and 0 in '
      'reg/mc/ioi/sc; the numbering starts at 49 with no printed 1-48 list')

# ---------------------------------------------------------------- G3 corrections-of-corrections
print('-' * 96)
ITEM = re.compile(r'^\s*(?:\*\*)?(\d+)(?:[\u2013\u2014-](\d+))?\.\s')
NOTE = re.compile(r'^\s{4,}\S')
starts = [i for i in range(LO, HI + 1) if ITEM.match(main[i - 1])]
UNIT = re.compile(r'^(?:\s*(?:cells|levels|of|%|channels|induced))')
print('G3  item cross-references (the witness for "corrections of corrections")')
for n, s in enumerate(starts):
    m = ITEM.match(main[s - 1]); a = int(m.group(1)); b = int(m.group(2) or m.group(1))
    e = starts[n + 1] - 1 if n + 1 < len(starts) else HI
    body = []
    for x in range(s, e + 1):
        if x > s and NOTE.match(main[x - 1]) and not ITEM.match(main[x - 1]):
            break                      # an indented closing note is not part of the item
        body.append(main[x - 1])
    txt = ' '.join(body)
    refs = sorted({int(v) for v, tail in re.findall(r'(?<![\d.])(\d{2})(?![\d])(.{0,8})', txt)
                   if 49 <= int(v) <= 74 and not (a <= int(v) <= b) and not UNIT.match(tail)})
    flag = 'CORRECTION OF A CORRECTION' if refs else ''
    if refs:
        print(f'G3  item {a}{"-" + str(b) if b != a else "":<3} L{s:<5} cites {refs}  {flag}')
        print(f'        {txt.strip()[:96]}')
print(f'G3  §28.7 L7502 states "two of these six are corrections of corrections"')
print(f'G3  §28.7.1 L7527 states "two of these eight … and one — 58 — was caught by a number that '
      f'could not exist"')

# ---------------------------------------------------------------- G4 Prints & Proofs
print('-' * 96)
for label, phrase in (('item 74 tail', 'median 340 induced cells'),
                      ('orphan 59', 'cheapest undetectable forgery'),
                      ('§28.6 heading', 'What the register shows about where errors are caught'),
                      ('§28.7 heading', 'made after the register was closed'),
                      ('§28.7.1 heading', 'more from the structural work'),
                      ('§28.7.2 heading', 'more from the structural and audit work'),
                      ('table header', 'caught by')):
    r1, j1 = sweep(main, phrase); r2, j2 = sweep(PP, phrase)
    print(f'G4  {label:<16} main {(r1 or j1)[:4]}  |  PP {(r2 or j2)[:4]}')
for lab, hit in (('item 74', sweep(PP, 'median 340 induced cells')[0]),
                 ('orphan 59', sweep(PP, 'cheapest undetectable forgery')[0])):
    if hit:
        p = hit[0]
        print(f'G4  PP around {lab}:')
        for x in range(p - 2, min(p + 3, len(PP)) + 1):
            print(f'      P{x}: {PP[x-1].rstrip()[:92]}')
ppt = sweep(PP, 'totality \u2014 a refusal at entry')[0]
if ppt:
    print('G4  PP table header rows (the shattered "count" column):')
    for x in range(ppt[0] - 5, ppt[0]):
        print(f'      P{x}: {PP[x-1].rstrip()[:80]}')

# ---------------------------------------------------------------- G5 Ruling 45 / 46
print('-' * 96)
for ph in ('retained in the compendium', 'originally written as', 'in the collaborator', 'the draft'):
    r, j = sweep(main, ph)
    print(f'G5  R45? "{ph:<26}" in unit {[x for x in r if LO <= x <= HI]} | main total {len(r)} {r[:8]}')
R46 = re.compile(r'\b\w+\.py\b|\bBuild \d+\b|register_gen|zeno')
print(f'G5  R46? script/build tokens in unit: '
      f'{[(i, R46.search(main[i-1]).group(0)) for i in range(LO, HI+1) if R46.search(main[i-1])] or "none"}')

# ---------------------------------------------------------------- G6 formatting
print('-' * 96)
for sec in ('28.6', '28.7', '28.7.1', '28.7.2'):
    h = heading_line(main, sec)
    nxt = next(x for x in range(h + 1, HI + 60) if main[x - 1].strip())
    f = main[nxt - 1].strip().lstrip('*\u2022 ')
    print(f'G6  §{sec:<7} first body L{nxt} lower-case open: {bool(f) and f[0].islower()}  "{f[:40]}"')
print(f'G6  §28.6 table header shattered over L7462-64: '
      f'{[main[i-1].strip()[:30] for i in (7462, 7463, 7464)]}')
dup = {}
for i in range(LO, HI + 1):
    t = main[i - 1].strip()
    if len(t) > 60:
        dup.setdefault(t, []).append(i)
print(f'G6  duplicated long lines in unit: '
      f'{ {t[:36]: v for t, v in dup.items() if len(v) > 1} or f"none of {len(dup)} long lines recur"}')

# ---------------------------------------------------------------- G7 negative claims, corroboration
print('-' * 96)
r, j = sweep(main, 'caught by a reader')
print(f'G7  "caught by a reader" raw {r} join {j}; table reader row = 0 (r2-ch15h F2) -> consistent')
for ph in ('nine literatures', 'zero-error capacity', 'Interval analysis', 'Manski', '1966', '1956', '1989'):
    d = anywhere(ph)
    print(f'G7  "{ph:<20}" sites {tot(d):>3}: ' +
          ('; '.join(f'{k} {v[:5]}' for k, v in d.items() if v) or 'ABSENT'))
print('=' * 96)
