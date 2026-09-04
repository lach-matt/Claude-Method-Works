#!/usr/bin/env python3
# r2-ch16c2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16c.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (24 anchors); nothing else changes. r2-ch16c.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16c.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16c — chat 117, PROSE batch for main L8451-L8574 (§30.3.3 - §30.3.9).

Every pointer resolved under BOTH resolvers and to the CLAIM; every attribution against the
BODY occurrence of ## References and against R.7; the register citation grouped-aware and
existence first; the Ruling 45 and Ruling 46 sweeps; the duplicated-section sweep; the
census rows in range read rather than counted; the splice at L8563-L8567 and the twice-printed
table header at L8480/L8483 witnessed against Prints & Proofs; and the chat-116 pointer defect
16b-04 carried to its real completion.

Functions owed to r2lib and carried here with provenance (DEFERRED): body_range (chat 108),
a last-occurrence resolver for '##'-level headings that also appear in the contents list
(chat 115), a lettered-heading resolver (chat 115), a left-bounded stem matcher (chat 113),
a raw symbol test (chat 113), and the digit-bounded numeral sweep with BOTH boundaries
corrected --- the trailing-period half by chat 116, the trailing-comma half by chat 117.
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
LO, HI = _L('### 30.3.3 What the interval machinery was'), _L(' Adams–Dwinger–Schmid 1996, both unread.', 1)
UTEXT = '\n'.join(M[LO - 1:HI])

NUMB = r'(?<![\d.,])%s(?!\d)(?!,\d)(?!\.\d)'


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
    """LAST line whose heading text is exactly `title`.  '## References' occurs twice --- the
    contents entry at L173 and the body at L11503 --- and taking the first reports every
    attribution unbibliographed (chat 115's fault).  Owed to r2lib."""
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(title) + r'\s*$', t.strip())]
    return hits[-1] if hits else None


def lettered_heading(Mx, label):
    """heading_line returns None for a lettered heading such as R.7 or E.5 --- use a window."""
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(label) + r'[ .]', t.strip())]
    return hits[-1] if hits else None


def stem(text, s):
    """Left-bounded only: has_token is letter-bounded on BOTH sides.  Provenance chat 113."""
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(s), text, re.I))


def stemlines(L, s):
    return [i for i, t in enumerate(L, 1) if re.search(r'(?<![A-Za-z])' + re.escape(s), t, re.I)]


print('=' * 100)
print('r2-ch16c  PROSE  chat 117  main L%d-L%d  (§30.3.3 - §30.3.9)' % (LO, HI))
print('=' * 100)

# ------------------------------------------------------------------ 1. pointers
print('\n## 1  EVERY §-POINTER IN THE UNIT, under BOTH resolvers, resolved to the CLAIM')
ptr = []
for i in range(LO, HI + 1):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', M[i - 1]):
        ptr.append((i, m.group(1)))
    for m in re.finditer(r'§([A-Z]\.\d+(?:\.\d+)*)', M[i - 1]):
        ptr.append((i, m.group(1)))
print('  pointer sites in unit: %d  %s' % (len(ptr), ptr))
CLAIM = {
    '18.4':   ('closure is a d-dimensional condition; no projection is a criterion',
               ['projection', 'closure', 'criterion', 'dimension']),
    '2.15.2': ('a derivation settling which predicate this book means',
               ['reorderable', 'closure', 'characteris', 'chain']),
    'E.5':    ('the precedence of Rival / Chen-Koh-Tan on maximal sublattices',
               ['Rival', 'sublattice', 'Chen', 'precedence']),
    'E.6':    ('the complexity question possibly settled in unread prior art',
               ['Ryter', 'Schmid', 'Adams', 'Dwinger', 'complexity', 'unread']),
}
for ln, sec in ptr:
    if re.match(r'^[A-Z]\.', sec):
        h = lettered_heading(M, sec)
        rng = None
        if h:
            nxt = next((i for i in range(h + 1, len(M) + 1)
                        if re.match(r'^#{1,4} ', M[i - 1].strip())), len(M) + 1)
            rng = (h, nxt)
        print('  L%d -> §%s  lettered heading %s  span %s' % (ln, sec, h, rng))
        if rng:
            seg = '\n'.join(M[rng[0] - 1:rng[1] - 1])
            want, toks = CLAIM.get(sec, ('(no single claim asserted)', []))
            print('        claim wanted: %s' % want)
            print('        tokens: %s' % {t: stem(seg, t) for t in toks})
        else:
            print('        NO HEADING ANYWHERE for §%s' % sec)
        continue
    br, ss = body_range(M, sec), section_span(M, sec)
    if br is None:
        print('  L%d -> §%s  NO HEADING ANYWHERE' % (ln, sec))
        continue
    same = 'COINCIDE' if br == ss else 'DIFFER'
    want, toks = CLAIM.get(sec, ('(pointer to a section, no single claim asserted)', []))
    print('  L%d -> §%s  body_range %s  section_span %s  %s' % (ln, sec, br, ss, same))
    print('        source line: %s' % M[ln - 1].strip()[:94])
    print('        claim wanted: %s' % want)
    for tag, rng in (('body_range', br), ('section_span', ss)):
        seg = '\n'.join(M[rng[0] - 1:rng[1] - 1])
        print('        %-12s %s' % (tag, {t: stem(seg, t) for t in toks} if toks else 'n/a'))

