# r2-ch24b.py — Appendix E part 1 (main L10898–L11053), the PROSE and POINTER claims (chat 137).
# Reads MEMBERS by name (never a bundle path) and the Prints & Proofs original at /home/claude/PP_The_Method_1_6.md; imports r2lib by path; deterministic.
# r2-ch24b2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch24b.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (29 anchors); nothing else changes. r2-ch24b.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch24b.out byte-exact on those bundles (G0c)

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
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
P = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

def rbody(n):   # copied verbatim from r2-ch23a.py (there from r2-ch22a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch23a.py (there from r2-ch22a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch23a.py (there from r2-ch22a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch24b — Appendix E part 1 (lead, E.1–E.1.5, E.2), prose and pointers')
s = lettered(M, 'Appendix E')[-1]; t = lettered(M, 'E.3')[-1]; U = M[s - 1:t - 1]
strip = lambda l: re.sub(r'\*\*|\*', '', ' '.join(l.split()))   # markup-stripped, whitespace-normalised
J = ' '.join(strip(l) for l in U)   # the two-line join of the whole unit, for wrapped phrases
print('§0 unit L%d–L%d (%d lines)' % (s, t - 1, len(U)))

# §1 headings against PP from `# Appendix E` (PP P10437 by the handoff; re-taken). PP's sub-headings are UNMARKED: a line indented one space after a blank line
# that begins `E.n` — read them, not just probe them (a bold paragraph or an epigraph is not a heading). Section number stripped from BOTH sides.
pe = [i for i, l in enumerate(P, 1) if re.match(r'^#{1,4}\s*Appendix E\b', l)][-1]; pf = [i for i, l in enumerate(P, 1) if re.match(r'^#{1,4}\s*Appendix F\b', l)][-1]
ppsub = [(i, P[i - 1].strip()) for i in range(pe + 1, pf) if re.match(r'^ ?E\.\d+(\.\d+)* [A-Z]', P[i - 1])]   # heading-form lines; READ below — the blank-line-above rule alone dropped PP's E.1.1 and E.1.3 (chat-137 fault 1)
print('   PP heading-form E.n lines without a blank line above (read as headings on their text):', [(i, l[:60]) for i, l in ppsub if P[i - 2].strip()])
mh = [(i, M[i - 1]) for i in range(s, t) if re.match(r'^#{1,4} ', M[i - 1])]
num = lambda l: re.sub(r'^#*\s*(Appendix E|E\.\d+(?:\.\d+)*)\s*[—–-]?\s*', '', l.strip())
print('§1 PP `# Appendix E` P%d to `# Appendix F` P%d (%d lines; main unit %d); PP unmarked E.n sub-headings in the appendix: %d' % (pe, pf, pf - pe, lettered(M, 'Appendix F')[-1] - s, len(ppsub)))
for i, l in ppsub: print('   P%d %s' % (i, l[:100]))
ppt = {num(l) for i, l in ppsub} | {num(P[pe - 1])}
for i, l in mh: print('   main L%d %-8s in PP (number stripped): %s' % (i, l.split(' ')[1], num(l) in ppt))
print('   E.3 onwards (part 2) PP sub-headings present:', [l.split(' ')[0] for i, l in ppsub if not re.match(r'E\.[12](\.\d)?$', l.split(' ')[0])])

# §2 body diff against PP on the part-1 range (PP from the heading to its `E.3` line)
pe3 = next(i for i, l in ppsub if l.startswith('E.3')); PU = P[pe - 1:pe3 - 1]
mb = Counter(strip(l) for l in U if l.strip()); pb = Counter(strip(l) for l in PU if l.strip())
om = [l for l in mb if l not in pb]; op = [l for l in pb if l not in mb]
print('§2 body: PP non-blank %d, main %d, shared %d, only-main %d, only-PP %d' % (sum(pb.values()), sum(mb.values()), sum((mb & pb).values()), len(om), len(op)))
for l in om: print('   only-main:', l[:150])
for l in op: print('   only-PP  :', l[:150])

# §3 pointers — each resolved to its heading AND to the claim, under both resolvers (body_range / section_span); lettered targets by exact token
def sec_hits(sec, pats):
    b = body_range(M, sec); sp = section_span(M, sec); return M[b[0] - 1][:70], {p: (sum(1 for i in range(*b) if re.search(p, M[i - 1], re.I)), sum(1 for i in range(*sp) if re.search(p, M[i - 1], re.I))) for p in pats}
