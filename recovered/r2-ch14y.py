#!/usr/bin/env python3
# r2-ch14y.py - prose batch for the Chapter 25 first read (main L6884-L6990, S25 through S25.5).
# Reads the six volume MEMBERS by name; never opens a BUILDnnn bundle path.
# Resolvers imported from r2lib by path and given the LINE LIST.
import importlib.util, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(HERE, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOL = {'main': 'The_Method_1_6-2.md', 'register': 'The_Method_1_6___The_Register-2.md',
       'math': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'phys': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'spectra': 'The_Method_1_6___Spectra_Compendium-2.md'}
LN = {v: open(os.path.join(HERE, VOL[v]), encoding='utf-8').read().split('\n') for v in VOL}
M = LN['main']
UNIT = (6884, 6990)

def strip_em(s):
    return re.sub(r'[*_`]', '', s)

def token_sites(vol, tok, lo=None, hi=None):
    out = []
    for i, l in enumerate(LN[vol], start=1):
        if lo and not (lo <= i <= hi):
            continue
        if has_token(strip_em(l), tok):
            out.append(i)
    return out

print('=== r2-ch14y  Chapter 25 first read, prose batch  (main L%d-L%d) ===' % UNIT)

# ---------------------------------------------------------------- Y1  14t-06 resolved at S25.2
print('\n[Y1] 14t-06: L6809 points at "S18\'s exclusions"; the docket names S25.2 as the target')
print('   L6809 verbatim: %s' % strip_em(M[6808]).strip()[:300])
lo, hi = section_span(M, '25.2')
print('   S25.2 span measured: L%d-L%d' % (lo, hi))
for form in ('exclusion', 'exclusions', 'exclude', 'excluded', 'excludes', 'declines', 'decline'):
    ins = [n for n in token_sites('main', form) if lo <= n <= hi]
    print('      %-11s in S25.2: %d  %s' % (form, len(ins), ','.join('L%d' % n for n in ins)))
lo18, hi18 = section_span(M, '18')
print('   S18 span L%d-L%d, for the negative that put the docket here:' % (lo18, hi18))
for form in ('exclusion', 'exclusions', 'exclude', 'excluded', 'excludes'):
    ins = [n for n in token_sites('main', form) if lo18 <= n <= hi18]
    print('      %-11s in S18: %d %s' % (form, len(ins), ','.join('L%d' % n for n in ins[:6])))

# ---------------------------------------------------------------- Y2  the competing five/N pairings
print('\n[Y2] the five/N pairings: front matter L62, S24.11, S24.12, S25.2')
print('   L62   : %s' % strip_em(M[61]).strip()[:260])
print('   L6891 : %s' % strip_em(M[6890]).strip()[:260])
print('   L6926-L6927 (the reduction): %s' % ' '.join(strip_em(M[i]).strip() for i in (6925, 6926))[:300])
for sec in ('24.11', '24.12'):
    a, b = section_span(M, sec)
    print('   S%-5s span L%d-L%d' % (sec, a, b))
    for n in range(a, b + 1):
        t = strip_em(M[n - 1])
        if re.search(r'\b(five|four|three)\b', t) and re.search(r'\b(sequence|mode|mechanism|exclusion|decline)', t):
            print('      L%-5d %s' % (n, t.strip()[:200]))
print('   sequences named in S24.12 (Cr-, Mn-, Fe-, Co-, Ni-like) inside S25.2?')
a, b = section_span(M, '25.2')
for sp in ('Cr', 'Mn', 'Fe', 'Co', 'Ni', 'isoelectronic', 'sequence'):
    ins = [n for n in token_sites('main', sp) if a <= n <= b]
    print('      %-13s %d sites in S25.2' % (sp, len(ins)))

# ---------------------------------------------------------------- Y3  pointers out of the unit
print('\n[Y3] every S-pointer in the unit, resolved to the CLAIM not the heading')
ptr = re.compile(r'\u00a7\s*(\d+(?:\.\d+)*)')
seen = []
for n in range(UNIT[0], UNIT[1] + 1):
    for m in ptr.finditer(strip_em(M[n - 1])):
        seen.append((n, m.group(1)))
for n, sec in seen:
    hl = heading_line(M, sec)
    sp = section_span(M, sec) if hl else (None, None)
    print('   L%-5d -> S%-7s heading %s  span %s' % (n, sec, ('L%d' % hl) if hl else 'NOT FOUND', sp))
    if hl:
        print('        heading text: %s' % strip_em(M[hl - 1]).strip()[:120])
print('   the two claims the pointers carry:')
a, b = section_span(M, '25.6')
rin = [n for n in range(a, b + 1) if re.search(r'(?<![\w.])r\s*<\s*5', strip_em(M[n - 1]))]
print('      "r < 5" inside S25.6 (L%d-L%d): %s' % (a, b, ','.join('L%d' % n for n in rin) or 'NO SITE'))
a, b = section_span(M, '23.11')
vin = [n for n in range(a, b + 1) if 'nu_V' in strip_em(M[n - 1]) or '\u03bd_V' in strip_em(M[n - 1]) or '\u03bd_v' in strip_em(M[n - 1])]
print('      "nu_V" inside S23.11 (L%d-L%d): %s' % (a, b, ','.join('L%d' % n for n in vin) or 'NO SITE'))

# ---------------------------------------------------------------- Y4  Rule 3, and the rules named in the unit
print('\n[Y4] Rule 3, cited twice in S25.2 as direction-agnostic and as a min/max form')
for v in ('main', 'math', 'register'):
    hits = [i for i, l in enumerate(LN[v], start=1) if re.search(r'\bRule 3\b', strip_em(l))]
    print('   %-9s %d sites %s' % (v, len(hits), ','.join('L%d' % n for n in hits[:12])))
for i in [n for n, l in enumerate(M, start=1) if re.search(r'\bRule 3\b', strip_em(l))][:6]:
    print('      main L%-5d %s' % (i, strip_em(M[i - 1]).strip()[:190]))

# ---------------------------------------------------------------- Y5  the retired-basis shape in this unit
print('\n[Y5] "An earlier version" and the figures it retires (docket 15)')
for v in VOL:
    hits = [i for i, l in enumerate(LN[v], start=1) if re.search(r'[Aa]n earlier version', strip_em(l))]
    if hits:
        print('   %-9s %d sites %s' % (v, len(hits), ','.join('L%d' % n for n in hits)))
for tok in ('35.3', '41.2', '58.8', '79', '60'):
    per = {v: [i for i, l in enumerate(LN[v], start=1)
               if re.search(r'(?<![\d.,])' + re.escape(tok) + r'(?![\d.,])', strip_em(l))] for v in VOL}
    inunit = [n for n in per['main'] if UNIT[0] <= n <= UNIT[1]]
    print('   %-5s total %3d | in unit %d: %s' % (tok, sum(len(x) for x in per.values()),
                                                  len(inunit), ','.join('L%d' % n for n in inunit) or '-'))

# ---------------------------------------------------------------- Y6  the species the unit names, across six volumes
print('\n[Y6] the species named in the unit, sited across the six volumes')
for sp in ('Sr I', 'Ti I', 'Sc VI', 'Hg II', 'Ca II', 'Ba II'):
    per = {}
    for v in VOL:
        per[v] = [i for i, l in enumerate(LN[v], start=1) if re.search(r'\b' + sp.replace(' ', r'\s') + r'\b', strip_em(l))]
    print('   %-6s %s' % (sp, ' | '.join('%s %d' % (v, len(per[v])) for v in VOL if per[v]) or 'NO SITE IN ANY VOLUME'))
    if per.get('spectra'):
        print('        spectra sites: %s' % ','.join('L%d' % n for n in per['spectra'][:8]))

# ---------------------------------------------------------------- Y7  name-form sweep inside the unit
print('\n[Y7] name-form sweep (14m-07 class) over the unit')
forms = {}
for n in range(UNIT[0], UNIT[1] + 1):
    for m in re.finditer(r'\b([A-Z][a-z]?)\s*(I{1,3}|IV|V|VI{0,3}|IX|XI{0,2}|XV)\b', strip_em(M[n - 1])):
        forms.setdefault(m.group(0), []).append(n)
for k in sorted(forms):
    print('   %-8s %d  %s' % (k, len(forms[k]), ','.join('L%d' % n for n in forms[k])))
print('   named-source and vocabulary tokens:')
for tok in ('Cooper', 'Cooper-type', 'NIST', 'ASD', 'Rydberg'):
    ins = [n for n in range(UNIT[0], UNIT[1] + 1) if has_token(strip_em(M[n - 1]), tok)]
    allv = sum(len([1 for l in LN[v] if has_token(strip_em(l), tok)]) for v in VOL)
    print('      %-12s unit %d %s | six volumes %d' % (tok, len(ins), ','.join('L%d' % n for n in ins) or '-', allv))

# ---------------------------------------------------------------- Y8  headings, captions, figure
print('\n[Y8] the unit\'s six headings, and whether the body completes the heading sentence')
for n in range(UNIT[0], UNIT[1] + 1):
    if re.match(r'^#{2,4} ', M[n - 1]):
        nxt = next((k for k in range(n + 1, UNIT[1] + 1) if M[k - 1].strip()), None)
        print('   L%-5d %s' % (n, strip_em(M[n - 1]).strip()))
        print('        first body line L%d: %s' % (nxt, strip_em(M[nxt - 1]).strip()[:120]))
print('   figure and caption:')
for n in range(UNIT[0], UNIT[1] + 1):
    if 'figure-25' in M[n - 1] or re.match(r'^\s*Figure 25', strip_em(M[n - 1])):
        print('   L%-5d %s' % (n, strip_em(M[n - 1]).strip()[:230]))
fa = [l for l in LN.get('main') if 'figure-25.1' in l]
print('   figure-25.1 referenced %d times in the main volume' % len(fa))
for v in ('ioi', 'math', 'phys', 'spectra', 'register'):
    k = [i for i, l in enumerate(LN[v], start=1) if 'Figure 25.1' in strip_em(l)]
    if k:
        print('   Figure 25.1 also named in %s at %s' % (v, ','.join('L%d' % n for n in k)))

# ---------------------------------------------------------------- Y9  Ruling 45 / 46 candidates
print('\n[Y9] Ruling 45 / 46 candidates in the unit (process or build language, reader-facing)')
pat = re.compile(r'\b(build|script|version|earlier draft|this chapter says|we (?:will|shall)|the author|rewrit|reported)\b', re.I)
for n in range(UNIT[0], UNIT[1] + 1):
    t = strip_em(M[n - 1]).strip()
    if pat.search(t):
        print('   L%-5d %s' % (n, t[:200]))

# ---------------------------------------------------------------- Y10  sentence terminals
print('\n[Y10] unit lines ending without terminal punctuation (prose lines only)')
for n in range(UNIT[0], UNIT[1] + 1):
    t = strip_em(M[n - 1]).rstrip()
    if not t or t.startswith(('#', '|', '!', ' ' * 4)) or t.lstrip().startswith(('|', '(')):
        continue
    nxt = M[n].strip() if n < len(M) else ''
    if nxt == '' and not re.search(r'[.!?:\u2014)]$', t):
        print('   L%-5d %s' % (n, t[-110:]))
print('=== end r2-ch14y ===')