print('\n  L8516 "its structure is constructed in Chapter 7" -- chapter 7 resolved and swept')
c7 = section_span(M, '7')
seg7 = '\n'.join(M[c7[0] - 1:c7[1] - 1]) if c7 else ''
print('  chapter 7 span %s | structure %d  constructed %d  axis %d  embedding %d  tight %d'
      % (c7, stem(seg7, 'structur'), stem(seg7, 'construct'), stem(seg7, 'axis'),
         stem(seg7, 'embedd'), stem(seg7, 'tight')))

# ------------------------------------------------------------------ 2. attributions
print('\n## 2  EVERY ATTRIBUTION IN THE UNIT against ## References (BODY) and R.7')
refs_ln = last_md_heading(M, 'References')
r7_ln = lettered_heading(M, 'R.7')
print('  ## References occurrences: %s   BODY = L%s'
      % ([i for i, t in enumerate(M, 1) if t.strip() == '## References'], refs_ln))
print('  R.7 heading L%s' % r7_ln)
REFS = '\n'.join(M[refs_ln - 1:]) if refs_ln else ''
R7 = '\n'.join(M[r7_ln - 1:]) if r7_ln else ''
names = ['Booth', 'Lueker', 'Rival', 'Chen', 'Koh', 'Tan', 'Dilworth', 'Larson', 'Tucker',
         'NextClosure', 'Ganter', 'Anstee', 'Farber', 'Hoffman', 'Kolen', 'Sakarovitch',
         'Lubiw', 'Ryter', 'Schmid', 'Adams', 'Dwinger']
unbib = []
for n in names:
    inunit = [i for i in range(LO, HI + 1) if n in M[i - 1]]
    rf, r7 = stem(REFS, n), stem(R7, n)
    if rf == 0 and r7 == 0:
        unbib.append(n)
    print('  %-12s unit %-16s | References %d | R.7 %d | six-volume %s'
          % (n, str(inunit), rf, r7,
             {t: stem('\n'.join(L), n) for t, L in LINES.items() if stem('\n'.join(L), n)}))
print('  UNBIBLIOGRAPHED (zero in References AND zero in R.7): %s' % (unbib or 'none'))
print('  NOTE L8572 calls Ryter & Schmid and Adams-Dwinger-Schmid "both unread" -- R.7 is the')
print('  section for what is not cited and why, so that is where they belong if not in References.')

# ------------------------------------------------------------------ 3. register citations
print('\n## 3  REGISTER CITATIONS in the unit -- existence FIRST, then the headline')
rc = [(i, m.group(1)) for i in range(LO, HI + 1)
      for m in re.finditer(r'[Rr]egisters?\s+(\d+)', M[i - 1])]
print('  sites: %s' % (rc if rc else 'none in unit'))
R = LINES['reg']
for ln, num in rc:
    exact = [i for i, t in enumerate(R, 1) if re.match(r'^#{1,4}\s*' + num + r'\s*$', t.strip())]
    grouped = [i for i, t in enumerate(R, 1)
               if re.match(r'^#{1,4}\s*\d+\s*[-\u2013]\s*\d+\s*$', t.strip())
               and int(re.findall(r'\d+', t)[0]) <= int(num) <= int(re.findall(r'\d+', t)[1])]
    print('  register %s cited at main L%d' % (num, ln))
    print('     exact heading in Register: %s | grouped heading covering it: %s' % (exact, grouped))
    for j in (exact + grouped)[:1]:
        print('     entry headline: %s' % ' / '.join(
            x.strip() for x in R[j:j + 4] if x.strip())[:140])
    print('     citing line: %s' % M[ln - 1].strip()[:110])

