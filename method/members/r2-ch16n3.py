#!/usr/bin/env python3
# r2-ch16n2.py — chat 153 — SUCCESSOR to r2-ch16n.py, re-anchored. Identical measurements; addresses move.
# r2-ch16n carried a hard-coded site LIST; three of its nine entries (9722, 9894, 11853) sit above the
# shift and now name the wrong lines. Those three are resolved by their own text; the six below the
# insertion point are untouched, because they did not move.
# r2-ch16n is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: reproduces r2-ch16n.out byte-exact on the pre-shift bundles (G0c).
# r2-ch16n3.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16n2.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (23 anchors); nothing else changes. r2-ch16n2.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 94+198 — reproduces r2-ch16n2.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16n --- chat 121 --- PROSE batch for main L8889-L9029.

Same discipline as r2-ch16m: r2lib by path, resolvers take the LINE LIST, members never a bundle,
no wall-clock time.  Every negative states what the sweep covered.  Symbols are tested RAW.
A probe scoring zero on its own volume is a broken probe, not a finding.
"""
import re, sys, importlib.util

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing  # noqa: E402

VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open('/home/claude/members/' + v, encoding='utf-8').read().split('\n') for k, v in VOL.items()}
M = V['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
U0, U1 = _L('### 32.1.2 Four of the seven, answered by computation'), _L(' Register 373.', 1)
out = []
def p(*a): out.append(' '.join(str(x) for x in a))
# Sites resolved by their own text rather than carried as line numbers. r3-wl2's +8 shift at main
# L9608 moved every one of them; a literal cannot follow its line, a search can.
def _at(_sub, _L=None):
    _L = M if _L is None else _L
    _h = [_i for _i, _l in enumerate(_L, 1) if _sub in _l]
    assert len(_h) == 1, 'anchor %r matches %d lines, not 1' % (_sub, len(_h))
    return _h[0]



def body_range(Mx, sec):                      # owed to r2lib; provenance chat 108
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def lettered_heading(Mx, label):              # owed to r2lib; provenance chat 118
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(label) + r'[ .]', t.strip())]
    return hits[-1] if hits else None


def last_md_heading(Mx, title):               # owed to r2lib; the BODY occurrence
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(title) + r'\s*$', t.strip())]
    return hits[-1] if hits else None


def numsites(Mx, n, lo=1, hi=None):
    """Digit-bounded numeral SITE lister --- sites, never a count.  A figure spelled in words is
    invisible to it, so the word form is swept separately.  Owed to r2lib."""
    hi = hi or len(Mx)
    pat = re.compile(r'(?<![\d.,])' + str(n) + r'(?!\d)(?!,\d)(?!\.\d)')
    return [i for i in range(lo, hi + 1) if pat.search(Mx[i - 1])]


# ============================================================ A. pointers, both resolvers
p('== A. every pointer the unit makes, resolved under body_range AND section_span ==')
for sec in ('32.2', '18.6', '17', '22.4', '12.11.3.1', '32.1.4', '18.4.1'):
    br, ss = body_range(M, sec), section_span(M, sec)
    same = 'COINCIDE' if br == ss else 'DIFFER'
    p(f'  §{sec}: body_range {br}  section_span {ss}  {same}')
for lab in ('F.4.1', 'F.4.3'):
    h = lettered_heading(M, lab)
    p(f'  §{lab}: lettered_heading L{h}' + (f'  "{M[h-1].strip()[:80]}"' if h else '  ABSENT'))

p('  --- §32.2 read IN FULL (the S3 claim L8921-22 attributes to it):')
b322 = body_range(M, '32.2')
for i in range(b322[0], b322[1]):
    p(f'      L{i}: {M[i-1].strip()[:150]}')

p('  --- §18.6, the sentence L8980 attributes to it ("calls it the prediction budget"):')
b186 = body_range(M, '18.6')
hits = [i for i in range(b186[0], b186[1]) if re.search(r'budget', M[i - 1], re.I)]
p(f'      body {b186}; "budget" at {hits}')
for i in hits[:4]:
    p(f'      L{i}: {M[i-1].strip()[:150]}')
p(f'      "prediction budget" anywhere in main: {[i for i,t in enumerate(M,1) if "prediction budget" in t.lower()]}')

p('  --- §17\'s extension test, the requirement L8991 attributes to it ("a candidate axis offered"):')
s17 = section_span(M, '17')
p(f'      section_span(17) {s17}; body_range(17) {body_range(M, "17")}')
for probe in ('offer', 'candidate', 'extension test', 'axis'):
    h = [i for i in range(s17[0], s17[1]) if re.search(r'(?<![A-Za-z])' + probe, M[i - 1], re.I)]
    p(f'      "{probe}" in §17 span: {len(h)} sites {h[:10]}')

p('  --- §22.4\'s closing result, cited at L8994:')
b224 = section_span(M, '22.4')
p(f'      section_span(22.4) {b224}; last two non-blank body lines:')
nb = [i for i in range(b224[0], b224[1]) if M[i - 1].strip()]
for i in nb[-2:]:
    p(f'      L{i}: {M[i-1].strip()[:150]}')

p('  --- §12.11.3.1\'s division of bounds, cited at L9017:')
b12 = section_span(M, '12.11.3.1')
p(f'      section_span {b12}')
h = [i for i in range(b12[0], b12[1]) if re.search(r'(?<![A-Za-z])(law|extent)(?![A-Za-z])', M[i - 1], re.I)]
p(f'      "law"/"extent" at {h[:10]} ({len(h)})')
for i in h[:3]:
    p(f'      L{i}: {M[i-1].strip()[:150]}')

p('  --- part labels (parts carry NO markdown heading; the printed label is swept instead):')
plab = [(i, M[i - 1].strip()[:60]) for i, t in enumerate(M, 1) if re.match(r'^#*\s*PART\b', t.strip())]
p(f'      {len(plab)} PART labels: {[i for i,_ in plab]}')
for i, t in plab:
    p(f'      L{i}: {t}')
p(f'      L8958 "register 321 promoted the procedure to PART I" --- PART I above is the test')
p(f'      L8957 "Part VI carries the record" and L9021 "Parts II and III" resolve against that list')

# ============================================================ B. Ruling 45 / 46
p('')
p('== B. Ruling 45 (build and editorial-process narration) and Ruling 46 (script, build, file names) ==')
R45 = ['this build', 'the press', 'at every build', 'the session', 'these sessions', 'was written',
       'recomputed now', 'compressed', 'from here', 'this section was written', 'intake',
       'the book now prints', 'stopped being hidden', 'the book will track']
seen45 = {}
for i in range(U0, U1 + 1):
    for t in R45:
        if t in M[i - 1].lower():
            seen45.setdefault(i, []).append(t)
p(f'  Ruling 45 candidate sites in the unit: {len(seen45)}')
for i in sorted(seen45):
    p(f'      L{i} [{", ".join(seen45[i])}]: {M[i-1].strip()[:120]}')
R46 = re.compile(r'\b[a-z0-9_]+\.py\b|\bBUILD\d+\b|\bgate\.py\b|\bclose\.py\b|MANIFEST|\.tsv\b|\.md\b')
h46 = [(i, R46.findall(M[i - 1])) for i in range(U0, U1 + 1) if R46.search(M[i - 1])]
p(f'  Ruling 46 sites in the unit (case-sensitive): {len(h46)} {h46}')
p(f'      sweep covered every line L{U0}-L{U1} for .py, BUILD<n>, MANIFEST, .tsv and .md tokens')

# ============================================================ C. spliced text
p('')
p('== C. the spliced-text class (DEFERRED item 26) at L8908-L8912 ==')
for i in range(_L(' **Flag 2 — fibration — is answered by disclosure, not by repair.** The honest number for a fibred'), _L(' the fibred ones appear. Nothing was fixed; something was stopped being hidden.', 1)):
    p(f'      L{i}: {M[i-1].rstrip()}')
joined = ' '.join(M[i - 1].strip() for i in range(_L(' **Flag 2 — fibration — is answered by disclosure, not by repair.** The honest number for a fibred', 1), _L(' the fibred ones appear. Nothing was fixed; something was stopped being hidden.')))
p(f'  two-line join L8909-L8911: "{joined[:220]}"')
p(f'  "= 0 at one fibre" occurrences in the join: {joined.count("= 0 at one fibre")}')
p(f'  line-length profile of the unit (chars): '
  f'{[len(M[i-1]) for i in range(_L(' **Flag 2 — fibration — is answered by disclosure, not by repair.** The honest number for a fibred'), _L(' the fibred ones appear. Nothing was fixed; something was stopped being hidden.', 1))]} --- L8910 is short where its neighbours run long')

# ============================================================ D. count words, N-of-M, universals
p('')
p('== D. count words, N-of-M forms and list-opening universals, each against its own body ==')
CW = ['four', 'seven', 'three', 'six', 'two', 'eight', 'fifty-five', 'forty-two', 'thirty-four',
      'nineteen', 'twenty', 'eleven', 'forty-eight', 'nineteenth', 'twentieth']
for w in CW:
    h = [i for i in range(U0, U1 + 1) if has_token(M[i - 1], w)]
    if h:
        p(f'  "{w}": {h}')
p('  N-of-M forms in the unit:')
for i in range(U0, U1 + 1):
    for m in re.finditer(r'\b(\w+)\s+of\s+(?:the\s+)?(\w+[\w-]*)\b', M[i - 1]):
        if re.match(r'^(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d+)$',
                    m.group(1), re.I):
            p(f'      L{i}: "{m.group(0)}"  in: {M[i-1].strip()[:110]}')
p('  universals in the unit ("every", "each", "all", "nothing", "never", "only"):')
for i in range(U0, U1 + 1):
    for w in ('every', 'each', 'all', 'nothing', 'never', 'only'):
        if has_token(M[i - 1], w):
            p(f'      L{i} [{w}]: {M[i-1].strip()[:120]}')
            break

# ============================================================ E. numeral sites
p('')
p('== E. digit-bounded numeral SITES for every figure the unit prints (sites, not counts) ==')
FIG = ['976', '8,853', '89,438', '267,858', '499,246', '18', '68', '26', '4', '42', '34', '8',
       '55', '33', '17', '48', '23', '21', '7.07', '16', '3', '540', '162']
for f in FIG:
    s_in = numsites(M, re.escape(f), U0, U1)
    s_out = [i for i in numsites(M, re.escape(f)) if not (U0 <= i <= U1)]
    p(f'  {f:>8}: in-unit {s_in}   out-of-unit {len(s_out)} sites, first eight {s_out[:8]}')
p('  word-form figures (invisible to the digit sweep):')
for w in ('fifty-five', 'forty-two', 'thirty-four', 'forty-eight', 'thirty-three', 'seventeen',
          'one thousand six hundred and thirty-five', 'twenty-five'):
    h = [i for i in range(U0, U1 + 1) if w in M[i - 1].lower()]
    if h:
        p(f'      "{w}" in unit at {h}')

# ============================================================ F. Prints & Proofs, per-witness anchor
p('')
p('== F. Prints & Proofs, every witness anchored on its OWN text (one global offset cannot span a unit) ==')
WIT = ['Four of the seven, answered by computation',
       'The frame has changed, and the change is measurable',
       'What this book names before anyone tells it',
       'Which of this book\'s numbers hold still',
       'The honest number for a fibred index is its unfibred one',
       'Fifty-five cells are named and nobody has put anything in them',
       'Every figure about', 'the two companion papers',
       'six and a half times chance', 'the register is a quarter of it']
def joins(X):
    """line i paired with the join of lines i and i+1, so a phrase broken by the wrap is visible."""
    return [(i, re.sub(r'\s+', ' ', X[i - 1] + ' ' + (X[i] if i < len(X) else '')))
            for i in range(1, len(X) + 1)]
MJ, PJ = joins(M), joins(PP)
for w in WIT:
    wl = w.lower()
    m_hits = [i for i, t in MJ if wl in t.lower() and U0 <= i <= U1]
    p_hits = [i for i, t in PJ if wl in t.lower()]
    off = (p_hits[0] - m_hits[0]) if (m_hits and p_hits) else None
    flag = '' if m_hits else '  <-- BROKEN PROBE: scores zero on its own volume, not a finding'
    p(f'  "{w[:52]}": main {m_hits}  PP {p_hits[:3]}  offset {off}{flag}')
p(f'  sweep covered all {len(WIT)} witnesses against the full PP file ({len(PP):,} lines)')

# ============================================================ G. census rows, duplication, attributions
p('')
p('== G. census rows in range, duplicated-section sweep, attribution sweep ==')
rows = open('/home/claude/members/DEFECT-CENSUS.tsv', encoding='utf-8').read().split('\n')
hdr = rows[0].split('\t')
ci = {c: k for k, c in enumerate(hdr)}
p(f'  DEFECT-CENSUS.tsv columns {hdr}; member values '
  f'{sorted({r.split(chr(9))[ci["member"]] for r in rows[1:] if r.strip()})}')
inrange = []
for r in rows[1:]:
    if not r.strip():
        continue
    f = r.split('\t')
    if f[ci['member']] in ('main', 'all'):
        try:
            ln = int(f[ci['line']])
        except ValueError:
            continue
        if U0 <= ln <= U1:
            inrange.append((f[ci['id']], f[ci['class']], f[ci['member']], ln, f[ci['item']][:40]))
p(f'  rows with member in (main, all) and line in [{U0},{U1}]: {len(inrange)}')
for r in inrange:
    p(f'      {r}')
p('  duplicated-section sweep (DEF-105 item 1): every unit line over 60 chars sought elsewhere:')
longs = [i for i in range(U0, U1 + 1) if len(M[i - 1].strip()) > 60]
dups = []
for i in longs:
    s = M[i - 1].strip()
    for j, t in enumerate(M, 1):
        if j != i and t.strip() == s:
            dups.append((i, j))
p(f'      {len(longs)} long lines swept, {len(dups)} recur elsewhere in the main volume {dups[:6]}')
p('  attribution sweep: proper-noun attributions in the unit against ## References (BODY) and R.7:')
refs = last_md_heading(M, 'References')
p(f'      "## References" BODY occurrence at L{refs}; all "## References" occurrences '
  f'{[i for i,t in enumerate(M,1) if re.match(r"^#{1,4}\s+References\s*$", t.strip())]}')
att = []
initial = []
for i in range(U0, U1 + 1):
    for m in re.finditer(r'\b([A-Z][a-z]{3,})\b', M[i - 1]):
        w = m.group(1)
        pre = M[i - 1][:m.start()].rstrip()
        if pre.endswith('.') or pre in ('', '**') or pre.endswith('**'):
            initial.append((i, w))
            continue
        if w not in ('This', 'That', 'What', 'Where', 'Which', 'Every', 'Each', 'Asked', 'Three',
                     'Four', 'Five', 'Flag', 'Flags', 'Register', 'Registers', 'Appendix',
                     'Appendices', 'Defects', 'Conflating', 'Nothing', 'Those', 'They', 'Measured',
                     'Recomputed', 'Fifty', 'Part', 'Parts', 'Their', 'Chapter', 'Chapters',
                     'Operationalised', 'Self', 'Book', 'From', 'Only', 'Both', 'Here', 'When',
                     'With', 'Then', 'Also', 'There', 'These', 'Some', 'Such', 'Have', 'Been'):
            att.append((i, w))
p(f'      mid-sentence capitalised tokens in the unit: {sorted(set(w for _, w in att))}')
p(f'      sentence-INITIAL capitalised tokens (reported, not hidden --- an attribution can open a '
  f'sentence): {sorted(set(w for _, w in initial))}')
p(f'      sweep covered every line L{U0}-L{U1} in both positions')

p('')
p('== I. the two cited criteria read AT THEIR TARGETS, and where the claim does live ==')
p('  §17, cited at L8991 for "requires a candidate axis to be OFFERED before it can be judged":')
for i in (_L(' **A difference is not a lattice homomorphism** — §18.2 refuses ν = e − δ as an axis for exactly that'), _L(' closure. Seniority parity at axis 10, the conjugation ceiling at axis 12, and the electromagnetic')):
    p(f'      L{i}: {M[i-1].strip()[:150]}')
p(f'      §17 heading L4789: {M[_L(' nowhere else.', 1)].strip()[:110]}')
sub17 = [(i, M[i - 1].strip()[:90]) for i in range(_L('    A closed index determines what may be added to it.', -1), _L(' The results of this chapter are the strongest in the book, and every one of them is negative.', -1)) if re.match(r'^#{1,4} 17', M[i - 1])]
p(f'      §17 subsection headings: {sub17}')
for probe in ('extension test', 'offered', 'new coordinate', 'candidate axis'):
    h = [i for i, t in enumerate(M, 1) if probe in t.lower()]
    p(f'      "{probe}" across the WHOLE main volume: {len(h)} sites {h[:10]}')
b172 = body_range(M, '17.2')
p(f'      §17.2 "E2 — which axes may be adjoined" READ IN FULL at its target, body_range {b172}:')
for i in range(b172[0], b172[1]):
    if M[i - 1].strip():
        p(f'      L{i}: {M[i-1].strip()[:150]}')
p('  §22.4, cited at L8994 for a "closing result" about language:')
b224b = body_range(M, '22.4')
p(f'      body_range {b224b}; heading and body:')
for i in range(b224b[0], b224b[1]):
    if M[i - 1].strip():
        p(f'      L{i}: {M[i-1].strip()[:150]}')
sub224 = [(i, M[i - 1].strip()[:90]) for i in range(_L('### 22.4 The price of limit-freedom, computed'), _L('### 22.5 Admissibility')) if re.match(r'^#{1,4} 22\.4', M[i - 1])]
p(f'      §22.4 subsection headings: {sub224}')
for probe in ('language', 'no language for'):
    h = [i for i in range(_L('### 22.4 The price of limit-freedom, computed'), _L('### 22.5 Admissibility')) if probe in M[i - 1].lower()]
    p(f'      "{probe}" in the §22.4 span: {h}')
    hv = [i for i, t in enumerate(M, 1) if 'no language for' in t.lower()]
    if probe == 'no language for':
        p(f'      "no language for" across the WHOLE main volume: {hv}')

# ============================================================ H. the companion papers
p('')
p('== H. "the two companion papers" (L8945) against "the third companion paper" (L9001) ==')
for i in [_L(' indices of the companion paper. Λ states F(z₁…z₈); the tower states its five bounds; the register'), _L(" That is the third companion paper's third finding arriving in the book's own instruments: **an arrow"), _L(' computed objects await constructions the companion papers do not print; six are definitional roots'), _L(' rather than a relation is the one the companion paper uses to withdraw a false node of its own:'), _L(' by something other than attention. The third column is the two companion papers — the method applied'), _L(" Measured across three states of the book — before the third companion paper's intake, before the"),
          _at('The challenge posed in 1969 is closed'),
          _at('*A challenge posed outside this work'),
          _at('The two companion papers carry their own reference lists')]:
    if i <= len(M):
        p(f'  L{i}: {M[i-1].strip()[:160]}')
p(f'  chapter headings 35 and 36: '
  f'{[(n, heading_line(M, n)) for n in ("35", "36")]}')
for n in ('35', '36'):
    h = heading_line(M, n)
    if h:
        p(f'      L{h}: {M[h-1].strip()[:110]}')

sys.stdout.write('\n'.join(out) + '\n')
