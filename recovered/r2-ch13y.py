#!/usr/bin/env python3
# r2-ch13y.py — chat 89 — PROSE batch for the Chapter 20 section read (main L5551-L5596).
# Every pointer resolved to the CLAIM, not the heading. Deterministic; prints no wall-clock time.

import os, re
H = os.path.dirname(os.path.abspath(__file__))
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in F.items()}
M = V['main']
A, B = 5551, 5596


def L(i): return M[i - 1]


# lifted verbatim from r2-ch13w.py (chat 88) — the exact-token heading resolver
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


print('-- 1. every Chapter 20 pointer resolved to the CLAIM --')
CLAIMS = [
    (5554, '21', 'states what the language claims have in common',
     ['language is a coordinate system', 'translation']),
    (5564, '1', "table gives five languages with their closure mechanisms and their MEASURED costs",
     ['tree factorisation', 'documentary', '0.00018']),
    (5567, '29', 'the precedent question can be bounded and never settled',
     ['bound', 'novelty']),
    (5568, '29.1', "two searches returning nothing", ['two searches']),
    (5574, '16', 'the constraint language of section 16', ['constraint language']),
    (5579, '27', 'proves that where they measure the same thing they agree',
     ['E(X)', 'void', 'V']),
    (5585, '12.11.2', 'the congruence is one of its three excluded forms',
     ['sums', 'differences', 'symmetric', 'congruence']),
    (5586, '14.4', "section 14.4's operator cannot carry it", ['operator']),
    (5592, '17.3', 'a difference is bracketed; convexity is closure for a bracketed quantity',
     ['interval property', 'convex', 'difference']),
]
for site, sec, what, keys in CLAIMS:
    t, e, bd = body(sec)
    if t is None:
        print('   L%-5d sec %-9s UNRESOLVED' % (site, sec)); continue
    low = bd.lower()
    found = [k for k in keys if k.lower() in low]
    print('   L%-5d sec %-9s -> L%-5d-%-5d  keys %d/%d  missing %s  %s'
          % (site, sec, t, e, len(found), len(keys),
             [k for k in keys if k not in found][:4],
             'CLAIM PRESENT' if len(found) == len(keys) else 'CLAIM SHORT'))

print()
print('-- 2. section 16 and the "constraint language" --')
t, e, bd = body('16')
print('   section 16 extent L%d-L%d;  "constraint language" occurrences in it: %d'
      % (t, e, len(re.findall(r'constraint language', bd, re.I))))
print('   volume-wide sites of "constraint language":',
      [i for i, x in enumerate(M, 1) if re.search(r'constraint language', x, re.I)])

print()
print('-- 3. section 14.4 and its "operator" --')
t, e, bd = body('14.4')
print('   section 14.4 extent L%d-L%d (%d lines); text: %r'
      % (t, e, e - t + 1, ' '.join(x.strip() for x in M[t - 1:e] if x.strip())[:120]))
print('   "operator" occurrences in section 14.4:', len(re.findall(r'operator', bd, re.I)))
t2, e2, b2 = body('14.2')
print('   section 14.2 heading: %r  ("operator" x%d)'
      % (M[t2 - 1].strip(), len(re.findall(r'operator', b2, re.I))))
print('   section 14.4 lists how many of its "three properties"? named items:',
      len(re.findall(r'^\s*[-*\d]', '\n'.join(M[t:e]), re.M)))

print()
print('-- 4. section 12.11.2 - which triple is which --')
t, e, bd = body('12.11.2')
print('   extent L%d-L%d' % (t, e))
print('   L3364-3365 (the three excluded forms):', ' '.join(x.strip() for x in M[3363:3365])[:150])
print('   "congruence" occurrences in 12.11.2:', len(re.findall(r'congruence', bd, re.I)))
print('   the CONGRUENCE is named at L3373 as one of the three MACHINES:',
      'three machines' in ' '.join(M[3370:3374]).lower() or 'Three machines' in ' '.join(M[3370:3374]))
print('   12.11.8 L3582 classifies the parity rule:', M[3581].strip()[:130])

print()
print('-- 5. section 29.1 and the search count --')
t, e, bd = body('29.1')
print('   extent L%d-L%d' % (t, e))
for i in range(t, e + 1):
    if re.search(r'search|literatur', M[i - 1], re.I):
        print('   L%d| %s' % (i, M[i - 1].strip()[:150]))
print('   "two searches" volume-wide:',
      [i for i, x in enumerate(M, 1) if 'two searches' in x.lower()])
print('   "nine" in 29.1:', len(re.findall(r'\bnine\b', bd, re.I)))

print()
print("-- 6. Chapter 1's table (L400-L406): rows, mechanisms, timings --")
rows = [M[i - 1] for i in range(402, 407)]
for i, r in enumerate(rows, 402):
    print('   L%d| %s' % (i, r.strip()[:120]))
