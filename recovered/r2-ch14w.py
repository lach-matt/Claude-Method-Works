#!/usr/bin/env python3
"""r2-ch14w — prose batch for the Chapter 24 third read, main L6817-L6883.

Pointers resolved to the claim as the target words it (never to the heading, never by
prefix); attributions checked against the compendium's own source table; every negative
given its own witness and the sweep stated.  Reads MEMBERS only.
"""
import os, re, importlib.util

H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

def lines(n):
    return open(os.path.join(H, n), encoding='utf-8').read().split('\n')

MAIN = lines('The_Method_1_6-2.md')
VOLS = [('main', MAIN),
        ('register', lines('The_Method_1_6___The_Register-2.md')),
        ('math', lines('The_Method_1_6___Mathematical_Compendium-2.md')),
        ('physics', lines('The_Method_1_6___The_Physics_Compendium-2.md')),
        ('index', lines('The_Method_1_6___The_Index_of_Indices-2.md')),
        ('spectra', lines('The_Method_1_6___Spectra_Compendium-2.md'))]
U0, U1 = heading_line(MAIN, '24.10'), heading_line(MAIN, '25') - 1
UNIT = MAIN[U0 - 1:U1]

def hits(V, tok, lo=1, hi=None):
    hi = hi or len(V) + 1
    return [i for i in range(lo, hi) if has_token(V[i - 1], tok)]

print('== Q1  pointers out of the unit, resolved to the claim')
sp1224 = section_span(MAIN, '24.12')
tgt = '\n'.join(MAIN[sp1224[0] - 1:sp1224[1] - 1])
print('   S24.12 span %s' % (sp1224,))
for tok in ('exclude', 'excluded', 'exclusion', 'exclusions', 'structurally',
            'open-d', 'open-f', 'd-shell', 'f-shell', 'transition'):
    print('       S24.12 has_token %-13s %d' % (tok, has_token(tgt, tok)))
print('   L6842 -> S24.12 for "every open-d and open-f sequence": the target names')
print('       the five as %s' % re.sub(r'\s+', ' ', MAIN[6849][:120]).strip())
print('   14r-22 (chat 99): L6666 -> S24.12 for a structural exclusion.')
print('       L6666 wording: %s' % re.sub(r'\s+', ' ', MAIN[6665]).strip())
print('       S24.12 wording: %s' % re.sub(r'\s+', ' ', MAIN[6849][:96]).strip())
print('       verdict: the target states the claim in its own words ("excluded structurally"),')
print('       so the pointer RESOLVES; the earlier negative came from testing the token *exclude*')
print('       where the section writes *excluded*.')

print('== Q2  front matter L62 against the unit')
print('   L62: %s' % re.sub(r'\s+', ' ', MAIN[61]).strip())
print('   S24.11 heading: %s' % MAIN[6825].strip())
rows = [t for t in MAIN[6828:6836] if t.startswith('|') and not set(t) <= set('|- ')]
print('   S24.11 table: %d rows, causes = %d distinct'
      % (len(rows) - 1, len({r.split('|')[2].strip().split(' —')[0].split(';')[0]
                             for r in rows[1:]})))
for r in rows[1:]:
    c = [x.strip() for x in r.strip('|').split('|')]
    print('       %-14s | %-58s | %s' % (c[0].replace('**', ''), c[1][:58], c[2].replace('**', '')))

print('== Q3  the census scope: is any open-f sequence in the six volumes?')
for nm, V in VOLS:
    print('   %-9s open-f %d  open-d %d  lanthanide %d  f-shell %d  4f %d'
          % (nm, has_token('\n'.join(V), 'open-f'), has_token('\n'.join(V), 'open-d'),
             has_token('\n'.join(V), 'lanthanide'), has_token('\n'.join(V), 'f-shell'),
             len(re.findall(r'(?<![\w])4f(?![\w])', '\n'.join(V)))))
print('   main-volume open-f sites: %s' % hits(MAIN, 'open-f'))
print('   sequences named in the census: %s'
      % re.sub(r'\s+', ' ', MAIN[6849][:110]).strip())

print('== Q4  S24.10 attribution against the compendium source table')
SPEC = dict(VOLS)['spectra']
b1 = next(i for i, t in enumerate(SPEC, 1) if t.strip().startswith('## B.1'))
print('   B.1 Sources at spectra L%d' % b1)
for i in range(b1, b1 + 12):
    if SPEC[i - 1].strip():
        print('       L%d %s' % (i, re.sub(r'\s+', ' ', SPEC[i - 1])[:112]))
