#!/usr/bin/env python3
# r2-ch13k.py — Phase R2, chat 82. PROSE batch for the section read main §14.5.8–§14.6
# (L3810–L4269), on the model of r2-ch13i.py (chat 81): every pointer resolved to the CLAIM and not
# the heading, every figure grepped for its other sites, every self-count re-derived, every Register
# citation opened, every attribution checked against the References.
# Deterministic: no wall-clock output.

import re, os

D = '/home/claude/members/'
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md', 'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md', 'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
L = {k: open(D + v, encoding='utf-8').read().split('\n') for k, v in F.items()}
M = L['main']; R = L['reg']
A, B = 3810, 4269


def show(k, i, w=118):
    return '%s L%d| %s' % (k, i, L[k][i - 1].strip()[:w])


def sites(tok, members=('main', 'reg', 'mc', 'pc', 'ioi', 'sc'), exclude=(A, B)):
    pat = re.compile(r'(?<![\d.,])' + re.escape(tok) + r'(?![\d.])')
    out = []
    for k in members:
        for i, l in enumerate(L[k], 1):
            if k == 'main' and exclude[0] <= i <= exclude[1]: continue
            if pat.search(l): out.append((k, i))
    return out


def body(head_pat):
    """the lines of a ### section, from its heading to the next heading of the same or higher level."""
    st = None
    for i, l in enumerate(M, 1):
        if re.match(head_pat, l): st = i; break
    if st is None: return None, None, []
    for j in range(st + 1, len(M) + 1):
        if re.match(r'^#{2,3} ', M[j - 1]): return st, j - 1, [x for x in M[st:j - 1] if x.strip()]
    return st, len(M), [x for x in M[st:] if x.strip()]


print('=== (1) the six pointers into §14.5.7, and the section they point at ===')
st, en, bd = body(r'^### 14\.5\.7 ')
print('   §14.5.7 heading at L%d, next heading at L%d, NON-BLANK BODY LINES: %d' % (st, en + 1, len(bd)))
for i in (3812, 3919, 3923, 3961, 3979, 4107):
    print('   ' + show('main', i))
print('   -> all six report the content of a section with no body (13i-01/03 class, DEFERRED chat 81)')

print('=== (2) L4006 §4.6 — the pointer r2-tools reports UNRESOLVED ===')
for i, l in enumerate(M, 1):
    if re.match(r'^#{2,4} 4\.6', l) or re.match(r'^#{2,4} 4\. ', l): print('   ' + show('main', i))
h46 = [i for i, l in enumerate(M, 1) if re.search(r'\b4\.6\b', l) and i not in range(A, B + 1)]
print('   other §4.6 sites in the main volume: %d — %s' % (len(h46), ', '.join('L%d' % i for i in h46[:8])))
print('   ' + show('main', 4006))

print('=== (3) the §8.2 / §8.4 pointers of §14.6.6: which §8 is meant ===')
for i in (4246, 4250, 4254, 4256, 4257, 4259, 4265):
    print('   ' + show('main', i))
for pat, nm in ((r'^### 8\.2 ', 'main §8.2'), (r'^### 8\.4 ', 'main §8.4')):
    s2, e2, b2 = body(pat)
    print('   %s at L%d: %s' % (nm, s2, M[s2 - 1].strip()))
anec = [i for i, l in enumerate(M, 1) if 'achronal' in l and 'ANEC' in l]
print('   lines naming the achronal ANEC in the main volume: %s' % ', '.join('L%d' % i for i in anec[:10]))
g84 = [i for i, l in enumerate(M, 1) if re.search(r'^\s*#{3,5}\s*8\.4', l) and i > 11000]
print('   Appendix G (opens L%d) headings numbered 8.4: %s' %
      ([i for i, l in enumerate(M, 1) if l.startswith('## Appendix G')][0], g84 or 'none'))
v6 = [i for i, l in enumerate(M, 1) if re.search(r'\bV6\b', l)]
print('   V6 sites in the main volume: %s' % ', '.join('L%d' % i for i in v6[:12]))
for i in v6[:6]:
    if i < 4000 or i > 4269: print('      ' + show('main', i))

print('=== (4) L3858 "§28.9 gives 33 and 6" ===')
s3, e3, b3 = body(r'^### 28\.9 ')
print('   §28.9 at L%d–L%d' % (s3, e3))
for i in range(s3, e3 + 1):
    if re.search(r'\b33\b|\bE = 6\b|\b32\b|\bE = 7\b', M[i - 1]): print('   ' + show('main', i))

print('=== (5) L3987-3988 "the only place the Pauli principle enters" against §7.1 ===')
pauli = [i for i, l in enumerate(M, 1) if 'Pauli' in l and not (A <= i <= B)]
print('   Pauli sites in the main volume outside this section: %d' % len(pauli))
for i in pauli[:12]:
    print('   ' + show('main', i, 104))

