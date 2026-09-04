# r2-ch13o.py — chat 84, prose batch for the section read §16.1–§16.5.1 (main L4332–L4481).
# Pointers resolved to the claim, figures, attributions, self-counts, headings, census rows.
import os, re, collections
D = os.path.dirname(os.path.abspath(__file__)) + '/'
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
L = {k: open(D + v, encoding='utf-8').read().split('\n') for k, v in F.items()}
M = L['main']; A, B = 4332, 4481
def head(t): print('\n== ' + t + ' ==')
def sites(pat, members=F.keys(), exclude=None):
    p = re.compile(pat); out = []
    for k in members:
        for i, l in enumerate(L[k], 1):
            if k == 'main' and exclude and exclude[0] <= i <= exclude[1]: continue
            if p.search(l): out.append((k, i))
    return out

# ------------------------------------------------- P1  pointers, to the claim
head('P1  every pointer in range, resolved to the claim')
def body(a, b): return '\n'.join(M[a - 1:b])
CHK = [
    ('L4382 §12.11.1 "computes as exact sets"', 3032, 3080, r'exact set'),
    ('L4446 §16.1 "the general form D >= dim q - rank"', 4335, 4350, r'rank ∂Φ/∂p'),
    ('L4473 §28.8 "applies chi to a new coordinate"', 7721, 7745, r'process index|χ over this index'),
    ('L4479 §2.9 "refuse rather than coerce"', 617, 640, r'[Rr]efuse rather than coerce'),
]
for tag, a, b, pat in CHK:
    n = len(re.findall(pat, body(a, b)))
    print(f'  {tag:<52} target L{a}-{b}: {n} match(es)  {"RESOLVES" if n else "UNRESOLVED"}')
print(f'  L4405 Register 242 states the tripwire claim        '
      f'{"YES" if "150 OF 216" in L["reg"][956] else "NO"}')
print(f'  L4457 Register 248 states the totality retest       '
      f'{"YES" if "6,912" in L["reg"][980] else "NO"}')
print(f'  L4440 "§17" is Edlen Handbuch §17, not this book:   '
      f'{"in a quoted citation" if "Handbuch" in M[4438] else "CHECK"}')

head('P1b  "§16.4 form": what §16.4 contains, and where the form is actually stated')
form = r'one coordinate bounded by a monotone function of one other'
print(f'  occurrences of the form-sentence in §16.4 (L4407-4430)   '
      f'{len(re.findall(form, body(4407, 4430)))}')
print(f'  occurrences anywhere in main                             '
      f'{[i for k, i in sites(form, ["main"])]}')
fs = sites(r'§\s?16\.4[- ]form|of §16\.4 form|§16\.4-form')
print(f'  sites naming "§16.4 form" / "§16.4-form"                 {len(fs)}  {fs}')
print(f'  §16.4 (L4407-4430) mentions "monotone"                   '
      f'{len(re.findall("monotone", body(4407, 4430)))}')
print(f'  §16.4 (L4407-4430) mentions "two disjoint paths"         '
      f'{len(re.findall("two disjoint paths", body(4407, 4430)))}')

head('P2  Appendix A: the index rows against the sections that exist')
idx = {}
for i in range(9940, 9956):
    m = re.match(r'\s+(A\.\d+)\s+(.+?)\s{2,}(\S.*)$', M[i - 1])
    if m: idx[m.group(1)] = (i, m.group(2).strip(), m.group(3).strip())
secs = {}
for i, l in enumerate(M, 1):
    m = re.match(r'^### (A\.\d+) (.+)$', l)
    if m: secs[m.group(1)] = (i, m.group(2))
print(f'  rows in the Appendix A index   {len(idx)}  {sorted(idx, key=lambda x: int(x[2:]))}')
print(f'  A.N sections that exist        {len(secs)}  {sorted(secs, key=lambda x: int(x[2:]))}')
print(f'  sections with no index row     '
      f'{sorted(set(secs) - set(idx), key=lambda x: int(x[2:]))}')
