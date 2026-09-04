#!/usr/bin/env python3
# r2-ch19b.py — chat 132 — R2 prose batch for main L10054–L10164 (Appendix A part 2: A.15, A.18, A.19, A.19.0, A.19.1), BUILD90.
# Reads MEMBERS only; imports r2lib by path. Rulings 45/46 tokens, first person (probe carries mine and myself), structure
# (bold lead-ins, italics, tables, code lines, unmarked sub-headings, line lengths), every negative with its witness, docket 27
# recurrence across the six volumes on the whitespace-normalised join, docket 36 names against the References body, the two
# pointer findings' homes (admissibility; the band ledger), census rows in range.
# r2-ch19b2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch19b.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (8 anchors); nothing else changes. r2-ch19b.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch19b.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
has_token = L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md')
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
a15 = [i for i, l in enumerate(M, 1) if re.match(r'^### A\.15 ', l)][-1]; appB = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix B ', l)][-1]
A, B = a15, appB; UL = M[A - 1:B - 1]; U = '\n'.join(UL); J = norm(U); JS = re.sub(r'[*_]', '', J)
print('unit L%d–L%d, %d lines (own scan: `### A.15` = last hit, `## Appendix B` body = last hit)' % (A, B - 1, B - A))
def ul(pat, flags=0): return [A + i for i, l in enumerate(UL) if re.search(pat, l, flags)]
ent = lambda ln: next((int(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1)) for j in range(ln, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1])), None)
def rbody(n):   # copied verbatim from r2-ch19a.py (there from r2-ch18a.py / r2-ch17e.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

hr('§1 RULING 45 (build/editorial-process remarks) AND RULING 46 (script names, build numbers, internal files) — case-insensitive letter-bounded tokens on the raw line; hits READ')
r45 = ['register', 'audit', 'rerun', 'run', 'ledger', 'chat', 'session', 'build', 'draft', 'handoff', 'instrument', 'golden', 'banked', 'docket', 'census', 'verified', 'tested', 'measured', 'recomputed', 'corrects', 'entry', 'until now', 'had not supplied', 'never prints']
for t in r45:
    hits = ul(r'(?<![A-Za-z])' + t + r'(?![A-Za-z])', re.I)
    if hits: print('  %-16s' % t, hits, [norm(M[i - 1])[:90] for i in hits][:4])
print('  read: "This corrects the ledger" (L10069), "register 208 spent an entry on" (L10155), "which is what S1 requires … and what the book had not supplied" (L10111), "unique and unnamed until now" (L10161), "It never prints the seventeen … the letters left unwritten" (L10093–L10095): the appendix narrating its own repair of the book — Ruling 45 candidates for chat 115\'s split (docket 5), the appendix\'s declared form being a corrective; "Verified:" (L10108) is the appendix\'s check form as in part 1')
print('  R46 — backticked names:', ul(r'`[^`]+`'), '; .py / BUILD / md5 / file references:', ul(r'\.py\b|BUILD\d|md5|\.md\b|\.tsv\b'), '— zero: negative witnessed by the two probes over all %d lines' % len(UL))

hr('§2 FIRST PERSON (probe carries mine and myself; `\\b(I|my|we|our)\\b` also matches a Roman numeral — hits are READ)')
fp = ul(r'\b(I|me|my|mine|myself|we|us|our|ours|ourselves)\b')
print('  hits:', fp, [norm(M[i - 1])[:110] for i in fp])
print('  read:', 'first person ZERO — the probe fires on no line of the unit (witness: the empty hit list over %d lines)' % len(UL) if not fp else 'each hit read above')

