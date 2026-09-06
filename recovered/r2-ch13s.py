#!/usr/bin/env python3
# r2-ch13s.py — chat 86, prose batch for the section read of main Chapter 17 (L4789-L4921).
# Pointers, attributions, restated figures, self-description, citation chains, vocabulary.
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
L = {k: r2lib.read_member(f).split('\n') for k, f in V.items()}
M = L['main']

def show(vol, a, b, w=150):
    for i in range(a, b + 1):
        if 1 <= i <= len(L[vol]): print('  %s L%-6d %s' % (vol, i, L[vol][i - 1][:w]))
def find(vol, pat, a=1, b=None, w=150, cap=12):
    b = b or len(L[vol]); out = []
    for i in range(a, min(b, len(L[vol])) + 1):
        if re.search(pat, L[vol][i - 1]): out.append((i, L[vol][i - 1][:w]))
    for i, t in out[:cap]: print('  %s L%-6d %s' % (vol, i, t))
    if len(out) > cap: print('  ... %d more' % (len(out) - cap))
    return out
def span(pat_open, pat_next):
    a = next(i for i, l in enumerate(M, 1) if re.match(pat_open, l))
    b = next(i for i, l in enumerate(M, 1) if i > a and re.match(pat_next, l)) - 1
    return a, b

print('== r2-ch13s : main Chapter 17, prose batch ==')
print('Chapter 17 runs main L4789-L4921 (heading scan, this chat); Chapter 18 opens L4922.')

print('\n-- P1. L4792 "three operations" against L4812 "three repair routes" --')
show('main', 4792, 4792); show('main', 4812, 4812, 220)

print('\n-- P2. L4806 Theorem 17.1 : its other sites, resolved to the claim --')
for ln in (3587, 4534, 10558):
    show('main', ln, ln, 200)

print('\n-- P3. L4812 "The calendar of Chapter 6 is repaired by reordering" --')
a, b = span(r'^## 6\. ', r'^## 7\. ')
print('  Chapter 6 runs main L%d-L%d' % (a, b))
c = find('main', r'calendar', a, b, cap=6)
print('  occurrences of "calendar" in Chapter 6: %d' % len(c))
allc = find('main', r'[Cc]alendar', 1, None, cap=0)
print('  occurrences of "calendar" in the whole main volume: %d, at lines %s'
      % (len(allc), [i for i, _ in allc][:14]))
for i, t in allc[:6]: print('   main L%-6d %s' % (i, t[:150]))

print('\n-- P4. L4815 "three wrong statements ... recorded in Chapter 28" --')
show('main', 4814, 4818, 200)
a, b = span(r'^## 28\. ', r'^## 29\. ')
print('  Chapter 28 runs main L%d-L%d' % (a, b))
w = find('main', r'E3|constraint.*impos|impos.*constraint', a, b, cap=10)
print('  Chapter 28 lines mentioning E3 or imposable constraints: %d' % len(w))

print('\n-- P5. L4815-L4817 : the colon at "The criterion is:" and what follows it --')
print('  L4815 ends with a colon introducing the criterion; the next non-blank line is L4817.')
show('main', 4815, 4817, 220)
print('  the E3 criterion itself is printed at L4860, forty-three lines later:')
show('main', 4860, 4860, 200)

print('\n-- P6. L4831 "the three ambients of §14.5" --')
show('main', 3738, 3741, 120)

print('\n-- P7. L4834 "§4.6" (r2-tools reports UNRESOLVED) --')
find('main', r'^#+ 4\.[5-7]', cap=6)
show('main', 4834, 4834, 200)

print('\n-- P8. L4844 "Register 449" and L4858 "Register 440" --')
for n in (449, 440):
    hits = [i for i, l in enumerate(L['reg'], 1) if re.match(r'^### %d\b' % n, l)]
    for i in hits: show('reg', i, i + 2, 200)