def let_hits(tag, pats):
    h = lettered(M, tag)
    if not h: return None, {}
    a = h[-1]; b = next(i for i in range(a + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1])); return (a, M[a - 1][:70]), {p: sum(1 for i in range(a, b) if re.search(p, M[i - 1], re.I)) for p in pats}
print('§3 pointers (hits under body_range, section_span):')
for sec, pats, note in (('32.1.1', [r'flag 2', r'fibred zero|fibred'], 'L10901 *see §32.1.1 flag 2 for what a fibred zero is worth*'),
                        ('12.11.7', [r'\bQ\b', r'four', r'tower'], 'L10906 *four entered by §12.11.7*'), ('29.2.1', [r'novelty', r'nothing'], 'L10961 *fell to nothing under §29.2.1*'),
                        ('12.11.3.1', [r'assert', r'compute', r'extent'], 'L10983 *§12.11.3.1\'s rule … assert the law, compute the extent*'),
                        ('32.1.4', [r'value sets|value set', r'ℛ\(X\)|\\prod|∏', r'repair'], 'L10994 *§32.1.4 says why it cannot be repaired from inside*'),
                        ('29.2.2', [r'branches', r'leave'], 'L11003 *§29.2.2\'s reading that the branches leave the object*'), ('14.5', [r'Cl\(ℛ\)|closed subsets|closed sets', r'size'], 'L11029 *|Cl(ℛ)| for Λ, which §14.5 states as a size*'),
                        ('29', [r'#P', r'closed sets|closure system'], 'L11023 *#P-complete (§29)*'),
                        ('23.10', [r'1,585', r'25\.96', r'0\.0164', r'518', r'(?<![\d,.])34(?![\d,])', r'containment', r'157', r'560', r'zero failures', r'Proposition 23\.1', r'classical bracket'], 'E.2 §23.10 items'),
                        ('23.11', [r'interior optimum', r'monoton', r'admissibility cap'], 'E.2 §23.11'), ('26.6', [r'Richardson', r'p\s?[−-]\s?1', r'accelerat'], 'E.2 §26.6'),
                        ('29.8', [r'Gr[öo]bner', r'eight', r'claim set'], 'E.2 §29.8'), ('11.8.1', [r'F\(−1\)', r'two values', r'coupling'], 'E.2 §11.8.1'), ('16.7', [r'amplification', r'0\.972', r'descendants', r'N\[φ'], 'E.2 §16.7')):
    h, d = sec_hits(sec, pats); print('   §%-9s %-55s %s — %s' % (sec, h, d, note))
for tag, pats, note in (('D.1', [r'ordered', r'fibred|fibre', r'categorical'], 'L10916 *the precondition §D.1 states*'), ('E.4.1', [r'eight', r'enumerat'], 'E.1.1'), ('E.4', [r'eight'], 'E.1.1 *eight at E.4*'),
                        ('E.3', [r'in full'], 'E.1.1'), ('E.8', [r'closed'], 'E.1.1'), ('E.2', [r'§23\.10'], 'E.1.1'), ('F.3.1', [r'count', r'prose', r'nine stable|stable cells|nine'], 'L10965 / L10955'), ('F.3', [r'refuted|dead|extent'], 'L11025 *F.3\'s rule*'),
                        ('F.3.3', [r'nine', r'stable'], 'register 371 names F.3.3 (E.1.2 row M says F.3.1)')):
    h, d = let_hits(tag, pats); print('   %-6s %s %s — %s' % (tag, h, d, note))
print('   `### E.4` heading (parent of E.4.1 / E.4.2):', lettered(M, 'E.4'), '; `#### ` lines in the whole appendix:', sum(1 for i in range(s, lettered(M, 'Appendix F')[-1]) if M[i - 1].startswith('#### ')))
print('   P19 sites in the volume:', [i for i, l in enumerate(M, 1) if re.search(r'\bP19\b', l)][:8], '; *Q(X) = ∅* sites:', [i for i, l in enumerate(M, 1) if 'Q(X) = ∅' in l][:8])

# §4 the short cited sections and the located claim sites, PRINTED (a short cited section is printed, not probed)
def pr(lo, hi, tag):
    print('   --- %s L%d–L%d' % (tag, lo, hi))
    for i in range(lo, hi + 1): print('   L%d %s' % (i, M[i - 1][:160]))