print('=== (6) the self-counts of §14.6.3–§14.6.6, re-derived ===')
for i in (4151, 4164, 4167, 4181, 4192, 4195, 4234, 4267):
    print('   ' + show('main', i, 150))
print('   L4164 headline 248 = 246 + 2 : %s ; 2 of 248 = %.1f%% (printed 12%%), 22 of 248 = %.1f%%'
      % (248 == 246 + 2, 100 * 2 / 248, 100 * 22 / 248))
print('   L4164 parenthetical 197 = 191 + 6 : %s ; 6 of 197 = %.1f%% (L4192/L4267 print 3%%)'
      % (197 == 191 + 6, 100 * 6 / 197))
print('   L4151 "265 objects at this build" against L4164 "the register now holds 197" — both stated as live')
print('   L4174-4177 breakdown 6 + 9 + 6 + 1 = %d against the headline 2 unfinished, and L4181 "twenty-two"' % (6 + 9 + 6 + 1))
print('   L4167 components 162 + 9 + 2 + 2 + 1 = %d over "the 176 objects" : %s' % (162 + 9 + 2 + 2 + 1, 162 + 9 + 2 + 2 + 1 == 176))
print('   L4200-4203 the seventeen 8 + 6 + 2 + 1 = %d ; 22 − 5 named = %d' % (8 + 6 + 2 + 1, 22 - 5))
print('   L4234 "179 → 170 settled · twelve unfinished": 179 − 170 = %d, 170 + 12 = %d, 12 of 179 = %.1f%% (printed 7%%)'
      % (179 - 170, 170 + 12, 100 * 12 / 179))
print('   L4236 what remains 6 + 2 + 1 + 2 + 1 = %d' % (6 + 2 + 1 + 2 + 1))
print('   L4267 repeats 248 · 246 · 2 · 3%% after §14.6.5 reported 179/170/12 and §14.6.6 closed two more')
print('   L4195 "18,288 constraint tests across all 118": 18,288 / 118 = %.2f' % (18288 / 118))
for k, i in sites('18,288'): print('   other site: ' + show(k, i, 100))

print('=== (7) every Register entry this section cites, opened ===')
regheads = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^### ([\d, ]+)', l)
    if m:
        for n in re.findall(r'\d+', m.group(1)): regheads.setdefault(n, i)
cited = ['493', '494', '495', '496', '497', '500', '501', '502', '503', '504', '505', '506',
         '509', '510', '511', '519', '522', '527', '529', '533', '543', '544', '545',
         '596', '597', '598', '599', '600', '601', '602', '603', '604', '605', '1739']
miss = [n for n in cited if n not in regheads]
print('   cited entries with no heading in the Register: %s' % (miss or 'none'))
for n in ('497', '501', '511', '1739'):
    i = regheads.get(n)
    if i: print('   Register %s at L%d: %s' % (n, i, ' / '.join(x.strip() for x in R[i:i + 3] if x.strip())[:150]))
print('   L3915 cites Register 497 for the parent-count claim; L3946 withdraws 497 — both inside this section')

print('=== (8) the figures of this section, and their other sites ===')
for tok in ('89×', '139 to 1', '24,585', '519', '157', '102', '87', '64,804', '3,590', '3,776',
            '732', '2,535', '1,654', '13,585', '199,130', '248', '265', '197', '176', '220', '18,288'):
    s = sites(tok)
    if s: print('   %-10s %d other site(s): %s' % (tok, len(s), ', '.join('%s L%d' % (k, i) for k, i in s[:8])))
    else: print('   %-10s no other site in any member' % tok)

print('=== (9) attributions of §14.6 and §14.6.5 against the References ===')
for name in ('Colomb', 'Irlande', 'Raynaud', 'Caspard', 'Monjardet', 'Kuznetsov', 'Obiedkov',
             'Chandrasekaran', 'Flanagan', 'Brunetti', 'Fredenhagen', 'Verch', 'Wiesbrock',
             'Reeh', 'Takesaki', 'Borchers', 'Carath', 'Janet', 'Birkhoff', 'Sorce'):
    s = [(k, i) for k, i in sites(name)]
    ref = [i for k, i in s if k == 'main' and i > 11400]
    print('   %-14s %2d site(s) total, %d in the References region (main L11400+)%s'
          % (name, len(s), len(ref), '' if ref else '   <- no References entry found'))

print('=== (10) Ruling 45 / 46 candidates and self-description in this section ===')
for i in (3823, 3832, 3877, 4001, 4006, 4151, 4164, 4169, 4184, 4260, 4261):
    print('   ' + show('main', i, 150))

print('=== (11) the seed vocabulary: "seed" and "cover" outside this section ===')
for tok in ('seed(Λ₈)', 'minimum set cover', 'set cover', 'prune-greedy', 'branch and bound'):
    s = sites(tok)
    print('   %-18s %d other site(s): %s' % (tok, len(s), ', '.join('%s L%d' % (k, i) for k, i in s[:8])))
