#!/usr/bin/env python3
# r2-ch16a2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16a.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (22 anchors); nothing else changes. r2-ch16a.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16a.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16a — chat 116, PROSE batch for main L8347-L8450 (§30.2 - §30.3.2).

Pointers under both resolvers, attributions against the BODY occurrence of ## References and
against R.7, the Ruling 45 / 46 sweeps with the chat-115 split, register citations, the
census rows in range with contiguous-id witnessing, the duplicated-section sweep, and the
cross-volume test of L8412's "the withdrawal is withdrawn".

Functions owed to r2lib and carried here with provenance (DEFERRED): body_range (chat 108),
a last-occurrence resolver for '##'-level headings that also appear in the contents list
(chat 115), a left-bounded stem matcher (chat 113), a raw symbol test (chat 113).
"""
import importlib.util, os, re

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

VOL = {
    'main': 'The_Method_1_6-2.md',
    'reg':  'The_Method_1_6___The_Register-2.md',
    'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
    'sc':   'The_Method_1_6___Spectra_Compendium-2.md',
}
LINES = {t: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for t, f in VOL.items()}
M = LINES['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
LO, HI = _L('### 30.2 What governs the difficulty'), _L(' says why.', 1)
UNIT = M[LO - 1:HI]
UTEXT = '\n'.join(UNIT)


def body_range(Mx, sec):
    """[start, end) of a section's OWN body.  Owed to r2lib; provenance chat 108."""
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def last_md_heading(Mx, title):
    """LAST line whose heading text is exactly `title`.  '## References' occurs twice — the
    contents entry at L173 and the body at L11503 — and taking the first reports every
    attribution unbibliographed (chat 115's fault).  Owed to r2lib."""
    hits = [i for i, t in enumerate(Mx, 1) if re.match(r'^#{1,4}\s+' + re.escape(title) + r'\s*$', t.strip())]
    return hits[-1] if hits else None


def lettered_heading(Mx, label):
    """heading_line returns None for a lettered heading such as R.7 — use a line window."""
    hits = [i for i, t in enumerate(Mx, 1) if re.match(r'^#{1,4}\s+' + re.escape(label) + r'[ .]', t.strip())]
    return hits[-1] if hits else None


def stem(text, s):
    """Left-bounded only: has_token is letter-bounded on BOTH sides and scores a stem zero on
    every inflected form (chat 115).  Owed to r2lib."""
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(s), text, re.I))


def raw(text, s):
    """A symbol is tested raw, never word-bounded."""
    return text.count(s)


print('=' * 100)
print('r2-ch16a  PROSE  chat 116  main L%d-L%d  (§30.2 - §30.3.2)' % (LO, HI))
print('=' * 100)

# ------------------------------------------------------------------ 1. pointers
print('\n## 1  EVERY §-POINTER IN THE UNIT, resolved to the CLAIM under BOTH resolvers')
ptr = []
for i in range(LO, HI + 1):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', M[i - 1]):
        ptr.append((i, m.group(1)))
print('  pointer sites in unit: %d  %s' % (len(ptr), ptr))
CLAIM = {
    '30.3': ('a complexity question / a parameter the section consumes',
             ['complexity', 'arity', 'law', 'parameter', 'exponent']),
    '30.3.3': ('completes the landscape reading — potential, basin, descent',
               ['interval', 'landscape', 'basin', 'potential', 'descent', 'stall']),
}
for ln, sec in ptr:
    br, ss = body_range(M, sec), section_span(M, sec)
    if br is None:
        print('  L%d -> §%s  NO HEADING ANYWHERE' % (ln, sec))
        continue
    same = 'COINCIDE' if br == ss else 'DIFFER'
    want, toks = CLAIM.get(sec, ('(pointer to a section, no single claim asserted)', []))
    print('  L%d -> §%s  body_range %s  section_span %s  %s' % (ln, sec, br, ss, same))
    print('        source line: %s' % M[ln - 1].strip()[:96])
    print('        claim wanted: %s' % want)
    for tag, rng in (('body_range', br), ('section_span', ss)):
        seg = '\n'.join(M[rng[0] - 1:rng[1] - 1])
        hits = {t: stem(seg, t) for t in toks}
        print('        %-12s %s' % (tag, hits if toks else 'n/a'))