for nm, V in VOLS:
    t = '\n'.join(V)
    print('   %-9s "Kaufman" %d  "ASD" %d  "47379" %d  "Al II" %d'
          % (nm, has_token(t, 'Kaufman'), has_token(t, 'ASD'),
             len(re.findall(r'47379', t)), has_token(t, 'Al II')))
print('   main "Kaufman" sites: %s' % hits(MAIN, 'Kaufman'))
print('   47379 sites in main: %s'
      % [i for i, t in enumerate(MAIN, 1) if '47379' in t])

print('== Q5  Ruling 45 / 46 candidates inside the unit')
PAT = [r'\bfetch\w*', r'\bthis work\b', r'\bthis book\b', r'\bthe index\b', r'\bchapter reads\b',
       r'\bbuild\s*\d', r'\.py\b', r'\bregister\s+\d+', r'\bshould be written\b', r'\bcost\b']
for i in range(U0, U1 + 1):
    m = [p for p in PAT if re.search(p, MAIN[i - 1], re.I)]
    if m:
        print('   L%d %-28s %s' % (i, ','.join(x.strip('\\b') for x in m),
                                   re.sub(r'\s+', ' ', MAIN[i - 1])[:78].strip()))
print('   "fetch*" across the volumes: %s'
      % ' '.join('%s %d' % (nm, len(re.findall(r'fetch\w*', '\n'.join(V), re.I))) for nm, V in VOLS))

print('== Q6  Figure 24.3 — placement, caption, cross-references')
fig = [i for i, t in enumerate(MAIN, 1) if 'figure-24.3' in t or re.search(r'Figure 24\.3', t)]
for i in fig:
    print('   L%d in %-6s %s' % (i, enclosing(MAIN, i), re.sub(r'\s+', ' ', MAIN[i - 1])[:96].strip()))
print('   the caption describes leave-one-out on four-point sequences, which is S24.13\'s material;')
print('   the image sits inside S24.12 (%s)' % enclosing(MAIN, fig[0]))
for nm, V in VOLS[1:]:
    h = [i for i, t in enumerate(V, 1) if re.search(r'Figure 24\.3', t)]
    if h:
        print('   also cited in %s at %s' % (nm, h))

print('== Q7  single-witness figures of the unit')
for tok in ('47379.140', '47379.7', '0.560', '107,942', '111,124', '108,014', '110,366',
            '11.1', '23.4', '0.53', '0.83', '34%', '19 to 37'):
    tot = {nm: len(re.findall(re.escape(tok), '\n'.join(V))) for nm, V in VOLS}
    print('   %-10s %s' % (tok, ' '.join('%s %d' % (k, v) for k, v in tot.items() if v)))

print('== Q8  restatement and duplication inside the unit')
bq = ' '.join(MAIN[6819:6822])
print('   L6820-L6822 blockquote: "one disagreement in 40" %d  "one disagreement in forty" %d'
      % (len(re.findall(r'one disagreement in 40', bq)),
         len(re.findall(r'one disagreement in forty', bq))))
print('   text: %s' % re.sub(r'\s+', ' ', bq).strip()[:190])

print('== Q9  S24.13 L6858 "five isoelectronic pairs and two four-point sequences"')
p66 = section_span(MAIN, '24.6')
pr = [re.sub(r'\s+', ' ', MAIN[i - 1]).strip() for i in range(p66[0] + 1, p66[1])
      if re.match(r'^\s{2,}\S', MAIN[i - 1]) and '-like' in MAIN[i - 1]]
print('   S24.6 span %s lists %d pairs:' % (p66, len(pr)))
for x in pr:
    print('       %s' % x[:74])
print('   the two four-point sequences of S24.13 are %s'
      % re.sub(r'\s+', ' ', MAIN[6862]).strip()[:74])

print('== Q10  every pointer and citation inside the unit')
for i in range(U0, U1 + 1):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)', MAIN[i - 1]):
        s = m.group(1)
        print('   L%d -> S%-7s heading %s' % (i, s, heading_line(MAIN, s)))
    for m in re.finditer(r'[Rr]egisters? (\d+)', MAIN[i - 1]):
        print('   L%d -> Register %s' % (i, m.group(1)))
print('   (no §-pointer or Register citation printed above means the unit carries none)')