nomech = [i for i, r in zip(range(402, 407), rows) if re.search(r'\|\s*—\s*\|', r)]
print('   rows in the table:', len(rows))
print('   rows whose mechanism cell is an em dash:', nomech)
print('   rows carrying a MEASURED timing (from L408, outside the table): 2 '
      '(tree factorisation, Grobner)')
print('   rows with no measured timing: %d' % (len(rows) - 2))
print('   L408:', M[407].strip()[:200])
print('   the table\'s cost column is complexity, not measured cost:',
      all(k in ' '.join(rows) for k in ['one pass', 'doubly exponential', 'triply exponential']))

print()
print('-- 7. the six languages: canon vs section 20.2 --')
canon = []
for i in range(2083, 2092):
    m = re.match(r'\s{2}(\w+)\s{2,}', M[i - 1])
    if m and m.group(1) not in ('language',):
        canon.append(m.group(1))
print('   section 11.1 table names:', canon)
print('   section 20.2 L5573-5574 names: order, geometry, arithmetic, calculus, logic,'
      ' the constraint language of section 16')
print('   in canon and not in 20.2:', [c for c in canon if c in ('algebra', 'analysis', 'information')])
print('   section 11.1 heading:', M[2078].strip())
print('   section 11.1.1 heading:', M[2093].strip())
print('   Register site for seven languages:',
      [i for i, x in enumerate(V['reg'], 1) if 'SEVEN LANGUAGES' in x])
print('   combinations involving "information" among the ten of 11.2:',
      len([i for i in range(2178, 2207) if 'information' in M[i - 1].lower()]))

print()
print('-- 8. logic as a language: the Register and the Mathematical Compendium --')
for i, x in enumerate(V['reg'], 1):
    if 'LOGIC IS NOT A LANGUAGE' in x:
        print('   reg L%d| %s' % (i, x.strip()[:170]))
for i, x in enumerate(V['mc'], 1):
    if re.search(r'LOGIC is not a language', x):
        print('   mc  L%d| %s' % (i, x.strip()[:170]))
print('   main L2090 (11.1 lists logic as a language):', M[2089].strip()[:110])

print()
print('-- 9. "Fifty sections make a claim about language, and no chapter owns one" --')
heads = [(i, t) for i, t in enumerate(M, 1) if re.match(r'^#{2,4} \d', t)]
cnt = 0
for k, (i, t) in enumerate(heads):
    end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len(M)
    if i >= A:
        continue
    if re.search(r'\blanguages?\b', '\n'.join(M[i - 1:end]), re.I):
        cnt += 1
print('   sections before L%d whose body contains "language(s)": %d  (text says fifty)' % (A, cnt))
chap = [t for i, t in heads if re.match(r'^## \d', t) and re.search(r'language', t, re.I)]
print('   chapters with "language" in the title:', chap)

print()
print('-- 10. register citations inside Chapter 20 (case-insensitive) --')
hits = [(i, m.group(0)) for i in range(A, B + 1)
        for m in re.finditer(r'[Rr]egisters?\s+\d+', L(i))]
print('   found:', hits if hits else 'none — Chapter 20 cites the Register zero times')

print()
print('-- 11. the Mathematical Compendium on the same claim --')
for i, x in enumerate(V['mc'], 1):
    if re.search(r'all ten pairs hold|C\(6, ?2\)|C\(5, ?2\)', x):
        print('   mc L%d| %s' % (i, x.strip()[:190]))

print()
print('-- 12. section 27 and the three names --')
t, e, bd = body('27')
print('   extent L%d-L%d;  "prove" occurrences: %d' % (t, e, len(re.findall(r'prov', bd, re.I))))
for k in ['E(X)', 'void', 'slack']:
    print('   %-8s in 27: %s' % (k, k in bd))
print('   main L5610 (Ch21 row):', M[5609].strip()[:120])

print()
print('-- 13. the two 4-space display paragraphs, against the volume convention --')
disp = [i for i, x in enumerate(M, 1) if re.match(r'^    \S', x)]
print('   4-space display lines in the volume: %d; inside Chapter 20: %s'
      % (len(disp), [i for i in disp if A <= i <= B]))

print()
print('-- 14. census rows 1124 and 1125 --')
for r in open(os.path.join(H, 'DEFECT-CENSUS.tsv'), encoding='utf-8').read().split('\n'):
    if r.startswith('1124\t') or r.startswith('1125\t'):
        print('   ', r[:120])

print()
print('-- 15. Parts II, III and V --')
for i, x in enumerate(M, 1):
    if re.match(r'^# PART ', x):
        print('   L%d| %s' % (i, x.strip()[:80]))