print('\n  L8414 "the recovered bound of Chapter 15" — resolved to chapter 15 and swept')
c15 = section_span(M, '15')
seg = '\n'.join(M[c15[0] - 1:c15[1] - 1]) if c15 else ''
print('  chapter 15 span %s  |  recovered %d  bound %d  irreducible %d  interval %d  Rival %d'
      % (c15, stem(seg, 'recover'), stem(seg, 'bound'), stem(seg, 'irreducib'),
         stem(seg, 'interval'), stem(seg, 'Rival')))

# ------------------------------------------------------------------ 2. attributions
print('\n## 2  EVERY ATTRIBUTION IN THE UNIT against ## References (BODY) and R.7')
refs_ln = last_md_heading(M, 'References')
r7_ln = lettered_heading(M, 'R.7')
print('  ## References occurrences: %s   BODY = L%s'
      % ([i for i, t in enumerate(M, 1) if t.strip() == '## References'], refs_ln))
print('  R.7 heading L%s' % r7_ln)
REFS = '\n'.join(M[refs_ln - 1:]) if refs_ln else ''
R7 = '\n'.join(M[r7_ln - 1:]) if r7_ln else ''
names = ['Van Isacker', 'Rival', 'Larson', 'Siggers', 'Stahl', 'Wille', 'Yannakakis']
for n in names:
    inunit = [i for i in range(LO, HI + 1) if n in M[i - 1]]
    print('  %-12s unit L%s | References %d | R.7 %d | six-volume sites %s'
          % (n, inunit, stem(REFS, n), stem(R7, n),
             {t: stem('\n'.join(L), n) for t, L in LINES.items() if stem('\n'.join(L), n)}))
print('  VERDICT: unbibliographed = zero hits in References AND zero in R.7')

# ------------------------------------------------------------------ 3. Ruling 45 / 46
print('\n## 3  RULING 45 — process and past-state remarks, split from plain self-reference')
FORMS = ['an earlier version', 'an earlier draft', 'a previous draft', 'from recollection',
         'now states', 'the guess that preceded it', 'the earlier figure of', 'the earlier reading',
         'a draft withdrew', 'is withdrawn', 'enumerated once', 'predates', 'was run once']
for f in FORMS:
    hits = [i for i in range(LO, HI + 1) if f.lower() in M[i - 1].lower()]
    allmain = [i for i, t in enumerate(M, 1) if f.lower() in t.lower()]
    print('  %-26s unit %-14s main total %d' % (f, hits, len(allmain)))
print('\n  PROCESS remarks (Ruling 45 sites) vs PLAIN SELF-REFERENCE (subject matter, not sites)')
for ln in (_L('### 30.2.1 And that list was enumerated once'), _L(' An earlier draft concluded from the 0.31 that the difficulty is not structural. That was a'), _L(' conclusion about ten invariants, and the list predates the containment forest, overlap components,'), _L('      Structure determines density; density determines difficulty. The earlier reading had the'), _L('      second link and called it the whole chain.'), _L(" §30.3's original citations — Stahl & Wille, Yannakakis — were correct; a draft withdrew them on the"), _L(' grounds that this was an interval problem, and it is not. The withdrawal is withdrawn.')):
    print('    L%d  %s' % (ln, M[ln - 1].strip()[:98]))

print('\n## 4  RULING 46 — script names, build numbers, internal files (case-sensitive, word-bounded)')
R46 = ['BUILD', 'gate.py', 'close.py', 'r2lib', 'tower-2.py', 'MANIFEST', 'md5', 'commit', 'repo']
for t in R46:
    hits = [i for i in range(LO, HI + 1)
            if re.search(r'(?<![A-Za-z])' + re.escape(t) + r'(?![A-Za-z])', M[i - 1])]
    print('  %-12s %s' % (t, hits if hits else 'zero sites in unit'))

# ------------------------------------------------------------------ 5. first person
print('\n## 5  FIRST-PERSON PRONOUNS in the unit')
fp = {p: [i for i in range(LO, HI + 1) if has_token(M[i - 1], p)]
      for p in ('I', 'we', 'our', 'us', 'my', 'ours')}
