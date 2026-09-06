#!/usr/bin/env python3
"""r2-ch15c — prose, pointer and cross-volume claims of Chapter 26 (main L7117-L7202).

Chat 104.  Reads the six volume MEMBERS, never a bundle.  Resolvers imported from r2lib by path
and passed the LINE LIST.  Every pointer test carries a claim-locator: a token test that fails
names no target.  Matches print a WINDOW around the hit, never the head of the line.

Rewritten once before banking.  The five faults, all self-caught in the first run:
  A. the sec 23.11 pointer failed and nothing then looked for where lambda^2 does live.
  B. the splice regex matched 'figures/figure-6.1.png', returning 34 main hits nearly all of
     which were image paths.  Paths and file names are now excluded before the sweep.
  C. C8 counted 'Figure 19.1' without printing a window, so a legitimate Chapter 19 figure and a
     stale caption were indistinguishable.  Every C8 hit now prints its line.
  D. 'cost law' was tested in one form; the volume writes 'cost-law' at L10278.  Both forms, and
     the same for 'three-level'.
  E. the Mathematical Compendium cites 'M sec 24.6' for the Aitken result.  That pointer is now
     tested against sec 24.6 itself, with a locator.
"""
import importlib.util, re

H = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', H + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token

VOL = {'main': 'The_Method_1_6-2.md',
       'reg':  'The_Method_1_6___The_Register-2.md',
       'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc':   'The_Method_1_6___Spectra_Compendium-2.md'}
M = {k: r2lib.read_member(v).split('\n') for k, v in VOL.items()}
A, B = 7117, 7202

def head(s): print('\n== ' + s)

def win(line, tok, w=70):
    i = line.lower().find(tok.lower())
    if i < 0: return line.strip()[:2*w]
    return ('...' if i-w > 0 else '') + line[max(0, i-w):i+len(tok)+w] + ('...' if i+len(tok)+w < len(line) else '')

print('r2-ch15c  Chapter 26, main L%d-L%d' % (A, B))

# ---------------------------------------------------------------- C1 the chapter's own pointers
head('C1  the two section pointers the chapter makes, each with a claim-locator')
print('  L7156 -> 29.8 for "the searched bound"')
sp = section_span(M['main'], '29.8')
print('   heading:', M['main'][sp[0]-1].strip(), '| span', sp)
body = '\n'.join(M['main'][sp[0]-1:sp[1]-1])
print('   tokens in 29.8:', ', '.join(f'{t}={has_token(body, t)}' for t in
                                      ('searched', 'bound', 'C6', 'collective', 'predicting')))
print('   RESOLVES. The pointer lands, but on a table cell, and the cell cites its own section:')
for i in range(sp[0]-1, sp[1]-1):
    if 'searched bound' in M['main'][i].lower():
        print(f'     L{i+1}: {M["main"][i].strip()}')
print('   the identical 27-character string in the chapter under read:')
print(f'     L7156: {M["main"][7155].strip()}')

print('\n  L7185 -> 23.11 for "exactly lambda-squared of 23.11"')
sp2 = section_span(M['main'], '23.11')
print('   heading:', M['main'][sp2[0]-1].strip(), '| span', sp2)
b2 = '\n'.join(M['main'][sp2[0]-1:sp2[1]-1])
print('   in 23.11: lambda-char', b2.count('λ'), '| "λ²"', b2.count('λ²'), '| "2/3"', b2.count('2/3'),
      '| Newton', has_token(b2, 'Newton'))
print('   FAILS. CLAIM-LOCATOR - where does the lambda-squared reading of 2/3 live?')
for k in VOL:
    hits = [(i+1, l) for i, l in enumerate(M[k]) if 'λ²' in l]
    print(f'     {k}: {len(hits)} lines carry the literal λ²', end='')
    print(' ->', ', '.join(f'L{n}' for n, _ in hits[:8]) if hits else '')
    for n, l in hits[:4]:
        if not (k == 'main' and A <= n <= B):
            print(f'        L{n}: {win(l, "λ²", 62)}')
print('   sections of the main volume that carry λ² (enclosing heading of each site):')
seen = set()
for i, l in enumerate(M['main']):
    if 'λ²' in l:
        j = i
        while j >= 0 and not re.match(r'^#{2,4} ', M['main'][j]): j -= 1
        h = M['main'][j].strip() if j >= 0 else '?'
        if h not in seen: seen.add(h); print(f'     L{i+1} under {h[:70]}')

# ---------------------------------------------------------------- C2 attribution
head('C2  attributions: Singer and Aitken against the bibliography (docket 16 class)')
for name in ('Singer', 'Aitken'):
    tot = {k: [(i+1, l) for i, l in enumerate(M[k]) if has_token(l, name)] for k in VOL}
    print(f'   {name}: total {sum(len(v) for v in tot.values())} :',
          ', '.join(f'{k} {len(v)}' for k, v in tot.items()))
    for k in ('main', 'mc'):
        for n, l in tot[k]:
            if any(w in l for w in ('**', 'Prior art', 'Proved', '(19', '(20')):
                print(f'      {k} L{n}: {win(l, name, 62)}')

# ---------------------------------------------------------------- E  the mc -> sec 24.6 pointer
head('E  mc cites "M sec 24.6" for the Aitken bias. The result is in sec 26.6. Test 24.6.')
sp3 = section_span(M['main'], '24.6')
print('   24.6 heading:', M['main'][sp3[0]-1].strip(), '| span', sp3)
b3 = '\n'.join(M['main'][sp3[0]-1:sp3[1]-1])
print('   tokens in 24.6:', ', '.join(f'{t}={has_token(b3, t)}' for t in
                                      ('Aitken', 'limit', 'extrapolat', 'bias', 'geometric')))