# ------------------------------------------------------------------ 4. 16b-04 carried
print('\n## 4  16b-04 CARRIED: which section completes §30.2.3\'s landscape reading?')
print('  L8396 promises "§30.3.3 completes this reading".  Chat 116 measured §30.3.3 at zero.')
LAND = ['landscape', 'basin', 'potential', 'descent', 'plateau', 'stall', 'uphill', 'component']
for sec in ('30.3.3', '30.3.4', '30.3.5', '30.3.6', '30.3.7', '30.3.8', '30.3.9'):
    br, ss = body_range(M, sec), section_span(M, sec)
    seg = '\n'.join(M[br[0] - 1:br[1] - 1])
    hits = {t: stem(seg, t) for t in LAND if stem(seg, t)}
    print('  §%-8s %s %s  %s' % (sec, br, 'COINCIDE' if br == ss else 'DIFFER', hits or 'zero'))
print('  the landscape vocabulary in the UNIT, by line:')
for t in LAND:
    ls = [i for i in range(LO, HI + 1) if re.search(r'(?<![A-Za-z])' + t, M[i - 1], re.I)]
    if ls:
        for i in ls:
            print('     %-10s L%d  %s' % (t, i, M[i - 1].strip()[:84]))

# ------------------------------------------------------------------ 5. Ruling 45 / 46
print('\n## 5  RULING 45 -- process and past-state remarks, split from plain self-reference')
FORMS = ['an earlier version', 'an earlier draft', 'a previous draft', 'from recollection',
         'now states', 'the earlier figure of', 'the earlier reading', 'is withdrawn',
         'was tried first', 'is now discharged', 'reopened the question', 'unread',
         'nothing of this book', 'the whole reason']
for f in FORMS:
    hits = [i for i in range(LO, HI + 1) if f.lower() in M[i - 1].lower()]
    print('  %-24s unit %-14s main total %d'
          % (f, str(hits), len([1 for t in M if f.lower() in t.lower()])))
print('\n  candidate Ruling 45 sites read out in full:')
for ln in (_L(' **The fourth lemma, verified.** The three lemmas above were checked at 2,047, 3,751 and 20,000'), _L(" instances; the fourth stood on Booth and Lueker's construction and on nothing of this book's own."), _L(' It is now discharged, and it did not need a linear-time algorithm:'), _L(' on 1,098 of those 2,354 sets. That reading was tried first here and was wrong, which is the whole'), _L(' reason the qualifier is in the statement. Register 247.'), _L(' — and the census is finite within any box, which is what reopened the question. The infinite antichain')):
    print('     L%d  %s' % (ln, M[ln - 1].strip()[:100]))

print('\n## 6  RULING 46 -- script names, build numbers, internal files (case-sensitive, bounded)')
R46 = ['BUILD', 'gate.py', 'close.py', 'r2lib', 'tower-2.py', 'MANIFEST', 'md5', 'commit', 'repo']
for t in R46:
    hits = [i for i in range(LO, HI + 1)
            if re.search(r'(?<![A-Za-z])' + re.escape(t) + r'(?![A-Za-z])', M[i - 1])]
    print('  %-12s %s' % (t, hits if hits else 'zero sites in unit'))

print('\n## 7  FIRST-PERSON PRONOUNS in the unit')
fp = {p: [i for i in range(LO, HI + 1) if has_token(M[i - 1], p)]
      for p in ('I', 'we', 'our', 'us', 'my', 'ours')}
print('  %s' % ({k: v for k, v in fp.items() if v} or 'none'))

# ------------------------------------------------------------------ 8. census rows
print('\n## 8  DEFECT-CENSUS.tsv rows in range -- READ, not counted')
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
main_rows = sorted([r for r in recs if r[1] == 'main'], key=lambda r: r[2])
inr = [r for r in main_rows if LO <= r[2] <= HI]
print('  rows in unit: %d' % len(inr))
for r in inr:
    print('     id %-6d L%-6d %-28s token %r' % (r[0], r[2], r[3], r[4]))
    print('        line: %s' % M[r[2] - 1].strip()[:100])
