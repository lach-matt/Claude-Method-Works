#!/usr/bin/env python3
# r2-ch17b.py — chat 128 — R2 prose batch for main L9716–L9805 (Chapter 35 head + epigraph, §35.1–§35.3), BUILD90.
# Pointers resolved to the CLAIM under both resolvers; Register existence first; attributions against the References
# body and R.7; count words against their DATA; Rulings 45/46; first person with mine/myself; headings read; the
# companion paper; single witnesses. Word-bounded, case-insensitive unless stated; a literal phrase is not a test.
import os, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
heading_line, section_span, has_token, enclosing = L.heading_line, L.section_span, L.has_token, L.enclosing
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); PAPER = rd('THE-LOWDIN-SOLUTION-2.md')
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
A, B = 9716, 9805; U = M[A - 1:B]; UT = '\n'.join(U); norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, flags=re.I): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in VOL.items()}
def fmt(s): return ' '.join(f'{v}:{len(n)}' + ('[' + ','.join(map(str, n[:6])) + ('…' if len(n) > 6 else '') + ']' if n else '') for v, n in s.items())
def rbody(n):
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def span_hits(sec, pats, lim=4):
    s, e = section_span(M, sec); out = []
    for pat in pats:
        h = [(i, norm(M[i - 1])[:110]) for i in range(s, e) if re.search(pat, M[i - 1], re.I)]
        out.append((pat, len(h), h[:lim]))
    return (s, e), out

hr('0  UNIT main L9716–L9805 (body_range-bounded; see r2-ch17a §0); a pointer is resolved to the CLAIM, not the heading')
print('  §35 body L%d; §35.1 L%d; §35.2 L%d; §35.3 L%d; §35.4 L%d' % tuple(heading_line(M, s) for s in ('35', '35.1', '35.2', '35.3', '35.4')))

# ---------------------------------------------------------------- 1. pointers in the unit
hr('1  POINTERS — every "Chapter N" / "§N" token in the unit, its line, and where the claim lives')
toks = [(i, m.group(0)) for i, l in enumerate(U, A) for m in re.finditer(r'§\d+(?:\.\d+)*|Chapter \d+', l)]
print('  tokens:', ' '.join(f'L{i}:{t}' for i, t in toks))
for sec, claim, pats in (('6', 'L9729 "Chapter 6 proved the periodic table is not a closed index"', [r'not a closed index', r'closed index', r'periodic table']),
                         ('33', 'L9729–L9731 "Chapter 33 said what that costs: what a closure cannot supply is exactly what requires an operator"', [r'cannot supply', r'requires an operator', r'\boperator\b']),
                         ('33', 'L9802–L9803 "Where a language falls silent, the silence names the object. Chapter 33 said it of the six languages"', [r'six languages', r'falls? silent', r'\bsilence\b']),
                         ('34.9', 'L9786 "Chapter 34 ended on a silence and called it a domain statement"; L9803 "enacted it at the f corridor"', [r'\bdomain\b', r'outside the domain', r'−∞|-∞']),
                         ('34', 'L9747 "the 106 transitions Chapter 34 counted"', [r'\b106\b', r'transitions?'])):
    (s, e), out = span_hits(sec, pats)
    print(f'  {claim}\n    Chapter/§{sec} span L{s}–L{e - 1}:')
    for pat, n, h in out: print(f'      {pat!r:24} {n:3} hits  ' + ' | '.join(f'L{i} {t}' for i, t in h))

# ---------------------------------------------------------------- 2. Register existence — entries 1701–1712, existence first
hr('2  REGISTER — "register entries 1701–1712 carry the record" (L9723): existence first, then subject')
present = [n for n in range(1701, 1713) if rbody(n) is not None]; absent = [n for n in range(1701, 1713) if rbody(n) is None]
print('  present: %s (%d of 12); ABSENT: %s' % (present, len(present), absent))
for n in present: print('    %d  %s' % (n, re.sub(r'\*', '', rbody(n))[:96]))
print('  sites of a bare "1710" in the six volumes:', fmt(sites(r'\b1710\b', 0)), '; sites of "1701–1712":', fmt(sites(r'1701–1712', 0)))
h = [n for n in range(1701, 1713) if rbody(n) and re.search(r'Löwdin|chain|walk|entrant|field|correlation|relativistic|residue|unwitnessed', rbody(n), re.I)]
print('  entries whose headline is on the Löwdin subject: %d of %d present' % (len(h), len(present)))
print('  1703 body (the collapse condition; L9797 "two coexisting solutions"):', re.sub(r'\*', '', rbody(1703))[:420])

# ---------------------------------------------------------------- 3. attributions
hr('3  ATTRIBUTIONS — names in the unit against the References body and R.7 (word-bounded)')
refs = [i + 1 for i, l in enumerate(M) if l.startswith('## References')]; rb = refs[-1]
r7 = [i + 1 for i, l in enumerate(M) if re.match(r'^#{2,4}\s*R\.7\b', l)]
print('  References body heading L%d (occurrences %s); R.7 heading %s' % (rb, refs, r7))
REF = '\n'.join(M[rb - 1:]); R7 = '\n'.join(M[r7[-1] - 1:]) if r7 else ''
for name in ('Löwdin', 'Schrödinger'):
    print('  %-12s unit sites %s; References body %d; R.7 %d' % (name, [i for i, l in enumerate(U, A) if has_token(l, name)], has_token(REF, name), has_token(R7, name)))
for name in ('Pulay', 'Griffin', 'Andrew', 'Cowan'):
    print('  %-12s OUT OF UNIT (§35.5, chat 129): unit sites %s; References body %d; R.7 %d' % (name, [i for i, l in enumerate(U, A) if has_token(l, name)], has_token(REF, name), has_token(R7, name)))