sp4 = section_span(M['main'], '26.6')
print('   26.6 heading:', M['main'][sp4[0]-1].strip(), '| span', sp4)
b4 = '\n'.join(M['main'][sp4[0]-1:sp4[1]-1])
print('   tokens in 26.6:', ', '.join(f'{t}={has_token(b4, t)}' for t in
                                      ('Aitken', 'limit', 'bias', 'geometric')))
print('   the citing lines in the Mathematical Compendium:')
for i, l in enumerate(M['mc']):
    if has_token(l, 'Aitken') and ('Proved' in l or 'Prior art' in l or l.startswith('###')):
        print(f'     mc L{i+1}: {l.strip()[:170]}')

# ---------------------------------------------------------------- C3 Rb absent member
head('C3  docket 20: sec 26.5 prices its only empirical test on Rb ns-ns. Rb rows?')
print('   spectra rows beginning "| Rb":',
      len([1 for l in M['sc'] if re.match(r'^\|\s*Rb\b', l.strip())]))
for k in VOL:
    n = sum(1 for l in M[k] if has_token(l, 'Rb'))
    m = sum(1 for l in M[k] if has_token(l, 'rubidium'))
    print(f'   {k:<5} Rb {n:>3}   rubidium {m:>3}')
print('   the compendium tabulates the species Chapter 26 tests on: NO.')

# ---------------------------------------------------------------- C4 Ruling 45 / 46
head('C4  Ruling 45 (no editorial-process remarks) and Ruling 46 (no internals)')
CH = M['main'][A-1:B]
print('   Ruling 46 tokens:', ', '.join(f'{t}={sum(1 for l in CH if has_token(l, t))}'
                                        for t in ('build', 'script', 'md5', 'instrument')))
for ln in (7189, 7190, 7201):
    print(f'   L{ln}: {M["main"][ln-1].strip()}')
print('   L7201 addresses the reader directly and describes the authoring choice: Ruling 45 member.')

# ---------------------------------------------------------------- C5 false universals
head('C5  docket 19: universals in the chapter, each with its witness')
for i, l in enumerate(M['main'][A-1:B], A):
    if has_token(l, 'every'):
        print(f'   L{i}: {win(l, "every", 78)}')
print('   All three are claims about the algebra (log q = p log nu), not about the collection,')
print('   so none is measurable against the channel table: docket 19 gains no member here.')

# ---------------------------------------------------------------- C6 headings
head('C6  14q-06: does any of the seven headings finish in the body?')
for ln in (7119, 7141, 7149, 7153, 7162, 7172, 7194):
    nxt = next((M['main'][j] for j in range(ln, ln+3) if M['main'][j].strip()), '')
    print(f'   L{ln} {M["main"][ln-1].strip()[:58]:<58} | body: {nxt.strip()[:48]}')

# ---------------------------------------------------------------- C7 the splice class
head('C7  the splice shape, swept with paths and file names excluded (fault B)')
PAT = re.compile(r'\d\.\d*(?=[a-z]{3})')
def is_path(l, m):
    s = max(0, m.start()-40)
    ctx = l[s:m.end()+40]
    return ('figures/' in ctx or '.png' in ctx or '.pdf' in ctx or '.tsv' in ctx
            or '.json' in ctx or '.md' in ctx or '`' in ctx or '](' in ctx)
for k in VOL:
    hits = []
    for i, l in enumerate(M[k]):
        m = PAT.search(l)
        if m and not is_path(l, m): hits.append((i+1, l, m.group(0)))
    print(f'   {k:<5} genuine decimal-into-word sites: {len(hits)}')
    for n, l, g in hits[:6]:
        print(f'      L{n}: {win(l, g, 62)}')

# ---------------------------------------------------------------- C8 figure numbering
head('C8  Figure 26.1 (BUILD90) vs Figure 19.1 (Prints & Proofs caption) - windows printed')
for tag in ('Figure 26.1', 'Figure 19.1', 'figure-26.1.png', 'figure-19.1.png'):
    for k in VOL:
        for i, l in enumerate(M[k]):
            if tag.lower() in l.lower():
                print(f'   {tag:<16} {k} L{i+1}: {win(l, tag, 62)}')

# ---------------------------------------------------------------- C9 locators, every word-form
head('C9  claim-locators for the figures the computable batch could not reproduce (fault D)')
def locate(forms, label):
    print(f'  {label}:')
    for k in VOL:
        hits = []
        for i, l in enumerate(M[k]):
            if any(f.lower() in l.lower() for f in forms): hits.append((i+1, l))
        if hits:
            print(f'     {k}: {len(hits)} ->', ', '.join(f'L{n}' for n, _ in hits[:8]))
            for n, l in hits[:3]:
                if not (k == 'main' and A <= n <= B):
                    print(f'        L{n}: {win(l, forms[0], 62)}')
locate(['cost law', 'cost-law'], 'the cost law (both forms)')
locate(['three-level', 'three level'], 'the three-level bracket (both forms)')
locate(['9.49'], 'sigma_1 = 9.49e1')
locate(['1.05%'], 'median error 1.05%')
locate(['1.83%'], 'maximum error 1.83%')
locate(['66 of 66'], '"66 of 66" as printed')
locate(['fifteen Rydberg'], 'the fifteen Rydberg quantities')

print('\nr2-ch15c complete')