print('  %s' % {k: v for k, v in fp.items() if v})
print('  zero first-person pronouns: %s' % (not any(fp.values())))

# ------------------------------------------------------------------ 6. register citations
print('\n## 6  REGISTER CITATIONS in the unit (lowercase form grepped by hand)')
rc = [(i, m.group(0)) for i in range(LO, HI + 1)
      for m in re.finditer(r'[Rr]egisters?\s+(\d+)', M[i - 1])]
print('  sites: %s' % (rc if rc else 'none in unit'))

# ------------------------------------------------------------------ 7. the withdrawal
print('\n## 7  L8411-L8412 "a draft withdrew them ... The withdrawal is withdrawn" — cross-volume')
for probe in ('Stahl', 'Yannakakis', 'interval problem', 'withdraw'):
    for tag, L in LINES.items():
        hits = [(i, t.strip()[:92]) for i, t in enumerate(L, 1)
                if re.search(r'(?<![A-Za-z])' + re.escape(probe), t, re.I)]
        if hits:
            print('  %-16s %-5s %d site(s)' % (probe, tag, len(hits)))
            for i, t in hits[:6]:
                mark = '  <-- IN UNIT' if (tag == 'main' and LO <= i <= HI) else ''
                print('        L%-6d %s%s' % (i, t, mark))

# ------------------------------------------------------------------ 8. census rows
print('\n## 8  DEFECT-CENSUS.tsv rows in range, keyed on the column named `member`')
rowsf = open(os.path.join(H, 'DEFECT-CENSUS.tsv'), encoding='utf-8').read().split('\n')
hdr = rowsf[0].split('\t')
mi, li, ii = hdr.index('member'), hdr.index('line'), hdr.index('id')
recs = []
for r in rowsf[1:]:
    c = r.split('\t')
    if len(c) < len(hdr):
        continue
    try:
        recs.append((int(c[ii]), c[mi], int(c[li]), c[1], c[4]))
    except ValueError:
        continue
print('  member values present: %s' % sorted({r[1] for r in recs}))
inr = [r for r in recs if r[1] == 'main' and LO <= r[2] <= HI]
print('  rows in unit: %d' % len(inr))
main_rows = sorted([r for r in recs if r[1] == 'main'], key=lambda r: r[2])
before = [r for r in main_rows if r[2] < LO][-2:]
after = [r for r in main_rows if r[2] > HI][:2]
print('  WITNESS either side:')
for r in before + after:
    print('     id %-6d L%-6d %-28s %s' % (r[0], r[2], r[3], r[4]))
ids = [r[0] for r in before[-1:] + after[:1]]
print('  ids either side %s contiguous: %s' % (ids, ids[1] - ids[0] == 1))

# ------------------------------------------------------------------ 9. duplicated sections
print('\n## 9  DUPLICATED-SECTION SWEEP (DEF-105 item 1) — long unit lines recurring elsewhere')
long_lines = [(i, M[i - 1].strip()) for i in range(LO, HI + 1) if len(M[i - 1].strip()) >= 60]
dups = 0
for i, t in long_lines:
    for tag, L in LINES.items():
        for j, u in enumerate(L, 1):
            if u.strip() == t and not (tag == 'main' and j == i):
                print('     RECURS  main L%d == %s L%d  %s' % (i, tag, j, t[:70]))
                dups += 1
print('  %d long lines tested, %d recurrences' % (len(long_lines), dups))

# ------------------------------------------------------------------ 10. splices and formatting
print('\n## 10  SPLICE AND FORMATTING TESTS')
print('  L8400-L8402 sentence continuity:')
for i in (_L(' The question this section asked was: given an index whose constraint graph has cycles, can'), _L(" **Van Isacker**'s survey gives the seniority reduction chains."), _L(' its coordinate order be recovered? The answer has a law, a procedure, and a residue, and none of the')):
    print('     L%d  %s' % (i, M[i - 1].rstrip()))
join = M[_L('### 30.3 Reorderability — the law, the procedure, and what is left')].rstrip() + ' ' + M[_L(" **Van Isacker**'s survey gives the seniority reduction chains.")].strip()
print('     L8400 + L8402 joined reads: %s' % join.strip()[:140])
print('     L8401 is a complete sentence of unrelated subject inserted mid-sentence: %s'
      % (M[_L(' The question this section asked was: given an index whose constraint graph has cycles, can')].strip().endswith('.') and not M[_L('### 30.3 Reorderability — the law, the procedure, and what is left')].rstrip().endswith('.')))
