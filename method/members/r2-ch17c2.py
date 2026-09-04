#!/usr/bin/env python3
# r2-ch17c.py — chat 129 — R2 computable batch for main L9806–L9891 (§35.4–§35.6, closing Chapter 35), BUILD90.
# Reads MEMBERS from /home/claude/members; imports r2lib by path and the NIST ground-configuration table from
# r2-ch16y.py §3 by path (stdout captured, as r2-ch17a does). Everything computed from the table is a
# RECONSTRUCTION. Every convention is named before a verdict is printed. Decimal, never round(). A count word
# counts DATA rows; a literal string is not a test; every negative carries its witness.
# r2-ch17c2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch17c.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (23 anchors); nothing else changes. r2-ch17c.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: NOT PROVED on 90+184, 92+188 or 98+202 — reproduces r2-ch17c.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, io, sys, importlib.util, contextlib
from decimal import Decimal as D, ROUND_HALF_UP
from fractions import Fraction as F
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token, enclosing = L.heading_line, L.section_span, L.has_token, L.enclosing
Y = load('r2-ch16y', quiet=True)            # §3 table: CONF, SYM, ENT, LQ, nl, cap, opening; validated in r2-ch16y (banked)
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); PP = rd(os.path.join(H, '..', 'PP_The_Method_1_6.md'))
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch17a.py (there from r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch17b.py: first non-blank line after '### n' (entries are '### N', blank, body); None when absent
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, vols=VOL, flags=0):
    return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def fmt(s): return ' '.join(f'{v}:{len(n)}' + ('[' + ','.join(map(str, n[:6])) + ('…' if len(n) > 6 else '') + ']' if n else '') for v, n in s.items())