print('\n-- P9. L4849 "§18.2 refuses nu = e - delta as an axis" --')
a, b = span(r'^### 18\.2 ', r'^### 18\.3 ')
show('main', a, b, 200)

print('\n-- P10. L4854 "§12.11.2\'s second excluded form" --')
a, b = span(r'^### 12\.11\.2 ', r'^### 12\.11\.3')
find('main', r'excluded|form', a, b, cap=10)

print('\n-- P11. L4857 "Seniority parity at axis 10, the conjugation ceiling at axis 12" --')
show('main', 4857, 4858, 220)
find('main', r'axis 9|axis 10|axis 11|axis 12|axis 13', 1, None, cap=14)

print('\n-- P12. L4886 / L4899 "of §16.4 form" (the 13o-01 class, eight sites) --')
sites = []
for k in L:
    for i, l in enumerate(L[k], 1):
        if re.search(r'§16\.4', l): sites.append((k, i, l[:170]))
print('  sites of "§16.4" across all six volumes: %d' % len(sites))
for k, i, t in sites: print('   %s L%-6d %s' % (k, i, t))
print('  §16.4 heading:'); find('main', r'^### 16\.4 ', cap=2)

print('\n-- P13. L4894 "Conservation is a bound on a sum, which §7.1 excludes" --')
a, b = span(r'^### 7\.1 ', r'^### 7\.2 ')
print('  §7.1 runs main L%d-L%d' % (a, b))
find('main', r'sum|exclu', a, b, cap=10)

print('\n-- P14. L4912 "This is P16 — treat bounds as coordinate values" --')
find('main', r'\bP16\b', cap=10)

print('\n-- P15. L4920 "the cost surface of Chapter 23 carries none beyond nu" --')
a, b = span(r'^## 23\. ', r'^## 24\. ')
print('  Chapter 23 runs main L%d-L%d' % (a, b))
find('main', r'no independent|carries none|beyond ν|reduces to ν', a, b, cap=8)

print('\n-- P16. L4916-L4918 : the S3 / D3 / S2 table of §17.5 --')
show('main', 4915, 4920, 200)
for tag in ('S3', 'D3', 'S2'):
    print('  sites of %s in the main volume:' % tag)
    find('main', r'\b%s\b' % tag, cap=6)

print('\n-- P17. attribution in Chapter 17 : every proper name in 133 lines --')
NAMES = r'Birkhoff|Janet|Racah|Freuder|Rota|Lauritzen|Noether|Edl|Ritz|Paschen|Dunz|Slater|Condon|Shortley|Dedekind|Stone|Gr[aä]tzer|Davey|Priestley'
find('main', NAMES, 4789, 4921, cap=10)

print('\n-- P18. restated figures : "288", "424", "2,513", "86%", "89,864" elsewhere --')
for fig in (r'\b288\b', r'\b424\b', r'2,513', r'86\s*%', r'89,864', r'979,300', r'45,690', r'1,040\b'):
    hits = []
    for k in L:
        for i, l in enumerate(L[k], 1):
            if re.search(fig, l): hits.append('%s:L%d' % (k, i))
    print('  %-10s %d sites : %s' % (fig, len(hits), ', '.join(hits[:14])))

print('\n-- P19. main L2260-L2261 : §11.7 cites itself for the 89,864 --')
a, b = span(r'^### 11\.7 ', r'^### 11\.8 ')
print('  §11.7 runs main L%d-L%d ; L2261 lies inside it: %s' % (a, b, a <= 2261 <= b))
show('main', 2260, 2262, 200)

print('\n-- P20. inbound descriptions of Chapter 17 (13f-05\'s site among them) --')
show('main', 3673, 3673, 200)
find('main', r'Chapter 17|§17\.', 1, 4788, cap=14)

print('\n-- P21. §17.5 and the contents list --')
show('main', 11450, 11452, 160)

print('\n== end r2-ch13s ==')