before = [r for r in main_rows if r[2] < LO][-2:]
after = [r for r in main_rows if r[2] > HI][:2]
print('  WITNESS either side:')
for r in before + after:
    print('     id %-6d L%-6d %-28s %s' % (r[0], r[2], r[3], r[4]))
ids = [r[0] for r in before] + [r[0] for r in inr] + [r[0] for r in after]
print('  id run %s contiguous: %s' % (ids, all(b - a == 1 for a, b in zip(ids, ids[1:]))))

# ------------------------------------------------------------------ 9. duplicated sections
print('\n## 9  DUPLICATED-SECTION SWEEP (DEF-105 item 1) -- long unit lines recurring elsewhere')
long_lines = [(i, M[i - 1].strip()) for i in range(LO, HI + 1) if len(M[i - 1].strip()) >= 60]
dups = 0
for i, t in long_lines:
    for tag, L in LINES.items():
        for j, u in enumerate(L, 1):
            if u.strip() == t and not (tag == 'main' and j == i):
                print('     RECURS  main L%d == %s L%d  %s' % (i, tag, j, t[:66]))
                dups += 1
print('  %d long lines tested, %d recurrences' % (len(long_lines), dups))

# ------------------------------------------------------------------ 10. splice + table header
print('\n## 10  THE SPLICE AT L8563-L8567, and the TWICE-PRINTED TABLE HEADER at L8480/L8483')
for i in range(_L(" Λ's constraint graph is a tree. Its nine recovered extra edges are implied. Every sublattice and"), _L(' derivation — box → interval → sublattice → product, three preserving rules, no search.', 1)):
    print('     L%d  %s' % (i, M[i - 1].rstrip()[:104]))
join = M[_L("### 30.3.9 And it is not this book's problem")].rstrip() + ' ' + M[_L(" **Lubiw 1982** and the Γ-free matrix literature are the nearest neighbours; §2.15.2's derivation settles which predicate this book means.")].strip()
print('  L8563 + L8566 joined: ...%s' % join.strip()[-118:])
print('  L8563 ends mid-sentence: %s   L8566 begins mid-sentence: %s'
      % (not M[_L("### 30.3.9 And it is not this book's problem")].rstrip().endswith('.'), not M[_L(" **Lubiw 1982** and the Γ-free matrix literature are the nearest neighbours; §2.15.2's derivation settles which predicate this book means.")].lstrip()[:1].isupper()))
print('  L8564 and L8565 are two COMPLETE prior-art sentences inserted between them: %s'
      % (M[_L(" Λ's constraint graph is a tree. Its nine recovered extra edges are implied. Every sublattice and")].strip().endswith('.') and M[_L(' **Anstee & Farber 1984** and **Hoffman, Kolen & Sakarovitch 1985** give the recognition results.')].strip().endswith('.')))
print('\n  the step-law table, header printed twice:')
for i in range(_L('  2                     1                         eight, all 2-D', -1), _L(' The over-cap cases collapse to a single object: the full box. Its largest reorderable proper subset')):
    print('     L%d  %r' % (i, M[i - 1].rstrip()[:92]))