def lettered(M, tag):   # lettered heading (Appendix sections), body occurrence = LAST hit, exact token
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def span_after(M, ln):   # heading at ln to the next heading of any rank
    for i in range(ln + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (ln, i)
    return (ln, len(M) + 1)

# ---------------------------------------------------------------- 0. the unit, resolved twice, bounded by body_range
hr('0  UNIT main L9806–L9891 — heading lines by own scan, both resolvers')
for sec in ('35.4', '35.5', '35.6', '36'):
    print(f'  §{sec:5} heading_line {heading_line(M, sec):5}  body_range {body_range(M, sec)}  section_span {section_span(M, sec)}')
A, B = _L('### 35.4 How the method did it'), _L('reached from both ends, closed in the middle.*', 3)
assert heading_line(M, '35.4') == _L('### 35.4 How the method did it') and body_range(M, '35.6')[1] == _L('*A challenge posed outside this work, answered with the law of Part III and the reach of Part VI. The chapter runs the method on the one object §12.11 named as the maximal case of what Chapter 18 forbids, and reports that the method\'s negative is the problem\'s solution. The formal statement is a companion paper, "The Three-Body Problem for Unknown Masses"; register entries 1713–1724 carry the record.*', -2) and heading_line(M, '36') == _L('*A challenge posed outside this work, answered with the law of Part III and the reach of Part VI. The chapter runs the method on the one object §12.11 named as the maximal case of what Chapter 18 forbids, and reports that the method\'s negative is the problem\'s solution. The formal statement is a companion paper, "The Three-Body Problem for Unknown Masses"; register entries 1713–1724 carry the record.*', -2)
print(f'  unit bound by body_range: L{A}–L{B} = {B - A + 1} lines; body_range and section_span COINCIDE on §35.4, §35.5, §35.6: '
      f'{all(body_range(M, s) == section_span(M, s) for s in ("35.4", "35.5", "35.6"))}')
U = M[A - 1:B]; UT = '\n'.join(U)
print('  Prints & Proofs: "## 35." body occurrences in PP = %d; "### 35.4" in PP = %d; PP "# APPENDICES" at P%s — the unit is post-PP authoring, stated once, not diffed'
      % (sum(1 for l in PP if l.startswith('## 35.')), sum(1 for l in PP if l.startswith('### 35.4')), [i + 1 for i, l in enumerate(PP) if l.startswith('# APPENDICES')]))

# ---------------------------------------------------------------- 1. §2.14 (L9810, L9815) — the pointer resolved to the claim
hr('1  §2.14 — "State the number before the interpretation" (L9810–L9811): resolved to the CLAIM under both resolvers')
s, e = body_range(M, '2.14'); ss, se = section_span(M, '2.14')
print(f'  §2.14 heading L{heading_line(M, "2.14")}: {norm(M[heading_line(M, "2.14") - 1])[:80]!r}; body_range {(s, e)}; section_span {(ss, se)}')
for pat in (r'number before the interpretation', r'\bState the number\b', r'\binterpretation\b'):
    h = [i for i in range(s, e) if re.search(pat, M[i - 1], re.I)]
    print(f'  {pat:36} in §2.14 body: {len(h)} L{h[:4]}; six-volume sites: {fmt(sites(pat, flags=re.I))}')
print('  the italic phrase at L9810–L9811 (join): %r' % norm(re.search(r'\*State the number before the\s+interpretation\*', UT).group(0)))

# ---------------------------------------------------------------- 2. §E.5 (L9827) — "nine things were derived here that were already in print"
hr('2  §E.5 — "nine things" (L9827) counted at §E.5\'s BODY (DATA rows / list items), lettered heading resolved exact-token')
hE = lettered(M, 'E.5'); print(f'  "E.5" heading occurrences: {hE} (last = body)')
if hE:
    es, ee = span_after(M, hE[-1]); EB = M[es - 1:ee - 1]
    print(f'  §E.5 heading L{es}: {norm(M[es - 1])[:90]!r}; body L{es + 1}–L{ee - 1} ({ee - es - 1} lines)')
    items = [(i, norm(l)[:100]) for i, l in enumerate(EB, es) if re.match(r'^\s*(?:[-*•]|\d+[.)])\s', l)]
    trows = [(i, norm(l)[:100]) for i, l in enumerate(EB, es) if l.startswith('|') and not re.match(r'^\|\s*-', l)]
    bolds = [(i, norm(l)[:100]) for i, l in enumerate(EB, es) if l.startswith('**')]
    print(f'  list items {len(items)}; pipe-table rows {len(trows)}; bold lead-in paragraphs {len(bolds)} — the ledger is whitespace-aligned (fault 3: the pipe/list detector matched nothing)')
    starts = [i for i, l in enumerate(EB, es) if re.match(r'^  \S', l) and not M[i - 2].strip()]   # convention: a ledger row starts at a two-space-indented line after a blank line; the first such is the column header
    hdr, lrows = starts[0], starts[1:]
    print(f'  ledger header L{hdr} {norm(M[hdr - 1])!r}; DATA rows (left-column starts) {len(lrows)}:')
    for i in lrows: print(f'    L{i} {norm(M[i - 1])[:110]}')
    tot = [(i, norm(l)) for i, l in enumerate(EB, es) if re.search(r'\bNine components\b', l)]
    print(f'  the ledger\'s own totals line: {tot}; count word at L9827 "nine things": DATA rows {len(lrows)} — {"EQUAL" if len(lrows) == 9 else "NOT EQUAL"} (the convention yielding nine is unnamed; the closing note folds the step law and the subcube-removal construction into Rival)')
    s303, e303 = section_span(M, '30.3'); b303 = [(i, norm(M[i - 1])[:90]) for i in range(s303, e303) if M[i - 1].startswith('**') and not M[i - 2].strip()]
    print(f'  "Every component of §30.3" — §30.3 L{s303}–L{e303 - 1}: bold lead-in paragraphs {len(b303)}; sub-headings {sum(1 for i in range(s303, e303) if M[i - 1].startswith("#"))}; list items {sum(1 for i in range(s303, e303) if re.match(r"^\s*(?:[-*•]|\d+[.)])\s", M[i - 1]))}')
    for i, t in b303[:12]: print(f'    L{i} {t}')
    print(f'  L11165–L11168: the step-law row\'s right column is typeset as a broken fraction over four lines (production; incidental)')
    print('  §E.5 opening lines:'); [print('    L%d %s' % (i, norm(l)[:150])) for i, l in enumerate(EB[:6], es) if l.strip()]
    print('  count words in §E.5 body:', sorted(set(re.findall(r'\b(nine|eight|ten|seven|six|five|four|three|two|one)\b', '\n'.join(EB), re.I))))
    print('  "already in print" / "in print" in §E.5 body:', [i for i, l in enumerate(EB, es) if re.search(r'in print', l, re.I)])
print('  six-volume sites of "nine things":', fmt(sites(r'\bnine things\b', flags=re.I)), '; of "§E\\.5":', fmt(sites(r'§E\.5\b')))

# ---------------------------------------------------------------- 3. the twenty-two audits (L9824) against §3 (docket 33)
hr('3  "the twenty-two audits\' principle" (L9824) — counted at §3\'s DATA (sub-headings, rows, list items); docket 33')
h3 = heading_line(M, '3'); s3, e3 = section_span(M, '3'); print(f'  §3 heading L{h3}: {norm(M[h3 - 1])[:80]!r}; section_span L{s3}–L{e3 - 1}')
subs = [(i, norm(M[i - 1])[:70]) for i in range(s3, e3) if re.match(r'^#{3,4} 3\.\d', M[i - 1])]
print(f'  §3 sub-headings: {len(subs)}'); [print('    L%d %s' % x) for x in subs]
S3 = M[s3 - 1:e3 - 1]
print('  §3 "audit" token lines: %d; count words with "audits" in §3: %s' % (sum(1 for l in S3 if has_token(l, 'audit') or has_token(l, 'audits')),
      sorted(set(m.group(0) for l in S3 for m in re.finditer(r'\b(?:twenty-two|twenty-\w+|\w+teen|twelve|eleven|ten|nine|eight|seven|six|five|four|three)\b(?= audits)', l, re.I)))))
ten = [i for i in range(s3, e3) if re.match(r'^\s+\d+·\s+[A-Z]+', M[i - 1])]            # the ten-audit list rows L1010–L1019 (convention: "N·  NAME" rows)
twelve = re.findall(r'\b[A-Z]{4,}\b', norm(' '.join(M[_L('    another form.** They are about Λ and the objects around it.', 1):_L(" CENSUS. **Every one has caught something real**, and several caught faults in this chapter's own")])))                          # the twelve named in the L1024–L1026 sentence (all-caps tokens)
described = [i for i in range(s3, e3) if re.match(r'^\s?\d+ — [A-Z]+\.', M[i - 1])]           # audits described in the body ("N — NAME.")
print('  §3 DATA: ten-list rows %d (L%s); twelve named %d (%s); 10 + 12 = %s (Decimal); audits described in the body %d (docket 33 / 15i-08: seven of twenty-two) at L%s'
      % (len(ten), ten[:1] + ten[-1:], len(twelve), ' '.join(twelve), D('10') + D('12'), len(described), described))
print('  L79 (front matter) says "world outside the book"; L9824 says "world outside the work": %s / %s' % ('outside the book' in M[78], 'outside the work' in M[_L('re-verified before a session touched it. **The audit reads the object, the')]))
print('  six-volume sites of "twenty-two audits":', fmt(sites(r'twenty-two audits', flags=re.I)), '; of "twenty-two":', fmt(sites(r'\btwenty-two\b', flags=re.I)))
for i in sites(r'twenty-two audits', flags=re.I)['reg'][:3]: print('    reg L%d %s' % (i, norm(R[i - 1])[:150]))
print('  "The audit reads the object, the source, the artefact and the world outside the work" — a four-object list:', len(re.findall(r'\bthe (object|source|artefact|world)\b', norm('\n'.join(U[_L('re-verified before a session touched it. **The audit reads the object, the') - A:_L('principle, running nightly on a physics derivation.') - A])))))
print('  six-volume sites of "world outside the work":', fmt(sites(r'world outside the work', flags=re.I)))

# ---------------------------------------------------------------- 4. the years and the arithmetic of §35.4 / §35.6
hr('4  YEARS — Pulay 1969 · Löwdin 1950 · Griffin, Andrew and Cowan 1969 and 1971 · the 1969 challenge; References body lines')
refs = [i + 1 for i, l in enumerate(M) if l.startswith('## References')]; rb = refs[-1]; REF = M[rb - 1:]
r7 = [i + 1 for i, l in enumerate(M) if re.match(r'^#{2,4}\s*R\.7\b', l)]; R7 = M[r7[-1] - 1:] if r7 else []
print(f'  References body L{rb}; R.7 heading {r7}')
for name in ('Pulay', 'Löwdin', 'Griffin', 'Andrew', 'Cowan'):
    ln = [(i, norm(l)[:130]) for i, l in enumerate(REF, rb) if has_token(l, name)]
    print(f'  {name:8} References-body lines {len(ln)}: ' + ' | '.join(f'L{i} {t}' for i, t in ln[:4]))
yrs = {n: sorted(set(y for i, l in enumerate(REF) if has_token(l, n) for y in re.findall(r'\b(19\d\d|20\d\d)\b', l))) for n in ('Pulay', 'Löwdin', 'Griffin', 'Cowan')}
print('  years on those lines:', yrs)
print('  unit asserts: Pulay 1969 %s; Löwdin 1950 %s; Griffin/Andrew/Cowan 1969 %s and 1971 %s; Löwdin challenge 1969 %s'
      % ('1969' in yrs['Pulay'], '1950' in yrs['Löwdin'], '1969' in yrs['Griffin'] or '1969' in yrs['Cowan'], '1971' in yrs['Griffin'] or '1971' in yrs['Cowan'], '1969' in yrs['Löwdin']))
print('  "nineteen years before" (L9876): 1969 − 1950 =', D('1969') - D('1950'), '(Decimal; convention: challenge year minus identity year)')
print('  "Three of the load-bearing works are dated 1969" (L9874): named — the challenge (Löwdin 1969), the Pulay term (Pulay 1969), the collapse computation (Griffin/Andrew/Cowan 1969): '
      'items named %d; References lines dated 1969 among those names: %d' % (3, sum(1 for i, l in enumerate(REF) if re.search(r'\b1969\b', l) and any(has_token(l, n) for n in ('Pulay', 'Löwdin', 'Griffin', 'Cowan')))))
print('  all References-body lines dated 1969:', [(i, norm(l)[:80]) for i, l in enumerate(REF, rb) if re.search(r'\b1969\b', l)][:6])

# ---------------------------------------------------------------- 5. counts inside §35.4 — count words against the items they count
hr('5  COUNT WORDS in §35.4 — three discrepancies / all three; twice / two entries; four refusals / the fifth; five evaluations')
three = re.search(r'three numerical discrepancies\s+remained.*?All three were found', UT, re.S).group(0)
disc = [m for m in ('force-versus-gradient', 'operator asymmetry', 'two-branch f physics') if re.search(m.replace('-', r'[- ]'), UT)]
print('  "three numerical discrepancies … All three" — items enumerated at L9831–L9834: %d (%s)' % (len(disc), ', '.join(disc)))
nothings = [m for m in (r'g\s+channels\' refusal to move', r'the walk\'s one persistent internal defect') if re.search(m, UT)]
print('  "A nothing was defined … twice" / "Two entries … reclassified": items at L9839–L9846: %d' % len(nothings))
# five evaluations determine a quartic: degree-4 polynomial in one variable has 5 coefficients; Vandermonde at 5 distinct points is nonsingular (exact, Fractions)
xs = [F(k) for k in (-2, -1, 0, 1, 2)]; coeff = [F(3), F(-1), F(2), F(5), F(-7)]   # a0..a4, arbitrary
ys = [sum(c * x ** k for k, c in enumerate(coeff)) for x in xs]
def solve(A_, b_):
    n = len(A_); Mx = [row[:] + [bb] for row, bb in zip(A_, b_)]
    for c in range(n):
        p = next(r for r in range(c, n) if Mx[r][c] != 0); Mx[c], Mx[p] = Mx[p], Mx[c]
        Mx[c] = [v / Mx[c][c] for v in Mx[c]]
        for r in range(n):
            if r != c: Mx[r] = [a - Mx[r][c] * b for a, b in zip(Mx[r], Mx[c])]
    return [row[-1] for row in Mx]
rec_ = solve([[x ** k for k in range(5)] for x in xs], ys)
print('  "exactly quartic … five evaluations determine every coefficient" (L9844–L9846): degree 4 ⇒ %d coefficients; 5 exact evaluations recover them: %s (Vandermonde, Fractions, no truncation)' % (len(coeff), rec_ == coeff))
refs_ = sites(r'\brefus(?:ed|al|es)?\b', flags=re.I)
print('  "Four of this book\'s results exist because a conclusion was refused; … the fifth" (L9855–L9856): six-volume sites of refus*:', fmt(refs_))
for i in refs_['main'][:12]: print('    main L%d %s' % (i, norm(M[i - 1])[:120]))
print('  Register sites naming a count with refus*:', [(i, norm(R[i - 1])[:110]) for i in refs_['reg'] if re.search(r'\b(four|fourth|fifth|five)\b', R[i - 1], re.I)][:6])
four = norm(' '.join(M[49:55])); items4 = re.findall(r'\b(?:The|And the) ([^,]+?), because', four)
print('  the four at L50–L55 (front matter): %d items — %s' % (len(items4), ' | '.join(items4)))
print('  "reasoning sound, destination wrong" (L9851) in its printed order at L54: %s; six-volume sites of "destination wrong": %s; "collaborator" sites: %s'
      % (bool(re.search(r'reasoning was sound and the destination wrong', four)), fmt(sites(r'destination wrong', flags=re.I)), fmt(sites(r'\bcollaborator', flags=re.I))))
print('  contents L108: %r' % norm(M[107]))
print('  "this book paid for that sentence twice" (L9819): six-volume sites of "wrong artefact":', fmt(sites(r'wrong artefact', flags=re.I)))
print('    L75 %r' % norm(M[74])[:120]); print('    events named at L75–L78: %d (cross-references; the operator not printing); L81 carries the sentence verbatim: %s' % (len(re.findall(r'twenty-eight cross-references|107 blank boxes', norm(' '.join(M[74:78])))), norm(M[80]) == 'An audit that reads the wrong artefact will pass anything.'))

# ---------------------------------------------------------------- 6. the §35.5 table against register 1701–1712 (record-carried figures; equality at both sites)
hr('6  §35.5 TABLE L9860–L9868 — DATA rows counted; each delivered/rests-on pair against the Register entry that carries it')
rows = [l for l in U[_L('| delivered | rests on |') - A:_L('| **zero unexplained residue** | Pulay 1969 · Löwdin 1950 · exact quartics |', 1) - A] if l.startswith('|') and not re.match(r'^\|\s*-', l)]
print('  table lines %d: header 1 + DATA rows %d; columns per row: %s' % (len(rows), len(rows) - 1, sorted(set(len([c for c in r.strip('|').split('|')]) for r in rows))))
for r in rows[1:]: print('    ' + norm(r)[:120])
ent = {n: (rbody(n) or '') for n in range(1701, 1713)}
def reg_has(pat): return [n for n, b in ent.items() if re.search(pat, b)]
print('  "107/107" (row 1) — entries whose BODY carries "107 of 107|107/107": %s; six-volume sites of "107/107": %s; of "107 of 107": %s'
      % (reg_has(r'107 of 107|107/107'), fmt(sites(r'107/107')), fmt(sites(r'107 of 107'))))
print('  "one constant" (row 1) — entries whose body carries 137.035999: %s; c = 137.035999 sites: %s' % (reg_has(r'137\.035999'), fmt(sites(r'137\.035999'))))
m3 = re.search(r'(La, Ac(?:,| and) Th)', ent[1703]); print('  "the three exceptions" (row 2) — 1703 body names: %s → %d; "collapse" in 1703: %s'
      % (m3.group(1) if m3 else None, len(m3.group(1).replace(' and ', ', ').split(', ')) if m3 else 0, bool(re.search(r'collapse', ent[1703], re.I))))
print('  "no g block below 121" (row 3) — 1704 body: %r' % re.sub(r'\*', '', ent[_L(' 388, 390.', 1)])[:200])
print('    1704 carries "121": %s; "−1/(2n²)" / "1/(2n" in 1704: %s; six-volume sites of "below 121|below Z = 121": %s' % (bool(re.search(r'\b121\b', ent[_L(' 388, 390.', 1)])), bool(re.search(r'1/\(2n', ent[_L(' 388, 390.', 1)])), fmt(sites(r'below (?:Z = )?121'))))
print('  "the correlation clause … second order, complete, at the five close rows" (row 4) — 1705 body: %r' % re.sub(r'\*', '', ent[1705])[:220])
z5 = re.search(r'Z = ((?:\d+, )+\d+)', ent[1705]); z5 = z5.group(1).split(', ') if z5 else []   # the list form "Z = 38, 56, 72, 89, 105" (fault 2: a single-number regex read one of five)
print('    1705 "second order" %s; Z values listed: %s (count %d); "five" in 1705: %s' % (bool(re.search(r'second[- ]order', ent[1705], re.I)), z5, len(z5), bool(re.search(r'\bfive\b', ent[1705], re.I))))
print('  "the relativistic table … c → ∞ twin walk, eleven elements apart" (row 5) — 1706 body: %r' % re.sub(r'\*', '', ent[_L(' The calendar fails for one reason: days(m) is not monotone in m, because February has 28. Relabel the')])[:220])
m6 = re.search(r'Λ_chain at ([A-Z][a-z]?(?:, [A-Z][a-z]?)+)', ent[_L(' The calendar fails for one reason: days(m) is not monotone in m, because February has 28. Relabel the')]); print('    1706 elements: %d; "c → ∞|c→∞|nonrelativistic" in 1706: %s' % (len(m6.group(1).split(', ')) if m6 else 0, bool(re.search(r'c\s*→\s*∞|non-?relativistic', ent[_L(' The calendar fails for one reason: days(m) is not monotone in m, because February has 28. Relabel the')]))))
print('  "twelve unwitnessed rows … past the last measurement" (row 6) — 1712 body: %r' % re.sub(r'\*', '', ent[_L(' So the trade is explicit, and it has a number:')])[:200])
print('    convention A (1712: rows 109–120 past Z = 108): %d rows; convention B (1446: the observational edge is 102; rows past it to 120): %d rows — 17a-02\'s class, second site'
      % (120 - 109 + 1, 120 - 103 + 1))
print('    1446 headline: %r' % re.sub(r'\*', '', rbody(_L('  4.5   **a conclusion written before the output** — the order matters even when the answer is right')) or '')[:230])
print('  "zero unexplained residue" (row 7) — entries whose body carries "residue": %s; six-volume sites of "unexplained residue": %s' % (reg_has(r'residue'), fmt(sites(r'unexplained residue', flags=re.I))))
print('    "Pulay" in 1707–1712 bodies: %s; "quartic" in 1701–1712: %s; six-volume sites of "quartic": %s' % ([n for n in range(_L(' months in order of length — February, April, June, September, November, January, March, … — and E'), 1713) if has_token(ent[n], 'Pulay')], reg_has(r'quartic'), fmt(sites(r'\bquartic\b', flags=re.I))))
print('  "No parameter is fitted. No observation enters upstream of the score." (L9870) — the derivation\'s own claim (DEF-128 item 8): six-volume sites of "No parameter is fitted": %s; "upstream of the score": %s'
      % (fmt(sites(r'No parameter is fitted')), fmt(sites(r'upstream of the score'))))

# ---------------------------------------------------------------- 7. the coda pointers — Chapter 34, the corridor, the collapse condition
hr('7  CODA L9884–L9888 — "Chapter 34 read the order out of the table\'s own coordinates"; the corridor\'s silence at f; the collapse condition\'s address')
s34, e34 = section_span(M, '34')
for pat in (r'\bcoordinates?\b', r'\bcorridor\b', r'\bsilen(?:ce|t)\b', r'\bdomain\b', r'−∞|-∞', r'\bcollapse\b', r'carried state', r'computab'):
    h = [i for i in range(s34, e34) if re.search(pat, M[i - 1], re.I)]
    print(f'  {pat:20} in Chapter 34 (L{s34}–L{e34 - 1}): {len(h)} sites L{h[:6]}')
print('  "corridor" in the unit: L%s; in Chapter 35 (L9716–L9891): %d; Register entries 1701–1712 carrying "corridor": %s' % ([i for i, l in enumerate(U, A) if has_token(l, 'corridor')], sum(1 for l in M[_L('three-body problem but a statement about which pairs exist — Chapter 36 takes this up.*', 3):_L('reached from both ends, closed in the middle.*', 3)] if has_token(l, 'corridor')), reg_has(r'corridor')))
print('  six-volume sites of "reached from both ends":', fmt(sites(r'reached from both ends', flags=re.I)), '; "closed in the middle":', fmt(sites(r'closed in the middle', flags=re.I)))

# ---------------------------------------------------------------- 8. docket 27 — long-line recurrence
hr('8  DOCKET 27 — unit lines ≥ 60 chars recurring anywhere in the six volumes (whitespace-normalised)')
ALL = {v: [norm(l) for l in t] for v, t in VOL.items()}
rec = []
for i, l in enumerate(U, A):
    n = norm(l)
    if len(n) < 60: continue
    hits = sum(1 for v, t in ALL.items() for j, x in enumerate(t, 1) if x == n and not (v == 'main' and j == i))
    if hits: rec.append((i, hits))
print('  %d long lines tested; recurring: %s' % (sum(1 for l in U if len(norm(l)) >= 60), rec or 'none'))

# ---------------------------------------------------------------- 9. numerals and phrases of the unit, cross-site
hr('9  NUMERALS AND PHRASES — sites across the six volumes')
for pat in (r'\b107/107\b', r'\b1969\b', r'\b1950\b', r'\b1971\b', r'\btwenty-two\b', r'\bnine things\b', r'\bfive evaluations\b', r'\bexactly quartic\b', r'\bfourth\b|\bthe fifth\b',
            r'\bnineteen years\b', r'\bcryptographic\b', r'\bprediction file\b', r'\bhash\b', r'\bsealed copy\b', r'\bnightly\b', r'\bfault ledger\b', r'\bg block\b', r'\bunwitnessed\b'):
    print('  %-28s %s' % (pat, fmt(sites(pat, flags=re.I))))
print('\nEND r2-ch17c')