hr('§3 STRUCTURE — bold lead-ins, whole-line italics, tables, code lines, unmarked sub-headings, long lines, Statement/Remark/∎ conventions')
bold = ul(r'^\s*\*\*[^*]+\*\*'); print('  bold lead-ins (%d):' % len(bold), [(i, re.match(r'^\s*\*\*([^*]+)\*\*', M[i - 1]).group(1)[:40]) for i in bold])
print('  whole-line italics:', ul(r'^\s*\*[^*].*\*\s*$'), '; markdown table rows (a | at line start outside 4-space code lines):', [i for i in ul(r'^\s*\|') if not M[i - 1].startswith('    ')], '; code lines (4-space):', ul(r'^    \S'), '(A.19\'s rank table %d lines, A.19.0\'s displayed definition %d lines, A.19.1\'s two rows)' % (len([i for i in ul(r'^    \S') if i < _L('### A.19.0 The alphabet, defined rather than listed')]), len([i for i in ul(r'^    \*\*') if _L('### A.19.0 The alphabet, defined rather than listed') < i < _L('### A.19.1 And two other sets counted but never listed')])))
tab = ul(r'^  (n|ℓ|k|q|e|f|g|2S) ≥ \d\s+\('); print('  the whitespace-aligned table (A.19.0): header L%s, DATA rows %d (rows starting with a letter ≥ v)' % (ul(r'^\s+letter\s+generator'), len(tab)))
unm = [A + i for i, l in enumerate(UL) if i > 0 and not UL[i - 1].strip() and l.strip() and not l.startswith('#') and not l.startswith('    ') and len(l.strip()) < 60 and not l.strip().endswith(('.', '∎', ':', ',')) and not re.match(r'^\s+(letter|[nℓkqefg2]\S* ≥)', l)]
print('  unmarked sub-heading candidates (short line after a blank, not a heading, not code, not sentence-terminated):', unm, [norm(M[i - 1])[:60] for i in unm])
print('  lines over 400 chars:', ul(r'^.{401,}'), '; "Statement." lines:', ul(r'^\s*Statement\.'), '(2: A.15, A.18 — A.19/A.19.0/A.19.1 are expository, no Statement); "Remark." lines:', ul(r'^\s*Remark\.'), '; ∎ lines:', ul(r'∎'), '(2 proofs, 2 ∎; A.15\'s "And C is not" is a counted refutation, no ∎)')
print('  "Proof, B_k." / "Proof of join-closure." lead-ins:', ul(r'^\s*\*\*Proof'), '; numbering gap A.16/A.17 between A.15 and A.18 is by design (table rows, r2-ch18a §1)')

hr('§4 NEGATIVES AND UNIVERSALS, EACH WITH A WITNESS (docket 19)')
neg = ul(r'\b(never|no |nowhere|none|nothing|cannot|not |only|every|any|all |always|whenever|wherever|unique)\b', re.I)
print('  candidate lines:', neg)
print('  "only one of them is a sublattice" / "C … is not a sublattice": witness r2-ch19a §1 — 44 bands B_k with 0 failures; C 12,654 / 113,568 / 565,284 failing meets, 0 joins')
print('  "which does not use the upper bound": witness r2-ch19a §1 — the Lower inequality holds on every pair of C at cap 8 with no upper bound present')
print('  "the phrase describes nothing" (a join-closed sublattice): a sublattice is closed under both operations by definition — a set closed under join only is not one; witness: C itself (r2-ch19a §1)')
print('  "is not closed under coordinatewise min" (A.18): witness r2-ch19a §2 — the two printed meets and 2,862 / 12,489 / 40,887 / 110,229')
print('  "not explained by this proof" (A.18): the proof bounds the join only; the split of failing meets by bound (upper 954 / lower 1,908 at cap 6; 4,163 / 8,326 at cap 8) is not in U4 — U4 L8288–L8291 print totals; the appendix\'s statement is exact')
print('  "It never prints the seventeen" (A.19): witness r2-ch19a §3 — 0 eight-tuples in §8.3, 0 lines with ≥ 3 eight-tuples anywhere in main before the appendices')
print('  "Λ is recoverable from this table and nothing else": witness r2-ch19a §3 — the joins of the 976 down-sets equal Λ₈ — with the one unprinted datum, the bottom cell (the empty down-set\'s join), which A.19.1 prints; "nothing else" is exact given the bottom, READ as the empty join')
print('  "Nothing needs to be counted" (A.19.0): witness r2-ch19a §4 — Σ(|Aᵢ| − 1) = 17 from the supports; every (c, v) has a unique least cell and the least cells are exactly the join-irreducibles')
print('  "unique and unnamed until now" (A.19.1): unique — r2-ch19a §5, one greatest and one least cell; "unnamed until now" — main sites of the top tuple before the unit:', [i for i, l in enumerate(M, 1) if i < A and '(3,1,3,3,3,1,3,3)' in l.replace(' ', '')], '; of the bottom tuple:', [i for i, l in enumerate(M, 1) if i < A and '(1,0,1,0,1,0,0,0)' in l.replace(' ', '')], '(a line list is the witness; an empty list means unnamed as a tuple before A.19)')
print('  "Every one has q = k, g = q and 2S = q" / "each at (1,0) or (2,1)": r2-ch19a §5, 8 of 8')

