#!/usr/bin/env python3
# r2-ch17d.py — chat 129 — R2 prose batch for main L9806–L9891 (§35.4–§35.6, closing Chapter 35), BUILD90.
# Pointers resolved to the CLAIM under both resolvers; attributions against the References body and R.7; count words
# against their DATA; Rulings 45/46 with the section's declared subject named; first person with mine/myself; headings
# and lead-ins read; the companion paper; single witnesses. Word-bounded, case-insensitive unless stated; a literal
# phrase is not a test; every negative carries its witness; passes recorded as well as failures.
import os, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
heading_line, section_span, has_token, enclosing = L.heading_line, L.section_span, L.has_token, L.enclosing
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); PAPER = rd('THE-LOWDIN-SOLUTION-2.md')
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
A, B = 9806, 9891; U = M[A - 1:B]; UT = '\n'.join(U); norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, flags=re.I): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in VOL.items()}
def fmt(s): return ' '.join(f'{v}:{len(n)}' + ('[' + ','.join(map(str, n[:6])) + ('…' if len(n) > 6 else '') + ']' if n else '') for v, n in s.items())
def body_range(M, sec):   # copied verbatim from r2-ch17a.py (there from r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch17b.py: first non-blank line after '### n'; None when absent
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def span_hits(sec, pats, lim=4):
    s, e = section_span(M, sec); out = []
    for pat in pats:
        h = [(i, norm(M[i - 1])[:110]) for i in range(s, e) if re.search(pat, M[i - 1], re.I)]
        out.append((pat, len(h), h[:lim]))
    return (s, e), out

hr('0  UNIT main L9806–L9891 (body_range-bounded; see r2-ch17c §0); a pointer is resolved to the CLAIM, not the heading')
print('  §35.4 L%d; §35.5 L%d; §35.6 L%d; §36 body L%d; unit %d lines' % (heading_line(M, '35.4'), heading_line(M, '35.5'), heading_line(M, '35.6'), heading_line(M, '36'), B - A + 1))
print('  post-PP: stated once in r2-ch17c §0; not diffed here')

# ---------------------------------------------------------------- 1. pointers in the unit
hr('1  POINTERS — every "Chapter N" / "§N" / "§X.N" token in the unit, its line, and where the claim lives')
toks = [(i, m.group(0)) for i, l in enumerate(U, A) for m in re.finditer(r'§[A-Z]\.\d+(?:\.\d+)*|§\d+(?:\.\d+)*|Chapter \d+', l)]
print('  tokens:', ' '.join(f'L{i}:{t}' for i, t in toks))
for sec, claim, pats in (('2.14', 'L9810–L9811 "§2.14 … State the number before the interpretation"; L9815 "That is §2.14 with teeth"', [r'computed before', r'number before', r'\bprotocol\b']),
                         ('34', 'L9884 "Chapter 34 read the order out of the table\'s own coordinates"', [r'\bcoordinates?\b', r'\border\b.*\btable\b|\btable\b.*\border\b'])):
    (s, e), out = span_hits(sec, pats)
    print(f'  §{sec} (L{s}–L{e - 1}) for {claim}:')
    for pat, n, h in out: print(f'     {pat:44} {n} hits ' + ' | '.join(f'L{i} {t[:80]}' for i, t in h[:2]))
print('  §2.14 body_range L%s (5 lines): the maxim is the book\'s paraphrase of §2.14, repeated at L29 and L7668 (r2-ch17c §1); the pointer resolves to the claim' % (body_range(M, '2.14'),))
e5 = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*E\.5\b', l)]
print('  §E.5 (L9827): heading %s %r; its DATA and totals line are r2-ch17c §2\'s (eleven rows under "Nine components")' % (e5, norm(M[e5[-1] - 1]) if e5 else None))

# ---------------------------------------------------------------- 2. attributions (in unit now; r2-ch17b measured them out of unit)
hr('2  ATTRIBUTIONS — names in the unit against the References body and R.7 (word-bounded)')
refs = [i + 1 for i, l in enumerate(M) if l.startswith('## References')]; rb = refs[-1]
r7 = [i + 1 for i, l in enumerate(M) if re.match(r'^#{2,4}\s*R\.7\b', l)]
print('  References body heading L%d (occurrences %s); R.7 heading %s' % (rb, refs, r7))
REF = '\n'.join(M[rb - 1:]); R7 = '\n'.join(M[r7[-1] - 1:]) if r7 else ''
for name in ('Pulay', 'Löwdin', 'Griffin', 'Andrew', 'Cowan'):
    print('  %-8s unit sites %s; References body %d; R.7 %d' % (name, [i for i, l in enumerate(U, A) if has_token(l, name)], has_token(REF, name), has_token(R7, name)))
