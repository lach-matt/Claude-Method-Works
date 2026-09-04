#!/usr/bin/env python3
# r2-ch14a.py - chat 90 - PROSE batch for the Chapter 21 first-part section read
# (main L5597-L5689).  Every pointer resolved to the CLAIM, not the heading; every figure
# grepped across all six volumes to test 21.4's "Every number above is already proved
# elsewhere in this book".  Deterministic; prints no wall-clock time.

import os, re
H = os.path.dirname(os.path.abspath(__file__))
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in F.items()}
M = V['main']
A, B = 5597, 5689


def L(i): return M[i - 1]


# lifted verbatim from r2-ch13w.py (chat 88) - the exact-token heading resolver
def heading_line(sec):
    """Body heading for a section number, taking the LATER match (the front-matter
    contents list at L120-L172 is not the body -- chat 87's fix)."""
    hits = []
    for i, t in enumerate(M, 1):
        m = re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec:
            hits.append(i)
    return hits[-1] if hits else None


# lifted verbatim from r2-ch13w.py (chat 88)
def extent(start):
    lvl = len(M[start - 1]) - len(M[start - 1].lstrip('#'))
    for i in range(start + 1, len(M) + 1):
        m = re.match(r'^(#{1,4}) ', M[i - 1])
        if m and len(m.group(1)) <= lvl:
            return i - 1
    return len(M)


def body(sec):
    t = heading_line(sec)
    if t is None:
        return None, None, ''
    e = extent(t)
    return t, e, '\n'.join(M[t - 1:e])


print('-- 1. every pointer of L5597-L5689 resolved to the CLAIM --')
CLAIMS = [
    (5618, '18.4.1', 'a law of realised closure', ['realis', 'closure']),
    (5620, '3.7', 'the asymmetry, 362 comparisons against eight and a half million',
     ['362', 'asymmetr']),
    (5621, '16.7.1', 'a removability test', ['remov']),
    (5626, '16.6', 'the three defences D_ref, D_dict, D_gro', ['ref', 'dict', 'gro']),
    (5632, '16.6.1', 'a reference index with a verdict coordinate', ['reference index', 'verdict']),
    (5656, '14.5.7', 'a constraint need not be printed: R from phi-hat from the seed',
     ['seed', 'envelope']),
    (5599, '20.1', 'a language is a coordinate system', ['coordinate system']),
]
for site, sec, what, keys in CLAIMS:
    t, e, bd = body(sec)
    if t is None:
        print('   L%-5d sec %-8s UNRESOLVED' % (site, sec)); continue
    low = bd.lower()
    hit = [k for k in keys if k.lower() in low]
    print('   L%-5d sec %-8s -> L%-5d-%-5d  keys %d/%d %-22s %s'
          % (site, sec, t, e, len(hit), len(keys), str(hit)[:22],
             'OK' if len(hit) == len(keys) else 'CHECK'))

print()
print('-- 1b. the forward pointer into 21.5 (19.5.1 L5492) --')
for i in range(5480, 5500):
    if '21.5' in L(i):
        print('   L%d: %s' % (i, L(i).strip()[:120]))

print()
print('-- 2. register citations in range (lowercase grepped by hand) --')
REG = V['reg']
cited = []
for i in range(A, B + 1):
    for m in re.finditer(r'[Rr]egisters?\s+(\d+)(?:\s*[-\u2013]\s*(\d+))?', L(i)):
        lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
        for n in range(lo, hi + 1):
            cited.append((i, n))
print('   citations in range:', [(i, n) for i, n in cited])
for site, n in cited:
    hits = [j for j, t in enumerate(REG, 1)
            if re.match(r'^#{2,4}\s*(Register\s+)?%d[\.\s\u2014-]' % n, t.strip())]
    if not hits:
        hits = [j for j, t in enumerate(REG, 1) if re.search(r'\b%d\b' % n, t) and t.strip().startswith('#')]
    if hits:
        j = hits[-1]
        print('   L%-5d register %-5d -> reg L%-6d %s' % (site, n, j, REG[j - 1].strip()[:88]))
    else:
        print('   L%-5d register %-5d UNRESOLVED' % (site, n))

