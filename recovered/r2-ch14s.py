#!/usr/bin/env python3
# r2-ch14s.py — chat 99, prose batch for the section read of main L6623-L6740.
# Reads the six volume MEMBERS by name; never a BUILDnnn bundle path.  r2lib by path.
# Every pointer is resolved to the CLAIM, not the heading; every negative states its sweep.

import re, importlib.util
from decimal import Decimal, ROUND_HALF_UP

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOLS = {'main': 'The_Method_1_6-2.md', 'spectra': 'The_Method_1_6___Spectra_Compendium-2.md',
        'math': 'The_Method_1_6___Mathematical_Compendium-2.md',
        'phys': 'The_Method_1_6___The_Physics_Compendium-2.md',
        'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
        'register': 'The_Method_1_6___The_Register-2.md'}
V = {k: open(MEM + f, encoding='utf-8').read().split('\n') for k, f in VOLS.items()}
MAIN, REG = V['main'], V['register']
LO, HI = 6623, 6740
UNIT = MAIN[LO - 1:HI]

def verdict(tag, ok, msg):
    print(f'{"OK " if ok else "DEV"}  {tag:9s} {msg}')

print('=== r2-ch14s  prose batch, main L6623-L6740 (Chapter 24 opening through §24.7) ===')

# ---------------------------------------------------------------- P1 the pointer census
print('\n-- P1  every §-pointer in the unit, resolved to the claim --')
ptrs = []
for off, l in enumerate(UNIT):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)', l):
        ptrs.append((LO + off, m.group(1)))
print(f'   {len(ptrs)} §-pointers: ' + ', '.join(f'L{a}→§{b}' for a, b in ptrs))
for ln, sec in ptrs:
    h = heading_line(MAIN, sec)
    sp = section_span(MAIN, sec) if h else None
    print(f'      L{ln} → §{sec}: heading L{h}, span {sp}')

def claim_test(sec, toks, label, src_ln):
    """Resolve a pointer to the claim: the target section must carry every token, word-bounded."""
    h = heading_line(MAIN, sec)
    if not h:
        verdict('24-P1', False, f'L{src_ln} → §{sec}: no heading resolves')
        return
    a, b = section_span(MAIN, sec)
    body = '\n'.join(MAIN[a - 1:b - 1])
    miss = [t for t in toks if not has_token(body, t)]
    verdict('24-P1', not miss, f'L{src_ln} → §{sec} ({label}) L{a}-{b - 1}: tokens absent from the target {miss or "none"}')
    if miss:
        for t in miss:
            sites = [(k, i) for k, L in V.items() for i, l in enumerate(L, 1) if has_token(l, t)]
            byv = {}
            for k, i in sites:
                byv.setdefault(k, []).append(i)
            print(f'         volume-wide sweep for "{t}": ' + (', '.join(f'{k} {len(v)} sites, first L{v[0]}' for k, v in byv.items()) or 'nowhere in the six volumes'))

claim_test('24.7', ['Ritz'], 'L6686 says §24.7 develops the ab initio / Ritz distinction', 6686)
claim_test('32.5', ['1,061'], 'L6683 says §32.5 places the bound at 1,061 cells', 6683)
claim_test('24.12', ['exclude'], 'L6666 says the census of §24.12 excludes the gaps structurally', 6666)

# ---------------------------------------------------------------- P2 Register citations
print('\n-- P2  Register citations in the unit --')
regs = sorted({int(m.group(1)) for l in UNIT for m in re.finditer(r'[Rr]egister\s+(\d+)', l)})
print(f'   cited: {regs}')
for n in regs:
    hits = [i for i, l in enumerate(REG, 1) if re.match(rf'^#{{1,4}}\s*{n}\s*$', l.strip())]
    ln = [LO + o for o, l in enumerate(UNIT) if re.search(rf'[Rr]egister\s+{n}\b', l)]
    if not hits:
        verdict('24-P2', False, f'Register {n} (cited at L{ln}) has no entry heading in the Register')
        continue
    a = hits[0]
    nxt = next((i for i in range(a + 1, len(REG) + 1) if re.match(r'^#{1,4}\s*\d+\s*$', REG[i - 1].strip())), len(REG))
    body = '\n'.join(REG[a:nxt - 1])
    head = ' '.join(body.split())[:150]
    verdict('24-P2', True, f'Register {n} (cited at L{ln}) resolves at Register-member L{a}')
    print(f'         {head}')

