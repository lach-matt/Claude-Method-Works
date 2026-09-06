#!/usr/bin/env python3
# r2-ch13q.py — Phase R2, chat 85.  PROSE batch for the section read of main §16.6–§16.8
# (main L4482–L4788): self-counts, pointers resolved to the claim, restated figures,
# attributions, citation chains and vocabulary.  Deterministic; no wall-clock output.

import re, collections

D = '/home/claude/members/'
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
L = {k: open(D + v, encoding='utf-8').read().split('\n') for k, v in F.items()}
M, R = L['main'], L['reg']
A, B = 4482, 4788
SEC = M[A - 1:B]


def sites(pat, vols=None, flags=0):
    out = []
    for k in (vols or F):
        for i, l in enumerate(L[k], 1):
            if re.search(pat, l, flags): out.append((k, i))
    return out


def show(k, i, w=118):
    return L[k][i - 1].strip()[:w]


print('=== r2-ch13q — prose batch, main §16.6-§16.8 (L%d-L%d, %d lines) ===' % (A, B, B - A + 1))

# ------------------------------------------------- 1. §16.6's self-count
print('\n--- 1. §16.6 L4482: "The defences are disjoint, and there are six" ---')
t1 = [i for i in range(4483, 4487) if M[i - 1].strip()]
t2 = [i for i in range(4491, 4499) if M[i - 1].strip()]
print('   first table L4483-4486  : header + %d mechanism rows' % (len(t1) - 1))
for i in t1[1:]: print('      L%d %s' % (i, show('main', i, 70)))
print('   second table L4491-4498 : header + %d mechanism rows' % (len(t2) - 1))
for i in t2[1:]: print('      L%d %s' % (i, show('main', i, 90)))
print('   L4488 says: %s' % show('main', 4488))
print('   L4489 says: %s' % show('main', 4489))
print('   L4500 says: %s' % show('main', 4500))
print('   heading count "six" ; second table rows %d ; L4500 "first four ... last three" = %d'
      % (len(t2) - 1, 4 + 3))
print('   L4572: %s' % show('main', 4572))

# ------------------------------------------------- 2. restated figures elsewhere
print('\n--- 2. figures of §16.6 restated elsewhere ---')
for pat, tag in ((r'[Tt]wenty-one structural audits', 'twenty-one structural audits'),
                 (r'ⅅ_gro', 'D_gro'), (r'ⅅ_ref', 'D_ref'), (r'ⅅ_dict', 'D_dict'),
                 (r'multiverse', 'multiverse'), (r'fifty-one terms|51 terms', 'fifty-one terms'),
                 (r'TRANSLATOR', 'TRANSLATOR'), (r'DICTIONARY', 'DICTIONARY')):
    s = sites(pat)
    print('   %-26s %d site(s): %s' % (tag, len(s), s[:8]))

# ------------------------------------- 3. the DEFERRED item: multiverse dimension / D_gro
print('\n--- 3. DEFERRED (chats 74, 83, 84): §16.6 L4482 "multiverse dimension ⅅ_gro" ---')
print('   §14.6.1 L4115: %s' % show('main', 4115))
print('   §14.6.1 L4116: %s' % show('main', 4116))
print('   occurrences of "multiverse" inside §16.6 (L4482-4519): %d'
      % sum(1 for l in M[4481:4519] if 'multiverse' in l))
print('   occurrences of "multiverse" in the whole main volume: %d'
      % sum(1 for l in M if 'multiverse' in l))
print('   what §16.6 actually grades with ⅅ_gro:')
for i in (4498, 4512, 4513, 4514):
    print('      L%d %s' % (i, show('main', i)))
print('   §29.2.2 opens L7922: %s' % show('main', 7922))
print('   "not posable" in main: %s' % sites(r'not posable', ['main'])[:6])