print('  L8419-L8422 run-together sentences and inter-word spacing:')
for i in (_L(' is a constraint system on those decisions, and every constraint is closed under reversing all of'), _L(' is a constraint system on those decisions, and every constraint is closed under reversing all of', 1), _L(' its own orientations — 3,781 constraints checked, 100%.                           A   function     invariant     under'), _L(' complementation depends only on XOR-differences, so:')):
    print('     L%d  %r' % (i, M[i - 1].rstrip()[:110]))
print('     L8420 is blank inside a sentence: %s' % (M[_L(' is a constraint system on those decisions, and every constraint is closed under reversing all of')].strip() == ''))
print('     L8421 runs >=3 consecutive spaces mid-prose: %d occurrence(s)'
      % len(re.findall(r'\S {3,}\S', M[_L(' is a constraint system on those decisions, and every constraint is closed under reversing all of', 1)])))

# ------------------------------------------------------------------ 11. universals
print('\n## 11  UNIVERSALS AND SUPERLATIVES in the unit, each recorded measurable or not')
UNIV = ['every constraint', 'zero disagreements', 'entirely bijunctive', 'all 14',
        'exactly when', 'does not climb', 'no Schaefer class', 'every axis', 'each axis',
        'universally', 'always', 'never']
for u in UNIV:
    hits = [i for i in range(LO, HI + 1) if u.lower() in M[i - 1].lower()]
    if hits:
        for i in hits:
            print('  L%-6d %-22s %s' % (i, u, M[i - 1].strip()[:80]))

# ------------------------------------------------------------------ 12. PP diff of the unit
print('\n## 12  PRINTS & PROOFS: is the unit textually the same there?')
anchor = [i for i, t in enumerate(PP, 1) if t.strip().startswith('### 30.2 ')]
print('  PP §30.2 heading at %s' % anchor)
if anchor:
    a = anchor[-1]
    off = a - LO
    diffs = 0
    for i in range(LO, HI + 1):
        j = i + off
        if 1 <= j <= len(PP) and PP[j - 1].rstrip() != M[i - 1].rstrip():
            diffs += 1
            if diffs <= 8:
                print('     DIFF main L%d | PP P%d' % (i, j))
                print('        main: %s' % M[i - 1].rstrip()[:96])
                print('        PP  : %s' % PP[j - 1].rstrip()[:96])
    print('  %d differing lines over the %d-line unit at offset %d' % (diffs, HI - LO + 1, off))

# ------------------------------------------------------------------ 13. the §30.3.3 target, read
print('\n## 13  L8396 "§30.3.3 completes this reading" — the TARGET READ, not token-probed')
s33 = body_range(M, '30.3.3')
for i in range(s33[0], s33[1]):
    print('   L%d  %s' % (i, M[i - 1].rstrip()[:104]))

print('\n  WHERE THE LANDSCAPE READING DOES LIVE — six-volume sweep')
for probe in ('basin', 'landscape', 'potential', 'descent', 'transposition', 'stall'):
    hit = {}
    for tag, L in LINES.items():
        ls = [i for i, t in enumerate(L, 1) if stem(t, probe)]
        if ls:
            hit[tag] = ls[:8]
    print('  %-14s %s' % (probe, hit if hit else 'zero sites in six volumes'))

print('\n## 14  FIGURE REFERENCES vs FIGURE MEMBERS (production, not authoring)')
figs = [(i, M[i - 1].strip()) for i, t in enumerate(M, 1) if re.search(r'!\[Figure', t)]
print('  main-volume inline figure references: %d' % len(figs))
print('  first three: %s' % figs[:3])
figdir = os.path.join(H, 'figures')
print('  members/figures exists: %s   any .png member: %s'
      % (os.path.isdir(figdir),
         [f for f in os.listdir(H) if f.endswith('.png')][:5] or 'none'))
print('  PP inline figure references: %d'
      % len([1 for t in PP if re.search(r'!\[Figure', t)]))

print('\nEND r2-ch16a')