print('§4 printed sites:')
b = body_range(M, '26.6'); pr(b[0], b[1] - 1, '§26.6 (E.2 cites it for the accelerator identity and Richardson)')
b = body_range(M, '29.8'); pr(b[0], b[1] - 1, '§29.8 (E.2 cites it for the Gröbner basis of eight)')
b = body_range(M, '23.11'); pr(b[0], b[1] - 1, '§23.11 (E.2 cites it for *no interior optimum*)')
pr(_L('| 1 | 499 | **499** | 19 | 25.96 cm⁻¹ |'), _L(" **Which supersedes §25.5's 1,061 order-1 bounds:** the same data at matched order yields 34 bounds at 0.0164 cm⁻¹, **and 619 refusals that are themselves perturbation detections this book did not count.**"), '§23.10.4 (1,585-fold, 25.96, 0.0164)'); pr(_L(' of §23.10.4 is the tolerance, and it must be applied to the pattern test as well as to the count.', 1), _L(' climb is σ.', 1), '§23.12 (interior optimum)'); pr(_L('  40        10⁻⁴      2                     2.75 × 10⁻²                 4.0 × 10⁻³'), _L('      computable per cell from the data alone.'), '§23.12 (admissibility cap)')
pr(_L('### 30.4.1 And the audit itself was run once'), _L(' was ever audited against any list.'), '§30.4.1 (Gröbner, (p−1), F(−1) = 2)'); pr(_L('  sequence acceleration          (Δx)²/Δ²x — Aitken 1926, Seki Kōwa           λ², and a new result'), _L('  optimisation                   λ² = f′²/f″, Nesterov 1994                   w·V = 8λ²;'), '§29.7 (Richardson)'); pr(_L(' **And the general form is the tree, not the constraint.** Four statistical measures of a constraint — leaf position, load, marginal contribution, activity — all failed to predict A. **A measure of the *tree* succeeds:**'), _L('    A/fibre) = −0.942, median error 7%, worst 24%.'), '§16.8.4 (0.972 − 0.154 · descendants)')
for n, pat in ((_L(' shown identical across a twenty-eight-fold range in cell count.', 1), r'518'), (_L(' antichain, or fail to — run at last past three coordinates, and the one underived number in Part II'), r'518')): print('   Register L%d: %s' % (n, R[n - 1][:220]))
pr(_L('    **The language a question is posed in bounds whether it can close, and at what cost.**', 1), _L(' timing, because it has no algorithm.** The documentary language — *has anyone said this before?* —'), '§20.1 (Gröbner)'); pr(_L(' used.'), _L(' **61. "Six relations reduce to eight generators, so −2 were redundant."** A Gröbner basis is routinely *larger* than its input. The redundancy measure is the reduction test, not the count.', 1), '§28.7.1 (Gröbner)')
b = body_range(M, '32.1.4'); pr(b[0], b[1] - 1, '§32.1.4 (cited for ℛ(X) ⊆ ∏ Aᵢ(X) / cannot be repaired from inside)')
b = section_span(M, '32.1.1'); print('   §32.1.1 span L%d–L%d numbered-flag lines:' % (b[0], b[1] - 1), [(i, M[i - 1].strip()[:80]) for i in range(*b) if re.match(r'^\s*(\*\*)?\d\.', M[i - 1]) or re.search(r'\bflag\b', M[i - 1], re.I)][:8])
for lab, pat in (('#P', r'#P'), ('assert the law', r'assert the law'), ('A^m identity', r'A\^\*?m\*?\(|A\^m\('), ('N[φ', r'N\[φ'), ('amplification', r'\bamplification\b'), ('E(claim set)', r'E\(claim set\)'), ('closed at eight|at eight', r'closed at eight')):
    print('   %-16s sites (line, section) outside the unit:' % lab, [(i, next((h for j, h in reversed([(j, hh) for j, hh in [(k, mm.group(1)) for k, ll in enumerate(M, 1) for mm in [re.match(r'^#{2,4}\s*(\d+(?:\.\d+)*|[A-G]\.\d+(?:\.\d+)*)\s', ll)] if mm]]) if j <= i), '-')) for i, l in enumerate(M, 1) if re.search(pat, l) and not (s <= i < t)][:8])
print('   `### F.3.n` headings:', [(i, M[i - 1][:70]) for i in range(1, len(M) + 1) if re.match(r'^#{2,4}\s*F\.3(\.\d+)?\s', M[i - 1])])
print('   *E.4* cited in the unit (bare, not E.4.1/E.4.2):', [(i, M[i - 1].strip()[:90]) for i in range(s, t) if re.search(r'\bE\.4(?!\.\d)', M[i - 1])])
print('   PP P10618 *E.4 The grid, read on the current set* in main (any form):', [(i, M[i - 1].strip()[:80]) for i, l in enumerate(M, 1) if 'grid, read on the current set' in l], '; PP lines P10617–P10619:', [P[i - 1].strip()[:80] for i in (_L(' until G did: a result is one element here and many occurrences there. |Λ| = 976 is a single'), _L(" measurement in D.5.2 and appears in G's count fibre wherever it is printed. Clause (iv) is why"), _L(" Theorem 7.1 is absent — withdrawn, and the status coordinate's *withdrawn* value is"))])
print('   *518* anywhere in six volumes:', {n: [i for i, l in enumerate(L.read_member(n).split('\n'), 1) if re.search(r'(?<![\d,.])518(?![\d,])', l)][:6] for n in (
      'The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md', 'The_Method_1_6___Mathematical_Compendium-2.md', 'The_Method_1_6___The_Physics_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Spectra_Compendium-2.md')})