# superseded check: a bare SUPERSEDED forward is not a live target (chat 97's finding)
for n in regs:
    hits = [i for i, l in enumerate(REG, 1) if re.match(rf'^#{{1,4}}\s*{n}\s*$', l.strip())]
    if hits:
        a = hits[0]
        nxt = next((i for i in range(a + 1, len(REG) + 1) if re.match(r'^#{1,4}\s*\d+\s*$', REG[i - 1].strip())), len(REG))
        body = '\n'.join(REG[a:nxt - 1])
        verdict('24-P2s', 'SUPERSEDED' not in body.upper(), f'Register {n} is a live entry, not a bare forward')

# ---------------------------------------------------------------- P3 lowercase register pointers
print('\n-- P3  lowercase "register NNN", grepped by hand (the pointer regex is case-sensitive) --')
low = [(LO + o, m.group(0)) for o, l in enumerate(UNIT) for m in re.finditer(r'\bregister\s+\d+', l)]
upp = [(LO + o, m.group(0)) for o, l in enumerate(UNIT) for m in re.finditer(r'\bRegister\s+\d+', l)]
print(f'   lowercase {low}')
print(f'   capitalised {upp}')
verdict('24-P3', not low or not upp, f'the unit uses one case for Register citations: {len(low)} lowercase, {len(upp)} capitalised')

# ---------------------------------------------------------------- P4 Ruling 45 / 46
print('\n-- P4  Ruling 45 (no editorial-process remarks) and Ruling 46 (no build numbers) in reader-facing text --')
r45 = [(LO + o, l.strip()[:120]) for o, l in enumerate(UNIT)
       if re.search(r'earlier version|earlier draft|not in hand|which are owed|this chapter read', l, re.I)]
r46 = [(LO + o, l.strip()[:120]) for o, l in enumerate(UNIT) if re.search(r'\bBuild\s*\d+', l)]
for ln, t in r45:
    print(f'      R45  L{ln}  {t}')
for ln, t in r46:
    print(f'      R46  L{ln}  {t}')
verdict('24-P4a', not r45, f'no editorial-process remark in the unit ({len(r45)} sites)')
verdict('24-P4b', not r46, f'no build number in the unit ({len(r46)} sites)')
allb = {k: [i for i, l in enumerate(L, 1) if re.search(r'\bBuild\s*\d+', l)] for k, L in V.items()}
print('   volume-wide sweep for "Build N": ' + ', '.join(f'{k} {len(v)}' for k, v in allb.items()))
for k, v in allb.items():
    for i in v[:4]:
        print(f'      {k:8s} L{i}  {V[k][i - 1].strip()[:120]}')