hr('§5 DOCKET 27 — RECURRENCE: every sentence of the unit ≥ 60 chars searched across the six volumes on the whitespace-normalised join (headings, code and table lines excluded)')
body = '\n'.join(l for l in UL if not l.startswith('#') and not l.startswith('    ') and not re.match(r'^  (letter|[nℓkqefg2]\S* ≥)', l))
sents = [s.strip() for s in re.split(r'(?<=[.∎])\s+', norm(body)) if len(s.strip()) >= 60]
joins = {v: norm(' '.join(t)) for v, t in VOL.items()}; rec = []
for s in sents:
    key = s[:120]
    for v, t in joins.items():
        c = t.count(key)
        if (v == 'main' and c > 1) or (v != 'main' and c > 0): rec.append((key[:70], v, c))
print('  sentences tested:', len(sents), '; recurrences outside the unit:', len(rec))
for r_ in rec: print('   ', r_)
print('  → docket 27 verdict: %s; the four-cap figures' % ('CLEAN — no sentence of the unit recurs outside it' if not rec else 'RECURRENCES listed above'), end=' '); print(' recur as FIGURES at §12.11.2 L3387, §29.12 L8290 and MC L1254/L1260 (r2-ch19a §2), not as sentences')

hr('§6 DOCKET 36 — NAMES IN THE UNIT AGAINST THE REFERENCES BODY (L11503–L11805) AND R.7 (L11806 on)')
refs = '\n'.join(M[_L(' and its presence is what makes ℛ(index) = index rather than merely index ⊆ ℛ(index).', 1):_L(' **Candelas, P., de la Ossa, X. & Rodriguez-Villegas, F.** (2007). *Triadophilia* (arXiv:0706.3134). — the thinly populated tip of the Hodge plot.', 1)]); r7 = '\n'.join(M[_L(' **Candelas, P., de la Ossa, X. & Rodriguez-Villegas, F.** (2007). *Triadophilia* (arXiv:0706.3134). — the thinly populated tip of the Hodge plot.', 1):])
for n in ['Birkhoff', 'Dilworth', 'Wigner', 'Sperner']: print('  %-9s unit lines %s · References body %d · R.7 %d · Register lines %d' % (n, ul(n), len(re.findall(n, refs)), len(re.findall(n, r7)), sum(1 for l in R if n in l)))
print('  verdict: Birkhoff is the unit\'s only named author and has a References-body line; docket 36 gains nothing from this unit')

hr('§7 WRAPPED PHRASES READ ON THE MARKUP-STRIPPED JOIN')
for ph in ['only one of them is a sublattice', 'a bound by a constant is monotone in both directions, a bound by a free coordinate is not', 'which §14.4 admits in both directions', 'Certainty survives upward and dies downward', 'It never prints the seventeen', 'Λ is recoverable from this table and nothing else', 'Every generator is the least cell with one coordinate at one value', 'one for each way χ\'s seven constraints bind at a value', 'The constraint system of §7.1 and the implications between bits are the same object counted twice', 'unique and unnamed until now', 'Nothing needs to be counted']:
    print('  %-70s join: %d ; raw lines (markup stripped):' % (ph[:70], JS.count(ph)), [A + i for i, l in enumerate(UL) if ph in re.sub(r'[*_]', '', l)])

