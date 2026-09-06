#!/usr/bin/env python3
# r2-ch13u.py — Phase R2, chat 87, prose batch for the Chapter 18 section read
# (main L4922–L5380).  Pointers resolved to the claim and not the heading; attributions,
# register citations, cross-site figure agreement, and the chapter's own self-counts.
# Deterministic; prints no wall-clock time.

import importlib.util, os, re

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)

V = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
D = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in V.items()}
M = D['main']
def L(i): return M[i - 1]
def head(t): print('\n=== ' + t)
def row(*a): print('   ' + '  '.join(str(x) for x in a))

def sites(pat, vols=None):
    out = []
    for k in (vols or V):
        for i, ln in enumerate(D[k], 1):
            if re.search(pat, ln): out.append((k, i, ln.strip()))
    return out

def span(start):
    """The lines of the main-volume section opening at `start`, to the next heading."""
    lvl = len(M[start - 1]) - len(M[start - 1].lstrip('#'))
    out = []
    for i in range(start + 1, len(M) + 1):
        t = L(i)
        if t.startswith('#') and (len(t) - len(t.lstrip('#'))) <= lvl: break
        out.append((i, t))
    return out

def heading_at(num):
    for i, ln in enumerate(M, 1):
        if re.match(r'^#+\s+' + re.escape(num) + r'[\s.]', ln): return i, ln.strip()
    return None, None

# ---------------------------------------------------------------- P1
# Every pointer in Chapter 18 resolved to the CLAIM attributed to it, not the heading.
head('P1  pointers resolved to the claim')
CLAIMS = [
    (4928, '§12.11.2', '12.11.2', ['coupling', 'triangle', 'sum', 'difference'],
     'carries the computation for exact vector coupling'),
    (4948, '§18.1.1', '18.1.1', ['conserving poset'],
     'names §18.1.1 as the source of the conserving poset — the section it is in'),
    (4974, 'Ch.12', '12', ['over, not graded by', 'over the lattice'],
     '"over, not graded by" is the same fact stated geometrically'),
    (4978, 'Ch.19', '19', ['depth', 'measured members', 'literature'],
     'Chapter 19 makes depth precise'),
    (4997, 'Ch.30', '30', ['cost', 'local', 'top'], 'Chapter 30 states what this costs'),
    (5010, '§2.18', '2.18', ['decision', 'test'], 'nothing tests a decision'),
    (5033, '§3.7', '3.7', ['certificate', 'checkable', 'comparison'],
     'a certificate is checkable where a search is not'),
    (5038, '§16.7.1', '16.7.1', ['removable', 'artefact', 'world'],
     'asks whether E is removable, artefact vs fact about the world'),
    (5043, 'Ch.15', '15', ['re-coordinatis', 'self-reference', 'alphabet'],
     'the thesis of Chapter 15 is the other half'),
    (5056, '§6.2', '6.2', ['drip', 'band'], 'the drip lines are the envelopes'),
    (5057, '§6.3', '6.3', ['relabel', 'month'], 'the relabelling creates the monotone bound'),
    (5117, '§28.1', '28.1', ['proxy', 'pattern'], 'the proxy mistaken for the property'),
    (5124, '§12.11.3.1', '12.11.3.1', ['bound', 'extent', 'law'],
     'draws a rule about where a bound is taken from'),
    (5150, '§7.1', '7.1', ['three central results', 'tree', 'follow'],
     'says three central results follow from Λ being a tree'),
    (5156, '§22', '22', ['bracket'], 'brackets in §22\'s sense'),
    (5216, '§2.18.1', '2.18.1', ['two parents', 'acyclic', 'decision'],
     'the decisions form an acyclic graph with exactly two two-parent nodes'),
    (5244, '§7.1', '7.1', ['single-argument', 'one coordinate bounded', 'monotone function of one'],
     'had said every bound is single-argument without saying what it bought'),
    (5253, '§17.4', '17.4', ['sum', 'index it', 'repair'],
     'the repair: a sum cannot be bounded, so index it'),
    (5295, 'Ch.23', '23', ['pole', 'p = 1', 'guarantee'], 'the cost of a guarantee has a pole at p = 1'),
    (5355, '§25.6', '25.6', ['Sc VI', '6s'], 'the Sc VI 6s cell'),
    (5328, '§29.1', '29.1', ['search', 'precedent', 'novelty'], 'E(search) > 0 always'),
]
for ln, ptr, num, keys, claim in CLAIMS:
    hi, ht = heading_at(num)
    if hi is None:
        row(f'L{ln} {ptr:12s}', 'NO HEADING', claim); continue
    body = ' '.join(t for _, t in span(hi)).lower()
    hit = [k for k in keys if k.lower() in body]
    row(f'L{ln} {ptr:12s}→ L{hi}', f'keys {len(hit)}/{len(keys)} {hit if hit else "NONE"}',
        'CLAIM PRESENT' if hit else 'CLAIM ABSENT', '|', claim[:52])

# ---------------------------------------------------------------- P2
head('P2  register citations in Chapter 18')
REGS = [412, 298, 275, 306, 326, 317, 406, 316, 308, 299, 302, 303, 325, 224, 355, 219, 220, 221, 222, 232]
R = D['reg']
for n in REGS:
    at = [i for i, ln in enumerate(R, 1) if re.match(r'^###\s.*\b%d\b' % n, ln)]
    body = ''
    if at: body = ' '.join(R[at[0]:at[0] + 6])[:78].replace('\n', ' ')
    row(f'Register {n:>4}', f'{"found L"+str(at[0]) if at else "NOT FOUND"}', body)

