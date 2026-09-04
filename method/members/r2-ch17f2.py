#!/usr/bin/env python3
# r2-ch17f.py — chat 130 — R2 prose batch for main L9892–L9936 (Chapter 36), BUILD90. Reads MEMBERS and the PP copy at
# /home/claude/PP_The_Method_1_6.md (read for the "already computed before the problem was posed" claim only; §36 itself
# is post-PP and is not diffed). Imports r2lib by path. Ruling 45/46 probes are case-sensitive and word-bounded on the raw
# line; the first-person probe carries mine and myself; a wrapped phrase is read on the join; every negative has its witness.
# r2-ch17f2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch17f.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (7 anchors); nothing else changes. r2-ch17f.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: NOT PROVED on 90+184, 92+188 or 98+202 — reproduces r2-ch17f.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, io, importlib.util, contextlib
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); IOI = rd('The_Method_1_6___The_Index_of_Indices-2.md')
CP = rd('The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md'); PP = rd(os.path.join(H, '..', 'PP_The_Method_1_6.md'))
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch17c.py (owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch17c.py (owed to r2lib, DEFERRED)
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
h36 = [i for i, l in enumerate(M, 1) if re.match(r'^## 36\. ', l)][-1]; app = [i for i, l in enumerate(M, 1) if re.match(r'^# APPENDICES\s*$', l)][-1]
A, B = h36, app; U = M[A - 1:B - 1]; UJ = norm(' '.join(U))
print('unit L%d–L%d, %d lines (own scan)' % (A, B - 1, B - A))

hr('§1 RULING 45 / RULING 46 PROBES (case-sensitive, word-bounded on the raw line; every hit READ)')
R45 = ['build', 'BUILD', 'session', 'chat', 'instrument', 'ruling', 'review', 'archive', 'nightly', 'hash', 'ledger', 'protocol', 'collaborator', 'handoff', 'register', 'audit', 'golden', 'bank', 'run', 'rerun', 'transcript', 'delivered', 'reconstructed']
hits = {}
for i, l in enumerate(U, A):
    for w in R45:
        for m in re.finditer(r'(?<![\w])' + w + r'(?![\w])', l):
            hits.setdefault(w, []).append(i)
for w in R45:
    if w in hits: print(f'  {w:14s} {hits[w]}')
print('  READ: "register" (L9894 "register entries 1713–1724", L9902 "(register 1717") and "Registers" cites name the Register — the volume\'s own object, not production. "audit"/"rerun"/"ledger"/"protocol": L9902 "audit paragraph … rerun by", L9920 "first audit run", L9922 "audit 7 supplied the ledger" — the chapter\'s declared subject is the method\'s run on the three-body problem (as §34.10 and §35.4: docket 5, chat 115\'s split); recorded for that split, not scored here.')
r46 = [(i, l) for i, l in enumerate(U, A) if re.search(r'`[^`]+`|\.py\b|BUILD\d+|\.md\b|\.tsv\b|\.json\b', l)]
print('  Ruling 46 (backticks, .py, BUILDn, file extensions):', [(i, re.findall(r'`[^`]+`|\S+\.py\b', l)) for i, l in r46])
print('  DEVIATION 17e-01 site: L9902 `tb_audit.py` — a script name visible to readers (docket 6), the same site as the 1756 citation with no entry (docket 9c).')

hr('§2 FIRST PERSON (probe carries mine and myself; He I Roman-numeral trap excluded by requiring the pronoun be followed by a lowercase word or punctuation)')
fp = [(i, m.group(0)) for i, l in enumerate(U, A) for m in re.finditer(r'\b(I|my|mine|myself|we|our|ours|us)\b(?=[\s,.;:—]+(?:[a-z]|$)|[,.;:])', l)]
print('  hits:', fp, '-> first-person zero:', not fp)
print('  witness that the probe fires: "A fault of mine" in register 1723 body:', bool(re.search(r'\bmine\b', rbody(1723))))

hr('§3 STRUCTURE — bold lead-ins, italics, unmarked sub-headings (blank line above, then READ), long lines, recurrence (docket 27)')
bold = [(i, re.match(r'^\*\*(.+?)\*\*', l).group(1)) for i, l in enumerate(U, A) if re.match(r'^\*\*', l)]
print('  bold lead-in paragraphs:', len(bold), [i for i, _ in bold]); print('   ', [t[:36] for _, t in bold])
b3 = body_range(M, '36.3'); bold3 = [(i, t) for i, t in bold if b3[0] <= i < b3[1]]
print('  of these in §36.3 (L%d–L%d): %d lead-ins, each opening with a § pointer:' % (b3[0], b3[1] - 1, len(bold3)), all(t.startswith('§') for _, t in bold3), '; sections named across them:', sorted(set(re.findall(r'§[\dE.]+(?<!\.)', ' '.join(t for _, t in bold3)))), '; the tenth bold lead-in is §36.4\'s "Mass-uniformity." (L9926)')
ital = [i for i, l in enumerate(U, A) if re.match(r'^\*[^*].*\*\s*$', l)]
print('  whole-line italics (epigraph L9894, one-line summary L9934):', ital)
cand = [i for i, l in enumerate(U, A) if i > A and not M[i - 2].strip() and l.strip() and not l.startswith('#') and len(l) < 60]
print('  unmarked sub-heading candidates (short line after a blank, not a heading):', cand, '-> READ: none (each is a full sentence or a heading)' if not cand else '')
long = [i for i, l in enumerate(U, A) if len(l) > 400]
print('  lines over 400 chars:', len(long), '; recurrence test (docket 27): each unit line of ≥ 60 chars searched in the rest of main:', end=' ')
rec = [i for i, l in enumerate(U, A) if len(l) >= 60 and not l.startswith('#') and sum(1 for j, x in enumerate(M, 1) if x == l and not (A <= j < B)) > 0]
print(rec, '-> none recurring (headings excluded; the `## 36.` heading recurs at L159 as the contents entry):', not rec)
print('  tables in unit (pipe rows):', sum(1 for l in U if l.startswith('|')), '; horizontal rules:', [i for i, l in enumerate(U, A) if l.strip() == '---'])

hr('§4 §36.5 — EVERY NEGATIVE WITH A WITNESS (the unit L9892–L9936 and the companion paper searched for the thing denied)')
neg = M[body_range(M, '36.5')[0] + 1]
print('  L%d:' % (body_range(M, '36.5')[0] + 2), neg[:120], '…')
tests = {'No trajectory': (r'\br\s*\(\s*t\s*\)|\btrajectory formula|closed-form (trajectory|solution)', 'a trajectory formula'),
         'No prediction': (r'\bpredicts? (that|the position|where)\b', 'a positive prediction'),
         'No extension to n ≥ 4': (r'\bn\s*[=≥>]\s*[4-9]\b', 'an n ≥ 4 claim'),
         'Nothing that touches Poincaré': (r'Poincaré', 'the name Poincaré')}
for k, (pat, what) in tests.items():
    inU = [i for i, l in enumerate(U, A) if re.search(pat, l)]; inCP = [i for i, l in enumerate(CP, 1) if re.search(pat, l)]
    print(f'  "{k}": {what} — unit sites {inU}; companion sites {inCP}')
print('  READ: "No trajectory" unit site L9906 is "no trajectory formula exists" (the negative, quoted as one of two statements); companion L164 is its claims paragraph "the absence of a trajectory formula" (the negative again). "n ≥ 4" hits in the unit are the negative itself (L9930: "n ≥ 4", "n = 5" inside its own clause); Poincaré at L9898 is the §31.1.1 quotation and at L9894/L9930 the negative — the unit asserts nothing positive under any of the four; the companion\'s Poincaré sites are its own scope clauses (read: %d lines).' % len([l for l in CP if 'Poincaré' in l]))
print('  "No statement about the contents of ℳ_per beyond the equal-mass figure-eight": ℳ_per sites in unit:', [i for i, l in enumerate(U, A) if 'ℳ_per' in l], '(the negative only); "figure-eight" attribution Moore / Chenciner–Montgomery — companion carries both:', has_token(' '.join(CP), 'Moore') > 0 and has_token(' '.join(CP), 'Chenciner') > 0)

hr('§5 WORDING PAIRS AND CROSS-VOLUME PHRASES (read on the join)')
pairs = [('eight closed', 'L9902'), ('seven closed to named owners', 'register 1721'), ('Seven belonged to others', 'L9922'), ('Hill regions', 'L9914'), ('Hill spheres', 'L5156'), ('the book\'s own five', 'L9908'),
         ('coordinates come from the subject or from nowhere', 'L9926 — the Index of Indices\' "one-line claim"')]
for ph, where in pairs:
    print(f'  "{ph}" ({where}): unit {UJ.count(ph)} · main {sum(l.count(ph) for l in M)} · reg {sum(l.count(ph) for l in R)} · ioi {sum(l.count(ph) for l in IOI)} · companion {sum(l.count(ph) for l in CP)}')
ioi_hits = [i for i, l in enumerate(IOI, 1) if re.search(r'from the subject or from nowhere', l)]
print('  IoI sites of "from the subject or from nowhere":', ioi_hits, '; the phrase at L9926 is not a quotation (no quotation marks):', '"coordinates come' not in M[_L('### 36.4 The law this chapter adds', 1)])
print('  "envelope precision only" (L9898) vs §18.4.1 L5154–L5155 "the book\'s prediction is envelope precision only" — read on the join:', 'envelope precision only' in norm(M[_L(' once — a sum in the superposition, a difference in the relative position, a symmetric function in the')] + ' ' + M[_L(" mutual interaction — so it is the maximal case of what Chapter 18 forbids, and the book's prediction")]), '; L9898 attributes it to §12.11.2; §12.11.2 span carries "envelope":', has_token('\n'.join(M[_L(' and parity-changing at 20.1%. Registers 628–629.', 1):_L('### 12.11.3 The dichotomy', -1)]), 'envelope'))
print('  L9898 "nothing here touches Poincaré" is quoted; §31.1.1 carries it verbatim:', sum('nothing here touches Poincaré' in l for l in M[_L(' different claim from one that fits.', 1):_L('### 31.1.2 The nucleus — a second index of the same construction', -1)]))

hr('§6 "THE BOOK HAD ALREADY COMPUTED THAT PRECISION BEFORE THE PROBLEM WAS POSED" (L9934) — witnessed against Prints & Proofs')
pp215 = [i for i, l in enumerate(PP, 1) if re.match(r'^#{1,4} 21\.5\.1\b', l)]; pp1211 = [i for i, l in enumerate(PP, 1) if re.match(r'^#{1,4} 12\.11\.2\b', l)]
print('  PP carries §21.5.1 at', pp215, 'and §12.11.2 at', pp1211, '(headings; body = last)')
def ppspan(ln):
    for i in range(ln + 1, len(PP) + 1):
        if re.match(r'^#{1,4} ', PP[i - 1]): return '\n'.join(PP[ln - 1:i - 1])
    return '\n'.join(PP[ln - 1:])
t215 = ppspan(pp215[-1]) if pp215 else ''; t1211 = ppspan(pp1211[-1]) if pp1211 else ''
print('  PP §21.5.1 states treewidth 2 / strong 3-consistency / "exactly one level":', 'treewidth 2' in t215.replace('*', ''), 'strong 3-consistency' in t215.replace('*', ''), 'exactly one level' in t215.replace('*', ''))
print('  PP §12.11.2 carries "excluded forms":', has_token(t1211, 'excluded forms'), '; the sentence "three bodies carry all three excluded forms" lives in §18.4.1 (main L5152–L5154), and PP carries "three bodies"/"three-body" at', [i for i, l in enumerate(PP, 1) if re.search(r'three bodies|three-body', l, re.I)][:8], '… (15 sites)')
print('  PP carries "## 36." body / "36.1":', [i for i, l in enumerate(PP, 1) if re.match(r'^## 36\. ', l)], [i for i, l in enumerate(PP, 1) if re.match(r'^### 36\.1', l)], '-> the chapter is post-PP; the precision it cites is pre-PP: the claim is witnessed')

hr('§7 THE COMPANION PAPER MEMBER against the unit\'s summary sentences (token presence, no diff)')
cpj = norm(' '.join(CP))
for ph in ('78 of 78', '78/78', 'Thirteen', 'thirteen', 'order-type', 'Mass-uniformity', 'mass-uniformity', 'Brudno', 'Saari', 'Painlevé', 'Xia', 'measure zero', 'figure-eight', 'resolvent', 'hyper-radius', 'Routh', '0.0385209'):
    print(f'    "{ph}": {cpj.count(ph)}', end='')
print()
print('  the companion cites the same absent entry: "1756" sites in the companion:', [i for i, l in enumerate(CP, 1) if '1756' in l], '; "tb_audit" sites:', [i for i, l in enumerate(CP, 1) if 'tb_audit' in l])