print()
print('-- 3. audit 21 (L5647): does it name three unreproducible results? --')
for k in ('main', 'mc', 'pc', 'ioi', 'sc'):
    for j, t in enumerate(V[k], 1):
        if re.search(r'\baudit 21\b|^#+ .*\b21\b.*audit', t, re.I) and k != 'main':
            print('   %s L%d: %s' % (k, j, t.strip()[:100]))
aud = [f for f in os.listdir(H) if 'udit' in f]
print('   audit members present:', sorted(aud)[:6])
for f in sorted(aud):
    txt = open(os.path.join(H, f), encoding='utf-8', errors='replace').read().split('\n')
    for j, t in enumerate(txt, 1):
        if re.match(r'^#{1,4}\s*(Audit\s*)?21[\.\s\u2014-]', t.strip(), re.I):
            print('   %s L%d: %s' % (f, j, t.strip()[:100]))
            print('        ' + ' / '.join(x.strip()[:70] for x in txt[j:j + 4] if x.strip())[:200])

print()
print('-- 4. 21.1 "Eight results ... the same shape": the table\'s own rows --')
rows = [i for i in range(5604, 5612)]
two_naming = 0
for i in rows:
    t = L(i)
    bolds = re.findall(r'\*\*(.+?)\*\*', t)
    struct = len(bolds) == 2
    two_naming += struct
    print('   L%d  bold fields %d %-14s %s' % (i, len(bolds), str(bolds)[:14],
                                               'two-naming row' if struct else 'NOT the printed shape'))
print('   rows: %d   rows carrying the header\'s one-object/two-naming/E shape: %d' % (len(rows), two_naming))
print('   header at L5603:', L(5603).strip()[:90])

print()
print('-- 5. 21.4 "Every number above is already proved elsewhere in this book" --')
FIGS = ['118', '36', '365', '750', '840', '578', '199,130', '341,150', '431,050', '206,520',
        '976', '2,370', '19,440', '1,442', '362', '216', '30', '90', '55', '763']
for f in FIGS:
    counts = {}
    for k in V:
        n = sum(t.count(f) for t in V[k])
        if n: counts[k] = n
    inrange = sum(L(i).count(f) for i in range(A, B + 1))
    elsewhere = sum(counts.values()) - inrange
    print('   %-8s in range %2d   elsewhere %4d   %-40s %s'
          % (f, inrange, elsewhere, str(counts)[:40],
             'OK' if elsewhere else 'ONLY HERE'))

print()
print('-- 6. the periodic table: 118 elements (L5604) against 90 cells (L5674) --')
for k in V:
    for j, t in enumerate(V[k], 1):
        if re.search(r'periodic', t, re.I) and re.search(r'\b(90|118)\b', t):
            print('   %-4s L%-6d %s' % (k, j, t.strip()[:112]))

print()
print('-- 7. the seed of Lambda: does any volume print seven, or ten? --')
for k in V:
    for j, t in enumerate(V[k], 1):
        if re.search(r'\bseed\b', t, re.I) and re.search(r'\b(seven|ten|7|10)\b', t):
            s = t.strip()
            if re.search(r'976|Lambda|\u039b', s) or 'seed is' in s:
                print('   %-4s L%-6d %s' % (k, j, s[:112]))

print()
print('-- 8. the three defences named at L5628-L5630 against section 16.6 --')
t, e, bd = body('16.6')
for nm in ('ref', 'dict', 'gro'):
    tok = '\u2145_' + nm
    n_here = sum(L(i).count(tok) for i in range(A, B + 1))
    n_166 = bd.count(tok)
    n_vol = sum(x.count(tok) for x in M)
    print('   %-8s in range %d   in 16.6 (L%s-%s) %d   in the volume %d  %s'
          % (tok, n_here, t, e, n_166, n_vol, 'OK' if n_166 else 'NOT IN 16.6'))

print()
print('-- 9. census rows in range --')
import csv
rows = list(csv.reader(open(os.path.join(H, 'DEFECT-CENSUS.tsv'), encoding='utf-8'), delimiter='\t'))
for r in rows[1:]:
    if r[2] == 'main' and r[3].isdigit() and A <= int(r[3]) <= B:
        print('   %s %s L%s  %s | %s' % (r[0], r[1], r[3], r[4], r[5][:80]))