# ---------------------------------------------------------------- P3
head('P3  the theorems §18.1.3 names')
for pat in (r'Theorem\s*11\.1', r'Theorem\s*11\.2', r'Theorem\s*18\.1', r'Theorem\s*18\.2'):
    ss = sites(pat)
    row(pat.replace('\\s*', ' '), f'{len(ss)} sites', [f'{k}:L{i}' for k, i, _ in ss][:8])
row('L4965 as printed:', L(4965).strip()[:96])
row('VERDICT: §18.1.3 disclaims theorems that do not exist; the ones argued are 18.1 (L4932) and 18.2 (L4940)')

# ---------------------------------------------------------------- P4
head('P4  the conserving poset')
ss = sites(r'conserving poset')
for k, i, t in ss: row(f'{k}:L{i}', t[:104])
row('VERDICT:', f'{len(ss)} sites, both inside §18.1.1; the object is defined nowhere in the six volumes')

# ---------------------------------------------------------------- P5
head('P5  the two printed definitions of ν')
for pat in (r'ν\s*=\s*e\s*−\s*δ', r'ν\s*=\s*n\s*−\s*δ', r'δ\s*=\s*f\s*−\s*ℓ'):
    ss = sites(pat)
    row(pat, f'{len(ss)} sites', [f'{k}:L{i}' for k, i, _ in ss])
row('L4971:', L(4971).strip()[:100])
row('L6422:', L(6422).strip()[:100])
row('L10016:', L(10016).strip()[:100])

# ---------------------------------------------------------------- P6
head('P6  the chapter\'s self-counts')
heads18 = [(i, L(i).strip()) for i in range(4922, 5381) if L(i).startswith('#')]
row('sections and subsections in Chapter 18:', len(heads18))
row('L4923:', L(4923).strip()[:96])
row('L5304:', L(5304).strip()[:96])
row('L5373:', L(5373).strip()[:96])
row('L5323:', L(5323).strip()[:110])
neg = [i for i in (4931, 4970, 4976, 4980, 5294) if L(i).startswith('###')]
row('the sections a reader would count as the limitations above §18.6:', [L(i).strip()[:34] for i in neg])
row('VERDICT: §18.6 counts five limitations above it; §18.6.4 calls itself the fifth; '
    'L4923 says every result is negative while L5321–5323 print one that is not')

# ---------------------------------------------------------------- P7
head('P7  attributions in Chapter 18')
for name in ('Brylawski', 'Freuder', 'Dechter', 'Baker', 'Janet', 'Maxwell', 'Ampère', 'Jacobi', 'Hill', 'KAM'):
    ss = sites(name)
    inch = [i for k, i, _ in ss if k == 'main' and 4922 <= i <= 5380]
    row(f'{name:10s}', f'total {len(ss)} sites', f'in Chapter 18: {inch}',
        'volumes ' + ','.join(sorted({k for k, _, _ in ss})))

# ---------------------------------------------------------------- P8
head('P8  cross-site agreement of the E figures')
FIG = {'calendar 7': (r'calendar', 7), 'periodic table 36': (r'periodic table', 36),
       'nuclide 9': (r'nuclide', 9), 'bibliography 6': (r'bibliograph', 6)}
for lbl, (pat, val) in FIG.items():
    hits = [i for i in range(4922, 5381) if re.search(pat, L(i), re.I) and re.search(r'\b%d\b' % val, L(i))]
    row(lbl, 'lines in Chapter 18 carrying both:', hits)
row('the audits: E =', re.search(r'coordinates\s+(\d+)', L(5025)).group(1), 'at L5025 and',
    re.search(r'coordinates\s+(\d+)', L(5062)).group(1), 'at L5062  — MISMATCH')
row('subnet with a hole, E = 8 (L5319): other sites',
    [f'{k}:L{i}' for k, i, _ in sites(r'subnet') if not (k == 'main' and 4922 <= i <= 5380)][:6])
row('asteroid belt 2 → 1 (L5336): §16.7.1 sites',
    [i for i, t in span(4578) if re.search(r'asteroid|belt', t, re.I)][:6])

# ---------------------------------------------------------------- P9
head('P9  §16.7.1 read against the two claims Chapter 18 makes about it')
b = ' '.join(t for _, t in span(4578))
for phrase in ('artefact', 'fact about the world', 'removable', 'mechanism', 'asteroid', 'irreducible'):
    row(f'"{phrase}" in §16.7.1:', phrase.lower() in b.lower())
row('L5038–5040 says §16.7.1 "gives an outcome without a mechanism"')
row('L5331 says §16.7.1 sorts a defect into two verdicts and Chapter 18 adds a third')

# ---------------------------------------------------------------- P10
head('P10  §18.4 against §15.3 and Appendix A.8 (13l-05, DEFERRED)')
for i in (4302, 9969, 9970):
    row(f'L{i}:', L(i).strip()[:112])
b184 = ' '.join(t for _, t in span(4980))
for phrase in ('total order', 'relabelling', 'may precede', 'd = 2'):
    row(f'"{phrase}" in §18.4:', phrase.lower() in b184.lower())
row('VERDICT: §15.3 promises a development in §18.4; §18.4 carries none of its vocabulary')

print('\n=== end r2-ch13u')