print('  R.7 section (L%d–): first lines: %s' % (r7[-1], ' | '.join(norm(l)[:70] for l in M[r7[-1] - 1:r7[-1] + 3] if l.strip())))
print('  unnamed sources in the unit: "the man who posed the question" (L9876) = Löwdin (L9722 "The challenge posed in 1969"; References L11809 Löwdin 1969): %s' % bool(re.search(r'Löwdin[^\n]{0,60}\(1969\)', REF)))

# ---------------------------------------------------------------- 3. Rulings 45 / 46 and first person
hr('3  RULING 45 (process remarks) with the section\'s declared subject; RULING 46; FIRST PERSON (mine, myself carried)')
print('  §35.4\'s heading: %r; its opener L9808: %r — the declared subject is how the method ran on the Löwdin problem' % (norm(M[9805]), norm(M[9807])))
for tok in ('build', 'chat', 'session', 'handoff', 'draft', 'edit', 'rewrite', 'instrument', 'instruments', 'golden', 'ruling', 'review', 'archive', 'nightly', 'hash', 'file', 'ledger', 'protocol', 'collaborator'):
    h = [i for i, l in enumerate(U, A) if has_token(l, tok)]
    if h: print('  R45 candidate %-12s L%s: %s' % (tok, h, ' | '.join(norm(M[i - 1])[:88] for i in h)))
print('  "this book" self-reference sites in the unit: L%s' % [i for i, l in enumerate(U, A) if re.search(r"\bthis book('s)?\b", l)])
print('  R46: backticked tokens %d; ".py" %d; "BUILD" %d; script/file names %d' % (len(re.findall(r'`[^`]+`', UT)), len(re.findall(r'\.py\b', UT)), len(re.findall(r'\bBUILD\s?\d', UT)), len(re.findall(r'\b\w+\.(?:py|md|tsv|json)\b', UT))))
fp = [(i, m.group(0)) for i, l in enumerate(U, A) for m in re.finditer(r'\b(I|my|we|our|us|mine|myself)\b', l)]
print('  first person (case-sensitive I): %s' % (fp or 'zero'))
for i, w in fp: print('     L%d %r in: %s' % (i, w, norm(M[i - 1])[:100]))
print('  the four refusals at L50–L55 carry "I concluded / I wrote / I called" — front matter, out of unit (a note from the collaborator, contents L108); recorded, not scored here')

# ---------------------------------------------------------------- 4. count words against their DATA
hr('4  COUNT WORDS — each against the rows it counts (r2-ch17c carries the arithmetic)')
cw = {'nine things (L9827) → §E.5 ledger rows': '11 (totals line says nine) — DEVIATION, r2-ch17c §2',
      'twenty-two audits (L9824) → §3 ten-list + twelve names': '10 + 12 = 22 — EQUAL; seven described (docket 33)',
      'three discrepancies / all three (L9829, L9831)': '3 items — EQUAL',
      'twice / Two entries (L9838, L9846)': '2 items — EQUAL',
      'five evaluations (L9845)': '5 coefficients of a quartic — EQUAL',
      'Four … refused; the fifth (L9855–L9856)': '4 enumerated at L50–L55 — EQUAL',
      'Three of the load-bearing works are dated 1969 (L9874)': '3 References lines dated 1969 — EQUAL',
      'nineteen years (L9876)': '1969 − 1950 = 19 — EQUAL',
      'the three exceptions (L9863)': '1703: La, Ac, Th — EQUAL',
      'the five close rows (L9865)': '1705: Z = 38, 56, 72, 89, 105 — EQUAL (1705 says "contested"; the unit says "close")',
      'eleven elements apart (L9866)': '1706: 11 — EQUAL',
      'twelve unwitnessed rows (L9867)': '1712: 12 (109–120); under 1446\'s edge at 102: 18 — 17a-02\'s class, second site',
      'twelve (L9867) vs "the last measurement"': 'convention unnamed at the site'}
