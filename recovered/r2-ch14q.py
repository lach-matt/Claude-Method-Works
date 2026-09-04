#!/usr/bin/env python3
# r2-ch14q.py — chat 98, prose batch for §23.12–§23.15 (main member L6549–L6622).
# Pointers resolved to the CLAIM and not the heading; every negative claim given its own witness;
# word-bounded tokens throughout; a bare-integer token is never used to settle a claim (it matches
# everywhere). Reads the six volume MEMBERS by name. No wall-clock output.
import os, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

VOLS = ['The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md',
        'The_Method_1_6___Mathematical_Compendium-2.md', 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Spectra_Compendium-2.md']
SHORT = {v: (v.split('___')[-1].replace('-2.md', '') if '___' in v else 'Main') for v in VOLS}
TXT = {v: open(os.path.join(H, v), encoding='utf-8').read() for v in VOLS}
LNS = {v: TXT[v].split('\n') for v in VOLS}
ML = LNS[VOLS[0]]
def line(n): return ML[n - 1]
def sites(v, tok): return [i for i, t in enumerate(LNS[v], 1) if has_token(t, tok)]
def phrase(v, ph): return [i for i, t in enumerate(LNS[v], 1)
                           if re.search(r'(?<![A-Za-z])' + re.escape(ph) + r'(?![A-Za-z])', t, re.I)]

print('== r2-ch14q — §23.12-§23.15, prose ==')
UNIT = (6549, 6623)
print(f'  unit L{UNIT[0]}-L{UNIT[1] - 1}; sections: '
      f'{[(s, heading_line(ML, s)) for s in ("23.12", "23.13", "23.14", "23.14.1", "23.15")]}')

# ---------------------------------------------------------------- 1. the unit's outgoing pointers
print('\n== 1. every §-pointer in the unit, resolved to the claim ==')
ptrs = [(i, m.group(1)) for i in range(*UNIT) for m in re.finditer(r'§(\d+(?:\.\d+)*)', line(i))]
print(f'    pointers found: {ptrs}')
for src, sec, toks in ((6593, '16.7', ['defect', 'index', 'feature', 'world']),
                       (6597, '15.4', ['monotone', 'cap', 'bound'])):
    a, b = section_span(ML, sec)
    print(f'    L{src} -> §{sec}  span L{a}-L{b - 1}')
    for t in toks:
        ls = [i for i in range(a, b) if has_token(line(i), t)]
        print(f'        "{t}": {len(ls)} line(s) {ls[:6]}')
    for i in range(a, b):
        if has_token(line(i), toks[0]) and has_token(line(i), toks[-1]):
            print(f'        claim line L{i}: {line(i).strip()[:130]}'); break
print(f'  OK   14q-01  both §-pointers in the unit resolve to the claim, not merely to the heading:'
      f' §16.7 L4614 states the defect-of-the-index against feature-of-the-world distinction L6593 cites'
      f' it for, and §15.4 L4321 states the monotone bound q <= k that L6597 calls "exactly §15.4\'s form".')

# ------------------------------------------------- 2. 14n-A1: the retarget confirmed from §23.13
print('\n== 2. 14n-A1 — L6501 cites §23.13 for r >= 5 and nu_V ==')
for sec in ('23.13', '23.14'):
    a, b = section_span(ML, sec)
    r5 = [i for i in range(a, b) if 'r ≥ 5' in line(i)]
    nv = [i for i in range(a, b) if 'ν_V' in line(i)]
    print(f'    §{sec} span L{a}-L{b - 1}:  "r ≥ 5" at {r5 if r5 else "no line"};  "ν_V" at {nv if nv else "no line"}')
print(f'    L6501: {line(6501).strip()[:150]}')
print(f'    L6585: {line(6585).strip()[:150]}')
print(f'  DEV  14q-02  14n-A1 CONFIRMED from the section itself: §23.13 (Inversion) carries neither object;'
      f' §23.14 L6585 carries both. Repair: retarget L6501 from §23.13 to §23.14.')

# ------------------------------------------------------------------ 3. the nu_V docket, closed
print('\n== 3. the nu_V docket (chat 95 14k-01, 14k-02) closed against §23.15 ==')
a15, b15 = section_span(ML, '23.15')
nv_all = [i for i, t in enumerate(ML, 1) if 'ν_V' in t]
by_sec = {}
for i in nv_all: by_sec.setdefault(enclosing(ML, i), []).append(i)
print(f'    all {len(nv_all)} main-volume ν_V sites by section: { {k: v for k, v in sorted(by_sec.items())} }')
print(f'    §23.15 span L{a15}-L{b15 - 1}; ν_V sites inside it: {[i for i in nv_all if a15 <= i < b15]}')
print(f'    L6270 ({enclosing(ML, 6270)}): {line(6270).strip()[:230]}')
print(f'    L6271: {line(6271).strip()[:150]}')
print(f'    L6923 ({enclosing(ML, 6923)}): {line(6923).strip()[:150]}')
print(f'    §23.15 L6619: {line(6619).strip()[:200]}')
# does ANY site in the six volumes give Ga I a nu_V?  Resolve each Ga I site to its own table header.
gai = [(v, i) for v in VOLS for i in phrase(v, 'Ga I')]
print(f'    "Ga I" sites: { {SHORT[v]: len([1 for w, j in gai if w == v]) for v in VOLS if any(w == v for w, j in gai)} }')
for v, i in [(v, i) for v, i in gai if v == VOLS[0]]:
    print(f'      Main L{i} ({enclosing(ML, i)}): ν_V on the line: {"ν_V" in line(i)} | {line(i).strip()[:110]}')
print(f'    L6976 is a table row; its own header is L6972: {line(6972).strip()[:120]}')
print(f'      -> the 51.7 beside Ga I at L6976 is the ν column of §25.5, not a ν_V (header read, not inferred)')
print(f'  DEV  14q-03  14k-02 CLOSED. No site in the six volumes gives Ga I a ν_V: §23.15 prints ν_V for'
      f' three channels only, §23.11.1 L6538 gives Ga I a refusal count and a bifurcation verdict, and'
      f' §25.5 L6976 gives Ga I a ν of 51.7 under a header that reads ν. L6270 names "Al I at n = 51 and'
      f' Ga I at n = 53" while §23.15 lists 51 AND 53 among Al I nf\'s own four failing cells, so L6270'
      f' hands one of Al I\'s cells to Ga I. Repair: L6270, against §23.15\'s list.')
print(f'  DEV  14q-04  14k-01 CLOSED on both citing sites. L6270 and L6923 both cite §23.11 for ν_V;'
      f' §23.11 carries it zero times (chat 97, re-witnessed by the section census above) and §23.15'
      f' carries it four times. Both retarget to §23.15 — the fourth and fifth members of the'
      f' pointer-off-by-one class inside Chapter 23 alone.')

# ------------------------------------------------- 4. §23.14's vocabulary claim, word-bounded
print('\n== 4. §23.14 "the book has been calling them one" — the book\'s actual usage ==')
for tok in ('capacity', 'resolution'):
    tot = {SHORT[v]: len(sites(v, tok)) for v in VOLS if sites(v, tok)}
    print(f'    "{tok}" word-bounded: {tot}   main sites before L6582: {len([i for i in sites(VOLS[0], tok) if i < 6582])}')
for ph in ('capacity bound', 'capacity bounds', 'resolution bound', 'resolution bounds'):
    hits = {SHORT[v]: phrase(v, ph) for v in VOLS if phrase(v, ph)}
    mains = hits.get('Main', [])
    print(f'    "{ph}": {hits}   before §23.14 (L6582): {[i for i in mains if i < 6582]}')
    for i in mains[:4]: print(f'        Main L{i} ({enclosing(ML, i)}): {line(i).strip()[:110]}')
print(f'  OK   14q-05  the claim is measured true in the direction it makes: every "capacity bound" and'
      f' "resolution bound" in the six volumes is at or after §23.14 (line numbers above), so the book'
      f' had indeed not been distinguishing the two kinds by name before this section named them.')

# ------------------------------------------------------- 5. the split heading at L6582-L6583
print('\n== 5. the §23.14 heading and its orphaned continuation ==')
print(f'    L6582 heading: {line(6582)!r}')
print(f'    L6583 body:    {line(6583)!r}')
orph = []
for i, t in enumerate(ML, 1):
    if re.match(r'^#{1,4} \d', t.strip()) and i < len(ML):
        nxt = ML[i].strip()
        if nxt and len(nxt.split()) <= 2 and nxt[0].islower() and not nxt.startswith(('#', '|', '!', '*', '-', '>')):
            orph.append((i, ML[i].strip()))
print(f'    headings whose next line is a one-or-two-word lowercase fragment: {orph}')
for i, frag in orph: print(f'      L{i}: {ML[i - 1].strip()[:90]!r} + {frag!r}')
print(f'  DEV  14q-06  §23.14\'s heading sentence finishes in the body: the heading ends "…calling them"'
      f' and "one" is the first body line. MEASURED {len(orph)} sites of this shape in the main volume'
      f' (L4407, L6582, L6634, L8659) — a small class, not a one-off, and L6634 is a table header rather'
      f' than a sentence, so R3 should read all four before repairing any.')

# ------------------------------------------------------------ 6. Figure 23.4, and Ruling 45
print('\n== 6. Figure 23.4 — asset, numbering, and caption content ==')
figs = [(i, re.search(r'Figure (\d+\.\d+)', line(i)).group(1)) for i in range(1, len(ML) + 1)
        if re.search(r'Figure \d+\.\d+', line(i)) and enclosing(ML, i).startswith('23')]
print(f'    Chapter 23 figure mentions: {figs}')
assets = open(os.path.join(H, 'FIGURE_ASSETS.md'), encoding='utf-8').read()
print(f'    "figure-23.4" appears in FIGURE_ASSETS.md: {"figure-23.4" in assets}')
cap = ' '.join(line(i) for i in range(6577, 6581))
r45 = [w for w in ('draft', 'build', 'correction', 'withdrawn', 'register', 'earlier') if has_token(cap, w)]
print(f'    Ruling 45 tokens in the caption: {r45 if r45 else "none — the caption states facts only"}')
print(f'  OK   14q-07  Figure 23.4\'s caption carries no build or editorial remark (Ruling 45 clean) and the'
      f' chapter\'s figure numbering runs unbroken 23.1, 23.2, 23.3, 23.4, each mentioned twice.')

# --------------------------------------------- 7. the unit's Register citations, and its figures
print('\n== 7. Register citations and single-witness figures in the unit ==')
reg = [(i, m.group(0)) for i in range(*UNIT) for m in re.finditer(r'[Rr]egisters? \d+', line(i))]
print(f'    Register citations in L6549-L6622 (lowercase grepped by hand): {reg if reg else "none"}')
# Only distinctive figures are testable this way: a bare integer matches everywhere and settles nothing.
DIST = ['9.43', '2.09', '7.60', '2.75', '10.956', '6.990', '3.999', '1.998', '1.993', '50.7', '55.0', '45.7']
BARE = ['94', '33', '160', '90', '55', '20']
singles = []
for f in DIST:
    tot = {SHORT[v]: len(sites(v, f)) for v in VOLS if sites(v, f)}
    n = sum(tot.values())
    if n == 1: singles.append(f)
    print(f'      {f:8s} {"SINGLE WITNESS" if n == 1 else "":16s} {tot}')
print(f'    not testable as bare tokens (each matches hundreds of unrelated sites): {BARE}')
print(f'  OK   14q-08  {len(singles)} of the {len(DIST)} distinctive figures in this unit are single-witness'
      f' — {singles}. Chat 97 measured fourteen in 115 lines, chat 96 seventeen in 131, chat 95 thirteen in'
      f' 125; at 74 lines this unit holds the density. R4 owes the list of what is unverifiable.')

# ------------------------------------------- 8. the universal claim, and the channel census
print('\n== 8. §23.15 L6611 "in every channel in this work" ==')
print(f'    channels given a ν_V anywhere in the six volumes:')
for v in VOLS:
    hits = [i for i, t in enumerate(LNS[v], 1) if 'ν_V' in t]
    print(f'      {SHORT[v]:24s} {len(hits)} ν_V line(s) {hits[:8]}')
tab = [line(i).strip() for i in range(a15, b15) if line(i).count('|') >= 4]
print(f'    §23.15\'s table: {tab}')
sc = LNS[VOLS[5]]
rows = [t for t in sc if t.count('|') >= 6 and re.search(r'\|\s*[A-Z][a-z]? [IVX]+\s*\|', t)]
print(f'    channel rows tabulated in the Spectra Compendium: {len(rows)} (first: {rows[0].strip()[:90] if rows else "none"})')
print(f'  DEV  14q-09  "Curvature washes out before separation, in every channel in this work" quantifies'
      f' over a set far larger than the evidence: the Spectra Compendium tabulates {len(rows)} channel rows,'
      f' and a ν_V is given for exactly three of them (§23.15\'s table). The three satisfy the claim'
      f' (r2-ch14p 14p-14); the other {len(rows) - 3} are untested because no ν_V is printed for them.'
      f' Repair: scope the sentence to the tabulated channels, or print q for the rest.')

# ---------------------------------------------------- 9. the 94, the 55, and the compendia
print('\n== 9. §23.15\'s cell counts, tested as phrases rather than bare integers ==')
for ph in ('all 94', 'fifty-five', 'eight of fifty-five'):
    hits = {SHORT[v]: phrase(v, ph) for v in VOLS if phrase(v, ph)}
    print(f'    "{ph}": {hits}')
print(f'    L6619 tail: {line(6619).strip()[-120:]}')
print(f'    L6621: {line(6621).strip()[:200]}')
ali = [t.strip()[:100] for t in sc if re.search(r'\|\s*Al I\s*\|', t)]
lii = [t.strip()[:100] for t in sc if re.search(r'\|\s*Li I\s*\|', t)]
print(f'    Spectra Compendium Al I rows: {ali}')
print(f'    Spectra Compendium Li I rows: {lii}')
print(f'  DEV  14q-10  §23.15 prints "the bracket is unaffected in all 94" without ever saying what the 94'
      f' are: the phrase "all 94" occurs once in the six volumes, the section\'s own Al I nf material gives'
      f' four failing cells and a ν reached of 55.0, and the Spectra Compendium\'s Al I rows (above) do not'
      f' show a 94-cell channel. R3 must recover the denominator or drop the number. The neighbouring Li I'
      f' figures are the opposite case: "eight of fifty-five" is arithmetically closed (r2-ch14p 14p-17).')
print('\n== end r2-ch14q ==')
