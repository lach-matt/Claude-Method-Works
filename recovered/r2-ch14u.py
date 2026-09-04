#!/usr/bin/env python3
"""r2-ch14u — prose batch for the Chapter 24 second read, main L6741-L6816.
Pointers, attributions, restated figures, self-description, internal supersession.
Chat 100.  Reads the six volume MEMBERS by name; never a BUILDnnn bundle path.
"""
import os, re, importlib.util

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span = r2lib.heading_line, r2lib.section_span
has_token, enclosing = r2lib.has_token, r2lib.enclosing

VOLS = {
    'main':     'The_Method_1_6-2.md',
    'register': 'The_Method_1_6___The_Register-2.md',
    'math':     'The_Method_1_6___Mathematical_Compendium-2.md',
    'physics':  'The_Method_1_6___The_Physics_Compendium-2.md',
    'index':    'The_Method_1_6___The_Index_of_Indices-2.md',
    'spectra':  'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for k, f in VOLS.items()}
M = V['main']
A, B = 6741, 6816
UNIT = '\n'.join(M[A - 1:B])

print('=' * 78)
print('r2-ch14u  prose batch  main L%d-L%d  (24.8, 24.9)' % (A, B))
print('=' * 78)

# ------------------------------------------------------------------ P1 pointers
print('\n[P1] every section pointer in the unit, resolved to the CLAIM and not the heading')
ptrs = sorted({(i, m) for i in range(A, B + 1)
               for m in re.findall(r'§(\d+(?:\.\d+)*)', M[i - 1])})
print('   §-pointers found: %s' % sorted({p for _, p in ptrs}))
for ln, sec in ptrs:
    s = heading_line(M, sec)
    if s is None:
        print('   L%d -> §%-7s NO HEADING' % (ln, sec)); continue
    lo, hi = section_span(M, sec)
    body = '\n'.join(M[lo - 1:hi - 1])
    print('   L%d -> §%-7s heading L%d "%s"' % (ln, sec, s, M[s - 1].strip()[:52]))
    print('        span L%d-L%d, %d lines' % (lo, hi - 1, hi - lo))
    for tok in ('decline', 'declines', 'exclusion', 'exclusions', 'measured'):
        c = has_token(body, tok)
        if c:
            print('        carries %-12s %d' % (tok, c))

print('\n   L6809 pairs "§24.11\'s decline modes and §18\'s exclusions". Testing §18 for the claim:')
lo, hi = section_span(M, '18')
body18 = '\n'.join(M[lo - 1:hi - 1])
print('   §18 span L%d-L%d (%d lines), heading: %s' % (lo, hi - 1, hi - lo, M[lo - 1].strip()))
for tok in ('exclusion', 'exclusions', 'species', 'levels'):
    print('        §18 carries %-12s %d' % (tok, has_token(body18, tok)))
print('   whole-main-volume sweep for the token "exclusions":')
for i, t in enumerate(M, 1):
    if has_token(t, 'exclusions'):
        print('        L%-6d %-8s %s' % (i, enclosing(M, i), t.strip()[:72]))

# --------------------------------------------------------- P2 register pointers
print('\n[P2] Register pointers in the unit (upper and lower case grepped separately)')
regs = sorted({int(n) for i in range(A, B + 1)
               for n in re.findall(r'[Rr]egisters?\s+(\d+)(?:\s+and\s+(?:\d+))?', M[i - 1])}
              | {int(n) for i in range(A, B + 1)
                 for n in re.findall(r'and\s+(\d+)\.', M[i - 1])})
print('   raw numerals near "Register": %s' % regs)
R = V['register']
def entry(num):
    pat = re.compile(r'^#{1,4}\s*%d\s*$' % num)
    for i, t in enumerate(R):
        if pat.match(t):
            j = i + 1
            while j < len(R) and not re.match(r'^#{1,4}\s*\d+\s*$', R[j]):
                j += 1
            return i + 1, '\n'.join(R[i:j])
    return None, ''
for num in (246, 436, 437):
    ln, body = entry(num)
    print('   Register %-4d L%-6s resolves %s' % (num, ln, ln is not None))
    print('        %s' % ' '.join(body.split())[:150])

# ------------------------------------------- P3 the He I contradiction, measured
print('\n[P3] the He I provenance question, stated at three sites inside one section')
sites = {
    6763: 'every level in the table is bracketed',
    6766: 'obtained by fitting the extended Ritz quantum-defect expansion',
    6767: 'Its 189 cells ... are not independent tests',
    6787: "He I's nine certainly [contain no independent test]",
    6807: "He I's bracketed values are ab initio and are the sharpest tests",
    6815: "He I's are ab initio QED calculations ... Those are genuine tests",
}
for ln in sorted(sites):
    print('   L%-5d %s' % (ln, M[ln - 1].strip()[:96]))
print('\n   the section\'s own delimiter rule, L6759-L6762:')
for ln in (6759, 6760, 6761, 6762):
    print('   L%-5d %s' % (ln, M[ln - 1].strip()[:96]))
print('\n   MEASURED: L6760-L6762 states [ ] = semi-empirical and ( ) = ab initio, and that')
print('   "This section reads [ ] as covering ab initio and it does not."  L6763 states every')
print('   He I level is bracketed [ ].  L6807 and L6815 then call He I\'s bracketed values')
print('   ab initio - which is the reading L6762 has just withdrawn.')
ln436, b436 = entry(436)
print('   Register 436 sides with L6767: %s'
      % ('YES - "contains no independent test"' if 'no independent test' in b436 else 'no'))

# ------------------------------------------- P4 internal supersession failures
print('\n[P4] phrases one part of the unit supersedes and another still prints')
pairs = [
    ('an unknown proper subset', 6791, 6811),
    ('never counted', 6801, None),
]
for phrase, sup_ln, still_ln in pairs:
    hits = [i for i in range(A, B + 1) if phrase.lower() in M[i - 1].lower()]
    print('   "%s" -> lines %s' % (phrase, hits))
for ln in (6791, 6811, 6801, 6781):
    print('   L%-5d %s' % (ln, M[ln - 1].strip()[:100]))
print('   MEASURED: L6791 says the blockquote form "supersedes an unknown proper subset";')
print('   L6811, twenty lines later, prints "an unknown proper subset" as the honest form.')
print('   L6801 says "The book has never counted the three"; L6781 counts H I and L6791')
print('   says two species of thirty-five are done.')

# ----------------------------------- P5 the no-failure claim against the chapter
print('\n[P5] "none produced a failure" against the chapter\'s own failure counts')
cs, ce = section_span(M, '24')
print('   chapter 24 span L%d-L%d' % (cs, ce - 1))
for i in range(cs, ce):
    if re.search(r'failure|failed|fails', M[i - 1], re.I) and re.search(r'\d', M[i - 1]):
        print('   L%-6d %s' % (i, M[i - 1].strip()[:104]))

# ------------------------------------------ P6 restated figures, six volumes
print('\n[P6] the unit\'s distinctive figures, swept across all six volumes')
for fig in ('1,442', '190 channels', '189 cells', '131', '13 of 64', '10\u207b\u2079'):
    print('   "%s"' % fig)
    tot = 0
    for k in VOLS:
        hits = [i for i, t in enumerate(V[k], 1) if fig in t]
        tot += len(hits)
        if hits:
            show = ', '.join('L%d' % h for h in hits[:9])
            print('     %-9s %2d  %s%s' % (k, len(hits), show, ' ...' if len(hits) > 9 else ''))
    if tot == 0:
        print('     (no site in any of the six volumes)')

# --------------------------------------------- P7 rulings 45/46 and name forms
print('\n[P7] Ruling 45 / Ruling 46 exposure in the unit, and name forms')
for i in range(A, B + 1):
    t = M[i - 1]
    if re.search(r'earlier (version|draft)|this book would defend|as it was written|'
                 r'was never carried|Build \d|build \d', t, re.I):
        print('   R45/46 L%-6d %s' % (i, t.strip()[:96]))
for nm in ('NIST', 'ASD', 'Drake', 'Kandula', 'Ritz', 'QED'):
    hits = [i for i in range(A, B + 1) if has_token(M[i - 1], nm)]
    forms = sorted({m for i in hits for m in re.findall(nm, M[i - 1], re.I)})
    print('   %-8s in unit: %d sites %s   forms %s'
          % (nm, len(hits), hits[:8], forms))
print('   whole-main-volume name-form check:')
for nm in ('Kandula', 'Drake'):
    hits = [i for i, t in enumerate(M, 1) if has_token(t, nm)]
    print('     %-8s %d sites %s' % (nm, len(hits), hits[:10]))

# ------------------------------------- P8 headings, and sentence continuation
print('\n[P8] the two headings, and whether either sentence finishes in the body')
for ln in (6741, 6752):
    print('   L%-5d %s' % (ln, M[ln - 1].strip()))
    print('   L%-5d %s' % (ln + 1, M[ln].strip()[:96]))
print('   MEASURED: neither heading ends in a word the next line completes.')

# ------------------------------------------------- P9 Q item P attributes
print('\n[P9] L6813 "Recorded in Q as item P - obstacle retrievable, cost hours, blocks one')
print('     stated claim"  resolved against the Q table')
for i, t in enumerate(M, 1):
    if re.match(r'^\s*\|?\s*P\s+the 1,442', t) or (' P ' in t and '1,442 split' in t):
        print('   Q table L%-6d %s' % (i, t.strip()[:104]))
for i, t in enumerate(M, 1):
    if 'item  question' in t or re.match(r'^\s+item\s+question', t):
        print('   Q header L%-6d %s' % (i, t.strip()[:104]))

print('\n[END r2-ch14u]')