# ------------------------------------------------- 4. pointers resolved to the claim
print('\n--- 4. every §-pointer in range, resolved to the CLAIM ---')
CHECK = [
    (4495, '§28.8', 7721, r'index'),
    (4525, '§16.4', 1765, r'monotone function of one other'),
    (4534, '§17.2', 4806, r'adjunction never repairs'),
    (4540, '§12.11.0.4', 2725, r'separation hypothesis'),
    (4550, '§19.5', 5432, r'blocked|stated gap|ρ'),
    (4552, '§16.5', 4449, r'totality'),
    (4557, '§16.1', 4335, r'counting argument'),
    (4562, '§29.1', 7859, r'novelty'),
    (4615, '§6.2', 1594, r'Janet'),
    (4629, '§16.7.1', 4578, r'missing cell'),
    (4645, '§16.3', 4359, r'wrong value in the data'),
    (4683, '§2.13', 649, r'Commit before you look'),
    (4734, '§16.8.4', 4691, r'cost of a fabrication'),
    (4786, '§11', 2075, r'single expression'),
]
for src, ptr, head, pat in CHECK:
    end = head
    while end + 1 < len(M) and not re.match(r'^#{2,4} ', M[end]):
        end += 1
    body = '\n'.join(M[head - 1:end])
    hit = len(re.findall(pat, body, re.I))
    print('   L%-5d %-12s -> L%-5d  "%s" occurs %d time(s) in that section  %s'
          % (src, ptr, head, pat[:34], hit, 'OK' if hit else '**ZERO**'))
print('   §19.5, the exact phrase §16.6.1 attributes to it:')
print('     §16.6.1 L4551: %s' % show('main', 4551))
for p in (r'stated gap', r'unexplained absence', r'ρ = 1'):
    print('     "%s" in main: %s' % (p, sites(p, ['main'])[:6]))
print('   §6.2 Janet: %s' % sites(r'Janet', ['main'])[:10])

# ------------------------------------------------- 5. §16.7.4's "five recorded failures"
print('\n--- 5. §16.7.4 L4645: "§16.3\'s five recorded failures" ---')
print('   §16.3 runs L4359-4378 and §16.3.1 L4379-4406.  Worked cases named there:')
for i in range(4359, 4407):
    if re.search(r'Worked case|failed|wrong|Referee flag', M[i - 1]):
        print('      L%d %s' % (i, show('main', i, 100)))
print('   §16.7.4\'s own table rows (L4647-4651):')
for i in range(4647, 4652):
    if M[i - 1].strip(): print('      L%d %s' % (i, show('main', i, 100)))
print('   L4653: %s' % show('main', 4653))
for p in (r'term value below zero', r'below zero'):
    print('   "%s" in main: %s' % (p, sites(p, ['main'])[:6]))
print('   "4.9" inside §16.3 (L4359-4406): %s'
      % [i for i in range(4359, 4407) if '4.9' in M[i - 1]])

# ------------------------------------------------- 6. the fabricated cell, as worded
print('\n--- 6. §16.7.2 L4621 / §16.8.1 L4665: "spin multiplicity 2, which no atom has" ---')
for i in (4621, 4665):
    print('   L%d %s' % (i, show('main', i)))
print('   sites of the phrase "spin multiplicity": %s' % sites(r'spin multiplicity')[:10])
print('   sites of "multiplicity 2S \\+ 1" or the 2S convention being stated:')
for p in (r'2S \+ 1', r'2\*S\* \+ 1', r'multiplicity'):
    s = sites(p, ['main'])
    print('     %-16s %d site(s) in main: %s' % (p, len(s), s[:8]))
print('   NOTE the measurement is in r2-ch13p §1: the cell refused is (k=1, 2S=2);')
print('   in spectroscopic usage multiplicity 2 is a doublet, which one electron DOES have.')

# ------------------------------------------------- 7. the D >= 1 floor claim
print('\n--- 7. §16.6.2 L4568-4569: "the FIRST coordinate anywhere in this book below the ⅅ ≥ 1 floor" ---')
for p in (r'ⅅ\([a-z]+\) = 0', r'ⅅ = 0'):
    s = sites(p, ['main'])
    print('   pattern %-18s %d site(s):' % (p, len(s)))
    for k, i in s[:14]: print('      %s L%-6d %s' % (k, i, show(k, i, 96)))
print('   L4565: %s' % show('main', 4565))
print('   L4568: %s' % show('main', 4568))
print('   L4569: %s' % show('main', 4569))

# ------------------------------------------------- 8. §16.7.1's two catalogues
print('\n--- 8. §16.7.1 L4587-4612: the periodic table and the belt ---')
for i in list(range(4587, 4594)) + list(range(4599, 4613)):
    if M[i - 1].strip(): print('   L%d %s' % (i, show('main', i, 110)))