# ---------------------------------------------------------------- P5 figures
print('\n-- P5  figures named in the unit --')
figs = sorted({m.group(1) for l in UNIT for m in re.finditer(r'Figure\s+(\d+\.\d+)', l)})
imgs = [(LO + o, m.group(1)) for o, l in enumerate(UNIT) for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', l)]
print(f'   figures referenced {figs}; image directives {imgs}')
for f in figs:
    sites = {k: sum(1 for l in L if has_token(l, f'Figure {f}')) for k, L in V.items()}
    verdict('24-P5', sites['main'] >= 2, f'Figure {f} has an image directive and a caption: main sites {sites["main"]}, all volumes {sites}')

# ---------------------------------------------------------------- P6 attributions
print('\n-- P6  attributions and the age claim --')
for name in ('Edlén', 'Curtis'):
    sites = {k: [i for i, l in enumerate(L, 1) if name in l] for k, L in V.items()}
    print(f'   {name}: ' + ', '.join(f'{k} {len(v)}' for k, v in sites.items()))
    for i in sites['main'][:6]:
        print(f'      main L{i}  {MAIN[i - 1].strip()[:130]}')
q = lambda x, p: Decimal(str(x)).quantize(Decimal(1).scaleb(-p), rounding=ROUND_HALF_UP)
print(f'   L6683 "sixty-five years old" against the 1960 date it cites: 2026 − 1960 = {2026 - 1960}')
verdict('24-P6a', 2026 - 1960 == 65, 'L6683-6684 "The observation is sixty-five years old" vs the 1960 manuscript it names')
bib = {k: [i for i, l in enumerate(L, 1) if 'Curtis' in l and ('1987' in l or 'review' in l.lower())] for k, L in V.items()}
verdict('24-P6b', any(v for v in bib.values()), f'the Curtis 1987 review is carried in a bibliography: {[(k, v) for k, v in bib.items() if v]}')

# ---------------------------------------------------------------- P7 name forms
print('\n-- P7  species name forms --')
forms = {}
for k, L in V.items():
    for i, l in enumerate(L, 1):
        for m in re.finditer(r'\b(K\s?I|neon II|Ne II|helium|bismuth)\b', l):
            forms.setdefault(m.group(1), {}).setdefault(k, []).append(i)
for f, d in sorted(forms.items()):
    print(f'   {f:9s} ' + ', '.join(f'{k} {len(v)}' for k, v in d.items()))
ki_bad = [(k, i) for k, L in V.items() for i, l in enumerate(L, 1) if re.search(r'\bKI\b', l)]
verdict('24-P7a', not ki_bad, f'"K I" is never set without its space: {len(ki_bad)} sites {ki_bad[:6]}')
neon = [(k, i) for k, L in V.items() for i, l in enumerate(L, 1) if 'neon II' in l]
verdict('24-P7b', not neon, f'the ionisation stage is never spelled out in words: "neon II" at {neon}')

# ---------------------------------------------------------------- P8 headings running into the body
print('\n-- P8  heading sentences finishing in the body (14q-06) --')
for off, l in enumerate(UNIT):
    if re.match(r'^#{1,6}\s', l):
        nxt = UNIT[off + 1] if off + 1 < len(UNIT) else ''
        print(f'      L{LO + off}  {l[:60]:60s} | next: {nxt.strip()[:70]}')
h241 = MAIN[6634 - 1]
verdict('24-P8', h241.startswith('### 24.1'), f'L6634 is the §24.1 heading; the line beneath it is {MAIN[6634]!r} — a table header, not a sentence continuation')

# ---------------------------------------------------------------- P9 the universals
print('\n-- P9  universal claims in the unit, each given its own witness --')
univ = [(LO + o, l.strip()[:130]) for o, l in enumerate(UNIT)
        if re.search(r'\bnever\b|\bevery\b|\ball\b|\bno\b\s|\bmonotonic', l, re.I)]
for ln, t in univ:
    print(f'      L{ln}  {t}')
print(f'   {len(univ)} universal or near-universal sentences in 118 lines')

# ---------------------------------------------------------------- P10 the two collections
print('\n-- P10  L6624 "Two collections, and only one of them is bracket-tested" --')
sp24 = section_span(MAIN, '24')
body24 = '\n'.join(MAIN[sp24[0] - 1:sp24[1] - 1])
for t in ('TRIVIAL', 'Appendix B', 'bracket-tested'):
    n = has_token(body24, t.replace(' ', '')) if ' ' not in t else body24.count(t)
    print(f'   "{t}" in Chapter 24: {n}')
verdict('24-P10', body24.count('collection') >= 2, f'the chapter names its second collection: "collection" occurs {body24.count("collection")} times in Chapter 24')

print('\n=== end r2-ch14s ===')