for k, v in cw.items(): print('  %-58s %s' % (k, v))

# ---------------------------------------------------------------- 5. structure
hr('5  STRUCTURE — bold lead-ins read (not headings); the italic opener; the table; the rules; the italic coda; unmarked sub-heading test')
leads = [(i, norm(re.match(r'\*\*(.+?)\*\*', l + ' ' + M[i]).group(1))[:80]) for i, l in enumerate(U, A) if l.startswith('**') and (i == A or not M[i - 2].strip())]   # join the next line: a lead-in may wrap
print('  bold lead-in paragraphs: %d -> %s' % (len(leads), ' | '.join(f'L{i} {t}' for i, t in leads)))
print('  L9808 italic one-liner: %r (an opener, not a heading)' % norm(M[9807]))
print('  L9870 bold one-liner: %r (a claim, not a heading; DEF-128 item 8: the derivation\'s own, not a 16z-01 site — 16z-01 sites L9596, L9659 recorded, not scored twice)' % norm(M[9869]))
print('  horizontal rules "---" in unit: L%s; italic coda L9884–L9888: starts "*" %s, ends ".*" %s' % ([i for i, l in enumerate(U, A) if l.strip() == '---'], M[9883].startswith('*'), M[9887].rstrip().endswith('.*')))
tbl = [i for i, l in enumerate(U, A) if l.startswith('|')]
print('  table L%d–L%d: %d lines (header, rule, %d DATA rows); header cells: %s' % (tbl[0], tbl[-1], len(tbl), len(tbl) - 2, [c.strip() for c in M[tbl[0] - 1].strip('|').split('|')]))
unmarked = [i for i, l in enumerate(U, A) if l.strip() and not l.startswith('#') and len(l) < 60 and not M[i - 2].strip() and (i < B and not M[i].strip()) and not l.startswith(('*', '>', '|', '-'))]
print('  unmarked sub-heading candidates (short line, blank above and below): %s' % (unmarked or 'zero'))
print('  headings in unit: %s' % [(i, l) for i, l in enumerate(U, A) if l.startswith('#')])
print('  quotation marks in unit: %s' % [(i, norm(M[i - 1])[:70]) for i, l in enumerate(U, A) if '"' in l or '“' in l])

# ---------------------------------------------------------------- 6. the companion paper
hr('6  THE COMPANION PAPER — member THE-LOWDIN-SOLUTION-2.md against §35.4–§35.6')
print('  first heading: %r; lines %d' % (next(l for l in PAPER if l.startswith('#')), len(PAPER)))
for pat in (r'\bPulay\b', r'\bquartic\b', r'five evaluations', r'\bhash\b', r'sealed', r'\bnightly\b', r'\bLöwdin\b.{0,40}1950|1950', r'\bGriffin\b', r'\bfitted\b', r'upstream', r'\bg block\b', r'109–120|109-120'):
    print('  %-32s paper lines %s' % (pat, [i + 1 for i, l in enumerate(PAPER) if re.search(pat, l, re.I)][:8]))

# ---------------------------------------------------------------- 7. single witnesses and the record's phrasing
hr('7  SINGLE-WITNESS CHECK (docket 17) — the unit\'s phrases with one site in six volumes; the Register\'s phrasing')
for pat in (r'cryptographic instrument', r'prediction file', r'mandatory failure modes', r'sealed copy', r'twenty-two audits', r'nine things', r'search before', r'force-versus-gradient', r'operator asymmetry',
            r'two-branch', r'non-orthogonality', r'defending something else', r'no g block', r'exactly quartic', r'five evaluations', r'fault ledger', r'converted into structure', r'destination wrong',
            r'the pinned channels', r'twin walk', r'unexplained residue', r'No parameter is fitted', r'upstream of the score', r'nineteen years', r'reached from both ends'):
    print('  %-30s %s' % (pat, fmt(sites(pat))))
print('  Register bodies 1707–1711 (the audit and the residues), first 120 chars each:')
for n in range(1707, 1712): print('    %d  %s' % (n, re.sub(r'\*', '', rbody(n) or 'ABSENT')[:120]))
print('\nEND r2-ch17d')