print(f'  index rows with no section     {sorted(set(idx) - set(secs))}')
for tag, (li, st, wh) in sorted(idx.items(), key=lambda x: int(x[0][2:])):
    if tag not in ('A.4', 'A.5', 'A.7'): continue
    tgt = re.match(r'§([\d.]+)', wh)
    ln = None
    if tgt:
        for i, l in enumerate(M, 1):
            if re.match(r'^#{3,4} ' + re.escape(tgt.group(1)) + r'\s', l): ln = i; break
    key = {'A.4': r'dim q − rank|dim q - rank|≥ dim q − dim p',
           'A.5': r'χ_Λ .*total|is total', 'A.7': r'may precede'}[tag]
    seg = body(ln, ln + 25) if ln else ''
    print(f'  {tag} "{st}" -> {wh:<22} heading L{ln}, claim matches: '
          f'{len(re.findall(key, seg))}')

head('P3  self-counts and figures restated elsewhere')
for tok, note in [('56 of 56', 'L4363'), ('fifty-six', 'L4371'), ('fifty cells', 'L4368'),
                  ('420', 'L4342'), ('150 of 216', 'L4396'), ('69.4', 'L4396'),
                  ('6,912', 'L4454'), ('30,000', 'L4455'), ('85 trials', 'L4463'),
                  ('36 cells', 'L4475'), ('0.09σ', 'L4426'), ('1.271', 'L4368'), ('0.86', 'L4368')]:
    o = sites(re.escape(tok), exclude=(A, B))
    print(f'  {note:<7} {tok:<12} other sites {len(o):<3} {o[:6]}')
print('  the fifty / fifty-six pair, in range:')
for i in (4363, 4368, 4371):
    print(f'    L{i}| ' + M[i - 1].strip()[:150])

head('P4  Figure 16.1: placement against the figure registries')
print(f'  placement in main       '
      f'{[i for k, i in sites(r"!\[Figure 16\.1\]", ["main"])]}')
for reg in ('FIGURE_ASSETS.md', 'FIGURE_MAP.md'):
    txt = open(D + reg, encoding='utf-8').read().split('\n')
    for i, l in enumerate(txt, 1):
        if '16.1' in l and 'figure' in l.lower(): print(f'  {reg:<18} L{i}| {l.strip()[:130]}')
print(f'  caption L4375-4377 states a fact only (no pictorial verb): '
      f'{"depict" not in body(4375, 4377) and "shows" not in body(4375, 4377)}')

head('P5  attributions in range (R-ATTR)')
print(f'  Register entries cited in L{A}-{B}   '
      f'{re.findall(r"Register (\d+)", body(A, B))}')
print(f'  named sources in range              '
      f'{sorted(set(re.findall(r"\b(Edl[eé]n|Racah|Hori|Condon|Shortley|Rydberg|Moore|Slater)\b", body(A, B))))}')
ed = sites(r'Edl[eé]n')
print(f'  Edlen sites, all volumes            {len(ed)}  {ed}')
print(f'  Handbuch der Physik sites           {sites(r"Handbuch")}')
print(f'  antiprotonic helium: sites of the 804,633,05x figures  '
      f'{sites(r"804,633,05")}')
print(f'  "antiprotonic" sites, all volumes   {sites(r"[Aa]ntiprotonic")}')
print(f'  "Referee flag" sites                {sites(r"Referee flag")}')
print(f'  "flag 5" sites                      {sites(r"flag 5")}')

head('P6  headings broken across two lines (the §16.4 / §28.8 class)')
brk = []
for i, l in enumerate(M, 1):
    m = re.match(r'^(#{2,4}) (.+)$', l)
    if not m or i >= len(M): continue
    nxt = M[i]
    if nxt.startswith(' ') and nxt.strip() and len(nxt.strip()) < 45 \
       and nxt.strip()[0].islower() and not m.group(2).rstrip().endswith(('.', '?', ':')):
        brk.append((i, m.group(2)[-28:], nxt.strip()))
print(f'  headings whose text continues on the following line: {len(brk)}')
for i, h, n in brk: print(f'    L{i}  …{h}  ||  L{i + 1} "{n}"')

head('P7  Ruling 45 / 46 in range, and the census rows')
print(f'  script names / build numbers / file handles in range  '
      f'{re.findall(r"[a-z_]+\.py|BUILD\d+|\.md\b|__pycache__", body(A, B))}')
cen = [l for l in open(D + 'DEFECT-CENSUS.tsv', encoding='utf-8').read().split('\n')
       if re.match(r'^\d+\t', l) and l.split('\t')[2] == 'main'
       and A <= int(l.split('\t')[3]) <= B]
print(f'  census rows in range: {len(cen)}')
for l in cen:
    f = l.split('\t'); print(f'    {f[0]}  {f[1]}  L{f[3]}  token "{f[4]}"')