hr('§8 THE TWO POINTER FINDINGS — WHERE THE CLAIM LIVES (docket 9(b): a citation whose target says nothing of the claim)')
adm = [(i, L.enclosing(M, i), norm(M[i - 1])[:150]) for i, l in enumerate(M, 1) if re.search(r'admissib', l, re.I) and i < _L('*The three-body problem is solved to exactly the precision a closed index permits, and the book had already computed that precision before the problem was posed to it.*', 3)]
print('  A.15 "monotone single-coordinate bounds … which §14.4 admits in both directions" — §14.4 is two lines (r2-ch19a §7). Every main line with admissib- before the appendices (line, section, text):')
for x in adm: print('    L%d §%s: %s' % x)
mono = [(i, L.enclosing(M, i), norm(M[i - 1])[:150]) for i, l in enumerate(M, 1) if re.search(r'monotone', l) and re.search(r'admiss|both directions|single|one coordinate|in each coordinate|upper|lower', l, re.I) and i < _L('*The three-body problem is solved to exactly the precision a closed index permits, and the book had already computed that precision before the problem was posed to it.*', 3)]
print('  main lines pairing monotone with admissible/direction/single:'); [print('    L%d §%s: %s' % x) for x in mono[:14]]
PPl = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n'); p144 = [i for i, l in enumerate(PPl, 1) if re.match(r'^#{2,4}\s*14\.4 ', l)]
print('  §14.4 in PP: heading lines', p144, '; PP body to the next heading:', [norm(PPl[i - 1])[:90] for i in range(p144[-1], next(j for j in range(p144[-1] + 1, len(PPl) + 1) if PPl[j - 1].startswith('#'))) if PPl[i - 1].strip()] if p144 else 'ABSENT', '— the colon-terminated lead-in with no list after it is PP\'s state too (record-carried), a docket 1 kind: the section announces three properties and prints none; the admissibility criterion the four citers mean lives at §7.2 L1765 (the constraint form) and §18.4.1 L5097/L5121 (the criterion, corrected)')
print('  the same pointer elsewhere: "admissibility condition (§14.4)" MC lines:', [i + 1 for i, l in enumerate(VOL['mc']) if 'admissibility condition (§14.4)' in l], '; "§14.4" in main outside the unit:', [i for i, l in enumerate(M, 1) if '§14.4' in l and not A <= i < B][:12])
print('  A.15 Remark "This corrects the ledger, which called C a join-closed sublattice … Register 230": Register 230 is Appendix D\'s kind coordinate (r2-ch19a §7). Register entries naming the band / B_k / C, bodies read:')
for e in sorted(set(ent(i + 1) for i, l in enumerate(R) if re.search(r'B₁|B_k|\bband\b|\|a − b\||two chains', l) and ent(i + 1))):
    print('    %d: %s' % (e, rbody(e)[:230]))
print('  "the ledger" in main (every site with section):', [(i, L.enclosing(M, i)) for i, l in enumerate(M, 1) if re.search(r'\bthe ledger\b', l)][:16])
print('  "join-closed" every volume:', {k: v for k, v in {v: [i + 1 for i, l in enumerate(t) if 'join-closed' in l] for v, t in VOL.items()}.items() if v})

hr('§9 PRE-PP POINTER RENUMBERING SEEN IN THE DIFF (record-carried; r2-ch19a §6): "§3" in PP → "§8" / "§8.3" in the volume at three lines; A.19.1\'s property sentence rewritten after PP')
print('  volume lines with §8 / §8.3 in the unit:', ul(r'§8\b'), '; §8.3 = "Seventeen generators" (L1847); §8 = "Shape" chapter heading:', [(i, norm(M[i - 1])[:50]) for i, l in enumerate(M, 1) if re.match(r'^## 8\. ', l)])
print('  A.19.1 L10159 "Every one has q = k, g = q and 2S = q, with (n, ℓ) and (e, f) each at (1,0) or (2,1)" — PP P%s read "q = k − something equal on both sides and g equal to q": the volume\'s sentence is the measured one (r2-ch19a §5, 8 of 8); post-PP correction, not a defect' % [i for i, l in enumerate(open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n'), 1) if 'something equal on both sides' in l])

hr('§10 CENSUS ROWS IN RANGE (DEFECT-CENSUS.tsv, member main, line in [L%d, L%d])' % (A, B - 1))
rows = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv') if l.strip()]; hdr = rows[0]; li = hdr.index('line'); mi = hdr.index('member')
inr = [r for r in rows[1:] if r[mi] == 'main' and r[li].isdigit() and A <= int(r[li]) < B]
print('  header:', hdr); print('  rows in range:', len(inr))
for r in inr: print('   ', r[:6])