print('\n## 11  PRINTS & PROOFS: is the unit textually the same there?')
anchor = [i for i, t in enumerate(PP, 1) if t.strip().startswith('### 30.3.3 ')]
print('  PP §30.3.3 heading at %s' % anchor)
if anchor:
    a = anchor[-1]
    off = a - LO
    diffs = []
    for i in range(LO, HI + 1):
        j = i + off
        if 1 <= j <= len(PP) and PP[j - 1].rstrip() != M[i - 1].rstrip():
            diffs.append((i, j))
    print('  offset %d ; %d differing lines over the %d-line unit' % (off, len(diffs), HI - LO + 1))
    for i, j in diffs[:10]:
        print('     DIFF main L%d | PP P%d' % (i, j))
        print('        main: %s' % M[i - 1].rstrip()[:94])
        print('        PP  : %s' % PP[j - 1].rstrip()[:94])
    print('\n  WITNESSES ANCHORED ON THEIR OWN TEXT (the offset shifts at the inserted image line)')
    a2 = [i for i, t in enumerate(PP, 1) if 'constraint graph is a tree. Its nine recovered' in t]
    print('  splice: PP anchor %s' % a2)
    for i in a2:
        block_pp = [PP[j - 1].rstrip() for j in range(i, i + 5)]
        block_m = [M[j - 1].rstrip() for j in range(_L(" Λ's constraint graph is a tree. Its nine recovered extra edges are implied. Every sublattice and"), _L(' derivation — box → interval → sublattice → product, three preserving rules, no search.', 1))]
        print('     PP block == main L8563-L8567 block: %s' % (block_pp == block_m))
        for k, (p, m) in enumerate(zip(block_pp, block_m)):
            print('        P%-5d %s' % (i + k, p[:88]))
    print('  the two prior-art sentences sit inside the sentence in PP TOO -> AUTHORING, not')
    print('  production.  Docket 26 gets its clearest member and it is original.')
    print('  raw symbol test on the unit (never transliterated): Gamma-char %d, lambda-char %d'
          % (UTEXT.count('\u0393'), UTEXT.count('\u039b')))
    print('\n  caption: PP prints %s ; volume prints %s ; image reference in PP %s / volume %s'
          % ([i for i, t in enumerate(PP, 1) if 'Figure 23.2' in t],
             [i for i, t in enumerate(M, 1) if 'Figure 30.2' in t],
             [i for i, t in enumerate(PP, 1) if 'figure-30.2.png' in t] or 'absent',
             [i for i, t in enumerate(M, 1) if 'figure-30.2.png' in t]))
    print('  and "Figure 23.2" is LIVE elsewhere in the volume at %s -- the production')
    print('  renumbering resolved a collision.'
          % [i for i, t in enumerate(M, 1) if 'Figure 23.2' in t])
    print('  table header printed twice: main L8483 %r' % M[_L('  2                     1                         eight, all 2-D', 1)].rstrip()[:60])
    hdr_pp = [i for i, t in enumerate(PP, 1)
              if t.rstrip() == M[_L('  2                     1                         eight, all 2-D', 1)].rstrip() and _L('  5                                    8.68                       39          1.56', 1) < i < _L(' is a constraint system on those decisions, and every constraint is closed under reversing all of', 1)]
    print('                              PP sites in range %s -> twice in PP too: %s'
          % (hdr_pp, len(hdr_pp) >= 1))

# ------------------------------------------------------------------ 12. universals
print('\n## 12  UNIVERSALS AND SUPERLATIVES, each recorded measurable or NOT measurable')
UNIV = ['zero counterexamples', 'no interval nests', 'every row', 'all four', 'no signature',
        'never the reverse', 'never has one', 'no finite census', 'no search', 'no loss',
        'It is complete', 'unbounded', 'no projection']
for u in UNIV:
    for i in range(LO, HI + 1):
        if u.lower() in M[i - 1].lower():
            print('  L%-6d %-22s %s' % (i, u, M[i - 1].strip()[:76]))

print('\n## 13  "nine recovered extra edges" -- LOCATED in six volumes, not re-derived')
for probe in ('extra edge', 'recovered edge', 'nine recovered', 'constraint graph', 'implied'):
    hit = {}
    for tag, L in LINES.items():
        ls = stemlines(L, probe)
        if ls:
            hit[tag] = ls[:8]
    print('  %-18s %s' % (probe, hit or 'zero sites in six volumes'))

print('\n## 14  FIGURE REFERENCES vs FIGURE MEMBERS (production layer, NOT a text defect)')
figs = [i for i, t in enumerate(M, 1) if re.search(r'!\[Figure', t)]
print('  main-volume inline figure references: %d ; in unit: %s'
      % (len(figs), [i for i in figs if LO <= i <= HI]))
print('  PP inline figure references: %d' % len([1 for t in PP if re.search(r'!\[Figure', t)]))
print('  any .png member: %s' % ([f for f in os.listdir(H) if f.endswith('.png')][:5] or 'none'))

print('\n## 15  SINGLE-WITNESS SWEEP (docket 17) -- unit figures across six volumes')
for f in ('2,354', '1,098', '2,047', '3,751', '20,000', '18,736', '1,834', '401', '493',
          '89.8', '96.7', '1.66', '2.19', '4,168', '267,000', '11,943,936'):
    sites = {t: len(re.findall(NUMB % re.escape(f), '\n'.join(L))) for t, L in LINES.items()}
    tot = sum(sites.values())
    print('  %-12s total %-3d %s%s' % (f, tot, {k: v for k, v in sites.items() if v},
                                       '   SINGLE-WITNESS' if tot == 1 else ''))

print('\nEND r2-ch16c')