print('   "irreducible" in range: %s' % [i for i in range(A, B + 1) if 'irreducible' in M[i - 1]])
print('   the belt table shows E = 2 under (p,q) and E = 1 under both re-coordinatisations.')
print('   "118" elsewhere in main: %s' % sites(r'\b118\b', ['main'])[:10])
print('   "Janet" elsewhere: %s' % sites(r'Janet')[:10])
print('   attribution for the resonance-strength law e^|p-q|:')
for p in (r'e\^', r'resonance', r'asteroid', r'mean-motion'):
    print('     %-14s %s' % (p, sites(p, ['main'])[:8]))

# ------------------------------------------------- 9. attributions in 307 lines
print('\n--- 9. attribution and citation density in the section (13l-04 class) ---')
names = ['Racah', 'Edlén', 'Ritz', 'Paschen', 'Götze', 'Dunz', 'Rydberg', 'Freuder',
         'Moore', 'Gödel', 'Birkhoff', 'Janet']
for nm in names:
    inr = [i for i in range(A, B + 1) if nm in M[i - 1]]
    allm = sites(re.escape(nm))
    print('   %-9s in §16.6-§16.8: %-14s   sites in all six volumes: %d'
          % (nm, inr if inr else 'none', len(allm)))
print('   Register citations in range: %s'
      % sorted({m for i in range(A, B + 1) for m in re.findall(r'Register (\d+)', M[i - 1])}))
print('   "Registers" (plural, the counted form) in range: %s'
      % [i for i in range(A, B + 1) if 'Registers' in M[i - 1]])
for n in ('403', '404', '405', '349'):
    hit = [i for i, l in enumerate(R, 1) if re.match(r'^### (\d+[, ]*)*\b%s\b' % n, l)]
    print('   Register %-4s -> reg L%s  %s' % (n, hit[:1], show('reg', hit[0] + 1) if hit else 'NOT FOUND'))

# ------------------------------------------------- 10. the back-matter Index
print('\n--- 10. §16.6.1 L4522: "its back-matter Index carries fifty-one terms" ---')
ix = [i for i, l in enumerate(M, 1) if re.match(r'^## .*\bIndex\b', l)]
print('   main-volume headings matching "Index": %s' % [(i, show('main', i, 60)) for i in ix])
for h in ix:
    end = h
    while end + 1 < len(M) and not re.match(r'^## ', M[end]):
        end += 1
    ent = [l for l in M[h:end] if re.match(r'^\s*(\*\*)?[A-Za-zΛℛⅅ]', l) and ',' in l]
    print('   under L%d: %d non-blank body lines, %d look like index entries' % (h, sum(1 for l in M[h:end] if l.strip()), len(ent)))

# ------------------------------------------------- 11. Figure 16.2 registry (13o-05 class)
print('\n--- 11. Figure 16.2: registered line vs placed line ---')
for mem in ('FIGURE_ASSETS.md', 'FIGURE_MAP.md'):
    try:
        txt = open(D + mem, encoding='utf-8').read().split('\n')
    except OSError:
        print('   %s not a member' % mem); continue
    for i, l in enumerate(txt, 1):
        if re.search(r'16\.2', l): print('   %s L%d: %s' % (mem, i, l.strip()[:110]))
print('   placed at main L%s' % [i for i in range(A, B + 1) if '![Figure 16.2]' in M[i - 1]])

# ------------------------------------------------- 12. §16.8.6's self-contradiction
print('\n--- 12. §16.8.6 L4784-4786 against its own table ---')
for i in range(4778, 4788):
    if M[i - 1].strip(): print('   L%d %s' % (i, show('main', i, 115)))
print('   the table prints one row where the two operators agree (2S <= k, 74 / 74),')
print('   while L4786 states they "agree on Λ and nowhere else"; r2-ch13p §8 measures')
print('   agreement on Λ ∪ {y} for 30/30 of 2S <= k and 30/30 of g <= q.')

# ------------------------------------------------- 13. headings and layout in range
print('\n--- 13. headings in range, and truncation (13o-04 class) ---')
for i in range(A, B + 1):
    if M[i - 1].startswith('#'):
        nxt = M[i].strip() if i < len(M) else ''
        flag = ''
        if nxt and not nxt.startswith(('#', '|', '!')) and M[i].startswith('    '):
            flag = '   <-- next line is an indented block'
        print('   L%-5d %s%s' % (i, M[i - 1][:96], flag))
print('   §16.3 L4366 (chat 84 range) ends: %r' % M[4365][-46:])
print('   §16.3 L4367 blank: %s ; L4368 starts: %r' % (not M[4366].strip(), M[4367][:52]))

print('\n=== end r2-ch13q ===')