print('  "The challenge posed in 1969" (L9722): Löwdin 1969 in References body: %s' % bool(re.search(r'Löwdin[^\n]{0,80}1969|1969[^\n]{0,80}Löwdin', REF)))

# ---------------------------------------------------------------- 4. Rulings 45 / 46 and first person
hr('4  RULING 45 (process remarks), RULING 46 (script names, build numbers, backticks), FIRST PERSON (mine, myself carried)')
for tok in ('build', 'chat', 'session', 'handoff', 'draft', 'edit', 'rewrite', 'instrument', 'golden'):
    h = [i for i, l in enumerate(U, A) if has_token(l, tok)]
    if h: print('  R45 candidate %-10s L%s: %s' % (tok, h, ' | '.join(norm(M[i - 1])[:90] for i in h)))
print('  R46: backticked tokens %d; ".py" %d; "BUILD" %d' % (len(re.findall(r'`[^`]+`', UT)), len(re.findall(r'\.py\b', UT)), len(re.findall(r'\bBUILD\s?\d', UT))))
fp = [(i, m.group(0)) for i, l in enumerate(U, A) for m in re.finditer(r'\b(I|my|we|our|us|mine|myself)\b', l)]
print('  first person (case-sensitive I): %s' % (fp or 'zero'))
for i, w in fp: print('     L%d %r in: %s' % (i, w, norm(M[i - 1])[:100]))

# ---------------------------------------------------------------- 5. count words against their DATA
hr('5  COUNT WORDS — each against the rows it counts')
cw = {'eleven elements (L9773)': len(re.search(r'eleven elements — ([^.]+)\.', UT).group(1).split(', ')),
      'twelve rows (L9777)': 120 - 109 + 1, 'five elements (L9766)': len(re.search(r'Z = ([\d, ]+)\)', UT).group(1).split(', ')),
      'three exception rows (L9750, L9757, L9794)': len(re.search(r'except at exactly ([A-Z][a-z]?, [A-Z][a-z]? and [A-Z][a-z]?)', UT).group(1).replace(' and ', ', ').split(', '))}
for k, v in cw.items(): print('  %-44s DATA rows %d' % (k, v))
s33, e33 = section_span(M, '33.1'); six = [(i, norm(M[i - 1])[:140]) for i in range(s33, e33) if re.search(r'six languages|languages', M[i - 1], re.I)]
print('  "the six languages" (L9803) -> §33.1 L%d–L%d lines naming the languages: %s' % (s33, e33 - 1, ' | '.join(f'L{i} {t}' for i, t in six[:3])))
print('  "Chapter 33 said it of the six languages" — the roster printed at §33.1 is chat 125\'s 16t finding (six there, six at §20.2, two in common); not re-derived here')

# ---------------------------------------------------------------- 6. headings, lead-ins, epigraph, blockquote
hr('6  STRUCTURE — bold lead-ins read (not headings), the epigraph, the blockquote; unmarked sub-heading test with a blank line above')
leads = [(i, norm(re.match(r'\*\*(.+?)\*\*', l + ' ' + M[i]).group(1))[:80]) for i, l in enumerate(U, A) if l.startswith('**') and (i == A or not M[i - 2].strip())]   # join the next line: a lead-in may wrap
print('  bold lead-in paragraphs: %d -> %s' % (len(leads), ' | '.join(f'L{i} {t}' for i, t in leads)))
print('  italic epigraph L9718–L9725: starts "*" %s, ends ".*" %s; blockquote L9746–L9750: %d "> " lines' % (M[9717].startswith('*'), M[9724].rstrip().endswith('.*'), sum(1 for l in U if l.startswith('> '))))
unmarked = [i for i, l in enumerate(U, A) if l.strip() and not l.startswith('#') and len(l) < 60 and not M[i - 2].strip() and (i < B and not M[i].strip()) and not l.startswith(('*', '>', '|', '-'))]
print('  unmarked sub-heading candidates (short line, blank above and below): %s' % (unmarked or 'zero'))
print('  headings in unit: %s' % [(i, l) for i, l in enumerate(U, A) if l.startswith('#')])

# ---------------------------------------------------------------- 7. the companion paper
hr('7  THE COMPANION PAPER — member THE-LOWDIN-SOLUTION-2.md against the chapter')
print('  first heading: %r; lines %d' % (next(l for l in PAPER if l.startswith('#')), len(PAPER)))
PT = '\n'.join(PAPER)
for pat in (r'107 of 107', r'La, Ac(,| and) Th', r'\beleven\b', r'0\.083', r'137\.035999', r'Koelling', r'\b1701\b|\b1712\b', r'\bmeasured ground configuration'):
    print('  %-32s paper lines %s' % (pat, [i + 1 for i, l in enumerate(PAPER) if re.search(pat, l)][:8]))

# ---------------------------------------------------------------- 8. single witnesses and the record's phrasing
hr('8  SINGLE-WITNESS CHECK (docket 17) — the unit\'s figures with one site in six volumes, and the Register\'s phrasing')
for pat in (r'two coexisting solutions', r'coexist', r'two (?:solutions|branches|stationary points)', r'106 transitions', r'106 steps', r'three elements wide', r'collapse condition', r'double-well'):
    print('  %-30s %s' % (pat, fmt(sites(pat))))
print('  "unwitnessed" as the book\'s own vocabulary: first Index-of-Indices site:', [norm(VOL['ioi'][i - 1])[:120] for i in sites(r'\bunwitnessed\b')['ioi'][:1]])
print('\nEND r2-ch17b')