print('   *cells at order 1|order 1* in §23.10 span:', [(i, M[i - 1][:120]) for i in range(*section_span(M, '23.10')) if re.search(r'order 1\b', M[i - 1])][:6])

# §5 first-person, Ruling 45 and Ruling 46 probes (word-bounded; the Roman numeral of a species excluded; *mine* and *myself* carried)
fp = re.compile(r"\b(I|I'm|I've|I'd|me|my|mine|myself|we|us|our|ours|ourselves)\b")
species = re.compile(r'\b[A-Z][a-z]?\s+(I|II|III|IV|V|VI|VII|VIII|IX|X)\b')
hits = [(i, M[i - 1].strip()[:120]) for i in range(s, t) if any(m for m in fp.finditer(M[i - 1]) if not species.search(M[i - 1][max(0, m.start() - 4):m.end()]))]
print('§5 first-person sites:', hits)
r45 = re.compile(r'\b(session|this pass|this build|the build|chat|press|this run|this session)\b', re.I); r46 = re.compile(r'\b(code|script|\.py|register 256\'s code|build\.py)\b')
print('   R45 candidates:', [(i, re.findall(r45, M[i - 1]), M[i - 1].strip()[:90]) for i in range(s, t) if r45.search(M[i - 1])])
print('   R46 candidates:', [(i, re.findall(r46, M[i - 1]), M[i - 1].strip()[:90]) for i in range(s, t) if r46.search(M[i - 1])])

# §6 census rows 1216–1223 (C9 *never*): each line printed with its witness
print('§6 census C9 *never* sites:')
for i in (_L('  E.1.2, as first listed                   13   N, O and P entered, having been named and never entered'), _L(' has depends = no**, which has held at every size and is the only column whose value has never changed.'), _L(" the operator is bounded by the index's own value sets, so it can name a cell the index lacks and never"), _L(' That is register 332 arriving where it is least comfortable — an index names cells and never'), _L('### E.1.5 The fourteenth item, the column that was never printed, and the constraint it killed'), _L(' The domain column above was assigned in the code that computed E(Q) at register 256 and never'), _L(' The code also carried a constraint the page never stated: *obstacle = buildable ⟹ cost ≤ days.*'), _L(' was never resting on it; only the unfibred count was.')): print('   L%d %s' % (i, M[i - 1].strip()[:150]))
print('   *never entered* (L10933) — N, O, P rows in the E.1.2 table:', [k for k in 'NOP' if any(re.match(r'\s*%s\s{2,}' % k, M[i - 1]) for i in range(s, t))],
      '; *has held at every size* (L10979): the depends column is printed in E.1.2?', any('depends' in M[i - 1] for i in range(lettered(M, 'E.1.2')[-1], t) if re.search(r'\s{2,}', M[i - 1]) and M[i - 1].lstrip().startswith('item')))

# §7 wording pairs in the unit (docket 34): six / five recomputations; E.4 / E.4.1; F.3.1 / F.3.3 for item M; seventeen / eleven items
for pat in (r'recomputed (five|six) times', r'(eight|fifteen|thirteen) (at|here)', r'nine stable', r'Eleven items|eleven items', r'the thirteen', r'ten open', r'fourth obstacle|fourth (value|coordinate)'):
    print('   %-32s' % pat, [(i, re.findall(pat, M[i - 1])) for i in range(s, t) if re.search(pat, M[i - 1])])

# §8 attributions in the unit against the References body
refs = body_range(M, '') if False else None
rs = [i for i, l in enumerate(M, 1) if re.match(r'^## References', l)][-1]; RB = '\n'.join(M[rs:])   # LAST hit = body (the first is the contents list)
print('§8 References body from L%d:' % rs, {n: bool(re.search(n, RB)) for n in ('Racah', 'Paschen', 'G[öo]tze', 'Kreuzer', 'Skarke', 'Richardson', 'Gr[öo]bner', 'Ritz')})
print('done')
